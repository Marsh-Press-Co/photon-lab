"""exp-072 -- T28's differential/beat fit of delta_AB(theta) between adjacent
`ABSORB` configs: desk-only re-analysis, zero new FDTD calls.
=============================================================================
Panel Iteration 49 (lead: PHOTONICS, rotation). Executes the Iteration-49
queue's item 1. Phase-2 Red Team audit verdict: PROCEED-WITH-MANDATORY-FIXES,
15 items, ZERO items un-adopted (3 seats' specific remedies overridden and
replaced with Red-Team-derived corrections, documented in
`phase2_redteam_audit.md` Sec 3; every other request from all five blind
critiques adopted in full). This file implements the FIXED design -- not the
Phase-1 proposal as originally written. See `phase3_synthesis.md` for the
full accepted/overridden record.

PRE-REGISTRATION CONTAMINATION DISCLOSURE (Red Team's Phase-2 audit Sec 4,
binding, reproduced here per its own condition 4): during Phase 2, QUANTUM
OPTICS executed the proposed estimator and both candidate nulls on the real
committed data (withholding outcome numbers) and VISION SCIENCE executed the
estimator and PUBLISHED outcome-determining numbers (ΔP, z, rho_c at three
carriers). Red Team then independently computed the observed surrogate
p-values under both nulls. The choice between the unrestricted null (as
Phase-1 originally specified) and the H0-restricted null (QUANTUM's Phase-2
fix) is OUTCOME-DETERMINING between Combined Verdict REFUTED and NEITHER --
Red Team verified this computationally before Phase 3. Per Red Team's ruling:
(1) every docket item is justified by an argument independent of any observed
value (see phase2_redteam_audit.md Sec 4, condition 1); (2) the net effect of
the docket is to make the design STRICTER, not looser (condition 2); (3) a
CONFIRM-shaped outcome this cycle cannot be certified as pre-registered by
any party and MUST be emitted as CONFIRM_UNCERTIFIED rather than CONFIRMED
(condition 3) -- verified inert on this data since no pair reaches RESOLVED
under either null; (4) this paragraph is the required disclosure (condition
4). No threshold below was set or moved after any number was computed.

Zero FDTD calls. Zero `lab/` diff. Reuses `_fixed_period_fit` from exp-069's
run.py verbatim (house convention: never re-derive existing machinery).
"""

import json
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, ROOT)
EXP069 = os.path.join(ROOT, "experiments", "069-t21-block-mini-period-match-power-up")
EXP071 = os.path.join(ROOT, "experiments", "071-t28-absorb-depth-causal-test")
sys.path.insert(0, EXP069)

import run as exp069_run  # noqa: E402  (reuse _fixed_period_fit verbatim)

_fixed_period_fit = exp069_run._fixed_period_fit

CENTER_DEG = 39.0
SEED = 20490072
N_SURR = 20000            # primary significance nulls (docket item 1)
N_SURR_Q95 = 2000         # carrier-consistency-gate calibration (item 6) --
                           # a documented computational economy: the q95
                           # calibration needs a smooth percentile, not a
                           # sharp p-value, and is applied identically and
                           # symmetrically to all four pairs before any
                           # comparison to the observed statistic.
N_GRID_Q95 = 300          # ditto, for the per-surrogate free-period search
N_GRID_CARRIER = 3000     # step-1 common-mode carrier search (Idealization 6)
HOLM_PAIRS = ("C40-C60", "C60-C70", "C70-C80")   # 3 algebraically free (item 14)
T_WRONG_DISPLACED = 3.60  # deg, >=1.5 Rayleigh widths from the carrier (item 10)
T_WRONG_FRINGE = 1.9608   # deg, T21's established fringe -- disclosure only,
                           # 0.6452 Rayleigh widths, NOT a control (item 10)
SAT_DECAY_L = 0.075       # 1/cell, engine-derived (_damping's cubic ramp,
                           # Red Team Attack 6), FIXED not fitted

PAIRS = [
    ("C40", "C60", 20.0),
    ("C60", "C70", 10.0),
    ("C70", "C80", 10.0),
    ("C40", "C80", 40.0),   # derived (= sum of the other three, G0-b) --
                             # never called "independently measured" (item 14)
]


