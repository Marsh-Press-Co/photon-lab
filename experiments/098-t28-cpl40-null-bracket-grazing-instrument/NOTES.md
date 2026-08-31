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
