# PHASE 5 — QUANTUM OPTICS REVIEW · Panel Iteration 85 (exp-108)

Fresh context, blind to the other six seats' own Phase-5 reviews. Read
PANEL.md in full, LOGBOOK.md in full (RULED OUT R1–R25, ESTABLISHED, LIVE
THREADS including T28/T9/T11), PLAN.md's Vision/Current-state, and this
cycle's complete record (`phase1_proposal.md`, all five
`phase2_critique_*.md`, `phase2_redteam_audit.md`, `NOTES.md`, `run.py`,
`chunk_runner.py`, `analyze.py`, `reclassify_106.py`, `results.json`,
`analyze_output.json`, `run_output.txt`, the patch diff to
`experiments/106-.../run.py`, and `lab/validation/run_all.py`'s new
`stage26_chunked_run_identity()`). All headline numbers below were
independently re-derived from source, not trusted from any prior
document's restatement — including my own Phase-2 critique's.

## 1. Independent reproduction (zero-FDTD, all three named scripts re-run fresh)

The pickled field captures from this cycle's own 6 real `Sim.run()`
calls are still present in this session's scratch directory
(`r{156,312}_{empty,hollow,peccored}_done.pkl`), so every zero-FDTD
script was actually re-executed against them, not merely read:

- `python3 reclassify_106.py` → reproduces bit-for-bit: `p_abs_frac_diff_156
  =0.12305795332466973`, `_312=0.17962207739772926`,
  `shape_ratio_fixedabs=18.228333623646076`, `trusted=False`,
  `noise_dominated=False`, OLD classification unchanged, NEW
  classification contains `"THREE-WAY-AMBIGUOUS"` — exact match to
  `run_output.txt`/`results.json['tier0_item1']`.
- `python3 analyze.py` → reproduces `gate_p0.pass_=True` (both r),
  `reproduction_precondition.pass_=True` (both r), `item_i verdict=CONFIRM`
  (both r), `item_ii residual_std=2.8972e-06`(r156)/`2.1022e-06`(r312),
  `item_iii frac_unresolved=0.1827`(r156)/`0.2525`(r312), `closure`
  hollow/peccored = `0.000196`/`0.000160`(r156), `0.000563`/`0.000581`
  (r312) — exact match to `run_output.txt`/`analyze_output.json`.
- `python3 lab/validation/run_all.py --only 26` → `2/2` PASS, positive
  control `max|diff|=0.000e+00`, negative control relative deviation
  `2.000` — exact match. Full standard suite (`--only 12346789`):
  `41/41` PASS.
- `git show` on the commit's own diff to `experiments/106-.../run.py`
  confirms `classify_shape_ratio_fixedabs()` is a genuine standalone
  function (Attack 1's fix, function-extracted per Red Team's option
  (a)), called both by the file's own inline site and imported directly
  by `reclassify_106.py` — no duplicated logic, matching R4's "one
  number, one name" discipline. `results.json`/`NOTES.md` inside
  `experiments/106-.../` are byte-unchanged by this commit (confirmed by
  `git show --stat`) — see §4 for a minor prose-accuracy note on this.
- `wall_times_s` in `results.json` sums exactly to the disclosed
  128.5 min (738.0s=12.3min at r=156; 6974.0s=116.23min at r=312).
- MATERIALS' T9-anchor correction independently re-derived:
  `2.96857e-5 / 1.56e-6 = 19.03`, `2.46843e-5 / 1.56e-6 = 15.82` — the
  `19.0×/15.8×` figure this cycle's synthesis restores is exact, not
  merely accepted.

**Constraint-3/T1 structural check (independent grep, not accepted from
the proposal or Red Team's own claim):** `grep -rniE
"coherent|quantum|photon(?!ics)|superposition|entangle|wavefunction|
nonclassical" *.py *.md *.txt` across this cycle's own directory returns
only the seat-name label "QUANTUM" (as a critique-author reference) and
one explicit negation ("Nothing non-classical is smuggled anywhere," my
own Phase-2 critique). Read `lab/sections.py` directly:
`angular_scattered_pattern()`/`widths()` both compute standard
time-averaged Poynting flux (`<Sx>=-1/2·Re{Ez·conj(Hy)}`) from
steady-state phasors extracted via quadrature capture — the same
construction every other channel in this program uses. **T1 is
correctly N/A throughout; zero non-classical content is expressible
anywhere in this cycle's `run.py`/`chunk_runner.py`/`analyze.py`,
confirmed structurally.**

## 2. My own Phase-2 attack, and whether the unified fix genuinely closes it

**My attack (Phase 2):** the six margins `{24,32,40,48,57,65}×k` sample
one deterministic field snapshot at increasing radius, not exchangeable
draws; a smooth near-to-far-field convergence trend inflates raw `std`
even with zero placement randomness, conflating convergence *bias* with
noise-floor content. Flip condition: detect monotonicity, and if
present, replace raw std with a residual-from-fit (`1/margin` detrend).

**Red Team's unified fix (§3 of `phase2_redteam_audit.md`):** combined my
finding with EM's box-independence attack into one root cause (box
radius treated as an iid nuisance parameter in two new, non-conserved
quantities) and mandated, for item ii specifically: fit `Δ(margin) = A +
B/margin`, report whether the sequence is smooth (monotonic or
`R²≥0.90`), and — "if it is" — report the residual-from-fit std as the
genuine floor, not the raw std.

