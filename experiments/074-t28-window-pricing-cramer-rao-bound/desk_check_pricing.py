"""exp-074 -- "Price the window": Cramer-Rao/conditioning pricing (EM) +
L(T) leakage budget (QUANTUM), turned into real, committed, reproducible
code, per Iteration-51 queue item 1 (near-unanimous #1 across all six of
exp-073's Phase-5 seats). Desk-first check, committed BEFORE phase1_proposal.md's
own numbers are cited in prose -- exp-069's own "desk_check_settling_delta.py"
convention, reused here for the identical reason: no falsifier or
"precisely recomputed" figure may be hand-typed (LOGBOOK R4).

Zero FDTD calls. Zero `lab/` diff. Reads ONLY already-committed results.json
from exp-069/071. Reuses `_fixed_period_fit`/`_free_period_search` from
exp-069's run.py and the exact `_amp_phase_at`/`carrier_fit`/`design_matrix`
basis from exp-072/073's run.py (re-implemented here verbatim, not imported,
solely because exp-073's own module is also named `run` and collides on
`sys.path` with exp-069's `run` -- the formulas are byte-for-byte identical
to exp-073's committed `run.py`; see the docstring on each function for the
line-level correspondence, and CHECK 0 below re-derives the byte-identity
claim against exp-072's own published results.json rather than asserting it).

This script answers, at zero cost: does theta in [36,42] deg support a
carrier-conditioned two-tone discriminator against T21's established
1.9608deg fringe at achievable SNR, under ANY correctly-calibrated null --
and how would that answer change at a widened window. It does NOT run a
null-calibration test itself (G0-e(ii) is a downstream, data-scored gate);
it prices the DESIGN's own information content, which is a precondition
for any null being calibratable to a useful power in the first place.
"""

import json
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
EXP069 = os.path.join(ROOT, "experiments", "069-t21-block-mini-period-match-power-up")
EXP071 = os.path.join(ROOT, "experiments", "071-t28-absorb-depth-causal-test")
EXP072 = os.path.join(ROOT, "experiments", "072-t28-differential-beat-fit")
sys.path.insert(0, EXP069)

import run as exp069_run  # noqa: E402  (reuse verbatim, house convention)

_fixed_period_fit = exp069_run._fixed_period_fit
_free_period_search = exp069_run._free_period_search

CENTER_DEG = 39.0
N_GRID_CARRIER = 3000
T_FRINGE_DEG = 1.9608          # deg, T21's established fringe, x=sin(theta) period
PAIRS = [("C40", "C60"), ("C60", "C70"), ("C70", "C80"), ("C40", "C80")]
WIDENED_CANDIDATES = [
    (42.0, "baseline (current window)"),
    (45.5, "~1.00 Rayleigh widths (EM's own exp-072 Sec.6 Direction 3, 'formally resolvable')"),
    (46.0, "grid-rounded widened candidate (0.2deg step lands here)"),
    (51.0, "~1.50 Rayleigh widths (EM's own exp-072 Sec.6 Direction 3, third option)"),
]
N_PSI_SWEEP = 8                # nuisance-phase robustness grid, [0,180)deg


# ===================================================== CHECK 0: byte-identity of the re-implemented basis
def check0_basis_identity():
    """Verify this file's design_matrix/carrier_fit reproduce exp-072's own
    committed per-pair (T_mean_deg, T_x, psi, amplitude, cond5) to machine
    precision on the identical data -- so every number below is priced
    against the SAME basis the rest of the T28 record uses, not a
    plausible-looking reconstruction. (exp-072's own psi/A_q/R_q sign
    convention was later corrected in exp-073; T_mean_deg/T_x/amplitude/
    cond5 are sign-convention-invariant and are what this check compares.)"""
    with open(os.path.join(EXP072, "results.json")) as f:
        d072 = json.load(f)
    data = load_data()
    theta = data["theta"]
    worst = 0.0
    rows = []
    for a, b in PAIRS:
        key = f"{a}-{b}"
        ref = d072["scored"]["per_pair"][key]
        carrier = carrier_fit(theta, data[a], data[b])
        for field, refval in [("T_mean_deg", ref["T_mean_deg"]), ("T_x", ref["T_x"]),
                               ("amplitude", ref["amplitude"])]:
            rel = abs(carrier[field.replace("T_mean_deg", "T_mean_deg")] - refval) / max(abs(refval), 1e-15) \
                if field != "T_mean_deg" else abs(carrier["T_mean_deg"] - refval) / abs(refval)
            worst = max(worst, rel)
        X5 = design_matrix(theta, carrier["T_x"], carrier["psi"], float(np.mean(np.sin(np.radians(theta)))))
        cond5 = float(np.linalg.cond(X5))
        rel_cond = abs(cond5 - ref["cond5"]) / ref["cond5"]
        worst = max(worst, rel_cond)
        rows.append(dict(pair=key, T_mean_deg=carrier["T_mean_deg"], ref_T_mean_deg=ref["T_mean_deg"],
                          cond5=cond5, ref_cond5=ref["cond5"]))
    return dict(pass_=bool(worst <= 1e-9), worst_rel_err=worst, rows=rows)


