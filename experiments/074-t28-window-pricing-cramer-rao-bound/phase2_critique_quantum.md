# PHASE 2 — CRITIQUE · QUANTUM OPTICS · Panel Iteration 51 · exp-074

*Fresh sub-agent, QUANTUM OPTICS charter (PANEL.md: non-classical
absorption, state-dependent or coherent interactions; expressibility
contract — mechanisms enter the bench only as effective classical
parameters, or Red Team strikes them). Not the same instance as the
exp-072 Phase-5 QUANTUM reviewer who originated `L(T)`; everything below
is independently re-derived against the committed code and data, not
cited on that predecessor's authority. Blind to the other six seats'
Phase-2 critiques this cycle.*

---

## 0. Independent re-run

`python3 experiments/074-t28-window-pricing-cramer-rao-bound/desk_check_pricing.py`
reproduces `desk_check_pricing_results.json` and every printed figure in
`phase1_proposal.md` exactly (`CHECK 0 pass=True worst_rel_err=0.00e+00`;
per-pair `cond5`/`z_ols`/`cond9`/`VIF_Rq`/`lev_ratio`/`L(fringe)` all match
to the printed digits). I also independently confirmed `design_matrix` and
`_amp_phase_at` in this script are byte-identical to exp-073's committed
`run.py` (diffed both functions directly — same `psi = -atan2(b,a)`, same
`[1,cos,-sin,u·cos,-u·sin]` basis). CHECK0's claim of exact reproduction is
real, not asserted.

**`L(T)` re-derivation.** The formula (`L=√(A²+B²)`, `A,B` = the fixed
pinv-row-4 dotted with `cos/sin(w_T·u)`) is the correct, complete
re-implementation of the max-over-relative-phase projection my predecessor
defined at exp-072 Phase 5, and it depends **only** on the primary
5-column basis (θ grid, fitted `T_x`, `psi`) — never on any second tone's
phase. I confirmed this by hand-tracing the code.

**But the proposal's own explanation for why its `L(1.9608°)` values
(27.7–28.1) differ from my predecessor's (≈26.8) is wrong.** §2f attributes
the ~4–5% gap to "a slightly different (but equally real, data-fitted)
second-tone phase convention" — impossible, since `L(T)` never references
a second tone. I rebuilt the *pre*-EM-fix basis (`psi=+atan2(b,a)`,
`+sin` columns — the convention active when my predecessor computed its
table at exp-072 Phase 5, before EM's Phase-5 review found the two sign
defects) and got **26.80, 26.80, 27.49, 27.54** at the four pairs —
matching the historical ≈26.8 figure almost bit-for-bit. The true source
of the discrepancy is that this cycle uses the *corrected* (exp-073)
primary-carrier sign convention while my predecessor's table used the
*uncorrected* (exp-072) one. Non-outcome-determining (both `L(T)` values
tell the same qualitative story, and 28.0 is the one anchored to the
record's own currently-trusted basis) but it is a wrong causal story
attached to a real number, the exact pattern LOGBOOK R4 exists to catch —
it should be corrected before this proposal's language is cited further.

**The widened-window `L(T)` collapse is genuine, not a coordinate
artifact.** I independently swept the primary-carrier phase at θ_max =
42°/46°/51° holding the true fitted `T_x` fixed: median `L(1.9608°)` =
31.5 → 12.4 → 2.2, tracking the Rayleigh separation growing monotonically
0.65 → 1.05 → 1.51 widths (`X=ptp(sinθ)` growing 0.0813→0.132→0.189,
computed directly). This is an ordinary resolving-power effect, not an
artifact of the `T_deg↔T_x` conversion (which uses a single, consistently
applied `cos(CENTER_DEG=39°)` factor at every window width — a convention
choice flagged honestly enough by Idealization 5, not silently varied).

## 1. On model misspecification (my own exp-072 finding) and this pricing

My predecessor's exp-072 Phase-5 finding — "the single-carrier-plus-ramp
model is misspecified on this window" (large curvature coefficients,
`R_i` strain-flagged at 2/4 pairs) — is *not* re-litigated here, and
Idealization 3 says so explicitly: this prices that specific model's
two-tone extension, not a from-scratch-optimal estimator. I checked
whether that weakens the CLOSURE-CONFIRM claim. It does not, and if
anything cuts the other way: `z_joint(optimistic)` at baseline
(0.54–0.81) clears its `<1.5` bar with 46–60% margin, so even a
substantially worse true noise floor from unmodeled misspecification only
reinforces "this specific fit cannot resolve here." Misspecification
would make the *pricing* pessimistic in exactly the direction the
retirement claim needs, not the direction that would undermine it — a
subtlety the task brief invited me to check both ways, and it resolves in
the proposal's favor at baseline.

