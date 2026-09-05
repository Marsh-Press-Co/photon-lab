# Phase 2 Critique — VISION SCIENCE (Panel Iteration 89, exp-112)

*Blind critique. Not seen and did not seek out any other seat's Phase-2
output this cycle.*

## Steel-man (≤150 words)

This cycle's disclaimer discipline is a genuine improvement, not a repeat.
The single-source `DISCLAIMER` string (`run.py` lines 231–251) explicitly
rules out Weber-contrast, `C_thr(L)` scoring, and σ(I)/σ(x,t)/sub-threshold
content, and — verified directly against source, not taken on the
proposal's own say-so — is enforced by TWO independent, committed,
re-invocable asserts: `run.py`'s own `--predictions-only` block (line 304)
and `analyze.py`'s Phase-4 `__main__` (line 141). That closes exactly the
predictions/result asymmetry that recurred twice on this same T28
sub-thread (exp-108, R23's founding instance; exp-111, the R23 First
Addendum) before this cycle even opens. T1/constraint-3 is correctly,
structurally confirmed N/A: this is a pure floor-comparison classifier and
a congruent grid-resolution refactor, with no expressible σ(I)/σ(x,t)/
angular-selectivity content anywhere in the actual code. Complying with the
R23 First Addendum's spirit ahead of its own pending ratification is
exactly the right posture for a Panel proposal to take toward an open
Tier-0 governance item.

## Sharpest attack (≤150 words)

The phrase "detection floor" (`phase1_proposal.md` §1, used twice: "genuine
... signature from instrument/quantization noise at a detection floor,"
"what counts as a genuine signal vs. instrument artifact at/near a
detection floor") is never disambiguated from a *human* perceptual
detection threshold — VISION's own charter question, and constraint-3's
own vocabulary ("what would make a human eye FAIL to register something
physically present"). Critically, this phrase sits in §1's mechanism
narrative, which is verifiably OUTSIDE the code-enforced `DISCLAIMER`
string: I read `run.py` lines 231–251 (the actual asserted text) and
"detection floor" does not appear in it — only "Weber-contrast," `C_thr(L)`,
and σ(I)/σ(x,t) are named. Nothing asserted anywhere blocks a future,
citation-shortening reviewer (this program's own R4/R9 lineage is built
entirely from that failure mode) from lifting "distinguishing signal from
noise at a detection floor" as if it bears on observer-detectability. This
exact quantity class — an unlabeled percentage/SNR-ratio figure — already
caused one real unit-conflation error on this program (R9, T16, Iteration
53–54: a field-magnitude ratio miscompared directly against `C_thr`). An
ambiguous, un-asserted phrase of the identical shape, sitting one section
away from the one place a code-level check actually looks, is not a
hypothetical risk.

## Verdict: support-with-changes

## Single parameter change that would flip to unconditional support

Add one clause to `DISCLAIMER` itself (so R23's existing asserts cover it
for free): *"'detection floor' throughout this document means the K=3/K=1
mirror-pooled-floor instrument's own SNR floor — a grid-discretization
noise threshold, not a human perceptual or observer-detection threshold;
no constraint-2/3 claim is made or implied by this term."* That single
edit closes the gap this critique found using the exact mechanism
(single-source string + existing asserts) the cycle already built, without
requiring any new machinery.
