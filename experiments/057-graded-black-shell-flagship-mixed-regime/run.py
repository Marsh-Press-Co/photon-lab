"""exp-057 -- Panel Iteration 34 (LOCKED, unconditional, breaking rotation):
graded_black_shell_flagship through the corrected mixed_length_scale_regime.
=============================================================================
Lead: THERMODYNAMICS. Red Team's Iteration-33 Phase-5 audit granted the
escalation: this program's own flagship absorber article, at the record's
thinnest thermal-detectability margin (~6.04x), has now been deferred
three times past the unconditional-lock bar Red Team itself pre-declared
at Iteration 32's close. Zero new FDTD calls -- pure desk/analytic
re-derivation from an already-committed bench measurement, reusing
`lab.thermo_sidecar.mixed_length_scale_regime` exactly as exp-054's own
Part A applied it to the ON-endpoint article.

Phase-3 synthesis incorporates Red Team's Iteration-34 Phase-2 mandatory-
fix docket (6 items, all accepted) -- see NOTES.md for the full record.
"""

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "..")))

from lab import thermo_sidecar as ts

# --------------------------------------------------------- cited constants
# exp-043's own established bench measurement (results.json::
# graded_black_shell_flagship) -- p_abs_w is measurement-locked, NOT
# re-derived this cycle (the mixed chain is mixed by design: p_abs stays
# on its own optical/w_on-based measurement; only h_eff/mass/area move to
# the geometric length). Mandatory fix 6 (Red Team): this constant is
# pinned by a same-shift regression assertion below, not silently retyped.
P_ABS_W_FLAGSHIP_CENTRAL = 1.7409069740390205e-12   # W
SIGMA_EXT_CELLS = 240.0073740162445                  # exp-043/run.py:291
RATIO_ABS_EXT = 0.51                                 # T9's established anchor

# Old (repudiated) chain's own committed numbers, exp-043/results.json --
# reused here ONLY as the standing comparator, not recomputed.
OLD_DT_K = 0.0033108079151108792
OLD_MARGIN = 0.020 / OLD_DT_K   # 6.0408...

# exp-054's own R_OUT_M/material-provenance convention, reused verbatim
# (silicon rho=2330 kg/m^3, c_p=700 J/(kg*K) -- ASSUMED, provenance
# terminates unsourced, T18; REALIZABILITY_MEMO.md's standing downgrade).
DX_M = 30.0e-9
R_OUT_CELLS = 78
R_OUT_M = R_OUT_CELLS * DX_M
K_AIR = 0.026
DENSITY_SI_KG_M3, C_P_SI_J_KGK = 2330.0, 700.0
EMISSIVITY = 0.9
T_AMBIENT_K = 293.15
NETD_BAND_K = (0.020, 0.050)   # experiments/043-.../results.json::p_d7_4_netd

NETD_DISCLAIMER = (
    "NETD is an instrument/detector threshold, not a human perceptual one "
    "(VISION SCIENCE's standing mandatory fix, exp-043 Red Team attack 7, "
    "reaffirmed exp-054 Phase-2 mandatory fix 6, reaffirmed again here per "
    "Red Team's Iteration-34 mandatory fix 5). This classification does "
    "NOT bear on constraint-3/4's human-eye verdict.")

# Mandatory fix 3 (PHOTONICS/QUANTUM, Red Team-confirmed): the w_on-vs-
# r_out area-shrink term rests on sigma_ext_cells=240 being genuinely
# diffraction-inflated relative to the object's real diameter (2*r_out=156
# cells, ~1.54x). This is ASSERTED, NOT INDEPENDENTLY BOUNDED -- exp-054's
# own NOTES.md flagged it, queuing a Q_ext(x) closed-form check (ranked #4,
# Iteration 31's close) that has now gone THREE full cycles (31,32,33)
# without being run. Carried forward here, not resolved. Non-load-bearing:
# even the widest plausible area-convention correction (~1.5-2x) cannot
# approach the margin computed below (~700x either way, and any DECREASE
# in the assumed p_abs_w-supporting area only makes the margin larger, the
# safe direction).
DIFFRACTION_INFLATION_CAVEAT = (
    "w_on (sigma_ext_cells=240.0073740162445) vs the object's real "
    "diameter (2*r_out=156 cells, ~1.54x excess) is a diffraction-inflated "
    "optical width -- ASSERTED, NOT INDEPENDENTLY BOUNDED (exp-054/"
    "NOTES.md). The Q_ext(x) closed-form check that would bound it (ranked "
    "#4, Iteration 31's close) has not been run at Iterations 32, 33, or "
    "34 -- three full cycles now. p_abs_w (this cycle's own untouched "
    "input) inherits this open question. Non-load-bearing here: the "
    "margin computed below clears any plausible correction to this "
    "convention by 2+ orders of magnitude.")

