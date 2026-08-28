# PHASE 5 — QUANTUM OPTICS REVIEW · Panel Iteration 63 · exp-086

*Fresh context, blind to all other seats' current-cycle Phase-5 reviews.
Charter this cycle, by T28-desk-cycle precedent (exp-085 Phase 5):
statistical-significance auditing. Read in full: PANEL.md; LOGBOOK.md lines
1–380 (RULED OUT, esp. R6–R11) and the complete T28 live-thread (Iterations
46–62, plus the CHECKPOINT entries); the full exp-086 record
(`phase1_proposal.md`, all five Phase-2 critiques including my own
`phase2_critique_quantum.md`, `phase2_redteam_audit.md`, `phase3_synthesis.md`,
`phase4_rescore.py`+results, `phase4_null_calibration_rerun.py`+results,
`phase4_null_calibration_controlled_comparison.py`+results,
`phase4_prior_citation_audit.py`+results, `NOTES.md`).*

## 0. Scope note

This is a zero-FDTD, model-internal instrument-repair cycle. Checkpoint
criterion 2 is correctly N/A, matching every T28 desk cycle since exp-069 —
nothing here bears on any phenomenon constraint. My own charter task: (1)
verify `phase4_rescore.py`'s own stride-phase implementation actually
reproduces what Phase 3 pre-registered, not a subtly different test; (2)
scrutinize whether the null-calibration controlled-comparison's "bit-identical
`max_r2_over_trials` at matched seed/N" is sufficient evidence the fix has
negligible effect, or whether it is a single-seed coincidence requiring
independent replication before it licenses a general claim.

## 1. Stride-phase implementation: independently re-derived, CONFIRMED correct

I read `phase4_rescore.py` §[3] directly (lines 247–295), not the surrounding
prose. The loop iterates `phase_start in (5.0, 7.0, 9.0)`, slices
`sub_results` at stride 3 starting from each phase's index, restricts to the
"recovered" set (`converged==True ∧ p_local_corrected≤6.0° ∧ r2_local≥0.30`
— exactly the criterion Phase 3 froze), and computes Spearman ρ plus an
**exact permutation p-value** for `n_rec≤8` by enumerating all `n!`
permutations of rank order and counting how many produce `|ρ_perm|≥|ρ_obs|-
1e-12`. This is algebraically the standard exact test for Spearman
significance at small n — not a t-approximation, not a bootstrap, not a
subtly different statistic than what Phase 1/Phase 2/Phase 3 all specified.

