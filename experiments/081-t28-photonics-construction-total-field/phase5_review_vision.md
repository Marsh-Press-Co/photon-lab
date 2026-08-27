# PHASE 5 — REVIEW · VISION SCIENCE · Panel Iteration 58 · exp-081
## Whole-cycle review, fresh context, blind to the other seats' Phase-5 reviews and to any phase5_redteam_audit.md from this cycle

**Seat: VISION SCIENCE** (human perceptual limits — contrast thresholds,
luminance edge detection, spectral sensitivity, adaptation, temporal
sensitivity, attentional blindness; duty: pin numeric thresholds, with
sources, BEFORE any run that scores against them). This cycle engages no
perceptual claim (T1 route N/A, constraint 3 not engaged — the disposition
every T28 cycle since exp-071 has carried, and this cycle's own explicit
framing). My load-bearing duty is therefore, again, a scope-discipline audit
— does anything smuggle a perceptual threshold or constraint-3 language into
the record — plus independent re-verification of the cycle's own numerical
claims from raw code, not from trusting five layers of prose that already
agree with each other.

---

## Verdict on the whole cycle: **PARTIAL**

Concurring with the record's own stated Combined Verdict
(`phase3_synthesis.md` §2/§5, `phase4_results.md`). Item 1 — the first
correctly-built, correctly-scored (total field, real-data free-period fit)
test this nine-cycle T28 y-wall sub-thread has ever run — lands NEITHER
mechanically under both admittance families, sharpened to REFUTE-leaning
substantively once the Red-Team-run ablation control (Phase 2) proves the
lone `C80−C40` SUPPORT survives with zero wall reflectance present. This is
real, cumulative narrowing of the coherent-echo mechanism class, not a
closed boundary: Checkpoint criterion 2 correctly stays NOT YET RIPE (single
construction, single wavelength, empty scene, phase-convention still open).
Nothing here touches constraint 3. On my own independent re-verification
below, the cycle's numerical record is clean — everything I recomputed from
scratch reproduces exactly — and its process discipline (git provenance,
NOTES.md completeness, verdict-field hygiene) is in genuinely better shape
than its own immediate predecessor.

---

## 1. Constraint-3 / perceptual-threshold scoping — NEGATIVE, independently re-run

I ran my own search across the complete `experiments/081-.../` directory —
every `.md`, `.py`, and `.json` file, including the Phase-3/4 material that
did not exist when Phase 1's own compliance note or Phase 2's five blind
critiques were written — for any perceptual or constraint-3 vocabulary:

```
grep -inE "c_thr|contrast|threshold|luminance|photopic|scotopic|weber|lux|
  adapt|glare|perceiv|visib|witness" *.md *.py *.json
```

