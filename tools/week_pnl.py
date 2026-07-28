"""Calendar-week P&L — Monday 00:00 through Sunday 23:59, US/Eastern.

The broker's own "week" span is a ROLLING 7 days, which silently drops
early-week winners as later days replace them — the number changes even
though nothing new happened. This computes a fixed calendar week instead:
stable within the week, resets cleanly every Monday.

Usage: python3 week_pnl.py <trades.json> [as_of_iso]
Input: same {"data": {"trades": [{symbol, timestamp, realized_gain}]}}
       shape as discipline.py / get_pnl_trade_history.
"""
import json, sys
from datetime import datetime, timezone, timedelta
from collections import defaultdict

ET = timezone(timedelta(hours=-4))  # EDT; fine for weekly bucketing

trades = json.load(open(sys.argv[1]))["data"]["trades"]
as_of = (datetime.fromisoformat(sys.argv[2]) if len(sys.argv) > 2
         else datetime.now(timezone.utc)).astimezone(ET)
week_start = (as_of - timedelta(days=as_of.weekday())).replace(
    hour=0, minute=0, second=0, microsecond=0)

in_week = []
for t in trades:
    ts = datetime.fromisoformat(t["timestamp"].replace("Z", "+00:00")).astimezone(ET)
    if ts >= week_start:
        in_week.append((ts, t["symbol"], float(t["realized_gain"])))

print(f"Calendar week: Mon {week_start.date()} through {as_of.strftime('%a %Y-%m-%d %H:%M')} ET")
if not in_week:
    print("No realized trades yet this calendar week.")
    sys.exit(0)

net = sum(g for _, _, g in in_week)
wins = [g for _, _, g in in_week if g > 0]
losses = [g for _, _, g in in_week if g <= 0]
print(f"Net: ${net:+,.2f} over {len(in_week)} trades "
      f"({len(wins)}W/{len(losses)}L, win rate {len(wins)/len(in_week):.0%})")

by_sym = defaultdict(float)
for _, sym, g in in_week:
    by_sym[sym] += g
print("\nBy symbol:")
for sym, g in sorted(by_sym.items(), key=lambda kv: -kv[1]):
    print(f"  {sym:6s} {g:+9.2f}")
