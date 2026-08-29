# PHASE 1 — PROPOSAL · Panel Iteration 65 · exp-088 · Lead seat: QUANTUM OPTICS

## "Bracket the Node, Gate the Ratio" — the decisive θ=38.4°/38.8° follow-up plus R13's floor gate, applied both forward and retroactively

### 1. Mechanism/method narrative (≤300 words)

**T1 escape route: N/A (T28 instrument work).** Like every T28 cycle since
exp-069, this makes no phenomenon-mechanism claim; it is instrument/
model-fidelity work on the bench's own energy-interception channel.

exp-087's PRIMARY result (`ratio_k`={2.64, 53.99, 5.71} at
θ={36.0°,38.6°,41.8°}) FALSIFIED its own ENERGY-DECOUPLED prediction and
classified ENERGY-DOMINANT — driven entirely by θ=38.6°, which sits
`≈0.01°` from `delta_scene(θ)`'s own zero-crossing (`θ₀≈38.590°`,
exp-083's committed data). That proximity is the exact hazard R13
(adopted the same cycle) names: a ratio classifier whose denominator
derives from a quantity with a real zero-crossing must be floor-gated
before a single-point decade classification is trusted. This cycle folds
two items together, because the second is only meaningful applied to
both the new and the already-collected data:

**(1) The 8-call bracketing follow-up.** Measure `ratio_k` at
θ=38.4°/38.8° — the established-grid neighbors flanking 38.6° on either
side of the zero-crossing, both already floor-clear (§4) — using
exp-087's own `widths()`/`widths_direction_corrected()`/thermo-chain
pipeline, verbatim. If ENERGY-DOMINANT is a genuine, spatially localized
regime, elevation should spread toward these neighbors. If it is purely
the disclosed node artifact, both should read CONSISTENT, comparable to
the already-measured 36.0°/41.8° values.

**(2) R13's floor gate, specified and applied both to the two new points
and retroactively to exp-087's own three already-collected points** — a
zero-marginal-cost rider. A gate that only ever protects future data,
never the flagged point that motivated it, is a weaker close than one
that resolves exp-087's own filed classification under the corrected
rule. §4 defines the exact threshold, grounded entirely in exp-083's own
already-committed 31-point window (zero FDTD to derive).

Item 2 of Red Team's Iteration-65 ranking (the 124-call full/denser
individual-`σ_abs` build) is scoped OUT of this cycle — argued in §7.

### 2. Parameter table

