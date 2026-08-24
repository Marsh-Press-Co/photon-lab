# PHASE 4 — RESULTS · exp-066 · Panel Iteration 43

Run 2026-08-24. 39 new FDTD calls, 3.7 min wall-clock (well under the 30-min
hard stop). Full data: `results.json`. Raw log: this file's own tables below
are produced directly from `results.json`, not hand-typed (R4).

## Gate P-066-G1 — PASSED, 18/18 bit-exact

All 18 new STEPS=1400 cells (`{36,37,39}°×{±}×{450,600,750}nm`) reproduce
exp-041's committed `results.json::block_main` `C_empty` values to
**exactly** `Δ = +0.000e+00` — float64 bit-identical, every cell. exp-065's
own G-1 anchor is now extended from 12/30 to **30/30** of exp-041's Block
MAIN cells. This is the same harness-reproducibility result exp-065's own
C40 cross-check already demonstrated at one cell; here demonstrated at all
18 previously-unaudited cells.

## Headline: P-066-1 through P-066-4 all CONFIRMED

| ID | Result | Verdict |
|---|---|---|
| P-066-1 | median `\|ΔC(2800−1400)\|` = **0.005767** (band [0.001,0.010]), max = 0.009575 | CONFIRMED |
| P-066-2 | **3 of 18** cells sign-flip between STEPS=1400 and 2800 | CONFIRMED |
| P-066-3a | 40°/750nm: `\|ΔC(4200−2800)\|/\|ΔC(2800−1400)\|` = **0.0098%** (bar ≤1%) | CONFIRMED (750nm settled by 2800) |
| P-066-3b | 37°/600nm: same ratio = **0.00072%** (bar ≤1%) | CONFIRMED (settled by 2800, generalizes across θ) |
| P-066-4 | settled-data fit: sign_agree **30/30** (was 27/30), r²(c*) **0.8271** (was 0.7852, Δ=+0.042, within ±0.10 band) | CONFIRMED (fit quality recovered — **no mechanism claim**, per mandatory fix C) |

P-066-3a/3b are the single most decisive numbers in this run: both
convergence ratios are **~100–1000× tighter** than their own 1%/5%
CONFIRM/REFUTE bar, at the two cells specifically chosen to test
generalization along λ (750nm, the residual-concentrated wavelength) and θ
(37°, an interior angle none of exp-065's own construction had tested).
STEPS=2800 is settled at both.

## Closure summary — the concrete answer to "how many citations are affected"

All **36** mandate-scope cells (`±35°/36°/37°/38°/39°/40°×{450,600,750}nm`)
are now covered at both STEPS=1400 and STEPS=2800 — 18 new FDTD calls
(this cycle), 12 already-settled cells cited from exp-065's own committed
data (±38°/±40°, mandatory fix A), and 6 fallback-only cells (±35°) cited
the same way.

**GATE_HARD (0.001) pass/fail count: 31/36 fail at STEPS=1400 → 34/36 fail
at STEPS=2800.** The settling correction makes the instrument's own
per-angle floor look **worse**, not better, over this cell set — the
opposite of what an "unsettled = noisy/inflated" prior might suggest.

**5 of 36 cells flip GATE_HARD bucket; 4 of the 5 flip PASS→FAIL, only 1
flips FAIL→PASS:**

| θ | λ | C(1400) | C(2800) | 1400 | 2800 |
|---|---|---|---|---|---|
| −39° | 450nm | −0.000030 | +0.003375 | PASS | **FAIL** |
| +37° | 450nm | −0.000935 | −0.001301 | PASS | **FAIL** |
| +39° | 450nm | +0.000456 | +0.004052 | PASS | **FAIL** |
| −35° | 750nm | −0.000948 | +0.005516 | PASS | **FAIL** |
| +38° | 600nm | −0.007305 | −0.000791 | **FAIL** | PASS |

Three of the four newly-failing cells were 450nm-side near-zero-crossing
points at STEPS=1400 (magnitudes 0.00003–0.00094, well inside the
GATE_HARD floor) that turn out to be genuinely larger once settled
(0.0013–0.0040) — the STEPS=1400 transient was landing coincidentally near
a sign-change of the oscillation at exactly those cells, not because the
instrument floor was actually that tight there. The single FAIL→PASS flip
(+38°/600nm) is the cell already reported in exp-065's own headline (T27's
opening finding).

