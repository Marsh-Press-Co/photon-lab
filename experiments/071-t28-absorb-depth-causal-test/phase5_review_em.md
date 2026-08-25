# PHASE 5 — REVIEW: ELECTROMAGNETISM (blind) · Panel Iteration 48 · exp-071

*Fresh sub-agent, ELECTROMAGNETISM charter (PANEL.md seat 3): field/wave
behavior, impedance matching, energy coupling; owns reciprocity/passivity/
causality bookkeeping. No memory of this seat's own Phase-2 critique on
this cycle (a different fresh instance) — read everything fresh from
`results.json`, `run.py`, `design_geometry.py`, and `lab/fdtd2d.py` directly,
not from prose summaries.*

## 1. Independent re-derivation of Block SETTLE-C60C70 from raw `results.json`

Read `results.json["settle_c60c70"]["scored"]["cells"]` directly:

| config | θ | C_2800 | C_4200 | |Δ| abs | Δ/GATE_HARD | Δ/C_2800 (rel. to signal) |
|---|---|---|---|---|---|---|
| C60 | 37.2° | 0.0097262 | 0.0097259 | 2.49e-7 | 2.5e-4 | 2.56e-5 (0.0026%) |
| C60 | 41.4° | -0.0076557 | -0.0076557 | 4.33e-8 | 4.3e-5 | 5.66e-6 (0.00057%) |
| C70 | 37.2° | 0.0099146 | 0.0099144 | 1.51e-7 | 1.5e-4 | 1.53e-5 (0.0015%) |
| C70 | 41.4° | -0.0078972 | -0.0078972 | 4.03e-8 | 4.0e-5 | 5.11e-6 (0.00051%) |

**The GATE_HARD substitution is sound here, and does not introduce a new
gap.** I computed the shift both ways: against `GATE_HARD=0.001` (the scale
actually used, `run.py::score_settle_c60c70`) and against the raw signal
value itself (`|Δ|/C_2800`, the convention P-069-4/exp-065 used for
C40/C80 at STEPS 1400→2800). Both land 3–4 orders of magnitude under any
plausible settling threshold (≤1%), and they *agree with each other* to
within a factor of ~2 at every cell, because these are the peak angles
(chosen specifically to sit near the extrema of `delta(θ)`, not a
zero-crossing) — `C_2800 ≈ 0.008–0.010`, i.e. eight to ten times
`GATE_HARD` itself, so the two normalizations are not in tension. Had this
check instead been scored at a zero-crossing angle (where `C_2800→0`), a
`Δ/C_2800`-style relative metric would blow up toward infinity for a
physically negligible absolute shift — `GATE_HARD`-relative scoring is
actually the *more* robust convention at exactly the angles a resolution
check would otherwise want to probe, so this is a good substitution, not a
weaker one dressed up as equivalent.

**Wave-physics read of what "settled" means here, and whether this
evidences it.** `lab/fdtd2d.py::Sim._damping` (verified directly, lines
122–129) is a purely dissipative, per-step multiplicative loss
(`exp(-0.30·d)`, `0 < factor ≤ 1` everywhere, no gain term) — for a linear
passive system like this, the field at a fixed observer point after a
transient launch converges to a steady state via decaying reflection
echoes off the absorbing boundary; "settled" means those echoes have
decayed below the measurement's own noise floor. A residual shift 2–4
orders of magnitude below that floor after a 50%-longer run (2800→4200
steps, the identical STEPS ratio that certified C40/C80) is exactly the
signature a genuinely decaying transient produces, not the signature of an
unsettled channel (which would show a shift comparable to or above the
floor, the way the pre-2800 STEPS=1400 data did historically). **I concur
with the design's own conclusion: C60/C70 are settled at STEPS=2800, and
Block SETTLE-C60C70's construction closes the exact gap this seat's own
prior-cycle Phase-2 critique raised.**

