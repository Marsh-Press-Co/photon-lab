# exp-055 — The T25 Coherent-vs-Incoherent Ambient-Sum Bridge Gate (N=9 Equal-Amplitude)

Panel Iteration 32. Lead: **QUANTUM OPTICS** (rotation — "still owed" the
lead slot since Iteration 30's content-policy block; LOGBOOK.md Iteration
31's own closing line). Full seven-seat cycle: Phase 1 proposal (QUANTUM
OPTICS) → five blind parallel critiques (PHOTONICS, MATERIALS,
ELECTROMAGNETISM, THERMODYNAMICS, VISION SCIENCE — all support-with-changes)
→ Red Team last with everything (verdict: proceed-with-mandatory-fixes, 5
numbered attacks, 9-item docket) → this Phase-3 synthesis. Full verbatim
record: `LOGBOOK.md`, Iteration 32.

## Hypothesis

Not a mechanism proposal — pure diagnostic/instrumentation work, same
register as Iterations 2/4/5/6/20/22/25/26/27/29/31. **T25** (opened
Iteration 29, exp-052 Phase-5, QUANTUM OPTICS' own catch, Red-Team-elevated
to program scope): every constraint-3 `C` citation this program has ever
issued rests on `lab/ambient.py`'s incoherent intensity sum over N=9
EQUAL-amplitude single-source FDTD runs. The only prior empirical license
for treating that approximation as valid, exp-029's stage-11 bridge gate
(Iteration 6), tested a structurally DIFFERENT configuration — one strong
beam (amplitude=1.0) plus one weak off-axis probe (amplitude=√(2×10⁻⁴)) —
whose Cauchy-Schwarz ceiling (2.83% of the beam's own absorbed power) does
not bound the cross-term between nine EQUAL-amplitude sources, the actual
object every headline `C` value in this program's nine-iteration
constraint-3 record rests on. No geometry this program has ever run has had
the real instrument's cross-term empirically bridge-gated at the
configuration it is actually used in.

This build closes that gap: inject all nine of this program's own
`FALLBACK_ANGLES` (±35°, N=9) SIMULTANEOUSLY, equal amplitude, in one `Sim`,
at this program's own headline r=78 ambient scene, and compare the
resulting coherently-summed field against `ambient.py`'s own naive
incoherent-sum pipeline — the exact object every constraint-3 citation
depends on, not a stand-in.

## Setup

**Object**: `graded_black_shell` PEC-cored — `pec_disk(r=30)` then
`graded_black_shell(r_in=30, r_out=78, sigma_max=0.5, eps_max=1.0)` —
exp-024/052's own "absorber" construction exactly (Red Team Attack 1,
below; NOT the Phase-1 proposal's original hollow construction).
**Geometry**: exp-024's own r=78 fallback geometry, reused verbatim — NOT
exp-030's `GEOM[78]` (Director's Phase-3 fix 2, below). NX=360, NY=1584,
OBJ=(170,792), SRC_X=300, ABSORB=40, TAPER=40, W_OBJ=W_FLANK=78,
GUARD_OUT=185, PLANE_X=77 (sensitivity plane 15), cpl=20, λ=600nm,
courant_frac=0.99, STEPS=1400. Full design: `design_geometry.py`.

**20 new FDTD calls**: 9(empty)+9(absorber) individual single-source legs
(FALLBACK_ANGLES, amplitude=1.0 each) + 2 joint scenes (`empty_joint`,
`absorber_joint`, 9 simultaneous sources each, fixed zero relative temporal
phase — the engine has no random-phase kwarg; true incoherent-ensemble
averaging stays explicitly out of scope, the same disclosure exp-029 made).

## New suite stage (PANEL.md's house rule: new machinery ⇒ new suite stage
## with ≥1 absolute identity gate BEFORE results are trusted)

