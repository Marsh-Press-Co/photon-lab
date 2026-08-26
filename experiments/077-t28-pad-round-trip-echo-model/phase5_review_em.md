# PHASE 5 — REVIEW (ELECTROMAGNETISM, blind) · Panel Iteration 54 · exp-077

*Fresh sub-agent, ELECTROMAGNETISM charter: field/wave behavior, impedance
matching, energy coupling; owns reciprocity/passivity/causality bookkeeping.
Blind to all other seats' Phase-5 reviews, including my own Phase-2
critique of this same cycle. Grounded on PANEL.md, LOGBOOK.md (RULED OUT
R1–R8, T28's full Iteration 46–53 history), and the complete exp-077
record (`phase1_proposal.md`, all five Phase-2 critiques,
`phase2_redteam_audit.md`, `phase3_synthesis.md`, `phase4_results.md`,
`NOTES.md`, `pad_round_trip_model.py`, `pad_round_trip_results.json`).
Independent computation this review: `pad_round_trip_model.py` re-run
end-to-end (bit-identical to the committed JSON); a new standalone script
built from the same imported, already-vetted primitives
(`boundary_reflectance.py`, `two_wall_cavity.py`, `design_geometry.py`)
that neither cycle's committed code nor any prior review contains.*

---

## 1. Verdict: **RULED OUT** (for the mechanism class this cycle tests),
**not yet RULED OUT** for T28's overall periodicity question

From EM's own field/energy bookkeeping lens, the specific claim this cycle
adjudicates — a single or double coherent echo off the domain's two
**x-normal** PEC walls (near + far, weighted by the graded-loss band's own
`r(theta;ABSORB)`) explains the dominant `PAIR_PAD` signal — is cleanly,
robustly **RULED OUT**. The instrument is sound (gates re-verify:
G-LOSSLESS `2.220e-16`, G-N1 `1.404e-15`, G-PASSIVITY worst `|r|=0.006423`,
independently re-run by me and bit-identical), the isolation is verified in
code (not merely asserted — `r_for["C40"] is r_for["G40"]`, same array
object, confirmed at `pad_round_trip_model.py` line 177 as filed), and I
found no defect in either the single- or two-wall REFUTE. This joins
exp-075's own `ABSORB`-boundary REFUTE as the second boundary-echo
mechanism killed for T28.

But — see §3 below — this is a RULED-OUT verdict on the **x-direction**
boundary-echo sub-class specifically, not on "coherent domain-boundary
echo" as a whole. The domain has four PEC-backed graded-loss walls, not
two; only the pair aligned with the beam's principal propagation axis has
ever been priced. T28's own substantive question (the periodicity's
origin) is **PARTIAL**, not closed.

---

## 2. Independent check: the "same `r(theta)` for both walls" premise,
re-derived from first principles, not re-cited — plus an energy-balance
decomposition neither this cycle nor exp-075 ever computed

### 2a. Is "mirror-symmetric launch angle" actually true for *this* geometry, or inherited prose?

I checked whether the shared premise underneath `two_wall_cavity.py`'s
three-term coherent sum — "same `r(theta;ABSORB)` weights both walls'
images, justified [in exp-075's `phase3_synthesis.md` §3.3] by mirror-
symmetric launch-angle magnitude" — is (a) actually re-verified against
*this cycle's* three geometries (`C40`, `G40`, `C80`, with their genuinely
different `PLANE_X`/`SRC_X`/`nx`), or (b) simply inherited, unchecked,
because it was true once for a different pair. Neither `phase1_proposal.md`
nor any of the five Phase-2 critiques nor the Red Team audit re-derives it
— all treat it as settled by exp-075's citation. I re-derived it two
independent ways, both against code, both new to this cycle's record:

**Check 1 — is `reflection_coefficient` itself direction-symmetric?**
I called `boundary_reflectance.py::reflection_coefficient(n_exact, +39.0,
CPL[600])` and the same at `-39.0`. Result: `(0.003226−0.002796j)` at both
— **bit-identical**, not merely close. This is exact because the formula
(`boundary_reflectance.py` lines 191–195) enters `theta_deg` only through
`s2 = sin(theta)**2`, which is even in `theta` by construction — the
function is incapable of returning a different value for `+theta` vs.
`-theta`, for *any* `ABSORB`, `PLANE_X`, or `PAD`. So "same `r` for both
walls" reduces to "same `|incidence angle|` at both walls," which is the
next question.

