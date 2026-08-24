# Phase 1 Proposal — Panel Iteration 45 — Lead: ELECTROMAGNETISM

**Branch chosen: (a).** Take T27's Block-ARTICLE settled-STEPS FDTD leg as a scoped secondary item with a pre-committed, capped call budget (42 calls planned, 45-call hard ceiling), reusing exp-065/066's harness verbatim where possible.

*(This document is the verbatim Phase-1 deliverable from the fresh-context ELECTROMAGNETISM sub-agent. Phase-3 synthesis — including the corrected call budget (40, not 42) and the mandatory-fix docket — is recorded in `phase3_synthesis.md`; do not read this file's numbers as final.)*

---

## 1. Mechanism/task narrative (≤300 words)

This is not a mechanism proposal — T1 escape route: **N/A**. It closes an instrument-trust gap left open by exp-065/066: Block ARTICLE (the *only* construction in this program's history to ever produce a scored constraint-3 PASS/MARGINAL number, τ_center=0.0065) was scored entirely at STEPS=1400, on the exact plane/tapered-source empty-scene channel exp-065 showed is *not* settled by 1400 steps at near-grazing angles — and at exactly the ±35° cells feeding Block ARTICLE's own N9 aggregate, which sign-flip under the STEPS=2800 correction (C40/−35°/600nm: +0.00112→−0.00440; /750nm: −0.00095→+0.00552).

My charter contribution is the passivity argument that governs what to *expect* here, extended from exp-066's own finding on the empty channel. exp-066's EM review established that this channel's boundary is graded loss, not a perfectly-matched termination — a genuinely dissipative, passive boundary condition. A passive lossy wall has no thermodynamic obligation for its converged residual field to trend toward zero — STEPS=1400's reading was a large transient that happened to cancel the T21 edge-diffraction fringe at some cells, not a "cleaner" estimate. **That reasoning is about the domain's boundary, not the object inside it.** A τ=0.0065 disk is optically thin — its own relaxation is a small linear perturbation on the ambient field, introducing no new long timescale comparable to the ~2800-step domain-transit/multi-bounce settling the boundary itself needs. So I predict the article-present channel's settling behavior should track the empty channel's own settling behavior in magnitude and general character (not average it away), and should **not** be expected to converge to a "smaller," "safer" reading merely because an absorber is present. This is a falsifiable causality/passivity claim, not a hope.

## 2. Parameter table

Experiment number reserved: **exp-068**.

| Knob | Value | Note |
|---|---|---|
| Configs | `CONFIGS["C40"]`, `CONFIGS["C80"]` (exp-065 `design_geometry.py`, verbatim, no new config) | C40 = exp-041's geometry verbatim, identity anchor; C80 = congruent series, ABSORB=80/PAD=40 |
| Article | `off_pass`-analog uniform disk, τ_center=**0.0065** (`TAU_OFF_PASS`), σ_e=**4.1667×10⁻⁵** (`SIGMA_OFF_PASS`=τ/(2·R_OUT)), R_OUT=**78** cells | Bit-identical article construction to exp-065's Block ARTICLE — analog, not re-measurement |
| Wavelengths | 600nm (full N9) + **750nm added** (new — exp-065's Block ARTICLE was 600nm-only) | cpl 20 / 25 |
| Angles | Full `FALLBACK_ANGLES` = (−35,−25,−15,−5,0,5,15,25,35) at 600nm; ±35° only at 750nm | |
| STEPS | **2800** (settled floor) for all new legs; one **4200** stress pair | |
| GATE_HARD | 0.001 (empty-scene rows) | |
| C_THR_LAB / MARGINAL band | 0.005 / [0.5, 2.0]× | |
| Baseline (STEPS=1400) | `C_empty,N9`=−3.3×10⁻⁵ (C40)/−1.3×10⁻⁴ (C80); article `C`=−0.00450 (C40)/−0.00460 (C80), bucket **MARGINAL** both | RETRACTED pending this re-verification |

**Call budget — original three-tier design (SEE phase3_synthesis.md — Red Team caught a 4-call double-count in Tier1; corrected total is 40, not 42):**

| Tier | Content | New calls (as originally proposed) |
|---|---|---|
| 0 — mandatory floor | Article-present ±35°, λ∈{600,750}, {C40,C80}, STEPS=2800 | 8 |
| 1 — N9 recertification | Article-present all 9 FALLBACK_ANGLES × {C40,C80} × 600nm (18) + empty-scene interior angles × {C40,C80} × 600nm (14) | 32 |
| 2 — convergence-generalization stress | C40 only, (−35°,600nm) and (−35°,750nm) at STEPS=4200 | 2 |
| Total (as originally proposed) | | 42 |

De-scope order if the hard stop is approached: drop Tier 2 first, then trim Tier 1's interior-angle empty block. Tier 0 is never de-scoped.

**Code reused vs. new:** Reused unchanged: `lab/fdtd2d.py::Sim`, `lab/sections.py`, `lab/ambient.py`; exp-065's `design_geometry.py` constants; exp-065's `run.py`'s `_one_run`/`_c_empty`/`_c_n9`/`_profile`/`_article_one`/`_settle_one`. Reused as committed data (zero new calls): exp-065's `results.json` and `settled_sweep_steps2800_diagnostic.json`. New: one worker composing `_article_one`'s sigma-injection with `_settle_one`'s STEPS parameter, plus a harness-continuity gate.

## 3. T1 escape route

**N/A — instrument/model-fidelity class**, matching exp-065/066's own precedent.

## 4. Per-metric predicted outcomes, falsifiable bands, and pre-registered flip conditions

**P-068-1** (empty N9 floor, settled, 600nm, both configs): CONFIRM |C_empty,N9(2800)| ≤ GATE_HARD=0.001 both configs. REFUTE: either breaches GATE_HARD.

**P-068-2** (article row C, N9, 600nm, settled vs 1400): CONFIRM |ΔC| ≤ 1.5×10⁻³ per config, bucket stays MARGINAL both, sign stays negative. REFUTE |ΔC| > 4×10⁻³ either config, or bucket disagreement. Pre-registered flip: baseline C≈−0.0045/−0.0046, MARGINAL band |C|∈[0.0025,0.01]. Flip to PASS requires ΔC ≥ +0.0020 (C past −0.0025). Flip to FAIL requires ΔC ≤ −0.0054 (C past −0.01).

**P-068-3** (sign persistence): CONFIRM stays negative both configs. REFUTE: sign flips.

**P-068-4** (750nm ±35° bracket vs 600nm): predict 750nm shift LARGER. CONFIRM within 2× of 600nm's. REFUTE exceeds 3×.

**P-068-5** (GATE_HARD count, interior empty legs, 600nm): predict interior angles show milder settling defect than grazing. CONFIRM ≥12/14 pass. REFUTE ≤7/14 pass.

**P-068-6** (convergence-generalization stress): CONFIRM |ΔC(4200−2800)| ≤ 0.01×|ΔC(2800−1400)|. REFUTE ratio ≥0.05.

## 5. Idealizations

2D TMz; bench-scale only (r=78 cells); article is an analog not a re-measurement; REALIZABILITY_MEMO Amendment stands, this cycle probes instrument uncertainty only; incoherent N9 quadrature not converged (T16/T21); Block MINI's period-match question stays UNDECIDED, out of scope; the passivity argument is a physical expectation, not a proof; interior-angle empty-scene legs have never been run at any STEPS beyond 1400.

## 6. Explicit disclosure — the deferral count

*(EM's own original count here read "3 consecutive iterations so far... 4th consecutive miss if it fails." Red Team's Phase-2 audit found this off by one against the program's own already-published record — PLAN.md/LOGBOOK.md's Iteration-44 close state "four consecutive cycles... fifth-consecutive-deferral" verbatim. Corrected text, per Phase-3 synthesis: this is the FOURTH consecutive cycle (Iterations 42→43→44→45) Block ARTICLE's article-present legs have not been closed; if this proposal runs as designed, Iteration 45 is the first of those four in which it is the cycle's actual primary, dedicated FDTD work. If Tier 0 fails to complete, that must be disclosed as a FIFTH consecutive miss, not a fourth.)*