Every hit traces to one of three harmless categories: (1) "ambient-contrast
channel" (`phase1_proposal.md` ×2) — the inherited *location* name of the
T28 signal (`lab/ambient.py`'s own channel), never a perceptual comparison,
exactly as this cycle's own Phase-2 VISION critique found and as Red Team's
Phase-2 audit independently confirmed by its own `grep -il` sweep; (2)
"threshold(s)" used four times, all as a statistical/algorithmic term (the
`rel_dev` SUPPORT/REFUTE bands, the gate re-run's `n_trials`/significance
bars, `phase4_results.md`'s own discussion of the `0.0075°` rounding-
precision miss) — never a luminance or contrast bar; (3) the Phase-2 VISION
critique's own self-referential lines reporting that it ran this exact
check. **No occurrence anywhere asserts or implies this cycle's arithmetic
bears on constraint 3, and no perceptual threshold (`C_thr` or otherwise) is
invoked, explicitly or implicitly, anywhere in Phase 1 through 4.** This
matches T16's own cautionary precedent (R9, Iterations 53–54) closely enough
to be worth stating plainly: T16's dimensional-error chain started from a
ratio that *did* get divided by `C_thr`; this cycle never does that
division at all, so the R9 failure shape has no foothold here. The "N/A,
constraint 3 not engaged" disposition is correctly and consistently applied
through every phase this cycle produced.

---

## 2. Independent numerical re-verification — re-ran the committed script from scratch

I did not trust `phase1_results.json`/`phase4_results.json`/`NOTES.md`'s own
printed numbers. I re-ran `photonics_construction.py` myself, in place,
against the committed repo state, and diffed the output against every
headline figure cited in the record. Everything reproduces exactly:

- **Item 1** (matched admittance, the primary test): `P*_model` =
  `1.8571°`/`2.0301°`/`2.0150°` vs `P*_real` = `4.6113°`/`4.1761°`/`2.8421°`,
  `rel_dev` = `0.5973`/`0.5139`/`0.2910` → INCONCLUSIVE/INCONCLUSIVE/SUPPORT,
  Combined **NEITHER** — bit-exact match.
- **Item 1b**: `E_direct` PAD-invariance bit-identical (`0.0` across all 5
  configs) confirmed by my own re-run; the pair-delta cancellation residual
  (`~10⁻¹⁴`) reproduces to the printed digit.
- **Admittance rescore** (Red Team's fix-docket item 1, folded into Phase 3):
  matched-vs-realizable period shifts `0.0075188°`/`0.0000°`/`0.0075188°`,
  verdicts unchanged, Combined NEITHER both families. I confirm the ONE
  literal frozen-prediction miss the record discloses (`0.0075188° >
  0.0075°` by `1.9×10⁻⁵°`) is real and exactly as characterized — a
  rounding-precision artifact of a bound copied from a 4-decimal-rounded
  audit table, not a physics discrepancy. This is the same honest-disclosure
  standard item 1b itself modeled (a literal miss reported as a miss, not
  smoothed into a pass), applied consistently a second time in the same
  cycle.
- **Ablation control** (fix-docket item 2): `PAIR_ABSORB40` ablated signal
  is `ss_tot=0.0` exactly (`SS_TOT_DEGENERATE=True`) — genuinely
  `r()`-dependent; `C80−C40` ablated `rel_dev=0.293651` (vs real `0.2910`,
  shift `0.0075°`) — the lone SUPPORT survives losing all wall reflectance
  almost unchanged; `PAIR_PAD` shift `0.150376°`. All three reproduce to the
  printed digit.
- **`conj(r)` sensitivity** (fix-docket item 3): periods shift to
  `2.1278°`/`2.4887°`/`2.2481°`, **zero verdict flips**, confirmed.
- **Phase-divergence figures** (fix-docket item D): item 1's own `[48°,54°]`
  range gives `[8.36°,10.55°]`, matching the audit's cited `8.4–10.6°`. I
  also reproduced the disclosed discrepancy in the `[5°,15°]` precedent-range
  figure (my own re-run: `[54.01°,89.06°]`, vs Red Team's `54.0–83.6°`) and
  confirm `phase4_results.md`'s own explanation — the true maximum grows
  with sweep grid density because `|r|~10⁻⁴` there is ill-conditioned in
  phase — is a legitimate, non-blocking characterization: no frozen
  prediction references that number, and the qualitative point (an
  order-of-magnitude larger phase gap at the near-normal precedent range
  than at item 1's own grazing range) holds under either figure.
- **Energy budget** (item 3): `θ_beam`-convention anchor `1.4943×10⁻³`,
  `theta_local`-convention `1.289×10⁻⁸` (matched)/`2.638×10⁻⁸` (realizable),
  ratio `1.160×10⁵` — all reproduce exactly.

I also scanned `phase4_results.json` programmatically for any `verdict`/
`combined_verdict` field that is missing or empty (the exact defect class
EM found in exp-080's `part_d_photonics_construction()`, and that a prior
VISION Phase-5 seat flagged in that same cycle, §4 of
`experiments/080-.../phase5_review_vision.md`). **None found** — every
scored construction this cycle produces (matched, realizable, ablated,
conj) carries an explicit verdict, consistently.

**Finding: every load-bearing number in this cycle's record is genuine,
reproducible, and honestly characterized where it fell short of its own
pre-registered bound.** No hand-typed figure, no R4-class defect found.

---

## 3. Git-provenance closure — the gap my own seat's Phase-2 self flagged is genuinely fixed, independently re-verified

This cycle's own Phase-2 VISION critique (read in full before writing this)
flagged that `experiments/081-.../` Phase 1 landed as one combined commit
(`ff73016`), unlike exp-080's genuinely separate `6fb6b99`→`23203cc` split —
required change: restore a genuine pre-registration-before-run commit split
at Phase 3. I independently re-ran `git log` and `git diff` myself, not
trusting Phase 3's own "restored" claim:

```
522e9fb  2026-08-27 21:41:50  Phase 3: Director synthesis, FROZEN
                                PREDICTIONS committed before corrected
                                re-run
c2bd9c2  2026-08-27 21:45:50  Phase 4: corrected re-run confirms 6/7
                                frozen predictions
```

A genuine 4-minute gap, and `git diff --stat 522e9fb c2bd9c2` touches only
`NOTES.md`, `_output.txt`, `phase4_results.json`, `phase4_results.md` — the
run's own outputs. `git diff 522e9fb c2bd9c2 -- phase3_synthesis.md` is
**empty**: the frozen-predictions text is provably untouched by the run
that followed it. This directly answers the residual worry my own seat's
Phase-2 critique raised (predictions not independently datable within a
single combined commit) — for Phase 3 specifically, the split is now real
and independently checkable, exactly the standard exp-080 set and this
cycle's own Phase-1 commit fell short of.

**One residual, now-unresolvable point, noted for completeness, not a
current defect**: Phase 1's own single-commit gap (`ff73016`) cannot be
retroactively split — my own Phase-2 self's stated flip condition ("if the
predictions text had in fact been edited after seeing results, I'd oppose")
remains formally unverifiable for Phase 1 specifically, forever, since no
separate pre-run commit for that phase exists or ever will. I find no
positive evidence of tampering (order of file mtimes, and now the clean
Phase-3 split as a revealed-preference argument that this Director does
follow the discipline when structurally able to), and Red Team's Attack 4
correctly showed the single-commit pattern is not actually a regression
from an established norm (exp-079 did the same). I do not weight this
against the cycle's verdict — but record it as the one governance question
this cycle's own record cannot fully close, distinct from the numerical
findings above.

---

## 4. `NOTES.md` completeness

`NOTES.md` exists (unlike exp-080, a gap my own seat's Phase-5 predecessor
caught and required closing — this cycle does not repeat it) and carries
every section CLAUDE.md's own convention requires: **Mandate, Hypothesis,
Setup, Idealizations, Result, Learned, Next** — plus, appended in place
rather than silently overwritten, a **"PHASE 3 — DIRECTOR SYNTHESIS"**
section that explicitly supersedes the pre-audit Result/Learned/Next
language point-by-point (five corrections, each citing which prior claim it
replaces and why) and a **"PHASE 4 — TEST"** section with the confirmed
frozen-prediction table. This is a materially more complete and more
auditable record than a document that had simply been edited in place —
a reader can see exactly what Phase 1 originally claimed, what Red Team's
audit found, and what changed, without reconstructing it from a diff.

---

## 5. One further check specific to my own charter: is "REFUTE-leaning" reasoning free of any accidental appeal to a perceptual look-elsewhere prior?

Item 1c's core move — comparing a recovered period's distance to T21's own
established fringe versus its distance to its own T28 target, and treating
"closer to T21" as evidence of a look-elsewhere artifact rather than a
genuine T28 signal — is a *statistical* look-elsewhere argument (this
program's own R5 discipline), not a perceptual one. I checked specifically
whether any part of this reasoning implicitly borrows a perceptual
"noticeability" intuition (e.g., treating T21's `1.9608°` fringe as more
"visible" or "salient" for reasons resembling contrast sensitivity, which
would be exactly the kind of unscoped implicit perceptual claim my charter
exists to catch). It does not: `rel_dev` is a pure ratio-distance metric on
recovered periods in degrees, computed identically for both references by
the same `rel_dev()` function (independently re-confirmed commensurable by
Red Team's own R9 self-check, §0 item F of `phase2_redteam_audit.md`, which
I re-verified: `1.4943e-3/1.2886e-8=115980`, matching the reported
`1.1597×10⁵` to 4 significant figures). No vision-science concept is doing
any work in this diagnostic, correctly.

---

## Summary

**Verdict: PARTIAL**, concurring with the cycle's own record, arrived at
independently. (1) No constraint-3/perceptual-threshold smuggling anywhere,
re-confirmed by my own fresh grep across the complete file set. (2) Every
headline number I re-derived from a fresh run of the committed script
matches the record exactly, including the one honestly-disclosed literal
miss (`0.0075188°` vs the `≤0.0075°` bound) and the disclosed, non-blocking
phase-divergence-range discrepancy. (3) The git-provenance gap my own
seat's Phase-2 self flagged at Phase 1 is genuinely closed at Phase 3,
independently re-verified by `git log`/`git diff` (a real 4-minute gap, a
clean append-only diff) — Phase 1's own gap remains formally unresolvable
in retrospect but is not evidence of anything, and does not recur. (4)
`NOTES.md` is complete, and no `verdict`/`combined_verdict` field anywhere
in `phase4_results.json` is missing or empty — the exact defect class a
prior VISION Phase-5 seat caught in exp-080 does not recur here. This is a
genuinely well-executed instrument-fidelity cycle.

---

## Ranked top-3 candidate directions for Iteration 59

I know PLAN.md's own Iteration-58 queue (Tier 1: the 750/450nm
wavelength-generality x-wall leg, broadband pulsed reflectance
spectroscopy, the 750nm x-wall two-wall spot-check; Tier 2: the PAD-loaded
real-article check). Both the wavelength-generality leg and the PAD-loaded
real-article check are now entering their **sixth consecutive deferred
T28 cycle** (076–081) as of this iteration's own close.

**On whether a sixth deferral is still defensible: no, not without this
cycle explicitly re-stating why — and this cycle's own record does not do
that.** `NOTES.md`'s own "Next" section names both items as "the board's
own oldest-overdue items, unaddressed by this cycle's own Tier-0 scope" and
asks Iteration 59 to weigh whether continuing to defer them "still has an
explicit, non-inertial reason" — but that is a question posed forward, not
an answer given this cycle. PLAN.md's own Iteration-58 queue text was
explicit that a sixth deferral of the PAD-loaded check specifically "must
again be stated explicitly in that cycle's own synthesis" — and
`phase3_synthesis.md` does not contain that statement anywhere; it defers
by Tier-0 scope choice without addressing the standing instruction
head-on. This is not a Checkpoint-4-shaped defect (no false claim is made,
and the Tier-0 item this cycle executed was itself legitimately the
highest-ranked item on the board) but it is the same "deferred by inertia,
not by stated reason" pattern the board has now been warned about for two
consecutive cycles running.

Ranked:

1. **The PAD-loaded real-article check.** This is explicitly this program's
   own charter-relevant question for my seat (LOGBOOK Iteration 53's own
   ranking named it as such: "VISION's own charter-relevant question, this
   cycle's empty-scene-only scope could not reach"), and it is now the
   single most overdue item on the entire T28 board — every congruent-series
   config across all ten T28 cycles to date, this one included, has been an
   EMPTY scene. This cycle's own sharpened finding (the lone SUPPORT
   requires zero wall physics, proven not merely argued) makes the case for
   running this stronger, not weaker: a construction this thoroughly
   REFUTE-leaning on an empty scene is exactly the situation where checking
   "does anything change with a real absorbing article loaded" is the
   highest-information remaining question, not a lower-priority one. I rank
   this above the wavelength leg because it is the one axis this sub-thread
   has never varied at all, not merely under-sampled.
2. **Extend `phase5_redteam_phase_convention_check.py`'s empirical FDTD
   tie-breaker to 2–3 angles inside `[47.5°,54.5°]`.** This cycle's own
   Red Team audit (Attack 3) found the magnitude-only gate re-run (item 2)
   cannot resolve the `r` vs `conj(r)` sign-convention ambiguity R8 exists
   to guard against, ran a cheap desk-only sensitivity check that shows it
   is NOT outcome-determining THIS cycle, but explicitly left the genuine
   empirical question open and named the exact affordable fix — cheap
   (exp-075's own precedent ran in ~90s), already queued twice now
   (Phase 3 §2 item 3, and again here), and the R8/R6/R7/R9 family of house
   rules exists precisely to stop a named, affordable, un-run check from
   lapsing a second cycle running.
3. **The 750/450nm wavelength-generality leg.** Tests whether this cycle's
   entire REFUTE-leaning finding — the sub-thread's first correctly-scored
   result in nine cycles — is a 600nm-specific artifact or a genuine,
   wavelength-general property of this construction, directly bearing on
   whether Checkpoint criterion 2 can ever be responsibly declared ripe for
   this mechanism class. Ranked third here only because items 1 and 2 are
   both cheaper and more informationally novel (neither has ever been
   tested at all, vs. this leg's own well-established sweep protocol), not
   because it is low-value — it remains, in the record's own words, one of
   the two most overdue items on the whole board.