**Independent spot-check performed** (not a re-execution of the committed
script — a from-scratch Python re-implementation, permuting the raw
`p_local_corrected` VALUES by index across all 5040 permutations directly,
a different code path than the script's own rank-based enumeration):

| Phase (θc-start) | n | ρ | p_exact (script) | p_exact (my independent enumeration) |
|---|---|---|---|---|
| 5° | 7 | 0.8571 | 0.023809523809523808 | **0.023809523809523808** |
| 7° | 7 | 0.4286 | 0.3535714285714286 | 0.3536 (asymptotic cross-check) |
| 9° | 7 | 0.5357 | 0.2357142857142857 | 0.2357 (asymptotic cross-check) |

Phase 5° matches **bit-for-bit** between two independently-coded exact
enumerations (120/5040 permutations meeting the threshold both ways). I also
independently recomputed the recovered-set arithmetic directly from
`phase4_rescore_results.json::method_c_rescore.sub_results` (37 raw rows,
not any derived summary): 21/37=0.5676 total recovered, boundary set exactly
`θc∈{45,59,61,63,71,73}` (6/37) — matching Phase 1/Red Team/Phase 3's own
triply-independent figure, now a **fourth** independent reproduction. **No
test-swap found.** The implementation is the pre-registered test, correctly
coded, and the persisted results are what a correct run of it actually
produces — this is not a hand-typed or narrated figure (R4 discipline
satisfied by the script itself, not merely by NOTES.md's restatement of it).

One process note, not a defect: my exact-permutation cross-check used a
*different* code path than the script's own (permuting the raw period
values by index vs. permuting rank order) specifically so the match would be
a genuine independent confirmation rather than a re-execution of identical
logic — the practice R4/R6 exist to require.

## 2. The null-calibration controlled comparison: sound methodology, under-
evidenced generalization claim as filed — independently repaired this review

### 2.1 What the comparison gets right

`phase4_null_calibration_controlled_comparison.py` correctly diagnoses and
fixes a real methodological trap: `max_r2_over_trials` is an order statistic,
not N-invariant, so comparing exp-077's cited N=20,000 figure (0.5609)
against a fresh N=3,000 run (0.5180) at face value — which is what
`phase4_null_calibration_rerun.py` alone would have invited, and which
falsified Phase 3's own pre-registered `[0.56,0.78]` band on the low side —
conflates "did the fix change anything" with "did N change." Reconstructing
the pre-R11 buggy logic and running it at the *identical* seed=7/N=3,000
draw isolates the fix's own effect correctly: a genuine paired comparison,
not a confounded one. This is real, disclosed, mid-cycle self-correction
(NOTES.md states the falsifier band was missed and explains why), matching
this program's own house discipline for handling a pre-registered prediction
that turns out to test the wrong thing.

### 2.2 The gap: one seed cannot license "negligible effect" as a general claim

The reported result — `max_r2_over_trials` and `p_r2_ge_070` bit-identical
between old-buggy and corrected logic at seed=7/N=3,000, despite the bug
firing at 6.70% (201/3,000) — is asserted in NOTES.md as establishing the fix
has **"negligible"** effect on the statistics underwriting exp-077's REFUTE
framing. As filed, this rests on **exactly one noise realization**. That is
a genuine gap, for a reason specific to this seat's charter: `max_r2_over_
trials` is a maximum over 3,000 draws — its value is set by whichever ONE
trial happens to realize the highest R², and whether that trial happens to
be among the 6.70% that are boundary-pinned (and therefore fix-sensitive) is
itself a random event. A single seed showing the maximizing trial was
NOT among the affected 6.70% establishes the claim for that one draw, not in
general. This is not a hypothetical concern: this SAME cycle's own
`phase4_prior_citation_audit_results.json` documents a real case
(exp-078's `c80_c40`, on genuine signal, not noise) where the narrow-stage
vs. widest-stage R² for an all-boundary-pinned fit swings from **0.247 to
0.969** — a 0.72-absolute jump. Nothing in the committed record rules out a
noise draw where a boundary-pinned trial's R² jumps similarly and lands
above the current ~0.52 ceiling, which would move `max_r2_over_trials` and
potentially `p_r2_ge_070` materially — exactly the Checkpoint-4-relevant
falsifier Phase 3 itself pre-registered. **"Bit-identical at one matched
seed" is evidence toward "negligible," not proof of it; the committed
record states it as though it were the latter.**

### 2.3 Independent multi-seed replication performed this review

I built a from-scratch, independently-coded reimplementation of both the
old-buggy and corrected `free_period_with_widening_quiet` logic (computing
both stages once per trial and deriving both variants' `chosen` record from
the same underlying fits, for efficiency — a different code structure than
either of exp-086's own two scripts) and ran it across **8 seeds**
(7, 1, 2, 3, 11, 42, 99, 123) at N=1,200 trials/seed (9,600 pure-noise trials
total, ~591 boundary-pinned instances observed) on the real `real_delta_pad`
grid/σ:

| seed | old max R² | new max R² | diff | old/new p(R²≥0.70) | n boundary | largest boundary R² jump |
|---|---|---|---|---|---|---|
| 7 | 0.5180 | 0.5180 | 0.0000 | 0/0 | 81 | 0.099 |
| 1 | 0.5070 | 0.5070 | 0.0000 | 0/0 | 73 | 0.053 |
| 2 | 0.5024 | 0.5024 | 0.0000 | 0/0 | 77 | 0.079 |
| 3 | 0.5311 | 0.5311 | 0.0000 | 0/0 | 70 | 0.174 |
| 11 | 0.4960 | 0.4960 | 0.0000 | 0/0 | 80 | 0.188 |
| 42 | 0.5353 | 0.5353 | 0.0000 | 0/0 | 73 | 0.079 |
| 99 | 0.5352 | 0.5352 | 0.0000 | 0/0 | 66 | 0.156 |
| 123 | 0.5121 | 0.5121 | 0.0000 | 0/0 | 71 | 0.159 |

Seed 7 reproduces the committed result exactly at the same seed (0.5180
both, matching the committed N=3,000/seed=7 figure to the printed digit at
N=1,200 — consistent, not identical N, as expected). Across all 8 seeds:
`max_r2_over_trials` is bit-identical between old and corrected logic every
time, `p(R²≥0.70)` stays at exactly 0 for both every time, and the single
largest boundary-pinned R² jump observed across ~591 boundary instances
(0.188 absolute, seed 11) comes nowhere close to threatening the ~0.50–0.53
ceiling set by genuinely-converged trials, let alone the 0.70/0.7156/0.8165
thresholds that actually matter for exp-077's REFUTE framing.

**Ruling on this point: the substantive conclusion — the fix has negligible
effect on these null-calibration statistics — now stands independently
corroborated across 8 seeds by a second, independently-coded implementation,
and is very likely a genuine structural fact** (plausibly because a
boundary-pinned fit's R² ceiling under this quiet variant's own 2-stage,
`[1,15]°`-capped widening is intrinsically bounded well below what a
genuinely resonant interior optimum reaches — a mechanistic explanation this
review surfaces but does not fully derive). **But this was not established
by the committed record as filed** — NOTES.md's "negligible" language and
"cleaner, more decisive answer than the frozen prediction anticipated"
framing overstate what a single paired seed can support, for a
tail/order-statistic specifically, the exact class of claim R6's lineage
(ground-truth recovery, null-calibration, this program's own repeated
"one run is not a proof" lesson) exists to guard. This is the same
underlying shape as R6/R6-addendum, applied here to a *comparison* between
two null constructions rather than to a null construction's own
calibration — a genuinely new instance of the family, not a restatement.

**Also unresolved**: neither the committed N=3,000 run nor my own N=1,200×8
replication is the mandated **full N=60,001-call** appendix (Red Team's
mandatory fix 2, explicitly not closed by this cycle — disclosed correctly
in NOTES.md's own "Next" section as a standing Tier-2 item). My replication
raises confidence the eventual full-scale run will not surprise, but does
not substitute for it — the same disclosed-scope-reduction caveat the
committed record already carries applies equally to this review's own
check.

## 3. Other findings (secondary to charter, verified not overridden by any prior seat)

- **R11 fix correctness, independently re-verified a fifth time**: read both
  `y_wall_prescreen.py::free_period_with_widening` (lines 325–379) and
  `pad_round_trip_model.py::free_period_with_widening_quiet` (lines 367–396)
  directly. Both correctly implement "if every stage stays `at_boundary`,
  return the LAST (widest) stage's record, flagged `converged=False`" — the
  `for...else` Python idiom is used correctly (the `else` clause fires only
  when the loop completes without `break`, i.e. exactly the all-boundary
  case). Algebraically sound, matching every other seat's independent
  derivation.
- **Prediction-6 falsifier band miss, correctly disclosed, not silently
  absorbed**: `max_r2_over_trials=0.5180` falls *below* the pre-registered
  `[0.56,0.78]` band. NOTES.md states this plainly and explains it as an
  N-mismatch artifact (the band assumed the full-scale run), not a fix
  effect — verified correct by §2 above. This is honest handling of a
  falsified pre-registered number, matching house discipline, not a defect.
- **Prior-citation audit scope narrowing (077–085, not 069–085) is
  justified**, not a silent gap: THERMODYNAMICS' Phase-2 critique
  independently confirmed zero `free_period_with_widening` occurrences in
  experiments 069–076; `phase4_prior_citation_audit.py`'s own docstring
  states this reasoning explicitly. I re-confirmed via `grep -rl
  "free_period_with_widening" experiments/069-076/` myself: zero matches.

## Verdict: **PARTIAL**

Matching every T28 desk-repair cycle since exp-069 (Checkpoint criterion 2
N/A — no phenomenon-mechanism claim anywhere in this cycle). The R11 repair
is correctly implemented and independently re-verified at the source, a
fifth time over. The stride-phase significance fix is correctly coded,
reproduces the pre-registered predictions exactly, and is real, useful,
falsifiable methodology this program should keep using. The null-calibration
controlled comparison's core substantive finding (negligible fix effect) is
now materially better-supported than the committed record itself establishes
— but the committed record's own "negligible"/"cleaner, more decisive"
language outran its one-seed evidentiary base at the time it was written,
and the mandated full-scale (60,001-call) run remains genuinely unexecuted.
Nothing in this cycle corrupts any currently-cited T28 number; nothing here
closes or advances T28's own substantive ~2.84°-family mechanism question.

## Ranked candidate next steps (checked against LOGBOOK's RULED OUT R1–R11 — none re-proposed)

1. **Formalize a multi-seed replicate requirement for the null-calibration
   controlled comparison**, as a named, pre-registered addition analogous to
   R6/R6-addendum: before "negligible effect" or any comparable claim about
   a fix's impact on a tail/order statistic is cited as settled, run the
   matched-seed comparison at ≥5–8 independent seeds (this review's own
   8-seed/N=1,200 check, §2.3, can be formally adopted or superseded by a
   committed, larger version) — not a new experiment, a ~4-minute script
   addition to this cycle's own record before its "negligible" framing
   propagates into LOGBOOK.
2. **Execute the still-outstanding full N=60,001-call `null_calibration_
   appendix` run** (Red Team's own mandatory fix 2, explicitly not closed
   this cycle) — now doubly de-risked by both the committed N=3,000 check
   and this review's own 8-seed/N=1,200 replication, but not yet actually
   run at the scale the original REFUTE citation used.
3. **PHOTONICS' grazing-incidence model-validity question** (does
   `edge_diffraction_c_empty_corrected` remain inside its own valid
   near-field regime at the ~5,444×–6,631× `ptp`-growth sub-windows,
   θc≥59°?) — disclosed, not resolved, this cycle; bears directly on
   whether the "recovered" 21/37 windows are measuring genuine periodic
   structure at every θc or an artifact of a formula operating outside its
   valid regime, a statistical-conclusion-validity question adjacent to this
   seat's own charter.
4. **The joint EM/THERMO energy-interception cross-check**, now FOUR
   consecutive cycles deferred/exempt (083/084/085/086) — correctly exempt
   here (no article-loaded scene), but the next scene-bearing T28 cycle
   should treat this as approaching the same escalation shape R6–R10 named
   for other repeatedly-deferred items, per NOTES.md's own "Next" section.
5. **The x-wall wavelength-generality leg**, now ELEVEN consecutive cycles
   deferred (076–086) — the single oldest item on the whole T28 board,
   unrelated to this cycle's own statistical findings but overdue enough to
   name here.
