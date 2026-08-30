# PHASE 5 — REVIEW · PHOTONICS · exp-092 · Panel Iteration 69

*Fresh context, blind to any other seat's current-cycle Phase-5 output.
Read in full: `PANEL.md`; `LOGBOOK.md` start to end (R1–R15 registry; the
full T28 live-thread arc; both CHECKPOINT entries; the T21/T24 "R3-overclaim
erratum" precedent, ~L17828-17858); the complete exp-092 record
(`phase1_proposal.md`, all five Phase-2 critiques including this seat's own,
`phase2_redteam_audit.md`, `phase3_synthesis.md`, `NOTES.md`, `run.py`,
`results.json`, `run_output.txt`); exp-091's full record as the immediately
preceding cycle. No FDTD run; no file modified except this one.*

## Verdict: **CONCUR-WITH-GAP**

The FDTD mechanics are clean — house gates all pass, the empty-leg
bit-exact reproduction independently confirms determinism, Rank 3's
sigma-rescale conclusion is physically coherent, and the lower-window
crossing (`40.0718°`) is a well-supported, independently-reproducible
result. The **gap** is specific and load-bearing: the write-up's own
Result/Learned sections assert the upper-window "double-crossing" is **"a
coherent, physically legible picture, not a numerical artifact"** (Learned
#3) using, as its only supporting evidence, two data points that fail this
program's own R13 floor gate and its own `resolved` flag — precisely the
condition R13 says must be *excluded from classification*, not read as
corroboration. This is the same overclaim shape this program has fired an
erratum on before (the T21/T24 "R3-overclaim critique," LOGBOOK
~L17834-17838: "overstated what a 2-of-31-angle, near-zero-crossing pass...
actually shows"). I recommend Learned #3 be corrected in place before
anything (e.g. an Iteration-70 caution-zone re-fit) treats the upper
crossing pair as a settled input.

## 1. Independent re-derivation of the two crossing locations (not trusted from prose)

Recomputed by hand from the raw `per_theta` `delta_scene` values in
`results.json`/`run_output.txt`, using the exact linear-interpolation rule
in `find_zero_crossings` (`t0 = t_i + (t_{i+1}-t_i)·|v_i|/(|v_i|+|v_{i+1}|)`):

- **Lower window**, 7 points, `39.2°→40.4°`: values run
  `-2.492e-3, -2.211e-3, -1.671e-3, -9.793e-4, -2.449e-4, +4.370e-4,
  +9.856e-4` — strictly monotonically increasing, sign changes exactly
  once, between 40.0° and 40.2°. My independent interpolation gives
  `40.0718°` — matches the filed value to 4 decimal places. **This is a
  clean, well-supported result**: one crossing, one monotonic curve, no
  ambiguity.
- **Upper window**, 4 points, `41.4°→42.0°`: values run `+5.626e-4,
  +1.784e-4, -1.865e-5, +8.042e-5` — **not** monotonic. My independent
  interpolation reproduces both filed crossings exactly: `41.7811°`
  (between 41.6°/41.8°) and `41.8377°` (between 41.8°/42.0°), `0.0566°`
  apart. Arithmetic confirmed, not in question.
- **Widening check.** cpl=20 lobe width `41.4609−40.2654 = 1.1955°`;
  cpl=30 width using the first upper crossing: `41.7811−40.0718 =
  1.7093°`, a **+43.0%** widening (using the second upper crossing instead:
  `+47.7%`). Both are in the same ballpark as the naive `~38%` estimate
  Phase 1 cited from a different, unrelated measurement (see §3).

## 2. The double-crossing's own supporting data fails this program's own reliability gates — verified, not assumed

Both `41.8°` and `42.0°` — the two points whose delta_scene *values*
generate the second crossing pair via linear interpolation — carry, in
`results.json::rank1.per_theta`:

| θ | `delta_scene` | `frac_contrast` | `floor_pass` | `resolved` | classification |
|---|---|---|---|---|---|
| 41.8 | `-1.865×10⁻⁵` | `3.517×10⁻⁵` | **False** | **False** | NODE-UNRESOLVABLE |
| 42.0 | `+8.042×10⁻⁵` | `1.533×10⁻⁴` | **False** | **False** | NODE-UNRESOLVABLE |

Both fail `frac_contrast ≥ FLOOR` (`1.917×10⁻⁴`) — the exact house floor
gate R13 established (LOGBOOK ~L410-469) specifically for angles near a
denominator/signal null, with the explicit rule: *"an angle failing this
gate is reported as its own outcome... **excluded from classification,
never silently scored alongside angles that cleared it**."* The write-up
follows this correctly for `ratio_k` classification (R1c labels both
NODE-UNRESOLVABLE, doesn't score them as CONSISTENT/DOMINANT). It does
**not** apply the same caution to the crossing-location use of the same two
numbers: the Result section states both interpolated angles to four
decimal places and Learned #3 declares the resulting picture "not a
numerical artifact," citing the very floor-gate failure as one of "three
independent signals... corroborating each other" — this inverts what the
floor gate means. Floor-gate failure is a *distrust* flag on a small
reading relative to a fixed empirical threshold; it does not corroborate
that a small reading is real. Near a genuine near-total destructive-
interference null, `delta_scene` is *also* exactly where subtractive-
cancellation and staircasing error are proportionally largest relative to
signal — the same species of hazard R14 names for a differently-shaped
construction (LOGBOOK ~L470-538). A same-order-of-magnitude sign flip
between two sub-floor points is equally consistent with **one deep,
under-resolved null whose true sign at this `cpl` is not reliably
determined** as with **two genuine adjacent nodes** — the two hypotheses
this cycle's own Next §item 2 says still need a denser off-grid check to
distinguish. **Learned #3 answers, with confidence, the exact question
Next #2 says is still open.** That is an internal inconsistency inside one
document, not merely a matter of emphasis.

## 3. The "widening lobe" framing is weaker corroboration than the prose implies

This seat's own Phase-2 critique already flagged that citing EM's
`2.8×–5.2×` `frac_contrast` amplitude inflation as support for a "widening
lobe" (a shape/width claim) was a non sequitur — amplitude rescaling and
zero-crossing location are independent under `f→kf`. The Result section
concedes this ("even though its amplitude-based corroboration was
independently ruled a non sequitur") but then still credits the picture as
"directionally confirmed" on the strength of two binary direction matches
(lower moved smaller, upper moved larger — each a 1-of-2 coin flip absent
a mechanism). Two independent correct-direction guesses is weak evidence
(`p=0.25` under a null of random direction) for a specific "widening lobe"
mechanism, and it is further undercut by what was actually found: the
upper region did not smoothly dilate — it grew genuinely new **interior
structure** (a sub-node) that the `cpl=20` census, at 0.2° resolution,
never showed at all. "Widening" and "new fine structure appearing" are
different physical pictures; Learned #2 partly concedes this for the R1a
verdict label but the "widening lobe... directionally confirmed" language
in R1b/Result carries forward the simpler, less-supported framing without
that same hedge.

## 4. Rank 3's optical-depth reasoning — checked, coherent

`τ_center(native) = 2·0.5·78 = 78` — deep into the saturated-absorption
regime (`τ≫1`). A shell that far into saturation is expected to show
strongly *sub-linear* sensitivity to a 33% conductivity cut, and that is
what was measured: `p_abs_w` ratio `0.961/0.962/0.960` at 37.2°/40.2°/41.4°
— a tight, angle-**independent** ~3.8–4.0% decrease. Angle-independence is
itself a good coherence check: a bulk conductivity change should move
absorption efficiency roughly uniformly across illumination angle for a
shell whose scattering geometry is unchanged, not produce angle-structured
variation — which is what was found. `ratio_abs_ext_raw` landing within
`0.54–0.93%` of the independently-established T9 `σ_abs/σ_ext≈0.51` anchor
(LOGBOOK ~L862-876, the extinction-paradox result) at all three angles is
a genuine, meaningful cross-check, correctly not over-claimed as proof the
PRIMARY channel is clean (R3's own six-cell CONFIRM does that separately).
**One unexplained, non-fatal wrinkle**: the `delta_scene` ratio's own
angle-dependence runs `37.2°→0.923`, `40.2°→1.014`, `41.4°→1.172` — the
*smallest* fractional change is at 37.2° (far from any null) as expected,
but the *largest* is at 41.4° (`~0.4°` from the nearest located null),
while 40.2° (`~0.13°` from the nearest located null, closer than 41.4° is
to its own nearest null) shows almost no change at all. If "closer to a
null ⇒ larger fractional sensitivity to a material perturbation" were the
operative story, this ordering is backwards. Not examined in the write-up;
worth a sentence, not a finding that changes the verdict — curve slope at
each null likely differs enough to explain it, but this wasn't checked.

## 5. Scale check against T28's own established periodicity

The 0.057° separation between the two upper crossings is **~2.0%** of
T28's own independently-established fringe period (`P*=2.8421°`,
`R²=0.6272` — a moderate, not tight, fit whose own physical origin
LOGBOOK repeatedly states "remains unidentified"). A genuine sub-structure
nested at 1/50th the scale of an already only-moderately-understood
periodic feature is not implausible for near-field diffraction, but it is
a materially finer physical scale than anything else this sub-thread has
reported, resting on a single sub-floor reading. That combination —
new spatial scale + single unresolved data point — is exactly the
configuration this program's own house discipline (R13/R15, and the
T21/T24 erratum precedent cited above) treats as needing an independent
resolution check before being written up as settled, not after.

## 6. What is solid and should not be re-litigated

- The lower-window crossing (`40.0718°`, `-0.194°` from the known
  `cpl=20` location) is real, independently reproduced here, and physically
  unremarkable: a `~6.8%`-of-period shift under `cpl` 20→30 refinement is a
  modest, plausible magnitude for a resolution-dependent phase-error-driven
  null relocation on this channel.
- Rank 3's CONFIRM (sigma_max does not contaminate the PRIMARY channel) is
  independently coherent on both the optical-depth argument (§4) and the
  T9-anchor cross-check, and closes exp-091's own single most consequential
  open question cleanly.
- The empty-leg bit-exact determinism check and the R1c floor-gate
  application to `ratio_k` classification are both done correctly.
- R2 (caution-zone desk rebuild) is outside this seat's charter; note only
  that its CONFIRM is a code-non-drift check (identical house functions
  re-run on identical frozen inputs), not new empirical evidence — correctly
  scoped as such, not a defect.

## Ranked top-3 candidate directions for Iteration 70 (PHOTONICS' own lens)

1. **Resolve the upper-window ambiguity before it becomes an input to
   anything else**: a small, cheap, off-grid or `cpl=40` spot-check
   densifying `41.6°–42.0°` (e.g. `41.7°, 41.75°, 41.8°, 41.85°, 41.9°`) to
   determine whether the true curve there is one deep near-total null or a
   genuine two-node feature. This is a direct, load-bearing test of §2/§5's
   finding above, cheaper than most of this program's own standing FDTD
   budgets, and should gate any future use of the upper crossing(s) as a
   caution-zone input — NOTES.md's own Next #2 already names this; I am
   elevating it above Next #1 (the caution-zone re-fit), which as currently
   scoped would build on the unresolved input.
2. **Re-fit R15's caution zone using only the confirmed lower crossing**,
   or, if both windows are used, report the caution-zone re-fit under both
   the single-null (`41.81°`) and two-node (`41.78°`/`41.84°`) hypotheses as
   a disclosed sensitivity check rather than picking one silently — converts
   NOTES.md's own Next #1 into a version that doesn't inherit §2's
   unresolved ambiguity.
3. **PHOTONICS' own long-queued grazing-incidence validity check** — still
   the single most-repeated deferred item on the whole T28 board (carried
   forward again this cycle, `phase1_proposal.md` §7, `NOTES.md` Next #4),
   and untouched by anything this cycle's own result changes. Overdue
   independent of this cycle's findings.

Also correct in place, at the next opportunity `NOTES.md` is touched: soften
Learned #3's "not a numerical artifact" to reflect that this remains an
open, disclosed hypothesis pending the check in Ranked-item-1 above — an
erratum-convention fix (original scored values untouched), matching this
program's own precedent for exactly this shape of overclaim.
