# exp-041 — Auditing the ±40° Angle Pair as the N17 Correction Standard (T20) (panel Iteration 18)

**2026-08-17 · driver: Clyde as panel Director · status: predictions committed, run not yet executed**

Eighteenth experiment of the panel program (PANEL.md / LOGBOOK.md). Lead
seat: **QUANTUM OPTICS** (rotation). Executes PLAN.md's queued Iteration-18
scope item (1) — Red Team's own #1-ranked Iteration-17 close priority,
live thread **T20**: Iteration 2 (exp-024) excluded the ±40° angle pair
from its standing ±35° fallback baseline *for cause* (it broke the δ_C
decision-floor gate non-monotonically at every wavelength) and named a
fine 36°→40° sweep its own #1 follow-up — never run, fifteen iterations
later. Meanwhile Iterations 11–12 (exp-034/035) built the N17 quadrature
(±35° fallback plus the SAME excluded ±40° pair) as the correction standard
used to downgrade this program's only-ever constraint-3 σ(I) OFF-state PASS
(exp-032) from PASS to MARGINAL — scored only against a loose 0.04
per-angle advisory bound never designed to catch this floor. This file is
the **Phase-3 synthesis**: one testable configuration, six critiques and a
Red Team audit resolved on the record, predictions committed before the
first run.

## Phase 1 — the proposal (QUANTUM OPTICS, lead)

Full text preserved verbatim in LOGBOOK.md Iteration 18. Summary: audit
T20 in two legs — (a) a zero-cost desk enumeration of every committed
LOGBOOK/PLAN.md conclusion resting on an N17-vs-N9 delta; (b) execute
Iteration 2's own never-run fine angle sweep at exp-024's exact geometry,
empty-scene-only, scored against the tight decision-floor gate rather than
the loose advisory bound.

**Leg (a) result (completed at Phase 1, unchallenged by any Phase-2 seat
— stands as written):**

*Directly rests on a measured N17-vs-N9 delta:* (1) exp-032/033's PASS→
MARGINAL downgrade (exp-035, Block N17_NATIVE_V2, Δ=6.522×10⁻⁴) — the
primary citation this thread exists to audit; (2) Block T16_CLOSE's
"REAL INTERACTION" verdict at r=156 (exp-035); (3) exp-034's own headline
citing "Block N17_156's domain at N17" as one of four readings; (4)
exp-040's dual-g decomposition attributing its dominant term to
"±35°→±40° coverage."

*Partially rests on N17-vs-N9, partially extrapolated:* (5) T16's own
program-wide claim that "every PASS/MARGINAL citation... including
off_lab at both scales" carries this uncertainty — checked: off_lab has
never itself been run at N17, so this is an unverified analogy, not a
direct measurement, and should be worded accordingly regardless of this
leg's own outcome.

*Checked and found NOT implicated:* (6) the g600 "reproducible anomaly"
recurrence (all four points are N9/±35°-fallback measurements); (7) T15's
reconciliation (exp-035, Block T15_RECONCILE — explicitly N9-only
throughout).

## Phase 2 — critiques (blind, then Red Team with everything)

Full text of all five discipline critiques and the Red Team audit
preserved verbatim in LOGBOOK.md Iteration 18. Summary:

- **PHOTONICS** (support-with-changes): the "empty-scene-only is fully
  sufficient" claim in the Phase-1 draft is optically overreaching — live
  thread T15 already measured a real, resolution-*growing* (1.0%→2.7%→
  3.1%) diffractive-leakage discrepancy at this bench's own extreme
  near-field standoff (PLANE_DX=15 cells = 0.75λ @600nm) that only
  manifests with an object present, a channel an empty-scene design
  structurally cannot see. Proposed 2-run object-present spot-check.
- **MATERIALS** (support): no MATERIALS-owned parameter appears in this
  leg; flagged that whichever direction this leg's finding runs, it cannot
  move either UNOBTANIUM-WITH-PARAMETERS verdict in `REALIZABILITY_MEMO.md`
  by more than a bookkeeping citation — both realizability gaps are 1–12
  orders of magnitude, decided on independent grounds.
