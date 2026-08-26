# exp-076 — T28 G40/`PAD` Decorrelation

**Panel Iteration 53.** Lead: QUANTUM OPTICS (by rotation). Director
synthesis post Phase 2 (five blind critiques + Red Team's Phase-2 audit,
verdict **PROCEED-WITH-MANDATORY-FIXES, 8-item docket, ALL 8 items ADOPTED,
ZERO overridden** — full record in `phase1_proposal.md`,
`phase2_critique_{em,materials,photonics,thermodynamics,vision}.md`,
`phase2_redteam_audit.md`, `phase3_synthesis.md`).

## Mandate

PLAN.md's Iteration-53 queue item 1 (near-unanimous #1 across exp-075's six
Phase-5 seats): decorrelate T28's amplitude-mismatch signal from the
`ABSORB`/`PAD` compound-axis confound that has run through every congruent
`{C40,C60,C70,C80}` `ABSORB`-depth reading since Iteration 48 (`PAD =
ABSORB − 40` exactly, by construction, at all four configs). Build and score
a fifth FDTD configuration, `G40` (`ABSORB=40, PAD=40`), already specified in
`experiments/065-.../design_geometry.py` but never run at T28's own dense
(31-angle, settled-`STEPS`) window — its two new differences, `C80−G40`
(pure-`ABSORB` at fixed `PAD`) and `G40−C40` (pure-`PAD` at fixed `ABSORB`),
isolate the two axes the congruent series entangles. Full mechanism/
instrument narrative: `phase1_proposal.md` §1.

## Setup

Reuses committed machinery programmatically throughout (R4 discipline — see
`run.py`'s own module docstring for the exact reuse chain):

- **Geometry**: `experiments/065-.../design_geometry.py::CONFIGS` (G40 is
  bit-identical to C80 in every scene coordinate — `NX,NY,SRC_X,PLANE_X,
  OBJ_Y,y_lo,y_hi,A=752,aperture=1504,D_SP=223` — differing from C80 *only*
  in `absorb` (40 vs 80) and the clearances mechanically derived from it;
  shares C40's `absorb` exactly). Reached via `exp069_run.dg` (exp-069's own
  `design_geometry.py` re-exports `dg065.CONFIGS` verbatim) to avoid a
  `sys.modules["design_geometry"]` name collision — see `run.py`'s
  `_load_module()` docstring.
- **FDTD call construction**: `experiments/069-.../run.py`'s `_one_run`/
  `_profile`/`_c_empty` (same `profile="plane"`, `edge=TAPER=40`, `STEPS`
  convention), reused **verbatim**, not re-implemented.
- **Scoring**: `experiments/076-.../g0e_amplitude_channel_check.py`'s own
  already-verified `_amp_ratio_recover` (which itself reuses exp-072's
  `carrier_fit`/`design_matrix`/`_amp_phase_at` verbatim) for every
  `amp_ratio` figure, and `experiments/072-.../run.py::analyze_pair`
  verbatim for the two new pairs' `delta_P_obs` (needed only for the
  disclosed-only `rho_pad_absorb` diagnostic).

Headline statistic (identical formula already applied to the confounded
series, exp-072's own instrument): `amp_ratio = √(A_i²+A_q²)/amp`, the
envelope-amplitude mismatch between two series at a common-mode carrier,
normalized by that carrier's own fitted amplitude. Applied to:

- **`PAIR_PAD ≡ (C40, G40)`**, `x = amp_ratio(PAIR_PAD)` — isolates `PAD`
  alone.
- **`PAIR_ABSORB40 ≡ (G40, C80)`**, `y = amp_ratio(PAIR_ABSORB40)` —
  isolates `ABSORB` alone.

Directly comparable to the existing baseline `amp_ratio(C40,C60)=0.161`,
`amp_ratio(C60,C70)=0.041`, `amp_ratio(C70,C80)=0.020`,
`amp_ratio(C40,C80)=0.166` — reproduced fresh, not hand-typed, by
`run.py::baseline_reproduction_check()` (see FROZEN PREDICTIONS below).

## The fixed design (Red Team's 8-item docket, `phase2_redteam_audit.md`,
all ADOPTED — full disposition table in `phase3_synthesis.md`)