| Quantity | Value | Source |
|---|---|---|
| λ | 600 nm | consistent with the rest of the T28 window; no deviation |
| `dx_m` (grid pitch) | 30 nm | `dg069.CPL[600]=20` bench convention |
| Article | PEC disk r=30 + `graded_black_shell` r_in=30→r_out=78, `sigma_max=0.5, eps_max=1.0` | `materials.pec_disk`/`materials.graded_black_shell`, bit-identical to exp-024/082/083/087's `build_article()` |
| Configs | `C40`, `G40` — `dg065.CONFIGS["C40"]`/`["G40"]`, re-exported by `dg069`, imported via exp-087's own `_load()` idiom (which itself loads exp-083's `run.py` for `dg`/`build_article`/`_run_sim`) | `experiments/065-.../design_geometry.py` |
| New angles | θ ∈ {38.4°, 38.8°} = `dg069.DENSE_ANGLES[12]`, `[14]` (bracketing `[13]`=38.6°, already measured) | `dg069.DENSE_ANGLES` |
| STEPS | 2800 (`dg069.STEPS_SETTLED`) | same as exp-087's `STEPS_MAIN`; no new settling spot-check this cycle (§5, idealization 7) |
| `BOX_A` clearance | `R_OUT+12` cells | exp-024/exp-087's established convention, unchanged |
| `BOX_B` clearance | `R_OUT+24` cells | box-independence companion, unchanged |
| `REF` | `(obj_x, obj_y, 80)` per config | exp-024/exp-087's established convention, unchanged |
| `XI_TOL` | 0.12 | exp-087's stage-8 extinction-routes-agreement tolerance, unchanged |
| `NOISE_MULT` | 3.0 | exp-087's box-dev noise-floor multiplier (house-style), unchanged |
| `RATIO_LOW, RATIO_HIGH` | 0.1, 10.0 | exp-087's classifier decade bounds, unchanged |
| **R13 floor gate, quantity** | `frac_contrast(θ) = \|delta_scene(θ)\| / \|C40_C(θ)\|` — the literal denominator of `ratio_k(θ)` | same definition exp-087 already used |
| **R13 floor gate, threshold** | `FLOOR = FLOOR_FRAC × RMS[frac_contrast(θ)]` over exp-083's own established 31-point (36.0°–42.0°, 0.2° step) window, `FLOOR_FRAC = 0.10` | derived below, zero new FDTD |
| RMS of `frac_contrast(θ)`, n=31 | `1.91744×10⁻³` | computed from `experiments/083-.../results.json::per_theta`, all 31 angles (verified: `sqrt(mean(frac_contrast²))`) |
| **FLOOR (numeric)** | `0.10 × 1.91744×10⁻³` = **`1.91744×10⁻⁴`** | `FLOOR_FRAC × RMS` |
| `frac_contrast(38.4°)` (cited, zero new FDTD) | `1.43705×10⁻³` | `experiments/083-.../results.json::per_theta["38.4"]` (`delta_scene=8.08335×10⁻⁴`, `C40_C=-0.5624963`) |
| `frac_contrast(38.8°)` (cited, zero new FDTD) | `1.53753×10⁻³` | `per_theta["38.8"]` (`delta_scene=-8.56873×10⁻⁴`, `C40_C=-0.5573055`) |
| `frac_contrast(36.0°)`, `(38.6°)`, `(41.8°)` (retroactive, cited) | `7.43828×10⁻⁴`, `7.41006×10⁻⁵`, `1.26338×10⁻³` | `experiments/087-.../results.json::frac_contrast` (already computed there, cited not recomputed) |
| Total new FDTD calls | **8** (2 configs × 2 angles × {empty, article}) | — |

### 3. T1 escape route

**N/A (T28 instrument work).** Per this sub-thread's own disposition,
stated at Iteration 46's close and every cycle since: this is
instrument/model-fidelity work on the bench itself, not a phenomenon-
mechanism proposal. Checkpoint criterion 2 is N/A, matching every T28
desk/instrument cycle since exp-069.

### 4. The R13 floor gate, specified

R13 requires a house-style convention, disclosed as such, floor-gating
the denominator's "own absolute or amplitude-normalized magnitude" —
it does not hand down a number. This proposal grounds the gate directly
in `frac_contrast(θ)` itself (not the raw `delta_scene(θ)` it is built
from), since `frac_contrast` is the literal quantity `ratio_k` divides
by, and `|C40_C(θ)|` (the other factor in `frac_contrast`'s own
definition) is slowly varying and never itself near zero across the
window (`0.52`–`0.58` throughout) — the entire zero-crossing hazard is
inherited from `delta_scene(θ)`, so gating `frac_contrast` directly is
the most literal reading of R13's text.

**Threshold: `FLOOR = 0.10 × RMS[frac_contrast(θ)]`, RMS taken over
exp-083's own committed 31-point window.** `RMS` (not the median or the
raw amplitude/2) is chosen because it is a single, standard, order-
statistic-free measure of the curve's typical magnitude that is not
itself dominated by the handful of near-zero points the gate exists to
exclude — using the median would already be depressed by exactly the
kind of near-node points under scrutiny; using peak amplitude alone would
ignore how much of the window sits well below the extremes.
`FLOOR_FRAC=0.10` is a house-style choice, one decade below the curve's
typical scale, deliberately loose (mirrors exp-087's own `NOISE_MULT=3.0`
"house-style, disclosed" precedent, Idealization 8) — chosen so that a
point must specifically be within roughly a fifth of the curve's own
zero-crossing neighborhood to fail, not merely "smaller than average."

