# exp-062 — Phase 3 Synthesis (Director)

**Panel Iteration 39.** Director resolves Phase 2 into one testable
configuration, states accepted/overridden criticisms, and applies Red
Team's mandatory-fix docket. Predictions are committed to git in
`NOTES.md`, this same commit, BEFORE any Phase 4 search runs (house
discipline, non-negotiable).

---

## 1. Criticisms accepted / overridden

**All Phase-2 criticism is accepted; none is overridden.** Five blind
critiques (PHOTONICS, MATERIALS, THERMODYNAMICS, QUANTUM OPTICS, VISION
SCIENCE), all support-with-changes, and Red Team's audit (PROCEED-WITH-
MANDATORY-FIXES) converge on a proposal that is physically sound at its
core (EM's Airy-stack/passivity analysis, independently re-derived to the
printed digit by Red Team) but under-specified in five places. Red Team's
independent re-verification found the critiques correct, sharpened two of
them with its own tracing (THERMODYNAMICS' `l_geometric_m` dependency;
Idealization/docket item 6, PHOTONICS' declined-item ownership gap), and
added one genuinely new finding (item 6). As Director I accept all seven
mandatory-fix items and the central Checkpoint ruling — see below — with
no override. No seat's criticism is rejected.

**Why no override.** Every attack in `phase2_redteam_audit.md` is
scoped, concrete, and cheap to apply without re-scoping the cycle's EM
lead or returning to Phase 1 — exactly the standard this program applies
before accepting a mandatory-fix docket wholesale (exp-060/061 precedent).
None of the five critiques opposed outright; MATERIALS' conditional
oppose is answered, not argued around. There is no case here for Director
override of a Red Team ruling that a fresh, independently-verifying seat
reached after directly re-deriving every disputed number and tracing
every disputed dependency through source, not merely relaying a critique.

---

## 2. The Checkpoint-4 ruling — Director's disposition

**Accepted, not overridden.** Red Team's Section 3 argument is read in
full and independently checked against the three sites carrying the
tightened `exp061-t18-evidentiary-tier-propagation` tripwire text
(`phase5_redteam_audit.md` §3 from exp-061, `PLAN.md`'s Current-state
"Standing tripwire" paragraph, the live registry entry's own
`description`): all three drop the sibling `exp060-sigma-flat-*` tripwire's
explicit phase-based safe harbor ("surviving into THIS cycle's own
published Phase-3/5 artifact"). The hardened wording instead reads
"discovered at Iteration 39 or later, auto-fires criterion 4, no further
deliberation" — no phase-within-cycle qualifier. VISION SCIENCE's blind
Phase-2 critique found exactly the gap this text was written to catch,
inside Iteration 39, before this synthesis. Per the text's own plain
reading and Red Team's independent confirmation, criterion 4 fires.

**This is a notification, not a pause** (PANEL.md; Iterations 17/36/37/38
direct precedent). A CHECKPOINT entry is filed in `LOGBOOK.md`,
`SESSION_LOG.md`, and `PLAN.md`'s Current-state section (this shift, after
this file commits); Marsh is notified. Unblocked work — this cycle's own
Phase 3/4/5 — continues per the same precedent.

**A house observation, recorded here for future Directors, not a
disagreement with the ruling**: this is now the SECOND time a Phase-2
critique (as opposed to a Phase-5 review, the previous three firings'
timing) has been the discovery site for a criterion-4 firing, and the
first time the firing target is "an old registry entry not yet covering
a not-yet-existing file" rather than a stale claim surviving inside a
frozen document. The mandatory-fix docket (below, item 1) closes the
immediate gap; whether future tightened tripwires should include an
explicit phase-based safe harbor by default, or omit one by default, is a
policy question for Red Team's own future rulings, not resolved here.

---

## 3. Mandatory-fix docket — applied

1. **Registry widened** (this commit, before this file): `lab/
   caveat_lint_config.json`'s `exp061-t18-evidentiary-tier-propagation`
   entry now lists this cycle's `NOTES.md` and `phase4_results.md` in
   `required_sites`; `candidate_globs` (and `lab/caveat_lint.py`'s own
   `DEFAULT_CANDIDATE_GLOBS`) gained a generic `experiments/*/
   phase4_results.md` pattern so this exact structural gap cannot recur
   under a future experiment number. Verified live: `python3 lab/
   caveat_lint.py --only exp061-t18-evidentiary-tier-propagation` now
   correctly FAILs on the two new required sites (they don't exist yet —
   this file and the eventual Phase-4 results file) and will PASS once
   both are written with the T18 disclosure at the verdict itself, per
   the entry's own `phrase_patterns`.
2. **Measurement-geometry query added** to the search plan (query 14,
   below), and EM-3's falsification condition amended in `NOTES.md` §8 to
   state explicitly that an angle-*integrated* broadband reading is NOT
   evidence against the resonant-absorber alternative.
3. **MP-style falsifiable bands attached** to the NiP-black/aerogel query
   set (EM-6/EM-7 below), with Phase-5 review — not this Phase-3 step —
   assigned to render the realizability-tier interpretation, since that
   interpretation is MATERIALS' charter and MATERIALS is not the lead
   seat this cycle; Phase 4 will report the raw findings, scored against
   EM-6/EM-7's bands, and flag explicitly that MATERIALS' own tier
   judgment is owed at Phase 5, not assumed here.
4. **THERMO disclosure added** (`NOTES.md` §9, new Idealization 9):
   covers both THERMODYNAMICS' original point and Red Team's own sharper
   tracing of `l_geometric_m`'s construction.
5. **Direction disclosure added** to EM-5 (near-field-coupling rider):
   `NOTES.md` §7 now asks Phase 4 to report, qualitatively, whether the
   coupled-dipole/local-field-correction literature indicates enhancement
   or suppression of ensemble absorption, or to flag it undecidable from
   available snippets — no new search cost, reusing Section 6's own query
   set.
6. **Item 3 re-filed with an owner**: PLAN.md's Iteration-40+ queue now
   names PHOTONICS' numeric-value-consistency-check tooling gap with an
   explicit owner (PHOTONICS, next rotation slot) rather than leaving it
   as an unowned recommendation — see PLAN.md diff, this shift.
7. **Carried, unchanged, non-blocking**: EM's `sim.omega` historical
   registry entry; THERMO's T25 sidecar-absence entry (bundle-candidate
   with item 4's new registry entry); the standing n_eff=1.04+0.01i
   primary-source pin (query 13 already re-attempts it).

---

## 4. Final configuration for Phase 4

Two co-scored items, as the proposal itself scoped, with the docket's
fixes folded in — see `NOTES.md` for the frozen predictions table (now
EM-1..EM-7) and the final 14-query search plan. No change to the EM-led
scope, no return to Phase 1. Phase 4 executes next: WebSearch only (T18
re-confirmed blocked, standing), scored against the frozen bands.
