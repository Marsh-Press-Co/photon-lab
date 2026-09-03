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
