# PHASE 1 — PROPOSAL · Panel Iteration 85 (candidate exp-108)
## Lead seat: PHOTONICS (rotation lead)
## "The Two-Cycle-Old Reclassification Fix, R25/R23 Governance Rulings, and a Bundled `angular_scattered_pattern`/Absolute-Floor/Suite-Stage Batch"

### 0. What kind of cycle this is

**Instrument-extension / governance cycle, matching exp-101/102/103/104/
105/106/107's own unbroken precedent since exp-069.** No σ(I)/σ(x,t)/
angular-selectivity/sub-threshold mechanism is proposed, built, or varied
anywhere in this document. **T1 escape route: N/A**, throughout, for the
same reason it has been N/A on every T28 desk/instrument cycle since
Iteration 46: nothing here is a candidate mechanism for the phenomenon
program, and no constraint-1/2/3/4 verdict is scored, touched, or claimed
to move.

This cycle executes `experiments/107-.../phase5_redteam_audit.md` §6 —
the literal Reconciled Iteration-85 queue, read verbatim, not from any
paraphrase (verified against the source file myself; the queue's own
text is quoted in §2 below wherever it matters). Per the task brief and
Red Team's own §6 ranking, this document schedules **all three Tier-0
governance items as mandatory** and, from Tier 1's four items, schedules
**all four** — justified in §5 by a bundling argument specific to this
cycle's own physics, not by default optimism: three of the four Tier-1
items share the identical three new field captures (empty, hollow-article,
PEC-cored-article, at each of r=156/312) that the fourth item (the
`angular_scattered_pattern` primary spend) already pays for, so scheduling
them costs zero marginal `Sim.run()` calls, and the remaining item is
code-only. All Tier-2/Tier-3 items are explicitly deferred (§5), matching
this program's own R17 discipline (a deferral must state its reason, not
merely recur).

### 1. Narrative (≤300 words)

Three things are owed to this program by name, and none of them is a new
physics claim. First: exp-106's own `run.py` still does not implement
mandatory-fix-1's own reclassification rule — `p_abs_frac_diff` exceeds
~10% at both measured r (12.31%/17.96%), and the rule's own text says
that should read THREE-WAY AMBIGUOUS, not a REFUTE nominal. Two full
cycles (83→84) have passed with the fix disclosed only in prose. R25 exists
to stop this happening a third time; I do not let it. Second: R25 itself
and the standing R23 scope question both need an actual ruling, not
another deferral — I make both rulings in this document, with reasons,
subject to Phase 2 override.

The substantive science this cycle can afford is a single, disciplined
optical-response question, squarely inside my own charter: does the
already-established, already-quiet aggregate finding — hollow-vs-PEC-cored
`abs_ext_ratio` differs by only ~2–3×10⁻⁵ at r=156/312, the same order T9
found at r=78 — hold up when the SAME two constructions are compared
*angularly*, not just in their box-integrated total? A bulk instrument
(`radial_absorbed_power`/`widths()`) cannot see a shape difference that
sums to near-zero; `lab/sections.py::angular_scattered_pattern`, built and
gated at exp-059/060 but never once applied to this family, can. I predict
the null generalizes — that a near-Babinet, largely-opaque graded shell's
angular scattering pattern is set by its outer profile, not by what fills
its interior — but I do not pre-load the answer: the test is genuinely
two-sided, floor-gated (R13) before any classification, and cross-checked
against a second, independently-sized box (R15) before a REFUTE is
trusted. Three more small, genuinely zero/near-zero-marginal-cost items
ride along on the same captures.

### 2. Parameter tables

#### 2a. Tier 0 — governance, zero FDTD, mandatory, in the order Red Team's
own queue lists them

**Item 1 — the `run.py` reclassification code fix.**

