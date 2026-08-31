# Phase 2 Critique — MATERIALS & METAMATERIALS

*Blind review of `phase1_proposal.md` (exp-096, Panel Iteration 73). T1
route N/A / realizability N/A this cycle (instrument-validation, not a
material/mechanism claim) — critique applies discipline-lens scrutiny to
the proposal's own construction/coverage claims instead, per the assigned
charter note.*

## Steel-man (≤150 words)

The gate is well-scoped, zero-FDTD, and correctly targeted: it fills the
one call-site axis — `angle_deg`/`sim.lam`/the phase-ramp array — that
Gate 5 (adopted Iteration 71) has never checked, having only ever verified
`sigma_e` magnitude. Its scope claim is accurate: I independently read
`lab/materials.py` and confirm `dielectric_cylinder`/`pec_disk`/
`graded_black_shell`/`uniform_lossy_shell` write only to `sim.eps_r`,
`sim.sigma_e`, `sim.pec`, `sim.objects` — never `sim.lam`, `sim.sources`,
or `sim.source_specs` — so skipping materials construction loses no
coverage of *this specific check's own assertions*. The three
fault-injection scenarios (§2b) are well-chosen against the actual
plausible defect shapes (family/`cpl` swap, adjacent-job angle mixup, sign
flip), and Option A's `construct_only` reuses the real production call
path rather than a hand-duplicated mirror, closing the drift risk named
in Idealization 34.

## Sharpest attack (≤150 words)

Every "intended" value the gate checks against (`theta`, `cpl_intended`,
`y_lo`/`y_hi`, `x`) — and, for Gate 5, `cx`/`cy`/`PEC_R_R{n}`/`R{n}_R_OUT`
— is pulled from `R{n}_CONFIGS`, itself produced entirely by the single
mechanical `r{n}_config()` recipe. Verified directly in
`design_geometry.py`: `R3_CONFIGS`/`R4_CONFIGS`/`R5_CONFIGS` are
module-level calls to `r3_config()`/`r4_config()`/`r5_config()`,
substituting only `RATIO`, and Gate 5's own `shell_mask` is computed with
the *same* `cx,cy` variable passed to the builder it is checking. So both
gates verify only that the recipe's own output reached `Sim()`/`sigma_e`
unchanged — never that the recipe's output is itself correct. They catch
a caller-level plumbing bug (exactly what FI-A/B/C inject) but are
structurally blind to a defect baked into the shared recipe — precisely
the live hypothesis Idealization 17, carried into this very proposal,
names. §5a's claim that CLEAN "removes construction-time
wiring/registration as a live explanation... entirely" therefore
overclaims: it removes only the caller-plumbing subclass, leaving the
recipe-level subclass — arguably the more probable one, since it would
explain a *uniform* six-point reversal — untouched.

## Verdict

**Support-with-changes.**

## Flip

Reword §5a's CLEAN branch to state explicitly that a CLEAN result rules
out only a *caller-level* plumbing defect (the class FI-A/B/C actually
demonstrate), not a *recipe-level* one shared by construction across
R3/R4/R5 — and add, as a companion (still zero-FDTD) check, one
independently-coded recomputation of at least one R4 `y_lo`/`y_hi`/`cx`/
`cy`/`src_x` value directly from the native (`cpl=20`) base constants and
`RATIO`, outside the `r{n}_config()` code path, before this cycle is
credited with closing "the single most fundamental unresolved question."
Without that, the proposal is fine to run as a cheap first move but should
not be allowed to retire the registration hypothesis on its own.
