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

### EVIDENCE FOR THE TURN-PROTOCOL REVIEW — 2026-08-18 (the cleanest counterexample yet)

The turn rule treats rising fresh 6h long flow as a LEADING indicator against a
coincident winner skew. Today inverted that premise for a full session, and the
record should carry the numbers.

Fresh 6h flow got steadily MORE long as the tape fell:
  10:06  19L / 15S     SPY -0.53%  QQQ -1.50%
  12:05  31L / 22S
  14:04  35L / 21S
  15:05  37L / 19S     SPY -0.64%  QQQ -1.73%

Confirmed candidates over the same window went the other way, completely:
  10:06  1 confirmed  (MU short)                       long-side greens: 0
  12:05  5 confirmed  (3 equity shorts, BTC + ETH)     long-side greens: 2, both crypto
  14:04  6 confirmed  (5 equity shorts, ETH)           long-side greens: 1, crypto
  15:05  6 confirmed  (ALL SIX equity shorts)          long-side greens: 0

At the 15:05 read there is not one confirmed idea on the "new" side the alarm
points to. BTC dropped off the confirmed list into CROWDED at 4 co-signs — late
consensus, which the rule itself reads as contrarian. The alarm fired at all four
check-ins and the threshold was never approached.

WHAT THIS SAYS ABOUT THE RULE: rising fresh long flow into a broad decline is not
positioning leading a turn, it is the crowd getting longer on the way down. The
protocol cannot distinguish the two, because it reads flow DIRECTION and never
asks whether the fresh flow is WORKING. A candidate amendment to test at the
weekly review:

> TURN ALARM is suppressed when fresh flow on the new side has a negative median
> return since posting. Divergence between positioning and winners only signals a
> turn when the new positioning is at least breaking even; when the new side is
> underwater, the same divergence signals capitulation-chasing and the grade does
> not move.

This is separate from, and compatible with, the 2026-08-10 proposal above
(tradeable-instrument filter). Today both would have blocked the shift, and the
rule as written also blocked it — so nothing was mistraded. The value is that this
is the first session where the alarm's PREMISE, not just its threshold, can be
tested against a full day of data.

Running record of the alarm: 8/5, 8/7, 8/10, 8/14, 8/17 confirmed (five shifts,
none of which changed a single permitted action); 8/18 fired four times and
confirmed nothing.

### RULE REVIEW REQUEST — SELF-REFERENCE IN THE TURN PROTOCOL (2026-08-19)

Today's turn confirmation cleared its 3-idea threshold on MRNA + SKHX + BTC. MRNA
is the position the manual desk bought this morning at 9.11 units. The protocol
therefore counted the desk's own holding as independent evidence for shifting the
grade in the direction that would license more of it.

Proposed clause, to sit alongside the 2026-08-10 tradeable-instrument filter:

> A name the desk already holds does not count toward the turn threshold. Turn
> confirmation measures whether OTHER participants' fresh positioning is working;
> a position the desk itself owns is not independent evidence about the regime,
> and counting it lets a single held name both create the exposure and justify it.

Applying both proposals to today: BTC excluded as untradeable, MRNA excluded as
held, leaving SKHX = 1 of 3 and no shift.

Also worth noting for the review: the winner skew reversed twice inside three
hours today — LONGS winning with no alarm at the 09:03 pre-open read, SHORTS
winning with the alarm re-armed by 10:06. A coincident measure that flips inside
a session is describing chop, not regime, and the alarm inherits that noise.

### RULE REVIEW REQUEST — THE PREMIUM BAND AND THE DELTA FILTER COLLIDE (2026-08-25)

The agentic sleeve's cash settled today and buying power reached $144.93 — the
first spendable dollar since August 3. It still cannot place a compliant order,
and the reason is no longer money.

risk.md sets the option premium band at **$20–60**. strategy.md requires
**delta 0.30–0.50** and **2–6 weeks to expiry**. Priced against today's only
confirmed board idea:

  NVDA 2026-09-18 225 call — 24 DTE, delta 0.333, IV 41.5%, OI 47,958
  ASK $4.75  =>  $475 per contract, 7.9x the top of the premium band

A contract inside the $20–60 band on a $213 underlying prices at $0.20–0.60 per
share, which at 24 days sits far out of the money with delta roughly 0.02–0.05 —
failing the delta filter by an order of magnitude. **The two rules cannot both be
satisfied on any underlying much above ~$20 a share.**

This is arithmetic, not market conditions. It means the sleeve could not have
traded most of this board even when funded, and it reframes the three paths
filed on 8/5:

> Fund it · screen for affordability at idea generation · declare it dormant
> — **and now a fourth: resize the premium band to match the filters, or state
> explicitly that the sleeve trades only low-priced underlyings.**

The $20–60 band was written for an account holding $148. The delta and expiry
filters were written for liquid large- and mid-caps. Those two intentions are
incompatible and one of them has to give.

- **2026-08-26 — premium-band conflict, third data point (closes the "find a cheaper one" escape).**
  Priced the board's one confirmed candidate as a compliant contract: META Sep-18 555 put,
  delta −0.335, 23 DTE, OI 2,548, volume 190, spread 5.3% of mark. It passes the delta filter,
  the expiry window, and the liquidity bar — every quality test in strategy.md. Ask $12.65 = **$1,265
  per contract**, 8.7× the sleeve's entire $144.93 and 21× the top of the $20–60 band.
  With NVDA ($475, passes) and VVV ($65, fails liquidity: zero volume, 48%-of-mark spread), the
  pattern now has both ends nailed down: contracts inside the band are illiquid, contracts that
  clear the quality filters cost multiples of the account. This is not a scanning problem that a
  wider search fixes. Either the band moves, the sleeve gets funded, or the sleeve is dormant.

- **2026-08-26 12:04 — tradeable-instrument filter, fresh instance (see the 8/10 item).**
  TURN ALARM fired with two confirmed candidates: ZHIPU long (+4.1%) and NVDA short (+1.6%).
  ZHIPU returns 404 from the broker — it is not a tradeable instrument here at all. The turn
  protocol counted it toward the threshold anyway, because the protocol counts board rows, not
  positions the desk could actually take. Second time this has happened since 8/10. The fix is
  one line: a confirmed candidate only counts toward the turn threshold if the desk can trade it.

- **2026-08-26 14:03 — the tradeable-instrument gap nearly moved the grade.**
  Two hours after the 12:04 instance, the board shows **three** confirmed candidates: ZHIPU long,
  NVDA short, ZEC long. The TURN ALARM had cleared by then, so the threshold was never applied —
  but had it still been firing, the turn protocol would have counted 3 fresh confirmed ideas on
  the new side and **shifted the grade a full notch**. Of those three: ZHIPU 404s, ZEC 404s, and
  NVDA is disqualified by risk.md line 17 (reports tonight, >$30 exits before earnings, always).
  Zero of the three are positions this desk could take. A rule that changes the grade off a count
  of board rows can be moved by names that do not exist here. Third instance since 8/10, and the
  first where the gap could have changed the posture rather than just the report.

- **2026-08-26 15:03 — the premium band, priced to a number.**
  INTC long joined the board's confirmed list at +1.0%. It is the cheapest tradeable large-cap the
  board has confirmed this week, so it is the fairest test of the band. INTC $87.62; Sep-18 92.5
  call, delta 0.395, 23 DTE, OI 4,229, volume 72, bid 3.30 / ask 3.50, spread 5.9% of mark —
  clears delta, expiry and liquidity. **Ask $350 per contract, against $144.93 of buying power.**
  That is the closest any candidate has come all week and it is still 2.4x the sleeve.
  Four data points now bracket the answer: META $1,265, NVDA $475, INTC $350, VVV $65 (illiquid).
  So the decision has a number attached. One standard position at current prices needs roughly
  $350-500, i.e. about 3x the sleeve's size; a band that admits real contracts is roughly
  $100-400, not $20-60. Fund it to ~$500, widen the band to ~$100-400, or declare it dormant.

- **2026-08-31 10:20 — the tradeable-instrument gap is no longer hypothetical: it just set the grade.**
  TURN ALARM fired with exactly three confirmed candidates on the new (long) side — SMSN, MU, INTC.
  Under workflow.md as written that meets the threshold and the grade shifts one notch, 0 → +1 RISK ON.
  **SMSN returns 404 from the broker.** MU and INTC are tradeable; SMSN is not. So the count is 3 by
  board rows and 2 by positions this desk could take, and the entire posture change rests on the
  difference. On 26 August this was logged as a near-miss — "the first where the gap could have
  changed the posture rather than just the report." Five days later it did, and it did so on the
  day the manual desk went flat with $28,510 of cash, which is the moment a permissive posture
  matters most. Fifth instance since 8/10. The fix remains one line: a confirmed candidate counts
  toward the turn threshold only if the desk can trade it.

