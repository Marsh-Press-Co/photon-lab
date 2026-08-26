# PHASE 2 — CRITIQUE · PHOTONICS seat · Panel Iteration 52 (exp-075)

*Fresh sub-agent, PHOTONICS charter (PANEL.md seat 1: surface interaction,
absorption spectra, angular dependence, scattering cross-sections — is the
proposal's optical response coherent as stated, across wavelength and
angle?). Blind to the other five seats' Phase-2 critiques. Independently
re-ran `boundary_reflectance.py` and re-derived the key formulas by hand
before writing this.*

---

## Steel-man (148 words)

The optics is sound where it matters most. I independently re-solved the
coupled 2D friction PDE (`dEz/dt=c(dHy/dx−dHx/dy)−ν(x)Ez`, etc., with `ν(x)`
acting identically on `Ez`, `Hx`, `Hy`) at oblique incidence rather than
trusting the "vacuum-Snell substitution" as merely borrowed: it reproduces
`kx(x,θ)=k0√(n(x)²−sin²θ)` *exactly*, not as an assumed generalization — so
Idealization 3/4 is more solid than the proposal gives itself credit for.
The `n(x)=1−iν(x)/ω` exact-quadratic identity is real algebra, correctly
flagged as exact rather than small-loss. The sign ambiguity (§2b) is
resolved by the right physical principle (passivity), not curve-fitted to
the target data, and G-LOSSLESS/G-N1/G-PASSIVITY are genuine,
hand-independent checks — a real transfer-matrix TMM, not a Born stub. The
zero-free-parameter, pre-registered-before-comparison discipline is
followed correctly (R4).

## Sharpest attack (150 words)

The single `-x`-wall echo is the *wrong* boundary-reflectance geometry to
have tested first, and the proposal's own numbers show it. Both domain
edges are PEC by construction (`Ez[1:-1,1:-1]` update — index 0 **and**
`nx-1` never touched), so a full-cavity round trip between the `-x` **and**
`+x` walls is at least as natural a candidate as the single `-x` echo. I
back-solved the needed round-trip length at θ=39°, λ=20 cells: `D_needed ≈
320` cells to hit `P*=2.8421°`. `PLANE_X` (the tested model's length scale)
gives 77–117 cells → predicted 7.8–11.8° (REFUTE, 3–5× off, as reported).
But `nx`, the full domain width available in the SAME committed geometry
(`design_geometry.py::CONFIGS`), is 360–440 cells across `ABSORB`=40–80 —
using `nx` alone as `D` gives 2.07–2.53°, **within the proposal's own
SUPPORT band (≤30% of 2.8421°)**, at zero extra FDTD cost. This
cavity-resonance variant was named in Idealization 6 but never priced,
despite sitting one closed-form line away and landing far closer than the
tested mechanism.

## Verdict: **support-with-changes**

The transfer-matrix derivation itself, the sign resolution, the passivity
gates, and the REFUTE of the specific single-`-x`-wall-echo mechanism are
all sound PHOTONICS physics and correctly executed — I would not overturn
that REFUTE for the mechanism as tested. What I cannot support as written
is §5's framing that this "narrows the remaining candidate space" for
graded-boundary-reflectance mechanisms generally: the untested two-wall
cavity variant is not a minor residual idealization, it is a same-cost,
same-machinery closed-form check whose length scale lands inside the
proposal's own falsification band where the tested variant misses by 3–5×.
Idealization 5/6 should be split out and explicitly re-ranked ahead of
"mechanism space narrowed," not filed as a deferred footnote.

## Parameter change that would flip my verdict to plain "support"

Compute (same script, same zero-FDTD budget) the two-wall cavity
reflectance/interference prediction — treating both the `-x` and `+x` PEC
walls' graded `ABSORB` bands as a coupled two-mirror system rather than a
single echo — and report Test A/B against it explicitly, even if it also
REFUTEs. Absent that one additional closed-form calculation, "REFUTE"
reads as stronger than what was actually shown.
