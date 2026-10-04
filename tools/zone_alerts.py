"""Zone alerts — push when a tactical pick trades inside its buy zone.

Added 2026-10-04 (user: "when you find plays ... notify me so I can buy" and
"find me asymmetric upside ... where you see the money flowing"). Zones live in
data/zones.json with qty, stop and targets. Manual desk ••••5308 is read-only:
this prints guidance, it never trades.

Usage: python3 tools/zone_alerts.py --px AAOI:108.2 SKHY:191 ... [--held AAOI ...]
                                    [--open-slots 3] [--dry-run]
Prints one line per symbol newly inside its zone (<200 chars) or NO ZONE ALERTS.
Each symbol alerts at most once per Eastern day (data/alerts/zones-DATE.json).
Nothing fires after valid_through, or when no tactical slot is open.
"""
import argparse, json, os
from datetime import datetime, timezone, timedelta

ET = timezone(timedelta(hours=-4))  # EDT
here = os.path.dirname(__file__)
p = argparse.ArgumentParser()
p.add_argument("--px", nargs="*", default=[])
p.add_argument("--held", nargs="*", default=[])
p.add_argument("--open-slots", type=int, default=3)
p.add_argument("--dry-run", action="store_true")
a = p.parse_args()

plan = json.load(open(os.path.join(here, "..", "data", "zones.json")))
now = datetime.now(timezone.utc).astimezone(ET)
day = now.strftime("%Y-%m-%d")
px = {s.split(":")[0]: float(s.split(":")[1]) for s in a.px}
out = []
if day <= plan["valid_through"] and a.open_slots > 0:
    for z in plan["zones"]:
        s = z["sym"]
        if s in a.held or s not in px:
            continue
        if z["lo"] <= px[s] <= z["hi"]:
            out.append((s, f"{s} in its buy zone: ${px[s]:,.2f} (zone ${z['lo']:,.2f}-{z['hi']:,.2f}). {z['qty']} sh, stop ${z['stop']:,.2f}, targets ${z['t1']:,.2f} / ${z['t2']:,.2f}. {z['tag']}"))

path = os.path.join(here, "..", "data", "alerts", f"zones-{day}.json")
os.makedirs(os.path.dirname(path), exist_ok=True)
sent = json.load(open(path)) if os.path.exists(path) else {}
new = [(k, m) for k, m in out if k not in sent]
for k, m in new:
    print(m[:199])
    sent[k] = datetime.now(timezone.utc).isoformat()
if not new:
    print("NO ZONE ALERTS")
if not a.dry_run:
    json.dump(sent, open(path, "w"), indent=1)