- **2026-09-08 15:03 — the losing mechanic today was re-entry price, not direction, and nothing measures it.**
  The desk went flat for the third time in six sessions (final exits HOOD 210 @ 119.8903, −$684.16 and
  ZCSH 250 @ 93.699, −$408.07, both 14:36–14:38 ET). Today realised **−$1,146.80 across 10 closes**:
  HOOD −$718.75, ZCSH −$425.32, DRAM +$18.03, HIMS −$20.76. ZCSH was sold at 92.64 and re-bought the
  same session at **95.33 — above its own exit** — and the loss on the second lot is roughly the gap.
  The direction calls were not the problem: every name sold earlier today closed lower than where it
  was sold, the same result as the prior three weeks. The cost sits entirely in paying up to get back
  into a position the desk had just left.
  `discipline.py` cannot see this. CHURN counts 5+ round trips in one symbol netting negative, OVERNIGHT
  counts fills outside 9am–8pm, REVENGE counts 3+ consecutive same-day losses — all price-blind. A rule
  that compares each entry against the most recent exit in the same symbol on the same day would have
  flagged both ZCSH re-entries and at least two of the five HOOD round trips on 9/4. Proposed one-liner:
  **no re-entry in a symbol above that day's own exit price in the same symbol without a fresh confirmed
  board row.** Seventh instance of the discipline-flag scoping gap; the first where the missing dimension
  is price rather than time or symbol count.

- **2026-09-09 09:22 — a board ticker resolved to a completely different real asset at the broker (VVV).**
  The board's only CONFIRMED candidate today was `VVV long +1.7%` from @degentradinglsd. The board's VVV is
  the **Venice AI token**, a hyperliquid perp at $27.64 with the thesis "should absorb capital rotating away
  from TAO as the default AI long." VVV at this broker is **Valvoline Inc.**, an NYSE automotive-lubricants
  company at $30.59. Same three letters, unrelated assets, both real and both liquid.
  This is worse than the tradeable-instrument gap logged five times since 10 August. Those tickers (ZHIPU,
  ZEC, TAO, SMSN, and CHIP again today) returned 404 or no quote — they failed loudly and could not be
  traded by accident. A collision fails **silently**: the order fills, in the wrong company, on a thesis
  that has nothing to do with it.
  It has already contaminated this record once. The 26 August premium-band review priced "VVV $65, OI 75,
  48% spread, illiquid" as one of the four data points bracketing the options band — that was Valvoline's
  chain, measured against a Venice AI signal. The band conclusion (~$100–400 needed) rests on META, NVDA
  and INTC and survives without it, but the VVV row should be struck from that comparison.
  Fix, one line, alongside the tradeable-instrument filter: **a board row counts as a candidate only when
  the broker instrument matches the board's asset, not merely its symbol** — check the venue and the
  underlying, not the three letters. All 25 board rows today were hyperliquid perps, so this is not rare.

- **2026-09-09 12:05 — TURN ALARM confirmed: grade shifts 0 → +1, and the tradeable-instrument filter
  was applied to a live turn decision for the first time without changing the answer.**
  Fresh 6h flow 27 long / 11 short while winner skew has shorts winning — divergence, so TURN ALARM.
  Four confirmed candidates on the new (long) side, all green since posting: ZEC +2.6%, MU +1.4%,
  INTC +1.2%, SNDK +0.7%. workflow.md's threshold is ≥3, the storm veto does not bind (SPY 0.94×,
  QQQ 0.88×), so the grade shifts one notch to **+1 RISK ON**, effective from the 14:04 check-in.
  **ZEC returns no quote at this broker** — the sixth instance of the tradeable-instrument gap this
  record (after ZHIPU, ZEC, TAO, SMSN, and CHIP this morning). Applying the filter that has sat
  unadopted since 10 August: 4 board rows, 3 tradeable instruments, threshold still met. This is the
  first time the filter has been exercised on a decision that mattered and left the outcome unchanged
  — on 31 August it would have blocked the identical shift. That is the argument for adopting it:
  it costs nothing when the signal is broad and it binds only when the count is exactly at the line.
  Two cautions on the confirmations themselves. @degentradinglsd, the author behind MU (and NBIS),
  sits **last on the 7d leaderboard at a 33% hit rate and −3.0% median**. And **VVV — this morning's
  single confirmed candidate — is now −9.0% since posting.** A confirmation four hours old is not a
  durable one.

- **2026-09-09 12:05 — the event-contract sleeve closed, and the terminal saw its P&L for the first time.**
  The $743.60 of event contracts flagged as unmeasured for six sessions were sold at 10:03 ET in three
  fills for a combined **−$205.10** (−$3.20, −$183.10, −$18.80). It never had a gauge, a unit size or a
  stop while it was open, and the only number this record ever carried for it was its market value.
  The open item can be closed as resolved-by-liquidation rather than resolved-by-measurement, which is
  the weaker of the two outcomes: if it is re-established, nothing has changed about the instrumentation.

- **2026-09-09 14:04 — two full liquidate-and-rebuild cycles in one session, and a number for what the
  round-tripping costs.**
  The manual desk went completely flat twice today and rebuilt both times: 11:22–11:51 ET (flat for
  **81 seconds**) and 12:55–13:21 ET (flat for **4m48s**). Fifth and sixth full liquidations in seven
  sessions. **ZCSH was re-entered above its own exit three separate times today** — 98.88 after a 93.699
  exit, 101.67 after a 100.16 exit, 102.45 after a 101.8442 exit — with the rebuilds walking up in price
  across six, then nine separate buy orders.
  What makes today diagnostic is that the round-tripping *made money on the tape* and still lost against
  doing nothing. ZCSH realised **+$776.35** across three closes today. But the average cost ratcheted up
  at every reset — **98.88 → 99.42 → 101.67 → 102.45**, a 3.6% climb — while the stock rose 10.4% from
  yesterday's 91.71 close to 101.255. Holding the original 500 shares at 98.88 untouched would be worth
  **+$1,187.50** right now. The actual outcome is +$776.35 realised plus −$268.88 open on the surviving
  225 shares = **+$507.47**. Roughly **$680 of a $1,188 move was given back** to the resets. (Share count
  varied between 225 and 500 across the day, so treat the figure as an approximation, not an accounting.)
  This is the cleanest evidence yet for the price-based rule proposed on 8 September. `discipline.py`
  sees none of it: three closes in ZCSH is under the CHURN threshold of five, and the symbol is net
  positive, so nothing fires. A rule keyed on *entry price versus the same day's exit price in the same
  symbol* would have flagged all three.

- **2026-09-09 15:04 — I reported agentic positions the account did not hold, for four sessions.**
  Every agentic-desk panel since 4 September has listed **TXXH 2 @ 66.69 and BITX 0.63 @ 18.32**. The
  account has not held either since **3 September at 12:59 ET**, when both were sold (TXXH 2 @ 68.84,
  +$4.30; BITX 0.6305 @ 18.8586, +$0.34). Since then the sleeve has held a single equity position in
  **RAM**, now 10.8194 shares at a 14.62 basis. Today's pre-open brief, its published dashboard, and the
  10:04, 12:04 and 14:04 check-ins all carried the wrong book.
  The mechanism is specific and worth fixing rather than apologising for: I called `get_portfolio` on
  981890924 at every check-in — which is why **every account-value figure was correct** — but I did not
  call `get_equity_positions` on it. `get_option_positions` returned `[]`, I read that as "nothing has
  changed in the sleeve," and reprinted the last equity snapshot I had. The trigger's step 1 names
  get_portfolio, get_option_positions and get_option_orders; equity positions are only implied by
  "+ get_equity_orders if relevant." For an options-only sleeve that holds equities, they are always
  relevant. **Fix: fetch `get_equity_positions` for 981890924 at every check-in, and never restate a
  position that was not re-fetched in the same turn.**
  Related, and only visible once the real book was fetched: cash in the sleeve is now **$0.00** — the last
  $4.22 went into RAM at 14:39 ET today. risk.md's cash floor is **$50**. The sleeve has been below its own
  hard floor all day, which is a cleaner statement of why no option entry is permissible than the premium
  band I have been citing for nine sessions. The dashboard has been corrected and republished.

- **2026-09-10 09:24 — the book is inside every hard limit for the first time, and it cost $788 to get there.**
  The manual desk this morning: 2 positions (max 3), ZCSH 1.81u and DRAM 2.16u (cap 3), gross **4.10 units**
  against a 9.0 ceiling, **zero margin** at a grade that permits zero, and **+$17,117.54 of cash** where
  yesterday there was $30,079.82 of debt. Every hard limit in risk.md satisfied simultaneously, with
  positions held. That has not happened before in this record.
  The route was a third liquidation at 16:49 ET yesterday: ZCSH 250 @ 99.30 (**−$788.38**) and DRAM 350 @
  61.5435 (−$32.11). Those turned 9 September from the +$378.23 I reported at 15:03 into **−$442.28** on
  the day. The ZCSH lot sold at 99.30 was the one bought at 102.45 in the 13:01–13:21 rebuild — the third
  re-entry above its own exit that day, carried three hours, and it accounts for essentially the whole loss.
  Two things worth recording rather than celebrating. **The compliance was produced by capitulation, not by
  sizing** — the desk did not trim to the cap, it sold everything and re-entered small. Nothing in the
  process changed, so nothing prevents 19 units reappearing tomorrow. And **today's ZCSH re-entry at 98.52
  is the first below a prior exit in eight sessions** (the exit was 99.30), which is the behaviour the
  proposed price rule is trying to make routine.
  **CHURN now fires on a held ticker.** DRAM: 11 round trips this week netting −$121.45, first strike of
  three. The desk holds 105 shares of it. Separately, the event-contract sleeve is **back at $390** one
  session after closing at −$205.10 — confirming that closing it was not the same as instrumenting it.

