# exp-071 — ELECTROMAGNETISM's C60/C70 `ABSORB`-Depth Causal Falsification Test for T28

**Panel Iteration 48.** Lead: VISION SCIENCE (by rotation). Director
synthesis post Phase 2 (five blind critiques + Red Team's Phase-2 audit,
verdict PROCEED-WITH-MANDATORY-FIXES, 7-item docket, **zero overridden** —
full record in `phase1_proposal.md`, `phase2_critique_{photonics,materials,
em,thermodynamics,quantum}.md`, `phase2_redteam_audit.md`,
`phase3_synthesis.md`).

## Mandate

PLAN.md's Iteration-48 queue, item 1, ranked #1 by a genuine 6-for-6
blind-seat convergence at exp-070's Phase-5 final audit:

> **ELECTROMAGNETISM's C60/C70 `ABSORB`-depth falsification test** — the
> already-built congruent configs (zero new `lab/` diff), varying `ABSORB`
> directly across all four points (40/60/70/80) while holding everything
> else fixed, the causal manipulation T28's own desk-check batch
> (exp-070) could not provide.

## Setup

Reuses exp-065's congruent construction (`CONFIGS["C40"/"C60"/"C70"/"C80"]`,
`A=752` cells held fixed across all four `ABSORB` depths) and exp-069's
dense-sweep/free-period-search machinery **verbatim — zero new `lab/`
diff**. `C40(θ)`/`C80(θ)` over the 31-point Block DENSE window (36.0°–
42.0°, 0.2° step, 600nm, STEPS=2800) are reused from exp-069's own
committed `results.json` (0 new calls); `C60(θ)`/`C70(θ)` are newly run at
the identical window (THE causal manipulation — Block DENSE-CAUSAL).