# ===================================================== data loading (G0-a/b/c)
def load_data():
    with open(os.path.join(EXP069, "results.json")) as f:
        d069 = json.load(f)
    with open(os.path.join(EXP071, "results.json")) as f:
        d071 = json.load(f)

    rows069 = {r["theta"]: r for r in d069["block_dense"]["rows"]}
    theta069 = sorted(rows069)
    c40 = np.array([rows069[t]["C_empty_C40"] for t in theta069])
    c80 = np.array([rows069[t]["C_empty_C80"] for t in theta069])
    delta_committed = np.array([rows069[t]["delta"] for t in theta069])

    theta_c60 = [r["theta"] for r in d071["dense_causal"]["rows"]["C60"]]
    theta_c70 = [r["theta"] for r in d071["dense_causal"]["rows"]["C70"]]
    c60 = np.array([r["C_empty"] for r in d071["dense_causal"]["rows"]["C60"]])
    c70 = np.array([r["C_empty"] for r in d071["dense_causal"]["rows"]["C70"]])

    theta = np.array(theta069, dtype=float)

    g0a = dict(
        n_checked=3,
        all_identical=bool(
            np.array_equal(theta, np.array(theta_c60))
            and np.array_equal(theta, np.array(theta_c70))
        ),
    )
    g0b_lhs = (c60 - c40) + (c70 - c60) + (c80 - c70)
    g0b_rhs = c80 - c40
    g0b = dict(max_abs_residual=float(np.max(np.abs(g0b_lhs - g0b_rhs))))
    g0c = dict(max_abs_delta=float(np.max(np.abs(delta_committed - (c80 - c40)))))

    m0 = d071["trend"]["linear_fit"]["slope"]  # (item 9) loaded, never hand-typed
    per_config_free = d071["per_config_free_periods"]

    return dict(theta=theta, C40=c40, C60=c60, C70=c70, C80=c80,
                m0_committed=float(m0), per_config_free_native=per_config_free,
                g0a=g0a, g0b=g0b, g0c=g0c)


# ===================================================== step 1: carrier fit
def _amp_phase_at(theta_deg, series, T_x, xbar):
    """Fit series = c0 + a*cos(w*u) + b*sin(w*u), u = sin(theta)-xbar, T_x
    FIXED -- i.e. fit directly in the SAME u-centered coordinate design_matrix()
    uses, so the returned phase is usable as design_matrix()'s `psi` with no
    extra w*xbar correction. (Fitting in raw x and reusing atan2(b,a) as a
    u-domain phase was a bug caught and fixed here: x = u + xbar, so a
    phase fitted in x needs a w*xbar shift before it means anything in u --
    skipping that shift silently misallocates signal between the carrier
    and ramp columns in design_matrix(), which is exactly the failure mode
    this whole cycle's estimator is built to avoid.)"""
    x = np.sin(np.radians(theta_deg))
    u = x - xbar
    fit = _fixed_period_fit(u, series, T_x)
    amp = math.hypot(fit["a"], fit["b"])
    psi = math.atan2(fit["b"], fit["a"])
    return amp, psi, fit["c0"]


def carrier_fit(theta_deg, series_a, series_b, n_grid=N_GRID_CARRIER):
    """Free-period search + fixed fit on the common-mode Cbar = (A+B)/2.
    Returns T_mean_deg (P*), T_x (sin-theta period), amplitude a, phase psi
    (in the u = sin(theta)-xbar coordinate, matching design_matrix())."""
    cbar = 0.5 * (series_a + series_b)
    free = exp069_run._free_period_search(theta_deg, cbar, center_deg=CENTER_DEG,
                                           n_grid=n_grid)
    T_mean_deg = free["p_star_deg"]
    cos_c = math.cos(math.radians(CENTER_DEG))
    T_x = math.radians(T_mean_deg) * cos_c
    xbar = float(np.mean(np.sin(np.radians(theta_deg))))
    amp, psi, _ = _amp_phase_at(theta_deg, cbar, T_x, xbar)
    return dict(T_mean_deg=T_mean_deg, T_x=T_x, amplitude=amp, psi=psi,
                r_squared=free["r_squared"])


