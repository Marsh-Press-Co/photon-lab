# exp-093 — T28 Upper-Window Crossing Resolution & NETD Threading

*Panel Iteration 70. Lead seat: THERMODYNAMICS. Runner: photonlab-shift
(cloud panel routine). Full phase record: `phase1_proposal.md`
(THERMODYNAMICS) → five blind Phase-2 critiques (PHOTONICS, MATERIALS,
ELECTROMAGNETISM, QUANTUM OPTICS, VISION SCIENCE, unanimous
support-with-changes, two load-bearing cross-review catches) →
`phase2_redteam_audit.md` (PROCEED-WITH-MANDATORY-FIXES, 6 items, zero
overridden, both disputed claims independently re-derived from primary
source) → `phase3_synthesis.md` (this cycle's frozen spec, all 6 fixes
adopted, Director's own independent third-derivation of both disputed
figures, bit-exact match to Red Team's own).*

## Hypothesis

exp-092 (Iteration 69) located the `cpl=30` lower `delta_scene`
zero-crossing (`40.0718°`) and found a new, unresolved double-crossing
structure in the upper window (`41.7811°`/`41.8377°`, `0.057°` apart,
straddling a `NODE-UNRESOLVABLE` near-total interference null) — status
(genuine two-node feature vs. under-resolved single null) explicitly
undecided. Every prior T28 cycle since exp-087 has scored
`delta_scene`/`frac_contrast` — a coherent phase/timing quantity — while
treating `p_abs_w`, the absorbed-power channel THERMODYNAMICS owns, as a
downstream ratio rather than a persisted physical quantity: individual
`p_abs_w`/`dt_ss_full_K`/`netd_classification` were never written to disk
for exp-092's own Rank-1 14 (angle, config) cells. This cycle closes that
gap by full backfill, and states the THERMODYNAMICS reading of what the
upper window's own unresolved status implies for **(NETD/instrument, not
human-eye) detectability: nothing, either way.** `delta_scene` is a
near-field phase/interference quantity; `p_abs_w` is bulk absorbed power,
and R14's own established mechanism (the oscillatory imprint lives in the
`σ_ext(θ)` config-differential term, not the absorption/scattering
partition) means the absorbed-energy channel is expected to stay smooth
and **(NETD/instrument, not human-eye) undetectable** regardless of how
the double-crossing resolves — tested directly below, not merely
asserted.

This cycle also resolves the double-crossing itself (a denser off-grid
`cpl=30` sweep), re-fits R15's own caution zone on a `cpl=30`-only basis
(gated on the sweep), runs a `sigma_max` PRIMARY-channel check localized
to the upper near-null, and computes — for the first time — the
twice-deferred Yee-grid dispersion phase-accumulation integral at the
actually-mandated aperture length scale (EM's own check, elevated to
mandatory under R8; a wrong, shorter length scale in the pre-freeze draft
was caught and corrected at Phase 2/3, see `phase2_redteam_audit.md`
RT-2 and `phase3_synthesis.md` §0).

This cycle makes **no phenomenon-mechanism claim** — T1 escape route N/A,
Checkpoint criterion 2 N/A, matching every T28 desk/instrument cycle
since exp-069 (independently re-verified against LOGBOOK.md's own record
by both the proposing seat and Red Team, `phase2_redteam_audit.md` §0).
It is pure instrument recalibration and energy-sidecar instrumentation.

## Setup

**Channel:** `PAIR_KEYS_R3=("C40_R3","G40_R3")` at `cpl=30`
(`R3_RATIO=1.5`, `experiments/069-.../design_geometry.py`). λ=600nm
throughout. All geometry (`R3_CONFIGS`, `PEC_R_R3`, `R3_R_OUT_CELLS`,
`BOX_CLEARANCE_A/B_R3`, `REF_HALF_H_R3`, `DENSE_ANGLES`,
`A_HALF_APERTURE=752`/`1128`) reused verbatim from
`experiments/069-.../design_geometry.py` and
`experiments/091-.../092-.../run.py` — zero new `lab/` diff, zero new
geometry formula.

**Five items, sequenced 5→3→1→2→4** (item 5 first: independent,
deterministic, non-gating, and its own fresh empty-leg captures at
41.8°/42.0° are reused in-memory by item 3; item 4 is desk-only and is
in fact computed in this document, ahead of any FDTD):

