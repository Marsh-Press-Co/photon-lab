"""exp-058 design constants -- QUANTUM OPTICS' phase-variance redesign.
=========================================================================
Panel Iteration 35 (lead: QUANTUM OPTICS, LOCKED, unconditional, breaking
rotation -- Red Team's Iteration-33 Phase-5 ruling, fired at Iteration
34's close per that ruling's own pre-registered condition). Phase-3
synthesis incorporates all five Phase-2 seats' fix requests (all returned
support-with-changes, zero opposes) plus Red Team's PROCEED-WITH-
MANDATORY-FIXES 5-item docket -- see NOTES.md for the complete
accepted/overridden record and LOGBOOK.md Iteration 35 for the verbatim
Phase 1/2/3 transcript.

T25 (opened Iteration 29, exp-052; sharpened Iteration 32/33, exp-055/056
-- T26): every constraint-3 `C` citation this program has issued rests on
lab/ambient.py's INCOHERENT sum -- 9 separate single-source runs combined
post-hoc as intensities. Iteration 6 proved analytically that the TRUE
random-phase incoherent-ensemble limit has exactly zero mean cross-term,
but T26 (exp-055/056) measured only ONE realization (fixed, all-zero
relative phase) of the actual coherent joint-injection instrument, and
found a large artifact. This cycle finally measures the VARIANCE across
real random-phase draws, on the two articles where it could actually flip
a live verdict: off_pass (tau=0.0065, this program's only-ever
constraint-3 PASS) and off_bracket (tau=0.003) -- exp-032/033/056's own
construction, native r=78 geometry, reused verbatim (byte-identical
confirmed against experiments/056-.../design_geometry.py).

New machinery, Panel-Iteration-35-built (see NOTES.md for the full
Phase-2/Red-Team record): `lab/fdtd2d.py`'s `Sim.add_line_source` gains a
`rel_phase` parameter (backward-compatible, default 0.0); `lab/
phase_lines.py` is a new, bespoke, non-artifact module persisting each
single-source leg's own Ez/Hy phasor on the ambient window's fixed
observation line, and reconstructing ANY relative-phase draw across the 9
angular components post-hoc via the derived (and independently
triple-re-derived: PHOTONICS, ELECTROMAGNETISM, Red Team) LTI law
F(delta) = F(0)*exp(+i*delta); trust-suite stage 20 gates both a
zero-phase (Q7) and a nonzero-phase (Q8) disk round trip on a small
canonical bench.

DIRECTOR'S OWN PHASE-3 CATCH, not raised by any Phase-2 seat or Red
Team (discovered by direct execution, this program's own established
"diagnose before trusting, disclose what's measured" discipline):
stage 20's canonical bench uses a STRONGLY lossy object
(graded_black_shell, sigma_max=0.5) -- material loss is what damps a
source's turn-on transient, and Q8's phase-rotation reconstruction is
exact only for the true periodic steady state, so any un-decayed
transient leaks into it (Q7's pure-additivity identity is unaffected
either way -- see run_all.py's stage20 docstring for the full
derivation). off_pass/off_bracket are almost UNDAMPED by comparison
(tau=0.0065/0.003 vs the bench's tau~effectively-total) -- direct
measurement (native geometry, STEPS=1400, one representative nonzero-
delta draw) found the SAME reconstruction technique's field-relative RMS
residual is ~100x larger here than on stage 20's own bench at the same
step count (1.06e-3 vs 1.45e-5), even though the resulting WEBER-C error
this induces is small in the units that matter (measured 1.24e-4 absolute
C-units for off_pass at that one draw, ~2.5% of C_thr=0.005 -- window-
averaging over 78-156 cells substantially, though not perfectly, damps
the field-level residual). Rather than bury this or brute-force ~40x more
FDTD steps (a multi-hour cost this cycle does not need), it is measured
directly, disclosed, and gated: exp-058 carries its OWN empirical
noise-floor validation leg per article (NOISE_FLOOR_SEED, below),
reusing the already-required 9 legs at zero-plus-one marginal FDTD cost,
scored against P-058-NF (see NOTES.md). New "Measurement lesson" line
added to VALIDATION.md at Phase 3 close.

Red Team's Iteration-35 Phase-2 docket, all five items applied (see
NOTES.md for the full text): (1) `_STAGE_IDS` bumped to cover stage 20
(lab/validation/run_all.py) -- the identical bug species this program has
hit three times before (Iterations 15, 17, 23), caught here BEFORE first
light, not after. (2) The Phase-2 docket is tiered explicitly below:
MANDATORY (EM's per-draw flank-denominator diagnostic; THERMODYNAMICS'
p_abs_naive anchor) vs RECOMMENDED (PHOTONICS' percentile-rank report;
MATERIALS' coherence-length citation; VISION's caveat-forward language).
(3) The flank_denominator threshold (<0.20) is disclosed below as reused
UNMODIFIED from its single-realization (exp-056) calibration, not
re-derived for the N=2000 ensemble. (4) Stage 20's object-loaded-branch-
only scope is stated explicitly in its own docstring (persistence
fidelity is scene-content-independent; the harder physics case subsumes
vacuum). (5) The `rel_phase`/lab.artifacts question is CLOSED, not open
-- confirmed harmless against `validate_groups`'s actual source-key
validation logic (only missing required keys are rejected, never unknown
extra ones).
"""

