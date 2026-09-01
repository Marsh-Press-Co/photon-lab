# exp-098 — cpl=40 Null Bracketing (Three Remaining Nulls), Re-Centered
θ₀≈38.590230° Recovery, and a Genuinely θ-Dependent Grazing-Incidence
Instrument

*Panel Iteration 75. Lead seat (rotation): ELECTROMAGNETISM. Director
synthesis of `phase1_proposal.md` (EM) after five blind Phase-2 critiques
(PHOTONICS, MATERIALS, THERMODYNAMICS, QUANTUM OPTICS, VISION SCIENCE —
unanimous support-with-changes) and Red Team's Phase-2 audit
(PROCEED-WITH-MANDATORY-FIXES, 9 numbered attacks, 1 critique overridden
on its factual precedent, its recommendation adopted anyway on independent
grounds). Executes exp-097's own Reconciled Iteration-75 queue: Tier 0
(zero-FDTD fixes) run ALONGSIDE Tier 1 (real FDTD spend), not gating it.*

## Hypothesis

This is a T28 house-discipline/validation cycle, not a new T1 escape-route
proposal. It serves the already-committed **angular-selectivity** escape
route by determining whether the FDTD evidence backing that line's
`delta_scene(θ)` sign-structure claims (the 36°–42° window) is itself
trustworthy, now that exp-096/097's registration-readback gate has proven
the underlying construction code (`Sim`, `add_line_source`,
`r{3,4,5}_config()`) CLEAN and Tier-1 spend unanimously unblocked.

Two independent hypotheses are tested:

1. **Family-wide-defect vs. feature-specific migration.** exp-095's Rank
   1c found a FAIL (no sign change) at cpl=40 near one established cpl=20
   null (θ₀≈38.590230°). If the other three established cpl=20 nulls
   *also* fail to reproduce at cpl=40 (all four same-sign, floor-clear),
   that points toward a family-wide cpl=40 recipe defect. If some or all
   of the other three DO show a genuine sign change, that isolates
   38.590230° as the outlier, strengthening feature-specific migration —
   though MATERIALS' Phase-2 finding (adopted, Attack 6 below) means
   neither outcome, by itself, distinguishes genuine migration from
   unconverged discretization absent a convergence-order estimate.
2. **Grazing-incidence validity of the shared diffraction instrument.**
   The closed-form model (`edge_diffraction_c_empty_corrected`,
   exp-048/084/085) underlying every `delta_scene`/`frac_contrast`
   reading in this window has a known, already-quantified failure mode
   near θc≈59°–73° (exp-086, a 5,444×–6,631× amplitude blow-up from a
   missing UTD/shadow-boundary correction term). This cycle builds the
   first instrument that can actually SEE that failure mode across a wide
   sweep, rather than certifying validity blind to it.

A defect surfacing in either channel is a real, falsifiable, non-circular
outcome — not evidence against the registration-readback gate itself
(orthogonal: that gate verifies construction-time wiring, not physical
convergence or model domain of validity).

## Changes from Phase 1, per Red Team's Phase-2 audit (9 attacks; 5
mandatory fixes ADOPTED in full; 1 critique's precedent OVERRIDDEN, its
recommendation adopted anyway on independent grounds; 3 non-blocking
ADOPTs; 0 REJECT-level defects)

Director's ruling: Red Team independently re-verified every load-bearing
claim in all five blind critiques against source before ruling (spot-
checking `_geom_derived`'s signature, `L_GEOMETRIC_M_R4/R5`'s invariance,
`netd_row()`'s call sites, `_geom_derived`'s `y_src`/`y_obs` identity, and
the Phase-1 document's own word count) — none of the five verdicts below
rest on the critiques' word alone.

1. **Item (v) as Phase-1-specified cannot honestly discharge the
   grazing-incidence governance ask (PHOTONICS, escalated by Red Team to
   a proposal-level defect, Attacks 1–3) — REDESIGNED, not deferred.**
   Confirmed at source: `dg048._geom_derived(g)` takes no `theta`
   parameter — `kr_min(θ)` is the *same floating-point number*
   (70.05751617505238, numerically reproduced) for every one of the 21
   originally-proposed θ, because θ never enters the computation that
   produces `gd["r"]`. GP1's `weber()` ratio is scale-blind by algebra
   (`bo/bf−1`, a uniform blow-up in both numerator and denominator
   cancels). Neither check, as specified, could ever detect the
   already-quantified θc≈59°–73° blow-up sitting squarely inside the
   sweep — shipping a PASS/VALID-everywhere table row under that design
   would itself be exactly the "quietly certifies a constraint-adjacent
   claim while blind to a known failure" pattern this program's Red Team
   charter exists to prevent (Red Team's Attack 3, a foreseeable-risk
   framing, not a this-cycle constraint violation — constraints 1–4 are
   correctly N/A this cycle per Idealization 7). **Director's choice, per
   Red Team's own offered menu:** implement the θ-dependent replacement
   (Red Team's option 1), not the smaller "rescope and re-defer" option
   (option 2) — the replacement reuses the *same* already-verified
   `edge_diffraction_c_empty_corrected`/`FastEval` machinery with zero new
   formula and negligible marginal cost, and a twelfth deferral of an
   item already 10–11 cycles undischarged is the weaker call when the fix
   is this cheap. See §Setup, GP2′ below for the redesign.
2. **Item (iii)'s "same commit" netd_row() wiring is prose-only, not
   enforced (THERMODYNAMICS, Attack 5) — REPLACED with a build-time
   assert.** R16's own ratified text (a disclaimer "travels
   unconditionally, but is necessary, not sufficient: the byproduct
   itself must be persisted... for every cell/angle where it is
   computed") is not satisfied by a note that "Phase 2/3 can hold as a
   mandatory fix if the eventual `run.py` draft omits it" — that is
   detection-after-the-fact, not enforcement. `run.py` now raises before
   `results.json` is written if any of the 32 real-FDTD report rows is
   missing any of `netd_row()`'s 10 keys. **Note (Red Team's Attack 4,
   OVERRIDE):** THERMODYNAMICS' own cited precedent ("exp-095/Iteration-72
   already failed this exact `C40_R4`/`G40_R4` pairing once") does not
   hold up — the actual R16-founding near-miss was exp-094/Iteration 71,
   on the R3 (`C40_R3`/`G40_R3`) pairing, and exp-095 is independently
   confirmed CLEAN on this axis by its own Phase-5 THERMODYNAMICS review.
   The precedent claim is not repeated below; the assert is adopted on
   R16's own text alone, which needs no precedent to require it.
3. **MATERIALS' "false dichotomy" (Attack 6) — ADOPTED.** `cpl` is
   confirmed exclusively a grid-density parameter (`CPL={R3:30,R4:40,
   R5:50}`); `L_GEOMETRIC_M_R4`/`_R5` are asserted invariant to the
   native geometry to `1e-12` across families; no convergence-order
   estimate has ever been computed from the three now-available
   resolution points despite a non-monotonic-in-sign shift history
   (−0.194°/+0.320°/+0.377°). A third live possibility — unconverged
   discretization moving in a consistent direction without approaching a
   continuum value — is not distinguished from genuine migration by
   items (i)/(ii) alone. Added: a zero-marginal-cost, explicitly
   descriptive (NOT a formal Richardson order estimate — no continuum
   reference value exists to anchor one) pairwise-shift-ratio field,
   computed only where both a cpl20→cpl30 shift (on file) and a new
   cpl20→cpl40 shift (this cycle, if a crossing is found) exist for the
   same null.
4. **QUANTUM OPTICS' GP3 degeneracy (Attack 7) — ADOPTED, non-blocking.**
   `y_src`/`y_obs` are the literal same `np.arange(y_lo,y_hi)` array;
   `obliquity` is symmetric purely because one shared `d_sp` serves both
   roles — there was never a second, independently-defined observer-side
   obliquity to compare. GP3's write-up states this explicitly (not
   "symmetrized... or single-sided," which poses a question with only one
   live answer in this geometry) and confirms it with a direct
   `np.array_equal` assertion rather than resting on inspection alone.
