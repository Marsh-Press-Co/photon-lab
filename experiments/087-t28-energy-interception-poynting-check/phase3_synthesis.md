# PHASE 3 — SYNTHESIS (Director) · Panel Iteration 64 · exp-087

## Disposition of Phase 2

Five blind critiques (PHOTONICS, MATERIALS, ELECTROMAGNETISM, QUANTUM
OPTICS, VISION SCIENCE), unanimous **support-with-changes**, zero overlap.
Red Team's Phase-2 audit independently re-derived every load-bearing claim
in all five from source (not from the critiques' own prose) and returned
**PROCEED-WITH-MANDATORY-FIXES**, confirming all five critiques exactly
(one immaterial imprecision noted and corrected in EM's own supporting
prose, non-load-bearing) and adding one new finding of its own (settling of
the `widths()`-derived channel unverified). Zero critiques were overstated;
zero were wrong. A 10-item fix docket was returned, tiered by urgency.

**Director's ruling: all 10 items ADOPTED IN FULL, zero overrides.** Every
item is independently re-verified from source in the audit itself (not
merely argued), cheap (mostly zero marginal FDTD cost), and closes a real
gap rather than gold-plating a non-issue. Two items (1, 3 below) are
directly load-bearing on the primary pre-registered metric and are treated
as blocking preconditions, not disclosed caveats — matching this
sub-thread's own R8 standard ("an unverified argument about a flagged gap
is not sufficient to file it non-blocking when an affordable check
exists").

## Adopted fixes, mapped to the frozen plan below

1. **`xi_ext` verification gate (EM, Red Team item 1).** ADOPTED as a
   blocking Tier-0 precondition. `xi_ext(cfg,θ,leg) =
   |sigma_ext_cross − sigma_ext| / |sigma_ext|`, computed at **both**
   `BOX_A` and `BOX_B` (folding in item 9's completeness request), reusing
   stage 8's own `xi_p ≤ 0.12` tolerance. HALT before computing any P5
   classification if violated anywhere.
2. **Break the aliasing lattice (PHOTONICS, Red Team item 2).** ADOPTED.
   Angle set changes from `{36.0°, 39.0°, 42.0°}` (uniform 3.0° spacing,
   1.02 cycles of `P*=2.9474°` per step, 1.8% from exact aliasing) to
   `{36.0°, 38.6°, 41.8°}` (`dg069.DENSE_ANGLES[0]`/`[13]`/`[29]` —
   confirmed valid grid points by direct computation) — non-uniform
   spacing (2.6°, 3.2°), chosen so neither gap sits within 5% of either
   `P_edge_A=2.8421°` or `P*=2.9474°`, and so a real aliasing artifact
   would show up as an internal inconsistency (the two gaps disagreeing)
   rather than hiding behind a single, uniform, near-resonant step.
3. **Pre-register 0/1-resolved disposition (QUANTUM, Red Team item 3).**
   ADOPTED. §4-P5's four classification labels are scoped explicitly to
   apply only when ≥2 of 3 angles resolve. 0 or 1 resolved angles is
   reported as its own fifth outcome, **DEGENERATE**, disclosed as
   non-informative for the scientific question even though (per Red Team's
   own careful separation of the two questions) it would still count as
   discharging the Checkpoint tripwire on the tripwire's own literal
   "build it" terms.
4. **Synthetic recovery check on the classification pipeline (QUANTUM,
   Red Team item 4).** ADOPTED. Before trusting the real data's
   classification, the pipeline is fed synthetic `(frac_p_abs,
   frac_contrast)` pairs at the decade boundaries (ratios 0.05, 0.1, 1, 10,
   20) and must recover the intended bucket at each — a unit-test-shaped
   gate on the classifier itself, zero FDTD cost.
5. **Settling spot-check on the new channel (Red Team item 5).** ADOPTED,
   taking the "run one cheap comparison" branch (not the "elevate the
   disclosure" branch) since the marginal cost is one extra FDTD call pair
   at STEPS=1400, mirroring exp-083's own settling idiom exactly.
   `STEPS=1400` vs `STEPS=2800` compared on `sigma_abs`/`sigma_ext` at one
   cell (`G40`, θ=38.6°, `BOX_A` — the article leg, middle angle, matching
   exp-083's own `SETTLE_THETA=39.0`/`SETTLE_CFG="G40"` choice as closely
   as this cycle's new angle grid allows). Disclosed alongside P5, not
   gating (matches exp-083's own precedent for this exact check), but its
   `rel_dev` is now a mandatorily-reported field, not a silent omission.
6. **Pre-commit a P6 flip-triage rule (MATERIALS, Red Team item 6).**
   ADOPTED as explicit text in §4/Idealizations (below): any P6 departure
   from UNDETECTABLE must first be checked against this program's own
   already-measured material-identity swing magnitudes (~780× Biot,
   Iteration 22; ~116× H_CONV, Iteration 34) before being read as new
   oblique physics.
7. **Non-negativity assertion (EM, Red Team item 7).** ADOPTED:
   `sigma_abs ≥ 0` and `p_abs_w ≥ 0` asserted at every (cfg, θ, box, leg)
   cell, both boxes, in the Phase-4 script itself (not merely stated in
   prose).
8. **Inline disclaimer discipline (VISION, Red Team item 8).** ADOPTED:
   every restatement of P6/constraint-3 language in this document,
   `NOTES.md`, and any future citation of this cycle's numbers must carry
   the NETD instrument-not-eye disclaimer and the "does not test
   constraint 3, only its energy-ledger bookkeeping" scope note inline,
   not by reference to a single frozen paragraph.
9. **Report `box_dev`/`xi_ext` at both boxes (Red Team item 9).** ADOPTED
   — folded into item 1 above.
10. **Log aliasing-risk-band membership at result time (Red Team item
    10).** ADOPTED: the Phase-4 script computes and persists, for the
    actual angle set used, how close each inter-angle gap sits to
    `P_edge_A`/`P*` (as a fraction of each period), so a future reviewer
    does not have to re-derive Attack 3 from scratch.

**Standing forward tripwire (Red Team, adopted verbatim):** if fixes 1
and/or 2 had NOT been adopted and either gap later proved
outcome-determining, that would fire Checkpoint criterion 4 under this
program's own R8 standard. Moot here since both are adopted before any
FDTD call — recorded for the register regardless, per this sub-thread's
own house habit of naming near-miss tripwires explicitly even when they do
not fire.

## Checkpoint criterion 2

**N/A**, unchanged from Phase 1 (§3) and confirmed independently by Red
Team (§0 of its audit): no phenomenon-mechanism claim, no T1 escape-route
framing applies.

## Frozen configuration (supersedes Phase 1's parameter table where changed)

All Phase-1 parameters carry forward UNCHANGED except the angle set
(fix 2) and the addition of one settling-check FDTD call pair (fix 5) and
the `xi_ext`/synthetic-recovery/non-negativity gates (fixes 1, 4, 7 — zero
marginal FDTD cost, pure post-processing of already-planned captures).

| Quantity | Phase-1 value | Phase-3 (frozen) value |
|---|---|---|
| Angle subset | {36.0°, 39.0°, 42.0°} | **{36.0°, 38.6°, 41.8°}** (`DENSE_ANGLES[0,13,29]`) |
| New FDTD calls | 12 | **14** (12 main + 2 for the STEPS=1400 settling spot-check at G40/38.6°) |
| `BOX_B` reporting | context-only (P3) | **mandatory alongside `BOX_A` for both `box_dev` AND `xi_ext`** |

Everything else (geometry, configs, STEPS=2800 main, `dx_m`, thermal
constants, `irr_central`, NETD band, `l_geometric_m`, area convention) is
unchanged from Phase 1 §2 — re-cited here, not retyped, per this
sub-thread's own R4 discipline.

## Frozen predictions (P1–P8, supersedes Phase 1 §4 — committed BEFORE any
Phase-4 code runs)

**P1 (zero-FDTD vacuum-footprint precondition, unchanged from Phase 1).**
Predict PASS at every `BOX_A`/`BOX_B` cell, both configs. HALT if it fails.

**P2 (reproduction precondition, unchanged in kind, re-targeted to the new
angle set).** Fresh `C_empty(cfg,θ)` at θ∈{36.0,38.6,41.8}° must reproduce
`experiments/083-.../results.json::per_theta` at those angles (`38.6` and
`41.8` are both present in exp-083's own 31-point grid), max|Δ|<1e-9.
Predict PASS.

**P3 (box independence, disclosed context, unchanged in kind).**
`box_dev_ext`/`box_dev_abs` reported at all 6 (cfg,θ) cells, both legs.

**P4 (xi_ext verification gate — NEW, Tier-0 blocking, fix 1).**
`xi_ext(cfg,θ,leg)` computed at `BOX_A` and `BOX_B`, both legs, all 3
angles (12 cells total). **HALT before any P7 classification is computed
unless `xi_ext ≤ 0.12` at every cell.** Predicted PASS, stated with only
moderate confidence per EM's own critique — this is a genuinely
never-tested combination (oblique incidence + `graded_black_shell` +
PAD-shifted box), not a foregone conclusion; a failure here would itself
be a significant, independently-flaggable instrument finding, not a
proposal failure.

**P5 (synthetic classifier-recovery check — NEW, Tier-0 blocking, fix 4).**
Synthetic `(frac_p_abs, frac_contrast)` pairs constructed to give
`ratio_k ∈ {0.05, 0.1_minus_eps, 0.1_plus_eps, 1, 10_minus_eps,
10_plus_eps, 20}` must each recover the intended bucket
(DECOUPLED/boundary/CONSISTENT/boundary/DOMINANT) exactly. Predict PASS —
this is arithmetic on the classifier's own already-stated thresholds, not
a new physical claim.

**P6 (settling spot-check — NEW, disclosed not gating, fix 5).**
`|sigma_abs(BOX_A, G40, θ=38.6°, STEPS=2800) −
sigma_abs(BOX_A, G40, θ=38.6°, STEPS=1400)| / |sigma_abs(..., 2800)|` and
the analogous ratio for `sigma_ext`, reported. No pre-registered pass/fail
band (matches exp-083's own precedent for the identical check on the
Weber-contrast channel) — but see Idealization 7 below for what a large
value would mean.

**P7 (PRIMARY, pre-registered, falsifiable — Phase-1's P5, re-scoped to
the new angle set and the explicit 0/1-resolved carve-out).** For each
θ∈{36.0,38.6,41.8}°, resolved per the noise-floor gate (Phase 1 §4-P5,
unchanged: excluded if `|p_abs_w(G40,θ)−p_abs_w(C40,θ)|` does not exceed
`3×max(box_dev_ext,box_dev_abs)(cfg,θ)×p_abs_w(C40,θ)`):

- **DEGENERATE**: fewer than 2 of 3 angles resolve. Reported as
  non-informative for the scientific question (though it would still
  discharge the tripwire on the tripwire's own "build it" terms — see
  Adopted-fixes item 3 above).
- **ENERGY-DECOUPLED**: `ratio_k(θ)<0.1` at every resolved angle (≥2).
- **ENERGY-DOMINANT**: `ratio_k(θ)>10` at any resolved angle.
- **CONSISTENT**: every resolved angle (≥2) has `0.1≤ratio_k(θ)≤10`.
- **MIXED**: resolved angles span more than one of the above three.

**Pre-registered prediction, carried from Phase 1, moderate confidence:
ENERGY-DECOUPLED at ≥2 of the 3 angles** (equivalently, at least 2
resolved AND all resolved angles read ENERGY-DECOUPLED). Reasoning
unchanged from Phase 1 (bulk-integrated flux vs. localized contrast are
different classes of observable; exp-076's lossless-vacuum proof already
implicates a phase-only mechanism at this confound). Corroborative, not
dispositive. Falsified by CONSISTENT or ENERGY-DOMINANT at ≥2 of 3
resolved angles, by MIXED, or by DEGENERATE (which falsifies the
prediction's own precondition of having an informative answer, though not
the tripwire discharge).

**P8 (scene-specific detectability, unchanged in kind from Phase 1, with
the mandatory triage rule attached — fix 6).** `netd_disposition` for both
configs at all 3 angles, at `BOX_A`. **Predict UNDETECTABLE at every
(cfg,θ) cell.** *Triage rule, pre-committed:* if any cell departs from
UNDETECTABLE, that departure must first be checked against this program's
own already-measured material-identity swing magnitudes (~780× Biot,
Iteration 22/exp-045; ~116× H_CONV, Iteration 34/exp-057) before being
read as genuine new oblique physics rather than a compounding
ASSUMED-silicon-constant artifact. *Disclaimer, carried inline
(fix 8):* NETD is an instrument/detector threshold, not a human
perceptual one — this classification does NOT bear on constraint-3/4's
human-eye verdict, matching `thermo_sidecar.py`'s own built-in disclaimer
text.

**Non-negativity gate (fix 7, blocking, not a numbered prediction but a
hard assertion in code):** `sigma_abs≥0` and `p_abs_w≥0` at every (cfg, θ,
box, leg) cell — trivial by passivity; a violation halts the run as a
sign/phasor-convention bug, not a physics finding.

## Idealizations (supersedes Phase 1 §5, fixes folded in)

1. 3-angle subset (now non-uniformly spaced, {36.0°,38.6°,41.8°}), not the
   full 31-point window.
2. Single λ=600nm.
3. `iso_xsec_sq` area convention (thermo_sidecar's own stated idealization).
4. Silicon thermal constants (ρ, c_p) ASSUMED, unsourced provenance (T18).
5. WitnessScenario irradiance/distance/candela WebSearch snippet-tier
   (T18), reused verbatim from exp-043.
6. `ratio_k` decade-scale tiers are a deliberately wide, first-of-its-kind
   band, not a rigorously derived confidence interval.
7. **Settling of the `widths()`-derived channel IS now spot-checked once
   (fix 5, P6)** — a single-cell check, not the full R3-grade convergence
   study; a large `rel_dev` there would be a genuine, disclosed reason to
   discount P7's own reliability, flagged explicitly if it occurs, not
   silently absorbed.
8. The 3× box-dev noise-floor multiplier remains a house-style choice
   (mirrors R3's "survive with margin" precedent), now additionally
   checked for basic sanity by the synthetic recovery test (fix 4), which
   validates the classifier's threshold LOGIC, not the 3×/0.1/10 numeric
   choices themselves — those remain a disclosed, non-rigorous convention.
9. NETD is an instrument/detector threshold, not a human-eye one (carried
   inline per fix 8, every restatement).
10. This cross-check bears only on T28's own confound-mechanism question
    and constraint-3's energy-ledger bookkeeping (carried inline per fix
    8). It does not test constraints 1/2/4, and does not re-open or
    re-score `REALIZABILITY_MEMO.md`'s verdict.
11. Not this cycle's mandate: the near-unanimous #1 grazing-incidence
    validity check, the x-wall leg (11 cycles deferred), the full-scale
    null-calibration re-run, R12-into-standard-practice — real, overdue,
    belong on Iteration 65's board.
12. **New, fix 4's own scope:** the synthetic recovery check validates the
    classifier's bucket LOGIC at exact/near decade boundaries; it is not a
    null-permutation test against this specific run's own real data (R5's
    literal machinery does not apply to a 3-point ratio comparison — no
    "search over combinations" occurs here) and is not represented as one.

## Phase 4 plan (final, supersedes Phase 1 §6)

One script, `experiments/087-.../run.py`, reusing exp-083's `_load()`
idiom to import `dg069`/`build_article`/`_run_sim` **unmodified**. Order of
operations, each a HALT point where marked:

1. P1 vacuum-footprint check on both configs' `Sim.__init__` arrays at
   both `BOX_A`/`BOX_B` footprints. **HALT if fails.**
2. Run 14 FDTD calls (2 configs × 3 angles × {empty,article} = 12, +
   2 for the G40/38.6°/STEPS=1400 settling pair), capturing via
   `sc.full_capture`.
3. P2 reproduction check against exp-083's committed data. **HALT if
   fails** (assert, matching exp-083's own `assert repro_pass` idiom).
4. Compute `sc.widths()` at `BOX_A` and `BOX_B` for every (cfg,θ,leg);
   compute `xi_ext` at both boxes (P4). **HALT before P7 if `xi_ext>0.12`
   anywhere.**
5. Non-negativity assertion on `sigma_abs`/`p_abs_w` (fix 7). **HALT if
   violated.**
6. Synthetic classifier-recovery check (P5). **HALT if any decade-boundary
   case misclassifies.**
7. Settling spot-check (P6), disclosed.
8. Feed `BOX_A`'s `sigma_ext_cells`/`ratio_abs_ext` into
   `ts.absorbed_power_established_ratio` → `ts.mixed_length_scale_regime`
   → `ts.netd_disposition` (P8), applying the pre-committed triage rule if
   any cell departs from UNDETECTABLE.
9. Compute `frac_p_abs(θ)`, cite `frac_contrast(θ)` from exp-083's
   committed `results.json` (read, never hand-typed), classify per P7 with
   the noise-floor gate and the DEGENERATE carve-out applied first.
10. Log aliasing-risk-band membership (fix 10) for the actual angle
    gaps used.
11. Persist every intermediate to `results.json`; write `NOTES.md`'s
    Result/Learned/Next sections after the run, never before.

Zero `lab/` diff planned or permitted this cycle (matches every T28
desk/instrument cycle's own discipline) — every primitive reused
(`Sim`, `materials`, `sections.widths`, `ambient.contrast_from_runs`,
`thermo_sidecar.*`) is already gated; `assert_lab_clean()`-style check
reused from exp-083's own idiom.
