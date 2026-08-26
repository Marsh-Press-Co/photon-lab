# PHASE 5 — REVIEW · THERMODYNAMICS · Panel Iteration 51 · exp-074

*Fresh sub-agent, THERMODYNAMICS charter (PANEL.md: where absorbed energy
goes; always asks what re-radiates and whether it would be detectable;
owns the per-proposal energy sidecar, analytic and labeled as such). Blind
to every other seat's Phase-5 review this cycle. Every number below was
independently computed by invoking `desk_check_pricing.py`'s and
`fit_and_calibrate.py`'s own committed functions, or short scratch
extensions of them — nothing is taken on the record's word, including my
own prior Phase-2 critique's `z9` table (LOGBOOK R4).*

---

## 0. Sidecar disposition — re-confirmed genuinely N/A, not by omission

`grep -in "energy\|power\|joule\|watt\|temperature\|absorb"` on both
`desk_check_pricing.py` and `fit_and_calibrate.py` returns only unrelated
string matches (path components: `power-up`, `absorb-depth-causal-test`).
Neither script computes or implies an absorbed-power figure, ΔT, emission
band, or detectability claim. The disposition is carried consistently
through every one of this cycle's own documents: `phase1_proposal.md`
Idealization 9, `phase3_synthesis.md` §7 ("all nine idealizations stand
unchanged... no energy sidecar"), `NOTES.md`, and `phase4_results.md`'s
own closing line ("No idealization changes"). **This is argued, not
omitted, at every stage — confirmed again this cycle.**

---

## 1. Independent re-derivation of `z9` (all four pairs, not just C60–C70)

Ran `fit_real_pair()` directly from the committed `fit_and_calibrate.py`
on freshly loaded data (not copied from any prior document):

| Pair | `R_q9` | `SE9` | **`z9` (mine)** | `RSS9/RSS5` (mine) |
|---|---|---|---|---|
| C40–C60 | +0.02202 | 0.02612 | **0.8428** | 0.5008 |
| C60–C70 | −0.01572 | 0.00312 | **5.0333** | 0.1933 |
| C70–C80 | −0.00201 | 0.00123 | **1.6342** | 0.0590 |
| C40–C80 | +0.00744 | 0.02158 | **0.3449** | 0.3454 |

Matches `phase4_results.md`'s table and my own predecessor's Phase-2
critique to 3–4 decimal places. **C60–C70's `z9=5.03` is real, not a
transcription artifact** — it survives independent re-computation from the
raw committed data through the raw committed formulas a third time (my
Phase-2 predecessor, Red Team's Phase-2 audit, and now this Phase-5
review, three separate invocations, byte-for-byte agreement).

Re-ran the official `fit_and_calibrate.py` end-to-end (fixed seeds
`SIGN_FLIP_SEED=74051`, `CAL_SEED=74052`): output is **bit-identical** to
the committed `fit_and_calibrate_results.json` on every field except
`elapsed_s` (I diffed programmatically, not by eye). `Combined Verdict:
HALT_NULL_MISCALIBRATED_9COL` reproduces exactly.

---

## 2. Re-checking the calibration test's two legs — both confirmed, and confirmed *robust*

### 2a. The i.i.d. leg
Reproduces exactly: worst inflation 7.2×–11.2× nominal at α=0.01 across
the three pairs (my own re-tabulation directly from the committed JSON;
`phase4_results.md`'s stated range "8.7×–11.2×" is the *per-pair maximum
across the three σ values*, which I confirm — C40–C60 max=11.2×,
C60–C70 max=10.3×, C70–C80 max=8.7×; the true *minimum* across all 9
i.i.d. cells is 6.9×, still a large failure, just not the headline number).

### 2b. The circular-shift leg — is `E[R_q]=0` real, or a subtle bias?

This is the specific question my charter was asked to settle. I checked
it two ways, independently of the 1000-draw Monte Carlo the script itself
runs.

**Analytically:** `_fixed_period_fit`'s design matrix (exp-069's `run.py`)
includes an intercept column (`np.ones_like(x)`), so its OLS residual is
orthogonal to that column — `sum(resid)=0` **exactly**, an algebraic
identity of least squares, not an approximation. A circular shift is a
permutation of a fixed vector's entries; averaged over all `n_a` possible
shifts (uniform), the expectation of `circshift(resid, s)` at every
position is the vector's own mean — zero. `R_q^surr = row9 · y0` is
*linear* in `y0` (a fixed `pinv9` row dotted with the data), so
`E[R_q] = row9 · E[y0] = row9 · 0 = 0` follows immediately from linearity.
**The claim is exactly true by construction, not an empirical accident.**

