# exp-097 — R18 Tier 0 Gate-Closure: Positional Check 6, Check-5 R3/R5 Extension, Check 7 (Taper), Documentation Bundle

*Panel Iteration 74. Lead seat (rotation): MATERIALS & METAMATERIALS,
ROTATION LEAD this cycle. Phase 1 proposal only — no `run.py`, no FDTD
calls executed by this document. Executes exp-096's own Reconciled
Iteration-74 queue, Tier 0 in full (`experiments/096-t28-r4-registration-
readback-gate/NOTES.md` §Next; `phase5_redteam_audit.md` §6, items 1–5),
as ONE combined build — items 1+2 share one function per the queue's own
text ("bundle with item 1, same function"); items 3, 4, 5 are independent,
zero-cross-dependency additions. Tier 1 (items 6–9, resuming real FDTD
spend) is explicitly OUT OF SCOPE this cycle, sequenced after, per the
queue's own stated rationale: no Tier-0 finding should require
retroactively auditing fresh FDTD spend.*

## Standing-rule compliance header (checked against R1–R18)

- **R1–R3, R5–R14** — not engaged: no mechanism, carrier/phase fit,
  named-constant search, free-period fit, or physical-measurement ratio of
  any kind is computed anywhere in this cycle. This cycle reads Python/NumPy
  object attributes off freshly-constructed `Sim` objects and does desk
  arithmetic on already-committed module constants — nothing R13/R14
  (denominator-floor/numerator-cancellation) governs exists here.