- **2026-09-10 12:05 — the daily-loss limit is the binding constraint for the first time, and the event
  sleeve is now measurably losing.**
  A fourth full liquidation, at **09:08 ET — five minutes after the pre-open brief fetched its positions
  and sixteen minutes before it published.** DRAM 105 @ 59.42 (−$132.70), event contracts 1000 @ 0.36
  (−$120.00), ZCSH 55 @ 94.58 (−$216.60). The ZCSH lot had been bought pre-market at 98.52 that same
  morning and was sold −4.0% within minutes of the open. Today's realised is **−$469.30 against a
  $574.11 daily limit — 82% of it** — with a further −$198.25 open. This is the first session in this
  record where the daily-loss framework, rather than a size cap, is the live constraint.
  Note for the brief itself: its book was accurate when fetched and stale when published. Worth stating
  the limitation rather than pretending a 09:24 snapshot describes the day.
  **Event contracts: two closes in two sessions, −$205.10 then −$120.00, −$325.10 combined.** The sleeve
  was logged as "unmeasured" for seven sessions; now that it has been measured twice it has lost both
  times. The open item changes from "we cannot see it" to "we can, and it is negative."
  Also worth recording: the board carried **NVDA in both directions simultaneously** — a confirmed short
  at +0.7% and a knife-catch long at −2.0% with four co-signs, the same ticker in the CONFIRMED, KNIFE
  CATCH and CROWDED lists at once. `board_signals.py` does not reconcile opposing rows on one ticker.

- **2026-09-10 14:04 — the daily-loss limit is breached: −$806.00 realised against a $570.18 cap (141%).**
  A second full liquidation today at **12:17 ET** — ZCSH 50 @ 92.2052 (−$106.54), HOOD 75 @ 113.5752
  (−$155.49), DRAM 125 @ 58.56512 (−$74.67) — on top of the 09:08 one. **Six closes today, all six losses:**
  DRAM −$132.70, event contracts −$120.00, ZCSH −$216.60, ZCSH −$106.54, HOOD −$155.49, DRAM −$74.67.
  risk.md's daily loss limit is 2% of equity, $570.18 on today's $28,509.16. Realised is **−$806.00,
  141% of it, over by $235.82.** This is the first time in this record the loss limit has actually been
  breached rather than approached — and it is the one limit that is supposed to end the session.
  **All three names were re-entered after the breach**, at 25 shares each. The size limits are all
  comfortably satisfied — book 2.31 units against a 9.0 ceiling, zero margin, one-sigma day $412 against
  $570 — which is precisely the problem with reading compliance off the size caps alone: the book has
  never looked safer and the day has never lost more.
  **Count correction:** at 12:04 I called the 09:08 liquidation "the fourth." It was the fifth since
  8 September (8 Sep 14:36 · 9 Sep 11:22, 12:55, 16:49 · 10 Sep 09:08), and the 12:17 one is the sixth.
  Two full liquidations today, four yesterday and today combined.

- **2026-09-11 09:25 — compliance lasted eighteen hours; leverage is now the highest on record.**
  Thursday 15:04 the manual desk held **2.31 units, zero margin, every hard limit satisfied**. This
  morning it holds **20.27 units** — DRAM 500 @ 59.82 (10.58u), ZCSH 300 @ 92.72 (9.69u) — against
  **−$29,237.30** of cash, a gross of **2.03×**. That is above the 1.96× of 9 September and the highest
  this record has measured. Yesterday's entry read *"nothing prevents 19 units reappearing tomorrow."*
  It took eighteen hours, and the grade being +1 does not help: the margin ceiling at +1 is 1.25×, so
  this is 62% over even at today's permissive setting.
  **Thursday's real close was −$883.59, not the −$806.00 I reported at 15:03** — HOOD 25 was sold at
  111.5728 at 18:06 ET for a further −$77.56. Seven closes, seven losses, **155% of the $570.18 limit.**
  **The trailing week is negative: −$388.85 over 31 closes at a 23% win rate.** Every symbol except ZEC
  lost: HOOD −$1,036.21 (5), ZCSH −$760.51 (8), event contracts −$337.80 (5), DRAM −$330.11 (11),
  HIMS −$20.76 (1). ZEC's single close made +$2,096.54; **the 30 closes this terminal can see produced
  −$2,485.39.** The win rate has fallen 44% → 35% → 23% across Tuesday, Thursday and today as the
  early-week winners aged out of the window.
  **Three CHURN flags fire at once — HOOD, ZCSH and DRAM — the most this record has carried** (previous
  high: one). Every ticker the desk traded this week is flagged and every one is negative, and two of
  the three are currently held at more than three times their cap.
  Worth holding against the +1: the board scored **−0.66 yesterday, its most negative, and +0.82 today,
  its most positive** — both extremes inside 24 hours, off 17 rows. And the 7d author leaderboard has
  decayed to three of six qualifying authors at a 33% hit rate or worse, with @_tolks 0-for-4.

- **2026-09-11 14:04 — the first board-confirmed entry, bought ~6% above the poster's price.**
  ETH is one of today's confirmed candidates and the desk holds it — the first time in this record that
  an entry and a live board confirmation are the same name. That is the right direction. The execution
  is the old problem in a new place: the board row shows **+4.4% since posting**, implying the author's
  entry near **23.35**; ETH closed 23.49 yesterday and trades **24.375** now. **The desk's basis is 24.80**
  — roughly **6% above the poster's entry and above the current price.** So the idea is a winner by the
  board's measure and the position is **−1.71%**.
  This is what the 2% chase band is for, and it is the cleanest illustration yet of why: the signal was
  correct, the desk acted on the correct signal, and the entry price turned it negative anyway. Following
  the board only pays if the entry is inside the band from the reference — the confirmation is not a
  licence to buy at any price.
  Elsewhere the day is the size lesson again. One trade all session (the 09:54 DRAM exit, −$379.96) and
  the account is down **$1,283.22** since 10:12 on marks alone — open P&L +$1,216.50 → +$96.00 → −$86.75
  across three check-ins. Book 20.13 units against a 9.0 ceiling, margin 2.01x against the 1.25x that
  grade +1 permits. Nothing is breached on stops or the loss limit; the exposure is doing all the work.

- **2026-09-14 09:26 — the payoff ratio was the edge, and it collapsed.**
  Last week: **−$3,836.78 over 36 closes at a 16% win rate**, five losing sessions out of five. Every one
  of the six symbols lost. Compare the month to 10 September: +$7,565.25, 39% win rate, **2.42× payoff**.
  Last week the payoff was **1.01×** — average win $161.66 against average loss $160.23.
  **The win rate was never the edge.** At 39% and 2.42× the style makes money; at 16% and 1.01× the same
  style cannot. What actually changed is the size of the winners: **average win $550.38 → $161.66.**
  Positions were cut before they could become the kind of trade that carried August (THYP +$1,150/close,
  ZEC +$2,096 on one). That is the mirror of the sizing problem already logged — **too large on the way
  in, too quick on the way out.** A book at 20 units cannot sit through a 9% one-sigma day, so winners
  get closed at +1% and losers get closed at −2.5%; the payoff ratio is the arithmetic consequence of the
  position size, not a separate failing.
  Friday closed at **−$945.39**, not the −$379.96 standing at the 15:03 check-in — **174% of the cap, the
  second consecutive breach** after Thursday's 155%. ETH stopped out at 24.18 against a 24.80 basis
  (−2.5%); at 6.66 units instead of the permitted 3 that cost **$465 instead of about $210**.
  **Four CHURN flags** — ZCSH −$1,186.69 (11), HOOD −$1,036.21 (5), DRAM −$710.07 (12), event contracts
  −$337.80 (5) — the most carried at once. None is held, so the ban rule has nothing to bite on: the
  flags describe a pattern, not a ticker.

- **2026-09-14 09:26 — the agentic mandate question is now a live 22% drawdown.**
  RAM is **−14.91% pre-market, 2.07× its own one-sigma day**, and **−21.96% from a 14.62 basis**. It is
  100% of the sleeve, which has fallen $158.29 → **$123.45** since Thursday. **No exit rule in risk.md
  reaches it:** the sleeve's stops are written on option premium (−50% / −35% / −25%) and this is an
  equity. Cash is **$0.00** against a $50 hard floor for an eighth session, so it cannot be hedged or
  reduced into either. Eleven sessions after the options-only-vs-equity question was first raised as a
  governance item, it has stopped being a governance item.

- **2026-09-14 09:26 — second instance of one ticker on both sides of the board.**
  NVDA is today's *only* confirmed candidate (short, +1.3%, two co-signs) and simultaneously sits in
  CROWDED as a long with four co-signs at −1.2%. The same defect appeared on 10 September. Proposed
  handling until `board_signals.py` reconciles opposing rows: **a ticker appearing on both sides counts
  as no signal, not as a confirmation.** Today that would leave the board with zero confirmed candidates,
  which is the honest reading of a 10-long/10-short tape.