**Numerically, exhaustively (not sampled):** for C60–C70 I enumerated
**all 31×31=961** possible `(sA, sB)` combinations (not the 1000-draw
Monte Carlo subsample the calibration test uses) and computed the exact
`R_q` for each:

```
Exhaustive mean(R_q) over all 961 shift combos: 1.48e-17   (machine-precision zero)
Exhaustive std(R_q):  0.5568
Exhaustive max|R_q|:  1.310
```

**Verdict on the specific question asked: no bias in the mean. The
`E[R_q]=0` claim is confirmed to machine precision by full enumeration,
independent of RNG seed or sample size — it cannot be an artifact of
Monte Carlo noise.**

### 2c. What *is* real, and previously unquantified: two structural facts explain the leg's severity

Having ruled out a location bias, I checked whether the *severity*
(38.9×–46.1× vs. the i.i.d. leg's 8.7×–11.2×) depends on an unstated
design choice — specifically, `calibrate_null()` draws `sA` and `sB`
**independently** (`rng_master.integers(0, n_a)` called twice). An
alternative, equally defensible construction — a single shared shift
(`sA=sB`), preserving each pair's own real cross-config relationship while
randomizing only the absolute θ-registration — was never tested or
disclosed as a considered-and-rejected alternative.

**I ran that counterfactual myself** (same script's own
`sign_flip_9col_surrogates`/`circular_shift`, K=1000, independent seed):

| Pair | independent-shift ×nominal (α=0.01, official run) | **coupled-shift (sA=sB) ×nominal, mine** |
|---|---|---|
| C40–C60 | 38.9× | **36.1×** |
| C60–C70 | 46.1× | **35.9×** |
| C70–C80 | 44.1× | **52.3×** |

**The independent-vs-coupled choice does not explain the severity** — both
constructions fail comparably badly on the real data. This ruled out my
own initial hypothesis (that independent re-phasing of near-identical
signals was manufacturing the extreme figure) — a hypothesis I formed,
then tested, then discarded on the evidence, per this program's own
verify-before-claim discipline.

**What does explain it, isolated by a control experiment:** I generated a
single fixed draw of matched-scale (`σ≈0.0045`) i.i.d. Gaussian noise
(lag-1 autocorrelation −0.0003, genuinely white) and ran both shift
variants on it:

| Construction | matched-scale **white noise** ×nominal (α=0.01) | **real per-config residuals** ×nominal (α=0.01) |
|---|---|---|
| independent-shift | 2.2×–4.0× | 38.9×–46.1× |
| coupled-shift | **≈0×** (well-calibrated) | 35.9×–52.3× |

The real per-config residuals (`per_config_residuals()`) have **lag-1
autocorrelation 0.92–0.94** at every one of the four configs — genuinely
smooth, structured, far from white — while my synthetic white-noise
control shows autocorrelation ≈0 and, critically, is **well-calibrated
under coupled shift and only mildly inflated under independent shift**.
**This isolates real residual autocorrelation (not the shift-pairing
choice) as the dominant driver of the circular-shift leg's extreme
severity** — the record's own framing ("the real per-config residuals
carry genuine, exploitable θ-adjacent correlation structure that an
i.i.d.-of-any-marginal-shape null cannot represent") is *correct*, and
this is the first place in the record that quantifies it (`~0.93` lag-1,
not previously stated) and confirms it against a proper white-noise
control rather than asserting it from the calibration-rate gap alone.

### 2d. A genuinely new, unremarked fact: the four configs' residuals are nearly the same signal

While building the coupled-shift counterfactual I found something not
stated anywhere in this record: the pointwise (true θ-alignment)
correlation between each pair's own two per-config residuals is
**0.997–0.9995** (C40↔C60: 0.9967, C60↔C70: 0.9991, C70↔C80: 0.9995).
This means what `per_config_residuals()` calls "each config's own real
per-config residual" is, physically, **overwhelmingly shared, common-mode
leftover structure across all four `ABSORB` depths — not independent
per-config measurement noise at all**. This is a sharper, residual-level
confirmation of the T28 program's own first-principles finding
(`A=752` cells identical across configs by construction, LOGBOOK T28
entry) — the same shared-geometry argument that already explains why
`C40(θ)` and `C80(θ)` individually carry the ~2.5° family (exp-070,
P-070-1). It does not change the calibration verdict (§2c shows the
failure is real and robust either way), but it **is** new, decision-useful
information: if four configs' *leftover, unexplained* residuals after
their own best single-sinusoid fit are essentially the same vector, the
common-mode signal these residuals still contain is a better,
more information-dense object to analyze directly than any further
pairwise *differencing* of it.

---

## 3. Checking `RSS9/RSS5` again — confirmed, mechanism restated precisely

| Pair | `RSS5` | `RSS9` | `RSS9/RSS5` |
|---|---|---|---|
| C40–C60 | 7.296e-06 | 3.654e-06 | 0.501 |
| C60–C70 | 3.257e-07 | 6.295e-08 | 0.193 |
| C70–C80 | 1.681e-07 | 9.916e-09 | 0.059 |
| C40–C80 | 7.346e-06 | 2.538e-06 | 0.345 |

Matches my own Phase-2 critique and Red Team's Phase-2 audit exactly.
This is the numerator of the mechanism Red Team named (§2, its audit):
adding 4 correlated columns at `cond9≈480–530` lets the model absorb
5–94% of `delta_ab`'s own sum-of-squares, far beyond what a VIF-only
rescaling (`z_joint_optimistic`) predicted — confirmed still true, and
untouched by this cycle's own fit-and-calibrate result, which correctly
never re-litigates it (it answers *whether z9 is trustworthy*, not
*whether z9 is large*).

---

## 4. Was there an energy-conservation-shaped bookkeeping gap analogous to my prior finding?

My prior Phase-2 critique found `z_joint(optimistic)` was asserted as a
valid upper bound without ever being checked against the actual fit — a
ledger that didn't close in the direction it needed to. I looked for the
same *shape* of defect in this cycle's new machinery (a claimed invariant
that the code never actually verifies against the data it's claimed of)
and found:

- **No such gap in the mean-bias claim** (§2b) — `E[R_q]=0` is checked
  here, exhaustively, for the first time in the record, and holds exactly.
- **A real, but non-fatal, gap in the *severity* claim's stated
  justification** (§2c) — the record attributes the circular-shift leg's
  extra severity over the i.i.d. leg to "genuine θ-correlated residual
  structure," which is correct, but ships with **no quantification** (no
  lag-1 autocorrelation number, no white-noise control, no
  independent-vs-coupled-shift check) anywhere in `phase3_synthesis.md`,
  `fit_and_calibrate.py`, or `phase4_results.md`. The claim happens to be
  right — I verified it three independent ways above — but it was
  asserted, not demonstrated, at the exact point where this program's own
  R4/R5/R6/R7 lineage says a claim needs a control, not just a plausible
  narrative. This is smaller than my prior cycle's finding (which
  inverted a scored verdict); here the *scored verdict is unaffected* —
  but it is the same failure shape at lower stakes, and it cost me under
  an hour to close with tools already in the committed script.
