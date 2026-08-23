# Phase 5 — RED TEAM final audit (exp-061 / Iteration 38)

*Fresh sub-agent, receives everything: the full experiment record and
all six blind Phase-5 reviews. Never leads.*

Verified directly, not taken on any seat's word: re-derived τ_true/
α_true/e-fold/OD from first principles; ran `python3 lab/caveat_lint.py`
and `--selftest` (5 caveats, 0 required-site failures, matches all six
reviews); independently reproduced THERMODYNAMICS' corrected-scale
sensitivity table via `lab.thermo_sidecar.mixed_length_scale_regime`
with the program's own standing constants; read `phase1_proposal.md`'s
successor chain, both Phase-2 audits' full text, `caveat_lint_config.json`'s
actual entries, `caveat_lint.py`'s source, `REALIZABILITY_MEMO.md` Entry
2, and all six Phase-5 reviews in full.

---

## 1. Numbered attacks (independent)

**1. [inconsistency]** NOTES.md's own Phase-4 Result section closes
with: "Every verdict above discloses its evidentiary tier ... at the
verdict itself." Read literally against NOTES.md's own five MP bullets
in that same section: **false**. None of the MP-1 through MP-5 bullets
in NOTES.md contain "T18" or "WebSearch-snippet" — only the trailing
paragraph does. True of `phase4_results.md`'s bullets, not of NOTES.md's
own. This is the identical "stated once, elsewhere" pattern the original
Phase-2 catch flagged, now additionally compounded by a false
self-description, not merely relocated.

**2. [inconsistency]** `exp061-t18-evidentiary-tier-propagation`'s
`required_sites=["experiments/061.../NOTES.md"]` never names
`phase4_results.md` — the file its own registry description calls out
as where "a Phase-4 verdict is actually cited from" — and its
`candidate_globs` structurally cannot discover it either. Confirmed
live: `python3 lab/caveat_lint.py` produces zero output mentioning
`phase4_results.md`.

**3. [inconsistency]** The THERMO disposition's "comfortably clear" /
8.1× headline anchors `l_geometric_m=150µm` — MP-2's pre-search
predicted upper thickness bound — while the same document, three
sections earlier, already contains MP-5's actually-found multiple
(230–730× of 1.44µm = 331µm–1.05mm). NOTES.md's own closing line is
asserted, not re-derived. Independently reproduced: at 730×/1.05mm,
worst-case irradiance, 100% ceiling → ΔT=0.01477K, margin=**1.35×**,
not 8.1×. Classification survives (UNDETECTABLE); "comfortably clear"
does not.

