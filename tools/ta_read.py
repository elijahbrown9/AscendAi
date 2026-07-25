"""Market Context Read (playbooks.md P1) — computed, not eyeballed.

Input: historicals JSON from get_equity_historicals (daily bars).
Output per symbol: price vs Daily 12/25 EMAs (support/resistance posture),
Stochastic RSI (14,14,3,3) with overbought/oversold state, and the two
nearest swing-pivot levels above and below price. Numbers only — the
narrative read (P1 section 4) is written by the agent from these facts.
No entries, stops, or targets ever.

Usage: python3 ta_read.py <historicals.json>
"""
import json, sys

def ema(vals, n):
    k, e = 2 / (n + 1), vals[0]
    out = [e]
    for v in vals[1:]:
        e = v * k + e * (1 - k); out.append(e)
    return out

def rsi(closes, n=14):
    gains, losses, out = 0.0, 0.0, [None] * len(closes)
    for i in range(1, len(closes)):
        d = closes[i] - closes[i-1]
        g, l = max(d, 0), max(-d, 0)
        if i <= n:
            gains += g; losses += l
            if i == n:
                ag, al = gains / n, losses / n
                out[i] = 100 - 100 / (1 + (ag / al if al else 1e9))
        else:
            ag = (ag * (n - 1) + g) / n; al = (al * (n - 1) + l) / n
            out[i] = 100 - 100 / (1 + (ag / al if al else 1e9))
    return out

def stoch_rsi(closes, n=14, k_s=3, d_s=3):
    r = [x for x in rsi(closes, n) if x is not None]
    raw = []
    for i in range(n, len(r)):
        w = r[i - n:i + 1]
        lo, hi = min(w), max(w)
        raw.append(100 * (r[i] - lo) / (hi - lo) if hi > lo else 50.0)
    sma = lambda a, m: [sum(a[i - m + 1:i + 1]) / m for i in range(m - 1, len(a))]
    k = sma(raw, k_s); d = sma(k, d_s)
    return k[-1], d[-1]

def pivots(highs, lows, wings=2):
    res, sup = [], []
    for i in range(wings, len(highs) - wings):
        if highs[i] == max(highs[i - wings:i + wings + 1]): res.append(highs[i])
        if lows[i] == min(lows[i - wings:i + wings + 1]): sup.append(lows[i])
    return res, sup

d = json.load(open(sys.argv[1]))
for r in d["data"]["results"]:
    bars = [b for b in r["bars"] if not b.get("interpolated")]
    closes = [float(b["close_price"]) for b in bars]
    highs = [float(b["high_price"]) for b in bars]
    lows = [float(b["low_price"]) for b in bars]
    px = closes[-1]
    e12, e25 = ema(closes, 12)[-1], ema(closes, 25)[-1]
    posture = ("ABOVE both EMAs -> they act as SUPPORT" if px > max(e12, e25)
               else "BELOW both EMAs -> they act as RESISTANCE" if px < min(e12, e25)
               else "BETWEEN the EMAs -> contested, no clean posture")
    k, dd = stoch_rsi(closes)
    state = "OVERBOUGHT (>80)" if k > 80 else "OVERSOLD (<20)" if k < 20 else "mid-range"
    res, sup = pivots(highs, lows)
    res_near = sorted({round(x, 2) for x in res if x > px})[:2]
    sup_near = sorted({round(x, 2) for x in sup if x < px}, reverse=True)[:2]
    print(f"\n=== {r['symbol']}  last {px:.2f} ===")
    print(f"  EMA12 {e12:.2f} | EMA25 {e25:.2f} -> {posture}")
    print(f"  StochRSI %K {k:.0f} %D {dd:.0f} -> {state}")
    print(f"  Nearest resistance (swing pivots): {res_near or 'none above in lookback'}")
    print(f"  Nearest support   (swing pivots): {sup_near or 'none below in lookback'}")