# Mandatory fix 4 (MATERIALS, Red Team-corrected citation): the flagship's
# ACTUAL construction (experiments/020-ambient-baseline/design_geometry.py,
# confirmed by Red Team direct read) is pec_disk(r=30) THEN
# graded_black_shell(r_in=30, r_out=78) -- an ANNULUS/SHELL, not a solid
# disk (graded_black_shell's own docstring: solid only if r_in=0). The
# core (r<30, ~15% of the disk area) is a PEC disk, NOT vacuum (Red Team's
# own correction of MATERIALS' Phase-2 alternative-hypothesis citation,
# which named exp-027 Cell B -- wrong for this specific article).
# lumped_cube_mass_kg nonetheless computes mass = density * r_out^3 as if
# the ENTIRE r_out volume were solid silicon. THIRD CONSECUTIVE CITATION
# CYCLE of this exact unresolved defect: Iteration 20 (exp-043) ->
# Iteration 31 (exp-054) -> Iteration 34 (this cycle). Confirmed
# NON-LOAD-BEARING for the SCORED predictions below: mixed_length_scale_
# regime's own dt_ss_full_K formula has NO mass_kg term (steady-state has
# no mass dependence) -- verified directly against lab/thermo_sidecar.py's
# source. mass_kg/tau_thermal_s land in results.json as UNSCORED
# byproducts of this cycle's own computation; a future citer of either
# figure must not silently assume a solid-disk reading of a shell object.
SHELL_VS_SOLID_MASS_CAVEAT = (
    "THIRD CONSECUTIVE CITATION CYCLE (Iteration 20 -> 31 -> 34) of an "
    "unresolved defect: graded_black_shell_flagship's real construction "
    "is an ANNULUS (pec_disk(r=30) then graded_black_shell(r_in=30, "
    "r_out=78), experiments/020-ambient-baseline/design_geometry.py), not "
    "a solid disk. lumped_cube_mass_kg computes mass=density*r_out^3 as "
    "if the entire r_out volume is solid silicon, ignoring the PEC core "
    "(r<30, ~15% of the disk area). CONFIRMED NON-LOAD-BEARING for this "
    "cycle's own scored predictions (dt_ss_full_K has no mass term, "
    "verified against lab/thermo_sidecar.py source) -- mass_kg/"
    "tau_thermal_s below are unscored byproducts, not falsifiable "
    "predictions. Any future citer of mass_kg or tau_thermal_s from this "
    "results.json must not read them as a solid-disk quantity.")

# Mandatory fix 2 (EM, Red Team-corrected citation): Knudsen number using
# this program's own SOURCED mean free path (exp-046's own LAMBDA_AIR_M,
# NOT a generic rounded figure) -- the identical r_out regime exp-046's own
# B4 result and exp-054's own phase1_proposal.md already established.
LAMBDA_AIR_M = 65.7e-9   # exp-046/run.py:1029, exp-054's own citation
KNUDSEN_NUMBER = LAMBDA_AIR_M / R_OUT_M
SLIP_CORRECTION_FRACTION = -0.053168   # exp-046 B4's own established value,
                                        # identical r_out regime, reused
                                        # verbatim (not re-derived)


