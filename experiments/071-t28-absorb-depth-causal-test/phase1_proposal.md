# PHASE 1 — PROPOSE · Panel Iteration 48 · exp-071
## ELECTROMAGNETISM's C60/C70 `ABSORB`-depth causal falsification test for T28

*Fresh sub-agent, VISION SCIENCE charter (PANEL.md seat 6), lead by rotation
(rotation cycled back after QUANTUM OPTICS led Iteration 47). Executes
PLAN.md's Iteration-48 queue item 1, LOCKED by Red Team's Phase-5 final
audit of exp-070 — a genuine, independently-confirmed 6-for-6 blind-seat
convergence.*

## Mandate

PLAN.md's Iteration-48 queue, item 1:

> **ELECTROMAGNETISM's C60/C70 `ABSORB`-depth falsification test** — the
> already-built congruent configs (zero new `lab/` diff), varying `ABSORB`
> directly across all four points (40/60/70/80) while holding everything
> else fixed, the causal manipulation T28's own desk-check batch (exp-070)
> could not provide. Per Red Team's own Phase-5 final-audit strengthening:
> (a) include EM's own direct cross-config consistency metric
> (`|P*(Ca)−P*(Cb)|/mean`) at every `ABSORB` pair, not only against a
> derived reference; (b) fold in the already-queued, near-zero-cost
> peak-cell R3 resolution recheck (θ≈37.2°/41.4°, 2 calls) at no extra
> cost. Score on the RECOVERED PERIOD at each `ABSORB` depth, and disclose
> the cross-config spread explicitly rather than only a binary
> CONFIRM/REFUTE.

## Mechanism narrative (why this discriminates)

T28 (opened exp-069) is a real, settled ~2.84°-period oscillation in the
`C80−C40` padding delta at θ∈[36°,42°]/600nm that does not match T21's own
established fringe period. exp-070's desk-check batch found the same
~2.8°-family signal lives in `C40(θ)` and `C80(θ)` *individually*
(recovered periods 2.4361°/2.5338°, only 3.93% apart from each other),
which genuinely disfavors an `ABSORB`-depth-tied mechanism relative to a
shared-geometry one — but this reading rests on comparing only **two**
`ABSORB` depths, and Red-Team-confirmed Phase-5 review found the near-match
is more consistent with a compromise fit against T21's own known 1.9608°
fringe (`R²=0.2988`/`0.2645`) than a clean independent confirmation.

This proposal supplies the causal test T28 has never had. `C60`
(ABSORB=60, PAD=20) and `C70` (ABSORB=70, PAD=30) are ALSO congruent
members of the same series exp-065 built (`A=752` cells held fixed for
all four). Running the identical dense 31-point/0.2°-step/STEPS=2800
sweep and free-period recovery exp-069/070 already ran on `C40`/`C80`, now
on `C60`/`C70` too, gives FOUR points on the `ABSORB`-depth axis instead of
two — a genuine manipulation of ONE physical parameter while holding the
rest of the congruent construction fixed.

What discriminates: if the recovered period `P*(ABSORB)` tracks `ABSORB`
depth systematically as it climbs 40→60→70→80 (large pairwise spread,
strong linear trend), that is positive evidence for a genuine
`ABSORB`-depth-tied mechanism — direct physical coupling between the
graded-loss boundary's own thickness and the observed periodicity. If
`P*(ABSORB)` stays essentially flat across all four depths despite
`ABSORB` spanning a 2× range, that argues for a shared-geometry origin
(something common to all four configs — the fixed `A=752` aperture,
`TAPER`, or a discretization-scale artifact) instead, and T28's mechanism
must be sought elsewhere. *(≈280 words)*

## Geometry — verified by running `design_geometry.py` (house rule R4)

Reuses exp-065's `CONFIGS`/`CONGRUENT_KEYS` **verbatim, zero new `lab/`
diff**. `A=752` cells is held bit-identical across all four `ABSORB`
depths (asserted in code):

| cfg | ABSORB | PAD | NX | NY | A | aperture_cells |
|---|---|---|---|---|---|---|
| C40 | 40 | 0 | 360 | 1584 | 752 | 1504 |
| C60 | 60 | 20 | 400 | 1624 | 752 | 1504 |
| C70 | 70 | 30 | 420 | 1644 | 752 | 1504 |
| C80 | 80 | 40 | 440 | 1664 | 752 | 1504 |

