# Panel Iteration 75 — Phase 1 Proposal (ELECTROMAGNETISM, rotation lead)

## 1. Mechanism/change narrative (≤300 words)

This is a **T28 house-discipline/validation cycle, not a new T1 escape-route
proposal.** T28's underlying, already-committed program investigates
whether an **angular-selectivity**-class mechanism (a shell whose
ambient-scene contrast depends on incidence angle θ, via edge/aperture
diffraction near a shell wall — the y-wall/x-wall echo family, exp-078–085)
can be certified or refuted from FDTD evidence. The specific finding at
stake, `delta_scene(θ)` sign structure in the 36°–42° window, is not a new
mechanism claim this cycle proposes or defends — it is the metric the
whole angular-selectivity line depends on being trustworthy. exp-095's
Rank 1c found a FAIL (no sign change) at cpl=40 near one established
cpl=20 null (θ₀≈38.590230°) using an undersized bracket; R17 (adopted from
that exact defect) requires bracket sizing to be justified against
established cross-resolution migration precedent, not an illustrative
round number. exp-096/097 then built and R18-hardened a zero-FDTD
registration-readback gate proving the construction code (`Sim`,
`add_line_source`, `r{3,4,5}_config()`) is clean — Tier 1 real FDTD spend
is unanimously unblocked.

**What EM specifically contributes as lead:** the reciprocity/passivity/
causality lens on two questions this cycle turns real. First, bracket
sizing (R17): I apply the *already-audited* ±0.5° desk bound (exp-096,
Red-Team-ratified against the three known cpl20→cpl30 migration figures)
uniformly, rather than re-deriving a new number — R4's own discipline.
Second, the long-deferred grazing-incidence validity question (§7 of the
brief): I schedule, not defer, a zero-FDTD analytic pass on
`edge_diffraction_c_empty_corrected`'s own closed-form Green's-function
sum, checking it against two EM-native invariants — passivity (no
negative-flux artifact) and reciprocity (source/observer symmetry) — as
θ→90°, tied to the same near-field validity parameter (kr) that already
governs this whole window's trustworthiness. Zero new physics is asserted;
this is instrument-trust bookkeeping, in EM's own idiom.

## 2. Parameter table

All FDTD calls below reuse, unmodified, `Sim`/`add_line_source`
(`lab/fdtd2d.py`), `r{3,4,5}_config()`/`R{3,4,5}_CONFIGS`/`R{3,4,5}_RATIO`
(`experiments/069-.../design_geometry.py:192/265/350`, imported as `dg`),
`construct_sim`/`CPL`/`TAPER`/`PAIR_KEYS` (exp-096's `run.py`, loaded via
the `_load()` chain), and the registration-readback gate (Checks 1–7,
CLEAN per exp-097). λ=600nm only (2D TMz), matching Idealization 1
throughout.

### (i) Bracket the other three established cpl=20 nulls at cpl=40 — 24 calls

Established cpl=20 zero-crossings not yet tested at cpl=40 (LOGBOOK.md::
`q8.crossings_deg`, exp-090; independently re-read this session,
byte-exact): **θ₀ᴬ=37.127246°, θ₀ᴮ=40.265420°, θ₀ᶜ=41.460901°.**

**Half-width: ±0.500°, symmetric, per point** — the *same* number exp-096's
own desk bound already computed and Red Team ratified as "most defensible
of the three candidates examined" against the three known cpl20→cpl30
migration shifts (0.193582°/0.320166°/0.376752°, giving 1.33×–2.58×
margin). R17 requires justification against established cross-resolution
precedent for a *comparable transition* — this is the identical
cpl20→cpl40 transition class the 38.590230° bracket (item ii) already
established that bound for; reapplying it here, rather than deriving a
fresh number per null, is the disciplined move (R4: don't re-litigate an
already-audited figure). No directional prior exists for these three
(the migration set itself contains both signs: −0.194°, +0.320°,
+0.377°), so symmetric is the correct default absent one.

**4 angles per null, quartile-spaced across the bracket** (finer than the
largest known shift, 0.377°, so a real crossing cannot hide between two
same-sign samples the way the ±0.1°/2-point exp-095 design allowed):
offsets θ₀+{−0.500°, −0.1667°, +0.1667°, +0.500°}.

| Null | θ₀ (established, cpl=20) | Test angles (cpl=40) |
|---|---|---|
| A | 37.127246° | 36.627246°, 36.960580°, 37.293913°, 37.627246° |
| B | 40.265420° | 39.765420°, 40.098753°, 40.432086°, 40.765420° |
| C | 41.460901° | 40.960901°, 41.294235°, 41.627568°, 41.960901° |

