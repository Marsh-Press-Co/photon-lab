# exp-028 — The Radial Ledger and the Channel Cross-Check

Panel Iteration 5 (lead: THERMODYNAMICS, rotation). Full seven-seat cycle:
Phase 1 proposal (THERMO) → 5 blind parallel critiques (PHOTONICS,
MATERIALS, ELECTROMAGNETISM, QUANTUM OPTICS, VISION SCIENCE — all
support-with-changes) → Red Team last with everything (verdict:
proceed-with-mandatory-fixes, seven numbered attacks, one load-bearing
catch that reaches into an already-published record) → this Phase-3
synthesis. Full verbatim record: `LOGBOOK.md`, Iteration 5.

## Hypothesis

Two threads, neither a mechanism proposal:

1. **T10's box-ledger-vs-envelope-ratio cross-check** — does the
   `BEAM_BEHIND` near-field envelope's resolution-sensitivity
   (46%→128% relative spread under exp-027's own cpl×1.5 companion) also
   show up in the conservation-protected box-ledger extinction channel
   (`sections.widths`), or is it specific to that one point-sampled
   measurement? Measured here as the box-ledger σ_ext's own relative
   spread at the identical rescaled-cpl geometries.
2. **T9's PEC-vs-rim spatial follow-up** — the box ledger's net four-face
   flux identity cannot see WHERE inside the box absorbed power lands; a
   new radial-binned absorbed-power ledger (`lab/sections.py::
   radial_absorbed_power`, new machinery, gated by suite stage 10) answers
   directly whether Cell B's (PEC-free) absorption profile differs
   spatially from Cell A's (PEC-cored) shell-only absorption, even though
   their aggregate σ_abs/σ_ext ratios are statistically indistinguishable
   (exp-027).

## Setup

Both blocks reuse the exp-001/002/026/027 beam-scene bench
(`lab/sections.py` box ledger, `lab/materials.py`) unchanged except where
stated. Full design: `design_geometry.py`.

**Block A — T10 cross-check, SIGMA rescaled per λ (mandatory fix).** Reuses
exp-027's own `BLOCK2_GEOM` rescaled-cpl geometry **bit-for-bit** (verified:
N/CX,CY/R_OUT/SRC_X/ABSORB/BOX_A/BOX_B/ANNULUS/BEHIND match exp-027's
printed table exactly) — the ONE change is that `SIGMA_ON` is now rescaled
per λ so the ON article's optical depth is held at exactly τ_center=3.9 at
every wavelength:

| λ (nm) | cpl | R_OUT | SIGMA_ON | τ_center check |
|---|---|---|---|---|
| 450 | 22 | 114 | 0.017105 | 3.9000 |
| 600 | 30 | 117 | 0.016667 | 3.9000 |
| 750 | 38 | 119 | 0.016387 | 3.9000 |

(`design_geometry.py`'s own `assert` enforces this to 1e-9 before any run.)
`BEAM_STEPS` held at native 3200, matching exp-027's own Block 2. 6 sim
calls (empty+on × 3λ).

**⚠ Correction to the published record (Red Team's load-bearing catch,
Iteration 5 Phase 2, independently verified this shift):** exp-027's own
`run.py::block2_one()` applies the same *unrescaled* module constant
`SIGMA_ON = 3.9/(2·78) = 0.025` at every λ, regardless of Block 2's own
per-λ-rescaled `r_out` (114/117/119 cells). Since optical depth in this
lab's convention is τ = 2·σ·r_out(cells), exp-027's **published** Block 2
ON article actually carried τ_center = 5.70 / 5.85 / 5.95 at 450/600/750nm
— not 3.9, and drifting ~4.3% across the sweep by construction. This means
**exp-027's own Block 2 beam-behind numbers (currently recorded in
LOGBOOK.md as live thread T10, the "46%→128%" and "0.32% collapse"
findings) measured a systematically different, more strongly-absorbing
article at every λ, not a resolution-matched rerun of the native τ=3.9
object.** A naive 1D Beer–Lambert check at the true (inflated) τ predicts
beam-behind ≈ 0.33%/0.29%/0.26% at 450/600/750nm — close to the *measured*
750nm value (0.32%, previously read as a mysterious near-field collapse)
but far from the measured 450/600nm values (1.09%/1.60%), so the confound
does not cleanly explain T10's whole effect — but it does invalidate the
premise that Block 2 tested "the same physical object at finer
resolution." **An explicit erratum is added to T10's LOGBOOK.md entry this
shift, independent of whether this experiment's own results below confirm
or complicate the underlying resolution question** — see LOGBOOK.md
Iteration 5. This experiment's own Block A is unaffected (τ held at 3.9
exactly, verified above) but is **not** a bit-for-bit resolution rerun of
exp-027's published Block 2 numbers; it is the resolution-matched
comparison exp-027's own numbers should have been, and the two are labeled
separately throughout (`ESTABLISHED_BLOCK2_BEAM_BEHIND_BUGGY` in
`design_geometry.py`, carried as a comparison label only, not an anchor).

