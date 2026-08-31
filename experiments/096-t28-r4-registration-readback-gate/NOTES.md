# exp-096 — Angle-Domain Registration-Readback Gate (R3/R4/R5) + Zero-FDTD Bracket-Width Desk Bound

*Panel Iteration 73. Lead seat (rotation): PHOTONICS. Full phase record:
`phase1_proposal.md` (PHOTONICS) → five blind Phase-2 critiques (MATERIALS,
ELECTROMAGNETISM, THERMODYNAMICS, QUANTUM OPTICS, VISION SCIENCE, unanimous
support-with-changes) → `phase2_redteam_audit.md` (PROCEED-WITH-MANDATORY-
FIXES, 8 items, zero overridden) → this document (Phase 3 SYNTHESIS,
Director), all 8 fixes adopted plus one Director-level clarification found
while merging them. Executes Reconciled Iteration-73 queue items 1 and 2
(`experiments/095-.../NOTES.md` §Next).*

## Hypothesis

Nineteen cycles of the T28 sub-thread (exp-069 through exp-095) have never
once verified that the constructed `Sim` object's own `lam`
(cells-per-wavelength), injected `angle_deg`, source placement, and
resulting phase-ramp array actually match what each call site *intended* —
Gate 5 (adopted Iteration 71) checks only `sigma_e` magnitude. exp-095's own
Rank 1c FAIL (the established θ₀≈38.590° null did not reappear as a sign
change in the `R4` family within a ±0.1° bracket) is, per its own Phase-5
record, genuinely ambiguous between two candidates: registration/wiring
defect, or real resolution-dependent node migration. This cycle builds and
runs the one check that can remove the first candidate from consideration
(within the scope stated below) at zero FDTD cost, plus an independent
zero-FDTD desk bound on how wide a future node-bracketing re-run's window
needs to be. **Pure instrument recalibration — no phenomenon-mechanism
claim.** T1 route N/A, Checkpoint criterion 2 N/A, matching every T28
desk/instrument cycle since exp-069.

## Changes from Phase 1, per Red Team's 8-item mandatory-fix docket (all
## ADOPTED, zero overridden)

1. **C/G-pair congruence claim corrected.** Phase 1's §3 wrongly claimed
   `C40_R{n}`/`G40_R{n}` share identical `nx,ny,src_x,y_lo,y_hi` "by Gate
   3." Independently re-verified this Phase (`design_geometry.py`, all
   three families): only the aperture `A` (and `cpl`) is held identical —
   `nx`/`ny`/`src_x`/`y_lo`/`y_hi` all differ, by construction (`G` adds a
   nonzero domain-wall `pad`; `C` does not). The congruence is **Gate 2**
   (`A` equality), not Gate 3 (an unrelated cross-*family*
   `L_GEOMETRIC_M` check). **Checks 1/2 (resolution, angle-spec) still use
   one representative member per pair** — `cpl` and `θ` don't depend on
   `pad`. **Checks 3/4 (placement, phase array) now exercise BOTH members
   of all 8 pairs — 16 constructions**, since a `pad`-arithmetic defect
   specific to `G`'s own code path would not be exercised by `C` alone.
