# PHASE 5 — REVIEW · PHOTONICS · exp-089 · Panel Iteration 66

*Fresh context, blind to any other seat's current-cycle Phase-5 output. Read
in full: PANEL.md; LOGBOOK.md's RULED OUT (R1–R14) and ESTABLISHED sections;
LIVE THREADS/T28 (Iterations 58–65, both CHECKPOINT entries) through
exp-088; the complete exp-089 record (`phase1_proposal.md`, all five Phase-2
critiques, `phase2_redteam_audit.md`, `phase3_synthesis.md`, `NOTES.md`,
`results.json`, `run.py`); exp-088's `phase5_review_photonics.md` for
house-style calibration. No FDTD run; no other file modified.*

## Verdict

**CONCUR-WITH-RESERVATIONS (T28 instrument work — no PROMISING/RULED-OUT
candidate-physics claim to grade).** I independently reproduce every
load-bearing number in Q3/Q4/Q6 from raw `results.json` primitives (§1) —
no R4-class slip. I concur with NOTES.md's own Q6 combined classification
(ENERGY-DOMINANT, 7/8 resolved) and with its own Learned §2 that R13's
`FLOOR_FRAC=0.10` reads as materially too permissive. My reservation is
about **attribution**, on my own charter: the record (including my own
Phase-2 critique this cycle) frames this as vindication of an R14
numerator-hazard warning — a "hidden sub-half-period feature" inside the
1.4° gap. The data do not support that specific mechanism. What actually
drove θ=40.2°/41.4° into ENERGY-DOMINANT territory is a **thin,
R13-class denominator** (`frac_contrast` at the second- and
third-smallest values of any floor-clearing point this sub-thread has
ever measured) paired with an **unremarkable, smoothly-continuing
numerator** — not a numerator spike narrower than the interior gap. My
own Phase-2 attack was right about the yardstick being conceptually
wrong; it was wrong to imply the practical failure mode would be a
missed narrow feature. It wasn't — it was ordinary continuation, and the
"wild swing" verdict of ratio_k lived downstream, in the ratio's own
sensitivity to a small denominator, not in a numerator ambush.

## 1. Independent recomputation from raw primitives

`frac_p_abs(θ) = |p_abs_w(G40,θ) − p_abs_w(C40,θ)| / p_abs_w(C40,θ)`,
`ratio_k(θ) = frac_p_abs(θ) / frac_contrast(θ)`. Pulled `p_abs_w` directly
from `results.json::thermo` (not from the summary `frac_p_abs`/`ratio_k`
dicts) and `frac_contrast` from `results.json::frac_contrast_new_angles`:

| θ | p_abs_w(C40) | p_abs_w(G40) | sign(G40−C40) | frac_p_abs (mine) | frac_p_abs (filed) | frac_contrast | ratio_k (mine) | ratio_k (filed) |
|---|---|---|---|---|---|---|---|---|
| 37.2° | 2.8127043563514567e-12 | 2.808672836407139e-12 | **−** | 1.4333×10⁻³ | 1.4333×10⁻³ | 4.1627×10⁻⁴ | 3.4433 | 3.4433 |
| 40.2° | 3.0772514226100976e-12 | 3.055401643746287e-12 | **−** | 7.1004×10⁻³ | 7.1004×10⁻³ | 2.8309×10⁻⁴ | 25.082 | 25.082 |
| 41.4° | 3.1649493630721244e-12 | 3.187842683949576e-12 | + | 7.2334×10⁻³ | 7.2334×10⁻³ | 2.5110×10⁻⁴ | 28.807 | 28.807 |

All three reproduce bit-exact from the persisted `p_abs_w`/`frac_contrast`
primitives (six-figure agreement, hand-verified division). **No arithmetic
defect anywhere.** I also reconstructed the sign of `(G40−C40)` at every
one of the 8 combined-set angles from the `r14a_smoothness_gate::steps`
sub-values (which carry `v_prev`/`v_cur` = `p_abs_w` at each config/angle):

```
θ:      36.0°  37.2°  38.4°  38.6°  38.8°  40.2°  41.4°  41.8°
sign:     +      −      +      +      +      −      +      +
```

**Both `p_abs_w(C40,θ)` and `p_abs_w(G40,θ)` are individually smooth and
strictly monotonically increasing across all 8 points** (I re-verified
this directly against the same `r14a_smoothness_gate` step values — every
`v_cur ≥ v_prev`, matching the filed PASS) — confirming R14(a)'s gate is
not merely asserted but genuinely satisfied. Yet their *difference's sign*
flips twice, at intervals (36.0°→37.2°=1.2°, 38.8°→40.2°=1.4°) that are
not evenly spaced at anything resembling half of `delta_scene`'s
2.84–2.95° period (~1.42–1.475°) — a clean inherited half-period
alternation would show flips roughly every ~1.45°, not one flip then
three same-sign points then another flip. This is architecturally
consistent with R14's own founding diagnosis (subtractive cancellation
between two independently-varying, comparable-magnitude curves is
fragile "by its own arithmetic shape," QUANTUM, exp-088) — not with a
clean inherited periodic signal.

