"""Unified trade-idea ranker — one score from three questions:
  1. Does the MARKET OUTLOOK (today's grade) favor this side?
  2. WHO is making the trade? (author's earned 7d record on the board)
  3. Does the ENVIRONMENT (conditions score) support it?
plus the price/crowd mechanics that were already in trade_ideas.py.

Scoring per idea (ticker+side, board rows merged):
  regime      +3 side matches grade sign · 0 at grade 0 · −3 against grade
  author      +0..+3 best author's leaderboard blend (top-10 scaled); −1 if the
              ONLY backer is on fade-watch (bottom-3 record)
  environment +1 conditions score supports side · −1 opposes (|score|>0.1)
  price       +2 confirming (now>+0.5% since post) · DISQUALIFIED if knife
              (bleeding <−2% with no peak) · 0 flat
  consensus   +1 per extra distinct author (cap +2) · +1 if ≥2 top-10 authors
  crowding    −2 if any row has 4+ co-signs (late consensus)
Tiers: ≥7 STRONG · 4-6 MODERATE · ≤3 WATCH ONLY. Knives never ranked.
Execution filters (budget/delta/earnings/liquidity) still apply at entry —
this ranks CONVICTION, it does not clear trades.

Usage: python3 rank_ideas.py board.json board_7d.json --grade N --env X.XX
"""
import argparse, json, statistics
from datetime import datetime, timezone

ap = argparse.ArgumentParser()
ap.add_argument("board"); ap.add_argument("board7d")
ap.add_argument("--grade", type=int, required=True)
ap.add_argument("--env", type=float, required=True)
a = ap.parse_args()

today = json.load(open(a.board)); seven = json.load(open(a.board7d))
now = datetime.now(timezone.utc)

by = {}
for r in seven["rows"]:
    for rr in [r] + (r.get("crowd") or []):
        h, p = rr.get("author_handle"), rr.get("current_pnl")
        if h and p is not None:
            by.setdefault(h, []).append(p)
ranked_auth = sorted(
    ((h, sum(1 for p in ps if p > 0)/len(ps), statistics.median(ps))
     for h, ps in by.items() if len(ps) >= 3),
    key=lambda x: -(x[1]*max(x[2], 0) + x[2]*0.1))
top10 = [h for h, *_ in ranked_auth[:10]]
fade = {h for h, *_ in sorted(ranked_auth, key=lambda x: x[1]*max(x[2],0)+x[2]*0.1)[:3]}
auth_pts = {h: max(3 - i*0.3, 0.5) for i, h in enumerate(top10)}

groups = {}
for r in today["rows"]:
    k = (r["display_ticker"], r["direction"])
    g = groups.setdefault(k, {"authors": set(), "rows": []})
    g["rows"].append(r)
    for rr in [r] + (r.get("crowd") or []):
        if rr.get("author_handle"): g["authors"].add(rr["author_handle"])

out = []
for (tick, side), g in groups.items():
    best = max(g["rows"], key=lambda r: r.get("shown_now") or 0)
    nowp = best.get("shown_now") or 0
    peak = best.get("shown_peak") or 0
    if nowp < -2 and peak < 1:
        continue                                    # knife: never ranked
    why = []
    s = 0.0
    if a.grade != 0:
        aligned = (side == "long") == (a.grade > 0)
        s += 3 if aligned else -3
        why.append("regime+" if aligned else "REGIME-AGAINST")
    tops_here = [h for h in g["authors"] if h in auth_pts]
    if tops_here:
        pts = max(auth_pts[h] for h in tops_here)
        s += pts; why.append(f"author+{pts:.1f}({sorted(tops_here, key=lambda h:-auth_pts[h])[0]})")
    elif g["authors"] and g["authors"] <= fade:
        s -= 1; why.append("fade-only-backer")
    if abs(a.env) > 0.1:
        env_up = a.env > 0
        s += 1 if (side == "long") == env_up else -1
        why.append("env+" if (side == "long") == env_up else "env-")
    if nowp > 0.5: s += 2; why.append("price+")
    s += min(len(g["authors"]) - 1, 2)
    if len(g["authors"]) > 1: why.append(f"x{len(g['authors'])}traders")
    if len([h for h in g["authors"] if h in top10]) >= 2:
        s += 1; why.append("top10-consensus")
    if any(len(r.get("crowd") or []) >= 4 for r in g["rows"]):
        s -= 2; why.append("CROWDED")
    tier = "STRONG" if s >= 7 else ("MODERATE" if s >= 4 else "WATCH ONLY")
    out.append((s, tier, tick, side, nowp, why))

out.sort(key=lambda x: -x[0])
print(f"RANKED IDEAS · grade {a.grade:+d} · env {a.env:+.2f} · knives excluded\n")
print(f"{'SCORE':>6s}  {'TIER':11s}{'TICKER':8s}{'SIDE':6s}{'NOW':>7s}  COMPONENTS")
for s, tier, tick, side, nowp, why in out[:12]:
    print(f"{s:>+6.1f}  {tier:11s}{tick:8s}{side:6s}{nowp:>+6.1f}%  {', '.join(why)}")