def design_matrix(theta_deg, T_x, psi, xbar, curvature=False):
    """5-column ramped basis [1, cos(theta_c), sin(theta_c), u*cos(theta_c),
    u*sin(theta_c)] at a FIXED carrier (T_x, psi) from step 1.  Optionally a
    6th disclosed curvature column u^2*sin(theta_c) (docket item 15)."""
    x = np.sin(np.radians(theta_deg))
    u = x - xbar
    w = 2 * math.pi / T_x
    theta_c = w * u + psi
    cols = [np.ones_like(x), np.cos(theta_c), np.sin(theta_c),
            u * np.cos(theta_c), u * np.sin(theta_c)]
    if curvature:
        cols.append(u * u * np.sin(theta_c))
    return np.column_stack(cols)


# ===================================================== nulls (docket item 1)
def fourier_phase_surrogates(y, n_surr, rng):
    """Unrestricted null: phase-randomize y's own spectrum (amplitude spectrum
    preserved exactly, Hermitian symmetry enforced). Returns (n, n_surr)."""
    n = len(y)
    Y = np.fft.rfft(y)
    mag = np.abs(Y)
    n_freq = len(Y)
    phases = rng.uniform(0, 2 * np.pi, size=(n_freq, n_surr))
    phases[0, :] = 0.0                      # DC stays real
    if n % 2 == 0:
        phases[-1, :] = 0.0                 # Nyquist stays real (even n)
    surrY = mag[:, None] * np.exp(1j * phases)
    surr = np.fft.irfft(surrY, n=n, axis=0)
    return surr  # (n, n_surr)


def restricted_null_surrogates(y, X4, n_surr, rng):
    """H0-restricted null (item 1): fit the 4-column H0 basis (R_q=0), phase-
    randomize THAT fit's residual, add back the H0-fitted series."""
    pinv4 = np.linalg.pinv(X4)
    coef0 = pinv4 @ y
    yhat0 = X4 @ coef0
    resid0 = y - yhat0
    resid_surr = fourier_phase_surrogates(resid0, n_surr, rng)
    return yhat0[:, None] + resid_surr  # (n, n_surr)


def holm_adjust(pvals, m=None):
    """Holm-Bonferroni step-down. pvals: dict name->p. m: correction count
    (item 14: 3, the algebraically-free pairs; C40-C80 excluded, reported
    unadjusted/derived)."""
    names = list(pvals)
    m = m or len(names)
    order = sorted(names, key=lambda k: pvals[k])
    adj = {}
    running_max = 0.0
    for i, name in enumerate(order):
        raw = pvals[name]
        val = min(1.0, (m - i) * raw)
        running_max = max(running_max, val)
        adj[name] = running_max
    return adj


