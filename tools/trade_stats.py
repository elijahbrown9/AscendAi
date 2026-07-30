"""R-multiple performance ledger — the substance of a Trade-OS dashboard.

Measures every closed trade in R (P&L / planned risk) instead of dollars,
so sizing discipline and stop discipline become visible:
  - a loss beyond -1.0R means the planned stop was not honored (or never set)
  - many tiny +/-0.1R bars in sequence = churn, regardless of dollar total
  - profit factor and payoff ratio stop being distorted by one big position

Planned risk per trade (denominator):
  - explicit stop journaled  -> |entry - stop| x quantity
  - agentic default          -> 50% of premium paid (risk.md standard stop)
  - manual default           -> 3% of position notional (risk.md stop guidance)

Outputs: stat tiles (net R, win rate, avg trade R, avg win/loss R, profit
factor), the trade sequence with per-trade R, plan-violation flags, and a
daily P&L calendar per desk. Reads data/decision_journal.jsonl.

Usage: python3 trade_stats.py [--desk agentic|manual|all]
"""
import argparse, json, os, re
from collections import defaultdict

PATH = os.path.join(os.path.dirname(__file__), "..", "data", "decision_journal.jsonl")

def parse_notional(row):
    """Best-effort dollar notional from size/instrument/entry."""
    size = row.get("size") or ""
    m = re.search(r"\$([\d,]+(?:\.\d+)?)", size.replace("\\", ""))
    if m:
        return float(m.group(1).replace(",", ""))
    m = re.search(r"(\d+(?:\.\d+)?)\s*sh", (row.get("instrument") or "") + " " + size)
    if m:
        return float(m.group(1)) * float(row["entry"])
    m = re.match(r"(\d+)x", size.strip())
    if m and row["desk"] == "agentic":
        return float(m.group(1)) * float(row["entry"]) * 100
    if row["desk"] == "agentic":
        return float(row["entry"]) * 100
    return None

def planned_risk(row):
    stop = row.get("stop")
    if stop not in (None, "", "null"):
        try:
            n = parse_notional(row)
            if n:
                per_unit = abs(float(row["entry"]) - float(stop)) / float(row["entry"])
                return max(per_unit * n, 1e-9)
        except (ValueError, TypeError):
            pass
    n = parse_notional(row)
    if n is None:
        return None
    return n * (0.50 if row["desk"] == "agentic" else 0.03)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--desk", default="all", choices=["agentic", "manual", "all"])
    a = ap.parse_args()

    rows = [json.loads(l) for l in open(PATH) if l.strip()]
    closed = [r for r in rows if r["status"] == "closed"
              and (a.desk == "all" or r["desk"] == a.desk)]
    if not closed:
        print("no closed trades"); return

    seq, skipped = [], 0
    for r in closed:
        risk = planned_risk(r)
        if not risk:
            skipped += 1; continue
        R = r["pnl"] / risk
        seq.append({"id": r["id"], "date": r.get("exit_date", r["date"]),
                    "desk": r["desk"], "ticker": r["ticker"],
                    "pnl": r["pnl"], "risk": risk, "R": R})

    wins = [t for t in seq if t["pnl"] > 0]
    losses = [t for t in seq if t["pnl"] <= 0]
    gross_w = sum(t["pnl"] for t in wins)
    gross_l = abs(sum(t["pnl"] for t in losses))
    net_R = sum(t["R"] for t in seq)
    pf = (gross_w / gross_l) if gross_l else float("inf")

    print(f"=== R LEDGER ({a.desk}) · {len(seq)} closed trades"
          f"{f' · {skipped} skipped (no computable risk)' if skipped else ''} ===")
    print(f"NET RETURN   {net_R:+.2f}R   (${sum(t['pnl'] for t in seq):+,.2f})")
    print(f"WIN RATE     {len(wins)/len(seq):.0%}   ({len(wins)}W / {len(losses)}L)")
    print(f"AVG TRADE    {net_R/len(seq):+.2f}R   "
          f"(avg win {sum(t['R'] for t in wins)/len(wins):+.2f}R / "
          f"avg loss {sum(t['R'] for t in losses)/len(losses):+.2f}R)"
          if wins and losses else "")
    print(f"PROFIT FACTOR {pf:.2f}   (gross +${gross_w:,.0f} / -${gross_l:,.0f})")

    viol = [t for t in seq if t["R"] < -1.0]
    if viol:
        print(f"\nPLAN VIOLATIONS — losses beyond -1.0R (stop not honored/never set):")
        for t in viol:
            print(f"  #{t['id']:>3} {t['ticker']:6s} {t['date']}  {t['R']:+.2f}R  (${t['pnl']:+,.2f} vs ${t['risk']:,.0f} planned)")

    print(f"\nSEQUENCE (oldest -> newest, each closed trade):")
    for t in seq:
        bar_n = min(int(abs(t["R"]) * 8), 40)
        bar = ("+" if t["R"] > 0 else "-") * max(bar_n, 1)
        print(f"  #{t['id']:>3} {t['ticker']:6s} {t['R']:+6.2f}R  {bar}")

    cal = defaultdict(lambda: [0.0, 0])
    for t in seq:
        cal[t["date"]][0] += t["pnl"]; cal[t["date"]][1] += 1
    print(f"\nPROFIT CALENDAR (by exit date):")
    for d in sorted(cal):
        pnl, n = cal[d]
        print(f"  {d}  ${pnl:+9,.2f}  ({n} trade{'s' if n>1 else ''})")

main()
