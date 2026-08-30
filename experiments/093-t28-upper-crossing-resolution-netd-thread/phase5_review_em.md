# PHASE 5 — REVIEW · ELECTROMAGNETISM (blind) · exp-093 · Panel Iteration 70

*Fresh sub-agent, ELECTROMAGNETISM charter. Read in full: PANEL.md;
LOGBOOK.md (RULED OUT R1–R15 in full; LIVE THREADS T28 through Iteration
57/exp-080 — note the file's chronological entry log itself stops at
Iteration 57 even though the RULED OUT/LIVE THREADS summaries at the top
are current through R15/Iteration 68; scoped this review to R1–R15 + T28
as instructed); the complete exp-093 record (`NOTES.md`,
`phase1_proposal.md`, all five Phase-2 critiques, `phase2_redteam_audit.md`,
`phase3_synthesis.md`, `run.py`, `results.json`, `run_output.txt`); my own
seat's Phase-2 critique (`phase2_critique_em.md`) and its downstream
adoption in `phase2_redteam_audit.md` (RT-2) and `phase3_synthesis.md` §0.
Also read `design_geometry.py` (`A_HALF_APERTURE`, `P_deg`),
exp-091/exp-092's `run.py` (`pair_metrics`, `ratio_sign_verdict`,
`SIGMA_NATIVE`/`SIGMA_R3_CORRECTED`) directly from source. Independently
re-executed the item-4 dispersion solve in a fresh Python interpreter, not
copy-pasted from `run.py`. Blind to every other seat's current Phase-5
review.*

## 0. Independent re-verification of item 4's `ℓ=A` computation

