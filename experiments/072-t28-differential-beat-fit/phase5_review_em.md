# ELECTROMAGNETISM — Phase 5 Review · Panel Iteration 49 · exp-072

*Fresh sub-agent, EM charter (field/wave behavior, impedance matching, energy coupling; owns reciprocity/passivity/causality bookkeeping). Blind to the other seats' Phase-5 reviews. Everything below was re-derived or re-executed independently against `run.py` and the committed JSON; no claim here is taken from prose.*

---

## Headline

**Red Team's two overrides of my Phase-2 remedies were both correct, and I reproduce Red Team's own demonstrations to 3–4 significant figures.** I withdraw both of my Phase-2 remedies without reservation.

**But the code that was actually committed and run in Phase 4 is not the estimator Red Team audited.** `run.py` carries two independent sign defects in the step-2 basis construction. Together they make the recovered `R_q` — and therefore every `ΔP`, every coefficient channel, every strain flag, and every surrogate *p*-value in `phase4_results.md` — a rotation of the intended coefficient by an angle set by the **common-mode carrier phase `ψ̄`**, a pure nuisance parameter. On synthetic data with known ground truth, the committed estimator returns recovered/true `ΔP` ratios wandering over the entire range **[−1.00, +1.00]** as `ψ̄` sweeps, tracking `cos(2ψ̄)`. With the two signs corrected it returns **+1.00 ± 0.03 uniformly**.

The Combined Verdict `NEITHER` survives the correction. Almost nothing else in `phase4_results.md` does.

I state up front what makes this a Phase-5 catch rather than an opinion: the corrected pipeline reproduces **every** independently verified Phase-2 number in Red Team's Sec-0 ledger and Attacks 3/10 — eight surrogate *p*-values, four `ΔP`s, `A_i`, `ρ_c`, and both of Red Team's real-data phase-artifact figures — and the committed pipeline reproduces **none** of them. The Director's Phase-3 note describes exactly the cross-check that would have caught this (comparing the tool's outputs against Red Team's and VISION's independently computed values); it was used to *find* the first bug and was not re-applied after the fix.

---

## 1. Re-derivation of Red Team's overrides of my two Phase-2 remedies

### 1a. `A_q`: my remedy was wrong. Override upheld, and I can now state the relation more exactly than the docket does.

The exact algebra, re-derived from `cos P − cos Q = −2 sin((P+Q)/2)·sin((P−Q)/2)` without reference to the audit:

```
delta_AB = δa·cosΘ − 2a_cfg·sin(χ₀ + πΔf·u)·sinΘ + O(δa·χ)
Θ = 2πf̄·u + ψ̄        χ₀ = πΔf·x̄ + Δψ/2
```

In the pre-registered basis `[1, cosΘ, −sinΘ, u·cosΘ, −u·sinΘ]`:

- `A_q = 2·a_cfg·sin χ₀` — **Red Team's relation, exact.** My `A_q = a·Δψ + R_q·x̄` is precisely its small-χ linearization; algebraically `A_q − R_q·x̄ = a·Δψ`, so my proposed channel `|A_q − R_q·x̄|/a` **is** `|Δψ|`, the θ = 0° extrapolation, 26 σ_u outside a 36°–42° window. Confirmed by construction, not by assertion.
- Evaluated on the **corrected** pipeline's real coefficients, my channel returns **185.9° at C40–C60 and 174.9° at C40–C80** — digit-for-digit Red Team's Attack-3 figures (+3.244 rad, +3.053 rad). The directly measured within-window phase difference at those pairs is **−2.26°** and **−4.97°**. My remedy would have had P-072-6 announce a 175°-class phase inversion between two configs whose common-mode average retains 99.9% of the mean per-config amplitude. Red Team's forward-simulation and real-data demonstrations both replicate. **Override upheld; my remedy was worse than the defect it named.**

**One correction to the docket that neither Red Team nor the Director caught, and that I owe as the seat that owns this bookkeeping.** Item 5's table uses the symbol `a` with two different meanings in two adjacent rows. The quantity `run.py` actually divides by (`carrier["amplitude"]`) is the *fitted common-mode* amplitude, and the common mode of two detuned tones is `a_cbar = a_cfg·cos χ₀`. Therefore, in the units the code actually uses:

- `R_q = 2π·a_cbar·Δf` — **exact** (the `cos χ` factor the Phase-1 proposal's own §1 carries is absorbed by `a_cbar`; the docket's "`R_q = 2πa·Δf` unchanged" is right, but only under this reading).
- `A_q = 2·a_cbar·tan χ₀` — **not** `sin`. So `χ₀ = arctan(A_q/2a_cbar)`, not `arcsin`.

Verified on synthetic data at `ΔP = 0.05°`: `A_q/(2a_cbar) = −2.339`, `arctan → χ₀ = −1.167 rad` against the constructed truth `πΔf·x̄ = −1.172 rad` (0.4%); `arcsin` is undefined there. On the observed data `|A_q|/2a_cbar ≤ 0.065`, so `tan ≈ sin` to better than 0.5% and **this correction is outcome-inert this cycle** — but the docket's own regime of interest (`χ ≈ 1.2 rad` at the predicted effect size, Red Team's own figure) is exactly where it becomes a factor of 2.6. It should be fixed in the table before any successor cycle quotes a phase channel.

### 1b. The wrong-carrier comparator: my flip was right to gate, Red Team was right that 1.9608° cannot be diagnostic — **and the replacement 3.60° comparator fails Red Team's own stated criterion by a factor of two.**

I verify the arithmetic all three of us agreed on: `X = 0.0813454`, Rayleigh width `1/X = 12.2933`, `f̄ = 29.65`, `f(1.9608°) = 37.600`, separation `7.95` → **0.647 Rayleigh widths**. My comparator is sub-Rayleigh and non-diagnostic. Conceded.

Applying the *same* convention to the substituted comparator:

| comparator | f | \|f − f̄\| | Rayleigh widths |
|---|---|---|---|
| 1.9608° (my proposal, rejected) | 37.600 | 7.95 | **0.647** |
| **3.60° (docket item 10, adopted, gating)** | 20.479 | 9.17 | **0.746** |
| 1.85° (docket's other stated endpoint) | 39.852 | 10.20 | 0.830 |

Per pair the displaced comparator lands at **0.702–0.746** Rayleigh widths. Docket item 10 asserts it is "**≥1.5 Rayleigh widths** from the carrier." It is not; it is 0.75, and every one of the ratios above is almost exactly **half** the docket's claimed figure — Red Team appears to have used the half-width `1/(2X) = 6.147` for the displacement while using the full width `1/X = 12.293` for the 0.6452 figure it rejected me on, inside the same attack. To reach a genuine ≥1.5 Rayleigh widths at `f̄ = 29.65` requires **T ≤ 1.533° or T ≥ 6.576°**; even 1.0 width requires **T ≤ 1.758° or T ≥ 4.248°**.

So Red Team's Attack-9 argument — "gating on a sub-Rayleigh comparator converts an under-resolution identity into a verdict; the comparator is guaranteed to be comparable, so pairs fail for a reason unrelated to contamination" — **applies to 3.60° with 87% of its original force, and the Phase-4 run shows exactly the predicted symptom**: at three of four pairs `|R_q(3.60°)|` is *larger* than `|R_q(T_mean)|`, i.e. the "wrong" carrier absorbs more ramp signal than the right one. The gate then fails those pairs.

The adjudication is therefore: my *diagnosis* (the comparator must gate) stands, Red Team's *diagnosis* of my comparator stands, and **Red Team's replacement does not fix the problem it was introduced to fix.** A ≥1.5-width comparator inside the existing search range does exist — `T_wrong = 1.50°` — and costs nothing.

---

## 2. The principal defect: two sign errors in the committed step-2 basis

### 2a. What is wrong

**Defect A — the carrier phase hand-off has the wrong sign.** `_amp_phase_at` returns `psi = atan2(b, a)` from `_fixed_period_fit`, which fits `y = c₀ + a·cos(wu) + b·sin(wu) ≡ c₀ + A·cos(wu − atan2(b,a))`. `design_matrix` then builds `theta_c = w·u + psi`. The correct hand-off is `psi ← −atan2(b, a)`. Direct residual check against the fitted `Cbar` (synthetic, amplitude 1.85e−3):

```
theta_c = w·u + psi   residual rms = 2.49e−3   (larger than the carrier itself)
theta_c = w·u − psi   residual rms = 1.60e−4
```

The Phase-3 note correctly identifies that "a phase fitted in x needs a `w·x̄` shift before it means anything in u" and fixes that. It does not address the sign, and fitting in `u`-space removes the shift but not the sign.

**Defect B — the basis sign convention deviates from the pre-registered specification.** `phase1_proposal.md` line 99 and `phase2_redteam_audit.md` item 1 both specify `[1, cos θ_c, −sin θ_c, u·cos θ_c, −u·sin θ_c]`. `run.py::design_matrix` builds `[1, cos, +sin, u·cos, +u·sin]` (and item 15's curvature column as `+u²·sin` where the docket says `u²·(−sin θ_c)`). The 4-column H₀ span is unaffected, so the restricted-null *construction* is fine; the reported `A_q`, `R_q` and everything derived from them carry the opposite sign to the documented coefficient table, and `delta_f_obs = R_q/(2πa)` inherits it.

### 2b. Why the two do not simply cancel

Defect B alone is a clean sign flip. Defect A alone rotates the `(cos, sin)` and `(u·cos, u·sin)` column pairs by `2ψ̄` relative to the true field quadrature — the span is preserved (which is why `cond5` and the fit residual are untouched and nothing looked wrong), but the *coefficients* become

```
R_q^committed ≈ cos(2ψ̄)·R_q^true − sin(2ψ̄)·R_i^true
```

i.e. the ramp-quadrature coefficient is mixed with the ramp-in-phase coefficient by a nuisance angle. Since `|R_i| ≳ |R_q|` at three of four pairs (Red Team's own Attack 8), the mixing is first order, not a perturbation.

### 2c. Ground-truth demonstration

Synthetic congruent pairs built on the real 31-point θ grid with known `ΔP` and a swept common phase `ψ₀` (recovered/true ratio; should be ≈ +1 independent of `ψ₀`):

| `ψ₀` | 0.0 | 0.8 | 1.6 | 2.4 | 3.1 | 4.0 | 5.0 |
|---|---|---|---|---|---|---|---|
| **as committed** | −0.45 | +0.93 | +0.33 | −0.91 | −0.52 | +0.97 | −0.10 |
| both signs fixed | +0.98 | +0.99 | +1.02 | +1.01 | +0.98 | +0.99 | +1.03 |

The committed estimator's answer is set by a parameter that carries no information about `ΔP`. This is the exact failure mode the whole differential framing exists to avoid, and it is the one my Phase-2 §3 flagged in principle ("a phase-reference error `ε` rotates the ramp plane, mixing `R_i` into `R_q` as `R_i·sin ε`") — I asked for `ε`'s *uncertainty* to be propagated and did not check whether `ε` itself was zero. It was not; it was `2ψ̄ ≈ 3.4–3.6 rad`.

### 2d. Cross-validation against every independently verified Phase-2 number

The two-line patch (`psi = -math.atan2(...)`; `−sin`/`−u·sin` columns) applied to `run.py`, re-run at the committed seed:

| quantity | Red Team / VISION, Phase-2, independently verified | **as committed** | **signs fixed** |
|---|---|---|---|
| ΔP(T_mean), 4 pairs | +0.0697 / +0.0085 / −0.0086 / +0.0668 | +0.0576 / −0.0020 / −0.0144 / +0.0380 | **+0.0697 / +0.0085 / −0.0086 / +0.0668** |
| `p` unrestricted, 4 pairs | 0.1738 / 0.7495 / 0.4706 / 0.3746 | 0.3509 / 0.9417 / 0.1617 / 0.7023 | **0.1737 / 0.7430 / 0.4768 / 0.3716** |
| `p` restricted, 4 pairs | 0.0057 / 0.1034 / 0.0041 / 0.0158 | 0.0122 / 0.4634 / 0.0066 / 0.0501 | **0.0067 / 0.1042 / 0.0045 / 0.0171** |
| `A_i` at C40–C60 (audit: "fitted 8.24e−4") | +8.24e−4 | −7.33e−4 | **+8.240e−4** |
| `ρ_c` closure at a common carrier (VISION: 0.041) | 0.041 | 0.085 | **0.0408** |
| EM's overridden channel (Attack 3) | 185.9° / 174.9° | — | **185.9° / 174.9°** |
| ΔP sign agreement with `n_grid=3000` absolute-period diffs | 4/4 | 3/4 | **4/4** |

Six independent quantities, three independent Phase-2 implementations, one conclusion. **Red Team's Phase-2 implementation was correct; the committed `run.py` is not it.**

### 2e. What changes and what survives

**Survives.** Combined Verdict `NEITHER`. Zero pairs `RESOLVED` (no pair reaches Holm-adjusted `p ≤ 0.01` either way — corrected values 0.0135 / 0.1042 / 0.0135 / 0.0171). G0-a/b/c/d all pass identically (`cond5` is rotation-invariant). `power_demonstrated = False`. P-072-3 `NOT_EVALUABLE`, P-072-4 `NEITHER`. The `n_holm10` counts are unchanged (3 restricted, 0 unrestricted), so the REFUTE branch is blocked for the same reason. The saturating-vs-linear disclosure is untouched (it never uses step 2). **The cycle's verdict and its headline "non-identifiability, not noise floor" framing both stand.**

**Does not survive.** Every entry of the P-072-1 coefficient/`SE` table; every entry of the P-072-6 phase/freq/strain table (the strain flag flips at C70–C80, from False to True — so `R_i` exceeds the frequency channel at **three** of four pairs, not two); every entry of the four-carrier `ΔP` table; every `p_fringe` (C40–C60 goes 0.0017 → 0.666, C40–C80 goes 0.00015 → 0.420 — the "T21's fringe dominates" disclosure numbers invert); every curvature coefficient; and specifically:

- **"C70–C80 is the only pair that would have passed the wrong-carrier check"** — under the corrected estimator `p_wrong(C70–C80) = 0.0426` and the gate **fails**. **Zero of four** pairs pass the displaced-carrier gate. The Bottom Line's sentence "the one pair whose displaced-carrier control passes (C70–C80) is exactly the pair whose significance and injection-recovery power both fail" has no referent and must be withdrawn.
- **"No pair's `|R_q|/SE_bootstrap` clears 2"** — corrected, C40–C60 reaches **2.16**.
- **"sign is not invariant across carriers"** — weakened. Corrected, `T_mean` and `T_delta` agree in sign at C60–C70, `T_delta ≈ 0` at C40–C60, and only C70–C80 and C40–C80 genuinely flip; the 3.60° column now agrees in sign with `T_mean` at three of four pairs where as-printed it disagreed at four of four. VISION's finding is real but its as-printed evidence is not the evidence for it.

---

## 3. Further defects, ranked by consequence

**D1 (above) — the two sign errors.** Verdict-inert, everything-else-fatal.

**D2 — the injection-recovery power test measures the wrong thing, and its published per-pair result is a cancellation artifact.** Docket item 4's literal wording ("inject into the H₀-fitted series **plus the observed residual**") sums to `yhat0 + resid0 ≡ delta_AB`, so `run.py` injects on top of the *observed* `R_q`. Exactly: `Rq_recovered = R_q_obs + Rq_pred` (verified to all printed digits at all three pairs). The published failure — "C70–C80's injection test misses the `p ≤ 0.01` bar by a small margin" — is the observed `R_q` partially cancelling the injected ramp. Running the same test with `R_q` projected out first, so the injected amplitude is exactly `Rq_pred`:

| pair | docket-literal | H₀-clean |
|---|---|---|
| C40–C60 | p = 0.0023 **PASS** | p = 0.0127 **FAIL** |
| C60–C70 | p = 0.0091 **PASS** | p = 0.0184 **FAIL** |
| C70–C80 | p = 0.0196 **FAIL** | p = 0.0096 **PASS** |

The pass/fail set **completely inverts**. `power_demonstrated = False` either way, so the branch logic is inert — but the per-pair power statements in `phase4_results.md` are uninterpretable, and a design's power statement must not depend on the sign of the effect it is trying to establish power for. This is a defect in the docket item itself (Red Team's own, not a seat's), faithfully implemented.

**D3 — the item-7 bootstrap does not propagate step-1 uncertainty; it propagates case-resampling noise, and the published interpretation is wrong.** This was my own Phase-2 request, so I checked it hardest. `run.py` draws an **iid case resample** of the 31 (θ, C_A, C_B) triples, refits the carrier at `n_grid=400`, and takes the sd of `R_q`. Decomposing on the corrected pipeline (n_boot = 300):

| pair | OLS SE | bootstrap, carrier **refit** | bootstrap, carrier **held fixed** | step-1 share of variance |
|---|---|---|---|---|
| C40–C60 | 0.00562 | 0.01274 (2.27×) | 0.01472 (2.62×) | **−0.34** |
| C60–C70 | 0.00116 | 0.00546 (4.70×) | 0.00632 (5.44×) | **−0.34** |
| C70–C80 | 0.00083 | 0.00266 (3.19×) | 0.00393 (4.71×) | **−1.19** |
| C40–C80 | 0.00562 | 0.01575 (2.80×) | 0.02142 (3.81×) | **−0.85** |

Holding the carrier fixed gives a **larger** spread at every pair. The step-1 contribution is not merely small, it is negative: refitting the carrier per resample lets it track the resampled data and *absorbs* part of the perturbation. Docket item 7 asked for the propagation of `(T_mean, ψ̄)` uncertainty into `SE(R_q)`; what is implemented and reported is the variance of an iid case resample of a 31-point deterministic angular sweep — a quantity that re-weights leverage and duplicates/drops θ nodes, and that has no clean interpretation for a design-based regression. `phase4_results.md`'s "the uncertainty item 7 required be propagated genuinely dominates the naive figure" is not supported by the code that produced the number. (I also checked the obvious alternative culprit — the bootstrap's coarser `n_grid=400` — and it is **not** the driver: 0.01302 at n_grid=400 vs 0.01305 at n_grid=3000 for C40–C60. My prior suspicion there was wrong; recording it as ruled out.)

**D4 — item 7 and item 12 are partially unimplemented, and no one flagged it.** Item 7 requires `SE(ΔP)` and per-pair `dR_q/dψ̄` and `R_i/R_q`. Item 12 requires "ΔP **and its propagated SE** at all four carriers." `run.py` computes none of: `SE(ΔP)` at any carrier, `dR_q/dψ̄`, or an explicit `R_i/R_q` column. `results.json`'s `deltaP_by_carrier` carries four bare point estimates. The mandatory disclosure that VISION's finding was converted into is therefore printed without the uncertainty that Red Team's §2 adjudication said was "the correct general form of the fix" — the sign-flip table is presented as measured fact with no indication that at three of four pairs the flipping quantity is well inside its own uncertainty. `phase3_synthesis.md` states "All 15 docket items are implemented in `run.py`, verbatim to the audit's specification." Two are not.

**D5 — the `ΔP` values at the two wrong carriers are mis-scaled by 5–8×.** `dP_wrong` and `dP_fringe` divide by `amp`, the amplitude fitted at `T_mean`, while `dP_Tdelta` correctly uses `amp_delta`. The common-mode amplitude at the comparator carriers is much smaller:

| pair | amp(T_mean) | amp(3.60°) | factor | amp(1.9608°) | factor |
|---|---|---|---|---|---|
| C40–C60 | 0.005276 | 0.001121 | 0.212 | 0.004149 | 0.786 |
| C60–C70 | 0.005725 | 0.000927 | 0.162 | 0.004243 | 0.741 |
| C70–C80 | 0.005703 | 0.000736 | 0.129 | 0.004350 | 0.763 |
| C40–C80 | 0.005245 | 0.000934 | 0.178 | 0.004250 | 0.810 |

So the eye-catching `−0.1080°` and `−0.1615°` entries in the 3.60° column are inflated by roughly 5–8×, and the 1.9608° column by ~25%. Signs are unaffected (the factor is positive), so the sign-flip narrative is not created by this bug — but the magnitudes that make the table look alarming are. **Present in both the committed and my sign-corrected run; I did not patch it.**

**D6 — `phase4_results.md` attributes the wrong-carrier gate failures to the wrong sub-condition.** The gate is `|R_q(T_wrong)| ≤ ½|R_q(T_mean)|` **and** `p(T_wrong) > 0.01`. Recomputed from the committed `results.json`:

| pair | magnitude clause | p clause (`p > 0.01`) | write-up blames |
|---|---|---|---|
| C40–C60 | **FAIL** (0.02036 vs 0.01139) | PASS (p = 0.0195) | "p = 0.0195 — fails" ✗ |
| C60–C70 | **FAIL** (0.00907 vs 0.00042) | FAIL (p = 0.0071) | "p = 0.0071 — fails" ✓ partial |
| C40–C80 | **FAIL** (0.03029 vs 0.00744) | PASS (p = 0.0125) | "p = 0.0125 — fails" ✗ |

At two of four pairs the write-up names a *p*-value as the failing condition when that *p*-value **satisfies** its clause. This is not cosmetic: the magnitude clause failing means `|R_q|` at the wrong carrier exceeds `|R_q|` at the right one, which is the diagnostic signature of §1b's sub-Rayleigh comparator problem — the single most informative fact in the table, and it is not reported anywhere.

**D7 — `A_i` is nowhere in `phase4_results.md`.** It is a coefficient in the mandated item-5 table and the *one* quantity in that table for which Red Team published an independently verified value (8.24e−4 fitted, 7.73e−4 directly measured, "6%"). Omitting it removed the only cross-check that would have exposed D1 by inspection: the committed run's `A_i` at C40–C60 is **−7.33e−4**.

**D8 — `n_resolved_holm10_*` counts the derived pair.** Both counters add C40–C80, which item 14 establishes is the exact arithmetic sum of the other three and "not an independent fifth test." Restricting to the three free pairs gives 2 (restricted) / 0 (unrestricted) instead of 3 / 0 — **outcome-inert**, REFUTE stays blocked. Recording for the ledger only.

**D9 — carrier-gate calibration resolution mismatch.** The observed `T_delta` is found at `n_grid=3000`; the surrogate `q95` ensemble that calibrates it is found at `n_grid=300` over the same [1°, 4°] range. The coarser surrogate search adds ~0.005° of quantization jitter to the reference statistic and therefore *loosens* the gate slightly. All four pairs pass with 2–3× margin either way, so **outcome-inert**; the economy is disclosed in the code comment, but the asymmetry with the observed statistic is not.

---

## 4. Passivity / reciprocity / causality bookkeeping — my charter's specific check

**Confirmed clean in the strict sense, with one caveat and one missed opportunity.**

This cycle produces no absorbed-power figure, no S-parameter, no energy balance, no dispersion relation, and no time-domain causality statement. `C_empty` is handled throughout as a dimensionless field ratio (Idealization 5), the energy sidecar is explicitly N/A by argument rather than omission (Idealization 8, verified — nothing in `run.py` computes a power), and T1 is genuinely not engaged. `ABSORB` is correctly and repeatedly held to be a numerical boundary-condition parameter rather than a material (Idealization 3). Nothing here smuggles a realizability, reciprocity, or passivity claim.

**The one caveat.** `saturating_vs_linear` fixes the saturating model's decay constant at `SAT_DECAY_L = 0.075`/cell, described in the code as "engine-derived (`_damping`'s cubic ramp)" and in `phase4_results.md` as "an engine-derived saturating model." That constant is a per-cell **optical depth** — an amplitude-attenuation rate. It is here applied as the decay rate of a **period**, i.e. of a phase observable. Relating an attenuation rate to a phase shift is a Kramers–Kronig-class claim and nothing in this cycle establishes it for `_damping`'s profile. The quantity is disclosed and non-gating, so it does not reach a verdict — but "engine-derived" overstates it. It is *engine-motivated by analogy*, on 4 points against 2 parameters, and the `R² = 0.9901` vs `0.8328` comparison is between two 2-parameter models on 4 points with no dof-aware statistic anywhere. I would ask that "engine-derived" be softened to "engine-motivated, decay constant imported from an amplitude-attenuation context to a phase observable without a stated causal relation" wherever it appears.

**The missed opportunity, which is squarely my seat's to have raised in Phase 2 and I did not.** Passivity supplies a free, independently-signed falsifier on the amplitude channel that this design computes and then discards. A monotonically deeper absorber cannot increase the boundary return; if the axis were acting purely absorptively, `A_i = a_B − a_A` would be negative at every pair. Corrected values: **+8.24e−4, +5.70e−6, −8.78e−5, +7.41e−4** — positive at three of four pairs, i.e. the deeper-`ABSORB` config returns a *larger* common-mode fringe. That is not a paradox: it is direct, zero-FDTD-cost evidence that the `ABSORB`/`PAD` compound axis is **not** acting as a pure absorber, which is exactly the confound Iteration-49 queue item 2 exists to break. Nobody used it, and the committed run's `A_i` signs are the reverse, so anyone who had used it would have drawn the opposite conclusion.

---

## 5. Disclosure and process defects

- **`phase3_synthesis.md`'s implementation-defect disclosure is exemplary in form and incomplete in fact.** It correctly localizes the bug to the step-1→step-2 phase hand-off using precisely the right instrument (step-1 outputs match Red Team/VISION exactly; step-2 outputs do not) — and then, after patching, does not re-apply that instrument. Had it been re-applied, the surviving `ΔP` mismatch (+0.0576 vs Red Team's verified +0.0697) would have been visible immediately. The house precedent my charter cites — Director self-catches are "expected to be checked, not assumed correct" — is what caught this, and the general lesson is narrower and more useful than "check harder": **a cross-check that finds a bug must be re-run as an acceptance test after the fix, not retired once it has served.**
- **The audit's own numbers and the official run's numbers are irreconcilable and the write-up does not say so.** A reader comparing `phase2_redteam_audit.md` Attack 1's *p*-table to `phase4_results.md`'s P-072-1 table finds C60–C70's restricted *p* differing by 4.5× with no explanation offered. `phase4_results.md` presents the contamination disclosure as though Red Team's Phase-2 numbers and the official numbers are the same estimator's.
- **A mitigating fact about the contamination ruling that nobody could have stated but that Phase 5 can.** Red Team's outcome-determining Phase-2 computation was performed on the *correct* estimator; the committed pipeline was a different one. The directional claim ("unrestricted null → REFUTED, restricted → NEITHER") survives on both — I verify it on the corrected pipeline: unrestricted Holm-adjusted *p* are 0.521 / 0.743 / 0.954, zero pairs at `p ≤ 0.10`, REFUTE's null-count condition met. So the §4 ruling was correct and remains correct. It should be recorded that it was verified against the corrected estimator in Phase 5.
- **Caveat propagation is otherwise good.** Idealizations 1–8 are carried into `phase4_results.md`'s Caveats block, the `ABSORB`-or-`PAD`-or-frequency-or-fringe-weight rule is stated as binding under every verdict including NEITHER (THERMO's fix, correctly applied), window provenance and the `ptp/mean`-is-not-a-contrast disclosure are both present, and `CONFIRM_UNCERTIFIED` is a genuine unconditional override in code, not prose. I found no dropped caveat. The failures this cycle are arithmetic and implementation, not disclosure discipline.