- **A genuine, independently-caught arithmetic error, R4-shaped:**
  `phase4_results.md` states the calibration gate "fails at every one of
  **72** cell combinations (3 free pairs × **24** cells: 3 sigmas × 3
  alphas for the i.i.d. leg, plus 3 alphas for the circular-shift leg)."
  3×3+3 = **12**, not 24; 3×12 = **36**, not 72. I counted the actual
  cells directly from the committed `fit_and_calibrate_results.json`:
  **36 cells total, all 36 fail** (confirmed programmatically, not by
  eye). The qualitative claim ("every cell fails") is correct and
  unaffected — but the count is wrong by exactly 2×, the same *shape* of
  defect (an aggregate/count figure not checked against the underlying
  per-cell structure) that R4's own Iteration-50 addendum was written to
  police ("144/144" vs. the true "143/144"). Non-outcome-determining;
  should be corrected in the record per house discipline.

---

## 5. Summary of independent findings

1. **`z9=5.03` at C60–C70 re-confirmed a third time**, from raw data
   through raw committed formulas, independent of my own prior Phase-2
   critique and of Red Team's Phase-2 audit. (§1)
2. **`Combined Verdict: HALT_NULL_MISCALIBRATED_9COL` reproduces
   bit-exact** under the official fixed seeds. (§1)
