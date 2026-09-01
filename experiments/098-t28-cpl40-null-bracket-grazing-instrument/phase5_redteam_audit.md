# Panel Iteration 75 — Phase 5 FINAL AUDIT (RED TEAM), exp-098

*Speaks last, sees everything: the frozen record (NOTES.md/results.json/run.py),
my own Phase-2 audit this cycle, and all six blind Phase-5 reviews
(PHOTONICS, MATERIALS, EM, THERMODYNAMICS, QUANTUM OPTICS, VISION SCIENCE —
unanimous CONCUR-WITH-GAP(S)). Every headline finding below is independently
re-derived from `results.json`/`run.py`/`NOTES.md`/exp-097's own NOTES.md
this session — none is adopted on a reviewer's word alone. Standard: not
textbook-physics compliance — internal inconsistency, unfalsifiable claims,
inexpressible mechanisms, and quiet constraint drift, especially #3.*

## 0. Independent re-verification log (numbers reproduced this session, not trusted)

- **Richardson ratio.** `crossing_cpl40_B = 39.921519316666235`,
  `THETA0_B = 40.26541960305772`, `shift_20_30 = -0.1935812644838535`.
  `theta(cpl30) = THETA0_B + shift_20_30 = 40.07183833857387`.
  `shift_30_40 = crossing_cpl40_B - theta(cpl30) = -0.15031902190763446`.
  `ratio_marginal = shift_30_40 / shift_20_30 = 0.7765163757372424`.
  Identity check: `1 + ratio_marginal = 1.7765163757372424`, exactly the
  code's own reported `observed_ratio` — confirms both numbers are
  internally consistent, just measuring different pairings (cumulative/
  marginal vs. marginal/marginal). **MATERIALS' 0.777 figure reproduces to
  full float precision.**
- **GP2′ curve, [50.5°, 89.5°] band.** Scanned all 79 points programmatically:
  **9 VALID** (52.0, 52.5, 53.0, 53.5, 54.0, 54.5, 60.5, 61.0, 69.5°), 70
  MARGINAL, 0 INVALID — exact match to PHOTONICS/THERMODYNAMICS' lists.
  69.5° (VALID) sits inside the θc≈59–73° corroboration band, confirmed.
  **Tail 74.0°–89.5° (32 points): 0 VALID, all 32 MARGINAL** — no recovery
  anywhere in this sub-range, confirming PHOTONICS' shape-divergence claim
  as at minimum internally consistent with the raw curve.
- **Row/call count.** `item_i` A+B+C = 12 distinct angle rows; `item_ii` = 4
  new + 2 reused = 6 rows. **16 new distinct rows, 18 total including the 2
  reused** — not 64. `fdtd_calls=64` confirmed as `16 angle-points × 2
  legs × 2 empty/article conditions = 64`, the call count, not a row count.
- **FI-G″.** Grepped exp-097's own `NOTES.md` line 517 directly: *"`FI-G″`
  (native_ny corrupted) optional, cheap to bundle in the same commit"* —
  named explicitly in exp-097's own Reconciled Next queue item 2. Grepped
  exp-098's `run.py`/`NOTES.md` for `FI-G″`/`native_ny` corruption: zero
  hits — `run_fi_g_prime()` (run.py:308-334) corrupts only `native_absorb`
  (41 not 40); `native_ny=1584` is used as the *true, uncorrupted* value in
  every leg. Confirmed: FI-G″ was named by name in the prior cycle's queue
  and never mentioned, run, or disclosed-as-deferred anywhere in exp-098.
- **Banner placement.** `grep -n "Carried idealizations banner"` →lines 338
  and 366. Line 338 precedes `## Predictions` (line 344) — it sits in
  `## Idealizations`, referencing §Predictions by name but not physically
  inside it. `sed -n '345,363p'` (the Predictions section body) contains no
  banner text. Line 366 sits immediately inside `## Result`. Confirmed
  exactly as VISION reported.
