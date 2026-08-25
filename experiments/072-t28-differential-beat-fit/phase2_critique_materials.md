# MATERIALS & METAMATERIALS — Phase 2 critique · Panel Iteration 49 · exp-072

*Fresh sub-agent, MATERIALS charter (sub-wavelength structure; what could physically realize the proposed optical behavior; owns the realizability bound). Blind to all other seats' Phase-2 output this cycle.*

---

## Steel-man (≤150 words)

This is the most honest realizability-adjacent handling in the T28 series. Idealization 3 states plainly that `ABSORB` is `lab/fdtd2d.py::Sim._damping`'s numerical domain-truncation device, not a medium, and forecloses any physical-medium claim outright — verified against the source, and it reproduces exp-071's committed `ABSORB_NOT_MATERIAL_CAVEAT` without softening. Idealization 2 carries `PAD = ABSORB − 40` through to the *verdict language* ("`ABSORB`-or-`PAD`-tied, never `ABSORB`-tied"), which is exactly where a confound of this kind has to bite, and refuses to let the sharper estimator lend spurious specificity.

The instrument argument is also sound in my lane: all four configs share the aperture (`A=752`) and `R_OUT=78`, so the T21 fringe and aperture response genuinely are common-mode and genuinely do cancel in `delta_AB`; what survives is the boundary-construction difference — the quantity actually at issue. Zero FDTD, pre-registered surrogates, an a-priori underpowered call, and a rule forbidding a quoted period for an unresolved pair.

## Sharpest attack (≤150 words)

The one physical model imported is linear in `ABSORB`, and the engine's own boundary law contradicts it. `_damping` builds a **cubic ramp normalized by `absorb`**, so depth sets taper *steepness*: single-pass optical depth `0.30·Σramp ≈ 0.30·ABSORB/4`, residual reflection falling exponentially — ~8× per 10-cell step, four decades across C40→C80. The four measured periods agree: fitting `P = P∞ + a·e^(−L(ABSORB))` with `L` **fixed** by `_damping`'s own optical depth (2 free parameters, identical dof to linear) gives **R² = 0.9957 versus linear's 0.8664**. The trend saturates.

Yet §2c's power table and P-072-4's whole band structure are multiples of one linear slope `m₀` — itself mis-transcribed: exp-071's committed `trend.linear_fit.slope` is **0.0025564 °/cell**, not `0.00244361` (R4). Under a saturating truth C70–C80's rate is ~0, so P-072-4 can fire REFUTE — "new structure" — on the *expected* behaviour of a graded absorber.

---

## Realizability bound (charter obligation)

**NOT_APPLICABLE — no realizability call is licensed or attempted this cycle.** Neither axis of the compound `ABSORB`/`PAD` variable is a material parameter: one is a damping-ramp depth, one is vacuum padding. Nothing here sits on the published / plausible / unobtainium-with-parameters scale, and I record that as the seat that owns it so no downstream reader mistakes silence for an unstated bound. Note the asymmetry: a CONFIRM would tighten T28 *toward* instrument and *away* from medium, retiring the realizability question rather than opening it; a REFUTE of the instrument leaves T28's material status exactly where iteration 46 left it. Both readings must be written that way.

## Required changes (support-with-changes)

1. **Correct `m₀` to the committed `0.0025564 °/cell`** (`experiments/071-.../results.json` → `trend.linear_fit.slope`, echoed in that cycle's `phase4_results.md`), recomputed by invoking the committed value at prediction-freeze, not hand-typed — R4, and load-bearing here because every P-072-4 band and every §2c power figure is a multiple of it.
2. **Two reference models in P-072-4, not one.** Score resolved rates against both the linear `m₀` ramp and the engine-derived saturating model (decay constant fixed by `_damping`, not fitted). Keep the sign-reversal clause gating; demote the `[m₀/10, 10m₀]` rate-window REFUTE to disclosed. As written, a correct measurement of a saturating absorber response is scored as "new structure."
3. **Add a curvature diagnostic to step 2 (disclosed, non-gating).** `R_q` cannot distinguish a genuine `Δf` from *any* smooth angle-dependent phase difference between the two boundary constructions — and a graded-loss band's residual reflection phase is angle-dependent by construction, over precisely θ∈[36°,42°]. A sixth column `u²·(−sin θ_c)` costs nothing (31 points, 25 dof): a pure `Δf` predicts a zero quadratic coefficient; a boundary-phase gradient generically does not. P-072-5 tests the wrong *carrier*, not this.
4. **Minor, in-lane:** §1 attributes C70 ≡ C80 solely to `n_grid=400` node collision. Genuine saturation is an equally live reading of the same collision, and the two are not distinguished by refining the grid. State both. Related free observation for the standing `PAD` confound: the two legs of the compound axis have different natural functional forms — absorber residual reflection saturates exponentially in depth, geometric path length does not on this scale — so the *curvature* of `P(ABSORB)` is partial, zero-cost information on a confound this program currently treats as wholly unaddressable. Four grid-quantized points cannot settle it; it should still be disclosed rather than omitted.

## Verdict

**SUPPORT-WITH-CHANGES.** The estimator, the pre-registered surrogate null, the closure falsifier (which telescopes correctly under *any* `P(ABSORB)`, saturating included — that test is robust), and the "not a material" / PAD-confound framing are all sound and should run. Changes 1 and 2 must land before prediction-freeze; 3 and 4 are cheap and belong in the disclosed set.

## Single parameter change that would flip my verdict to SUPPORT

In **P-072-4**, replace the REFUTE rate-window `r ∉ [m₀/10, 10m₀]` with a **sign-only** REFUTE clause (retaining `ΔP < 0` with `|ΔP| ≥ 0.010°`), and re-anchor `m₀` to the committed **0.0025564 °/cell**. That single edit removes the one gate where the engine's own graded-absorber law would be scored as an anomaly.
