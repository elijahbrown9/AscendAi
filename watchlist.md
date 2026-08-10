# watchlist.md — On the radar, not yet a trade

Names here are re-evaluated every pre-open brief. Being on this list is not
an entry signal — every name still has to clear strategy.md/risk.md filters
the day it's actually traded.

## STANDING RULE — DO NOT FADE @firstadopter (user-imposed, 2026-08-03)
The user's own words: "i faded the trader who is really good. i am no longer
allowed to go against him in my ideas."

Receipt: @firstadopter posted CRWV LONG at $73.596 on Sun 2026-08-02 22:28 ET.
The book was short CRWV via CORD (2x inverse) and ADDED 400 shares 8.5 hours
later, 07:07-07:42 ET Monday, at ~$7.195. CRWV ran to $78.86 (+9.9% on the
day, +7.1% since his post). CORD went to $5.68.

Loss attribution, computed not estimated:
  - original 100sh @ 7.0396 (opened Fri, BEFORE his post) ... -$135.96
  - 400sh added AFTER his post @ 7.1950 .................... -$606.01
  - 82% of the damage sits in the shares bought against him.

Scope, as the agent will enforce it at every check-in:
  - A fresh LONG from @firstadopter in a name bars a NEW short or any ADD to
    an existing short in that name or its inverse/leveraged proxies, and
    vice versa. CORD/CRWV, SOXL/SOXS-type pairs count as the same name.
  - It does NOT force an exit of a position opened before his post. It stops
    you adding to it.
  - @firstadopter's rank is re-earned weekly like everyone else's. If he
    drops out of the TRUSTED set, this rule lapses with his rank — it is a
    rule about a RECORD, not about a person.
  - Current live idea to check against: KIOXIA LONG @ 255.82 (+16.83%).

CAVEAT THE AGENT IS OBLIGED TO KEEP RAISING: this is a person-named rule,
and every person/ticker-named control in this file has relocated the
behaviour rather than stopped it (RDDT banned -> EWY -> CORD -> SNDK). It is
worth having. It is not sufficient on its own. See the stop note below.

## THE STOP WAS WORTH $634.57 TODAY (2026-08-03)
risk.md already mandates -3% from entry. On the $7.16 average that is $6.945.
  honored:  -$107.40
  actual:   -$741.97  (at $5.68)
  cost of not honoring it: -$634.57
No stop was written on CORD at any point - journal #36 records "none set".
The fade rule would have prevented the add. The stop would have capped the
damage whether or not the add happened. Both, not either.

