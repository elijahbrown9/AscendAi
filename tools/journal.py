"""Decision journal — one line per trade, written AT ENTRY, reviewed monthly.

Each entry records: the thesis, the grade it was placed under, and the
FALSIFIER — the observable fact that would prove the thesis wrong. At close,
the outcome and exit reason are attached. The monthly review then asks the
only two questions that improve a trader:
  1. When the falsifier fired, did we actually exit? (discipline)
  2. Which thesis types and grades make money, and which just feel good?

Commands:
  add    --date --desk agentic|manual --ticker --direction --instrument
         --entry --size --grade --thesis --falsifier [--stop] [--target]
  close  --id N --date --exit --pnl --reason plan_stop|plan_target|
         plan_earnings|plan_expiry|thesis_broken|discretion|drift
  reflect --id N (--clean | --stage execution|management|closure
         --mistake "detail")   # post-trade reflection, playbooks.md P2
  open   (list open entries)
  review [--month YYYY-MM]

Data: data/decision_journal.jsonl. Manual-desk fills found without a journal
entry are added by the check-in as thesis UNRECORDED — the brief then asks
the user for the thesis. An unrecorded thesis is itself a discipline flag.
"""
import argparse, json, os
from collections import defaultdict

PATH = os.path.join(os.path.dirname(__file__), "..", "data", "decision_journal.jsonl")

def load():
    if not os.path.exists(PATH): return []
    return [json.loads(l) for l in open(PATH) if l.strip()]

def save(rows):
    os.makedirs(os.path.dirname(PATH), exist_ok=True)
    with open(PATH, "w") as f:
        for r in rows: f.write(json.dumps(r) + "\n")

def cmd_add(a):
    rows = load()
    rows.append({"id": len(rows) + 1, "date": a.date, "desk": a.desk,
                 "ticker": a.ticker, "direction": a.direction,
                 "instrument": a.instrument, "entry": a.entry, "size": a.size,
                 "grade": a.grade, "thesis": a.thesis, "falsifier": a.falsifier,
                 "stop": a.stop, "target": a.target, "status": "open"})
    save(rows)
    print(f"journaled #{len(rows)}: {a.ticker} {a.direction} — falsifier: {a.falsifier}")

def cmd_close(a):
    rows = load()
    for r in rows:
        if r["id"] == a.id and r["status"] == "open":
            r.update({"status": "closed", "exit_date": a.date, "exit": a.exit,
                      "pnl": a.pnl, "exit_reason": a.reason})
            save(rows)
            print(f"closed #{a.id}: {r['ticker']} pnl {a.pnl:+.2f} ({a.reason})")
            return
    print(f"no open entry #{a.id}")

def cmd_reflect(a):
    rows = load()
    for r in rows:
        if r["id"] == a.id:
            if a.clean:
                r["reflection"] = {"clean": True}
                print(f"#{a.id} {r['ticker']}: reflected — no mistakes claimed")
            else:
                r.setdefault("reflection", {"clean": False, "mistakes": []})
                r["reflection"]["clean"] = False
                r["reflection"].setdefault("mistakes", []).append(
                    {"stage": a.stage, "detail": a.mistake})
                print(f"#{a.id} {r['ticker']}: mistake logged [{a.stage}] {a.mistake}")
            save(rows); return
    print(f"no entry #{a.id}")

def cmd_open(a):
    for r in load():
        if r["status"] == "open":
            print(f"#{r['id']} {r['date']} {r['desk']:7s} {r['ticker']:6s} "
                  f"{r['direction']:5s} @{r['entry']} grade {r['grade']:+d}")
            print(f"    thesis:    {r['thesis']}")
            print(f"    falsifier: {r['falsifier']}")

def cmd_review(a):
    rows = [r for r in load() if r["status"] == "closed"
            and (not a.month or r.get("exit_date", "").startswith(a.month))]
    if not rows: print("no closed entries in window"); return
    n = len(rows); pnl = sum(r["pnl"] for r in rows)
    print(f"{n} closed trades · net {pnl:+.2f}\n")
    print("By exit reason (plan_* = discipline held; drift/discretion = leaks):")
    by = defaultdict(list)
    for r in rows: by[r["exit_reason"]].append(r["pnl"])
    for k, v in sorted(by.items(), key=lambda kv: -sum(kv[1])):
        print(f"  {k:15s} {len(v):2d} trades  net {sum(v):+8.2f}")
    drift = [r for r in rows if r["exit_reason"] in ("drift", "discretion")]
    if drift:
        print(f"\n  DRIFT CHECK: {len(drift)} exits deviated from plan, net "
              f"{sum(r['pnl'] for r in drift):+.2f} — would the plan have done better?")
    print("\nBy grade at entry:")
    byg = defaultdict(list)
    for r in rows: byg[r["grade"]].append(r["pnl"])
    for g in sorted(byg):
        v = byg[g]; print(f"  {g:+d}: {len(v):2d} trades  net {sum(v):+8.2f}")
    print("\nMistakes by lifecycle stage (playbooks P2):")
    stages = defaultdict(list)
    unreflected = 0
    for r in rows:
        ref = r.get("reflection")
        if not ref: unreflected += 1; continue
        for m in ref.get("mistakes", []):
            stages[m["stage"]].append((r["ticker"], m["detail"]))
    if stages:
        for st, ms in sorted(stages.items(), key=lambda kv: -len(kv[1])):
            print(f"  {st:11s} {len(ms)} mistake(s)")
            for t, det in ms: print(f"     {t}: {det}")
        top = max(stages.items(), key=lambda kv: len(kv[1]))
        print(f"  >> pattern: mistakes cluster in {top[0].upper()} — train there first")
    else:
        print("  none logged")
    if unreflected:
        print(f"  ({unreflected} closed trades not yet reflected on — run the P2 questions)")
    unrec = [r for r in rows if "UNRECORDED" in r["thesis"]]
    if unrec:
        print(f"\n  {len(unrec)} trades closed with UNRECORDED thesis, net "
              f"{sum(r['pnl'] for r in unrec):+.2f} — trades without a written "
              "reason are bets, not decisions.")

p = argparse.ArgumentParser()
sub = p.add_subparsers(dest="cmd", required=True)
pa = sub.add_parser("add")
for k in ("date", "desk", "ticker", "direction", "instrument", "thesis", "falsifier"):
    pa.add_argument(f"--{k}", required=True)
pa.add_argument("--entry", type=float, required=True)
pa.add_argument("--size", required=True)
pa.add_argument("--grade", type=int, required=True)
pa.add_argument("--stop"); pa.add_argument("--target")
pc = sub.add_parser("close")
pc.add_argument("--id", type=int, required=True)
pc.add_argument("--date", required=True)
pc.add_argument("--exit", type=float, required=True)
pc.add_argument("--pnl", type=float, required=True)
pc.add_argument("--reason", required=True,
                choices=["plan_stop", "plan_target", "plan_earnings",
                         "plan_expiry", "thesis_broken", "discretion", "drift"])
pf = sub.add_parser("reflect")
pf.add_argument("--id", type=int, required=True)
pf.add_argument("--clean", action="store_true")
pf.add_argument("--stage", choices=["execution", "management", "closure"])
pf.add_argument("--mistake")
po = sub.add_parser("open")
pr = sub.add_parser("review")
pr.add_argument("--month", default=None)
a = p.parse_args()
if a.cmd == "reflect" and not a.clean and not (a.stage and a.mistake):
    p.error("reflect needs --clean or both --stage and --mistake")
{"add": cmd_add, "close": cmd_close, "reflect": cmd_reflect,
 "open": cmd_open, "review": cmd_review}[a.cmd](a)
