# PHASE 5 — REVIEW · QUANTUM OPTICS · Panel Iteration 48 · exp-071

*Fresh sub-agent, QUANTUM OPTICS charter (PANEL.md seat 5): non-classical
absorption, state-dependent or coherent interactions. Expressibility
contract: mechanisms enter the bench only as effective classical parameters.
Blind to the other five Phase-5 reviews this cycle. No memory of this
seat's own Phase-2 critique of exp-071 (a different fresh instance wrote
it) — read fresh, verified independently, not taken on trust.*

## 0. Verification performed (own re-derivation, not copied from any document)

Re-derived `rayleigh_resolution_ratio` from scratch in a standalone script
(not by reading `design_geometry.py`'s implementation first): converted a
period in θ-degrees to a period in `sin θ` units via the window's own local
linearization `T_sin(P) = radians(P)·cos(θ_center)`, took the frequency
separation `|1/T_sin(P_a) − 1/T_sin(P_b)|`, inverted it to a required
`Δ(sinθ)`, and divided the fixed window `Δ(sinθ) = sin42° − sin36° =
0.081345` by that requirement. Result, independently computed:

| Pair | window | required Δsinθ | ratio (mine) | `results.json` | Match |
|---|---|---|---|---|---|
| C40–C60 | 0.081345 | 1.00630 | 0.080836 | 0.080836 | exact |
| C40–C70/C80 | 0.081345 | 0.85656 | 0.094967 | 0.094967 | exact |
| C60–C70/C80 | 0.081345 | 5.75669 | 0.014131 | 0.014131 | exact |

`trend_resolution_ratio=0.095`, `all_pairs_resolved=False` — **the code's
own numbers reproduce bit-for-bit against an independent implementation.
The math checks out.** Also confirmed the free-period grid step by hand:
`np.linspace(1.0, 4.0, 400)` gives step `3/399 = 0.0075188°`, matching the
figure cited in `phase4_results.md`. Read `run.py::score_trend_and_pairs`
directly (not just its output) to check the boolean logic — see §2 below,
which surfaces a real defect this reading found.

## 1. Was my seat's own Phase-2 finding — and Red Team's extension of it — validated?

**Yes, substantially — with one overclaim in the write-up worth correcting.**

The resolution-floor concern was not moot: every pairwise comparison except
the C70–C80 tie is genuinely unresolved (ratios 0.081/0.095/0.014, all far
below 1.0), exactly as predicted, and Red Team's own extension — that the
CONFIRM band's 30% threshold sits at only 75% of full resolving power — is
the correct, load-bearing generalization; my own Phase-2 critique only
flagged the REFUTE side. Both directions were right to distrust.

But the causal chain phase4_results.md and NOTES.md draw — "the
resolution-floor gate resolves the ambiguity," "decisive" — overstates its
role in *this specific run*. Checking `score_trend_and_pairs` directly:
`raw_confirm` requires `spread≥30% AND R²≥0.50`; `raw_refute` requires
`max_pair_spread≤15% AND R²≤0.30`. The observed `R²=0.8664` already fails
the REFUTE band's own `R²≤0.30` ceiling, and the observed `spread=3.9%`
already fails CONFIRM's `≥30%` floor — **both raw bands were already going
to miss, independent of the resolution-floor gate, from the R² criterion
alone.** The resolution floor is the correct *explanation* for why the
shape is so oddly high-R²-but-tiny-magnitude (a discretization-limited
grid search overfitting a monotone-looking curve to noise inside its own
resolving power), and it is genuinely what will protect a *future* run
sitting closer to either raw band (Red Team's 75%-of-floor CONFIRM-band
point shows the margin there is thin) — but for the Combined Verdict
actually reached this run, "NEITHER" was already locked in by the
pre-committed conjunctive bands before the resolution gate was applied.
Worth a one-line correction in any future citation of this result: the gate
validated correctly and is prospectively essential; it was not the
proximate cause of *this run's* NEITHER.

## 2. A defect this reading found: the exact-tie pair is mis-flagged `resolved=True`

`rayleigh_resolution_ratio`'s own docstring: two identical periods return
`+inf`, described explicitly as "trivially unresolvable AND uninformative
— treated as unresolved by the caller, never as a false REFUTE." I read
the actual caller (`run.py::score_trend_and_pairs`, line 392):
`resolved=bool(ratio >= dg.RESOLUTION_FLOOR_RATIO_THRESHOLD)`. Since
`RESOLUTION_FLOOR_RATIO_THRESHOLD = 1.0` and `inf ≥ 1.0`, the C70–C80 tie
is flagged `"resolved": true` in `results.json` — the **opposite** of what
the function's own documented contract promises. It folds into
`all_pairs_resolved = all(p["resolved"] for p in pairs)` as a `True`.

**Non-load-bearing this run** — the other four non-trivial pairs are
already `False`, so `all_pairs_resolved` is correctly `False` regardless of
the tie's mislabel. But this is a real, verified inconsistency between
documented intent and implementation that will not stay silent forever: a
future reuse of this pairwise machinery on a smaller config set (or one
where the only pairs available happen to include a discretization tie
alongside genuinely resolved pairs) could let an uninformative tie count as
"the most resolved pair of all" toward a REFUTE. Recommend a one-line fix
before `score_trend_and_pairs` is next reused: exclude `p_a==p_b` pairs
from the `all()` reduction, or special-case `ratio==inf` to `resolved=False`
matching the docstring.

## 3. C70/C80 exact tie — same R5 suspicion, or a genuinely different diagnosis?

**Different diagnosis, and I can make it sharper than "plausibly a
discretization tie."** R5 and its Iteration-47 addendum both describe one
specific failure shape: a *dense, unconstrained combinatorial search* over
many candidate matches to an external target, where closeness alone looks
decisive but a null-permutation control shows the match is unremarkable
(exp-051's phase regressor; exp-070's `A_eff`/`A_alt` 36,680-combination
search). That shape requires (a) many candidates, (b) a target being
matched, and (c) a researcher degree of freedom in what counts as "close."

None of those three apply here. `_free_period_search` is run **twice**,
independently, on two **different, fixed, already-collected** datasets
(`C70(θ)`, `C80(θ)`), against the same **deterministic 400-point grid** —
not against each other, and not against an external target. The tie is not
"two things found to be close"; it is `p_star_deg` printing the **exact
same float**, `2.533834586466165`, for both — the two searches landed on
the identical discrete candidate. Given the grid step is `0.0075188°` and
the resolution-floor arithmetic in §0 independently shows the window cannot
separate periods this close (C70–C80's own true best-fit periods, whatever
they are, sit well inside half a grid step of each other at this
resolving power), landing on the same bin is the *expected* outcome of
running an under-resolved discrete search twice on two similar underlying
signals — not a coincidence requiring a look-elsewhere correction. There is
no combinatorial space here for a null-permutation control to run over;
`phase4_results.md`'s "grid discretization" framing is the correct,
different diagnosis, and my own arithmetic (§0, §2) makes it a stronger
claim than "plausibly" — the tie is the mechanical fingerprint of
under-resolution, consistent with (not merely compatible with) the same
resolution-floor finding gating the rest of P-071-2.

## 4. Is "shared-geometry origin" a well-posed alternative? — my sharpest finding this cycle

My charter asks whether a coherent-superposition mechanism is stated with
enough physical specification to be testable. Reading `design_geometry.py`'s
actual `CONFIGS` dict (not just the summary table in the proposal) surfaces
something none of the five blind Phase-2 critiques, Red Team's audit, or
the Phase-3/4 documents name:

```
        ABSORB   PAD   NX    NY    src_x  plane_x  obj_x  obj_y
C40       40      0    360   1584   300     77      170    792
C60       60     20    400   1624   320     97      190    812
C70       70     30    420   1644   330    107      200    822
C80       80     40    440   1664   340    117      210    832
```

**`PAD = ABSORB − 40` exactly, at all four points — perfect collinearity,
by construction** — and every absolute position (`nx, ny, src_x, plane_x,
obj_x, obj_y, y_lo, y_hi`) shifts in lockstep with it. Only the *relative*
quantities are genuinely fixed across all four configs: `A=752`,
`aperture_cells=1504`, `clear_plane=37`, `clear_src=20`, `d_sp=223`,
`lever=93` (and `TAPER`, per exp-070's own finding). This is sound,
deliberate design for isolating a boundary-*depth* effect while holding
relative clearances constant — I am not calling it a flaw in the
congruent-series construction itself.

But it means "shared-geometry, NOT ABSORB-tied" is not actually a single,
well-posed alternative to "ABSORB-tied" **given this specific four-point
series**. The label bundles two physically distinct candidate coherent-
superposition sources that this design cannot tell apart:

1. A source whose length scale is genuinely shared/fixed across all four
   configs (interference between wavelets diffracted at the fixed aperture
   edge and/or `TAPER` boundary — the mechanism the proposal actually
   names) — this candidate *would* predict a flat `P*(ABSORB)`.
2. A source tied to the **PAD/domain-truncation offset** — e.g. a weak
   residual reflection off the graded-loss ramp's own leading edge, whose
   round-trip path length to the aperture grows with `PAD` — which, because
   `PAD` is perfectly collinear with `ABSORB` in this series, would
   predict **the same monotonic P*(ABSORB) trend as a genuine ABSORB-tied
   mechanism would**, for a reason that has nothing to do with absorption
   depth per se.

A properly-resolved run of *this exact series* — even with the resolution
floor cleared — could not distinguish candidate 2 from "ABSORB-depth-tied,"
because no config in the series varies `ABSORB` while holding `PAD` (or
vice versa) fixed. The REFUTE hypothesis, as currently operationalized,
needs a config that decorrelates the two before it is a genuinely
falsifiable alternative rather than a second name for the same trend.

## 5. Why "widen the window" (NOTES.md's own proposed fix) is harder than it reads

I checked whether the per-config independent-fit approach could simply be
rescued with a wider angular window, using the required-`Δsinθ` figures
from §0. For **C60–C70** (the interior, most policy-relevant pair),
resolving them via independent per-config fits requires `Δsinθ ≥ 5.757` —
**exceeding the entire achievable range of `sinθ` (max 2.0, θ∈[−90°,90°])
by nearly 3×; this pair cannot be Rayleigh-resolved by this method at any
physically achievable window.** For C40–C60, the requirement (`Δsinθ ≥
1.006`) just exceeds the *entire positive quadrant* (`θ∈[0°,90°]` supplies
only 1.0) — also impractical, and would abandon the near-normal-incidence
regime this bench idiom depends on (idealization 3, "not a symmetry test").
Only C40 vs. C70/C80 (`Δsinθ ≥ 0.857`) is nominally achievable within
`θ∈[0°,90°]`, but would require expanding the current 6° window roughly
tenfold — a different physical regime, not a tweak. **"Wider window" is not
a viable fix for the two closest, most diagnostic pairs; the per-config
independent-fit method is the wrong instrument for this length scale,
not merely underpowered at the current window.**

## 6. Proposed next move for T28 (concrete, falsifiable)

Two changes, both cheap and both addressing a distinct gap identified
above — neither is a re-proposal of anything RULED OUT:

**(a) Decorrelate PAD from ABSORB.** Add one new congruent-style config
that holds `PAD` fixed while `ABSORB` changes (or the reverse) — e.g.
`C60'`: `ABSORB=60`, `PAD=0` (matching `C40`'s offset, not `C60`'s own
`PAD=20`), same `A=752`/clearances by construction. Run the same 31-point
dense window at 600nm. **Falsifiable test:** if `P*(C60')` tracks `C40`'s
period (not `C60`'s), the trend is PAD/offset-tied, not ABSORB-tied — the
first clean separation of the two candidates named in §4. This is a single
new config, ~16 FDTD calls at the existing cost basis, zero new `lab/`
machinery.

**(b) Replace per-config independent fitting with a direct pairwise
delta/beat fit.** §5 shows the carrier-vs-carrier Rayleigh approach cannot
resolve the closest pairs at any practical window. But T28 was *discovered*
via exactly this alternative: fitting `_free_period_search` directly to a
**difference** signal `δ(θ)=C_b(θ)−C_a(θ)` (as `C80−C40` already was,
`ptp/mean=16.2`, unambiguously significant) is a heterodyne-style
measurement — its resolving requirement scales with the *separation*
between the two underlying periods, which is the quantity actually being
tested, not with independently resolving two nearly-identical carriers
against a fixed external grid. Apply this already-proven-sensitive
methodology to the **adjacent** pairs (`C60−C40`, `C70−C60`, `C80−C70`)
rather than only the endpoints, and score whether each adjacent-pair delta
resolves its own coherent period distinct from T21's 1.9608° fringe. Zero
new `lab/` diff; reuses the exact machinery that found T28 in the first
place, on data (C40/C60/C70/C80 dense sweeps) already fully collected by
this cycle — a same-shift, zero-FDTD-cost analysis, not a new experiment.

## 7. Rating: **PARTIAL**

The underlying `C80−C40` oscillation is real, settled, and — now,
independently reconfirmed at the actual peak cells rather than the
original zero-crossing cells — resolution-robust; nothing here rules it
out. But this cycle's specific causal test (ABSORB-tied vs.
shared-geometry) could not be decided, for two independently-verified
reasons: a genuine Rayleigh resolution floor (validated, §0–1) and a
previously unflagged PAD/ABSORB confound in the experimental design itself
(§4) that would limit even a fully-resolved version of this same series.
Neither finding closes off the phenomenon; both point to concrete,
inexpensive next moves (§6) that were not available before this cycle's
own data existed. T1 remains N/A throughout — no phenomenon constraint is
engaged by this instrument-identification thread, so this cannot be rated
PROMISING regardless of outcome; and the real, well-fit, monotonic
per-config trend (R²=0.87) means RULED-OUT-for-this-approach would overstate
what a resolution-limited null actually shows.
