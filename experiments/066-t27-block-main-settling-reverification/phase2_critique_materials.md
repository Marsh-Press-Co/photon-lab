# PHASE 2 — CRITIQUE · Panel Iteration 43 · Seat: MATERIALS & METAMATERIALS

*Fresh sub-agent, blind to the other four seats' critiques this cycle. Preserved
verbatim as delivered.*

**On charter standing, stated up front:** this cycle proposes no material, no
mechanism, no ε(ω)/σ law of any kind — it is a pure STEPS-convergence
re-verification of an existing empty-scene instrument channel, T1 escape
route correctly declared NONE. MATERIALS' realizability-bound duty ("what
could physically realize the proposed optical behavior") has no direct
object here; I am not manufacturing a mechanism critique to fill the seat.
My standing is indirect: this channel's numbers feed MATERIALS' own
downstream realizability verdicts, and that dependency is what I critique.

## Steel-man (for)

MATERIALS' charter has nothing to grip here, and the proposal is honest
about that — T1=NONE, matching PANEL.md's explicit precedent for
instrument-trust cycles (exp-041/exp-064). More importantly, its scope
stays clean of MATERIALS' own load-bearing numbers: Block MAIN's
36°/37°/39° cells sit outside the `FALLBACK_ANGLES`/N17 quadrature that
`REALIZABILITY_MEMO.md`'s g₀≈0.69–0.70 and D_req≈537–600× figures are
calibrated from, so nothing here can silently move MATERIALS' own
UNOBTANIUM-WITH-PARAMETERS verdict without a separate, disclosed step.
The two absolute-identity gates (bit-exact G-1′, N/A'd G-2) and the
R4-grounded argument for full 30-row closure over a cheaper 12-row reuse
are sound instrument hygiene — a precondition for every realizability
call this program will ever make downstream of this channel, even though
this cycle moves none of them.

## Sharpest attack (against)

§4's citation-scoping plan presents itself as comprehensive — "the
enumeration instrument, already built" — but never once names
`REALIZABILITY_MEMO.md`, the document holding MATERIALS' charter-defining
UNOBTANIUM-WITH-PARAMETERS verdict, whose own D_req≈537–600× is
calibrated from `off_pass` at N9/N17 quadrature — a set that includes
±35°, already confirmed by T27 to sign-flip under settling correction. I
checked directly: the memo matches NONE of `caveat_lint_config.json`'s
`candidate_globs` (it lives outside `NOTES.md`/`phase*.md` naming and
outside the two named experiment dirs), and contains none of the entry's
`trigger_terms` (it predates T24/exp-065's vocabulary entirely). The tool
this proposal deputizes as its closure mechanism is structurally blind to
MATERIALS' own highest-stakes downstream artifact — and §4's own R4
argument for full-vs-partial closure applies with equal force against
itself: a citation audit that silently omits this document is exactly
the "partial standing in for complete" failure this cycle exists to
close.

## Verdict: **support-with-changes**

The core proposal (Block MAIN closure, 38 calls, absolute gates) is sound
and outside MATERIALS' domain in a way it correctly discloses. The one
gap is §4's implicit claim of completeness.

## Parameter change that would flip to unconditional support

Add one desk-only line to §4: explicitly check `REALIZABILITY_MEMO.md`'s
reachability under the current `caveat_lint_config.json` entry, and
either widen `candidate_globs`/`trigger_terms` to cover it or state on
the record why its g₀/D_req chain is currently judged unaffected. Zero
FDTD cost, matches the cycle's own methodology exactly — it just needs to
be pointed at MATERIALS' own document, not only PHOTONICS'/QUANTUM's.
