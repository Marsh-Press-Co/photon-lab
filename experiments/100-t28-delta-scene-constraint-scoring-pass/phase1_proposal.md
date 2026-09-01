# Panel Iteration 77 — Phase 1 Proposal (QUANTUM OPTICS, rotation lead)

## 1. Mechanism/change narrative (≤300 words)

No new escape-route mechanism is proposed. This executes exp-099's own
Reconciled Iteration-77 Tier 1 + Tier 2 queue in one build: the trigger
seven consecutive T1:N/A cycles (Iterations 70–76) name explicitly, and
Red Team's own Phase-5 reconciliation ruled QUANTUM's dissent (that the
partition must run first) gates the scoring-pass trigger structurally.

Three zero-FDTD Tier-1 preconditions run first, deciding whether
`delta_scene(θ)` — the T28 sub-thread's own ~2.9474°-period `C40`/`G40`
diffraction signal — carries genuine article-coupled content or is, per
exp-076's own lossless-vacuum proof and Iteration 59's still-unreaffirmed
rule, a pure domain/`PAD` artifact with zero realizability content: (1)
QUANTUM's own PAD-vs-article partition, correlating `delta_scene(θ)`
against `frac_p_abs(θ)`/`ratio_abs_ext_raw(θ)` — the absorbed-power
channel `PAD` is proven structurally unable to move on its own — across
every filed `C40`/`G40` cell this sub-thread has produced; (2) MATERIALS'
disposition memo, formally separating the newly-reconfirmed "`cpl` is
inert" fact from the still-open "`delta_scene` has zero realizability
content" claim; (3) a 4-point Richardson characterization at Null B,
testing whether the climbing 0.7765→0.9623 marginal-ratio sequence is
slow convergence or a stalled recipe artifact.

Tier 2 then runs `delta_scene(θ)`'s own magnitude — and, if found
non-negligible, its article-coupled residual — through three already-
pinned constraint instruments applied to this specific bench geometry for
the first time: VISION's frozen `C_thr(L)` (T2, zero FDTD, desk), a
direction-corrected `emit.observer_record` (constraint 2), and a
direction-corrected beam-behind downstream-flux strip (constraint 1) —
reusing this sub-thread's own mirrored-propagation-correction precedent
(`widths_direction_corrected`, exp-091) since this bench's source sits
opposite `lab/emit.py`'s own assumed convention. Tier 3 is explicitly
out of scope this cycle, not folded in.

## 2. Parameter table

All reuse is unmodified unless stated. λ = 600 nm only, 2D TMz
(Idealization 1). `Sim`/`add_line_source` (`lab/fdtd2d.py`),
`r{3,4}_config()`/`R{3,4}_CONFIGS` (`experiments/069-.../design_
geometry.py`, as `dg`), the registration-readback gate
(`run_checks_1234_and_7`/`check6_positional_and_cpl`,
`experiments/097-.../run.py`), `cell_metrics_r4`/`run_block_r4`/
`pair_metrics_full`/`netd_row()` (`experiments/094/093-.../run.py`),
`find_sign_change`/`richardson_style_diagnostic`/`run_r4_batch`
(`experiments/098-.../run.py`) — all imported via the house `_load()`
chain, zero `lab/` diff for Tier 1.

### Tier 1, item 1 — PAD-vs-article partition (QUANTUM) — 0 new FDTD calls

