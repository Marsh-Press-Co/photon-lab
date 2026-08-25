# PHASE 5 — REVIEW · VISION SCIENCE · Panel Iteration 49 · exp-072

*Fresh sub-agent, VISION SCIENCE charter (PANEL.md seat 6): human perceptual limits — contrast thresholds, luminance edge detection, spectral sensitivity, adaptation, temporal sensitivity, saccadic/attentional blindness. Blind to the other seats' Phase-5 reviews. I was this cycle's VISION Phase-2 critic but hold no memory of it; everything below was recomputed this phase from `results.json`, `run.py`, and the two upstream `results.json` files, in an implementation I wrote from the docket specification rather than by calling `run.py`, precisely so the two could be compared.*

**Verdict: PARTIAL.** The cycle's headline verdict (`NEITHER`) is correct, its Combined-Verdict branch trace is arithmetically sound, and its central substantive claim — that the estimator's reach is bounded by carrier non-identifiability rather than by the noise floor — is true and is a real advance on Iteration 48. But the disclosure layer that was supposed to carry my Phase-2 finding forward softens it on all three axes where softening was possible, two headline arithmetic figures are wrong, four docket items are partly or wholly unimplemented behind a Phase-3 claim of "all 15 implemented verbatim," and the specific evidence Red Team used to override my gate does not survive the official run.

---

## 0. Verification performed this phase

I re-implemented steps 1–2 of the fixed design independently from `phase2_redteam_audit.md` Sec 6 (free-period search on `Cbar` at `n_grid=3000`; amplitude/phase fitted in the `u = sinθ − x̄` coordinate; 5-column ramped fit; `ΔP = −(Δf/f̄)·P`) without importing `run.py`'s pipeline.

| Check | Result |
|---|---|
| `T_mean`, amp, `R_q`, `T_delta` at all four pairs | **reproduce `run.py` to every published digit** |
| ΔP at all four carriers, all four pairs | **reproduce `phase4_results.md`'s table exactly** |
| Holm arithmetic (both nulls, m=3) | **verified**: 0.0199/0.0244/0.4634 and 0.485/0.702/0.942 |
| G0-b telescoping, `cond5` 59.9–61.0, carrier R² vs exp-071's per-config R² | **verified** |
| `n_resolved_holm10_restricted = 3` | **verified** (0.0244, 0.0199, 0.0501) |
| Injection arithmetic `R_q^rec = R_q^obs + R_q^pred` | **verified at all three pairs** |
| Bootstrap SE ratios as published | **NOT REPRODUCED — see D1** |
| My own Phase-2 §0b ΔP table | **NOT REPRODUCED — see D7** |

`run.py` is internally self-consistent and `phase4_results.md` transcribes it faithfully. Every defect below is in the design, the propagation, or the prose — not in the transcription.

---

## 1. Was Red Team's override of my gate reasonable? — **Half of it. The narrow half.**

### 1a. What I accept, on reflection

Red Team Attack 9/10's core argument is correct and I withdraw the corresponding part of my Phase-2 proposal. The 1.9608° comparator sits **0.6452 Rayleigh widths** from the carrier (verified: `f₂ − f̄ = 7.93` against `1/X = 12.29`). At that separation a *genuine* period difference projects into the 1.9608° ramp column by construction — Red Team measured the leakage at 28.0 per unit amplitude. A gate demanding sign-invariance against a comparator that is contaminated by the signal itself is not a falsifier; it is a guarantee of failure. "No correct measurement could pass" is the right ruling on that specific carrier, and my Phase-2 §7 was wrong to put it in the invariance set.

### 1b. What does not survive — the override's own evidence

Red Team offered two affirmative reasons to discard the *principle* rather than repair the set. Neither holds after the official run.

**Reason 1 is falsified by the committed code.** Attack 10's first bullet: *"At `T_mean` the differential ΔP agrees in sign at 4/4 pairs with the independently-computed `n_grid=3000` absolute-period differences ... including the C70/C80 reversal VISION themselves discovered."* Under the officially committed pipeline:

| Pair | absolute Δperiod (`n_grid=3000`) | official ΔP(`T_mean`) | sign agrees? |
|---|---|---|---|
| C40–C60 | +0.08303° | +0.0576° | ✓ |
| C60–C70 | +0.01500° | **−0.0020°** | **✗** |
| C70–C80 | −0.00500° | −0.0144° | ✓ |
| C40–C80 *(derived)* | +0.09303° | +0.0380° | ✓ |

Agreement is **3/4**, and **2/3 among the algebraically-free pairs**. Red Team itself priced 4/4-of-3-free at p ≈ 1/8 and called that "weak." 2-of-3 is p = 0.5 — exactly chance. The one affirmative reason to treat `T_mean` as a privileged member of the admitted carrier set evaporated when the numbers were computed by the official code, and nothing in Phase 4 revisits it.

**Reason 2 — "the underlying defect is fixed by items 6 + 7 instead" — is not fulfilled.**

- **Item 6 does not do what it was justified by.** Its stated ground (Attack 4) was that the `0.414` band "admits T21's declared-wrong 1.9608° carrier at all four pairs." The recalibrated `q95` is 0.4473 / 0.2804 / 0.4013 / 0.3525; `|1.9608 − T_mean|/T_mean` is 0.2114 / 0.2245 / 0.2258 / 0.2127. **1.9608° is still admitted at all four pairs.** At C40–C60 the new gate is also *looser* than the one it replaced (0.4473 vs 0.414), which sits awkwardly with the contamination ruling's condition-2 "strictly stricter" claim. (Outcome-inert here — every pair passes either gate — but the disclosure that the carrier gate was tightened is not supported at every pair.)
- **Item 7 is half-implemented and half-artifact.** `SE(ΔP)` — the quantity a reader needs to interpret the disclosure table at all — is never computed (D9). And the `SE(R_q)` that *was* computed inflates for the wrong reason (D2).

### 1c. What the run itself proved

The strongest instance of my principle is in this cycle's own output and is not stated as such: **ΔP changes sign between `T_mean` and each pair's own `T_delta` at 4 of 4 pairs** — and `T_delta` is the one comparator the design's *own recalibrated gate certifies as consistent at every pair* (0.1235 ≤ 0.4473, 0.1622 ≤ 0.2804, 0.2540 ≤ 0.4013, 0.1410 ≤ 0.3525). The set `{T_mean, T_delta}` contains no declared-wrong member, contains no sub-Rayleigh comparator, and is a set a correct measurement *can* pass. No pair passes it.

