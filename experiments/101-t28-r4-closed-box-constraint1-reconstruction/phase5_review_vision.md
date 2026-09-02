# Phase 5 Review — VISION SCIENCE seat (Panel Iteration 78, exp-101)

**SELF-REVIEW.** My own seat led this cycle's Phase 1 proposal. Per this
program's own precedent (self-review seats have repeatedly found real
defects in their own earlier work), I read `phase1_proposal.md` and
`NOTES.md` as a hostile fresh reviewer, not as their defender, and
independently re-derived every load-bearing number below directly from
`results.json` (never from NOTES.md's own prose) with a short Python script
run against the committed file, not typed by hand. Full inputs read in
full before drafting: `phase1_proposal.md`, all five `phase2_critique_*.md`,
`phase2_redteam_audit.md`, `NOTES.md`, `run.py`, `results.json`,
`run_output.txt`, plus `lab/sections.py` (to check the `back_frac`/`p_scat`
face-flux convention directly) and the relevant `LOGBOOK.md` spans (R20's
full text, T2/T3's full text, the Reconciled Iteration-78 queue).

## Bottom line

**CONCUR-WITH-GAPS on the Tier-0 deliverable itself; separately, this
document independently trips the program's own R20 standing rule** (three
or more independent citation/figure/label defects surviving Phase-3 freeze
into Result/Learned/Next, each caught only at Phase 5) — a Checkpoint-4-
grade pattern per R20's own text, regardless of whether any instance is
load-bearing to the scored verdict. None of the five Phase-2 critiques or
Red Team's audit could have caught the two Result-section instances (they
predate Phase 4's run); the third (a mislabeled cross-reference to "T3")
was already present in the Phase-1 proposal and survived all six Phase-2
reviews uncaught. I did not find any defect that would flip Predictions
1, 2, or 4's pass verdicts, and Prediction 3's falsification is real and
correctly diagnosed at the physics level. The closed-box reconstruction
itself — the actual Tier-0 mandate — is sound, correctly implemented, and
a genuine improvement over `beam_behind_t28`.

---

## 1. Independent re-verification of the four predictions' self-scoring

I recomputed every ratio below directly from `results.json`'s 12
`partition_{key}_*` fields (script output retained in this review's working
notes; spot values shown here to the same precision NOTES.md uses).

**Prediction 1** (`sigma_abs/sigma_ext` (BOX_A) ∈ [0.505, 0.520]):
independently recomputed all 12 cells; min = 0.512906 (`C40_R4`, 40.265°),
max = 0.514499 (`C40_R4`, 41.461°). **Matches NOTES.md's stated [0.5129,
0.5145] exactly.** CONFIRMED, no defect.

**Prediction 2** (`back_frac > 0.5` at all 12 cells): recomputed
`back_frac = sigma_scat_downstream/sigma_scat` at all 12 cells; min =
0.5324 (`C40_R4`, 42.961°), matching NOTES.md's endpoints (`0.6536→0.5324`
C40_R4, `0.6529→0.5340` G40_R4) exactly. The `>0.5` verdict is correctly
CONFIRMED. **But the accompanying characterization is not accurate as
stated**: NOTES.md's Result says the two configs are "tracking each other
to 3 decimal places at every angle." The actual per-angle
`|back_frac_C − back_frac_G|` I computed is 0.000713, 0.000074, 0.000662,
0.001602, 0.001602, 0.001557 across the six angles (ascending θ) — at
three of six angles (40.265°, 41.461°, 42.961°) the two configs disagree
in the **third decimal digit itself** (e.g. 0.5812 vs 0.5828), not merely
beyond it. "Tracking to 3 decimal places at every angle" reproduces at
only half the angles; a defensible claim would be "agree to within
0.0007–0.0016" or "agree to 2 decimal places." Minor on its own, but see
§3 for why this is not an isolated case.

**Prediction 3** (`sigma_scat_downstream/312 < 0.15`): independently
recomputed all 12 cells; min = 0.5457, max = 0.6159 — **matches NOTES.md's
stated [0.5457, 0.6159] exactly.** FALSIFIED as stated, correctly reported.
See §2 for a critique of the physical explanation given, and a pre-run
internal-consistency gap none of the six Phase-2 reviews caught.

