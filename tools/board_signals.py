"""Leading-indicator extraction from the paste.trade board.

The winner skew (who's green now) is COINCIDENT — it describes today.
Leading signals extracted here:
  1. FRESH FLOW  — direction of ideas posted in the last 6h/24h: what sharp
     accounts are positioning for NEXT, before it has paid.
  2. TURN ALARM  — fresh flow direction diverging from winner skew: the crowd
     that was right is being faded by new positioning. React here, not after.
  3. CANDIDATES  — ideas <24h old whose P&L since posting is already POSITIVE
     (price confirms) with early crowd (1-3 co-signs). Momentum, not hope.
  4. KNIFE CATCHES — counter-trend ideas still bleeding since posting, no
     confirmation. Never entered; listed so we know what we're NOT doing.
  5. CROWDED      — ideas with 4+ co-signs: consensus is late; treat as
     contrarian information, not entry signal.

Usage: python3 board_signals.py board.json [now_iso]
Output is data for the regime/momentum process — never auto-executed.
"""
import json, sys
from datetime import datetime, timezone, timedelta

d = json.load(open(sys.argv[1]))
now = (datetime.fromisoformat(sys.argv[2]) if len(sys.argv) > 2
       else datetime.now(timezone.utc))
if now.tzinfo is None:
    now = now.replace(tzinfo=timezone.utc)

def age_h(r):
    t = datetime.fromisoformat(r["created_at"].replace("Z", "+00:00"))
    return (now - t).total_seconds() / 3600

rows = d["rows"]
flat = []
for r in rows:
    flat.append(r)
    flat.extend(r.get("crowd") or [])

def flow(hours):
    f = [r for r in flat if age_h(r) <= hours]
    L = sum(1 for r in f if r["direction"] == "long")
    S = len(f) - L
    return L, S

l6, s6 = flow(6)
l24, s24 = flow(24)
print(f"FRESH FLOW  6h: {l6} long / {s6} short   24h: {l24} long / {s24} short")

longs_now = [r.get("shown_now") or 0 for r in rows if r["direction"] == "long"]
shorts_now = [r.get("shown_now") or 0 for r in rows if r["direction"] == "short"]
skew = "shorts" if (sum(shorts_now)/max(len(shorts_now),1)) > (sum(longs_now)/max(len(longs_now),1)) else "longs"
fresh = "long" if l6 > s6 else ("short" if s6 > l6 else "balanced")
print(f"WINNER SKEW (coincident): {skew} winning · FRESH 6h FLOW (leading): {fresh}")
if (skew == "shorts" and fresh == "long") or (skew == "longs" and fresh == "short"):
    print(">>> TURN ALARM: fresh positioning diverges from today's winners <<<")

def line(r):
    crowd = len(r.get("crowd") or [])
    return (f"  {r['display_ticker']:7s} {r['direction']:5s} "
            f"now {r.get('shown_now') or 0:+6.1f}% peak {r.get('shown_peak') or 0:+6.1f}% "
            f"age {age_h(r):4.1f}h crowd {crowd}  @{r['author_handle']}")

print("\nCONFIRMED CANDIDATES (fresh + price agrees + early crowd):")
cands = [r for r in rows if age_h(r) <= 24 and (r.get("shown_now") or 0) > 0.5
         and 1 <= len(r.get("crowd") or []) <= 3]
for r in sorted(cands, key=lambda r: -(r.get("shown_now") or 0))[:6]:
    print(line(r))
if not cands: print("  none")

print("\nKNIFE CATCHES (bleeding since posting — we do NOT touch these):")
knives = [r for r in rows if (r.get("shown_now") or 0) < -2
          and (r.get("shown_peak") or 0) < 1]
for r in sorted(knives, key=lambda r: (r.get("shown_now") or 0))[:6]:
    print(line(r))
if not knives: print("  none")

print("\nCROWDED (4+ co-signs — late consensus, contrarian info):")
crowded = [r for r in rows if len(r.get("crowd") or []) >= 4]
for r in crowded[:5]:
    print(line(r))
if not crowded: print("  none")