**Gate rule.** An angle's `ratio_k(θ)` reading enters classification only
if it clears BOTH gates: the existing box-dev noise-floor "resolved" test
(exp-087's own numerator-side gate, unchanged) AND
`frac_contrast(θ) ≥ FLOOR` (this cycle's new denominator-side gate). An
angle failing the floor gate is reported as its own outcome,
**`NODE-UNRESOLVABLE`**, excluded from `classify_resolved()`, never
silently scored alongside cleared angles — the pipeline change is a
pre-filter on the `resolved_ratios` list `classify_resolved()` already
consumes, not a change to `classify_resolved()`'s own bucket logic
(which stays bit-identical to exp-087's, re-verified by exp-087's own
already-passing synthetic-recovery check, reused unmodified).

**Desk-computable margins (zero FDTD, from the table above):**
- θ=36.0°: `7.438×10⁻⁴ / 1.917×10⁻⁴ = 3.88×` FLOOR → **clears**.
- θ=38.6°: `7.410×10⁻⁵ / 1.917×10⁻⁴ = 0.39×` FLOOR → **fails**.
- θ=41.8°: `1.263×10⁻³ / 1.917×10⁻⁴ = 6.59×` FLOOR → **clears**.
- θ=38.4°: `1.437×10⁻³ / 1.917×10⁻⁴ = 7.50×` FLOOR → **clears**.
- θ=38.8°: `1.538×10⁻³ / 1.917×10⁻⁴ = 8.02×` FLOOR → **clears**.

All five margins are computable today, before any Phase-4 code runs,
because `frac_contrast(θ)` depends only on already-committed exp-083 data
— the floor-gate PASS/FAIL calls below are genuinely pre-registered, not
merely the `ratio_k` values built on top of them.

### 5. Idealizations

1. 2 new angles (38.4°, 38.8°), not the full 31-point window — mirrors
   exp-087's own 3-angle-subset idealization (its Idealization 1).
2. Single λ=600nm, matching the rest of the T28 window (exp-087's
   Idealization 2, unchanged).
3. `iso_xsec_sq` area convention — object treated as compact, not an
   infinite rod (exp-087's Idealization 3, cited not re-litigated).
4. Silicon thermal constants (ρ, c_p) ASSUMED, provenance unsourced (T18)
   — reused verbatim from exp-057/exp-087 (exp-087's Idealization 4).
5. WitnessScenario irradiance/distance/candela WebSearch snippet-tier
   (T18), reused verbatim from exp-043/exp-087, not re-searched this
   cycle (exp-087's Idealization 5).
6. `ratio_k`'s decade tiers (0.1×/10×) remain a deliberately wide,
   first-of-its-kind falsification band, not a rigorously derived
   confidence interval (exp-087's Idealization 6, unchanged this cycle).
7. **Settling is NOT independently re-verified at 38.4°/38.8°
   specifically.** This cycle inherits exp-087's own STEPS=1400-vs-2800
   spot-check at the immediately adjacent angle (G40/38.6°,
   `rel_dev(sigma_abs)=7.9×10⁻⁵`) and exp-083's dense-grid settling
   precondition at nearby angles as evidence STEPS=2800 is adequate
   across this narrow ±0.2°/±0.4° neighborhood — no dedicated new
   spot-check is run. Flagged as a plausible Phase-2 mandatory-fix
   candidate, not preempted here.
8. The `NOISE_MULT=3.0` box-dev multiplier and the new
   `FLOOR_FRAC=0.10` denominator multiplier are both house-style choices
   (§4), not formally derived statistical thresholds — R13 explicitly
   permits this, requiring only that the convention be disclosed as
   such, which this table and §4 do.
9. NETD (P8-equivalent) is an instrument/detector threshold, not a
   human-eye one; nothing in this cycle bears on constraint-3/4's
   human-eye verdict (exp-087's Idealization 9, unchanged). This cycle
   does not re-run P8/NETD for the two new points — it is a corroborative
   context figure in exp-087, not load-bearing to this cycle's own
   scored predictions, and reusing the identical thermo chain at two more
   angles would not plausibly move a margin already ≈374×–442×.
10. This cross-check bears only on T28's own confound-mechanism question
    and constraint-3's energy-ledger bookkeeping; it does not test
    constraints 1/2/4 and does not re-open `REALIZABILITY_MEMO.md`'s
    verdict (exp-087's Idealization 10, unchanged).
11. Not this cycle's mandate: Red Team's Iteration-65 ranking item 2 (the
    124-call full/denser individual-`σ_abs(C40,θ)`/`σ_abs(G40,θ)` build,
    MATERIALS' "passive transducer, not resonant source" test) is
    explicitly left queued, not folded in — argued in §7. PHOTONICS'
    grazing-incidence validity check (still near-unanimous #1 on the
    whole T28 board) and the x-wall wavelength-generality leg (now
    THIRTEEN consecutive cycles deferred, 076–087) remain real, overdue,
    out-of-scope items.
12. The inverted `back_frac`/`fwd_frac` labels in
    `sections.py::widths()` (flagged forward by exp-087, non-blocking)
    are not read anywhere in this cycle's own scored quantities — same
    disclosure exp-087 made about its own scored quantities.

### 6. Pre-registered, falsifiable numeric predictions

All predictions below are committed BEFORE any Phase-4 code runs.

**Q1 (desk, zero-FDTD, R13 floor gate applied retroactively to exp-087's
own already-collected data — no new FDTD needed to score this).**
Applying §4's floor gate to exp-087's three points: **θ=38.6°
reclassifies `NODE-UNRESOLVABLE`, excluded**; θ=36.0° and θ=41.8° both
clear the floor and remain `resolved=True`/labeled "C" (CONSISTENT
bucket, `ratio_k`=2.64, 5.71 — neither exceeds `RATIO_HIGH=10` nor falls
below `RATIO_LOW=0.1`). **Predicted corrected classification of
exp-087's own 3-angle primary result, under R13: CONSISTENT** (down from
the filed ENERGY-DOMINANT) — `classify_resolved([2.64, 5.71])` has no
"X" label and not all-"D", landing CONSISTENT by the same bucket logic
exp-087's own synthetic-recovery check already validated. This
prediction is entirely desk-computable and is scored identically whether
or not the new FDTD calls below ever run.

**Q2 (P1/P2/P4/non-negativity preconditions, new angles).** Predicted
PASS at both new angles, both configs, both legs — identical
construction to exp-087's own 12 cells (same box/ref conventions, same
`Sim`/`build_article`), which cleared cleanly at margins of
5–2,500× their own tolerances. HALT if any precondition fails, exactly
as exp-087's own gating discipline.

**Q3 (floor gate, new angles — pre-registered from §4, zero new FDTD).**
Both θ=38.4° and θ=38.8° predicted to **clear** the R13 floor gate
(margins 7.50× and 8.02× FLOOR respectively, per §4) — i.e. neither new
point is predicted to land in `delta_scene`'s own near-zero
neighborhood. This is knowable today from exp-083's committed data alone
and is not contingent on this cycle's new FDTD calls.

**Q4 (PRIMARY, `ratio_k` at the two new angles — genuinely contingent on
new FDTD, moderate confidence).** Linearly interpolating exp-087's own
`frac_p_abs(θ)` between its two floor-cleared, non-node points (36.0° →
`1.9655×10⁻³`; 41.8° → `7.2142×10⁻³`) gives central estimates
`frac_p_abs(38.4°)≈4.14×10⁻³`, `frac_p_abs(38.8°)≈4.50×10⁻³`. exp-087's
own interior check at 38.6° (interpolated `4.318×10⁻³` vs. measured
`4.001×10⁻³`) showed this same linear-trend method reads ≈7% high at an
interior point — so a ±20% band around each central estimate is used
here to be conservative:

- `frac_p_abs(38.4°)` predicted in `[3.3, 5.0]×10⁻³` →
  **`ratio_k(38.4°)` predicted in `[2.3, 3.5]`**, band widened to
  **`[1.5, 5.0]`** to absorb additional uncertainty from the new box-dev
  noise floor not yet measured.
- `frac_p_abs(38.8°)` predicted in `[3.6, 5.4]×10⁻³` →
  **`ratio_k(38.8°)` predicted in `[2.3, 3.5]`**, widened to
  **`[1.5, 5.5]`**.

**Both predicted to classify "C" (CONSISTENT) — specifically, both
predicted to clear `RATIO_HIGH=10` with margin, i.e. NOT to reproduce or
approach the 38.6° spike.** This is the falsifiable core of the
bracketing test: if either new point instead reads `>10` (label "X"),
that is evidence the ENERGY-DOMINANT reading is not confined to a single
denominator-artifact point and the node-artifact explanation is
materially weakened, regardless of what the floor gate says about 38.6°
itself. If either reads `<0.1` ("D"), that would itself be a surprising,
independently-flaggable new finding (a genuine local dip in energy
coupling), not predicted by any smooth-trend argument above.

**Q5 (combined 5-angle picture, contingent on Q1+Q4 both landing as
predicted).** If Q1 and Q4 land as predicted, the combined floor-gated,
resolved set across all five now-measured angles (36.0°, 38.4°, 38.8°,
41.8° cleared; 38.6° excluded as `NODE-UNRESOLVABLE`) is predicted to
classify **CONSISTENT** overall — no angle reads "X", none reads "D".
This would be the first fully R13-compliant classification of T28's
energy-interception channel across the node's immediate neighborhood,
replacing exp-087's own filed ENERGY-DOMINANT headline with a corrected,
gate-respecting CONSISTENT reading, while explicitly not re-litigating
whether the true θ=38.6° point itself carries any real energy-dominant
physics (it remains formally unresolved-by-construction under this
gate, not adjudicated either way).

### 7. Scope decision: item 2 (full 31-point individual-σ_abs build) left queued

Red Team's Iteration-65 ranking item 2 — extending the channel to the
full/denser 31-point window, scoring `σ_abs(C40,θ)`/`σ_abs(G40,θ)`
individually — is a ~15× larger build (124 calls vs. this cycle's 8) and
answers a structurally different question (MATERIALS' "passive
transducer, not resonant source" test, about the channel's own smooth
θ-dependence generally) than this cycle's decisive, narrowly-targeted
node-artifact-vs-genuine-physics question. Folding it in would dilute
the falsifiability of the bracketing test's own pre-registered bands
(§6, Q4) behind a much larger, slower-to-review build, and — unlike
exp-076's `G0-e` companion or exp-087's own NETD-chain rider, both
genuinely zero/near-zero marginal cost — item 2 is not a zero-cost
rider by any reasonable accounting. Left queued for a future cycle,
named explicitly in Idealization 11, not silently dropped.

### 8. Frozen configuration — exact new FDTD call count

**8 new FDTD calls total**, all at STEPS=2800:

| # | Config | θ | Leg |
|---|---|---|---|
| 1 | C40 | 38.4° | empty |
| 2 | C40 | 38.4° | article |
| 3 | C40 | 38.8° | empty |
| 4 | C40 | 38.8° | article |
| 5 | G40 | 38.4° | empty |
| 6 | G40 | 38.4° | article |
| 7 | G40 | 38.8° | empty |
| 8 | G40 | 38.8° | article |

= 2 configs × 2 angles × 2 legs = 8. No settling spot-check call this
cycle (Idealization 7). The R13 floor gate itself (§4, and its
retroactive application to exp-087's data, Q1) costs **zero** additional
FDTD calls — it is computed entirely from already-committed
`experiments/083-.../results.json` and `experiments/087-.../results.json`
data.

Phase 4 will reuse, verbatim and unmodified: exp-087's `_load()` idiom
(itself chaining through exp-083's `run.py` for `dg`/`build_article`/
`_run_sim`), `box_for`/`ref_for`, `widths_direction_corrected` (the
sign-correction wrapper, unchanged — this geometry is the same
`src_x>obj_x>plane_x` `-x`-propagating case), `_label`/`classify_resolved`
(the classifier bucket logic, unchanged, its own synthetic-recovery
check already passing), and the full P1/P2/P4/non-negativity gate
sequence. The only new code is: the two new angles in `ANGLES`, the
`FLOOR`/`FLOOR_FRAC` constant and its gate check (a boolean AND with the
existing `resolved` flag before an angle enters `classify_resolved()`),
and the retroactive re-classification of exp-087's own three cited
`frac_contrast` values against the same `FLOOR`.
