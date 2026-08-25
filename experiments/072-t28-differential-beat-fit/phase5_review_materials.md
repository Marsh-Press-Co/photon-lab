# MATERIALS & METAMATERIALS — Phase 5 Review · Panel Iteration 49 · exp-072

*Fresh sub-agent, MATERIALS & METAMATERIALS charter (sub-wavelength structure; what could physically realize the proposed optical behavior; owner of the realizability bound). Blind to the other six seats' Phase-5 reviews. Everything numerical below was re-executed against the committed `run.py`, `results.json`, `experiments/069-.../results.json`, `experiments/071-.../results.json`, `experiments/065-.../design_geometry.py` and `lab/fdtd2d.py` — nothing is taken from Phase-4 prose.*

---

## 0. Bottom line, stated first

**The Combined Verdict `NEITHER` and the headline "zero of four pairs `RESOLVED`" both survive independent re-verification.** I re-ran the entire committed pipeline with the one defect below corrected and the verdict does not move.

**But the estimator that produced every number under that verdict has a phase-reference sign error, and it fails a noiseless ground-truth recovery test.** On synthetic data built from two pure cosines with a *known* period difference, the committed pipeline returns an answer that is non-monotone in the truth and wrong in sign at four of seven injected values, including at the effect sizes this cycle's own power table predicts. Consequences: the published `R_q` column flips sign at three of four pairs, the restricted-null *p*-values move by up to 0.36 (120× the seed drift Red Team declared), the `R_i` strain flags change, the wrong-carrier gate goes from "one pair passes" to "zero pairs pass", and the injection-recovery narrative inverts completely — the pair blamed in `phase4_results.md` for the power failure becomes the *strongest* pair.

Two of the three "measured rather than merely argued" mechanism claims in the Phase-4 Bottom Line do not survive. The third — the bootstrap SE inflation — is separately an artifact of the bootstrap *resampling scheme*, not of carrier uncertainty.

**My Phase-2 findings were both implemented, and both hold.** `m₀` is genuinely loaded from JSON at runtime (`run.py:113`); the saturating-over-linear result reproduces exactly at `n_grid=3000`. But the saturating result is being reported with more specificity than the data carries — see §3.

**The realizability bound is not violated anywhere.** `ABSORB` is handled as a numerical boundary parameter throughout, Idealization 3 is carried into `phase4_results.md`'s caveat block, and no result in this cycle is used to license a materials claim. Two framing tightenings recommended, no violation found — see §4.

---

## 1. My own Phase-2 findings: verified as implemented

### 1a. `m₀` provenance (Attack 5, docket item 9) — **correctly implemented**

`run.py:113`:

```python
m0 = d071["trend"]["linear_fit"]["slope"]  # (item 9) loaded, never hand-typed
```

Verified: `experiments/071-.../results.json → trend.linear_fit.slope = 0.0025563909774436134`, and `results.json → m0_committed` carries that value to the last digit. Grep-verified: **no slope constant is typed anywhere in `run.py`**, and the value flows into `injection_recovery()` through `data["m0_committed"]`, not through a literal. Red Team's correction of my diagnosis — provenance conflation, not transcription slip — is recorded in `NOTES.md` §Setup. Docket item 9's "one-line note" landed in `NOTES.md`, not in `phase4_results.md`; the item did not specify a location, so I score this **satisfied**.

This is the one item in the cycle I would call cleanly closed.

### 1b. Saturating-vs-linear (Attack 6, docket item 9) — **reproduces exactly, but is over-specified in the write-up**

Recomputed from `results.json → saturating_vs_linear`, and independently from the four `n_grid=3000` free periods:

| Model | R² (my recomputation) | R² (reported) |
|---|---|---|
| Linear in `ABSORB` | 0.8328 | 0.8328 ✓ |
| Saturating, `L = 0.075/cell` fixed | 0.9901 | 0.9901 ✓ |

The tie-break VISION's Phase-2 critique forced was genuinely re-run at this cycle's own `n_grid=3000` (`run.py:432`, `n_grid=N_GRID_CARRIER`), not carried over from exp-069's `n_grid=400`. My Phase-2 finding survives it. Good.

**But the specificity is not earned, and this is my finding to correct, not someone else's.** I swept the decay constant and alternative concave forms on the same four points:

| Form | R² |
|---|---|
| linear | 0.8328 |
| saturating, L=0.02 | 0.9086 |
| saturating, L=0.05 | 0.9713 |
| **saturating, L=0.075 (as committed)** | **0.9901** |
| saturating, L=0.10 | 0.9942 |
| saturating, L=0.15 | 0.9898 |
| saturating, L=0.30 | 0.9823 |
| `log(ABSORB)` | 0.8988 |
| `−1/ABSORB` | 0.9453 |
| quadratic (3 params) | 0.9999 |

