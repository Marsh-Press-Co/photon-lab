# Phase 2 Blind Critique — ELECTROMAGNETISM

*Panel Iteration 72, exp-095. Independent, blind to other seats' critiques.*

## Steel-man (≤150 words)

The `sigma_max` correction itself is not mere pattern-matching: from
`fdtd2d.py`'s own loss update, `alpha = sigma_e·S/(2·eps_r)` with
`S = courant_frac/√2` held fixed across every resolution family, the
accumulated attenuation exponent over a crossing of `r_out(cells)` scales
as `2·alpha·N ≈ sigma_e·r_out(cells)/eps_r` — the Courant number cancels
exactly. Holding `sigma_max ∝ 1/RATIO` to fix `r_out(cells)·sigma_max` is
therefore a genuine, resolution-independent consequence of the update
equations, not merely dimensional plausibility, and it correctly reduces
to `R3`'s and `R4`'s already-verified values at `RATIO=1.5,2.0`. The
`cpl=50`-over-`cpl=45` choice is also well-reasoned: it is the only option
of the two Red Team offered that keeps Gate 3's bit-exact physical radius,
rather than trading one rounding defect for another. Rank 1's ground-truth
angles are legitimately far from any known null by the record's own
`ratio_k`/floor margins.

## Sharpest attack (≤150 words)

The `sigma_max∝1/RATIO` invariant is only the *leading-order* term of
`ca=(1−α)/(1+α)`'s true accumulated decay,
`exp[−2N(α+α³/3+…)]` — exact only as `α→0`. More importantly, this
program's own record already shows the correction is NOT PRIMARY-channel-
neutral everywhere: exp-092's Rank 3 confirmed cleanliness only at
robust census angles, while exp-093's Item 3 found the identical
correction **sign-flips** `delta_scene` at 42.0° (R4, the fragile
near-null). Rank 2 — this cycle's single largest item (~529 of 744
CPU-min, 71%) — runs the `cpl=50` interior sweep at 41.75°–41.90°
(the analogous fragile near-null band) using CORRECTED sigma exclusively,
with **no native-sigma R5 comparator anywhere in the design** — unlike
Rank 3, which is given exactly that check for R4. A TWO-NODE/SINGLE-NULL
verdict from Rank 2b could itself be a sigma-correction artifact, invisible
to any check this cycle runs, exactly where it matters most.

## Verdict

**Support-with-changes.**

## Parameter change that would flip to full support

Add a native-sigma `R5` leg at one or two of Rank 2b's six interior
angles (4–8 extra calls, budget-trivial against Rank 2's own ~529
CPU-min), mirroring Rank 3a's native-vs-corrected `R4` design — or,
failing that, commit in §5 to reporting any Rank 2b TWO-NODE/SINGLE-NULL
classification as provisional-pending-sigma-check rather than a
free-standing resolution finding.