- **2026-09-14 14:04 — the clean book lasted about three hours, and leverage set a new record.**
  At 12:04 the manual desk was **4.59 units, zero margin, +$14,358 cash** — the best-shaped book in this
  record. At 14:04 it is **20.89 units on 2.089× gross with −$29,198.66 of cash**, the highest leverage
  measured here (previous 2.034× on 11 September). Three positions, all three above the 3-unit cap:
  DRAM 10.36u, ZCSH 6.02u, ETH 4.51u.
  The pattern is now precisely dated three times: **compliant at 15:04 Thu 10 Sep → 20.27u by Fri open;
  compliant at 12:04 Mon 14 Sep → 20.89u by 14:04 the same day.** The interval has compressed from
  eighteen hours to two. Sizing is not drifting upward gradually; the book is rebuilt to ~20 units in a
  single burst each time it is emptied.
  One thing did change: **DRAM was re-entered at 55.45 against a 59.06 exit on Friday — 6.1% BELOW its
  own exit**, and ETH at 23.89 against a 23.88 exit. Two consecutive entries at or below the prior exit
  after ten above it. The entry-price habit is improving while the size habit is not, which suggests
  they are separate problems and should be tracked separately.

- **2026-09-14 14:04 — the board reversed on my own top idea inside five hours, and a third
  ticker-both-sides case.**
  This morning's brief made **USO long** idea #1 on a supply-shock thesis (Brent $108.34, Saudi pipeline
  shut). At 14:04 the board carries **WTI as a CONFIRMED SHORT** (+0.8%, two co-signs, @tradfi) *and*
  **WTI long as a KNIFE CATCH** (−2.8%). USO peaked at +3.28% pre-market and is now **+0.93%** — it gave
  back two-thirds of the move.
  The honest read: the idea was scored +3 on regime-and-price with **no board row at all** at 09:26,
  which I flagged as its conflict. Five hours later the board arrived and it arrived on the other side.
  A same-session reversal of a thesis backed by a physical supply event is a caution about how quickly
  these confirmations decay — the ZEC/ETH confirmations on 11 September lasted about six hours too.
  Third instance today of one ticker on both sides (NVDA twice, now WTI), which strengthens the proposed
  rule: **a ticker on both sides counts as no signal.**

- **2026-09-14 15:04 — my USO idea would have stopped out the same session it was published.**
  This morning's brief made **USO long** idea #1 at an entry of **160.19** with a **−3% stop at 155.38**.
  USO peaked at +3.28% pre-market, and at 15:04 it trades **155.41** — **−2.98% from that entry, three
  cents above the stop.** The trade as written is a stop-out on day one.
  Two things went wrong and they are separable. The **thesis** was a real supply event (Saudi pipeline
  shut, Brent $108.34) and it is not obviously refuted — Brent is still above $100. The **entry** was the
  pre-market high after a 9% weekly rally, which is the same chase error logged against ETH on
  11 September: right idea, price already extended. The 09:26 scoring gave it `price_confirms: true` on a
  **+3.28% pre-market print**, which is precisely the input that reversed at the open on 10 September.
  **Proposed fix, and it applies to the brief's own scoring rather than to the desk:** `price_confirms`
  should not be satisfied by a pre-market print more than ~2% above the prior close. On today's numbers
  that single condition would have disqualified the USO entry while leaving the thesis intact for a
  pullback entry.
  The board then confirmed **WTI short** at +1.3% with three co-signs — the opposite side of my own top
  idea, five hours after publication.

- **2026-09-15 09:25 — what is improving and what is not, separated cleanly.**
  Three behaviours have measurably changed in a week and one has not:
  **Improving — entry price.** DRAM re-entered 6.1% *below* its own exit, ETH 0.04% above. Two consecutive
  entries at or below the prior exit after ten above it.
  **Improving — holding.** DRAM was held ~75 minutes and closed **+$47.12**, the first green DRAM sequence
  in this record; both ETH and ZCSH were carried overnight (`intraday_quantity 0`), the first overnight
  carry since 8 September, rather than round-tripped.
  **Not improving — size.** 20.27u Friday, 20.89u Monday, **19.91u today**. Margin 1.99× where grade 0
  permits zero. Time-to-rebuild after going flat has *compressed*: 18 hours Thursday, 2 hours Monday.
  **Monday's DRAM trade is the whole argument in miniature:** correct entry, held not churned, closed
  green — for $47.12, because it was one of three positions each carried at ten units. The good habits
  are being executed at a size that makes them irrelevant to the P&L, while the bad one sets the loss.
  Today's version: both held names sit **within 1% of their −3% stops** (ZCSH 0.75%, ETH 1.0%). A
  double stop-out at current sizes realises about **−$490** on top of what is open; at the 3-unit cap it
  would be about **−$140**. Nothing about either direction call has to change to alter that number.
  The payoff ratio has now fallen through 1.0: **2.42× over the month → 1.01× last week → 0.77× now**
  (avg win $129.11 vs avg loss $168.28) at a 25% win rate. That combination is unprofitable at any size.

- **2026-09-15 09:25 — the emptiest board in this record, scoring +0.21.**
  Fifteen rows and **zero** confirmed candidates, zero knife catches, zero crowded — all three
  classifications empty for the first time. Longs average +0.29% against shorts at −0.55%, which produces
  a mildly positive **+0.21** from essentially no information. The score is arithmetically correct and
  substantively meaningless. Worth a note in the scoring: **a board with zero confirmations and fewer
  than ~20 rows should contribute a damped score, not a full-weight one** — at weight 2 this reading is
  currently doing as much work in the composite as the −0.66 of 10 September, which came off 24 rows with
  five knife catches.

- **2026-09-15 12:03 — both stops hit, and the size multiplied the loss by 3.4×.**
  At 10:41 ET both positions were closed: **ETH 1000 @ 22.99 for −$1,160.10** and **ZCSH 300 @ 88.95 for
  −$1,175.73**. Today's realised is **−$2,335.83** against a **$506.10** daily limit — **4.6× the cap**,
  the largest single-day breach in this record. The desk is flat with $24,348.70 of cash and no margin.
  **This was priced in advance and the arithmetic held.** At the 10:04 check-in ETH was already through
  its −3% stop at 9.22 units, and the note read: stop-out costs about −$820 at current size versus
  roughly −$267 at cap. Both names then fell further before the exit, so the actual numbers are larger,
  but the ratio is the point:
  · ETH lost **$1.16/share**; 1,000 shares = −$1,160. At the 3-unit cap (314 shares) = **−$364**.
  · ZCSH lost **$3.92/share**; 300 shares = −$1,176. At the 3-unit cap (82 shares) = **−$321**.
  · Actual **−$2,336** versus **≈−$685** at cap. **The direction calls were identical; the size
  multiplied the loss 3.4×.**
  The exits themselves were correct — both names were through or at their stops and both were sold.
  Entry timing was fine (ETH 0.04% above its own prior exit, DRAM 6.1% below). Holding was fine (both
  carried overnight, not round-tripped). **Every behaviour logged as improving over the past week did
  improve, and the session still lost $2,336, because the one behaviour that did not improve is the one
  that sets the number.**

- **2026-09-16 09:26 — the payoff ratio has collapsed to 0.13×, and the winners are what vanished.**
  Four readings of the same measure:
  · Month to 10 Sep — 39% hit rate, avg win **$550.38**, avg loss −$227.62, **2.42×** → **+$7,565.25**
  · Week to 11 Sep — 23%, $497.70 / −$151.86, 1.01× → −$388.85
  · Week to 15 Sep — 25%, $129.11 / −$168.28, 0.77× → −$2,630.14
  · **Week to 16 Sep — 16%, $31.86 / −$239.45, 0.13× → −$4,901.10**
  **The average win fell 94% while the average loss barely moved.** The hit rate going 39% → 16% on
  25 trades is well inside noise; what is not noise is that no position is being held long enough, or
  sized small enough to be held long enough, to become a large winner. The month worked because a
  sub-40% hit rate was paired with winners 2.4× the size of losers. That is the whole edge and it is gone.
  Every symbol in the window is negative for a third consecutive week: ZCSH −$2,147.76 (8 closes),
  ETH −$1,762.42 (5), DRAM −$540.22 (6), HOOD −$233.06 (2), event contracts −$188.21 (3), ARKG −$29.43.

- **2026-09-16 09:26 — the largest re-entry-above-exit yet: ZCSH bought 10.1% above yesterday's stop-out.**
  ZCSH was stopped out yesterday at **88.95** for −$1,175.73. This morning it was re-entered at **97.97**
  — **10.1% above that exit**, on a stock that gapped **+8.2%** from its own close. Eleventh instance of
  the pattern and nearly double the previous worst (5.5%, ZCSH on 9 September).
  The rest of the book is nearly right, which is what makes this legible: one position of a permitted
  three, 4.10 units against a 9.0 ceiling, **zero margin**, $14,136.78 of cash — the second-cleanest book
  this record has measured. Size is no longer the binding error this morning; **entry price is.**
  Also today, before this brief was written: **five pre-market closes, five losses, −$309.20** — already
  65% of the $479 daily limit with the session yet to open. Two new OVERNIGHT flags (ZCSH, ETH) match
  that: three fills each outside 9am–8pm ET. And **ARKG** appeared and was closed inside the same window,
  a name that has never been in a position snapshot at any check-in.