---

## 6. Ranked candidate directions

### 1. Re-execute exp-072 with the two sign corrections, under a new estimator-identity gate `G0-e`. Zero FDTD, zero `lab/` diff.

Nothing downstream of step 2 in this cycle can be entered into LOGBOOK as measured. The re-run is two lines of patch plus a re-scored write-up, and the contamination ruling already requires a fresh pre-registered cycle before any CONFIRM-shaped result enters the record — this folds into that.

The generalizable part is the gate, and it belongs to my seat because it is the estimator's own reciprocity bookkeeping: **the ramp basis must be the true field quadrature, and that is checkable for free.** `G0-e`: before any pair is scored, build synthetic congruent pairs on the real θ grid with a known injected `ΔP` and a common-mode phase `ψ₀` swept over `[0, 2π)`, and **HALT unless recovered/true ∈ [0.95, 1.05] at every `ψ₀`**. That single gate detects D1, would have detected the original `w·x̄` bug, and detects any future basis/phase-convention drift — none of which move `cond5`, `R²`, or the residual, which is why four seats plus Red Team plus the Director all missed it. Add to the same re-run: `A_q = 2·a_cbar·tan χ` (§1a), the `1.50°` comparator (§1b), the H₀-clean injection (D2), a residual or parametric step-1 bootstrap that actually perturbs `(T, ψ̄)` rather than resampling cases (D3), `SE(ΔP)` at all four carriers and `dR_q/dψ̄` (D4), the correct per-carrier amplitude (D5), sub-condition-level gate reporting (D6), and `A_i` in the published table with its passivity sign expectation stated (§4). Also worth adopting as the basis-stability check the design lacked: the **phase-channel closure** `Σ 2χ(adjacent)` vs `2χ(C40–C80)`, which is `−5.297°` vs `−4.972°`, a **6.5% residual** — a genuine, non-tautological consistency test that is computable even when no pair is `RESOLVED`, unlike the `ρ_c` route that came back `NOT_EVALUABLE`.