- **GP1 formula.** Read `lab/ambient.py` directly: `weber(b_obj,b_flank) =
  (b_obj-b_flank)/b_flank`; `window_means()` computes spatial windowed
  *means* of whatever profile it's given — here a signed Poynting-vector
  component (`Sx`), not a closed-surface flux integral. `C≥-1 ⟺ b_obj≥0` by
  algebra. Confirms EM's self-critique: this is the program's own
  ambient-scene silhouette-contrast formula, repointed at a signed
  quantity, not a derived consequence of Poynting's/passivity theorems
  (which bound *net* flux through a closed surface, not one windowed local
  vector component in an interference pattern where local backflow is
  ordinary).
- **Idealization 47 (bonus, THERMODYNAMICS' find, independently confirmed).**
  Grepped every call site of `run_checks_1234_and_7` and `registration_preflight`
  in `run.py`: only ever invoked from `run_r4_batch()`, only ever called
  with `angles_sorted` (item i, new angles) or `NEW_ANGLES_II` (item ii, the
  4 *new* angles). **38.49 and 38.69 never appear as arguments to the
  registration gate anywhere in this file.** Idealization 47's claim that
  the reused rows were "re-verified this cycle by running that same gate
  against their exact tuple" is FALSE as written — the only check actually
  run against them is the netd-key-coverage assert at import time (a real
  but different guarantee). Confirmed independently; adding this to the
  record below as a seventh confirmed defect, not one of the original six
  but caught the same way (source read, not trust).

## 1. Ruling on the six headline findings

| # | Seat(s) | Finding | Ruling | Independent verification |
|---|---|---|---|---|
| 1 | QUANTUM OPTICS | FI-G′ only exercises the `native_absorb`-driven half of the `y_lo`/`y_hi` branch; `native_ny` (the only input that moves `y_hi` independently of `y_lo`) has zero fault-injection coverage across this program's entire history. exp-097's own Next queue named this as `FI-G″`, "optional, cheap to bundle." exp-098 silently dropped it — no mention, no disclosed deferral. | **ADOPT, in full.** | Confirmed both halves at source (§0): the queue item's exact text, and `run.py`'s exact silence on `native_ny`. The "closes the gap... left open" language (item iv-c, repeated in Result) is a genuine overclaim — it closes only the `absorb`-driven portion. |
| 2 | PHOTONICS + THERMODYNAMICS | Result's "flags MARGINAL continuously... the ENTIRE upper half" is factually wrong against `gp2_curve`: 9 VALID points are interspersed, including 69.5° *inside* the θc≈59–73° corroboration band. PHOTONICS additionally flags an unexamined shape divergence in the 74°–89.5° tail (persistent MARGINAL, no recovery, unlike exp-086's own ptp measure which falls back below its pre-peak shoulder by θc=75–77°). | **ADOPT both.** | Independently recomputed the full 79-point band and the 32-point tail myself (§0) — exact match on both counts, including the tail's 0/32 VALID. I did not independently re-derive exp-086's own `ptp` values from `phase4_rescore_results.json` this session (out of this audit's critical path — Red Team's own Phase-2 audit already verified the θc≈59–73°/5,444×–6,631× figure at source), but PHOTONICS' comparison is internally coherent with the GP2′ numbers I did check, and the claim ("exp-086's own trend would predict recovery, never surfaced") is a legitimate, falsifiable, currently-unexamined gap, not speculation. |
| 3 | MATERIALS | `richardson_style_diagnostic()` divides a **cumulative** cpl20→40 shift by a **marginal** cpl20→30 shift — a category-mismatched comparison. Correctly-paired marginal/marginal ratio (cpl30→40 ÷ cpl20→30) is 0.777 (shrinking, same direction as expected), not the reported 1.777 (growing) — an opposite-direction characterization. | **ADOPT, in full.** | Recomputed independently from raw `results.json` crossing values (§0): 0.7765163757372424, matching MATERIALS to full precision, with the algebraic identity `1+ratio_marginal=observed_ratio` confirming both figures are internally consistent, just different pairings. Learned #3's "growing faster than 2nd-order... MORE open, not less" does not survive this correction — the corrected number is mildly *reassuring*, not alarming. |
| 4 | THERMODYNAMICS + EM | NOTES.md's Result claims the `netd_row()` assert covered "64 real-FDTD report rows" — the actual distinct row/data-point count is 16 new (18 incl. 2 reused); 64 is the FDTD *call* count. Identical error class to this cycle's own already-disclosed 32-vs-64 *calls* miscount, recurring one paragraph later in the same document. | **ADOPT, in full.** | Independently counted item_i (12) + item_ii (4 new, 2 reused) = 16/18, confirmed 64 = 16 points × 4 calls/point (2 legs × 2 conditions), matching the task's own "4 calls per row" framing exactly (§0). The underlying coverage itself is not in dispute (100%, exhaustively re-checked by THERMODYNAMICS) — only the count label is wrong. |
| 5 | VISION SCIENCE | The Predictions-side carried-idealizations banner sits in the closing paragraph of `## Idealizations`, naming "§Predictions" but not physically inside the `## Predictions` section body — a milder recurrence of last cycle's placement-not-substance gap. | **ADOPT, in full.** | Grepped and read section boundaries directly (§0): confirmed exactly — line 338 precedes the `## Predictions` header at line 344; the Predictions body (345–363) carries no banner text of its own. |
| 6 | ELECTROMAGNETISM (self) | GP1's "hard passivity floor" framing overclaims: local windowed non-negativity of one signed Poynting-vector component is not what passivity/energy-conservation theorems guarantee (they bound net flux through a closed surface). PASS result is correct; physics justification oversells its derivation. Also: confirms Red Team's own `netd_row()` assert fix is robustly implemented, three independent enforcement points, no bypass. | **ADOPT, in full, on both parts.** | Read `lab/ambient.py::weber`/`window_means` directly (§0) — the formula is exactly the program's reused Weber-contrast machinery pointed at a signed quantity; nothing in it derives from a closed-surface flux argument. Also independently re-read `run.py`'s three enforcement points (per-row inline at 179–181, aggregate at 464–470, import-time reused-row check at 118–120) in a single linear `main()` with no `try/except` and exactly one `json.dump` — confirmed no bypass path exists. |