**4. [unfalsifiable]** The pre-registered coherence/localization
fallback tests whether a WebSearch snippet *uses* localization/coherence
vocabulary, not whether the underlying near-field-coupling physics was
actually screened for. Bruggeman/effective-medium framing is this
subfield's universal reporting convention regardless of true origin
(QUANTUM's independently-sound point). As executed, the test is close to
guaranteed to read "did not trigger" independent of the actual physics.

**5. [inconsistency, disclosed-judgment-call-not-fully-closed]** The
MP-3/MP-4 exclusion of the black-matrix patent (excluded for being "not
graded enough") runs in the opposite direction from Idealization 4's
exclusion of black-silicon/moth-eye (excluded for being "too graded") —
both exclusions, opposite grounds, same cycle, both happen to preserve
the predicted tier. Each is individually defensible on its own
pre-registered text — but the pattern is never disclosed as a pattern
anywhere in the record.

**6. [inconsistency]** Next item 1's proposed `REALIZABILITY_MEMO.md`
language ("driven by thickness, not rate ... rate is within ~2× of at
least one real ... absorber film") overclaims the rate axis's health for
the actual target class. The true in-class comparator (CNT-forest, best
visible-band figure 2.28×10³ cm⁻¹) misses target by >25×. The "~2×"
figure is true only of the excluded out-of-class candidate.

**7. [inexpressible-adjacent, correctly disclosed as unresolved]**
PHOTONICS flags, cannot resolve (T18-blocked): whether the black-matrix
"OD≥3.0" figure is reflectance-based (as every CNT-class α figure in
MP-1 is converted) or transmission-based. A real, disclosed unknown,
direction unresolved.

**Confirmed clean, not an attack:** T1-scoping propagates correctly into
`phase4_results.md`'s MP-4/MP-5 rows, not just NOTES.md's top. VISION's
smuggled-perceptual-claim grep found nothing. EM's independent
from-scratch τ_true re-derivation confirms the formula and the
`d`-linear-in-`r` claim exactly; the one discrepancy (~8×10⁻⁷ relative,
6dp-rounding) is genuinely cosmetic.

---

## 2. Ruling on Finding 1 (THERMO) — mandatory fix now, not queued

**Mandatory fix required before this cycle closes.** The classification
(UNDETECTABLE) is robust and survives at every scale tested — not a
reversal. But "comfortably clear" is a claim about slack, and that claim
is measurably wrong at the scale this cycle's own Phase-4 result shows
is representative. At 1.35× margin, this disposition is one ~35%
modeling perturbation from crossing into MARGINAL. The fix is cheap
(desk-only, same `thermo_sidecar.py` calls, already computed and
independently reproduced). This program has already paid twice for
exactly this failure mode (`TAU_SHELL=24` unreconciled against exp-060's
9.4026 for two cycles) — shipping this cycle's own analog, in the same
document, on the same shift it was caught, would be inconsistent with
this program's own R4/caveat-propagation discipline.

**Docket:** replace the single 150µm point with THERMODYNAMICS'
four-row sensitivity table (230×/298×/374×/730×) in NOTES.md's THERMO
disposition and Result-section closing line; strike "comfortably
clear"; add a new registry entry ("THERMO disposition length scale must
track MP-5's own resolved multiple, not MP-2's pre-search prediction").

---

## 3. Ruling on Finding 2 (VISION) and the forward tripwire — the
central call

**Does NOT auto-fire Checkpoint criterion 4 this cycle. Two independent
reasons — but this consumes the T18-propagation-caveat's self-catch
grace IN FULL, and a materially tighter tripwire is set below.**

**Textual reason (dispositive on its own).** The tripwire's own wording
requires a recurrence "found again *at a future cycle*," discovered
"*after* Phase 3 has already frozen predictions." Finding 2 was
discovered in Phase 5 of Iteration 38 — the same cycle that registered
the entry at Phase 3. Not a future-cycle recurrence; a second self-catch
within the cycle that introduced the fix, structurally identical in
kind to the original Phase-2 catch (self-diagnosed, before this cycle's
own close-out, by the same discipline — VISION — that caught the first
instance). The tripwire's trigger condition is not met on its face.

**Substantive reason.** The caveat WAS registered — not "a never-
registered caveat gap." It is a `required_sites` scoping gap on an
already-existing entry. Red Team's own Phase-2 mandatory-fix docket item
2 (which authorized this entry) instructed `required_sites` cover
"`phase1_proposal.md` (or its Phase-3 successor) Section 3 ... and the
eventual Phase-4 `NOTES.md`" — written BEFORE Phase 4 ran, before
`phase4_results.md`'s existence as a separate, append-only file (a
structural convention that file's own header establishes, not one
Phase 2 or Phase 3 specified) had been decided. The shipped entry is a
literal, complete execution of what the docket actually asked for at the
time it was written. This is a gap that emerged from a downstream,
Phase-4-time architectural choice the Phase-2 docket could not have
named — not a docketed promise broken by hand-review.

**What this ruling is NOT: a clean pass.** Two things elevate this
above "no action needed": (a) attack #1 — NOTES.md's own trailing
sentence makes a FALSE claim about its own compliance, closer to a
hand-review miss than the registry gap itself; (b) this is the SECOND
T18-propagation coverage gap self-caught within one cycle. Both call for
mandatory correction now (§6 docket), and a NEW, TIGHTENED, non-
negotiable tripwire is set: any further gap in this specific caveat's
coverage — unregistered site, under-scoped `required_sites`, or
within-file location gap — discovered at Iteration 39 or later,
auto-fires criterion 4 with no "different defect species" argument
entertained a second time. The T18-propagation lineage has used its one
self-catch grace period; it does not get a third.

---

## 4. Ruling on the MP-4 mechanism-class exclusion asymmetry

**Mandatory fix: disclose the asymmetry explicitly; do not re-scope the
exclusion criterion itself.**

The exclusion should stand — EM's physical argument (impedance-matching
vs. discrete-pigment ε-discontinuities is a real, load-bearing
distinction) is sound, and there's no better bright line to offer; the
thickness axis (70–350×, anchor-invariant, unanimous across all six
seats) overdetermines MP-4's tier regardless of how this judgment call
resolves. Re-scoping the exclusion criterion now would be new literature
work with no clear payoff given that overdetermination.

But shipping it as a "clean" exclusion, with Next item 1's "driven by
thickness, not rate" language unqualified, is not adequately disclosed —
it lets a future reader (or the permanent `REALIZABILITY_MEMO.md`) infer
the rate axis is healthy for the class this construction actually
targets, when it is not. **Mandatory, cheap fix**: add one explicit
sentence flagging that this cycle's two mechanism-class exclusions run
in opposite directions and both happen to preserve the tier; correct
Next item 1's memo language to MATERIALS' more precise framing.
PHOTONICS' T/R-OD units question and MATERIALS' NiP-black/aerogel
search-plan gap are legitimate but require new search work — correctly
queued to Iteration 39, not mandatory now.

---

## 5. Ruling on QUANTUM's fallback-test critique

**Split ruling: one cheap mandatory fix now, the substantive rebuild
queued.** The proper fix (a physical near-field-coupling numeric
threshold) is real new analysis, not a costless docket line — queue for
Iteration 39. **Mandatory now, zero-cost**: downgrade MP-4's
"coherence/localization fallback did NOT trigger" sub-claim from
CONFIRMED to OPEN in `phase4_results.md` and NOTES.md — a wording
change only, does not touch MP-4's tier, but prevents an overclaimed
CONFIRMED status on an effectively-untested sub-claim from propagating
forward uncaveated.

---

## 6. Final ruling and mandatory-fix docket

**PROCEED-WITH-MANDATORY-FIXES.** MP-4's headline status
(**CONFIRMED — UNOBTANIUM-WITH-PARAMETERS**) stands unchanged: it is
overdetermined by MP-2's thickness axis alone (70–350×, anchor-
invariant, unanimous across all six seats and independently re-verified).
No verdict flip.