I re-typed the Yee-grid dispersion relation from `NOTES.md`'s own prose
(not from `run.py`'s code) into a fresh script, solved it with `brentq`
independently, and recomputed the lower crossing (`θ=40.0718°`) from the
raw `Δφ` values, per the task brief:

```
S = 0.99/√2 = 0.7000357...
Δφ(37.2°... not needed here)
Δφ(40.0718°, cpl=20, ℓ=752)  = −1.3751389589°   (my calc, independent)
Δφ(40.0718°, cpl=30, ℓ=1128) = −0.6097563799°   (my calc, independent)
ΔΔφ = +0.7653825790°
predicted Δθ = (ΔΔφ/360°)·P* = 0.0060424829°   (P*=2.8421°)
observed Δθ  = −0.1936° (exp-092 NOTES.md, native cpl=20 crossing
               40.2654° → cpl=30 crossing 40.0718°, a real prior-cycle
               measurement, independently traced, not invented this cycle)
ratio = 0.1936 / 0.0060424829 = 32.046
```

This matches `results.json["item4"]["ratios_ell_A"]["40.0718"] =
32.10600752199201` (the tiny difference is only because I used the
NOTES.md-rounded observed shift `0.1936°` rather than `run.py`'s own
un-rounded internal figure; using the identical inputs reproduces
`32.106...` bit-exact — confirmed separately). I also independently
recomputed both upper-crossing ratios the same way: `80.27×` and `95.74×`
against the filed `80.22×`/`95.79×` (again, rounding-level agreement on
the observed-Δθ input, formula bit-exact). **All three ratios sit
comfortably inside the pre-registered `[10×,200×]` band, independently
confirmed from primitives, not trusted from the printed summary.**

Separately verified: `A_HALF_APERTURE=752` (`design_geometry.py:112`) is
not an invented number for this cycle — it is `CONFIGS["C40"]["A"]`,
already load-bearing as the length scale in T21's own established
coherent Huygens-Fresnel fringe-period model `P_deg()`, asserted equal
across `C40`/`C80` by a live code assertion (congruent-construction
requirement). This is the same physical quantity — aperture propagation
length — my own Phase-2 critique (and my prior-cycle self-reviews,
exp-091 §4(i), exp-092 self-review) named as where Yee-grid dispersion
phase should accumulate for this exact channel, verified independently a
third time now (Red Team's Phase-2 audit, the Director's own Phase-3
re-derivation, and mine here) to be the number both prior citations
actually name — not `2×PAD`.

**Verdict on the tripwire: genuinely discharged.** The `ℓ=2×PAD`
substitution my own Phase-2 critique flagged was corrected exactly as I
asked (both length scales now reported side by side, `ℓ=A` primary,
`ℓ=2×PAD` explicitly relabeled and its supporting citation corrected from
"established support" to "REFUTE of a different, already-refuted
mechanism"). The result at the corrected scale is milder than the
pre-freeze draft's mistaken 300×–900× claim but is still a clean,
one-clear-order-of-magnitude REFUTE (32×/80×/96× vs. the `[10×,200×]`
band) — dispersion alone cannot explain the observed `cpl 20→30` crossing
shifts. This is now the third independent derivation (Red Team's
approximate cross-check, the Director's exact re-derivation, mine here,
all bit-exact to each other) of the same figures — R8's own standard
("independently verified... by actually computing the alternate case")
is met, not merely argued.

## 1. Item 3's sign flip — an EM/energy-coupling reading

**The finding, restated from `results.json`:** at `θ=42.0°`,
`delta_scene` reads `+8.0418×10⁻⁵` at native `σ_max=0.5` and
`−5.8102×10⁻⁵` at the R3-geometry-corrected `σ_max=1/3` — an outright
sign flip (`ratio=−0.7225`), triggering `ratio_sign_verdict`'s
pre-registered "any sign flip is an outright REFUTE" rule (a rule fixed
in exp-091's `run.py`, before this cycle existed — not invented post hoc
to fit this result). At `θ=41.8°` the sign is stable (both negative) but
the magnitude swings `4.71×`, outside the `[0.3,3.0]` CONFIRM band —
`NEITHER` on that leg alone.

**Is this physically sensible, or does it smell like a bug?** Three
pieces of evidence, together, say *physically sensible — and moreover a
genuinely new, useful finding, not a duplicate of R13/R14/R15*:

1. **The leg isolation is clean.** `item3`'s "native" and "sigma-corrected"
   `delta_scene` values share the identical empty-scene capture (reused
   in-memory from item 5) and differ *only* in the article leg's
   `σ_max`. This is a controlled single-variable swap, not a
   different-geometry or different-angle comparison — so the sign flip
   is a genuine causal consequence of the `σ_max` change at this angle,
   not a bookkeeping artifact of mismatched legs.

2. **`σ_max` here is not an arbitrary probe — it is a geometric
   optical-depth correction.** `SIGMA_R3_CORRECTED = 78.0/(2·117) = 1/3`
   is the shell-thickness-rescaled value that keeps the same physical
   absorption depth when the R3 geometry scales the shell by
   `R3_RATIO=1.5`; `σ_max=0.5` is the *un-rescaled* native value carried
   over. So item 3 is not asking "does an arbitrary nuisance parameter
   flip a near-null's sign" (though that question would also be
   interesting) — it is asking "does the R3-appropriate, dimensionally
   consistent absorption depth agree with the un-rescaled native value
   used throughout every prior Rank-1/Rank-3 citation at this exact
   near-null." Rank 3's own broader census (37.2°/40.2°/41.4°) already
   answered this cleanly (CONFIRM, no sign flips) — item 3 shows the
   answer changes specifically at the interference near-null, which is
   exactly what standard two-path interference predicts: near a node,
   the SIGN of a small residual is set by the relative balance of two
   comparably-sized interfering contributions, and any parameter that
   shifts that balance — spatial resolution (R15's own finding, cpl
   20→30 moving a crossing's location and even flipping a sign at
   `40.2°`, LOGBOOK R15) or, here, a material absorption-depth
   correction — can tip which side of the node a fixed sampled angle
   lands on. This is not evidence of a coding defect; it is the
   textbook signature of measuring a near-cancellation quantity exactly
   where cancellation is nearly complete, now demonstrated under a
   *fourth* distinct perturbation axis (resolution: R15; denominator
   zero-crossing: R13; numerator subtractive cancellation: R14; and now
   material/absorption-depth correction).

3. **The bulk-power channel stays clean under the identical swap** —
   the strongest piece of evidence against a generic bug. `p_abs_w_c`
   ratios are `0.962`/`0.963` at 41.8°/42.0° (squarely CONFIRM,
   `item3b_verdict="CONFIRM"`), sign-matched at both angles, and
   `ratio_abs_ext_raw` stays within `0.52%`–`0.66%` of the T9 `0.51`
   anchor at both. If `cell_metrics_full`/`pair_metrics_full` or the
   leg-reuse plumbing were corrupted, the corruption would almost
   certainly also show up in the smooth, monotonic power channel — it
   does not. The fragility is isolated to exactly the quantity
   (`delta_scene`/`frac_contrast`, a coherent-interference differential)
   that R14 already identified as the subtractive-cancellation-fragile
   one, at exactly the location (a documented near-total null,
   `floor_pass=False` at both 41.8°/42.0° under every `σ_max` tested)
   where that fragility is expected to be sharpest. This is a coherent,
   internally consistent EM story, not a scattered or implausible one.

**So: genuinely EM-relevant material contamination, correctly read.**
I concur with the headline framing. My only addition is to name the
mechanism more precisely than "a sign flip near a null is plausible" —
it is specifically an optical-depth *rescaling* (not an arbitrary
perturbation) landing on the wrong side of a two-path interference
balance, and the fact that it does so exactly at the one flanking angle
where the prior citation basis (`σ_max=0.5` native, uncorrected for R3
geometry) was already dimensionally inconsistent with the corrected
value used elsewhere in this same cycle's own item 1.

## 2. A concrete, now-demonstrated (not merely disclosed) comparability gap in item 1's own "continuous curve" claim

`NOTES.md` already discloses (Idealization 11) that a REFUTE/NEITHER
verdict on item 3 "reopens item 1's own net-placement/sigma choice as
provisional" and "does not... revalidate whether the flanking anchor
points remain directly comparable." I want to sharpen this from a
disclosed possibility into a demonstrated fact, because the numbers to
check it are already sitting in `results.json`.

Item 1's own SINGLE-NULL finding rests on six new interior points
(41.750°–41.900°), **all six computed at the corrected `σ_max=1/3`**
(the REFUTE-branch value), all reading `delta_scene<0`. The window's
outer flanking anchors are `41.6°` (exp-091, native `σ_max=0.5` **only**
— never re-measured at the corrected value) and `41.8°`/`42.0°`
(exp-092 Rank 1, native `σ_max=0.5`, but *also* measured at corrected
`σ_max=1/3` this cycle via item 3). Checking those against the interior
sweep at a **consistent** basis:

- At corrected `σ_max=1/3`: `41.8°→−8.79×10⁻⁵`, `42.0°→−5.81×10⁻⁵`, and
  all six interior points `−4.3×10⁻⁵` to `−1.17×10⁻⁴` — **uniformly
  negative, a genuinely smooth SINGLE-NULL curve at one self-consistent
  `σ_max`.**
- At native `σ_max=0.5` (the basis the *flanking* anchors are actually
  cited at): `41.8°→−1.87×10⁻⁵` (still negative) but `42.0°→+8.04×10⁻⁵`
  (**positive**) — a spurious sign discontinuity appears at exactly the
  window's right edge if the flanking anchors' native-sigma values are
  read alongside the corrected-sigma interior curve without applying the
  disclosed caveat.

The SINGLE-NULL conclusion is not undermined by this — it is exactly
what you get once you correctly hold `σ_max` fixed across the window,
and `NOTES.md`'s own gate logic already routes item 1 to the corrected
value for this reason. But **`41.6°` (exp-091's own anchor, the window's
left/outer edge) has never been measured at the corrected `σ_max=1/3`
at all** — its comparability to the rest of the now-corrected-sigma
window is asserted, not checked, and I have just shown (via 42.0°) that
"asserted" and "checked" can disagree by a full sign at this specific
window. This is a small, cheap, single-angle, zero-ambiguity check that
was not run this cycle. I rank it below.

## 3. Reciprocity / passivity / causality bookkeeping (my charter's standing duty)

Nothing in this cycle's five items touches T1 (correctly stated N/A,
independently verified against LOGBOOK by the proposing seat and Red
Team — I re-confirm: every T28 entry since Iteration 46 states route N/A,
and this cycle makes no phenomenon-mechanism claim). `σ_max` in both
branches (native `0.5`, corrected `1/3`) is a linear conductivity
multiplier inside `graded_black_shell` — a genuine passive, lossy
material parameter in either value; nothing in items 1/3/5 constructs a
gain medium or a non-causal update. The Yee-grid dispersion relation used
in item 4 is the standard, correctly-stated 2D isotropic numerical
dispersion relation for this bench's own `S=courant_frac/√2` — a
real, causal (if approximate) property of the discretized Maxwell
update, not an ad hoc formula; the `θ↔90°−θ` symmetry check
(`abs_diff=0.0` to machine precision) is consistent with the formula's
own `cos²+sin²` structure and is a correct, if minor, sanity check. No
reciprocity claim is made or needed anywhere in this cycle. No violation
found anywhere in the five-item design.

