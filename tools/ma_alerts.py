#!/usr/bin/env python3
"""ma_alerts.py — moving-average buy alerts on the names the trader actually makes money in.

Backtested 4 Nov 2026 on 16 of the trader's own equities + BTC/ZEC/STRK/HYPE (2 years of daily bars,
2 ATR stop, 2R target, 15-day max hold). Baseline (buy any day): +0.18R/trade.
  TREND DIP      close > 50d > 200d, 50d rising over 20 days, RSI(2) < 5  -> +0.59R, 74% hit (34 signals)
  TREND DIP (wk) same but RSI(2) < 10                                      -> +0.33R, 57% hit (88)
  BREAKOUT       close at a 20-day closing high, 50d > 200d                -> +0.35R, 50% hit (251)
Did NOT beat baseline: touching the 20 EMA or 50 SMA, 20/50 crossovers, dips below the 200d (+0.04R).
In-sample, small samples, names chosen because they worked — treat as a filter, not a guarantee.

Usage:
  python3 tools/ma_alerts.py --hist FILE [FILE ...] [--crypto DIR] [--px SYM:PRICE ...]
         [--equity 24083] [--grade -1] [--earnings SYM:YYYY-MM-DD ...] [--late] [--dry-run]
--hist: saved get_equity_historicals results (interval=day, >= ~260 bars).
--crypto: directory of hyperliquid 1d candleSnapshot files named COIN.json.
--px: live prices; today's price is used as a provisional close (alerts say "confirm at close"
      unless --late, which is the 3:40pm run).
Dedupes per symbol+setup per day in data/alerts/ma-DATE.json. Prints one line per NEW alert,
or "NO MA ALERTS".
"""
import argparse, datetime as dt, json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAMES = os.path.join(ROOT, 'data', 'my_names.json')
STATS = {'TREND DIP': '+0.59R, 74% hit', 'TREND DIP (watch)': '+0.33R, 57% hit', 'BREAKOUT': '+0.35R, 50% hit'}


def ema(v, n):
    k = 2 / (n + 1); o = []; e = None
    for x in v:
        e = x if e is None else x * k + e * (1 - k); o.append(e)
    return o


def sma(v, n):
    return [None if i < n - 1 else sum(v[i - n + 1:i + 1]) / n for i in range(len(v))]


def rsi(v, n):
    o = [None] * len(v); g = l = 0.0
    for i in range(1, len(v)):
        ch = v[i] - v[i - 1]; up = max(ch, 0); dn = max(-ch, 0)
        if i <= n: g += up / n; l += dn / n
        else: g = (g * (n - 1) + up) / n; l = (l * (n - 1) + dn) / n
        if i >= n: o[i] = 100.0 if l == 0 else 100 - 100 / (1 + g / l)
    return o


def atr(b, n=14):
    tr = [b[0][2] - b[0][3]] + [max(b[i][2] - b[i][3], abs(b[i][2] - b[i - 1][4]), abs(b[i][3] - b[i - 1][4])) for i in range(1, len(b))]
    return ema(tr, n)


