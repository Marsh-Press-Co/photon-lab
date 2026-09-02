# RED TEAM — Phase-5 FINAL AUDIT, exp-104 (Panel Iteration 81)

**Seat: RED TEAM. Sees Phase-1 proposal record + all six blind Phase-5 reviews (condensed). Standard: not textbook-physics compliance — kills internal inconsistency, unfalsifiable claims, mechanisms inexpressible as simulation parameters, and quiet constraint drift, especially #3. Never leads; has no proposal of its own to protect.**

Every finding below was independently re-derived from primitives — `run.py`, `results.json`, `NOTES.md`, `LOGBOOK.md`, `PANEL.md`, exp-102's and exp-103's own `run.py`/`results.json` — not taken on any reviewer's word. `run.py --predictions-only` was executed live (a second independent confirmation of VISION's own claim).

---

## 0. Independent primitive-level re-verification (show work)

**(a) QUANTUM's monotonicity claim.** Pulled `residual_point` for all 53 `DENSE_X` points directly from `results.json` and checked each quintile's raw sequence by hand:
- Q0 (x=352→372, 11 pts): 0.0018838 → 0.0029112, strictly increasing, 10/10 positive diffs.
- Q1 (x=374→394, 11 pts): 0.0030375 → 0.0042224, strictly increasing, 10/10 positive diffs.
- Q2 (x=396→416, 11 pts): 0.0043903 → 0.0062211, strictly increasing, 10/10 positive diffs.
- Q3 (x=418→436, 10 pts): 0.0065138 → 0.0080724, strictly increasing, 9/9 positive diffs.

**Confirmed exactly**: zero internal sign changes in the raw increments across Q0–Q3 — 39/39 consecutive diffs positive. Q4 (x=438→456) is the sole exception: 4 of its 9 diffs are negative (a real up/down wiggle, consistent with its own FFT-determined in-band period). QUANTUM's diagnosis is correct and precise.

**(b) A sharper version of PHOTONICS' P2-structural-blindness finding, independently derived.** Checked whether `residual_point` ever crosses zero across the full 53-point span: **it does not — all 53 values are strictly positive** (range ≈0.0019–0.0088). Since P2's reversal test (`np.sign(res_seq[i]) != np.sign(res_seq[i-1])`) can only fire on a *value*-sign flip, not an increment-sign flip, P2 is not merely "structurally blind to a ripple riding on a smooth positive baseline" in the abstract — it is blind to the *specific, genuine, in-band wiggle Q4 actually contains*. Q4's own peak-to-peak `residual_point` amplitude is `0.000572` against a local baseline of `~0.0083–0.0088`: the wiggle would need to be **~15× larger** than it actually is before it could ever cross zero and register as a "sign change," regardless of the 5%-relative-amplitude threshold layered on top. P2's "0 qualifying reversals ⇒ no ripple anywhere" framing is not merely optimistic phrasing — for this quantity's regime, P2 is structurally incapable of ever falsifying a ripple that doesn't first clear the residual's own DC offset from zero. This sharpens, not merely repeats, PHOTONICS' finding.

**(c) PHOTONICS' Q4/P4 sinc-mismatch claim.** Independently recomputed `predicted_ratio(p=9.06634619846641)`:
```
sinc(11/p) = -0.16292574547691432
sinc(1/p)  =  0.9801081014602222
predicted_ratio = sinc(11/p)/sinc(1/p) = -0.16623242398892332
```
Matches `results.json`'s stored `predicted_ratio` to every digit. Stored `measured_ratio = 3.677420740011675`. **Wrong sign confirmed** (predicted negative, measured positive); **magnitude ratio confirmed at 22.12×** (`|measured/predicted|`). PHOTONICS' claim is exact, not an approximation.