**Re-deriving `residual_std` myself, from `analyze_output.json`'s raw
`delta_values`/`margins`, by an independent implementation (normal
equations, not `numpy.linalg.lstsq`, not importing `run.py`):**

```
r=156: delta_values = [-3.2254e-5, -2.9686e-5, -2.1943e-5, -1.8651e-5, -1.9736e-5, -2.4697e-5]
       A=-1.29692e-5  B=-4.55907e-4  R²=0.66537  is_monotonic=False
       residual_std (ddof=0) = 2.89716e-6   <- matches reported 2.897e-6
       raw std (ddof=0, no detrend)         = 5.00833e-6

r=312: delta_values = [-2.8692e-5, -2.4684e-5, -2.9952e-5, -2.6736e-5, -2.4369e-5, -2.8845e-5]
       A=-2.63552e-5  B=-3.39405e-5  R²=0.02050  is_monotonic=False
       residual_std (ddof=0) = 2.10220e-6   <- matches reported 2.102e-6
       raw std (ddof=0, no detrend)         = 2.12409e-6
```

**`residual_std` reproduces the reported 2.897×10⁻⁶ (r=156) and
2.102×10⁻⁶ (r=312) exactly, from an independently-written fit, confirmed
bit-for-bit.** The mechanics of the fix are correctly implemented and
correctly reproduce. So far, CONFIRM.

**But the fix's own stated precondition is not actually wired into
item ii's classification, and this is a real, if non-load-bearing,
gap.** `run.py::linear_fit_1_over_margin()` computes `is_monotonic` and
`smooth` (`is_monotonic OR R²≥0.90`) for every fit — and these two
fields ARE load-bearing for item i's REFUTE branch
(`classify_item_i`'s `smooth_run_found` check). But
`classify_item_ii()` (`run.py:187-193`) uses `fit["residual_std"]`
**unconditionally** — it never reads `fit["smooth"]`, `fit["r_squared"]`,
or `fit["is_monotonic"]` at all. By this same document's own R²≥0.90
smoothness bar, **neither r=156 (R²=0.665, not monotonic) nor r=312
(R²=0.021, not monotonic) actually qualifies as "smooth."** At r=312 the
fit explains essentially no variance (2%) — detrending there is barely
distinguishable from fitting two parameters to six noise points and
removing a small amount of noise-driven variance by construction
(residual_std 2.102e-6 vs. raw 2.124e-6, a ~1% reduction, consistent with
overfitting rather than genuine bias removal). At r=156 a real, if
imperfect, trend does appear present (R²=0.665, a substantial fraction
of variance, though not monotonic — the sequence dips then partially
recovers) and detrending there materially matters (raw 5.01e-6 →
residual 2.90e-6, a 42% reduction) — but this is exactly the regime
Red Team's own text conditioned the swap on ("if it is [smooth]"), and
by the file's own R² bar it isn't. **The Result section (`NOTES.md`)
reports both r's `residual_std` uniformly as "the genuine floor," with
no mention of `R²`/`smooth` for item ii at either r** — those fields
are computed and persisted in `analyze_output.json` but never narrated
(the same shape LOGBOOK's own R21 rule names: a persisted field's
headline finding not stated in Result prose — not itself a fresh R21
firing, since this is a founding-shaped instance on a new field, but the
identical pattern).

**Is this outcome-reversing? No.** I independently checked: the
un-detrended raw std also clears item ii's own CONFIRM bar at both r
(r=156: 5.008e-6 vs. 1.485e-5 bar, 2.97× margin, still CONFIRM; r=312:
2.124e-6 vs. 1.234e-5 bar, 5.81× margin, essentially identical to the
detrended 5.87× reading). So the CONFIRM verdict for item ii would have
survived even with the raw std my own Phase-2 attack objected to — the
detrending changes the reported margin (materially at r=156, negligibly
at r=312) but not the classification. **The attack is closed in the
sense that matters most (the correct, defensible statistic — a genuine
least-squares detrend, independently reproduced — now drives the
headline number, and I confirm it is not merely re-labeled raw std) but
not fully closed in the sense my own flip condition asked for: the fix
never actually checks whether detrending is *justified* by a
demonstrated smooth trend before trusting the result as "the genuine
floor," at either r, by this same file's own smoothness standard.**

**A second, related, independently-found implementation gap (item i,
not part of my own original attack but the same instrument family):**
`classify_item_i`'s CONFIRM branch and NOTES.md's own Predictions/Result
text both describe the test as restricted to "every one of the 48 bins
that clears the item-ii absolute floor" — but I confirmed, by reading
`run.py` and `analyze.py` directly, that **no floor-clearing mask is
ever computed or applied anywhere in this cycle's code.**
`lab/sections.py::angular_scattered_pattern()` has no floor concept at
all (confirmed by reading its source), and `analyze.py::analyze_r()`
passes `pattern_peccored[m]`/`pattern_delta[m]` straight from the raw
function output into `R.classify_item_i()` with no masking step. The
function's own docstring even says "floor-cleared mask applied
upstream" — describing a step that does not exist upstream. **This does
not reverse the CONFIRM verdict** (testing all 48 bins is a strict
superset of testing only a floor-cleared subset; since all 48 passed,
any subset trivially would too — if anything this is a stronger, not
weaker, test than claimed), but the Result prose describes a
computation that was never executed, the same "claimed scope vs. actual
source" shape R18 exists to catch (non-firing here: this is this
instrument's own founding cycle, and the gap is not load-bearing to any
scored verdict).

