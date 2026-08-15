"""exp-033 design constants -- The g600 Resolution Check (Block A only).
=========================================================================
Panel Iteration 10 (lead: ELECTROMAGNETISM, rotation). Phase-3 synthesis
incorporates Red Team's PROCEED-WITH-MANDATORY-FIXES verdict in full --
see NOTES.md for the complete accepted/overridden record and LOGBOOK.md
Iteration 10 for the verbatim Phase 1/2/3 transcript.

SCOPE CHANGE FROM PHASE 1: Block B (radial_absorbed_power on beam-scene
off_pass/off_bracket) is CUT this cycle, per Red Team's own explicit
sanctioned fallback ("cut Block B entirely and re-scope it as a standalone
cycle. Do not run it as proposed.") -- PHOTONICS' attack (structurally
underpowered by 2-3 orders of magnitude, and P-EM-7's discriminator is
sign-degenerate between bulk and rim absorption) was independently
confirmed by Red Team's own direct computation. Re-queued for a future
standalone lead cycle, not smuggled in here as an unreviewed bolt-on.

Ambient geometry is exp-032's own +-35deg fallback bench, RESCALED x1.5
(cpl 20->30) per exp-025's own scaling idiom -- every cell constant
independently rounded, physical size held fixed. Verified self-similar
by both PHOTONICS and Red Team (fringe zone, windows, post-ramp settling
periods all scale; STEPS 1400->2100 holds post-ramp periods at 49,
identical to native -- this is also T10's own settling-confound fix,
which exp-025's own R3 check on this bench did NOT apply).

MANDATORY FIXES applied here (Red Team, Panel Iteration 10 Phase 2):
  1. [attack 1, LOAD-BEARING] SIGMA is pinned as an explicit number per
     article below, with a runtime assert (see run.py) holding
     tau_center = 2*sigma*r_out exactly -- this is exp-027's own T10
     SIGMA_ON bug (a rescaled-geometry material constant computed
     downstream, silently drifting tau), reproduced by this cycle's own
     Phase-1 proposal and caught by no blind seat, only Red Team. A
     silent tau drift here would spuriously fire the artifact verdict
     (P-EM-2) and retroactively kill every g600 citation on a bookkeeping
     error indistinguishable from the verdict it triggers.
  2. [attack 5] DECISION_FLOOR corrected to the EQUAL-weighted column.
     exp-024's originally committed table silently MIXED weighting
     conventions (450nm equal-weighted, 600/750nm cos-weighted) while
     every scoring run since (exp-026/030/032) uses equal weights
     ([1.0]*9). This is the entire explanation for VISION's "unexplained
     ~2x drift" in the 600nm floor (0.00007 committed / 3.3166e-5
     measured = 2.11, exactly the equal-vs-cos ratio) -- there was no
     drift, no reproducibility failure. Corrected below; erratum owed to
     LOGBOOK T7 and Iteration 9's carried-forward questions.
  3. [attack 3] off_field (tau=0.032, exp-026's third endpoint) ADDED to
     this cycle's article set -- the excluded 4th point cost the fit its
     only degree of freedom (3 points/3 free params = exactly determined,
     no residual diagnostic possible).
  4. [attack 9, MATERIALS] eps_r == 1.0 idealization is LOAD-BEARING, not
     a background note -- stated explicitly here and in NOTES.md
     Idealizations, with numbers: a realizable condensed-phase host
     (n=1.33-1.5) gives two-surface ambient contrast C = -0.040 to -0.078
     (a VISION-ladder FAIL by 2-4x, 9-17x the entire off_pass signal) and
     specular return 143-571x the established camera floor (constraint-2
     violation). g0 below is a constant of a gas/aerosol-host article
     (n-1 <~ 1e-5) ONLY, never a material transfer function.

See NOTES.md for the g0 refit banding (attacks 2/4/6), the retired
QUANTUM disposition clause and its numeric successor (attack 14), and the
scoring-currency declaration (attack 13, VISION's P-VIS-0(i)).
"""

import math