**Prediction 4** (`box_dev_scat_downstream ≤ 0.12`): independently
recomputed all 12 cells; min = 0.005703, max = 0.045437 — **matches
NOTES.md's stated [0.0057, 0.0454] exactly**, and 0.12/0.0454=2.64,
0.12/0.0057=21.05, matching the stated "2.6×–21× inside the bar." CONFIRMED,
no defect.

**Constraint 2** (`observer_article_norm`, cited as unchanged/clean):
NOTES.md's Result states "`2.26e-4`–`3.95e-4` across all 12 cells." I
computed all 12 `partition_{key}_observer_article_norm` values directly
from `results.json`. **This range does not reproduce.** The true minimum
across all 12 cells is `1.155427e-4`, at `G40_R4`, θ=37.127246° — roughly
**half** the stated floor of 2.26e-4. The cited [2.26e-4, 3.95e-4] is
actually the range of the `C40_R4` subset alone (6 of 12 cells); every one
of `G40_R4`'s six values is lower than 2.26e-4 except the top one
(3.09e-4), and `G40_R4`'s own minimum (1.155e-4) is entirely outside the
stated band. **This is a genuine, source-checkable, wrong figure in the
frozen Result section** — exactly the class of defect R4/R20 exist to
catch (a claimed-exact figure that does not reproduce from its own cited
source). It does not change the qualitative verdict: even the true minimum
(1.155e-4) is still ~173× inside the R18 gate's 0.02 bar, so constraint 2
still reads clean. But the stated range itself is wrong and should be
corrected to `[1.1543e-4, 3.9490e-4]` (all 12 cells) if this document is
amended, or explicitly re-labeled "`C40_R4` range" if that was the intent.

