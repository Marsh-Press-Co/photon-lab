"""exp-056 design constants -- The T26 Near-Null Generalization Test.
=========================================================================
Panel Iteration 33 (lead: VISION SCIENCE, rotation). Phase-3 synthesis
incorporates Red Team's PROCEED-WITH-MANDATORY-FIXES verdict (docket
items 1,2,4,5,6,7) -- see NOTES.md for the complete accepted/overridden
record and LOGBOOK.md Iteration 33 for the verbatim Phase 1/2/3 transcript.

T26 (opened Iteration 32, exp-055): fixed-zero-relative-phase N=9 coherent
joint injection produces a large EMPTY-scene artifact (C_empty_joint =
-0.05343, >10x VISION's own T2 photopic C_thr=0.005) that was small on the
one loaded article tested (the deep-shadow PEC-cored absorber, |dC|=0.32%
absolute). This cycle asks whether that suppression generalizes to a
near-null sigma(I) OFF-state article -- the regime where the artifact
could actually flip a live PASS/MARGINAL verdict -- using off_pass/
off_bracket (exp-032/033's own construction, geometry byte-identical to
exp-024/055's native r=78 bench, confirmed by a bit-identical C_empty
match: -3.316590819191224e-05 in both exp-032 and exp-055).

DIRECTOR'S PHASE-3 CORRECTION to Red Team's mandatory-fix docket item 3
(PHOTONICS' "phantom disk" control, sigma=0/eps_r=1, r=78): as specified,
sigma=0 is a no-op on sim.sigma_e and eps_r=1 matches the ambient
background exactly -- this "phantom" scene is PHYSICALLY IDENTICAL to the
vacuum/empty scene already measured at this exact native geometry
(exp-055's own C_empty_joint=-0.05343). Running it would be a wasted FDTD
call reproducing an existing number to machine precision. The scientific
intent (an edge/geometry-vs-tau discriminator) is instead satisfied at
ZERO additional cost: the existing empty_joint measurement IS the tau=0
point on the same suppression-vs-tau curve as off_bracket (tau=0.003) and
off_pass (tau=0.0065) -- a genuine 3-point curve, for free. See NOTES.md
Phase 3 for the full disclosure of this partial override.

3 NEW FDTD calls only (matching the Phase-1 proposal's own original
count): off_pass_joint, off_bracket_joint (native r=78, cpl=20, N=9
simultaneous, fixed zero relative phase) + empty_joint_cpl30 (rescaled
r=117, cpl=30, R3 check on the empty-scene artifact itself, never
previously run -- T26 gap 2).
"""

import numpy as np

# =========================================================== NATIVE (r=78)
# exp-024/032/055's own fallback geometry, reused verbatim.
NX = 360
NY = 1584
ABSORB = 40
SRC_X = 300
TAPER = 40
R_OUT = 78
OBJ_X = 170
PLANE_DX_NATIVE = 15
PLANE_X = OBJ_X - R_OUT - PLANE_DX_NATIVE      # 77
OBJ = (OBJ_X, NY // 2)                          # (170, 792)
FALLBACK_ANGLES = (-35, -25, -15, -5, 0, 5, 15, 25, 35)   # N=9

W_OBJ = 78
GUARD_OUT = 185
W_FLANK = 78

CPL = 20
LAM_NM = 600
COURANT_FRAC = 0.99
STEPS = 1400

# window-position sensitivity offsets (fix, "not mandatory, recommended" --
# symmetrized around the primary dx=15 per Red Team's Phase-2 note)
PLANE_DX_SENS_NATIVE = (13, 15, 17)

# ---------------------------------------------- sigma(I) OFF-state articles
# exp-032/033's own construction: uniform disk, no PEC core, eps_r=1.0,
# sigma_engine = tau_center / (2*R_OUT).
TAU_OFF_PASS = 0.0065
TAU_OFF_BRACKET = 0.003
SIGMA_OFF_PASS = TAU_OFF_PASS / (2 * R_OUT)        # 4.166666...e-5
SIGMA_OFF_BRACKET = TAU_OFF_BRACKET / (2 * R_OUT)  # 1.923076...e-5
assert abs(SIGMA_OFF_PASS - 4.16667e-5) < 1e-9
assert abs(SIGMA_OFF_BRACKET - 1.92308e-5) < 1e-9

ARTICLES = ("off_pass", "off_bracket")
SIGMA_BY_ARTICLE = {"off_pass": SIGMA_OFF_PASS, "off_bracket": SIGMA_OFF_BRACKET}
TAU_BY_ARTICLE = {"off_pass": TAU_OFF_PASS, "off_bracket": TAU_OFF_BRACKET}

# --------------------------------------- established anchors (exp-032, ZERO new FDTD)
C_NAIVE_ESTABLISHED = {
    "off_pass": -0.004502830238451187,
    "off_bracket": -0.0020992636423987046,
}
C_EMPTY_NAIVE_NATIVE_ESTABLISHED = -3.316590819191224e-05   # exp-032 == exp-055, bit-identical
C_EMPTY_JOINT_NATIVE_ESTABLISHED = -0.0534252451544586       # exp-055 -- ALSO the tau=0 "phantom"
                                                               # point, see module docstring
EMPTY_JOINT_FLANK_RAW_NATIVE_ESTABLISHED = 2.8615137799931016  # exp-055 results.json,
                                                                 # joint_coherent.empty_joint_flank_raw
                                                                 # -- EM's mandatory-fix-1 comparator:
                                                                 # same injection modality (coherent
                                                                 # N=9), same geometry, so "did loading
                                                                 # the object collapse the flank window"
                                                                 # is answered directly, not by proxy.
DEEP_SHADOW_COMPARATOR_DC_ABS = 0.003168   # exp-055's own PEC-cored absorber, |dC| abs

# =========================================================== RESCALED (r=117, R3 check)
# exp-033's own x1.5 rescale of the identical physical scene, verbatim.
RATIO = 1.5
NX_R = 540
NY_R = 2376
ABSORB_R = 60
SRC_X_R = 450
TAPER_R = 60
R_OUT_R = 117
OBJ_X_R = 255
PLANE_DX_R = 22
PLANE_X_R = OBJ_X_R - R_OUT_R - PLANE_DX_R     # 116
OBJ_R = (OBJ_X_R, NY_R // 2)                    # (255, 1188)

W_OBJ_R = 117
GUARD_OUT_R = 278
W_FLANK_R = 117

CPL_R = 30
COURANT_FRAC_R = 0.99
STEPS_R = 2100

PLANE_DX_SENS_R = (20, 22, 24)   # symmetrized rescaled offsets (Red Team's own recommendation)

# established rescaled empty-scene naive anchor (exp-033, ZERO new FDTD).
# CORRECTED SIGN (Red Team docket item 5 / PHOTONICS' catch): the Phase-1
# proposal cited "+1.1648e-4" -- the true value in exp-033's own
# results.json (ambient_contrasts.*.C_empty) is NEGATIVE, matching the
# native-scale sign. The "+1.1648e-4" figure IS in exp-033's results.json,
# but under a differently-named, deliberately-positive-magnitude field
# (`fresh_empty_decision_floor_600_cpl30`, a floor convention) -- not the
# signed Weber C. Verified directly against experiments/033-.../results.json.
C_EMPTY_NAIVE_RESCALED_ESTABLISHED = -0.00011647923213709