| Order | Item | Configs | Angles | `cpl` | `STEPS` | `sigma_max` | Leg(s) | Calls |
|---|---|---|---|---|---|---|---|---|
| 1st | **5 — NETD backfill** | `C40_R3`, `G40_R3` | 39.2°, 39.4°, 39.6°, 39.8°, 40.0°, 41.8°, 42.0° (existing grid) | 30 | 4200 | 0.5 (native) | empty+article | **28** |
| 2nd | **3 — sigma check, near-null** | `C40_R3`, `G40_R3` | 41.8°, 42.0° | 30 | 4200 | 1/3 (corrected) | article only (empty reused from item 5) | **4** |
| 3rd | **1 — denser sweep** | `C40_R3`, `G40_R3` | 41.750°, 41.775°, 41.825°, 41.850°, 41.875°, 41.900° (off-grid, 0.025° step) | 30 | 4200 | branch-gated on item 3 | empty+article | **24** |
| 4th | **2 — caution-zone re-fit** | desk only | — | — | — | — | — | **0** |
| any time | **4 — dispersion integral** | desk only | 37.2°, 40.2°, 41.4°, 40.0718°, 41.7811°, 41.8377° | — | — | — | — | **0** |
| **Total** | | | | | | | | **56** |

**Item 5 — NETD/energy-sidecar backfill (THERMODYNAMICS' own signature
item).** `pair_metrics()` in `experiments/092-.../run.py` computes full
per-cell `thermo` dicts for both `c_cell` and `g_cell` at every Rank-1
angle but only ever persists `c_cell`'s own values; `g_cell`'s are
computed in-memory and discarded. No T28-family experiment persists raw
FDTD captures to disk, so the only way to recover `g_cell`'s NETD fields
is a deterministic re-run (exp-092's own Learned #4: `_run_sim_r3`-family
calls are exactly deterministic across process invocations). New,
additive code only: `cell_metrics_full()` (generalizes `cell_metrics()`,
returns the full `thermo` dict) and `pair_metrics_full()` (forwards
`g_cell`'s own `p_abs_w`, `dt_ss_full_K`, `netd_classification`,
`sigma_ext_cells`, `ratio_abs_ext_raw` alongside `c_cell`'s own).
**Consistency gate:** `delta_scene`, `frac_contrast`, `ratio_k`,
`floor_pass` at all 7 angles must reproduce exp-092's own filed
`rank1.per_theta` values to float equality — licenses treating the newly
captured NETD fields as attached to the same already-scored physical
result.

**Item 3 — sigma_max check, localized to the upper near-null.** Angles
41.8°/42.0° (the two Rank-1 angles both `NODE-UNRESOLVABLE`,
`floor_pass=False`) — not Rank 3's own three broader census angles
(already CONFIRMed clean, exp-092). Article leg only, `sigma_max=1/3`;
empty legs reused in-memory from item 5's own fresh capture (bit-
independent of `sigma_max` by construction). Same `[0.3,3.0]` CONFIRM /
`[0.1,10]` REFUTE bands as exp-092's own Rank 3, applied to
`{sigma-corrected}/{item 5's own native-sigma value}` at each of
`delta_scene` (sign+ratio) and `frac_contrast` (ratio), worst-case across
both angles/quantities, plus a co-equal, non-gating `p_abs_w`-ratio check.

**Item 1 — denser off-grid `cpl=30` sweep, 41.75°–41.90°.** Six new
off-grid points, 0.025° step, bracketing both located crossings
(`41.7811°`, `41.8377°`), at least two strictly between them. Combined
with the three already-committed flanking `cpl=30` points (41.6°
[exp-091], 41.8°/42.0° [exp-092 Rank 1]), gives a continuous
~0.025°–0.05°-step curve across the entire 41.6°–42.0° window — well
under half the 0.057° separation between the candidate crossings.
`sigma_max` branch-gated on item 3's own verdict, fixed here before any
run: **CONFIRM → 0.5** (native, directly comparable to the flanking
anchors); **REFUTE → 1/3** (corrected — disclosed as not directly
comparable to the native-sigma flanking anchors); **NEITHER → 1/3**
(conservative default, same comparability caveat). Falsifiable three-way
outcome: **TWO-NODE CONFIRMED** (≥1 new interior point reads
`delta_scene>0` AND clears R13's floor gate); **SINGLE-NULL** (every new
interior point reads `delta_scene≤0`); **STILL AMBIGUOUS** (no new
interior point clears the floor gate either direction). No confident
directional lean stated in advance (PHOTONICS' own "widening lobe"
amplitude picture from exp-092 argues one way; R13/R14's own standing
near-zero-denominator caution argues the other, with comparable force).

