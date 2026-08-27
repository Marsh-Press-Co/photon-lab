# PHASE 5 — REVIEW (ELECTROMAGNETISM, blind) · Panel Iteration 56 · exp-079

*Fresh sub-agent, ELECTROMAGNETISM charter: field/wave behavior, impedance
matching, energy coupling; owns reciprocity/passivity/causality bookkeeping —
formalizes what T1 permits and forbids. Blind to all other seats' Phase-5
reviews this cycle, and to this cycle's own Phase-2 EM critique (re-derived
here from scratch, not recalled or carried forward by assumption — I am a
fresh sub-agent with no memory of writing it, even though the task brief
discloses that critique fed part of this cycle's own central finding).
Grounded on `PANEL.md`, `AGENTS.md`, `LOGBOOK.md` in full (RULED OUT R1–R9,
T28's complete Iteration 46–55 history, close attention to Iterations 46–55
and exp-078's own record), `experiments/078-.../phase5_redteam_audit.md` in
full (§2 especially, this cycle's own direct ancestor), and this cycle's
complete, final record in order: `phase1_proposal.md` (as corrected, PHASE-3
UPDATE and revised §4/§7), all five Phase-2 critiques, `phase2_redteam_
audit.md`, `phase3_synthesis.md`, `phase4_results.md`, `y_wall_aperture_
sum.py`, `y_wall_aperture_sum_results.json`, `_output.txt`, plus
`experiments/075-.../boundary_reflectance.py`, `experiments/065-.../design_
geometry.py`, `experiments/048-.../design_geometry.py`, and `lab/fdtd2d.py::
Sim.add_line_source`. Independent computation this review: a from-scratch
reimplementation of `E_echo(theta_beam)` for C40 using only the raw
primitives (`dg065.CONFIGS`, `br.reflection_coefficient` scalar) — new to
this cycle, not copied from any Phase-2 critique, `y_wall_aperture_sum.py`,
or the Red Team audit — plus a quantitative near-field/Fraunhofer and
Nyquist-margin analysis, neither of which appears anywhere in the committed
record.*

---

## 1. Verdict: **PARTIAL** — the corrected record's own structural finding is
independently confirmed and, on inspection, airtight; Red Team's own
recommended next instrument is not electromagnetically free — it trades a
physically well-founded construction for a genuinely new, unproven, and on
this bench's own geometry probably poorly-justified approximation

The corrected `phase1_proposal.md` (Idealization 9, §4, §7) states the
model's entire `theta_beam`-dependence is carried by the shared driven-phase
ramp because `theta_local(y_s)` and `dist_image(y_s)` are static functions of
geometry — "the spatial Fourier transform of a `theta_beam`-independent
envelope." **I re-derived this independently, from raw geometry and the
scalar, already-gated `reflection_coefficient` (not the committed vectorized
form), and it is exactly right, with no hidden subtlety from the trapezoidal
discretization** (§2). The reflectance-ablation control folded into Phase 3
is the correct, decisive resolution of the disclosed R5 gap, and I concur it
supersedes a generic null-permutation control (§3). **My own charter
contribution — assessed directly against the task's own central question —
is that Red Team's §8/§9 recommendation (a plane-wave/global-steering
incidence-angle construction for the y-wall, mirroring the x-wall's own
two-plane-wave reduction) is *not* simply "the same trick, rotated 90°."**
The x-wall's reduction is not a plane-wave approximation at all — it is an
exact algebraic cancellation that holds at any range. No equivalent symmetry
exists for the y-wall, and this bench's own geometry (a wall sitting 2–4
wavelengths from the aperture's near edge, ~0.8%–2.1% of the aperture's own
Fraunhofer distance) puts the aperture deep in its Fresnel zone at the wall
— exactly where a single-global-angle plane-wave picture is least justified.
§4 works this through quantitatively; the recommended instrument is
electromagnetically *plausible* but not electromagnetically *free* the way
the write-up's own analogy implies, and should not be built without a
pre-registered validity check of its own.