R3-rescaled (cpl 20→30, geometry ×1.5, mirrors exp-033's/exp-069's own R3
idiom exactly — same `A` held fixed at the rescaled resolution):

| cfg | ABSORB | PAD | A | NX | NY |
|---|---|---|---|---|---|
| C40_R3 | 60 | 0 | 1128 | 540 | 2376 |
| C60_R3 | 90 | 30 | 1128 | 600 | 2436 |
| C70_R3 | 105 | 45 | 1128 | 630 | 2466 |
| C80_R3 | 120 | 60 | 1128 | 660 | 2496 |

`P(39°, 600nm) = 1.9608°` (T21's established stationary-phase-limit model,
cited context, never scored as ground truth). `DENSE_ANGLES`: 36.0°–42.0°,
0.2° step, 31 points, reused verbatim from exp-069.

**Peak-angle verification** (against exp-069's own already-committed
`block_dense` data, run in code, not hand-picked): θ=37.2° sits at
`|delta|/(ptp/2)=0.949` and θ=41.4° at `0.984` of the window's own
peak-to-peak amplitude — genuinely near the two local extrema, in sharp
contrast to the ORIGINAL R3 leg's cells (θ=39.0°/40.0°, `delta≈1.2e-4`/
`1.7e-4`, near the zero-crossing) that exp-069's own resolution check
actually tested. This closes the exact "near-zero-crossing, not a peak"
gap Red Team named.

## Parameter table

| Block | Angles | λ | STEPS | Configs | Calls |
|---|---|---|---|---|---|
| **G1 (identity gate)** | {39.0°, 40.0°} | 600nm | 2800 | C40, C80 | 4 |
| **DENSE-CAUSAL** (new) | 36.0°–42.0°, 0.2° step (31 pts, reused window) | 600nm | 2800 | **C60, C70** | 62 |
| **R3-PEAK** (new, extended) | {37.2°, 41.4°} | 600nm, cpl=**30** | 4200 (=2800×1.5) | C40_R3, C60_R3, C70_R3, C80_R3 | 8 |
| **Total** | | | | | **74** |

