# exp-097 — R18 Tier 0 Gate-Closure: Positional Check 6, Check-5 R3/R5 Extension, Check 7 (Taper), Documentation Bundle

*Panel Iteration 74. Lead seat (rotation): MATERIALS & METAMATERIALS.
Director synthesis of `phase1_proposal.md` (MATERIALS) after five blind
Phase-2 critiques (PHOTONICS, ELECTROMAGNETISM, THERMODYNAMICS, QUANTUM
OPTICS, VISION SCIENCE — unanimous support-with-changes) and Red Team's
Phase-2 audit (PROCEED-WITH-MANDATORY-FIXES, 6 items, zero overridden).
Executes exp-096's own Reconciled Iteration-74 queue, Tier 0 in full.
Tier 1 (real FDTD spend) stays explicitly out of scope this cycle.*

## Hypothesis

exp-096's own Phase-5 audit found its six-check registration-readback
gate CLEAN but narrower in scope than three governing texts claimed on
four axes, adopting R18 (a check's claimed coverage must be confirmed
against its actual code, and any check joining an already-fault-
injection-verified architecture must earn its own control in the cycle
it joins). This cycle's hypothesis: R18's own Tier-0 discipline, applied
retroactively to exp-096's own gate, closes those four gaps (plus a
fifth — the amplitude-taper channel, unchecked by anything) without
discovering a genuine registration DEFECT in the underlying,
already-validated construction code (`Sim`, `add_line_source`,
`design_geometry.py`'s `r{3,4,5}_config()`). A defect surfacing in this
cycle's own extended checks would mean either a genuine, previously
undetected `design_geometry.py` bug (sitting unfound since `R3`/`R5`
were built, exp-069/exp-095) or a defect in this cycle's own Phase-1
desk arithmetic — both real, falsifiable, non-circular outcomes.

## Changes from Phase 1, per Red Team's 6-item mandatory-fix docket (all ADOPTED, zero overridden)

Director's ruling: Red Team's Phase-2 audit independently re-verified
all five blind critiques from source (not on their word) and found one
further defect of its own (item 5/6 below, the most load-bearing of the
docket — a Check-6 sub-check that is a tautology by construction). All
six items are ADOPTED as written; none is overridden. Reasoning for
adopting Red Team's own item 5/6 in full rather than the milder
"disclose as an idealization" alternative it also offered: this cycle's
entire purpose is closing R18-class "claimed coverage exceeds actual
coverage" gaps in its own founding gate; shipping a fix for that class
of gap which itself has the identical defect shape, one cycle after R18
was adopted, would be a direct self-refutation this program's own
verify-before-claim culture cannot let stand uncorrected the same
shift it was caught.

1. **`y_hi`/`BASE_NY` mis-citation (EM + THERMODYNAMICS, independently
   convergent; Red Team extended: appears in BOTH §0 and §2b of the
   Phase-1 text, not only §2b).** Corrected below (§Setup, item 3): the
   desk pre-check's own prose now cites the true comparison target,
   `R{3,5}_CONFIGS["C40_R{3,5}"]["y_hi"]` = 2316/3860, never
   `R{n}_BASE_NY` (2376/3960 — a different quantity, the domain height,
   offset from `y_hi` by `y_lo`). Non-load-bearing to the executable
   `assert` (which always compared against the correct field), but the
   false "bit-exact" prose is corrected here, in this frozen document,
   so it is never carried forward uncorrected — the exact discipline R4
   exists to enforce.
2. **Standing-items ledger line silently dropped (PHOTONICS).** Restored
   verbatim below (§What this cycle does NOT do), updated to ten and
   twenty-two consecutive cycles respectively.
3. **Check 5's new `R3`/`R5` legs shipped without their own
   fault-injection control (QUANTUM OPTICS).** FI-G is extended to both
   new legs (§Setup, item 3) — not merely disclosed as a gap.
4. **§6 governance ruling had no attached verification mechanism (VISION
   SCIENCE).** This document's own Result section (once written, Phase 4)
   is required to carry the carried-idealizations banner, and Phase 5's
   synthesis must explicitly confirm it by name — stated as a same-cycle
   commitment below (§Predictions' own closing line) rather than left
   implicit.
5/6. **Check 6's `cpl_intended` sub-check is a family-level tautology,
   keyed by the same untrusted `pt["family"]` field on both sides — it
   cannot catch a family-mislabeling transcription slip, the exact fault
   class exp-096's own FI-A already treats as a live threat and the
   single most plausible real-world instance of the coverage gap R18
   exists to police (Red Team, independently found; the most
   load-bearing item in the docket).** Fixed below (§Setup, item 1+2):
   the NOTES.md ground truth is re-keyed by `notes_line` (independent of
   `pt["family"]`) via a new `NOTES_MD_FROZEN_FAMILY_BY_LINE` map; a
   `family_ok` sub-check is added; a new fault-injection scenario, FI-H
   (a genuine family mislabel, distinct from FI-F's global-constant
   corruption), proves the fixed check now catches what the un-re-keyed
   design could not. Added to the predicted-outcomes table.

## Setup

Same construction machinery as exp-096 (imported by reference, never
edited — `experiments/096-t28-r4-registration-readback-gate/run.py`'s
`REPRESENTATIVE`, `PAIR_KEYS`, `CONFIGS`, `TAPER`, `CPL`,
`construct_sim`, `phase_expected`, `NOTES_MD_FROZEN_LINE_VALUES` reused
verbatim). Four items, each with its own fault-injection scenario, per
R18:

**Item 1+2 — Check 6, positional and `cpl_intended`-complete, `family`
independently keyed.**

```python
NOTES_MD_FROZEN_FAMILY_BY_LINE = {437: "R4", 445: "R4", 476: "R5",
                                   495: "R4", 511: "R3"}
NOTES_MD_FROZEN_CPL_BY_FAMILY = {"R3": (30, 304), "R4": (40, 291), "R5": (50, 265)}

def check6_positional_and_cpl(pt):
    line = pt["notes_line"]
    theta_frozen = NOTES_MD_FROZEN_LINE_VALUES[line][pt["pair_index"]]
    family_frozen = NOTES_MD_FROZEN_FAMILY_BY_LINE[line]
    cpl_frozen, _ = NOTES_MD_FROZEN_CPL_BY_FAMILY[family_frozen]
    theta_ok = abs(pt["theta"] - theta_frozen) < 1e-9
    family_ok = (pt["family"] == family_frozen)
    cpl_ok = (CPL[pt["family"]] == cpl_frozen)
    return dict(theta_ok=theta_ok, family_ok=family_ok, cpl_ok=cpl_ok,
                clean=bool(theta_ok and family_ok and cpl_ok))
```

`family_ok` is the fix: `family_frozen` is looked up by `notes_line`
alone, never by `pt["family"]` — a genuinely independent ground truth,
unlike `cpl_ok` alone (which stays family-keyed on both sides but is now
gated behind `family_ok` having already confirmed the family label
itself is trustworthy). The old set-membership function is kept, renamed
`check6_set_membership_OLD`, run side by side on every fault-injection
scenario (R12's own old-vs-new idiom).

Fault-injection: **FI-E** (line-437 index swap, `RANK1A_ANGLES_SWAPPED
=(39.4,39.2)`, zero new `Sim` constructions); **FI-F** (`CPL["R4"]`
corrupted to 30, zero new constructions); **FI-H, new** (representative
point 6 — the true `R3`/38.4°/line-511 point — scored with `family`
overridden to `"R4"`; `family_ok` must read False where the un-re-keyed
design reads True; zero new constructions).

**Item 3 — Check 5, negative control extended to `R3`/`R5`.**
Hand-arithmetic (native `cpl=20` constants `(300, 40, 1584)` × literal
`ratio`, outside `design_geometry.py`, mirroring the existing `R4`
precedent bit-for-bit): `R3` (ratio=1.5) gives `src_x=450, y_lo=60,
y_hi=2316`; `R5` (ratio=2.5) gives `src_x=750, y_lo=100, y_hi=3860`.
Independently confirmed this session directly against
`R3_CONFIGS["C40_R3"]`/`R5_CONFIGS["C40_R5"]`'s own stored fields (the
correct comparison target — not `R3_BASE_NY`/`R5_BASE_NY`, which are the
domain-height constants 2376/3960, a different quantity offset from
`y_hi` by `y_lo`; corrected per the docket item 1 above).

Fault-injection: **FI-G**, now three legs — `native_src_x=301` (not
300) scored against all three of `R3_CONFIGS["C40_R3"]`
(ratio=1.5→`451*1.5`≈ predicted mismatch), `R4_CONFIGS["C40_R4"]`
(ratio=2.0, `602≠600`, exp-096/097's original leg), and
`R5_CONFIGS["C40_R5"]` (ratio=2.5). All three legs zero new `Sim`
constructions (Check 5 remains pure arithmetic on constants, no `Sim()`
call in its own design).

**Item 4 — Check 7, amplitude-taper registration.** Reads
`sim.sources[-1]['profile']` against an independent hand-reproduction of
`lab/fdtd2d.py:160-164`'s raised-cosine window formula (`p=ones(n);
win=0.5*(1-cos(pi*arange(edge)/edge)); p[:edge]=win; p[-edge:]=win[::-1]`,
stored as `amplitude*p`), using the already-verified `edge=TAPER[family]`
value. Run against all 16 representative constructions, the positive
control, and FI-A/B/C (predicted CLEAN on all four — none corrupts
`edge` — a specificity demonstration).

Fault-injection: **FI-D** — the `R4`/39.2°/`C40_R4` point rebuilt with
`edge=TAPER["R3"]=60` where `TAPER["R4"]=80` is intended. One new `Sim`
construction. Predicted DEFECT-FOUND on Check 7 alone, CLEAN on Checks
1–6 (none reads `edge`) — the specificity result proving Check 7 covers
a genuinely orthogonal axis.

**Item 5 — documentation bundle**, applied throughout this document:
the FI-A/Check-4 overclaim corrected wherever restated; containment-
ratio triples (none appear in this cycle's own Result, carried forward
only as a citation) will be labeled `lower/upper1/upper2:` explicitly if
restated at Phase 4/5; the `design_geometry.py` citation path corrected
throughout (`experiments/069-t21-block-mini-period-match-power-up/`,
never a T28 `069-...` path); the carried-idealizations-banner governance
ruling below.

**Governance ruling (item 5d, Director ratifies MATERIALS' Phase-1
reading unchanged — no Phase-2 seat challenged the textual reading
itself, only its lack of an attached verification step, fixed by this
document's own closing commitment below).** LOGBOOK.md's Iteration-65
CHECKPOINT text, independently re-confirmed: *"the 'carried
idealizations' banner is now required at BOTH the Predictions section
AND the Result section."* This document places the banner at both.
Phase 5's synthesis is required to grep this document's own Result
section by name and report pass/fail on the banner's presence — the
verification step VISION found missing from Phase 1.

## T1 escape route

**N/A** — pure zero-FDTD instrument/code-verification work, matching
exp-095/exp-096 precedent exactly. No mechanism, material, or T1
position is proposed. Checkpoint criterion 2 is N/A for the identical
reason.

## Realizability bound

**N/A**, identical reason — `REALIZABILITY_MEMO.md` is not opened,
cited, or re-scored this cycle.

## Idealizations

**Carried forward (exp-096 `NOTES.md`), cited by original number:** 1
(2D TMz, 600nm only), 7 (no constraint-1/2/3/4 test, no T1 position), 17
(`R3`/`R4`/`R5` share one mechanical `r{n}_config()` recipe), 38 (this
cycle's extended gate still does not prove the shared recipe's complete
internal arithmetic defect-free beyond the specific spot-checks run —
now three points, still not a census), 39 (Check 5, even extended,
remains independent of the module constants and the function call but
not of the formula itself).

**New this cycle (renumbered from Phase 1's 40–44 to absorb Red Team's
fix; 40 and 41 below now describe the FIXED design, not the flawed
Phase-1 draft):**

40. Check 6's `family_ok` sub-check is independently keyed by
    `notes_line` (not `pt["family"]`) and is the genuine fix for the
    tautology Red Team found in Phase 1's draft. `cpl_ok`, however, is
    STILL keyed by `pt["family"]` on both sides after `family_ok` has
    passed — this is now safe (a wrong `family` is caught by `family_ok`
    first, and `cpl_ok`'s own family-level comparison is only meaningful
    once `family_ok` is confirmed true), but it means `cpl_ok` alone,
    read in isolation from `family_ok`, is still not an independent
    per-point check — division of labor stated explicitly so a future
    document does not claim `cpl_ok` alone closes what only the pair
    closes together.
41. Check 6's `cpl_intended` half (both sub-checks together) verifies
    the per-family constant against NOTES.md's own frozen per-family
    declaration — it does NOT re-verify, a second independent way, that
    this same constant is what actually reaches
    `Sim(cells_per_lambda=...)` at construction time (Check 1's job,
    already covered). Complementary, not redundant.
42. Item 3's Check-5 extension to `R3`/`R5` remains independent of the
    module constants and the function call but not of the two-stage
    `round(native×RATIO)`-then-`+pad`-then-subtract FORMULA itself,
    necessarily authored by reading `r{n}_config()`'s own source — this
    cycle implements the Reconciled queue's own literal item-3 text
    (hand-written arithmetic mirroring the `R4` precedent), not Red
    Team's own stronger alternative ("a genuinely formula-independent
    recompute... a from-scratch physical-units derivation") offered in
    the same queue entry. A defect baked into the shared method itself
    would not be caught by any of the three spot-checked points.
43. Check 7 verifies construction-time registration of the `edge`
    parameter only — it does not evaluate whether the raised-cosine
    window is the physically correct choice of taper function at all
    (already exercised, and the "TAPER-as-sub-aperture" mechanism
    already REFUTED, at exp-070).
44. This cycle's fault-injection scenarios (FI-D/E/F/G/H) are, like
    exp-096's own FI-A/B/C, single-point discriminator-validation
    exercises, not an exhaustive census across every family/config/axis
    combination. FI-D is tested only at `R4`/`C40_R4`; FI-H only at the
    one `R3`/line-511 point. A registration defect isolated to a
    combination none of FI-D/E/F/G/H exercises would not be caught by
    this cycle.
45. This cycle re-derives Checks 1–4's own FI triad (positive control,
    FI-A, FI-B, FI-C) as a bit-exact reproduction of exp-096's own
    already-filed results, not as a new design — R18 already discharged
    those four checks at exp-096 itself; this cycle's own R18 compliance
    duty is scoped to Checks 5, 6, and 7, the three checks that joined
    this gate's architecture without their own control.

**Carried idealizations banner: every prediction below is governed by
Idealizations 1/7/17/38/39 plus this cycle's own 40–45.**

## Predictions (frozen, committed BEFORE any Phase-4 script runs)

**Carried idealizations banner: every prediction below is governed by
Idealizations 1/7/17/38/39 plus this cycle's own 40–45 (restated per
§6's own governance ruling — Predictions AND Result both carry it).**

Confident lean stated for every row — a correctness requirement of each
check's own design, not a genuine physical uncertainty (matching
exp-096's own framing). The representative-set rows are also confidently
predicted CLEAN: `construct_sim`, `design_geometry.py`, and
`add_line_source` are byte-for-byte unchanged since exp-096 already
confirmed Checks 1–4 CLEAN on these identical 16 objects — this cycle
changes only the CHECKING logic, never the construction code.

| Check | Representative (16 pts) | Positive control | FI-A | FI-B | FI-C | FI-D | FI-E | FI-F | FI-G | FI-H |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 (resolution) | CLEAN | CLEAN | **DEFECT-FOUND** | CLEAN | CLEAN | CLEAN | n/a | n/a | n/a | n/a |
| 2 (angle-spec) | CLEAN | CLEAN | CLEAN | **DEFECT-FOUND** | **DEFECT-FOUND** | CLEAN | n/a | n/a | n/a | n/a |
| 3 (placement) | CLEAN | CLEAN | CLEAN | CLEAN | CLEAN | CLEAN | n/a | n/a | n/a | n/a |
| 4 (phase-ramp) | CLEAN | CLEAN | CLEAN (spurious agreement, R18's own §1 finding) | **DEFECT-FOUND** | **DEFECT-FOUND** | CLEAN | n/a | n/a | n/a | n/a |
| 5 (recipe spot-check, R3+R4+R5) | CLEAN, 3/3 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | **DEFECT-FOUND, all 3 legs** | n/a |
| 6-old (set-membership, retained) | CLEAN, 8/8 | n/a | n/a | n/a | n/a | n/a | CLEAN (**misses** — the gap item 1 closes) | n/a | n/a | CLEAN (**misses** — the gap item 5/6 closes) |
| 6-new (positional+cpl+family) | CLEAN, 8/8 | n/a | n/a | n/a | n/a | n/a | **DEFECT-FOUND** (`theta_ok`) | **DEFECT-FOUND** (`cpl_ok`) | n/a | **DEFECT-FOUND** (`family_ok`) |
| 7 (taper) | CLEAN, 16/16 | CLEAN | CLEAN (specificity) | CLEAN (specificity) | CLEAN (specificity) | **DEFECT-FOUND** | n/a | n/a | n/a | n/a |

**Composite registration-gate outcome, confident lean:** CLEAN across
all seven checks and every fault-injection scenario resolving exactly
as tabled — extending, not reversing, exp-096's own CLEAN finding, under
strictly more discriminating machinery.

**Predicted total `Sim.__init__` construction count:** 16 (representative
set) + 4 (positive control, FI-A, FI-B, FI-C) + 1 (FI-D) = **21**.
FI-E/F/G/H add zero `Sim` constructions (Checks 5 and 6 are pure
Python/arithmetic checks with no `Sim()` call in their own design).
**0 FDTD calls** — every one of the 21 constructions stops before
`sim.run()`.

## Estimated FDTD call count and wall-time budget

**0 FDTD calls.** Estimated wall time under 60 seconds (Python/NumPy
object construction and array comparison only), matching exp-096's own
estimate and this sub-thread's established zero-FDTD-cycle band.

## What this cycle does NOT do

Per the Reconciled Iteration-74 queue's own Tier 0/Tier 1 split: Tier 1
items 6–9 (bracketing the other three established `cpl=20` nulls at
`cpl=40`, ~24 calls; the re-centered node-bracketing re-run at
θ₀≈38.590°, ~8–16 calls; pre-wiring `netd_row()`/`cell_metrics_r{3,4,5}`
sidecar extraction per R16; the deferred `cpl=50`/`R5` interior sweep)
are explicitly NOT run this cycle, sequenced after Tier 0 so that any
Tier-0 finding does not require retroactively auditing fresh FDTD spend
that leaned on the unextended gate.

**Standing, unranked, carried forward unchanged (restored per docket
item 2 — PHOTONICS, silently dropped from Phase 1's own draft):**
PHOTONICS' own grazing-incidence validity check (now TEN consecutive
cycles undischarged, Iterations 64–74); the x-wall wavelength-generality
leg (now TWENTY-TWO consecutive cycles deferred, 076–097); the unbiased
margin-vs-distance rebuild; the ritualization governance question
(Iteration 61).
