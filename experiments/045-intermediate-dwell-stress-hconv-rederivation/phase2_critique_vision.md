# PHASE 2 — CRITIQUE · VISION SCIENCE (blind) · exp-045, Panel Iteration 22

## Steel-man (≤150 words)

The proposal gets the *scope* discipline right where it matters most: T1
escape route is explicitly "NONE," the narrative states up front this is
instrument-characterization, not a constraint-3 ambient-appearance test,
and the Idealizations section (`phase1_proposal.md` lines 233–235)
contains the correct, complete, word-for-word disclaimer: "NETD is an
instrument/detector threshold, not a human perceptual one … nothing in
either block bears on constraint-3/4's human-eye verdict." No claim
anywhere states or implies a human-eye verdict — Block A stays inside
`coupled_kinetics_thermal_dT`/NETD space throughout, Block B never touches
ambient contrast, adaptation, or glare. Correctly, this cycle does **not**
trigger my own Iteration-23 glare/adaptation Tier-W tripwire early — there
is no ambient-silhouette scene here to trigger it, and Red Team's own
Iteration-21 close already ruled REJECT-AS-OVERREACH on any acceleration
absent new cause. This cycle gives none.

## Sharpest attack (≤150 words)

`run.py` line 258 calls `ts.netd_disposition(exact_dT, NETD_BAND_K)`,
which — per its own docstring and Iteration-20's mandatory fix — returns a
dict carrying a `"disclaimer"` field specifically so callers don't have to
retype it. Line 268 then stores only `netd["classification"]`, **discarding
the disclaimer the function auto-attached**, at all 1664 sweep points.
Contrast exp-044 (`run.py` line 166), which stored the whole `netd_b` dict
per point. The proposal's own disclaimer (phase1_proposal.md lines 233–235)
appears exactly once, in Idealizations, never inline at P-EM45-A1/A2's
actual NETD-comparison claims; `block_a["netd_disclaimer"]` (run.py line
343) is block-scope only, and none of the console prints (lines 397–421)
mention it — the identical "thorough in results.json, absent from prose/
prints" gap I self-caught at Iteration 20, and the identical "stated once
in Idealizations, absent at points of claim" gap Red Team fixed at
Iteration 21 (mandatory fix 6). This is a regression to the pre-fix
pattern, at 100x the point-count (1664 vs 16), and matches VISION's own
Iteration-21 finding that all 4 prior recurrences happened at the
logbook-summarization step — the exact failure mode this cycle reopens.

## Verdict

**support-with-changes**

## Single parameter change that would flip to unconditional support

Stop discarding `netd["disclaimer"]` — store the full `netd_disposition()`
return dict (or at minimum its `"disclaimer"` field) at every sweep point
in `results.json`, add the disclaimer text to at least one console print
line adjacent to the `all_points_undetectable_or_better` line, and inline
the one-sentence disclaimer at P-EM45-A1 and P-EM45-A2 in
`phase1_proposal.md` Section 4 (not only in Idealizations) — matching
exp-044's already-established, Red-Team-mandated propagation standard
exactly, not merely gesturing at it once.
