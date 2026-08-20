# PHASE 3 — SYNTHESIS · Panel Iteration 28 · exp-051

*Director: the cloud panel shift agent. Per PANEL.md, the Director
synthesizes but does not vote in Phase 2, and must state which criticisms it
accepts and which it overrides, and why — in writing, here. The Phase-1
proposal (`phase1_proposal.md`) stands **unedited** as the historical
record, per this program's "flag, don't silently rewrite" convention
(exp-050's own precedent). This file, plus the frozen predictions in
`NOTES.md`, is the design Phase 4 executes.*

---

## 0. What Phase 2 did to this proposal

ELECTROMAGNETISM proposed a phase-corrected difficulty predictor: regress
tier-instability on (i) θ₀'s phase offset from the nearest zero-crossing of
the underlying single-angle T21 fringe, normalized by the local fringe
period `P(θ)=λ/(A·cosθ)`, and (ii) `|C(n=81)|/ABS_TOL`.

Five seats critiqued blind. **Four of the five independently rebuilt the
proposal's own §2.2 machinery from its prose and ran it** — PHOTONICS,
MATERIALS, QUANTUM OPTICS, VISION SCIENCE — and all four found the same
thing: the proposal's primary scored deliverable (P-PCDP-1) and its
pre-registered fallback (P-PCDP-2) **already fail their own falsification
bands at the desk**, before Phase 4 would run. Red Team, going last with
everything, rebuilt both the original predictor and QUANTUM's proposed
replacement cold and confirmed all of it to four-plus significant digits.

Convergent numbers, four independent implementations:

| Quantity | PHOTONICS | MATERIALS | QUANTUM | Red Team |
|---|---|---|---|---|
| AUC(\|offset\|) | 0.649 | 0.649 | 0.6494 | **0.6494** |
| AUC(`log10(\|C(81)\|/ABS_TOL)`) | — | 0.52 | 0.5195 | **0.5195** |
| P-PCDP-2 threshold scan | fails hard | fails hard | fails hard | **fails at all 400 thresholds in [0.05,0.40], including the lenient hard-falsification-escape bar** |

Against a CONFIRMED bar of AUC≥0.85 and a REFUTED line at 0.65, the primary
regressor lands at 0.6494 — REFUTED by six-tenths of a percentage point,
and its companion regressor is indistinguishable from chance.

**The structural reason, found independently by PHOTONICS and VISION and
confirmed by Red Team, is not statistical power.** Both proposed regressors
are *convention-blind by construction* (mean inter-convention |Δoffset| =
0.041) while the label is *convention-determined* (6 of 7 positives are
`incoherent_corrected`; the label flips between conventions at 5 of 9
cells). A zero-information predictor — "unstable iff the function is
`incoherent_corrected`" — scores sens 6/7, spec 8/11, AUC 0.792, **clearing
P-PCDP-2's own success bar outright using no phase information whatsoever.**
A regressor that cannot see the axis the label varies on cannot explain
that label, at any sample size.

## 1. The replacement mechanism, and why I adopt it

QUANTUM OPTICS did not stop at refuting. It diagnosed the crux quantity as
measuring the wrong periodicity **in kind**, and named the right one.

The n=41 quadrature residual is the **Poisson-alias term of the single-angle
fringe referenced to the quadrature node lattice** — spacing
`h = 2·half_width_factor·FWHM/(n−1)` (= 2.5° at n=41, FWHM=20°,
`half_width_factor=2.5`, read directly from the already-committed
`gaussian_angle_weights`) — **not** the fringe's own period `P`. The
proposal normalizes by `P`; the phenomenon is set by `h`.

PHOTONICS independently falsified the proposal's premise on the same
machinery from the other side: the fringe's measured zero-crossing gaps span
**0.137·P to 1.279·P**, a 9.3× spread. The fringe does not recur at `P` at
all, so "offset within the local period" is not a phase.

QUANTUM's replacement, verified twice independently (QUANTUM, then Red Team
from a cold implementation):

- `E_pred = 2·Re[alias_coeff(m=1)] + 2·Re[alias_coeff(m=2)]`
- Reproduces the **measured** `C(41)−C(161)` at all 18 pre-checked
  combinations: QUANTUM r=1.00000 / ≤1.4%; Red Team r=0.999998 / ≤1.445%
  (residual gap fully explained by a coarser integration step).
- Separates the same 7-unstable/11-stable set **perfectly** (AUC 1.0000,
  sens 7/7, spec 11/11) at the *unfitted* threshold `|E_pred| = ABS_TOL` —
  the pre-existing decision line, no fitted parameter anywhere.
- Explains the ~1.9–2.3× convention asymmetry as the ratio of the two
  conventions' angular spectral amplitude at the single alias frequency
  `1/h` (median 1.92–1.95), **including reproducing the anomalous inversion
  at 750nm/38°** that VISION independently found in the raw `Δabs` ratio
  (0.775) via a structurally unrelated computation — 0.835 in Red Team's
  spectral object. Two unrelated diagnostics, three seats, one anomalous
  cell.

