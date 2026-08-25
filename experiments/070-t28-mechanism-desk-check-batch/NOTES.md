# exp-070 — T28 Mechanism Desk-Check Batch

**Panel Iteration 47.** Lead: QUANTUM OPTICS (by rotation). Director
synthesis post Phase 2 (five blind critiques + Red Team's Phase-2 audit,
verdict PROCEED-WITH-MANDATORY-FIXES, 10-item docket, **zero overridden**
— full record in `phase1_proposal.md`, `phase2_critique_{photonics,
materials,em,thermodynamics,vision}.md`, `phase2_redteam_audit.md`,
`phase3_synthesis.md`).

## Mandate

PLAN.md's Iteration-47 queue, item 1: a single zero-FDTD-cost desk-check
batch on live thread **T28** — the real, resolution-robust-at-two-points,
settled ~2.84° periodic oscillation in the `C80−C40` padding delta (600nm,
θ∈[36°,42°]), opened by exp-069, that does NOT match T21's own established
fringe period `P(θ)=λ/(A·cosθ)≈1.96°`. Red Team's own standing forward
tripwire (exp-069 Phase-5 final audit): T28 must receive at least this
cheap, desk-only first move by Iteration 48's close, or the gap itself
becomes Checkpoint-4-adjacent.

## Setup

Reads ONLY already-committed data — **zero new FDTD calls, zero `lab/`
diff**:
- `experiments/069-.../results.json` — `block_dense.rows` (600nm, 31 pts,
  θ=36–42°), `block_leg750.rows` (750nm, 16 pts, θ=38–41°), `scored.p3`
  (the committed free-fit period of the padding delta, `P*_delta=2.8421°`,
  `R²=0.6272`).
- `experiments/065-.../design_geometry.py` — `CONFIGS["C40"]`/`["C80"]`,
  the 14 NAMED domain-construction constants (see below).
- `experiments/069-.../run.py` — `_fixed_period_fit`/`_free_period_search`,
  imported verbatim, never re-derived.

Five items, all engaged (none dropped from the Phase-1 proposal's
mandate-derived list):

- **(a) Per-config decomposition** — does the ~2.8°-family signature
  already live in `C40(θ)` and/or `C80(θ)` individually, not only in the
  difference?
- **(b) Beat-frequency reconstruction** — solve `1/P_beat=|1/P(39°,600nm)
  −1/P*_delta|` for both branches, convert to an effective aperture
  `A_alt`, search the 14 NAMED constants for a match.
- **(c) Taper-as-second-aperture check** — does `TAPER=40` cells alone, as
  a diffracting sub-aperture, predict a period near `P*_delta`?
- **(d) `A_eff` systematic trace** — back-solve `A_eff` from `P*_delta`
  directly, search NAMED for a match, cross-validate the best candidate
  against the held-out 750nm leg.
- **(e) Convergence check** — do (b)'s and (d)'s matches name the same
  NAMED combination?

**NAMED constants (14, all read programmatically from `CONFIGS`, none
hand-typed):** `A=752`, `TAPER=40`, `R_OUT=78`, `W_OBJ=78`,
`GUARD_OUT=185`, `W_FLANK=78`, `D_SP=223`, `LEVER=93`,
`aperture_cells=1504`, `clear_plane=37`, `clear_src=20`, `ABSORB40=40`,
`ABSORB80=80`, `PAD80=40`. Search space: all single terms (`c·x`,
`c∈[-10,10]\{0}`, 280 expressions) and pairs (`c1·x1+c2·x2` over distinct
unordered name-pairs, 36,400 expressions) — **36,680 total, 7,179 distinct
values** (reproduced independently by PHOTONICS, MATERIALS, and Red Team's
Phase-2 audit; verified again here by `design_geometry.py::build_search_space`).

## Mandatory disclosed caveat (docket item 5 — applies regardless of any
## item's outcome, CONFIRM, REFUTE, or NEITHER)

**No outcome of items (b), (d), or (e) bears on realizability or
establishes a physical diffraction mechanism.** Every one of the 14 NAMED
constants is this bench's own FDTD domain-construction bookkeeping (grid
padding, graded-loss absorbing-boundary depth — **not PML**, per
VALIDATION.md's own documented construction — taper length, window/guard
clearances), not a material or physical-optics parameter. A numeric match
between a recovered length scale and some combination of these constants
is at least as consistent with a numerical-boundary-construction artifact
of this engine's own graded-loss absorbing boundary as with a physically
real diffracting edge (MATERIALS' Phase-2 finding, Red Team-adopted in
full).

## Disclosed pre-registration caveat (docket item 7)

