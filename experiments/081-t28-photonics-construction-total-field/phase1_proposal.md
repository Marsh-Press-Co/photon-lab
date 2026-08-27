# PHASE 1 — PROPOSAL · THERMODYNAMICS · Panel Iteration 58 · exp-081
## Building PHOTONICS' construction AS ORIGINALLY SPECIFIED — total field,
## scored via a free-period fit against REAL T28 reference periods — plus
## the Iteration-58 Tier-0 batch (EM gate re-run, THERMO energy budget,
## MATERIALS hygiene)

**Seat: THERMODYNAMICS** (where absorbed energy goes; owns the per-proposal
energy sidecar — absorbed power → temperature rise → emission band →
detectability; *expressibility contract: the sidecar is a post-run analytic
calculation, not an FDTD output, and is labeled as such*). Lead this cycle,
by rotation.

Read, in order: `PANEL.md` in full, `AGENTS.md` in full, `LOGBOOK.md`
(RULED OUT R1–R9 in full; ESTABLISHED; LIVE THREADS in full, T28's complete
Iteration 46–57 history), `PLAN.md`'s Iteration-58 queue (Red Team's
`experiments/080-.../phase5_redteam_audit.md` §6/§7 reconciliation),
`experiments/080-.../phase1_proposal.md`, `validity_precheck.py`,
`validity_precheck_results.json`, `NOTES.md`, `phase5_review_photonics.md`,
`phase5_review_quantum.md`, `phase5_redteam_audit.md` in full;
`experiments/079-.../phase1_proposal.md` §4 (PHOTONICS' original
construction sketch) and `y_wall_aperture_sum.py` in full;
`experiments/069-.../run.py::_free_period_search`/`_fixed_period_fit`;
`experiments/076-.../results.json`/`NOTES.md`/`phase1_proposal.md` (the real
T28 reference periods); `experiments/071-.../results.json`
(per-ABSORB free periods); `lab/validation/run_all.py`'s gate pattern.

**No RULED-OUT item (R1–R9) is re-proposed.** This is instrument-fidelity
work continuing T28 — no mechanism is asserted to be real; every falsifiable
band below is stated before running anything.

---

## 1. Mechanism narrative (≤300 words)

Nine T28 cycles (exp-069 through exp-080) have chased an unexplained
~2.84°-family periodicity in `C80−C40`/`PAIR_PAD`/`PAIR_ABSORB40` deltas of
the ambient-contrast channel. Every coherent-echo model tried so far —
single-edge (exp-078), full non-edge-reduced aperture sum (exp-079),
plane-wave/global-steering pre-check (exp-080) — was either structurally
foreclosed (part (a): the aperture sits 0.76–2.15% of its own Fraunhofer
distance from the wall, `theta_local` spread 2.6–2.75× across the aperture —
no single global angle is a sound description of the true multi-point
geometry) or, when PHOTONICS' own remaining §4 construction was actually
built (by QUANTUM's blind Phase-2 critique in exp-080, zero new FDTD), only
**half** of what PHOTONICS specified: `E_photonics=r(90°−θ_beam;ABSORB)·
W(θ_beam)` omits the direct term `E_direct(θ_beam)` and was scored by an R²
shape-comparison against exp-079's own already-discredited candidate curve —
never the free-period fit against REAL T28 data PHOTONICS' own sketch
actually named.

This cycle builds `E(θ_beam)=E_direct(θ_beam)+r(90°−θ_beam;ABSORB)·
W(θ_beam)` — the total field, both terms present — and scores its
`PAIR_PAD`/`PAIR_ABSORB40`/`C80−C40` pair-deltas via `_free_period_search`/
staged-widening against the REAL T28 reference periods, exactly as every
prior y-wall model in this sub-thread has been held to. `E_direct` is cited
verbatim from PHOTONICS' own exp-080 Phase-5 proof (bit-identical across all
5 congruent configs — a coordinate substitution `u=y_s−OBJ_Y` makes every
ingredient PAD-invariant), not re-derived; this cycle re-verifies it
numerically as a cheap sanity check, and additionally checks — a question
neither PHOTONICS nor Red Team's audit posed explicitly — whether a
config-invariant `E_direct` is a load-bearing addition to the pair-delta
scores at all, or cancels out of them identically by the same algebra that
proves it PAD-invariant. Alongside the build: EM's gate re-run at
`[47.5°,54.5°]`, THERMODYNAMICS' own energy-budget upper bound, and
MATERIALS' docstring/disclaimer hygiene.

