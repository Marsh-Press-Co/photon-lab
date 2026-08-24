# exp-066 — Settling Re-Verification of exp-041's Block MAIN (T27 closure) (panel Iteration 43)

**2026-08-24 · driver: Clyde as panel Director · status: predictions
committed, run not yet executed**

Forty-third experiment of the panel program (PANEL.md / LOGBOOK.md). Lead
seat: **PHOTONICS** (rotation — VISION SCIENCE → PHOTONICS → MATERIALS →
ELECTROMAGNETISM → THERMODYNAMICS → QUANTUM OPTICS → repeat; Iteration 42
was VISION SCIENCE). Executes live thread **T27**'s Red-Team-ranked #1
priority for Iteration 43 (LOGBOOK.md T27 entry / PLAN.md queue, verbatim):
*"Re-verify `experiments/041-t20-angle-audit`'s own MAIN-block ±35°/±38°/
±40° rows at STEPS≥2800, and scope exactly how many downstream citations
are affected."*

## Hypothesis

`experiments/041-t20-angle-audit` (Iteration 18) measured its
`{36,37,38,39,40}°×{±}×{450,600,750}nm` "Block MAIN" — 30 rows, the
empty-scene per-angle Weber contrast floor `C_empty(θ,λ)` on the
plane/tapered-source ambient channel (`lab/ambient.py`) — at `STEPS=1400`.
exp-065 (Iteration 42) found this channel is NOT settled at that step
count: a 4-point convergence trend at one cell (40°/600nm/C40, C40 =
exp-041's own geometry verbatim) shows
`-0.010965→-0.002802→-0.002801→-0.002802` across
`STEPS=1400/2800/4200/5600` — a 74.4% shift, flat by 2800. **Hypothesis:**
STEPS=2800 is the settled floor generally across this channel's near-
grazing angle window (not just the one cell exp-065 measured), and the
remaining 18 of exp-041's own 30 Block MAIN cells (36°,37°,39°, both
signs, 3λ — the only cells this program has never re-measured beyond
STEPS=1400) will show the same order-of-magnitude correction.

## Setup

Reuses exp-065's own `CONFIGS["C40"]` (=exp-041's geometry verbatim,
already G-1-gated bit-exact against exp-041's committed data at 12/30
Block MAIN cells) and its `_settle_one`/`_c_empty` harness directly — see
`design_geometry.py`'s import-collision-safe loading mechanism and
`run.py`'s docstring. **Zero new `lab/` engine code.**

| Knob | Value | Source |
|---|---|---|
| Geometry | exp-041/exp-065's C40 config, unchanged | `CONFIGS["C40"]` |
| STEPS (baseline) | 1400 | exp-041's own original |
| STEPS (settled) | 2800 | exp-065's own 4-point convergence trend (flat by 2800) |
| STEPS (stress) | 4200, 5600 | exp-065's own convergence-trend extension |
| Angles, new FDTD | {36,37,39}°×{±} | the 18-row gap no committed data covers beyond STEPS=1400 |
| Angles, cited (fix A) | {35}°×{±} (fallback-only), {38,40}°×{±} (already-settled main-block) | `experiments/065-.../results.json`, `settled_sweep_steps2800_diagnostic.json` |
| Wavelengths | 450, 600, 750 nm | program standard |
| GATE_HARD | 0.001 | exp-024/041's own per-angle instrument-floor gate |

## T1 escape-route statement

**NONE.** Instrument/model-fidelity re-verification class, identical to
exp-041 (Iteration 18) and exp-064 (Iteration 41). No σ(I), σ(x,t),
angular-selectivity, or sub-threshold machinery is touched, advanced, or
claimed. Constraint 3 is not directly at stake this cycle.

## Panel record

