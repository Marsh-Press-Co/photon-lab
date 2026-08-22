# exp-056 — The T26 Near-Null Generalization Test

Panel Iteration 33. Lead: **VISION SCIENCE** (rotation — completes the
rotation's second full cycle: VISION→PHOTONICS→MATERIALS→EM→
THERMODYNAMICS→QUANTUM→repeat; QUANTUM led Iteration 32). Full seven-seat
cycle: Phase 1 proposal (VISION SCIENCE) → five blind parallel critiques
(PHOTONICS, MATERIALS, ELECTROMAGNETISM, THERMODYNAMICS, QUANTUM OPTICS —
all support-with-changes) → Red Team last with everything (verdict:
proceed-with-mandatory-fixes, 6 numbered attacks, 7-item docket) → this
Phase-3 synthesis. Full verbatim record: `LOGBOOK.md`, Iteration 33.

## Hypothesis

Not a mechanism proposal — pure diagnostic/instrumentation work, same
register as Iterations 2/4/5/6/20/22/25/26/27/29/31/32. **T26** (opened
Iteration 32, exp-055): fixed-zero-relative-phase N=9 coherent joint
injection produces a large EMPTY-scene artifact (`C_empty_joint=−0.05343`,
>10× VISION's own T2 photopic `C_thr=0.005`) but was characterized on only
one loaded article — the deep-shadow PEC-cored absorber (`C_naive≈−0.72`),
where the coherent-vs-incoherent deviation was small (`|ΔC|=0.317%`
absolute), plausibly because strong absorption suppresses the vacuum
interference pattern before it reaches the object window.

That suppression hypothesis has never been tested where it actually governs
a real verdict: `off_pass` (τ=0.0065, exp-032, established naive
`C₆₀₀=−0.00450`) is this program's **only-ever constraint-3 PASS**, and it
is optically thin (by linearity its loaded field differs from the empty
field by only O(τ)≈0.65%). If the T26 artifact is not suppressed at this τ,
`off_pass`'s coherent-injection `C_joint` should sit near the raw
empty-scene artifact scale (≈−0.05), not its own real −0.0045 — a
human-visible PASS would read, under coherent injection, as a FAIL by more
than 10×, an instrument choice masquerading as physics. `off_bracket`
(τ=0.003, exp-032) rides along as a second, more transparent point on the
same curve.

This build closes T26's two other open gaps at the same time: EM's
still-missing R3 check on the coherent EMPTY-scene channel itself (stage
19's own R3 check ran only on an unrelated small canonical geometry, never
on the actual r=78 bench), and a zero-marginal-cost window-position/
angle-quantization sensitivity read.

## Setup

**Native geometry (r=78)**: exp-024/032/055's own fallback bench, reused
verbatim — NX=360, NY=1584, OBJ=(170,792), SRC_X=300, ABSORB=TAPER=40,
W_OBJ=GUARD_OUT=W_FLANK=78/185/78, PLANE_X=77 (dx=15), cpl=20, λ=600nm,
courant=0.99, STEPS=1400.

**Rescaled geometry (r=117, R3 check)**: exp-033's own ×1.5 rescale of the
identical physical scene, reused verbatim — NX=540, NY=2376, OBJ=(255,1188),
SRC_X=450, ABSORB=TAPER=60, W_OBJ=GUARD_OUT=W_FLANK=117/278/117, PLANE_X=116
(dx=22), cpl=30, STEPS=2100.

**Articles**: `off_pass` (uniform disk r≤78, ε_r=1.0, σ=4.16667×10⁻⁵,
τ=0.0065), `off_bracket` (σ=1.92308×10⁻⁵, τ=0.003) — exp-032/033's own
construction, no PEC core, unchanged. `empty` (vacuum) for the R3 leg.

**3 NEW FDTD calls**: `off_pass_joint`, `off_bracket_joint` (native r=78,
cpl=20, N=9 simultaneous sources, fixed zero relative phase, amplitude=1.0
each) + `empty_joint_cpl30` (rescaled r=117, cpl=30, N=9 simultaneous,
vacuum). Full design: `design_geometry.py`.

## New suite machinery

None. Stage 19's own docstring (`lab/validation/run_all.py`) states its
field-identity argument (joint N-source phasor == pointwise sum of
single-source phasors) is geometry- and N-independent — a structural
property of the engine's fixed linear update operators (LTI recursion,
already proven at two different geometries: the canonical small scene and
r=78/exp-055). Verified this claim directly against the docstring and code
before relying on it (Red Team's own audit read the same code and did not
contest it). This cycle's own empty-scene R3 check (cpl 20→30 at the actual
bench geometry) is the genuine new empirical validation T26 was missing —
a resolution-convergence check, not a new identity gate. Full existing
bench reverified 49/49 (`--only 12346789,10,11,19`) before this run.