---

## 2. Parameter table

All geometry/reflectance constants are direct lookups from already-committed
code, re-confirmed by import (R4), never hand-typed.

| Symbol | Meaning | Source | Value |
|---|---|---|---|
| `CONGRUENT_KEYS` | the 5 congruent configs | `dg065`/`ywas.CONGRUENT_KEYS` | `("C40","C60","C70","C80","G40")` |
| `D_SP` | source-to-plane x-distance | `dg065.CONFIGS[key]["d_sp"]` | `223` cells, congruent-series constant |
| `OBJ_Y`, `y_lo`, `y_hi` | aperture geometry | `dg065.CONFIGS[key]` | per-config, `PAD`-shifted; `aperture_cells=1504` fixed |
| `ABSORB` | per-config graded-loss boundary depth | `dg065.CONFIGS[key]["absorb"]` | `40/60/70/80/40` for C40/C60/C70/C80/G40 |
| `λ` | wavelength in cells at 600nm | `br.CPL[600]` | `20` cells |
| `θ_beam` grid | real dense sweep | `experiments/076-.../results.json::headline["theta"]` | 31 points, 36.0°–42.0°, 0.2° step |
| `dist_direct(y_s)` | direct source-point-to-observer distance | **new**, this file: `hypot(D_SP, OBJ_Y−y_s)` — PHOTONICS' own exp-080 Phase-5 formula (§4), cited verbatim | evaluated over the native aperture grid |
| `E_direct(θ_beam)` | direct (unmirrored, no wall) field | **new**, this file: `∫ amp(y_s)·exp(i[phase_drive(y_s,θ_beam)+K·dist_direct(y_s)]) dy_s` | reuses `ywas.aperture_amplitude`/`source_driven_phase`, `br`'s `K600` |
| `E_image(θ_beam)` | `r(90°−θ_beam;ABSORB)·W(θ_beam)` | `d80.photonics_image_term_curve` (exp-080, already committed) | reused unchanged |
| `E_total(θ_beam)` | `E_direct+E_image` | **new**, this file | the object PHOTONICS actually specified |
| `REFERENCE_PERIODS` | REAL T28 reference periods, `PAIR_PAD`/`PAIR_ABSORB40`/`C80−C40` | recomputed fresh from `experiments/076-.../results.json::headline`'s raw `C40`/`G40`/`C80` curves via `free_period_with_widening` — same idiom `y_wall_aperture_sum.py` §[3] uses, never hand-typed | citations: `2.8421°`/`4.6113°`/`4.1761°` (exp-079's own independently-reproduced figures; recomputed fresh here, not copied) |
| SUPPORT/REFUTE bands | `rel_dev = |P*_model−P*_real|/P*_real` | `ywas.score_period` (imported, unchanged) | SUPPORT ≤0.30, REFUTE >1.00, else INCONCLUSIVE — the SAME convention every T28 cycle since Iteration 46 has used |
| Gate range (item 2) | `90°−θ_beam` envelope + 0.5° margin | EM's exp-080 Phase-5 review | `[47.5°,54.5°]` |
| Energy anchor (item 3) | `|r(90°−θ_beam)|²` at ABSORB=40 | `d80.part_c_power_budget_at_true_angle()` (already committed) | cited anchor: `≤0.15%` (max `1.4943×10⁻³`) |

---

## 3. T1 escape route

**N/A.** This is instrument/model-fidelity work on an unexplained numerical
periodicity in the ambient-contrast channel, not a proposed mechanism for
the phenomenon program's constraint-3 tension — the same disposition every
T28 cycle since exp-071 has carried (`experiments/076-.../results.json::
t1_escape_route`: `"N/A (instrument/model-fidelity class...)"`). Constraint
3 is not engaged. Confirmed from precedent, not asserted fresh.

---

## 4. Idealizations

