# PHASE 1 — PROPOSAL · Panel Iteration 47 · Lead seat: QUANTUM OPTICS
## T28 mechanism, desk-check batch — zero FDTD cost

**Mandate:** PLAN.md's Iteration-47 queue, item 1 (Red Team's Phase-5
final-audit reconciliation of exp-069's six seats, near-unanimous):
characterize live thread T28 — the real, resolution-robust-at-two-points,
settled ~2.84° periodic oscillation in the `C80−C40` padding delta
(600nm, θ∈[36°,42°]) that does not match T21's own established fringe
period `P(θ)=λ/(A·cosθ)≈1.96°` — with a single zero-FDTD-cost desk-check
batch, before any new FDTD spend. Standing forward tripwire (Red Team,
exp-069 Phase-5 final audit): this must land by Iteration 48's close or
the gap itself becomes Checkpoint-4-adjacent.

---

## 1. Mechanism narrative (≤300 words)

T28's own first-principles argument (ELECTROMAGNETISM, exp-069 Phase 5,
verified) is that `A=752` is bit-identical for `C40`/`C80` by construction,
so a 45%-off best-fit period in `delta(θ)=C80(θ)−C40(θ)` is evidence of a
**second, physically distinct oscillatory contributor** — provisionally
attributed to `ABSORB` depth (40 vs 80 cells), the one thing that differs
between the two configs.

