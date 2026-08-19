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

## Results

`run.py` executed cleanly, zero exceptions. Full per-point data:
`results.json`.

**Scorecard: 13 CONFIRMED, 1 PARTIAL, 0 REFUTED.**

- **P-A1 — CONFIRMED.** Thickness 0.307692/0.615385/0.923077 m, core
  0.192308/0.384615/0.576923 m — match the predicted bands exactly; τ =
  24.000000 exactly at all three witness radii.
- **P-A2 — struck (fix 7), not scored.**
- **P-A3 — CONFIRMED.** No existing verdict's code, gate, or `results.json`
  touched by this cycle's changes (checked: only `REALIZABILITY_MEMO.md`
  gained new text; `lab/glare_sidecar.py` gained a docstring only, zero
  numeric/behavioral change — verified by re-running the full trust suite,
  see below).
- **P-A4 — CONFIRMED.** σ_max/e-folding figures reported and labeled
  illustrative-only throughout (`run.py` output, `results.json`,
  `REALIZABILITY_MEMO.md` Entry 2).
- **P-A5 — CONFIRMED.** τ-conservation reframe adopted verbatim in
  `REALIZABILITY_MEMO.md` Entry 2.
- **Regression gate — CONFIRMED, exact.** The generalized propagator at
  the OLD (exp-042) geometry, θ=+40°, reproduces exp-042's own committed
  module output to `0.00e+00` relative error at all 3λ (`results.json`,
  `block_b.regression`) — the generalization introduces no bug.
- **P-B1 — PARTIAL, and the honest miss is itself informative.** The
  literal falsifier (predicted period within 5% of exp-042's own
  *cited* periods, 1.4°/1.9°/2.4°) is REFUTED: measured 1.550°/2.066°/
  2.583° at the new geometry's A=724, 7.6–10.7% off the cited (rounded,
  2-sig-fig) figures. But recomputing the OLD-geometry period with the
  identical formula and full precision (not the LOGBOOK's rounded
  citation) gives **1.4919°/1.9892°/2.4865°** [corrected at Phase 5 —
  see erratum below; an earlier draft of this paragraph cited
  1.4925°/1.9900°/2.4875°, hand-computed out-of-band rather than
  produced by invoking the committed `ripple_period_deg` function, caught
  independently by PHOTONICS and ELECTROMAGNETISM] — and the new/old
  ratio then matches the pure geometric prediction A_old/A_new =
  752/724 = 1.0386740331491713 **exactly** (an algebraic identity of
  `ripple_period_deg`'s own formula — λ and cosθ cancel — not an
  approximate empirical convergence; EM's own Phase-5 correction to this
  paragraph's original "well under 1% self-consistency" framing, itself
  more conservative than the truth). **The re-parameterized CODE is
  internally self-consistent at the new geometry; this is a
  code-algebraic identity, not evidence that the real edge-diffraction
  fringe (only an FDTD run could confirm) tracks the formula this
  precisely at the new geometry** — EM's own Phase-5 correction to this
  paragraph's original "the mechanism transfers correctly" sentence,
  which overclaimed past what mandatory fix 5's own INCONCLUSIVE scope
  already limits Block B to. The apparent 5%-band miss against the
  *cited* periods remains an artifact of comparing against a
  2-significant-figure citation, not a defect in the re-parameterization.
  Flagged honestly rather than silently re-scoped after the fact — this
  is exactly the kind of comparator-precision trap this program's own R3
  discipline exists to catch, applied here to a citation-precision
  question instead of a spatial-resolution one. **Erratum (Phase 5,
  applied same-shift, per Red Team's audit):** the figures in this
  paragraph were corrected in place (T10's own "flag, don't silently
  rewrite" precedent applies to measured/scored data in `results.json`,
  which is unaffected — this paragraph is prose commentary, not a scored
  prediction, and two independent Phase-5 seats plus Red Team's own audit
  converged on the same correct figures before this text was touched).
- **P-B2 — CONFIRMED.** 5 of 27 (θ,λ) points exceed GATE_HARD=0.001
  (worst: θ=−25°, 750nm).
- **P-B3 — CONFIRMED.** Worst |C_empty| = 0.004855, inside the predicted
  [0.0005, 0.006] band and below VISION's photopic C_thr=0.005 (by a
  ~3% margin — the closest any reading gets to the perceptual bar on this
  channel, informational only).
- **P-B4 — CONFIRMED, exactly as predicted.** 5.865×10⁻³ × 1.3872 =
  8.136×10⁻³ → 61.5×/245.8× below MARGINAL/FAIL. P-G24-2 survives
  regardless of anything measured in this block.
- **P-B5 — CONFIRMED.** exp-047's three near-boundary points shift by
  −0.0063/−0.0073/−0.0420 ratio-units under a maximally conservative
  (zero-cancellation) worst-case correction — all well under the 0.1
  falsifier, no category flip (all three stay MARGINAL).
- **P-B6 — CONFIRMED by construction.** Scope note shipped verbatim in
  every output (`run.py`, `results.json`, this file) — no language
  anywhere claims this block "closes" the T21/T24 contamination question.
