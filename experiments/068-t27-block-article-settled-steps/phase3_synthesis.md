# Phase 3 Synthesis — Director — Panel Iteration 45 (exp-068)

Red Team's verdict: **PROCEED-WITH-MANDATORY-FIXES**. All seven mandatory docket items are **accepted, zero overridden**. This is a rare full six-way convergence (five blind support-with-changes + Red Team PROCEED-WITH-MANDATORY-FIXES) with disjoint, additive flip conditions — the Director's job here is mechanical reconciliation, not adjudication between conflicting seats.

## Accepted (all seven mandatory items, verbatim per Red Team's docket)

1. **Deferral-count correction** (VISION's catch, Red Team-confirmed against `PLAN.md:2424-2436`/`LOGBOOK.md:13846-13852` directly): this is the **FOURTH** consecutive cycle (Iterations 42→43→44→45) Block ARTICLE's article-present legs have not closed; a Tier-0 failure must be disclosed as a **FIFTH** consecutive miss, not a fourth. Applied throughout NOTES.md/run.py below.
2. **Tier0/Tier1 double-count fix** (Red Team's own Attack 1, self-found — no seat caught this): Tier1's article-present block is the **7 interior** `FALLBACK_ANGLES` only (0°,±5°,±15°,±25°), not all 9 — ±35° is already covered by Tier0. 14 calls, not 18.
3. **Tier2 disambiguation** (PHOTONICS' flip, Red Team Attack 4): Director takes Red Team's recommended resolution — extend Tier2 to **both** C40 and C80, both wavelengths (600/750nm), at STEPS=4200 vs 2800, article-present, θ=−35°. 4 calls, never de-scoped (folded into the mandatory floor alongside Tier0).
4. **Caveat propagation** (THERMODYNAMICS' flip, elevated to mandatory by Red Team Attack 7): `T5_THERMAL_CAVEAT`, `REALIZABILITY_MEMO_CAVEAT`, `G_TRANSFER_T15_CAVEAT` (all three, verbatim from exp-065's `design_geometry.py`) are printed and written into `results.json` at every site stating Block ARTICLE's C value or PASS/MARGINAL bucket.
5. **M3 propagation** (Red Team's own Attack 3, the hidden constraint-3 angle no seat surfaced): exp-066's own M3 sentence — *"GATE_HARD is not VISION's own perceptual bar, and this result does not by itself move any constraint-3 verdict"* — is printed and written into `results.json` at every site reporting a GATE_HARD tally (P-068-1 and P-068-5).
6. **REALIZABILITY_MEMO contingency** (MATERIALS' flip): if the article-row C (N9, 600nm) flips past MARGINAL_LO=−0.0025 at either config, this same shift's close opens a `REALIZABILITY_MEMO.md` Amendment 2 revising the D_req-as-lower-bound language — not merely a relabel. Coded as an explicit check in `run.py`, flagged loudly in output if triggered.
7. **caveat_lint registry widening** (Red Team's own Attack 6): `exp065-steps1400-unsettled-plane-channel`'s `required_sites` widened to add `experiments/068-.../NOTES.md` and `experiments/068-.../phase4_results.md`. Applied directly to `lab/caveat_lint_config.json` as a disclosed, separate step (same precedent as exp-066's own mandatory fix D) — **not** gated by this experiment's own `_lab_diff_excluding_registry()` check, exactly as exp-066 established.

**Nice-to-have, also applied** (QUANTUM's flip): a one-line NOTES.md/results.json tripwire barring citation of the 14 new interior-angle empty-scene cells as bearing on T21 mechanism-vs-artifact until Block MINI's own dense scan runs (queue item 3, not this cycle's scope).

## One further correction, caught at Director synthesis (not by any of the six seats or by Red Team's own docket text)

Red Team's own docket arithmetic has a small internal inconsistency: it states the double-count fix gives "total = 38" (8+14+14+2), then says extending Tier2 by 2 more calls "land[s] at 42" — but 38+2=40, not 42. **Corrected total: 40 calls, ceiling 45** (8 Tier0 + 14 Tier1-article-interior + 14 Tier1-empty-interior + 4 Tier2 = 40). This is a Director-caught arithmetic error in Red Team's own reconciliation, not a re-opening of any seat's substantive finding — recorded here per R4 discipline (never propagate an unverified number, including one from Red Team itself).

## Final synthesized design (exp-068)

| Block | Content | Calls |
|---|---|---|
| **Tier 0 — mandatory floor** | Article-present, θ=±35°, λ∈{600,750nm}, config∈{C40,C80}, STEPS=2800 | 8 |
| **Tier 1a — N9 recertification, article** | Article-present, θ∈{0,±5,±15,±25}° (7 interior angles), config∈{C40,C80}, λ=600nm, STEPS=2800 | 14 |
| **Tier 1b — N9 recertification, empty floor** | Empty scene, θ∈{0,±5,±15,±25}° (7 interior angles), config∈{C40,C80}, λ=600nm, STEPS=2800 | 14 |
| **Tier 2 — convergence-generalization stress** | Article-present, θ=−35°, λ∈{600,750nm}, config∈{C40,C80}, STEPS=4200 (vs. the STEPS=2800 value from Tier 0) | 4 |
| **Total** | | **40** (ceiling 45) |

Tier 0 and Tier 2 are never de-scoped (they are now the same size and jointly form the mandatory floor per fix 3 above). If a genuine hard-stop pressure appears, Tier 1b (empty interior) is trimmed first (its data is lower-stakes — a floor check, not the scored article row), then Tier 1a.

Empty-scene companions for the ±35°/{600,750}nm/{C40,C80} pairs (needed to score Tier 0's article rows) are **not re-run** — cited directly from `experiments/065-t24-absorb-boundary-sweep/settled_sweep_steps2800_diagnostic.json`, already at STEPS=2800, zero marginal cost (verified present and matching exp-066's own citation convention).

T1 escape route: **N/A** (instrument/model-fidelity re-verification class), unchanged from the Phase-1 proposal.

## Overridden

**None.** Six-for-six convergence; every flip condition applied.

## Experiment number

**exp-068**, directory `experiments/068-t27-block-article-settled-steps/`.

Predictions committed to git in `NOTES.md` **before** `run.py`'s first FDTD call, per house discipline — see `NOTES.md`.
