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
    "source": (
        "Iteration 7 (exp-030) Phase 5 -- MATERIALS' own Phase-2 review first "
        "proposed this figure but stated it wrong (a unit-misread, "
        "'~0.62-1.85m'); RED TEAM's Phase-5 audit caught and corrected it to "
        "the 0.31-0.92m value used here (Iteration-24 Phase-5, MATERIALS'/"
        "Red Team's own re-audit, provenance-corrected)."
    ),
    "construction_note": (
        "C_MEASURED (this module) is drawn from the SELF-SIMILAR-SCALED "
        "graded_black_shell construction (r_in/r_out both scale together) -- "
        "the exact construction this realizability figure already names "
        "UNOBTANIUM at witness scale (real ultra-black coatings scale by "
        "FIXED ABSOLUTE thickness, the opposite law). A fixed-absolute-"
        "thickness variant has been proposed (Iteration 7) but never built "
        "or measured, at any scale, as of Iteration 24 (Iteration-24 Phase-5, "
        "MATERIALS' major finding)."
    ),
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
    (T18 blocked); flagged, not silently assumed valid outside that range.
    Callers may evaluate outside it (both directions are un-enforced, not
    silently safe): the "fixed-gaze" scenario's own LARGE-theta excursions
    are stated idealizations (Iteration 24 Phase 1); its own SMALL-theta
    end (P-G24-4 evaluates theta=0.5deg, below the 1.0deg floor) was an
    undisclosed gap until Red Team's Iteration-24 Phase-5 audit caught it
    -- physically the more dangerous direction, since L_v diverges as
    theta->0 and the point-source assumption is weakest exactly there.

    ACHROMATICITY NOTE (Red Team's Iteration-24 Phase-5 audit, elevating
    PHOTONICS' finding): E here is treated as a flat photometric quantity
    with no spectral term -- a SECOND, separate achromaticity assumption
    from C_MEASURED's own V-weighting (this program has caught this exact
    "achromatic by construction" overclaim pattern before, Iteration 20/
    exp-043 Phase 5). Intraocular forward light scatter (the physical
    mechanism behind veiling glare) is itself known to be wavelength-
    dependent; not modeled here."""
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
    against `veiled_contrast_direct` (trust-suite stage 17).

    EXTRAPOLATION-RANGE CAVEAT (EM's Iteration-24 Phase-5 finding): the
    headline grid's own L_v/L_B ratio spans ~2.5e4x to ~2.2e9x -- the
    Stiles-Holladay/CIE-family literature this relation is drawn from is
    calibrated against road-lighting/automotive glare scenarios, where
    glare-to-background ratios are typically small integers to low
    hundreds, not 1e4-1e9. The formula's asymptotic washout (C_eff->0 as
    L_v->infinity) is physically sound regardless (verified: this cannot
    reverse sign or vanish, so it cannot flip a PASS to FAIL) -- but a
    reported "robust margin" at these ratios is substantially a statement
    about extrapolating this linear model far past its empirical support,
    not fresh confirmation of the underlying physical claim. Not
    independently re-verified via WebFetch this cycle (T18 blocked)."""
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
    computed here, flagged as open (Red Team fix 5).

    SCALE ANCHOR (THERMO's Iteration-24 Phase-5 finding, added same-shift):
    for comparison, terrestrial solar irradiance is ~100 mW/cm^2 broadband
    -- this module's ceiling-extreme figure (~18.4 mW/cm^2) is ~18% of
    that, for a single-pass, worst-case-STACKED (max spill fraction x min
    hold distance x max candela -- these do not co-occur by default)
    near-field SPILL component, not direct beam viewing.

    NOT A HAZARD ASSESSMENT: corneal irradiance ALONE does not establish
    retinal hazard -- that depends on the source's angular subtense/
    radiance (a diffuse spill source and a quasi-point source at the same
    corneal irradiance are different hazard classes), which this function
    does not model. No ANSI/IEC-class exposure-limit comparison is made
    or implied anywhere in this module."""
    if efficacy_lm_per_w <= 0:
        raise ValueError(f"efficacy_lm_per_w must be > 0, got {efficacy_lm_per_w}")
    w_per_m2 = e_lux / efficacy_lm_per_w
    return w_per_m2 / 1.0e4


def tier_w_verdict(c_measured: float, l_v_cdm2: float, l_b_cdm2: float,
                    p: float, bar: str = "lab") -> dict:
    """One scored point: composes veiled_contrast + c_thr and classifies
    PASS / MARGINAL / FAIL against the (bar-explicit, fix-4) threshold.
    MARGINAL band: within a factor of 2 either side of the bar.

    SOURCED (panel Iteration 25, exp-048, Block C): the x2/x0.5 band
    matches T2's own committed vertical-log uncertainty on C_thr(L) itself
    (+-0.3 log -- LOGBOOK.md, "Scotopic scaling" section) to 0.24%
    (10^0.3=1.99526, 10^-0.3=0.50119) -- a distinct axis from the
    separately-gridded p in {0.4,0.5} exponent family, not a restatement
    of it. Regime-checked, not just numerically matched: exp-047's own
    three near-boundary points (L_eq=1e-5/1.7e-4/1.17e-3 cd/m^2) all sit
    well below L_REF=3.0 -- the low-luminance regime this +-0.3-log figure
    is committed for, not the clamped photopic floor. Applicability
    CONFIRMED for the points that currently matter; NOT independently
    verified for any future near-boundary point at L_eq>=L_REF, where
    c_thr is pinned at its floor and this figure's own status is
    unaddressed."""
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