- **P-C1 — CONFIRMED.** 10^0.3=1.99526 (0.2369% err), 10^−0.3=0.50119
  (0.2374% err) — both comfortably under 0.3%.
- **P-C2 — CONFIRMED, regime check passed (necessary, not sufficient) —
  reworded at Phase 5, VISION's own catch, Red-Team-adopted.** All three
  of exp-047's own near-boundary points (L_eq = 1×10⁻⁵ / 1.7×10⁻⁴ /
  1.17×10⁻³ cd/m²) sit below L_REF=3.0 — the low-luminance regime T2's
  ±0.3-log figure is committed for, not the clamped photopic floor. This
  rules out the wrong (clamped) regime; it does NOT establish that ±0.3
  log is UNIFORM across the low-luminance regime, which T2's own source
  describes as bridging three physically distinct psychophysical
  behaviors (Weber's law, Rose–de Vries, near-absolute-threshold) via one
  fitted power law. One of the three points (L_eq=1×10⁻⁵) sits only ~2×
  above this program's own cited absolute-rod-limit crossover
  (L*_lab≈5×10⁻⁶ cd/m², LOGBOOK Iteration 1) — a regime where classical
  psychophysics typically shows LARGER, not smaller, threshold scatter
  than in the Weber-law regime the figure may be most directly informed
  by. The original committed language ("Applicability CONFIRMED") is
  corrected here to state plainly what was and wasn't tested — see
  `results.json`'s own `block_c.recommendation_scope` field, left
  unrewritten per T10's precedent, this prose paragraph corrects the
  reading of it, not the underlying committed data.
- **P-C3 — CONFIRMED: SOURCE.** `lab/glare_sidecar.py::tier_w_verdict`'s
  docstring updated with the citation and regime-applicability scope
  (see diff); **zero numeric change** to the function itself, exactly as
  the conditional recommendation specified.

**Trust suite**: full fast suite + stages 10–17 re-run after all code
changes (docstring-only in `lab/glare_sidecar.py`, no behavioral change
expected) — 104/104 green, unchanged from pre-shift baseline. Results
(`results.json`, `REALIZABILITY_MEMO.md` Entry 2, `lab/glare_sidecar.py`
docstring): committed together with this file.

## Learned

- The panel's own independence mechanics caught, blind and before any
  code existed, a real defect (MATERIALS' dx-bridge finding) that would
  otherwise have shipped a units-incoherent "sharpened" physical claim
  into a permanent realizability memo — precisely the failure mode this
  program's own Red Team exists to prevent, and this time prevented
  *before* Phase 3, not corrected after.
- P-B1's own honest miss (refuted against a rounded citation, confirmed
  against a precise same-formula comparator) is a small, low-stakes
  instance of a real methodological lesson: falsifier bands written
  against another cycle's *rounded, reported* figures rather than a
  freshly, precisely recomputed comparator can manufacture a spurious
  "miss" — worth remembering for any future cycle citing another
  experiment's own rounded headline numbers as a falsifier target.
- Red Team's independent re-verification (running the cited formulas
  directly, not trusting seat characterizations) caught two real defects
  (the `round()`-drop mislabeling, the P-A2 anchoring risk) that none of
  the five blind seats named — the standing "verify against source, not
  seat characterization" discipline doing real work again.
- This cycle's own three blocks stayed genuinely file-disjoint and
  desk-only exactly as scoped at Phase 1 — no scope-dilution symptom
  observed (the risk PHOTONICS/the proposer both self-flagged).

## Phase 5 (six fresh blind seats + Red Team audit)

**Six independent reviews, verdicts: 4 PROMISING (PHOTONICS, ELECTRO-
MAGNETISM, THERMODYNAMICS, QUANTUM OPTICS), 2 PARTIAL (VISION SCIENCE,
MATERIALS — each scoped to open items adjacent to the headline, neither
finding a defect in P-B4/P-G24-2 itself). Red Team's own independent
verdict for the cycle as a whole: PROMISING**, re-derived from source at
every load-bearing claim, not inherited from the vote count.

**Does anything found threaten P-G24-2/P-B4? No — independently
re-confirmed by Red Team a fourth way** (own arithmetic, EM's, PHOTONICS',
and Red Team's own recompute all converge on 8.136×10⁻³, 61.5×/245.8×
margins). The headline is physics-capped (|C|≤1.0) against every
correction any seat raised.

**Two genuinely new cross-seat findings, independently converged, both
verified against source by Red Team and corrected same-shift (see above,
"Erratum" and reworded P-C2):**

1. **PHOTONICS and ELECTROMAGNETISM independently, by different routes**
   (direct execution vs. algebraic re-derivation), caught that this
   file's own "precisely recomputed" OLD-geometry period figures
   (1.4925°/1.9900°/2.4875°) do not reproduce from the committed
   `ripple_period_deg` function — they were hand-computed out-of-band.
   Red Team's own third independent recompute (backward-solving the
   implied `A` from the wrong figures: 751.70, not 752) confirms the
   diagnosis precisely. Corrected same-shift. **Separately, EM proved the
   new/old period ratio is an EXACT algebraic identity** (752/724,
   λ-independent), not an approximate "<1%" empirical convergence as
   originally stated — a genuine strengthening, alongside a genuine
   overclaim catch (the algebra proves code self-consistency, not that
   the real FDTD fringe tracks the formula this precisely at the new
   geometry) — both corrected same-shift.
