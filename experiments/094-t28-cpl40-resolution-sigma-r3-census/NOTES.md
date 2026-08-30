# exp-094 — T28 cpl=40 Resolution Check, sigma_max Comparability Close, R3 Census

*Panel Iteration 71. Lead seat: QUANTUM OPTICS. Runner: photonlab-shift
(cloud panel routine). Full phase record: `phase1_proposal.md` (QUANTUM
OPTICS) → five blind Phase-2 critiques (PHOTONICS, MATERIALS,
ELECTROMAGNETISM, THERMODYNAMICS, VISION SCIENCE, unanimous
support-with-changes, five distinct, non-overlapping catches) →
`phase2_redteam_audit.md` (PROCEED-WITH-MANDATORY-FIXES, 5 items, zero
overridden) → `phase3_synthesis.md` (this cycle's frozen spec, all 5 fixes
adopted, Director's own independent third-derivation of the one disputed
figure set, bit-exact match both prior derivations).*

## Hypothesis

exp-093 (Iteration 70) left the T28 upper-window sub-thread with three
genuinely open gaps, all named in its own Next section and PLAN.md's
Reconciled Iteration-71 queue: (1) the SINGLE-NULL verdict at 41.75°–41.90°
is angular-resolution-verified only, not yet R15-grade cross-`cpl`-verified
(Idealization 16); (2) a real `sigma_max`-sensitivity discovered at the
upper near-null (item 3's sign flip at 42.0°) leaves the window's flanking
anchor at 41.6° on a different sigma basis than the interior sweep,
uncorrected; (3) three of exp-090's original seven `cpl=20` caution-zone
points (36.0°, 38.4°, 38.8°) have never been measured at `cpl=30` at all —
R15's own founding discharge condition, the single most-repeated open item
on the whole T28 board.

This cycle closes all three in one combined build, in cheapest-and-
independent-first order (no item gates another's parameter choice — a
genuine departure from exp-092/093's own gated 5→3→1→2→4 chain, justified
by the absence of any cross-item dependency here). It makes **no
phenomenon-mechanism claim** — T1 escape route N/A, Checkpoint criterion 2
N/A, matching every T28 desk/instrument cycle since exp-069 (independently
re-verified against LOGBOOK.md's own unbroken record by the proposing seat,
all five Phase-2 critics, and Red Team). It is pure instrument
recalibration.

## Setup

**Channel:** `PAIR_KEYS_R3=("C40_R3","G40_R3")` at `cpl=30` for Rank 2/3,
plus a genuinely new `PAIR_KEYS_R4=("C40_R4","G40_R4")` congruent geometry
family at `cpl=40` for Rank 1. λ=600nm throughout. All `R3`-family geometry
(`R3_CONFIGS`, `PEC_R_R3`, `R3_R_OUT_CELLS`, `BOX_CLEARANCE_A/B_R3`,
`REF_HALF_H_R3`, `DENSE_ANGLES`, `A_HALF_APERTURE=752`/`1128`) reused
verbatim from `experiments/069-.../design_geometry.py` and
`experiments/091-.../092-.../093-.../run.py` — zero `lab/` diff, zero
existing-file diff. The new `R4` family (§ below) is additive only.

**Three items, sequenced cheapest-and-independent-first** (no cross-item
gate this cycle — unlike exp-093's own item 3→1 dependency, none of Rank
2/3/1 sets a parameter for either of the others; Rank 2 tests one flanking
anchor at an angle already known, at native sigma, to sit well clear of the
interior null; Rank 3 tests three angles entirely outside the
41.6°–42.0° window; Rank 1 is self-contained, its own settling precondition
gating only its own interior sweep):

| Order | Queue rank | Item | Configs | Angles | `cpl` | `STEPS` | `sigma_max` | Calls |
|---|---|---|---|---|---|---|---|---|
| 1st | **Rank 2** | sigma@41.6° | `C40_R3`,`G40_R3` | 41.6° | 30 | 4200 | 1/3 (corrected) | **4** |
| 2nd | **Rank 3** | census R3-verify | `C40_R3`,`G40_R3` | 36.0°, 38.4°, 38.8° | 30 | 4200 | 0.5 (native) | **12** |
| 3rd | **Rank 1a** | `cpl=40` settling gate | `C40_R4`,`G40_R4` | 41.825° | 40 | 5600 vs 8400 | 0.25 (corrected) | **8** |
| 3rd | **Rank 1b** | `cpl=40` interior sweep | `C40_R4`,`G40_R4` | 41.750,41.775,41.825,41.850,41.875,41.900 | 40 | 5600 | 0.25 (corrected, gated on 1a settling only) | **24** |
| 4th | **Rank 3-ext** | caution-zone growth, `cpl=30`-only, desk only | — | — | — | — | — | **0** |
| **Total** | | | | | | | | **48** |

**Estimated cost:** Rank 2 ≈13.5 CPU-min; Rank 3 ≈40.4 CPU-min; Rank 1
≈271.1 CPU-min (79.7 settling + 191.4 sweep). **Total ≈325 CPU-min**, wall
≈80–100 min at 4 workers (model estimate; every prior T28 cycle's actual
wall time has landed well under its own model estimate — e.g. exp-093's
29.4 min actual vs. 55–166 min estimated).

**Rank 2 — sigma@41.6° (sigma-comparability close, lower flanking edge).**
exp-093's item 3 found `delta_scene` at 41.8°/42.0° moves 4.71×/sign-flips
under the τ_center-preserving `sigma_max` correction (native 0.5 →
corrected 1/3). The interior sweep (41.75°–41.90°) that produced the
SINGLE-NULL verdict therefore ran at corrected sigma, while the flanking
anchor at 41.6° (exp-091's own Leg-4 bracket) has only ever been measured
at native sigma. This item measures 41.6° at corrected sigma, completing a
sigma-consistent curve across the *entire* 41.6°–42.0° window for the first
time. **Calls the existing `R3`-family `cell_metrics_full`/`pair_metrics_full`
(the `_full` variant, unconditionally — matching exp-093's own item1/item3
idiom exactly; no plain-variant code path exists in the reused machinery
to choose between).**

**Rank 3 — census R3-verify, three angles.** 36.0°, 38.4°, 38.8° — three of
exp-090's original n=7 caution-zone points, never measured at `cpl=30`.
Measured at native sigma (matching the original `cpl=20` dataset's own
basis; these three angles sit far from any known or suspected
interference null, so the sigma-sensitivity localized to the 41.8°/42.0°
near-null by exp-093's item 3 is not expected to apply here — disclosed as
an assumption, not re-verified this cycle, Idealization 21). Also calls the
`_full` metrics variant, per the same house-idiom reuse as Rank 2.

**Rank 1 — `cpl=40` congruent-geometry resolution check.** A new `R4`
family (`R4_RATIO=2.0`, mechanically substituted for `R3_RATIO=1.5` into
the already-committed `r3_config()` recipe — additive only, zero
`lab/`-diff, zero existing-file diff beyond appending the new `R4_*` block
the same way exp-091 additively appended `G40_R3`). Re-sweeps the same six
interior near-null points exp-093 swept at `cpl=30`, at the analogous
τ_center-preserving corrected sigma (`SIGMA_R4_CORRECTED=0.25`), to make
the SINGLE-NULL verdict cross-resolution-verified per R15, exactly as
exp-093's own Idealization 16 named.

**New geometry constants** (append to `experiments/069-.../design_geometry.py`):

| Constant | Formula | Value |
|---|---|---|
| `R4_RATIO` | `40/20` | `2.0` |
| `R4_CPL` | `{600: 40}` | — |
| `R4_BASE_NX` | `round(360*R4_RATIO)` | `720` |
| `R4_BASE_NY` | `round(1584*R4_RATIO)` | `3168` |
| `R4_BASE_ABSORB` | `round(40*R4_RATIO)` | `80` |
| `R4_BASE_OBJ_Y` | `R4_BASE_NY//2 − R4_BASE_ABSORB` (un-tabulated in the `R3` family too — same derived-quantity precedent) | `1504` |
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
| `SIGMA_R4_CORRECTED` | `SIGMA_NATIVE/R4_RATIO` — **derivable from first principles** (EM's own Phase-2 re-derivation, independently confirmed against `lab/fdtd2d.py`'s own E-update/loss coefficient: this is the condition holding the shell's accumulated optical depth `2·σ·r_out(cells)` invariant under a pure grid-density rescale, not merely an empirical pattern-match at one ratio) | `0.25` |
| `DX_M_R4` | `600e-9/40` | `1.5e-8` m |
| `L_GEOMETRIC_M_R4` | `R4_R_OUT*DX_M_R4` | `2.34e-6` m (must equal `L_GEOMETRIC_M`/`L_GEOMETRIC_M_R3` exactly) |

`R4_CONFIGS = {"C40_R4": r4_config(80, 0), "G40_R4": r4_config(80, 80)}`.
Both configs give `A = obj_y − y_lo = 1504 = round(752·2.0)`, the same
congruent-construction identity `R3_CONFIGS` already asserts.

**New functions** (thin, mechanical mirrors of the existing `R3` layer):
`box_for_r4`, `ref_for_r4`, `build_article_r4_sigma`, `_run_sim_r4_sigma`,
`one_call_r4`, `cell_metrics_r4` (the one genuinely necessary new function —
`cell_metrics` is hardcoded to `dg.R3_CONFIGS`/`box_for_r3`; `pair_metrics`/
`pair_metrics_full` are called on its output **unmodified**, they only
consume cell dicts, never a resolution constant directly). Rank 3's desk
extension reuses exp-093's own `compute_zone()` verbatim on an extended
`rows_subset` — no new function.

### Mandatory new-suite gates (PANEL.md's "new machinery ⇒ new suite stage
with ≥1 absolute identity gate" requirement)

1. Vacuum-footprint precondition (existing idiom, unmodified), applied to
   `R4_CONFIGS`.
2. `assert R4_CONFIGS["C40_R4"]["A"] == R4_CONFIGS["G40_R4"]["A"] ==
   round(A_HALF_APERTURE*R4_RATIO) == 1504`.
3. `assert abs(L_GEOMETRIC_M_R4 - L_GEOMETRIC_M) < 1e-12` — physical shell
   radius bit-identical across native/`R3`/`R4`.
4. `assert abs(SIGMA_R4_CORRECTED - 0.25) < 1e-12`.
5. **(NEW, Red Team RT-1, the discriminating gate.)** Immediately after
   each `build_article_r4_sigma(sim, cx, cy, sigma_max)` call in Rank
   1a/1b, **before any FDTD step runs**:
   `assert np.isclose(sim.sigma_e[shell_mask].max(), sigma_max,
   atol=1e-9)`, where `shell_mask` selects the article's own shell cells
   (mirroring the indexing `build_article_r4_sigma` itself uses) and
   `sigma_max` is the exact value passed at that call site. This is the
   first runtime-array sigma gate anywhere in this sub-thread's history —
   gates 1–4 (and every sigma-related gate any prior T28 cycle has ever
   shipped) check only Python constants, never what value actually lands
   in the constructed `Sim` object; a copy-paste sigma-constant slip at
   this new family's call sites would sail through gates 1–4 undetected,
   reproducing R15's exact founding defect (exp-091: `sigma_max` left
   un-rescaled at runtime despite a correct formula already existing,
   found only by hand at Phase 5) one call-site over. **Mandatory, per
   Red Team's Phase-2 audit.**
6. **(Documentation-only, non-discriminating — retained for the physical
   record, must never be read as a substitute for gate 5.)** EM's own
   proposed static assert, `abs(2*SIGMA_R4_CORRECTED*R4_R_OUT -
   2*SIGMA_NATIVE*R_OUT) < 1e-9` — independently shown at Phase 3 to reduce
   algebraically to a tautology already implied by gate 4 at any value of
   `SIGMA_NATIVE`/`R_OUT`/`R4_RATIO`, i.e. it cannot fail given gate 4
   passes, so it verifies nothing gate 4 doesn't already. Kept only because
   it documents the physical τ_center-invariance argument explicitly.

**Results-file convention (Red Team RT-4, mandatory):** this cycle's own
`results.json` carries the identical top-level `netd_disclaimer` key
`experiments/093-.../results.json` established ("NETD is an
instrument/detector threshold, not a human perceptual one... does NOT bear
on constraint-3/4's human-eye verdict"), written unconditionally at the top
level, regardless of whether any NETD byproduct field (produced because
Rank 2/3 call the `_full` metrics variant, per house-idiom reuse) is ever
printed to `run_output.txt`.

## Idealizations

**Carried forward from exp-093's own list, cited by original number:** 1
(2D TMz, 600nm only), 3 (NETD ≠ human-eye threshold — this cycle's `_full`-
variant byproducts are NETD/instrument-scoped only, no human-eye claim), 6
(`FLOOR` applied, not recomputed, at every new point), 7 (no constraint-
1/2/3/4 test, no T1 position), 8 (unbiased margin-vs-distance rebuild on
the full 31-point window remains open), 11 (a sigma-branch verdict at one
angle does not, by itself, revalidate comparability elsewhere), 12–13
(Yee-dispersion desk work untouched by this cycle), 15 (the zone table's
40.0°/40.2° treatment as independent members unchanged), 16 (angular-only
resolution results are not automatically R15-grade cross-resolution
findings — this is what Rank 1 exists to partially relieve for the
interior near-null specifically).

**New this cycle:**

17. The `R4` (`cpl=40`) geometry family is a mechanical, zero-design-
    freedom substitution of `R4_RATIO=2.0` for `R3_RATIO=1.5` into the
    already-committed `r3_config()` recipe. If the `R3`-family recipe
    itself carries any undetected systematic bias, `R4` inherits it
    unchanged; the two families are not independent confirmations of the
    underlying re-discretization scheme, only of the specific feature
    under test at two grid densities.
18. `SIGMA_CORRECTED(RATIO) = SIGMA_NATIVE/RATIO` is, per EM's own
    independent Phase-2 re-derivation from `lab/fdtd2d.py`'s own E-update/
    loss coefficient (confirmed at Phase 3), derivable from first
    principles as the condition holding the shell's accumulated optical
    depth invariant under a pure grid-density rescale — not merely an
    empirical pattern-match confirmed at one ratio and extrapolated to a
    second. This does not make gate 4 (which still pins the specific
    numeric value at `R4_RATIO=2.0`) or gate 5 (which still confirms the
    derived value actually reaches the constructed object) unnecessary.
19. Rank 1's `cpl=40` settling precondition is a single-angle (41.825°),
    both-config spot-check, not an exhaustive per-angle settling
    verification of all six interior points — matching this program's own
    established spot-check convention.
20. Rank 1 is localized to the interior near-null band (41.75°–41.90°)
    only. It does not re-verify the flanking anchors, the located lower
    crossing (40.0718°), or any other point in the 36°–42° dense window at
    `cpl=40` — R15's own "no `cpl=40` comparator exists anywhere on this
    channel" discharge condition gets its first-ever data point on this
    channel, localized, not a channel-wide resolution census.
21. Rank 3's three census points are measured at native `sigma_max=0.5`
    only, not cross-checked at corrected sigma — because item 3 (exp-093)
    localized the demonstrated sigma-sensitivity to the 41.8°/42.0°
    near-null specifically, and 36.0°/38.4°/38.8° sit far from any known or
    suspected null. If a future cycle finds sigma-sensitivity is not in
    fact localized to near-null regions, this choice should be revisited.
22. Rank 2's sigma-consistency close is local to 41.6°; it does not extend
    corrected-sigma coverage to 36°–41.4°, where no contamination has been
    demonstrated or suspected.
23. **(New, Red Team RT-5.)** exp-093's own energy-flatness/UNDETECTABLE
    finding (item 5b, Learned #2) is verified at `cpl∈{20,30}` only. Rank
    1b's `p_abs_w` check (§ Predictions) is this sub-thread's first test of
    whether that finding is itself resolution-robust at `cpl=40` — a
    genuinely new question, not assumed pre-answered by extension from
    lower resolutions.

**Carried idealizations banner (mandatory at both this section and the
Predictions section, per the Iteration-65 CHECKPOINT's non-discretionary
rule): every prediction below is governed by Idealizations
1/3/6/7/8/11/16 plus this cycle's own 17–23.**

## Predictions (frozen, committed BEFORE any Phase-4 script runs)

*Every prediction below is governed by Idealizations 1/3/6/7/8/11/16 plus
this cycle's own 17–23.*

**(Rank 2, PRIMARY) sigma@41.6°.** At native sigma (already filed,
`experiments/091-.../results.json::raw.r3_leg4_cpl30_steps4200_bracket
["41.6"]`, independently re-derived a third time at Phase 3, bit-exact):
`delta_scene=+1.7838×10⁻⁴`, `frac_contrast=3.3296×10⁻⁴`, `ratio_k=25.9467`,
`frac_p_abs=8.6392×10⁻³`, `floor_pass=True`. Scored with exp-092/093's own
`[0.3,3.0]` CONFIRM / `[0.1,10]` REFUTE bands on `{corrected}/{native}` for
both `delta_scene` (sign+ratio) and `frac_contrast` (ratio), worst-case
across both quantities, exactly as item 3 did. **No confident directional
lean stated** (RT-2/Phase-3 correction, replacing the pre-freeze draft's
now-struck "CONFIRM is more likely" reasoning): 41.6°'s `ratio_k=25.9467`
sits inside the *same* high-`ratio_k`, near-null-adjacent population as
exp-093's own confirmed-fragile interior sweep (20.48×–29.58×, floor-
clearing points only), not the far-from-null CONSISTENT population
(0.076×–3.841×) — the R13/R14 mechanism this house has established (a
large `ratio_k` against a near-flat `frac_p_abs` numerator signals a small
`frac_contrast` denominator, i.e. proximity to a null) applies here at
least as plausibly as the opposite reading. REFUTE is disclosed as at
least as plausible as CONFIRM; either outcome is reported as informative,
not as a surprise requiring explanation. **Informational, non-gating:**
`p_abs_w` ratio expected within 2–5% of the 0.51 T9 anchor (matching item
3b's own precedent).

**(Rank 3, PRIMARY) census R3-verify, three angles.** Original `cpl=20`
values (independently retrieved from `experiments/090-.../run.py`'s own
committed `dataset`): 36.0°→`ratio_k=2.6424,Y=0` (exp-087); 38.4°→
`ratio_k=0.9075,Y=0` (exp-088); 38.8°→`ratio_k=3.8733,Y=0` (exp-088). All
three sit comfortably below `RATIO_HIGH=10.0` at `cpl=20`. Falsifiable
three-way outcome per angle: **CONSISTENT** (`floor_pass=True`, same `Y` at
`cpl=30`); **FLIPPED** (`floor_pass=True`, different `Y`); **NODE-
UNRESOLVABLE** (`floor_pass=False`). **Informed, not confident, lean:** the
modal expectation is CONSISTENT (`Y=0`) at all three — but this program's
own record directly warns against over-trusting "comfortable" margins:
41.4° (`ratio_k=28.8`, nearly 3× further from the boundary than any of
these three) FLIPPED under the identical `cpl=30` R3 check (exp-091). Any
FLIPPED or NODE-UNRESOLVABLE reading is reported as a genuine finding, not
downweighted for contradicting the modal expectation.

**(Rank 1a, PRIMARY, gates Rank 1b) `cpl=40` settling precondition.**
CONFIRM/PASS = `|delta_scene(STEPS=8400) − delta_scene(STEPS=5600)| /
|delta_scene(STEPS=5600)| ≤ 1×10⁻²` at both `C40_R4` and `G40_R4`
(deliberately loosened from this program's historical ~10⁻⁴–10⁻⁵ clean-
settling bar, because 41.825° sits inside a near-total-null where the
underlying quantity is a small residual — R14's caution, applied here to a
settling check). CAUTIONARY-PASS (proceed, flag results settling-
uncertain) = `1×10⁻² < \text{rel. dev.} ≤ 1×10⁻¹`. HALT (do not spend Rank
1b's 24 calls) = `>1×10⁻¹` at either config.

**(Rank 1b, PRIMARY) `cpl=40` interior three-way outcome.** Identical
categories to exp-093's own item 1: **TWO-NODE CONFIRMED** (≥1 point
`delta_scene>0` AND `floor_pass`); **SINGLE-NULL** (all six points
`delta_scene≤0`); **STILL AMBIGUOUS** (no point clears the floor gate
either direction). **Informed, not confident, lean:** SINGLE-NULL is the
modal expectation (matching `cpl=30`'s own clean result, MATERIALS' own T10
near-field/curved-boundary account for why resolution moves this class of
feature continuously) — explicitly not a confident lean, since prior
resolution changes on this exact channel (41.4°'s own `cpl=20→30` flip;
item 3's own `sigma_max` sign flip at 42.0°) have gone the other way.
**Informational, non-gating:** at any `cpl=40` point within ±0.025° of a
`cpl=30` floor-clearing point, `ratio_k` expected same-order-of-magnitude
ENERGY-DOMINANT (`10×`–`60×`, loosened around the `cpl=30` figures' own
20.5×–29.6×). **Informational, non-gating (NEW, Red Team RT-5).** `p_abs_w`
ratio (G4/C4, per angle) expected within 2–5% of the 0.51 T9 anchor,
computed at zero additional FDTD cost from the already-budgeted 32 calls —
this sub-thread's first test of whether exp-093's own energy-flatness/
UNDETECTABLE finding (`cpl≤30`-verified only, per Idealization 23) extends
to `cpl=40`. A deviation outside 2–5% here would be a genuine, previously-
unexamined surprise, not smoothed over.

**(Rank 3-ext, PRIMARY, zero-FDTD) caution-zone growth.** Re-invoke
`compute_zone()` on the existing `cpl=30`-only `n=8` table (exp-093 item 2)
plus every one of the three new Rank-3 points that clears `floor_pass`
(excluded if NODE-UNRESOLVABLE) — `cpl=30`-only throughout, Rank 1's
`cpl=40` data deliberately NOT mixed in. CONFIRM = the extended zone is
non-inverted and the live recomputation reproduces `auc`/Firth/zone figures
bit-exact on re-run. No numeric band is pre-committed for the value itself
(circular); the falsifier is explicit: an inverted zone (any `Y=1` margin
exceeding any `Y=0` margin) is reported as a genuine R15-relevant finding,
matching exp-090's own founding falsifier clause.

## T1 escape route

**N/A** — independently re-verified against LOGBOOK.md's own record by the
proposing seat, all five Phase-2 critics, and Red Team: every T28
sub-thread entry from Iteration 46 through Iteration 70 states T1 route
N/A / Checkpoint criterion 2 N/A. This cycle takes no position on
σ(I)/σ(x,t)/angular selectivity/sub-threshold operation, makes no
phenomenon-mechanism claim, and does not touch `REALIZABILITY_MEMO.md`.

## Realizability bound

**N/A.** Pure instrument/desk-recalibration cycle: no new material,
mechanism, or optical-response claim is made anywhere in this document.
`REALIZABILITY_MEMO.md` is not opened, cited, or re-scored.

## Result

*(Added post-Phase-4, before Phase-5 review, per this program's own
Result-section-existence safeguard. All 48 FDTD calls ran, all six house
gates PASS — including the new Gate 5 runtime `sigma_e`/`sigma_max` check
(Red Team RT-1), which fired inline on all 16 Rank 1a/1b article calls
before any FDTD step. **Correction (Red Team Phase-5 final audit, Fix
#1):** this paragraph originally claimed Gate 5 was verified "by injecting
a simulated R15-style wiring defect into a standalone test harness during
Phase 4" — no such artifact existed anywhere in the committed record when
this sentence was first written, an unverifiable claim three independent
Phase-5 seats (QUANTUM's own self-review, MATERIALS, PHOTONICS) caught
blind. What actually happened: `gate5_wiring_defect_verification.py`
(Director, written and run **mid-Phase-5**, after those three seats' own
findings, not during Phase 4) is the real, permanent, reproducible
artifact — independently re-executed a fourth time by Red Team's own final
audit, confirming Gate 5 correctly raises `AssertionError` against an
injected wiring defect while passing silently on correct wiring. The
underlying scientific claim was true throughout; its first description of
how and when it was verified was not. Trust suite 41/41 green both before
and after this run.
Zero `lab/` diff. Total wall time 3033.7s (50.56 min), well under the
80–100 min model estimate — matching this program's own established
"actual lands under the model estimate" track record. Full record:
`run_output.txt`, `results.json`.)*

**(Rank 2) PRIMARY — CONFIRM.** `delta_scene` ratio (corrected/native)
1.0766, `frac_contrast` ratio 1.0856, both sign-matched and inside
`[0.3,3.0]`. Per Phase 3's corrected, no-lean framing (RT-2), this CONFIRM
was reported as no more or less likely than REFUTE going in — it landed
CONFIRM. **Informational:** `p_abs_w` (G/C) ratio 1.0085 (within 1% of
unity); `ratio_abs_ext_raw` deviates 0.81% from the 0.51 T9 anchor.

**(Rank 3) PRIMARY — TWO CONSISTENT, ONE FLIPPED.** 36.0°→CONSISTENT
(`ratio_k` 2.6424→2.4582, `Y=0` both resolutions); 38.8°→CONSISTENT
(`ratio_k` 3.8733→2.2729, `Y=0` both resolutions); **38.4°→FLIPPED**
(`ratio_k` 0.9075→16.9967, `Y=0`→`Y=1`, crossing `RATIO_HIGH=10` by a wide
margin). This is the modal-expectation-violating outcome NOTES.md's own
Predictions section explicitly flagged as plausible and non-downweighted:
38.4°'s `cpl=20` `ratio_k` (0.9075) was the single SMALLEST of all seven
original n=7 points — comfortably far from `RATIO_HIGH`, by raw margin —
yet flipped at `cpl=30` by nearly a factor of 19, a larger **fold-change**
than 41.4°'s own precedent-setting flip at exp-091 (28.85→9.21, itself
already a reclassification) — **correction (Red Team Phase-5 final audit,
Fix #5, PHOTONICS' own catch)**: by raw magnitude, 41.4°'s swing (19.60)
actually exceeds 38.4°'s (16.09); only the fold-change reading (18.73×
vs. 3.13×) supports "larger," and that is the comparison intended here.
All three points clear `floor_pass=True` at `cpl=30` — none is
`NODE-UNRESOLVABLE`.

**(Rank 1a) PRIMARY — PASS.** `rel_dev=0.1297%` between `STEPS=5600` and
`STEPS=8400` at 41.825°, comfortably under the `1×10⁻²` CONFIRM/PASS bar
(and far under the `1×10⁻¹` HALT bar) — Rank 1b proceeded at
`sigma_max=SIGMA_R4_CORRECTED=0.25` as pre-registered.

**(Rank 1b) PRIMARY — TWO-NODE CONFIRMED, and a materially stronger
reversal than that category name alone conveys.** At least one interior
point clears `delta_scene>0 AND floor_pass` — the pre-registered
TWO-NODE-CONFIRMED bar. **What actually happened is stronger: all six
interior points (41.750°–41.900°) read `delta_scene>0`, `floor_pass=True`,
classification CONSISTENT** (`ratio_k` range 3.67–7.13) — not merely one
excursion inside an otherwise-negative trough, but the *entire* previously
near-total-null band exp-093 measured at `cpl=30` (all six points there
read `delta_scene≤0`, four ENERGY-DOMINANT at `ratio_k` 20.5×–29.6×,
classified SINGLE-NULL) **reads oppositely in both sign and
classification at `cpl=40`.** This is disclosed exactly as measured, not
downgraded to fit the pre-registered category's literal wording: exp-093's
own SINGLE-NULL verdict does not survive R15-grade cross-`cpl`
verification — the specific failure mode R15 (adopted Iteration 68) exists
to catch, now realized on its own founding sub-thread's own most recent
headline result, one cycle later. **Informational (Red Team RT-5):**
`p_abs_w` (G4/C4) ratio stays within 0.57% of 1.0 across all six angles.
**Correction (Red Team Phase-5 final audit, Fix #4, VISION's own catch):**
this paragraph originally claimed exp-093's own energy-flatness/
UNDETECTABLE finding "is directly confirmed to extend to `cpl=40`" — only
the energy-**flatness** half (the `p_abs_w` ratio, above) was actually
measured; the UNDETECTABLE/NETD-**classification** half
(`netd_classification`/`dt_ss_full_K`) was computed internally by
`cell_metrics_r4` for every one of these six cells but never extracted
into this cycle's own report or `results.json` — a genuine
"confident-claim-unverified" gap, the same shape exp-093's own
THERMODYNAMICS self-review caught one cycle earlier. **Fix #2/#3 applied
post-audit (zero-FDTD-marginal-cost, deterministic rerun): see the
`dt_ss_full_K`/`netd_classification` values now cited directly below**,
replacing the withdrawn inference-only claim.

**(Rank 3-ext) PRIMARY — CONFIRM.** Base `n=8` table reproduces exp-093's
frozen figures bit-exact (`auc=1.0000`, zone `[4.1083,5.4287]`,
`firth_β=[3.76504788,−5.60700572]`, `m₅₀=4.6934`, naive MLE diverges).
Extended `n=11` table (all three new Rank-3 points clear `floor_pass`, per
NOTES.md's "excluded only if NODE-UNRESOLVABLE" rule — including 38.4°,
now `Y=1`) remains **non-inverted** (`zone=[4.1083,5.4287]` unchanged at
the boundary-setting values, `firth_m₅₀` shifts to 4.3832, `auc=1.0000`
unchanged) — no falsifier fires.

## Learned

1. **R15's own concern is not hypothetical — it just fired, on R15's own
   founding sub-thread, one cycle after the SINGLE-NULL verdict it was
   meant to stress-test was filed.** Exp-093's `cpl=30` SINGLE-NULL reading
   of the 41.75°–41.90° interior does not merely fail to be confirmed at
   `cpl=40` — it reverses in both sign and classification at every single
   sampled point in that window. This is now the third distinct instance
   on this exact 41.6°–42.0° window, across three consecutive cycles
   (41.4°'s `cpl=20→30` flip at exp-091; `delta_scene`'s `sigma_max`
   sign-flip at 42.0° at exp-093; this cycle's full-window `cpl=30→40`
   reversal), of a "settled-looking" reading in this narrow angular band
   moving under a resolution or numerical-parameter change most of this
   sub-thread's other angles do not show this sensitivity to.
2. **The energy channel keeps not moving.** Across three different kinds
   of perturbation now applied specifically to this near-null band
   (`cpl` 30→40 this cycle, `sigma_max` native→corrected at exp-093,
   angular density at exp-093's own item 1) the absorbed-power channel
   (`p_abs_w`, `ratio_abs_ext_raw`) has never shown a swing exceeding ~1%,
   while the coherent `delta_scene`/`frac_contrast`/`ratio_k` channel has
   reversed sign and/or classification at least three times in the
   identical window. R14's own mechanistic account (the oscillatory
   imprint lives in the `σ_ext(θ)` config-differential term, never the
   absorption/scattering partition) continues to hold at a third
   resolution.
3. **A "comfortable" `cpl=20` margin from `RATIO_HIGH` is not a reliable
   predictor of `cpl=30` stability**, now demonstrated a second time on two
   different points by two different cycles: 41.4° (exp-091, margin ~2.9×
   from the boundary by raw ratio) and 38.4° (this cycle, margin ~11×) both
   flipped, while several points with comparable or smaller `cpl=20`
   margins (37.2°, 39.2°–39.8°) did not. The direction and magnitude of a
   `cpl`-refinement-driven change on this channel appears to depend on
   proximity to the underlying oscillatory feature's own zero-crossings,
   not on the raw classifier margin at the coarser resolution.
4. Gate 5 (this cycle's new runtime `sigma_e`/`sigma_max` array check) is
   this sub-thread's first-ever verification that actually reads the
   constructed `Sim` object rather than a Python constant. **Correction
   (Red Team Phase-5 final audit, Fix #1):** confirmed a genuine
   discriminator not during Phase 4 but **mid-Phase-5**, by
   `gate5_wiring_defect_verification.py` (Director), independently
   re-executed a fourth time by Red Team's own final audit — see the
   Result section's own correction above for the full provenance. This
   class of gate should be considered for retrofitting onto the `R3`
   family's own existing sigma-branch call sites (exp-091/092/093), which
   have never had an equivalent check (ranked #6, Iteration-72 queue,
   MATERIALS' own finding).
5. **(New, added post-Red-Team-audit.)** A verification claim ("we tested
   X") is exactly as subject to this program's own R4 house rule
   (recompute-don't-hand-type) as a numeric figure — this cycle produced
   the rule's first instance applied to a claim ABOUT verification itself,
   independently caught by three Phase-5 seats (QUANTUM's own self-review,
   MATERIALS, PHOTONICS) before it reached any later cycle's citation.

## Next (ranked, pending Phase 5's own six blind reviews + Red Team's final audit — provisional)

1. **The 41.6°–42.0° window's own status is now genuinely three-way
   unresolved across `cpl∈{20,30,40}`**, not merely "SINGLE-NULL, pending
   R15 verification" as exp-093 left it. A `cpl=50` (or higher) check at
   the same six interior points would show whether the sequence is
   converging toward one of the two readings, oscillating, or genuinely
   non-convergent under this bench's own discretization scheme —
   Idealization 17's own disclosed risk (the `R3`/`R4` families are not
   independent confirmations of the re-discretization scheme itself) is
   now directly load-bearing to interpreting this reversal.
2. **38.4°'s flip deserves the same kind of dedicated follow-up 41.4°'s
   flip received** (exp-092's own Rank-1 net-widening design was partly
   motivated by 41.4°'s flip) — is 38.4° similarly close to an underlying
   `delta_scene` zero-crossing at `cpl=30` that a coarser `cpl=20` grid
   simply missed, the same story R13/R14 already tell for this channel
   elsewhere?
3. R15's own two founding discharge conditions are now BOTH touched this
   cycle (the three-point `cpl=30` census closes one; the `cpl=40` check
   opens, rather than closes, the other) — a future cycle should decide
   whether R15 itself needs a new addendum given its own founding
   instrument now shows the cross-resolution instability was even sharper
   than the rule anticipated (a full-window sign reversal, not a
   near-boundary single-point wobble).
4. The unbiased margin-vs-distance rebuild on the full 31-point window
   (exp-090's own Rank-2-in-queue item, carried as open since exp-090,
   Idealization 8) remains open, still not run.

*(This section is provisional — Phase 5's own six blind reviews and Red
Team's final audit may substantially revise this ranking; the Director's
own closing synthesis, not this draft, is authoritative.)*
