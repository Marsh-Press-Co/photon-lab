# Phase 5 — RED TEAM final audit (Panel Iteration 77, exp-100)

Input packet: PANEL.md (full), LOGBOOK.md (full — RULED OUT registry R1–R20
read verbatim, ESTABLISHED section, LIVE THREADS T1–T27, the T28 sub-thread
narrative in full through Iteration 76/exp-099), the complete exp-100
record (`phase1_proposal.md`, all five `phase2_critique_*.md`, my own
`phase2_redteam_audit.md`, `NOTES.md`, `run.py`, `results.json`,
`run_output.txt`, `disposition_memo.md`), and all six Phase-5 reviews
(`phase5_review_{photonics,materials,em,thermodynamics,vision,quantum}.md`).
Every load-bearing claim below is independently re-derived from primitives
(`lab/fdtd2d.py`, `lab/emit.py`, `experiments/069-.../design_geometry.py`,
`experiments/090/095/098/099-.../results.json`, `git log`/`git show` on this
experiment's own commit history) — marked **[verified from primitives]** —
or explicitly marked as relying on a cited seat's own factual claim,
spot-checked. Nothing below is taken on any seat's word, including my own
earlier Phase-2 audit's.

---

## 0. Independent primitive re-verification (before ruling on anything)

**The `beam_behind_t28` lateral-shift defect.** Recomputed independently
in Python from `lab/fdtd2d.py:138-139`'s documented convention ("the −x-going
wave then travels along (−cosθ,+sinθ)" — confirmed verbatim by direct grep,
not paraphrased) and `design_geometry.py:257,296` (`R4_R_OUT=156`,
`REF_HALF_H_R4=160`, both confirmed by direct read): `Δy=(156+10)·tanθ` at
the six Leg-B angles gives 125.669 / 132.470 / 140.606 / 144.103 / 146.663 /
154.586 cells — reproducing NOTES.md's cited "125.7–154.6 cells" and
"79%–97% of the 160-cell half-width" to the digit, independent of PHOTONICS'
and EM's own (also independent) re-derivations. **All three re-derivations
agree exactly; the claim is correct.**

**The Tier-1 pooled/family-stratified numbers.** Read directly from
`results.json`, independent of NOTES.md's prose: `r_pooled=0.20650703941944507`
(0.2065), `p_pooled=0.0758`; R3 `n=33, r=0.4862068708642141` (0.4862),
`p=0.00415` (0.0042); R4 `n=35, r=0.1102867253871392` (0.1103), `p=0.5249`
(0.525); R5 `n=4, r=0.9010050941024483`, `p=0.1644`. **All match the task
brief's own cited figures and NOTES.md's Result section exactly, to full
stored precision.** `run.py`'s `pearson_r()`/`permutation_test()`/
`tier1_item1()` implement the stated joint rule (`p<0.05 AND |r|≥0.2`) and
family split exactly as described; `POOL_TABLE`'s family tags are each
independently sourced from the originating file's own family-defining
constant (documented inline), never guessed from the pooled JSON — no R4/R20
defect found in this machinery.

**MATERIALS' claim that the R3-vs-R4 split is a named instance of R15's own
Iteration-71/exp-094 addendum.** Read R15's addendum text directly from
LOGBOOK (RULED OUT registry, lines 578–618, quoted in full in my Phase-0
read above): its founding shape is a **cross-resolution reversal of the SAME
measured feature at matched geometry** (exp-093's `cpl=30` near-null points
reversing sign/classification at exp-094's `cpl=40`, built via a
"congruent-construction recipe" mechanically rescaled), with the explicit
remedy "a third, differently-ratioed resolution point... and, before that
point is trusted, the new family must... reproduce the ALREADY-KNOWN-CORRECT
sign at a robust, far-from-null angle" (a ground-truth-recovery
precondition), and the explicit rejection of "defaulting to the finer grid
as automatically more correct." **exp-100's Tier-1 item 1 is structurally
similar but not identical**: it is not a pointwise sign reversal of the same
angle at two resolutions, but a stratified-correlation split across pooled,
largely non-matched angle sets computed at different `cpl` values within
each family. The underlying lesson generalizes cleanly (don't trust either
resolution family in isolation when they disagree; more data of the
disagreeing family's own kind cannot resolve which one is right; the
addendum's own named remedy — a third, differently-ratioed, properly-powered
point with ground-truth gating — is the correct diagnostic class here too),
but MATERIALS' framing ("a named instance," full stop) slightly overstates
the literal fit. **Ruling: ADOPTED, with a precision correction** — see §2.

