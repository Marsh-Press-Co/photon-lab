# PHASE 1 — PROPOSAL · Panel Iteration 70 · exp-093 · Lead seat: THERMODYNAMICS

## "Upper-Window Crossing Resolution & NETD Threading" — a targeted off-grid `cpl=30` sweep of the 41.75°–41.90° near-null, a sigma_max PRIMARY-channel check localized to that same region, a full energy-sidecar backfill of exp-092's own Rank-1 cells, a zero-FDTD caution-zone re-fit gated on the sweep's outcome, and the twice-deferred Yee-grid dispersion integral computed for the first time — exp-092's Reconciled Iteration-70 queue (`phase5_redteam_audit.md` §8), combined into one ordered build

### 0. Reconciliation against the authoritative source (read directly, not paraphrased)

This proposal executes, in full, `experiments/092-t28-crossing-relocation-
caution-zone-rebuild/phase5_redteam_audit.md` §8's Reconciled Iteration-70
recommendations: **Tier 1** items 1 (denser off-grid resolution of the
double-crossing) and 2 (caution-zone re-fit, gated on item 1); **Tier 2**
items 3 (sigma_max check at the upper near-null, MATERIALS' own #1), 4 (the
Yee-grid dispersion integral, EM's own #2, elevated to **mandatory** at §7
— a third undisclosed citation fires R8), and 5 (NETD/energy-sidecar
threading through Rank 1's own 14 cells — THERMODYNAMICS' own #3 ranking
at that same reconciled queue, and this seat's own charter duty as
Iteration-70 lead). Item 6
(extend the search past 42.0°, NOTES.md's own Next item 3) is named but
**declined this cycle on budget grounds**, matching exp-092's own Tier-2/
Tier-3 deferral precedent (§8 below).

### 1. Design narrative — THERMODYNAMICS' own reasoning (≤300 words)

Every prior T28 cycle since exp-087 has scored `delta_scene`/`frac_contrast`
— a coherent phase/timing quantity, proven config-invariant in
`ratio_abs_ext` to <0.1% (R14's own founding evidence) — while treating
`p_abs_w`, the actual absorbed-power channel this seat owns, as a
downstream ratio (`frac_p_abs`) rather than a persisted physical quantity.
That gap is real: individual `p_abs_w`/`dt_ss_full_K`/`netd_classification`
were never written to disk for Rank 1's 14 (angle, config) cells, so no one
can yet say what a thermal-camera-equivalent instrument would read at the
exact angles that now anchor T28's own most consequential open question.
This cycle closes that gap by full backfill (§3), and states the
THERMODYNAMICS reading of what the upper window's own unresolved status
implies for detectability: **nothing, either way.** `delta_scene` is a
near-field phase/interference quantity built from a residual-reflection
comparison; `p_abs_w` is bulk absorbed power, and R14's own established
mechanism (the ~2.84° oscillatory imprint lives in the `σ_ext(θ)`
config-differential term, not in the absorption/scattering partition) means
whichever way the double-crossing resolves — a genuine two-node feature or
a coarse-grid interpolation artifact — the absorbed-energy channel is
expected to stay smooth and undetectable regardless, because it is
mechanistically decoupled from the interference-node structure under
dispute. This cycle's own §3 data will test that expectation directly, not
merely assert it: a `netd_classification` swing coincident with the
disputed node would itself be a new, genuinely surprising finding.

### 2. Sequencing — a real gating dependency, learned from exp-092's own Red-Team-caught mistake

Red Team's own exp-092 Phase-2 audit forced a resequencing (Rank 3 before
Rank 1) after two blind critiques independently caught the reverse order
risking a 28-call spend on an article whose `sigma_max` correctness was
still undetermined. The same shape recurs here: item 1's new off-grid net
samples **inside the exact near-null region** item 3 exists to validate —
narrower and closer to the disputed node than any of Rank 3's own three
census angles (37.2°/40.2°/41.4°), none of which sits within 0.38° of the
upper double-crossing (exp-092's own `NOTES.md` Result section, "Scope
correction," citing exp-092's own `phase5_redteam_audit.md`). Running item
1 before item 3 would repeat exactly the mistake Red Team already named
once. This proposal therefore fixes the order
**item 5 → item 3 → item 1 → item 2 → item 4** (item 4 is desk-only and is
in fact computed below, in this document, ahead of any FDTD — matching
EM's own Rank-2 pre-verification precedent). Item 5 runs first not only
because it is independent, deterministic, and non-gating, but because its
own empty-leg captures at 41.8°/42.0° (already inside its 7-angle set) are
exactly the two angles item 3 needs — reused in-memory, zero marginal cost,
exactly the "re-run rather than reuse-from-disk, but reuse-within-the-same-
process" idiom exp-092's own Rank 3 established for its own empty legs.

### 3. Item 5 — NETD/energy-sidecar backfill of Rank 1's own 14 cells (THERMODYNAMICS' own signature item)

**Why this requires new FDTD, not a JSON patch (verified from source, not
assumed).** `pair_metrics()` in `experiments/092-.../run.py` computes full
per-cell `thermo` dicts (via `cell_metrics()`) for **both** `c_cell` and
`g_cell` at every Rank-1 angle, but only ever forwards the `c_cell`'s own
`dt_ss_full_K_c`/`netd_classification_c` into the persisted record — the
`g_cell`'s own values are computed in-memory and discarded before
`results.json` is written. No T28-family experiment persists raw FDTD
captures to disk (exp-092's own Rank-3 empty-leg problem, identical shape),
so there is no artifact on disk from which to recover the `g_cell` values
after the fact — the only way to obtain them is to re-run the cells. This
is a **deterministic reproduction**, not new information (exp-092's own
Learned #4, independently confirmed: "`_run_sim_r3`-family FDTD calls are
exactly deterministic across separate process invocations").

**Design.** Re-run all 7 of exp-092's own Rank-1 angles
(`{39.2°, 39.4°, 39.6°, 39.8°, 40.0°, 41.8°, 42.0°}`), both configs
(`C40_R3`, `G40_R3`), both legs (empty + article), at
`sigma_max=SIGMA_NATIVE=0.5` — the identical convention exp-092's own Rank
1 used (the sigma branch there resolved CONFIRM, licensing native
`sigma_max` at the three census angles; this re-run is not itself a test of
that question, it is a bit-exact reproduction of an already-scored result,
now capturing the fields that were dropped). A new, reusable
`cell_metrics_full()` (generalizing `cell_metrics()` by returning the FULL
`thermo` dict, not stripping it) and a `pair_metrics_full()` (generalizing
`pair_metrics()` to also forward `g_cell`'s own `p_abs_w`,
`dt_ss_full_K`, `netd_classification`, `sigma_ext_cells`,
`ratio_abs_ext_raw`, alongside the `c_cell`'s own, which the existing
function already threads) are the only new code — same formula, same
calls, nothing retyped.

**Consistency check (falsifiable, matching R4's committed-recomputation
discipline).** `delta_scene`, `frac_contrast`, `ratio_k`, `floor_pass` at
all 7 angles are asserted to reproduce exp-092's own filed `rank1.per_theta`
values to float equality (deterministic FDTD, no tolerance needed) — this
is the load-bearing gate that licenses treating the newly-captured NETD
fields as attached to the *same* physical result already scored, not a
different run.

**Calls:** 7 angles × 2 configs × 2 legs = **28**.

### 4. Item 3 — sigma_max PRIMARY-channel check, localized to the upper near-null

**Angles: 41.8°, 42.0°** — the two Rank-1 angles Red Team's own audit named
as the actual near-null region (both `NODE-UNRESOLVABLE`, `floor_pass=
False`), not a re-run of Rank 3's own three broader census angles (already
CONFIRMed clean, exp-092 Result §R3). **Leg: article only**
(`sigma_max=SIGMA_R3_CORRECTED=1/3`), empty legs reused **in-memory** from
item 5's own fresh capture at these same two angles (bit-independent of
`sigma_max` by construction, exactly as established in exp-091/092).
Mirrors Rank 3's own recipe exactly (`ratio_sign_verdict`'s `[0.3,3.0]`
CONFIRM / `[0.1,10]` REFUTE bands, applied to
`{sigma-corrected}/{item-5's own native-sigma value}` at each of
`delta_scene` (sign+ratio) and `frac_contrast` (ratio), worst-case across
both angles/quantities), plus a co-equal, non-gating `p_abs_w`-ratio check
(mirroring Rank 3b) — a free byproduct of the same 4 calls, THERMODYNAMICS'
own charter check applied a second time this cycle, now precisely where it
matters most.

**Calls:** 2 angles × 2 configs × 1 leg = **4**.

### 5. Item 1 — denser off-grid `cpl=30` sweep to resolve the double-crossing

**Angles — six new off-grid points, 0.025° step, spanning 41.75°–41.90°**
(bracketing both located crossings, `41.7811°` and `41.8377°`, with at
least two new points strictly between them):
`{41.750°, 41.775°, 41.825°, 41.850°, 41.875°, 41.900°}`
(`41.800°` is excluded — already measured at `cpl=30` by exp-092's own
Rank 1, reused as a free interior anchor). Combined with the three already-
committed `cpl=30` points flanking this window (`41.6°` from exp-091's own
Leg 4, `41.8°`/`42.0°` from exp-092's own Rank 1), this gives a
**continuous ~0.025°–0.05°-step curve across the entire 41.6°–42.0°
window** — 4–8× finer than the native `DENSE_ANGLES` step and well under
half the `0.057°` separation between the two candidate crossings, the
resolution R3's own meta-rule requires before trusting a feature this
narrow.

**Why 41.75°–41.90°, not the full 41.6°–42.2° span named at Tier 1:**
the flanking points (41.6°, 42.0°) are already same-signed and resolved at
`cpl=30`; the disputed structure is entirely interior to
`[41.6°, 42.0°]`. Extending outward past 42.0° is a distinct question
(item 6, §9) that this design does not need to answer to resolve THIS
cycle's own disputed feature; declining it here keeps item 1's own cost
proportionate to the question it actually answers.

**`sigma_max`: branch-gated on item 3's own verdict (fixed here, before any
run — house discipline, mirroring exp-092's own Rank-3→Rank-1 branch rule
exactly):**
- **CONFIRM** → `sigma_max=0.5` (native) — directly comparable to the
  three already-committed flanking anchors (41.6°/41.8°/42.0°, all
  measured at native `sigma_max`), a single internally-consistent curve.
- **REFUTE** → `sigma_max=1/3` (corrected — the finding itself, not a
  default, matching exp-092's own REFUTE-branch policy) — disclosed
  explicitly as **not directly comparable** to the native-sigma flanking
  anchors; item 1's own crossing-location read would then answer a
  genuinely different (sigma-corrected) question than the flanking points
  it is nested inside, a real, named limitation carried forward, not
  silently absorbed.
- **NEITHER** → `sigma_max=1/3` (the conservative default, matching
  exp-092's own NEITHER-branch policy exactly — disclosed as a
  NEITHER-triggered default, not a CONFIRM-level finding) — the same
  comparability caveat as the REFUTE branch applies.

**Falsifiable outcome categories (three-way, matching this cycle's own
scored question, not a binary):**
- **TWO-NODE CONFIRMED** — at least one new interior point (any of the six)
  reads `delta_scene>0` AND clears R13's floor gate
  (`frac_contrast≥FLOOR`) — a genuine, resolvable positive excursion
  between the two candidate crossings, establishing a real second
  oscillatory node nested inside the established ~2.84° macro-period (whose
  own half-period, ≈1.42°, is 25× wider than the `0.057°` gap in dispute —
  this would be new structure, not an artifact of the macro period).
- **SINGLE-NULL** — every new interior point reads `delta_scene≤0`
  (floor-passing or not) — no genuine positive excursion is found; the
  original "two crossings 0.057° apart" is best read as a 3-point
  linear-interpolation artifact across a single smooth trough, and the
  double-crossing does not survive resolution refinement (an R11/R13-
  lineage outcome).
- **STILL AMBIGUOUS** — no new interior point clears the floor gate in
  either direction (i.e., the entire interior stays `NODE-UNRESOLVABLE`) —
  reported as its own genuine outcome, not forced into either label above.

**No confident directional lean stated in advance** — PHOTONICS' own
"widening lobe" amplitude picture (frac_contrast inflates 2.8–5.2× under
resolution refinement, exp-092 §2a) is directionally suggestive of real
structure surviving refinement, but R13/R14's own standing caution (a
ratio built from a near-zero, floor-gate-failing denominator is exactly the
regime where a spurious reading is most likely) argues the other way with
comparable force. This is a genuinely open, two-sided question.

**Calls:** 6 angles × 2 configs × 2 legs = **24**.

### 6. Item 2 — zero-FDTD caution-zone re-fit, gated on item 1

**What "using the newly-located crossings as direct inputs" means,
concretely.** Not a DROP/RELABEL counterfactual on the OLD `cpl=20` n=7
Table 1 (exp-092's own Rank 2 already exhausted that question, CONFIRMed
bit-exact, seven-times independently reproduced — re-litigating it adds
nothing). Instead: build a **fresh, `cpl=30`-only** caution-zone dataset
from every now-available, floor-gate-clearing `cpl=30` point, reusing
exp-090's own `find_zero_crossings`/`firth_logistic`/`naive_mle_diverges`/
`auc` verbatim, no new statistical machinery:

| θ | source (all native `sigma_max=0.5`, one consistent article throughout) | floor_pass | ratio_k | Y (`ratio_k>10`) |
|---|---|---|---|---|
| 37.2° | exp-091 Leg 2 (native cpl=30) | True | 1.8463 | 0 |
| 39.2°/39.4°/39.6°/39.8° | exp-092 Rank 1 (native cpl=30) | True | 0.920/0.076/1.211/3.841 | 0/0/0/0 |
| 40.0° | exp-092 Rank 1 (native cpl=30) | True | 18.885 | 1 |
| 40.2° | exp-091 Leg 2 (native cpl=30) | True | 10.074 (razor-thin) | 1 |
| 41.4° | exp-091 Leg 2 (native cpl=30) | True | 9.212 (reclassified) | 0 |
| 41.8°/42.0° | exp-092 Rank 1 (native cpl=30) | **False** | — | excluded (`NODE-UNRESOLVABLE`) |

An `n=8` dataset (`margin=frac_contrast/FLOOR`, `FLOOR` unrecomputed,
Idealization 6) with **zero mixed-resolution rows** — every point is a
genuine `cpl=30` measurement, directly addressing R15's own founding
concern (a boundary built from `cpl=20` points was never trustworthy near a
resolution-sensitive node; this one is `cpl=30` throughout). It is,
deliberately, ALSO a zero-mixed-`sigma_max` table: every one of these
eight rows is measured at the identical native `sigma_max=0.5`, matching
item 5's own flanking-anchor convention — not Rank 3's own sigma-corrected
readings, which would introduce exactly the "two different physical
articles in one curve" contamination §5 disclosed for item 1.

**A genuinely new finding this table-construction step itself surfaces,
disclosed here rather than left implicit:** Rank 3's own sigma-corrected
`ratio_k` at 40.2° reads **9.729** (`experiments/092-.../results.json::
rank3.per_theta["40.2"].ratio_k`) — **below** `RATIO_HIGH=10`, i.e. under
the sigma-corrected convention 40.2° would ALSO classify `Y=0`, not `Y=1`.
Combined with the native-sigma value's own already-razor-thin margin
(`10.074`, `0.74%` over the boundary), **40.2°'s own `Y=1` classification
is fragile under BOTH axes this sub-thread has now tested it against** —
grid resolution (exp-091: `25.05→10.074`, native sigma) AND `sigma_max`
choice (exp-092 Rank 3: `10.074→9.729`, fixed `cpl=30`) — each perturbation
individually inside its own governing CONFIRM band (`[0.3,3.0]` magnitude
ratio for the resolution step; the sigma-correction step's own
`ratio_k(sigma-corrected)/ratio_k(native-sigma)` at 40.2° is `9.7285/
10.0744=0.9657`, also comfortably inside `[0.3,3.0]` — note this specific
ratio is a diagnostic computed here, not itself one of Rank 3's own two
pre-registered scored quantities, `delta_scene`/`frac_contrast`), yet each is
independently sufficient to flip a binary threshold classification sitting
this close to `RATIO_HIGH`. 40.0° (`18.885`, this cycle's own newly
measured point) is, at present, the **only** unambiguous `Y=1` example in
this sub-thread's entire native-cpl=30 record — a fact item 2's own zone
construction (§ below) must carry forward explicitly, not average away.

**Pre-verified computation (I, THERMODYNAMICS, ran this exact recipe
against the real house functions, imported unmodified from
`experiments/090-.../run.py`, before proposing it — matching R4's
discipline and EM's own Rank-2 precedent in exp-092; disclosed as my own
pre-verification, to be independently reproduced bit-exact by a committed
Phase-4 script, not copied from this document as a substitute for that
reproduction). `margin=frac_contrast/FLOOR`, `FLOOR=1.91744×10⁻⁴`:**

| θ | margin (sorted ascending) | Y |
|---|---|---|
| 40.0° | 2.3005 | 1 |
| 40.2° | 4.1083 | 1 |
| 41.4° | 5.4287 | 0 |
| 39.8° | 9.1877 | 0 |
| 37.2° | 11.2790 | 0 |
| 39.6° | 15.6474 | 0 |
| 39.4° | 20.6530 | 0 |
| 39.2° | 23.1785 | 0 |

**AUC(margin) = 0.0000 — perfect separation, but REVERSED in direction
from exp-090's own original `n=7` (`AUC=1.0000`, where higher margin
predicted `Y=1`): here every `Y=1` margin is SMALLER than every `Y=0`
margin.** Firth's fit (`X=[1,log10(margin)]`) converges in 15 iterations to
`β=[3.7650, −5.6070]` — the negative slope is the direct algebraic
signature of the reversed direction — giving `m₅₀=4.6934` (margins BELOW
this value predict `Y=1`, the opposite decision rule from the original
`m₅₀=2.071013`'s own "above predicts `Y=1`"). The naive MLE diverges
(perfect separation, `n=8`, matching the original's own divergence
pattern). The zone itself, defined the same way as exp-090's own
construction with the roles of `max`/`min` swapped to match the reversed
direction, is `[max(margin|Y=1), min(margin|Y=0)] = [4.1083, 5.4287]` —
**not inverted** (`4.1083<5.4287`), a coherent, non-degenerate boundary,
just one that classifies the opposite way round from the `cpl=20`-era
zone.

**Disclosed limitation on how much weight this reversal should carry:**
this `n=8` set is **not** a like-for-like resample of the original seven
points at higher resolution — five of its eight members (`39.2°`–`40.0°`)
sample a region (the lower-crossing neighborhood) the original `n=7` never
touched at all, while three of the original's own seven members
(`36.0°`, `38.4°`, `38.8°`) have no `cpl=30` measurement to include here
(§9's own Tier-3 gap). The AUC/direction "reversal" is a real, computed
fact about these two specific datasets; it is **not** yet evidence that
margin's own relationship to classification has itself reversed as a
general rule — that would need the same seven θ values measured at both
resolutions, which is exactly what Tier 3 (still deferred) would supply.
Reported here as a genuine, load-bearing, disclosed-as-such finding, not
overclaimed as a resolved reversal.

**Falsifiable check on this base computation (unconditional — none of
these eight rows falls inside item 1's own disputed 41.75°–41.90°
interior, so this table needs no gate to compute or report):** **CONFIRM**
= Phase 4's committed script reproduces every figure above to ≥4
significant figures. **REFUTE** = any disagreement, investigated not
silently reconciled.

**The gate on item 1 is about EXTENDING this table, not building it —
stated exactly:**
- **TWO-NODE CONFIRMED** → extend the `n=8` table with item 1's own newly
  floor-clearing interior point(s), correctly labeled by their own `Y`; if
  more than one clears the floor, report the zone under both "treat the
  pair as one interior excursion" and "treat each floor-clearing point
  independently" readings, side by side (mirroring exp-092's own DROP/
  RELABEL side-by-side convention).
- **SINGLE-NULL** → the `n=8` table stands as built above; item 1's own new
  interior points, having failed to establish a genuine excursion, are
  reported as context (their `Y`, where floor-passing) but not added as
  zone-defining members, since a smoothly-collapsing trough carries no new
  classification information beyond what 40.0°/40.2°/41.4° already supply.
- **STILL AMBIGUOUS** → the `n=8` table stands as built above; explicitly
  report the zone as **provisional pending item 1's own unresolved
  interior**, not silently treated as final — the literal "report both
  readings pending item 1's outcome" instruction, discharged as: one
  reading (the `n=8` table as-is) plus an explicit disclosure that the
  interior near-null remains unclassified and could, on a future denser
  check, still add a member on either side of the boundary.

**Calls: 0** (desk only, using item 1's and item 3/5's own already-
collected `cpl=30` primitives).

### 7. Item 4 — the Yee-grid dispersion phase-accumulation integral (MANDATORY, desk-only, computed now)

**Why this is mandatory, not ranked.** Named once (exp-091's own Phase-5 EM
review, `phase5_review_em.md` §4), restated a second time without running
it (exp-092's own Phase-1 §1, the identical qualitative "accumulated
propagation phase" claim), caught unrun a second time at exp-092's own
Phase-5 self-review by the same seat. Red Team's exp-092 final audit ruled
this non-firing under R8 only because it was not yet outcome-determining,
and named explicitly: **a third citation without running it fires
Checkpoint criterion 4 automatically.** This section is that check, run.

**Method.** The 2D isotropic Yee-grid numerical dispersion relation
(Taflove & Hagness; grid units `dx=dy=1`, `c=1`, this bench's own
`courant_frac=0.99` giving Courant number `S=courant_frac/√2≈0.700036`,
`lab/fdtd2d.py::Sim.__init__`):

```
(1/S²) sin²(πS/cpl) = sin²(k cosθ / 2) + sin²(k sinθ / 2)
```

solved numerically (Brent's method) for the numerical wavenumber magnitude
`k(θ, cpl)` at each census/near-null angle, against the ideal
`k₀=2π/cpl`. **The formula is exactly symmetric under `θ↔90°−θ`**
(independently verified: `k(41.4°)` and `k(48.6°)` agree to 12 significant
figures), so the ambiguity in which grid axis this bench's own `angle_deg`
convention is measured from does not affect the result — no idealization
needed on that point.

**Length scale — the aperture's own known differential geometry, not a
searched constant (R5 does not apply: this is one pre-declared, physically
motivated length, not a search over many candidate constants).** `G40`'s
sole geometric difference from `C40` is `PAD` (`design_geometry.py::
r3_config`): 40 cells native / 60 cells at R3, added symmetrically around
the whole domain. A residual-reflection echo model (this bench's own
established `pad_round_trip_echo_model`, exp-077) means the differential
propagation path between the two configs is the **round-trip PAD
distance**: `ℓ_native=2×40=80` cells, `ℓ_R3=2×60=120` cells — verified to
correspond to the identical physical length at both resolutions
(`80×(600nm/20)=120×(600nm/30)=2400nm`, consistent with the R3-scaling
rule's own "same physical geometry" convention).

**Computed result (my own pre-verification, via a standalone desk script,
not FDTD — to be independently reproduced bit-exact by a committed Phase-4
desk script before this document's own numbers are cited as settled,
matching R4's discipline and EM's own Rank-2 precedent in exp-092):**

| θ | Δφ(cpl=20) | Δφ(cpl=30) | Δφ(30)−Δφ(20) | predicted Δθ (`P*=2.8421°`) | observed Δθ |
|---|---|---|---|---|---|
| 37.2° | −0.2742° | −0.1216° | +0.1526° | +0.00121° | — |
| 40.2° | −0.1419° | −0.0629° | +0.0790° | +0.00062° | — |
| 40.0718° (lower) | −0.1463° | −0.0649° | +0.0814° | +0.00064° | **−0.194°** |
| 41.4° | −0.1059° | −0.0469° | +0.0589° | +0.00047° | — |
| 41.7811° (upper 1) | −0.0966° | −0.0428° | +0.0538° | +0.00042° | **+0.320°** |
| 41.8377° (upper 2) | −0.0953° | −0.0422° | +0.0530° | +0.00042° | **+0.377°** |

`predicted Δθ` maps the differential accumulated-phase error onto a
crossing-location shift via `Δθ = (ΔΔφ/360°)×P*`, using T28's own
established `P*=2.8421°` period as the local phase-to-angle conversion
(dimensionally consistent — a fraction of one full period maps to a
fraction of `P*` in θ, R9-compliant, both operands in degrees).

**Falsifiable finding, stated in advance of Phase-4 reproduction:**
predicted `|Δθ|` is **2–3 orders of magnitude smaller** than every observed
shift (ratio range **301×–900×**, computed directly from the table above).
**Reversal check (secondary, disclosed with lower confidence than the
magnitude result — convention-independent; the sign mapping is not):** the
model predicts a uniformly *positive*-direction shift at every angle
tested, matching the observed upper-window direction (+0.320°/+0.377°) but
**not** the observed lower-crossing direction (−0.194°) — a second,
independent strike against this specific mechanism/length-scale pairing,
though sign-convention interpretation carries more uncertainty than the
magnitude comparison and is reported as secondary for that reason.

**What this settles, and what it does not.** This REFUTES "differential
Yee-grid dispersion phase, accumulated over the PAD round-trip distance, at
this bench's own actual resolution and Courant number, is sufficient to
explain the observed `cpl 20→30` crossing-location shifts" as a
quantitative claim — the single most natural, pre-registered candidate
length scale for this mechanism, cleanly and by a wide margin. It does
**not** rule out numerical dispersion as *a* contributing factor at some
other, longer effective path (the reverse calculation shows an effective
length of `24,000–72,000` cells would be needed — 40–130× the entire
simulation domain, `nx≈360–660` cells — which has no known physical
referent in this bench's own geometry, and is disclosed as such, not
proposed as a new length-scale hypothesis to chase). MATERIALS' own T10
near-field/curved-boundary precedent remains the better-supported
qualitative account of *why* resolution refinement moves this feature; this
section closes the twice-cited *dispersion* claim specifically, not the
open mechanism question generally.

**Calls: 0** (desk-only; the standalone verification script is not `lab/`
code and touches no committed experiment file — a Phase-4 script will
reproduce this table from the same formula, committed to
`experiments/093-.../`).

### 8. Full parameter table — geometry, `cpl`, `STEPS`, `sigma_max`, configs, call counts

All geometry (`R3_RATIO=1.5`, `R3_CONFIGS`, `PEC_R_R3`, `R3_R_OUT_CELLS`,
`BOX_CLEARANCE_A/B_R3`, `REF_HALF_H_R3`, `DENSE_ANGLES`) reused verbatim
from `experiments/069-.../design_geometry.py` and
`experiments/091-.../092-.../run.py` — zero new `lab/` diff, zero new
geometry formula. `λ=600nm` throughout, matching every T28 cycle.

| Order | Item | Configs | Angles | `cpl` | `STEPS` | `sigma_max` | Leg(s) | Calls |
|---|---|---|---|---|---|---|---|---|
| 1st | **5 — NETD backfill** | `C40_R3`, `G40_R3` | 39.2°, 39.4°, 39.6°, 39.8°, 40.0°, 41.8°, 42.0° (7, existing grid) | 30 | 4200 | 0.5 (native) | empty+article | **28** |
| 2nd | **3 — sigma check, near-null** | `C40_R3`, `G40_R3` | 41.8°, 42.0° (2, existing grid) | 30 | 4200 | 1/3 (corrected) | article only (empty reused from item 5) | **4** |
| 3rd | **1 — denser sweep** | `C40_R3`, `G40_R3` | 41.750°, 41.775°, 41.825°, 41.850°, 41.875°, 41.900° (6, off-grid, 0.025° step) | 30 | 4200 | branch-gated on item 3 (§5) | empty+article | **24** |
| 4th | **2 — caution-zone re-fit** | — (desk only) | — | — | — | — | — | **0** |
| any time | **4 — dispersion integral** | — (desk only) | 37.2°, 40.2°, 41.4°, 40.0718°, 41.7811°, 41.8377° | — | — | — | — | **0** |
| declined | **6 — extend past 42.0°** | — | — | — | — | — | — | **0** |
| | | | | | | | **Total** | **56** |

**Cost** (`dg069._cost(key, steps, cell_ratio)` at `steps=4200,
cell_ratio=R3_RATIO²=2.25`, identical basis exp-091/092 used,
`cost(C40_R3)=168.75` CPU-s/call, `cost(G40_R3)=234.9` CPU-s/call,
disclosed as an estimate, not a measurement):

| Item | Calls | CPU-s |
|---|---|---|
| 5 (7 angles, both legs) | 28 | `7×2×(168.75+234.9) = 5651.1` |
| 3 (2 angles, article leg only) | 4 | `2×(168.75+234.9) = 807.3` |
| 1 (6 angles, both legs) | 24 | `6×2×(168.75+234.9) = 4843.8` |
| **Total** | **56** | **11302.2 CPU-s ≈ 188.4 CPU-min** |

Wall time at `N_WORKERS=4, PARALLEL_EFFICIENCY=0.98, OVERHEAD_FACTOR=1.15`
(unchanged house constants): `wall_s = 1.15×11302.2/(4×0.98) ≈ 3315s ≈
55.3 min`; 3× safety envelope ≈ 166 min.

**Budget disclosure (stated plainly, not minimized):** `188.4` CPU-min sits
**above** this sub-thread's own established `~100–150` CPU-min per-cycle
band (exp-091: 125.6; exp-092: 134.6). This is the first Iteration-70-class
cycle combining **five** reconciled queue items (vs. exp-092's three); item
5 alone (`94.2` CPU-min) reproduces exp-092's own already-spent Rank-1 cost
exactly, because backfilling dropped fields requires a full deterministic
re-run, not a cheaper partial one (§3's own verified reasoning) — Red
Team's own audit named this the one item it could not close additively.
Item 6 is declined explicitly on these grounds (§9), keeping the overrun to
what the mandatory/near-unanimous items actually require.

**Applied unchanged:** `XI_TOL=0.12`, `NOISE_MULT=3.0`, `RATIO_LOW/HIGH=
0.1/10.0`, `FLOOR_FRAC=0.10`, `FLOOR=1.91744×10⁻⁴` (applied unrecomputed
against every new point, in items 1/3/5 alike — a disclosed mixed-
resolution comparison only where the comparator is `cpl=20`; item 2's own
`n=8` table is `cpl=30`-only throughout, so no mixed-resolution comparison
exists there specifically).

### 9. Explicitly out of scope this cycle, named forward

- **Item 6 — extend the search past 42.0°.** Declined on budget grounds
  (§8); the true picture beyond the window edge remains unknown, unchanged
  from exp-092's own disclosure.
- **Tier 2 (exp-092's own numbering) — a third `cpl=40` resolution point**
  at the original three census angles: still premature (still no settled
  reason to center it anywhere new), unchanged.
- **Tier 3 — extending R3 to exp-090's remaining four caution-zone points**
  (36.0°, 38.4°, 38.8°, partial 41.8°): still deferred, unchanged. This is
  exactly why item 2's own `n=8` table (§6) cannot yet be a full
  replacement for the original `n=7` — three of its seven original members
  have no `cpl=30` measurement at all.
- Also untouched, standing: PHOTONICS' own grazing-incidence validity
  check (still the single most-repeated item on the whole T28 board); the
  x-wall wavelength-generality leg (076–093, now **eighteen** consecutive
  cycles deferred); the still-queued R14(b) formal null-controlled period
  fit; the Rank-2-in-exp-090's-own-queue unbiased margin-vs-distance
  rebuild on the full 31-point window; VISION's own restated
  ritualization/governance question (Iteration 61), unchanged, not
  re-litigated here.

### 10. Idealizations

**Carried forward from exp-092's own NOTES.md (not re-derived, not
renumbered — cited by exp-092's own original numbers so future cross-
references stay stable):**

3. **NETD is not a human-eye threshold.** Nothing in this cycle bears on
   constraint-3/4's human-eye verdict; `REALIZABILITY_MEMO.md` is not
   re-opened or re-scored.
6. **`FLOOR`/`RMS[frac_contrast]` applied, not recomputed,** against every
   new `cpl=30` point in items 1/3/5 — a disclosed mixed-resolution
   comparison (item 2's own `n=8` table is the one exception, §6).
7. **This cycle does not test constraints 1/2/3/4 and takes no T1
   escape-route position.**
11. **A Rank-3-style REFUTE/NEITHER-default (here, item 3's own verdict)
    reopens item 1's own net-placement/sigma choice as provisional for a
    future cycle** — resequencing fixes which article item 1's 24 calls
    measure; it does not, by itself, revalidate whether the flanking
    anchor points (41.6°/41.8°/42.0°, all native-`sigma_max`) remain
    directly comparable if item 3 fires REFUTE/NEITHER (§5's own explicit
    disclosure).

**New this cycle:**

12. **Item 4's own length-scale choice (round-trip PAD distance) is one
    pre-declared, physically motivated candidate, not an exhaustive
    accounting of every possible dispersion path** — the reverse
    calculation's own implied `24,000`–`72,000`-cell effective length has
    no known physical referent in this bench's geometry and is not
    proposed as a replacement hypothesis (§7).
13. **Item 4's `θ↔90°−θ` symmetry check (§7) is a formula-level property,
    independently verified to 12 significant figures, not a claim about
    which physical axis this bench's own `angle_deg` convention actually
    measures from** — the underlying convention itself is not
    re-derived this cycle.
14. **No settling re-check at item 1's/item 3's new angles** — `STEPS=4200`
    at `cpl=30` is cited as already clean from exp-091's own `(c1)/(c2)`
    result at this identical `STEPS`/`cpl` pair, on the same reasoning
    exp-092's own Idealization 8 stated (a checked margin many orders of
    magnitude larger than any plausible angle-to-angle variation), not
    independently re-verified at these specific new angles.
15. **Item 2's own `n=8` table treats `40.0°`/`40.2°` as two independent
    `Y=1` members rather than resolving whether they represent the same
    underlying feature at two adjacent angles** — a genuine simplification,
    disclosed, not resolved this cycle.

**Carried idealizations banner (mandatory at both this section and the
future Result section, per the Iteration-65 CHECKPOINT's escalated,
non-discretionary rule): every prediction in §11 below is governed by
Idealizations 3/6/7/11 (exp-092's own numbering, carried forward unchanged)
plus this cycle's own 12–15.**

### 11. Falsifiable predicted outcomes (per scored item)

**(Item 5) PRIMARY — reproduction.** **CONFIRM** = `delta_scene`,
`frac_contrast`, `ratio_k`, `floor_pass` at all 7 angles reproduce
exp-092's own filed `rank1.per_theta` values to float equality. **REFUTE**
= any disagreement — itself a significant, unanticipated finding about this
bench's own determinism, investigated before trusting the rest of this
cycle's own results (mirroring exp-092's own empty-leg-consistency
precedent exactly).

**(Item 5b) informational, non-gating — NETD threading.** Predicted:
`dt_ss_full_K` in the range `1×10⁻⁵`–`5×10⁻⁴` K at all 14 cells (both
configs, all 7 angles), all classifying **UNDETECTABLE** against
`NETD_BAND_K=(0.020, 0.050)` — consistent with Rank 3's own already-filed
C-config values at this identical `STEPS`/`cpl` (`4.6×10⁻⁵`–`5.2×10⁻⁵` K) and
with T9's established near-saturation anchor. Falsifiable: a `MARGINAL` or
`DETECTABLE` reading at any cell, or a `dt_ss_full_K` outside the stated
range by more than 3×, is reported as a genuine surprise, not smoothed
into the prediction after the fact.

**(Item 3) PRIMARY, gates item 1's `sigma_max` — does the sigma-corrected
article move `delta_scene`/`frac_contrast` materially at the near-null
angles specifically?** Same `[0.3,3.0]` CONFIRM / `[0.1,10]` REFUTE bands
as Rank 3. **No confident directional lean** — Rank 3's own CONFIRM at
three broader census angles is informative but, per Red Team's own scope
correction, does not extend to this specific region; this is the
affordable check that closes that exact gap.

**(Item 3b) informational, non-gating** — co-equal `p_abs_w` ratio check at
the same two angles, mirroring Rank 3b; `ratio_abs_ext_raw` checked for
remaining within `~2–3%` of the `0.51` T9 anchor, informational only.

**(Item 1) PRIMARY — three-way outcome, §5's own falsifiable categories
(TWO-NODE CONFIRMED / SINGLE-NULL / STILL AMBIGUOUS).** No confident
directional lean stated in advance (§5).

**(Item 2) PRIMARY — the base `n=8` `cpl=30`-only zone (unconditional,
already pre-verified in §6) reproduces bit-exact when Phase 4's committed
script recomputes it live: `AUC=0.0000`, zone `[4.1083, 5.4287]` (not
inverted), Firth `β=[3.7650,−5.6070]`, `m₅₀=4.6934`, naive MLE diverges.**
**CONFIRM** = reproduces to ≥4 significant figures. **REFUTE** = any
disagreement, investigated not silently reconciled — the same falsifiable-
recomputation standard exp-092's own Rank 2 used. **(Item 2, extension)
gated on item 1 (§6's own three-way branch)** — no pre-registered numeric
band for the extension itself, since its content depends entirely on which
of item 1's three outcome categories fires; reported as a location/
composition disclosure, not a pass/fail test.

**(Item 4) already computed (§7) — falsifiable claim stated in advance of
Phase-4 reproduction:** the desk script reproduces the §7 table to ≥4
significant figures, and the magnitude ratio (observed vs. predicted
`|Δθ|`) stays in the **`100×`–`1000×`** range at each of the three
angles with a known observed crossing shift (lower, upper 1, upper 2)
(i.e., a REFUTE of the dispersion-alone mechanism by at least two clear
orders of magnitude, not a near-miss). The three non-crossing census
angles (37.2°/40.2°/41.4°) carry no observed shift to compare against and
are reported for the table's own internal consistency only.

### 12. T1 escape route

**N/A**, verified directly against LOGBOOK.md's own record, not asserted on
precedent alone: every T28 sub-thread entry from Iteration 46 (exp-069)
through Iteration 69 (exp-092) states "T1 route N/A"/"Checkpoint criterion
2: N/A" — independently re-confirmed here by grep against the committed
LOGBOOK.md text (every `T28` iteration entry's own Phase-1/Combined-Verdict
language), matching exp-092's own Red Team audit's identical verification
method (`phase5_redteam_audit.md` §6). This cycle takes no position on
σ(I)/σ(x,t)/angular selectivity/sub-threshold operation, makes no
phenomenon-mechanism claim, and does not touch `REALIZABILITY_MEMO.md`. It
is pure instrument recalibration and energy-sidecar instrumentation of the
AMBIENT channel's own R13/R15 machinery.

### 13. Confirming this design does not re-open ruled-out ground (R1–R15, checked individually)

- **R1/R2** — N/A, no phenomenon-mechanism or shell-thickness claim.
- **R3** — this cycle **is** R3's own meta-rule applied again (item 1: a
  resolution check on a surprising feature before any mechanism debate).
- **R4** — item 4's own figures are produced by an actual Python
  computation (not hand-typed arithmetic), disclosed explicitly as
  pre-verification pending bit-exact Phase-4 reproduction, matching EM's
  own Rank-2 precedent in exp-092.
- **R5** — item 4's length scale is one pre-declared, physically motivated
  candidate (the PAD round-trip distance), not a search over a named-
  constant space; no null-permutation control is owed (§7's own explicit
  distinction). No other item in this proposal searches a parameter space.
- **R6/R7** — N/A, no carrier/phase-conditioned fit, no conditioning-only
  closure or detection claim.
- **R8** — item 4 directly discharges the standing tripwire (§7): the
  named, affordable check is now actually run, not argued a third time.
- **R9** — item 4's own Δθ mapping is checked for unit consistency
  explicitly (§7): both operands (`ΔΔφ`, `P*`) are expressed in degrees
  before the ratio is taken.
- **R10/R11** — N/A, `find_zero_crossings` is a linear-interpolation
  zero-finder, not the staged-widening `free_period_with_widening`
  machinery either rule concerns; no free-period/free-phase fit is made.
- **R12** — N/A, no tail-statistic "negligible effect" claim across
  seeded noise (this bench's FDTD is deterministic, not stochastic).
- **R13** — applied unchanged throughout (§8): every new point's
  `floor_pass` gates its own classification; a floor-failing point is
  never silently scored alongside floor-clearing ones.
- **R14** — applied unchanged: item 5's own `frac_p_abs` numerator (§3)
  inherits the same numerator-distrust caution R14 established; the NETD
  backfill is reported per-cell, not used to drive any new classification
  claim this cycle, so R14's own minimum-discharge conditions are not
  triggered by it.
- **R15** — item 1/item 2 together are the direct completion of R15's own
  founding mandate (a caution zone must be independently R3-verified
  before being trusted); item 2's own `n=8` table is the first
  `cpl=30`-only version of this boundary this sub-thread has ever built.

No R1–R15 rule is violated, re-litigated, or silently worked around. No new
numbered rule is proposed.
