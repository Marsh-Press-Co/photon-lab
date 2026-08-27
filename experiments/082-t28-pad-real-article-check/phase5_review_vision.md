# PHASE 5 — REVIEW · VISION SCIENCE · Panel Iteration 59 · exp-082
## Whole-cycle review, fresh context, blind to the other seats' Phase-5 reviews and to any phase5_redteam_audit.md from this cycle

**Seat: VISION SCIENCE** (human perceptual limits — contrast thresholds,
luminance edge detection, spectral sensitivity, adaptation, temporal
sensitivity, attentional blindness; duty: pin numeric thresholds, with
sources, BEFORE any run that scores against them). This cycle's T1
disposition is N/A (instrument-fidelity/generalization work, zero
constraint-3 engagement) — but it is also the first cycle in this whole
nine-cycle T28 y-wall/PAD sub-thread to touch my own charter directly:
Iteration 53/54/55's own PAD-sensitivity finding is, for the first time,
measured on the real, article-loaded Weber-contrast channel every
constraint-3 citation this program has ever issued actually uses, and the
task brief assigns me a specific, checkable arithmetic duty — independently
recompute the secondary-metric comparator from scratch, because a prior
VISION seat's own Phase-2 "correction" of a naive comparator was itself
caught arithmetically wrong by Red Team. That correction-of-a-correction is
exactly R9's own subject matter, one cycle after R9 was adopted for the
first instance of this same failure shape (T16's "24×"). I read the
complete record fresh and re-derive every number below from primitives, not
from trusting any prose layer that already agrees with itself.

---

## Verdict on the whole cycle: **PARTIAL**

Concurring with the record's own corrected framing (`phase3_synthesis.md`
§4, NOTES.md's corrected "Result"/"Learned"). The primary metric
(`ratio=A_scene/A_empty=0.6573`) is a genuine, decisive, bit-exact,
pre-registered SURVIVES — a real measurement that a comparable-*scale*
version of the empty-scene PAD-sensitivity confound reaches the real,
article-loaded scoring channel, for the flagship strongly-absorbing article
specifically. This discharges a standing six-cycle tripwire and is the
sub-thread's first-ever article-loaded FDTD measurement in nine cycles —
genuine advancement, not inertia. But the deeper, more consequential
question — whether this is the SAME lossless phase-interference mechanism
Iteration 53 characterized empty, merely observed through the article's own
shadow term, or a qualitatively different article-mediated interaction of
similar scale — is honestly shown, not merely left open, to be
UNRESOLVABLE at this cycle's own 7-point statistical power (four
independent lines of evidence, Red Team's Phase-2 audit §0d–k, adopted by
Phase 3 without softening). Nothing here touches constraint 3 directly; the
article tested sits ~100× past `C_thr` by design, so this cycle's own
numbers say nothing yet about whether the confound could ever flip a real
PASS/MARGINAL call. PARTIAL is the correct word for a cycle that lands a
real, disciplined, honestly-scoped positive finding on one narrow question
while proving — not merely admitting — that a materially more important
question is currently unanswerable with the data in hand.

---

## 1. Independent recomputation of the secondary-metric comparator (task-assigned duty)

I did not trust the ≈5.5× / ≈2.77× / ≈0.12× figures as printed anywhere in
the record — including Red Team's own audit — and rebuilt all three from
raw primitives myself.

**Step 1 — `A_scene` and `C_thr`.** From `results.json` directly:
`A_scene = ptp(delta_scene) = 0.0034076196723707985`,
`C_thr = gs.c_thr(3.0, 0.4, bar="lab") = 0.005` (I called the real function
myself, not the cached JSON value — reproduces `0.005` exactly).
`A_scene / C_thr = 0.6815239344741597` — matches the record's own
`0.6815` bit-for-bit.

**Step 2 — T16's raw numerator, re-derived from the fitted-carrier
primitives, not copied.** I loaded `experiments/072-t28-differential-
beat-fit/run.py`'s own `analyze_pair` (the exact, unmodified function this
whole sub-thread's `amp_ratio` channel is built on) and ran it myself
against `experiments/076-.../results.json::headline`'s raw 31-point
`C40`/`G40` arrays — the same primitive data, re-fit from scratch, not the
cached `A_i`/`A_q`/`amplitude` values:

```
A_i = 0.0006081146443953447
A_q = -9.377432678008948e-05
amplitude = 0.005154759403028982
sqrt(A_i^2 + A_q^2) = 0.0006153024013370462
amp_ratio = 0.11936588174716538   <- matches results.json's classification.x
                                       ("x = amp_ratio(PAIR_PAD) = 0.11936588174716538")
                                       bit-for-bit, confirming my re-fit is correct
```

