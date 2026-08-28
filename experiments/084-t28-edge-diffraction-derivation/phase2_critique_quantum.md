# PHASE 2 — CRITIQUE · QUANTUM OPTICS · Panel Iteration 61 · exp-084

## Steel-man (150 words)

LEG (a)'s SUPPORT rests on numbers I independently reproduced bit-for-bit
from `derivation_results.json`: `p_model_a=2.533834586...°`,
`R²=0.369655809...`, `rel_dev=0.108466` against `P_edge_A=2.8421052632°` —
no hand-typed figures (R4). The R5 specificity control is also arithmetically
correct: re-deriving the `linspace(1,15,60)` grid gives exactly `5/60 =
8.333%` clearing `rel_dev≤0.20`, and I confirmed (`n`=20…10000) this
converges to the true continuous fraction `≈7.54%` — the `n=60` grid is not
manufacturing the headline number, and it is genuinely tighter than
exp-083's own 99.3% phase-shift non-finding. Anchor 1's classical-limit
cross-check (the deliberately-paraxial substitute collapsing the residual
from `9.25e-2` to `3.29e-3`) is a real, independent validation of the
underlying Green's-function machinery. The pre-registered structural
corollary (`max|C80-C40|_model = 0.0` exactly, checked not asserted) is
disclosed honestly rather than buried. Unusually disciplined self-scoring.

## Sharpest attack (150 words)

The R5 target-sweep answers "is this match specific to `P_edge_A`?", not
"is `R²=0.3697` distinguishable from chance?" — a different R5-family
question this cycle never asks of itself. I built the missing null: run
the SAME `free_period_search` (400-pt grid, `[1,4]°`) on order-destroyed
copies of the identical 31-point `c_a` curve. Full permutation (2000
draws): `P(null R²≥0.3697)=0.029` — looks significant. But this program's
own established "harder companion" (R6/R7, exp-083's own circular-shift
reversal of the two-tone claim, one cycle ago) is exhaustive circular
shift, which preserves the curve's autocorrelation: all 30 nontrivial
shifts give mean `R²=0.427`, max `0.675`, and **14/30 (46.7%) meet or
exceed 0.3697**. Under the exact null-construction discipline this panel
adopted to kill a naive-significant finding last cycle, `R²=0.3697` is
unremarkable — the curve's own smooth wiggliness, at any phase, produces
comparable fits. LEG (a)'s SUPPORT has not been tested against the null
this program itself now requires.

## Verdict: support-with-changes

The near-field re-derivation is genuine, well-instrumented progress (a
real diffractor mechanism finally modeled, `P_edge_B`'s far-field-formula
category error correctly diagnosed, LEG (b) honestly withheld on a
directly-verified, convergence-tested Anchor-2 failure — this is
exactly the caution the R4 discipline exists to produce). But LEG (a)'s
"FINAL VERDICT: SUPPORT" is not yet earned: `R²=0.3697` clears the
specificity-over-*targets* sweep but has never been checked against a
null distribution of `R²` under a period-free process using this bench's
own search machinery — the check this program itself performed one cycle
ago (exp-083) precisely because a specificity-style control and a
null-under-noise control are not the same test and can disagree. Here
they do disagree, sharply (permutation `p≈0.03` vs. circular-shift
`p≈0.47`), the identical divergence shape that reversed exp-083's
two-tone claim. Required change: downgrade LEG (a) to INCONCLUSIVE pending
a pre-registered, order-preserving null-calibration test (circular-shift
or an AR(1)-matched surrogate, per QUANTUM's own already-sketched
Iteration-61 design cited in LOGBOOK Iteration 60) before "genuine
periodic structure" is asserted. The structural corollary should also be
foregrounded, not left as a caveat: this mechanism is provably incapable
of producing the real, non-zero `C80(θ)−C40(θ)` signal that motivated
T28 in the first place, so even a fully-vindicated LEG (a) explains a
component nobody doubted existed, not the anomaly itself.

## Parameter change that would flip my verdict

If the exhaustive circular-shift null (30 shifts of the real `c_a` curve,
same 400-point `[1,4]°` search) had instead shown `R²=0.3697` in the tail
— say `P(shift R² ≥ observed) ≲ 0.10` — rather than the `46.7%` I
measured, I would support LEG (a)'s SUPPORT as filed.
