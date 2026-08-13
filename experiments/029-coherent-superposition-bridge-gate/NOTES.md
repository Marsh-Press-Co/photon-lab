# exp-029 — The Coherent-Superposition Bridge Gate

Panel Iteration 6 (lead: QUANTUM OPTICS, rotation — the mandatory,
fourth-cycle build of QUANTUM's own coherent-superposition bridge-gate
package, deferred at Iterations 2, 3/4, and 5). Full seven-seat cycle:
Phase 1 proposal (QUANTUM) → 5 blind parallel critiques (PHOTONICS,
MATERIALS, ELECTROMAGNETISM, THERMODYNAMICS, VISION SCIENCE — all
support-with-changes, with EM and THERMODYNAMICS independently converging
on the identical Cauchy-Schwarz normalization catch) → Red Team last with
everything (verdict: proceed-with-mandatory-fixes, six numbered attacks,
one — the derived-amplitude precision bug — caught by none of the five) →
this Phase-3 synthesis. Full verbatim record: `LOGBOOK.md`, Iteration 6.

## Hypothesis

Not a mechanism proposal — pure diagnostic/instrumentation work, same
register as Iterations 2–5. This program has never run two sources
simultaneously in one `Sim` and checked the joint field against linear
superposition; every multi-angle ambient measurement (`lab/ambient.py`)
sums intensities from separate single-source runs post-hoc. `Sim.sources`
is a plain list and `run()`'s step loop already sums an arbitrary number
of source injections with zero new engine physics — but the mechanical
capability existing is not the configuration being validated end-to-end
(Red Team's own Iteration-5 ruling), and no future σ(I) or joint
beam+ambient mechanism can be built until this is checked.

**Stated honestly, up front:** a real flashlight-beam-over-ambient scene
is physically INCOHERENT (different sources, femtosecond coherence
times). This experiment tests COHERENT superposition — a forced choice,
not a preference, since a single-tone CW run of two simultaneous same-λ
sources is deterministically phase-locked by this engine's own update
equations; true mutual incoherence needs an ensemble-averaged
random-relative-phase idiom, unbuilt, out of scope. This build does not
model the witness scene; it validates machinery and characterizes a real
complication (coherent interference in the absorption channel) a future
incoherent bridge will have to handle.

## Setup

Two sources, injected simultaneously in one `Sim` for the first time
outside a suite check: "beam" (angle 0°, amplitude 1.0) and "off_axis"
(angle 30°, amplitude √(AMP_REL), AMP_REL = 2×10⁻⁴ — Iteration 1's own
committed scenario default, LOGBOOK.md docket #4). Object: exp-028's
exact Cell B construction (`graded_black_shell(r_in=30, r_out=78,
sigma_max=0.5, eps_max=1.0)` **plus** the core-fill line
`sigma_e[rr<r_in]+=sigma_max`) — T9's mechanistically clean,
non-PEC-cored article, at exp-001/026/027/028's native beam-scene bench
(N=560, λ=600nm, cpl=20, courant_frac=0.32, steps=3200). Full design:
`design_geometry.py`.

**6 new FDTD sim calls**: empty+beam, empty+off_axis, empty+joint,
object+beam, object+off_axis, object+joint.

## New suite stage (PANEL.md's house rule: new machinery ⇒ new suite
## stage with ≥1 absolute identity gate BEFORE results are trusted)

`lab/validation/run_all.py::stage11_multisource_superposition()`, built
and run this shift BEFORE any exp-029 number below was computed. Compact
canonical scene (stage 10's own no-core article, `graded_black_shell(0,
32)`, cpl=20, 900 steps), same two-source configuration:

- **Vacuum scene: joint Ez phasor == sum of single-source phasors (RMS
  relative)**: measured **1.91×10⁻¹⁵** — **PASS** (gate ≤1×10⁻⁶), two
  orders tighter than even the proposal's own optimistic 10⁻¹³–10⁻¹¹
  central estimate.
- **Object scene (lossy σ_e branch, exercised with 2 concurrent sources
  for the first time): joint Ez phasor == sum of single-source phasors**:
  measured **1.89×10⁻¹⁵** — **PASS**. Confirms EM's/Red Team's line-by-line
  trace: every step in `Sim.run()` is a fixed linear operator on the field
  state (ca/cb depend only on static σ_e/ε_r, source injection is
  additive per-source, damping and the PEC clamp are fixed diagonal
  maps) — superposition holds to float64 round-off, not merely
  approximately.
- **Joint (2-source) scene: radial closure vs box-ledger p_abs**: measured
  **1.13%**, inside the reused stage-10-calibrated **≤1.5%** gate and
  squarely inside P-QUANTUM-3's own committed central band (1.0–1.3%) —
  the empirical circle-vs-square registration offset stays source-count-
  independent, now confirmed on a spatially-interfering field.

Full suite: **48/48 green** (`--only 12346789,10,11`) before this
experiment's first official run.

## Phase 3 — accepted / overridden (Director's synthesis)

Red Team's verdict: **proceed-with-mandatory-fixes**, six numbered
attacks. **All six ACCEPTED, zero overridden** — full record:

1. **[inconsistency, LOAD-BEARING] The bench object was missing the
   core-fill line — MATERIALS' catch, confirmed exactly by Red Team
   against `experiments/028.../run.py::build_cell`.** As originally
   tabulated (Phase 1), `graded_black_shell(r_in=30,...)` alone leaves
   r<30 an unfilled vacuum hole — a different, never-validated
   hollow-shell article, not "T9's mechanistically clean article." **Fixed:**
   `run.py::build_object()` now applies exp-028's exact Cell B
   construction (shell + `sigma_e[rr<r_in]+=sigma_max`), with a printed,
   asserted non-vacuum check (`core-fill assertion failed` if r<r_in reads
   as vacuum) before any gate is trusted.
2. **[inconsistency] P-QUANTUM-7/8's predicted band [0%,30%] used the
   wrong denominator — EM and THERMODYNAMICS independently derived the
   identical Cauchy-Schwarz bound; PHOTONICS independently flagged the
   same order-of-magnitude problem via a Bessel-suppression argument;
   Red Team confirmed all three by direct re-derivation.** |P_int| ≤
   2√(P_abs(beam)·P_abs(off_axis)) is a passivity fact (σ_e≥0
   everywhere); normalized against P_abs(off_axis) (the proposal's
   original choice) the ceiling is 2/√AMP_REL ≈ 14,142% — not 30%, off by
   ~3 orders of magnitude. **Fixed:** P-QUANTUM-7 renormalized to
   |ΔP_int|/P_abs(object+beam), predicted band **[0%, 2.83%]**
   (`design_geometry.py::P_INT_CEILING_FRAC_OF_BEAM = 2√AMP_REL`, the
   physically correct, bounded ceiling).
3. **[inexpressible] `intensity_role`/`amp_rel` are not `add_line_source()`
   kwargs — PHOTONICS' catch, escalated to mandatory by Red Team (a real
   implementation blocker, not a wording nit — checked against the actual
   function signature in `lab/fdtd2d.py`).** **Fixed:** `run.py` passes
   only `(x, angle_deg, amplitude)` to `add_line_source()`, exactly
   exp-028's own precedent; `intensity_role`/`amp_rel`-equivalent fields
   (`amp_rel`, `amp_beam`, `amp_offaxis`, `offaxis_angle_deg`) live only in
   `results.json`'s `meta` dict.
4. **[inconsistency] The proposal's own hand-copied amplitude literal
   (0.014142) fails its OWN stated 1e-9 assert tolerance by 3.8× — a NEW
   catch, none of the five blind critiques caught this, Red Team's own
   find.** The identical "derived value checked against a pre-rounded
   display number" bug class as Iteration 5's SIGMA_ON drift and the
   "55.47" peak-bin rounding. **Fixed:** `design_geometry.py::AMP_OFFAXIS
   = AMP_BEAM * np.sqrt(AMP_REL)` — derived at full float64 precision in
   code, never a hand-copied literal; the module-level `assert` now holds
   trivially (verified: `(AMP_OFFAXIS/AMP_BEAM)**2 = 0.000200000000`,
   target `0.0002`).
5. **[inconsistency] The second source's `"ambient"` label risked
   implying constraint-3 progress this build doesn't deliver — VISION's
   catch, sharpened by Red Team: "orthogonal" mischaracterizes what is
   actually a silently-dropped half of QUANTUM's own Iteration-1-committed
   design (LOGBOOK.md docket #4/(b): "one joint beam+ambient run on the
   linear sponge reproducing beam-behind and C simultaneously").** **Fixed:**
   the second source's role is labeled `"off_axis"` throughout code,
   results, and this NOTES.md — not `"ambient"`. `results.json`'s
   `meta.note_naming` field states explicitly, in full: this experiment
   does not touch `lab/ambient.py`, computes no Weber contrast, and does
   not reproduce C; it DEFERS the beam+ambient-C-reproduction half of
   docket #4/(b), not built this cycle — named as a deferred commitment,
   not described as merely unrelated.
6. **[inconsistency, recommended, folded in] Gate Q6 alone doesn't test
   for hidden spatial redistribution between the joint field and the
   naive per-source sum — Red Team's own extension of QUANTUM's original
   Iteration-5 scoping intent.** Field-level equality (Gate Q5, ≤1e-6) does
   NOT imply `p_J=0.5·σ_e·|Ez|²` is bin-wise additive, since `p_J` is
   QUADRATIC in Ez. **Folded in:** a new informational metric,
   **P-QUANTUM-9**, compares the joint scene's radial-ledger bins directly
   against the bin-wise sum of the beam-only and off_axis-only radial
   ledgers — the actual spatial-redistribution test Q6's aggregate closure
   alone can't provide.

## T1 escape-route statement

No escape mechanism implemented or claimed — pure diagnostic/
instrumentation work, the same register as Iterations 2–5. This build
removes a named prerequisite for any future proposal needing a joint
beam+ambient scene, but stated honestly: because the physically correct
model of that scene is INCOHERENT, this build does not itself deliver the
joint scene T1 needs. It validates that `Sim.sources` correctly
implements linear superposition end-to-end and characterizes a genuine
complication (coherent interference in the absorption channel) a future
incoherent-ensemble or extended-`ambient.py` bridge will have to handle.

## Predictions — committed before this experiment's first (`run.py`) run

**Field superposition (reconfirm at exp-029's native beam-scene scale,
3200 steps vs. suite stage 11's 900):**
- **P-QUANTUM-4 (Gate Q4, vacuum scene):** RMS relative error ≤ 1×10⁻⁶
  (gate); central prediction **~10⁻¹⁴–10⁻¹²** (more steps than suite
  stage 11 accumulate marginally more float64 round-off, but the
  algebraic identity is exact regardless of step count).
- **P-QUANTUM-5 (Gate Q5, object scene — primary claim, lossy σ_e branch
  at full beam-scene scale):** ≤1×10⁻⁶ gate; central prediction
  **~10⁻¹⁴–10⁻¹²**, same order as Q4.

**Empirical closure:**
- **P-QUANTUM-6 (Gate Q6, radial closure, joint scene, core-filled
  object):** ≤1.5% gate (reused, stage-10/11-calibrated); central
  prediction **0.2–0.4%**, matching exp-028's own established closure at
  this exact bench scale (0.20–0.26%, native beam-scene geometry).
- **Precondition:** the core-fill assertion (`sigma_e(r<r_in) > 0`,
  printed) must hold before any gate is trusted.

**Coherent interference (informational, NOT gated, renormalized per fix
2 — Cauchy-Schwarz-bounded, not the proposal's original impossible
band):**
- **P-QUANTUM-7:** |ΔP_int| / P_abs(object+beam), predicted band
  **[0%, 2.83%]** (the Cauchy-Schwarz ceiling 2√AMP_REL,
  `design_geometry.py::P_INT_CEILING_FRAC_OF_BEAM`), nonzero, sign
  uncommitted. Reasoning: the interference term scales as
  √(P_abs(beam)·P_abs(off_axis)), i.e. linearly in the weak source's
  amplitude rather than quadratically — it can be materially larger, in
  absolute terms, than the off_axis source's own direct absorption, but
  is passivity-bounded relative to the beam's own dominant channel.
- **P-QUANTUM-9 (NEW, fix 6, bin-wise spatial redistribution check):**
  the peak-magnitude LOCAL (per-annulus) fractional deviation of the
  joint scene's bins from the naive bin-wise sum
  (`|bin_joint − bin_naive| / bin_naive`, at the bin of largest absolute
  deviation) exceeds the AGGREGATE fractional deviation (P-QUANTUM-7) by
  **≥3×** — i.e., real spatial structure in the interference pattern an
  aggregate closure check alone would wash out, consistent with the 30°
  off-axis source's Λ_y=2λ=40-cell interference fringe period cutting
  across the object's 156-cell diameter (≈3.9 fringe periods).

**Cross-cutting caveat:** the box-ledger channel's own decision-floor/
noise characterization (T11, still open, cross-cutting, unassigned to
this iteration) means P-QUANTUM-6/7/9's precise values should be read as
informally suggestive at the sub-percent level, not floor-gated verdicts
— the same standing caveat carried through Iterations 4–5.

## Idealizations

2D TMz, single polarization. Single λ=600nm scope — no chromatic sweep of
this bridge gate; the SIGMA_ON-style per-λ printed-assertion discipline
is satisfied vacuously by scope (nothing here rescales a geometric
constant), not exercised — a future 3-λ extension would need to add it
explicitly. **COHERENT superposition only** — explicitly NOT validating
incoherent superposition, which remains `lab/ambient.py`'s own
separate-run/post-hoc-intensity-sum idiom, untouched. The real
beam-over-ambient scene is physically incoherent; this build's two-source
coherent injection is a prerequisite validation plus a characterization
of why naive coherent joint-injection would give different physics than
that real scene, not a model of the scene itself. **No R3 (cpl×1.5)
resolution companion** for gates Q4/Q5 — they are resolution-independent
by construction (an algebraic property of the discrete recursion, not a
near-field measurement); IF P-QUANTUM-7/9's interference finding becomes
load-bearing for a future mechanism claim, it would warrant its own R3
check in a future cycle — named, not built. AMP_REL=2×10⁻⁴ is Iteration
1's own committed scenario default, reused, not re-sourced or re-derived
this cycle. **T11 (box-ledger decision floor) and the T10 +3.05pp
residual sub-cell sweep are NOT folded in this cycle** — both real,
cheap, and queued (Merged Ranking, Iteration 5), named for Phase 5
consideration or a future cycle. VISION's r=156 build is untouched — not
this seat's domain, Iteration 7's own hard commitment (with its own
pre-registered Checkpoint-4 tripwire), this proposal does not
second-guess it.

## Realizability bound (Materials' seat duty)

Not applicable — no new material or mechanism is proposed; the object
reuses exp-028's own Cell B construction (`graded_black_shell` + core
fill) verbatim, this program's most validated article (R≤0.2% broadband
reflection, σ_abs/σ_ext independently corroborated across four prior
experiments). The realizability question this cycle answers is purely
instrumental: does the engine's existing multi-source list correctly
implement linear superposition — answered by machinery already present,
zero new material physics.

## Results

*(to be appended after `run.py` executes — predictions above are
committed to git first, per house discipline.)*
