# exp-100 — First Constraint-1/2/3 Scoring Pass on `delta_scene(θ)`,
Gated on a PAD-vs-Article Partition (Panel Iteration 77)

*Panel Iteration 77. Lead seat (rotation): QUANTUM OPTICS. Director synthesis
of `phase1_proposal.md` (QUANTUM OPTICS) after five blind Phase-2 critiques
(PHOTONICS, MATERIALS, ELECTROMAGNETISM, THERMODYNAMICS, VISION SCIENCE —
unanimous support-with-changes) and Red Team's Phase-2 audit
(PROCEED-WITH-MANDATORY-FIXES, 9 numbered attacks, 0 critiques overridden, 3
new defects Red Team itself found independently). Executes exp-099's own
Reconciled Iteration-77 queue: Tier 1 (mandatory preconditions) + Tier 2 (the
constraint-1/2/3/4 scoring pass, seven-cycles-deferred).*

## Hypothesis

No new T1 escape-route mechanism is proposed. Three questions:

1. **Does `delta_scene(θ)` — this sub-thread's own ~2.9474°-period `C40`/`G40`
   diffraction signal — carry genuine article-coupled content, or is it a
   pure domain/`PAD` artifact with zero realizability content?** (Tier 1,
   item 1: a zero-FDTD correlation test against `frac_p_abs(θ)`, the only
   already-persisted proxy for article-toggled/PAD-fixed content, since raw
   per-config Weber contrast is never persisted.)
2. **What does that finding, plus the already-inert `cpl` fact, imply about
   `delta_scene`'s own realizability tier?** (Tier 1, item 2, MATERIALS.)
3. **Is the climbing 0.7765→0.9623 marginal Richardson ratio at Null B
   genuine-but-slow convergence or a non-convergent recipe artifact?** (Tier
   1, item 3 — zero new FDTD, full stored precision.)
4. **Does `delta_scene(θ)`'s own magnitude — measured for the first time
   against the program's own constraint-1/2/3 instruments on this specific
   bench — pose any real threat to beam termination, specular return, or
   the ambient-silhouette bound?** (Tier 2 — the seven-cycle-deferred
   scoring pass, honestly labeled whichever way Tier 1 comes out.)

Nothing below re-proposes a RULED-OUT idea (R1–R20 read in full by every
seat, confirmed independently by Red Team).

## Changes from Phase 1, per Red Team's Phase-2 audit (9 attacks; all 9
mandatory fixes ADOPTED in full; 0 critiques overridden; 3 new defects Red
Team itself found independently — RT-1, RT-2, RT-3)

Director's ruling: I accept every one of Red Team's nine rulings without
override. Red Team independently re-verified the load-bearing claims in all
five blind critiques from source (not on any seat's word) before ruling, and
additionally re-derived EM's electromagnetic claim (RT-4) from primitives by
an independent route (the pseudovector-parity argument), confirming it
exactly. None of the fixes below is cosmetic; three (RT-1, RT-3,
THERMODYNAMICS/fix-7) sit directly on this program's own most sensitive
standing tripwires and are treated as such.

1. **(RT-1, Red Team's own finding — ADOPTED, mandatory, option (a)
   chosen).** Leg B's original four angles (37.127246°, 38.590230°,
   40.265420°, 41.460901°) are `delta_scene(θ)`'s own zero-crossings
   (`experiments/090-.../run.py`'s `find_zero_crossings` applied directly to
   `delta_scene`) — the worst possible sampling for testing whether the
   signal's *ripple* threatens constraints 1/2. **Fix**: add the two
   largest-magnitude already-filed `delta_scene` values in the
   characterized 36°–43° window, both cpl=40/`R4` family (no new angle
   invented, no fresh derivation of a predicted extremum — pure reuse of
   filed data, per R4 discipline): **θ=42.960901°** (`delta_scene
   =+2.778079×10⁻³`, exp-099) and **θ=40.960901°** (`delta_scene
   =+2.471869×10⁻³`, exp-099). Leg B now runs **6 angles**, not 4.
