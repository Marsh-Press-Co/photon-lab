# Phase 3 — Director's synthesis (exp-061 / Iteration 38)

*Director: cloud panel shift. Resolves the Phase-2 debate into ONE
testable configuration, records which criticisms are accepted/overridden
and why, and freezes predictions to git BEFORE Phase 4 (the actual
literature search + THERMO desk computation) runs — house discipline,
non-negotiable.*

## What Phase 2 produced

Five blind critiques (PHOTONICS, ELECTROMAGNETISM, THERMODYNAMICS,
QUANTUM OPTICS, VISION SCIENCE), all **support-with-changes**, plus a
Red Team audit ruling **PROCEED-WITH-MANDATORY-FIXES**. Full text: the
five `phase2_critique_*.md` files and `phase2_redteam_audit.md` in this
directory.

Two independent, load-bearing, self-verified numeric findings emerged
that neither the Phase-1 proposal nor any single seat's Phase-1 read
caught alone:

1. **PHOTONICS**: the proposal's headline `TAU_SHELL=24` figure
   (`sigma_max × thickness`, a peak-conductivity line-integral) is
   **2.55× larger** than the graded profile's own actual raw σ-line-
   integral for the identical object (9.4026, already computed by
   exp-060 for a matched geometry).
2. **ELECTROMAGNETISM**: even 9.4026 is not a physically meaningful
   absorption coefficient — it is still a raw conductivity integral, not
   a loss-tangent → `Im(n)` → radially-integrated α. EM correctly
   predicted the true correction would move the figure by "tens of
   percent," not flip the qualitative verdict.
3. **RED TEAM**, adjudicating both: computed the actual physically
   correct anchor, `τ_true ≈ 8.26`, from a number *already sitting in the
   record* — exp-060's own committed `∫₀¹ Im(n(σ_graded(d))) dd =
   0.273840` — at zero marginal FDTD/network cost. This is neither
   seat's proposed fix; it is stricter than PHOTONICS' (uses `Im(n)`, not
   raw σ) and cheaper than EM's (reuses an existing number instead of a
   fresh derivation).

Independently re-verified by the Director (not hand-copied — R4):

```
tau_true = 2*(2*pi/20)*48*0.273840 = 8.258819829686677
alpha_true = 8.258819829686677 / 1440nm = 0.0057353/nm = 5.7353e4 cm^-1
e-fold length = 174.36 nm   (was 60.00 nm at the original tau=24 anchor)
```

## Accepted criticisms

- **PHOTONICS' core finding (τ mis-derivation)** — accepted, but
  Red Team's `τ_true≈8.26` anchor is adopted in place of PHOTONICS' own
  proposed fix (9.4026), which under-corrects (still a raw-σ integral,
  not `Im(n)`-weighted).
- **EM's core finding (α needs a proper loss-tangent/`Im(n)` bridge, not
  a length-unit bridge alone)** — accepted in substance; Red Team's
  `τ_true` derivation IS that bridge, computed from an already-published
  number rather than a fresh derivation, closing EM's own concern at
  lower cost than EM itself proposed.
- **THERMODYNAMICS' demand for a mandatory Phase-3 disposition box** —
  accepted, **in the stronger unconditional form Red Team ruled** (not
  THERMO's own conditional flip-clause, which Red Team judged
  near-vacuous given MP-5's fallback keeps a design candidate alive under
  nearly every realistic outcome). Computed below.
- **QUANTUM's demand for explicit classical-parameter scoping +
  coherence/localization fallback** — accepted as stated.
- **VISION's finding (the tool's own T18-propagation gap, live inside
  this cycle's own document)** — accepted; new registry entry added
  (`exp061-t18-evidentiary-tier-propagation`), required site is this
  cycle's own `NOTES.md`. Red Team ruled this does NOT fire Checkpoint
  criterion 4 (a registration gap self-caught pre-freeze is a different
  defect species than a docketed propagation promise broken by hand-
  review) but set a binding forward tripwire: a recurrence of this exact
  shape **after** this cycle's own fix lands would auto-fire criterion 4.
  Director adopts this tripwire without qualification.
- **QUANTUM's registry gap (sigma_flat corrected-bias-direction)** —
  accepted; new registry entry added
  (`exp060-sigma-flat-corrected-bias-direction`), verified PASS against
  the live tree.
- Red Team's own attacks #3 (MP-4's dual-axis ambiguity), #4 (MP-5's
  missing inline T1/constraint disclaimer), #6 (self-test summary
  overstating scope), #7 (MP-3's missing evidentiary-tier scoping) — all
  accepted, applied below in `NOTES.md`.

## Overridden / deferred criticisms

- **EM's own proposed fix** (a fresh, full radial loss-tangent
  derivation) is overridden in favor of Red Team's cheaper, already-
  published-number derivation — EM's own hedge ("plausibly enough to
  matter... but not obviously enough to flip MP-4") is honored: the
  correction is applied, but no new FDTD or fresh symbolic derivation is
  spent chasing a number that Red Team showed (via MP-2's own anchor-
  invariance) does not decide the qualitative verdict.
- **PHOTONICS' own proposed fix** (9.4026) is overridden by Red Team's
  stricter `Im(n)`-corrected figure (8.26) — PHOTONICS' finding that 24
  was wrong stands and is credited; its specific replacement number does
  not ship.
- **EM's `sim.omega` historical registry entry, THERMO's T25 sidecar-
  absence entry, PHOTONICS' numeric-value-consistency-check tooling
  gap** — all real, all deferred per Red Team's ruling (§6 of the audit):
  no live reintroduction vector for the first, lower urgency for the
  second, and the third is new tool machinery, not a one-line registry
  fix. Queued explicitly in `NOTES.md`'s Next section so they are not
  lost to the exact "un-registered gap" failure mode this cycle's own
  Phase 2 just demonstrated.

## THERMO disposition box (mandatory fix 4, computed this Phase)

Desk-only, `lab/thermo_sidecar.py` calls, post-run analytic per the
THERMO expressibility contract (no FDTD). Question: if MP-5's own
fallback resolves TRUE (a real CNT-forest-class coating supplies
`graded_black_shell`'s required optical depth, but only at MP-2's
predicted 15–150µm thickness rather than the 1.44µm this program's
`fixed-absolute-thickness` construction builds), is the resulting object
still thermally UNDETECTABLE at witness scale, under conservative,
worst-case assumptions?

**Worst-case construction** (deliberately over-conservative in every
free choice, so a PASS here is robust):
- `l_geometric_m = 150e-6` (MP-2's own predicted UPPER thickness bound,
  taken as the object's full outer radius — larger, and hence a worse
  cooling case, than the ~150.9µm a literal core+shell sum would give).
- `ratio_abs_ext = 1.0` (100% absorption ceiling — well above the
  established 0.51–0.61 measured ratio family this program actually
  uses; deliberately the most conservative choice, not a measurement).
- `area_m2 = l_geometric_m**2` (the same `iso_xsec_sq` convention
  `thermo_sidecar.py` already uses elsewhere).
- Two irradiance points, both from the program's own sourced
  `WitnessScenario` (docket #7, exp-043): **central** 6.58×10⁻⁶ W/cm² and
  **worst-case (upper bound)** 4.414×10⁻⁵ W/cm².
- Material provenance: silicon (ρ=2330 kg/m³, c_p=700 J/(kg·K)),
  `ASSUMED — provenance terminates unsourced (T18)`, identical disclosed
  caveat this program has carried since Iteration 23 — reused verbatim,
  not newly asserted.
- NETD band: (0.020, 0.050) K, exp-043's own sourced figure.

```
p_abs_ceiling(central)      = 6.58e-6 W/cm2 * 2.25e-4 cm2 * 1.0 = 1.4805e-09 W
p_abs_ceiling(worst-irrad.) = 4.414e-5 W/cm2 * 2.25e-4 cm2 * 1.0 = 9.9315e-09 W

