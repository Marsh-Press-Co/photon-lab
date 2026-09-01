# Phase 5 Review — MATERIALS & METAMATERIALS (blind)

*Panel Iteration 75 (exp-098). Reviewing NOTES.md, results.json, run.py
against my own Phase-2 critique (`phase2_critique_materials.md`).*

## 1. Independent spot-verification

**(a) The Richardson-style ratio — reproduced, THEN independently
recomputed a different way, and the two disagree in a load-bearing way.**

From `results.json::richardson_diagnostic.B` directly (not NOTES.md's
prose): `shift_20_30 = -0.1935812644838535`, `shift_20_40 =
-0.34390028639148795`, `observed_ratio = 1.7765163757372424`,
`naive_order2_ratio = 0.5625`. I recomputed `observed_ratio =
shift_20_40/shift_20_30` by hand: matches to reported precision. So the
*arithmetic* NOTES.md reports is correct as far as it goes. But I then
checked what quantities are actually being divided, per
`richardson_style_diagnostic()` in `run.py` (lines 202–217) and its call
site (lines 403–406):

- `shift_20_30` = θ(cpl30) − θ(cpl20) — a **marginal** (single
  refinement-step) shift, filed at exp-092.
- `shift_20_40` = `item_i["B"]["crossing_cpl40"] − THETA0_B` = θ(cpl40) −
  θ(cpl20) — a **cumulative** (two refinement-step) shift, spanning
  cpl20→cpl30→cpl40 in one hop.

These are not the same kind of quantity, and `naive_order2_ratio =
(h40/h20)²/(h30/h20)² = (h40/h30)² = 0.5625` is algebraically just
`(h40/h30)²` — i.e., it is the naive 2nd-order prediction for a
**marginal-to-marginal** ratio (h30→h40 step vs. h20→h30 step), not for a
cumulative-over-marginal ratio. Comparing a two-step cumulative shift to
a one-step marginal naive prediction is a category mismatch.

I recomputed the quantity my own Phase-2 Flip actually asked for
("pairwise shift ratio, cpl20→30 shift ÷ cpl30→40 shift" — i.e., marginal
÷ marginal). Since exp-092 gives θ(cpl30) directly via `shift_20_30`, and
this cycle gives θ(cpl40) directly:

```
theta(cpl30)_B = THETA0_B + shift_20_30       = 40.071838338...
shift_30_40    = crossing_cpl40_B - theta(cpl30)_B = -0.150319022...
ratio_marginal = shift_30_40 / shift_20_30    = 0.7765163757...
```

(Note the clean algebraic identity `observed_ratio = 1 + ratio_marginal`
— confirms both numbers are internally consistent, just measuring
different things.) **0.7765 vs. the naive-2nd-order 0.5625 is a 1.38×
gap and is still shrinking (ratio < 1, same direction as expected for a
damping sequence).** That is a categorically different, far less
alarming finding than "growing faster than 2nd-order, not shrinking
toward it" (the 1.777 vs. 0.5625 comparison NOTES.md reports, a 3.16×
gap, apparently growing). **Verdict: the reported comparison is
internally correct arithmetic, but it compares the wrong pair of
quantities, and the mis-paired comparison materially overstates how
anomalous Null B's behavior is.**

**(b) Item (i) crossing values — spot-checked against `results.json`
directly, not the NOTES.md table.** `item_i.A.crossing_cpl40 =
36.77035821175119`, `item_i.B.crossing_cpl40 = 39.921519316666235`,
`item_i.C.crossing_cpl40 = None` (verdict `NO-SIGN-CHANGE`). Matches
NOTES.md's `≈36.770358°` / `≈39.921519°` / "—" to displayed precision.
`item_i_family_verdict = "MIXED"` confirmed directly.

**(c) GP2′ peak/flagged-band claim.** Scanned `item_v.gp2_curve` (120
points) directly rather than trusting the prose: max `ratio_to_ref` is
**235.39611912782016 at θ=66.0°**, classification `MARGINAL` — matches
NOTES.md's "235.4×, at θ=66.0°" exactly. `gp2_marginal_thetas` spans
50.5°–89.5° (70 points), `gp2_invalid_thetas` is empty — matches "MARGINAL
… θ=50.5°–89.5°… zero INVALID." This one checks out cleanly.

