"""Core adds — tells the user when to put the next unit into a core hold.

Added 2026-10-04 at the user's request: "for arkg and zcsh i want you to send
me alerts of when to put a unit into either of them." The ladder lives in
data/core_plan.json (levels, max units, whole-position weekly-close stop).
Manual desk ••••5308 is read-only: this prints guidance, it never trades.

Usage (from the hourly monitor):
  python3 tools/core_adds.py --equity 22631 --pos ARKG:0:0:53.80 ZCSH:66:34.1:30.2 [--late] [--dry-run]
  --pos   SYMBOL:QTY:AVG_COST:PRICE for every core name (QTY 0 if not held)
  --late  this is the 3:40pm run: 'close_at_or_above' levels may fire
Prints one line per NEW alert (<200 chars) or NO CORE ALERTS. Each level fires
at most once per Eastern day (data/alerts/core-DATE.json).
"""
import argparse, json, os
from datetime import datetime, timezone, timedelta

ET = timezone(timedelta(hours=-4))  # EDT
here = os.path.dirname(__file__)
p = argparse.ArgumentParser()
p.add_argument("--equity", type=float, required=True)
p.add_argument("--pos", nargs="*", default=[])
p.add_argument("--late", action="store_true")
p.add_argument("--dry-run", action="store_true")
a = p.parse_args()

plan = json.load(open(os.path.join(here, "..", "data", "core_plan.json")))
unit = a.equity * plan["unit_pct"]
out = []
for spec in a.pos:
    sym, qty, avg, px = spec.split(":")
    qty, avg, px = float(qty), float(avg), float(px)
    cfg = plan["names"].get(sym)
    if not cfg:
        continue
    held = round(qty * avg / unit) if qty else 0
    if held >= cfg["max_units"]:
        continue
    for lv in cfg["levels"]:
        if lv["units_before"] != held:
            continue
        if lv["type"] == "at_or_below":
            hit = px <= lv["price"]
            how = f"${px:,.2f} at/below ${lv['price']:,.2f}"
        else:
            hit = a.late and px >= lv["price"]
            how = f"${px:,.2f} into the close, at/above ${lv['price']:,.2f}"
        if hit:
            sh = int(unit // px)
            out.append((f"{sym}:{lv['id']}", f"{sym} add unit {held + 1} of {cfg['max_units']}: {how}. Buy ~{sh} sh (${unit:,.0f}). Stop for the whole position: Friday close below ${cfg['stop_weekly_close']:,.2f}."))
            break

day = datetime.now(timezone.utc).astimezone(ET).strftime("%Y-%m-%d")
path = os.path.join(here, "..", "data", "alerts", f"core-{day}.json")
os.makedirs(os.path.dirname(path), exist_ok=True)
sent = json.load(open(path)) if os.path.exists(path) else {}
new = [(k, m) for k, m in out if k not in sent]
for k, m in new:
    print(m[:199])
    sent[k] = datetime.now(timezone.utc).isoformat()
if not new:
    print("NO CORE ALERTS")
if not a.dry_run:
    json.dump(sent, open(path, "w"), indent=1)
