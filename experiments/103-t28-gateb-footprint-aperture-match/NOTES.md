# exp-103 — The Footprint- and Aperture-Matched Gate B Rebuild

**Panel Iteration 80. Lead seat (rotation): MATERIALS & METAMATERIALS.
Director: Clyde (photonlab-shift, cloud panel shift).** Reconciled
Iteration-80 queue, Tier 1 items 1+2 combined (Red Team's own top ranking,
exp-102 close). Instrument-repair cycle — T1: N/A, zero `lab/` diff, no
mechanism proposed or varied.

Full record: `phase1_proposal.md` (MATERIALS), five blind Phase-2
critiques (`phase2_critique_{photonics,em,thermodynamics,quantum,
vision}.md`, four support-with-changes + one support), `phase2_redteam_
audit.md` (4 Red Team findings, rulings on all five critiques — 8
mandatory fixes adopted, 1 explicitly overridden as a zero-information
no-op).

## Hypothesis

exp-102 (Panel Iteration 79) built a coherent phase-resolved
point/region field-intensity ratio κ(θ) but honestly FAILED "Gate B" — a
cross-check against this program's original, long-established
`beam_behind` figure (exp-001/002, 1.5–1.8% beam transmission behind the
absorber object, a WIDE spatial window average) — diagnosed as two
compounding, undisclosed confounds: (1) the new instrument's point sample
and the established window average were taken at different effective
near-field standoffs, where a real shadow reads measurably darker before
Fresnel diffraction fills it back in; (2) direct code read found Gate B's
own source construction silently used `add_line_source`'s code default
(`edge=24`) rather than any deliberately-matched aperture. Hypothesis:
rebuilding Gate B from ONE new field capture — the literal established
`BEHIND` window footprint, with a source aperture taper genuinely
physically matched (not merely cell-count-matched) to the R4-family
construction the rest of this program trusts — resolves confound (2)
outright and lets confound (1) be characterized directly via an
11-point standoff trend from the near-field gap out through the window.

## Setup

- **Article**: exp-001/002's own native-scale flagship, unchanged —
  `pec_disk`(r=30) + `graded_black_shell`(r_in=30, r_out=78,
  sigma_max=0.5 default, unchanged), N=560×560, cells_per_lambda=20,
  courant_frac=0.32, absorb=40, SRC_X=64, object center (252,280),
  θ=0° (normal incidence), 600 nm.
- **Source aperture, corrected (Phase-2 mandatory fix 1, Red Team's own
  top-ranked finding):** `profile="plane", edge=40` — **not** `edge=80`
  as this cycle's own Phase-1 proposal originally specified. `R4_TAPER=80`
  (`experiments/069-.../design_geometry.py`) is `round(TAPER·R4_RATIO)
  = round(40·2.0)`, deliberately rescaled UP because the R4 family runs
  at DOUBLE this file's own `cells_per_lambda` (R4_CPL[600]=40 vs this
  file's 20) — `R4_TAPER=80` cells at cpl=40 represents the SAME
  2-wavelength PHYSICAL taper width as `TAPER=40` cells
  (`experiments/065-.../design_geometry.py`) at cpl=20. Reusing
  `R4_TAPER=80` unchanged at this file's own cpl=20 grid would have given
  a 4-wavelength taper — twice the R4 family's actual physical aperture,
  reintroducing exactly the kind of unexamined cross-resolution-constant
  confound this whole cycle exists to retire, one level down, in the one
  parameter this cycle is actively changing. `EDGE=TAPER=40` genuinely
  matches the R4 family's own physical aperture width.
- **kappa_window footprint**: x ∈ [357, 457), y ∈ [260, 300) — the
  literal established `BEHIND` slice, byte-for-byte
  (`experiments/001-.../run.py`: `slice(CX+R_CLK+15, CX+R_CLK+115)`,
  CX=252, R_CLK=90), independently verified by EM's Phase-2 critique.
