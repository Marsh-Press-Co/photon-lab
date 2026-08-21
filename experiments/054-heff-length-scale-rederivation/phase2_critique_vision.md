# Phase 2 Critique — VISION SCIENCE (blind, independent)

## Steel-man

Scope discipline is genuinely clean: the word "eye," "human," "contrast,"
"luminance," "photopic," "scotopic," and "constraint-3" appear **zero**
times anywhere in `phase1_proposal.md`. This is the correct posture — the
proposal touches only `h_eff`'s upstream length input, never
`netd_disposition`'s own logic, and correctly inherits (rather than
re-litigates) that function's already-in-place disclaimer, won as my
seat's own mandatory fix at Iteration 20: "NETD is an instrument/detector
threshold, not a human perceptual one... this classification does NOT
bear on constraint-3/4's human-eye verdict." NETD_BAND_K itself is not a
new numeric threshold requiring my gatekeeper sourcing duty this cycle —
it is cited verbatim from an already-sourced Iteration-20 figure
(P-D7-4, `[0.020,0.050]` K), not re-derived or re-scored against fresh
here. No implicit visible-light claim is smuggled in anywhere I can find.

## Sharpest attack

The proposal's silence is the defect. Nowhere in its own text — including
P-054-2 and P-054-4, the two headline predictions, which report bare
"×NETD-lo margin" numbers — does it restate that these margins say
nothing about human-eye detectability. That silence is not neutral in
this program's actual record: the NETD/human-eye conflation has already
recurred as a documented, VISION-caught defect at least three times —
Iteration 17 (fired Checkpoint criterion 4), Iteration 22 ("dropped
across all 1664 sweep points"), and Iteration 23 ("'eye-invisible'
language... unflagged... one cycle after this program invented the
SUPERSEDED banner for this exact failure mode"). This cycle mints two new
prediction IDs and a new trust-suite stage that will get quoted verbatim
into NOTES.md prose and the LOGBOOK Iteration 31 entry. As scoped, Phase 4
carries no explicit requirement to attach the disclaimer sentence at
those quotation points. Given a base rate of three-for-three prior
cycles where an undisclosed carry-forward reintroduced this exact
conflation, omission here is a near-certain fourth recurrence, not a
hypothetical one.

## Verdict

**support-with-changes**

## Flip condition

Add one explicit Phase 4/3 scope line: the disclaimer sentence ("NETD is
an instrument/detector threshold, not a human perceptual one — does not
bear on constraint-3/4") must be reproduced verbatim at every locus where
P-054-2, P-054-4, or P-054-5's UNDETECTABLE classification is quoted
outside `lab/thermo_sidecar.py` itself — i.e., in `results.json`'s new
keys, NOTES.md's Results/Learned prose, and the LOGBOOK Iteration 31
entry. With that line added, this flips to plain **support**.
