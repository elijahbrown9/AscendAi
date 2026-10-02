# plans.md — Active sell plans, agentic sleeve ••••0924

Read at every check-in and position monitor. Levels are fixed when a position
opens and only ever move in the position's favour. Execute exactly as written
(autonomy: risk.md Process guards). ••••5308 is read-only and is never traded.

## RAM — 20 sh @ 14.45 (USER buy, limit GTC all-day session, 1 Oct 21:15 ET)
User override: the buy took cash to $11.33 (< $20 floor) and RAM ≈ E/2. No new
agent entries until the book is back inside risk.md. No user instruction about
stops on this one, so the AAPU precedent applies: the agent places the resting
stop at the 10am check-in (no exits before then — this brief places no trades).
- STOP: resting GTC stop_market 20 @ **13.02** (1.5σ ≈ 9.9% > 6% floor; σ from
  realized vol — RAM listed 25 Jun, too little history for GARCH).
  Order id 6abfb484-5988-4bff-9310-15d455cdcda7 (placed 9:41 ET 2 Oct, confirmed).
- TARGET 1: RAM ≥ **17.31** (2× stop distance) → cancel the stop, sell 10, stop
  the last 10 at **14.45** (breakeven).
- TRAIL (after T1): 9.9% below the highest RAM price seen at any monitor.
- TIME: sold by the close on **Fri 16 Oct** (10-session limit for 2x) unless a
  reason is logged. MU reports in late Dec — clear.
- REGIME: grade −1 → sell 10; grade −2 → sell all.

## NVDL — 5 sh @ 37.7486 (agent buy 7, 1 Oct 15:12 ET; user sold 2 @ 39.62, 2 Oct 09:53)
Thesis: NVDA board-confirmed long (posted 10:32 ET @ 230.17, +0.7% at entry,
1 co-sign, one side only); grade +1 after the 2pm turn confirmation. Earnings
17 Nov (pm, verified) — clear. Sized ≤ E/2 ($264 of $564.57).
- STOP: resting GTC stop_market 5 @ **35.48** (−6% floor; 1.5σ ≈ 4.8%).
  Order id 6abfbcba-6dfc-4bd0-a631-1c4e6e76c40e (re-placed 10:16 ET 2 Oct after
  the user cancelled the 7-share stop to sell 2). Verify open at every monitor;
  re-place at once if missing.
- TARGET 1: NVDL ≥ **42.28** (+12% = 2× stop distance) → cancel the stop, sell 2
  (marketable limit at the bid), re-place a GTC stop on the last 3 at **37.75**.
- TRAIL (after T1): stop on the last 3 = 6% below the highest NVDL price seen at
  any monitor, never lowered.
- TIME: sold in full by the close on **Thu 15 Oct** (10-session limit for 2x)
  unless a reason is logged here.
- REGIME: grade −1 → sell 3 and stop the rest at breakeven; grade −2 → sell all.
- BOARD: NVDA a knife catch or on both sides while in profit → stop to breakeven.
- FALSIFIER: NVDA closes below 225.00 (−2.2% from the post) → thesis broken, exit.

## AAPU — CLOSED
Stop hit: 6 @ 42.931 (GTC stop 42.94, filled 11:32 ET 1 Oct); fractional 0.127782
sold @ 42.71 at the 11:40 monitor. Result −$16.88 (−6.0%) on $279.92. AAPL
327.48 (−1.7% on the day) at exit. Plan retired.

## ZCSH — CLOSED
User sold all 8 @ 37.69 (market) at 11:29 ET 30 Sep. Plan retired.

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
- 30 Sep 11:29 user sold 8 ZCSH @ 37.69 (−$3.52 vs 38.13). 11:40 monitor: AAPU
  45.53, stop verified open; cash $301.52, E $580.52 — book back inside limits
  (1 position, AAPU ≤ E/2, cash ≥ $20). Next entry eligible at the 12pm check-in.
- 1 Oct 11:32 AAPU stop filled 6 @ 42.931 (AAPL ~327.5). 11:41 monitor: agent sold
  0.127782 AAPU @ 42.71 (market, fractional). Book flat: cash $564.57, E $564.57.
  AAPU −$16.88. Next entry eligible at the 12pm check-in under risk.md.
- 1 Oct 12:11 check-in: book flat ($564.57 cash). Only confirmed long SNPS (+5.3%
  since post) has no 2x–5x ETF → no entry. TURN ALARM (fresh flow long vs short
  winners) unconfirmed: 1 of 3 fresh longs green. Grade stays 0.
- 1 Oct 14:11 check-in: book flat ($564.57). Candidates: SNPS/COHR/RKT no 2x–5x
  ETF; TLT on both sides (no signal); WTI → UCO blocked by chase (USO +2.2% from
  today's 147.14 open, band 2% at grade 0; last 30m spike +1.9%). TURN CONFIRMED:
  alarm + 4 fresh longs green (SNPS, COHR, RKT, WTI) → grade 0 → +1 from the 3pm
  check-in (posture unchanged: full size, any leverage). Alert sent: COHR.
- 1 Oct 15:11 check-in (grade +1): bought 7 NVDL @ 37.7486 (NVDA confirmed long
  +0.7% from 230.17 post, inside 2%). GTC stop 7 @ 35.48 placed and verified
  (confirmed). Cash $300.33. UCO: WTI dropped off the confirmed list — no entry.
- 2 Oct 09:25 brief: grade +1 (composite +0.252). User bought 20 RAM @ 14.45 at
  21:15 ET 1 Oct; cash $11.33 → book outside limits, no agent entries until fixed.
  Pre-market NVDL 38.98 (stop 35.48 open), RAM 14.71. RAM stop 13.02 at 10am.
- 2 Oct 09:41 monitor: RAM GTC stop 20 @ 13.02 placed and verified (confirmed).
  NVDL 39.19 (stop 35.48 open), RAM 14.43, NVDA 236.14. E $574.23, cash $11.33.
- 2 Oct 09:53 user cancelled the NVDL stop and sold 2 @ 39.62 (+$3.74). 10:16
  check-in: agent re-placed GTC stop 5 @ 35.48 (confirmed). Cash $90.57; RAM
  $290.80 vs E/2 $289.11 → still $1.69 over, no entry. TLT long confirmed (crowd
  3, one side) → TMF would qualify once the book is inside limits.
- 2 Oct 12:12 check-in: E $572.65, cash $90.57, RAM $285.60 ≤ E/2 $286.32 → book
  back inside limits (1 slot open). No confirmed candidates (TLT aged off) → no
  entry. NVDL 39.25 / RAM 14.28, both stops open.
