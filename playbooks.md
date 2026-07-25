# playbooks.md — Analytical frameworks (run on request or where wired below)

## P1 — Market Context Read (on demand: user names a ticker)
Compute from daily bars via `tools/ta_read.py`, then present:
1. **EMA posture**: price vs Daily 12/25 EMAs. Below both → they act as
   resistance. Above both → support. Between → contested, say so.
2. **Key levels**: two closest resistance and support levels, each with the
   reasoning (swing pivot, prior gap, round number, high-volume close).
3. **Stochastic RSI discipline**: Daily StochRSI overbought + price into
   resistance → don't chase longs. Oversold + price into support → don't
   chase shorts.
4. **Confluence read**: a couple of lines — the cleanest read, where the
   action is vs where it's noise. NO entries, stops, or targets — the
   trader does that part.

## P2 — Post-Trade Reflection (after every closed trade, asked ONE AT A TIME)
1. "Did you make any mistakes during the trade?"
2. If yes → "Which part of the lifecycle: Execution, Management, or Closure?"
3. "What mistakes, in as much detail as possible?"
Log answers via `journal.py reflect` (stage + description). The monthly
review aggregates WHERE in the lifecycle mistakes cluster and what TYPE
repeats — the pattern, not the incident, is the deliverable.

## P3 — Thesis Red Team (user pastes a full thesis + chart; also run on any
## STRONG-conviction system idea before entry)
A couple of lines per section:
1. **Higher-timeframe counter** — strongest counterargument from a higher
   timeframe than the one being traded. If HTF disagrees, say so directly.
2. **Underweighted confluence** — factors visible in the trader's own thesis
   that are being dismissed or minimized.
3. **Catalyst risk** — recent or scheduled events (macro, on-chain,
   earnings) that could invalidate the thesis within the trade's duration.
4. **The other trader** — the thesis an experienced trader on the OTHER side
   would write. The job is not to talk anyone out of the trade; it is to
   make the opposing view concrete.