# ===================================================== step 1: carrier fit (verbatim formulas, exp-072/073 run.py)
def _amp_phase_at(theta_deg, series, T_x, xbar):
    x = np.sin(np.radians(theta_deg))
    u = x - xbar
    fit = _fixed_period_fit(u, series, T_x)
    amp = math.hypot(fit["a"], fit["b"])
    psi = -math.atan2(fit["b"], fit["a"])
    return amp, psi, fit["c0"]


def carrier_fit(theta_deg, series_a, series_b, n_grid=N_GRID_CARRIER):
    cbar = 0.5 * (series_a + series_b)
    free = _free_period_search(theta_deg, cbar, center_deg=CENTER_DEG, n_grid=n_grid)
    T_mean_deg = free["p_star_deg"]
    cos_c = math.cos(math.radians(CENTER_DEG))
    T_x = math.radians(T_mean_deg) * cos_c
    xbar = float(np.mean(np.sin(np.radians(theta_deg))))
    amp, psi, _ = _amp_phase_at(theta_deg, cbar, T_x, xbar)
    return dict(T_mean_deg=T_mean_deg, T_x=T_x, amplitude=amp, psi=psi, r_squared=free["r_squared"])


def design_matrix(theta_deg, T_x, psi, xbar):
    """The frozen 5-column basis: [1, cos(theta_c), -sin(theta_c),
    u*cos(theta_c), -u*sin(theta_c)]. R_q is column index 4."""
    x = np.sin(np.radians(theta_deg))
    u = x - xbar
    w = 2 * math.pi / T_x
    theta_c = w * u + psi
    return np.column_stack([np.ones_like(x), np.cos(theta_c), -np.sin(theta_c),
                             u * np.cos(theta_c), -u * np.sin(theta_c)])


def tone_cols(theta_deg, T_x, psi, xbar):
    """The 4 ramped-quadrature columns [cos,-sin,u*cos,-u*sin] for one
    additional tone at (T_x, psi) -- used to build the 9-column two-tone
    design X9 = [X5 | tone_cols(second tone)]."""
    x = np.sin(np.radians(theta_deg))
    u = x - xbar
    w = 2 * math.pi / T_x
    theta_c = w * u + psi
    return np.column_stack([np.cos(theta_c), -np.sin(theta_c), u * np.cos(theta_c), -u * np.sin(theta_c)])


def load_data():
    with open(os.path.join(EXP069, "results.json")) as f:
        d069 = json.load(f)
    with open(os.path.join(EXP071, "results.json")) as f:
        d071 = json.load(f)
    rows069 = {r["theta"]: r for r in d069["block_dense"]["rows"]}
    theta069 = sorted(rows069)
    c40 = np.array([rows069[t]["C_empty_C40"] for t in theta069])
    c80 = np.array([rows069[t]["C_empty_C80"] for t in theta069])
    theta_c60 = [r["theta"] for r in d071["dense_causal"]["rows"]["C60"]]
    theta_c70 = [r["theta"] for r in d071["dense_causal"]["rows"]["C70"]]
    c60 = np.array([r["C_empty"] for r in d071["dense_causal"]["rows"]["C60"]])
    c70 = np.array([r["C_empty"] for r in d071["dense_causal"]["rows"]["C70"]])
    theta = np.array(theta069, dtype=float)
    g0a = bool(np.array_equal(theta, np.array(theta_c60)) and np.array_equal(theta, np.array(theta_c70)))
    return dict(theta=theta, C40=c40, C60=c60, C70=c70, C80=c80, g0a_grid_identical=g0a)


