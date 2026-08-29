# exp-088 — T28 Node Bracket + R13 Floor Gate

Panel Iteration 65. Lead: QUANTUM OPTICS (rotation). Executes Red Team's
own Iteration-65 reconciled ranking, Tier 1 items 1+3: an 8-call FDTD
bracketing follow-up at θ=38.4°/38.8° around exp-087's θ=38.6°
ENERGY-DOMINANT spike, folded with R13's new denominator floor gate
(zero marginal FDTD cost), applied both forward to the two new angles and
retroactively to exp-087's own three already-collected points. Full phase
record: `phase1_proposal.md` → five blind Phase-2 critiques (PHOTONICS,
MATERIALS, ELECTROMAGNETISM, THERMODYNAMICS, VISION SCIENCE, unanimous
support-with-changes, zero overlap) → `phase2_redteam_audit.md`
(PROCEED-WITH-MANDATORY-FIXES, 10 items, zero overridden) →
`phase3_synthesis.md` (this cycle's frozen spec, all 10 fixes adopted).

## Hypothesis

exp-087's PRIMARY result (`ratio_k`={2.64, 53.99, 5.71} at
θ={36.0°,38.6°,41.8°}) FALSIFIED its own pre-registered ENERGY-DECOUPLED
prediction, classifying ENERGY-DOMINANT — driven entirely by θ=38.6°,
which sits ≈0.01° from `delta_scene(θ)`'s own zero-crossing
(θ₀≈38.590°, exp-083's committed data). R13 (adopted the same cycle)
names exactly this hazard: a ratio classifier whose denominator derives
from a quantity with a real zero-crossing must be floor-gated before a
single-point decade classification is trusted. This cycle tests two
linked hypotheses: (1) that the ENERGY-DOMINANT reading is confined to
the immediate neighborhood of the θ=38.6° node rather than a broader
energy-coupling regime — tested by measuring `ratio_k` at the two
established-grid neighbors flanking the node on either side; (2) that
R13's floor gate, applied both prospectively and retroactively,
correctly reclassifies exp-087's own filed result.

## Setup

Reuses exp-087's `_load()` idiom (itself chaining through exp-083's
`run.py` for `dg`/`build_article`/`_run_sim`), `box_for`/`ref_for`,
`widths_direction_corrected()` (the sign-correction wrapper, unchanged —
identical `src_x>obj_x>plane_x`, -x-propagating geometry at every angle),
`_label`/`classify_resolved()` (the classifier bucket logic, unchanged,
its own synthetic-recovery check already validated by exp-087) — all
verbatim, zero geometry retyped. New code: two new angles
(θ=38.4°,38.8° = `dg069.DENSE_ANGLES[12]`,`[14]`), the R13 floor-gate
threshold and pre-filter (a boolean AND with the existing `resolved`
flag before an angle enters `classify_resolved()`), the retroactive
re-classification of exp-087's own three cited points against the same
floor, and — per Phase-2 fix items 7-8 — `netd_disposition` and the T9
`ratio_abs_ext` cross-check extended to the two new angles, reusing
values already required for the PRIMARY metric.

## Idealizations

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
   spot-check is run. Red Team's Phase-2 audit reviewed this explicitly
   and did not elevate it to mandatory (phase2_redteam_audit.md §6.3).
8. The `NOISE_MULT=3.0` box-dev multiplier and the `FLOOR_FRAC=0.10`
   denominator multiplier (below) are both house-style choices, not
   formally derived statistical thresholds — R13 explicitly permits
   this, requiring only that the convention be disclosed as such.
9. **NETD is an instrument/detector threshold, not a human-eye one** —
   any classification derived from `dt_ss_full_K` does NOT bear on
   constraint-3/4's human-eye verdict. *(Phase-2 fix item 1 — carried
   inline at every restatement below, not stated once and dropped.)*
10. **This cross-check bears only on T28's own confound-mechanism
    question and constraint-3's energy-ledger bookkeeping.** It does not
    test constraints 1/2/4, and does not re-open or re-score
    `REALIZABILITY_MEMO.md`'s verdict. *(Phase-2 fix item 1 — carried
    inline at every restatement below.)*
