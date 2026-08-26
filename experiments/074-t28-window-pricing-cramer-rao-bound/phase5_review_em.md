# ELECTROMAGNETISM — Phase 5 Review · Panel Iteration 51 · exp-074

*Fresh sub-agent, EM charter (field/wave behavior, impedance matching,
energy coupling; owns reciprocity/passivity/causality bookkeeping).
Not the same instance that led this cycle's Phase 1; blind to every other
seat's Phase-5 review this cycle. Every numeric claim below was
independently re-derived by invoking the actual committed code or by
deriving the algebra from scratch — nothing is taken from `phase3_
synthesis.md`, `NOTES.md`, `phase4_results.md`, or any Phase-2 critique on
their own word (LOGBOOK R4, and the task's own explicit instruction).*

---

## 0. Reproduction baseline

Re-ran both committed scripts unmodified:

- `desk_check_pricing.py`: `CHECK0 pass=True worst_rel_err=0.00e+00`;
  every per-pair and widened-window number reproduces
  `phase1_proposal.md`'s tables bit-for-bit (`cond5≈60`,
  `cond9∈[478.4,529.4]`, `VIF_Rq∈[31.1,36.6]`, `z_joint∈[0.54,0.81]`,
  `lev_ratio≈0.80→0.914`, `L(fringe)∈[27.7,28.1]`).
- `fit_and_calibrate.py`: reproduces `phase4_results.md`'s official run
  bit-for-bit on every reported quantity (verified directly against my own
  re-run's printed cell table, e.g. `C60-C70 circ_leg α=0.01 rate=0.4610`
  = the reported 46.1×). `Combined Verdict: HALT_NULL_MISCALIBRATED_9COL`
  confirmed, independently, end to end.

House discipline held throughout this cycle: nothing below finds a
reproduction failure. My findings are about what the reproducible numbers
do and do not license, and about one undisclosed structural property of
the calibration machinery's own inputs.

---

## 1. Charter task 1 — passivity/reciprocity/causality bookkeeping on the cycle's final state

**Clean. No medium, no passivity/reciprocity/causality claim, made or
implicit, anywhere in `fit_and_calibrate.py` or the documents built on
it.**

- `grep -in "absorb|passiv|reciproc|causal|energy|power|s-param|epsilon|
  permittiv|medium"` on `fit_and_calibrate.py` returns only path
  components of reused directory names (`069-...-power-up`,
  `071-t28-absorb-depth-causal-test`) — no live term. Identical to what
  THERMODYNAMICS' Phase-2 critique found for `desk_check_pricing.py`; the
  generalization to the fit-and-calibrate script preserves it.
- The sign-flip generalization (reduced model = `X9` minus column 4,
  full model = `X9`) operates entirely on `delta_ab`, a dimensionless
  field-ratio difference, and on Gram-matrix algebra of a fixed design
  matrix. It asserts nothing about a boundary's admittance, reflectivity,
  or energy budget. `ABSORB`/`PAD` enter only as which already-collected
  `results.json` series is loaded — never as a material parameter (same
  finding as Idealization 2, re-verified against the new script).
- The **circular-shift leg** is the one place a physical-symmetry
  assumption could in principle sneak in (shifting data across θ could be
  read as invoking some angular symmetry of a boundary). It does not: the
  shift is a modular re-indexing of a *residual* vector within the
  collected 36°–42° grid, not a reflection about normal incidence or a
  source–receiver exchange. It is a **stationarity** assumption about the
  residual's own autocorrelation, not a reciprocity assumption. Correctly
  scoped as such (Idealization 11).
- **My charter's own standing missed opportunity, raised at Phase 5 of
  exp-072 and never picked up since:** a passivity falsifier exists for
  free on this exact data (`A_i = a_B − a_A` sign, per `ABSORB` pair — a
  monotonically deeper absorber cannot increase the common-mode boundary
  return if the axis is acting purely absorptively). Neither
  `desk_check_pricing.py` nor `fit_and_calibrate.py` computes it. This is
  **not a defect of this cycle** — the cycle's own scope is instrument
  statistics, not a mechanism claim, and Idealization 2/§3 correctly
  decline to engage T1 — but it is now the second consecutive T28 cycle
  (exp-072, exp-074) where my seat's own free, zero-cost passivity check
  sits unused on data already in hand. Flagged again, explicitly, so it
  does not silently become a third.

