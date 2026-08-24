# exp-069 — Block MINI's Period-Match Test, Powered Up

**Panel Iteration 46.** Lead: THERMODYNAMICS (by rotation). Director
synthesis post Phase 2 (five blind critiques + Red Team's Phase-2 audit,
verdict PROCEED-WITH-MANDATORY-FIXES, 10-item docket, **zero overridden** —
full record in `phase1_proposal.md`, `phase2_critique_{photonics,materials,
em,quantum,vision}.md`, `phase2_redteam_audit.md`, `phase3_synthesis.md`).

## Mandate

PLAN.md's Iteration-46 queue, item 1, **LOCKED, unconditional**:

> Block MINI's period-match test — LOCKED, unconditional. T21's own
> mechanism-vs-artifact question, deferred-behind-relabeling for a third
> consecutive cycle at minimum... Either build the properly-powered FDTD
> version (≥2–3 T21 periods at ~0.2° spacing, settled STEPS≥2800,
> desk-first per QUANTUM's own zero-cost check on the existing
> settling-delta dataset before any FDTD spend) or formally retire the
> test with a stated reason — no further relabeling, no further
> citation-tripwire-only treatment.

Born of LOGBOOK Iteration 45's CHECKPOINT (criterion 4 fired): Block MINI's
period-match test (`P-VIS42-10`, exp-065) has been deferred-behind-
relabeling for three (or four, by this program's own more literal count)
consecutive cycles.

## Desk-first check (zero FDTD cost, run and committed BEFORE this design)

`desk_check_settling_delta.py` (committed separately, see git log) reads
exp-066's own already-committed 36-cell Block MAIN settling-delta dataset
(`delta(theta) = C_2800 - C_1400`, fixed padding) and finds the adjacent-pair
sign-flip fraction is 1.0/0.6/0.8 at 600/450/750nm. **This is a DIFFERENT
quantity than Block MINI's own scored test** (a STEPS-settling delta at
fixed padding, not the padding delta `C80-C40` at fixed STEPS) — Phase 2
(PHOTONICS + QUANTUM, independently) found the original framing of this
result ("600nm cleanest/least-aliased") was **backward**: 600nm's perfect
flip-fraction is the textbook signature of near-Nyquist aliasing (0.503
samples/period at 1° step), not clean resolution. Corrected framing (below):
600nm is scoped as primary because it matches `P-VIS42-10`'s own original
scope, not because the desk check favors it.

## Setup

Reuses `experiments/065-t24-absorb-boundary-sweep`'s harness **verbatim** —
`CONFIGS["C40"]`/`CONFIGS["C80"]` (the congruent `ABSORB`/padding
construction, `A=752` cells held fixed), `Sim`/`ambient`/`sections` calls
unchanged. **Zero `lab/` diff.**

