# PHASE 2 — CRITIQUE · MATERIALS & METAMATERIALS · Panel Iteration 42

## Steel-man (≤150 words)

The proposal is unusually disciplined about *not* smuggling a realizability
claim. T1's escape route is stated N/A and defended (§3: "no σ(I)... claim is
made or advanced"); §5 cleanly separates the instrument-floor bar
(`GATE_HARD=0.001`, scores Blocks SWEEP/PAD/BEAM) from the perceptual bar
(`C_thr=0.005`, scores Block ARTICLE only) — exactly the distinction exp-041's
own mandatory fix 1 exists to enforce, and it is honored here rather than
merely cited. Idealization 8 correctly scopes Block ARTICLE as "an analog, not
a re-measurement" of `off_pass`, sharing τ and construction idiom but not
domain, and explicitly disclaims re-adjudicating exp-032's PASS→MARGINAL
history. §8.2 does not hide the fact that `ABSORB` has never before been a
*controlled, swept* variable — it states the counter-argument against its own
"no new machinery" position in its own text and commits to a Phase-3 fallback
build if Red Team disagrees. For a zero-mechanism instrument cycle, this is
close to the right posture.

## Sharpest attack (≤150 words)

`REALIZABILITY_MEMO.md` names τ_off=0.0065 by number as *the* anchor of this
program's whole σ(I) verdict: "The best-characterized OFF article is τ_off =
0.0065 (exp-032's off_pass)... the only σ(I) OFF-state configuration in this
program's history to clear that bar" — the article this memo built D_req≈
540–600× and UNOBTANIUM-WITH-PARAMETERS from, by name. `phase1_proposal.md`
never cites `REALIZABILITY_MEMO.md` once, and P-VIS42-7 — the row that reports
a fresh PASS/MARGINAL/FAIL *bucket* for exactly that σ, at a geometry this
article has never been measured at — carries no realizability caveat inline.
Idealization 8 disclaims re-adjudicating exp-032's PASS→MARGINAL *history*,
but says nothing about the article's standing UNOBTANIUM status; a reader
hitting a new bucketed verdict for this exact τ, unqualified, could easily
mistake it for live movement on a candidate mechanism rather than a pure
instrument stress-test — precisely the omission this seat's charter exists to
catch. Compounding it: P-VIS42-7's "descriptive-only" central estimate,
0.00449, is computed via g≈0.69 — T15's own transfer constant, which T15
itself states is "specific to this bench's own... geometry specifically, not
a portable constant even among gas-host articles at other standoffs." Applying
it at exp-041's geometry (not exp-030/032's) to produce a headline-adjacent
number, even hedged "not scored," reports a precision the program's own
standing finding says is unlicensed.

## Verdict: **support-with-changes**

The engineering is sound and the boundary-systematic question is legitimate
and overdue (nineteen iterations deferred). Nothing here revives R1/R2/R3/R4/
R5, and no new σ(I) mechanism claim is advanced — the T1 route N/A
self-classification is honest for Blocks SWEEP/PAD/BEAM. But Block ARTICLE
does touch the one live realizability finding this program has on this exact
numeral, and the proposal's own document is silent on it at the one place
(P-VIS42-7) a future cycle is most likely to cite out of context. Two fixes,
both cheap and zero-FDTD:

1. Add a one-line `REALIZABILITY_MEMO.md` cross-reference inline at P-VIS42-7
   ("this σ is `off_pass`'s own, scored UNOBTANIUM-WITH-PARAMETERS,
   Iteration 11/14 — this row is an instrument diagnostic, not a
   realizability re-check").
2. Either strike the 0.00449 central estimate from P-VIS42-7 or re-label it
   as carrying T15's own non-portability caveat explicitly in the same
   sentence, not by cross-reference to §6 alone.

Neither fix touches the FDTD budget, the gates, or any falsifiable band —
this is a documentation-completeness objection, not a design objection, which
is why it does not rise to oppose.

## Parameter change that would flip the verdict

Add the one-line `REALIZABILITY_MEMO.md` cross-reference to P-VIS42-7 (fix 1
above) before Phase 3 freeze. With that single addition, verdict → support.
