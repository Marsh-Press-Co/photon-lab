# PHASE 2 — CRITIQUE · VISION SCIENCE · Panel Iteration 26 (candidate exp-049)

*Blind parallel critique. Charter: human perceptual limits — contrast
thresholds, luminance edge detection, spectral sensitivity, adaptation,
temporal sensitivity. Duty: pin numeric thresholds, with sources, BEFORE any
run that scores against them. This cycle pins none — it reuses my own frozen
T2 bar (C_THR=0.005, the photopic floor of C_thr(L)=0.005·max[1,(L/3)^−p])
as a fixed decision line and issues no new perceptual claim (idealization 9).
That framing is checked below, not re-litigated.*

---

## Steel-man (≤150 words)

Methodologically clean reuse of my own instrument. C_THR=0.005 is cited to
its exact source (`run.py:41`) and used only as a fixed comparator, never
re-derived, re-scoped, or re-interpreted — idealization 9 states this
explicitly, and the proposal never issues a constraint-3/4 or Tier-W/Tier-A
verdict anywhere (grep-confirmed: the only "constraint-3" hits are the two
explicit disclaimers). ABS_TOL=5×10⁻⁴ (0.1·C_THR) is disclosed as a modelling
choice (idealization 2), not smuggled in as a threshold revision, and follows
T7's own precedent (δ_C sitting an order of magnitude below GATE_HARD). No
"invisible"/"eye-invisible" language appears anywhere. This is exactly the
instrument-fidelity discipline T20→T21 needed four iterations ago and is the
right cycle to finally run `gaussian_angle_weights`'s own convergence check
before it is cited again.

## Sharpest attack (≤150 words)

P-NCONV26-5's "sharpest stakes test... does NOT flip" conflates *this
cycle's one axis* (quadrature self-convergence) with *contamination-risk
safety in general*. The worst cell is 750nm/θ₀=38°/FWHM=2° — and LOGBOOK's
own T24 entry already measured a **real, FDTD, +0.0070** `ABSORB` boundary
systematic at that *exact* (λ,θ,FWHM), ~7× the cell's entire 0.000994
headroom to C_THR, unaddressed here (idealization 5 scopes it out formally,
but the P-NCONV26-5 row itself carries no inline pointer to T24). If n-
convergence passes clean, a LOGBOOK citation reading "does NOT flip" — two
sections away from idealization 5's caveat — is exactly the headline-adjacent
caveat-drop this program has now named three times running (Iteration
24's bare-"Tier-W" slip, R4). Passing this audit proves the desk value is
numerically stable, not that the cell is safe: a known, comparable-magnitude,
unaddressed systematic sits right on top of it.

## Verdict

**support-with-changes.**

## Flip

Append to P-NCONV26-5's own prediction text (not only idealization 5):
"FDTD-unvalidated at this cell; T24's ~0.0070 ABSORB systematic at this same
(λ,θ,FWHM) point is untested here and could independently flip the cell."
With that inline scope attached, this seat's verdict is unqualified support.
