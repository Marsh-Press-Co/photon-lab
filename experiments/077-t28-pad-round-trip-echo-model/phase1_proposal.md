# PHASE 1 — PROPOSE · Panel Iteration 54 · exp-077
## The `PAD` round-trip-distance refit of exp-075's single-wall echo model: the only mechanism class still permitted for T28's dominant PAIR_PAD signal (T28)

*Fresh sub-agent, VISION SCIENCE charter (PANEL.md seat: human perceptual
limits — pins numeric thresholds before any run scores against them), lead
by rotation. Executes LOGBOOK.md's Iteration-53 (exp-076) Tier-0 #1 queue
item, EM's own #1 pick seconded by THERMO. Per house precedent (Iteration
44/52), the rotation lead formalizes the queue's own #1 regardless of
whose charter it fits most naturally; my own seat's angle (is any of this
perceptually meaningful) is engaged briefly in §3 and found not to add a
new constraint — the substantive content is EM/PHOTONICS field-and-
boundary physics, executed as the queue directs.*

---

## 0. What this is, and what it is not

**ZERO new FDTD calls.** Every number below comes from `pad_round_trip_
model.py`, this directory, which imports (never reimplements) exp-075's
already-vetted transfer-matrix/gate machinery (`boundary_reflectance.py`),
exp-065's geometry (`design_geometry.py::CONFIGS`), exp-069's period-fit
methodology (`run.py::_free_period_search`/`_fixed_period_fit`), and reads
exp-076's already-collected real `C40`/`G40`/`C80` dense-sweep arrays
(`results.json::headline`) — none hand-typed (R4).

This is exp-075's own single-wall echo model, unchanged in its physics,
refit against a DIFFERENT pair of configs than it was originally scored
against. exp-075 computed `C80 − C40` (the confounded `ABSORB`-vs-`PAD`
series). This cycle computes `G40 − C40` (`PAIR_PAD`, `ABSORB` held fixed
at 40, only geometry/round-trip-distance changes) and `C80 − G40`
(`PAIR_ABSORB40`, geometry held fixed, only `ABSORB`/reflectance changes)
— the two axes exp-076 decorrelated. No new derivation, no new
idealization beyond exp-075's own (§6 below); the model is applied to a
cleaner target.

**Pre-registered bands are reused verbatim from exp-075's own
`phase1_proposal.md` §5** (Test A period rel_dev ≤0.30 SUPPORT / >1.00
REFUTE; Test B shape `r²` ≥0.30 SUPPORT / ≤0.05 REFUTE) — no reason to
change them: they were derived once, from first principles (what
"comparably well-determined" means for a sinusoid-fit comparison in this
program), not tuned to any one dataset, and this cycle is the SAME model
class scored on a different real-data target.

---

## 1. Narrative (≤300 words)

exp-076 (Iteration 53) decorrelated T28's confounded `{C40,C60,C70,C80}`
`ABSORB`/`PAD` axis and found the dominant signal (`amp_ratio=0.119`,
HIGH) is `PAIR_PAD ≡ (C40,G40)` — a difference in `PAD` alone, `ABSORB`
held fixed at 40. Its own load-bearing Phase-5 finding, independently
re-derived from `lab/fdtd2d.py`'s primitive source (confirmed again here,
§2, by direct inspection: `_damping`'s ramp is built from `self.absorb`
and array shape alone; `Sim.__init__` never receives a `pad` argument —
`PAD` cells enter only as more `nx`/`ny`, over which the ramp construction
has no separate dependence): `PAD` is provably lossless vacuum. This rules
out an entire mechanism class — anything acting through absorbed power —
for `PAIR_PAD`'s signal, leaving only a coherent propagation-phase/
interference effect as physically permitted.

exp-075 already built and passivity-gated exactly this kind of mechanism
— a single coherent echo off the `-x` wall, weighted by the graded
`ABSORB` band's own reflection coefficient `r(theta;ABSORB)` — but scored
it against the WRONG pair (`C80−C40`, which entangles both `ABSORB` and
`PAD` changes). `PAIR_PAD` isolates exactly the piece of that same
mechanism the task names: since `C40` and `G40` share `ABSORB=40`
identically, `r(theta;40)` is the SAME function call for both — the
model's entire predicted `C40`-vs-`G40` difference is the image-source
round-trip distance to the near wall changing (`PLANE_X`: 77→117,
`SRC_X`: 300→340, geometry-only), with zero change to reflectance. This
is a clean, zero-new-cost, falsifiable test of whether this SPECIFIC
coherent-echo class explains the dominant PAD-tied signal.