**It does not resolve as favorably for the 51° "further-spend" band.**
That band's `z_joint∈[2.55,4.10]` figures are computed by dividing the
*current-window* `z_ols` (built on **naive OLS SE**) by the widened
window's VIF-only SE-inflation — nothing in that chain accounts for a
fact already established in this exact record: exp-072 Phase-5's own EM
review (`phase5_review_em.md` D3, table) found the naive OLS SE
understates a design-respecting residual bootstrap's SE by **1.56–2.31×**
(carrier held fixed) to **2.27–4.70×** (carrier refit) at these same four
pairs. Idealization 6 flags that real data "could show a worse effective
SNR" in general terms but never names this specific, already-quantified,
same-record correction factor. Chaining even the smallest established
factor (1.56×) onto the reported 51° `z_joint` values:

| Pair | z_joint (optimistic, as reported) | ÷1.56 (min established factor) | ÷2.27 (carrier-refit factor) |
|---|---|---|---|
| C40–C60 | 4.10–4.14 | 2.65 | 1.82 |
| C60–C70 | 2.55–2.57 | 1.65 | 1.13 |
| C70–C80 | 3.59–3.60 | 2.30 | 1.58 |
| C40–C80 | 3.94 | 2.53 | 1.74 |

At the conservative end the "≥3 of 4 pairs clear 2σ" WIDENED-WINDOW band
degrades to 1 of 4; even at the mild end it is 2 of 4. This is the one
recommendation in the proposal that authorizes new spend (~45 FDTD
calls), and it is not nearly as robust as its stated 4/4 margin suggests
once the record's own already-published SE correction is applied.

## 2. R6 / `G0-e` scope check

The script never scores a p-value against a constructed null and never
emits a `RESOLVED`-class verdict; `z_ols` is a raw OLS statistic used only
as an input to a *design* bound, and the docstring/§0 disclosure
explicitly disclaims running "a null-calibration test itself." I find no
place where the proposal implicitly claims R6/`G0-e(ii)` compliance it
hasn't earned — its own scope (design-only power/conditioning bound, not
a scored statistical test) is stated honestly everywhere it matters,
including in the pre-committed decision rule (§6), which conditions any
future real fit on "its own fresh `G0-e(ii)`-style calibration test."

---

## Steel-man (≤150 words)

This is the right instrument, correctly executed. It turns two informal,
hand-typed Phase-5 numbers into committed, reproducible code, verifies
its own basis against the record's ground truth (`CHECK0`,
`worst_rel_err=0.00e+00`) before citing a single downstream figure, and
prices all four pairs instead of one. The `L(T)` formula is exactly and
completely re-derived from its original definition, and its widened-window
collapse is a real Rayleigh-resolution effect I reproduced independently,
not a unit-conversion trick. The baseline CLOSURE-CONFIRM clears its
threshold with 46–60% margin — comfortably wide enough to absorb the
model-misspecification concern my own predecessor raised, since a worse
true noise floor only reinforces this verdict. Scope discipline around
R6/`G0-e` is honest throughout. The formal-retirement claim, restricted to
this exact 5-column basis at 36°–42°, is earned.

## Sharpest attack (≤150 words)

The one recommendation that spends new budget — WIDENED-WINDOW-LICENSES-
FURTHER-SPEND at 51°, "z_joint clears 2σ at 4/4 pairs" — is built by
dividing the *current-window* `z_ols`, which uses **naive OLS SE**, by the
widened window's VIF-only inflation. It never applies the SE-inflation
factor this exact record already established for these exact four pairs
(exp-072 Phase-5, EM's own residual bootstrap: 1.56–2.31× carrier-fixed,
2.27–4.70× carrier-refit). Chaining even the smallest of those factors
onto the reported figures drops the pass count from 4/4 to as few as 1/4.
Idealization 6 gestures at "could show worse SNR" but never names or
applies this specific, already-quantified, same-record number — a
material omission given the whole cycle's stated purpose is pricing with
nothing hand-waved. The baseline retirement claim is unaffected (its
margin absorbs this easily); the 51°-spend recommendation is not.

## Verdict

**Support-with-changes.**

## Parameter change that would flip my verdict to full support

Add one pre-registered column to the 2e/§5 widened-window table: `z_joint`
divided by an additional, named SE-inflation factor of ≥1.6× (the
established minimum from exp-072 Phase-5's own residual bootstrap on
these four pairs), and re-score the WIDENED-WINDOW-LICENSES-FURTHER-SPEND
band against that adjusted figure before it is allowed to authorize the
~45-call FDTD extension. If ≥3 of 4 pairs still clear 2σ under that
correction, I support the proposal without reservation; my own quick
check above suggests it is genuinely marginal (1–2 of 4, depending on
which established factor is used), so this must be resolved on the record
before any new spend, not deferred.
