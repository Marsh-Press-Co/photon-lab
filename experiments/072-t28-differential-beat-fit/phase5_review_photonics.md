# PHOTONICS — Phase 5 Review · Panel Iteration 49 · exp-072 (T28 differential/beat fit)

*Fresh sub-agent, PHOTONICS charter (surface interaction, absorption spectra, angular dependence, scattering cross-sections). Blind to the other seats' Phase-5 reviews. Everything below was re-executed from `run.py` and the committed JSON in an independent session; no number in this document is taken from prose.*

---

## 0. Headline

**The officially committed `run.py` carries a carrier-phase sign defect in the step-1 → step-2 handoff, and a second, independent deviation from the frozen pre-registered basis. Together they corrupt every signal coefficient this cycle publishes.** The two errors partially cancel — which is exactly why they survived a 15-item Red Team docket, a Director's synthesis that re-derived three overrides by hand, and a Phase-4 write-up.

The good news, stated first because it is load-bearing: **the Combined Verdict `NEITHER` survives the fix.** Zero pairs reach Holm-adjusted `p ≤ 0.01` and three clear `p ≤ 0.10` under the restricted null both before and after correction. The cycle's *conclusion* stands. Its *numbers* do not — P-072-1's `R_q`/`SE`/`p` columns, P-072-6's three channels, the four-carrier ΔP table, and the injection-recovery table are all wrong, and two published sign claims invert.

The decisive proof is not my own re-derivation. It is that **the corrected pipeline reproduces Red Team's own independently-computed Phase-2 numbers to the digit, and the committed one does not** — including the specific tripwire the docket itself pre-registered (item 11's "verified to fire at three of four pairs"), which the official run failed and `phase4_results.md` published without noticing.

---

## 1. D1 — [CRITICAL] The carrier phase handed from step 1 to step 2 has the wrong sign

### The defect

`_amp_phase_at` (`run.py:122–137`) fits `series = c0 + a·cos(wu) + b·sin(wu)` via `_fixed_period_fit` and returns

```python
psi = math.atan2(fit["b"], fit["a"])          # run.py:136
```

For a carrier `A·cos(wu + φ)` the least-squares coefficients are `a = A·cos φ`, `b = −A·sin φ`, so **`atan2(b, a)` returns `−φ`, not `+φ`.** `design_matrix` then builds

```python
theta_c = w * u + psi                          # run.py:163
```

i.e. `θ_c = wu − φ`, where the pre-registered specification (`phase1_proposal.md:97`, restated in `phase3_synthesis.md`) is `θ_c = 2πu/T_mean + ψ̄` with `ψ̄` the carrier's own phase. **The basis is rotated by −2φ from the data's actual carrier.**

### Three independent proofs

**(a) Closed form.** A rotation by `2ψ` in the (cos, sin) plane maps the true coefficients onto the fitted ones:

```
A_i_pub = A_i_true·cos2ψ − A_q_true·sin2ψ        R_i_pub = R_i_true·cos2ψ − R_q_true·sin2ψ
A_q_pub = A_i_true·sin2ψ + A_q_true·cos2ψ        R_q_pub = R_i_true·sin2ψ + R_q_true·cos2ψ
```

