"""Weekly author re-evaluation — trader ranks earn tenure, they don't coast.

Every Friday close: snapshot the 7d leaderboard into data/author_history.jsonl,
then report movers vs prior weeks. Rank is re-earned weekly from the board's
own record; TRUSTED status (top-10 for 2+ consecutive weeks) is what
rank_ideas.py should weight hardest, one hot week is just a hot week, and a
trader who drops out of the top-10 loses the weight immediately.

Commands:
  log <board_7d.json>    snapshot this week's leaderboard (run Friday close)
  report                 streaks, promotions, demotions, TRUSTED list
"""
import json, os, statistics, sys
from datetime import datetime, timezone

PATH = os.path.join(os.path.dirname(__file__), "..", "data", "author_history.jsonl")

def leaderboard(seven):
    by = {}
    for r in seven["rows"]:
        for rr in [r] + (r.get("crowd") or []):
            h, p = rr.get("author_handle"), rr.get("current_pnl")
            if h and p is not None:
                by.setdefault(h, []).append(p)
    return sorted(
        ((h, len(ps), sum(1 for p in ps if p > 0)/len(ps), statistics.median(ps))
         for h, ps in by.items() if len(ps) >= 3),
        key=lambda x: -(x[2]*max(x[3], 0) + x[3]*0.1))

def cmd_log(f):
    lb = leaderboard(json.load(open(f)))
    week = datetime.now(timezone.utc).date().isoformat()
    os.makedirs(os.path.dirname(PATH), exist_ok=True)
    with open(PATH, "a") as out:
        for rank, (h, n, hit, med) in enumerate(lb, 1):
            out.write(json.dumps({"week": week, "rank": rank, "handle": h,
                                  "n": n, "hit": round(hit, 3),
                                  "median": round(med, 2)}) + "\n")
    print(f"logged {len(lb)} authors for week ending {week}")

def cmd_report():
    if not os.path.exists(PATH):
        print("no history yet — run `log` at a Friday close first"); return
    rows = [json.loads(l) for l in open(PATH) if l.strip()]
    weeks = sorted({r["week"] for r in rows})
    latest = [r for r in rows if r["week"] == weeks[-1]]
    prior_weeks = weeks[:-1]

    streak = {}
    for w in weeks:
        top = {r["handle"] for r in rows if r["week"] == w and r["rank"] <= 10}
        for h in top:
            streak[h] = streak.get(h, 0) + 1 if h in streak else 1
        for h in list(streak):
            if h not in top: streak[h] = 0

    print(f"AUTHOR RE-EVALUATION — {len(weeks)} weekly snapshot(s), latest {weeks[-1]}\n")
    print(f"{'RANK':>4s}  {'TRADER':22s}{'IDEAS':>6s}{'HIT':>6s}{'MEDIAN':>8s}  STATUS")
    for r in sorted(latest, key=lambda x: x["rank"])[:12]:
        s = streak.get(r["handle"], 0)
        tag = ("TRUSTED (top-10 x%d wks)" % s if s >= 2 and r["rank"] <= 10
               else "top-10, wk 1 — not yet trusted" if r["rank"] <= 10
               else "")
        print(f"{r['rank']:>4d}  @{r['handle']:21s}{r['n']:>6d}{r['hit']:>6.0%}"
              f"{r['median']:>+7.1f}%  {tag}")
    if prior_weeks:
        prev_top = {r["handle"] for r in rows if r["week"] == prior_weeks[-1] and r["rank"] <= 10}
        now_top = {r["handle"] for r in latest if r["rank"] <= 10}
        if prev_top - now_top:
            print("\nDEMOTED (weight removed immediately): " +
                  ", ".join("@"+h for h in sorted(prev_top - now_top)))
        if now_top - prev_top:
            print("PROMOTED (probation — trusted after a 2nd week): " +
                  ", ".join("@"+h for h in sorted(now_top - prev_top)))
    else:
        print("\n(first snapshot — everyone is week-1; TRUSTED status starts next Friday)")

{"log": lambda: cmd_log(sys.argv[2]), "report": cmd_report}[sys.argv[1]]()
