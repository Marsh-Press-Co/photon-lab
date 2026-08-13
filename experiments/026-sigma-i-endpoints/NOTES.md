# exp-026 — The σ(I) Endpoint Triplet

Panel Iteration 3 (lead: MATERIALS, rotation). Full seven-seat cycle:
Phase 1 proposal (MATERIALS) → 5 blind parallel critiques (PHOTONICS, EM,
THERMO, QUANTUM, VISION — all support-with-changes) → Red Team last with
everything (verdict: proceed-with-mandatory-fixes, one decisive catch) →
this Phase-3 synthesis. Full verbatim record: `LOGBOOK.md`, Iteration 3.

## Hypothesis

Three uniform-conductivity, index-matched (ε_r = 1) sponge disks — no PEC
core, r_out = 78 cells, same construction as the existing calibration
sponge — measure the σ(I) escape route's static endpoints on exp-024's
±35° fallback geometry, the first instrument geometry in this program
precise enough to *measure* C in the near-threshold regime at real SNR
(not just certify a deep FAIL): OFF-lab (τ_center = 0.008, straddles the
lab bar 0.005), OFF-field (τ_center = 0.032, straddles the field bar
0.02), and ON (τ_center = 3.9, the beam-termination endpoint). No
intensity dependence is built or claimed — these are two ends and one
interior point of a hypothetical trajectory, measured as ordinary static
linear articles. **Explicit caution (accepted from QUANTUM's Phase-2
critique): measuring these three static points does not reduce
uncertainty about the σ(I) switching mechanism itself, still ruled
UNOBTANIUM-WITH-PARAMETERS (Iteration 2 Phase 5) — no trajectory or
de-risking claim is made about the path between OFF and ON.**

## Setup

Geometry inherited **verbatim** from exp-024's ±35° fallback (zero
changes): `experiments/026-sigma-i-endpoints/design_geometry.py` — NX=360,
NY=1584, ABSORB=40, SRC_X=300 (y∈[40,1544], taper 40), OBJ=(170,792),
R_OUT=78, PLANE_X=77, FALLBACK_ANGLES=(−35,−25,−15,−5,0,5,15,25,35), N=9.
Ambient decision floor reused from exp-024/025 (not remeasured): δ_C =
0.00089/0.00007/0.00045 @ 450/600/750nm.

Three new articles (`run.py::build_ambient`, `dg.SIGMA_BY_ARTICLE`):

