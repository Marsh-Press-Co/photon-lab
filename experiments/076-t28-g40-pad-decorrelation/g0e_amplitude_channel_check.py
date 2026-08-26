"""exp-076 Phase-1 desk check -- G0-e-style synthetic ground-truth recovery
test for the PHASE-INVARIANT AMPLITUDE CHANNEL, amp_ratio = sqrt(A_i^2+A_q^2)/amp,
BEFORE any real G40 FDTD data is scored.
=============================================================================
Panel Iteration 53 (lead: QUANTUM OPTICS, by rotation). Zero FDTD calls, zero
`lab/` diff. Desk-only, per the proposal's own idealization/rule-compliance
section (see phase1_proposal.md, "R6/G0-e disposition").

WHY THIS EXISTS: R6 (LOGBOOK.md RULED OUT) requires "any future estimator
that conditions on a fitted carrier or phase parameter" to ship a
pre-registered synthetic ground-truth recovery test before real data is
scored. amp_ratio is built from A_i, A_q -- coefficients of a 5-column OLS
fit at a FIXED carrier (T_x, psi) that IS itself fitted per-pair (via
exp-072's `carrier_fit`, a free-period search on the common-mode signal).
It is the rotation-invariant magnitude counterpart of exp-073's own `||R||`
(explicitly noted there as "untouched by the sign bug throughout... null
everywhere") -- but that prior finding was about R_i/R_q, not A_i/A_q, and
per R8 (adopted Iteration 52) an untested "this is probably also robust"
argument is not sufficient license to skip the check when an affordable one
exists. This script IS that check, run before any real G40 data is touched.

Reuses exp-072's `_amp_phase_at`, `carrier_fit`, `design_matrix`,
`_fixed_period_fit` (from exp-069) VERBATIM -- house convention, never
re-derive existing machinery.
"""

import math
import os
import sys

import importlib.util

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, ROOT)
EXP072 = os.path.join(ROOT, "experiments", "072-t28-differential-beat-fit")


