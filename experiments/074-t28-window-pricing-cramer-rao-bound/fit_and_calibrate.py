"""exp-074 Phase 3/4 -- the actual 9-column two-tone FIT + its own
null-calibration test, per Red Team's Phase-2 docket item 7 and PLAN.md's
Iteration-51 queue item 3 ("a properly-calibrated null construction ...
explicitly gated on item 1's result, not built in parallel"). Item 1
(desk_check_pricing.py) priced the design's conditioning and, per the
Phase-2 Red Team audit, did NOT establish CLOSURE-CONFIRM: two blind
critics (PHOTONICS, THERMODYNAMICS), independently confirmed by Red Team,
showed a conditioning-only bound is not a valid substitute for actually
fitting the design. This script does the fit Red Team's docket item 7
calls for, gated behind a genuinely new null-calibration test before any
pair's two-tone significance is scored -- the same G0-e(ii)/R6 discipline
exp-073 established, generalized one level upstream to a NEW candidate
standing rule (R7, Red Team's phase2_redteam_audit.md Sec 6): a
conditioning/VIF-based pricing of an un-fit design is not sufficient
evidence either way; the design must be fit and null-calibrated.

Two structural improvements over exp-073's own G0-e(ii):
  (1) The null is a direct generalization of exp-073's own T2-3 sign-flip
      construction (Freedman-Lane-style), applied one level up: reduced
      model = X9 with the primary ramp column (R_q, index 4) DROPPED (an
      8-column model, "X8"); full model = X9. Sign-flip the FULL model's
      own residual, add back the reduced model's own fit, refit X9,
      extract R_q^surr. This tests whether R_q is significant WITHIN the
      two-tone model, i.e. whether the original 5-column finding survives
      once a modeled second tone (T21's own established fringe) is fit
      jointly rather than priced only through its Gram-matrix conditioning.
  (2) A GENUINELY order-preserving residual-structure calibration leg --
      a circular shift of each config's own real per-config carrier-fit
      residual (exp-069/071's C40/C60/C70/C80, at each config's own
      native n_grid=400 free-period fit, exactly `build_residual_pool`'s
      per-config inputs before exp-073 pooled and flattened them) --
      closing the exact gap exp-073's own Phase-5 erratum named and
      queued for Iteration 51 (`phase4_results.md`, "A genuinely
      order-preserving leg ... is queued for Iteration 51"). A circular
      shift preserves 100% of a real residual vector's own theta-adjacent
      autocorrelation structure (every pairwise lag is preserved exactly,
      only the theta-anchoring changes) -- unlike exp-073's pooled,
      order-discarded flat resample, which measurably could not (and did
      not) differ from its own i.i.d. Gaussian leg (Pearson r=0.907).

PRE-REGISTERED PREDICTION (committed before the official run, see
phase3_synthesis.md / NOTES.md): the 9-column sign-flip null is expected
to ALSO be anti-conservative, and by a comparable-or-LARGER margin than
exp-073's 5-column finding (1.7x-5.7x at alpha=0.10/0.01). Reason,
computed and disclosed here in advance: the leverage-weighted ratio
driving this failure mode, lev9_Rq = sum(row9_i^2 * diagM9_i) /
sum(row9_i^2) with row9 = pinv(X9)[4,:] and diagM9 = 1-diag(X9 pinv(X9)),
measures 0.586-0.596 across the four pairs at the real fitted carriers --
LOWER (worse) than exp-073's own 0.79-0.80 for the 5-column case, which
already produced 1.7x-5.7x inflation. A lower ratio predicts a larger
inflation. If this prediction is WRONG (the 9-column null passes
calibration), that is itself a genuine surprise, disclosed as such.

Zero FDTD. Zero lab/ diff. Reuses desk_check_pricing.py's basis (already
CHECK0-verified against exp-072's committed record) without modification.
"""

import json
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import desk_check_pricing as dcp  # noqa: E402  (this cycle's own verified basis)

ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
EXP069 = os.path.join(ROOT, "experiments", "069-t21-block-mini-period-match-power-up")
EXP071 = os.path.join(ROOT, "experiments", "071-t28-absorb-depth-causal-test")

FREE_PAIRS = [("C40", "C60"), ("C60", "C70"), ("C70", "C80")]  # G0-b: C40-C80 is the exact sum, not free
ALL_PAIRS = dcp.PAIRS