- **R4/R9** (recompute-don't-hand-type; commensurability) — engaged
  directly: every constant cited below (`R3`/`R4`/`R5`'s own native-scaled
  values, `TAPER[family]`, the NOTES.md line citations) was retrieved this
  session by directly reading `experiments/069-t21-block-mini-period-
  match-power-up/design_geometry.py`, `experiments/096-.../run.py`,
  `experiments/095-.../NOTES.md`, and `lab/fdtd2d.py`, not hand-typed from
  LOGBOOK prose. The R3/R5 hand-arithmetic given in §3 below was
  independently spot-checked against `design_geometry.py`'s own comments
  this session (bit-exact) — disclosed as a Phase-1 desk pre-check, per R4
  NOT a substitute for the actual committed script's own recompute at
  Phase 4.
- **R15–R17** — not directly engaged: this cycle performs no cross-`cpl`
  physical measurement and sizes no new bracket/tolerance. `atol=1e-9` on
  Check 7's taper-array comparison is, like Check 4's existing `atol=1e-9`
  (exp-096 §2a), a floating-point-noise floor on two IEEE-754 evaluations
  of one closed-form formula, not an R17-governed physical bracket — flagged
  here to preempt the identical Phase-2 conflation exp-096 already
  preempted for Check 4.
- **R18** (adopted exp-096, Iteration 73) — this entire cycle IS R18's own
  discipline applied retroactively to its own founding gate: every item
  below either gives an already-shipped, control-free check (5, 6) its
  first fault-injection control, or ships a genuinely new check (7)
  together with its own control in the same cycle it joins — never
  inheriting the trust Checks 1–4's already-verified triad earned.

## 1. Mechanism/change narrative

Not a mechanism proposal — the fourth consecutive zero-FDTD
code-verification cycle in this sub-thread (exp-069 pattern; T1 route N/A,
matching exp-095/exp-096 precedent exactly). exp-096 built a six-check
registration-readback gate and found it CLEAN, but its own Phase-5 audit —
adopting R18, the rule this cycle now applies to R18's own founding
cycle — found Checks 5 and 6, the two checks shipped without a
fault-injection control, cover less than three governing texts claim:
Check 6 is set-membership, not positional, and never reads
`cpl_intended`; Check 5 restates rather than independently re-derives
`r{n}_config()`'s own formula, and covers only `R4`/`C40`; nothing checks
the amplitude-taper channel at all — a previously-refuted T28 mechanism
candidate (exp-070) whose registration value has never been audited. This
cycle closes all five reconciled Tier-0 items in one build: fix Check 6 to
positional, index-for-index comparison, adding its own `cpl_intended`
half; give Check 5 a negative control and extend its recompute to `R3`/
`R5`; add a seventh check independently reproducing the raised-cosine
taper formula against `sim.sources[-1]['profile']`; and a zero-cost
documentation-correction bundle, including a governance ruling on the
carried-idealizations-banner rule's own literal scope. Every new check or
fix ships with its own fault-injection scenario this same cycle, per R18's
own text. Tier 1 (real FDTD spend) stays out of scope, as stated above.

*(212 words.)*

## 2. Design and exact check logic (items 1–4)

All four items extend `experiments/096-t28-r4-registration-readback-gate/
run.py` by IMPORT (the `_load()` house pattern, mirroring exp-096's own
import of exp-095's `run.py`) — never by editing that file, matching this
program's established immutable-past-experiments discipline (exp-096
`run.py`'s own docstring, verbatim). `REPRESENTATIVE`, `PAIR_KEYS`,
`CONFIGS`, `TAPER`, `CPL`, `construct_sim`, `phase_expected`, and
`NOTES_MD_FROZEN_LINE_VALUES` are reused verbatim by reference. Because
this codebase does not persist raw object state across process boundaries
(the Director's own Iteration-72 finding, `experiments/095-.../NOTES.md`),
every `Sim` object this cycle inspects — including the 16 representative
constructions and the positive-control/FI-A/FI-B/FI-C fault-injection
constructions, all bit-exact reproductions of exp-096's own already-filed
results — is freshly rebuilt this cycle via the imported `construct_sim`,
never read back from exp-096's own completed run.

### 2a. Item 1 + Item 2 — Check 6, positional and `cpl_intended`-complete

**Exact check logic.** Add a `pair_index` field (0 or 1) to each
`REPRESENTATIVE` entry, recording which position within its NOTES.md line's
frozen value list that point occupies (already implicit in the existing
`notes_label` field — `"RANK1A[0]"`→`pair_index=0`, `"RANK1A[1]"`→
`pair_index=1`; singleton lines 495/511 get `pair_index=0` against a
one-element list). Add `NOTES_MD_FROZEN_CPL_BY_FAMILY = {"R3": (30, 304),
"R4": (40, 291), "R5": (50, 265)}` — the per-family `cpl` NOTES.md
independently states in prose at these lines (`experiments/095-.../
NOTES.md:304`: *"Rank 4 — 38.4° at corrected sigma, `R3`/`cpl=30` family"*;
`:291`: *"Rank 3 — `cpl=40` (`R4`) sigma-comparability"*; `:265`:
*"Rank 2 — `cpl=50` (`R5`) family"* — independently re-grepped this
session, not restated from the existing `NOTES_MD_FROZEN_LINE_VALUES`
comment block). New check body, replacing the set-membership `any(...)`:

```python
def check6_positional_and_cpl(pt):
    line = pt["notes_line"]
    theta_frozen = NOTES_MD_FROZEN_LINE_VALUES[line][pt["pair_index"]]
    cpl_frozen, cpl_line = NOTES_MD_FROZEN_CPL_BY_FAMILY[pt["family"]]
    theta_ok = abs(pt["theta"] - theta_frozen) < 1e-9
    cpl_ok = (CPL[pt["family"]] == cpl_frozen)
    return dict(theta_ok=theta_ok, cpl_ok=cpl_ok, clean=bool(theta_ok and cpl_ok))
```

The old set-membership function is KEPT, renamed
`check6_set_membership_OLD`, run side by side on every fault-injection
scenario below — the direct, executed old-vs-new comparison this program's
own R12 idiom (exp-086, old-buggy vs. corrected logic) established as the
strongest form of fault-injection demonstration.

**Fault-injection scenarios.**

- **FI-E (item 1, theta-positional axis).** A same-line index swap:
  construct a local `RANK1A_ANGLES_SWAPPED = (39.4, 39.2)` (the true
  `exp095.RANK1A_ANGLES` reversed) and re-score both of line 437's two
  points (`pair_index=0`→θ=39.4, `pair_index=1`→θ=39.2) against the
  UNCHANGED, correct `NOTES_MD_FROZEN_LINE_VALUES[437]=[39.2,39.4]` under
  both functions. Zero new `Sim` constructions (pure metadata comparison,
  matching FI-B's own zero-construction precedent).
- **FI-F (item 2, `cpl_intended` axis).** A family/`cpl` job-constant
  misread: score an `R4`-family representative point (any of the five)
  with `CPL["R4"]` corrupted to read `30` (`R3`'s own value) instead of
  `40`, against the unchanged `NOTES_MD_FROZEN_CPL_BY_FAMILY["R4"]=(40,
  291)`. Zero new `Sim` constructions.

### 2b. Item 3 — Check 5, negative control + `R3`/`R5` extension

**Exact independent-recompute formula (mirrors exp-096's own `R4`
recompute exactly, per the Reconciled queue's own literal text —
hand-written arithmetic outside `design_geometry.py`, not a call to
`r3_config()`/`r5_config()`; RATIO values hand-typed as literals, not read
off `dg.R3_RATIO`/`dg.R5_RATIO`, matching Check 5's own existing `R4`
precedent for `ratio=2.0`):**

```python
native_src_x, native_absorb, native_ny = 300, 40, 1584   # unchanged, cpl=20 base
for family, ratio, target in [("R3", 1.5, dg.R3_CONFIGS["C40_R3"]),
                               ("R5", 2.5, dg.R5_CONFIGS["C40_R5"])]:
    src_x = round(native_src_x * ratio) + 0     # pad=0 for C40
    absorb = round(native_absorb * ratio)
    ny = round(native_ny * ratio) + 0
    y_lo = absorb + 0
    y_hi = ny - y_lo
    assert (src_x, y_lo, y_hi) == (target["src_x"], target["y_lo"], target["y_hi"])
```

**Phase-1 desk pre-check (R4 discipline: disclosed, to be reproduced by
the committed script, not treated as proven here):** `R3` (ratio=1.5):
`src_x=450, y_lo=60, y_hi=2316` — matches `design_geometry.py`'s own
`R3_BASE_SRC_X`/`R3_BASE_ABSORB`/`R3_BASE_NY` comments (450/60/2376) bit-
exact. `R5` (ratio=2.5): `src_x=750, y_lo=100, y_hi=3860` — matches
`R5_BASE_SRC_X`/`R5_BASE_ABSORB`/`R5_BASE_NY` comments (750/100/3960)
bit-exact.

**Fault-injection scenario, FI-G (negative control, item 3).** Deliberately
corrupt one native constant by the smallest plausible transcription error
— `native_src_x=301` (not 300) — in the existing `R4` recompute
(`ratio=2.0`): `src_x_wrong = round(301*2.0) = 602 ≠ 600` (`R4_CONFIGS
["C40_R4"]["src_x"]`). Zero new `Sim` constructions (Check 5, like its
extension, is pure arithmetic on constants — no `Sim()` call anywhere in
this check's own design, unchanged from exp-096).

### 2c. Item 4 — Check 7 (amplitude-taper registration)

**What it reads.** `sim.sources[-1]['profile']` — the stored amplitude-
taper array `add_line_source` builds from `edge` (`lab/fdtd2d.py:160-164`,
read directly this session): `p = np.ones(n); win =
0.5*(1-cos(pi*arange(edge)/edge)); p[:edge]=win; p[-edge:]=win[::-1]`,
stored as `amplitude * p` — an entirely separate array from `phase`
(Check 4's own target), built from a different input (`edge`, not
`angle_deg`).

**Exact independent-recompute formula (hand-reproduced outside
`lab/fdtd2d.py`, using the ALREADY-VERIFIED `edge=TAPER[family]` intended
value, matching Check 4's own "recompute using the verified upstream
value" pattern):**

```python
def taper_expected(n, edge, amplitude=1.0):
    p = np.ones(n)
    win = 0.5 * (1.0 - np.cos(np.pi * np.arange(edge) / edge))
    p[:edge] = win
    p[-edge:] = win[::-1]
    return amplitude * p

check7 = np.allclose(sim.sources[-1]["profile"],
                      taper_expected(cfg["y_hi"] - cfg["y_lo"], TAPER[family]),
                      atol=1e-9, rtol=0.0)
```

Run against all 16 representative constructions (both pair members, since
`n=y_hi-y_lo` differs between `C40`/`G40` under `pad`, exercising the same
`pad`-arithmetic risk Checks 3/4 already cover) plus the positive control
and FI-A/B/C (predicted CLEAN on all four — none corrupts `edge` — a
specificity demonstration, not merely a catch demonstration).

**Fault-injection scenario, FI-D (mandatory per the queue's own naming).**
A wrong/swapped `edge` value: construct the `R4`/39.2°/`C40_R4` point
(otherwise identical to representative point 1 and the positive control)
with `edge=TAPER["R3"]=60` where `TAPER["R4"]=80` is intended — `R3`'s own
taper width substituted for `R4`'s. One new `Sim` construction.
`sim.sources[-1]['profile']` is corrupted (window width 60, not 80);
`sim.lam`, `angle_deg`, `x`, `sl`, and `phase` are ALL untouched by `edge`,
so Checks 1–6 are predicted CLEAN on this same construction — the
specificity result that proves Check 7 covers a genuinely orthogonal axis,
not a redundant re-statement of Checks 1–4.

## 3. Parameter table

| Item | Check logic (exact) | Fault-injection scenario (exact injected value) | Independent-recompute source |
|---|---|---|---|
| 1 | `check6_positional_and_cpl`'s `theta_ok`: `pt["theta"] == NOTES_MD_FROZEN_LINE_VALUES[line][pair_index]` (index-for-index, not membership) | **FI-E**: `RANK1A_ANGLES_SWAPPED=(39.4,39.2)` scored at `pair_index∈{0,1}` against unchanged `[39.2,39.4]` | `experiments/095-.../NOTES.md:437` (unchanged ground truth) |
| 2 | `check6_positional_and_cpl`'s `cpl_ok`: `CPL[family] == NOTES_MD_FROZEN_CPL_BY_FAMILY[family][0]` | **FI-F**: `CPL["R4"]` corrupted to `30` (R3's value), scored against unchanged `(40, line 291)` | `experiments/095-.../NOTES.md:265/291/304` |
| 3 | `(src_x,y_lo,y_hi) == target` per family, native literals `(300,40,1584)` × hand-typed `ratio∈{1.5,2.5}` | **FI-G**: `native_src_x=301` (not 300), scored against `R4_CONFIGS["C40_R4"]` (ratio=2.0 unchanged) → `602≠600` | Hand arithmetic outside `design_geometry.py`; §2b desk pre-check bit-exact vs. `design_geometry.py`'s own `R3_BASE_*`/`R5_BASE_*` comments |
| 4 | `np.allclose(sim.sources[-1]['profile'], taper_expected(n, TAPER[family]), atol=1e-9, rtol=0.0)` | **FI-D**: `edge=TAPER["R3"]=60` substituted where `TAPER["R4"]=80` is intended, at `R4`/39.2°/`C40_R4` | `lab/fdtd2d.py:160-164` formula, hand-reproduced |
| 5a | *(no check — documentation only)* Correct the "Check 1, transitively Check 4" claim for FI-A everywhere this cycle's own document states it | — | R18's own §1 finding (`phase5_redteam_audit.md:44-64`) |
| 5b | *(documentation convention)* Any containment-ratio triple this cycle's own document cites is labeled `lower/upper1/upper2:` explicitly, not positional order alone | — | THERMODYNAMICS' Phase-5 finding (exp-096) |
| 5c | *(documentation correction)* `design_geometry.py` cited as living in `experiments/069-t21-block-mini-period-match-power-up/`, never a T28 `069-...` path | — | Directly confirmed this session (§0 required reading item 6) |
| 5d | *(governance ruling)* — see §6 below | — | LOGBOOK.md Iteration 65 (exp-088) record, verbatim |

## 4. T1 escape route

**N/A** — pure zero-FDTD instrument/code-verification work, matching every
T28 desk/instrument cycle since exp-069 and, specifically, exp-095's and
exp-096's own immediately-prior precedent. This cycle takes no position on
σ(I)/σ(x,t)/angular selectivity/sub-threshold operation, proposes no
material or mechanism, and does not touch `REALIZABILITY_MEMO.md`.
Checkpoint criterion 2 is N/A for the identical reason.

## Realizability bound

**N/A**, identical reason — `REALIZABILITY_MEMO.md` is not opened, cited,
or re-scored. (Noted per this seat's own charter, MATERIALS' realizability
duty, even though this cycle proposes no material.)

## 5. Per-check predicted outcomes (falsifiable)

**Confident lean stated for every row below — a correctness requirement of
each check's own design, not a genuine physical uncertainty (matching
exp-096's own §5b framing for its FI triad).** The representative-set rows
are ALSO confidently predicted CLEAN, not "no lean," because `construct_sim`,
`design_geometry.py`, and `add_line_source` are byte-for-byte unchanged
since exp-096 already confirmed Checks 1–4 CLEAN on these identical 16
objects — this cycle changes only the CHECKING logic, never the underlying
construction code, so a defect surfacing here would mean either this
proposal's own Phase-1 desk arithmetic (§2b) is wrong or a genuine
`design_geometry.py` defect has sat undetected since `R3`/`R5` were built
(exp-069/exp-095) — a real, falsifiable, non-circular prediction.

| Check | Representative set (16 pts, 3 families) | Positive control | FI-A | FI-B | FI-C | FI-D | FI-E | FI-F | FI-G |
|---|---|---|---|---|---|---|---|---|---|
| 1 (resolution) | CLEAN | CLEAN | **DEFECT-FOUND** | CLEAN | CLEAN | CLEAN | n/a | n/a | n/a |
| 2 (angle-spec) | CLEAN | CLEAN | CLEAN | **DEFECT-FOUND** | **DEFECT-FOUND** | CLEAN | n/a | n/a | n/a |
| 3 (placement) | CLEAN | CLEAN | CLEAN | CLEAN | CLEAN | CLEAN | n/a | n/a | n/a |
| 4 (phase-ramp) | CLEAN | CLEAN | CLEAN (spurious agreement — comparator built from already-corrupted `sim.lam`, per R18's own §1 finding) | **DEFECT-FOUND** | **DEFECT-FOUND** | CLEAN | n/a | n/a | n/a |
| 5 (recipe spot-check, `R3`+`R4`+`R5`) | CLEAN, 3/3 families | n/a | n/a | n/a | n/a | n/a | n/a | n/a | **DEFECT-FOUND** |
| 6-old (set-membership, retained for comparison) | CLEAN, 8/8 | n/a | n/a | n/a | n/a | n/a | CLEAN (**misses** — the exact gap this item closes) | n/a (old check never reads `cpl`) | n/a |
| 6-new (positional + `cpl_intended`) | CLEAN, 8/8, both axes | n/a | n/a | n/a | n/a | n/a | **DEFECT-FOUND** (both sub-points) | **DEFECT-FOUND** | n/a |
| 7 (taper) | CLEAN, 16/16 | CLEAN | CLEAN (specificity) | CLEAN (specificity) | CLEAN (specificity) | **DEFECT-FOUND** | n/a | n/a | n/a |

**Composite registration-gate outcome, confident lean:** CLEAN across all
seven checks and every fault-injection scenario resolving exactly as
tabled — extending, not reversing, exp-096's own CLEAN finding, now under
strictly more discriminating machinery (positional+`cpl`-complete Check 6,
`R3`/`R5`-extended Check 5, and a new, independently-verified Check 7).

**Predicted total `Sim.__init__` construction count (actual constructor
calls, per THERMODYNAMICS' Phase-5-corrected accounting basis, not
"distinct configurations"):** 16 (representative set, rebuilt fresh this
cycle since object state does not persist across process boundaries) + 4
(positive control, FI-A, FI-B, FI-C, likewise rebuilt fresh to also feed
Check 7) + 1 (FI-D, genuinely new) = **21**. FI-E/F/G add zero `Sim`
constructions (Check 6 and Check 5 are both pure Python/arithmetic checks
with no `Sim()` call anywhere in their own design, unchanged from
exp-096). **0 FDTD calls** — every one of the 21 constructions stops
before `sim.run()`, identical in kind to exp-096's own zero-FDTD guarantee.

## 6. Governance ruling (item 5d)

**The Iteration-65 CHECKPOINT rule's own literal text (LOGBOOK.md,
Iteration 65/exp-088 record, independently re-grepped and read this
session): "the 'carried idealizations' banner is now required at BOTH the
Predictions section AND the Result section of any future T28
committed-predictions document."** This is unambiguous — "Predictions +
Result," not "Idealizations + Predictions." exp-095 and exp-096 both
instead placed the banner at the Idealizations section (immediately before
Predictions) and at Predictions itself, never at Result — a genuine,
two-cycle-old drift from the ratified text, not an equally valid
alternative reading. exp-096's own Phase-5 (VISION) independently caught
the Result-section gap as real but it was not fixed same-shift. **Ruling:
the literal, ratified text governs. This cycle's own future NOTES.md (this
document's own eventual Phase-3 synthesis) places the banner at BOTH
Predictions AND Result, matching the rule as actually adopted — not the
Idealizations+Predictions pattern the two most recent cycles drifted into.**
Stated here, explicitly, before a third occurrence forces the question
under worse conditions, per the queue's own framing.

## 7. Idealizations

**Carried forward, cited by original number (exp-096 `NOTES.md`):** 1 (2D
TMz, 600nm only), 7 (no constraint-1/2/3/4 test, no T1 position), 17
(`R3`/`R4`/`R5` share one mechanical `r{n}_config()` recipe — directly
relevant to item 3's own extension), 38 (this cycle's extended gate still
does not prove the shared recipe's COMPLETE internal arithmetic
defect-free beyond the specific spot-checks run — now three points instead
of one, still not a census), 39 (Check 5, even extended to `R3`/`R5`,
remains independent of the module constants and the function call but not
of the FORMULA itself — see Idealization 41 below, which sharpens this for
the extension specifically).

**New this cycle:**

40. Check 6's new `cpl_intended` half verifies the per-family constant
    (`CPL[family]`) against NOTES.md's own frozen per-family declaration —
    it does NOT re-verify, a second independent way, that this same
    constant is what actually reaches `Sim(cells_per_lambda=...)` at
    construction time (that is Check 1's own job, already covered). The
    two checks are complementary, not redundant: Check 1 catches a
    caller-plumbing divergence between the job constant and the
    constructed object; the new Check 6 half catches a transcription
    divergence between the job constant and NOTES.md's own frozen prose.
    Stating this division of labor explicitly, per R18, rather than
    letting a future document claim doubled coverage that isn't there.
41. Item 3's Check-5 extension to `R3`/`R5` remains, like the original `R4`
    spot-check (MATERIALS' own Phase-5 finding, exp-096), independent of
    the module constants and the function call but NOT independent of the
    two-stage `round(native×RATIO)`-then-`+pad`-then-subtract FORMULA
    itself, which was necessarily authored by reading `r{n}_config()`'s
    own source — this cycle implements the Reconciled queue's own literal
    item-3 text (hand-written arithmetic mirroring the existing `R4`
    precedent), not Red Team's own stronger, alternative framing offered in
    the same queue entry ("a genuinely formula-independent recompute...
    e.g. a from-scratch physical-units derivation"). Disclosed as a
    scope choice: three spot-checked points now share one recompute
    METHOD, not three independently-derived ones. A defect baked into that
    shared method itself — as opposed to a per-family literal — would not
    be caught by any of the three.
42. Check 7 verifies CONSTRUCTION-TIME registration of the `edge`
    parameter only (does `sim.sources[-1]['profile']` match what
    `TAPER[family]` intends) — it does not evaluate whether the
    raised-cosine window is the physically correct choice of taper
    function at all (that modeling question was already exercised, and
    the resulting "TAPER-as-sub-aperture" mechanism already REFUTEd, at
    exp-070; out of scope here, matching Idealization 33's own division of
    labor for Checks 1–4).
43. This cycle's own fault-injection scenarios (FI-D/E/F/G) are, like
    exp-096's own FI-A/B/C, single-point discriminator-validation
    exercises — one family, one axis corrupted at a time — not an
    exhaustive census across every family/config/axis combination. FI-D is
    tested only at `R4`/`C40_R4`; a taper-registration defect isolated to
    `R3`/`R5` or to the `G` (padded) configs specifically would not be
    exercised by this single scenario, mirroring Idealization 39's own
    scope statement for Check 5's original `R4`-only spot-check.
44. This cycle re-derives Checks 1–4's own FI triad (positive control,
    FI-A, FI-B, FI-C) as a bit-exact REPRODUCTION of exp-096's own
    already-filed results, not as a new design — R18 already discharged
    those four checks at exp-096 itself; this cycle's own R18 compliance
    duty is scoped to Checks 5, 6, and 7 specifically, the three checks
    that joined this gate's architecture without their own control.

**Carried idealizations banner (per §6's own governance ruling — this
Phase-1 document is neither a Predictions nor a Result section, so the
banner is stated here once, for completeness, and will be placed at BOTH
Predictions and Result in this cycle's own eventual NOTES.md): every
prediction in §5 above is governed by Idealizations 1/7/17/38/39 plus this
cycle's own 40–44.**

## 8. Estimated FDTD call count and wall-time budget

**0 FDTD calls**, per §5's own construction-count derivation (21 `Sim`
constructions, every one stopping before `sim.run()`). Estimated wall
time: under 60 seconds total (Python/NumPy object construction and array
comparison only, plus a handful of already-established-constant lookups
for the documentation bundle), matching exp-096's own estimate and this
sub-thread's own established zero-FDTD-cycle band.

## 9. What this cycle does NOT do (explicit scope boundary)

Per the Reconciled Iteration-74 queue's own Tier 0/Tier 1 split: Tier 1
items 6–9 (bracketing the other three established `cpl=20` nulls at
`cpl=40`, ~24 calls; the re-centered node-bracketing re-run at θ₀≈38.590°,
~8–16 calls; pre-wiring `netd_row()`/`cell_metrics_r{3,4,5}` sidecar
extraction per R16; the deferred `cpl=50`/`R5` interior sweep) are
explicitly NOT run this cycle, sequenced after Tier 0 so that any Tier-0
finding (a genuine defect in Checks 5/6/7's own extended scope) does not
require retroactively auditing fresh FDTD spend that leaned on the
unextended gate. This document proposes exactly Tier 0 items 1–5, sized
and gated as the reconciled queue itself specifies.