2. **MATERIALS offered to render, this shift, the tier call
   `REALIZABILITY_MEMO.md` Entry 2 deliberately deferred**
   (UNOBTANIUM-WITH-PARAMETERS, via an informal thickness comparison).
   **Red Team rejected the offer**, checked against the memo's own table:
   every existing WITH-PARAMETERS row rests on a sourced literature check
   (exp-036/exp-037), none informally — Entry 2's own deferral is the
   standard-consistent call, not a shortfall. Recorded in the memo, not
   acted on.

**Other findings, all confirmed and corrected same-shift:**

- MATERIALS' "<0.1%" thickness-match claim was arithmetically wrong
  (actual 0.75%/0.33%) — corrected in `REALIZABILITY_MEMO.md`.
- MATERIALS' "no dx bridge anywhere in this program" overstated the gap
  (a real bench-scale bridge exists; the missing bridge is specifically
  to witness scale) — corrected in `REALIZABILITY_MEMO.md`.
- THERMODYNAMICS' own Phase-2 finding (witness-scale `h_eff` unverified)
  landed correctly in this file and `design_geometry.py` but was missing
  from `REALIZABILITY_MEMO.md` Entry 2, the most durable record for
  exactly these numbers — added same-shift. THERMO also computed (as an
  estimate, not a run) that the correction shrinks this program's two
  thinnest detectability margins (exp-043's ON-endpoint: ~5.1×→~2.6×;
  exp-045's dose-accumulation: ~27,080×→~38–42×) without flipping either
  — queued as an Iteration-26 candidate, not run this cycle.
- VISION's Phase-2 catch (Block C's regime check is necessary, not
  sufficient — doesn't establish ±0.3-log uniformity near the
  absolute-threshold edge, where one near-boundary point sits only ~2×
  above this program's own cited crossover) — reworded above.
- EM found an undisclosed latent narrowing in the geometry-dict
  generalization (never exercised at TAPER≠ABSORB or OBJ_Y≠NY//2) —
  harmless for every case this cycle runs (both hold in both geometries
  used), flagged for any future geometry that might not.
- PHOTONICS found the 9-angle FALLBACK grid (10° steps) is coarser than
  the ~1.5–2.6° fringe period it characterizes — the reported worst point
  is likely not the true worst phase at this geometry. New, not caught at
  Phase 2, feeds Iteration 26's own ranked queue.

**Checkpoint criterion 4: does NOT fire.** Every defect found this Phase
5 is confined to disclosure/labeling/citation precision in prose or a
memo entry, none load-bearing, all correctable same-shift and corrected.
Named plainly per this program's own convention: this is the **third
consecutive cycle** (23: Biot/fill-factor gap; 24: bare-"Tier-W" slip;
25: two independently-caught unreproducible "precise" figures) the
fix-docket-delivery pattern recurs inside the document meant to close a
prior gap. **New standing house rule, adopted (VISION's Phase-5 proposal,
Red-Team-elevated from recommendation to adopted rule):** any falsifier
or self-consistency figure cited as "precisely recomputed" must be
produced by invoking the actual committed function at prediction-freeze
or Phase-5-correction time, never hand-typed, however simple the
arithmetic looks. Recorded in `LOGBOOK.md`'s house-discipline record.

**Red Team's ranked priorities for Iteration 26** (adjudicating EM's
disagreement with VISION/PHOTONICS/QUANTUM's own rankings — Red Team's
standing authority): (1) QUANTUM's `gaussian_angle_weights`
n-convergence audit — non-negotiable, a third deferral would repeat this
program's own named r=156 anti-pattern. (2) T8/T13/T14: at minimum,
replace the point-C=−0.7209 with a sensitivity band spanning T13's two
extrapolation models everywhere cited as a witness-scale surrogate
(EM's own cheap fallback), with a proper reconciliation scoped as a
future Phase-1 proposal, not assumed solved by the band alone. (3)
Genuine FDTD `ABSORB` sweep at Block B's new geometry (T21-vs-T24). (4)
Build and measure the fixed-absolute-thickness `graded_black_shell`
variant (now a 9-iteration deferral, four seats independently rank it).
(5) Fine (≤1°) angular sweep around the actual ±35° fallback geometry.
(6) Fresh c*(λ) refit at the new geometry. (7) THERMO's witness-scale
`h_eff` re-derivation for the two thinnest-margin readings. (8)
Regime-stratify T2's ±0.3-log uncertainty near the absolute-threshold
edge. (9) [done same-shift: the house rule above.] (10) Ocular-dose
disposition (low priority, unchanged).

## Next

Superseded by Red Team's own Phase-5 ranked priorities (above) — this
section is left as the pre-Phase-5 draft's own record (Director's
original Phase-1 scope call) for the historical trail; **the authoritative
Iteration-26 queue is the ten-item Phase-5 list above**, not this one.
