"""Cumulative weekly consensus tracker — what keeps earning attention vs
what we actually watched and traded.

Every check-in logs a snapshot of the board's top-trader consensus
(tools/board_signals.py logic). The weekly report then answers the user's
question directly: which names showed QUALITY agreement repeatedly this
week, and of those, which never made our watchlist or book — the gap
between what the best traders kept flagging and what we actually did.

Commands:
  log <board_today.json> <board_7d.json>   append current consensus snapshot
  report [--week-of YYYY-MM-DD]            aggregate the calendar week,
                                           cross-referenced against
                                           watchlist.md + decision journal

Data: data/consensus_week.jsonl (append-only; a new week just filters by date).
"""
import json, os, re, sys, statistics
from datetime import datetime, timezone, timedelta

BASE = os.path.join(os.path.dirname(__file__), "..")
PATH = os.path.join(BASE, "data", "consensus_week.jsonl")

def top_authors(seven):
    by = {}
    for r in seven["rows"]:
        for rr in [r] + (r.get("crowd") or []):
            h, p = rr.get("author_handle"), rr.get("current_pnl")
            if h and p is not None:
                by.setdefault(h, []).append(p)
    ranked = sorted(
        ((h, len(ps), sum(1 for p in ps if p > 0)/len(ps), statistics.median(ps))
         for h, ps in by.items() if len(ps) >= 3),
        key=lambda x: -(x[2] * max(x[3], 0) + x[3] * 0.1))
    return {h for h, *_ in ranked[:10]}

def cmd_log(today_f, seven_f):
    today, seven = json.load(open(today_f)), json.load(open(seven_f))
    tops = top_authors(seven)
    now = datetime.now(timezone.utc).isoformat(timespec="minutes")
    groups = {}
    for r in today["rows"]:
        k = (r["display_ticker"], r["direction"])
        g = groups.setdefault(k, {"authors": set(), "top": set(), "now": 0.0})
        for rr in [r] + (r.get("crowd") or []):
            h = rr.get("author_handle")
            if h:
                g["authors"].add(h)
                if h in tops: g["top"].add(h)
        g["now"] = max(g["now"], r.get("shown_now") or 0)
    n = 0
    os.makedirs(os.path.dirname(PATH), exist_ok=True)
    with open(PATH, "a") as f:
        for (tick, side), g in groups.items():
            if len(g["authors"]) >= 2:
                f.write(json.dumps({"ts": now, "ticker": tick, "side": side,
                                    "n_authors": len(g["authors"]),
                                    "n_top": len(g["top"]),
                                    "top": sorted(g["top"]),
                                    "now_pct": round(g["now"], 2)}) + "\n")
                n += 1
    print(f"logged {n} consensus rows @ {now}")

def cmd_report(week_of=None):
    if not os.path.exists(PATH):
        print("no snapshots yet"); return
    rows = [json.loads(l) for l in open(PATH) if l.strip()]
    anchor = (datetime.fromisoformat(week_of).replace(tzinfo=timezone.utc)
              if week_of else datetime.now(timezone.utc))
    monday = (anchor - timedelta(days=anchor.weekday())).date()
    rows = [r for r in rows
            if datetime.fromisoformat(r["ts"]).date() >= monday]
    if not rows:
        print(f"no snapshots in week of {monday}"); return

    agg = {}
    for r in rows:
        k = (r["ticker"], r["side"])
        a = agg.setdefault(k, {"days": set(), "hits": 0, "max_top": 0,
                               "top": set(), "last_pct": 0})
        a["days"].add(r["ts"][:10]); a["hits"] += 1
        a["max_top"] = max(a["max_top"], r["n_top"])
        a["top"].update(r.get("top") or [])
        a["last_pct"] = r["now_pct"]

    watch = open(os.path.join(BASE, "watchlist.md")).read().upper()
    jpath = os.path.join(BASE, "data", "decision_journal.jsonl")
    traded = {json.loads(l)["ticker"].upper() for l in open(jpath) if l.strip()}

    ranked = sorted(agg.items(),
                    key=lambda kv: (-len(kv[1]["days"]), -kv[1]["max_top"], -kv[1]["hits"]))
    print(f"CUMULATIVE CONSENSUS — week of {monday} · {len(rows)} snapshot rows\n")
    print(f"{'TICKER':8s}{'SIDE':6s}{'DAYS':>4s}{'SEEN':>5s}{'TOP-10':>7s}  {'LAST%':>7s}  STATUS")
    for (tick, side), a in ranked[:15]:
        on_watch = bool(re.search(rf"\b{re.escape(tick)}\b", watch))
        was_traded = tick.upper() in traded
        status = ("TRADED" if was_traded else
                  "on watchlist" if on_watch else
                  ">>> GAP — never watched or traded <<<")
        print(f"{tick:8s}{side:6s}{len(a['days']):>4d}{a['hits']:>5d}{a['max_top']:>7d}  "
              f"{a['last_pct']:>+6.1f}%  {status}")
    gaps = [(t, s) for (t, s), a in ranked
            if len(a["days"]) >= 2
            and not re.search(rf"\b{re.escape(t)}\b", watch)
            and t.upper() not in traded]
    if gaps:
        print("\nSHOULD-BE LIST (multi-day quality consensus we never acted on):")
        for t, s in gaps:
            print(f"  {t} {s} — backed by {', '.join('@'+h for h in sorted(agg[(t,s)]['top'])) or 'board consensus'}")

if sys.argv[1] == "log":
    cmd_log(sys.argv[2], sys.argv[3])
elif sys.argv[1] == "report":
    cmd_report(sys.argv[2] if len(sys.argv) > 2 else None)
