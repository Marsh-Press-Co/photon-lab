# PHASE 3 — SYNTHESIS · Director · Panel Iteration 59 · exp-082

**Role: Director** (synthesizes, does not vote). Read the complete Phase 1
record (`phase1_proposal.md`, `NOTES.md`, `run.py`, `results.json`,
`run_output.txt`, `x_wall_realizable_refit.py`/`_results.md`/`_results.json`/
`x_wall_output.txt`, `phase_convention_extension.py`/`_results.md`/
`_results.json`/`_output.txt`), all five blind Phase-2 critiques, and Red
Team's Phase-2 audit (`phase2_redteam_audit.md`) in full before writing this.
Also read `experiments/081-.../phase3_synthesis.md` as the direct ancestor's
format/discipline model (not copied) and LOGBOOK.md's own established
precedent for a no-freeze-needed fold-in cycle (Iteration 56/exp-079's
Phase 3: "No FROZEN PREDICTIONS git-commit-before-run cycle was needed...
none of the 9 items touch any already-computed Test-A number"; Iteration
57/exp-080's Phase 3 uses the identical shape: "no FROZEN-PREDICTIONS
freeze cycle needed... a confirmatory fold-in, not a fresh prediction").
**Citation correction, stated for the record, not a re-litigation**: this
cycle's own task brief cited this precedent as "Iteration 53 (exp-076)";
independently checked against LOGBOOK.md directly, the precedent's own
exact language lives in Iteration 56 (exp-079) and Iteration 57 (exp-080),
not Iteration 53 — Iteration 53 (exp-076) is the `PAIR_PAD` discovery
cycle itself (the finding this cycle's own item 7 build tests), a
different entry. The reasoning the brief invokes is sound and applies
here regardless of which iteration number carries it; corrected here per
this program's own R4 citation discipline, not as grounds to change the
substantive call.

## 1. Disposition of Red Team's Phase-2 audit

Red Team's ruling: **PROCEED-WITH-MANDATORY-FIXES**, a 6-item prioritized
fix docket (`phase2_redteam_audit.md` §3), zero overrides of any of the
five blind critiques' overall verdicts (all five filed support-with-changes;
Red Team concurs support-with-changes for all five), one specific numeric
sub-claim inside one critique corrected (VISION's own "≈4.2×" secondary-
metric figure, shown not to reproduce from VISION's own stated operands;
corrected to ≈2.77×, Attack 5).

**The Director adopts Red Team's audit in full — all six fix-docket items,
zero overrides.** This is not a rubber stamp. The audit independently
reproduced every existing number in `results.json`, `x_wall_realizable_
refit_results.json`, and `phase_convention_extension_results.json` bit-exact
(§0a–0c, 0m of the audit) before adjudicating anything. It then went
substantially beyond either critique that raised the correlation concern
(PHOTONICS, EM): it ran an exact 7!-permutation test on the observed Pearson
r (§0g), a lag-tolerant cross-correlation search (§0h), the sub-thread's own
real free-period-search machinery on both series directly (§0i), a
ground-truth check against exp-076's own independently-known-correct
31-point period (§0j), and a 200,000-trial null-permutation control on that
search's own R² (§0k) — four independent lines of evidence, not one, all
converging on the same conclusion and all reproducible from primitives
already in the committed record. It also caught and corrected an arithmetic
error inside a Phase-2 reviewer's own "correction" (VISION's own "≈4.2×"
figure, Attack 5) — with the audit's own re-derivation (≈2.77×) laid out
step-by-step and independently checkable — and confirmed a governance
finding (VISION's git-provenance flag) as real and, checked directly,
*worse* than VISION's own description (Attack 6). This is a rigorous,
evenhanded audit with no self-serving asymmetry — it corrects a critique
that itself exists to correct the primary record, in the same direction
(toward less overclaiming) both times, exactly matching this program's own
established practice of adopting a non-self-serving Red Team fix docket in
full (exp-080 Iteration 57, exp-081 Iteration 58, among others) rather than
re-litigating findings Red Team has already independently re-derived from
primitives.

## 2. Why no FROZEN-PREDICTIONS git-freeze cycle is needed this cycle

Every one of the six fix-docket items is a prose/framing correction to an
already-computed, already-independently-verified number — none requires new
FDTD, and none touches a quantity whose value is still unknown at synthesis
time:

- Item 1 restates what `ratio=0.6573` (§0a, exact) does and does not
  establish, using numbers Red Team already computed from data already in
  `results.json` (§0d–0k) — no new computation, only corrected prose.
- Item 2 restricts existing generalizing sentences to their actually-tested
  scope (the flagship article) — a scoping correction, not a new result.
- Item 3 relabels an existing ratio and reports Red Team's own already-
  computed ≈2.77× figure (§0l) alongside the existing ≈5.5× and T16's own
  historical ≈0.12× — three already-known numbers, correctly labeled.
- Item 4 merges two already-filed findings into one open question — no new
  arithmetic.
- Item 5 states a standing rule for *future* FDTD spend; no FDTD is spent
  this cycle.
- Item 6 requires no action.

This is the identical shape LOGBOOK.md's own Iteration 56 (exp-079) and
Iteration 57 (exp-080) precedents establish for when a fold-in cycle needs
no FROZEN-PREDICTIONS git-freeze: "a confirmatory fold-in, not a fresh
prediction." No new number is committed to git as a prediction here because
no new number is computed here — the fixes are folded directly into the
committed record, then Phase 4 verifies the corrected record accurately and
completely reflects Red Team's own §0 findings.

## 3. Fix docket — disposition of all six items

### Item 1 [HIGH] — mechanism-continuity language corrected

`NOTES.md`'s "Learned" §1–2 and `phase1_proposal.md`'s "PHASE 1 RESULTS"
VERDICT/Combined-self-score language are revised in place (this document's
own companion edit) to state precisely: **SURVIVES stands MECHANICALLY** —
the pre-registered `ratio = A_scene/A_empty = 0.6573` computation is
correct, reproduces bit-exact against `results.json`, and sits centrally
inside the pre-registered `[0.5,2.0]` band (Red Team §0a). **The
mechanism-continuity reading — "the PAD confound reaches the real scored
channel," "the same lossless phase artifact reaches the scored channel" —
is NOT established, and is shown, not merely suspected, to be UNRESOLVABLE
at this cycle's own 7-point statistical power.** Four independent lines of
evidence, all from `phase2_redteam_audit.md` §0, cited as the source (not
re-derived here, per R4 discipline — this record points to where these
numbers were independently computed):

(a) **Exact permutation test**: `p=0.953` two-sided (not asymptotic) on the
observed `r=0.0306`; the exact critical value at α=0.05, n=7, is
`|r|≥0.746` — roughly 24× the observed magnitude (§0g).

(b) **Divergent free periods**: the sub-thread's own established
`free_period_with_widening` machinery, run directly on both series, gives
`delta_scene` P*=2.940° and `delta_empty` P*=1.015° — a 190% relative
divergence (`rel_dev=1.896`), not a shared period (§0i).

(c) **Ground-truth check**: `delta_empty`'s 7 points are bit-identical
(independently confirmed, §0b) to `experiments/076-.../results.json`'s own
committed `PAIR_PAD` data, whose TRUE established period — the full
31-point fit already reused this cycle in the x-wall refit — is
`4.611289746337977°`. The 7-point reduction recovers `1.015°` instead: a
78% miss, with a spuriously high R²=0.864 alongside it (§0j).

(d) **Null-permutation control**: 200,000 trials of Gaussian noise at each
series' own measured σ, run through the identical real free-period search,
show `P(R²≥0.858)=0.272` for `delta_scene`'s own R² and `P(R²≥0.864)=0.257`
for `delta_empty`'s — roughly a quarter of pure-noise 7-point series clear
the same bar both real series clear (§0k).

Together these do not establish that the two series are unrelated either —
that would require power this instrument does not have at n=7. The honest
finding, exactly as Red Team's own Attack 1 states it, is a third, sharper
one: the shape/mechanism-identity question is demonstrated to be **below
this instrument's own resolving power**, independent of which way the true
answer lies — not merely "not yet resolved," and not merely "weakly
supported." `phase2_redteam_audit.md` §0d–0k is appended in force by
reference from both `NOTES.md` and `phase1_proposal.md`'s corrected
sections.

### Item 2 [HIGH] — article-generality scoping corrected

Every generalizing sentence in `NOTES.md`/`phase1_proposal.md` is revised
to scope explicitly to **the flagship, strongly-absorbing article class**
(`materials.graded_black_shell` + `pec_disk`, `C≈−0.55`, ~100× past
`C_thr` by design) — no claim survives about "real absorbing articles" in
general, or about the channel itself independent of which article occupies
it. `NOTES.md`'s "Next" section now names the near-null σ(I) article
follow-up as a standing item: MATERIALS' own flip condition (`off_pass`,
`τ_off≈0.0065`, exp-032/exp-034) — rerun the identical `PAIR_PAD`/C40–G40
harness with `build_article` replaced by that construction, and check
whether `ratio`/`A_scene/C_thr` land in a comparable range. Per this task's
own scope, this is recorded as a named "Next" item in `NOTES.md`, not added
to `PLAN.md`'s queue — that board edit is the Director's own Phase 5 job,
not this Phase 3/4 pass.

