# PHASE 5 — REVIEW · QUANTUM OPTICS · Panel Iteration 47 · exp-070

Fresh sub-agent, QUANTUM OPTICS charter (PANEL.md seat 5): "non-classical
absorption, state-dependent or coherent interactions." Blind to any other
seat's Phase-5 review this cycle (one sibling file,
`phase5_review_thermodynamics.md`, exists on disk — not opened). Note for
the record: this seat authored the Phase-1 proposal under review, as lead
by rotation; this review holds it to the same independence standard as any
other seat's work, including its own corrected design choices.

## 0. Independent reproduction

`python3 desk_check_mechanism.py`, re-run from a clean copy of
`results.json`, reproduces every field **bit-for-bit** — `diff` against the
committed file is empty. Beyond re-running the committed script, I built a
second, independently-coded reimplementation of the search space and the
null-permutation control (different code structure: vectorized
broadcasting instead of the committed per-trial loop) and confirmed:
search-space size (36,680 expressions / 7,179 distinct values), all three
real-target `best_rel` values, the RNG draw sequence, and all three
`null_p` values (0.2039 / 0.8055 / 0.4969) match to the digit. **No
computational defect found anywhere in this batch.**

## 1. Is `N=20,000` the right precedent to match?

**Finding — the stated justification conflates two structurally different
null tests; the resulting choice is harmless, but the citation is wrong.**
Docket item 2 (`phase2_redteam_audit.md` ruling 2) sets `N=20,000` "matching
T28's own founding permutation test exactly... for direct
precedent-consistency." I traced that precedent
(`experiments/069-.../phase5_review_quantum.md` §3, this seat's own prior
cycle): it drew 20,000 noise realizations and, **for each one, re-ran a
400-point grid search** over `P*∈[1°,4°]`, to test whether the *fringe fit's
own R²* is significant against the look-elsewhere risk of a 400-candidate
period search. Exp-070's null test draws 20,000 random *targets* and, for
each, searches a **36,680-expression** combinatorial space for the closest
match — a different statistic (closest-match distance, not fit R²) over a
space ~92× larger. The two "N=20,000"s count different things: number of
noise draws in one case, number of null-target draws in the other; neither
test's `N` needs to scale with the *other* test's per-trial search-space
size, because in both constructions the per-trial search is evaluated
exhaustively, not sampled — enlarging the per-trial space does not create a
need for more outer trials, only tighter resolution at the outer level
does. So "the search space is 92× larger, therefore N should be larger" is
not actually a valid inference from that space-size fact alone.

**What actually determines whether `N=20,000` is adequate:** Monte Carlo
resolution of the percentile estimate near the `p≤0.05` decision boundary.
I checked this directly, re-running the null control at `N=2,000` /
`5,000` / `20,000` / `50,000` (3 seeds each): all three real targets'
percentiles are stable to within ~0.01 across two decades of `N` (e.g.
`A_eff`: 0.489–0.497 across every `N`/seed tested) — **`N=2,000` already
gives the identical qualitative and near-identical quantitative answer**.
Given how far all three observed `p` (0.20, 0.50, 0.81) sit from 0.05, this
was never a close call that needed high `N` to resolve. `N=20,000` is not
wrong — it is generous, and the qualitative conclusion (no CONFIRM survives
null control) does not depend on it.

**Proposed fix (non-load-bearing — does not change any verdict):** correct
the docket-item-2/NOTES.md rationale from "matching the founding test's
`N`" to the actually-operative reason — Monte Carlo resolution at the
decision threshold — and note the founding test's own search space (400
grid points) is not comparable in kind to this one (36,680 expressions), so
the precedent-consistency framing should not be read as validating the
*search-space* choice, only reusing a round number for the *trial count*.

## 2. Does R5 apply — should P-070-2/4's NEITHER be read as REFUTE?

**Finding — evidentially, yes, and more decisively than R5's own numbers
were; procedurally, no retroactive re-verdict is warranted, but a
LOGBOOK-level generalization is.** R5 (Iteration 28, exp-051) ruled a
regressor out despite an AUC (0.649) that was *close to* its own REFUTE
line (0.65) — the ruling's force came from structural reasons (convention-
blindness; zero-crossings not recurring at the claimed period) and a
trivial baseline beating it, not from the raw number missing a band by a
wide margin.

