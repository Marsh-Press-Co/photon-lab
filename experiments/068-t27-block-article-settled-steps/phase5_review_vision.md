# Phase 5 Review — VISION SCIENCE (blind, fresh context)

*(Own charter's item — scoped this exact budget in exp-067's own phase5_review_vision.md. Full exhaustive independent recomputation; findings condensed here, all verified against source before writing.)*

## 1. Verification findings

**Minimum scope — satisfied and exceeded.** Tier0 (8 calls, ±35°×{600,750}nm×{C40,C80}@2800) matches the pinned minimum exactly; total 44 ≤ 45 ceiling, asserted in code not merely reported. Prediction-freeze discipline verified against git: `run.py` has zero post-freeze diff between the predict-commit and results-commit.

**GATE_HARD vs C_THR_LAB separation — correct throughout the actual scoring code**, traced every use: GATE_HARD appears only at the two empty-scene sites (P-068-1, P-068-5); C_THR_LAB appears only as a multiplicand for the MARGINAL band; MARGINAL_LO/HI are correctly applied as multipliers (giving the [0.0025,0.01] absolute band), boundary-equivalent to exp-065's own `bucket()` precedent.

**Deferral-count correction — stuck through every downstream artifact, but internally self-contradictory.** The corrected text says exp-067 "deferred it a third time," closes the streak "at three misses if it completes," yet also says a Tier0 failure "must be disclosed as a FIFTH consecutive miss" — under the same paragraph's own enumeration, a failure at cycle 45 would be the FOURTH miss, not fifth. Inherited from PLAN.md's own "FOUR consecutive cycles (Iterations 42→43→44)" phrasing. Non-load-bearing this cycle (the branch never fired) but will recur.

**P-068-1 scoping — correct at every site, and independently substantively tested, not just procedurally correct.** Recomputed: the MARGINAL bucket survives a full ±floor-width perturbation at both configs with 2.7–6.0× headroom to the nearer band edge — a check that exists nowhere in the committed record, only asserted in prose.

## 2. Verdict: PARTIAL (a high one)

The narrow claim endorsed without reservation: Block ARTICLE's re-certified MARGINAL is a stable, trustworthy instrument reading — six independent supports, each checked here. Not PROMISING because: (1) the scored N9 number exists at only one wavelength (600nm); (2) the instrument floor under it is no longer certified clean (P-068-1); (3) the number rests on an unconverged quadrature whose diagnostic (Block MINI) is now deferred a third consecutive cycle, undisclosed.

## 3. Ranked top-3 for Iteration 46

1. Block MINI's period-match test — build it or formally retire it, no third relabel.
2. Commit the floor-propagated uncertainty band on the bucket call as code, not prose.
3. Extend Block ARTICLE's N9 to 450nm — with a photopic/scotopic V(λ) argument that 750nm is a numerical-fidelity probe, not a witness-realism point, and 450nm is scotopically dominant and untested (the reported scene was a night flashlight sweep).

## 4. Process concerns (F1–F8, all independently verified against source)

- **F1**: stale "predictions committed, run not yet executed" status header survives in NOTES.md above the filled Result section.
- **F2**: "15–24% relative movement" recomputes to 14.15%/24.39% (R4-class prose figure, non-load-bearing — the scored quantity is the absolute delta, correct).
- **F3**: "two orders of magnitude inside the bar" for P-068-6 overstates by ~1 order (worst-cell margin ≈17.3×, ≈1.24 orders).
- **F4**: wrong idealization cross-reference in run.py (cites Idealization 10 for a claim that's actually Idealization 9).
- **F5**: two of the 44 committed FDTD calls (+35°/750nm article-present, both configs) are computed but never persisted to results.json — a real, non-load-bearing reproducibility gap.
- **F6**: the FOUR-cycles/FIFTH-miss self-contradiction (see above).
- **F7 — sharpest flag**: Block MINI's third consecutive deferral is nowhere counted, an asymmetry with this cycle's own meticulous Block-ARTICLE deferral handling.
- **F8**: results.json's `gates` dict mixes absolute and multiplier-valued thresholds with no unit label.
