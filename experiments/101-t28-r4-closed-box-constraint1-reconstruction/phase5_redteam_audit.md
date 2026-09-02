# Phase-5 FINAL AUDIT — RED TEAM seat, Panel Iteration 78 (exp-101)

Fresh sub-agent. I am the only seat this cycle that received the complete
record: `phase1_proposal.md`, all five `phase2_critique_*.md`,
`phase2_redteam_audit.md`, `NOTES.md`, `run.py`, `results.json`,
`run_output.txt`, and all six `phase5_review_*.md` files. Per charter #7,
I speak last, defer to no one, and independently re-verified every
load-bearing claim below from primitives (`results.json`, `run.py`,
`lab/sections.py`, `lab/fdtd2d.py`, `lab/qext_theory.py`,
`experiments/002-cross-sections/results.json`,
`experiments/034-.../REALIZABILITY_MEMO.md`, `LOGBOOK.md`'s R20/R21/T3
text, `experiments/069-.../design_geometry.py`) with my own scripts run
against the actual committed files — nothing here is taken on any
reviewer's word, including my own reading of the brief. I additionally
re-ran `lab/validation/run_all.py --only 12346789` live this session:
**41/41 green**, confirming the "trust suite unchanged" claim directly
rather than by restatement. `git log` on `NOTES.md`/`run.py`/`results.json`
confirms Phase-3 freeze (`ae1a7b4`, 03:40:52 UTC) strictly precedes the
Phase-4 results commit (`3c5eb42`, 04:18:55 UTC) — house discipline on
prediction-freezing held.

**Bottom line up front:** the Tier-0 deliverable is sound, correctly
scoped, and a genuine instrument improvement. Four predictions were
honestly scored (three CONFIRMED, one correctly FALSIFIED with the right
qualitative physics). No constraint (1-4) was violated or quietly
touched. **But standing rule R20 fires this cycle — the first time R20's
own automatic clause has actually triggered a Checkpoint** — and
Checkpoint criterion 4 fires as its direct, textually-mandated
consequence. This is not a close call decided by inertia; the math is
below.

---

## 1. Central task: does R20 fire?

### 1.1 R20's text, re-read in full before ruling (`LOGBOOK.md` lines 799-844)

Three-or-more independent R4-class defects (a claimed-exact figure,
citation, label, or coincidence that does not reproduce from its own
cited source) surviving a document's own Phase-3 freeze into its
Result/Learned sections, each caught only at Phase 5, fires Checkpoint
criterion 4 automatically — "no further deliberation" — with the
"known" precondition explicitly discharged by the rule's own text, not
by a prior cycle's named instance. exp-099 (the founding case) did NOT
fire on itself (grace period, matching every prior R-rule's precedent).
**exp-101 is a later cycle already bound by the adopted rule — if it
independently meets the bar, it fires, full stop, no grace period left
to spend.**

I independently confirmed the founding case's own three "surviving"
instances (Learned #4's retracted-figure citation, THERMODYNAMICS'
mislabeled ratio, EM's false coincidence claim about two angles) were
themselves *authored in the Result/Learned sections after the run*, not
things that sat in the frozen Predictions text and were carried forward
unedited. That settles an ambiguity in R20's own phrasing: "surviving...
Phase-3 freeze into Result/Learned" means "present in the Result/Learned
sections of the completed document, as opposed to being caught in Phase 2
(pre-freeze) or confined to Idealizations/Next" — not literally
"unmodified since before the freeze." I apply that same reading below,
consistent with precedent.

### 1.2 Candidate-by-candidate independent re-verification (never taken on any reviewer's restatement)

**Candidate 1 — `observer_article_norm` range, "`2.26e-4`–`3.95e-4` across
all 12 cells" (NOTES.md Result, constraint-2 paragraph).**
I computed all 12 `partition_{C40_R4,G40_R4}_observer_article_norm`
values directly from `results.json` with my own script:

```
C40_R4: 2.2591e-4, 2.9927e-4, 2.6983e-4, 3.6393e-4, 3.7426e-4, 3.9490e-4
G40_R4: 1.1554e-4, 1.2260e-4, 1.3892e-4, 1.8218e-4, 2.1211e-4, 3.0938e-4
true 12-cell min/max = [1.15427e-4, 3.94897e-4]
```

**Confirmed wrong.** The stated `2.26e-4` floor is exactly `C40_R4`'s own
subset minimum (`2.2591e-4`, θ=38.590°); the true 12-cell minimum
(`G40_R4`, θ=37.127°) is **less than half** the stated floor. This is a
textbook R4-class defect — a claimed-exact figure that does not reproduce
from its own cited source (`results.json`). **VERDICT: genuine R4-class
defect. Location: Result. Caught only at Phase 5** (I confirmed by
re-reading all five Phase-2 critiques and the Phase-2 Red Team audit in
full myself — none could have caught it: this figure did not exist until
after Phase 4 ran).

**Candidate 2 — "tracking each other to 3 decimal places at every angle"
(back_frac, C40_R4 vs G40_R4, NOTES.md Result, Prediction 2 paragraph).**
I recomputed `back_frac = sigma_scat_downstream/sigma_scat` at all 12
cells directly from `results.json` and compared per-angle:

```
theta        back_frac_C  back_frac_G   |diff|    3rd-decimal digit match?
37.127246    0.653579     0.652866      0.000713  NO  (3 vs 2)
38.590230    0.618499     0.618425      0.000074  YES (8 vs 8)
39.200000    0.607571     0.606908      0.000662  NO  (7 vs 6)
40.265420    0.581197     0.582799      0.001602  NO  (1 vs 2)
41.460901    0.561949     0.560348      0.001602  NO  (1 vs 0)
42.960901    0.532434     0.533991      0.001557  NO  (2 vs 3)
```

**Confirmed wrong — the claim fails at 5 of 6 angles, matching only at
38.590230°.** This is R20's own named category verbatim ("a coincidence
that does not reproduce from its own cited source"), directly analogous
in shape to R20's own EM founding-case instance (a false "coincidence"
claim between two angles). **VERDICT: genuine R4-class defect. Location:
Result. Caught only at Phase 5** (grepped all five critiques and the
Phase-2 audit; this claim, like candidate 1, could not exist before
Phase 4 ran).

**A finding none of the six Phase-5 reviews caught, on this exact
candidate:** VISION's own Phase-5 review (which is the one that surfaced
this defect) states the claim "fails to reproduce at 3 of 6 angles
(40.265°, 41.461°, 42.961°)." **My own independent recomputation above
shows the true count is 5 of 6, not 3 of 6** — 37.127246° and 39.200000°
also fail at the third decimal digit (VISION's own listed diff values for
those two angles, 0.000713 and 0.000662, are large enough to flip the
third decimal under both truncation and standard rounding; I verified
this both ways). This does not change the R20 disposition of candidate 2
(it is still a genuine, still-wrong claim, still counts as one instance),
but it means VISION's own restated count is itself a minor,
non-load-bearing imprecision that a fresh Phase-5 reviewer's "recompute,
don't restate" standard (R4) would also flag — nobody, including VISION
itself, actually ran the digit-by-digit comparison to completion. I note
this for the record rather than as a chargeable defect against VISION's
otherwise excellent self-review (self-reviews are held to the same bar as
any other seat's numbers, per this program's own standing practice).