N_SURR = 20000          # real-data sign-flip test, per pair
K_CAL = 1000            # calibration Monte-Carlo draws per (leg, sigma) cell
N_SURR_CAL = 4000        # sign-flip surrogates per calibration draw (cheaper than N_SURR; disclosed)
ALPHAS = (0.01, 0.05, 0.10)
IID_SIGMAS = (0.0005, 0.002, 0.008)   # matches exp-073's own G0-e(ii) sigma grid, same units (C_empty)

SIGN_FLIP_SEED = 74051     # fixed, frozen at Phase-3 commit, unchanged thereafter
CAL_SEED = 74052           # fixed, frozen at Phase-3 commit, unchanged thereafter


# ===================================================== the two-tone fit itself (Red Team docket item 7)
def build_X9_X8(theta, data, a, b, T_fringe_deg=dcp.T_FRINGE_DEG):
    """Real X9 (9-col, at the pair's own REAL fitted primary carrier and
    T21's established fringe with its own data-fit phase -- identical
    construction to desk_check_pricing.price_pair, not re-derived) and
    X8 (X9 with column 4, R_q, removed -- the reduced/null model for the
    sign-flip test below)."""
    xbar = float(np.mean(np.sin(np.radians(theta))))
    cos_c = math.cos(math.radians(dcp.CENTER_DEG))
    series_a, series_b = data[a], data[b]
    delta_ab = series_b - series_a
    carrier = dcp.carrier_fit(theta, series_a, series_b)
    T_x, psi = carrier["T_x"], carrier["psi"]
    X5 = dcp.design_matrix(theta, T_x, psi, xbar)
    Cbar = 0.5 * (series_a + series_b)
    T_fx = math.radians(T_fringe_deg) * cos_c
    _, psi_fr, _ = dcp._amp_phase_at(theta, Cbar, T_fx, xbar)
    X9 = np.column_stack([X5, dcp.tone_cols(theta, T_fx, psi_fr, xbar)])
    X8 = np.delete(X9, 4, axis=1)
    return X9, X8, delta_ab, dict(T_mean_deg=carrier["T_mean_deg"], T_x=T_x, psi=psi, psi_fringe=psi_fr)


def fit_real_pair(theta, data, a, b):
    X9, X8, delta_ab, meta = build_X9_X8(theta, data, a, b)
    n, p9 = X9.shape
    pinv9 = np.linalg.pinv(X9)
    coef9 = pinv9 @ delta_ab
    resid9 = delta_ab - X9 @ coef9
    R_q9 = float(coef9[4])
    gram9_inv = np.linalg.inv(X9.T @ X9)
    SE_Rq9_ols = math.sqrt(np.sum(resid9 ** 2) / (n - p9) * gram9_inv[4, 4])
    z9 = abs(R_q9) / SE_Rq9_ols if SE_Rq9_ols > 0 else float("nan")
    H9 = X9 @ pinv9
    diagM9 = 1.0 - np.diag(H9)
    row9 = pinv9[4, :]
    lev9 = float(np.sum(row9 ** 2 * diagM9) / np.sum(row9 ** 2))
    return dict(pair=f"{a}-{b}", n=n, p9=p9, R_q9=R_q9, SE_Rq9_ols=SE_Rq9_ols, z9=z9,
                RSS9=float(np.sum(resid9 ** 2)), lev9_Rq=lev9, meta=meta,
                cond9=float(np.linalg.cond(X9)))


# ===================================================== sign-flip null, generalized from exp-073's T2-3
def sign_flip_9col_surrogates(delta_ab, X9, X8, n_surr, rng):
    pinv9 = np.linalg.pinv(X9)
    pinv8 = np.linalg.pinv(X8)
    coef9 = pinv9 @ delta_ab
    yhat0 = X8 @ (pinv8 @ delta_ab)
    resid9 = delta_ab - X9 @ coef9
    n = len(delta_ab)
    S = rng.choice(np.array([-1.0, 1.0]), size=(n, n_surr))
    surr = yhat0[:, None] + resid9[:, None] * S
    Rq_surr = (pinv9 @ surr)[4, :]
    return Rq_surr, float(coef9[4])


def two_sided_p(obs, surr):
    n_surr = len(surr)
    return (1 + int(np.sum(np.abs(surr) >= abs(obs)))) / (n_surr + 1)


def holm_adjust(pvals):
    names = list(pvals)
    m = len(names)
    order = sorted(names, key=lambda k: pvals[k])
    adj, running = {}, 0.0
    for i, name in enumerate(order):
        val = min(1.0, (m - i) * pvals[name])
        running = max(running, val)
        adj[name] = running
    return adj