# ===================================================== one pair, full pipeline
def analyze_pair(data, key_a, key_b, d_absorb, rng):
    theta = data["theta"]
    series_a, series_b = data[key_a], data[key_b]
    delta_ab = series_b - series_a
    n = len(theta)

    # ---- step 1: common-mode carrier (Idealization 6: n_grid=3000 removes
    # the exp-069 n_grid=400 quantization; adds no resolving power)
    carrier = carrier_fit(theta, series_a, series_b)
    T_x, psi = carrier["T_x"], carrier["psi"]
    x = np.sin(np.radians(theta))
    xbar = float(np.mean(x))

    # ---- step 2: 5-column ramped fit (+ item 15's disclosed 6th column)
    X5 = design_matrix(theta, T_x, psi, xbar, curvature=False)
    X6 = design_matrix(theta, T_x, psi, xbar, curvature=True)
    pinv5 = np.linalg.pinv(X5)
    coef5 = pinv5 @ delta_ab
    cond5 = float(np.linalg.cond(X5))
    coef6 = np.linalg.pinv(X6) @ delta_ab
    cond6 = float(np.linalg.cond(X6))
    c0, A_i, A_q, R_i, R_q = (float(v) for v in coef5)

    amp = carrier["amplitude"]
    f_bar = 1.0 / T_x
    delta_f_obs = R_q / (2 * math.pi * amp) if amp != 0 else float("nan")
    delta_P_obs = -(delta_f_obs / f_bar) * carrier["T_mean_deg"]

    # item 5: A_q relabeled -- "half the phase difference at window centre",
    # A_q = 2*a*sin(chi), chi = pi*Delta_f*xbar + Delta_psi/2. Delta_psi
    # (the theta=0 deg extrapolation) is NEVER reported -- it is ~26 sigma_u
    # outside this window (Red Team Attack 3).
    phase_channel = abs(A_q) / amp if amp != 0 else float("nan")
    freq_channel = abs(R_q) * float(np.std(x - xbar)) / amp if amp != 0 else float("nan")
    strain_channel = abs(R_i) * float(np.std(x - xbar)) / amp if amp != 0 else float("nan")
    strain_flag = bool(strain_channel > freq_channel)

    # ---- G0-d: conditioning gate
    ill_conditioned = cond5 > 100.0

    # ---- nulls (docket item 1): BOTH reported, restricted null gates
    rng_pair = np.random.default_rng(rng.integers(0, 2**63 - 1))
    unrestricted = fourier_phase_surrogates(delta_ab, N_SURR, rng_pair)
    R_q_unrestricted_surr = (pinv5 @ unrestricted)[4, :]

    X4 = X5[:, :4]
    restricted = restricted_null_surrogates(delta_ab, X4, N_SURR, rng_pair)
    R_q_restricted_surr = (pinv5 @ restricted)[4, :]

    def two_sided_p(obs, surr):
        return float((1 + np.sum(np.abs(surr) >= abs(obs))) / (len(surr) + 1))

    p_unrestricted = two_sided_p(R_q, R_q_unrestricted_surr)
    p_restricted = two_sided_p(R_q, R_q_restricted_surr)

    # ---- item 6: carrier-consistency gate, recalibrated from the restricted
    # null's own T_delta distribution (q95), replacing the imported 0.414.
    rng_q95 = np.random.default_rng(rng.integers(0, 2**63 - 1))
    q95_surr = restricted_null_surrogates(delta_ab, X4, N_SURR_Q95, rng_q95)
    grid = np.linspace(1.0, 4.0, N_GRID_Q95)
    cos_c = math.cos(math.radians(CENTER_DEG))
    Tx_grid = np.radians(grid) * cos_c
    w_grid = 2 * math.pi / Tx_grid
    # vectorized free-period search across the surrogate batch:
    best_r2 = np.full(q95_surr.shape[1], -np.inf)
    best_Tx = np.full(q95_surr.shape[1], np.nan)
    for gi in range(N_GRID_Q95):
        Xg = np.column_stack([np.ones(n), np.cos(w_grid[gi] * x), np.sin(w_grid[gi] * x)])
        Hg = Xg @ np.linalg.pinv(Xg)
        yhat = Hg @ q95_surr
        ss_res = np.sum((q95_surr - yhat) ** 2, axis=0)
        ss_tot = np.sum((q95_surr - q95_surr.mean(axis=0, keepdims=True)) ** 2, axis=0)
        r2 = 1.0 - ss_res / np.where(ss_tot > 0, ss_tot, np.nan)
        better = r2 > best_r2
        best_r2 = np.where(better, r2, best_r2)
        best_Tx = np.where(better, Tx_grid[gi], best_Tx)
    carrier_stat_surr = np.abs(best_Tx - T_x) / T_x
    q95 = float(np.nanpercentile(carrier_stat_surr, 95))

    T_delta = exp069_run._free_period_search(theta, delta_ab, center_deg=CENTER_DEG,
                                              n_grid=N_GRID_CARRIER)["p_star_deg"]
    T_delta_x = math.radians(T_delta) * cos_c
    carrier_stat_obs = abs(T_delta_x - T_x) / T_x
    carrier_gate_pass = carrier_stat_obs <= q95

    linearization_gate_pass = abs(delta_f_obs) * (float(np.ptp(x))) <= 0.25

    # ---- item 10: wrong-carrier gate (displaced) + fringe disclosure (not a control)
    def at_carrier(T_wrong_deg):
        Tx_w = math.radians(T_wrong_deg) * cos_c
        _, psi_w, _ = _amp_phase_at(theta, 0.5 * (series_a + series_b), Tx_w, xbar)
        X5w = design_matrix(theta, Tx_w, psi_w, xbar)
        pinv5w = np.linalg.pinv(X5w)
        coefw = pinv5w @ delta_ab
        R_q_w = float(coefw[4])
        X4w = X5w[:, :4]
        rng_w = np.random.default_rng(rng.integers(0, 2**63 - 1))
        restr_w = restricted_null_surrogates(delta_ab, X4w, N_SURR, rng_w)
        R_q_w_surr = (pinv5w @ restr_w)[4, :]
        p_w = two_sided_p(R_q_w, R_q_w_surr)
        return R_q_w, p_w

    R_q_wrong_disp, p_wrong_disp = at_carrier(T_WRONG_DISPLACED)
    R_q_fringe, p_fringe = at_carrier(T_WRONG_FRINGE)
    wrong_carrier_gate_pass = (abs(R_q_wrong_disp) <= 0.5 * abs(R_q)) and (p_wrong_disp > 0.01)

    # ---- item 12: DeltaP at all four carriers, T_mean's own SE too
    # ΔP at T_delta's own carrier: refit the 5-column model with theta_c
    # built from (T_delta_x, its own phase) instead of (T_x, psi).
    amp_delta, psi_delta, _ = _amp_phase_at(theta, 0.5 * (series_a + series_b), T_delta_x, xbar)
    X5_delta = design_matrix(theta, T_delta_x, psi_delta, xbar)
    Rq_at_Tdelta = float((np.linalg.pinv(X5_delta) @ delta_ab)[4])

    def dP_from(Rq_val, amp_val, Tx_val, Tdeg_val):
        if amp_val == 0:
            return float("nan")
        df = Rq_val / (2 * math.pi * amp_val)
        fb = 1.0 / Tx_val
        return -(df / fb) * Tdeg_val

    dP_Tmean = delta_P_obs
    dP_Tdelta = dP_from(Rq_at_Tdelta, amp_delta, T_delta_x, T_delta)
    dP_wrong = dP_from(R_q_wrong_disp, amp, math.radians(T_WRONG_DISPLACED) * cos_c, T_WRONG_DISPLACED)
    dP_fringe = dP_from(R_q_fringe, amp, math.radians(T_WRONG_FRINGE) * cos_c, T_WRONG_FRINGE)

    # ---- item 7: bootstrap step-1 uncertainty into SE(R_q)
    rng_boot = np.random.default_rng(rng.integers(0, 2**63 - 1))
    n_boot = 500
    boot_idx = rng_boot.integers(0, n, size=(n_boot, n))
    Rq_boot = np.empty(n_boot)
    for bi in range(n_boot):
        idx = boot_idx[bi]
        th_b, a_b, b_b = theta[idx], series_a[idx], series_b[idx]
        try:
            car_b = carrier_fit(th_b, a_b, b_b, n_grid=400)  # coarser: bootstrap-only
            x_b = np.sin(np.radians(th_b))
            xbar_b = float(np.mean(x_b))
            Xb = design_matrix(th_b, car_b["T_x"], car_b["psi"], xbar_b)
            coefb = np.linalg.pinv(Xb) @ (b_b - a_b)
            Rq_boot[bi] = coefb[4]
        except Exception:
            Rq_boot[bi] = np.nan
    SE_Rq_bootstrap = float(np.nanstd(Rq_boot))
    SE_Rq_ols = float(np.sqrt(np.sum((delta_ab - X5 @ coef5) ** 2) / (n - 5) *
                               np.linalg.inv(X5.T @ X5)[4, 4]))

    # NOTE: `resolved` is NOT decided here -- it needs the Holm-adjusted p
    # across all pairs (item 14: 3 free pairs), computed once by the caller
    # after every pair's raw p is in hand. See score_all().

    return dict(
        pair=f"{key_a}-{key_b}", d_absorb=d_absorb,
        T_mean_deg=carrier["T_mean_deg"], T_x=T_x, amplitude=amp, psi=psi,
        carrier_r_squared=carrier["r_squared"],
        c0=c0, A_i=A_i, A_q=A_q, R_i=R_i, R_q=R_q,
        cond5=cond5, cond6=cond6, curvature_coef=float(coef6[5]),
        ill_conditioned=ill_conditioned,
        delta_f_obs=delta_f_obs, delta_P_obs=delta_P_obs,
        phase_channel=phase_channel, freq_channel=freq_channel,
        strain_channel=strain_channel, strain_flag=strain_flag,
        p_unrestricted=p_unrestricted, p_restricted=p_restricted,
        T_delta_deg=T_delta, carrier_stat_obs=carrier_stat_obs,
        carrier_gate_q95=q95, carrier_gate_pass=bool(carrier_gate_pass),
        linearization_gate_pass=bool(linearization_gate_pass),
        R_q_wrong_displaced=R_q_wrong_disp, p_wrong_displaced=p_wrong_disp,
        wrong_carrier_gate_pass=bool(wrong_carrier_gate_pass),
        R_q_fringe=R_q_fringe, p_fringe=p_fringe,
        deltaP_by_carrier=dict(T_mean=dP_Tmean, T_delta=dP_Tdelta,
                                T_wrong_displaced=dP_wrong, T_fringe=dP_fringe),
        SE_Rq_ols=SE_Rq_ols, SE_Rq_bootstrap=SE_Rq_bootstrap,
    )


