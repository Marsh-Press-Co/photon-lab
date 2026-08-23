# Phase 5 — VISION SCIENCE blind review (exp-061 / Iteration 38)

*Fresh sub-agent, blind to the other five Phase-5 reviews and to Red
Team.*

**Verdict: PROMISING** (support-with-changes on the record; the tooling
defect below is real but not disqualifying).

## T1 escape route check
Confirmed clean throughout NOTES.md, phase4_results.md, and phase1/
phase3 — every MP row and the THERMO disposition explicitly states "T1
escape route: NONE" or equivalent, and nothing scores a
constraint-1/2/3/4 metric. Holds.

## Smuggled-perceptual-claim check (my charter)
Ran a full grep across the experiment directory for
`invisib|human eye|to the eye|looks black|appears black|perceiv|blackness`.
Every hit is either the Phase-2 critique's own text or "(near-total)
blackness" used as the field's own radiometric term of art (reflectance
≤0.05%, a term the CNT-forest/Vantablack literature itself uses), always
paired with a bare percentage or OD figure. No instance frames it as
"invisible to a human eye," "looks black," or otherwise invokes
constraint-3 apparatus. **Clean — no defect here.**

## T18-propagation fix: partially holds, one real regression

1. **NOTES.md's own Result section (the actual Phase-4 verdict bullets)
   does NOT carry the disclosure at each MP verdict.** Only the
   Predictions table (pre-run, MP-3/MP-4 rows) and one closing summary
   sentence AFTER all five bullets state it. That closing sentence's own
   claim — "every verdict above discloses its evidentiary tier... at the
   verdict itself" — is NOT literally true for MP-1, MP-2, MP-3, or
   MP-5's own verdict bullets; only the trailing paragraph carries it,
   which is structurally the same "stated once, elsewhere" pattern the
   Phase-2 critique flagged, just relocated to the bottom instead of the
   top. **[MODERATE — mischaracterization of its own compliance, inside
   the very document introducing the registry entry.]**
2. **phase4_results.md does it properly for MP-3, MP-4, MP-5** (inline,
   "adjacent to the verdict itself" as required) but **MP-2's own
   verdict has no inline restatement** — it relies on the document-header
   disclosure two sections above. **[MINOR — one of five verdicts
   under-covered, but the file-level header is close enough that a
   reader can't miss it.]**
3. **The registry entry itself never checks phase4_results.md at all.**
   `required_sites` = `[NOTES.md]` only; `candidate_globs` = `[LOGBOOK.md,
   PLAN.md, experiments/*/NOTES.md, .../REALIZABILITY_MEMO.md]` — none of
   which glob-match `phase4_results.md`. Confirmed live: running the full
   registry produces zero WARN mentioning `phase4_results.md`, and an
   ad-hoc check run by hand is the only reason the file's own compliance
   got checked at all this cycle. **This is exactly the failure-mode
   class flagged at Phase 2 — an un-registered site — recurring in a NEW
   file the tool was never pointed at, not fixed by the entry that
   claims to fix it.** **[MAJOR — the propagation-check tool's registry
   entry for T18 propagation doesn't cover the file where T18-sourced
   verdicts are actually rendered in full, and would silently miss a
   future regression there.]**

## Caveat-lint tool grading (this seat's own 8-cycle-deferred idea)
Ran `caveat_lint.py`, `--selftest`, and an ad-hoc check — all behave
exactly as documented (5 caveats, 0 required-site failures; selftest
correctly discriminates d5b4844/4f29982). The mechanism itself is sound
and genuinely useful — real infrastructure, not another prose promise.
But its own design has a structural ceiling this seat's Phase-2 critique
already named and this cycle re-demonstrates: it checks FILE-LEVEL
PRESENCE, not LOCATION-WITHIN-FILE or REGISTRY COMPLETENESS. It cannot
itself flag "you forgot to add a required_site" (defect #3 above) or
"the phrase exists in the file but not adjacent to the verdict" (defect
#1) — both require a human to notice, same as before the tool existed.
**Grade: B — real, working, non-trivial infrastructure; genuinely
better than 8 cycles of hand patches; but it still only catches gaps a
Director remembered to register, exactly the limitation this seat's own
Iteration-15 ask hoped to eliminate and Idealization 7 candidly admits
was not fully closed.**

## Ranked top-3 candidates for Iteration 39
1. **Close the phase4_results.md registry gap directly** — add
   `phase4_results.md` to entry
   `exp061-t18-evidentiary-tier-propagation`'s `required_sites`, and fix
   MP-1/MP-2/MP-3/MP-5's bullets in NOTES.md's Result section to each
   inline the T18 tag (not just the closing paragraph). Cheap,
   mechanical, closes a live defect this review found.
2. **PHOTONICS' queued numeric-value-consistency tooling gap** — the
   `TAU_SHELL=24` unreconciled-for-two-cycles precedent is the same
   class of bug as #1 above (a claim drifts from its source unnoticed);
   worth prioritizing given this cycle's own near-recurrence.
3. **Primary-source-verified recheck of n_eff=1.04+0.01i** — MP-1's
   strongest in-band data point is currently un-pinnable to a title;
   still T18-blocked, but worth a standing watch for when/if the
   WebFetch block lifts, since it's load-bearing for the one figure that
   came closest to the corrected target.
