# exp-104 — The Sub-Nyquist Standoff Recheck

**Panel Iteration 81. Lead seat (rotation): ELECTROMAGNETISM. Director:
Clyde (photonlab-shift, cloud panel shift).** Reconciled Iteration-81
queue, Tier 1 (Red Team's own top ranking, exp-103 Phase-5 close).
Instrument-repair/recheck cycle — T1: N/A, zero `lab/` diff, no mechanism
proposed or varied.

Full record: `run.py`'s own module docstring (compressed panel record +
all four mandatory Idealizations fixes verbatim), this document's "Panel
record" section below.

## Hypothesis

exp-103 (Panel Iteration 80) rebuilt Gate B and reported a clean,
zero-reversal 16-point standoff trend, but its own Phase-5 review
(PHOTONICS and QUANTUM, independently, by two different routes) found the
"Nyquist fix" it shipped — a ≤10-cell window-spanning sample pitch — does
**not** actually satisfy Nyquist against the λ/2=10-cell coherent-intensity
fringe period it was meant to guard against: the samples land at *exactly*
one full period, the textbook degenerate-aliasing case, not a resolved
one. True Nyquist needs <5-cell spacing. exp-103's own disclosed
`kappa_window` internal spread (pointwise std/mean=0.849, 97× min/max) is
itself evidence that comparable-scale spatial structure exists nearby.
Hypothesis: a genuinely sub-Nyquist recheck — 2-cell pitch across the same
near-field-to-window span, with two independent read channels (an
unchanged 11-cell box average as a "filtered" continuity channel, and a
brand-new zero-averaging single-cell "point" channel ported from exp-102)
— will surface a real, previously-masked ripple in the point channel,
absent (by construction, via low-pass box averaging) from the wide
channel, at a period near the suspected λ/2≈10-cell scale.

## Setup

- **Article/geometry: byte-identical to exp-103's primary pair**, verified
  directly against that file's own committed constants (`experiments/
  103-t28-gateb-footprint-aperture-match/run.py`): `pec_disk`(r=30) +
  `graded_black_shell`(r_in=30, r_out=78, sigma_max=0.5 default), N=560×560,
  cells_per_lambda=20, courant_frac=0.32, absorb=40, SRC_X=64, object
  center (252,280), θ=0° (normal incidence), 600 nm, STEPS=3200.
  `EDGE=TAPER=40` — **not** `R4_TAPER=80** — confirmed by reading
  `experiments/103-.../run.py:102` directly: exp-103's own corrected value
  (the cpl=20-calibrated one), not the Phase-1-proposal-era mistake that
  cycle's own Phase-2 audit already caught and fixed.
- **`kappa_window` footprint (BEHIND)**: x ∈ [357, 457), y ∈ [260, 300) —
  unchanged, byte-for-byte from exp-001/exp-103.
- **`_run()`, `block_mean_intensity`, `kappa_region_at`-equivalent
  machinery reused verbatim** from `experiments/103-.../run.py` wherever
  unchanged. `point_intensity` (single-cell `|Ez|²`, zero averaging) and
  the `delta_phi = angle(mean_a/mean_e)` formula are ported from
  `experiments/102-coherent-downstream-point-intensity/run.py` —
  `point_intensity` at lines 406–407, the `delta_phi` line inside
  `kappa_at` at line 417 (verified by direct read, not merely cited from
  the Phase-1 proposal).
- **DENSE_X = `list(range(352, 457, 2))`** → 53 points, 2-cell pitch,
  spanning the same near-field-gap-to-window range exp-103's 16-point
  `ALL_X` covered at ≤10-cell pitch.
