# exp-094 — T28 cpl=40 Resolution Check, sigma_max Comparability Close, R3 Census

*Panel Iteration 71. Lead seat (rotation): QUANTUM OPTICS. Phase 1 proposal
only — no `run.py`, no FDTD calls executed by this document. Executes the
Reconciled Iteration-71 queue (Red Team's Phase-5 final audit, exp-093,
LOGBOOK.md Iteration 70) as one combined, ordered build, matching this
sub-thread's own established pattern (exp-091/092/093 each combined a
reconciled queue into a single Phase-1 proposal).*

## Standing-rule compliance header (checked against R1–R15; Red Team will
## check this line by line)

- **R1–R2, R5, R7, R10** — not engaged: this cycle fits no carrier/phase
  parameter, searches no named-constant space, prices no un-fit design, and
  claims no mechanism (T1 route N/A throughout, see below).
- **R3** (resolution-check meta-rule) — this entire proposal exists to
  extend R3 checks; complied with directly, not merely avoided.
- **R4/R9** (recompute-don't-hand-type; commensurability) — every existing
  figure cited below (the n=7 dataset's `ratio_k` values, the 41.6°
  native-sigma `delta_scene`/`ratio_k`, `SIGMA_R3_CORRECTED`) was retrieved
  by directly reading the committed `run.py`/`results.json` source this
  session, not hand-typed from memory or from a prior prose citation.
- **R6/R8** — not engaged: no carrier-conditioned coefficient fit, no
  unverified robustness argument stands in for a check anywhere in this
  design (the one generalization this proposal makes — `SIGMA_CORRECTED
  (RATIO) = SIGMA_NATIVE/RATIO` at a new `RATIO=2.0` — is required to be
  independently asserted bit-exact at Phase 4, mirroring the existing
  `assert abs(SIGMA_R3_CORRECTED - 1/3) < 1e-12` precedent, not merely
  argued).
- **R11** — not engaged: no `free_period_with_widening`/staged-widening
  search is run.
- **R12** — not engaged: this bench's FDTD is deterministic (no seeds); no
  tail-statistic-across-seeds claim is made.
- **R13** (denominator floor gate) — applied unchanged: `floor_pass` is
  computed via the existing, unmodified `compute_floor()`/`FLOOR` for every
  new angle at every new resolution, exactly as every T28 cycle since
  exp-087 has done. A point failing it (as 41.8°/42.0° did at native cpl=30)
  is reported `NODE-UNRESOLVABLE`, never silently scored.
- **R14** (numerator subtractive-cancellation caution) — `frac_p_abs` is
  reported informationally only, never PRIMARY, consistent with its
  standing treatment since exp-088.
- **R15** (the rule this whole cycle exists to advance) — this proposal
  executes real, named steps on BOTH of R15's still-open discharge
  conditions per exp-093's own `r15_disclaimer` (three missing `cpl=30`
  census points; no `cpl=40` comparator anywhere on this channel) —
  **but is explicit that neither condition is fully closed by this cycle
  alone**: the census (Rank 3) covers only the three named angles, and the
  `cpl=40` check (Rank 1) is localized to the interior near-null
  (41.75°–41.90°), not a channel-wide resolution sweep. See Idealizations.

## 1. Mechanism/instrument narrative (≤300 words)

This is pure instrument recalibration — no phenomenon-mechanism claim, no
new material law. Three independent gaps left open by exp-093 (Iteration
70) are closed in one combined build, in cheapest-and-independent-first
order (no item gates another's parameter choice, so sequencing is by cost,
not by dependency — a genuine departure from exp-092/093's own gated
5→3→1→2→4 pattern, justified below).