## Phase 3 — accepted / overridden (Director's synthesis)

Red Team's verdict: **proceed-with-mandatory-fixes**, 6 numbered attacks,
7-item docket. **6 of 7 items ACCEPTED IN FULL; item 3 (the "phantom disk"
control) ACCEPTED IN INTENT, IMPLEMENTED DIFFERENTLY** — Director's own
Phase-3 catch, below. Full record:

1. **[Attack 2, EM, load-bearing] Weber `C` has no finite passivity
   ceiling — only raw window flux does.** Cauchy-Schwarz bounds
   `|ΣEᵢ|²` (triangle inequality, geometry-independent); it says nothing
   about the RATIO `(b_obj−b_flank)/b_flank`, which can diverge if
   `b_flank→0`. A large `|C_joint|` alone cannot distinguish genuine
   unsuppressed interference from one fixed-phase draw landing near a
   flank-window node. **Fixed:** every native disposition now reports
   `b_obj_joint`/`b_flank_joint` explicitly and computes
   `flank_ratio_vs_empty_joint = b_flank_joint /
   EMPTY_JOINT_FLANK_RAW_NATIVE_ESTABLISHED` (2.8615137799931016, exp-055's
   own established joint-empty-scene flank reading at this exact
   geometry — the same coherent injection modality, so this is a direct,
   apples-to-apples "did loading the object collapse the flank window"
   check, not a cross-modality proxy). `flank_denominator_flag = True` if
   that ratio < 0.20 invalidates a CONFIRMED verdict on P-VIS-1/2 as
   denominator-artifact-consistent, not scored.
2. **[Attack 1, MATERIALS, constraint-3-adjacent] No explicit
   "Realizability bound" line; the constraint-3-headline-vs-caveat hedge
   (this program's own recurring failure mode, now flagged a fourth time
   by Red Team) was left inferable only from Idealizations.** **Fixed:**
   Realizability bound section added below. P-VIS-1/2's own disposition-(a)
   sentence now states explicitly, inline, that a CONFIRMED result
   establishes nothing about `off_pass`'s appearance under real,
   non-phase-locked ambient light — fixed-zero-relative-phase N=9 injection
   has no ambient-illumination analog — and moves no Tier-W/Tier-A verdict.
