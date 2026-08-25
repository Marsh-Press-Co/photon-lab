# PHASE 5 — REVIEW · QUANTUM OPTICS · Panel Iteration 49 · exp-072

*Seat charter: non-classical absorption, state-dependent or coherent interactions; mechanisms enter the bench only as effective classical parameters — σ(I), σ(x,t), dispersive ε(ω), gain — or Red Team strikes them. Fresh sub-agent, blind to the other six Phase-5 reviews. This seat wrote the exp-071 Rayleigh derivation the instrument routes around, was one of this cycle's five blind Phase-2 critics, and proposed the H₀-restricted null the design gates on. Everything below was re-executed against `run.py` and `results.json`; nothing is taken from prose.*

---

## 0. Headline

The Combined Verdict `NEITHER` is correct and I do not contest it. The **reason** published for it is not, in three separate places, and one of the three errors is mine, carried unchecked through Red Team's audit and the Director's Phase-3 verification into the frozen design.

- The pre-registered power test **cancels the effect it injects**. At C70–C80 the observed `R_q` is opposite in sign to the injected ramp, so the test recovers 44% of what it injects. Rebuilt on an H₀-restricted base, C70–C80 recovers at *p* = 0.0038 and **passes**; C40–C60 is the pair that fails. The published "power fails at C70–C80, by a small margin" is an artifact of the test's own construction, and the corrected pattern is the one I predicted a-priori at Phase 2 §5d.
- The wrong-carrier control at **3.60° is 0.746 Rayleigh widths from the carrier, not ≥1.5** — barely further than the 1.9608° comparator Red Team struck for being "provably non-diagnostic" at 0.645. Worse: 3.60° sits within 2% of the **global maximum** of the leakage function it was supposed to be clean of. That number came from my own Phase-2 §5a. I got it wrong; Red Team adopted it verbatim without recomputing; the Director's Phase-3 check re-verified only the 1.9608° figure. It is the single most consequential defect in the cycle and it is a self-catch.
- `SE(R_q)` is a **case-resampling bootstrap over a deterministic 31-point design grid**. A design-respecting residual bootstrap that still refits step 1 gives 1.6–2.3× the OLS SE, not 3.8–6.9×; two pairs then clear `|R_q|/SE > 2` where the write-up says none do.

Twelve defects follow, four of them substantive. Against that: `restricted_null_surrogates` **is** what I proposed at Phase 2, implemented correctly, and the Phase-3 self-caught u-space phase-handoff bug is real, correctly diagnosed, and correctly fixed. Credit where it is owed, in §1.

---

## 1. Re-verification: does `run.py`'s restricted null match what I proposed?

**Yes, exactly — and it is correct.** Line-by-line against my Phase-2 §4:

| My Phase-2 specification | `run.py` (`restricted_null_surrogates`, L188–196) | Status |
|---|---|---|
| Fit the 4-column H₀ basis `[1, cos θ_c, −sin θ_c, u·cos θ_c]` | `X4 = X5[:, :4]` = `[1, cos θ_c, sin θ_c, u·cos θ_c]` | **Equivalent.** Sign convention on the sin column differs; the column *span* is identical, so `yhat0` and `resid0` are bit-identical either way. Not a defect. |
| Phase-randomise that fit's residual | `fourier_phase_surrogates(resid0, …)` — amplitude spectrum preserved, DC and Nyquist held real, Hermitian symmetry enforced | **Verified correct** |
| Add it back to the fitted null series | `yhat0[:, None] + resid_surr` | **Verified correct**, and provably a no-op for the statistic: `yhat0 ∈ span(X4) ⊂ span(X5)`, so `pinv5 @ yhat0 = [coef0; 0]` exactly and the null distribution of `R_q` is centred at 0 by construction. Harmless; I would keep it for legibility. |
| Refit the 5-column model, statistic `\|R_q\|`, two-sided, N=20 000, seed `20490072` | `(pinv5 @ restricted)[4, :]`, `two_sided_p` = `(1+#{\|surr\|≥\|obs\|})/(N+1)` | **Verified correct** |
| Report both nulls always; gate on the restricted one | Both computed, both stored, both in the P-072-1 table | **Verified correct** |

