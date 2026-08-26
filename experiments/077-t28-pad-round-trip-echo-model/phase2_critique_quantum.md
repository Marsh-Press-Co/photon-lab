# PHASE 2 — CRITIQUE · QUANTUM OPTICS · Panel Iteration 54 · exp-077

*Blind critique, independent of other seats. Charter: non-classical
absorption, state-dependent or coherent interactions; mechanisms enter the
bench only as effective classical parameters or Red Team strikes them.
This proposal's mechanism (a coherent boundary echo weighted by a complex
`r(theta;ABSORB)`) is exactly this seat's expressibility contract already
satisfied — the physics under test is the classical-coherent limit my own
charter treats as in-scope.*

---

## 1. Steel-man (≤150 words)

exp-076's proof that `PAD` is lossless vacuum leaves exactly one physically
permitted mechanism class for `PAIR_PAD`'s dominant signal: coherent
propagation-phase interference. This proposal is the cleanest available test
of it — reusing exp-075's own already passivity-gated coherent-echo model
(`G-LOSSLESS`, `G-N1`, `G-PASSIVITY`, all re-verified here, worst
`|r|=0.006423`) completely unchanged, refit against the one pair `(C40,G40)`
where `ABSORB=40` is bit-identical for both configs, so `r(theta;40)` is
provably the same complex reflection amplitude for both curves — isolating
exactly the round-trip-distance axis a coherent-echo mechanism predicts
should matter, at zero new FDTD cost. The staged period-window widening
(narrow→`[1,15]°`→cross-checked stable to `[1,180]°`) is applied
symmetrically to both curves before either verdict is read, not tuned
toward REFUTE. The resulting REFUTE (`rel_dev=1.88`, `r²=0.044`) is a
genuine, disciplined negative result for the one mechanism class this
proposal — and my own charter — can actually engage here.

## 2. Sharpest attack (≤150 words)

`_free_period_search` maximizes R² over a 2800-point grid per curve
(`pad_round_trip_model.py` lines 188–221, calling `run69._free_period_search`
at line 206) with no look-elsewhere or ground-truth-recovery control anywhere
in this cycle — the exact gap R5/R6/R8 exist to close, and one I have
direct authorship standing on (`G0-e`, exp-076). I computed it. Two
independent white-noise 31-point curves on this identical grid/window
(20,000 Monte Carlo trials): `P(rel_dev>1.00)=0.214`, and the observed
`1.8798` sits at only the 86.9th percentile of that null — not overwhelming
as a bare number. But the same null shows `P(R²≥0.70)=0/40,000` draws (max
`0.64`) — both the real (`R²=0.8165`) and model (`R²=0.8592`) fits are far
beyond noise's reach, so neither curve's periodicity is a grid-search
artifact. A bootstrap recovery check — resample the real curve's own
residuals (std `6.50e-4`) onto its own best fit, 20,000 trials — recovers
`P*=4.61°` to `rel_dev≤0.30` every single time and never approaches
`rel_dev>1.0`, let alone the model's `13.28°`. The control is missing from
the record but, run, it CONFIRMS REFUTE rather than undermining it.

## 3. Independent verification performed (this critique's own computation)

Two checks, both run against the actual committed `_free_period_search`
machinery (imported, not reimplemented — `experiments/069-.../run.py` lines
308–337), on the real 31-point, `[36°,42°]`, 0.2° grid:

**(a) Pure-noise null (does the grid search manufacture high R² / small
rel_dev from nothing?).** 20,000 trials, two independent
`N(0,1)` 31-point curves each, `_free_period_search(lo=1°, hi=15°,
n_grid=2800)` — the exact window/grid `PAIR_PAD`'s "chosen" stage uses:

| Quantity | Null result | Observed (`PAIR_PAD`) |
|---|---|---|
| `P(rel_dev > 1.00)` | 0.214 | rel_dev=1.8798 (86.9th pct of null) |
| `P(R² ≥ 0.70)` | 0/40,000 (max 0.64) | real R²=0.8165, model R²=0.8592 |
| `P(shape r² ≤ 0.05)` | 0.778 | r²=0.0444 (75.0th pct of null) |