**(d) The R23-coverage-gap claim.** `grep -n "assert" run.py` returns exactly 8 hits: two structural invariants (`BEHIND_*` tuple, `len(ALL_X)==16`), one shape invariant (`len(DENSE_X)==53`), two margin-gate asserts, one FDTD-call-count assert, and **exactly two `DISCLAIMER`-referencing asserts** (`assert DISCLAIMER in PREDICTIONS_TEXT`, `assert DISCLAIMER in result_text`). `grep -n "DISCLAIMER"` returns 4 hits total (the constant's definition + its 2 f-string interpolations + the assert already counted). By contrast, the MATERIALS aliasing-origin sentence, the THERMODYNAMICS N/A sentence, and the λ/scope-only idealization exist **only** in the module docstring (lines 44–86) and in `NOTES.md`'s prose — grepping either sentence's characteristic text against `assert` or against `PREDICTIONS_TEXT`/`result_text`'s f-string bodies returns nothing. **Confirmed exactly as MATERIALS, THERMODYNAMICS, and PHOTONICS each independently found**: R23's code enforcement covers exactly one disclaimer.

**(e) Q3 shares the excluded quintiles' own artifact signature — independently found, corroborating and sharpening QUANTUM's Gap 1.** Read every quintile's `period_diag` field directly: Q0/Q1/Q2 (excluded, near-null) all report `peak_idx=4, nfft=64`. **Q3 — scored in P4/P5, NOT excluded — also reports `peak_idx=4, nfft=64`** (`interp_bin=4.356`, vs Q0's `3.934`, Q1's `3.942`, Q2's `3.931`). All four quintiles lock onto the *identical* raw FFT bin despite covering four different 10–11-point x-stretches; only the sub-bin interpolation (driven by each quintile's own smooth-curvature shape) nudges the continuous-valued period estimate across or short of the 10%-of-33-cells exclusion boundary (Q0–Q2 land at 29.4–32.9 cells → within 10% of 33; Q3 lands at 29.4 cells → 32.9% away from 33, just outside). The near-null exclusion is a **derived-period** proxy for an **raw-bin-identity** phenomenon, and the proxy has a false negative here. QUANTUM's Gap 1 is not merely plausible — it is directly demonstrated by the diagnostic fields already sitting in `results.json`.

**(f) EM's `kappa_window` provenance claim.** Read exp-103's own `results.json.kappa_window`: `pointwise_max = 0.07250328395401615`, `pointwise_min = 0.0007487406954119105`, `pointwise_std/pointwise_mean = 0.015864562708848298/0.01868984554416697 = 0.8489…` (matches the cited "std/mean=0.849" and "97× min/max": `0.07250.../0.0007487... ≈ 96.85×`). Cross-checked exp-104's own `results.json.point_channel["456"].kappa_region_point = 0.07250328395401615` — **bit-identical** to exp-103's `pointwise_max`, to all 17 significant digits. EM's claim that exp-103's cited "evidence of comparable-scale structure" traces to a single centerline point at the window's own far edge (the smooth radial falloff's own maximum, not λ/2 structure) is confirmed exactly, digit-for-digit — not approximately.

**(g) Gate P1 exactness.** All 16 `p1_rows` entries in `results.json` show `rel: 0.0` verbatim (not merely `<1e-9`) — `max_rel: 0.0`. Confirmed literally exact, not rounded.