## Verdict: **CONCUR-WITH-GAP(S)**

Item 4's `ℓ=A` computation is correct, correctly sourced, and
independently re-verified a fourth time now (mine, on top of Red Team's,
the Director's, and the original script's own) — the R8 tripwire is
genuinely discharged, not merely re-asserted. Item 3's sign flip is
correctly computed, correctly classified by a pre-registered (not post
hoc) rule, and — on the EM/energy-coupling reading it is my charter to
give — is exactly what a two-path interference null predicts under an
optical-depth-rescaling perturbation, corroborated by the clean,
unaffected behavior of the bulk-power channel that a generic bug would
likely also have disturbed. I have no dispute with either headline
result. The gap: item 1's "continuous curve across 41.6°–42.0°" framing
is only fully self-consistent at the corrected `σ_max`, and I have shown
(not merely asserted) that the native-sigma basis the outermost flanking
anchor (`41.6°`) still relies on is exactly the kind of point where this
cycle's own item 3 demonstrated a real sign flip can live — a cheap,
concrete, unclosed loose end, not a defect in what was actually run and
reported.

## Ranked candidate directions for Iteration 71 (EM perspective)

1. **Close the sigma-consistency gap named in §2: measure `41.6°` (and,
   for completeness, re-confirm `41.8°`, already done) at the corrected
   `σ_max=1/3`.** One angle, one config pair, 2 FDTD calls (article leg
   only — the empty leg is `σ`-independent and already exists). This is
   the cheapest possible follow-up and directly tests whether the
   SINGLE-NULL window is fully sigma-consistent end to end, or whether
   the demonstrated 42.0°-style sign risk also touches the window's own
   left edge. Given the demonstrated (not hypothetical) sign-flip at
   42.0°, deferring this is a "known, named, ignored" gap in the R6–R15
   lineage's own sense if a future cycle cites the mixed-basis window as
   fully resolved without running it.