**R16's exact text vs. THERMODYNAMICS'/EM's "persisted-but-not-narrated"
finding.** R16's text (LOGBOOK lines 619–661) and its forward clause
("a third occurrence of 'a disclaimer travels but the field it is meant to
cover is never persisted'... fires Checkpoint criterion 4 automatically")
concern **non-persistence** specifically — a computed field that never
reaches `results.json`. `results.json` confirms **[verified from
primitives]**: all 6 `tier2_leg_b.report` rows carry
`p_abs_w_{c,g}`/`dt_ss_full_K_{c,g}`/`netd_classification_{c,g}`/
`sigma_ext_cells_{c,g}`/`ratio_abs_ext_raw_{c,g}` in full, and `run.py:531-534`
hard-asserts `set(nrow.keys()) >= NETD_ROW_KEYS` before writing
`results.json` — a code-enforced gate stronger than either prior occurrence
of this pattern shipped. **R16's own literal trigger is not met — persistence
happened, verifiably.** The gap THERMODYNAMICS and EM both independently
found is different in kind: NOTES.md's own Result/Learned prose (as
originally filed) never stated the sidecar's own headline finding in words,
even though the data sat correctly in `results.json`. This is a real,
distinct, "one level up" recurrence of the exact shape THERMODYNAMICS' own
Iteration-76 self-review found in itself one cycle earlier (LOGBOOK
6688–6691, confirmed verbatim) — **not an R16 violation, a new pattern**. See
§4 for the standing-rule ruling.

**The module-chain crash — is this a two-cycle-running pattern?**
Independently read `git show fd3ab66` (the crash-fix commit) and LOGBOOK's
own exp-099 entry (lines 6658–6662). exp-099's crash was a `KeyError` from a
freshly-computed float failing to bit-match a 6-decimal-rounded filed key,
occurring **after 12 real FDTD calls had already completed**. exp-100's crash
was a multiprocessing `PicklingError` from two independent `_load()` chains
clobbering the same `sys.modules` registration, occurring **before any
`sim.run()` call executed**. **These are two different failure shapes, in
different code, with different consequences (zero calls wasted here; the
prior 12 calls survived intact there).** Ruling in §4.

**QUANTUM's self-review structural finding.** Independently re-read PANEL.md
§"The seven seats," item 7: "Red Team never leads a cycle; it has no
proposal of its own to protect" — this is PANEL.md's own, already-adopted
structural answer to exactly the bias QUANTUM's self-review names (a
rotation lead has a motivated stake in "being the cycle that broke the
drift"). Ruling in §4.

---

## 1. Ruling on each of the six Phase-5 reviews' findings

Discipline matches my own Phase-2 audit: every finding is ADOPTED,
ADOPTED (non-blocking), or OVERRIDDEN, with reasons.

### PHOTONICS (verdict: CONCUR-WITH-GAPS)

1. **`beam_behind_t28` diagnosis is physically sound, corroborated
   quantitatively (top-hat model, 0.42→0.50 predicted vs. 0.4156→0.4589
   measured).** **ADOPTED.** Independently re-verified the Δy arithmetic
   myself (§0); the top-hat cross-check is a genuine, additional
   quantitative corroboration beyond what NOTES.md itself offered — a real
   contribution, not a restatement.
2. **`observer_record_t28` is correctly exempt from the same defect class
   (whole-domain FFT, no window to mis-center).** **ADOPTED** — confirmed
   `lab/emit.py:80-127` FFTs the full interior window, not a narrow strip;
   PHOTONICS' distinction is accurate.
3. **Prefer the closed-box reconstruction over line-window re-centering,
   stated as a preference, not an equal alternative.** **ADOPTED
   (non-blocking, forward-looking).** This is a recommendation for
   Iteration 78, not a defect in what shipped. Endorsed in the reconciled
   queue (§6).
4. **The T21 750nm/4.7×`C_thr` precedent needs a sharper flag and a higher
   Iteration-78 rank than the generic deferred-backlog bucket.** **ADOPTED
   (non-blocking).** The precedent is real and already correctly disclosed
   in NOTES.md (per my own Phase-2 audit's mandatory fix, itself adopted
   from PHOTONICS' Phase-2 critique) — this is a ranking argument, not a new
   defect. Folded into §6.
5. **Give the R3-only correlation a physical hypothesis (Fresnel-number/
   length-scale check) before spending new FDTD on it.** **ADOPTED
   (non-blocking).** A genuinely cheap, zero-FDTD desk item; sequenced in
   §6 ahead of any new FDTD spend on this question.

### MATERIALS (verdict: CONCUR-WITH-GAP(S))

1. **Fix 6 (the per-outcome conditional) genuinely resolved the category
   error, on real, not merely hypothetical, data.** **ADOPTED.**
   Independently confirmed against `results.json`/`disposition_memo.md`:
   the ambiguous branch fired exactly as pre-registered, with zero post-hoc
   discretion.
2. **The R3-vs-R4 split is a named instance of R15's Iteration-71 addendum,
   whose already-specified remedy (a properly-powered, ground-truth-gated
   R5 census) — not "more R3 data" — is the correctly-targeted next step.**
   **ADOPTED, with the precision correction stated in §0**: the fit is
   close but not literal (a stratified-correlation split across a pooled,
   non-matched census is not the same construction as R15's own founding/
   addendum pointwise-reversal shape). The underlying prescription is
   nonetheless correct and now applied to `disposition_memo.md` (same-shift
   fix, §5) and to the reconciled queue (§6), which resolves the direct
   tension with QUANTUM's own "targeted R3 replication" recommendation by
   sequencing, not by picking one over the other.
3. **The realizability ceiling: no branch of item 2's conditional can ever
   exceed "published."** **ADOPTED, mandatory, zero marginal cost.** Applied
   same-shift to `disposition_memo.md` (§5).

### ELECTROMAGNETISM (verdict: CONCUR-WITH-GAP(S))

1. **`observer_record_t28`'s fix is correctly implemented (three
   independent checks: magnitude sanity, directional determinism, trend
   consistency).** **ADOPTED.** Independently re-read `run.py:472-490`
   against `lab/emit.py`; the construction matches the mandated fix exactly,
   with no field-array edits — confirmed clean.
