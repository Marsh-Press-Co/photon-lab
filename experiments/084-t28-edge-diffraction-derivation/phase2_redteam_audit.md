# PHASE 2 — RED TEAM FINAL AUDIT · Panel Iteration 61 · exp-084

*Seat: RED TEAM. Reads the proposal, `phase1_derivation.py`/`phase1_output.txt`/
`derivation_results.json`, and all five blind Phase-2 critiques
(materials/em/thermodynamics/quantum/vision). Every load-bearing number below
was independently recomputed from committed files, not copied from the five
critiques' prose — code and results shown inline where it matters. T1 escape
route is **N/A** this cycle, matching the proposal's own framing and every
T28 desk cycle since exp-069: this is instrument-fidelity work internal to
the bench, not a phenomenon-constraint mechanism. Accordingly most attacks
below carry **no constraint tag** — stated explicitly per the assignment,
not forced.*

## 0. Housekeeping, independently reconfirmed

- No data leakage: `grep -n "070" phase1_derivation.py` returns **zero
  hits**. The file's only external reads are `dg048`, `dg065`, `run69`
  (`_free_period_search`/`_fixed_period_fit`, the *function objects*,
  imported verbatim), `ywp` (`free_period_with_widening`), and
  `experiments/083-.../results.json` (the four reference periods, R4). No
  path to `experiments/070-.../results.json` exists anywhere in this file's
  import graph.
- Anchor 1, Anchor 2, and the R5 specificity fractions (5/60, 0/60) all
  reproduce bit-for-bit from an independent re-implementation (below).

## 1. Numbered attacks

1. **[inconsistency]** Leg (a)'s "FINAL VERDICT: SUPPORT" was certified
   against the wrong control. The file runs an R5 *specificity-over-targets*
   sweep (holding the fitted curve fixed, varying the target) and treats
   that as sufficient, but this program's own established "harder
   companion" — an order-preserving circular-shift null-under-noise test,
   R6/R7's own family, used to reverse exp-083's two-tone claim one cycle
   ago (Iteration 60) — was never run on leg (a) despite the identical
   tooling (`free_period_with_widening`) being already in this exact file.
   Independently rebuilt below: it reverses the verdict. This is not a new
   failure mode; it is the *same* pattern LOGBOOK already named and fixed
   once this program-cycle ago, recurring one cycle later in a new
   instrument.
2. **[inconsistency — fires Checkpoint criterion 4]** The joint EM/THERMO
   energy-interception cross-check is now a **third consecutive cycle**
   (exp-082 → exp-083 → exp-084) without either being run or being
   explicitly deferred with a stated reason. Iteration 60's own close
   pre-committed: *"a third consecutive deferral without an explicit reason
   would fire it [Checkpoint criterion 4]."* THERMODYNAMICS' blind Phase-2
   critique independently confirms zero occurrences of "Poynting,"
   "interception," or "cross-check" anywhere in `phase1_proposal.md` — not
   deferred-with-reason, simply absent. Per the program's own explicit,
   already-written precommitment, this fires automatically; it is not a
   judgment call this audit is making fresh.
3. **[no constraint tag — causal-attribution risk]** EM's independently-
   verified finding (confirmed below, bit-for-bit) that
   `c_twostage(R_OUT=0)/c_direct` is not a smooth θ-dependent scalar (range
   1.47–5.66 away from zero-crossings; up to ~25× *at* zero-crossings) is
   real. But the write-up's own causal language ("most likely a missing
   Rayleigh–Sommerfeld-style boundary treatment") should not enter LOGBOOK
   as settled: EM named a cheaper, sharper, already-precedented alternative
   (a missing obliquity/90°-phase-rotating factor from feeding a bare field
   into `propagate()` in place of a properly weighted secondary source —
   the same convention-bug species VALIDATION.md documents recurring four
   times already) that was never tested against the RS-term hypothesis.
   Adopting one specific causal diagnosis without running the cheaper
   discriminating test is the same shape of error R4/R8 exist to prevent
   (an untested argument, however plausible, filed as if verified).
4. **[no constraint tag]** Leg (b)'s reported `ptp_b = 8.21×10⁻²` is ~41×
   the bench's own ESTABLISHED `graded_black_shell` reflectance ceiling
   (`R≤0.2%`, `0.10%` @600nm) — independently confirmed
   (`0.0821/0.002 ≈ 41`). THERMODYNAMICS is right that this comparison is
   entirely absent from the file. It does not change leg (b)'s
   already-correct WITHHELD status (Anchor 2 already disqualifies it), but
   it is independent evidence *for* the file's own diagnosis that the
   opaque-mask construction is not measuring a real partial reflection off
   the actual lossy absorber (which could not produce an amplitude this
   large) — this should be stated explicitly, not left as an implicit
   consequence of Anchor 2 alone.
