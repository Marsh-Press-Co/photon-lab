# PHASE 1 — PROPOSAL · Panel Iteration 43 · Lead seat: PHOTONICS

*Fresh sub-agent, PHOTONICS charter, per PANEL.md's independence mechanics.
Preserved verbatim as delivered.*

## Candidate exp-066 — Settling Re-Verification of exp-041's Block MAIN (T27 closure, item #1)

### 1. Mechanism/scope narrative (≤300 words)

This is not a mechanism proposal. PHOTONICS' charter question — is the optical response coherent across wavelength and angle? — is exactly what T27 put in doubt: `experiments/041-t20-angle-audit` (Iteration 18) measured its {36°,37°,38°,39°,40°}×{±}×{450,600,750}nm "Block MAIN" — 30 rows, the empty-scene per-angle floor `C_empty(θ,λ)` on the plane/tapered-source ambient channel — at `STEPS=1400`, and exp-065 (Iteration 42) showed that channel is not settled at that step count: a 4-point convergence trend at one cell (40°/600nm/C40) shows `-0.010965→-0.002802→-0.002801→-0.002802` across `STEPS=1400/2800/4200/5600` — a 74.4% shift that fully resolves by 2800, and does not recur at STEPS beyond that. `STEPS≥2800` is therefore the correct floor: it is the first step count at which this channel's own committed convergence evidence goes flat, not an arbitrary doubling.

Scope-definition, resolved rather than inherited: exp-041's own `MAIN_ANGLES = {36,37,38,39,40}×{±}` (30 rows) is textually distinct from `FALLBACK_ANGLES = {0,±5,±15,±25,±35}` (exp-024's baseline quadrature, 9 angles, no overlap with MAIN except in spirit). exp-065's own `settled_sweep_steps2800_diagnostic.json` already covers `{-40,-38,-35,35,38,40}°` — the intersection with Block MAIN is only `{±38,±40}` (12 of 30 rows); `±35°` is a FALLBACK-only cell, relevant to T16/Block-ARTICLE citations but outside "MAIN-block" proper. This proposal targets Block MAIN as textually defined: closing the 18-row gap (`{36,37,39}×{±}×3λ`) that no committed data anywhere in this program covers at any STEPS beyond 1400.

**T1 escape route: NONE.** Instrument/model-fidelity re-verification class, identical in kind to exp-041 and exp-064 (Iteration-18/41 precedent) — no σ(I), σ(x,t), angular-selectivity, or sub-threshold machinery is touched or advanced.

### 2. Parameter table

**Already committed, citable directly (zero new calls):**

| Data | Source | Coverage | STEPS |
|---|---|---|---|
| Block MAIN, all 30 rows | `experiments/041-t20-angle-audit/results.json::block_main` | {36,37,38,39,40}°×{±}×{450,600,750}nm | 1400 (baseline for the delta) |
| Settled re-sweep, 12 of 30 MAIN rows | `experiments/065-.../settled_sweep_steps2800_diagnostic.json` (`C40` key = exp-041 geometry verbatim, G-1-gated bit-exact) | {±38,±40}°×3λ | 2800 |
| Settled re-sweep, 6 adjacent FALLBACK rows (not MAIN) | same file | {±35}°×3λ | 2800 |
| 4-point convergence trend, 1 cell | `settling_trend_diagnostic.py`/`_output.txt` | 40°/600nm/C40 | 1400/2800/4200/5600 |

Measured relative shifts on the 12 already-settled MAIN rows (computed this cycle from the two committed files above, for calibration — not new data):

| λ | θ=±38° shift | θ=±40° shift |
|---|---|---|
| 450nm | 70–75% | 16% |
| 600nm | 83–89% | 69–74% |
| 750nm | 15–16% | 60–62% |

