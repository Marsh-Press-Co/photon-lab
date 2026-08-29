# PHASE 5 — REVIEW · Seat: THERMODYNAMICS · Panel Iteration 65 · exp-088

Fresh sub-agent, no memory of writing this cycle's own Phase-2 critique
(`phase2_critique_thermodynamics.md`) beyond what is read back from the
committed record. Read in full: LOGBOOK.md's RULED OUT (R1–R13) and LIVE
THREADS/T28 through Iteration 64/exp-087; PANEL.md; the complete exp-088
cycle record (`phase1_proposal.md`, all five Phase-2 critiques,
`phase2_redteam_audit.md`, `phase3_synthesis.md`, `NOTES.md`, `run.py`,
`results.json`, `run_output.txt`); `lab/thermo_sidecar.py` source; and
exp-087's `phase5_review_thermodynamics.md` (my seat's own prior-cycle
review, for continuity of method, not deference).

## 1. Was my own Phase-2 fix (Q6, NETD at 38.4°/38.8°) actually delivered?

**Yes — delivered exactly as specified, blocking-item-free (Red Team ruled
it a "recommended" not "mandated" item, §4 of `phase2_redteam_audit.md`,
and Phase 3 adopted it anyway, item 7).** `results.json::thermo` carries
`dt_ss_full_K`/`netd_classification`/`netd_disclaimer` for all 4 new cells
(C40/G40 × 38.4°/38.8°), and `run.py` shows it reuses the `p_abs_w` values
already required for the PRIMARY `frac_p_abs` metric — genuinely zero
marginal FDTD cost, as promised.

**Independently recomputed from `results.json::thermo` end-to-end**
(NETD band = 0.020 K, `run.py::exp087.NETD_BAND_K`, unchanged from
exp-087):

| cfg, θ | `dt_ss_full_K` (file) | margin = 0.020/`dt_ss` (recomputed) |
|---|---|---|
| C40, 38.4° | 4.805995×10⁻⁵ | **416.15×** |
| G40, 38.4° | 4.812263×10⁻⁵ | **415.60×** |
| C40, 38.8° | 4.856021×10⁻⁵ | **411.86×** |
| G40, 38.8° | 4.884940×10⁻⁵ | **409.42×** |

Matches `NOTES.md`'s claimed "≈409×–416×" exactly, and sits comfortably
inside exp-087's own 374×–442× range at the three original angles — no
discontinuity, no surprise, nothing off. **UNDETECTABLE is genuine at all
four new cells, independently confirmed, not merely restated.**

One thing worth adding to the record that isn't currently in it: the
`resolved` gate's own noise margin (not just its PASS bit) is markedly
thinner at 38.4° than at 38.8° — `|Δp_abs_w|` clears its noise floor
(`3×box_dev_max×p_c40`) by only **2.70×** at 38.4° vs. **4.22×** at
38.8° (recomputed directly from `results.json::box_dev`/`thermo`; not
reported anywhere in `NOTES.md`, which states only the boolean
`resolved=True`). This does not change any verdict — 2.70× still clears
cleanly, nothing near a coin-flip — but it means the single most
surprising number in this cycle's own Result section (the 38.4° dip,
§2 below) also carries this batch's thinnest resolvability margin, a
combination worth flagging rather than passing over silently.

## 2. The `frac_p_abs(38.4°)` dip — independently recomputed, traced to `σ_ext(θ)`

Recomputed `p_abs_w` for both configs at both new angles directly from
`results.json::thermo`, and pulled exp-087's own three angles from its
`results.json::thermo` for the full 5-point picture:

| θ | `p_abs_w`(C40) | `p_abs_w`(G40) | `frac_p_abs` (recomputed) | file value |
|---|---|---|---|---|
| 36.0° | 2.748814×10⁻¹² | 2.754216×10⁻¹² | 1.96547×10⁻³ | (exp-087) |
| 38.4° | 2.925321×10⁻¹² | 2.929136×10⁻¹² | **1.30414×10⁻³** | 1.30414×10⁻³ ✓ |
| 38.6° | 2.941857×10⁻¹² | 2.953626×10⁻¹² | 4.00057×10⁻³ | (exp-087) |
| 38.8° | 2.955771×10⁻¹² | 2.973373×10⁻¹² | 5.95524×10⁻³ | 5.95524×10⁻³ ✓ |
| 41.8° | 3.234850×10⁻¹² | 3.258186×10⁻¹² | 7.21416×10⁻³ | (exp-087) |

Both file values reproduce bit-exact from primitives. **Confirmed: the
38.4° reading genuinely dips below 36.0°'s own value** — the headline
surprise is real arithmetic, not a transcription artifact.