| Block | Angles | λ | STEPS | Configs | Calls |
|---|---|---|---|---|---|
| DENSE | 36.0°–42.0°, 0.2° step (31 pts, center 39.0°, ≈3.06 T21 periods) | 600nm | 2800 (settled) | C40, C80 | 62 |
| SETTLE-C80 | {39.0°, 40.0°} | 600nm | 4200 | C80 | 2 |
| R3 (resolution) | {39.0°, 40.0°} | 600nm, **cpl=30** (geometry ×1.5, mirrors exp-033's own R3 idiom) | 4200 (=2800×1.5) | C40_R3, C80_R3 | 4 |
| LEG750 | 38.0°–41.0°, 0.2° step (16 pts, ≈1.22 T21 periods — NOT powered the same as 600nm, disclosed context only) | 750nm | 2800 | C40, C80 | 32 |
| **Total** | | | | | **100** |

Cost basis: `design_geometry.py::fdtd_budget()` (code-produced, not
hand-typed — house rule R4). Predicted: **100 calls, ≈6637 CPU-s, wall ≈32.5
min, 3× envelope ≈97.4 min.** Recomputed **hard stop: 100 min** (restated per
Red Team's mandatory-fix docket item 7 — the original Phase-1 hard stop of
75 min is superseded by this larger, corrected design; the recomputed 3×
envelope of 97.4 min sits just under it). Pre-declared de-scope order if
breached, applied in this priority (least to most load-bearing): trim Block
LEG750 (generalization-breadth) first, then Block R3 (resolution — but
retirable only down to the C80-alone minimum Red Team named), never Block
DENSE or Block SETTLE-C80 (these gate the headline claim directly).

## T1 escape route

**N/A — instrument/model-fidelity re-verification class**, identical in
kind to exp-041/065/066/068. No mechanism proposed; constraint 3 not
directly at stake.

## Idealizations

1. 2D TMz, single polarization.
2. **600nm primary, 750nm confirmatory (not full 3λ)** — corrected
   justification (Phase-2 mandatory fix 6): matches `P-VIS42-10`'s own
   original scope; the desk check's "600nm least-aliased" framing was
   backward (see above) and is NOT the reason for this scope.
3. Positive θ branch only (36°–42° / 38°–41°) — not a symmetry test.
4. `C40`/`C80` only — the two configs `P-VIS42-10` was built to difference.
5. The period-match statistics (P-069-2/3) test **consistency with** T21's
   established stationary-phase-limit model (`P(θ)=λ/(A·cosθ)`, fit to real
   FDTD data at R²=0.7852→0.8271, **never 1.0**), not an independently
   verified exact period (Phase-2 mandatory fix 2, EM's catch).
6. Bench scale only (r=78 cells) — no witness-scale claim.
7. `A=752` held fixed at native cpl (G-2 identity, exp-065, already passed);
   Block R3's own `A_r3=1128` is the same physical aperture, checked in code
   (`design_geometry.py` assertion).
8. Single-angle `C_empty`, not an N9/N17 aggregate — T25/T26 do not apply.
9. **R_contact (PLAN.md's Iteration-46 queue item #2) remains untouched
   this cycle** — still blocked on WebSearch/WebFetch tooling, not picked
   up in parallel despite PLAN.md's explicit invitation to do so if
   capacity allows (Phase-2 mandatory fix 9, MATERIALS' catch — disclosed,
   not silently dropped).

## Scoring currency — stated once, before any run

All `C_empty` values are single-angle instrument-floor readings scored
against `GATE_HARD=0.001` where cited elsewhere; **this cycle's own scored
predictions (P-069-1 through -5) are NOT scored against `GATE_HARD` or any
perceptual threshold** — they are internal statistics of the `delta(θ)`
series itself (amplitude ratio, R² of a periodic fit), per PANEL.md's
instrument/model-fidelity class.

## Predictions — committed to git BEFORE the run (house discipline)

| ID | Claim | CONFIRM | REFUTE |
|---|---|---|---|
| **P-069-G1** | Absolute identity gate. θ∈{38°,40°}×{C40,C80}×600nm×STEPS=2800 reproduce exp-065's committed `settled_sweep_steps2800_diagnostic.json` exactly (4 values, loaded programmatically). | `ΔC=0.0` for all 4 | any nonzero Δ — halts the cycle |
| **P-069-1 (HEADLINE)** | Amplitude clause. `ptp/\|mean\|` of `delta(θ)=C80(θ)−C40(θ)` over the 31-point Block DENSE window. Raw `ptp` and `mean` reported alongside (mandatory fix 10). | `ptp/\|mean\| ≤ 1.5` | `ptp/\|mean\| > 2.5` |
| **P-069-2 (HEADLINE, primary period)** | Fixed-period fit `delta(x)=c₀+a·cos(2πx/T)+b·sin(2πx/T)`, `x=sinθ`, `T=cpl/A=0.026595745` **fixed**. R² vs flat null. | `R² ≤ 0.15` | `R² ≥ 0.50` |
| **P-069-3 (co-gating, secondary period)** | Free-period grid search, `P*∈[1.0°,4.0°]`, best R². | within tolerance: `\|P*−P(39°)\|/P(39°) ≤ 20%` AND `R²(P*) ≥ 0.30` | out of tolerance: `≥50%` deviation, or no `P*` clears `R²≥0.30` |
| **P-069-4 (co-gating, settling)** | Block SETTLE-C80: `\|ΔC(4200−2800)\|` at θ∈{39°,40°}, relative to `\|ΔC(2800−1400)\|` at the same cells (1400 values reused from exp-065's committed `block_mini`). | ≤1% relative at **both** cells | ≥5% relative at **either** cell |
| **P-069-5 (co-gating, resolution/R3)** | Does `delta(θ)` at θ∈{39°,40°} survive cpl 20→30 (geometry ×1.5, mirrors exp-033's R3 idiom)? | same sign at both angles AND ratio `delta_r3/delta_native ∈[0.3,3.0]` at both | sign flip at either, OR ratio outside `[0.1,10]` at either |
| **P-069-6 (disclosed, non-gating)** | 750nm amplitude/period statistics, same form as P-069-1/3, over the 16-point LEG750 window (~1.22 periods — under-powered vs. the 600nm leg by design; context only). | — | — |

## Combined Verdict — computed in code, pre-committed logic (mandatory fixes 1, 3, 4)

- **COHERENT-FRINGE, fully corroborated** ⟺ P-069-1 REFUTE **AND** P-069-2
  REFUTE **AND** P-069-3 within tolerance **AND** P-069-4 CONFIRM **AND**
  P-069-5 CONFIRM. All five must hold — P-069-4 and P-069-5 are BINDING
  preconditions, not independent side-rows (Red Team's own catch: a prior
  draft of this design let P-069-1/2 alone license "not settling" language
  without actually checking P-069-4 — fixed).
- **ADDITIVE-SYSTEMATIC, vindicated** ⟺ P-069-1 CONFIRM **AND** P-069-2
  CONFIRM.
- **Anything else ⇒ immediate FORMAL RETIREMENT of the period-match test**,
  stated reason (recorded verbatim, computed in `run.py`, not written
  after the fact): *"Statistical power was raised to the mandate's own
  spec (31 points/0.2° step/~3.0 periods, settled STEPS=2800, a resolution
  check, a settling-closure check, and a co-gating free-period
  cross-check) and the result is still non-decisive — that is itself the
  finding."* **This is NOT reported as PARTIAL-and-deferred** (mandatory
  fix 4 — the direct fix for the "PARTIAL escape hatch" VISION SCIENCE's
  Phase-2 critique identified as this design's single most important
  gap, given this program fired Checkpoint criterion 4 exactly one cycle
  ago on the identical failure shape).

**Checkpoint-criterion-2 candidacy: none.** No mechanism class is bounded
here — this is instrument closure, either direction.

## Gates

Full bench (`lab/validation/run_all.py`, stages 1–25, heavy stage 5
optional) green before and after — **193/193 reconfirmed this shift before
any panel work began** (heavy stage 5 skipped per house convention). No new
trust-suite stage (zero `lab/` diff; `run.py`'s own `assert_lab_clean()`
idiom reused verbatim). Binding stages: 1 (angle_deg=0 bit-exactness), 6
(phasor conventions), 9 (the ambient instrument itself). One local
**absolute-identity** gate, **P-069-G1**, gates every other number.

---

## Result

*(filled in after Phase 4 — see `phase4_results.md`)*
