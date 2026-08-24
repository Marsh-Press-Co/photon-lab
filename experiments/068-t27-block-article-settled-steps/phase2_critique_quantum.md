# Phase 2 Critique — QUANTUM OPTICS (blind, fresh context)

## Steel-man

The proposal keeps the expressibility contract clean: τ=0.0065 enters purely as a fixed classical σ_e (SIGMA_OFF_PASS = tau/(2·R_OUT)), no σ(I) or state-dependence is claimed, and it correctly carries forward the REALIZABILITY_MEMO Amendment's disclaimer rather than re-claiming the retracted PASS/MARGINAL as physical. Since the article is optically thin and static, EM's passivity null (article-present settling should track the empty channel's settling, not converge toward something smaller) is the right test: if P-068-2/3 confirm, that is itself informative for my discipline — it's evidence against any exotic state-dependent absorption transient, since such a mechanism would be expected to introduce its own settling timescale distinct from the passive boundary's. Tight pre-registered bands make this a genuine, not rhetorical, null-result check.

## Sharpest attack

Tier1 adds 14 NEW empty-scene interior-angle (0°,±5°,±15°,±25°) settling-delta cells at STEPS=2800 — exactly the kind of data Block MINI's queued desk check (PLAN.md Iteration-45 item 3: "does the existing settling-delta dataset already show `A·cosθ`-periodic structure matching T21's period") would be tempted to glance at, at only 5° spacing — the same statistical-underpowering QUANTUM's own Phase-5 self-catch just relabeled P-VIS42-10 UNDECIDED over ("a period-match fit from 5 points spanning ~1 T21 period was judged too statistically underpowered to trust"). Nothing in §5 (Idealizations) or §6 commits a caveat-lint tripwire — this program's standard remedy — forbidding future citation of these 14 cells on the mechanism-vs-artifact question before Block MINI's properly-powered scan runs. The expressibility contract itself is fine (σ_e is genuinely fixed and classical, no smuggled coherence); the risk is procedural sequencing, not physics framing.

## Verdict: support-with-changes

## Flip condition

Add a caveat-lint registry entry (or explicit forward tripwire in NOTES.md) barring any citation of the 14 new interior-angle empty-scene settling-delta cells as bearing on T21 mechanism-vs-artifact until Block MINI's own dense scan runs — or, cleaner and cheaper, resequence: since PLAN.md's item 3 desk check is zero-cost and explicitly meant to run *before* any new FDTD spend, run it first on the existing 36-cell Block MAIN dataset, then let exp-068 proceed knowing whether its own new interior data risks contaminating or duplicating that pending result.