def load(args):
    data = {}
    for f in args.hist or []:
        for r in json.load(open(f))['data']['results']:
            data[r['symbol']] = [(x['begins_at'][:10], float(x['open_price']), float(x['high_price']), float(x['low_price']), float(x['close_price'])) for x in r['bars'] if not x.get('interpolated')]
    if args.crypto:
        for fn in os.listdir(args.crypto):
            if fn.endswith('.json'):
                d = json.load(open(os.path.join(args.crypto, fn)))
                if isinstance(d, list) and d:
                    data[fn[:-5] + '-USD'] = [(dt.datetime.utcfromtimestamp(x['t'] / 1000).strftime('%Y-%m-%d'), float(x['o']), float(x['h']), float(x['l']), float(x['c'])) for x in d]
    return data


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--hist', nargs='*'); ap.add_argument('--crypto'); ap.add_argument('--px', nargs='*', default=[])
    ap.add_argument('--equity', type=float, default=24000); ap.add_argument('--grade', type=int, default=0)
    ap.add_argument('--earnings', nargs='*', default=[]); ap.add_argument('--late', action='store_true')
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--status', action='store_true', help='print every name\'s trend state and what would trigger a signal')
    a = ap.parse_args()
    cfg = json.load(open(NAMES))
    today = (dt.datetime.utcnow() - dt.timedelta(hours=5)).date()  # ET (EST)
    banned = {s for s, until in cfg.get('banned', {}).items() if today.isoformat() <= until}
    px = {k.upper(): float(v) for k, v in (p.split(':') for p in a.px)}
    earn = {k.upper(): v for k, v in (e.split(':') for e in a.earnings)}
    if a.grade <= -2:
        print('NO MA ALERTS (grade -2: no long entries)'); return
    unit = a.equity * 0.10 * (0.5 if a.grade == -1 else 1.0)
    data = load(a)
    out = []
    for sym, b in data.items():
        if sym not in cfg['names'] or sym in banned or len(b) < 205:
            continue
        b = list(b)
        today_s = today.isoformat()
        if sym in px:
            p = px[sym]
            if b[-1][0] == today_s:
                o, h, l, _ = b[-1][1:5]; b[-1] = (today_s, o, max(h, p), min(l, p), p)
            else:
                b.append((today_s, p, p, p, p))
        c = [x[4] for x in b]; s50 = sma(c, 50); s200 = sma(c, 200); r2 = rsi(c, 2); A = atr(b)
        i = len(b) - 1
        if not (s50[i] and s200[i] and s50[i - 20]):
            continue
        if a.status:
            if c[i] > s50[i] > s200[i]:
                need = f'UPTREND: buy a dip to RSI2<5 (holding above {s50[i]:.2f}) or a close above {max(c[i-20:i]):.2f}'
            elif s50[i] > s200[i]:
                need = f'needs a close back above the 50d {s50[i]:.2f}'
            else:
                need = f'downtrend: 50d {s50[i]:.2f} below 200d {s200[i]:.2f} - no MA buy until the 50d turns back over the 200d'
            print(f'{sym:9s} {c[i]:10.4g}  50d {s50[i]:10.4g}  200d {s200[i]:10.4g}  RSI2 {r2[i]:3.0f}  -> {need}')
            continue
        uptrend = c[i] > s50[i] > s200[i]
        setup = None
        if uptrend and s50[i] > s50[i - 20] and r2[i] is not None and r2[i] < 5:
            setup = 'TREND DIP'
        elif uptrend and r2[i] is not None and r2[i] < 10:
            setup = 'TREND DIP (watch)'
        elif s50[i] > s200[i] and c[i] >= max(c[i - 20:i]):
            setup = 'BREAKOUT'
        if not setup:
            continue
        ed = earn.get(sym.replace('-USD', ''))
        if ed and 0 <= (dt.date.fromisoformat(ed) - today).days <= 5:
            continue
        stop = c[i] - 2 * A[i]; tgt = c[i] + 4 * A[i]
        risk = c[i] - stop
        qty = unit / c[i]
        qtxt = f'{qty:.4f}' if sym.endswith('-USD') else f'{int(qty)}'
        prov = '' if (a.late or sym not in px) else ' (intraday, confirm at the close)'
        why = cfg['names'][sym]
        out.append((sym, setup, f'MA BUY {setup}: {sym} {c[i]:.2f}{prov}. 50d {s50[i]:.2f} / 200d {s200[i]:.2f}, RSI2 {r2[i]:.0f}. '
                              f'{"Half" if a.grade == -1 else "1"} unit = {qtxt} sh, stop {stop:.2f} (2 ATR), target {tgt:.2f} (2R). '
                              f'Backtest {STATS[setup]}. Your record: {why}'))
    if a.status:
        return
    fn = os.path.join(ROOT, 'data', 'alerts', f'ma-{today.isoformat()}.json')
    seen = json.load(open(fn)) if os.path.exists(fn) else {}
    new = [o for o in out if f'{o[0]}|{o[1]}' not in seen]
    rank = {'TREND DIP': 0, 'BREAKOUT': 1, 'TREND DIP (watch)': 2}
    new.sort(key=lambda o: rank[o[1]])
    if not new:
        print('NO MA ALERTS'); return
    for o in new:
        print(o[2]); seen[f'{o[0]}|{o[1]}'] = dt.datetime.now().isoformat(timespec='minutes')
    if not a.dry_run:
        os.makedirs(os.path.dirname(fn), exist_ok=True); json.dump(seen, open(fn, 'w'), indent=1)


if __name__ == '__main__':
    main()
