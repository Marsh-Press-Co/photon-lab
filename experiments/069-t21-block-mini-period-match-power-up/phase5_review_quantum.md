# PHASE 5 — REVIEW · QUANTUM OPTICS · Panel Iteration 46 · exp-069

*Fresh sub-agent, QUANTUM OPTICS charter (PANEL.md seat 5). Blind to any
other seat's Phase-5 review this cycle. All numbers below independently
recomputed from `results.json`, `run.py`, and `desk_check_settling_delta_
output.json` — not taken on the writeup's word.*

## 0. Independent reproduction

Recomputed directly from `results.json::block_dense` (31 rows) and
`run.py`'s own fitting code, cold, without reading `phase4_results.md`
first: `ptp=0.0040263`, `mean=-0.0002485`, `ratio=16.2003`; fixed-period
`R²=0.201650` at `T=cpl/A=0.0265957`; free-period grid search over
`P*∈[1.0°,4.0°]`, 400 points, best `P*=2.842105°`, `R²=0.627213`,
`rel_dev=44.95%` from `P(39°,600nm)=1.960795°`. **Every headline number in
`phase4_results.md` reproduces exactly.** No R4-class defect found.

## 1. The R3 resolution check (P-069-5) — implemented as I specified, but the pass is weaker than the write-up's language suggests

**Implementation fidelity: correct.** My own Phase-2 critique demanded a
minimal, budget-conscious R3 leg at the two cells already earmarked for
Block SETTLE-C80 (39.0°, 40.0°), `cpl` 20→30. `results.json::block_r3`
confirms: 2 angles, **both** configs (`C_empty_C40_r3`, `C_empty_C80_r3` —
Red Team's docket upgraded my own "C80 alone at minimum" ask to both, which
I take as an improvement, not scope creep), `cpl=30` (geometry ×1.5,
`STEPS=4200=2800×1.5`). This is exactly what I asked for.

**Does the CONFIRM/REFUTE band test what I intended?** Only partially.
P-069-5's construction (same sign at both angles AND
`delta_r3/delta_native ∈ [0.3, 3.0]`) is a legitimate discriminator in
principle — a Yee-staircase artifact tied to the `ABSORB` boundary's
discretization would plausibly sign-flip or collapse under a 1.5×
resolution change, the way exp-009's cloak-geometry artifacts did at
`cpl=20`. But the **measured** ratios are 1.97 (θ=39°) and 2.50 (θ=40°) —
the delta value nearly *doubled*, and at 40° increased by 150%, under
resolution refinement. Compare this program's own **established** R3
precedent for "a feature survives resolution and is real": exp-005's
mu_r_floor jump shrank 17.7%→16.4% (**7% relative**) under the identical
cpl 20→30 step; exp-015's eps_z trough shrank 17.69%→16.42% (**7.2%
relative**), explicitly cited in LOGBOOK as confirming a *genuine physical
feature, not a 1-cell grid-quantization artifact*. Every prior "survives
resolution" claim in this program's history changed by single-digit
percent. This cycle's R3 pass changed by **97–150%**, and only avoided
REFUTE because the band itself (`[0.3,3.0]`, i.e. −70% to +200%) is an
order of magnitude wider than anything this program has previously treated
as a clean resolution-convergence result.

This does not overturn P-069-5's CONFIRM — same sign, same order of
magnitude, and the delta values here (~10⁻⁴) are two orders of magnitude
smaller than the C_empty absolute values (~5×10⁻³) they're differenced
from, so proportionally larger discretization noise on the delta itself is
plausible and was reasonably anticipated by the wider band (which mirrors
exp-033's own precedent, not a bar loosened this cycle). But
`phase4_results.md`'s declarative language — "**not** a resolution
artifact," "a real physical feature, **not** Yee-grid discretization
structure" — overstates what a pass this close to the tolerance ceiling,
at only 2 of 31 angles, actually establishes. **The R3 check validates that
`delta(θ)` doesn't vanish or flip sign under refinement at two spot
points; it does not validate that the specific ~2.84° period found by the
free-period fit across the whole 31-point window is itself
resolution-robust** — a genuinely independent test of that would rerun a
representative span of the DENSE window (not just 2 points) at `cpl=30`
and refit. That test was never run. This is the one concrete residual gap
in an otherwise sound design.

## 2. Does T28 repeat R5's mistake? No — argued from the actual construction, not asserted

R5 (Iteration 28, exp-051) was ruled out because its regressor — offset
from a fringe's own zero-crossing, normalized by the *local* period
`P(θ)=λ/(A·cosθ)` — failed on two independent structural grounds: (a) the
fringe's real zero-crossings do not recur at `P` (measured spread
0.137–1.279·P, 9.3×), so "phase within a period" wasn't a phase at all;
and (b) the construction was convention-blind while the thing it was
trying to predict was convention-determined, so a zero-information
baseline beat it outright (AUC 0.792 vs 0.649).

