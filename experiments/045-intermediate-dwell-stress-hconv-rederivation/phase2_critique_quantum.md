# Phase 2 Critique — QUANTUM OPTICS

**Cycle:** Panel Iteration 22, exp-045 ("The Intermediate-Dwell Coupled
Kinetics-Thermal Stress Sweep + h_conv/mass_kg Re-derivation"). Lead:
ELECTROMAGNETISM. This seat critiques blind, no access to other seats'
Phase-2 output this cycle.

## Steel-man (≤150 words)

Blocks A and B are real, verified work, not scope-inflation dressed up as
discipline. I independently re-derived `coupled_kinetics_thermal_dT`'s
bracket term from the stated coupled ODE (integrating factor on the
thermal equation, substituting the exact logistic n(t)) and it matches
the code's bracket exactly, sign for sign. Deferring Block C is *not* the
"claimed-complete-but-undelivered" pattern Red Team named at Iteration
21's close — nothing here is claimed done. The proposal states the
deferral, its reason, and a concrete return point (Iteration 24) in
writing, before any run — the disclosure discipline the house requires.
The cited precedent (MATERIALS deferring EM's/THERMO's items at
Iteration 21) is real and already accepted, not invented. And Block A's
dwell-magnitude sweep is legitimate, independently useful work: it closes
a real gap (one dwell tested against 16 hosts) even though it is not
*my* gap.

## Sharpest attack (≤150 words)

The "QUANTUM-native judgment call" justification for deferring Block C
doesn't hold up under its own logic. `pulse_train_segments` already
exists, and exp-038 (Iteration 15) already made the exact judgment call
in question — a 5τ/0.5τ inter-pulse-interval bounding pair — and already
ran it at Host D. Block A's own sweep even computes τ_kinetics(Host D, r)
at all 4 ratios needed to reuse that convention verbatim with
`dwell_central`=66.7ms as `T_pulse`. Nothing about choosing that pair
required design work this cycle didn't already do elsewhere in the same
script. More precisely on my Iteration-21 catch: Block A sweeps dwell
*magnitude* at `n0=0.0` on every one of 1664 points
(`kin.relax_exact(n0=0.0, ...)`) — it never sets `n0≠0`. My concern
(population memory carried from an incompletely-relaxed prior pass) is
untouched, not partially addressed — Block A moves along an orthogonal
axis while my gap sits exactly where Iteration 21 left it, now deferred a
second cycle running with a rationale weaker than stated.

## Answers to the three assigned questions

1. **Is the Block C deferral reasonable, or a new-form instance of the
   Red-Team-flagged pattern?** Not the same failure mode — this is
   honestly disclosed, not overclaimed. But the *substance* of the
   deferral reasoning is weak: the specific judgment call cited as
   requiring QUANTUM's discipline ("choosing a physically-motivated
   sweep-rate/inter-pulse interval") was already made and validated at
   exp-038, using machinery this cycle's own Block A already exercises
   for the identical host/ratio grid. This is my own Iteration-21 catch,
   ranked priority #3 for this exact iteration, and it is now the *only*
   Tier-1 item of three not delivered — deferred a second consecutive
   cycle (first at Iteration 21's close, "deferred to Iteration 22";
   now again to Iteration 24) with no new obstacle raised, only a
   restated scope-discipline argument. A single bounding run at near-zero
   marginal cost was available and not taken.

2. **Does Block A's dwell/τ sweep engage my Iteration-21 concern, or
   sweep an orthogonal axis?** Orthogonal axis, precisely. Confirmed by
   reading `run.py`: `n_at_dwell = float(kin.relax_exact(n0=0.0, k_f=k_f,
   k_r=k_r, dt=dwell))` is called identically across all 1664 sweep
   points — dwell *magnitude* varies (R∈[0.1,10]× either τ_kinetics or
   τ_thermal), but the starting population is cold (`n0=0`) at every
   single point, always. My concern is specifically about `n0≠0` —
   population left over from an earlier, incompletely-relaxed exposure,
   which is the entire mechanism `pulse_train_segments` exists to test
   (ambient→pulse→ambient→pulse…, tracking whether periodic/first-pulse
   peak-n creeps above 1 at Hosts D/E, exactly as exp-038's own P-MAT-5b
   already found: ratio up to 2.106 at Host E under a 0.5τ stress
   interval). Sweeping dwell magnitude with a cold start every time
   answers "how good is the decoupled shortcut at various single-exposure
   durations," a real and useful question — but it is not an answer,
   partial or otherwise, to "does repeated exposure accumulate population
   above what any single-pass point in this sweep ever reaches." Status:
   UNCHANGED from Iteration 21's close, not partially addressed.

3. **`coupled_kinetics_thermal_dT` bracket identity — independent
   re-derivation.** Starting from the stated coupled ODE (dn/dt =
   k_f(1−n) − k_r·n, n(0)=0; dΔT/dt = (1/τ_th)(ΔT_ss·n(t) − ΔT), ΔT(0)=0),
   substitute the exact logistic solution n(t) = n_ss(1 − e^{−t/τ_k}) and
   solve the resulting linear first-order ODE in ΔT via integrating
   factor e^{t/τ_th}. Carrying the algebra through (two exponential
   integrals, one direct, one shifted by 1/τ_th − 1/τ_k = (τ_k−τ_th)/
   (τ_kτ_th)) and collecting the e^{−t/τ_th} coefficients gives:

   ΔT(t) = ΔT_ss·n_ss·[1 − (τ_k/(τ_k−τ_th))e^{−t/τ_k} +
   (τ_th/(τ_k−τ_th))e^{−t/τ_th}]

   This matches `run.py`'s `bracket` expression term-for-term
   (`tau_k`↔τ_k, `tau_thermal_s`↔τ_th, `dwell_s`↔t). **Confirmed
   correct.** As a byproduct I also checked the monotonicity argument
   underlying P-EM45-A1 (no coupled-ODE point can exceed
   `dt_ss_full·n_ss`): since n(t) itself rises monotonically to n_ss with
   no overshoot, and ΔT(t) is a passive first-order-lowpass-filtered
   version of that already-monotonic input, ΔT(t) is bounded above by the
   sup of its own forcing input at every t — the ceiling bound holds by
   the standard argument for a stable linear system driven by a
   monotonically-increasing-to-its-asymptote input. No objection to
   P-EM45-A1's structural claim.

## Verdict: **support-with-changes**

The verified-correct closed form and the honestly-scoped, genuinely
useful Block A/B content earn support. The one required change: this
cycle should not close with my own priority-#3 catch simply re-deferred
on a "requires QUANTUM's own judgment" rationale that the record itself
contradicts — the judgment was already made, at Iteration 15, using
machinery Block A already touches for the same hosts.

## Single parameter change that would flip to full support

Add one bounded Block C sensitivity check before Phase 3, reusing
exp-038's own already-validated convention rather than inventing a new
one: `pulse_train_segments(k_f_ambient, k_r, A=1, T_pulse=dwell_central
(66.7ms), dt_sweep, n_pulses=5)` at Host D (all 4 ratios), with
`dt_sweep ∈ {5×τ_kinetics(Host D, r), 0.5×τ_kinetics(Host D, r)}` —
exactly exp-038's bounding pair, applied to this cycle's own witness
dwell instead of a generic pulse duration. Report periodic/first-pulse
peak-ΔT ratio (via `coupled_kinetics_thermal_dT` fed the accumulated
`n0` at each pulse start, not the cold-start shortcut) against the same
NETD band already in use. This costs a handful of extra lines reusing
functions this script already imports (`kin.relax_exact`,
`coupled_kinetics_thermal_dT`) and directly closes the gap instead of
carrying it to Iteration 24 untouched.
