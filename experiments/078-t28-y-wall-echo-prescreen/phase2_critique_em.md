# PHASE 2 — CRITIQUE (ELECTROMAGNETISM, blind) · Panel Iteration 55 · exp-078

*Fresh sub-agent, ELECTROMAGNETISM charter: field/wave behavior, impedance
matching, energy coupling; owns reciprocity/passivity/causality bookkeeping.
Blind to other seats' Phase-2 critiques. Grounded on PANEL.md, AGENTS.md,
LOGBOOK.md (RULED OUT R1–R9, T28's full Iteration 46–54 history), the
proposal, its code (`y_wall_prescreen.py`), its output
(`y_wall_prescreen_results.json`), and the reused machinery
(`boundary_reflectance.py`, `lab/fdtd2d.py::Sim._damping`).*

---

## 1. Steel-man

The general strategy is sound EM reasoning. The §3.2 disanalogy — mirroring
the source *in x* leaves the y-dependent steering ramp untouched (whole
aperture stays coherently re-steerable, licensing the two-ray reduction),
while mirroring *in y* touches that exact coordinate, so a bare coordinate
swap is NOT the right image — is a correct diagnosis of standard image
theory for a driven phased-array line source, and the §3.1 from-scratch
re-derivation of the x-wall formula (reproducing it to `1.8e-15°`) is a real
validation of the method before it is extended somewhere new. The §3.4
premise check — reading the actual `damp_e` columns off one `Sim` instance
and finding the x-edge and y-edge ramps bit-identical (`worst diff=0.0`) —
is exactly the "verify in code, not assumed" discipline this program
requires, and it is a genuinely necessary precondition. The document's own
honesty about scope (no Test B, no null-permutation control, `C80`
near-noise-floor) is a model of the disclosure this sub-thread now expects.

## 2. Sharpest attack

**§3.4 verifies the wrong thing is identical.** The damping *ramp array*
being shared says nothing about whether the *angle argument* fed into
`reflection_coefficient` is the correct one for a y-normal wall.
`boundary_reflectance.py`'s own docstring (line 183) is explicit:
`theta_deg` there means "from the x-normal," and `s2=sin(theta)²` is used
because sin(θ) is the wavevector component *tangential* to an x-stratified
slab. For a y-stratified slab, the conserved tangential component is
`k_x/k=cos(θ_beam)`, i.e. the correct call is
`reflection_coefficient(n_prof, 90-θ_beam, ...)`, not `θ_beam` unchanged.
`edge_image_phase_difference` calls it with the raw beam angle. I
recomputed both ways: at `ABSORB=40`, `|r|` swings **2.5×–13.3×** between
the two conventions across 36–42°, and — because the theta-independent
geometric offset contributes zero ptp (§3 below) — `arg(r(θ))` is the
*sole* source of every oscillation this model reports; the reused angle is
wrong from the ground up, and the corrected range (48–54°) also sits
outside the gates' own tested envelope (±44°, `boundary_reflectance.py`
lines 232/249).

## 3. Independently computed check

Script: `y_wall_prescreen.py`'s own imported `br.reflection_coefficient`,
called both ways at the swept angles (`/tmp/.../scratchpad/
em_theta_frame_check.py`, this session).

| θ_beam | ABSORB | `\|r\|` as-implemented (θ_beam) | `\|r\|` corrected (90−θ_beam) | ratio | arg(r) impl (°) | arg(r) corrected (°) |
|---|---|---|---|---|---|---|
| 36° | 40 | 0.002900 | 0.038656 | 13.3× | −78.1 | 154.3 |
| 39° | 40 | 0.004269 | 0.024900 | 5.8× | −40.9 | 117.5 |
| 42° | 40 | 0.006423 | 0.015755 | 2.5× | −1.2 | 79.1 |
| 36° | 80 | 0.000029 | 0.001889 | 64.6× | 171.6 | −169.1 |
| 39° | 80 | 0.000068 | 0.000777 | 11.4× | −179.5 | 126.8 |
| 42° | 80 | 0.000116 | 0.000202 | 1.8× | −145.5 | 47.6 |

Two structural facts, confirmed directly from the code and from this table,
sharpen why this is decision-relevant rather than a footnote:

