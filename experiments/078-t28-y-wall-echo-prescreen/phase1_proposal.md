# PHASE 1 — PROPOSE · Panel Iteration 55 · exp-078
## A closed-form period pre-screen of the y-direction (transverse-normal) wall echo: does the untested mechanism class even land in T28's ballpark? (T28)

*Fresh sub-agent, PHOTONICS charter (PANEL.md seat 1: surface interaction,
absorption spectra, angular dependence, scattering cross-sections — owns
whether the proposal's optical response is coherent as stated, across
wavelength and angle), lead by rotation. Executes PLAN.md's Iteration-55
queue, Tier 0 item 2 (PHOTONICS #1, EM #1, independently convergent —
both seats named this exact candidate at exp-077 Phase 5, after the
x-normal echo class was REFUTEd twice over without ever checking the
parameter — `clear_span_y` — that actually tracks T28's own dominant
`PAIR_PAD` signal). EM's own caution is engaged directly in §3: whether a
naive `A=752` substitution (T21's own already-refuted reference length)
is the right length scale here, or a look-elsewhere trap of the kind R5
already rules out.*

---

## 0. What this is, and what it is not

**ZERO new FDTD calls.** Every number below is produced by
`y_wall_prescreen.py`, this directory (`y_wall_prescreen_results.json` /
`_output.txt`) — none hand-typed (R4). It imports, never reimplements:
`boundary_reflectance.py`'s (exp-075) gated transfer-matrix `n(x)`/
`r(theta;ABSORB)` machinery, `design_geometry.py`'s (exp-065) `CONFIGS`,
`run.py`'s (exp-069) `_free_period_search`/`_fixed_period_fit`, and the
real, already-collected `C40`/`G40`/`C80` dense-sweep arrays
(`experiments/076/results.json::headline`) plus the established real
period citations (`experiments/077/phase1_proposal.md`).

**This is explicitly a PRE-SCREEN, in the queue item's own words — not a
full model build.** The queue item asks one question: does a properly
*derived* (not guessed) grazing-incidence period formula for a
transverse-normal (`+y`/`-y`) wall land anywhere near T28's established
periods, before anyone spends the effort building the full coherent,
y-mirrored, aperture-weighted Huygens-Fresnel propagator (`c_empty_
with_wall`'s own generalization, which exp-075/077 built for the x-wall
and which does NOT exist for a y-wall in this codebase). Consequently:

- This file computes and scores **period only** (a Test-A analog). It
  does **not** build a Test-B shape-match (`Pearson r²` against the real
  `delta(theta)` curve) — that would require the full weighted-aperture
  field model the pre-screen is designed to avoid building. This is
  disclosed as a load-bearing scope limit throughout, not silently
  dropped, and it directly bounds what verdict this document is entitled
  to draw (§7).
- No null-permutation control (R5's own standing house rule) is run on
  the period matches below. This is also disclosed as a load-bearing gap,
  not fixed here — R5 exists precisely because a single, moderately-close
  period match, found by trying more than one candidate length scale,
  is not by itself evidence. §7 treats this as decision-relevant, not
  merely a footnote.

---

## 1. Narrative (≤300 words)

exp-075/exp-077 REFUTEd a coherent echo off the wall whose *normal* is
along `x` (the beam's principal propagation axis) for both `PAIR_PAD` and
`PAIR_ABSORB40`, on the complete two-wall instrument — but T28's own
dominant signal (`PAIR_PAD`, `amp_ratio=0.119`, HIGH) tracks `PAD`'s
`clear_span_y` parameter (0/40/0 across `C40`/`G40`/`C80`), a quantity the
x-normal model never touches. `clear_span_y` is the vacuum gap between the
source aperture's own near edge (`y_lo`) and the *y*-direction
`ABSORB`/PEC wall — a genuinely untested wall orientation.

This file derives the y-wall's period from scratch via the same
mirror-image method exp-075 used for the x-wall, and finds the two
geometries are **not** simple coordinate swaps of each other. The x-wall
case works because mirroring the source *in x* leaves the source's own
`y`-dependent steering phase ramp untouched — the image is a coherently
re-steerable copy of the whole aperture, reducible to two interfering rays
(§3.1, re-derived and validated bit-exact against the committed formula).
Mirroring *in y* touches the very coordinate the steering ramp depends on:
an image point preserves the *real* point's own driven phase (a physical
wall reflects whatever instantaneous field arrives, it does not
re-compute a new "steering intent"), so the clean two-ray reduction does
not transfer. The physically justified reduction instead compares one
source edge (T21's own established diffracting entity) to its own
wall-image, weighted by `r(theta;ABSORB)` — the *identical* transfer-matrix
reflectance already gated and Red-Team-adjudicated for the x-wall, reused
here because `Sim._damping` applies the same cubic ramp to all four domain
edges (verified in code, §2). The result: no exact closed form exists in
one line, but a fully closed-form, zero-FDTD numeric evaluation does
(§3.2), and it is scored against T28's established periods in §5-§6.

---

## 2. Parameter table / geometry

All values from `y_wall_prescreen_results.json::geometry` and
`::primary_model_edge_curves` (Sec [0]/[1]/[4] of `_output.txt`).

| cfg | `ABSORB` | `PAD` | `OBJ_Y` | `y_lo` | `A` | `D_SP` | `clear_span_y` | dist(edge→obs) | dist(image edge→obs) | fixed offset (cells) |
|---|---|---|---|---|---|---|---|---|---|---|
| C40 | 40 | 0 | 792 | 40 | 752 | 223 | 0 | 784.3679 | 861.3669 | 76.9990 |
| C60 | 60 | 20 | 812 | 60 | 752 | 223 | 0 | 784.3679 | 900.0628 | 115.6949 |
| C70 | 70 | 30 | 822 | 70 | 752 | 223 | 0 | 784.3679 | 919.4526 | 135.0847 |
| C80 | 80 | 40 | 832 | 80 | 752 | 223 | 0 | 784.3679 | 938.8679 | 154.5000 |
| G40 | 40 | 40 | 832 | 80 | 752 | 223 | **40** | 784.3679 | 938.8679 | 154.5000 |

`A` (source-edge-to-`OBJ_Y` offset) is bit-identical (752) across the
whole congruent series — the T21 length scale is unchanged by this
mechanism's own construction, exactly as EM's caution named as a risk if
naively reused (§3.3 explains why this file does *not* reuse it as the
y-wall's own governing length). Note `G40` and `C80` share an **identical**
`(OBJ_Y, y_lo)` pair (832, 80) — both have `PAD=40` — so under the
edge-image reduction they share the identical fixed geometric offset
(154.5000 cells); only `r(theta;ABSORB)` (40 vs 80) differs between them.
`C40` and `G40` share the identical `ABSORB=40` (hence identical
`r(theta)`) but differ in geometric offset (76.999 vs 154.500 cells) —
the mirror image, by construction, of `PAIR_PAD`'s own established finding
that its signal is a pure propagation/phase effect, not a reflectance
one (exp-076's lossless-vacuum proof).

**T1 escape route: N/A.** Instrument/model-fidelity thread, matching every
T28 cycle since exp-069 — no absorber, no switch, no constraint-3 scene
anywhere in this file.

---

## 3. Derivation

### 3.1 — Validation: re-deriving the established x-wall formula from scratch

`boundary_reflectance.py` Sec [8] states, without an in-file derivation,
`P_x(theta) = (180/pi)*lambda / (2*PLANE_X*sin(theta))`. This file
re-derives it independently (`x_wall_closed_form_rederivation`,
Sec [2] of `_output.txt`) via the mirror-image method: the source's own
driven phase is `phase(y_s) = k*sin(theta)*(y_s - OBJ_Y)`
(`_src_amp`/`add_line_source`, verified against code); the direct wave
travels in direction `(-cos(theta), +sin(theta))` (per `add_line_source`'s
own docstring); the `x=0` PEC wall's image flips `k_x`, preserves `k_y`
→ direction `(+cos(theta), +sin(theta))`. Evaluated at the observation
point `(PLANE_X, OBJ_Y)`, the `SRC_X` dependence cancels identically
between direct and image terms, leaving
`Delta_phi(theta) = 2*k*PLANE_X*cos(theta)`, whose period is exactly the
committed formula. **Reproduced bit-for-bit**: `C40` `11.823882°` vs
`11.823882°` (`|dev|=1.776e-15°`, float noise); `C80` `7.781529°` vs
`7.781529°` (`|dev|=0.000e+00°`). The method is validated before being
applied somewhere new.

### 3.2 — Why a bare x↔y coordinate swap is not justified (§1b of the script)

The x-wall reduction's own validity rests on one specific fact: mirroring
the source *in x* does **not** touch the `y`-dependent phase ramp, so the
whole aperture's image is coherently re-steerable, exactly like the real
aperture — a clean two-ray/plane-wave picture. Mirroring *in y* **does**
touch that same coordinate. A real point source at `y_s` reflected by a
wall does not "re-steer" — it re-radiates its own arriving instantaneous
phase (scaled/rotated only by `r(theta)`), from the mirrored position.
This is a different physical object from "the same phased array, position
translated," and it is what makes the y-wall genuinely NOT a coordinate
swap of the x-wall formula.

**Primary reduction (edge-image / self-echo):** T21's own established
mechanism already treats the source aperture as edge-dominated (its two
taper edges at `y_lo`/`y_hi`, offset `∓A` from `OBJ_Y`). A stationary-phase
argument on the y-mirrored aperture sum (`phase1_proposal.md` reasoning,
not separately re-coded — the sum's phase gradient
`dPhi/dy_s ≈ k*(sin(theta)+1)` never vanishes over `theta∈[36°,42°]`,
so the sum has no interior stationary point and is dominated by its own
edges, the identical idealization T21's own real-aperture model already
makes) licenses treating the near edge (`y_lo`) and its own wall-image as
the leading-order y-wall contribution:

```
Delta_phi_self(theta; cfg) = arg(r(theta; ABSORB))
    + k * [ hypot(D_SP, OBJ_Y + y_lo) - hypot(D_SP, A) ]
```

The driven-phase term `k*sin(theta)*A` is **identical** on the real edge
and its own image (an image source preserves the real source's own
instantaneous phase, up to `r`'s own phase and magnitude) and cancels
exactly in the difference — it does **not** survive into `Delta_phi_self`,
unlike the x-wall's `2*k*PLANE_X*cos(theta)` term, which comes entirely
from a fixed-position propagation-distance difference, not a
driven-phase term. This is the structural reason the y-wall is a
"genuinely different formula," not a relabeled x-wall formula, exactly as
the queue item anticipated.

### 3.3 — Why `A=752` is deliberately NOT used as this model's governing length

EM's own caution named `A=752` (T21's own already-refuted reference
length) as a look-elsewhere risk. This file does not use it as the
primary model's governing length at all: `A` appears in
`Delta_phi_self` only inside a **fixed, theta-independent** distance term
(`hypot(D_SP,A)`, the real edge's own fixed distance to the observation
point) — it contributes a *constant* offset, not an oscillatory
component, so it cannot itself be mistaken for producing T28's periodicity
under this derivation. The two length scales that *do* enter as new,
config-varying quantities are `OBJ_Y` and `y_lo` (via the image distance
`hypot(D_SP, OBJ_Y+y_lo)`) and the `ABSORB`-dependent `r(theta)` — neither
is `A`, and neither was chosen by searching for a match; both are the
geometric quantities the edge-image construction itself requires.

Sec [6]/[6b] of the script *does* separately evaluate two **explicitly
labeled, secondary, naive** coordinate-swap candidates
(`P_y = lambda/(2*Y_STANDOFF*cos(theta))` for `Y_STANDOFF ∈ {OBJ_Y, y_lo}`)
— reported only because the queue asks whether *any* simple substitution
is in the ballpark, and flagged with R5's own look-elsewhere caveat
throughout (two candidates × four reference periods = 8 comparisons, no
null-permutation control, no comparison here is treated as evidence).

### 3.4 — Load-bearing premise check: does `r(theta;ABSORB)` transfer to a y-wall unchanged?

`lab/fdtd2d.py::Sim._damping` (verified live, `_output.txt` Sec [0], not
merely cited) builds ONE `ramp = (arange(absorb,0,-1)/absorb)**3` array
and applies it via `np.maximum` to all four domain edges identically —
x-low, x-high, y-low, y-high. A single `Sim` instance's own x-edge and
y-edge `damp_e` columns (same `absorb`) are read directly and compared:
`worst |x_edge_col - y_edge_col| = 0.000e+00`, exactly identical. The
x-wall's already-gated (`G-LOSSLESS`, `G-N1`, `G-PASSIVITY`), Red-Team
phase-convention-adjudicated (R8, Iteration 52) `r(theta;ABSORB)` therefore
applies to a y-wall of the same `ABSORB` depth **unchanged, by
construction** — no new reflectance model is built or needed here.

---

## 4. Falsifiable predicted outcomes — pre-registered numeric bands

**Test A (period) band reused verbatim from exp-075/077** (`rel_dev ≤ 0.30`
SUPPORT / `>1.00` REFUTE / else INCONCLUSIVE), because this is the same
general-purpose "comparably well-determined periodicity" band this
program has used for every T28 echo-model period comparison since
Iteration 52, and this file's period statistic is computed by the
identical imported `_free_period_search` machinery — no reason to retune
it for one more application of the same instrument.

**No Test B band is applicable this cycle** — disclosed as a scope limit
(§0), not a silently-dropped test. Consequently **this document cannot
compute this sub-thread's own Combined Verdict** (which by established
convention, exp-075 §5/exp-077 §5, requires BOTH Test A and Test B) — only
a Test-A-only reading, explicitly labeled as such throughout §5-§7.

---

## 5. Results (all numbers from `y_wall_prescreen_results.json` / `_output.txt`, never hand-typed)

### 5.1 — Real, already-established reference periods (re-derived here from committed data, not copied from prose)

| reference | P* (this run) | R² | citation |
|---|---|---|---|
| `C80−C40` (exp-069) | `2.8421°` | `0.6272` | LOGBOOK T28, exp-069 |
| `PAIR_PAD` (exp-077) | `4.6113°` | `0.8165` | exp-077 phase1_proposal.md |
| `PAIR_ABSORB40` (exp-077) | `4.1761°` | `0.7156` | exp-077 phase1_proposal.md |
| `PAIR_PAD`, 750nm two-wall (exp-077, carried, not re-derived) | `3.8271°` | `0.9884` | exp-077 phase1_proposal.md §5c |

All three re-derived values reproduce their citations exactly (to the
printed digits), confirming the reuse of `_free_period_search`/the real
data is correct before scoring the model against them.

### 5.2 — Primary model: self-echo curve, per config

| cfg | `ptp(Delta_phi_self)` | `\|r\|` range | free-period `P*` (narrow[1,4]) | R² | at boundary? |
|---|---|---|---|---|---|
| C40 | `76.897°` | `[0.0029, 0.0064]` | `3.2180°` | `0.1557` | no |
| C60 | `131.795°` | `[0.0001, 0.0007]` | `4.0000°` | `0.2418` | **yes** (widens to `60°`, R²=0.9895) |
| C70 | `133.798°` | `[0.0001, 0.0001]` | `4.0000°` | `0.2777` | **yes** (widens to `60°`, R²=0.8740) |
| C80 | `358.446°` | `[0.00003, 0.00012]` | `3.1880°` | `0.1439` | no |
| G40 | `76.897°` (= C40, exact) | `[0.0029, 0.0064]` | `3.2105°` | `0.1544` | no |

`C60`/`C70` (deep `ABSORB`, `\|r\|≈10⁻⁴`) run to the search boundary at
every widened stage, converging on implausibly high `R²` (`0.98`/`0.87`)
at a 60° period — a signature of fitting a near-degenerate, numerically
ill-conditioned quantity (`arg()` of a complex number whose magnitude is
within an order of magnitude of float noise in the underlying transfer-
matrix recursion), not a physical oscillation. **Neither `C60` nor `C70`
is used in any scored comparison below** (they enter no `PAIR_*`
combination this cycle scores), but `C80` — whose own `\|r\|` is smaller
still (`3×10⁻⁵`–`1×10⁻⁴`) — **is** used in two of the three scored
comparisons (`C80−C40` and `PAIR_ABSORB40`), and its own free-period
search, while nominally "interior" (not literally at the grid boundary),
rests on the same near-noise-floor `\|r\|` regime. This is the single
biggest reason for caution in §7.

### 5.3 — Primary model: `PAIR_PAD`/`PAIR_ABSORB40`/`C80−C40` deltas, scored against real periods

| comparison | P*_real | P*_model | rel_dev | Test-A-only verdict |
|---|---|---|---|---|
| `C80−C40` | `2.8421°` | `3.2105°` | `0.1296` | SUPPORT |
| `PAIR_PAD` (T28's actual dominant target) | `4.6113°` | `3.1654°` | `0.3136` | **INCONCLUSIVE** (just over the 0.30 bar) |
| `PAIR_ABSORB40` | `4.1761°` | `3.2030°` | `0.2330` | SUPPORT |

Model R² at these three comparisons: `0.1530` / `0.1331` / `0.1493` —
**all far below** the real data's own established R² (`0.63`–`0.82`) and
below the R² this program has previously treated as even a "soft" CONFIRM
(exp-070's own P-070-1, R²≈0.26–0.30, was itself scored "softer than
first read"). No comparison here runs to a search boundary (§5.4's flag
in the script output is `False` for all three), but that only means an
interior optimum exists — it does not mean the fit is strong.

### 5.4 — Secondary, naive coordinate-swap candidates (R5-flagged, not evidence)

`Y_STANDOFF=OBJ_Y`: periods `0.886°`–`0.931°` at 600nm — `rel_dev` against
all four references ranges `0.67`–`0.81` (INCONCLUSIVE-to-REFUTE-adjacent,
never SUPPORT). `Y_STANDOFF=y_lo`: periods `9.2°`–`18.4°` at 600nm —
`rel_dev` ranges `1.0`–`5.5` for `C40`, and for `C80`/`G40` (`y_lo=80`,
`P_y=9.2157°`) `rel_dev=[2.243, 0.999, 1.207, 1.408]` against
`[C80−C40, PAIR_PAD, PAIR_ABSORB40, PAIR_PAD-750nm]` respectively — one
near-boundary case (`0.999` against `PAIR_PAD`'s real `4.6113°`, on the
REFUTE side of `1.00` by a hair), otherwise squarely REFUTE-range
(`_output.txt` [6b] has the full table). **Neither naive
candidate is treated as supporting or refuting anything** — both are
reported solely because the queue asked whether a simple substitution
lands in the ballpark (it mostly does not), with R5's caveat that trying
two candidates against four targets without a null-permutation control is
a search, not a derivation.

---

## 6. Idealizations (stated explicitly, house norm)

1. **Edge-dominance idealization.** The primary model reduces the full
   y-mirrored aperture sum to its own near edge only (`y_lo`), justified
   by a stationary-phase argument (§3.2) that is the same class of
   idealization T21's own established model already makes for the real
   (non-mirrored) sum — not independently re-verified numerically against
   a full aperture sum here (that full sum is exactly the "y-mirrored
   propagator" this pre-screen is scoped to avoid building).
2. **No amplitude/taper weighting.** `cos(Delta_phi_self(theta))` is used
   as a unit-amplitude proxy oscillation curve — it does not weight by
   `\|r(theta)\|` or the source's own taper profile. This means configs
   with very small `\|r\|` (`C60`, `C70`, and especially `C80`) are treated
   on equal footing with configs whose `\|r\|` is 10–200× larger (`C40`,
   `G40`) in every comparison that involves them — almost certainly
   overstating their evidentiary weight (§5.2/§5.3, §7).
3. **Single (near) wall, one edge only.** Neither the far edge (`y_hi`)
   nor the far y-wall's own image is included (by domain symmetry the far
   pair contributes an equal-magnitude, phase-shifted term; a real model
   would sum all four contributions — real+near-image, and the analogous
   far-edge+far-image pair — coherently, not just the one pair modeled
   here).
4. **No Test B.** No shape (`Pearson r²` against real `delta(theta)`) is
   computed anywhere in this file (§0, §4) — a period match alone, per
   this sub-thread's own established convention, is necessary but never
   sufficient for a Combined SUPPORT.
5. **No null-permutation control** (R5) on any period match in §5.3/§5.4.
6. **TE/matched-`eps=mu` admittance**, inherited unchanged from
   `boundary_reflectance.py` — the same unrealizable-admittance caveat
   MATERIALS attached to the x-wall model (exp-077 Idealization 10)
   applies identically here; a y-wall SUPPORT or REFUTE under this
   construction says nothing about realizability either way.
7. **600nm only** — the 750nm reference (`3.8271°`) is compared against,
   not independently modeled at 750nm for this file's own primary curves
   (Sec [6] does evaluate the naive secondary candidates at both
   wavelengths, but the primary edge-image model is 600nm-only this
   cycle).
8. **Image-phase convention.** `Delta_phi_self` assumes an image source
   preserves the real source's own driven phase exactly (up to `r`'s own
   complex factor) — the same convention the x-wall model uses implicitly
   via `c_empty_with_wall`'s coherent sum, not independently re-derived
   or gated here as its own numbered check.

---

## 7. Self-scored verdict

**INCONCLUSIVE (Test-A-only reading) — this pre-screen does NOT desk-close
the y-wall echo mechanism the way EM's own caution hoped it might, but it
also does not license treating the period match as real support for
building the full model.** Reasoning, weighing both directions honestly:

**Why this is not a REFUTE.** None of the three primary comparisons come
remotely close to the `>1.00` REFUTE bar (worst case `0.314`, barely over
the *SUPPORT* line, not anywhere near REFUTE) — a sharp contrast with the
x-wall model, whose own single-wall/two-wall REFUTEs were period
deviations of `88%`–`188%`. The naive secondary candidates fare far worse
(`rel_dev` mostly `0.7`–`5.5`), but they are explicitly not this file's
own primary claim (§3.3). Desk-closing this mechanism class on this
evidence would overstate what a REFUTE requires.

**Why this is not a SUPPORT either, despite 2 of 3 raw period comparisons
clearing the `≤0.30` bar.** Three independent, load-bearing reasons, each
sufficient on its own:

1. **The one comparison built from the least-degenerate, most trustworthy
   pair of configs (`PAIR_PAD` — `C40` vs `G40`, both `ABSORB=40`,
   comparable non-tiny `\|r\|`) is the one that does NOT clear SUPPORT**
   (`rel_dev=0.314`). `PAIR_PAD` is also, per exp-076's own `PAD_TIED`
   finding, T28's *actual* dominant empirical target — the comparison
   this pre-screen most needs to land well on is its own weakest result.
2. **Two of the three comparisons that DO clear SUPPORT are contaminated
   by `C80`, whose own `\|r\|≈3×10⁻⁵–1×10⁻⁴` sits within roughly an order
   of magnitude of what this file's own `C60`/`C70` results show is a
   numerically ill-conditioned regime** (those two configs' own period
   searches run to the 60° search boundary with implausible `R²` up to
   `0.99` — a clear artifact signature). `C80`'s own comparisons did not
   run to boundary, but they rest on the same small-`\|r\|` footing, and
   Idealization 2 (no amplitude weighting) means this file cannot rule
   out that `C80`'s contribution to those two "SUPPORT" verdicts is
   dominated by near-noise-floor phase, not real reflectance structure.
3. **Every fit's own R² (`0.13`–`0.15` at the three scored comparisons) is
   far below what this program has ever treated as a credible period
   match** (the real data's own R² is `0.63`–`0.82`; even exp-070's own
   "softer than first read" CONFIRM was R²≈0.26–0.30) **and no
   null-permutation control has been run** to establish these R² values
   are distinguishable from a period fit to structured noise over a
   narrow 6° window (exactly the R5 failure mode: a moderately-close
   period match, found without a look-elsewhere control, is not by
   itself evidence).

**The honest bottom line**: this candidate mechanism survives the cheap
period pre-screen (it is not obviously wrong, unlike the x-wall class),
but the pre-screen's own evidence for it is weak, partially contaminated,
and missing the two checks (Test B shape match; a null-permutation
control on the period match) that would be needed before recommending the
full y-mirrored coherent propagator be built. **Recommendation for Phase
2/3, stated plainly rather than smuggled into the verdict**: the cheapest
next move that would actually discriminate is NOT the full propagator —
it is (a) a null-permutation control on this file's own Test-A period
searches (desk-only, reuses `pad_round_trip_model.py`'s own null-
generation pattern), and (b) re-scoring §5.3 with `C60`/`C70`/`C80`
weighted by their own `\|r\|` (still desk-only, no full propagator needed)
to see whether the two nominal "SUPPORT" comparisons survive once the
near-noise-floor configs are properly downweighted. Only if both of those
cheap checks still look encouraging does building the full model become
justified.

---

## 8. Open questions for Phase 2

1. Does a null-permutation control (R5) on this file's own Test-A period
   searches show `rel_dev≤0.30` at a rate distinguishable from chance
   over this narrow window, or does it reproduce the "any reasonably
   dense search finds a plausible match" failure mode already established
   at exp-070?
2. Does `\|r\|`-weighting the per-config self-echo curves (cheap, still
   desk-only) change which of the three primary comparisons clear
   SUPPORT — in particular, does it downgrade `C80−C40` and
   `PAIR_ABSORB40` once `C80`'s own near-noise-floor contribution is
   properly discounted, leaving `PAIR_PAD` (already the weakest) as the
   only comparison that matters?
3. Is the edge-dominance idealization (§6.1) actually safe, or does the
   full (non-edge-reduced) y-mirrored aperture sum contribute genuinely
   different oscillatory structure the two-point reduction cannot see —
   i.e., is building the full propagator actually unavoidable before this
   mechanism can be honestly scored, regardless of what (1)/(2) show?
4. Does including the far edge/far-wall pair (Idealization 3) change the
   period materially, or does it mostly add amplitude (as the x-wall
   two-wall extension did) without moving `P*`?
5. If (1) and (2) both come back encouraging, what is the minimal
   Test-B-capable model that stays zero-FDTD — can `dg048.field_and_h` be
   reused with a genuinely y-mirrored source-position array (not just a
   translated one), or does a proper y-mirror require new machinery
   beyond a parameter change to the existing propagator?