Verified myself, directly against the source, not from any summary
(R4/R18 discipline): `experiments/106-t28-kappa-window-floor-fixedabs-
control/run.py`'s classification assignment runs from **line 753**
(`sr_fa = p4_fa["shape_ratio"]`) **through line 765** (the `print(...)` that
reports it) — I re-read this block character-by-character before writing
this table; it is NOT lines "754–765" as one secondary source states it
(off by one at the top edge only; the substance is identical either way).
The block currently reads `sr_fa` against `SHAPE_RATIO_FIXEDABS_CONFIRM=
8.0`/`SHAPE_RATIO_FIXEDABS_REFUTE=14.8` (module constants, line 112–113),
wraps the result in `NOISE-DOMINATED-UNRELIABLE(...)` if
`p4_fa["noise_flag"]["noise_dominated"]`, then wraps it again in
`(NOT-TRUSTED -- r=312 MARGINAL/unsettled)` if
`not shape_ratio_fixedabs_trusted`. **`p_abs_frac_diff_156`/
`p_abs_frac_diff_312` (computed at lines 593 and 672, printed at lines
595–596 and 674–675) are never read inside this block, or anywhere else
in the file** (`grep -n "p_abs_frac_diff" run.py` returns exactly those
four lines — two definitions, two print statements, zero uses in
`classification`'s own construction) — independently reconfirming
exp-107's own audit finding (§0.2 of `phase5_redteam_audit.md`) from the
source myself.

| Field | Current behavior (verified, lines 753–765) | Required behavior (mandatory fix 1's own text, `experiments/106-.../phase2_redteam_audit.md` §3.1) |
|---|---|---|
| Trigger | none | `p_abs_frac_diff_156 > 0.10` **or** (`p_abs_frac_diff_312 is not None and p_abs_frac_diff_312 > 0.10`) |
| Consequence | — | prepend `"THREE-WAY-AMBIGUOUS ("` … `" nominally per shape_ratio_fixedabs bands)"` around whatever `CONFIRMS-`/`REFUTES-`/`AMBIGUOUS` string the existing `sr_fa` comparison already produced, BEFORE the noise-dominated and NOT-TRUSTED wraps (both of which must still apply on top, unchanged) |
| Threshold constant | hard-coded `0.10` inline in a print f-string (line 596/675) | promote to a named module constant, `P_ABS_FRAC_DIFF_TRIGGER = 0.10`, used identically at both the print sites and the new classification check (R4: one number, one name) |

**Exact patch, specified precisely enough to apply without further
interpretation (Phase 3's job, not this document's — I do not edit
`experiments/106-.../run.py` myself; per this program's own "flag, don't
silently rewrite" convention for a document already closed by its own
Combined Verdict, the source fix lands as a new, disclosed, git-tracked
change, and exp-106's own historical `results.json`/`NOTES.md` are
annotated, not overwritten):**

```python
# inserted immediately after line 759 ("classification = 'AMBIGUOUS'"),
# before the existing noise_flag wrap at line 760-761
P_ABS_FRAC_DIFF_TRIGGER = 0.10  # promoted from the inline 0.10 literal at lines 596/675
divergences = [p_abs_frac_diff_156]
if p_abs_frac_diff_312 is not None:
    divergences.append(p_abs_frac_diff_312)
if any(d > P_ABS_FRAC_DIFF_TRIGGER for d in divergences):
    classification = (f"THREE-WAY-AMBIGUOUS ({classification} nominally "
                       f"per shape_ratio_fixedabs bands; p_abs_frac_diff="
                       f"{p_abs_frac_diff_156:.4f}(r156)"
                       + (f"/{p_abs_frac_diff_312:.4f}(r312)" if p_abs_frac_diff_312 is not None else "")
                       + f" exceeds {P_ABS_FRAC_DIFF_TRIGGER:.2f})")
```

This is **pure post-processing of already-persisted, already-measured
scalars** — `p_abs_frac_diff_156=0.1231`, `p_abs_frac_diff_312=0.1796`,
`shape_ratio_fixedabs=18.2283` are all already committed in exp-106's own
`results.json`. Applying the fix requires **zero new `Sim.run()` calls**:
a standalone `reclassify_106.py` (living in this cycle's own directory,
importing the corrected function from the patched `run.py`) reads
exp-106's committed `results.json`, re-derives `classification` under the
corrected logic, and reports it — exactly the `finalize.py` idiom
exp-107 itself established for zero-FDTD post-processing of a prior
cycle's own committed pickles.

**Item 2 — ratify or reject R25.**

Read directly, not summarized: LOGBOOK.md's own RULED OUT registry entry
for R25 already states, in its own founding sentence, that it is *"a
standing house-discipline rule, **proposed and ratified** by Red Team's
own Phase-5 final audit, Iteration 84"* (LOGBOOK.md, R25 entry, first
line). R25 is **already ratified** — this Tier-0 queue line, like exp-106's
own R24 line one cycle earlier, is a **bookkeeping confirmation, not a
live decision**, and I rule it exactly that way, for the identical reason
VISION's own Phase-1 proposal ruled the analogous R24 line at exp-107
(`phase1_proposal.md`, exp-107, §Idealizations: *"R24 was already ratified
by the Director at Iteration 83's own close... this cycle has no live
ratify-or-reject action to take on it"*). I note this parallel explicitly
because it is the second consecutive cycle this exact "the queue names an
already-closed ratification as if it were open" shape has occurred — worth
a standing note (not a new rule; two data points, not three), named in
§7.

**Item 3 — force the standing R23 scope decision (three consecutive
cycles, 82→83→84, unresolved).**

Read directly against R23's own operative text (LOGBOOK RULED OUT
registry) and against exp-104's own founding implementation
(`experiments/104-.../run.py`): R23 mandates a code-level assert on a
single `DISCLAIMER` source-of-truth string, checked against
`build_predictions_text()`/`build_result_text()`'s own generated output.
**Ruling (this document's own call, subject to Phase 2 override — this is
a governance question no single seat owns unilaterally, and I say so, the
same disclaimer VISION attached to its own R23-adjacent finding at
exp-107):**

**RATIFY R23 as intentionally scoped to the code-generated
`PREDICTIONS_TEXT`/`RESULT_TEXT` pipeline — do NOT genericize.** Reasons:
(a) every one of the three non-firing R23 gap instances on record
(exp-104's own founding scope gap; exp-105's missing `PREDICTIONS_TEXT`
assert, closed by exp-106's own mandatory fix 5; exp-107's
zero-`DISCLAIMER`-code cycle) was independently caught
non-load-bearing because constraint-3 is **independently, redundantly**
checked every cycle by two OTHER mechanisms that do not depend on R23 at
all — Phase-2 Red Team's own "no constraint-#N-violation found" scan, and
a Phase-5 seat's own direct code-read/grep (caught the exp-104 founding
gap via PHOTONICS/MATERIALS/THERMODYNAMICS; the exp-107 zero-`DISCLAIMER`-
code gap via VISION's own self-review, independently re-confirmed by Red
Team's own grep, §0.6 of `phase5_redteam_audit.md`) — a real,
already-functioning belt-and-suspenders that a fourth,
generic-code layer would duplicate at real engineering cost for
diminishing marginal safety; (b) genericizing to "a table-driven check
covering every document family" requires inventing a taxonomy of
"document family" this program has never needed before (hand-written
NOTES.md tables vs. code-generated text vs. this cycle's own governance
prose) and gates every future zero-FDTD governance cycle behind new
machinery, a cost asymmetric to the risk it retires. **This cycle's own
Tier-1 batch (§2b) DOES produce new scored classifications (the
`angular_scattered_pattern` CONFIRM/REFUTE call, §4), so it DOES invoke
the pipeline** — `run.py` for this cycle reuses exp-104–106's own
`DISCLAIMER`/`build_predictions_text()`/`build_result_text()` idiom
verbatim, keeping this cycle itself R23-clean by construction and
demonstrating the pipeline is used exactly when it is supposed to be.
**No forward-elevating clause is added to R23's own text** — this ruling
closes the three-cycle-old open question with a decision, not a
recurrence, matching R23's own "does not fire on its own founding
instance" precedent one level up (a scope-clarification is not itself a
new gap).