The result is **"any concave two-parameter form beats linear on four points"**, not "the engine-derived exponential wins." `L=0.075` is not a discriminating choice — anything in 0.05–0.5 gives 0.97–0.99. And a 3-parameter quadratic hits 0.9999, which is the honest measure of how little four points constrain a functional form.

**Second, the "engine-derived" label overstates the derivation.** `lab/fdtd2d.py:122–129`:

```python
ramp = (np.arange(self.absorb, 0, -1) / self.absorb) ** 3
...
return np.exp(-0.30 * d)
```

Red Team's `0.30/4 = 0.075` is arithmetically right as the **depth-averaged per-*step* damping exponent** (mean of a cubic ramp over its span is 1/4). But (a) the profile is *cubic*, not exponential — the exponential functional form is not engine-derived at all, only the scale constant is; and (b) it is per *time step*, and `lab/fdtd2d.py:78` sets `S = courant_frac/√2 = 0.700` cells/step, so a wave making a round trip through an `N`-cell layer accumulates roughly `2 × 0.075 × N / 0.700 ≈ 0.214·N` — the physically motivated decay constant for a *boundary return* is ≈0.21/cell, about 2.9× the value used. At `L = 0.212` the saturating fit gives R² = 0.9847, so this is **outcome-inert**; but the label "engine-derived saturating model (decay fixed at `_damping`'s own 0.075/cell, not fitted)" is doing rhetorical work the derivation does not support.

**Recommended correction for the record**, which does not change the verdict: report this as *"every concave two-parameter form tested beats linear (R² 0.90–0.99 vs 0.83) on four points against two parameters; the comparison discriminates curvature, not functional form or decay constant."* That is precisely the narrower ground Red Team's Attack 6 adopted my and THERMODYNAMICS' change on ("right for the robustness reason, not because saturation is established"). `phase4_results.md` line 166 — *"MATERIALS' and THERMODYNAMICS' finding survives the tie-break VISION's critique forced"* — reads as vindication of the saturating physics and drops that narrowing. **Caveat-propagation defect, minor, mine to flag.**

---

## 2. PRIMARY DEFECT — the estimator's phase reference is conjugated, and the ΔP sign is inverted

This is the substantive finding of my review. It was missed at Phases 2, 3 and 4.

### 2a. The defect

`run.py:122–137`, `_amp_phase_at`, returns

```python
psi = math.atan2(fit["b"], fit["a"])
```

where `_fixed_period_fit` (exp-069 `run.py:308`) fits `y = c0 + a·cos(w·u) + b·sin(w·u)`. That series equals `c0 + A·cos(w·u − ψ)` with `ψ = atan2(b, a)`. But `design_matrix` (`run.py:163`) builds

```python
theta_c = w * u + psi
```

i.e. the **complex conjugate** of the carrier that actually fits the data. Direct check on the committed data — reconstructing `Cbar` under each convention:

| Pair | ψ | R² using `cos(wu + ψ)` | R² using `cos(wu − ψ)` | free-fit R² |
|---|---|---|---|---|
| C40–C60 | 98.1° | **−1.288** | 0.4394 | 0.4394 |
| C60–C70 | 102.1° | **−1.258** | 0.4451 | 0.4451 |
| C70–C80 | 103.9° | **−1.213** | 0.4380 | 0.4380 |
| C40–C80 | 99.9° | **−1.246** | 0.4308 | 0.4308 |

The `+ψ` reference is anti-correlated with the data it is supposed to track.

