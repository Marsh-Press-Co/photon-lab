# PHASE 2 — CRITIQUE · VISION SCIENCE (blind) · Panel Iteration 63 · exp-086

*Fresh context. Read PANEL.md in full; LOGBOOK.md lines 1–380 (RULED OUT,
esp. R6–R11) and the T28 sub-thread (LIVE THREADS, Iterations 46–62 in
full, including both Iteration-52/54 CHECKPOINT entries and the
Iteration-61 CHECKPOINT); `experiments/085-.../phase5_redteam_audit.md` in
full; `experiments/086-.../phase1_proposal.md` under review. Not shown any
other seat's current-cycle critique.*

## Steel-man (≤150 words)

This is careful, well-scoped instrument-repair work, not a rubber-stamp
re-run. It correctly locates BOTH files carrying the identical
`chosen`-selection bug and, unlike a lazier repair, traces which copy
`phase4_derivation.py` actually imports (`y_wall_prescreen.py`'s copy, via
`phase1_derivation.py`'s loader chain) rather than assuming. It finds a
genuine subtlety the audit's own hand-count missed: `θc=45°` is a
confirmed all-stage-boundary artifact whose as-filed period happens to sit
under the 6°-width proxy filter by coincidence, so a flag-based
(`converged==True`) criterion — not the audit's period-width proxy alone —
is required for a complete correction, yielding a disclosed 21/37-vs-22/37
uncertainty band instead of false precision. The cosmetic-fix docket item
is handled completely: both the `phase4_derivation.py` print-statement
mislabel AND the `NOTES.md` "62.8%" citation are independently named and
recomputed to 91.6%, not just one of the two audit-flagged halves.

## Sharpest attack (≤150 words)

Prediction (2) — the load-bearing headline — states flatly "predict NOT
STABLY PERIODIC" with no restatement of exp-085's own audit's carefully
earned caveat (§2/§5 of `phase5_redteam_audit.md`): that this label is a
statement about what *this instrument* can currently certify, explicitly
**not** a claim that no near-normal-quarter periodicity exists — a
distinction the audit spent a full paragraph establishing. I grepped the
complete proposal: "instrument," "certif," "foreclose," "reliability"
appear nowhere attached to prediction (2); the nearest related text
(prediction 3) is scoped only to the Spearman-significance question, not
the headline classification. Nothing in §4's frozen predictions or §6's
Phase-4 plan commits the eventual `NOTES.md` to carrying that caveat
forward — it only specifies "report the result under the label this
audit's §5 verdict specifies." Given this exact sub-thread's own T16
precedent (a caveated finding hardening into a bare, overclaimed fact one
cycle later, caught only by a fresh seat), this is precisely the failure
mode to pre-empt before, not after, Phase 4 writes the label down.

## Verdict

**Support-with-changes.**

## Single change that would flip to unconditional support

Add an explicit, pre-registered requirement (§4 prediction (2) or §6) that
Phase 4's `NOTES.md` and any `classification_a` headline must restate the
audit's own instrument-reliability caveat — verbatim or materially
equivalent to "a statement about what this cycle's own instrument can
currently certify, not a claim that no periodicity exists" — every place
"NOT STABLY PERIODIC" is reported, not merely emit the bare label the
existing decision code produces.