**Check 2 — do both walls actually see the same `|incidence angle|` in
this geometry?** I traced `design_geometry.py::_src_amp`, the function
that imposes the steering phase used identically by the direct, left-image,
and right-image terms: `phase = k*sin(theta_deg)*(y_src − obj_y)`. This
expression has **no dependence on `d_sp`, `PLANE_X`, or `SRC_X` at all** —
the transverse spatial frequency `k_y = k·sin(theta)` imposed on the source
aperture is fixed by `theta_deg` alone. By the dispersion relation
`k_x² + k_y² = k²`, this forces `|k_x| = k·cos(theta)` — identical in
magnitude for a component propagating toward either wall, *regardless of*
`PLANE_X`, `SRC_X`, `nx`, or `PAD` — because both walls' normals point
along the same axis (`x`), so the angle a fixed-`k_y` wave subtends from
either wall's normal is the same `theta` by construction of the dispersion
relation, not by a geometric coincidence that could fail for a particular
`PAD` value. Combined with Materials'/Red Team's already-independently-
confirmed finding that both walls' damping ramps are bit-identical
(`lab/fdtd2d.py::_damping`, worst diff `0.000e+00` across all four edges,
`phase4_results.md` fix 3) — same layer profile, same incidence angle,
same (even-in-theta) formula — **the "same `r` for both walls" premise is
not an approximation that happens to hold for this cycle's numbers; it is
exact for this instrument class, for any `D_left`/`D_right` asymmetry.**
`D_left_img`/`D_right_img` differ substantially and asymmetrically between
configs (verified: `C40` 377/341, `G40`/`C80` 457/421 cells — the far wall's
image is *closer* than the near wall's in both configs, since the source
sits nearer the far wall physically), but none of that distance asymmetry
threatens the angle argument, which never depended on distance. **This is
a genuinely new Phase-5 finding — the assumption was inherited by citation
in every phase of this cycle and never independently re-derived until now
— but it resolves in the model's favor: no hidden geometry-dependent flaw,
and the REFUTE verdicts rest on solid ground.**

### 2b. Energy balance: does adding a second lossy wall's echo behave sanely?

Neither `phase1_proposal.md` nor any critique ever separated the two-wall
model's two coherent terms to check whether the resulting amplitude growth
is physically bounded. I built a standalone decomposition (reusing
`c_empty_with_wall`/`image_geometry_right` verbatim, isolating left-only
and right-only echo contributions) and computed each wall's *own*
standalone contribution to `PAIR_PAD`'s and `PAIR_ABSORB40`'s predicted
`delta(theta)`:

| | left-wall-only `ptp` | right-wall-only `ptp` | filed single-wall (=left-only) | filed two-wall (coherent sum) | ratio two-wall/single-wall |
|---|---|---|---|---|---|
| `PAIR_PAD` | `2.2317e-3` | `1.1661e-3` | `2.2317e-3` (exact match, sanity-confirmed) | `3.0251e-3` | `1.356×` |
| `PAIR_ABSORB40` | `1.4972e-3` | `0.9042e-3` | `1.4972e-3` | `2.1492e-3` | `1.436×` |

