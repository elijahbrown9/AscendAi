#!/usr/bin/env python3
"""After-hours pump study: does a non-earnings after-hours move carry into the next day?

Inputs (all saved get_equity_historicals / get_earnings_calendar results):
  --ext   4hour bars with bounds=24_5 (sessions: overnight / pre / reg / post)
  --daily day bars, regular session (official open/close)
  --earn  get_earnings_calendar results (used to drop earnings-driven moves)
  --retail SYM ...  names to tag as the "retail" group (everything else is "other")

During EDT the 4hour grid lines up with the sessions exactly:
  20:00Z bar = 4-8pm ET post-market; 00:00Z / 04:00Z bars = Robinhood 24-hour
  overnight (8pm-4am ET). The study window must therefore stay inside EDT.

For an event day D (non-earnings, |AH move| over the threshold) it measures, from
the 8pm ET post-market close (the price you could actually trade at on Robinhood):
  hold_open   next regular open / 8pm price - 1      (does the pump survive the night?)
  open_close  next close / next open - 1             (does it keep running in the session?)
  hold_close  next close / 8pm price - 1             (buy 8pm, sell next close)
  best        next high / 8pm price - 1              (best exit available next day)
  overnight   4am ET price / 8pm price - 1           (Robinhood 24h session drift)
"""
import argparse, json, statistics as st
from collections import defaultdict
from datetime import date, timedelta


def load_bars(paths):
    out = defaultdict(list)
    for p in paths:
        for r in json.load(open(p))['data']['results']:
            out[r['symbol']].extend(r['bars'])
    return out


def load_earnings(paths):
    rep = defaultdict(set)
    for p in paths:
        for e in json.load(open(p))['data']['results']:
            d = date.fromisoformat(e['report']['date'])
            # A report moves the stock from the session before (pm) through the session after (am).
            for k in (-1, 0, 1):
                rep[e['symbol']].add(d + timedelta(days=k))
    return rep


def stats(xs):
    if not xs:
        return '   n=0'
    up = sum(1 for x in xs if x > 0) / len(xs)
    return (f'n={len(xs):4d}  mean {st.mean(xs)*100:+6.2f}%  median {st.median(xs)*100:+6.2f}%'
            f'  up {up*100:4.0f}%')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--ext', nargs='+', required=True)
    ap.add_argument('--daily', nargs='+', required=True)
    ap.add_argument('--earn', nargs='+', required=True)
    ap.add_argument('--retail', nargs='*', default=[])
    ap.add_argument('--min-dollars', type=float, default=250_000,
                    help='minimum post-market dollar volume for an event to count')
    ap.add_argument('--events', help='write every qualifying event to this JSON file')
    a = ap.parse_args()

    ext, daily, rep = load_bars(a.ext), load_bars(a.daily), load_earnings(a.earn)
    retail = set(a.retail)
    rows = []
    for sym, bars in ext.items():
        if sym not in daily:
            continue
        day = {b['begins_at'][:10]: b for b in daily[sym] if not b.get('interpolated')}
        days = sorted(day)
        nxt = {d: days[i + 1] for i, d in enumerate(days[:-1])}
        post, on = {}, {}
        for b in bars:
            if b.get('interpolated'):
                continue
            t = b['begins_at']
            if b['session'] == 'post' and t[11:13] == '20':
                post[t[:10]] = b
            elif b['session'] == 'overnight' and t[11:13] == '04':
                # 04:00Z on calendar day X closes the overnight that began the ET evening before.
                on[(date.fromisoformat(t[:10]) - timedelta(days=1)).isoformat()] = b
        for d, pb in post.items():
            if d not in day or d not in nxt:
                continue
            n = day[nxt[d]]
            c0 = float(day[d]['close_price'])
            p8 = float(pb['close_price'])
            if c0 <= 0 or p8 <= 0:
                continue
            dd = date.fromisoformat(d)
            earn = dd in rep[sym] or date.fromisoformat(nxt[d]) in rep[sym]
            o1, c1, h1 = (float(n[k]) for k in ('open_price', 'close_price', 'high_price'))
            rows.append(dict(
                sym=sym, date=d, grp='retail' if sym in retail else 'other', earn=earn,
                ah=p8 / c0 - 1, dollars=float(pb['volume']) * p8,
                hold_open=o1 / p8 - 1, open_close=c1 / o1 - 1, hold_close=c1 / p8 - 1,
                best=h1 / p8 - 1, cc=c1 / c0 - 1,
                overnight=(float(on[d]['close_price']) / p8 - 1) if d in on else None))

    clean = [r for r in rows if not r['earn'] and r['dollars'] >= a.min_dollars]
    print(f'{len(ext)} symbols, {len(rows)} symbol-nights, {sum(r["earn"] for r in rows)} earnings nights dropped,'
          f' {len(clean)} clean nights with post-market dollar volume >= ${a.min_dollars:,.0f}')
    print(f'window {min(r["date"] for r in rows)} -> {max(r["date"] for r in rows)}\n')

    base = [r for r in clean if abs(r['ah']) < 0.01]
    print('BASELINE (quiet nights, |AH| < 1%)')
    for k in ('hold_open', 'open_close', 'hold_close'):
        print(f'  {k:11s} {stats([r[k] for r in base])}')

    buckets = [('AH pump +3% to +5%', 0.03, 0.05), ('AH pump +5% to +10%', 0.05, 0.10),
               ('AH pump > +10%', 0.10, 9), ('AH dump -3% to -5%', -0.05, -0.03),
               ('AH dump < -5%', -9, -0.05)]
    for grp in ('all', 'retail', 'other'):
        sel = clean if grp == 'all' else [r for r in clean if r['grp'] == grp]
        print(f'\n=== {grp.upper()} ===')
        for name, lo, hi in buckets:
            ev = [r for r in sel if lo <= r['ah'] < hi]
            print(f'{name}  ({len(ev)} events)')
            if not ev:
                continue
            for k in ('hold_open', 'open_close', 'hold_close', 'best'):
                print(f'  {k:11s} {stats([r[k] for r in ev])}')
            ov = [r['overnight'] for r in ev if r['overnight'] is not None]
            print(f'  {"overnight":11s} {stats(ov)}')

    if a.events:
        ev = sorted((r for r in clean if abs(r['ah']) >= 0.03), key=lambda r: -r['ah'])
        json.dump(ev, open(a.events, 'w'), indent=1)


if __name__ == '__main__':
    main()
