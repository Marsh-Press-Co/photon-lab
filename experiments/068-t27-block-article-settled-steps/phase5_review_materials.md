# Phase 5 Review — MATERIALS & METAMATERIALS (blind, fresh context)

## 1. Verification findings

**(a) `realizability_memo_amendment_needed: false` — recomputed independently, correct.** C40=−0.005601, C80=−0.005253, MARGINAL_LO=0.0025, MARGINAL_HI=0.01. Both |C| sit inside (0.0025,0.01), not close to either edge (C40 2.24× LO, 56% of HI; C80 2.10× and 53%). Bucket logic in `run.py:345-356` verified correct; `realizability_flip` only populates on a PASS bucket, neither config is PASS. Scope observation, not a bug: the coded contingency only gates a PASS-direction flip, not FAIL-direction — moot this cycle.

**(b) `REALIZABILITY_MEMO.md` standing text — still accurate, no update owed, correctly not touched.** exp-068's settled-STEPS result (MARGINAL, not PASS) is consistent with — mildly reinforces — Amendment 1's standing finding.

**(c) Caveat propagation — present and verbatim, but with one standing gap.** Diffed T5_THERMAL_CAVEAT/REALIZABILITY_MEMO_CAVEAT/G_TRANSFER_T15_CAVEAT against source: byte-identical, genuinely imported. GATE_HARD_M3_NOTE verbatim at both required sites. **However**: `lab/caveat_lint_config.json` still has ZERO entry mechanically guarding this propagation (grep confirmed) — a gap first recommended at exp-065's own Phase-5 Red Team audit ("before any future cycle cites this article's caveats"), still open two cycles later. The actual mandatory fix (manual carrying) was honored; the mechanical guard was not registered.

**(d) Build-time corrections — no MATERIALS-specific concern.** Both touch instrumentation/aggregation methodology, not material parameters.

## 2. Verdict: PROMISING

The one MATERIALS-relevant question (does settled-STEPS re-verification threaten REALIZABILITY_MEMO.md's standing tier) comes back cleanly negative, correctly computed and disclosed. The pre-registered contingency worked exactly as designed.

## 3. Ranked top-3 for Iteration 46

1. R_contact literature search (still the only queued item that can move a number).
2. Register the missing caveat_lint_config.json entry for T5_THERMAL_CAVEAT/REALIZABILITY_MEMO_CAVEAT/G_TRANSFER_T15_CAVEAT.
3. Block MINI's period-match test.

## 4. Process-concern flags

`lab/caveat_lint_config.json` has no entry for the three caveats — standing gap first flagged in exp-065's own Phase-5 audit, reconfirmed unresolved in exp-068's own Phase-2 Red Team audit Attack 5, still true after this cycle closes.
