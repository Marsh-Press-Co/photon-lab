# PHASE 5 — REVIEW · VISION SCIENCE · Panel Iteration 69 · exp-092

Fresh context, no memory of any prior cycle beyond what is written down.
Read in full: `PANEL.md`; `LOGBOOK.md` (RULED OUT R1–R15; LIVE THREADS
T1–T28 through Iteration 68/exp-091, including every disclaimer-erosion
Checkpoint-4 episode — Iteration 53/T16, Iteration 63/exp-086, Iteration
64/exp-087, Iteration 65/exp-088 [FIRED, escalated dual-section-banner
rule adopted], plus the Iteration 66/exp-089 and Iteration 67/exp-090
near-misses ruled non-firing on reasoned grounds, and exp-091's own
Phase-5 finding — `netd_disclaimer`/`scope_note` written to `results.json`
but never `print()`-ed to `run_output.txt`, ruled a new, distinct gap
shape, non-firing, with a named structural fix recommended). Blind to
every other seat's exp-092 Phase-5 output, per instruction. Did not open
`phase2_critique_{photonics,materials,thermodynamics,quantum}.md` (out of
scope for this review) but did read my own `phase2_critique_vision.md`
verbatim, as instructed, since it frames both items 1–2 below.

## Verdict, up front

**CONCUR-WITH-GAP.** Every scientific number I independently re-derived
reproduces exactly, and both mandatory fixes carried out of my own
Phase-2 critique landed cleanly — the cleanest disclaimer/idealization
record this T28 sub-thread has produced since the Iteration-65 CHECKPOINT.
But `NOTES.md` ships with a genuinely new record-hygiene defect this
document has never had a chance to be checked for before now: duplicate,
self-contradicting `## Learned`/`## Next` section pairs, the second an
unedited Phase-3 placeholder stub left standing after real content was
inserted above it. Non-load-bearing to any measurement, but exactly the
species of defect a future citation could trip over.

## What I independently verified

- **Print-parity fix (my own top Phase-2 ask): FIXED, confirmed by direct
  grep of both sides.** `run.py` lines 628–630 `print()` all three
  disclaimer strings (`netd_disclaimer`, `scope_note`, and this cycle's
  new `sigma_branch_disclaimer`). `run_output.txt` lines 131–133 carry
  them **verbatim**, word-for-word identical to the strings defined at
  `run.py` lines 606–612 and to `results.json`'s own values. This closes
  exp-091's own Phase-5 finding (a `print()` call that was never
  authored) on the exact surface it was found missing from, one cycle
  later, as recommended.