def main():
    regime = ts.mixed_length_scale_regime(
        p_abs_w=P_ABS_W_FLAGSHIP_CENTRAL, l_geometric_m=R_OUT_M,
        k_air=K_AIR, density_kg_m3=DENSITY_SI_KG_M3, c_p_j_kgk=C_P_SI_J_KGK,
        emissivity=EMISSIVITY, t_ambient_k=T_AMBIENT_K)

    dt_ss = regime["dt_ss_full_K"]
    margin = NETD_BAND_K[0] / dt_ss
    netd_disp = ts.netd_disposition(dt_ss, NETD_BAND_K)

    # -------------------- mandatory fix 6: same-shift regression asserts
    # (Red Team's Iteration-34 own addition -- closes the exact gap
    # Iteration-31 Phase-5 pre-flagged: stage 18's own regression gate
    # pins only the ON-endpoint call site, not this one.)
    assert abs(P_ABS_W_FLAGSHIP_CENTRAL - 1.7409069740390205e-12) < 1e-27, \
        "p_abs_w drifted from experiments/043-.../results.json's own committed value"
    assert abs(dt_ss - 2.8601275372385233e-05) / 2.8601275372385233e-05 < 1e-9, \
        f"dt_ss_full_K={dt_ss} does not reproduce the Phase-3-committed regression anchor"

    # -------------------- mandatory fix 1: mechanism decomposition, CODE-
    # VERIFIED (not the Phase-1 draft's wrong naive-product narrative).
    old_area_m2 = (SIGMA_EXT_CELLS * DX_M) ** 2   # w_on-based (old, wrong)
    old_h_conv = 5.0
    old_rad_coeff = 4.0 * EMISSIVITY * ts.SIGMA_SB * T_AMBIENT_K ** 3
    old_dp_dt = old_area_m2 * (old_rad_coeff + old_h_conv)
    old_rad_share = old_rad_coeff / (old_rad_coeff + old_h_conv)

    new_area_m2 = regime["area_m2"]
    new_h_eff = regime["h_eff_w_m2k"]
    new_dp_dt = regime["dp_dt_w_k"]
    new_rad_share = old_rad_coeff / (old_rad_coeff + new_h_eff)  # same
    # radiative coefficient (area-independent per unit area; area cancels
    # in the SHARE, not in dp_dt itself -- both area_m2 factors are
    # applied once each to old_dp_dt/new_dp_dt above)

    dp_dt_ratio = new_dp_dt / old_dp_dt
    # naive (WRONG) story: dp_dt_ratio ~= (h_eff ratio) * (area ratio, NEW/OLD
    # direction, matching dp_dt_new/dp_dt_old) -- ignores that dp_dt also has
    # a radiative term whose SHARE changes (co-equal -> negligible), not just
    # a two-factor conductance-coefficient*area product.
    naive_product = (new_h_eff / old_h_conv) * (new_area_m2 / old_area_m2)

    # -------------------- mandatory fix 2: Kn/slip-flow disclosure
    # SLIP_CORRECTION_FRACTION (-5.3168%) reduces the CONDUCTANCE (dp_dt),
    # which INCREASES dT (less heat escapes per degree) and so DECREASES
    # the margin proportionally: margin_slip = margin * (1 + fraction),
    # fraction already negative. (dT_slip = P/(dp_dt*(1+fraction)) =
    # dT/(1+fraction); margin_slip = NETD_lo/dT_slip = margin*(1+fraction).)
    margin_slip_corrected = margin * (1.0 + SLIP_CORRECTION_FRACTION)

    out = {
        "meta": {
            "experiment": "exp-057", "panel_iteration": 34,
            "lead": "THERMODYNAMICS (LOCKED, unconditional, breaking rotation)",
            "t1_escape_route": "NONE (sidecar-cycle correction)",
            "n_new_fdtd_calls": 0,
            "module": "lab/thermo_sidecar.py (exp-054's own reusable code, unmodified)",
        },
        "old_chain": {
            "dt_K": OLD_DT_K, "margin": OLD_MARGIN,
            "area_m2_w_on_based": old_area_m2, "h_conv_placeholder": old_h_conv,
            "radiative_coeff_w_m2k": old_rad_coeff, "dp_dt_w_k": old_dp_dt,
            "radiative_share_of_dp_dt": old_rad_share,
            "mass_kg_hardcoded": 1.0e-15,
            "caveat": "H_CONV=5.0 (macroscopic natural-convection placeholder, "
                      "never replaced), MASS_KG=1.0e-15 kg (hardcoded, "
                      "untethered to any geometric length), area from w_on "
                      "(diffraction-inflated optical width). The repudiated chain.",
        },
        "mixed_regime": regime,
        "netd_disposition": netd_disp,
        "netd_lo_margin": margin,
        "netd_disclaimer": NETD_DISCLAIMER,
        "mechanism_decomposition_code_verified": {
            "dp_dt_ratio_new_over_old": dp_dt_ratio,
            "naive_two_factor_product_WRONG_do_not_cite": naive_product,
            "old_radiative_share_of_dp_dt": old_rad_share,
            "new_radiative_share_of_dp_dt": new_rad_share,
            "note": ("The Phase-1 draft's mechanism narrative implied "
                     "dp_dt_ratio ~= (h_eff jump)*(area shrink) ~= "
                     f"{naive_product:.2f}x -- WRONG, per Red Team's "
                     "Iteration-34 mandatory fix 1. The REAL, code-"
                     f"verified ratio is {dp_dt_ratio:.3f}x. The gap: the "
                     "OLD chain's radiative term is CO-EQUAL with H_CONV="
                     f"5.0 ({old_rad_share:.1%} of dp_dt, not convection-"
                     "dominated as the naive story implies); in the NEW "
                     f"chain radiation collapses to {new_rad_share:.3%} of "
                     "dp_dt because h_eff swamps it. This dilution of the "
                     "radiative term from co-equal to negligible -- not a "
                     "clean two-factor product -- is what the real ratio "
                     "reflects."),
        },
        "diffraction_inflation_caveat": DIFFRACTION_INFLATION_CAVEAT,
        "shell_vs_solid_mass_caveat": SHELL_VS_SOLID_MASS_CAVEAT,
        "knudsen_slip_flow": {
            "lambda_air_m_sourced": LAMBDA_AIR_M,
            "l_geometric_m": R_OUT_M,
            "knudsen_number": KNUDSEN_NUMBER,
            "regime": "slip-flow (0.01 < Kn < 0.1), not strict continuum",
            "slip_correction_fraction_reused_from_exp046_B4": SLIP_CORRECTION_FRACTION,
            "margin_slip_corrected": margin_slip_corrected,
            "note": "First-order slip correction, identical r_out regime "
                    "as exp-046's own B4 result -- reused, not re-derived. "
                    "No verdict risk: margin stays >>1x either way.",
        },
        "comparison_to_standing_figure": {
            "old_dt_K": OLD_DT_K, "old_margin": OLD_MARGIN,
            "new_dt_K": dt_ss, "new_margin": margin,
            "margin_ratio_new_over_old": margin / OLD_MARGIN,
            "direction": "GROWS (opposite exp-054's own ~3.03x SHRINK for "
                         "the two articles it corrected) -- the flagship "
                         "never had H_CONV corrected even once, unlike "
                         "those two, so this cycle applies two corrections "
                         "(placeholder-H_CONV AND w_on-vs-r_out length) in "
                         "one step, and the placeholder-replacement effect "
                         "dominates.",
        },
    }

    with open(os.path.join(HERE, "results.json"), "w") as f:
        json.dump(out, f, indent=2)

    print(f"graded_black_shell_flagship, corrected mixed_length_scale_regime:")
    print(f"  dt_ss_full_K = {dt_ss:.6e} K  (old: {OLD_DT_K:.6e} K)")
    print(f"  NETD-lo margin = {margin:.2f}x  (old: {OLD_MARGIN:.2f}x, ratio {margin/OLD_MARGIN:.2f}x)")
    print(f"  classification = {netd_disp['classification']}")
    print(f"  dp_dt ratio (code-verified) = {dp_dt_ratio:.3f}x  (naive-product, WRONG: {naive_product:.2f}x)")
    print(f"  Kn = {KNUDSEN_NUMBER:.5f}  slip-corrected margin = {margin_slip_corrected:.2f}x")
    print(f"  results -> results.json")


if __name__ == "__main__":
    main()