# --------------------------------------------------- ambient geometry (fallback, x1.5 rescaled)
RATIO = 1.5
CPL_NATIVE = 20
CPL = 30                      # the R3 check: cpl 20 -> 30 at 600nm only
NX = 540
NY = 2376
ABSORB = 60
SRC_X = 450
TAPER = 60
R_OUT = 117                   # 78 * 1.5, independently rounded
OBJ_X = 255
PLANE_DX = 22
PLANE_X = OBJ_X - R_OUT - PLANE_DX           # = 116
OBJ = (OBJ_X, 1188)                          # NY//2 = 1188
FALLBACK_ANGLES = (-35, -25, -15, -5, 0, 5, 15, 25, 35)   # N=9, unchanged

W_OBJ = 117
GUARD_OUT = 278
W_FLANK = 117
FLANK = (GUARD_OUT, GUARD_OUT + W_FLANK)     # (278, 395)

BOX_CLEARANCE = 18                            # 12 * 1.5
BOX = (OBJ_X - R_OUT - BOX_CLEARANCE, OBJ_X + R_OUT + BOX_CLEARANCE,
       OBJ[1] - R_OUT - BOX_CLEARANCE, OBJ[1] + R_OUT + BOX_CLEARANCE)
       # (120, 390, 1053, 1323)

STEPS_AMBIENT = 2100           # 1400 * 1.5 -- fixes T10's settling confound
                               # (exp-025's own R3 held steps fixed; this
                               # cycle's own settling control, below, checks it)
STEPS_SETTLING_CONTROL = 1400  # native step count, rerun at this geometry
                               # for the settling-control pair (empty, off_pass @ theta=0)

# ---------------------- mandatory fix 2: corrected decision floor (equal-weighted) ----------------------
# exp-024's ORIGINAL committed table mixed weighting conventions; VALUES BELOW
# are the equal-weighted column (matches weights=[1.0]*9, used by every scoring
# run since exp-026). Erratum: LOGBOOK T7 / Iteration 9 carried-forward Qs.
DECISION_FLOOR_NATIVE_CPL20 = {450: 8.8921e-4, 600: 3.3166e-5, 750: 4.3161e-4}
# ORIGINAL (WRONG, mixed-weighting) table, kept for the erratum record only --
# NOT used for scoring: {450: 0.00089, 600: 0.00007, 750: 0.00045}

# ---------------------- mandatory fix 1: sigma pinned as numbers, per article ----------------------
# sigma_engine = tau_center / (2 * R_OUT); uniform disk, eps_r=1 (mandatory
# fix 4 -- LOAD-BEARING idealization, see module docstring), no PEC core.
TAU_OFF_BRACKET = 0.003
TAU_OFF_PASS = 0.0065
TAU_OFF_LAB = 0.008
TAU_OFF_FIELD = 0.032          # mandatory fix 3 -- restored 4th endpoint

SIGMA_OFF_BRACKET = TAU_OFF_BRACKET / (2 * R_OUT)   # 1.2820512821e-05
SIGMA_OFF_PASS = TAU_OFF_PASS / (2 * R_OUT)         # 2.7777777778e-05
SIGMA_OFF_LAB = TAU_OFF_LAB / (2 * R_OUT)           # 3.4188034188e-05
SIGMA_OFF_FIELD = TAU_OFF_FIELD / (2 * R_OUT)       # 1.3675213675e-04

ARTICLES = ("off_bracket", "off_pass", "off_lab", "off_field")
TAU_BY_ARTICLE = {"off_bracket": TAU_OFF_BRACKET, "off_pass": TAU_OFF_PASS,
                  "off_lab": TAU_OFF_LAB, "off_field": TAU_OFF_FIELD}
SIGMA_BY_ARTICLE = {"off_bracket": SIGMA_OFF_BRACKET, "off_pass": SIGMA_OFF_PASS,
                    "off_lab": SIGMA_OFF_LAB, "off_field": SIGMA_OFF_FIELD}

for _art in ARTICLES:
    assert abs(2.0 * SIGMA_BY_ARTICLE[_art] * R_OUT - TAU_BY_ARTICLE[_art]) < 1e-9, \
        f"tau_center rescale failed for {_art} -- mandatory fix 1 (attack 1)"

