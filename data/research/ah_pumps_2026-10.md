# After-hours pumps (non-earnings) → next day — study of 28 Oct 2026

Tool: `tools/ah_study.py` (4hour bars, bounds=24_5, so the 20:00Z bar is the 4–8pm ET post session and 00:00Z/04:00Z are Robinhood's overnight session).
Window: 27 Apr – 26 Oct 2026 (all EDT). 150 names: 50 Robinhood-retail favourites (PLTR, TSLA, SMCI, IONQ, RGTI, QBTS, ASTS, RKLB, HOOD, SOFI, GME, AMC, …) + 99 mid/large caps from the money-flow scan + SPY.
18,914 symbol-nights; 1,144 earnings nights dropped (report date ±1 day, from get_earnings_calendar); 12,116 clean nights with ≥ $250k post-market dollar volume.

Entry = the 8pm ET post-market close (the last price you can trade on Robinhood before the overnight session).

| Move at 8pm vs 4pm close | n | 8pm → next open | next open → close | 8pm → next close (% up) | 4pm → next close |
|---|---|---|---|---|---|
| Quiet night (\|AH\| < 1%) | 10,677 | −0.03% | +0.03% | +0.01% (48%) | — |
| Pump +3% to +5% | 64 | −1.33% | −0.29% | −1.63% (33%) | +1.96% |
| Pump +5% to +10% | 30 | −2.20% | −1.59% | −3.77% (23%) | — |
| Pump > +10% | 7 | −2.23% | −1.10% | −3.36% (14%) | — |
| Dump −3% to −5% | 42 | +1.71% | +1.76% | +3.51% (74%) | −0.25% |
| Dump < −5% | 14 | +3.33% | −1.55% | +1.83% (71%) | −5.86% |

Robustness: entering at the post-session typical price (H+L+C)/3 instead of the 8pm print, 5%+ pumps still lose (median −2.2% to next close, 30% up); the 3–5% pump bucket is ~flat (−0.25% median); 3–5% dumps still bounce (+1.8% median, 69% up).

Read: non-earnings AH pumps partly stick for people who already held at 4pm (they keep ~45–58% of the AH move at the next close), but buying the pump in AH/overnight has lost money — 77% of 5%+ pumps closed the next day below the 8pm price. Mild AH dumps tended to bounce.
Caveats: six months, small event counts (37 pumps ≥5%), EDT-only, earnings filter depends on the calendar feed, other news (FDA, M&A, offerings) is not separated.