**Tracing it through `σ_ext(θ)`, per the charter's own energy-ledger
mandate.** `lab/thermo_sidecar.py::absorbed_power_established_ratio`
(read directly) computes `p_abs_w = ratio_abs_ext × I × (σ_ext_cells ×
dx_m)²` — the `iso_xsec_sq` convention makes absorbed power **quadratic**
in the measured extinction cross-section, not linear (exp-087's own
THERMODYNAMICS Phase-5 review flagged this exact sensitivity, §8 of that
document, independently confirmed here by direct source read). Since
`ratio_abs_ext` is nearly config-independent at every sampled angle (T9's
own established flatness — `ratio_abs_ext_raw` = 0.5128–0.5138 across all
10 (config,θ) cells now on record, exp-087+exp-088 combined, max
config-to-config spread 7.8×10⁻⁴ relative), a first-order Taylor expansion
gives:

```
frac_p_abs(θ) ≈ 2·[σ_ext(G40,θ) − σ_ext(C40,θ)]/σ_ext(C40,θ)  +  [ratio(G40,θ) − ratio(C40,θ)]/ratio(C40,θ)
```

Computed both terms from `results.json::widths`/`thermo` directly at all
5 angles:

| θ | frac Δσ_ext (C40→G40) | frac Δratio_abs_ext | 2·(1st term)+(2nd) | exact `frac_p_abs` |
|---|---|---|---|---|
| 36.0° | 0.0696% | 0.0573% | 1.9642×10⁻³ | 1.9655×10⁻³ |
| **38.4°** | **0.0263%** | 0.0777% | **1.3037×10⁻³** | **1.3041×10⁻³** |
| 38.6° | 0.1703% | 0.0589% | 3.9957×10⁻³ | 4.0006×10⁻³ |
| 38.8° | 0.2844% | 0.0257% | 5.9457×10⁻³ | 5.9552×10⁻³ |
| 41.8° | 0.3732% | −0.0261% | 7.2022×10⁻³ | 7.2142×10⁻³ |

The linear decomposition reproduces the exact `frac_p_abs` to <0.5%
relative at every point — the mechanism is fully accounted for, nothing
residual. **This settles the question the charter posed**: the
`ratio_abs_ext`-difference term is small and roughly stable in magnitude
across all 5 angles (5.7–7.8×10⁻⁴, even changing sign at 41.8°) — it is
*not* the driver. The dip is carried almost entirely by the **σ_ext(θ)
differential term**, which falls to a local minimum (0.026%) precisely at
38.4° — well below its value at every other sampled angle, including
36.0° (0.070%) — before rising monotonically through 38.6°→38.8°→41.8°
(0.17%→0.28%→0.37%).

**Is this in tension with T9's flat `ratio_abs_ext≈0.51`, or does T9's
flatness actually *require* it?** The latter. T9's flatness is what
*licenses* attributing the entire dip to the `σ_ext` differential channel
rather than to the absorption/extinction partition — if `ratio_abs_ext`
swung meaningfully between configs, the dip could instead reflect a
config-specific shift in how much of the extinguished power gets
absorbed vs. scattered at 38.4° specifically. It doesn't: the partition
is essentially frozen (T9-flat, independently reconfirmed here at 5
points, not the 3 exp-087 established). What the flat ratio *forces* is
that the entire fractional swing between C40 and G40 must live in
`σ_ext(θ)` itself — specifically, in the **second-order, config-differential
component** of `σ_ext(θ)`, not in `σ_ext(θ)`'s own bulk behavior. And on
that count nothing is anomalous or implausible: `σ_ext(C40,θ)` and
`σ_ext(G40,θ)` *individually* both trace smooth, monotonically increasing
curves across the full 36.0°→41.8° span (300.77→325.95 cells and
300.98→327.16 cells respectively) — there is no kink, dip, or
irregularity in either config's own extinction cross-section anywhere in
this window. The C40-minus-G40 *gap* between those two smooth curves
never even changes sign across the 5 sampled points (G40 > C40
throughout) — it is a local minimum in a small, positive, second-order
quantity riding on top of two much larger, well-behaved curves, not a
zero-crossing or a discontinuity in either curve individually.

**Physically plausible, not implausible — and independently reinforcing,
not undermining, T28's own standing prior.** A local minimum in the
C40-vs-G40 padding-differential channel, sampled at exactly one point
(38.4°) among five, is squarely consistent with — though not proof of —
T28's own long-established ~2.84°–2.95° periodicity in exactly this kind
of padding-dependent differential signature (the sub-thread's founding
`C80−C40` periodicity, and PHOTONICS' own finding this cycle that
`delta_scene` itself has 4 zero-crossings ≈1.2–1.7° apart across the same
window, roughly half that period). This cycle's own 5 points cannot by
themselves establish periodicity in the `σ_ext`-differential channel
specifically (that requires the denser, per-config `σ_abs(θ)`/`σ_ext(θ)`
sweep Red Team's Iteration-65 ranking item 2 and MATERIALS' "passive
transducer, not resonant source" test already name, explicitly scoped out
of this cycle) — but nothing in the bookkeeping is implausible, self-
inconsistent, or artifact-shaped. It reads as a genuine, if under-sampled,
second-order structural feature.

## 3. Anything else off in the energy bookkeeping?

