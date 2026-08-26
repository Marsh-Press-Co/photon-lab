# PHASE 3 — SYNTHESIS · Panel Iteration 51 · exp-074
## Director's resolution: withdraw the pricing-only closure claim, run the actual fit, gate it properly

*Director synthesis, post Phase 2 (five blind critiques + Red Team's audit,
all in this directory). Per PANEL.md: the Director does not vote in Phase
2 and must state, in writing, which criticisms are accepted and which are
overridden, and why. Below: every one of the Phase-2 Red Team audit's ten
docket items is accepted in full — none overridden. This is itself
unusual (compare exp-072/073, where Red Team overrode several critics'
specific remedies with independently-derived corrections) and reflects
that this cycle's own Red Team audit already independently re-derived,
computationally, every load-bearing claim from all five blind critiques
before I ever saw it — there is nothing left for the Director to
re-litigate that was not already re-verified from scratch.*

---

## 1. Docket resolution (Red Team's `phase2_redteam_audit.md` §9, all ten items)

| # | Item | Disposition |
|---|---|---|
| 1 | Withdraw §5 CLOSURE-CONFIRM / §6's "independent of which null" language (baseline window) | **Accepted, implemented.** `phase1_proposal.md` §5/§6 stand in the record as originally written (house convention: correct forward, do not silently rewrite), superseded by this document and `phase4_results.md`. |
| 2 | Withdraw Idealization 6's "cannot do better...even in principle" claim | **Accepted.** Confirmed false by construction: see §3 below, the real 9-column fit. |
| 3 | Withdraw/caveat the WIDENED-WINDOW-LICENSES-FURTHER-SPEND finding | **Accepted.** No FDTD spend is authorized by this cycle at ~51° or any other widened window. |
| 4 | Correct the ~51° FDTD cost citation (~90/~180 calls, not ~45) | **Accepted, moot but recorded** — no widened-window spend is being proposed this cycle regardless. |
| 5 | Derive or relabel `cond9≥300`/`VIF_Rq≥15`/`lev_ratio≥0.90` as heuristic | **Accepted.** All three are relabeled below (§5) as precedent-anchored heuristic margins, not first-principles bars, and are not used to gate anything in this cycle's own new test. |
| 6 | Adopt or reject candidate standing rule "R7" | **Adopted**, verbatim in substance, see §2. |
| 7 | Run the actual 9-column fit + null-calibration test on current data | **Adopted as this cycle's own Phase 3/4 design** — the entire remainder of this document and `fit_and_calibrate.py`. |
| 8 | State the "seventh non-decisive cycle" decision rule in writing | **Done, §6 below**, pre-committed before this cycle's own official run. |
| 9 | Two small citation corrections (QUANTUM's superseded bootstrap figures; the `L(T)` discrepancy's real cause) | **Accepted, disclosed** — no code in this cycle depends on either number. |
| 10 | The three-document-old "Iteration 5, exp-027" mislabel | **Accepted as out-of-scope**, not touched this cycle (Red Team's own ruling: not chargeable here). |

**No item overridden.** Red Team's own audit already independently
computationally re-derived every load-bearing claim from all five blind
critiques before reaching the Director; there is no further adjudication
left to perform on the substance, only implementation.

---

## 2. R7 adopted as a standing house rule (LOGBOOK.md, pending this cycle's close)

> **R7 — a conditioning/VIF-based pricing of an UN-FIT multi-tone or
> multi-parameter design is necessary, not sufficient, evidence for a
> closure or detection claim.** Collinearity can make a design's realized
> residual variance, once actually fit to data, either larger OR smaller
> than a naive Gram-matrix-only (VIF) extrapolation predicts — a
> conditioning number alone cannot distinguish these. The design must be
> fit to the real data and the resulting estimate must pass its own
> null-calibration test (per R6) before either a closure ("this route
> cannot work") or a detection ("this route found something") claim may be
> scored. Generalizes R6 one level upstream: R6 already requires
> calibrating a *fitted* coefficient's significance test; R7 closes the
> loophole of pricing a design's conditioning *instead of* fitting it, and
> treating that price as if it carried the fit's own calibrated
> significance.

This is directly, empirically confirmed by this cycle's own §4 below: the
5-column leverage mechanism (R6, exp-073) predicted, and this cycle's own
9-column extension directly measures, an even worse null-calibration
failure than pricing alone would have suggested from `lev_ratio` scaling
arguments.

---

## 3. This cycle's own Phase 3/4 design: the actual fit, properly gated

Red Team's docket item 7 (`phase2_redteam_audit.md` §9.7) specifies the
single highest-information, lowest-cost action available: fit the real
9-column two-tone design to real `delta_ab` data (already sketched,
independently, by two of five blind Phase-2 critics — THERMODYNAMICS'
attack and Red Team's own re-derivation), under a genuine null-calibration
gate before the fit's own significance is trusted. Implemented in
`fit_and_calibrate.py`, this directory. Full derivation and code
docstrings there; summary:

**The fit.** `R_q` (index 4) fit within the full `X9` two-tone model
(`coef9 = pinv(X9) @ delta_ab`), at each pair's own real fitted primary
carrier and T21's own established fringe (`T=1.9608°`, phase fit from the
real common-mode `C̄`, never hand-set) — identical construction to
`desk_check_pricing.py`'s own `price_pair`, not re-derived.

**The null.** A direct generalization of exp-073's own T2-3 sign-flip
construction, one level up: reduced model = `X9` with column 4 (`R_q`)
removed (`X8`, 8 columns); full model = `X9`. Sign-flip the full model's
own residual, add back the reduced model's own fit, refit `X9`, extract
`R_q^surr`. This tests whether `R_q` remains significant **within** the
two-tone model — i.e., whether the original 5-column finding survives
once T21's fringe is fit jointly, not merely priced through its Gram-
matrix conditioning (closing exactly the gap PHOTONICS'/THERMODYNAMICS'
Phase-2 attacks named).

**The calibration gate — mandatory, HALT-style, before any real-data
p-value is trusted (R6/R7).** Two legs:
- **i.i.d. leg**: pure Gaussian H₀ noise at `σ∈{0.0005,0.002,0.008}`
  (exp-073's own `G0-e(ii)` sigma grid, same units), `R_q`-true `=0` by
  construction.
- **Circular-shift leg — genuinely order-preserving, new this cycle.** A
  circular shift of each config's own REAL per-config carrier-fit
  residual (exp-069/071's C40/C60/C70/C80, native `n_grid=400` fit —
  exactly `build_residual_pool`'s per-config inputs, kept as four
  SEPARATE 31-point vectors rather than pooled and flattened). A circular
  shift preserves 100% of a real residual's own θ-adjacent
  autocorrelation structure (every pairwise lag is exactly preserved,
  only the θ-anchor changes) — closing the specific gap exp-073's own
  Phase-5 erratum named: its own "residual-structure" leg pooled/
  flattened real residuals into an i.i.d. bootstrap, which measurably
  could not (and did not — Pearson r=0.907 against its own i.i.d. leg)
  differ from pure noise. This leg genuinely can, and (§4, below) does.

`K_CAL=1000` synthetic draws/cell, `N_SURR_CAL=4000` sign-flip surrogates
per draw (a disclosed cost economy vs. the real-data scoring's own
`N_SURR=20000` — calibration needs many draws at moderate surrogate
resolution; real-data scoring needs few draws at high surrogate
resolution). PASS bar: empirical rejection rate inside
`α±3√(α(1−α)/K_CAL)` at **every** `(leg, condition, α)` cell — identical
tolerance convention to exp-073's own `G0-e(ii)`.

**Fixed seeds, frozen at this commit, unchanged thereafter**:
`SIGN_FLIP_SEED=74051`, `CAL_SEED=74052` (`fit_and_calibrate.py`
module-level constants).

---

## 4. FROZEN PREDICTIONS (committed here, before the official Phase-4 run)

**Primary, falsifiable prediction: the 9-column null-calibration gate
WILL FAIL (`HALT_NULL_MISCALIBRATED_9COL`), and by a comparable-or-LARGER
margin than exp-073's own 5-column finding (1.7×–5.7× at α=0.10/0.01).**

Reason, computed and disclosed in advance (not fit to the outcome — this
is a closed-form design property, independent of `delta_ab`'s own real
values): the leverage-weighted ratio driving this failure mode,
`lev9_Rq = Σ row9ᵢ²·diagM9ᵢ / Σ row9ᵢ²` (`row9 = pinv(X9)[4,:]`,
`diagM9 = 1−diag(X9·pinv(X9))`), measures **0.586–0.596** across the four
pairs at the real fitted carriers — computed once, before this cycle's
own official run, directly in `fit_and_calibrate.fit_real_pair`. This is
markedly LOWER (worse) than exp-073's own 5-column figure (0.79–0.80),
which already produced 1.7×–5.7× rejection-rate inflation. A lower ratio
predicts larger anti-conservative bias (the mechanism, per exp-073's own
independently-verified derivation: `E[Var(R_q^surr)]/Var(R_q^obs)` scales
with this ratio). `n−p9=22` degrees of freedom (vs. `n−p5=26`) further
concentrates leverage relative to the model's own residual budget.

**Secondary, falsifiable prediction: the circular-shift leg will fail by
a LARGER margin than the i.i.d. leg**, because it is the first leg in
this sub-thread's five-cycle history to test genuine θ-correlated
residual structure rather than i.i.d. noise of any marginal shape — if
the model misspecification QUANTUM's own exp-072 Phase-5 review
identified (`R_i` strain-flagged, curvature coefficient large at 3/4
pairs) leaves real low-frequency structure in the per-config residuals,
a structure-preserving leg should expose it where a flat/i.i.d. leg
cannot, by construction.

**If BOTH predictions are wrong** (calibration passes, or the circular
leg passes while the i.i.d. leg fails) — that is itself a first-order
surprise for this program and must be reported as such, not absorbed
quietly.

**Scored predictions, reached only if calibration PASSES (i.e., contrary
to the primary prediction):**
- `n_holm_p05 ≥ 2` of the three free pairs (Holm-adjusted, `p≤0.05`) ⟹
  `CONFIRM_R_Q_SURVIVES_JOINT_FIT` — R_q's original 5-column significance
  is real even once T21's fringe is fit jointly.
- `n_relaxed_p10 = 0` (no pair even reaches relaxed `p≤0.10`) ⟹
  `REFUTE_R_Q_DOES_NOT_SURVIVE_JOINT_FIT`.
- Anything else ⟹ `NEITHER`.

**Combined Verdict, computed in this exact order** (in code,
`fit_and_calibrate.main`): calibration FAIL ⟹ `HALT_NULL_MISCALIBRATED_9COL`
(no pair scored) → else the scored predicate above.

---

## 5. Falsifiable-bar provenance (VISION's docket item 5, applied forward)

Per the docket, `cond9≥300`/`VIF_Rq≥15`/`lev_ratio≥0.90` from
`phase1_proposal.md` §5 are **relabeled here, explicitly, as
precedent-anchored heuristic margins, not first-principles bars** — they
gate nothing in this cycle's own new test (§3–4 above use only the
Monte-Carlo tolerance band `α±3√(α(1−α)/K)`, which IS first-principles:
it is the exact sampling distribution of a Bernoulli rate estimator under
the null that the true rate equals `α`).

---

## 6. The seventh-cycle decision rule (Red Team docket item 8, binding, pre-committed)

Iterations 46–51 are, by the time this document is committed, **six
consecutive T28 differential/two-tone cycles without a resolved pair**
(exp-069 desk-check batch, exp-070 mechanism batch, exp-071 causal test,
exp-072 differential fit, exp-073 corrected re-issue, exp-074 this
cycle) — the fifth-through-sixth in Red Team's own count depending on
convention, now unambiguous at six once this cycle's own pricing-only
claim (which would have made it "resolved, by pricing") is properly
withdrawn per §1.

**Pre-committed, in writing, before this cycle's own result is known
(beyond the primary prediction in §4, which is a HALT, not a resolution
either way):**

> If this cycle's own official run lands `HALT_NULL_MISCALIBRATED_9COL`
> or `NEITHER` (i.e., anything short of a clean `CONFIRM` or `REFUTE` on
> whether `R_q` survives the joint two-tone fit), that constitutes the
> **sixth** non-decisive cycle on this exact sub-thread, and **no
> seventh cycle attempting the SAME instrument class — a sign-flip or
> permutation null on this ramped-quadrature OLS basis, at any window
> width, single-tone or multi-tone — is authorized without a qualitatively
> different calibration strategy** (e.g., a fully Bayesian treatment with
> an informative, independently-sourced prior on the contaminant's
> amplitude; a genuinely different estimator class, not merely a
> different null construction on the same basis; or PHOTONICS' own
> queued WKB/adiabatic boundary-reflectance analytic model, which
> requires no fit or null at all). This is the differential/two-tone
> sub-thread's own Block-MINI-style formal-retirement trigger, matching
> PANEL.md's own precedent (exp-069, Iteration 46): a properly-powered,
> honestly-executed, non-decisive result is retired, not deferred a
> seventh time. **The underlying pricing/fitting instrument
> (`desk_check_pricing.py`, `fit_and_calibrate.py`, R6, R7) is NOT
> retired** — it is exactly the kind of reusable, generalizable machinery
> this program keeps regardless of what it finds about T28 specifically,
> and remains available to any future carrier/phase-conditioned fit in
> this program, on different data.

If instead this cycle lands a clean `CONFIRM` or `REFUTE`, this rule does
not fire — a decisive result, however narrow, is real forward motion and
does not trigger formal retirement.

---

## 7. Idealizations (carried forward, plus new)

1–9. All nine of `phase1_proposal.md` §4's idealizations stand unchanged
   (600nm only; `ABSORB` not a material; single-carrier-plus-ramp basis;
   T21's fringe as the only named contaminant; widened-window figures as
   extrapolation; `z_joint(optimistic)` withdrawn per §1 above rather than
   idealized; the curvature caveat; `lev_ratio` necessary-not-sufficient;
   no energy sidecar).
10. **New: the calibration gate's own Monte-Carlo precision.**
    `K_CAL=1000` gives a 3σ tolerance band of roughly `±1–3` percentage
    points depending on `α` — wide enough that a PASS at exactly the
    boundary would be a weak pass, not examined further here since the
    primary prediction is a clean, wide-margin FAIL (§4), not a
    boundary case.
11. **New: the circular-shift leg tests ONE specific alternative to
    i.i.d. Gaussian noise (real per-config residual structure,
    circularly re-anchored), not every possible correlation structure.**
    A PASS on this leg would not certify robustness to, e.g., a
    genuinely different autocorrelation length scale than the one the
    real residuals happen to exhibit.
12. **New: `N_SURR_CAL=4000` (calibration) vs. `N_SURR=20000` (real-data
    scoring)** is a disclosed cost/precision tradeoff, not a hidden one —
    calibration needs `K_CAL` independent draws at moderate surrogate
    resolution; real-data scoring needs one draw at high resolution.

---

## 8. Cost note

Zero FDTD. Zero `lab/` diff. `fit_and_calibrate.py` runs in ~25s, single
core (measured, this cycle's dev run) — `K_CAL×(24 cells iid + 24 cells
circ)×3 pairs` calibration draws, each a `N_SURR_CAL=4000`-surrogate
sign-flip test, plus the real-data `N_SURR=20000` scoring pass (reached
only if calibration passes).