Red Team's ruling — adopt QUANTUM's mechanism as the corrected primary
design, not as an addendum — **I accept in full.** `phase_offset` is not a
rough draft of the right idea that needs tuning; it targets a different and
demonstrably wrong object.

## 2. Director's ruling: the pre-check problem, and why Phase 4's scored predictions move

**This is the one place I go beyond Red Team's docket, and it is the most
important decision in this synthesis.**

Red Team's docket item 7 would have Phase 4 score the alias predictor
against the continuous target on the 18 GEOM78 FWHM=20° incoherent-family
combinations. **I override that scoping.** Here is the problem: the alias
predictor's performance on those 18 combinations has now been computed, at
the desk, **twice** — once by QUANTUM in Phase 2, once by Red Team
adjudicating Phase 2 — with the answers written into committed files before
Phase 3 froze anything. A "prediction" that the model will score AUC≈1.0 on
exactly those 18 rows is not a prediction. It is a transcription.

This program has been here before and handled it by disclosure (exp-050,
where Red Team's own pre-Phase-4 check informed P-NCONV27-2, disclosed as a
cross-checkable pre-check rather than an authority). But exp-050's pre-check
covered **2 coordinates of a 108-cell sweep**. Here the pre-check covers
**the entire scored deliverable.** Disclosure alone is not enough at that
ratio; the house discipline that predictions are committed before the run
would become ceremonial.

**Ruling.** The 18 pre-checked combinations are hereby designated a
**disclosed CALIBRATION set: reported in full, scored against nothing.**
Phase 4 reports their numbers and reports agreement with QUANTUM's and Red
Team's independent pre-checks as a three-way cross-validation of the
implementations — informational, exactly as P-NCONV27-6b was.

**Every scored prediction in this cycle is moved out-of-sample**, onto the
**198 combinations no seat has computed an alias coefficient for**:

| Block | Combinations | Committed unstable (`n*≠41`) | Source of labels |
|---|---|---|---|
| GEOM78, `coherent`, FWHM=20° | 9 | 6 | exp-050 `results.json` |
| GEOM78, all functions, FWHM≤10° | 81 | 0 | exp-050 `results.json` |
| A=752 (`GEOM_EXP042_OLD`), all functions, all FWHM | 108 | 16 | exp-049 `results.json` |
| **Out-of-sample total** | **198** | **22** | — |

The labels are already committed public data in two prior experiments —
they were not generated by this cycle and cannot be tuned by it — but **no
seat, and not the Director, has evaluated `E_pred` at a single one of these
198 combinations.** The threshold is unfitted (`|E_pred| = ABS_TOL`, the
pre-existing decision line). This is a genuine out-of-sample test of a
mechanism proposed at Phase 2, and it is a far stronger cycle than the one
the Phase-1 proposal designed.

It also converts three of Phase 2's own criticisms into scored tests rather
than concessions: MATERIALS' demand that `coherent` be restored (it now
carries 6 of the 22 out-of-sample positives, on a shared single-angle fringe
where `|offset|` is degenerate by construction — the falsifier MATERIALS
said was being dropped); VISION's class-balance concern (22/176 across 198
rows, not 7/11 across 18); and MATERIALS' own separate finding that **7 of
18 tier labels flip between A=752 and A=724**, which makes the A=752 block a
real generalization test rather than a repeat.

## 3. Accepted criticisms

Every one of Red Team's 9 mandatory-fix items is **ACCEPTED and adopted**:

1. **Crux replaced** — `phase_offset` out, `alias_coeff`/`E_pred` in, with
   both `m=1` and `m=2` (m=1 alone is 6–16% off at 450nm). *Accepted:
   verified independently twice.*
2. **Memoization mandatory** — `_geom_derived(g)` and the propagator
   matrices hoisted once per `(geometry, λ)`. *Accepted: THERMODYNAMICS
   measured 168–269 ms/evaluation unmemoized vs 3.96/15.43 ms hoisted (~8×),
   putting the zero-crossing search alone at ≈103 min against a claimed
   13-minute whole-cycle budget; Red Team independently confirmed the fix is
   sufficient (≈8.5 min for a strictly larger computation). §6's "optional,
   this proposal does not require" framing was wrong.*
3. **`coherent` restored** — *Accepted, and promoted: see §2. Its
   single-angle fringe is bit-identical to `incoherent`'s by construction,
   yet its tier labels differ at 5 of 9 cells — a degenerate-x1 control that
   is free to compute.*
4. **Slope machinery retired** — P-PCDP-4/5 replaced by the alias-frequency
   spectral-amplitude ratio. *Accepted: the slope ratio anti-correlates with
   the quantity it was meant to explain (Spearman ρ = −0.300), while the
   spectral ratio reproduces both the magnitude and the 750nm/38°
   inversion.*