def L_of_T(pinv5_row4, theta_deg, xbar, T_deg):
    """The QUANTUM leakage function |L(T)|: the coefficient with which a
    unit-amplitude sinusoid of period T (in u=sin(theta)-xbar) projects
    into R_q through the FIXED 5-column basis, maximised over relative
    phase -- a design-time fact, no data. L(T) = |A + iB| where A,B are
    the row's dot products with cos(w_T u), sin(w_T u) (the max-over-phase
    of A*cos(phi)-B*sin(phi) is exactly hypot(A,B))."""
    x = np.sin(np.radians(theta_deg))
    u = x - xbar
    cos_c = math.cos(math.radians(CENTER_DEG))
    w = 2 * math.pi / (math.radians(T_deg) * cos_c)
    A = np.dot(pinv5_row4, np.cos(w * u))
    B = np.dot(pinv5_row4, np.sin(w * u))
    return math.hypot(A, B)


def hat_and_residual_maker(X):
    pinv = np.linalg.pinv(X)
    H = X @ pinv
    return pinv, H


# ===================================================== per-pair pricing at the REAL fitted carriers (item a, b)
def price_pair(theta, data, a, b, T_fringe_deg=T_FRINGE_DEG):
    series_a, series_b = data[a], data[b]
    delta_ab = series_b - series_a
    xbar = float(np.mean(np.sin(np.radians(theta))))
    cos_c = math.cos(math.radians(CENTER_DEG))
    n = len(theta)

    carrier = carrier_fit(theta, series_a, series_b)
    T_x, psi, amp, T_mean = carrier["T_x"], carrier["psi"], carrier["amplitude"], carrier["T_mean_deg"]

    X5 = design_matrix(theta, T_x, psi, xbar)
    pinv5, H5 = hat_and_residual_maker(X5)
    coef5 = pinv5 @ delta_ab
    R_q = float(coef5[4])
    p = X5.shape[1]
    resid5 = delta_ab - X5 @ coef5
    gram5_inv = np.linalg.inv(X5.T @ X5)
    SE_Rq_ols = math.sqrt(np.sum(resid5 ** 2) / (n - p) * gram5_inv[4, 4])
    z_ols = abs(R_q) / SE_Rq_ols if SE_Rq_ols > 0 else float("nan")
    cond5 = float(np.linalg.cond(X5))

    # -- leverage (item c): house convention is M5 = I - H5 (the
    # residual-maker used by exp-073's own sign-flip null, resid5 = M5@y),
    # so diag(M5) = 1 - h_ii and mean(diag(M5)) = (n-p)/n exactly (a trace
    # identity: trace(H5)=p always for full-rank X5). h_ii itself (the
    # ordinary hat-matrix leverage) is where "leverage concentrates".
    h_ii = np.diag(H5)
    diagM5 = 1.0 - h_ii
    mean_diagM5 = float(diagM5.mean())
    edge_idx = list(range(4)) + list(range(n - 4, n))
    edge_h = float(h_ii[edge_idx].mean())
    center_h = float(np.delete(h_ii, edge_idx).mean())
    row5 = pinv5[4, :]
    # the exact quantity driving exp-073's own G0-e(ii) anti-conservative
    # finding: E[Var(Rq_sign_flip_surrogate)]/Var(Rq_obs) under equal-
    # variance H0 noise = sum(row5_i^2 * diagM5_i) / sum(row5_i^2).
    lev_ratio = float(np.sum(row5 ** 2 * diagM5) / np.sum(row5 ** 2))

    # -- two-tone conditioning/VIF (item a): the second tone's OWN phase is
    # fit from the real common-mode Cbar at T_fringe, exactly paralleling
    # how the primary carrier's own psi was fit (never hand-set) --
    # matches exp-072/073's own at_carrier() idiom for the fringe-
    # disclosure leg.
    Cbar = 0.5 * (series_a + series_b)
    T_fx = math.radians(T_fringe_deg) * cos_c
    amp_fr, psi_fr, _ = _amp_phase_at(theta, Cbar, T_fx, xbar)
    X9 = np.column_stack([X5, tone_cols(theta, T_fx, psi_fr, xbar)])
    cond9 = float(np.linalg.cond(X9))
    gram9_inv = np.linalg.inv(X9.T @ X9)
    VIF_Rq = float(gram9_inv[4, 4] / gram5_inv[4, 4])
    SE_inflation = math.sqrt(VIF_Rq)
    z_joint_optimistic = z_ols / SE_inflation  # optimistic: assumes noise/effect unchanged

    # -- L(T) leakage (item b)
    T_grid = np.linspace(1.2, 5.5, 861)
    L_vals = np.array([L_of_T(row5, theta, xbar, t) for t in T_grid])
    Lpeak = float(L_vals.max())
    Lpeak_T = float(T_grid[np.argmax(L_vals)])
    L_fringe = L_of_T(row5, theta, xbar, T_fringe_deg)

    return dict(
        pair=f"{a}-{b}", T_mean_deg=T_mean, T_x=T_x, psi=psi, amplitude=amp,
        cond5=cond5, R_q=R_q, SE_Rq_ols=SE_Rq_ols, z_ols=z_ols,
        cond9_fringe=cond9, VIF_Rq_fringe=VIF_Rq, SE_inflation_fringe=SE_inflation,
        z_joint_optimistic=z_joint_optimistic,
        mean_diagM5=mean_diagM5, edge_h_ii=edge_h, center_h_ii=center_h,
        edge_center_ratio=edge_h / center_h if center_h > 0 else float("nan"),
        lev_weighted_ratio=lev_ratio,
        L_fringe=float(L_fringe), Lpeak=Lpeak, Lpeak_T_deg=Lpeak_T,
    )


