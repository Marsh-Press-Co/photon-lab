# PHASE 3 — SYNTHESIS · Director · Panel Iteration 60 · exp-083

**Role: Director** (synthesizes, does not vote). Read the complete Phase 1
record (`phase1_proposal.md`, `NOTES.md`, `run.py`, `results.json`,
`run_output.txt`, `null_permutation_control.json`), all five blind Phase-2
critiques (MATERIALS, THERMODYNAMICS, PHOTONICS, QUANTUM, ELECTROMAGNETISM),
and Red Team's Phase-2 audit (`phase2_redteam_audit.md`) in full before
writing this. Also read `experiments/082-.../phase3_synthesis.md` as the
direct ancestor's format/discipline model (not copied) and PANEL.md/PLAN.md's
own established precedent for a no-freeze-needed fold-in cycle (exp-079/
exp-080/exp-082's own identical shape: "a confirmatory fold-in, not a fresh
prediction").

---

## 1. Disposition of Red Team's Phase-2 audit

Red Team's ruling: **PROCEED-WITH-MANDATORY-FIXES**, a 6-item prioritized
fix docket (`phase2_redteam_audit.md` §3), zero overrides of any of the five
blind critiques' overall verdicts (all five filed support-with-changes; Red
Team concurs support-with-changes for all five). Two specific substantive
sub-claims — QUANTUM's and EM's own "resolved... genuine partial admixture,
p<0.001" reading of the two-tone finding — are overridden, on the strength
of an independent, from-scratch reversal Red Team ran itself, not merely
argued.

**The Director adopts Red Team's audit in full — all six fix-docket items,
zero overrides.** This is not a rubber stamp. The audit independently
reproduced every existing headline number in `results.json` and
`null_permutation_control.json` bit-exact or to Monte Carlo tolerance
(§0a, 0c, 0f–0g of the audit) before adjudicating anything, then went
substantially beyond what any raising critique attempted:

- It recomputed PHOTONICS' own back-of-envelope two-rim estimate
  independently (§0c: `Δθ=9.4520°`, a `3.326×` miss against `P_edge_A`,
  matching PHOTONICS' own figure almost exactly) and added a genuinely new
  check neither PHOTONICS' critique nor any prior document in this cycle
  ran — a Fresnel-number computation (§0d: `N_F≈13.08`) showing the
  far-field two-slit formula PHOTONICS applied is not even the correct
  regime for this aperture. This sharpens PHOTONICS'/MATERIALS' shared
  attack into a precise, falsifiable statement rather than a vague caution.
- It caught that two independently-converging blind critiques (QUANTUM,
  EM) share a genuinely subtle, real statistical flaw: both built a
  two-tone fit and validated it with a Freedman-Lane full-permutation
  test on residuals that turn out to be highly autocorrelated (lag-1
  `r≈0.93–0.95`, matching a previously-documented exp-074 pattern),
  invalidating that test's own exchangeability assumption. Red Team then
  ran the correct order-preserving circular-shift companion test itself
  (§0j) and found it REVERSES the "resolved admixture" verdict
  (`p=0.581` primary series, not significant) — a materially deeper
  correction than a typical Phase-2-audit override in this sub-thread's
  own history: not a single arithmetic slip, but a shared choice of null
  construction, independently found and independently reversed, correcting
  two independent seats without any self-serving asymmetry.
- It independently verified this cycle's own claimed git-provenance
  restoration at the source (§0e: `git show 06cb96b` confirms `run.py`
  did not exist and no results text was present at the freeze commit),
  rather than taking the write-up's word for it.

This is exactly the kind of rigor this program exists to produce. The
Director adopts the fix docket in full for this reason, matching this
program's own established practice of adopting a non-self-serving Red Team
fix docket in full (exp-080 Iteration 57, exp-081 Iteration 58, exp-082
Iteration 59) rather than re-litigating findings Red Team has already
independently re-derived from primitives.

---

## 2. Why no FROZEN-PREDICTIONS git-freeze cycle is needed this cycle

Every one of the six fix-docket items is a prose/framing correction to an
already-computed, already-independently-verified number — no new FDTD, no
new computed number, nothing whose value is still unknown at synthesis
time:

- Item 1 restates what the primary discriminator's `R²=0.858`/null-control
  statistic does and does not establish, using numbers Red Team already
  computed from data already in `results.json` and its own audit (§0c–0d)
  — no new computation, only corrected prose plus a citation of an
  already-independently-derived Fresnel-number fact.
- Item 2 restates what the two-tone correlation figure does and does not
  establish, citing numbers QUANTUM, EM, and Red Team already computed
  (`R²`/`F`/`p` values, lag-1 autocorrelation, circular-shift `p`-values) —
  no new arithmetic performed by this synthesis.
- Item 3 adds a forward-looking board note (MATERIALS' discriminator) —
  no FDTD, no computed number.
- Item 4 re-scopes an existing concern's framing — no new arithmetic.
- Item 5 states a standing discipline note for *future* FDTD spend; no
  FDTD is spent this cycle.
- Item 6 requires stating, plainly, a verification Red Team already ran
  (`git show 06cb96b`) — no action beyond crediting it in the record.

This is the identical shape PLAN.md's own precedent (exp-079/exp-080,
reaffirmed at exp-082 Iteration 59) establishes for when a fold-in cycle
needs no FROZEN-PREDICTIONS git-freeze: "a confirmatory fold-in, not a
fresh prediction." No new number is committed to git as a prediction here
because no new number is computed here — the fixes are folded directly into
the committed record (`NOTES.md`, `phase1_proposal.md`'s own "PHASE 1
RESULTS" section), then Phase 4 verifies the corrected record accurately
and completely reflects Red Team's own §0 findings.

---

## 3. Fix docket — disposition of all six items

### Item 1 [HIGH] — causal-label overreach corrected

Every "ARTICLE-EDGE DIFFRACTION, confirmed/decisively" sentence in
`NOTES.md`'s headline "Result"/"Learned" sections and `phase1_proposal.md`'s
"PHASE 1 RESULTS" primary-discriminator header and "Combined self-score"
have been replaced in place with: **"matches T28's own long-standing,
unexplained `P_edge_A` family — period-family membership, statistically
decisive and null-controlled (`R²=0.858`, clears a 20,000-trial null with
`p=0.0`), NOT yet demonstrated to be article-intrinsic."** The underlying
statistic is not retracted — it is independently reproduced at minimum four
times (committed run, QUANTUM's critique, EM's critique, Red Team's audit)
and remains the strongest-powered period-family measurement this
nine-cycle-plus sub-thread has produced. Both of Red Team's own §0c–0d
findings are appended in the corrected sections: PHOTONICS' own far-field
two-rim estimate misses the recovered period by 3.3× (`9.45°` vs `2.84°`),
AND this aperture's own Fresnel number (`N_F≈13`) means the far-field
formula wasn't even the right one to apply — so this is an **untested
regime**, not a clean refutation of a rim-diffraction origin either. This
is not a close call on the label: five of five blind critiques (MATERIALS
and PHOTONICS directly; THERMODYNAMICS, QUANTUM, and EM by not disputing
it) and Red Team's own independent recomputation converge on the same
correction.

### Item 2 [HIGH] — "resolved... genuine partial admixture" claim overridden

QUANTUM's and EM's "resolved... genuine partial admixture, p<0.001"
language is NOT adopted anywhere in the corrected record. `NOTES.md`'s
"Result" and "Learned" sections and `phase1_proposal.md`'s correlation
discussion and "Combined self-score" now state both readings explicitly:
the naive Freedman-Lane full-permutation test found the two-tone admixture
highly significant (`p<0.001`, corroborated `p=0.00018` in EM's field
companion), but Red Team's own from-scratch verification found the
underlying residuals highly autocorrelated (lag-1 `r≈0.93–0.95`) —
invalidating that test's own exchangeability assumption — and the correct,
order-preserving circular-shift companion test REVERSES the finding
(`p=0.581` for the primary series, `p=0.097` for EM's own field-difference
companion; the observed `F`-statistic sits below the null distribution's
own median). This is now stated explicitly, in both `NOTES.md` and
`phase1_proposal.md`, as an **open question requiring a properly
pre-registered null-calibration test** (matching R6's own Iteration-50
addendum standard) at Iteration 61 — not a settled finding either way, and
specifically not settled in the direction either QUANTUM's or EM's own
critique claimed.

### Item 3 [HIGH] — MATERIALS' article-radius discriminator named as Iteration-61 top priority

Added explicitly, in `NOTES.md`'s "Next" section and in `phase1_proposal.md`'s
corrected causal-framing paragraph: an `R_OUT` sweep at fixed `PAD`
(re-running the identical `PAIR_PAD` harness at an alternate article
radius, holding every other geometry parameter fixed, checking whether
`P*` tracks `R_OUT/λ` or stays pinned) is now this sub-thread's single
highest-priority item for Iteration 61 — sharpened, not merely confirmed,
by Item 1's own downgrade of the causal label: it is the only test that can
move Branch B from a period-family match to a demonstrated causal claim, in
either direction. Per this task's own instruction, this is recorded in
`NOTES.md`'s "Next" section; the corresponding `PLAN.md` board edit is the
Director's own separate Phase 5 job, not part of this Phase 3/4 pass.

### Item 4 [MEDIUM] — energy-interception concern re-scoped

Re-scoped in `phase1_proposal.md`'s idealization 6 and `NOTES.md`'s
"Learned" section to state precisely: `P_edge_A`'s own physical origin,
under ANY reading (article-intrinsic or not), has never been shown
non-dissipative — this is a pre-existing, broader gap in the founding
periodicity's own characterization that this cycle's own Branch-B language
does not specifically create or worsen, only makes newly live because it
is, for the first time, scored on a channel with a real absorbing article
present.

### Item 5 [MEDIUM] — R5 pre-registration discipline note logged

Logged explicitly in `NOTES.md`'s "Learned" and "Next" sections: EM's own
finding — the null-permutation control that actually validates the primary
discriminator against look-elsewhere concerns appears only in the RESULTS
section, not in §4a's own pre-registered gate — is real, non-outcome-
determining given the enormous margin (`R²=0.858` beats the null's own
maximum, not merely a percentile), but is now a recurring pattern across
nearly every T28 cycle since R5's Iteration-47 adoption (exp-069 Block
MINI, exp-070, exp-077, and now exp-083). Per Red Team's own framing, this
earns a **discipline note, not a new formal rule**: future T28 cycles using
`free_period_with_widening`/`_free_period_search` should pre-register their
own null-permutation control in the SAME freeze commit as the falsifiable
bands, closing this now-multi-cycle gap for good rather than re-disclosing
it every time.

### Item 6 [LOW] — git-provenance restoration credited explicitly

Added, in `NOTES.md`, an explicit sentence crediting that this cycle's own
git-provenance restoration — frozen predictions committed at `06cb96b`,
strictly before `run.py` existed or any FDTD call executed — is
independently verified genuine at the source by Red Team's own audit
(`git show 06cb96b:experiments/083-.../run.py` → confirms the file did not
exist at that commit; `git show 06cb96b:...phase1_proposal.md` → confirms
no results text was present either). The two-cycle-old tripwire (exp-081,
exp-082) is correctly discharged. Stated plainly, matching this program's
own R4 standard for how a "restored" claim earns trust — verified, not
merely asserted.

---

## 4. Corrected headline framing (what this cycle's result means now)

**The mechanism-identity power deficiency exp-082 left open is resolved —
but only at the period-family level, not the causal level.** At full
(31-point) statistical power, `delta_scene`'s dominant periodicity is
shown, decisively and doubly-instrument-corroborated (Weber-contrast
pair-fit and EM's independent linear field-difference pair-fit, each
clearing its own fresh null-permutation control), to belong to T28's own
long-standing, unexplained `P_edge_A` period family — not to the
`PAD`-tied `P_continuity` family Iteration 53 characterized as lossless on
the empty scene. That is a real, hard-won, first-of-its-kind finding for
this nine-cycle-plus sub-thread: it is the first time the article-loaded
channel's own dominant periodicity has been statistically pinned down with
confidence.

**What it does not mean:** it does not mean a new "article-edge
diffraction" mechanism has been discovered and confirmed. `P_edge_A` is
itself unexplained — nine-plus dedicated mechanism-search cycles have
refuted every domain-echo candidate for it on the empty scene, and nobody
has ever derived it from geometry, including this cycle. Landing on it
specifically most plausibly means the article-loaded channel inherited the
SAME unexplained artifact the empty scene already produces. PHOTONICS' own
far-field rim-diffraction estimate misses by 3.3×, and the aperture sits
deep in the near-field/Fresnel regime where that formula does not apply
cleanly — so this is a genuinely untested causal regime, not a settled
mechanism either way.

**It also does not mean the two-tone `PAD`-continuity admixture question is
closed, in either direction.** Two blind critiques found apparent
significance for a coexisting `PAD`-continuity component under a
full-permutation null; Red Team's own independent verification found that
null invalid for these residuals and reversed the finding under the
correct, order-preserving companion. Phase 5 reviewers should read this as
a genuinely open, correctly-flagged methodological caution — a real finding
in its own right, with implications for how this program should run any
future nested-model significance test at small n — not as evidence either
for or against mechanism admixture.

**Net: this cycle answers "which established period family dominates?"
cleanly and for the first time. It does not yet answer "is that family
caused by the article itself?" or "is a second, weaker mechanism also
present?" — both are now sharply-defined, board-ranked open questions for
Iteration 61, not loose ends.**

---

## 5. Gates

Zero `lab/` changes this cycle (Phase 1, Phase 2, or this Phase 3/4 pass) —
confirmed by `git diff --stat -- lab/` (empty) and re-confirmed at Phase 4
below. The house trust suite (`lab/validation/run_all.py --only
12346789`) is re-confirmed green at Phase 4. No `lab/` diff this cycle means
no new trust-suite stage is required by house discipline.

## 6. Checkpoint ruling (re-reasoned through by the Director; no criterion
## changes from Red Team's own Phase-2 ruling)

- **Criterion 1**: N/A — zero constraint-3 engagement, T1 stated N/A
  throughout, confirmed by direct inspection of both corrected documents.
- **Criterion 2**: N/A, not merely not-yet-ripe — reasoned through
  explicitly by Red Team's own audit (§4) and re-confirmed here: this
  cycle's findings, including the two-tone reversal, are entirely about
  artifact attribution and null-construction validity inside this lab's
  own FDTD instrument — a statistics-and-methodology finding, not a claim
  touching any phenomenon-program constraint or escape route.
- **Criterion 3**: N/A — zero new `lab/` machinery in the committed run
  (`assert_lab_clean()` passed, `run_output.txt`); this audit's own
  verification scripts are session-local scratch, touching nothing under
  `experiments/083-.../` or `lab/`.
- **Criterion 4**: does not fire — conditioned explicitly, per Red Team's
  own ruling, on this document adopting the fix docket in full, which it
  does. Neither overclaim (the causal label, the two-tone "resolved"
  reading) reaches the permanent record unqualified.
- **Criterion 5**: not at risk — this cycle resolves the period-family
  power deficiency exp-082 left open, delivers the sub-thread's first
  properly-powered article-loaded period discriminator, and — via Red
  Team's own Attack 2 — produces a genuinely new, independently-verified
  instrument-caution finding (residual autocorrelation invalidating a
  permutation null's exchangeability assumption on this exact
  construction) with implications beyond this one result.

## 7. Git provenance for this cycle

Per §2/§5 of this document: no FROZEN-PREDICTIONS freeze-then-run split is
needed, because every fix is a prose/framing correction to already-computed,
already-independently-verified numbers — the same shape PLAN.md's own
established precedent (exp-079/exp-080, reaffirmed exp-082 Iteration 59)
establishes for when a fold-in cycle needs no such split. This document, the
corrected `NOTES.md`/`phase1_proposal.md`, and everything else touched this
cycle are committed together as ONE commit — stated explicitly in the
commit message, citing this exact reasoning.

Full record: `experiments/083-t28-pad-article-full-power-retest/` —
`phase1_proposal.md`, `NOTES.md`, `run.py`, `results.json`,
`run_output.txt`, `null_permutation_control.json`, all five Phase-2
critiques, `phase2_redteam_audit.md`, and this document.