T28's construction shares neither defect. It is not a normalized offset
built by referencing a measured zero-crossing to an assumed period at all —
it is a direct, unconstrained least-squares fit of a periodic model to
31 real, densely-sampled `delta(θ)` values, with the period itself as the
one free parameter the grid search is estimating, not assuming. It is not
used as a predictor of a downstream convention-sensitive label (R5's fatal
flaw); it is a descriptive measurement of the dominant periodicity actually
present in one specific, well-defined series, reported honestly as
**not matching** the a priori T21 prediction rather than being retrofitted
to match it. Nothing about T28 is convention-blind — `delta(θ)` is
computed once, from committed `C_empty` values, with no ambiguous
convention choice anywhere in its definition. R5 died because its quantity
wasn't actually a phase and didn't track what it claimed to; T28's quantity
is exactly what it claims to be — the best-fit period of a real signal —
and the honest, disclosed finding is that this period is real but
*unexplained*, not that it's being oversold as a validated mechanism. This
is a materially different, better-grounded construction, not a repeat.

**One genuine physical argument worth adding, absent from the write-up
entirely**: `C40` and `C80` are a **congruent** construction — `A=752` is
held *identical* for both configs by exp-065's own design (that congruence
is the entire point of the C40/C80 pairing, independently re-verified this
cycle at G-1). T21's aperture-diffraction model depends on `A` alone, so it
predicts C40(θ) and C80(θ) individually carry the **same** period
`P(θ)≈1.96°` — meaning their *difference*, to first (linear) order, should
also carry that same period, just with different amplitude/phase, not a
different frequency. Finding a genuinely different dominant period in the
difference (2.84° vs 1.96°, `R²=0.63` vs the fixed-`T` fit's 0.20) is
therefore itself informative: it argues against "T21 aperture fringe,
slightly detuned" and toward "the `ABSORB`/`PAD` boundary condition
contributes its own, distinct periodicity that the two configs don't
share identically" — exactly T28's own "boundary-thickness-scale
mechanism" candidate, but with an actual mechanistic reason to prefer it
over a residual-artifact reading, not just a name on a list. I'd rank
testing this first (§4 below).

## 3. The multiple-comparisons risk — real in principle, empirically absent in this result

The concern is legitimate: a 400-point grid search over `P*∈[1°,4°]`,
reporting the best `R²` from a 3-parameter fit (fixed `c₀`, plus `a,b` at
each candidate period) on 31 points, is exactly the shape of procedure that
can manufacture an impressive-looking fit from pure noise if not checked.
I tested this directly rather than reasoning about it qualitatively: I
reimplemented the exact grid search (same 31 θ-values, same 400-point grid
over `[1.0°,4.0°]`, same fixed-`c₀`+cos+sin fit) and ran it against 20,000
draws of pure Gaussian white noise (R² is scale-invariant, so the noise
amplitude is irrelevant to the null distribution).

**Result: the null distribution of the search-maximized R² has median
0.179, 95th percentile 0.331, 99.9th percentile 0.502, 99.99th percentile
0.604 — and 0 of 20,000 draws reached 0.6272.** The observed R²=0.6272
sits above the entire simulated null distribution; the empirical p-value
is below ~5×10⁻⁵, and the tail is clearly falling off fast enough that a
much larger simulation would not be expected to change this qualitative
conclusion. As a secondary sanity check, only 22/20,000 draws (0.11%)
even reached P-069-2's own REFUTE band (`R²≥0.50`) under the *searched*
statistic — meaning the design's own pre-registered 0.50 REFUTE line for
the **fixed**-period test (which doesn't search at all) is, if anything,
conservative relative to what the *searched* statistic alone would need to
clear by chance.

**Conclusion: this is not an overfit peak.** Even fully accounting for
the 400-candidate search, `R²=0.6272` at `P*=2.84°` is a genuinely
strong, well-determined periodic signal — not a good fit that turned up
by chance. The claimed "not noise" language in `phase4_results.md` and
`NOTES.md` is, on this specific point, appropriately confident, not
overclaimed — a rare case this cycle where the write-up's language is
exactly as strong as the underlying statistics support, no more and no
less.

## 4. Desk-check-then-build sequence — honored, unlike Iteration 45

My own standing concern from Iteration 45 (the desk-check discipline
demanded there was silently narrowed to a citation tripwire, dropping the
substantive half) did **not** recur here. `desk_check_settling_delta.py`
and its output JSON are committed and dated before `phase1_proposal.md`'s
own text references them; I independently verified the file's `flip_
fraction`/`samples_per_period_at_1deg_step` figures (0.6703/0.5027/0.4022
at 450/600/750nm) against the raw 36-row dataset and they check out. The
one real defect in the desk check — its "600nm least-aliased" framing was
backward (600nm's near-Nyquist sampling is the signature of aliasing, not
clean resolution) — was independently caught by two blind Phase-2 seats
(PHOTONICS, and my own Phase-2 self) and corrected at Phase 3
(Idealization 2 now states the true fact). The sequence itself, not just
the framing of its output, was followed properly this cycle.

## 5. Other findings

- **Combined Verdict gating (Attack 1 from Red Team's Phase-2 audit)**:
  independently confirmed fixed. `run.py::score()`'s combined verdict is a
  genuine 5-way conjunction (P-069-1 through -5); the actual outcome
  (P-069-4 CONFIRM, P-069-5 CONFIRM, but P-069-2/P-069-3 both NEITHER) does
  route to `FORMAL_RETIREMENT_NON_DECISIVE`, not to a mislabeled "not
  settling" claim — the fix held under the real data, not just on paper.
- **The pre-committed non-decisive-outcome rule (mandatory fix 4, VISION's
  Phase-2 catch) worked exactly as intended.** The result landed in
  precisely the ambiguous bucket VISION warned was the most likely outcome
  given the desk-check evidence, and the retirement fired automatically,
  with the stated reason computed in code rather than argued after the
  fact. This is the correct outcome for the LOCKED mandate's own "no
  further relabeling" text, and I credit it as real process progress.
- **R_contact disclosure (mandatory fix 9)**: present, one line, in both
  NOTES.md Idealization 9 and `phase4_results.md`. Untouched this cycle,
  correctly disclosed rather than silently dropped.

## Verdict: **PARTIAL**

The LOCKED mandate is genuinely closed, honestly and without relabeling —
that is real, credit-worthy progress on a four-cycle-deferred
Checkpoint-4 item, and the statistical rigor behind the headline new
finding (T28) holds up to independent, adversarial re-derivation, including
the multiple-comparisons scrutiny it most needed. I do not find grounds to
call this RULED OUT or PROMISING, for one reason each way: it is not RULED
OUT because the period-match instrument did its job and produced a real,
well-supported finding, not a failed or uninformative test; it falls short
of PROMISING because the one test built specifically to separate "real
physical feature" from "grid-discretization artifact" (P-069-5) passed by
a much narrower and differently-shaped margin than this program's own
historical bar for that claim, at only 2 of 31 angles — meaning T28's
mechanism-vs-artifact question is *less* closed than `phase4_results.md`'s
declarative language ("not... Yee-grid discretization structure") states,
even though I find no evidence it is *wrong*, only under-tested at the
specific period value now in question. A LOCKED item closing into a new,
only-partially-resolution-verified open thread is real progress, but not a
clean win.

## Top-3 ranked candidate directions for Iteration 47 (QUANTUM'S charter)

1. **Close the residual R3 gap on T28 itself, not on the original P-069-5
   cells.** Rerun a representative span of the DENSE window — enough
   points to re-run the free-period fit, not just check 2 spot values —
   at `cpl=30`, and refit `P*`. This is the direct, cheap (a handful of
   points, same harness, zero new `lab/` code) test of whether `P*≈2.84°`
   itself is resolution-robust, which is what the mechanism-vs-artifact
   question actually turns on, not whether `delta` at 39°/40° keeps its
   sign. Desk-first is not available here (this needs new FDTD points),
   but the design is a trivial extension of exp-069's own harness.
2. **Test the congruent-A argument (§2 above) before proposing any new
   mechanism.** A zero-FDTD desk check: fit each config's own `C_empty(θ)`
   series (C40 alone, C80 alone — both already sitting in this cycle's own
   `results.json::block_dense`) to T21's `P(θ)` model separately, and check
   whether the ~2.84° signature is already present in one or both configs
   individually, or only emerges in the difference. If it's present in
   `C80` alone (the padded config) and not `C40`, that's a strong,
   specific pointer toward a padding/`ABSORB`-boundary-scale mechanism
   distinct from T21's aperture fringe — expressible as an effective
   classical parameter (a second spatial frequency tied to `PAD`/`ABSORB`
   depth) per this seat's own expressibility contract, and testable at
   zero marginal FDTD cost using data already committed.
3. **R_contact's `measured_direct` literature search** (PLAN.md queue item
   #2) — not my own charter's centerpiece, but still the program's only
   standing item that can move a real materials number, three-plus cycles
   blocked purely on tooling availability, explicitly orthogonal to items
   1–2 above. Flagging it here only to keep it visible, not to argue its
   physics.
