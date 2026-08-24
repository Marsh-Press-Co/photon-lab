# PHASE 2 — CRITIQUE · VISION SCIENCE · Panel Iteration 43 · exp-066 proposal

*Fresh sub-agent, blind to the other four seats' critiques this cycle. Preserved
verbatim as delivered.*

## 1. Steel-man (148 words)

The proposal's scope-definition is textually correct, not just
plausible — I verified it directly: `experiments/041-t20-angle-audit/
results.json::block_main` contains exactly 30 rows, θ∈{36,37,38,39,40}×±,
no 35° present. `FALLBACK_ANGLES` and `MAIN_ANGLES` genuinely don't
overlap in exp-041's own committed data, so "Block MAIN, item #1" is a
real, distinct, closeable unit, not an arbitrary slice. The G-1′
bit-exact gate, the reuse of `settled_sweep_steps2800_diagnostic.json`'s
own C40 anchor, and committing falsifiable bands before any run are all
faithful to house discipline. Crucially for my own charter: T21's
magnitude fit was *my own* seat's exp-042 build, and its NOTES.md (line
337) explicitly assumed "settling in the ORIGINAL FDTD runs is otherwise
assumed complete, not re-litigated here" — an idealization T27 now
falsifies. Closing that gap is legitimate VISION-relevant work, not
merely PHOTONICS' own charter question in disguise.

## 2. Sharpest attack (150 words)

The 38-call budget touches zero cells outside `MAIN_ANGLES{36–40}°`,
which structurally excludes ±35° and all four interior
`FALLBACK_ANGLES`. Those are exactly the angles that feed actual
constraint-3 PASS/MARGINAL scoring against my own C_thr ladder —
P-VIS42-7's MARGINAL verdict, and the whole `off_pass`/`off_bracket`/
`off_lab` lineage. My own Iteration-42 Phase-5 review ranked
settling-checking those angles #1 and #2, *ahead* of Block MAIN. This
proposal spends its own "cost is trivial, minutes not hours" argument to
justify full 30-row MAIN closure over a 12-row partial reuse — but never
applies that identical argument to fold in ±35° (+6 calls) or the
interior angles (+21 calls), which would cost the same order of
magnitude and would actually move a live constraint-3 verdict. The
result: PHOTONICS' T21 fit gets closed this cycle; whether any
constraint-3 citation this program has ever issued survives settling
correction stays exactly as open as Iteration 42 left it — deferred to
an unscoped, unbudgeted "item #2."

## 3. Verdict: **support-with-changes**

## 4. Parameter change that flips my verdict

Broaden §2's new-call parameter table from `MAIN_ANGLES{36,37,39}×±×3λ`
to the union with `{±35}×3λ` (the 6 cells) at STEPS=2800 — folding
PLAN.md item #2's cheapest, highest-VISION-stakes bullet into this run
rather than deferring it. That directly tests whether P-VIS42-7's
MARGINAL bucket survives, at the marginal cost the proposal's own cost
argument already licenses.
