# Phase 2 Critique — MATERIALS & METAMATERIALS

Seat charter note: T1 is correctly N/A this cycle (pure grid-resolution
instrumentation, no material/mechanism proposed). My stake, per this
cycle's own framing: does the `cpl=20→25` geometry-scaling recipe correctly
preserve the represented MATERIAL LAW (the absorbing shell), and is every
material-parameter scaling choice (`sigma_max`, `ABSORB`/`EDGE`) actually
justified, or merely carried over by naming-convention analogy?

## Independent verification performed

Ran the proposal's own code directly (never trusted its prose numbers):

- `python3 experiments/112-.../run.py --verify-geometry` → `{"pass_": true,
  "mismatches": []}` at both r — confirms `geom_fixedabs_cpl(r,20)` reduces
  byte-exact to the frozen exp-108/110 geometry.
- Independently invoked `geom_fixedabs_cpl(156,20)` vs `geom_fixedabs_cpl
  (156,25)`: physical `R_COAT`=4680nm, `R_CORE`=3240nm, shell thickness
  =1440nm — bit-identical at both `cpl`; `tau_shell`=24.0 exact at both
  (`sigma_max`=0.5×48=0.4×60); simulated optical periods `STEPS·S/lam`=320·S
  exact at both — all match the proposal's own §2.1 table.
- Read `lab/fdtd2d.py` directly (not assumed): the shell's loss enters via
  `alpha = sigma_e*S/(2*eps_r)` (line 215), folded into the Yee `ca`/`cb`
  coefficients — genuinely resolution-covariant. The domain-edge sponge is a
  DIFFERENT mechanism: `self.Ez *= self.damp_e` (line 253), a bare
  per-timestep multiplicative mask with no `S`/`dt` normalization anywhere
  in `_damping()`'s own formula (lines 122-129).
- Computed the sponge's own actual accumulated log-attenuation from its real
  ramp formula, `absorb`=40 vs 50 (`(np.arange(absorb,0,-1)/absorb)**3`,
  coefficient 0.30, `S`=0.32/√2 fixed): **13.93 at `cpl`=20 vs 17.24 at
  `cpl`=25 — a genuine 1.24× increase**, not an invariant.

## Steel-man

The `tau_shell`-preserving `sigma_max∝1/ratio` recipe is not a superficial
borrow — I independently re-derived it from `lab/fdtd2d.py`'s own
normalized-grid update rule and confirmed it analytically cancels: total
shell attenuation crossing `N_cells` cells reduces to `sigma_max·N_cells/
(2·eps_r)`, with the Courant factor `S` cancelling exactly, so it is
genuinely resolution-invariant by construction, not merely asserted. This
is the SAME invariant EM first-principles-derived for the T21/R4 family
(`design_geometry.py` line 300, "holds... optical depth... invariant")
correctly, verifiably (byte-exact, machine-checked) generalized to a
structurally distinct family for the first time — real transferred physics,
not analogy.

## Sharpest attack

The proposal folds `ABSORB`/`EDGE` into the "same congruent-refinement
convention" as `sigma_max` (§2.1, "following the T21/Block-MINI family's
own established convention"), but they do not rest on the same physics, and
the `ABSORB` one is measurably not invariant. `sigma_max`'s resolution-
independence comes specifically from `S` cancelling inside the Yee `ca`/`cb`
coefficients; the sponge (`damp_e`) has no such cancellation anywhere in its
code. Since `STEPS` scales by `ratio` to hold optical-period count fixed, a
wave takes 25% more timesteps to cross the same physical `ABSORB` width at
`cpl`=25 — and I computed the real consequence from the actual formula:
accumulated sponge log-attenuation rises from 13.93 to 17.24 (a genuine
1.24×, `exp(-13.93)=8.9e-7` → `exp(-17.24)=3.2e-8`). Non-fatal only because
both sit ~6-8 orders below the ~1e-4-1e-3 measurement floor the DISCLAIMER
itself names — the boundary gets stronger, not weaker, so it cannot
manufacture the near-field signal under test — but the "same convention"
framing is false as stated, and the Idealizations section discloses only
"not re-derived from a bound," not that this parameter's scaling is
provably non-neutral where `sigma_max`'s is provably neutral.

## Verdict

**support-with-changes.**

## Parameter change that would flip verdict

None needed to flip to outright oppose this cycle — the asymmetry is real
but the direction (stronger absorption) cannot contaminate the named bin's
signal, and no r=312 leg is run here to compound it. The single change I
require before freeze: correct §2.1/Idealizations to state plainly that
`ABSORB`/`EDGE` scaling by `ratio` is NOT backed by the same
resolution-invariance derivation as `tau_shell` — it is a habit carried over
from the T21 family, and it demonstrably strengthens (not merely
"unverified-but-neutral") the domain-edge sponge with `cpl`. The single
change that WOULD flip me to oppose: if a future cycle instead held
`ABSORB`/`EDGE` at a FIXED CELL COUNT while raising `cpl` (shrinking the
sponge's physical/electrical width) — that constant-in-cells mistake, which
this cycle correctly avoids for the shell but does not explicitly rule out
by name for the boundary, would genuinely degrade absorbing-boundary
fidelity AS resolution refines, injecting a confound that grows exactly
where this experiment needs it to stay silent.
