# Phase 2 Critique — PHOTONICS (blind)

*Panel Iteration 76, exp-099. Independent verification performed against
source before writing this critique (not just proposal prose): item 1's
four filed Null C `delta_scene` values and the derived deceleration ratio
`r₃=|Δ₃|/|Δ₂|` were recomputed directly from
`experiments/098-.../results.json::item_i.C.report` (all four values and
`r₃=0.1240`, the ~8.06× slope drop, reproduce exactly); item 2's claim
that no R5 data exists near Null B was confirmed from
`experiments/095-.../results.json` (`rank2_calls=0`,
`rank2.skipped=True`, `reason="Rank 1 combined go/no-go gate did not
PROCEED"`), and the cited `shift_20_30`/`shift_30_40`/`observed_ratio`
figures for Null B reproduce exactly from
`experiments/098-.../results.json::richardson_diagnostic.B`; item 3's
θc=69°/75°/77°/5° `ptp` values and the 6630.99×/311×/621× ratios
reproduce exactly from
`experiments/086-.../phase4_rescore_results.json::method_c_rescore.sub_results`,
as does the 235.396×-at-θ=66.0° GP2′ peak and the non-recovering
12.2×–78.5× 74°–89.5° tail from
`experiments/098-.../results.json::item_v.gp2_curve`. Every load-bearing
number I checked survived independent recomputation.

## 1. Steel-man

Item 3 is exactly on this seat's charter: it extends the closed-form
diffraction model's angular coverage to the untested 79°–87° window,
right up against the aperture-grazing limit (90°) where a missing
UTD/shadow-boundary correction term is most consequential — and it does
so with a pre-registered, falsifiable shape criterion (recovery-vs-
persistent-elevation) rather than a magnitude-only comparison, correctly
distinguishing "differing statistic" from "differing physics" as two
genuinely different hypotheses. Item 1's bracket direction and width are
derived from Null C's *own* measured cpl20→cpl30 shift (+0.320°/+0.377°,
both upward) rather than borrowed by analogy from a differently-signed
feature — the right angular-dependence discipline, and a direct,
disclosed improvement on R17's founding failure mode. Every headline
number I independently recomputed reproduced exactly.

## 2. Sharpest attack

Item 1's pre-registered VANISHING-AMPLITUDE criterion (`r_i<0.5` at all
3 new points) cannot discharge what it claims to discharge, for a
reason the proposal's own Idealization 53 does not reach. `delta_scene(θ)`
is *this program's own* independently, `p=0.0`-null-controlled,
established oscillatory curve (LOGBOOK R13/T21: period `P_edge_A≈2.8421°`,
confirmed repeatedly, `experiments/083`). A monotonically decelerating
but still-positive run over a window is the textbook signature of a
curve flattening toward a local EXTREMUM of a periodic function, not of
an asymptote — and it is indistinguishable, by `r_i<0.5` alone, from
"this is one lobe of the known ~2.84° oscillation, and the next real
zero-crossing sits beyond the tested span." The new bracket's own
half-width (1.500°) is only ~53% of that established period — R17
compliance was checked against cross-resolution *migration* shifts
(0.320°–0.377°), the wrong yardstick for this specific question; against
the curve's own *period*, 1.5° is not obviously wide enough to rule out
the same-lobe explanation, and a half-period-scale zero-crossing
(~θ0+1.42°=42.88°) would land inside, not past, the newly tested span —
meaning the pre-registered scoring rule is at real risk of stamping
ordinary oscillatory curvature as physical decay-to-zero.

## 3. Verdict

**support-with-changes**

## 4. Parameter change that would flip to support

Replace the bare `r_i<0.5`-at-3-points VANISHING-AMPLITUDE trigger with
one that also requires the tested half-width to exceed roughly one full
established period (`≥~2.84°`, i.e., extend the upward bracket step
count, or explicitly fit the 7-point curve against the known
periodic/decay alternative) before VANISHING-AMPLITUDE — rather than
INCONCLUSIVE-consistent-with-same-lobe-oscillation — is reported as the
outcome.