- **ELECTROMAGNETISM** (support-with-changes): the geometry table is
  internally self-consistent (independently re-derived against
  `design_geometry.py`), but the Phase-1 draft's "sharp threshold, not
  smooth ramp" shape prediction leaned on EM's own "twentyfold
  cancellation collapse" mechanism as justification — a mechanism
  exp-024's own MARGIN_MULT-widening result (P-M1: REFUTED) already shows
  does NOT explain this specific floor. Proposed a 6-run θ=41–42–43°
  extension to let data, not an unsupported analogy, adjudicate shape.
- **THERMODYNAMICS** (support-with-changes): charter genuinely silent this
  cycle (no article, no absorbed power) — verified, not assumed, by
  checking leg (a)'s own dependency list. Flagged that the proposal's own
  reported 5–14× runtime slack goes unweighed against PLAN.md's two queued
  "cheap add-on if budget allows" THERMO items (thermo_sidecar rescoping,
  docket #7's witness table); asked for an explicit Phase-3 disposition
  rather than silent default.
- **VISION SCIENCE** (support-with-changes, **load-bearing**): the
  Phase-1 draft's §2 scoring-gate table mislabeled 0.005 as "the"
  decision floor. Checked directly against `experiments/024.../NOTES.md`
  and `run.py`: exp-024's own committed hard gate is **δ_C ≤ 0.001 at
  every λ** — 0.005 is VISION's own T2 photopic perceptual bar (C_thr),
  not an instrument-floor gate. Scoring an instrument-characterization
  leg against a perceptual threshold risks exactly the scope-tag-
  non-propagation pattern that has recurred across this program's history
  and once escalated to a Checkpoint firing.
- **RED TEAM** (numbered attacks, then overall ruling
  **PROCEED-WITH-MANDATORY-FIXES**): independently re-verified VISION's
  gate claim directly against code (`experiments/024.../run.py:40-44`) —
  **confirmed, load-bearing**. Found and independently confirmed a second
  load-bearing defect the Phase-1 draft did not catch: its Idealization 3
  falsely claimed θ=40° was already exercised by the trust-suite's stage-9
  gate list — checked directly against `lab/validation/run_all.py`: stage
  9's angle set is `(0, ±15)` plus a separate 30° wavelength check; θ=40°
  has never been gated. Also corrected: stage 9's current aggregate
  empty-identity gate is 0.005, not the stale 0.01 the Phase-1 draft cited
  (Iteration-1's original P-V1 number, since tightened). Adjudicated the
  five seats' asks: PHOTONICS' and EM's block additions ruled
  correctable/recommended (not load-bearing, not overreach); THERMO's and
  MATERIALS' asks ruled correctable, cheap, recommended. Two secondary
  citation errors caught and corrected (a self-contradiction in the
  Phase-1 draft's own §4a reasoning re-invoking a mechanism its own §1
  says was refuted; a function-name mix-up, `block_cpl40()` not
  `block_n17()`, for which function discards signed empty-scene data).
  VISION's own supporting statistic corrected (Checkpoint criterion 4 has
  fired **once**, Iteration 17 — not "4 of 5" as the critique stated; the
  underlying *pattern* of non-propagating scope tags has recurred across
  Iterations 13, 14, 15, 17, but only one escalated to an actual firing).
  No overreach found; nothing rejected. No unfalsifiable claims, no
  inexpressible mechanisms, no constraint-#N violation found anywhere in
  the proposal (confirmed: this leg touches no σ(I)/σ(x,t)/ε(ω)/gain
  parameter, so constraint 3 is not directly at stake this cycle).

## Phase 3 — Synthesis (Director)

**Accepted, implemented as stated:**

1. **VISION's flip, Red-Team-confirmed load-bearing** — `GATE_HARD = 0.001`
   is the ONLY threshold that scores PASS/FAIL in this experiment's
   Results section. `GATE_PERCEPTUAL_CONTEXT = 0.005`,
   `ADVISORY_BOUND_040 = 0.04`, and `STAGE9_EMPTY_GATE = 0.005` (corrected
   from the Phase-1 draft's stale 0.01) are reported every row, as labeled
   context, never as "the gate" (`design_geometry.py`).
2. **Red Team's own load-bearing catch** — Idealization 3 corrected: θ=40°
   was never previously exercised by any trust-suite gate (stage 9's set
   is `(0,±15)` plus a 30° wavelength check only). This leg is the FIRST
   trust-suite-adjacent measurement of this angle at any resolution.
3. **PHOTONICS' block addition** — Block OBJPRESENT added: sponge article
   (exp-024's own primary N9 article, `SIGMA_SPONGE` unchanged) at θ=±40°,
   600nm, 2 new runs, reusing Block MAIN's own empty(±40°,600nm) profiles
   for the contrast pairing (no redundant empty rerun).
4. **EM's block addition** — Block EXTEND added: θ∈{41,42,43}°, both
   signs, 600nm only, empty-scene-only, 6 new runs.
5. **THERMO's disposition request** — PLAN.md's two queued cheap THERMO
   add-ons (re-scoping `lab/thermo_sidecar.py`'s two known corrections and
   sourcing the six-cycle-unsourced ΔT anchor; docket #7's sourced
   witness-parameter table) are **DEFERRED to Iteration 19, explicitly, not
   by silent default.** Reason: this cycle's own budget is fully allocated
   to closing the two load-bearing gate/idealization fixes (items 1–2) and
   the two correctable block additions (items 3–4); folding in unrelated
   THERMO literature-sourcing/coding work would blur this leg's own
   tightly-scoped, zero-mechanism charter (§3 below) and risk exactly the
   kind of scope creep this cycle exists to audit against. Both items stay
   at their existing PLAN.md priority ranking, untouched.
6. **MATERIALS' cap** — a realizability-relevance cap sentence is added to
   §Results discussion (below, pre-committed): this leg's outcome, in
   either direction, cannot move either UNOBTANIUM-WITH-PARAMETERS verdict
   in `REALIZABILITY_MEMO.md`.
7. **Red Team's secondary corrections** — §4a's central-magnitude
   estimates (below) are stated as informed extrapolation from
   geometrically-adjacent evidence only, with no appeal to the
   MARGIN_MULT/fringe-ratio mechanism (exp-024's own P-M1 already refutes
   it as this floor's cause). Citation corrected: `block_cpl40()`
   (exp-034) discards signed `C_empty`, not `block_n17()` (exp-035, which
   retains it — the precedent Block OBJPRESENT/EXTEND both follow).
8. **VISION's own stat, corrected** — the program's Checkpoint criterion 4
   has fired **once** (Iteration 17); the underlying scope-tag
   non-propagation *pattern* recurred across Iterations 13, 14, 15, 17
   (each needing a Phase-5 catch), only one of which escalated to an
   actual firing. Stated accurately here and in `design_geometry.py`.

**Overridden: none.** Every mandatory and correctable fix from Phase 2 is
adopted; Red Team found no overreach to reject.

## Setup (`design_geometry.py` — copied verbatim from exp-024/design_geometry.py; re-run it if any constant moves)

| Knob | exp-024 (the geometry under audit) | exp-041 (this experiment) |
|---|---|---|
| Grid | Δ=30nm, courant 0.99, absorb 40, cpl {450:15,600:20,750:25} | **unchanged, verbatim** |
| Domain | 360 × 1584 (MARGIN_MULT=3.5) | **unchanged, verbatim** |
| Source | x=300, y∈[40,1544], taper 40 | **unchanged, verbatim** |
| Object center | (170, 792) | **unchanged, verbatim** |
| Windows | W_OBJ=78, guard→185, flank (185,263) | **unchanged, verbatim** |
| Sponge article | SIGMA_SPONGE = 0.10/(2·78) = 6.410×10⁻⁴ | **unchanged, verbatim — Block OBJPRESENT only** |
| **Angles (this leg's own contribution)** | ANGLES=(±40..0, 10°step, N9); FALLBACK=(±35..0, 5°step, N9, excludes ±40) | **MAIN: {36,37,38,39,40}×{±}, N=10, all 3λ. OBJPRESENT: {±40}, 600nm only. EXTEND: {41,42,43}×{±}, N=6, 600nm only.** |
| Decision floor | δ_C ≤ 0.001 hard gate (aggregate 9-angle) | **GATE_HARD=0.001, applied PER-ANGLE (a stricter, novel application of the same number — see Predictions)** |
| Steps | 1400 | unchanged |
| Runs | 124 (primary) | **38 new FDTD calls** |
| Runtime estimate | 390s (4 workers) | **≈95–150s (4 workers, 2 for the small OBJPRESENT block)** |

## T1 escape-route statement

**This experiment implements no escape mechanism.** No σ(I), σ(x,t),
angular-selectivity, or sub-threshold machinery is touched; `lab/ambient.py`
is unmodified. Block MAIN and Block EXTEND place no article in the grid at
all; Block OBJPRESENT places only the pre-existing, materially-unmodified
dilute-sponge article from exp-024's own primary run. This is pure
instrument characterization — closing a program-integrity gap (T20), not
advancing or retiring any T1 escape route. Constraint 3 is not directly at
stake this cycle (confirmed by Red Team).

## Predictions — committed before this experiment's first run

**P-M1 (Block MAIN, per-λ magnitude at θ=40°, the endpoint).** Extrapolated
from two geometrically-adjacent-but-distinct anchors (neither at exp-024's
own geometry): N17_NATIVE_V2 (exp-035, r=117 rescale, cpl=30, 600nm:
|C_empty(±40)|=0.0123/0.0127) and T16_CLOSE (exp-035, r=156, cpl=20,
600nm: 0.00069/0.00105, judged NOT self-similar to the r=78 family).
- 600nm: central **0.008**, band **[0.004, 0.016]**.
- 450nm: central **0.006**, band **[0.003, 0.015]**.
- 750nm: central **0.010**, band **[0.005, 0.020]** (set highest —
  exp-024's own N9-aggregate primary-vs-fallback gap was largest at
  750nm).
- **Falsification:** any λ's θ=40° reading outside its stated band.

**P-M2 (Block MAIN, shape across 36°→40° — REVISED per Red Team/EM's
mandatory fix into an explicit three-way falsifiable partition, replacing
the Phase-1 draft's single "sharp threshold" claim):**
- **(i) Generic-large-angle:** if θ=36° AND θ=37° both already breach
  GATE_HARD (0.001) at every λ — the floor is not "±40°-specific," it's
  large-angle-generic across this whole window, and T20's original framing
  ("something specific to ±40°") needs revisiting.
- **(ii) Localized-near-40° (the predicted/expected outcome):** θ=36–37°
  stay ≤0.001 at every λ, and the GATE_HARD crossing (positive side) falls
  within θ∈[38°,40°] — central estimate θ=**39°**.
- **(iii) Extrapolation failure:** even θ=40° stays ≤0.001 at every λ —
  the §P-M1 magnitude estimates are themselves wrong, and Iteration 2's
  original aggregate anomaly needs a different explanation (e.g. how the
  per-angle floor integrates across the full N9 angle *set*, not a single
  endpoint's raw magnitude) — a major, surprising finding if it occurs.

**P-M3 (Block MAIN, sign asymmetry).** Predict |C_empty(+θ)| and
|C_empty(−θ)| agree to within 30% relative at every θ∈{36..40}° — wide
enough to contain both prior precedents (3.4%, 34%) without being
vacuous. **Falsification:** any θ exceeding 30% asymmetry — kept in the
signed raw record as a new finding (candidate T21), not averaged away.

**P-EXT (Block EXTEND, θ=41–43°, 600nm).** Predict the floor continues to
rise monotonically past 40° (not a local maximum exactly at 40°) —
central estimate |C_empty(43°)| ≈ 1.3–1.6× |C_empty(40°)|.
**Falsification:** if 41–43° drop back below 40°'s own reading, that is a
genuine peak/resonance-like feature specific to θ≈40°, worth a dedicated
follow-up (not chased further this cycle).

**P-OBJ (Block OBJPRESENT, sponge @ ±40°, 600nm — PHOTONICS' own
falsifiable outcome partition).**
- **(a) Agrees:** |C(sponge,θ)| relative to the geometric-ceiling-
  consistent baseline tracks Block MAIN's own C_empty(θ,600) reading
  within T15's own established ~1–3% relative band. PHOTONICS' concern is
  answered negative this cycle — the empty-scene design's sufficiency
  claim stands for this specific check, T15's near-field-leakage channel
  does not measurably couple with the ±40° geometry.
- **(b) Diverges:** the object-present reading departs from the
  empty-scene reading by more than that band. PHOTONICS' concern is
  confirmed — N17's per-angle floor is object-dependent, not purely an
  empty-aperture artifact, and Block MAIN's own numbers alone cannot
  certify N17 safe for object-bearing scenes.
- **Self-consistency check (zero-cost):** `C_empty_paired` (recomputed
  from Block OBJPRESENT's own contrast call) must reproduce Block MAIN's
  own `C_empty` at the same (θ,λ) to numerical precision — an internal
  identity, not a physics prediction.

**Materials realizability cap (pre-committed, per MATERIALS' mandatory
fix):** whatever this leg finds, in either direction, it cannot move
either UNOBTANIUM-WITH-PARAMETERS verdict in `REALIZABILITY_MEMO.md` — RSA
falls 1–2 orders of magnitude short on dynamic range and TPA falls 9–12
orders of magnitude short on operating irradiance, both on grounds
independent of this bookkeeping channel. This leg's scope is limited to
correcting or reconfirming the exp-032/033 PASS→MARGINAL citation and its
downstream N17-dependent conclusions (leg (a)'s own enumerated list,
above).

## Idealizations

2D TMz, one polarization; CW single-λ per run. Graded damping bands, not
PML. Window MEANS, not point-wise B(y). **No object article in Blocks
MAIN/EXTEND** — measures the instrument's own floor only, makes no claim
about any escape route. **Single resolution only — no R3 cross-check this
leg**, flagged explicitly (per this program's own R3 meta-rule, a
surprising result here is a natural, cheap candidate for a future cpl
20→30 follow-up at this exact geometry, not committed now). **This leg
does not explain *why* θ≈40° might be special** — it localizes where
(and whether) the floor crosses GATE_HARD across 36°–43°, not the
underlying mechanism; a mechanism investigation (e.g. the deprioritized
GUARD_OUT-fringe-period sweep) stays a separate, unscoped follow-up.
**θ=40° was never previously exercised by any trust-suite gate** (Red
Team's corrected Idealization 3, verified against `lab/validation/
run_all.py`'s stage-9 angle set `(0,±15)` plus a separate 30° check) — this
leg is the first characterization of this specific angle at any
resolution, on this or any prior geometry that matches exp-024's own.
GATE_HARD (0.001) is applied here **per-angle**, a stricter and novel
application of exp-024's own aggregate 9-angle number — not itself
previously validated at single-angle granularity; this leg is exactly
that validation.

## Run plan

`python3 run.py` — 38 new FDTD calls (Block MAIN 30, Block OBJPRESENT 2,
Block EXTEND 6), ProcessPoolExecutor (4 workers for MAIN/EXTEND, 2 for the
small OBJPRESENT block), results written to `results.json`. Full bench
(`lab/validation/run_all.py --only 12346789`) reverified green before and
after (no `lab/` change, so this is a formality per house discipline, not
expected to move).