2. **`beam_behind_t28`'s reading is fully and only explained by the
   geometric window/shadow mismatch — no separate energy/normalization
   defect.** **ADOPTED.** Confirmed `beam_behind_t28`'s ratio is
   self-normalizing (same fixed window both times, no separate `i_inc`
   division to get wrong) — a materially different risk profile than
   `sections.widths()`'s own channels, correctly distinguished.
3. **NETD data is persisted but never narrated — a completeness gap, not a
   persistence gap; R16 is cleanly satisfied.** **ADOPTED** — matches my own
   independent R16 re-reading in §0 exactly. Folded into the R21 ruling
   (§4).
4. **RT-1's fix is a real improvement but a partial one — the genuine local
   extremum near θ≈41.5°–42° and any peak beyond 42.960901° remain
   untested.** **ADOPTED (non-blocking)**, and superseded in severity by
   Red Team's own new finding below (§3): the gap is not only "unsampled
   territory," it is a citation-accuracy defect against ALREADY-sampled
   territory.
5. **Loose citation of "R18" for the empty-scene validation gate; a
   defensible but imprecise fit.** **ADOPTED (non-blocking, citation
   hygiene).** Correct: R18's own text concerns a check's documented scope
   vs. source and fault-injection controls for a layered architecture; the
   validate-before-trust discipline here is closer to the general R6/R8
   lineage. Non-load-bearing — the gate itself is sound regardless of which
   rule number labels it.

### THERMODYNAMICS (verdict: CONCUR-WITH-GAP(S))

1. **Fix 7's literal persistence mandate is honored exactly, code-enforced,
   stronger than any prior occurrence of this pattern.** **ADOPTED** —
   independently confirmed in §0.
2. **But the sidecar's own headline finding never reached NOTES.md's
   Result/Learned prose — a "one level up" recurrence of THERMODYNAMICS'
   own Iteration-76 self-review finding, on the identical channel, one
   cycle later — not a literal third R16 occurrence.** **ADOPTED, ruled
   precisely**: this is the correct, careful distinction (§0), and it is
   the evidentiary basis for the new standing rule proposed in §4.
   Same-shift narration fix applied to NOTES.md (§5).
3. **The `ratio_abs_ext_raw` reconfirmation of T9's ~0.51 anchor at oblique
   R4-family incidence is a genuine, previously-uncredited free finding.**
   **ADOPTED.** Applied same-shift to NOTES.md's Result section (§5).
4. **Candidate standing-rule text offered for Red Team's consideration
   (not self-adopted), citing Iteration 65's dual-section
   carried-idealizations-banner rule as the structural precedent.**
   **ADOPTED as the basis for R21** — see §4; THERMODYNAMICS' own proposed
   mechanism (require the headline classification/value inline in Result,
   not merely Setup/Predictions) is close to what I adopt, sharpened with
   an explicit forward-firing trigger matching R16–R20's own format.

### VISION SCIENCE (verdict: CONCUR-WITH-GAP(S))

1. **Both Phase-2 mandatory fixes (corrected scotopic anchors; static-
   contrast-bound-only caveat) are correctly implemented in code, not just
   promised in prose.** **ADOPTED** — independently confirmed against
   `run.py:404-405,418-425` and `results.json`.