5. **VISION SCIENCE's Result-banner gap (Attack 8) — ADOPTED.** The
   carried-idealizations banner below (§Idealizations) is restated at
   both Predictions (this document) and Result (once Phase 4 completes),
   naming both sections explicitly, with Phase 5's synthesis required to
   confirm this by grep before closing the cycle (not left to "applies
   automatically," the precondition VISION's own charter history shows
   let this gap recur).

Non-blocking cosmetic note (Attack 9, flagged for wording only, no fix
gate): §1's narrative undersold that a family-wide FAIL result is *also*
consistent with MATERIALS' unconverged-discretization reading; this
document's own Result section states both readings explicitly rather than
leaning on the "instrument-trust bookkeeping" framing alone.

## Setup

All FDTD calls reuse, unmodified: `Sim`/`add_line_source`
(`lab/fdtd2d.py`), `r{3,4,5}_config()`/`R{3,4,5}_CONFIGS`
(`experiments/069-.../design_geometry.py`), `cell_metrics_r4`/
`_run_sim_r4_sigma`/`run_block_r4`/`PAIR_KEYS_R4`/`BOX_CLEARANCE_{A,B}_R4`/
`PEC_R_R4`/`DX_M_R4`/`L_GEOMETRIC_M_R4` (`experiments/094-.../run.py`),
`pair_metrics_full`/`netd_row()` (`experiments/093-.../run.py`), and the
registration-readback gate (`run_checks_1234_and_7`,
`check5_recipe_spot_check_extended`, `check6_positional_and_cpl` —
`experiments/097-.../run.py`, CLEAN). λ=600nm (2D TMz) only, matching
Idealization 1. `dg.R4_STEPS=5600`, `SIGMA_R4_CORRECTED=0.25` (native
`0.5/R4_RATIO`, matching every prior R4-family call on file) for every new
real-FDTD point below.

### (i) Bracket the other three established cpl=20 nulls at cpl=40 — 24 calls

Established cpl=20 zero-crossings not yet tested at cpl=40 (re-pulled this
session from `experiments/090-.../results.json::q8.crossings_deg`, not
hand-typed — indices 0, 2, 3 of the four-element list; index 1,
38.590230°, is item (ii) below): **θ₀ᴬ=37.127246°, θ₀ᴮ=40.265420°,
θ₀ᶜ=41.460901°.**

