# exp-074 — ELECTROMAGNETISM's window pricing, then the actual fit + its own null-calibration test

**Panel Iteration 51.** Lead: ELECTROMAGNETISM (by rotation). Director
synthesis post Phase 2 (five blind critiques + Red Team's audit, verdict
PROCEED-WITH-MANDATORY-FIXES, ten-item docket, **zero items overridden** —
full record in `phase1_proposal.md`, `phase2_critique_{photonics,
materials,thermodynamics,quantum,vision}.md`, `phase2_redteam_audit.md`,
`phase3_synthesis.md`).

## Mandate

PLAN.md's Iteration-51 queue, item 1 (near-unanimous #1 across all six of
exp-073's Phase-5 seats, `phase5_redteam_audit.md` §6.2): "price the
window" — decide, at zero FDTD cost, whether θ∈[36°,42°] can ever support
a carrier-conditioned discriminator (the differential/beat-fit approach
five prior T28 cycles have spent on this thread) at achievable SNR, for
any correctly-calibrated null.

## Setup

**Phase 1** (ELECTROMAGNETISM): formalized two informal, uncommitted
exp-072 Phase-5 figures (EM's `cond(X9)=529` two-tone conditioning pricing,
QUANTUM's `L(T)` leakage function) into `desk_check_pricing.py`, run
against the real fitted carriers of all four `ABSORB` pairs. Reproduced
both prior figures exactly; extended to widened-window candidates.

**Phase 2** (five blind critiques + Red Team): two of five critics
(PHOTONICS, THERMODYNAMICS), by two independent methods, found the
proposal's headline CLOSURE-CONFIRM claim (and its §6 formal-retirement
decision rule) does not survive: (a) scanning the assumed-contaminant
period across `L(T)`'s own claimed 1.8°–5.0° danger band breaks the
closure result from ~3.7° onward; (b) actually FITTING the real 9-column
design to real data (never done by the pricing-only script) shows the
true joint-fit significance EXCEEDS the proposal's own "optimistic upper
bound" at 3 of 4 pairs, by up to 9.3× — the conditioning-only method
cannot, in principle, certify a null result. QUANTUM (support-with-
changes) independently found the widened-window recommendation omits an
already-established SE-inflation correction that, applied, drops "4/4
clear 2σ" to 0/4. MATERIALS and VISION found a cost-citation error and
three unsourced falsifiable bars, respectively. Red Team's audit
independently re-derived every one of these attacks computationally and
confirmed all five in full — zero overridden — and added a sixth finding
of its own (a new candidate standing rule, "R7": pricing an un-fit
design's conditioning is not a substitute for actually fitting and
null-calibrating it).