| Block | Angles | λ | STEPS | Configs | Calls |
|---|---|---|---|---|---|
| **G1** (identity gate) | {39°, 40°} | 600nm | 2800 | C40, C80 | 4 |
| **DENSE-CAUSAL** (new) | 36.0°–42.0°, 0.2° step (31 pts) | 600nm | 2800 | C60, C70 | 62 |
| **R3-PEAK** (new, all 4 depths) | {37.2°, 41.4°} (peak cells, verified against exp-069's committed data — NOT the original zero-crossing R3 cells) | 600nm, cpl=**30** | 4200 | C40_R3, C60_R3, C70_R3, C80_R3 | 8 |
| **SETTLE-C60C70** (new, mandatory fix 1) | {37.2°, 41.4°} | 600nm | 4200 vs 2800 | C60, C70 | 4 |
| **Total** | | | | | **78** |

Cost basis: `design_geometry.py::fdtd_budget()` (code-produced — R4).
Predicted: **78 calls, 6266.6 CPU-s, wall ≈30.64 min, 3× envelope ≈91.92
min. Hard stop: 100 min** (restated from the Phase-1 proposal's 90 min per
mandatory fix 8, preserving this program's "a few minutes past the 3×
envelope" convention under the revised budget). De-scope order if
breached: retract Block R3-PEAK to the literal C40/C80-only minimum first
(74 calls, 26.41 min), then to a single peak angle; **Block G1, Block
DENSE-CAUSAL, Block SETTLE-C60C70, and the resolution-floor computation
are NEVER de-scoped** (mandatory fix 7).

## T1 escape route

**N/A — instrument/mechanism-identification class**, identical in kind to
exp-041/065/066/068/069/070. No mechanism is proposed as satisfying the
phenomenon's four constraints; constraint 3 is not engaged.
**Checkpoint-criterion-2 candidacy: none.**

## Idealizations

1. 2D TMz, single polarization.
2. **600nm only** — no 750nm leg this cycle (PHOTONICS' Phase-2 finding:
   this means a CONFIRM below is scoped to 600nm and cannot by itself
   distinguish a λ-scaled physical coupling from a cell-count/
   discretization artifact — see the wavelength-scope caveat below; a
   confirmatory 750nm leg is queued as a fast-follow, Iteration 49, not
   run this cycle per Red Team's scope ruling).
3. Positive θ branch only (36°–42°), matching Block DENSE's own window.
4. All four congruent `ABSORB` depths engaged; `G40`/`N60` (pad-only/naive
   controls) are T24's own separate question, not re-run here.
4b. **ADDED (Red Team's Phase-5 final audit, mandatory fix 6, independently
   confirmed by three blind Phase-5 seats — THERMODYNAMICS, ELECTROMAGNETISM,
   QUANTUM OPTICS): `PAD = ABSORB − 40` exactly at all four congruent
   configs.** Every absolute position shifts in lockstep with `ABSORB`;
   only relative quantities (`A=752`, clearances) are held fixed. This
   ONE axis is a compound `ABSORB`/`PAD` axis, not a pure `ABSORB` axis —
   a hypothetical CONFIRM on this series describes an ABSORB-*or*-PAD-tied
   effect, not specifically ABSORB-tied (a hypothetical REFUTE is not
   equally compromised — it validly rules out both together). Does not
   affect this cycle's own NEITHER verdict, but is a standing forward
   constraint on any future causal use of this exact congruent series,
   unflagged across three prior cycles (46/47) that reused it. See
   `phase4_results.md`'s own "Standing forward constraint" section.
5. The free-period grid search fits a fixed sinusoidal form in `sin θ`; a
   4-point linear `P*(ABSORB)` trend has only 2 residual degrees of
   freedom — mitigated, not eliminated, by the resolution-floor gating
   below (mandatory fix 2) and the independent P-071-3 pairwise table.
6. Bench scale only (`r_out=78` cells) — no witness-scale claim.
7. `A=752` held fixed at native cpl for all four configs (already passed);
   R3's own `A_r3=1128` is the same physical aperture, checked in code.
8. Single-angle `C_empty` readings, not an N9/N17 aggregate.
9. `C70`'s `CPU_S_PER_CALL` is a linear interpolation (exp-065's own
   disclosure), used only for budgeting, never for a physics comparison.
10. **Block SETTLE-C60C70's peak angles (37.2°/41.4°) are off exp-065's
    coarse STEPS=1400 angle grid** — there is no 1400-STEPS comparator at
    these exact cells, so this new settling check is scored on the
    ABSOLUTE 2800-vs-4200 shift relative to `GATE_HARD` (the instrument
    floor), not a 1400-anchored relative percentage. Disclosed explicitly,
    not silently substituted (see `run.py::score_settle_c60c70`).
11. R_contact (PLAN.md queue item 2) remains untouched this cycle's
    mandate — see the tooling disclosure in `phase3_synthesis.md`.

## Three caveats, disclosed unconditionally regardless of outcome (mandatory fixes 3, 4, 5)

- **`ABSORB` is not a material.** It is `lab/fdtd2d.py::Sim._damping`'s own
  numerical domain-truncation boundary depth (a cubic-ramp PML-analog,
  `exp(-0.30·d)`, applied to all four box edges) — not a material or
  physical-optics parameter, real or hypothetical. Any CONFIRM below
  describes a numerical-boundary-construction effect, never a physical
  absorbing mechanism (reinstating exp-070's own mandatory fix 5, dropped
  in the Phase-1 draft and caught independently by MATERIALS and
  THERMODYNAMICS this cycle).
- **The THERMO energy-sidecar metric row does not apply this cycle.** No
  absorbing article is run (Block ARTICLE not re-run), and all four
  congruent configs are near-total absorbers at their own boundary by
  construction regardless of `ABSORB` depth — there is no absorbed-energy
  trend to characterize and no witness-scene material to re-radiate from.
- **600nm-only scope caveat** — see idealization 2.

## Predictions — committed to git BEFORE the run (house discipline, non-negotiable)

Reproduced verbatim from `run.py`'s `FROZEN_PREDICTIONS` string (this
program's own established discipline: the committed prose and the executed
code cannot drift apart).

| ID | Claim | CONFIRM | REFUTE |
|---|---|---|---|
| **P-071-G1** (absolute identity gate) | θ∈{39°,40°}×{C40,C80}×600nm×STEPS=2800 reproduce exp-069's committed `block_dense` rows exactly (4 values, loaded programmatically). | `ΔC=0.0` for all 4 | any nonzero Δ — **halts the cycle** |
| **Block SETTLE-C60C70** (mandatory fix 1, EM — binding precondition) | `\|ΔC(4200−2800)\|` at θ∈{37.2°,41.4°}, 600nm, C60/C70, relative to `GATE_HARD` (idealization 10). | ≤1× `GATE_HARD` at all 4 cells | ≥5× `GATE_HARD` at any cell |
| **P-071-1** (descriptive) | Free-period grid search (imported by reference from exp-069/070, defaults asserted `[1,4]°`/`n_grid=400`/`center=39°`) applied to `C40(θ)`, `C60(θ)`, `C70(θ)`, `C80(θ)` individually over the 31-pt window. `C40`/`C80` reused from exp-069's committed data; `C60`/`C70` newly computed. | — | — |
| **P-071-2 (HEADLINE, causal trend, resolution-floor-gated)** | Linear regression `P*(ABSORB) = m·ABSORB + c` over the four points. | **CONFIRM** (ABSORB-depth-tied **numerical-boundary-construction effect**, not a material mechanism — see caveats): `\|P*(80)−P*(40)\|/mean(P*) ≥30%` AND `R²≥0.50` AND the 40-vs-80 comparison's own Rayleigh resolution ratio `≥1.0` | **REFUTE** (shared-geometry, NOT ABSORB-tied): max pairwise spread `≤15%` AND `R²≤0.30` AND **every** pairwise comparison used has resolution ratio `≥1.0` |
| **P-071-3** (required disclosure) | Pairwise `\|P*(Ca)−P*(Cb)\|/mean` at all 6 pairs, each annotated with its own Rayleigh resolution ratio and RESOLVED/UNRESOLVED flag (mandatory fix 2). | — | reported in full regardless of outcome |
| **P-071-4** (co-gating, peak-cell R3 — binding precondition) | Does `delta(θ)=C80(θ)−C40(θ)` survive cpl 20→30 at θ∈{37.2°,41.4°} (the peak cells, not the original zero-crossing cells)? | same sign at both **AND** ratio `∈[0.3,3.0]` at both | sign flip at either, **OR** ratio outside `[0.1,10]` at either |
| **P-071-5** (disclosed, non-gating) | Same peak-cell R3 check on `delta(θ)=C70(θ)−C60(θ)`. | — | context only |

**Combined Verdict — computed in code, not prose (`run.py::main`):**

- **HALT** ⟺ P-071-G1 fails.
- **CONFIRMED** (`CONFIRMED_ABSORB_TIED_NUMERICAL_BOUNDARY_EFFECT`) ⟺ G1
  PASSED **AND** Block SETTLE-C60C70 CONFIRM **AND** P-071-4 CONFIRM
  **AND** P-071-2 CONFIRM (resolution-floor-gated).
- **REFUTED** (`REFUTED_SHARED_GEOMETRY_NOT_ABSORB_TIED`) ⟺ G1 PASSED
  **AND** Block SETTLE-C60C70 CONFIRM **AND** P-071-4 CONFIRM **AND**
  P-071-2 REFUTE (resolution-floor-gated).
- **NEITHER** ⟺ G1 PASSED **AND** anything else — an explicit, computed
  branch (any precondition failure, or a resolution-floor failure on the
  trend test itself), reported with the full P-071-1/P-071-3 tables
  attached, **never a silent PARTIAL escape hatch**.

## Gates

Full bench (`lab/validation/run_all.py --only 12346789`) reconfirmed
green this shift: 41/41 checks (heavy stage 5 optional, house convention).
Zero `lab/` diff throughout. `assert_lab_clean()` re-verifies at the start
of every run. P-071-G1 is the one local absolute-identity gate.

---

## Result

78 FDTD calls, 925.7s (15.43 min), zero `lab/` diff. **P-071-G1 PASSED**
(4/4 exact). **Both binding preconditions CONFIRM**: Block SETTLE-C60C70
(2800-vs-4200 shift 2–4 orders of magnitude below `GATE_HARD` at all 4
cells — C60/C70 genuinely settled) and P-071-4 (peak-cell R3, `C80−C40`
survives cpl 20→30 at both peaks, ratios 1.234/1.047). Per-config free
periods rise smoothly and monotonically with `ABSORB`: C40=2.4361°→
C60=2.5188°→C70=2.5338°→C80=2.5338° (linear fit R²=0.8664), but the total
spread is only 3.90% — far below the 30% CONFIRM threshold, while R²=0.87
sits far above REFUTE's own R²≤0.30 ceiling, so the raw statistic clears
neither band. **The Rayleigh resolution-floor gate (mandatory fix 2)
resolves the ambiguity**: the window supplies only 9.5% of the frequency
resolution needed to distinguish P*(40) from P*(80) — `trend_resolved=
False`, and 5 of 6 pairwise comparisons are independently `UNRESOLVED`
(the 6th is an exact C70/C80 grid-search tie, likely a discretization
artifact of the 400-point search grid, not independent confirmation).
**Combined Verdict: NEITHER** — an explicit, computed branch, not a silent
PARTIAL escape hatch. Full detail: `phase4_results.md`.

## Learned

1. **The mandatory-fix docket did its job — and Phase 5 caught a real
   overclaim about exactly how.** ERRATUM (Red Team's Phase-5 final audit,
   independently confirmed by VISION SCIENCE and QUANTUM OPTICS' blind
   Phase-5 reviews): the sentence originally here — "without the
   resolution-floor gate, this cycle would likely have reported a spurious
   REFUTE" — is a checkable, false counterfactual. `results.json["trend"]`
   shows `raw_refute=False` on the pre-registered `R²≤0.30` ceiling ALONE
   (`R²=0.8664`), with no resolution floor involved at all; re-scoring the
   identical data against the unmodified REFUTE band, with the
   resolution-floor gate removed entirely, still yields NEITHER. Corrected
   account: both of Red Team's Phase-2 load-bearing concerns (EM's
   settling-closure gap, QUANTUM's/Red Team's resolution-floor risk) were
   real, testable claims, and both came back informative — settling was
   genuinely fine (closing EM's gap), and the resolution floor is real,
   correctly computed, and prospectively load-bearing for any future run
   whose raw statistic lands closer to either band — but for *this* run,
   the raw CONFIRM/REFUTE bands already missed independently, on their own
   pre-registered thresholds, before the resolution floor even entered the
   decision. The mandatory-fix docket still did its job: it built a gate
   that would have caught a false CONFIRM/REFUTE had one nearly fired, and
   it happened not to be the deciding factor this particular run — that is
   a more precise, and more honest, statement than the original claim.
2. **T28's causal question remains genuinely open**, narrowed rather than
   answered: the per-config periods DO rise smoothly with `ABSORB` depth
   (a real, well-fit shape), but the magnitude (3.9% over a 2× `ABSORB`
   range) is too small for this window to distinguish from four noisy
   estimates of one shared, non-ABSORB-tied period. This is a genuine
   instrument-power limit, not a hedge: the fix is a wider angular window
   (more T21 periods) or a discriminator that does not depend on
   frequency-resolving the difference between four close periods.
3. The exact C70/C80 free-period tie (2.5338° to all printed digits) is a
   useful, disclosed caveat for any future reuse of this per-config
   free-period table: with `n_grid=400` over `[1°,4°]` (step 0.0075°), an
   exact match this precise is plausibly a grid-search discretization
   coincidence, not evidence the two configs share an identical period —
   consistent with (not contradicted by) the resolution-floor finding.

## Next

Ranked queue for Iteration 49, per Red Team's Phase-5 final-audit
reconciliation of all six Phase-5 seats' proposals (full reasoning in
`phase5_redteam_audit.md` §6):

