# exp-079 — T28 Y-Wall Full (Non-Edge-Reduced) Aperture Sum

**Panel Iteration 56.** Lead: MATERIALS & METAMATERIALS (by rotation).
Director synthesis post Phase 2 (five blind critiques + Red Team's Phase-2
audit, verdict **PROCEED-WITH-MANDATORY-FIXES, 9-item docket, ALL 9 items
ADOPTED, ZERO overridden** — full record in `phase1_proposal.md`,
`phase2_critique_{vision,photonics,em,thermodynamics,quantum}.md`,
`phase2_redteam_audit.md`, `phase3_synthesis.md`). Phase 5: six blind
reviews (unanimous PARTIAL) + Red Team's final audit (PARTIAL, one
substantial cross-seat synthesis — see below).

## Mandate

`experiments/078-.../phase5_redteam_audit.md` §7 Tier 0 item 1 — the
reconciled Iteration-56 ranking's single highest-value item on the whole
T28 board: does exp-078's own flat/zero-amplitude single-edge result
generalize to the FULL, non-edge-reduced y-mirrored source aperture sum?

## Hypothesis

exp-078's single-point (near-edge-only) reduction, evaluated at its own
rigorous stationary-phase bounce angle, predicted exactly zero signal —
but a real source aperture is ~1,504 coherently-driven cells, not one
point. Each aperture point has its own per-point rigorous bounce angle
(`theta_local(y_s)=atan(D_SP/(OBJ_Y+y_s))`, a natural generalization of
exp-078's own single-point formula) and its own driven, `theta_beam`-
dependent phase. Hypothesis (per exp-078's own §3.2 stationary-phase
argument, never previously computed): edge-domination should hold for the
full sum too, and the flat result should survive.

## Setup

Reuses committed machinery programmatically throughout (R4 discipline):

- **Geometry/aperture**: `experiments/065-.../design_geometry.py::CONFIGS`;
  `lab/fdtd2d.py::Sim.add_line_source`'s own raised-cosine taper and
  driven-phase convention, re-derived from that function's own source.
- **Reflectance/gates**: `experiments/075-.../boundary_reflectance.py`,
  plus a vectorized-over-theta re-implementation (validated bit-exact
  against the scalar, already-gated function before use).
- **Period fitting**: `experiments/078-.../y_wall_prescreen.py`'s own
  `free_period_with_widening` (including its `SS_TOT_DEGENERATE` guard).
- **Real data**: `experiments/076-.../results.json::headline`.
- **Pre-registered band**: Test A (period) only, reused verbatim from
  exp-075/077/078.

## Result

**The flat result does NOT generalize — but the recovered `theta_beam`-
dependence cannot discriminate a real y-wall echo, at any period a
slowly-varying reflectance could produce, from no echo at all.**

Official Test-A (unchanged since Phase 1, verified bit-exact through every
phase): 1/3 nominal SUPPORT (`C80−C40`, `rel_dev=0.2857`, non-informative
per the reflectance-ablation control), 0/3 REFUTE, 2/3 INCONCLUSIVE
(primary `Re{E_echo}` proxy); 0/3 SUPPORT (secondary `|E_echo|` proxy). A
real, well-converged, non-degenerate oscillation reappears (`ss_tot` ratio
`9.4×10⁻⁷`, `≈20.2` orders of magnitude above exp-078's own `5.9×10⁻²⁷`
ratio) — the strict single-edge flatness does not survive.

**But this cycle's own central finding (Red Team's Phase-2 audit,
independently confirmed three ways — EM analytically, QUANTUM empirically,
Red Team's own from-scratch re-run, then independently confirmed a fourth
time at Phase 5 against a SECOND, materially different admittance family,
MATERIALS): the recovered dependence is structurally, not merely
empirically, uninformative.** Both `theta_local(y_s)` and the image
propagation distance are, by construction, pure functions of static
geometry with zero `theta_beam` dependence — so `E_echo`'s entire
`theta_beam`-dependence is the spatial Fourier transform of a `theta_beam`-
independent envelope, evaluated at `k·sinθ_beam`, governed by the shared
aperture window's own T21-family content regardless of the wall's true
reflectance. A committed reflectance-ablation control (`r(theta_local
(y_s))→1`, zero wall physics) makes this directly checkable: `PAIR_PAD`/
`C80−C40`'s periods survive UNCHANGED (`|ΔP*|≤0.023°`); `PAIR_ABSORB40`'s
ablated delta is EXACTLY zero (`G40`/`C80` share identical geometry under
`PAD=40`), meaning that one pair's real signal genuinely does require
`ABSORB`-dependence — but even it still lands on T21's own period, not
T28's. A real echo at T28's own period, had one existed, would have been
just as invisible to this instrument as no echo at all.

