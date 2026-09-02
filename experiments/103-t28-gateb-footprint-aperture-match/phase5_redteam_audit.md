# RED TEAM — Phase-5 FINAL AUDIT, exp-103 (Panel Iteration 80)

**Seat: RED TEAM. Sees Phase-1 + all six blind Phase-5 reviews. Standard: not textbook-physics compliance — kills internal inconsistency, unfalsifiable claims, mechanisms inexpressible as simulation parameters, and quiet constraint drift, especially #3. Never leads; has no proposal of its own to protect.**

All findings below were checked against primitives I re-derived myself — `run.py`, `results.json`, `run_output.txt`, `phase1_proposal.md`, all five Phase-2 critiques, `phase2_redteam_audit.md`, `lab/thermo_sidecar.py`, `lab/fdtd2d.py`, `experiments/065-…/design_geometry.py`, `experiments/069-…/design_geometry.py`, `lab/validation/VALIDATION.md`, and `LOGBOOK.md` directly — not taken on any review's word.

---

## 0. Independent primitive-level re-verification (show work)

**(a) The Nyquist/aliasing math (PHOTONICS F2/F3, QUANTUM Finding 1).** A coherent field's intensity |Ez|² carries a cross-term at *double* the field's spatial frequency: for a two-wave superposition, |E|² ⊃ cos(2kx), period = λ/2 = 10 cells at this cycle's λ=20-cell grid. Nyquist requires sample spacing strictly less than **half** that period, i.e. <5 cells. The adopted "≤10-cell (λ/2) pitch" fix samples at *exactly one full period* of the quantity actually at risk — the textbook degenerate aliasing case (a periodic signal sampled once per period reads as a constant regardless of true amplitude). Independently confirmed correct — this is not a matter of interpretation, it's arithmetic, and PHOTONICS/QUANTUM both derived it correctly by different routes.

I also independently recomputed the boxcar-filtering mitigation (PHOTONICS F3): `H_REGION=5` → block width W=11; filtering a period-10 sinusoid gives `|sinc(11/10)|`:
```
sinc(1.1) = sin(1.1π)/(1.1π) ≈ -0.0894  →  |sinc| ≈ 0.089
```
Matches PHOTONICS's figure exactly. **Confirmed**: each single sample already suppresses ~91% of any λ/2-period ripple internally, independent of pitch — this is real, but it is a *different* mechanism than "the pitch resolves the ripple," and doesn't rescue the pitch's own Nyquist failure.

**(b) EM's "backwards citation" claim.** I read `VALIDATION.md` lines 363–391 directly: stage-20's canonical `sigma_max=0.5` bench "settles to ~1.5×10⁻⁵ field-relative RMS at 900 steps" — confirmed verbatim, EM quoted it correctly. I then recomputed all five `settling_check` ratios from `results.json` against 1.5e-5:

| x | rel_change (fraction) | ÷1.5e-5 |
|---|---|---|
| 352 | 1.0990e-3 | **73.27×** |
| 353 | 8.358e-4 | 55.72× |
| 354 | 5.221e-4 | 34.81× |
| 355 | 2.328e-4 | 15.52× |
| 356 | 3.137e-5 | **2.09×** |

Every value is **larger**, not smaller, than the cited figure, by 2×–73×. NOTES.md's Result/Learned-#2 claim ("two to three orders of magnitude SMALLER") is confirmed objectively backwards. **EM's finding is correct**, independently reproduced from source.

**(c) MATERIALS Finding 1 (dropped Realizability Bound).** `grep -n "Realizab\|layer\|Kramers\|realizab" NOTES.md` returns exactly one hit — line 175, the promissory "(Realizability Bound below)" cross-reference itself. Zero occurrences anywhere after it. Confirmed: the label survived Phase 1→3, the reasoning did not.

**(d) VISION Finding 1 (disclaimer placement).** `grep -n "Weber-contrast\|C_thr(L)\|perceptual scoring\|DISCLAIMER"` on NOTES.md returns three hits: Setup, Idealizations, and Next (a *different* sentence, naming the still-unbuilt future perceptual-conversion item, not the disclaimer). The mandatory-fix-8 disclaimer sentence itself is confirmed absent from Predictions and Result. Confirmed mechanically.

