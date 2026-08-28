# PHASE 5 — REVIEW · MATERIALS & METAMATERIALS · Panel Iteration 60 · exp-083

**Seat: MATERIALS & METAMATERIALS.** Fresh sub-agent, zero memory of any
prior session. Charter: sub-wavelength structure; what could physically
realize the proposed optical behavior; owns the realizability bound
(published / plausible / unobtainium-with-parameters). Read PANEL.md,
AGENTS.md, LOGBOOK.md (RULED OUT R1–R9, ESTABLISHED, LIVE THREADS in full,
T28's complete history through Iteration 59/exp-082), PLAN.md's
Iteration-60 queue, and the complete `experiments/083-.../` record —
`phase1_proposal.md`, `NOTES.md`, `run.py`, `results.json` (spot-checked),
`run_output.txt`, `null_permutation_control.json`, all five Phase-2
critiques, `phase2_redteam_audit.md`, `phase3_synthesis.md`. Blind to any
`phase5_review_*.md` from other seats this cycle, per PANEL.md.

**Independent verification performed.** Loaded `results.json` directly and
confirmed `primary_period_discriminator.p_star_deg=2.9473684210526314`,
`r_squared=0.858195125110302`, `branch="B_ARTICLE_EDGE_DIFFRACTION"`,
`branch_detail.rel_dev_edge_a=0.0370`, matching every cited figure in
`phase1_proposal.md`/`NOTES.md` to full float precision — not restated on
faith. Confirmed `secondary_correlation.{r_obs,p_value}=(0.39494,0.02806)`
and `reproduction_precondition.per_theta` shows `C40_dev=G40_dev=0.0` at
every one of the 31 angles sampled, matching the claimed bit-exact
reproduction. Confirmed `null_permutation_control.json`'s two entries match
the cited null-control prose exactly (`delta_scene`: `p=0.0`, `null_max=
0.6324`; `em_pair`: `p=0.00185`, `null_max=0.5599`). Everything I checked
reproduces.

---

## 1. My predecessor's article-radius discriminator — verified landed correctly, at the named priority

The task's own first question: did my Iteration-59 predecessor's proposal
land as the Iteration-61 top priority? **Yes, cleanly, at every layer of
this cycle's record, not merely asserted once.**

- `phase3_synthesis.md` §3, Item 3 [HIGH]: "MATERIALS' article-radius
  discriminator named as Iteration-61 top priority... now this sub-thread's
  single highest-priority item for Iteration 61 — sharpened, not merely
  confirmed, by Item 1's own downgrade of the causal label."
- `phase2_redteam_audit.md` Attack 3 independently ranks it "the single
  most information-dense open item on the board, more clearly so than
  MATERIALS' own critique states it" and Attack 1's own fix explicitly
  reads "Add MATERIALS' article-radius discriminator to PLAN.md's
  Iteration-61 board as the single highest-priority item."
- `NOTES.md`'s "Next" section leads with it verbatim: an `R_OUT` sweep at
  fixed `PAD`, checking whether `P*` tracks `R_OUT/λ` (genuine article-rim
  origin) or stays pinned (pre-existing domain/source artifact).
- This cycle's own `phase2_critique_materials.md` — read here as my
  predecessor seat's Phase-2 voice this same cycle, not confused with the
  exp-082 Phase-5 review that originated the Iteration-59 rule — restated
  the identical proposal as its own "single parameter change that would
  flip my verdict to full support," and Red Team's audit adopted that
  critique in full.

The proposal is intact end-to-end: Phase 2 named it, Red Team's audit
independently re-derived why it is now the single highest-value item (not
merely echoing MATERIALS' framing), and Phase 3 recorded it as the named
Iteration-61 top priority in both `NOTES.md` and `phase1_proposal.md`. The
only outstanding step is the mechanical one — the PLAN.md board edit itself
is explicitly deferred to the Director's own separate Phase-5 pass
(`phase3_synthesis.md` §3, Item 3's closing sentence), which is this
document's own job to flag forward, not to perform.

---

## 2. The task's own central question: does my Iteration-59 rule apply cleanly again, or does genuine ambiguity remain?

**Genuine ambiguity remains — my rule does not yet re-apply cleanly, and
saying it does would overstate what this cycle actually resolved.** Here is
the reasoning, worked through rather than pattern-matched to the prior
verdict.

### 2a. What my Iteration-59 rule actually said, re-read precisely

At exp-082 (7-point power), my predecessor's finding was: "this whole
confound is a pure scene/domain-geometry fact, no material implicated" —
adopted as a standing framing rule specifically because, at that cycle's
own statistical power, NO causal story had been distinguished from any
other; the entire observed effect was scene/domain-geometry by elimination,
since nothing had identified an alternative. That is a strong claim under
uncertainty, not a claim that survives any finding equally. It is TRUE
precisely when the record cannot yet distinguish a materials-relevant
mechanism from a materials-irrelevant one.

### 2b. What Red Team's correction (Attack 1) actually changed

The task brief frames this as "Red Team's correction... that this is
'matches T28's own unexplained family,' not 'article-edge diffraction'" —
and that framing is correct as far as it goes, but understates the
directional content of what was corrected. Attack 1 did not simply retract
"article-edge diffraction" back to "purely a domain/scene artifact." It
retracted the CAUSAL label while leaving the STATISTICAL finding — a
decisive, doubly-instrument-corroborated, null-controlled period-family
match to `P_edge_A` — fully intact and re-affirmed. Two live possibilities
remain, both explicitly still open per Attack 1's own text: (i) the
article-loaded channel inherited T28's pre-existing, unexplained empty-
scene artifact (my Iteration-59 rule's reading, materials-irrelevant), or
(ii) it is genuine article-rim diffraction that happens to coincide with
`P_edge_A`'s own value (a live, not-yet-refuted possibility, since
PHOTONICS' own back-of-envelope estimate used the wrong formula class for
this near-field aperture — Fresnel number `N_F≈13`, not far-field — so its
3.3× miss is a formula-regime failure, not a clean refutation of a rim
origin).

This is the crux for my charter specifically. My Iteration-59 rule's
"zero realizability content" claim is licensed ONLY by reading (i). Reading
(ii), if it turns out correct, has the OPPOSITE realizability content: a
disk of `R_OUT/λ=3.9λ` presenting a diffracting rim to a swept beam is
trivially realizable — any macroscopic opaque edge of comparable electrical
size does this, published/plausible-tier by construction, no exotic
material required, but also not a "no material implicated" scene-geometry
artifact in the sense my rule asserts. **These are not two phrasings of the
same finding; they are two different realizability readings of the SAME
period-family match, and this cycle's own record — correctly, per Attack
1 — declines to adjudicate between them.**

### 2c. Why "cleanly re-applies" is the wrong description

My own Phase-2 critique this cycle (read blind to this document, but
consistent with the record I am now reviewing) reached the same structural
conclusion at Phase 2, before Attack 1 existed as a ruling: extend the rule
with an explicit addendum rather than let it re-apply unchanged, precisely
because Branch B's classification does not by itself tell you which reading
is true. Red Team's Phase-2 audit (Attack 3) went further and ranked the
discriminator as the single most information-dense item on the entire
board — a ranking that is only coherent if the ambiguity is real and
consequential, not resolved. A Phase-5 reader concluding "the causal claim
was walked back, so my rule already covers this" would be doing exactly
the thing Attack 1 exists to prevent one layer up: treating a corrected,
narrowed statistical finding as if it settled a question it was never
built to answer. The rule's ORIGINAL scope (drawn from a 7-point-power
cycle where every causal story was equally undetermined) is not
automatically the right description of a 31-point-power cycle where one
specific causal reading (rim diffraction) has been sharpened into a
falsifiable, still-open question with a named, cheap, un-run test.

### 2d. What would make the rule re-apply cleanly, and what would overturn it

Neither has happened yet. The `R_OUT` sweep is the entire content of the
open question: if `P*` stays pinned near `2.84°`/`1.96°` across article
radii, my Iteration-59 rule re-applies with full force and no addendum is
needed — the period-family match was always going to be a domain/source
artifact regardless of what sits in the object window. If `P*` tracks
`R_OUT/λ`, the rule needs the addendum my own Phase-2 critique already
drafted: article-rim diffraction of this kind sits at the trivial,
published end of my own realizability scale, but is a real, article-
mediated finding, not a "no material implicated, pure scene geometry" one.
**Until that 31-call sweep runs, both readings remain live, and this
cycle's own record — correctly, and disclosed as such throughout — does
not choose between them.**

---

## 3. Secondary findings, own charter

- **Construction identity, reconfirmed.** `run.py::build_article` is
  `pec_disk(...,30)` + `graded_black_shell(...,30,dg.R_OUT=78)`, unchanged
  from `exp-024`'s and `exp-082`'s own flagship absorber — no new material
  law, no new construction this cycle. `R_OUT=78` is a single, module-level
  scalar (`design_geometry.py`), never config-keyed, confirmed identical
  for `C40`/`G40` and never varied anywhere in this cycle's own 125 calls —
  independently re-confirmed here, matching Red Team's own §0b finding.
- **The near-null σ(I) article follow-up (Tier 1 item 6, still queued,
  not run this cycle) is the correct complementary test, not a
  substitute, for the article-radius discriminator.** A weak absorber
  answers "does the branch classification depend on absorption strength?";
  the radius sweep answers "does it depend on absorption geometry (rim
  size)?" Both bear on realizability but resolve different halves of the
  question — the radius sweep is correctly ranked first since it is the
  one that can flip Branch B's causal reading outright, not merely modulate
  its amplitude.
- **THERMODYNAMICS' re-scoped energy-interception concern (Item 4, Attack
  4) is realizability-adjacent and correctly generalized.** Whether
  `P_edge_A`'s own mechanism is dissipative bears on realizability too:
  a lossy rim-diffraction reading and a lossless domain-artifact reading
  would license different Joule-accounting stories for any future
  constraint-3 candidate that reused this geometry. This is downstream of
  the same open question §2 describes, not a separate one.