None found. `xi_ext` (extinction-routes agreement) is ≤3.86×10⁻⁴ at all
8 new cells, comfortably inside the ≤0.12 gate. `sigma_abs≥0` everywhere.
`P2` reproduction is bit-exact (`max_dev=0.0`). Q7's `ratio_abs_ext`
cross-check against T9's 0.51 anchor is confirmed at all 4 new cells
(0.5131–0.5138, within 0.6%–0.8% of the anchor) — a genuine, if modest,
extension of T9's own confirmed-flat range from 3 to 5 angles, now
spanning both configs at both new points. No sign errors, no unit
mismatches (R9 discipline applied), no unfalsifiable claim.

## Verdict on this cycle's Combined Verdict contribution

**From THERMODYNAMICS: CONCUR with PARTIAL / support the frozen Q1–Q7
Result as filed, on the energy-ledger axis specifically.** My own Phase-2
zero-cost fix (Q6) was delivered in full and independently reproduces;
the T9-anchor extension (Q7) was delivered and independently reproduces;
the PRIMARY metric's headline surprise (the 38.4° `frac_p_abs` dip) is
independently confirmed as genuine arithmetic, traced to its physical
source (`σ_ext(θ)`'s own config-differential component, not the
absorption/extinction partition, which T9's flatness pins down), and
found to be a legitimate, if thinly-sampled, reading — not an artifact,
not a bookkeeping error, not in tension with any established anchor. The
one gap I would flag as worth closing, not blocking: the 38.4° reading's
own noise-floor margin (2.70×) is the thinnest of the batch and Idealization
7 (settling not independently re-checked at these two angles) applies
directly to it — a cheap, targeted check that would firm up exactly the
number this cycle's own Result section calls "a genuine, well-resolved
… surprise."

## Ranked top-3 for the Director's Iteration-66 queue

1. **Settling spot-check specifically at 38.4°** (STEPS=1400 vs. 2800,
   either config) before the `frac_p_abs(38.4°)` dip is cited elsewhere
   as established structure. Idealization 7 explicitly disclosed this gap
   as not independently re-checked at the two new angles; it is the
   thinnest-margin point (2.70× its own noise floor, vs. 4.22× at 38.8°)
   carrying this cycle's single most novel finding. Near-zero marginal
   cost (one extra FDTD call, exp-087's own precedent).
2. **Extend the σ_ext(θ) differential channel densely enough to test for
   periodicity in the C40-minus-G40 gap itself** — Red Team's own
   Iteration-65 ranking item 2 (the ~124-call full/denser individual
   `σ_abs(C40,θ)`/`σ_abs(G40,θ)` build) and MATERIALS' "passive
   transducer, not resonant source" test, already named and scoped out
   of this cycle, are now sharper and better-motivated than when first
   proposed: this cycle's own 5-point trace shows the differential term
   driving `frac_p_abs`'s dip-then-rise shape in a pattern consistent with
   (not yet proven to match) T28's own ~2.84°–2.95° established period.
   This directly tests whether that consistency is real.
3. **Close the "un-sampled node census" gap this cycle's own NOTES.md
   Next section already names** (measure `ratio_k` by real FDTD at
   ≈37.1°/37.2°, 40.2°, 41.4° — the three other `delta_scene`
   zero-crossings never yet FDTD-sampled) before any future LOGBOOK/
   PLAN.md entry treats the energy-interception channel's CONSISTENT
   reading as channel-general rather than single-node-local. Zero new
   framing needed — this cycle's own forward tripwire already states it;
   it is simply the next FDTD spend on the board.

## Files consulted (read/executed directly)

- `/home/user/photon-lab/PANEL.md`, `/home/user/photon-lab/LOGBOOK.md`
  (RULED OUT R1–R13 in full; LIVE THREADS/T28 in full through Iteration
  64/exp-087, targeted full reads at T9, R13, and the exp-087 Iteration-64
  entry)
- `/home/user/photon-lab/experiments/088-t28-node-bracket-r13-floor-gate/`
  `phase1_proposal.md`, `phase2_critique_{em,materials,photonics,
  thermodynamics,vision}.md`, `phase2_redteam_audit.md`,
  `phase3_synthesis.md`, `NOTES.md`, `run.py`, `results.json`,
  `run_output.txt`
- `/home/user/photon-lab/experiments/087-t28-energy-interception-poynting-check/
  results.json` (`thermo` block, all 3 angles, both configs — independently
  cross-referenced against exp-088's own 4 new cells)
- `/home/user/photon-lab/lab/thermo_sidecar.py`
  (`absorbed_power_established_ratio` read directly to confirm the
  `p_abs_w ∝ σ_ext²` functional form underlying §2's decomposition)
- `/home/user/photon-lab/experiments/087-t28-energy-interception-poynting-check/
  phase5_review_thermodynamics.md` (this seat's own prior-cycle review,
  consulted for continuity of method — specifically its own §8 finding on
  the `iso_xsec_sq` quadratic sensitivity, independently re-confirmed
  here, not deferred to)
