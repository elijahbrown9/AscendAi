# MA buy-signal backtest on the trader's own names — 4 Nov 2026

Universe: MU THYP CRWV SNDK HOOD INTC EWY LIME META AGRO GLD HIMS BE AAOI ONDS ARKG + BTC ZEC STRK HYPE
(the names with positive realized P&L in 1,754 closes). Daily bars Nov 2024 → Nov 2026.
Trade sim: enter at the signal close, stop 2×ATR(14), target 2R, max hold 15 days; 5-day cooldown per name.

| Signal | n | exp R | hit | fwd 10d avg / median |
|---|---|---|---|---|
| Baseline (any day) | 6,122 | +0.18 | 47% | +3.0% / +0.4% |
| TREND DIP: close > 50d > 200d, 50d rising 20d, RSI(2) < 5 | 34 | **+0.59** | **74%** | +7.7% / +5.8% |
| TREND DIP watch: same, RSI(2) < 10 | 88 | +0.33 | 57% | +5.8% / +3.1% |
| BREAKOUT: close at 20-day closing high, 50d > 200d | 251 | +0.35 | 50% | +6.2% / +2.9% |
| 55-day high, above 50d | 230 | +0.37 | 50% | +5.2% / +2.1% |
| Touch of 20 EMA in uptrend | 218 | +0.05 | 40% | +3.3% |
| Touch of 50 SMA in uptrend | 150 | +0.04 | 42% | +0.9% |
| 20 EMA cross-up | 123 | +0.11 | 46% | +1.8% |
| Reclaim of 50 SMA | 103 | +0.14 | 42% | +1.5% |
| Dip while below the 200d (RSI2 < 10) | 186 | +0.04 | 45% | +2.4% / −0.8% |

Read: on these names, buy oversold dips only while the trend is intact, or buy strength at highs.
Simple "it touched the moving average" and catching dips in downtrends add nothing. In-sample,
small n for the best rule, names selected with hindsight — a filter, not a promise. Implemented in
tools/ma_alerts.py; wired into the hourly monitor as step 3c4.

State on 4 Nov close: every equity name is below its 50-day. No signals. Closest to an uptrend:
ARKG (49.69 vs 50d 49.92), THYP (48.36 vs 48.98), BTC (80.5k vs 82.1k), HYPE (84.0 vs 85.9), ZEC (1,290 vs 1,320).