**(e) R4_TAPER provenance (PHOTONICS F6, Red Team's own Phase-2 finding).** Read `experiments/065-…/design_geometry.py:123` (`TAPER = 40`) and `experiments/069-…/design_geometry.py:228,256` (`R4_RATIO = 2.0`; `R4_TAPER = round(TAPER * R4_RATIO)  # 80`) directly. Confirmed exactly as narrated — `EDGE=40` is the correct cpl=20-calibrated value.

**(f) THERMODYNAMICS/MATERIALS thermo_sidecar independence.** Read `lab/thermo_sidecar.py:124–168` directly: `absorbed_power_established_ratio(i_incident_w_cm2, sigma_ext_cells, dx_m, ratio_abs_ext, …)` — no parameter reads an FDTD source object, amplitude, or `edge`. `grep -n thermo_sidecar run.py` shows only comment/docstring/print-string occurrences, zero import/invocation. Confirmed.

**(g) QUANTUM's linearity claim (engine has no saturation/gain/nonlinearity).** `grep -n "saturat\|nonlinear\|gain\b\|kerr\|chi2\|chi3"` on `lab/fdtd2d.py` returns nothing but the unrelated `envelope()` Pythagorean sum. Confirmed: the update loop is linear, so Red Team's own Phase-2 override of QUANTUM's phase-resampling remedy is independently re-confirmed correct (a third independent confirmation, after Red Team's Phase-2 audit and QUANTUM's own Phase-5 re-derivation).

**(h) `Delta_phi` absence (QUANTUM Finding 4).** `grep -n Delta_phi\|delta_phi` on exp-103's `run.py` returns nothing; the identical grep on exp-102's `run.py` returns five hits including a working `delta_phi` computation. Confirmed: silently not carried forward, zero marginal cost to add.

That's eight independent primitive-level re-derivations, spanning five of the six reviews.

---

## 1. Ruling on every numbered finding

### PHOTONICS
- **F2** [load-bearing] — **ADOPT.** Independently re-derived (§0a). The "Nyquist fix" is not a fix in kind, only in degree.
- **F3** [load-bearing, mitigating] — **ADOPT.** Independently re-derived (§0a), sinc value matches exactly.
- **F4** [load-bearing] — **ADOPT.** Follows directly from F2+F3; NOTES.md's causal claim overstates what the measurement can show. Discussed further under Checkpoint 4 below.
- **F5** [non-load-bearing, corroborating] — **ADOPT.** 10-cell pitch against a 25–40-cell period gives 2.5–4 samples/period, sub-half-period, genuinely adequate — the two-fringe-mechanism conflation is real and worth separating.
- **F6** [confirmed correct] — **ADOPT.** Independently re-traced from `design_geometry.py` sources (§0e), exact match.
- **F7** — **ADOPT-WITH-CLARIFICATION.** 1.8337% is arithmetically *just above*, not "at the edge of," the 1.5–1.8% range — PHOTONICS's own phrasing is slightly loose, but the underlying point (proximity, not central match) is correct, and NOTES.md's own text only ever claims "close to," never "inside" — so no NOTES.md defect exists here. Non-load-bearing either way.
- **Argued next change** — **ADOPT, with one correction**: the field arrays are **not** cached across cycles (`results.json` stores only derived scalars, not raw `Ez`), so "post-processing-only if fields still cached" does not apply — this requires a fresh, minimal FDTD pair. Still cheap. Folded into the Iteration-81 queue below.

### MATERIALS & METAMATERIALS (self-review)
- **Finding 1** [load-bearing, MATERIALS-charter gap] — **ADOPT.** Independently confirmed by direct grep (§0c). A real content drop that survived Phase 1→3 undetected by five critiques and Red Team's own Phase-2 audit.
- **Finding 2** — **ADOPT.** Confirmed non-conflated by inspection of NOTES.md Setup.
- **Finding 3** — **ADOPT.** Reasonable, non-load-bearing framing point.
- **Finding 4** — **ADOPT.** A genuine, well-posed hypothesis worth carrying forward; correctly labeled speculative/future.
- **Finding 5** — **ADOPT-AS-FLAGGED, not independently reproduced.** I did not re-run the full trust suite to confirm 41/41 exists as claimed. MATERIALS's own characterization is fair; I have no basis to override it either way.
- **Argued next change** — **ADOPT.** Directly discharges Finding 1; folded into the mandatory-fixes docket.

### ELECTROMAGNETISM
- **Backwards-citation finding** [load-bearing] — **ADOPT.** Independently re-derived from primitives (§0b), confirmed exact. This is the single cleanest, most objectively-verifiable defect surfaced by any review this cycle.
- **Settling-methodology finding** [non-load-bearing] — **ADOPT.** Correct and well-reasoned: a shared-artifact floor cannot be ruled out by this design in principle, but the monotonic decay of `rel_change` with standoff is the right signature of a genuine decaying transient, not a flat floor. A fair, appropriately-scoped limit on "decisively" language, not a verdict-changing gap.
- **Passivity-bound finding** [non-load-bearing, positive] — **ADOPT.** Spot-checked against `results.json`: the largest kappa value present (0.0641, x=456) is nowhere near 1. Cheap, worth stating.
- **Jensen's-inequality finding** [non-load-bearing] — **ADOPT.** Recomputed, matches "~1.9%" exactly.
- **Quantization-bias recomputation** — **ADOPT.** Independently recomputed: `omega≈0.071086` (not 0.07111), `phi≈1.56389`, `cos(phi)≈0.00686` (not 0.0064, ~7.5% higher). EM's arithmetic is right; NOTES.md's own worked numbers carry a rounding slip. Genuinely non-load-bearing.
- **Argued next change** — **ADOPT**, folded into standing-watch tier of the Iteration-81 queue.

### THERMODYNAMICS
No numbered findings — clean self-review, explicitly registered orthogonal disposition. **ADOPT the disposition as accurate**: independently confirmed the dependency-chain claim (§0f) and the zero-import claim; the "genuinely orthogonal" characterization is correct. **Argued next change — ADOPT**, filed as a standing process flag, not an Iteration-81 action item.

### QUANTUM OPTICS
- Independent re-derivation of Red Team's Phase-2 override — **ADOPT, third independent confirmation** (§0g above).
- **Finding 1** [load-bearing] — **ADOPT.** Independently re-derived by a different route than PHOTONICS (§0a) and confirmed identical: genuine convergence, not duplication.
- **Finding 2** [load-bearing] — **ADOPT.** Spot-checked from `results.json`: matches "97x" and "0.849" claims exactly. Real, disclosed data directly in tension with the "clean" framing.
- **Finding 3** — **ADOPT.** A fair, well-reasoned parsimony argument; correctly scoped as not falsifying Prediction 2 as literally scored.
- **Finding 4** — **ADOPT.** Independently confirmed by grep (§0h). A real, silent, zero-marginal-cost-to-fix omission.
- **Finding 5** — **ADOPT.** Fair, appropriately hedged.
- **Argued next change** — **ADOPT**, merged with PHOTONICS's parallel ask into a single Iteration-81 Tier-1 item.

### VISION SCIENCE
- **Finding 1** [load-bearing, program-integrity] — **ADOPT the mechanical claim** (independently confirmed, §0d) — see §3 for the forward-firing status, traced independently rather than taking VISION's own (appropriately hedged) characterization at face value.
- **Finding 2** — **ADOPT.** Agree the vocabulary is optics/instrumentation, not visibility/detectability. Real gap is placement, not overclaim.
- **Finding 3** — **ADOPT.** Reasonable terminology-collision caution, correctly non-actionable this cycle.
- **Finding 4** — **ADOPT.** Confirmed by inspection — no detectability figure is leaned on anywhere in this cycle's predictions.
- **Argued next change** — **ADOPT**, folded into the mandatory-fixes docket.

**No OVERRIDE rulings this cycle.** Every numbered finding across all six reviews, independently checked, holds up.

---

## 2. R20 tally — genuine R4-class defects surviving into Result/Learned

R20's adopted text (verified directly, `LOGBOOK.md:799–844`): *"three or more independent R4-class defects (**a claimed-exact figure, citation, label, or coincidence that does not reproduce from its own cited source**) surviving a document's own Phase-3 prediction-freeze into its Result/Learned sections, each caught only at Phase 5 — not earlier — in a single document, constitutes a Checkpoint-4-grade recurrence pattern on its own, independent of whether any individual instance is load-bearing."*

Auditing every candidate surfaced this cycle, filtered to (a) genuinely R4-shaped **and** (b) located in Result or Learned, **and** (c) caught only at Phase 5:

| Candidate | R4-shaped? | In Result/Learned? | Caught only at P5? | Counts? |
|---|---|---|---|---|
| EM backwards settling-citation | Yes — a claimed comparison figure that doesn't reproduce against its own cited source | Yes (Prediction-4 Result paragraph *and* Learned #2) | Yes | **YES — 1** |
| EM quantization-bias arithmetic slip | Yes (numeric) | No — Setup section | Yes | No (location) |
| MATERIALS Realizability-Bound drop | No — an omitted/broken forward-reference, not a figure/citation/label mismatch | No — the promissory line is in Idealizations | Yes | No (both) |
| PHOTONICS/QUANTUM Nyquist-overclaim | No — an interpretive/methodological overreach, not a figure, citation, label, or coincidence | Yes (Result, Prediction-2 paragraph) | Yes | No (shape) |

**Tally: 1.** Far below R20's "three or more" bar. **R20 does not fire.**

---

## 3. Checkpoint-criteria ruling

**Criteria 1–3**: N/A this cycle (T1:N/A, no mechanism proposed, zero `lab/` diff). Do not fire.

**Criterion 4** — two sub-issues:

### 3a. The disclaimer-erosion question

The Iteration-65 CHECKPOINT entry's escalated remedy, verbatim: *"the 'carried idealizations' banner is now required at BOTH the Predictions section AND the Result section of any future T28 committed-predictions document."* Confirmed mandatory and confirmed to apply to exp-103. VISION's Finding 1 is right that this rule is violated.

But that entry also explicitly states: *"No new numbered rule adopted for the erosion pattern itself"* — unlike R16/R19/R20/R21/R22, this pattern was never given a standing rule with its own forward-firing clause, and a later cycle's own Red Team final audit found no text generalizing Iteration 64's "fires automatically" language to a fifth instance of any kind.

exp-103 is the third post-escalation instance of this sub-pattern, and the first to survive all the way to Phase 5 (two priors were caught at Phase 2, before Predictions/Result text was frozen). A real, worsening trend, worth naming plainly.

**Ruling: Checkpoint criterion 4 does NOT fire on this sub-issue.** Applying the program's own consistently-used discharge test — caught blind, same cycle (Phase 5), before this LOGBOOK entry, non-load-bearing to any scored verdict — and given the confirmed absence of a generalized forward-auto-fire clause, this is ruled non-firing, consistent with unbroken precedent. It IS a mandatory same-shift fix regardless. Flagged for the Director/next lead: a fourth post-escalation instance should be treated as ripe for a standing numbered rule with its own forward-firing clause.

### 3b. The Nyquist-overclaim question

**Ruling: Checkpoint criterion 4 does NOT fire.** Three reasons: (1) the literal, pre-registered Prediction 2 is falsifiable and was honestly scored against its own criteria, unaffected by this finding; (2) constraint #3 is not implicated — this is a purely physical/methodological sampling-adequacy question in a cycle that explicitly disclaims perceptual scoring; (3) direct precedent exists for an affirmative, over-strong prose claim surviving into frozen Result-stage prose, caught blind at Phase 5, non-load-bearing, ruled not Checkpoint-4-firing and logged as an R4/R9-class registry note instead — the same reasoning applies here.

**Combined criterion-4 ruling: does not fire.** Two real, independently-confirmed, non-trivial gaps exist, both correctly caught this cycle, neither individually or jointly meeting this program's own bar for automatic firing, both mandatory same-shift fixes regardless.

---

## 4. Mandatory fixes docket (same-shift, documentation only — no rerun, no verdict changes)

1. **[EM, load-bearing]** Fix the backwards comparison in the Result section's Prediction-4 paragraph and in Learned #2: replace "two to three orders of magnitude **smaller** than VALIDATION.md's own stage-20 canonical figure" with the correct direction — observed residuals are **larger** than the cited 1.5×10⁻⁵ figure, by roughly 2×–73× across the five points — while remaining 180×–6,600× inside the 20% pass tolerance. Prediction 4's verdict is unaffected.
2. **[VISION, mandatory per Iteration-65 escalated rule]** Add the mandatory-fix-8 disclaimer sentence verbatim as the opening line of the Predictions section and the opening line of the Result section.
3. **[MATERIALS, load-bearing]** Restore an actual Realizability Bound section/paragraph to NOTES.md. Carry forward `phase1_proposal.md` §6's two falsifiable expectations verbatim or lightly sharpened, and fold in MATERIALS Finding 4's r_out-vs-(r_out−r_in) hypothesis as a forward note.
4. **[PHOTONICS + QUANTUM, load-bearing, interpretive]** Rewrite the Prediction-2 Result paragraph: the zero-reversal result is weak, not clean, disconfirmation of a fine-scale standing-wave alternative (Nyquist-degenerate pitch); it remains valid, unweakened evidence against the coarser 25–40-cell Fresnel-edge-fringe alternative. Prediction 2's literal scored verdict is unaffected.
5. **[EM, non-load-bearing]** Add one sentence stating no kappa value anywhere in `results.json` approaches or exceeds 1 — the passivity bound is implicitly satisfied everywhere.
6. **[EM, non-load-bearing]** Correct the worked quantization-bias numbers in the Setup's envelope()-vs-phasors() disclosure: ω≈0.071086 (not 0.07111), φ≈1.563895, cos(φ)≈0.0069 (not 0.0064).

No fix in this docket changes any of the four Prediction verdicts, the trust-suite status, or the Combined Verdict below.

---

## 5. Combined Verdict

**PARTIAL.**

All four pre-registered Predictions genuinely clear their own committed criteria, all headline numbers were independently reproduced from primitives by multiple seats and by this audit, `n_fdtd_calls==4`/row-count asserts hold, no `lab/` diff, no mechanism smuggled in, no live Checkpoint criterion fires. This is real, logbook-advancing progress on Gate B's own instrument-trust question — the two diagnosed exp-102 defects are genuinely resolved by construction, and Predictions 1/3/4 hold up to independent scrutiny without qualification.

It is not simply CONFIRMED-clean: Prediction 2's headline claim is scored honestly but its supporting Result-section narrative overclaims what a Nyquist-blind sampling design can demonstrate; a promised Realizability Bound section is missing entirely; a program-mandated dual-section disclaimer banner is absent from both sections it's required in (a third post-escalation recurrence of a named pattern); and one Result/Learned citation runs numerically backwards. None of these change a scored verdict, all are same-shift fixable, none reaches this program's own firing thresholds — but a cycle whose own self-review, four independent Phase-5 seats, and this final audit collectively surface six-plus distinct, confirmed documentation-layer defects is not a clean CONFIRM either.

---

## 6. Reconciled Iteration-81 queue

**Tier 0 — same-shift, this cycle, no new FDTD.** The six-item mandatory-fixes docket (§4) above.

**Tier 1 — cheap, one new minimal FDTD pair (~2 calls, native flagship geometry, reusing this cycle's exact setup).** Merges PHOTONICS's and QUANTUM's argued-next-change paragraphs:
- A genuinely sub-Nyquist re-check: either a contiguous stretch at ≤4-cell pitch across a representative span of [357,457), or `H_REGION` dropped to 1–2 cells at a handful of points.
- At zero further marginal cost from the same capture: restore `Delta_phi` at all 16 points; report `kappa_region`'s own local pointwise std/min/max at each of the 16 x-points.
- **Correction to both reviews' own framing**: this is NOT free post-processing on already-cached fields — `results.json` persists only derived scalars, not raw `Ez` arrays, across cycles. Budget it as one fresh, cheap 2-call pair.

**Tier 2 — the standing top scope item, sequenced after Tier 1.** Tier 1 item 3 (T8 r=78/156/312 near-field-to-witness-scale bridge extension). Sequenced after the Tier-1 Nyquist recheck so the bridge build inherits a ratified sampling convention.

**Tier 3 — standing watch-items, no dedicated cycle required now.**
- EM's flag: a genuine multi-step-count convergence bench for whichever future cycle pushes standoff genuinely nearer-field than x=352.
- THERMODYNAMICS' flag: re-apply this cycle's own cross-resolution rescaling scrutiny to any length/area constant crossing into a future `thermo_sidecar` call on this instrument family.
- The disciplinary flag from §3a: a fourth post-escalation instance of the disclaimer-banner-placement gap should trigger consideration of a standing numbered rule with its own forward-firing clause.

**Tier 4 — already-standing items, carried forward unchanged from NOTES.md's own Next list.**
- Tier 2 (perceptual conversion), T5 (witness-scale wattage), `delta_scene` R3-vs-R4 split (now FOUR consecutive deferrals — Iteration 81 must either execute it or explicitly re-justify a fifth deferral in writing), dense-standoff-trend functional-form fit.