# ===================================================== item 4: injection-recovery power test
def injection_recovery(data, key_a, key_b, m0, d_absorb, rng):
    theta = data["theta"]
    series_a, series_b = data[key_a], data[key_b]
    delta_ab = series_b - series_a
    carrier = carrier_fit(theta, series_a, series_b)
    T_x, psi, amp = carrier["T_x"], carrier["psi"], carrier["amplitude"]
    x = np.sin(np.radians(theta))
    xbar = float(np.mean(x))
    cos_c = math.cos(math.radians(CENTER_DEG))
    f_bar = 1.0 / T_x

    dP_pred = m0 * d_absorb
    dT_x = math.radians(dP_pred) * cos_c
    df_pred = -dT_x / (T_x ** 2)
    Rq_pred = 2 * math.pi * amp * df_pred

    X5 = design_matrix(theta, T_x, psi, xbar)
    X4 = X5[:, :4]
    pinv4 = np.linalg.pinv(X4)
    coef0 = pinv4 @ delta_ab
    yhat0 = X4 @ coef0
    resid0 = delta_ab - yhat0
    synthetic = yhat0 + resid0 + Rq_pred * X5[:, 4]

    pinv5 = np.linalg.pinv(X5)
    coef_syn = pinv5 @ synthetic
    Rq_syn = float(coef_syn[4])

    rng_inj = np.random.default_rng(rng.integers(0, 2**63 - 1))
    restr = restricted_null_surrogates(synthetic, X4, N_SURR, rng_inj)
    Rq_surr = (pinv5 @ restr)[4, :]
    p_syn = float((1 + np.sum(np.abs(Rq_surr) >= abs(Rq_syn))) / (len(Rq_surr) + 1))
    return dict(pair=f"{key_a}-{key_b}", Rq_pred=Rq_pred, Rq_recovered=Rq_syn, p_recovered=p_syn)