# ===================================================== widened-window design-only pricing (item c), phase-swept for robustness
def price_window_design_only(theta_wide, T_x_fixed, T_fringe_deg=T_FRINGE_DEG, n_psi=N_PSI_SWEEP):
    """Design-only (no y needed beyond the theta grid): cond(X5), the
    leverage pattern, cond(X9)/VIF, and L(T), at a widened window, holding
    the TRUE carrier's own T_x fixed (the physical periodicity in x=sin
    theta does not change with window choice) and sweeping BOTH the
    carrier's nuisance phase psi and the second tone's nuisance phase psi2
    over [0,180)deg -- neither is knowable a priori for a window with no
    real data yet, so every reported quantity is a (min,median,max) over
    that sweep, never a single cherry-picked phase."""
    xbar = float(np.mean(np.sin(np.radians(theta_wide))))
    cos_c = math.cos(math.radians(CENTER_DEG))
    n = len(theta_wide)
    T_fx = math.radians(T_fringe_deg) * cos_c
    psis = np.radians(np.linspace(0, 180, n_psi, endpoint=False))

    cond5 = None
    mean_diagM5 = None
    edge_h = center_h = None
    VIFs, levs, Lpeaks = [], [], []
    for psi_p in psis:
        X5 = design_matrix(theta_wide, T_x_fixed, psi_p, xbar)
        pinv5, H5 = hat_and_residual_maker(X5)
        if cond5 is None:
            cond5 = float(np.linalg.cond(X5))  # psi-invariant (verified below), computed once
            h_ii = np.diag(H5)
            diagM5 = 1.0 - h_ii
            mean_diagM5 = float(diagM5.mean())
            edge_idx = list(range(4)) + list(range(n - 4, n))
            edge_h = float(h_ii[edge_idx].mean())
            center_h = float(np.delete(h_ii, edge_idx).mean())
        else:
            cond5_check = float(np.linalg.cond(X5))
            assert abs(cond5_check - cond5) / cond5 < 1e-9, "cond(X5) unexpectedly psi-dependent"
        row5 = pinv5[4, :]
        diagM5_p = 1.0 - np.diag(H5)
        levs.append(float(np.sum(row5 ** 2 * diagM5_p) / np.sum(row5 ** 2)))
        gram5_inv44 = np.linalg.inv(X5.T @ X5)[4, 4]
        T_grid = np.linspace(1.2, 5.5, 300)
        Lpeaks.append(float(max(L_of_T(row5, theta_wide, xbar, t) for t in T_grid)))
        for psi2 in psis:
            X9 = np.column_stack([X5, tone_cols(theta_wide, T_fx, psi2, xbar)])
            gram9_inv44 = np.linalg.inv(X9.T @ X9)[4, 4]
            VIFs.append(float(gram9_inv44 / gram5_inv44))

    VIFs = np.array(VIFs)
    levs = np.array(levs)
    Lpeaks = np.array(Lpeaks)
    return dict(
        n=n, cond5=cond5, mean_diagM5=mean_diagM5, edge_h_ii=edge_h, center_h_ii=center_h,
        edge_center_ratio=edge_h / center_h if center_h else float("nan"),
        VIF_min=float(VIFs.min()), VIF_median=float(np.median(VIFs)), VIF_max=float(VIFs.max()),
        SE_inflation_min=float(math.sqrt(VIFs.min())), SE_inflation_median=float(math.sqrt(np.median(VIFs))),
        SE_inflation_max=float(math.sqrt(VIFs.max())),
        lev_ratio_min=float(levs.min()), lev_ratio_median=float(np.median(levs)), lev_ratio_max=float(levs.max()),
        Lpeak_min=float(Lpeaks.min()), Lpeak_median=float(np.median(Lpeaks)), Lpeak_max=float(Lpeaks.max()),
    )