**Result, derived in §5: REFUTE for `PAIR_PAD`** (the task's own primary
target) — same failure shape as exp-075's original scoring (period too
long, shape uncorrelated), now demonstrated on the physically-correct,
decorrelated pair rather than a confounded one. `PAIR_ABSORB40` (the
complementary, geometry-fixed control) scores INCONCLUSIVE. *(281 words)*

---

## 2. Parameter table / mechanism

### 2a. The two configs' geometric relationship, verified in code

| | `C40` | `G40` | `C80` |
|---|---|---|---|
| `ABSORB` | 40 | 40 | 80 |
| `PAD` | 0 | 40 | 40 |
| `nx` | 360 | 440 | 440 |
| `SRC_X` | 300 | 340 | 340 |
| `PLANE_X` | 77 | 117 | 117 |
| `D_SP` | 223 | 223 | 223 |

`PAIR_PAD ≡ (C40,G40)`: `ABSORB` identical (40=40) → `n(x)`, `r(theta)`
identical by construction (same function call, verified: `pad_round_trip_
model.py::load_pair_geometries` asserts `c40["absorb"]==g40["absorb"]`).
Only `PLANE_X`/`SRC_X`/`nx` differ — the image-source round-trip distance.

`PAIR_ABSORB40 ≡ (G40,C80)`: `nx`,`SRC_X`,`PLANE_X`,`D_SP` all IDENTICAL
(verified by assertion over 7 geometry fields) — only `ABSORB` differs
(40 vs 80), so `r(theta;40)` vs `r(theta;80)` is the only thing that
changes. The mirror-image control to `PAIR_PAD`.

### 2b. `PAD` is lossless vacuum — re-confirmed directly against the primitive source

`lab/fdtd2d.py::Sim.__init__` takes `(nx, ny, cells_per_lambda, courant_
frac, absorb)` — there is no `pad` parameter anywhere in `Sim`; `nx`/`ny`
already ARE the padded totals when the caller builds them larger.
`_damping(nx, ny)` builds its cubic ramp `((absorb-i)/absorb)**3` purely
from `self.absorb` and the array's own shape — confirmed by direct
reading, `lab/fdtd2d.py` lines 122-128 (not re-quoted from exp-076's own
citation; read again, this cycle, independently). `PAD` cells sit deep in
the domain interior relative to either edge's own `absorb`-cell band and
never touch the damping construction. This is why `r(theta;ABSORB=40)`
being IDENTICAL for `C40`/`G40` is a proof, not a numerical coincidence —
the exact premise this cycle's test rests on.

### 2c. The model, unchanged from exp-075

`boundary_reflectance.py::c_empty_with_wall` — exp-048's Huygens-Fresnel
direct field PLUS a mirror-image source through the `x=0` wall, weighted
by the complex `r(theta;ABSORB)` from the exact recursive transmission-
line transform over the graded-loss band, backed by the PEC wall.
Imported here verbatim; zero reimplementation, zero re-tuning.

### 2d. Sanity/passivity gates, re-run on THIS cycle's own r(theta) values

| Gate | What it checks | Result (this run) |
|---|---|---|
| G-LOSSLESS | random real index profiles give `|r|=1` exactly | worst deviation `2.220e-16` — PASS |
| G-N1 | N=1 recursion matches the direct textbook formula | worst deviation `1.404e-15` — PASS |
| G-PASSIVITY | every physically-lossy `r(theta;ABSORB)` (62 pairs: 31 angles × {40,80}) satisfies `|r|≤1` | worst `|r|=0.006423` — PASS |

All three PASS — required before any number below is trusted (house
rule); all three are `assert`-gated in `pad_round_trip_model.py`, halting
the run on failure.

### 2e. `r(theta;ABSORB)` on the real dense grid

| `ABSORB` | θ=36.0° | θ=39.0° | θ=42.0° |
|---|---|---|---|
| 40 | \|r\|=0.0029, arg=−78.12° | \|r\|=0.0043, arg=−40.91° | \|r\|=0.0064, arg=−1.23° |
| 80 | \|r\|=0.0000, arg=+171.64° | \|r\|=0.0001, arg=−179.49° | \|r\|=0.0001, arg=−145.47° |

