"""VISION SCIENCE's glare/adaptation Tier-W sidecar (panel Iteration 24,
exp-047 -- docket #7's second and final half; THERMO's own half, the
witness-photometry table, closed at Iteration 20/exp-043).

EXPRESSIBILITY CONTRACT (PANEL.md): every function here is a POST-RUN
ANALYTIC calculation, not an FDTD output -- desk radiometry composed onto
an ALREADY-MEASURED bench quantity (the graded_black_shell absorber's own
Weber contrast). Nothing in this module runs a field solve.

MANDATORY-FIX PROVENANCE (Red Team's Phase-2 audit, Iteration 24, ruling
proceed-with-mandatory-fixes, all seven items adopted, none overridden --
full record: LOGBOOK.md Iteration 24):

  1. [constraint-3-violation, load-bearing] Every "clears Tier-W" claim
     this module's callers make MUST be labeled TIER_W_HEADLINE_LABEL
     below, not bare "Tier-W" -- the C value composed here is a
     NEAR-FIELD bench measurement (r_out~78 cells, ~2.3 um shell), not a
     witness-scale (45 m) measurement, and this program's own T13/T14
     threads show the two do NOT track each other the naive way (T14:
     measured |C| SHALLOWS, not deepens, toward far field; T13: two
     independent extrapolation fits disagree by 0.220, unresolved).
  2. [inconsistency] C_MEASURED is cited to Iteration 7's close (exp-030),
     NOT Iteration 4 (exp-027, an unrelated diagnostic cycle) -- the
     Phase-1 proposal's own citation was wrong; EM's catch, independently
     re-verified by Red Team directly against LOGBOOK.md.
  3. [inconsistency] `graded_black_shell` has never been formally scored
     by REALIZABILITY_MEMO.md (which covers only sigma(I) switching
     classes). Its own Iteration-7/exp-030 Phase-5 record carries an
     INFORMAL UNOBTANIUM call for a self-similar witness-scale
     realization (required shell thickness 0.31-0.92 m at r_w=0.5-1.5m).
     Carried here as WITNESS_SCALE_REALIZABILITY, inline, not a silent
     gap.
  4. [inconsistency, caught by no blind seat] Tier-W's own definition
     (PANEL.md) names the observer explicitly as "the flashlight
     holder" -- the maximally CUED case. The frozen threshold ladder's
     two bars are NOT interchangeable readings of the same conditions:
     lab=0.005 is the cued bar, field=0.02=lab*4 is the UNCUED bar
     (exp-020 NOTES.md, "field factor x4 (uncued observer)"). This module
     scores the LAB (cued) bar as the Tier-W default and computes field
     only for comparison, never as a headline substitute.
  5. [unfalsifiable, resolvable] Near-eye ocular exposure at the CEILING
     glare estimate was never checked against anything. This module
     exposes `corneal_irradiance_wcm2` so every ceiling-estimate result
     carries its own corneal-irradiance figure alongside the contrast
     number -- SINGLE-PASS only; session-accumulated dose over multiple
     sweep passes is explicitly flagged as open, not computed here.
  6. QUANTUM's threshold-transfer caveat, corrected: C_thr(L) is
     established for glare GENERALLY (Adrian 1989 is CIE road-lighting
     disability-glare literature, already load-bearing in the field-x4
     factor) but UNVERIFIED specifically for a localized, near-field
     (<1m), self-held entoptic-scatter source -- narrower than "diffuse
     ambient only" as QUANTUM's Phase-2 critique first framed it.
  7. P-VIS24-3-class results (the FLOOR-glare-estimate branch) are
     DEMOTED to informational-only, never fed into the headline
     commitment -- T7's real ~1.5-1.9% chromatic red-growth and T21's
     unresolved ~1-2deg-period angular fringe (both un-error-banded
     anywhere in this module or its caller) sit specifically inside this
     branch's own thin margin.
"""
from __future__ import annotations

import math

# ------------------------------------------------------------- constants

C_MEASURED = -0.7209
C_MEASURED_CITATION = (
    "Iteration 7 close (exp-030), V-weighted back-lit, r=78 cells, "
    "+-35deg fallback geometry, floor-corrected -- NOT Iteration 4 "
    "(exp-027, an unrelated diagnostic cycle); NOT exp-020's superseded "
    "-0.686/-0.6855 (pre-floor-correction)."
)

C_THR_BASE = 0.005          # lab (cued observer) bar, photopic reference
C_THR_L_REF_CDM2 = 3.0
C_THR_FIELD_FACTOR = 4.0    # uncued observer -- NOT the Tier-W default (fix 4)
C_THR_P_BAND = (0.4, 0.5)
C_THR_SOURCES = ("Blackwell 1946", "Rose 1948", "CIE 19/2 (1981)", "Adrian 1989")

WITNESS_SCALE_REALIZABILITY = {
    "tier": "UNOBTANIUM (informal call, not a formal REALIZABILITY_MEMO.md entry)",
    "required_shell_thickness_m": (0.31, 0.92),
    "witness_radius_m": (0.5, 1.5),
    "source": "Iteration 7 (exp-030) Phase 5, MATERIALS seat, informal call",
}

TIER_W_HEADLINE_LABEL = (
    "clears the bench-scale glare-diluted SURROGATE of Tier-W, pending the "
    "T8/T13/T14 near-field-to-witness-scale bridge -- NOT a witness-scale "
    "constraint-3 verdict"
)

STILES_HOLLADAY_VALID_THETA_DEG = (1.0, 30.0)  # canonical range, not
# independently re-verified via WebFetch this cycle (T18 blocked)