2. **A second, distinct caveat (Tier 1's ambiguous outcome) is not restated
   at Leg A's own point-of-claim, even though the two caveats that ARE
   present there are correctly implemented.** **ADOPTED, mandatory.**
   This is a real, precisely-identified gap — the ambiguous-mechanism
   caveat is a different failure mode (whether `delta_scene` is a real
   scene-observable quantity at all) than the two present caveats
   (instrument scope). Applied same-shift to NOTES.md (§5).
3. **On `beam_behind_t28`: the corrected re-run does not need to wait on T3
   and is not a near-threshold call — a genuine leak, if real, would be
   orders of magnitude past any of this program's own thresholds.**
   **ADOPTED.** Correct and useful: this decouples Tier-0's fix from any
   T3 dependency, and is folded into the reconciled queue's own sequencing
   (§6) to make explicit that Tier 0 and the T3-build recommendation do not
   compete for priority.
4. **T3 should be built now — first-ranked for Iteration 78 — via a
   differently-scoped dispatch route that avoids the prior `[bio]`-tagged
   false-positive.** **ADOPTED (non-blocking on this cycle, forward
   recommendation).** A legitimate, well-argued process point; folded into
   §6 as a parallel, non-FDTD-budget-competing track, not gating Tier 0.

### QUANTUM OPTICS (self-review, verdict: CONCUR-WITH-GAPS)

1. **Honest self-accounting of RT-1/RT-2/RT-3: each defect was visible from
   QUANTUM's own Phase-1 text cross-read against itself, and the proximate
   cause was reduced adversarial scrutiny from a motivated author.**
   **ADOPTED as an accurate self-assessment** — independently checked
   against the actual `phase1_proposal.md` text (§7 "open question 1" vs.
   the Leg-B angle selection; the "not a confident lean" prediction vs.
   RT-2's missing threshold; the correctly-cited "gated on Tier 1's
   outputs" language vs. the unconditional Leg-B commitment) — all three
   self-diagnoses are precise, not exculpatory.
2. **The structural argument (a rotation lead has a lower adversarial bar
   than Red Team on its own cycle) is offered as a possible fresh
   governance finding.** **OVERRIDDEN as a request for new governance** —
   see §0 and §4: this is exactly the failure mode PANEL.md's own
   already-adopted charter design (Red Team "never leads a cycle; it has no
   proposal of its own to protect," §"The seven seats" item 7) exists to
   counteract, and this cycle's own outcome (three real defects caught by
   Red Team, corrected pre-freeze, zero surviving to Phase 4 undisclosed)
   is evidence the existing mechanism is working as designed, not evidence
   of a gap needing new text. Retained as a valuable, well-articulated
   first-person case study for the record — not as a rule.
3. **`beam_behind_t28`'s window-centering defect is a genuinely new defect
   class this seat did not anticipate, distinct from RT-1/2/3's
   "missing a threshold/gate/sampling correction" shape.** **ADOPTED** —
   an accurate characterization; already the cycle's own Tier-0 item.
4. **The module-chain-loading crash: "no, not yet" rule-worthy.**
   **ADOPTED** — matches my own independent ruling in §4 exactly, for the
   same reasons (different failure shape than exp-099's; zero calls
   wasted; a process/tooling hazard, not a substantive-claim hazard).
5. **Ranked-3 items (fix beam_behind_t28; targeted R3 replication; scope
   what a future σ(I)/σ(x,t) proposal may claim from `delta_scene`).**
   **ADOPTED (non-blocking, forward recommendations)** — folded into §6;
   item 3 in particular (explicitly narrowing what a future proposal may
   claim) is a good, cheap governance discipline, adopted into the queue.

---

## 2. New findings, independent of all six reviews

### RT5-1 — [inconsistency] Fix 1's "two largest-magnitude already-filed
`delta_scene` values" claim is false against this cycle's own full pooled
table [verified from primitives]

**Claim.** NOTES.md's fix 1 (RT-1's own mandatory fix from Phase 2) states
Leg B's two added angles, θ=40.960901° (`delta_scene=+2.471869×10⁻³`) and
θ=42.960901° (`+2.778079×10⁻³`), are "the two largest-magnitude already-filed
`delta_scene` values in the characterized 36°–43° window." I independently
searched this cycle's own full pooled table — the exact 75-row, 36°–43°-
windowed dataset `tier2_leg_a()` scores, built by `pool_rows()` from 7
experiment directories, the SAME data source Tier 1 item 1 uses — and found
its own computed peak, reported in `results.json:tier2_leg_a`, is
**`peak_abs_delta_scene=0.003149520984824239` at `theta=39.2`**, sourced from
`095-t28-r4-ground-truth-sign-control`. I independently re-verified this
against `experiments/095-.../results.json::rank1.rank1a.per_theta["39.2"]`
directly: `delta_scene=-0.003149520984824239` — the raw stored value, whose
magnitude (0.0031495) exceeds BOTH of Leg B's "two largest" points (0.002778,
0.002472) by 13%–27%. The 39.2° row is tagged `R4` family (same family, same
`cpl=40`, per `POOL_TABLE`'s own family sourcing) — so the restriction to
"R4 family, `cpl=40`" cited in fix 1's own justification does not explain
the omission; it is a genuine search-scope gap: fix 1's search covered only
`experiments/099-.../item_1.combined_report`, never the full pool this same
document's own Tier 1 item 1 assembles from 7 directories including
exp-095.

**Tag:** [inconsistency] — a claimed-exact descriptive figure about a
data-derived selection that does not reproduce against the very dataset this
same document computes elsewhere, an R4/R20-adjacent citation-accuracy
defect in shape (a specific, checkable claim that fails on direct
re-verification), though not a literal instance of R4 (which concerns
"precisely recomputed" figures cited in prose, not a search-scope omission
in a selection criterion).

**Severity, assessed honestly: real but non-load-bearing.** Constraint 2's
PASS margin (empty self-ratios 1.0×10⁻⁴–3.9×10⁻⁴ against a 0.02 gate, ~50–
200× headroom) is far too large for a 13% larger `delta_scene` reading at
39.2° to plausibly change the qualitative PASS. Constraint 1 is already
UNINTERPRETABLE for an unrelated, unrelated-in-mechanism reason (the window
defect, §RT-1 already fixed at Phase 2, itself independent of which angles
are chosen). No scored verdict in this document moves.

**Note for the record: caught at the correct, final layer.** None of the
five Phase-2 blind critiques, my own Phase-2 audit, nor any of the six
Phase-5 blind reviews caught this — it surfaced only here, at Red Team's own
Phase-5 final audit, which is exactly the backstop role PANEL.md assigns
this seat ("speaks last and hardest"). This is the process working as
designed, not a gap in the process — matching this program's own
established non-firing treatment of a defect caught by Red Team's own final
audit before LOGBOOK, corrected same-shift (§5), never defended.

**Same-shift fix, applied:** NOTES.md's Idealization 68 and Result section
corrected in place (see the edits already applied to `NOTES.md`, this
audit's own companion fixes) to state the true scope of fix 1's search and
name the θ=39.2° value explicitly. Iteration 78's own angle-selection
practice (whenever it next needs "the largest-magnitude filed value") is
bound to search the full pool, not a single experiment's own subset.

---

## 3. Standing-rule ruling

### R21 — a persisted post-run analytic sidecar field's own headline finding
(classification/value) must be stated inline in the cycle's own Result
section, not merely in Setup or the frozen Predictions table — persistence
alone (R16's own standard) is necessary, not sufficient, for the finding to
be treated as engaged with

**Not a ruled-out idea; proposed standing house-discipline rule, Red Team's
Phase-5 final audit, Iteration 77.** R16 (adopted Iteration 71) polices
whether a computed byproduct field reaches `results.json` at all. exp-100
shows this is not sufficient: fix 7's `netd_row()` mandate was honored
exactly, code-enforced (`run.py:531-534`'s assert), independently confirmed
present in all 6 report rows (THERMODYNAMICS, EM, and this audit,
independently, §0/§1) — R16's own literal trigger does not fire. But the
sidecar's own headline finding (all 12 classifications `UNDETECTABLE`; the
free `ratio_abs_ext_raw≈0.51` reconfirmation) never reached NOTES.md's
Result/Learned prose in the version filed at Phase 4 — the exact shape
THERMODYNAMICS' own Iteration-76 self-review found in itself one cycle
earlier, on the identical NETD/thermal-sidecar channel (LOGBOOK 6688–6691,
independently confirmed verbatim, §0), now recurring a second time, one
cycle later, on a document that satisfied the STRICTER, code-asserted
version of the persistence mandate. **This is a genuinely distinct failure
axis from R16: R16 asks "was the field written to `results.json`?"; this
rule asks "was the field's own finding stated in the prose a future citation
will actually read?" — a document can pass the first test perfectly and
fail the second, as this cycle demonstrates.**

**Rule:** any cycle that persists a `netd_row()`-class (or equivalent
post-run analytic sidecar) field, satisfying its own persistence mandate,
must ALSO state that field's own headline classification/value inline in
the Result section — not merely in Setup, the tools-reused list, or the
frozen Predictions table — before the persistence commitment is treated as
fully discharged. This generalizes, one level up, the precedent already set
by this program's own dual-section carried-idealizations-banner rule
(Iteration 65, exp-088 — adopted after a disclaimer proved not to propagate
from Predictions into Result on its own) to a computed VALUE rather than a
disclaimer.

**Founding basis: two instances on record** (Iteration 76/exp-099,
THERMODYNAMICS' own self-review; Iteration 77/exp-100, THERMODYNAMICS' and
EM's independently-convergent Phase-5 findings), both on the identical NETD
channel. **Does not fire on either founding instance** — matching every
prior R-rule's own precedent (R5–R20): a rule's founding/consolidating
cycle establishes the standard rather than retroactively violating it; both
instances were caught blind, within each cycle's own review layer, before
LOGBOOK, and corrected same-shift (this cycle's fix already applied, §5).
**Standing forward-elevating clause: a THIRD occurrence of "a persisted
byproduct field's own headline finding never stated in Result/Learned
prose," on this or any T28-adjacent channel, in any form, fires Checkpoint
criterion 4 automatically, no further deliberation** — mirroring R16's own
three-strike forward clause exactly, one level up (narration, not
persistence). Full record: this document, §0/§1/§3; LOGBOOK.md Iteration
76 (THERMODYNAMICS self-review, lines 6688–6691); this experiment's
`phase5_review_thermodynamics.md`, `phase5_review_em.md`.

### Not adopted as standing rules

- **The module-chain-loading `PicklingError`.** Ruled **NOT YET
  PATTERN-WORTHY**, agreeing with QUANTUM's own self-review ruling and
  independently confirmed in §0: exp-099's `KeyError` (a dict-key
  float-rounding mismatch, caught after 12 calls) and exp-100's
  `PicklingError` (a multiprocessing module-registration collision, caught
  before any call) are genuinely different failure shapes in different
  code, sharing only the surface commonality "an own-code bug caught before
  any result was corrupted, fixed same-shift, disclosed in full." Two
  instances of different shapes do not meet this program's own "known,
  named, ignored" bar (R6–R20's own shared standard requires the SAME
  defect recurring unfixed, not two different defects in the same general
  category). **Endorsed as a cheap, non-mandatory improvement** (not a
  rule): QUANTUM's own suggestion — a one-line assert at the top of any
  future `_load()` block checking no `sys.modules` name is about to be
  silently re-registered by a second, independent load of a file another
  already-loaded chain also transitively loads — would catch this
  mechanically going forward, worth adopting as a house idiom even absent a
  named rule.
- **QUANTUM's structural self-review finding (rotation-lead self-review has
  a lower adversarial bar than Red Team).** Ruled **ADEQUATELY COVERED by
  existing discipline**, not a fresh governance gap: PANEL.md's own
  founding charter already assigns Red Team the role of the harshest,
  last-word, non-lead-carrying check for exactly this reason (§"The seven
  seats," item 7, quoted in full in §0), and this cycle's own outcome — all
  three of QUANTUM's self-diagnosed defects (RT-1/RT-2/RT-3) were caught
  and fixed before Phase 3 freeze, by Red Team, not defended — is a clean
  demonstration the mechanism is functioning, not evidence it needs new
  text. No rule proposed. The self-review practice itself (informal,
  adopted by precedent since Iteration 76, not mandated by PANEL.md's
  original Phase-5 text) remains valuable for candor and is correctly
  labeled "(self-review, rotation lead)" in this cycle's own document,
  distinguishing it from a blind critique — that labeling convention is
  sufficient; no additional rule is warranted.

---

## 4. Checkpoint criterion 4 — explicit ruling

**Does NOT fire this cycle.** Ruled after weighing every candidate vector
named across all six Phase-5 reviews, my own Phase-2 audit's flagged risks,
and this audit's own new finding (§2) — this is a genuinely close call, in
the same rhetorical territory as Iterations 51/53/55/56/57's own "close but
non-firing" rulings, not a reflexive non-firing by inertia.

**Evidence weighed toward firing:**
- RT-3's own Phase-2 warning (an eighth T1:N/A deferral dressed as
  progress) was a serious, well-founded risk at Phase 2 — exactly the
  "unfalsifiable claim of progress on the central tension" pattern
  Checkpoint 4 exists to catch.
- The netd-narration gap (§3/R21) is a SECOND occurrence of a named pattern
  on the identical channel, one cycle after the first.
- `beam_behind_t28`'s own constraint-1 reading came back UNINTERPRETABLE —
  the one direct constraint-1 measurement this cycle set out to make did
  not, in the end, produce one.
- This audit's own new finding (§2, RT5-1) shows a mandatory Phase-2 fix
  was implemented against an incomplete search, undetected by five blind
  critiques, my own prior audit, and six further blind reviews.
- The T1:N/A streak is now honestly extended to an EIGHTH consecutive cycle
  (Iterations 70–77) — precisely the drift pattern PANEL.md names by
  number of cycles, not merely by kind.

**Evidence weighed toward non-firing, ruled controlling:**
- RT-3's risk was **verified, from primitives, to have been structurally
  discharged, not merely narrated as discharged**: `results.json`'s own
  `t1_label` field reads "N/A, unresolved... Tier 2's own numbers... do not
  move T1 in either direction," exactly the pre-registered branch for a
  contradictory outcome — the mechanism designed to prevent the drift-as-
  progress overclaim fired correctly, on real, non-hypothetical
  contradictory data (independently confirmed, §0). No document in this
  cycle's own record narrates this as "the streak broken."
- The netd-narration gap is the SECOND, not the third, instance — R21's own
  forward clause (mirroring R16's) requires a third before automatic firing;
  this cycle IS one of R21's two founding instances, non-firing by the same
  precedent every prior R-rule has established.
- `beam_behind_t28`'s UNINTERPRETABLE result is a genuine, first-time
  defect in a NEW instrument, caught, quantified (the exact Δy mechanism,
  independently reproduced three ways: NOTES.md, PHOTONICS, EM, and this
  audit — four ways), and honestly reported as uninterpretable rather than
  smoothed into a false PASS or a false constraint-1 finding — the correct,
  scientifically honest disposition, not a defended error.
- RT5-1 (§2) was caught by Red Team's own final audit, before LOGBOOK,
  exactly where PANEL.md's own design places the last check — and it is
  non-load-bearing to every scored verdict in the document (§2's own
  severity assessment).
- The module-chain crash cost zero FDTD calls and is fully disclosed with a
  git-tracked diff (§0).
- Constraint 3 — "the hard one, do not let it slip" — was NOT quietly
  dropped: Leg A explicitly scores it, with the T21/750nm contamination
  risk disclosed (not hidden) as untested, and the ambiguous-mechanism
  caveat now explicitly attached (VISION's fix, §5) rather than allowed to
  read as a clean verdict.

**On the 8-cycle T1:N/A streak specifically:** this is real and should be
named explicitly, not folded silently into "PARTIAL" the way it might read
at a skim. It is not, itself, evidence of drift-as-concealment — this
cycle's own record is the most direct, honest engagement with the question
in the streak's history, including a genuine methodological win (the
pre-registered branching mechanism validated on real contradictory data).
But an 8th cycle without resolution is exactly the number PANEL.md's own
Checkpoint criterion 4 language contemplates, and Iteration 78 should not
be permitted a 9th non-resolving cycle on this specific sub-question without
either (a) running the specifically-indicated diagnostic (§6, Tier 0) or (b)
an explicit, written decision to retire the `delta_scene`-realizability
question as economically unresolvable at this bench — mirroring this
program's own Iteration-51 precedent ("no seventh cycle on the same
instrument class... without a qualitatively different calibration
strategy"). Stated as a binding queue item, not a Checkpoint firing, in §6.

---

## 5. Same-shift mandatory fixes (applied)

All documentation-only, zero-FDTD, matching this program's own precedent
for closing Phase-5-caught gaps before a cycle's record is considered
closed:

1. **NOTES.md, Tier 2 Leg A Result paragraph** — appended the
   ambiguous-T1/instrument-characterization-only caveat VISION's Phase-5
   review specified. **Applied.**
2. **NOTES.md, Tier 2 Leg B Result section** — added the NETD/thermal
   sidecar narration paragraph (THERMODYNAMICS'/EM's Phase-5 finding):
   all 12 classifications UNDETECTABLE, `dt_ss_full_K` range stated, and
   the free `ratio_abs_ext_raw≈0.51` generalization credited. **Applied.**
3. **NOTES.md, Tier 2 Leg B Result section** — disclosed this audit's own
   RT5-1 finding (the θ=39.2° angle-selection gap) directly in the Result
   section, not only in the Idealizations. **Applied.**
4. **NOTES.md, Idealization 68** — corrected to state the true scope of
   fix 1's search (exp-099's own subset, not the full pool) and name the
   θ=39.2°/3.1495×10⁻³ value the search missed. **Applied.**
5. **disposition_memo.md** — added the MATERIALS-specified realizability
   ceiling statement (no branch can ever exceed "published") and the
   precise R15-Iteration-71-addendum connection with the corrected remedy
   language (a properly-powered, ground-truth-gated R5 census, not a fresh
   R3-family spend). **Applied.**

No fix required a re-run, a changed classification, or a changed
PASS/FAIL/UNINTERPRETABLE verdict anywhere in this document — every fix is
additive disclosure or a corrected descriptive claim about already-computed
data.

---

## 6. Overall Combined Verdict: **PARTIAL**

Genuine, disclosed progress, on both sides of the ledger:

**Real progress.** (a) Constraint 2 (specular return) receives this bench's
first-ever clean, trustworthy, directly-measured PASS, at 6 points,
independently re-verified by this audit and EM from primitives — a real,
first-time result. (b) The pre-registered T1-labeling mechanism (fix 3,
Idealization 70) — this cycle's own central defensive structure, forced
onto the design by Red Team's own Phase-2 RT-3 finding — is shown working
on genuine, non-hypothetical contradictory data, not merely specified on
paper: a real methodological win for this program's own governance, however
the substantive `delta_scene` question resolves. (c) `delta_scene` receives
its first-ever direct comparison against a perceptual threshold instrument
(Leg A) and its first-ever refresh at points never sampled before (Leg B),
both honestly scoped and caveated. (d) A genuine, previously-uncredited free
finding (T9's ~0.51 anchor, reconfirmed at R4-family oblique incidence for
the first time) is recovered and now credited.

**Real, disclosed shortfalls.** (a) Constraint 1 (beam termination) —
the cycle's other headline goal — comes back UNINTERPRETABLE, a genuine,
first-time defect in a newly-built instrument, honestly diagnosed and not
papered over, but a real gap nonetheless: this cycle's own "first-ever
direct constraint-1/2 measurement" framing is only half true as filed. (b)
Tier 1's central question — does `delta_scene` carry genuine article-coupled
content — remains AMBIGUOUS, not resolved in either direction; the T1:N/A
streak is honestly extended to an eighth consecutive cycle. (c) This
audit's own new finding (RT5-1) shows even the mandatory Phase-2 fix meant
to broaden Leg B's coverage was executed against an incomplete search,
caught only at this final layer.

No mechanism class is ruled out or confirmed this cycle (Checkpoint
criterion 2 correctly stays N/A, per unanimous seat agreement); no
constraint metric passes cleanly across the board; nothing here rises to
RULED OUT. **PARTIAL**, matching this sub-thread's own established standard
for a cycle that genuinely narrows the record without closing its central
question.

---

## 7. Final, reconciled Iteration-78 queue

This supersedes NOTES.md's own draft §Next. Resolves the real disagreement
between MATERIALS' remedy (a properly-powered, ground-truth-gated R5
census) and QUANTUM's own recommendation (a targeted R3-family replication
check) by **sequencing both**, cheapest-and-most-informative first, rather
than treating them as competing.

