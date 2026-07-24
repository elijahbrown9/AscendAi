# workflow.md — The daily machine

## 9:00am ET — Risk Environment Brief (no trades)
1. Storm gauge: `python3 tools/garch.py` on SPY, QQQ + all held underlyings
2. paste.trade board: `curl https://paste.trade/api/board?window=today&lens=spot`
3. Conditions panel: VIX, BTC 24h, Brent, KOSPI, geopolitical headlines
4. Discipline: `python3 tools/discipline.py` on the week's realized trades
5. Composite score: `python3 tools/risk_score.py` → grade (−2 … +2)
6. Rebuild `terminal/dashboard.html` with the day's data and republish the
   Terminal artifact (same file path + url → same link)

### Composite score weights
- Storm gauge (GARCH regimes + IV vs forecast): **weight 3** — the anchor
- Conditions panel (VIX/Brent/KOSPI/BTC/geo): **weight 2**
- paste.trade winner skew: **weight 2**
- X notifications sentiment: **weight 1** (0 while offline)

Each input scores −1…+1; composite = Σ(weight × score) / Σ(active weights).
Grade boundaries in `strategy.md`. The gauge can veto: if GARCH says STORM on
both indexes, the grade cannot be better than −1 regardless of other inputs.

## 10:00am / 12:00pm / 2:00pm / 3:00pm ET — Momentum loop (trades)
Manage exits first (stops, scales, expiry, earnings calendar), then entries if
a slot is open — direction and sizing per the morning grade, filters per
`strategy.md`, limits per `risk.md`. Every action reported after the fact.

## Session-start checklist (the guide prompt)
When a session opens with the standard prompt: read strategy.md, risk.md,
workflow.md → pull portfolio value, buying power, open positions, cash →
state the current grade and whether any rule fires right now → wait. No trade
is placed until the state has been read back and there is a rule-based reason.

## Weekly (Friday close)
Week wrap: realized P&L by trade, rule adherence audit, discipline flags on
both accounts, and one improvement noted for next week.
