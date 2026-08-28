# exp-084 — Source-Aperture / Article-Rim Fresnel Edge-Diffraction Derivation

Panel Iteration 61. Lead: PHOTONICS (rotation). Zero-FDTD desk cycle.

## Hypothesis

T28's founding periodicity `P_edge_A=2.8421°` (empty-scene `C80−C40`,
exp-069) has, across nine-plus prior mechanism cycles, only ever been
modeled as a **reflection/echo** off the graded-loss `ABSORB` boundary
band — every such model was REFUTEd (exp-078/079/081). This cycle proposed
instead treating the source aperture's own two tapered edges as genuine
near-field **Fresnel/Kirchhoff diffractors** — a mechanism class never
tried in this sub-thread — motivated by the fact that this bench's own
aperture sits at 0.2% of its Fraunhofer distance (deep near-field), where
the already-tested-and-refuted far-field grating formula (`P_edge_B`)
should not be expected to apply.

## Setup

Pure Python desk calculation, zero new FDTD calls. Reused already-
validated machinery: `dg048.field_and_h`/`edge_diffraction_c_empty_
corrected` (exact, non-paraxial 2D scalar Huygens–Fresnel sum),
`dg065.CONFIGS` (canonical T28 geometry), `run69._free_period_search` and
`ywp.free_period_with_widening` (the sub-thread's own established
free-period-fit machinery). Predictions pre-registered and committed to
git (`c714ad5`) strictly before `phase1_derivation.py` was written —
house discipline restored for a second consecutive cycle. Two legs: (a)
the source aperture's own two edges, scored against `P_edge_A`; (b) the
article's own rim edges (a two-stage propagation), scored against
exp-083's `P*=2.9474°`.

## Result

**Leg (a): INCONCLUSIVE on the period match** (corrected at Phase 3 from
an initial, incorrect self-scored SUPPORT — see `phase3_synthesis.md` for
the full reasoning). The model curve's free-fit period (`P_model_a=
2.5338°, R²=0.3697`) nominally cleared the pre-registered SUPPORT band
(`rel_dev=0.1085`), but Red Team's Phase-2 audit — and this Director's own
third, independent re-run (`phase3_fix_docket_checks.py`) — showed
`R²=0.3697` is met or exceeded by 50.0% of the real curve's own
order-preserving circular shifts (this program's established "harder
companion" null test): the fit sits at the null distribution's median, not
a rejection tail. VISION's own pre-registered T21-decorrelation escape
test, run to its conclusion, independently mandates the same downgrade.

**But a genuine, independently triple-confirmed positive finding
survives**: the model curve's raw *shape* correlates `r=+0.958` with the
real FDTD `C80(θ)` empty-scene curve — far above any control (leg (b)'s
own real output `r=−0.10`, a bare linear ramp `r=−0.33`, a bare quadratic
`r=−0.55`). A zero-FDTD, vacuum-only diffraction integral over the source
aperture's own two tapered edges reproduces ~92% of the real curve's
variance in raw shape — real signal, not a generic "any two smooth curves
correlate" artifact.

**Leg (b): NO VERDICT (instrument-validation failure), not REFUTE.** The
article-rim two-stage propagation's own pre-registered Anchor 2 (a
composition-of-propagators identity that must hold exactly with the mask
disabled) failed a convergence-checked test (stable mismatch ratio
2.894–2.895 across 1×–8× oversampling — not a discretization artifact).
Two competing causal explanations remain open and undischarged: the
write-up's own guess (a missing Rayleigh–Sommerfeld boundary term) and
EM's independently-verified, better-evidenced alternative (a missing
phase-carrying obliquity/normalization factor — the ratio's own
non-smoothness across angles, `1.47`–`5.66`, argues against a simple
missing real correction and for a missing complex/phase one).

**Checkpoint criterion 4 FIRES** — the third consecutive silent (no stated
reason) deferral of the joint EM/THERMO energy-interception cross-check
(named at Iteration 59, flagged again at Iteration 60 with an explicit
tripwire, silently absent again here). Ruled a notification, not a pause,
matching this program's unbroken 12-for-12 precedent (now 13 for 13). See
LOGBOOK.md's CHECKPOINT entry for this iteration.

## Learned

1. The near-field/Fraunhofer-distance framing (this bench's aperture sits
   deep in the Fresnel regime, invalidating `P_edge_B`'s far-field
   assumption) is a genuinely productive lens — it produced the first
   mechanism in this sub-thread's history to show real shape kinship with
   the actual FDTD physics, even though the specific period question
   remains unresolved.
2. **R10 adopted**: a specificity-over-candidate-targets sweep (R5's
   original form) is not a substitute for an order-preserving
   null-under-noise test — the two can and do disagree sharply on
   identical data. This is now the second consecutive cycle (exp-083,
   exp-084) this exact divergence has been outcome-determining.
3. A composition-of-propagators identity (leg (b)'s Anchor 2) is a cheap,
   powerful self-check for any multi-stage Huygens construction — it
   caught a real methodological gap before a false REFUTE could be
   reported, exactly as the anchor was designed to do.
4. Genuine shape correlation and genuine period significance are
   different questions and must be reported separately — a result can be
   real on one axis and not yet established on the other.

## Idealizations

See `phase1_proposal.md` Section 5 (2D scalar diffraction, not full vector
FDTD; single λ=600nm; near-field Green's-function/Fresnel-integral
treatment, not exact Maxwell; no lossy medium; taper as amplitude
weighting only; CW/steady-state; article rim as two point-like edges).

## Next

1. **Discharge the energy-interception cross-check** (Checkpoint-4-firing
   item) — high priority for Iteration 62, on a cycle with a genuine
   article-loaded scene to reuse (as originally scoped at Iteration 59).
2. **EM's discriminating test** for leg (b)'s Anchor-2 failure: re-weight
   the two-stage construction's stage-2 secondary sources by
   `field_and_h`'s own driven-current obliquity/phase convention before
   crediting either causal story.
3. **THERMODYNAMICS' Anchor 3** (fringe amplitude vs. the
   `graded_black_shell`'s `R≤0.2%` reflectance ceiling) — mandatory before
   any future leg (b) re-attempt.
4. A properly-powered (more than 31 points, or a different window) re-test
   of leg (a)'s shape-correlation finding — does a wider or denser angular
   window let the model curve's own period become distinguishable from
   noise, now that the shape match motivates spending more FDTD-free
   compute on it?
5. Apply R10 retroactively as a checklist item to any future free-period
   or free-phase SUPPORT/CONFIRM claim on this board.