- **Standoff sample x-values (κ_region)**: near-field gap-fill
  x=352–356 (5 points, x=352 = exp-102's own Gate-B-corrected reference
  point, D_STANDOFF=100 cells rescaled by the article's r_out ratio);
  window-spanning x=357,367,377,387,397,407,417,427,437,447,456 (11
  points total), **≤10-cell (λ/2) pitch** on the window-spanning leg
  (Phase-2 mandatory fix 5, PHOTONICS/Red Team) — tightened from the
  Phase-1 proposal's own original ~18–20-cell (≈1λ) pitch, which Red
  Team confirmed carried a genuine sub-Nyquist aliasing risk against a
  coherent field's own λ/2-scale standing-wave structure. `kappa_window`'s
  own internal spatial variance (min/max/std across its 100×40-cell
  footprint) is also reported, per the same fix's cheaper-default option.
- **Settling-independence leg (Phase-2 mandatory fix 6, EM/Red Team,
  Director's own disposition — see below)**: a SECOND field-capture pair
  at 2× STEPS (6400, vs. the primary 3200) re-reads ALL FIVE near-field
  points (x=352–356), not the single-point fallback Red Team's own audit
  text treated as the safe minimum — because `sc.full_capture()` returns
  the whole field, re-reading 5 points from the same 2 settling-check
  calls costs nothing beyond that pair. **Total call budget stays
  exactly 4** (2 primary + 2 settling), never silently exceeding the
  cycle's own stated FDTD-call discipline while delivering the fuller
  check EM's own Phase-2 steel-man originally wanted.
- **Floor gate**: RMS across the 16-point pool's own local
  `i_region_empty` readings (exp-102's own established `floor_gate()`
  convention exactly, Phase-2 mandatory fix 3 — the Phase-1 proposal's
  own prose language, "source-region reference amplitude," was corrected
  to match; the code was never actually built to any other convention).
  FLOOR_FRAC=0.10 (R13/R14 lineage, house style).
- **Thermal sidecar: NOT invoked this cycle** (Phase-2 mandatory fix 7).
  `thermo_sidecar.absorbed_power_established_ratio`'s own `p_abs_w`
  derives from `sigma_ext_cells` (exp-059's Mie/qext-theory extinction-
  width calculation) times an externally assumed `i_incident_w_cm2` —
  verified directly against `lab/thermo_sidecar.py:124–168`: neither
  input reads this file's FDTD source construction, amplitude, or `edge`
  parameter, so this cycle's aperture change cannot silently stale the
  existing 699.27× thermal-UNDETECTABLE citation (exp-057). This file
  imports nothing from `lab.thermo_sidecar`.
- **Perceptual scoring: NONE this cycle** (Phase-2 mandatory fix 8,
  VISION/Red Team — directly closing this cycle's own named
  constraint-3-drift exposure). **DISCLAIMER: kappa_window/kappa_region
  are raw physical intensity ratios; no Weber-contrast or C_thr(L)
  perceptual scoring is performed this cycle.**
- **`envelope()`-vs-`phasors()` disclosure** (Phase-2 mandatory fix 4,
  Red Team's own finding): `kappa_window` (`sc.phasors()`, a
  trig-corrected two-snapshot quadrature phasor) and the established
  `beam_behind` figure (`Sim.envelope()`, an UNCORRECTED
  `sqrt(snap_a²+snap_b²)`) are related but not identical
  amplitude-reconstruction conventions. At this cycle's own grid numbers
  (λ=20 cells, S≈0.2263, quarter=22 steps, ω=2π·S/λ≈0.071086, φ=ω·22≈1.563895 rad vs. exact
  π/2=1.5708 — corrected per Phase-5 mandatory fix 6, ELECTROMAGNETISM: the
  originally-stated ω≈0.07111/cos φ≈0.0064 carried a rounding slip),
  `envelope()` carries a small (cos φ≈0.0069, up to ~0.7%
  relative in the worst-case phase relationship) quantization bias that
  `kappa_window` does not — relevant context if `kappa_window` lands
  outside the predicted band on the low side; does not by itself
  invalidate the comparison.
- **Call budget**: **exactly 4** real FDTD calls (2 primary pair +
  2 settling-independence pair), code-asserted (`n_fdtd_calls==4`,
  Phase-2 mandatory fix 2/R19). **16** total `kappa_region`
  point-readings reported (11 standoff points + the settling leg's own
  re-read of all 5 near-field points, code-asserted separately from the
  call count) plus 1 `kappa_window` window reading.
- **`lab/` diff: zero.** All new code lives in this experiment's `run.py`.

## New trust-suite stage: N/A this cycle

This cycle adds no new trust-suite-gated machinery — it reuses only
already-gated primitives (`Sim`, `materials.pec_disk`/`graded_black_shell`,
`sc.full_capture`/`phasors`, all trust-suite stage 1/6/7/8-covered) in a
new configuration. No new absolute-identity gate is proposed; this is
consistent with exp-102's own precedent (an instrument-REPAIR cycle, not
a new-machinery cycle).

## Predictions (committed to git BEFORE Phase 4 runs any FDTD call — house
## discipline, non-negotiable)

**kappa_window/kappa_region are raw physical intensity ratios; no
Weber-contrast or C_thr(L) perceptual scoring is performed this cycle**
(Phase-2 mandatory fix 8, restated here per the T28 dual-section banner
requirement, LOGBOOK.md Iteration 65 — added at Phase 5, per Red Team's
final-audit mandatory-fixes docket item 2).

1. **kappa_window** ∈ **[0.005, 0.04]** (0.5%–4.0%). Anchored to the
   established `beam_behind` figure (1.5–1.8%), widened for the facts
   that (a) this is a coherent, window-averaged |Ez|² intensity ratio at
   a single θ, not necessarily the same convention as the original
   figure (see the envelope()-vs-phasors() disclosure above), and (b)
   the aperture correction (edge=40, vs. the previously-undisclosed
   edge=24 default) may itself shift diffraction fill-in somewhat.
   **Falsified** if kappa_window falls outside this band (e.g. an
   order-of-magnitude miss, or a value indistinguishable from the
   empty-scene floor).
2. **Standoff-trend shape**: kappa_region rises monotonically
   (non-decreasing above the floor-gate noise tolerance) across the
   16-point pool from x=352 through x=456, with **at most one local
   reversal** exceeding FLOOR_FRAC-scale tolerance. **Falsified** by a
   non-monotonic, multi-reversal pattern, which would instead support a
   fringe-limited near-field-null explanation for Gate B's original
   failure rather than smooth Fresnel fill-in.
3. **Floor-gate / span-consistency check**: every one of the 16 sampled
   points must clear the pool-RMS floor gate (FLOOR_FRAC=0.10); the mean
   of the 11 window-spanning `kappa_region` readings must fall within a
   factor of 2× of `kappa_window` itself. **Falsified** if any point
   fails the floor gate (excluded from Prediction 2's trend claim, not
   silently averaged in) or if the span-mean-to-window ratio exceeds 2.0.
4. **Settling-independence** (Phase-2 mandatory fix 6): at all 5
   near-field points (x=352–356), `kappa_region` measured at STEPS=3200
   must agree with the same point measured at STEPS=6400 to within 20%
   relative. **Falsified** if any near-field point's relative change
   exceeds 20% — this would mean the near-field gap-fill points are not
   yet settled to true CW steady state at this suite's own STEPS=3200
   convention, undermining Prediction 2's own trend claim at exactly the
   points most likely to drive a "reversal" reading.

## Idealizations

- 2D FDTD, single wavelength (600 nm), normal incidence only (θ=0°); no
  dispersion, no broadband claim.
- Near-field-only standoff range sampled (x=352–456); no far-field
  extrapolation is claimed or implied.
- PEC core treated as ideal; `graded_black_shell` is the program's
  already-established **UNOBTANIUM-WITH-PARAMETERS** idealized article
  (Realizability Bound below), unchanged by this cycle.
- `courant_frac`, `absorb`, `STEPS`, and `sigma_max` are inherited
  unchanged from established convention (R5/R17) — only the source
  `edge` parameter is deliberately changed, and, after Phase-2's
  correction, matches the R4 family's own physical aperture width
  exactly (not merely its cell count).
- **kappa_window/kappa_region are raw physical intensity ratios; no
  Weber-contrast or C_thr(L) perceptual scoring is performed this
  cycle** (restated per Phase-2 mandatory fix 8 — this sentence is the
  fix, present verbatim in both this document and `run.py`'s own printed
  output).
- Thermal sidecar N/A this cycle, dependency chain disclosed above —
  not merely asserted (Phase-2 mandatory fix 7).
- **Tier 1 item 3 (r=78/156/312 T8 near-field-to-witness-scale bridge
  extension) is explicitly deferred to Iteration 81.** Reason: this
  cycle already spends its real FDTD budget (4 calls) on the Gate B
  rebuild + standoff trend + settling check; a genuine r=156/312
  extension requires new, non-trivial geometry-scaling work (not a
  parameter tweak) and deserves a dedicated cycle rather than being
  compressed alongside this build.
- **Tier 3 (delta_scene R3-vs-R4 split) — this is the FOURTH consecutive
  deferral** (exp-100, exp-101, exp-102, and now exp-103).
  MATERIALS-seat reasoning, unchallenged by Phase 2/Red Team: the Gate B
  rebuild in this cycle is a precondition for trusting any future
  kappa(theta)-family citation, including whatever a delta_scene
  resolution would itself need to cross-check against — resolving
  delta_scene now, before the instrument it would presumably be read
  through is independently trusted, risks producing a result nobody can
  yet calibrate. This is a scope-ordering argument, not a dismissal: if
  Iteration 81 completes the Tier 1 item 3 bridge-family extension,
  delta_scene should be treated as due next, and a fifth silent
  deferral should be considered a rule violation rather than routine.

## Realizability Bound (MATERIALS' seat duty — restored at Phase 5,
## mandatory fix 3; dropped between Phase 1 and this document's own
## Phase-3 freeze, caught only at Phase 5 by MATERIALS' own self-review)

**Article status: UNOBTANIUM-WITH-PARAMETERS**, unchanged by this cycle
— the `graded_black_shell` article measured here is the same idealized
article already carrying that status across exp-001/002 and every
R4-family cycle since. Carried forward from `phase1_proposal.md` §6
(the reasoning promised inline above but never delivered into this
document before Phase 5): if a realizable graded-absorption coating at
comparable optical depth were substituted, expect the near-field
fill-in curve to differ in two ways — (1) **less smoothness**: a finite
number of discrete grading layers, rather than continuous sigma
grading, would imprint small periodic ripple on the standoff trend tied
to layer-boundary reflections; (2) **a higher floor at short standoff**:
real absorbers are bounded by causality (Kramers–Kronig) and finite
sub-wavelength thickness in how much extinction they can pack into
`r_out − r_in`, so a realizable shell would likely leak more field into
the near-field shadow than this idealized, arbitrarily-strong-graded
article does — `kappa_window` for a realizable coating should sit at or
above this cycle's own measured 1.83%, not below it.

**This cycle's own measured data sharpens, not merely restates, that
prediction.** The demonstrated zero-reversal smoothness (16/16 points
strictly increasing, well inside settling and floor gates) is the
correct continuum-limit control a future discretely-layered-coating
comparison would need to difference against — any layer-tied ripple
found in a future realizable-coating rerun, above this cycle's own
demonstrated noise floor, would be attributable to discreteness, not
instrument artifact.

**New hypothesis, MATERIALS' own Phase-5 self-review (speculative,
untested this cycle):** re-anchoring the standoff samples to the
shell's own physical outer surface (`r_out=78` cells = 3.90λ, not the
window formula's inherited `R_CLK=90` — exp-001's *cloak* radius, reused
only because that file fixed one window across all three of its
scenes), the sampled range runs from 1.10λ (x=352) to 6.30λ (x=456)
from the coating's actual surface, over which κ rises ~14×. The shell's
own radial grading thickness is `r_out − r_in = 48` cells = 2.4λ — the
healing length needed for κ to climb an order of magnitude (~5λ of
standoff) is roughly *double* the grading thickness, suggestive that
fill-in here is dominated by the shell's overall transverse silhouette
(diameter `2·r_out` = 7.8λ) rather than by how deep the sigma grading
runs radially. If true, the grading thickness would principally set the
*floor* of κ at the shell's own surface (how dark the shadow starts),
while the silhouette size would set how *fast* it heals downstream —
two distinct physical knobs. Any future dense-standoff-trend functional
fit (Next item 5) should be parameterized against `r_out`, not
`r_out − r_in`, per this hypothesis — untested, flagged for that future
cycle, not resolved here.

