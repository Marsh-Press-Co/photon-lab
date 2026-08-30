# PHASE 5 — REVIEW · PHOTONICS · Panel Iteration 70 · exp-093

*Blind, parallel review. No access to any other seat's Phase-5 output this
cycle.*

## 0. Independent re-derivation (R4 discipline)

Recomputed, from `results.json` primitives, not trusted from any printed
summary:

- `ratio_k(41.75°) = frac_p_abs/frac_contrast = 0.006877207633201729 /
  8.197538885033123e-05 = 83.89356524746684` — bit-exact match to the
  printed `83.8936`.
- `floor_pass` at all six item-1 interior points, recomputed against
  `FLOOR = RMS[frac_contrast]·FLOOR_FRAC = 1.917438e-3 × 0.10 =
  1.917438e-4`: 41.75°/41.775° → `frac_contrast` (8.20e-5/1.29e-4) below
  floor → `False`; 41.825°–41.9° → all above floor (1.96e-4 to 2.24e-4,
  clearing by as little as 2.1% at 41.825°) → `True`. Matches the printed
  4-of-6-clear count exactly.
- Item-4 dispersion ratios independently recomputed from the printed
  `observed`/`predicted_Dtheta` pairs: `0.320/0.003989=80.22×`,
  `0.377/0.003936=95.78×`, `0.194/0.006042=32.11×` — match the printed
  `80.2×/95.8×/32.1×` to stated precision.
- The item-3 sign flip at 42.0° independently confirmed from raw fields,
  not the `sign_match` boolean alone: `native_delta_scene=
  +8.041787e-05`, `sigma_corrected_delta_scene=-5.810166e-05` — a genuine
  sign reversal, not a rounding artifact of a near-zero ratio.

The headline **SINGLE-NULL** classification (four of six interior points
clear R13's floor gate, all classifying ENERGY-DOMINANT, `ratio_k`
20.5×–83.9×; all six interior points read `delta_scene≤0`) is arithmetically
sound and correctly derived under the pre-registered three-way rule.

## 1. Does SINGLE-NULL make more physical sense than a genuine two-node structure?

Yes, on priors, and this cycle's own item 3 result independently
reinforces rather than undermines that reading — for a reason not stated
in `NOTES.md` itself.

exp-092's two candidate crossings (`41.7811°`/`41.8377°`) sit only
`0.057°` apart — about 2% of T28's own established `~2.84°` carrier
period. A genuine, well-separated double zero-crossing from an
independent oscillatory contributor would be expected near half that
carrier's period (`~1.4°`) apart, the way T21's own fringe and T28's own
carrier are each internally spaced. A pair of crossings 35× closer
together than that would require an unexplained, much-higher-spatial-
frequency secondary component riding on the smooth carrier — and this
thread's own multi-cycle look-elsewhere discipline (R5, the exp-070 desk-
check batch, the exp-072/073/074 differential-fit program) has never
found evidence of any such short-period contributor at this system's
named length scales. By contrast, `delta_scene` is R14's own established
config-DIFFERENCE quantity (`C40_R3` vs `G40_R3`), and a near-total null
is exactly the generic signature of two comparable-magnitude, slowly-
θ-varying contributions passing through near-cancellation — a smooth
trough that dips close to zero, not a fast independent oscillator
crossing it twice. A trough sitting within `2×10⁻⁵`–`8×10⁻⁵` of zero
(this cycle's own native-sigma readings at 41.8°/42.0°, both already
below R13's floor) is a textbook near-degenerate local minimum, and such
minima are generically fragile to ANY small perturbation — grid
refinement (R15's own concern) or, as item 3 now independently
demonstrates, a purely numerical absorbing-boundary parameter (`sigma_max`)
that has no physical content at all. That a nuisance PML-type parameter
can flip the *sign* of the reading at 42.0° is the expected behavior of a
near-tangent trough, not evidence for a second genuine node — if anything
it is a second, independent line of evidence (distinct from R15's cpl
axis) for exactly the "single fragile near-null" picture SINGLE-NULL
reports, over the "two robust nodes" picture the original interpolation
implied.

**One clarification the record should carry but currently doesn't**: both
of exp-092's original candidate-crossing-defining points, `41.8°` and
`42.0°`, already failed R13's floor gate **at native sigma**, before item
3's sigma correction ever entered the picture (`item5` per-angle results,
this cycle: both `floor_pass=False`, `NODE-UNRESOLVABLE`, native
readings). The double-crossing was therefore always an interpolation
through two already-untrustworthy points, not a reading built on
floor-clearing data. Item 1's SINGLE-NULL verdict is the first time this
window has been measured with floor-clearing points at all (four of six
interior points), self-consistently at one sigma throughout — a
methodologically stronger basis than what it supersedes, independent of
which reading turns out to be right.

## 2. Internal inconsistency found (independent of any other seat)

`run.py`'s item-1 "combined curve" print (and the identical
`combined_curve_41_6_to_42_0` field persisted into `results.json`) is
captioned: *"41.6/41.8/42.0 are always native sigma_max=0.5."* This is
**false for this actual run**. Traced to source (`run.py:584-585`):

