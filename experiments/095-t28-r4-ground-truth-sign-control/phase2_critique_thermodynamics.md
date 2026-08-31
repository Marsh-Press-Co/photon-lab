# Phase 2 Critique — THERMODYNAMICS (blind)

**Cycle:** Panel Iteration 72, exp-095 (`t28-r4-ground-truth-sign-control`).
**Seat charter:** where absorbed energy goes; owns the per-proposal energy
sidecar (absorbed power → ΔT → emission band → detectability), expressed as
a post-run analytic calculation, never an FDTD output.

## Steel-man (≤150 words)

The proposal's R16 language is not empty ritual: it correctly identifies
`netd_row()` as a pure extraction function over a `pair_metrics_full`
dict and commits to calling it "at first draft," which is the right fix
target — exp-094's failure was a *timing* failure (post-audit patch), not
a missing function. The go/no-go gate (Rank 1) is genuinely
thermo-adjacent good discipline: it explicitly defers all `cpl=50` energy
spend until sign-recovery is confirmed, so if this cycle's energy
channel *is* mis-wired for the new family, at most 8 calls' worth of
`thermo` dicts are exposed before anyone would notice, not 60. The
"Informational, non-gating, every Rank" `p_abs_w`/`ratio_abs_ext_raw`
band (1–5% of unity, ~1% of the T9 0.51 anchor) is stated up front,
falsifiably, and ported forward unchanged from a three-resolution track
record — exactly the right way to carry an established energy-channel
check into a new grid density rather than re-litigating it.

## Sharpest attack (≤150 words)

The R16-compliance line names only what already exists: `netd_row()`
and `pair_metrics_full` are reused verbatim, and Rank 1/3(b) reuse
`cell_metrics_r4` verbatim too — genuinely low-risk. But Rank 2 (the
`cpl=50` family, the cycle's largest and most expensive item) has **no
named metrics-computation function at all**. §3's parameter table
specifies `r5_config()` as a line-for-line mirror of `r4_config()`
(the geometry-*construction* side, in `design_geometry.py`) but never
names an R5 analog of `cell_metrics_r4` — the function that actually
calls `ts.absorbed_power_established_ratio`/`mixed_length_scale_regime`/
`netd_disposition` and builds the `thermo` dict `pair_metrics_full`
consumes. In exp-094, `cell_metrics_r4` was hand-copied from scratch
(new `box_for_r4`/`ref_for_r4`/`_run_sim_r4_sigma`, R4-specific constants
threaded through by hand) and it was exactly *that* freshly-written
function's silence that let the `thermo` dict compute but never reach
`netd_row()`. Nothing in this proposal shows `cell_metrics_r5` will be
written any differently — the R16 compliance line is a prose commitment
about a function that isn't specified yet, over the one Rank most likely
to reproduce R16's own founding mechanism a third time.

## Verdict: support-with-changes

## Parameter change that would flip to plain support

Add one line to §3 naming the R5-family metrics function explicitly —
e.g. "`cell_metrics_r5(key, th, steps, cap_empty, cap_article)`, a
line-for-line mirror of `cell_metrics_r4` substituting
`R5_*`/`DX_M_R5`/`L_GEOMETRIC_M_R5` constants, with its `netd_row()`
merge written in the SAME diff that adds the function, not a follow-up
edit" — closing the gap the way the geometry table already closes it for
`r5_config()`. Absent that, Rank 2's own energy channel (the settling
check at 7000/10500 steps included — no `p_abs_w` stability check is
named for Rank 2a specifically, only the generic cross-Rank band) should
be spot-verified at Phase 4 before any Rank-2 `delta_scene` reading is
trusted, since a silently-broken `thermo` dict there would be invisible
to Rank 2's own sign-only go/no-go criterion entirely.
