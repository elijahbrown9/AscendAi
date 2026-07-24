# AscendAi — Daily Risk Environment System

Tooling behind the automated daily trading brief for the Robinhood accounts.
All models are implemented from scratch in this repo — no third-party trading
code is fetched or executed.

## Components

| File | Purpose |
|---|---|
| `tools/garch.py` | GARCH(1,1) volatility model ("storm gauge"), fitted by maximum likelihood on daily bars from the broker API. Reports next-day expected move, current/forecast/long-run annualized vol per symbol. |
| `tools/discipline.py` | Trade-discipline analyzer. Reads realized-trade history and flags churn (5+ trades one symbol, net red), overnight-session fills, and revenge-trading streaks. |
| `tools/garch_gauge.pine` | TradingView (Pine v5) indicator version of the storm gauge for chart use. Variance-targeted GARCH recursion with adjustable alpha/beta. |

## Daily Risk Environment Brief (automated, weekdays 9:00am ET)

The scheduled agent run:
1. Pulls a year of daily bars for SPY, QQQ, and every underlying currently held
   in either account, then runs `garch.py` on them.
2. Classifies the regime per index: **CALM** (conditional vol < 0.8× long-run),
   **NORMAL** (0.8–1.25×), **STORM** (> 1.25× long-run anchor).
3. Pulls positions + realized P&L for both accounts and runs `discipline.py`
   on the last week of closed trades.
4. Publishes one brief: regime per index, whether open option premium is
   cheap/fair/rich vs forecast vol, portfolio exposure summary, discipline
   flags, and a risk-posture suggestion (add / hold / reduce).

The brief is informational; trading in the agentic account follows its own
mandate and limits. Nothing here is financial advice.

## Running manually

```bash
python3 tools/garch.py <historicals.json>      # from get_equity_historicals
python3 tools/discipline.py <trades.json>      # from get_pnl_trade_history
```