5. **[no constraint tag — credit, not an attack]** The five-critique record
   does not surface the one finding that actually resolves item 1's
   question of *why* the coincidence happens: leg (a)'s synthetic curve and
   the real `C80(θ)` curve are genuinely, distinctively correlated in raw
   shape (`r=0.958`, independently computed below) — far above any control
   curve tested (leg (b)'s own output: `r=-0.10`; a bare linear ramp:
   `r=-0.33`; a bare quadratic: `r=-0.55`, all sampled at the identical
   31-point grid). This is real signal, not an artifact of "any smooth
   curve correlates with any other smooth curve" — logged here because it
   is a stronger, more direct, and more defensible piece of evidence for
   the underlying mechanism than the period-match that Phase 3 should not
   discard along with the period-match's own downgrade (item 1).

## 2. The three assigned load-bearing claims — independently verified

### 2.1 VISION's bit-identical-coincidence claim

**Verdict: CONFIRMED bit-identical; NOT a data-leakage bug; genuine
shape-correlation explanation, independently found and quantified.**

`derivation_results.json`'s `leg_a.p_model_deg = 2.533834586466165`. Grepped
`experiments/070-.../results.json` programmatically (not by eye) for every
float beginning `2.53`: exactly one hit,
`p_070_1_per_config.cells.C80.p_star_free = 2.533834586466165` — identical
to full float precision (`==` in Python, not merely close).

**Ruled out data leakage**: confirmed at §0 above — zero references to
exp-070 anywhere in `phase1_derivation.py`'s source or import graph.