**Idealization 16 (new this cycle, RT-3 fix):** item 1's three-way
outcome is angular-only (fixed `cpl=30`) and does not itself constitute
an R15-grade cross-resolution finding — a genuine two-node feature
established this way still needs a future `cpl=40` check at the interior
near-null angles specifically before it is treated as resolution-verified
under R15's own standard.

**Item 2 — zero-FDTD `cpl=30`-only caution-zone re-fit, gated on item 1.**
NOT a DROP/RELABEL counterfactual on the old `cpl=20` n=7 table (exp-092's
own Rank 2 already exhausted that, bit-exact, seven times reproduced).
Instead, a fresh `cpl=30`-only dataset (`n=8`) from every floor-gate-
clearing `cpl=30` point on record, reusing exp-090's own
`find_zero_crossings`/`firth_logistic`/`naive_mle_diverges`/`auc`
verbatim:

| θ | source (native `sigma_max=0.5`) | floor_pass | ratio_k | Y |
|---|---|---|---|---|
| 37.2° | exp-091 Leg 2 | True | 1.8463 | 0 |
| 39.2°/39.4°/39.6°/39.8° | exp-092 Rank 1 | True | 0.920/0.076/1.211/3.841 | 0/0/0/0 |
| 40.0° | exp-092 Rank 1 | True | 18.885 | 1 |
| 40.2° | exp-091 Leg 2 | True | 10.074 (razor-thin) | 1 |
| 41.4° | exp-091 Leg 2 | True | 9.212 (reclassified) | 0 |
| 41.8°/42.0° | exp-092 Rank 1 | **False** | — | excluded (NODE-UNRESOLVABLE) |

