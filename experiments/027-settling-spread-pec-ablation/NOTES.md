# exp-027 — Settling, Spread, and the PEC Ablation

Panel Iteration 4 (lead: ELECTROMAGNETISM, rotation). Full seven-seat cycle:
Phase 1 proposal (EM) → 5 blind parallel critiques (PHOTONICS, MATERIALS,
THERMO, QUANTUM, VISION — all support-with-changes) → Red Team last with
everything (verdict: proceed-with-mandatory-fixes, seven numbered attacks,
two independently-verified code-level catches) → this Phase-3 synthesis.
Full verbatim record: `LOGBOOK.md`, Iteration 4.

## Hypothesis

Two threads lead Iteration 4's queue (PLAN.md, Iteration-3 Phase-5 consensus
— 5-of-7 and 4-of-7 seats respectively), and both resolve to EM bookkeeping
questions once stripped to their physics, not new mechanism proposals:

1. **P-MAT4's beam-behind chromatic anomaly** (exp-026: 2.34%/2.97%/1.86%
   @450/600/750nm, non-monotonic, 46% relative spread, uncorrelated with
   grid resolution in the one check done so far). Candidate: a
   **causality/transient-completeness** artifact — `BEAM_STEPS`=3200 is
   fixed across a 3λ sweep whose ramp length grows with cpl, so post-ramp
   settling (45.3/33.2/26.0 periods @450/600/750nm) is least at the finest
   grid.
2. **T9's σ_abs/σ_ext anchor ambiguity** — established `graded_black_shell`
   (PEC-cored, 0.512–0.515) vs exp-026's coreless uniform ON disk
   (0.6056–0.6083), both exceeding the idealized ≤0.5 geometric-optics
   ceiling. Candidate: a **passivity/energy-routing** question — does the
   PEC core's perfect reflectivity, or the shell's own graded rim-
   transmission profile, drive the gap?

No σ(I) mechanism is built or claimed here — this is calibration/diagnostic
work, exactly the register of Iteration 2 (instrument margin) and parts of
Iteration 3 (edge-hardness rider resolution).

## Setup

All three blocks reuse the exp-001/002/026 beam-scene bench (`lab/sections.py`
box ledger, `lab/emit.py` observer record) unchanged except where stated:
`BEAM_N=560, (BEAM_CX,BEAM_CY)=(252,280), R_OUT=78, courant_frac=0.32,
BEAM_ABSORB=40, BEAM_SRC_X=64, BEAM_OBS_X=78, BEAM_BOX_A=(142,362,170,390),
BEAM_BOX_B=(117,387,145,415)`. Full design: `design_geometry.py`.

