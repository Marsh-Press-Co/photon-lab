# exp-031 — The T12 Ripple Sweep, the T13 Desk Reconciliation, and QUANTUM's σ-Held g-Point

Panel Iteration 8. Lead: **PHOTONICS** (rotation). Full seven-seat cycle:
Phase 1 proposal (PHOTONICS) → 5 blind parallel critiques (MATERIALS,
ELECTROMAGNETISM, THERMODYNAMICS, QUANTUM OPTICS, VISION SCIENCE) → Red
Team last with everything (verdict: **proceed-with-mandatory-fixes**, 9
numbered attacks, **one — the PEC core missing from `graded_black_shell`'s
own construction in exp-030 — caught by none of the five blind seats, and
predating this cycle**) → Phase 3 synthesis (Director) → predictions
committed here, before any run → Phase 4 test. Verbatim panel transcript:
`LOGBOOK.md` Iteration 8.

## Hypothesis

Three independent diagnostic/reconciliation questions, none proposing a
new constraint-3 mechanism:

- **T12** — is PEC's flatly non-monotonic C(r) (exp-030, Iteration 7) a
  Fresnel-zone/edge-diffraction ripple, detectable as non-smooth structure
  in C(PLANE_DX) at fixed r?
- **T13** — the standing |C|≈0.98 witness-scale estimate (unsourced,
  Iteration 1) sharply disagrees with exp-030's own fitted witness
  prediction (−0.73/−0.86, finding e2, Iteration 7). Does a θ=0
  (single-angle, boresight) re-reading of the same bench data reconcile
  the two, or does the disagreement survive?
- **QUANTUM's g-calibration** — does the σ-held (not τ-held) sponge
  family's per-unit-τ efficiency g=|C|/τ stay scale-robust the way the
  τ-held diagnostic family already has?

## Red Team's load-bearing catch (accepted in full, not overridden)

Independently verified against the actual code before this experiment was
built: `experiments/030-scale-bridge/run.py::build_ambient`'s `"absorber"`
branch calls **only** `materials.graded_black_shell(...)` — no
`materials.pec_disk(...)`. Every other construction of this article in
this program's history (exp-001, exp-020, exp-024, exp-025, exp-027) pairs
`pec_disk(r_in)` + `graded_black_shell(r_in, r_out)`. exp-030's r_in region
(14.8% of the object's cross-sectional area, self-similar across
r=78/156/312) is literal vacuum in that experiment's code, not a coated
solid. θ=0 (boresight) is exactly the geometry this most directly
contaminates — a normal-incidence ray through the hollow core passes
unobstructed, where the historical construction would have hit PEC.

**Accepted, not overridden.** Folded into this experiment's own T12 sweep
rather than run as a separate bolt-on (Director's synthesis decision,
recorded here): the sweep's own r=78/156 "absorber" runs use the
historically-correct PEC-cored construction. This both supplies T12's
ripple data with the right article AND, by direct comparison against
exp-030's existing (uncored) r=156/θ=0 reading (C=−0.83412, established),
quantifies the core-correction delta at zero extra run cost. **This
experiment does not touch or re-run exp-030's own r=312 leg** — the
core-correction question at r=312 stays open, inherited to a future
iteration; exp-030's own headline ambient-summed (N=9) C(z/z_R) fit and
its Iteration-7 verdicts (PASS/MARGINAL/FAIL licensing, T9/T11 floor
closures) are **not retroactively altered by this experiment** — those
used the established, separately-sourced r=78 anchor and the N=9 metric
throughout, not the θ=0 single-angle reading this experiment newly
introduces.

## Setup