#### 2b. Tier 1 — the bundled real-FDTD batch (item numbering follows Red
Team's own §6 Tier-1 list in exp-107's audit)

| Knob | Value | Source / formula |
|---|---|---|
| Family, construction | fixed-absolute-thickness (`geom_fixedabs(r)`, exp-106's own `run.py`, `ABS_THICKNESS=48` cells fixed, `SIGMA_MAX_FIXED=0.5` fixed) — re-derived locally in this cycle's own `run.py`, byte-for-byte, gated against exp-106's own committed `geom_156_fixedabs`/`geom_312_fixedabs` (Gate P0, exp-107's own idiom, reused verbatim) BEFORE any `Sim.run()` call | `experiments/106-.../run.py::geom_fixedabs()` |
| r | 156, 312 | matches exp-106/107's own r-family points; r=78 excluded (below, §6) |
| Article A ("hollow") | `materials.graded_black_shell(sim, CX, CY, R_CORE, R_COAT, sigma_max)` only — interior vacuum | exp-107's own construction, this cycle's own reused reference leg |
| Article B ("PEC-cored", the PRIMARY article) | `materials.pec_disk(sim, CX, CY, R_CORE)` **then** `materials.graded_black_shell(...)` — identical to exp-106's own `_run(with_article=True, ...)` | `experiments/106-.../run.py::_run()` |
| Scenes per r | empty, hollow-article, PEC-cored-article = **3** | new this cycle — exp-107 only ever captured (empty, hollow); the PEC-cored capture is new |
| New `Sim.run()` calls | **6** (3 scenes × 2 r) | up from exp-107's own 4 (which never captured PEC-cored fields) |
| Execution method | `chunk_runner.py`-style checkpoint/resume (`CHUNK_STEPS=2200`, foreground Bash calls only) — exp-107's own precedent, empirically bit-exact-validated (§0.4 of exp-107's own audit) | `experiments/107-.../chunk_runner.py` |
| Ledger box (item i, `angular_scattered_pattern` primary + `widths()` reproduction gate) | `box_a` = `(CX∓(R_COAT+round(32·k)), CY∓(R_COAT+round(32·k)))` | exp-106's own `geom()`/`geom_fixedabs()`, `BOX_A_MARGIN0=32` |
| Ledger box (item i, cross-check) | `box_b`, `BOX_B_MARGIN0=57`, same formula | exp-106's own `geom()` |
| `ref` (incident-intensity strip) | `(CX, CY, round(60·k))` | exp-106's own `geom()`, `REF_HH0=60` |
| Absolute-floor box family (item ii) | 6 margins beyond `R_COAT`: **{24, 32, 40, 48, 57, 65} × k cells** (32/57 reused from `box_a`/`box_b`; 24/40/48/65 new, interpolating/extending) — all independently verified in-domain at both r before freezing (r=312's widest box, margin=65 → `hw=572` cells, reaches x∈[436,1580] inside `N=2240`'s valid `[40,2200]` interior, `ABSORB=40`, well clear of both boundaries — recomputed directly, not hand-typed, per R4) | this proposal's own extension of exp-106/028's `box_a`/`box_b` convention (T11/T9's own 80-cycle-old "only ever two boxes" caveat) |
| `angular_scattered_pattern` bins | `n_bins=48` (function default, unchanged — first-ever reuse of this exact default outside exp-059/060) | `lab/sections.py::angular_scattered_pattern` |
| Item iii box (numerator floor-gate, PEC-cored primary) | `g["behind"]` (the SAME window `kappa_window`'s own `window_stats()`/`floor_gate_window()` measure, NOT `box_a`/`box_b`) | `experiments/106-.../run.py::geom()`, `behind=(CX+R_COAT+27, CX+R_COAT+127, CY-20, CY+20)` |
| `FLOOR_FRAC` (item iii) | 0.10, unchanged | exp-106's own established convention |
| Cost gate | pilot r=156 (3 calls) first; commit r=312 (3 calls) only if the r=156 pilot's own empty-scene call is `<90 min` **and** the projected 3-call r=312 total is `<180 min` — **the identical gate, verbatim, exp-106's own `r312_primary_committed` rule already used** (`experiments/106-.../run.py`, `r312_primary_committed = (wall_312_empty_pilot/60.0)<90.0 and projected_primary_min<180.0`), reused rather than re-invented | exp-105/106/107's own established pilot-and-abort precedent |
| Estimated cost | r=156: ≈18–25 min (3 calls, extrapolated from exp-107's own ≈6 min/call at r=156); r=312: ≈140–165 min (3 calls, chunked, extrapolated from exp-107's own ≈49 min/call at r=312) — **total ≈160–190 min (2.7–3.2h)**, an extrapolation from a stated scaling assumption (per-call cost roughly constant within a fixed r, not re-derived from first principles), disclosed as such, bounded by the pilot-and-abort gate above, not treated as precise (R4) | derived from exp-107's own disclosed 109.3 min / 4-call combined wall time, apportioned 2 r=156 calls / 2 r=312 calls |
| Suite-stage addition (item iv) | new `stage26_chunked_run_identity()` in `lab/validation/run_all.py`; `_STAGE_IDS` extended from `range(1,26)` to `range(1,27)` | this proposal — see §5 |

### 3. T1 escape-route statement

**N/A**, matching every T28 desk/instrument cycle since Iteration 46 and
every rotation-lead cycle since exp-101. Nothing in this document builds,
varies, or claims any σ(I)/σ(x,t)/angular-selectivity/sub-threshold
mechanism; no constraint-1/2/3/4 verdict is scored or moved by any branch
of this cycle. This is confirmed structurally, not merely asserted:
neither the Tier-0 code fix, the R25/R23 rulings, nor the Tier-1
`angular_scattered_pattern`/floor-characterization/suite-stage batch
touches perceptual scoring, `C_thr(L)`, or `lab/ambient.py` anywhere.

### 4. Predictions — falsifiable, numeric, gated in order

**Tier 0, item 1 (deterministic — a reproducibility gate on the patch's
own correctness, not a physical-uncertainty forecast):**

| Check | Predicted | Falsified if |
|---|---|---|
| Classification string, r=156/312 (single family-wide `shape_ratio_fixedabs`, both r's `p_abs_frac_diff` feed the same check) | contains the literal substring `"THREE-WAY-AMBIGUOUS"` | does not contain it, despite `p_abs_frac_diff_156=0.1231>0.10` and `p_abs_frac_diff_312=0.1796>0.10` both being true |
| Every other persisted field (`shape_ratio_fixedabs=18.2283`, `abs_ratio(156)=1.0852`, `abs_ratio(312)=1.8797`, `p3`'s own numbers, `noise_flag` values) | bit-identical to exp-106's own committed `results.json` | any value changes at all (would mean the patch touched more than the classification string — a bug, not the intended fix) |

**Tier 1, item i (`angular_scattered_pattern`, PRIMARY, genuine physical
uncertainty — this program's first application of this instrument to a
shell geometry at r≠78):**

Reproduction precondition (must PASS before the angular comparison is
trusted at all): the fresh PEC-cored capture's `sections.widths()`-derived
`sigma_abs`/`sigma_ext`/`abs_ext_ratio` at `box_a` must reproduce exp-106's
own committed `ledger_r156["fixedabs"]`/`ledger_r312["fixedabs"]` values to
`<1e-6` relative — falsified (→ HALT before any angular claim) by any
larger deviation, which would mean this cycle's re-derived geometry or
construction has silently diverged from exp-106's own.

| Quantity | r | Predicted band | Falsified if |
|---|---|---|---|
| `max_bin \|Δpattern(θ)\|` (`Δpattern = σ_scat_per_bin[PEC-cored] − σ_scat_per_bin[hollow]`, `box_a`) relative to `max_bin(σ_scat_per_bin[PEC-cored])` | 156, 312 | **CONFIRM (null generalizes to the angular domain)** if every one of the 48 bins that clears the absolute floor (item ii, this same cycle) shows relative deviation `≤0.05` (5%) | **REFUTE (a genuine angular signature exists)** if any contiguous run of ≥3 bins (≥22.5° of arc) clears BOTH the item-ii absolute floor AND a `≥0.15` (15%) relative-deviation bar, AND the same feature (same angular location, same sign) reproduces at `box_b` (this suite's own established box-independence discipline, stage 8, `≤0.12` convention — extended here to the angular channel for the first time; a single-box angular excursion is not trusted as physics without an independent-box confirmation) |
| `sum(pattern) == sigma_scat` self-consistency (per `angular_scattered_pattern`'s own docstring) | both r, both articles, both boxes | agrees with `widths()`'s own `sigma_scat` to `<1e-9` relative (an implementation identity, not a physical test) | any larger deviation — halts the angular reading, not merely a caveat, since the docstring states this must be checked before the pattern is trusted for shape comparisons at all |

**Tier 1, item ii (absolute box-ledger noise floor — six-box family,
extends `box_dev`'s own established n=2 comparison):**

| Quantity | r | Predicted band | Falsified if |
|---|---|---|---|
| `std` of `Δ(abs_ext_ratio) = abs_ext_ratio[hollow] − abs_ext_ratio[PEC-cored]` across the 6-box family | 156 | `≤0.5×\|Δ_boxA\|` = `≤1.48×10⁻⁵` (the box-placement floor is genuinely tighter than the already-measured signal — the T9-style comparison is meaningful) | `≥\|Δ_boxA\|` = `≥2.97×10⁻⁵` (box-placement sensitivity is comparable to or larger than the signal itself — the `≤2×10⁻⁵`/`≤2×10⁻⁴` bands inherited from T9's own two-anchor spread do not reflect this channel's real floor at these ratios, and Iteration-85's own Tier-2 item 1 — re-deriving that band — is thereby answered as a byproduct, not deferred) |
| same | 312 | `≤0.5×\|Δ_boxA\|` = `≤1.23×10⁻⁵` | `≥\|Δ_boxA\|` = `≥2.47×10⁻⁵` |

**Tier 1, item iii (numerator floor-gate, PEC-cored PRIMARY article —
closing exp-107's own hollow-only substitution):**

| r | Predicted | Falsified if |
|---|---|---|
| 156 | `frac_unresolved` on the PEC-cored article's `g["behind"]` window lands within **±0.05** of exp-107's own hollow-article reading (0.18275) — i.e. `[0.133, 0.233]` — construction difference (hollow vs. PEC-cored interior) does not materially change the numerator's own noise-floor contamination | `frac_unresolved` falls outside `[0.133, 0.233]` — would mean the hollow-substitute measurement exp-107 filed is not representative of the PEC-cored primary article `kappa_window`'s own shape_ratio was actually scored from, a genuinely new, more consequential finding |
| 312 | within **±0.05** of exp-107's own hollow reading (0.2675) — `[0.218, 0.318]` | outside that band |

**Tier 1, item iv (chunked-vs-continuous suite-stage identity gate, code
only, zero marginal FDTD beyond a cheap canonical bench scene):**

| Check | Predicted | Falsified if |
|---|---|---|
| Positive control: chunked path (3× ~300-step chunks) vs. single-shot continuous `Sim.run()`, identical canonical bench scene (reusing stage 8's own `Sim(360,240,...)` construction, ~900 steps, cheap) | `max\|diff\|=0.0` on every field (`ez_a`,`hx_a`,`hy_a`,`ez_b`,`hx_b`,`hy_b`, extracted phasor) — matching exp-107's own r=156 A/B finding exactly, now at a suite-permanent, always-run scale | any nonzero deviation |
| Negative control (R18 discipline — a check joining an already-verified architecture needs its own fault-injection control the same cycle it is added): a corrupted checkpoint (`steps_done` off by one chunk) fed to the resume path | produces a field reading that deviates from the true continuous result by `>1%` relative (demonstrating the check is a genuine discriminator, not a tautology that would pass even a broken resume) | the corrupted-checkpoint path reproduces the true result anyway (would mean this gate cannot actually catch the defect class it exists to catch) |

### 5. Bundled items and the case for scheduling all four Tier-1 items

**The bundling, stated precisely.** Item i needs three fresh field
captures per r (empty, hollow, PEC-cored) to compute
`angular_scattered_pattern`. Once those captures exist:

- **Item ii** is `sections.widths()` called with 6 different `box` tuples
  on the SAME already-captured empty/hollow/PEC-cored phasor fields — zero
  additional `Sim.run()` calls, pure post-processing.
- **Item iii** is `floor_gate_window()` called on the SAME PEC-cored
  article's `ez` field, over `g["behind"]` instead of `box_a`/`box_b` —
  zero additional `Sim.run()` calls, a different box on data already in
  memory.
- **Item iv** shares no data dependency with items i–iii at all; it is a
  small, independent addition to `lab/validation/run_all.py`, run once,
  reused by every future cycle's own `--only` invocation — its cost is
  engineering time, not FDTD wall-clock, and does not compete with the
  cost gate on items i–iii.

So the entire Tier-1 batch costs **one** FDTD commitment (6 calls,
cost-gated exactly like exp-105/106/107's own pilot-and-abort precedent)
plus one small, independent code addition — not four separate spends.
This is why all four are scheduled rather than a subset: deferring items
ii/iii specifically would forgo genuinely free information already paid
for by item i's own captures, the opposite of this program's own
established discipline (e.g. exp-107's own item-4-folded-into-item-1
precedent, exp-094's own Rank-3-before-Rank-1 sequencing).

**Explicitly deferred, with reasons (not silently dropped):**

- **Tier 2, item 1** (re-derive Item 1's own `≤2×10⁻⁵` confirms band) —
  **partially discharged as a byproduct of Tier-1 item ii** (§4); not
  formally re-derived as its own standing band this cycle, left for
  Iteration 86 to adopt or refine once this cycle's own 6-box spread is
  on file and reviewed.
- **Tier 2, item 2** (restore `Q_ext`-invariance/`closure` narration into
  exp-106's Result prose) — a pure documentation task on a document this
  cycle does not otherwise touch; deferred, not blocking, no FDTD
  competition either way.
- **Tier 2, item 3** (reframe Item 4's "worsens with r" claim) — needs a
  third r-point on the numerator channel specifically (QUANTUM's own
  named caution) to move past a two-point read; this cycle's own item iii
  adds a same-r cross-check (hollow vs. PEC-cored), not a new r-point, so
  it does not discharge this item — deferred to whichever future cycle
  budgets a genuine third-r-point leg.
- **Tier 2, item 4** (decide whether the constraint-3-immunity claim needs
  its own reopening condition) — a VISION-charter question (perceptual
  scope), not mine to rule on unilaterally; deferred explicitly to
  whichever cycle next rotates to VISION SCIENCE or MATERIALS.
- **Tier 3** (oblique-angle extension, near-null-exclusion refinement, a
  fourth r-point, a different bridge geometry, the 750/450nm leg, the
  `G40` full-width leg, the x-wall admittance refit, `PAD`-with-article
  survival) — all standing, all older than this cycle's own Tier-0/1
  commitments, all genuinely competing for a future cycle's FDTD budget;
  none is bundleable at zero marginal cost with this cycle's own captures,
  and this cycle's own disclosed ≈160–190 min budget is already fully
  committed. None is newly created or newly deferred by this document —
  all were already open before this cycle began.

### 6. Idealizations

- 2D TMz, λ=600nm only — unchanged program-wide scope, all four Tier-1
  items.
- θ=0° (normal incidence) only — the oblique-angle extension (standing
  Tier 3 item) remains untested; `angular_scattered_pattern`'s own
  angle-around-the-box convention is unrelated to source incidence angle
  and does not itself require an oblique sweep to be meaningful at normal
  incidence.
- r=78 excluded from this cycle's own Tier-1 batch: exp-106's own ledger
  already covers r=78 (bit-exact, `core_frac=0` by PEC construction), and
  neither `angular_scattered_pattern` nor the 6-box floor family adds new
  information there that the shell's own smaller size (fewer resolvable
  bins per unit arc) would not simply degrade — a genuine idealization,
  not silently assumed.
- The absolute-floor box family (item ii) is itself a NEW convention,
  first used this cycle — its own 6 margins are chosen to interpolate/
  extend the already-validated `box_a`/`box_b` pair, not independently
  re-derived from a resolution or aliasing bound; a future cycle
  formalizing this into a standing convention (as Tier 3's own T11
  thread has asked for across 80+ cycles) should re-derive the margin
  choices from first principles, not merely reuse this cycle's own
  illustrative six.
- `angular_scattered_pattern`'s own docstring idealization is unchanged
  and applies here unmodified: this is a square-path angular sample, not
  a true circular far-field pattern, consistent with `sigma_scat`'s own
  near-to-mid-field box convention (`VALIDATION.md`), not a new
  approximation this cycle introduces.
- The Tier-0 code fix (item 1) changes a classification STRING only; it
  does not re-run, re-score, or re-interpret any other exp-106/107
  finding, and does not touch `p3_trusted`/`shape_ratio_fixedabs_trusted`
  or any other gate.
- No witness-scale extrapolation is attempted or claimed anywhere in this
  document.
- `DISCLAIMER` text (exp-104–106's own standing perceptual/expressibility
  disclaimer, R23 pattern) applies unchanged to this cycle's own Tier-1
  `run.py`, reused verbatim: raw physical intensity/angular-pattern ratios
  and an absorbed-power sanity ledger only — no Weber-contrast or
  `C_thr(L)` perceptual scoring is performed by any item in this document.
- `lab/` diff: the ONLY intended diff to `lab/` itself is the new
  `stage26_chunked_run_identity()` addition to `lab/validation/run_all.py`
  (item iv) — disclosed explicitly, not incidental; every other item
  touches only `experiments/106-.../run.py` (the Tier-0 patch) and this
  cycle's own new experiment directory.

### 7. What would falsify this cycle's own framing, and what Red Team
should look for

- **If the Tier-0 patch changes any field other than the classification
  string** (§4), that is a defect in the patch's own scope, not a physics
  finding — Red Team should diff exp-106's own `results.json` before and
  after byte-for-byte, not merely re-read the printed classification.
- **If my own reading of R25's "already ratified" status (§2a item 2) is
  wrong** — i.e., if LOGBOOK's own R25 entry does NOT in fact carry
  ratification language, or if a later edit changed it — Red Team should
  re-grep LOGBOOK.md directly rather than trust this document's own
  quotation, exactly the discipline exp-107's own audit applied to
  exp-106's queue text.
- **If my own R23 scope ruling (§2a item 3) is judged wrong** — this is a
  governance call I am not uniquely positioned to make (my own charter is
  optical response, not house discipline), and I say so explicitly here;
  Red Team should weigh it on its own stated reasons, not defer to
  "PHOTONICS proposed it."
- **If the `angular_scattered_pattern` reproduction precondition fails**
  (fresh PEC-cored capture does not reproduce exp-106's own committed
  ledger to `<1e-6`), the entire Tier-1 batch HALTS before any angular
  claim is made — Red Team should confirm this precondition is checked
  BEFORE the angular comparison, not treated as a post-hoc caveat if it
  fails.
- **If the cost gate does not fire correctly** (e.g. the r=156 pilot
  under-estimates r=312's true cost by more than the stated scaling
  assumption's own honest uncertainty), the pilot-and-abort structure is
  the safety net, reused verbatim from exp-106 rather than re-invented —
  Red Team should confirm it is wired to trigger BEFORE the r=312 leg
  commits, not only checked after the fact.
- **If a REFUTE is filed on the angular pattern (item i) without the
  `box_b` independent-box confirmation** (§4's own box-independence
  requirement), that REFUTE should not be trusted as physics — Red Team
  should check this explicitly; the broader family of "a single-instrument
  reading is not trusted without an independent cross-check before a
  boundary/classification is scored" is exactly the discipline R13/R15's
  own lineage exists to enforce, applied here to a genuinely new channel
  (box choice) rather than either of their own original ones (a
  zero-crossing-capable denominator; cross-resolution).
- **If any Tier-1 item's "zero marginal cost" bundling claim does not
  survive contact with the actual code** (e.g. `angular_scattered_pattern`
  turns out to need a capture format item ii/iii cannot also use), that
  would repeat exactly the "zero marginal cost" mischaracterization Red
  Team's own Attack 8 caught in exp-106's own mandatory fix 1 — Red Team
  should verify this at Phase 2, before any FDTD call, not discover it at
  Phase 4.
