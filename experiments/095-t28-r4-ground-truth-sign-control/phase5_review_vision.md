# Phase 5 Review — VISION SCIENCE

*Panel Iteration 72, exp-095. Blind, independent — fresh context, no memory
of this seat's own Phase-1 proposal draft that opened this cycle, no
access to any other seat's Phase-5 review. Charter: human perceptual
limits — contrast thresholds, luminance edge detection, spectral
sensitivity, adaptation, temporal sensitivity, saccadic/attentional
blindness. Central question: what would make a human eye FAIL to register
something physically present? Duty: pin numeric thresholds, with sources,
before any run that scores against them.*

## 0. Charter-engagement note, stated up front

This cycle is disclosed, correctly, as pure instrument recalibration — T1
route N/A, Checkpoint criterion 2 N/A, `REALIZABILITY_MEMO.md` untouched,
zero constraint-3/4 scoring anywhere in `results.json`. No perceptual
threshold is pinned or scored against in this cycle, so this seat's
narrow "pin the number before the run" duty is not engaged on the object
level — correctly so; I find nothing here that quietly smuggles a
constraint-3 claim past that scope, matching the T1-N/A disclosure
verbatim in `phase1_proposal.md` §4 and `NOTES.md`'s own T1/Realizability
sections. This seat's actual load-bearing duty on this specific sub-thread,
established over five prior cycles (Iterations 53/63/64/65/70), is
disclaimer-propagation vigilance — the NETD-is-not-a-human-threshold /
constraint-3-not-tested language must travel with every classification it
governs, in every surface (JSON, stdout, prose). That is where I spent
most of this review, plus a general-purpose adversarial pass per the
task's own instruction not to stay narrowly in-lane.

## 1. Independent verification of headline figures (recomputed from
`results.json`/`run_output.txt`, not taken on NOTES.md's word)

- **Rank 1a (sign check).** 39.2°: `delta_scene=-3.149521e-3` (<0),
  `floor_pass=true`. 39.4°: `delta_scene=-2.590877e-3` (<0),
  `floor_pass=true`. Both negative, both floor-clearing → **PASS**,
  confirmed exactly against the pre-registered criterion in `NOTES.md`
  ("PASS = delta_scene(R4) negative at BOTH... floor_pass=True at both").
- **Rank 1c (node-bracketing).** 38.49°: `delta_scene=-1.516840e-3`
  (<0), `floor_pass=true`. 38.69°: `delta_scene=-2.538531e-3` (<0),
  `floor_pass=true`. **Both floor-clear, SAME (negative) sign** → per the
  pre-registered rule ("FAIL = both floor-clear, same sign") this is
  **FAIL**, confirmed exactly.
- **Combined gate.** `rank1.proceed_gate=false` in `results.json`,
  matching the pre-registered AND-logic ("PROCEED only if Rank 1a is PASS
  AND Rank 1c is PASS or INCONCLUSIVE"). `rank2_calls=0`,
  `rank3_calls=0` — confirmed skipped. Saved spend: Rank 2 (36) + Rank 3
  (30) = **66 calls**, matching the task framing exactly; `total_fdtd_calls
  =20 = rank1_calls(16)+rank4_calls(4)`, confirmed by direct sum.
- **Rank 4.** Corrected-sigma 38.4°: `frac_contrast=5.2041×10⁻⁶` against
  `FLOOR=1.917438×10⁻⁴` — `frac_contrast` is only **2.7% of FLOOR**, a
  clean, unambiguous floor-gate failure (`floor_pass=false`, `y=null`),
  correctly labeled `NEITHER` per the pre-registered rule. I independently
  reconstructed `ratio_k` from `p_abs_w_c`/`p_abs_w_g`
  (`frac_p_abs=|2.92161×10⁻¹²−2.90936×10⁻¹²|/2.90936×10⁻¹²=4.208×10⁻³`;
  `ratio_k=4.208×10⁻³/5.2041×10⁻⁶≈808.8`) — matches the filed `808.6716`
  to 3 significant figures (small residual from my own rounding, not a
  discrepancy). The R13/R14 arithmetic underneath this classification is
  internally consistent and not fabricated.
- **Disclaimer bit-exactness, R9-style commensurability check, not merely
  restated.** I pulled exp-094's own `results.json::netd_disclaimer`
  directly and diffed it character-for-character against exp-095's: they
  are **byte-identical**
  (`"NETD is an instrument/detector threshold, not a human perceptual
  one -- does NOT bear on constraint-3/4's human-eye verdict.
  (Idealization 3)"`), confirming `NOTES.md`'s own "identical wording to
  exp-093/094" claim rather than trusting it. Same check on `scope_note`:
  also present and correctly worded in both JSON and `run_output.txt`
  (lines 93–94), not merely one surface.

All headline numbers check out. No arithmetic defect found anywhere in
this cycle's own record.

## 2. Disclaimer-propagation audit (this seat's own standing duty on this
sub-thread — R16, and the five prior disclaimer-erosion incidents)

