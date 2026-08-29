# PHASE 1 — PROPOSAL · Panel Iteration 66 · exp-089 · Lead seat: VISION SCIENCE

## "Combined Angle Census" — the denominator-side node census and the numerator-side gap census, answered by one 3-angle set

### 1. Mechanism/method narrative (≤300 words)

**T1 escape route: N/A (T28 instrument work).** Like every T28 cycle since
exp-069, this makes no phenomenon-mechanism claim; it extends
instrument/model-fidelity work on the bench's own energy-interception
channel (`ratio_k(θ)=frac_p_abs(θ)/frac_contrast(θ)`).

exp-088 floor-gated `ratio_k` at 5 angles (36.0°, 38.4°, 38.6°, 38.8°,
41.8°) and found the true node (38.6°) NODE-UNRESOLVABLE while the other
four clear R13's floor gate — but θ=38.4°'s own reading (`ratio_k=0.908`)
missed its pre-registered `[1.5,5.0]` band, revealing `frac_p_abs(θ)`
itself is non-monotonic in a way this sub-thread had never sampled
densely enough to see coming. Red Team's own Iteration-66 ranking named
one combined follow-up: sample `ratio_k` near the three OTHER
`delta_scene` zero-crossings (never FDTD-measured — only desk-derived
from exp-083's scalar sweep) and inside the two large unsampled interior
spans (36.0°→38.4°, 38.8°→41.8°), "at once."

This proposal picks **θ = {37.2°, 40.2°, 41.4°}** — the tightest-floor-
margin grid neighbor of each remaining zero-crossing (37.127°, 40.265°,
41.461°) — and shows (§2, §4) that these same three points, by their
grid position, already do double duty as the gap census: 37.2° sits at
the exact midpoint of the 36.0°→38.4° gap; 40.2° and 41.4° together
subdivide the 38.8°→41.8° gap into three sub-spans, none exceeding
1.4°, comfortably under half of T28's own established ~2.84–2.95° period
(§4). One combined 3-angle set therefore answers both censuses at once,
at 12 new FDTD calls — inside Red Team's own "~8-16" estimate without
needing the wider "3 node + 2 gap = 20" overshoot the Director's brief
also authorized, and matching this deliverable's own "5 existing + your
new points = 8-point combined picture" framing exactly.

`phase1_proposal.md` alone is committed and pushed strictly before any
Phase-4 code exists, per this sub-thread's own restored git-provenance
discipline.

### 2. Parameter table

| Quantity | Value | Source |
|---|---|---|
| λ | 600 nm | consistent with the rest of the T28 window; no deviation |
| `dx_m` (grid pitch) | 30 nm | `dg069.CPL[600]=20` bench convention |
| Article | PEC disk r=30 + `graded_black_shell` r_in=30→r_out=78, `sigma_max=0.5, eps_max=1.0` | `materials.pec_disk`/`materials.graded_black_shell`, bit-identical to exp-024/082/083/087/088's `build_article()` |
| Configs | `C40`, `G40` — `dg065.CONFIGS["C40"]`/`["G40"]`, re-exported by `dg069`, imported via exp-088's own `_load()` idiom (which itself chains through exp-087's `run.py` → exp-083's `run.py` for `dg`/`build_article`/`_run_sim`) | `experiments/065-.../design_geometry.py` |
| New angles | θ ∈ {37.2°, 40.2°, 41.4°} = `dg069.DENSE_ANGLES[6]`, `[21]`, `[27]` (verified: indices confirmed against the live 31-point array) | `dg069.DENSE_ANGLES` |
| STEPS | 2800 (`dg069.STEPS_SETTLED`) | same as exp-087/088's `STEPS_MAIN`; no new settling spot-check this cycle (§5, idealization 6) |
| `BOX_A` clearance | `R_OUT+12` cells | exp-024/087/088's established convention, unchanged |
| `BOX_B` clearance | `R_OUT+24` cells | box-independence companion, unchanged |
| `REF` | `(obj_x, obj_y, 80)` per config | exp-024/087/088's established convention, unchanged |
| `XI_TOL` | 0.12 | exp-087/088's stage-8 extinction-routes-agreement tolerance, unchanged |
| `NOISE_MULT` | 3.0 | exp-087/088's box-dev noise-floor multiplier (house-style), unchanged |
| `RATIO_LOW, RATIO_HIGH` | 0.1, 10.0 | exp-087/088's classifier decade bounds, unchanged |
| **R13 floor gate, threshold** | `FLOOR = 1.91744×10⁻⁴` | reused verbatim from exp-088 (`FLOOR_FRAC=0.10 × RMS[frac_contrast]` over exp-083's own 31-point window) — zero new computation, this cycle adds no new points to the window the FLOOR is computed over |
| `frac_contrast(37.2°)` (cited, zero new FDTD) | `4.162655×10⁻⁴` | `experiments/083-.../results.json::per_theta["37.2"]` (`delta_scene=2.348254×10⁻⁴`, `C40_C=-0.564124`) |
| `frac_contrast(40.2°)` (cited, zero new FDTD) | `2.830881×10⁻⁴` | `per_theta["40.2"]` (`delta_scene=-1.540815×10⁻⁴`, `C40_C=-0.544288`) |
| `frac_contrast(41.4°)` (cited, zero new FDTD) | `2.510967×10⁻⁴` | `per_theta["41.4"]` (`delta_scene=1.337362×10⁻⁴`, `C40_C=-0.532608`) |
| Total new FDTD calls | **12** (3 angles × 2 configs × 2 legs) | — |

### 3. T1 escape route

**N/A (T28 instrument work).** Per this sub-thread's own disposition,
stated at Iteration 46's close and every cycle since: this is
instrument/model-fidelity work on the bench itself, not a phenomenon-
mechanism proposal. Checkpoint criterion 2 is N/A, matching every T28
desk/instrument cycle since exp-069.

### 4. How R13 and R14 apply to the new angles

**R13 (denominator floor gate) — desk-computable margins, all three clear:**

| θ | zero-crossing it brackets | `frac_contrast(θ)` | margin (× FLOOR) | floor_pass |
|---|---|---|---|---|
| 37.2° | 37.127° | 4.162655×10⁻⁴ | **2.17×** | PASS |
| 40.2° | 40.265° | 2.830881×10⁻⁴ | **1.48×** | PASS |
| 41.4° | 41.461° | 2.510967×10⁻⁴ | **1.31×** | PASS |

All three margins are known exactly today (desk-computed from already-
committed exp-083 data, no new measurement noise on this side of the
ratio) — these PASS calls are genuinely pre-registered, identical in
kind to exp-088's own §4 table. **None of the three is a comfortable
margin.** All three sit well below the already-measured points' own
range (36.0°: 3.88×; 38.4°: 7.49×; 38.8°: 8.02×; 41.8°: 6.59×) and
substantially closer, in relative terms, to 38.6°'s own failing 0.39×
than any previously-sampled point. 41.4° (1.31×) is the thinnest margin
of any angle this sub-thread has ever sent to FDTD for `ratio_k`. This
is by design — the whole point of the node census is to sample close to
a crossing without falling inside R13's own exclusion zone — but it
means these three points are the sharpest test yet of whether clearing
the floor gate is *sufficient* protection, not just necessary (§6, Q5).

**R14 (numerator subtractive-cancellation hazard) — the three-part
minimum discharge, applied:**

- **(a) Parent-quantity smoothness.** R14(a) requires verifying
  `p_abs_w(C40,θ)` and `p_abs_w(G40,θ)` are individually smooth/monotonic
  before trusting `frac_p_abs`'s difference. This is **not desk-checkable
  before Phase 4** — it requires the new FDTD data itself. Pre-registered
  here as a mandatory Phase-4 check (mirrors THERMODYNAMICS' exp-088
  Phase-5 decomposition), not silently deferred.
- **(b) Shared-config-pair risk, stated explicitly, fit declined.** C40/G40
  are the identical pair `delta_scene` is built from, and `delta_scene`
  is independently, twice-over, null-controlled to carry a genuine
  ~2.84–2.95° period (exp-083's own null-permutation control, `p=0.0`).
  This cycle explicitly **declines** to fit that period against the raw signed
  difference `p_abs(G40,θ)−p_abs(C40,θ)` (Red Team's own Iteration-65 Tier
  2 item, already named and left queued) — it instead runs a much cheaper,
  narrower single-recurrence check (§6, Q4) that needs no formal fit.
- **(c) No numerator extrapolation exceeding half a period without an
  interior check.** The combined 8-point angle set (5 existing + 3 new,
  sorted: 36.0°, 37.2°, 38.4°, 38.6°, 38.8°, 40.2°, 41.4°, 41.8°) has
  interior gaps of 1.2°, 1.2°, 0.2°, 0.2°, **1.4°**, 1.2°, 0.4°. Half of
  T28's own established period range [2.84°,2.95°] is [1.42°,1.475°].
  Every gap clears this bound — but the tightest, 38.8°→40.2° at 1.4°,
  clears it by only **0.02°–0.075°**, a near-exact match to the bound
  rather than a comfortable margin. Disclosed, not smoothed over: if a
  genuine sub-half-period feature lives in that specific 1.4° span, this
  cycle's own design would still miss it (Idealization 11).

### 5. Idealizations

1. 3 new angles (37.2°, 40.2°, 41.4°), not the full remaining 26
   unsampled grid points — a targeted census by design, not exhaustive
   coverage (mirrors exp-087/088's own subset idealizations).
2. Single λ=600nm, matching the rest of the T28 window.
3. `iso_xsec_sq` area convention — object treated as compact, not an
   infinite rod (exp-087's Idealization 3, cited not re-litigated).
4. Silicon thermal constants (ρ, c_p) ASSUMED, provenance unsourced (T18)
   — reused verbatim from exp-057/087/088.
5. WitnessScenario irradiance/distance/candela WebSearch snippet-tier
   (T18), reused verbatim, not re-searched this cycle.
6. **Settling is NOT independently re-verified at 37.2°/40.2°/41.4°
   specifically.** This cycle inherits exp-087's STEPS=1400-vs-2800
   spot-check at the immediately adjacent 38.6° angle
   (`rel_dev(sigma_abs)=7.9×10⁻⁵`) and exp-083's dense-grid settling
   precondition at nearby angles as evidence STEPS=2800 is adequate. No
   dedicated new spot-check is run.
7. `NOISE_MULT=3.0` and `FLOOR_FRAC=0.10` remain house-style, disclosed
   choices, not formally derived statistical thresholds (§4's own margin
   table is exactly the kind of evidence that would motivate revisiting
   `FLOOR_FRAC` in a future cycle, per §6 Q5).
8. **NETD (P8-equivalent) idealization, carried per the Iteration-65
   CHECKPOINT's escalated mandatory dual-section banner:** NETD is an
   instrument/detector threshold, not a human-eye one. Nothing in this
   cycle bears on constraint-3/4's human-eye verdict. This banner is
   stated here (Predictions-adjacent section) AND must be re-stated
   verbatim in any future Result/NOTES.md prose this proposal's Phase 4
   produces — the Iteration-65 firing exists precisely because a banner
   scoped to only one document section does not propagate to the other.
9. This cross-check bears only on T28's own confound-mechanism question
   and constraint-3's energy-ledger bookkeeping; it does not test
   constraints 1/2/4 and does not re-open `REALIZABILITY_MEMO.md`'s
   verdict.
10. R14(a)'s parent-quantity smoothness check (§4) is pre-registered as a
    mandatory Phase-4 obligation, not performed here — it requires data
    this proposal does not yet have.
11. R14(c)'s half-period interior-check bound (§4) is cleared by every
    combined-set gap, but the tightest (38.8°→40.2°, 1.4°) clears it by
    only 0.02°–0.075° — named explicitly as a residual open span for a
    future cycle to further subdivide, not hidden inside a passing
    aggregate check.
12. Not this cycle's mandate: Red Team's Iteration-65 ranking item 2 (the
    ~124-call full/denser individual-`σ_abs(C40,θ)`/`σ_abs(G40,θ)` build)
    remains explicitly queued, not folded in. PHOTONICS' grazing-incidence
    validity check (still near-unanimous #1 on the whole T28 board) and
    the x-wall wavelength-generality leg (now FIFTEEN consecutive cycles
    deferred, 076–089, this cycle included) remain real, overdue,
    out-of-scope items.
13. The inverted `back_frac`/`fwd_frac` labels in
    `sections.py::widths()` (flagged forward by exp-087, non-blocking)
    are not read anywhere in this cycle's own scored quantities.

### 6. Pre-registered, falsifiable numeric predictions

All predictions below are committed BEFORE any Phase-4 code runs.

**Q1 (desk, zero-FDTD, R13 floor gate).** All three new angles predicted
to **PASS** the floor gate: 37.2° (2.17× FLOOR), 40.2° (1.48× FLOOR),
41.4° (1.31× FLOOR) — per §4's table, entirely desk-computable from
already-committed exp-083 data, scored identically whether or not the
new FDTD calls below ever run.

**Q2 (P1/P2/P4/non-negativity preconditions).** Predicted PASS at all 3
new angles, both configs, both legs (12 cells total across BOX_A/BOX_B) —
identical construction to exp-087/088's own cells, which cleared cleanly
at margins of 5–2,500× their own tolerances. HALT if any precondition
fails.

**Q3 (PRIMARY per-angle `ratio_k`, genuinely contingent on new FDTD).**

- **θ=37.2° — CONSISTENT, band `[1.5, 9.0]`, moderate confidence.**
  Two interpolation methods bracket a central estimate: the local
  36.0°→38.4° linear trend gives `frac_p_abs(37.2°)≈1.63×10⁻³` →
  `ratio_k≈3.9`; the wider 36.0°→41.8° trend (the same method exp-088's
  own Q4 used, which itself missed by >3× at 38.4°) gives `≈3.05×10⁻³` →
  `ratio_k≈7.3`. The band is widened beyond either single estimate given
  the demonstrated unreliability of both interpolation schemes. Predicted
  to clear comfortably below `RATIO_HIGH=10`.
- **θ=40.2° and θ=41.4° — NO tight numeric band committed; qualitative
  prediction only, genuinely bimodal.** Naive linear interpolation across
  the 38.8°→41.8° span (the same method that already over-predicted
  `frac_p_abs(38.4°)` by >3×) gives central estimates `ratio_k≈20–28` at
  both points — i.e., **ENERGY-DOMINANT** under a naive smooth-trend
  reading. But that same method's own demonstrated failure mode at 38.4°
  argues against trusting it here. Given exp-088's own already-established
  warning against overconfident bands at exactly this kind of point, this
  proposal declines to pick a tight number for either angle and instead
  ties the prediction to the periodicity test below (Q4), which supplies
  an independent, cheaper discriminator than pure interpolation. **Primary
  directional lean: CONSISTENT is more likely than not at both** (4 of the
  5 already-measured angles read CONSISTENT; both new points sit at 1.3–
  1.5× FLOOR, comfortably clear of 38.6°'s own failing 0.39×) — but this
  is explicitly the lowest-confidence call in this document, and a miss
  here (either point reading `>10`) is pre-registered as the single most
  consequential possible outcome of this cycle (Q5).

**Q4 (periodicity-inheritance test — PHOTONICS' Phase-5 hypothesis from
exp-088, directly testable for the first time).** The combined angle set
supplies two independent, near-exact one-period (Δθ=3.0°, vs. T28's
established 2.84°–2.95°) recurrence pairs, neither requiring a formal
period fit:

- **Test A: 37.2° vs. 40.2°.** If `frac_p_abs` inherits the period,
  `frac_p_abs(40.2°)` should track `frac_p_abs(37.2°)`'s own reading
  (order `10⁻³`, roughly `1–3×10⁻³`) rather than the smooth 38.8°→41.8°
  trend (interpolated `≈6.5×10⁻³`). **CONFIRM signature:**
  `frac_p_abs(40.2°) < 3.3×10⁻³` (comfortably below the naive-trend
  estimate, tracking 37.2° instead). **REFUTE signature:**
  `frac_p_abs(40.2°) ≥ 5.5×10⁻³` (behaves as though continuing the smooth
  rise, no recurrence).
- **Test B: 38.4° vs. 41.4°.** If the 38.4° dip (`frac_p_abs=1.304×10⁻³`,
  the well-resolved non-monotonic feature exp-088 found) is a genuine
  recurring feature of the ~2.84–2.95° period rather than a one-off,
  `frac_p_abs(41.4°)` should show a comparable local dip relative to the
  38.8°→41.8° smooth trend (interpolated `≈7.05×10⁻³`). **CONFIRM
  signature:** `frac_p_abs(41.4°) < 3.0×10⁻³`. **REFUTE signature:**
  `frac_p_abs(41.4°) ≥ 6.0×10⁻³` (no recurring dip; smooth continuation).

**Both tests CONFIRMing is predicted to correlate with the Q3
CONSISTENT lean holding at both 40.2° and 41.4° (a low `frac_p_abs`
numerator keeps `ratio_k` low even at a thin-margin denominator); both
REFUTing is predicted to correlate with at least one exceeding
`RATIO_HIGH=10`.** This is a single-recurrence check, not a
null-controlled period fit (R5/R10's own look-elsewhere discipline still
applies to any FORMAL period claim) — it is reported as a directional
signal only, explicitly not a substitute for the still-queued desk fit
against the raw signed difference (Idealization 12/R14(b)).

**Q5 (the floor-gate-adequacy prediction — the sharpest test this cycle
registers).** If either 40.2° or 41.4° reads `ratio_k>10` despite
formally clearing R13's floor gate at only 1.31–1.48× FLOOR, that is
evidence `FLOOR_FRAC=0.10` is not fully protective near a zero-crossing
and should be tightened, or replaced with a graduated caution zone,
rather than treated as a binary pass/fail — a genuinely new
instrument-calibration finding, distinct from anything exp-087/088
tested (both of those cycles' floor-clearing points sat at ≥3.88×
margin, never below 3×). **CONFIRM signature (gate inadequate):** any
new angle reads `>10` while floor-clearing. **REFUTE signature (gate
adequate at this margin):** all three new angles read `≤10`.

**Q6 (combined 8-point classification, contingent on Q3).** If both
40.2° and 41.4° hold their Q3 CONSISTENT lean, the combined floor-gated
`resolved` set across all 8 now-measured angles (36.0°, 37.2°, 38.4°,
38.8°, 40.2°, 41.4°, 41.8° cleared; 38.6° excluded as
`NODE-UNRESOLVABLE`) is predicted to classify **CONSISTENT** overall —
extending exp-088's own Q5 CONSISTENT reading from 4 to 7 resolved
angles. If either 40.2° or 41.4° reads `>10`, the combined classification
flips to **ENERGY-DOMINANT** by `classify_resolved`'s own any-X veto
priority — the same mechanism that drove exp-087's original filed
result — and this would be a *second*, floor-clearing, non-artifactual
ENERGY-DOMINANT angle, materially undermining the single-node-artifact
reading this sub-thread has held since exp-088.

### 7. Frozen configuration — exact new FDTD call count

**12 new FDTD calls total**, all at STEPS=2800:

| # | Config | θ | Leg |
|---|---|---|---|
| 1 | C40 | 37.2° | empty |
| 2 | C40 | 37.2° | article |
| 3 | C40 | 40.2° | empty |
| 4 | C40 | 40.2° | article |
| 5 | C40 | 41.4° | empty |
| 6 | C40 | 41.4° | article |
| 7 | G40 | 37.2° | empty |
| 8 | G40 | 37.2° | article |
| 9 | G40 | 40.2° | empty |
| 10 | G40 | 40.2° | article |
| 11 | G40 | 41.4° | empty |
| 12 | G40 | 41.4° | article |

= 2 configs × 3 angles × 2 legs = 12. No settling spot-check call this
cycle (Idealization 6). The R13 floor gate itself (§4) costs **zero**
additional FDTD calls — computed entirely from already-committed
`experiments/083-.../results.json` data, unchanged from exp-088's own
`FLOOR` value.

Phase 4 will reuse, verbatim and unmodified, exp-088's own machinery
(itself chaining through exp-087's and exp-083's `run.py`):
`_load()`/`dg`/`build_article`/`_run_sim`, `box_for`/`ref_for`,
`widths_direction_corrected`, `_label`/`classify_resolved`,
`frac_contrast_of`/`compute_floor`, and the full P1/P2/P4/non-negativity
gate sequence. The only new code is: the three new angles in `ANGLES`
(asserted `== [37.2, 40.2, 41.4]`, mirroring exp-088's own
`assert ANGLES == [38.4, 38.8]` idiom), and the periodicity-recurrence
comparison (Q4) computed directly from the persisted `frac_p_abs` dict —
no new statistical machinery, no new null test.
