# PHASE 3 — SYNTHESIS · Panel Iteration 43 · Director

Resolves PHOTONICS' Phase-1 proposal, five blind Phase-2 critiques
(MATERIALS, ELECTROMAGNETISM, THERMODYNAMICS, QUANTUM OPTICS, VISION
SCIENCE), and Red Team's Phase-2 final audit (verdict:
**PROCEED-WITH-MANDATORY-FIXES**) into ONE testable configuration —
candidate exp-066.

## Accepted / overridden

**All five Phase-2 critiques' load-bearing findings are ACCEPTED, as
reconciled by Red Team's own docket (A–E below). None overridden.** Red
Team's own audit (§1, "overreach check") independently verified every
critique's factual claims against primary artifacts before ruling, and
found nothing to strike. This Director adopts that ruling without
override — a rare, but not unprecedented, 5-for-5 acceptance (Iteration
41's exp-064 Phase-3 synthesis is the direct precedent for zero-override
closes on instrument-trust cycles).

The two apparent tensions Red Team flagged and resolved:

- **VISION's ±35° ask vs. the Phase-1 proposal's "Block MAIN, textually
  defined" scope-definition.** Red Team's attack 1 sharpened this beyond
  VISION's own framing: the Iteration-43 mandate's own committed text
  (LOGBOOK.md T27 entry, "Ranked top-3," and PLAN.md's queue — all three,
  independently) reads **"MAIN-block ±35°/±38°/±40° rows,"** not
  exp-041's internal `MAIN_ANGLES` naming alone. The Phase-1 proposal's
  scope-narrowing, while textually correct about exp-041's own code
  (verified: `results.json::block_main` has exactly 30 rows, no 35°),
  silently departed from the mandate's own words. **Accepted as
  load-bearing, per Red Team attack 1.**
- **EM's "move 2 calls to a new interior angle" vs. VISION's "add 6 calls
  for ±35°" — apparently competing for the same 38-call budget.** Red
  Team's attack 2 dissolved this: VISION's own costing was wrong.
  exp-065's own C40 config (=exp-041's own geometry verbatim) already has
  ±35°×3λ committed at **both** STEPS=1400 and STEPS=2800 — folding it in
  costs **zero** new FDTD calls, a citation only. EM's and VISION's asks
  do not compete; they compose. **Both accepted, neither traded against
  the other.**

## The one testable configuration (candidate exp-066)

**T1 escape route: NONE** — instrument/model-fidelity re-verification
class (exp-041/exp-064 precedent). No σ(I)/σ(x,t)/angular-selectivity/
sub-threshold machinery is touched, advanced, or claimed.

**FDTD blocks (39 new calls total, via exp-065's own `CONFIGS["C40"]`/
`_settle_one`/`_c_empty` harness — zero `lab/` engine change):**

1. **Block G1EXT** — {36,37,39}°×{±}×{450,600,750}nm @ STEPS=1400 (18
   calls). Extends exp-065's own G-1 bit-exact anchor from 12/30 to
   30/30 of exp-041's committed Block MAIN cells.
2. **Block MAIN2800** — the same 18 cells @ STEPS=2800 (18 calls). The
   core deliverable: closes the 18-row gap no committed data anywhere in
   this program covers at any STEPS beyond 1400.
3. **Block STRESS** (3 calls, **mandatory fix B applied**):
   - 40°/750nm @ STEPS=4200, 5600 (2 calls, unchanged from Phase 1) —
     the λ-axis generalization check.
   - 37°/600nm @ STEPS=4200 (1 **new** call, Red Team attack 3/EM's
     catch) — the θ-axis generalization check the Phase-1 draft
     completely lacked (zero of its 18 new interior-angle cells had any
     independent convergence check of their own).

**Desk-only, zero new FDTD calls:**

4. **Mandatory fix A** — the mandate's own literal "±35°/±38°/±40°" text
   is closed in full by citing exp-065's own already-committed ±35°×3λ
   values at both STEPS=1400 (`results.json` Block SWEEP) and STEPS=2800
   (`settled_sweep_steps2800_diagnostic.json`), alongside the
   already-settled ±38°/±40° cells from the same two files. Combined
   with blocks 1–2, this gives full closure of all 36 mandate-named
   cells (±35° through ±40°, both signs, 3λ) at both STEPS values.
