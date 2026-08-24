# PHASE 5 — REVIEW · MATERIALS & METAMATERIALS · Panel Iteration 42 · exp-065

Fresh-context read. `results.json`, `settled_sweep_steps2800_diagnostic.json`,
`phase4_results.md`, `NOTES.md`, `phase1_proposal.md`,
`phase2_critique_materials.md`, `phase2_redteam_audit.md`,
`REALIZABILITY_MEMO.md`, `PANEL.md`, `LOGBOOK.md` (full read per Director
packet) all consulted directly; every number below is read from the
committed JSON, not from prose.

## 1. Does the disclosure discipline around τ=0.0065 hold up against the real numbers?

**At the level it was designed to check: yes.** `results.json::scored.
P-VIS42-7.caveats` carries all three caveat strings verbatim and
code-produced (`REALIZABILITY_MEMO_CAVEAT`, `G_TRANSFER_T15_CAVEAT`,
`T5_THERMAL_CAVEAT`), exactly discharging my own Phase-2 critique's fix 1/2
demand. `tier_label` reads "BENCH-SCALE SURROGATE ONLY... no Tier-W/Tier-A
verdict". The REALIZABILITY_MEMO caveat states the correct fact precisely:
D_req≈540–600× is a *lower* bound, not an achieved reference (memo
Amendment, Iteration 12) — this cycle's MARGINAL bucket for τ=0.0065 at a
*third* geometry (r=78-native/exp-041, distinct from exp-032's own and
exp-034's r=156) is consistent with, not contradictory to, that standing
finding: a third independent measurement now shows this τ failing to clear
the perceptual bar. Nothing here re-opens or narrows the memo's own
UNOBTANIUM-WITH-PARAMETERS verdict, and the document does not claim
otherwise.

**But the disclosure is silent on a deeper problem the results themselves
now surface, and this is the finding I am adding at Phase 5.** T24's own
settling confound (P-VIS42-11, REFUTED 400× past its bar) was diagnosed by
the Director using only θ=40°/600nm/C40 (Diagnostic 2: clean, monotone
convergence, 1400→2800 shrinks |C| by 74%, flat through 5600). I pulled
`settled_sweep_steps2800_diagnostic.json` — which *does* contain settled
(STEPS=2800) readings at ±35° that `phase4_results.md` never tabulates by
angle-pair the way it does for ±40° — and computed C40/C80 at ±35°/600nm,
1400 vs 2800:

| cfg | θ | C_empty(1400) | C_empty(2800) |
|---|---|---|---|
| C40 | −35° | +0.001120 | **−0.004397** |
| C40 | +35° | +0.001762 | **−0.003973** |
| C80 | −35° | +0.000529 | **−0.003018** |
| C80 | +35° | +0.001179 | **−0.002645** |

This is not the "same pattern, smaller magnitude" the Director's residual
discussion (§ "Where the residual max lives") implies for 600nm — **it is a
sign flip**, at all four cells, at the exact wavelength Block ARTICLE is
scored at. The ±40° convergence (Diagnostic 2) is monotone and single-signed;
the ±35° convergence is not merely unsettled, it crosses zero. And ±35° is
not a bystander angle — it is **two of the nine `FALLBACK_ANGLES` legs that
compose Block ARTICLE's own N9 aggregate**, the exact channel P-VIS42-6/7
score against.

**What this does and does not show.** `_c_n9()` builds the N9 reading from
combined window fluxes across all nine angles *before* one Weber-contrast
step — it is not an average of the nine per-angle `C_empty` values in
`block_sweep`/`block_pad`, so the sign-flip above does not arithmetically
prove the aggregate itself misbehaves. But it removes the only thing that
made the aggregate's tiny empty floor (C40: −3.3×10⁻⁵, C80: −1.3×10⁻⁴)
credible as a *converged* cancellation rather than a *coincidental* one:
two of its nine contributing legs are now shown, at this cycle's own
wavelength, to be dominated by an unsettled transient large enough to flip
sign. **Block ARTICLE's N9 aggregate was never itself re-run at STEPS=2800**
(disclosed generally in idealization 12/13, but not argued specifically) —
so P-VIS42-6/7's CONFIRMED status rests on an instrument reading that is
demonstrably built, in part, from inputs known to be unsettled at the
governing wavelength. This is a real gap the committed record does not
close, not a refutation of the CONFIRMED verdicts as scored.

**Is Block ARTICLE insulated because it's scored at N9/600nm, not the raw
±40° legs?** No — not cleanly. It would be insulated if its wavelength or
its angle set avoided the affected regime; it does neither. It IS partially
insulated by aggregation (N9's own reading, whatever its true settled value,
is an order of magnitude smaller than any single contaminated leg,
consistent with genuine partial cancellation across 9 angles even under
noise) — but "partially insulated by construction" is different from
"settling-clean," and the record currently claims the latter implicitly by
reporting P-VIS42-6/7 as CONFIRMED without this caveat.

## 2. Verdict (MATERIALS' own charter standard)

**PARTIAL.** No realizability tier moves — REALIZABILITY_MEMO.md is
correctly and explicitly not re-scored by this cycle, and I concur nothing
here should change it. But MATERIALS' charter is the realizability *bound*,
and every bound this program has stated or will state on a σ(I)-class OFF
article rests, transitively, on this program's ambient-contrast instrument
reading true values. This cycle both (a) failed to resolve T24's own
question (the stated headline outcome) and (b) surfaced — via its own
disclosed follow-up data, not fully narrated — a second, more severe
instance of the same failure mode sitting inside the exact channel every
constraint-3/realizability-adjacent τ citation in this program's future will
use. That is a genuine, load-bearing contribution even though it settles
nothing. Not PROMISING (nothing new clears a realizability bar, and the
cycle's own headline question is explicitly undecided); not RULED OUT
(nothing here rules out any mechanism class or forecloses future work).

## 3. Ranked top candidate next directions (MATERIALS' priority ordering)

1. **Re-verify Block ARTICLE's own N9 aggregate directly at STEPS≥2800** (not
   inferred from the individual-leg table) at C40 and C80/600nm — the
   cheapest, most load-bearing open item. Until this runs, any future
   citation of an N9-scored τ bucket (including this cycle's own P-VIS42-7)
   carries an uncharacterized, possibly sign-relevant, settling uncertainty
   at exactly the angles (±35°) that most contaminate it.
2. **Re-verify `experiments/041-t20-angle-audit`'s own MAIN-block ±38°/±40°
   AND now ±35° rows at STEPS≥2800**, and scope which of T21's fringe-model
   fit, T16's quadrature deltas, and any near-threshold τ citation since
   Iteration 18 are built on unsettled inputs — this is squarely the
   Director's own "Next" item 1, and I concur it is the correct next FDTD
   spend, ahead of any new mechanism or literature work.
3. Only after (1)–(2): resume MATERIALS' own queued backlog
   (`PLAN.md`'s CNT `R_contact` term, `length_provenance` hardening, the CNT
   pitch/diameter+conductivity query bundle) — none of it is invalidated by
   this cycle, but a future OFF-state σ(I) candidate evaluated against this
   same instrument, before (1)/(2) close, would inherit an unquantified
   floor risk this seat should not sign off on.

## 4. Checkpoint criterion — my own reasoned opinion

**Criterion 4 fires, in my judgment.** Not because a constraint was quietly
dropped or a claim is unfalsifiable in the Red-Team sense, but because this
is precisely "program-integrity drift": a load-bearing instrument-floor gap
(STEPS=1400 unsettled, now shown to include a sign-flipping ±35° component
at the article-scoring wavelength, not just the already-disclosed ±40°
magnitude collapse) has been silently inherited across nineteen iterations
and multiple headline citations (T21's fringe fit, T16's quadrature deltas,
every near-threshold constraint-3 τ reading since Iteration 18) without
anyone measuring it until this cycle's own incidental follow-up. The
Director explicitly declines to pre-empt this ruling; I vote it fires,
independent of whatever PHOTONICS/EM/VISION conclude on their own axes,
because from MATERIALS' seat the consequence is concrete: no future
realizability verdict this program issues on an ambient-contrast-scored τ
can be trusted at its stated margin until this is closed.
