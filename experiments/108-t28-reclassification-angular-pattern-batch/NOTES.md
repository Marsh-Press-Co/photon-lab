# exp-108 — The Two-Cycle-Old Reclassification Fix, R25/R23 Governance
Rulings, and a Bundled `angular_scattered_pattern`/Absolute-Floor/Suite-
Stage Batch

**Panel Iteration 85. Lead seat (rotation): PHOTONICS. Director: Clyde
(photonlab-shift, cloud panel shift).** Executes exp-107's own Reconciled
Iteration-85 queue (`phase5_redteam_audit.md` §6 of exp-107): all three
Tier-0 governance items (R25's own load-bearing tripwire — a third cycle
unexecuted fires Checkpoint criterion 4 automatically) and all four Tier-1
items (a bundled `angular_scattered_pattern`/absolute-floor/suite-stage
batch), scheduled together because Tier 1's own machinery pays for itself
at zero marginal FDTD cost once its primary spend commits.

Full record: `phase1_proposal.md` (PHOTONICS), `phase2_critique_
{materials,em,thermodynamics,quantum,vision}.md` (five blind critiques,
all support-with-changes), `phase2_redteam_audit.md` (5 numbered attacks,
all five critiques ADOPTED in full — none overridden; EM's and QUANTUM's
own remedies combined into one unified fix rather than picked separately
— verdict PROCEED-WITH-MANDATORY-FIXES, 7 mandatory fixes).

## Hypothesis