**Mandatory-fix docket** (before this cycle's close-out is filed):

1. Replace the THERMO disposition's single 150µm point with
   THERMODYNAMICS' corrected-scale sensitivity table
   (230×/298×/374×/730×); strike "comfortably clear"; add the
   length-scale-staleness registry entry.
2. Widen `exp061-t18-evidentiary-tier-propagation`'s `required_sites`
   to include `phase4_results.md`; correct NOTES.md's Result-section
   closing sentence so it no longer falsely claims inline compliance for
   its own bullets.
3. Add one explicit sentence disclosing the opposite-direction
   mechanism-class exclusion pattern; correct Next item 1's
   `REALIZABILITY_MEMO.md`-bound language on the rate axis.
4. Downgrade MP-4's "fallback did not trigger" sub-claim from CONFIRMED
   to OPEN.
5. Queue, unchanged priority from Iteration 37: EM's `sim.omega` entry,
   THERMO's T25 entry (review alongside item 1's new entry for possible
   consolidation). **Re-ranked up**: PHOTONICS' numeric-value-consistency-
   check tooling gap (§9).
6. Queue for Iteration 39: QUANTUM's physical-coupling-threshold
   rebuild; PHOTONICS' T/R-OD methodology check + interference-stack
   check on the black-matrix candidate; MATERIALS' NiP-black/aerogel
   query set; the standing n_eff=1.04+0.01i primary-source pin
   (T18-blocked, standing watch only).