# ===================================================== real per-config residuals (theta-adjacency preserved)
def per_config_residuals(data):
    """The four configs' own real per-config free-period-fit residuals
    (exp-069's C40/C80, exp-071's C60/C70, native n_grid=400 fit) -- SAME
    inputs as exp-073's build_residual_pool, kept as four SEPARATE
    31-point vectors (not concatenated/flattened) so their theta-adjacent
    structure can be preserved by a circular shift, rather than destroyed
    by pooling."""
    theta = data["theta"]
    x = np.sin(np.radians(theta))
    xbar = float(np.mean(x))
    u = x - xbar
    cos_c = math.cos(math.radians(dcp.CENTER_DEG))
    # exp-071's own results.json carries per_config_free_periods -- all
    # four configs' own native (n_grid=400) free-period fit collected
    # together -- exactly the source exp-073's own build_residual_pool
    # (run.py:177) reads as `per_config_free_native`.
    with open(os.path.join(EXP071, "results.json")) as f:
        d071 = json.load(f)
    out = {}
    for key in ("C40", "C60", "C70", "C80"):
        p_star = d071["per_config_free_periods"][key]["p_star_deg"]
        Tx = math.radians(p_star) * cos_c
        fit = dcp._fixed_period_fit(u, data[key], Tx)
        w = 2 * math.pi / Tx
        yhat = fit["c0"] + fit["a"] * np.cos(w * u) + fit["b"] * np.sin(w * u)
        out[key] = data[key] - yhat
    return out


def circular_shift(vec, shift):
    return np.roll(vec, shift)


# ===================================================== G-cal: null calibration (mandatory HALT gate, R7/R6-generalized)
def calibrate_null(theta, X9, X8, resid_pool_a, resid_pool_b, rng_master):
    """Two legs, matching exp-073's own G0-e(ii) shape but with a
    genuinely order-preserving leg this time:
      (A) i.i.d. Gaussian noise at IID_SIGMAS, R_q_true=0 by construction.
      (B) circular-shift leg: delta_ab_null = circshift(resid_A, s_A) -
          circshift(resid_B, s_B), independent random shifts s_A,s_B each
          draw -- preserves each config's own real residual autocorrelation
          exactly (a circular shift changes only the theta-anchor, not any
          pairwise lag relationship), R_q_true=0 in expectation (E[shifted
          residual]=0 by construction of the original fit) but genuinely
          structured, non-Gaussian, non-i.i.d. noise.
    For each cell: draw K_CAL synthetic H0 datasets, run the SAME
    sign_flip_9col_surrogates construction (N_SURR_CAL surrogates each),
    two-sided p-value, empirical rejection rate at each alpha. PASS bar:
    inside alpha +/- 3*sqrt(alpha*(1-alpha)/K_CAL) at EVERY (leg,sigma/draw,alpha)
    cell -- else this pair's null is HALT_NULL_MISCALIBRATED_9COL."""
    n = len(theta)
    results = {"iid_leg": {}, "circ_leg": {}}

    for sigma in IID_SIGMAS:
        rej = {a: 0 for a in ALPHAS}
        for k in range(K_CAL):
            y0 = rng_master.normal(0.0, sigma, size=n)
            surr, obs = sign_flip_9col_surrogates(y0, X9, X8, N_SURR_CAL, rng_master)
            p = two_sided_p(obs, surr)
            for a in ALPHAS:
                if p <= a:
                    rej[a] += 1
        results["iid_leg"][sigma] = {a: rej[a] / K_CAL for a in ALPHAS}

    n_a = len(resid_pool_a)
    rej = {a: 0 for a in ALPHAS}
    for k in range(K_CAL):
        sA = int(rng_master.integers(0, n_a))
        sB = int(rng_master.integers(0, n_a))
        y0 = circular_shift(resid_pool_a, sA) - circular_shift(resid_pool_b, sB)
        surr, obs = sign_flip_9col_surrogates(y0, X9, X8, N_SURR_CAL, rng_master)
        p = two_sided_p(obs, surr)
        for a in ALPHAS:
            if p <= a:
                rej[a] += 1
    results["circ_leg"] = {a: rej[a] / K_CAL for a in ALPHAS}
    return results


def calibration_pass(cal):
    worst = {}
    all_pass = True
    for leg_name, leg in [("iid_leg", cal["iid_leg"]), ("circ_leg", {"circ": cal["circ_leg"]})]:
        for cond_key, rates in leg.items():
            for a, rate in rates.items():
                tol = 3 * math.sqrt(a * (1 - a) / K_CAL)
                lo, hi = a - tol, a + tol
                ok = lo <= rate <= hi
                worst[f"{leg_name}:{cond_key}:{a}"] = dict(rate=rate, band=[lo, hi], pass_=ok)
                if not ok:
                    all_pass = False
    return all_pass, worst


