# PHASE 2 — RED TEAM AUDIT · Panel Iteration 63 · exp-086

*Fresh context. Received: `phase1_proposal.md` + all five blind Phase-2
critiques (PHOTONICS, MATERIALS, THERMODYNAMICS, QUANTUM, VISION — EM leads
this cycle and does not also critique its own proposal). Every claim below —
the proposal's own, and each critique's own — is independently re-derived
from primitives: the two target source files read line-by-line, exp-085's
own committed `derivation_results.json` re-loaded directly, exp-085's own
`phase5_redteam_audit.md`/`phase2_redteam_audit.md` re-read in full, and,
where a claim was numeric and checkable, re-computed from scratch in a fresh
Python re-implementation of the fix logic — not accepted from any seat's
arithmetic, including this task's own critique-count framing.*

## 0. Scope note

Confirmed independently, not accepted from the proposal's own §3: this is a
zero-FDTD, model-internal instrument-repair cycle on shared period-search
machinery (`free_period_with_widening`, two files, identical bug shape). No
absorption mechanism, no constraint-3 scene, nothing bearing on T1's
escape-route taxonomy anywhere in `phase1_proposal.md` or either target
source file. **All `constraint-#N-violation` tags are N/A this cycle** —
every attack below is tagged `inconsistency` or `unfalsifiable`, matching
this task's own framing and exp-085's own Phase-2 audit precedent exactly.

## 1. Independent primitive-level verification performed