Two things worth recording. **First**, the two walls' *individual*
contributions are meaningfully unequal (right/left ≈ 0.52–0.60) despite
carrying the identical `|r(theta;ABSORB)|` weight (§2a) — this is
explained entirely by the different image-to-plane propagation distances
(`D_left_img`/`D_right_img` above; the Huygens-Fresnel `1/√r` decay and
different diffraction geometry, not a different reflectivity), a
consistent, non-alarming story. **Second**, and this is the actual energy
check: for two coherently-summed terms of unequal individual amplitude
`A=2.232e-3` and `B=1.166e-3` (using `PAIR_PAD`'s numbers) at *different*
periods (no fixed phase relationship across the 6°-wide window), the
physically-available range for the sum's peak-to-peak is bounded by
`|A−B|=1.066e-3` (near-total destructive overlap) at one extreme and
`A+B=3.398e-3` (near-total constructive overlap) at the other — this is
just the triangle inequality applied to two passive (`|r|≤1`), weakly-
coupled scatterers, nothing more. The observed two-wall `ptp` (`3.025e-3`
for `PAIR_PAD`, `2.149e-3` for `PAIR_ABSORB40`) **sits inside that bound in
both cases** — 84% and 86% of the way, respectively, from the destructive
extreme (`|A−B|`) toward the fully-constructive extreme (`A+B`) — both
walls are lossy, so this is expected: two similarly-weak, similarly-signed
scatterers summing mostly (not perfectly) constructively over most of a
narrow window is unremarkable, not super-radiant, and nothing here exceeds
what two independently-passive reflectors can produce. **No energy-
bookkeeping red flag.** This also
gives a clean, independent explanation for something the filed record
notes but does not derive: why Test A's period match *improves* while Test
B's shape match *collapses* on the two-wall cut — summing two comparable-
amplitude sinusoids at genuinely different periods (`P_left(39°)=2.42°`,
`P_right(39°)=2.67°` for `C40`'s own image geometry, by the direct-
computation route, not the closed-form `PLANE_X`-only proxy) produces a
beat-like waveform whose *single best-fit period* can drift toward the
real data's period by chance while its *shape* necessarily diverges
further from either constituent curve — exactly the "different tests, same
REFUTE" pattern `phase4_results.md` reports, now with a first-principles
mechanism behind it rather than just the observed numbers.


---

## 3. Has the coherent-domain-boundary-echo mechanism class now been fully
exhausted, or does an untested boundary configuration remain?

**Not fully exhausted — a genuinely distinct, untested boundary
configuration remains, though it is a harder lift than either echo model
built so far, not a trivial refit.**

- **Multi-bounce beyond one round trip per wall: already quantitatively
  closed, not open.** exp-075's own idealization (carried unchanged into
  this cycle, §6 item 1–8) bounds a double-bounce term at `|r|² ≤ 4.1×10⁻⁵`
  — over 150× smaller than the single-bounce terms, which are themselves
  already 2.4–4.2× too small to match the real amplitude (`phase1_proposal.md`
  §5, "Amplitude, disclosed"). No further work is owed here; re-litigating
  it would violate this program's own look-elsewhere discipline (R5) by
  chasing a term already shown negligible.

- **Corner effects (where an x-normal wall meets a y-normal wall):**
  untested, but very likely sub-dominant — corner-scattered energy from a
  graded-loss boundary is a higher-order, more strongly diffracted
  contribution than either principal wall's specular-like echo, and no
  quantitative argument in this program's history assigns it comparable
  weight. Not worth building before cheaper items are tried.