def main():
    t0 = __import__("time").time()
    data = dcp.load_data()
    theta = data["theta"]
    resid_pools = per_config_residuals(data)

    per_pair_fit = {}
    for a, b in ALL_PAIRS:
        per_pair_fit[f"{a}-{b}"] = fit_real_pair(theta, data, a, b)

    rng_cal = np.random.default_rng(CAL_SEED)
    calibration = {}
    cal_pass_all = True
    for a, b in FREE_PAIRS:
        X9, X8, delta_ab, meta = build_X9_X8(theta, data, a, b)
        cal = calibrate_null(theta, X9, X8, resid_pools[a], resid_pools[b], rng_cal)
        ok, detail = calibration_pass(cal)
        calibration[f"{a}-{b}"] = dict(raw=cal, pass_=ok, detail=detail)
        cal_pass_all = cal_pass_all and ok

    combined_verdict = None
    scored = {}
    if not cal_pass_all:
        combined_verdict = "HALT_NULL_MISCALIBRATED_9COL"
    else:
        rng_score = np.random.default_rng(SIGN_FLIP_SEED)
        pvals = {}
        for a, b in FREE_PAIRS:
            X9, X8, delta_ab, meta = build_X9_X8(theta, data, a, b)
            surr, obs = sign_flip_9col_surrogates(delta_ab, X9, X8, N_SURR, rng_score)
            p = two_sided_p(obs, surr)
            pvals[f"{a}-{b}"] = p
        holm = holm_adjust(pvals)
        n_resolved_relaxed = sum(1 for v in pvals.values() if v <= 0.10)
        n_resolved_holm05 = sum(1 for v in holm.values() if v <= 0.05)
        scored = dict(raw_p=pvals, holm_p=holm,
                      n_relaxed_p10=n_resolved_relaxed, n_holm_p05=n_resolved_holm05)
        if n_resolved_holm05 >= 2:
            combined_verdict = "CONFIRM_R_Q_SURVIVES_JOINT_FIT"
        elif n_resolved_relaxed == 0:
            combined_verdict = "REFUTE_R_Q_DOES_NOT_SURVIVE_JOINT_FIT"
        else:
            combined_verdict = "NEITHER"

    results = dict(
        experiment="074-t28-window-pricing-cramer-rao-bound",
        panel_iteration=51, phase="3-4 (fit + null-calibration, gated)",
        per_pair_fit={k: {kk: vv for kk, vv in v.items() if kk != "meta"} | {"meta": v["meta"]}
                      for k, v in per_pair_fit.items()},
        calibration_pass_all=cal_pass_all,
        calibration=calibration,
        scored=scored,
        combined_verdict=combined_verdict,
        seeds=dict(sign_flip_seed=SIGN_FLIP_SEED, cal_seed=CAL_SEED),
        params=dict(n_surr=N_SURR, k_cal=K_CAL, n_surr_cal=N_SURR_CAL, alphas=list(ALPHAS),
                    iid_sigmas=list(IID_SIGMAS)),
        elapsed_s=__import__("time").time() - t0,
    )
    with open(os.path.join(HERE, "fit_and_calibrate_results.json"), "w") as f:
        json.dump(results, f, indent=2, default=float)

    print("Real 9-column fit (R_q within the two-tone model, at real fitted carriers):")
    for k, v in per_pair_fit.items():
        print(f"  {k}: R_q9={v['R_q9']:.5f}  SE9={v['SE_Rq9_ols']:.5f}  z9={v['z9']:.2f}  "
              f"lev9_Rq={v['lev9_Rq']:.4f}  cond9={v['cond9']:.1f}")
    print(f"\nCalibration pass (all cells, all free pairs): {cal_pass_all}")
    for k, v in calibration.items():
        print(f"  {k}: pass={v['pass_']}")
        for cell, d in v["detail"].items():
            flag = "OK" if d["pass_"] else "FAIL"
            print(f"    {cell}: rate={d['rate']:.4f} band=[{d['band'][0]:.4f},{d['band'][1]:.4f}] {flag}")
    print(f"\nCombined Verdict: {combined_verdict}")
    if scored:
        print(f"  raw p: {scored['raw_p']}")
        print(f"  Holm p: {scored['holm_p']}")
    print(f"\nelapsed: {results['elapsed_s']:.2f}s")


if __name__ == "__main__":
    main()