5. **`g["A"]` KeyError fixed** — `A = g["OBJ_Y"] − g["ABSORB"]`. *Accepted:
   verified — no `"A"` key exists in either geometry dict.*
6. **Counting slips fixed** — "9×3=27 spot points" → 9 cells × 2 conventions
   = **18**; per-cell ratio objects are one-per-cell (**9**), not
   one-per-combination. *Accepted: three seats caught these independently.*
7. **Continuous target primary, binary demoted** — *Accepted as to
   substance, **overridden as to scope** (§2): scored out-of-sample, not on
   the pre-checked 18.*
8. **`ABS_TOL`-sensitivity ledger row** — *Accepted: VISION's finding that
   `ABS_TOL = 0.1·C_THR` makes every in-scope label reduce to one continuum
   cut, stable only over `ABS_TOL ∈ [0.08,0.10]·C_THR`, is real and must be
   disclosed. Reported, not re-tuned — idealization 2 still governs.*
9. **Executable ledger assertion + process-start timing** —  *Accepted:
   Red Team verified by direct code read that exp-050's `t0 = time.time()`
   still sits inside `main()`, so THERMODYNAMICS' Iteration-27
   recommendation was never actually adopted. It is adopted here, in code.*

**Red Team's scope-drift ruling is also ACCEPTED and binding:** Iteration 29
builds and measures the fixed-absolute-thickness `graded_black_shell`
variant's own `C`, **unconditionally** — not contingent on this cycle's
findings, not subject to a fifth ranked-list competition. Red Team verified
the citation chain independently: first queued at Iteration 7, re-ranked
without being reached at 25, 26, 27, and 28 — a 21-iteration span — while
this cycle is the third consecutive instrument-fidelity cycle and the sixth
in nine. The program's one prior precedent (the r=156 leg) got a committed
unconditional trigger after its *fourth* deferral. This one is well past
that bar. Recorded in LOGBOOK and PLAN.md at close.

## 4. Overridden criticisms

Stated plainly, per PANEL.md's requirement:

- **Red Team's docket item 7, as to scope** — overridden and *strengthened*,
  per §2: the continuous target is scored, but out-of-sample on 198
  untouched combinations rather than on the 18 the Phase-2 pre-checks
  already answered. Red Team was right about the target and did not address
  the pre-check-saturation problem its own audit created. The Director's job
  is to notice when a Phase-2 pre-check has consumed the deliverable.
- **MATERIALS' request to retarget onto `Δabs` and drop the binary label
  entirely** — partially overridden. The continuous target becomes primary
  (accepted), but the binary `n*≠41` classification is *retained as a scored
  secondary*, because it is the quantity every downstream citation in this
  program actually uses (`nstar` governs whether n=41 is safe at a given
  cell) and because the unfitted-threshold claim is the strongest falsifiable
  form the mechanism takes. VISION's `ABS_TOL`-fragility finding is handled
  by disclosure (item 8), not by discarding the label.
- **VISION's implicit suggestion that the Iteration-27 standing rule
  (re-measure near-boundary headroom citations at their own geometry, check
  angular neighbours) binds this cycle** — overridden on the letter, adopted
  in spirit. This cycle issues no headroom citation and no perceptual
  verdict, so the rule does not bind. But VISION's underlying point stands
  and is honored: the A=752 block is included precisely so no conclusion here
  rests on a single geometry, and idealization 9 below restates that no
  perceptual claim is made.
- **Nothing else is overridden.** No seat's finding is set aside as wrong;
  every numeric claim any seat made and that Red Team or I checked, held.

## 5. What this cycle now is

Not "test ELECTROMAGNETISM's predictor." That question was answered at the
desk during Phase 2, by four seats independently: **it does not work, and
the record says why.** That is a real result and it is reported as one.

This cycle is now: **a genuine out-of-sample test of the alias-lattice
mechanism QUANTUM OPTICS proposed and Red Team independently verified** —
across 198 combinations, two geometries, three functions, and four beam
widths that no pre-check has touched, against unfitted thresholds and
already-committed labels from two prior experiments.

If it holds, exp-050's tier instability and its ~1.9–2.3× convention
asymmetry are both explained by one geometric fact — the fringe aliasing
against the quadrature node lattice — and this program gains a
zero-FDTD-cost predictor for whether any future `beam_divergence_*` citation
at any geometry needs n>41, replacing a per-cycle re-run. If it fails
out-of-sample after scoring AUC 1.000 in-sample, that is a textbook
overfitting lesson delivered on 18 rows, and the honest record will say so.

Both outcomes are worth the ≈15 minutes this costs.

---

*Predictions are frozen in `NOTES.md` and committed to git BEFORE any Phase-4
code is written. House discipline, non-negotiable.*