Reading: **rel_dev and shape-r² alone, taken as isolated numbers, are
weaker evidence than the proposal's prose implies** — noise this size
clears the REFUTE bar on Test A 21% of the time and on Test B 78% of the
time, so "REFUTE" by itself is not automatically decisive. But the R² each
curve *individually* achieves is essentially unreachable by chance (p≈0.0003
for R²≥0.56, the weakest value in the whole table) — both curves carry real,
non-noise periodic structure. This is the correct rebuttal to a naive
"maybe it's all noise" reading, and the proposal never states it.

**(b) Ground-truth recovery (is the REFUTE gap explainable by estimation
noise around a shared true period?).** Fit the real `PAIR_PAD` curve at its
own reported `P*=4.6113°` (R²=0.8165), take that fitted sinusoid as ground
truth, bootstrap-resample its own residuals onto it 20,000 times, and refit
each resample with the identical `_free_period_search`:

- Recovered `P*` median = `4.6113°` (exact); `P(rel_dev(vs. true) ≤ 0.30)
  = 1.0000`; `P(rel_dev > 1.00) = 0`; `P(within 10% of the model's own
  13.2794°) = 0`. 5th/95th percentile band: `4.38°`–`4.85°`.

The real data's own period estimate is not noise-fragile — under its own
realistic residual noise it never wanders anywhere near the model's 13.28°.
**The 1.88 gap is a genuine model-vs-data mismatch, not sampling variance
dressed up as a mechanism failure.**

**Net answer to the question posed**: a look-elsewhere/null-calibration
control was needed to make this REFUTE trustworthy by this program's own
R5/R6/R8 standard — the raw numbers alone (1.88, nearly double the REFUTE
line; 0.044, near-zero) are suggestive but, per check (a), not by themselves
outside what noise alone occasionally produces on Test A/B individually.
Running the actual control (checks a+b together) closes that gap decisively
in REFUTE's favor. The omission is a real process gap under this program's
own standing rules, not a substantive defect in the conclusion.

## 4. Verdict: **support-with-changes**

The physics conclusion (REFUTE for `PAIR_PAD`, INCONCLUSIVE for
`PAIR_ABSORB40`) is correct and now independently secured by both a
pure-noise calibration and a ground-truth-recovery bootstrap, neither of
which appears anywhere in `phase1_proposal.md` or
`pad_round_trip_model.py`. Per this program's own R8 precedent (Iteration
52, exp-075: an unverified robustness argument may not be filed as
non-blocking when a named, affordable check exists and is not run — even
when, independently checked later, the underlying conclusion turns out
correct), this cycle should not close on the REFUTE headline without this
control appearing in the committed record. The fix is cheap (the two checks
above run in under two minutes combined, zero new FDTD) and does not change
a single frozen prediction.

**Required change**: add a null-calibration appendix to `pad_round_trip_
model.py` — (a) a pure-noise Monte-Carlo null for Test A/B on this exact
grid/window, and (b) a bootstrap ground-truth-recovery check on the real
`PAIR_PAD` curve's own best fit — before Phase 3 synthesis treats the
REFUTE verdict as fully closed. This mirrors `G0-e`'s own spirit (exp-076,
my own prior cycle) one level applied to a period-comparison test rather
than a fitted significance-tested coefficient; I do not think it rises to
a full new numbered house rule (R5/R6 already cover the *dense-search* and
*carrier-conditioned-significance* cases respectively, and this is neither
exactly), but the specific check should be run and cited, not left as an
unverified robustness assumption a second time in three cycles.

## 5. Single change that would flip this to full support

Add the two checks in §3 (or equivalent) to the committed `pad_round_trip_
model.py`/`pad_round_trip_results.json`, with their numeric output stated
in `phase1_proposal.md` §5 alongside the existing bands — no change to any
frozen prediction, verdict, or band is needed, only the missing control
itself. Absent that addition, I hold at support-with-changes rather than
support, matching R8's own standard: the check must actually be run and
recorded, not merely argued to be unnecessary (which is the same shape of
gap that fired Checkpoint criterion 4 one cycle ago, in this exact
sub-thread).
