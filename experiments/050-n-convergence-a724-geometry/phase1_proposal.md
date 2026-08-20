# PHASE 1 — PROPOSAL · Panel Iteration 27 · Lead seat: MATERIALS & METAMATERIALS

## "The n-Convergence Audit at the A=724 Fallback Geometry" (candidate exp-050)

*Runner: cloud panel shift · rotation: VISION→PHOTONICS→**MATERIALS**→
ELECTROMAGNETISM→THERMODYNAMICS→QUANTUM OPTICS→repeat. Protocol: PANEL.md.
Memory: LOGBOOK.md (RULED OUT R1–R4 checked — nothing here resurrects a
ruled-out idea; this cycle proposes no mechanism at all).*

**Executing a queued item, not a fresh MATERIALS mechanism proposal**, per
PANEL.md's own Iteration-20/22/23/26 precedent for instrument/model-fidelity
cycles and Red Team's Iteration-26 Phase-5 synthesis, ranked #1 and
near-unanimous across five of six reviewing seats (`phase5_redteam_audit.md`
lines 411–420): *"Re-run this identical n-doubling sweep at exp-048's
A=724/NY=1528 fallback geometry ... the geometry any actual near-boundary
constraint-3 or realizability citation would use, and it has never been
convergence-tested."* This is also, verbatim, **MATERIALS' own Phase-2
Attack-1 follow-up trigger on exp-049** (`experiments/049-.../
phase2_redteam_audit.md` Attack 1, adopted without change; exp-049's own
idealization 7): exp-049's n\* findings are scoped to exp-042/046's
A=752/NY=1584 geometry and "must not be cited as governing the A=724
fallback geometry ... without this cheap re-run" (PLAN.md, panel-Iteration-27
queue entry (1)). Instrument/model-fidelity cycle, Iteration-20/22/23/26
class. **T1 escape route: NONE.**

---

## 1. Mechanism / test narrative (≤300 words)

**This is NOT a T1 mechanism proposal.** No material law, no σ(I)/σ(x,t),
no angular-selectivity claim, no constraint-3/4 verdict.

exp-049 (Iteration 26) formally convergence-tested `gaussian_angle_weights`'s
quadrature order `n` for all three committed `beam_divergence_*` functions
(`experiments/042-t21-magnitude-bridge/design_geometry.py:279-355`) — but
**only** at exp-042/046's own hardcoded module-global geometry
(`A=752`, `NY=1584`). That geometry was never the one any live constraint-3
or realizability citation near the fallback boundary actually uses: exp-048
(Iteration 25) already established that the operative near-boundary geometry
is `GEOM78` (`NY=1528, OBJ_Y=764` ⇒ `A=724`,
`experiments/048-evidentiary-chord-closure/design_geometry.py:145-149`) and
already generalized part of exp-042's own propagator (`field_and_h`,
`edge_diffraction_c_empty_corrected`) to run at that geometry via a
geometry-dict pattern (`_geom_derived(g)`, `_src_amp(theta_deg,k,gd)`,
ibid. `:179-230`). exp-049's own idealization 7 states plainly that its
finding (global max n\*=81 across 108 cell-function combinations) "says
nothing about whether n=41 is converged at that separate geometry."