Because `[cos θ_c, sin θ_c]` and `[u cos θ_c, u sin θ_c]` each span the same 2-D subspace regardless of `ψ`, the *column space* of `X5` is unchanged — which is exactly why `cond5`, the residuals, and the fitted values all look healthy and no gate tripped. What changes is the **allocation between the in-phase and quadrature coefficients**: the wrong reference rotates the `(A_i, A_q)` and `(R_i, R_q)` pairs by `2ψ ≈ 196°–208°`, i.e. a sign flip plus a genuine **16°–28° mixing of `R_i` into `R_q`**. Since `|R_i| ≳ |R_q|` at three of four pairs (Red Team's own Attack 8, verified), that mixing is not small.

There is a **second, independent sign error** that partially masks the first. `run.py:243` and `run.py:335`:

```python
delta_P_obs = -(delta_f_obs / f_bar) * carrier["T_mean_deg"]
```

With `run.py`'s `+sin θ_c` basis the fitted quadrature ramp coefficient is `R_q = −2πa·Δf·cos χ̄`, so `delta_f_obs = −Δf` and the leading minus sign inverts ΔP a second time. Because `2ψ ≈ π + ε`, the two errors nearly cancel — which is why the reported ΔP column *looks* plausible at three of four pairs and why nothing looked wrong to Phase 4.

### 2b. Ground-truth demonstration (R3 meta-rule: an artifact claim gets the check too)

Two pure cosines on the committed 31-point θ grid, identical phase, amplitude 0.005, `P_A = 2.49°`, known `ΔP`. Nothing here depends on the real data:

| true ΔP (°) | committed `run.py` | phase-fixed only | phase-**and**-sign-fixed |
|---|---|---|---|
| +0.0050 | +0.00458 | −0.00500 | **+0.00500** |
| +0.0100 | +0.00783 | −0.00999 | **+0.00999** |
| +0.0200 | **+0.00843** | −0.01996 | **+0.01996** |
| +0.0400 | **−0.01835** | −0.03967 | **+0.03967** |
| +0.0800 | **−0.09656** | −0.07357 | **+0.07357** |
| −0.0100 | −0.00951 | +0.01000 | **−0.01000** |
| −0.0400 | **+0.00268** | +0.04046 | **−0.04046** |

The corrected estimator is essentially unbiased across the whole band (the mild compression at ±0.08° is the linearization the design's own gate covers). **The committed estimator is non-monotone and sign-unstable**, and it is worst precisely in the 0.02°–0.08° range that `m₀·ΔABSORB` predicts for these pairs (0.026°–0.102°).

### 2c. Independent triangulation against Red Team's own Phase-2 table

Red Team's Attack 1 published unrestricted raw *p* from an independent implementation, declared robust across three seeds with max drift 0.003. Re-running the committed `score_all()` with only `_amp_phase_at`'s sign corrected:

| Pair | Red Team, unrestricted | committed run | **phase-fixed run** |
|---|---|---|---|
| C40–C60 | 0.1738 | 0.351 | **0.174** |
| C60–C70 | 0.7495 | 0.942 | **0.743** |
| C70–C80 | 0.4706 | 0.162 | **0.477** |
| C40–C80 | 0.3746 | 0.702 | **0.372** |

| Pair | Red Team, restricted | committed run | **phase-fixed run** |
|---|---|---|---|
| C40–C60 | 0.0057 | 0.0122 | **0.0067** |
| C60–C70 | 0.1034 | **0.4634** | **0.1042** |
| C70–C80 | 0.0041 | 0.0066 | **0.0045** |
| C40–C80 | 0.0158 | 0.0501 | **0.0171** |

The phase-fixed run reproduces Red Team's independent implementation at every cell, within the declared seed drift. The committed run does not: **C60–C70's restricted *p* differs from Red Team's by 0.36 — 120× the drift Red Team declared for its own table.** Red Team's implementation used the correct phase reference; `run.py` does not.

This is the methodological lesson. **Phase 4 published a table whose values were already sitting in Phase 2's audit ledger and never compared the two.** A three-line diff against Red Team's Attack-1 table would have caught this before the results were written up.

### 2d. What actually changes, and what does not

Full corrected re-run (phase reference fixed only; injection, nulls, gates, seeds untouched):

| Quantity | committed | corrected |
|---|---|---|
| **Combined Verdict** | NEITHER | **NEITHER** (unchanged) |
| **Pairs `RESOLVED`** | 0 of 4 | **0 of 4** (unchanged) |
| P-072-2 / P-072-3 / P-072-4 | NEITHER / NOT_EVALUABLE / NEITHER | **unchanged** |
| `power_demonstrated` | False | **False** (different cause) |
| `n_resolved_holm10` restr./unrestr. | 3 / 0 | **3 / 0** (unchanged) |
| `R_q` C40–C60 | −0.02278 | **+0.02754** (sign flip) |
| `R_q` C60–C70 | +0.00085 | **+0.00353** (4.2×) |
| `R_q` C70–C80 | +0.00593 | **−0.00355** (sign flip) |
| `R_q` C40–C80 | −0.01487 | **+0.02618** (sign flip) |
| `R_i` all four | +0.0203 / +0.0105 / +0.0036 / +0.0359 | **all sign-flipped**, magnitudes shift 35–66% |
| strain flags | F / T / F / T | **F / T / T / T** |
| Holm-adj. restricted *p* | 0.0244 / 0.4634 / 0.0199 | **0.0135 / 0.1042 / 0.0135** |
| C40–C80 derived *p* | 0.0501 | **0.0171** |
| wrong-carrier gate passes | C70–C80 only | **none** |
| injection *p* (C40-C60/C60-C70/C70-C80) | 0.0039 ✓ / 0.0082 ✓ / **0.0146 ✗** | **0.1424 ✗ / 0.0055 ✓ / 0.0001 ✓** |
| ΔP(`T_mean`) | +0.0576 / −0.0020 / −0.0144 / +0.0380 | **−0.0697 / −0.0085 / +0.0086 / −0.0668** |

Three consequences worth naming individually:

1. **`phase4_results.md`'s injection-recovery narrative is entirely an artifact.** The document says *"C70–C80's injection test misses the p ≤ 0.01 bar by a small margin (0.0146 vs 0.01)"* and builds a whole paragraph on it. Under the correction, C70–C80 is the *strongest* pair at p = 0.0001 and the failure moves to C40–C60 at p = 0.1424 — a gross failure, not a near miss. `power_demonstrated = False` survives, for a different reason and with a far larger margin.

2. **`phase4_results.md`'s Bottom Line sentence — *"the one pair whose displaced-carrier control passes (C70–C80) is exactly the pair whose significance and injection-recovery power both fail"* — dissolves.** Under the correction, no pair passes the displaced-carrier gate, and C70–C80's injection recovery is the best of the three.

3. **Red Team's own load-bearing counter-evidence against VISION does not reproduce under the committed code, and nobody noticed.** Red Team's Attack 10 refused VISION's "the sign is arbitrary" inference on the strength of *"the differential ΔP agrees in sign at 4/4 pairs with the independently-computed `n_grid=3000` absolute-period differences."* The absolute differences are +0.0830 / +0.0150 / −0.0050 / +0.0930. Red Team's differential ΔP (+0.0697 / +0.0085 / −0.0086 / +0.0668) — which I reproduce exactly once both signs are fixed — agrees **4/4**. The committed run's (+0.0576 / −0.0020 / −0.0144 / +0.0380) agrees only **3/4**, flipping at C60–C70. `phase4_results.md` reports at length that VISION's finding reproduces and is silent that Red Team's counter-evidence to it did not. That silence is a **caveat-propagation defect**: the override of VISION's gate rests on evidence the official run failed to reproduce.

### 2e. Recommended fix (one coherent change, not two)

The cleanest repair makes the code match the docket's published algebra verbatim, which is what item 5 mandated anyway. Adopt the docket's **literal** basis `[1, cos θ_c, −sin θ_c, u·cos θ_c, −u·sin θ_c]` (item 1 states it explicitly), plus the curvature column as `u²·(−sin θ_c)` exactly as item 15 states it, and fix the phase:

```python
psi = math.atan2(-fit["b"], fit["a"])   # so theta_c = w*u + psi tracks the data
```

Under that basis the published relations hold as written — `A_q = 2a·sin χ`, `R_q = 2πa·Δf`, `R_i ≈ 0` — and `dP_from`'s existing `−(Δf/f̄)·T` becomes the *correct* sign, giving ΔP = P_B − P_A. I verified this composite recovers the synthetic ground truth exactly (column 4 of the §2b table).

**Warning for whoever does it: the two errors must be fixed together.** Fixing only the obvious one (`psi`) silently inverts every ΔP, which silently inverts P-072-4's gating sign-reversal clause (`ΔP < 0 and |ΔP| ≥ 0.010 → REFUTE`). That clause is unreachable this cycle, so it is a latent landmine, not a live one — but it is armed for exp-073 if the code is reused.

### 2f. On the Phase-3 self-catch

`phase3_synthesis.md` §Implementation notes discloses one genuine bug found and fixed in development (the missing `w·x̄` shift between `x`-space and `u`-space), and states the fix was *"fitting amplitude and phase directly in `u`-space (`_amp_phase_at`) so no implicit shift is needed anywhere."* That fix is real and correct as far as it goes. But `_amp_phase_at` is the function that carries the conjugation, and the disclosed diagnostic — *"comparing the tool's own `T_mean` outputs against its `ΔP` outputs"* — is blind to it by construction: `T_mean` comes from the free-period search and does not depend on `ψ` at all, and ΔP was "fixed" until it looked plausible rather than until it recovered a known input.

House precedent is that self-catches by the Director are **expected to be checked, not assumed correct**. This one was checked here and is incomplete. That is not a criticism of disclosing it; disclosure is what made it checkable.

---

## 3. Realizability bound — no violation found

My charter owns the published / plausible / unobtainium-with-parameters call. **This cycle licenses nothing on that axis, correctly, and I find no place where it tries to.**

Checked line by line:

- `NOTES.md` Idealization 3 states `ABSORB` is a numerical boundary-condition parameter and that no realizability claim is licensed. ✓
- `phase4_results.md`'s caveat block carries it forward verbatim (*"`ABSORB` is not a material — no realizability claim licensed"*). ✓ Docket item 13's requirement that the confound-writing rule bind **under every verdict including NEITHER** is satisfied — the caveat block says *"This binds every table above, under every verdict, not only a hypothetical CONFIRM."* ✓
- No absorbed-power, no σ_abs, no ε(ω), no n(t), no `R_contact` number appears anywhere in `run.py` or `results.json`. The energy sidecar is genuinely N/A by argument, not omission. ✓
- The saturating-model paragraph is the only place a materials-shaped reading could leak in, and it is fenced: *"neither model licenses a mechanism claim on its own."* ✓

**Two framing tightenings, neither a violation:**

1. `NOTES.md` line 70–71 justifies the P-072-4 demotion with *"a **graded absorber's** boundary return is a-priori expected to saturate."* That phrasing is mine originally, and I should tighten it: `lab/fdtd2d.py::_damping` is a **graded damping mask**, not an absorber in any material sense — it multiplies E and H by `exp(−0.30·d)` per time step with a cubic depth ramp; it has no permittivity, no conductivity, no dispersion, and no impedance to match. The argument is valid *about the mask's own transfer function*, which is what makes it admissible under Idealization 3, but the word "absorber" invites exactly the reading Idealization 3 forbids. Recommend "graded damping mask" throughout exp-073.

2. Similarly, "engine-derived saturating model" should read "a two-parameter concave form with its scale constant taken from the mask's depth-averaged per-step exponent" — see §1b for why the current label overstates what was derived, and by roughly 2.9× on the constant itself.

Neither changes any verdict. Both matter because this program's realizability discipline is maintained by keeping the vocabulary bright-line, not by relying on a caveat paragraph to undo a paragraph of material-sounding prose.

---

## 4. Other defects found

### 4a. R4 recurrence — three hand-typed prose figures that do not reproduce from `results.json`

LOGBOOK's **R4** is a standing house rule: *any self-consistency figure cited in prose MUST be produced by invoking the committed function — never hand-typed.* It is the rule my own Phase-2 `m₀` finding invoked, and it recurs in this cycle:

| `phase4_results.md` claim | recomputed from `results.json` |
|---|---|
| *"Bootstrap SE is **3.7–4.8×** the naive OLS SE at every pair"* | **3.82 / 6.86 / 5.75 / 4.81 ×** → range is **3.8–6.9×** |
| Bottom Line: *"bootstrap-propagated uncertainty is **4–5×** the naive OLS estimate at every pair"* | same; also wrong, and inconsistent with the sentence above it in the same document |
| *"No pair's `\|R_q\|/SE_bootstrap` clears 2 (**0.94 / 0.09 / 0.99 / 0.42**)"* | **1.06 / 0.11 / 1.24 / 0.55** — all four wrong; two exceed 1, not 0.99 |

The qualitative claim ("none clears 2") survives; none of the six quoted figures does. All are derivable in one line from committed fields. **R4, third named instance since Iteration 25, inside the cycle that adopted an R4 fix.**

### 4b. The bootstrap SE headline is an artifact of the resampling scheme, not of carrier uncertainty

Docket item 7 mandated *"Bootstrap step 1 (carrier period and ψ̄) and propagate into `SE(R_q)`."* `run.py:342–359` implements this by **case resampling** — `rng.integers(0, n, size=(n_boot, n))`, i.e. drawing 31 rows with replacement.

That is the wrong bootstrap for this design. The 31 θ points are a deterministic, uniformly spaced angular sweep, not a random sample. Case resampling duplicates points, leaves gaps, and destroys the uniform grid the free-period search depends on — so most of the resulting spread measures *"what happens to a period search on a randomly thinned grid,"* not step-1 uncertainty.

I tested this. Two controls, 200–400 replicates each:

| Pair | committed (case resample, `n_grid=400`) | case resample at `n_grid=3000` | **residual bootstrap, fixed design** | OLS SE |
|---|---|---|---|---|
| C40–C60 | 0.02334 | 0.02334 | **0.00471** | 0.00562 |
| C70–C80 | 0.00452 | 0.00452 | **0.00077** | 0.00083 |

Two findings:

- **A control that passes, reported as such:** the bootstrap's use of a coarser `n_grid=400` (`run.py:351`) is *not* a source of inflation — identical SE at 3000. I flagged this as a suspicion and it is unfounded. Recording it because a Phase-5 check that clears something is worth as much as one that doesn't.
- **The inflation is entirely the resampling scheme.** Under a residual bootstrap on the fixed design (permute residuals, refit the carrier each replicate — which propagates exactly the step-1 uncertainty item 7 asked for), `SE(R_q)` collapses to **at or below the OLS SE**. Step-1 carrier uncertainty contributes essentially nothing at C70–C80 and modestly at C40–C60.

So `phase4_results.md`'s Bottom Line claim that *"the bootstrap-propagated uncertainty is 4–5× the naive OLS estimate at every pair"* — presented as one of three measured mechanism findings — **measures the bootstrap, not the instrument.** Item 7's intent is unmet.

### 4c. Four docket sub-items are not implemented, against an explicit "all 15 implemented verbatim" claim

`phase3_synthesis.md` line 11 and `run.py`'s docstring both assert all 15 items landed verbatim, "ZERO items un-adopted." Grep-verified absent from `run.py`, `results.json`, `NOTES.md` and `phase4_results.md`:

| Docket text | Status |
|---|---|
| Item 7: *"propagate into `SE(R_q)` **and `SE(ΔP)`**"* | `SE(ΔP)` **never computed** anywhere |
| Item 7: *"additionally report **`dR_q/dψ̄`** and `R_i/R_q` per pair"* | `dR_q/dψ̄` **never computed**; `R_i/R_q` not reported as a field (derivable) |
| Item 8: *"Report the measured `R_q` telescoping residual at a common carrier (3.79%) as the calibration that justifies the band"* | **absent** — this was an unconditional reporting requirement, not gated on `RESOLVED` |
| Item 12: *"Report ΔP **and its propagated SE** at all four carriers"* | ΔP reported at four carriers; **no SE column at any carrier** |

The `dR_q/dψ̄` omission deserves a sentence of its own. **That derivative is the sensitivity of the target coefficient to the carrier phase — the single diagnostic in the entire docket that would have exposed §2's defect immediately**, since it quantifies exactly the mixing a wrong `ψ` induces. It is the one mandated item that was dropped.

Item 9 is a fifth, partial case: it mandated *"score resolved rates against **both** the linear `m₀` ramp and an engine-derived saturating model."* `saturating_vs_linear()` fits both models to the four **absolute per-config periods**, which is a different object from scoring *resolved pair rates*; `score_all()`'s P-072-4 branch references neither model. Outcome-inert (Red Team certified P-072-4 unreachable), but the mandated scoring path does not exist in code.

### 4d. Three mandated disclosure bullets never landed, and one cross-reference is false

Docket item 13's disclosure block, grep-verified against both `NOTES.md` and `phase4_results.md`:

- *"state that P-072-6 supplies the confounded arm of Iteration-49 queue item 2 and does not substitute for it"* — **absent** (no occurrence of "queue item", "substitute").
- *"Name Iteration-49 queue item 4 (PHOTONICS' two-tone joint fit) and re-defer it with a stated reason; P-072-5 is a single-carrier contamination diagnostic, not a two-tone joint fit"* — **absent** (no occurrence of "two-tone" anywhere in the experiment directory's prose).
- *(my own item)* *"§1's C70≡C80 attribution must state that genuine saturation is an equally live reading of the same node collision"* — **absent** ("node collision", "equally live": no hits).
- Docket: *"At `n_grid=3000` the C70/C80 order reverses… One sentence in §2c, one in **Idealization 6**."* `phase4_results.md` line 158 cites *"the order-reversal … Idealization 6 discloses"* — but **`NOTES.md`'s Idealization 6 says nothing about it** (it is the no-new-FDTD idealization). `run.py:64` and `run.py:223` make the same false citation. The disclosure exists in exactly one place, `phase4_results.md`'s P-072-4 section, and three documents point somewhere it isn't.

### 4e. Two smaller items

- **Unsupported comparative.** `phase4_results.md`'s Bottom Line: *"The differential/beat-fit instrument is real and **better-conditioned** than the absolute-period route it replaces (the carrier itself resolves cleanly, R²≈0.43–0.45 at every pair, **matching** Iteration 48's own per-config fits)."* I verified the parity: exp-071's per-config free-fit R² are 0.4327 / 0.4483 / 0.4422 / 0.4337, versus this cycle's 0.431–0.445. **They match — which is a parity statement offered as evidence for a superiority claim.** No measured quantity in this cycle compares conditioning between the two routes; `cond5 ≈ 60` is a property of this design matrix, not a comparison. Separately, "resolves cleanly" is generous for a carrier explaining 43% of `Cbar`'s variance while `|R_i| ≳ |R_q|` at three of four pairs.
- **Curvature column sign convention unstated.** Docket item 15 specifies `u²·(−sin θ_c)`; `run.py:167` builds `u*u*np.sin(theta_c)`. Internally consistent with `run.py`'s own (wrong) basis, opposite to the docket's. The published coefficients (−1.058 / −0.177 / +0.025 / −1.231) therefore carry an unstated sign convention *and* are contaminated by §2's rotation. They should not be quoted until re-run.

---

## 5. Ranked top-3 candidate directions

Checked against LOGBOOK's RULED OUT registry (R1–R5) — see the note under D3, where R2 constrains what I am allowed to propose and I have adjusted accordingly.

### D1 — Re-issue the differential estimator behind a ground-truth recovery gate, before any new FDTD spend. Zero FDTD cost.

Every T28 differential number now in the record is provisional. My charter's whole function is to say what a measurement can license; an estimator that cannot recover a known Δf from noiseless synthetic data licenses nothing, and no FDTD spend downstream of it is interpretable. This has to come first.

Scope:

1. Apply §2e's composite fix (docket-literal basis + `atan2(-b, a)`), which restores `A_q = 2a·sin χ`, `R_q = 2πa·Δf`, `R_i ≈ 0` and `ΔP = P_B − P_A` to the published algebra.
2. **Add `G0-e`, a synthetic ground-truth recovery gate, to the existing arithmetic-integrity class (`G0-a/b/c/d`).** Pre-register it: inject a known ΔP into two pure cosines on the committed θ grid, sweep ΔP across the design's own predicted band (±0.005° to ±0.10°), and **HALT** unless the pipeline returns the correct sign at every point and the magnitude to within a pre-registered tolerance. This cycle established the G0 class as the right instrument; §2b is the gate it was missing. It costs milliseconds and it would have stopped this defect at Phase 3.
3. Implement the four dropped sub-items from §4c, `dR_q/dψ̄` first.
4. Replace the case-resampling bootstrap with a residual bootstrap on the fixed design (§4b), and report both so the difference is on the record rather than in a Phase-5 review.
5. Re-issue the P-072-1 / P-072-6 / ΔP-by-carrier / injection tables. Correct §4a's six arithmetic figures and §4d's four disclosure gaps at the same time.
6. State plainly in the re-issue that the Combined Verdict `NEITHER` and "zero of four `RESOLVED`" were **verified to survive** the correction — this is a numbers correction, not a verdict retraction, and saying so protects the finding.

Ranked first because it gates D2 and D3, and because it is free.

### D2 — The G40 leg: close the `ABSORB`/`PAD` confound for ~31 calls, not 62–93. (PLAN.md Iteration-49 queue item 2, cost revised down.)

**The parent's hint checks out, and it changes the cost materially.** `experiments/065-t24-absorb-boundary-sweep/design_geometry.py:287–294` already contains:

```python
"G40": config(40, 40),           # pad-only control (A held at 752, clearances +40)
"N60": config(60, 0, naive=True) # naive protocol (A drops to 732)
```

From the committed `design_geometry_output.txt`, G40 and C80 are **geometrically identical in every respect except absorber thickness**: both `nx=440, ny=1664, src_x=340, plane_x=117, obj_y=832, y_lo=80, y_hi=1584, A=752, aperture=1504, d_sp=223`. Only `absorb` differs (40 vs 80). G40 vs C40 is the mirror image: same `absorb=40`, different padding.

So one new dense sweep buys **two** clean contrasts:

- **(G40 vs C80)** — pure `ABSORB` 40→80 at fixed `PAD=40` and fixed everything else. Directly comparable to the founding C40–C80 pair at the *same* ΔABSORB=40.
- **(G40 vs C40)** — pure `PAD` at fixed `ABSORB=40`.

C40 and C80 dense at 600nm on the 31-point 36–42° grid already exist (exp-069 `block_dense`). **The minimum decorrelating build is therefore G40 alone on that grid: ~31 calls at 600nm, not PLAN.md's 62–93.** G40 has already been built, congruence-asserted, and FDTD-run (9 calls in exp-065's `block_pad`, at θ ∈ {−35, 35, 40}) — the geometry design and the C40-vs-G40 causal-identity gate are done work. This is the single largest cost reduction available in the current queue and it should move item 2's priority accordingly.

**Structural caveat that must be pre-registered, not discovered later.** The 2×2 factorial is **not completable**. The missing cell is `(ABSORB=80, PAD=0)`, i.e. `config(80, 0)` — which gives `clear_span_y = y_lo − absorb = 40 − 80 = −40`, an absorber band eating 40 cells into the source aperture. It is not constructible without breaking the congruence that defines the series, and that is precisely *why* `PAD = ABSORB − 40` was tied to `ABSORB` in the first place. **Consequence: the two main effects are identifiable from three cells only under an additivity assumption; the ABSORB×PAD interaction is not identifiable at all.** That belongs in the Phase-1 idealizations of whichever cycle runs this, stated up front, not conceded at Phase 5.

Note also that this satisfies VISION's window-discipline constraint the same way item 1 did: it is a differential/beat use of the 36–42° window, not a third absolute-period discriminator.

### D3 — Mask-functional-form ablation, promoted on a confound-freedom argument the panel has not yet made. (PLAN.md item 3, strengthened; reprioritized above item 4.)

PLAN.md item 3 is *"hold `ABSORB` fixed (e.g. `C80`) and vary the damping ramp's exponent/decay constant at fixed cell depth."* From `lab/fdtd2d.py:122–129` there are three separable knobs — the cubic exponent (3), the per-step prefactor (0.30), and the depth in cells — and the queued item varies the first two at fixed depth.

**The argument for promoting it is that it is the only T28 manipulation available that carries no `PAD` confound at all.** Changing the ramp exponent or prefactor at fixed `ABSORB` changes *nothing* about the domain size, the scene coordinates, `A`, the aperture, `d_sp`, `lever`, or the clearances. `PAD` is untouched by construction. Idealization 2 binds every deliverable in the T28 series to "`ABSORB`-or-`PAD`-or-frequency-or-fringe-weight-tied"; D2 relieves that under an additivity assumption, D3 relieves it by construction. Those are complementary, and D3's relief is the stronger of the two even though D2 attacks the founding pair directly.

The second argument is that §1b shows the four-point saturating-vs-linear comparison **cannot discriminate functional form** — any concave two-parameter form wins, the decay constant is unconstrained over an order of magnitude, and a third parameter reaches R² = 0.9999. Adding a fifth point at `ABSORB≈120` (PLAN item 4) buys one degree of freedom on a comparison that already has two and still cannot separate exponential from `log` from `1/A`. **The ablation buys a new axis instead of one more point on an under-determined curve.** That is why I rank item 3 above item 4.

Design sketch: hold `C80` fixed, run the ramp exponent at {1, 2, 3, 4} (or, cheaper and more directly interpretable, the prefactor at {0.15, 0.30, 0.60}), 31 points at 600nm each. Score with D1's corrected differential estimator against `C80` itself as the reference leg. The question it answers is the one no T28 cycle has been able to ask: **is the ~2.84° periodicity tied to a length scale in cells, or to the residual boundary-return amplitude?** Those two have identical signatures on the `ABSORB` axis and orthogonal signatures on this one.

**One design defect in the queued items, flagged under R2 discipline.** From exp-065's own committed geometry output, `ABSORB/cells-per-λ` at 600nm is 2.000 (C40), 3.000 (C60), 3.500 (C70), 4.000 (C80) — and `ABSORB≈120` would be **6.000**, exactly integer again. So "absorber thickness is an integer number of wavelengths" is an **unvaried covariate of the entire series**, held at integer for every point except C70 — which is the sole half-integer point *and* the point whose free period breaks the monotone trend and collides with C80. LOGBOOK **R2** rules out "integer resonance / shell-thickness law" as a mechanism class without new evidence, and I have no new evidence, so **I am not proposing it as a mechanism and it should not be scored as one.** What I am proposing is design hygiene: a covariate held constant across every point of a four-point series is not controlled, it is confounded, and PLAN item 4's `ABSORB≈120` preserves it rather than breaking it. Any `ABSORB` extension should deliberately break the covariate — and the ablation in D3 does so at zero `PAD` cost, by changing effective optical thickness while leaving every length, including the λ-count, fixed. That is another reason to run D3 before item 4.

---

## 6. What I am not claiming

- I am **not** claiming the Combined Verdict is wrong. It is right, and I verified it survives the correction. The cycle's central substantive finding — that `R_q`'s reach in this window is bounded by non-identifiability rather than by the noise floor — is a real advance on Iteration 48 and is not undermined by §2. What is undermined is the specific measured evidence offered for it.
- I am **not** claiming the pre-registration contamination handling was mishandled. Red Team's four conditions were implemented as code, the `CONFIRM_UNCERTIFIED` override is unconditional in `run.py:558–563`, the disclosure paragraph is carried verbatim in four places, and I verified the override is inert on this data. That part of the cycle is the best-executed part of it.
- I am **not** claiming any realizability-bound violation. §3 found none, and I looked specifically.
- The `n_grid=400` bootstrap suspicion in §4b **did not hold up** and I am reporting it as a control that cleared.
- The half-integer-λ observation in D3 is a **covariate-control argument, not a mechanism proposal**, and R2 forbids the latter without new evidence I do not have.

---

## 7. Summary of defects, for the Director's docket

| # | Defect | Severity |
|---|---|---|
| 1 | `_amp_phase_at` returns the conjugate phase (`atan2(b,a)`, should be `atan2(-b,a)`); estimator fails noiseless ground-truth recovery | **Substantive** — verdict survives, every published coefficient and *p*-value does not |
| 2 | `dP_from`/`delta_P_obs` carry a second, compensating sign inversion; latent inversion of P-072-4's gating clause | **Substantive** (currently unreachable) |
| 3 | Phase 4 never compared its *p*-values to Red Team's already-published Attack-1 table (0.36 discrepancy at C60–C70) | **Substantive** — methodology |
| 4 | Red Team's 4/4 sign-agreement counter-evidence against VISION does not reproduce (3/4) under the committed code; unreported | Substantive — caveat propagation |
| 5 | Six hand-typed prose figures do not reproduce from `results.json` (R4 recurrence) | Moderate |
| 6 | Case-resampling bootstrap; SE inflation is a scheme artifact, elevated to a Bottom-Line finding | Moderate |
| 7 | Docket items 7, 8, 12 partially unimplemented; item 9's dual-model scoring path absent — against an explicit "all 15 verbatim" claim. `dR_q/dψ̄` is the one omitted diagnostic that would have caught #1 | Moderate |
| 8 | Three item-13 disclosure bullets never landed; three documents cite an Idealization-6 disclosure that does not exist there | Moderate |
| 9 | "Better-conditioned than the absolute-period route" supported by a parity statement | Minor |
| 10 | Saturating-vs-linear over-specified; "engine-derived" decay constant understates the physical value by ≈2.9×; any concave form wins | Minor, mine to correct |
| 11 | Curvature column sign convention opposite to docket item 15 and unstated | Minor |
| 12 | "graded absorber" phrasing for a numerical damping mask — realizability-vocabulary risk, not a violation | Minor |