- **2026-09-16 12:04 — margin redrawn inside two hours, and BHYP is back.**
  At 10:08 the manual desk held one position, 8.27 units, **zero margin** and $4,176.96 of cash. At 12:04
  it holds ZCSH 300 @ 99.85 (**12.44u**) and BHYP 100 @ 44.08 (1.83u) — **14.27 units** on
  **−$10,317.23** of cash, gross **1.43×** where grade 0 permits none. ZCSH was added to at roughly
  **101.99**, above its own 99.85 average: averaging up into a position already 4.1× its cap.
  **BHYP is the notable name.** It carried this record's only completed CHURN ban (7 round trips netting
  **−$1,596.35**, ban ran to 10 September) and was the worst single symbol of the trailing month. It has
  now been re-established. The ban expired six sessions ago and nothing carried forward from it — which
  is the practical weakness of a time-boxed ban: it ends, and the ticker returns with no record attached.
  One-sigma day on ZCSH alone is **$2,532** against a **$482.80** limit — **5.25×**. The position is only
  +$79.50 open; the whole of today's gain in it (+10.4% on the day) has been given back by adding at
  higher prices as it rose.
  Fifth instance of one ticker on both sides of the board: **INTC is a confirmed long (+2.1%) and a
  knife-catch short (−2.3%) simultaneously.** ZEC has moved from confirmed to CROWDED at five co-signs.

- **2026-09-16 14:02 — first green session in seven, and the entry I called the worst on record made money.**
  Today closed the manual desk at **+$45.03 realised**, breaking a run of six consecutive losing sessions
  (−$1,159.52 / −$442.28 / −$883.59 / −$945.39 / −$358.88 / −$2,404.04). The account is up **$308.21** on
  the day at $24,262.85, flat, **zero margin**, every hard limit satisfied.
  The morning was −$309.20 across five pre-market closes; the afternoon was **+$354.23** across five:
  ZCSH 200 @ 99.35 (+$113.69), BHYP 50 @ 44.33 (+$12.50), ZCSH 50 @ 101.34 (+$72.92), ZCSH 300 @ 100.57
  (+$143.94), BHYP 300 @ 44.30 (+$11.18).
  **The ZCSH entry at 97.97 — 10.1% above the prior day's 88.95 stop-out, which this morning's brief called
  the largest re-entry-above-exit on record — finished net positive.** ZCSH's five closes today total
  **+$107.85**. Recording that plainly because the brief criticised it twice before the outcome was known.
  It does not change the case against the pattern: eleven instances, and the argument is about expectation
  across all of them, not this one. But the one-sided version of the record would be wrong.
  What did work today is visible and worth keeping: **the position was scaled out in three tranches on the
  way up (200, 50, 300) rather than round-tripped**, and the desk finished flat rather than rebuilding.
  That is the first session in this record where an oversized position was reduced into strength instead
  of being carried to a stop.

- **2026-09-17 09:26 — correction: 16 September ended at −$547.22, not the +$45.03 I reported.**
  At the 14:02 check-in I reported +$45.03 realised and called it the first green session in seven. It was
  accurate to that minute and wrong by the close. After 15:00: BHYP 400 @ 44.45 (−$51.80), ZCSH 300 @
  107.44 (−$186.41), event contracts (−$23.52), then **ZCSH 220 after hours at ~104.34 (−$330.50)**.
  **Final: −$547.22 across 15 closes.** The losing run was not broken.
  The specific failure mode is one I had already described in the same check-in and then narrated as a
  success: I praised the afternoon scale-out (200/50/300 into strength) as "the first session where an
  oversized position was reduced into strength instead of being carried to a stop." It was — and then the
  position was rebuilt at 107.62 and liquidated twice more, the second time after hours 3.0% below the
  earlier exit. **Reporting a mid-session number as a session outcome is the error; the check-in cadence
  invites it and I should date-stamp such claims as provisional until the close.**

- **2026-09-17 09:26 — third leverage record in four sessions, and the first ticker to carry three flags.**
  Gross **2.102×**, above 2.089× (14 Sep) and 2.034× (11 Sep). ZCSH 350 @ 107.35 is **16.05 units**
  against a 3-unit cap — 5.4× — and 76% of the book; ETH 500 @ 23.46 is 4.98u. Book **21.02 units** on
  **−$26,018.81** of cash at a grade that permits no margin. One-sigma day **$3,854** against a **$472**
  limit, **8.17×**.
  **ZCSH now carries CHURN (16 round trips, −$1,918.14), OVERNIGHT (7 fills outside hours) and REVENGE
  (16 Sep) simultaneously** — the first name in this record to hold three at once.
  Two measurement notes worth keeping. **ETH and ZCSH show the identical 0.82× ratio and differ 2.7× in
  daily risk** (±3.37% vs ±9.13%); the ratio is a regime read and the absolute vol is what sizes a
  position, and conflating them is how a 5-unit ETH and a 16-unit ZCSH end up looking equally "NORMAL".
  And the **week's win rate recovered to 40% while the payoff stayed at 0.18×** — four of today's closes
  were 5-share ZCSH sales booking ~$23 each, which lift the count and move no money. Win rate is the
  wrong number to watch on this book.

- **2026-09-17 12:03 — holding produced the largest open gain in this record: ZCSH +$4,340.**
  ZCSH 350 @ 107.35 marks **119.75**, **+15.7% on the session**, and the position is **+$4,340.00** open.
  ETH 500 @ 23.46 is +$52.50. Book open **+$4,392.50**; the account is up **$3,420** since the 10:03
  check-in, and **no trade has been placed since four 5-share sales at 08:19.**
  This is the behaviour the 11 September month review identified as the actual edge — THYP +$1,150/close,
  ZEC +$2,096 on one trade, BTC +$3,410 over thirteen — and it is the first time since that review that
  the desk has held a large winner through a double-digit move instead of round-tripping it. Recorded as
  a success with the same specificity the failures get.
  The unresolved half: the gain is **unrealised and concentrated**. ZCSH is **15.15 units** against a
  3-unit cap, 78% of a book at **1.940× gross** on −$26,018.81 of cash, and its one-sigma day is
  **$3,827** against a **$553.31** limit — **7.63×**. A single one-sigma down day gives back 88% of the
  open gain. Yesterday is the precedent: +$45.03 at 14:02 became −$547.22 by the close.
  Scaling out partially resolves both at once, which is what 16 September got right between 10:51 and
  13:18 before the rebuild undid it. Selling 284 of 350 at 119.30 books roughly **+$3,393**, leaves 66
  shares in a name that is working, and takes the book from 19.40 units to about 7.5 — inside every limit
  for the first time while holding a winner.