2. **(RT-2, Red Team's own finding — ADOPTED, mandatory).** Tier-1 item
   1(a)'s correlation test had no pre-registered decision threshold.
   **Fix, committed now**: "coupling detected" requires BOTH the 20,000-trial
   permutation two-tailed `p<0.05` AND `|r|≥0.2` (a conventional small-to-
   medium effect-size floor, chosen because the pooled `n`≈80+ rows makes a
   physically negligible `r` statistically detectable on `p` alone).
   Failing either condition → "majority-PAD / no significant coupling."
   Family-stratified `r` (R3/R4/R5) uses the same joint rule per family.
3. **(RT-3, Red Team's own finding — ADOPTED, mandatory, the single most
   important fix this cycle).** Tier 2 was not actually gated on Tier 1's
   outputs as LOGBOOK's own Iteration-76 commissioning language requires
   ("gated on Tier 1's outputs but not deferred an eighth cycle") — a live
   risk of an eighth T1:N/A deferral dressed as progress, given the
   proposal's own predicted lean is that Tier 1 finds no coupling. **Fix,
   pre-registered now, before any run**: the cycle's own Combined Verdict
   T1-label is fixed in advance per Tier-1 outcome —
   - Tier 1 finds **majority-PAD / no significant coupling** (item 1's
     joint rule fails) → Combined Verdict states **T1: N/A, `delta_scene`
     excluded from the angular-selectivity class for this specific signal**
     — not narrated as "the first cycle to touch scoring." Tier 2's own
     numbers are still reported (they are the first real constraint-1/2
     FDTD measurement on this signal, a genuine instrument-build result)
     but explicitly filed as **characterizing a domain-geometry artifact's
     magnitude against perceptual/beam thresholds, not testing a material
     mechanism.**
   - Tier 1 finds **coupling detected** (joint rule passes) → Combined
     Verdict states **T1: angular-selectivity, partial/gated evidence**,
     scoped explicitly to this bench/λ=600nm/the tested angle window only.
   - Tier 1 is **ambiguous/underpowered** (e.g. a HALT before the
     correlation completes, or a family-stratified split contradicting the
     pooled result) → Tier 2's numbers are filed as
     **instrument-characterization only; T1 stays N/A, unresolved.**
4. **(RT-4/EM's fix — ADOPTED, mandatory, not merely non-blocking; Red
   Team independently re-derived EM's claim from primitives, confirming it
   exactly).** `observer_record_t28`'s proposed array-mirror construction
   ("flip Ez/Hy along x identically") is provably wrong: `Ez` is a true
   (polar) vector component in this TMz mirror-plane geometry and correctly
   mirrors under bare index reversal, but `Hy` is the pseudovector partner
   and requires an *additional* sign flip; omitting it exactly cancels the
   intended correction (`a_fwd=0, a_bwd=`full beam on the empty-scene
   capture — verified two independent ways, EM's and Red Team's own).
   **Fix, per EM's own specification, adopted verbatim**: no array mirror.
   Call `lab.emit.observer_record(sim, capture, plane_x, reference=None)`
   **unmirrored**, then swap which of its two already-correct scalar totals
   means "toward the observer" for this bench's geometry (`src_x > obj_x >
   plane_x`, opposite `emit.py`'s own assumed low-x/+x-source convention —
   the same mismatch `sections.widths()` already corrects for via
   `widths_direction_corrected`, exp-087/091, which uses a scalar sign
   correction, never an array mirror — EM's own precedent-consistency
   finding). Concretely: `observer_record_t28` calls `observer_record`
   unmirrored and reads `aux["p_forward_total"]` (the `a+`/+x-traveling
   total; this bench's own injected beam is the `a-`/-x-traveling wave,
   since the source sits at high-x) as the "returned-to-observer" power,
   normalized by `aux["p_backward_total"]` from the matching empty-scene
   reference capture (the injected beam's own power in this convention) —
   a scalar total-power comparison, matching the trust suite's own stage-6
   idiom ("empty room returns ~nothing," "mirror returns ~everything") at
   the same granularity, not a new angle-resolved measurement (disclosed
   as Idealization 67 below, replacing the now-moot Idealization 65).
5. **(RT-5, Red Team's own finding — ADOPTED, mandatory, bundled with fix
   4).** Idealization 65 (disclosing the array-mirror's own boundary-
   symmetry assumption) is deleted — the fixed construction has no such
   assumption. Replaced by Idealization 67 (below), stating the new
   construction's own actual scope limit (scalar total, not angle-resolved).
6. **(MATERIALS' fix — ADOPTED, mandatory, zero marginal cost).** Tier-1
   item 2 ("disposition memo") was a category error as scoped: neither of
   `delta_scene`'s two candidate readings (pure PAD/domain artifact, or
   diffraction off the already-published `graded_black_shell` geometry)
   requires a published/plausible/unobtainium realizability verdict for a
   *new* structure. **Fix, MATERIALS' own proposed conditional, adopted**:
   item 2 is rescoped to a pre-registered per-outcome disposition, decided
   by item 1's own finding — (i) majority-PAD → "`delta_scene`'s dominant
   identity is a domain-geometry artifact; no realizability tier applies,
   it is not a material property to bound"; (ii) coupling detected → "the
   coupled residual is a diffraction consequence of the already-published,
   already-realized `graded_black_shell` rim geometry — **published**, no
   new material or structure required"; (iii) ambiguous → "disposition
   deferred, no realizability claim made this cycle." This mirrors, one
   level down, the same per-outcome pre-registration fix 3 applies to the
   cycle's own headline T1 label.
7. **(THERMODYNAMICS' fix — ADOPTED, mandatory, elevated severity: a
   credible THIRD occurrence of R16's own named pattern).** `netd_row()`
   was listed among Tier 2 Leg B's reused functions but never actually
   invoked on the new cells — the same "disclaimer travels, byproduct not
   persisted" shape as exp-092/93 (closed) and exp-094 (R16's founding
   instance) and, per Iteration 76's own THERMODYNAMICS self-review, this
   sub-thread's own R5 landmark points. R16's forward clause: a third
   occurrence fires Checkpoint criterion 4 automatically. **Fix, committed
   now**: `netd_row()` is called on **all 6** new `(C40_R4,G40_R4)` pairs
   (matching fix 1's expanded 6-angle Leg B) and the result is persisted in
   `results.json` under each angle's own report row, disclaimed per
   `lab/thermo_sidecar.py`'s own EXPRESSIBILITY CONTRACT (a post-run
   analytic sidecar, not an FDTD output). This is treated as load-bearing,
   not optional: Phase 4 code must assert all 6 rows carry a `netd_row`
   sub-dict before `results.json` is written, or halt.
8. **(VISION-a's fix — ADOPTED, mandatory).** `C_thr(L)` is T2's own
   static, steady-adaptation, extended-uniform-patch threshold
   (Iteration-1 idealization ii: "area contrast, not edge-profile
   detectability"); `delta_scene(θ)` is a ~2.9474°-period oscillation whose
   content only exists as θ sweeps — the transient/modulation regime T3
   (still this program's longest-standing unbuilt instrument) was built to
   score, not T2. **Fix**: any Leg-A PASS/FAIL reading is reported
   explicitly as **a static-contrast bound only, provisional pending T3 —
   not a completed Tier-W/Tier-A verdict on a swept angular fringe.** The
   "complete both tiers" language in the original proposal is struck.
9. **(VISION-b's fix — ADOPTED, mandatory; a clean R4-class citation
   defect caught at Phase 2, before freeze).** The proposal's cited
   scotopic anchors (`L*≈5×10⁻⁶`–`4×10⁻⁵`, moonless-rural`≈1.7×10⁻⁴`
   cd/m²) are digit-for-digit Iteration-1's **superseded pre-correction
   draft** numbers, not the corrected band Phase-3 actually committed.
   **Fix**: replaced throughout with the corrected, committed band —
   **`L*_lab∈[5.3×10⁻⁶,7.5×10⁻⁵]`, `L*_field∈[1.7×10⁻⁴,1.2×10⁻³] cd/m²`**
   (LOGBOOK.md, Iteration-1 Phase-3 synthesis).

## Setup

All FDTD calls reuse, unmodified: `Sim`/`add_line_source` (`lab/fdtd2d.py`),
`r4_config()`/`R4_CONFIGS` (`experiments/069-.../design_geometry.py`, as
`dg`), the registration-readback gate (`run_checks_1234_and_7`/
`check6_positional_and_cpl`, `experiments/097-.../run.py`),
`cell_metrics_r4`/`run_block_r4`/`pair_metrics_full`/`netd_row()`
(`experiments/094/093-.../run.py`), `find_sign_change`/
`richardson_style_diagnostic` (`experiments/098-.../run.py`), and
`lab.emit.observer_record`/`lab.sections.flux_profile_x` (unmirrored,
scalar-relabeled per fix 4 — zero `lab/` diff). λ=600nm only, 2D TMz
(Idealization 1).

### Tier 1 — 0 new FDTD calls

**Item 1 — PAD-vs-article partition.** Pool every filed `(θ,family)` cell
with a `pair_metrics_full`-derived row from `experiments/{087,088,089,091,
092,093,094,095,098,099}-.../results.json`, read by actual stored keys
(never hand-typed). Compute (a) Pearson `r(delta_scene, frac_p_abs)` with
the 20,000-trial random-permutation null (justified per R10: an assembled,
non-time-ordered census has no circular-shift operation), scored against
fix 2's joint rule (`p<0.05` AND `|r|≥0.2` ⇒ coupling); (b) the same,
family-stratified (R3/R4/R5 — a real systematic should recur per R15); (c)
`Δratio_abs_ext(θ) = ratio_abs_ext_raw_g − ratio_abs_ext_raw_c`, testing
whether T9's established <0.1% flatness (exp-087) holds at this larger `n`.

**Item 2 — MATERIALS' disposition memo**, rescoped per fix 6: a short,
citable file (`disposition_memo.md`) stating the per-outcome conditional
above, decided by item 1(a)'s own joint-rule result.

**Item 3 — 4-point Richardson characterization at Null B.** Pull
`shift_20_30`/`shift_30_40`/`observed_ratio=0.7765163757372424`
(`experiments/098-.../results.json::richardson_diagnostic.B`) and
`shift_40_50`/`observed_ratio≈0.9623`
(`experiments/099-.../results.json::item_2.step3`) at full stored float
precision. Compute: (a) raw-magnitude monotonicity of
`|shift_20_30|`/`|shift_30_40|`/`|shift_40_50|` at full precision (not the
6-decimal display exp-099's own prose used); (b) implied local order
`p_i=ln(r_i)/ln(cpl_i/cpl_{i+1})` for both available ratios, reported
descriptively (Idealization 49 — no continuum reference value exists, `n=2`
is too few points to fit an asymptotic order).

### Tier 2 — the scoring pass, per outcome per fix 3

**Leg A — `C_thr(L)` desk score, 0 new FDTD.** Score item 1's full pooled
`delta_scene(θ)` table (36°–43° window only) against `C_thr(L) =
0.005·max[1,(L/3)^−p]`, `p∈{0.4,0.5}`: photopic bars 0.005/0.02 (Tier A),
and the corrected scotopic band (fix 9) for Tier W. Reported per fix 8's
caveat (static-contrast bound only, pending T3) and per PHOTONICS' fix
(Idealization 64, unchanged: 600nm-only, LOGBOOK's own established T21
750nm/θ=40° fringe — 0.0237, 4.7×`C_thr`, in this identical window —
disclosed as an unaddressed same-window contamination-risk precedent, NOT
tested this cycle).

**Leg B — direct FDTD legs, constraints 1 and 2, 6 angles (per fix 1) ×
2 keys (`C40_R4`,`G40_R4`) × 2 conditions (empty/article) = 24 `sim.run()`
calls.** Angles: **37.127246°, 38.590230°, 40.265420°, 41.460901°**
(established cpl=20 zero-crossings, `experiments/090-.../results.json::
q8.crossings_deg`) **+ 40.960901°, 42.960901°** (the two largest-magnitude
already-filed `delta_scene` values in this window, fix 1). Registration-
gate-clean (Checks 1–7) required before each. From the same captures
(`sc.full_capture`, already needed for `cell_metrics_r4`), zero marginal
`sim.run()` cost: **(i) `beam_behind_t28`** — `sections.flux_profile_x`,
sign-negated (matching `ambient.observer_profile`'s own established
convention — this extraction was already correct in the original proposal,
confirmed by EM), scene/empty ratio at a plane ~10 cells past the object's
outer radius. **(ii) `observer_record_t28`** — per fix 4, an unmirrored
`observer_record` call with `p_forward_total`/`p_backward_total` relabeled
for this bench's geometry, normalized against the matching empty-scene
reference capture's own `p_backward_total`. **Mandatory validation gate
(R18)**: on the empty-scene captures already collected in this same spend,
`observer_record_t28` must read near the established camera-floor scale
(stage-6's own "empty≈0" gate) before any article-loaded reading from
these same 24 calls is trusted — zero extra calls. **Thermal sidecar (fix
7)**: `netd_row()` called and persisted for all 6 new pairs, asserted
present before `results.json` is written.

## Idealizations

**Carried forward** (exp-096–100, cited by number, unchanged): 1 (2D TMz,
600nm only), 17 (R3/R4/R5 share one mechanical recipe), 38/39/42 (Check 5
has never tested a `G40_*` padded config — applies to the 12 new `G40_R4`
calls in Leg B), 49 (any Richardson-style figure is descriptive only), 62
(the `frac_p_abs` proxy is the only recoverable analog of the literal
article-toggled/PAD-fixed leg — a found correlation is evidence of
coupling, its absence does not certify zero coupling on every channel), 63
(`frac_p_abs` and `delta_scene` share the same four FDTD calls per row — a
correlation may reflect shared variance from one underlying `σ_ext`
differential, not two independent instruments agreeing), 64 (Leg A is
600nm-only; the established 750nm T21 fringe in the same window is an
unaddressed contamination-risk precedent, not tested this cycle), 66 (a
clean Leg-A reading bounds only the already-measured angle set, not a
survey).

**Deleted this cycle**: 65 (the array-mirror's own boundary-symmetry
assumption — the construction it described no longer exists, per fix 4/5).

**New this cycle:**

67. `observer_record_t28`'s fix (unmirrored call + scalar total relabeling,
    fix 4) reports a single scalar power ratio per (angle, key), not an
    angle-resolved backscatter distribution — a coarser instrument than
    `emit.observer_record`'s own native angle-binned output, matching the
    trust suite's own stage-6 scalar idiom but disclosed as a scoping
    choice, not a defect: a future cycle wanting angle-resolved
    T28-geometry backscatter needs its own dedicated extraction.
68. Leg B's 6 angles (4 established zero-crossings + 2 largest-filed-
    magnitude points) are still not a survey of `delta_scene`'s own
    extrema — the 2 added points are the largest values *already
    characterized* in this window, not a located true maximum (the
    genuine local extremum near θ≈41.5°–42° per exp-099's own "bounce"
    finding, or any peak beyond 42.960901° where the signal was still
    climbing at the edge of exp-099's own tested span, remain unlocated).
    A clean Leg-B PASS bounds constraint-1/2 risk at these 6 specific
    points only.
69. Item 1(a)'s joint decision rule (fix 2, `p<0.05` AND `|r|≥0.2`) is a
    pre-registered convention, not a physically derived boundary — a
    different, equally defensible threshold could classify some borderline
    pooled result differently. Stated once, before running, per R7/R10.
70. Fix 3's three T1-label branches are exhaustive over item 1(a)'s three
    stated outcomes but do not anticipate every possible edge case (e.g. a
    family-stratified split that contradicts the pooled joint-rule result)
    — such a case is explicitly folded into the "ambiguous/underpowered"
    branch per this idealization, not left to post-hoc judgment.

**Carried idealizations banner: every prediction in this section
(§Predictions) is governed by Idealizations 1/17/38/39/42/49/62–64/66–70.**

## T1 escape-route disposition

**No new mechanism is proposed. This is genuinely gated, not merely
plausible, for a PARTIAL verdict — the honest scope, stated before any run,
per RT-3.** Tier 1 decides, zero-FDTD, whether `delta_scene` has any
material analog at all. Tier 2 Leg A fully scores the signal's own
magnitude against `C_thr(L)` within its own disclosed scope (static-
contrast bound, 600nm-only, pending T3 — fixes 8/64). Tier 2 Leg B gives
this bench's first-ever direct constraint-1/2 measurement, at 6 points
chosen to include both `delta_scene`'s established nulls and its largest
already-filed magnitudes — a first point, not a closure (Idealization 68).
**The cycle's own Combined Verdict T1-label is fixed in advance, per fix
3's three branches, before Tier 1 runs** — this is the specific,
structural answer to Red Team's own central worry (RT-3): whichever way
Tier 1 comes out, the label is pre-committed, so the result cannot be
narrated as "the first break in the seven-cycle streak" if the honest
finding is that `delta_scene` carries no article-coupled content.
**Checkpoint criterion 2 remains N/A**: even a clean Tier-1+Leg-A+Leg-B
result is not a proven mechanism-class boundary.

## Predictions (frozen before any Phase-4 code exists)

**Carried idealizations banner (duplicated into this section's own body,
per exp-098/099's own established fix): every prediction below is governed
by Idealizations 1/17/38/39/42/49/62–64/66–70.**

| Item | Metric | Predicted band / criterion | Confident lean? |
|---|---|---|---|
| T1-item1(a) | `r(delta_scene, frac_p_abs)`, pooled, joint rule (p<0.05 AND \|r\|≥0.2) | Genuinely open. Weak lean toward **majority-PAD / no significant coupling** (exp-076's lossless-vacuum proof, T9's established <0.1% `ratio_abs_ext` flatness) — not a confident lean, this exact pairing has never been tested. |
| T1-item1(a) | `Δratio_abs_ext(θ)`, pooled | Weak lean: stays <0.5% at every row (extends exp-087's own finding to larger n). |
| T1-item1(a) | Family-stratified `r` (R3/R4/R5) | No confident lean — a real cross-term should recur across families (R15); a pooled-only effect falsifies "genuine coupling" in favor of a family-specific artifact. |
| T1-item2 | Disposition memo branch taken | Contingent on item 1(a); weak lean toward branch (i) (majority-PAD → no realizability tier applies), matching item 1(a)'s own weak lean. |
| T1-item3 | Raw-magnitude monotonicity at full precision | Genuinely open — the entire point of pulling full float precision; no confident lean. |
| T1-item3 | Implied order `p₁`,`p₂` | No confident lean on values; weak lean `p₂<p₁` (deceleration continues, matching the ratio's own climb toward 1). |
| T2-LegA | `max\|delta_scene(θ)\|` (36°–43°) vs `C_thr_lab=0.005` | Weak-to-moderate lean: **stays below 0.005** at every tested angle (largest filed value, θ=42.960901°, `+2.778×10⁻³`, ≈56% of the lab bar) — reported as a static-contrast bound only (fix 8), not a completed Tier-A verdict. |
| T2-LegA | Tier-W (corrected scotopic band, fix 9) | If Tier-A leans PASS, Tier-W (looser bar at low L) leans PASS a fortiori — contingent on the row above, same static-bound caveat. |
| T2-LegB | `beam_behind_t28`, scene/empty, all 6 angles | No confident lean on the exact ratio; strong lean it stays close to the established `graded_black_shell` figure (1.5–1.8%, LOGBOOK ESTABLISHED) at all 6 angles — `delta_scene`'s own ≤10⁻³-scale ripple is a small perturbation on an already-opaque object. |
| T2-LegB | `observer_record_t28`, empty-scene validation gate, all 6 angles | Confident lean: **PASS** (reads near the established camera floor) — if this fails, article-loaded readings this cycle are UNINTERPRETABLE-PENDING-VALIDATION. |
| T2-LegB | `observer_record_t28`, article-loaded, at the 2 new largest-magnitude angles vs. the 4 established nulls | No confident lean on absolute values; weak lean that the 2 new (larger-`delta_scene`) angles show a detectably larger backscatter reading than the 4 null angles, if `delta_scene` has any constraint-2 relevance at all — the genuinely new comparison this cycle's fix 1 exists to make. |
| T2-LegB | Registration-readback gate, all 6×2×2 new points | Confident lean: **CLEAN** (zero exception across R4 to date). |
| T2-LegB | `netd_row()` presence, all 6 pairs | Confident lean: **present and asserted**, per fix 7 — a HALT here is a process failure, not a physics finding. |

## FDTD-call budget, self-checked

- Tier 1 (items 1–3): **0 `sim.run()` calls.**
- Tier 2 Leg A: **0 `sim.run()` calls.**
- Tier 2 Leg B: 6 angles × 2 keys × 2 conditions = **24 `sim.run()`
  calls.**
- **Grand total: 24 real FDTD calls**, plus 24 zero-cost registration-
  readback preflight checks (6 angles × 2 keys × 2 check-families) and one
  empty-scene `observer_record_t28` validation pass (0 marginal calls,
  reuses the 12 empty-leg captures already inside the 24).

Wall-time estimate, scaling from exp-099's own 40-call/148.32-min pace
(≈3.71 min/call): **≈89 minutes** for 24 calls.

## Result

*(to be filled at Phase 4, after the run — predictions above are frozen
and committed to git before any Phase-4 code exists.)*