**Candidate 3 — THERMODYNAMICS' own finding: `p_abs_w`/`dt_ss_full_K`
"track the same smooth, monotonic-with-θ trend as `sigma_abs`" (NOTES.md
Result, Thermal sidecar paragraph).**
I recomputed both trends directly from `results.json` (C40_R4,
37.127246°→42.960901°):

```
sigma_abs:      310.928 -> 338.789   (+8.96%)
p_abs_w:      2.7866e-12 -> 3.3080e-12  (+18.71%)
dt_ss_full_K: 4.5780e-05 -> 5.4347e-05  (+18.71%)
ratio of relative growth rates: 18.71/8.96 = 2.088 (~2.09x)
```

**Confirmed wrong** — these are not "the same trend"; the two families
diverge by a factor of ~2.09, a real, exact, mechanically-derivable
consequence of `absorbed_power_established_ratio`'s quadratic
(`sigma_ext_cells²`) `iso_xsec_sq` convention, not noise (I independently
confirmed the constant `p_abs_w/(sigma_ext_cells²·ratio_abs_ext_raw)`
holds to 5 significant figures at all 6 angles, exactly as THERMODYNAMICS
found). This is R20's own "claimed... coincidence" category — a
same-trend/tracking claim that fails to reproduce. **VERDICT: genuine
R4-class defect. Location: Result (Thermal sidecar paragraph). Caught
only at Phase 5** (THERMODYNAMICS' own self-review; not addressable by
any Phase-2 seat since it is a post-run numeric relationship).

**Candidate 4 — QUANTUM's finding: NOTES.md's stated mechanism for
Prediction 3, "extinction efficiency approaches `Q_ext→2`," cites an
inflated number against this bench's own already-locked anchor
(`lab/qext_theory.py`/exp-002, `Q_ext_measured=1.5385088077964393` for
the identical article class, exp-059/exp-002).**
I independently re-derived every step:
- `experiments/002-cross-sections/results.json::absorber-600.q_ext =
  1.5385088077964393` — confirmed by direct grep, not restated.