Also verified correct and worth recording: G0-a/b/c/d reproduce; `m₀` is read from `experiments/071-…/results.json` at runtime with no slope constant typed anywhere in the file (grep-confirmed; `SAT_DECAY_L = 0.075` is the engine-derived, item-9-fixed decay, not a slope); Holm is a correct step-down over the three algebraically-free pairs with C40–C80 flagged `p_derived_unadjusted`; and the Phase-3 phase-handoff fix is real — `_amp_phase_at` fits amplitude and phase directly in `u = sin θ − x̄`, the same coordinate `design_matrix` builds `θ_c` in, so no residual `w·x̄` shift exists anywhere in the pipeline. I re-derived that and confirm it.

### 1a. Two objections I now raise **against my own fix**

Phase 5 is where independent re-verification catches what Phase 2–4 missed, and my Phase-2 §4 is fair game.

**(i) I called the restricted null "calibrated rather than merely conservative." I withdraw the word.** Under the committed pipeline the restricted-null SD divided by the OLS SE is:

| | C40–C60 | C60–C70 | C70–C80 | C40–C80 |
|---|---|---|---|---|
| unrestricted SD / OLS SE | 3.62 | 6.11 | 4.92 | 4.51 |
| **restricted SD / OLS SE** | **2.00** | **0.87** | **3.51** | **1.45** |

A four-fold spread across pairs for the same estimator on the same window — and at C60–C70 the null is *narrower* than the model's own OLS SE — means these *p*-values are governed by the spectral shape of each pair's H₀ residual, not by an effect size. My quoted 1.04–1.37× does not reproduce; neither does Red Team's 1.8–2.4×. Docket item 2's blanket prohibition on deriving any threshold from either set was the right call and is vindicated, but it applies to Red Team's numbers as much as mine.

**(ii) The construction leaves the signal in the null.** `resid0` is the *H₀*-fit residual, so it still contains `R_q·(u sin θ_c)`. Phase-randomising it scrambles the true ramp into the null's variance, making the ensemble width effect-size-dependent. Conservative at large effects, but not clean. A sign-flip null (random ±1 on the **5-column** residual, re-added to the H₀ fit) or a residual-permutation null removes this without touching anything else. I propose it as a fix rather than defending what I wrote at Phase 2.

---

## 2. The injection-recovery power test (docket item 4) — **substantive defect**

### D1. The test injects into a base that already contains the effect, and at C70–C80 the two cancel

`run.py` L410–413 builds the injected series as `yhat0 + resid0 + Rq_pred·X5[:,4]`. But `yhat0 + resid0 ≡ delta_AB` — the observed data. So the recovered coefficient is **exactly `R_q^obs + R_q^pred`**, which I confirm reproduces every published figure to five digits:

| Pair | `R_q^obs` | `R_q^pred` | sum | published "recovered" |
|---|---|---|---|---|
| C40–C60 | −0.02278 | −0.02021 | −0.04299 | −0.04299 |
| C60–C70 | +0.00085 | −0.01060 | −0.00975 | −0.00975 |
| C70–C80 | **+0.00593** | **−0.01053** | **−0.00460** | −0.00460 |

At C70–C80 the observed coefficient is **opposite in sign** to the injected ramp, so the test recovers 44% of the amplitude it injected. That is not a measurement of the instrument's power at the predicted effect size; it is a measurement of destructive interference between the injection and the data.

Rebuilt with an H₀-restricted base — `yhat0 + resid₅ + R_q^pred·X5[:,4]`, i.e. the observed series with its own fitted ramp removed, which recovers `R_q^pred` exactly by construction — and run through the identical restricted-null pipeline:

| Pair | as-run recovered / *p* | **corrected** recovered / *p* |
|---|---|---|
| C40–C60 | −0.04299 / 0.0039 ✓ | −0.02021 / **0.0162 ✗** |
| C60–C70 | −0.00975 / 0.0093 ✓ | −0.01060 / 0.0077 ✓ |
| C70–C80 | −0.00460 / **0.0146 ✗** | −0.01053 / **0.0038 ✓** |