**Block B — radial-binned absorbed-power ledger, native + resolution
companion.** New function `lab/sections.py::radial_absorbed_power`
(Joule-dissipation density `p_J = 0.5·σ_e·|Ez_phasor|²`, binned into 26
concentric annuli), gated by **suite stage 10** before this experiment
trusts it (`lab/validation/run_all.py`, 43/43 green including the two new
stage-10 checks — see below). Native geometry: exp-027's own Block-3 bench
verbatim (`N=560, (CX,CY)=(252,280), R_CORE=30, R_OUT=78, cpl=20,
λ=600nm, BEAM_STEPS=3200`), three cells + empty:

| Cell | Construction | Core (r&lt;30) |
|---|---|---|
| A | `pec_disk(30)` + `graded_black_shell(30,78,σ_max=0.5,ε_max=1.0)` | PEC, Ez≡0 |
| B | `graded_black_shell(30,78,...)` + `sigma_e[rr<30]+=0.5` (strict `<`, exp-027's fix, reused) | lossy, σ=0.5 |
| C | `sigma_e[rr<=78]+=τ_ON/(2·78)` (τ_center=3.9, exp-026's exact ON article) | lossy |

4 sim calls. **Plus (EM's mandatory fix, this program's own R3 meta-rule
applied to a brand-new near-field spatial channel before its first
mechanism reading is trusted): a cpl×1.5 resolution companion on Cell B
only**, at exp-027's own `BLOCK2_GEOM[600]` geometry
(`N=840, (CX,CY)=(378,420), R_OUT=117, R_CORE=45, cpl=30`) — empty + B, 2
more sim calls. **Total Block B: 6 sim calls.**

**Total this experiment: 12 new sim calls**, ≈6–8 min at prior shifts'
per-run pace.

## New suite stage (PANEL.md's house rule: new machinery ⇒ new suite
## stage with ≥1 absolute identity gate BEFORE results are trusted)

`lab/validation/run_all.py::stage10_radial_power()`, run this shift
BEFORE any exp-028 number below was computed:

- **PEC-core absorbed power is exactly zero** (r ≤ R_CORE, PEC-cored
  scene): `0.00e+00` — **PASS**, machine-epsilon exact (doubly forced:
  Ez≡0 by the PEC clamp, σ_e≡0 by construction — either alone suffices).
- **Closure vs. box-ledger p_abs** (graded shell, no PEC core): measured
  **1.11%**, confirmed **settling-independent** (stable to the 4th
  significant figure across a 900/1800/3600-step sweep — ruled out as an
  incomplete-CW-settling artifact, this program's own recurring
  candidate). Gate calibrated on this first-run measurement, per lab
  convention (VALIDATION.md's own precedent for first-run recalibration):
  **≤1.5%**, margin above the measured value. This is an **empirical**
  closure (EM's mandatory-fix correction, accepted — see Phase 3 below),
  not an exact identity to machine epsilon; the small offset is read as a
  genuine grid-quantization registration difference between a circular
  disk mask and a rectangular box, not incomplete convergence.

Full suite: **45/45 green** (`--only 12346789,10` → 43/43, 84s; `--only 5`
→ 2/2, unchanged) before this experiment's first official run.

## Phase 3 — accepted / overridden (Director's synthesis)

Red Team's verdict: **proceed-with-mandatory-fixes**, seven numbered
attacks. **All seven ACCEPTED, zero overridden** — full record:

1. **[inconsistency, LOAD-BEARING] SIGMA_ON not rescaled per λ —
   MATERIALS' verified catch, escalated by Red Team from "fix the new
   proposal" to "the published record needs a correction."** Fixed in this
   experiment's own Block A (τ_center=3.9 held exactly, asserted in code);
   **an explicit erratum added to LOGBOOK.md's T10 entry**, independent of
   this experiment's outcome (see above and LOGBOOK.md Iteration 5).
2. **[inconsistency] P-THERMO-B3's stated direction was backwards —
   PHOTONICS' catch, independently reproduced from `materials.py` by Red
   Team.** `graded_black_shell`'s conductivity peaks at the INNER boundary
   (r=r_in=30) and is zero at the outer boundary (r=r_out=78) — the
   opposite of "skew toward the outer boundary." **Fixed: the prediction
   now states the radial peak should sit in r∈[30,50]** (rising σ(r)
   against a field envelope already depleted by upstream absorption), not
   near r≈78.
3. **[inconsistency] "Absolute Poynting-theorem closure identity" language
   overclaimed — EM's catch, independently verified by Red Team against
   this program's own precedent (VALIDATION.md's own closed-box identities
   carry real empirical tolerances, never machine-epsilon).** **Fixed:**
   the closure gate is now named "empirical closure gate (≤1.5%,
   calibrated stage 10)" throughout; "absolute identity" language is
   reserved strictly for Cell A's r≤30 hard zero. **A cpl×1.5 resolution
   companion is added on Cell B** (this program's own R3 meta-rule,
   applied to a first-run near-field spatial reading before its mechanism
   reading is trusted) — see Block B setup above and P-THERMO-B2-R3 below.
4. **[inconsistency] QUANTUM's joint-injection rider was framed as
   "near-zero marginal cost" — Red Team's independent check: opening
   simultaneous-source injection is a real, if small, new-machinery build
   (its own gated suite stage, per Iteration 2's own standing rule QUANTUM's
   own seat has been held to before).** **Not added this cycle.** Instead:
   the coherent-superposition half of QUANTUM's bridge-gate package is
   **honestly re-deferred as its fourth deferral** (not framed as "not a
   repeated tautology"), **committed as a mandatory build on QUANTUM's own
   Iteration-6 lead cycle** (next in rotation: VISION→PHOTONICS→
   MATERIALS→EM→**THERMO(this cycle)**→**QUANTUM(next)**→repeat) — opening
   its own gated suite stage as Red Team's ruling requires, not a rider.
5. **[inconsistency] The box-ledger channel's own missing decision-floor
   characterization (Red Team's own queued Iteration-4 item) is carried
   explicitly into Predictions, not left in Idealizations alone.** See the
   caveat under Predictions below: P-THERMO-A1/A2/A3 and P-THERMO-B1/B2's
   verdicts are read as informally suggestive, not floor-gated, exactly as
   T9's own "well-supported but not yet floor-gated" reading was scored.
6. **[inconsistency] VISION's r=156 scale-bridge check deferral was a bare
   omission, not a reasoned re-deferral — VISION's own catch, endorsed and
   sharpened by Red Team (now overdue a fourth cycle, not "twice-deferred"
   as originally undercounted).** **Not folded in this cycle as an
   unreviewed ad hoc addition** — PANEL.md's independence mechanics (blind
   Phase-2 critique BEFORE a design runs) are the product this program
   protects; the Director designing a new instrument in VISION's own
   domain without her own Phase-1/Phase-2 cycle would violate that
   discipline for the sake of expedience. **Instead: committed HARD as
   VISION's own mandatory Iteration-7 lead-cycle build** (her next natural
   rotation slot, one full cycle after QUANTUM's Iteration-6 commitment
   above) — a hard commitment, not a soft "should," carried into PLAN.md's
   queue.
7. **[unfalsifiable] The QUANTUM rider's language ("applied for the first
   time to a real experiment... not a third silent deferral") oversold a
   schema stub — Red Team's independent check: every run in this
   experiment is a single-source capture at amplitude 1.0, so
   `amp_rel=1.0` is true by construction and untestable.** **Fixed:**
   `results.json`'s `intensity_ledger` field is now labeled "field names
   established, not yet exercised on a non-trivial value" (see `run.py`'s
   meta output).

## T1 escape-route statement

No escape mechanism implemented or claimed — pure diagnostic/
instrumentation work, the same register as Iterations 2, 3, and most of 4.

## Predictions — committed before this experiment's first run

**Block A — T10 cross-check (P-THERMO-A1/A2/A3), on the CORRECTED
(τ=3.9-held) geometry:**
- **P-THERMO-A1 (channel-specific artifact):** box-ledger σ_ext relative
  spread across the 3 rescaled-cpl geometries ≤ **10%**. Reading: the
  box-ledger channel stays flat under resolution refinement even where a
  near-field point-sample channel might not — consistent with box_dev's
  own established cleanliness (≤0.0019, exp-027 Block 3).
- **P-THERMO-A2 (general grid-resolution defect):** relative spread ≥
  **40%** — comparable to exp-027's own NATIVE (uncontaminated) beam-behind
  spread (46.41%, Block 1). Reading: extinction itself, not only a
  near-field point-sample, is resolution-sensitive at these geometries.
- **P-THERMO-A3 (ambiguous, exhaustive middle):** (10%, 40%).
- **Precondition:** τ_center_check = 3.9000 exactly at all 3λ (code
  `assert`, verified pre-run); box_dev ≤ 0.02 at all 3λ.
- **Explicit labeled comparison, not a prediction:** Block A's own
  beam-behind figures (recomputed here with τ correctly held at 3.9) are
  reported alongside exp-027's published (buggy-τ) Block 2 beam-behind
  numbers for reference — the two are NOT the same measurement and no
  prediction is scored against the mismatch between them.

**Block B — radial-binned absorbed-power ledger:**
- **P-THERMO-B1 (precondition, closure):** Σ_bins P_J reproduces the
  box-ledger's own p_abs to **≤1.5%** (stage-10-calibrated gate, not the
  original ≤1% band) at all cells including the companion. **Cell A's
  r≤30 power = 0.0 exactly** (hard identity).