- **2026-09-17 15:03 — the full arc of a board idea, and $840 of an unrealised gain given back.**
  **INTC lifecycle, start to finish in three sessions:** not on the board 15 Sep → consensus-without-
  confirmation at 100.52 on 16 Sep (idea #2 in that brief, entry 100.55, stop 97.53) → confirmed three
  sessions running → **CROWDED at four co-signs today at +7.6%**, trading 110.59. That is **+10.0% from
  the quoted entry**, and the board's own contrarian flag now marks it as late consensus. The complete
  arc — unnoticed, consensus, confirmed, crowded — took three sessions, which is the practical lifespan
  of a signal on this board and matches the six-hour confirmation decay logged on 11 September.
  **ZCSH, meanwhile, has given back $840 of an unrealised gain with no trade placed.** 119.75 at 12:03 →
  118.48 at 14:03 → **117.35** now; open **+$4,340.00 → +$3,895.50 → +$3,500.00**. The trim flagged at
  every check-in today would have booked about **+$3,393 at 12:03 and +$2,741 now** — roughly $652 of
  trim value lost in three hours, on top of the $444.50 lost in the previous two.
  ETH was closed at 14:35, 500 @ 23.425 for **−$17.10** — a clean, small exit on a confirmed name, and
  the first position this week closed within 0.1% of its basis. ETH's week nonetheless finishes
  **−$1,779.52 over six closes.**
  Today's realised stands at **+$75.75**; the book is ZCSH alone at **15.35 units**, gross 1.535×, with a
  one-sigma day of **$3,750** against a **$535.32** limit — **7.01×**. Twenty-seven minutes to the close.

## 18 Sep 2026 — pre-open rule review

**A held winner survived a session for the first time.** ZCSH 350 @ 107.35 showed +$3,500
unrealised at the 15:03 check-in on 16 Sep. It was not scaled out and not rebuilt higher;
it was carried, ZCSH settled 17 Sep at 120.09, and the position closed +$4,459 unrealised.
At this morning's 116.77 bid it is +$3,297. Every prior large open gain in this record was
either flushed and re-entered above the exit, or given back. Recording the counter-example
with the same care as the failures.

**New record: BHYP re-entered 15.1% above its own exit.** Bought back this morning in six
pre-market clips 07:46–09:01 ET, 250 shares, average 51.15, against exits at 44.45 and 44.30
on 16 Sep and a 46.85 close yesterday (+9.2%). Previous record was ZCSH at 97.97 versus an
88.95 exit on 16 Sep, +10.1%. This is the 13th instance of the pattern and 4.6× the 2% chase
band. Structure of the fills is the new detail: the three cheapest clips are the three
smallest (75 shares over 75 minutes), and 175 shares — 70% of the position — filled inside
thirty seconds at 09:01 at the three highest prices of the morning. Size follows price up.

**Proposed rule (unadopted), applied against my own idea today.** The 14 Sep proposal —
`price_confirms` should not be satisfied by a pre-market print more than ~2% above the prior
close — was written after my USO idea stopped out on day one. IBIT would have scored +2 on
price this morning at +2.01%. One basis point outside. Marked it as failing the test rather
than rounding in favour of an idea I generated, because a rule only applied when it is
convenient is not a rule.

**Win rate is not the number.** Week to 18 Sep: 48% hit rate, the best since the month
review, on a week that is −$3,075.45 over 27 closes. Avg win $43.18 vs avg loss $259.77,
payoff 0.17×. Fifth consecutive sub-1.0 reading: 1.01× → 0.77× → 0.13× → 0.18× → 0.17×.
Average win is down 92% from $550.38 (month to 10 Sep); average loss has barely moved.

**Tradeable-instrument gap, 7th instance: NEAR.** The board's only confirmed candidate this
morning (+3.4%, 1 co-sign) has no equity instrument at this broker. ZEC is on the consensus
list again — 4th signal in six sessions. The crypto sleeve that produced +$2,096.54 on
7 Sep still has no gauge, no unit size and no stop.

**Discipline analyzer gap.** BHYP does not raise a flag this week — three closes is below
every threshold — yet this morning's entry is exactly the behaviour CHURN and the chase band
exist to catch. The flags are backward-looking on closed round trips; the worst entry in this
record is invisible to all of them.

**Overnight session, counter-example.** GLD bought 35 @ 399.75 at 20:45 ET Thursday
(all_day_hours), sold 35 @ 401.67 at 07:37 ET Friday: +$67.21, +0.48%, eleven hours. The
OVERNIGHT flag fires on this window because fills there usually cost money on this book.
This one did not.

### 18 Sep 10:12 ET — TURN CONFIRMED, grade 0 → +1

At the 09:15 pre-open the TURN ALARM fired with exactly one fresh green idea on the
new (long) side — NEAR +3.4% — against a threshold of three, so no shift was made.
One hour later the board carries **three** confirmed longs: NEAR +3.8% (2 co-signs),
ZEC +0.7%, MU +0.7%. Fresh 6h flow is 35 long / 9 short while the winner skew is still
short. workflow.md's condition is met. **Grade shifts one notch toward the new side:
0 → +1.** Storm veto is not active (SPY 0.97×, QQQ 0.92×), so the shift stands. Per
protocol the adjusted posture is traded from the NEXT check-in, not this one.

This is the second confirmed turn in this record (first: 9 September) and the first
where the alarm fired at the pre-open and confirmed intraday — the one-hour gap between
alarm and confirmation is the whole argument for not acting on the alarm alone.

**INTC completed the full board lifecycle in four sessions.** Absent 15 Sep →
consensus-without-confirmation at 100.52 on the 16th (my idea #2 at 100.55) → confirmed
three sessions → CROWDED at four co-signs at 110.59 on the 17th → **KNIFE CATCH at −2.5%
today**. Every stage of the taxonomy, in order, on one ticker. The crowded reading was
the sell signal it is documented to be.

**Ticker-on-both-sides, 7th instance: BTC.** BTC long is CROWDED at 4 co-signs and +3.1%;
BTC short is a KNIFE CATCH at −2.8%. Same asset, same board, opposite classifications.
The proposed rule — a ticker appearing on both sides counts as no signal, not a
confirmation — would have excluded BTC from today's count. It was not among the three
that confirmed the turn, so the outcome is unchanged either way.

**MU, against my own morning call.** I scored MU −2 WATCH ONLY at 978.67 on the grounds
that a +0.12% pre-market print was not confirmation and the board skew was net short.
Both conditions have since flipped: MU is a confirmed candidate and the skew has turned.
MU trades 996.70, +1.96% on the day and +1.84% above the entry I declined to rank. The
reasoning was right for the data available at 09:15; the data changed within an hour.

### 18 Sep 12:06 ET — the chase I called the worst on record made money

BHYP was sold at 10:24 ET, 260 @ 51.5711, for **+$108.05** — 4.4 hours after the entry
I described this morning as the largest re-entry-above-exit in this record. The entry was
+15.1% above its own 16 Sep exit and 4.6× outside the 2% chase band; it returned +0.80%.

**This is the second consecutive time the most extreme chase on record has been
profitable** (ZCSH at +10.1% above its own exit on 16 Sep netted +$107.85 across five
closes). Two of the two largest instances have made money. The aggregate case against the
pattern rests on 13 instances and on expectation, not on these outcomes — but it is worth
stating plainly that the two most extreme examples have both paid, and that my framing has
now been contradicted twice by the tape within a day of writing it.

**HOOD bought 110 @ 117.925 at 10:24 ET, twelve minutes after the grade shift.** That is
+7.4% above yesterday's 109.81 close, outside the 2% band again. It is also the first
entry in weeks that the system would sanction on direction and source: HOOD is a CONFIRMED
CANDIDATE on the board at +5.0% with two co-signs, long, aligned with the +1 grade the turn
protocol produced an hour earlier. Size is the problem, not the idea — 4.76 units against a
3-unit hard cap. Per the month review, HOOD is the name where five large closes made
+$3,378 while the other fifteen lost $1,443.

**The turn protocol's leading indicator was right.** At 10:12 fresh flow was long while
winners were short; by 12:06 the winner skew had flipped to long and the alarm cleared.
Two hours from confirmation to coincident agreement. This is the first clean end-to-end
validation of the workflow.md turn sequence in this record.

**VVV collision, second occurrence.** The board carries VVV long +1.8% (@notthreadguy,
0.7h old). Broker VVV is Valvoline, trading 27.19 — close enough to the Venice AI perp's
price that the 9 September contamination could repeat exactly. The proposed rule is still
unadopted: a board row counts only when the broker instrument matches the board's asset,
not merely its symbol.

Manual desk realised today: **+$175.26** over two closes, both winners (GLD +$67.21,
BHYP +$108.05). Provisional until the close — the 16 September lesson stands.

### 18 Sep 14:03 ET — ZEC ran the full arc to CROWDED and turned negative

ZEC is now **CROWDED at 5 co-signs and −0.9%**, down from +0.9% at the 12:06 check-in.
That is the second ticker in two days to complete confirmed → crowded → negative; INTC
did it yesterday into today and is a knife catch at −3.8%.

This cuts against my own framing of the crypto-sleeve open item. I have logged ZEC four
times as "the board's best idea, unreachable" — the implication being that the missing
instrument was costing money. Today is the first time the signal was watched all the way
through, and it decayed to negative before it crowded. One observation is not a base rate,
but the honest version of that open item is now: *the sleeve has no gauge, no unit size and
no stop, and the signal it would have traded has not yet been shown to be worth reaching.*
The gap is a process defect either way; the cost of it is unproven.

**HOOD sits at 3 co-signs.** One more makes it crowded, which on the only two observations
available today has been the exit signal, not the entry. The desk owns 110 shares at
117.92, +$279.40 at 120.46.

### 18 Sep 15:03 ET — largest weekend carry in this record

With 57 minutes to the close the desk holds ZCSH 350 @ 107.35 (**15.32 units**, +$3,384.50)
and HOOD 110 @ 117.92 (4.91 units, +$167.20), gross **2.023×**, book **20.23 units** against
a 9.0 ceiling. If both are carried, this is the largest weekend exposure in this record.

The number that frames it: ZCSH gauges at **158.1% annualised, ±9.96% for one day**. On a
$40,957 position that is **±$4,079 of one-sigma over a single session** — 7.6× the $535
daily loss limit — before any weekend gap, in a crypto-linked name that trades continuously
while the equity wrapper does not. The book's entire margin cushion is $802.42 of buying
power.

**This is the same clock that decided the last two sessions in opposite directions.** On
16 September the desk was +$45.03 at 14:02 and closed −$547.22 after three liquidations
between 15:07 and 18:34. On 17 September it held and was rewarded with a +$4,459 mark.
The distinction the record supports is trimming into strength versus flushing and
re-entering higher — not holding versus selling as such.

## 21 Sep 2026 — pre-open rule review

**Correction to the 18 Sep 14:03 entry.** I wrote that ZEC "decayed to negative before it
crowded" and concluded the crypto sleeve's missing-instrument cost was "unproven." That
read an intraday wiggle as a trend. On the 7-day board window **ZEC is +37.5% with 17
co-signs and NEAR is +45.6% with 7** — the two largest moves on the board are the two names
the sleeve cannot reach. The cost is demonstrated, not unproven, and the open item is now
the most expensive one in this record. The methodological error was judging a multi-day
signal on a two-hour sample; workflow.md line 137 requires running both windows precisely
so this does not happen, and I ran both and then reasoned from one.

**Friday's provisional figure held.** No trade after 10:24; 18 September closed +$175.26
over two closes, both winners. First time since the 16 September correction that a
mid-session green number survived to the bell — and the first session in this record with
no trade placed after 10:24.

**The weekend carry paid +$2,853.10.** ZCSH +4.5% and HOOD +5.6% from Friday's closes; open
P&L +$6,420.77. The exposure flagged on Friday was real either way — 14.55 units of a name
that moves ±9.30% a day, across three calendar days, against $978 of buying power — and the
outcome does not retire the sizing point. Third consecutive instance of a position held
against the sizing rules paying.

**Everything gapped.** AMD +3.54%, IBIT +4.95%, INTC +5.87% pre-market. All three are board
confirmations and all three fail the 14 September pre-market rule, so the best score today
is +1. This is the day that rule costs the most, which is the only real test of it.

**INTC: four classifications in four sessions.** Confirmed 16 Sep → CROWDED at 4 co-signs
17 Sep → KNIFE CATCH at −3.8% 18 Sep → CONFIRMED again 1.3h ago. Whatever the board is
measuring on this ticker is not persistent enough to hold a position against. USELESS shows
the same instability in reverse: knife catch at −7.3% on 17 Sep, confirmed at +2.7% today.

**Board skew has a sample-size problem today.** 23 rows: 22 long, **one** short. The +0.54
board score is computed from a single row on one side. Recomputed from the long side alone
it is +0.136 and the composite lands at +0.207 scaled — still grade 0, so the posture is
unaffected, but the score should not be quoted as a skew measurement at this n.

**Composite missed +1 by 0.002.** 0.239 × 5/3 = 0.3983 against a 0.400 threshold. Friday's
+1 came from the turn protocol and does not carry over; today opens at 0 on its own inputs.

**X inbox correction.** Previous briefs said the digest was unchanged since 18 August. The
file header reads `AS_OF 2026-08-03T02:45:00Z`, 19 posts — a fortnight staler than reported.
35th consecutive miss.

**Wider-volatility clause unapplied on two of three positions.** HOOD's GARCH persistence is
0.999, so its ratio is meaningless and the governing number is 73.9% annualised — above
risk.md's 60% threshold, which calls for one unit and a −5% stop. It is held at 4.70 units
with no stop. RAM is the same diagnosis at 118.5% for a sixth session.

### 21 Sep 10:11 ET — the gap was sold, and my pre-open marks were too generous

At 09:51 HOOD 110 was sold @ 122.013 for **+$450.23**; at 09:52 META 20 was bought
@ 705.39. Both regular-hours market orders.

**The pre-market marks in this morning's brief overstated the book by roughly $630.** I
published open P&L of +$6,420.77 using pre-market prints of ZCSH 123.00 and HOOD 126.49.
HOOD actually sold twenty-one minutes into the session at **122.013** — the gap gave back
$4.48 a share, about half of it, before the position could be realised at the quoted level
— and ZCSH is 122.09 rather than 123.00. Realised plus open now stands at $5,788.38 against
the $6,420.77 I published at 09:21. The figures were correctly labelled as pre-market, but
the lesson is the same one the `price_confirms` rule encodes from the other side: a
pre-market print is not a price you can transact at, whether you are buying into it or
marking a position against it. **Pre-open book values should be quoted off the prior
settled close, with the pre-market move shown separately.**

**HOOD's exit was well timed against the board.** A fresh HOOD long posted 1.7h ago is a
KNIFE CATCH at −2.9%; the desk was out before that classification landed. The name also
illustrates the full round trip: bought Friday at 117.925 (+7.4% above the prior close,
which I criticised), sold today at 122.013 for +$450.23. Third consecutive chase entry to
close profitably.

**META bought +5.95% above Friday's close**, at 4.93 units against a 3-unit cap. It is a
CONFIRMED board candidate at +4.7% with 2 co-signs, so the idea has support; the entry is
again a gap-chase and the size is again above cap. That is now four consecutive entries
where the direction matched a board confirmation and the size did not match risk.md.

**ZEC is a knife catch at −2.4% on today's window while sitting +37.5% on the 7-day.**
Same contradiction as this morning, now in the opposite direction from Friday's. The
window, not the signal, is what keeps changing.

### 21 Sep 12:05 ET — scoring the pre-market rule on the day I said would test it

This morning I disqualified all three tradeable board ideas for gapping more than 2% above
Friday's close, and wrote that "this is the day the rule is worth the most and the day it is
hardest to keep." It is fair to score it.

| idea | my quoted entry | 12:05 | move | 2-unit P&L foregone |
|---|---|---|---|---|
| AMD  | 579.66 | 610.50 | **+5.32%** | ≈ +$308 |
| INTC | 114.98 | 123.53 | **+7.44%** | ≈ +$436 |
| IBIT | 48.30  | 48.65  | +0.72% | ≈ +$43 |

**The rule cost roughly $787 on paper today**, across three ideas it would have sized at two
units each. That is the largest single-day cost of the rule since it was proposed on
14 September, and it is the honest counterweight to the USO stop-out that motivated it.

The qualification that matters: **AMD and INTC are both CROWDED now** — 5 and 6 co-signs —
which is the board's documented exit signal, not an entry. The move happened between the
posting and the crowd, which is a window the desk has never yet caught, on either side of
this rule. The rule's real cost is therefore bounded by whether that window is capturable at
all, and nothing in this record yet shows that it is.

**ZEC is a knife catch at −4.1% on today's window and +37.5% on the 7-day.** Third
observation of the same contradiction in one session. Whatever else the board measures, its
today-window classification of a multi-day trend is not stable enough to act on.

Book at 12:05: ZCSH 350 @ 107.35 → 119.975, +$4,419.25, **14.78u**; META 20 @ 705.39 →
722.515, +$342.50, **5.09u**. Gross 1.987×, book 19.87u against the 9.0 ceiling. Realised
today +$450.23, provisional.

### 21 Sep 14:04 ET — META reaches CROWDED while held; ZCSH gives back $1,907

**META is CROWDED at 6 co-signs and +9.0% since posting, and the desk owns it.** This is
the first time in this record a held position has reached the crowded threshold while being
watched. The three prior observations all went the same way inside one or two sessions:
INTC crowded at 4 co-signs on 17 Sep at 110.59 → knife catch at −3.8% on the 18th; ZEC
crowded at 5 co-signs on the 18th → knife catch at −5.9% today; AMD crowded at 7 today after
running +7.9% from posting. Three for three is not a base rate, but the taxonomy documents
crowded as contrarian information, and the desk is now on the wrong side of that reading
with 5.32 units.

**ZCSH gave back $1,907.50 of open gain today without a single trade.** It marked 123.00
pre-market, 122.09 at 10:11, 119.98 at 12:05 and **117.55 now — below Friday's 117.72
close**. Open P&L on the position has fallen from +$5,477.50 at the pre-open to +$3,570.00.
The account has tracked it down: $29,594.72 → $28,974.77 → $28,405.20 → **$27,989.15**,
which is −$1,605.57 on the day despite +$450.23 of realised gains.

This is the counterweight to Friday's entry. On Friday I recorded that holding a winner beat
flushing and re-entering, and that was true of that session. Today the same position held
through the same hours cost $1,907.50 of paper gain. **Neither holding nor trimming is free;
what is not free is holding 14.70 units of a name that moves ±9.30% a day and calling the
decision settled by the last outcome.** Gross is back above 2× at 2.002×.

### 21 Sep 15:11 ET — applying this morning's own fix

At 10:11 I proposed that pre-open book values be quoted off the prior settled close, with
the pre-market move shown separately, after my 09:21 marks overstated the book by ~$630.
Applying it to today: Friday's settled close values the book at 350 × 117.72 + 110 × 119.82
= $54,382.20 against cash of −$27,353.78, an account of **$27,028.42**. It is now
**$28,294.55** — the session is **+$1,266.13**, not the −$1,300.17 that comparing against
this morning's inflated pre-market figure would suggest. The two framings differ by $2,566
on the same day. The settled-close baseline is the one that does not move.

META is crowded at **8 co-signs** now, up from 6 at 14:04, +8.9% since posting; the position
is +$753.20 off a +$780.70 high. ZCSH recovered to 118.50 from 117.55, +$4,002.50 open.
Gross 1.991×, book 19.91u. Realised +$450.23, provisional.

## 22 Sep 2026 — pre-open rule review

**A single board row moved the grade a full notch.** The board carries a CLDX short posted
36 minutes ago at −32.3%. On a 20-row board with 6 short rows, that one entry drags the
short average to −5.242%, clamps the board sub-score at +1.00 and prints **+1 RISK ON**.
Excluding it, the short side averages +0.170, the board scores +0.06 and the grade is
**0 MIXED**. The row also fails to reconcile: CLDX the equity trades 35.89 against a 37.89
close, a −5.3% move, not a 32% one.

**I am operating on 0** — the conservative of two defensible readings on contaminated input,
and the one that permits no margin. Recorded explicitly because it is a judgement call that
overrides the tool's printed output, and the reasoning should be auditable.

**Proposed rule:** winsorise board rows at ±15% before averaging, and require at least three
rows on a side before the skew is scored at all. Either clause alone produces 0 today. This
is the third consecutive session with a board-sample defect — 26 vs 9 on Friday, 22 vs 1 on
Monday, 14 vs 6 with one outlier today — and the first where it changed the posture.

**Monday was the best session in this record: +$1,530.48 over five closes.** META 20 sold at
743.64 for +$765.00, one minute after the 15:11 check-in flagged it crowded at 8 co-signs;
ZCSH 50 at 116.15 for +$511.31; HOOD 110 at 122.013 for +$449.68. Three large wins in one
session, the first since the month review. **The week has flipped positive at +$1,143.58
with a 1.81× payoff** — first reading above 1.0 in seven.

Honest qualification on that payoff: the average loss fell from $269.24 to $92.67 **largely
because the 15 September pair rolled out of the rolling window**, not because losses got
smaller. The average win rising from $56.57 to $167.74 is real.

**Every loss in the last two sessions came from the extended session.** ETH was churned four
times between 15:33 and 20:27 on Monday — buy 550, buy 50, sell 600, buy 700, sell 700 — for
−$195.51. META, correctly exited at 743.64 on the crowded signal, was re-bought in three
clips averaging 741.28 between 20:13 and 22:29 and sold this morning at 735.672 for
−$114.20. The regular-hours record over the same span is +$1,726.20 across four closes.
**The edge was in what was closed during regular hours; the leak was in what was opened
after them.**

**BTC 500 @ 38.05 bought 09:01, into the storm band.** GARCH reads **1.28× — the first
position in this record gauged into STORM while held** — 60.7% annualised, ±3.82% a day.
That clears risk.md's 60% wider-volatility threshold, which calls for one unit and a −5%
stop: 76 shares, stop 36.14. It is held at 6.53 units with no stop. The board also had BTC
CROWDED at 7–8 co-signs through yesterday afternoon. Three rules point the same way.

**First session in this record with zero confirmed board candidates.** There is nothing to
enter. The scorer returns −2 on ZCSH and −3 on BTC — both positions the book already owns.

**ZCSH's CHURN flag cleared** (13 closes now netting +$195.08) and Monday's 50-share trim at
116.15 is the first scale-out into strength in this record that was not followed by a
rebuild at a higher price.

### 22 Sep 10:12 ET — BTC held 22 minutes; RAM turns green; the board firms on its own merits

**BTC was sold at 09:23 for −$34.50 after a 22-minute hold.** Bought 500 @ 38.05 at 09:01,
sold @ 37.981 at 09:23 — the position this morning's brief flagged as the first in this
record gauged into a storm band at 6.53 units. It was gone before the brief had been
published twenty minutes. The exposure the brief warned about lasted less than the time it
took to write about it, which is worth recording: **the sizing critique was right about the
size and irrelevant to the outcome, because the holding period was 22 minutes.** A rule
about units and stops has little purchase on a book that turns over intraday.

**ETH re-established at 800 @ 26.30 — the sixth round trip in under 24 hours.** Sold last
night at 26.45 for −$171.01, re-bought this morning in four clips: 100 @ 26.2397, 100 @
26.22, 100 @ 26.1981 (all extended hours, 09:23–09:29) and 500 @ 26.355 (regular, 09:35).
The re-entry is *below* the exit, so it is not a chase — but ETH already carries CHURN at 5
round trips netting −$269.68 and is now **7.26 units**, the largest non-ZCSH position in
weeks, in the only name on the book with an active churn flag.

**RAM is green for the first time.** 15.1095 against a 14.62 basis: **+$4.89, +3.09%**, and
the agentic sleeve is $163.07. It was −14.98% on 17 September. Eight consecutive up
sessions. No rule in risk.md reaches it in either direction — the exits are premium-based
and this is an equity — so it has run its entire arc untouched by the framework that is
supposed to govern it.

**The board firmed on its own merits, and the grade still holds at 0.** This morning I
excluded a CLDX outlier to operate on 0 rather than the printed +1. At 10:12 the long side
averages +1.494% across 18 rows and the short side is negative even after winsorising at
±15% (−2.332%), so the board scores **+0.956 winsorised, not +0.06**. Recomputing the
composite with that: (3×0.01 + 2×(−0.17) + 2×0.956)/7 = 0.229, scaled **+0.382** against a
+0.400 threshold. **Still grade 0**, by 0.018. The morning call does not need revising, but
the reason has changed: it is no longer the outlier holding the grade down, it is
conditions.

### 22 Sep 12:11 ET — the crowded signal was right for eighteen hours, then wrong

I have now cited the CROWDED → fade pattern four times, most forcefully on Monday at 14:04
and 15:11 when META hit 6 then 8 co-signs. The desk sold META at 743.64 on that signal for
+$765.00. Follow-through:

- Tue 09:00 — META 735.45. The signal was right; the exit saved ~$8/share.
- Tue 12:11 — META **749.67**, above the 743.64 exit. The signal is now wrong by $6.03/share,
  about $120 on the 20 shares sold.

META is still crowded on the board, now at 5 co-signs but only **+0.5% since posting**,
versus +9.0% yesterday. So the *board row* has faded exactly as the taxonomy predicts while
the *price* has recovered past the exit. Those are two different claims and I have been
running them together. **The accurate version: crowded has reliably marked the end of the
board idea's run in this record; it has not reliably marked a price top.** The exit was
sound on the day and the pattern's predictive claim needs narrowing to what the data
supports.

**ZEC is a confirmed candidate again at +2.4% — the fifth confirmation in eight sessions**,
and still has no instrument at this broker. It is the most persistent signal on this board
and the one the account has never been able to act on.

Book at 12:11: ZCSH 300 @ 107.59 → 123.13, **+$4,662.00**, 12.71u; ETH 800 @ 26.30 → 26.10,
**−$160.00**, 7.18u. Gross 1.989×, book 19.89u. Realised today −$148.70, provisional.
Agentic sleeve $162.29, RAM +2.60% and still above basis.

### 22 Sep 14:11 ET — three losses today, all three opened inside 24 hours

ETH 800 sold at 13:19 @ 26.21 for **−$72.00** — the **seventh ETH round trip in 26 hours**,
taking the name to −$341.68 over six closes this week. DRAM 325 bought @ 63.06 twenty-four
seconds later.

**Today's realised is −$220.70 across three closes, and all three were losers. Every one of
them was a position opened within the previous 24 hours:**

| close | opened | held | result |
|---|---|---|---|
| META 20 @ 735.672 | 20:13–22:29 Mon, extended | ~11h | −$114.20 |
| BTC 500 @ 37.981 | 09:01 Tue | **22 min** | −$34.50 |
| ETH 800 @ 26.21 | 09:23–09:35 Tue | ~4h | −$72.00 |

Meanwhile the one position held longer than a day — ZCSH, open since 15 September — is
**+$4,706.70**. Monday's three large winners were held 4.5h, 1.5 days and 6 days
respectively. **The pattern across the last two sessions is not about direction or size: it
is that nothing opened and closed inside a day has made money, and everything carried has.**
Six of the last seven sub-24-hour round trips have lost.

**DRAM is the second-best-disciplined entry of the week.** Bought at 63.06 against a 61.58
close — **+2.40%**, just outside the 2% band, versus BHYP +9.2%, HOOD +7.4% and META +5.95%.
Only BTC's entry at −0.52% below the prior close was tighter. Recorded because the chase
criticism has been made repeatedly and this one barely qualifies.

**MU is on both sides of the board — 8th instance.** MU long is a confirmed candidate at
+3.6% (@notthreadguy, 2.5h); MU short is a knife catch at −5.0% (@michaeljburry, 5.3h).
Same ticker, same board, opposite classifications, both live. The proposed rule — a ticker
on both sides counts as no signal, not a confirmation — is still unadopted after eight
occurrences.

Book: ZCSH 300 @ 107.59 → 123.28, +$4,706.70, 12.63u; DRAM 325 @ 63.06 → 63.34, +$91.00,
7.03u. Gross **1.965×**, book 19.65u. Agentic sleeve $164.73, RAM **+4.14%**, a new high.

## 22 Sep 20:55 ET — $500 added to the agentic sleeve; why it still cannot trade

The user deposited $500. Sleeve: RAM 10.8194 (≈$163.91) + **$500.00 cash**, $663.91 total.

**The premium cap and the entry filters are incompatible for every board name.** strategy.md
requires delta 0.30–0.50, 2–6 weeks to expiry, liquid large/mid caps; risk.md caps premium at
$20–60 per position ($20–40 at grade 0) and $120 total. Checked against the cheapest
board-confirmed equity today, MRVL at $262, Oct 16 calls (22 Sep close marks):

| strike | mark | delta | cost / contract |
|---|---|---|---|
| 265 | 17.40 | 0.52 | $1,740 |
| 275 | 13.83 | 0.44 | $1,383 |
| 285 | 10.68 | 0.36 | **$1,068** ← cheapest contract meeting the 0.30 floor |
| 300 | 7.18 | 0.27 | $718 |
| 350 | 1.83 | 0.08 | $183 |

The cheapest in-filter contract is **18× the $60 cap**; even a 0.08-delta lottery ticket is 3×.
The other confirmed names are dearer still (TSM $452, MU $1,096, SNDK $1,887). Under the rules
as written, the only reachable underlyings are stocks under roughly $20–25, which the board
almost never confirms. This — more than the cash floor — is why the sleeve has gone 155
check-ins without an agent-placed order, and adding cash does not change it. Raised with the
user as a decision; no rule changed and no order placed.

### 22 Sep 21:10 ET — first agent-placed order in ••••0924
User confirmed. Resting GTC stop placed on RAM under the new risk.md: sell 10 @ stop $13.00
(entry 14.62 − max(6%, 1.5 × 7.38% one-day sigma) = −11.1%). Order 6ab326f3, state queued,
verified on re-fetch. The 0.819405 fractional share cannot carry a stop order.