Half-width **±0.500°** symmetric, per null — the same figure exp-096's
own desk bound computed and Red Team ratified against the three known
cpl20→cpl30 migration shifts (1.33×–2.58× margin), reapplied here for the
identical cpl20→cpl40 transition class rather than re-derived per null
(R4 discipline: don't re-litigate an already-audited figure). No
directional prior exists for these three (the migration set itself
contains both signs), so symmetric is the correct default.

4 angles per null, quartile-spaced (finer than the largest known shift,
0.377°, so a real crossing cannot hide between two same-sign samples):

| Null | θ₀ (cpl=20) | Test angles (cpl=40) |
|---|---|---|
| A | 37.127246° | 36.627246°, 36.960580°, 37.293913°, 37.627246° |
| B | 40.265420° | 39.765420°, 40.098753°, 40.432086°, 40.765420° |
| C | 41.460901° | 40.960901°, 41.294235°, 41.627568°, 41.960901° |

Family: `R4` only. Both legs (`C40_R4`/`G40_R4`) per angle → 3×4×2 =
**24 `sim.run()` calls.**

### (ii) Re-centered node-bracketing re-run at θ₀≈38.590230° — 8 calls

exp-095's own Rank 1c already ran 38.49°/38.69° (±0.10°, both FAIL,
same-sign) — filed, reused not rebuilt. **New angles: 38.09°, 38.19°,
38.29°, 38.39°** (0.10° spacing, matching exp-095's own step size),
extending the evaluated span to **38.09°–38.69°, 0.60° total ≥ the
R17-mandated 0.5° minimum**, lower-θ-weighted (5 of 6 evaluated points,
including the 2 reused, sit below θ₀) — justified by the one directly
analogous cross-resolution shift on file (the 40.265420° cpl=20→cpl=30
migration moved DOWN by 0.193582°; if 38.590230° migrates the same
direction, the new node sits below 38.49°, exactly where exp-095's own
bracket never looked; the opposite-direction analogy — the 41.460901°
crossing's own +0.320°/+0.377° migrations — is why this is a weighting,
not a certainty).

Family: `R4` only, both legs → 4×2 = **8 `sim.run()` calls.**

**Total real FDTD spend: 32 `sim.run()` calls**, each preceded by a
zero-cost registration-readback pre-check (`run_checks_1234_and_7` against
the exact intended `family`/`theta`/`cpl`/`config_key` for that point) —
extending the CLEAN gate's checked-point set beyond exp-097's 16-point
representative sample, per R18's own "earn coverage, don't just claim it"
discipline. `sim.run()` fires only if that pre-check reads CLEAN.

### (iii) netd_row() sidecar wiring — enforced, 0 new calls

Every one of the 32 report rows carries `**netd_row(pm)` (the 10-key
sidecar built from `pair_metrics_full`), merged in the same commit that
introduces the report-building code. `main()` asserts
`NETD_ROW_KEYS <= set(row.keys())` for all 32 rows before `results.json`
is written — a build failure, not a documentation note, if any row is
short a key.

### (iv) Tier-0 documentation/code-correction bundle — 0 FDTD calls

(a) **Idealization 40 correction** (exp-097's text superseded): `cpl_ok`
alone already discriminates every currently-possible family mislabel
among R3/R4/R5, since `CPL={R3:30,R4:40,R5:50}` is injective —
independently re-confirmed by QUANTUM OPTICS this cycle — not merely
"safe because gated behind `family_ok`" as exp-097's own text claimed.
(b) **Same-shift log**: QUANTUM OPTICS' own exp-097 Phase-5 self-review
independently repeated this exact mischaracterization — the first
instance of an R18-class scope error occurring inside a review document
itself, not a proposal. Logged here per T10 (flag, don't silently
rewrite the original document).
(c) **FI-G′** (new): corrupts `native_absorb` (41, not the true 40),
scored against all three families' `y_lo`/`y_hi` recomputation — closes
the gap that the original FI-G (native `src_x` corruption) left the
`y_lo`/`y_hi` branch of Check 5 with zero fault-injection coverage.
(d) **G40_* disclosure restated**: Check 5 has never tested any `G40_*`
(padded) config for any family, for any of exp-096/097/this cycle's own
fault-injection scenarios — restated with exp-096's original precision,
not narrowed.

### (v) Grazing-incidence instrument — REDESIGNED, 0 FDTD calls

Reuses `dg048.edge_diffraction_c_empty_corrected`/`_geom_derived`
(`experiments/048-.../design_geometry.py`) via `FastEval`
(`experiments/085-.../phase4_derivation.py`, verified bit-identical to the
original per-call function at 5 spot angles before use, per that module's
own mandatory pre-use check, re-run here). `CFG_C40`/`LAM600` (exp-085's
own geometry — the model's native fit geometry).

**Sweep**: θ ∈ [30°, 89.5°], 0.5° steps → **120 evaluations**, zero `Sim()`
constructions, no FDTD.

- **GP1 (passivity bound, unchanged from Phase 1).** `C(θ)=weber(bo,bf)
  ≥ −1−1e-6` at every θ — a hard passivity floor for this lossless,
  source-driven field superposition (no gain anywhere in the
  construction). Confident-lean PASS.
- **GP2′ (grazing-incidence amplitude-blowup instrument, REPLACES the
  original θ-independent `kr_min` classification).** At every swept θ,
  classify `|C(θ)|` against `median(|C(θ)|)` over the reference band
  θ∈[30°,50°] (comfortably inside the model's own original narrow-window
  fit range, per exp-084/085, and below the known θc≈59°–73° blow-up
  band): **VALID** (ratio ≤10×), **MARGINAL** (10×<ratio≤1000×),
  **INVALID** (ratio>1000×). The 10×/1000× bands are a new, disclosed
  instrument threshold (Idealization 51 below) — not yet cross-validated
  against `box_dev`/`xi_ext` the way this program's other gates have been
  — chosen so the check has genuine discriminating power against the
  already-quantified 5,444×–6,631× exp-086 blow-up (1000× sits one order
  of magnitude below that known severity) while staying well above
  ordinary numerical/floating-point noise (which should read as O(1)
  ratios). This is the SAME `C(θ)` values GP1 already reads, viewed a
  second way (magnitude vs. sign) — no new formula, genuinely
  θ-dependent by construction (`_src_amp(theta_deg,...)` enters `E`/`H`
  directly, unlike `gd["r"]`).
- **GP3 (reciprocity, code-read + assertion).** `_geom_derived`'s
  `y_src`/`y_obs` are the identical `np.arange(y_lo,y_hi)` call;
  `obliquity` is symmetric purely because one shared `d_sp` serves both
  roles — confirmed by direct `np.array_equal(gd["y_src"], gd["y_obs"])`
  assertion, not inspection alone. There was never a second,
  independently-defined observer-side obliquity to compare against in
  this geometry (QUANTUM OPTICS' degeneracy finding, adopted verbatim).

**Falsifiable claim (genuinely open, no confident lean):** if GP2′
classifies any θ MARGINAL/INVALID, report exactly which band and whether
it overlaps θc≈59°–73° — a real cross-check between this closed-form
model's own self-diagnosed domain and exp-086's already-measured,
independently-sourced blow-up. If GP2′ reads VALID everywhere, that is
itself a reportable, surprising non-replication via a different (but
overlapping) instrument, not swept aside.

## Idealizations

**Carried forward** (exp-096/097, cited by number, unchanged): 1 (2D TMz,
600nm only), 7 (no constraint-1/2/3/4 test, no T1 position this cycle —
Checkpoint criterion 2 is N/A), 17 (R3/R4/R5 share one mechanical recipe —
a family-wide defect in that shared recipe is not distinguishable from
independent per-family bugs by (i)/(ii) alone), 38/39/42 (Check 5 has
never tested any `G40_*` padded config, restated per item iv-d above).

**New this cycle:**

46. Items (i)/(ii)'s 4-point-per-bracket quartile design localizes a sign
    change to within ~0.33° of its true location if one exists inside the
    tested span — it does not certify the ABSENCE of a crossing outside
    that span.
47. The reused-not-rebuilt 38.49°/38.69° points (item ii) ran under
    exp-095's own construction code, byte-identical to this cycle's per
    exp-096/097's registration-readback gate — re-verified this cycle by
    running that same gate against their exact `(family, theta, cpl,
    config_key)` tuple, not merely asserted equivalent by reference.
48. Item (i)'s reused ±0.5° half-width is a direct reapplication of
    exp-096's own desk bound, not a fresh R17 derivation for these three
    specific nulls — defensible because the transition class (cpl20→cpl40)
    is identical, disclosed so a future audit does not read this as an
    independently-rederived figure.
49. MATERIALS' pairwise-shift-ratio field (§Setup item i) is explicitly
    descriptive, not a formal Richardson extrapolation / convergence-order
    estimate — no continuum (converged) reference value exists anywhere in
    this program's record to anchor one. It can show whether a shift is
    monotonically shrinking or not; it cannot, by itself, certify
    convergence.
50. GP2′ evaluates the CLOSED-FORM diffraction MODEL's own internal
    amplitude behavior — it is not a new FDTD measurement and cannot, by
    itself, tell apart "the model is invalid near grazing" from "the
    model is valid but the physical mechanism it represents genuinely
    vanishes near grazing." Distinguishing those needs a future FDTD
    point near any θ* this cycle flags, out of scope here.
51. GP2′'s 10×/1000× classification bands are a new instrument threshold,
    chosen to have genuine discriminating power against the already-known
    exp-086 severity (5,444×–6,631×) while staying well clear of ordinary
    numerical noise — disclosed as a fresh choice, not yet cross-validated
    against this program's other established gates (`box_dev`, `xi_ext`,
    `FLOOR_FRAC`) the way those were validated at their own founding
    cycles.
52. GP1/GP2′/GP3 are self-consistency and internal-amplitude checks on one
    closed-form model; they do not themselves re-derive or challenge the
    model's underlying physics (a bare Kirchhoff-Huygens coherent sum,
    already diagnosed by PHOTONICS at exp-086 as missing a UTD/
    shadow-boundary correction term) — they characterize WHERE that
    already-known limitation manifests in this specific sweep, which is
    the governance ask's actual scope.

**Carried idealizations banner: every prediction in this section
(§Predictions) AND this cycle's eventual Result section is governed by
Idealizations 1/7/17/38/39/42 plus this cycle's own 46–52. Phase 5's
synthesis must confirm this banner is present in BOTH sections by direct
grep before the cycle closes (VISION SCIENCE's fix, Attack 8).**

## Predictions (frozen before any Phase-4 code exists)

**Carried idealizations banner (duplicated here into the Predictions
section body itself, same-shift fix, Red Team Phase-5 final audit —
VISION SCIENCE found the §Idealizations closing paragraph named this
section without a banner sentence physically inside it): every
prediction below is governed by Idealizations 1/7/17/38/39/42 plus this
cycle's own 46–52 (§Idealizations above).**

| Item | Metric | Predicted band / criterion | Confident lean? |
|---|---|---|---|
| (i) A/B/C | `delta_scene(θ)` sign, all 4 angles/null, both legs | **PASS-family-clean**: all three nulls show a sign change *somewhere* inside their ±0.5° bracket → feature-dependent migration, matching θ₀=38.590°'s FAIL as the outlier. **FAIL-family-wide**: all three show NO sign change (same-sign, floor-clear) → points toward a family-wide cpl=40 recipe defect. No confident lean — genuine open question; per Idealization 17/MATERIALS' finding, EITHER outcome is also consistent with unconverged discretization, stated explicitly in Result regardless of which outcome obtains. |
| (i) | `floor_pass`/`ratio_k` | Every angle clears `FLOOR_FRAC=0.10` and `RATIO_LOW/HIGH=0.1/10.0` (matching every prior R4-family reading on file, zero exception to date). Confident lean: **PASS** at all 24 points. |
| (ii) combined (6 points: 4 new + 2 reused) | `delta_scene` sign across 38.09°–38.69° | **CONFIRM migration-down**: exactly one sign change, located below 38.49° (in {38.09,38.19,38.29,38.39}). **REFUTE-down / CONFIRM-neither**: no sign change anywhere in the full 0.60° span → strengthens (does not settle) the family-wide-defect reading from (i). No confident lean. |
| (iii) | `netd_row()` key coverage | All 32 rows carry all 10 keys, enforced by assert before `results.json` is written. Confident lean: **PASS** (design constraint, not physics). |
| (iv)(a)–(d) | Doc/code diff + FI-G′ | Confident lean: **CLEAN**, zero `results.json`/prior-verdict impact; FI-G′ predicted to be CAUGHT (y_lo/y_hi mismatch detected) at all three families. |
| (v) GP1 | `min(C(θ))` over 120 pts | **PASS band: ≥ −1.0−1e-6** at every θ. Confident lean: PASS. |
| (v) GP2′ | Per-θ VALID/MARGINAL/INVALID classification | Genuinely open. If any θ classifies MARGINAL/INVALID, report the band and whether it overlaps θc≈59°–73° (an a-fortiori cross-check against exp-086's independently-measured blow-up). If VALID everywhere, report that as a reportable non-replication, not swept aside. No confident lean either way — though a MARGINAL/INVALID reading somewhere near 59°–73° would corroborate, not surprise, given exp-086's own prior finding at this same underlying model. |
| (v) GP3 | `y_src==y_obs` assertion + degeneracy disclosure | Deterministic code fact, already independently confirmed twice (Red Team, QUANTUM OPTICS) before this run. Confident lean: **CONFIRMED, symmetric-by-construction, single live answer in this geometry**. |
| (i)/(ii) Richardson-style diagnostic | Pairwise shift ratio, nulls B/C only (A has no cpl=30 counterpart on file) | Reported only if a genuine crossing is found this cycle at B and/or C. No confident lean — explicitly descriptive (Idealization 49), not a convergence-order claim. |

**Total FDTD-call budget: 32 `sim.run()` calls** (24 item (i) + 8 item
(ii)), plus 32 zero-FDTD registration pre-checks (Checks 1–4+7, extending
the CLEAN gate) and 120 zero-FDTD closed-form evaluations (item v). Wall
time, scaling from exp-095's own 20-call/22.47-min pace: **≈35 minutes**
for the 32 real calls; item (v) adds under 30 seconds.

## Result

**Carried idealizations banner: this section is governed by Idealizations
1/7/17/38/39/42 plus this cycle's own 46–52 (§Idealizations above) —
restated here per VISION SCIENCE's own fix (Attack 8), confirmed present
in both Predictions and Result by direct grep before this cycle closes.**

**Correction, disclosed (R4 discipline, applied to this program's own
process, not just its physics claims):** this document's own §Setup/
§Predictions predicted **32** real `sim.run()` calls (24 item (i) + 8
item (ii)). The actual, necessary figure is **64** — an arithmetic error
that omitted the empty/article factor: each of the 16 angle/config
points needs BOTH an empty and an article `Sim` construction (matching
exp-095's own established `PAIR_KEYS_R4` × empty/article job-list
convention, e.g. its own 2-angle Rank 1c used 8 calls, not 4). This
undercount survived Phase 1's proposal, all five blind Phase-2
critiques, and Red Team's own Phase-2 audit — none of the seven seats
caught it. It was caught only by `run.py`'s own internal
`assert total_calls == 32`, which failed on first execution (`git log`:
the failing run's console output is superseded by the corrected one
below; the assert was corrected to 64 and the full run re-executed from
scratch, since the crash occurred before `results.json` was written —
no partial artifact existed to salvage without hand-typing figures from
console text, which this program's own R4 discipline forbids). Non-
load-bearing to any physics finding: the actual FDTD spend was always
the complete, correct 64-call set (both conditions are required to
compute `delta_scene` at all) — only the predicted/asserted count was
wrong. Logged for Phase 5 as a genuine process finding: this program's
own review pipeline (five blind critiques + Red Team) did not catch an
arithmetic error in a parameter table, only the code's own execution
did — worth Phase 5's explicit attention on whether this generalizes
(a call-count arithmetic check is currently nobody's assigned duty
across the seven charters).

**64 real FDTD calls, 8077.1s (134.62 min) wall time** (materially
longer than the ≈35-minute estimate scaled from exp-095's own pace —
disclosed as a container/hardware timing difference, not a physics
finding: a smaller validation batch, run separately before the full
spend, reproduced exp-095's own filed Rank 1c `delta_scene` values
**bit-exactly** at both 38.49° and 38.69°, confirming the pipeline
itself, not just its speed, matches precedent). Trust suite
re-confirmed green (41/41, `--only 12346789`) both before and after this
cycle's full close; zero `lab/` diff throughout.

**Item (i) — bracket the other three established cpl=20 nulls at
cpl=40: MIXED**, neither family-wide-clean nor family-wide-defect.

| Null | θ₀ (cpl=20) | Verdict | Crossing (cpl=40) |
|---|---|---|---|
| A | 37.127246° | **SIGN-CHANGE-FOUND** | ≈36.770358° |
| B | 40.265420° | **SIGN-CHANGE-FOUND** | ≈39.921519° |
| C | 41.460901° | **NO-SIGN-CHANGE** | — (same sign throughout, floor-clear at all 4 angles) |

All 12 angles (3 nulls × 4) cleared `floor_pass=True` and the
registration-readback pre-check CLEAN, at every one of the 48 real
calls those 12 angles required — no ambiguous-floor result anywhere in
item (i). Two of the three re-tested established cpl=20 nulls DO
reproduce a genuine `delta_scene` sign change at cpl=40; one does not.
Combined with θ₀≈38.590230° (item ii, below), **two of the four
established cpl=20 nulls now share the "no cpl=40 crossing inside a
naively-sized bracket" outcome, not one** — a materially different
picture than exp-095's own single-null FAIL suggested, though item (ii)
below shows that outcome is itself bracket-size-sensitive, so Null C's
own NO-SIGN-CHANGE here is not yet re-tested at a wider bracket (see
§Next).

**Item (ii) — re-centered node-bracketing re-run at θ₀≈38.590230°:
CONFIRM-migration-down.** A genuine sign change is found at
**θ≈38.252279°**, strictly below exp-095's own original 38.49°/38.69°
bracket (all 6 points in the combined 38.09°–38.69° span floor-clear):

| θ | 38.09° | 38.19° | 38.29° | 38.39° | 38.49° (reused) | 38.69° (reused) |
|---|---|---|---|---|---|---|
| `delta_scene` | +1.038×10⁻³ | +4.091×10⁻⁴ | −2.478×10⁻⁴ | −8.999×10⁻⁴ | −1.517×10⁻³ | −2.539×10⁻³ |

This **directly confirms the lower-θ-weighting hypothesis** stated in
§Setup: the one directly analogous cross-resolution shift on file (Null
B's own −0.194° cpl20→cpl30 migration, this cycle's own item (i)) DID
predict the right direction. exp-095's Rank 1c FAIL is now best read as
**a bracket-sizing failure (R17's own founding case, working as
intended one cycle later), not a genuine absence of a crossing** — the
true cpl=40 node for this feature sits ≈0.338° below θ₀, outside the
±0.10° window Rank 1c originally tested.

**MATERIALS' Richardson-style diagnostic (descriptive only,
Idealization 49 — no continuum reference exists, NOT a formal
convergence-order estimate):**

| Null | shift 20→30 | shift 20→40 | observed ratio | naive 2nd-order-accurate ratio | same sign? |
|---|---|---|---|---|---|
| B | −0.193581° | −0.343900° | **1.777** | 0.5625 | yes |
| A | no cpl=30 counterpart on file | — | — | — | — |
| C | not applicable (NO-SIGN-CHANGE this cycle) | — | — | — | — |

Only Null B has both shifts available. The observed ratio (1.78×) is
**same-sign but far from** the naive uniform-2nd-order-accuracy
expectation (0.5625×) — descriptively, the shift is GROWING faster than
2nd-order convergence would predict, not shrinking toward it. This is
flagged, not resolved: per Idealization 49, it does not by itself
distinguish genuine (non-monotonic-in-magnitude) physical migration
from a convergence order lower than 2, or from the near-null
sensitivity R15 already warned about. One data point cannot settle
this; a third resolution point at this SAME feature (cpl=50/R5, already
built at exp-095, explicitly deferred) is the natural next test.

**Item (v) — grazing-incidence instrument: a real, informative, mixed
result.** **GP1 (passivity): PASS**, `min(C(θ)) = −0.4405 ≥ −1` at all
120 swept points — no numerical defect. **GP2′ (redesigned amplitude
probe): flags MARGINAL** (10×–1000× vs. the θ∈[30°,50°] reference band)
continuously across **θ=50.5°–89.5°** — the ENTIRE upper half of the
sweep, not a narrow band — with **zero INVALID (>1000×) points**
anywhere in this specific curve. This flagged region **directly
overlaps** the already-known exp-086 blow-up band (θc≈59°–73°),
corroborating that finding via a structurally different instrument
(a wide, coarse 0.5°-step sweep of the full model here, vs. exp-086's
own narrow, fine-step windows centered at specific θc values there) —
but the severity differs: this instrument's worst ratio — **235.4×, at
θ=66.0°, itself squarely inside the exp-086 blow-up band** (verified
directly from `results.json::item_v.gp2_curve`, not hand-typed: I
initially drafted this as peaking near θ=89.5° and caught the error by
re-reading the actual array before freezing this section, R4 applied to
this very paragraph) — reads well below exp-086's own reported
5,444×–6,631×, an expected, disclosed difference: exp-086 measured
PEAK-TO-PEAK ripple within a narrow sliding window at fixed θc, this
instrument measures a single point value against a fixed reference band
— two different quantities probing the same underlying breakdown, not a
discrepancy to resolve, and this instrument's own peak landing INSIDE
the known band (not merely overlapping its edges) is a materially
stronger corroboration than "the flagged range overlaps." **This
cycle's own governance ask is genuinely, honestly discharged**: the
instrument is no longer a deterministic non-test (Red Team's Attack 1
is resolved — GP2′ produces a real, non-constant curve, `np.std` over
the 120 `ratio_to_ref` values is nonzero, independently checkable in
`results.json`), and it corroborates rather than contradicts the
already-known failure mode, rather than certifying PASS/VALID blind to
it. **GP3 (reciprocity): CONFIRMED degenerate**,
`y_src == y_obs` holds by direct assertion — the single live answer in
this geometry, as QUANTUM OPTICS found.

**`netd_row()` coverage: PASS** — the mandatory build-time assert
(`NETD_ROW_KEYS <= set(row.keys())`) held for all 64 real-FDTD report
rows (item (i) 48 + item (ii) 16, the reused 38.49°/38.69° rows
independently re-checked against the same key set from exp-095's own
already-filed data) — enforced, not merely disclaimed (R16, in full,
this time).

**Item (iv): CLEAN, exactly as predicted.** `check5_recipe_spot_check_extended()`
clean=True (reused from exp-097, unmodified). **FI-G′: CAUGHT at all
three families** (R3/R4/R5) — the `native_absorb` corruption (41, not
40) is detected via the `y_lo`/`y_hi` mismatch at every family. This
closes only the `absorb`-driven half of the y_lo/y_hi coverage gap — see
Phase 5 corrections item 7 below; it does NOT independently exercise
`native_ny`, as this section's own "closing the gap the original FI-G
left open" claim overstated (T10: flagged here, not silently rewritten).

## Phase 5 corrections (same-shift, Red Team final audit — flagged per
T10, not silently rewritten into the Result prose above)

All six blind Phase-5 reviews returned CONCUR-WITH-GAP(S); Red Team's
final audit independently re-verified every finding from source and
ADOPTED all six plus one bonus self-found defect (Idealization 47).
None changes a PASS/FAIL classification or a crossing value already on
file — all are zero-FDTD, zero-new-`sim.run()`-call prose/formula/
scoping corrections, applied via `phase5_same_shift_fixes.py` (which
recomputes every corrected figure from the actual committed function,
never hand-typed) plus this document. Full detail:
`phase5_redteam.md`.

1. **Richardson diagnostic (MATERIALS, adopted).** `richardson_style_diagnostic()`
   divided a CUMULATIVE cpl20→40 shift by a MARGINAL cpl20→30 shift — a
   category-mismatched comparison. **Corrected**: the properly-paired
   marginal-to-marginal ratio (cpl30→40 shift ÷ cpl20→30 shift) is
   **0.777** (SHRINKING, same sign), not the originally-reported 1.777
   (growing) — reversing the direction of the finding. Above (§Result,
   Null B's own Richardson row) and Learned #3's "growing faster than
   2nd-order... MORE open, not less" no longer hold: the corrected
   reading is mildly **reassuring**, not alarming — same-sign, and only
   ~38% off the naive 2nd-order-accurate expectation (0.5625) rather
   than 3.16× off in the wrong direction. `run.py`'s own function and
   call site are corrected at source; `results.json::richardson_diagnostic.B`
   now reports the corrected pairing.
2. **GP2′ Result overclaim (PHOTONICS + THERMODYNAMICS, independently
   convergent, adopted).** Above (§Result, item v), "flags MARGINAL
   continuously... the ENTIRE upper half" is factually wrong against
   `results.json::item_v.gp2_curve`: **9 VALID points are interspersed**
   in the 50.5°–89.5° band (52.0°, 52.5°, 53.0°, 53.5°, 54.0°, 54.5°,
   60.5°, 61.0°, 69.5°) — not a solid band. Notably **θ=69.5° reads
   VALID despite sitting INSIDE** the θc≈59°–73° corroboration band.
   Separately, the **74°–89.5° tail shows ZERO recovery** (0/32 points
   VALID) — a shape divergence from exp-086's own trend (which recovers
   below its pre-peak shoulder by θc=75°–77°) never surfaced in the
   original Result text (PHOTONICS). Exact counts now persisted at
   `results.json::item_v.gp2_band_exact_counts`.
3. **Row-count vs. call-count (THERMODYNAMICS + ELECTROMAGNETISM,
   independently convergent, adopted) — a THIRD instance of this
   cycle's own named error class.** Above (§Result), "held for all 64
   real-FDTD report rows" mislabels the call count (64) as a row count.
   The actual distinct row/data-point count is **16 new (18 including
   the 2 reused from exp-095)**; each row costs 4 real FDTD calls (2
   configs × 2 conditions) — `64 = 16 × 4`. `results.json` now carries
   `n_rows_new`/`n_rows_total_incl_reused` and a code-enforced assert
   (`fdtd_calls == n_rows_new * 4`) in `run.py`, per the new standing
   rule (below).
4. **GP1 framing (ELECTROMAGNETISM self-review, adopted).** Above
   (§Setup item v and §Result), "a hard passivity floor... for this
   lossless, source-driven field superposition" oversells its own
   derivation: `weber()`/`window_means()` (`lab/ambient.py`) compute a
   windowed mean of a signed local Poynting-vector component, not a
   closed-surface flux integral — passivity/energy-conservation theorems
   bound *net* flux through a closed surface, not one windowed local
   component in an interference pattern, where local backflow is
   ordinary. **The PASS result itself is correct**; only the physics
   justification was oversold. Corrected framing:
   `results.json::gp1_framing_correction`.
5. **Idealization 47 (THERMODYNAMICS' bonus find, independently
   confirmed by Red Team, adopted).** Idealization 47's claim that the
   reused 38.49°/38.69° rows were "re-verified this cycle by running
   that same [registration-readback] gate against their exact tuple"
   was FALSE as coded — `registration_preflight()` was only ever called
   with NEW angles. **Made true rather than written around**: the gate
   is now actually executed against both reused points
   (`results.json::item_ii.reused_points_registration_check`, CLEAN).
6. **Banner placement (VISION SCIENCE, adopted).** The Predictions-side
   carried-idealizations banner sentence is now duplicated directly
   inside the `## Predictions` section body (above), not only in the
   closing paragraph of `## Idealizations` that names it.
7. **FI-G″ (QUANTUM OPTICS, adopted — ruled by Red Team as the single
   finding this audit weighs most heavily, "closest call" under
   Checkpoint criterion 4).** FI-G′ (`native_absorb` corruption) moves
   `y_lo` and `y_hi` TOGETHER (`y_hi = ny − y_lo`), so it only ever
   exercises the `absorb`-driven half of that branch. `native_ny` — the
   only input that can move `y_hi` INDEPENDENTLY of `y_lo` — had zero
   fault-injection coverage across this program's entire history, and
   exp-097's own Next queue had named exactly this scenario (`FI-G″`,
   "optional, cheap to bundle") one cycle earlier; exp-098 dropped it
   without disclosure. **Executed now, not deferred**: `native_ny`
   corrupted to 1585 (true: 1584), scored against all three families —
   CAUGHT at every family, and independently confirmed `y_lo` stays
   unmoved by this corruption (`results.json::item_iv.fi_g_double_prime`).
8. **GP2′/exp-086 "structurally different instrument" disclosure
   (QUANTUM OPTICS, adopted).** §Result's "corroborating... via a
   structurally different instrument" is now qualified:
   `results.json::gp2_vs_exp086_disclosure` states plainly that GP2′ and
   exp-086's own `ptp` method are two post-processing statistics on the
   IDENTICAL closed-form formula, not independent physical instruments —
   real corroboration of the same underlying model behavior, not two
   separate measurements of reality.

**New standing rule, ADOPTED NOW** (Red Team's explicit exception to
this program's usual cross-cycle recurrence-before-ratification cadence,
justified by the within-cycle recurrence strength — see `phase5_redteam.md`
§3): *any results table, Result-section prose, or Learned/Next item that
states a count of FDTD calls, report rows, or data points must be backed
by an explicit, checkable assert distinguishing call-count from
distinct-row/data-point-count wherever both exist in the same
computation — a code-enforced invariant, not a reviewer's manual
cross-check.* `run.py` now implements this assert
(`fdtd_calls == n_rows_new * 4`, `n_rows_new == 16`,
`n_rows_total_incl_reused == 18`).

**Checkpoint criterion 4 ruled the closest call this program has had
(Red Team's own words) but does NOT fire**: every defect above,
including the FI-G″ undisclosed drop, was caught blind by this same
cycle's own six-seat-plus-Red-Team review process before Iteration 76
opens — matching this program's established R16/R17/R18 non-firing
precedent. Red Team's own warning: a fourth instance of the count-
conflation class, or any confirmed-but-undisclosed dropped commitment
surviving uncorrected into a future cycle's LOGBOOK entry, should fire
criterion 4 without further warning. **All five checkpoint criteria: do
not fire** (1/2 N/A — no T1 candidate under test; 3 N/A — zero engine
physics beyond the validated bench classes; 5 N/A — genuine logbook-
advancing content this cycle, independent of every corrected defect).

**Combined Verdict: PROMISING** (Red Team's final ruling, upgraded from
this Director's own draft framing) — both of this cycle's stated goals
were substantively achieved in the underlying data (item i/ii's real
MIXED migration result, and the 11-cycle-old grazing-incidence
governance ask genuinely, honestly discharged), and every confirmed
defect is a zero-FDTD, non-load-bearing correction that changes no
PASS/FAIL classification or crossing value already on file.

## Learned

1. **This program's own five-blind-critique-plus-Red-Team review process
   has a real, demonstrated blind spot: parameter-table arithmetic.**
   Six independent seats read the same "32 calls" table and none
   flagged that it omitted the empty/article multiplier — every seat's
   own discipline-specific lens (optical coherence, realizability,
   energy budget, expressibility, perceptual thresholds, internal
   consistency) had no natural angle on "does this multiplication check
   out." Only the code's own execution caught it. Candidate fix for a
   future cycle's governance docket: assign call-count arithmetic
   verification explicitly (a natural fit for whichever seat is
   already checking `results.json`'s own `fdtd_calls` field against the
   frozen prediction — currently nobody's stated duty). **[Phase 5
   correction: this blind spot recurred a SECOND time within this same
   Result section — see "Phase 5 corrections" item 3 above — and Red
   Team ADOPTED a new standing rule NOW, as an explicit exception to the
   usual cross-cycle cadence, making this a code-enforced assert rather
   than an assigned human duty.]**
2. **R17's bracket-sizing discipline, adopted one cycle after its own
   founding defect (exp-095's undersized ±0.10° bracket), worked exactly
   as intended one cycle later**: item (ii)'s wider, lower-θ-weighted
   bracket found the crossing exp-095's own narrower bracket missed.
   This is the sub-thread's first fully-worked example of an R-rule
   closing the exact gap it was written for, not just preventing a
   repeat in the abstract.
3. **"Genuine migration vs. family-wide recipe defect" (this cycle's own
   Hypothesis 1) resolved to neither cleanly** — it is feature-dependent
   (2 of 3 tested nulls migrate, 1 does not, matching θ₀≈38.590230°'s
   own now-resolved migration) but MATERIALS' own Phase-2 finding stands
   unrefuted: without a convergence-order estimate, "migrates" and
   "hasn't converged" remain observationally similar for any single
   pairwise comparison. ~~The Richardson-style diagnostic's own surprising
   direction (growing faster than 2nd-order, not shrinking toward it)
   makes this MORE open, not less~~ — **[Phase 5 correction: this
   sentence rested on a mis-paired ratio (cumulative/marginal, not
   marginal/marginal — see "Phase 5 corrections" item 1 above). The
   corrected marginal-to-marginal ratio is 0.777 (shrinking, same sign),
   mildly REASSURING, not alarming. The underlying open question
   (migration vs. non-convergence, MATERIALS' own finding) still stands
   — it is just not sharpened in the direction this sentence claimed.]**
   — a genuine, disclosed, unresolved
   finding for the next cycle.
4. **A redesigned, genuinely θ-dependent instrument found something a
   vacuous one could not, and it corroborated rather than contradicted
   prior work.** This is the sub-thread's first cycle in several to
   report a new, substantive FDTD-adjacent physics finding (rather than
   another registration/gate-integrity result) — the grazing-incidence
   governance ask, live since Iteration 64 (11 cycles), is genuinely
   closed this cycle, not deferred a 12th time.

## Next (Reconciled Iteration-76 queue — FINAL, per Red Team's Phase-5
audit, superseding the Director's own draft above; origins cited per
`phase5_redteam.md` §5)

1. **Null C re-test at a wider, R17-compliant, asymmetric bracket,
   explicitly scoping a "vanishing amplitude, no crossing at any
   reasonable width" outcome as a live third result** (not just "wider
   bracket will find it"). *Origin: Director's own draft (above, item 1),
   independently ranked #2 by EM/THERMODYNAMICS/VISION; PHOTONICS'
   additional vanishing-amplitude hypothesis (Null C's decelerating
   `delta_scene` curve) folded in as an explicit alternative to test for.*
   Five of six seats converge on this as the most physics-load-bearing
   open thread — item (ii) just proved a same-sized-but-mis-centered
   bracket produces a false NO-SIGN-CHANGE, and Null C's current verdict
   rests on exactly that untested failure mode.
2. **The cpl=50/R5 third resolution point at Null B (and/or
   θ₀≈38.590230°)**, reusing exp-095's already-built family, run against
   the CORRECTED marginal-to-marginal Richardson formula (Phase 5
   correction item 1 above), not the miscomputed one. *Origin:
   Director's own draft (above, item 2), PHOTONICS #3, EM #3, MATERIALS
   #2 (explicitly gated on the formula fix landing first — now landed).*
   Zero new `Sim` family construction; the only genuine path to an
   actual (still non-formal, per Idealization 49) convergence read at
   one feature.
3. **Reconcile GP2′ against exp-086's own sliding-window `ptp` method,
   extended through the 74°–89.5° tail** (not just the originally-swept
   59°–73° band) at matched θ range, zero-FDTD, reusing exp-086's method
   verbatim — explicitly scoped to also state whether the severity gap
   (235× vs. 5,444×–6,631×) is fully explained by the differing statistic
   or partially by something else. *Origin: Director's own draft (above,
   item 3), QUANTUM OPTICS #3, PHOTONICS #1 (extending the pre-existing
   scope to cover the tail divergence this seat found).*
4. **Ratify the call-count/row-count arithmetic-assert standing rule**
   (already adopted this cycle, see "Phase 5 corrections" above) into
   `LOGBOOK.md`'s numbered R-rule sequence. *Origin: Director's own draft
   (above, item 4), THERMODYNAMICS #1 (promote candidate→committed),
   VISION #3 (calibration: a code-enforced invariant, not a new
   attentional/duty burden on any one seat).*
5. **State the cpl-is-orthogonal-to-realizability finding explicitly in
   a future Result section**, and revisit the standing T1-route-N/A
   governance flag (six consecutive cycles, exp-094 through exp-098,
   zero new FDTD evidence bearing on any realizability parameter) at the
   next Phase 3 checkpoint. *Origin: MATERIALS #3.* Not a forcing
   function for a T1 proposal this cycle, but the flag has outlived its
   own originally-cited precedent count without a Result-section-level
   re-raise.