# ---------------------- established anchors (native cpl=20, 600nm) ----------------------
# free-curvature-coefficient fit (QUANTUM/Red Team verified, Panel Iteration 10
# Phase 2): g_corr(tau) = A - B*tau, A=g0, B free (NOT the imposed 4/(3pi) --
# attack 16, g0 is a fitted bench-calibration constant, never a mechanism
# signature or a measured constant).
G0_ESTABLISHED_600_CPL20 = 0.689593
B_ESTABLISHED_600_CPL20 = 0.299943
CURVATURE_COEFF_IMPOSED = 4.0 / (3.0 * math.pi)     # 0.424413 -- reference only,
                                                     # REFUTED as the true coefficient
                                                     # by the free fit (B/A=0.435 != 0.424,
                                                     # 2.5%, 35x the fit's own residual --
                                                     # QUANTUM/Red Team attack 16)
G0_POOLED_12POINT = 0.688902     # all 3 lambda, native cpl, informational only

# ---------------------- mandatory fix 5/6: rebanded R3 disposition (Director, Phase 3) ----------------------
# Red Team attack 4: gate on the fit's own max residual FIRST (a 3100x-amplified
# floor-error detector, free from data the run already produces) -- only a
# residual-clean fit licenses any A-comparison verdict at all.
RESIDUAL_GATE_4ARTICLE = 3.0e-3     # g_corr units; Red Team's own verified number
                                    # for a floor error at P-EM-1's original band edge
# A-comparison bands (Director's reband, Red Team attack 6: "reband to what the
# design can deliver, or delete it" -- original +-5% band was unsatisfiable even
# at this bench's best-ever floor). Derived from attack 3's noise propagation
# (dA/d(delta_C) ~ 254 for the 4-article design) against the native floor order
# (~3e-5): expected achievable resolution in A is ~0.008-0.015 at good SNR.
A_CONFIRMED_BAND = 0.015     # |A_new - G0_ESTABLISHED_600_CPL20| <= this -> resolution-invariant
A_ARTIFACT_BAND = 0.035      # |A_new - G0_ESTABLISHED_600_CPL20| >= this -> artifact
                             # (between the two bands, or residual gate fails -> INCONCLUSIVE,
                             # a real, pre-registered outcome -- VISION's P-VIS-0(ii), Red Team attack 2)

# ---------------------- mandatory fix 4: eps_r=1 idealization, load-bearing numbers ----------------------
# Red Team attack 9, verified: two-surface Fresnel ambient contrast for a
# REALIZABLE condensed-phase host (n=1.33 water-like / n=1.50 glass-like),
# independent of tau -- exceeds the entire off_pass signal (0.0045) before
# tau enters the arithmetic, and independently FAILS constraint 2 (specular
# return 143-571x the camera floor).
EPS_R_IDEALIZATION_NOTE = (
    "g0 and every PASS in this line are properties of an index-matched "
    "(eps_r == 1.0, n-1 <~ 1e-5) article -- a gas/aerosol host only. At a "
    "realizable condensed-phase index (n=1.33-1.5): two-surface ambient "
    "contrast C = -0.040 to -0.078 (VISION-ladder FAIL, 9-17x the off_pass "
    "signal), specular return 143-571x the established camera floor "
    "(constraint-2 violation). NOT a material transfer function."
)

if __name__ == "__main__":
    print("exp-033 geometry (Block A only -- Block B cut this cycle, see NOTES.md):")
    print(f"  ambient x{RATIO}: {NX}x{NY}, OBJ={OBJ}, PLANE_X={PLANE_X}, BOX={BOX}")
    print(f"  angles: {FALLBACK_ANGLES}")
    print(f"  decision floor (corrected, equal-weighted): {DECISION_FLOOR_NATIVE_CPL20}")
    print("\nsigma(I) OFF-state articles (mandatory fix 1 -- sigma pinned + asserted):")
    for name in ARTICLES:
        print(f"  {name:12s} tau_center={TAU_BY_ARTICLE[name]:7.4f}  "
              f"sigma_engine={SIGMA_BY_ARTICLE[name]:.10e}")
    print(f"\nestablished 600nm/cpl20 fit: A(g0)={G0_ESTABLISHED_600_CPL20} B={B_ESTABLISHED_600_CPL20}")
    print(f"reband: CONFIRMED |dA|<={A_CONFIRMED_BAND}  ARTIFACT |dA|>={A_ARTIFACT_BAND}  "
          f"else INCONCLUSIVE; residual gate <= {RESIDUAL_GATE_4ARTICLE}")