- **Two read channels, same box-ratio convention
  (`|Ez_article|²/|Ez_empty|²`)**:
  - **`H_REGION_WIDE = 5`** (unchanged 11×11 box, exp-103's own
    `H_REGION`) — the "filtered" channel, retained both for continuity
    with exp-103's own 16-point trend (Gate P1 below) and as the smooth
    baseline `residual_point` is measured against.
  - **`H_REGION_POINT = 0`** — literal single Ez cell, zero averaging,
    ported from exp-102's `point_intensity`. This is the channel expected
    to actually surface any sub-Nyquist ripple the box average suppresses.
  - `kappa_region_wide(x)`/`kappa_region_point(x)` computed at all 53
    `DENSE_X` points **and** at the original 16 `ALL_X` points (needed for
    Gate P1).
  - `delta_phi_wide(x)` (exp-102's exact formula, `H_REGION_WIDE` box) at
    the 16 original x-points only. `delta_phi_point(x)` (single-cell) at
    all 53 `DENSE_X` points.
  - Wide-box pointwise spread (std/min/max of the per-cell ratio inside
    each `H_REGION_WIDE` box, mirroring `kappa_window`'s own established
    spread convention, `experiments/103-.../run.py:229–237`) extended to
    each of the 16 original x-points.
- **`FLOOR_FRAC = 0.10`** (unchanged) — applied *separately* to the wide
  channel's own 16-point `i_region_empty` pool (exp-103's own convention,
  reproduced for continuity) and to the point channel's own 53-point
  `i_point_empty` pool.
- **Ripple residual**: `residual_point(x) = kappa_region_point(x) −
  kappa_region_wide(x)` at each of the 53 `DENSE_X` points — the wide
  channel as the smooth/filtered baseline, the residual isolating the
  ripple the box average suppresses.
