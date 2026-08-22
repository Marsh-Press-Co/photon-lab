"""exp-059 -- Panel Iteration 36 (LOCKED, unconditional, breaking rotation):
the closed-form Q_ext(x) cylinder/disk check.
=============================================================================
Lead: PHOTONICS. Red Team's Iteration-34 Phase-5 audit granted this item
unconditional-lock status after three clean deferrals (Iterations 32/33/34)
-- the lowest deferral count that has ever triggered a lock in this
program's history. Zero new FDTD calls -- pure closed-form/special-function
evaluation (`lab/qext_theory.py`), reusing already-committed bench data
(`experiments/002-cross-sections`, `experiments/043-docket7-thermo-sidecar`)
for every empirical comparator.

Phase-3 synthesis incorporates Red Team's Iteration-36 Phase-2 mandatory-fix
docket (6 items: MF-1..MF-6, all accepted -- MF-5 accepted in part, its
FDTD-requiring half explicitly overridden as out of this LOCKED item's own
zero-new-FDTD scope). See NOTES.md for the full record.
"""

import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "..")))

from lab import qext_theory as qt
from lab import thermo_sidecar as ts

# --------------------------------------------------------- cited constants
# exp-020/043's own established bench geometry -- reused, not re-derived.
R_OUT_CELLS = 78
DX_M = 30.0e-9
LAMBDA_M = 600.0e-9
SIGMA_EXT_CELLS = 240.0073740162445  # exp-043/results.json::graded_black_shell_flagship

# MF-4 (THERMODYNAMICS): recompute graded_black_shell_flagship's own
# thermal margin (exp-057's own corrected chain) under BOTH bounding
# extremes this item motivates -- the conservative Q_ext=1 floor (area =
# r_out^2, i.e. treating sigma_ext as if it equaled the geometric radius)
# and the new PEC ceiling (area = (Q_ext_PEC * 2*r_out)^2, i.e. treating
# the object as if it scattered/extincted as strongly as a sharp PEC edge)
# -- to confirm, not merely assert, that NO scored margin changes.
P_ABS_W_FLAGSHIP_CENTRAL = 1.7409069740390205e-12   # exp-043/results.json, unmodified
K_AIR = 0.026
DENSITY_SI_KG_M3, C_P_SI_J_KGK = 2330.0, 700.0
EMISSIVITY = 0.9
T_AMBIENT_K = 293.15
NETD_BAND_K = (0.020, 0.050)

NETD_DISCLAIMER = (
    "NETD is an instrument/detector threshold, not a human perceptual one. "
    "This item's margin recompute (below) does NOT bear on constraint-3/4's "
    "human-eye verdict -- included only to verify MF-4's claim that no "
    "scored margin changes, not as a new thermal finding.")

DIFFRACTION_CAVEAT = (
    "Q_ext_PEC is a REFERENCE/BOUNDING comparison only (MF-3), NOT a "
    "literal model of the graded_black_shell profile. The directional "
    "comparison (measured < PEC reference) is consistent with, not "
    "diagnostic of, edge-grading specifically (MF-5) -- a sharp but "
    "uniformly lossy disk would plausibly show the same qualitative "
    "pattern; no control case in this cycle disentangles the two "
    "mechanisms (queued, NOTES.md Next). This item bounds a previously-"
    "unbounded assumption; it does NOT change any scored thermal margin "
    "(MF-4) and does NOT resolve the separate, still-open iso_xsec_sq "
    "squaring-a-width-to-get-an-area convention question.")