`T16_raw = √(A_i²+A_q²) = 6.153024×10⁻⁴` — this is the amplitude of a
**fitted sinusoid**: a coefficient pair `(A_i,A_q)` from a `c0 + A_i·sin(·)
+ A_q·cos(·) + …` OLS design describes a single-sided **peak** deviation
from the fitted mean, not a peak-to-peak span. `A_scene`, by contrast, is
`np.ptp()` of 7 raw sampled points — a **peak-to-peak** quantity by
construction (`max−min`). These are not the same convention, and dividing
one by the other directly is a category error the task brief correctly
flags.

**Step 3 — the three comparators, computed independently:**

| Comparator | My independent computation | Cited figure | Match? |
|---|---|---|---|
| T16 historical (`T16_raw/C_thr`) | `0.0006153024013370462 / 0.005 = 0.12306048` | ≈0.12× | **YES** |
| Naive (`A_scene/T16_raw`, no convention conversion) | `0.0034076196723707985 / 0.0006153024013370462 = 5.538122` | ≈5.5× | **YES** |
| Properly like-for-like (`A_scene / (2×T16_raw)`) | `0.0034076196723707985 / 0.0012306048026740925 = 2.769061` | ≈2.77× (Red Team) | **YES** |

**Which comparator is correct, per the task's own instruction to convert
peak-to-peak vs. peak conventions before dividing**: a sinusoid with peak
(single-sided) amplitude `X` has peak-to-peak span `2X`. To compare
`A_scene` (already ptp) against `T16_raw` (a peak), `T16_raw` must first be
doubled to its ptp-equivalent — **not** divided directly. Doing that
conversion gives `A_scene / (2×T16_raw) = 2.77×` — my own independent
number, matching Red Team's own re-derivation (`phase2_redteam_audit.md`
§0l, Attack 5) to 4 significant figures, and I verify algebraically it is
the *only* self-consistent reading: halving `A_scene` to a peak-equivalent
instead of doubling `T16_raw` to a ptp-equivalent gives the identical ratio
(`0.0017038.../0.0006153... = 2.769`), as it must.

**My own independent finding: ≈2.77× (Red Team's re-derivation) is the
correct comparator.** The naive ≈5.5× is not a wrong number — it reproduces
exactly — but it is the WRONG quantity, a ptp divided by a peak with no
conversion, exactly the R9 failure shape applied a second time in this same
sub-thread's history. The ≈0.12× figure is not a comparator to `A_scene` at
all — it is a different measurement entirely (T16's own empty-scene-only
`amp_ratio` numerator against `C_thr`, Iteration 54/R9, with no `A_scene`
term in it anywhere); citing it as a third "comparator" alongside the other
two, as the corrected record does, is defensible only because it is
explicitly labeled as measuring something different (T16's own historical
reading, not an exp-082 cross-comparison) — I confirm the record's own
table (`phase3_synthesis.md` §Item 3) does label it that way, correctly,
not as a peer figure to the other two.

I also independently confirm the record's own disposition of the original
VISION Phase-2 "≈4.2×" figure: **I could not reconstruct 4.2 from the
stated operands under any reading either** — `A_scene / (2×T16_raw)` is
algebraically forced to `2.77`, not `4.2`, regardless of which side of the
ratio the factor of 2 is applied to. The prior seat's diagnosis (a
ptp-vs-peak convention mismatch) was correct; its own arithmetic executing
that diagnosis was not, and Red Team's override (adopting ≈2.77×, not
≈4.2×) is the right call, independently re-confirmed here by a third
computation from scratch.

---

## 2. Item 3's fix — relabeling and the "different KIND of quantity" argument

