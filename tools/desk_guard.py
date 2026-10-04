"""Desk guard — rule alerts for the manual desk (account ••••5308, read-only).

Added 2026-10-04 at the user's request after a month of 104 trades / -$4,468
where nine losses of $400+ (-$7,061) and three churned names (ZCSH, DRAM, ETH:
63 trades, -$4,978) did the damage. The agent never trades this account; this
script only turns the risk.md manual-desk rules into push-ready lines.

Usage (the monitor fills these in from get_portfolio / get_equity_positions /
get_equity_quotes / today's filled orders):
  python3 tools/desk_guard.py --equity 22631 --gross 0 --day-pnl -120 \\
      --pos LITE:2:1050:1071 AAOI:20:110:108.2 \\
      --entries LITE:1 AAOI:2 --wide LITE AAOI --core ARKG:49.68 ZCSH:30 \\
      --grade 1 [--dry-run]
  --pos     SYMBOL:QTY:AVG_COST:PRICE for every open position
  --entries SYMBOL:N buy orders filled today per symbol
  --wide    symbols on the wide-vol rule (R = 5%); everything else R = 3%
  --core    SYMBOL:STOP for core holds (no profit ladder; stop only)
Prints one line per NEW alert (<200 chars), or NO DESK ALERTS. Alerts are
recorded once per symbol+kind per Eastern day in data/alerts/desk-DATE.json.
"""
import argparse, json, os
from datetime import datetime, timezone, timedelta

ET = timezone(timedelta(hours=-4))  # EDT
p = argparse.ArgumentParser()
p.add_argument("--equity", type=float, required=True)
p.add_argument("--gross", type=float, default=0.0)
p.add_argument("--day-pnl", type=float, default=0.0)
p.add_argument("--grade", type=int, default=0)
p.add_argument("--pos", nargs="*", default=[])
p.add_argument("--entries", nargs="*", default=[])
p.add_argument("--wide", nargs="*", default=[])
p.add_argument("--core", nargs="*", default=[])
p.add_argument("--dry-run", action="store_true")
a = p.parse_args()

core = {c.split(":")[0]: float(c.split(":")[1]) for c in a.core}
cands = []  # (key, message)

for spec in a.pos:
    sym, qty, avg, px = spec.split(":")
    qty, avg, px = float(qty), float(avg), float(px)
    gain = px / avg - 1
    value = qty * px
    if sym in core:
        if px <= core[sym]:
            cands.append((f"{sym}:core_stop", f"{sym} core stop: ${px:,.2f} is at/below ${core[sym]:,.2f}. Plan says exit in full, then 2 weeks out."))
    else:
        r = 0.05 if sym in a.wide else 0.03
        third = max(1, int(qty // 3))
        if gain >= 2 * r:
            cands.append((f"{sym}:2R", f"{sym} +2R: ${px:,.2f} ({gain:+.1%}). Sell another third ({third} sh), trail the rest."))
        elif gain >= r:
            cands.append((f"{sym}:1R", f"{sym} +1R: ${px:,.2f} ({gain:+.1%}). Sell a third ({third} sh) now and move the stop to ${avg:,.2f}."))
        elif gain <= -r:
            cands.append((f"{sym}:stop", f"{sym} at its stop: ${px:,.2f} ({gain:+.1%}, rule -{r:.0%}). Exit. No re-entry today."))
    if value > 0.30 * a.equity:
        cands.append((f"{sym}:size", f"{sym} is ${value:,.0f} = {value / a.equity:.0%} of equity. Cap is 30% (${0.30 * a.equity:,.0f}). Trim to the cap."))

for spec in a.entries:
    sym, n = spec.split(":")
    if int(n) >= 3:
        cands.append((f"{sym}:churn", f"{sym}: {n} entries today. The cap is 2. This is the churn pattern. Done with {sym} until tomorrow."))

cap = 1.25 if a.grade >= 1 else 1.0
if a.equity > 0 and a.gross / a.equity > cap:
    cands.append(("BOOK:margin", f"Gross {a.gross / a.equity:.2f}x equity; grade {a.grade:+d} allows {cap:.2f}x. Cut back to the cap."))
if a.day_pnl <= -0.02 * a.equity:
    cands.append(("BOOK:dayloss", f"Down ${-a.day_pnl:,.0f} today ({a.day_pnl / a.equity:.1%}). Daily loss limit hit: go flat, done for the day."))

day = datetime.now(timezone.utc).astimezone(ET).strftime("%Y-%m-%d")
path = os.path.join(os.path.dirname(__file__), "..", "data", "alerts", f"desk-{day}.json")
os.makedirs(os.path.dirname(path), exist_ok=True)
sent = json.load(open(path)) if os.path.exists(path) else {}
new = [(k, m) for k, m in cands if k not in sent]
for k, m in new:
    print(m[:199])
    sent[k] = datetime.now(timezone.utc).isoformat()
if not new:
    print("NO DESK ALERTS")
if not a.dry_run:
    json.dump(sent, open(path, "w"), indent=1)
