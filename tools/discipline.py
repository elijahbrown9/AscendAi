"""Trade-discipline analyzer.

Input: JSON file(s) from the Robinhood MCP get_pnl_trade_history tool
       ({"data": {"trades": [{symbol, timestamp, realized_gain, ...}]}}).
Output: win/loss stats, per-symbol P&L, and behavioral flags:
  - CHURN:     5+ round trips in one symbol netting negative
  - OVERNIGHT: fills in the overnight session (8pm-4am ET), where spreads widen
  - REVENGE:   3+ consecutive losses in the same symbol within one day

Usage: python3 discipline.py trade_history.json [more.json ...]
"""
import json, sys
from collections import defaultdict
from datetime import datetime, timezone, timedelta

ET = timezone(timedelta(hours=-4))  # EDT; close enough for session bucketing

trades = []
for path in sys.argv[1:]:
    d = json.load(open(path))
    trades += d["data"]["trades"]

if not trades:
    print("No realized trades in window.")
    sys.exit(0)

per_sym = defaultdict(list)
for t in trades:
    g = float(t["realized_gain"])
    ts = datetime.fromisoformat(t["timestamp"].replace("Z", "+00:00"))
    per_sym[t["symbol"]].append((ts, g))

wins = [g for s in per_sym.values() for _, g in s if g > 0]
losses = [g for s in per_sym.values() for _, g in s if g <= 0]
net = sum(wins) + sum(losses)
print(f"Realized net: ${net:+,.2f} over {len(wins)+len(losses)} closed trades "
      f"| win rate {len(wins)/(len(wins)+len(losses)):.0%}")
if wins and losses:
    print(f"Avg win ${sum(wins)/len(wins):.2f} vs avg loss ${sum(losses)/len(losses):.2f} "
          f"(payoff ratio {abs((sum(wins)/len(wins))/(sum(losses)/len(losses))):.2f}x)")

print("\nPer symbol:")
for sym, rows in sorted(per_sym.items(), key=lambda kv: sum(g for _, g in kv[1])):
    tot = sum(g for _, g in rows)
    print(f"  {sym:6s} {tot:+9.2f}  ({len(rows)} trades)")

print("\nBehavioral flags:")
flagged = False
for sym, rows in per_sym.items():
    tot = sum(g for _, g in rows)
    if len(rows) >= 5 and tot < 0:
        flagged = True
        print(f"  CHURN     {sym}: {len(rows)} round trips netting ${tot:+.2f} — ban the ticker for a week after 3 strikes")
    overnight = [1 for ts, _ in rows if not (9 <= ts.astimezone(ET).hour < 20)]
    if len(overnight) >= 3:
        flagged = True
        print(f"  OVERNIGHT {sym}: {len(overnight)} fills outside 9am-8pm ET — thin books, wide spreads")
    by_day = defaultdict(list)
    for ts, g in sorted(rows):
        by_day[ts.date()].append(g)
    for day, gains in by_day.items():
        run = 0
        for g in gains:
            run = run + 1 if g <= 0 else 0
            if run >= 3:
                flagged = True
                print(f"  REVENGE   {sym} on {day}: {run}+ consecutive losses same day — step away")
                break
if not flagged:
    print("  none — clean tape")
