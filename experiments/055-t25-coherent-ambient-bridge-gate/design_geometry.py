"""exp-055 design constants — The T25 Coherent-vs-Incoherent Ambient-Sum
Bridge Gate, N=9 Equal-Amplitude Configuration.
=======================================================================
Panel Iteration 32 (lead: QUANTUM OPTICS, rotation — "still owed" the lead
slot since Iteration 30's content-policy block; LOGBOOK.md Iteration 31
close). T25 (opened Iteration 29, exp-052 Phase-5, QUANTUM's own catch,
Red-Team-elevated to program scope): every constraint-3 `C` citation this
program has ever issued rests on `lab/ambient.py`'s incoherent intensity
sum over N=9 EQUAL-amplitude single-source runs — the only prior coherent
cross-term measurement (exp-029, stage 11) tested a structurally different,
amplitude-ASYMMETRIC 2-source configuration (one strong beam + one weak
probe, AMP_REL=2e-4) whose Cauchy-Schwarz ceiling does not bound the
equal-amplitude N=9 case. This experiment builds the real bridge gate.

Phase-3 synthesis incorporates Red Team's Phase-2 mandatory-fix docket
(LOGBOOK.md Iteration 32) in full — see NOTES.md for the complete
accepted/overridden record. Two corrections load-bearing enough to name
here, both caught between the Phase-1 proposal and this synthesis:

  1. [Red Team Attack 1, LOAD-BEARING, docket items 1-3] The Phase-1
     proposal's "absorber" article was HOLLOW (`graded_black_shell` alone,
     no PEC core) and claimed this was "exp-020/024/030/052's own
     construction, inherited unchanged." Verified FALSE: exp-020/024 (the
     actual source of the `C78_ESTABLISHED` anchor) build "absorber" as
     `pec_disk(r_in=30)` THEN `graded_black_shell(r_in=30, r_out=78)` —
     PEC-CORED. Only exp-030's own `build_ambient` used hollow, a defect
     exp-052 itself already diagnosed and reversed. Fixed here: the article
     under test is PEC-cored, matching exp-024/052's own construction
     exactly, at the very angles (±25°/±35°) PLAN.md's own Iteration-32+
     queue (item 7) flags as untested for the hollow/PEC-core delta.
  2. [Director's own Phase-3 catch, not raised by any Phase-2 seat] The
     Phase-1 proposal cited `C78_ESTABLISHED['absorber'] = -0.72087` as its
     naive-incoherent anchor, but that constant (defined in
     `experiments/030-scale-bridge/design_geometry.py`) is a PHOTOPIC-
     luminosity-weighted average across 450/600/750nm
     (`_vweight(_C78_RAW['absorber'])`), while this cycle is single-λ=600nm
     scope. The correct single-λ anchor is `_C78_RAW['absorber'][600] =
     -0.7211` (exp-024's own NOTES.md fallback table, ±35deg/N=9/NY=1584).
     Fixed here. Separately (disclosed, not "fixed" — the pre-registered
     check below is the actual test): `experiments/030-scale-bridge`'s own
     `GEOM[78]` (ny=1528, obj=(170,764), guard_out=186), which exp-030/052
     reused as "the r=78 geometry," is NOT byte-identical to exp-024's own
     original fallback geometry that produced `C78_ESTABLISHED`
     (NY=1584, OBJ=(170,792), GUARD_OUT=185) — this file uses exp-024's
     OWN geometry directly (imported by value below, not re-derived via
     exp-030's r-family formula), so this cycle's own reproduction check
     (NOTES.md P-055-6) is a clean test of ONE variable (coherent vs.
     incoherent), not confounded by an unrelated geometry-formula drift.
     Whether `GEOM[78]`'s own small drift from this geometry matters to any
     OTHER experiment's numbers is a separate, unaddressed question, named
     for a future cycle.

See NOTES.md for the full Phase 1/2/3 accepted/overridden record and
LOGBOOK.md Iteration 32 for the verbatim panel transcript.
"""

import numpy as np

# ---------------------------------------- r=78 geometry, exp-024's own
# (sourced verbatim from experiments/024-ambient-margin-adjudication/
# design_geometry.py's own fallback-geometry constants — NOT re-derived via
# exp-030's r-family formula; see Director's Phase-3 note above.)
NX = 360
NY = 1584
R_OUT = 78
SRC_X = 300
ABSORB = 40
TAPER = 40
OBJ_X = 170
OBJ = (OBJ_X, NY // 2)                 # (170, 792)
W_OBJ = 78
GUARD_OUT = 185
W_FLANK = 78
SENS_PLANE = 15                        # primary reporting plane (exp-024/030/052 precedent)
PLANE_X = OBJ_X - R_OUT - SENS_PLANE   # 77

CPL = 20
LAM_NM = 600
COURANT_FRAC = 0.99
STEPS = 1400

FALLBACK_ANGLES = (-35, -25, -15, -5, 0, 5, 15, 25, 35)   # N=9, exp-024/030/052's own set
R_IN = 30                              # PEC-core / shell inner radius (exp-024/052's own "absorber")
SIGMA_MAX = 0.5                        # graded_black_shell defaults, exp-024's own call
EPS_MAX = 1.0

# ------------------------------------- established single-lambda anchor
# exp-024's own NOTES.md fallback table (line ~271-277), verified against
# experiments/030-scale-bridge/design_geometry.py::_C78_RAW['absorber'][600]
# (the raw, pre-V-weighting input) — NOT the V-weighted, 3-lambda
# `C78_ESTABLISHED['absorber']` constant (Director's Phase-3 fix 2, above).
C78_ABSORBER_600_ESTABLISHED = -0.7211

# ---------------------------------------------- Cauchy-Schwarz ceiling
# EM's Phase-2 re-derivation (Red-Team-confirmed, independently corroborated
# by THERMODYNAMICS' own N^2 statement): for N equal-amplitude sources, each
# pairwise cross-term |Q_ij| <= sqrt(P_i*P_j) = P (passivity, sigma_e>=0);
# total coherent intensity in [0, N^2*P]; incoherent baseline is N*P; so
# fractional deviation from the incoherent baseline is in [-1, N-1].
N_SOURCES = len(FALLBACK_ANGLES)
assert N_SOURCES == 9
DEVIATION_CEILING_LO = -1.0
DEVIATION_CEILING_HI = float(N_SOURCES - 1)   # 8.0 == +800%
assert DEVIATION_CEILING_HI == 8.0