**(d) `CPL` really is grid density only.** Confirmed at
`experiments/069-t21-block-mini-period-match-power-up/design_geometry.py`:
`R3_CPL={600:30}`, `R4_CPL={600:40}`, `R5_CPL={600:50}` — three dicts
keyed by wavelength to a cells-per-λ integer, no geometry parameter in
sight. Consistent with my Phase-2 finding and NOTES.md/run.py's repeated
assertion that `L_GEOMETRIC_M_R{4,5}` is invariant to 1e-12 across
families.

## 2. Steel-man

This cycle did engage my Phase-2 attack rather than waving it off: it
explicitly declined to call (i)/(ii)'s outcome a clean "migration"
finding, restated Idealization 17 and my own dichotomy point at both
Predictions and Result, added the diagnostic at zero marginal FDTD cost
using only already-filed numbers, and flagged its own surprising
direction as "unresolved" rather than quietly filing it as a footnote.
The item (i) MIXED design (4-point quartile brackets, finer than the
largest known shift) is honest about its own scope limits (Idealization
46), and item (ii)'s wider, lower-θ-weighted bracket recovering a
crossing exp-095's narrower bracket missed is a genuine, well-earned
methodological win — R17 working as designed one cycle after its own
founding defect. None of that is undermined by what follows.

## 3. Sharpest finding

**The Richardson-style diagnostic does not do what my Phase-2 critique
asked for — it implements a different, mismatched quantity, and the
mismatch is exactly what manufactures the "growing faster than 2nd-order"
alarm.** My Flip asked for `(cpl20→30 shift) ÷ (cpl30→40 shift)` — a
ratio between two *single, consecutive* refinement steps, which is the
only pairing a naive-order sanity check is meaningfully entitled to
predict a clean power-law ratio for. `run.py`'s
`richardson_style_diagnostic()` instead divides the *cumulative*
cpl20→cpl40 shift by the *marginal* cpl20→cpl30 shift, then compares
that to a `naive_order2_ratio` formula that is algebraically `(h40/h30)²`
— i.e., built for the marginal/marginal comparison the code never
actually performs. The data needed to do it correctly was already sitting
in the very inputs the function receives (`shift_20_30` from exp-092
directly gives θ(cpl30); the marginal step is one subtraction away), so
this is a bug in the diagnostic's construction, not a limitation of what
data exists.

Recomputing the *correctly paired* marginal-to-marginal ratio myself
(§1a): **0.777, not 1.777** — still shrinking, only ~38% off the naive
2nd-order prediction rather than ~3.16× off and reversed in direction.
"Growing faster than 2nd-order convergence would predict, not shrinking
toward it" is not an honest characterization of what the underlying
numbers show once the diagnostic is computed the way it should have
been; if anything, the corrected number is *mildly reassuring* about
convergence at Null B, not alarming.

**This changes the register of the "flagged, not resolved" framing.**
NOTES.md treats the open question as "one data point can't settle
convergence order" — true, but beside the point raised here: the *single*
data point it does have is itself computed with a category error, so
even the descriptive, non-formal claim it makes about that one point
("growing, not shrinking") is not reliably established by the numbers
cited. That is a stronger and more specific problem than "n=1 is thin
evidence" — it means the panel's current belief about Null B's
convergence behavior (as stated in Learned #3, "the Richardson-style
diagnostic's own surprising direction… makes this MORE open, not less")
is resting on a miscomputed ratio, and should not be propagated into
Iteration-76 framing as-is. **Every future reference to "Null B is
growing faster than 2nd-order" should be corrected or re-derived before
it accrues more weight in the log.**

**On item (i)'s MIXED result and realizability — orthogonal, and this
cycle's own text half-concedes it without saying so plainly.** `cpl` is
confirmed (again, independently, at source) to be exclusively a
cells-per-wavelength mesh-density parameter; the physical geometry is
identical bit-for-bit across R3/R4/R5. A fabricated device has no
"cpl" — it has one continuum geometry and (for this feature) one true
null angle. Whether a given null's FDTD-computed location moves, holds
still, or vanishes into the noise floor as mesh density increases from
20→30→40 cells/λ is a statement about **the numerical scheme's
convergence behavior for that particular scattering feature**, full
stop — it carries **zero realizability content** on its own, in either
direction of outcome. NOTES.md's own framing gestures at this
(Idealization 17, restated Hypothesis-1 language) but still lets the
item (i)/(ii) headline ("MIXED," "CONFIRM-migration-down") read as if it
were adjudicating something about the *physical* null, when what's
actually been adjudicated is only where the *discretized* null sits at
three mesh densities. The one channel through which this line of work
COULD eventually earn realizability content is precisely the thing the
diagnostic is supposed to supply and currently doesn't reliably supply:
a genuine extrapolated continuum-limit estimate, which is the number "a
realizability bound would need" (my own Phase-2 Flip's closing line).
Until that diagnostic is fixed and has ≥3 clean, correctly-paired
resolution points at one feature, this entire sub-thread — MIXED result
included — has produced zero data usable by a realizability bound. Worth
stating plainly rather than soft-pedaled, exactly as the task asks: **not
"this bears indirectly on realizability," but "this bears on
realizability only through a diagnostic that is currently broken and
under-populated."**

Separately, the standing process point from my own Phase-2 verdict is
still true and still not addressed: this is now the **sixth**
consecutive Panel Iteration (71–75 plus this one, exp-094 through
exp-098) with the T1 realizability route N/A and zero new FDTD evidence
bearing on any realizability parameter (the Iteration-7 UNOBTAINIUM
shell-thickness figure, 0.31–0.92 m at witness scale, remains untouched).
Not a defect in this cycle's own scope (correctly a T28 house-discipline
cycle, not a T1 cycle) — but the run continues, and nothing in this
cycle's Next-queue proposes closing it.