**Phase 3** (this Director): adopted R7; withdrew §5/§6 of the Phase-1
proposal as written; designed and built `fit_and_calibrate.py` — the
actual 9-column fit (does `R_q`, the mechanism-relevant coefficient,
survive once T21's fringe is fit jointly rather than merely priced?),
gated behind a mandatory null-calibration test with two legs: i.i.d.
Gaussian noise, and — new this cycle, closing a gap exp-073's own Phase-5
erratum flagged as queued for Iteration 51 — a genuinely order-preserving
circular-shift leg built from each config's own real per-config residual.
Predictions frozen (below) BEFORE the official run, including an
analytic, pre-computed reason to expect the calibration gate to FAIL, and
by a larger margin than exp-073's own 5-column precedent.

## FROZEN PREDICTIONS (committed here, before Phase 4's official run)

Full specification: `phase3_synthesis.md` §3–6 (design, seeds, formulas,
decision rule) — single source of truth, not re-transcribed here (R4).

**Primary prediction: `HALT_NULL_MISCALIBRATED_9COL`**, i.e. the
9-column null-calibration gate FAILS, by a comparable-or-larger margin
than exp-073's 5-column finding (1.7×–5.7× at α=0.10/0.01). Reason,
computed and disclosed in advance: `lev9_Rq` (the leverage-weighted ratio
driving this failure mode) measures 0.586–0.596 across the four pairs —
lower (worse) than exp-073's own 5-column 0.79–0.80.

**Secondary prediction: the circular-shift (order-preserving) leg fails
by a larger margin than the i.i.d. leg** — the first test in this
sub-thread's five-cycle history of genuine θ-correlated residual
structure rather than any i.i.d. marginal shape.

**If calibration instead PASSES** (contrary to the primary prediction):
score `R_q`'s significance within the two-tone fit via a Holm-adjusted
sign-flip p-value at the three free pairs. `n_holm_p05≥2` ⟹
`CONFIRM_R_Q_SURVIVES_JOINT_FIT`; `n_relaxed_p10=0` ⟹
`REFUTE_R_Q_DOES_NOT_SURVIVE_JOINT_FIT`; else `NEITHER`.

**Seventh-cycle decision rule (binding, `phase3_synthesis.md` §6):** if
this cycle lands `HALT` or `NEITHER`, that is the sixth consecutive
non-decisive T28 differential/two-tone cycle (Iterations 46–51), and no
seventh cycle on the SAME instrument class (a sign-flip/permutation null
on this ramped-quadrature OLS basis, any window, single- or multi-tone)
is authorized without a qualitatively different calibration strategy. The
underlying pricing/fitting machinery itself is not retired.

## Idealizations

See `phase1_proposal.md` §4 (nine items, all still binding except
`z_joint(optimistic)`, withdrawn) plus `phase3_synthesis.md` §7 (three
new items: calibration Monte-Carlo precision, the circular-shift leg's
own scope, the `N_SURR_CAL` vs `N_SURR` cost tradeoff).

## Result

**Combined Verdict: `HALT_NULL_MISCALIBRATED_9COL`.** Both frozen
predictions confirmed. The i.i.d. leg fails 8.7×–11.2× nominal at
α=0.01 (worse than exp-073's 5-column 5.4×, as predicted from the lower
`lev9_Rq`). The new, genuinely order-preserving circular-shift leg fails
far worse still — 38.9×–46.1× nominal at α=0.01, 3.5×–5.9× worse than the
i.i.d. leg at every α — the first test in this five-cycle sub-thread to
show a real, structure-preserving null leg is NOT statistically
indistinguishable from an i.i.d. one (exp-073's own pooled leg was,
`r=0.907`; this one measurably is not). No pair's `R_q`-within-the-two-
tone-fit significance was ever scored. Full detail: `phase4_results.md`.

## Learned

The real 9-column fit's own `z9=5.03` at C60–C70 (independently found in
Phase 2 by THERMODYNAMICS and Red Team) remains genuinely unresolved —
this cycle establishes WHY it cannot currently be resolved with this
instrument, rather than resolving it: the null construction needed to
test it is badly miscalibrated, worse on realistic (θ-correlated) noise
than on idealized (i.i.d.) noise. R7 (adopted this cycle) is directly,
empirically confirmed on its first application: a design-only
conditioning bound (`lev9_Rq≈0.59`, computed in Phase 1/3 before any
calibration Monte Carlo ran) correctly predicted the DIRECTION of this
failure but could not have predicted its MAGNITUDE, particularly the
5× additional degradation on genuinely correlated noise — only actually
fitting and calibrating exposed that. Per the pre-committed seventh-cycle
decision rule (`phase3_synthesis.md` §6): this is the sixth consecutive
non-decisive T28 differential/two-tone cycle (Iterations 46–51), and no
seventh cycle on the same instrument class (a sign-flip/permutation null
on this ramped-quadrature OLS basis, any window, single- or multi-tone)
is authorized without a qualitatively different calibration strategy.

## Next

*(Placeholder — see PLAN.md's Iteration-52 queue, Director's update, post
Phase 5.)*