Full five-phase cycle preserved verbatim: `phase1_proposal.md` (PHOTONICS,
lead), `phase2_critique_{materials,em,thermodynamics,quantum,vision}.md`
(five blind critiques, all support-with-changes), `phase2_redteam_audit.md`
(Red Team's final audit — verdict PROCEED-WITH-MANDATORY-FIXES, a 5-item
reconciled docket A–E), `phase3_synthesis.md` (Director's synthesis — all
five critiques' load-bearing findings accepted, zero overrides).

## Mandatory fixes applied (Red Team's docket, Phase 3)

**A.** Scope widened to cover the mandate's own literal "±35°/±38°/±40°"
text (not exp-041's internal "Block MAIN" naming alone) at zero new FDTD
cost — exp-065's own C40 config already has ±35°×3λ committed at both
STEPS=1400 and STEPS=2800.

**B.** The λ-coherence stress test is augmented with a genuine θ-axis
generalization check: 37°/600nm @ STEPS=4200 (1 new call), since zero of
the 18 new interior-angle cells had any independent convergence check of
their own in the Phase-1 draft.

**C.** P-066-4's fringe-fit refit is reported **strictly as a
fit-quality statistic** — no causal/mechanism language. Forward tripwire
(extended from exp-065's own QUANTUM-proposed, Red-Team-ratified
precedent): no future citation of this refit's R² may be read as
"confirmed edge-diffraction/coherent-fringe mechanism" while Block MINI's
period-match test (P-VIS42-10, exp-065) remains UNDECIDED.

**D.** `lab/caveat_lint_config.json`'s `exp065-steps1400-unsettled-plane-
channel` entry widened to make `REALIZABILITY_MEMO.md` reachable
(`candidate_globs` + `trigger_terms`, applied and verified live before
this predict-commit — see `phase3_synthesis.md`). `REALIZABILITY_MEMO.md`
is the **only** `lab/` file touched this cycle; no engine code changed
(`run.py`'s own `_lab_diff_excluding_registry` check enforces this).

**E.** R_contact disposition, stated once: PLAN.md's `R_contact` item
(CNT-forest root-to-substrate thermal contact resistance, TD-5's own
thinnest safety factor of any kind, 7.8× over κ_critical) is **deferred a
third consecutive cycle** (Iteration 41→42→43). This is disclosed, not
silent: R_contact is desk/literature-sourcing work on
`lab/thermo_sidecar.py`'s analytic Biot-number formula, orthogonal to
this cycle's FDTD budget — the two items never competed for the same
resource, so this is a scope-discipline choice (T27's own 19-iteration
citation exposure vs. one margin number), not a resource trade-off. A
fourth consecutive deferral would itself be worth flagging at Iteration
44 (T27's own closing note, restated here per THERMODYNAMICS' request).

## Predictions — committed before this experiment's first run

**P-066-G1 (absolute identity gate).** The 18 new STEPS=1400 cells
(`{36,37,39}°×{±}×3λ`) reproduce exp-041's committed `results.json::
block_main` `C_empty` values bit-exact.
- **CONFIRM:** `ΔC = 0.0` (float64 equality) for all 18.
- **REFUTE:** any nonzero Δ — **halts the cycle before STEPS=2800 is
  trusted.**

**P-066-1 (magnitude of settling correction, 18 new cells).** Basis: the
already-measured 12-cell range on ±38°/±40° (0.0007–0.0145 absolute,
15–89% relative away from near-zero-crossing cells).
- **CONFIRM:** median `|ΔC(2800−1400)|` ∈ **[0.001, 0.010]**.
- **REFUTE:** median < 0.0003 (interior angles anomalously immune) or >
  0.020 (worse than any measured precedent).

**P-066-2 (sign-flip prevalence, 18 new cells).** Basis: exp-041's own
Phase-4 finding that the fringe sign-flips almost every 1° across
36°–43°, and 4/4 of the ±35° cells sign-flipped under this same
correction (this cycle's own fix-A citation, see `phase3_synthesis.md`).
- **CONFIRM:** ≥3 of 18 cells sign-flip between 1400 and 2800.
- **REFUTE:** 0 of 18 flip.

**P-066-3a (λ-coherence stress test, 40°/750nm — is 750nm actually
converged at 2800?).**
- **CONFIRM:** `|ΔC(4200−2800)|` ≤ **1%** of `|ΔC(2800−1400)|` (matches
  600nm's own 4200/5600 plateau, 0.04% change, from exp-065).
- **REFUTE:** `|ΔC(4200−2800)|` ≥ **5%** of `|ΔC(2800−1400)|** — 750nm
  needs STEPS>2800 even for Block MAIN, sharpening not closing item #2's
  own "750nm not fully converged" open question.

**P-066-3b (θ-coherence stress test, 37°/600nm — mandatory fix B, does
settling generalize across the axis that actually differentiates the 18
new cells?).**
- **CONFIRM:** `|ΔC(4200−2800)|` ≤ **1%** of `|ΔC(2800−1400)|`.
- **REFUTE:** `|ΔC(4200−2800)|` ≥ **5%** of `|ΔC(2800−1400)|` — settling
  at STEPS=2800 does not generalize across θ, only along λ, undermining
  the whole cycle's own extrapolation basis.

**P-066-4 (T21 fringe-fit refit, desk-only, zero FDTD cost — STRICTLY
STATISTICAL, mandatory fix C). Basis: exp-042's own committed
`r2_cstar=0.7852421354715854` (sign_agree 27/30, `c*=1.6196430704378861`)
against the STEPS=1400 dataset.**
- **CONFIRM:** the settled-data `r2_cstar` stays within **±0.10** of
  0.7852421354715854 — the propagator's fit quality is not materially
  degraded by the settling correction. *Makes no claim about which
  physical mechanism, if any, the fit quality establishes* — see fix C
  and `design_geometry.FRINGE_FIT_STATISTICAL_ONLY_NOTE`.
- **REFUTE:** `r2_cstar` drops below **0.4**.

## Idealizations

- **2D TMz, single polarization** — inherited from every prior cycle on
  this channel.
- **Angular sampling: exactly exp-041's own 10-angle Block MAIN set,
  1° granularity, 36°–40°, plus the ±35° fallback-only cells cited under
  fix A.** Does not extend to Block EXTEND (41°–43°) or the interior
  `FALLBACK_ANGLES` (0°,±5°,±15°,±25°) — explicitly PLAN.md item #2's
  scope, deferred not silently dropped.
- **Wavelength set: the program's standard 3λ (450/600/750nm) quadrature
  only** — the stress tests (P-066-3a/3b) probe two (θ,λ) cells as
  proportionate, not exhaustive, generalization checks.
- **`STEPS=2800` is licensed by convergence evidence at two cells this
  cycle (40°/750nm via P-066-3a, 37°/600nm via P-066-3b) plus exp-065's
  own original 40°/600nm point — three of the program's 36 mandate-scope
  cells directly convergence-tested; the remaining 33 are extrapolated,
  not individually verified to STEPS=4200+.**
- **The 750nm settling-residual mechanism is disclosed, not adjudicated**
  — see `design_geometry.SETTLING_MECHANISM_NOTE`: the turn-on-ramp
  candidate (~107 steps) is roughly one order of magnitude too small to
  be the dominant driver (Red Team's corrected arithmetic); a stronger
  already-committed candidate (exp-042's own `MARGIN_PERIODS`, thinnest
  at 750nm) is named but not tested as a causal claim by any gate here.
- **P-066-4's refit is a fit-quality statistic only** — see mandatory
  fix C. It does not adjudicate T21's own mechanism-vs-settling-artifact
  question (Block MINI's period-match test, P-VIS42-10, remains
  UNDECIDED — unchanged by this cycle).
- **No R3 (spatial-resolution) cross-check in this leg** — cpl held
  fixed throughout, matching exp-041's own original scope.
- **Graded damping bands, not PML; window means, not point-wise `B(y)`**
  — standard bench convention, unchanged.
- **Bench-scale only** (r=78 cells) — no witness-scale (T8/T13/T14)
  claim of any kind.
- **R_contact deferred a third consecutive cycle** — see mandatory fix E,
  disclosed above, not silent.

## Run plan

`python3 run.py` — 39 new FDTD calls (Block G1EXT 18, Block MAIN2800 18,
Block STRESS 3), `ProcessPoolExecutor` (4 workers for G1EXT/MAIN2800, 3
for the small STRESS block), results written to `results.json`. Full
bench (`lab/validation/run_all.py --only
12346789,10,11,18,19,20,21,22,23,24`) reverified green before and after
(no `lab/` engine change, so this is a formality per house discipline,
not expected to move; the one `lab/` file touched this cycle,
`caveat_lint_config.json`, is a data registry with no trust-suite stage).

## PHASE 4 — RESULTS

*(to be filled in after the run — see `phase4_results.md`)*