Family/config: `R4` only (`cpl=40`), both legs `C40_R4`/`G40_R4` per angle
→ 3 nulls × 4 angles × 2 legs = **24 `sim.run()` calls.** Every
construction passes Checks 1–7 first (zero marginal FDTD cost — the gate
stops before `sim.run()`); this extends the gate's checked-point set
beyond exp-097's 16-point representative sample, which is good R18
practice, not a new gate design.

### (ii) Re-centered node-bracketing re-run at θ₀≈38.590230° — 8 calls

θ₀ = 38.590230° exact (37.127246379304516… family, per `q8.crossings_deg`).
exp-095's own Rank 1c already ran 38.49°/38.69° (±0.10°, both FAIL,
same-sign, non-load-bearing negative — filed, reused not rebuilt).

**New angles: 38.09°, 38.19°, 38.29°, 38.39°** — 0.10° spacing (matching
exp-095's own step size for direct comparability), all *below* θ₀,
extending the *already-filed* 38.49°/38.69° pair down to θ₀−0.500°.
Combined evaluated span: **38.09°–38.69°, 0.60° total ≥ the R17-mandated
0.5° minimum**, and asymmetric/lower-θ-weighted (5 of 6 evaluated points,
including the 2 reused, sit below θ₀) — not the symmetric 38.09°–39.09°
window a literal ±0.5° would give. Justification for the low-θ weighting:
the one already-measured migration at a directly analogous crossing
*rank* (lower/mid crossing, established↔cpl30) shifted **down** by
0.193582° (40.265420°→40.071838°); if θ₀=38.590230° migrates the same
direction, the new node sits below 38.49°, exactly where exp-095's own
bracket never looked. (The opposite-direction analogy, the upper crossing
shifting +0.320°/+0.377°, is the reason this is stated as a *weighting*,
not a certainty — both directions stay on the table.)

Family/config: `R4` only, both legs `C40_R4`/`G40_R4` → 4 angles × 2 legs
= **8 `sim.run()` calls.**

### (iii) `netd_row()` pre-wiring — 0 new calls, house-discipline requirement

Per R16: whichever new `run.py` (covering (i)+(ii) above) computes
`delta_scene`/`frac_contrast` via `pair_metrics_full`/`cell_metrics_r4`,
its report dict for **every one of the 32 angle/leg cells** must include
`**netd_row(pm)` (the 10-key sidecar: `p_abs_w_c/g`, `dt_ss_full_K_c/g`,
`netd_classification_c/g`, `sigma_ext_cells_c/g`, `ratio_abs_ext_raw_c/g`
— `experiments/093-.../run.py:185`) **in the same commit that introduces
the report-building code**, not retrofitted. This is a design constraint
on Phase 4 implementation, stated here so Phase 2/3 can hold it as a
mandatory fix if the eventual `run.py` draft omits it — a third
disclaimer-without-persistence occurrence anywhere T28-adjacent fires
Checkpoint criterion 4 automatically (R16's standing clause); this cycle
must not be that occurrence.

### (iv) Tier-0 documentation/code-correction bundle — 0 FDTD calls

Runs *alongside* Tier 1, not gating it (exp-097's own precedent — none of
these implicates construction code (i)/(ii) depend on):

(a) **Correct Idealization 40** in exp-097's `NOTES.md`/`run.py` docstring
to the Phase-5-verified text: *"`cpl_frozen` is keyed by `family_frozen`
(sourced from `notes_line`), independent of `pt["family"]`; `cpl_ok`
alone already discriminates every currently-possible family mislabel
among R3/R4/R5, contingent on their cpl values staying pairwise distinct
— not merely safe because gated behind `family_ok`."* (b) **Same-shift
LOGBOOK note**: QUANTUM OPTICS' own exp-097 Phase-5 review independently
repeated the identical Idealization-40 mischaracterization — first
instance of an R18-class error inside a review document itself, logged
per T10 (flag, don't silently rewrite). (c) **Add `FI-G′` to Check 5**:
corrupt `native_absorb` (41, not 40), score against `R3`/`R4`/`R5`
(`R3_CONFIGS["C40_R3"]`/`R4_CONFIGS["C40_R4"]`/`R5_CONFIGS["C40_R5"]`),
zero new `Sim` constructions — closes the `y_lo`/`y_hi` fault-injection
gap FI-G (src_x-only) left open. (d) **Restate Idealizations 39/42**
naming that Check 5 has never tested any `G40_*` (padded) config, for any
family, with exp-096's original precision.

### (v) Grazing-incidence validity — SCHEDULED this cycle (EM's own call), 0 FDTD calls

MATERIALS' governance ask (exp-097, Director-adopted): schedule within
two cycles or formally deprioritize. **I schedule it now** — it is
zero-marginal-FDTD-cost (pure function evaluation of the already-committed
`dg048.edge_diffraction_c_empty_corrected` / exp-085's bit-identical-
verified `FastEval`), squarely inside EM's charter, and directly informs
whether every existing 36°–42° `delta_scene` reading this cycle produces
sits safely inside the model's own domain of validity. Deprioritizing it a
further cycle, on an item already 10–11 cycles undischarged, is the
weaker call when the check costs under a minute of wall time.

**Design.** Reuse `CFG_C40` (native cpl=20, the model's own fit geometry),
`LAM600`, `dg048._geom_derived`, `FastEval.one(θ)` (exp-085,
verified-bit-identical to the original per-call function). Sweep
θ ∈ {30°, 35°, …, 80°} (5° steps, 11 pts) ∪ {81°, 82°, …, 89°} (1° steps,
9 pts) ∪ {89.5°} = **21 evaluations**, zero `Sim()` constructions, no FDTD.

Three EM-native checks, each a closed-form desk computation:

- **GP1 (passivity bound).** `C(θ) = weber(bo,bf)` must satisfy
  `C(θ) ≥ −1` at every θ (bo ≥ 0 is a hard passivity floor for a
  source-driven, lossless field superposition — no gain anywhere in this
  construction). A violation is a numerical, not physical, defect.
- **GP2 (near-field/far-field validity parameter).** The model's
  amplitude kernel `exp(i(kr−π/4))/√r` is the stationary-phase (kr≫1)
  reduction of the exact 2D Green's function `H₀⁽¹⁾(kr)`; compute
  `kr_min(θ) = min` over all aperture-element/observation-point pairs
  (`gd["r"]`, `k=2π/λ_cells`, already-stored `FastEval` fields) at each
  swept θ. Classify VALID (kr_min ≥ 2π), MARGINAL (π ≤ kr_min < 2π),
  INVALID (kr_min < π) per the standard Hankel-asymptotic convention.
- **GP3 (reciprocity).** Direct code-read of `dg048._geom_derived`'s
  `obliquity` construction: confirm by inspection whether it is
  symmetrized in source↔observer exchange or single-sided (tied only to
  the observer-side normal). Report which, and state analytically whether
  any reciprocity defect this implies is bounded by the same `kr` regime
  GP2 already flags (i.e., whether "near-field breakdown" and
  "reciprocity breakdown" are the same failure mode or two independent
  ones) — a genuine open question, not a confident-lean row.

## 3. T1 escape-route mapping

**No new escape-route mechanism is proposed or defended this cycle.** The
underlying, already-committed T28 program serves the **angular-selectivity**
escape route: whether an aperture/edge-diffraction effect gives a shell's
ambient-scene contrast a genuine θ-dependence usable toward constraints
1–3 (as opposed to grid staircasing, R3). This cycle does not argue FOR
angular selectivity — it determines whether the FDTD instrument that would
ever certify or refute it (`delta_scene(θ)` at cpl=40, and the diffraction
model behind it) is itself trustworthy in the window and angular regime
that window's own past claims have been made in. A CLEAN outcome across
(i)+(ii) narrows "genuine node migration vs. family-wide recipe defect";
a validity boundary θ* found in (v) bounds every future claim this line
makes near grazing incidence. Checkpoint criterion 2 (T1 position) is
N/A this cycle, matching exp-095/096/097 precedent exactly.

## 4. Per-metric predicted outcomes (falsifiable, frozen before any run)

| Item | Metric | Predicted band / criterion | Confident lean? |
|---|---|---|---|
| (i) A/B/C | `delta_scene(θ)` sign, all 4 angles/null, both legs | **PASS-family-clean**: if all three nulls show a sign change *somewhere* inside their ±0.5° bracket → feature-dependent migration, matching θ₀=38.590°'s own FAIL as the outlier, not the rule. **FAIL-family-wide**: if all three nulls show NO sign change (same-sign throughout, floor-clear) → points toward a family-wide cpl=40 recipe defect, escalating status of exp-095's FAIL. Genuine physics question — no confident lean stated. |
| (i) | `floor_pass`/`ratio_k` | Every angle clears `FLOOR_FRAC=0.10` and `RATIO_LOW/HIGH=0.1/10.0` (matching every prior R4-family reading to date, zero exception on file) — confident lean: **PASS** at all 24 points. |
| (ii) | `delta_scene` sign across 38.09°–38.69° | **CONFIRM migration-down**: exactly one sign change, located below 38.49° (in {38.09,38.19,38.29,38.39}). **REFUTE-down/CONFIRM-neither**: no sign change anywhere in the full 0.60° span (same-sign throughout) → strengthens, not settles, the family-wide-defect reading from (i). No confident lean — genuine open question, symmetric to (i). |
| (iii) | `netd_row()` presence | All 32 report rows carry the 10-key sidecar in the frozen commit — confident lean: **PASS** (design constraint, not physics). |
| (iv)(a)-(d) | Doc/code diff applied | Confident lean: **CLEAN**, zero `results.json`/verdict impact (matches R18's own founding-instance precedent for non-load-bearing corrections). |
| (v) GP1 | `min(C(θ))` over 21 pts | **PASS band: ≥ −1.0−1e-6** at every θ. A reading below −1 is a hard FAIL (numerical defect in the model, not a physics finding) — confident lean: PASS. |
| (v) GP2 | `kr_min(θ)` classification | Genuinely open. **Falsifiable claim**: if `kr_min` stays VALID (≥2π) through 89.5°, every existing 36°–42° `delta_scene` reading is a-fortiori validated on this axis (that window is far from grazing). If `kr_min` drops to MARGINAL/INVALID at some θ* < 89.5°, report θ* as the model's own self-diagnosed boundary — this is the deliverable the two-cycle governance ask requires, either way. |
| (v) GP3 | Obliquity symmetry (code read) | Report which construction is used (binary, verifiable fact) and whether its reciprocity-defect scale ties to GP2's `kr` — genuinely open, not a confident lean. |

## 5. Idealizations

**Carried forward** (exp-096/097, cited by number): 1 (2D TMz, 600nm
only), 7 (no constraint-1/2/3/4 test, no T1 position this cycle), 17
(`R3`/`R4`/`R5` share one mechanical recipe — a family-wide defect in that
shared recipe, if it exists, is not distinguishable from independent
per-family bugs by (i)/(ii) alone), 38/39/42 (as restated, item iv-d).

**New this cycle:**

46. Items (i)/(ii)'s 4-point-per-bracket quartile design localizes a sign
    change to within ~0.33° of its true location if one exists inside the
    tested span — it does not certify the ABSENCE of a crossing outside
    that span (θ₀±0.5° for (i); 38.09°–38.69° for (ii)).
47. The reused-not-rebuilt 38.49°/38.69° points (item ii) were run under
    exp-095's own construction code, byte-identical to this cycle's per
    exp-096/097's registration-readback gate — but were not re-verified
    against the extended (Check-5/6/7) gate specifically; a full re-run
    is not proposed since re-verifying construction parameters on
    already-filed data is exactly what the gate is designed to do without
    new FDTD spend, and is included as a zero-cost step in item (ii).
48. GP2's `kr` classification thresholds (2π/π) are a standard Hankel-
    asymptotic convention, not a value this program has independently
    derived or calibrated against its own FDTD data — a genuinely new
    instrument, flagged, not yet cross-validated the way `box_dev`/`xi_ext`
    were.
49. The grazing-incidence pass (v) evaluates the CLOSED-FORM diffraction
    MODEL's own internal consistency — it is not a new FDTD measurement
    and cannot, by itself, tell apart "the model is invalid near grazing"
    from "the model is valid but the physical mechanism it represents
    genuinely vanishes near grazing." Distinguishing those needs a future
    FDTD point near θ*, out of scope this cycle.
50. Item (i)'s reused ±0.5° half-width is a direct reapplication of
    exp-096's own desk bound, not a fresh R17 derivation for these three
    specific nulls — defensible because the transition class (cpl20→cpl40)
    is identical, disclosed explicitly so a future audit does not read
    this as an independently-rederived figure.

**Carried idealizations banner: every prediction in §4 is governed by
Idealizations 1/7/17/38/39/42 plus this cycle's own 46–50.**

## 6. Total estimated FDTD-call budget

- Item (i): 24 `sim.run()` calls.
- Item (ii): 8 `sim.run()` calls.
- Items (iii)/(iv)/(v): 0 FDTD calls (wiring, documentation, closed-form
  desk computation respectively).

**Total: 32 `sim.run()` calls**, plus ~32+ zero-FDTD `Sim()`-stopped-
before-`run()` constructions for registration-gate re-verification on the
new angle points (Checks 1–7, no marginal FDTD cost) and 21 zero-FDTD
function evaluations for item (v). Matches the low end of the Reconciled
Iteration-75 queue's own "~24" + "~8–16" bands (24+8=32, at the
reuse-favoring low end of the second range, justified by not re-running
exp-095's already-filed 38.49°/38.69° points). Wall-time estimate,
scaling from exp-095's own 20-call/22.47-min pace: **≈35 minutes** for the
32 real FDTD calls; item (v) adds under 5 seconds.
