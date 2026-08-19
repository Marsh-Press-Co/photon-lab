# exp-048 — Closing exp-047's Evidentiary Chord

**Panel Iteration 25.** Lead seat: VISION SCIENCE (rotation). Executes
exp-047 NOTES.md's own Red-Team-ranked Iteration-25 queue, items 1–3
(formal `REALIZABILITY_MEMO.md` entry, T21 fringe bound at the actual
±35° fallback geometry, MARGINAL-band source check) — all desk-only, zero
new FDTD calls. Full Phase 1–5 record: `LOGBOOK.md` Iteration 25.

## Hypothesis

Iteration 24's headline (exp-047, P-G24-2) survived Phase 5 intact but
left three loose threads in its own evidentiary chord — none of which
touch P-G24-2 itself, all of which bear on whether any FUTURE
near-boundary Tier-W-surrogate reading can be trusted. This cycle closes
all three: (A) formalizes MATERIALS' informal Iteration-7 UNOBTANIUM call
for `graded_black_shell` into a `REALIZABILITY_MEMO.md` entry; (B) bounds
T21's edge-diffraction fringe at the domain the C=−0.7209 anchor actually
uses (not the ±40° geometry T21 was discovered at); (C) checks whether
`lab/glare_sidecar.py`'s unsourced `[0.5,2.0]` MARGINAL band matches T2's
own committed ±0.3-log threshold uncertainty.

## Panel record summary

**Phase 1 (VISION SCIENCE):** proposed all three blocks combined (Red
Team's own Iteration-24 ranking put items 1–3 ahead of everything else,
all zero-FDTD). Self-flagged five conflicts, including that Block A's tier
judgment is properly MATERIALS' charter call and that combining three
blocks risks the scope-dilution pattern exp-042's own mandatory fix 7
warned against.

**Phase 2 (five blind seats + Red Team):** all five seats returned
support-with-changes (zero outright oppose), each with a distinct
load-bearing catch — the panel's independence mechanics doing real work,
not formal ritual:

- **MATERIALS** [load-bearing]: Block A's σ_max/e-folding-length figures
  (78.0/39.0/26.0 "m⁻¹") silently reuse `sigma_max_shell`'s FDTD
  grid-normalized formula (`lab/fdtd2d.py`'s own convention: grid units,
  dx=1) with meter-valued input, no dx/unit bridge — the identical
  near-field↔witness-scale conflation T8/T13/T14 already flagged for C,
  now smuggled into σ. Separately: "a conductivity that must shrink as
  the object grows, a property no real material has" mischaracterizes
  ordinary optical-depth conservation (achievable via independently-chosen
  σ/doping per build size), not a forbidden material property.
- **ELECTROMAGNETISM** [load-bearing, Red-Team-hardened to a flat mandatory
  fix]: P-B4's "headroom 0.28" additive framing is the wrong lens —
  `veiled_contrast` is linear/multiplicative in C; the correct bound is
  ×1.3872 (0.7209→1.0), giving 8.14×10⁻³ and 61×/246× margins to
  MARGINAL/FAIL (matching PHOTONICS' own Iteration-24 closed-form
  figure), not an additive 0.28 gap.
- **PHOTONICS** [load-bearing]: Block B's own predicted contamination band
  overlaps live thread T24's uncharacterized `ABSORB=40` boundary
  systematic (0.002–0.007 absolute), held fixed and uncorrected this
  cycle — a desk propagator with zero FDTD boundary physics cannot
  distinguish a real edge fringe from a boundary artifact of comparable
  size. Reframe: this block's deliverable is a re-parameterization +
  magnitude cross-check ONLY, not a completed contamination-risk verdict.
- **QUANTUM OPTICS** [load-bearing]: Block B silently inherits the
  "deliberately beamformed/focused synthetic array" construction
  (`_src_amp` driving the full tapered aperture) QUANTUM's own Iteration-22
  finding (exp-046/T21) already flagged as physically distinct from a
  naturally-divergent single-mode emitter — undisclosed at the new
  geometry unless fixed.
