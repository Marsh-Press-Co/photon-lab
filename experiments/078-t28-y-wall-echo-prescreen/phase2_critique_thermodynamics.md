# THERMODYNAMICS — Phase 2 Critique · Panel Iteration 55 · exp-078 (T28 y-wall echo pre-screen)

*Fresh sub-agent, THERMODYNAMICS charter (PANEL.md, verbatim): "where absorbed
energy goes. Always asks what re-radiates and whether it would be detectable.
Owns the per-proposal energy sidecar: absorbed power -> temperature rise ->
emission band -> detectability. Expressibility contract: the sidecar is a
post-run analytic calculation, not an FDTD output, and is labeled as such."
Blind to all other Phase-2 critiques this cycle. Verified independently by
reading `y_wall_prescreen.py`/`boundary_reflectance.py`/`lab/fdtd2d.py`
source directly and re-deriving the incidence-angle geometry from
`add_line_source`'s own docstring — not merely trusting the proposal's
printed tables. Given this seat's own load-bearing arithmetic slip last
cycle (exp-077, caught by Red Team), every number below was independently
recomputed, not read off the proposal.*

---

## Steel-man (≤150 words)

§3.4's premise is correct and I independently re-verified it: `Sim._damping`
(`lab/fdtd2d.py` lines 122-129) builds one `ramp=(arange(absorb,0,-1)/absorb)**3`
array and applies it via `np.maximum` to all four edge bands identically —
x-low, x-high, y-low, y-high, same `self.absorb`, no directional term. So the
graded-loss `n(x)` profile, and therefore the absorbed-power fraction
`1-|r(θ;ABSORB)|²` *at whatever angle is actually incident on a given wall*,
is a pure function of ABSORB depth and local incidence angle — never of which
Cartesian edge hosts the band. No new thermodynamic machinery is needed for a
y-wall that didn't already exist, gated, for the x-wall. And because this file
computes zero FDTD and zero absorbed-power number anywhere, an N/A sidecar
disposition would be the objectively correct one to state — the defect below
is an omission, not a wrong physics claim.

## Sharpest attack (≤150 words)

`boundary_reflectance.py`'s `reflection_coefficient` is documented, and I
confirmed in its own docstring, as computing r for "angle theta_deg from the
x-normal" (`s2=sin(theta)**2`). `y_wall_prescreen.py` line 214 passes the
SAME sweep `theta_deg` (36-42°, incidence from the x-normal, per
`add_line_source`'s own "angle_deg: launch angle from the x-axis" convention)
into this call for the y-wall, never transforming to the geometrically
correct y-normal incidence angle, `90-theta_deg` (48-54°) — grepped the whole
file for any such transform; none exists. Consequence, worked through: for
`PAIR_PAD` (C40 vs G40, both ABSORB=40) `arg(r)` is identical on both terms
regardless of which angle convention is used, so it cancels and this specific
error doesn't touch that comparison. But `C80-C40` and `PAIR_ABSORB40`
compare DIFFERENT ABSORB depths, so `arg(r(θ;40))-arg(r(θ;80))` does NOT
cancel — these are exactly the two comparisons that cleared SUPPORT
(rel_dev 0.130/0.233), and §5.2's own "near-noise-floor artifact" flag on
C60/C70/C80's `|r|` may itself be an angle-convention artifact, not (only)
numerical ill-conditioning as claimed — an alternative, cheaper-to-test
explanation the proposal never considers.

## Verdict

**support-with-changes.**

The self-scored Test-A-only INCONCLUSIVE verdict is the honest read of what
this file actually computed, and I don't think the angle issue below flips it
to SUPPORT or REFUTE on its own — but it changes *which* of the three scored
comparisons deserve trust, and that bears directly on this seat's own
question (does the near-noise-floor `|r|` regime have a thermodynamic
implication?). It does: a near-zero `|r|` config (C60/C70, and to a lesser
extent C80) means that wall is absorbing ≥99.9999% of incident power —
essentially the ABSORB band doing exactly its designed job. A "coherent echo"
built from `arg()` of a complex reflection coefficient whose magnitude sits
within an order of magnitude of the float-noise floor of a 40-80-cell
recursive transfer-matrix product is not a physically well-posed re-radiated
quantity at all — there is no real energy budget left to carry a coherent
phase signature once >99.9999% of the incident power has already gone into
the lossy band. That reading (independent of, and additional to, §5.2's own
numerical-conditioning framing) argues C60/C70/C80's contribution to any
scored comparison should be treated as physically, not just numerically,
suspect — reinforcing rather than replacing the proposal's own caution.

Two changes required before this cycle closes:

1. **Verify the angle-convention question empirically** (cheap, zero-FDTD,
   desk-only): re-run `edge_image_phase_difference` for the y-wall calls with
   `90-theta_deg` substituted for `theta_deg` in the `reflection_coefficient`
   call, and re-score §5.3's three comparisons. If `C80-C40`/`PAIR_ABSORB40`
   move materially (plausible, given `sin²θ∈[0.35,0.45]` vs
   `cos²θ∈[0.55,0.66]` over 36-42°, a non-trivial swing in the impedance
   mismatch term), the "2 of 3 SUPPORT" headline needs re-stating; if they
   don't move materially, that itself is worth reporting as a robustness
   check this proposal is currently missing.
2. **State the sidecar disposition explicitly.** Every T28 instrument cycle
   since exp-071 has carried a one-sentence THERMO N/A disposition (present
   even in exp-077, and the omission caught, named, and fixed at Phase 2 in
   exp-076 two cycles ago). This proposal — zero FDTD, zero absorbed-power
   number computed anywhere — has an obviously correct N/A to state, and
   states nothing. A recurring one-line process gap after it was already
   caught once is worth naming plainly rather than re-discovering silently
   each cycle.

## Single change that would flip my verdict

To **oppose**: if re-scoring with the corrected `90-theta_deg` angle for the
y-wall's `reflection_coefficient` calls materially changes `C80-C40`'s or
`PAIR_ABSORB40`'s `rel_dev` (e.g. pushes either from SUPPORT into REFUTE, or
reveals the two nominal SUPPORTs were entirely angle-artifact-driven), then
§5.3's "2 of 3 SUPPORT" framing — which §7's own reasoning leans on to argue
"not obviously wrong" — would be actively misleading rather than merely
under-caveated, and this pre-screen should not be cited as evidence the
mechanism class survives even a cheap look.

