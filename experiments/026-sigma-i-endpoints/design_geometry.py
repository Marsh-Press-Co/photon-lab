"""exp-026 design constants -- the sigma(I) Endpoint Triplet.
=================================================================
Panel Iteration 3 (lead: MATERIALS). Geometry is INHERITED VERBATIM from
exp-024's pre-committed +-35deg fallback (the standing near-threshold-
scoring baseline per Iteration 2's close, ruled explicitly, not an implicit
carryover) -- zero geometry changes proposed or made here. Constants below
are copied from experiments/024-ambient-margin-adjudication/design_geometry.py
(NY=1584 branch) rather than cross-imported, per this lab's own convention
(each experiment directory is self-contained -- exp-025 did the same).

New in this experiment: three uniform-conductivity sigma(I)-endpoint
articles (OFF-lab / OFF-field / ON), plus the exp-001/002 beam-scene
geometry (unchanged) used for the ON article's beam-behind / observer-
return / box-ledger channels.
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
N5_SUBSAMPLE = (-35, -15, 0, 15, 35)        # P-MAT7: 5 of the 9 fallback angles -- ZERO new runs

W_OBJ = 78
GUARD_OUT = 185
W_FLANK = 78
FLANK = (GUARD_OUT, GUARD_OUT + W_FLANK)    # (185, 263)

BOX_CLEARANCE = 12
BOX = (OBJ_X - R_OUT - BOX_CLEARANCE, OBJ_X + R_OUT + BOX_CLEARANCE,
       OBJ[1] - R_OUT - BOX_CLEARANCE, OBJ[1] + R_OUT + BOX_CLEARANCE)

# established decision floor at this exact geometry (exp-024/025, REUSED not
# remeasured): delta_C = 0.00089 / ~0.00005-0.00007 / 0.00043-0.00045 @
# 450/600/750nm -- SNR against P-MAT1's loose-edge central (-0.0035) is
# >= 4.7x even at 450nm, the worst wavelength.
DECISION_FLOOR = {450: 0.00089, 600: 0.00007, 750: 0.00045}

# --------------------------------------------------- sigma(I) endpoint articles
# sigma_engine = tau_center / (2 * R_OUT); uniform disk, eps_r=1 (background,
# untouched -- no index step, only a conductivity step), no PEC core. Same
# construction as exp-024's run.py "sponge" branch, three new tau values.
TAU_OFF_LAB = 0.008
TAU_OFF_FIELD = 0.032
TAU_ON = 3.9
TAU_TIE = 0.10                              # exp-024's own calibration point, REUSED not rerun

SIGMA_OFF_LAB = TAU_OFF_LAB / (2 * R_OUT)     # 5.1282e-5
SIGMA_OFF_FIELD = TAU_OFF_FIELD / (2 * R_OUT)  # 2.0513e-4
SIGMA_ON = TAU_ON / (2 * R_OUT)               # 2.5000e-2

ARTICLES_AMBIENT = ("off_lab", "off_field", "on")
SIGMA_BY_ARTICLE = {"off_lab": SIGMA_OFF_LAB, "off_field": SIGMA_OFF_FIELD,
                    "on": SIGMA_ON}

# reused, not rerun -- exp-024 fallback commit c67506b (empty + tau=0.10 sponge,
# all 3 lambda, N=9 fallback angles). Printed here as documentation only.
REUSED_TAU010_C_FALLBACK = {450: -0.0651, 600: -0.0661, 750: -0.0654}

# --------------------------------------------------- beam-scene geometry (ON only)
# Unchanged from exp-001/exp-002 -- same R_OUT=78 (their R_COAT), same domain,
# same courant fraction, for direct comparability with the established
# camera-floor (0.00007-0.00014) and Q_ext=0.51 (graded_black_shell)
# baselines this experiment's predictions are anchored against.
BEAM_N = 560
BEAM_ABSORB = 40
BEAM_FRAC = 0.32
BEAM_STEPS = 3200
BEAM_CX, BEAM_CY = 252, 280
BEAM_SRC_X, BEAM_OBS_X = 64, 78
BEAM_SWEEP = ((15, 450), (20, 600), (25, 750))
BEAM_BOX_A = (142, 362, 170, 390)            # exp-002's box pair, unchanged
BEAM_BOX_B = (117, 387, 145, 415)
BEAM_REF = (BEAM_CX, BEAM_CY, 60)
_bx = np.arange(BEAM_N)[:, None]
_by = np.arange(BEAM_N)[None, :]
_brr = np.hypot(_bx - BEAM_CX, _by - BEAM_CY)
BEAM_ANNULUS = (_brr >= R_OUT + 10) & (_brr <= R_OUT + 70)
BEAM_BEHIND = (slice(BEAM_CX + R_OUT + 15, BEAM_CX + R_OUT + 115),
              slice(BEAM_CY - 20, BEAM_CY + 20))

# established anchor this experiment's P-MAT8/P-MAT5 predictions are scored
# against (LOGBOOK ESTABLISHED section): graded_black_shell at this SAME
# R_OUT=78 measured sigma_abs/sigma_ext = 0.51 (the extinction-paradox
# saturation value for an optically-thick, near-zero-reflectivity absorber).
ESTABLISHED_ABS_EXT_RATIO = 0.51
ESTABLISHED_CAMERA_FLOOR = (0.00007, 0.00014)   # exp-001 post-phasor-fix, absolute


if __name__ == "__main__":
    print("exp-026 geometry (inherited verbatim from exp-024's +-35deg fallback):")
    print(f"  ambient: {NX}x{NY}, OBJ={OBJ}, PLANE_X={PLANE_X}, BOX={BOX}")
    print(f"  angles: {FALLBACK_ANGLES}  (N5 subsample: {N5_SUBSAMPLE})")
    print(f"  decision floor (reused): {DECISION_FLOOR}")
    print("\nsigma(I) endpoint articles:")
    for name, tau, sig in (("OFF-lab", TAU_OFF_LAB, SIGMA_OFF_LAB),
                           ("OFF-field", TAU_OFF_FIELD, SIGMA_OFF_FIELD),
                           ("ON", TAU_ON, SIGMA_ON)):
        atten_um = 1.0 / (sig) * 0.03 if sig > 0 else float("inf")  # ~ Delta/sigma, cells->um
        print(f"  {name:10s} tau_center={tau:6.3f}  sigma_engine={sig:.4e}")
    print(f"\nbeam-scene (exp-001/002 domain, unchanged): N={BEAM_N}, "
          f"CX,CY=({BEAM_CX},{BEAM_CY}), SRC_X={BEAM_SRC_X}, OBS_X={BEAM_OBS_X}")
    print(f"established anchors: graded_black_shell sigma_abs/sigma_ext = "
          f"{ESTABLISHED_ABS_EXT_RATIO}, camera floor = {ESTABLISHED_CAMERA_FLOOR}")