The Phase-1 proposal's own disclosed desk reconnaissance found
`A_alt≈233.19` (0.35% from `3·R_OUT=234`) and `A_eff≈518.81` (0.16% from
`A−3·R_OUT=518`, `R²=0.7666` at 750nm) **before** the 1%/0.70 CONFIRM
thresholds were finalized in this document — i.e., the thresholds were
set with these specific numbers already known, not blind. This is exactly
why docket item 2's permutation-null control, not the raw threshold
distance, is the actual gate on items (b)/(d)/(e): a raw-threshold CONFIRM
here would be indistinguishable from HARKing (VISION's finding); a
null-controlled `p≤0.05` is not, regardless of how the threshold itself
was chosen.

## Disclosed scope choice (docket item 6)

PLAN.md's Iteration-47 queue item 1 named a capacity-permitting fold-in:
"THERMODYNAMICS' own desk-only WKB/adiabatic boundary-reflectance model
for the graded-loss `ABSORB` band." **Not picked up this cycle.** No
capacity constraint prevented it — this is a scope choice (the batch as
designed answers a geometric/statistical question, not a boundary-physics
one), disclosed rather than silent, per Red Team's Attack 6 ruling.

## T1 escape route

**N/A** — instrument/model-fidelity class, identical in kind to
exp-041/065/066/068/069. No mechanism proposed against constraint 3;
Checkpoint-criterion-2 candidacy explicitly declined for every outcome.

## Idealizations

1. 2D TMz, single polarization.
2. Desk-only, zero new FDTD — pure arithmetic over already-committed data.
3. Reuses only the 600nm DENSE block's 31 points and the 750nm LEG750's
   16 points — no new angles, λ, resolution, or settling checks (P-069-4/5
   already CONFIRMED, carried forward unchanged).
4. `R_OUT` and `W_OBJ` are numerically degenerate at this bench's own
   geometry (both 78 cells) — any match against `R_OUT` is equally a
   match against `W_OBJ`; this batch cannot distinguish "object radius"
   from "measurement-window half-width" as the physically loaded
   quantity, if either is real at all (see mandatory caveat, above).
5. The NAMED search space is bounded to single terms and pairs with
   `|c|≤10` — a three-or-more-term combination, or a non-integer physical
   ratio, is out of scope and would not be found even if real.
6. The beat-frequency formula (item b) assumes a genuine two-tone linear
   superposition; the candidate periods (~1.96° vs ~2.84°) are comparable
   order over a ~3-period window, so a null result does not rule out a
   related but non-additive (e.g. modulated-envelope) mechanism.
7. Numerology-vs-mechanism discriminator, not a mechanism proof — even a
   clean, null-controlled CONFIRM licenses only "a specific, falsifiable
   geometric candidate survives a zero-cost check with real statistical
   power," not a proven physical mechanism (see mandatory caveat, above).
   PLAN.md's own queue item 2 (EM's C60/C70 test, or PHOTONICS' 750/450nm
   re-run) is the correct next FDTD-cost step to test causation.
8. Distinct from R2 (LOGBOOK RULED OUT) — R2 concerned an
   integer-multiple-of-λ resonance condition on shell thickness; this
   batch's candidates are ordinary geometric diffraction-aperture
   arithmetic (a length-scale ratio), a different claim class.
9. `T_SINTHETA_600=cpl/A` is T21's own fitted stationary-phase *model*
   under test (R²=0.7852→0.8271 at its own best fit), not
   independently-verified ground truth (unchanged from exp-069's own
   Idealization 5).
10. **THERMODYNAMICS' WKB/adiabatic boundary-reflectance fold-in is not
    picked up this cycle** — disclosed scope choice, not silence (docket
    item 6, above).

## Predictions — committed to git BEFORE the run (house discipline)

| ID | Claim | CONFIRM | REFUTE | else |
|---|---|---|---|---|
| **P-070-1** | Item (a). Free-fit period recovered independently from `C_empty_C40(θ)` and `C_empty_C80(θ)` (grid `[1°,4°]`, center 39°) is close to `P*_delta` (config-invariant hypothesis) — scored on the RECOVERED PERIOD, not bare R² (docket fix 1). | recovered-period deviation from `P*_delta` ≤ 20% for **both** C40 **and** C80 | **either** config's free-fit `R²<0.15` **or** its recovered-period deviation ≥ 50% | NEITHER, disclosed |
| **P-070-2** | Item (b). Beat-frequency reconstruction (`P_beat≡P*_delta` vs. T21's `P(39°,600nm)`) yields an `A_alt` branch matching a NAMED combination, **null-controlled**. | best match ≤1% relative **AND** null-permutation `p≤0.05` (`N=20,000`, `T~Uniform(100,1600)`) | best match ≥10% relative on **both** branches | NEITHER, disclosed |
| **P-070-3** | Item (c). `TAPER=40` cells alone predicts `P_taper(39°,600nm)` near `P*_delta`. | `\|P_taper−P*_delta\|/P*_delta ≤ 20%` | `≥ 100%` | NEITHER, disclosed |
| **P-070-4** | Item (d). `A_eff` (back-solved from `P*_delta`) matches a NAMED combination, **null-controlled**, and that candidate's implied period fits the held-out 750nm leg. | best match ≤1% **AND** `p≤0.05` **AND** `R²(750nm)≥0.70` | best match ≥10%, **OR** `R²(750nm)<0.40` | NEITHER, disclosed |
| **P-070-5** | Item (e). The tie-sets from (b)'s branches and (d) share ANY common NAMED expression (docket fix 3 — no single arbitrary "best pick"). | any shared expression | no shared expression | — (binary by construction) |

**No Combined Verdict gate** (unchanged from Phase 1 — these five items are
diagnostic and largely independent; each is reported individually).
**Per docket item 10: PLAN.md queue item 2 is narrowed ONLY by items that
clear the corrected gate above — a NEITHER never narrows it**, regardless
of how close its raw (non-null-controlled) numbers sit to a threshold.

## Gates

Zero new `lab/` diff; no trust-suite stage added or touched. Full bench
(41/41 fast-subset checks) reconfirmed green at shift start (SESSION_LOG.md).
No FDTD calls this cycle — no `box_dev`/`cross_dev` gate applies; this
batch refits already-gated `results.json` data, it does not re-derive it.

---

## Result

*(filled in Phase 4 — see `phase4_results.md`)*

## Learned

*(filled in Phase 4)*

## Next

*(filled in Phase 4/5)*
