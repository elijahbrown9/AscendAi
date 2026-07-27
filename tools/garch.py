"""GARCH(1,1) volatility forecaster — built from scratch, no third-party trading code.

Model: r_t = mu + e_t,  e_t ~ N(0, h_t),  h_t = omega + alpha*e_{t-1}^2 + beta*h_{t-1}
Fit by maximum likelihood (Nelder-Mead, numpy only).
Outputs: fitted params, next-day vol, annualized current vol, 21-day forecast vol,
         and long-run (unconditional) vol for mean-reversion context.
"""
import json, math, sys
import numpy as np

DATA = sys.argv[1]
TRADING_DAYS = 252

def neg_loglik(params, r):
    omega, alpha, beta = params
    if omega <= 0 or alpha < 0 or beta < 0 or alpha + beta >= 0.999:
        return 1e10
    h = np.empty_like(r)
    h[0] = np.var(r)
    for t in range(1, len(r)):
        h[t] = omega + alpha * r[t-1]**2 + beta * h[t-1]
    h = np.maximum(h, 1e-12)
    return 0.5 * np.sum(np.log(h) + r**2 / h)

def nelder_mead(f, x0, args, steps=2000, tol=1e-10):
    n = len(x0)
    simplex = [np.array(x0)]
    for i in range(n):
        p = np.array(x0, dtype=float); p[i] *= 1.2 if p[i] != 0 else 0.01
        simplex.append(p)
    for _ in range(steps):
        simplex.sort(key=lambda p: f(p, *args))
        best, worst, second = simplex[0], simplex[-1], simplex[-2]
        centroid = np.mean(simplex[:-1], axis=0)
        if abs(f(worst, *args) - f(best, *args)) < tol:
            break
        refl = centroid + (centroid - worst)
        if f(refl, *args) < f(best, *args):
            exp = centroid + 2 * (centroid - worst)
            simplex[-1] = exp if f(exp, *args) < f(refl, *args) else refl
        elif f(refl, *args) < f(second, *args):
            simplex[-1] = refl
        else:
            contr = centroid + 0.5 * (worst - centroid)
            if f(contr, *args) < f(worst, *args):
                simplex[-1] = contr
            else:
                simplex = [best + 0.5 * (p - best) for p in simplex]
    simplex.sort(key=lambda p: f(p, *args))
    return simplex[0]

def fit_garch(closes):
    closes = np.asarray(closes, dtype=float)
    lr = np.diff(np.log(closes))
    r = lr - lr.mean()                      # demeaned returns
    var = r.var()
    # init: modest persistence
    x0 = [var * 0.05, 0.08, 0.88]
    omega, alpha, beta = nelder_mead(neg_loglik, x0, (r,))
    # current conditional variance path
    h = np.empty_like(r); h[0] = var
    for t in range(1, len(r)):
        h[t] = omega + alpha * r[t-1]**2 + beta * h[t-1]
    h_next = omega + alpha * r[-1]**2 + beta * h[-1]
    lr_var = omega / (1 - alpha - beta)     # long-run variance
    # k-step-ahead average variance over next 21 days
    k = 21
    hs, hk = [], h_next
    for _ in range(k):
        hs.append(hk)
        hk = lr_var + (alpha + beta) * (hk - lr_var)
    ann = lambda v: math.sqrt(v * TRADING_DAYS)
    # When alpha+beta -> 1 the unconditional variance omega/(1-a-b) is not
    # identified: the long-run anchor (and therefore the current/long-run
    # ratio) becomes meaningless. Flag it rather than reporting a false CALM.
    unreliable = (alpha + beta) > 0.98
    return {
        "omega": omega, "alpha": alpha, "beta": beta,
        "persistence": alpha + beta,
        "longrun_unreliable": unreliable,
        "next_day_vol_pct": math.sqrt(h_next) * 100,
        "ann_current_vol_pct": ann(h_next) * 100,
        "ann_21d_avg_vol_pct": ann(np.mean(hs)) * 100,
        "ann_longrun_vol_pct": ann(lr_var) * 100,
        "n_obs": len(r),
    }

raw = json.load(open(DATA))
for res in raw["data"]["results"]:
    sym = res.get("symbol") or res.get("instrument_symbol")
    bars = [b for b in res["bars"] if not b.get("interpolated")]
    closes = [float(b["close_price"]) for b in bars]
    out = fit_garch(closes)
    print(f"\n=== {sym}  ({out['n_obs']} daily returns) ===")
    print(f"  GARCH(1,1): omega={out['omega']:.3e} alpha={out['alpha']:.3f} "
          f"beta={out['beta']:.3f}  persistence={out['persistence']:.3f}")
    print(f"  Next-day expected move (1 sigma): +/-{out['next_day_vol_pct']:.2f}%")
    print(f"  Annualized vol  — now: {out['ann_current_vol_pct']:.1f}%  "
          f"21d-avg forecast: {out['ann_21d_avg_vol_pct']:.1f}%  "
          f"long-run: {out['ann_longrun_vol_pct']:.1f}%")
    ratio = out['ann_current_vol_pct'] / out['ann_longrun_vol_pct']
    if out["longrun_unreliable"]:
        print(f"  !! persistence {out['persistence']:.3f} > 0.98 — long-run anchor NOT "
              f"identified; the {ratio:.2f}x ratio is meaningless. Judge on absolute "
              f"vol ({out['ann_current_vol_pct']:.1f}%) and treat shocks as non-decaying.")
    else:
        print(f"  Ratio {ratio:.2f}x -> "
              f"{'CALM' if ratio < 0.8 else 'STORM' if ratio > 1.25 else 'NORMAL'}")
