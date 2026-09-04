# PHASE 2 — CRITIQUE · MATERIALS & METAMATERIALS · Panel Iteration 87 (exp-110)

Blind to all other seats' critiques this cycle. MATERIALS led the immediately
preceding cycle (Iteration 86, exp-109); no re-proposal of any R1–R26 idea.

## Verification performed

**(a) Item 1a geometry, byte-for-byte.** Independently re-derived
`geom_fixedabs(156)`/`geom_fixedabs(312)` from the formula chain in
exp-108's own `run.py` (`k=r/78`, `N0..STEPS0` scaled by `k`, `R_CORE =
R_COAT-ABS_THICKNESS`, `ABS_THICKNESS=48` and `SIGMA_MAX_FIXED=0.5` held
constant) and confirm every constant in the proposal's item-1a table
(N/CX/CY/SRC_X/STEPS/R_CORE/R_COAT at both r) matches exactly. The
proposal's predicted reproduction values (σ_abs/σ_ext = 279.6607/560.1989
at r=156, 588.0218/1191.3259 at r=312) are read verbatim, correctly, from
exp-108's own committed `results.json`. `chunk_runner.py`'s `build_sim()`
(materials calls, source angle/profile) is unmodified. **Confirmed
byte-for-byte identical to exp-108's own already-realized fabrication
parameters** — no subtly different structure found.

**(c) R13+R14 joint-gate claim.** `local_rel = |pattern_delta|/|pattern_
peccored|` is a ratio whose denominator (`pattern_peccored`) is a signed,
per-bin Poynting-flux quantity (`sections.angular_scattered_pattern`,
confirmed from source: `flux = sx/sy` of `Re(Ez·Hy*)`, not a magnitude) —
genuinely R13-shaped: a diffraction pattern with real interference nulls
(30/48 bins <1% of peak, exp-108's own PHOTONICS finding) is exactly the
"independently knowable to pass through/near zero" template R13 was
founded on. Floor-gating `pattern_peccored` against the mirror-noise floor
correctly discharges R13. **R14 is mislabeled.** R14's own minimum
discharge (a) requires verifying the numerator's parent curves are
individually *smooth/monotonic* — its founding case was a slowly-varying
θ-sweep. Here `pattern_peccored(θ)`/`pattern_hollow(θ)` are physically
multi-lobed diffraction patterns; they are not smooth by construction, and
per-bin floor-clearance (a point check) is not curve-level
smoothness/registration verification. The proposal claims discharge of a
criterion it does not actually apply.

## Steel-man (150 words)

The re-capture is the right move and is honestly self-audited: §0.5's
three-way verification (scratch-path gone, committed JSON lacks the
per-bin arrays, exp-108's own Phase-5 record timestamps when the pickles
were last live) is exactly the kind of "verify, don't assume" discipline
this program's own R4/R9 lineage demands, and it is the correct read —
independently reproduced above. The mirror-symmetry floor is a genuinely
clever zero-new-assumption instrument for THIS bench specifically: the
target is analytically circularly symmetric, CY=N/2 lands the material
grid exactly on a mirror axis, and `graded_black_shell`/`pec_disk` depend
only on radius — so the floor it measures really is discretization
artifact, not signal, for the simulated geometry as built. Scoping the
output as informational-only (not folding into item i's frozen CONFIRM)
is the correct, R24-lineage-aware caution given this is a first-use
instrument.

## Sharpest attack (150 words)

The mirror floor silently assumes the fabricated article is exactly what
the FDTD idealizes: a PEC core perfectly concentric with an azimuthally
uniform graded coating. Nothing in §5's Idealizations says this floor is
a *numerical/discretization* noise floor, not a *fabrication-tolerance*
one — and the two are not remotely the same scale. `graded_black_shell`'s
own docstring names its physical referent as a CNT-black-style sponge
coating; real dip/sputter-coated shells carry azimuthal thickness/dose
non-uniformity at the percent level from deposition and gravity effects,
plus core-eccentricity from molding/machining tolerance — both orders of
magnitude above the ~1e-9–1e-4-scale floor `rel32` already shows this
channel resolves to. A bin clearing `K·mirror_floor` here says nothing
about whether the SAME asymmetry would survive in a physically realized
shell; a future citation reading "cleared the floor" as bearing on
realizable angular-pattern reproducibility would be exactly R9's
unit-mismatch failure shape, recurring.

## Verdict: SUPPORT-WITH-CHANGES

Item 1a's geometry fidelity is genuinely verified, not merely asserted.
The R13 half of the joint-gate claim is sound. Two textual fixes needed
before Phase 3, both zero-FDTD:

1. Idealizations: state explicitly that `mirror_floor` characterizes
   grid-discretization/floating-point noise for the IDEALIZED simulated
   geometry only, and is not a fabrication-tolerance bound — a bin
   clearing it does not license any inference about a physically realized
   coated-disk's own achievable angular-pattern symmetry.
2. Correct "discharging R13 (denominator) and R14 (numerator-parent
   smoothness) in one gate" — R14 is not discharged by a per-bin floor
   check; either drop that half of the claim or add the actual R14(a)
   verification (confirm `pattern_peccored(θ)`/`pattern_hollow(θ)`, among
   RESOLVED bins, carry no sign-bookkeeping/registration artifact —
   distinct from, and in addition to, the floor gate).

## Single change that would flip to SUPPORT

Add idealization sentence 1 above (the discretization-vs-fabrication-floor
disclaimer). That alone removes the one gap capable of silently
mis-informing a future realizability citation; the R14-labeling issue is
real but currently harmless since the diagnostic is disclosed as
informational-only and un-scored.