- **THERMODYNAMICS**: Block A's newly-computed witness-scale physical
  dimensions (cm-scale e-folding depth, m-scale radius) have never had
  THERMO's own sidecar UNDETECTABLE verdicts (exp-043/044/045)
  re-derived at that scale; `h_eff=k_air/L`'s quiescent-conduction-limit
  assumption is unverified there (real natural convection likely governs
  at meter scale, not conduction-limited transfer).

**Red Team** (ruling: **proceed-with-mandatory-fixes**). Independently
verified the two most load-bearing claims against source before ruling:
(1) ran `dg.sigma_max_shell(0.5)` directly — reproduces the proposal's
cited 78.0 exactly, confirming MATERIALS' dx-bridge attack (found it
understated, not overreach — the implied cell size backing these numbers
is ~10⁵–10⁶× coarser than any wavelength this engine has ever resolved);
(2) recomputed EM's multiplicative bound independently — confirmed
5.865×10⁻³ × 1.3872 = 8.1357×10⁻³, matching PHOTONICS' cited figure.
Also found, independently (missed by all five blind seats): Block A's
core-radius figures (0.192/0.385/0.577m) do not actually come from a
"verbatim" call to exp-030's `r_in_shell` (its `round()` silently returns
0/0/1 when fed meters, not the cited figures) — the continuous formula
was used instead, undisclosed as such. Also: Block A's P-A2 ("tier stays
UNOBTANIUM-WITH-PARAMETERS") pre-commits to MATERIALS' own charter
verdict before the memo is written, especially now that attack (2) shows
the underlying arithmetic doesn't establish what the narrative claimed —
struck. Explicitly checked for constraint-3 violations and unfalsifiable
claims (own standing mandate): none found — no block touches P-G24-2's
verdict, and no language anywhere relaxes the LAB-bar default, the
MARGINAL band's conservatism, or T21/T24 contamination concerns.
Checkpoint criterion 4 does **not** fire; flagged (not fired) as another
instance of this program's own named "fix-docket-delivery pattern" —
overclaiming language ("closes the gap," "sharpens WHY unobtainium,"
"headroom 0.28") riding ahead of what the underlying arithmetic supports,
recurring in the very cycle meant to close Iteration 24's own loose
threads.

**Ruling: proceed-with-mandatory-fixes, seven items, all adopted, none
overridden** (see `design_geometry.py`'s module docstring for the full
numbered list). Full numbered attacks and ruling text: `LOGBOOK.md`
Iteration 25.

## Setup

`experiments/048-evidentiary-chord-closure/design_geometry.py`: Block A's
geometric-fact formulas (thickness/core-radius, continuous, disclosed as
NOT a call to exp-030's cell-quantized `r_in_shell`) plus the
illustrative-only σ_max reading and the τ-conservation reframe; Block B's
generalized `field_and_h`/`edge_diffraction_c_empty_corrected`,
parameterized on a geometry dict (exp-042's own module hardcoded a single
geometry — this is the disclosed generalization, mandatory fix 1) plus
both the OLD (exp-042, regression-anchor only) and NEW (exp-030's
`GEOM[78]`) geometry dicts; Block C's MARGINAL-band and T2 vertical-log
constants.

`run.py`: executes all three blocks, prints the frozen predictions first,
writes `results.json`. Zero new FDTD calls, zero new engine code in
`lab/` — no new trust-suite stage required (house convention: a
re-parameterization of an already-committed desk propagator, reusing
`lab.ambient.window_means`/`weber` unmodified, is not new physics
machinery). Instead, a local self-check regression gate: the generalized
propagator, evaluated at the OLD (exp-042) geometry, θ=+40°, all 3λ, must
reproduce exp-042's own committed module's output to machine precision —
verified BEFORE any NEW-geometry number is trusted (the same discipline
stage-16's own gate (c) used for its FDTD anchor, applied here to a
code-correctness regression instead of a physics anchor).

## Parameters

**Block A**: `SIGMA_MAX_BASE=0.5`, `R_BASE_CELLS=78`, `R_IN_BASE_FRAC=30/78`,
`TAU_SHELL=24.0` — all reproduced verbatim from exp-030's own code-asserted
formulas. Witness radii (0.5, 1.0, 1.5) m — exp-030's own committed set.

**Block B**: NEW geometry = exp-030's `GEOM[78]` (NY=1528, OBJ_Y=764,
D_SP=223, GUARD_OUT=186, R_OUT=W_FLANK=78, PLANE_X=77, SRC_X=300,
ABSORB=TAPER=40); OLD geometry (regression-anchor only) = exp-042's own
hardcoded constants (NY=1584, OBJ_Y=792, GUARD_OUT=185, same else).
FALLBACK_ANGLES = (−35,−25,−15,−5,0,5,15,25,35), N=9 — exp-030/047's own
set. 3λ (450/600/750nm), cpl 15/20/25. `GATE_HARD=0.001` (exp-024/041's
own committed hard gate).

