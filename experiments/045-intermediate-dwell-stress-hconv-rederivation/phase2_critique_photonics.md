# PHASE 2 — CRITIQUE · PHOTONICS (blind) · Panel Iteration 22 · exp-045

## Steel-man (≤150 words)

Block B is a disciplined, correctly-executed extension of an idealization
this program has already disclosed and lived with since Iteration 20, not
a new invention. `h_eff=k_air/r_out=0.026/2.34e-6=11111.1 W/(m²K)` is
exact arithmetic (verified by hand) and the right physical regime
(gas-phase conduction at micron scale, per THERMODYNAMICS' own Iteration-20
call). The T22 area table numbers check out exactly too (5.0112e-11 m²,
2.9131×; 5.1843e-11 m², 3.0138× — both matching the established 2.9–3.0×
band). It correctly reuses `steady_state_delta_T`'s proven area-invariance
(PHOTONICS' own Iteration-20 proof) rather than re-deriving it, and cleanly
separates the mass-invariant ceiling from the mass-dependent time constant.
Committing the comparison table closes a real, three-cycle-deferred
obligation (T22) with genuine numbers instead of another deferral.

## Sharpest attack (≤150 words)

Block B silently uses TWO different length scales for the SAME idealized
object. `h_eff` is computed from `r_out=R_OUT_CELLS×dx=2.34µm`, the
bench's real simulated geometric radius. `mass_kg` is computed from
`w_on=SIGMA_EXT_ON×dx=7.079µm` — an *extinction cross-section* width, not
a geometric one. `w/r_out=3.03`, far beyond the ~1.77× a disk-vs-square
shape difference alone would produce (`sqrt(π)`); the residual ~1.7×
linear inflation is exactly this program's own T9 finding that σ_ext
exceeds naive geometric limits (Q_ext≠1, extinction paradox). Narrative
§1 claims both quantities are "derived from the object's own bench
geometry" — false for mass_kg, which is derived from its 600nm *optical
response*, not its physical size. Because mass_kg scales as w³, this
conflation is cubic, not linear. It happens to look "wavelength-safe"
only because this bench article's σ_ext is flat by construction (450nm
238.2, 600nm 236.0, 750nm 241.1 cells, exp-026 `beam_scene`, 2.2%
spread) — an achromatic idealization, not evidence the convention is
sound. Applied to any real dispersive σ(I) host (T18's own standing
finding), a σ_ext measured off-resonance would silently understate a
"first-principles" mass by whatever factor Q_ext departs from 1 at that
probe λ — a nonphysical, wavelength-of-measurement-dependent mass.

## Verdict

**Support-with-changes.**

## Parameter change that would flip to full support

Put `h_eff` and `mass_kg` on the SAME length convention — either both
from `r_out` (real geometric disk) or both from `w_on` (iso_xsec_sq) —
and disclose the resulting factor-of-~3× shift in the mixed-convention
`tau_thermal_s`/dwell-ratio headline (P-EM45-A6) explicitly, rather than
reporting the current mixed-scale number as "first principles."

## Supporting arithmetic (checked by hand)

- `r_out_m = 78 × 30e-9 = 2.34e-6 m`; `h_eff = 0.026/2.34e-6 = 11111.11
  W/(m²K)` — matches proposal exactly.
- `w_on_m = 235.96673494878587 × 30e-9 = 7.0790e-6 m` — matches.
- `w_on/r_out = 7.079/2.34 = 3.025`; shape-only expectation for equal
  area (square side vs. circle radius) is `sqrt(π) = 1.772` — the
  residual ~1.71× is real cross-section inflation, not a disk/square
  bookkeeping artifact.
- σ_ext at 450/600/750 nm (exp-026 `beam_scene`, ON-endpoint article):
  238.219, 235.967, 241.127 cells — 2.2% relative spread, i.e. flat by
  construction (this bench article is a scalar, achromatic σ_e bump, per
  exp-044's own Block-C idealization note), which is why this
  inconsistency does not show up as a numeric problem *this cycle* but
  would for any real dispersive host.
