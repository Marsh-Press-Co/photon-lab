# Phase 5 Self-Review — QUANTUM OPTICS (exp-112, Panel Iteration 89)

*Fresh context. This cycle's own rotation-lead seat, re-auditing the cycle
it proposed at Phase 1, blind to the Phase-2/4 record as it evolved and to
every other seat's own Phase-5 review this cycle. Charter: non-classical
absorption, state-dependent or coherent interactions; distinguishing
genuine signal from instrument artifact at a detection floor is this
seat's own charter question. Every claim below is independently
re-derived from `results.json`/committed source, not trusted on
`NOTES.md`'s own prose — this sub-thread's own R4/R9 discipline.*

## Verdict: PARTIAL — and one genuinely new, load-bearing correction to this cycle's own Interpretation

T1 correctly N/A throughout, confirmed structurally (no σ(I)/σ(x,t)/
angular-selectivity/sub-threshold content anywhere in `run112.py`/
`chunk_runner112.py`/`analyze.py`). Every numeric claim in the Result
block reproduces exactly from `results.json` — no R4-class figure defect
found. But re-deriving Check C's own discriminating power from data
**already committed by this cycle** (zero new FDTD) shows it has none: the
named bin's headline `corr=0.9994` is not distinguishable from this same
instrument's own reading at every other bin in the pattern, resolved or
not. This cycle's own Interpretation section states the correlation is "a
striking number... not obviously expected... by chance" — that claim is
false as stated, checkable from data this cycle itself already produced.
Not outcome-reversing (the document's own bottom line — no "candidate real
structure" claim made — survives, and for an even stronger reason than it
states), but it is exactly the kind of unverified interpretive claim R4/R8
exist to catch, and it belongs in the permanent record, corrected, not
merely disclosed here.

## 1. Verifying Check A/B/C from primitives

Recomputed directly from `results.json` (exp-112) and `results.json`
(exp-110, for the `cpl=20` baseline) — no figure below is copied from
`NOTES.md`'s own prose:

| Quantity | `cpl=20` (baseline) | `cpl=25` (this cycle) |
|---|---|---|
| `local_snr_peccored` | 0.096521 | 0.144424 |
| `local_snr_hollow` | 0.106057 | 0.158947 |
| mirror-pooled floor (K=3, median) | 1.126167e-3 | 9.725055e-4 |
| `delta[idx=4]` | −1.073928e-05 | −1.412430e-05 |
| `delta` ratio (new/old) | — | 1.315200× |

**Check A: AMBIGUOUS, confirmed.** Both `local_snr` values improved
(≈+50% peccored, ≈+50% hollow) as the floor itself dropped ≈13.6% — but
both stay 6–7× below the pre-registered `K=1=1.0` bar. Neither the
SURVIVES nor COLLAPSES band is met; "AMBIGUOUS" is the honest, correctly
computed reading.

**Check B: SURVIVES, confirmed.** Sign unchanged (both negative); ratio
1.3152×, inside the pre-registered `[0.1, 10]` band by a wide margin. This
is real but weak evidence — the band is wide enough that almost any
outcome short of a sign flip or an order-of-magnitude collapse clears it;
it does not by itself argue for "real structure" over "noise that happens
to persist at similar order of magnitude across a 1.25× mesh refinement."

**Check C: `corr=0.9993580404725309`, confirmed bit-exact.** This is where
my own independent verification diverges from the document's own framing
— see §2.

**Reproduction/geometry preconditions**: `repro_ok=True`,
`rel_dev_peccored=0.0`, `rel_dev_hollow=0.0`, `geom_identity.pass_=True`,
`mismatches=[]` — all confirmed bit-exact against `results.json`. R23
compliance (Fix 5) independently re-verified here a second time: both
`results.json["predictions_text"]` and `["result_text"]` contain the
Fix-4 "grid-discretization SNR threshold" disambiguating clause verbatim
— the assert genuinely fired on real execution, not merely present in
source.

## 2. Check C has no demonstrated discriminating power — a genuinely new finding

Docket Fix 3's own `neighbor_correlation_check` docstring (and PHOTONICS'
own Phase-2 critique that motivated it) rests on an unverified premise,
stated as fact: "a genuine deterministic sub-wavelength field feature...
must imprint correlated structure across several adjacent bins...
uncorrelated Yee-grid staircase noise, by construction, need not." This
premise was never checked against this cycle's own data before being used
to interpret the one bin it was built to adjudicate. I checked it, using
only already-committed arrays (`results.json["pattern_delta"]`, this
cycle; `experiments/110-.../results.json["r156"]["raw_patterns"]["32"]
["delta"]`, the existing baseline) — zero new FDTD, pure arithmetic,
reproducible by anyone from the same two files:

Computing the identical ±2-bin Pearson correlation `neighbor_correlation_
check` applies to the named bin, at **every one of the other 47 bins**:

- **Resolved bins** (34 of 48, `local_snr` deep in the thousands-to-tens-
  of-thousands range — the dominant, unambiguously real scattering lobe):
  correlation ranges **0.8169–0.9996**, mean **0.9793**.
- **Unresolved bins** (14 of 48, including the named bin — `local_snr`
  comparable to or below the named bin's own reading): correlation ranges
  **0.9689–0.9995**, mean **0.9916**.
- The single **lowest** correlation anywhere in the pattern (0.8169, bin
  index 35) sits in the **resolved** population, not the unresolved one.
  The **unresolved population's own mean correlation (0.9916) is higher**
  than the resolved population's (0.9793) — the opposite of what the
  check's own motivating premise predicts.
- The named bin's own reading, 0.9994, is unremarkable against either
  population — it sits inside both ranges, near the middle of the
  unresolved population's own distribution.

The reason is straightforward once checked: `delta(θ)` (the peccored−
hollow scattering-pattern difference) is a smooth, slowly-varying function
of angle at *both* resolutions — it is dominated by the disk's overall
diffraction envelope, not by bin-to-bin independent noise — so **any**
±2-bin window correlates highly between two congruently-refined meshes,
independent of whether the *absolute* magnitude at that window is
individually well-resolved by the mirror-pooled-floor SNR test or not.
`neighbor_correlation_check`, as built, measures whether the *local shape*
of an already-smooth curve persists under refinement — it does not
isolate, and was never shown to isolate, whatever fine-scale component
(real near-field feature vs. staircase artifact) actually differs between
the two hypotheses Check A exists to adjudicate. A pre-registered `corr≥
0.5` bar that is cleared by 48 of 48 sampled bins, spanning both
populations, carries no information at the resolution this cycle needed
it to operate at — the identical "look-elsewhere" shape this program's own
R5/R10 lineage exists to catch (a discriminator run without ever checking
what it reads under conditions where the answer is already known by
construction).

**This directly falsifies NOTES.md's own Interpretation-section claim**
("a striking number for an independent grid refinement to reproduce by
chance... a purely random discretization artifact would not obviously be
expected to preserve a 0.9994-correlated local shape") — checked, this
statement is not true of this cycle's own data: a purely-noise-floor bin
elsewhere in the identical pattern (e.g. index 0, `local_snr≈0.04`, deep
in the unresolved population) reproduces a **0.9959** correlation, higher
than the named bin's own 0.9994 is unusual relative to. Non-outcome-
reversing (the document's own final position — no "candidate real
structure" claim, Check A never reached SURVIVES — is unaffected, and in
fact *more* defensible once this correction is made, not less), but it is
exactly the class of "confirmation of a comparison without checking the
comparison's own commensurability/null behavior" R9 was written to close,
applied here to a spatial-correlation discriminator instead of a unit
ratio. I recommend NOTES.md's Interpretation section be corrected in
place (same-shift, non-outcome-reversing, per this program's own R4/R8
annotation convention) rather than left as filed.

## 3. Does this cycle answer QUANTUM's own charter question?

Phase 1's own framing (§1, `phase1_proposal.md`): "distinguishing a
genuine deterministic near-field signature from instrument/quantization
noise at a detection floor is exactly this seat's charter question." My
own honest re-assessment, now that §2 is on the table: **no — and the
correct characterization is weaker than "genuinely open, real tension,"**
which is how NOTES.md's own Interpretation section states it.

- Check A (this cycle's own *primary*, pre-registered instrument for
  exactly this question) returns AMBIGUOUS — it does not merely fail to
  decide, it is 6–7× short of even its own most permissive (K=1) bar. This
  is a real result (the bin has not newly cleared the floor at `cpl=25`),
  but it is not evidence *for* real structure either.
- Check B is weak, wide-band evidence, uninformative on its own (§1).
- Check C, the one reading that *looked* like it might tip the balance
  toward "real structure," is shown in §2 to carry no discriminating
  information at all, once its own null behavior is checked.

Net: this cycle's own instruments do not merely leave the charter question
open — they provide **no positive evidence either way** once Check C's
apparent signal is correctly discounted. The honest statement is not "a
real tension between two readings" but "one inconclusive primary result
(Check A) and one instrument (Check C) whose apparent tie-breaking value
does not survive its own null check." This is a meaningfully different,
and weaker, epistemic position than NOTES.md's own filed Interpretation
claims, though it changes no verdict (the document already declines to
claim "candidate real structure," for the right procedural reason —
Check A never reached SURVIVES — even though its stated *reason for
finding this interesting* does not hold up).

## 4. The R29 process question — could Phase 1 have caught this?

Both collisions (`run.py`/`run.py`, caught at Phase 2; `chunk_runner.py`/
`chunk_runner.py`, caught only at Phase 4) were introduced in the
identical Phase-1 commit (`b25ff99`, this seat's own draft), from the
identical proximate cause: this cycle's own `sys.path.insert(0, ...)`
ordering, copied from exp-110's own established two-cycle-running
convention (`import <prior-cycle> as R<n>`, `import <this-cycle> as R`)
without independently checking that convention for basename collisions
against *every* file this cycle's own package introduces — not just the
one (`run.py`) whose collision happens to crash loudest and first.

**Was there a way Phase 1 itself should have caught this?** Yes, and it
did not require running real FDTD or even a full dry run — a purely
**static** check would have sufficed: enumerate every bare `import
<name>` statement across every file in the committed Phase-1 package
(`run.py`, `chunk_runner.py`, `analyze.py`), cross-reference each `<name>`
against every *other* directory the same file adds to `sys.path`, and flag
any basename present in more than one such directory. This is a zero-
execution, mechanical grep-and-compare — I confirmed it myself, from the
committed Phase-1 files, without running anything: `analyze.py`'s own
original commit did `sys.path.insert(0, HERE)`, `sys.path.insert(0,
ROOT)`, `sys.path.insert(0, .../110-.../)`, then bare-imported `run` (name
collides — `run.py` exists in both `HERE` and the exp-110 directory) *and*
`chunk_runner` (name collides identically — `chunk_runner.py` exists in
both). Both collisions were visible, side by side, in the same eight-line
import block, from the moment the file was written. Phase 1's own §2.0
grounding checks ran `run112.py --verify-geometry` directly (bypassing
`chunk_runner.py`/`analyze.py`'s own import chain entirely) — it never
attempted to invoke the two files that actually carried the risk.

**But I do not think "always dry-run every file before calling it ready"
is by itself the correct forward lesson, and R29's own text already gets
closer to the right one.** THERMODYNAMICS' own Phase-2 critique, and Red
Team's own Phase-2 audit, *did* dry-run the pipeline — `python3
chunk_runner.py 156 25 empty` and `python3 analyze.py`, both executed for
real, both crashing. That crash caught the first collision cleanly. It
structurally **could not** have caught the second: `analyze.py` raises
`AttributeError` on its own first `R.verify_geometry_identity()` call,
which sits *before* any line that would exercise `CR.SCRATCH` — so no
amount of re-running the same crashing file surfaces the second collision
until the first is fixed. And even after Fix 1 landed, the second
collision did not crash at all — `chunk_runner as CR` silently resolved to
exp-110's own module, which happens to *also* define a `SCRATCH`
attribute (pointing at the wrong, empty directory), so `have(...)` merely
returned a plausible-looking `False` instead of raising. This was only
caught because someone compared the code's own claim ("captures not yet
complete") against directly-observed filesystem state (`done.pkl` files
genuinely present) — a discrepancy check, not a crash.

**The forward lesson, more precisely than "dry-run everything": a same-
basename import risk is a *static* property of the source text (which
names are bound bare, against which directories are on that file's own
`sys.path`), fully checkable before any execution — but *dynamic*
execution (dry-run or real) can only ever surface the *first* instance of
it reached, because a collision that crashes masks every later one in the
same file, and a collision that does not crash (this cycle's second
instance) may not surface even on a full successful run unless its output
is independently cross-checked against ground truth.** R29's own text
already requires "an EXECUTED identity or attribute check... before any
function relying on the distinction is trusted" for *every* colliding
import — which, applied literally and up front (one static pass over the
whole package, not one collision discovered per crash), would have caught
both in the same sitting Phase 1 wrote the files. I recommend this be
stated explicitly as a corollary to R29 (not a new rule): the identity-
check discipline R29 mandates must be applied by *enumerating all
same-basename risk in the package first*, not by fixing forward from
whichever collision happens to crash first.

## 5. The Checkpoint-4/R29-second-instance question — my reasoned view

This originates from my own Phase-1 draft, so I state a view, not a
ruling — this program's own convention (and NOTES.md's own Phase-4 entry)
correctly declines to self-adjudicate it in the same breath that found it.

**My view: this is the same founding instance, manifesting twice, not a
second instance triggering R29's forward-firing clause — Checkpoint 4
should not fire on it.** Reasoning, checked against this registry's own
operative precedent rather than my own preference:

1. **Root cause is singular, not repeated.** Both collisions trace to one
   decision, made once, in one sitting (adopting exp-110's own `import
   <prior> as R<n>` / `import <this> as R` idiom without checking it
   against every file the new package introduces) — not two independent
   failures to apply a rule that already existed. R29 did not exist when
   either collision was written.
2. **Phase 2 could not have reached the second collision even trying** —
   demonstrated directly in §4, not asserted. A "known, named, ignored"
   bar (the standard every prior rule in this registry — R6 through
   R28 — requires before treating a repeat as culpable) cannot be met by
   a defect that was structurally unreachable by the review layer that
   would have named it.
3. **This matches, closely, the shape this registry has already ruled
   non-firing more than once within a single founding cycle**: R18's own
   founding instance (two distinct scope-overclaim defects, same gate,
   same cycle, "does NOT meet the strict... bar... this is this specific
   gate's own founding cycle"); R21's own text explicitly declines to fire
   on *either* of its two founding instances; R23's First Addendum treats
   its own two-builder asymmetry, discovered in one document, as one
   consolidating instance. In each case, multiple manifestations of a
   *newly-named* failure shape, surfacing within the cycle that names the
   shape, are treated as one founding event, not a founding-plus-a-
   second-strike.
4. **Self-disclosed, same-shift, non-outcome-reversing** — matching this
   registry's own universal precondition for founding-instance leniency.
   No result was scored on the broken pipeline at any point; the fix
   landed before any check's outcome was read.

The genuine tension, stated plainly rather than argued away: R29's own
forward clause reads "a second instance... after this rule is on the
books" without qualifying "instance" to mean a later *cycle*'s reuse
specifically, and the second collision was, in a strict chronological
sense, discovered after Phase 3 ratified R29 within this same document. I
do not think that chronological fact should control — the rule exists to
punish a *future cycle* choosing to reuse a known-risky idiom having had
the chance to consult this registry first, not to punish this cycle's own
delayed discovery of a defect it had already introduced before the rule
existed to warn it. If Red Team's own final audit disagrees and rules this
a firing second instance, I would not consider that an unreasonable
reading either — the text genuinely under-specifies "instance," and I
recommend whichever way this is decided, R29's own text be tightened
(a parenthetical: "a second CYCLE's own instance of this collision shape,
introduced after R29 was ratified" or equivalent) so this ambiguity is not
inherited by a future adjudication.

## Combined Verdict: PARTIAL

Not RULED OUT — T1 correctly N/A, geometry/reproduction preconditions
clean, Check B is a genuine (if weak) SURVIVES, and the named bin's own
disposition remains legitimately unresolved on the strength of Check A
alone. Not PROMISING — the one instrument that appeared to break the tie
toward "interesting" (Check C) is shown here, from data this cycle itself
already committed, to have no demonstrated discriminating power, and the
document's own Interpretation section states an unverified, and on
inspection false, claim about it. Zero Checkpoint criteria fire from this
review alone (criterion 4 assessed and reasoned against, above, but left
for Red Team's own final audit per this program's standing practice).

## Ranked next-step recommendations

1. **Null-calibrate `neighbor_correlation_check` before its reading is
   ever cited again, and correct NOTES.md's Interpretation section
   in place.** Zero new FDTD — the calibration in §2 above uses only
   already-committed `results.json` data from this cycle and exp-110.
   Report the background correlation distribution (resolved vs.
   unresolved bins) alongside any future named-bin reading, and require a
   bar set relative to that distribution (e.g. a percentile within the
   pattern's own observed spread), not a fixed, uncalibrated `corr≥0.5`
   that 48/48 sampled bins already clear.
2. **Adjudicate the R29 second-instance/Checkpoint-4 question explicitly**
   (Red Team's own final audit, per NOTES.md's own deferral) — my own
   reasoned recommendation is non-firing, same founding cycle (§5) — and
   tighten R29's own text to specify "instance" at the cycle level so a
   future adjudication does not face the identical ambiguity.
3. **Before spending the deferred r=312/+168.75° leg** (or a third,
   differently-scaled resolution point, R15 discipline), re-scope its own
   pre-registered checks to include the null-calibrated correlation
   control from item 1 at design time, not add it reactively after a
   surprising reading — this cycle's own Check C was added reactively at
   Phase 2 and still shipped uncalibrated at Phase 4; the next leg should
   not repeat that shape a second time on the identical instrument.

Full record consulted: `experiments/112-t28-cpl25-floor-spot-check/
phase1_proposal.md`, five `phase2_critique_*.md`,
`phase2_redteam_audit.md`, `NOTES.md`, `run112.py`, `chunk_runner112.py`,
`analyze.py`, `results.json`; `experiments/110-t28-item-i-local-norm-and-
controls/NOTES.md`, `run.py`, `results.json`; LOGBOOK.md RULED OUT
registry (R1–R29) and Iterations 85–88 narrative.