1. **`arg(r(θ))` is the entire model.** In `edge_image_phase_difference`,
   `delta_phi = angle(r) + k*fixed_offset`, and `fixed_offset =
   dist_image − dist_real` is built from `d_sp`, `A`, `obj_y`, `y_lo` —
   all static per-config numbers, none a function of θ. Every degree of
   `ptp_delta_phi_deg` reported in §5.2 of the proposal (76.9°/358.4°/…)
   is therefore generated *exclusively* by `arg(r(θ;ABSORB))`'s own
   θ-dependence. There is no other term to fall back on if that term is
   wrong.
2. **The two conventions are not just rescaled, they trend oppositely.**
   As-implemented, `|r|` at `ABSORB=40` *rises* with θ (0.0029→0.0064,
   36°→42°); corrected, it *falls* (0.0387→0.0158). `arg(r)` swings by a
   comparable total excursion under both conventions at `ABSORB=40`
   (≈77° either way, coincidentally) but through a qualitatively different
   θ-dependence (`sin²θ` vs `cos²θ` inside the transfer matrix) — so even
   where the *ptp* happens to land near the reported number, the *shape*
   `cos(Δφ_self(θ))` that Test A's period search is fit to is built from
   the wrong trig dependence, and there is no reason its recovered period
   (`P*≈3.17–3.21°`) bears any principled relationship to whichever period
   the correct convention would produce.

This is not the same defect class as R8/exp-075's `conj(r)` phase-convention
question (which was about which SIGN of an already-correctly-posed θ to
trust) — it is a frame error: the wrong physical angle is being asked of an
otherwise-correct, otherwise-gated function. G-PASSIVITY still holds at the
spot-checked corrected angles (`|r|<1` in every cell above), so passivity
per se is not violated — but the gates were never *re-run* at the corrected
θ-range (48°–54°, outside the ±44° envelope `gate_lossless_unimodular`/
`gate_single_layer_identity`/`gate_passivity` actually sampled), so even a
fixed version of this file would owe a fresh gate pass, not just a formula
edit, before its numbers could be trusted — precisely the "affordable named
check" R8 requires be run, not argued around.

On the image-phase convention itself (§3.2/§8): preserving the real
source's own driven phase at the image point, scaled only by `r`'s own
complex factor, is the physically correct boundary condition for a linear,
time-invariant, non-gyrotropic reflector (true here — static `ABSORB`
profile, matched-admittance TE model) — it does not smuggle in an
unexamined reciprocity assumption. The defect is not in that convention;
it is in which `r` gets plugged into it.

## 4. Verdict: **support-with-changes**

The edge-image strategy and the x-wall re-derivation/validation are sound
EM method, and the document's own self-scored INCONCLUSIVE is honest about
what a period-only, no-Test-B, no-null-control pre-screen can support. But
none of §5.2/§5.3's numbers — including the one comparison (`PAIR_PAD`,
`rel_dev=0.314`) the write-up leans on hardest to argue this *isn't* an
easy SUPPORT — can be trusted as computed: they rest entirely on
`arg(r(θ))` evaluated at the wrong incidence angle relative to the y-wall's
own normal. This is exactly the shape of gap R8 was adopted to close
(`experiments/075-.../phase5_redteam_audit.md` §2–§6): a fixable,
affordable, named check that was not run before a headline INCONCLUSIVE
reading was reported.

## 5. Single change that would flip my verdict to plain `support`

Fix the angle argument — call `br.reflection_coefficient(n_prof, 90.0 -
theta_deg, lam_cells)` in `edge_image_phase_difference` (or equivalently
swap `sin`↔`cos` in a y-wall-specific copy) — re-run the three gates
(`gate_lossless_unimodular`, `gate_single_layer_identity`,
`gate_passivity`) at the corrected 48°–54° envelope to confirm they still
pass outside their originally-sampled ±44° range, and re-score §5.3 with
the corrected `r(θ)`. If the resulting `rel_dev` pattern is qualitatively
similar (2-of-3 SUPPORT, `PAIR_PAD` still the weakest), the current
Test-A-only INCONCLUSIVE reading survives on firmer ground and I would
move to plain `support`; if it moves materially (plausible, given the
2.5×–13.3× magnitude swing and opposite θ-trend shown above), the
document's own headline numbers need to be re-issued before Iteration 56
ranks anything against them.