### 2. Settle T28's differential route in this window with a Cramér–Rao / conditioning feasibility calculation *before* any further fitting — then, only if it passes, PHOTONICS' two-tone joint fit (queue item 4). Zero FDTD.

The wrong-carrier control is the wrong instrument and three cycles have now been spent on it. You cannot separate two sub-Rayleigh contributors by *choosing* a comparator carrier; you can only separate them by constraining both jointly, using the fact that T21's fringe frequency is independently established, so only its amplitude and phase are free. I priced it: the 9-column two-tone ramped design `[1, carrier×4, fringe×4]` at the observed carrier and 1.9608° gives `cond = 529` (vs 60) and a **36.6× variance inflation on `R_q`, i.e. a 6.0× SE inflation**, before any noise is added. Against corrected `|R_q|/SE_OLS` ratios of 4.9 / 3.0 / 4.3 / 4.7, that is decisive: the joint fit cannot reach 2σ on `R_q` at this SNR in this window. **My recommendation is that the panel publish that number and close the differential route on the 36°–42° grid**, rather than run item 4 and add a fourth NEITHER. This converts a repeatedly re-litigated qualitative claim ("non-identifiable") into a pre-computed quantitative bound, which is what Iteration 49's substantive finding was reaching for and did not quite state.

### 3. Extend the θ window upward — the only change that buys real resolution — with the requirement stated as a number, and with the `sin θ` linearity idealization re-validated as a condition of the spend.