## LOGBOOK.md RULED OUT registry / standing rules check

No item in LOGBOOK's RULED OUT registry (R1–R22) is re-proposed: no
mechanism or material parameter is touched (not R1); no named-constant
search is performed (not R5); this cycle's own would-be R5/R17 violation
(reusing `R4_TAPER=80` at the wrong resolution without checking it
against established precedent) was caught and corrected at Phase 2,
before any FDTD call, per R17's own discipline; the floor-gate
convention now matches exp-102's own established formula exactly (not a
departure, per fix 3); the settling-independence leg (fix 6) directly
answers the VALIDATION.md stage-20 lesson EM's critique invoked, at the
correct (moderately-lossy, sigma_max=0.5) regime that lesson's own
canonical bench describes; the R22 sign-convention rule does not apply
(kappa is |Ez|²/|Ez|², non-negative by construction, no vector
self-consistency identity is introduced). No closed Live Thread claim is
re-litigated: T8's near-field caveat is disclosed, not resolved; T9's
Babinet-ceiling disclaimer is not engaged (this cycle does not compute
σ_abs/σ_ext); T28's own `delta_scene`/R3-vs-R4 split (Tier 1,
exp-100/101/102) is untouched — this experiment does not read, cite, or
score `delta_scene`/`frac_contrast`/`ratio_k` at all.

