# PHASE 5 — REVIEW · VISION SCIENCE (blind) · Panel Iteration 63 · exp-086

*Fresh context. Read PANEL.md in full; LOGBOOK.md lines 1–380 (RULED OUT,
esp. R6–R11) and lines 426–4117 (LIVE THREADS, T28 sub-thread in full);
the complete exp-086 record (`phase1_proposal.md`, all five Phase-2
critiques including my own, `phase2_redteam_audit.md`, `phase3_synthesis.md`,
both Phase-4 scripts + results for the rescore/null-calibration/
prior-citation legs, `NOTES.md`). Not shown any other seat's current-cycle
Phase-5 review.*

## 1. Did the instrument-reliability caveat actually carry forward?

**Yes — confirmed, and correctly attached, not merely present.** I raised
this at this cycle's own Phase 2 (`phase2_critique_vision.md`): the frozen
Prediction (2) text as originally drafted stated "predict NOT STABLY
PERIODIC" with no restatement of exp-085's own audit caveat, and nothing in
§4/§6 of the Phase-1 proposal *committed* Phase 4 to carrying it forward.
Red Team's Phase-2 audit independently confirmed the omission by direct grep
(§1, "VISION's omission claim... CONFIRM, exactly") and folded it into
mandatory fix 4, which `phase3_synthesis.md` §2 item 4 accepted in full.

Grepping the shipped `NOTES.md`: the caveat appears twice, and both times
it is bound to the specific line reporting `classification_a`, not floated
elsewhere in the document as generic hedging:

- Predictions §3: `` `classification_a` = **NOT STABLY PERIODIC** — carrying
  forward, every place this label is reported, exp-085's own
  instrument-reliability caveat: a statement about what this doubly-corrected
  instrument can currently certify, NOT a claim that no near-normal-quarter
  periodicity exists.``
- Result: `` `classification_a = NOT STABLY PERIODIC` (`frac_recovered<0.80`
  gate, first branch). Caveat carried per fix 4: this is a statement about
  what this doubly-corrected instrument can currently certify, not a claim
  that no near-normal-quarter periodicity exists.``

Both instances sit in the same sentence/bullet as the label itself, not in
a separated caveats section a reader (or a future LOGBOOK-writing seat)
could clip off independently of the classification. This closes the finding
I raised — the fix was not merely accepted on paper, it shipped.

## 2. Prediction 6 ("negligible" / "cleaner than the frozen prediction
anticipated") — is the characterization fully earned?

**Mostly earned for the narrow claim actually tested; the prose over-widens
it once, in a way that echoes — faintly, not as badly — the T16
caveat-erosion shape.**

**What is well-earned.** The literal numeric claim — "`max_r2_over_trials`
and `p_r2_ge_070` are IDENTICAL... between the old buggy and corrected quiet
function" — reproduces exactly against
`phase4_null_calibration_controlled_comparison_results.json`:
`old_buggy.max_r2_over_trials = 0.5179691995509128` and
`corrected.max_r2_over_trials = 0.5179691995509128` are the *same float to
full precision* (not merely "4 decimal places," the script's own conclusion
undersells its own result), and both `p_r2_ge_070` values are `0.0`. The
mechanism given for why — boundary-pinned trials (6.70%, 201/3000) never
approach the max, which is set by trials that already found a genuine
non-boundary optimum — is stated, checkable, and consistent with the data.
The "wrong test, corrected mid-cycle" framing (recognizing that `max` is an
order statistic and a raw N=3000-vs-N=20000 diff confounds fix-effect with
sample-size effect) is itself good, disclosed methodology, not glossed over.
So: for **the one real signal actually re-tested (`pair_pad`)**, "negligible
effect of the fix, at matched N/seed" is fully earned by the cited numbers.

