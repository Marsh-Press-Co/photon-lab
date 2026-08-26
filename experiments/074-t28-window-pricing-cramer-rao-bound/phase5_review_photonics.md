# PHASE 5 — REVIEW · PHOTONICS · Panel Iteration 51 · exp-074

*Fresh sub-agent, PHOTONICS charter (PANEL.md: surface interaction,
absorption spectra, angular dependence, scattering cross-sections; owns:
is the proposal's optical response coherent as stated, across wavelength
and angle?). Blind to every other seat's Phase-5 review this cycle. Not
the same instance as the exp-074 Phase-2 PHOTONICS critic; every claim
below independently re-derived against the committed code, not taken on
that predecessor's word.*

---

## 0. What I ran

`desk_check_pricing.py` and `fit_and_calibrate.py`, both unmodified, plus
four scratch extensions (not committed) that call only their own already-
committed functions: (a) a contaminant-period re-scan of `price_pair`
across `T∈[1.8°,5.0°]`; (b) a direct inspection of `per_config_residuals`
and `circular_shift`; (c) a comparison of independent-shift vs. paired-
shift (`sA=sB`) null constructions; (d) a curvature/shape check on the
four configs' own per-config residual pools.

---

## 1. Reproduction — CONFIRMED, bit-exact

Re-ran `fit_and_calibrate.py` end to end: prints `z9 = 0.84 / 5.03 / 1.63
/ 0.34` at C40–C60/C60–C70/C70–C80/C40–C80, matching
`fit_and_calibrate_results.json` and `phase4_results.md` to the digit;
`Combined Verdict: HALT_NULL_MISCALIBRATED_9COL`, all 72 cells FAIL,
i.i.d.-leg worst 11.20×/10.30×/8.70× nominal at α=0.01 for the three free
pairs, circular-shift-leg worst 38.90×/46.10×/44.10× — matches
`phase4_results.md` exactly. Independently re-ran the contaminant-period
scan (PHOTONICS' own Phase-2 finding) directly against `desk_check_pricing.price_pair`:
CLOSURE-CONFIRM holds at `T=1.9608°/3.5°/3.6°`, fails at `T≥3.7°`
(`min_VIF` 31.1→19.0→15.4→13.0, `max_z_joint` 0.81→1.13→1.25→1.36),
matching PHOTONICS' Phase-2 table and Red Team's audit to the last digit.
No reproduction defect anywhere in this record.

## 2. `lev9_Rq` is genuinely a pure design-time computation — CONFIRMED, with one standing caveat

`fit_real_pair()` (`fit_and_calibrate.py:108-124`) computes `lev9_Rq` from
`X9` alone (`row9 = pinv9[4,:]`, `diagM9 = 1-diag(H9)`) — no RNG, no call
into `calibrate_null`, no dependence on the sign-flip Monte Carlo anywhere
in the call graph. `main()`'s own control flow computes all four pairs'
`per_pair_fit` (including `lev9_Rq`) *before* `rng_cal` is even
instantiated. This is genuinely a closed-form property of the design
matrix, not a Monte-Carlo output — the claim in `phase3_synthesis.md` §4
and `phase4_results.md` ("a pure design-time computation... no calibration
Monte Carlo involved") is true as stated.

Git history corroborates genuine pre-registration at the *artifact* level:
commit `3aaae38` (Phase 3) adds `fit_and_calibrate.py`, `NOTES.md`,
`phase3_synthesis.md` but **no** `fit_and_calibrate_results.json` —
`git show 3aaae38:.../fit_and_calibrate_results.json` errors, "exists on
disk, but not in 3aaae38." Commit `af2f381` (Phase 4, 95 seconds later)
adds the results file; `git diff 3aaae38 af2f381 -- fit_and_calibrate.py`
is empty — the script that "officially" ran is byte-identical to what
Phase 3 committed. **Standing caveat, not specific to this cycle:** Phase
3 and Phase 4 in this pipeline execute within the same continuous agent
session, so the git record cannot rule out the synthesizing agent having
run the script once, informally, before writing the "frozen" prose —
exactly the structural weakness LOGBOOK R4 was built around for hand-typed
figures. Nothing here suggests that happened (the predicted failure
*direction and even rough magnitude* — `lev9_Rq≈0.59` vs. exp-073's
`0.79–0.80` — is a genuine, checkable extrapolation from an already-
published mechanism, not a suspiciously exact number), but the record
should not claim stronger process-guarantees than a single continuous
session can actually provide.

## 3. Contaminant-period non-robustness (PHOTONICS' Phase-2 finding) — CONFIRMED again, correctly resolved by Phase 3

Re-verified independently (§0/§1 above): CLOSURE-CONFIRM is not stable
against the choice of assumed contaminant period within `L(T)`'s own
claimed 1.8°–5.0° danger band. Phase 3 correctly withdrew §5/§6 of
`phase1_proposal.md` over this (docket item 1, `phase3_synthesis.md` §1) —
nothing further to add; the resolution is honest and complete.

## 4. The real 9-column fit's `z9=5.03` at C60–C70 — CONFIRMED, genuinely still unresolved

Independently re-fit `X9` to real `delta_ab` (identical formulas to
`fit_and_calibrate.fit_real_pair`): `z9 = 0.843/5.033/1.634/0.345` at the
four pairs, `RSS9/RSS5 = 0.50/0.19/0.06/0.35` — matches THERMODYNAMICS'
Phase-2 table and Red Team's re-derivation to three decimals. This
confirms the central open question is real and correctly left open: a
collinear (`cond9≈480–530`) design can shrink `RSS9` far faster than
`VIF`-only rescaling predicts, so `z_joint(optimistic)` was never a valid
upper bound (Idealization 6, correctly withdrawn). Phase 3/4's decision to
gate this fit behind a calibration test before trusting it, rather than
score it directly, is the right call — and, per §5 below, the gate was
right to fire.

## 5. NEW FINDING (not previously surfaced in this record): the circular-shift leg's "genuinely order-preserving" construction discards the dominant *cross-config* correlation, and this — not necessarily "real θ-adjacent noise structure" — plausibly drives most of its extra severity over the i.i.d. leg

This is the load-bearing finding of my review. `per_config_residuals()`
(`fit_and_calibrate.py:159-185`) builds each config's own per-config
free-period-fit residual, kept as four separate 31-point vectors "so
their theta-adjacent structure can be preserved by a circular shift." The
docstring's claim — "a circular shift preserves 100% of a real residual's
own theta-adjacent autocorrelation structure" — is true for each
*individual* vector in isolation (trivially: `np.roll` cannot alter a
sequence's own pairwise-lag structure). But the null actually used in
`calibrate_null()`'s `circ_leg` is `circular_shift(resid_A, sA) −
circular_shift(resid_B, sB)` with `sA`, `sB` drawn **independently**
(`fit_and_calibrate.py:225-227`). That is a *different* random object
than "the real residual's own structure" — it is the structure of a
newly-constructed difference between two independently re-anchored copies
of two (possibly-related) shapes, and I found the two shapes are, in
fact, almost the same shape:

**Evidence.** Raw, unshifted per-config residual pools are correlated
with each other at:

| Pair | Pearson r (raw, unshifted) | std(resid_a) | std(resid_b) | std(resid_a − resid_b), REAL |
|---|---|---|---|---|
| C40–C60 | **0.9967** | 0.003963 | 0.004438 | 0.000586 |
| C60–C70 | **0.9991** | 0.004438 | 0.004505 | 0.000206 |
| C70–C80 | **0.9995** | 0.004505 | 0.004528 | 0.000140 |

Each config's own residual is ~4× larger than the *difference* between
adjacent configs' residuals — near-total common-mode cancellation, which
is exactly why `delta_ab`'s own residual variance is so small
(`std(delta_ab) = 0.000915/0.000274/0.000158` at the three free pairs,
matching column 4 above almost exactly). This is not noise that is
merely *correlated in θ within one config* — it is **the same shape,
shared across all four `ABSORB` depths** (40/60/70/80 cells), largely
independent of the one parameter (`ABSORB`) that actually varies between
configs. I checked the shape: `corr(residual, u²)` (a simple curvature
proxy in the fit's own `u=sinθ−x̄` coordinate) is **−0.48/−0.62 to
−0.65** at *every one* of the four configs, not concentrated in any one
depth — consistent with QUANTUM's own already-published exp-072 Phase-5
finding that the single-carrier-plus-ramp model is curvature-
misspecified at this window (`R_i` strain-flagged, 3/4 pairs). This is a
**model-misspecification artifact common to the shared fitting basis and
window geometry, not an independent stochastic process per config.**

Independently drawing `sA` and `sB` and differencing destroys this
near-total cancellation. I measured the resulting null-draw magnitude
directly, and compared it to a **paired**-shift construction
(`sA=sB`, which *does* preserve the cross-config correlation, only
re-anchoring both copies identically):

| Pair | real `std(delta_ab)` | independent-shift null, mean `std(y0)` | paired-shift (`sA=sB`) null, mean `std(y0)` |
|---|---|---|---|
| C40–C60 | 0.000915 | 0.005633 (**6.2×** real) | 0.000586 (64% of real) |
| C60–C70 | 0.000274 | 0.006020 (**22×** real) | 0.000206 (75% of real) |
| C70–C80 | 0.000158 | 0.006034 (**38×** real) | 0.000140 (89% of real) |

The paired-shift construction — which respects the empirical fact that
these two "noise" pools are ~99.7–99.95% the same shape — reproduces the
real data's own noise magnitude closely. The independent-shift
construction *as coded* manufactures a null 6×–38× larger, and (by the
same trig identity this program already invoked for T21/T28, exp-069 —
"two sinusoids sharing one frequency sum to a third at that same
frequency regardless of relative amplitude/phase") a *differently
structured* one: the difference of two near-identical shapes at a random
relative offset is itself a shape at the *same* dominant spatial
frequency content as the shared original, just rescaled and rephased —
not a draw from "genuine θ-adjacent noise in `delta_ab`," but an
amplified, decorrelated echo of a shared systematic that the real fitting
procedure was never going to see at that scale.

**Consequence for the write-up.** `phase4_results.md`'s claim — "the
real per-config residuals carry genuine, exploitable θ-adjacent
correlation structure that an i.i.d.-of-any-marginal-shape null cannot
represent" — correctly describes a real property (each residual has real
internal θ-structure), but the *specific* claim that the circular-shift
leg's 3.5×–5.9× worse-than-i.i.d. failure demonstrates this **in a way
relevant to `delta_ab`** is not established, and my evidence above
suggests a large share of that extra severity is a side effect of
independently decorrelating two residual pools that are actually
~99.7–99.95% the *same* shape — the opposite of what a null representing
`delta_ab`'s own noise process should do. This was not, and could not
have been, caught in Phase 2: `fit_and_calibrate.py` did not exist until
commit `3aaae38` (Phase 3), after all five blind critiques and Red Team's
audit had already run (`b5006ad`, earlier). This is a genuinely new
Phase-5 finding, not a re-litigation of anything already on the record.

**What this does and does not change.** It does **not** overturn the
Combined Verdict `HALT_NULL_MISCALIBRATED_9COL` — the i.i.d. leg alone
already independently fails 8.7×–11.2× nominal at α=0.01 (worse than
exp-073's 5-column 5.4×, exactly as the pre-registered, design-time
`lev9_Rq≈0.59` prediction anticipated, per §2 above, with zero dependence
on the circular-shift construction). The instrument-class HALT is sound
on the i.i.d. leg by itself. What needs correction is the *interpretive*
claim attached to the circular-shift leg specifically — "closing the
exact gap... this leg genuinely CAN [and does] expose real correlation
structure" overclaims what was actually demonstrated, in the same shape
(a causal story attached to a real number without independently
re-deriving the causal mechanism) that LOGBOOK R4 already exists to
police, most recently in this exact document (docket item 9b, the
`L(T)`-discrepancy mislabel QUANTUM caught in Phase 2).

## 6. MATERIALS' cost-citation correction — CONFIRMED, simple arithmetic

`n=76` at 51° vs. `n=31` baseline ⟹ 45 new points/config, ×2 configs = 90
calls (not 45), ×4 configs (needed for all four pairs) = 180 calls.
Independently re-derived from `desk_check_pricing_results.json`'s own
`widened_windows` block. Correctly withdrawn as moot in Phase 3 (§1,
docket item 4) since no widened-window spend is authorized this cycle
regardless.

## 7. Charter question: is anything about the angular/wavelength coherence of this cycle's claims incoherent or overstated?

Two things, one already caught and correctly resolved (item 3/§3 above),
one not previously caught (§5 above). Beyond those: no wavelength claim
is made anywhere in this cycle (Idealization 1, "600nm only," correctly
carried forward unchanged) and no angular claim outside 36°–42° is
asserted as measured rather than extrapolated (Idealization 5, phase-swept
widened-window figures explicitly marked "physical extrapolation, not a
measurement"). The one genuinely new, on-charter observation from my own
re-derivation (§5): the leftover per-config residual shape is **shared
across all four `ABSORB` depths**, not depth-dependent — an angular/optical
fact this cycle did not set out to establish but that bears directly on
T28's own still-open mechanism question (§9 below).

## 8. Charter question: does the seventh-cycle decision rule (`phase3_synthesis.md` §6) correctly state what's been learned, or overclaim/underclaim?

**Mostly honest, with one specific overclaim (traced to §5's finding) and
one omission.** The rule's central move — HALT/NEITHER here counts as the
sixth non-decisive cycle, no seventh cycle on the *same instrument class*
without a qualitatively different calibration strategy, underlying
pricing/fitting machinery NOT retired — is well-scoped and does not
overclaim on the headline verdict; it is appropriately conservative (it
does not, e.g., claim `z9=5.03` at C60–C70 is refuted, only that it
"remains genuinely unresolved," which my own re-derivation confirms is
correct). The overclaim is narrower: `phase4_results.md`'s attribution of
the circular-shift leg's extra severity to "genuine, exploitable
θ-adjacent correlation structure" is not established by the construction
actually run (§5). The omission: the rule lists a "qualitatively
different calibration strategy" (Bayesian, a different estimator class,
or PHOTONICS' own WKB model) as the way forward but does not flag the
lesson my own re-derivation surfaces — that a residual-structure/
circular-shift null built from **multiple correlated units** (here, four
`ABSORB` configs sharing common-mode structure) must itself be checked
for whether it preserves or destroys the *cross-unit* correlation
dominant in the real target quantity, not merely each unit's own
autocorrelation, before its extra failure is attributed to "real
structure" rather than the construction's own choice of how units are
recombined. This is a generalizable gap in the same R4/R6/R7 lineage this
cycle itself extended, and belongs in the docket, not just this review.

## 9. On T28's own mechanism question (informational, not gating — this cycle correctly disclaims any mechanism claim, §3 of `phase1_proposal.md`)

§5's finding is also a small, free, on-charter data point for T28 itself:
the leftover-after-best-single-sinusoid-fit shape is essentially the same
shape at `ABSORB=40/60/70/80` (corr(residual,u²)≈−0.5 to −0.65 at every
depth, not concentrated at any one) — i.e., depth-*independent*. That
argues, weakly but for free, against a graded-loss-boundary-reflectance
origin for this particular leftover component (which should plausibly
scale with absorption depth) and toward a shared geometric/model-basis
origin (curvature in the fixed window, or a `PAD`/`TAPER`-tied grid
effect common to all four configs) — consistent with, not contradicting,
this program's own already-established `PAD=ABSORB−40` confound (exp-071,
LOGBOOK Iteration 48) and QUANTUM's exp-072 curvature-misspecification
finding. Not a mechanism claim; a data point the queued WKB/adiabatic
model (§10 below) could use directly.

---

## Verdict

**PARTIAL.** Matches the program's own combined verdict for this cycle
(sixth consecutive non-decisive T28 differential/two-tone cycle) with one
correction: the "secondary prediction confirmed, dramatically" language
for the circular-shift leg should be downgraded from a confirmed
substantive finding to a disclosed, unresolved confound — real narrowing
happened this cycle (R7 adopted and immediately, usefully, applied; the
i.i.d.-leg failure alone is sufficient and decisive; the contaminant-
period non-robustness and the `z_joint(optimistic)` invalidity are both
genuinely closed questions now) but the circular-shift leg's own
causal story is not yet trustworthy as written, and needs its own
Iteration-52 audit before any future cycle cites "3.5×–5.9× worse than
i.i.d." as evidence about the real world rather than about this specific
null construction.

## My ranked top-3 candidate directions for Iteration 52

1. **PHOTONICS' own queued WKB/adiabatic boundary-reflectance analytic
   model** (Iteration-51 queue item 4, already unanimous-adjacent, queued
   and dropped twice before, Iterations 46/47). Zero FDTD, directly
   engages this seat's own charter physics rather than re-verifying
   statistics, and is now additionally motivated by §5/§9 above: an
   analytic admittance-profile model can directly test whether the
   depth-*independent* leftover curvature this cycle surfaced is
   consistent with an ordinary graded-boundary reflectance effect or
   argues for a shared geometric/grid origin instead — a question no
   amount of further null-construction work on the current instrument
   can answer.
2. **Audit and, if it fails, repair the circular-shift null's
   cross-config construction** before it is cited again as evidence of
   "real" residual structure (my own §5 finding). Cheapest concrete next
   step: re-run `calibrate_null`'s `circ_leg` with `sA=sB` (paired
   shifts, preserving cross-config correlation) alongside the current
   independent-shift version, report both, and only then decide whether
   the "genuinely order-preserving" claim survives. Zero FDTD, a few
   lines of code, directly closes a gap this review — not Phase 2 — found.
3. **G40/`PAD` decorrelation** (Iteration-51 queue item 2, ~31 calls,
   still the only queued item that *relieves* rather than merely
   discloses the `ABSORB`-or-`PAD` confound). My own §9 finding sharpens
   its payoff: a PAD-decorrelated config would let a future cycle test
   directly whether the shared, depth-independent curvature-like residual
   this review identified is tied to `PAD`/`TAPER` geometry or genuinely
   varies with `ABSORB` — informative regardless of which queue item 1
   above resolves first.