Bit-identical to exp-075's own Sec 2d table (same ABSORB, same theta grid
— the SAME `r(theta;ABSORB)` function, confirming the reused machinery is
untouched).

### 2f. Closed-form round-trip period, per wall (zero-order in r's own phase)

`P_wall(θ) = (180/π)·λ/(2·PLANE_X·sin θ)`, at θ=39°:

| config | `PLANE_X` | `P_wall(39°)` |
|---|---|---|
| `C40` | 77 | 11.824° |
| `G40` | 117 | 7.782° |
| `C80` | 117 | 7.782° |

`PAIR_ABSORB40`'s two terms (`G40`,`C80`) share the SAME `PLANE_X=117` —
a difference of two sinusoids at the SAME frequency, differing only in
`r`'s magnitude/phase, sums to a third sinusoid at that same frequency
(the same algebraic argument T28's own `A=752` cell-identity finding used,
LOGBOOK Iteration 46). `PAIR_PAD`'s two terms (`C40` at 11.824°, `G40` at
7.782°) are at DIFFERENT frequencies — their difference is a BEAT, not a
single sinusoid, and no simple closed form gives its envelope period
directly; this is exactly why the numeric free-period fit (§5), not this
table, is the actual test.

---

## 3. THERMODYNAMICS sidecar — N/A, same disposition as exp-071 through exp-076

**Not applicable.** This mechanism is a coherent-field interference effect
on `C_empty`, not an absorbed-power question — reinforced, not merely
inherited, by this cycle's own finding (§2b): `PAD` cells are proven
lossless vacuum, so `PAIR_PAD`'s signal by construction cannot be an
absorbed-power effect of any kind. No object, no absorber, no new
thermal question is opened here.

---

## 4. T1 escape-route statement

**N/A — instrument/model-fidelity thread, constraint 3 not engaged.**
Matching exp-069 through exp-076's own precedent on this exact
sub-thread: this cycle characterizes the FDTD instrument's own
boundary-condition physics against a decorrelated pair of empty-scene
configs. No absorber, no switch, no constraint-3 scene anywhere in this
file.

---

## 5. Falsifiable predicted outcomes — pre-registered numeric bands

All numbers below are produced by `pad_round_trip_model.py`
(`pad_round_trip_results.json`/`pad_round_trip_output.txt`, this
directory) — none hand-typed (R4). **The bands are fixed BEFORE this
document reports the self-score below** — reused verbatim from exp-075's
own §5 (stated there as the general-purpose bands for "comparably
well-determined periodicity"/shape comparisons in this instrument class);
no data-dependent adjustment is made here.

### Test A — period match

`rel_dev = |P*_model − P*_real| / P*_real`, both `P*` fit with the SAME
`_free_period_search` methodology (imported from `experiments/069-.../
run.py`, not reimplemented). Per the task's own instruction, BOTH the
established narrow `[1,4]°` window AND a widened window are run whenever
the narrower one hits its own boundary — exactly `boundary_reflectance.py`
Sec [6]'s own staged pattern, applied here to whichever curve (real or
model) needs it, since it was not known in advance which would:

- **SUPPORT** iff `rel_dev ≤ 0.30`
- **REFUTE** iff `rel_dev > 1.00`
- **INCONCLUSIVE** otherwise

**`PAIR_PAD`**: both the real and model curves' free-period fits run to
the narrow window's own `4°` boundary (`R²=0.6824` real, `R²=0.5599`
model — both flagged `AT BOUNDARY`), so both widen to `[1,15]°`, where
both land on genuine interior optima (confirmed by a further check to
`[1,180]°`: the model's own `P*` and `R²` are stable to 4 significant
figures across every window from 15° to 180°, `13.264°–13.290°`,
`R²=0.85923` throughout — not a boundary-running artifact).
**`P*_real=4.6113°` (`R²=0.8165`), `P*_model=13.2794°` (`R²=0.8592`) →
`rel_dev=1.8798` → REFUTE.**

**`PAIR_ABSORB40`**: same staged pattern — narrow window boundary-hits for
both curves, widened to `[1,15]°`, both land interior.
**`P*_real=4.1761°` (`R²=0.7156`), `P*_model=8.2026°` (`R²=0.8461`) →
`rel_dev=0.9642` → INCONCLUSIVE** (between the SUPPORT and REFUTE bars).

### Test B — shape match (Pearson `r²`)