**The pattern inverts.** The pair the official run reports as the power failure is the pair with the *most* power; the pair that fails is C40–C60 — which is exactly what I predicted a-priori at Phase 2 §5d ("common-mode cancellation works better between adjacent configs than between C40 and C80, so the **wide** pairs are the underpowered ones") and exactly what my Phase-2 §4 restricted-null power ratios said (0.69 / 2.26 / 2.80 / 1.38). The design's own a-priori power ordering, corrected, is confirmed by the data. The published version conceals that.

Docket item 4's wording — "inject … into the H₀-fitted series plus the observed residual" — is genuinely ambiguous between the 4-column and 5-column residual, and `run.py` took the reading that makes the test self-cancelling. This is a docket-drafting defect executed faithfully, not a coding error, and I attribute it accordingly.

**Verdict-inertness, stated honestly:** `power_demonstrated = False` under *both* constructions, so the Combined Verdict is unchanged. What changes is the published reason, and the reason is what LOGBOOK will carry into Iteration 50.

### D2. The test was scored against a looser rule than the one frozen

Docket item 4: "require recovery at the same **Holm-adjusted** *p* ≤ 0.01." `run.py` L493–494 tests the **raw** *p*. Holm over the three injection *p*-values gives:

| | C40–C60 | C60–C70 | C70–C80 |
|---|---|---|---|
| raw (official) | 0.00395 | 0.00825 | 0.01465 |
| **Holm-adjusted** | **0.0118** | **0.0165** | **0.0165** |

Under the pre-registered rule, **zero of three** pairs demonstrate power, not two of three. Under the corrected injection base, Holm gives 0.0114 / 0.0154 / 0.0162 — also zero of three. So `power_demonstrated = False` is robust, but `phase4_results.md`'s "C70–C80's injection test misses the *p* ≤ 0.01 bar by a small margin" is a two-fold understatement of a failure that, as frozen, was total. An undisclosed departure from a frozen threshold, in the looser direction, on the one gate whose purpose was to stop a power failure being read as a result.

---

## 3. Revisiting my Phase-2 §5a: is `R_q`'s non-identifiability really about T21's fringe?

`phase4_results.md`'s Bottom Line makes my §5a finding the cycle's headline mechanism: reach "bounded by non-identifiability against the window's own second, unresolved contributor (T21's 1.9608° fringe, sitting only 0.65 Rayleigh widths from the carrier)."

**With real numbers in hand, that reading is true but over-specified, and the general version is both cleaner and much stronger.** I computed the leakage function `L(T)` — the coefficient with which a unit-amplitude sinusoid of period `T` projects into `R_q` through the fixed 5-column basis, maximised over relative phase. `L(T)` depends only on the design matrix and the 31-point θ grid; **no data enters it**, so this is a design-time fact that Phase 2, 3 and 4 could all have computed:

| `T` (°) | 1.50 | **1.60** | 1.80 | **1.9608** | 2.10 | 2.4865 | 2.80 | 3.00 | **3.60** | 4.20 | 5.00 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Rayleigh widths | 1.63 | 1.38 | 0.96 | 0.69 | 0.49 | ≈0 | 0.23 | 0.37 | **0.70** | 0.94 | 1.17 |
| `\|L\|` per unit amp | 7.4 | **0.4** | 18.6 | 26.8 | 26.3 | 3.4 | 17.3 | 26.6 | **35.7** | 29.1 | 15.0 |

`R_q` is not specifically non-identified against T21's fringe. It is non-identified against **essentially any periodic contributor between ~1.8° and ~5°**, at 17–36 per unit amplitude. A second-contributor amplitude difference of only 3–6% of carrier amplitude reproduces the entire observed C70–C80 `R_q` at almost any period in that band. T21's fringe is simply the one contributor we happen to have a name for — and it is not even the worst one.

Four independent facts in the committed data are the same fact, and no one has yet said so in one sentence:

1. **Wrong-carrier gate fails at 3 of 4 pairs**, with `p(3.60°)` = 0.0195 / 0.0071 / 0.7647 / 0.0125.
2. **`R_i`, which the single-carrier model predicts is exactly zero, is strain-flagged at 2 of 4 pairs** and is 0.48–2.81× `|R_q|`.
3. **The curvature column's coefficient is large at 3 of 4 pairs** (−1.058 / −0.177 / +0.025 / −1.231).
4. **`T_delta` departs from `T_mean` by 0.124–0.254** where the design's own noiseless forward simulation (Red Team Attack 4) predicts ≤ 0.001 — a 100–250× departure.