`C40(θ)`/`C80(θ)` over the same 31-point window are ALREADY committed
(exp-069's Block DENSE, 62 calls) — reused via `load_exp069_dense()`, **0
new calls**, gated by Block G1 before trust. Source spec: 2D TMz line
source, single polarization, `cells_per_lambda=20` native / `30` at R3,
`courant_frac=0.99` (all reused verbatim from exp-065/069). Nothing in
`lab/` changes — every config, cost figure, and rescale idiom is imported,
not redefined.

## T1 escape route

**N/A — instrument/mechanism-identification class**, identical in kind to
exp-041/065/066/068/069/070. No mechanism is proposed as satisfying the
phenomenon's four constraints; constraint 3 is not engaged.
**Checkpoint-criterion-2 candidacy: none** — no mechanism class is bounded
here, in either outcome.

## Predictions — committed before any run (house discipline)

| ID | Claim | CONFIRM | REFUTE |
|---|---|---|---|
| **P-071-G1** (identity gate) | θ∈{39°,40°}×{C40,C80}×600nm×STEPS=2800 reproduce exp-069's committed `block_dense` rows exactly (4 values, loaded programmatically). | `ΔC=0.0` for all 4 | any nonzero Δ — **halts the cycle before any other item is scored** |
| **P-071-1** (descriptive, feeds -2/-3, not itself gated) | Free-period grid search — **identical methodology to exp-069/070's `_free_period_search`** (`[1°,4°]` grid, `n_grid=400`, `center_deg=39.0`, fit in `sin θ`) — applied to `C40(θ)`, `C60(θ)`, `C70(θ)`, `C80(θ)` over the 31-pt window. `C40`/`C80` reused from exp-070's already-committed `P*=2.4361°`/`2.5338°` (`R²=0.4327`/`0.4337`); `C60`/`C70` newly computed. | — | — |
| **P-071-2 (HEADLINE — causal trend test)** | Linear regression `P*(ABSORB) = m·ABSORB + c` over the four points `ABSORB∈{40,60,70,80}`. | **CONFIRM (ABSORB-depth-tied):** `\|P*(80)_fit − P*(40)_fit\|/mean(P*) ≥ 30%` **AND** `R²(linear fit) ≥ 0.50` | **REFUTE (shared-geometry, NOT ABSORB-tied):** max over all 6 pairwise `\|P*(Ca)−P*(Cb)\|/mean ≤ 15%` **AND** `R²(linear fit) ≤ 0.30`. **NEITHER** (explicit, computed, disclosed — not a silent default): anything outside both bands. |
| **P-071-3** (required disclosure, item a/d — not independently gated) | Pairwise cross-config consistency `\|P*(Ca)−P*(Cb)\|/mean` at **all 6 pairs** among `{C40,C60,C70,C80}` (C40-C60, C40-C70, C40-C80, C60-C70, C60-C80, C70-C80). | — | — reported **in full, every pair, regardless of P-071-2's outcome** (Red Team item d) |
| **P-071-4 (co-gating, peak-cell R3 — binding precondition)** | Mirrors P-069-5's exact construction, now at the PEAK angles: does `delta(θ)=C80(θ)−C40(θ)` survive cpl 20→30 (R3_STEPS=4200) at θ∈{37.2°,41.4°}? | same sign at both angles **AND** ratio `delta_r3/delta_native ∈[0.3,3.0]` at both | sign flip at either, **OR** ratio outside `[0.1,10]` at either |
| **P-071-5** (disclosed, non-gating extension) | Same peak-cell R3 check, additionally on `delta(θ)=C70(θ)−C60(θ)` at the same two peak angles — extends resolution-robustness evidence into the interior of the ABSORB series (this file's own extension beyond the literal-minimum R3 scope). | — | — context only |

## Combined Verdict — pre-committed, to be computed in code (not prose)

- **HALT** ⟺ P-071-G1 fails. No other item is scored; the cycle stops and
  the reused exp-069 data is not trusted this run.
- **CONFIRMED (genuine ABSORB-depth-tied mechanism)** ⟺ P-071-G1 PASSED
  **AND** P-071-2 CONFIRM **AND** P-071-4 CONFIRM.
- **REFUTED (shared-geometry origin, NOT ABSORB-tied)** ⟺ P-071-G1 PASSED
  **AND** P-071-2 REFUTE **AND** P-071-4 CONFIRM.
- **NEITHER / gray zone** ⟺ P-071-G1 PASSED **AND** (P-071-2 NEITHER **OR**
  P-071-4 REFUTE). This is an explicit, code-computed branch, reported with
  the full P-071-3 spread table and the P-071-1 per-config table attached —
  **not** a silent PARTIAL escape hatch (exp-069's own house discipline,
  VISION's Phase-2 catch at that cycle). If it fires, the honest statement
  is "the causal manipulation could not distinguish the two hypotheses at
  this power," stated as a real finding, not deferred.

P-071-4 is a **binding precondition**, exactly as P-069-4/5 were binding
preconditions on exp-069's own Combined Verdict (that cycle's mandatory fix
1) — a REFUTE or CONFIRM verdict on P-071-2 is not reported as trustworthy
unless the underlying `delta(θ)` signal is independently shown to survive
resolution refinement at a peak, not only a zero-crossing.

## Null-permutation-control question (R5/R5-addendum applicability)

**Not required, stated explicitly.** R5's generalized house rule (RULED
OUT, LOGBOOK) targets a *dense, unconstrained search* over named-constant
or parameter combinations for a match to a target value — the
look-elsewhere problem that inflated exp-051's phase-offset regressor and
exp-070's own `A_eff`/`A_alt` matches. This test is different in kind: it
manipulates **one** already-named physical parameter (`ABSORB` depth)
across **four** already-built, already-fixed congruent configurations —
there is no combinatorial space of candidate explanations being searched,
and no researcher degree of freedom in selecting what to compare against
what. The one adjacent statistical concern — a 4-point linear fit has only
2 residual degrees of freedom, and could in principle over-read a small
sample — is a **power** concern, not a look-elsewhere one, and is mitigated
by requiring P-071-2's CONFIRM/REFUTE bands to be corroborated by the
independent P-071-3 pairwise-spread table (6 pairs, not 1 slope) and the
P-071-4 peak-cell resolution precondition, rather than by a single
regression statistic alone.

## Idealizations

1. 2D TMz, single polarization.
2. **600nm only** — T28's own established scope (exp-069/070); no 750nm
   leg this cycle (a separate, unranked item, not required by the mandate).
3. Positive θ branch only (36°–42°, matching Block DENSE's own window) —
   not a symmetry test.
4. All four congruent `ABSORB` depths (`C40`/`C60`/`C70`/`C80`) engaged;
   `G40`/`N60` (pad-only/naive controls) are T24's own separate question,
   not re-run here.
5. The free-period grid search fits a fixed sinusoidal functional form in
   `sin θ`; a 4-point linear `P*(ABSORB)` trend has only 2 residual degrees
   of freedom — a real statistical-power limit, disclosed, not hidden
   (mitigated per the null-control section above, not eliminated).
6. Bench scale only (`r_out=78` cells) — no witness-scale claim.
7. `A=752` held fixed at native cpl for all four configs (G-2-style
   identity, exp-065, already passed); R3's own `A_r3=1128` is the same
   physical aperture, checked in code (`design_geometry.py` assertion).
8. Single-angle `C_empty` readings, not an N9/N17 aggregate — T25/T26 do
   not apply.
9. `C70`'s `CPU_S_PER_CALL` figure is a **linear interpolation** between
   measured `C60`/`C80` figures (exp-065's own disclosed estimate, not a
   measurement) — used only for wall-clock budgeting below, never for a
   physics comparison.
10. R_contact (PLAN.md queue item 2) remains untouched this cycle — see
    tooling disclosure below; not picked up in parallel, this cycle's
    mandate is item 1 only.

## Tooling disclosure (not this cycle's mandate — stated per Director's instruction)

This session's own tool list includes `WebSearch` and `WebFetch` as
available (deferred) tools. PLAN.md's queue item 2 (`R_contact`'s
`measured_direct` literature search) has been blocked for eight cycles
purely on WebSearch/WebFetch tooling availability in the executing
environment. **This is a capability observed in THIS sub-agent's own
environment, not a claim about the environment any future cycle executing
item 2 will run in** — flagged for the Director to verify and act on if it
holds generally; not attempted here, and not this cycle's mandate.

## `fdtd_budget()` cost estimate — code-produced, `design_geometry.py`

Cost basis reused verbatim from exp-065's measured `CPU_S_PER_CALL` table
(`{"C40":25.0,"C60":31.1,"C70":32.95(interpolated),"C80":34.8}`, 4-worker
`ProcessPoolExecutor` contention included) — not re-measured, per task
instruction.

```
Block G1            calls=  4  cpu_s=239.2
Block DENSE_CAUSAL   calls= 62  cpu_s=3971.1
Block R3_PEAK        calls=  8  cpu_s=1672.0
TOTAL calls = 74
TOTAL cpu_s = 5882.3
wall = 28.76 min   (4 workers, 98% parallel efficiency, 1.15x overhead)
3x envelope = 86.28 min
```

**Hard stop: 90 min** (just above the 3× envelope, matching this program's
own convention of setting the hard stop a few minutes past the computed
envelope, e.g. exp-069's 100 min against a 97.4 min envelope).

**De-scope order if breached (least to most load-bearing), pre-declared:**

1. **First**: retract Block R3-PEAK from the 4-config extension back to
   the literally-queued `C40_R3`/`C80_R3`-only minimum (drops `C60_R3`/
   `C70_R3`, −4 calls). `design_geometry.py::fdtd_budget_minimum()`
   computes this floor in code: **70 calls, 5017.6 CPU-s, wall 24.53
   min**. P-071-5 (the disclosed extension) is dropped; P-071-4 (the
   binding precondition) is unaffected.
2. **Second, only if still breached**: retract Block R3-PEAK to a single
   peak angle (41.4°, the higher `|delta|/(ptp/2)=0.984` fraction) at
   `C40_R3`/`C80_R3` only — P-071-4's CONFIRM/REFUTE bands are then scored
   on one angle instead of two, disclosed as a weaker resolution check if
   this branch is ever taken.
3. **Never de-scoped**: Block G1 (near-zero cost, gates trust in all reused
   data) and Block DENSE-CAUSAL (`C60`/`C70`'s dense sweep — the entire
   causal manipulation this cycle exists to run). If budget cannot cover
   these two, the correct action is to halt and re-propose, not to trim
   them.

## Gates

Full bench (`lab/validation/run_all.py`) reconfirmed green before any panel
work, per house convention (heavy stage 5 optional). Zero `lab/` diff
throughout this design — every config, rescale idiom, and cost figure is
imported from exp-065/exp-069, never redefined. P-071-G1 is the one local
**absolute-identity** gate; it gates every other number this cycle
produces.