**Design: reuse exp-049's own Phase-3-corrected machinery unmodified**
(N_SERIES, the exemption-not-floor convergence criterion, the 36-cell grid,
all three function names) — the only new work is (i) generalizing the three
`beam_divergence_*` functions to take a geometry dict, following exp-048
Block B's own precedent, and (ii) a **mandatory regression anchor**: the
generalized functions, called at `GEOM_EXP042_OLD` (exp-048's own verbatim
reconstruction of exp-042's module-globals, ibid. `:154-158`), must
reproduce exp-049's own committed `results.json` `per_cell_summary` — all
108 rows, not a worst-cell-plus-counts summary (§2.2 explains why that
distinction is itself a lesson from this program's own record) — before any
`GEOM78` number is trusted.

*(229 words)*

---

## 2. Parameter tables

Every number below is either copied from a cited repo line or computed from
cited repo constants by a formula stated in full and evaluated by direct
computation this cycle (not hand-typed — see §2.3's note on this program's
own R4 rule).

### 2.0 What is reused verbatim from exp-049 (unmodified)

| Constant / function | Value | Source |
|---|---|---|
| `N_SERIES` | (41, 81, 161, 321, 641, 1281, 2561, 5121) | `experiments/049-.../run.py:34` |
| `N_REGRESSION` | 401 | ibid. `:35` |
| `C_THR`, `ABS_TOL`, `REL_TOL` | 0.005, 5×10⁻⁴, 1.0% | ibid. `:30-32` |
| Convergence criterion (**exemption, not floor** — Red Team Attack 5, exp-049 Phase 2) | `Δabs(n)=\|C(2n)−C(n)\|`; if `\|C(2n)\|≥C_THR`: also require `Δrel(n)=100·Δabs/\|C(2n)\|≤REL_TOL`; **else the relative clause is exempted** and the step passes on `Δabs≤ABS_TOL` alone | ibid. `delta_step`, `:111-121` |
| Trustworthy n\* rule | smallest N_SERIES entry where **two consecutive** doublings both converge; else NOT CONVERGED WITHIN RANGE | ibid. `find_nstar`, `:124-136` |
| The 36-cell grid | θ₀∈{36,38,40}°, FWHM∈{2,5,10,20}°, λ∈{450,600,750}nm | ibid. `:37-49`; unchanged from exp-042/046 |
| `gaussian_angle_weights(θ₀,fwhm,n,half_width_factor=2.5)` | reused **as-is, no parameterization needed** — takes no geometry argument at all | `experiments/042-.../design_geometry.py:310-318` |

**Nothing in this table is modified.** Reusing the corrected (Phase-3)
criterion, not exp-049's own original ill-conditioned Phase-1 formula, is
itself a design decision this proposal makes explicitly — the alternative
(re-deriving a criterion from scratch) would repeat work exp-049's own Phase
2/3 already did and would make this cycle's results non-comparable to
exp-049's.

### 2.1 Geometry: what changes, what doesn't — verified directly, not assumed

| Quantity | OLD (`GEOM_EXP042_OLD`, exp-042/046, regression anchor) | NEW (`GEOM78`, exp-048, this cycle's target) | Source |
|---|---|---|---|
| `NY` | 1584 | **1528** | `experiments/042-.../design_geometry.py:120`; `experiments/048-.../design_geometry.py:145-158` |
| `OBJ_Y` | 792 | **764** | ibid. |
| `ABSORB` | 40 | 40 (same) | ibid. |
| `A = OBJ_Y − ABSORB` | **752** | **724** | computed, verified: 792−40=752 ✓ (matches exp-042's own `assert A==752`, `:139`); 764−40=724 ✓ |
| `D_SP` | 223 | 223 (same) | ibid. |
| `GUARD_OUT` | **185** | **186** | `experiments/042-.../design_geometry.py:127`; `experiments/048-.../design_geometry.py:146` |
| `R_OUT`, `W_FLANK`, `PLANE_X`, `SRC_X`, `TAPER` | 78, 78, 77, 300, 40 | 78, 78, 77, 300, 40 (all same) | ibid. |
| `CPL` (λ→λ_cells) | {450:15, 600:20, 750:25} | {450:15, 600:20, 750:25} — **identical** | `experiments/042-.../design_geometry.py:129`; `experiments/048-.../design_geometry.py:160` |
| Y-domain length (`NY−2·ABSORB`) | 1504 cells | 1448 cells (**3.72% smaller**) | computed |
| `R_EDGE = √(D_SP²+A²)` | 784.368 cells | 757.565 cells | computed |

**Design decisions, stated explicitly (per the Director's brief):**

1. **`CPL` does NOT differ** between the two geometries — verified by direct
   comparison of the two files' own `CPL` dicts, not assumed. No
   wavelength-to-cells recalibration is needed anywhere in this cycle.
2. **The 36-cell (θ₀,FWHM,λ) grid transfers unchanged.** The grid is defined
   purely in degrees and nanometres; it enters the propagator only through
   `CPL` (unchanged, above) and through `A`/`NY` inside the geometry-derived
   quantities each function already recomputes per call. No grid point needs
   re-selection.
3. **`GUARD_OUT` differs by 1 cell (185→186)**, a real but tiny difference
   (0.07% of the 1504/1448-cell domain) affecting only where the flank
   (background) window starts in `amb.window_means`. Disclosed, not
   corrected to match — `GEOM78` is exp-048's own committed geometry and
   this cycle uses it verbatim, exactly as received.
4. **`A` shrinks 3.73%** (752→724) and the Y-domain shrinks 3.72% — the two
   percentages agree because both differences trace to the same `NY`
   reduction (1584→1528, a 56-cell/3.5% cut) at fixed `ABSORB`/`D_SP`/
   `OBJ_Y`-offset construction. This is the single geometric fact §2.3's
   falsifiable predictions are built on.

### 2.2 Generalizing the three `beam_divergence_*` functions — what exists, what must be built fresh

Following exp-048 Block B's own precedent (`_geom_derived(g)` builds every
derived quantity — `y_lo`, `y_hi`, `obj_y`, `a`, `r`, `obliquity`, the
tapered aperture `p` — from a geometry dict `g`;
`experiments/048-.../design_geometry.py:179-197`):

| Target function (exp-042) | Propagator convention it needs | Parameterized building block available today | Gap |
|---|---|---|---|
| `beam_divergence_incoherent_corrected` (`:279-295`) | single-obliquity-via-H (E from bare `G0`, H from `G0·obliquity`) — the **erratum/corrected** convention | **Already built**: `field_and_h(theta_deg, lam_cells, g)`, `experiments/048-.../design_geometry.py:207-219` | None — direct reuse per angle, then `amb.incoherent_sum` over the Gaussian-weighted angle set, exactly as `:279-295` already does with the module-global version |
| `beam_divergence_incoherent` (`:321-334`) | obliquity-applied-to-E-then-squared (`\|G@amp\|²`, `G=G0·obliquity`) — the **original/committed** convention (`_G_for(lam,True)`, `:197-212`) | **Not built anywhere yet** — exp-048 Block B never needed this convention (it only ever re-parameterized the corrected one) | New, but algebraically trivial from `_geom_derived`'s own output: `G = G0 * gd["obliquity"]` where `G0 = exp(i(k·gd["r"]−π/4))/√gd["r"]` |
| `beam_divergence_coherent` (`:337-355`) | same obliquity-on-E convention as above, summed coherently before `\|·\|²` | same gap as above | same fix as above |

**Flagged here so Phase 4 does not silently improvise it**: two of the three
target functions need a propagator convention (`_G_for`'s own
obliquity-on-E recipe) that has never been generalized in this program's
history — only the corrected H-based one has (exp-048). The fix is a
one-line addition to `_geom_derived`'s output (or a thin wrapper around it),
not a new physical idealization; it reuses the exact formula already
committed at `experiments/042-.../design_geometry.py:197-212`, evaluated on
`gd["r"]`/`gd["obliquity"]` instead of the module globals `_R`/`_OBLIQUITY`.
`gaussian_angle_weights` itself needs no change (§2.0) — it never touches
geometry.

### 2.3 The regression anchor — learning from exp-049's own Attack 7

exp-049's own P-NCONV26-0 regression gate (scored against exp-046's
`results.json`) was found by Red Team, uncaught by any of five blind
seats, to be **not executable as written**: it promised a 36-cell per-cell
match against data recorded only as one worst-cell figure plus two integer
counts (`experiments/049-.../phase2_redteam_audit.md`, Attack 7a), and half
of it needed a function outside the audit's own declared scope (Attack 7b).
**This cycle does not repeat that defect, for a structural reason, not
extra diligence**: exp-049's own committed `results.json` `per_cell_summary`
records `nstar`, `c41`, `c401`, and `converged_value` **for all 108
cell-function combinations** (`experiments/049-.../results.json`, verified
by direct inspection — 108 rows), a genuinely full table, unlike exp-046's
worst-cell-only record. The regression anchor below is therefore fully
executable exactly as stated.

> **Regression anchor (mandatory, checked before any GEOM78 number is
> trusted):** call the newly-parameterized `beam_divergence_incoherent`,
> `beam_divergence_incoherent_corrected`, `beam_divergence_coherent`
> functions with `g=GEOM_EXP042_OLD` (`experiments/048-.../
> design_geometry.py:154-158`) at every one of the 36 grid cells × 8
> `N_SERIES` entries + `n=401`, and confirm: (a) every `c41`/`c401` value
> matches exp-049's own committed `per_cell_summary` row to ≤10⁻⁹ relative
> (float-identical, since both are the same formula evaluated on numerically
> identical geometry — the OLD-geometry call is not an approximation, it is
> the same computation); (b) every `nstar` matches exactly (integer
> identity, not a tolerance); (c) every `converged_value` matches to the
> same ≤10⁻⁹ relative bound. **Hard failure: any single mismatch beyond
> float noise ⇒ no GEOM78 number in this cycle is trusted until resolved**
> — the same "checked first, gates everything else" role P-NCONV26-0 held,
> now actually checkable as stated.

### 2.4 Fringe period at the two geometries — computed, not assumed (§4's grounding)

LOGBOOK's own T21 fringe-period model, `P(θ)=λ_cells/(A·cosθ)`
(Iteration 18, reused by analogy for this construction since exp-049,
`experiments/049-.../phase1_proposal.md` §2.1, idealization 3), evaluated at
both geometries' own `A` (direct computation this cycle, not from a prior
results.json):

| λ (nm) | θ₀ | P(θ), A=752 (deg) | P(θ), A=724 (deg) | ratio (724/752) |
|---|---|---|---|---|
| 450 | 36° | 1.4127 | 1.4673 | |
| 450 | 38° | 1.4503 | 1.5064 | |
| 450 | 40° | 1.4919 | 1.5496 | |
| 600 | 36° | 1.8835 | 1.9564 | |
| 600 | 38° | 1.9338 | 2.0085 | |
| 600 | 40° | 1.9892 | 2.0661 | |
| 750 | 36° | 2.3544 | 2.4455 | |
| 750 | 38° | 2.4172 | 2.5107 | |
| 750 | 40° | 2.4865 | 2.5827 | |

Every one of the 9 ratios is **exactly 752/724 = 1.038674** (a pure
consequence of `P∝1/A` at fixed λ,θ — the same multiplicative factor for
every cell, not a coincidence needing per-cell verification). **The period
grows ~3.87% at GEOM78** — i.e. samples-per-period at any fixed `n` also
grows ~3.87% (since `Δθ_sample(n,fwhm)` depends only on `n`,`fwhm`, never on
`A`, `:310-318`). At n=41, FWHM=20° (the regime exp-049 found hardest):
samples/period range **0.565–0.995 at A=752** vs **0.587–1.033 at A=724**
(computed this cycle) — uniformly higher, still below or at the Nyquist
line (2 samples/period) everywhere, the same qualitative "structurally
aliased" bucket exp-049's own §2.1 table assigned this regime.

---

## 3. T1 escape-route statement

**NONE.** This cycle proposes no material law, no σ(I), no σ(x,t), no
angular selectivity, no sub-threshold operation, and no new mechanism class.
It re-runs an already-committed quadrature self-convergence audit at a
different, already-committed geometry. Per PANEL.md's Latitude rule there is
nothing exotic to bound; per the Iteration-20/22/23/26 precedent an
instrument cycle states NONE. No constraint-3/4 verdict is issued at either
tier, and no result here can move any `REALIZABILITY_MEMO.md` tier.

---

## 4. Falsifiable predicted outcomes — committed BEFORE any run

Nothing below has been computed by running `beam_divergence_*` at GEOM78 —
only the geometry arithmetic in §2.1/§2.4 (pure algebra on cited constants)
has been evaluated. "Converged value" always means the value at n\* (or the
n=5121 reading, labelled as such, for a NOT-CONVERGED-WITHIN-RANGE cell) —
same convention as exp-049.

| ID | Prediction | Committed band | Hard falsification |
|---|---|---|---|
| **P-NCONV27-0** | **Regression anchor, checked first** (§2.3). The parameterized functions at `g=GEOM_EXP042_OLD` reproduce exp-049's own `per_cell_summary` | ≤10⁻⁹ relative on every `c41`/`c401`/`converged_value`; exact integer match on every `nstar`, all 108 rows | any row mismatches beyond float noise ⇒ no new number in this audit is trusted until resolved |
| **P-NCONV27-1** | The global maximum n\* across all 108 GEOM78 cell-function combinations does not exceed exp-049's own A=752 maximum | max n\* ≤ **81** (central estimate: exactly 81, unchanged) | any combination needs n\*>81, or any combination is flagged NOT CONVERGED WITHIN RANGE |
| **P-NCONV27-2** | **No cell-function combination needs a strictly larger N_SERIES tier at GEOM78 than it needed at A=752** — grounded in §2.4: the period grows (never shrinks) at A=724, so samples-per-period at fixed n can only improve, and the ~3.87% multiplicative shift is far smaller than N_SERIES's own ~2× step granularity (tier index = position in the 8-entry N_SERIES tuple; "stricter" = larger tier index; explicit sign convention stated here to avoid exp-049's own Phase-4 rank-sign erratum, `experiments/049-.../run.py:62-88`) | 0 of 108 combinations move to a strictly larger tier; **up to 5** may move to a strictly smaller tier without falsifying (an easier-convergence direction consistent with the period argument) | any combination moves to a larger tier (contradicts the monotonic-period argument outright), or more than 15/108 combinations change tier at all (would mean the ~3.87% shift is not the small perturbation this proposal argues it is) |
| **P-NCONV27-3** | The coherent-function FWHM=20° under-convergence pattern (exp-049's P-NCONV26-1a: 8/9 cells fail n=41) reproduces at GEOM78, same direction, comparable count | **6–9 of 9** FWHM=20° coherent cells have n\*>41, central estimate 8/9 (same as A=752) | ≤2/9 fail (the mechanism does not survive the geometry change) |
| **P-NCONV27-4** | `incoherent_corrected`'s FWHM=20° residual failure count (exp-049: 5/9) reproduces in a comparable range | **3–7 of 9** FWHM=20° `incoherent_corrected` cells have n\*>41, central estimate 5/9 | 0/9 or 9/9 (either extreme contradicts the "intermediate, not dominant-or-absent" character exp-049 measured) |
| **P-NCONV27-5** | FWHM≤10° stays universally, cleanly converged at n=41 (exp-049's P-NCONV26-1c: 81/81, stronger than its own ≥70% prior) | **≥95%** of the 81 FWHM≤10° cell-function combinations converged at n=41 (central estimate 81/81, 100%, matching exp-049 exactly, since the period shift only improves oversampling in this already-comfortable regime) | <70% pooled (a materially worse finding, would mean the A=752 result does not generalize even in its best-behaved regime) |
| **P-NCONV27-6** | The GEOM78 analogue of exp-042's sharpest-stakes near-boundary cell (750nm, θ₀=38°, FWHM=2°, `incoherent_corrected` — same grid point, §2.1 point 2) stays converged at n=41, no flip. **Disclosed, inline (per exp-049's own Attack-6-driven precedent): this cell is FDTD-unvalidated here, and LOGBOOK's T24 boundary systematic (~+0.0070 at 750nm/38°/FWHM=2°) was measured at exp-046's own A=752 geometry, not GEOM78 — carried over here by analogy only, not measured at this geometry** | n\*=41 (unchanged), converged-value relative move ≤**1%** (central estimate ≈0%, matching exp-049's own ~7.7×10⁻⁹%-level finding at this cell, `experiments/049-.../phase5_redteam_audit.md:415-424`) | n\*>41 (a flip in convergence status at this program's single sharpest-stakes cell), or relative move >5% |
| **P-NCONV27-7** | The coherent-function worst-cell relative move at converged n\* stays close to exp-049's own 4.4747% figure (450nm/36°/FWHM=20°, `experiments/049-.../results.json` `P_NCONV26_8`) — the mechanism is primarily set by the aperture's own grating-lobe structure, and the aperture geometry shifts only ~3.7–3.9% (§2.1/§2.4) | worst coherent move at GEOM78 in **[3.0%, 6.5%]**, central estimate ≈4.5% | <1.5% (mechanism collapses at this geometry) or >10% (mechanism amplifies far more than the small geometric shift would suggest) |

**What would make this cycle a failure, stated plainly:** if P-NCONV27-2
falls the way its own hard-falsification band names (any cell moves to a
*larger* N_SERIES tier at the smaller-A geometry), the period-growth
argument grounding every directional claim in this proposal (§2.4) is
wrong, and the "n=41 is even safer at GEOM78" reading this cycle expects
would need re-explaining, not just re-measuring. That is a real,
pre-registered way for this proposal to lose — matching exp-049's own
"what would make this cycle a failure" convention (`phase1_proposal.md`
lines 224–230).

---

## 5. Idealizations (lab convention — stated, not buried)

1. **Scope: geometry only.** `half_width_factor=2.5`, `N_SERIES`,
   `ABS_TOL`/`REL_TOL`, and the exemption-not-floor criterion are all held
   exactly as exp-049's own Phase-3-corrected design fixed them (§2.0) — no
   further tuning of the convergence machinery itself is in scope this
   cycle.
2. **The convergence criterion remains a disclosed modelling choice**,
   inherited from exp-049 (already corrected once at that cycle's own
   Phase 3), not re-litigated here.
3. **The T21 fringe-period model is reused by analogy, twice-compounded.**
   First compounding (inherited from exp-049, idealization 3): the model
   was derived for `edge_diffraction_c_empty`, a single-angle sweep, not
   `beam_divergence_*`'s own integrated quantity. **Second compounding, new
   this cycle:** the model's own magnitude-level validation (exp-042,
   Iteration 19) was performed only at A=752; its accuracy at A=724 has
   never been separately checked — §2.4/§4's predictions use it only as a
   *directional* argument (period grows, monotonically, by a single
   geometry-independent multiplicative factor), never as a magnitude claim
   at the new geometry.
4. **`GUARD_OUT` differs by 1 cell (185→186) between the two geometries**
   (§2.1 point 3) — used verbatim from `GEOM78` as committed by exp-048, not
   adjusted to match the OLD geometry's own value. A negligible (<0.1%)
   effect on the flank-window baseline, disclosed rather than silently
   absorbed into "the geometry difference."
5. **Desk-only; says nothing about FDTD agreement at GEOM78 specifically.**
   The desk-propagator-vs-FDTD check (exp-046 Block A5, N_F≈0.54–65.6,
   0.03–5.68% residual) was performed only at A=752 — this cycle's own
   GEOM78 numbers carry no independent FDTD cross-check, at any n. Same
   status as exp-048 Block B's own numbers (mandatory fix 5, that module's
   own docstring): a re-parameterization + convergence characterization,
   not a physics validation against the engine.