**Clean, this cycle, on every surface actually checked.** `netd_disclaimer`,
`scope_note`, `r4_r5_family_disclaimer`, and `call_count_disclosure` all
appear at the top level of `results.json` AND are printed verbatim in
`run_output.txt` (lines 93–96) — the exact JSON-present/stdout-silent gap
that exp-091's own Phase-5 review caught (a genuinely different surface
than the four prose-to-prose disclaimer-erosion instances at Iterations
53/63/64/65) is not repeated here. Per-cell NETD fields
(`dt_ss_full_K_c/g`, `netd_classification_c/g`) are populated and persisted
for **every** angle in every Rank that actually ran (Rank 1a: 2 angles ×
2 configs; Rank 1c: 2×2; Rank 4: 2 configs) — R16's own founding gap (a
`_full` metrics path computing NETD byproducts that never reach
`netd_row()`) does not recur; this cycle's own R16-compliance header
promised this "from the first draft," and Phase-2 THERMODYNAMICS'
critique independently forced `cell_metrics_r5` to be explicitly named
before Phase 4 — though moot in the end, since Rank 2 never ran, that
fix would have covered exactly the code path most likely to repeat R16's
founding shape had the gate PASSED. Credit due: this is the first T28
cycle since R16's adoption that engaged the R5-style fresh-metrics-path
risk and closed it *before* the run rather than discovering it after.