## 4. Verdict

**CONCUR-WITH-GAP(S).**

I do not dispute item (i)'s MIXED finding, item (ii)'s recovered
crossing, or GP1–GP3's results — all independently spot-checked and
correct in `results.json`. My concurrence is qualified because:

- Gap 1 (material): the Richardson-style diagnostic's `observed_ratio`
  divides a cumulative two-step shift by a marginal one-step shift and
  compares the result to a naive prediction built for a marginal/marginal
  pairing — a construction bug, not just thin data, and it manufactures
  the "growing faster than 2nd-order" characterization that Learned #3
  and the Iteration-76 queue both lean on.
- Gap 2 (framing): NOTES.md's "flagged, not resolved" undersells the
  above — the issue isn't only n=1, it's that the n=1 point itself is
  currently miscomputed.
- Gap 3 (scope honesty): item (i)/(ii)'s realizability content is exactly
  zero as constituted (cpl is mesh density, not a fabrication parameter);
  this should be stated as plainly as I've stated it here rather than
  left implicit in the Idealization-17 restatement.

None of these gaps invalidate this cycle's real, hard-won results (item
(ii)'s bracket-sizing win, item (v)'s genuinely θ-dependent grazing
instrument); they narrow what those results are entitled to claim.

## 5. Ranked top-3 candidate next directions

1. **Fix `richardson_style_diagnostic()` to compute the marginal-to-marginal
   ratio my Phase-2 Flip actually specified** (`shift_30_40 =
   crossing_cpl40 − theta(cpl30)`, where `theta(cpl30) = THETA0 +
   shift_20_30`; ratio = `shift_20_30 / shift_30_40` or its inverse,
   documented either way), re-run it against the existing Null B data
   (zero new FDTD calls — this is a pure recomputation), and correct the
   Learned/Next-queue language that currently cites the miscomputed 1.777
   figure. This is strictly cheaper than Iteration-76's own queued item 2
   (the cpl=50/R5 third point) and should happen *before* that point is
   added, not after — right now a third resolution point would be fed
   into a diagnostic function I've just shown is wired wrong.
2. **The already-queued cpl=50/R5 third resolution point at Null B**
   (Iteration-76 queue item 2), but gated on item 1 above landing first,
   and extended: with 3 resolution points (20/30/40/50) and a corrected
   marginal-ratio formula, this is the first cycle that could compute an
   actual (still rough, still non-formal per Idealization 49, but at
   least correctly-paired) local convergence-order estimate for one
   feature — the closest this sub-thread has come to a number a
   realizability bound could use.
3. **State the cpl-is-orthogonal-to-realizability finding explicitly in
   a future NOTES.md Result section** (not just implicit in Idealization
   17), and revisit the standing T1-route-N/A governance flag (six
   consecutive cycles now) at the next Phase 3 checkpoint — not to force
   a T1 proposal this cycle, but because the flag has now outlived its
   originally-cited precedent count without any seat re-raising it in a
   Result section rather than a Phase-2 aside.