## 2. Vindicated, or a different mechanism? — the question this review was asked

**Neither cleanly.** My own Phase-2 critique this cycle argued R14(c)'s
half-period bound borrowed the wrong quantity's period, and that against
`frac_p_abs`'s actual demonstrated (sub-0.4°) scale, the 1.4° gap "isn't
a near-miss, it's ~3.5× too wide to guarantee no hidden feature." Now
checked against real data at 40.2°/41.4°:

- **The general point stands**: `frac_p_abs`'s own native behavior (the
  sign-flip table above) is demonstrably not well-approximated by
  `delta_scene`'s smooth single tone, so R14(c)'s borrowed yardstick was
  conceptually the wrong quantity — this is not newly shown, but it is
  now doubly confirmed on a second angle pair.
- **The specific failure mode I warned about — a narrow (<0.4°) spike
  hidden inside the 1.4° gap, missed by coarse sampling — did not
  happen.** Compare Q4's own pre-registered "smooth 38.8°→41.8° trend"
  desk estimates (computed *before* Phase 4, from the two flanking
  points only) against what Phase 4 actually measured:

  | θ | naive smooth-trend estimate (pre-Phase-4) | actual `frac_p_abs` | ratio (actual/trend) |
  |---|---|---|---|
  | 40.2° | 6.5427×10⁻³ | 7.1004×10⁻³ | **1.085×** |
  | 41.4° | 7.0463×10⁻³ | 7.2334×10⁻³ | **1.027×** |

  Both land within ~3–9% of the naive linear interpolation — an order of
  magnitude *closer* to the trend than the same method's own 3.17× miss
  at 38.4° one cycle earlier. **The naive, explicitly-distrusted
  interpolation was right this time; the qualitative CONSISTENT lean the
  document actually committed to (built on the correct observation that
  the method is unreliable in general) was wrong at exactly these two
  points.** This is a smooth continuation, correctly anticipated by the
  interpolation my own critique (and the proposal's own Q3) argued not to
  trust — not a narrow feature squeezed into the gap and missed.
- **What the interior-gap framing obscures is where the real hazard
  actually sat.** `frac_contrast(40.2°)=2.831×10⁻⁴` and
  `frac_contrast(41.4°)=2.511×10⁻⁴` are the second- and third-smallest
  `frac_contrast` values of any of the 8 now-measured angles — smaller
  than every previously-floor-clearing point (36.0°: 7.44×10⁻⁴; 38.4°:
  1.44×10⁻³; 38.8°: 1.54×10⁻³; 41.8°: 1.26×10⁻³ — all recovered from
  their cited FLOOR-margin multiples), beaten only by 38.6° itself
  (7.48×10⁻⁵, which fails the gate outright). These two points are, by
  construction, R13-node-adjacent — that's *why* the proposal picked
  them. A moderately-sized, unremarkable numerator divided by an
  anomalously small (though gate-passing) denominator is exactly R13's
  own hazard class, not R14's: the denominator is doing almost all of
  the work in both blow-ups, and it is doing so from a margin (1.31×–
  1.48× FLOOR) that R13's binary gate treats as safely clear.

**Conclusion on the charge**: my Phase-2 attack's *diagnosis* (wrong
yardstick) was correct; its *implied prognosis* (a hidden narrow
numerator feature would be missed) was not what happened. The actual
mechanism is R13-adjacent — a floor gate whose margin turned out not to
be protective — which is a genuinely different, and in my view sharper,
finding than "R14(c) let a feature through." NOTES.md's own Learned §2
independently reaches the FLOOR_FRAC-too-permissive conclusion but frames
it descriptively ("both misses happened well inside the clears region")
without diagnosing *why* — the sigma/ratio decomposition above supplies
the missing why: it's a small-denominator effect riding an ordinarily-
behaved numerator, not two comparably-surprising quantities colliding.

## 3. Is the optical response internally coherent?

**Yes, entirely — the swing lives in the ratio construction, not in the
underlying optical quantities.** Independently checked across all 8
angles:

- `p_abs_w(C40,θ)` and `p_abs_w(G40,θ)`: individually smooth, strictly
  monotonic (§1) — the absorbed-power channel itself shows nothing
  incoherent across this 5.8° span.
- `ratio_abs_ext` (T9 anchor): 0.5126–0.5151 across all 6 new-angle
  cells (`results.json::ratio_abs_ext_new_angles`), within 0.5–1.0% of
  T9's established broadside 0.51 anchor and matching exp-087/088's own
  0.5128–0.5138 range — the absorption/scattering partition is flat and
  unremarkable at every one of these angles, including the two that read
  ENERGY-DOMINANT. Nothing about the underlying material response is
  doing anything unusual at 40.2°/41.4° specifically.
- `sigma_ext_cells` rises smoothly and monotonically with θ across the
  combined set (303.8→323.2 across C40, 303.8→323.2 across G40,
  36.0°→41.8°) — ordinary oblique-incidence cross-section growth, no
  discontinuity.