def main():
    # -------------------- gates (stage 21's own 4-gate self-test, reused
    # here for the results.json record, not re-implemented)
    self_test = qt._self_test(verbose=False)
    assert self_test["all_gates_pass"], "qext_theory self-test gates failed -- do not trust results below"

    # -------------------- P-059-5: discriminating regression anchor
    comp = qt.compare_measured_to_pec(R_OUT_CELLS, DX_M, LAMBDA_M, SIGMA_EXT_CELLS)
    assert abs(comp.q_ext_pec_reference - 2.1177205150608365) <= 1e-9, \
        f"Q_ext_PEC(x)={comp.q_ext_pec_reference} does not reproduce the Phase-3-committed regression anchor"
    assert abs(comp.q_ext_measured - 1.5385088077964393) <= 1e-12, \
        "Q_ext_measured drifted from experiments/002-.../results.json's own committed value"

    # -------------------- MF-4: margin recompute under both bounding extremes
    # THERMODYNAMICS' own Phase-2 sensitivity (reproduced here, code-
    # verified, not hand-typed): p_abs_w (via absorbed_power_established_
    # ratio) scales as sigma_ext_cells^2 -- i.e. as Q_ext^2 at fixed
    # ratio_abs_ext and r_out -- while h_eff/mass/RADIATING area stay
    # UNMODIFIED on r_out throughout (T23/exp-054's own established, still-
    # correct convention; this item does not touch that chain at all). What
    # varies here is only the hypothetical Q_ext feeding p_abs_w's own
    # ABSORPTION-width area, not the radiating/convecting area.
    r_out_m = R_OUT_CELLS * DX_M

    def margin_for_hypothetical_q_ext(q_ext_hyp):
        p_abs_hyp = P_ABS_W_FLAGSHIP_CENTRAL * (q_ext_hyp / comp.q_ext_measured) ** 2
        regime_hyp = ts.mixed_length_scale_regime(
            p_abs_w=p_abs_hyp, l_geometric_m=r_out_m, k_air=K_AIR,
            density_kg_m3=DENSITY_SI_KG_M3, c_p_j_kgk=C_P_SI_J_KGK,
            emissivity=EMISSIVITY, t_ambient_k=T_AMBIENT_K)
        return NETD_BAND_K[0] / regime_hyp["dt_ss_full_K"], regime_hyp["dt_ss_full_K"]

    margin_floor, dt_floor = margin_for_hypothetical_q_ext(1.0)              # conservative Q_ext=1 floor
    margin_ceiling, dt_ceiling = margin_for_hypothetical_q_ext(comp.q_ext_pec_reference)  # PEC ceiling

    # exp-057's own established chain (the actual measured sigma_ext_cells,
    # the correct, standing convention) for reference -- unmodified.
    regime_established = ts.mixed_length_scale_regime(
        p_abs_w=P_ABS_W_FLAGSHIP_CENTRAL, l_geometric_m=r_out_m,
        k_air=K_AIR, density_kg_m3=DENSITY_SI_KG_M3, c_p_j_kgk=C_P_SI_J_KGK,
        emissivity=EMISSIVITY, t_ambient_k=T_AMBIENT_K)
    margin_established = NETD_BAND_K[0] / regime_established["dt_ss_full_K"]
    assert abs(margin_established - 699.27) < 0.5, \
        f"margin_established={margin_established} does not reproduce exp-057's own committed ~699.27x"
    assert abs(margin_floor - 1655.5) < 5.0, \
        f"margin_floor={margin_floor} does not reproduce THERMODYNAMICS' own Phase-2 recompute (~1655x)"
    assert abs(margin_ceiling - 369.0) < 5.0, \
        f"margin_ceiling={margin_ceiling} does not reproduce THERMODYNAMICS' own Phase-2 recompute (~369x)"

    out = {
        "meta": {
            "experiment": "exp-059", "panel_iteration": 36,
            "lead": "PHOTONICS (LOCKED, unconditional, breaking rotation)",
            "t1_escape_route": "NONE (sidecar/validation cycle)",
            "n_new_fdtd_calls": 0,
            "module": "lab/qext_theory.py (new, this cycle)",
            "trust_suite_stage": 21,
        },
        "self_test_gates": self_test,
        "flagship_comparison": {
            "x_ka": comp.x_ka,
            "q_ext_pec_reference": comp.q_ext_pec_reference,
            "q_ext_measured": comp.q_ext_measured,
            "ratio_measured_over_pec": comp.ratio_measured_over_pec,
            "q_ext_measured_sq_area_domain": comp.q_ext_measured_sq,
            "q_ext_pec_reference_sq_area_domain": comp.q_ext_pec_reference_sq,
            "source_note": comp.source_note,
            "diffraction_caveat": DIFFRACTION_CAVEAT,
        },
        "margin_sensitivity_MF4": {
            "established_margin_r_out_based_UNCHANGED": margin_established,
            "conservative_q_ext1_floor_margin": margin_floor,
            "pec_ceiling_margin": margin_ceiling,
            "note": ("MF-4 verification: substituting either bounding "
                     "extreme this item motivates into the AREA term only "
                     "(p_abs_w/h_eff/mass stay on the established r_out "
                     "convention, T23/exp-054) still leaves the margin "
                     f"{margin_ceiling:.0f}x-{margin_floor:.0f}x, both 2+ "
                     "orders of magnitude clear of NETD-lo -- confirms "
                     "THERMODYNAMICS' Phase-2 finding that NO scored "
                     "thermal classification changes. This is a "
                     "SENSITIVITY probe, not a claim that either bounding "
                     "area is the correct convention -- the established "
                     "r_out-based area (T23) stands unmodified."),
            "netd_disclaimer": NETD_DISCLAIMER,
        },
    }

    def _json_default(o):
        if isinstance(o, (np.bool_, bool)):
            return bool(o)
        if isinstance(o, (np.integer,)):
            return int(o)
        if isinstance(o, (np.floating,)):
            return float(o)
        raise TypeError(f"Object of type {o.__class__.__name__} is not JSON serializable")

    with open(os.path.join(HERE, "results.json"), "w") as f:
        json.dump(out, f, indent=2, default=_json_default)

    print(NETD_DISCLAIMER)
    print(f"Q_ext_PEC(x=ka={comp.x_ka:.4f}) = {comp.q_ext_pec_reference:.10f}")
    print(f"Q_ext_measured                  = {comp.q_ext_measured:.10f}")
    print(f"ratio measured/PEC              = {comp.ratio_measured_over_pec:.4f} "
          f"({comp.ratio_measured_over_pec*100:.1f}%)")
    print(f"empirical cross-validation max|rel_dev| = "
          f"{self_test['empirical_cross_validation']['max_abs_rel_dev']*100:.3f}% (bar 3%)")
    print(f"MF-4 margin sensitivity: established={margin_established:.2f}x "
          f"floor={margin_floor:.2f}x ceiling={margin_ceiling:.2f}x "
          f"(all 2+ orders of magnitude clear of NETD-lo)")
    print(DIFFRACTION_CAVEAT)
    print("results -> results.json")


if __name__ == "__main__":
    main()
