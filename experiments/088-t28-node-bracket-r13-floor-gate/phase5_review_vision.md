# PHASE 5 — REVIEW · VISION SCIENCE · Panel Iteration 65 · exp-088

Fresh context, no memory of any other seat's current-cycle output. Read in
full: LOGBOOK.md's RULED OUT (R1–R13) and T28's LIVE THREADS through
Iteration 64/exp-087 (including my own seat's prior findings there);
PANEL.md; this cycle's complete record — `phase1_proposal.md`, all five
`phase2_critique_*.md`, `phase2_redteam_audit.md`, `phase3_synthesis.md`,
`NOTES.md` (frozen spec + filled-in Result), `run.py`, `results.json`; my
own `phase2_critique_vision.md` and `phase2_redteam_audit.md` §5/§8/§9
item 1's adjudication of it.

## Verdict, up front

**The disclaimer-erosion tripwire FIRES — this is the fourth instance.**
Not in the frozen Predictions section (which correctly carries
Idealizations 9/10 inline at every one of Q1/Q3/Q4/Q5/Q6, exactly per
Red Team's mandatory fix docket item 1). It fires in **NOTES.md's own
Result section, at Q4 — the PRIMARY metric and the sole site of this
cycle's new, unpredicted finding** — where the classification language
("Both angles classify 'C' (CONSISTENT)...") is restated at length with
**zero** occurrence of "Idealization," "NETD," "human-eye," or
"constraint-3" anywhere in that paragraph.

## What I independently verified

I did not trust NOTES.md's own prose. I read `results.json` directly.

- `frac_p_abs`: 38.4°=`0.0013041389697994702`, 38.8°=`0.005955237665824989`
  — matches NOTES.md's cited `1.304×10⁻³`/`5.955×10⁻³` exactly.
- `frac_contrast_new_angles`: 38.4°=`0.0014370491250264455`,
  38.8°=`0.001537528237042816` — matches `1.437×10⁻³`/`1.538×10⁻³`.
- `ratio_k_new_angles`: 38.4°=`0.9075117524430284`,
  38.8°=`3.873254176638027` — matches `0.908`/`3.873` exactly.
- `q4_predictions_check`: `{"theta_38_4_in_band": false, "theta_38_8_in_band":
  true}` — matches NOTES.md's "NO"/"yes" cells exactly.
- `retroactive_exp087_reclassification` and `q5_all_resolved_ratios =
  [2.6423677612294223, 5.710203290428644, 0.9075117524430284,
  3.873254176638027]` — matches Q1/Q5's cited figures exactly.
- **Critical finding**: `results.json` itself carries two top-level fields,
  `"netd_disclaimer"` and `"scope_note"`, stating Idealization 9/10
  verbatim ("NETD is an instrument/detector threshold, not a human
  perceptual one... does NOT bear on constraint-3/4's human-eye verdict";
  "This cross-check bears only on T28's own confound-mechanism question
  and constraint-3's energy-ledger bookkeeping..."), plus a per-cell
  `netd_disclaimer` string repeated at all four thermo cells. **The
  disclaimer is present in the raw data. It is not carried into NOTES.md's
  own Q4 Result prose.** This is, structurally, the exact same gap
  Iteration 64's LOGBOOK entry used to describe the third instance:
  "NETD/constraint-3 language present in `results.json` but not carried
  inline at... NOTES.md prose restatements." It has recurred, inside this
  very cycle's own document, in the one place — Q1/Q5/Q6's Result
  paragraphs — the cycle had just finished proving it knows how to avoid.

No arithmetic or citation defect found anywhere in this cycle's Result
section. Every number I could independently check reproduces exactly.
The defect is a carry-forward omission, not a wrong number.

## Sharpest finding

**NOTES.md's own Result section is inconsistent within itself: Q1, Q5,
and Q6 all correctly carry Idealizations 9/10 inline (Q6 verbatim,
"NETD is an instrument/detector threshold, not a human perceptual
one..."; Q1 and Q5 both cite "(Idealizations 9-10)" explicitly), but Q4
— the PRIMARY result, and the only place this cycle's genuinely new,
unpredicted finding (the non-monotonic `frac_p_abs` dip at 38.4°, where
`ratio_k=0.908` falls *below* even the 36.0° anchor value the linear
interpolation was built from) is written up — carries neither disclaimer
anywhere in its ~500-word discussion.** This is precisely the
Director-flagged risk: not a hypothetical, but a real, present-tense
demonstration that the disclaimers "silently drop out again once real
numbers arrived" — in the single section of the document a future
LOGBOOK/PLAN.md citation is most likely to quote (it is the PRIMARY
metric and the cycle's only surprise). Red Team's own Phase-2 mandatory
fix (item 1, BLOCKING, explicitly Checkpoint-4-relevant) named the
requirement as carrying the disclaimers "at every restatement of the
P7/Q1/**Q4**/Q5 classification language... in Phase 3's synthesis and
**the eventual NOTES.md**" — Q4 is named explicitly, and "the eventual
NOTES.md" unambiguously includes the Result section that did not exist
yet when that fix was written. The fix was delivered in the document's
frozen Predictions half and dropped in its own Result half, inside one
document, one cycle, immediately after being warned about the exact
failure mode by three prior LOGBOOK entries, this cycle's own Phase-2
critique (mine), and Red Team's own audit.

Iteration 64's close was explicit and unconditional about the
consequence: *"a fourth instance fires Checkpoint criterion 4
automatically."* Unlike the third instance (caught in a Phase-1 draft,
correctable before any data existed, legitimately closed same-shift as
non-firing), this fourth instance sits in the frozen, results-filled
NOTES.md — the permanent experimental record — and was not caught by
Phase 2, Red Team's Phase-2 audit, or Phase 3 (none of which could see
it; it did not exist until Phase 4 filled in the Result section). It is
being caught now, at Phase 5, by this seat, exactly as the third instance
was. The whole point of Iteration 64's harder, "no further deliberation"
language — deliberately stricter than R6–R12's ordinary "caught blind,
same cycle" discharge pattern — was to close the loophole of an
indefinitely-recurring defect that keeps getting fixed just in time and
therefore never actually stops. Ruling this one non-firing on the grounds
that it, too, was "caught blind, same cycle" would erase the distinction
Iteration 64 explicitly built the tripwire to enforce.

**I recommend the Director treat this as a firing of Checkpoint criterion
4** — a CHECKPOINT entry in LOGBOOK.md and SESSION_LOG.md, Marsh notified,
per PANEL.md's continuous-mode protocol — even though the textual fix
itself (adding one sentence to Q4's Result paragraph, mirroring Q6's own
already-correct wording) costs nothing and should also be applied
same-shift regardless of the Checkpoint ruling.

## Secondary, non-blocking finding

Q4's Result prose calls the 38.4° dip "a real, **well-resolved** reading
(it clears the box-dev noise floor with margin, `resolved=True`... not a
noise-floor artifact)." `resolved` here is inherited, correctly, from the
gate's own statistical/instrument sense (SNR above `box_dev`'s noise
floor) — not a human-visual-resolution claim, and I found no place this
cycle uses "resolved" to mean anything else. But this is exactly the kind
of perceptually-loaded vocabulary this sub-thread has been burned by
before (exp-087's own "localized Weber contrast" mislabel, flagged at my
own seat's Phase-2 critique this cycle). A one-clause gloss ("resolved in
the box-dev/instrument sense, not a claim about human visual resolution")
would close the ambiguity at zero cost. Not blocking — the surrounding
sentence and Idealization 9 (when restored to this paragraph) already
supply enough context that a careful reader would not misread it, but a
future skimmer quoting only "a real, well-resolved reading" out of
context could.

Separately: the new dip finding itself is written up cleanly with respect
to my own charter's central question (what would make a human eye FAIL to
register something physically present) — it never claims or implies
anything about ambient appearance, Weber contrast, or perceptibility. The
gap is entirely about the missing disclaimer stating that explicitly,
not about any language overreaching into a perceptibility claim.

## Ranked top-3 for the Director's Iteration-66 queue

1. **Immediate, same-shift, zero-cost**: add the Idealization 9/10
   disclaimer sentence to NOTES.md's Q4 Result paragraph, matching Q6's
   own already-correct wording verbatim, and add the one-clause
   "resolved-in-the-instrument-sense" gloss noted above. This is the fix
   that discharges the tripwire going forward; it does not undo the fact
   that it fired.
2. **Structural, not textual** (Red Team's own §5 recommendation,
   escalated by this finding from "strong recommendation" to warranted):
   adopt a "carried idealizations" banner as a **mandatory, machine- or
   checklist-verifiable requirement at both the Predictions section AND
   the Result section** of any future T28 NOTES.md — this cycle is
   direct, first-hand proof that a banner scoped only to "every
   prediction below" (as this cycle's own banner literally read) does not
   propagate to the Result section filled in after Phase 4, precisely the
   gap that just fired. A single banner instance is not enough; the
   discipline needs to survive the transition from pre-registered
   prediction to reported result, which is exactly where this defect keeps
   recurring.
3. **The named forward-tripwire itself** (already correctly logged in
   NOTES.md's own Next section, not new to this review, but worth keeping
   at the top of the queue): measure `ratio_k` by real FDTD at the three
   other node-adjacent established-grid angles (≈37.1°/37.2°, 40.2°,
   41.4°) before any future LOGBOOK/PLAN.md entry describes the
   energy-interception channel as CONSISTENT in a channel-general sense —
   PHOTONICS' and Red Team's own §6.2 finding this cycle, independently
   confirmed sound by my own reading; only 1 of 4 known `delta_scene`
   zero-crossings has ever had `ratio_k` measured near it.