11. Not this cycle's mandate: Red Team's Iteration-65 ranking item 2 (the
    124-call full/denser individual-`σ_abs(C40,θ)`/`σ_abs(G40,θ)` build,
    MATERIALS' "passive transducer, not resonant source" test) is left
    queued, not folded in (phase1_proposal.md §7). PHOTONICS' own
    grazing-incidence validity check (still near-unanimous #1 on the
    whole T28 board) and the x-wall wavelength-generality leg (now
    THIRTEEN consecutive cycles deferred, 076–087) remain real, overdue,
    out-of-scope items.
12. The inverted `back_frac`/`fwd_frac` labels in
    `sections.py::widths()` (flagged forward by exp-087, non-blocking)
    are not read anywhere in this cycle's own scored quantities.
13. **`FLOOR`/`RMS[frac_contrast(θ)]` are specific to `graded_black_shell`
    /600nm and must be independently recomputed, not numerically reused,
    for any other absorber article or wavelength this gate is later
    applied to.** *(Phase-2 fix item 6, MATERIALS.)*

## The R13 floor gate, specified (unchanged from phase1_proposal.md §4)

**Quantity**: `frac_contrast(θ) = |delta_scene(θ)| / |C40_C(θ)|` — the
literal denominator of `ratio_k(θ)`.

**Threshold**: `FLOOR = FLOOR_FRAC × RMS[frac_contrast(θ)]` over
exp-083's own committed 31-point window, `FLOOR_FRAC=0.10`. Measured:
`RMS=1.91744×10⁻³`, `FLOOR=1.91744×10⁻⁴` — independently reproduced by
all five Phase-2 critics and Red Team's own audit, bit-exact.

**Gate rule**: an angle's `ratio_k(θ)` enters classification only if it
clears BOTH the existing box-dev noise-floor "resolved" test AND
`frac_contrast(θ)≥FLOOR`. A failing angle is reported
`NODE-UNRESOLVABLE`, excluded from `classify_resolved()`.

**Scope, per Phase-2 fix item 3 (PHOTONICS)**: this floor gate, applied
to the FULL 31-point window (desk-only, zero FDTD, computed by Red
Team's own audit), excludes only 1 of 31 points (38.6° itself) — the
threshold itself is not miscalibrated. But `delta_scene(θ)` has **four**
zero-crossings in the swept window (37.127°, 38.590°, 40.265°, 41.461°,
independently re-derived by PHOTONICS and Red Team from exp-083's raw
data), and the two established-grid points nearest the other three
crossings clear the floor by only **1.31×–1.48×** (θ=41.4°, 40.2°
respectively) — markedly tighter margins than the 7.49×/8.02× margins
of the two angles this cycle actually brackets (38.4°/38.8°). **This
cycle's own 5-point sample (36.0°, 38.4°, 38.6°, 38.8°, 41.8°) measures
`ratio_k` by real FDTD near only ONE of the four known near-zero
features — any CONSISTENT verdict this cycle produces is a claim about
behavior near that one node, not a claim about this channel's behavior
near near-zero-crossing regions in general.** See Next, below, for the
named forward-tripwire this requires.

**Bracket-width bound, per Phase-2 fix item 5 (ELECTROMAGNETISM)**: the
±0.2°/±0.4° bracket around θ=38.6° rules out only a genuine
energy-coupling feature **≳0.4° wide** — grounded in T28's own
established ~2.84°–2.95° periodicity as the physical reference scale
this bound is measured against (a feature narrower than this test's own
resolution, e.g. a critical-coupling-type resonance on the
absorbed-power channel specifically, which need not share the
ambient-contrast channel's linewidth, would not be ruled out by this
cycle). This test is a bound, not a "decisive" resolution of the
node-artifact-vs-genuine-physics question in the unqualified sense
phase1_proposal.md's own §1 first claimed.

**Historical-record disclosure, per Phase-2 fix item 9**: `experiments/
087-.../results.json`/`NOTES.md` remain the unedited historical record
of what the frozen Iteration-64 pipeline computed. This cycle's own
Q1 "CONSISTENT" reading (below) is a separate, disclosed, R13-corrected
reading, supplied for forward citation purposes alongside exp-087's own
filed record — not a retroactive edit of it. Any future citation of
"T28's energy-interception classification" must specify which of the
two it means.

**`NODE-UNRESOLVABLE` gloss, per Phase-2 fix item 10**: this label
refers to denominator-resolvability of one internal ratio construction
(`ratio_k`'s own denominator, `frac_contrast`), not a scene-visibility
or constraint-3 human-eye verdict.

## Predictions (frozen, committed BEFORE any Phase-4 code runs)

**Carried idealizations banner** (Phase-2 fix item 2, standing-practice
proposal): every prediction below is governed by Idealizations 9+10
(NETD is not a human-eye threshold; this cycle does not test constraint
3/1/2/4) and Idealization 13 (FLOOR/RMS are article/wavelength-specific)
— restated inline at each restatement, not only here.

1. **Q1 (desk, zero-FDTD, R13 floor gate applied retroactively to
   exp-087's own already-collected data — no new FDTD needed to score
   this; NETD-not-human-eye and constraint-3-not-tested disclaimers
   apply, Idealizations 9-10; scoped to the 5 sampled angles only, per
   Phase-2 fix item 3).** θ=38.6° reclassifies `NODE-UNRESOLVABLE`,
   excluded; θ=36.0° and θ=41.8° both clear the floor, remain
   `resolved=True`, label "C" (`ratio_k`=2.64, 5.71). **Predicted
   corrected classification of exp-087's own 3-angle primary result,
   under R13, at these 5 sampled angles only: CONSISTENT** (down from
   the filed ENERGY-DOMINANT) — supplied as a separate, forward-citable
   reading alongside exp-087's own unedited filed record (Idealization
   9-10, fix item 9), not a claim about the channel's behavior near
   near-zero-crossing regions in general (the other three known nodes
   remain FDTD-unsampled, see Next).

2. **Q2 (P1/P2/P4/non-negativity preconditions, new angles).** Predicted
   PASS at both new angles, both configs, both legs — identical
   construction to exp-087's own 12 cells, which cleared at margins of
   5-2,500× their own tolerances. HALT if any precondition fails.

3. **Q3 (floor gate, new angles — pre-registered, zero new FDTD;
   Idealization 13 applies — this FLOOR is `graded_black_shell`/600nm-
   specific).** Both θ=38.4° and θ=38.8° predicted to clear the R13
   floor gate (margins 7.49×/8.02× FLOOR).

4. **Q4 (PRIMARY, `ratio_k` at the two new angles — genuinely
   contingent on new FDTD, moderate confidence; NETD/constraint-3
   disclaimers apply, Idealizations 9-10; bracket-width bound applies —
   rules out only a feature ≳0.4° wide, not a decisive resolution of
   the node question in general, per the R13-floor-gate §
   "Bracket-width bound" above).** Linear interpolation of exp-087's
   own `frac_p_abs(θ)` between 36.0° (`1.9655×10⁻³`) and 41.8°
   (`7.2142×10⁻³`) gives central estimates `frac_p_abs(38.4°)≈4.14×10⁻³`,
   `frac_p_abs(38.8°)≈4.50×10⁻³` (this method reads ≈7.9% high at the
   interior 38.6° check, per exp-087's own data — a ±20% conservative
   band is used):
   - `ratio_k(38.4°)` predicted in **[1.5, 5.0]**.
   - `ratio_k(38.8°)` predicted in **[1.5, 5.5]**.
   Both predicted to classify "C" (CONSISTENT), clearing `RATIO_HIGH=10`
   with margin — NOT reproducing or approaching the 38.6° spike.
   Falsified if either reads `>10` (label "X", weakening the
   node-artifact explanation regardless of what the floor gate says
   about 38.6° itself) or `<0.1` (label "D", a surprising, independently
   flaggable new finding).

5. **Q5 (combined 5-angle picture, contingent on Q1+Q4 landing as
   predicted; NETD/constraint-3 disclaimers apply, Idealizations 9-10;
   scoped explicitly to the 5 sampled angles only — NOT a
   channel-general claim, per Phase-2 fix items 3-4).** If Q1 and Q4
   land as predicted, the combined floor-gated, resolved set across all
   five now-measured angles (36.0°, 38.4°, 38.8°, 41.8° cleared; 38.6°
   excluded as `NODE-UNRESOLVABLE`) is predicted to classify
   **CONSISTENT** — no angle reads "X", none reads "D". **This would be
   the first fully R13-compliant classification of T28's
   energy-interception channel across this ONE node's immediate
   neighborhood only** — it explicitly does NOT establish the channel
   is CONSISTENT near the other three known `delta_scene` zero-crossings
   (≈37.13°, ≈40.27°, ≈41.46°), which have never been FDTD-sampled for
   `ratio_k` at all (see Next). It supplies a separate, forward-citable
   reading alongside exp-087's own filed ENERGY-DOMINANT record — not a
   replacement of it (fix item 9).

6. **Q6 (P8/NETD extension, new angles — zero marginal cost, Phase-2
   fix item 7).** `netd_disposition` predicted UNDETECTABLE at both new
   angles, both configs — reusing the already-required `p_abs_w` values
   (THERMODYNAMICS' own Phase-2 recomputation found `p_abs_w` varies
   only ~18.5% across 36.0°→41.8°, comfortably inside a margin already
   ≈374×–442×). **NETD is an instrument/detector threshold, not a
   human-eye one — this does NOT bear on constraint-3/4's human-eye
   verdict** (Idealization 9).

7. **Q7 (T9 anchor cross-check extension, new angles — zero marginal
   cost, Phase-2 fix item 8).** `ratio_abs_ext = sigma_abs/sigma_ext`
   predicted in the same `0.51–0.52` band exp-087 measured at its own
   three angles (within 0.55%–0.75% of T9's established broadside
   anchor, 0.51) — informal context, not a scored falsifier.

**Non-negativity gate (hard assertion, not a scored prediction, unchanged
from exp-087):** `sigma_abs≥0`, `p_abs_w≥0` everywhere. HALT if violated.

## Next (forward tripwire, Phase-2 fix item 4 — named now, before any
Phase-4 result, so it cannot be silently dropped by a favorable outcome)

**Before any future LOGBOOK/PLAN.md entry describes T28's
energy-interception channel as CONSISTENT in a channel-general (not
merely 5-point/one-node-sampled) sense**, a future cycle must measure
`ratio_k` by real FDTD at the three other node-adjacent established-grid
angles: ≈37.1°/37.2° (nearest `delta_scene`'s zero-crossing at 37.127°),
40.2° (nearest 40.265°, floor margin only 1.48×), and 41.4° (nearest
41.461°, floor margin only 1.31×). This is a real, quantified gap this
cycle's own 8 calls do not close — named here explicitly so it is not
lost regardless of whether this cycle's own predictions land.