### Item 3 [HIGH] — secondary-metric comparator corrected

`A_scene/C_thr=0.6815` is relabeled explicitly as an **instrument-
uncertainty-budget number**, not a perceptual-detectability claim — per
VISION's own request (Attack 4), adopted in full, and per VISION's own
T3-precedent argument: `C_thr` is a static-scene JND threshold; `A_scene`
is peak-to-peak of a *difference between two numerical domain-treatments*
of the same scene, swept across angle — no human views that quantity
directly, a different KIND of quantity even though the units (dimensionless
Weber contrast) match. The single "5.5×" framing is replaced with all three
correctly-labeled figures, per Red Team's Attack 5 disposition (VISION's
own "≈4.2×" correction is overridden — it does not reproduce from its own
stated operands; the audit's own independent re-derivation is cited
instead):

| Comparator | Value | What it measures |
|---|---|---|
| Naive / mismatched-convention | ≈5.538× (`5.5×`) | `A_scene/C_thr` divided by T16's raw single-sided fitted-carrier amplitude `√(A_i²+A_q²)/C_thr` — divides a peak-to-peak quantity by a single-sided-amplitude quantity; a convention mismatch, disclosed as such, not corrected out |
| Properly like-for-like (ptp-to-ptp) | ≈2.769× (`≈2.8×`) | `A_scene` divided by T16's own figure doubled to its ptp-equivalent (`2×6.1530×10⁻⁴=1.2306×10⁻³`) — the audit's own independent re-derivation (`phase2_redteam_audit.md` §0l), cited here, re-verified against `experiments/076-.../results.json::carrier_diagnostics_PAIR_PAD` directly rather than recomputed independently a third time |
| T16's own historical empty-scene-only reading | ≈0.12× | `√(A_i²+A_q²)/C_thr` at Iteration 54/R9 — the pre-existing, already-corrected empty-scene-only figure this cycle's result is compared against |

