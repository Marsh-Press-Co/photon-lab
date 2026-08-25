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

Zero FDTD calls, pure desk arithmetic. **P-070-1 CONFIRM** — both `C40`
and `C80`'s own free-fit periods (2.4361°, 2.5338°) sit within 20% of
`P*_delta=2.8421°` (14.29%, 10.85% deviation), and neither config's R² is
disqualifying (0.4327, 0.4337) — the ~2.8°-family signature genuinely
lives in each config **individually**, not only in their difference.
**P-070-2 NEITHER** — both beat-frequency branches find a sub-1% named-
constant match (`A_alt=233.19`→`233` at 0.081%; `A_alt=1270.81`→`1271` at
0.015%), but neither clears the null-permutation gate (`p=0.806`, `p=0.204`
— worse than or comparable to a majority of random targets in the same
search space). **P-070-3 REFUTE** — `P_taper(39°,600nm)=36.86°`, 1197% off
`P*_delta`, an order-of-magnitude clean rejection. **P-070-4 NEITHER** —
`A_eff=518.81` matches `519` (six-way tie) at 0.036%, and the candidate's
750nm cross-validation R²=0.7663 clears the 0.70 bar, **but** `null_p
=0.497` — statistically indistinguishable from a coin flip, decisively
failing the null-controlled gate despite passing every raw-threshold
component. **P-070-5 REFUTE** — no NAMED expression is shared between
either (b) branch's tie-set and (d)'s tie-set. Full detail:
`phase4_results.md`.

## Learned

1. **T28's ~2.84°-family signal is config-invariant (P-070-1), which
   disfavors an `ABSORB`-depth-tied mechanism relative to a geometry-
   invariant one.** `A=752` is bit-identical across `C40`/`C80` by
   construction (exp-069); this cycle adds that the recovered periods
   inside `C40(θ)` and `C80(θ)` alone (2.44°/2.53°) both independently
   land close to the padding-delta's own free-fit period, something an
   `ABSORB`-depth-specific mechanism (the one thing that differs between
   configs) offers no obvious reason to produce. This does not identify a
   mechanism — it narrows the *class* of viable ones toward something
   present in both configs' shared geometry (candidates: `R_OUT`/`W_OBJ`,
   degenerate at 78 cells here, per Idealization 4).
2. **The named-constant search (items b/d/e) has essentially zero power
   to discriminate a real geometric mechanism from chance, exactly as
   Red Team's Phase-2 audit predicted and the mandatory null control now
   demonstrates on the actual gated run, not a scratch check.** Every raw
   "match" this batch found (0.015–0.081% deviation) looked, before the
   null control, like strong evidence; after it, every one lands at or
   above the 20th percentile of a 20,000-trial random-target null — not
   even close to the `p≤0.05` bar. This is the single clearest
   demonstration in this program's own history that PHOTONICS'/MATERIALS'
   general worry (a dense small-integer search over many named constants
   finds *something* regardless of ground truth) was not theoretical.
3. **Taper-as-second-aperture (item c) is cleanly, decisively dead** — an
   order of magnitude off, zero ambiguity, the one item this batch
   resolves with no caveats attached.
4. A mandatory-fix docket built entirely from Phase-2 critique + Red Team
   ruling — with the Director adding zero new judgment calls at Phase 3 —
   changed three of five headline verdicts from what a naive read of the
   Phase-1 proposal's own disclosed recon numbers would have suggested
   (P-070-2 and P-070-4 both looked pre-confirmed at Phase 1; both are
   NEITHER once null-controlled). This is the process working as
   intended, not a failure of Phase 1 — VISION's own Phase-2 HARKing flag
   and Red Team's own executed proof are exactly what caught it before
   either number reached PLAN.md as a load-bearing claim.

## Next

- **T28's own forward tripwire (Red Team, exp-069 Phase-5 final audit) is
  discharged**: this cycle is the cheap, desk-only first move required by
  Iteration 48's close, delivered at Iteration 47.
- **PLAN.md queue item 2 (EM's C60/C70 falsification test, or PHOTONICS'
  properly-powered 750/450nm re-run) should be narrowed by P-070-1's
  CONFIRM, not by P-070-2/4's raw (pre-null) numbers**, per docket item
  10: EM's own C60/C70 test — which actually varies `ABSORB` while holding
  everything else fixed — is now the more direct next step, since P-070-1
  positively disfavors the `ABSORB`-tied hypothesis it was designed to
  test, while items (b)/(d)/(e) contribute no surviving candidate length
  scale to narrow a re-run's own target period toward.
- **This batch does NOT identify a mechanism** for T28 — it establishes
  that the signal is config-invariant (a real, if partial, narrowing) and
  that this program's own dense small-integer named-constant search
  methodology needs a null-permutation control by default going forward
  whenever a future cycle proposes a similar search (a general process
  lesson, not scoped to T28 alone — candidate for a standing house-rule
  note, Red Team's/Phase-5's call).
