# Phase 2 Critique — THERMODYNAMICS (blind)

## Steel-man (≤150 words)

Not re-running the NETD/energy-sidecar backfill is well grounded. exp-093's
item 5 already measured the absorbed-energy channel at all 14 of exp-092's
Rank-1 cells and found it flat and UNDETECTABLE (5.07×10⁻⁵–5.59×10⁻⁵ K),
"zero surprises," matching R14's own established mechanistic argument that
`ratio_abs_ext` is a smooth, config-invariant partition (<0.1% deviation),
not an oscillatory quantity riding the same near-null structure as
`delta_scene`. This cycle makes no new phenomenon-mechanism claim (T1 N/A) —
it is pure comparability/resolution recalibration on the PRIMARY channel.
Rank 2 sits at a flanking angle well clear of any null; Rank 3's three
angles sit far from any known or suspected node. Building the NETD
machinery for the brand-new `R4` cell layer, only to re-confirm an already
well-evidenced flatness, would be spend without a live question behind it.

## Sharpest attack (≤150 words)

Rank 1 is not "a new angle on an already-characterized grid" — `cpl=40`
(`R4_RATIO=2.0`, cell_ratio=4.0) is a discretization this channel's energy
pathway has *never* been measured at. Item 5's flatness finding was an FDTD
result at `cpl=20/30` only; nothing in this program has shown it is
resolution-invariant, and R15 exists precisely because this sub-thread has
repeatedly found settled-looking features flip under grid refinement
(40.2°/41.4°, 42.0°'s sigma sign flip). Idealization 3 only discloses "no
backfill is run" — it never names the risk that flatness itself is
unverified at `cpl=40`. Worse, Rank 2's §4 commits an explicit `p_abs_w`
check against the 0.51 T9 anchor (2–5% band); Rank 1 — the most expensive,
most novel item — commits **no** equivalent check anywhere in §4, despite
`p_abs_w` already being a `cell_metrics_r4` output at zero marginal FDTD
cost. That is a real, cheap, falsifiable gap left open specifically on the
newest machinery, not on the repeat-resolution items.

## Verdict: **support-with-changes**

## Parameter change that would flip to unqualified support

Add, at zero additional FDTD calls, a `p_abs_w`-vs-0.51-T9-anchor
informational check (2–5% band, mirroring Rank 2's own) computed from
Rank 1's already-planned 32 calls across all six `cpl=40` interior points
plus the settling-gate pair, and add an explicit new Idealization stating
that exp-093's energy-flatness finding is `cpl≤30`-verified only and has
not yet been checked at `cpl=40`. Absent either, I'd move to oppose Rank 1
specifically (Rank 2/3 stand on their own).
