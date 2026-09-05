# exp-112 — Phase 2 Critique — ELECTROMAGNETISM (blind)

Charter: field/wave behavior, impedance matching, energy coupling;
reciprocity/passivity/causality bookkeeping — what T1 permits and forbids.
Read blind, independent of any other seat's Phase-2 output.

## Steel-man (140 words)

The recipe's stated physical-consistency claims are genuinely verified,
not merely asserted, and they are the right invariants. `tau_shell =
sigma_max·(R_COAT−R_CORE)` is held bit-exact at 24.0 by construction; from
`lab/fdtd2d.py`'s own update coefficients (`alpha = sigma_e·S/(2·eps_r)`,
`run()` line 215), the shell's total per-transit optical depth reduces to
`(sigma_max/2)·(R_COAT−R_CORE)`, independent of `cpl`, since `S =
courant_frac/√2` is **bit-identical** at both resolutions (`courant_frac`
unchanged) — so the numerical CFL stability margin is *provably*, not
assumedly, identical between the two legs, and `sigma_max=0.4` carries no
passivity risk (real, positive conductivity stays passive at any
magnitude). `STEPS·S/lam` held at `320·S` confirms identical total
settling time; `ramp_periods·lam/S` scales in lock-step. Domain clearance
(12.2λ, both resolutions, re-derived) and `geom_fixedabs_cpl`'s
byte-exact reduction to `R.geom_fixedabs` at `cpl=20` are genuinely
executed, zero-FDTD checks — not hand-waved.

## Sharpest attack (149 words)

The two stated preconditions don't gate what my charter asks. `sum(sigma_
scat_per_bin)==sigma_scat` is an internal re-partition identity (per
`angular_scattered_pattern`'s own docstring) — it cannot detect a real
resolution-dependent bias. Tracing `lab/fdtd2d.py::run()` (`self.Ez *=
self.damp_e`; `damp_e=exp(-0.30·d)`, `_damping()`, applied every TIME
STEP, not scaled by `dt`), the domain-edge graded-loss band's (VALIDATION.
md's own term — not a true PML) one-way attenuation exponent is
`-(0.3/S)·∫₀^absorb d(x)dx = -(0.3·C/S)·absorb` (`C=∫(1-ξ)³dξ=1/4`) — it
scales with ABSORB's **absolute cell count**, not its wavelength depth.
So although ABSORB/λ is held at 2λ both ways, `cpl=25` (absorb=50) is
1.25× deeper in exponent than `cpl=20` (absorb=40): −16.57 vs −13.26
(`S=0.32/√2`, verified by direct computation). T28's own record (exp-069)
already flagged ABSORB depth as the one parameter that carries real
signal between compared configs — exactly the asymmetry the proposal's
"physical-consistency check" never bounds. My own estimate puts both
residuals ~7+ orders below the ~1e-4 target signal (non-load-bearing) —
but that number is nowhere in the document, an unquantified idealization
on exactly the axis R8 exists to close.

## Verdict: support-with-changes

Mandatory fix: before Phase 4 trusts the named-bin comparison, compute
and print (zero marginal FDTD cost — pure arithmetic on already-known
constants) the graded-loss-band one-way field-attenuation exponent at
both `cpl=20`/`absorb=40` and `cpl=25`/`absorb=50` using the formula
above, and state explicitly that both are orders of magnitude below the
~1e-4 target signal scale — closing the Idealizations section's current
vague "not independently re-derived from a PML-reflectance bound"
disclosure with an actual number, per R8's standard (a named, affordable
check must be run, not merely gestured at). Everything else this seat can
check — `tau_shell` invariance, Courant-margin identity, settling-time
identity, domain clearance, passivity of `sigma_max=0.4` — is genuinely
sound.

## Single parameter change that would flip my verdict

If the mandatory-fix computation above, once actually run, showed the
`cpl=20` and `cpl=25` graded-loss-band residuals differing from the
~1e-4 target-signal scale by fewer than, say, 3–4 orders of magnitude
(rather than the ~7+ my own back-of-envelope estimate finds) — i.e., if
the boundary-condition asymmetry I identified turned out to be
non-negligible relative to the ~9.88% near-null signal under test — I
would flip to oppose: the comparison would then be confounded by an
upstream difference this cycle's own gates cannot see, independent of
whether the −146.25° bin's structure is real.