Each figure measures a different thing; none is a claim that the artifact
itself is "N% of the way to visible." The record states this explicitly.

### Item 4 [MEDIUM] — mechanism-identity findings merged

THERMODYNAMICS' own attack (`PAIR_PAD`'s losslessness was proven
empty-scene-only, in `lab/fdtd2d.py`'s damping-mask construction, never
re-verified with a real absorber sitting in the coherent echo's own
round-trip path) and Item 1's own shape-evidence finding are the SAME
underlying open question asked from two different charter angles —
energy-accounting and statistical-shape — per Red Team's Attack 3. Both
are merged into ONE "mechanism-identity: open" note in `NOTES.md`, not
carried as two independent footnotes. Neither line of evidence alone
settles it; together they converge on "genuinely open, not merely
under-checked."

### Item 5 [MEDIUM] — standing rule stated, no action needed this cycle

No new FDTD is required by this docket, so no FROZEN-PREDICTIONS commit is
needed this cycle (§2 above). The standing rule this fix-docket item
establishes, stated explicitly for the record: **any future FDTD spend on
this construction must have its frozen predictions committed in a commit
genuinely separate from, and strictly before, the run's own results.**
This exact pattern — predictions and an already-executed (or
already-partially-executed) run landing in the same commit — has now
recurred twice at Phase 1 (exp-081's own Iteration 58, flagged by that
cycle's own VISION seat; exp-082's own Iteration 59, commit `5bb78df`,
where the FDTD run was already 27/29 calls complete when the predictions
text was committed, per Red Team's own Attack 6 finding, worse than
VISION's Phase-2 description of it). PANEL.md's literal git-before-run
mandate binds Phase 3's FROZEN PREDICTIONS commit specifically, not Phase
1, so neither instance is a rules violation — but per Red Team's own
Attack 6, a third recurrence should not be treated as a close call.

### Item 6 [LOW] — no fix needed, noted for completeness

Independently re-verified correct already, per Red Team §0 and direct
inspection this Phase-3/4 pass: the reproduction precondition
(`max_dev=0.0`, §0b), the settling precondition (both the committed
θ=39° check and EM's own independent θ=38°/STEPS=4200 corroboration),
the x-wall realizable-admittance refit's own "2 of 4 cells flip, none to
SUPPORT" self-scoring (§0m, `x_wall_realizable_refit_results.json::
verdict_flips`), and the phase-convention tie-breaker extension's own
"genuinely inconclusive, `[CALIB]` reliability precondition fails" self-
scoring are all correct as recorded. No edit made to any of these sections.

## 4. Corrected headline framing (what SURVIVES means now)

**SURVIVES** in this record's corrected sense means: on the flagship,
strongly-absorbing article class only, the pre-registered `ptp`-amplitude-
ratio computation between the real, article-loaded Weber-contrast channel
and the empty-scene proxy channel lands at `0.6573`, centrally inside the
pre-registered `[0.5,2.0]` band — a comparable-*scale* oscillation is
present on the real scoring channel, mechanically, reproducibly, and
decisively (not a boundary call). It does **not** mean the same
lossless-phase mechanism identified in Iteration 53's empty scene has been
shown to persist once a real absorber sits in the coherent path — that
question is open, and this cycle's own instrument, independently
demonstrated by Red Team from four separate lines of evidence, cannot
resolve it at n=7. Phase 5 reviewers should read this cycle's result as:
the practical risk this nine-cycle sub-thread carried without ever testing
against a real article — that a background/instrument confound might
vanish under object-minus-flank subtraction — is retired for the flagship
article class specifically; whether it is the SAME confound, unchanged in
mechanism, or a new article-mediated interaction of similar scale, remains
a named, convergent, open question for a future full-power (31-point) test.

## 5. Gates

Zero `lab/` changes this cycle (Phase 1, Phase 2, or this Phase 3/4 pass) —
confirmed by `git diff --stat -- lab/` (empty) and re-confirmed at Phase 4
below. The house trust suite (`lab/validation/run_all.py --only
12346789`) is re-confirmed green at Phase 4. No `lab/` diff this cycle means
no new trust-suite stage is required by house discipline.

## 6. Checkpoint ruling (re-reasoned through by the Director; no criterion
## changes from Red Team's own Phase-2 ruling)

- **Criterion 1**: N/A — zero constraint-3 engagement, T1 stated N/A
  throughout, confirmed by direct grep (Red Team §1 closing paragraph).
- **Criterion 2**: N/A, not merely not-yet-ripe — this cycle is
  instrument-fidelity/generalization work, not a mechanism-class claim.
- **Criterion 3**: N/A — zero new `lab/` machinery, `assert_lab_clean()`
  passed in `run.py`'s own execution.
- **Criterion 4**: does not fire — conditioned explicitly, per Red Team's
  own ruling, on this document adopting the fix docket in full, which it
  does. The overclaiming language Red Team flagged is corrected here, not
  carried forward unreconciled.
- **Criterion 5**: not at risk — this cycle discharges the six-cycle
  tripwire on item 7 and produces the sub-thread's first-ever article-loaded
  FDTD measurement, plus a genuinely new, independently-verified
  instrument-limitation finding (Red Team §0i–k) with implications beyond
  this one result.

## 7. Git provenance for this cycle

Per §2/§5 of this document: no FROZEN-PREDICTIONS freeze-then-run split is
needed, because every fix is a prose/framing correction to already-computed,
already-independently-verified numbers — the same shape LOGBOOK.md's own
Iteration 56 (exp-079) and Iteration 57 (exp-080) precedents establish for
when a fold-in cycle needs no such split. This document, the corrected
`NOTES.md`/`phase1_proposal.md`, and everything else touched this cycle are
committed together as ONE commit — stated explicitly in the commit message,
citing this exact reasoning.

Full record: `experiments/082-t28-pad-real-article-check/` —
`phase1_proposal.md`, `NOTES.md`, `run.py`, `results.json`,
`run_output.txt`, the x-wall refit and phase-convention-extension files,
all five Phase-2 critiques, `phase2_redteam_audit.md`, and this document.