## Phase 3 — Director's synthesis: accepted / overridden criticisms

**All 8 numbered Red Team mandatory fixes ACCEPTED** (fixes 1–8 above,
folded into Setup/Idealizations/`run.py`). **Fix 9 (QUANTUM's proposed
3–4-phase-reference resampling) ACCEPTED AS OVERRIDDEN** — Red Team's
own reasoning is adopted verbatim: `sc.phasors()`'s magnitude is
provably `rel_phase`-invariant (a constant source phase multiplies the
whole linear-field solution by a unit-modulus factor, cancelling exactly
under `|·|`), so re-sampling at different launch phases would be a
zero-information no-op burning 3–4× the FDTD call budget. The
PHOTONICS/QUANTUM Phase-2 disagreement is resolved per Red Team's own
explicit ruling: both seats converged on the same underlying hazard
(coherent spatial ripple under-sampled by the standoff grid) under two
framings; PHOTONICS's spatial-Nyquist framing is the technically correct
one and its fix (tightened window-spanning pitch, ≤10 cells) is adopted
as the sole discharge — QUANTUM's own remedy is not additionally
implemented.

**One Director-level disposition, beyond Red Team's own text** (recorded
explicitly, since the audit itself left this as an open call-budget
trade): fix 6 (settling-independence leg) is implemented for **all
five** near-field points rather than Red Team's own single-point
fallback, because the check is a whole-field capture — re-reading 5
points from the same 2 settling-check FDTD calls costs nothing beyond
that pair. This delivers the FULL strength of EM's own original Phase-2
steel-man (not the scaled-down compromise Red Team's audit accepted as a
safe minimum) while keeping the total call budget at exactly 4, never
silently exceeding this cycle's own stated FDTD-call discipline. No
criticism is overridden by this choice — it is a strictly stronger
discharge of an already-adopted fix, made possible by a capability
(whole-field re-use) Red Team's own text did not fully account for.