## 3. Other checks

- **`closure` (mandatory fix 5, EM's ask):** re-verified all four cells
  (`0.0196%`/`0.0563%` hollow, `0.0160%`/`0.0581%` PEC-cored) against
  `analyze.py::closure_for()`'s own formula — matches, comfortably
  inside the 0.1% CONFIRM band, consistent with exp-106's own 0.02–0.06%
  precedent.
- **R23 live-fire check:** re-ran `run.py --predictions-only` and
  `grep -in disclaimer` across all four executable files myself — 4 hits
  in `run.py` (constant + 3 uses), 0 in `chunk_runner.py`/`analyze.py`/
  `reclassify_106.py`, matching the claim exactly.
- **Minor prose-accuracy note, not load-bearing:** `NOTES.md`'s
  Idealizations claims exp-106's own historical `results.json`/`NOTES.md`
  "are annotated, not overwritten." I confirmed via `git show --stat`
  and direct grep that `results.json` is correctly **unchanged**
  (true half of the claim), but **`NOTES.md` in
  `experiments/106-.../` carries zero reference to exp-108, Iteration 85,
  or the reclassification** anywhere — only `run.py` itself was
  annotated (three comment blocks, confirmed). "Annotated, not
  overwritten" is accurate for `run.py`, true-by-omission for
  `results.json` (correctly never touched), but false for `NOTES.md`
  specifically, which was neither touched nor annotated. Cosmetic; does
  not affect any measurement, gate, or verdict — flagged per this
  program's own R4/R9 "claimed figure/scope must match source" discipline.

## 4. Verdict

**CONFIRM-WITH-GAPS.**

Every headline number I attempted to independently reproduce did
reproduce — `reclassify_106.py`, `analyze.py`, and `stage26` were all
re-executed fresh against the cycle's own retained field captures, not
merely read, and all outputs matched `results.json`/`run_output.txt`/
`analyze_output.json` exactly, including my own from-scratch re-fit of
`residual_std` (2.897×10⁻⁶/2.102×10⁻⁶, both r). T1/constraint-3 is
correctly N/A throughout; the classical Poynting-flux construction is
confirmed by direct source read; zero non-classical language appears
anywhere except as a seat-name label. My own Phase-2 attack is
**substantively but not completely** closed: the unified fix replaced
raw std with a genuinely independent, correctly-computed detrended
statistic (a real improvement, and I confirm the detrending is not
window-dressing — it materially changes the r=156 reading), but
`classify_item_ii()` applies that detrended statistic unconditionally,
never checking the `smooth`/`R²` precondition Red Team's own fix text
invoked to justify trusting it — a precondition that, by this file's own
0.90 bar, is not met at either r. Combined with the separately-found
"floor-cleared" filtering that was described but never implemented for
item i, this is a real gap in rigor, though non-load-bearing to any
verdict scored this cycle (both CONFIRM calls survive under the
stricter, undetrended/unfiltered alternative I checked by hand).

**Single most important finding:** `classify_item_ii()` reports
`residual_std` (independently re-derived and confirmed exact: 2.897e-6/
2.102e-6) as the unconditional "genuine floor" without ever checking the
`smooth`/`R²≥0.90` precondition the unified EM+QUANTUM fix's own text
required before trusting a detrend over raw std — and by that precise
bar, neither r=156 (R²=0.665) nor r=312 (R²=0.021, essentially no real
trend) actually qualifies as smooth, though the CONFIRM verdict survives
under the un-detrended raw std at both r regardless (2.97×/5.81×
margins vs. 1.48e-5/1.23e-5 bars).