- **The bug trace and R11's fix logic.** Re-read `pad_round_trip_model.py`
  lines 374–407 and `y_wall_prescreen.py` lines 325–361 directly (not the
  proposal's paraphrase). Hand-traced the truth table of
  `if chosen is None or (chosen["at_boundary"] and not at_boundary)`: it
  updates away from stage 1 only when a *later* stage reports an interior
  optimum; if every stage is `at_boundary`, `chosen["at_boundary"]` stays
  `True` for the whole loop. Post-loop testing of that flag is therefore a
  correct and sufficient detector, algebraically — matching every seat's
  claim and R11's own text (LOGBOOK.md, RULED OUT registry).
- **Call-path trace.** Confirmed directly: `phase4_derivation.py` line 54
  loads `experiments/084-.../phase1_derivation.py`, whose own `ywp = _load(...
  y_wall_prescreen.py)` (traced in that file) is the version
  `free_period_with_widening` in `phase4_derivation.py`'s namespace actually
  resolves to. Site 2 in the proposal's own table is the correct target, not
  merely asserted.
- **Independent, from-scratch re-implementation of the R11 fix**, built
  without reference to any seat's code, then run against `FastEval` (bit-
  identical per exp-085's own spot-check convention) on exp-085's own 37
  sub-window recipe (`theta_centers=arange(5,77+ε,2)`, `sub_theta=thc±3°,
  0.2° step`):
  - Reproduces the AS-FILED (unfixed) `p_local_corrected`/`r2_local` for
    every one of the 31 non-boundary windows to <1e-6° — confirms my own
    reimplementation is faithful to the real machinery, not a strawman.
  - Boundary set, corrected machinery: exactly **6/37**,
    `θc∈{45,59,61,63,71,73}`, bit-identical to both exp-085's own audit and
    this proposal's own claim.
  - Applying the proposal's own §2 "recovered" criterion
    (`converged==True ∧ p_local_corrected≤6.0° ∧ r2_local≥0.30`):
    **21/37=0.5676**, matching Prediction (1)'s own primary (0.568) figure
    exactly, independently reproduced from a clean re-implementation, not
    the proposal's own arithmetic.
- **PHOTONICS' ptp/amplitude claim, recomputed independently via `FastEval`
  on the real curve** (not asserted from PHOTONICS' own numbers): ptp grows
  from `2.5577×10⁻⁴` at `θc=5°` to `1.392305` at `θc=63°` — a **5443.7×**
  factor, confirming "~5000×" — and the true maximum is even larger,
  `1.695985` at `θc=69°` (**6631×**), before falling at 71–73°. **CONFIRMED**
  exactly, independent computation.
- **PHOTONICS' "already computed, silently discarded" claim.** Traced
  `y_wall_prescreen.py::free_period_with_widening`'s own per-stage `rec`
  (line 350): it *does* carry `ss_tot_full`. `phase4_derivation.py`'s Method
  C loop builds `stages_sub` (line 333) carrying these per-stage recs, but
  the persisted `rec` written to `sub_results` (lines 339–341) keeps only
  `theta_c`, `p_local_reported_at_39`, `p_local_corrected`, `r2_local`,
  `window` — `stages_sub` itself is never written to `out["method_c"]`.
  `ptp` specifically is not literally computed as a named variable anywhere,
  but `c_sub` (line 332) — from which it is a zero-cost one-liner — already
  exists in scope at the exact point the `rec` is built. **CONFIRMED**, with
  this precision: `ss_tot_full` is discarded; `ptp` is trivially derivable
  from an already-computed array, not merely "already computed" verbatim.
- **QUANTUM's stride-phase claim, recomputed independently, from scratch**
  (own re-implementation of the fix, own construction of the recovered set,
  own Spearman + exact-permutation computation — not QUANTUM's numbers, not
  the audit's own §1.8 reconstruction):

  | Phase (start θc) | n | ρ | p (exact permutation) |
  |---|---|---|---|
  | 5° | 7 | **0.8571** | **0.0238** |
  | 7° | 7 | 0.4286 | 0.3536 |
  | 9° | 7 | 0.5357 | 0.2357 |

  **Matches QUANTUM's cited figures to the printed digit at all three
  phases** (0.857/0.024, 0.429/0.337 t-approx, 0.536/0.215 t-approx).
  Phase-5° clears the proposal's own falsification band (`|ρ|>0.75` AND
  `p<0.05`) outright; phases 7°/9° do not. **CONFIRMED exactly.**
- **MATERIALS' quiet-variant claim.** Traced `free_period_with_widening_quiet`
  (`pad_round_trip_model.py` lines 353–371) directly: identical
  `chosen is None or (chosen["at_boundary"] and not at_boundary)` logic,
  2-stage (`[1,4]`,`[1,15]`), called inside `null_calibration_appendix`
  (lines 274–350, matching MATERIALS' own citation exactly). **But
  independently recounting the call sites** (not MATERIALS' own "40,000"
  figure): `for i in range(n_trials)` at line 299 (pure-noise null,
  **20,000** calls) + `best = free_period_with_widening_quiet(...)` at line
  320 (**1** call) + `_bootstrap("iid")` at line 346 (**20,000** calls) +
  `_bootstrap("circular")` at line 347 (**20,000** calls, a SECOND
  20,000-trial bootstrap variant MATERIALS' own count does not carry) =
  **60,001 total calls**, not 40,000 — MATERIALS undercounts by ~50%. This
  is a genuine correction to MATERIALS' own arithmetic (not a restatement),
  in exactly the spirit this audit is instructed to apply to every seat
  including itself.
- **New, this audit's own addition, going beyond any of the five critiques**:
  actually measured whether the quiet-variant's bug fires, rather than
  arguing from code shape alone. Re-implemented
  `free_period_with_widening_quiet` from the primitive source and ran it
  against a 3,000-trial partial sample (disclosed as partial, not the full
  20,000 — a cost-bounded probe, not a claim of exhaustive replication) of
  the SAME pure-noise-null construction `null_calibration_appendix` actually
  uses (`σ = std(real_delta_pad) = 0.0014412`, `n=31` angles, the real
  `experiments/076-.../results.json::headline` grid):

  **201/3000 = 6.70% of sampled pure-noise trials hit the all-stage-boundary
  case** — the identical defect shape R11 names, firing at a real,
  non-trivial rate inside the null distribution that feeds `p_r2_ge_070`
  and `max_r2_over_trials`, the statistics `exp-077`'s own headline REFUTE
  cites as "far outside the pure-noise R² distribution." Also independently
  confirmed: the best free fit to the real `real_delta_pad` curve itself
  gives `p_star_deg=4.6126°, R²=0.8165, at_boundary=False` — consistent with
  (not identical to, since this is the *quiet* 2-stage variant, not Method
  C's 3-stage one) T28's own separately-established `P_continuity=4.611°`
  citation (LOGBOOK Iteration 59), a useful cross-check that this
  re-implementation is behaving correctly on real data, not merely on
  synthetic noise.
  **What this does NOT establish**: whether the ~6.7% firing rate actually
  *moves* any of the three cited null-calibration statistics in a
  materially different direction once corrected (a boundary-pinned
  fallback's own R² is plausibly, but not confirmed, *lower* than the
  correctly-widened alternative would be, which could make the current,
  uncorrected statistics conservative rather than anti-conservative — this
  is a real, disclosed open question, not resolved by this audit, and
  should not be asserted in either direction without actually re-running
  the corrected 60,001-call appendix).
- **THERMODYNAMICS' omission claim.** `grep -in
  "poynting|interception|energy|thermo"` against the full proposal text:
  **zero matches**, confirmed independently exactly as THERMODYNAMICS
  states.
- **VISION's omission claim.** `grep -in
  "instrument|certif|foreclose|reliabilit"` against the full proposal text:
  the word "instrument" appears twice, both in scope-note language
  ("instrument-repair... work," "not... a re-specified instrument") — never
  attached to Prediction (2)'s headline classification or any caveat
  language. **CONFIRMED exactly.**
- **New finding, this audit's own, not raised by any of the five critiques**:
  the proposal's own title claims to execute "Red Team's Reconciled
  Iteration-63 Ranking, **Tier-1 items (1)–(5)**." Re-read exp-085's own
  §7 verbatim: that list has **no Tier-0/Tier-1 labeling at all** (unlike
  several earlier iterations' rankings, which did use that structure) — it
  is a flat, numbered 1–6 list. Item 4 of that list is the joint EM/THERMO
  energy-interception cross-check, explicitly scoped **"on the next
  scene-bearing T28 cycle"** — i.e., explicitly NOT this cycle (consistent
  with THERMODYNAMICS' own attack, above: this proposal correctly does not
  touch it, but its title implies it does). Item 5 is PHOTONICS' domain-
  truncation test for leg (b)'s Anchor 2 / EM's kernel rebuild — a
  different sub-thread question, also not mentioned anywhere else in this
  proposal. The proposal's own actual scope (§2/§4/§6) is items **1–3
  only**. The title's "(1)–(5)" is a citation-accuracy defect: harmless in
  substance (nothing in the executed work actually claims items 4/5 were
  done), but exactly the kind of imprecise self-citation R4 exists to
  catch before it propagates into NOTES.md or LOGBOOK.

## 2. Numbered attacks

1. **[unfalsifiable]** Prediction (4) — "no currently-cited T28 headline
   number is corrupted" — is scoped (§2's audit-coverage row) to exclude
   `free_period_with_widening_quiet` entirely. This is not merely a
   documentation gap (THERMODYNAMICS' framing) or an unaudited-volume risk
   (MATERIALS' framing): §1 of this audit **empirically measured** a 6.70%
   (201/3000) all-stage-boundary firing rate in exactly the quiet variant's
   own pure-noise-null construction, feeding `null_calibration_appendix`,
   the evidentiary basis for the x-normal/unrealizable-admittance REFUTE
   every T28 cycle has cited as settled since Iteration 54. As scoped,
   Prediction (4) cannot be falsified by the one corruption class now shown
   to be real and non-trivial, because that class is defined out of the
   audit's own coverage before the prediction is even tested. This is the
   single most consequential attack in this audit.

2. **[inconsistency]** QUANTUM's finding, independently re-derived exactly
   in §1: the overlap-corrected Spearman fix (§2 table, "Spearman
   significance correction" row) does not specify which of three valid,
   non-overlapping stride-3 phases (θc starting 5°/7°/9°) to use, and the
   choice is outcome-determining — `ρ=0.857, p=0.024` (falsifies Prediction
   3) at phase 5° vs. `ρ=0.429–0.536, p=0.22–0.35` (does not falsify it) at
   the other two. An unstated researcher degree of freedom in a fix built
   specifically to correct a *different* significance overstatement is the
   same R5 look-elsewhere shape this program already has a standing rule
   against.

3. **[inconsistency]** PHOTONICS' finding, independently re-derived exactly
   in §1: sub-window signal amplitude (ptp) grows 5,444×–6,631× across the
   grazing-incidence region, and the proposal's uniform `r2_local≥0.30`
   recovery bar cannot distinguish a plausibly-noise-floor θc=5° fit from a
   θc=63–69° fit sitting on a signal four-to-five orders of magnitude
   larger — a scale-blind threshold applied to a quantity whose own scale
   varies by nearly four orders of magnitude across the domain being
   classified.

4. **[inconsistency]** THERMODYNAMICS' finding, independently confirmed by
   direct grep in §1: the proposal contains zero mentions of the joint
   EM/THERMO energy-interception cross-check, which fired Checkpoint
   criterion 4 at Iteration 61 (exp-084) for the identical silent-absence
   shape — no explicit exemption sentence, even though exp-084/085's own
   established language (a scene-less desk cycle has no article-loaded
   scene to check against) fully justifies one and costs nothing to state.

5. **[inconsistency]** VISION's finding, independently confirmed by direct
   grep in §1: Prediction (2)'s headline "NOT STABLY PERIODIC" carries none
   of exp-085's own carefully-earned instrument-reliability caveat forward,
   and nothing in §4/§6 requires Phase 4's `NOTES.md` to restate it — the
   same caveat-erosion shape T16 (LOGBOOK) already recorded once in this
   exact sub-thread.

6. **[inconsistency]** *(this audit's own finding, not raised by any
   critique)* The proposal's title claims to execute "Tier-1 items (1)–(5)"
   of exp-085's own Reconciled Iteration-63 Ranking. Independently re-read,
   that ranking has no Tier-0/Tier-1 structure and is a flat 1–6 list; items
   4 (energy-interception, explicitly deferred to a future scene-bearing
   cycle) and 5 (leg-(b) Anchor 2 domain-truncation / kernel rebuild, an
   unrelated sub-thread) are neither executed nor referenced anywhere else
   in this document. Non-blocking (the actual executed scope, items 1–3, is
   correct and narrowly stated in §2/§4/§6) but should be corrected before
   this title is copied into NOTES.md or a LOGBOOK citation, per this
   program's own R4 self-citation discipline.

7. **[inconsistency]** *(disclose-only, non-blocking)* MATERIALS' own
   critique undercounts `free_period_with_widening_quiet`'s call volume —
   "40,000" vs. the actually-traced 60,001 (§1) — missing the second
   (circular-shift) bootstrap variant. Does not change MATERIALS' own
   verdict or flip parameter, but the corrected figure should replace
   "40,000" wherever this docket item is carried forward, matching this
   audit's own instruction to re-derive every seat's arithmetic, not merely
   its own.

## 3. Adjudication of the five critiques — confirm/override, independently re-derived

**(a) PHOTONICS — grazing-incidence ptp growth not distinguished by the
uniform R² bar.** **CONFIRM, exactly.** Independently recomputed via
`FastEval` on the real curve (§1): 5,444× growth θc=5°→63° (true peak 6,631×
at θc=69°) — matches PHOTONICS' own "~5000×" to within the rounding
PHOTONICS itself used. The claim that `ss_tot`/`ptp` is "already computed...
and silently discarded" is confirmed with one precision correction: only
`ss_tot_full` is literally computed-then-discarded inside the per-stage
`rec`; `ptp` is not itself a named, computed variable anywhere in the chain,
but is a zero-cost derivative of the already-computed `c_sub` array at the
exact point the persisted `rec` is built — a distinction without
consequence for the flip parameter, which remains correct and cheap as
proposed.

**(b) MATERIALS — the quiet-variant sibling is unaudited by Prediction
(4).** **CONFIRM the substantive finding, going further than MATERIALS
itself did; OVERRIDE the specific "40,000" figure.** The bug-sharing claim
and the `null_calibration_appendix` citation (lines 274–350) are both
confirmed exactly from source. The call-volume figure is wrong (60,001, not
40,000 — §1); more importantly, this audit did not stop at flagging the gap
as MATERIALS did — it **ran** MATERIALS' own proposed flip-parameter check
(a bounded firing-rate sample) and found a real, non-trivial 6.70% rate,
converting MATERIALS' theoretical concern into a demonstrated fact (attack
1). MATERIALS' own verdict (support-with-changes) and flip parameter both
stand, strengthened.

**(c) THERMODYNAMICS — the energy-interception cross-check goes
unmentioned.** **CONFIRM, exactly.** Independent grep (§1) finds zero
matches for any of the four terms THERMODYNAMICS names. THERMODYNAMICS'
own cross-reference to the Iteration-61 Checkpoint-4 firing on the
identical shape is independently verified against LOGBOOK.md's own
Iteration-61 CHECKPOINT entry (re-read in full for this audit) — accurate,
not overstated.

**(d) QUANTUM — the stride-phase researcher degree of freedom.**
**CONFIRM, exactly, digit-for-digit**, via a fully independent re-
implementation and computation (§1) — not a re-execution of QUANTUM's own
code, a from-scratch build of the fix, the recovered-set logic, and the
Spearman/permutation test. All three phases' ρ and p-values match QUANTUM's
own cited figures to the printed digit. QUANTUM's central claim — that
phase 5° is not a fringe case but the same alignment the cited audit's own
§1.8 reconstruction uses, and what a default `array[::3]` slice produces —
is independently verified as the natural, unmarked default a careless
implementation would reach.

**(e) VISION — the caveat does not carry forward.** **CONFIRM, exactly.**
Independent grep (§1) finds no instrument-reliability language anywhere
near Prediction (2). VISION's citation of exp-085's own audit §2/§5
paragraph establishing the caveat is independently verified against that
document (re-read in full for this audit, §2 and §5 above) — accurate.
VISION's own T16 cross-reference (a caveated finding hardening into a bare
fact one cycle later) is a real, on-point precedent, independently
re-confirmed by reading LOGBOOK's own T16 entry.

## 4. Ruling: **PROCEED-WITH-MANDATORY-FIXES**

No defect found — by any critique or independently by this audit — is
structural. The core repair (R11's fix, applied to both files, detection
condition algebraically sound) is correct, minimal, and precisely scoped;
every defect below is a cheap, fully expressible correction (a missing
phase pre-registration, two persisted fields, one disclosure sentence, one
caveat-carrying requirement, one title correction, one bounded empirical
check already run once by this audit and needing only to be completed at
full scale). `constraint-#N-violation` is N/A throughout (§0).

**Mandatory fixes — for the Director to specify into the committed proposal
/ Phase-3 build before Phase 4 runs:**

1. **Pre-register and report all three stride-phase alignments** (θc
   starting 5°/7°/9°) for the overlap-corrected Spearman test, or adopt an
   explicit phase-invariant block/effective-N correction instead of any
   single arbitrarily-chosen phase. The headline "not independently
   significant" claim (Prediction 3) must hold across all three, or the
   disagreement must be reported and reconciled explicitly, before it is
   cited as a T28 permanent-record finding. [QUANTUM, independently
   confirmed]

2. **Scope Prediction (4) explicitly to the non-quiet citation set it
   actually audits**, and complete — not merely start — a bounded empirical
   firing-rate check on `free_period_with_widening_quiet`'s own
   pure-noise-null and both bootstrap legs (full 60,001 calls, corrected
   count — not 40,000) inside `null_calibration_appendix`, before this
   cycle's own record asserts "no currently-cited number is corrupted."
   This audit's own 3,000-trial partial sample already found a real 6.70%
   firing rate in the pure-noise leg alone; whether that materially moves
   any cited statistic (`p_r2_ge_070`, `max_r2_over_trials`, or the
   headline "far outside the pure-noise distribution" claim) is not yet
   known in either direction and must be determined by actually re-running
   the appendix on the corrected quiet-variant, not argued from firing rate
   alone. [MATERIALS, confirmed and extended by this audit]

3. **Add one explicit sentence** (§3 or §5) stating the joint EM/THERMO
   energy-interception cross-check is exempt this cycle because no
   article-loaded FDTD scene exists to check against, matching exp-084/085's
   own established language — before Phase 4 runs, not after. [THERMODYNAMICS,
   confirmed]

4. **Add an explicit, pre-registered requirement** that Phase 4's
   `NOTES.md` and any `classification_a` headline restate exp-085's own
   instrument-reliability caveat — verbatim or materially equivalent —
   every place "NOT STABLY PERIODIC" (or any other corrected label) is
   reported, not merely emit the bare decision-code label. [VISION,
   confirmed]

5. **Persist `ss_tot_full` and `ptp` per sub-window** in
   `phase4_rescore_results.json` (the former already computed and
   discarded, the latter a zero-cost derivative of the already-computed
   `c_sub` array) — required before any classification headline is drawn
   from the corrected data, so this and future cycles can check whether
   "recovered" windows span a coherent, physically meaningful amplitude
   scale. Additionally, **disclose explicitly** (a sentence in §5
   Idealizations or the eventual NOTES.md) that the grazing-incidence
   amplitude blow-up raises an unresolved question about whether
   `edge_diffraction_c_empty_corrected` remains inside its own valid
   near-field regime there — a model-validity caveat this cycle is not
   scoped to resolve, but must not silently omit. [PHOTONICS, confirmed]

6. **Correct the title's "Tier-1 items (1)–(5)" claim** to accurately
   describe the executed scope (items 1–3 of exp-085's own flat, unTiered
   1–6 ranking); items 4 and 5 are neither executed nor in scope here.
   [this audit, new]

**Recommended, non-blocking (disclose, do not need to gate Phase 4):**
correct "40,000" to "60,001" wherever MATERIALS' own citation of the
quiet-variant call volume is carried forward into NOTES.md or a future
LOGBOOK entry (this audit, attack 7).

## Summary (≤250 words)

**Ruling: PROCEED-WITH-MANDATORY-FIXES.** The core R11 repair is correct,
minimal, algebraically sound — independently re-derived and re-implemented
from scratch, reproducing the proposal's own 21/37=0.568 recovered count
exactly. All five blind critiques are **CONFIRMED** by independent
re-derivation, not restatement: PHOTONICS' ~5000× grazing-incidence
amplitude growth (measured 5,444×–6,631× via a fresh `FastEval`
computation); THERMODYNAMICS' energy-interception omission (grep-confirmed,
zero matches); VISION's dropped instrument-reliability caveat
(grep-confirmed); QUANTUM's stride-phase degree of freedom
(digit-for-digit reproduced from a from-scratch reimplementation:
ρ=0.857/p=0.024 at phase 5° vs. ρ=0.43–0.54/p=0.22–0.35 at phases 7°/9°).
MATERIALS' quiet-variant finding is CONFIRMED and extended, with one
correction to its own arithmetic (60,001 calls, not 40,000) — and this
audit went further, actually running the flip-parameter check MATERIALS
proposed: a 3,000-trial empirical sample found the boundary-pinning bug
fires at 6.70% inside the same null-calibration appendix that underwrites
T28's "settled" x-normal REFUTE since Iteration 54, converting a
theoretical coverage gap into a demonstrated, unresolved risk (attack 1,
the audit's own most consequential finding). One further defect found
independently: the title's "Tier-1 items (1)–(5)" mischaracterizes
exp-085's own flat, unTiered ranking — items 4/5 are neither executed nor
in scope. Six mandatory fixes, all cheap, zero new FDTD, none structural.
No `constraint-#N` tags apply — model-internal desk cycle, per §0.