**Dataset.** Pull every filed `(θ, family)` cell this sub-thread has
produced with a `pair_metrics_full`-derived report row (`delta_scene`,
`frac_p_abs`, and, where present, `ratio_abs_ext_raw_c`/`_g`) directly
from each cycle's own `results.json`, by its own actual stored keys
(never hand-typed, per R4/R20): `experiments/{087,088,089,091,092,093,
094,095,098,099}-.../results.json`. This spans R3/R4/R5 and is
substantially larger than any single cycle's own local set — on the
order of 80+ rows; the exact count is pinned by the aggregation script
itself, not asserted here. Where an older cycle's row predates the
`_full` extension (R16's own history), only `frac_p_abs`/`ratio_k` are
available for that row without the `ratio_abs_ext_raw` breakdown —
disclosed per-row, not silently dropped.

**Partition logic.** `delta_scene(θ) = C(G,θ) − C(C,θ)` is already a
PAD-toggled quantity with the article held present in both terms (each
`C` is that config's own article-vs-its-own-empty Weber contrast, via
`amb.contrast_from_runs`). The article-toggled/PAD-held-fixed leg is,
by the identical construction, `c_cell["C"]` (or `g_cell["C"]`) alone —
but raw per-config `C` is never persisted to `results.json` (only the
derived `delta_scene`/`frac_contrast` survive), so it cannot be
recovered zero-FDTD. The reusable, already-persisted analog on the
*absorbed-power* channel is `frac_p_abs(θ) = |p_abs_w(G,θ) −
p_abs_w(C,θ)| / p_abs_w(C,θ)` (`pair_metrics`/`pair_metrics_full`,
exp-092/093): since `PAD` is proven to leave the boundary's damping-mask
construction bit-identical between `C40`/`G40` (exp-076), *any*
non-zero `frac_p_abs` can only arise from how the article's own
near-field absorption couples to the different domain/registration
geometry `PAD` creates — a genuine article×`PAD` cross-term, not a
pure-vacuum effect. Compute, across the full pooled row set: (a) Pearson
`r(delta_scene, frac_p_abs)`; (b) the same `r`, stratified by family
(R3-only, R4-only, R5-only — a real systematic should recur across all
three, per R15's own addendum discipline); (c) `Δratio_abs_ext(θ) =
ratio_abs_ext_raw_g − ratio_abs_ext_raw_c`, testing whether T9's
established flatness (<0.1%, exp-087) still holds at this larger `n`.

**Null-calibration, justified before running (R10).** The pooled rows
are an *assembled census* across ≥10 independent cycles at 3
resolutions with non-uniform, often crossing-proximity-enriched angle
selection (exp-090's own established sampling bias) — not one
continuously-swept curve. Circular-shift (R10's mandatory default for a
swept curve) has no natural operation on this set; per R10's own text, a
non-circular-shift surrogate must be justified by the data's own
dependency structure *before* running, not selected after seeing the
answer — stated here: a 20,000-trial random-permutation null (shuffle
`frac_p_abs` against `delta_scene`, unpaired, this program's own
established trial count) is the correctly-scoped test for an assembled,
non-time-ordered set.

**R9 check (dimensional commensurability, explicit).** `delta_scene` and
`c_cell["C"]`/`g_cell["C"]` are all raw `amb.weber()` outputs (the same
construction as `C_empty` elsewhere in this program) — not a
fitted-local-carrier-normalized ratio like `amp_ratio` (T16/R9's own
founding defect). `frac_p_abs` and `ratio_abs_ext_raw` are likewise raw,
un-normalized fractions. No cross-unit comparison is made anywhere in
this item; R9 does not apply here as a risk, stated for the record.

### Tier 1, item 2 — MATERIALS' disposition memo (bundled) — 0 new FDTD calls

A short, citable file (`disposition_memo.md`) formalizing the split
already drafted in exp-099's own §T1 disposition: **(1) `cpl`-is-inert**
— confirmed, `L_GEOMETRIC_M` invariant to 1e-12 across R3/R4/R5 (Gate 3,
every `R{n}` cycle since exp-094), a resolution-knob fact, closed.
**(2) `delta_scene`'s own realizability status** — an inherited, still-
open ambiguity (Iteration 59's "zero realizability content" framing,
declined reinstatement at Iteration 60: "genuine ambiguity remains
between two opposite-realizability readings") — NOT settled by (1), and
not re-tested by any `cpl`-indexed work since. States plainly: item 1's
own partition result (above) is the first work in this sub-thread's
history actually aimed at (2) rather than (1).

### Tier 1, item 3 — 4-point Richardson characterization at Null B — 0 new FDTD calls

Pull, by stored key: `shift_20_30`, `shift_30_40`,
`observed_ratio=0.7765163757372424` from
`experiments/098-.../results.json::richardson_diagnostic.B`; `shift_40_50`
(`= crossing_50 − theta_c40`) and `observed_ratio≈0.9623` from
`experiments/099-.../results.json::item_2.step3.richardson_30_40_50`, at
full stored float precision (not the 4-sig-fig prose citation).

**Procedure**, all closed-form, reusing `richardson_style_diagnostic()`
only for the two ratios already on file, adding two new checks: (a)
**raw-magnitude monotonicity** — is `|shift_40_50| < |shift_30_40| <
|shift_20_30|` strictly, at full float precision? Exp-099's own prose
flags `|shift_40_50|` and `|shift_30_40|` as "coincidentally close" at
6-decimal display — the *sign* of any residual difference, read at full
stored precision, is the single most direct test of whether the
crossing location is still moving at all between cpl=40 and cpl=50, and
costs nothing beyond a precise re-read. (b) **implied local order** —
back out an apparent convergence order from each ratio via `p_i =
ln(r_i)/ln(cpl_i/cpl_{i+1})` (the two available ratios only: `20/30/40`
and `30/40/50`); report both `p` values and whether they are stable,
climbing toward the geometric-decay boundary (`p→0`, non-convergent), or
consistent with ordinary pre-asymptotic behavior at `n=2` ratios (too
few points to fit an asymptotic order at all). *(Illustrative hand-check
only, not the frozen figure: `r₁=0.7765`⇒`p₁≈0.88`; `r₂=0.9623`⇒`p₂≈0.17`
— the actual script recomputes both from the stored floats, never
retyped, per R4/R20.)*

### Tier 2 — constraint-1/2/3 scoring pass (QUANTUM, rotation lead)

**Leg A — `C_thr(L)` desk score, 0 new FDTD, mandatory both branches.**
Using item 1's full pooled `delta_scene(θ)` table (already on file,
36°–43° window only — no claim beyond this tested span), compute
`|delta_scene(θ)|` against VISION's frozen T2 formula, `C_thr(L) =
0.005·max[1,(L/3)^−p]`, `p∈{0.4,0.5}`, at: the photopic lab/field bars
(0.005/0.02) for Tier A, and the pinned witness-scenario scotopic
anchors (`L*≈5×10⁻⁶`–`4×10⁻⁵` cd/m², moonless-rural `≈1.7×10⁻⁴`) for
Tier W — reusing T2's own committed table verbatim, never re-derived.
**Explicit T16/T21/T24/T27 inheritance**: this channel's own documented
instrument-floor uncertainty (T16's combined domain+quadrature swing,
up to `7.80×10⁻⁴`; T21/T24/T27's edge-fringe/boundary/settling
systematics, `0.002–0.007` absolute pre-fix) is comparable in scale to
`delta_scene` itself — any PASS/FAIL verdict here is reported bounded by
that instrument floor, not as a clean physical reading.

**Leg B — direct FDTD legs, constraints 1 and 2, 16 new calls,
low-marginal-cost, priced explicitly.** No zero-cost route exists:
`observer_record`/beam-behind have never been computed on this bench at
all, and raw field captures are never persisted across process
boundaries (exp-095's own disclosure iv) — reusing a filed cell cannot
recover them. Per R8 ("an unverified independence argument is not
sufficient when an affordable named check exists"), this is priced and
run now rather than argued away. **Angles: the four already-established
cpl=20 crossings — 37.127246°, 38.590230°, 40.265420°, 41.460901°**
(`experiments/090-.../results.json::q8.crossings_deg`) — no new angle
invented (R17 N/A: this is not a bracket-sizing exercise). **Family:
`R4` only** (`C40_R4`/`G40_R4`, this sub-thread's most-exercised,
R18-gated family) — 4 angles × 2 keys × 2 conditions = **16
`sim.run()` calls**, registration-gate-clean (Checks 1–7) required
before each, zero marginal cost. These 16 calls also refresh
`delta_scene` at points literally never sampled before (every prior
`R4` reading bracketed *around* these θ₀, never *at* them) — a genuine,
not merely instrumental, new datum.

From the *same* captures (`sc.full_capture`, already needed for
`cell_metrics_r4`), extract, zero marginal `sim.run()` cost: **(i)
`beam_behind_t28`** — a downstream-flux window (`sections.flux_profile_x`,
sign-negated to match this bench's −x propagation, mirroring
`ambient.observer_profile`'s own established convention) at a plane
`~10` cells past the object's outer radius, scene/empty ratio,
matching exp-001's own beam-behind idiom exactly. **(ii)
`observer_record_t28`** — a new, mirrored wrapper around
`emit.observer_record`: physically flip the captured Ez/Hy arrays
along `x` (`a[::-1,:]`, `plane_x_mirrored = nx−1−plane_x`) before
calling `observer_record` unmodified, since this bench's source sits at
high-`x` propagating −x, the mirror image of `lab/emit.py`'s own
assumed low-`x`/+x convention — the identical mirrored-geometry
correction this sub-thread already made for `sections.widths()`
(`widths_direction_corrected`, exp-091), now extended to the observer
camera. **Mandatory validation gate (R18: a check joining new territory
needs its own control the same cycle)**: on the *empty*-scene captures
already collected in this same 16-call spend, `observer_record_t28`
must read near the established camera-floor scale (stage-6's own
"empty ≈ 0" gate) before any *article*-loaded reading from these same
16 calls is trusted — zero extra calls, since the empty legs are
already spent.

## 3. T1 escape-route disposition

**No new mechanism proposed.** This is the first cycle in seven to
actually touch constraint-1/2/3/4 scoring on `delta_scene(θ)` — the
signal that would, if article-coupled, be evidence toward the
**angular-selectivity** escape route. **Genuinely gated, not merely
plausible, but only a partial verdict is reachable this cycle**: Tier 1
determines whether `delta_scene` has *any* material analog at all
(zero FDTD); Tier 2 Leg A fully scores the signal's own magnitude
against `C_thr(L)` (zero FDTD, complete both tiers); Tier 2 Leg B gives
a first, necessarily narrow (4 angles, one resolution family, one
wavelength) direct measurement of constraints 1/2 *at exactly the
points this feature has been characterized*, not a general survey. If
Leg A shows `|delta_scene|` stays well under `C_thr` everywhere on file
(my own weak lean, below) — that alone does not certify Tier A/Tier W;
it only says this particular ripple is too small to be a constraint-3
*violation* on its own. Whether it is large enough to matter for
constraint 1 (beam termination) cannot be answered by Leg A at all — a
Weber-contrast-scale ripple and a beam-extinction fraction are
different physical quantities; that comparison is exactly what Leg B
measures, and only at 4 points. **Checkpoint criterion 2 remains N/A**:
even a clean Leg-A+B result at 4 angles is not a proven mechanism-class
boundary.

## 4. Predictions (falsifiable, frozen before any run)

| Item | Metric | Predicted band | Confident lean? |
|---|---|---|---|
| T1-1 | `r(delta_scene, frac_p_abs)`, pooled, permutation `p` | Genuinely open. **Weak lean toward small/non-significant** `r` (majority-PAD), given exp-076's lossless-vacuum proof and T9's established `ratio_abs_ext` flatness (<0.1%, exp-087) — but this exact pairing has never been tested; not a confident lean. |
| T1-1 | `Δratio_abs_ext(θ)`, pooled | Weak lean: stays <0.5% at every row, extending exp-087's own flatness finding to a much larger `n` — a confirmatory, low-stakes check. |
| T1-1 | Family-stratified `r` (R3/R4/R5) | No confident lean — if a real cross-term exists it should recur across families (R15 discipline); if the pooled `r` is driven by one family alone, that itself falsifies "genuine article coupling" in favor of a family-specific recipe artifact. |
| T1-3 | Raw-magnitude monotonicity (`|shift_40_50|` vs `|shift_30_40|`) | Genuinely open, explicitly undecidable at the display precision already on file — the entire point of pulling full float precision. No confident lean. |
| T1-3 | Implied order `p₁`,`p₂` | No confident lean on the values; weak lean that `p₂ < p₁` (deceleration continues), matching the ratio's own climb toward 1. |
| T2-A | `max|delta_scene(θ)|` (36°–43° window, full pooled table) vs `C_thr_lab=0.005` | **Weak-to-moderate lean: stays below 0.005 at every tested angle** — the single largest filed value I can cite directly (exp-099, θ=42.960901°, `+2.778×10⁻³`) sits at ≈56% of the lab bar; a genuinely larger peak elsewhere on file would falsify this. |
| T2-A | Tier-W (scotopic) comparison | If Tier-A already PASSes, Tier-W (looser `C_thr` at low `L`) PASSes a fortiori — confident lean: **PASS**, contingent on the T2-A row above. |
| T2-B | `beam_behind_t28` ratio at the 4 nulls, scene/empty | No confident lean on the exact ratio; strong lean that it stays close to the already-ESTABLISHED `graded_black_shell` figure (1.5–1.8%, LOGBOOK ESTABLISHED section) at all 4 angles — `delta_scene`'s own ~10⁻³-scale ripple is a small perturbation on an already-opaque object, not a distinct channel capable of moving this ratio by orders of magnitude. |
| T2-B | `observer_record_t28`, empty-scene validation gate | Confident lean: **PASS** (reads near the established camera floor) — if this fails, Leg B's article-loaded readings this cycle are UNINTERPRETABLE-PENDING-VALIDATION, not silently trusted. |
| T2-B | `observer_record_t28`, article-loaded, backscatter vs camera floor | No confident lean — the genuinely new measurement this cycle exists to make. |
| T2-B | Registration-readback gate, all 16 new (family,θ,key) points | Confident lean: **CLEAN** (zero exception across R4 to date). |

## 5. Idealizations

**Carried forward** (exp-096–099, cited by number, unchanged): 1 (2D
TMz, 600 nm only), 17 (R3/R4/R5 share one mechanical recipe — T1-1's own
family-stratified check exists because of this), 38/39/42 (the
registration gate's Check 5 has never tested a `G40_*` padded config —
applies directly to the 8 new `G40_R4` calls in Tier 2 Leg B), 49 (any
Richardson-style figure, T1-3 included, is descriptive only — no
continuum reference value exists).

**New this cycle:**

62. Tier 1's partition uses `frac_p_abs`/`ratio_abs_ext_raw` as the
    *only* already-persisted proxy for "article-toggled, PAD-held-fixed"
    content — the raw per-config `C` values that would give a literal,
    unconfounded version of that leg are provably unrecoverable
    zero-FDTD (never persisted). A found correlation is evidence of
    coupling; its absence does not certify zero coupling on every
    channel, only on this one.
63. `frac_p_abs` and `delta_scene` are computed from the *same* four
    FDTD calls at every row — any correlation found is not two
    independent instruments agreeing; it must be read against the
    possibility that both simply inherit shared variance from the one
    underlying `σ_ext(G,θ)−σ_ext(C,θ)` config differential (R14's own
    established mechanism) rather than reflecting new, independently
    confirmed physics.
64. Tier 2 Leg A's scored table is scoped to the 36°–43° window only —
    the T28 founding `delta_empty` fringe is known to reach far larger
    amplitude near grazing incidence (50°–90°, exp-086); nothing here
    tests whether `delta_scene` (with article) does the same, since the
    with-article census has never been extended past ~43°.
65. `observer_record_t28`'s mirror construction assumes the domain's
    two `x`-boundary absorbing bands are symmetric (both `ABSORB=40`
    for the `R4` family here) — true for `C40_R4`/`G40_R4` by
    construction, but a caller reusing this wrapper on an
    asymmetric-boundary config must re-verify it.
66. A clean Leg-A PASS (`|delta_scene|<C_thr` everywhere on file) is a
    statement about *this specific, already-measured* angle set; it is
    not a survey and does not certify the signal stays sub-threshold at
    unsampled angles inside or outside the tested window.

**Carried idealizations banner: every prediction in §4 is governed by
Idealizations 1/17/38/39/42/49/62–66.**

## 6. FDTD-call budget, self-checked

- Tier 1 (items 1–3): **0 `sim.run()` calls** — all desk/JSON
  aggregation, reusing already-committed functions and files.
- Tier 2 Leg A: **0 `sim.run()` calls** — desk score of the already-
  pooled `delta_scene` table.
- Tier 2 Leg B: 4 angles × 2 keys (`C40_R4`,`G40_R4`) × 2 conditions
  (empty/article) = **16 `sim.run()` calls.**
- **Grand total: 16 real FDTD calls** (all in Tier 2 Leg B), plus 16
  zero-cost registration-readback preflight checks (4 angles × 2 keys +
  4 angles × 2 keys for the `_1234_7`/Check-6 pair — priced exactly by
  the executing script, not asserted here) and one empty-scene
  `observer_record_t28` validation pass (0 marginal calls, reuses the
  8 empty-leg captures already inside the 16).

## 7. Confidence and open questions for Phase 2

**This design is genuinely gated, not merely plausible — but only for a
partial verdict.** Tier 1's zero-FDTD partition and Tier 2 Leg A's
zero-FDTD `C_thr(L)` score are fully executable and decisive within
their own scope this cycle; Tier 2 Leg B's 16-call spend gives this
sub-thread's first-ever direct constraint-1/2 reading on this bench,
but at only 4 angles, one family, one wavelength — explicitly a first
point, not a closure. I could not resolve alone: (1) whether 16 calls
at exactly the four cpl=20 crossings is the right angle set for Leg B,
or whether Red Team judges a wider/denser set necessary before any
constraint-1/2 reading is trusted, given `delta_scene`'s own oscillation
period (2.9474°) is wider than the spacing between some of these four
θ₀ values; (2) whether the mirrored-array construction for
`observer_record_t28` is the correct fix or whether a more direct
re-derivation of `lab/emit.py`'s own internal sign convention (as EM did
for `sections.widths()`'s own analogous defect) is required instead of
mirroring; (3) whether Tier 1's chosen proxy (`frac_p_abs` vs. the
un-recoverable raw per-config `C`) is an acceptable substitute for the
literal partition the queue names, or whether Red Team judges this close
enough to Idealization 62's own disclosed gap to require a small, fresh
FDTD leg computing per-config `C` directly instead.
