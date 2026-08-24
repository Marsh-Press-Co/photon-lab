# Phase 2 Critique — PHOTONICS (blind, fresh context)

## Steel-man (≤150 words)

The proposal's physical claim is well-grounded, not asserted blind: exp-065's own Phase-4 diagnostic (`experiments/065-.../phase4_results.md` lines 143–155) traced the 750nm settling residual to a **source-side** mechanism — ramp length scales with `cpl`, so 750nm's cpl=25 gives a 67% longer ramp than 450nm's cpl=15 — not to anything about an object in the scene. A weak, non-resonant τ=0.0065/σ_e≈4.2e-5 disk sitting inside a domain whose settling is governed by source ramp-up and graded-boundary decay has no obvious channel to introduce a *new* long timescale; EM's passivity argument (already load-bearing in exp-066, explaining the 31/36→34/36 GATE_HARD count) is the same logic applied one level up. Reusing exp-065/066's `_article_one`/`_settle_one` idioms verbatim to build `_article_settle_one` is genuinely zero-new-physics, and the harness-continuity gate (bit-exact reproduction of a known settled empty cell) is the right pre-flight check before trusting any new number.

## Sharpest attack (≤150 words)

STEPS=2800 has **never been confirmed settled at the exact cell this proposal's Tier0 rests on**. exp-066's only 750nm convergence-ratio check (P-066-3a, `phase4_results.md` line 23) is at θ=40°, C40, **empty** scene — a non-crossing angle, article-absent. The cell that actually matters — θ=−35°/750nm, article-present, C40/C80 — is exactly the one that sign-flipped 1400→2800 (−0.00095→+0.00552, confirmed in `phase4_results.md` lines 250–251) and sits near a zero-crossing where transient decay can behave differently than at 40°. The proposal's *only* direct test of whether 2800 is actually converged there is Tier2 (2 calls, C40-only, −35°/{600,750}nm at 4200) — and Tier2 is explicitly named first to be cut ("De-scope order... drop Tier2 first"). So the single empirical check that would validate the load-bearing "STEPS=2800 = settled floor" assumption at the highest-residual wavelength and highest-stakes angle is optional, C40-only, and never covers C80. If Tier2 is dropped, every 750nm number in Tier0/Tier1 rests on an untested extrapolation from a different angle and a different scene state.

## Verdict

**support-with-changes**

## Parameter change that would flip my verdict to support

Move the Tier2 stress pair (−35°/750nm at STEPS=4200 vs 2800, both C40 and C80) into Tier0 (mandatory floor, never de-scoped) instead of Tier2 (first cut) — even at the cost of trimming Tier1's interior-angle count, since Tier1's 600nm-only interior sweep is lower-stakes than validating the one wavelength/angle pair the headline settled-vs-1400 comparison actually depends on.
