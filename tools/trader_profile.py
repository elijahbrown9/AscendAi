"""Trader psychology profile — mechanical tagging of the decision journal.

This does NOT try to grade trades on P&L (journal.py review already does
that). It tags each entry against risk.md and the trader's OWN written plan,
so patterns in how decisions get made are visible across weeks, not just
whether they made money. The weekly synthesis (what the pattern MEANS) is
a judgment call made at Friday review, not hardcoded here — this script only
surfaces evidence.

Flags:
  LATE_THESIS     - thesis contains "backfilled" or "UNRECORDED": written
                    after entry, not at the moment of the decision.
  USER_CONVICTION - thesis text attributes the call to the user's own read
                    ("User:", "user macro call", "user doubled down") rather
                    than a system signal (board/GARCH/grade).
  SIZE_OVERRIDE   - manual-desk size exceeds the 3-unit hard cap (risk.md);
                    agentic premium-at-risk falls outside the $20-60 band.
  UNREFLECTED     - closed trade with no P2 reflection logged yet.

Usage: python3 trader_profile.py [decision_journal.jsonl]
"""
import json, re, sys, os
from collections import defaultdict

PATH = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
    os.path.dirname(__file__), "..", "data", "decision_journal.jsonl")

HARD_CAP_UNITS = 3.0
AGENTIC_BUDGET = (20, 60)

rows = [json.loads(l) for l in open(PATH) if l.strip()]

def manual_units(size_str):
    m = re.search(r"~?([\d.]+)\s*u", size_str or "", re.I)
    return float(m.group(1)) if m else None

def agentic_contracts(size_str):
    m = re.match(r"(\d+)x", (size_str or "").strip())
    return int(m.group(1)) if m else 1

flags = defaultdict(list)
for r in rows:
    tag = f"#{r['id']} {r['ticker']}"
    thesis = r.get("thesis", "")

    if "backfilled" in thesis.lower() or "UNRECORDED" in thesis:
        flags["LATE_THESIS"].append(tag)

    if re.search(r"\buser[: ]", thesis, re.I) and "backfilled" not in thesis.lower():
        flags["USER_CONVICTION"].append(tag)

    if r["desk"] == "manual":
        u = manual_units(r.get("size", ""))
        if u is not None and u > HARD_CAP_UNITS:
            flags["SIZE_OVERRIDE"].append(f"{tag} — {u}u vs {HARD_CAP_UNITS}u hard cap")
    elif r["desk"] == "agentic":
        c = agentic_contracts(r.get("size", ""))
        premium = r["entry"] * c * 100
        if not (AGENTIC_BUDGET[0] <= premium <= AGENTIC_BUDGET[1]):
            flags["SIZE_OVERRIDE"].append(f"{tag} — ${premium:.0f} premium vs ${AGENTIC_BUDGET[0]}-{AGENTIC_BUDGET[1]} band")

    if r["status"] == "closed" and "reflection" not in r:
        flags["UNREFLECTED"].append(f"{tag} (pnl {r['pnl']:+.2f})")

print(f"{len(rows)} journal entries scanned ({sum(1 for r in rows if r['status']=='closed')} closed)\n")
for name in ("LATE_THESIS", "USER_CONVICTION", "SIZE_OVERRIDE", "UNREFLECTED"):
    items = flags[name]
    print(f"{name} ({len(items)}):")
    for it in items:
        print(f"  {it}")
    print()

reflected_closed = [r for r in rows if r["status"] == "closed" and "reflection" in r]
unrefl_wins = [r for r in rows if r["status"] == "closed" and "reflection" not in r and r["pnl"] > 0]
unrefl_losses = [r for r in rows if r["status"] == "closed" and "reflection" not in r and r["pnl"] <= 0]
print(f"Reflection asymmetry: {len(unrefl_wins)} unreflected winning trade(s) vs "
      f"{len(unrefl_losses)} unreflected losing trade(s) — reflection that only "
      f"happens after losses can't tell a good process from a lucky one.")