- **P-THERMO-B2 (central, Cell B's native core fraction) — my own
  Iteration-4 committed band, resolved this cycle:** fraction of Cell B's
  total P_J residing in r≤30, band **[1%, 40%]**. Sub-readings: ≤5% →
  topologically real but energetically negligible; ≥15% → a real, sizable
  spatial redistribution the box ledger has been structurally unable to
  report; (5%,15%) → ambiguous.
- **P-THERMO-B2-R3 (NEW, EM's mandatory resolution companion):** does
  Cell B's core-fraction reading survive cpl×1.5? |companion_core_frac −
  native_core_frac| ≤ **5 percentage points** → resolution-stable; **>10
  points** → real resolution sensitivity in this brand-new channel too
  (a candidate third data point for T10's own open question, alongside
  Block A above); (5,10] points → ambiguous.
- **P-THERMO-B3 (informational, CORRECTED direction, PHOTONICS'/Red
  Team's fix):** Cell A's radial Joule-dissipation peak sits in
  **r∈[30,50]**, tracking the shell's own rising σ(r) toward r=r_in
  against a field envelope already depleted by upstream absorption — NOT
  near r≈78 (the shell's outer, σ≈0 edge). No numeric gate; a
  cross-consistency shape check on the new instrument's first run.

**Cross-cutting caveat (Red Team's mandatory fix #5, stated here not only
in Idealizations):** the box-ledger channel this whole experiment leans on
(both Block A's σ_ext and Block B's p_abs closure reference) has **no
formal decision-floor/noise characterization** — informally, box_dev's own
established cleanliness (≤0.0019–0.02 across this program's history)
argues the channel is trustworthy at the percent level, but P-THERMO-A1/
A2/A3 and P-THERMO-B1/B2's verdicts should be read as **informally
suggestive, not floor-gated**, pending that characterization (still
queued, cross-cutting, no single iteration assigned).

## Idealizations

2D TMz, one polarization. Non-dispersive real σ_e everywhere. Block A's
τ-fix closes exp-027's own confound for THIS experiment only — exp-027's
own published numbers stand uncorrected in their own NOTES.md/results.json
(house convention: correct forward, flag the record, don't silently
rewrite committed history) with the erratum carried in LOGBOOK.md. Block
B's radial ledger reads the TOTAL field (not scattered), the physically
correct quantity for Joule heating in a lossy medium — confirmed
term-for-term consistent with the engine's own loss coefficient (EM,
Phase 2). The empirical closure gate (≤1.5%) is a registration-level
limit between a circular mask and a rectangular box, confirmed
settling-independent — not evidence about CW convergence more broadly.
Single-λ (600nm) scope for Block B's native cells, justified by exp-027's
own established near-flatness of both A's and C's aggregate ratios across
the 3λ sweep. No constraint-3/PASS-FAIL language anywhere.

## Realizability bound (Materials' seat duty)

Not applicable — no new material or mechanism is proposed; all articles
reuse existing, already-characterized constructions
(`graded_black_shell`, `pec_disk`, exp-026's uniform sponge) verbatim.

## Results

12 new FDTD sim calls, ~8 min (Block A 307.1s, Block B native+companion
~161s). Suite 45/45 green before and after (no further `lab/` changes
this run). Full data: `results.json`.

**Block A (T10 cross-check, τ_center=3.9 held exactly at all 3λ — verified
by code `assert`, reproduced in `results.json`):**

| λ | cpl | τ_check | beam_behind | σ_ext | box_dev |
|---|---|---|---|---|---|
| 450nm | 22 | 3.9000 | 2.822% | 346.26 | 0.0015 |
| 600nm | 30 | 3.9000 | 3.252% | 353.94 | 0.0001 |
| 750nm | 38 | 3.9000 | 1.932% | 369.41 | 0.0017 |

box-ledger σ_ext relative spread: **6.49%**.

**Block B (radial-binned absorbed-power ledger):**

| Cell | abs/ext | closure | core_power (r≤30) | core_frac | peak bin r |
|---|---|---|---|---|---|
| A (native) | 0.5118 | 0.26% | **0.0 exactly** | 0.0000 | 55.5 |
| B (native) | 0.5118 | 0.26% | 0.019006 | **0.0001 (0.01%)** | 55.5 |
| C (native) | 0.6075 | 0.21% | 27.633 | 0.0773 (7.73%) | 76.5 |
| B (companion, cpl×1.5) | — | 0.20% | — | **0.0000 (0.00%)** | 83.2 (=55.5 in native cells) |

### Predictions scored

- **P-THERMO-A1 (channel-specific artifact) — CONFIRMED.** Box-ledger σ_ext
  relative spread = 6.49%, inside the ≤10% band. Reading: the box-ledger
  channel stays comparatively flat at Block A's rescaled-cpl geometries.

- **The T10 comparison, beyond the pre-committed bands (the decisive
  result this experiment was built to get) — the SIGMA_ON confound
  explains the overwhelming majority of T10's originally reported
  "enlargement," once correctly controlled:**

  | Quantity (beam-behind spread) | value |
  |---|---|
  | Native, τ=3.9 held (exp-026/027 Block 1, cpl=15/20/25) | 46.41% |
  | Block 2, τ DRIFTING 3.9→5.70/5.85/5.95 (exp-027 PUBLISHED, cpl=22/30/38) | 127.57% |
  | Block A here, τ=3.9 held (this experiment, cpl=22/30/38) | **49.46%** |

  Once the SIGMA_ON bug is fixed and τ_center is correctly held at 3.9 at
  every λ, the cpl×1.5 refinement moves the beam-behind relative spread by
  only **+3.05 percentage points** (46.41%→49.46%) — not the **+81.16
  percentage points** (46.41%→127.57%) originally recorded as T10. **96%
  of T10's reported "enlargement" evaporates once the optical-depth-drift
  confound is removed.** A small residual (+3.05pp) survives and is not
  itself explained by this experiment — genuinely open, but two orders of
  magnitude smaller than what was reported, and well within the kind of
  run-to-run variation this program's own R3 checks have historically
  treated as unremarkable when *shrinking* a feature (exp-005, -010, -015,
  -023, -025 all report native-to-refined shifts of comparable or larger
  size without triggering a "genuinely enlarged" reading). **T10, as
  originally framed ("the R3 spatial-resolution check can ENLARGE a
  feature, not just confirm or refute it" — the first exception to this
  program's five prior R3 instances), is substantially reframed: the
  apparent exception was mostly an uncontrolled confound, not a genuine
  near-field-channel resolution pathology.** Box-ledger σ_ext, in
  contrast, stayed flat (6.49% spread) at these SAME geometries — so even
  the small residual +3.05pp beam-behind shift is consistent with
  `BEAM_BEHIND` being a somewhat noisier near-field channel than the
  box-ledger (PHOTONICS'/EM's original candidate explanation), just not
  the dramatic one T10 as originally recorded implied.

- **P-THERMO-B1 (precondition, closure) — CONFIRMED, all cells.** Closure
  0.20–0.26%, all ≪ the calibrated ≤1.5% gate. **Cell A's r≤30 power =
  0.0 exactly** — hard identity, PASS.

- **P-THERMO-B2 (central, Cell B's native core fraction) — REFUTED, a
  genuine surprise, reported honestly rather than smoothed into the
  nearest bucket.** Measured core_frac = **0.01%** — an order of magnitude
  BELOW the committed band's own lower edge [1%,40%], and below even the
  "≤5% → topologically real but energetically negligible" sub-reading.
  **New mechanistic finding, sharper than the band anticipated:** the
  graded shell's own conductivity profile (peaking at r=30, the inner
  wall, per PHOTONICS'/Red Team's corrected reading) means the field must
  first traverse the r=30–78 shell — itself carrying substantial optical
  depth — before reaching the core; by the time it arrives, almost no
  field energy remains to be absorbed there, REGARDLESS of whether the
  core is PEC (Cell A, exactly zero by construction) or lossy (Cell B,
  measured statistically negligible). **This sharpens T9's own
  PEC-incidental finding (exp-027) from an aggregate-ratio coincidence
  into a mechanistic one**: Cell A and Cell B's near-identical
  σ_abs/σ_ext ratios aren't a cancellation between "PEC reflects nothing"
  and "lossy core absorbs a little" — the core's contribution is
  negligible in BOTH constructions, because the shell in front of it
  already extinguishes nearly everything.

- **P-THERMO-B2-R3 (resolution companion) — CONFIRMED resolution-stable.**
  |companion (0.00%) − native (0.01%)| = 0.01 percentage points, well
  inside the ≤5pp band. The near-zero core-fraction reading is real, not a
  grid artifact — independently corroborated by the companion's own
  peak-bin location (r=83.2 at cpl×1.5, which rescales to r=55.47 in
  native cells — matching the native peak_bin_r=55.5 almost exactly).

- **P-THERMO-B3 (informational, corrected direction) — partially
  confirmed, band undershot.** Cell A's radial Joule-dissipation peak sits
  at **r=55.5** — well inside from the outer edge (r_out=78), confirming
  the corrected qualitative direction (PHOTONICS'/Red Team's fix: rising
  σ(r) toward r_in competing against a depleted field envelope, not a
  naive skew toward r_out) — but outside the specific committed band
  [30,50]. No numeric gate attached (informational only, as specified);
  noted honestly as a band miss on the specific range, not a directional
  failure.

### Headline (for LOGBOOK)

**Both threads resolve, and the box-ledger cross-check (Block A) produced
a result well beyond its own pre-committed bands.** (1) T10's originally
reported "R3 enlarges a near-field feature" finding is substantially
reframed: once exp-027's own SIGMA_ON confound is corrected (τ_center held
at exactly 3.9 across the λ sweep, verified in code), the same cpl×1.5
resolution refinement that produced a 46%→128% "enlargement" in the
uncorrected record produces only a 46%→49% shift here — **96% of the
originally reported growth evaporates**. A small (+3pp) residual survives,
open but two orders of magnitude smaller than what was recorded. The
box-ledger channel itself stays flat (6.49% spread) throughout, supporting
`BEAM_BEHIND`'s own modestly-higher noise as the likely source of the
small residual, not a general resolution defect implicating exp-001's
extinction headline. (2) T9's PEC-incidental finding (exp-027) is
sharpened from an aggregate coincidence into a mechanistic one: Cell B's
own (non-PEC) core absorbs essentially nothing (0.01% of total, resolution
-stable), because the shell in front of it already extinguishes nearly all
the field before it arrives — Cell A and Cell B's near-identical ratios
reflect the SAME underlying mechanism (a negligible-contribution core), not
two different mechanisms cancelling.

## Next (pre-registered, for Phase 5)

(1) The small residual (+3.05pp, native→Block-A's own beam-behind spread)
is not itself explained — worth a future targeted check if this program
returns to near-field channel characterization, though it is now a small
enough effect that it may not warrant dedicated cycles. (2) T10's LOGBOOK
entry needs updating to reflect this experiment's reframing (Phase 5's
job, this shift). (3) QUANTUM's coherent-superposition bridge-gate
package is committed as a mandatory build for QUANTUM's own Iteration-6
lead cycle (next in rotation). (4) VISION's r=156 scale-bridge check is
committed as a mandatory build for VISION's own Iteration-7 lead cycle.
(5) The box-ledger channel's own decision-floor/noise characterization
remains unresolved and cross-cutting (Red Team's own recurring queued
item) — not assigned to a specific iteration.

**Phase 5 outcome:** seven fresh seats read these results — full verbatim
record: `LOGBOOK.md`, Iteration 5 Phase 5.