**Thermal sidecar paragraph**: qualitatively correct (`p_abs_w`/
`dt_ss_full_K` do rise monotonically with θ in step with `sigma_abs`, and
all 12 `netd_classification` values are genuinely `UNDETECTABLE` — I
confirmed both directly from `results.json`). The parenthetical "(absorbed
power rising 310→339 W-equivalent-cells as θ increases)" is confusing
rather than wrong: `310→339` is `sigma_abs` (a cross-section in grid
cells, dimensionless once normalized), not `p_abs_w` (actual absorbed
Watts, which is ~2.79e-12→3.31e-12 W across the same six angles — twenty-
four orders of magnitude smaller). "W-equivalent-cells" is not a unit used
anywhere else in this document or, as far as I can find, this bench, and
invites a reader to conflate the two very different quantities. Worth a
one-line fix (say "cells (cross-section units); see `p_abs_w` above for
the actual Watts figures"), not a substantive defect.

## 2. Prediction 3's falsification and its extinction-paradox/Babinet explanation

The physics explanation itself is used correctly and is appropriately
hedged, not overreaching. I checked the size parameter it implicitly
relies on (large-particle/geometric-optics extinction limit): the article
radius `R4_R_OUT=156` cells at `R4_CPL[600]=40` cells/λ gives a physical
radius of 3.9λ, i.e. `ka = 2π·3.9 ≈ 24.5` — comfortably in the regime
where `Q_ext→2` (roughly equal absorbed and diffracted cross-sections) is
expected, so invoking the extinction paradox here is quantitatively
defensible, not just a plausible-sounding excuse. NOTES.md does not state
this size parameter explicitly; doing so would have made the explanation's
applicability verifiable rather than merely asserted — a should-fix, not a
must-fix.

The explanation's own final caveat — that `sigma_scat_downstream` is an
incoherent scattered-power integral that "cannot, by construction,
distinguish 'forward diffraction that cancels the beam in shadow' from
'forward diffraction that refills it'" because that requires phase
information a Poynting-flux magnitude integral discards — is correct and
is the single most important thing in this document. It is NOT overstated;
if anything it under-sells its own implication (see §3).

**A genuine pre-run gap none of the six Phase-2 reviews caught**: Phase 1's
own Prediction 1 already cited T9's finding that `sigma_abs/sigma_ext≈0.51`
exceeds the ≤0.5 Babinet ceiling — i.e., the SAME document already asserted,
before any FDTD ran, that roughly half of this object's extinguished power
must be scattered/diffracted rather than absorbed (`sigma_scat` comparable
in magnitude to `sigma_abs`, i.e. comparable to the object's own geometric
cross-section). Prediction 3, drafted in the same proposal, nonetheless
assumed the *downstream-directed* share of that scattered power would be
a small fraction (<15%) of the object's diameter — i.e., that diffraction
contributes only a minor correction to a small geometric shadow, not a
cross-section of order unity. These two predictions are in tension on
their face: if `sigma_scat ~ sigma_abs ~ O(sigma_ext/2)` for an optically
thick absorber, and `sigma_ext` itself scales with roughly twice the
geometric cross-section in this regime, `sigma_scat` alone should already
be `O(2·R4_R_OUT)`, not a small fraction of it — before `back_frac`'s
downstream/sourceward split is even applied. This was catchable analytically
(a zero-FDTD desk check, the same standard this program applies elsewhere
in the T28 thread) by cross-checking Prediction 3's own premise against
Prediction 1's own cited T9 anchor, in the same document, before committing
either to git. None of MATERIALS (whose sharpest attack was specifically
about T9/Prediction 1), the other four Phase-2 critiques, or Red Team's
audit made this cross-check. NOTES.md's Result section correctly diagnoses
the physics after the fact but frames Prediction 3's failure as a
surprising empirical finding rather than acknowledging it was an avoidable,
same-document internal inconsistency. This is a process lesson worth
naming explicitly for future cycles: when a proposal cites an established
anchor for one prediction, it should be cross-checked against every OTHER
prediction in the same document that shares a dependent quantity, before
either is committed.

## 3. The R20 pattern this document independently trips

Re-read `LOGBOOK.md` lines 799–834 verbatim (R20's full adopted text)
before writing this section. R20: "three or more independent R4-class
defects (a claimed-exact figure, citation, label, or coincidence that does
not reproduce from its own cited source) surviving a document's own
Phase-3 prediction-freeze into its Result/Learned sections, each caught
only at Phase 5 — not earlier — in a single document, constitutes a
Checkpoint-4-grade recurrence pattern on its own, independent of whether
any individual instance is load-bearing to a scored verdict." I count
**three**, independently verified above and below, none flagged by any of
the five Phase-2 critiques or Red Team (I grepped all six Phase-2 documents
for the relevant terms and confirmed zero hits on two of the three; the
third predates Phase 4 and so could not have been caught pre-run by
anyone):

1. Constraint 2's `observer_article_norm` range (`2.26e-4`–`3.95e-4`
   claimed vs. `1.1543e-4`–`3.9490e-4` actual, all 12 cells) — §1 above.
2. The "tracking each other to 3 decimal places at every angle" claim on
   `back_frac` (fails to reproduce at 3 of 6 angles) — §1 above. This is
   the same *shape* as R20's own EM founding-case instance ("a false
   'coincidence' claim between two angles that actually differ by
   3.3368×10⁻⁴°") — a claimed close-tracking that does not hold at every
   point it is claimed for.
3. The "T3" mislabeling — detailed in §4 below, present already in the
   Phase-1 proposal (`phase1_proposal.md` §5, and again §6) and carried,
   uncorrected, all the way through NOTES.md's frozen Idealizations
   (committed at Phase 3, before any FDTD ran) into the post-run Next
   section.

Per R20's own text this fires independent of whether any instance changes
a scored verdict (none of the three do — Predictions 1/2/4 still pass,
Prediction 3 is still falsified, constraint 2 still reads clean either
way). I am flagging this as the Director's action item, not resolving it
myself: R20 says a future cycle exhibiting this density "fires Checkpoint
criterion 4 automatically, no further deliberation," matching PANEL.md's
own Checkpoint criterion 4 ("Red Team flags program-integrity drift").

## 4. "T3" — my own seat's charter, and where Next item 1 gets it wrong

The brief for this review asks specifically whether Next item 1 correctly
identifies what my own eventual constraint-3 instrument will need, and
whether the perceptual-relevance framing is overstated or understated
anywhere. It is both — in different places — and the misattribution here
is squarely my own seat's error, not another seat's.

**The technical proposal in Next item 1 is right and important on its own
terms.** Building "a coherent, phase-resolved downstream point-intensity
instrument (total-field amplitude at a witness-scale standoff, compared
coherently against the empty-scene reference)" is exactly the correct
successor to both `beam_behind_t28` and this cycle's own
`sigma_scat_downstream` — §2 above independently confirms why: an
incoherent scattered-power box integral cannot, even in principle,
distinguish a real shadow from one being refilled by diffraction, because
that distinction is carried in phase, not magnitude. This part of Next
item 1 should stand.

**The cross-reference to "T3" does not.** NOTES.md's Next item 1 calls
this proposed instrument "closely related to, but distinct from, Tier 2's
own still-unbuilt T3 instrument (constraint 3) — worth scoping whether one
construction can serve both." The same claim already appears, verbatim in
substance, in the frozen Idealizations section ("That conversion is exactly
the still-unbuilt T3 instrument," Phase 1 §5, restated in NOTES.md §
Idealizations) — so this did not originate post-run; it was already wrong
in Phase 1 and no Phase-2 critique caught it (I grepped all five
critiques and the Red Team audit for "T3": zero hits in any of them).

I independently re-read LOGBOOK's own T3 entry in full (lines 1066–1106)
and the Reconciled Iteration-78 queue's own Tier-2 line (line 6904–6906,
cross-checked against the packet brief's own citation) before writing this.
**T3, as this program has defined and partially built it since Iteration
16, is specifically the eye's TEMPORAL-contrast (flicker/motion)
sensitivity instrument — scoring a mid-sweep SWITCHING transient (a
mechanism turning on/off as the beam crosses the volume) against
temporal-CSF landmarks and, eventually, `C_thr(L)` composed with a
kinetics trajectory `n(t)` (`lab/temporal_csf.py` + `lab/amplitude_bridge.py`,
suite stages 13/14, partially built at exp-039/exp-040).** It is a
constraint-3/4 JOINT instrument about a TIME-VARYING mechanism, not a
general-purpose "convert an energy quantity into a witness-scale irradiance
for Weber-contrast comparison" instrument. This cycle's own T1 route is
N/A — no σ(I)/σ(x,t) switching mechanism is on the table at all — so there
is no switching transient for T3 to score here in the first place. The
static, at-rest ambient-appearance side of constraint 3 (which IS what a
"downstream irradiance vs. ambient, Weber contrast" framing sounds like)
already has its own, ALREADY-BUILT instrument: `lab/ambient.py` (suite
stage 9, built at Panel Iteration 1 — PANEL.md's own metrics table lists
it as the constraint-3 instrument, separately from "downstream flux
strips," which is constraint 1's own listed instrument for exactly the
"background illumination behind the volume" question Next item 1 is
actually trying to solve).

So "T3" in this document refers to none of: (a) constraint 1's own
still-missing coherent downstream conversion (what Next item 1 actually
proposes — this has no name on the books yet, it is not "T3"), (b)
constraint 3's already-built static instrument (`lab/ambient.py`), or (c)
what T3 actually is (temporal switching-transient detectability). Next
item 1 conflates (a) with (c) via a bare cross-reference, and the "worth
scoping whether one construction can serve both" line invites a future
cycle to go looking for overlap between a downstream-transmission,
single-oblique-plane-wave, steady-state measurement (constraint 1) and a
time-domain, mechanism-switching, temporal-CSF measurement (T3/constraint
3-4) that does not exist beyond the shared, genuinely-transferable
methodological point already stated correctly elsewhere in this same
document: coherent field measurement beats incoherent power-flux
integration whenever the sign of interference matters. That lesson
applies to all three of (a)/(b)/(c) — including my own already-built
`lab/ambient.py` module, which is worth auditing on this same axis in a
future cycle — but it does not make any two of them "one construction."

This is a notable place for a VISION SCIENCE self-review to have caught
this and not another seat's: temporal (flicker/motion) sensitivity is
named explicitly in my own charter text (PANEL.md, seat 6), so
misidentifying T3 — my own seat's own long-running instrument thread — as
something else is a direct hit on my own charter's bookkeeping, not a
tangential slip.

**Recommended correction**, for whoever next touches this file or cites
"T3" from it: drop the "T3" cross-reference from Next item 1 entirely (and
retroactively note the same in a follow-up to the Idealizations section if
this document is ever amended); scope the coherent downstream-intensity
instrument purely as constraint 1's own missing conversion (PANEL.md's
"Background illumination behind the volume" row), independent of both
`lab/ambient.py` and the real T3; and if a future cycle wants to state the
shared "coherent-vs-incoherent" lesson, state it as a lesson, not as grounds
for a shared build.