**Tier 0 (governance, no FDTD).** Three items are owed to this program by
name: (1) exp-106's own `run.py` still does not implement mandatory-fix-1's
reclassification rule two full cycles (83→84) after it was disclosed in
prose — R25 exists to stop a third cycle unexecuted, and this cycle
executes it, not merely re-describes it. (2) R25 itself needs a ratify/
reject ruling — LOGBOOK's own text shows it is already ratified (Red
Team's Phase-5 final audit, Iteration 84), so this is bookkeeping. (3) The
three-cycle-stale R23 scope question (genericize the disclaimer assert, or
ratify it as intentionally single-scoped) needs an actual decision.
Hypothesis: all three close cleanly at zero FDTD cost, with the sole risk
being that (1) gets described rather than executed a third time — the
literal R25 failure mode — which this cycle guards against explicitly
(§Setup, Tier-0 item 1's binding execution requirement).

**Tier 1 (real FDTD, one bundled spend).** `lab/sections.py::
angular_scattered_pattern`, validated at exp-059/060 but never applied to
the fixed-abs hollow-vs-PEC-cored pair, is the correctly-targeted
instrument (PHOTONICS/MATERIALS, both exp-106 and exp-107 Phase 5) for
whether the near-zero *aggregate* `abs_ext_ratio` delta between hollow and
PEC-cored fixed-abs shells (T9's own "core is energetically incidental"
null, 2.97×10⁻⁵/2.47×10⁻⁵ at r=156/312) also holds *angularly* — a bulk
instrument cannot see a shape difference that sums to near-zero. Genuinely
two-sided hypothesis: I predict the null generalizes (an opaque, near-
Babinet graded shell's angular scattering pattern is set by its outer
profile, not its interior fill) but the test is real. Bundled at zero
marginal FDTD cost: an absolute box-ledger noise-floor characterization
(T11, 80+ cycles open), the numerator floor-gate check on the actual
PEC-cored PRIMARY article (closing exp-107's own hollow-substitute
disclosure), and promoting `chunk_runner.py`'s checkpoint/resume mechanism
to a named, suite-gated trust-suite stage.

## Phase 2 → Phase 3: synthesis of the debate

**Disposition of the five blind critiques (Red Team's own ruling, §2 of
`phase2_redteam_audit.md`): all five ADOPTED, unconditionally, none
overridden.** MATERIALS and THERMODYNAMICS' findings are pure corrections
(narrative citation fix; an unlooked-at thermal cross-check) with no
remedy conflict. VISION's finding is adopted with its own named remedy.
EM's and QUANTUM's findings are both adopted but their remedies are
**combined into one unified fix (Red Team's own §3, the deepest finding
of the audit)** rather than either being picked in isolation — Director
adopts this combination in full, below.

**[MATERIALS, ADOPTED] T9-anchor citation corrected.** The Phase-1
proposal's §1 narrative wrote "the same order T9 found at r=78" for the
hollow-vs-PEC-cored `abs_ext_ratio` delta. LOGBOOK's own Iteration-84
record (Red Team's Phase-5 final audit) already corrected this exact
comparison once: like-for-like against `exp-027`'s own box-ledger anchor
(`+1.56×10⁻⁶`) alone (not `exp-031`'s different-channel `6.8×10⁻⁶`), the
gap is **19.0× at r=156, 15.8× at r=312** — a real ~1.2-decade gap, not
"same order." This cycle's own §Setup/§Predictions below use the corrected
figures throughout; the regression is noted here as a live finding (a
one-cycle-old correction re-entering the record uncorrected), not silently
fixed.

**[THERMODYNAMICS, ADOPTED] Real absorbed-watts divergence, not merely
`sigma_abs`, checked.** The Phase-1 proposal declared T1/thermal N/A
"confirmed structurally" without checking whether the Tier-0 reclassify-
ing trigger (`p_abs_frac_diff`, a `sigma_abs`-based fractional divergence)
has any thermal-detectability reading. THERMODYNAMICS independently
propagated the real absorbed-power proxy (`p_abs_w ∝ σ_ext·σ_abs`, exp-
107's own `item3_rows` formula chain, not merely `sigma_abs`) for the
identical fixedabs-vs-selfsim split Tier-0 item 1 reclassifies: **real
absorbed-watts divergence is 30.9% (r=156) / 46.3% (r=312) — larger than
the 12.31%/17.96% `sigma_abs`-only figure**, since `p_abs_w` scales
quadratically in `sigma_ext`. Both remain UNDETECTABLE (minimum margin
across all four `item3_rows` cells, ≥117×, per exp-107's own committed
Result table) — **N/A holds**, but the proposal reached it by never
looking, an R8-shaped gap (an unverified robustness assumption standing in
for an affordable check). Recorded explicitly below (§Idealizations) so
Tier-0 item 1's own reclassification is not mistaken for a thermal
finding — it is a `sigma_abs`-based statistical divergence trigger, a
different quantity from the real absorbed-watts divergence, both large,
neither thermally detectable.

**[VISION, ADOPTED] The R23 "belt-and-suspenders" premise corrected; the
scope ruling itself stands.** The Phase-1 proposal's R23 ratify-as-scoped
ruling (§2a item 3) justified itself partly on two claimed independent
safety nets (a Phase-2 Red Team constraint scan, and a Phase-5 seat code-
read) having independently caught all three non-firing R23 gap instances
on record. VISION traced all three (exp-104's founding gap, exp-105's
missing assert, exp-107's zero-`DISCLAIMER`-code gap) and found **every
one came from the SAME mechanism — a voluntary Phase-5 seat code-read —
never from the Phase-2 scan**, which structurally cannot catch this class
of gap (it fires against a scored constraint claim; none of the three
cycles scored one). Red Team independently re-verified this from LOGBOOK
directly (`phase2_redteam_audit.md` §0.10, Attack 5) and confirms: this is
**one mechanism working 3/3, not two independent layers** — real, but
thinner redundancy than claimed. **This does NOT reverse the ratify-as-
scoped OUTCOME** (the proposal's premise (b) — genericizing invents an
undefined "document family" taxonomy at real engineering cost for
diminishing marginal safety — stands independently of premise (a)'s
overstated redundancy) — but the ruling's own stated justification is
corrected here, not merely caveated, and a **mandatory bound condition is
added**: Phase 4 must run a live-fire check (`run.py --predictions-only`,
`grep -in disclaimer` across this cycle's own `run.py`/`chunk_runner.py`/
`finalize.py`, reported by name in this document's own Result section)
before the R23 ruling is treated as closed — since this cycle's own
Tier-1 batch is the first to newly invoke the code-generated
`DISCLAIMER`/`build_predictions_text()`/`build_result_text()` pipeline in
three cycles, VISION's own repeated finding is precisely the failure mode
most likely to recur here if left unchecked.

**[EM + QUANTUM combined, ADOPTED as a unified fix — the deepest finding
of Red Team's audit, §3]** Both EM's and QUANTUM's attacks trace to one
root-cause error: this cycle's own Tier-1 falsification logic (as
originally drafted) treats **box radius as an exchangeable, iid nuisance
parameter** — legitimate for `sigma_ext`/`sigma_scat` (a scalar, Poynting-
conserved quantity, which is why stage 8's own `box_a`-vs-`box_b` `≤0.12`
convention is sound) but NOT legitimate for the two NEW quantities this
cycle builds: a per-bin angular reading (item i) and a between-family
difference-of-ratios (item ii), neither of which inherits that
conservation guarantee at a fixed pair of radii 2.5–5λ apart (EM,
independently re-derived: `box_a`/`box_b` separation is exactly 2.5λ at
r=156, 5λ at r=312). Item ii's own already-scheduled six-margin family
`{24,32,40,48,57,65}×k` — built for the floor characterization — is also
the exact ≥3-point convergence instrument EM's own flip condition asked
for, at zero additional cost (Red Team, §0.9, independently confirmed:
`widths()`/`angular_scattered_pattern()` both take `box` as a post-hoc
tuple over already-captured phasor fields). **Director adopts the unified
fix in full, replacing both items' original two-point/raw-std logic**
(§Predictions, below, supersedes the Phase-1 proposal's own tables for
items i/ii).

**[Attack 1, ADOPTED] The `run.py`-patch/`reclassify_106.py` specification
gap resolved by function extraction (Red Team's option (a), not (b)).**
The Phase-1 proposal's patch was literal inline code with no importable
function boundary — Director resolves this the R4-clean way: extract
`classify_shape_ratio_fixedabs(...)` as a standalone function in exp-106's
own `run.py`, called both by `run.py`'s own inline flow (replacing lines
753–765's tail) and imported directly by `reclassify_106.py` — one
function, one name, zero duplicated logic (§Setup, exact signature given).

**[Attack 2/3/6, ADOPTED] Middle-verdict bands, a precise negative-control
threshold, and the `closure` field are added** to the predictions tables
below (§Predictions) — all zero-cost documentation/logic completions, no
FDTD implication.

**[Attack 4, confirmed, non-firing] Constraint-3 structural check: clean.**
Red Team's own grep (`C_thr`, `ambient`, `Weber`, any perceptual-scoring
construction) across this cycle's full disclosed scope returns zero hits;
the only `lab/` diff is a pure FDTD-identity regression stage
(`stage26_chunked_run_identity`). **T1/constraint-3 is N/A throughout,
confirmed structurally, not merely accepted from the proposal's own
self-report.**

**R25's own status this cycle (Red Team's ruling, §4 of the audit,
adopted in full).** Tier-0 item 1, as specified below, is textually a
clean, distinct, non-parenthetical line item — the shape R25 exists to
require — and discharges the rule's founding instance **on paper**. Red
Team's own conditional stands and is adopted as a binding requirement,
not a caveat: **this cycle's own Result section (Phase 4) must state, with
the reclassified string quoted inline, that the patch was actually applied
and its output checked against §Predictions' own band — not merely
described as specified.** If a future audit finds this cycle's own
Tier-0 item 1 was only described and not executed, that is the literal
second R25 instance and fires Checkpoint criterion 4 automatically, per
R25's own forward-elevating clause.

## Setup

### Tier 0 — governance, zero FDTD, mandatory

**Item 1 — the `run.py` reclassification code fix (R25's own tripwire).**
Patches `experiments/106-t28-kappa-window-floor-fixedabs-control/run.py`.
Extracted function, inserted near the existing classification block
(replacing its lines 753–765 tail with a call to this function):

```python
P_ABS_FRAC_DIFF_TRIGGER = 0.10  # promoted from the inline 0.10 literal at lines 596/675

def classify_shape_ratio_fixedabs(sr_fa, noise_dominated, trusted,
                                   p_abs_frac_diff_156, p_abs_frac_diff_312=None):
    if sr_fa <= SHAPE_RATIO_FIXEDABS_CONFIRM:
        classification = "CONFIRMS-electrical-thickness-growth-hypothesis"
    elif sr_fa >= SHAPE_RATIO_FIXEDABS_REFUTE:
        classification = "REFUTES-electrical-thickness-growth-hypothesis"
    else:
        classification = "AMBIGUOUS"
    divergences = [p_abs_frac_diff_156]
    if p_abs_frac_diff_312 is not None:
        divergences.append(p_abs_frac_diff_312)
    if any(d > P_ABS_FRAC_DIFF_TRIGGER for d in divergences):
        classification = (f"THREE-WAY-AMBIGUOUS ({classification} nominally "
                           f"per shape_ratio_fixedabs bands; p_abs_frac_diff="
                           f"{p_abs_frac_diff_156:.4f}(r156)"
                           + (f"/{p_abs_frac_diff_312:.4f}(r312)" if p_abs_frac_diff_312 is not None else "")
                           + f" exceeds {P_ABS_FRAC_DIFF_TRIGGER:.2f})")
    if noise_dominated:
        classification = f"NOISE-DOMINATED-UNRELIABLE ({classification} nominally)"
    if not trusted:
        classification = f"{classification} (NOT-TRUSTED -- r=312 MARGINAL/unsettled)"
    return classification
```

`run.py`'s own inline call site becomes
`classification = classify_shape_ratio_fixedabs(sr_fa, p4_fa["noise_flag"]["noise_dominated"], shape_ratio_fixedabs_trusted, p_abs_frac_diff_156, p_abs_frac_diff_312)`.
`reclassify_106.py` (new, this cycle's own directory) imports this
function directly from the patched `run.py`, loads exp-106's own committed
`results.json`, re-derives `classification` under the corrected logic
using the four already-persisted scalars (`shape_ratio_fixedabs=18.2283`,
`p4_fa.noise_flag.noise_dominated`, `shape_ratio_fixedabs_trusted=False`,
`p_abs_frac_diff_156=0.1231`, `p_abs_frac_diff_312=0.1796`), and reports
it — zero new `Sim.run()` calls, matching `finalize.py`'s own zero-FDTD
post-processing idiom (exp-107).

**Item 2 — ratify R25.** Bookkeeping confirmation (LOGBOOK's own R25 entry
already states it was "proposed and ratified... Iteration 84") — no live
action.

**Item 3 — R23 scope decision: RATIFY as intentionally scoped to the
code-generated `PREDICTIONS_TEXT`/`RESULT_TEXT` pipeline; do NOT
genericize.** Corrected justification (per Phase 2→3 synthesis, above):
the belt-and-suspenders premise is one mechanism (voluntary Phase-5 code-
read), not two, 3/3 so far — real but thinner than originally claimed;
the ruling nonetheless stands on its independent cost argument (premise
(b): inventing a "document family" taxonomy this program has never needed,
gating every future zero-FDTD governance cycle behind new machinery, a
cost asymmetric to the risk it retires). **Bound condition (VISION's
mandatory ask, adopted): the live-fire check specified below must PASS
before this ruling is treated as closed on the record.**

### Tier 1 — the bundled FDTD batch

**Construction.** Fixed-absolute-thickness family (`geom_fixedabs(r)`,
`experiments/106-.../run.py`, re-derived locally byte-for-byte, gated
against exp-106's own committed `geom_156_fixedabs`/`geom_312_fixedabs`
before any `Sim.run()` call — HALT on any mismatch). r = 156, 312 (r=78
excluded: exp-106's own ledger already covers it, `core_frac=0` by PEC
construction, and neither instrument below adds new information at that
scale). Two articles per r: **hollow** (`materials.graded_black_shell`
only, exp-107's own reference construction) and **PEC-cored/PRIMARY**
(`materials.pec_disk` then `materials.graded_black_shell`, exp-106's own
`_run(with_article=True)` construction). **6 new `Sim.run()` calls**
total (empty + hollow-article + PEC-cored-article, at each of r=156/312;
the empty scene is shared between both articles at a given r, matching
exp-106's own established reuse discipline), each with
`capture_sigma_e=True` on both article calls (needed for `ledger_check`'s
`radial_absorbed_power`/`closure`/`core_frac` fields on both
constructions). Execution: `chunk_runner.py`-style checkpoint/resume
(`CHUNK_STEPS=2200`, foreground Bash calls only — this session's own
backgrounded/nohup execution is confirmed pathologically slow for
sustained FDTD numpy work, exp-107's own A/B-tested finding, reused
without re-testing). Cost gate, reused verbatim from exp-106's own
`r312_primary_committed` rule: pilot r=156 (3 calls) first; commit r=312
(3 calls) only if the r=156 pilot's own empty-scene wall time is `<90 min`
**and** the projected 3-call r=312 total is `<180 min`.

**Absolute-floor box family (item ii), reused for item i's own unified
fix (§Predictions):** 6 margins beyond `R_COAT`: `{24, 32, 40, 48, 57,
65}×k` cells (32/57 are the pre-existing `box_a`/`box_b`; 24/40/48/65 are
new, interpolating/extending). Domain clearance independently verified at
both r before freezing: r=312's widest box (margin=65) has `hw=572`
cells, spans `x∈[436,1580]`, inside `N=2240`'s valid `[40,2200]` interior
with `ABSORB=40` — recomputed directly from `geom()`'s own formula, not
hand-typed.

**`angular_scattered_pattern`:** `n_bins=48` (function default), called at
each of the 6 margins, on both hollow and PEC-cored captures, at both r —
`lab/sections.py::angular_scattered_pattern(cap_scene, cap_empty, box,
ref, n_bins=48)`, a pure post-hoc function over already-captured phasor
fields (verified, zero additional `Sim.run()` cost for any of the 6
margins).

**Item iii (numerator floor-gate, PEC-cored PRIMARY article):**
`floor_gate_window(ez_PECcored_article, *g["behind"], label)` at r=156/312
— closes exp-107's own disclosed hollow-substitute measurement, now run on
the actual PEC-cored primary article `kappa_window`'s own shape_ratio was
scored from.

**Item iv (suite-stage promotion, code only):** new
`stage26_chunked_run_identity()` in `lab/validation/run_all.py`
(`_STAGE_IDS` extended from `range(1,26)` to `range(1,27)` — verified the
current file tops out at stage 25, no stage 26 exists yet). Positive
control: chunked path (3× ~300-step chunks) vs. single-shot continuous
`Sim.run()` on a cheap canonical bench scene (reusing stage 8's own
`Sim(360,240,...)` construction, ~900 steps). Negative control (R18
discipline — a check joining an already-verified architecture needs its
own fault-injection control the same cycle it is added): a corrupted
checkpoint (`steps_done` off by one chunk) fed to the resume path, must
demonstrably fail to reproduce the true continuous result.

**R23 live-fire check (VISION's mandatory bound condition):** Phase 4
must run `python3 experiments/108-.../run.py --predictions-only` and
`grep -in disclaimer experiments/108-.../run.py
experiments/108-.../chunk_runner.py experiments/108-.../finalize.py`,
reporting both by name in this document's own Result section, before the
Tier-0 item 3 (R23 scope) ruling is treated as closed.

## Predictions — committed BEFORE any Phase 4 `Sim.run()` call

### Tier 0, item 1 (deterministic — a reproducibility gate on the patch's
own correctness, not a physical-uncertainty forecast)

| Check | Predicted | Falsified if |
|---|---|---|
| `reclassify_106.py`'s reported classification string, using exp-106's own committed `p_abs_frac_diff_156=0.1231`/`_312=0.1796` (both `>0.10`) | contains the literal substring `"THREE-WAY-AMBIGUOUS"` | does not contain it |
| Every other field `reclassify_106.py` reports (`shape_ratio_fixedabs=18.2283`, `noise_dominated`, `trusted=False`) | bit-identical to exp-106's own committed `results.json` | any value differs (the patch touched more than the classification string) |
| Live re-run of `run.py`'s own patched inline classification block (`run.py --predictions-only` or a full re-run) | reproduces `reclassify_106.py`'s own string exactly | diverges (the extracted function and the inline call site have drifted) |
| Execution requirement (binding, not a physical prediction, per R25's own conditional) | Phase 4's Result section states, with the string quoted inline, that the patch was applied and checked | Result section only describes/recommends the fix without confirming execution — this alone is a live R25 concern to flag, even if not immediately a second firing instance |

### Tier 1, item i (`angular_scattered_pattern`, unified multi-margin fix
— supersedes the Phase-1 proposal's own two-box table)

**Reproduction precondition (must PASS before ANY angular claim is
trusted):** the fresh PEC-cored capture's `sections.widths()`-derived
`sigma_abs`/`sigma_ext`/`abs_ext_ratio` at `box_a` (margin=32) must
reproduce exp-106's own committed `ledger_r156["fixedabs"]`/
`ledger_r312["fixedabs"]` values to `<1e-6` relative — falsified (→ HALT
before any angular claim) by any larger deviation.

**Implementation-identity check:** `sum(sigma_scat_per_bin) ==
sigma_scat` (from `widths()`, same box) to `<1e-9` relative, at every
margin, both articles, both r — an implementation self-consistency
identity per the function's own docstring, not a physical test; any
larger deviation halts the angular reading.

**Classification (3-way, per mandatory fix 6):**

| Verdict | Condition |
|---|---|
| **CONFIRM** (null generalizes to the angular domain) | at margin=32 (`box_a`), every one of the 48 bins that clears the item-ii absolute floor (below) shows `\|Δpattern(θ)\|/max_bin(σ_scat_per_bin[PEC-cored]) ≤ 0.05` (5%), **AND** this holds at all 6 margins, not just margin=32 |
| **REFUTE** (a genuine, radius-consistent angular signature exists) | a contiguous run of ≥3 bins (≥22.5° of arc) clears BOTH the item-ii floor and a `≥0.15` (15%) relative-deviation bar at margin=32, **AND** the same bin-run's own 6-point sequence across all margins is SMOOTH — either strictly monotonic in margin, or fits `Δ(margin) = A + B/margin` with `R²≥0.90` — consistent with genuine near-to-far-field lobe migration, not noise |
| **AMBIGUOUS** (everything else) | a candidate feature exists at margin=32 but its 6-point across-margin sequence is neither monotonic nor well-fit by the `A+B/margin` model (`R²<0.90`) — flagged NOISE-ARTIFACT, not trusted as physics, not confidently ruled a pure null either; **or** a feature clears the floor+15% bar at some margins but not margin=32 itself |

Falsified (in the sense of "this document's own classification logic is
broken," an R4 concern, not a physics finding) if any bin/margin
combination cannot be assigned to exactly one of the three named
branches.

### Tier 1, item ii (absolute box-ledger noise floor, six-margin family,
detrended per the unified fix)

For each r, at each of the 6 margins: `Δ(margin) = abs_ext_ratio[hollow]
(margin) − abs_ext_ratio[PEC-cored](margin)` (via `sections.widths()`).
Fit `Δ(margin) = A + B/margin` (linear regression in `1/margin`);
`residual_std` = std of the 6 fit residuals. `|Δ_boxA|` (margin=32,
already measured by exp-107 for this identical pair: `2.969×10⁻⁵` at
r=156, `2.468×10⁻⁵` at r=312) is the comparison anchor, reused not
re-derived.

| Verdict | r=156 condition | r=312 condition |
|---|---|---|
| **CONFIRM** (floor genuinely tighter than the signal) | `residual_std ≤ 1.48×10⁻⁵` (0.5×`\|Δ_boxA\|`) | `residual_std ≤ 1.23×10⁻⁵` |
| **AMBIGUOUS** | `1.48×10⁻⁵ < residual_std < 2.97×10⁻⁵` | `1.23×10⁻⁵ < residual_std < 2.47×10⁻⁵` |
| **REFUTE** (box-placement/near-field-trend content comparable to or exceeding the signal) | `residual_std ≥ 2.97×10⁻⁵` | `residual_std ≥ 2.47×10⁻⁵` |

A REFUTE here means the `≤2×10⁻⁵`/`≤2×10⁻⁴` bands T9's own two-anchor
spread established do not reflect this channel's real floor at these
ratios — Iteration-85's own Tier-2 item 1 (re-derive that band) is
thereby answered as a byproduct, using the DETRENDED number, not the raw
std the Phase-1 proposal originally proposed to lean on (Red Team's
Attack against the un-detrended statistic, §3).

### Tier 1, item iii (numerator floor-gate, PEC-cored PRIMARY article)

| r | Predicted | Falsified if |
|---|---|---|
| 156 | `frac_unresolved` lands within **±0.05** of exp-107's own hollow-article reading (0.18275) — i.e. `[0.133, 0.233]` | outside `[0.133, 0.233]` — would mean the hollow-substitute measurement is not representative of the primary article `kappa_window`'s shape_ratio was actually scored from |
| 312 | within **±0.05** of exp-107's own hollow reading (0.2675) — `[0.218, 0.318]` | outside `[0.218, 0.318]` |

### Tier 1, item iv (chunked-vs-continuous suite-stage identity gate)

| Check | Predicted | Falsified if |
|---|---|---|
| Positive control (chunked vs. continuous, canonical bench scene) | `max\|diff\|=0.0` on every field, matching exp-107's own r=156 A/B finding | any nonzero deviation |
| Negative control (corrupted checkpoint, off-by-one chunk) | field reading deviates from the true continuous result by `>1%` relative | deviates by `≤1%` relative (the check cannot discriminate the defect class it exists to catch) |

### `ledger_check`'s own `closure` field (mandatory fix 5, zero marginal
cost — already computed by `ledger_check`, newly surfaced in this table)

| Article | r | Predicted `closure` | Falsified if |
|---|---|---|---|
| hollow, PEC-cored | 156, 312 | `≤0.001` (0.1%) — established precedent range is 0.02–0.06% (exp-106's own record, PLAN.md Current-state), this band is deliberately looser (R17: bracket sized against the largest already-established value on file) | `>0.01` (1%) |

## Idealizations

- 2D TMz, λ=600nm only — unchanged program-wide scope, all four Tier-1
  items.
- θ=0° (normal incidence) only — the oblique-angle extension remains
  untested; `angular_scattered_pattern`'s own angle-around-the-box
  convention is unrelated to source incidence angle.
- r=78 excluded from this cycle's own Tier-1 batch — already covered by
  exp-106's own ledger (bit-exact, `core_frac=0` by PEC construction).
- The absolute-floor box family (item ii) is a NEW convention, first used
  this cycle — its 6 margins interpolate/extend the already-validated
  `box_a`/`box_b` pair, not independently re-derived from a resolution or
  aliasing bound; a future cycle formalizing this into a standing
  convention should re-derive the margin choices from first principles
  (Tier 3, standing, per this document's own Idealizations discipline).
- `angular_scattered_pattern`'s own docstring idealization is unchanged:
  a square-path angular sample, not a true circular far-field pattern.
- The Tier-0 code fix (item 1) changes a classification STRING only; it
  does not re-run, re-score, or re-interpret any other exp-106/107
  finding, and does not touch `p3_trusted`/`shape_ratio_fixedabs_trusted`.
- **[THERMODYNAMICS, adopted] `p_abs_frac_diff` (the Tier-0 reclassifying
  trigger, `sigma_abs`-fractional-divergence based) is NOT the same
  quantity as the real absorbed-watts divergence between the two
  families.** Independently checked this cycle (§Synthesis, above): the
  real, physically-correct `p_abs_w ∝ σ_ext·σ_abs` proxy diverges more
  (30.9%/46.3% at r=156/312) than `p_abs_frac_diff` itself (12.31%/17.96%),
  but both stay UNDETECTABLE by a wide margin (≥117×, exp-107's own
  `item3_rows`) — thermal N/A is correct, checked, not merely asserted.
- No thermal sidecar is invoked FRESH this cycle (the check above reuses
  exp-107's own already-persisted `item3_rows`, zero new computation).
- `DISCLAIMER` text (exp-104–107's own standing perceptual/expressibility
  disclaimer, R23 pattern) applies unchanged to this cycle's own `run.py`:
  raw physical intensity/angular-pattern ratios and an absorbed-power
  sanity ledger only — no Weber-contrast or `C_thr(L)` perceptual scoring
  is performed by any item in this document. **Live-fire-verified, not
  merely asserted (§Result, Phase 4).**
- `lab/` diff: the ONLY intended diff to `lab/` itself is the new
  `stage26_chunked_run_identity()` addition to `lab/validation/run_all.py`
  (item iv). Every other item touches only
  `experiments/106-.../run.py` (the Tier-0 patch, a disclosed, git-tracked
  change to a document already closed by its own Combined Verdict —
  historical `results.json`/`NOTES.md` there are annotated, not
  overwritten) and this cycle's own new experiment directory.
- No witness-scale extrapolation is attempted or claimed anywhere in this
  document.

## T1 escape-route statement

**N/A**, matching every T28 desk/instrument cycle since Iteration 46.
Nothing in this document builds, varies, or claims any σ(I)/σ(x,t)/
angular-selectivity/sub-threshold mechanism; no constraint-1/2/3/4 verdict
is scored or moved by any branch of this cycle. Confirmed structurally
(Red Team's own grep, `phase2_redteam_audit.md` §0, Attack 4): zero
perceptual-scoring code path anywhere in this cycle's scope.