Between the model's own predicted `delta(theta)` and the REAL `delta
(theta)` (31 points, the real dense-sweep grid, `experiments/076/
results.json::headline`):

- **SUPPORT** iff `r² ≥ 0.30`
- **REFUTE** iff `r² ≤ 0.05`
- **INCONCLUSIVE** otherwise

**`PAIR_PAD`**: `r = +0.2107`, `r² = 0.0444` → **REFUTE** (just under the
REFUTE ceiling; positively signed, unlike exp-075's original negatively-
signed `C80−C40` shape match, but far too weak to support).

**`PAIR_ABSORB40`**: `r = +0.4468`, `r² = 0.1997` → **INCONCLUSIVE**
(between the bars, correctly signed and closer to SUPPORT than `PAIR_PAD`
managed, but not clearing 0.30).

### Amplitude, disclosed (non-gating)

Model `ptp` / real `ptp`: `PAIR_PAD = 0.424`, `PAIR_ABSORB40 = 0.241` —
the model under-predicts both amplitudes by roughly 2.4×–4.2×, in the
same direction (too small) as exp-075's original scoring, though closer
than that cycle's ~5× shortfall. Consistent with, not independent
evidence for or against, the verdicts below.

### Combined verdict (same combining rule as exp-075: REFUTE if EITHER test REFUTEs; SUPPORT only if BOTH SUPPORT; INCONCLUSIVE otherwise)

**`PAIR_PAD` (the task's own primary target — T28's dominant, HIGH-tier
signal): Test A REFUTE, Test B REFUTE → COMBINED: REFUTE.**

**`PAIR_ABSORB40` (secondary, geometry-fixed control): Test A
INCONCLUSIVE, Test B INCONCLUSIVE → COMBINED: INCONCLUSIVE.**

**Reading, stated plainly, not softened toward a desired outcome:** the
single coherent near-wall echo mechanism, refit against the exact
decorrelated pair the task named, does NOT explain T28's dominant
`PAIR_PAD` signal — its own predicted period (13.28°, driven by the
round-trip-distance CHANGE between `PLANE_X=77` and `PLANE_X=117`) is
still roughly 4× too long relative to the real data's own free-fit period
on this pair (4.61°), and the shape match is weak and on the wrong side
of the REFUTE bar. This is a genuine, informative negative result: it is
not merely "REFUTE repeated on the same wrong pair" — it is REFUTE on the
one pair exp-076's own proof says is the ONLY remaining candidate for this
specific mechanism CLASS (single coherent echo weighted by `r(theta;
ABSORB)`), on the physically correct geometry. **`PAIR_ABSORB40` genuinely
differs in character (INCONCLUSIVE, not REFUTE)** — its period rel_dev
(0.96) sits just under the REFUTE ceiling and its shape r² (0.20) is the
better of the two, correctly signed — worth noting as a secondary,
non-headline observation, not overclaimed as support.

---

## 6. Idealizations (inherited from exp-075 §6, unchanged; plus one new item)

1–8. All of exp-075's own idealizations (discrete-to-continuous decay,
the matched-`eps=mu` friction-PDE bridge and its realizability caveat,
the passivity-adjudicated sign branch, the vacuum-Snell oblique
substitution, single-echo-only, TE-only, 600nm-only) carry over
UNCHANGED — this cycle reuses the identical `n(x)`/`r(theta)`/`c_empty_
with_wall` machinery, none of it re-derived.

9. **Single-wall (near `-x` wall) only, this first cut.** Per the task's
   own instruction and this program's own precedent (exp-075 Phase 1
   proposed single-wall first; the two-wall-cavity extension
   (`two_wall_cavity.py`) followed only after Phase-2 critique flagged it
   as necessary). `PAD` changes BOTH the near-wall (`PLANE_X`) AND the
   far-wall (`(nx−1)−SRC_X`) round-trip distances — named here explicitly,
   not smuggled past: `D_right` for `C40`/`G40`/`C80` is 59/99/99 cells
   respectively (from `two_wall_cavity.py`'s own `d_right` formula), so
   `PAIR_PAD`'s far-wall echo term ALSO shifts (59→99), a second,
   uncomputed contribution this single-wall cut omits. **If Phase 2/3
   flags this REFUTE as premature given the far wall's own shift, the
   two-wall extension is available immediately** — `two_wall_cavity.py`'s
   `image_geometry_right`/`c_empty_two_wall` need only be pointed at this
   cycle's own `(C40,G40,C80)` triple instead of the `{C40,C60,C70,C80}`
   series it was built for; zero new machinery, only a re-target.
2. Only the `PAIR_PAD`/`PAIR_ABSORB40` pair from exp-076's dense 600nm
   window is scored; the 750nm advisory leg (queue item 2, a fixed-
   carrier re-score) is explicitly out of scope for this cycle — a
   separate queued item, not folded in here.
3. No energy sidecar beyond §3's argued N/A (house precedent).

---

## 7. LOGBOOK.md / rule-compliance confirmation

Read LOGBOOK.md in full (RULED OUT R1–R8, LIVE THREADS/T28's complete
Iteration 46–53 history) before writing this proposal. This cycle does
NOT re-propose anything ruled dead:

- **R1** (refractive/Δε cloaking): not engaged — no refractive mechanism,
  no constraint-1 claim anywhere in this file.
- **R2** (integer-λ shell rule): not engaged — no shell-thickness claim;
  `ABSORB=40`/`80` at 600nm ARE integer-λ (2λ/4λ), inherited from
  exp-065's own design, not a new resonance claim of this cycle's.
- **R3** (grid-artifact / resolution-check discipline): not directly
  engaged (no new resolution sweep this cycle — zero new FDTD), but its
  general "surprising feature gets a check before a mechanism debate"
  spirit is honored: the model's own `P*=13.28°` interior-optimum claim
  for `PAIR_PAD` is independently re-checked across five widened windows
  (§5) before being trusted, exactly the kind of "don't take one number
  at face value" discipline R3 established.
- **R4** (no hand-typed "precisely recomputed" figures): every number in
  this document is copied from `pad_round_trip_results.json`/stdout,
  produced by `pad_round_trip_model.py` — verified by direct comparison
  while writing this document, not merely asserted.
- **R5** (look-elsewhere / null-permutation discipline for dense
  constant/parameter searches): not engaged — this cycle fits exactly TWO
  periods (one per pair) against one pre-registered pair of bands each,
  not a dense named-constant search; no look-elsewhere risk of the kind
  R5 targets.
- **R6/addendum** (`G0-e` ground-truth recovery / null-calibration
  gates): not engaged — `amp_ratio`, `R_q`, and any carrier/phase-
  conditioned significance-tested coefficient are absent from this
  cycle entirely; Test A/B are magnitude/period/shape comparisons against
  a zero-free-parameter model, not a fitted, null-calibrated coefficient.
- **R7** (conditioning/VIF number is not sufficient for a closure/
  detection claim): not engaged — no design-conditioning number of any
  kind appears in this cycle.
- **R8** (an unverified robustness argument may not be filed as
  informational ahead of a headline verdict when a named, affordable
  check exists): directly honored, not merely avoided — the model
  PAIR_PAD "interior optimum" claim in §5 is NOT asserted on the strength
  of a single window; the affordable check (widening to `[1,15]°`,
  `[1,60]°`, and further to `[1,180]°`) was actually run and its stable
  result reported, before the REFUTE verdict was written down.

No LOGBOOK item is re-opened, no dead idea is re-proposed. T28's own
mechanism question is not closed by this cycle — a REFUTE of one specific
mechanism class on the physically correct pair, per exp-076's own
lossless-vacuum proof, narrows what remains, exactly as exp-075's original
REFUTE did for the confounded series.

---

## 8. Cost estimate

**Zero FDTD calls. Zero `lab/` diff.** `pad_round_trip_model.py` reads one
already-committed `results.json` (`experiments/076/.../results.json`) and
imports three already-committed modules (`experiments/075/.../boundary_
reflectance.py`, `experiments/065/.../design_geometry.py`,
`experiments/069/.../run.py`); runs in under 2 seconds, single core
(measured, this run — `Sim.__init__` calls only, no `.run()`), and writes
`pad_round_trip_results.json` + `pad_round_trip_output.txt` in this
directory.

---

## Reproduction

`python3 experiments/077-t28-pad-round-trip-echo-model/pad_round_trip_model.py`
— writes `pad_round_trip_results.json` and prints the tables above to
stdout. No seed dependence in this cycle's own new code (the two
sanity-gate random profiles use `boundary_reflectance.py`'s own fixed
`np.random.default_rng` seeds — deterministic, bit-exact run to run).