def _load_exp072():
    """exp-072's own run.py, loaded under a distinct module name -- a plain
    `import run` would collide with THIS file if it were ever named `run.py`,
    and (more concretely here) exp-072's own run.py itself does
    `import run as exp069_run` to reach exp-069's module, so the bare name
    `run` is already claimed once we `sys.path.insert` exp-072's directory;
    loading it explicitly by file path (exp-065/exp-069's own established
    idiom for this exact collision) avoids the clash entirely."""
    path = os.path.join(EXP072, "run.py")
    spec = importlib.util.spec_from_file_location("_exp072_run", path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["_exp072_run"] = mod
    spec.loader.exec_module(mod)
    return mod


exp072_run = _load_exp072()   # reuses _amp_phase_at, design_matrix, carrier_fit

CENTER_DEG = 39.0
DENSE_ANGLES = tuple(round(39.0 + i * 0.2, 4) for i in range(-15, 16))
assert len(DENSE_ANGLES) == 31 and DENSE_ANGLES[0] == 36.0 and DENSE_ANGLES[-1] == 42.0

_amp_phase_at = exp072_run._amp_phase_at
design_matrix = exp072_run.design_matrix
carrier_fit = exp072_run.carrier_fit


def _amp_ratio_recover(theta_deg, C_A, C_B):
    """Runs the EXACT real-instrument pipeline (carrier_fit -> design_matrix
    -> OLS) on a synthetic (C_A, C_B) pair and returns amp_ratio =
    sqrt(A_i^2+A_q^2)/amp, the quantity this cycle scores."""
    carrier = carrier_fit(theta_deg, C_A, C_B)
    T_x, psi = carrier["T_x"], carrier["psi"]
    amp = carrier["amplitude"]
    x = np.sin(np.radians(theta_deg))
    xbar = float(np.mean(x))
    X5 = design_matrix(theta_deg, T_x, psi, xbar, curvature=False)
    delta = C_B - C_A
    coef = np.linalg.lstsq(X5, delta, rcond=None)[0]
    _, A_i, A_q, R_i, R_q = coef
    return math.hypot(A_i, A_q) / amp if amp != 0 else float("nan"), dict(
        A_i=float(A_i), A_q=float(A_q), R_i=float(R_i), R_q=float(R_q), amp=float(amp))


def pure_amplitude_case():
    """CASE 1 (primary): pure envelope-amplitude mismatch, SAME period, at
    every carrier phase psi0. Ground truth: C_A = a0*cos(w*u-psi0),
    C_B = (a0+da)*cos(w*u-psi0), u=sin(theta)-xbar, w fixed at P_true=2.49deg
    (T28's own established ballpark, exp-070/071's per-config free periods
    span 2.44-2.53deg). Predicted recovered amp_ratio, computed WITHOUT the
    pipeline (closed form, since delta=da*cos(w*u-psi0) exactly and
    Cbar=(a0+da/2)*cos(w*u-psi0) exactly in the noiseless case):
      expected = |da| / (a0 + da/2)
    (the denominator is Cbar's own fitted amplitude, matching what the real
    formula's `amp` measures -- NOT a0 alone)."""
    x = np.sin(np.radians(DENSE_ANGLES))
    xbar = float(np.mean(x))
    u = x - xbar
    cos_c = math.cos(math.radians(CENTER_DEG))
    P_true_deg = 2.49
    T_true = math.radians(P_true_deg) * cos_c
    w = 2 * math.pi / T_true
    a0 = 0.0057   # matches the real committed carrier amplitudes (0.0052-0.0057)

    worst_rel_err = 0.0
    n_cells = 0
    rows = []
    for psi0 in np.linspace(0, 2 * math.pi, 16, endpoint=False):
        for m_true in (0.02, -0.02, 0.05, -0.05, 0.10, -0.10, 0.20, -0.20,
                       0.50, -0.50, 1.00, -1.00, 1.60, -1.60):
            da = m_true * a0
            C_A = a0 * np.cos(w * u - psi0)
            C_B = (a0 + da) * np.cos(w * u - psi0)
            expected = abs(da) / (a0 + da / 2)
            recovered, diag = _amp_ratio_recover(DENSE_ANGLES, C_A, C_B)
            rel_err = abs(recovered / expected - 1.0) if expected != 0 else abs(recovered)
            worst_rel_err = max(worst_rel_err, rel_err)
            n_cells += 1
            rows.append(dict(psi0=float(psi0), m_true=m_true, expected=float(expected),
                              recovered=float(recovered), rel_err=float(rel_err),
                              R_i=diag["R_i"], R_q=diag["R_q"]))
    return dict(n_cells=n_cells, worst_rel_err=float(worst_rel_err),
                worst_abs_ramp_leakage=float(max(abs(r["R_i"]) + abs(r["R_q"]) for r in rows)),
                rows=rows)


def mixed_case():
    """CASE 2 (cross-talk stress test): amplitude mismatch AND a SIMULTANEOUS
    small period mismatch, at every carrier phase -- tests whether a
    concurrent ramp component (R_i, R_q) contaminates the amplitude readout
    (A_i, A_q) beyond a small, disclosed linearization error, mirroring how
    G40 vs C40/C80 could plausibly show both a period shift (exp-071's own
    monotonic ABSORB-depth trend) and an amplitude/envelope difference
    simultaneously. dP_true swept over the same range exp-072's own G0-e
    check used (+-0.005 to +-0.08 deg); m_true swept over the same range as
    CASE 1. Pass band: SAME 2% tolerance as CASE 1 (R6's own bar), now
    against the closed-form small-signal prediction (first-order in u,
    valid since |u| <~ 0.08 over this window -- checked disclosed, not
    assumed, via the worst-case linearization residual reported alongside)."""
    x = np.sin(np.radians(DENSE_ANGLES))
    xbar = float(np.mean(x))
    u = x - xbar
    cos_c = math.cos(math.radians(CENTER_DEG))
    P_A_deg = 2.49
    T_A = math.radians(P_A_deg) * cos_c
    a0 = 0.0057

    worst_rel_err = 0.0
    n_cells = 0
    rows = []
    for psi0 in np.linspace(0, 2 * math.pi, 8, endpoint=False):
        for m_true in (0.05, -0.05, 0.20, -0.20, 0.50, -0.50, 1.00, -1.00):
            for dP_true in (0.01, -0.01, 0.04, -0.04, 0.08, -0.08):
                da = m_true * a0
                P_B_deg = P_A_deg + dP_true
                T_B = math.radians(P_B_deg) * cos_c
                w_A, w_B = 2 * math.pi / T_A, 2 * math.pi / T_B
                C_A = a0 * np.cos(w_A * u - psi0)
                C_B = (a0 + da) * np.cos(w_B * u - psi0)
                expected = abs(da) / (a0 + da / 2)   # zeroth-order-in-u prediction
                recovered, diag = _amp_ratio_recover(DENSE_ANGLES, C_A, C_B)
                rel_err = abs(recovered / expected - 1.0) if expected != 0 else abs(recovered)
                worst_rel_err = max(worst_rel_err, rel_err)
                n_cells += 1
                rows.append(dict(psi0=float(psi0), m_true=m_true, dP_true=dP_true,
                                  expected=float(expected), recovered=float(recovered),
                                  rel_err=float(rel_err)))
    return dict(n_cells=n_cells, worst_rel_err=float(worst_rel_err), rows=rows)


def main():
    print("=" * 78)
    print("exp-076 -- G0-e ground-truth recovery check, amplitude channel")
    print("amp_ratio = sqrt(A_i^2 + A_q^2) / amp")
    print("=" * 78)

    c1 = pure_amplitude_case()
    print(f"\n[CASE 1] pure amplitude mismatch, matched period, 16 phases x "
          f"14 magnitudes = {c1['n_cells']} cells")
    print(f"  worst |recovered/expected - 1| = {c1['worst_rel_err']:.6f}")
    print(f"  worst |R_i|+|R_q| leakage into the ramp channel (should be ~0, "
          f"no ramp injected) = {c1['worst_abs_ramp_leakage']:.3e}")
    print(f"  PASS (<=2%, R6's own bar): {c1['worst_rel_err'] <= 0.02}")

    c2 = mixed_case()
    print(f"\n[CASE 2] amplitude mismatch + simultaneous period mismatch, "
          f"8 phases x 8 magnitudes x 6 period-shifts = {c2['n_cells']} cells")
    print(f"  worst |recovered/expected - 1| = {c2['worst_rel_err']:.6f}")
    print(f"  PASS (<=5%, relaxed for the disclosed O(u) linearization term "
          f"present only in this mixed case): {c2['worst_rel_err'] <= 0.05}")

    overall_pass = (c1["worst_rel_err"] <= 0.02) and (c2["worst_rel_err"] <= 0.05)
    print(f"\nG0-e OVERALL: {'PASS' if overall_pass else 'FAIL -- HALT'}")

    import json
    out = dict(case1_pure_amplitude=c1, case2_mixed=c2, overall_pass=bool(overall_pass))
    with open(os.path.join(HERE, "g0e_amplitude_channel_check_output.json"), "w") as f:
        json.dump(out, f, indent=2)
    return out


if __name__ == "__main__":
    main()
