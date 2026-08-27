# PHASE 2 — CRITIQUE · VISION SCIENCE · Panel Iteration 58 · exp-081

**Seat:** VISION SCIENCE (human perceptual limits — contrast thresholds,
luminance edge detection, spectral sensitivity, adaptation, temporal
sensitivity, attentional blindness; duty: pin numeric thresholds, with
sources, BEFORE any run that scores against them). Blind to other seats'
current-cycle critiques.

## Steel-man (≤150 words)

This cycle finally builds and correctly scores the one construction nine
T28 cycles have been circling: `E_direct+r(90°−θ_beam)·W(θ_beam)`, against
REAL reference periods, not a candidate curve. Item 1a re-verifies
PAD-invariance bit-exact (a fourth independent confirmation). Item 1b
honestly reports its own "0.0 bit-identical" prediction as technically
REFUTED (`~10⁻¹⁴` residual) rather than rounding it to a pass, then traces
the residual to floating-point cancellation of two `O(100)` values — more
informative than the naive check would have been. Item 1c, not originally
pre-registered, is added specifically because a lone near-boundary SUPPORT
deserves scrutiny (this sub-thread's own R5 look-elsewhere discipline) and
correctly downgrades a mechanical NEITHER to a substantive REFUTE-leaning
reading. Item 3's energy bound (`~116,000×` looser under the wrong angle
convention) is a genuinely useful, permanently negative finding.

## Sharpest attack (≤150 words)

The "N/A — constraint 3 not engaged" framing is correctly and consistently
applied: I grepped the entire proposal and NOTES.md for `C_thr`/contrast/
threshold language — "ambient-contrast channel" names the T28 signal's
*location* (inherited terminology, `lab/ambient.py`'s channel), never a
perceptual comparison. Unlike T16 (exp-076/077), no ratio is ever divided
by `C_thr` here. That charge doesn't stick.

The record-hygiene gap does: **`git status` shows the entire
`experiments/081-.../` directory is untracked — zero commits exist.**
Every T28 cycle since exp-076, including this cycle's own direct ancestor
exp-080, committed the frozen-predictions text to git in a dedicated
commit *before* the run commit (verified: `23203cc`/`6fb6b99` for exp-080).
That is precisely the mechanism exp-080's own Phase-5 VISION reviewer used
to confirm "pre-registration is genuine (`git log -p`)." Here, that check
is structurally unavailable — only a self-authored "compliance note"
attests the predictions were frozen before the script ran. File mtimes are
*consistent* with the claimed order (script 857s → results 863s → NOTES
1009s → final proposal edit 1159s) but cannot prove the predictions
section itself was untouched during that final edit, since the whole file
was rewritten as one artifact with results appended, not diffed. PANEL.md's
literal text binds the git-before-run mandate to Phase 3, so this is not a
rules violation — but it is a real, avoidable regression in auditability
below the standard this exact sub-thread's own immediately preceding cycle
set and relied on.

## Verdict: **support-with-changes**

The science is sound, honestly self-scored, and closes real ground (T21
compromise-fit diagnosis, the energy-budget bound). The one required change
is procedural, not physical: commit `phase1_proposal.md`'s predictions
section to git now, before Phase 3 synthesis, so a future Phase-5 reviewer
can independently verify pre-registration the way exp-080's own reviewer
did — rather than trusting this cycle's own self-report.

## Parameter change that would flip my verdict

None needed to flip to plain **support** — a same-shift `git commit` of the
frozen-predictions text (even now, out of temporal order, with an honest
note that it was captured late) would fully close this gap. Conversely, if
it turned out the predictions text in `phase1_proposal.md` had in fact been
edited *after* seeing `phase1_results.json` (I found no positive evidence
of this, only the absence of proof against it), that would flip me to
**oppose** — a self-scored REFUTE-leaning reading that cannot be
independently dated is exactly the failure mode R4's "precisely
recomputed" rule and this thread's own R9 dimensional-audit discipline
exist to prevent one level upstream of arithmetic: not "is the number
right," but "is the claimed *order of events* verifiable at all."
