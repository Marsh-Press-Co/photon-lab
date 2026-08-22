# exp-059 — The LOCKED `Q_ext(x)` Closed-Form Cylinder/Disk Check

Panel Iteration 36. Lead: **PHOTONICS**, by **UNCONDITIONAL LOCK, breaking
rotation** (though PHOTONICS was also next-in-rotation regardless — Iteration
35 closed with "rotation resumes at PHOTONICS" — a clean coincidence, not a
scheduling conflict) — Red Team's Iteration-34 Phase-5 ruling granted this
item unconditional-lock status after three clean deferrals (Iterations
32/33/34), the lowest deferral count that has ever triggered a lock in this
program's history (`h_eff` fired at 5, `graded_black_shell_flagship` at 3).
Confirmed as Iteration 36's lead at Iteration 35's own close ("Director's
call: NOT folded in [to Iteration 35] as a zero-cost rider, explicitly
deferred").

Full cycle: Phase 1 proposal (PHOTONICS) → five blind parallel critiques
(MATERIALS, ELECTROMAGNETISM, THERMODYNAMICS, QUANTUM OPTICS, VISION
SCIENCE — all support-with-changes, no opposes) → Red Team last with
everything (PROCEED-WITH-MANDATORY-FIXES, 6-item docket, one new load-bearing
finding of its own) → this Phase-3 synthesis. Full verbatim record:
`LOGBOOK.md`, Iteration 36.

## Hypothesis

Not a mechanism proposal — a sidecar/validation cycle, same register as
Iterations 20/22/25/27/31/34. This item closes a physics gap opened at
panel Iteration 20 (exp-043) and sharpened at Iteration 31 (exp-054):
`lab.thermo_sidecar.absorbed_power_established_ratio`'s `iso_xsec_sq`
convention treats the flagship absorber's absorbing area as
`(sigma_ext_cells*dx)^2` — i.e. it takes the object's MEASURED,
diffraction-inflated extinction width `w_on` as if it were the object's
real size, rather than its true geometric radius `r_out`. That inflation
(`w_on/(2*r_out) ~= 1.54`, i.e. an implied `Q_ext~=1.54`) has sat as an
unbounded empirical number since Iteration 31, asserted but never checked
against established diffraction physics — the exact gap THERMODYNAMICS
itself recommended pre-registering an unconditional-lock trigger for,
rather than waiting on a retroactive discovery (Iteration 34).

This item builds an exact, zero-FDTD closed-form reference: the classical
Bessel/Hankel partial-wave (Mie-cylinder) series for the extinction
efficiency `Q_ext(x)` of a normally-illuminated, perfectly-conducting (PEC)
infinite cylinder, TM_z polarization (this bench's own 2D convention),
evaluated at the bench's actual size parameter `x=k*r_out~=24.50`. It
bounds — not "closes," see Phase-3 fix 4 below — whether the bench's
observed excess is consistent with, above, or below what a sharp-edged,
fully-opaque object of the same size is exactly predicted to do.

## Setup

New module: `lab/qext_theory.py`. Zero new FDTD calls — confirmed by
inspection, no `Sim`/`fdtd2d` import anywhere in the module.

| Parameter | Value | Source |
|---|---|---|
| `R_OUT_CELLS` (flagship) | 78 | `experiments/020-ambient-baseline/design_geometry.py:25` |
| `dx_m` | 30e-9 m | same file, `CPL_600=20` cells/lambda at 600nm |
| `r_out_m` | 2.34e-6 m | computed |
| lambda | 600e-9 m | bench point |
| `k` | 1.0471975511965977e7 rad/m | computed |
| `x = k*a` | 24.504422698000383 | computed, code-verified (confirms/sharpens PHOTONICS' own Iteration-34 informal `ka~=24.5` estimate) |
| `sigma_ext_cells` (flagship) | 240.0073740162445 | `experiments/043-docket7-thermo-sidecar/results.json::graded_black_shell_flagship.sigma_ext_cells` |
| `w_on = sigma_ext_cells*dx` | 7.200221220487335e-6 m | computed |
| `Q_ext_measured = w_on/(2*r_out)` | 1.5385088077964393 | computed — EXACTLY matches `experiments/002-cross-sections/results.json::absorber-600.q_ext` (independently confirmed by four of six Phase-2 seats plus Red Team) |
| `Q_ext_measured^2` (area-domain, `iso_xsec_sq`) | 2.367009351667221 | computed |
| `Q_ext_PEC(24.5044)` (this item's closed-form reference) | 2.1177205150608365 | `lab/qext_theory.py`, exact partial-wave series, 4-gate self-tested |
| ratio measured/PEC | 0.7264928477836661 | computed |

Formula (module docstring, verbatim): normal-incidence TM_z scattering by
an infinite PEC cylinder, boundary condition (tangential E=0 at rho=a)
gives `c_n(x) = -J_n(x)/H_n^(1)(x)`, `Q_ext = (2/x)*Re[c_0 + 2*sum_{n>=1}
c_n]`. Sourced to Bohren & Huffman, *Absorption and Scattering of Light by
Small Particles* (Wiley, 1983/1998), Ch. 8 SS8.4. WebFetch to the primary
scholarly source failed (DNS/egress block, T18's standing condition) —
WebSearch-snippet-level sourcing only, disclosed as such throughout. The
`x->infinity->2` extinction-paradox limit is cited to Wikipedia's
"Extinction paradox" article (general result for any large opaque/
reflecting obstacle, independent of composition). Independently re-derived
from Jacobi-Anger + the stated boundary condition by BOTH ELECTROMAGNETISM
and QUANTUM OPTICS at Phase 2, matching line-by-line.

## Phase 2 — five blind critiques + Red Team (accepted/overridden, Director's synthesis)

All five seats: **support-with-changes**, zero opposes. Red Team's own
ruling: **PROCEED-WITH-MANDATORY-FIXES**, 6-item docket. **All six items
ACCEPTED IN FULL** (one, MF-5, accepted in part with an explicit override
of its own FDTD-requiring half — see below):

1. **[MF-1, ELECTROMAGNETISM + QUANTUM OPTICS, independently converged,
   Red-Team-reconfirmed a third way]** `qext_theory.py`'s original self-test
   docstring claimed gate 1 (energy conservation, `Q_ext==Q_sca` for a
   lossless PEC scatterer) was "the independent numerical proof that this
   sign/coefficient choice is right." **FALSE AS STATED**: `-Re(c_n) ==
   |c_n|^2` is an algebraic tautology for ANY coefficient of the form
   `c_n=-A/(A+iB)` with real A,B — verified numerically (both critiquing
   seats, then Red Team a third way) for BOTH this module's TM_z
   (non-derivative Bessel) coefficients AND the different TE_z
   (derivative-Bessel) polarization's coefficients alike. Gate 1 proves
   only the overall SIGN convention (it did catch a real first-draft bug,
   `Q_ext->-2`) — it cannot discriminate TM_z from TE_z or any other
   lossless boundary condition. **Fixed**: docstring reworded to state the
   gate's true, narrower scope; polarization-specific correctness now
   rests explicitly on the independent boundary-condition re-derivation
   (module docstring) plus the NEW gate 4 (MF-6, below) rather than on
   gate 1's inflated claim.
2. **[MF-2, QUANTUM OPTICS, Red-Team-reconfirmed at the exact threshold]**
   Gate 3's own verification method (a 2.2x-n_terms comparator call) was
   found to silently return NaN via Bessel/Hankel underflow at `x>=260`
   (confirmed: 255 finite, 260 NaN) — undisclosed in the original draft,
   only ~10x past the bench's own `x=24.5`. The production
   `q_ext_pec_cylinder` at its own default `n_terms` stays finite through
   at least `x=300` — this is a self-check-scaffolding ceiling, NOT a
   production-formula bug. **Fixed**: new module constant
   `X_CONVERGENCE_CHECK_MAX=255.0`, `_self_test` now raises a clear
   `ValueError` rather than silently reporting a spurious pass/fail if gate
   3 is ever invoked past that ceiling by a future cycle reusing this
   module at a larger geometry.
3. **[MF-3, VISION SCIENCE, escalated by Red Team given recurrence count]**
   The Phase-1 draft's most-quotable numeric claim ("26.9% BELOW the
   sharp-edge reference... consistent with that direction") and the
   Predicted-Outcomes "confirmed (1.5385<2.1177)" line both appeared BARE,
   with the "REFERENCE/BOUNDING, NOT a literal model" caveat stated only
   ONCE, three paragraphs later in Idealizations — the exact
   once-stated-not-propagated pattern this program has now hit at
   Iterations 17/24/32/33/34/35, flagged by Red Team as approaching a
   materially stronger case for Checkpoint criterion 4 if it recurs again.
   **Fixed**: the caveat now travels inline at both bare-result sites
   (this document's own Results section below; `qext_theory.py`'s own
   `__main__` block print statement, module-level, so any future console
   run of the file carries it too, not just this NOTES.md).
4. **[MF-4, THERMODYNAMICS, confirmed against the LOCK's own charter text]**
   The Phase-1 draft's "closes a physics gap" framing overstated what this
   item does relative to the fact that ZERO scored margins move
   (THERMODYNAMICS' own recompute: substituting either the conservative
   `Q_ext=1` floor or the new PEC ceiling `Q_ext_PEC=2.1177` into
   `graded_black_shell_flagship`'s thermal-margin chain gives 1655x or
   369x respectively — both 2+ orders of magnitude clear of NETD-lo,
   unchanged classification). **Fixed**: reframed throughout as "bounds,
   for the first time, a previously-unbounded assumption" — not "closes."
   The separate, still-open `iso_xsec_sq` squaring-a-width-to-get-an-area
   convention question is stated explicitly as NOT resolved by this item.
5. **[MF-5, MATERIALS, accepted in part, one half overridden by Red Team]**
   MATERIALS found the directional claim ("a softer edge diffracts less...
   consistent with that direction") conflates two distinct, un-disentangled
   mechanisms: at the bench's own `x=24.5044`, `Q_ext_PEC=2.1177` sits in
   the resonance-ripple regime (MATERIALS' own independent sweep: x=20 to
   2.135, x=200 to 2.029, still ~6% above the x to infinity limit at
   x=24.5), not the pure asymptotic shadow-diffraction regime — and a
   SHARP-edged but uniformly LOSSY disk of the same `r_out` would also
   damp this ripple well below 2.12, no grading required. The proposal
   computed no control case isolating grading from bulk-loss damping, so
   the measured/PEC ratio cannot actually discriminate "soft edge
   diffracts less" from "any lossy material damps PEC's resonance ripple."
   MATERIALS' proposed remedy had two halves: (a) soften the wording, or
   (b) add a new sharp-uniformly-lossy-disk FDTD control run. **Red Team's
   override, adopted**: only (a) is mandatory for THIS cycle — (b) would
   require new FDTD, which is outside this LOCKED item's own zero-new-FDTD
   scope (verified: no `Sim` call anywhere in `qext_theory.py`); adopting
   it here would violate the cycle's own procedural constraint. **Fixed**:
   wording softened to "consistent with, not diagnostic of, edge grading
   specifically" throughout; the sharp-lossy-disk control run is queued as
   new backlog for a future, non-LOCKED iteration (see Next).
6. **[MF-6, Red Team's own new finding — the load-bearing answer to MF-1's
   gap]** Nobody (proposer or any of the five blind critiques) exploited a
   free, already-committed, genuinely non-tautological empirical
   cross-check sitting in the repo: `experiments/002-cross-sections`'s own
   three "reflector" scenes are a BARE PEC disk (`materials.pec_disk`,
   `R_CORE=30` cells, no shell) at 450/600/750nm — real Ez/Hy FDTD-measured
   `Q_ext` at three size parameters (`x=7.54/9.42/12.57`) distinct from the
   flagship's own `x=24.50`. Comparing the closed-form series against those
   three independently-measured values is exactly the check gate 1's
   tautology cannot provide: TWO INDEPENDENT ANSWERS (exact partial-wave
   series vs. a full discretized time-domain Maxwell solve) agreeing to a
   few percent is not explainable by an algebraic sign-convention identity.
   **Fixed**: added as new **gate 4** (`empirical_cross_validation`),
   zero new FDTD (data already committed) — measured agreement **+2.32%,
   -0.60%, -1.72%** at 750/600/450nm respectively, all within a 3% bar
   (chosen with ~30% margin above the largest observed deviation).

## T1 escape route

**NONE.** Pure closed-form/desk-analytic sidecar correction — no material
or mechanism change, no sigma(I)/sigma(x,t)/coherent apparatus proposed.
Does not touch constraints 1-4 and carries no constraint-1/2/3/4 stakes
directly. Red Team's explicit ruling: no `[constraint-#N-violation]` tag
applies anywhere in this cycle.

## Realizability bound

Not applicable — no new material or mechanism proposed.

## Predictions — committed before this cycle's final `run.py` execution

All four gate predictions below were computed during Phase 1/Phase 2 (the
closed-form code is fully deterministic — no stochastic element exists to
"blind" a prediction against, unlike an FDTD run) and are stated here, with
that fact disclosed plainly rather than presented as blind foresight, per
this program's verify-before-claim culture. What IS committed before any
run, in the house-discipline sense that matters (predictions fixed before
the OFFICIAL gated trust-suite execution that this NOTES.md's Results
section reports), is: the exact four gate thresholds below, fixed at Phase
3 synthesis, before `python3 lab/validation/run_all.py --only 21` (and the
full suite) was invoked as this cycle's own official, git-recorded run.

**P-059-1 (gate 1, energy conservation).** Predicted: `max|Q_ext-Q_sca|
<= 1e-9` absolute across 8 x-values spanning 1e-3..1e3. Central estimate
(already measured during Phase 1): `1.688e-13`.

**P-059-2 (gate 2, large-x asymptote).** Predicted: `|Q_ext(1e3)-2|<=0.011`
AND `|Q_ext(1e6)-2|<=1e-4`. Central estimates: `9.960e-3` / `9.962e-5`.

**P-059-3 (gate 3, series-convergence stability, x<=255 only per MF-2).**
Predicted: `|Q_ext_default - Q_ext_2x_terms| <= 1e-10` at the bench's own
`x=24.5044`. Central estimate: `0.000e+00` (bit-identical).

**P-059-4 (gate 4, NEW — empirical cross-validation, MF-6).** Predicted:
`max|rel_dev| <= 0.03` (3%) across the three bare-PEC reflector points
(450/600/750nm). Central estimates: `-1.716%`, `-0.605%`, `+2.324%`
(largest magnitude at 750nm/x=7.54, the smallest size parameter of the
three — consistent with finite-x diffraction-ripple effects being
proportionally larger at smaller x, a directionally sensible, not
surprising, pattern).

**P-059-5 (discriminating regression anchor).** Predicted:
`Q_ext_PEC(x=24.504422698000383) == 2.1177205150608365` to `<=1e-9`
absolute tolerance, reproducing the Phase-1/Phase-2-verified value exactly
under the OFFICIAL trust-suite invocation (stage 21's own regression gate).

**Falsification condition, pre-registered:** any gate failing under the
official `run_all.py --only 21` execution — despite passing identically
during Phase 1/2's informal verification — would indicate a Phase-3
synthesis edit introduced a regression, and would block this cycle's
Phase-5 review until root-caused.

## Idealizations

2D infinite-cylinder theory vs. this bench's finite simulated cylinder
(finite domain, `ABSORB` boundary cells, not literally infinite in y) —
already trust-gated elsewhere (stage 7), not re-litigated here.
**PEC-sharp-edge reference vs. the real graded/absorbing profile** —
`materials.graded_black_shell` is a graded-conductivity coating
(`R_CORE=30` PEC core, `R_COAT=78` shell edge, "quintic-smooth adiabatic
entry") over a PEC core, NOT a bare sharp PEC disk at `R_COAT=78` — the PEC
series is explicitly a REFERENCE/BOUNDING case, not a literal model
(inline at every citation point per MF-3). The directional comparison
(measured < PEC reference) is **consistent with, not diagnostic of, edge
grading specifically** (MF-5) — a sharp but uniformly lossy disk would
also be expected to damp the PEC resonance-ripple structure below 2.12; no
control case in this cycle disentangles the two mechanisms (queued, Next).
Normal incidence only — verified both sides of every comparison (bench
measurement and the closed-form reference) are normal-incidence
quantities. Single lambda=600nm for the flagship's own headline comparison
(the MF-6 cross-check spans 450/600/750nm, but that is a distinct,
separate object — a bare PEC disk, not the graded shell). Perfectly
conducting idealizes "opaque/strongly-absorbing" vs. the real shell's
measured absorption (`sigma_abs/sigma_ext=0.51`, T9, CLOSED — not
reopened here). `n_terms_default` truncation rule generalizes a
sphere-scattering heuristic (not itself cylinder-literature-sourced) —
sufficiency verified empirically (gate 3, within its now-documented
`x<=255` validity range), not assumed from the formula alone. **This item
does not change any scored constraint-1/2/3/4 verdict or any scored
thermal margin** (MF-4) — it bounds a previously-unbounded assumption
feeding `thermo_sidecar.py`'s ledger, nothing more.

## Trust-suite promotion

**Stage 21**, `lab/validation/run_all.py::stage21_qext_theory` — four
gates (energy conservation, large-x asymptote, series-convergence
stability, empirical cross-validation) plus a discriminating regression
anchor pinning the flagship's own `x=24.5044` evaluation, mirroring stage
18's own "formula self-consistency + discriminating regression pin"
pattern. `_STAGE_IDS` bumped from `range(1,21)` to `range(1,22)` — the
exact omitted-bump bug class this program has hit three times before
(Iterations 15/17/23), caught and applied correctly here on first wiring
(both the proposer's own recommendation and Red Team's audit flagged it
explicitly before any commit).

## Results

Zero new FDTD calls (confirmed: `git grep -c "Sim(" lab/qext_theory.py` is
empty). Official trust-suite invocation: `python3 lab/validation/run_all.py
--only 21` and the full fast bench `--only 12346789,10,11,18,19,20,21`.
Full data: `results.json`.

| Prediction | Predicted | Measured (official run) | Verdict |
|---|---|---|---|
| P-059-1 (gate 1) | <=1e-9 | **1.688e-13** | **CONFIRMED** |
| P-059-2 (gate 2) | <=0.011 / <=1e-4 | **9.960e-3 / 9.962e-5** | **CONFIRMED** |
| P-059-3 (gate 3, x<=255 only) | <=1e-10 | **0.000e+00** | **CONFIRMED** |
| P-059-4 (gate 4, NEW) | <=3% | **-1.716% / -0.605% / +2.324%** (450/600/750nm) | **CONFIRMED** |
| P-059-5 (regression anchor) | 2.1177205150608365 +-1e-9 | **2.1177205150608365** | **CONFIRMED** |
| MF-4 margin sensitivity (informational, not a falsifiable prediction) | established ~699.27x; floor/ceiling 2+ orders of magnitude clear | **established=699.27x, Q_ext=1 floor=1655.18x, PEC ceiling=369.07x** | **CONFIRMS MF-4**: no scored classification changes under either bounding extreme |

### Headline (for LOGBOOK)

**All four gates and the regression anchor CONFIRM under the official,
git-recorded trust-suite execution — zero deviation from Phase-1/2's own
informal verification, as expected for fully deterministic closed-form
code.** The LOCKED `Q_ext(x)` item — three clean deferrals (Iterations
32/33/34), the program's lowest-ever lock-trigger threshold — closes this
cycle with a genuine, gate-clean, honestly-scoped bound: the flagship
absorber's measured `Q_ext=1.5385` sits at **72.6%** of the exact
PEC-sharp-edge reference `Q_ext_PEC(ka=24.5044)=2.1177`, inside the
physically sane envelope `[1.0, 2.1177]` — bounding, for the first time,
an assumption that had sat as bare assertion since Iteration 31. **This
does NOT change any scored thermal margin** (`graded_black_shell_flagship`
stays 369x-1655x clear of NETD-lo under either bounding extreme, MF-4) and
does NOT resolve the separate, still-open `iso_xsec_sq`
squaring-a-width-to-get-an-area convention question. The directional
comparison (measured below the sharp-edge reference) is **consistent
with, not diagnostic of, edge-grading specifically** (MF-5) — a sharp but
lossy disk would plausibly show the same qualitative pattern, and this
cycle does not disentangle the two mechanisms. **Red Team's own new
finding (MF-6), independently exploiting already-committed
`experiments/002-cross-sections` bare-PEC bench data nobody else used,
supplies the load-bearing, non-tautological validation MF-1 showed gate 1
alone cannot provide**: the closed-form series agrees with this bench's
own real Ez/Hy FDTD solve to within 2.32% at three independent size
parameters — genuine cross-validation between an exact partial-wave series
and a full discretized Maxwell solve, now a permanent stage-21 gate.

## Next (pre-registered, for Phase 5)

Queued, not run this cycle (Red Team's own MF-5 override: out of this
LOCKED item's zero-new-FDTD scope): **(1)** the sharp-uniformly-lossy-disk
FDTD control run MATERIALS proposed, to actually disentangle "edge
grading reduces diffraction" from "any bulk loss damps PEC's resonance
ripple" — cheap (one new scene, reusing `materials.pec_disk` at `R_COAT`
with a uniform, non-graded sigma matched to the shell's own optical
depth), a natural Iteration 37+ candidate, not LOCKED. **(2)** The
remaining competitive queue from Iteration 35's own close (superseded
list retained as valid backlog, not deleted): R3-on-loaded-legs for
`off_pass_joint`/`off_bracket_joint`; the flank-denominator distribution
upgrade; a Geary-Hinkley tail-shape model of `C(delta)`; P-VIS-5's
angle-quantization sensitivity formula; MATERIALS' absorptivity/mechanism
literature check (now SEVEN cycles deferred, approaching this program's
own escalation pattern — flagged again); the T26 lambda/angle
generalization; the shell-vs-solid thermal-mass parameterization (third
consecutive cycle open); `graded_black_shell_flagship`'s own 450/750nm
sweep; `coupled_segment_general`'s RK4-cross-checked trust-suite
promotion.

## Phase 5 outcome

Six fresh blind seats + Red Team audit. **4 PROMISING (PHOTONICS,
ELECTROMAGNETISM, THERMODYNAMICS, QUANTUM OPTICS), 2 PARTIAL (MATERIALS,
VISION SCIENCE).** All six independently re-ran the code and confirmed
every gate/regression-anchor number byte-identical to this document's
Results table — the physics content was never in question from any seat.

**MATERIALS' PARTIAL**: confirmed MF-5's wording fix genuinely present and
correct everywhere checked, but the underlying edge-grading-vs-bulk-loss-
damping question (MF-5) remains a substantive, undisentangled realizability
unknown, not a footnote — a legitimate open question, not disqualifying on
its own.

**VISION SCIENCE's PARTIAL — the one that controlled the final verdict.**
A repo-wide sweep (not just the two sites MF-3 named) found MF-3's own fix
was itself incomplete: `lab/validation/run_all.py`'s `stage21_qext_theory`
docstring — the single most load-bearing, permanent, git-tracked site of
all — stated the 72.6%/PEC-reference comparison with zero MF-3/MF-5 caveat
language. **Independently, MF-1's fix was ALSO only half-applied**:
`lab/qext_theory.py`'s TOP-LEVEL MODULE docstring still carried the exact
disproven "independent numerical proof that this sign/coefficient choice
is right" claim verbatim — only `_self_test`'s own docstring got the
corrected wording. Both findings independently confirmed by the Director
and by Red Team's own re-verification before this ruling.

**Red Team's audit: Checkpoint criterion 4 FIRES, without qualification.**
Iteration 35's own pre-declared, binding tripwire ("a further recurrence
of the caveat-placement pattern is a retroactive Checkpoint-4 trigger, no
further deliberation required") is triggered by this cycle's own two
independent, partial-fix recurrences — the program's 7th-9th confirmed
instance of this defect class (Iterations 17/24/32/33/34/35, now 36
twice), and the FIRST time it has recurred *inside the very cycle whose
mandatory fix was written to close it*. Red Team's ruling: this aggravates
rather than mitigates — a scoped, itemized fix that still misses a site is
stronger evidence the panel's remedy mechanism itself is unreliable than a
cycle that never engaged with the pattern at all. **Overall verdict:
PARTIAL, explicitly OVERRIDING the raw 4-2 PROMISING count** — not on
physics (all four gates, the regression anchor, and every seat's
independent re-derivation stand unchallenged), but because the cycle's own
closing claim (that MF-3 closed the caveat-propagation defect) was false
as documented, in exactly the load-bearing-document class the tripwire
existed to catch. **Verdict is explicitly provisional on Tier-1 fixes
landing same-shift** — applied immediately following this ruling (see
below); once applied and re-verified, Red Team's own stated position is
the verdict "should read PROMISING going forward."

**Tier-1 mandatory fixes, applied same-shift, all zero-new-FDTD**: (1)
`run_all.py::stage21_qext_theory`'s docstring — MF-3/MF-5 caveats now
inline at the 72.6% figure. (2) `qext_theory.py`'s top-level module
docstring — the disproven "independent numerical proof" claim replaced
with the corrected sign-convention-scope-only wording (matching
`_self_test`'s own, now-consistent). (3) `qext_theory.py`'s `__main__`
demo block — MF-5's caveat added alongside the existing MF-3/MF-4
citations. A full repo-wide re-sweep (`grep -rn "72.6%\|independent
numerical proof\|softer edge diffracts less"`) confirms every remaining
hit is either a fixed-with-caveat site or an appropriate historical
quotation inside a mandatory-fix's own writeup (this document's own MF-1/
MF-3/MF-5 paragraphs, quoting the original defect for the record). Full
bench 67/67 green after all three fixes (`--only 12346789,10,11,18,19,20,21`).

**Tier-1 remedy authorized, not yet built (queued, Iteration 37+ scope,
not blocking)**: a mechanical, lint-style caveat-propagation check — grep
every mandatory-fix caveat's own key phrase across every file touched by
that fix's cited sites, not just the sites the fix draft names by hand —
Red Team's own ruling that a fifth wording-only patch would not
distinguish this closure from the six that already preceded and failed to
hold.

**exp-057 erratum (THERMODYNAMICS' new finding, Red Team-ruled a SEPARATE,
non-blocking item)**: `experiments/057-.../NOTES.md` contains a live,
self-contradictory arithmetic error — it asserts "a smaller assumed area
only increases the margin" then computes `699.27/2.367≈295.4x` (division,
decreases) instead of `699.27*2.367≈1655.2x` (multiplication, increases,
matching its own stated direction and this cycle's own independently
code-verified 1655.18x figure). No scored classification changes either
way (both 2+ orders of magnitude clear of NETD-lo). **Directive: a
same-program erratum, three string edits (`NOTES.md`, `run.py`,
`results.json`), executed as a zero-cost rider at the START of Iteration
37, not part of exp-059's own docket** (a different, already-closed
cycle's record; folding it in would blur which cycle owns which fix).

**Checkpoint criteria, all five checked explicitly**: criterion 1 (all
constraint metrics pass) does not fire — no constraint metric scored this
cycle. Criterion 2 (proven boundary) does not fire — this bounds, does not
close, and isn't an unsatisfiability finding. Criterion 3 (engine physics
beyond validated bench classes) does not fire — confirmed zero new FDTD.
**Criterion 4 FIRES** (see above — process, not physics; constraint #3 is
the constraint MF-3/MF-5's caveats gate, the load-bearing reason this is a
criterion-4 matter). Criterion 5 (two consecutive no-result iterations)
does not fire — both Iteration 35 and 36 delivered genuine results.

**CHECKPOINT entry**: written to `LOGBOOK.md` and `SESSION_LOG.md` per
PANEL.md's checkpoint procedure — Marsh is notified. Per Iteration 17's own
direct precedent, this is a notification, not a pause: the Tier-1 fixes
landed same-shift (above), and per Red Team's own explicit ruling this
does not block Iteration 37's unblocked proposal work from continuing.

**Ranked priorities for Iteration 37+** (Red Team's reconciliation of all
six seats — six-way convergence on item 1, a rare unanimity): (1) **The
sharp-uniformly-lossy-disk FDTD control run** — all six seats named this
in their top-3, five as #1; directly resolves MATERIALS' PARTIAL-driving
concern (MF-5), cheap, already scoped. (2) The exp-057 erratum fix (above).
(3) The Tier-1 doc fixes (already applied this shift) plus building the
mechanical propagation-check remedy (an Iteration-37-scoped deliverable,
not just this cycle's hand-applied patch). (4) MATERIALS' absorptivity/
mechanism literature check — now SEVEN cycles deferred, approaching this
program's own escalation pattern; pin it to one checkable question before
an eighth deferral forces an unconditional lock. (5) EM's TE_z companion
series for `qext_theory.py` (mechanical, demonstrates gate 1's
polarization-agnostic tautology numerically, resolves the Hankel-choice
documentation gap). (6) PHOTONICS' T26 lambda/angle generalization /
oblique-incidence Q_ext extension, paired with `graded_black_shell_flagship`'s
own 450/750nm sweep. (7) Carried backlog, unblocked, lower urgency:
shell-vs-solid thermal-mass parameterization (3rd consecutive cycle open);
P-VIS-5's angle-quantization sensitivity formula; QUANTUM's
convergence-guard audit pass across `lab/`'s other closed-form modules for
the "exact-threshold-from-a-wide-bracket" pattern (QUANTUM's own new
Phase-5 finding: the "x=260 exact threshold" claim is itself imprecise,
true NaN onset ≈x=259 — queued, Tier-2, non-blocking); EM's
flank-denominator distribution upgrade.

Full verbatim record: `LOGBOOK.md`, Iteration 36.