- **exp-091's Idealization 8 (my own sharpest Phase-2 attack): RESTORED,
  confirmed present and correctly attributed.** `NOTES.md` Idealization 8
  reads: "No full R3-rescaled rebuild of exp-083's 31-point window, and no
  extension of R14(b)'s still-queued formal null-controlled period fit —
  both remain open, separate, standing T28 items (exp-091's own
  Idealization 8, restored here after `phase1_proposal.md`'s silent drop
  — VISION's Phase-2 finding, upheld by Red Team)." Both halves of my
  Phase-2 "parameter change that would flip my verdict" request (Add
  Idealization 8; fix the `print()` gap) are independently confirmed
  landed — `phase3_synthesis.md` §3 items 6–7 record the same disposition
  in the Director's own words.
- **Predictions-section vs. Result-section carried-idealizations banner:
  word-for-word number match, content-checked against `NOTES.md`'s own
  ten-item Idealizations list.** Predictions (§ line 128): "governed by
  Idealizations 3/6/7/11." Result (§ line 263): "governed by
  Idealizations 3/6/7/11." I checked each of the four numbers against its
  own listed content, not merely that the digit-strings match: 3 = "NETD
  is not a human-eye threshold" (correct, both sections use it that way);
  6 = "`FLOOR`/`RMS[frac_contrast]` applied, not recomputed" (correct,
  both sections say this); 7 = "does not test constraints 1/2/3/4... T1
  N/A" (correct in both); 11 = "a Rank-3 REFUTE/NEITHER-default reopens
  Rank 1's net-placement logic" — the Result section correctly updates
  this to its now-resolved, moot state ("moot this cycle, since Rank 3
  CONFIRMed") rather than silently dropping it or restating the
  conditional as if still live. This is the second consecutive T28 cycle
  (after exp-091's own same-shift fix) to carry the escalated Iteration-65
  dual-section banner rule cleanly through both mandated locations, this
  time from a clean Phase-1 draft rather than a same-shift repair.
- **Numeric spot-check, independent of the brief.** Re-derived
  `delta_scene`/`frac_contrast`/`ratio_k`/`classification`/`floor_pass`
  for all 7 Rank-1 angles directly from `results.json::rank1.per_theta`
  and confirmed every value `NOTES.md`'s (R1c) paragraph cites
  (39.4°→ENERGY-DECOUPLED at `ratio_k=0.0762`; 40.0°→ENERGY-DOMINANT at
  `ratio_k=18.89`; 41.8°/42.0°→both NODE-UNRESOLVABLE, `floor_pass=False`)
  reproduces bit-exact. Confirmed the two crossing locations
  (`40.07184°`, `41.78107°`/`41.83765°`) and both comparator tables in
  (R1b) match `run_output.txt`'s own printed `[R1b diagnostic]` JSON
  exactly. No arithmetic defect found anywhere in the scored record.

## Findings

**1. (Confirmed fixed) Print-parity gap closed** — see above. No further
action needed; recommend this remain a permanent `run.py` convention for
any future `_disclaimer`/`_note` key, not something re-litigated per
cycle.

**2. (Confirmed fixed) exp-091's Idealization 8 restored** — see above.
No further action needed.

**3. (Confirmed clean) Dual-section banner citation is correct, content
and numbers, in both mandated locations.** No erosion found. This is the
first T28 Phase-1 draft since the Iteration-65 CHECKPOINT to land the
escalated rule correctly on the first attempt rather than needing a
same-shift Phase-2 or Phase-5 repair (exp-088 fired the CHECKPOINT;
exp-089/090 needed reasoned non-firing rulings; exp-091 needed a same-shift
Phase-5 fix). Worth naming explicitly as the escalated rule visibly
working as intended, three cycles running.

**4. (NEW, previously uncheckable) `NOTES.md` carries duplicate,
contradictory `## Learned` and `## Next` sections.** Traced via `git show`
on the two commits that built this file:

- `d72df83` (Phase 3, frozen before any run) ends with template
  placeholders: `## Result` / `*(To be written after Phase 4...)*`,
  `## Learned` / `*(To be written after Phase 5.)*`, `## Next` /
  `*(To be written after Phase 5 — see the reconciled Iteration-70
  queue.)*` — correct and expected at that stage.
- `989a4a4` (Phase 4 close-out) replaces **only** the `## Result`
  placeholder with real content, then appends its own new, fully-populated
  `## Learned` (4 items) and `## Next` (4-item ranked queue) sections —
  but never deletes the original placeholder pair below them. The diff
  shows the insertion landing entirely above the untouched trailing
  `## Learned`/`## Next` stub.

The result, present in the file today (verified by direct `grep -n`, two
hits each): `NOTES.md` lines 386–451 carry the real, substantive
Learned/Next content; lines 453–459 are a **second**, still-unedited
`## Learned` / `## Next` pair reading verbatim "*(To be written after
Phase 5.)*" and "*(To be written after Phase 5 — see the reconciled
Iteration-70 queue.)*" — language that was already false the moment the
real sections above it were written, and is more obviously false now,
mid-Phase-5, with six real reviews about to cite this document. This
happened *after* my own Phase-2 critique (which only had the Predictions/
Idealizations sections to check) and is the first Phase-5 layer this
specific document has had — this is genuinely new, not a recurrence I or
anyone else could have caught earlier.

This is **not** the same mechanism as the R6–R15 caveat-carry-forward
lineage (nothing here is a scope-limiting qualifier failing to propagate
between two prose restatements of a finding) — it is leftover Phase-3
boilerplate that a same-shift insertion failed to clear. But it is squarely
this seat's charge on record-hygiene grounds: a `NOTES.md` whose own house
format promises one hypothesis/setup/result/learned/next document now
contains two mutually contradicting Learned sections and two mutually
contradicting Next sections, and a future reader or script grepping for
`## Learned` without checking for a second match could silently quote the
dead placeholder, or a future editor filling in "the" Next section post-
Phase-5 could append the Iteration-70 queue reconciliation under the wrong
(stale) header and strand it below the real content. **Non-load-bearing to
any number in this cycle's record** — every scored quantity above and
below the seam reproduces bit-exact from `results.json`/`run_output.txt`,
independently re-verified in this review. **Recommended fix, same-shift,
near-zero cost**: delete `NOTES.md` lines 453–460 (the stale duplicate
pair), leaving the single already-correct Learned/Next section in place.

**5. Assessed from this seat's own competence: the newly-discovered
upper-window double-crossing near-null structure correctly has NO bearing
on constraint-3/4, and the write-up does not smuggle any such claim.**
Traced `delta_scene`/`frac_contrast` to their source definition
(`run.py` line 215: `delta_scene = g_cell["C"] - c_cell["C"]`) —
this is a **difference between two separate hypothetical article
geometries' own scene contrast** (`G40` minus `C40`), not a single real
scene's contrast against ambient background as a human eye would actually
view it. Its zero-crossings mark angles where two *different* constructed
geometries happen to read numerically equal, which is a property of the
differencing construction (the same fragility class R14 names for
numerator hazards generally), not a statement about any one scene's
absolute, eye-relevant Weber contrast. A human observer sweeping a
flashlight does not perceive `delta_scene`; nothing in `lab/ambient.py`'s
own photopic/scotopic Weber-contrast machinery (stage 9, the actual
constraint-3 instrument) is invoked anywhere in this cycle's `run.py`. I
grepped the full `NOTES.md` for "eye"/"visib"/"ambient"/"photopic"/
"scotopic"/"glare" and confirmed every hit sits inside the disclaimer
language itself (Idealization 3, the two banner instances) — no result
prose anywhere states or implies a perceptual reading of the double-
crossing null. The write-up's own scoping (Idealizations 3/7, "does not
test constraint 1/2/3/4") is correct here, not merely asserted. One
forward caution, not a defect in this cycle: if a future cycle is tempted
to treat this near-null angular region as a natural candidate for an
actual constraint-3 ambient-appearance run (i.e., "interesting because a
diagnostic differential goes near zero here"), that inference does not
follow — a near-null in a two-config *difference* channel does not predict
where a single real geometry's *absolute* contrast against ambient would
also be near-threshold, and any such future proposal would need its own,
freshly-argued case, not a citation to this cycle's finding as if it were
already evidence of perceptual relevance.

## Governance observation (not a new rule, extending Iteration 61's still-
unresolved question with independent testimony)

This is Iteration 69 of a T28 desk/instrument sub-thread that has run
continuously, with T1 route N/A and Checkpoint criterion 2 N/A stated
every single cycle, since Iteration 46/exp-069 — 24 consecutive iterations
in which my seat's own founding charter duty ("pin numeric thresholds…
BEFORE any run that scores against them") has had structurally nothing to
score against, because no cycle in this span has run an ambient-appearance
measurement. The internal rigor of this work is genuinely excellent (six-
to-nine-way independent reproduction is now routine), and nothing here
argues for stopping it. But 24 iterations is a long run for a program
whose founding target phenomenon (`PANEL.md`'s constraint 3, "the hard
one, do not let it slip") has not been touched even once in that span. I
second, from a seventh independent angle, the still-unresolved
"ritualization governance question" named at Iteration 61: the Director/
panel should state explicitly, at some near-term checkpoint, either a
condition under which this desk work is expected to reconnect to a
constraint-3-scoring run, or a formal decision to carry it as a separate,
explicitly-parked instrument-fidelity project distinct from the program's
main constraint ledger.

## Ranked top-3 for the Director's Iteration-70 queue

1. **Immediate, same-shift, near-zero cost**: delete `NOTES.md`'s
   duplicate stale `## Learned`/`## Next` placeholder pair (lines
   453–460) before any future document cites this file's tail. Cheapest
   possible fix, closes the one genuinely new defect this review found,
   before it has a chance to mislead a citation the way past
   disclaimer-carry gaps did.
2. **Cheap, zero-FDTD, the direct payoff of this cycle's own successful
   crossing-location work**: re-fit R15's caution-zone question using the
   two newly-located `cpl=30` crossings (lower at 40.072°; upper pair at
   41.781°/41.838°, or the region treated as one complex feature) as
   inputs — `NOTES.md`'s own Next item 1, which I independently rank
   highly on its merits: it is the natural, already-budgeted-for
   completion of exactly what this cycle set out to measure, and R15 has
   now sat as an open, named question for one full cycle with the data to
   close it sitting unused.
3. **Governance, program-wide, no cost**: fold this review's independent
   restatement of the Iteration-61 ritualization question into the
   Director's own LOGBOOK entry, with an explicit disposition (not
   deferral) — either name the condition for this sub-thread's next
   constraint-3-facing run, or formally reclassify T28 desk work as a
   parked instrument-fidelity track. Twenty-four cycles of silence on my
   seat's own founding duty is long enough that "still unresolved" should
   become a decision, not a running tally.

Honorable mention, outside my own comparative advantage but supported on
the record: a dedicated, finer-than-0.2° sweep of the 41.6°–42.2° upper
window to determine whether the double-crossing pair is a genuine two-node
feature or an under-resolved single deep null (`NOTES.md`'s own Next item
2) — a real open question, just not one my charter is positioned to
adjudicate ahead of PHOTONICS/ELECTROMAGNETISM.