Exp-070's `A_alt`/`A_eff` matches are, if anything, a **more decisive**
case for the same treatment. My independent null reconstruction (§0) shows
the null distribution's own 5th percentile is `best_rel≈0.0036%` and its
**median is `0.0365%`** — i.e. a *typical* random target in the same
plausible range already matches some named-constant expression this
tightly. The real targets' matches (0.015%, 0.081%, 0.036%) sit at or
*worse* than that median (the `A_alt`-minus branch, `p=0.8055`, is beaten
by 80% of pure chance draws). This is structurally the same shape as R5's
"a zero-information baseline beats it" finding — a specific, quantified
demonstration that the closeness is not surprising, not merely "we lack
power to tell." By this program's own R5 discipline, that is REFUTE-grade
evidence, not gray-zone evidence.

**But** I do not recommend retroactively re-scoring the committed
`confirm`/`refute`/`neither` booleans. That would violate the same
pre-registration discipline (predictions committed before the run) that
Iteration 46's Block MINI record exists to protect, and NOTES.md's prose
already states the finding with the correct force ("statistically
indistinguishable from chance," "worse than 80.6% of pure-chance targets")
— the epistemic content is not being softened, only the three-way
CONFIRM/REFUTE/NEITHER label doesn't have a category for "decisively
non-significant" distinct from "ambiguous." **Concrete fix, forward-looking
only:**
1. **A new LOGBOOK entry or R5 addendum**, memorializing (a) as a general
   house rule — any future dense small-integer bookkeeping-constant search
   (of this shape) requires a pre-registered null-permutation control
   before any match counts as evidence, generalizing this cycle's own
   docket item 2 the way R4 generalized exp-048's specific defect — and (b)
   as a specific dead end — `A_alt≈3·R_OUT` (233) and `A_eff≈`[the 519
   six-way tie] are not to be re-proposed as T28 candidate mechanisms
   without new information. This is squarely the Director's/Red Team's call
   at synthesis, not something this review can commit unilaterally.
2. **A symmetric REFUTE band for future batches of this shape**: the
   current design lets CONFIRM require *both* `best_rel≤1%` and `p≤0.05`,
   but REFUTE requires only `best_rel≥10%` — there is no path to REFUTE via
   a high null percentile, so an extremely unremarkable match (e.g.
   `p≥0.50`, worse than the coin-flip line) always lands in NEITHER by
   construction, however decisive the null result actually is. Recommend:
   `refute = best_rel≥0.10 OR null_p≥0.50` for any future reuse of this
   pattern. Applying this post-hoc to exp-070's own numbers would flip
   `A_alt`-minus (`p=0.8055`) to REFUTE but leave `A_alt`-plus (`p=0.2039`)
   and `A_eff` (`p=0.4969`, just under the line) as NEITHER — so even this
   sharper band would not have produced a clean sweep, which is itself a
   useful, honest calibration of how strong "REFUTE-grade" should be read
   here.

## 3. Is the "state-dependent/coherent" framing doing any real work?

**Finding — no, and it should not be expected to; the batch is honest about
this, but the disclosure could be more explicit given the QUANTUM
OPTICS-lead byline.** Item (b)'s "beat-frequency reconstruction" is the
ordinary trigonometric identity `1/P_beat=|1/P_a−1/P_b|` for two linearly
superposed real periodic signals — the same algebra used for RF envelope
detection or acoustic beat notes, requiring nothing beyond linear
superposition of two classical sinusoids in `sinθ`-space, fit to
deterministic FDTD output. Nothing in items (a)–(e) touches photon
statistics, coherence time, quantum state superposition, or any of this
seat's charter subject matter (non-classical absorption, state-dependent
interaction). This is *correct*, not a defect — the batch is explicit
throughout that Checkpoint-criterion-2 is declined and this is
"instrument/model-fidelity work" (§8, all phases), and PANEL.md's own
expressibility contract for this seat requires mechanisms to enter the
bench only as effective classical parameters in the first place. THERMO's
Phase-2 critique made the parallel observation about its own charter this
cycle ("a rare cycle where the charter has little physics to grade") —the
same is true here, and for the same reason: this is a geometry/statistics
diagnostic, not a mechanism proposal.