def rayleigh_widths(theta_wide, f_bar, f_fringe):
    X = float(np.ptp(np.sin(np.radians(theta_wide))))
    rayleigh = 1.0 / X
    return dict(X=X, rayleigh=rayleigh, sep_over_rayleigh=abs(f_fringe - f_bar) / rayleigh)


def main():
    t0 = __import__("time").time()
    check0 = check0_basis_identity()

    data = load_data()
    theta = data["theta"]

    per_pair = {}
    for a, b in PAIRS:
        per_pair[f"{a}-{b}"] = price_pair(theta, data, a, b)

    # C40-C80's own carrier is used as "the true carrier" for widened-window
    # design-only pricing -- it is the derived/summary pair (G0-b: exact sum
    # of the other three) and its T_x is representative of all four
    # (2.4861-2.5325deg, 1.9% spread, see per_pair above).
    T_x_true = per_pair["C40-C80"]["T_x"]
    f_bar = 1.0 / T_x_true * (2 * math.pi) / (2 * math.pi)  # keep in same units as elsewhere (cycles per x-unit)
    f_bar_cycles = 1.0 / T_x_true

    cos_c = math.cos(math.radians(CENTER_DEG))
    f_fringe_cycles = 1.0 / (math.radians(T_FRINGE_DEG) * cos_c)

    widened = {}
    for tmax, label in WIDENED_CANDIDATES:
        n = int(round((tmax - 36.0) / 0.2)) + 1
        theta_w = np.linspace(36.0, 36.0 + 0.2 * (n - 1), n)
        design = price_window_design_only(theta_w, T_x_true)
        design["rayleigh"] = rayleigh_widths(theta_w, f_bar_cycles, f_fringe_cycles)
        design["theta_max_deg"] = tmax
        design["label"] = label
        widened[f"theta_max_{tmax}"] = design

    results = dict(
        experiment="074-t28-window-pricing-cramer-rao-bound",
        panel_iteration=51,
        lead_seat="ELECTROMAGNETISM",
        phase="1-PROPOSE (desk-check pre-registration verification, not a scored Phase-4 run)",
        t1_escape_route="none -- pure instrument/statistics characterization, no medium",
        check0_basis_identity=check0,
        per_pair=per_pair,
        f_bar_cycles=f_bar_cycles, f_fringe_cycles=f_fringe_cycles,
        widened_windows=widened,
        elapsed_s=__import__("time").time() - t0,
    )

    out_path = os.path.join(HERE, "desk_check_pricing_results.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2, default=float)

    print(f"CHECK 0 (basis identity vs exp-072's committed results.json): "
          f"pass={check0['pass_']} worst_rel_err={check0['worst_rel_err']:.2e}")
    print("\nPer-pair pricing at REAL fitted carriers (baseline window, 36-42deg, n=31):")
    for k, v in per_pair.items():
        print(f"  {k}: cond5={v['cond5']:.1f}  |Rq|/SE_ols={v['z_ols']:.2f}  "
              f"cond9(fringe)={v['cond9_fringe']:.1f}  VIF_Rq={v['VIF_Rq_fringe']:.1f}  "
              f"SEinfl={v['SE_inflation_fringe']:.2f}  z_joint(optimistic)={v['z_joint_optimistic']:.2f}  "
              f"lev_ratio={v['lev_weighted_ratio']:.4f}  L(fringe)={v['L_fringe']:.1f}  "
              f"Lpeak={v['Lpeak']:.1f}@{v['Lpeak_T_deg']:.2f}deg")
    print("\nWidened-window design-only pricing (phase-swept, min/median/max over psi,psi2):")
    for k, v in widened.items():
        print(f"  {v['label']} (n={v['n']}, sep={v['rayleigh']['sep_over_rayleigh']:.3f} widths): "
              f"cond5={v['cond5']:.1f}  mean_diagM5={v['mean_diagM5']:.4f}  "
              f"edge/center_h_ii={v['edge_h_ii']:.4f}/{v['center_h_ii']:.4f} (ratio {v['edge_center_ratio']:.2f})  "
              f"VIF=[{v['VIF_min']:.1f},{v['VIF_median']:.1f},{v['VIF_max']:.1f}]  "
              f"lev_ratio=[{v['lev_ratio_min']:.3f},{v['lev_ratio_median']:.3f},{v['lev_ratio_max']:.3f}]")
    print(f"\nelapsed: {results['elapsed_s']:.2f}s")


if __name__ == "__main__":
    main()