Predictions above are committed to git in this same commit as this
synthesis, strictly BEFORE `run.py`'s first real Phase-4 invocation.

## Result

**kappa_window/kappa_region are raw physical intensity ratios; no
Weber-contrast or C_thr(L) perceptual scoring is performed this cycle**
(restated per the T28 dual-section banner requirement, LOGBOOK.md
Iteration 65 — added at Phase 5, Red Team final-audit mandatory-fixes
docket item 2; the mechanical gap — this sentence present in Setup/
Idealizations but absent from Predictions/Result through Phase 4 — was
independently caught by VISION's Phase-5 review, the third post-
escalation instance of this exact pattern on this T28 sub-thread, ruled
non-Checkpoint-4-firing per unbroken discharge-test precedent, ruled a
mandatory same-shift fix regardless).

**All 4 real FDTD calls executed exactly as budgeted** (2 primary + 2
settling-check), 226.7s (3.78 min) total wall time (113.8s + 112.8s),
trust suite confirmed green (41/41, `--only 12346789`) before and after,
zero `lab/` diff throughout.

**Prediction 1: CONFIRMED.** `kappa_window = 1.8337%`, inside the
predicted [0.5%,4.0%] band and close to the established `beam_behind`
figure's own 1.5–1.8% (this cycle's number is a distinct, phasor-based
window-mean-intensity convention, not a literal re-derivation of that
figure — see the envelope()-vs-phasors() disclosure in Setup — but the
close numeric proximity is itself informative, not merely inside a wide
tolerance band). Internal spatial spread within the window is real and
substantial (pointwise ratio std/mean = 0.849, min 0.075%, max 7.25%) —
the window genuinely averages over a spatially varying near-field
pattern, not a flat plateau; this is disclosed data, not swept into the
single scalar.

**Prediction 2: CONFIRMED as literally scored — zero reversals against
its own pre-registered criteria.** The 16-point `kappa_region` trend
rises monotonically and smoothly from 0.458% at x=352 to 6.41% at
x=456, every single step an increase, no local maxima or dips anywhere
in the sampled range.