**My Phase-5 position:** reinstate sign-invariance, corrected — over the gate-admitted set only (`T_mean`, each pair's `T_delta`, and any carrier that is both ≥1 Rayleigh width displaced and inside `q95`), with sub-Rayleigh comparators excluded by construction. Reinstate it not as a Combined-Verdict branch but as an **admissibility condition on quoting ΔP**: a pair whose ΔP sign is not invariant across gate-admitted carriers may publish `R_q` and its p-value, but may not have its ΔP quoted as a period difference. That is my seat's standard remedy in its proper form — pin the instrument's discrimination threshold in code before scoring against it — and it costs three `lstsq` calls per pair.

---

## 2. Does the four-carrier table carry my finding faithfully? — **In kind, yes. In degree, no.**

Structurally the table is a good-faith implementation: it is unconditional, it is credited, and the sentence "sign is not invariant across carriers admitted by the design" is present and is allowed into the Bottom Line. Three things are lost in translation, and all three lose in the same direction.

**(i) `SE(ΔP)` is gone.** Docket item 12 says "Report ΔP **and its propagated SE** at all four carriers." No SE is computed anywhere in `run.py` for ΔP at any carrier. My Phase-2 table carried a `z` in every cell for exactly this reason: without a dispersion, a reader cannot tell whether +0.0576 → −0.0007 is instability or noise, and the table's rhetorical force collapses into "numbers differ."

**(ii) The 3.60° column is understated ~5× by a mixed normalization.** `run.py` normalizes ΔP at *both* wrong carriers by the **`T_mean` amplitude**, while normalizing the `T_delta` column by that carrier's own amplitude (`_amp_phase_at` is called at `T_wrong` but its amplitude return is discarded at `run.py:306`, then `amp` is passed to `dP_from` at lines 339–340). Self-consistent per-carrier normalization:

| Pair | 3.60° as published | 3.60° self-consistent | 1.9608° published | 1.9608° self-consistent |
|---|---|---|---|---|
| C40–C60 | −0.1080° | **−0.5082°** | +0.0539° | +0.0685° |
| C60–C70 | −0.0443° | **−0.2736°** | +0.0107° | +0.0144° |
| C70–C80 | −0.0005° | −0.0037° | +0.0022° | +0.0028° |
| C40–C80 | −0.1615° | **−0.9072°** | +0.0671° | +0.0829° |

Signs are unaffected, so the qualitative finding stands. Magnitudes of the carrier-dependence are understated by 4.7–5.6× in the displaced column and 1.24–1.27× in the fringe column.

**(iii) The harsher half of the same finding is withheld.** `results.json` holds `R_q` and the restricted-null p at both wrong carriers. None of it reaches the write-up:

| Pair | `R_q`(`T_mean`) / p | `R_q`(1.9608°) / p | `R_q`(3.60°) / p |
|---|---|---|---|
| C40–C60 | −0.02278 / 0.0122 | **−0.03425 / 0.0017** | +0.02036 / 0.0195 |
| C60–C70 | +0.00085 / 0.4634 | −0.00738 / 0.0415 | **+0.00907 / 0.0072** |
| C70–C80 | +0.00593 / 0.0066 | −0.00148 / 0.5548 | +0.00010 / 0.7647 |
| C40–C80 | −0.01487 / 0.0501 | **−0.04243 / 0.00015** | +0.03029 / 0.0125 |

**At three of four pairs the most significant `R_q` in the whole cycle is measured at a carrier the design declares wrong** — by up to 330× in p at C40–C80 (0.00015 vs 0.0501), with a coefficient 2.9× larger. C60–C70's only significant reading anywhere is at a wrong carrier. This is a far sharper statement of the identification failure than the ΔP table makes, it was computed by the official code, it is sitting in the committed JSON, and it is invisible to any reader of `phase4_results.md`.

**Net:** the finding survives, credited and correctly signed, quantitatively softened at every point where softening was available.

---

## 3. Perceptual-claim scan (charter duty) — **clean, with one half-landed disclosure**

I grepped both deliverables for `visib|percept|eye|naked|human|see|seen|legib|glance|apparent|Weber|Michelson|contrast|observer`. Hits in `phase4_results.md`: the caveat itself, a "see caveats below" pointer, and the contamination-disclosure heading. Hits in `NOTES.md`: Idealization 5 and the contamination heading. **No visibility, perceptibility, or detectability-by-a-human claim appears anywhere in either file.** The Phase-1 proposal's "made `C80−C40` legible" metaphor did *not* migrate into any deliverable; the Bottom Line's `ptp/mean=16.2` is presented as the named statistic it is. My charter's central question is not engaged and stays that way. This desk-only statistical cycle claims nothing my seat would have to adjudicate.

**The `C_empty` disclosure landed at 60%.** `NOTES.md` Idealization 5 carries it in full ("a dimensionless field ratio, not a Michelson/Weber perceptual contrast; `ptp/mean`-style figures are fit-conditioning statistics, never photometric ones") — correct and exactly as requested. `phase4_results.md`'s caveat block carries only the second clause; **the "`C_empty` is not a Michelson/Weber contrast" clause is missing from the results file**, which is the file LOGBOOK and PLAN cite. And docket item 13's wording was "wherever `ptp/mean` appears next to a ΔP": in the Bottom Line, `ptp/mean=16.2` shares a sentence with the zero-of-four resolution claim and is discharged by a cross-reference rather than an inline clause. Ask: restore the `C_empty` clause to `phase4_results.md`'s caveats and inline the guard at the Bottom Line's own use site.

Standing note, forward-only: T28's own thread text still names `C_empty` an "ambient-**contrast** metric." That naming, not this cycle's prose, is the durable miscitation risk, and it should be renamed or footnoted in LOGBOOK's LIVE THREADS entry rather than re-caveated once per cycle forever.

---

## 4. Defects found

Ordered by consequence. D1–D8 are new this phase; D9–D13 are compliance and framing.

**D1 [arithmetic, headline sentence, repeated in the Bottom Line].** `phase4_results.md`: *"Bootstrap SE is 3.7–4.8× the naive OLS SE at every pair"* and *"(0.94 / 0.09 / 0.99 / 0.42 respectively)"*. From `results.json`: the ratios are **3.83 / 6.87 / 5.75 / 4.81×**, and `|R_q|/SE_bootstrap` is **1.06 / 0.11 / 1.24 / 0.55**. Neither published set matches its own committed numbers; the Bottom Line then repeats the wrong range as "4–5×." Two of the four published `|R_q|/SE` values are understated across 1.0, which materially changes how a reader reads the point estimates. The claim "no pair clears 2" happens to survive; the numbers supporting it do not.

**D2 [methodology — the SE propagation is half artifact].** Item 7 asked to "bootstrap **step 1** (carrier period and `ψ̄`) and propagate." `run.py` instead case-resamples the 31 θ-points with replacement — but θ here is a *designed*, equally-spaced grid, not a sample from a population, so case resampling degrades the design (duplicated points, holes, unstable free-period search) and charges that degradation to parameter uncertainty. Three propagations, same data:

| Pair | OLS SE | case bootstrap (as coded) | **residual bootstrap, carrier refit each draw** | residual bootstrap, carrier fixed |
|---|---|---|---|---|
| C40–C60 | 0.00562 | 0.02151 (3.8×) | **0.00963 (1.71×)** | 0.00503 (0.9×) |
| C60–C70 | 0.00116 | 0.00795 (6.9×) | **0.00245 (2.11×)** | 0.00105 (0.9×) |
| C70–C80 | 0.00083 | 0.00478 (5.8×) | **0.00140 (1.69×)** | 0.00076 (0.9×) |
| C40–C80 | 0.00563 | 0.02707 (4.8×) | **0.01078 (1.91×)** | 0.00499 (0.9×) |

The middle column is what item 7 actually specified: residuals resampled on the fixed grid, carrier and `ψ̄` refit every draw. It gives **1.7–2.1×**, not 3.8–6.9×. Under it, `|R_q|/SE` = **2.37 / 0.35 / 4.24 / 1.38** — two pairs clear 2, contradicting the published sentence. I also tested and **dismiss** a concern I had about `n_grid=400` inside the bootstrap re-introducing the exp-069 quantization: SEs are identical to 4 significant figures at `n_grid=3000`, so that is not a driver. No verdict moves (gating is on surrogate p, not SE) — but one of the Bottom Line's three named legs is overstated by roughly a factor of 2.5, and in the direction that flatters the cycle's conclusion.

**D3 [implements my own item wrongly].** Mixed ΔP normalization across the disclosure table's columns — §2(ii) above.

**D4 [disclosure omission, softens my finding].** Wrong-carrier `R_q` and p withheld from the write-up — §2(iii) above.

**D5 [incomplete gate reporting].** The wrong-carrier gate has two clauses (`|R_q(3.60°)| ≤ ½|R_q(T_mean)|` **and** `p > 0.01`). `phase4_results.md`'s P-072-2 table reports only p-failures. The magnitude clause also fails at C40–C60 (0.02036 vs bound 0.01139), C60–C70 (0.00907 vs 0.00043 — 21× over) and C40–C80 (0.03029 vs 0.00744 — 4× over). At two pairs the deliberately-wrong displaced carrier yields a *larger* ramp coefficient than the true carrier. That is the gate working, and it is not reported.

**D6 [the override's evidentiary basis].** 4/4 sign agreement → 3/4 (2/3 free) under the official code — §1b above. Not revisited anywhere in Phase 4.

**D7 [unreconciled three-way estimator discrepancy — and a correction to my own Phase-2 seat].** My Phase-2 §0b `T_mean` row was +0.0697 / +0.0085 / −0.0086 / +0.0668 and Red Team's verification ledger certifies it "**VERIFIED, every digit**." The committed pipeline gives +0.0576 / **−0.0020** / −0.0144 / +0.0380 — a sign change at C60–C70 and 17–43% shifts elsewhere. My independent Phase-5 reimplementation, written from the docket spec and not from `run.py`, reproduces the **committed** numbers exactly at all four carriers, so my finding here is a self-correction: **the officially committed numbers are the trustworthy ones and my Phase-2 table is the outlier.** I swept `ψ` over ±π at every pair and no single phase offset reproduces my four Phase-2 values, so it was not a simple convention shift and I cannot recover it from a fresh context. Consequences the cycle does not state: (a) `phase4_results.md`'s "VISION's finding reproduces under the fixed, officially-committed pipeline" is true of the *finding* and false of the *numbers*, and the difference is unflagged; (b) the Phase-3 self-caught phase-handoff bug was validated against `T_mean` **periods** (which always matched) and never against ΔP, which is where it lived; (c) `ρ_c` at `T_mean` is now **0.0846** ( |0.041180 − 0.037969| / 0.037969 ), not the 0.042 in the certified table — outside the new `ρ_c ≤ 0.05` band, which matters if any successor cycle resolves pairs. The general lesson for the house: a ledger row saying "VERIFIED, every digit" certifies that two implementations agreed, not that either matches the code eventually committed. Phase 5 is where that gets caught, and it did.

**D8 [the power test is not a power test].** Docket item 4's literal text — "inject into the H₀-fitted series plus the observed residual" — is `yhat0 + resid0`, which *is* the observed data. `run.py` codes it faithfully, so `R_q^recovered = R_q^observed + R_q^predicted` (verified at all three pairs). At C70–C80 the observed +0.00593 cancels 56% of the injected −0.01053, and *that*, not power, is why p = 0.0146 misses. Stripping the observed component first (recovered = predicted exactly) inverts the pattern:

| Pair | as-coded p | corrected p |
|---|---|---|
| C40–C60 | 0.0024 ✓ | **0.0170 ✗** |
| C60–C70 | 0.0082 ✓ | 0.0064 ✓ |
| C70–C80 | **0.0153 ✗** | 0.0030 ✓ |

`power_demonstrated = False` either way and no verdict moves. But `phase4_results.md` names the wrong pair as underpowered ("C70–C80's injection test misses the `p ≤ 0.01` bar by a small margin") and credits the precondition with having "did its job of preventing exactly the 'REFUTE fires on pure power failure' defect" — it blocked REFUTE for a reason unrelated to power, at a pair that in fact has the *most* power of the three.

**D9 [dropped docket items behind a "verbatim" claim].** `phase3_synthesis.md` states "All 15 docket items are implemented in `run.py`, verbatim to the audit's specification." Not so:
- **item 7** — `SE(ΔP)` and `dR_q/dψ̄` are never computed (absent from `run.py` and `results.json`).
- **item 12** — "ΔP **and its propagated SE** at all four carriers": the SE half is absent. This was my Phase-2 request #2, adopted and then half-dropped.
- **item 8** — "report the measured `R_q` telescoping residual at a common carrier (3.79%) as the calibration that justifies the band": absent from code and both deliverables. The band it justified (`ρ_c ≤ 0.05`) is therefore uncalibrated in print — and the actual value at `T_mean` is 8.5% (D7), outside it.
- **item 13**, three bullets absent from both deliverables: "P-072-6 supplies the confounded arm of Iteration-49 queue item 2 and does not substitute for it"; "name Iteration-49 queue item 4 (PHOTONICS' two-tone joint fit) and re-defer it with a stated reason"; "genuine saturation is an equally live reading of the same node collision."
- **item 13**, C70/C80 bullet — **broken cross-reference and dropped from `NOTES.md`.** The bullet required "one sentence in §2c, one in **Idealization 6**." `NOTES.md`'s Idealization 6 is the no-new-FDTD idealization and contains no such sentence. The reversal appears only in `phase4_results.md`'s P-072-4 parenthetical, which cites "Idealization 6 discloses" — pointing at a sentence that does not exist. Meanwhile `NOTES.md`'s Mandate paragraph still reads *"whose per-config free periods rise smoothly with `ABSORB` depth"* with no caveat — the exact framing my finding refuted, uncaveated, in the file PLAN and LOGBOOK cite.

**D10 [substitute remedy does not do what justified it].** Item 6's recalibrated carrier gate still admits 1.9608° at all four pairs, and is looser than the `0.414` it replaced at C40–C60 — §1b above.

**D11 [Attack 5's own error, recurring in the paragraph that discloses it].** The disclosed saturating-vs-linear block names *"the committed linear `m₀ = 0.0025564°/cell`"* alongside `R² = 0.8328`. But `run.py::saturating_vs_linear` **refits** the linear model to the `n_grid=3000` periods and obtains slope **0.0024637** (`results.json`); the published R² belongs to that refitted slope, not to `m₀`. This is precisely MATERIALS' Attack-5 defect — attaching one estimator's goodness-of-fit to a different estimator's slope — reproduced inside the disclosure written to prevent it. (The refitted slope also lands within 0.8% of the 0.0024436 chord Attack 5 condemned.) Separately: the fitted saturating model is `P = 2.5417 − 2.0807·e^(−0.075·ABSORB)`, whose implied `ABSORB = 0` period is **0.46°** — below the free-period search's own 1.0° floor and physically meaningless — and `e^(−0.075·60) = 0.011`, so the exponential is numerically saturated from C60 onward. The model is effectively a two-level step ("C40 low, the rest high"), and `R² = 0.9901` is shape-matching on four points, not evidence that saturation is established. Whichever cycle next quotes 0.9901-vs-0.8328 needs that sentence attached.

**D12 [minor, outcome-inert].** `n_resolved_holm10_restricted = 3` includes C40–C80, which item 14 establishes is the arithmetic sum of the other three and "not an independent fifth test." Excluding it from Holm while counting it in the REFUTE-blocking tally is inconsistent. (Two free pairs already clear 0.10, so nothing moves.)

**D13 [framing].** Bottom Line: *"The differential/beat-fit instrument is real and better-conditioned than the absolute-period route it replaces (the carrier itself resolves cleanly, R² ≈ 0.43–0.45, at every pair, matching Iteration 48's own per-config fits)."* The parenthetical supports "matching," not "better": exp-071's per-config R² are 0.4327/0.4483/0.4422/0.4337 against this cycle's 0.4394/0.4451/0.4380/0.4308 — indistinguishable. The common-mode construction bought **no** improvement in carrier determination, which is the exact parameter whose uncertainty broke the estimator; the genuine improvement is in `cond5 ≈ 60`, and the sentence should say so. And "resolves cleanly" for R² ≈ 0.44 is loose language for a fit that leaves 56% of `Cbar`'s variance unexplained.

---

## 5. Ranked top-3 candidate directions

### #1 — Retire 36°–42° for **every** T28 carrier-conditioned discriminator, and expand to a pinned Rayleigh target

My Iteration-48 guidance was scoped to *absolute-period* discriminators and Red Team's queue reconciliation narrowed it further; item 1 satisfied it in letter. This cycle's result changes that ruling. The differential estimator did not escape the Rayleigh problem — it **relocated** it from the scored parameter into a fixed, unreported nuisance parameter, and then failed there. So the constraint must generalize: **the 36°–42° window is now retired for any T28 estimator that conditions on a carrier, differential and two-tone included.** Third reuse was the last one that could be justified as free.

Thresholds pinned here, before any run, per my seat's duty:

- Current window: `X = ptp(sinθ) = 0.0813454`, `1/X = 12.2933`, spanning **2.40 carrier periods**. `|f(1.9608°) − f(2.5°)| = 8.110` → **0.66 Rayleigh widths**. Below 1.0, no estimator of any flexibility can separate the ~2.5° carrier from T21's fringe. This cycle is the measured proof.
- **Minimum admissible window (1.0 Rayleigh):** `X ≥ 0.12331` → **θ ∈ [34.59°, 43.71°]**, 47 points at 0.2° step. The existing 31 points are interior and reusable: **+16 points/config, 64 new FDTD calls** for the four congruent configs.
- **Recommended target (1.5 Rayleigh):** **θ ∈ [32.47°, 46.20°]**, 70 points, +39/config, **156 calls**.
- **Comfortable (2.0 Rayleigh):** θ ∈ [30.40°, 48.82°], 93 points, 248 calls.

Two further benefits from my desk: the new points were **not** used to discover T28, which retires the accumulated-looks problem (my Phase-2 §4b — the p-values are now roughly a fifteenth look at the same 31 points) for the extended region; and the expanded window is the only condition under which queue item 4's two-tone joint fit becomes an evaluable test rather than an exercise.

**Caveat I must attach as a precondition, not an afterthought:** widening in θ is legitimate only because the fit lives in `sinθ`, where the fringe period is uniform. The *amplitude envelope's* θ-dependence over ±9° is not established anywhere in this program. Any expanded run must pre-register an envelope check — fit `a` and R² in three sub-windows and require agreement within a stated band — before a single global carrier may be assumed. Otherwise the expansion trades a resolution failure for a model-misspecification failure, and `R_i` (already the larger coefficient at three of four pairs, item 11's strain flag firing at two) is the coefficient that will absorb it.

### #2 — A zero-cost, same-shift erratum on exp-072's disclosure layer (verdict untouched)

House precedent (exp-069, exp-070, exp-071) is same-shift correction of the write-up with the pre-registered verdict left standing. Everything here is arithmetic on committed data; no FDTD, no `lab/` diff, no threshold movement:

1. Correct the bootstrap ratios (D1) and re-do the propagation as the design-respecting residual bootstrap with carrier refit that item 7 actually specified (D2) — reporting **1.7–2.1×**, and stating plainly that two pairs then clear `|R_q|/SE = 2`.
2. Fix the ΔP normalization across the four-carrier table (D3) and add `SE(ΔP)` at all four carriers (D9 / item 12).
3. Publish `R_q` and restricted-null p at both wrong carriers (D4) and both wrong-carrier gate clauses (D5). This is the single highest-value addition available at zero cost.
4. Correct the injection test to strip the observed `R_q` before injecting, and re-word the power paragraph (D8).
5. Restore the four missing item-13 bullets and item 8's 3.79% calibration; repair the dangling "Idealization 6" cross-reference and caveat `NOTES.md`'s "rise smoothly" mandate sentence (D9).
6. Restore the `C_empty` clause to `phase4_results.md`'s caveats and inline it at the Bottom Line's `ptp/mean=16.2` use site (§3).
7. Add the Attack-5-shaped correction and the unphysical-`P(0)` note to the saturating-vs-linear block (D11).
8. Add a paragraph reconciling — or, failing that, plainly flagging — the Phase-2 / Phase-4 ΔP discrepancy and my correction of my own seat (D7).

### #3 — Re-rank the Iteration-50 queue: PAD-decorrelation first; **block** the two-tone joint fit until the window is expanded

- **Queue item 2 (PAD decorrelation) should lead.** Every deliverable this cycle is bound by "`ABSORB`-or-`PAD`-or-frequency-or-fringe-weight-tied." That caveat has now survived three cycles and has begun doing real work — it is why P-072-6's amplitude channels license nothing. It is also the one item whose value does not depend on carrier resolution.
- **Queue item 4's desk-only half (PHOTONICS' two-tone joint fit) should be explicitly deferred, with the reason stated in writing** — which is also the docket item-13 bullet that went missing (D9). A two-tone joint fit is a model with *more* free parameters run on a pair of tones 0.65 Rayleigh widths apart. By this program's own R5 precedent (exp-070's null-permutation result: a dense named-constant search finds a plausible match regardless of ground truth), a flexible model on under-resolved data returns a confident, meaningless answer. Item 4's FDTD half (`ABSORB≈120`) is unaffected by this objection and can proceed.
- **Queue item 3 (MATERIALS' mask-functional-form ablation) is the strongest orthogonal buy** and should be run *inside* the expanded window from #1, purchasing both at once: varying the damping ramp's exponent at fixed cell depth tests whether the periodicity is tied to a length scale at all, and it touches neither the carrier problem nor the PAD confound.

---

## 6. One standing note from this seat, forward-only

Nothing in this program has yet defined a mapping from `C_empty` to any photometric or perceptual quantity, and the mandate's arc ("cloaking material or color") will eventually need one before any visibility language is licensed. This cycle correctly claims nothing of the kind. My seat's offer stands: name the cycle that intends to make a visibility claim, and I will pin the numbers — Michelson and Weber contrast definitions, foveal contrast-detection thresholds at the relevant spatial frequency, and the adaptation state assumed — *before* its Phase 1, per charter. Until then, `C_empty` remains a dimensionless field ratio and the word "contrast" in T28's thread text should be repaired at its source rather than re-caveated once per cycle forever.
