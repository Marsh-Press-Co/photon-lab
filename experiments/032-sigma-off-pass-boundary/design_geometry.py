"""exp-032 design constants -- The sigma(I) OFF-State PASS-Boundary Run.
=========================================================================
Panel Iteration 9 (lead: MATERIALS, per rotation; content dictated by
Iteration 8's binding, three-times-deferred priority -- see NOTES.md for
the full Phase 1/2/3 accepted/overridden record and LOGBOOK.md Iteration 9
for the verbatim transcript).

Ambient geometry is INHERITED VERBATIM from exp-026's own +-35deg fallback
bench (itself inherited from exp-024's MARGIN_MULT=3.5 result) -- zero
geometry changes proposed or made here. Constants below are copied from
experiments/026-sigma-i-endpoints/design_geometry.py rather than
cross-imported, per this lab's own stated convention for simple constant
blocks (exp-025/026 did the same) -- each experiment directory stays
self-contained.

New in this experiment: two uniform-conductivity sigma(I)-OFF-state
articles, both weaker (lower tau_center) than exp-026's own off_lab
(tau=0.008), the weakest sigma(I) article ever built on this bench:

  - off_pass  (tau_center=0.0065): the headline PASS-boundary probe.
    Predicted (established off_lab g-transfer, g in [0.50,0.80]) to be
    the first sigma(I) OFF-state configuration in this program's history
    to clear VISION's frozen lab bar (|C|<0.005) at all three lambda.
  - off_bracket (tau_center=0.003): Red Team's mandatory Phase-2 fix
    (EM's own proposed bracket point, corrected from PHOTONICS' mislabeled
    tau=0.012 suggestion, which sits ABOVE the already-validated tau=0.008
    floor and so cannot bracket an extrapolation that only begins below
    it). Discriminates two live hypotheses for exp-026's own unexplained
    g600 anomaly: bulk-absorption-dominated (g stays flat as tau shrinks
    further) vs edge/rim-scattering-floor-dominated (g rises as tau -> 0,
    per T9's rim-transmission mechanism). Pre-registered SNR risk: the
    450nm channel at this tau sits at SNR~1.9 against the reused decision
    floor -- thinner than any channel this program has ever scored,
    informational-only at that one wavelength, not a scored gate.

No PEC core, ε_r=1.0 (background untouched -- no index step, only a
conductivity step) -- identical idiom to exp-026's off_lab/off_field.
"""

import numpy as np