## Fringe-fit refit (P-066-4) — full detail, strictly statistical

Refitting exp-042's own `edge_diffraction_c_empty_corrected` against the
full 30-row settled Block MAIN dataset (12 already-settled ±38°/±40° cells
+ 18 new cells, all at STEPS=2800):

| | STEPS=1400 (original, exp-042) | STEPS≥2800 (this cycle) |
|---|---|---|
| sign_agree | 27/30 | **30/30** |
| r²(c=1) | 0.6570 | 0.8052 |
| c* | 1.6196 | 0.8712 |
| r²(c*) | 0.7852 | **0.8271** |

Every metric improves at settled STEPS — sign agreement goes from 27/30 to
a clean 30/30, and the best-fit R² rises by 0.042 (well inside the ±0.10
CONFIRM band). **Per mandatory fix C, this is reported and should be cited
ONLY as a statement about fit quality: the propagator's correlation with
the corrected data did not degrade, and in fact improved.** It is
**explicitly not** evidence that the underlying mechanism is genuine
coherent edge-diffraction rather than settling-transient content
correlating with the same geometric clock (`A·cosθ`) — Block MINI's
period-match test (P-VIS42-10, exp-065) remains UNDECIDED, unchanged by
this cycle, and the forward tripwire (`design_geometry.
FRINGE_FIT_STATISTICAL_ONLY_NOTE`) governs any future citation of these
numbers.

The c* shift (1.62→0.87) is itself notable and disclosed without
interpretation: the settled data's own amplitude sits closer to the
propagator's raw (unscaled) prediction than the STEPS=1400 data did —
consistent with (not proof of) the settling artifact having previously
been inflating the measured amplitude relative to the diffraction model's
own un-rescaled prediction, but this cycle does not adjudicate that
reading.

## Downstream citation scope (per the mandate's own "scope exactly how
many downstream citations are affected")

**AFFECTED-NUMERIC, load-bearing, now closeable:**
- `experiments/042-t21-magnitude-bridge/NOTES.md:11,338` — T21's own
  edge-diffraction magnitude fit. This cycle's P-066-4 refit is the
  concrete numeric update this citation needs; exp-042's own committed
  `r2_cstar=0.7852421354715854`/`c_star=1.6196430704378861` should be
  read alongside this cycle's settled-data `r2_cstar=0.8271`/`c_star=
  0.8712` — not superseding exp-042's own committed record (T10 convention:
  flag, don't silently rewrite), but no longer citable as "unsettled."

**AFFECTED-DISCLOSURE, now closeable:**
- LOGBOOK.md's T16, T20, T21, T24, T27 entries — each may now cite this
  cycle's closure rather than an open gap; `lab/caveat_lint_config.json`'s
  `exp065-steps1400-unsettled-plane-channel` entry should be updated (a
  Phase-5/close-of-cycle task, not this Phase-4 file's own scope) to
  reflect that Block MAIN's own 30 rows are no longer "unsettled," while
  the four interior `FALLBACK_ANGLES` and Block ARTICLE's article-present
  legs (PLAN.md item #2) remain open.
- `experiments/046-.../NOTES.md:495` — same disposition.
- exp-065's own `P-VIS42-6`/`P-VIS42-7` — **NOT closed by this cycle.**
  Those score Block ARTICLE (τ=0.0065 article present, N9 `FALLBACK_ANGLES`
  aggregate), a structurally different measurement (aggregate N9, article
  present) from this cycle's own empty-scene Block MAIN cells. PLAN.md item
  #2's own scope, unchanged.

**UNAFFECTED:** MATERIALS' `REALIZABILITY_MEMO.md` D_req figure — confirmed
this cycle only in the sense that its reachability gap (mandatory fix D) is
closed, not that its own number moved; the memo's UNOBTANIUM-WITH-
PARAMETERS verdict rests on grounds independent of this channel's precise
value (RSA/TPA gaps), unchanged.

## Bench trust suite

Reverified before (implicitly, via the pre-Phase-1 pre-flight check) and
after this run: `python3 lab/validation/run_all.py --only
12346789,10,11,18,19,20,21,22,23,24` — see SESSION_LOG.md for the exact
pass count. Only `lab/caveat_lint_config.json` (data registry, one entry
widened) touched among `lab/` files; zero engine code diff
(`run.py`'s own `_lab_diff_excluding_registry` assertion passed live).
