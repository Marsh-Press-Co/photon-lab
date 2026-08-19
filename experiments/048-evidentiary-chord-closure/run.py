"""exp-048 -- Closing exp-047's Evidentiary Chord (Panel Iteration 25).

Block A: formal REALIZABILITY_MEMO.md entry inputs for `graded_black_shell`
          at witness scale (geometric facts only; sigma_max figures
          explicitly illustrative-only, mandatory fix 2).
Block B: T21 fringe-contamination magnitude cross-check at the actual
          +-35deg fallback geometry (exp-030's GEOM[78]), reusing exp-042's
          own committed propagator, re-parameterized (mandatory fix 1).
Block C: source/retire check on `lab/glare_sidecar.py`'s unsourced
          [0.5,2.0] MARGINAL band, with QUANTUM's regime-applicability
          fold-in (mandatory fix 6).

Zero new FDTD calls. Predictions below are FROZEN before this script's
output is read as a result (house discipline) -- see NOTES.md for the
predict-commit.
"""
import json
import sys

import numpy as np

import design_geometry as dg

sys.path.insert(0, "../../")  # repo root, for `lab` and `experiments/047.../..`

PREDICTIONS = """
FROZEN PREDICTIONS (Panel Iteration 25, exp-048) -- committed before this
script's results are read. Corrected per Red Team's seven mandatory fixes
(LOGBOOK.md Iteration 25 Phase 2).

BLOCK A
  P-A1 (identity): thickness 0.308/0.615/0.923 m and core radius
    0.192/0.385/0.577 m (continuous formula, fix 1) match to <0.1%;
    tau_check == 24.0 exactly (algebraic identity) at all three witness
    radii, regardless of the illustrative-only sigma reading.
  P-A2: STRUCK (fix 7) -- no tier prediction made here; MATERIALS' charter
    call solicited fresh at Phase 5.
  P-A3 (non-interference): this entry moves ZERO existing verdicts.
  P-A4 (illustrative-only labelling, fix 2): sigma_max/e-folding figures
    reported, explicitly labelled non-physical.
  P-A5 (tau-conservation reframe, fix 3): stated as ordinary optical-depth
    conservation, not a forbidden material property.

BLOCK B
  P-B1 (consistency): predicted ripple period at the NEW geometry's own
    A (=OBJ_Y-ABSORB=764-40=724) lands within 5% of exp-042's own cited
    periods (1.4/1.9/2.4 deg at 450/600/750nm) -- predicted
    ~1.45/1.97/2.49 deg.
  P-B2 (contamination exists): at least one of the 27 (theta,lambda)
    FALLBACK_ANGLES x 3lambda points exceeds GATE_HARD=0.001.
  P-B3 (magnitude band): worst per-angle |C_empty| in [0.0005, 0.006].
  P-B4 (headline immunity, MULTIPLICATIVE per fix 4): P-G24-2's worst-case
    ratio (5.865e-3) scaled by the maximum possible |C| correction
    (0.7209 -> 1.0, a x1.3872 factor) reaches only 8.14e-3 -- 61x/246x
    below MARGINAL/FAIL. Regardless of what this block measures, P-G24-2
    survives.
  P-B5 (informational-point sensitivity): exp-047's own near-boundary
    ratios (0.929, 1.085, 0.907) shift by <0.1 ratio-units under a
    worst-case uncancelled correction at this new geometry -- no category
    flip.
  P-B6 (scope, fix 5): this block's own deliverable is a re-parameterization
    + magnitude cross-check ONLY -- P-B2/P-B3 are explicitly INCONCLUSIVE
    against T24's own uncharacterized ABSORB=40 boundary systematic
    (0.002-0.007 absolute), held fixed, uncorrected this cycle.
  REGRESSION GATE (self-check, not a science prediction): the generalized
    `field_and_h`/`edge_diffraction_c_empty_corrected` reproduces
    exp-042's own committed module's output EXACTLY (bit-for-bit) at the
    OLD (exp-042) geometry, theta=+40deg, all 3 lambda -- proves the
    generalization introduced no bug before any NEW-geometry number is
    trusted.

BLOCK C
  P-C1 (arithmetic): 10^0.3 and 10^-0.3 match 2.0/0.5 to <0.3%.
  P-C2 (provenance + regime-applicability, fix 6): T2's +-0.3-log vertical
    threshold uncertainty is committed specifically for the "Scotopic
    scaling" (low-luminance, unclamped/exponent-sensitive) regime
    (LOGBOOK.md). Predicted: all three of exp-047's own near-boundary
    points sit in that regime (L_eq well below L_REF=3.0 cd/m^2, not the
    clamped photopic floor) -- applicability CONFIRMED for the points that
    currently matter; NOT verified for any future point at L_eq>=3.
  P-C3 (conditional recommendation): if P-C2 holds -> SOURCE (cite T2,
    zero numeric change to `lab/glare_sidecar.py`); else -> RETIRE.
"""