def c_thr(L_cdm2: float, p: float, bar: str = "lab") -> float:
    """Frozen threshold function (T2, exp-020, corrected exp-024):
    C_thr(L) = 0.005 * max[1, (L/3)^-p], clipped at 1 (photopic floor),
    field bar = lab bar * 4 (uncued observer -- exp-020 NOTES.md).
    `bar="lab"` is Tier-W's own default (fix 4): the flashlight holder is
    the maximally CUED observer PANEL.md names."""
    if L_cdm2 <= 0:
        raise ValueError(f"L_cdm2 must be > 0, got {L_cdm2}")
    if bar not in ("lab", "field"):
        raise ValueError(f"bar must be 'lab' or 'field', got {bar!r}")
    base = C_THR_BASE * max(1.0, (L_cdm2 / C_THR_L_REF_CDM2) ** (-p))
    return base * C_THR_FIELD_FACTOR if bar == "field" else base


def stiles_holladay_veiling_luminance(e_lux: float, theta_deg: float) -> float:
    """Stiles-Holladay disability-glare veiling luminance, L_v = 10*E/theta^2
    (Holladay 1926; Stiles 1929). Canonical validity range
    STILES_HOLLADAY_VALID_THETA_DEG (CIE 146:2002/road-lighting
    literature) -- NOT independently re-verified via WebFetch this cycle
    (T18 blocked); flagged, not silently assumed valid outside that range
    (the "fixed-gaze" scenario's own large-theta excursions are stated
    idealizations, not claims)."""
    if theta_deg <= 0:
        raise ValueError(f"theta_deg must be > 0, got {theta_deg}")
    return 10.0 * e_lux / (theta_deg ** 2)


def veiled_adapting_luminance(l_b_cdm2: float, l_v_cdm2: float) -> float:
    """L_eq = L_B + L_v -- the elevated adapting background a glare-exposed
    eye actually sees."""
    return l_b_cdm2 + l_v_cdm2


def veiled_contrast(c_measured: float, l_v_cdm2: float, l_b_cdm2: float) -> float:
    """C_eff = C_measured / (1 + L_v/L_B) -- the standard veiling-contrast
    dilution relation (CIE 146:2002 Threshold Increment family, not
    independently re-verified via WebFetch this cycle -- flagged, not
    load-bearing: see `veiled_contrast_direct` for the first-principles
    derivation this is checked against). EM's Phase-2 re-derivation
    (Iteration 24): algebraically identical to C_measured*L_b/(L_b+L_v),
    obtained by adding L_v uniformly to both the object and flank
    luminance windows before taking Weber contrast -- gated bit-exact
    against `veiled_contrast_direct` (trust-suite stage 17)."""
    return c_measured / (1.0 + l_v_cdm2 / l_b_cdm2)


def veiled_contrast_direct(c_measured: float, l_v_cdm2: float, l_b_cdm2: float) -> float:
    """C_eff = C_measured * L_b / (L_b + L_v) -- the direct first-principles
    form of the same identity (Weber contrast of (L_obj+L_v) vs (L_bg+L_v)
    collapses to this), used as an independent cross-check of
    `veiled_contrast` (EM's Phase-2 algebraic re-derivation, Iteration 24)."""
    return c_measured * l_b_cdm2 / (l_b_cdm2 + l_v_cdm2)


def stray_light_ceiling_lux(candela: float, f_spill: float, r_hold_m: float) -> float:
    """E = f_spill * I / r_hold^2 (inverse-square, near-eye spill estimate,
    NEW this cycle -- f_spill and r_hold are uncited anthropometric/
    lighting-engineering estimates, this proposal's single largest
    evidentiary gap, per VISION's own Phase-1 disclosure)."""
    if r_hold_m <= 0:
        raise ValueError(f"r_hold_m must be > 0, got {r_hold_m}")
    return f_spill * candela / (r_hold_m ** 2)


def corneal_irradiance_wcm2(e_lux: float, efficacy_lm_per_w: float) -> float:
    """Unit-conversion only (Red Team fix 5): near-eye illuminance
    (lx = lm/m^2) -> irradiance at the cornea (W/cm^2), via the same
    luminous-efficacy constant docket #7's witness table already uses
    (exp-043, 300 lm/W, uncited). SINGLE-PASS instantaneous figure only --
    session-accumulated dose over multiple sweep passes is explicitly NOT
    computed here, flagged as open (Red Team fix 5)."""
    if efficacy_lm_per_w <= 0:
        raise ValueError(f"efficacy_lm_per_w must be > 0, got {efficacy_lm_per_w}")
    w_per_m2 = e_lux / efficacy_lm_per_w
    return w_per_m2 / 1.0e4


def tier_w_verdict(c_measured: float, l_v_cdm2: float, l_b_cdm2: float,
                    p: float, bar: str = "lab") -> dict:
    """One scored point: composes veiled_contrast + c_thr and classifies
    PASS / MARGINAL / FAIL against the (bar-explicit, fix-4) threshold.
    MARGINAL band: within a factor of 2 either side of the bar (a stated,
    round convention -- not itself sourced)."""
    l_eq = veiled_adapting_luminance(l_b_cdm2, l_v_cdm2)
    c_eff = veiled_contrast(c_measured, l_v_cdm2, l_b_cdm2)
    thr = c_thr(l_eq, p, bar=bar)
    ratio = abs(c_eff) / thr
    if ratio < 0.5:
        cls = "PASS"
    elif ratio <= 2.0:
        cls = "MARGINAL"
    else:
        cls = "FAIL"
    return {
        "l_b_cdm2": l_b_cdm2,
        "l_v_cdm2": l_v_cdm2,
        "l_eq_cdm2": l_eq,
        "p": p,
        "bar": bar,
        "c_eff": c_eff,
        "c_thr": thr,
        "abs_c_eff_over_thr": ratio,
        "classification": cls,
    }