**Relabeling, verified present and unambiguous.** `phase1_proposal.md`'s
corrected "PHASE 1 RESULTS" section states the secondary metric is
"**Relabeled as an instrument-uncertainty-budget number, NOT a
perceptual-detectability claim**." `NOTES.md`'s corrected "Result" section
carries the identical framing ("relabeled per Phase 3 as an
instrument-uncertainty-budget number, not a perceptual-detectability
claim"). `phase3_synthesis.md` Item 3 states it a third time, in the
Director's own voice, with the operative sentence: "Each figure measures a
different thing; none is a claim that the artifact itself is 'N% of the way
to visible.'" This is the correct fix for exactly the risk my own charter
exists to catch — a raw ratio to `C_thr` reads, to an unguarded eye, as a
percent-of-visible-threshold claim, and it is not one here (`A_scene`
answers "how much does a domain-construction choice move the scored
number," not "how much of the way to a detectable edge is this").

**The "different KIND of quantity" argument, verified present, correctly
reasoned, and correctly sourced.** `phase1_proposal.md`'s corrected section:
"`C_thr` is a static-scene JND threshold; `A_scene` is peak-to-peak of a
*difference between two numerical domain-treatments* of the same scene,
swept across angle — no human views that quantity directly. Units match
(both dimensionless Weber contrast) but the KIND of quantity does not."
`phase3_synthesis.md` Item 3 restates it near-verbatim: "a different KIND
of quantity even though the units (dimensionless Weber contrast) match."
This is the right distinction and I independently confirm it traces to a
real, previously-named precedent, not an invented one this cycle: LOGBOOK's
own T3 thread ("`C_thr(L)` is a static-target threshold applied to a
physically transient event," cited by name in the original VISION Phase-2
critique and confirmed by Red Team's Attack 4 as "correctly identified and
matches this program's own T3 precedent"). `C_thr` is T2's pinned Weber-JND
for one steady scene viewed at fixed adaptation (Blackwell/Rose-type
calibration, per this bench's own established convention); `A_scene` is a
*swing across a discrete angular sweep of an already-differenced quantity*
— structurally the same category error T3 named for a transient event, now
correctly recognized for a swept-domain difference. No human observer, in
any adaptation state, ever looks at "`A_scene`" as a viewed scene — it is
an artifact of comparing two simulated domain constructions, not a radiance
pattern reaching a retina. I find nothing in the corrected record that
backslides into treating `A_scene/C_thr=0.68` as a literal visibility
fraction anywhere — a direct grep of `phase1_proposal.md`/`NOTES.md`/
`phase3_synthesis.md` for "visible"/"invisible" adjacent to `A_scene` or
`0.68`/`0.6815` returns zero hits outside of explicit "NOT a... claim"
disclaimers.

**One clarification I add, not a defect**: because `A_scene` is measured on
the flagship article (`C(G40,article)≈−0.556`, ~100× past `C_thr` in
absolute terms already), even the correctly-labeled instrument-uncertainty
number (`0.68×C_thr`) says nothing about whether *this specific object* is
perceptible — it plainly is, by a huge margin, with or without the
PAD-artifact wobble riding on top of it. The number's only honest use is
exactly as labeled: a bound on how much a domain-construction choice could
move a *near-threshold* citation, hypothetically, if the same absolute
wobble scale transferred to a weaker article — which is precisely why the
near-null-article follow-up (§4, below) is the test that would make this
number perceptually load-bearing rather than merely diagnostic. The
corrected record does not overclaim this either way; I record it here for
completeness, matching Red Team's own Attack 2 disposition (MATERIALS'
article-generality gap) from an adjacent angle.

---

## 3. Record hygiene audit

**NOTES.md**: complete. Hypothesis, Setup, Result, Learned, Next are all
present and populated, with the pre-audit "Learned" items 1–2 explicitly
marked as corrected by Phase 3 and the corrected text standing in their
place (not silently overwritten — the document states plainly which prior
claim each correction replaces). "Next" names four concrete, specific
follow-ups (near-null article, full 31-point window, `PAIR_ABSORB40`/
`C80−C40`, R3-grade settling) rather than a vague placeholder.

**Verdict fields**: appropriately populated at every stage. Phase 1's
self-scored VERDICT (SURVIVES, mechanically) is stated in
`phase1_proposal.md`, correctly labeled as superseded-in-part by the
Phase-3 correction that follows it in the same section (not deleted,
appended — I can read exactly what changed and why). `results.json` itself
carries an explicit `"verdict": "SURVIVES"` field, non-empty. The x-wall
refit and phase-convention-extension riders each carry an explicit
self-scored disposition ("closed for this cycle" / "GENUINELY
INCONCLUSIVE, not a tie-breaker") rather than a bare number with no
verdict attached — I checked both `x_wall_refit_results.md` and
`phase_convention_extension_results.md` directly for this, not merely their
JSON. No empty or missing verdict field found anywhere in this cycle's own
record.

**T1-N/A disposition**: consistent. Stated once, explicitly, in
`phase1_proposal.md` §3 ("N/A... instrument-fidelity/generalization work,
not a constraint-3 mechanism candidate") and applied without contradiction
everywhere else — `NOTES.md` defers to it rather than restating it
(matching the sub-thread's own established convention, e.g. exp-076/
exp-081), and I independently grepped the complete directory for any place
a scored `C`/`C_empty`/`ratio` value is used as evidence for or against a
T1 escape route: none found. `phase2_redteam_audit.md` §4 (Criterion 1
ruling) independently confirms the identical result. I find nothing to add
here beyond what Red Team's audit already established — a genuinely clean
disposition, not merely asserted.

**One residual hygiene note, not load-bearing**: the same git-provenance
gap the original VISION Phase-2 critique flagged (commit `5bb78df` bundles
pre-registered predictions with an already-27/29-complete run — confirmed
and sharpened by Red Team's own Attack 6) is real and correctly disclosed,
but it is a *procedural* finding, not a record-*completeness* one — I note
it here for cross-reference rather than re-litigating it, since Red Team's
audit and Phase 3 (Item 5) already dispose of it fully and correctly (not a
rules violation, given PANEL.md's mandate binds Phase 3's freeze
specifically; flagged as a two-cycle pattern not to recur a third time).

---

## Summary

**Verdict: PARTIAL.** The primary SURVIVES result is genuine, decisive, and
correctly scoped after Phase 3's corrections. My own independent
recomputation of the secondary-metric comparator — rebuilt from raw
`A_i`/`A_q`/`amplitude` primitives via `analyze_pair`, not copied from any
prose — confirms all three cited figures reproduce exactly (≈5.5× naive,
≈2.77× properly like-for-like, ≈0.12× T16's own unrelated historical
reading), and confirms Red Team's ≈2.77× is the one correct comparator once
peak-to-peak and peak conventions are properly reconciled — the original
VISION Phase-2 "≈4.2×" figure is not reconstructable from its own stated
inputs under any reading I could find. Item 3's fix (relabeling as an
instrument-uncertainty-budget number; the "different KIND of quantity"
JND-vs-swept-domain-difference argument, correctly tied to the pre-existing
T3 precedent) is present, clearly stated, and not backslid anywhere in the
corrected record. Record hygiene is clean: NOTES.md complete, every verdict
field populated at every stage, T1-N/A disposition stated once and applied
consistently with zero contradictions found.

---

## Ranked top-3 candidate directions for Iteration 60

1. **The near-null σ(I) article follow-up** (MATERIALS' own flip condition,
   Red Team Attack 2; `off_pass`, `τ_off≈0.0065`, exp-032/exp-034) — rerun
   the identical `PAIR_PAD`/C40–G40 harness with `build_article` replaced by
   this near-threshold construction in place of `graded_black_shell`. This
   is the single test that converts this cycle's own correctly-labeled
   *instrument-uncertainty-budget* number into a genuine
   *perceptual-detectability* question — my own charter's central concern.
   The flagship article's own `C≈−0.55` sits so far past `C_thr` that the
   PAD-wobble's absolute scale is currently diagnostic only; a near-null
   article is the one case where the same absolute wobble could plausibly
   sit close enough to a real PASS/MARGINAL boundary to matter. Ranked
   first because it is the only queued item that could change what this
   whole nine-cycle sub-thread's findings mean for an actual constraint-3
   citation, not merely for the instrument's own characterization.
2. **The full 31-point/0.2° window at the same `PAIR_PAD` pair** (already
   named in `NOTES.md`'s "Next," near-unanimous across the Phase-2
   critiques that raised the correlation concern) — the single test that
   would give the free-period search the statistical power Red Team's own
   audit shows this cycle's 7-point reduction demonstrably lacks (four
   independent lines of evidence, §0d–k). Ranked second, just behind item
   1, because it resolves a real open question (is this the SAME mechanism
   or a new one) that determines how cautiously future near-threshold
   citations at this geometry should be read — directly informs how much
   weight item 1's own result, once run, should carry.
3. **Extend the real-article check to `PAIR_ABSORB40`/`C80−C40`** (named in
   `NOTES.md`'s "Next," Idealization 3) — this cycle tested only the
   dominant `PAIR_PAD` pair; whether the same SURVIVES-mechanically /
   mechanism-open pattern holds for the other two established empty-scene
   pairs is untested, and a real-article generalization claim across "the
   PAD/ABSORB axis" (as opposed to one pair of it) needs this leg before it
   can be stated. Ranked third, below items 1–2, because those two more
   directly bear on whether this whole line of measurement is perceptually
   load-bearing or purely an instrument-characterization exercise — the
   question my own charter is most directly positioned to weigh.