This proposal tests a **competing, equally falsifiable candidate**: that
the second contributor is tied not to `ABSORB` (which differs between
configs) but to a length scale that is **identical across the congruent
`C40`/`C80` series by construction** — most obviously `R_OUT`/`W_OBJ`
(both 78 cells at this bench's geometry, degenerate with each other here).
If the ~2.8°-family signature already lives in `C40(θ)` and `C80(θ)`
**individually** (item a, below), an ABSORB-tied mechanism is disfavored
relative to a geometry-invariant one — a real, pre-registered discriminator
between EM's own framing and this one, not a restatement of it.

Desk reconnaissance (reported transparently below, not smuggled into the
bands) finds a specific, simple, testable candidate: an effective aperture
`A_eff = A − 3·R_OUT = 752 − 234 = 518` cells reproduces the committed
600nm free-fit period (`P*=2.8421°`, back-solving to `A_eff≈518.81`,
0.16% off) and, independently, the beat-frequency reconstruction (item b)
lands a second-aperture branch at `A_alt≈233.19` cells — 0.35% from
`3·R_OUT=234`. Two independently-run zero-parameter searches converging
on the same small-integer relation is either a real geometric mechanism
(candidate: the object window itself acting as a secondary truncating
edge for the reflected/diffracted contribution) or a numerological
coincidence — which this batch is built to discriminate, not assert.

## 2. T1 escape route

**N/A** — instrument/model-fidelity work, identical in kind to
exp-041/065/066/068/069. No mechanism is proposed against constraint 3;
Checkpoint-criterion-2 candidacy is not claimed for any outcome here.

## 3. Parameter table — every quantity, formula, and data source

All quantities below are computed from data **already committed** in
`experiments/069-.../results.json` (`block_dense.rows`, 31 pts/600nm;
`block_leg750.rows`, 16 pts/750nm) and named constants **already
committed** in `experiments/065-t24-absorb-boundary-sweep/design_geometry.py`
(`CONFIGS`, `CPL`). Zero new FDTD calls. Methods marked "(reused)" import
`_fixed_period_fit`/`_free_period_search` verbatim from
`experiments/069-.../run.py` rather than re-deriving them — the identical
statistic, applied to new series, per this program's own R4 discipline.

| # | Quantity | Formula | Source data |
|---|---|---|---|
| 1 | `P(θ,λ)` — T21's established period | `λ_cells/(A·cosθ)`, `A=752` | `exp-069/design_geometry.py::P_deg` (reused) |
| 2 | `P*_delta`, `R²_delta` — free-fit period of `delta(θ)` (600nm) | grid search `P*∈[1.0°,4.0°]`, 400 pts, center=39°, fit in `sinθ` (reused `_free_period_search`) | already scored: `results.json::scored.p3` (`P*=2.8421°`, `R²=0.6272`) — **not recomputed, cited** |
| 3a | `R²_C40_fixed`, `R²_C80_fixed` — item (a) | `_fixed_period_fit(x, C_empty_C40, T=cpl/A)` / same for `C80` | `block_dense.rows` |
| 3b | `P*_C40`, `R²_C40`, `P*_C80`, `R²_C80` — item (a) | `_free_period_search` applied to `C_empty_C40(θ)`, `C_empty_C80(θ)` individually | `block_dense.rows` |
| 4 | `A_alt` (two branches) — item (b) | `1/P_beat=\|1/P(752,39°)−1/P(A_alt,39°)\|`, solved for `A_alt`, using `P_beat≡P*_delta` (row 2) | `P_deg`, row 2 |
| 5 | Named-constant search — items (b), (d) | for every `x∈NAMED` and every pair `x1,x2∈NAMED`, test `c·x`, `c1·x1+c2·x2` (`c,c1,c2∈{±1..±10}`) against `A_alt` (item b) and `A_eff` (item d) | `exp-065/design_geometry.py::CONFIGS["C40"]`/`CONFIGS["C80"]` — `A, TAPER, R_OUT, W_OBJ, GUARD_OUT, W_FLANK, D_SP, LEVER, ABSORB(40/80), PAD(0/40), aperture_cells, clear_plane, clear_src` |
| 6 | `P_taper(39°,600nm)` — item (c) | `λ_cells/(TAPER·cos39°)`, `TAPER=40` | row 1's formula, `TAPER` from `CONFIGS` |
| 7 | `A_eff` — item (d) | `cpl600/(radians(P*_delta)·cos39°)` | row 2 |
| 8 | 750nm cross-validation — item (d) | fit `delta_750(θ)` to fixed period `T_750=cpl750/A_eff_candidate`; report `R²` | `block_leg750.rows`; compare to already-committed `R²=0.348` (T21's own model) and the already-computed (uncommitted-to-code) post-hoc `R²=0.7666` |
| 9 | Convergence check — item (e), added | do the winning named-constant matches for `A_alt` (item b) and `A − A_eff` (item d) agree (same combination, or algebraically equivalent)? | rows 4, 5, 7 |

**NAMED constants (from `CONFIGS`, both configs share these by
congruent construction):** `A=752`, `TAPER=40`, `R_OUT=78`, `W_OBJ=78`,
`GUARD_OUT=185`, `W_FLANK=78`, `D_SP=223`, `LEVER=93`,
`aperture_cells=1504`, `clear_plane=37`, `clear_src=20`; plus the one pair
that differs by construction, `ABSORB∈{40,80}` and `PAD∈{0,40}`.

## 4. Which of (a)–(d) I keep, drop, reorder, add

**Keep all four**, engaged in full — no drops. **Reordered**: (a) first
(diagnostic, decides whether the signal is difference-only or
config-invariant — sharpens how to read (b)/(d)); (d) and (b) run
together, second (desk recon above shows they are linked: both search
the identical NAMED-constant space and, in preliminary arithmetic,
converge on the same candidate); (c) last (already fully resolved by a
single closed-form number, see §5).

**Added, item (e):** a convergence check between (b)'s beat-derived
`A_alt` and (d)'s directly-traced `A_eff` — if both independently point to
the same named combination, that is stronger evidence than either alone;
if they disagree, neither should be treated as more than a coincidence.
This was not in the original four-item list but falls directly out of
running (b) and (d) against the *same* NAMED-constant search space, which
the mandate already specifies for both — computing the overlap is free.

## 5. Falsifiable predicted outcomes

Every band below is a genuine test, not a restatement of the desk
reconnaissance in §1 — the reconnaissance used `numpy`/`scipy` ad hoc in
this session, not the exact code path Phase 3/4 must commit (R4: no
hand-typed figures cited as final). Bands are set with real width; the
reconnaissance numbers (disclosed) inform them but do not replace the
gated run.

| ID | Claim | CONFIRM | REFUTE |
|---|---|---|---|
| **P-070-1 (item a)** | The ~2.8°-family signature already lives in `C40(θ)` and/or `C80(θ)` alone (config-invariant hypothesis), not only in the difference. | `R²_free(C40)≥0.30` **AND** `R²_free(C80)≥0.30` (both individually resolve periodic structure in the searched window) | `R²_free(C40)<0.15` **AND** `R²_free(C80)<0.15` (signal exists only in the difference — favors EM's ABSORB-tied framing instead) |
| **P-070-2 (item b)** | The beat-frequency reconstruction (`P_beat≡P*_delta=2.8421°` against T21's `P(39°,600nm)=1.9608°`) yields an `A_alt` branch matching some `≤2`-term NAMED-constant combination. | best match within **1%** relative | no match within **10%** relative on either `A_alt` branch |
| **P-070-3 (item c)** | `TAPER=40` cells, alone, as a diffracting sub-aperture, predicts `P_taper(39°,600nm)` near the observed `P*=2.8421°`. | `\|P_taper−P*_delta\|/P*_delta ≤ 20%` | `\|P_taper−P*_delta\|/P*_delta ≥ 100%` |
| **P-070-4 (item d)** | `A_eff` (back-solved from `P*_delta`) matches some `≤2`-term NAMED-constant combination, **and** that combination's implied period fits the held-out 750nm leg at least as well as the already-known post-hoc free fit (`R²=0.7666`). | best match within **1%** relative **AND** `R²(750nm, candidate) ≥ 0.70` | no match within **10%** relative, **OR** best candidate's `R²(750nm) < 0.40` (does not clear T21's own model, R²=0.348, by a real margin) |
| **P-070-5 (item e, added)** | The `A_alt` (b) and `A−A_eff` (d) matches name the *same* NAMED combination (or an algebraically equivalent one). | exact same combination, both branches | different, unrelated combinations |

**Disclosed recon (informs, does not substitute for, the gated bands
above)**: preliminary arithmetic this session found `A−3·R_OUT=518` cells
(0.16% from the free-fit `A_eff≈518.81`) and a beat-derived
`A_alt≈233.19` (0.35% from `3·R_OUT=234`) — the same integer relation
from two independent routes — and `P_taper(39°,600nm)=36.86°`, over an
order of magnitude from `P*=2.8421°` (a clean REFUTE-side number for
P-070-3, computed directly, not fitted). These are cited so Phase 2/3
critique the actual claim, not a black box; the committed script (§6)
must reproduce them by running code, not by trusting this table.

## 6. Idealizations

1. 2D TMz, single polarization — unchanged from every upstream thread.
2. **Desk-only, zero new FDTD.** Every number here is arithmetic over
   already-committed `results.json`/`design_geometry.py` content.
3. Reuses only the 600nm DENSE block's 31 points and the 750nm LEG750's
   16 points — no new angles, no new λ, no new resolution or settling
   checks (those are P-069-4/5's job, already CONFIRMED/CONFIRMED, with
   P-069-5's own caveat about the two R3 cells sitting near a
   zero-crossing, carried forward unchanged, not re-litigated here).
4. **`R_OUT` and `W_OBJ` are numerically degenerate at this bench's own
   geometry (both 78 cells)** — any match this batch finds against
   `3·R_OUT` is equally a match against `3·W_OBJ`; this batch cannot
   distinguish "object radius" from "measurement window half-width" as
   the physically loaded quantity. A future geometry where `R_OUT≠W_OBJ`
   would be needed to break the tie — explicitly not this cycle's job.
5. The NAMED-constant search space (§3, row 5) is bounded to single terms
   and pairs with small-integer coefficients (`|c|≤10`) — a combination
   requiring three or more named terms, or a non-integer physical ratio
   (e.g. a resonance order, a refractive-index-scaled length), is out of
   scope and would not be found even if real.
6. The beat-frequency formula (item b) assumes a genuine two-tone linear
   superposition; if the real mechanism is nonlinear (e.g. a modulated
   envelope, not a sum of two sinusoids) the formula's algebra does not
   apply and a null result here does not rule out a related but
   non-additive mechanism.
7. This is explicitly a **numerology-vs-mechanism discriminator, not a
   mechanism proof.** Even a clean CONFIRM across P-070-2/4/5 licenses
   only "a specific, simple, falsifiable candidate survives a zero-cost
   check" — PLAN.md's own queue item 2 (EM's C60/C70 falsification test,
   which actually varies `ABSORB` while holding everything else fixed)
   is the correct next FDTD-cost step to test causation, not this batch.
8. Distinct from R2 (LOGBOOK RULED OUT) — R2 concerned an
   integer-multiple-of-λ **resonance** condition on shell thickness; this
   batch's small-integer candidates are ordinary geometric
   diffraction-aperture arithmetic (a length-scale ratio, not a
   wavelength-resonance order), a different claim class. Stated so Red
   Team does not need to re-derive the distinction.
9. `T_SINTHETA_600 = cpl/A` (T21's own period, expressed as the exact
   period of `d(sinθ)`) is treated as a fixed reference throughout — per
   exp-069's own Idealization 5, this is T21's fitted stationary-phase
   *model* under test (R²=0.7852→0.8271 at its own best fit), not
   independently-verified ground truth.

## 7. Script design (for Phase 3/4 — no further judgment calls needed)

**File:** `experiments/070-t28-mechanism-desk-check-batch/desk_check_mechanism.py`
(naming mirrors exp-069's own `desk_check_settling_delta.py` convention).

**Inputs** (read-only, no writes to either):
- `experiments/069-t21-block-mini-period-match-power-up/results.json` —
  `block_dense.rows` (600nm, 31 pts), `block_leg750.rows` (750nm, 16 pts),
  `scored.p3` (the committed `P*_delta`, `R²_delta`).
- `experiments/065-t24-absorb-boundary-sweep/design_geometry.py` —
  imported via the same `importlib.util.spec_from_file_location` pattern
  `exp-069/design_geometry.py::_load_exp065()` already uses (avoids the
  `design_geometry` module-name collision documented there); reads
  `CONFIGS["C40"]`/`CONFIGS["C80"]` and `CPL`.
- `experiments/069-t21-block-mini-period-match-power-up/run.py` —
  import `_fixed_period_fit` and `_free_period_search` directly (or copy
  verbatim with a one-line provenance comment if `run.py` is not
  import-safe as a module) rather than reimplementing the statistic.

**Computation, in order:**
1. Load `block_dense.rows`; extract `theta`, `C_empty_C40`, `C_empty_C80`,
   `delta` arrays.
2. **Item (a):** run `_fixed_period_fit(sinθ, C_empty_C40, T=cpl600/A)`
   and the same for `C_empty_C80`; run `_free_period_search` on each
   (identical grid: `P*∈[1.0°,4.0°]`, 400 pts, `center_deg=39.0`, matching
   `exp-069/run.py`'s own call exactly, for direct comparability to the
   already-committed `scored.p3` on `delta`). Score P-070-1.
3. Build `NAMED = {"A":752, "TAPER":40, "R_OUT":78, "W_OBJ":78,
   "GUARD_OUT":185, "W_FLANK":78, "D_SP":223, "LEVER":93,
   "aperture_cells":1504, "clear_plane":37, "clear_src":20,
   "ABSORB40":40, "ABSORB80":80, "PAD80":40}` read from
   `CONFIGS["C40"]`/`CONFIGS["C80"]` fields (`A`, `d_sp`, `lever`,
   `aperture_cells`, `clear_plane`, `clear_src`), plus the module-level
   `TAPER`, `R_OUT`, `W_OBJ`, `GUARD_OUT`, `W_FLANK` constants — **do not
   hand-type any of these values; read them from the imported module.**
4. **Item (b):** compute `P39_600 = P_deg(39.0, 600)` (reuse
   `exp-069/design_geometry.py::P_deg`); `P_beat = scored.p3.p_star_deg`
   (read from `results.json`, not retyped); solve both branches
   `inv_b = 1/P39_600 ± 1/P_beat` → `P_b = 1/inv_b` → `A_alt =
   cpl600/(radians(P_b)·cos(radians(39.0)))`. Search `NAMED` (§3 row 5,
   single terms and pairs, coefficients `-10..10` excluding 0) for the
   closest relative match to each `A_alt` branch; record best match name,
   value, and relative deviation. Score P-070-2.
5. **Item (c):** `P_taper = degrees(cpl600/(TAPER·cos(radians(39.0))))`.
   Compare directly to `scored.p3.p_star_deg`. Score P-070-3.
6. **Item (d):** `A_eff = cpl600/(radians(scored.p3.p_star_deg)·cos(radians(39.0)))`.
   Run the same `NAMED` search as step 4 against `A_eff` directly (not a
   beat branch). For the best match, compute `T_750 =
   cpl750/A_eff_candidate` and evaluate `_fixed_period_fit` against
   `block_leg750.rows`' `delta` series; report `R²`. Score P-070-4.
7. **Item (e):** compare step 4's and step 6's best-matching NAMED
   combinations (string/algebraic equality, e.g. `"3*R_OUT"` on both
   sides counts as a match even if derived as `A_alt` vs. `A−A_eff`
   respectively — normalize before comparing). Score P-070-5.
8. Write `experiments/070-t28-mechanism-desk-check-batch/results.json`
   with keys `{p1: {...}, p2: {...}, p3: {...}, p4: {...}, p5: {...},
   named_constants_used: {...}}` — every field code-produced, nothing
   hand-typed into NOTES.md except by copy from this file's own printed
   output (house rule R4).

**Pass/fail logic** (exactly the bands in §5's table — implement as
boolean `confirm`/`refute` fields per prediction, mirroring
`exp-069/run.py::score()`'s own dict shape so a future reviewer can diff
the two files structurally):

```
p1: confirm = (r2_free_c40 >= 0.30 and r2_free_c80 >= 0.30)
    refute  = (r2_free_c40 < 0.15 and r2_free_c80 < 0.15)
p2: confirm = (best_rel_dev_A_alt <= 0.01)
    refute  = (best_rel_dev_A_alt >= 0.10)   # for BOTH branches
p3: confirm = (abs(P_taper - P_star)/P_star <= 0.20)
    refute  = (abs(P_taper - P_star)/P_star >= 1.00)
p4: confirm = (best_rel_dev_A_eff <= 0.01) and (r2_750_candidate >= 0.70)
    refute  = (best_rel_dev_A_eff >= 0.10) or (r2_750_candidate < 0.40)
p5: confirm = (normalized_combo_b == normalized_combo_d)
    refute  = (normalized_combo_b != normalized_combo_d)
```

No Combined Verdict gate is proposed here (unlike exp-069's five-way
conjunction) — these five items are diagnostic and largely independent,
each answering a distinct sub-question the mandate names; Phase 3 should
report each individually and let the Iteration-47 queue's own item 2
(EM's C60/C70 test, or PHOTONICS' re-run) be *narrowed* by whichever of
P-070-1 through -5 confirm, per PLAN.md's own stated design.

## 8. Checkpoint-criterion-2 candidacy

**Explicitly declined**, matching exp-069's own framing. This batch can
at most identify or rule out a candidate geometric explanation for a
model-fidelity question; it bounds no mechanism class and makes no
constraint-3 claim.
