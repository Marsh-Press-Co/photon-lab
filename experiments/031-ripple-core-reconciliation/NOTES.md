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