Summary of what changed from the raw Phase-1 proposal:

1. **§4's outcome bands rewritten**: the old `(a)/(b)/(c1)/(c2)` scheme
   (neither mutually exclusive nor exhaustive — Red Team Attack 1) is
   replaced by an exhaustive, mutually-exclusive **9-cell / 5-outcome**
   scheme (`ABSORB-TIED`, `ABSORB-LEANING`, `PAD-TIED`, `BOTH-LOW/NULL`,
   `BOTH-HIGH/POSSIBLE SUPER-ADDITIVE`). Full 3×3 table, verified by direct
   enumeration: `phase3_synthesis.md` §3.
2. **`rho_pad_absorb` downgraded** to a disclosed, uncalibrated, non-gating
   diagnostic — its "real evidence... interaction exists" language
   contradicted `experiments/072-.../run.py`'s own documented disposition
   of the identical `rho_c` construction, which was never evaluated on real
   data in this program's history (Red Team Attack 2).
3. **`R_q`'s role scoped precisely**: not used in the gating `amp_ratio`
   statistic; used, via `delta_P_obs`, in the disclosed-only
   `rho_pad_absorb` diagnostic, no null-calibration attached (Red Team
   Attack 3).
4. **A 3-call settling precondition added, run and checked FIRST** — G40 at
   θ∈{39°,40°}, 600nm, `STEPS=4200` vs the same points at `STEPS=2800`
   (EM's forward-settling fix, HALT-if-fails), plus G40 at θ=39°, 600nm,
   `STEPS=1400` (VISION's backward differential, disclosed only). G40's own
   geometry (C40's thin, leakier `ABSORB=40` boundary sitting at C80's
   larger domain) had never been settling-tested at any `STEPS≥2800` before
   this cycle — every prior settling check co-varied boundary thickness and
   domain size.
5. **A 16-call G40-at-750nm advisory leg added**, replacing PHOTONICS'
   original 6-call sparse-angle proposal (too sparse for `amp_ratio`'s own
   carrier-fit machinery — Red Team Attack 4). Reuses
   `experiments/069-.../results.json::block_leg750`'s already-committed,
   non-aliased window (θ∈[38°,41°], `STEPS=2800`) for C40/C80 at zero
   marginal cost. Every config this cycle otherwise runs sits at an exact
   integer multiple of λ at 600nm (2λ/4λ) — the resonant/aliased condition
   `C70` was added, in this identical sub-thread's own precedent cycle, to
   guard against.
6. **Threshold gloss corrected**: 0.050 is 30% of the combined baseline
   `amp_ratio(C40,C80)=0.166`, **well ABOVE** the smallest already-
   established adjacent-pair reading (`C70-C80=0.020`) — not "at or below"
   it, the original proposal's backwards phrasing (Red Team Attack 5).
7. **MATERIALS' caveat added verbatim**, attached to every outcome using
   ABSORB-tied/PAD-tied language: `ABSORB` and `PAD` are both pure
   numerical domain-construction parameters; neither carries more physical
   standing than the other.
8. **THERMODYNAMICS' energy-sidecar N/A sentence restored** (see
   Idealizations below) — silently dropped from the raw Phase-1 proposal,
   breaking an unbroken convention every T28 instrument cycle has stated
   since exp-071.

## Idealizations

1. **600nm primary, 750nm advisory only.** The 16-point 750nm leg (docket
   item 5) is explicitly labeled advisory/narrow-window (3° vs the 600nm
   window's 6°) — NOT decisive, and does not license any wavelength-general
   citation of this cycle's headline verdict. A future full-width
   (6°/31-point) non-aliased leg is required before any such citation.
2. **The 2×2 (`ABSORB`×`PAD`) factorial is not completable.**
   `config(ABSORB=80, PAD=0)` gives `clear_span_y=−40` (geometrically
   invalid — `clear_plane`/`clear_src` go negative too). Main effects
   (pure-`ABSORB`-at-fixed-`PAD`, pure-`PAD`-at-fixed-`ABSORB`) are
   identifiable from `{C40,C80,G40}` only under an additivity assumption;
   the interaction term at the missing 4th corner is not identifiable at
   all by this design. `rho_pad_absorb` can detect that additivity fails in
   aggregate; it cannot say by how much, in which direction, or attribute
   the failure to a specific interaction value — and, per docket item 2, it
   cannot even certify that a large value IS an interaction failure rather
   than a carrier-fit artifact.
3. **Different pairs use independently-fit carriers.** `PAIR_PAD` and
   `PAIR_ABSORB40` each get their own `(T_x, psi)` from a free-period search
   on their own `Cbar` (needed for direct comparability to the
   0.161/0.041/0.020/0.166 baseline, which uses this same convention) —
   `amp_ratio` values are magnitudes in different local bases, not
   components of one shared vector; `amp_ratio(PAIR_PAD) +
   amp_ratio(PAIR_ABSORB40)` is not expected to equal `amp_ratio(C40,C80)`
   even under perfect physical additivity.
4. **`G40` has never been run at settled `STEPS=2800` or at T28's dense
   window before this cycle.** exp-065's own `Block PAD` `G40` legs (3
   angles × 3 wavelengths, `STEPS=1400`) are a distinct, unsettled-STEPS,
   sparse-angle reading of the same config, reused ONLY for the disclosed
   backward-differential bonus at θ=40° (docket item 4b), not as scored
   `amp_ratio` input.
5. **`amp_ratio`'s carrier is fitted from data, not parameter-free** — R6/
   `G0-e` is directly engaged (not deferred): `g0e_amplitude_channel_check.py`
   (Phase 1, already run) gives Case 1 worst `|recovered/true−1|=1.03×10⁻⁴`
   (PASS, ≤2%) and Case 2 worst `=8.35×10⁻³` (PASS, ≤5%, relaxed only for
   the disclosed first-order-in-`u` term present exclusively in the mixed
   case). `G0-e OVERALL: PASS`. Re-confirmed unchanged (not merely cited
   forward) before any real-data `amp_ratio` is reported.
6. **cpl=20 (native resolution) only.** No R3 resolution check on the new
   `G40` legs this cycle — a natural Iteration-54+ follow-up if either new
   `amp_ratio` reading comes back large enough to be load-bearing.
7. **`amp_ratio` and `delta_P_obs` are fixed-formula readouts, not
   significance tests.** No p-value, null-calibration, or `RESOLVED`-class
   claim is made this cycle on either new pair — the 9-cell/5-outcome
   scheme is a magnitude-comparison scheme only, deliberately outside the
   formally-retired differential/two-tone significance-testing instrument
   class (exp-074's seventh-cycle rule) — `amp_ratio` reads off `A_i`/`A_q`
   (not `R_i`/`R_q`) and attaches no null-calibration, so it is genuinely
   null-free and `R_q`-free.
8. **`ABSORB`/`PAD` are not materials** (MATERIALS' caveat, docket item 7):
   both pure numerical FDTD boundary-condition parameters; neither reading
   in this cycle is a realizability or material claim, and "`ABSORB`-tied"
   carries no more physical standing than "`PAD`-tied."
9. **Energy sidecar: N/A this cycle** (THERMODYNAMICS' disposition, docket
   item 8) — `ABSORB`/`PAD` are numerical damping-mask constructs with no
   loss tangent or physical dissipative volume; no absorbed-power/thermal
   disposition is produced or applicable, consistent with every T28
   instrument cycle since exp-071.
10. 2D TMz, single polarization, positive-θ branch only (36°–42°/38°–41°),
    bench scale (`R_OUT=78` cells), no witness-scale claim.

## FROZEN PREDICTIONS (committed here, before `run.py`'s first execution)

**These are the pre-registered, falsifiable outcome bands — no threshold
below is adjusted after any real `G40` FDTD call runs.**

**Bin edges** (re-derived programmatically from the real committed baseline
at implementation time, never hand-typed — R4; `run.py::
baseline_reproduction_check()` reproduces `amp_ratio(C40,C80)` two
independent ways — a fresh re-fit from raw committed data, and a read of
exp-072's committed OLS coefficients — and asserts they agree to ~1e-15
relative before deriving anything from it):

```
THRESH_LOW  = 0.3 x amp_ratio(C40,C80) ≈ 0.049762   (0.050 is 30% of the
THRESH_HIGH = 0.7 x amp_ratio(C40,C80) ≈ 0.116111    combined baseline
                                                       0.166, well ABOVE
                                                       C70-C80=0.020)
LOW = [0, THRESH_LOW)   MED = [THRESH_LOW, THRESH_HIGH)   HIGH = [THRESH_HIGH, inf)
```

**9-cell / 5-outcome mapping** (`x = amp_ratio(PAIR_PAD)`,
`y = amp_ratio(PAIR_ABSORB40)`; verified exhaustive and mutually exclusive
by direct enumeration, `run.py::verify_outcome_table_exhaustive_and_exclusive()`):

| x \\ y | LOW | MED | HIGH |
|---|---|---|---|
| **LOW**  | BOTH-LOW / NULL | ABSORB-LEANING | **ABSORB-TIED** |
| **MED**  | PAD-TIED | ABSORB-LEANING *(x<y)* / PAD-TIED *(x≥y)* | ABSORB-LEANING |
| **HIGH** | PAD-TIED | PAD-TIED | **BOTH-HIGH / POSSIBLE SUPER-ADDITIVE** |

Full outcome interpretations and MATERIALS' caveat: `phase3_synthesis.md`
§3.

**Settling precondition (docket item 4, MANDATORY, HALT-if-fails, checked
BEFORE the remaining 29-point dense sweep or any real `amp_ratio` is
scored)**: `|C_G40(4200,θ) − C_G40(2800,θ)| / amp_ref < THRESH_LOW` at BOTH
θ∈{39°,40°}, where `amp_ref` is the C40-C80 baseline's own fitted carrier
amplitude (the same normalization `amp_ratio`'s numerator uses). If this
fails: HALT, write a partial `results.json` flagged for Director review,
do not run the remaining 45 calls. Bar cited exactly:
`THRESH_LOW` itself — the smallest live §4 band edge — per the Director's
own instruction; full rationale in `run.py::settling_gate_check()`'s
docstring.

**`rho_pad_absorb`** (disclosed-only, never gating, docket items 2/3):
`|delta_P_obs(PAIR_PAD) + delta_P_obs(PAIR_ABSORB40) − delta_P_obs(C40,C80)|
/ max(|delta_P_obs(C40,C80)|, 0.005)`, `delta_P_obs(C40,C80)=0.06684°`
loaded from `experiments/072-.../results.json`, not re-fit. No verdict of
any kind is attached to any value of this quantity.

**750nm leg** (docket item 5, advisory only): raw `amp_ratio(PAIR_PAD)`/
`amp_ratio(PAIR_ABSORB40)` at the `block_leg750` window, plus a qualitative
same-direction/opposite-direction comparison against the 600nm headline
ordering (`x≤y` vs `x>y`) only — the 9-cell band machinery is NOT applied
at 750nm.

**FDTD budget**: 50 new calls total (2 settle-forward @4200 + 1
settle-backward @1400 + 31 dense @600nm/2800 [including the 2 settle-reused
points] + 16 leg750 @750nm/2800), ~15–17 min wall-clock by the established
linear-scaling method.

**None of this is a RESOLVED/CONFIRMED-class significance claim on `R_q` or
any carrier/phase-conditioned coefficient.** `amp_ratio` is null-free and
`R_q`-free (`phase1_proposal.md` §7); `rho_pad_absorb` carries no
null-calibration and is explicitly non-gating.

**Checkpoint status**: per Red Team's own explicit ruling
(`phase2_redteam_audit.md`'s Checkpoint-status section, quoted in full in
`phase3_synthesis.md` §6), Checkpoint criterion 4 does NOT fire on this
cycle — the docket above lands before this §4 language freezes.

## Result

See `phase4_results.md` (not yet written — Phase 4 execution pending
Director authorization; this cycle's FROZEN PREDICTIONS above were
committed before `run.py`'s first execution, per house discipline).

## Learned

See `phase4_results.md` Bottom Line and this experiment's contribution to
LOGBOOK.md Iteration 53 (not yet written).

## Next

See PLAN.md's Iteration-54 queue (Director's update, post Phase 5, not yet
written).