The correct sentence is: **the single-carrier-plus-ramp model is misspecified on this window, the ramp column absorbs the misspecification, and with 2.4 carrier cycles across 31 points there is no way to tell absorption-of-misspecification from a genuine `Δf`.** That is a stronger, more general, and more falsifiable claim than "T21's fringe contaminates it," and it is what the numbers actually show.

### D3 (substantive, **my error**). The displaced wrong-carrier control is not displaced

My Phase-2 §5a wrote: "replaced by a carrier displaced ≥1.5 Rayleigh widths (**≳3.6° or ≲1.85°**)". Recomputing with the exact convention Red Team and I both verified (`X = 0.0813454`, `1/X = 12.2933`, `f̄ = 29.6505` at `T_mean = 2.4865°`, matching Red Team's `f₂ − f̄ = 7.9316` for the fringe to four digits):

| `T` (°) | 1.9608 (fringe, struck) | 1.85 (mine) | **3.60 (adopted as the gate)** | 1.533 | 6.576 |
|---|---|---|---|---|---|
| Rayleigh widths | 0.647 | 0.830 | **0.746** | 1.502 | 1.498 |

**≥1.5 Rayleigh widths requires `T ≤ 1.533°` or `T ≥ 6.576°`.** Neither of my proposed values is anywhere near it. Red Team struck EM's 1.9608° comparator as "provably non-diagnostic" at 0.645 widths, adopted my replacement verbatim, and installed a comparator at **0.746** widths — 16% further away. The Director's Phase-3 check independently re-verified the 0.6452 figure for 1.9608° and did not recompute my displacement.

And the leakage table above makes it worse than a near-miss. `|L(T)|` peaks at `T` = 3.49–3.55° with `|L|` = 35.7–36.7 across the four pairs; at 3.60° it is 35.7–36.4 — **within 2% of the global maximum**. The gate installed to certify that `R_q` is not contamination was placed essentially at the maximum of the contamination function. Red Team's own Attack 9 predicted the consequence precisely ("the comparator is guaranteed to be comparable, so the clause would fail pairs for a reason unrelated to contamination"), and it duly failed 3 of 4 pairs. `phase4_results.md` reports those failures as informative. They are not.

A genuinely diagnostic comparator exists and is free: minimising `max_pairs |L(T)|` over `T ∈ [1.2°, 2.0°]` gives **`T_ctrl ≈ 1.258°`, worst-case leak 0.90** — a 40× reduction — at 2.40 Rayleigh widths, so it satisfies the displacement criterion 3.60° never did. The window supplies 4.8 cycles there against a Nyquist limit of `T ≥ 0.4°`, so it is comfortably fittable. **R5 check:** this is the minimisation of a design-derived function of the θ grid and the basis, with no data and no target value, over a 1-D continuum already ruled non-triggering by exp-069/071 — it is not a named-constant or match-to-target search, and the Iteration-47 addendum's null-permutation requirement is not engaged. It must still be pre-registered as a single named carrier before the next run.

### D8. Red Team's counter-argument to VISION does not survive its own committed code

Attack 10 refused VISION's "the sign is set by a nuisance choice" reading on this evidence: "At `T_mean` the differential ΔP agrees **in sign at 4/4 pairs** with the independently-computed `n_grid=3000` absolute-period differences … ratios 0.84/0.57/1.72/0.72." Under the officially committed pipeline:

| Pair | absolute-period difference | committed ΔP(`T_mean`) | sign | ratio |
|---|---|---|---|---|
| C40–C60 | +0.0830 | +0.0576 | agree | +0.69 |
| **C60–C70** | **+0.0150** | **−0.0020** | **disagree** | **−0.14** |
| C70–C80 | −0.0050 | −0.0144 | agree | +2.88 |
| C40–C80 | +0.0930 | +0.0380 | agree | +0.41 |

**3/4, not 4/4** — and the disagreeing pair is one of the three algebraically free ones. Red Team itself put 4/4 at only *p* ≈ 1/8 given ~3 free signs; 3/4 with a free-pair disagreement is no evidence at all. The single piece of positive evidence used to override VISION's gate does not reproduce under the code that override was written into. `phase4_results.md` neither re-runs the check nor notes its failure. VISION's stronger reading is better supported by the official run than by the Phase-2 numbers used to strike it. I say this as the seat Red Team adjudicated *in favour of* on this same question (§2 of the audit) — the adjudication went my way on the diagnosis and VISION's way on the remedy, and the remedy half now looks under-adopted, not over-adopted.

---

## 4. Remaining defects

### D4. `SE(R_q)` uses a case-resampling bootstrap over a deterministic design grid

`run.py` L345 resamples the 31 θ-points with replacement, then refits step 1 on the resampled grid. On a designed, non-random, uniformly-spaced sweep this is the wrong bootstrap: it destroys the design, duplicates points, and drops ~11 distinct angles per replicate before a period search runs on what is left. A residual bootstrap that holds the θ design fixed and still refits step 1 on a resampled common-mode residual — which is what item 7 actually asks for ("bootstrap step 1 … and propagate") — gives:

| Pair | OLS SE | **case-boot (as run)** | **residual-boot** | boot/OLS as run | boot/OLS residual |
|---|---|---|---|---|---|
| C40–C60 | 0.00562 | 0.02219 | **0.00876** | 3.83× | **1.56×** |
| C60–C70 | 0.00116 | 0.00783 | **0.00268** | 6.86× | **2.31×** |
| C70–C80 | 0.00083 | 0.00486 | **0.00159** | 5.75× | **1.92×** |
| C40–C80 | 0.00563 | 0.02778 | **0.01003** | 4.81× | **1.78×** |

Consequently `phase4_results.md`'s "No pair's `|R_q|/SE_bootstrap` clears 2" is a property of the inflation: under the residual bootstrap the ratios are **2.60 / 0.32 / 3.73 / 1.48** and two pairs clear 2. So does the Bottom Line's "the bootstrap-propagated uncertainty is 4–5× the naive OLS estimate at every pair," which is doing load-bearing work in the published explanation of the NEITHER.

*Retraction, per verify-before-claim:* I initially suspected the bootstrap's `n_grid=400` (which reintroduces the exp-069 quantization Idealization 6 exists to remove) was inflating the SE. It is not — re-running the same case bootstrap at `n_grid=3000` gives 0.02218 / 0.00783 / 0.00486 / 0.02779, identical to four digits. The inflation is entirely the case resampling. The `n_grid=400` inconsistency remains a tidiness issue, not a numerical one.

### D5. Arithmetic errors in `phase4_results.md`

| Published | Actual (recomputed from `results.json`) |
|---|---|
| "Bootstrap SE is **3.7–4.8×** the naive OLS SE at every pair" | **3.83 / 6.86 / 5.75 / 4.81** — range 3.8–6.9×, upper end understated by 43% |
| Bottom Line: "**4–5×** the naive OLS estimate at every pair" | same — 3.8–6.9× |
| "`\|R_q\|/SE_bootstrap` … (**0.94 / 0.09 / 0.99 / 0.42**)" | **1.059 / 0.107 / 1.241 / 0.550** — all four wrong; two exceed 1 where the text implies all are below |

The conclusion drawn ("no pair clears 2") survives; none of the quoted numbers do.

### D6. Item 10's mandatory fringe disclosure is only one-third reported

Item 10 required the 1.9608° run be "retained as **mandatory disclosure** explicitly labelled a resolution identity." `run.py` computes `R_q_fringe` **and** `p_fringe` and stores both. `phase4_results.md` publishes only the ΔP column. The omitted numbers are the strongest in the cycle:

| Pair | `R_q(T_mean)` / *p* | `R_q(1.9608°)` / *p* | ratio |
|---|---|---|---|
| C40–C60 | −0.02278 / 0.0122 | −0.03425 / **0.0017** | 1.50× |
| C60–C70 | +0.00085 / 0.4634 | −0.00738 / 0.0415 | 8.69× |
| C70–C80 | +0.00593 / 0.0066 | −0.00148 / 0.5548 | 0.25× |
| C40–C80 | −0.01487 / 0.0501 | −0.04243 / **0.00015** | 2.85× |

At C40–C80 the carrier the design **declares wrong** yields *p* = 1.5×10⁻⁴ against the true carrier's 0.050 — a 300-fold stronger apparent detection at the wrong carrier. `|R_q|` is larger at the wrong carrier at 3 of 4 pairs, and `R_q_fringe` is negative at all four while `R_q(T_mean)` alternates sign. Had the fringe carrier been held to the same gate as the displaced one, it would have failed 3 of 4. This is the cleanest quantitative statement of the cycle's own headline finding, it was computed, it was mandated, and it did not reach the write-up.

### D7. The contamination disclosure's central factual claim is no longer true of the committed code

The paragraph reproduced verbatim in `run.py`, `phase3_synthesis.md`, `phase4_results.md` and `NOTES.md` states that the null choice "is **outcome-determining between Combined Verdict REFUTED and NEITHER**." Trace the committed logic on the committed numbers with the restricted null removed: `n_resolved_holm10_unrestricted = 0` → the REFUTE branch is reached → but `power_demonstrated = False` → L512 emits `UNDERPOWERED_NOT_EVALUABLE`, and L554 makes that the Combined Verdict. **`REFUTED` was unreachable regardless of the null**, because Red Team's own items 3 + 4 blocked it — and it stays unreachable under the corrected injection base of D1. The one "loosening" item in the docket (mine) moved the verdict from `UNDERPOWERED_NOT_EVALUABLE` to `NEITHER`, not from `REFUTED`.

I am **not** asking that the four binding conditions be relaxed — they were right to impose ex ante, on the information Red Team had. I am asking that the record be corrected before Iteration 50 inherits an overstated precedent, and that the correction note *why* it is overstated: Red Team's Phase-2 restricted-null *p*-values (0.0057 / 0.1034 / 0.0041 / 0.0158) differ from the committed run's (0.0122 / 0.4634 / 0.0066 / 0.0501) by up to 4.5×, against a stated seed-to-seed drift of 0.003. That is ~150× the claimed reproducibility, so Red Team's Phase-2 implementation almost certainly carried the same step-1→step-2 phase-handoff bug the Director caught at Phase 3. Every ledger row downstream of that handoff — the null-SD ratios, `|R_i/R_q|`, VISION's ΔP/z/ρ_c table "verified, every digit", the 3.79% telescoping residual, the 28.0 leak — was verified between two implementations that both had it. The step-1-only rows (grid identity, G0-b, `cond`, `X`, `1/X`, the per-config periods, the exp-071 rates, `m₀`) are unaffected and stand.

### D9. Item 12's ΔP table mixes two normalisation conventions

`dP_from` divides `R_q` by the carrier amplitude. `run.py` L338 uses each carrier's own amplitude for the `T_delta` column but L339–340 use the **true-carrier** amplitude for both wrong-carrier columns. Cbar's amplitude at 3.60° is only 0.129–0.212 of the true-carrier amplitude:

| Pair | reported ΔP(3.60°) | **consistently normalised** | ΔP(`T_mean`) |
|---|---|---|---|
| C40–C60 | −0.1080° | **−0.5082°** | +0.0576° |
| C60–C70 | −0.0443° | **−0.2736°** | −0.0020° |
| C70–C80 | −0.0005° | **−0.0037°** | −0.0144° |
| C40–C80 | −0.1615° | **−0.9072°** | +0.0380° |

Signs, and therefore the sign-non-invariance conclusion, are unaffected. Magnitudes are understated 4.7–5.6× and the four columns are not mutually comparable as presented — in a table whose stated purpose is cross-carrier comparison. The corrected figures make the non-identifiability case *far* stronger: at C40–C80 the displaced carrier reports a period difference 24× the true carrier's, with the opposite sign.

### D10. "The carrier itself resolves cleanly, R² ≈ 0.43–0.45" is an overclaim

The carrier comes from a free-period search over a 300–3000-point grid, so its R² carries a look-elsewhere premium. A permutation null of the same Cbar over the same grid gives median best-R² = 0.18 and q95 = 0.34; the observed 0.431–0.445 sits at *p* ≈ 0.004–0.009. The carrier is real and I do not dispute it — but a statistic whose chance ceiling is 0.34 does not "resolve cleanly" at 0.44, and this sentence is doing rhetorical work in the Bottom Line's contrast between the differential instrument and the absolute-period route it replaces.

### D11. The recalibrated carrier-consistency gate is uninformative, and it hides a real model-strain signal

The gate passes 4/4, but the observed statistic sits at the **30th–72nd percentile** of its own null (fraction of surrogates ≥ observed: 0.413 / 0.722 / 0.295 / 0.669). It is not passing; it is blind. Item 6 was right to strike the imported `0.414`, but calibrating to H₀ (`R_q = 0`) rather than to the **model** means the quantity the model actually predicts — Red Team's own noiseless forward simulation gives `|T_delta − T_mean|/T_mean ≤ 0.001` — can be violated by 100–250× and pass silently. Calibrating this gate against the design's own noiseless model, as Attack 4 computed but did not gate on, would have flagged all four pairs.

### D12. The REFUTE-branch counter includes the derived pair

`n_resolved_holm10_restricted` (L497–499) counts C40–C80, which item 14 and G0-b establish is the exact arithmetic sum of the other three and not an independent test. Of the three algebraically free pairs, **two** clear the relaxed 0.10 bar under the restricted null, not three. Outcome-inert here (2 > 0 fires the same branch), but per item 14 the counter that gates REFUTE should run over the free pairs only.

---

## 5. Ranked candidate directions

### 1. Re-run exp-072's own estimator with three data-free corrections, at zero FDTD cost — before anything else, and before any new spend on PLAN items 2–4

Not a new experiment: the same 124 committed points, the same frozen docket, three fixes that are each a property of the design rather than of an observed value.

- **(a) A leakage-minimising wrong-carrier control.** Pre-register `T_ctrl` at the minimum of `max_pairs |L(T)|`, computable from the basis and the θ grid with no data: `T_ctrl ≈ 1.258°`, worst-case leak 0.90 against 35.7–36.4 at 3.60°, at 2.40 Rayleigh widths. Replaces a gate placed at the maximum of the contamination function with one placed at its minimum (D3).
- **(b) An H₀-restricted injection base** — `y − R̂_q·X5[:,4] + R_q^pred·X5[:,4]` — scored against docket item 4's own **Holm-adjusted** `p ≤ 0.01` as frozen (D1, D2).
- **(c) A residual bootstrap on the fixed θ design** for `SE(R_q)`, with the step-1 refit retained (D4).

Add as disclosure: the omitted fringe `R_q`/`p` columns (D6), the consistently-normalised ΔP table (D9), and the corrected arithmetic (D5). Each fix is justified by an argument that references no observed value — Red Team's own Sec-4 condition 1 — so this does **not** re-open the contamination question; on the contrary it retires it, since D7 shows the hazard was inert in the executed design. **Rationale from my seat:** this cycle's NEITHER is almost certainly the right answer, and the panel currently cannot tell whether it is right for the published reason. Until the power test stops cancelling itself and the control stops sitting at the leakage peak, no future differential fit on this thread is readable, and every subsequent cycle inherits the ambiguity. Highest information-per-cost item available, by a wide margin.

### 2. PLAN item 2 (matched-`PAD` build), with a **leakage budget** written into the window, not just the fit

The binding lesson of this cycle is not about `PAD` and it is not about T21's fringe. It is that a 36°–42° window supplies **2.4 carrier cycles**, and at 2.4 cycles the ramp column is within a few percent of collinear with *any* second periodic contributor from ~1.8° to ~5° (§3). A matched-`PAD` run that reuses this window inherits that non-identifiability in full, no matter how cleanly it separates `ABSORB` from `PAD` — it would relieve one confound and leave the one that actually killed this cycle untouched.

Concrete ask, and it costs nothing to state: `L(T)` is computable before any FDTD call for any candidate θ span. **Strengthen VISION's item-5 window-discipline constraint** from "do not reuse the 36°–42° window a third time for an absolute-period discriminator" to "any new FDTD spend must report `max|L|` over the admitted carrier band for its proposed window and pre-register a target." A window spanning enough θ to give ~5 carrier cycles pushes the leakage maximum down by roughly the ratio of cycle counts. Within my charter's expressibility contract this enters the bench as a geometry/window parameter — no mechanism claim attaches.

### 3. Score the envelope explicitly — the one observable this cycle produced that the model forbids, and the one that is *not* Rayleigh-limited

`R_i` is predicted exactly zero by the single-carrier model and comes out at 0.48 / 2.81 / 1.69 / 1.10 × `|R_q|` (Red Team Phase 2) with strain flags at 2 of 4 under the committed run; the curvature coefficient is large at 3 of 4; `T_delta` departs from `T_mean` by 100–250× the model's own prediction. Those are one fact: **the common-mode envelope drifts across the window**, and the ramp column is currently absorbing it.

Within my expressibility contract, an envelope that varies with θ is what an effective `σ(x)` whose optical depth changes with incidence angle produces at a graded absorbing boundary — expressed purely as a classical parameter, no mechanism claim, no realizability claim, `ABSORB` still not a material. The decisive point for this seat: **an envelope is an amplitude observable, so it is not subject to the Rayleigh bound that has blocked T28 for three iterations.** Propose a zero-FDTD companion fit on the same 124 points that makes the envelope explicit (a linear or Gaussian envelope on the carrier, ramp column retained) and reports whether the fitted envelope accounts for `R_i`'s magnitude and for the `T_delta` departure.

This **subsumes and sharpens PLAN item 4's two-tone joint fit**, deferred again this cycle with a stated reason. A second tone and a drifting envelope are competing explanations of the *same* residual, they are near-degenerate over 2.4 cycles, and they should be scored head-to-head on the already-collected points — with a pre-registered discriminator — before either is allowed to justify new FDTD (item 4's `ABSORB≈120` config, 31 calls). Note the honest asymmetry: if the two are not separable at 2.4 cycles, that result is itself the answer, and it converts direction 2's window argument from a recommendation into a requirement.

