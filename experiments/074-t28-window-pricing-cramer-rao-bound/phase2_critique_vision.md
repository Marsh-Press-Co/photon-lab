# VISION SCIENCE — Phase 2 Critique · Panel Iteration 51 · exp-074

*Blind to all other seats' critiques this cycle. Charter: human perceptual
limits — contrast thresholds, luminance edge detection, spectral
sensitivity, adaptation, temporal sensitivity, saccadic/attentional
blindness. Duty: pin numeric thresholds, with sources, before any run
that scores against them.*

## Independent verification performed

Re-ran `desk_check_pricing.py` unmodified. `CHECK 0` passes
(`worst_rel_err=0.00e+00`). All per-pair figures in phase1_proposal.md §2b–2f
reproduce bit-for-bit against my own run: `cond5≈60`, `cond9∈[478.4,529.4]`,
`VIF_Rq∈[31.1,36.6]`, `z_joint(optimistic)∈[0.54,0.81]`, `lev_ratio≈0.80`
(baseline) rising to `0.914` at 51°, `VIF` median falling to `1.4` at 51°.
The widened-window table (§2e) also reproduces to every printed digit. I
traced the cross-references cited as anchoring the §5 bars: `exp-072/
phase5_review_em.md` §6 item "2." (the numbered subsection under "## 6.
Ranked candidate directions") does contain `cond=529`, `36.6×` VIF, and the
"cannot reach 2σ" language exactly as quoted; `exp-072/phase5_review_
quantum.md` §3 does contain `|L(1.9608°)|≈26.8`, peak `35.7–36.7` at
`3.49–3.55°`, exactly as quoted; `exp-073/phase5_redteam_audit.md` §6.2 is
indeed "Ranked queue for Iteration 51." No dangling or mis-numbered
cross-reference found — a clean result given this program's specific,
repeated history of exactly that defect.

**Constraint-3 check:** grepped the full proposal for perceptual/
detectability language (`invisib`, `perceiv`, `ambient`, `ontrast`,
`scoto`, `photop`, `observer`) — zero hits. `T1 N/A` is correctly stated;
nothing here implicitly smuggles a perceptual claim. This is a clean
instrument-pricing exercise, confirmed.

## Cross-domain threshold-discipline check (my charter's own duty, applied here)

My seat's duty is "pin numeric thresholds, with sources, BEFORE any run
that scores against them." I checked whether §5's five load-bearing bars
meet that bar themselves:

- `z_joint(optimistic) < 1.5` / `≥ 2.0` — **sourced.** `2.0` is literally
  EM's own stated "2σ" bar from exp-072 §6.2; `1.5` is a stated margin
  below it. Traceable.
- `cond9 ≥ 300` — **not derived, only gestured at.** §0 cites "the
  cond≤100/(n−p)/n machinery already standing in run.py" as the source,
  but `cond≤100` is a threshold on the **5-column** single-carrier design
  (`ill_conditioned = cond5 > 100.0`, `run.py` line 307/406); no formula or
  argument in the document scales that to a **9-column** two-tone design's
  condition number, and "×3" is never stated as the multiplier being used,
  let alone justified.
- `VIF_Rq ≥ 15` — **not derived.** No formula ties 15 (or the equivalent
  `3.9×` SE-inflation) to an actual consequence (achieved power, false-
  negative rate). Observed values are `31–37`, over 2× the bar.
- `lev_ratio ≥ 0.90` — **not derived**, and the document itself concedes
  this in Idealization 8 ("necessary, not sufficient... a genuinely new
  null must still pass its own fresh calibration test"). No stated formula
  connects `lev_ratio=0.90` to any specific bound on null over/under-
  rejection.

Three of five bars are precedent-flavored assertions, not derivations —
exactly the failure shape my charter would flag in a perceptual context
(a JND cited as "≈2%" with no source is not usable to score a run; a
condition-number cutoff cited as "3× an unrelated design's threshold" with
no stated multiplier is the same category of unsourced number). Mitigating
fact, independently checked: none of these three bars is outcome-
determining. The tightest real quantity — `z_joint=0.81` at C40–C60 — is
60% below the bar that *is* properly sourced (`2.0`), and `VIF/cond9`'s
actual values clear their unsourced bars by 2×+ margin. Tightening or
loosening `cond9`'s bar to anywhere in `[150,450]` would not change the
CLOSURE-CONFIRM verdict. The discipline violation is real; it is not
load-bearing this cycle.

## Legibility of the central logical chain

A reader unfamiliar with this thread is told "closed independent of which
null eventually gates it" but the mechanism — *why* a conditioning/VIF
bound is null-construction-independent — is never spelled out as its own
sentence. The implicit chain (OLS's SE is the Cramér–Rao-efficient
variance floor for any unbiased linear estimator here; a null construction
changes only the critical value the observed statistic is judged against,
not the estimator's own sampling variance, which is fixed by the design
matrix alone) has to be reconstructed by the reader from Idealization 6's
one clause ("assumes... noise level and true effect are identical to what
the single-carrier fit measured, which the two-tone fit cannot do better
than even in principle"). That clause is the whole argument and it is
under-flagged as such — it reads as a modeling caveat, not as the load-
bearing step that makes the "any null" claim true.

## Steel-man (≤150 words)

This is the T28 program's first cycle in six that turns an assertion into
a number with a re-runnable script, at zero cost, and the number is
decisive by a wide margin: the tightest achievable joint-fit significance
across all four `ABSORB` pairs is `z_joint=0.81`, 60% below even the
lenient `1.5` bar and 60% below the properly-sourced `2σ` floor itself.
`CHECK 0` anchors every reused formula to exp-072's committed record at
machine precision before anything is claimed, and the widened-window
sweep is honestly phase-swept (min/median/max over 64 nuisance-phase
combinations) rather than reported at one convenient phase. The §6
decision rule directly answers PLAN.md's own outstanding requirement (what
a further non-decisive cycle would mean) in writing, matching the Block-
MINI precedent this program already trusts.

## Sharpest attack (≤150 words)

Three of the five falsifiable bars in §5 (`cond9≥300`, `VIF_Rq≥15`,
`lev_ratio≥0.90`) are asserted, not derived — §0 claims they are "argued
from Iteration 49/50's own already-published figures," but the cited
figure (`cond5≤100`, a 5-column threshold) is never connected by a stated
formula to the 9-column `cond9≥300` bar actually used, and the VIF/
lev_ratio bars have no formula linking them to an achieved error rate at
all. Every one of these bars was written into the document *after* the
script had already computed the real numbers it is scoring — the exact
"see the answer, then set a comfortable bar" shape that R5/R6 exist to
police for stochastic thresholds. The proposal's own §0 argues this
differs categorically (deterministic, no p-fishing) — a defensible
distinction, but it is argued, not gated, and the document never states
it as a limitation of the CLOSURE-CONFIRM band's own evidentiary weight.

## Verdict: **support-with-changes**

The substantive conclusion survives scrutiny at wide margin and does not
depend on the unsourced bars — I independently confirmed the numbers and
the properly-sourced `2σ` comparison alone already closes the case. Change
required before Phase 3 adopts this: either (a) derive `cond9≥300`,
`VIF_Rq≥15`, and `lev_ratio≥0.90` from a stated formula connecting them to
an actual false-positive/false-negative rate, or (b) relabel them
explicitly as "precedent-anchored heuristic margins, not first-principles
bars" in §5, so a future reader does not mistake generous margin for
derivation — matching the standard my own charter is held to.

## Single parameter change that would flip my verdict

If the tightest observed `z_joint(optimistic)` at baseline had been
anywhere in `[1.3, 1.9]` (close to either the `1.5` or `2.0` line) instead
of `0.81`, the undischarged bars would become outcome-determining rather
than cosmetic, and I would move to **oppose** pending a real derivation —
the actual data leaves no such ambiguity this cycle.