- **Quintile split (PHOTONICS' adopted chirp-tolerant fix)**: the 53
  `DENSE_X` points split into 5 contiguous quintiles via
  `numpy.array_split` (11, 11, 11, 10, 10 points).
- **Per-quintile period estimation (Red Team's Attack-1 fix)**: FFT of
  each quintile's `residual_point` values, zero-padded to ≥4× the
  quintile's point count, dominant non-DC bin + parabolic/quadratic
  sub-bin interpolation across the 3 straddling bins → a continuous-valued
  period estimate in cells, NOT constrained to even integers (raw
  reversal-position differencing on this fixed 2-cell-pitch grid is
  mathematically confined to even multiples of 2 cells and can never
  surface an odd true period — the defect this fix specifically retires).
  Peak-above-noise criterion: peak non-DC bin power > 3× the median of all
  non-DC bin powers; otherwise the quintile's period is indeterminate
  (`None`).
- **Per-quintile signed suppression-ratio prediction (QUANTUM's refined
  fix)**: `predicted_ratio_i = sinc(11/p_i) / sinc(1/p_i)` (numpy's
  normalized `sinc`, SIGNED, no `abs()`) vs. the measured ratio = signed
  peak-to-peak(`kappa_region_wide`'s own residual from a global cubic
  smooth fit, within quintile i) / peak-to-peak(`residual_point`, within
  quintile i) — sign assigned via the sign of the demeaned correlation
  between the two residual signals within the quintile (a defensible
  simplified proxy for "same phase vs. phase-inverted", analogous to what
  a negative sinc lobe means physically). **Pre-registered exclusion**: if
  `p_i` is within 10% of any integer multiple of 11 cells, that quintile's
  P4 comparison is flagged "near-null, not scored."
- **Sign co-variation check (P5, QUANTUM's fix, simplified proxy stated
  explicitly)**: `delta_phi_wide` is sparse (16 points only, by item-4's
  own scope), so a rigorous same-frequency-bin phase decomposition against
  a densely-sampled reference isn't available. Adopted proxy: linearly
  interpolate `delta_phi_wide` (unwrapped across the 16 sparse points)
  onto the `DENSE_X` grid, form a phase-ripple residual =
  `delta_phi_point(x) − interpolated delta_phi_wide(x)` within each
  quintile, and take `sign(correlation(residual_point, phase-ripple
  residual))` as the proxy sign, compared against `sign(predicted_ratio_i)`.
  Stated exactly as computed — not fabricated to a false precision.
- **Call budget: exactly 2** real FDTD calls (empty + article, θ=0°,
  STEPS=3200 only — **no `STEPS_2X` leg this cycle**, see Idealizations).
- **`lab/` diff: zero.** All new code lives in this experiment's `run.py`.

## New trust-suite stage: N/A this cycle

Reuses only already-gated primitives (`Sim`, `materials.pec_disk`/
`graded_black_shell`, `sc.full_capture`/`phasors`) in a new post-processing
configuration; no new absolute-identity gate proposed. `lab/validation/
run_all.py --only 12346789` re-confirmed green both before and after this
cycle's own diff (which is zero).

## Predictions (committed to git BEFORE Phase 4 runs any FDTD call — house
## discipline, non-negotiable; generated verbatim from `run.py`'s own
## `PREDICTIONS_TEXT`, R23 — not hand-typed)

```
PREDICTIONS (pre-registered, exp-104, Panel Iteration 81)

Raw physical intensity/phase ratios only -- no Weber-contrast or C_thr(L) perceptual scoring is performed this cycle; not a claim about human visibility.

**P1 (reproducibility gate, absolute identity check).** kappa_region_wide(x)
at the 16 original x-points (ALL_X, reproduced verbatim from exp-103's own
NEAR_FIELD_X+WINDOW_SPAN_X) reproduces experiments/103-.../results.json's
kappa_region_trend to <1e-9 relative. This is the run's precondition -- if
it fails, halt and report the defect rather than proceeding to trust P2-P6.

**P2 (ripple existence).** residual_point(x) = kappa_region_point(x) -
kappa_region_wide(x), at each of the 53 DENSE_X points (2-cell pitch,
x=352..456), shows >=2 sign changes (local reversals) with amplitude >5%
relative to the local kappa_region_wide value, across the full 53-point
span. Predicted CONFIRMED, citing exp-103's own disclosed kappa_window
pointwise spread (std/mean=0.849, 97x min/max) as evidence of nearby
comparable-scale structure -- that ripple is not present in the wide-box
trend (VISION's Phase-2 wording fix: "not present in", not "NOT visible
in").

**P3 (per-quintile period match, PHOTONICS' chirp-tolerant fix).** The 53
DENSE_X points are split into 5 contiguous quintiles (numpy.array_split,
~10-11 points each). In each quintile where a period is determined (FFT of
that quintile's residual_point, zero-padded to >=4x its point count,
dominant non-DC bin + parabolic sub-bin interpolation; peak power >3x the
median non-DC bin power, else indeterminate/None), the estimated period
falls in [7,13] cells. Predicted: at least 3 of 5 quintiles determine a
period in this band -- chirp across quintiles is expected and does NOT
falsify this prediction; a per-quintile band match does.

**P4 (signed suppression-ratio cross-check, QUANTUM's refined fix).** For
each quintile with both a determined period AND not near-null-excluded
(pre-registered exclusion below), predicted_ratio_i =
sinc(11/p_i)/sinc(1/p_i) (numpy's normalized sinc, SIGNED, no abs()) is
compared against the measured ratio = signed peak-to-peak(kappa_region_
wide's own residual from a smooth global fit, within quintile i) /
peak-to-peak(residual_point, within quintile i) -- sign assigned via the
sign of the (demeaned) correlation between the two residual signals within
the quintile (a defensible simplified proxy for "same phase vs. inverted
phase", analogous to what a negative sinc lobe means physically: the
11-cell box average phase-inverts a period this short relative to a
1-cell point sample). Pre-registered exclusion: if p_i is within 10% of
any integer multiple of 11 (min(|p_i-11k|)/11 < 0.10 for integer k>=1),
that quintile's P4 comparison is flagged "near-null, not scored" rather
than forced into pass/fail. Predicted CONFIRMED for at least 2 of
however-many non-excluded quintiles exist: sign(predicted_ratio_i) matches
the measured ratio's sign, AND |predicted_ratio_i| is within a factor of
2x of |measured ratio_i| (loose magnitude tolerance, justified by
quintile-scale amplitude estimation being crude with ~10 points).

**P5 (delta_phi co-variation, QUANTUM's fix, simplified proxy).**
delta_phi_wide(x) (exp-102's angle(mean_a/mean_e) formula, H_REGION_WIDE
box) is computed only at the 16 sparse original x-points (item 4's own
scope); delta_phi_point(x) is computed at all 53 DENSE_X points. A rigorous
same-frequency-bin phase decomposition against a densely-sampled delta_phi_
wide is not available (delta_phi_wide is sparse by construction), so the
adopted simplified proxy is: linearly interpolate delta_phi_wide (unwrapped
across the 16 sparse points) onto the DENSE_X grid, form a phase-ripple
residual = delta_phi_point(x) - interpolated delta_phi_wide(x) within each
quintile, and take sign(correlation(residual_point, phase-ripple residual))
as the proxy sign, compared against sign(predicted_ratio_i). This
substitutes a correlation-sign covariation check for a rigorous per-
frequency-component phase comparison -- stated exactly as computed, not
fabricated to a false precision. Predicted: directionally consistent (same
sign) in a majority of quintiles where both P3 and P4 are determined.

**P6 (scope, Red Team's numeric threshold, Attack 2 fix).**
ripple_fraction_i = peak-to-peak(residual_point in quintile i) /
mean(kappa_region_wide in quintile i). "Narrows" exp-103's own framing:
ripple_fraction_i <= 0.20 in ALL 5 quintiles. "Overturns": ripple_fraction_i
> 0.50 in ANY quintile. Between 0.20 and 0.50 in one or more quintiles
(none exceeding 0.50): reported as "MIXED/PARTIAL narrowing," not forced
into either bucket. Predicted: NARROWS (all quintiles <=0.20) -- because
kappa_window/exp-103's own Prediction-3 span-consistency result are wide-
window averages insensitive to ripple phase and are predicted to reproduce
unchanged (via kappa_region_wide at the retained 16 points, to P1's <1e-9
tolerance).

Mandatory Idealizations fixes (MATERIALS, THERMODYNAMICS, settling-leg
scope, QUANTUM citation correction) are stated in full in this file's
module docstring and in NOTES.md's Idealizations section verbatim.
```

## Idealizations

- 2D FDTD, single wavelength (600 nm), normal incidence only (θ=0°); no
  dispersion, no broadband claim.
- Near-field-only standoff range sampled (x=352–456); no far-field
  extrapolation is claimed or implied.
- PEC core treated as ideal; `graded_black_shell` is the program's already
  established **UNOBTAINIUM-WITH-PARAMETERS** idealized article,
  unchanged by this cycle.
- **MATERIALS' mandatory fix (verbatim, this cycle's own P2 ripple)**: Any
  P2 ripple found in `residual_point(x)` is necessarily numerical/aliasing
  in origin — a consequence of grid-sampling this idealized, continuously-
  graded article, which has no discrete layer structure — and is NOT
  evidence bearing on the layer-tied ripple signature a realizable,
  discretely-graded coating would add per exp-103's own restored
  Realizability Bound. `graded_black_shell` remains
  UNOBTAINIUM-WITH-PARAMETERS, unchanged.
- **THERMODYNAMICS' mandatory fix (verbatim)**: Thermal sidecar: N/A this
  cycle — no `thermo_sidecar.py` call, no new `sigma_ext`/`ratio_abs_ext`
  measured. `H_REGION_POINT=0` point samples are peak local downstream
  |Ez|² in a coherent-superposition zone, NOT an incident-intensity-on-
  object quantity, and are not thermally interpretable without a separate
  aperture-integration step not attempted here.
- **Settling-leg scope (Red Team Attack 4, mandatory fix)**: this cycle
  runs NO fresh `STEPS_2X` leg. "Settling already established clean" rests
  on exp-103's own check at x∈[352,356] only (a 4-cell span, 5 points) —
  NOT independently verified across the full 104-cell dense span out to
  x=456. Skipping a fresh settling leg this cycle relies on the general
  physical argument (settling error decreases monotonically with
  standoff, EM's own prior finding, exp-103 Prediction 4) rather than
  direct measurement at the farther points. This is an explicit
  idealization, not an implied full-span verification.
- **QUANTUM's citation-overreach correction (Red Team Attack 5, mandatory
  fix)**: the `H_REGION_WIDE=5` (11-cell) box-width sinc-null hazard used
  in the P4 suppression-ratio prediction is NOT "structurally identical"
  to exp-103's own original pitch-aliasing defect — it is analogous in
  EFFECT (both mask ripple amplitude) but mechanistically DISTINCT (a
  low-pass filter null vs. a sampling-rate failure). Stated that way
  throughout, not conflated.
- Call budget: exactly 2 real FDTD calls this cycle (down from exp-103's
  4) — the settling-independence leg is not re-run (see above), so this
  cycle spends its entire budget on the dense-standoff/quintile
  machinery.

## R23 — new standing house rule (ratified and IMPLEMENTED this cycle)

Red Team's proposed text, adopted verbatim: a disclaimer required in
multiple document sections must be enforced by a code-level assert on a
single source-of-truth string, not manual prose-carrying-forward (this
exact drift pattern has recurred 8 times on this T28 sub-thread, most
recently exp-103's own Phase-5 catch). Implemented in `run.py`: a single
`DISCLAIMER` string constant, `PREDICTIONS_TEXT`/`RESULT_TEXT` generated
as Python strings from code (not hand-typed), and two hard asserts
(`assert DISCLAIMER in PREDICTIONS_TEXT`, `assert DISCLAIMER in
RESULT_TEXT`) — a future 9th recurrence is now a hard run failure, not a
review-time catch. This document's own Predictions section above (and its
Result section, once Phase 4 runs) is pasted verbatim from those generated
strings' actual printed output, per the same discipline.

## Panel record

**Phase 1 (exp-103's own Phase-5 close, Reconciled Iteration-81 queue,
Tier 1)**: exp-103's own <10-cell window-spanning standoff pitch was
Phase-5-flagged as failing to satisfy Nyquist against the λ/2=10-cell
coherent-intensity fringe period it was meant to guard against — samples
land at exactly one full period (textbook degenerate aliasing), not a
resolved one; true Nyquist needs <5-cell spacing. ELECTROMAGNETISM (this
cycle's lead seat) proposed the Tier-1 fix: a genuinely sub-Nyquist
recheck.

**Phase 2 (five blind critiques, all support-with-changes, distinct
concrete flip conditions)**:
- **PHOTONICS**: chirp-tolerant per-quintile period estimation instead of
  a single global period fit (a fixed period across the full 104-cell span
  is not physically guaranteed) — ADOPTED (items 8–9 above).
- **MATERIALS**: any ripple found is necessarily a numerical/aliasing
  artifact of the idealized continuously-graded article, not evidence
  about a realizable discretely-layered coating's own ripple signature —
  ADOPTED verbatim (Idealizations above).
- **THERMODYNAMICS**: the new zero-averaging point channel's peak local
  |Ez|² must be explicitly disclaimed as NOT a thermally-interpretable
  incident-intensity quantity — ADOPTED verbatim (Idealizations above).
- **QUANTUM OPTICS**: a signed (not `abs()`'d) suppression-ratio
  prediction from the 11-cell box's own sinc transfer function, plus a
  `delta_phi` co-variation cross-check — ADOPTED, refined (items 10–11
  above; P5's simplified proxy stated explicitly per QUANTUM's own "do not
  fabricate a false precision" caution).
- **VISION SCIENCE**: P2's wording ("NOT visible in the wide-box trend" →
  "not present in the wide-box trend") — a perceptual-language leak into a
  raw-physical-ratio claim — ADOPTED (see `PREDICTIONS_TEXT` above).

**Red Team's audit**: independently re-verified every sharpest claim from
primitives (recomputed the sinc math itself, checked the geometry, checked
the code) and **ADOPTED ALL FIVE flip conditions** — none overridden.
Raised 2 additional attacks of its own:
- **Attack 1 (P3 grid-quantization artifact)**: raw reversal-position
  differencing on the fixed 2-cell-pitch `DENSE_X` grid is mathematically
  confined to even multiples of 2 cells and can never surface an odd true
  period — fixed via per-quintile FFT + parabolic sub-bin interpolation
  instead (item 9 above), which is NOT constrained to even integers.
- **Attack 2 (P6 lacking a numeric threshold)**: "narrows/overturns" was
  previously qualitative — fixed via the explicit `ripple_fraction_i`
  ≤0.20 / >0.50 numeric bands (P6 above).
- **Attack 4** (folded into the settling-leg scope Idealizations fix
  above) and **Attack 5** (folded into the QUANTUM citation-overreach
  correction above) are also mandatory fixes this cycle, per Red Team's
  own numbering.

**Checkpoint criterion 4 ruling**: does **NOT** fire this cycle — both live
sub-issues (the disclaimer-erosion recurrence pattern that motivated R23,
and the Nyquist-overclaim prose that motivated this whole cycle) were
caught **blind, before freeze** — the discharge-test precedent holds
unbroken.

**R23 adopted**: see the section above — ratified AND implemented this
cycle, not merely described (Red Team's own explicit condition for
counting it as discharged).

**Attack-7 reconciliation**: already folded into items 8–10 above —
per-quintile period feeds per-quintile P4 ratio; PHOTONICS' and QUANTUM's
fixes are composed, not left in conflict.

## LOGBOOK.md RULED OUT registry / standing rules check

No item in LOGBOOK's RULED OUT registry (R1–R22) is re-proposed: no
mechanism or material parameter is touched (not R1); no named-constant
search is performed (not R5); the floor-gate convention matches exp-102/
exp-103's own established formula exactly on the wide channel, and applies
the same RMS-pool convention (not a new formula) to the new point channel
(not R5/R17); the R22 sign-convention rule does not directly apply (kappa
ratios are non-negative by construction) though the new *signed*
suppression-ratio prediction (P4) and the phase co-variation proxy (P5)
are new vector/sign-bearing quantities, handled with explicit, disclosed
sign conventions rather than an implicit assumption — consistent with
R22's spirit, not a violation of its letter (R22 itself governs a
different, already-closed self-consistency identity). No closed Live
Thread claim is re-litigated: T8's near-field caveat is unaffected; T28's
own `delta_scene`/R3-vs-R4 split remains untouched — this experiment does
not read, cite, or score `delta_scene`/`frac_contrast`/`ratio_k` at all
(now a fifth consecutive deferral if Iteration 82 does not address it,
per exp-103's own explicit written warning).

## Phase 3 — Director's synthesis: accepted / overridden criticisms

**All five Phase-2 flip conditions ACCEPTED, zero overridden** (per Red
Team's own independent re-verification from primitives). **Both Red Team
attacks (1, 2) ACCEPTED**, plus Attacks 4 and 5 folded into the
Idealizations fixes above. **R23 ratified and implemented this cycle.**
Predictions above are committed to git in this same commit as this
synthesis, strictly BEFORE `run.py`'s first real Phase-4 invocation.

## Result

**Pasted verbatim from `run.py`'s own generated `RESULT_TEXT` (R23
discipline — not hand-typed):**

```
RESULT (exp-104, Panel Iteration 81)

Raw physical intensity/phase ratios only -- no Weber-contrast or C_thr(L) perceptual scoring is performed this cycle; not a claim about human visibility.

All 2 real FDTD calls executed exactly as budgeted (theta=0, STEPS=3200),
58.7s (0.98 min) total wall time, zero `lab/`
diff throughout.

**Gate P1 (reproducibility identity check): PASS.**
max relative deviation = 0.000e+00 across all 16 original x-points,
against experiments/103-.../results.json's own kappa_region_trend
(<1e-9 required). This is the run's precondition; P2-P6 below are only
trusted because Gate P1 passed.

**P1: CONFIRMED.**

**P2 (ripple existence): FALSIFIED.** 0 qualifying sign
changes (>5% relative amplitude) found in residual_point(x) across the
full 53-point DENSE_X span (>=2 required).

**P3 (per-quintile period match): FALSIFIED.** 5/5
quintiles determined a period; 1 of those fall in [7,13]
cells (>=3 required). Per-quintile periods: [(0, 32.540162151563344), (1, 32.46870463306552), (2, 32.55833657701957), (3, 29.384689967054342), (4, 9.06634619846641)].

**P4 (signed suppression-ratio cross-check): FALSIFIED.**
2 quintile(s) scorable (determined period, not
near-null-excluded); 1 pass (sign match + magnitude within
2x) (>=2 required, or AMBIGUOUS if zero are scorable). Near-null-excluded
quintiles (period within 10% of an integer multiple of 11 cells): [0, 1, 2].

**P5 (delta_phi co-variation, simplified proxy): CONFIRMED.**
2/2 scorable
quintiles (both P3 and P4 determined) show sign-consistent covariation
between residual_point and the delta_phi_point-vs-interpolated-delta_phi_
wide phase-ripple residual (majority required). Proxy computed exactly as
pre-registered in PREDICTIONS_TEXT -- no rigorous per-frequency-bin phase
decomposition was attempted (delta_phi_wide is sparse by construction,
only the 16 original x-points).

**P6 (scope, narrows/overturns/mixed): NARROWS.** Per-quintile
ripple_fraction_i (peak-to-peak(residual_point)/mean(kappa_region_wide)):
['0.1380', '0.0730', '0.0614', '0.0337', '0.0095']. Narrows requires all <=0.20;
overturns requires any >0.50.

Mandatory Idealizations fixes (MATERIALS' aliasing-origin disclaimer on any
P2 ripple found here, THERMODYNAMICS' thermal-sidecar N/A disclosure, the
settling-leg scope correction, and QUANTUM's citation-overreach correction
distinguishing a low-pass filter null from a sampling-rate failure) are
carried unchanged from this file's own module docstring and NOTES.md's
Idealizations section -- restated in full there, not narrowed or dropped
here.
```

**Interpretation, not a modification of the scored verdicts above.** P2's
FALSIFIED result is itself the headline finding, not a null result to
explain away: at genuinely sub-Nyquist 2-cell pitch, with a zero-averaging
single-cell point channel specifically built to surface any ripple an
11-cell box average would suppress, **no qualifying (>5%-amplitude,
sign-changing) ripple was found anywhere across the full 104-cell dense
span**. This directly answers the concern that motivated this whole
cycle: exp-103's own Phase-5-flagged degenerate-aliasing risk (samples at
exactly the λ/2≈10-cell period) does not, on this genuinely resolved
recheck, turn up the ripple it could have been masking.

The P3/P4 FALSIFIED periods are consistent with this reading, not in
tension with it: three of five quintiles' FFTs locked onto periods near
32.5 cells — close to **3×11=33 cells**, triggering the pre-registered
near-null exclusion — and the two non-excluded quintiles' periods (29.4
and 9.1 cells) are not a coherent, chirp-consistent λ/2-scale signal
either. A period longer than the quintile's own ~20-cell span is the
signature of `estimate_period` locking onto the smooth curvature mismatch
between a point sample and an 11-cell box average of the same underlying
smooth Fresnel-fill-in trend (a Taylor-expansion-scale artifact, not a
periodic ripple) rather than any real coherent fringe. This is a genuine,
honestly-reported null result, not a forced pass — MATERIALS' own
Idealizations fix above already pre-registered that *any* ripple found
this cycle would be aliasing/numerical in origin, not physically
interpretable; the actual finding is stronger still: no ripple, real or
artifactual, was found in the first place.

P5's CONFIRMED (2/2) and P6's NARROWS are consequences of the same
underlying finding: with no genuine ripple present, the wide/point
channels' residuals are small, smoothly-varying, and mutually consistent
in sign by construction (P5's proxy), and `ripple_fraction_i` stays well
under the 0.20 "narrows" bar in all 5 quintiles (max 0.138, in the
near-object Q0). **Overall scope disposition: NARROWS** — exp-103's own
16-point trend and `kappa_window` figure are reproduced unchanged (Gate
P1, exact to machine precision) and no sub-Nyquist ripple hazard
materializes at the resolution this cycle was built to check.

## Learned

1. **A genuinely sub-Nyquist recheck can falsify the very concern that
   motivated it, and that is itself the useful result.** exp-103's Phase-5
   review correctly identified a real methodological gap (the ≤10-cell
   pitch does not satisfy Nyquist against a λ/2=10-cell period); this
   cycle closed that gap with a real 2-cell-pitch, zero-averaging-channel
   recheck and found P2 (ripple existence) FALSIFIED — no comparable-scale
   coherent structure actually exists in this quantity at this geometry,
   despite the internal spread `kappa_window` itself disclosed
   (std/mean=0.849) being real. The two facts are not in tension:
   `kappa_window`'s spread is measured over a much larger 100×40-cell
   footprint (real spatial variation across that whole window, much of it
   at longer length scales than λ/2) while `residual_point` isolates
   specifically the wide-vs-point *channel* difference at the λ/2 scale —
   a different question than "does the field vary spatially," which it
   plainly does.
2. **A per-quintile FFT period estimator needs its own near-null
   discipline to avoid mistaking a smooth-curve artifact for a genuine
   period** — three of five quintiles' dominant FFT peaks landed near
   3×11=33 cells (an exact near-null of the 11-cell box width), which is
   far more likely to be a numerical beat between the point-vs-box
   curvature mismatch and the FFT's own zero-padded frequency grid than a
   physical period; the pre-registered near-null exclusion (item 10)
   correctly caught this and excluded those quintiles from P4 scoring
   rather than forcing a spurious signed-ratio comparison on them. A
   useful house lesson for any future per-quintile period-fit machinery:
   always check whether an estimated "period" is actually shorter than
   the window it was estimated from before trusting it as a real
   oscillation.
3. **R23's assert-based discipline worked exactly as designed, with zero
   manual transcription drift.** Both `PREDICTIONS_TEXT` (committed before
   any FDTD call) and `RESULT_TEXT` (generated after) were pasted into
   this document verbatim from `run.py`'s own printed output — the two
   `assert DISCLAIMER in ...` calls in `run.py` passed on the actual run,
   confirmed by inspection of the generated strings above, not merely by
   the code not crashing.

## Next (candidate directions, not this cycle's scope)

1. **Tier 1 item 3 (T8 r=78/156/312 near-field-to-witness-scale bridge
   extension)** — deferred again this cycle (this cycle's own scope was
   the sub-Nyquist recheck, not the bridge extension); now the object of
   Iteration 82's own queue per exp-103's Phase-5 tiering, since this
   cycle's recheck is the "ratified sampling convention" that extension
   was sequenced to inherit. The genuine finding here (no sub-Nyquist
   ripple at this geometry) is a reasonable basis to proceed with that
   extension using the same wide-channel convention, without needing to
   re-litigate pitch/Nyquist concerns at the bridge-family radii.
2. **Tier 3 — the standing `delta_scene` R3-vs-R4 split** — now FIVE
   consecutive deferrals (exp-100→101→102→103→104); per exp-103's own
   explicit written warning, this should be treated as a rule violation
   rather than routine unless Iteration 82 either executes it or
   re-justifies a sixth deferral in writing.
3. A genuine multi-step-count settling convergence bench across the full
   dense span (not just x∈[352,356]) remains open — this cycle's own
   settling-leg-scope Idealization explicitly flags that the farther
   `DENSE_X` points (out to x=456) were never directly settling-checked,
   only argued from the general monotonic-decay-with-standoff physical
   claim.