## 5. What the Tier-0 core deliverable got right (independently confirmed)

- The box-margin gates (Fix 4) are implemented as real, pre-registered
  asserts in `run.py::_verify_box_margins()` (`assert margin_cross >= 90`),
  not merely claimed in prose — confirmed by reading the function, and its
  printed output in `run_output.txt` shows the exact margins (90/136 cells)
  matching the mandatory-fix numbers in NOTES.md's "Changes from Phase 1."
- The `FLOOR_FRAC_SCAT=0.10` amplitude floor (Fix 1/R13) is real,
  executed code (`run.py` lines ~238–270), not an unexercised assertion —
  it happened to pass at all 12 cells (`n_unresolved_by_construction=0`,
  confirmed in `results.json`), but the gate itself is genuine.
  `back_frac`/`fwd_frac`'s shared `p_scat` denominator is `_face_flux`'s
  sum over all four box faces (confirmed directly in `lab/sections.py`),
  not merely the two x-faces — so `back_frac+fwd_frac` summing to well
  under 1 at every angle (0.53–0.65, not ~1) is expected behavior (a large
  lateral/diffuse component through the y-faces), not a bug; NOTES.md
  discloses this qualitatively but never quantifies the lateral fraction
  itself (up to ~47% of `sigma_scat` at some angles) — worth stating as a
  number in a future revision, not a defect.