mixed_length_scale_regime(p_abs_ceiling(central), l=150e-6m, ...):
    dt_ss_full_K = 3.6868e-04 K   -> margin vs NETD_lo(0.020K) = 54.2x   -> UNDETECTABLE

mixed_length_scale_regime(p_abs_ceiling(worst-irrad.), l=150e-6m, ...):
    dt_ss_full_K = 2.4732e-03 K   -> margin vs NETD_lo(0.020K) = 8.1x    -> UNDETECTABLE
```

**Result: UNDETECTABLE at both irradiance points, even under a
ceiling absorption ratio, worst-case irradiance, and MP-2's own upper
thickness bound simultaneously.** The tightest margin (8.1×, worst-case
irradiance) is comfortably clear of the standing NETD band. This is a
genuine, if modest, informative finding: MP-5's own "PLAUSIBLE at
15–100× thickness" fallback does not open a new thermal-detectability
risk for this program's own standing constraint-4-adjacent NETD channel,
under deliberately pessimistic assumptions. It does **not** bear on
constraint-3/4's human-eye verdict (NETD is an instrument threshold, per
`thermo_sidecar.py`'s own standing disclaimer, restated here).

Wien peak (informational only, both irradiance points land within
~10⁻⁴K of ambient): ≈9.88 µm — deep thermal-IR, consistent with every
other UNDETECTABLE finding this program has logged since Iteration 20.

## What ships to `NOTES.md` (frozen predictions, BEFORE Phase 4 runs)

See `NOTES.md`, this directory — the master document, superseding
`phase1_proposal.md`'s own numbers where corrected (that file is left
as-is, a historical record, per house convention: errata are flagged,
not silently rewritten).