**Verdict on task 1: the "no medium, no passivity claim" cleanliness
established at Phase 1 survives unchanged into the fit-and-calibrate
machinery. No implicit physical-boundary assertion found.**

---

## 2. Charter task 2 — independent from-scratch re-derivation of `E[R_q^surr]=0`

**Confirmed exactly, by an algebraic mechanism more general than anything
cited in this cycle's own documents, and independently verified
numerically to machine precision.**

### 2.1 The derivation

Let `X9` be the `n×9` full design, `X8` the same matrix with column 4
(`R_q`'s column) deleted, both full column rank. Let `row9 = pinv(X9)[4,
:]` — the linear functional OLS uses to extract `R_q` from any response
vector: `R̂_q(y) = row9 · y` for any `y`.

By the defining property of the Moore–Penrose pseudoinverse for a
full-column-rank matrix, `pinv(X9) @ X9 = I₉` exactly. Reading off row 4:

```
row9 · X9[:, j] = δ_{j,4}    for every column j of X9.
```

`X8`'s nine... eight columns are *exactly* the other eight columns of
`X9` (columns 0,1,2,3,5,6,7,8) — none of them is column 4. Therefore:

```
row9 · X8 = 0        (the zero row-vector, exactly — row9 annihilates
                       every column of X8, one at a time, by the identity
                       above)
```

For any vector `v` in the column space of `X8` — in particular
`yhat0 = X8 @ (pinv(X8) @ y)`, the reduced-model fit to any `y` —
`row9 · yhat0 = row9 · X8 · (pinv(X8)@y) = 0 · (pinv(X8)@y) = 0` exactly.

The surrogate is `surr = yhat0 + resid9 ⊙ S`, `S` an i.i.d. Rademacher
(±1) vector. Then

```
R_q^surr = row9 · surr = row9 · yhat0 + Σ_i row9_i · resid9_i · S_i
         = 0 + Σ_i row9_i · resid9_i · S_i
```

Taking expectation over `S` (each `S_i` mean-zero, independent of
`yhat0`, `resid9`, `row9`, which are all fixed functions of the observed
`y`):

```
E_S[R_q^surr] = row9·yhat0 + Σ_i row9_i·resid9_i·E[S_i] = 0 + 0 = 0
                                                              exactly.