1. **`E_direct`'s definition is the one physically natural choice consistent
   with the x-wall's own `E=E_d+r_coeff·E_i` convention** (PHOTONICS' own
   caveat, exp-080 §4) — the same taper and driven-phase convention as the
   echo term, propagated over the direct, unmirrored source-to-observer
   distance, no wall, no `r()`. Not an arbitrary choice, but not the only
   logically conceivable one either.
2. **`E_direct`'s PAD-invariance is cited from PHOTONICS' own proof, not
   re-derived from first principles here** — this file only numerically
   re-verifies the already-proven bit-identical result (a cheap sanity
   check, not an independent derivation) and additionally checks whether it
   is a load-bearing addition to the pair-delta scores.
3. **`W(θ_beam)`/`r(90°−θ_beam;ABSORB)` are reused unchanged from
   `validity_precheck.py`'s already-committed `photonics_image_term_curve()`**
   — any defect in that function (e.g. the ungated `[48°,54°]` angle range,
   item 2 below) is inherited unless this cycle's own gate re-run closes it.
4. **The comparison target for the free-period fit is REAL T28 data**
   (`experiments/076-.../results.json::headline`), not a candidate model —
   this is the correction to exp-080's own methodology gap, not a new
   idealization on top of it, but the pre-registered bands (rel_dev
   thresholds) are themselves a convention, not a unique physical
   discriminator.
5. **Energy-budget item 3 uses an interception factor upper-bounded at 1**
   (i.e., the maximally generous assumption that 100% of the source's
   radiated power reaches the wall) — a real, disclosed idealization, not a
   computed geometric solid-angle fraction (which would need new,
   not-yet-gated machinery). This can only make the reported bound looser
   (larger), never tighter — a genuine upper bound, not a point estimate.
6. **Item 2's gate re-run reuses the SAME nested-function pattern
   `y_wall_aperture_sum.py`/`y_wall_prescreen.py` already use** (near-verbatim,
   same `n_trials=2000`, same thresholds) — not a new gate design, applied at
   a new angle range only.
7. **Zero new FDTD anywhere in this cycle.**

---

## House-discipline applicability (R4, R6, R9 — stated explicitly, not assumed)

- **R4** (hand-typed figures / independent verification): every number cited
  in this proposal and its results section is produced by invoking the
  actual committed code (`photonics_construction.py`, or a direct call into
  already-committed `d80`/`ywas` functions) and copied from
  `phase1_results.json`/`_output.txt` — none is hand-computed. The
  `REFERENCE_PERIODS` are recomputed fresh from `experiments/076-.../
  results.json::headline`'s raw arrays each run, not copied from exp-079's
  own JSON, closing any drift risk between the two cycles' own citations.