**Mechanism, independently derived** (not merely re-argued): both numbers
are the output of the *literal same function object*
(`run69._free_period_search`, imported verbatim by both exp-070's
`design_geometry.py` and exp-084's `phase1_derivation.py`) applied to two
structurally different signals sampled on the identical 31-point θ grid
(36.0°–42.0°, 0.2° step). Landing on the same one of 400 discrete candidate
periods is not generic: I ran the identical search on a battery of other
smooth curves at the same grid (linear ramp, quadratic, three pure sines,
a smoothed-noise curve, white noise, a step function, a permutation of the
real C80 curve, and a lightly-noised copy of the real C80 curve) — **none**
of them land on 2.533834586466165; the noised-C80 copy alone moves to a
different grid point (2.4662°). What *does* explain the coincidence:
`corr(leg_a_curve, C80_real) = 0.9581856926779434` — a genuinely high,
distinctive shape correlation, confirmed not to be a generic artifact of
"two smooth curves over a narrow window" (leg (b)'s own output correlates
`-0.10` with the same real curve; a bare linear ramp correlates `-0.33`; a
bare quadratic correlates `-0.55`). **The coincidence is a profound clue,
not a bug**: a zero-FDTD, vacuum-only, boundary-free Huygens integral over
the source aperture's own two tapered edges reproduces ~92% of the real
FDTD curve's variance in raw shape. That is real, substantive, independent
corroboration of the underlying diffraction physics.

**But** — running VISION's own named decisive test, exactly as VISION
pre-registered it: `R²_fixed(leg_a_curve, T_SINTHETA_600) = 0.27096`
(independently computed against `run69._fixed_period_fit`), compared to
`R²_fixed(C80_real, T_SINTHETA_600) = 0.26453` (reproduces exp-070's own
committed `0.2645317405627635` exactly). These are comparable — **0.271 vs
0.265, a 2.4% relative difference** — not "near-zero" as VISION's own
pre-registered escape clause required for unqualified SUPPORT. Per VISION's
own stated rule: *"If it reproduces a comparable R²_fixed, SUPPORT should
downgrade to INCONCLUSIVE, matching exp-070's own 'compromise fit'
characterization of this identical number."* **This is exactly what
happened.** VISION's own critique, run to its own conclusion, independently
mandates the downgrade — a second, independent line of evidence for §2.2's
verdict below, arrived at by a completely different route.

### 2.2 QUANTUM's circular-shift null-test claim

**Verdict: reproduced closely (my number is if anything slightly worse for
leg (a) than QUANTUM's) — CONFIRMED, leg (a)'s R² is NOT significant under
this program's own established harder-companion null.**

Rebuilt from scratch (own re-implementation of `_fixed_period_fit`,
`_free_period_search`, and `free_period_with_widening`, not QUANTUM's code),
using the real committed `leg_a.curve` array from `derivation_results.json`
and the *actual* fitting machinery `phase1_derivation.py` calls
(`free_period_with_widening` — the full three-stage `[1,4]→[1,15]→[1,60]`
widening idiom, not just the fixed `[1,4]` window). First confirmed my
re-implementation reproduces the committed result exactly:
`P*=2.533834586466165°, R²=0.36965580905914364`, settled at
`narrow[1,4]` (interior optimum) — matches to full precision.

Then ran all 30 nontrivial circular shifts of the real 31-point `c_a`
array through the **identical full pipeline**:

```
n_meet_or_exceed(R² ≥ 0.36965580905914364) = 15/30 = 50.0%
mean shift R² = 0.4594   max = 0.7302   min = 0.2892
```

Using QUANTUM's own narrower methodology instead (fixed `[1,4]°` window
only, no staged widening — matching QUANTUM's own stated method) reproduces
QUANTUM's exact figure: **14/30 = 46.7%**, bit-for-bit.

Both numbers tell the same story and neither is close to a rejection tail:
the observed `R²=0.3697` sits at roughly the **median** of its own
circular-shift null distribution. Using the *actual* production pipeline
(full staged widening — several shifts land "at boundary" in `[1,4]` and
widen to `[1,15]`, where an even better fit is available, since a
longer-period sinusoid has more freedom to track 31 points spanning only
6°) gives an even less favorable reading (50.0% vs QUANTUM's 46.7%) — this
audit's own number is the more conservative (i.e. more damaging) of the
two, not a softened restatement. **QUANTUM's claim holds up and, run
against the literal production code, is slightly understated.**

### 2.3 EM's Anchor-2 ratio non-smoothness claim

**Verdict: CONFIRMED, essentially exactly.**

Re-imported `phase1_derivation.py` as a module (without triggering
`main()`) and called `leg_a_curve()` / `leg_b_curve(mask_r_out=0)` directly
across all 31 angles:

```
θ=36.0° ratio=+2.48   θ=36.8° ratio=+3.15   θ=37.4° ratio=+2.51   θ=37.6° ratio=+1.47
θ=38.0° ratio=+5.28   θ=38.4° ratio=+5.66   θ=38.6° ratio=+1.64   θ=39.0° ratio=+2.90
```

This reproduces EM's cited spot values (`2.48→3.15→2.51→1.47`,
`5.28→5.66→1.64→2.90`) exactly. Away from the two angles nearest a
zero-crossing of `c_a` (36.6°, 37.8°, where the ratio blows up to 12.7× and
25.5× respectively — division by a near-zero denominator, correctly
excluded by EM from the headline range), the well-behaved range is
`[1.4656, 5.6650]`, matching EM's cited `1.47–5.66` to the stated
precision. This is not a smooth θ-dependent scalar (a genuine missing
`cosθ`-type real correction would rescale amplitude and preserve `c_a`'s
own zero-crossing locations and shape; this doesn't) — EM's reading is
correct, independently reproduced from the file's own functions, no
adjustment needed.

## 3. Other items — independently assessed, not merely adopted

- **THERMODYNAMICS' energy-ceiling point**: see attack 4 above — the raw
  `ptp_b` vs. `R≤0.2%` comparison independently confirmed (~41×). Correct
  and should be added as a mandatory Anchor 3, exactly as THERMODYNAMICS'
  named parameter-change proposes, once leg (b)'s kernel is fixed. The
  twice-deferred-now-third-deferred cross-check itself is escalated at
  attack 2 above, above the level THERMODYNAMICS' own critique put it at
  (THERMODYNAMICS logged it as "the third consecutive cycle... undischarged"
  but did not invoke Iteration 60's own pre-committed Checkpoint-4 firing
  language by name — this audit does).
- **MATERIALS' zero-realizability-content point**: correct, adopted as-is.
  Even a fully-vindicated leg (a) SUPPORT would show only that the
  empty-scene *source geometry* (vacuum, no material) is congruent with
  `P_edge_A` — nothing here bears on realizability either way, consistent
  with the proposal's own Sec 6 framing and MATERIALS' standing Iteration-59
  rule. Nothing to add.
- **The R5-specificity-vs-null-test distinction QUANTUM raised**: confirmed
  as a real, structural, non-cosmetic gap, not merely a stylistic
  preference between two similar controls. The two tests disagree sharply
  in this exact case (R5 specificity-over-targets: `8.3%` clear, reads as
  tight/specific; circular-shift null-under-noise: `46.7–50.0%` meet or
  exceed, reads as thoroughly unremarkable) — precisely the same divergence
  shape that reversed exp-083's two-tone claim one cycle ago. **This is now
  the second time in two consecutive cycles this exact divergence has been
  outcome-determining for a T28 verdict.** Recommend the Director consider
  whether this warrants promotion to a standing house rule (an "R5
  addendum" or new numbered rule, in the R6/R7/R8/R9 lineage): any
  single-curve free-period-fit SUPPORT verdict must clear an
  order-preserving null-under-noise test (circular-shift or equivalent)
  before it is reported, not merely a specificity-over-candidate-targets
  sweep — the two are not substitutes, exactly as R7 already established
  conditioning-numbers are not substitutes for a fit-and-calibrate step.

## 4. Ruling: **PROCEED-WITH-MANDATORY-FIXES**

Not HALT: nothing here is unfalsifiable, internally self-contradictory
beyond correction, or inexpressible as simulation parameters — the
methodology (two self-built anchors, one caught failing and honestly
withheld; an R5 control; R4 sourcing discipline) is genuinely some of the
more careful work this sub-thread has produced, and this audit's own
investigation surfaced a real new positive finding (§1 item 5, §2.1) worth
keeping. Not plain PROCEED: the headline verdict is wrong as filed and a
pre-committed Checkpoint trigger fires. Fix docket (6 items):

1. **Downgrade leg (a)'s FINAL VERDICT from SUPPORT to INCONCLUSIVE.** Two
   independent lines of evidence both mandate this — this audit's own
   circular-shift null (§2.2: 46.7–50.0% of the null distribution meets or
   exceeds the observed R²) and VISION's own pre-registered T21-decorrelation
   test run to its actual conclusion (§2.1: `R²_fixed=0.271` vs. `0.265` for
   the real curve — "comparable," triggering VISION's own downgrade clause).
   This exactly matches Iteration 60/exp-083's own precedent: do not soften
   it in Phase 3 prose.
2. **Log Checkpoint criterion 4 as FIRING** in the LOGBOOK entry for this
   cycle, per Iteration 60's own explicit precommitment (third consecutive
   silent deferral of the joint EM/THERMO energy-interception cross-check,
   confirmed zero mentions in `phase1_proposal.md`). Either run a minimal
   version of the check now, before Phase 3 closes, or state an explicit,
   substantive reason for deferring again — silence a fourth time is not an
   option this rule permits.
3. **Do not adopt "missing Rayleigh–Sommerfeld boundary term" as settled
   cause** for leg (b)'s Anchor-2 failure in LOGBOOK. Run EM's named,
   cheaper discriminating test (re-weight leg (b)'s stage-2 secondary
   sources by the same obliquity/phase convention `field_and_h` already
   uses for a driven current) before crediting either causal story.
4. **Add THERMODYNAMICS' Anchor 3** (fringe-amplitude vs. the
   `graded_black_shell`'s established `R≤0.2%` ceiling) as mandatory before
   any future leg (b) re-attempt is scored — log this cycle's own `~41×`
   finding (attack 4) as the reason it is needed, not merely a nice-to-have.
5. **Log the shape-correlation finding (§1 item 5 / §2.1) explicitly and
   separately from the period-match downgrade.** `corr(leg_a, C80_real) =
   0.958`, control-tested against three unrelated curves (all `|r|<0.35`,
   one of them this same file's own leg (b) output at `r=-0.10`), is a
   genuine, independently-verified positive result for the source-aperture
   diffraction mechanism that survives item 1's downgrade — Phase 3 should
   not let the period-match correction erase this.
6. **Flag the R5-specificity-vs-null-test divergence (§3, last bullet) for
   Director/next-lead consideration** as a candidate standing rule,
   parallel to R6/R7/R8/R9 — two consecutive cycles now where this exact
   distinction was outcome-determining.

## 5. Explicit recommendation for Phase 3 on leg (a)'s verdict

**Do not let leg (a) stand as SUPPORT.** My own from-scratch circular-shift
null test, run against the literal production fitting pipeline
(`free_period_with_widening`) on the real committed `leg_a.curve` array,
shows `R²=0.3697` is met or exceeded by **50.0%** of the 30 possible
order-preserving circular shifts of that exact curve (46.7% using QUANTUM's
narrower fixed-window method — the two agree on the substance, not just the
ballpark). An `R²` sitting at its own null distribution's median is not
"genuine periodic structure recovered," regardless of how tight the
R5 specificity-over-targets sweep looked (8.3%, a different question this
audit confirms is not a substitute). This is structurally identical to
exp-083/Iteration 60's own precedent — the same program, the same
instrument family, the same "specificity check passed, null-under-noise
check failed" shape, one cycle later — and this program's own written
standard for that precedent (do not soften a real finding) applies here
without qualification: **leg (a)'s verdict should be recorded in LOGBOOK as
INCONCLUSIVE, not SUPPORT**, with the shape-correlation finding (§1 item 5)
credited alongside it as the genuinely new, surviving, positive result of
this cycle — the two are not in tension: the model curve's *shape* is a
real, independently-confirmed match to the real FDTD data; its *best-fit
period*, taken alone, is not distinguishable from noise at this sample
size, and the record should say both things plainly rather than collapsing
to one.