3. **The circular-shift null's `E[R_q]=0` claim is exactly true — no
   bias — confirmed both algebraically and by full 961-combination
   enumeration**, not merely by the 1000-draw Monte Carlo the script
   itself runs. (§2b)
4. **The circular-shift leg's extra severity over the i.i.d. leg is
   robust to the independent-vs-coupled shift choice** (both
   ~36×–52× at α=0.01) **and is attributable to the real per-config
   residuals' own strong autocorrelation (lag-1 ≈ 0.92–0.94)**,
   confirmed against a matched-scale white-noise control that shows the
   opposite behavior (near-zero inflation under coupled shift). This
   strengthens, and for the first time quantifies, the record's own
   causal story. (§2c)
5. **New, unremarked, physically meaningful finding: the four configs'
   own per-config residuals are cross-correlated at r=0.997–0.9995** —
   essentially the same shared signal, not independent per-config noise —
   consistent with, and a residual-level sharpening of, this program's
   own established shared-geometry (`A=752` cells) finding. (§2d)
6. **`RSS9/RSS5` re-confirmed exactly**, mechanism restated. (§3)
7. **A minor, R4-shaped arithmetic error in `phase4_results.md`**: "72
   cell combinations" should be **36** (12 per pair × 3 pairs, not 24 per
   pair). Non-outcome-determining. (§4)
8. **The circular-shift severity claim was correct but under-evidenced**
   in the committed documents — asserted from the calibration-rate gap
   alone, with no autocorrelation number, no white-noise control, and no
   check of the independent-vs-coupled-shift degree of freedom. All three
   now exist, in this review, and should be folded into the permanent
   record. (§4)
9. **Energy sidecar: genuinely N/A, correctly argued at every stage of
   this cycle's own documents, not omitted.** (§0)

---

## 6. Verdict

**PROMISING** — with the scope stated precisely, matching this cycle's
own careful distinction between the *instrument* and the *substantive
question*.

- **This cycle's own contribution (the fit, the two-leg calibration test,
  R7): PROMISING, independently re-verified sound.** Every headline number
  reproduces bit-exact; the one claim I could not immediately verify from
  the documents alone (why the circular-shift leg is so much worse) I
  independently tested three ways and found **correct, robust, and
  previously under-quantified** — a genuine strengthening, not a
  weakening, of the record.