**New FDTD calls proposed (all via exp-065's own `CONFIGS["C40"]`/`_one_run`/`_c_empty`, `design_geometry.py`+`run.py` — zero `lab/` changes):**

| Block | Cells | STEPS | Calls | Purpose |
|---|---|---|---|---|
| G-1′ extension | {36,37,39}°×{±}×3λ | 1400 | 18 | extend exp-065's G-1 anchor from 12/30 to 30/30 MAIN cells (§3) |
| MAIN-2800 | {36,37,39}°×{±}×3λ | 2800 | 18 | close the Block MAIN gap — the core deliverable |
| λ-coherence stress test | 40°/750nm/C40 | 4200, 5600 | 2 | PHOTONICS' own charter demand: does 750nm's longer source ramp mean 2800 isn't actually converged there? |

**Total: 38 new FDTD calls**, same order as exp-041's own 38-call budget. Cost basis: `settling_trend_diagnostic.py`'s single-threaded per-call times (20.6s@1400 → 53.1s@5600) and exp-041's 38-call/137.8s 4-worker wall-clock ⇒ projected **≈8–12 min wall-clock at 4-way parallelism**.

**Recommended scope: full closure (38 calls), not the narrow ±38°/±40°-only reuse (0 new calls).** Justification against R4 and cost/stakes:
- **Cost is trivial** (minutes, not the hours this program's budget guards normally worry about) — the cost asymmetry that would justify the narrow scope elsewhere doesn't exist here.
- **R4 directly bites the narrow option.** exp-042's entire T21 fringe fit (`chord_model`/Huygens sum) was scored against **all 30** Block MAIN rows (`experiments/042-t21-magnitude-bridge/NOTES.md:11`, `:338`). Re-verifying only 12 of those 30 and then citing "Block MAIN re-verified at settled STEPS" would itself be a new instance of the citation-imprecision this cycle exists to close.
- The 18 ungated cells (36°,37°,39°) sit *inside* the oscillation window exp-041 itself measured to sign-flip almost every 1° — there is no basis to assume they behave like their neighbors rather than needing independent measurement.

### 3. Verification/gate design

- **G-1′ (absolute identity, extends exp-065's own G-1).** The 18 new STEPS=1400 reruns must reproduce exp-041's own committed `results.json::block_main` `C_empty` values **bit-exact** (`ΔC = 0.0`, float64 equality) for all 18 cells. Failure halts the cycle before any STEPS=2800 number is trusted.
- **G-2 (reused, not re-derived).** `static_construction_identity` — N/A here (no padded geometry introduced), recorded as N/A rather than silently dropped.
- **Independent spot-check.** The λ-coherence stress test (40°/750nm/C40 at STEPS=4200,5600): if `|ΔC(4200−2800)|` exceeds 5% of `|ΔC(2800−1400)|`, STEPS=2800 is not actually settled at 750nm.
- **Full bench** reverified before and after.

### 4. Citation-scoping plan

**Mechanical pass (zero cost).** `lab/caveat_lint_config.json`'s existing entry `exp065-steps1400-unsettled-plane-channel` already ships `trigger_terms`/`candidate_globs`. Run this lint config as a repo-wide grep to produce a candidate site list.

**Scoring rule.** AFFECTED-NUMERIC (conclusion changes) / AFFECTED-DISCLOSURE (survives numerically but stated as settled without disclosure) / UNAFFECTED.

**First-pass results:**
- `experiments/042-t21-magnitude-bridge/NOTES.md:11,338` — AFFECTED-NUMERIC, load-bearing: T21's entire edge-diffraction magnitude fit was regressed against all 30 STEPS=1400 Block MAIN rows.
- `experiments/046-.../NOTES.md:495` — AFFECTED-DISCLOSURE.
- LOGBOOK.md T16, T20, T21, T24 entries — AFFECTED-DISCLOSURE.
- exp-065's own P-VIS42-6/7 — already RETRACTED; re-scoring is item #2's job.

### 5. Predictions — falsifiable bands, committed before any run

| ID | Claim | CONFIRM | REFUTE |
|---|---|---|---|
| P-066-G1 | G-1′ extension: 18 new STEPS=1400 cells reproduce exp-041's committed block_main bit-exact | ΔC=0.0 for all 18 | any nonzero Δ — halts cycle |
| P-066-1 | Magnitude of settling correction, 18 new cells | median \|ΔC(2800−1400)\| ∈ [0.001, 0.010] | median <0.0003 or >0.020 |
| P-066-2 | Sign-flip prevalence, 18 new cells | ≥3 of 18 flip | 0 of 18 flip |
| P-066-3 | λ-coherence stress test at 750nm | \|ΔC(4200−2800)\| ≤1% of \|ΔC(2800−1400)\| | ≥5% |
| P-066-4 | T21 fringe-fit refit (desk-only), corrected-data R² vs original | stays within ±0.10 of original | drops below 0.4 |

### 6. Idealizations

2D TMz single polarization; angular sampling exactly exp-041's 10-angle MAIN set (36-40°, no Block EXTEND 41-43°, no interior FALLBACK_ANGLES); standard 3λ only; STEPS=2800 licensed at exactly one prior cell (40°/600nm) — this cycle's P-066-3 is the first λ-generalization test; no R3 spatial-resolution cross-check; does not investigate WHY the transient behaves as it does; bench-scale only.