The one gap: unlike THERMODYNAMICS' WKB fold-in, which now carries an
explicit disclosed-scope-choice line (docket item 6, NOTES.md), there is no
equivalent one-line disclosure that this cycle's QUANTUM OPTICS lead slot
produced a purely classical statistical/geometric result with zero
state-dependent or coherent content. Given "beat frequency" is also a term
of art in actual quantum-coherent contexts (e.g. quantum beats between
closely-spaced levels), a future reader skimming a QUANTUM-OPTICS-led
write-up could reasonably wonder whether something coherence-related is
being claimed. **Proposed fix (cosmetic, not load-bearing):** add one
sentence to NOTES.md's mandatory-caveat section, symmetric to docket item
6: "The beat-frequency algebra in item (b) is classical linear
superposition of two real periodic functions in `sinθ`-space over
deterministic FDTD output; no photon-statistics, coherence-time, or
state-dependent physics is engaged or claimed by any item in this batch."

## 4. Self-scrutiny — this seat's own Phase-1 design

Four distinct defects in this seat's own Phase-1 proposal were caught and
fixed before the Phase-4 run, none surviving into the committed result:
(1) item (a)'s original bare-`R²≥0.30` gate would CONFIRM regardless of
which hypothesis is true (EM's attack, Red Team-proven — Attack 1); (2) no
null-permutation control existed anywhere in the original items (b)/(d)/(e)
design (PHOTONICS/MATERIALS, Red Team-executed — Attack 2); (3) item (e)'s
"record best match" (singular) was undefined under ties, which existed at
every real target (Red Team's own catch — Attack 4); (4) no gray-zone
disposition existed for any of the five items (VISION, ranked the cycle's
top finding — Attack 5). All four are exactly the shape of gap this
program's Checkpoint-4 history keeps finding — the process caught every one
of them before they reached a committed result, which is the discipline
working as designed, not a clean Phase-1. Worth stating plainly rather than
only in the docket's own dry language: three of five headline verdicts
(`P-070-1`'s qualitative CONFIRM, but for the *wrong reason* if unfixed;
`P-070-2`, `P-070-4`) would have been mis-scored, in the CONFIRM direction,
had Phase 2/3 not intervened.

## Ranked top-3 candidate next directions

1. **Run PLAN.md queue item 2's EM branch: the C60/C70 causal test.**
   Cheapest possible decisive next FDTD step — two new configs varying only
   `ABSORB` (60, 70 cells) against the existing C40/C80 pair, holding every
   other NAMED constant fixed by the same congruent-construction discipline
   already used throughout T21/T27/T28. This directly arbitrates the live
   tension P-070-1 raised (config-invariant signal, disfavoring an
   `ABSORB`-tied mechanism) against EM's own exp-069 Phase-5 argument
   (`ABSORB`-tied, the one thing that differs between C40/C80) — a real
   causal test, not another desk numerology pass. PHOTONICS' 750/450nm
   fallback should NOT run first: item (b)/(d)/(e) leave no surviving
   candidate period to narrow that re-run's own target toward (§2 above),
   so it would currently be an unfocused full redesign, exactly what
   PLAN.md's queue text warned against.
2. **Codify the null-permutation-control house rule and close the T28
   dead-end explicitly**, per §2's proposed LOGBOOK entry — generalizes a
   real, now-twice-demonstrated lesson (R5, and this cycle's own
   independently-reproduced null result) into a standing rule, and prevents
   a future cycle re-discovering `A_alt≈3·R_OUT`/`A_eff≈519` as an
   apparently-striking coincidence without first checking this cycle's own
   record.
3. **Break the `R_OUT=W_OBJ=W_FLANK=78` / `TAPER=ABSORB40=PAD80=40`
   labeling degeneracy** (Idealization 4, sharpened by PHOTONICS' Phase-2
   critique) with a dedicated geometry variant where these constants no
   longer coincide numerically. Currently structurally impossible for any
   named-constant search on this bench to distinguish "object radius" from
   "measurement-window half-width" as the physically loaded quantity, if
   either is real at all — a cheap, one-time geometry-design fix that would
   make any *future*, properly null-controlled search on this bench
   actually capable of identifying a mechanism, not just ruling candidates
   out.

## Bottom line

No computational defect in this batch (bit-identical reproduction,
independent reimplementation agrees to the digit). The `N=20,000` choice is
harmless but its stated precedent-match rationale is not valid reasoning
(§1) — cosmetic fix only. P-070-2/4's NEITHER verdicts carry REFUTE-grade
evidentiary weight by this program's own R5 discipline; the pre-committed
band schema (not this cycle's execution of it) is what stops that from
showing up as a REFUTE label, and the right fix is forward (§2), not
retroactive. This seat's own charter is correctly, honestly N/A this
cycle — no state-dependent or coherent physics is or should be claimed;
the "beat frequency" label is accurate classical trigonometry, and one
disclosure line would remove any ambiguity for a future reader (§3).