3. **[Attack — PHOTONICS' phantom-disk control (σ=0, ε_r=1, r=78),
   Red-Team-endorsed as mandatory fix 3] DIRECTOR'S OWN CATCH, not raised
   by any Phase-2 seat or Red Team: as specified, this "phantom" scene is
   PHYSICALLY IDENTICAL to the vacuum/empty scene already measured at this
   exact geometry.** `sim.sigma_e[mask] += 0` is a no-op; `ε_r=1` matches
   the ambient background exactly — there is no discontinuity of any kind
   for the field to interact with. Running it would reproduce
   `C_empty_joint=−0.0534252451544586` (exp-055) to machine precision, a
   wasted FDTD call. **Implemented differently, same intent, ZERO
   additional cost**: the existing native empty-scene joint measurement
   IS the τ=0 point on the same suppression-vs-τ curve as `off_bracket`
   (τ=0.003) and `off_pass` (τ=0.0065) — a genuine 3-point curve for free,
   discriminating geometric/edge-driven suppression (predicts τ=0/0.003/
   0.0065 all show comparable |C|, since there's no absorption to vary)
   from τ-scaled bulk suppression (predicts a real trend with τ) exactly
   as PHOTONICS intended, without the redundant run. Recorded in
   `results.json`'s `phantom_control_zero_cost` block.
4. **[THERMODYNAMICS, confirmed by Red Team] Zero energy sidecar for the
   two new real-media legs — cannot tell "genuinely elevated local
   absorption" from "pure redistribution of exactly-conserved energy."**
   **Fixed, Director-scoped**: `sc.radial_absorbed_power` is applied to
   the SAME held captures (zero marginal FDTD cost) to report
   `p_abs_joint_measured` for `off_pass_joint`/`off_bracket_joint`. **Not
   fully implemented as originally worded** — Red Team's docket asked for
   this measured value to be compared "against the established
   naive-incoherent anchor," but no such anchor exists in this program's
   record: exp-032 never computed `radial_absorbed_power` for these
   articles (only Weber-contrast window profiles were saved, and the raw
   FDTD captures were discarded after use). Building that anchor would
   require re-running the 9+9 individual legs with full captures retained
   — the same structural gap Red Team itself used to defer QUANTUM's
   fuller redesign (docket item 7, below) rather than smuggle it in
   unscoped. Named as a follow-on (see Next), not built here.
5. **[Attacks 4/5, PHOTONICS' citation catches, confirmed by Red Team]
   §6's cited rescaled-geometry established empty-scene `C` had the wrong
   sign (+1.1648×10⁻⁴ cited, true value −0.00011648); the "fringe-period
   array" cited for P-VIS-5 does not exist as committed data, only Phase-5
   review prose.** **Fixed:** `design_geometry.py::
   C_EMPTY_NAIVE_RESCALED_ESTABLISHED = −0.00011647923213709`, verified
   directly against `experiments/033-.../results.json`'s
   `ambient_contrasts.*.C_empty` field (the deliberately-positive-magnitude
   `fresh_empty_decision_floor_600_cpl30` field is a DIFFERENT, floor-
   convention quantity, not the signed Weber C the proposal actually cited
   from). P-VIS-5's sourcing corrected below.
6. **[Attack 3, unfalsifiable] P-VIS-5 (angle-quantization sensitivity)
   committed a numeric threshold with no shown formula converting the
   fringe-period estimate into that number.** **Fixed per Red Team's own
   sanctioned alternative:** relabeled a named, unresolved open question
   with NO numeric disposition threshold this cycle (see Predictions,
   below) rather than a pseudo-quantified claim.
7. **[Attack 6, adjudicating QUANTUM's proposed redesign] QUANTUM's
   critique correctly identified that the real open question is
   phase-realization VARIANCE, not one arbitrary fixed-phase draw, and
   proposed replacing the joint call with individual per-angle legs saving
   full complex phasors, reconstructed post-hoc into multiple random-phase
   draws.** Red Team's own verification found the "already-validated"
   linear-superposition identity holds only for in-memory complex `Ez`
   arrays, never persisted to disk by any existing `run.py` — building the
   needed save format plus a new trust-suite identity gate is genuine new
   machinery under PANEL.md's own house rule, not a same-cycle parameter
   swap, and honestly scoped for both articles is an 18-leg, 6×+ scope
   escalation. **Ruling accepted: NOT adopted this cycle.** Named
   Iteration-34's ranked-#1 follow-on (see Next) — a deferral with a name
   and a reason, exp-033's own Block-B precedent for handling exactly this
   situation.

**Not mandatory, adopted**: window-position sensitivity offsets
symmetrized around the primary plane (native `{13,15,17}`, rescaled
`{20,22,24}`, replacing the Phase-1 proposal's asymmetric `{12,15,16}`/
`{18,22,24}`) — free, since both are read post-hoc from the same captures.

## T1 escape route

**NONE.** Both `off_pass`/`off_bracket` are static/linear/time-invariant
media (real σ, no PEC core, ε_r=1) — no σ(I) gating is built or claimed.
This measures only whether the ambient instrument's own coherent-injection
artifact could contaminate a scoring of an already-built OFF-state
endpoint.

## Realizability bound (Materials' seat duty — Red Team mandatory fix 2)

**Not applicable.** No new material or mechanism is proposed; `off_pass`/
`off_bracket` reuse exp-032/033's own construction verbatim (PUBLISHED-tier
ordinary lossy media — a ε_r=1 conductive sponge with a hard conductivity
step, ka≈24.5). The realizability question this cycle answers is purely
instrumental: does the fixed-zero-relative-phase joint-injection artifact
characterized at Iteration 32 (T26) generalize to a near-null article, and
by how much — not whether either article can be built. Any CONFIRMED
verdict below establishes nothing about buildability, and nothing about
`off_pass`'s appearance under real, non-phase-locked ambient light (no
ambient-illumination analog exists for fixed-relative-phase N=9 injection).

## Predictions — committed before this experiment's first (`run.py`) run

**P-VIS-1 (`off_pass` coherent joint Weber C, native r=78, 600nm) — the
headline question.** Predicted band **|C_joint| ∈ [0.020, 0.11]** — the
ladder bucket would flip from established PASS (naive |C|=0.0045) to
MARGINAL-or-FAIL. Informal central estimate (low-confidence, by analogy,
same register as exp-055's own P-055-1): **≈0.045–0.065**. Disposition:
(a) |C_joint| ≥ 0.02 AND `flank_denominator_flag` is False → CONFIRMED,
artifact unsuppressed at this τ — but this establishes NOTHING about
`off_pass`'s appearance under real ambient light (no phase-locked-injection
analog exists), only that this bench's fixed-zero-relative-phase joint
idiom is unsafe for scoring future near-null articles; moves no Tier-W/
Tier-A verdict. If `flank_denominator_flag` is True instead, relabel
"denominator-artifact-consistent, not scored," per Red Team's mandatory
fix 1. (b) 0.005 ≤ |C_joint| < 0.02 → PARTIAL, partial suppression.
(c) |C_joint| < 0.005 → REFUTED, weak τ=0.0065 absorption suppresses the
artifact nearly as well as the deep-shadow article does.

**P-VIS-2 (`off_bracket` coherent joint C, informational discriminator).**
Predicted band **|C_joint| ∈ [0.020, 0.10]**, central ≈0.045–0.060. Same
three-way disposition and ambient-light-analog caveat as P-VIS-1.

**P-DIR-1 (the zero-cost τ=0 "phantom" point, Director's Phase-3
correction).** Not a prediction — a fact verifiable by construction:
`C_joint(τ=0) ≡ C_empty_joint(native) = −0.0534252451544586` exactly (same
scene). Read alongside P-VIS-1/2 as the third point of a τ∈{0, 0.003,
0.0065} suppression curve, discriminating geometric/edge-driven suppression
(flat across τ) from τ-scaled bulk suppression (a real trend).

**P-VIS-3 (empty-scene R3 check, cpl 20→30 at the ACTUAL r=78-equivalent
geometry — T26's own missing empirical validation).** Predicted band
**|C_empty_joint(cpl30)| ∈ [0.025, 0.11]** — within ~2× of the established
cpl=20 value (−0.05343), consistent with genuine deterministic multi-beam
interference (EM's Cauchy-Schwarz mechanism, already confirmed real) rather
than a grid artifact. Disposition: stays in band → CONFIRMED, T26 is
R3-clean; shrinks below **0.017** (>3× reduction toward the naive-floor
scale, ~10⁻⁴) → REFUTED, T26 is at least partly a resolution artifact.

**P-VIS-4 (window-position sensitivity, zero-FDTD, read post-hoc from the
3 captures at dx∈{13,15,17} native / {20,22,24} rescaled).** Predicted:
`C_empty_joint`'s window-mean swings ≤30% relative across these 2-cell
shifts. Disposition: swing >50% relative → the artifact's magnitude is
placement-dominated, not a stable scene property — a new citation caveat.

**P-VIS-5 (angle-quantization sensitivity) — RELABELED an unresolved open
question, no numeric disposition threshold this cycle** (Red Team mandatory
fix 6: no shown formula converts a fringe-period estimate into a
±0.5°-sensitivity number). Not scored; named again in Next.

**THERMO sidecar (P-VIS-1/2 companion, informational, not a pass/fail
prediction)**: `p_abs_joint_measured` (FDTD-derived, `radial_absorbed_power`
on the held capture) reported for `off_pass_joint`/`off_bracket_joint`.
No naive-incoherent absorbed-power anchor exists to compare against this
cycle (see Phase-3 fix 4, above) — reported as a bare number for a future
cycle to compare, not scored against a band here.

## Idealizations

Fixed (zero) relative temporal phase — one coherent realization per
article, not the true random-phase incoherent ensemble; T25 stays open
regardless of this cycle's outcome (QUANTUM's own deferred redesign is the
correct next build for the variance question, not this cycle's scope). 2D
TMz, single λ=600nm, no chromatic sweep. `off_pass`/`off_bracket` are
ordinary static/linear media — no σ(I) gating tested; this cycle is purely
about whether the *instrument* contaminates their score. Bench-scale
diagnostic only: no Tier-W/Tier-A constraint-3 verdict moves from this
cycle regardless of outcome — `off_pass`'s PASS was already flagged
bench-scale-only and already shown fragile under a *different* instrument
axis (T16, N9→N17 angular quadrature, exp-034/035); this cycle adds a
third, independent fragility axis to an already-thin margin, it does not
newly endanger a robust result. R3 leg reuses exp-033's own established
×1.5 rescaling idiom. P-VIS-1/2 central estimates are explicitly informal/
low-confidence, by analogy. The THERMO sidecar (P-VIS-1/2 companion)
reports a measured absorbed power with no established naive-incoherent
comparator — informational only, not scored. No new suite stage: stage
19's field-identity argument is geometry/N-independent by construction,
verified against the docstring/code, not re-derived here.

## Results

3 new FDTD calls. Full data: `results.json`.

| Gate/Prediction | Predicted | Measured | Verdict |
|---|---|---|---|