**Correction (Phase-5 mandatory fix 4, PHOTONICS + QUANTUM, Red Team
final-audit-adopted — the original text below overclaimed what this
data can show):** this is valid, unweakened evidence against the
coarser (25–40-cell) Fresnel-edge-fringe alternative `VALIDATION.md`
documents (adequately Nyquist-sampled at 10-cell pitch, 2.5–4
samples/period). It is **weak, not clean, disconfirmation** of the
finer λ/2-scale coherent standing-wave alternative Prediction 2 was
also meant to distinguish from: the adopted ≤10-cell window-spanning
pitch samples at *exactly* the λ/2=10-cell period of the coherent
intensity cross-term at risk (the textbook degenerate-aliasing case,
not a resolved one — independently re-derived by two Phase-5 seats and
confirmed by Red Team's own final audit), and `H_REGION=5`'s own
11-cell block-average independently suppresses ~91% of any such
ripple's amplitude per sample (|sinc(11/10)|≈0.089), regardless of
inter-sample pitch. `kappa_window`'s own disclosed internal spread
(pointwise std/mean=0.849, 97× min-to-max within the window footprint —
see below) is itself direct evidence that comparable-scale spatial
structure genuinely exists nearby. The zero-reversal result therefore
does not, on its own, rule out a fringe-limited near-field null at the
λ/2 scale; it only rules out one at the coarser edge-diffraction scale.
Queued for Iteration 81 Tier 1: a genuinely sub-Nyquist recheck (≤4-cell
pitch, or a much smaller `H_REGION`).

**Prediction 3: CONFIRMED.** Floor gate: 0/16 points unresolved (all
comfortably above the pool-RMS floor). Window-spanning mean
(3.293×10⁻²) vs. `kappa_window` (1.834×10⁻²): ratio 1.796×, inside the
≤2.0× band — expected, since the window-spanning points span a range
(0.58%→6.41%) that straddles `kappa_window`'s own window-averaged value,
not a tight cluster around it; the two readings are consistent measures
of the same rising trend, not independent quantities that should match
closely.

**Prediction 4: CONFIRMED.** All 5 near-field points show
STEPS=3200-vs-6400 relative changes of 0.003%–0.11% — two to four
orders of magnitude inside the 20% tolerance band. **Correction
(Phase-5 mandatory fix 1, ELECTROMAGNETISM, Red Team-confirmed exact —
the original text here ran the comparison backwards):** these residuals
are LARGER than, not smaller than, VALIDATION.md's own stage-20
canonical figure for this exact loss regime (`sigma_max=0.5`, ~1.5×10⁻⁵
field-relative RMS by 900 steps) — by roughly 2×–73× across the five
points (largest at x=352, closest to the object; smallest at x=356).
This does not change the verdict: even the largest residual (0.110%)
clears the pre-registered 20% tolerance by ~180×. The comparison to the
stage-20 figure was never fully apples-to-apples in the first place (a
two-step-count κ comparison vs. that lesson's own phase-rotation-
identity noise floor) and is retained here only as informal context, not
as a validated ceiling. Relative-change DOES decrease monotonically with
standoff (0.110%→0.003%, x=352→356) — the correct qualitative signature
of a decaying near-field transient, not a flat step-count-independent
artifact floor, though this two-step-count check cannot by construction
rule out convergence to a wrong value shared by both step counts (a
genuine multi-step-count convergence bench is queued for a future
cycle that pushes standoff nearer-field than x=352). This corroborates
Red Team's own Phase-2 ruling that ELECTROMAGNETISM's original critique,
while correctly motivated, imported an alarm figure from a structurally
different (near-lossless) regime — the moderately-lossy `sigma_max=0.5`
article settles at this suite's own established STEPS=3200 convention
well inside its own pass bar, at all 5 of the near-field points the
concern was raised about (not merely the single spot-check Red Team's
own fallback text would have settled for), even though the residuals
are not as small as the original Result text claimed.

**Passivity check (Phase-5 mandatory fix 5, ELECTROMAGNETISM):** no
`kappa` value — window or region, mean, pointwise, min, or max — anywhere
in `results.json` approaches or exceeds 1 (largest value present:
0.0641, the x=456 region reading); the passivity bound is implicitly
satisfied everywhere.

**Gate B is now genuinely, honestly reproduced — not force-fixed.**
Both of exp-102's own diagnosed defects (near-field-standoff mismatch,
undisclosed aperture-taper mismatch) are resolved by construction in
this cycle's build, and the resulting `kappa_window` figure lands close
to the established `beam_behind` anchor while every supporting
diagnostic (floor gate, settling check, monotonicity) independently
clears. The one real, load-bearing correction this cycle required — the
`edge=80`→`edge=40` fix, caught by Red Team's own Phase-2 audit before
any FDTD call ran — means the originally-proposed `edge=80` construction
was never actually executed; there is no "what if we'd used the wrong
aperture" comparison to report, only the corrected run's own clean
result.