def block_a():
    rows = []
    for r_w in dg.WITNESS_R_M:
        thickness = dg.shell_thickness_m(r_w)
        core = dg.core_radius_m(r_w)
        sigma_illustrative = dg.physical_sigma_max_illustrative_only(r_w)
        tau = dg.tau_check(r_w)
        efold_cm = 100.0 / sigma_illustrative
        rows.append(dict(
            witness_r_m=r_w, thickness_m=round(thickness, 6),
            core_radius_m=round(core, 6),
            sigma_max_illustrative_only_permeter=round(sigma_illustrative, 4),
            efold_length_illustrative_only_cm=round(efold_cm, 4),
            tau_check=tau,
        ))
    tau_ok = all(abs(row["tau_check"] - dg.TAU_SHELL) < 1e-9 for row in rows)
    return dict(
        rows=rows,
        tau_identity_holds=tau_ok,
        c_anchor=dg.C_ANCHOR,
        c_anchor_citation=dg.C_ANCHOR_CITATION,
        prior_tier_call=dg.PRIOR_TIER_CALL,
        sigma_illustrative_only_disclaimer=(
            "NOT physically-grounded conductivities -- literal reuse of the "
            "FDTD's cell-normalized sigma_max_shell formula fed meter-valued "
            "input, no dx/unit bridge established (mandatory fix 2)."
        ),
        tau_conservation_reframe=(
            "Holding tau_shell constant under self-similar r-scaling is "
            "ordinary optical-depth conservation, achievable via an "
            "independently-chosen conductivity/doping at each build size -- "
            "NOT a forbidden material property (mandatory fix 3)."
        ),
        tier_prediction_struck="P-A2 struck per mandatory fix 7 -- MATERIALS' own charter call, not predicted here.",
    )