import numpy as np

# =========================================================== NATIVE (r=78)
# exp-024/032/055/056's own fallback geometry, reused verbatim.
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
STEPS = 1400   # exp-056's own established convention, reused unchanged
               # (Director's Phase-3 call: NOT increased despite the
               # settling finding above -- the measured noise floor is
               # small relative to C_thr and to the predicted C spread;
               # see NOTES.md P-058-NF and its disposition).

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
# Deterministic per-article RNG stream offset -- NOT Python's built-in
# hash() (randomized per-process via PYTHONHASHSEED unless fixed, which
# would silently break run-to-run reproducibility of the N_DRAWS/noise-
# floor draws; caught before first light).
ARTICLE_SEED_OFFSET = {"off_pass": 0, "off_bracket": 1}

# --------------------------------------- established anchors (ZERO new FDTD)
# exp-056's own native joint (N=9, fixed zero relative phase) C_joint --
# the target this cycle's own delta=0 reconstruction must reproduce.
C_JOINT_ESTABLISHED = {
    "off_pass": -0.058149,
    "off_bracket": -0.055609,
}
# exp-056's own naive-incoherent C (exp-032/033's construction) -- the
# INCOHERENT-SUM anchor this cycle's N=2000 empirical mean is read against.
C_NAIVE_ESTABLISHED = {
    "off_pass": -0.004502830238451187,
    "off_bracket": -0.0020992636423987046,
}
# exp-055's own established joint-empty-scene flank reading at this exact
# geometry -- EM's mandatory-fix comparator (Iteration 33), REUSED
# UNMODIFIED here per Red Team's Iteration-35 disclosure requirement (item
# 3): calibrated against ONE delta=0 realization, not re-derived for the
# N=2000 ensemble.
EMPTY_JOINT_FLANK_RAW_NATIVE_ESTABLISHED = 2.8615137799931016
FLANK_DENOMINATOR_THRESHOLD = 0.20

# exp-056's own p_abs_joint_measured (radial_absorbed_power on the delta=0
# joint captures) -- THERMODYNAMICS' comparator for this cycle's new
# p_abs_naive anchor (mandatory fix).
P_ABS_JOINT_ESTABLISHED = {
    "off_pass": 2.7927,
    "off_bracket": 1.2908,
}

# VISION's own T2 photopic perceptual threshold (pinned exp-020, reused
# unmodified through exp-055/056) -- large-target regime, flat value.
C_THR_PHOTOPIC = 0.005

# ----------------------------------------------------------- RNG discipline
# N random relative-phase draws per article -- pure post-hoc reconstruction
# from the 9 already-captured legs, zero marginal FDTD cost.
N_DRAWS = 2000
DRAW_SEED = 2035   # Panel Iteration 35
# One FIXED, reproducible nonzero-phase draw used for (a) the Director's
# own noise-floor validation leg (Phase-3 catch, above) and (b) as a
# cross-check point inside the N_DRAWS ensemble is NOT reused for
# double-counting -- the noise-floor leg is a SEPARATE, additional FDTD
# call, not one of the N_DRAWS post-hoc reconstructions.
NOISE_FLOOR_SEED = 58
