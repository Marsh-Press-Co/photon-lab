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
  (λ=20 cells, S≈0.2263, quarter=22 steps, φ=ω·22≈1.5644 rad vs. exact
  π/2=1.5708), `envelope()` carries a small (cos φ≈0.0064, up to ~0.6%
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

**Prediction 2: CONFIRMED, cleanly — zero reversals.** The 16-point
`kappa_region` trend rises monotonically and smoothly from 0.458% at
x=352 to 6.41% at x=456, every single step an increase, no local maxima
or dips anywhere in the sampled range. This is the clean Fresnel-fill-in
signature the Iteration-79 Red Team audit's own standoff hypothesis
predicted, not the "fringe-limited near-field null" alternative — the
tightened (≤10-cell/λ2) window-spanning sampling pitch (Phase-2
mandatory fix 5) that closed the original Nyquist-aliasing risk shows no
sign of the aliased ripple that risk would have produced; the trend is
smooth at this resolution.

**Prediction 3: CONFIRMED.** Floor gate: 0/16 points unresolved (all
comfortably above the pool-RMS floor). Window-spanning mean
(3.293×10⁻²) vs. `kappa_window` (1.834×10⁻²): ratio 1.796×, inside the
≤2.0× band — expected, since the window-spanning points span a range
(0.58%→6.41%) that straddles `kappa_window`'s own window-averaged value,
not a tight cluster around it; the two readings are consistent measures
of the same rising trend, not independent quantities that should match
closely.

**Prediction 4: CONFIRMED, decisively.** All 5 near-field points show
STEPS=3200-vs-6400 relative changes of 0.003%–0.11% — two to four orders
of magnitude inside the 20% tolerance band, and itself two to three
orders of magnitude smaller than VALIDATION.md's own stage-20 canonical
figure for this exact loss regime (`sigma_max=0.5`, ~1.5×10⁻⁵ field-relative
RMS by 900 steps) would suggest as a rough ceiling. This corroborates
Red Team's own Phase-2 ruling that ELECTROMAGNETISM's critique, while
correctly motivated, imported an alarm figure (~100× larger residual)
from a structurally different (near-lossless) regime — the moderately-
lossy `sigma_max=0.5` article settles cleanly at this suite's own
established STEPS=3200 convention, now demonstrated rather than argued,
at all 5 of the near-field points the concern was raised about (not
merely the single spot-check Red Team's own fallback text would have
settled for).

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