So the published `R_q` is a **mixture of the true `R_i` and the true `R_q`**. At the four pairs `ψ = 1.712/1.782/1.814/1.744 rad`, giving `cos2ψ = −0.960/−0.912/−0.884/−0.941` and `sin2ψ = −0.279/−0.410/−0.467/−0.339`. Since `|R_i| ≳ |R_q|` at every pair (docket item 11's own finding), the 28–47% `R_i` leakage is a **first-order** contamination of the cycle's central estimand.

**(b) Forward simulation.** Noiseless two-sinusoid pairs, equal amplitude, known ΔP, pushed through `run.py`'s own `carrier_fit` → `design_matrix` → `ΔP` chain:

| carrier phase `φ_true` | `psi` returned | `ΔP_est / ΔP_true` | `cos(2φ)` |
|---|---|---|---|
| 0.000 | −0.0000 | −0.9999 | +1.0000 |
| 0.300 | −0.3000 | −0.8252 | +0.8253 |
| 0.900 | −0.8999 | **+0.2273** | **−0.2272** |
| 1.500 | −1.5000 | +0.9903 | −0.9900 |
| 1.712 | −1.7120 | +0.9607 | −0.9604 |
| 2.500 | −2.5001 | −0.2837 | +0.2837 |

The recovery ratio is **exactly `cos(2φ)`** — a pure basis-rotation artefact, and `psi` is demonstrably `−φ`. With `θ_c = wu − psi` the same synthetic data returns `ΔP_est/ΔP_true = −1.0001` and `−1.0003` (the −1 is D2, below). The estimator is not weakly biased; at `φ = 0.9` it recovers 23% of a known period difference.

**(c) Real data, against a directly measurable quantity.** `A_i` is defined as `a_B − a_A` (Red Team Attack 3, unchallenged). The per-config carrier amplitudes are directly measurable at the pair carrier:

| Pair | `A_i` published | `A_i` with phase fixed | directly measured `a_B − a_A` |
|---|---|---|---|
| C40–C60 | **−7.333e−4** | **+8.240e−4** | +7.733e−4 |
| C60–C70 | +9.027e−5 | +5.70e−6 | +1.485e−5 |
| C70–C80 | +1.106e−4 | −8.778e−5 | −6.903e−5 |
| C40–C80 | **−5.429e−4** | **+7.413e−4** | +7.213e−4 |

The published `A_i` has the **wrong sign at three of four pairs**, including both wide pairs, where it would assert that C80's fringe amplitude is *below* C40's — against a measured `ptp` that rises 0.01649 → 0.02008 (+21.8%, THERMODYNAMICS' own exp-071 finding). With the phase corrected, `A_i` lands on the measured value, and `+8.240e−4` is **precisely the number Red Team's independent Phase-2 implementation reported** ("fitted 8.24e−4 vs directly measured 7.73e−4, 6%", Attack 3). Red Team's implementation had the phase right. The committed one does not.

### The tripwire that should have caught it — and did fire, unread

Docket item 11 pre-registers a verified expectation: `|R_i/R_q|` = **0.48 / 2.81 / 1.69 / 1.10**, strain flag "verified to fire at three of four pairs."

| Pair | `\|R_i/R_q\|` published | `\|R_i/R_q\|` phase-fixed | docket item 11 |
|---|---|---|---|
| C40–C60 | 0.892 | **0.478** | 0.48 |
| C60–C70 | 12.342 | **2.811** | 2.81 |
| C70–C80 | 0.613 | **1.687** | 1.69 |
| C40–C80 | 2.417 | **1.099** | 1.10 |
| flags fired | **2 of 4** | **3 of 4** | 3 of 4 |

Exact agreement, four for four, once the phase is fixed. `phase4_results.md` reports the two-of-four result ("`R_i` … exceeds the frequency channel at C60–C70 and C40–C80") with no note that this contradicts the docket item it is implementing. That is the single caveat-propagation failure that let a cycle-invalidating bug through Phase 4.

The same holds for the primary significance test. Restricted-null `p` (N=20 000, seed 20490072), and Red Team's Attack-1/item-12 table:

| Pair | `p` published | `p` phase-fixed | Red Team Phase 2 |
|---|---|---|---|
| C40–C60 | 0.0122 | **0.0064** | 0.0057 |
| C60–C70 | 0.4634 | **0.1058** | 0.1034 |
| C70–C80 | 0.0066 | **0.0042** | 0.0041 |
| C40–C80 | 0.0501 | **0.0168** | 0.0158 |
| Holm(3) | 0.0244/0.4634/0.0199 | **0.0129/0.1058/0.0126** | 0.0123/0.1034/0.0123 |

Within Red Team's own stated seed drift (≤0.003) once fixed; nowhere near it as published. **`n(p≤0.01) = 0` and `n(p≤0.10) = 3` under both — so P-072-2 = `NEITHER` and Combined Verdict `NEITHER` are unchanged.**

### Fix

`run.py:136` → `psi = -math.atan2(fit["b"], fit["a"])`, or equivalently `run.py:163` → `theta_c = w * u - psi`. Note that `phase3_synthesis.md`'s disclosed implementation fix (the `x → u` shift) addressed a *different* half of the same handoff and left this one standing. The lesson generalizes: the handoff was fixed by argument, not by a calibration test.

---

## 2. D2 — [CRITICAL] The design matrix deviates from the frozen pre-registered basis in two of five columns

`phase1_proposal.md:99` freezes the basis as

```
[1, cos θ_c, −sin θ_c, u·cos θ_c, −u·sin θ_c]  →  [c0, A_i, A_q, R_i, R_q]
```

and the coefficient map `R_q = 2πa·Δf` (proposal §2b table, docket item 5) is derived *for that basis*. `run.py:164–165` builds

```python
cols = [ones, cos(theta_c), +sin(theta_c), u*cos(theta_c), +u*sin(theta_c)]
```

then applies the `−sin`-basis relation `delta_f_obs = R_q / (2π·amp)` (`run.py:242`). In the `+sin` basis the correct relation is `R_q = −2πa·Δf`. Forward simulation confirms it: with the phase corrected, `ΔP_est/ΔP_true = −1.000` exactly.

**D1 and D2 cancel wherever `cos 2ψ < 0`, which holds at all four real pairs** (`ψ ≈ 1.71–1.81 rad`, near π/2, so `cos2ψ ∈ [−0.96, −0.88]`). That is the whole reason the published ΔP signs look reasonable and agree with the absolute-period route at 3/4 pairs. It is an accident of where this window's carrier phase happens to sit. Nothing about the design guaranteed it, and at a carrier phase near 0 or π/2 the same code would have published sign-inverted or 4× attenuated ΔP with no external symptom.

Correcting both, `ΔP(T_mean)` = **+0.0697 / +0.0085 / −0.0086 / +0.0668** — Red Team's Attack-10 values exactly, and **4/4 sign agreement** with the independently-computed `n_grid=3000` absolute-period differences (+0.0830/+0.0150/−0.0050/+0.0930), restoring the one piece of evidence Red Team used to override VISION's "the sign is arbitrary" inference. As published, that agreement is 3/4, C60–C70 having flipped — and no phase re-ran the check.

The full four-carrier ΔP table changes in 8 of 16 cells by sign:

| Pair | `T_mean` pub/fix | `T_delta` pub/fix | 3.60° pub/fix | 1.9608° pub/fix |
|---|---|---|---|---|
| C40–C60 | +0.0576 / +0.0697 | −0.0007 / −0.0001 | −0.1080 / **+0.6266** | +0.0539 / +0.0092 |
| C60–C70 | −0.0020 / **+0.0085** | +0.0120 / +0.0127 | −0.0443 / **+0.3261** | +0.0107 / **−0.0177** |
| C70–C80 | −0.0144 / −0.0086 | +0.0046 / +0.0153 | −0.0005 / **+0.0692** | +0.0022 / **−0.0080** |
| C40–C80 | +0.0380 / +0.0668 | −0.0153 / −0.0054 | −0.1615 / **+1.1131** | +0.0671 / **−0.0175** |

VISION's sign-non-invariance finding survives qualitatively. Every number reported for it does not.

---

## 3. D3 — [MAJOR] `T_wrong = 3.60°` is 0.75 Rayleigh widths from the carrier, not "≥1.5". The decisive gate is a sub-Rayleigh comparator — the exact defect Attack 9 said it was closing

Docket item 10 disqualifies T21's 1.9608° fringe as a control because it "sits 0.6452 Rayleigh widths" away and "gating on a sub-Rayleigh comparator converts an under-resolution identity into a verdict," then fixes `T_wrong` at 3.60° "(≥1.5 Rayleigh widths from the carrier)". Recomputed in the docket's own verified convention (`X = 0.0813454`, `1/X = 12.2933`, Rayleigh widths = `|f₂ − f̄|·X`):

| Pair | carrier | 3.60° | 1.9608° |
|---|---|---|---|
| C40–C60 | 2.4865° | **0.7460** | 0.6466 |
| C60–C70 | 2.5285° | **0.7060** | 0.6867 |
| C70–C80 | 2.5325° | **0.7022** | 0.6905 |
| C40–C80 | 2.4905° | **0.7422** | 0.6505 |

**3.60° is 2–15% further from the carrier than the comparator the docket ruled "provably non-diagnostic."** QUANTUM's "≳3.6° or ≲1.85°" arithmetic (adopted verbatim by Red Team, Director and code) is simply wrong: from a 2.4865° carrier, 1.5 Rayleigh widths requires `P ≤ 1.533°` **or** `P ≥ 6.576°`, and the free-period search range is `[1.0, 4.0]°` — so the only admissible genuinely-displaced comparators lie at `P ≤ 1.53°`.

Attack 9's own prediction — a sub-Rayleigh comparator "is guaranteed to be comparable" — is confirmed on the data it was supposed to protect against: `|R_q(3.60°)| / |R_q(T_mean)|` = **0.89 / 10.67 / 0.02 / 2.04**. At C40–C80 a carrier the design calls wrong recovers *twice* the ramp coefficient of the carrier it calls right.

And the comparator choice is outcome-changing. Re-running the gate at `P = 1.50°` (≈1.55 Rayleigh widths, inside the search range):

| Pair | gate @3.60° | gate @1.50° |
|---|---|---|
| C40–C60 | fail (`\|R_q\|` 0.0204 vs bar 0.0114) | **pass** (0.0011, p=0.892) |
| C60–C70 | fail | fail |
| C70–C80 | **pass** | **fail** (0.0044, p=0.0002) |
| C40–C80 | fail | fail |

Three of four pairs change under a comparator choice the window cannot adjudicate. The design's most decisive-looking conjunct is set by an arbitrary parameter, one level up from the problem the cycle is reporting.

**Bonus defect (D3b):** `phase4_results.md`'s P-072-2 table misattributes the failure. At C40–C60 and C40–C80 the p-condition **passes** (0.0195 and 0.0125, both > 0.01) and the **magnitude** condition fails; the table prints "`p=0.0195` — fails" and "`p=0.0125` — fails". The magnitude failure is the far more interesting fact and it is invisible in the deliverable.

---

## 4. D4 — [MAJOR] The injection-recovery power test injects on top of the observed `R_q`. `power_demonstrated = False` is not a power statement

`injection_recovery` (`run.py:410–413`) builds

```python
yhat0 = X4 @ coef0;  resid0 = delta_ab - yhat0
synthetic = yhat0 + resid0 + Rq_pred * X5[:, 4]
```

but `yhat0 + resid0 ≡ delta_ab` identically. The 4-column H₀ fit's *residual* still contains the observed ramp, so the "synthetic" series is the raw data plus the injected ramp. Verified to machine precision:

| Pair | `R_q` obs | `R_q` pred | sum | `R_q` recovered | rel. sign |
|---|---|---|---|---|---|
| C40–C60 | −0.022778 | −0.020211 | −0.042989365 | −0.042989365 | same → **2.13× amplification** |
| C60–C70 | +0.000850 | −0.010603 | −0.009753549 | −0.009753549 | opposite |
| C70–C80 | +0.005929 | −0.010530 | −0.004600893 | −0.004600893 | opposite → **0.44× cancellation** |

So C70–C80's "miss by a small margin (0.0146 vs 0.01)" is not a power shortfall. It is **destructive interference between the injected ramp and the pair's own observed, reversed ramp** — a direct consequence of the C70/C80 period-order reversal. And C40–C60's "pass" is inflated by constructive interference at 2.13× the amplitude the test claims to be injecting. The test measures nothing about the instrument's power at the pre-registered effect size; it measures `|R_q_obs + R_q_pred|`.

The docket's own wording ("inject … into the H₀-fitted series plus the observed residual") is the origin — `run.py` implemented it literally and correctly. The defect is in the docket, and Phases 3–5 are where it should have been caught. A correct construction injects into an H₀-*consistent* series (5-column residual, or a surrogate), not into the data.

`phase4_results.md`'s reading — "the power precondition did its job of preventing exactly the 'REFUTE fires on pure power failure' defect" — is therefore not supported. It happened to reach the safe branch for the wrong reason.

---

## 5. D5 — [MAJOR, my charter] "The carrier itself resolves cleanly, R² ≈ 0.43–0.45" inverts the proposal's own Idealization 4, and the window's second tone is not where the headline puts it

This is the claim I own. `phase4_results.md`'s Bottom Line reads:

> the carrier itself resolves cleanly, R²≈0.43–0.45, at every pair, matching Iteration 48's own per-config fits

`phase1_proposal.md` §6, Idealization **4**, cites the identical numbers to the opposite end:

> The window demonstrably contains ≥2 contributors (T21's 1.9608° fringe coexists with the ~2.5° family; per-config fits reach only `R²≈0.43–0.45`). P-072-5 measures the contamination but does not remove it.

The same statistic is a stated limitation in the frozen pre-registration and a stated strength in the results. That is a caveat inversion, not a rewording. I measured the residual structure to settle it:

| Pair | carrier `P*` / R² | residual best `P*` / R² | R² @ 1.9608° on residual | Cbar variance unexplained |
|---|---|---|---|---|
| C40–C60 | 2.4865° / 0.4394 | **1.8243° / 0.3312** | 0.2686 | 56.1% → 37.5% (two tones) |
| C60–C70 | 2.5285° / 0.4451 | **1.8343° / 0.3511** | 0.2960 | 55.5% → 36.0% |
| C70–C80 | 2.5325° / 0.4380 | **1.8373° / 0.3805** | 0.3238 | 56.2% → 34.8% |
| C40–C80 | 2.4905° / 0.4308 | **1.8273° / 0.3638** | 0.2986 | 56.9% → 36.2% |

Three findings, all new to this cycle:

1. **The single-carrier model is quantitatively violated.** The carrier accounts for 43–45% of the common-mode variance; a coherent second tone accounts for another ≈19 points; **≈35% remains unmodelled even with two tones.** "Resolves cleanly" is not supportable at any of those numbers.
2. **The measured second tone sits at 1.824–1.837°, not 1.9608°.** The headline "T21's 1.9608° fringe, sitting only 0.65 Rayleigh widths from the carrier" quotes a *nominal* period. The window's actual second peak sits at **0.865 Rayleigh widths** — still unresolved, so the conclusion holds, but 34% further out than stated, and *further from the carrier than the 3.60° comparator the design gates on* (0.746). The `R_q(1.9608°)` disclosure run is therefore evaluated at a position the window itself does not put the contaminant.
3. **Common-mode averaging suppresses nothing.** Per-config R² (0.4327/0.4483/0.4422/0.4337) and pair-carrier R² (0.4394/0.4451/0.4380/0.4308) are the same to ~1%. "Matching Iteration 48's per-config fits" is arithmetically accurate and evidentially damning: averaging two configs did not improve the fit, which means the 56% residual is itself common-mode and is not attenuated anywhere in the pipeline. Its cancellation in `delta_AB` is only as good as the between-config fringe-amplitude match — QUANTUM's 2.2%.

**The physical picture this supports.** A second angular tone at 0.87 Rayleigh widths from the carrier is exactly what appears, in a single-carrier basis, as a spurious low-order polynomial-in-`u` modulation of that carrier. The disclosed curvature column is the receipt: its rms contribution `‖coef·u²sinθ_c‖` exceeds the ramp term's `‖R_q·u sinθ_c‖` at **three of four pairs** (5.7e−4 vs 3.9e−4 at C40–C60; 1.0e−4 vs 1.5e−5 at C60–C70; 6.7e−4 vs 2.5e−4 at C40–C80), and adding it shifts `R_q` by −5.5% / −42.2% / +1.0% / −12.7%. `phase4_results.md` records the coefficients and declines to interpret them; the free, one-line check of *whether they move the headline coefficient* was in hand and not run. (These figures are computed in the buggy basis and need re-derivation after D1/D2, but the magnitude ordering will not reverse — the effect is a basis-completeness problem, not a phase one.)

---

## 6. Remaining defects

**D6 — [MODERATE] `NOTES.md` says its idealizations are "unchanged from the Phase-1 proposal … still binding". They are not.** The proposal's §6 lists nine; `NOTES.md` lists eight, dropping proposal items **4** (single-carrier model — see D5), **5** (~2.4 periods in window; "edge effects on the ramp coefficient are real"), **6** (`n_grid=3000` "adds no resolving power"), and **9** (a-priori power caveat), while adding three new ones. Dropping item 4 is what made D5's inversion possible; dropping item 5 removes the standing caveat on the exact column (`u·sinθ_c`) that carries the whole inference. `phase4_results.md:158`'s citation "*and Idealization 6 discloses*" the C70/C80 reversal is **dangling** — neither the proposal's nor `NOTES.md`'s Idealization 6 mentions it, and docket item 13 explicitly mandated a sentence there.

**D7 — [MODERATE] `phase4_results.md`'s caveat block drops the angular and polarization scope entirely.** Proposal Idealization 7 / `NOTES.md` Idealization 7 — *2D TMz, single polarization; positive-θ branch only (36°–42°), not a symmetry test; bench scale (`R_OUT=78`), no witness-scale claim* — appears in no deliverable caveat. Every result in this cycle is a single-polarization, single-angular-branch, bench-scale measurement, and the document a reader will actually cite says only "600nm only." From my seat that is the most consequential missing caveat after D5: an angular-periodicity result whose deliverable does not state which polarization or which angular branch it was measured on.

**D8 — [MODERATE] Arithmetic errors in `phase4_results.md`.**
- "Bootstrap SE is **3.7–4.8×** the naive OLS SE at every pair" — actual **3.83 / 6.86 / 5.75 / 4.81**. Two of four pairs lie outside the stated range; the Bottom Line's "4–5×" is worse.
- "No pair's `|R_q|/SE_bootstrap` clears 2 (**0.94 / 0.09 / 0.99 / 0.42**)" — actual **1.06 / 0.11 / 1.24 / 0.55**. All four wrong, understated by 11–24%. The qualitative claim survives; none of the four published figures reproduces from `results.json`.
- "C60–C70 and C70–C80 flip sign between `T_mean` and **every other carrier tested**" — false for both. C60–C70 is −0.0020 at `T_mean` and −0.0443 at 3.60° (same sign); C70–C80 is −0.0144 and −0.0005 (same sign). Each flips against 2 of 3, not 3 of 3 — an error in the direction that flatters the headline.

**D9 — [MODERATE] The recalibrated carrier-consistency gate (item 6) is near-vacuous.** The surrogate-derived `q95` admits `T_delta` over **74% / 47% / 68% / 59%** of the entire `[1.0, 4.0]°` free-period search range. Red Team's own noiseless forward simulation predicted this statistic at ≤0.001; the observed values are 0.12–0.25, i.e. 120–250× the model prediction, and pass comfortably. Item 6 replaced a wrongly-scaled gate with an unfalsifiable one. `phase4_results.md` prints "✓" four times with no indication that the gate could hardly have done otherwise. (The linearization gate is likewise non-binding: it admits `|ΔP|` up to ≈0.26°, ~100× the pre-registered effect size.)

**D10 — [MODERATE] Mandatory disclosures computed and dropped, or never computed.**
- `R_q` and `p` at the 1.9608° fringe carrier are computed (`run.py:320`) and **published nowhere** — only the ΔP column survives. The dropped numbers are the strongest in the cycle: `p_fringe` = **0.00170 / 0.04150 / 0.55477 / 0.00015**, against true-carrier `p_restricted` of 0.0122 / 0.4634 / 0.0066 / 0.0501. At C40–C80 the "resolution identity" carrier is **334× more significant** than the design's own carrier, with 2.85× the `R_q`. The report *undersells its own headline* by omitting this.
- Docket item 7's `dR_q/dψ̄` is **never computed** anywhere in `run.py` — grep returns nothing. It is the one quantity that would have directly measured the carrier-choice sensitivity the Bottom Line rests on (and, incidentally, would have exposed D1). `R_i/R_q` is likewise never reported as a field. `phase3_synthesis.md`'s "All 15 docket items are implemented in `run.py`, verbatim to the audit's specification" is therefore an overclaim.
- Docket item 13's mandated re-deferral of Iteration-49 queue item **4** (PHOTONICS' two-tone joint fit, "with a stated reason") appears in **no** deliverable — "two-tone" does not occur in `NOTES.md`, `phase4_results.md`, or `run.py`.
- Docket item 13's mandated sentence that "P-072-6 supplies the confounded arm of queue item 2 and does not substitute for it" appears in no deliverable.
- P-072-6's **amplitude channel `|A_i|/a`** — the original discriminator (`phase1_proposal.md:279`) and precisely THERMO's confounded arm of queue item 2 — is **absent from the published table**, which carries only phase/freq/strain. Given D1 it would have been sign-inverted at three of four pairs had it been printed; dropping it accidentally suppressed the symptom.

**D11 — [MINOR] The saturating-vs-linear disclosure overstates the mechanism content of its "engine-derived" decay constant.** Both R² values reproduce exactly (0.9901 / 0.8328). But:
- R² is nearly flat in `L`: **0.9713 (L=0.05) / 0.9901 (0.075) / 0.9942 (0.10) / 0.9898 (0.15) / 0.9832 (0.25) / 0.9817 (0.50)**. The "engine-derived, FIXED not fitted" constant is not even the optimum, and any concave two-parameter family beats linear (`a + b/A`: 0.945; `a + b·ln A`: 0.899). The comparison discriminates **curvature**, not mechanism.
- The fitted model is `P = 2.5417 − 2.0807·exp(−0.075·A)`, which extrapolates to **P(ABSORB=0) = 0.461°** — at the Nyquist period of the 0.2° θ grid, and five times below any observed period. Not a mechanism-grade model.
- `results.json`'s `saturating.amplitude = −2.0807` is sign-flipped relative to the fitted model (`run.py:451` stores `−coefs[1]` against a `−exp()` column). Cosmetic, unquoted, but it will mislead the next reader.

**D12 — [MINOR] The C70/C80 order reversal is doing load-bearing work at 0.5% of the window's own resolution floor.** The split is **0.0050°** = exactly 5 grid steps at `n_grid=3000`, against a Rayleigh floor of 41.4% (≈1.03°). It is the datum that drives (a) the saturating model's curvature, (b) the injection test's cancellation (D4), and (c) `m₀`'s demotion. It carries no more evidential weight than the `n_grid=400` node collision it replaced — both are readings of the same sub-resolution noise. `NOTES.md` Idealization 6's "adds no resolving power" was the right caveat and it was dropped (D6).

**D13 — [MINOR] Stale cross-references.** `PLAN.md`'s Iteration-49 queue item 4 still cites "R²=0.998 vs 0.866" for saturating/linear; this cycle supersedes both with 0.9901/0.8328 at `n_grid=3000`. `run.py:114` loads `per_config_free_periods` from exp-071 into `data` and never uses it — a silent opportunity to have compared the native and refined values in-run.

---

## 7. What checks out

Recorded per house discipline, so the fix does not read as a repudiation of the cycle:

- **G0-a/b/c/d all reproduce exactly** — grid identity, telescoping residual `0.0`, column provenance `0.0`, `cond5 = 59.9–61.0`.
- **`m₀` is loaded from committed JSON at runtime** (`run.py:113`), `0.0025563909774436134`, never hand-typed. MATERIALS' Attack-5 fix is implemented correctly.
- **The common-mode carrier behaves exactly as the beat model predicts.** Per pair, `T_mean` = 2.4865 / 2.5285 / 2.5325 / 2.4905 against the mean of the two configs' own `n_grid=3000` free periods = 2.479 / 2.528 / 2.533 / 2.484. Step 1 is sound; the defect is entirely in the handoff to step 2.
- **The contamination disclosure paragraph is present verbatim** in `run.py`'s docstring, `phase3_synthesis.md`, `NOTES.md` and `phase4_results.md`, and the `CONFIRM_UNCERTIFIED` override is unconditional in the Combined-Verdict branch. Condition 4 is discharged.
- **The Combined Verdict `NEITHER` is robust to every defect above**, including D1 and D2.
- **The cycle's substantive claim — that `R_q` is bounded by non-identifiability rather than by the noise floor — is not only intact, it is understated.** D3, D5 and D10 each strengthen it.

---

## 8. Ranked candidate directions

### 1. `exp-073` — re-run this cycle's design corrected, behind a mandatory forward-calibration gate. Zero FDTD.

Not "fix a bug and re-publish." The specific structural addition, pre-registered, is a **calibration harness that runs before any real datum is touched**: push noiseless synthetic pairs through the exact committed estimator at ≥6 carrier phases spanning `[0, π)` and ≥4 known ΔP spanning the pre-registered effect range, and HALT unless `|ΔP_est/ΔP_true − 1| ≤ 0.02` at every cell. That single gate detects D1 (`cos 2φ` signature), D2 (uniform −1), and any future basis or convention drift, in under a second. Add two cheap assertions from the docket's own verified values: `|R_i/R_q|` must reproduce `0.48/2.81/1.69/1.10`, and `A_i` must match the directly measured `a_B − a_A` within 10%.

House precedent supports this strongly: every "implementation defect found and disclosed" in this program so far — including `phase3_synthesis.md`'s own `x → u` catch — was found by *comparing a computed quantity to an independently computed one*, never by reading the code. This cycle had two such comparators sitting in its own docket (item 11's ratios; Red Team's `A_i`) and checked neither. Also fold in D3's comparator fix (`T_wrong ≤ 1.53°`), D4's injection reconstruction, and D10's missing outputs (`dR_q/dψ̄`, `R_i/R_q`, `|A_i|/a`, `R_q`/`p` at 1.9608°).

### 2. Promote Iteration-49 queue item 4's desk half — the two-tone joint fit — from re-deferred to primary, re-scoped on this cycle's own measurement. Zero FDTD.

The measurement in D5 changes what this item is. It is no longer "PHOTONICS would like to try two tones"; it is the identified limiting mechanism, located: a coherent second angular tone at **1.824–1.837°** carrying R² = 0.331–0.381 of the common-mode residual, at **0.865** Rayleigh widths, in a window where the single-carrier model leaves 56% of the variance unexplained.

Fit both tones jointly — two carriers with a shared phase reference, each with an amplitude and a ramp coefficient. Three things follow that nothing else in the queue delivers:

- It converts the contaminant from a *comparator* into a *modelled term*, which is the only way out of D3 that does not require inventing another arbitrary carrier. The wrong-carrier gate becomes unnecessary rather than mis-specified.
- It gives the first direct separation of the "frequency-**or**-fringe-weight" ambiguity that Idealization 2 now has to carry under every verdict — the second tone's amplitude and its frequency become separately fitted parameters across the four ABSORB depths.
- It subsumes the curvature column: a second tone at 0.87 Rayleigh widths is precisely what a single-carrier basis reports as a spurious `u²·sinθ_c` term, and the curvature coefficient exceeds the ramp term at three of four pairs. Predict, and pre-register, that the curvature coefficient collapses once the second tone is modelled. That is a falsifiable, zero-cost test of the whole diagnosis.

Caveat this direction honestly: at 0.87 Rayleigh widths the two tones are still unresolved, so a two-tone fit will be strongly conditioned and its parameters correlated. It should be scored on *whether it removes the strain and curvature signatures*, not on the recovered second-tone period. And it must be pre-registered against R5 — two named tones at pre-specified positions, not a search.

### 3. Widen the angular window before spending a third statistic on these 31 points — and pair it with `ABSORB≈120`. ~31–93 FDTD calls.

Every problem above is one problem: `X = ptp(sin θ) = 0.0813454`, giving `1/X = 12.29` and a 41.4% fractional Rayleigh floor. That single number is why C60/C70's absolute periods are unresolvable (exp-071), why `R_q` is non-identifiable against the second tone (exp-072), why no comparator inside `[1, 4]°` can be displaced past 0.75 Rayleigh widths (D3), and why a 0.005° period split is being asked to carry a saturation argument (D12).

Extending to θ ∈ [30°, 48°] roughly triples `X`, drops the floor to ≈14%, and moves the carrier/second-tone separation from **0.87 to ≈2.6 Rayleigh widths** — the first configuration in this thread where the two contributors are genuinely separable and where "displaced carrier" means something. It also satisfies VISION's window-discipline constraint in spirit rather than by concession: a new window, not a twelfth statistic on the old one.

Run it at `ABSORB ∈ {40, 80, 120}` so the FDTD spend does double duty. The saturating and linear models diverge by **0.106°** at ABSORB=120 (2.5414 vs 2.6477) — **21× the C70–C80 split** the current argument leans on, and comfortably above even the *present* window's resolution, let alone a widened one. That is the only discriminator on the table that is larger than the instrument's noise by an order of magnitude rather than a factor of two.

**Explicitly subordinate queue items 2 (PAD-decorrelation) and 3 (mask-form ablation) to this.** Both are correct and both are worth doing — but both would currently be measured with an instrument whose ramp coefficient is non-identifiable against an unmodelled second contributor, in a window whose "wrong carrier" is 0.75 Rayleigh widths from its right one. Spending 62–93 new calls to decorrelate `PAD` and then reading the answer off `R_q` would inherit every defect in this document. Fix the instrument (1), model the contaminant (2), widen the window (3) — then decorrelate.

---

## 9. Recommendation to the Director

`phase4_results.md`'s Combined Verdict and Bottom Line stand. Its per-pair number tables do not, and should be marked as superseded rather than silently corrected — the LOGBOOK entry for Iteration 49 should record that the differential/beat instrument's first official run was executed on a mis-rotated basis, that the error was found in Phase 5 by re-verification against the docket's own pre-registered check values, and that the verdict was unaffected. That is a better entry than the one the cycle was about to write, and it is the second consecutive cycle in which the load-bearing defect was in the *handoff between two correct pieces of machinery* rather than in either piece.