# --------------------------------------------------- ambient geometry (fallback)
NX = 360
NY = 1584                    # exp-024's MARGIN_MULT=3.5 result, reused unchanged
ABSORB = 40
CPL = {450: 15, 600: 20, 750: 25}
SRC_X = 300
TAPER = 40
R_OUT = 78                   # 2.34 um at Delta=30nm -- all calibration articles
OBJ_X = 170
PLANE_DX = 15
PLANE_X = OBJ_X - R_OUT - PLANE_DX          # = 77
OBJ = (OBJ_X, NY // 2)                      # (170, 792)
SRC_Y = (ABSORB, NY - ABSORB)
FALLBACK_ANGLES = (-35, -25, -15, -5, 0, 5, 15, 25, 35)   # N=9, exp-024's pre-committed fallback
N5_SUBSAMPLE = (-35, -15, 0, 15, 35)        # 5 of the 9 fallback angles -- ZERO new runs, inherited idiom

W_OBJ = 78
GUARD_OUT = 185
W_FLANK = 78
FLANK = (GUARD_OUT, GUARD_OUT + W_FLANK)    # (185, 263)

BOX_CLEARANCE = 12
BOX = (OBJ_X - R_OUT - BOX_CLEARANCE, OBJ_X + R_OUT + BOX_CLEARANCE,
       OBJ[1] - R_OUT - BOX_CLEARANCE, OBJ[1] + R_OUT + BOX_CLEARANCE)

# established decision floor at this exact geometry (exp-024/025, REUSED not
# remeasured): delta_C = 0.00089 / 0.00007 / 0.00045 @ 450/600/750nm.
DECISION_FLOOR = {450: 0.00089, 600: 0.00007, 750: 0.00045}

# --------------------------------------------------- sigma(I) OFF-state articles
# sigma_engine = tau_center / (2 * R_OUT); uniform disk, eps_r=1 (background,
# untouched -- no index step, only a conductivity step), no PEC core. Same
# construction as exp-026's off_lab/off_field.
TAU_OFF_PASS = 0.0065        # the headline PASS-boundary probe
TAU_OFF_BRACKET = 0.003      # Red Team's mandatory below-tau_off bracket point

SIGMA_OFF_PASS = TAU_OFF_PASS / (2 * R_OUT)        # 4.16667e-5
SIGMA_OFF_BRACKET = TAU_OFF_BRACKET / (2 * R_OUT)  # 1.92308e-5

ARTICLES_AMBIENT = ("off_pass", "off_bracket")
SIGMA_BY_ARTICLE = {"off_pass": SIGMA_OFF_PASS, "off_bracket": SIGMA_OFF_BRACKET}
TAU_BY_ARTICLE = {"off_pass": TAU_OFF_PASS, "off_bracket": TAU_OFF_BRACKET}

# reused, not rerun -- exp-026's own established off_lab anchor (results.json,
# commit for exp-026's results), tau=0.008, N=9 fallback, all 3 lambda.
# Printed here as documentation only -- the run itself does not depend on it.
OFF_LAB_C_ESTABLISHED = {450: -0.00460711308931395, 600: -0.005530667330154762,
                          750: -0.005052707590063023}
OFF_LAB_G_ESTABLISHED = {450: 0.5758891361642438, 600: 0.6913334162693453,
                          750: 0.6315884487578778}
TAU_OFF_LAB_ESTABLISHED = 0.008

# g-transfer band, HARMONIZED per Red Team's Phase-2 audit (attack #2: the
# Phase-1 proposal's P-MAT-1 C-band and P-MAT-2 g-band did not share one
# model). Single band used for BOTH predicted-C and predicted-g dispositions
# below: g in [0.50, 0.80].
G_BAND = (0.50, 0.80)

# ON-article anchor, reused for THERMODYNAMICS' mandatory energy sidecar
# (Red Team's fix #3 -- the sentence must show its arithmetic, not just
# assert "negligible"). exp-026 established range across 3 lambda.
ESTABLISHED_ABS_EXT_RATIO_ON = (0.6056, 0.6083)   # sigma_abs/sigma_ext, ON article (tau=3.9)
TAU_ON_ESTABLISHED = 3.9


if __name__ == "__main__":
    print("exp-032 geometry (inherited verbatim from exp-026's +-35deg fallback):")
    print(f"  ambient: {NX}x{NY}, OBJ={OBJ}, PLANE_X={PLANE_X}, BOX={BOX}")
    print(f"  angles: {FALLBACK_ANGLES}  (N5 subsample: {N5_SUBSAMPLE})")
    print(f"  decision floor (reused): {DECISION_FLOOR}")
    print("\nsigma(I) OFF-state articles:")
    for name, tau, sig in (("off_pass", TAU_OFF_PASS, SIGMA_OFF_PASS),
                           ("off_bracket", TAU_OFF_BRACKET, SIGMA_OFF_BRACKET)):
        print(f"  {name:12s} tau_center={tau:7.4f}  sigma_engine={sig:.5e}")
    print("\npredicted C bands (g in [0.50,0.80], per-lambda, harmonized):")
    for name, tau in (("off_pass", TAU_OFF_PASS), ("off_bracket", TAU_OFF_BRACKET)):
        lo, hi = G_BAND[0] * tau, G_BAND[1] * tau
        print(f"  {name:12s} tau={tau:7.4f}  C in [{lo:.5f}, {hi:.5f}]  "
              f"(central, established-g carried down: "
              f"{ {k: round(v * tau, 5) for k, v in OFF_LAB_G_ESTABLISHED.items()} })")
    print("\npredicted SNR = |C_central| / decision_floor, off_pass (established-g central):")
    for lam, floor in DECISION_FLOOR.items():
        c = OFF_LAB_G_ESTABLISHED[lam] * TAU_OFF_PASS
        print(f"  {lam}nm: C={c:.5f}  floor={floor:.5f}  SNR={c / floor:.2f}")
    print("\npredicted SNR = |C_central| / decision_floor, off_bracket (established-g central):")
    for lam, floor in DECISION_FLOOR.items():
        c = OFF_LAB_G_ESTABLISHED[lam] * TAU_OFF_BRACKET
        print(f"  {lam}nm: C={c:.5f}  floor={floor:.5f}  SNR={c / floor:.2f}")
