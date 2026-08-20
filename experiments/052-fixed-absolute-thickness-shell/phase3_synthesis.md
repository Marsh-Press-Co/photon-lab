# PHASE 3 — SYNTHESIS · Panel Iteration 29 · exp-052

*Director: the cloud panel shift agent. Per PANEL.md, the Director
synthesizes but does not vote in Phase 2, and must state which criticisms
it accepts and which it overrides, and why — in writing, here. The Phase-1
proposal (`phase1_proposal.md`) stands **unedited** as the historical
record, per this program's "flag, don't silently rewrite" convention. This
file, plus the frozen predictions in `NOTES.md` and the accompanying
`design_geometry.py`/`run.py`, is the design Phase 4 executes.*

## 0. What Phase 2 did to this proposal

All five blind seats returned **support-with-changes** — no outright
opposition, but five distinct, independently-verified substantive
concerns, none overlapping. Red Team, going last with everything,
independently re-verified all five against the actual code (not any seat's
prose), ruled all five REAL and LOAD-BEARING (none cosmetic or
overstated), found two additional defects none of the five caught, and
issued **PROCEED-WITH-MANDATORY-FIXES** with a 9-item prioritized docket.

## 1. Ruling on each item (Director, adopting Red Team's audit)

**ACCEPTED, as specified:**

1. **PEC-cored construction for the new object** (ELECTROMAGNETISM →
   Red Team #1, load-bearing). Red Team's own code-level verification is
   decisive: `experiments/030-scale-bridge/run.py::build_ambient`'s
   `"absorber"` branch really does call only `graded_black_shell`, no
   `pec_disk`. Accepted without modification — the exp-031-precedented
   PEC-cored idiom.
4. **Correct the C78 transcription** (Red Team #6b, house rule R4).
   Accepted mechanically — re-derive by import from
   `experiments/030-scale-bridge/design_geometry.py::C78_ESTABLISHED`
   rather than a second hand-copy.
5. **Scope P-3 to 600nm only** (PHOTONICS). Accepted via Red Team's own
   offered cheaper alternative (re-wording over a new run) — the exact
   arithmetic (1.92λ–3.2λ swing) is unambiguous and cheap to state
   honestly rather than expensive to close by measurement this cycle.
6. **Add the absorption e-folding length to §9** (MATERIALS). Accepted,
   desk-only — computed in `design_geometry.py`
   (`ALPHA_PER_NM`/`EFOLD_LENGTH_NM`), not asserted in prose.
8. **Widen P-2's r=312 band** (VISION). Accepted via Red Team's own
   offered cheaper alternative — `P2_R312_BAND = 2×T16's r=156 budget`,
   computed in `design_geometry.py`, not a new floor spot-check.
9. **State the R-gate's evidentiary limits explicitly** (Red Team #7,
   disclosure-only). Accepted, one sentence in `run_rgate()`'s own output
   and NOTES.md's P-4 entry.

**ACCEPTED, with a Director-level redesign (not the literal item):**

2. **Re-measure the self-similar comparator, PEC-cored, at the full
   N9-ambient level** (Red Team, new at Phase 2). Accepted as specified —
   this is a new run (`absorber_selfsim` article in `run.py`), not merely
   a correction to cited numbers, since exp-030's own committed
   `results.json` never has a PEC-cored N9-ambient reading to draw from.
3. **A check that T9's core-incidental null survives at the new object's
   much larger r_in/r_out ratios** (Red Team, new at Phase 2, proposed as
   a `radial_absorbed_power` ledger check). **Director's override, with
   reasons stated:** the literal proposal is replaced with a differently-
   instrumented but equivalently-targeted test — a direct PEC-cored-vs-
   hollow comparison of `C` itself at θ=0, using the already-validated N9
   ambient instrument, rather than `sections.widths()`'s box/ref
   machinery. Reason: `experiments/031-ripple-core-reconciliation/
   run.py::run_thermo` carries a live `NotImplementedError` documenting
   that no validated `box`/`ref` convention exists for a box-ledger
   measurement on this exact scene class (ambient/line-source, θ-swept) —
   attempting one fresh, under this shift's time budget, risked silently
   reproducing that same diagnosed failure mode. The substituted test
   answers the identical scientific question (does core content matter at
   this ratio) using an instrument this cycle already trusts for its
   headline result, at comparable cost (1 extra run vs. 1–2). This is
   disclosed as a redesign, not a silent substitution — see NOTES.md's
   Accepted Fixes item 3 for the full reasoning, reproduced verbatim
   there for anyone auditing this cycle who reads NOTES.md alone.

**ACCEPTED, as a scope limitation rather than new work (Director's call,
stated as such — not a rejection of the concern's validity):**

7. **The coherent-vs-incoherent bridge gate's validity at this cycle's new
   shell fraction (30.8% at r=156)** (QUANTUM OPTICS). Red Team ruled this
   REAL and LOAD-BEARING and did not offer a cheaper alternative the way
   it did for items 5 and 8. **Director's ruling: genuinely open, not
   resolved this cycle.** Re-implementing `experiments/029`'s bespoke
   beam-scene coherent-cross-term measurement correctly for a new
   ambient-scene object, under this shift's remaining time budget, was
   judged higher-risk (of introducing an unvalidated, possibly-wrong new
   instrument under time pressure — exactly the failure mode T11/T22's own
   histories warn against) than disclosing the gap honestly and scoping
   this cycle's own confidence accordingly. This is the one item where the
   Director is NOT closing Red Team's docket in full — stated plainly, not
   smoothed over, per this program's own disclosure standard. Queued
   explicitly as a named follow-up (not competing with the already-LOCKED
   Iteration-30 slot).

**Nothing rejected as unfounded.** Every one of the nine items either lands
as specified, via Red Team's own offered cheaper alternative, or — for item
7 only — is disclosed as a genuine, unresolved scope limitation rather than
either silently accepted or silently dropped.

## 2. The one configuration Phase 4 executes

See `NOTES.md` in full for the frozen hypothesis, setup, idealizations, and
falsifiable predictions P-0 through P-5. See `design_geometry.py` for the
concrete parameter tables and printed-assertion verification, and `run.py`
for the executable design. Predictions are committed to git in this same
batch, **before** `run.py` is ever executed, per house discipline.