- **The y-direction (top/bottom) walls: the actually open item.** I
  independently confirmed (re-reading `lab/fdtd2d.py::_damping`, the same
  four-edge construction Materials/Red Team already verified for the
  x-edges in this cycle's own audit) that the **same** `self.absorb`-
  parameterized cubic damping ramp is applied to the `y=0`/`y=ny-1` edges,
  not just `x=0`/`x=nx-1`. Every echo model built for T28 so far —
  exp-075's single-wall, exp-075's two-wall extension, and this cycle's
  refit — has priced *only* the two walls aligned with the beam's
  principal propagation axis (`x`). The two walls perpendicular to it have
  never entered any model. This is a physically distinct configuration,
  not a relabeling of what's already been tested: a wave with wavevector
  `(k cosθ, k sinθ)` meets a **y-normal** wall at incidence angle
  `(90°−theta)` from *that* wall's normal, not `theta` — so `r(theta;ABSORB)`
  cannot simply be re-used at the same angle argument, and the existing
  `image_geometry`/`image_geometry_right` functions (which mirror through
  x=const planes, holding y fixed) do not generalize to a y=const mirror
  without a new construction (mirroring the *y*-extent of the aperture,
  `y → 2·y_wall − y`). **Caution, stated plainly so Iteration 55 does not
  spend the FDTD-free budget on a foregone conclusion:** the natural
  "reference distance" for a y-wall echo is `A = obj_y − y_lo = 752` cells
  — the *same* length scale T21's own already-tested edge-diffraction
  fringe model uses (`P(θ)=λ/(A·cosθ)≈1.96°`, LOGBOOK's original T28-
  founding citation), which is already established to sit ~45% from T28's
  own period and fit T28's data far worse than the freely-fit `A_eff≈518.8`
  (`R²=0.35` vs `0.77` at 750nm, Iteration 46). A y-wall coherent-echo
  model that turns out to share this same dominant length scale would
  likely inherit that same mismatch rather than open new ground — this
  should be checked with a **zero-cost closed-form period estimate**
  (analogous to `two_wall_cavity.py`'s own `closed_form_period`, correctly
  re-derived for grazing incidence, not copy-pasted) *before* any new
  image-geometry machinery is built, exactly the discipline this
  sub-thread's own R5/R8 house rules require.

---

## 4. Ranked top candidate directions for Iteration 55 (my own top 3)

1. **A zero-FDTD closed-form period pre-screen of the y-direction
   (top/bottom) wall echo, before building any new image-geometry code.**
   Derive the correct grazing-incidence period formula for a wall whose
   normal is transverse to the beam's principal axis (not a copy of
   `closed_form_period`, which assumes an x-normal wall), evaluate it at
   `A=752` (and, separately, at the actual aperture-to-wall distance for
   each of `C40`/`G40`/`C80`, since `PAD` shifts `y_lo` too), and compare
   to T28's established `P*≈2.84°`/`4.2–4.6°` periods. If it lands as close
   to T21's own `1.96°` as the §3 caution above suggests, this sub-
   mechanism can likely be desk-closed in under an hour without ever
   writing the full `y`-mirrored propagator; if it lands somewhere new,
   *then* it is worth the moderate (not trivial) lift of building the
   correct incidence-angle convention and image geometry. Either outcome
   narrows the board.
2. **Score the already-built two-wall model against the already-collected
   750nm leg** (`experiments/069-.../results.json::block_leg750`) — carried
   unexecuted from Iteration 53's own ranking (item 3) through this cycle;
   zero new FDTD, and a genuine cross-wavelength consistency check on a
   mechanism now REFUTEd at 600nm — if the two-wall model's REFUTE holds
   at 750nm too, that strengthens confidence this specific mechanism class
   is closed at more than one wavelength point; if it doesn't, that
   disagreement is itself informative.
3. **A Red Team reckoning on Checkpoint criterion 2 candidacy, scoped
   correctly.** Two x-wall coherent-echo mechanisms are now REFUTEd
   (exp-075's `ABSORB`-boundary; this cycle's `PAD`-round-trip, both single-
   and two-wall cuts). That is real, hard-won negative evidence for the
   *x-direction* boundary-echo sub-class specifically — but §3 shows the
   full "coherent domain-boundary echo" mechanism class is not yet
   exhausted (the y-walls remain genuinely untested). I recommend Red Team
   assess Checkpoint criterion 2 (a proven, jointly-unsatisfiable mechanism-
   class boundary) as **not yet ripe** — scoped narrowly to "x-normal
   single/double wall echo," not the broader class — until item 1 above
   either closes or opens the y-wall sub-case. Declaring the full class
   exhausted one cycle early would repeat the shape of gap R7/R8 exist to
   prevent: a boundary claimed closed on an argument (or, here, an
   unpriced remaining configuration) rather than an actually-run check.

---

## Compliance note

No RULED-OUT item (R1–R8) is re-opened or re-proposed here. This review
adds two new, independently-computed findings not present anywhere in the
committed record (the first-principles re-derivation of the mirror-
symmetric-launch-angle premise, §2a; the left/right energy-balance
decomposition, §2b) and one new, scoped-cautiously candidate direction
(§3–4), consistent with R5's look-elsewhere discipline (the y-wall
proposal is explicitly flagged as possibly sharing T21's already-tested
length scale, to be checked cheaply before any new machinery is built) and
R8 (I ran the checks myself rather than asserting an untested robustness
argument).