- The R4 article's shell thickness: `(R4_R_OUT-PEC_R_R4)*DX_M_R4 =
  (156-60)*1.5e-8 = 1.44 µm`, and `SIGMA_R4_CORRECTED=0.25` is the
  `R4_RATIO`-scaled equivalent of the native absorber's optical depth
  (`design_geometry.py`'s own comment: "holds the shell's optical depth
  constant") — this is the same self-similar construction, so its
  angle-independent Q_ext *should* equal 1.5385 once correctly
  normalized, if the object is truly rotationally symmetric and LTI.
- `lab/sections.py::widths()`'s `i_inc` is computed as
  `-0.5·Re(Ez·conj(Hy))` at a single fixed vertical reference line — this
  measures only the **x-component** of the incident Poynting flux
  density. `lab/fdtd2d.py::add_line_source`'s own docstring confirms an
  oblique source launches a wave traveling along `(−cosθ, +sinθ)`, so
  `i_inc` undercounts the true incident intensity by a factor of `cosθ`
  at oblique incidence.
- I recomputed `sigma_ext/312` (the raw, uncorrected Q_ext this cycle
  reports) and its `cosθ`-corrected version at all 12 cells myself:

```
theta    Qraw_C   Qraw*cosθ_C   Qraw_G   Qraw*cosθ_G
37.127   1.9389   1.5459        1.9356   1.5432
38.590   1.9830   1.5500        1.9905   1.5558
39.200   1.9992   1.5493        2.0032   1.5524
40.265   2.0353   1.5531        2.0277   1.5472
41.461   2.0634   1.5463        2.0733   1.5537
42.961   2.1125   1.5459        2.1036   1.5394
anchor: 1.5385088077964393
```

All 12 corrected values land in **1.539–1.556**, within ~1% of the
already-locked 1.5385 anchor — an independent, non-tautological
confirmation via a completely different route (closed-form Bessel/Hankel
series vs. real FDTD). The raw, uncorrected values (1.94–2.11) that
NOTES.md's "approaches `Q_ext→2`" language implicitly leans on are an
`i_inc`-normalization artifact of oblique incidence, not a real
angle-dependent rise in extinction efficiency. I also confirmed applying
the same correction to `sigma_scat_downstream/312` still gives
0.399–0.491 — Prediction 3 remains genuinely falsified either way, so
this finding changes no scored verdict.

**VERDICT on categorization (the close call the brief specifically
flagged): this is a genuine, serious, independently-reproducible physics
defect — but I rule it does NOT count as an R20 "R4-class" instance.**
R20's own text and its three founding-case examples (a retracted-figure
citation, a mislabeled ratio *formula*, a false numeric coincidence
between two *specific stated values*) are all narrow, single-step,
source-checkable restatement failures: one exact number or formula from
one exact place, checked against one exact source. QUANTUM's finding is
categorically deeper — it is a *derived, multi-step physics
inconsistency* uncovered by cross-checking an implicit magnitude claim
against a different instrument's own locked output, not a literal
mis-transcription of an existing number. NOTES.md never actually states
"our `Q_ext` is 1.9-2.1" as a claimed figure sourced from somewhere else;
it makes a qualitative asymptotic claim ("approaches `Q_ext→2`") whose
*unstated* implicit numeric backing turns out to be an artifact. QUANTUM
itself categorizes this correctly as an **R9 (commensurability)
violation** — a different standing rule, with a different textual scope,
not R20's citation-restatement lane. I adopt QUANTUM's own R9 framing
rather than folding it into R20's tally. **This ruling is explicitly not
inertia**: even excluding this candidate entirely, three valid R20
instances remain (below) — the ruling on R20 firing does not turn on
this classification either way, which is precisely why I can rule it on
its true merits rather than on which way the vote needs to go.

**Candidate 5 — the "T3" mislabeling in the Next section.**
I independently re-read `LOGBOOK.md`'s actual T3 definition (lines
1066-1106) and the Reconciled Iteration-78 queue's own Tier-2 line (lines
6904-6906): **T3 is specifically the eye's temporal-contrast
(flicker/motion) switching-transient instrument** (`lab/temporal_csf.py`
+ `lab/amplitude_bridge.py`, suite stages 13/14) — a constraint-3/4
*joint, time-varying-mechanism* instrument, unrelated to a steady-state
downstream-irradiance conversion. I confirmed `phase1_proposal.md` §5
already states "That conversion is exactly the still-unbuilt T3
instrument" (present in the frozen Idealizations, Phase 1, carried
unedited into NOTES.md's Idealizations at Phase 3), and NOTES.md's Next
item 1 repeats the same mislabeling post-run. I grepped all five Phase-2
critiques and the Phase-2 Red Team audit for "T3": **zero hits**,
confirming no one caught it at Phase 2. **VERDICT: genuine label defect,
confirmed. But it lives in Idealizations (frozen at Phase 1/3) and Next
(post-run) — never in Result or Learned.** R20's text is specific to
"Result/Learned sections"; Idealizations and Next are different, named
sections in this program's own NOTES.md template, used for a different
purpose (disclosed scope limits and forward-looking candidates,
respectively, not scored findings). **This does NOT count toward R20's
tally** — a genuine defect, correctly caught only at Phase 5, but a
legitimate scope exclusion under R20's own specific text, not a "let it
off easy" reading. (It should still be corrected — see §6.)

### 1.3 The counting question the brief flags as dispositive: is candidate 1 one instance or two?

VISION and EM independently found candidate 1 — but they found the
*identical* defect: the same wrong number (`2.26e-4` vs. true
`1.1554e-4`), the same location (NOTES.md's constraint-2 sentence in
Result), the same root cause (silently reporting the `C40_R4` subset as
"all 12 cells"), down to matching digits in both reviews' own
recomputation scripts. This is corroboration of one fact by two
independent methods, not two independently-arising defects. R20's own
text counts "independent R4-class defects," meaning distinct defect
*instances* in the document, not distinct *catches* of the same
instance — exactly as a scientific replication of one measurement by two
labs is one result, not two. **I rule candidate 1 = ONE instance.**

### 1.4 Final tally and ruling

| # | Candidate | R4-class? | Section | Caught only at Phase 5? | Counts? |
|---|---|---|---|---|---|
| 1 | `observer_article_norm` range | YES | Result | YES (VISION+EM, same instance) | **YES — 1** |
| 2 | back_frac "3dp tracking" | YES | Result | YES (VISION) | **YES — 1** |
| 3 | `p_abs_w`/`sigma_abs` "same trend" | YES | Result | YES (THERMODYNAMICS) | **YES — 1** |
| 4 | "`Q_ext→2`" mechanism claim | Real defect, but R9-shaped not R4-shaped | Result | YES (QUANTUM) | NO (different rule) |
| 5 | "T3" mislabeling | YES | Idealizations/Next | YES (VISION) | NO (wrong section) |

**Valid R20-countable instances: 3, independently confirmed from raw
source by me, none double-counted, none miscategorized by inertia.**

**RULING: R20 FIRES.** The bar ("three or more") is met on strict,
independently-reproduced grounds, using the most conservative valid
counting convention available (excluding the debatable candidate 4
entirely, and counting the two-seat-confirmed candidate 1 only once).
Per R20's own adopted text, this is automatic — "no further
deliberation" — and the founding instance's one-time grace period was
already spent at exp-099 (Iteration 76); exp-101 is a later, already-bound
cycle. **This is the first cycle in this program's history where R20's
automatic clause actually fires**, as distinct from every prior close
call (exp-098's FI-G'', exp-099's own founding five-instance case,
exp-100) where every instance was caught blind within the same cycle's
own review layers and the rule's forward-elevating clause had not yet
been triggered.

**Worth stating plainly, because it matters for how this should read to
the Director and to Marsh: R20 firing here is not evidence this cycle's
science is bad.** The Tier-0 deliverable is real and correctly executed
(§2 below). What fired is a *citation-hygiene density* pattern in
post-run prose — three independent, non-load-bearing restatement/
tracking-claim errors in one document's Result section, each individually
minor, exactly the pattern R20 was built to catch systemically rather
than case-by-case. The rule's own design intent (stated at its adoption)
is to escalate *density*, independent of whether any instance is
load-bearing — and none of these three is (§1.5 below).

### 1.5 Did any of the five candidates change a scored verdict?

I independently re-checked all four predictions and the constraint-2
reading against the raw data, including QUANTUM's own cosine-corrected
numbers:

- **Prediction 1** (`sigma_abs/sigma_ext` ∈ [0.505,0.520]): true range
  [0.51291, 0.51450] — CONFIRMED, untouched by any candidate (this is a
  ratio, immune to the `i_inc`/cosθ artifact per QUANTUM's own proof).
- **Prediction 2** (`back_frac`>0.5): true min 0.5324 — CONFIRMED,
  untouched; candidate 2 only affects the *descriptive characterization*
  of the trend, not the `>0.5` pass/fail itself.
- **Prediction 3** (`sigma_scat_downstream`/312 <0.15): true range
  [0.5457, 0.6159], FALSIFIED. I confirmed the cosθ-corrected range
  (0.399-0.491, from candidate 4's own correction) is *still* nowhere
  near 0.15 — the falsification verdict is unchanged either way.
- **Prediction 4** (`box_dev_scat_downstream`≤0.12): true range
  [0.0057, 0.0454] — CONFIRMED, untouched by any candidate.
- **Constraint 2** (`observer_article_norm` "stays clean," gated at R18's
  <0.02 bar): even the corrected true minimum (1.1554e-4) is ~173×
  inside the gate — candidate 1 changes the stated range but not the
  "stays clean" verdict.

**Confirmed independently: zero of the five candidates changes any of
this cycle's four scored PASS/FAIL verdicts, or the constraint-2
"clean" reading.** All six Phase-5 reviews' claim to this effect is
correct, verified from the raw numbers myself, not restated from their
text.

---

## 2. Disposition of each of the six Phase-5 reviews' core findings

**VISION (self-review).** **CONFIRM**, with one correction noted above
(§1.2, candidate 2's own true fail-count is 5/6, not the stated 3/6 — a
minor imprecision in an otherwise excellent, appropriately hostile
self-review). VISION's identification of the R20 pattern itself, the
Prediction-1-vs-Prediction-3 same-document tension nobody cross-checked
before committing (a genuine, well-reasoned pre-run process finding), and
the T3 mislabeling diagnosis (independently confirmed against
LOGBOOK's own T3 text by me, §1.2 candidate 5) all check out. The
"W-equivalent-cells" unit critique is correct and minor, as stated.

**ELECTROMAGNETISM.** **CONFIRM in full**, including the "floor gate only
wired into one of four fields" finding, which I independently
re-verified by reading `run_leg_b_fixed()` line-by-line myself: only
`row[f"{prefix}_partition_forward_continuing"]` is conditioned on
`scat_floor_pass` (set to `None` on failure); `partition_absorbed`
(feeding Prediction 1), the raw `sigma_scat_downstream`/
`sigma_scat_sourceward` fields (from which `back_frac`/Prediction 2 is
reconstructed), and `box_dev_scat_downstream` (Prediction 4) are all
assigned unconditionally a few lines earlier, with no floor check
anywhere near them. This is a real, currently-dormant (0/12 cells failed
this run) **code-level latent gap**, not a documentation-only issue — see
§6's explicit flag on this. EM's lateral-face-leakage finding (35-47% of
`sigma_scat` exits laterally, growing monotonically with θ, exceeding
`back_frac` itself at the largest angle) is independently confirmed by my
own recomputation (`1-(back_frac+fwd_frac)` at all 12 cells matches EM's
table to 4 decimal places) — a genuine, previously-undisclosed,
non-load-bearing but scientifically important omission from NOTES.md's
"lateral/diffuse remainder" framing. The `observer_article_norm`
restatement-error finding is the same single instance as VISION's (§1.3).

**THERMODYNAMICS.** **CONFIRM in full.** The R21 third-strike discharge
is independently re-verified (I grepped `results.json` myself for all 12
`netd_classification`/`p_abs_w`/`dt_ss_full_K` fields: all UNDETECTABLE,
368× below `NETD_BAND_K`'s lower edge). The `sigma_abs`-vs-`p_abs_w`
divergence finding (candidate 3 above) is independently reproduced by me
to the same digits (2.088× ≈ 2.09×). The explicit disclaimer that
Prediction 3's falsification (elastic 600nm scattering) carries zero
constraint-3/thermal implication is correct — I independently traced
`cell_metrics_r4`'s call to `absorbed_power_established_ratio` and
confirmed its only inputs are `sigma_ext_cells`/`ratio_abs_ext_clamped`;
`back_frac`/`fwd_frac`/`sigma_scat_downstream` appear nowhere in that
call chain.

**MATERIALS.** **CONFIRM in full**, including both new findings I
independently re-derived: (1) `Q_abs = sigma_abs/312` exceeds 1.0 at 10
of 12 cells, rising to 1.086 at 42.96° — I recomputed this myself from
`results.json` and matched MATERIALS' table to 4 decimal places at every
cell; `Q_abs≤1` is indeed a sharper, more elementary bound than the
`σ_abs/σ_ext≤0.5` Babinet ratio (it doesn't require invoking the forward
companion lobe at all), and it currently carries no disclaimer despite
sitting one line below the ratio that does. (2) The 1.44 µm shell
thickness (`(156-60)*1.5e-8 m`, independently recomputed by me) exactly
matches `REALIZABILITY_MEMO.md`'s own cited figure (grepped directly:
"this construction's own 1.44µm shell," Amendment 7) — MATERIALS'
observation that Prediction 3's extinction-paradox magnitude describes an
article already LOCKED UNOBTANIUM-WITH-PARAMETERS, not a property a
realizable coating at this thickness would show, is a correct and
valuable scope connection nobody else in the packet made.

**PHOTONICS.** **CONFIRM**, with an appropriately hedged rating on the
central claim. The box-registration-artifact explanation for the
`back_frac` decline is well-argued and quantitatively grounded — I
independently recomputed the lateral-flux-share table (`101.84→149.58`
cells, `0.3464→0.4670` fraction) and confirmed it matches PHOTONICS'
numbers exactly, and confirmed `tan θ` grows 23% over the same sweep
(same order of magnitude and direction as the 35% relative lateral-share
growth). This is a genuinely strong circumstantial case (a fixed
lab-frame box measuring an obliquely-launched forward lobe should show
exactly this signature), correctly hedged by PHOTONICS itself as "very
likely," not proven with certainty — I did not find, and PHOTONICS did
not claim to find, a rigorous exclusion of a real article-angular-response
contribution layered on top of the geometric effect. I rate this
**CONFIRM as the best-supported available explanation**, not as an
established fact beyond dispute — the appropriate epistemic state given
what a single 6-angle, fixed-box sweep can actually establish. PHOTONICS'
observation that `box_dev_scat_downstream`'s same-orientation box pair
cannot detect this class of artifact (only size-independence, never
orientation-independence, is tested) is a correct and useful structural
point for any future reuse of this box family.

**QUANTUM OPTICS.** **CONFIRM**, with the categorization ruling above
(§1.2, candidate 4) as my one point of independent judgment layered on
top of QUANTUM's own findings. The box-margin re-verification (item a),
the `box_dev` size-delta-ratio-tracking finding (item b — I independently
confirmed the 2.4× size-delta ratio vs. the observed 2.5-3.15× `box_dev`
ratio track closely across all 6 angles), and the `cosθ`-correction
finding (item c) are all independently reproduced by me to the digit.
QUANTUM's own framing of this as an R9 violation, not an R4/R20 one, is
the categorization I adopt (§1.2).

---

## 3. What none of the six Phase-5 reviews caught

Beyond VISION's own imprecise "3 of 6" restatement (§1.2, noted above as
attached to that seat's review specifically), two smaller items, neither
scored as a defect:

1. **The Phase-2 Red Team audit's own contingent R20 risk (attack #3, the
   R3-vs-R4 pool-duplication finding) was correctly discharged — worth
   stating explicitly because it means R20 fired this cycle via a
   completely different, unanticipated pathway than the one flagged and
   mitigated at Phase 2.** I confirmed NOTES.md's "Changes from Phase 1"
   item 5 and its Idealizations both correctly carry the dedup caveat as
   disclosed, not settled fact — that specific R20 exposure was closed as
   designed. None of the six Phase-5 reviews states this contrast (that
   the anticipated R20 risk was neutralized while three unanticipated ones
   independently accumulated) — worth a line in the LOGBOOK entry so a
   future cycle does not conclude "Phase-2 already checked for R20 risk
   here" as a reason to skip a fresh Phase-5 citation audit.
2. **NOTES.md's Learned-section framing of the `back_frac` trend as "a
   genuine angular trend... worth a future cycle's attention"** sits in
   tension with PHOTONICS' own Phase-5 finding (§2 above) that this trend
   is very likely a box-registration artifact, not a genuine property of
   the article's own angular scattering. This is not itself an R4-class
   citation defect (no specific figure is misquoted; "genuine... trend" is
   defensible as "a genuine, reproducibly-measured trend" without implying
   it is article-physics) but it is an interpretive gap in the same
   family as candidate 4 — worth a same-shift NOTES.md clarification
   (§6) even though it does not add to the R20 tally.

I did not find a sixth, independent defect beyond what the six reviews
and my own re-derivations above already surface. I specifically checked
(and found clean): the `xi_ext`/`sigma_ext_cross` internal-consistency
identity at all 12 cells (agrees to 6.5e-5–2.6e-4, tighter than the
trust-suite's own PEC reference case); the `sigma_abs+sigma_scat=sigma_ext`
definitional identity; the box-margin gate arithmetic (`_verify_box_margins`
recomputes from raw `Sim` geometry, not hand-derived, and I independently
re-derived the same 90/136-cell margins from raw constants); the R19
call-count(24)/row-count(6) separation; and the registration preflight
(`all_clean: true`, all 12 points, confirmed directly in `results.json`).

---

## 4. Checkpoint criteria

- **Criterion 4 (Red Team flags program-integrity drift) — FIRES.** Per
  §1.4's ruling: R20's own automatic clause is met on independently
  re-verified grounds (3 valid instances, conservative counting), and
  this is a later cycle with no grace period remaining. This is the
  correct, non-inertial application of this program's own established
  R16/R20-style discipline — the founding instance got a pass; the next
  qualifying cycle does not, by the rule's own design.
- **Criterion 2 (a proven mechanism-class boundary, gates clean) — does
  NOT apply, confirmed explicitly rather than assumed.** This cycle makes
  zero constraint-satisfiability claim of any kind: T1's escape route is
  N/A (independently reconfirmed — the article, geometry, and
  `SIGMA_R4_CORRECTED=0.25` are byte-identical to the already-committed
  R4 config; no σ(I)/σ(x,t)/angular-selectivity/sub-threshold parameter
  is touched anywhere in `run.py`, and no constraint-3 ambient/silhouette
  claim or `C_thr` comparison appears anywhere in `NOTES.md`). With no
  mechanism-class hypothesis on the table, there is nothing for a
  "boundary" to be proven about. N/A, confirmed.
- **Criterion 1 (passes all constraint metrics) — N/A.** Constraints 3/4
  are not addressed this cycle by design (Tier 0 only).
- **Criterion 3 (engine physics beyond validated bench classes) — N/A.**
  Zero `lab/` diff, confirmed via `git log -- lab/` (no pending or recent
  diff) and the live 41/41 trust-suite re-run.
- **Criterion 5 (two consecutive no-result iterations) — N/A.** exp-100
  (Iteration 77) produced a genuine logbook-advancing defect diagnosis;
  exp-101 (this cycle) produces a genuine logbook-advancing instrument fix
  plus the R20 firing itself — neither is a null iteration, so there is
  no two-in-a-row pattern to invoke, independent of criterion 4 already
  firing on its own separate textual trigger.

---

## 5. Combined Verdict

**PROMISING, with Checkpoint criterion 4 FIRED as a same-cycle process
flag, not a scientific one.** Splitting the two axes deliberately, because
conflating them is exactly the mistake R20 exists to prevent:

- **Substantively:** the Tier-0 mandate was delivered correctly. The
  closed-box reconstruction genuinely fixes `beam_behind_t28`'s
  uninterpretable line-window defect (0/12 cells unresolved, box
  independence 2.6×-21× inside `XI_TOL`), all six Phase-2-mandated fixes
  landed in executed code (not merely prose — independently re-verified
  by EM and by me), the angle re-selection is correctly re-derived from
  the full pool, and two seats (QUANTUM, PHOTONICS) turned up genuinely
  new, well-evidenced physics (the `i_inc`-cosθ artifact resolving to a
  1%-precision match against an independent locked anchor; the
  box-registration explanation for the `back_frac` trend) that will
  materially improve the next instrument. Zero constraint violated,
  zero `lab/` diff, house discipline on prediction-freezing honored.
- **Procedurally:** three independently-reproduced R4-class citation/
  coincidence defects in Result prose, none load-bearing, meet R20's bar
  on the most conservative valid count. This is not a reason to distrust
  this cycle's actual numbers (I independently reproduced all of them);
  it is a reason to log the pattern and fix the prose, per R20's own
  design, which explicitly separates "fires" from "was load-bearing."

---

## 6. Ranked mandatory same-shift fixes to NOTES.md

**Confirmed: all fixes below are documentation-only corrections to
NOTES.md's prose.** I independently checked every one of the six reviews
for a claim that any scored *number* in `results.json` is itself wrong
(as opposed to a prose restatement of it) — none found one. The one
partial exception, flagged distinctly rather than folded in: EM's
floor-gate-wiring finding is a genuine **code** gap in `run.py` (not
NOTES.md prose), but it changed zero values this run (0/12 cells ever
needed the exclusion) — it is a latent risk for a *future* reuse of this
exact pipeline shape, not a fix this cycle's own results require.

1. **Correct the `observer_article_norm` range** to `[1.1543e-4,
   3.9490e-4]` (all 12 cells), or explicitly relabel the existing
   `[2.26e-4, 3.95e-4]` figure as "`C40_R4` range only" if that was the
   actual intent. *(Candidates 1; VISION + EM.)*
2. **Correct or drop "tracking each other to 3 decimal places at every
   angle"** for `back_frac` — replace with an accurate characterization,
   e.g. "agreeing to within 0.0007–0.0016 across the sweep" (I independently
   confirmed the true fail-rate is 5 of 6 angles at the literal third
   decimal, stricter than VISION's own stated 3 of 6 — use the corrected
   figure if this document is amended). *(Candidate 2; VISION, corrected
   per §1.2/§3 above.)*
3. **Rewrite the Thermal-sidecar paragraph**: do not claim `p_abs_w`/
   `dt_ss_full_K` "track the same trend" as `sigma_abs` — state the
   +18.71% vs. +8.96% divergence (2.09×) and its exact mechanical cause
   (`p_abs_w ∝ sigma_ext_cells²` via the `iso_xsec_sq` convention, while
   `sigma_abs ∝ sigma_ext_cells` at a nearly flat `ratio_abs_ext_raw`).
   Drop the invented "W-equivalent-cells" unit; cite `sigma_abs` in its
   native cross-section units (cells) and `p_abs_w` separately in Watts.
   *(Candidate 3; THERMODYNAMICS.)*
4. **Drop the "T3" cross-reference** from both Idealizations and Next
   item 1 — the coherent downstream point-intensity instrument is
   constraint 1's own missing conversion (PANEL.md's metric-table row),
   not T3 (the temporal-CSF switching-transient instrument, unrelated).
   *(Candidate 5; VISION.)*
5. **Extend the existing T9 disclaimer to cover `Q_abs=sigma_abs/312`**
   explicitly (10 of 12 cells exceed the `Q_abs≤1` geometric-optics
   ceiling, up to 1.086 at 42.96°) — one sentence, same paragraph as the
   already-carried ratio disclaimer. *(MATERIALS.)*
6. **Add one sentence to Learned** noting the extinction-paradox magnitude
   measured (`sigma_scat_downstream` ∈ [170.5, 192.2]) describes the
   already-LOCKED UNOBTANIUM-WITH-PARAMETERS `graded_black_shell`
   construction specifically (cross-reference `REALIZABILITY_MEMO.md`
   Amendments 6-7), not a property any currently-named realizable coating
   at this 1.44 µm thickness would reproduce. *(MATERIALS.)*
7. **Correct Prediction 3's stated mechanism**: replace "extinction
   efficiency approaches `Q_ext→2`" with the corrected, `cosθ`-normalized
   reading (`~1.54`, matching `lab/qext_theory.py`'s locked
   `Q_ext_measured=1.5385` to ~1%) — the raw `~2` figures this cycle
   produced are an `i_inc`-normalization artifact of oblique incidence,
   documented in `lab/fdtd2d.py::add_line_source`, not a real
   angle-dependent rise. The qualitative Babinet/extinction-paradox
   argument for why a large forward lobe accompanies a real shadow is
   still correct and should stay; only the specific "`→2`" magnitude
   claim needs correcting. *(Candidate 4/QUANTUM — flagged as R9, not
   R20, per §1.2, but still a mandatory same-shift prose fix.)*
8. **Re-invoke T8's near-field disclaimer for Prediction 3's explanation**,
   the same way it is already invoked for Prediction 2 — the
   Babinet/`Q_ext→2` asymptote is a far-field statement, and this box
   sits at z/z_R≈0.04-0.06. *(PHOTONICS.)*
9. **Quantify the lateral-flux channel** in the Idealizations/Result
   partition disclosure — replace "a lateral/diffuse remainder" with the
   actual, growing fraction (35%→47% of `sigma_scat` across the sweep,
   exceeding `back_frac` itself at 42.96°). *(EM.)*
10. **Add one sentence connecting the `back_frac` Learned-section
    observation to Prediction 3's own falsification** as very likely the
    same box-registration effect viewed two ways (not two unrelated
    observations), per PHOTONICS' finding — and soften "a genuine angular
    trend" to avoid implying confirmed article physics pending an
    orientation-sensitivity test. *(PHOTONICS; also addresses §3 item 2
    above.)*
11. **Add one sentence disclaiming any constraint-3/thermal implication**
    from Prediction 3's falsification — the large forward-scattered
    residual is elastic 600nm scattering, a physically distinct channel
    from blackbody/graybody re-radiation; `cell_metrics_r4`'s NETD chain
    never references it. *(THERMODYNAMICS.)*
12. **[Code, not NOTES.md — flag for future reuse, not required this
    cycle]** Wire the Fix-1 `scat_floor_pass` exclusion into all four
    predicted-band-feeding fields (`partition_absorbed`,
    `sigma_scat_downstream`/`sigma_scat_sourceward`, and
    `box_dev_scat_downstream`), not only `partition_forward_continuing`,
    if this exact `run_leg_b_fixed()` pattern is reused in a future
    cycle. *(EM.)*
13. **Log this cycle's R20 firing and Checkpoint-4 trigger in LOGBOOK.md**,
    per §1.4/§4's ruling — a Director action, not a NOTES.md edit, but
    listed here because it is the one mandatory same-shift action with no
    natural home in NOTES.md's own template.

None of the above requires a re-run, changes the angle set, box geometry,
or call budget, or alters any of the four scored PASS/FAIL verdicts —
confirmed independently in §1.5.

---

## 7. Ranked candidate next-iteration directions (top-3, synthesizing all six reviews)

1. **Build the coherent, phase-resolved downstream point-intensity
   instrument** (NOTES.md's own Next item 1, correctly scoped per
   VISION's fix — NOT badged "T3") — independently endorsed, from five
   different charter angles, by VISION, EM (implicitly, via the
   coherent-vs-incoherent lesson), MATERIALS, PHOTONICS, and QUANTUM. This
   review adds one binding precondition uncovered only this cycle: the new
   instrument must (a) correctly normalize its own incident reference for
   oblique incidence (fix or explicitly correct for the `i_inc`/`cosθ`
   artifact QUANTUM found — it will need a correct absolute intensity far
   more than this cycle's ratio-only predictions did), and (b) use a
   beam-aligned or beam-rotating reference frame rather than a fixed
   lab-frame box (PHOTONICS' finding) — building it on the current box
   family's orientation convention unmodified would silently inherit both
   artifacts this cycle just surfaced.
2. **Close the 13 same-shift NOTES.md/LOGBOOK fixes above (§6) and log
   the R20/Checkpoint-4 entry** — zero FDTD, must happen before this
   cycle's Result section is cited by any future iteration, and is itself
   this program's own standing practice for a fired standing rule.
3. **Tier 1** (PHOTONICS' zero-FDTD physical-hypothesis check on the
   R3-vs-R4 `delta_scene` split), unchanged priority per the Reconciled
   Iteration-78 queue, now doubly informed: it must inherit both this
   cycle's own Phase-2 pool-duplication finding (12/33 R3 rows, 6/35 R4
   rows are non-independent citation-republished duplicates) and, if it
   ever touches `sigma_scat_downstream`-style box-face quantities, the
   orientation-sensitivity caveat from item 1 above.

Secondary/maintenance items (not top-3, but on the record): re-run
`box_dev_scat_downstream`'s cross-check with a matched *relative* `Δr`
for both configs rather than a matched absolute clearance (QUANTUM,
item b); the code-level floor-gate wiring fix (§6 item 12, EM) if this
pipeline shape is reused.

---

## 8. Summary for the Director

- **R20 FIRES.** Three independently-reproduced, non-load-bearing
  R4-class defects in Result prose (the `observer_article_norm` range,
  the `back_frac` "3dp tracking" claim, the `sigma_abs`/`p_abs_w`
  "same trend" claim), each caught only at Phase 5, meet the bar under
  the most conservative valid counting (candidate 1 counted once despite
  two-seat confirmation; the debatable `Q_ext` finding excluded entirely
  as R9-shaped, not R4-shaped; the T3 mislabeling excluded as
  outside Result/Learned). This is the first cycle where R20's own
  automatic clause actually triggers a Checkpoint, as designed, with no
  grace period remaining after exp-099's founding instance.
- **Checkpoint criterion 4 FIRES**, directly and automatically, per R20's
  own text. Criteria 1, 2, 3, 5 do not apply (each confirmed explicitly
  above, not assumed).
- **Combined Verdict: PROMISING** on substance (a real, correctly-executed
  instrument fix, zero constraint violated, zero verdict changed by any
  defect found) **with Checkpoint 4 fired as a same-cycle process flag.**
- 13 ranked, same-shift, documentation-only fixes to NOTES.md (plus one
  flagged code-level latent gap for future reuse, and the LOGBOOK entry
  itself) are listed in §6, none requiring a re-run or changing any
  scored verdict.
- Top-3 next-iteration directions in §7: the coherent downstream
  instrument (with two new preconditions this cycle discovered), the
  same-shift documentation fixes, and Tier 1's R3-vs-R4 physical-
  hypothesis check.
