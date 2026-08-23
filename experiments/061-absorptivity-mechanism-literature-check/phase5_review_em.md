# Phase 5 — ELECTROMAGNETISM blind review (exp-061 / Iteration 38)

*Fresh sub-agent, blind to the other five Phase-5 reviews and to Red
Team.*

## Verdict: PROMISING

**τ_true re-derivation — independently confirmed sound, formula and
arithmetic both check out.**

Derivation from first principles: for complex n = n′+in″, power decays
as exp(−2(ω/c)n″x), giving α=2ω·Im(n)/c and τ=∫α dx=(2ω/c)∫Im(n)dx. In
cell units, ω/c·dx_phys = (2π/cpl)·dx_cells exactly (dx_phys=λ/cpl), so
τ=2·(2π/cpl)·∫_shell Im(n(r))dr_cells — this matches the bench's
established t=σ·cpl/(2π) loss-tangent convention (Red-Team-corrected
from the `sim.omega` units bug at exp-060) with no additional
assumption. The step specifically scrutinized — collapsing
`I_graded=∫₀¹Im(n(σ(d)))dd` into a radial integral by multiplying by 48
cells — requires d linear in r. Read `materials.py::graded_black_shell`
directly: `d = clip((r_out−r)/(r_out−r_in), 0, 1)` is exactly affine in
r (the quintic-smoothstep nonlinearity is applied to σ(d), not to d(r)
itself), so `dr_cells = −thickness_cells·dd` holds identically across
the shell. The multiplication is therefore exact, not an approximation
layered on top of the WKB one — Red Team did not skip a step here.

Reproduced the number from scratch (same n=sqrt(1−it), same
200,001-point trapezoid): I_graded=0.27383977733, τ_true=8.258813.
NOTES.md's published 8.258819829686677 differs at the 6th significant
figure (~8×10⁻⁷ relative) — traced to NOTES.md chaining forward from
I_graded rounded to 6dp rather than full precision; cosmetic, not a
defect, flagging only so nobody mistakes it for a real discrepancy
later.

What the formula genuinely is NOT: a full-wave cylindrical solution.
It's a 1D radial-ray WKB/eikonal treatment — local Im(n(r)) integrated
along one ray, ignoring curvature and any coherent multi-reflection
between radii. NOTES.md's own Idealization 5 discloses exactly this,
correctly. Given T1 escape route: NONE this cycle (no constraint metric
scored) and MP-2 (thickness) being the anchor-invariant deciding axis
regardless of which τ candidate is used, this is the right rigor/cost
tradeoff — concur with Red Team's scoping, not merely its arithmetic.

**Passivity/causality sanity**: σ(r)=σ_max·s(d)²≥0 everywhere, Im(n)>0
for t>0 — an ordinary passive, dissipative (not gain) medium throughout
the shell, consistent with T1's constraints. No reciprocity issue arises
(normal-incidence scalar problem).

**THERMO spot-check**: ran `mixed_length_scale_regime` with the exact
stated inputs (l=150µm, K_AIR=0.026, ρ=2330, c_p=700, ε=0.9,
T_amb=293.15K, the two WitnessScenario irradiances) — reproduced
ΔT=3.6868×10⁻⁴K/54.2× and ΔT=2.4731×10⁻³K/8.1× to 5 significant figures.
Confirmed.

**caveat_lint.py**: ran it — `5 caveat(s) checked, 0 required-site
failure(s)`, exit 0. Confirmed, matches the document's claim.

**T1-scoping check**: NOTES.md's Hypothesis section explicitly excludes
σ(I) switching mechanisms and frames this cycle as "the raw absorptivity
of a passive, always-on absorber, not a switchable one" — correctly
binding `graded_black_shell` outside T1's constraint-1+2+3 escape route
at the point of introduction. `phase4_results.md` restates "T1 escape
route: NONE" at MP-4's and MP-5's own verdict rows, not only at the
document top — the mandatory fix from Red Team's Phase-2 attack #4
actually propagated into Phase 4, not just Phase 3. This scoping holds
everywhere checked.

## Defects found

1. **[cosmetic]** τ_true's published value (8.258819829686677) carries a
   ~8×10⁻⁷ relative drift from full-precision chaining, traced to a 6dp
   rounding of I_graded before multiplying — non-material, but future
   citations of this number to more than 5 sig figs should recompute
   from full-precision I_graded rather than copy-forward.
2. **[pre-existing, not new]** The MP-3/MP-4 mechanism-class judgment
   call (LCD black-matrix film exclusion) — independently affirm the
   exclusion is EM-defensible: `graded_black_shell`'s entire design claim
   (exp-060, empirically confirmed) is index-matched entry with zero
   interface to glint off; a discrete-pigment film in a polymer host
   necessarily has real ε-discontinuities at pigment boundaries, a
   structurally different impedance-matching regime. The exclusion is
   physically correct, not a rationalization.

No defect touches the τ_true derivation's soundness, the THERMO numbers,
or the caveat-lint pass.

## Top-3 candidate directions for Iteration 39

1. EM's queued `sim.omega` historical-units-bug registry entry (Red
   Team's Phase-2 docket item 9) — cheap, closes a real if
   currently-dormant reintroduction vector in the loss-tangent
   convention that τ_true and Fresnel-R both depend on.
2. The closed-form two-region Bessel/Hankel `Q_ext_uniform` series
   (four-seat convergence from exp-060) — would give an independent,
   zero-FDTD cross-check on the same Im(n)/attenuation machinery this
   cycle leaned on.
3. A genuinely attenuation-matched third `uniform_lossy_shell` article
   (t′≈0.566, QUANTUM's flagged item) — turns this cycle's analytic
   Jensen's-inequality correction into an empirically measured one,
   directly exercising the τ_true chain under real FDTD rather than
   desk arithmetic.
