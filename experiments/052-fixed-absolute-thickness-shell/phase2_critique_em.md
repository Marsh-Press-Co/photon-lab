# ELECTROMAGNETISM — Phase 2 Critique, Iteration 29

**Steel-man:** The mechanism argument is legitimate on the axis that actually
governs near-field diffraction (T8/T12): the Fresnel number is set by
`r_out` and `PLANE_DX`, both held bit-identical to the self-similar family
at every κ — the outer edge-diffraction/fringe geometry (T21's own
mechanism) is genuinely unperturbed by `r_in`'s growth, since `r_in` is
buried inside an already τ_shell=24 (~e⁻²⁴) wall. T9's own established null
result (Δσ_abs/σ_ext=1.56×10⁻⁶, PEC-core-vs-rim) shows core content doesn't
move the aggregate absorption ratio at the one r_in/r_out it was tested at,
and the shell profile itself (48 cells, 2.4λ, same σ_max, same smoothstep
law) is bit-identical at every r_out — whatever local-extinction physics
made the r=78 leg trustworthy is genuinely, not just formally, unperturbed
by this construction.

**Sharpest attack:** The proposal never states which core-fill convention
builds `absorber` at r=156/312 — and it matters. exp-030's own convention,
which §2a's reuse and P-0's bit-identical r=78 check commit to, is HOLLOW
(no `pec_disk` call in `build_ambient()`); exp-031 itself later flagged this
as NOT historically correct, restoring PEC to "match
exp-001/020/024/025/027" instead. T9's "PEC-presence is incidental" null
(Δσ_abs/σ_ext=1.56×10⁻⁶) was measured on the PEC-cored construction
(exp-027) — not the hollow one this proposal actually reuses — so the one
result licensing "the core doesn't matter" was never established for this
object, at this or any r_in/r_out. At r=312 a hollow r_in=264 core is a
~13λ vacuum cavity behind an already-attenuating wall — an unexamined
resonant-coupling risk. No reciprocity/passivity/causality violation (σ≥0,
non-gyrotropic, LTI) — this is an unaddressed interior energy-coupling gap,
not a T1 breach.

**Verdict:** support-with-changes

**Parameter change that would flip verdict (optional):** Pin the core-fill
convention explicitly in run.py (adopt exp-031's PEC-cored construction,
since a real coating implies a solid backing substrate, and it is what the
R-gate's own `coated_wall_r_gate` already tests against) AND add one
radial absorbed-power ledger check (T9's own `exp-028` instrument) at
r=156 or r=312 confirming Δσ_abs/σ_ext stays negligible at r_in/r_out≈0.69–
0.85 — not assumed by extrapolation from the single 0.385 point T9 actually
measured.