To **support** outright (no changes needed): if the angle-corrected re-score
reproduces materially the same three `rel_dev` values (i.e. the swap turns
out not to matter at this precision), and the missing sidecar sentence is
added, both open items close with zero new FDTD and zero change to the
Test-A-only INCONCLUSIVE self-score — which I'd then have no basis to
withhold support from.

---

## Independent verification notes (for the record)

- Re-read `lab/fdtd2d.py::Sim._damping` (lines 122-129) directly: confirmed
  one shared `ramp` array applied via `np.maximum` to all four edge slices,
  no `nx`/`ny`/axis-dependent term in the ramp construction itself — matches
  my own seat's independent confirmation of this same fact last cycle
  (exp-077 critique, §"Independent verification notes"), now re-derived a
  second time from scratch rather than carried forward.
- Re-read `boundary_reflectance.py::reflection_coefficient`'s docstring and
  body: `theta_deg` enters only as `s2=sin(radians(theta_deg))**2`, and the
  docstring states this is the angle "from the x-normal" explicitly — not a
  generic "angle from whichever wall's normal" parameter.
- Re-read `lab/fdtd2d.py::add_line_source`'s docstring: `angle_deg` is
  documented as "launch angle from the x-axis," confirming the sweep
  `theta_deg` used throughout `y_wall_prescreen.py` (36-42°) is measured from
  the x-axis/x-normal, not from the y-wall's own normal.
- `grep -n "90\b\|90-\|theta_y\|from_normal" y_wall_prescreen.py`: zero
  matches — no angle transform of any kind exists in the file before
  `theta_deg` is passed into `reflection_coefficient` at line 214.
- Worked the cancellation argument for `PAIR_PAD` by hand from
  `edge_image_phase_difference`'s own formula
  (`delta_phi = arg(r) + k*fixed_offset`): since C40 and G40 share
  `ABSORB=40` and hence identically the same `r(theta;40)` value at every
  `theta`, `arg(r)` is bit-identical in both terms of the `PAIR_PAD`
  difference and cancels regardless of which angle convention was used —
  confirming this specific defect does not touch T28's actual dominant
  target, only the two comparisons that mix `ABSORB` depths.
- Computed `sin²θ` and `cos²θ` at the sweep endpoints by hand: `sin²(36°)=
  0.3455`, `sin²(42°)=0.4477` vs `cos²(36°)=0.6545`, `cos²(42°)=0.5523` — the
  two candidate `s²` regimes differ by roughly 20-30 percentage points over
  the scored window, not a negligible swing given how sensitive `|r|` is
  shown to be across ABSORB depths in §5.2's own table.
