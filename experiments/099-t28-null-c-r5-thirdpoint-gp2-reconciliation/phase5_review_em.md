# Phase 5 Review — ELECTROMAGNETISM (blind, fresh context)

*Panel Iteration 76, exp-099. Charter: field/wave behavior, impedance
matching, energy coupling; owns the reciprocity/passivity/causality
bookkeeping and formalizes what T1 permits and forbids for each proposal.
I have not seen any other seat's Phase-5 output and do not defer to one.
Required reading (PANEL.md, LOGBOOK.md in full, PLAN.md, and this cycle's
complete record — `phase1_proposal.md`, all five Phase-2 critiques,
`phase2_redteam_audit.md`, `NOTES.md`, `run.py`, `results.json`,
`run_output.txt`) completed before writing this review.*

## 1. Independent spot-verification

Six load-bearing numbers, recomputed by hand from `results.json`/
`run_output.txt` primitives, not trusted from `NOTES.md`'s prose.

1. **Item 1 interval-slope-decay ratios (`r_ratios`).** Using the four
   filed cpl=40 points plus the three new points from
   `results.json::item_1.combined_report`: deltas_seq =
   [4.704114×10⁻⁴, 1.322251×10⁻³, 2.456623×10⁻³, 2.778079×10⁻³].
   d₁ = 1.322251×10⁻³ − 4.704114×10⁻⁴ = 8.51840×10⁻⁴.
   d₂ = 2.456623×10⁻³ − 1.322251×10⁻³ = 1.13437×10⁻³.
   d₃ = 2.778079×10⁻³ − 2.456623×10⁻³ = 3.21456×10⁻⁴.
   r_ratios[0] = |d₂|/|d₁| = 1.13437×10⁻³/8.51840×10⁻⁴ = **1.33167** —
   matches the filed `1.3316739748300177` exactly.
   r_ratios[1] = |d₃|/|d₂| = 3.21456×10⁻⁴/1.13437×10⁻³ = **0.28338** —
   matches the filed `0.28337723580831364` exactly. **MATCH.** Since
   r_ratios[0] > 0.5, `amplitude_criteria_met=False` follows correctly,
   and — since `crossing_c is None` and amplitude criteria fail —
   `item1_verdict=INCONCLUSIVE-AT-THIS-WIDTH` is the only value the
   code's own branch logic (lines 372–382 of `run.py`) can produce.
   Confirmed by direct trace, not merely trusted.
2. **R13 floor gate.** `results.json::r13_floor_gate`: `rms=1.9174375118×10⁻³`,
   `floor=1.9174375118×10⁻⁴`. `floor/rms = 0.10000000...` — exactly
   `FLOOR_FRAC=0.10`, matching R13's own founding convention. **MATCH.**
   (Cosmetic note, non-load-bearing: the returned tuple's third element is
   named `n83` in `run.py`/`results.json` but its value is `31`, not `83` —
   an inherited variable-naming leftover from an earlier cycle's own
   `compute_floor()`, not a bug; the actual sample size used is the
   correct, disclosed `n=31` R13 census.)
3. **Item 2 Step 2 settling `rel_dev`.** `delta_scene(R5_STEPS)=
   5.253136×10⁻⁴`, `delta_scene(R5_STEPS_STRESS)=5.243753×10⁻⁴`.
   `rel_dev = |5.243753×10⁻⁴ − 5.253136×10⁻⁴| / 5.253136×10⁻⁴ =
   9.383×10⁻⁷ / 5.253136×10⁻⁴ = 1.786×10⁻³ = 0.1786%` — matches the filed
   `0.0017861832836256804` exactly. **MATCH**, well inside the ≤1% PASS
   band.
4. **Richardson diagnostic (30/40/50 triple).** `shift_20_30`(field name,
   actually the 30→40 shift per the deliberate positional relabeling) =
   −0.15031902190763446; `shift_30_40`(field name, actually the 40→50
   shift) = crossing_cpl50 − θc40 = 39.77686992722644 − 39.921519316666235
   = **−0.14464938943979...** — matches the filed value exactly.
   `observed_ratio = 0.14464938943979/0.15031902190763 = 0.962283` —
   matches the filed `0.962282667915931` to 6 significant figures.
   `naive_order2_ratio = (40/50)² = 0.64` — exact. **MATCH.** (See §4.3
   below for a naming-clarity concern with this field's own labels —
   non-load-bearing, but worth a house-discipline note.)