**Block C**: MARGINAL band [0.5, 2.0] (`lab/glare_sidecar.py::tier_w_verdict`);
T2's own committed vertical-log uncertainty ±0.3 (`LOGBOOK.md`, "Scotopic
scaling" section, `C_thr(L) = 0.005·max[1,(L/3)^−0.4]`); `L_REF=3.0` cd/m²
(the photopic-floor clamp boundary).

## Idealizations

- **Block A**: no fresh literature check this cycle (T18's WebFetch block,
  independently re-confirmed blocked as of this iteration's own pre-flight
  — see below). σ_max/e-folding-length figures are **illustrative-only** —
  a literal reuse of a cell-normalized FDTD formula fed meter-valued
  input, with no dx/unit bridge established anywhere in this program; NOT
  asserted as physical conductivities. Fabrication/structural feasibility
  out of scope. **New (THERMO's finding, adopted):** no existing THERMO
  sidecar UNDETECTABLE verdict has been re-derived at these newly-computed
  witness-scale physical dimensions (cm-scale e-folding depth, m-scale
  radius) — `h_eff=k_air/L`'s quiescent-conduction-limit assumption is
  unverified at meter scale, where real natural convection (not
  conduction-limited transfer) likely governs; a real, disclosed, unclosed
  gap, not resolved by this cycle.
- **Block B**: desk-only, inherits every idealization already disclosed in
  exp-042's own module (2D TMz continuum, kr≫1 far-field validity,
  incoherent per-θ CW summation, no FDTD settling dynamics or grid
  dispersion). ABSORB held fixed at 40, not swept — T24's own known
  0.002–0.007-absolute uncorrected boundary systematic rides under every
  number this block reports; **this block's own findings are explicitly
  INCONCLUSIVE against that confound**, not a completed contamination-risk
  verdict (mandatory fix 5). **New (QUANTUM's finding, adopted):** this
  block's per-angle numbers, like exp-041/042's own, are produced by
  `_src_amp` driving the FULL tapered aperture with a per-θ linear phase
  ramp — the same "deliberately beamformed/focused synthetic array"
  construction exp-046/T21 already flagged as physically distinct from a
  naturally-divergent single-mode emitter (mandatory fix 6).
- **Block C**: examines exactly one candidate uncertainty source and one
  regime-applicability check; does not attempt a full stacked-uncertainty
  budget across every channel that could legitimately inform a MARGINAL
  band's width (T7 chromatic, Block B's own fringe finding, T16
  quadrature, EM's L_v/L_B extrapolation-range concern).
- **General**: zero new engine code, zero new FDTD calls; three blocks
  combined in one cycle (Director's Phase-3 call, per this program's own
  precedent — Iterations 8, 20, 23), all desk-only, mostly file-disjoint.

## Predictions (committed before this experiment's own run — see `run.py`'s
frozen `PREDICTIONS` string, printed first, unmodified by the scoring
logic)

See `run.py`'s `PREDICTIONS` string (reproduced in full there) for the
verbatim frozen text: P-A1/A3/A4/A5 (P-A2 struck), P-B1/B2/B3/B4/B5/B6
(+ the regression gate), P-C1/C2/C3.

T18 (WebFetch egress block) not re-tested this cycle — not load-bearing
(Block A makes no fresh literature claim; its own P-A4/P-A5 are desk
arithmetic and a reframe of already-committed program facts, not a
literature check).
