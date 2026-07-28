"""Grade validation log — does the grade actually predict anything?

Every trading day the pre-open brief appends one record; each new record
backfills the previous one with what actually happened next. After ~40
records, `report` answers: do negative grades precede negative tape, do we
make money on the days the system says we should, and which inputs carry
the signal?

  log    --date --grade --composite --gauge --conditions --board --x
         --spy --qqq --agentic --manual
         (closes = most recent session close at time of logging; account
          values = current; the PREVIOUS record gets its next-day returns
          and P&L backfilled from today's values)
  report [--min 10]

Data: data/grade_log.jsonl, one JSON object per line, append-only.
"""
import argparse, json, os
from collections import defaultdict

PATH = os.path.join(os.path.dirname(__file__), "..", "data", "grade_log.jsonl")

def load():
    if not os.path.exists(PATH): return []
    return [json.loads(l) for l in open(PATH) if l.strip()]

def save(rows):
    os.makedirs(os.path.dirname(PATH), exist_ok=True)
    with open(PATH, "w") as f:
        for r in rows: f.write(json.dumps(r) + "\n")

def cmd_log(a):
    rows = load()
    if rows and rows[-1]["date"] == a.date:
        print(f"already logged {a.date}"); return
    if rows:  # backfill yesterday with today's observed values
        p = rows[-1]
        if p.get("spy") and a.spy:
            p["next_spy_ret"] = round((a.spy / p["spy"] - 1) * 100, 3)
        if p.get("qqq") and a.qqq:
            p["next_qqq_ret"] = round((a.qqq / p["qqq"] - 1) * 100, 3)
        if p.get("agentic") and a.agentic:
            p["next_agentic_pnl"] = round(a.agentic - p["agentic"], 2)
        if p.get("manual") and a.manual:
            p["next_manual_pnl"] = round(a.manual - p["manual"], 2)
    rows.append({"date": a.date, "grade": a.grade, "composite": a.composite,
                 "inputs": {"gauge": a.gauge, "conditions": a.conditions,
                             "board": a.board, "x": a.x},
                 "spy": a.spy, "qqq": a.qqq,
                 "agentic": a.agentic, "manual": a.manual})
    save(rows)
    print(f"logged {a.date} grade {a.grade:+d} ({len(rows)} records)")

def cmd_report(a):
    rows = [r for r in load() if "next_spy_ret" in r]
    if len(rows) < a.min:
        print(f"only {len(rows)} completed records (<{a.min}) — keep collecting; "
              "conclusions now would be noise"); return
    by_grade = defaultdict(list)
    for r in rows: by_grade[r["grade"]].append(r)
    print(f"{len(rows)} completed records\n")
    print(f"{'GRADE':>6s} {'N':>3s} {'AVG SPY+1':>10s} {'AVG QQQ+1':>10s} "
          f"{'AGENTIC P&L':>12s} {'MANUAL P&L':>11s}")
    for g in sorted(by_grade):
        rs = by_grade[g]
        n = len(rs)
        f = lambda k: sum(r.get(k, 0) for r in rs) / n
        print(f"{g:+6d} {n:3d} {f('next_spy_ret'):9.2f}% {f('next_qqq_ret'):9.2f}% "
              f"${f('next_agentic_pnl'):10.2f} ${f('next_manual_pnl'):9.2f}")
    # which inputs correlate with next-day QQQ return (sign agreement rate)
    print("\nInput sign-agreement with next-day QQQ direction:")
    for k in ("gauge", "conditions", "board", "x"):
        pairs = [(r["inputs"].get(k), r.get("next_qqq_ret"))
                 for r in rows if r["inputs"].get(k) is not None]
        pairs = [(i, q) for i, q in pairs if abs(i) > 0.05]
        if not pairs:
            print(f"  {k:10s} insufficient data"); continue
        agree = sum(1 for i, q in pairs if (i > 0) == (q > 0)) / len(pairs)
        print(f"  {k:10s} {agree:.0%} over {len(pairs)} days "
              f"{'(better than coin flip)' if agree > 0.55 else '(no evidence of signal)' if agree < 0.55 else ''}")
    print("\nCaveat: small samples lie. <40 records = suggestive at best.")

p = argparse.ArgumentParser()
sub = p.add_subparsers(dest="cmd", required=True)
pl = sub.add_parser("log")
pl.add_argument("--date", required=True)
pl.add_argument("--grade", type=int, required=True)
pl.add_argument("--composite", type=float, required=True)
for k in ("gauge", "conditions", "board"):
    pl.add_argument(f"--{k}", type=float, required=True)
pl.add_argument("--x", type=float, default=None)
for k in ("spy", "qqq"):
    pl.add_argument(f"--{k}", type=float, required=True)
for k in ("agentic", "manual"):
    pl.add_argument(f"--{k}", type=float, default=None,
                     help="omit when the account's portfolio API is down")
pr = sub.add_parser("report")
pr.add_argument("--min", type=int, default=10)
a = p.parse_args()
cmd_log(a) if a.cmd == "log" else cmd_report(a)