---

## VERDICT: **PARTIAL**

The primary statistical finding (Branch B, `R²=0.858`, doubly
instrument-corroborated, null-controlled at `p=0.0`) is decisive and not in
question — the strongest-powered period-family measurement this
nine-cycle-plus T28 sub-thread has produced, and correctly, honestly
corrected from an overclaimed causal label to an accurate period-family-
match statement (Attack 1, adopted in full, independently verified above).
But the question my own charter owns — what could physically realize this,
and at what tier — is **not answered by this cycle**, and could not have
been: the one test that discriminates realizable-article-rim-diffraction
from zero-realizability-content-domain-artifact was never run (`R_OUT` held
fixed throughout). My Iteration-59 rule stands as written for the case it
was built for (a fully undetermined confound) but does not yet cleanly
re-apply to THIS cycle's own sharper finding without begging the open
question — genuine ambiguity remains, correctly disclosed throughout this
cycle's own record, not resolved by the causal-label correction alone.

## Ranked top-3 candidate directions for Iteration 61

1. **MATERIALS' article-radius discriminator (`R_OUT` sweep at fixed
   `PAD`).** Re-run the identical `PAIR_PAD` (C40/G40) harness at one
   alternate article radius (e.g. `R_OUT=50` or `100`, ~31 calls, holding
   every other geometry parameter fixed), applying the same pre-registered
   free-period fit to `delta_scene`. This is the only test that resolves
   §2's own open question in either direction — confirmed as the board's
   single highest-priority item by Red Team's own independent ranking
   (Attack 3), not merely by my own predecessor's proposal. Pre-register
   both directional predictions (period tracks `R_OUT/λ` vs. stays pinned)
   before running, per this program's own standing discipline.