**Phase 5 addendum:** QUANTUM correctly narrowed the "at ANY period" claim
to `r(θ)` slowly-varying relative to the aperture window — proven, before
Phase 5, only for the matched-admittance model. MATERIALS, independently
and from a different starting question, had already run the concrete
alternative QUANTUM names (the realizable `μ_r=1` admittance, at this
cycle's own wide `[4.77°,15.50°]` envelope) end to end and found the
practical conclusion survives (`≤0.015°` period shift, no verdict flips)
despite the underlying admittance correlation collapsing far more than an
inherited exp-078 citation implied (Pearson `r` `0.74–0.88`, negative at
one depth). Idealization 9 is scoped, not retracted, by Red Team's final
audit — see `phase5_redteam_audit.md` §2 for the full reconciliation.

## Learned

1. **A construction can recover real, non-degenerate `theta_beam`-
   dependence and still be structurally incapable of answering the
   question it was built to answer.** This is a sharper, more useful
   negative than either "flat" (exp-078) or "matches a known-different
   frequency" (this cycle's own as-filed framing) alone — it identifies
   *why* an entire per-point-image construction family cannot resolve a
   real-vs-no-echo question, not merely that two attempts within it
   didn't.
2. **A reflectance-ablation control (wall physics on/off) can be a
   sharper, more decisive test than a generic R5 null-permutation
   control** for the specific question "does this signal depend on the
   mechanism at all" — Red Team's own ruling this cycle, matching
   QUANTUM's own independent judgment that the standard control was the
   wrong tool here.
3. **Two independently blind Phase-5 seats, working from different
   starting questions and neither seeing the other's work, can jointly
   close a scope gap that neither alone resolves** — QUANTUM's theoretical
   narrowing and MATERIALS' empirical re-run answered the same underlying
   question from opposite directions; reconciling them (not merely
   adopting one or the other) is what actually closed the gap.
4. **A "corrected" label needs independent re-verification even when a
   prior phase's own record claims the fix landed** — two items this
   cycle's own Phase-3/4 record described as already closed (a stale
   R5-disclosure cross-reference; an inherited admittance citation) had
   not actually been applied when Phase 5 checked; Red Team's own audit
   catching this, rather than trusting the label, is what kept Checkpoint
   criterion 4 from firing on a genuinely close call.
5. **A recommended "next instrument" can itself carry an unproven
   physical assumption that deserves a cheap pre-check before it is
   built** — EM's near-field/Fraunhofer-distance challenge to the
   plane-wave/global-steering construction this cycle's own ranking
   recommends is a real, quantified concern (the y-wall lacks the exact
   cancellation symmetry that makes the x-wall's own analogous reduction
   valid at any range), sequenced ahead of PHOTONICS' own concrete build
   sketch rather than dismissed or deferred past it.

## Next

Reconciled Iteration-57 ranking (Red Team's Phase-5 final audit, 4 tiers,
11 items; `phase5_redteam_audit.md` §7 has the full text). **Tier 0 — zero
FDTD, run as one batch:** (1) EM's cheap validity pre-check of the
plane-wave/global-steering y-wall construction (Fraunhofer margin +
effective-angle-vs-full-envelope test), run BEFORE building it, immediately
followed by PHOTONICS' own concrete build (with its own pre-registered
prediction: still-T21-proximate, `ABSORB`-tracking offset) if the
pre-check does not foreclose it — the single highest-value item on the
board; (2) re-run the smoothness check against the realizable admittance
at this cycle's own full envelope, more targeted than the Pearson-r
correlation already run; (3) the still-unexecuted x-wall realizable-
admittance refit — now the single oldest-deferred MATERIALS item on the
whole board, three cycles running; (4) a period confidence band for this
cycle's own T21-proximity claim; (5) derive the taper's own diffraction
overtone against PHOTONICS' 2.55° residual (low priority, five orders of
magnitude too small to matter); (6) this cycle's own record-hygiene docket
(done, this shift). **Tier 1 — cheap FDTD:** (7) the full-width non-aliased
`G40` leg (now deferred FOUR consecutive cycles); (8) broadband pulsed
reflectance spectroscopy of the `ABSORB` boundary; (9) the 750nm x-wall
two-wall spot-check (the single oldest-unexecuted item on the whole T28
board). **Tier 2 — the standing charter-relevant test, now the single most
overdue item on the board:** (10) whether the `PAD`-sensitivity axis
survives with a real absorbing article loaded — now deferred FOUR
consecutive cycles; this cycle's own Phase 3 finally supplied the explicit
scheduling reason exp-078's own ranking demanded (see `phase3_synthesis.md`
§4b), but the underlying deferral itself continues; if Iteration 57 defers
this a fifth time, the reason should again be stated explicitly. **Tier
3 — governance:** (11) Checkpoint criterion 2 (mechanism-class boundary)
ruled NOT YET RIPE this cycle — the plane-wave/global-steering
construction, the x-wall realizable-admittance refit, and the wavelength-
generality leg remain genuinely open. Full record: this directory;
LOGBOOK.md Iteration 56; PLAN.md's own Iteration-57 queue.