`lab/validation/run_all.py::stage19_n9_superposition()` — built and
syntax-checked this shift BEFORE any exp-055 number below was computed;
run (and its own gate outcomes recorded) BEFORE `run.py`'s first official
run, per exp-029's own precedent. Extends stage 11's exact Ez-phasor-sum
identity (Gates Q4/Q5) from N=2 → N=9 on stage 10/11's own canonical
compact scene (`graded_black_shell(240,120,0,32)`, 360×240, absorb=30,
cpl=20, 900 steps), plus a NEW third gate (Red Team's docket item 7,
THERMODYNAMICS' own Phase-2 catch): stage 11's own Gate Q6 (radial closure
vs. box-ledger absorbed power), generalized from N=2 to N=9, on the joint
(9-source) object scene — stage 11's amplitude-ASYMMETRIC pair had an
implicit Cauchy-Schwarz amplitude bound the equal-amplitude N=9 case does
not share, so this closure check is load-bearing, not decorative.

## Phase 3 — accepted / overridden (Director's synthesis)

Red Team's verdict: **proceed-with-mandatory-fixes**, 5 numbered attacks,
9-item docket. **All 9 items ACCEPTED, zero overridden.** Full record:

1. **[Attack 1, inconsistency, LOAD-BEARING] The Phase-1 proposal's r=78
   "absorber" article was HOLLOW and claimed "inherited unchanged from
   exp-020/024/030/052" — verified FALSE by Red Team against source.**
   `C78_ESTABLISHED` traces to exp-024's own NOTES.md fallback table;
   exp-024's `run.py` (identical at the relevant lines to exp-020's) builds
   "absorber" as `pec_disk(r_in=30)` THEN `graded_black_shell(r_in=30,
   r_out=78)` — **PEC-cored**. Only exp-030's own `build_ambient` used
   hollow, a defect exp-052 itself already diagnosed and reversed
   (`experiments/052-.../NOTES.md` Fix 1). MATERIALS' own Phase-2 critique
   caught the same underlying fact (exp-052's headline articles are
   PEC-cored) but mischaracterized `C78_ESTABLISHED` itself as "the hollow
   number, never measured" — Red Team independently verified
   `C78_ESTABLISHED` IS the PEC-cored, actually-measured (exp-024) anchor.
   **Fixed:** the r=78 legs (individual AND joint) build the PEC-cored
   article, matching exp-024/052's own construction exactly.
2. **[Attack 1] Strike "inherited unchanged" framing.** **Fixed:** this
   NOTES.md and `design_geometry.py`'s own header state the true chain
   (exp-020/024 PEC-cored → exp-030 hollow, a diagnosed defect → exp-052
   PEC-cored again, corrected).
3. **[Attack 1] Pre-registered reproduction check added.** **Fixed:** the
   naive-incoherent sum of the new PEC-cored legs is checked against the
   established single-λ anchor before any coherent-vs-incoherent deviation
   number is trusted (P-055-6, below).
