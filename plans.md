# plans.md — Active sell plans, agentic sleeve ••••0924

Read at every check-in and position monitor. Levels are fixed when a position
opens and only ever move in the position's favour. Execute exactly as written
(autonomy: risk.md Process guards). ••••5308 is read-only and is never traded.

## AAPU — 6.127782 sh @ 45.68 (user market buys, 30 Sep 10:05 ET + 0.127782 fractional)
Thesis: AAPL board-confirmed long (+2.0%, posted pre-open 30 Sep), grade 0.
- STOP: resting GTC stop_market 6 @ **42.94** (−6%, the floor; 1.5σ ≈ 4.4%).
  Order id 6abd177a-1d07-4e37-bbc1-bd31173be042. Verify it is still open at
  every monitor; re-place it at once if missing. The 0.127782 fractional share
  cannot carry a stop order: it follows the same levels, sold at a monitor.
- TARGET 1: AAPU ≥ **51.16** (+12% = 2× stop distance) → cancel the stop,
  sell 3 (marketable limit at the bid), re-place a GTC stop on the last 3 at
  **45.68** (breakeven).
- TRAIL (after T1): stop on the last 3 = 6% below the highest AAPU price seen
  at any monitor, never lowered.
- TIME: sold in full by the close on **Wed 14 Oct** (10-session limit for 2x)
  unless a reason is logged here; in any case before AAPL earnings **29 Oct (pm)**.
- REGIME: grade −1 → sell 3 and stop the rest at breakeven; grade −2 → sell all.
- BOARD: AAPL a knife catch or on both sides while in profit → stop to breakeven.

## ZCSH — 8 sh @ 38.13 (user-held; "let the zcash trade run")
User cancelled the resting stop on 30 Sep: NO resting stop order on ZCSH.
Levels are checked at each monitor and acted on there; a gap through them
between monitors is accepted by the user.
- TARGET 1: ZCSH ≥ **43.85** (+15%) → sell 4 (marketable limit at the bid).
- TRAIL (after T1): sell the last 4 if ZCSH falls 11% (1.5 × 7.33% σ) from the
  highest price seen at any monitor since T1.
- FLOOR: ZCSH ≤ **33.94** at a monitor (−11% from cost, 1.5σ) → sell all 8.
- ZCSH is not a 2x–5x ETF; no adds by the agent.

## Next trade
Opens when the book is inside risk.md: cash ≥ $20 after the buy and every share
position ≤ E/2. Source: board CONFIRMED CANDIDATE → 2x–5x ETF, chase ≤ 2% from
the reference price (3% at +2), not crowded, not two-sided, earnings clear.
Every new position gets its section here before the fill is reported.

## Log
- 30 Sep 10:03 agent sold 7 ZCSH @ 39.07; 10:05–10:06 user bought 6 AAPU @ 45.68
  and 1 ZCSH @ 39.72, cancelled agent orders; 10:06 agent AAPU stop 42.94.
- 30 Sep ~10:10 user bought 0.127782 AAPU with the last $5.84 (cash $0). 10:11
  check-in: AAPU stop verified open; no level hit (AAPU 45.57, ZCSH ~39.0).