Given all of that, calling 40.2°/41.4° "ENERGY-DOMINANT" — language that
reads as a distinct *optical regime* — overstates what changed physically.
What changed is that two smooth, nearly-parallel curves (`p_abs_w` for
C40 vs. G40) sit close enough together, and `delta_scene` sits close
enough to zero, that dividing one small residual by another produces a
large, unstable number. This is the R13/R14 "construction artifact"
reading, independently confirmed here with the actual numbers rather than
argued in the abstract: **the classifier's own architecture — a ratio of
two independently near-cancelling differentials — is what swings wildly,
not the photonic response feeding it.**

## 4. On this cycle's own house-discipline record

The 41.4°-is-"the-thinnest-margin"-claim correction (Phase-2 fix item 2)
and the 1.4°-gap-not-protected disclosure (fix item 3) both landed as
adopted — I re-verified both are present in `NOTES.md` §Idealizations 12
and the Result-section prose, matching the frozen fix docket. The
dual-section carried-idealizations banner (fix item 1) is present at both
Predictions and Result. Q4 correctly ships as a raw-number-only report,
not a labeled verdict (Idealization 13) — and, checked against §2 above,
that caution was well-placed: had Q4 been scored with its originally-
drafted (uncorrected) thresholds, it would have returned REFUTE at both
angles (the raw numbers track the smooth trend, not a recurring dip) —
correct as description, but for a different reason (ordinary continuation)
than "no periodicity-inheritance" per se would suggest, since this
cycle's data can't rule out that the *34.4° dip itself* is a one-off
excursion in an otherwise smoothly-varying differential rather than
evidence against inherited periodicity generally.

## Sharpest finding

**The ENERGY-DOMINANT reading at 40.2°/41.4° is a denominator-margin
(R13-class) failure riding an unremarkable numerator, not a numerator
(R14-class) hidden-feature failure — a materially different diagnosis
than either this cycle's own Phase-2 critiques (mine included) or
NOTES.md's descriptive Learned §2 explicitly states.** The pre-registered,
explicitly-distrusted naive linear interpolation of `frac_p_abs`
predicted both angles within 3–9% (§2 table) — the opposite of a missed
narrow spike — while `frac_contrast` at both points is the second- and
third-smallest value of any of the 8 now-measured angles, i.e.
genuinely R13-node-adjacent despite formally clearing the floor gate at
1.31×–1.48×. This reframes the Iteration-67 priority: the fix that
matters most is tightening or restructuring R13's `FLOOR_FRAC` itself
(already Tier 2 on this cycle's own board), not primarily a denser
numerator-side interior search — the interior-gap concern (mine, EM's)
was conceptually sound but did not turn out to be the load-bearing
mechanism.

## Ranked top-3 for the Iteration-67 queue

1. **Recompute R13's floor-margin distribution against actual `ratio_k`
   outcomes, not just theoretical adequacy.** This cycle supplies the
   first real data point: two of three points at 1.31×–1.48× FLOOR both
   misclassified; the two comfortably-clearing legacy points among the 8
   (36.0° at 3.88×, 38.4°/38.8° at 7.49×/8.02×, 41.8° at 6.59×) did not.
   A single logistic/threshold fit of `resolved-and-CONSISTENT` vs.
   `resolved-and-ENERGY-DOMINANT` against floor margin, using all 7
   resolved points now on record, is zero-FDTD and would give
   `FLOOR_FRAC` an actual empirical basis instead of the current
   house-style 0.10 guess — directly answering Q5's own open question
   with real (if thin, n=7) data rather than leaving it to a future
   cycle's judgment call.
2. **A targeted bracket at 40.2°/41.4° specifically** (NOTES.md's own
   Next item), but reframed by §2/§3 above: the diagnostic question is
   not "is this a narrow numerator spike" (already shown: no, the
   numerator tracked the smooth trend) but "does `frac_contrast`
   collapse further as θ approaches the true zero-crossings
   (40.265°/41.461°) more closely than this cycle's 0.14°/0.06° grid-
   neighbor choice did" — i.e., is `ratio_k`'s blow-up graded and
   denominator-driven (predicting a smooth further rise toward the exact
   crossing) or does it plateau (which would argue for some numerator
   contribution after all)? A 2–4 call bracket answers this directly.
3. **The still-queued formal null-controlled period fit against the raw
   signed difference `p_abs(G40,θ)−p_abs(C40,θ)`** (R14(b), Red Team's
   Iteration-65 Tier-2 item, still not run) — now with a concrete new
   motivating fact from §1: the sign-flip pattern across the 8-point set
   is irregular, not evenly spaced at anything resembling
   `delta_scene`'s own established period. A real fit (with R5/R10's
   look-elsewhere discipline) would settle whether this differential
   carries T28's established periodicity at all, or is closer to
   structured noise riding two smooth, nearly-parallel curves — directly
   resolving the open question my own §2 above leaves unclosed.
