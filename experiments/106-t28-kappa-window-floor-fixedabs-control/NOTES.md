# exp-106 — Floor-Gating, Settling, Risk-Propagation, and the Fixed-Absolute-Thickness Control for `kappa_window`

**Panel Iteration 83. Lead seat (rotation): QUANTUM OPTICS. Director:
Clyde (photonlab-shift, cloud panel shift).** Executes exp-105's own
Reconciled Iteration-83 queue, Tier 1 items 1–4 in full (Red Team's own
final-audit tiered ranking, `phase5_redteam_audit.md` §7 of exp-105).
Instrument-extension cycle, diagnostic only — T1: N/A, zero `lab/` diff,
no mechanism proposed or varied.

Full record: `phase1_proposal.md` (QUANTUM OPTICS), `phase2_critique_
{photonics,materials,em,thermodynamics,vision}.md` (five blind critiques,
all support-with-changes), `phase2_redteam_audit.md` (9 numbered attacks,
7 mandatory fixes, one MAJOR partial override of MATERIALS' own critique,
verdict PROCEED-WITH-MANDATORY-FIXES).

## Hypothesis

exp-105 (Iteration 82) extended T8's r=78/156/312 near-field scale-bridge
to the coherent `kappa_window` channel for the first time, finding a
headline "shape_ratio=19.79" result — but its own Phase-5 review left
four specific gaps open: `kappa_window` has never been floor-gated at any
r; it has never had its own settling-independence leg (only the sibling
`kappa_region_point` channel did); P3's own scored verdict has no
risk-propagation gate symmetric to P4's `p4_156_trusted`; and a genuine
alternative mechanism (the self-similar family's own coating growing
electrically thicker, 2.4λ→9.6λ, as r scales) was never discriminated
against exp-052's already-built fixed-absolute-thickness control.
Hypothesis: closing all four lets P3's own accelerating collapse finally
be TRUSTED or REFUTED as physics, rather than merely SCORED-BUT-CAVEATED.

## Setup

Full derivation: `phase1_proposal.md` (Phase-1 draft) as corrected by
`phase2_redteam_audit.md` §3.1 (7 mandatory fixes, all adopted). Every
geometric constant is computed by `run.py::geom(r)`/`geom_fixedabs(r)`,
never hand-typed (R4 discipline) — this file states the DESIGN, not fresh
arithmetic.

- **Self-similar family**: `run.py::geom(r)`, byte-for-byte the same
  formula chain as exp-105's own `geom(r)` (κ=r/78, `R_CORE=round(30κ)`,
  `sigma_max=0.5/κ`, `tau_shell=24.0` fixed) — re-verified to reproduce
  exp-105's own committed `geom_78/156/312` exactly on every shared field
  (Gate P0, below).
- **Fixed-absolute-thickness family**: `run.py::geom_fixedabs(r)`,
  exp-052's own `design_geometry.py` formulas (`R_CORE=r-48` cells fixed,
  `sigma_max=0.5` fixed, `tau_shell=24.0` fixed — coincides exactly with
  the self-similar family at r=78) — generalized to the coherent
  point/region-intensity channel and to r=156/312 for the first time.
  Domain construction (N/CX/CY/SRC_X/STEPS/behind window/dense_x/
  `z_over_zr`/`nyquist_margin`) is IDENTICAL to the self-similar family at
  the same r — only `R_CORE`/`sigma_max` differ, verified by construction
  (`geom_fixedabs()` copies `geom()`'s own dict and overrides only those
  two fields plus the derived `tau_shell`).
- **Ledger box/ref (new this cycle, mandatory fix 1)**: `box_a`/`box_b`
  margins and `ref` half-height reuse exp-028/exp-030's own established
  `_rescaled_geom()` convention verbatim, scaled by κ
  (`box_a_hw=R_COAT+round(32κ)`, `box_b_hw=R_COAT+round(57κ)`,
  `ref_hh=round(60κ)`) — independently confirmed to reproduce exp-028's
  own native r=78 values bit-exact (`box_a=(142,362,170,390)`,
  `box_b=(117,387,145,415)`, `ref=(252,280,60)`).