| Article | τ_center | σ_engine | Attenuation length | Chord-model C_geo (fallback N9) |
|---|---|---|---|---|
| OFF-lab | 0.008 | 5.1282e-5 | ≈585 µm | −0.0055 |
| OFF-field | 0.032 | 2.0513e-4 | ≈146 µm | −0.0216 |
| ON | 3.9 | 2.5000e-2 | ≈1.2 µm | −0.7823 |
| (tie-point, reused, not rerun) τ=0.10 | 0.10 | 6.4103e-4 | ≈47 µm | −0.0657 (matches exp-024's fallback commit `c67506b`) |

Beam-scene channel (ON article only) reuses exp-001/002's exact validated
domain unchanged: N=560, CX,CY=(252,280), R_OUT=78 (their R_COAT),
SRC_X=64, OBS_X=78, courant_frac=0.32, STEPS=3200 — for direct
comparability with the established camera-floor (7×10⁻⁵–1.4×10⁻⁴) and
`graded_black_shell` σ_abs/σ_ext=0.51 baselines this experiment's
predictions are scored against.

**Run plan (corrected at Phase 3 — two bookkeeping fixes over the Phase-1
proposal, both caught in Phase 2/Red Team):**

| Block | Runs | Note |
|---|---|---|
| Ambient: 3 new articles × 9 angles × 3λ, + empty per group | 81 sim runs (27 groups × 3 articles) + 27 empty | empty NOT reused from exp-024's file — the empty-scene B(y) profile is regenerated bit-reproducibly here (same geometry/seed/steps) rather than depending on a cross-experiment results file read |
| Beam-scene: empty + ON, 3λ | 6 | **corrected from the Phase-1 proposal's "3 runs"** — an empty reference is required per λ for beam-behind/observer-return/box-ledger (exactly as exp-001/002 needed it), not reusable across λ |
| N-convergence (P-MAT7, off_lab@600nm, N5 vs N9) | **0 new** | recomputation from the 9 already-collected off_lab@600nm angle runs (Red Team's catch: the Phase-1 table miscounted this as "5 runs") |
| Box-closure identity (Thermo's mandatory fix) | **0 new** | recomputation from the empty-scene capture already required as `widths()`'s reference in the beam-scene block |
| **Total new FDTD runs** | **108 + 6 = ~114** ambient sim calls (27 groups × 4 scenes) **+ 6 beam-scene** | ≈ 8–10 min at the smoke-tested pace (single ambient group ≈ 60s / 4 workers; single beam group ≈ 55s × 3λ sequential) |

Suite: 41/41 before this experiment (verified this shift); no `lab/`
engine changes — reverification after is a formality per house discipline,
run anyway.

## Phase 3 — accepted / overridden (Director's synthesis)

Red Team's verdict: **proceed-with-mandatory-fixes**, with one decisive,
load-bearing catch (attack #1–#3): EM's Phase-2 attack — P-MAT8's original
σ_abs/σ_ext ≥ 0.90 prediction directly contradicts the panel's own
**ESTABLISHED** measurement (`graded_black_shell`, same r_out=78,
σ_abs/σ_ext = 0.51 — the extinction-paradox saturation value for an
optically-thick, near-zero-reflectivity absorber) — was independently
verified correct by Red Team and found to understate the severity: the
ON article's abrupt σ-step (no adiabatic grading, unlike `graded_black_shell`)
adds a front-edge reflection channel the graded shell's design specifically
eliminated, so the *true* number is likely at or below 0.51, not above it.
Red Team additionally caught that P-MAT8's error cascades into P-MAT5
(observer-return), a constraint-2 metric, riding unexamined on the same
optimistic split.

**Accepted in full:**
1. **EM's P-MAT8 attack + Red Team's severity extension** — P-MAT8
   rebanded from [0.90,1] to **[0.35, 0.65], central ≈0.50**, anchored
   explicitly to the established 0.51 measurement, with the added
   front-edge reflection channel as the reason to expect at-or-below
   rather than above it. (Smoke-tested at 600nm before freeze: real FDTD
   gave σ_abs/σ_ext = 0.6075 — inside the revised band, nowhere near the
   original ≥0.90 claim. This number is a pre-freeze plumbing check only,
   not the committed result — the real run below is what's scored.)
2. **Red Team's cascade finding (P-MAT5)** — observer-return band widened
   from ≤7×10⁻⁴ to **[7×10⁻⁵, 0.02], central ≈3×10⁻⁴**, and marked
   **PROVISIONAL / informational** — it rides on the same corrected-but-
   uncertain reflectivity assumption as P-MAT8 and is not scored as a
   tight constraint-2 verdict this iteration.
3. **PHOTONICS' rider attack + Red Team's T7 anchor (#5)** — the original
   binary "step alone sufficient / needs a discontinuity" edge-hardness
   rider is replaced with an **exhaustive 3-way partition** anchored to
   two existing data points: the τ=0.10 null (Δ=0.0003, noise-level, same
   bare-σ-step construction at low depth) and T7's own established
   finding that the red-ward chromatic drift already appears in BOTH an
   adiabatic-smoothstep edge (absorber, Δ=0.0114) AND an abrupt PEC edge
   (Δ=0.0166, "same rough magnitude") — i.e. edge hardness has already
   been shown NOT to gate the effect on/off. See P-MAT3 below.
4. **THERMO's flip** — the box-closure identity gate added (zero extra
   runs, using the already-required empty-scene beam-domain capture);
   the ΔT/emission-band/detectability sidecar explicitly deferred to
   docket #7's witness-wattage pin (not attempted here).
5. **VISION's underlying concern, accepted in full; her specific remedy
   (build r=156 geometry now) overridden** — a real scale-bridge concern
   (measured |C| at 2.34 µm scale may not transfer to real perceptual
   thresholds pinned on much larger targets, per exp-020's own idealization
   (iii)) is real and mandatory to address in language, but redesigning
   windows/BOX for a doubled object radius inside this same cycle is a
   real geometry-redesign task, not a same-cycle rider — this lab's own
   precedent (exp-024's own margin fix) treats window/domain redesigns as
   their own dedicated, careful build. **Resolution: strike all "certify a
   PASS" framing; P-MAT1/P-MAT2 carry NO PASS/FAIL or constraint-3
   language anywhere in this record.** VISION's r=156 bridge check (ideally
   both OFF-lab and OFF-field) is queued as dedicated future work (PLAN.md).
6. **Red Team's run-accounting catch (#7)** — N5 convergence and the
   box-closure gate both cost zero new runs; the Phase-1 proposal's "89
   runs" total corrected to the table above.

**Overridden, with reasons:**
- **QUANTUM's flip** (fold the coherent-superposition bridge-gate check in
  now, as a non-gating rider) — **not adopted**. Red Team's own standing
  Iteration-2 rule applies unchanged: new source/injection machinery needs
  its own gated suite stage, a real build cost QUANTUM's "near-zero
  marginal" framing understates — Iteration 2's synthesis already ruled
  this belongs to its own iteration, and nothing here changes that.

## T1 escape-route statement

Serves intensity-gated absorption σ(I) — but only its static endpoints,
per the hypothesis section's explicit caution above. No σ(I) mechanism is
built; Checkpoint 3 engine work remains untouched and out of scope.

## Predictions — committed before this experiment's first real run

- **P-MAT1 (OFF-lab, ambient C, all 3λ):** central −0.0055, band
  [−0.0075, −0.0035]. Chromatic spread |C(750)−C(450)| ≤ 0.001. **No
  PASS/FAIL or constraint-3 language attaches to this reading** — reported
  as a position relative to the lab bar (0.005) only, pending VISION's
  queued scale-bridge check.
- **P-MAT2 (OFF-field, ambient C, all 3λ):** central −0.0217, band
  [−0.026, −0.018]. Chromatic spread ≤ 0.002. Same non-verdictive framing.
- **P-MAT3 (ON, ambient C, all 3λ):** central −0.786, band [−0.85, −0.72].
  **Chromatic-spread 3-way partition** (replaces the original binary
  rider): (a) spread ≥ 0.008 (comparable to T7's established 0.0114/
  0.0166) → opacity alone, independent of edge type, reproduces the T7
  drift — a materials-general finding; (b) spread ∈ [0.001, 0.008) →
  ambiguous/partial, flagged, no strong claim; (c) spread ≤ 0.001 (matches
  the τ=0.10 null) → opacity alone, even at τ=3.9, does not reproduce the
  drift, and — combined with T7's own edge-type-insensitivity — deepens
  the open puzzle rather than resolving it (no mechanism identified either
  way).
- **P-MAT4 (ON, exp-001 beam-behind):** central 2.0% (= e^−3.9), band
  [1.5%, 6%], wavelength-flat (≤1% relative spread across λ).
- **P-MAT5 (ON, observer-return) — REVISED, PROVISIONAL:** band
  [7×10⁻⁵, 0.02], central ≈3×10⁻⁴. Rides on the same corrected-but-uncertain
  reflectivity assumption as P-MAT8; scored informationally, not as a
  tight constraint-2 verdict, until a dedicated front-lit/reflectivity
  follow-up exists.
- **P-MAT6 (linear-transfer constant g = |C|/τ_center, OFF-lab +
  OFF-field):** g ∈ [0.62, 0.69].
- **P-MAT7 (N-convergence, OFF-lab @ 600nm, N5 vs N9 fallback subsample,
  zero new runs):** |ΔC| ≤ 0.001, central ≤ 0.0005.
- **P-MAT8 (ON, closed-box ledger, zero extra runs) — REVISED:** σ_abs/
  σ_ext ∈ [0.35, 0.65], central ≈0.50, anchored to the established 0.51
  `graded_black_shell` measurement at the same r_out=78. **Precondition
  gate (Thermo's mandatory fix, zero extra runs): box-closure identity on
  the empty beam-scene reference ≤ 0.02 relative** (house standard,
  matching exp-024's own P6-emptybox convention) — if missed, P-MAT8 and
  P-MAT5 are not interpreted this shift.

## Idealizations

2D TMz, one polarization; static/linear/time-invariant throughout — no
σ(I) implemented, only its hypothesized static endpoints measured, no
claim about the trajectory between them; CW single-λ, 3-λ quadrature for
white light; incoherent-sum linear-media idiom unchanged (`lab/ambient.py`
untouched); back-lit ambient only for OFF-lab/OFF-field; graded damping
bands, not PML; ±35° fallback omits ±40° (T7's angle-specific mechanism
still open) — a narrower ambient than the original ±40° design; chord-model
bands are geometric-optics (straight-ray Beer–Lambert, no diffraction
term); ε_r pinned at exactly 1.0 (zero *index-step* reflection by
construction — but NOT zero reflection: the abrupt σ-step is its own
scattering channel, per EM/Red Team, which is exactly why P-MAT8/P-MAT5
were widened rather than trusted at their Phase-1 values); the ON article's
abrupt σ step is a genuinely new boundary condition for this instrument
family; **P-MAT1/P-MAT2's near-threshold C readings are explicitly NOT a
constraint-3 verdict at any scale beyond this 2.34 µm bench object** — the
scale-bridge check that would license that reading is queued, not run,
this iteration.

## Realizability bound (Materials' seat duty, carried from Phase 1)

OFF-lab (τ=0.008) — **PUBLISHED**. OFF-field (τ=0.032) — **PUBLISHED**. ON
(τ=3.9, α≈0.83 µm⁻¹, attenuation length ≈1.2 µm) — **PLAUSIBLE**: the
absorption coefficient has real precedent (VACNT/heavily-loaded
composites) but holding it simultaneously with ε_r pinned at literally 1.0
(zero index contrast) is not demonstrated by any citable material —
flagged as the open engineering ask. The switching mechanism itself
(σ_on/σ_off swing, Δσ/σ ≈ 122–487× under CW broadband illumination) —
**UNOBTANIUM-WITH-PARAMETERS** at any σ₂ nameable today, carried forward
verbatim from Iteration 2 Phase 5's ruling; this experiment does not
change that ruling (per the T1 escape-route statement above).

## Results

**Correction (Red Team's Phase-5 audit, accepted in full — see LOGBOOK.md
Iteration 3 Phase 5):** this section originally reported "87 new FDTD runs"
and "435s total (329+106)" — both wrong. The correct count is **114 new
FDTD sim calls** (108 ambient: 27 groups × [empty + 3 articles] + 6
beam-scene: 3λ × [empty + on]) — "87" was a leftover arithmetic error from
an earlier draft, never reconciled against the code's own `n_new_runs`
field (114, correct in `results.json` throughout). The wall-clock total
**435 s (329 s ambient + 106 s beam-scene) is itself correct** — it matches
the run's own console log — but `results.json`'s `elapsed_s_ambient` field
had an independent instrumentation bug (captured after the beam block too,
double-counting it as ≈435s instead of the true ≈329s); fixed in `run.py`
for future runs, not retroactively edited in the committed `results.json`
(historical record kept honest, not silently patched).

114 new FDTD sim calls, 435 s total (329 s ambient + 106 s beam-scene),
suite 41/41 before and after (no `lab/` changes). Full data:
`results.json`.

**Ambient decision floors (new empty runs, regenerated bit-reproducibly at
this geometry, informational — exp-024/025's committed values remain the
scored ones):** 0.000889/0.000033/0.000432 @ 450/600/750 nm — essentially
identical to exp-024/025's own numbers (0.00089/0.000033–0.000071/
0.00043–0.00045), confirming the geometry reproduces bit-for-bit as
designed.

**Ambient Weber contrast C (fallback, N=9):**

| Article | 450 nm | 600 nm | 750 nm |
|---|---|---|---|
| OFF-lab | −0.0046 | −0.0055 | −0.0051 |
| OFF-field | −0.0209 | −0.0218 | −0.0213 |
| ON | −0.7822 | −0.7854 | −0.7851 |

**Beam-scene (ON article):**

| λ | beam-behind | observer-return | σ_abs/σ_ext | box_dev | empty-closure |
|---|---|---|---|---|---|
| 450 nm | 2.34% | 0.000194 | 0.6056 | 0.0027 | 3.25e-4 |
| 600 nm | 2.97% | 0.000151 | 0.6075 | 0.0004 | 1.57e-4 |
| 750 nm | 1.86% | 0.000215 | 0.6083 | 0.0023 | 1.17e-3 |

### Predictions scored

- **P-MAT1 — CONFIRMED.** OFF-lab C ∈ [−0.0055, −0.0046], band
  [−0.0075, −0.0035]: inside at every λ. Chromatic spread |C(750)−C(450)|
  = 0.0005 ≤ 0.001. Per the accepted VISION/Red-Team ruling, **no PASS/FAIL
  or constraint-3 language attaches** — this measures the instrument's
  precision straddling the lab bar (0.005), nothing more, pending the
  queued r=156 scale-bridge check.
- **P-MAT2 — CONFIRMED.** OFF-field C ∈ [−0.0218, −0.0209], band
  [−0.026, −0.018]. Chromatic spread 0.0004 ≤ 0.002. Same non-verdictive
  framing.
- **P-MAT3 — band CONFIRMED; chromatic-spread partition outcome (b),
  ambiguous.** ON C ∈ [−0.7854, −0.7822], band [−0.85, −0.72]: comfortably
  inside, close to the −0.786 central prediction. Chromatic spread
  |C(750)−C(450)| = 0.0029 — **lands in partition (b) [0.001, 0.008):
  ambiguous/partial, no strong claim per the pre-committed disposition.**
  Notably: this is 4–6× smaller than T7's established hard-edge spreads
  (absorber Δ=0.0114, PEC Δ=0.0166) but ~10× larger than the τ=0.10 null
  (Δ=0.0003) — sitting between both established anchors rather than
  matching either. Honest reading: a bare, deep (τ=3.9) conductivity step
  shows *some* chromatic drift, smaller than either hard-edge article, so
  neither the "opacity alone reproduces it" nor the "opacity alone doesn't"
  reading is earned — genuinely inconclusive, flagged for Phase 5 rather
  than forced into either bucket.
- **P-MAT4 — band CONFIRMED; wavelength-flatness sub-claim REFUTED.**
  Beam-behind ∈ [1.86%, 2.97%], comfortably inside [1.5%, 6%]. But the
  predicted ≤1% relative spread across λ is badly missed: (max−min)/mean
  = (2.97−1.86)/2.39 ≈ 46%, non-monotonic in λ (450 > 750, but 600 is the
  peak, not either edge). This is a genuine, unpredicted result, not a
  measurement artifact by the checks available here (box_dev stays low,
  0.0004–0.0027, at every λ) — flagged honestly rather than folded into
  "wavelength-flat as expected." Candidate explanations for Phase 5: cpl
  varies 15/20/25 across this sweep (staircase resolution differs per λ,
  though 750nm has the FINEST resolution yet the LOWEST beam-behind,
  ruling out a simple resolution-quality story); or a genuine λ-dependent
  interaction with the abrupt σ-step boundary, in the same unexplained
  family as T7's chromatic silhouette finding and the still-open PEC N17
  excess.
- **P-MAT5 — informational reading consistent with the provisional band.**
  Observer-return ∈ [0.000151, 0.000215], inside the revised
  [7×10⁻⁵, 0.02] band and close to the ≈3×10⁻⁴ central estimate — modest,
  a few× the established camera floor (7×10⁻⁵–1.4×10⁻⁴), consistent with
  a weakly-reflective (not glinting) coreless disk. Per the accepted
  ruling this is NOT scored as a tight constraint-2 verdict.
- **P-MAT6 — band CONFIRMED at 4 of 6 points; two honest misses (corrected
  from an earlier miscount — Red Team's Phase-5 audit).** g = |C|/τ_center
  ∈ [0.5759, 0.6913] across both articles and all λ; the predicted band
  [0.62, 0.69] holds at 4/6 points. **OFF-lab/450nm misses low** (g=0.5759
  vs band floor 0.62) — the weakest-signal point in the whole dataset
  (|C|=0.0046 against the 450nm decision floor 0.00089, SNR≈5.2, the
  thinnest margin of any scored point here), plausibly floor-proximity
  bias. **OFF-lab/600nm ALSO misses, high, and this one was originally
  undisclosed**: g=0.69133 exceeds the band's own upper edge (0.69).
  Floor-proximity cannot explain this second miss — the 600nm decision
  floor is ~0.00007, giving SNR≈79–167 at this point, an order of
  magnitude cleaner than the explained miss. Both misses are on OFF-lab
  (never OFF-field, four clean points), in OPPOSITE directions (low at
  450nm, high at 600nm) — read as λ-dependent scatter around the true g
  at this program's lowest-τ article, not a systematic bias in one
  direction, but genuinely unexplained rather than dismissed as floor
  noise. Flagged, not hidden, per house discipline — the original
  "5 of 6, one honest miss" framing understated this and is corrected
  here.
- **P-MAT7 — CONFIRMED.** N5 vs N9 (OFF-lab@600nm): N5=−0.0050, N9=−0.0055,
  |Δ|=0.00050 — exactly at the predicted central value, comfortably inside
  the 0.001 gate. Zero new runs, as designed.
- **P-MAT8 — band CONFIRMED; direction of the correction was WRONG, band
  was still right.** σ_abs/σ_ext ∈ [0.6056, 0.6083] across all 3λ — inside
  the revised [0.35, 0.65] band (comfortably clear of the original,
  refuted [0.90,1] claim) but consistently *above*, not at-or-below, the
  established 0.51 `graded_black_shell` anchor EM/Red Team reasoned toward
  — the anticipated extra front-edge reflection from the abrupt σ-step did
  not push the ratio down. **Honest, unresolved candidate explanation for
  Phase 5:** the established 0.51 anchor was measured on a graded shell
  wrapped around a PEC core (exp-001's absorber scene), not a solid
  uniform disk — this ON article has no internal PEC/hard discontinuity at
  all. A hard internal reflector redirecting energy into wide-angle
  scattering the box counts as σ_scat (lowering σ_abs/σ_ext) is a
  plausible mechanism for why the PEC-cored article sits lower than the
  solid one, but this is NOT established here, only proposed as a testable
  next step. The revised, correctly-anchored band still did its job:
  Director's synthesis correctly rejected the original ≥0.90 claim and
  correctly bracketed the real regime, even though the specific reasoning
  about which side of 0.51 the true value would land on was itself wrong.
- **Precondition gate (Thermo's mandatory fix) — PASSED cleanly.**
  Empty-scene box-closure identity (relative to the ON article's own
  σ_ext, same run): 3.25×10⁻⁴ / 1.57×10⁻⁴ / 1.17×10⁻³ @ 450/600/750nm, all
  ≤ 0.02 by 1–2 orders of magnitude. P-MAT8 and P-MAT5 are interpretable.

### Headline (for LOGBOOK)

**Seven of eight predictions land cleanly within their (Phase-3-revised)
bands; P-MAT6 (a calibration constant, not a phenomenon verdict) holds at
4 of 6 points — the Director's synthesis, especially the two mandatory
rebandings (P-MAT8, P-MAT5) Red Team's decisive P-MAT8 catch forced, held
up against real FDTD data.** Two genuine open findings ride along, neither
hidden: (1) P-MAT4's beam-behind is NOT wavelength-flat as predicted (46%
relative spread, non-monotonic in λ) — a new, unexplained chromatic effect
in the beam-transmission channel, distinct from but possibly related to
T7's ambient-silhouette chromatic finding; (2) P-MAT8's σ_abs/σ_ext sits
consistently ~0.10 ABOVE the established 0.51 anchor, opposite the
direction Red Team/EM's mandatory-fix reasoning predicted, though still
inside the widened band that reasoning produced — a real materials
distinction (PEC-cored vs. solid-disk absorber) proposed as the candidate
explanation, not yet tested. **Two honest misses, both on P-MAT6, both on
OFF-lab, in opposite directions** (450nm low, plausibly floor-proximity,
SNR≈5.2; 600nm high, g=0.6913 vs. band ceiling 0.69, NOT floor-explicable,
SNR≈79–167) — corrected here from an original "5 of 6, one miss" framing
Red Team's Phase-5 audit caught understated the record. The σ(I) design
window's static endpoints are now real, gate-clean FDTD numbers rather
than chord-model estimates — g=|C|/τ ≈ 0.58–0.69 across the OFF-lab/
OFF-field range (4 of 6 points), broadly consistent with exp-024's own
one-point calibration (g≈0.62–0.63) now across an order of magnitude in τ,
with two λ-dependent excursions at the lowest-τ article left genuinely
unexplained rather than smoothed over. **No PASS/FAIL or constraint-3
verdict is claimed for the near-threshold OFF-lab/OFF-field readings** —
per the accepted VISION/Red-Team ruling, that requires the still-queued
r=156 scale-bridge check.

## Next (pre-registered, for Phase 5)

(1) P-MAT4's unexplained beam-behind chromatic spread — candidate for a
resolution check (R3 meta-rule: any surprising feature gets one before a
mechanism debate) and/or a direct comparison against the τ=0.10 sponge's
own beam-behind at the same 3λ (not measured yet — only its ambient
channel has ever been run). (2) P-MAT8's PEC-cored-vs-solid-disk
hypothesis for the sign of the 0.51 anchor deviation — testable cheaply:
rerun the established `graded_black_shell` article (or the bare-PEC-core
absorber) with the SAME box-ledger machinery at this exact beam-scene
domain, isolating whether the internal PEC core is what shifts the ratio.
(3) VISION's r=156 scale-bridge check (OFF-lab, ideally OFF-field too) —
still queued, the necessary precondition before any PASS/FAIL or
constraint-3 language may attach to near-threshold C readings. (4) P-MAT3's
ambiguous chromatic-partition outcome — a genuinely new middle-ground
result, worth a dedicated resolution check before either "opacity alone"
reading is asserted. (5) P-MAT6's two OFF-lab misses (450nm low, plausibly
floor-proximity; 600nm high, NOT floor-explicable, SNR≈79–167) —
informational, not urgent for perceptual scoring, but the 600nm excursion
in particular is a genuinely unexplained λ-dependent deviation at this
program's lowest-τ article and worth a look if a future iteration extends
the g-calibration to more τ points.