**Where the prose over-widens.** The re-run script's own top-of-file comment
(`phase4_null_calibration_rerun.py`, lines 54–58) states explicitly: *"Only
pair_pad: exp-077's own committed `null_calibration_appendix` is a single
top-level key, computed once against `real_delta_pad`, not per-pair.
Re-running an appendix for `pair_absorb40` would be new scope..."* — i.e.
neither exp-077's original appendix nor this cycle's re-run and controlled
comparison ever touched `pair_absorb40`'s own noise floor. That scoping is
legitimate (it matches original scope exactly, and `phase3_synthesis.md`'s
own clarifying note already establishes `null_calibration_appendix` isn't
REFUTE's evidentiary basis anyway) — but it is stated **only inside the
Python source comment**, never restated in `NOTES.md` itself. `NOTES.md`'s
Learned section instead generalizes: *"the boundary-pinning bug... has
negligible effect on the specific statistics that underwrite 'the real
oscillation is not noise'"* — singular, unqualified "the real oscillation,"
immediately after a Result section that itself cites **both** real R² values
(0.8165 pair_pad, 0.7156 pair_absorb40) as the numbers this leg's noise
ceiling is being checked against. A reader of `NOTES.md` alone — without
opening the script — would reasonably read "the real oscillation" as
covering exp-077's REFUTE citation family broadly (`pair_pad`,
`two_wall_pair_pad`, `two_wall_pair_absorb40`), when only `pair_pad`'s own
null was ever recomputed here, at either N. The pre-registered falsifier
itself uses `pair_absorb40`'s R² (0.7156) as a threshold against a noise
ceiling measured only on `pair_pad`'s sigma — a cross-pair reuse of a null
distribution that is never verified as commensurable between the two real
channels (the R9 concern: same units, unconfirmed cross-applicability).
This is not a broken number — nothing here is arithmetically wrong, and
unlike the original T16 episode nothing downstream currently depends on the
distinction (Prediction 6 is Tier-2/informational, not a verdict this cycle
scores against) — but it is exactly the shape R9/T16 exists to catch: a
scope qualifier that lives in the machinery and gets silently generalized
one level up in the prose that a future cycle or LOGBOOK entry is more
likely to read and re-cite verbatim. **Recommend**: before this Prediction-6
finding is cited again (Next-section item 1, or any future LOGBOOK entry),
add one clause naming the `pair_pad`-only scope explicitly in `NOTES.md`'s
own prose, not only in the script comment.

## 3. "Now ELEVEN consecutive cycles deferred, 076–086" — independent check

**Confirmed correct, arithmetically and against LOGBOOK's own citation
trail.** LOGBOOK.md line 4108 (Iteration 62 / exp-085's own entry) states:
*"the x-wall wavelength-generality leg, now **TEN** consecutive cycles
deferred, 076–085"* — `085 − 076 + 1 = 10`, checks out. The chain of prior
citations is internally consistent at every step I could grep: "FIVE...
076–080" (`080−076+1=5`), "SIX," "SEVEN," "EIGHT," "NINE," "TEN...076–085" —
one increment per iteration, no skips or double-counts. exp-086
(Iteration 63) is a zero-FDTD instrument-repair/re-score desk cycle by its
own explicit scope statement (`phase1_proposal.md` §1, §3: "Checkpoint
criterion 2 is N/A... no absorption mechanism is proposed") and touches
nothing wavelength-related — the x-wall wavelength-generality leg is absent
from every fix item (1)–(6) in the parameter table and from the Phase-3
synthesis's disposition. It is therefore correctly deferred again this
cycle, and `086 − 076 + 1 = 11` reproduces `NOTES.md`'s own "ELEVEN...
076–086" exactly. No erosion or arithmetic drift found here.

## Verdict

**PARTIAL.** This cycle does exactly what it set out to do — instrument
repair, not phenomenon work (Checkpoint criterion 2 correctly N/A) — and
does it with real discipline: three independent reproductions of the
corrected `frac_recovered`/classification, a genuine methodological
self-correction on Prediction 6 (recognizing and fixing an invalid
mismatched-N comparison openly), and the specific caveat-carrying
requirement I raised at Phase 2 shipped correctly, attached to the
classification itself. It is PARTIAL rather than PROMISING because (a) it
is bookkeeping/hygiene work, not new evidence about the phenomenon, by its
own stated scope, and (b) my own §2 finding above — a real scope caveat
(pair_pad-only) present in code but not in the NOTES.md prose that will be
read and re-cited — should not ship into a permanent LOGBOOK entry
unaddressed, on this program's own R9/T16 precedent. Not RULED OUT: nothing
here fails a gate, and the R11 machinery fix itself is confirmed correct
and load-bearing for the whole T28 board going forward.

## Ranked top candidate next steps (T28 sub-thread; none re-propose R1–R11)

1. **Add the `pair_pad`-only scope clause to `NOTES.md` before this cycle's
   LOGBOOK entry is written** (my own §2 finding). Cheapest possible fix —
   one sentence — and forecloses a T16/R9-shaped erosion before, not after,
   it hardens into permanent record. Should happen this cycle, not be
   queued.
2. **The joint EM/THERMO energy-interception cross-check**, now four
   consecutive cycles deferred/exempt (083/084/085/086) per `NOTES.md`'s own
   Next section — this is the item closest to R6–R10's "known, named,
   ignored" escalation shape if a fifth scene-bearing cycle defers it again
   without comment.
3. **PHOTONICS' grazing-incidence model-validity question** (does
   `edge_diffraction_c_empty_corrected` stay inside its own valid near-field
   regime at the ~5,444×–6,631× `ptp`-growth sub-windows?) — disclosed, not
   resolved, this cycle; directly bears on whether the corrected Method C
   fits at the extreme sub-windows are physically meaningful at all, prior
   to any further statistics being built on them.
4. **The full-scale (60,001-call) `null_calibration_appendix` re-run**,
   substantially de-risked in urgency by this cycle's own controlled
   N=3000 comparison but still queued — lower priority than items 1–3 since
   the matched-N test already isolated the fix's own effect as null.