**Rank 2 topic (run first, 4 calls):** exp-093's item 3 found `delta_scene`
at 41.8°/42.0° moves 4.71×/sign-flips under the τ_center-preserving
`sigma_max` correction (native 0.5 → corrected 1/3). The interior sweep
(41.75°–41.90°) that produced the SINGLE-NULL verdict therefore ran at
corrected sigma, while the flanking anchor at 41.6° has only ever been
measured at native sigma (exp-091's own Leg-4 bracket). This item measures
41.6° at corrected sigma, completing a sigma-consistent curve across the
*entire* 41.6°–42.0° window for the first time.

**Rank 3 topic (run second, 12 calls):** three of exp-090's original
n=7 caution-zone points — 36.0°, 38.4°, 38.8° — have never been measured
at `cpl=30`, the single most-repeated open item on the whole T28 board.
This item measures them, at native sigma (matching the original dataset's
own basis), extending the `cpl=30`-only n=8 table (exp-093 item 2) toward
n=11.

**Rank 1 topic (run third, 32 calls, most expensive, self-gated):** builds
a new `cpl=40` congruent-geometry family (`R4`, mechanically analogous to
the existing `R3` family) and re-sweeps the same six interior near-null
points exp-093 swept at `cpl=30`, at the analogous τ_center-preserving
corrected sigma, to make the SINGLE-NULL verdict cross-resolution-verified
per R15, exactly as exp-093's own Idealization 16 named.

**Rank-3 extension (desk-only, 0 calls, run last):** grows the `cpl=30`-only
caution zone with Rank 3's new points, gated on which clear R13's floor.

## 2. Parameter table

All geometry/functions reused verbatim except the new `R4` family (§2.3),
which is a mechanical, zero-design-freedom substitution of `R4_RATIO=2.0`
for `R3_RATIO=1.5` into the *already-committed* `r3_config()`/derived-
constant recipe (`experiments/069-.../design_geometry.py`,
`experiments/091-.../run.py`) — additive only, zero `lab/` diff, zero
existing-file diff beyond appending the new `R4_*` block the same way
exp-091 additively appended `G40_R3` to `R3_CONFIGS`.

### 2.1 Execution order and call budget

| Order | Queue rank | Item | Configs | Angles | `cpl` | `STEPS` | `sigma_max` | Calls |
|---|---|---|---|---|---|---|---|---|
| 1st | **Rank 2** | sigma@41.6° | `C40_R3`,`G40_R3` | 41.6° | 30 | 4200 | 1/3 (corrected) | **4** |
| 2nd | **Rank 3** | census R3-verify | `C40_R3`,`G40_R3` | 36.0°, 38.4°, 38.8° | 30 | 4200 | 0.5 (native) | **12** |
| 3rd | **Rank 1a** | `cpl=40` settling gate | `C40_R4`,`G40_R4` | 41.825° | 40 | 5600 vs 8400 | 0.25 (corrected) | **8** |
| 3rd | **Rank 1b** | `cpl=40` interior sweep | `C40_R4`,`G40_R4` | 41.750,41.775,41.825,41.850,41.875,41.900 | 40 | 5600 | 0.25 (corrected, gated on 1a) | **24** |
| 4th | **Rank 3-ext** | caution-zone growth, `cpl=30`-only | desk only | — | — | — | — | **0** |
| **Total** | | | | | | | | **48** |

**Why cheapest/independent-first, not a gated chain (departure from
exp-092/93's own 5→3→1→2→4 pattern, stated explicitly):** unlike exp-093's
own item 3→1 relationship (item 3's verdict literally selected item 1's
`sigma_max`), none of this cycle's three FDTD items sets a parameter for
either of the others — Rank 2 tests one flanking anchor at an angle already
known (native-sigma) to sit well clear of the interior null; Rank 3 tests
three angles entirely outside the 41.6°–42.0° window; Rank 1 is
self-contained (its own settling precondition gates only its own interior
sweep). With no cross-item gate, the house convention (stated explicitly in
the task brief and consistent with Red Team's own repeated "cheapest first"
sequencing rationale, e.g. exp-092's Rank-3-before-Rank-1 ordering) is
cheapest-and-independent items first, most expensive and internally-gated
item last.

**Estimated cost** (model: `experiments/065-.../design_geometry.py::
CPU_S_PER_CALL`/`_cost()`, base costs C40=25.0s, G40=34.8s at
STEPS=1400/native cpl=20; cell_ratio scales as `RATIO²`): Rank 2 ≈13.5
CPU-min; Rank 3 ≈40.4 CPU-min; Rank 1 (`RATIO=2.0` ⇒ cell_ratio=4.0,
STEPS_ratio=2.0/4.0 for the settling stress leg) ≈271.1 CPU-min (79.7
settling + 191.4 sweep). **Total ≈325 CPU-min**, wall ≈80–100 min at 4
workers (model estimate only — every prior T28 cycle's actual wall time has
landed well under its own model estimate, e.g. exp-093's 29.4 min actual
vs. 55–166 min estimated; this is the most expensive single T28 cycle to
date by CPU-min, driven entirely by `cpl=40`'s 16× native per-call cost,
justified by Rank 1's own near-unanimous #1 ranking).

### 2.2 Reused verbatim, unmodified (zero `lab/` diff, zero existing-file diff)

Via the house `_load()` module-chain (`experiments/094` loads
`experiments/093`'s `run.py`, which already loads 092→091→090): `dg`
(=`design_geometry.py`), `PAIR_KEYS_R3`, `STEPS_R3=4200`,
`SIGMA_NATIVE=0.5`, `SIGMA_R3_CORRECTED=1/3`, `box_for_r3`, `ref_for_r3`,
`build_article_r3`, `build_article_r3_sigma`, `_run_sim_r3`,
`_run_sim_r3_sigma`, `one_call`, `run_block`, `cell_metrics`,
`cell_metrics_full`, `pair_metrics`, `pair_metrics_full`, `netd_row`,
`widths_direction_corrected`, `_label`, `compute_floor`, `_profile`,
`contrast_pair`, `ratio_sign_verdict`, `classification_word`,
`find_zero_crossings`, `firth_logistic`, `naive_mle_diverges`, `auc`,
`compute_zone`, `PEC_R_R3=45`, `R3_R_OUT_CELLS=117`,
`BOX_CLEARANCE_A_R3=18`, `BOX_CLEARANCE_B_R3=36`, `REF_HALF_H_R3=120`,
`DENSE_ANGLES`, `A_HALF_APERTURE=752`, `RATIO_LOW`, `RATIO_HIGH=10.0`,
`XI_TOL`, `NOISE_MULT=3.0`, `FLOOR`, `FLOOR_FRAC=0.10`, `NETD_BAND_K`. Note
`pair_metrics`/`pair_metrics_full`/`compute_zone`/`ratio_sign_verdict` are
already resolution-agnostic (parametrized by cell dicts / a `floor` value,
never by `cpl` directly) and need **zero** modification to work on `R4`
cells — only the Sim-construction layer is resolution-specific.

### 2.3 New this cycle (all additive, mechanically forced, zero design freedom)

**New geometry constants** (append to `experiments/069-.../design_geometry.py`,
same file/pattern exp-091 already additively extended with `G40_R3`;
formula is `r3_config()`'s own recipe with `R4_RATIO` substituted for
`R3_RATIO`, every constant independently checked below against the
physical-length-invariance identity that already gates `R3`):

| Constant | Formula | Value |
|---|---|---|
| `R4_RATIO` | `40/20` | `2.0` |
| `R4_CPL` | `{600: 40}` | — |
| `R4_BASE_NX` | `round(360*R4_RATIO)` | `720` |
| `R4_BASE_NY` | `round(1584*R4_RATIO)` | `3168` |
| `R4_BASE_ABSORB` | `round(40*R4_RATIO)` | `80` |
| `R4_BASE_SRC_X` | `round(300*R4_RATIO)` | `600` |
| `R4_BASE_PLANE_X` | `round(77*R4_RATIO)` | `154` |
| `R4_BASE_OBJ_X` | `round(170*R4_RATIO)` | `340` |
| `R4_TAPER` | `round(TAPER*R4_RATIO)` | `80` |
| `R4_R_OUT` | `round(R_OUT*R4_RATIO)` | `156` |
| `R4_W_OBJ` | `round(W_OBJ*R4_RATIO)` | `156` |
| `R4_GUARD_OUT` | `round(GUARD_OUT*R4_RATIO)` | `370` |
| `R4_W_FLANK` | `round(W_FLANK*R4_RATIO)` | `156` |
| `R4_STEPS` | `round(STEPS_SETTLED*R4_RATIO)` | `5600` |
| `R4_STEPS_STRESS` | `round(R4_STEPS*1.5)` | `8400` |
| `PEC_R_R4` | `round(PEC_R_NATIVE*R4_RATIO)` | `60` |
| `BOX_CLEARANCE_A_R4` | `round(12*R4_RATIO)` | `24` |
| `BOX_CLEARANCE_B_R4` | `round(24*R4_RATIO)` | `48` |
| `REF_HALF_H_R4` | `round(80*R4_RATIO)` | `160` |
| `SIGMA_R4_CORRECTED` | `SIGMA_NATIVE/R4_RATIO` (generalizes `SIGMA_R3_CORRECTED=SIGMA_NATIVE/R3_RATIO`, independently confirmed `78.0/(2·117)=0.5/1.5=1/3` exactly) | `0.25` |
| `DX_M_R4` | `600e-9/40` | `1.5e-8` m |
| `L_GEOMETRIC_M_R4` | `R4_R_OUT*DX_M_R4` | `2.34e-6` m (must equal `L_GEOMETRIC_M`/`L_GEOMETRIC_M_R3` exactly — the physical-length-invariance identity gate, §2.4) |

`R4_CONFIGS = {"C40_R4": r4_config(80, 0), "G40_R4": r4_config(80, 80)}`
(only the two `PAIR_PAD` configs are needed — `C80_R4` is out of scope,
matching `PAIR_KEYS_R3`'s own C40/G40-only scope). Independently verified
by hand here: both configs give `A = obj_y - y_lo = 1504 = round(752·2.0)`,
the same congruent-construction identity `R3_CONFIGS` already asserts.

**New functions** (thin, mechanical mirrors of the existing R3 layer — no
new formula, no new physics):
- `box_for_r4(cfg, clearance)` — mirrors `box_for_r3`, substituting
  `R4_R_OUT_CELLS` for `R3_R_OUT_CELLS`. Needed because `box_for_r3` is
  hardcoded to the R3 constant.
- `ref_for_r4(cfg)` — mirrors `ref_for_r3`, substituting `REF_HALF_H_R4`.
- `build_article_r4_sigma(sim, cx, cy, sigma_max)` — mirrors
  `build_article_r3_sigma`, substituting `PEC_R_R4`/`R4_R_OUT_CELLS`.
- `_run_sim_r4_sigma(cfg, theta, steps, with_article, sigma_max)` — mirrors
  `_run_sim_r3_sigma`, substituting `dg.R4_CPL[600]` and
  `build_article_r4_sigma`.
- `one_call_r4(args)` — module-level picklable worker mirroring `one_call`.
- `cell_metrics_r4(key, th, steps, cap_empty, cap_article)` — mirrors
  `cell_metrics` line-for-line, substituting `dg.R4_CONFIGS`, `box_for_r4`,
  `ref_for_r4`, `BOX_CLEARANCE_A/B_R4`, `DX_M_R4`, `L_GEOMETRIC_M_R4`. This
  is the one genuinely necessary new function — `cell_metrics` itself is
  hardcoded to `dg.R3_CONFIGS`/`box_for_r3`, so it cannot be called on `R4`
  cells without a parallel. `pair_metrics`/`pair_metrics_full` are called
  on `cell_metrics_r4`'s own output **unmodified** — they only consume cell
  dicts, never a resolution constant directly.
- `compute_zone_ext(rows_subset)` — **not new**: this is exp-093's own
  `compute_zone()`, called verbatim on an extended `rows_subset` (no new
  function needed for the Rank-3 extension beyond re-invoking the existing
  one on a longer list).

### 2.4 Mandatory new-suite gates (PANEL.md's own "new machinery ⇒ new
suite stage with ≥1 absolute identity gate" requirement, for Phase 4)

1. Vacuum-footprint precondition (P1, existing idiom, unmodified) applied to
   `R4_CONFIGS` in addition to `R3_CONFIGS`.
2. `assert R4_CONFIGS["C40_R4"]["A"] == R4_CONFIGS["G40_R4"]["A"] ==
   round(A_HALF_APERTURE*R4_RATIO) == 1504` — mirrors the existing
   `R3_CONFIGS` congruent-construction assert exactly.
3. `assert abs(L_GEOMETRIC_M_R4 - L_GEOMETRIC_M) < 1e-12` — the physical
   shell radius must be bit-identical across native/`R3`/`R4`, mirroring
   the existing `L_GEOMETRIC_M_R3` assert exactly. This is the absolute
   identity gate: it fails loudly, before any FDTD call, if the mechanical
   `R4_RATIO` substitution was applied incorrectly anywhere.
4. `assert abs(SIGMA_R4_CORRECTED - 0.25) < 1e-12` — mirrors the existing
   `SIGMA_R3_CORRECTED` assert.

## 3. T1 escape-route statement

**N/A.** Independently re-verified against LOGBOOK.md's own record this
session (read in full, RULED OUT through the complete T28 thread,
Iterations 46–70): every T28 sub-thread entry since exp-069 states T1 route
N/A / Checkpoint criterion 2 N/A, most recently reconfirmed explicitly at
exp-092 ("T1 route N/A, Checkpoint criterion 2 N/A, independently
reconfirmed against the unbroken LOGBOOK record for this sub-thread since
exp-069") and carried again at exp-093. This cycle makes no
phenomenon-mechanism claim, touches no σ(I)/σ(x,t)/angular-selectivity/
sub-threshold-operation position, and does not open
`REALIZABILITY_MEMO.md`. It is pure instrument recalibration (a new
resolution family + two comparability closes), matching every T28
desk/instrument cycle's own disposition.

## 4. Falsifiable predicted outcomes

**(Rank 2, PRIMARY) sigma@41.6°.** At native sigma (already filed,
`experiments/091-.../results.json::raw.r3_leg4_cpl30_steps4200_bracket
["41.6"]`, retrieved this session, not hand-typed): `delta_scene=
+1.7838×10⁻⁴`, `frac_contrast=3.3296×10⁻⁴`, `ratio_k=25.9467`,
`floor_pass=True` — a clean, well-resolved, ENERGY-DOMINANT, **positive**
(`Y=1`) reading, unlike 41.8°/42.0° which sit inside the fragile
near-total-null itself. Scored with exp-092/093's own `[0.3,3.0]` CONFIRM /
`[0.1,10]` REFUTE bands on `{corrected}/{native}` for both `delta_scene`
(sign+ratio) and `frac_contrast` (ratio), worst-case across both
quantities, exactly as item 3 did. **Informed, not confident, lean:**
CONFIRM is more likely here than it was at 41.8°/42.0°, because 41.6° sits
well inside the curve's own positive lobe, not adjacent to a near-total
destructive-interference null — R13/R14's own established principle is
that sigma-sensitivity concentrates near small-residual/near-zero
quantities, and 41.6°'s `ratio_k=25.9` is not small. A REFUTE here would be
a genuine surprise, disclosed as such, not smoothed over. **Informational,
non-gating:** `p_abs_w` ratio expected within 2–5% of the 0.51 T9 anchor
(matching item 3b's own precedent, 0.7% deviation at both its angles).
**Informational, non-gating, reported regardless of the PRIMARY verdict:**
the fully sigma-consistent 8-point curve across 41.6°–42.0° (41.6° [new,
corrected] + 41.750°–41.900° [exp-093 item 1, corrected] + 41.8°/42.0°
[exp-093 item 3, corrected]) — does `delta_scene(41.6°)` stay positive at
corrected sigma too, i.e. does SINGLE-NULL's own "the null is a single
smooth trough, not two nodes" reading extend cleanly to a *sign change*
just outside the trough at 41.6°, on one consistent sigma basis, for the
first time?

**(Rank 3, PRIMARY) census R3-verify, three angles.** Original `cpl=20`
values (independently retrieved from `experiments/090-.../run.py`'s own
committed `dataset` list, not hand-typed): 36.0°→`ratio_k=2.6424,Y=0`
(exp-087); 38.4°→`ratio_k=0.9075,Y=0` (exp-088); 38.8°→`ratio_k=3.8733,
Y=0` (exp-088). All three sit comfortably below `RATIO_HIGH=10.0` at
`cpl=20`. Falsifiable three-way outcome per angle: **CONSISTENT**
(`floor_pass=True`, same `Y` at `cpl=30`); **FLIPPED** (`floor_pass=True`,
different `Y`); **NODE-UNRESOLVABLE** (`floor_pass=False`). **Informed,
not confident, lean:** the modal expectation is CONSISTENT (`Y=0`) at all
three, given their comfortable margin from `RATIO_HIGH` — but this program's
own record directly warns against over-trusting "comfortable" margins:
41.4° (`ratio_k=28.8`, nearly 3× further from the boundary than any of
these three) FLIPPED under the identical `cpl=30` R3 check (exp-091). Any
FLIPPED or NODE-UNRESOLVABLE reading is reported as a genuine finding, not
downweighted for contradicting the modal expectation.

**(Rank 1a, PRIMARY, gates Rank 1b) `cpl=40` settling precondition.**
CONFIRM/PASS = `|delta_scene(STEPS=8400) − delta_scene(STEPS=5600)| /
|delta_scene(STEPS=5600)| ≤ 1×10⁻²` at both `C40_R4` and `G40_R4`
(looser than this program's historical ~10⁻⁴–10⁻⁵ clean-settling bar,
disclosed as deliberately loosened because 41.825° sits inside a
near-total-null where the underlying quantity is a small residual —
R14's own subtractive-cancellation caution, applied here to a settling
check rather than a cross-config numerator). CAUTIONARY-PASS (proceed,
flag results as settling-uncertain) = `1×10⁻² < \text{rel.\ dev.} ≤
1×10⁻¹`. HALT (do not spend Rank 1b's 24 calls) = `>1×10⁻¹` at either
config — investigated before proceeding, per this program's own
`HALT`-precondition precedent (exp-076).

**(Rank 1b, PRIMARY) `cpl=40` interior three-way outcome.** Identical
categories to exp-093's own item 1: **TWO-NODE CONFIRMED** (≥1 point
`delta_scene>0` AND `floor_pass`); **SINGLE-NULL** (all six points
`delta_scene≤0`); **STILL AMBIGUOUS** (no point clears the floor gate
either direction). **Informed, not confident, lean:** SINGLE-NULL is the
modal expectation (matching `cpl=30`'s own clean result, all four
floor-clearing points ENERGY-DOMINANT with no positive excursion, and
MATERIALS' own T10 near-field/curved-boundary account for *why* resolution
moves this class of feature continuously rather than discontinuously) —
explicitly not a confident lean, since this check exists precisely because
prior resolution changes on this exact channel (41.4°'s own `cpl=20→30`
flip; item 3's own `sigma_max` sign flip at 42.0°) have gone the other way.
**Informational, non-gating:** at any `cpl=40` point landing within
±0.025° of a `cpl=30` floor-clearing point, `ratio_k` is expected to remain
same-order-of-magnitude ENERGY-DOMINANT (informally, `10×`–`60×`, a
loosened band around the `cpl=30` figures' own `20.5×–29.6×`, to allow for
genuine resolution-driven drift without over-constraining).

**(Rank 3-ext, PRIMARY, gated on Rank 3, zero-FDTD) caution-zone growth.**
Re-invoke `compute_zone()` on the existing `cpl=30`-only `n=8` table
(exp-093 item 2) plus every one of the three new Rank-3 points that clears
`floor_pass` (excluded if `NODE-UNRESOLVABLE`, matching 41.8°/42.0°'s own
exclusion convention) — `cpl=30`-only throughout, `cpl=40` data from Rank 1
deliberately NOT mixed in (preserves a single consistent resolution basis,
matching exp-093's own item-2 discipline). CONFIRM = the extended zone is
non-inverted and the live recomputation reproduces `auc`/Firth/zone figures
bit-exact on re-run. No numeric band is pre-committed for the *value* of
the extended zone itself (that would be circular — the whole point is to
measure it), but the **falsifier is explicit**: an inverted zone (any
`Y=1` margin exceeding any `Y=0` margin) is reported as a genuine
R15-relevant finding, exactly matching exp-090's own founding falsifier
clause.

## 5. Idealizations

**Carried forward from exp-093's own list, cited by original number
(unchanged in scope unless noted):** 1 (2D TMz, 600nm only), 3 (NETD ≠
human-eye threshold — N/A this cycle, no NETD backfill is run), 6
(`FLOOR` applied, not recomputed, at every new point in every item), 7
(no constraint-1/2/3/4 test, no T1 position), 8 (unbiased
margin-vs-distance rebuild on the full 31-point window remains open, not
run this cycle either), 11 (a sigma-branch verdict at one angle does not,
by itself, revalidate comparability elsewhere — extended below), 12–13 (the
Yee-dispersion desk work is unrelated to and untouched by this cycle), 15
(the `n≥8` zone table's 40.0°/40.2° treatment as independent members is
unchanged), 16 (angular-only resolution results are not automatically
R15-grade cross-resolution findings — this is the idealization Rank 1
exists to relieve, partially, for the interior near-null specifically).

**New this cycle:**

17. The `R4` (`cpl=40`) geometry family is a mechanical, zero-design-freedom
    substitution of `R4_RATIO=2.0` for `R3_RATIO=1.5` into the
    already-committed `r3_config()` recipe — not independently re-derived
    from first principles beyond the identity gates named in §2.4. If the
    `R3`-family recipe itself carries any undetected systematic bias, `R4`
    inherits it unchanged; the two families are not independent
    confirmations of the underlying re-discretization scheme, only of the
    specific feature under test at two grid densities.
18. `SIGMA_CORRECTED(RATIO) = SIGMA_NATIVE/RATIO` is empirically confirmed
    to match the already-established, algebraically-derived
    `SIGMA_R3_CORRECTED` at `RATIO=1.5` — but the *generalization* to
    `RATIO=2.0` is asserted, not independently re-derived from the
    underlying physical argument (τ_center-preservation) at Phase 1; Phase
    4's own identity gate (§2.4 item 4) checks only algebraic consistency
    of the formula, not that τ_center-preservation is still the physically
    correct criterion at this new, coarser-to-finer ratio.
19. Rank 1's `cpl=40` settling precondition is a single-angle
    (41.825°), both-config spot-check, not an exhaustive per-angle
    settling verification of all six interior points — matching this
    program's own established spot-check convention (e.g. exp-091's own
    two-angle `R3_STEPS=4200` settling check), disclosed as a spot-check.
20. Rank 1 is localized to the interior near-null band (41.75°–41.90°)
    only. It does **not** re-verify the flanking anchors, the located
    lower crossing (40.0718°), or any other point in the 36°–42° dense
    window at `cpl=40` — R15's own "no `cpl=40` comparator exists anywhere
    on this channel" discharge condition gets its first-ever data point on
    this channel, localized, not a channel-wide resolution census.
21. Rank 3's three census points are measured at native `sigma_max=0.5`
    only (matching the original `cpl=20` dataset's own basis), not
    cross-checked at corrected sigma — because item 3 (exp-093) localized
    the demonstrated sigma-sensitivity to the 41.8°/42.0° near-null
    specifically, and 36.0°/38.4°/38.8° sit far from any known or
    suspected null. If a future cycle finds sigma-sensitivity is not in
    fact localized to near-null regions, this choice should be revisited
    for these three points.
22. Rank 2's sigma-consistency close is local to 41.6°; it does not extend
    corrected-sigma coverage to 36°–41.4°, where no contamination has been
    demonstrated or suspected.

**Carried idealizations banner (mandatory, Iteration-65 CHECKPOINT's
non-discretionary rule): every prediction in §4 is governed by
Idealizations 1/3/6/7/8/11/16 plus this cycle's own 17–22.**

## 6. Realizability bound

**N/A.** This is a pure instrument/desk-recalibration cycle: no new
material, mechanism, or optical-response claim is made anywhere in this
proposal (§3). `REALIZABILITY_MEMO.md` is not opened, cited, or re-scored.
Matches every T28 desk/instrument cycle's own disposition since exp-069,
independently re-verified against LOGBOOK.md's record this session.
