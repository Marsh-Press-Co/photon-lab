# PHASE 1 — PROPOSE · Panel Iteration 52 · exp-075
## The `ABSORB` band's own boundary reflectance: an analytic transfer-matrix model, tested zero-cost against T28's real data (T28)

*Fresh sub-agent, THERMODYNAMICS charter (PANEL.md seat: where absorbed
energy goes; owns the per-proposal energy sidecar), lead by rotation.
Executes Iteration-52 queue item 1 — PLAN.md's own "PHOTONICS' WKB/
adiabatic boundary-reflectance model for the graded-loss `ABSORB` band" —
queued and dropped without execution twice (Iterations 46, 47). Per house
precedent (Iteration 44, MATERIALS-by-rotation executing a substantively
thermal-contact item), the rotation lead formalizes the queue's own #1
regardless of whose charter it fits most naturally; my own seat's angle
(does the reflected/dissipated energy this mechanism moves around matter,
and is it detectable) is engaged briefly in §3 and found not to add a new
constraint here — the substantive content is EM/PHOTONICS field-and-
boundary physics, executed as the queue directs.*

---

## 0. What this is, and what it is not

**ZERO new FDTD calls.** `lab.fdtd2d.Sim` is imported once, to build its
`damp_e` array via `__init__` alone (no `.run()` anywhere in this
experiment's code) — reading the graded-loss band's own per-cell numbers
programmatically rather than retyping the cubic-ramp formula by hand
(house rule R4; the context packet's own recommendation).

This is an **analytic derivation, tested against already-collected data**,
not a fit. The reflection coefficient `r(theta; ABSORB)` is derived from
first principles (§2), gated by three zero-data sanity/passivity checks
(§2d) before any number is trusted, then turned into a predicted
interference signature (§2e) with **zero free parameters tuned to the real
data** — the comparison in §5 is the first and only time the real
`block_dense.rows` numbers are touched. `desk_reflectance.py` — sorry,
`boundary_reflectance.py`, this directory — computes every number below;
none is hand-typed (R4).

**Disclosure, matching this program's own desk-check convention
(exp-069/070/074):** deriving the physics did involve iterative
debugging — an initial sign choice for the loss term inside the effective
complex index failed a basic passivity check (`|r|<=1`) catastrophically
(worst case `|r|~3.4e4`), which is itself reported as a finding (§2c) —
the CORRECTED formula is what every number below uses, and the correction
was made by an unambiguous physical requirement (energy conservation),
not by trying values until the real data looked better. No falsifiable
band below was chosen after seeing the comparison in §5.

---

## 1. Narrative (<=300 words)

T28 (opened Iteration 46) is a real, resolution-checked, settled ~2.84°
periodicity in the `C80-C40` ambient-contrast differential that does not
match the program's own established T21 source-aperture-diffraction
fringe (`P(theta)=lambda/(A cos theta)~1.96°`). Six cycles of
differential/beat-fit statistical work (Iterations 46-51) narrowed but
could not resolve the mechanism, and formally retired that entire
instrument class last cycle (exp-074) — the panel's own seventh-cycle
rule now requires "a qualitatively different strategy" before the
sub-thread reopens. This cycle is that strategy: instead of re-fitting
the existing angle sweep, derive what the `ABSORB` band's own graded-loss
profile — the one thing that actually differs between `C40` and `C80` by
construction (exp-065's PAD trick, LOGBOOK-verified) — predicts as a
REFLECTION physics effect, with zero reference to the target data, and
test that prediction once.

The mechanism: the `-x` edge `ABSORB` band sits 37 cells in front of a
PEC-like hard wall (`Sim.Ez[0,:]` is never updated by the Maxwell curl
step — a fixed boundary by construction, not an assumption). A wave that
overshoots the observation plane, crosses the band, and reflects off that
wall returns to the plane as a second, coherent contribution — a source
image, weighted by the band's own complex reflection coefficient
`r(theta;ABSORB)`. This predicts a NEW angle-dependent term in `C_empty`,
with its own characteristic length scale (the plane-to-wall distance,
`ABSORB`-dependent by construction) — testable with zero new data.

**Result, stated here and derived in §5: the mechanism is real (nonzero,
passivity-respecting, `ABSORB`-dependent, as required) but wrong in scale
— REFUTE against the pre-registered bands.** Not a null result: it rules
a specific, previously-untested mechanism class out, narrowing what T28
can still be. *(299 words)*

---

## 2. Parameter table / derivation

### 2a. From the discrete per-step decay to an effective complex index

`lab/fdtd2d.py::Sim._damping` builds, per edge, a cubic ramp
`d(i)=((absorb-i)/absorb)**3` for `i=0..absorb-1` (`i=0` at the domain
edge, decaying to 0 at the interior), converted to a per-step
MULTIPLICATIVE field decay `exp(-0.30*d(i))`, applied to `Hx`/`Hy` right
after their curl update and to `Ez` right after source injection —
**every** step, identically for E and H (verified directly against
`lab/fdtd2d.py` lines 122-129, 226-253 — not assumed). This is a genuinely
different loss mechanism from the `sigma_e`-based conductivity elsewhere
in the same file (which enters the E-update's `ca`/`cb` coefficients) —
no equivalence between the two is built or assumed anywhere in this file.

**Idealization 1 — discrete decay treated as continuous.** The per-step
multiplicative kick `exp(-0.30*d(x))` is modeled as continuous exponential
decay at rate `nu(x)` sampled once per timestep: `exp(-nu(x)*dt)=damp_e(x)`,
`dt=courant_frac/sqrt(2)` (grid units, `c=1`) — exact for reproducing the
discrete map's OWN decay rate; the genuinely-discrete-in-time character of
the real update is not separately modeled. `nu(x)` is read directly from a
real `Sim.damp_e` array (`boundary_reflectance.py::damp_e_profile`), not
from the retyped cubic formula.

**Idealization 2 — the friction-PDE-to-complex-index bridge.** Because the
SAME `_damping` formula (same `self.absorb`, same ramp) damps `Ez`,
`Hx`, and `Hy` identically, this is modeled as a matched loss acting
equally on E and H: `dE/dt=c dH/dx - nu(x)E`, `dH/dt=c dE/dx - nu(x)H`.
Solving for a traveling-wave mode gives a local dispersion relation
`k(x)^2 = (omega^2 - nu(x)^2 - 2i*omega*nu(x))/c^2`, i.e. an effective
complex index `n(x) = 1 - i*nu(x)/omega`. **This is exact, not a
small-loss approximation** — `(1-ix)^2 = 1-x^2-2ix` identically for any
real `x`, verified numerically to machine precision at every `ABSORB`
(`[1b]` in the script's own output, max relative deviation `~1.5e-16`
across all four configs) — a finding of this file, corrected from an
original small-loss framing during derivation. This makes E and H equally
lossy but leaves the local wave impedance `Z(x)=n(x)/n(x)=1` matched to
vacuum at NORMAL incidence identically, for any `nu(x)` — no reflection
from admittance mismatch at normal incidence, by construction of the
symmetric E/H loss.

**Idealization 2b — a genuine sign ambiguity, resolved by passivity.**
Solving the k^2 equation admits two branches for `n(x)`, differing by
complex conjugation — a signature of a time-convention mismatch between
the friction-PDE derivation and the (separately, correctly) verified
lossless transfer-matrix algebra (§2c). **Adjudicated by an unambiguous
physical requirement**, not asserted: a source-free, PEC-backed, passive
(loss-only) stack must satisfy `|r(theta)|<=1` for every angle and
thickness — energy conservation, nothing more exotic. The `n(x)=1-i*nu/
omega` branch satisfies this at every one of 124 `(ABSORB,theta)` pairs
tested (worst `|r|=0.0064`, §2d); the OTHER branch (`n=1+i*nu/omega`, the
first thing tried) fails it by up to 4 orders of magnitude even at tiny
loss (`worst |r|~2.03` at `nu/omega=0.01`, climbing to `~1.8e16` at
`nu/omega=2.0` — both reproducible by re-running the sign-flipped
formula, left in the script's git history / this file's own record, not
hidden). Flagged here as an idealization, not swept under the rug: this
bridge from a discrete time-domain multiplicative decay to a frequency-
domain admittance carries a genuine sign choice that physics, not
algebra alone, had to resolve.

**Idealization 3 — oblique incidence via the vacuum-Snell substitution.**
`n(x)` is derived at NORMAL incidence; oblique behavior uses the standard
stratified-medium generalization `kx(x,theta)=k0*sqrt(n(x)^2-sin^2(theta))`,
TE (s-pol, matching this bench's scalar `Ez` field) admittance
`Z(x,theta)=n(x)/sqrt(n(x)^2-sin^2(theta))`. This is exact for an ordinary
complex-`epsilon(x)`,`mu(x)` medium; applied here to a friction-type loss
without an independent oblique re-derivation from the coupled E/H PDE.
Stated, not hidden.

### 2b. Band thickness in wavelengths (600nm, cpl=20) — is WKB/adiabatic even applicable?

| `ABSORB` | thickness (lambda) | max(nu/omega) [outer cell] |
|---|---|---|
| 40 | 2.00 | 1.3641 |
| 60 | 3.00 | 1.3641 |
| 70 | 3.50 | 1.3641 |
| 80 | 4.00 | 1.3641 |

Only 2-4 wavelengths thick, with the outer cell's own loss rate
EXCEEDING the optical frequency (`nu/omega=1.36`) — a single-pass
WKB/Born reflection integral is not automatically trustworthy here.
**Choice, stated up front (per the task's own escape clause): this
proposal does NOT use a truncated single-pass WKB/Born reflectance
integral as the primary calculation.** It uses an EXACT (given
Idealizations 1-3) recursive transmission-line impedance transform over
the discrete per-cell profile — one homogeneous layer per grid cell,
correctly handling multiple internal reflections within the graded
region, which a single-pass Born approximation by construction cannot.
The WKB single-pass adiabaticity parameter is computed anyway, as a
DIAGNOSTIC (not the reflectance calculation itself):

| `ABSORB` | max &#124;d(1/kx)/dx&#124; (theta=39°) | reading |
|---|---|---|
| 40 | 0.178 | marginal |
| 60 | 0.119 | marginal |
| 70 | 0.102 | marginal |
| 80 | 0.089 | slowly varying |

Consistent with 2-4λ being a genuinely marginal regime for a first-order
adiabatic treatment — exactly why the exact transfer matrix, not a Born
integral, is used for the number that matters.

### 2c. Sanity / passivity gates (must pass before any r(theta) is trusted)

| Gate | What it checks | Result |
|---|---|---|
| G-LOSSLESS | random REAL index profiles (any thickness/angle) give `&#124;r&#124;=1` exactly — a lossless PEC-backed stack cannot do otherwise | worst deviation `2.2e-16` — PASS |
| G-N1 | the general N-layer recursion's first step matches the textbook single-layer short-circuited-line formula, computed independently outside the loop | worst deviation `1.4e-15` — PASS |
| G-PASSIVITY | every physically-lossy computed `r(theta;ABSORB)` (124 pairs, the real dense-sweep grid) satisfies `&#124;r&#124;<=1` | worst `&#124;r&#124;=0.0064` — PASS |

All three are `assert`-gated in code — the script halts before computing
anything downstream if any fails (matching this program's own G0-style
convention).

### 2d. `r(theta; ABSORB)` — magnitude and phase, on the real dense-sweep grid

| `ABSORB` | theta=36.0° | theta=39.0° | theta=42.0° |
|---|---|---|---|
| 40 | &#124;r&#124;=0.0029, arg=-78.1° | &#124;r&#124;=0.0043, arg=-40.9° | &#124;r&#124;=0.0064, arg=-1.2° |
| 80 | &#124;r&#124;=0.0000, arg=+171.6° | &#124;r&#124;=0.0001, arg=-179.5° | &#124;r&#124;=0.0001, arg=-145.5° |

Sensible on its face: the thicker (`ABSORB=80`) band reflects roughly two
orders of magnitude LESS than the thinner (`ABSORB=40`) one — a thicker
graded absorber genuinely absorbs more before any wave can reach the wall
and return, exactly as intended by the boundary's own design purpose.

### 2e. From `r(theta;ABSORB)` to a predicted interference signature

Reused, not reimplemented: exp-048's own already-committed, already-
vetted Huygens-Fresnel desk propagator
(`edge_diffraction_c_empty_corrected` / `field_and_h`,
`experiments/048-evidentiary-chord-closure/design_geometry.py`) computes
the DIRECT source's field at the observation plane. This proposal adds a
SECOND coherent contribution: the mirror image of the real source through
the `x=0` wall (same y-positions, same taper, image-to-plane distance
`PLANE_X+SRC_X`), weighted by the complex `r(theta;ABSORB)` derived
above, summed coherently with the direct field before recomputing
`C_empty` via the SAME `lab.ambient.window_means`/`weber` reduction
exp-048's own function uses. Zero new field-propagation code — an
extension of established, vetted machinery, not a new instrument.

**Closed-form cross-check (independent of the numeric propagator, a
useful sanity companion, not the primary number):** the round-trip phase
difference between the direct and wall-echo paths is
`Delta_phi(theta)=2*k*cos(theta)*PLANE_X(ABSORB) + arg(r(theta;ABSORB))`
(source-position dependence cancels exactly out of the DIFFERENCE — a
standard interferometer-arm argument), giving a period

`P_wall(theta;ABSORB) = (180/pi) * lambda / (2*PLANE_X(ABSORB)*sin(theta))`

— note the **sin(theta), not cos(theta)**, dependence: T21's own fringe
comes from a Y-oriented baseline (`P=lambda/(A cos theta)`); this
mechanism's baseline (source-to-wall-and-back) is X-oriented, giving the
complementary trig function. A genuinely different functional form, not
T21's reused.

| `ABSORB` | `PLANE_X` (cells, from `exp-065::CONFIGS`) | `P_wall(39°)` |
|---|---|---|
| 40 | 77 | 11.82° |
| 60 | 97 | 9.39° |
| 70 | 107 | 8.51° |
| 80 | 117 | 7.78° |

Already visibly far from 2.84° at this closed-form level — the full
numeric test (§5) confirms this is not an artifact of the closed-form
simplification.

---

## 3. THERMODYNAMICS sidecar — does absorbed/re-radiated energy bear on this mechanism?

**Briefly: not applicable here, and here is why, not just an assertion.**
This mechanism concerns a REFLECTED field's interference with the direct
field — a coherent, elastic (non-dissipative in the observable itself)
effect on `C_empty`. The energy the `ABSORB` band DOES dissipate
(`1-|r|^2`, essentially all of it — `|r|<=0.0064` throughout §2d means
`>99.996%` of incident power is absorbed, not reflected) has nowhere to
re-radiate INTO this measurement: `C_empty` is a coherent-field
ambient-contrast reading at 600nm, not a thermal/IR channel, and no
object or observer sits anywhere near the `ABSORB` band itself (it is a
domain-edge numerical construct, not a physical body — `lab/materials.py
::graded_black_shell`, T5's own established subject, is the actual
physical absorber this sidecar exists to track). There is no absorbed-
power budget to log here that isn't already covered by T5/Iteration-20's
own standing UNDETECTABLE verdicts for physical absorbers on this bench —
this cycle introduces no new object and no new absorbed-power number.
Stated per PANEL.md's own instruction to say so briefly when the sidecar
doesn't apply, rather than pad.

---

## 4. T1 escape-route statement

**N/A — instrument-fidelity thread, constraint 3 not engaged.** Same
disposition as exp-069 through exp-074 on this exact sub-thread: this
cycle characterizes the FDTD instrument's own boundary-condition physics,
not a phenomenon-mechanism candidate. No absorber, no switch, no
constraint-3 scene anywhere in this file.

---

## 5. Falsifiable predicted outcomes — pre-registered numeric bands

All numbers below are produced by `boundary_reflectance.py`
(`boundary_reflectance_results.json` / `boundary_reflectance_output.txt`,
this directory) — none hand-typed (R4). The bands themselves were fixed
before this comparison was computed (§0); the desk-level closed-form
estimate in §2e (periods of 7.8-11.8°, already far from 2.84°) was known
before the bands were written down, and is disclosed as such — matching
this program's own "disclosed reconnaissance up front, not smuggled into
the bands" convention (exp-070).

### Test A — period match (against the established `P*=2.8421°` family)

`rel_dev = |P_model - P*_real| / P*_real`, both `P*` fit with the SAME
fixed-then-free sinusoid methodology `exp-069/run.py::_free_period_search`
already used to establish `P*=2.8421°, R^2=0.6272` (imported here, not
reimplemented, called with its own default grid arguments — re-run on the
real data by this script reproduces `P*=2.8421°, R^2=0.6272` exactly,
confirming the reused machinery).

- **SUPPORT** iff `rel_dev <= 0.30`
- **REFUTE** iff `rel_dev > 1.00`
- **INCONCLUSIVE** otherwise

**Observed: `P_model=15.0000°`** (the free-period search over the
program's own conventional 1-8° window runs to ITS search boundary — a
widened 1-60° search also runs to boundary, `P*=60.0°`, `R^2=0.879`,
confirming the model's own predicted curve does not complete even one
oscillation across the 6° dense-sweep window at all, consistent with
§2e's closed-form 7.8-11.8° period estimate). **`rel_dev=4.28` — REFUTE.**

### Test B — shape match (the stronger test PANEL.md's own mandate names as preferable to a bare period match)

Pearson `r^2` between the model's own predicted `delta(theta) =
C_with_wall(80) - C_with_wall(40)` (31 points, the real dense-sweep grid)
and the REAL `delta(theta)` from `experiments/069/results.json ->
block_dense.rows`.

- **SUPPORT** iff `r^2 >= 0.30`
- **REFUTE** iff `r^2 <= 0.05`
- **INCONCLUSIVE** otherwise

**Observed: `r^2 = 0.2586`, Pearson `r = -0.508` (NEGATIVE correlation).**
**INCONCLUSIVE** — close to, but under, the SUPPORT bar, and the sign is
the wrong direction (weak anti-correlation, not the mechanism's own
predicted-vs-real curves tracking together).

### Amplitude, disclosed (non-gating — not part of either pre-registered band, reported for completeness)

The model's own predicted `delta(theta)` has peak-to-peak `7.70e-4`; the
REAL `delta(theta)` has peak-to-peak `4.03e-3` — the mechanism, even at
its own best-fit phase, predicts an oscillation **roughly 5x smaller**
than what is observed. Consistent with, not independent evidence for or
against, the REFUTE verdict below.

### Combined verdict

**Combined rule (stated before scoring, per §0):** REFUTE if EITHER test
REFUTEs; SUPPORT only if BOTH tests SUPPORT; INCONCLUSIVE otherwise.

**Observed: Test A REFUTE, Test B INCONCLUSIVE -> COMBINED: REFUTE.**

**Reading, stated plainly and not overclaimed:** this specific mechanism —
a single coherent echo off the `-x` wall through the graded `ABSORB`
band, interfering with the direct source field — is a real, passivity-
respecting, `ABSORB`-dependent effect (§2d), but its own characteristic
angular scale (7.8-11.8°, set by the plane-to-wall distance) is roughly
3-5x too long, and its predicted amplitude is roughly 5x too small, to be
the T28 ~2.84° family. **This does not close T28's mechanism question**
— it rules OUT one previously-untested, physically well-motivated
candidate (a single-bounce wall echo through the band's own admittance
profile), narrowing the remaining space. It does not by itself rule out
richer variants of the same physical idea (e.g. the `+x`-side band behind
the source, or multiple internal bounces beyond the single echo modeled
here — both named, not computed, in Idealization 4 below).

---

## 6. Idealizations (full list, consolidating §2's inline disclosures)

1. Discrete per-step multiplicative decay treated as continuous
   exponential decay sampled once per timestep (§2a).
2. The friction-PDE-to-complex-index bridge, assuming E/H loss symmetry
   from the code's own identical `_damping` formula implies a matched
   (`eps=mu`) effective medium (§2a) — an EXACT, not small-loss,
   consequence of that assumption (§2a, corrected during derivation).
3. A genuine sign/branch ambiguity in that bridge, resolved by an
   unambiguous physical requirement (passivity, `|r|<=1`), not asserted
   (§2b — the single largest correction made during this cycle's own
   derivation, disclosed in full in §0/§2b, not smoothed over).
4. Oblique incidence handled via the standard vacuum-Snell stratified-
   medium substitution, not independently re-derived from the coupled
   friction PDE at oblique angles (§2a).
5. **Only the `-x` edge band (the one facing the observation plane and
   PEC wall) is modeled.** The `+x` edge band, behind the source
   (`clear_src=20` cells, ALSO `ABSORB`-thick by construction — the same
   `self.absorb` parameter drives all four edges, `lab/fdtd2d.py::
   _damping`), could produce an analogous rearward echo with its own,
   different length scale. Not computed here — a genuinely different
   candidate mechanism for a future cycle, not smuggled into this one's
   prediction.
6. Single echo only (one reflection off the wall) — no multiple internal
   bounces between the band and the source's own near-field structure are
   modeled; the transfer matrix itself DOES handle multiple bounces
   WITHIN the graded band (that is its whole point over a Born
   approximation), but the IMAGE-SOURCE step (§2e) models only the
   band-plus-wall system's overall reflectance as a single coherent add,
   not a resonant cavity between the band and anything else in the scene.
7. TE (Ez-scalar) polarization only — matches this bench throughout, not
   a new idealization specific to this cycle.
8. 600nm only, matching `block_dense.rows`'s own wavelength; no claim
   about 450/750nm behavior is made (the `block_leg750` confirmatory leg,
   named in the context packet, is not touched by this cycle — a
   deliberate scope cut, not an oversight, given the ranking pressure to
   deliver a decisive test against the specific dataset the queue names).
9. No energy sidecar beyond §3's own argued N/A (house precedent for a
   disposition-by-argument, not an omission).

---

## 7. Cost estimate

**Zero FDTD calls. Zero `lab/` diff.** `boundary_reflectance.py` reads one
already-committed `results.json` (`experiments/069/.../results.json`) and
two already-committed desk-propagator modules
(`experiments/048/.../design_geometry.py`,
`experiments/065/.../design_geometry.py`), runs in under 2 seconds
(measured, this run, single core — `Sim.__init__` calls only, no
`.run()`), and writes `boundary_reflectance_results.json` +
`boundary_reflectance_output.txt` in this directory.

---

## Reproduction

`python3 experiments/075-t28-absorb-boundary-wkb-reflectance/boundary_reflectance.py`
— writes `boundary_reflectance_results.json` and
`boundary_reflectance_output.txt` in this directory. No seed, no Monte
Carlo (the two random-profile sanity gates in §2c use a fixed
`np.random.default_rng` seed each — deterministic, reproduced bit-exact
run to run).