def block_b():
    # --- regression gate: OLD geometry must reproduce exp-042's own module
    old_anchors = {
        450: -0.010329176182132263,
        600: -0.004649509989137881,
        750: -0.006421144336224298,
    }
    regression = {}
    for lam, cpl in dg.CPL.items():
        val = dg.edge_diffraction_c_empty_corrected(40.0, cpl, dg.GEOM_EXP042_OLD)
        ref = old_anchors[lam]
        regression[lam] = dict(value=val, ref=ref, rel_err=abs(val - ref) / abs(ref))
    regression_ok = all(v["rel_err"] <= 1e-9 for v in regression.values())

    # --- P-B1: ripple period at the NEW geometry's own A
    gd = dg._geom_derived(dg.GEOM78)
    a_new = gd["a"]
    predicted_periods = {lam: dg.ripple_period_deg(a_new, cpl) for lam, cpl in dg.CPL.items()}
    cited_periods = {450: 1.4, 600: 1.9, 750: 2.4}
    period_rel_err = {lam: abs(predicted_periods[lam] - cited_periods[lam]) / cited_periods[lam]
                       for lam in dg.CPL}

    # --- Main scan: FALLBACK_ANGLES x 3 lambda at the NEW (exp-030) geometry
    rows = []
    for theta in dg.FALLBACK_ANGLES:
        for lam, cpl in dg.CPL.items():
            c_empty = dg.edge_diffraction_c_empty_corrected(theta, cpl, dg.GEOM78)
            rows.append(dict(theta=theta, lam_nm=lam,
                              c_empty=c_empty, abs_c_empty=abs(c_empty),
                              exceeds_gate_hard=abs(c_empty) > dg.GATE_HARD,
                              exceeds_c_thr_lab=abs(c_empty) > dg.GATE_PERCEPTUAL_CONTEXT))
    worst = max(rows, key=lambda r: r["abs_c_empty"])
    n_exceed_gate_hard = sum(r["exceeds_gate_hard"] for r in rows)

    # --- P-B4: multiplicative headline-immunity bound
    p_g24_2_worst_ratio = 5.865e-3
    max_c_scale = 1.0 / abs(dg.C_ANCHOR)
    corrected_worst_ratio = p_g24_2_worst_ratio * max_c_scale
    margin_to_marginal = 0.5 / corrected_worst_ratio if corrected_worst_ratio else float("inf")
    margin_to_fail = 2.0 / corrected_worst_ratio if corrected_worst_ratio else float("inf")

    # --- P-B5: sensitivity of exp-047's near-boundary points (informational only)
    # An uncancelled worst-case ABSOLUTE contamination (this block's own worst
    # |C_empty|) is added to |C_eff| directly (conservative: assumes zero
    # cancellation with the veiling-dilution machinery) and the ratio shift
    # is reported.
    near_boundary = [
        dict(label="P-G24-1 L_B=1e-5,p=0.4", c_eff=-0.7209, c_thr=0.77592278695768, ratio=0.9290872907942049),
        dict(label="P-G24-1 L_B=1.7e-4,p=0.5", c_eff=-0.7209, c_thr=0.6642111641550714, ratio=1.085347610675953),
        dict(label="P-G24-3 L_B=1.7e-4,p=0.4,theta=10,E=0.01", c_eff=-0.10474615384615385, c_thr=0.11548994154398182, ratio=0.9069720916454319),
    ]
    for row in near_boundary:
        c_eff_shifted = row["c_eff"] - np.sign(row["c_eff"]) * worst["abs_c_empty"]
        row["ratio_shifted_worst_case"] = abs(c_eff_shifted) / row["c_thr"]
        row["ratio_delta"] = row["ratio_shifted_worst_case"] - row["ratio"]

    return dict(
        regression=regression, regression_ok=regression_ok,
        geom78=dg.GEOM78, a_new=a_new,
        predicted_periods_deg=predicted_periods, cited_periods_deg=cited_periods,
        period_rel_err=period_rel_err,
        rows=rows, worst=worst, n_exceed_gate_hard=n_exceed_gate_hard,
        n_total=len(rows),
        p_g24_2_worst_ratio=p_g24_2_worst_ratio,
        multiplicative_scale_to_ceiling=max_c_scale,
        corrected_worst_ratio_multiplicative=corrected_worst_ratio,
        margin_to_marginal=margin_to_marginal, margin_to_fail=margin_to_fail,
        near_boundary_sensitivity=near_boundary,
        scope_note=(
            "Re-parameterization + magnitude cross-check ONLY (mandatory "
            "fix 5) -- INCONCLUSIVE against live thread T24's own "
            "uncharacterized ABSORB=40 boundary systematic (0.002-0.007 "
            "absolute), held fixed and uncorrected this cycle."
        ),
        beamformed_array_disclosure=(
            "This block's per-angle numbers, like exp-041/042's own, are "
            "produced by `_src_amp` driving the FULL tapered aperture with "
            "a per-theta linear phase ramp -- the same deliberately "
            "beamformed/focused synthetic-array construction exp-046/T21 "
            "already flagged as physically distinct from a naturally-"
            "divergent single-mode emitter (mandatory fix 6)."
        ),
    )