---

## 7. Overall cycle verdict: **PROMISING**

Overriding the raw 4-2 PARTIAL/PROMISING split, per this program's own
established precedent that the verdict turns on whether a cycle's own
open questions close, not the vote count.

Every one of the four PARTIAL votes is explicit that its findings do NOT
overturn the headline UNOBTANIUM-WITH-PARAMETERS tier or MP-2's
dominant thickness finding — each names a scoped, fixable defect, not a
doubt about the cycle's core deliverable. The substantive numerics are
independently re-verified sound by multiple seats and directly: τ_true/
α_true/e-fold from first principles (EM), all conversion arithmetic
(MATERIALS, QUANTUM, Red Team), the caveat-lint tool's basic function
(all six seats plus Red Team, 0 required-site failures throughout).
Item (B) is real working infrastructure, validated against one genuine
historical case and exercised live across this entire cycle.

What keeps this from a clean PROMISING: two MAJOR findings (THERMO,
VISION) reaching Phase 5 at all is itself a mild negative signal about
this cycle's own quality control — both are cases where a number
computed elsewhere in the same document should have been reconciled by
hand before freeze and wasn't. Worth naming plainly — exactly why the
tripwire in §3 is tightened rather than waived silently.

---

## 8. Checkpoint criteria — explicit ruling, all five

1. **All constraint metrics pass.** Does not fire — zero constraint
   metric scored this cycle.
2. **Proven boundary, gates clean.** Does not fire — a real
   realizability finding, but does not "gate clean" given the two MAJOR
   findings and open judgment calls pending the mandatory-fix docket.
3. **Engine physics beyond validated bench classes.** Does not fire —
   explicitly desk-only, zero FDTD, confirmed by inspection.
4. **Program-integrity drift.** Does not fire — ruled in full at §3.
   Consumes this caveat-lineage's self-catch grace entirely; a
   materially tighter tripwire is now in force for Iteration 39+.
5. **Two consecutive non-advancing iterations.** Does not fire — two
   real, git-committed deliverables this cycle.

**None of the five fire. No Marsh convening required this cycle.**

---

## 9. Ranked top-3 priorities for Iteration 39

1. **Resolve the MP-3/MP-4 mechanism-class ambiguity properly**
   (PHOTONICS #1 + MATERIALS #1 + QUANTUM #2, converging): pin whether
   the black-matrix OD is R- or T-based; check it for substrate-
   interference enhancement; run MATERIALS' missed NiP-black/electroless-
   nickel-black and carbon/graphene-aerogel queries as a genuinely
   comparator-relevant third search class.
2. **Replace QUANTUM's fallback vocabulary-presence test with a
   physical near-field-coupling numeric threshold** — estimate VACNT
   pitch/diameter vs. visible λ from already-in-hand packing-density
   figures and pre-register a coupling-regime threshold.
3. **PHOTONICS' numeric-value-consistency-check tooling gap — re-ranked
   up.** No longer a single-instance concern: this same cycle
   independently demonstrated the identical bug class TWICE
   (`TAU_SHELL=24` vs. exp-060's 9.4026 at Phase 2; `l_geometric_m=150µm`
   vs. MP-5's own 230–730× finding at Phase 5). Two independent
   within-program demonstrations of the same failure shape is exactly
   the escalation pattern that turned the caveat-phrase propagation gap
   into mandatory Item-B tooling this very cycle. Build it before a
   third instance ships.

**Iteration-37 carried items, re-ranked:** EM's `sim.omega` entry —
unchanged priority. THERMO's T25 sidecar-absence entry — bump for
review alongside the new THERMO length-scale-staleness registry entry
(docket item 1); both are now staleness/length-scale-adjacent and may
consolidate into one entry. Standing watch, unranked: primary-source pin
of n_eff=1.04+0.01i (T18-blocked, flagged by MATERIALS, QUANTUM, and
VISION).