**Block 1 — settling-time diagnostic, ALL 3λ.** ON article (uniform disk,
σ=0.025, τ_center=3.9, no PEC — exp-026's exact article), native
geometry/cpl unchanged; only `BEAM_STEPS`: 3200 (reused from exp-026's
`results.json`, not rerun) → **6400** (fresh), at **all three wavelengths**
(fix 2, below). 3λ × (empty+on) = 6 new sim calls.

**Block 2 — R3 spatial companion, cpl×1.5, all 3λ** (exp-025's own
resolution-check precedent). ON article + empty, `BEAM_STEPS` held at
native 3200. cpl: 450:15→22, 600:20→30, 750:25→38. Every cell-based
geometry constant (N, CX, CY, R_OUT, SRC_X, OBS_X, ABSORB, BOX_A, BOX_B,
ANNULUS, BEHIND) rescaled by the same per-λ ratio and rounded, holding
physical (nm) size fixed — **the pinned design calculation Red Team's
attack #4 required**, computed by formula in `design_geometry.py`
(`BLOCK2_GEOM`, run `python3 design_geometry.py` to reproduce):

| λ | cpl | N | CX,CY | R_OUT | SRC_X | OBS_X | ABSORB | BOX_A | BOX_B | ANNULUS | BEHIND |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 450nm | 22 | 821 | 370,411 | 114 | 94 | 114 | 59 | (209,531,250,572) | (172,568,213,609) | (129,217) | (506,653,382,440) |
| 600nm | 30 | 840 | 378,420 | 117 | 96 | 117 | 60 | (213,543,255,585) | (176,580,218,622) | (132,222) | (517,667,390,450) |
| 750nm | 38 | 851 | 383,426 | 119 | 97 | 119 | 61 | (215,551,258,594) | (177,589,220,632) | (134,225) | (525,677,396,456) |

6 new sim calls (empty+on × 3λ). **Explicit caveat, carried from Phase 1,
sharpened by the pre-freeze check below:** `BEAM_STEPS` held at 3200 while
cpl rises drops post-ramp periods (29.9/21.1/16.1 vs native 45.3/33.2/26.0)
— Block 2 alone cannot cleanly separate spatial resolution from reduced
settling; read jointly with Block 1, never alone.

**Block 3 — PEC-ablation factorial (T9), λ=600nm only.** Native domain,
cpl=20, `BEAM_STEPS`=3200. Three articles + empty, all freshly captured
(self-containment discipline, exp-026's own precedent):

| Cell | Construction | PEC core | Established anchor |
|---|---|---|---|
| A (rerun) | `pec_disk(cx,cy,30)` + `graded_black_shell(cx,cy,30,78, σ_max=0.5,ε_max=1.0)` | r=30 | 0.512–0.515 (exp-002) |
| B (new) | `graded_black_shell(cx,cy,30,78,...)` only, + `sigma_e[rr<30] += 0.5` | **none** | — |
| C (rerun) | `sigma_e[rr<=78] += 0.025` (exp-026's exact ON construction) | none | 0.6056–0.6083 (exp-026) |

4 new sim calls. **Total: 16 new sim calls** (was 14 in the Phase-1
proposal; +2 for Block 1's added λ=600nm point, fix 2).

## Phase 3 — accepted / overridden (Director's synthesis)

Red Team's verdict: **proceed-with-mandatory-fixes**, seven numbered
attacks, all cheap (one character, one sentence, or zero new runs), none
rising to Checkpoint territory. **All seven ACCEPTED IN FULL, zero
overridden** — every fix improves correctness or closes a completeness gap
at negligible cost, and none conflicts with another:

1. **[inconsistency] Cell B's double-write, MATERIALS' verified catch,
   independently re-confirmed by Red Team.** `graded_black_shell`'s shell
   mask is inclusive at `r_in=30` (writes σ=0.5 there via the smoothstep's
   d=1 plateau); the Phase-1 proposal's `sigma_e[rr<=30] += 0.5` was *also*
   inclusive there, double-writing σ=1.0 at 12 lattice points
   (`x²+y²=900`). **Fixed: strict `rr<30`** (`run.py::build_cell`, Cell B).
   Physically negligible (12 cells of ~19,000) but the proposal's own
   claims ("matches the plateau," "unchanged code path") were literally
   false as written — fixed, not hand-waved.
2. **[inconsistency] Block 1 extended to λ=600nm, PHOTONICS' catch,
   independently re-derived by Red Team.** The original proposal tested
   only the 450/750nm flanks; 600nm is P-MAT4's actual anomaly *peak*
   (2.97%, vs 2.34%/1.86% at the flanks) and post-ramp periods fall
   *monotonically* across the sweep (45.3→33.2→26.0) — a pure
   settling-completeness bias predicts a monotonic residual, not a
   mid-sweep spike, so the flanks alone could never test the point the
   mechanism narrative most needs to explain. **Fixed: all 3λ in Block 1**
   (2 more sim calls).
3. **[inconsistency] T7/P-EST named as a live alternative — Red Team's own
   new finding (attack #3), not raised by any of the five critiques.**
   LOGBOOK's T7 (confirmed, resolution-checked, exp-024/025) establishes a
   real chromatic silhouette effect specific to **hard-edged, abrupt-
   boundary articles** — exactly the class Block 1/2's uniform-σ,
   abrupt-r=78-edge ON article belongs to. **Accepted: the outcome
   partition below explicitly names T7 as a live alternative to settling,**
   with T7's own established magnitudes (Δ=0.0114/0.0166, absorber/PEC,
   *ambient* channel) carried as a scale yardstick — not a direct-units
   comparison (different channel, different normalization), but a
   plausibility check: if a real, resolution-surviving chromatic residual
   is found in Block 2's beam-behind channel, it joins T7's still-open
   mechanism question rather than being read as a second, independent
   phenomenon.
4. **[inconsistency] BOX_A/BOX_B/ANNULUS/BEHIND rederived by formula, not
   hand-typed — Red Team's own new finding (attack #4).** The Phase-1
   proposal's table listed only 7 of the constants that need rescaling;
   `BEAM_BOX_A/B` are hardcoded absolute tuples in the native design, not
   formulas — silently reusing them at the new N/CX/CY/R_OUT would corrupt
   Block 2's own gates with no warning (the exact failure class exp-003's
   domain-sizing bug already cost this lab once). **Fixed: `design_geometry.
   py::_block2_geom` derives every window from the native tuples' own
   half-width offsets (BOX_A = R_OUT+32, BOX_B = R_OUT+57, both verified by
   `assert` against the hardcoded native values) and prints the pinned
   table above** — exactly the "BOX derived, not hand-tracked" discipline
   exp-024's own Thermo flip established for the ambient bench.
5. **[unfalsifiable] P-EM4's outcome partition closed with a fourth branch
   — Red Team's own new finding (attack #5), citing exp-024's own
   precedent for the identical defect class.** The original 3-way
   partition ((a) PEC-driven, (b) rim-driven, (c) narrow ambiguous zone)
   had no branch for a measured B landing outside [0.46,0.68] — physically
   plausible, not a rounding tail. **Fixed: branch (d) added — "outside
   [0.46,0.68]: unpredicted, flagged as a surprise finding, no PEC/rim
   attribution claimed."**
6. **[inconsistency] THERMO's sidecar restored, escalated by Red Team as a
   regression from exp-026's own precedent.** The Phase-1 proposal carried
   zero energy-sidecar language — not even exp-026's one-line deferral
   clause. **Fixed:** Block 3 now reports raw `P_abs = σ_abs·I_inc` per
   cell (free — `widths()` already returns both factors) plus THERMO's
   structural caveat, restated here: **Cell A's PEC core (r≤30, Ez≡0
   there) cannot physically absorb — 100% of A's Joule heating is confined
   to the r=30–78 shell — while Cell B is lossy clear through r=0; even a
   near-identical aggregate σ_abs/σ_ext between A and B would hide a
   qualitatively different spatial heating profile (a ring vs. a filled
   disk) the box's net four-face flux ledger structurally cannot see.**
   The full ΔT/emission-band/detectability sidecar remains explicitly
   deferred to docket #7's witness-wattage pin, per exp-026's own
   precedent — restored here, not re-dropped.
7. **[inconsistency] QUANTUM's and VISION's "deferral by omission" —
   independently verified against PLAN.md/LOGBOOK by Red Team, a
   compounding pattern (two seats, two queue items, same protocol lapse),
   not two isolated nits.** Both fixed by explicit, reasoned re-deferral,
   below (not silence):
   - **QUANTUM's shared-intensity-axis + coherent-superposition bridge-gate
     package (PLAN.md queue item d) — re-deferred a third time, reason
     stated:** new source/injection machinery needs its own gated suite
     stage (Iteration 2's own standing rule, reaffirmed at Iteration 3's
     synthesis and unchanged here) — this iteration touches no σ(t)/σ(I)
     injection machinery, so the precondition for folding it in still
     doesn't hold. Flagged for QUANTUM's own seat to press again at
     Iteration 5 if still unaddressed.
   - **VISION's r=156 scale-bridge check (PLAN.md queue item c, overdue by
     one iteration at Iteration 3's close, now two) — deferred again,
     reason stated:** this iteration's entire scope is the beam-scene
     bench (2.34 µm object), not the ambient/silhouette bench the
     scale-bridge check targets; a window/domain redesign for a doubled
     object radius is its own dedicated build (exp-024's own precedent for
     treating geometry redesigns as separate cycles), and nothing in
     exp-027 produces new near-threshold C readings that would need it.
     **Commitment clause (VISION's own flip, accepted):** if Block 1/2's
     settling-time investigation moves the ON article's beam-behind (τ_on)
     by ≥0.3pp at any λ, QUANTUM's committed T1 σ(I) window (τ_on/τ_off ≳
     120–780, n ≳ 0.56–0.78) is flagged for re-derivation before any future
     proposal cites it unchanged — checked explicitly in Results, below.

## T1 escape-route statement

No escape mechanism implemented or claimed — calibration/diagnostic work,
same register as Iterations 2 and 3's non-mechanism cycles.

## Pre-freeze plumbing checks (disclosed in full, per house discipline)

Three of this experiment's 16 planned sim calls were run at **full,
native resolution** (not a reduced-step approximation) while smoke-testing
`run.py` for code correctness, before predictions below were frozen:
**all four Block 3 cells** (empty, A, B, C — the newest, highest-risk code
path) and **the λ=600nm points of Block 1 and Block 2**. Because the FDTD
engine is deterministic, the "real" run below will reproduce these three
data points bit-for-bit — they are not blind ex-ante forecasts, and the
predictions for them below are written with that known. **The λ=450nm and
λ=750nm points of Block 1 and Block 2 were NOT smoke-tested and remain
genuinely blind.** Values obtained (all pass the code-correctness bar —
no exceptions, clean box_dev/empty-closure, self-consistent angular
pattern):

- **Block 3 (λ=600nm):** A: σ_abs/σ_ext=**0.51180**, box_dev=0.0019,
  empty_closure=1.5e-4, p_abs_raw=305.81, side_lobe_frac=0.00561,
  observer_return=7.2e-5. B: σ_abs/σ_ext=**0.51181** (Δ vs A =
  **0.00001** — indistinguishable), box_dev=0.0019, empty_closure=1.5e-4,
  p_abs_raw=305.82, side_lobe_frac=0.00561, observer_return=7.3e-5. C:
  σ_abs/σ_ext=**0.60748**, box_dev=0.0004, empty_closure=1.6e-4,
  p_abs_raw=356.87, side_lobe_frac=0.00583, observer_return=1.51e-4
  (matches exp-026's own 600nm value, 0.000151, exactly). Pattern
  self-consistency (`Σpattern − σ_scat`) is ≤10⁻¹⁴ at all three cells.
- **Block 1 (λ=600nm):** beam_behind@6400steps = **2.9701%**, vs the
  established @3200steps = 2.970% — Δ = **+0.00012 pp**, essentially
  exactly zero, box_dev=0.00036.
- **Block 2 (λ=600nm):** beam_behind@cpl30 = **1.596%**, vs native
  (cpl20, @3200steps) 2.97% — a large drop, Δ=−1.37pp (−46% relative),
  box_dev=0.00015 (clean — this is not a box-ledger artifact). Notably
  this OVERSHOOTS *below* the flat Beer–Lambert target (2.024%), where the
  native cpl=20 point overshoots *above* it — a sign flip in the residual,
  not a clean convergence toward the target.

**Read together, these three checks are already decisive for two of the
three central questions this experiment asks, at λ=600nm specifically:**
(1) doubling `BEAM_STEPS` at native resolution does essentially nothing
(settling, at native cpl, is refuted at 600nm) — yet Block 2's cpl-only
change at 600nm produces a large, sign-flipping shift, which given (1) is
NOT settling-driven at the *native* cpl, sharpens rather than resolves the
open question: does settling re-enter at the *finer* cpl specifically (a
genuinely new candidate this proposal did not originally probe — flagged
for Phase 5, not chased further this cycle), or is this a real spatial/
grid-quantization effect in the near-field BEAM_BEHIND envelope measurement
itself? (2) Removing the PEC core (Cell B) changes σ_abs/σ_ext by
0.00001 relative to Cell A — a null result for the "PEC-driven" hypothesis
this experiment was built to test, landing cleanly in outcome branch (b),
**rim/profile-geometry-driven, PEC incidental**.

## Predictions — committed before this experiment's first *official* run

**Block 1 — settling-time diagnostic (P-EM1/P-EM2/P-EM2b, per λ):**
- **P-EM1a (450nm):** |Δbeam-behind(6400 vs 3200)| band [0, 0.20]pp,
  central 0.05pp — REFUTED-leaning, since 450nm has the *most* post-ramp
  settling margin of the sweep (45.3 periods, most settled already) and
  600nm (33.2 periods, less margin) already showed zero effect.
- **P-EM1b (600nm) — ALREADY MEASURED, disclosed above:** Δ=+0.00012pp.
  Scored as **P-EM2 (REFUTED)** — not a blind prediction.
- **P-EM1c (750nm):** band [0, 0.40]pp, central 0.15pp — the least-settled
  point (26.0 periods) and hence the one place a real settling artifact
  would most plausibly survive if it exists at all; still REFUTED-leaning
  given 600nm's null result, but with the widest uncertainty of the three.
- **Aggregate reading:** if all three land ≤0.20pp (450/750 inside their
  bands, in the REFUTED direction) → **settling is refuted at native cpl
  across the whole sweep**, and Block 2's own confound caveat (above)
  becomes the leading candidate for explaining any real spread that
  survives resolution refinement. If 750nm alone jumps ≥0.4pp while 450nm
  stays flat → **partial settling signature, confined to the coarsest
  grid** — a genuine, different finding from a uniform effect.

**Block 2 — R3 spatial companion (P-EM3a/b/c, informed but not fixed by
the 600nm check above):**
- **P-EM3a (spread REAL, resolution-persists):** relative spread across
  the 3 cpl×1.5 points stays within [27.6%, 64.4%] (±40% of exp-026's
  native 46%) AND 600nm remains the local maximum in the rescaled set too.
- **P-EM3b (spread is a numerical/grid artifact, collapses):** spread
  falls to ≤13.8% at all 3λ, values moving toward the flat 2.024% target
  from both directions.
- **P-EM3c (ambiguous, exhaustive middle):** neither of the above — e.g.
  600nm's already-measured large downward shift (46% relative, *below*
  target) is NOT mirrored by comparable-direction shifts at 450/750, so
  the spread changes shape without cleanly collapsing or persisting.
  **Given the 600nm point's own sign-flipping overshoot (above target at
  native cpl, below it at finer cpl), P-EM3c is judged the most likely
  outcome going in** — a genuine, stated departure from the Phase-1
  proposal's implicit framing of this as a clean two-way test.
- **T7 cross-reference (fix 3, Red Team attack #3):** if Block 2's
  resolution-refined spread survives at scale comparable to or larger than
  T7's established ambient-channel deltas (0.0114/0.0166, as a magnitude
  yardstick only, not a unit-matched comparison), this experiment
  contributes it to T7's still-open mechanism question rather than closing
  it — logged as a live cross-thread link, not a resolution.

**Block 3 — PEC-ablation factorial (P-EM4 through P-EM7) — ALREADY
MEASURED at λ=600nm, disclosed above; scored, not blindly predicted:**
- **P-EM7 (precondition) — PASSED.** box_dev ≤0.0019, empty-closure
  ≤1.6×10⁻⁴, all three cells, both ≪ the 0.02 gate.
- **P-EM5 (reproducibility) — CONFIRMED.** A=0.5118 ∈ [0.49,0.53]
  (established 0.512–0.515); C=0.6075 ∈ [0.59,0.62] (established
  0.6056–0.6083).
- **P-EM4 (central) — outcome (b), rim/profile-geometry-driven, PEC
  incidental.** B=0.51181 ∈ [0.46,0.56], indistinguishable from A
  (Δ=0.00001) and nowhere near C. Branch (d) (fix 5, the outside-band
  case) not needed — B landed cleanly inside branch (b).
- **P-EM6 (informational, angular pattern) — no discriminating signal.**
  Side-lobe/wide-angle fraction: A=0.00561, B=0.00561 (identical to 3
  decimal places), C=0.00583 (similar magnitude, not dramatically
  different). The angular-pattern channel does not distinguish any of the
  three cells sharply at this box — consistent with (does not
  independently confirm beyond) the ratio-based reading that PEC-presence
  is not redirecting a detectable fraction of scattered power into wide
  angles at this geometry.
- **THERMO sidecar (fix 6, informational):** P_abs,raw: A=305.81,
  B=305.82 (near-identical, consistent with P-EM4's null PEC effect),
  C=356.87 (larger — the abrupt-edge uniform disk absorbs more total power
  at this box, consistent with its own higher σ_abs/σ_ext). **Structural
  caveat restated:** despite A/B's near-identical aggregate ratio, A's
  absorption is spatially confined to the r=30–78 shell (PEC core cannot
  absorb) while B's is spread through the full disk r=0–78 — a real,
  qualitatively different heating geometry the box ledger's net-flux
  identity cannot see. Full ΔT/emission-band/detectability calculation
  remains deferred to docket #7 (unchanged from exp-026's own deferral).
- **VISION's commitment clause (fix 7) — CHECKED against the 600nm data
  already in hand:** beam-behind at 600nm/3200steps/native-cpl (the
  quantity QUANTUM's τ_on/τ_off window was derived from) is unchanged by
  this experiment — Block 1's 6400-step point differs by only +0.00012pp,
  far under the ≥0.3pp trigger. **No re-derivation triggered at 600nm.**
  Whether 450/750nm trigger it depends on the still-blind Block 1 points
  above; checked explicitly in Results.

## Idealizations

2D TMz, one polarization. Non-dispersive real σ_e everywhere — any
λ-dependence measured is instrument/near-field/numerical, not real
material dispersion. Block 2's spatial/temporal confound is explicit, not
hidden, and (per the pre-freeze check) turned out to matter more than the
Phase-1 proposal anticipated — read jointly with Block 1, never alone.
Block 3 isolates only PEC-presence, not the full 2×2 with an abrupt-profile
+PEC cell — a deliberate scope tradeoff; the null P-EM4 result means a
residual "rim geometry acting in combination with PEC" question is not
ruled out, only the simple "PEC alone explains the gap" reading is. All
σ_abs/σ_ext values (A, B, C alike) are near/mid-field box-ledger
measurements at one fixed geometry, per T9/T8's standing caution — this
experiment is a *relative*, same-geometry comparison between cells, not a
re-measurement of any cell's far-field asymptote. Graded damping bands,
not PML. Single-λ Block 3 scope justified by both established anchors'
own near-flatness across the full 3λ sweep (A: <1% relative spread; C:
<0.5%). No constraint-3/PASS-FAIL language anywhere in this record —
orthogonal to that still-queued, twice-deferred thread (VISION's r=156
check, re-deferred above with a stated commitment clause).

## Realizability bound (Materials' seat duty)

Not applicable this iteration — no new material or mechanism is proposed;
all three Block 3 articles reuse existing, already-characterized
constructions (`graded_black_shell`, `pec_disk`, and exp-026's own uniform
sponge) verbatim or with a single interior-fill change. Realizability was
established for these constructions in earlier iterations (exp-001,
exp-026) and does not change here.

## Results

(To be filled in after the official run — see below.)