- **Floor-gate on `window_stats()`'s own output** (`floor_gate_window()`,
  mandatory fix, proposal §2c): reuses `floor_gate()` verbatim on the
  EMPTY-scene window box's own per-cell `|Ez|²` array (4,000 cells, fixed
  across r) — `FLOOR_FRAC=0.10`, unchanged. Because an empty scene never
  calls `materials.pec_disk`/`materials.graded_black_shell`, this result
  is mathematically IDENTICAL between families at a given r — computed
  once, shared.
- **Settling-independence leg on `kappa_window`** (`settling_pass_
  window()`, item 2): doubled STEPS, `STABILITY_TOL=0.20` (exp-103's
  established tolerance, unchanged), applied to BOTH families at r=156
  AND r=312.
- **`p3_trusted` / `shape_ratio_fixedabs_trusted`** (item 3, mandatory
  fix 3): `settling_pass AND (nyquist_tier(r)=="TRUSTED")`, symmetric in
  KIND (not just name) to exp-105's own `p4_156_trusted`. Both
  structurally forced **False** at r=312 (`nyquist_margin(312)=1.234`,
  MARGINAL — a fixed domain-geometry property, identical between
  families). A units-corrected noise-floor flag (`noise_floor_flag()`,
  Director's own correction of Red Team's literal proposal — see `run.py`
  module docstring) additionally guards the shape_ratio denominator on
  both families symmetrically (R13/R14 discipline).
