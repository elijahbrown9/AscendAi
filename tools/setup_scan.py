"""Setup scan — turn scanner hits into tradeable, risk-sized setups.

Added 2026-10-04 (user: "constantly be scanning to find trades"). The monitor
and the post-close scan feed this a get_equity_historicals file (daily bars,
~6 months, up to 10 symbols) for fresh scanner hits. It keeps only names where
the money is moving in (uptrend + accumulation) that still have room to an
old high, and turns each into a buy zone, stop and targets sized to a fixed
dollar risk. Manual desk ••••5308 is read-only: output is guidance only.

Usage:
  python3 tools/setup_scan.py HIST.json --equity 22631 [--risk-pct 0.005]
      [--earnings SYM:YYYY-MM-DD ...] [--skip SYM ...] [--add] [--max 2]
  --earnings  known next report dates; a name reporting within 7 days is dropped
  --skip      names to ignore (held, banned, already in data/zones.json)
  --add       append the passing setups to data/zones.json (7-day expiry)
Every symbol evaluated is logged to data/alerts/scanned-DATE.json so the next
run takes the next batch of scanner hits instead of re-checking the same ten.
Prints "NEW SETUP: ..." lines (<200 chars, push-ready) or NO NEW SETUPS.

Rules (all must pass):
  close > 50-day avg, and either 20-day avg > 50-day avg or a fresh turn
    (close 5%+ over the 20-day avg with buying volume >= 2x selling)  (trend)
  up-day volume / down-day volume over 20 days >= 1.5 (accumulation)
  10-day average dollar volume >= $20M              (liquidity)
  6-month high at least 15% above the zone          (room)
  reward to the 6-month high >= 3x the risk         (asymmetry)
Zone = the 20-day avg or the last 3 days' low, whichever is higher (+3%).
T1 = the 60-day high when it is 10%+ above the zone (the ladder's first sale),
T2 = the 6-month high. Size = fixed dollar risk, capped at 1 unit (10% of
equity) when the name moves >3% a day, else 2 units.
"""
import argparse, json, math, os
from datetime import datetime, timezone, timedelta, date

ET = timezone(timedelta(hours=-4))  # EDT
here = os.path.dirname(__file__)
p = argparse.ArgumentParser()
p.add_argument("hist")
p.add_argument("--equity", type=float, required=True)
p.add_argument("--risk-pct", type=float, default=0.005)
p.add_argument("--earnings", nargs="*", default=[])
p.add_argument("--skip", nargs="*", default=[])
p.add_argument("--add", action="store_true")
p.add_argument("--max", type=int, default=2)
a = p.parse_args()

today = datetime.now(timezone.utc).astimezone(ET).date()
earn = {e.split(":")[0]: date.fromisoformat(e.split(":")[1]) for e in a.earnings}
zpath = os.path.join(here, "..", "data", "zones.json")
zones = json.load(open(zpath))
have = {z["sym"] for z in zones["zones"]} | set(a.skip)
risk_usd = a.equity * a.risk_pct

found = []
results = json.load(open(a.hist))["data"]["results"]
lpath = os.path.join(here, "..", "data", "alerts", f"scanned-{today.isoformat()}.json")
os.makedirs(os.path.dirname(lpath), exist_ok=True)
seen = json.load(open(lpath)) if os.path.exists(lpath) else []
json.dump(sorted(set(seen) | {r["symbol"] for r in results}), open(lpath, "w"))  # evaluated today
for r in results:
    s = r["symbol"]
    if s in have:
        continue
    b = [x for x in r["bars"] if not x.get("interpolated")]
    if len(b) < 60:
        continue
    c = [float(x["close_price"]) for x in b]
    h = [float(x["high_price"]) for x in b]
    l = [float(x["low_price"]) for x in b]
    v = [float(x["volume"]) for x in b]
    last = c[-1]
    sma20, sma50 = sum(c[-20:]) / 20, sum(c[-50:]) / 50
    up = sum(v[i] for i in range(-20, 0) if c[i] > c[i - 1])
    dn = sum(v[i] for i in range(-20, 0) if c[i] < c[i - 1]) or 1
    dollar = sum(c[i] * v[i] for i in range(-10, 0)) / 10
    rr = [math.log(c[i] / c[i - 1]) for i in range(len(c) - 20, len(c))]
    m = sum(rr) / 20
    dvol = (sum((x - m) ** 2 for x in rr) / 19) ** 0.5
    trend = sma20 > sma50 or (last > sma20 * 1.05 and up / dn >= 2.0)
    if not (last > sma50 and trend and up / dn >= 1.5 and dollar >= 20e6):
        continue
    support = max(sma20, min(l[-3:]))
    lo, hi = (support, support * 1.03) if last > support * 1.03 else (last * 0.985, last)
    mid = (lo + hi) / 2
    low10 = min(l[-10:])
    stop = low10 * 0.99 if low10 < lo and (mid - low10 * 0.99) / mid <= 0.12 else lo * 0.93
    t2 = max(h)
    t1 = max(h[-60:]) if max(h[-60:]) / mid >= 1.10 else t2
    risk = mid - stop
    if t2 / mid - 1 < 0.15 or risk <= 0 or (t2 - mid) / risk < 3:
        continue
    if s in earn and 0 <= (earn[s] - today).days <= 7:
        continue
    cap = a.equity * (0.10 if dvol > 0.03 else 0.20)
    qty = int(min(risk_usd // risk, cap // mid))
    if qty < 1:
        continue
    found.append(dict(sym=s, lo=round(lo, 2), hi=round(hi, 2), qty=qty, stop=round(stop, 2),
                      t1=round(t1, 2), t2=round(t2, 2), r1=(t1 - mid) / risk, r2=(t2 - mid) / risk,
                      ud=up / dn, last=last))

found.sort(key=lambda f: -f["r2"])
found = found[: a.max]
for f in found:
    print(f"NEW SETUP: {f['sym']} buy zone ${f['lo']:,.2f}-{f['hi']:,.2f} (now ${f['last']:,.2f}). {f['qty']} sh, stop ${f['stop']:,.2f}, "
          f"T1 ${f['t1']:,.2f} ({f['r1']:.1f}R), T2 ${f['t2']:,.2f} ({f['r2']:.1f}R). Buy vol {f['ud']:.1f}x sell."[:199])
if not found:
    print("NO NEW SETUPS")
if a.add and found:
    exp = (today + timedelta(days=7)).isoformat()
    for f in found:
        zones["zones"].append({"sym": f["sym"], "lo": f["lo"], "hi": f["hi"], "qty": f["qty"], "stop": f["stop"],
                               "t1": f["t1"], "t2": f["t2"], "expires": exp, "added": today.isoformat(),
                               "tag": f"scan {today.isoformat()}: {f['r2']:.1f}R to the 6-month high, buying vol {f['ud']:.1f}x selling"})
    json.dump(zones, open(zpath, "w"), indent=1)
