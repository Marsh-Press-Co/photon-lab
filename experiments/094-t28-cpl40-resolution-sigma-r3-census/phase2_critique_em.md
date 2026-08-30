# PHASE 2 — CRITIQUE · ELECTROMAGNETISM (blind) · exp-094 · Panel Iteration 71

*Fresh sub-agent, ELECTROMAGNETISM charter. Read in full: PANEL.md;
LOGBOOK.md (RULED OUT R1–R15, LIVE THREADS, full T28 history including my
own seat's exp-093 Yee-dispersion-length finding and the exp-091/092
`sigma_max` confound discovery and correction); PLAN.md's Current-state
section; `experiments/094-.../phase1_proposal.md`;
`experiments/093-.../NOTES.md`/`run.py`; `experiments/092-.../run.py`
(origin of `SIGMA_R3_CORRECTED`); `experiments/091-.../run.py`;
`experiments/069-.../design_geometry.py`; `lab/materials.py::
graded_black_shell`/`_graded_black`; `lab/fdtd2d.py::Sim.__init__`/`run`
(the actual E-update: `alpha = sigma_e*S/(2*eps_r)`,
`ca=(1-alpha)/(1+alpha)`). Blind to every other seat's current critique.*

## Independent re-derivation, done before trusting the proposal's own algebra

`fdtd2d.py` states its own convention explicitly: "grid units (dx=1,
c=1)." Given that, and `S = courant_frac/√2` held numerically fixed
across every `cpl`, the loss coefficient `alpha = sigma_e·S/(2·eps_r)` is
the discretized form of `sigma_phys·dt/(2ε)`, which forces `sigma_e`
(code) `= sigma_phys·dx/(c·ε₀)` — i.e. code-`sigma_max` carries an
implicit factor of `dx`. `r_out(cells) = R_out_phys/dx` carries the
inverse factor. So `sigma_e·r_out(cells) = sigma_phys·R_out_phys/(c·ε₀)`
is **exactly `dx`-invariant** — a real, `cpl`-independent physical
quantity (the shell's true accumulated optical depth, up to the fixed
`2×`/grading-profile constant). Re-deriving from this, for *any* ratio
`R` between native and a rescaled family: `sigma_e(R)·[R_out_native·R] =
sigma_e_native·R_out_native` ⇒ `sigma_e(R) = sigma_e_native/R`. This
reproduces `SIGMA_R3_CORRECTED=1/3` at `R=1.5` (matching exp-092's own
`78.0/(2·117)`) **and** falls out of the identical algebra at `R=2.0`
with no new assumption — the generalization is a genuine re-derivation
from the update equation's own physics, not a pattern extrapolated from
one data point. On this specific question the proposal's Idealization 18
is too modest about its own footing.

## Steel-man (≤150 words)