- **Ledger sanity check** (`ledger_check()`, mandatory fix 1, cost
  characterization corrected per Red Team Attack 8): `sections.widths()`
  (box-independence, `sigma_abs`/`sigma_ext`) and
  `sections.radial_absorbed_power()` (spatial concentration, core_frac ≈
  0 sanity) on BOTH families at r=156/312 — the fixed-abs family reaches
  `R_CORE/R_COAT`=0.692 (r=156)/0.846 (r=312), past T9's only-validated
  core-energetically-incidental anchor of 0.385. Requires a small,
  disclosed code change to `_run()` (now optionally also returns the
  article scene's `sim.sigma_e` grid) — zero new `Sim.run()` calls, per
  Red Team's own corrected characterization.
- **Director's own cost optimization** (disclosed, not hidden): because
  an empty scene is family-independent, each empty-scene capture is run
  ONCE per (r, STEPS) and reused for both families' `kappa_window`/ledger
  computations. This cuts the Phase-1 proposal's own disclosed 16-call
  budget to **12 real `Sim.run()` calls** if every leg commits (r=78
  contributing 0 to both families, unchanged) — a free, physically-
  justified reduction, not a scope cut; every Tier-1 item still executes
  in full.
- **Cost-gating**: each r=312 leg (primary self-similar+fixed-abs pair;
  settling self-similar+fixed-abs pair) is piloted independently via its
  own shared empty-scene call — abort if that pilot exceeds 90 minutes,
  or if the projected 3-call total (1 empty + 2 article) exceeds 180
  minutes. Two data points ground the estimate: T8's own Iteration-7
  precedent (a real leg overran its own hand estimate by up to 8×) and
  exp-105's own r=312 primary pilot (31.13 min, well under threshold).
- **Reproduction checks** (R4/R8 discipline, zero new information but
  load-bearing): fresh r=156/312 self-similar captures' `kappa_window`
  must reproduce exp-105's own committed values to <1e-6 relative before
  any of this cycle's own floor-gate/settling diagnostics are trusted.
- **P5 (thermal sidecar): NOT re-invoked** this cycle — THERMODYNAMICS'
  own Phase-2 critique raised a real question (does the fixed-abs
  family's higher, non-rescaled `sigma_max` change the absorbed-power
  budget vs. self-similar at fixed r_out?) which the new ledger check
  (`p_abs_frac_diff`) directly answers empirically this cycle, without
  needing to re-invoke the full thermal chain (the `l_geometric_m`
  argument genuinely does not change, THERMODYNAMICS' own steel-man point
  — only the absorbed-power INPUT to that chain could, and the ledger
  measures it directly).

## T1 escape-route statement

**N/A — instrumentation/diagnostic work**, exactly as exp-102/103/104/105
were. No σ(I)/σ(x,t)/angular-selectivity machinery is built or varied.
Constraint-3/4 perceptual scoring is explicitly NOT performed this cycle —
the `DISCLAIMER` (extended this cycle to also name the Nyquist-margin
gate's own reused-proxy scope, mandatory fix 7) is asserted present in
both `PREDICTIONS_TEXT` and `RESULT_TEXT` (R23 pattern, code-enforced per
mandatory fix 5 — a single string is built once and both asserts check
the SAME concatenated text every new verdict this cycle introduces is
folded into, closing the specific erosion risk VISION's Phase-2 critique
named).

## Idealizations

- 2D TMz, single λ=600nm/cpl=20 scope, unchanged from exp-102/103/104/105.
- θ=0° only (normal incidence) — the oblique-angle extension remains
  open (Tier 3 item 1, deferred again, not executed this cycle).
- `graded_black_shell` remains UNOBTANIUM-WITH-PARAMETERS at every r in
  BOTH families — see the Realizability note in Predictions (mandatory
  fix 4, Red Team's own citation-grounded replacement text, correcting a
  stale claim in the Phase-1 proposal's own §5).
- P5 (thermal sidecar) not re-invoked (see Setup, above) — the ledger's
  own `p_abs_frac_diff` is the scored proxy for whether the thermal chain
  would need re-derivation, not a full re-invocation.
- The ledger check (`ledger_check()`) is explicitly NOT a re-run of
  exp-052's own hollow-vs-PEC-cored delta methodology (Red Team Attack 9)
  — it establishes only that absorbed power is physically sane
  (concentrated in the shell annulus, box-independent) at these new,
  higher `R_CORE/R_COAT` ratios, not a validated delta against T9's own
  0.385 anchor. A genuine hollow-vs-PEC-cored delta test is a Tier-2 item,
  a real new-FDTD-call cost, not executed this cycle.
- No fourth r-point (Tier 2 item 1) is added this cycle — the two-point
  fit degeneracy (78/156/312 only) is unchanged.
- No witness-scale extrapolation is attempted or claimed.
- `lab/` diff: zero.

**Tier 3 item 2 — the `delta_scene` R3-vs-R4 split, explicit
re-justification for a SEVENTH consecutive deferral (required in
writing, per PLAN.md's own instruction — this is a departure this file
must not make silently):** This is a genuinely different, older, much
larger T28 sub-question (a boundary-echo/PAD-diffraction mechanism's own
resolution-sensitivity at a specific x-normal-wall angle scan), with its
own independent multi-iteration history (Iterations 51 through 82),
structurally unrelated to the `kappa_window` r-family bridge work this
cycle's entire FDTD budget (12 real calls, cost-gated up to ~4 hours
disclosed worst case) is already committed to. This program has a direct
precedent for exactly this situation: **Iteration 51's "no-seventh-cycle"
rule**, which capped a DIFFERENT, prior `delta_scene` question at six
deferrals with the identical structure (a standing, well-understood, but
never-executed-or-formally-retired item competing against a cycle's own
committed higher-priority FDTD budget) — that precedent is the model
followed here. Stated plainly, as the Phase-1 proposal itself already
committed: **Iteration 84, or the next cycle with spare FDTD/wall-clock
budget, must either execute the `delta_scene` R3-vs-R4 split or formally
retire it** — an eighth deferral would not be acceptable under this
program's own standing discipline, and this file does not attempt either
option itself this cycle.

## Predictions (frozen BEFORE any FDTD call — house discipline)

Verbatim from `run.py::build_predictions_text()` (generated by code, not
hand-typed, R23/R4 discipline) — printed in full by `run.py
--predictions-only`, reproduced here for the record at freeze time:

```
PREDICTIONS (pre-registered, exp-106, Panel Iteration 83)

Raw physical intensity ratios and an absorbed-power sanity ledger only --
no Weber-contrast or C_thr(L) perceptual scoring is performed this cycle;
not a claim about human visibility. The Nyquist-margin trust tier is a
reused DENSE_X point-sampling aliasing proxy, not an independently-derived
box-integral aliasing bound for window_stats() (mandatory fix 7). NETD is
an instrument/detector threshold, not a human perceptual one -- this
classification does NOT bear on constraint-3/4's human-eye verdict (panel
Iteration 20, VISION SCIENCE's mandatory fix, Red Team attack 7).

Gate P0 (ground-truth recovery, zero cost): geom(78/156/312) reproduces
exp-105's own committed geometry EXACTLY on every shared field (N, CX,
CY, SRC_X, STEPS, R_CORE, sigma_max, behind window, dense_x). Falsified
by ANY mismatch -> halt. [Independently dry-run-verified TRUE before this
freeze -- see Panel record, below.]

Reproduction check (Gate-P1-equivalent for kappa_window, zero new
information but load-bearing): fresh r=156/312 self-similar captures'
kappa_window must reproduce exp-105's own committed values to <1e-6
relative. Falsified -> halt.

Item 1 (floor-gate window_stats()): predicted PASS (frac_unresolved<2%)
at r=156; BORDERLINE predicted at r=312 (possibly >10%) -- the empty-
scene window-box mean intensity itself falls steeply with r. Shared
between families (empty-scene-only check). r=312's own self-similar
wide/point/delta_phi (dense_x) persisted in full this cycle.

Item 2 (settling leg on kappa_window itself, both families): r=156
predicted PASS (rel_change<=0.20); r=312 genuinely uncertain -- no
settling leg has ever run there for any channel, the most urgent leg
this cycle.

Item 3 (p3_trusted / shape_ratio_fixedabs_trusted): BOTH predicted FALSE
at r=312 by construction (nyquist_margin(312)=1.234, MARGINAL, a fixed
domain-geometry property identical between families) -- a structural,
disclosed prediction, not a coin flip. A units-corrected noise_floor_flag
additionally guards both families' shape_ratio denominators.

Item 4 (fixed-abs control): a pure geometric-window effect predicts
shape_ratio_fixedabs approx EQUAL to self-similar's own 19.79 (scored
directly via abs_ratio(r)=kappa_fixedabs(r)/kappa_selfsim(r), band:
within a factor of 2.0 of 1.0). Classification bands on shape_ratio_
fixedabs itself: <=8.0 CONFIRMS the growing-electrical-thickness
hypothesis; >=14.8 REFUTES it; between AMBIGUOUS. Even the CONFIRM band
(implied exponent n<=3.0) sits above this program's own cited
edge-diffraction theory range (n~1-2) -- neither outcome reconciles with
known diffraction physics, only arbitrates two internal hypotheses. A
radial_absorbed_power/widths() sanity ledger runs on both families at
r=156/312 (R_CORE/R_COAT=0.692/0.846, past T9's 0.385 anchor) before this
verdict is trusted as clean -- not a re-run of exp-052's own hollow-core
delta test (Tier 2).

Realizability note (mandatory fix 4, Red Team's own replacement text):
both families' r=78 anchor's 1.44um shell thickness is already CLOSED
UNOBTANIUM-WITH-PARAMETERS at REALIZABILITY_MEMO.md AMENDMENT 6/7
(Iteration 38/39), overdetermined by the THICKNESS axis (100-500um real
vs 1.44um, 70-350x gap); fixed-abs holds this gap at every r, self-
similar's absolute thickness grows with r and is marginally (not
substantially) closer at larger r -- the opposite of a naive "fixed-abs
is more realistic" reading.

Mandatory Idealizations: 2D TMz, single lambda=600nm/cpl=20, theta=0 only,
no witness-scale extrapolation, P5 not re-invoked, delta_scene R3-vs-R4
split re-justified for a seventh deferral (see NOTES.md Idealizations).
```

## Panel record

**Phase 1** (QUANTUM OPTICS, lead seat by rotation): `phase1_proposal.md`
— 16-call design, closing all four exp-105 Phase-5 gaps.

**Phase 2**: five blind critiques, all support-with-changes
(`phase2_critique_{photonics,materials,em,thermodynamics,vision}.md`):
PHOTONICS proposed a sharper, free, absolute-ratio cross-family test
(adopted as `abs_ratio`); MATERIALS flagged a realizability-claim
conflation later found stale by Red Team; ELECTROMAGNETISM and
THERMODYNAMICS independently converged on the identical finding — the
fixed-abs family's own `R_CORE/R_COAT` ratio (0.692/0.846) exceeds T9's
only-validated core-incidental anchor (0.385), needing a `radial_
absorbed_power`/`widths()` ledger check; VISION flagged an R23
disclaimer-erosion risk specific to this cycle's new verdict text.

**Red Team's Phase-2 audit** (`phase2_redteam_audit.md`): independently
re-verified every critique's core finding from primitives (confirming
the 0.692/0.846 arithmetic, confirming `sections.radial_absorbed_power`
exists but needs a small `_run()` code change to supply `sigma_e`, first
verified). **One MAJOR partial OVERRIDE**: MATERIALS' own critique cited
a since-superseded claim (the absorptivity-realism question was already
CLOSED at REALIZABILITY_MEMO.md AMENDMENT 6/7, Iterations 38/39,
postdating exp-052's own Phase-5 open item MATERIALS cited) — Red Team
caught this and supplied citation-grounded replacement text (mandatory
fix 4). Two new Red-Team-only attacks: an R13/R14-flavored gating-rigor
gap (`shape_ratio_fixedabs`'s own r=312 reading only got a soft caveat
where `p3_trusted` gets a hard suppressor — mandatory fix 3); the EM/
THERMODYNAMICS ledger fix's own "zero marginal cost" framing needed a
small correction (mandatory fix 1/Attack 8). **Verdict: PROCEED-WITH-
MANDATORY-FIXES, Checkpoint criterion 4 does NOT fire** (no unfalsifiable
claims; T1 correctly, repeatedly N/A; constraint-3 explicitly, not
quietly, out of scope by inherited precedent).

**Phase 3 (this synthesis, Director).** All 7 of Red Team's mandatory
fixes ADOPTED in full:

**Same-shift correction (Red Team's Phase-5 final audit,
`phase5_redteam_audit.md` §0.1/§4, added post-freeze — zero re-run, zero
verdict-arithmetic change): "ADOPTED in full," above, is imprecise for
mandatory fix 1 specifically.** Mandatory fix 1's own text
(`phase2_redteam_audit.md` §3.1) carries TWO parts: a ledger COMPUTATION
(`ledger_check()`, `sections.widths()`+`radial_absorbed_power()`) and an
attached interpretation RULE ("if fixed-abs and self-similar's
`p_abs`/`sigma_ext` fractions land within ~10% of each other... adequately
clean; if they diverge materially, report `shape_ratio_fixedabs`'s bands
as **three-way ambiguous**"). Only the computation was wired into
`run.py`; the rule's own consequence was never implemented in the
classification logic (five of six blind Phase-5 seats — EM, MATERIALS,
PHOTONICS, QUANTUM, THERMODYNAMICS — independently caught this from
primitives; see the Result section's own Item 4 paragraph, corrected
below, and the audit's §0.1/§2 for the full trace). No override of this
consequence was ever recorded in this Panel record. Checkpoint criterion 4
does not fire on this gap (audit §2: R20's own strict tally is 0, at most
1 under the most generous reading, far short of "three or more"; the gap
was caught blind, within this cycle's own six-seat-plus-Red-Team review
layer, before LOGBOOK) — but a new standing rule (proposed R24, audit §2)
is recommended for Director ratification to close it going forward.

1. Ledger check (`ledger_check()`, `sections.widths()`+
   `radial_absorbed_power()`) on both families at r=156/312 — cost
   characterization corrected per Attack 8 (`_run()` now optionally
   returns `sim.sigma_e`, a small code change, zero new `Sim.run()`
   calls).
2. `abs_ratio(r) = kappa_fixedabs(r)/kappa_selfsim(r)` at r=156/312,
   factor-of-2 band.
3. Hard `p3_trusted`/`shape_ratio_fixedabs_trusted` gates, symmetric in
   kind to `p4_156_trusted`, PLUS a noise-floor flag on the shape_ratio
   denominator — **implemented with a units correction** (Director's own
   fix: Red Team's literal proposal compared a dimensionless kappa
   difference against a raw intensity RMS; this file's own
   `noise_floor_flag()` instead uses `3*FLOOR_FRAC*|kappa_156|`, a
   relative tolerance dimensionally consistent with `floor_gate()`'s own
   convention, applied to BOTH families symmetrically).
4. Realizability sentence replaced verbatim with Red Team's own
   citation-grounded text (REALIZABILITY_MEMO.md AMENDMENT 6/7).
5. R23 concatenation code-enforced: `build_predictions_text()`/
   `build_result_text()` are the single source of truth every new
   verdict this cycle introduces is folded into; both `assert DISCLAIMER
   in ...` lines check the actual concatenated string.
6. Predictions text states explicitly that even the CONFIRM band (n≤3.0)
   sits above the cited edge-diffraction theory range (n≈1–2).
7. `DISCLAIMER` extended to name the Nyquist-margin gate's own
   reused-proxy scope.

No criticism was overridden except the one MAJOR partial override above
(Red Team's own, not the Director's) — every mandatory fix is
independently cheap, mechanical, and leaves the cycle's own disclosed
scope/budget intact.

**Director's own additional contribution, disclosed**: the empty-scene
cost optimization (§Setup) — reduces the real `Sim.run()` call count from
the Phase-1 proposal's own disclosed 16 to 12, with zero loss of
diagnostic coverage (every Tier-1 item still executes in full at every
committed r).

`run.py`'s Gate P0 logic was independently dry-run-verified against
exp-105's own committed `geom_78/156/312` dicts before predictions were
frozen (PASS on every shared field at all three r) — this dry-run touches
zero FDTD machinery and is disclosed here as a pre-freeze code-correctness
check, not a result. A code-path smoke test (tiny STEPS, not physically
meaningful) additionally confirmed `floor_gate_window()`, `settling_pass_
window()`, `ledger_check()`, `shape_ratio_fit()`, and `noise_floor_flag()`
all execute without error on real `Sim`/`materials`/`sections` calls
before any real-STEPS FDTD call ran.

Predictions frozen and committed to git in this same commit, strictly
BEFORE `run.py`'s first real-STEPS `Sim.run()` call, per house
discipline.

## Result

**10 real FDTD calls (of the 12 scheduled if every leg committed),
18398.4s (306.64 min / 5.11h) wall time, zero `lab/` diff throughout.**
The two calls not run were the r=312 settling leg's own article pair
(self-similar + fixed-abs): its own empty-scene pilot alone took 6196.6s
(103.28 min) — past the 90-min per-leg abort threshold on its own, before
either article call would have run — so the cost gate correctly deferred
the entire leg rather than committing further wall-clock. (The r=312
*primary* leg's own empty pilot, by contrast, came in at 3158.8s
(52.65 min), under threshold, so its own two article calls DID commit —
the same gate firing two different ways on two legs of the identical r,
exactly as designed.)

**Gate P0: PASS.** **Reproduction checks (r=156/312, self-similar):**
both **exact**, rel_dev=0.000e+00 — fresh captures reproduce exp-105's
own committed `kappa_window` values to machine precision at both r,
before any of this cycle's own diagnostics are trusted.

**Item 1 (floor-gate `window_stats()`'s own output): PASS at BOTH r,
cleanly — the r=312 BORDERLINE prediction is FALSIFIED, in the
reassuring direction.** r=156 frac_unresolved=0.0000 (n=4000, rms=5.002,
floor=0.5002, 0 unresolved cells). r=312 frac_unresolved=0.0000 as well
(n=4000, rms=5.003, floor=0.5003, 0 unresolved) — the Phase-1 proposal's
own "possibly >10%" concern, carried into the frozen Predictions, does
not survive contact with the actual data: the solver's noise floor tracks
the signal's own fall-off closely enough that `window_stats()`'s mean
intensity never approaches it at either scale tested. r=312's own
wide/point/delta_phi channels (DENSE_X, self-similar) are persisted in
full this cycle — see `results.json` `r312_selfsim` — the specific
"stop discarding" gap exp-105's own Phase 5 named is closed; its own
floor gate is likewise clean (frac_unresolved=0.0000, n=53).

**Item 2 (settling-independence leg on `kappa_window` itself): PASS,
landslide, at r=156 for BOTH families; genuinely NOT RUN at r=312 (cost-
deferred, per the pre-registered gate, not a silent drop).** r=156
self-similar rel_change=0.0002 (tol 0.20 — three orders of magnitude
inside); fixed-abs rel_change=0.0001 (four orders of magnitude inside).
r=312: the empty-scene settling pilot alone exceeded the 90-min abort
threshold (see wall-time note above), so neither family's article pair
ran — `kappa_window`'s own settling status at r=312 remains genuinely
untested, exactly the "most urgent, genuinely uncertain" leg the frozen
Predictions named as the cycle's own biggest open risk, and it is the
one leg that did NOT resolve this shift. Queued forward, not silently
dropped (see Next).

**Item 3 (risk-propagation gates): both FALSE, exactly as predicted —
a structural outcome, not a coin flip.** `p3_trusted` (self-similar) =
False; `shape_ratio_fixedabs_trusted` = False. Both forced by
`nyquist_tier(312)=MARGINAL-REDUCED-CONFIDENCE` (nyquist_margin=1.234,
a fixed domain-geometry property identical between families) — and, for
`shape_ratio_fixedabs_trusted` specifically, doubly so this shift since
the r=312 settling leg never ran for either family (item 2, above).
`noise_floor_flag`: NOT triggered for either family (`noise_dominated=
False` on both self-similar's and fixed-abs' own shape_ratio
denominators) — the near-zero-denominator failure mode the gate exists
to catch did not occur.

**Item 4 (fixed-abs control — the falsifiable heart of this cycle):
a real, scored, but explicitly NOT-TRUSTED result — and, per a same-shift
correction below, also THREE-WAY AMBIGUOUS, not a clean binary (see the
"Same-shift correction" paragraph following the Ledger sanity check,
below).**
`shape_ratio_fixedabs=18.2283` — inside the pre-registered REFUTE band
(>=14.8), the same classification direction as a clean read would give
("REFUTES-electrical-thickness-growth-hypothesis": geometric z/z_R
window effect dominates, not the coating's own growing electrical
thickness) — but `run.py`'s own classification string appends
"(NOT-TRUSTED — r=312 MARGINAL/unsettled)" because `shape_ratio_
fixedabs_trusted=False` (item 3), and per Red Team's own mandatory fix 3
this gate is honored literally: **the discriminator's own headline
number is reported, not suppressed, but is not certified as physics
this cycle.** The ledger sanity check below independently exceeds
mandatory fix 1's own ~10% reclassification trigger, at both measured r —
this is a second, additive reason (beyond the NOT-TRUSTED settling/Nyquist
gate) the REFUTE reading is not yet a clean two-hypothesis discriminator.
Self-similar P3, recomputed fresh (not merely reused):
`shape_ratio=19.7878` — reproduces exp-105's own committed 19.79 to
four significant figures, an independent confirmation via a freshly-run
capture, not a re-read of the same file.

**PHOTONICS' own sharper absolute-ratio test (mandatory fix 2) DOES
clear its own band at both r, and is NOT gated by `..._trusted`** (it
compares two families' raw `kappa_window` values directly, not a fitted
shape parameter): `abs_ratio(156) = kappa_fixedabs/kappa_selfsim =
1.0852`; `abs_ratio(312) = 1.8797` — both within the pre-registered
factor-of-2.0 band of 1.0, corroborating geometric-window dominance at
the absolute-magnitude level at both r, independent of the settling
question above. (Read together with item 4: the shape-fit discriminator
is honestly withheld from trust, but the simpler, ungated absolute-ratio
test the same Phase-2 critique proposed as a cheaper cross-check already
points the same direction.)

**Ledger sanity check (mandatory fix 1): core-concentration and
box-independence both clean; the cross-family absorbed-power fraction
itself diverges more than the ~10% informal expectation named in the
frozen Predictions, an honest, unresolved-band finding, not a pass/fail
gate.** `core_frac` (fraction of absorbed power landing inside the PEC
core, should be ~0): 0.000e+00 at every (r, family) — perfectly clean,
same as exp-105's own r=78/156 anchor, generalizing cleanly to both
higher `R_CORE/R_COAT` ratios (0.692/0.846) past T9's 0.385 anchor.
`box_dev` (established <=0.12 convention): 0.0001 (r=156 self-similar),
0.0008 (r=156 fixed-abs), 0.0000 (r=312 self-similar), 0.0002 (r=312
fixed-abs) — all 2+ orders of magnitude inside the established bound.
**But `|p_abs_fa − p_abs_ss|/p_abs_ss`: 0.1231 at r=156, 0.1796 at
r=312 — both EXCEED the ~10% figure `run.py`'s own print-statement used
as an informal descriptor.** No pre-registered pass/fail band was frozen
for this specific quantity (the frozen Predictions describe the ledger
as a sanity check on concentration/box-independence, not a gated
tolerance on the cross-family absorbed-power delta itself) — reported
here as a genuine, disclosed, un-gated observation for Phase 5 to weigh:
the two families hold `tau_shell=24.0` exactly equal by construction
(both self-similar and fixed-abs), but achieve it via different
thickness/sigma_max combinations, so some cross-family divergence in the
realized absorption fraction is not on its face surprising — whether
12–18% is "physically sane" (as the ledger check's own stated purpose
requires before trusting item 4 as a clean discriminator) or itself
informative is not adjudicated here.

**Same-shift correction (Red Team's Phase-5 final audit, applied
post-freeze — zero re-run, pure re-labeling of already-persisted
`results.json` fields, zero verdict-arithmetic change): this paragraph's
own "not adjudicated here" is superseded.** Mandatory fix 1's own text
(`phase2_redteam_audit.md` §3.1, itself reusing THERMODYNAMICS' own
Phase-2 flip condition verbatim) pre-registers exactly this adjudication:
*"if fixed-abs and self-similar's `p_abs`/`sigma_ext` fractions land
within ~10% of each other at matched r, treat item 4's two-hypothesis
framing as adequately clean; if they diverge materially, report
`shape_ratio_fixedabs`'s CONFIRM/REFUTE bands as **three-way ambiguous**
(thickness-law vs. core-reflection/gradient-steepness vs. both), not a
clean binary."* The measured divergence — 12.31% (r=156), 17.96% (r=312)
— **exceeds this ~10% trigger at both measured r, including r=156, this
cycle's one fully TRUSTED, cleanly-settled leg.** Per this program's own
rule, Item 4's honest classification is therefore: **THREE-WAY AMBIGUOUS
(thickness-law vs. core-reflection/gradient-steepness vs. both) —
REFUTES-electrical-thickness-growth-hypothesis nominally, per the raw
`shape_ratio_fixedabs=18.2283` bands alone, but not yet certified as a
clean two-hypothesis discriminator — and, independently, NOT-TRUSTED
(r=312 MARGINAL/unsettled).** `run.py`'s own persisted classification
string was never updated to reflect this rule (five of six blind Phase-5
seats — EM, MATERIALS, PHOTONICS, QUANTUM, THERMODYNAMICS — independently
caught this gap from primitives; full trace:
`phase5_redteam_audit.md` §0.1/§2); correcting the code is Iteration-84's
job (Tier 1, `phase5_redteam_audit.md` §5), not a same-shift change to
`run.py`/`results.json` — this note corrects the prose record only. A
genuine hollow-vs-PEC-cored delta test (exp-052's own methodology, Tier 1
item 1 of the Reconciled Iteration-84 queue) remains the instrument that
would actually resolve the three-way ambiguity, not merely disclose it.

**Realizability note (mandatory fix 4): unchanged, reported verbatim as
frozen** — both families' r=78 anchor is UNOBTANIUM-WITH-PARAMETERS per
REALIZABILITY_MEMO.md AMENDMENT 6/7; fixed-abs holds the same 69–347×
thickness gap at every r; self-similar's absolute thickness grows with r
(2.88µm/5.76µm at r=156/312) and is only marginally, not substantially,
closer to the real 100–500µm range at larger r.