**T12 sweep** — 6 new FDTD runs, θ=0 only: empty/PEC/absorber(cored) ×
r∈{78,156}. Each run's full 2D field is captured once
(`sections.full_capture`) and its phasors re-sliced at every PLANE_DX in
that r's own grid (`design_geometry.py::PLANE_DX_GRID`) — 9 offsets at
r=78, 8 at r=156, both spanning N_F≈8–110 (z/z_R≈0.010–0.125) — zero extra
FDTD stepping per offset. Object window (`|y−y₀|≤r`) and flank window
(established `guard_out`/`flank` from `dg030.GEOM[r]`, computed for the
PLANE_DX=15 anchor) are held FIXED across the sweep — at normal incidence
the shadow doesn't shift with standoff the way it does across an angular
span, so this is the simpler, defensible choice (not re-derived per
offset). **Safety diagnostic**: the empty run's absolute (un-normalized)
flank level is tracked at every offset; any point where it droops >5% from
its own PLANE_DX=15 value is excluded from ripple interpretation as
ABSORB-band-contaminated, not read as physics. **Magnitude floor**: a
slope-sign reversal only counts toward P-PHOTONICS-1/2 if the slope change
exceeds `RIPPLE_NOISE_FLOOR=0.002` (Red Team fix #4/#5) — matching the
established r=156 δ_C floor-bias scale.

**T13 reconciliation** — zero new FDTD. Both the sqrt-law
(`C=C_∞+B√(z/z_R)`) and the ceiling-law (`C=−1+B·(z/z_R)^p`) are fit,
exactly (2-point solve, no ambiguity), to the θ=0 (r=78,r=156) pair — for
PEC and the now-correctly-cored absorber, separately. **Explicit
non-claim, per MATERIALS'/Red Team's mandatory fix**: PEC is
constraint-2-disqualified (it specularly reflects) — a clean PEC
reconciliation is diagnostic-only and materially moot for constraint 3,
and (per EM's independently-confirmed saturation-artifact finding) is
expected to converge regardless of whether the metric-mismatch hypothesis
is physically true, since PEC's θ=0 (r=156,r=312) pair from exp-030 was
already measured near-saturated. **No witness-scale "resolution" is
claimed for the absorber under any framing this cycle** — the two-law
comparison on the cored absorber data is reported honestly, whichever way
it comes out.

**QUANTUM's σ-held run** — 9 new FDTD runs at r=156, θ ∈ FALLBACK_ANGLES
(N=9), σ fixed at `sigma_off_lab(78)=5.128205e-5` (τ_center(156)=0.016,
printed-asserted). Reuses exp-030's own saved r=156 empty profiles (all 9
angles, `results.json['block1']['156']['profiles']['empty']`) — zero new
empty runs.

**THERMO sidecar** — post-run analytic only (expressibility contract).
r=156/θ=0/PLANE_DX=15 (canonical anchor) empty+PEC+absorber(cored) scenes
re-run (full 2D fields are not persisted between process invocations, so
this costs 3 small re-runs, ~2 min at the established rate — corrected
from the Phase-1 proposal's general "stays in memory" framing, which held
only within a single process invocation) and fed through the established
`sections.widths()` box-ledger idiom (`dg030.GEOM[156]['box']`) to report
absorbed fraction of the object-footprint incident power. Labeled
explicitly as **post-run analytic**, not an FDTD output. The ΔT/
emission-band step of THERMO's own charter stays blocked on docket #7's
still-missing witness-scenario watts, exactly as recorded at Iteration 1 —
this sidecar closes only the P_abs half of that chain.

**Scoring convention (VISION's flip, adopted verbatim, extending Iteration
7's own e2 tripwire):** every θ=0 single-angle C value produced this
cycle — T12's raw sweep points, T13's fitted witness predictions — is
**diagnostic-only and explicitly ineligible for constraint-3
photopic/scotopic scoring**. Only the N=9 ambient-summed metric may be
scored against VISION's frozen C_thr ladder. QUANTUM's σ-held run DOES use
the full N=9 ambient metric and IS scored against the ladder (P-DIR-3,
below).

## Idealizations

2D TMz, single λ=600nm/cpl=20 scope, unchanged throughout. The θ=0-only
T12/T13 instrument is a genuinely NARROWER measurement than the production
N=9 ambient C metric — it isolates a per-direction diffraction quantity
the ambient instrument's own incoherent sum would average out, at the
declared cost of not being constraint-3-scoreable itself. The PLANE_DX
grids under-sample the ripple's own (sub-cell) period at every point
tested (Phase-1's own idealization, unchanged) — this experiment tests for
aliasing-consistent non-smoothness, not a resolved fringe reconstruction.
Object/flank windows are held fixed across the PLANE_DX sweep rather than
re-derived per offset (defensible at θ=0, stated not smuggled). The
core-correction comparison uses exp-030's existing r=156/θ=0 uncored
reading as its baseline — a cross-experiment comparison, not a same-run
control; residual differences beyond the core (grid rerun, no other
changes) are not expected but not independently isolated either. T13's
2-point (r=78,156) fits span less than exp-030's own (r=156,312) baseline
in z/z_R dynamic range and are extrapolated across the same 1.5–2.5-decade
gap to witness scale — flagged, per Red Team's own fix, as NOT a
"resolution" for the absorber under any outcome. THERMO's sidecar reports
a fraction, not absolute watts — the ΔT/emission chain stays incomplete
pending docket #7. `graded_black_shell`'s realizability caveat (Iteration
7: self-similar construction ⇒ unobtainium coating thickness at witness
scale, ~0.31–0.92 m) is inherited unchanged; MATERIALS' Phase-2 note that
a solid-backed coated object (this experiment's corrected construction) is
also more physically representative of a real witness-scale absorber than
a free-floating hollow shell is recorded, independent of the
internal-consistency argument for restoring it.

## T1 escape-route statement

Instrumentation/reconciliation only, unchanged from the Phase-1 proposal:
no σ(I), σ(x,t), or angular-selectivity machinery is built; no new
material behavior; no new constraint-3 mechanism proposed or tested.

## Predictions (committed BEFORE any run — house discipline)

**T12 — ripple presence & structure**
- **P-PHOTONICS-1** (PEC ripple, magnitude-floored): ≥2 significant
  (slope-change > `RIPPLE_NOISE_FLOOR=0.002`) sign reversals across r=78's
  9-point sweep AND r=156's 8-point sweep.
- **P-PHOTONICS-2** (absorber, cored): ≤3 significant reversals per
  sweep, banded to allow but not require some non-smoothness (the shell's
  apodized edge should suppress but, per Phase-1's own uncored θ=0
  finding of absorber non-monotonicity at r=156→312, may not eliminate
  ripple).
- **P-PHOTONICS-3** (κ²-matched cross-check, PEC): C(r=78,PLANE_DX=15)
  and C(r=156,PLANE_DX=60) — same N_F=20.28, different r — agree within
  **0.03**. A larger gap indicates real r-dependence beyond N_F alone.
- **P-PHOTONICS-4** (safety diagnostic): empty raw flank level stays
  within 5% of its own PLANE_DX=15 value at every swept, non-excluded
  point.

**Fix 1 — core-correction delta (Director's own falsifiable band,
resolving Red Team attack #1)**
- **P-DIR-1**: |ΔC_core| = |C(r=156,θ=0,PLANE_DX=15,absorber-CORED) −
  (−0.83412)| (exp-030's established uncored reading) lands in
  **[0.02, 0.10]**, direction: cored reads MORE negative (deeper) than
  uncored. Decision bands, pre-committed: **<0.02 → negligible**, prior
  Iteration-7 absorber-side findings stand with only a footnote;
  **0.02–0.25 → moderate**, an explicit qualifier is added to T13/finding-
  e2's record but no retraction; **>0.25 → load-bearing**, the missing
  core is a materially large fraction of Iteration 7's own gap and
  triggers a formal erratum on exp-030's absorber-side conclusions,
  parallel to the SIGMA_ON erratum precedent (T10, Iteration 4/5).

**T13 — reconciliation**
- **P-PHOTONICS-5/6** (derivation audit; bounded-ansatz test on the
  ambient-summed metric): already established at Phase 1/Red Team's
  independent verification — reconfirmed as committed findings, not
  re-tested this run: no sourced derivation for |C|≈0.98 exists anywhere
  in the program record; the bounded-ansatz hypothesis is REFUTED (sqrt-
  law and ceiling-law already agree within 0.011 on the ambient-summed
  r=156/312 pair — a functional-form-robustness result, not this
  experiment's own new data).
- **P-DIR-2** (θ=0 dual-law fit, the corrected T13 test — replaces
  P-PHOTONICS-7): fit sqrt-law and ceiling-law to the θ=0 (r=78,r=156)
  pair, separately for PEC and the CORED absorber. Predict: **PEC's two
  fits agree within 0.02** (expected near-certainly regardless of the
  metric-mismatch hypothesis's truth, per EM's independently-confirmed
  saturation argument — explicitly NOT interpreted as validating the
  hypothesis if it passes). **Absorber's two fits disagree by more than
  0.05** (echoing the 0.13 disagreement already found on the uncored
  r=156/312 pair — predict the cored data remains functional-form-
  unstable, since correcting the construction doesn't fix the
  fundamental short-baseline-extrapolation problem). A absorber
  agreement within 0.05 would be a genuine surprise, flagged for Phase 5,
  not assumed away.

**QUANTUM**
- **P-QUANTUM-1**: C(156, σ-held) ∈ **[−0.0145, −0.0100]**, central
  ≈ −0.0123 (linear-τ interpolation −0.01105 plus the established r=156
  δ_C floor bias −0.00121, same direction as the τ-held sponges).
- **P-QUANTUM-2**: g floor-corrected ≈ **0.69**, within 15% of both
  g(78)=0.6848 and g(312)=0.6936.
- **P-DIR-3** (VISION's flip, scored explicitly against the frozen
  ladder): C(156,σ-held) scores **MARGINAL** (falls in [0.005, 0.02]) —
  the same verdict every σ(I) OFF-state article this program has ever
  built has received, at every scale tested to date.

**THERMO sidecar**
- **P-DIR-4**: PEC's `sigma_abs` reads at or near the numerical floor
  (≤0.01 in normalized units — PEC absorbs nothing by construction, any
  nonzero reading is grid/registration noise); the cored absorber's
  `sigma_abs` reads substantially above it, consistent with (not
  necessarily numerically equal to) the established σ_abs/σ_ext≈0.5–0.6
  regime this program has measured at other geometries. Reported as
  informational — no ΔT/detectability claim is made pending docket #7.

## Results (exp-031, 2026-08-14)

18 new FDTD calls (6 sweep + 9 quantum + 3 thermo attempt), ~13 minutes
wall-clock for the sweep+quantum legs (sweep 264s, quantum 609s). r=156
sweep runs measured 62–84s each (vs. the 39.6s/run baseline established
by exp-030 at the same domain — the operational tripwire fired: actual
was ~1.6–2.1× the baseline, not the 8–28× miss this program has seen at
larger domain jumps, and total wall-clock stayed well inside budget).
**The THERMO sidecar (P-DIR-4) did not complete this cycle** — the first
attempt used `dg030.GEOM[156]['box']`, a field grepped-confirmed to be
computed but never actually referenced anywhere in exp-030's own code,
and produced unphysical `sigma_abs` (large negative) for the absorber. A
second attempt with a freshly-built, more conservative box (4λ clearance)
stalled well past the established per-run rate and was killed rather than
let run indefinitely against this shift's own time budget. **Deferred to
a future iteration, not silently dropped** — THERMODYNAMICS' Phase-2 flip
stands accepted in principle; its execution needs a validated box
geometry for this specific (line-source, θ=0, ambient-plane) scene class,
which does not yet exist in this program's own machinery.

**Erratum, added at Phase 5 (THERMODYNAMICS' own catch, independently
verified against the code, more precise than the account above):** the
first attempt's failure runs deeper than a bad box. `dg030.GEOM[156]` has
no `ref` field at all — the `sections.widths()` incident-intensity
reference strip exists only on the beam-scene `BEAM_GEOM`
(`ref=(cx,cy,round(60·κ))`, tuned to a collimated beam's flat-top core).
The first attempt's improvised `ref=(cx,cy,r)` (half-height 156) was
never validated for this scene class, sits upstream of the box entirely,
and produced a **negative** reference intensity (i_inc=−0.258) — meaning
every downstream number (including PEC's own sigma_scat=−646, a
lossless-scatterer sanity violation on its face) is uninterpretable, not
merely off. This numeric block was left in `results.json` under the key
`thermo` with no label distinguishing it from validated output — a real
gap against this program's own "flag, don't silently rewrite" convention,
corrected in this shift's own close-out: the block is now relocated to
`thermo_attempt1_INVALID` with an explicit erratum note in the JSON
itself. **No trust-suite gate exists for this scene class's box-ledger
channel** (PANEL.md's own house rule: new machinery needs an absolute
identity gate before results are trusted) — building one (box-independence
+ PEC lossless-null) is the correct prerequisite for any future P-DIR-4
attempt, not another hand-built box under time pressure.

**Every other prediction ran and is scored below** (all figures computed
in code, `run.py::run_fit`, not hand-asserted):

| Prediction | Predicted | Measured | Verdict |
|---|---|---|---|
| P-PHOTONICS-4 (safety diagnostic) | flank dev ≤5% at every point | max \|dev\| = 0.05% (r=78), 0.02% (r=156) | **CONFIRMED**, ~100× inside band |
| P-PHOTONICS-1 (PEC ripple, ≥2 sig. reversals) | ≥2 per r | **0 at both r=78 and r=156** | **REFUTED** |
| P-PHOTONICS-2 (absorber ripple, ≤3 reversals) | ≤3, allowing non-zero | **0 at both r** | technically inside band, but far cleaner than predicted |
| P-PHOTONICS-3 (κ²-matched cross-check) | agree within 0.03 | \|−0.98987 − (−0.98942)\| = **0.00044** | **CONFIRMED**, ~68× inside band |
| P-DIR-1 (core-correction delta) | \|ΔC_core\| ∈ [0.02,0.10], deeper when cored | **6.8×10⁻⁶** (−0.834113 vs established −0.83412) | **NEGLIGIBLE band, far below the predicted range** |
| P-DIR-2, PEC (dual-law agreement) | agree within 0.02 | **0.00314** | **CONFIRMED** (near-certain convergence, per EM's saturation argument — NOT read as validating metric-mismatch) |
| P-DIR-2, absorber (dual-law disagreement) | >0.05 | **0.2203** | **CONFIRMED**, more unstable than predicted |
| P-QUANTUM-1 (C(156,σ-held)) | [−0.0145,−0.0100], central −0.0123 | **−0.012361** | **CONFIRMED**, matches central prediction to 3 digits |
| P-QUANTUM-2 (g floor-corrected ≈0.69) | within 15% of 0.68–0.69 | **0.69685** (g_raw=0.77256) | **CONFIRMED**, within ~2% |
| P-DIR-3 (ladder score) | MARGINAL | \|C\|=0.01236 ∈ [0.005,0.02] → **MARGINAL** | **CONFIRMED** |

**T12's own central hypothesis test came back a clean, decisive NULL,
not a confirmation.** Across both r=78 (9 points, N_F 8.0–101.4) and
r=156 (8 points, N_F 10.0–110.6), for BOTH PEC and the (now correctly
cored) absorber, C(PLANE_DX) is smoothly and (within the 0.002 magnitude
floor) monotonically decreasing as PLANE_DX shrinks — **zero significant
sign reversals anywhere, in any of the four (r, article) sweeps.** This
directly refutes P-PHOTONICS-1's own falsifiable band. The dense sweep
finds no aliasing-consistent non-smoothness at this grid resolution for
either article — a genuinely clean null, not a marginal or ambiguous one
(the largest raw point-to-point change anywhere in the whole dataset is
0.0036, and every one of those small changes is monotonic-consistent,
not sign-flipping). **Read carefully**: this experiment's own PLANE_DX
sweep varies standoff at FIXED r — a different axis than T12's original
observation (C varying across the r=78→156→312 family at FIXED
PLANE_DX=15). A clean null on this axis doesn't retire T12 (the original
r-family non-monotonicity is untouched by this data — no r=312 point was
re-measured here), but it does mean the specific mechanism test proposed
(aliasing detectable as PLANE_DX-sweep non-smoothness) found no support,
at either r tested — a real, if partial, narrowing of T12's live
hypothesis space, for Phase 5 to weigh.

**P-DIR-1 (Fix 1's own core-correction delta) is a clean, load-bearing,
GOOD-NEWS result.** Restoring the historically-correct PEC core to the
absorber construction changes its r=156/θ=0 reading by **6.8×10⁻⁶** —
five orders of magnitude below even the "negligible" threshold. Physical
reading: the shell's own radial optical depth (τ_shell=24, printed-
asserted since Iteration 7's fix 2) is so large that essentially no
incident power survives the shell to ever reach the core region, whether
that region is PEC or vacuum — **the same mechanism T9 already
established via the box-ledger channel (exp-027/028: "the graded shell's
own σ(r) profile extinguishes nearly all incident power before it
reaches the core, in either construction")**, now independently
reproduced via a completely different measurement channel (single-angle
ambient contrast, not box-ledger absorbed power). Red Team's attack #1
was a genuine, necessary, load-bearing catch as a matter of construction
correctness and program hygiene — exp-030's own record technically used
the wrong article for every absorber-related θ=0/ambient number it ever
reported — but the corrected number reveals the defect was, for this
specific observable, quantitatively inconsequential. **exp-030's own
committed N=9 ambient-summed conclusions (the r=78 anchor, the PASS/
MARGINAL/FAIL licensing, T9/T11's floor closures) are untouched** — they
never used the θ=0 metric this experiment introduces, and in any case the
core-correction delta measured here is far too small to have moved them.

**T13 remains genuinely unresolved for the absorber — and the properly-
corrected data makes the case for caution stronger, not weaker.** PEC's
θ=0 dual-law fit converges tightly (0.00314), exactly as EM's Phase-2
saturation-artifact argument predicted — but per the pre-committed
reading, this is a structurally-guaranteed convergence given how close
PEC's own two points already sit to −1, not evidence the metric-mismatch
hypothesis is true. MATERIALS' point stands: PEC is constraint-2-
disqualified, so this convergence is diagnostic-only. **The absorber's
own dual-law disagreement (0.220) is actually LARGER than the uncored,
longer-baseline (r=156,312) comparison found at Phase 1/2 (0.132)** —
using the corrected article and the shorter (r=78,156) baseline makes the
functional-form instability worse, not better. No witness-scale number
for the absorber earns any more trust after this experiment than before
it; if anything, less.

**QUANTUM's g-calibration gap closes, in one regime, at one point —
narrower than first drafted here, per Phase-5 correction below.**
C(156,σ-held)=−0.01236 lands within 0.0001 of the pre-committed central
prediction. Scored against VISION's frozen ladder (P-DIR-3, her own
mandatory Phase-2 fix): **MARGINAL** — the same verdict every σ(I)
OFF-state article this program has ever built has received, at every
scale tested, restated explicitly here per her fix rather than left
implicit. The raw g(156)=0.773 sits notably above g(78)=0.685/g(312)=0.694
— but **once the same-run empty-scene δ_C floor bias is subtracted
(matching Red Team's own Iteration-7 e1 finding that this exact bias
explained 87–97% of the τ-held sponges' own apparent r=156 excursion),
g_floor_corrected=0.697 lands within 2% of both established endpoints.**

**Correction, added at Phase 5 (QUANTUM's own review, Red Team-confirmed
and sharpened):** this floor-correction is not a free arithmetic step —
it is licensed by an unstated **linear-response/weak-perturbation
assumption** (the object's own perturbation to the profile is localized
to the object window, so `C − C_empty ≈ δ_obj/e_flank` cleanly separates
object signal from baseline instrument bias), valid only because
τ=0.016 keeps |C| at the ~1% level where second-order terms are
negligible. **It is explicitly NOT licensed for PEC or the absorber**
(|C|~0.83–0.99, nowhere near the weak-perturbation regime) — exactly why
the floor-correction is correctly never applied to them in this
document, though the reason was never stated until now. The original
draft's closing claim — "T1's g=|C|/τ calibration constant is
strengthened as a robust, scale-independent quantity across BOTH the
τ-held and σ-held families" — **overclaimed relative to what was
actually measured, per Red Team's Phase-5 audit**: the σ-held family's
scale-robustness now rests on exactly ONE new floor-corrected point
(r=156); r=78 for this family was never separately run, and r=312 is
inherited only via the τ_off_field/τ_off_lab=κ(312)=4 numerical
coincidence (a repurposed τ-held point, not an independent σ-held
measurement). **Corrected statement:** the one new floor-corrected point
is consistent with scale-robust g in the weak-perturbation regime
(τ≈0.016, |C|≈1%); untested outside it, and untested at a second
independent σ-held geometry.

## Phase 5 — Director's addendum (six blind reviews + Red Team audit)

Full verbatim transcript: `LOGBOOK.md` Iteration 8. Two corrections above
already fold in the highest-priority Phase-5 findings (THERMO's erratum,
QUANTUM's g-calibration overclaim). Three more, recorded here per house
convention:

**The absorber's "wrong-direction asymptote" is elevated to program-level
significance.** PHOTONICS (ceiling-law exponent p=−0.148, structurally
cannot reach C=−1 at any finite z/z_R) and ELECTROMAGNETISM (sqrt-law
slope B=−0.277, C_∞=−0.803 shallower than either measured point) reached
the same conclusion through two independent functional-form diagnostics.
Red Team's audit named this the cycle's most decisive finding: it is the
**exact pathology Iteration 7's finding e2 first named**, now reproduced
on a corrected construction (PEC core restored) and a different, shorter
baseline (r=78,156 vs the original r=156,312) — three independent axes
of confirmation (construction, baseline, functional form) for the same
directional anomaly. No longer reasonably read as "the extrapolation is
merely unstable" — it is a reproducible, sign-consistent physical puzzle:
this graded absorber's contrast does not deepen toward geometric-shadow
completeness as the measurement approaches the regime where it should.
Unexplained; the leading candidate test (PHOTONICS' multi-point r-sweep,
Ranked top-3 below) is not yet run.

**A proposed cheap fix for T12 is likely geometrically infeasible as
described — caught by Red Team, missed by all six blind reviews.**
EM's/PHOTONICS' shared next-change pick (extend the r=156 PLANE_DX sweep
to reach N_F≈300+, where the original r=156→312 reversal actually lives)
requires PLANE_DX≈3.75 cells (0.19λ) — well inside the object's own
reactive near field, a regime none of this program's diagnostics have
validated and where "Fresnel-zone ripple" may not even be the right
model. Tips the Iteration 9 queue toward PHOTONICS' costlier but
structurally correct alternative (a genuine r-family sweep, the axis the
original reversal was actually observed on) over EM's cheaper one.

**Minor, flagged not corrected:** P-PHOTONICS-5/6's cited "0.011"
disagreement (ambient-summed sqrt-vs-ceiling law comparison, Phase 1)
does not independently reproduce under Red Team's audit — recomputing
with this cycle's own fit functions on the cited established values gives
0.0029–0.0055 (central 0.0045), roughly 2–4× smaller. Low-stakes (the
qualitative point — the ambient-summed metric is far more stable than
the θ=0 diagnostic's 0.220 — survives under every version computed) and
not gated this cycle; recorded per house discipline.

**Checkpoint assessment (Red Team's own explicit ruling, adopted):**
criterion 4 does not fire (constraint 3's status stated with unusual
candor this cycle; the θ=0-diagnostic-only labeling convention honored
everywhere load-bearing). Criterion 5 does not fire on the letter (both
Iteration 7 and 8 produced real, independently-verified content) —
**but Red Team flags, and the Director adopts as a direction check, not
a violation:** Iterations 4 through 8 — five straight cycles — are
instrument/reconciliation/audit work; Iteration 3 (exp-026) was the last
cycle to test an actual σ(I) candidate against VISION's ladder. Her
cheapest, most directly mechanism-relevant proposal (locate the actual
σ(I) PASS boundary, τ_off≈0.0065) has now been the top-ranked Phase-5
pick for three consecutive iterations (7, 8) without being built.
Surfaced explicitly for Iteration 9's own queue, below — not deprioritized
a fourth time.

## Cost note

15 new FDTD calls for the sweep+quantum stages (6+9, as scoped at Phase
1) + 3 small re-runs for the thermo sidecar (correction above) = **18
total**, all at r≤156. Estimated wall-clock, using exp-030's own measured
r=156 rate (39.6s/run) and the κ³-scaled r=78 estimate (~5s/run), flagged
per Red Team's own finding that this program's single worst empirically-
observed scaling miss (r=312's pilot run, ~28.6× the r=156 rate for a
κ=2 step) was well above naive κ³ — **not repeated here** since no run in
this experiment exceeds r=156, the domain size at which the established
rate is a measured baseline, not an extrapolation: sweep ≈ 3×5s (r=78) +
3×40s (r=156) ≈ 135s; quantum ≈ 9×40s ≈ 360s; thermo ≈ 3×40s ≈ 120s.
**Total ≈ 10 minutes.** Operational tripwire (Red Team's recommended,
adopted): log actual r=156 wall-clock on the sweep stage's first r=156 run
and compare against the 39.6s/run baseline before treating the remaining
estimate as reliable.