---

## 2. Independent re-derivation: is `E_echo`'s entire `theta_beam`-dependence
really the Fourier transform of a fixed envelope, and does the discretization
hide anything a continuum argument would not have?

### 2a. The continuum claim, re-derived analytically from the formula itself

`echo_field_curve`'s own per-point integrand (§3.4 of the proposal, §[3] of
the script) is

```
dE(y_s;theta_beam) = w(y_s) * exp(i*k*sin(theta_beam)*(y_s - OBJ_Y))
w(y_s) = amp(y_s) * r(theta_local(y_s);ABSORB) * exp(i*k*dist_image(y_s))
```

with `w(y_s)` containing every ingredient that is *not* `theta_beam` —
confirmed directly by inspection of `theta_local_deg`/`dist_image_cells`
(neither takes a `theta_beam` argument anywhere in their signatures, and
`aperture_amplitude`/`r_of_ys` are computed once per `(config, oversample)`
and cached across the whole `theta_beam` sweep, §[3] of the script). So

```
E_echo(theta_beam) = INTEGRAL_{y_lo}^{y_hi} w(y_s) * exp(i*k*sin(theta_beam)*(y_s-OBJ_Y)) dy_s
```

is, term for term, the definition of the (continuous) Fourier transform of
`w(y_s)` — compactly supported on `[y_lo,y_hi]` — evaluated at spatial
frequency `k*sin(theta_beam)`, with the origin already centered at `OBJ_Y`
by the exponent's own `(y_s-OBJ_Y)` term (no separate phase factor needs
factoring out — the write-up's framing is exact as stated, not an
approximation of something subtly different). This is why the recovered
period is set by the *support width* of `w(y_s)` (the shared `[y_lo,y_hi]`/
`TAPER=40` window, identical to the real aperture's own) rather than by
`r(theta_local(y_s))`'s own values — a finite-window Fourier transform's
dominant oscillation frequency is fixed by the window's own extent,
regardless of what smooth or piecewise-smooth function is windowed. This
also explains, mechanistically and not merely by citation, PHOTONICS'
residual sideband (§5.3 of the corrected proposal): finite-window Fourier
transforms of a tapered top-hat generically carry side lobes at higher
spatial frequencies than the main lobe — exactly the kind of secondary,
smaller-amplitude structure a raised-cosine-tapered aperture's own transform
produces, with no need to invoke any new physical channel.

### 2b. From-scratch numerical reconstruction (not accepted on the write-up's word)

I built an independent script (this session's scratchpad,
`em_review_check.py`) importing *only* `dg065.CONFIGS` and the **scalar**,
already-gated `br.reflection_coefficient` — not `y_wall_aperture_sum.py`'s
own vectorized `reflection_coefficient_vec`, `echo_field_curve`, or
`build_aperture_grid` — and re-derived `theta_local`, `dist_image`, the
raised-cosine taper, and the trapezoidal integral independently for `C40`.
**First attempt did not reproduce the committed numbers exactly** (`Re{E_
echo}` at `theta_beam=36°/39°/42°` off by 1.2%–2.6%) — traced this myself,
before crediting anything, to a genuine bug in my own quick script: my
raised-cosine taper let the far-edge grid point (`y_s=y_hi`, one node past
the last real discrete source cell) extrapolate to a small nonzero value
(`0.00154`), while the committed `aperture_amplitude` correctly clips this
to exactly `0.0` (`np.clip(n-1-i, 0, None)` in the source) — the physically
correct choice, since a discrete `n`-cell taper array has no cell at that
index at all. **Once I substituted the committed `theta_local`/`dist_image`/
`amp`/`r_vec` arrays into my own independently-written trapezoidal-integral
loop, the result reproduces the committed JSON bit-exact**
(`Re{E_echo}(C40,36°)=6.831934930790395e-06`, etc., matching to every printed
digit) — confirming the formula, not merely the code path, is correctly
implemented. I also independently swept the **scalar** `reflection_
coefficient` against the **vectorized** one across the *entire* sampled
`theta_local` range (not just the write-up's own 5-point spot check):
`max |r_vec-r_scalar| = 8.063e-16` over 41 evenly-spaced sample points — the
vectorized form is trustworthy everywhere in this cycle's envelope, not just
at the five angles originally checked.

### 2c. Does the trapezoidal discretization hide a spurious `theta_beam`-dependent artifact? No — quantitatively confirmed, not merely converged-and-trusted

A discrete (trapezoidal-rule) approximation to a Fourier integral can, in
general, introduce spurious frequency-dependent structure (aliasing) once
the phase increment per sample approaches the Nyquist limit. I checked this
directly rather than relying only on the pre-registered convergence check:
at the native grid (`dy=1` cell), the phase increment per sample is
`k*sin(theta_beam)*dy`. At `theta_beam=36°/39°/42°` this is
`0.1847/0.1977/0.2102` rad — **5.9%–6.7% of the Nyquist limit (`pi` rad)** —
comfortably inside the safely-sampled regime, nowhere near the aliasing
threshold. This is a quantitative, first-principles reason (not merely an
empirical convergence pass) that the pre-registered `1x→2x→4x` check (§5.1
of the proposal, `2.4×10⁻⁴`→`1.5×10⁻⁵` relative change, correctly converging)
behaves exactly as it does: the integral was never close to under-resolved
in the first place. **Conclusion: the "spatial Fourier transform of a fixed
envelope" framing is exactly right for the continuum problem, and the
trapezoidal discretization introduces no additional, hidden `theta_beam`-
dependent structure of its own** — the convergence check the proposal
already ran is real evidence of this, and the Nyquist-margin calculation
above is the reason it had to come back clean, worth stating explicitly
since neither the proposal nor any Phase-2 critique computed this margin.

---

## 3. Passivity, reciprocity, causality — the bookkeeping this seat owns

**Passivity: clean, independently spot-checked, unaffected by any of this
cycle's own additions.** `G-PASSIVITY` at the full, never-before-sampled
`[4.77°,15.50°]` envelope reports worst `|r|=0.000115` — deep in the
near-total-absorption regime (consistent with every prior T28 cycle's own
finding for this `ABSORB`-band construction). Passivity is a property of the
`reflection_coefficient` transfer-matrix recursion itself (`|r|≤1` for any
`nu≥0` PEC-backed stack, at any angle fed to it) — it does not depend on
which physical *convention* (`theta_local(y_s)`, `90−theta_beam`, or a
hypothetical plane-wave incidence angle) supplies that angle, so this gate
would need to be, and should be, re-run fresh at whatever new angle range
any future construction introduces — exactly the discipline this sub-thread
has followed at every prior angle-convention change.

**Coherent aggregation does not itself threaten energy conservation.**
Summing many per-point contributions, each individually passive
(`|r(theta_local(y_s))|≤1`), is a linear superposition of physically valid
elementary reflections from a decomposition of the source into point
radiators — nothing about coherently adding sub-unity reflected
contributions can produce a total reflected field that violates energy
conservation of the aggregate system; this is a standard property of linear
passive superposition, not something this construction risks by summing
over ~1,504 points instead of one. No further check needed here.

**Reciprocity: not at risk, and — as at exp-078's own Phase-5 review of this
identical primitive — not actually the operative concern.**
`reflection_coefficient_vec`/`reflection_coefficient` enter `theta_deg` only
through `s2 = sin(theta)**2` (confirmed directly, `y_wall_aperture_sum.py`
line 226) — the function cannot distinguish `+theta` from `-theta`, an even
function about normal incidence, standard Fresnel/transfer-matrix behavior,
unaffected by which incidence-angle convention a caller supplies. No
source/observer exchange is performed anywhere in this file that would put
reciprocity itself in question. The substantive question this cycle raises —
and the one the task brief is really asking about under "reciprocity" — is
not whether `r(theta)` is reciprocal (it is, trivially, for any angle), but
whether a *given angle* correctly represents the physical incidence geometry
at all. That is a model-fidelity question, addressed directly in §4.

**Causality: no new concern.** This is a steady-state, single-frequency
(600nm) phasor calculation throughout, matching every other T28 cycle since
exp-069 — no transient/switching claim, no new causality question raised by
building a full aperture sum instead of a single-edge reduction.

---

## 4. The task's own central question: is a plane-wave/global-steering
incidence-angle construction for the y-wall electromagnetically sound — does
it correctly capture reciprocity/energy conservation for an obliquely-
illuminated finite-width wall band, or is the plane-wave picture just as
physically questionable there as it would be for the x-wall?

### 4a. The x-wall's own reduction is not a plane-wave *approximation* — it is an exact cancellation, valid at any range

Re-reading `phase1_proposal.md` [exp-078] §3.1 and independently re-deriving
it: mirroring the source through the `x=0` PEC wall flips only the
propagation direction's `x`-component; every aperture point keeps its own
`y_s` unchanged (the wall's normal is `x̂`, and every source point already
shares one `x=SRC_X` coordinate, so the mirror only ever touches that one
shared coordinate, never `y_s`). Both the driven-phase ramp
`k*sin(theta_beam)*(y_s-OBJ_Y)` **and** the amplitude taper `amp(y_s)` are
therefore *identical, term for term*, between the real aperture and its
image — the entire `y_s`-dependence cancels **before the aperture integral
is even taken**, collapsing what would otherwise be a full coherent sum into
an exact two-term (two-ray) interference, valid at *any* propagation
distance, not merely in some asymptotic far-field limit. This is why the
x-wall model has a genuine closed form (`P_x(theta)=(180/pi)*lambda/
(2*PLANE_X*sin(theta))`, no integral) reproduced bit-exact by both exp-075
and exp-078 — it is not a plane-wave/Fraunhofer *approximation* to the real
aperture's behavior; it is the real aperture's own exact behavior, because
the mirror symmetry makes the aperture's finite width irrelevant to the
phase difference by construction.

### 4b. The y-wall does not have this symmetry — already established, re-confirmed here, and the reason a "genuine analogue" needs its own justification

Mirroring through the `y=0` wall instead flips the very coordinate (`y_s`)
that both the driven-phase ramp and the taper depend on: the image aperture
spans `[-y_hi,-y_lo]`, disjoint from the real aperture's own `[y_lo,y_hi]`
(since `y_lo>0` for every congruent-series config), and the driven-phase
ramp evaluated at the mirrored coordinate,
`k*sin(theta_beam)*(-y_s-OBJ_Y)`, is a genuinely *different* function of
`y_s`, not a relabeling of the same one. There is no cancellation, and this
is exactly why `phase1_proposal.md` [exp-078] §1 states the "clean two-ray
reduction does not transfer" and why exp-078/079 built the full per-point
image machinery instead of a two-line closed form. **A "plane-wave/
global-steering" y-wall construction, proposed by direct analogy to the
x-wall, does not inherit the x-wall's own exactness for free — it would have
to be justified as an independent physical approximation**, standing or
falling on its own merits, not on the x-wall's precedent.

### 4c. Quantifying that independent justification against this bench's own geometry — and finding it weak

A "the aperture behaves as one plane wave at angle `theta_beam` by the time
it reaches the wall" claim requires the aperture to have effectively entered
its Fraunhofer (collimated/far-field) regime at the relevant propagation
distance — i.e., `distance >> W²/lambda`. Computed directly from this
cycle's own committed geometry (§0 of `_output.txt`, `W=aperture_cells=1504`
cells, `lambda=CPL[600]=20` cells):

```
W^2/lambda = 1504^2/20 = 113,101 cells        (Fraunhofer/far-field distance)
D_SP = 223 cells                               (source-to-wall x-clearance)
dist_image range = [861, 2347] cells           (image-to-observer distance, C40)
```

**The actual propagation distances at stake are 0.8%–2.1% of the Fraunhofer
distance** — two to three orders of magnitude short of it. This is not a
marginal near-field correction; it is deep Fresnel-zone territory, where a
finite aperture's field genuinely has *not* resolved into a single-direction
wavefront. This is not merely a textbook criterion asserted from outside —
**this cycle's own primitives directly confirm it empirically**: the
`theta_local(y_s)` envelope this file computed (`[0b]` of `_output.txt`)
spans `5.27°`–`15.00°` across the aperture, a **2.8× range** in the local
bounce angle different aperture points present to the wall/observer
geometry. If the aperture behaved as a single collimated beam at angle
`theta_beam`, this spread would shrink toward a common value as distance
grows; instead it is large and systematic (near edge grazes closer to
normal incidence, far edge grazes closer to the wall's own plane) — direct,
already-computed evidence that no single global incidence angle
characterizes how this aperture actually meets this wall. (`k*r` at the
near/far edge, `271`/`737`, is separately large — confirming the *point-
source* stationary-phase approximation each individual `theta_local(y_s)`
rests on is itself well-justified; this is a different "far field" criterion
than the aperture's own collimation distance, and satisfying one does not
imply the other — a distinction worth stating explicitly since conflating
them is an easy mistake here.)

### 4d. A second, smaller idealization: the wall band's own finite lateral extent

Separately from 4c: `Sim._damping` applies the graded-loss ramp across the
*entire* domain width in `x` (`nx=360` cells for `C40`, up to `440` for the
`PAD=40` configs) — comparable to, though somewhat larger than, the beam's
own relevant `x`-footprint (`D_SP=223` cells between `SRC_X` and
`PLANE_X`). `boundary_reflectance.py`'s transfer-matrix reflectance assumes
a laterally-*infinite*, uniform layered stack; any plane-wave-incidence
construction inherits this same assumption and, by extension, neglects
diffraction from the wall band's own `x`-extent edges. The beam's footprint
sits with roughly 70–140 cells of margin inside the wall's own extent on
each side, so this is a real but almost certainly secondary idealization
next to §4c's near-field issue — worth disclosing if this instrument is
built, not a reason on its own to avoid building it.

### 4e. The conflation risk this exact sub-thread has already caught twice

A plane-wave-incidence y-wall model that simply plugs `theta_beam` (or
`90-theta_beam`) into `r()` as though that quantity were the field's actual
local propagation direction *at the wall* is the same move already tried
and found not rigorous at exp-078 Phase 5 for the point-source construction
— there, `theta_beam` is a **source-side steering parameter** (it sets how
the aperture is *driven*), not automatically the local field's true
propagation direction at any specific downstream location. Re-deploying
that identification inside a different representation (a putative single
global plane wave, rather than one point's own geometric ray) does not
repair the conflation on its own — it requires a fresh, independent argument
for why the field *near the wall* genuinely propagates as one ray at angle
`theta_beam`, and §4c's numbers argue the opposite: the aperture is deep in
its own near field there, with a 2.8× spread in local geometry already
measured. This is not a hypothetical risk; it is the *same failure shape*
this exact sub-thread has now caught at exp-078 Phase 2 (the as-filed
`theta_beam` bug) and exp-078 Phase 5 (the "corrected" `90-theta_beam` bug)
— a third instance would not be a surprising outcome, it would be the base
rate.

### 4f. Net answer

**Not electromagnetically free, and more questionable for the y-wall than
for the x-wall, not merely equally questionable.** The x-wall's picture is
exact at any range; a y-wall plane-wave picture would be a genuinely new,
unproven approximation, and this bench's own geometry (§4c, computed
directly from committed primitives, not assumed) argues it is a *poor* one
at the distances actually in play here. This does not mean the instrument
is unsound to attempt — it is the only construction in this family that
could, in principle, escape Attack 1's mathematical trap, since a plane-wave
reflectance term genuinely depends on `theta_beam` by design — but it should
not be built and trusted on the strength of the x-wall analogy alone. It
needs its own pre-registered validity check (§6, ranked item 1) before its
period-comparison numbers are treated as informative about the wall's real
reflectance, the same discipline this program applied to every prior
angle-convention change on this exact sub-thread.

---

## 5. Does this change how T28's board should be read?

No change to the Combined Verdict, the Test-A numbers, or the ablation
control's own conclusion — all independently re-derived above and correct.
What this review adds is a caution specifically about what comes *next*:
Red Team's own §8/§9 recommendation is the right *direction* (a construction
that breaks the static-per-point-angle pattern is the only way to escape
Attack 1's structural trap), but it is not a *validated* instrument yet, and
should not be treated as one merely because it "mirrors" a construction this
program already trusts for a differently-symmetric wall.

---

## 6. Ranked top-3 candidate directions for Iteration 57 (my own seat, EM)

1. **Before spending any effort on a full plane-wave/global-steering y-wall
   build, run a cheap, zero-FDTD desk pre-check of its own basic premise**:
   compute the Fraunhofer-distance margin and the `theta_local(y_s)` spread
   this review used (§4c) as a stated, pre-registered validity gate — and,
   more decisively, test whether *any* single "effective angle" summary
   (e.g., `theta_beam` itself, `90-theta_beam`, or an amplitude-weighted
   average of `theta_local(y_s)` over the illuminated aperture) reproduces
   the full per-point coherent sum's own envelope structure to a stated
   tolerance. Attack 1's own math already predicts this test must fail (the
   real `theta_beam`-dependence is carried *only* by the driven-phase ramp,
   never by any reflectance-angle choice) — running it explicitly turns that
   prediction into a committed, falsifiable check, and cheaply forecloses
   (or, if it somehow does not fail, sharply informs) whether a plane-wave
   construction is worth building at all.
2. **If a plane-wave/global-steering model is built anyway, gate it, before
   any number from it is trusted, on**: (a) a fresh `G-LOSSLESS`/`G-N1`/
   `G-PASSIVITY` re-run at whatever new angle range it introduces (routine,
   cheap, this sub-thread's own established discipline, §3); (b) an explicit,
   pre-registered statement of its own governing near-field/collimation
   idealization, quantified as in §4c — not asserted by analogy to the
   x-wall — as a disclosed Idealization from the moment it is filed, not a
   Phase-5 correction found after the fact a fourth time on this exact
   sub-thread.
3. **Independent of the plane-wave question, this sub-thread's own
   still-longer-deferred items remain higher-certainty uses of the next FDTD
   budget**: the 750nm x-wall two-wall spot-check (oldest unexecuted item on
   the whole T28 board, PHOTONICS/EM), the full-width non-aliased `G40`
   wavelength leg (now deferred three consecutive cycles), and whether
   `PAD`-sensitivity survives with a real absorbing article loaded (also
   deferred three consecutive cycles, per LOGBOOK's own standing caution
   that a fourth deferral needs an explicit stated reason). None of these
   are contingent on resolving the plane-wave question first, and all three
   cost less than building a new, unvalidated instrument.

---

## Compliance note

No RULED-OUT item (R1–R9) is re-opened or re-proposed here. §2/§4 are new,
independently-computed findings — a from-scratch numerical reconstruction of
`E_echo` (§2b), a quantitative Nyquist-aliasing margin (§2c), and a
Fraunhofer/near-field-distance calculation against this cycle's own
committed geometry (§4c) — none of which appear in `phase1_proposal.md`, any
of the five Phase-2 critiques, or `phase2_redteam_audit.md`. Consistent with
R5's look-elsewhere discipline: §6 item 1 is framed as a single, pre-
registrable validity check, not a new dense parameter search. Consistent
with R8: this review computes the near-field margin and the reproduction
check itself (§2b, §4c) rather than asserting an argument about either
without running it.