6. **T24's ABSORB-boundary systematic (~+0.0070) was measured at A=752, not
   GEOM78** (§4, P-NCONV27-6's inline disclosure) — its relevance to a
   GEOM78 near-boundary reading is carried by analogy (same ABSORB=40,
   same order-of-magnitude domain), not independently measured. A genuine
   FDTD `ABSORB` sweep at GEOM78 is out of this cycle's own zero-FDTD scope
   (it is LOGBOOK's separately-queued item (2), not this one).
7. **Floating-point accumulation is negligible**, unchanged from exp-049's
   own argument (≈1.1×10⁻¹² relative at n=5121, nine orders below
   `ABS_TOL`) — the smaller Y-domain at GEOM78 (1448 vs 1504 cells,
   §2.1) only reduces this further.
8. **`n=401` remains a single fixed regression/reproduction value**, not a
   doubling-series member, at both geometries.
9. **No perceptual claim.** `C_THR=0.005` is cited only as the pre-existing
   decision line these readings are already scored against (VISION's T2
   bar) — this cycle issues no new perceptual verdict.
10. **Sign/ordering conventions are stated explicitly wherever a directional
    comparison is scored** (§4, P-NCONV27-2's own tier-index definition) —
    a direct, disclosed response to exp-049's own self-caught Phase-4
    `predicted_difficulty_rank()` sign-inversion erratum
    (`experiments/049-.../NOTES.md`, Phase-5 erratum section;
    `experiments/049-.../run.py:62-88`), so Phase 4 has no ambiguous
    "larger = harder or easier" convention left to invert by accident.

---

## 6. Cost note

**New FDTD calls: 0.** Pure `numpy`, reusing exp-049's own Phase-3-corrected
machinery and exp-048 Block B's own geometry-dict pattern; no `lab/` file
and no `experiments/042-.../design_geometry.py` or
`experiments/048-.../design_geometry.py` line is modified — a new, thin
geometry-parameterized module is added under `experiments/050-.../`
(Phase 4 work, not written yet, per the Director's brief).

**Scale:** the regression anchor (§2.3) re-evaluates exp-049's own full
sweep once, at `GEOM_EXP042_OLD` (36 cells × 3 functions × (8 N_SERIES
entries + n=401) = 972 evaluations-worth of records, identical in shape to
exp-049's own completeness ledger); the GEOM78 sweep repeats the same shape
once more. **Total: ≈2× exp-049's own 1,145,772 angle-sample evaluations ≈
2,291,544**, each a cached-matrix `G@amp` product against a domain
**3.7% smaller** (1448 vs 1504 Y-cells at GEOM78, §2.1) — if anything
marginally cheaper per evaluation, not more expensive. **Wall-clock
estimate: ≈90 minutes single-threaded**, obtained by doubling exp-049's own
*measured* (not estimated) 45m44s full-sweep runtime
(`experiments/049-.../NOTES.md`, Results section) — not a fresh guess, the
same profiling discipline Red Team's own Attack 4 established as mandatory
last cycle.

**Code footprint:** `experiments/050-.../design_geometry.py` (new,
geometry-parameterized, per §2.2) and `experiments/050-.../run.py` (new,
reusing exp-049's own `run.py` structure — `delta_step`, `find_nstar`, the
completeness ledger — parameterized over two geometries instead of one). No
new trust-suite stage (house convention, exp-048/049's own precedent — a
re-evaluation of already-committed desk functions at different geometry
arguments is not new physics machinery); P-NCONV27-0's regression anchor
plays the equivalent role for this cycle, now fully executable as written
(§2.3).