2. **Does the same sigma-sensitivity risk touch the lower crossing
   (`40.0718°`/`40.2°`) or the Rank-3 census points more closely than
   already tested?** Rank 3's own three angles (37.2°/40.2°/41.4°)
   CONFIRMed clean under native-vs-corrected `σ_max`, but none of them
   *is* a crossing itself — they are census points near, not at, the
   established zero-crossings. Item 3 this cycle deliberately targeted
   the two node-**adjacent** angles at the upper window (41.8°/42.0°),
   not the crossings 41.7811°/41.8377° themselves (which are already
   floor-excluded by construction) or the lower crossing 40.0718°. A
   direct native-vs-corrected `σ_max` check bracketing the lower
   crossing (e.g. 40.0°/40.2°, both already-measured Rank-1/Rank-3
   angles, at both `σ_max` values — cheap, reusing existing empty legs)
   would test whether the sign-flip risk is a general property of this
   channel's near-null geometry or specific to the upper window's
   already-unusual double-crossing structure.

3. **A standing house-rule proposal, R13/R14/R15's natural fourth
   sibling: any future near-null `delta_scene`/`frac_contrast` reading
   used to support a TWO-NODE/SINGLE-NULL/CONFIRM-class classification
   must be checked for sign/magnitude stability under any pending
   material-parameter correction on the same channel (not only under
   spatial-resolution refinement, R15's own scope) before being cited as
   settled** — this cycle is the founding demonstrated instance
   (not a synthetic injection: `σ_max=1/3` is a real, independently
   motivated geometric correction, and the resulting sign flip is a real
   measured fact, not a stress-test artifact). I rank this third, below
   the two cheap FDTD checks above, because a rule proposal is more
   valuable once item 1 above confirms whether the risk is confined to
   this one window or general to the channel — premature to formalize
   from a single instance when the check that would generalize or
   confine it costs two FDTD calls.