**Seventh, additional confirmed defect (not among the assigned six, caught the same way — source read, not trust):** Idealization 47's "re-verified this cycle by running that same [registration-readback] gate against their exact `(family, theta, cpl, config_key)` tuple" is false for the two reused rows (38.49°/38.69°) — `run_checks_1234_and_7` is never called with those angles anywhere in `run.py` (§0, confirmed independently, matching THERMODYNAMICS' bonus finding exactly). This is a real, checkable overclaim inside the very Idealization written to disclose a limitation honestly — it currently overstates the diligence actually applied.

## 2. Ruling on the five checkpoint criteria

1. **Candidate reproduction (passes ALL constraint metrics) — DOES NOT FIRE (N/A).** No T1 candidate configuration is under test this cycle; correctly a T28 house-discipline/validation cycle per Idealization 7 (re-confirmed: constraints 1–4 do not appear anywhere in `NOTES.md`'s Setup/Predictions/Result).

2. **Proven boundary (constraint subset jointly unsatisfiable) — DOES NOT FIRE (N/A).** Same basis as (1); no constraint-satisfaction question was posed this cycle to gate.

3. **Synthesis requires engine physics beyond validated bench classes — DOES NOT FIRE.** All 64 real FDTD calls reuse `Sim`/`add_line_source`/`r{3,4,5}_config()` unmodified (confirmed in Setup, zero `lab/` diff before and after this cycle's close, trust suite 41/41 both times). Item (v)'s grazing-incidence instrument reuses the already-existing, already-verified `edge_diffraction_c_empty_corrected`/`FastEval` closed-form machinery — zero new formula, zero new `Sim()` construction. Nothing here demands engine physics this program's validated bench classes cannot already express.

4. **Program-integrity drift (unfalsifiable claims; a constraint quietly dropped, esp. #3) — DOES NOT FIRE, but this is the closest call this program has had, and I am logging it as a formal warning shot, not a clean pass.**

   Reasoning, addressing the task's specific framing directly:

   - **The call-count/row-count confusion class.** This cycle contains (a) the self-disclosed 32-vs-64 *predicted-vs-actual calls* miscount, and (b) the undisclosed 64-*calls*-vs-16/18-*rows* mislabeling one paragraph later in the same Result section — the identical error shape recurring within one document, the second instance written immediately after the first was diagnosed and turned into a "Learned" item. That sequencing (state the lesson, then immediately fail to apply it) is qualitatively different from an ordinary first-time miss. **However, neither instance is unfalsifiable, and neither touches a target constraint (1–4, correctly N/A this cycle).** Both were caught this same cycle — instance (a) by the code's own assert before `results.json` was written, instance (b) by two independent Phase-5 seats before the cycle closes and before either figure propagates uncorrected into the Iteration-76 Logbook entry. That is the same shape as this program's own established non-firing precedent for R16/R17/R18's founding instances: a defect caught blind by the same cycle's own review layers is the review process *working*, not drift. I rule it **does not fire** on that basis.
   - **FI-G″ dropped without disclosure.** This is the sharper of the two candidates for criterion 4, because it is closer in *shape* to "quietly certifies/claims a discharge while blind to a known gap" — the exact pattern this charter exists to prevent (my own Phase-2 Attack 3 language, cited against a different item this same cycle). NOTES.md states flatly that FI-G′ "clos[es] the gap... left open" with no caveat, while a scenario that would test the *other* half of that gap was named, by name, in the immediately-prior cycle's own queue and never addressed or disclosed as deferred. This is closer to a genuine omission-as-overclaim than the count-mislabeling issue. But it is **not a target-constraint (1–4) drop** — it is a Tier-0 house-discipline fault-injection item, not a physical realizability/scene-contrast claim — and it too was caught this same cycle, by QUANTUM OPTICS, before Iteration 76 opens. I rule it **does not fire** criterion 4 on the same "caught blind, same cycle" basis, but it is the single finding this audit weighs most heavily toward drift, and it is why I am mandating its same-shift correction now (§4) rather than deferring it.
   - **Net ruling: criterion 4 DOES NOT FIRE this cycle.** But three same-cycle instances of one arithmetic-conflation error class, plus one undisclosed dropped-commitment overclaim, in a single document, is a materially thicker file than a typical founding miss. If a fourth instance of the count-conflation class appears in Iteration 76, or if any confirmed-but-undisclosed dropped commitment survives uncorrected past this Phase 5 into a future cycle's Logbook entry, Red Team should fire criterion 4 at that point without further warning. This audit is that warning.

5. **Two consecutive iterations with no logbook-advancing result — DOES NOT FIRE.** This cycle produced real, non-vacuous forward motion independent of any of the confirmed prose/arithmetic defects: item (ii) recovered a genuine crossing (θ≈38.252279°) that exp-095's narrower, mis-centered bracket missed — R17 working exactly as designed, one cycle after its own founding defect; item (i) resolved MIXED (2 of 4 established cpl=20 nulls now share the "no cpl=40 crossing in a naively-sized bracket" outcome, a materially different picture than exp-095's single-null read); and item (v)'s redesigned GP2′ delivered the first genuinely θ-dependent grazing-incidence finding after 11 cycles of a deterministic non-test — closing a governance ask that was itself flagged as a live Red Team defect at this cycle's own Phase 2. None of the confirmed defects above touch these underlying results (all are prose/formula-presentation bugs; §0 confirms none change a PASS/FAIL/verdict outcome). Genuine logbook-advancing content exists.

## 3. New standing rule

**ADOPT NOW, as an explicit exception to this program's usual cross-cycle recurrence-before-ratification cadence.**

Rationale for skipping the cadence: the usual reason to wait for cross-cycle recurrence is to avoid over-fitting governance to single-cycle noise. That reasoning does not apply here — the recurrence signal already exists *within* one cycle at the strength normally supplied by two full cycles: two distinct, independently-confirmed instances of the identical error shape (32-predicted-vs-64-actual calls; 64-calls-vs-16/18-rows) in one document, the second occurring immediately after the first was named and logged as a lesson, neither caught by the five-blind-critique-plus-Red-Team Phase 2/3/4 pipeline, both caught only by Phase 5. Waiting for a second *cycle* to "confirm the pattern" would mean deliberately tolerating a further cycle's worth of the same class of undetected error when the within-cycle count already meets the bar this program has historically treated as recurrence.

**Proposed rule text** (calibrated per VISION'S own caution against re-creating the same unowned-channel gap by naming a person/seat rather than a mechanism): *Any results table, Result-section prose, or Learned/Next item that states a count of FDTD calls, report rows, or data points must be backed by an explicit, checkable assert (in the spirit of `netd_row()`'s coverage assert and this cycle's own `assert total_calls == 64`) distinguishing call-count from distinct-row/data-point-count wherever both exist in the same computation — not a reviewer's manual cross-check.* This makes the fix a code-enforced invariant, not a newly-assigned human duty (which is exactly the shape of channel that went unowned three times this cycle already).

Numbering/ratification of this into `LOGBOOK.md` as the next R-rule is a Director/Panel function; Red Team's role here is the nomination and the rationale for accelerating past the usual cadence, not the ratification itself.

## 4. Combined Verdict: **PROMISING**

Both of this cycle's stated goals were substantively achieved in the underlying data, independent of every confirmed defect above: (1) the family-wide-vs-feature-specific migration question resolved to a real, informative MIXED answer (2 of 4 established nulls now share the no-crossing-in-a-naive-bracket outcome), and (2) the 11-cycle-old grazing-incidence governance ask was genuinely, honestly discharged for the first time — a real, non-vacuous, falsifiable instrument that corroborates rather than contradicts prior work, closing a standing Red Team defect from this cycle's own Phase 2. Every confirmed defect in §1 (the FI-G″ gap, the GP2′ overclaim, the Richardson bug, the row-count mislabeling, the banner placement, the GP1 framing, the Idealization 47 overclaim) is a zero-FDTD, zero-new-`Sim()`-construction, non-load-bearing prose/arithmetic/scoping correction — none of them, on independent re-verification, changes a single PASS/FAIL classification, crossing value, or the item (i)/(ii)/(v) verdicts. This is not RULED OUT (nothing here undermines the core findings) and it is not merely PARTIAL (both stated goals were actually met, not half-met) — it is a cycle with real, hard-won physics content that also needs a same-shift correction pass before its numbers are cited forward, which is exactly what this audit is for.

## 5. Reconciled Iteration-76 queue

Ordered by convergence across seats and load-bearing weight; origin cited per item. (Same-shift fixes, §6 below, are corrections to *this* cycle's record and are not repeated here as forward work — Iteration 76 should build on the corrected record.)

1. **Null C re-test at a wider, R17-compliant, asymmetric bracket, explicitly scoping a "vanishing amplitude, no crossing at any reasonable width" outcome as a live third result** (not just "wider bracket will find it"). *Origin: NOTES.md's own Director draft (Next item 1), independently ranked #2 by EM, #2 by THERMODYNAMICS, #2 by VISION; PHOTONICS' additional vanishing-amplitude hypothesis (§3, Null C's decelerating `delta_scene` curve) folded in as an explicit alternative to test for, not a separate task.* Five of six seats converge on this as the most physics-load-bearing open thread — item (ii) just proved a same-sized-but-mis-centered bracket produces a false NO-SIGN-CHANGE, and Null C's current verdict rests on exactly that untested failure mode.
2. **The cpl=50/R5 third resolution point at Null B (and/or θ₀≈38.590230°)**, reusing exp-095's already-built family, run *against the corrected marginal-to-marginal Richardson formula* (§6 below), not the miscomputed one. *Origin: NOTES.md Director draft (Next item 2), PHOTONICS #3, EM #3, MATERIALS #2 (explicitly gated on the formula fix landing first).* Zero new `Sim` family construction; the only genuine path to an actual (still non-formal, per Idealization 49) convergence read at one feature.
3. **Reconcile GP2′ against exp-086's own sliding-window `ptp` method, extended through the 74°–89.5° tail** (not just the originally-swept 59°–73° band) at matched θ range, zero-FDTD, reusing exp-086's method verbatim — explicitly scoped to also state whether the severity gap (235× vs. 5,444×–6,631×) is fully explained by the differing statistic or partially by something else. *Origin: NOTES.md Director draft (Next item 3), QUANTUM OPTICS #3, PHOTONICS #1 (extending the pre-existing queue item's scope to cover the tail divergence this seat found).*
4. **Ratify the call-count/row-count arithmetic-assert standing rule** (§3 above) into `LOGBOOK.md`, framed as a code-enforced invariant, not an assigned human duty. *Origin: NOTES.md Director draft (Next item 4), THERMODYNAMICS #1 (promote candidate→committed), VISION #3 (calibration: division-of-labor fix, not a new attentional burden).*
5. **State the cpl-is-orthogonal-to-realizability finding explicitly in a future Result section**, and revisit the standing T1-route-N/A governance flag (six consecutive cycles, exp-094 through exp-098, zero new FDTD evidence bearing on any realizability parameter) at the next Phase 3 checkpoint. *Origin: MATERIALS #3.* Not a forcing function for a T1 proposal this cycle, but the flag has outlived its own originally-cited precedent count without a Result-section-level re-raise.

## 6. Same-shift corrections mandated NOW (zero-FDTD, zero-new-`Sim()`-construction, non-load-bearing — apply before Iteration 76 cites this record)

Matching this program's own established practice (Tier-0 fixes run alongside, not gating, Tier-1 spend):

1. **Richardson formula bug (MATERIALS, adopted §1).** Recompute `richardson_style_diagnostic()`'s call site to report the correctly-paired marginal-to-marginal ratio (`shift_30_40/shift_20_30 = 0.777`, not `shift_20_40/shift_20_30 = 1.777`); correct Result and Learned #3's language from "growing faster than 2nd-order... MORE open, not less" to the corrected, mildly-reassuring reading. Pure recomputation from already-filed numbers.
2. **GP2′ Result overclaim (PHOTONICS+THERMODYNAMICS, adopted §1).** Replace "flags MARGINAL continuously... the ENTIRE upper half" with the actual punctuated pattern (9 named VALID exceptions), and add the 74°–89.5° tail non-recovery disclosure PHOTONICS surfaced.
3. **Row-count mislabeling (THERMODYNAMICS+EM, adopted §1).** Correct "held for all 64 real-FDTD report rows" to "16 new report rows (18 including 2 reused from exp-095), backed by 64 real FDTD calls."
4. **GP1 framing (EM self, adopted §1).** Replace "hard passivity floor" with EM's own proposed sentence: a non-negativity check on a windowed Poynting-flux component, motivated by the absence of any gain mechanism in this source-driven construction, not a direct corollary of Poynting's theorem applied to this specific window.
5. **Idealization 47 overclaim (THERMODYNAMICS bonus finding, independently confirmed §0).** Either (preferred, cheaper to make true than to write around) execute the two missing `run_checks_1234_and_7("R4", th, 40, key)` calls for θ=38.49°/38.69° — zero new `Sim()` construction, pure desk computation — so the claim becomes true; or, failing that, correct the text back to Phase 1's own original accurate framing (gate not re-run for these two points, only the netd-key-coverage assert applies).
6. **Banner placement (VISION, adopted §1).** Duplicate (or move) the carried-idealizations banner sentence into the `## Predictions` section body itself, not only into the closing paragraph of `## Idealizations` that references it by name.
7. **FI-G″ (QUANTUM OPTICS, adopted §1) — ruled IN-SCOPE NOW, not deferred.** Execute the `native_ny` corruption scenario (e.g. 1585, not 1584) against all three families, scored against the same `y_lo`/`y_hi` recomputation FI-G′ uses — zero new `Sim()` constructions, same cost class as FI-G′ itself. Correct item (iv-c)'s "closes the gap... left open" language to state precisely which portion(s) are now closed. This is the single finding this audit weighs most heavily under criterion 4 (§2); closing it now, fully, rather than carrying a second silently-dropped commitment into Iteration 76, is the cheaper and safer choice.
8. **GP2′/exp-086 "structurally different instrument" overclaim (QUANTUM OPTICS finding (a), adopted §1).** Add one disclosure sentence stating plainly that GP2′ and exp-086's `ptp` method are two post-processing statistics computed from the *identical* closed-form formula, not independent physical instruments — before "corroboration via a structurally different instrument" is cited forward as stronger evidence than it is.

None of these eight require a new `Sim()` construction or real FDTD spend; none change a PASS/FAIL classification or a crossing value already on file. All are cheap enough, and all were caught within this cycle's own six-seat-plus-Red-Team process before Iteration 76 opens — consistent with the "caught blind, same cycle" ruling in §2's criterion-4 analysis, provided they are actually applied before that record is cited forward.