**But: the disclaimer's own home document — `NOTES.md` — carries no
Result, Learned, or Next section at all.** I confirmed this by direct
grep (`^## Result`, `^## Learned`, `^## Next` — zero matches) against the
file on disk as of this review; `NOTES.md`'s last edit predates
`results.json`/`run_output.txt`'s own timestamps, meaning the frozen
Phase-3 document has not been updated with any account of what Phase 4
actually found. This is not a disclaimer-erosion instance in the R16/
Iteration-53/63/64/65 lineage (there is no prose restatement that
*dropped* a caveat — there is no prose restatement of the result at all),
but it is the identical failure shape Red Team's own Phase-5 audit named
and fixed same-shift at exp-080 and exp-090 ("three of six Phase-5
reviews independently converged on this same disposition unprompted").
The Iteration-65 CHECKPOINT's own non-discretionary rule requires the
carried-idealizations banner "at BOTH the Predictions section AND the
Result section" — with no Result section to carry it, that requirement
is currently unsatisfiable by construction, not merely unmet. I flag this
as the sharpest structural gap in the record as it stands at the point of
this review, matching precedent for a same-shift, non-firing fix — not a
new finding worth a numbered rule, but one that should not be left for a
sixth or seventh reviewer to name.

## 3. Sharpest finding: Rank 1c's FAIL is read as one-sided evidence for a
"registration defect," but the record's own data more directly supports
an under-powered bracket over a wiring bug

The task's own prompt asks whether the "reported outcome, never a crash"
framing is even-handed between a registration bug and genuine node
migration. It is not, and the imbalance is traceable to specific,
citable text, not merely a vibe:

- `phase1_proposal.md` §2 (carried into the frozen record, never revised
  at Phase 3): on FAIL, the cycle "names the finding an **R4-family
  registration-defect candidate** for Phase 2/5 to investigate."
- `NOTES.md`'s own frozen Rank-1c prediction: FAIL means "the established
  node **appears to have vanished** from this window in the `R4` family —
  a **genuine integrity finding**."
- `run_output.txt`'s own summary line: "HALT before Rank 2/3 —
  **integrity finding, Checkpoint-4-relevant**."

Every one of these three surfaces reaches for "something is wrong with
this family's construction" language. None of them gives equal billing
to the alternative R15's own Iteration-71 addendum explicitly names as a
live possibility: that the null **genuinely migrated**, under `cpl=40`
refinement, to somewhere **outside** the tested ±0.1° window
(38.49°–38.69°) — which a two-point bracket test cannot distinguish from
"the node vanished" no matter how the two points read.

This matters because the record's own data, re-derived independently
this review, argues for the migration reading being at least as
plausible as the defect reading, on two separate grounds neither Phase 2
critique nor the Red Team audit raised:

1. **The ±0.1° bracket width was never calibrated against this exact
   neighborhood's own established migration scale.** QUANTUM's Phase-2
   critique proposed "±0.1°" as an example figure, not a derived one; no
   document in this cycle's record computes it from data. But this
   program's own record, re-checked directly: exp-094's own Rank 3 (native
   sigma, `cpl=20→30`, the SAME `C40`/`G40` pair, one cycle earlier) found
   38.4° itself — 0.19° from θ₀=38.590° — **flips sign and classification**
   between resolutions (`ratio_k` 0.9075→16.9967, `Y=0→Y=1`). That is
   direct, already-filed, on-the-books evidence that a null in this exact
   38.4°–38.6° neighborhood moves by an amount comparable to or exceeding
   0.1°–0.2° between adjacent resolution families on this identical
   channel — yet Rank 1c's own bracket is sized at exactly that scale,
   with no stated margin against it. A ±0.1° window is not obviously wide
   enough to catch a null this program's own data already shows can move
   at least that far.
2. **Rank 4's own reading, independently reconstructed above, is
   additional, unexploited evidence for migration, not defect.** At
   corrected sigma, `cpl=30`, 38.4° reads `frac_contrast` at only 2.7% of
   `FLOOR` — the reading sits almost exactly ON a zero, not merely near
   one. Combined with the native-sigma flip already on record at the same
   angle, the most parsimonious reading is that the `PAIR_PAD` null
   *itself* sits extremely close to 38.4° at corrected sigma, `cpl=30` —
   consistent with active, ongoing migration of this specific node across
   both the sigma correction and the resolution axis, not a static
   feature a `cpl=40` construction bug simply failed to reproduce. This
   cycle's own two Ranks (1c and 4), run independently of each other,
   point the same direction and neither document connects them.

To be clear about what mitigates this: the FAIL-branch language was
**pre-registered** (frozen in Phase 1/3 before any run), which is the
correct house discipline and rules out post-hoc spin in the strict
sense — this is not a case of seeing an inconvenient result and reaching
for a flattering explanation after the fact. But pre-registering an
asymmetric interpretive frame is still an asymmetric interpretive frame;
"integrity finding" and "registration-defect candidate" were the only
vocabulary on offer for FAIL before the run happened, and nothing in
Idealization 24/28 (the closest hedges in the record) explicitly names
"the tested bracket may simply be narrower than this neighborhood's own
established migration scale" as an alternative reading. Both explanations
remain genuinely open; the record should say so with equal weight, and
should say so explicitly in whatever fills the still-missing Result
section (§2, above).

## 4. A methodological point in this cycle's favor, worth crediting
explicitly (not all findings should be attacks)

QUANTUM's own Phase-2 critique argued, before any data existed, that a
sign-only check at amplitude-dominated (off-node) points has "near-zero
statistical power" against exactly the registration/phase-defect class
this control exists to catch, and that the fix (a node-bracketing check)
would be "powered against exactly the defect class an off-node sign check
cannot see." That prediction is now empirically borne out: Rank 1a (the
sign-only check QUANTUM warned was underpowered) PASSED cleanly, while
Rank 1c (the addition QUANTUM specifically proposed) FAILED. Had Red
Team's audit not elevated QUANTUM's critique to a mandatory fix, this
cycle would have shipped a clean PASS on Rank 1a alone and proceeded to
spend the full 66 calls on Rank 2/3 under a false all-clear — a
genuinely consequential catch, not a hypothetical one. This is the kind
of Phase-2 critique this program's own review layer exists to produce,
and it worked exactly as designed here.

Separately: `gate5_wiring_defect_verification_result.json`
(`control_pass: true`, `injected_defect_pass: true`, `verdict: "PASS"`)
shows the `R5` family's Gate 5 fault-injection control was actually
**executed for real** this cycle (the script constructs a genuine `Sim`
object and calls the real `_run_sim_r5_sigma`/`build_article_r5_sigma`
code path — confirmed by reading the script directly, not merely its
docstring) — correcting exp-094's own Phase-5-caught overclaim (a
verification claim asserted without a corresponding artifact). Credit
where due: this cycle applied its own predecessor's Learned lesson before
being asked to a second time.

## 5. Other findings, general adversarial pass

- **Rank 4's outcome label ("NEITHER") is a stylistic, not substantive,
  departure from R13's own suggested vocabulary** ("NODE-UNRESOLVABLE" /
  "UNRESOLVED-BY-CONSTRUCTION"). Functionally identical (`floor_pass=
  false`, `y=null`, excluded from classification, not silently scored) —
  I do not read this as an R13 compliance defect, only a naming
  inconsistency across this sub-thread's own outcome taxonomies (Rank 4
  uses CONFIRM/REFUTE/NEITHER; R13's own founding text uses
  NODE-UNRESOLVABLE). Low priority, cosmetic.
