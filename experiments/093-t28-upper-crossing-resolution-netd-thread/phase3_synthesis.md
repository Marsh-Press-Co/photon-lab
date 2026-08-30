# PHASE 3 — SYNTHESIS · Panel Iteration 70 · exp-093 · Director: photonlab-shift (cloud panel routine)

*Director role per PANEL.md: synthesizes, does not vote in Phase 2, states
which criticisms are accepted/overridden and why. Before freezing any
prediction, independently re-verifies Red Team's own disputed numbers —
not adopted on trust — matching this sub-thread's own established
practice (exp-090/091/092 precedent).*

## 0. Independent Director-level re-verification of RT-1 and RT-2

Both disputes were re-derived a THIRD time, independently, from primary
source, before being adopted (Bash/Python, this session):

**RT-1 (AUC sign convention).** Reimplemented `auc()` verbatim from
`experiments/090-.../run.py:55` and ran both calling conventions against
the proposal's own n=8 table:
`auc(-pos,-neg)=1.0000` (exp-090's own convention, matches its own
`AUC=1.0000` result); `auc(pos,neg)=0.0000` (the proposal's own reported
"reversed" figure — a different question, not a different answer to the
same one). `zone_lo=max(pos)=4.1083`, `zone_hi=min(neg)=5.4287` reproduce
the proposal's own §6 zone bit-exact, using `run.py`'s own unconditional
formula, no swap needed or made. **Bit-exact match to Red Team's own
RT-1 figures. UPHELD, independently, a third time.**