**Not proposed, explicitly:** nothing above re-proposes a `P`-normalised phase offset (R5), `A_alt ≈ 3·R_OUT`, or the `A_eff ≈ 519` cluster (R5 addendum). The `T_ctrl` selection in direction 1(a) is a data-free minimisation over a 1-D continuum already ruled non-triggering, not a named-constant match search, and the Iteration-47 null-permutation requirement is not engaged.

---

## 6. Ledger — what I verified, what I could not, what I retract

**Verified by independent re-execution:** the restricted-null construction against my Phase-2 §4 (matches); `pinv5 @ yhat0` has zero 5th coefficient (the add-back is a provable no-op); every P-072-1, P-072-6, curvature, ΔP, injection, gate and G0 figure against `results.json` (all reproduce to the digits quoted, except D5's three); `Rq_recovered = R_q^obs + R_q^pred` at all three pairs; the corrected-injection *p*-values; Holm on both injection variants; the Rayleigh displacement of 1.9608°/1.85°/3.60°/1.533°/6.576°; the full `L(T)` leakage profile at all four pairs; the case-vs-residual bootstrap comparison; the restricted/unrestricted null SD ratios; the ΔP sign-agreement recount; Cbar amplitudes at all three carriers; the carrier-gate surrogate percentiles; the permutation null for the free-period R².

**Not checked:** the exp-069/071 committed data themselves (inherited trust, Idealization 6, correctly scoped); `_fixed_period_fit` and `_free_period_search` internals beyond confirming the search range `[1.0°, 4.0°]` is shared between the observed `T_delta` and the q95 surrogate grid (it is — no apples-to-oranges there); wall-clock.

**Retracted from my own earlier suspicions:** the bootstrap's `n_grid=400` is *not* the source of the SE inflation (n_grid=3000 gives identical SEs to four digits) — the case resampling is. The `X4` sin-column sign difference from my Phase-2 text is not a defect. **Retracted from my Phase 2:** the "≳3.6° or ≲1.85°" displacement figures (D3, wrong by 2×), and the characterisation of the restricted null as "calibrated" (§1a).

**Overall assessment of this cycle's execution:** the design discipline is the best in the T28 series and the Phase-3 self-catch is exemplary — the Director found a real bug, disclosed it unprompted, and fixed it correctly. But the same self-catch is why several Phase-2 "VERIFIED" ledger rows can no longer be relied on, and Phase 4 did not re-verify any of them against the corrected code. Two of the four gates that were added *specifically* to make this cycle's negative result trustworthy — the power precondition and the displaced-carrier control — are each defective in a way that inverts what they report, and both defects were computable with zero data before the run. Phase 5 caught them. That is the system working, and it is also the reason direction 1 should run before anything else.