# ===================================================== saturating vs linear (item 9, disclosed)
def saturating_vs_linear(theta, data):
    configs = ["C40", "C60", "C70", "C80"]
    absorb_vals = np.array([40.0, 60.0, 70.0, 80.0])
    periods = []
    for key in configs:
        free = exp069_run._free_period_search(theta, data[key], center_deg=CENTER_DEG,
                                               n_grid=N_GRID_CARRIER)
        periods.append(free["p_star_deg"])
    periods = np.array(periods)

    # linear
    Xl = np.column_stack([np.ones(4), absorb_vals])
    coefl, *_ = np.linalg.lstsq(Xl, periods, rcond=None)
    yhat_l = Xl @ coefl
    r2_l = 1.0 - np.sum((periods - yhat_l) ** 2) / np.sum((periods - periods.mean()) ** 2)

    # saturating, L fixed
    Xs = np.column_stack([np.ones(4), -np.exp(-SAT_DECAY_L * absorb_vals)])
    coefs, *_ = np.linalg.lstsq(Xs, periods, rcond=None)
    yhat_s = Xs @ coefs
    r2_s = 1.0 - np.sum((periods - yhat_s) ** 2) / np.sum((periods - periods.mean()) ** 2)

    return dict(absorb=absorb_vals.tolist(), periods_n_grid3000=periods.tolist(),
                linear=dict(intercept=float(coefl[0]), slope=float(coefl[1]), r_squared=float(r2_l)),
                saturating=dict(P_inf=float(coefs[0]), amplitude=float(-coefs[1]),
                                 decay_L=SAT_DECAY_L, r_squared=float(r2_s)))