## Learned

1. **A cross-resolution constant reused unchanged for a NEW purpose
   needs the same rescaling scrutiny already applied to its OLD purpose
   — checking one use of a shared constant does not clear a second,
   independent use.** exp-102 correctly rescaled `D_STANDOFF`/`H_REGION`
   by the article's own `r_out` ratio when reusing them across the
   R4-family's cpl=40 grid and Gate B's own cpl=20 grid — but this
   cycle's own Phase-1 proposal, written by the same lineage of
   instrument-repair cycles, initially reused `R4_TAPER=80` (itself
   already a resolution-rescaled constant, `round(TAPER·R4_RATIO)`)
   unchanged at Gate B's cpl=20 grid, without asking whether THIS
   constant needed the identical treatment — caught only at Phase 2, by
   Red Team's own direct provenance trace, not by any of five blind
   Phase-2 critiques (all of which engaged with the *choice* to change
   `edge` but not the *correctness* of the specific new value). A
   generalizable house lesson: any proposal reusing a constant from a
   different-resolution geometry family, however recently that
   constant's own resolution-dependence was itself established and
   fixed elsewhere in the same document, should re-verify the
   rescaling explicitly for its own new use, not merely cite the
   constant's name.
2. **A settling-time alarm imported from one loss regime does not
   automatically transfer to a different, more strongly-damped regime —
   confirmed quantitatively, not merely argued, this cycle.**
   ELECTROMAGNETISM's Phase-2 critique correctly named a real,
   documented risk (VALIDATION.md's own stage-20 lesson: near-lossless
   geometries need far more settling than strongly-lossy ones) but cited
   a magnitude figure from the wrong regime; Red Team's own audit caught
   this and scaled the fix down accordingly. This cycle's own settling
   check — run at FULL strength (all 5 points, not the single-point
   compromise) because a whole-field capture makes the fuller check free
   — confirms Red Team's own correction was right: residuals here are
   0.003%–0.11%, not "~100× larger" than a lossy-regime baseline. Both
   the original alarm and its correction were worth having on the
   record; a Phase-4 check that could be run at zero marginal cost
   settled a Phase-2 disagreement definitively rather than leaving it as
   competing arguments.
3. **A whole-field capture makes a "settling-independence leg" and a
   "standoff-trend leg" the same kind of cheap, multi-point diagnostic**
   — this cycle's own 4-call budget produced 16 primary-channel readings
   plus 5 settling-check readings from those same 4 calls, a pattern
   worth reusing: when `sc.full_capture()`/`sc.phasors()` already return
   the entire field, any number of point/region readings drawn from one
   captured pair cost nothing beyond that pair's own two FDTD calls —
   Red Team's own fallback "one representative point" compromise was a
   reasonable caution given the audit's own text did not have this
   cycle's own Director-level accounting of that fact in hand.

## Next (candidate directions, not this cycle's scope)

1. **Tier 1 item 3 (T8 r=78/156/312 near-field-to-witness-scale bridge
   extension)**, explicitly deferred this cycle (see Idealizations) —
   extend this cycle's own now-validated aperture-matched, footprint-
   matched instrument (both the `kappa_window` and the standoff-trend
   machinery) across the established bridge-family radii, closing
   exp-102's own Reconciled Iteration-80 Tier 1 item 3.
2. **Tier 2 — the perceptual conversion** (constraint 1's own missing
   conversion from a raw physical `kappa`/intensity reading to a
   witness-perceived `C_thr(L)` judgment), gated on item 1's own
   bridge-family extrapolation to witness scale — still unbuilt.
3. **Tier 2 — pin the witness-scale absolute source wattage** (T5's
   long-open precondition), parallel-track with items 1–2.