5. **Mandatory fix C** — P-066-4's T21 fringe-fit refit (exp-042's own
   `edge_diffraction_c_empty_corrected`, scored against the full 30-row
   settled Block MAIN dataset) is reported **strictly as a fit-quality
   statistic**. No causal or mechanism language anywhere in its
   CONFIRM/REFUTE interpretation — a recovered R² does not, by itself,
   distinguish a genuine coherent edge-diffraction fringe from the
   settling artifact's own (θ,λ)-dependence correlating with the fringe
   model's own geometric clock `A·cosθ` (Red Team attack 4 / QUANTUM's
   own Phase-2 self-catch on its own Phase-1 exp-065 proposal). Forward
   tripwire attached verbatim, extended: no future citation of this
   refit's R² may be read as "confirmed edge-diffraction/coherent-fringe
   mechanism" while Block MINI's period-match test (P-VIS42-10, exp-065)
   remains UNDECIDED.

**Applied before the predict-commit, not gated by the run:**

6. **Mandatory fix D** — `lab/caveat_lint_config.json`'s
   `exp065-steps1400-unsettled-plane-channel` entry widened: `candidate_
   globs` now includes `experiments/034-floor-convergence-scale-bridge/
   REALIZABILITY_MEMO.md`; `trigger_terms` widened with `off_pass`, `N17`,
   `D_req`, `537`, `540.{0,5}600` (the memo's own vocabulary). Verified
   live, before and after: `python3 lab/caveat_lint.py --only
   exp065-steps1400-unsettled-plane-channel` found **zero** mentions of
   `REALIZABILITY_MEMO.md` before the edit and **one** WARN-level
   candidate-site finding (trigger `off_pass`) after — the reachability
   gap Red Team's attack 5 found is closed. Still 0 required-site
   failures (this widening adds a candidate lead, not a new hard
   requirement — `REALIZABILITY_MEMO.md`'s own UNOBTANIUM-WITH-PARAMETERS
   verdict is independently confirmed unaffected in substance: it rests
   on RSA's 1–2 OOM dynamic-range gap and TPA's 9–12 OOM irradiance gap,
   both stated by the memo itself as independent of the D_req figure's
   precise value).
7. **Mandatory fix E** — R_contact disposition (see
   `design_geometry.R_CONTACT_DISPOSITION` and NOTES.md): named
   explicitly as a **third consecutive deferral** (Iteration 41→42→43),
   disclosed as desk/literature work orthogonal to this cycle's FDTD
   budget, per Red Team attack 6 / THERMODYNAMICS' catch.

**Settling-mechanism disclosure (Red Team attack 3, not a mandatory fix
but load-bearing context):** the Phase-1 proposal's own candidate
mechanism for the 750nm residual (turn-on ramp length, ~107 steps at
cpl=25) is roughly one order of magnitude too small to be the dominant
driver (corrected from the Phase-1 draft's "two orders of magnitude" —
Red Team's own arithmetic check). A stronger, already-committed
candidate exists on this program's own record (exp-042's
`MARGIN_PERIODS`, thinnest at 750nm) but is not tested as a causal claim
by any gate here — see `design_geometry.SETTLING_MECHANISM_NOTE`, cited
in NOTES.md, not scored.

## Predictions committed before any run

See NOTES.md — P-066-G1, P-066-1, P-066-2, P-066-3a, P-066-3b, P-066-4,
identical to `run.py`'s own `FROZEN_PREDICTIONS` structural-freeze print
(verified to match, word for word, at commit time).

## Checkpoint status

Per Red Team's own audit §3: none of PANEL.md's five Checkpoint criteria
fire. Criterion 4 (program-integrity drift) explicitly does not fire,
conditional on this docket (A–E) actually landing before the predict-
commit — it has: all five items are applied above, verified live where
verifiable (D), and the run has not yet executed. No Marsh convening
required at this phase.