**RT-2 (dispersion length scale).** Confirmed `A_HALF_APERTURE=752`
(`experiments/069-.../design_geometry.py:112`) is the actual committed
value both of EM's own prior citations (exp-091/exp-092
`phase5_review_em.md`) name, not a figure taken from either party's
prose. Reimplemented the Yee-grid dispersion solve (Brent's method) from
the proposal's own §7 formula independently and confirmed it reproduces
the proposal's own `ℓ=2×PAD` table to the stated precision. Then
recomputed at `ℓ=A` (752 cells native / 1128 at R3):

| θ | observed Δθ | ratio at `ℓ=2×PAD` | ratio at `ℓ=A` (Director's own, independent third derivation) |
|---|---|---|---|
| 40.0718° (lower) | −0.194° | 301.8× | **32.1×** |
| 41.7811° (upper 1) | +0.320° | 754.0× | **80.2×** |
| 41.8377° (upper 2) | +0.377° | 900.4× | **95.8×** |

**Bit-exact match to Red Team's own approximate figures (32×/80×/96×),
now exact rather than approximate — Red Team's own table was explicitly
disclosed as a directional cross-check; this is the properly-sourced
Phase-4-grade computation Red Team itself asked for.** Confirms RT-2 in
full: at the mandated length scale, the lower crossing's own ratio
(32.1×) does **not** clear the proposal's own pre-registered
"100×–1000×, at least two clear orders of magnitude" REFUTE band — this
is the "more important finding" both EM's critique and Red Team's audit
anticipated, now settled rather than merely flagged. All three ratios
DO clear a one-order-of-magnitude bar (≥10×) cleanly, so the qualitative
REFUTE conclusion survives; the proposal's own quantitative band claim
does not, and is corrected below (§3, item 4).

## 1. Criticisms accepted (all six of Red Team's mandatory fixes — zero overridden)

1. **RT-1 fix, adopted verbatim.** "REVERSED"/"opposite decision rule"/
   "roles of max/min swapped" language struck. Corrected finding: the
   n=8 `cpl=30`-only sample preserves the SAME lower-margin-predicts-`Y=1`
   relationship as the original n=7 `cpl=20` sample (`AUC=1.0000` under
   the consistent convention both datasets share), zone `[4.1083,5.4287]`
   — a real, independently valuable, non-contradictory finding on its own
   terms. Idealization 15 and the Phase-4 reproduction gate corrected to
   certify this direction.
2. **RT-2 fix, adopted, extended by the Director's own third
   derivation (§0 above).** §7's table now reports BOTH length scales
   side by side, `ℓ=A` (752/1128 cells, sourced directly from
   `design_geometry.py`) as PRIMARY (the actually-named mandate),
   `ℓ=2×PAD` relabeled explicitly as a secondary computation against a
   *different*, previously-REFUTEd echo mechanism (exp-077's own
   `pad_round_trip_echo_model`, two-wall `r²=0.0001` for `PAIR_PAD` —
   cited now as what it is, not as supporting grounding). §13's R8 bullet
   reworded: the mandate IS now discharged — `ℓ=A` was actually computed,
   third-citation-avoided — but the discharge finding is a REFUTE at
   one order of magnitude (32×–96×), not the proposal's own originally
   predicted two-order-of-magnitude band. The falsifiable prediction
   (§4 below) is corrected to match what was actually run, not what was
   hoped for.
3. **RT-3 fix (R15-completion overclaim), adopted verbatim** (MATERIALS'
   own offered wording). §13's R15 bullet reworded from "direct
   completion" to: *"items 1/2 are a further, `cpl=30`-verified step
   toward R15's founding mandate — not its completion. Two discharge
   conditions remain open: three of exp-090's seven original points
   (36.0°, 38.4°, 38.8°) still have no `cpl=30` measurement, and no
   `cpl=40` comparator exists anywhere on this channel to confirm
   `cpl=30` itself is converged rather than merely a second, different,
   fixed resolution."*
4. **RT-3 fix (angular-vs-spatial conflation), adopted verbatim**
   (PHOTONICS' own offered wording). New Idealization 16 added (§5
   below): item 1's three-way outcome is angular-only (fixed `cpl=30`)
   and does not itself constitute an R15-grade cross-resolution finding.
   Item 2's gate (§6 of the proposal, reproduced in NOTES.md) reworded so
   a TWO-NODE CONFIRMED or SINGLE-NULL extension is reported as
   provisional pending a future spatial (`cpl=40`) check at the interior
   near-null angles specifically.
5. **RT-4 fix (disclaimer erosion), adopted verbatim.** Inline
   `(NETD/instrument, not human-eye)` qualifier added at both bare
   "detectability"/"undetectable" occurrences in the Hypothesis section.
   Carried-idealizations banner extended to include Idealization 1 (2D
   TMz, single λ=600nm) and Idealization 8 (the still-open unbiased
   margin-vs-distance rebuild), alongside the previously-cited 3/6/7/11.
6. **Minor batch, adopted.** MATERIALS' `sigma_max=1/3` disambiguating
   note (numerical rescaling, not a `REALIZABILITY_MEMO.md` claim) carried
   forward. VISION's `NETD_BAND_K=(0.020,0.050)` provenance pointer
   (Iteration-20/exp-043) added inline. QUANTUM's R14-bullet tightening
   applied (item 5 reproduces 40.0°'s already-scored fields bit-exact;
   the NETD sidecar itself, for all 14 cells, is the new content).

**Zero criticisms overridden.**

## 2. A Director-caught defect of the Director's own (checked for, per this
sub-thread's own established pattern — Iterations 67/69 both had one)

Checked explicitly for: (a) whether item 4's corrected `ℓ=A` band change
propagates consistently everywhere the old `301×–900×` figures were
quoted (NOTES.md draft below uses the corrected figures throughout, no
stale copy found); (b) whether item 2's `n=8` table membership is
affected by the RT-1 fix (it is not — the fix corrects only the AUC/
direction language, not zone membership or the underlying margin/Y
table, which was never in dispute); (c) whether the `ℓ=A` recomputation
changes item 4's own Idealization-12 language ("one pre-declared,
physically motivated candidate, not an exhaustive accounting") — it does
not, since `ℓ=A` was itself one of the two candidates already named by
EM's own prior reviews, not a new one invented at Phase 3. **No
additional defect found this cycle** — the six-item docket plus the
Director's own independent third derivation appear to close every open
question raised at Phase 2. (Stated explicitly, not silently: absence of
a Director-caught defect is itself checked and reported, not assumed.)

## 3. Corrected item 4 falsifiable prediction (supersedes phase1_proposal.md §11)

**(Item 4) PRIMARY, corrected.** Predicted (before Phase 4's committed
desk script runs): the desk script reproduces the `ℓ=A` table (§0 above)
to ≥4 significant figures, and the magnitude ratio (observed vs.
predicted |Δθ|, at `ℓ=A`) stays in the **`10×`–`200×`** range at each of
the three angles with a known observed crossing shift — a REFUTE of the
dispersion-alone mechanism by at least one clear order of magnitude, not
the originally-claimed two. **CONFIRM** = reproduces to ≥4 significant
figures and the ratio band holds. **REFUTE of THIS band** = the recomputed
ratio falls outside `10×`–`200×` at any of the three angles — itself a
significant, unanticipated finding, investigated not smoothed over. The
`ℓ=2×PAD` computation is retained and reported as a secondary,
explicitly-relabeled result (a real REFUTE of the *different*,
already-refuted `pad_round_trip_echo_model` echo mechanism specifically),
not substituted for the mandate.

## 4. Everything else in phase1_proposal.md stands unmodified

Items 1, 2 (base table + gate, as reworded per §1.3–1.4 above), 3, 5, the
full parameter table (§8), the sequencing (§2: 5→3→1→2→4), the budget
(56 calls, 188.4 CPU-min), and §13's R1–R14 bullets (unaffected by any
of the six fixes) all stand as proposed. `NOTES.md` (this cycle's frozen
document) incorporates every fix above and is committed to git strictly
BEFORE any Phase-4 script executes, per house discipline.