Every identification failure in this cycle traces to one quantity: `X = ptp(sin θ) = 0.0813`, giving `1/X = 12.29` against a carrier–fringe separation of `7.95`. The requirement is arithmetic:

| target separation | required `X` | required `θ_max` (from 36.0°) |
|---|---|---|
| 0.65 widths (today) | 0.0813 | 42.0° |
| **1.00 widths (formally resolvable)** | 0.1258 | **45.5°** |
| 1.50 widths | 0.1887 | 50.9° |

`θ_max ≈ 46°` is the first point at which T21's fringe and the T28 carrier are separable *at all*, and it is reachable: at the existing 0.2° step it is 20 new points per config, so **40 FDTD calls for a C40/C80 two-config extension** — cheaper than queue item 2's 62–93. It also directly satisfies VISION's window-discipline constraint, which forbids reusing 36°–42° a third time for an absolute-period discriminator; a *new* window is the compliant move, not another desk pass on the old one.

**Binding condition from my seat.** The whole model is "a sinusoid in `x = sin θ`," and `x` is not linear in `θ`. The local scale `cos θ` varies **8.1%** across 36°–42°, **14.1%** across 36°–46°, and **22.2%** across 36°–51°. My Phase-2 §3 estimate of the resulting common-mode quadratic phase — 0.207 rad ≈ 12° over the present window, which a pure sinusoid-in-`x` cannot absorb and which is a live candidate for the `R² ≈ 0.43–0.45` ceiling and for the non-zero `R_i` at three of four pairs — grows with the window. So the extension must be scored with the curvature column (item 15) **promoted from disclosed to fitted**, or with the fit moved to a form linear in the actual propagation phase. Extending the window without that turns a resolution gain into a model-strain loss, and `R_i` is already the largest coefficient in the table.