```

**This is not a property special to this design's conditioning or to a
9-column model.** It is a general fact about any nested pair of OLS
models where the reduced model's columns are a subset of the full
model's: the full model's own coefficient-extracting row for a dropped
column always annihilates the reduced model's fitted values, by the
pseudoinverse identity alone. Exp-073's own 5-column T2-3 construction
(`X4` = `X5` minus column 4) has the identical structure and the identical
proof; this cycle's 9-column version is a faithful, unmodified
generalization, confirmed from first principles rather than by analogy.

### 2.2 Independent numerical verification (this review's own script, not reused from any prior seat)

Ran directly against `fit_and_calibrate.build_X9_X8` at all four pairs:

| Pair | `max\|row9·X9 − e₄\|` | `max\|row9·X8\|` |
|---|---|---|
| C40–C60 | 2.31×10⁻¹⁴ | 2.31×10⁻¹⁴ |
| C60–C70 | 2.31×10⁻¹⁴ | 2.31×10⁻¹⁴ |
| C70–C80 | 1.95×10⁻¹⁴ | 1.95×10⁻¹⁴ |
| C40–C80 | 3.91×10⁻¹⁴ | 3.91×10⁻¹⁴ |

Machine-precision confirmation of the annihilation identity at every pair.
A 200,000-draw Monte Carlo of the actual `sign_flip_9col_surrogates`
function at real fitted `delta_ab` gives `row9·yhat0` between `1.4×10⁻¹⁶`
and `6.6×10⁻¹⁷` (exact zero to rounding) and empirical surrogate means of
`6.8×10⁻⁵`, `−6.4×10⁻⁶`, `4.6×10⁻⁶`, `−2.8×10⁻⁵` against `R_q9` values of
order `10⁻²`–`10⁻³` — consistent with Monte-Carlo noise around an exact
zero, not a biased construction.

### 2.3 A second closed-form identity, re-derived the same way, that the primary prediction depends on

The cycle's **primary FROZEN PREDICTION** (`phase3_synthesis.md` §4) rests
on `lev9_Rq = Σ row9ᵢ²·diagM9ᵢ / Σ row9ᵢ²` being lower (worse) than
exp-073's 5-column figure. I re-derived, from scratch, *why* this ratio is
the right quantity, rather than trusting its role as asserted:

Under pure H₀ noise `y0` with i.i.d. variance `σ²`, `resid9 = M9·y0`
(`M9 = I−H9`, the residual-maker), and since `M9` is a symmetric
idempotent projector, `Cov(resid9) = σ²·M9`, so `E[resid9ᵢ²] =
σ²·diagM9ᵢ`. Then:

```
E[Var(R_q^surr) | y0] = Σᵢ row9ᵢ²·E[resid9ᵢ²] = σ²·Σᵢ row9ᵢ²·diagM9ᵢ
```

Separately, under the same H₀, `Var(R_q_obs) = Var(row9·y0) =
σ²·‖row9‖² = σ²·Σᵢ row9ᵢ²` (the ordinary OLS-variance identity, since
`‖row9‖² = [(X9ᵀX9)⁻¹]₄₄` exactly for the pseudoinverse row of a
full-rank design). Dividing:

```
E[Var(R_q^surr)] / Var(R_q_obs) = Σ row9ᵢ²·diagM9ᵢ / Σ row9ᵢ² = lev9_Rq
                                                                  exactly.