One residual, lower-severity limitation worth naming for the record (not a
reason to distrust this result): this is a **2-point** check (2800 vs
4200), not the 4-point asymptotic series (1400/2800/4200/5600) that
originally certified STEPS=2800 for C40. A purely dissipative single-mode
system cannot show a *non-monotonic* residual in STEPS without multiple
decaying modes beating against each other — possible in principle for a
2D boundary-truncation problem, but even a hypothetical second mode ten to
one-hundred times larger than what was observed here would still land
safely under the 1% CONFIRM band. Cheap to shore up further (one more
STEPS=5600 point per config/angle, ~4 calls) if a future cycle wants the
literal 4-point series, but not load-bearing for this cycle's own
conclusion.

## 2. Is a genuine ~4% ABSORB-depth-dependent period shift physically plausible?

This is the sharpest question this review can add, independent of whether
the current window can resolve it. My answer: **yes, plausible — but not
via the mechanism the Combined Verdict's own linear model
(`P*(ABSORB) = m·ABSORB + c`) implicitly assumes.**

`ABSORB` is a numerical domain-truncation depth (confirmed directly,
§1) — it is not a physical medium the beam couples to, so there is no
impedance-matching or energy-coupling story in which the *interior*
aperture-diffraction pattern (T21's own `P(θ)=λ/(A·cosθ)`, set by the
fixed `A=752`) should depend on how many cells of lossy boundary sit
beyond it. A properly-functioning absorbing boundary is, by construction,
supposed to be invisible to the interior solution — extending it should
change *nothing* about the field the observer sees, which is the entire
reason PML-style boundaries are used instead of hard walls. If the
observed period genuinely tracked `ABSORB` linearly and smoothly with no
floor, that would be the surprising, hard-to-motivate result.

**The EM-plausible mechanism is residual back-reflection off an
*imperfectly* terminated boundary, interfering with the primary
aperture-diffraction pattern to produce a beat.** No absorbing boundary of
finite depth is perfectly reflectionless; the cubic ramp here
(`d=(i/absorb)³`, `exp(-0.30·d)`) is *identical in normalized shape*
regardless of `absorb` — only the total number of lossy layers a
reflected wave must cross (there and back) changes with `ABSORB` depth.
That is a textbook "more layers ⇒ exponentially smaller residual
reflection, with diminishing returns" profile: a real residual-reflection
amplitude should **shrink roughly geometrically with ABSORB depth and
saturate**, not grow linearly forever. This makes a specific, falsifiable
prediction that is a *better* fit to the actual (unresolved, caveated)
data than the linear model reported: the recovered `P*` sequence
(`2.4361° → 2.5188° → 2.5338° → 2.5338°` at ABSORB `40/60/70/80`) shows
**essentially the entire shift occurring in the first step (C40→C60,
+0.0827°) with near-zero further movement (C60→C70→C80, +0.0150° then
+0.0000°)** — a saturating curve, not a straight line, despite the
reported linear-fit `R²=0.8664`. `phase4_results.md` reports the R² but
never flags this shape asymmetry.

I want to be precise about how much weight this carries: these numbers sit
below the same Rayleigh floor `run.py` already (correctly) refuses to
trust (§3 below reaffirms that gate is sound), so this is offered as a
**candidate mechanism and a falsifiable discriminator for a future,
properly-powered test — not a claim that this cycle's data confirms
saturation over linearity.** But it is a concrete reason to expect *if* a
real ABSORB-tied effect exists, it should look like a saturating
boundary-reflection artifact, not a linearly-growing physical coupling —
which also means the Combined Verdict's own CONFIRM criterion
(`|P*(80)-P*(40)|/mean ≥ 30% AND R²≥0.50`, a straight-line test) is testing
the wrong functional form for the most physically-motivated candidate
mechanism, independent of the resolution-floor problem it was correctly
caught by this cycle.

