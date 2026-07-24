"""Composite risk-regime scorer.

Inputs (JSON on stdin or as file arg):
{
  "garch": {"spy_ratio": 0.90, "qqq_ratio": 1.05},   # current vol / long-run vol
  "conditions": {"vix": 18.79, "brent": 100.4, "kospi": 6690.6,
                  "btc_24h_pct": -1.3, "geo_risk": true},
  "board_skew": {"long_avg_now": -2.3, "short_avg_now": 1.7},
  "x_sentiment": null                                  # -1..1 or null if offline
}
Output: per-input scores, composite, and the grade per strategy.md.
"""
import json, sys

d = json.load(open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin)

def clamp(v, lo=-1.0, hi=1.0):
    return max(lo, min(hi, v))

# --- Storm gauge (weight 3). ratio <0.8 CALM(+1) · 0.8-1.25 NORMAL(0) · >1.25 STORM(-1)
def regime_score(r):
    if r < 0.8:  return 1.0
    if r > 1.25: return -1.0
    return round((1.025 - r) / 0.225 * 0.5, 2)   # gentle slope inside NORMAL

g = d["garch"]
garch_scores = [regime_score(g["spy_ratio"]), regime_score(g["qqq_ratio"])]
garch = clamp(sum(garch_scores) / len(garch_scores))
storm_veto = all(r > 1.25 for r in (g["spy_ratio"], g["qqq_ratio"]))

# --- Conditions panel (weight 2): each sub-input -1/0/+1, averaged
c = d["conditions"]
subs = []
subs.append(-1 if c["vix"] >= 21 else (-0.5 if c["vix"] >= 19 else 0.5))
subs.append(-1 if c["brent"] >= 92 else (-0.5 if c["brent"] >= 90 else 0.5))
subs.append(-1 if c["kospi"] <= 6450 else (-0.5 if c["kospi"] <= 6700 else 0.5))
subs.append(clamp(c["btc_24h_pct"] / 5.0))
subs.append(-1 if c.get("geo_risk") else 0.5)
conditions = clamp(sum(subs) / len(subs))

# --- Board skew (weight 2): winners long => +, winners short => -
b = d["board_skew"]
edge = b["long_avg_now"] - b["short_avg_now"]      # >0 longs winning
board = clamp(edge / 4.0)

# --- X (weight 1, optional)
x = d.get("x_sentiment")

parts = [(garch, 3), (conditions, 2), (board, 2)] + ([(clamp(x), 1)] if x is not None else [])
composite = sum(s * w for s, w in parts) / sum(w for _, w in parts)

if storm_veto:
    composite = min(composite, -0.5)

def grade(s):
    if s >= 1.2:  return "+2 ULTRA RISK ON"
    if s >= 0.4:  return "+1 RISK ON"
    if s > -0.4:  return "0 MIXED"
    if s > -1.2:  return "-1 RISK OFF"
    return "-2 ULTRA RISK OFF"

print(json.dumps({
    "scores": {"storm_gauge": round(garch, 2), "conditions": round(conditions, 2),
                "board_skew": round(board, 2), "x": x},
    "storm_veto": storm_veto,
    "composite": round(composite, 3),
    "grade": grade(composite * (5/3)),   # scale: max |composite| = 1 -> map to ±5/3 -> grades at ±0.4/±1.2 of scaled
}, indent=2))