```

Independently computed at all four pairs from `fit_and_calibrate`'s own
matrices: **0.5858, 0.5932, 0.5960, 0.5883** — matching the document's
"0.586–0.596" range to four decimal places, derived here without
reference to that number. Since `lev9_Rq < 1`, the sign-flip surrogate's
variance *understates* the true null variance of `R_q_obs` on average,
which is exactly the direction of anti-conservative bias (surrogates too
tight ⇒ real observations look artificially significant ⇒ rejection rate
inflated above nominal). This mechanistic claim in `phase3_synthesis.md`
§4/`fit_and_calibrate.py`'s own docstring is **independently confirmed,
not merely reproduced**.

**Verdict on task 2: both the centering claim (`E[R_q^surr]=0` exactly)
and the magnitude-direction mechanism (`lev9_Rq<1` ⇒ anti-conservative)
are correct, general, closed-form properties, re-derived here from first
principles and confirmed to machine precision independent of any prior
seat's work.**

---

## 3. Charter task 3 — stress-testing my own predecessor's withdrawn CLOSURE-CONFIRM for residual traces

**No residual trace found. This is a clean supersession, not a partial
one — checked deliberately hard given the charter's own warning about
same-seat defense of prior work.**

Method: grepped `phase3_synthesis.md`, `NOTES.md`, `phase4_results.md` for
every load-bearing term the withdrawn claim depended on
(`CLOSURE-CONFIRM`, `cond9≥300`, `VIF_Rq`, `z_joint`, `independent of
which null`, `51°`/widened-window figures), then read every hit in
context rather than trusting a keyword miss:

1. `phase3_synthesis.md` §1 explicitly disposes of every one of Red
   Team's ten docket items **without exception** (table, all ten rows
   "Accepted"), and states outright that `phase1_proposal.md` §5/§6 "stand
   in the record as originally written... superseded by this document."
   No later section re-imports `cond9≥300`/`VIF_Rq≥15`/`lev_ratio≥0.90` as
   gates — §5 explicitly relabels them as non-gating heuristics and the
   new test (§3–4) gates on nothing but the Monte-Carlo tolerance band.
2. The primary prediction's own justification (`lev9_Rq`, §2.3 above) is a
   **new quantity**, built fresh in this cycle's own `fit_real_pair`
   function — not a reuse or rescaling of the withdrawn `cond9`/`VIF_Rq`
   figures. I checked specifically for an implicit ×3 or similar rescaling
   of the old bars into the new leverage ratio: there is none; `lev9_Rq`
   is derived from the residual-maker `diagM9`, an entirely different
   object from `cond9`/`VIF_Rq`.
3. The **WIDENED-WINDOW-LICENSES-FURTHER-SPEND** claim (the other
   withdrawn Phase-1 finding, independently refuted by QUANTUM/Red Team in
   Phase 2) also leaves no trace: no `51°`, `46°`, or "further spend"
   language appears anywhere in `phase3_synthesis.md`, `NOTES.md`, or
   `phase4_results.md` outside the docket-resolution table itself, where
   it is explicitly marked withdrawn and "no FDTD spend is authorized."
4. The **"independent of which null eventually gates it"** framing — the
   specific phrase PHOTONICS' Phase-2 attack falsified — does not
   reappear in any form. The cycle's actual epistemic move is the opposite
   of that framing: it fits the model and gates on an actual null, exactly
   what R7 (this cycle's own new rule) requires and what the withdrawn
   claim's method skipped.
5. The **seventh-cycle decision rule** (§6, `phase3_synthesis.md`) is
   built on a genuinely different foundation: a *process* rule (repeated
   non-decisive outcomes, matching the Block-MINI precedent) rather than a
   *physics* closure claim. I checked whether this process rule quietly
   inherits the withdrawn claim's conclusion by counting this cycle as
   "resolved, by pricing" — it explicitly does the opposite: "now
   unambiguous at six once this cycle's own pricing-only claim... is
   properly withdrawn."

**Verdict on task 3: the withdrawn CLOSURE-CONFIRM claim is fully and
correctly superseded everywhere in this cycle's later documents. My
predecessor's overclaim does not survive, in whole or in disguised part,
past the Phase-2/Phase-3 correction.**

---

## 4. A new finding, mine, not present in any of this cycle's prior documents

**The circular-shift leg's "genuinely order-preserving... real per-config
residual" framing is imprecise about which correlation structure it
preserves, and omits a dominant, easily-checked structural fact about its
own inputs — though, checked computationally, this does not change the
verdict.**

`per_config_residuals()` draws four **separate** 31-point residual pools
(C40/C60/C70/C80's own per-config free-period-fit residuals), and the
calibration leg constructs synthetic null data as
`circshift(resid_A, s_A) − circshift(resid_B, s_B)` with `s_A`, `s_B`
drawn **independently**. I computed the actual cross-config correlation of
these four residual pools, which is disclosed nowhere in `phase1_
proposal.md`, `desk_check_pricing.py`, `phase3_synthesis.md`,
`fit_and_calibrate.py`, `NOTES.md`, or `phase4_results.md`:

| Pair | Pearson r |
|---|---|
| C40–C60 | 0.997 |
| C60–C70 | 0.999 |
| C70–C80 | 1.000 |
| C40–C80 | 0.992 |

The four configs' own residuals are **near-identical in shape**
(r=0.992–1.000) — consistent with a common-mode misspecification that
barely depends on `ABSORB` depth, exactly the picture QUANTUM's own
exp-072 Phase-5 review already established from a different angle
("the single-carrier-plus-ramp model is misspecified on this window").
Consequence, checked directly: the **real** full-model (`X9`) residual
after fitting actual `delta_ab` data has `std` of `3.4×10⁻⁴` /
`4.5×10⁻⁵` / `1.8×10⁻⁵` at the three free pairs — one to two orders of
magnitude **smaller** than either config's own raw residual `std`
(`≈4.0–4.5×10⁻³`), because the near-total cross-config correlation
cancels almost entirely under subtraction. **Independent random shifts
for A and B destroy that cancellation by construction**: a Monte-Carlo
check gives synthetic `y0 = circshift(resid_A,s_A) − circshift(resid_B,
s_B)` with `std ≈ 5.6–6.1×10⁻³` under independent shifts versus
`1.4–5.9×10⁻⁴` under a **same-shift** reconstruction that respects the
empirical correlation — 16×–340× larger under the as-committed
construction than the real data's own residual scale, and one to two
orders of magnitude larger than a correlation-respecting alternative.

**This sounds, at first, like it could be driving part of the reported
"circular-shift leg fails far worse than i.i.d." finding as an artifact
rather than a genuine structure effect — I checked this directly rather
than asserting it either way.** Two checks:

1. **Scale invariance.** I verified, by direct computation, that
   `two_sided_p` from `sign_flip_9col_surrogates` is *exactly* invariant
   to uniformly rescaling `y0` by any positive constant (`p(y0) =
   p(3.7·y0)` to full float precision) — a property that follows
   immediately from the construction (`obs` and every surrogate scale by
   the same factor, so their rank ordering, and hence the two-sided
   p-value, is unchanged). **The amplitude mismatch above (16×–340×)
   therefore cannot, by itself, explain the reported miscalibration
   magnitude** — sign-flip p-values do not depend on the overall scale of
   `y0`, only on its *shape* relative to the design.
2. **Direct substitution test.** I re-ran a shortened version of
   `calibrate_null`'s circular-shift leg at C40–C60 with `s_A = s_B`
   (respecting the real correlation) instead of independent draws
   (`K=400`, same `N_SURR_CAL`): rejection rates `0.3325 / 0.665 / 0.665`
   at `α = 0.01/0.05/0.10`, against the **as-committed independent-shift**
   leg's `0.3775 / 0.4875 / 0.5675` at the same `K`/seed family. **Both
   constructions are comparably, severely miscalibrated** — the
   correlation-respecting alternative is not meaningfully better
   calibrated, and is worse at two of three tested `α`.

**Conclusion: this is a real, previously-undisclosed structural fact about
the calibration machinery's own inputs (the four configs' residuals are
almost the same curve), and the current `per_config_residuals`/
`calibrate_null` code does not preserve or even mention it — Idealization
11's "tests ONE specific alternative... not every possible correlation
structure" is technically true but understates the gap: the specific
structure it fails to preserve is the empirically *dominant* one in these
particular inputs, not an arbitrary omitted alternative. But, checked
computationally rather than assumed, this gap is NOT outcome-determining
for this cycle's verdict**: a correlation-respecting reconstruction shows
comparable-or-worse miscalibration, so the qualitative finding ("real
per-config residual structure is harder to calibrate against than i.i.d.
noise") is robust to this specific construction choice, even though the
document's framing of *why* ("genuinely order-preserving... 100% of a
real residual's own θ-adjacent autocorrelation structure") describes only
the within-config axis it does preserve and is silent on the cross-config
axis it does not. **Recommend, non-blocking**: add the cross-config
correlation table above to `fit_and_calibrate.py`'s own disclosure (or a
follow-up patch) before this machinery's circular-shift leg is reused on
different data in a future cycle, since the next dataset's per-config
residuals may not be as forgivingly (comparably-miscalibrated-either-way)
correlated as this one happened to be.

---

## 5. Other checks performed, no findings

- **Nested-model correctness of `X8`**: verified `X8 = np.delete(X9, 4,
  axis=1)` removes exactly and only column 4 (`R_q`'s column) at all four
  pairs, leaving the other 8 columns (both the primary carrier's
  in-phase/ramp-in-phase columns and all 4 of the second tone's columns)
  intact — the reduced model still fits T21's fringe jointly, so the test
  genuinely asks "does `R_q` survive once the fringe is modeled," not a
  weaker question.
- **Seed/determinism**: re-ran `fit_and_calibrate.py` end to end (fixed
  `SIGN_FLIP_SEED=74051`, `CAL_SEED=74052`); every printed cell matches
  `phase4_results.md` exactly, confirming no undisclosed randomness.
- **Checkpoint framing** (not my charter's primary duty, noted in
  passing): `phase3_synthesis.md` §6's count of "six consecutive
  non-decisive cycles" (Iterations 46–51) is arithmetically correct against
  LOGBOOK's own T28 thread (exp-069 through exp-074); I found no
  off-by-one or double-counting.
- **T1/Checkpoint-criterion-2 candidacy**: re-confirmed "none" is still
  the right answer for the fit-and-calibrate machinery — nothing in it
  bounds any phenomenon constraint subset.

---

## 6. Overall verdict

**PARTIAL.**

Not `PROMISING`: T28's own mechanism question (what produces the ~2.84°
family) is exactly where exp-072 left it — no pair's `R_q`-within-the-
two-tone-fit significance was ever scored, and the pre-committed
seventh-cycle rule now blocks a same-instrument-class seventh attempt.

Not `RULED-OUT-worthy`: this cycle delivers genuine, verifiable narrowing
— a real methodological finding (a generalized sign-flip null is
anti-conservative by a *larger* margin at 9 columns than at 5, and worse
still on realistic residual structure than on i.i.d. noise), a
correctly-adopted new standing rule (R7) confirmed on its first
application, and a cleanly executed, fully-disclosed self-correction of
my own predecessor's overclaim with no residual trace (§3 above) — plus
one new, non-blocking disclosure gap this review adds (§4). This is the
same shape PANEL.md's own "mapped constraint boundary" product describes:
a real negative result about the *instrument*, honestly bounded, not a
phenomenon finding and not a wasted cycle.

The reciprocity/passivity/causality bookkeeping my charter owns is clean
throughout the cycle's final state (§1), and the two closed-form claims my
charter was specifically asked to re-derive both check out exactly, from
scratch (§2).

---

## 7. Ranked top-3 candidate directions for Iteration 52

1. **PHOTONICS' WKB/adiabatic boundary-reflectance analytic model for the
   graded-loss `ABSORB` band.** Queued twice before (Iterations 46, 47),
   confirmed dropped without execution both times, and now doubly
   motivated: it is the seventh-cycle rule's own named example of a
   "qualitatively different" approach (`phase3_synthesis.md` §6), and it
   sidesteps the entire failure mode this cycle and exp-073 both exposed
   — no fit, no null, no calibration gate to miscalibrate, because it
   computes a reflection phase from the boundary's own admittance profile
   as a function of angle, zero data. Either it explains the ~2.5° family
   directly (closing T28's mechanism question outright) or it rules it
   out analytically (narrowing the remaining candidate space) — the first
   candidate in six T28 cycles to engage a seat's own charter physics
   rather than re-verify statistics.
2. **G40/`PAD` decorrelation build** (~31 calls, per MATERIALS' verified
   geometry-reuse claim). The only queued T28 item that actually
   *relieves*, rather than discloses, the `ABSORB`-or-`PAD` compound-axis
   confound that has followed every causal claim on this thread since
   Iteration 48 — orthogonal to this cycle's own null-calibration
   findings and to item 1, and cheap. Read out on the phase-invariant
   amplitude channel (`√(A_i²+A_q²)/a`), which conditions on no fitted
   carrier phase and inherits neither the Rayleigh-resolution problem nor
   any sign-flip calibration problem.
3. **Close the cross-config-correlation disclosure gap in the calibration
   machinery itself** (this review's own §4 finding) — not a new T28
   attempt (the seventh-cycle rule bars that), but a cheap, zero-FDTD
   hygiene fix to `fit_and_calibrate.py`'s `per_config_residuals`/
   `calibrate_null`: disclose the four configs' own residual-pool
   correlation matrix, and add a same-shift (or jointly-resampled)
   alternative construction as a documented option, before this
   explicitly-kept-for-reuse machinery (`phase3_synthesis.md` §6: "remains
   available to any future carrier/phase-conditioned fit in this program,
   on different data") is pointed at a dataset where the two constructions
   might *not* agree as comfortably as they did here.
