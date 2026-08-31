# PHASE 2 — CRITIQUE · VISION SCIENCE seat · exp-097

*Constraint-3 perceptual metrics are N/A this cycle (zero-FDTD code-verification,
no ambient/contrast claim anywhere in scope). Per this cycle's charge, VISION's
discipline is applied instead to the proposal's own procedural/documentation
compliance and the soundness of its §6 governance ruling — the seat's
established catch-class the last several T28 cycles running.*

## Steel-man (≤150 words)

The §6 governance ruling is textually sound, not asserted. I independently
re-grepped LOGBOOK.md's Iteration-65 CHECKPOINT text myself: it reads "...at
BOTH the Predictions section AND the Result section..." — unambiguous, and the
proposal quotes it verbatim rather than paraphrasing. I independently confirmed
the underlying factual claim too: exp-095's and exp-096's own NOTES.md files
both carry the banner at their Idealizations and Predictions sections but
nowhere in their Result sections (`grep` on both files, lines cited match). The
ruling resolves a real two-cycle-old drift at the cheapest possible point —
Phase 1, before Phase 3 drafts the next NOTES.md — rather than deferring a
third time. Every other numeric claim I spot-checked against source (the taper
formula against `lab/fdtd2d.py:160-164`, `TAPER["R3"]=60`/`TAPER["R4"]=80`,
`R3`/`R5` base constants) reproduced exactly. The 300-word narrative cap is
honestly met (independently recounted: 212, matching the proposal's own
figure).

## Sharpest attack (≤150 words)

The ruling fixes nothing by itself — it is a stated intention in a Phase 1
document ("this cycle's own eventual NOTES.md... places the banner at BOTH"),
with no verification step attached. Two independent prior cycles (exp-095,
exp-096) each believed, in real time, that they were complying with this exact
rule and were both wrong — caught only after the fact, at Phase 5, by this
same seat. A bare promise carries no more evidentiary weight than either of
those cycles' own good-faith compliance did. This is precisely the pattern
that produced R18 one cycle ago (a check's claimed scope must get its own
verifying control, not inherited trust) — applied to code there, but this
proposal ships no documentation analog: no Phase-5-mandatory grep-check on the
eventual NOTES.md's Result section is named anywhere in §5–§9. Nothing here
stops a third occurrence — the exact outcome the queue text that spawned this
ruling was written to prevent.

## Verdict: support-with-changes

The substance (Checks 5/6/7, all four fault-injection scenarios, the
governance ruling's own textual reasoning) is sound and independently
verified against source in every case I checked. But §6 discharges only the
*interpretation* question, not the *recurrence* risk, and this cycle is the
one place in the record where naming an explicit verification step costs
nothing and directly targets a two-time-failed discipline.

## Parameter change that would flip verdict to support

Add one sentence to §6 or §9: this cycle's own Phase 3 NOTES.md is not
considered complete until a Phase-5 (or Red Team Phase-2) reviewer explicitly
greps its own Result section for the "governed by Idealizations..." sentence
and reports pass/fail by name — the same "claimed scope must be independently
confirmed against the actual document" discipline R18 already mandates for
code, extended here to this cycle's own governance fix for documentation.