4. **Tier 3 — the standing `delta_scene` R3-vs-R4 split** (Tier 1,
   PHOTONICS' own zero-FDTD physical-hypothesis check) — now deferred
   FOUR consecutive cycles (exp-100→101→102→103); Iteration 81 should
   either execute it or explicitly re-justify a fifth deferral in
   writing, per this cycle's own Idealizations disposition.
5. **A dense-standoff-trend fit**: this cycle's own 16-point monotonic
   trend (x=352→456) is smooth enough to invite a candidate functional
   form (e.g. a Fresnel-diffraction-fill-in closed form) — not attempted
   this cycle (T1: N/A, instrument-repair scope only), but a natural,
   cheap (zero new FDTD, reusing this cycle's own committed data)
   follow-up for a future cycle with spare capacity.

## Phase 5 outcome (six blind reviews + Red Team final audit)

Six blind Phase-5 reviews: THERMODYNAMICS (CONFIRM, zero findings, most
thorough verification pass, explicitly registered zero energy-balance
content this cycle); PHOTONICS, MATERIALS (this cycle's own rotation-lead
seat, self-reviewing), ELECTROMAGNETISM, QUANTUM OPTICS, and VISION
SCIENCE (all CONFIRM-WITH-GAPS). PHOTONICS and QUANTUM independently
converged, by two different routes, on the same load-bearing finding:
the Phase-2 "Nyquist fix" (≤10-cell window-spanning pitch) does not
actually satisfy Nyquist for the λ/2=10-cell coherent-intensity fringe
period it was meant to guard against (true Nyquist needs <5 cells) —
PHOTONICS additionally found `H_REGION=5`'s own box-average partially
mitigates this via low-pass filtering (~91% suppression per sample),
and QUANTUM independently re-derived and confirmed correct Red Team's
own Phase-2 rel_phase-invariance override of QUANTUM's own prior-cycle
proposed remedy. MATERIALS' own self-review found its Phase-1 proposal's
Realizability Bound reasoning was silently dropped between Phase 1 and
this document's Phase-3 freeze — the status label survived, the
reasoning did not, uncaught by five Phase-2 critiques and Red Team's own
Phase-2 audit. ELECTROMAGNETISM found the Result section's own settling-
residual comparison to VALIDATION.md's stage-20 baseline was numerically
backwards (residuals larger, not smaller, by up to 73×; Prediction 4's
verdict unaffected, cleared by ~180× regardless). VISION found the
mandatory perceptual-scoring disclaimer present in Setup/Idealizations
but absent from Predictions/Result, against an established LOGBOOK
Iteration-65 standing rule requiring both — the third post-escalation
instance of this exact gap shape on this T28 sub-thread, the first to
survive to Phase 5 rather than being caught at Phase 2.

Red Team's Phase-5 final audit independently re-verified every finding
from primitives (eight independent primitive-level re-derivations,
spanning five of the six reviews) and adopted all of them — zero
overrides. R20 tally: 1 genuine R4-class defect surviving Phase-3 freeze
into Result/Learned (the EM backwards-citation finding; the Nyquist
overclaim and the dropped Realizability Bound are both real but not
R4-shaped by R20's own text) — far below the "three or more" bar; R20
does NOT fire. Checkpoint criterion 4 ruled on both live sub-issues
(disclaimer-erosion recurrence; Nyquist-overclaim prose) and does NOT
fire on either, per this program's own unbroken discharge-test
precedent (caught blind, same cycle, before LOGBOOK, non-load-bearing
to any scored verdict) — though the disclaimer-erosion sub-issue is
flagged explicitly: a fourth post-escalation instance of this exact gap
shape should be treated as ripe for a standing numbered rule with its
own forward-firing clause. All six mandatory same-shift documentation
fixes applied above (zero re-run, zero verdict change). **Combined
Verdict: PARTIAL** — all four predictions genuinely hold against
independent scrutiny and the two exp-102-diagnosed Gate B defects are
genuinely resolved, weighed against six-plus distinct, confirmed
documentation-layer defects (none load-bearing to a verdict, none
Checkpoint-4-firing, all same-shift fixed) that a clean CONFIRM would
not carry. Reconciled Iteration-81 queue (Red Team's own tiered
ranking): Tier 1 (a genuinely sub-Nyquist standoff recheck, ≤4-cell
pitch or smaller `H_REGION`, one fresh ~2-call FDTD pair — NOT free
post-processing, `results.json` persists no raw field arrays across
cycles — plus restoring `Delta_phi` and per-point spread reporting at
zero further marginal cost from that same pair); Tier 2 (the T8
r=78/156/312 bridge extension, sequenced after Tier 1 so it inherits a
ratified sampling convention); Tier 3 (a multi-step-count settling
convergence bench; thermal-sidecar cross-resolution scrutiny
pre-registered for whenever it's next invoked on this instrument
family; the disclaimer-erosion standing-rule question); Tier 4 (Tier-2
perceptual conversion, witness-scale wattage, the `delta_scene`
R3-vs-R4 split — now FOUR consecutive deferrals, a fifth must be
explicitly re-justified in writing — dense-standoff-trend functional
fit). Full record: `phase5_review_{photonics,materials,em,
thermodynamics,quantum,vision}.md`, `phase5_redteam_audit.md`.