**(h) Citation accuracy (EM's "no R4-class defect" self-finding).** Read `experiments/103-.../run.py:102` directly: `EDGE = 40  # TAPER (...)`. Matches NOTES.md's citation exactly (not `R4_TAPER=80`). Read `experiments/102-.../run.py`: `point_intensity` def at line 406, its `return` at line 407; the `delta_phi = float(np.angle(mean_a / mean_e))…` line at line 417. Both citations exact. **Zero R4-class defects found in Setup's citations.**

**(i) The floor-gate empty-only convention (EM's low-priority finding).** `floor_gate()` is called twice, both times over `i_region_empty`/`i_point_empty` pools only (`run.py` lines 518–519) — confirmed, the article-side numerator is never floor-gated, exactly as EM stated, inherited unchanged from exp-102/103.

**(j) THERMODYNAMICS' grep claims.** `grep -n "thermo_sidecar"` on `run.py` returns zero hits; `grep -n "sigma_ext\|ratio_abs_ext\|thermal"` on `results.json` returns zero hits. Confirmed.

**(k) VISION's live-execution and R23-registry claims.** Ran `python3 run.py --predictions-only` myself: prints `PREDICTIONS_TEXT` (disclaimer included) and exits 0 — the two `assert DISCLAIMER in ...` calls are live-fired on the predictions path, not merely present as inert code (the predictions-only path only exercises the first assert; the result-block assert was independently confirmed by the fact that `results.json`'s own `result_text` field, generated by the same real Phase-4 run, contains the disclaimer verbatim — the assert would have raised `AssertionError` and prevented `results.json` from ever being written otherwise). `grep -n "R23" LOGBOOK.md` returns **zero hits** — confirmed, VISION is correct that R23 is not yet in the registry.

That is eleven independent primitive-level re-derivations, spanning all six reviews plus two novel findings of Red Team's own (§0b, §0e).

---

## 1. Ruling on every review's findings

### PHOTONICS (CONFIRM-WITH-GAPS)
- P2 structural-blindness finding — **ADOPT**, and sharpened (§0b): not just abstractly blind, but demonstrably blind to the one region that actually oscillates.
- Q0/Q1/Q2 identical FFT bin, stronger corroboration than stated — **ADOPT**, and extended (§0e): Q3 shares it too, a fourth instance PHOTONICS did not report.
- No R23-style assert for the λ/scope-only disclaimer — **ADOPT** (§0d).

### MATERIALS (CONFIRM)
- Aliasing-origin disclaimer present, unaltered, correctly un-triggered — **ADOPT** (direct textual match confirmed by inspection, run.py docstring lines 44–54 vs. NOTES.md Idealizations, verbatim).
- R23 covers only the perceptual `DISCLAIMER` — **ADOPT** (§0d).

### ELECTROMAGNETISM (self-review, CONFIRM)
- P2's null is a genuine, robust zero (value-sign, not merely "qualifying") — **ADOPT**, confirmed exactly (§0b: all 53 values positive).
- `kappa_window`'s cited evidence traces to a single centerline point at the window's own far edge — **ADOPT**, confirmed digit-for-digit (§0f), the single sharpest citation-tracing in this round.
- Floor gate never gates the article-side numerator (low priority, inherited) — **ADOPT**, confirmed (§0i). Correctly triaged as low-priority/Next-cycle, not a same-shift blocker — it changes no verdict this cycle (both channels' floor gates already pass 0/16 and 0/53 unresolved on the empty pool alone).
- No R4-class citation defect found — **ADOPT**, independently re-confirmed (§0h).

### QUANTUM OPTICS (CONFIRM-WITH-GAPS)
- Raw monotonicity in Q0–Q3, zero internal sign changes — **ADOPT**, confirmed exactly (§0a).
- "Numerical beat" language is technically imprecise; true diagnosis is spectral leakage — **ADOPT**. A beat requires two genuine, distinct frequency components; what is actually present is a single smooth monotonic trend (a Taylor-expansion-scale curvature mismatch between a point sample and a box average of the same underlying field) leaking into the FFT's lowest non-DC bin because the trend is not periodic within the analysis window. "Beat" implies periodicity that is not present in the raw data (§0a). Mandatory same-shift language fix (applied below).
- Q0/Q1/Q2 lock onto the identical bin, period/window_span ~constant (~1.62–1.63) — **ADOPT**, independently recomputed: Q0 32.540/20=1.627, Q1 32.469/20=1.623, Q2 32.558/20=1.628. Confirmed.
- Near-null exclusion arithmetic verified by hand — **ADOPT**, independently re-verified for all 5 quintiles (Q0: 0.0418, Q3: 0.3287, Q4: 0.1758 — all match `results.json`'s `near_null_frac_of_11` to 3–4 significant figures).
- Gap 1 (Q3 shares the excluded quintiles' leakage signature; P4's "1 pass" is really "0 meaningful comparisons") — **ADOPT**, independently confirmed and demonstrated directly from `period_diag`, not merely argued (§0e) — the single most consequential finding of the round.
- Gap 2 (P5's 2/2 rests on the same two dubious quintiles) — **ADOPT**, follows directly from Gap 1: if Q3 is spurious and Q4 already fails its own P4 sign/magnitude test, P5's "sign-consistent covariation" is being computed on a spurious-artifact quintile and an internally-contradicted quintile, not two genuine confirmations.

### THERMODYNAMICS (CONFIRM, with process gap)
- Zero `thermo_sidecar.py` calls, zero thermal fields — **ADOPT**, confirmed (§0j).
- R23 doesn't cover the thermal N/A disclosure — **ADOPT** (§0d).

### VISION SCIENCE (CONFIRM-WITH-GAPS)
- R23 asserts genuinely fire, live-executed — **ADOPT**, independently re-confirmed by a second live execution (§0k).
- Byte-identical disclaimer text, zero leaked perceptual vocabulary — **ADOPT**, confirmed by direct string inspection of `results.json`'s `predictions_text`/`result_text` fields against `NOTES.md`'s own Predictions/Result blocks (character-for-character match, "not present in" wording present, "NOT visible in" absent).
- Deepest structural critique: R23 proves transcription-fidelity, not content-adequacy/placement/generality — **ADOPT as a real, correct critique**. Ruled NOT immediately remedy-worthy this shift; see §3.
- R23 not yet in LOGBOOK's registry — **ADOPT**, confirmed independently (§0k). This is a sequencing item for whoever writes the Iteration-81 LOGBOOK entry, not a NOTES.md defect — flagged, not charged against this cycle's verdict.

**Zero overrides across all six reviews.** Every claim checked reproduced from primitives exactly; two (§0b, §0e) were independently sharpened beyond what any single review stated.

---

## 2. Red Team's own numbered attacks

**Attack 1 [inconsistency].** NOTES.md's Learned #2 calls the Q0–Q3 artifact a "numerical beat," but the raw data this document itself generated rules that out: a beat requires interference between two distinct frequency components, and the raw `residual_point` sequence in Q0–Q3 is strictly monotonic with zero internal sign changes (§0a) — there is no oscillation to beat against. **ADOPT — mandatory same-shift fix**: replace "beat" language with "spectral leakage of a smooth monotonic trend," per QUANTUM's more precise diagnosis. Applied below.

**Attack 2 [inconsistency].** The Interpretation section presents "0 qualifying reversals" as freestanding, headline-grade proof that "no ripple, real or artifactual, was found in the first place," without disclosing that P2's test cannot, in this quantity's regime, ever detect the one genuine in-band wiggle the run's own data contains (Q4, period 9.07 cells, ptp amplitude ~15× too small to ever flip `residual_point`'s sign — §0b). The actual disproof of Q4 as a real λ/2-scale ripple is P4's sign+magnitude mismatch, not P2. Presenting P2's "0 reversals" as the headline, with P4 relegated to a supporting sentence deep in the Interpretation paragraph, inverts which test is actually load-bearing. **ADOPT — mandatory same-shift fix**: reframe the headline to name P4 as the operative disproof of the sole candidate, and disclose P2's structural limitation explicitly. Applied below.

**Attack 3 [inconsistency].** P4's "1 pass" and P5's "2/2 CONFIRMED" are computed over Q3 and Q4. Q3 shares the identical raw FFT bin (`peak_idx=4, nfft=64`) with the three near-null-excluded quintiles (§0e) — the near-null exclusion is a period-based proxy for exactly this raw-bin-identity artifact, and the proxy has a demonstrated false negative on Q3. Scoring Q3 as a "pass" while excluding Q0–Q2 for what is diagnostically the same underlying leakage is an inconsistent application of the exclusion rule's own intent (not its literal text — the literal text is followed correctly; the *purpose* is not achieved). **ADOPT — mandatory same-shift fix**: reframe P4's "1/2 pass" and P5's "2/2" as resting on evidentiarily weak ground (one likely-spurious quintile, one quintile that already fails its own P4 test), per QUANTUM's Gaps 1–2. Applied below.

**Attack 4 [unfalsifiable — narrowly scoped].** R23's own adopted text ("a disclaimer required in multiple document sections must be enforced by a code-level assert on a single source-of-truth string") is general; a claim that "R23 is ratified and IMPLEMENTED" cannot itself be verified against that general text from the code alone, because the code only checks one of at least three multi-section disclaimers this document carries (§0d). This is a scope/completeness gap between a rule's stated generality and its delivered implementation, not a claim about physics. **Ruled real but not Checkpoint-4-grade this cycle** — see §3 for full reasoning. **ADOPT — mandatory same-shift fix**: an explicit scope-limitation statement in NOTES.md's R23 section, stating plainly that the code-level assert covers the perceptual disclaimer only. Applied below.

**Attack 5 [inexpressible].** None found. R23's mechanism (a string constant + two asserts) is fully expressible as simulation-adjacent code and was confirmed to actually run (§0k) — no attack here.

**Attack 6 [constraint-#N-violation].** None found. This cycle touches zero `lab/` code and scores none of the four physical witness-statement constraints by design (T1: N/A, explicitly stated and confirmed by `git diff --stat` showing zero `lab/` changes) — constraint 3 (Red Team's own special-attention constraint) is untouched, not quietly dropped. No attack here.

---

## 3. Rulings

### 3.1 The R23-coverage gap (cross-cutting pattern, four seats)

**Ruled: a normal same-shift documentation fix + Iteration-82 queue item, NOT Checkpoint-criterion-4-grade.**

Reasoning: Checkpoint criterion 4 fires on "unfalsifiable claims" or "a constraint quietly dropped — especially #3." Neither applies literally: the MATERIALS/THERMODYNAMICS/scope disclaimers are not unfalsifiable — they are true, complete, verbatim-consistent statements, independently confirmed by direct string comparison (§0). What is missing is *code enforcement* of that consistency, not the consistency itself. And no witness-statement constraint (1–4) is implicated at all — this experiment scores none of them by design. This is a rule-completeness gap, not a program-integrity failure in the sense Checkpoint 4 targets.

It also matches this program's own unbroken discharge-test precedent, applied identically to the Iteration-78/79/80 disclaimer-erosion and Nyquist-overclaim rulings: the gap was caught blind, by four independent seats, in Phase 5 — before this LOGBOOK entry, before any external reader saw it, and it is non-load-bearing to every scored verdict (P1–P6 stand unaffected). This is the textbook shape of "caught blind, same cycle, before LOGBOOK" that has never fired Checkpoint 4 on its own in this program's history.

One further reason this is not yet ripe for an automatic-firing rule the way R20 is for R4 recurrences: this is R23's *founding cycle*. R23 itself was only just implemented this shift; a scope question discovered in a rule's first real use is a design refinement, not a recurrence pattern. (Contrast with R20, which required *three* independent instances of the *same* failure shape before it became a standing automatic-fire rule — R23's coverage gap has exactly one instance on record: this one.)

**Same-shift requirement**: NOTES.md must state the scope limitation explicitly, not imply completeness by silence. Applied below. **Iteration-82 queue item**: either genericize R23's implementation (a small `(sentence, required_locations)` table checked in a loop) or formally ratify R23 as intentionally single-disclaimer-scoped with a placeholder for a future generic rule if a second multi-section-disclaimer-drift instance is ever found uncovered by code.

### 3.2 VISION's legibility-vs-transcription critique of R23

**Ruled: correctly scoped as an Iteration-82 queue item, not an immediate same-shift structural remedy.**

Reasoning: VISION's critique is a valid, well-argued *general* observation about what any substring-assert mechanism can and cannot prove (content adequacy, placement/prominence, and third-location generality are all outside what `assert X in Y` can ever certify). But it is not a report of a live defect in *this* document: VISION's own review confirms the disclaimer here is not gutted, not buried, and does not need a third location this cycle. There is no active problem to remedy same-shift — only a designed-in ceiling on what R23 can certify, correctly named for the first time. Mandating a fresh-context cold-read process step retroactively, on a cycle where nothing it would have caught actually went wrong, would be exactly the kind of process-overreaction Red Team should resist as much as it resists under-scrutiny. **Queue it**: trial VISION's fresh-context cold-read as a supplementary (not replacement) Phase-5 check at Iteration 82, with an eye toward a possible new numbered rule if it catches something a substring-assert structurally cannot.

### 3.3 R20 tally

**Ruled: zero R4-class defects found this cycle.** Every citation independently re-checked (§0f, §0h) reproduces exactly from its cited source: exp-103's `EDGE=40` at line 102, exp-102's `point_intensity`/`delta_phi` at lines 406–407/417, exp-103's own `kappa_window` provenance traced digit-for-digit. Gate P1 is exact to `0.0` relative deviation, not merely `<1e-9`.

This is a *cleaner* citation-hygiene record than exp-103 (1 R4-class defect, non-firing) or Iteration 78/exp-101 (3, R20's only firing to date). **The distinction between a citation-reproduction failure and an evidentiary-strength/framing critique matters to R20's own definition, and is dispositive here, not incidental**: R20's text requires "a claimed-exact figure, citation, label, or coincidence that does not reproduce from its own cited source." The "beat" mislabeling (Attack 1) is a physical-mechanism description, not a citation to an external source. The P2-headline-overstatement (Attack 2) and the P4/P5-evidentiary-weakness findings (Attack 3) are about how strongly the *evidence supports the verdict label already correctly computed by the code* — not about a false restatement of a cited number. This is precisely the same distinction this program has already drawn and ruled on twice (Iteration 78's `Q_ext→2`/`cosθ` finding ruled R9-shaped not R4-shaped; Iteration 80's Nyquist-overclaim and dropped-Realizability-Bound findings ruled "interpretive overreach... not R4-shaped"). Applying it consistently here: **R20 does not fire; the count is 0, not a close call.**

### 3.4 Checkpoint criteria (PANEL.md's five)

1. **Configuration passes all constraint metrics** — N/A. This cycle scores no witness-statement constraint.
2. **Proven mechanism-class boundary** — N/A. No mechanism proposed or varied this cycle (T1: N/A, confirmed).
3. **Synthesis requiring engine physics beyond validated bench classes** — N/A. Zero `lab/` diff.
4. **Program-integrity drift** — **does NOT fire.** Ruled in full at §3.1–3.2 above: the R23-coverage gap and VISION's legibility critique are both real, both caught blind pre-LOGBOOK, both non-load-bearing, neither a dropped constraint nor an unfalsifiable claim in the actual scored record.
5. **Two consecutive iterations with no logbook-advancing result** — N/A. Iteration 80 (exp-103) delivered a genuine footprint/aperture-matched Gate B rebuild (PARTIAL); this cycle delivers a genuine, cleanly-gated closure of the exact methodological gap that motivated it. Two consecutive advancing results, not two consecutive nulls.

**Zero criteria fire this cycle.**

---

## 4. Red Team's own final verdict

**Combined Verdict: PARTIAL.**

The substantive science is strong and, on Red Team's own independent re-derivation, essentially unimpeachable: Gate P1 reproduces to literal `0.0` relative deviation; the genuinely sub-Nyquist 2-cell-pitch, zero-averaging point channel finds no value-sign-changing ripple anywhere across the full 104-cell span (P2); the one candidate with an in-band period is decisively disproved by an independently-recomputed, digit-exact sinc mismatch (wrong sign, 22.12× magnitude — P4/§0c); P6's scope margins are wide (max ripple_fraction 0.138 against a 0.20 bar); and the cycle carries **zero R4-class citation defects**, a cleaner record than either of the two prior T28 cycles. This directly, honestly answers the concern that motivated the whole cycle — exp-103's own Phase-5-flagged degenerate-aliasing risk does not, on a genuinely resolved recheck, turn up the ripple it could have been masking.

That is weighed, per this program's own PARTIAL convention, against a real cluster of same-shift-fixable weaknesses the frozen document did not honestly carry before this audit: a physically-imprecise "beat" label in Learned (Attack 1); a headline that oversells what P2's own test can prove and under-credits what P4 actually establishes (Attack 2); P3/P4/P5's sub-verdicts resting on evidentiary ground weaker than their FALSIFIED/CONFIRMED labels suggest, independently demonstrated (not merely argued) via the shared raw FFT bin across four of five quintiles (Attack 3); and a rule (R23) whose delivered scope is narrower than its own general text, independently found by four of six seats plus Red Team's own re-derivation (Attack 4). None of these changes P1–P6's scored verdicts. None is R4/R20-shaped. None fires Checkpoint 4. All are same-shift fixable and are fixed below. That is exactly the shape of a PARTIAL cycle in this program's own established sense — a genuinely-reproduced primary result carrying real, confirmed, non-load-bearing documentation-layer drag that a clean CONFIRM would not carry.

---

## 5. Mandatory same-shift NOTES.md fixes (applied this audit, zero re-run, zero verdict change)

1. Interpretation: reframe the P2/P4 headline — name P4's sign+magnitude sinc mismatch as the operative disproof of the sole in-band candidate (Q4), and disclose P2's structural inability to ever detect a ripple that doesn't first clear `residual_point`'s own positive DC offset from zero.
2. Interpretation: add the Q3-shares-Q0–Q2's-raw-FFT-bin finding, and reframe P4's "1/2 pass" and P5's "2/2" as resting on weaker evidentiary ground than their labels suggest (one likely-spurious quintile, one internally-contradicted quintile) — without changing either scored verdict.
3. Learned #2: replace "numerical beat" with "spectral leakage of a smooth monotonic trend" (QUANTUM's more precise diagnosis, independently confirmed via raw-data monotonicity, §0a) and cite the Q3-bin-sharing finding as the sharper evidentiary basis for the near-null-exclusion lesson.
4. R23 section: add an explicit scope-limitation sentence — the code-level assert covers the perceptual disclaimer only, not the MATERIALS/THERMODYNAMICS/scope-only disclaimers, which remain manual prose this cycle.
5. Next: add two Iteration-82 queue items — (a) R23 scope-extension-or-explicit-limitation decision; (b) VISION's fresh-context cold-read as a trial supplementary Phase-5 check; (c) generalize the near-null-exclusion proxy for any future per-quintile-FFT reuse, since it has a demonstrated false negative (Q3) on its own diagnostic grounds.
6. Append a "Phase 5 outcome" section (this audit's own summary), matching exp-103's own established NOTES.md convention.

(All six applied directly to `NOTES.md` in this same commit — see the diff.)

---

## 6. Reconciled Iteration-82 queue (Red Team's own tiered ranking)

**Tier 1 — zero-to-cheap-FDTD, ready now:**
1. **T8 r=78/156/312 near-field-to-witness-scale bridge extension.** The consensus top pick across this cycle's own Next section and exp-103's own Iteration-81 tiering — now unblocked: this cycle's clean, zero-R4-defect null result on the sub-Nyquist question is a reasonable basis to extend the wide-channel convention to the bridge-family radii without re-litigating pitch/Nyquist concerns there.
2. **R23 scope decision** (§3.1, §5 item 4/5a): genericize the code-level assert to cover all multi-section disclaimers this document carries, or formally ratify R23 as intentionally single-disclaimer-scoped. Four of six seats independently flagged this; it should not go a second cycle without an explicit decision.
3. **Near-null-exclusion rule refinement** for any future per-quintile-FFT reuse (§0e, QUANTUM's Gap 1): supplement the period-based proxy with a direct raw-bin-identity check (e.g., flag any quintile whose `peak_idx` matches an excluded quintile's, independent of where the continuous-valued period estimate happens to land).

**Tier 2:**
4. **VISION's fresh-context cold-read**, trialed as a supplementary Phase-5 check (§3.2) — not a replacement for R23's assert, a complement to it.
5. **Multi-step-count settling convergence bench across the full dense span** (x=352–456, not just x∈[352,356]) — this cycle's own explicit Idealization gap, unresolved for a second cycle now.

**Tier 3:**
6. **The standing `delta_scene` R3-vs-R4 split** — now FIVE consecutive deferrals (exp-100→101→102→103→104). Per exp-103's own explicit written warning, a sixth deferral at Iteration 82 must be re-justified in writing, not silent, or executed.
7. Standing lower-priority items, unchanged from exp-103's own Tier 4: the Tier-2 perceptual conversion (gated on item 1 above), witness-scale source-wattage pinning, the dense-standoff-trend functional-form fit, and EM's floor-gate-empty-only-convention note (§0i, low priority, non-load-bearing, worth a one-line disclosure whenever the floor-gate convention is next touched).

Full record: `NOTES.md`, `run.py`, `results.json`, this file. Six blind Phase-5 reviews were received condensed (not as separate committed files this cycle) and independently re-verified from primitives throughout §0–§1 above.