## STANDING BAN — RDDT (user-imposed, 2026-07-30, indefinite)
The user has banned themselves from trading RDDT: "i am no longer allowed
to trade it anymore." Context: 11 round trips in 4 sessions, CHURN x9 and
REVENGE x2 flags, capped by a 50sh entry minutes before the earnings print
that exited -\$703.95 in the post-print gap 17 minutes later (journal #27,
reflected: execution-stage mistake, the user's own call). Enforcement on a
read-only desk = surveillance, not prevention: every brief and check-in
checks fills for RDDT, and ANY future RDDT fill is flagged as a ban
violation in the same breath it is found — no grace, no interpretation.
The ban is the user's own rule; only the user can lift it, in writing,
and lifting it in the heat of a moving tape should be treated as the
pattern firing again, not as a decision.

## Entry plan for Thu 2026-07-30 (user: "enter the market tomorrow")
Screened Wed evening after the close. All three are PUTS on confirmed
breakdowns — consistent with both the user's stated bearish stance and
the likely grade. CONDITIONAL: the 9am brief still recomputes the grade
fresh; if futures gap up hard on tonight's MSFT/META prints and price
confirmation vanishes, these do not fire. Entries at the 10am check-in,
max 2 positions, ≤$120 total, review_option_order first, fresh UUIDs.
1. **SOFI 8/21 $14.5P** — PRIMARY. ~$50/ctr at close, delta −0.33, tight
   spread, OI/volume deep. Reported earnings this morning (beat) and still
   fell −9% — sell-the-news breakdown with the binary REMOVED. Earnings
   clear until late Oct. Stop −35% if grade ≤−1 else −50%. Falsifier:
   reclaim of $16 (yesterday's close zone) on volume.
2. **OPEN 8/21 $3.5P** — SECONDARY. ~$25/ctr est, familiar chain (traded
   it this month). Housing casualty still bleeding (−7% today). EARNINGS
   AUG 4 PM: sized ≤$30 AND hard exit by Mon Aug 3 close, written here in
   advance per risk.md.
3. **MARA 8/21 $9P** — BACKUP. ~$30-40/ctr est, BTC-linked breakdown
   (−11.5% today, BTC weak). EARNINGS AUG 6: ≤$30 sizing or pre-earnings
   exit. Only if one of the two above fails live checks.
Rejected: HIMS puts (IV pumped after −25%/2d, in-delta costs >$100,
earnings 8/10 complication), SKHX (spreads 40-90% of mid), NVDA/SMH/MU
(budget, same as all week), NBIS calls from X feed (single poster, long
side contradicts stance, knife-catch history this week, fails budget).

## User macro stance — 2026-07-29
User cut all positions (agentic OPEN, manual RDDT) and states a bearish
view: "much lower to go," wants to stay cash unless puts/shorts. This
matches today's own -1 RISK OFF read (already puts-preferred, no new
long calls except commodity/defensive) — no conflict, just reinforcement.
This is a discretionary lean, not a rule change: the grade is still
recomputed fresh each check-in from live data, not from this note. If the
grade swings back to RISK ON while this stance still stands, that tension
gets surfaced explicitly next time, not silently resolved either way.

## RDDT — added 2026-07-25 (user thesis: risk-on return this week)
- **Structure:** below Daily 12/25 EMA ($180.96/$181.20) → resistance overhead.
  Resistance $174.22 then $177.13. Support $166.16 then $159.11.
- **Momentum:** Daily StochRSI oversold (%K 0/%D 4) — per playbooks.md P1,
  oversold-at-support argues against chasing MORE downside, not for chasing
  the bounce. Read as bounce-risk, not breakout.
- **Vol:** GARCH ann. vol 71.5% now / 75.8% 21d forecast. ATM Aug21 $170c
  IV 89% — RICH vs forecast (earnings priced in).
- **CATALYST: earnings Thu Jul 30 PM** — 4 trading days out. Every 2-6wk
  expiry straddles the print. Agentic: budget alone excludes it ($1,655/ctr
  ATM); would need a cheap post-earnings contract or a >6wk expiry sized
  <=$30 with written reason. Manual: shares-only, size and stop as normal,
  but earnings gap risk applies to shares same as options.
- **Re-evaluation trigger:** reclaim of $174.22 on volume (structure flip) OR
  clean post-earnings setup once IV crushes. Until either fires: WATCH ONLY.
- **UPDATE 2026-07-26:** RDDT earnings (Thu 7/30 PM) now sits ONE DAY after
  FOMC (Tue-Wed 7/28-29, no SEP this meeting). User macro thesis: peak
  hawkish-rate-sentiment (Warsh raised terminal rate to 3.8% in June) is
  mean-reverting down on a weak June jobs print (+57K vs 115K exp, -74K
  revisions) and cool June CPI (-0.4% MoM / 3.5% YoY), lifting rate-sensitive
  risk even without a cut. Mechanism is legitimate but red-teamed: (1) Warsh
  has fresh credibility incentive not to fold; (2) June CPI cooled on FALLING
  energy prices, and Brent is now >$100 on the same weekend war headline the
  thesis opens with — the disinflation driver is actively reversing; (3) war/
  oil + FOMC + RDDT earnings is three stacked binaries in 5 trading days.
  GRADE UNCHANGED per turn protocol — narrative is not confirmed flow. Watch
  Wed FOMC presser tone + board fresh-flow for actual confirmation.
- **UPDATE 2026-07-26 (Sun evening):** Brent $90.95, -7.56% from prior
  session (TradingEconomics) — real pullback from the >$100 spike, though
  still elevated vs pre-war ~$60s. This partially repairs the CPI-leg
  critique above (energy driver reversing helps, not hurts, disinflation).
  BTC +1.75% 24h (confirmed, modest). "Stocks bouncing" claim NOT confirmed
  — cash equities closed since Friday's close (QQQ finished red intraday);
  Hyperliquid's synthetic XYZ100 perp is trading but has no reliable
  same-scale weekend baseline to measure a move from. Treat as a hint, not
  evidence, until Monday's real session. Grade still recomputes fresh at
  9am Monday off actual data, not weekend synthetic-perp levels.

## Week of 2026-07-27 — user's main plays, screened 2026-07-27
$THYP, $MU, $SNDK, $AMD, $INTC, $RDDT submitted as this week's focus list.

- **MU** — below Daily 12/25 EMA (resist $945.59/$958.24), StochRSI 79/69
  mid-range, vol NORMAL (1.25x, at the storm edge). Earnings Sep 22 — clear.
  **ADDED.**
- **AMD** — below EMA but coiled (EMA12 $529.71 > EMA25 $523.59, still
  short-term-above-long-term). StochRSI 63/59 mid. Vol NORMAL (0.98x).
  **Earnings Aug 4 — 8 days out.** Any option bought this week with a
  standard 2-6wk expiry WILL span that print — size <=$30 or plan the exit
  before 8/4. **ADDED, calendar-flagged.**
- **INTC** — below EMA (resist $103.05/$108.60, large gap from the post-beat
  selloff). StochRSI 30/32. Vol elevated in absolute terms (85% ann.) but
  NORMAL ratio. Just reported 7/23 (huge beat, sold off on CFO dilution
  comments) — next print Oct 22, fully clear. Already the board's top
  confirmed short Friday. **ADDED.**
- **SNDK** — below EMA (resist $1595/$1679), StochRSI 46/42 neutral. Vol
  STORM on absolute terms: 137.2% annualized, GARCH long-run anchor
  UNRELIABLE (persistence 0.982 > 0.98) — judge on the absolute number, not
  a ratio. Earnings Aug 5 — 9 days out, watch if held into next week.
  **BEHAVIORAL FLAG: journal.py shows 17 round trips net -$772 (CHURN) —
  the worst pattern on the manual desk.** Setup itself is clean; the risk is
  the trader's history in this specific name. **ADDED with a hard cap:
  max 1-2 entries this week, each journaled with a falsifier before fill.**
- **RDDT** — unchanged from prior entries above. Earnings Thu 7/30, 3 days
  out. WATCH ONLY, reclaim of $174.22 is still the only trigger.
- **THYP — EXCLUDED, not added.** Not an equity: spot HYPE-token wrapper
  ETF. $61.5M market cap, 1.83M shares out, 58-80K avg daily volume (~$2M
  notional/day), 18% bid/ask spread observed live (31.98/38.15). GARCH
  model broke on it (only 50 days of history, long-run variance ~0, ratio
  1279x) — insufficient data to size responsibly. Direct HYPE token
  exposure (already tradeable via Hyperliquid) expresses the same thesis
  without the wrapper's cost and illiquidity.

## RULE-FRICTION ESCALATION — the agentic budget wall (2026-08-03, 12pm loop)
Trigger: workflow.md "rule-friction escalation." The SAME filter (premium
budget) has blocked EVERY candidate at consecutive check-ins while the grade
is directional. Today the grade is +1 RISK ON with BOTH slots open and the
tape up (SPY +1.20%, QQQ +1.44%) — and nothing is enterable.

Measured, not asserted (BABA 8/21 calls, 12:10 ET, BABA 128.53):
  130C  delta 0.489  ask 5.10  = $510   OI 11,051
  135C  delta 0.356  ask 3.25  = $325   OI  7,346   <- cheapest in-band contract
  140C  delta 0.246  ask 2.00  = $200   (delta below the 0.30 floor)
Cheapest strategy.md-compliant contract on the only in-chase-band liquid
candidate: $325. risk.md cap: $60. Account buying power: $138.62.
Blocked by 5.4x on the rule and 2.3x on the actual cash.

The honest diagnosis: this is NOT a rule that is set wrong. Raising the $60
cap to the full $120 book budget still does not reach $325. The binding
constraint is $148 of capital against a universe where liquid large/mid-cap
momentum names trade at $80-800/share.

Three paths, for the user to choose (NOT deferred silently — see below):
  (a) Fund the agentic sleeve from the manual account's idle cash.
  (b) Amend strategy.md's universe: add a hard affordability screen at
      IDEA-GENERATION time (scan only underlyings where a 2-6wk delta
      0.30-0.50 contract prices inside $20-60, i.e. roughly sub-$40 stocks
      with real chains) instead of generating ideas we then reject. Costs
      nothing, but shrinks the universe to small/mid-caps and raises the
      average IV we pay.
  (c) Accept the agentic sleeve is dormant at this size and say so plainly
      rather than running a full check-in that cannot act.
Agent recommendation: (b) now, (a) as a separate conversation. NOT putting
a "move money in" prompt to the user on a day the manual desk realized
-$1,367.50 (2.7x the daily loss limit) — that decision gets made on a flat
day, per the trader_psych.md leak-5 discipline. Carried to Friday review.

## RULE GAP — POSITION DRIFT INTO THE UNIT CAP (raised 2026-08-05, 15:05 ET)
risk.md sets "max-conviction 3 units (30pct of equity, HARD CAP)" but is
silent on what happens when a position grows INTO the cap on appreciation
rather than on buying.

Live example today: LIME 200sh, basis 30.67, now 36.6132. Zero orders
placed since 8/4. The position is 2.76 units purely because it is up
19.4pct, and it crosses the 3.0-unit hard cap at $39.76 - another 8.6pct -
without a single order being entered.

Three possible readings, none of which the file settles:
  (a) The cap governs ENTRY size only. A winner that drifts past it is
      fine, because the risk was sized correctly when it was taken.
  (b) The cap governs EXPOSURE at all times, so drift past 3.0u forces a
      trim - which means systematically cutting winners, the exact
      behaviour the R-ledger work says destroys expectancy.
  (c) The cap governs exposure but drift gets a band (say 3.5u) before a
      trim is required, so ordinary appreciation does not trigger churn.
Agent view: (c). (a) lets one winner become the whole book; (b) turns the
risk framework into a profit-taking rule, which it was never meant to be.
Proposed wording for Friday, NOT applied unilaterally:
  "The 3-unit cap is measured at ENTRY. A position that drifts above it on
   appreciation is trimmed back to 3 units only once it exceeds 3.5 units,
   and never below 3 units."
Carried to the Friday review alongside the agentic budget-wall escalation
and the TRUSTED positive-median fix.

## RULE REVIEW REQUEST — THE TURN PROTOCOL (2026-08-10)

Raised at the 2pm loop on 8/10, after the third turn confirmation in four
sessions. All three fired LONG. Record so far:

| date | confirmed by | grade move | what happened next |
|---|---|---|---|
| 2026-08-05 | 5 fresh greens | 0 -> +1 | next session realised -1,185.51 |
| 2026-08-07 | 3 fresh greens (STRC at +0.7%) | 0 -> +1 | next morning's composite recomputed to -1: a two-notch reversal overnight |
| 2026-08-10 | 3 fresh greens, TWO OF THEM CRYPTO | -1 -> 0 | open |

Two problems, both visible in the table:

1. **The threshold counts ideas the desks cannot trade.** Today's confirmation
   rests on PUMP and HYPE (crypto perps) plus BX. The manual desk trades US
   large-cap shares; the agentic sleeve trades single-leg options. Two-thirds of
   the evidence is untradeable by either desk, yet it moves the posture for both.
2. **The shift has never unlocked anything.** On 8/5, 8/7 and 8/10 the book was
   already past every limit the new grade would permit, so the notch changed the
   label and nothing else. A rule that only ever ratifies existing positioning
   is not adding information.

Proposed wording, for the Friday review — not applied:

> Turn confirmation counts only ideas in instruments a desk can actually trade:
> US-listed equities and ETFs. Crypto and perp-only ideas set context and are
> reported, but do not count toward the 3-idea threshold. A confirmed turn that
> would not change what any desk is permitted to do is logged as CONTEXT ONLY
> and does not move the grade.

This joins the three proposals already waiting here: the agentic budget wall,
the TRUSTED positive-median fix, and the position-drift-into-the-unit-cap
wording. Four now, none applied.
