# PHASE 5 — REVIEW · Panel Iteration 83 · Seat: ELECTROMAGNETISM
## exp-106 — "Floor-Gating, Settling, Risk-Propagation, and the Fixed-Absolute-Thickness Control for `kappa_window`"

*Fresh context, blind to any other seat's current-cycle Phase-5 review, per
PANEL.md. Read in full: PANEL.md; LOGBOOK.md (RULED OUT R1–R23; LIVE
THREADS T1–T21 in full, T28 in full through Iteration 82/exp-105); the
complete exp-106 record (`phase1_proposal.md`, all five
`phase2_critique_*.md`, `phase2_redteam_audit.md`, `NOTES.md`, `run.py`,
`results.json`); exp-105's own `NOTES.md`. Every headline number below is
recomputed directly from `results.json`'s raw fields, not restated from
NOTES.md's prose (R4/R8/R19 discipline) — arithmetic shown, not asserted.*

## Verdict: **CONFIRM-WITH-GAPS**

The risk-propagation gate I flagged at exp-105 Phase 5 (P3 had no
equivalent to P4's `p4_156_trusted`) is now built, symmetric in kind for
both families, correctly forced False by the same fixed domain-geometry
property, and independently reproducible from primitives — real,
load-bearing self-correction, not decoration. But the fix was built one
layer too shallow: (1) the *same* unsettled, MARGINAL-tier r=312 capture
also backs `abs_ratio(312)=1.8797`, a brand-new, ungated cross-family
metric this cycle introduces and reports without any trust caveat —
exactly the asymmetric-rigor shape Red Team's own Attack 7 closed for
`shape_ratio_fixedabs` but never extended to; (2) Red Team's own mandatory
fix 1 wrote a specific, numeric reclassification rule (`p_abs_frac_diff`
>10% ⇒ report item 4 as three-way AMBIGUOUS, not a clean REFUTE/CONFIRM
binary) that NOTES.md's Panel record claims was "ADOPTED in full," but
`run.py`'s actual classification logic never implements it — and the
measured `p_abs_frac_diff` (12.3% at r=156, 18.0% at r=312) *exceeds* that
threshold at **both** r, including r=156, this cycle's one fully
TRUSTED/settled point. Both gaps are self-disclosed honestly in NOTES.md's
Result section (not hidden), and neither reverses the reported REFUTE
classification's arithmetic — but both bear directly on how much
confidence that classification actually deserves, at exactly the two
places this cycle's own new machinery was supposed to settle that
question.

---

## 0. Independent numeric verification

All figures below recomputed from `results.json`'s raw fields.

**Nyquist margins/tiers.** `nyquist_margin = predicted_ripple_period /
(2·DENSE_PITCH)`, `DENSE_PITCH=2`. r=78: `19.743590/4 = 4.935897` →
`≥2.0` → **TRUSTED**. r=156: `9.871795/4 = 2.467949` → `≥2.0` →
**TRUSTED**. r=312: `4.935897/4 = 1.233974` → `≥1.0, <2.0` →
**MARGINAL-REDUCED-CONFIDENCE**. All three reproduce the stored
`nyquist_margin` fields exactly and match exp-105's own committed values
(Gate P0 passing confirms this independently as well).

**`p3_trusted` / `shape_ratio_fixedabs_trusted` forcing logic.** Both are
defined `settle_312_pass AND (nyquist_tier(312)=="TRUSTED")`. Since
`nyquist_tier(312)="MARGINAL-REDUCED-CONFIDENCE"` for **both** families
(identical domain geometry, confirmed: `geom_312_fixedabs`'s
`nyquist_margin` field is bit-identical to `geom_312`'s, `1.233974...`),
the boolean is forced False **regardless of the settling leg's outcome or
even whether it ran** — verified directly against `settling_r312` in
`results.json`, which shows `pass_: false, rel_change: null` for both
families (the settling leg never ran; `pass_` defaults to `False`, the
same value a genuine failure would produce — a minor representational
wrinkle, discussed in §2, that does not affect the correctness of the
forced-False conclusion since the Nyquist term already forces it
independently). `p3_trusted=False`, `shape_ratio_fixedabs_trusted=False`
— **both reproduce exactly as predicted**, and the forcing logic is
mechanically correct.

**`noise_floor_flag` values.** Self-similar: `denom = k156−k312 =
0.0008866623871477821 − 0.00000479303718569495 = 0.0008818693499620872`
(matches `p3_selfsim.noise_flag.denom` exactly); `noise_floor =
3×0.10×|k156| = 0.00026599871614433463` (matches). `|denom| >
noise_floor` ⇒ `noise_dominated=False` — correct. Fixed-abs: `denom =
0.000962183331795694 − 0.000009009267358438566 = 0.0009531740644372554`
(matches exactly); `noise_floor = 0.3×0.000962183331795694 =
0.00028865499953870826` (matches); `noise_dominated=False` — correct.
Neither shape_ratio denominator is anywhere near collapse; this specific
R13/R14-style hazard did not fire this cycle.

**`shape_ratio` reproduction.** Self-similar: `(k78−k156)/(k156−k312) =
(0.018336958179764707−0.0008866623871477821)/0.0008818693499620872 =
0.017450295792616925/0.0008818693499620872 = 19.7878...` — matches
`p3_selfsim.shape_ratio=19.787847024468125` and reproduces exp-105's
committed 19.79 to four significant figures, from a **freshly executed**
capture (reproduction check `rel_dev=0.000e+00` against exp-105's own
committed `kappa_window` values at both r=156 and r=312 — exact, not
merely close). Fixed-abs: `(0.018336958179764707−0.000962183331795694)
/0.0009531740644372554 = 0.017374774847969013/0.0009531740644372554 =
18.2283...` — matches `item4_fixedabs.shape_ratio=18.228333623646076`.
`18.2283 ≥ 14.8` (the pre-registered REFUTE threshold) — the
classification arithmetic is correct on its own terms.

**`abs_ratio`.** r=156: `0.000962183331795694/0.0008866623871477821 =
1.08517...` — matches `1.0851744088196273`. r=312:
`0.000009009267358438566/0.00000479303718569495 = 1.87966...` — matches
`1.8796573048352636`. Both inside the pre-registered factor-of-2.0 band
(`0.5 ≤ x ≤ 2.0`) — correctly classified as passing, per §2 below.

**Ledger arithmetic.** `abs_ext_ratio = sigma_abs/sigma_ext`: r156
selfsim `249.017/480.688=0.51804`, fixedabs `279.661/560.199=0.49922`;
r312 selfsim `498.483/960.446=0.51901`, fixedabs `588.022/1191.326=
0.49359` — all four reproduce the stored `abs_ext_ratio` fields exactly
and sit in the 0.49–0.52 band cited in the task brief, broadly consistent
in magnitude with the ESTABLISHED σ_abs/σ_ext≈0.51 absorber anchor
(exp-002), though this is a different measurement channel/geometry and
T9 already forecloses reading 0.51 as an asymptotic constant. `core_frac`
is exactly `0.0` at all four (r, family) points — perfectly clean.
`box_dev` (established ≤0.12 convention): 7.97×10⁻⁵/7.58×10⁻⁴ at r=156
(ss/fa), 4.90×10⁻⁵/2.20×10⁻⁴ at r=312 — all 2+ orders of magnitude
inside bound, confirmed clean. `p_abs_frac_diff`: r156
`|279.661−249.017|/249.017=0.12306`, r312 `|588.022−498.483|/498.483=
0.17962` — both reproduce the stored values exactly and both exceed the
informal 10% figure `run.py`'s own print statement uses — see §1.

**Cost-gate arithmetic — the one place I found a genuine, if minor,
reproducibility gap.** Primary leg: `wall_312_empty_pilot_s=
3158.8114171028137s = 52.6469 min < 90` → pilot clears; projected
3-call total `= 3×52.6469 = 157.94 min < 180` → **commit** — matches
`r312_primary_committed=true` and NOTES.md's own "52.65 min" figure
exactly. **Settling leg: NOTES.md's Result section states the settling
leg's own empty-scene pilot "took 6196.6s (103.28 min)."** This number
does **not** appear anywhere in `results.json` as its own field — no
`wall_312_empty_settling_pilot_s` key exists; `wall_312_settling_s` is
`null` (that field is reserved for the never-run *article* pair, not the
pilot). The only way to check it is by subtraction: `total_wall_s
(18398.414408683777) − [wall_156_primary_s (1054.554) +
wall_156_settling_s (1633.387) + wall_312_empty_pilot_s (3158.811) +
wall_312_article_s (6332.601)] = 6219.061s (103.65 min)` — the implied
residual is **22.46s (0.36%) larger** than the figure NOTES.md's Result
prose cites, and this residual also absorbs whatever non-FDTD numpy
processing (floor gates, ledger checks, the 53-point `dense_x` loop) ran
on N=2240 (~5×10⁶-cell) arrays between the pilot call and the final
timer read, so it is not even a clean isolate of the pilot alone. **The
qualitative conclusion is unaffected either way** — 103.28 min and 103.65
min both clear the 90-minute abort threshold by a wide margin, so the
settling leg's deferral is correctly triggered under either reading, and
no `run_output.txt` exists to arbitrate which figure is the console
ground truth. But this is exactly the shape of gap R4/R19 exist to
catch: a specific number entered NOTES.md's permanent Result prose
without a code-enforced, independently-reproducible source in the
committed artifact — non-load-bearing here (see the margin above), but a
genuine, disclosed-nowhere transparency gap in a cycle whose entire
mandate is closing exactly this kind of unverified-figure risk on a
sibling channel (item 1's floor-gate persistence). Recommend: persist
the settling-pilot wall time as its own named field in any future cycle
that pilots a leg, exactly as `wall_312_empty_pilot_s` already is for
the primary leg.

**P2 monotonicity.** `0.018336958 > 0.0008866624 > 0.0000047930` — true;
`p2_verdict="CONFIRMED"` is correct.

## 1. Does the risk-propagation gate now work correctly and symmetrically? — Yes, at the layer it was built for; no, one layer down

The core self-correction is real. `p3_trusted` and
`shape_ratio_fixedabs_trusted` are defined by the *identical* boolean
formula (`settle_312_pass AND nyquist_tier(312)=="TRUSTED"`), evaluated
against a `nyquist_margin(312)` value that is bit-identical between
families by construction (both `geom_312` and `geom_312_fixedabs` share
every domain field except `R_CORE`/`sigma_max`/`tau_shell` — verified in
§0) — this is genuinely symmetric in kind, not merely in name, closing
the exact gap I flagged at exp-105 Phase 5 (P3 had no gate at all where
P4 had `p4_156_trusted`). The classification string correctly appends
`(NOT-TRUSTED — r=312 MARGINAL/unsettled)` rather than silently
suppressing the number — the right house-style choice (report, don't
hide, per this program's own established convention).

**But the gate does not propagate to every downstream number built from
the same at-risk r=312 capture.** `abs_ratio(312)=1.8797` — introduced
this cycle (PHOTONICS' own mandatory fix 2, adopted at Phase 3) — is
computed from `kappa_window_312_fa` and `kappa_window_312_ss`, the
identical 1×-STEPS, never-settling-verified r=312 fields `shape_ratio_
fixedabs` is built from. NOTES.md's own Result section states this
explicitly is "NOT gated by `..._trusted`" and reads the result as
corroborating evidence alongside item 4's REFUTE — but `abs_ratio(312)`
inherits exactly the same unsettled-capture risk `shape_ratio_
fixedabs_trusted` was built to flag, and receives no caveat at all.
This matters quantitatively, not just formally: `1.8797` sits at 94% of
the factor-of-2.0 band's own edge — a modest shift in the true (settled)
`kappa_window_312` values in either direction could plausibly move this
number across the band boundary, flipping "geometric-window dominance
corroborated" to "outside the band." This is the same asymmetric-rigor
shape Red Team's own Attack 7 named and closed for `shape_ratio_
fixedabs` this cycle (a soft caveat where a hard suppressor belongs) —
recurring one metric downstream, uncaught by any of the five Phase-2
critiques or Red Team's own audit. I do not think this rises to a
firing-grade recurrence on its own (it is the second instance of this
specific shape in this exact sub-thread — exp-105's original P3/P4
asymmetry was the first — and, like every prior R-rule's founding
instance, this is caught here at Phase 5, not defended past it), but it
is the kind of pattern this program's own R13/R14/R17 lineage explicitly
tracks, and a third instance on this channel should be read as
established, not novel.

## 2. The ledger check's own energy-bookkeeping concern: real, disclosed, and its own pre-registered consequence was not actually coded

`core_frac=0.0` at every (r, family) is clean, but — per Red Team's own
Attack 9, correctly anticipated and never contradicted by this cycle's
data — this is close to tautological for a PEC core (`Ez≡0` inside by
construction), so it cannot by itself detect the exact hazard EM's and
THERMODYNAMICS' own Phase-2 critiques raised: core-reflection/
diffraction leakage into the forward window as `R_CORE/R_COAT` climbs
past T9's only-validated 0.385 anchor (fixed-abs reaches 0.692/0.846).
`box_dev` is clean (2+ orders of magnitude under the established ≤0.12
bound at all four points) — genuine, useful evidence of box-independence,
i.e. that `sigma_abs`/`sigma_ext` are being measured consistently, not
evidence the *comparison across families* is clean.

The one instrument that actually speaks to the cross-family confound —
`p_abs_frac_diff` — **exceeds** the 10% figure Red Team's own mandatory
fix 1 named as the dividing line (12.3% at r=156, 18.0% at r=312), and
this crosses the line at **r=156**, this cycle's one fully TRUSTED,
cleanly-settled point (Nyquist TRUSTED, settling PASS at 3–4 orders of
magnitude inside tolerance for both families) — not only at the
already-flagged-risky r=312. That is a materially different finding
than "the risky point looks risky": it says the two families'
absorbed-power fractions diverge by a non-trivial amount even where
nothing else about the measurement is in question, which is exactly the
condition under which THERMODYNAMICS' own Phase-2 flip condition said
item 4's two-hypothesis framing needs to move from a clean binary to
"three-way AMBIGUOUS (thickness-law vs. core-reflection/gradient-
steepness vs. both)." Red Team's own `phase2_redteam_audit.md` §3.1 item
1 states this reclassification rule in exactly those terms, under the
heading "[Highest priority]," and NOTES.md's Panel record states flatly
that "All 7 of Red Team's mandatory fixes ADOPTED in full." **I checked
`run.py`'s classification logic directly (lines computing `p4_fa[
"classification"]`): it applies only the `SHAPE_RATIO_FIXEDABS_CONFIRM`/
`_REFUTE` numeric bands, the `noise_dominated` flag, and the `_trusted`
flag — nowhere does `p_abs_frac_diff` or any 10% threshold enter the
classification string.** NOTES.md's own Result section discloses this
gap candidly ("No pre-registered pass/fail band was frozen for this
specific quantity... reported here as a genuine, disclosed, un-gated
observation for Phase 5 to weigh") — which is the right house instinct
and is why I do not read this as a hidden defect. But it does mean the
Panel record's "ADOPTED in full" is imprecise for mandatory fix 1
specifically: the mechanical ledger computation was adopted; the
reclassification *consequence* Red Team wrote into the same fix was not
implemented as a binding gate, only as an unscored number left for a
human reader to notice. Given the observed divergence exceeds the named
threshold at the one point (r=156) where every other precondition is
clean, `item4_fixedabs`'s "REFUTES-electrical-thickness-growth-
hypothesis" classification is arithmetically correct against its own
`shape_ratio` bands but should not yet be read as a validated clean
two-hypothesis result even independent of the r=312 trust flag — a
third channel (core-reflection or gradient-steepness) remains a live,
disclosed-but-unresolved candidate contaminant, exactly per THERMODYNAMICS'
own Phase-2 critique, which this cycle's own ledger data corroborates
rather than closes.

**T1/passivity/reciprocity/causality bookkeeping — unchanged, correctly
N/A.** `sigma_max` stays strictly positive at every (r, family)
combination checked (0.5/0.25/0.125 self-similar; 0.5 fixed-abs
uniformly) — no gain anywhere, passivity holds trivially. `tau_shell=
24.0` is held exactly fixed (verified via the module's own printed
assertions and independently recomputed: `0.125×192=24.0`,
`0.5×48=24.0`, etc., at every r in both families). Reciprocity remains
moot (single-source, no source/observer swap on this bench family).
Causality is moot for a steady-state phasor instrument. Nothing this
cycle executed changes T1's correct N/A disposition.

## 3. Other gaps, cross-checked against LOGBOOK's registry

- **R4/R19 lineage**: the settling-pilot wall-time figure (§0) is the
  kind of number this registry exists to keep code-enforced and
  reproducible; it currently is neither. Non-load-bearing this cycle
  (margin against the 90-min threshold is enormous either way) but worth
  a one-line fix forward, not a Checkpoint-grade finding.
- **R13/R14 lineage**: `abs_ratio(312)`'s missing trust caveat (§1) is a
  second instance, in this same T28 sub-thread, of a metric built from
  an at-risk capture escaping the rigor a sibling metric received. Not
  yet a firing pattern (caught here, at Phase 5, same cycle it was
  introduced) but worth a Red Team ruling on whether this constitutes
  the second data point toward a forward-elevating clause, given
  Attack 7 already named the first instance of this exact shape one
  layer up, in the same cycle.
- **R7 lineage** (a design/pricing number is necessary, not sufficient,
  for a closure/detection claim without being scored against a
  pre-registered band): `p_abs_frac_diff`'s un-coded reclassification
  rule (§2) is a close cousin — a number was computed, exceeded its own
  named threshold, and the consequence Red Team itself specified was not
  applied as a binding gate on the headline classification. NOTES.md's
  own honest disclosure keeps this from meeting R7/R8's "unverified
  argument defended past a named check" firing shape — the check WAS
  run and its result WAS disclosed, just not wired into the
  classification logic — but this is worth flagging in writing, per this
  program's own standing discipline that a Phase-3 synthesis claiming
  "adopted in full" should mean what it says at the code level, not only
  at the level of "the underlying data exists somewhere in
  `results.json`."
- **Gate P0/reproduction checks**: both exact (`rel_dev=0.000e+00` at
  r=156 and r=312), independently re-derived in §0 from a fresh capture,
  not merely re-read from the same file — genuinely load-bearing
  confirmation that this cycle's new machinery is measuring the same
  physics exp-105 measured, before any of the new diagnostics are
  trusted.
- **Floor-gate item 1**: the frozen Predictions' own "possibly >10%
  unresolved at r=312" concern is cleanly falsified in the reassuring
  direction (`frac_unresolved=0.0000` at both r, `n=4000`, `rms≈5.00`,
  `floor≈0.50`) — a genuine, correctly-scored negative result, not a
  close call.
- No unfalsifiable claims, no constraint quietly dropped (T1/constraint-3
  are both explicitly, repeatedly, correctly scoped N/A this cycle, with
  numbers, matching R21's own "narrate, don't just persist" standard for
  every gate this cycle introduces — I checked `predictions_text`/
  `result_text` directly and both contain the DISCLAIMER string verbatim,
  satisfying the two `assert DISCLAIMER in ...` sites R23 requires; VISION's
  own Phase-2 concern that new verdict text might land outside the
  asserted strings is not realized — items 1–4's actual numbers are all
  concatenated into `result_text` itself, confirmed by direct inspection).

## Ranked top-3 candidate directions for Iteration 84 (ELECTROMAGNETISM's own picks)

1. **Run the deferred r=312 settling leg on `kappa_window` (both
   families).** This remains the single largest disclosed, un-closed
   physical-settling risk directly underlying both P3's `shape_ratio=
   19.79` and item 4's `shape_ratio_fixedabs=18.23` — the one leg this
   cycle's own frozen Predictions named "the most urgent... genuinely
   uncertain" and the one leg that did not resolve this shift. Until it
   runs, `p3_trusted`/`shape_ratio_fixedabs_trusted` stay forced False by
   the Nyquist term alone regardless, but the settling question itself
   (does `kappa_window_312` change under doubled STEPS at all?) remains
   genuinely open, not merely gated.
2. **Extend `..._trusted`-style gating (or at minimum an explicit inline
   caveat) to `abs_ratio(312)`, and code Red Team's own `p_abs_frac_diff`
   >10% ⇒ three-way-AMBIGUOUS reclassification rule as a binding
   override on `item4_fixedabs["classification"]`, not an unscored
   observation.** Both are cheap, mechanical, zero-new-FDTD-cost fixes
   (the underlying numbers already exist in `results.json`) that close
   the two concrete gaps §1/§2 name — directly analogous to how this
   cycle itself closed exp-105's own P3/P4 asymmetry, applied one layer
   further down the same architecture.
3. **A genuine hollow-vs-PEC-cored `sections.radial_absorbed_power`
   delta test (exp-052's own original T9 methodology) for the fixed-abs
   family at r=156/312 — its now-higher `R_CORE/R_COAT` ratios (0.692,
   0.846) past the only point this program has ever validated a PEC
   core's energetic incidence at.** This cycle's ledger check
   (`core_frac`, `box_dev`) is necessary but, per Red Team's own Attack
   9, structurally cannot detect core-reflection leakage on its own; a
   real hollow-core comparison (a Tier-2 item this cycle explicitly
   deferred, disclosed as such) is the only instrument that actually
   answers the question EM's and THERMODYNAMICS' own Phase-2 critiques
   raised and that §2's own `p_abs_frac_diff` finding now sharpens from
   "a named risk" to "a measured, threshold-exceeding divergence at a
   fully trusted point."