- **The T28 differential/two-tone-fit sub-thread, on this exact
  instrument class, is correctly and robustly HALTed.** My own
  independent seed reproduces comparable inflation factors (41× at
  α=0.01 for C60–C70, vs. the official run's 46.1×); my coupled-shift
  counterfactual does not rescue it (35.9× instead of 46.1×, still a
  catastrophic failure); nothing I found suggests this HALT would
  reverse under a different reasonable construction of the same
  instrument class. The pre-committed seventh-cycle decision rule
  (`phase3_synthesis.md` §6) correctly bars a further sign-flip/
  permutation attempt on this basis without a qualitatively different
  strategy — my own review adds no reason to relax that.
- **`z9=5.03` at C60–C70 remains genuinely unresolved**, not because the
  number is in doubt (three independent re-derivations agree to 4
  decimals) but because no valid null exists yet to test its
  significance. This is not "ruled out" — it is a real, open, currently
  un-testable-by-this-instrument finding, exactly as `phase4_results.md`
  states.

---

## 7. My own ranked top-3 candidate directions for Iteration 52

**1. Fit the near-universal common-mode residual directly, not
another pairwise difference (new this review, zero FDTD).** §2d's
finding — the four configs' own per-config residuals are correlated at
r=0.997–0.9995, i.e., essentially the same shared leftover signal — means
the richest, most information-dense object left unexamined in this record
is that shared residual itself (any one config's residual is nearly as
good as all four; averaging the four for noise reduction costs nothing).
A proper multi-tone fit (T21's 1.9608° fringe *and* a free second period,
jointly, on the *un-differenced* common-mode residual, not `delta_ab`) is
a qualitatively different analysis than the barred sign-flip/permutation
route on `X9` — it does not difference two nearly-identical signals against
each other (which is what has made every differential attempt since
Iteration 49 underpowered), and it directly tests whether the ~2.5° family
is present, with a clean amplitude, in the object every config already
independently confirms. This also directly serves PHOTONICS' own queued
item (below): whatever period this fit recovers is a data-driven prior for
the WKB model's own predicted reflectance phase, rather than two
independent, unconnected efforts.

**2. PHOTONICS' own queued WKB/adiabatic boundary-reflectance analytic
model (Iteration-51 queue item 4, twice-queued and twice dropped) —
promote it now that a seventh same-instrument-class attempt is barred.**
Zero FDTD, engages a seat's own charter physics directly rather than
re-verifying statistics for a sixth time, and is the only queued item that
could *explain* the ~2.5° family rather than merely bound or fail to
detect it. My own §2d finding (near-total cross-config correlation) is
independent evidence *for* a shared-geometry-driven mechanism (consistent
with a boundary-reflectance effect that doesn't depend on `ABSORB` depth),
which should be disclosed to whichever seat builds this model as
supporting context, not treated as this review's private finding.

**3. Fold this review's three now-quantified facts into the permanent
record before either of the above starts, and correct the minor
arithmetic error (both cheap, R4/R7-shaped housekeeping).** Add lag-1
autocorrelation (~0.93) and cross-config correlation (~0.997–0.9995) as
committed, reproducible numbers (not prose assertions) to
`fit_and_calibrate.py`'s own output next time it or a descendant script
runs; correct `phase4_results.md`'s "72 cell combinations" to the true
36; and record R7's own first-application lesson precisely: a
conditioning-only bound predicted the *direction* of the circular-shift
leg's extra severity but not its *magnitude*, and this review shows the
magnitude is explained by a specific, checkable structural fact
(autocorrelation, not shift-pairing) — worth stating as a sharpened
corollary to R7 for the next seat that builds a structure-preserving
null on different data.

---

## Reproduction

Every number above was produced by importing `desk_check_pricing.py` and
`fit_and_calibrate.py` directly (no re-derivation of formulas) and calling
their own committed functions (`fit_real_pair`, `per_config_residuals`,
`circular_shift`, `sign_flip_9col_surrogates`, `build_X9_X8`) from a
scratch driver script, plus one unmodified end-to-end re-run of
`fit_and_calibrate.py` diffed programmatically against the committed
`fit_and_calibrate_results.json`. No number in this review was hand-typed
from another document.