*(I set aside queue item 3 — MATERIALS' mask-functional-form ablation — not because it is weak, but because it is orthogonal to my seat's findings and is well argued where it stands. Queue item 5 is a constraint, not an item, and direction 3 above is written to satisfy it.)*

---

## 7. Reproduction

Everything above is reproducible from the committed repo with no `lab/` diff and no new FDTD. The two-line patch to `run.py`:

```python
# _amp_phase_at:  Cbar = c0 + A·cos(w·u − atan2(b,a)), so design_matrix's
#                 theta_c = w·u + psi requires the negated phase
psi = -math.atan2(fit["b"], fit["a"])

# design_matrix:  pre-registered basis is [1, cos, −sin, u·cos, −u·sin]
#                 (phase1_proposal.md line 99; redteam item 1); item 15's
#                 curvature column is u²·(−sin)
cols = [np.ones_like(x), np.cos(theta_c), -np.sin(theta_c),
        u * np.cos(theta_c), -u * np.sin(theta_c)]
```

Re-running yields Combined Verdict `NEITHER`, zero pairs `RESOLVED`, and the right-hand column of §2d. The ground-truth sweep in §2c, the bootstrap decomposition in D3, the injection comparison in D2, the amplitude table in D5 and the conditioning figure in direction 2 are each a few lines against `run.py`'s own functions and the committed JSON.

**Verdict on this cycle's execution:** the design Red Team produced was sound and the audit's arithmetic was sound; the failure is entirely between Phase 3 and Phase 4, in code that no gate in the design was capable of interrogating. The `NEITHER` stands. The tables under it do not, and should be re-published, not annotated.