`margin=frac_contrast/FLOOR`, `FLOOR=1.91744×10⁻⁴` (unrecomputed).
**Corrected finding (RT-1 fix, adopted — the "REVERSED" language in the
original proposal draft was a sign-convention artifact, struck; see
`phase3_synthesis.md` §0/§1.1 for the independent triple-verification):**
`auc(-pos_m,-neg_m)=1.0000` under exp-090's own calling convention — the
**same** lower-margin-predicts-`Y=1` relationship as the original n=7
`cpl=20` sample, not a reversal. Firth's fit (`X=[1,log10(margin)]`)
converges in 15 iterations to `β=[3.76504788,−5.60700572]`, `m₅₀=4.6934`
— negative slope, matching the original's own `β=[1.7806,−5.6315]`
direction. Zone (`[max(margin|Y=1), min(margin|Y=0)]`,
`run.py`'s own unconditional formula, no swap): `[4.1083, 5.4287]` — a
real, non-contradictory, independently valuable finding on its own terms:
a `cpl=30`-only version of the boundary, narrower than the original
`cpl=20` zone (`[1.4764,2.1709]`, not directly comparable — different
resolution, partially different θ-population) but pointing the same
direction.

**Disclosed limitation (unchanged from the proposal draft):** this `n=8`
set is not a like-for-like resample of the original seven points — five
of its eight members sample a region the original n=7 never touched,
while three of the original seven (36.0°, 38.4°, 38.8°) have no `cpl=30`
measurement to include here. **RT-3 fix, adopted (MATERIALS' own
wording):** items 1/2 are a further, `cpl=30`-verified **step** toward
R15's founding mandate — **not its completion**. Two discharge conditions
remain open: the three still-unmeasured original points, and no `cpl=40`
comparator anywhere on this channel confirming `cpl=30` itself is
converged rather than merely a second, different, fixed resolution.

**Gate on item 1's extension (RT-3 angular/spatial fix, adopted):**
**TWO-NODE CONFIRMED** → extend the table with item 1's own newly
floor-clearing interior point(s), reported **provisional pending a future
spatial (`cpl=40`) check at the interior near-null angles specifically**
(not treated as R15-closing). **SINGLE-NULL** → table stands as built;
new interior points reported as context, not zone-defining. **STILL
AMBIGUOUS** → table stands as built, explicitly flagged provisional
pending item 1's own unresolved interior.

**Item 4 — Yee-grid dispersion phase-accumulation integral (MANDATORY
under R8, corrected at Phase 3 — see `phase3_synthesis.md` §0/§1.2).**
2D isotropic Yee-grid dispersion relation (`courant_frac=0.99`,
`S=courant_frac/√2≈0.700036`, `lab/fdtd2d.py::Sim.__init__`):

```
(1/S²) sin²(πS/cpl) = sin²(k cosθ/2) + sin²(k sinθ/2)
```

solved (Brent's method) for `k(θ,cpl)`. **Length scale, corrected to the
actually-mandated value (Director's own independent third derivation,
`phase3_synthesis.md` §0):** the aperture propagation length
`A_HALF_APERTURE=752` cells native / `1128` cells at R3
(`experiments/069-.../design_geometry.py:112`) — the length scale both of
EM's own prior citations (exp-091/092 `phase5_review_em.md`) actually
name, not the round-trip `PAD` distance the pre-freeze draft
mistakenly substituted (that computation is retained below, relabeled).

| θ | Δφ(cpl=20,`ℓ=A`) | Δφ(cpl=30,`ℓ=A`) | ΔΔφ | predicted Δθ (`P*=2.8421°`) | observed Δθ | ratio |
|---|---|---|---|---|---|---|
| 37.2° | −2.5773° | −1.1428° | +1.4345° | +0.011325° | — | (no observed shift; table internal-consistency only) |
| 40.2° | −1.3335° | −0.5913° | +0.7422° | +0.005860° | — | (no observed shift; internal-consistency only) |
| 40.0718° (lower) | −1.3751° | −0.6098° | +0.7654° | +0.006042° | **−0.194°** | **32.1×** |
| 41.4° | −0.9954° | −0.4413° | +0.5540° | +0.004374° | — | (no observed shift; internal-consistency only) |
| 41.7811° (upper 1) | −0.9078° | −0.4025° | +0.5053° | +0.003989° | **+0.320°** | **80.2×** |
| 41.8377° (upper 2) | −0.8956° | −0.3971° | +0.4985° | +0.003936° | **+0.377°** | **95.8×** |

**Secondary, relabeled (not the mandate — a real REFUTE of a different,
already-refuted mechanism):** the round-trip `PAD` distance (`ℓ=2×PAD`,
80/120 cells) gives ratios **301.8×/754.0×/900.4×** — but its supporting
citation (`pad_round_trip_echo_model`, exp-077) was itself a REFUTE of
that exact coherent-echo mechanism against real `PAIR_PAD` data
(two-wall `r²=0.0001`), not established support for reusing its length
scale here (`phase2_redteam_audit.md` RT-2). Reported for completeness,
not substituted for the mandated `ℓ=A` computation above.

**What this settles, and what it does not.** At the actually-mandated
length scale, differential Yee-grid dispersion phase over the aperture
propagation length REFUTES as a *sufficient* explanation of the observed
`cpl 20→30` crossing shifts by one clear order of magnitude (32×–96×) —
milder than the pre-freeze draft's mistaken 300×–900× claim, but still a
clean, unambiguous REFUTE, not a near-miss. It does not rule out
numerical dispersion as *a* contributing factor at some other path, nor
does it identify the actual mechanism — MATERIALS' own T10 near-field/
curved-boundary account remains the better-supported qualitative story
for *why* resolution refinement moves this feature.

## Idealizations

**Carried forward from exp-092's own NOTES.md, cited by original number
(extended per RT-4, adopted):**

1. **2D TMz, single λ=600nm** — no chromatic sweep, no 3D geometry.
3. **NETD is not a human-eye threshold.** Nothing in this cycle bears on
   constraint-3/4's human-eye verdict; `REALIZABILITY_MEMO.md` is not
   re-opened or re-scored. Every "detectability"/"undetectable" claim in
   this document is NETD/instrument-scoped, marked inline where used.
6. **`FLOOR`/`RMS[frac_contrast]` applied, not recomputed,** against
   every new `cpl=30` point in items 1/3/5 — a disclosed mixed-resolution
   comparison (item 2's own n=8 table is the one exception).
7. **This cycle does not test constraints 1/2/3/4 and takes no T1
   escape-route position.**
8. **The unbiased margin-vs-distance rebuild on the full 31-point window
   (exp-090's own Rank-2-in-queue item) remains open, still not run this
   cycle.**
11. **A Rank-3-style REFUTE/NEITHER-default (item 3's own verdict)
    reopens item 1's own net-placement/sigma choice as provisional for a
    future cycle** — it does not, by itself, revalidate whether the
    flanking anchor points remain directly comparable if item 3 fires
    REFUTE/NEITHER.

**New this cycle:**

12. Item 4's `ℓ=A` length-scale choice is one pre-declared, physically
    motivated candidate (independently confirmed as the value both of
    EM's own prior reviews actually name) — not an exhaustive accounting
    of every possible dispersion path.
13. Item 4's `θ↔90°−θ` symmetry check is a formula-level property,
    independently verified, not a claim about which physical axis this
    bench's own `angle_deg` convention measures from.
14. No settling re-check at item 1's/item 3's new angles — `STEPS=4200`
    at `cpl=30` cited as already clean from exp-091's own result at this
    identical `STEPS`/`cpl` pair, not independently re-verified at these
    specific new angles.
15. Item 2's own n=8 table treats 40.0°/40.2° as two independent `Y=1`
    members rather than resolving whether they represent the same
    underlying feature at two adjacent angles — disclosed, not resolved.
16. Item 1's three-way outcome is angular-only (fixed `cpl=30`), not
    itself an R15-grade cross-resolution finding (§ above).

**Carried idealizations banner (mandatory at both this section and the
Result section, per the Iteration-65 CHECKPOINT's escalated,
non-discretionary rule): every prediction below is governed by
Idealizations 1/3/6/7/8/11 plus this cycle's own 12–16.**

## Predictions (frozen, committed BEFORE any Phase-4 script runs)

**(Item 5) PRIMARY — reproduction.** CONFIRM = `delta_scene`,
`frac_contrast`, `ratio_k`, `floor_pass` at all 7 angles reproduce
exp-092's own filed `rank1.per_theta` values to float equality. REFUTE =
any disagreement, investigated before trusting the rest of this cycle.

**(Item 5b) informational, non-gating — NETD threading (NETD/instrument,
not human-eye).** Predicted: `dt_ss_full_K` in the range
`1×10⁻⁵`–`5×10⁻⁴` K at all 14 cells, all classifying **UNDETECTABLE**
against `NETD_BAND_K=(0.020,0.050)` (Iteration-20/exp-043) — consistent
with Rank 3's own filed C-config values (`4.6×10⁻⁵`–`5.2×10⁻⁵` K) and T9's
near-saturation anchor. Falsifiable: a MARGINAL/DETECTABLE reading at any
cell, or a value outside the stated range by >3×, is a genuine surprise.

**(Item 3) PRIMARY, gates item 1's `sigma_max`.** Same `[0.3,3.0]`
CONFIRM / `[0.1,10]` REFUTE bands as Rank 3. No confident directional
lean.

**(Item 3b) informational, non-gating.** Co-equal `p_abs_w` ratio check;
`ratio_abs_ext_raw` within ~2–3% of the 0.51 T9 anchor, informational.

**(Item 1) PRIMARY — three-way outcome** (TWO-NODE CONFIRMED /
SINGLE-NULL / STILL AMBIGUOUS). No confident directional lean.

**(Item 2) PRIMARY — corrected (RT-1 fix).** The base n=8 `cpl=30`-only
zone reproduces bit-exact when Phase 4's committed script recomputes it
live: `auc(-pos,-neg)=1.0000` (exp-090's own convention), zone
`[4.1083, 5.4287]`, Firth `β=[3.76504788,−5.60700572]`, `m₅₀=4.6934`,
naive MLE diverges. CONFIRM = reproduces to ≥4 significant figures.
REFUTE = any disagreement, investigated. **(Item 2, extension) gated on
item 1** — reported per the corrected gate above, not a pass/fail test.

**(Item 4) PRIMARY, corrected (RT-2 fix + Director's own independent
derivation, `phase3_synthesis.md` §0/§3).** The desk script reproduces
the `ℓ=A` table above to ≥4 significant figures, and the magnitude ratio
(observed vs. predicted |Δθ|, at `ℓ=A`) stays in the **`10×`–`200×`**
range at each of the three angles with a known observed crossing shift —
a REFUTE of the dispersion-alone mechanism by at least one clear order
of magnitude, not the pre-freeze draft's mistaken two-order claim.
CONFIRM = reproduces and the ratio band holds. REFUTE of this band = the
recomputed ratio falls outside `10×`–`200×` at any of the three angles —
investigated, not smoothed over.

## T1 escape route

**N/A** — verified directly against LOGBOOK.md's own record by the
proposing seat and independently re-confirmed by Red Team
(`phase2_redteam_audit.md` §0): every T28 sub-thread entry from Iteration
46 through Iteration 69 states T1 route N/A / Checkpoint criterion 2 N/A.
This cycle takes no position on σ(I)/σ(x,t)/angular selectivity/
sub-threshold operation, makes no phenomenon-mechanism claim, and does
not touch `REALIZABILITY_MEMO.md`.