5. **Item 2 Step 3 crossing bracket and R13 floor gate, all four points.**
   Recomputing sign(delta_scene) at the four Step-3 angles from
   `results.json::item_2.step3.report`: 39.521519°→negative,
   39.688519°→negative, 39.854519°→**positive**, 40.021519°→positive.
   Linear interpolation between the sign change
   (39.688519°, −5.951707×10⁻⁴) and (39.854519°, +5.230823×10⁻⁴) gives
   `θ_cross = 39.688519 + 0.166 × 5.951707/(5.951707+5.230823) =
   39.688519 + 0.166×0.53225 = 39.77689...` — matches the filed
   `39.77686992722644` to 4 decimal places. **MATCH.** All four points
   independently confirmed `floor_pass=true` against `floor=1.9174×10⁻⁴`
   (each `frac_contrast` value — 3.04×10⁻³, 1.09×10⁻³, 9.55×10⁻⁴,
   2.92×10⁻³ — clears the 0.10×RMS floor by 5×–16×, comfortably clean).
6. **R19 call-count self-check.** item_1.n_calls=12 (3 angles × 2 legs ×
   2 conditions), item_2.total_calls = step1(4) + step2(8) + step3(16) =
   28. 12+28=**40**, matching `results.json::fdtd_calls=40` and the
   printed `[R19 assert]` line exactly. Independently re-derived the
   *distinct-row* count separately from the *call* count, the exact
   distinction R19 exists to enforce: 40 real `sim.run()` calls produced
   **8** new classification-relevant `delta_scene` rows (3 in item 1, 1
   Step-1 + 4 Step-3 in item 2) plus 2 settling-comparison readings (Step
   2, not scored as classification rows) — nowhere in `NOTES.md` or
   `run.py`'s own prints is the call count (40, 12, 28...) substituted for
   a row count or vice versa. R19 (adopted one cycle ago, specifically to
   prevent this exact conflation) is honored correctly throughout this
   cycle, checked directly rather than assumed.

**All six independently reproduce exactly or to the printed precision.**
No arithmetic defect found in any of the numbers checked above.

## 2. Steel-man

This is genuinely disciplined EM/house-discipline work, and the strongest
part of it is squarely process, not a single physics headline. Three
things earn real credit from this seat specifically. First, R5's first-ever
real FDTD spend was gated, not merely announced: Red Team's Phase-2 audit
caught a genuine three-way convergent validation gap (MATERIALS' R15-
addendum attack, QUANTUM's fault-injection-coverage attack, this seat's own
blind Phase-2 attack on the unpriced `xi_ext`/`sigma_abs_nonneg` HALT
outcome) and all three fixes were actually built and executed — not merely
promised — before any interior-near-null R5 reading was trusted. Step 0's
fault-injection re-scoring at `family="R5"` (six scenarios, all six caught
correctly) and Step 1's far-from-null sign-recovery check (36.0°, sign
match against the established R4 reference) are the first real discharge,
anywhere in this program's 76-iteration history, of both R18's fault-
injection-coverage standard and R15's addendum ground-truth-recovery
standard *at R5's own resolution* — genuinely new evidentiary weight, not
inherited by analogy from R3/R4. Second, the energy-bookkeeping outcome
this seat's own blind critique demanded (a predicted row for the
`xi_ext`/`sigma_abs_nonneg` HALT possibility) was honored in the frozen
Predictions table before Phase 4 ran, and the gate never fired — a clean,
disclosed non-event, exactly as house discipline requires. Third, Item 1's
own honest non-resolution (a genuine "bounce," not the anticipated
crossing or clean decay) and Item 3's own honest non-resolution (neither
falsification branch clears cleanly) are both reported as such, with the
concrete new shape disclosed rather than smoothed into a false confidence
either way — the correct scientific posture for a house-discipline cycle.

## 3. Sharpest finding

**A claimed exact angular coincidence between Item 2's settling-precondition
point and its own interior-sweep bracket point is false as stated — and the
error survives, uncaught, from Phase 1 through the frozen `NOTES.md`
Result section, in the same document that caught and fixed the identical
failure shape twice over for Item 1 (Attacks 4 and 6).**