2. **§5a's CLEAN-branch language rescoped.** No longer claims a CLEAN
   result "removes registration... entirely." Rescoped to name the three
   defect classes precisely (see §"Registration-readback gate outcome,
   rescoped" under Predictions below): caller-level plumbing (fully ruled
   out, as originally designed); `run.py`-vs-NOTES.md transcription (ruled
   out by fix #4, new); one spot-check against the shared-recipe class
   (fix #3, new — a spot-check, not exhaustive coverage). Does **not**,
   even post-fix, prove the shared `r{n}_config()` recipe's complete
   internal arithmetic defect-free (Idealization 38, new).
3. **MATERIALS' companion recompute, new, Check 5.** Independently
   recomputes `R4_CONFIGS["C40_R4"]`'s own `y_lo`/`y_hi`/`src_x` directly
   from native (`cpl=20`) base constants × `RATIO=2.0`, **outside** the
   `r{n}_config()` code path (a hand-written, independent arithmetic
   expression, not a call to the function under test) — extending the
   existing Gate-2 precedent (which already does exactly this for `A`) to
   the placement quantities this registration gate itself reads. One
   representative point (`R4`/`C40`) is sufficient — this is a spot-check
   of the recipe's own internal consistency, not a census (Idealization
   38 states this scope explicitly).
4. **QUANTUM's NOTES.md cross-check, new, Check 6 — the single most
   load-bearing fix in this docket.** For each of the 8 representative
   `(family, θ)` points, asserts `run.py`'s job constants
   (`RANK1A_ANGLES`, `RANK1C_ANGLES`, `RANK2A_ANGLE`, `RANK2B_NATIVE_
   ANGLES`, `RANK3A_ANGLE`, `RANK4_ANGLE`, all defined in
   `experiments/095-.../run.py`) equal the values stated in exp-095's own
   `NOTES.md` **Predictions** section (lines 437/445/476/495/511 — a
   textually separate document, committed to git and frozen *before*
   `run.py` was written, per house discipline) — closing the one defect
   class (a transcription slip made when those constants were first typed
   from NOTES.md's prose into `run.py`'s code) that Checks 1–5 cannot
   reach by construction, since they all ultimately read from the same
   `run.py` source as the thing they check.
5. **§7's Sim-construction count corrected: 12→10** (pre-fix-#1 count).
   The positive control (`R4`, `θ=39.2°`, correct wiring) is the identical
   object, as constructed, to representative point 1; FI-B (`angle_deg=
   38.69` mislabeled as intended `39.2°`) is identical, as a constructed
   `Sim`, to representative point 4 — only the harness's own bookkeeping
   label differs, not the object built. Stated explicitly here, not left
   implicit: reusing an already-scheduled correct construction as the
   positive-control demonstrator is efficient, not a design flaw. Post
   fix #1 (16-point set), the true count is **16 (Checks 3/4) + 8 (Checks
   1/2/5/6, one per pair, since those checks don't depend on `pad`) = 16
   distinct constructions total** for the representative set (Checks 1/2/
   5/6 read attributes already present on the same 16 `Sim` objects Checks
   3/4 construct — no separate construction needed), **plus 2 genuinely
   new fault-injection constructions (FI-A, FI-C)** — FI-B is dropped as a
   separate construction per this same finding (it is representative
   point `R4`/38.69°, already built; the harness re-labels its existing
   `theta_intended` to 39.2° for scoring purposes only, spending zero new
   constructions). **Total: 18 `Sim` constructions**, corrected and
   reconciled here from Phase 1's original 12 and this fix's own
   intermediate 10, following fix #1's independent 8→16 expansion. Every
   number in this paragraph is arithmetic on already-stated quantities,
   not a new design choice.
6. **Missing §5-banner added.** ("Every prediction below is governed by
   Idealizations 1/7/17/31–38" — added at the top of Predictions, below.)
7. **§1 trimmed to ≤300 words** (this document's own Hypothesis section
   above, 209 words, replacing Phase 1's 335-word draft).
8. **Vestigial `phase_expected(cpl_intended)` clarified.** Check 4/Check 6
   below state precisely which single recomputation each check diffs
   against `sim.sources[-1]['phase']` — no ambiguity left for the
   implementer.

**Director's own additional clarification, found while merging the
docket (not part of Red Team's 8 items):** fix #1's 8→16 expansion for
Checks 3/4, combined with fix #4's Check 6 (job-constant vs. NOTES.md
cross-check), raises a bookkeeping question Red Team's docket did not
itself resolve: does Check 6 also need both pair members, or is one
sufficient? Resolved here: **one per pair is sufficient for Check 6** —
`theta_intended`/`cpl_intended` are shared across a pair by construction
(fix #1's own finding: only `pad`-dependent fields differ), so NOTES.md's
own frozen angle values apply identically to both `C` and `G`; checking
one member per pair against NOTES.md fully discharges this check for both.
This keeps fix #1's scope expansion limited to exactly the two checks
(placement, phase array) attack #1 showed actually need it, not a blanket
doubling of every check.

## Setup

**Six layered checks per representative point** (superseding Phase 1's
four; a point is CLEAN only if all applicable checks pass):

1. **Resolution registration.** `sim.lam == cpl_intended`.
2. **Angle-spec registration.** `sim.source_specs[-1]['angle_deg'] ==
   theta_intended`.
3. **Placement registration (BOTH pair members, fix #1).**
   `sim.sources[-1]['x'] == x_intended` AND `sim.sources[-1]['sl'] ==
   slice(y_lo_intended, y_hi_intended)`.
4. **Phase-ramp/k-vector registration (BOTH pair members, fix #1).**
   `np.allclose(sim.sources[-1]['phase'], phase_expected, atol=1e-9,
   rtol=0.0)`, where `phase_expected` is computed ONCE, using the
   already-verified `sim.lam` from Check 1 (per fix #8, this is the ONLY
   `phase_expected` array computed; Phase 1's vestigial
   `cpl_intended`-based illustration is removed).
5. **Recipe-internal spot-check (new, fix #3, one point: `R4`/`C40`).**
   `y_lo`/`y_hi`/`src_x` independently recomputed from native `cpl=20`
   base constants × `RATIO=2.0` (hand-written arithmetic, not a call to
   `r4_config()`), compared against `R4_CONFIGS["C40_R4"]`'s own stored
   values.
6. **NOTES.md cross-check (new, fix #4, one point per pair — 8 checks).**
   `theta_intended`/`cpl_intended` (as read from `run.py`'s job constants)
   compared against the values frozen in `experiments/095-.../NOTES.md`'s
   own Predictions section (line-cited per point).

**Representative points (16 `Sim` constructions for Checks 3/4 — both
pair members; Checks 1/2/6 read the same 16 objects' attributes, one
result per pair since those checks are `pad`-independent; Check 5 is one
point only):**

| Family | `cpl_intended` | θ (deg) | Configs (both checked, Checks 3/4) | NOTES.md citation (Check 6) |
|---|---|---|---|---|
| `R4` | 40 | 39.2 | `C40_R4`, `G40_R4` | line 437 |
| `R4` | 40 | 39.4 | `C40_R4`, `G40_R4` | line 437 |
| `R4` | 40 | 38.49 | `C40_R4`, `G40_R4` | line 445 |
| `R4` | 40 | 38.69 | `C40_R4`, `G40_R4` | line 445 |
| `R4` | 40 | 41.6 | `C40_R4`, `G40_R4` | line 495 |
| `R3` | 30 | 38.4 | `C40_R3`, `G40_R3` | line 511 |
| `R5` | 50 | 41.825 | `C40_R5`, `G40_R5` | line 476 |
| `R5` | 50 | 41.850 | `C40_R5`, `G40_R5` | line 476 |

**Fault-injection scenarios (2 genuinely new constructions, fix #5):**

| # | Scenario | Corrupted | Ground truth | Must be caught by |
|---|---|---|---|---|
| Positive control | none (reuse `R4`/39.2°/`C40_R4`, representative point 1) | — | 40, 39.2° | Gate reports CLEAN |
| FI-A | Family/`cpl` swap | `Sim(cells_per_lambda=30)` built where `cpl_intended=40` | 40 | Check 1 (transitively, Check 4) |
| FI-B | Angle mislabel (reuse representative point 4, `R4`/38.69°/`C40_R4`, harness relabels `theta_intended` to 39.2°) | — | 39.2° | Checks 2, 4 |
| FI-C | Sign flip | `add_line_source(angle_deg=-39.2, ...)` where intended is `+39.2°` | +39.2° | Checks 2, 4 (signed-array comparison) |

**Zero-FDTD desk bound (queue item 2, unchanged from Phase 1 — already
computed, independently spot-checked this Phase against raw
`results.json`, bit-exact):** containment ratios of candidate bracket
half-widths (±0.2°/±0.4°/±0.5°) at θ₀≈38.590° against the three already-
filed cross-resolution migration figures (0.193582°/0.320166°/0.376752°).
Answer (Phase 1's §5c, re-verified): ±0.2° insufficient (misses two of
three); ±0.4° clears all three at only 1.06× margin against the largest
(razor-thin by this sub-thread's own R13/R15 empirical standard); ±0.5°
gives 1.33× margin, the most defensible of the three candidates examined.

## T1 escape route

**N/A** — pure instrument-validation work, matching every T28 desk/
instrument cycle since exp-069. No σ(I)/σ(x,t)/angular-selectivity/
sub-threshold claim; `REALIZABILITY_MEMO.md` not touched.

## Realizability bound

**N/A**, identical reason.

## Idealizations

**Carried forward, cited by original number:** 1 (2D TMz, 600nm only), 7
(no constraint-1/2/3/4 test, no T1 position), 17 (`R3`/`R4`/`R5` share one
mechanical `r{n}_config()` recipe, not three independent discretizations —
directly relevant: Check 5's own spot-check bears on exactly this class).

**From Phase 1, renumbered/kept:**

31. This gate checks CONSTRUCTION-TIME registration only, not RUN-TIME
    numerical behavior during `sim.run()` (already separately bounded:
    ELECTROMAGNETISM's exp-093/094/095 Phase-5 reviews independently rule
    out Yee-grid dispersion at 25×–78× too small to explain the observed
    signature). A CLEAN result here does not re-derive that bound; it
    removes a different candidate.
32. A CLEAN result does not itself prove genuine node migration — it
    narrows the live hypothesis space, post-fix, from three named defect
    classes (caller plumbing, transcription, one recipe spot-check) to
    whatever remains after all three are checked (Idealization 38 states
    the residual precisely).
33. Detects defects in how the phase-ramp formula's INPUTS were wired;
    cannot detect a defect in the formula's OWN correctness (the trust
    suite's stage-1/stage-9 regression gates own that).
34. Whichever implementation route Phase 4 uses, the gate's own
    construction-sequence replication must stay in lock-step with the real
    `_run_sim_r{3,4,5}_sigma` call sites, or a future edit to one without
    the other could produce a stale CLEAN reading.
35. The representative set reuses angles already committed in exp-095's
    own job constants, specifically to avoid a fresh, undischarged angle
    choice — not an exhaustive audit of every angle this sub-thread has
    ever measured across 19 cycles.
36. The desk bound's "comparable scale" assumption (a `cpl=20→40`
    migration falling in the same range already measured for the smaller
    `cpl=20→30` step) is stated as optimistic, not conservative — no
    scaling law is fit or claimed.
37. The R13/R15 margin-based comfort benchmark cited for the desk bound is
    drawn from an unrelated measurement domain, offered as a suggestive
    analogy, not a formal transplant.

**New this Phase (Director's synthesis, from the mandatory-fix docket):**

38. **Post all fixes, the gate's honest residual scope**, stated
    precisely per fix #2: a CLEAN result across Checks 1–6 plus a
    correctly-caught FI-A/B/C triad rules out (a) caller-level plumbing
    divergence between a call site and its own job constant [Checks 1–4];
    (b) `run.py`-vs-NOTES.md transcription drift [Check 6]; and gives one
    spot-check, not a census, against a defect baked into `r{n}_config()`'s
    own shared internal arithmetic [Check 5, one point]. It does **not**
    prove the recipe's complete internal arithmetic is defect-free at
    every constant it touches — a narrower, honestly nameable residual
    than "removes registration... entirely," which Phase 1's original
    language overclaimed and this Phase's fix #2 corrects.
39. Check 5's spot-check recomputes `y_lo`/`y_hi`/`src_x` for exactly one
    `(family, config)` pair (`R4`/`C40_R4`). A defect isolated to a
    different family (`R3`/`R5`) or the `G` (padded) config specifically
    would not be caught by this single spot-check — Checks 3/4's own
    16-point expansion (fix #1) covers `G` for placement/phase-array
    registration, but Check 5's recipe-arithmetic recompute does not
    itself extend there this cycle. Left open, not silently assumed
    covered.

**Carried idealizations banner (mandatory at both this section and
Predictions, per the Iteration-65 CHECKPOINT's non-discretionary rule):
every prediction below is governed by Idealizations 1/7/17/31–39.**

## Predictions (frozen, committed BEFORE any Phase-4 script runs)

*Every prediction below is governed by Idealizations 1/7/17/31–39.*

**(Registration-readback gate outcome, PRIMARY, rescoped per fix #2.) No
confident lean on CLEAN vs. DEFECT-FOUND** — this remains the genuinely
open question the reconciled queue names as this sub-thread's single most
fundamental unresolved item.

- **CLEAN** (all 16 representative constructions pass Checks 1–4; Check 5
  passes at its one point; Check 6 passes at all 8 pairs): per
  Idealization 38, rules out caller-level plumbing and `run.py`-vs-
  NOTES.md transcription entirely, and finds no defect at the one
  recipe-arithmetic spot-check — does **not** prove the shared recipe's
  complete arithmetic defect-free. Narrows, does not close, the
  two-candidate (registration-defect vs. migration) hypothesis space Red
  Team's exp-095 audit named; strengthens, does not complete, the existing
  "2:1 to 3:1, impressionistic" reading on file.
- **DEFECT-FOUND** (any check fails at any point): localizes which check
  and which point caught it (Checks 1–4 → caller plumbing; Check 5 →
  shared-recipe arithmetic; Check 6 → `run.py`/NOTES.md transcription),
  reprioritizing every downstream Iteration-73-queue item (3/4/6) around
  understanding and fixing the defect's scope before further FDTD spend
  on this window, and requiring an audit of which of exp-092 through
  exp-095's own filed `results.json` citations rest on the affected call
  site(s) — named as the immediate next action, not scoped further here.

**(Fault-injection positive control, PRIMARY, MUST-catch, per this
program's own R-lineage discipline.)** Confident lean stated, as a
correctness requirement of the check's own design, not a genuine
uncertainty: the positive control MUST NOT be flagged; **all three of
FI-A/FI-B/FI-C MUST be caught** (FI-A by Check 1, transitively Check 4;
FI-B by Checks 2 and 4; FI-C by Checks 2 and 4, specifically because the
signed-array comparison in Check 4 is sensitive to `sin(−θ)=−sin(θ)`). If
any of the three is not caught, the gate itself is not a genuine
discriminator and §"Registration-readback gate outcome" above must not be
trusted until the gate's own design is fixed and re-verified.

**(Zero-FDTD desk bound, PRIMARY, computed, not deferred.)** Already
computed in Phase 1 and independently spot-checked this Phase, bit-exact
against raw `results.json`: at θ₀≈38.590°, ±0.2° is insufficient (misses
two of three already-filed migration figures); ±0.4° clears all three but
at only 1.06× margin against the largest (razor-thin by this sub-thread's
own R13/R15 empirical standard); ±0.5° is the narrowest candidate
examined that clears every figure by more than 30%. This independently
corroborates exp-095's own already-queued item-4 bracket design (asymmetric
half-width roughly 0.3°–0.7°, weighted toward lower θ).

## Estimated FDTD call count and wall-time budget

**0 FDTD calls** — every one of the 18 `Sim` constructions (16
representative + 2 genuinely-new fault-injection, per fix #5's corrected
count) stops before `sim.run()` is ever invoked. Estimated wall time:
under 60 seconds total (Python/NumPy object construction and array
comparison only), matching Phase 1's estimate, adjusted for the 8→16
expansion (still negligible against this sub-thread's own established
~100–150 CPU-minute per-cycle band).

## What this cycle does NOT do (unchanged from Phase 1)

Items 3 (bracketing the other three `cpl=20` nulls at `cpl=40`, ~24 calls)
and 4 (a reconciled node-bracketing re-run at 38.590°, ~8–16 calls) are
gated on this cycle's own registration-readback outcome and are explicitly
NOT run this cycle. Item 6 (resuming the `cpl=50`/`R5` interior sweep)
remains deferred.