- **The call-count correction (Phase-1's 72/18 → NOTES.md's 86/20) is
  itself independently verifiable and correct.** I recomputed Rank 3b
  (2 configs × 6 angles × (empty+article, both legs fresh) = 24, not 12)
  and Rank 4 (2 configs × (empty+article) = 4, not 2) directly from the
  stated call-accounting logic; both match the "Disclosed spec-resolution
  note" in `NOTES.md` exactly, and the actually-filed FAIL-path total
  (20 = 16+4) matches the corrected model precisely, not the Phase-1
  draft's original (18). No inconsistency found.
- **No T1/constraint smuggling found anywhere.** I read every predicted
  outcome in `NOTES.md` §Predictions and every printed line in
  `run_output.txt` looking specifically for language that could be
  mis-cited later as a constraint-3/4 status update (this sub-thread's
  own recurring risk, T16/R9-lineage) — found none; every quantity here
  (`delta_scene`, `ratio_k`, `frac_contrast`, NETD) is explicitly scoped
  as instrument-internal.
- **`R5` family fully built and gate-verified but entirely unused this
  cycle** (Rank 2/3 skipped) — this is the correct, intended behavior of
  the gate, not a defect, but it means `R5`'s substantive value (as the
  minimum-discharge item for R15's addendum, per Red Team's own
  Iteration-71 ranking) is now deferred, not delivered, exactly as
  Idealization 17/28 anticipated it might be. Worth stating plainly for
  Iteration 73's own planning: the `cpl=50` spend was not wasted (it was
  correctly avoided), but R15's addendum remains exactly where exp-094
  left it, now compounded by a second, unresolved data point (Rank 1c's
  own FAIL) rather than clarified.

## 6. Verdict

**CONCUR-WITH-GAP(S).**

The core deliverable — a disciplined, correctly-sequenced, correctly-gated
go/no-go control that saved 66 calls on a well-justified HALT — is sound
and independently verified arithmetic-exact throughout; every Phase-2
mandatory fix (control-angle replacement, the node-bracketing addition,
Gate 5's real fault-injection execution, R16 compliance) landed as
promised. Against that: the record's own framing of Rank 1c's FAIL leans
toward a "registration defect" reading without stating, with equal
weight, the better-evidenced "genuine node migration beyond an
uncalibrated ±0.1° bracket" alternative this sub-thread's own already-
filed data (the 38.4° native-sigma flip, this cycle's own Rank 4 near-
total-null reading) more directly supports; and `NOTES.md` currently
carries no Result/Learned/Next section at all, leaving the
Iteration-65-mandated dual-section idealizations banner structurally
unsatisfiable and this cycle's own most consequential open question
(does exp-094's headline reversal survive?) unstated anywhere in the
committed prose record.

## 7. Ranked recommendations for Iteration 73

1. **Highest priority, cheapest, most decisive: widen Rank 1c into a
   denser bracket before drawing any conclusion from this cycle's FAIL.**
   A ~6–10-call sweep at `cpl=40`, `R4` family, corrected sigma, spanning
   roughly 38.1°–39.1° in 0.1°–0.2° steps (centered on θ₀=38.590°, wide
   enough to exceed the 0.19°+ migration scale this sub-thread's own
   record already shows at this exact neighborhood) — the single test
   that can actually distinguish "the R4 family's construction is broken
   near this node" (no crossing found anywhere in the wider window) from
   "the null migrated past the ±0.1° bracket this cycle happened to test"
   (a crossing found just outside it). Until this runs, neither this
   cycle's own "registration-defect candidate" framing nor a "genuine
   migration" reading is entitled to more confidence than the other, and
   Rank 1c's FAIL should not be cited elsewhere as evidence for either
   specific mechanism — only as evidence that the R4 family fails this
   particular ground-truth check as currently constructed.
2. **Write `NOTES.md`'s missing Result/Learned/Next section same-shift,
   before this cycle is cited by any future document.** State explicitly
   what this review names in §3 and §5: exp-094's own headline
   TWO-NODE-CONFIRMED/complete-reversal finding has not been vindicated
   OR refuted by this cycle — it is now sitting downstream of an
   unresolved ground-truth-control FAIL, a materially different status
   than "PARTIAL, narrowed" implies on its own. Carry the idealizations
   banner into this new section per the Iteration-65 CHECKPOINT's own
   non-discretionary rule.
3. **Do not spend the `cpl=50` (`R5`) budget until (1) resolves**, even
   though the family is now fully gate-verified and ready — MATERIALS'
   own exp-095 critique already showed no `R5`-family outcome can, on its
   own, discharge R15's addendum (a recipe-level artifact reproduces at
   any ratio drawn from the same construction); spending it now, before
   the more basic question of whether the `R4` anchor itself is trustworthy
   near this node is settled, would risk producing a third data point
   whose interpretation is exactly as compromised as the second.