def block_c():
    hi, lo = dg.log_band_ratio(dg.T2_VERTICAL_LOG_UNCERTAINTY)
    hi_err = abs(hi - dg.MARGINAL_HI) / dg.MARGINAL_HI
    lo_err = abs(lo - dg.MARGINAL_LO) / dg.MARGINAL_LO

    # regime-applicability check (QUANTUM's fold-in, mandatory fix 6):
    # do exp-047's own near-boundary points sit in the CLAMPED
    # (photopic-floor, L_eq>=L_REF) or UNCLAMPED (low-luminance,
    # exponent-sensitive) regime?
    near_boundary_l_eq = [1e-05, 0.00017, 0.00117]
    regime = [dict(l_eq_cdm2=l, clamped=(l >= dg.L_REF_CDM2)) for l in near_boundary_l_eq]
    all_unclamped = all(not r["clamped"] for r in regime)

    recommend = "SOURCE" if (hi_err < 0.01 and lo_err < 0.01 and all_unclamped) else "RETIRE"

    return dict(
        computed_hi=hi, computed_lo=lo,
        target_hi=dg.MARGINAL_HI, target_lo=dg.MARGINAL_LO,
        hi_rel_err=hi_err, lo_rel_err=lo_err,
        t2_source="LOGBOOK.md 'Scotopic scaling' section -- committed threshold "
                  "function C_thr(L)=0.005*max[1,(L/3)^-0.4], vertical uncertainty +-0.3 log",
        near_boundary_regime=regime,
        all_near_boundary_points_unclamped=all_unclamped,
        recommendation=recommend,
        recommendation_scope=(
            "Applicability CONFIRMED for exp-047's own three near-boundary "
            "points (all L_eq << L_REF=3.0, the low-luminance regime this "
            "+-0.3-log figure is committed for). NOT verified for any "
            "future near-boundary point at L_eq>=L_REF (the clamped "
            "photopic floor), where c_thr is pinned and the vertical-log "
            "uncertainty's own applicability is unaddressed by this cycle."
        ),
    )


def main():
    print(PREDICTIONS)
    a = block_a()
    b = block_b()
    c = block_c()

    print("\n=== BLOCK A ===")
    for row in a["rows"]:
        print(f"  r_w={row['witness_r_m']}m: thickness={row['thickness_m']}m "
              f"core={row['core_radius_m']}m sigma*={row['sigma_max_illustrative_only_permeter']} "
              f"(illustrative-only) efold={row['efold_length_illustrative_only_cm']}cm tau={row['tau_check']}")
    print(f"  tau identity holds at all 3 points: {a['tau_identity_holds']}")

    print("\n=== BLOCK B ===")
    print(f"  regression gate (OLD geometry, theta=+40, 3lambda) exact match: {b['regression_ok']}")
    for lam, v in b["regression"].items():
        print(f"    {lam}nm: {v['value']:.15f} vs ref {v['ref']:.15f} (rel_err {v['rel_err']:.2e})")
    print(f"  NEW geometry A={b['a_new']}")
    for lam in dg.CPL:
        print(f"    predicted period {lam}nm: {b['predicted_periods_deg'][lam]:.3f}deg "
              f"vs cited {b['cited_periods_deg'][lam]}deg (rel_err {b['period_rel_err'][lam]:.1%})")
    print(f"  {b['n_exceed_gate_hard']}/{b['n_total']} points exceed GATE_HARD={dg.GATE_HARD}")
    print(f"  worst: theta={b['worst']['theta']} lam={b['worst']['lam_nm']} "
          f"|C_empty|={b['worst']['abs_c_empty']:.6f}")
    print(f"  P-B4 multiplicative: worst P-G24-2 ratio {b['p_g24_2_worst_ratio']} "
          f"x {b['multiplicative_scale_to_ceiling']:.4f} = {b['corrected_worst_ratio_multiplicative']:.6f} "
          f"-> {b['margin_to_marginal']:.1f}x/{b['margin_to_fail']:.1f}x below MARGINAL/FAIL")
    print(f"  scope: {b['scope_note']}")

    print("\n=== BLOCK C ===")
    print(f"  10^+0.3={c['computed_hi']:.5f} vs {c['target_hi']} (err {c['hi_rel_err']:.4%})")
    print(f"  10^-0.3={c['computed_lo']:.5f} vs {c['target_lo']} (err {c['lo_rel_err']:.4%})")
    print(f"  near-boundary regime check: {c['near_boundary_regime']}")
    print(f"  recommendation: {c['recommendation']}")

    out = dict(experiment="exp-048", panel_iteration=25, lead_seat="VISION SCIENCE",
               block_a=a, block_b=b, block_c=c)
    with open("results.json", "w") as f:
        json.dump(out, f, indent=2, default=str)
    print("\nwrote results.json")


if __name__ == "__main__":
    main()