`NOTES.md`'s own Setup section (line 251, part of the frozen-before-any-run
Predictions/Setup record) states, in Item 2 Step 3's own interior-sweep
table:

> `| 39.854853° | −0.067° (= Step 2's angle) |`

— i.e., it asserts as a design fact that the interior-sweep point at offset
−0.067° from `θc40` **is** 39.854853°, literally identical to Step 2's own
settling-precondition angle (also stated as 39.854853° at line 232: "θ=
**39.854853°** (coincides with one Rank 2b interior angle...)"). This
"coincidence" is the entire justification, inherited from `phase1_
proposal.md` (lines 149–151, 178–183), for choosing that specific settling
angle rather than an arbitrary one — the design intent, stated explicitly
in Phase 1, was that Rank 2a's settling check would double as a settling
check *at one of Rank 2b's own scored interior points*.

It is not true as executed. `θc40 = 39.921519316666235` (`results.json::
item_2.step3.theta_c40`). `θc40 − 0.067 = 39.854519316666235` — this is the
literal value `run.py` computes and actually spends real FDTD on (`step3_
angles[2]`, confirmed directly in `results.json::item_2.step3.angles[2] =
39.854519316666234` and in `run_output.txt`'s own printed angle list:
`[39.521519, 39.688519, 39.854519, 40.021519]`). Step 2's own settling
angle, by contrast, is the literal hardcoded constant `settle_angle =
39.854853` (`run.py` line 421) — **not** `θc40 − 0.067`. The two values
differ by

  `39.854853 − 39.854519316666235 = 3.3368×10⁻⁴°`

— over an order of magnitude larger than the θ₀-digit-insertion error
VISION caught in this same cycle's Item 1 (`2.5×10⁻⁷°`, Attack 6), and
roughly 10× the *label* error Red Team itself caught in Item 1's own
filed-angle table (`3.33×10⁻⁵°`, Attack 4) — the identical failure
*shape* (a rounded literal-decimal offset presented as if it exactly
equalled a related quantity), recurring in this same document, at larger
magnitude, in a location none of the five blind critiques or Red Team's
own audit checked. `run.py` itself is not confused about this: line 474's
comment ("theta_c40-0.067 should coincide with the settling angle
(39.854853deg)") and the accompanying assert use a *loose* 5×10⁻⁴°
tolerance rather than bit-exact equality — the code was written knowing
the two floats would not match exactly, but `NOTES.md`'s own frozen prose
(both the Setup table, written before any run, and nowhere corrected in
the Result section 250 lines later) states the stronger, false claim of
literal identity throughout.

**Consequence, scoped honestly.** This does **not** touch the Step 3
crossing itself (`θc50≈39.77687°`, `bracket=[39.688519°, 39.854519°]`) —
that computation uses its own four directly-measured points, unaffected by
what Step 2's settling angle happens to be. What it *does* undercut is the
specific epistemic claim `NOTES.md` makes about what Step 2's settling PASS
(`rel_dev=0.18%`) actually certifies: it certifies convergence at
39.854853°, a point **not** among the four points that determined the
crossing, not literally at 39.854519° (the crossing bracket's own upper
point) as claimed. The risk this creates is bounded, not eliminated, by
data already on file: `delta_scene` at 39.854853° (Step 2, R5_STEPS) reads
`+5.253136×10⁻⁴`, and at the true nearby point 39.854519° (Step 3) reads
`+5.230823×10⁻⁴` — a 0.4% relative difference between the two, which is
reassuring evidence the curve is locally smooth enough that the settling
result very likely transfers — but this reassurance is available only
because I traced it independently; `NOTES.md` states the stronger, false
"coincide" claim and never notes the actual gap or the smoothness argument
that would license treating it as harmless.

This is precisely the class of finding this seat's own Phase-2 critique,
Red Team's Phase-2 audit (Attacks 1–4), and this program's own R4 lineage
all exist to catch — a claim of exactness that does not survive contact
with the executed code — recurring in the *same cycle*, in the *same
document*, one level away from where it was already caught and fixed
twice. Its narrow scope (a 3.3×10⁻⁴° gap, non-verdict-changing, empirically
low-risk on the data already collected) argues against this being a
Checkpoint-4-grade "known, named, ignored" defect — nobody previously named
this gap for this cycle to ignore, and it is caught here, blind, before any
later cycle cites Item 2's settling precondition as literally validating a
specific interior point it does not. It should be corrected in the
permanent record (either restate the true, non-coincident relationship
explicitly with the smoothness argument above, or spend the negligible
marginal cost of adding 39.854853° itself, already measured, to the
reported interior set) before any future T28 cycle cites this settling
check as covering the crossing bracket's own points.

## 4. Secondary findings

### 4.1 `xi_ext`/`sigma_abs_nonneg` margins are gated but never persisted — a residual R16-shaped gap this cycle's own Attack 3 fix did not reach

This seat's own blind Phase-2 critique (Attack 3, adopted) demanded a
predicted-outcome row for the possibility that `cell_metrics_r5`'s hard
`assert xi_pass`/`assert nonneg_pass` gates HALT before any `delta_scene`
reading exists — and that fix was applied correctly (`NOTES.md`'s
Predictions table now carries an explicit "no confident lean... HALT is a
live, disclosed possibility" row). But the fix addressed only the
*predicted-outcome* gap, not a companion *persistence* gap: `run.py`
computes `cell["xi_ext"]` (a dict of per-route extinction-agreement
figures) and `cell["sigma_abs_nonneg"]` for every one of this cycle's 20
R5-family cells (Step 1, Step 2 ×2 step-counts, Step 3 ×4 angles) purely to
compare against `XI_TOL` inside a boolean gate — confirmed directly:
`grep -c "xi_ext" results.json` returns **0**. Nowhere in `results.json`
can a reader verify *how close* R5's first-ever real energy-bookkeeping
check came to its own tolerance boundary; only that it did not exceed it
(no crash occurred). This is the same shape LOGBOOK's own R16 (Iteration
71) names — a governing quantity computed everywhere and persisted
nowhere — applied here not to a NETD byproduct but to this seat's own
charter quantity (an extinction-routes energy-conservation identity). Not
new to this cycle (the same gap exists in the inherited R3/R4 code path
this cycle reused unmodified), and not load-bearing to any verdict here —
but this cycle's own Attack 3 named exactly this energy-bookkeeping gate as
a live risk and only priced its *failure mode*, not its *margin*, leaving
the next reader unable to independently judge how comfortably R5's first
real spend actually cleared this seat's own gate. A cheap fix (persist
`max(cell["xi_ext"].values())` and `cell["sigma_abs_nonneg"]` into every
report row, mirroring the already-persisted `ratio_abs_ext_raw_*`/
`sigma_ext_cells_*` fields) closes it at zero marginal FDTD cost.

### 4.2 R15's addendum is discharged to the letter, but its own single-point limit is real and should stay visible

Step 1's far-from-null sign check (36.0°, 1.127° from the nearest
established null) genuinely discharges MATERIALS' Phase-2 attack and R15's
own addendum text — this is a real, substantive gate, not a paperwork
gesture, and `NOTES.md`'s own Idealization 59 discloses its limit honestly
("establishes sign-agreement at ONE point; it does not certify R5's
construction is defect-free at every angle"). Worth restating for the
record, since this exact sub-thread's own history (T28/R15's founding
instance, exp-094→exp-095) shows a single-point check is a *necessary*, not
*sufficient*, discriminator between genuine physics and a systematic
registration/dispersion defect that manifests specifically near a null —
the class of defect a far-from-null point is structurally unable to catch.
This is not a defect in this cycle's own work (the disclosure is already
correct and appropriately conservative) — it is a note that Item 2's Step
3 crossing (`θc50≈39.777°`) should continue to be read as "R5's first
gated reading, consistent with the established trend," not yet as
"R5-resolution-confirmed" in the fuller sense R15's own addendum was
written to eventually require (a second, differently-conditioned check, per
that rule's own text).

### 4.3 Richardson diagnostic's field names are a house-discipline readability risk, not a defect

`results.json::item_2.step3.richardson_30_40_50` stores the 30→40 shift
under the JSON key `"shift_20_30"` and the 40→50 shift under
`"shift_30_40"` — a deliberate, explicitly disclosed positional relabeling
(`richardson_style_diagnostic()`'s own docstring permits it, and both
`phase1_proposal.md` and `NOTES.md` state the relabeling in prose at every
point of use). Independently verified this is not a bug: the *values*
under those keys are correct for the 30/40/50 triple, only the key *names*
literally describe the function's original 20/30/40 argument order. This
is adequately disclosed within this document and does not rise to an R9
violation (the commensurability is stated, not silently assumed) — but a
future citation that reads `results.json` directly, without the
surrounding prose, would misread `"shift_20_30": −0.150319` as a literal
20→30 shift. A one-line clarifying key (e.g. `shift_pair_a`/`shift_pair_b`)
in any future reuse of this function for a third triple would remove the
risk at zero cost; not urgent enough to gate this cycle's own verdict.

## 5. Verdict

**CONCUR-WITH-GAP(S).**

Every mandatory Phase-2 fix was genuinely, verifiably implemented (not
merely claimed) — I independently traced Fixes 1, 2, 4, 5, and 6 against
`run.py`'s actual code and `results.json`'s actual output, not `NOTES.md`'s
own account of them. Every headline number I recomputed reproduces
exactly. The science itself is sound and honestly reported, including two
genuine non-resolutions (Items 1 and 3) that were not smoothed into false
confidence. Set against that: one genuinely new, previously-uncaught claim-
accuracy defect (§3) — the same failure shape this cycle's own review layer
caught and fixed twice for Item 1, recurring unfixed in Item 2 — plus one
real, non-load-bearing energy-bookkeeping persistence gap (§4.1) inside
this seat's own charter area. Neither changes any reported verdict; both
should be corrected before either quantity (Step 2's settling coverage,
R5's `xi_ext` margin) is cited by a future cycle as more thoroughly
established than it is.

## 6. Ranked top-3 candidate directions for Iteration 77

Independently reasoned; I partly **disagree** with `NOTES.md`'s own draft
ordering (which ranks "widen the Null C bracket further" as Next item 1 and
the T1/constraint-scoring trigger as item 2) — I would invert that
priority.

**1. Run the actual constraint-1/2/3/4 scoring pass — rank this above any
further T28-internal instrument work, not below it.** THERMODYNAMICS' own
Phase-1 disposition (§T1, this cycle) is sound reasoning as far as it goes,
but from this seat's own charter — formalizing what T1 *permits and
forbids* — the more forceful framing is: after seven consecutive cycles
(exp-093–exp-099) of pure instrument/resolution/registration validation on
one diffraction feature, there is currently **no scored claim anywhere in
this program's record** about whether the now-extensively-characterized
`delta_scene(θ)` sign structure, taken as an angular-selectivity mask,
actually helps or hurts against beam-termination, backscatter, or ambient-
contrast — the metrics PANEL.md's own table requires every run to advance.
This is not a scheduling nicety; it is this seat's own bookkeeping duty
left undischarged for a whole escape-route candidate. I concur with the
override trigger `NOTES.md` itself states and would make it non-negotiable
for Iteration 77, ahead of any further bracket-widening.

**2. Before spending more FDTD on Null C, fit the newly-discovered
"bounce" (the local minimum near θ₀+0.5°–0.83° found this cycle) against
T28's own already-gated closed-form models — zero new FDTD.** This
sub-thread already has multiple passivity/reciprocity-gated analytic
constructions on file (the single- and two-wall transfer-matrix echo
models, GP1/GP2′, the y-wall aperture-sum family) that have never been
scored against this specific new feature (a genuine trough, not the
crossing or asymptote the pre-registered trichotomy anticipated). A
zero-cost fit of the 7 combined points against these existing, gated
models is a materially cheaper and more diagnostic next step than a fourth
symmetric-or-asymmetric bracket-widening exercise, and is squarely this
seat's own charter territory (does any already-validated wave model
predict a local extremum here, and if so at what physical length scale).

**3. Close this review's own two findings and extend R5's energy ledger,
not just its sign check.** Persist `xi_ext`/`sigma_abs_nonneg` margins into
every R4/R5 report row going forward (§4.1); correct or re-scope the Item
2 "coincidence" claim (§3, negligible marginal cost — the point in
question, 39.854853°, is already measured). Then use the now-built R5
machinery to extend T28's own established Poynting-box energy-interception
cross-check (exp-087's instrument, never yet run at R5's resolution) to
Null B's own crossing region — strengthening R5's ground-truth standing
beyond a single far-from-null sign check (§4.2) while simultaneously
closing this seat's own named persistence gap, at low marginal cost given
the machinery already built this cycle.