4. **[Attack 3, inconsistency/unfalsifiable-band] Outcomes 1/3's "3×–100×
   of exp-029's own finding" heuristic is ungrounded — PHOTONICS' rescaling
   citation (exp-046's grating-lobe replicas, 41.7–68.0%) is the wrong
   instrument (a different physical mechanism — undersampled coherent-beam
   array-factor sidelobes, not a fixed-window N=9 cross-term); EM's
   independent Cauchy-Schwarz re-derivation is correct and
   THERMODYNAMICS-corroborated.** **Fixed:** the formal ceiling is now
   EM's re-derivation — for N=9 equal-amplitude sources, deviation from the
   incoherent baseline ∈ **[−100%, +800%]** (=(N−1)×) — stated as the
   passivity bound (near-certain to hold, not discriminating), with a
   separately-labeled informal central estimate (below).
5. **[Attack 4, unfalsifiable] Outcome 2's ΔC band was never derived from
   anything.** **Fixed:** relabeled informational-only, no formal ceiling
   derived (Red Team's own sanctioned option) — Weber contrast is a RATIO
   of two independently-perturbed window means; whether a common
   multiplicative factor cancels (making C far more robust than raw flux)
   or the two windows see uncorrelated local interference (comparable
   ceiling to flux) is genuinely open, not asserted either way.
6. **[VISION, confirmed by Red Team] "T24" mis-cites the perceptual
   threshold — C_thr(L)=0.005 (photopic) is pinned in T2, not T24 (T24 is
   an unrelated EM/Red-Team instrument-noise thread on `C_empty`).**
   **Fixed:** citation corrected to T2; explicit statement added (below)
   that no outcome this cycle can move any existing Tier-A/Tier-W verdict.
7. **[THERMODYNAMICS, confirmed by Red Team, LOAD-BEARING] Stage 19 (as
   originally scoped) had only the field-identity gate — a real regression
   vs. stage 11's own Gate Q6 precedent, since N equal-amplitude
   zero-relative-phase sources are NOT amplitude-bounded the way stage 11's
   asymmetric pair was.** **Fixed:** stage 19 gets a third gate, the
   N=9 generalization of Gate Q6 (radial closure vs. box-ledger absorbed
   power on the joint object scene, ≤1.5% reused tolerance) — implemented
   in `lab/validation/run_all.py::stage19_n9_superposition()`.
8. **[Attack 2] MATERIALS' own critique record mis-cited
   `REALIZABILITY_MEMO.md` Entry 2 as having asked for this build —
   verified false (Entry 2 is exp-048's witness-scale dimensional-analysis
   memo, unrelated to this thread).** **Fixed:** noted here; does not
   change MATERIALS' "not applicable" realizability-tier disposition, which
   stands on its own merits (no new material/mechanism proposed).
9. **[Attack 5, cosmetic] "Iteration 31's own closing line named QUANTUM as
   Iteration 32's lead 'still owed' THIS BUILD" overstated the source — the
   closing line names QUANTUM as owed the LEAD SLOT (rotation), not this
   build by name.** **Fixed:** phrasing corrected throughout (T25's #1
   ranking is separately, correctly sourced: PLAN.md's Iteration-32+ queue,
   item 1, "QUANTUM #1" among 5 of 6 exp-052 Phase-5 seats).

**Director's own Phase-3 catch, not raised by any Phase-2 seat or Red
Team**: the Phase-1 proposal's cited anchor, `C78_ESTABLISHED['absorber']
= −0.72087`, is a **photopic-luminosity-weighted average across
450/600/750nm**, while this cycle is single-λ=600nm scope. The correct
single-λ anchor is `_C78_RAW['absorber'][600] = −0.7211` (exp-024's own
NOTES.md fallback table) — a ~0.03% relative difference from the
V-weighted figure, small but a real citation-precision fix, applied
throughout (`design_geometry.py::C78_ABSORBER_600_ESTABLISHED`). Separately
disclosed (not "fixed" — the pre-registered check IS the actual test): the
geometry that produced `C78_ESTABLISHED` is exp-024's OWN original fallback
geometry (NY=1584, OBJ=(170,792), GUARD_OUT=185) — **not** byte-identical to
exp-030's own `GEOM[78]` (ny=1528, obj=(170,764), guard_out=186), which
exp-030/052 reused as "the r=78 geometry" without ever re-deriving
`C78_ESTABLISHED` from it. This build uses exp-024's own geometry directly
(not exp-030's r-family formula), so this cycle's own reproduction check
(P-055-6) tests exactly ONE variable (coherent vs. incoherent), uncomplicated
by an unrelated geometry-formula drift whose own significance is a separate,
unaddressed question — named for a future cycle, not chased here.

## T1 escape-route statement

No escape mechanism implemented or claimed — pure diagnostic/instrumentation
work, same register as Iterations 2/4/5/6/20/22/25/26/27/29/31.

## Predictions — committed before this experiment's first (`run.py`) run

**Suite gates (stage 19, must PASS before anything below is trusted):**
- **P-055-5a/5b (Gates, N=9 field-identity, vacuum + object):** ≤1×10⁻⁶ RMS
  relative gate (reused stage-11 tolerance); central estimate
  **1×10⁻¹⁴–1×10⁻¹³** (one order looser than stage 11's own N=2 figure —
  more accumulated sources/round-off — but far inside the gate).
- **P-055-5c (Gate, N=9 radial closure vs. box-ledger, joint object scene):**
  ≤1.5% gate (reused stage-10/11-calibrated tolerance); central estimate
  **0.2%–1.5%**, matching exp-028/029's own established closure range at
  this exact canonical-scene family.

**Reproduction (precondition for everything below, Red Team's mandatory
fix 3):**
- **P-055-6:** naive-incoherent `C` (9 individual legs, PEC-cored absorber)
  reproduces `C78_ABSORBER_600_ESTABLISHED = −0.7211` to **≤0.5% relative**
  — a deterministic FDTD rerun of the same construction/geometry/steps as
  exp-024's own committed run, expected to land far inside this tolerance
  (likely to many more digits); the tolerance is generous, not
  discriminating, precisely because this precondition must not itself
  become an ambiguous result.

**Coherent-vs-incoherent deviation (the actual T25 question):**
- **P-055-1 (raw flux/intensity deviation, object-window, both legs placed
  on the naive pipeline's own normalized scale):** **Formal ceiling**
  (EM's Cauchy-Schwarz re-derivation, Red-Team-confirmed,
  THERMODYNAMICS-corroborated, `design_geometry.py::DEVIATION_CEILING_{LO,
  HI}`): deviation ∈ **[−100%, +800%]** — near-certain to hold, a passivity
  bound not a discriminating test. **Informal central estimate** (clearly
  separate, NOT rigorously derived — no seat produced one that survived
  Red Team's audit; PHOTONICS' own grating-lobe analogy was ruled
  inapplicable): **1%–15%**, reasoning by loose analogy to exp-029's own
  measured ~126–152× suppression of its aggregate cross-term below ITS OWN
  Cauchy-Schwarz ceiling (applying a comparable suppression factor to the
  800% formal ceiling here gives ≈5–6%; widened to 1–15% to reflect low
  confidence in transferring a suppression factor measured on a
  structurally different 2-source configuration). Sign not committed.
- **P-055-2 (Weber `C` deviation, informational only, no formal ceiling
  derived — Red Team's mandatory fix 5):** `|C_joint − C_naive|`, no
  pre-registered band. **Explicit statement (VISION's mandatory fix 6):**
  `C_thr(L)=0.005` is pinned in **T2**, not T24; r=78's naive `C≈−0.7211`
  sits ~144× above `C_thr` — **no outcome this cycle is expected or able to
  change any existing Tier-A/Tier-W constraint-3 verdict**; the value here
  is validating shared bridge-gate machinery for future near-threshold
  geometries, not rescoring this one.
- **P-055-4 (empty-scene identity check, informational, no formal ceiling
  derived, same reasoning as P-055-2):** `|C_empty,joint − C_empty,naive|`,
  informal central-estimate range **[0.0001, 0.01]** (order-of-magnitude
  guess, unbounded formally) — tests whether this program's own T24
  instrument-noise systematic on `C_empty` (0.002–0.007, `ABSORB`-boundary
  related) is joined, dwarfed, or swamped by a distinct coherent-injection
  systematic of comparable or larger size.

## Idealizations

Fixed (zero) relative temporal phase across all nine sources — a
single-realization COHERENT measurement, NOT ensemble-averaged incoherent;
true mutual incoherence needs random-relative-phase multi-draw averaging,
no `add_line_source` phase kwarg exists for it, unbuilt, explicitly out of
scope (identical disclosure to exp-029). 2D TMz, single λ=600nm, no
chromatic sweep of this gate. PEC-cored `graded_black_shell` article only
(exp-024/052's own construction) — the hollow construction (exp-030's own,
diagnosed as a defect) is not tested here at all. Single geometry (r=78)
only; r=156/312 untested, named for follow-up. Reuses exp-024's own
geometry directly, not exp-030's r-family `GEOM[78]` formula — see
Director's Phase-3 note above for why, and for the disclosed, unaddressed
question of whether `GEOM[78]`'s own small drift from this geometry matters
elsewhere. T11 (box-ledger decision-floor characterization) not folded in —
standing cross-cutting caveat, unaffected by this cycle. P-055-1's informal
central estimate is explicitly NOT a rigorous bound — stated as low
confidence, by analogy to a structurally different prior measurement.

## Realizability bound (Materials' seat duty)

Not applicable — no new material or mechanism is proposed; the object
reuses exp-024/052's own PEC-cored `graded_black_shell` construction
verbatim. The realizability question this cycle answers is purely
instrumental: does the engine's existing N-source list correctly implement
linear superposition at N=9, and how large is the coherent cross-term the
program's own incoherent-sum instrument has always silently approximated
away — answered by machinery already present at N=2 (stage 11), extended
here, zero new material physics.

## Results

*(to be filled in after Phase 4 — this section is written and committed
BEFORE any run, per house discipline)*

## Next (pre-registered, for Phase 5)

*(to be filled in after Phase 4)*