- `git log` confirms `NOTES.md`/`run.py` (with frozen predictions) were
  committed at Phase 3 (`ae1a7b4`, 03:40:52 UTC) strictly before
  `results.json` was written at Phase 4 (`3c5eb42`, 04:18:55 UTC) — house
  discipline on prediction-freezing was followed.
- `git status`/`git log -- lab/` show no pending or recent `lab/` diff —
  the "zero `lab/` diff" claim is structurally consistent with the repo
  state; I did not re-run the full 41-test trust suite myself (no `lab/`
  change to gate), consistent with `VALIDATION.md`'s own re-run trigger
  (only required after a `lab/` change).
- All 6 mandatory Phase-2 fixes (R13 floor, the false-citation correction,
  R21 thermal narration, R17 box-margin widening, the R3-vs-R4 dedup
  caveat, the T9 disclaimer) are genuinely present in both code and prose,
  not merely asserted — I checked each against `run.py` and NOTES.md's own
  text directly.
- The `pool_rows()`-derived angle re-selection (39.200000° largest,
  42.960901° second) is reused unchanged from Phase 1/Red Team's own
  re-verification; I did not re-run `pool_rows()` myself this cycle (out
  of this review's scope — no new angle claim is made here), but nothing
  in the run or its output contradicts it.

## 6. Ranked candidate directions for the next cycle

1. **(Immediate, no FDTD) Correct this document's three R20-class
   defects** (§1/§3/§4) in place, and have the Director log this pattern
   against R20 in LOGBOOK.md — per R20's own text this should be treated
   as firing Checkpoint criterion 4, independent of the substantive
   verdict on Tier 0 itself, which stands.
2. **Build the coherent, phase-resolved downstream point-intensity
   instrument** (NOTES.md's own Next item 1, correctly scoped): a
   total-field (not scattered-field-only) amplitude/phase measurement at a
   witness-scale standoff downstream of the object, compared coherently
   against the empty-scene reference — scoped purely as constraint 1's own
   missing "background illumination behind the volume" conversion
   (PANEL.md's metric-table row), explicitly NOT badged as "T3" and not
   pre-committed to sharing a construction with either `lab/ambient.py` or
   the real T3 thread. When this instrument is eventually scored against a
   perceptual threshold, it should reuse T2's already-pinned `C_thr(L)`
   function rather than inventing a new one.
3. **Tier 1** (PHOTONICS' zero-FDTD physical-hypothesis check on the
   R3-vs-R4 split), unchanged priority per the Reconciled Iteration-78
   queue — but its own setup should explicitly inherit Red Team's dedup
   finding from this cycle (12/33 R3 rows and 6/35 R4 rows in `pool_rows()`
   are non-independent citation-republished duplicates) so Tier 1 does not
   repeat the same non-independence mistake when it re-examines the
   R3-vs-R4 correlation asymmetry.