The `sigma_max` rescale is sound EM bookkeeping, independently
re-derived above from `fdtd2d.py`'s own loss-update coefficient rather
than accepted on the proposal's algebra: because code-`sigma_max`
implicitly carries a factor of grid spacing under this bench's `dx=1,
c=1` convention, `sigma_max·r_out(cells)` is the `cpl`-invariant proxy for
the shell's *real* accumulated optical depth, and `SIGMA_CORRECTED(R) =
SIGMA_NATIVE/R` is the general closed form for holding that fixed at any
ratio, not a coincidence tied to `R=1.5`. The proposal also directly
answers a standing gap my own seat named at exp-093 Phase-5 (`run.py`'s
"continuous curve across 41.6°–42.0°" mixed native- and corrected-sigma
points with no single physical basis) — Rank 2 finally builds an
all-corrected-sigma curve at that window. Rank 3's native-sigma choice is
correctly scoped: no null is known or suspected at 36.0°/38.4°/38.8°, so
skipping the correction there is not the same omission R15 exists to
catch.

## Sharpest attack (≤150 words)

§2.4's gates check *consequences* of the correction, never the
correction's own defining invariant. Gate 3 checks physical shell radius
in meters; gate 4 checks `SIGMA_R4_CORRECTED==0.25` as bare arithmetic.
Neither directly asserts `2·SIGMA_R4_CORRECTED·R4_R_OUT ==
2·SIGMA_NATIVE·R_OUT` (`=78`, by hand) — the actual `τ_center`
preservation the whole correction exists to buy. That's a real gap, and
`RATIO=2.0` makes the existing gates a *weaker* substitute than they were
for R3: doubling any native integer is exact, so unlike R3 (whose own
recipe forced two half-integer roundings, `PLANE_X`/`GUARD_OUT`), every
R4 constant satisfies its own arithmetic identity trivially regardless of
whether `τ_center`-preservation is still the right criterion at this
ratio — the one gate that would actually discriminate a wrong physical
argument from a right one is the one gate not written. Fix: add
`assert abs(2*SIGMA_R4_CORRECTED*R4_R_OUT - 2*SIGMA_NATIVE*R_OUT) < 1e-9`
as a fifth mandatory gate, before any Rank-1b call.

## Secondary point: the sequencing claim doesn't fully hold under EM's own standard

"No item gates another's parameter" is true narrowly (no item *sets* a
literal parameter for another), but it isn't the same as no coupling.
Rank 2's informed CONFIRM lean rests on 41.6° sitting "well inside the
curve's own positive lobe, not adjacent to a near-total... null" —
that's a claim about where the null's *edge* sits, established only at
`cpl=30`. Rank 1 is the first check of whether that edge moves under
resolution refinement at all (its own predicted outcomes disclose
exactly this risk for the interior). If Rank 1b returns TWO-NODE
CONFIRMED or a trough that reads as widened/shifted toward 41.6° at
`cpl=40`, Rank 2's own "comfortably outside the null" framing needs
retroactive re-reading, even though none of Rank 2's own numbers change.
Running Rank 2 before Rank 1 is fine on cost grounds; reporting Rank 2's
qualitative lean as settled before Rank 1 completes is not — the
proposal should flag Rank 2's interpretive framing (not its data) as
provisional pending Rank 1b, symmetric to how it already treats Rank 1a
as gating Rank 1b.

## Branch-gating / passivity check

`sigma_max` enters `graded_black_shell` as `sim.sigma_e[shell] +=
sigma_max·sig/0.5` — a strictly non-negative additive real conductivity
at every `sigma_max∈{0.5, 1/3, 0.25}` tested here (`_graded_black`'s
`sig` is a smoothstep-squared quantity, non-negative by construction).
No branch in this proposal introduces gain, negative loss, or a
non-causal update coefficient; `ca=(1-alpha)/(1+alpha)` stays in `(0,1)`
for all three values. No T1/passivity objection to any of the three
`sigma_max` values used across Ranks 1–3.

## Verdict: **support-with-changes**

The `sigma_max` generalization to `R4_RATIO=2.0` is physically sound —
independently re-derived here from the engine's own loss-update
equation, not merely reproduced algebraically — so I do not object to
the mechanism. But the identity-gate set as written checks the
correction's downstream footprints, not the `τ_center` invariant itself,
and at `RATIO=2.0` specifically that omission is closer to a rubber
stamp than a test (every derived constant passes its own arithmetic
trivially by construction). And Rank 2's PRIMARY-channel interpretive
lean should be marked provisional pending Rank 1b's outcome, not
reported as settled ahead of it.

**Single change that would flip me to full support:** add the direct
`τ_center`-invariance assertion (`2·SIGMA_R4_CORRECTED·R4_R_OUT ==
2·SIGMA_NATIVE·R_OUT`) as a fifth mandatory §2.4 gate before Rank 1b
executes, and add one sentence to Rank 2's §4 prediction marking its
"well inside the positive lobe" framing as provisional pending Rank 1b's
own outcome.