1. **Merge EM's differential/beat-fit and QUANTUM's item (b) proposals —
   zero new FDTD cost.** Fit `delta_AB(θ)=C_B(θ)−C_A(θ)` directly for every
   adjacent ABSORB pair (reusing all 124 already-collected points), instead
   of independently fitting absolute periods and subtracting — converts an
   unresolvable absolute-frequency problem (QUANTUM: the C60–C70 pair needs
   `Δsinθ≥5.76`, exceeding the maximum achievable 2.0) into a
   phase-accumulation/beat-detection problem, and reuses the exact
   methodology that discovered T28 in the first place.
2. **Merge THERMODYNAMICS' matched-PAD amplitude probe and QUANTUM's item
   (a) into one new-config build** (~62–93 calls) — the only way to
   directly close the PAD/ABSORB confound (idealization 4b above): hold
   `PAD` fixed while `ABSORB` varies, scoring both THERMO's
   resolution-floor-free amplitude discriminator (primary) and the period
   fit (secondary, floor-caveated) on the same run.
3. **MATERIALS' mask-functional-form ablation** — cheap, answers whether
   the periodicity is tied to a length scale at all vs. the damping mask's
   numerical decay profile.
4. **PHOTONICS' two-tone joint fit** (zero-cost, desk-only) **+ EM's new
   ABSORB≈120 config** (31 calls) — direct tests of the saturating-mechanism
   candidate independently confirmed real this cycle (R²=0.998 saturating
   vs. 0.866 linear, at equal parameter count — see `phase5_redteam_audit.md`
   §1.5), run together, informed by item 1's result.
5. **VISION's window-discipline guidance** — do not reuse the 36°–42°
   window a third time for an absolute-period discriminator; a binding
   constraint on items 2–4's new FDTD spend, not a standalone item, already
   substantially satisfied by item 1's shift to differential/beat fitting.

`R_contact`'s literature search (PLAN.md queue item 2, 9 consecutive
cycles blocked on WebSearch/WebFetch tooling) remains unchanged in ranking
relative to T28 work — still untouched by this cycle's own locked
mandate; see `phase3_synthesis.md`'s tooling disclosure for the Director's
own capacity note.