**Tier 0 — mandatory precondition, cheap, zero ambiguity, no dependency on
anything else in this queue:**

1. **Fix `beam_behind_t28`'s window-centering defect and re-run
   constraint-1 at the same 6 angles.** Per PHOTONICS' and EM's own
   convergent, independently-reasoned preference: **prefer the closed-box
   (4-face Poynting) reconstruction over a re-centered line window** — it
   needs no new trigonometric correction to derive or verify at all
   (eliminating the exact defect class that has now hit this new-instrument
   family twice in one cycle — the missing Hy sign flip, then the missing
   angle correction), reuses already fault-injection-verified machinery,
   and is derivable at zero marginal FDTD cost from data this cycle already
   collected (`sigma_ext_cells`/`p_abs_w` are already in `results.json`). If
   a re-centered line window is chosen instead, EM's three named safeguards
   are mandatory (independent second-seat re-derivation of the correction;
   a positive control at the smallest tested angle; a cross-check against
   the already-trusted `sigma_ext_cells`/`p_abs_w` channel from the same
   captures) — not optional, given this is now the third new-instrument
   directional/geometric correction in this same family within two cycles.
2. **Re-select any "largest-magnitude" angle set from the FULL pooled
   table**, per RT5-1 (§2) — include θ=39.2° (or the actual global maximum,
   recomputed after the window fix, since the fix may itself shift which
   points are largest) rather than repeating exp-099's own incomplete
   subset search.