# ===================================================== full scoring + Combined Verdict
def score_all(data):
    rng = np.random.default_rng(SEED)

    per_pair = {}
    for key_a, key_b, d_absorb in PAIRS:
        per_pair[f"{key_a}-{key_b}"] = analyze_pair(data, key_a, key_b, d_absorb, rng)

    # item 14: Holm over the 3 algebraically-free adjacent pairs; C40-C80's p
    # reported unadjusted, explicitly labelled derived (G0-b proves it is the
    # arithmetic sum of the other three).
    p_restricted_free = {k: per_pair[k]["p_restricted"] for k in HOLM_PAIRS}
    p_unrestricted_free = {k: per_pair[k]["p_unrestricted"] for k in HOLM_PAIRS}
    holm_restricted = holm_adjust(p_restricted_free, m=3)
    holm_unrestricted = holm_adjust(p_unrestricted_free, m=3)
    for k in HOLM_PAIRS:
        per_pair[k]["p_restricted_holm"] = holm_restricted[k]
        per_pair[k]["p_unrestricted_holm"] = holm_unrestricted[k]
    per_pair["C40-C80"]["p_restricted_holm"] = per_pair["C40-C80"]["p_restricted"]
    per_pair["C40-C80"]["p_unrestricted_holm"] = per_pair["C40-C80"]["p_unrestricted"]
    per_pair["C40-C80"]["p_derived_unadjusted"] = True

    # RESOLVED (docket items 3, 6, 9(sign-clause n/a here), 10)
    for k, p in per_pair.items():
        p["resolved"] = bool(
            (not p["ill_conditioned"])
            and (p["p_restricted_holm"] <= 0.01)
            and p["linearization_gate_pass"]
            and p["carrier_gate_pass"]
            and p["wrong_carrier_gate_pass"]
        )

    # item 4: injection-recovery power test, the 3 adjacent pairs (m0-scaled
    # predicted effect at each pair's own d_absorb)
    injection = {}
    for key_a, key_b, d_absorb in PAIRS[:3]:
        injection[f"{key_a}-{key_b}"] = injection_recovery(
            data, key_a, key_b, data["m0_committed"], d_absorb, rng)
    power_demonstrated = all(
        injection[k]["p_recovered"] <= 0.01 for k in injection)

    # ---- P-072-2
    n_resolved_holm10_restricted = sum(
        1 for k in HOLM_PAIRS if per_pair[k]["p_restricted_holm"] <= 0.10
    ) + (1 if per_pair["C40-C80"]["p_restricted"] <= 0.10 else 0)
    n_resolved_holm10_unrestricted = sum(
        1 for k in HOLM_PAIRS if per_pair[k]["p_unrestricted_holm"] <= 0.10
    ) + (1 if per_pair["C40-C80"]["p_unrestricted"] <= 0.10 else 0)

    c4080 = per_pair["C40-C80"]["resolved"]
    c4060 = per_pair["C40-C60"]["resolved"]
    c6070 = per_pair["C60-C70"]["resolved"]
    c7080 = per_pair["C70-C80"]["resolved"]

    if c4080 and c4060 and (c6070 or c7080):
        p072_2 = "CONFIRM"
    elif n_resolved_holm10_restricted == 0 and n_resolved_holm10_unrestricted == 0:
        p072_2 = "REFUTE" if power_demonstrated else "UNDERPOWERED_NOT_EVALUABLE"
    else:
        p072_2 = "NEITHER"

    # ---- P-072-3 (item 8: relabeled basis-stability, NOT gating CONFIRMED)
    adj_resolved = [per_pair[k]["resolved"] for k in HOLM_PAIRS]
    if not all(adj_resolved):
        p072_3 = "NOT_EVALUABLE"
        rho_c = None
    else:
        S = sum(per_pair[k]["delta_P_obs"] for k in HOLM_PAIRS)
        D = per_pair["C40-C80"]["delta_P_obs"]
        rho_c = abs(S - D) / max(abs(D), 0.005)
        if rho_c <= 0.05:
            p072_3 = "CONFIRM_BASIS_STABLE"
        elif rho_c >= 1.00:
            p072_3 = "REFUTE_BASIS_UNSTABLE"
        else:
            p072_3 = "NEITHER"

    # ---- P-072-4 (item 9: rate-window demoted to disclosed; sign-reversal is
    # the only gating rate clause)
    resolved_pairs = [k for k in per_pair if per_pair[k]["resolved"]]
    sign_reversal = any(
        per_pair[k]["delta_P_obs"] < 0 and abs(per_pair[k]["delta_P_obs"]) >= 0.010
        for k in resolved_pairs
    )
    if sign_reversal:
        p072_4 = "REFUTE"
    elif len(resolved_pairs) >= 2 and all(per_pair[k]["delta_P_obs"] > 0 for k in resolved_pairs):
        p072_4 = "CONFIRM"
    else:
        p072_4 = "NEITHER"

    # ---- Combined Verdict
    g0_pass = (
        data["g0a"]["all_identical"]
        and data["g0b"]["max_abs_residual"] <= 1e-12
        and data["g0c"]["max_abs_delta"] <= 1e-12
    )
    if not g0_pass:
        combined = "HALT"
    elif p072_2 == "UNDERPOWERED_NOT_EVALUABLE":
        combined = "UNDERPOWERED_NOT_EVALUABLE"
    elif p072_2 == "REFUTE" or p072_4 == "REFUTE":
        combined = "REFUTED"
    elif p072_2 == "CONFIRM" and p072_4 == "CONFIRM":
        # Red Team Phase-2 audit Sec 4, condition 3: pre-registration
        # contaminated this cycle (two seats saw real numbers during Phase
        # 2) -- a CONFIRM-shaped result CANNOT be certified as blind and
        # MUST be emitted as CONFIRM_UNCERTIFIED, not CONFIRMED.
        combined = "CONFIRM_UNCERTIFIED"
    else:
        combined = "NEITHER"

    return dict(
        per_pair=per_pair, injection=injection, power_demonstrated=power_demonstrated,
        p072_2=p072_2, p072_3=p072_3, rho_c=rho_c, p072_4=p072_4,
        combined_verdict=combined,
        g0_pass=g0_pass,
        n_resolved_holm10_restricted=n_resolved_holm10_restricted,
        n_resolved_holm10_unrestricted=n_resolved_holm10_unrestricted,
    )