```python
combined_curve[41.8] = item5_report[41.8]["delta_scene"] if sigma_item1 == SIGMA_NATIVE else item3_report[41.8]["sigma_corrected_delta_scene"]
combined_curve[42.0] = item5_report[42.0]["delta_scene"] if sigma_item1 == SIGMA_NATIVE else item3_report[42.0]["sigma_corrected_delta_scene"]
```

Since item 3 fired REFUTE, `sigma_item1 = 1/3` (corrected), so both
branches actually took the **sigma-corrected** value. Confirmed directly
against `results.json`: `combined_curve_41_6_to_42_0["41.8"] =
-8.7906e-05` (matches `item3.per_theta["41.8"].sigma_corrected_delta_scene`
exactly, not `item5`'s native `-1.865e-05`); `["42.0"] = -5.8102e-05`
(matches the sigma-corrected value, not native `+8.042e-05`). The *code*
did the right thing; the *caption*, a static string not conditioned on
the branch actually taken, did not. Non-outcome-determining — item 1's
own PRIMARY three-way verdict is computed strictly from the six interior
points and never reads `combined_curve` — but this is exactly the
commensurability-labeling hazard R9 was adopted to catch, now surfacing
in a persisted `results.json` field with no accompanying flag, available
for a future cycle to build on without realizing which sigma condition it
actually reflects. Recommend correcting the caption (branch-conditioned,
as the trailing "directly comparable"/"NOT directly comparable" phrase
two lines later already correctly is) before this field is reused.

## 3. Process-completeness gap

`NOTES.md` (as committed) has no `## Result`, `## Learned`, or `## Next`
section at all — it ends at "T1 escape route." `results.json` and
`run_output.txt` are both complete and postdate `NOTES.md`'s own
timestamp, so this reads as an in-progress Phase-4→Phase-5 handoff gap,
not a missing run. Matches this sub-thread's own recurring pattern
(exp-080, exp-091, exp-092 all needed a same-shift Result-section
fix/hygiene catch at Phase 5) — naming it here for the Director to close,
per house convention, rather than silently working around it.

## 4. Verdict

**CONCUR-WITH-GAP(S).**

I concur with SINGLE-NULL as reported: correctly derived under its own
pre-registered rule, independently re-verified from primitives, and —
per §1 above — the more physically expected reading for a near-total-
cancellation feature in a slowly-varying config-differential channel,
now further (if circumstantially) supported by the sigma_max fragility
item 3 found at the adjacent already-floor-failing points. Item 3's
REFUTE and item 4's CONFIRM are both sound and correctly hedged. Gaps,
none outcome-determining for this cycle's own Combined Verdict, all
worth carrying forward: (a) Idealization 16's own disclosed limit — this
remains an angular-only finding at fixed `cpl=30`, not yet an R15-grade
cross-resolution result, and my own Phase-2 concern is not resolved by
this result, if anything it is sharpened by the sigma-sensitivity finding
that the near-null neighborhood is fragile to more than one kind of
numerical nuisance parameter; (b) the mislabeled "always native" caption
(§2); (c) the missing NOTES.md Result section (§3).

## 5. Ranked candidate directions for Iteration 71 (PHOTONICS)

1. **A `cpl=40` spatial-resolution spot-check at the interior near-null
   angles themselves** (e.g. 41.825°/41.875°, both comfortably
   floor-clearing this cycle) — the single cheapest, most decisive test
   of whether SINGLE-NULL is a genuine, resolution-stable feature or
   itself a `cpl=30`-specific discretization artifact, exactly the R15
   discharge condition Idealization 16 already names. This is the direct
   continuation of my own Phase-2 concern and the top-ranked item in
   exp-092's own reconciled queue that this cycle explicitly declined
   (Idealization 16) rather than closed.
2. **Map `sigma_max` sensitivity across the broader near-null
   neighborhood, not only 41.8°/42.0°** — item 3 found a purely numerical
   PML-type parameter can flip the sign of `delta_scene` at a point
   already failing R13's floor gate; before this program treats
   `sigma_max=1/3` as simply "the corrected, more-trustworthy" choice
   going forward, it needs the same kind of convergence characterization
   R15 now demands of `cpl` — is `delta_scene` near this null stable under
   a third `sigma_max` value, or does it remain a moving target the way
   the `cpl=20→30` crossings did? This is a genuinely new hazard this
   cycle surfaced, not yet named as its own standing concern.
3. **PHOTONICS' own long-standing grazing-incidence validity check** —
   still the single most-repeated undischarged item on the whole T28
   board (named at Iterations 64/65/67/68/69 and now 70). This cycle
   closed EM's parallel long-deferred dispersion-integral debt (item 4);
   my own charter's equivalent debt is now conspicuously the oldest
   unexecuted board item and directly bears on whether the analytic/FDTD
   boundary treatment this whole near-null discussion rests on stays
   valid at the angles in play.

*Honorable mention, not in my own top 3 but flagged per the task's own
framing*: the x-wall wavelength-generality leg (now eighteen consecutive
cycles deferred) is squarely PHOTONICS territory (wavelength dependence)
and the oldest debt on the board by cycle-count — but it is a broader,
more expensive re-validation than the three above, none of which it
would gate or be gated by; ranking it below three cheaper, more
directly-consequential-to-this-cycle's-own-open-question items is a
sequencing judgment, not a dismissal.