3. **Report the corrected forward-flux reading alongside the already-filed
   `p_abs_w`/`netd_classification`/`observer_article_norm` figures as one
   three-way energy-partition table** (absorbed / observer-direction return
   / forward-continuing) — THERMODYNAMICS' own Phase-5 recommendation,
   zero marginal cost, closes this seat's own open charter question in one
   step if the corrected reading confirms near-total blocking.

**Tier 1 — parallel, cheap, sequenced to resolve the R3-vs-R4 contradiction
efficiently (this queue's own resolution of the MATERIALS/QUANTUM tension):**

4. **PHOTONICS' zero-FDTD physical-hypothesis check first** (cheapest):
   before spending any new FDTD on the R3-vs-R4 split, compare R3's and
   R4's own respective length-scale/Fresnel-number regimes (already
   computable from `design_geometry.py`'s own constants) — if R3's geometry
   sits in a genuinely different diffraction regime, that is a candidate
   PHYSICAL reason for family-dependent coupling strength, distinct from
   "R3 is a recipe artifact."
5. **QUANTUM's targeted R3-family replication check second** (cheap FDTD):
   a small, fresh R3-family spend at a few new angles, testing whether the
   R3-only significant correlation (r=0.486, n=33) replicates
   independently. If it does NOT replicate, that alone is strong evidence
   against genuine coupling and may make item 6 unnecessary — the cheap
   filter this program's own house discipline favors before a larger spend.
6. **MATERIALS'/R15's own specifically-indicated remedy: a properly-
   powered, ground-truth-gated R5 (`cpl=50`) census at R3/R4 density
   (~30+ points) across the same 36°–43° window**, gated on first
   reproducing a known-robust, far-from-null `delta_scene` sign on the R5
   channel (R15's own addendum precondition) — run regardless of item 5's
   outcome if item 4 does not foreclose a physical explanation, since only
   a properly-powered third resolution family can actually adjudicate which
   of R3/R4's readings (if either) is trustworthy. **This is the queue's
   own binding answer to the "no ninth non-resolving T1:N/A cycle" concern
   named in §4**: Iteration 78 or 79 should either complete this
   diagnostic or explicitly retire the `delta_scene`-realizability question
   as economically unresolvable at this bench, in writing.
7. **The 750nm (and ideally 450nm) leg of Leg A's own scored window** —
   elevated from the generic "standing 5–8-cycle-deferred" bucket to an
   explicit, ranked Iteration-78 item, per PHOTONICS'/EM's/VISION's
   independently-convergent argument: T21's own on-file 750nm/θ=40° fringe
   already measures 4.7×`C_thr` in this identical window, a specific,
   quantified, already-measured risk, not a generic wavelength-generality
   hedge.

**Tier 2 — parallel, non-competing for FDTD budget:**

8. **A genuine, differently-scoped attempt to build T3** (VISION's own
   #1 ranking) — a process/scheduling item, not a physics one; does not
   compete with items 1–7 for FDTD budget and should not be gated behind
   them or vice versa.
9. **Explicitly scope what a future σ(I)/σ(x,t) proposal may claim from
   `delta_scene`/Tier 1's own result** (QUANTUM's own item 3) — cheap
   governance text, before any such proposal is drafted: restrict any
   citation to the R3 family specifically (never the pooled null result)
   until item 5/6 resolves it, and treat the correlation as
   "unreplicated, single-family, possible shared-variance artifact"
   (Idealization 63) in the meantime.

**Tier 3 — standing, unchanged, carried forward:** the still-deferred
full-width non-aliased `G40` leg; the x-wall realizable-admittance refit;
`PAD`-sensitivity with a real absorbing article at other wavelengths/τ.