- **R6** (synthetic ground-truth recovery gate, mandatory for any carrier/
  phase-conditioned coefficient FIT): **does not apply here.** R6 targets a
  NEW estimator that fits a coefficient conditioned on a nuisance carrier
  phase (exp-072's differential/beat-fit class, where a sign or rotation
  bug in the fitted coefficient was invisible to every ordinary check). This
  cycle's `_free_period_search`/`free_period_with_widening` is (a) not a
  new estimator — it is the SAME machinery every T28 cycle since Iteration
  46 has used, already exercised and cross-checked dozens of times in this
  program's own record, and (b) not a carrier/phase-conditioned coefficient
  fit — it is a free-period grid search that reports a single scalar
  (`P*`, `R²`) per curve, with no nuisance carrier-phase parameter anywhere
  in its own construction (unlike `R_q`/`dR_q/dψ̄`'s own carrier-rotation
  object, R6's actual target). Reusing already-validated machinery on new
  input curves (this cycle's `E_total` pair-deltas) is the class of use R6
  was explicitly written to NOT require a fresh gate for.
- **R9** (commensurability of any cited ratio/comparison — same units,
  independently confirmed, not just the arithmetic): item 3's own
  `~116,000×` ratio (`θ_beam`-convention anchor / `theta_local`-convention
  bound) divides two quantities of the SAME kind (`reflected_power_fraction
  = |r(θ)|²`, dimensionless, both computed by the identical `|r|²`
  operation on the identical `n_prof`/`lam_cells` inputs, differing only in
  which `θ` array is passed) — commensurable by construction, not merely by
  a reproduced division. Item 1c's `rel_dev` comparisons (model period vs.
  T21 fringe; model period vs. T28 real target) are likewise the SAME
  `rel_dev(p_real,p_model)` function applied to the SAME units (degrees) in
  both cases — no cross-unit or cross-normalization risk of the kind R9 was
  adopted to catch.

---

## 5. PRE-REGISTERED, falsifiable predictions (before `photonics_construction.py` is written or run)

### Item 1 — the total-field free-period fit (the primary, decisive test)

**Per-pair bands** (identical to every T28 cycle since Iteration 46,
`ywas.score_period`): for each of `PAIR_PAD`, `PAIR_ABSORB40`, `C80−C40`,
computed on the PRIMARY (`Re{E_total}`) proxy —

- **SUPPORT** if `rel_dev = |P*_model−P*_real|/P*_real ≤ 0.30`.
- **REFUTE** if `rel_dev > 1.00`.
- **INCONCLUSIVE** otherwise.

**Combined Verdict rule, stated before running** (the standard 3-pair
combination this sub-thread's own precedent — exp-071's `NEITHER`,
exp-079/080's per-part reporting — uses, made explicit and symmetric here):

- **SUPPORT** if all 3 pairs SUPPORT.
- **REFUTE** if all 3 pairs REFUTE.
- **NEITHER** (this program's own established label for "mixed/gray-zone",
  not a new term) otherwise — including any mix of SUPPORT/INCONCLUSIVE/
  REFUTE across the 3 pairs.

**Prediction: NEITHER, leaning REFUTE.** Two independent lines of reasoning,
both disclosed honestly before running:

*For a REFUTE-leaning result:* part (a)'s FORECLOSE finding (exp-080,
reconfirmed at all 3λ) establishes the aperture never actually presents a
single global angle to the wall; `photonics_image_term_curve()`'s own raw
amplitude regime is 100–400× larger than the true `|r(theta_local(y_s))|`
range (a direct numerical consequence); and PHOTONICS' own feasibility
probe (exp-079 §4) predicted the dominant recovered period would land close
to T21's own 1.9608° fringe, not T28's ~2.84°-4.6°family, because
`r(90°−θ_beam)`'s own phase swings too slowly (75–143° of phase change
across the whole 6° sweep) to produce an independent short-period
oscillation on its own.

*For real uncertainty, not a foregone REFUTE:* this is the FIRST time this
exact free-period-against-real-data test has ever been run on this
construction — every prior negative result in this nine-cycle sub-thread was
either structurally guaranteed to fail regardless of wall reflectance
(single-edge, full-aperture-sum, both `theta_beam`-independent by
construction) or scored against the wrong target entirely. This construction
is the first whose own `r()` term genuinely depends on `θ_beam`, so a clean
SUPPORT is not ruled out by any prior finding the way it was for every
earlier y-wall model.

**If the result lands INCONCLUSIVE or SUPPORT on 2+ pairs instead of the
predicted REFUTE-leaning NEITHER:** that is real news — it would mean
PHOTONICS' own `θ_beam`-dependent `r()` term, despite the FORECLOSE finding,
recovers something close to T28's real periodicity, and Checkpoint criterion
2 bookkeeping should treat this construction as a live candidate requiring
further scrutiny (a PAD-loaded real-article check, item 8 of the Iteration-58
board, becomes far more urgent), not as another closed member of the
coherent-echo class.

### Item 1b — does `E_direct` change the pair-delta scores at all?