**A second, related EM point on the causal-manipulation design itself:**
in this congruent series, `ABSORB` and `PAD` (hence `NX`/`NY`, hence the
total box round-trip path length) are *exactly collinear* —
`ABSORB = 40 + PAD` for all four configs, by the congruent construction
that holds `A` fixed. A residual-reflection-beat mechanism's frequency
content is set by the **round-trip optical path to the boundary and
back** (a length scale, tied to `NX`/`PAD`), while its **amplitude** is
set by the **absorption strength** (tied to `ABSORB`'s cell count via the
damping profile). On this single-axis series those two physically
distinct EM quantities cannot be told apart — a future test that wants to
attribute a real effect to "ABSORB depth" specifically (as opposed to
"the boundary is closer/farther away") needs a config that varies one
while holding the other fixed (e.g., a deeper `ABSORB` at *fixed* `PAD`/
`NX`, or vice versa). This is not a defect in exp-071 — it correctly
executed exactly the mandate it was given — but it is a real degeneracy in
what that mandate's single-parameter-axis design can, in principle,
attribute causally, worth flagging before any future cycle calls a result
"ABSORB-tied" rather than "boundary-construction-tied" on this series
alone.

## 3. Peak-cell R3 construction (`_one_run_r3`, `R3_CONFIGS`) — passivity/causality check

**No inconsistency found.** Checked specifically for the class of defect
this seat caught at Iteration 42/exp-065 (conflating the wave's Courant
phase speed with the leapfrog stencil's true 1-cell/step domain of
dependence):

- `R3_STEPS = 4200 = 2800 × 1.5` and `R3_RATIO = 1.5` (spatial rescale,
  `cpl` 20→30). With `courant_frac` held fixed across both resolutions,
  `dt ∝ dx ∝ 1/cpl`, so covering the *same physical time* at `cpl=30`
  requires `STEPS_r3 = STEPS_native × (cpl_r3/cpl_native) = 2800 × 30/20 =
  4200` — exactly what's used. This is the correct scaling (verified by
  direct arithmetic, not taken on trust), and is the specific fix this
  seat's own prior finding required; it is applied correctly here.
- `ABSORB`/`PAD` cell counts are scaled by the same `R3_RATIO=1.5` in
  `R3_CONFIGS` (e.g. `C60_R3`: absorb=90, pad=30), which holds the
  **physical** (wavelength-referenced) thickness of the absorbing layer
  fixed across native and R3 resolutions — correct; a fixed *cell* count
  across a resolution change would have changed the physical boundary
  thickness and invalidated the comparison.
- `courant_frac` itself (a dimensionless stability fraction, not a fixed
  `dt`) is reused unchanged — correct; this is what should stay invariant
  across a spatial-resolution rescale, not the raw step count or `dt`.
- Damping remains purely dissipative (`0 < exp(-0.30·d) ≤ 1`) for every
  `(absorb, pad)` pair used, native or R3 — no new passivity risk, no gain
  introduced by the rescale. Confirmed directly from `_damping`'s source
  (§1 above), not deferred to prior seats' say-so.

I found nothing here that undermines P-071-4/P-071-5's peak-cell R3
result — the construction is dimensionally and causally sound.

## 4. Proposed next move for T28 (Iteration 49's queue)

**Yes — a direct phase/beat measurement between adjacent-ABSORB configs can
plausibly sidestep the Rayleigh resolution floor, and it can be run on
data already sitting in `results.json` today, at zero new FDTD cost.**

The design that just ran independently free-fits an absolute period to
each of `C40(θ)`, `C60(θ)`, `C70(θ)`, `C80(θ)` and compares the four fitted
numbers *after the fact*. That is precisely the estimation strategy the
Rayleigh criterion bounds: resolving two absolute frequencies that are
`~4%` apart from a `~2.5`-period window is what the math correctly says
this window cannot do. But T28 was **discovered** in the first place by
looking at the raw *difference* `C80(θ)−C40(θ)` directly (exp-069), not by
subtracting two independently-fit periods — and that same move, done more
formally, is the right next step:

1. **Joint/differential phase-drift fit on the pairwise difference
   signals** `delta_AB(θ) = C_B(θ) − C_A(θ)` for every adjacent pair
   (C40–C60, C60–C70, C70–C80; C40–C80 already exists as T28's own
   founding signal). Fit a **single shared carrier period** (e.g. the
   best-established reference — T21's own `P(θ)` or a pooled fit across
   all four raw series) plus a **linear phase-ramp term** to each
   difference signal, instead of independently fitting `P_A` and `P_B`
   and subtracting. If `P_A = P_B` exactly (shared-geometry hypothesis),
   the difference signal is a *clean* single-frequency sinusoid at the
   shared period with zero phase drift (this seat's own established
   argument from exp-069: two sinusoids of one frequency sum to a third at
   that same frequency, regardless of amplitude/phase — the null
   hypothesis has a sharp, zero-parameter prediction here). If
   `P_A ≠ P_B` even slightly, the difference signal shows a **systematic,
   accumulating phase lag** across the window — a beat/heterodyne
   signature. This is the standard reason beat-frequency measurement beats
   independent-frequency estimation for detecting *small relative*
   differences between two nearly-identical oscillators: it converts an
   absolute-frequency-resolution problem (Rayleigh-limited, and failing
   here) into a phase-accumulation problem, which for a real `~4%` split
   over the existing window's `~2.45` periods already predicts roughly
   `2π×2.45×0.039 ≈ 0.60` rad (~34°) of accumulated phase drift — large
   enough to be plausibly visible directly in the shape of the difference
   trace's own zero-crossing spacing, without needing 10× more angular
   range. **This is a genuinely different, more powerful statistic than
   what P-071-2 computed, is falsifiable (predicts zero drift under the
   null, a specific nonzero drift under the alternative), and costs zero
   new FDTD calls** — pure re-analysis of `results.json`'s own
   `dense_causal` rows plus the reused exp-069 `block_dense` data.

2. **A single new high-ABSORB config, cheap, to test the saturation
   prediction from §2.** If the residual-reflection-beat mechanism is
   real, a config at, say, `ABSORB≈120` (double `C80`, same congruent
   construction, one new dense sweep = 31 calls) should show **near-zero
   further period shift relative to C80** — the saturation the C40→C60→
   C70→C80 shape already hints at. A continued, non-saturating shift at
   `ABSORB=120` would instead favor the (harder-to-motivate) linear-in-
   ABSORB story, or point to a still-different mechanism. This directly
   falsifies/confirms §2's candidate mechanism and is complementary to
   item 1, not a replacement for it.

3. Only if both (1) and (2) remain inconclusive would I fall back to the
   NOTES.md-proposed brute-force fix (a much wider angular window, ~10×
   the current span, to directly clear the Rayleigh floor) — correct in
   principle but the most FDTD-expensive of the three options, and the
   one that least uses this seat's own charter (phase/frequency-domain
   bookkeeping) to get more information per call.

## Rating: **PARTIAL**

The Combined Verdict NEITHER is honestly earned, not a hedge: G1 passed
exact, both binding preconditions (settling, peak-cell R3) independently
and correctly CONFIRM under my own re-derivation, and the resolution-floor
gate is legitimate wave-physics (a correctly-derived Rayleigh/Fourier
bound, appropriately conservative given the individual per-config fits'
own low R² of 0.43–0.45 leaves no room to claim parametric
super-resolution beyond that bound). This cycle closed real, load-bearing
gaps (settling-closure now genuinely established for C60/C70; both
directions of the trend test now honestly gated) and did not overclaim
past what the data supports. It is not PROMISING (constraint 3 is not
engaged, by design, and T28's causal question is narrowed, not answered)
and not RULED-OUT (nothing here forecloses an ABSORB-tied mechanism —
if anything, §2's saturating-shape observation and the code-level
`_damping` profile give a *more* physically motivated reason to keep
investigating, just not via a linear-in-ABSORB model or via independent
absolute-period fitting). The path forward is concrete and largely
zero-cost: a differential phase-drift re-analysis of data already in
hand, plus one cheap new high-ABSORB config to test saturation.
