# PHASE 4 — RESULTS · Panel Iteration 51 · exp-074
## Official run of the 9-column fit + null-calibration test

*Official Phase-4 run: `fit_and_calibrate.py`, unmodified, executed after
Phase 3's git-frozen predictions (commit `3aaae38`). Deterministic — fixed
seeds throughout (`SIGN_FLIP_SEED=74051`, `CAL_SEED=74052`, unchanged from
Phase 3); this run reproduces, bit-for-bit on every reported quantity
except `elapsed_s`, the development run disclosed and bounded in
`phase3_synthesis.md` §4. Elapsed: 24.81s (dev run: 25.22s), single-core,
zero FDTD, zero `lab/` diff. Full data: `fit_and_calibrate_results.json`.*

---

## Bottom line

**Combined Verdict: `HALT_NULL_MISCALIBRATED_9COL`.** Both frozen
predictions confirmed, with margin.

**Primary prediction confirmed.** The 9-column null-calibration gate
fails at **every one of 72 cell combinations** (3 free pairs × 24 cells:
3 sigmas × 3 alphas for the i.i.d. leg, plus 3 alphas for the
circular-shift leg). The i.i.d. leg's worst inflation is **8.7×–11.2×**
nominal at α=0.01 — WORSE than exp-073's own 5-column finding (5.4×
worst, at the same α) — exactly as predicted from the lower `lev9_Rq`
(0.586–0.596 vs. exp-073's 0.79–0.80).

**Secondary prediction confirmed, dramatically.** The circular-shift
(genuinely order-preserving) leg fails far worse than the i.i.d. leg at
every pair and every α:

| Pair | i.i.d. worst ×nominal (α=0.01) | circular-shift ×nominal (α=0.01) |
|---|---|---|
| C40–C60 | 11.20× | **38.90×** |
| C60–C70 | 10.30× | **46.10×** |
| C70–C80 | 8.70× | **44.10×** |

At `α=0.10` the circular-shift leg still rejects **58–65%** of pure-noise
draws against a nominal 10% — not a marginal failure, a near-coin-flip
false-positive rate. **This is the first test in this sub-thread's
five-cycle history to genuinely expose θ-correlated real-residual
structure**, closing the exact gap exp-073's own Phase-5 erratum named:
its own pooled/flattened "residual-structure" leg was, by construction,
statistically indistinguishable from its own i.i.d. leg (`r=0.907`); this
cycle's circular-shift leg is **not** indistinguishable from its own
i.i.d. leg — it is 3.5×–5.9× worse at every α, meaning the real
per-config residuals carry genuine, exploitable θ-adjacent correlation
structure that an i.i.d.-of-any-marginal-shape null cannot represent.

**No pair's `R_q`-within-the-two-tone-fit significance was ever scored.**
`scored={}`; `combined_verdict` is the named `HALT` branch, computed
before any p-value would have been trusted.

---

## The real fit (for the record — not gating, since calibration failed first)

| Pair | `R_q9` | `SE9` (naive OLS) | `z9` | `lev9_Rq` | `cond9` |
|---|---|---|---|---|---|
| C40–C60 | +0.02202 | 0.02612 | 0.84 | 0.5858 | 529.4 |
| C60–C70 | −0.01572 | 0.00312 | **5.03** | 0.5932 | 482.4 |
| C70–C80 | −0.00201 | 0.00123 | 1.63 | 0.5960 | 478.4 |
| C40–C80 | +0.00744 | 0.02158 | 0.34 | 0.5883 | 524.5 |

These are the same numbers THERMODYNAMICS' Phase-2 attack and Red Team's
independent re-derivation found (matched to 3 decimals in Phase 2). This
run does not change or re-litigate them — it answers the question Phase 2
raised: **is `z9=5.03` at C60–C70 real, or an artifact of `cond9≈480`
letting the two-tone fit's residual variance shrink faster than a naive
extrapolation predicts?** The answer, from this run: **we still do not
know**, and — this is the substantive finding — **we now know why we
cannot know with this instrument**: the null construction that would
answer it is itself badly miscalibrated, on both a standard (i.i.d.) and
a harder, more realistic (θ-correlated real-residual) noise assumption.
`z9=5.03`'s own naive OLS SE cannot be trusted as a significance
statement in either direction.

---

## What this means for R7 (adopted this cycle, `phase3_synthesis.md` §2)

This is R7 working exactly as designed, on its very first application:
the design-only `lev9_Rq≈0.59` pricing (this cycle's own Phase 1) already
predicted a worse calibration failure than exp-073's 5-column case; this
run **directly measures** that failure rather than merely inferring it —
and finds it is worse again once real, order-preserving residual
structure (rather than i.i.d. noise of any shape) is used to test it.
**A conditioning-only bound would have been silent on the circular-shift
leg's own 5× additional degradation** — R7's own point, confirmed on its
first use: pricing an un-fit design's conditioning is necessary, not
sufficient; only the calibration test actually run here reveals how much
worse the realistic-noise case is than the idealized one.

---

## Contamination / pre-registration note

`fit_and_calibrate.py`'s core formulas (`build_X9_X8`, `fit_real_pair`)
are extensions of `desk_check_pricing.py`'s own already-CHECK0-verified
basis, applied to real `delta_ab` data most of which was already visible
in Phase 2 (THERMODYNAMICS' and Red Team's own attacks independently
computed `z9` before this cycle's Phase 3 was written). Per this
program's own contamination-disclosure convention (exp-072/073): the
**calibration gate's own pass/fail thresholds were fixed before any
calibration Monte Carlo was run** (the tolerance band `α±3√(α(1−α)/K)` is
a closed-form statistical identity, not tuned to this data), and the
**qualitative primary prediction (HALT, and worse than exp-073's 5-column
case) was stated and justified analytically in `phase3_synthesis.md`
BEFORE this script's calibration routine was ever executed** — the
`lev9_Rq` numbers that justify it are a pure design-time computation
(`fit_real_pair`, no calibration Monte Carlo involved) already disclosed
in Phase 3. No threshold here was set with reference to the calibration
run's own outcome.

---

## Idealizations, unchanged from `NOTES.md`/`phase3_synthesis.md`

No idealization changes. Both predicted failure directions were
confirmed; no idealization was found wrong or in need of revision by this
run.