def main():
    t0 = __import__("time").time()
    data = load_data()
    scored = score_all(data)
    sat = saturating_vs_linear(data["theta"], data)

    results = dict(
        experiment="072-t28-differential-beat-fit",
        panel_iteration=49,
        lead_seat="PHOTONICS",
        t1_escape_route=None,
        m0_committed=data["m0_committed"],
        g0=dict(a=data["g0a"], b=data["g0b"], c=data["g0c"]),
        saturating_vs_linear=sat,
        scored=scored,
        elapsed_s=__import__("time").time() - t0,
    )

    out_path = os.path.join(HERE, "results.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2, default=float)
    print(f"Combined Verdict: {scored['combined_verdict']}")
    print(f"P-072-2: {scored['p072_2']}  P-072-3: {scored['p072_3']} (rho_c={scored['rho_c']})  "
          f"P-072-4: {scored['p072_4']}")
    for k, p in scored["per_pair"].items():
        print(f"  {k}: resolved={p['resolved']}  p_restr_holm={p.get('p_restricted_holm'):.4f}  "
              f"dP(Tmean)={p['delta_P_obs']:+.4f}deg  cond={p['cond5']:.1f}")
    print(f"elapsed: {results['elapsed_s']:.1f}s")


if __name__ == "__main__":
    main()