**Prediction, stated as a directly falsifiable numeric claim before
running:** `max|E_total pair-delta − E_image-only pair-delta| = 0.0`
(bit-identical), for all 3 pairs, because `E_direct` is proven
config-invariant (PHOTONICS' proof, cited) and a config-invariant additive
term cancels EXACTLY out of any difference between two configs' totals.
**If this is NOT exactly zero**, that is itself a finding requiring
explanation (a bug in this file's own `E_direct` implementation, or a
subtlety in PHOTONICS' proof this cycle has not correctly transcribed) —
not something to wave through.

### Item 2 — EM's gate re-run at `[47.5°,54.5°]`

**Prediction: PASS on all three gates**, reproducing EM's own Phase-5
hand-check (`worst |r|=0.0853` at the wider `[36°,60°]` sweep; `≈0.0387` at
the actually-used `[48°,54°]` range) as a formally committed gate, not
merely a hand-checked number. **If any gate fails**, `photonics_image_term_
curve()`/item 1's own construction cannot be trusted at this angle range
until resolved — this would upgrade from "hygiene" to load-bearing
immediately.

### Item 3 — THERMODYNAMICS' energy-budget upper bound

**Prediction: the reported ≤0.15% anchor (ABSORB=40, `90°−θ_beam`
convention, matched admittance, interception=1) reproduces exactly**
(`1.4943×10⁻³` from `d80.part_c_power_budget_at_true_angle()`, called
directly, never hand-typed). **A second, tighter bound — using the
physically-correct `theta_local(y_s)` angle convention EM's own item-4
finding names (not the borrowed `θ_beam`-steering convention) — is predicted
to be many orders of magnitude smaller** (the already-disclosed
`|r(theta_local)|²≈1e-13`–`1e-8` range, exp-080's own MATERIALS/THERMO
Phase-5 findings), confirming that even the loosest possible (100%
interception) upper bound on this entire construction family's contribution
to constraint-3's energy budget is negligible under the physically-correct
angle convention specifically, several more orders of magnitude below the
already-negligible `90°−θ_beam`-based anchor. **If the `theta_local`-based
bound is NOT smaller than the `90°−θ_beam`-based one**, that contradicts
EM's own item-4 finding and needs explaining before either number is cited
again.

### Item 4 — MATERIALS hygiene

Fix `reflection_coefficient_vec_realizable()`'s docstring
(`mu_r=ni^2`→`mu_r=ni`) in `experiments/080-.../validity_precheck.py` (the
function's actual location — PLAN.md's Iteration-58 text names
`reflection_coefficient_vec_realizable()` without a file path; the function
was folded into `validity_precheck.py` at exp-080 Phase 3, not into
`lab/materials.py`, which contains no matched/realizable admittance code at
all — confirmed by grep before writing this). State explicitly, in
`NOTES.md`: (a) the realizable number, not the matched one, is the only one
that could ever describe a real material; (b) a valid global-angle y-wall
construction needs an angle convention built from `theta_local(y_s)`'s own
fixed-observer geometry, not a borrowed `θ_beam`-steering convention.

---

## Compliance note

This document makes no `lab/` changes to engine physics (item 4 edits a
docstring only, in an experiment-directory file, not `lab/materials.py` —
see item 4's own note on the file-path correction) and does not modify
`LOGBOOK.md`/`PLAN.md`/`SESSION_LOG.md`/`lab/ARTIFACTS.md`/`lab/artifacts.py`/
`AGENTS.md`. Per house discipline, this file's predictions are written
BEFORE `photonics_construction.py` is written or run. Per this task's own
instruction, git commit is deferred to Phase 3 — but the ORDER of authoring
(bands frozen in this file first) is honored within this single-session
draft exactly as house discipline requires.

---

## PHASE 1 RESULTS (post-freeze)

`photonics_construction.py` written and run only after the predictions
above were frozen in this file. Every number below is copied from
`phase1_results.json`/`_output.txt`, never hand-typed (R4).

### Item 1a — `E_direct` PAD-invariance: **CONFIRMED, bit-identical**

`max|E_direct(cfg)−E_direct(C40)|` = exactly `0.0` for all five configs
(C40/C60/C70/C80/G40), at every one of the 31 real `θ_beam` values. This
numerically re-verifies PHOTONICS' own exp-080 Phase-5 proof to the
strongest possible standard (bit-exact, not merely "small") — the fourth
independent confirmation of this fact across this program's own record
(PHOTONICS' original proof, Red Team's from-scratch reproduction, and now
this cycle's own from-scratch script).

### Item 1 — the total-field free-period fit: **Combined Verdict NEITHER
### (mechanically), REFUTE-leaning on the substantive T21-proximity reading**

| pair | `P*_real` | `P*_model` | `rel_dev` | verdict |
|---|---|---|---|---|
| `PAIR_PAD` | 4.6113° | 1.8571° | 0.5973 | INCONCLUSIVE |
| `PAIR_ABSORB40` | 4.1761° | 2.0301° | 0.5139 | INCONCLUSIVE |
| `C80−C40` | 2.8421° | 2.0150° | 0.2910 | SUPPORT |

`REFERENCE_PERIODS` recomputed fresh from `experiments/076-.../results.json::
headline`'s raw `C40`/`G40`/`C80` curves (never hand-typed): `4.6113°` /
`4.1761°` / `2.8421°` — matching exp-079's own independently-reproduced
citations exactly (`2.8421`/`4.6113`/`4.1761`), confirming no drift in the
real reference data between exp-079 and this cycle. Per the pre-registered
combination rule, 1 SUPPORT + 2 INCONCLUSIVE + 0 REFUTE → **Combined Verdict:
NEITHER**, mechanically exactly as the rule requires — not a judgment call.

**This REFUTES my own pre-registered directional lean ("NEITHER, leaning
REFUTE") only partly** — no pair landed REFUTE outright (`rel_dev>1.00`)
where I expected at least a plausible REFUTE-leaning cluster; one pair
(`C80−C40`) landed SUPPORT, just inside the 0.30 bar (`rel_dev=0.2910`,
margin `0.009`, i.e. within 3% of the SUPPORT/INCONCLUSIVE boundary itself).
**But the [1c] look-elsewhere diagnostic (below), run precisely because a
lone near-boundary SUPPORT deserves scrutiny, shows this SUPPORT is not
trustworthy evidence for the mechanism.**

### Item 1b — does `E_direct` change the pair-delta scores at all? **Cancels
### to float-precision noise, NOT literally bit-identical — my "0.0" prediction
### was too strong, stated honestly, not smoothed over**

`max|E_total pair-delta − E_image-only pair-delta|` = `1.014×10⁻¹⁴` /
`1.179×10⁻¹⁴` / `1.287×10⁻¹⁴` (`PAIR_PAD`/`PAIR_ABSORB40`/`C80−C40`) —
**not exactly `0.0`**, so `all_exactly_zero=False`, contradicting the literal
pre-registered prediction. Traced to source (a follow-up check, not
pre-registered, run to explain the discrepancy rather than wave it through):
`|E_direct|` is `88.9–110.7` in magnitude — **4–5 orders of magnitude larger
than `|E_image|` (`1.3×10⁻⁴`–`3.5×10⁻³`)**, confirming PHOTONICS' own
exp-079 §4 prediction that `E_direct` would be the "dominant carrier."
Subtracting two `O(100)`-magnitude `E_direct` values that are analytically
equal (per item 1a's own bit-exact proof) leaves a floating-point residual
of order `100 × 2.2×10⁻¹⁶ ≈ 2×10⁻¹⁴` — exactly the observed scale. **Honest
self-score: the literal "bit-identical difference" prediction is REFUTED;
the substantive claim it was meant to test — that `E_direct` does not
change which pair-delta periods or verdicts this test reports — is
CONFIRMED to 11+ orders of magnitude below the signal scale**, i.e. as
close to "changes nothing" as floating-point arithmetic can ever
demonstrate. The scores above are computed on the genuine total field
(`E_direct` included, not skipped) — this check is a redundant,
confirmatory diagnostic on top of that, not a shortcut that bypassed
building `E_direct` at all.

### Item 1c — T21-proximity diagnostic (this sub-thread's own established
### look-elsewhere discipline, `y_wall_aperture_sum.py` §[6a]): **the lone
### SUPPORT is a T21-proximity artifact, not evidence for the mechanism**

| pair | `P*_model` | `rel_dev` vs T21 (1.9608°) | `rel_dev` vs T28 real target | closer to T21? |
|---|---|---|---|---|
| `PAIR_PAD` | 1.8571° | 0.0529 | 0.5973 | **yes** |
| `PAIR_ABSORB40` | 2.0301° | 0.0353 | 0.5139 | **yes** |
| `C80−C40` | 2.0150° | 0.0277 | 0.2910 | **yes** |

**All three model periods sit within 2.8–5.3% of T21's own established
1.9608° fringe, but 29–60% away from their own scored T28 real targets** —
every one of the three is more than 10× closer to T21 than to T28. This
reproduces, quantitatively, exactly what PHOTONICS' own exp-079 §4
feasibility probe predicted before this construction was ever built:
*"expect the dominant recovered period to still land close to T21's 1.96°,
with the interesting result being how far off T21 it lands."* Read against
this diagnostic, `C80−C40`'s lone SUPPORT (`rel_dev=0.2910`, a 2.6-degree
model period sitting 2.8% from T21 and only barely — 0.9 percentage points —
inside the 30% SUPPORT bar against its own T28 target) is the same
"compromise fit between two nearby, imperfectly-separated frequencies"
pattern this program's own Iteration-47 record (exp-070, P-070-1) already
named and cautioned against, not independent confirmation of a real T28
echo. **Self-scored reading: Combined Verdict NEITHER stands as computed
mechanically, but the informative, substantive reading is REFUTE-leaning**
— this construction, built and scored exactly as PHOTONICS specified for
the first time in this nine-cycle sub-thread, recovers T21's carrier
(exactly as its own author predicted it would), not T28's real
periodicity, on any of the three pairs.

### Item 2 — EM's gate re-run at `[47.5°,54.5°]`: **PASS, all three gates,
### exactly as predicted**

- G-LOSSLESS: worst `||r|−1|` = `2.220×10⁻¹⁶` (PASS, bar `<1e-9`)
- G-N1: worst `|r_loop−r_direct|` = `3.140×10⁻¹⁵` (PASS, bar `<1e-12`)
- G-PASSIVITY: worst `|r|` = `0.041413` (PASS, bar `≤1.0`)

Reproduces EM's own Phase-5 hand-check order of magnitude (`≈0.0387` at the
narrower `[48°,54°]` range; this cycle's `[47.5°,54.5°]` re-run, with the
same `0.5°` margin convention, finds worst `|r|=0.0414`, consistent — the
small difference is the wider range, not a discrepancy) as a formally
committed, code-executed gate rather than a hand-checked Phase-5 number.
`reflection_coefficient_vec` is now gated at this angle range; item 1's own
construction can be trusted at `[47.5°,54.5°]` going forward.

### Item 3 — THERMODYNAMICS' energy budget: **reproduced the `≤0.15%` anchor
### exactly; the physically-correct bound is ~116,000× smaller**

- `θ_beam`-convention anchor (`90°−θ_beam`, ABSORB=40, matched admittance,
  interception=1): **`1.4943×10⁻³`** (`0.14943%`) — reproduces PLAN.md's
  own `≤0.15%` anchor exactly, called directly from
  `d80.part_c_power_budget_at_true_angle()`, never hand-typed.
- `theta_local(y_s)`-convention (the physically-correct, fixed-observer
  angle, EM's own item-4 finding), ABSORB=40, matched admittance,
  interception=1: **`1.289×10⁻⁸`**.
- Same, realizable (`μ_r=1`) admittance: **`2.638×10⁻⁸`**.
- Ratio (θ_beam anchor / theta_local matched): **`1.160×10⁵`** — the
  `90°−θ_beam` convention over-states the true physical upper bound on this
  construction family's energy budget by roughly **116,000×**.

**Prediction confirmed: the `theta_local`-based bound is smaller (item 3's
own pre-registered directional claim), and by a very large margin.** Even
under the loosest possible assumption anywhere in this analysis —
interception factor = 1, i.e. 100% of the source's total radiated power
somehow reaches the wall, which is itself already generous by construction
— the physically-correct angle convention puts an upper bound of
`~1.3×10⁻⁸` (matched) / `~2.6×10⁻⁸` (realizable) on the fraction of total
scene power the echo path at ABSORB=40 could ever carry. **This construction
family could not matter to constraint 3's energy budget in absolute terms,
under either angle convention, but the honest physical bound is many orders
of magnitude more negligible than the already-tiny anchor PLAN.md cited.**

### Item 4 — MATERIALS hygiene: **applied**

`reflection_coefficient_vec_realizable()`'s docstring, in
`experiments/080-.../validity_precheck.py`, corrected
(`mu_r=ni^2`→`mu_r=ni`) — see that file's own diff. **File-path correction,
disclosed at proposal time (§5 item 4), confirmed here**: the function does
not live in `lab/materials.py` (which contains no matched/realizable
admittance code — confirmed by grep before this cycle began); it was folded
into `validity_precheck.py` at exp-080 Phase 3. The two explicit
disclaimers MATERIALS'/EM's own item-4 text requires are stated in
`NOTES.md`, below, not merely implied.