2. **A properly pre-registered null-calibration test for the two-tone
   `PAD`-continuity admixture question** (Attack 2's own named follow-up).
   This is not my charter's own primary concern, but it is realizability-
   adjacent: if a genuine second, `PAD`-tied component survives a correctly
   calibrated null, that component is independently already known lossless
   (Iteration 53) and materials-irrelevant regardless of how the radius
   sweep resolves — worth running in parallel since it is zero-FDTD and
   answers a structurally independent question from item 1.
3. **PHOTONICS' own zero-FDTD desk pre-check** — a coherent-sum
   construction treating the article's own two rim edges as a pair of
   secondary apertures, correctly accounting for the Fresnel-regime
   (`N_F≈13`) rather than the far-field two-slit formula PHOTONICS' own
   back-of-envelope estimate misapplied. This is the mechanistic companion
   to item 1: even if the radius sweep confirms `P*` tracks `R_OUT/λ`,
   nobody has yet derived what value it SHOULD track to, from the
   article's own geometry in the correct near-field regime — item 1
   establishes causation, this establishes the actual predictive formula,
   which is what ultimately fixes the realizability tier (published vs.
   plausible) once causation is settled.

Full record reviewed: `experiments/083-t28-pad-article-full-power-retest/`
— `phase1_proposal.md`, `NOTES.md`, `run.py`, `results.json` (spot-checked),
`run_output.txt`, `null_permutation_control.json`, all five Phase-2
critiques, `phase2_redteam_audit.md`, `phase3_synthesis.md`.
