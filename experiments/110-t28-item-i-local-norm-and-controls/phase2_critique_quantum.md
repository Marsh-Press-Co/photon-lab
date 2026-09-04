# PHASE 2 — CRITIQUE · QUANTUM OPTICS · Panel Iteration 87 (exp-110)

*Blind to all other seats' Phase-2 output. Charter: non-classical
absorption / state-dependent or coherent interactions; expressibility
contract N/A this cycle (no σ(I)/σ(x,t)/ε(ω)/gain mechanism is proposed —
confirmed, §3 of the proposal, structurally correct). Per the Director's
brief, this review leans on the from-primitives statistical/logical audit
role this seat has carried in recent T28 cycles.*

## Independent recomputation — item 2's four synthetic sequences

Loaded `linear_fit_1_over_margin` directly from the real committed
`experiments/108-.../run.py` via `importlib.util.spec_from_file_location`
(the proposal's own idiom) and invoked it on P1/P2/P3/N1 exactly as
specified — no hand arithmetic anywhere. **All four reproduce bit/decimal-
exact to the proposal's own table:**

| Case | is_monotonic | r_squared | residual_std | smooth |
|---|---|---|---|---|
| P1 | True | 1.000000 | 3.6158e-21 | True |
| P2 | True | 0.397147 | 1.4121e-05 | True |
| N1 | False | 0.096971 | 2.8508e-06 | False |
| P3 | False | 0.912047 | 1.1179e-06 | True |

R4 satisfied — these are genuinely committed-function outputs, not
hand-typed. The OR-arm isolation claims also check out mechanically: P2 is
smooth *only* via `is_monotonic` (R²=0.397 fails the 0.90 bar alone), P3
*only* via R² (monotonicity fails), N1 clears neither. This is a clean,
correctly-designed fault-injection control for `linear_fit_1_over_margin`
itself — scoped honestly (it tests the function, not its two downstream
callers' consumption of `smooth`, and the proposal never claims otherwise).

## Item 1's local-normalization construction — a new R13/R14-shaped hazard

I checked `lab/sections.py`'s `angular_scattered_pattern()`: both the
peccored and hollow patterns are `pt - pi` (article minus empty) binned
over the **identical outer-shell Cartesian perimeter grid** — only the
core fill differs. This matters: `classify_item_i_local`'s floor,
`K * max(mirror_floor(peccored)[bin], mirror_floor(hollow)[bin])`, is a
**single-realization, per-bin, per-margin** point estimate of a quantity
whose true expectation is zero everywhere (the bench is genuinely
mirror-symmetric). Any single such estimate has real, non-negligible
probability of landing near zero purely by chance at some bins — and
because peccored/hollow share the same shell discretization, their
mirror-asymmetries are correlated, not independent draws, so `max(...)`
does not buy the robustness it appears to. Where this happens the floor
collapses toward zero, `RESOLVED` becomes nearly automatic (any nonzero
`|peccored[bin]|` clears it), and `local_rel = |delta|/|peccored|`
re-opens exactly the division-by-near-zero hazard R13 exists to gate —
now hidden behind a floor that *looks* like it discharged R13/R14 but is
itself an unaggregated noise estimate. Nothing in the proposal pools the
floor across the 6 available margins or across bins to guard against
this — the "joint gate" (AND across peccored/hollow) closes R13's
original denominator concern but not this one.

## Steel-man (146 words)

Item 2 is genuinely rigorous: a from-primitives, deterministic,
seed-free fault-injection control that correctly isolates both arms of
`linear_fit_1_over_margin`'s OR-logic (monotonicity vs. R²≥0.90), closing
the R18 gap this program has now flagged three cycles running
(exp-108→109→this proposal), scoped honestly to the function it actually
tests. The §0.5 grounding-fact finding (the Iteration-86 queue's "zero
new FDTD" premise for item 1 is false) is exactly the verify-before-claim
discipline this program demands — checked three independent ways
(filesystem search, `results.json` field audit, cross-cycle Phase-5
citation) before being acted on, not asserted. Item 1's joint
peccored-AND-hollow floor gate is a real structural improvement over
prior single-parent gating, its informational-only scoping correctly
avoids folding a first-use instrument into a frozen verdict (the exact
R24 shape), and its own R18 gap is honestly named as deferred, not
silently assumed closed.

## Sharpest attack (150 words)

`classify_item_i_local`'s floor is a single-sample estimate of a
zero-mean-in-expectation quantity (mirror asymmetry on a genuinely
symmetric bench), computed once per bin per margin per pattern, with no
pooling across the 6 margins or the 24 available bin-pairs that would
let a spuriously-low draw be caught. Worse: peccored and hollow share the
*identical* outer-shell grid discretization (`angular_scattered_pattern`
only differs by core fill), so their mirror-asymmetries are correlated,
not independent — `max(mirror_floor(peccored), mirror_floor(hollow))`
does not deliver the two-independent-draws robustness it implies. At any
bin where this correlated single-sample floor happens to read low
(plausible precisely at the low-cross-section bins motivating this
instrument — PHOTONICS' own 62.5%-of-bins finding), `RESOLVED` becomes
near-automatic and `local_rel=|delta|/|peccored|` reopens R13's
division-by-near-zero hazard behind a gate that appears, but does not
actually, discharge it. This is a construction-level flaw the deferred
Iteration-88 fault-injection control might not even catch unless its
synthetic test specifically includes a near-coincidental true-symmetry
case.

## Verdict: support-with-changes

Item 2 and the §0.5 grounding-fact correction should proceed as
specified. Item 1c/1d's floor should not be reported, even
informationally, without first replacing the single-bin/single-margin
point estimate with a pooled one (e.g. median or a stated percentile of
`|pattern[i]-pattern[47-i]|` across all 24 pairs, or across the 6
margins for that bin) — otherwise a future citation of "bin X is
RESOLVED with N% local deviation" cannot be distinguished from an
artifact of a lucky near-symmetric noise draw. Item 3's truncation
control is sound and low-risk; no objection.

**Single parameter change to flip verdict to support:** replace
`floor = K * max(mirror_floor(pattern_peccored)[bin],
mirror_floor(pattern_hollow)[bin])` with a floor built from a pooled
statistic (e.g. `K * median` or a stated percentile of the per-bin
mirror-asymmetry array, computed once per pattern rather than reused
per-bin) — closing the single-point-estimate gap without expanding this
cycle's scope.
