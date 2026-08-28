# PHASE 1 — PROPOSAL · Panel Iteration 61 · exp-084 · Lead seat: PHOTONICS

## "The Source Aperture's Own Two Edges, Treated as Fresnel Diffractors, Not a Far-Field Grating" — a zero-FDTD near-field re-derivation of T28's founding periodicity

### 1. Mechanism narrative (≤300 words)

Every prior T28 mechanism cycle (exp-075/077/078/079/080/081) modeled the
graded-loss `ABSORB` band as a **reflector** — a specular echo with a
transfer-matrix `r(θ)`, image sources, cavity round-trips — and every one
was REFUTEd or foreclosed. None modeled the source's own finite, tapered
aperture as what near-field diffraction theory says a finite aperture edge
actually is: a **diffractor**. I propose computing the genuine near-field
(Fresnel) diffraction pattern produced by the two tapered edges of the
source aperture itself (`y_lo`, `y_hi`), using the exact 2D scalar
Huygens–Fresnel propagation integral — not the paraxial, far-field
(Fraunhofer) grating approximation that produced `P_edge_B` and was
already refuted (45% off `P_edge_A`).

This is a priori plausible precisely because of the near-field diagnostic
already on record: the Fraunhofer distance for this aperture,
`W²/λ = 1504²/20 = 113,101` cells, is 507× the actual source-to-plane
distance `D_SP = 223` cells (0.2% of Fraunhofer range). `P_edge_B`'s
formula, `P(θ) = λ/(A·cosθ)`, is the small-angle stationary-phase reduction
of the exact diffraction integral valid *only* once that Fraunhofer
condition holds — applying it here is a category error, not a mechanism
error, and is the leading candidate reason it misses by 45%. A rigorous
near-field treatment introduces a **different natural length scale**,
the Fresnel zone width `√(λ·D_SP) ≈ 66.8` cells, set by the propagation
distance rather than the aperture's full width `A` — a structurally
different quantity, not a re-tuned version of the same formula.

Concretely: I evaluate the exact (no far-field approximation) coherent
Huygens sum already validated on this bench (`edge_diffraction_c_empty_
corrected`) at the true near-field geometry, and separately isolate each
tapered edge's own Fresnel-integral (`C(v)`, `S(v)`) contribution to
interpret *why* any resulting period differs from `P_edge_B`. No ABSORB
band, no reflection coefficient, no image source anywhere in this
derivation.

### 2. Parameter table

Every value below is sourced to a committed file, not hand-typed (R4).

| Quantity | Value | Source |
|---|---|---|
| Source-aperture half-width `A` | 752 cells | `dg065.CONFIGS["C40"]["A"]` (congruent across C40/C60/C70/C80/G40 by construction, verified by a live assert in `design_geometry.py`) |
| Full aperture width | 1504 cells | `dg065.CONFIGS["C40"]["aperture_cells"]` |
| Taper half-width `TAPER` | 40 cells | `dg065.TAPER`; functional form: raised-cosine (Hann) ramp, `p(i) = 0.5·(1−cos(πi/40))` for `i∈[0,40)` at each end, `p≡1` in the flat interior — bit-identical to `Sim.add_line_source`'s own array, reproduced by `dg048.aperture_profile` |
| Wavelength `λ` | 20 cells (600 nm) | `CPL[600]`, `dg065.CPL` |
| Source→observation-plane distance `D_SP` | 223 cells | `dg065.D_SP = BASE_SRC_X − BASE_PLANE_X` |
| Observation-plane→article distance `LEVER` | 93 cells | `dg065.LEVER = BASE_OBJ_X − BASE_PLANE_X` |
| Angle sweep | 36.0°→42.0°, 0.2° step, 31 points, center 39° | `dg065`/exp-069's `DENSE_ANGLES` |
| Article rim half-separation (secondary target only) | `R_OUT = 78` cells (`Δy = 2·R_OUT = 156` cells) | `dg065.R_OUT` |
| Fraunhofer distance, source aperture | `A_full²/λ = 1504²/20 = 113,101` cells | desk arithmetic on the row above |
| Actual/Fraunhofer ratio, source aperture | `D_SP/113,101 = 0.197%` | desk arithmetic — deep Fresnel regime |
| Fresnel zone width, source aperture | `√(λ·D_SP) = √4460 ≈ 66.8` cells | desk arithmetic; the length scale this mechanism substitutes for `A` |
| Fresnel number, article rim | `N_F = Δy²/(λ·LEVER) = 156²/(20·93) ≈ 13.08` | dossier / desk arithmetic — also deep-to-moderate Fresnel, not far field |
| Free-period search machinery | `_free_period_search`, staged widening `[1°,4°]→[1°,15°]`, center 39° | `experiments/069-.../run.py`, reused verbatim (not reimplemented) by exp-077/078/083 |

Not used by this desk derivation (listed for completeness, since they
appear in the dossier): `ABSORB`, `PAD`, `STEPS`, `COURANT_FRAC` — this
mechanism is, by construction, independent of the graded-loss boundary
entirely (see Idealization 5 and the falsifiable structural corollary
below).

### 3. T1 escape-route statement

**N/A — instrument/model-fidelity thread, identical disposition to every
T28 cycle since exp-069 (069, 075, 077, 078, 079, 080, 081, 082, 083).**
This derivation characterizes the FDTD bench's own diffraction physics at
a specific, already-built geometry; it proposes no absorption mechanism,
no σ(I)/σ(x,t)/angular-selectivity/sub-threshold escape route, and touches
no constraint-3 scene. Checkpoint criterion 2 (mechanism-class boundary)
is likewise N/A this cycle, matching exp-083's own explicit ruling — this
is artifact-attribution work internal to the lab's instrument, unconnected
to any phenomenon-program constraint.

### 4. Falsifiable predicted outcomes

**Convention adopted** (matching the sub-thread's own established
`rel_dev ≤ 0.20` AND `R² ≥ 0.30` "within tolerance" bands — exp-069
P-069-3, exp-077 Test A, exp-083's three-branch discriminator): reused
here, not re-invented, for direct comparability with every prior T28
period-matching verdict on this exact metric. `rel_dev = |P_model −
P_target| / P_target` throughout.

**(a) Empty-scene target, `P_edge_A = 2.8421°`** (measured from the
free-period fit of `delta(θ) = C80(θ) − C40(θ)`, but per exp-070's own
established finding, the same `~2.8°`-family signal lives in `C40(θ)` and
`C80(θ)` **individually** — the honest target for an ABSORB-independent
mechanism is the period of the model's own predicted curve at ONE
config's exact geometry, since the mechanism is structurally incapable of
distinguishing C40 from C80, see the structural corollary below):

- **SUPPORT**: `R² ≥ 0.30` AND `rel_dev(P_model, P_edge_A) ≤ 0.20`.
- **INCONCLUSIVE**: `R² ≥ 0.30` AND `0.20 < rel_dev ≤ 0.50`, OR the
  specificity control (below) shows the SUPPORT band is not usefully
  selective at this `R²`.
- **REFUTE**: `R² < 0.30` (no genuine periodic structure recovered at
  this window), OR `R² ≥ 0.30` AND `rel_dev > 0.50` (a clear, confident
  miss — matching `P_edge_B`'s own already-refuted 45% miss as the
  reference scale for "clearly wrong").

**Structural corollary, pre-registered now**: because this mechanism uses
only `A`, `TAPER`, `λ`, `D_SP` — all congruent/ABSORB-independent by
construction — it predicts `delta_model(θ) ≡ 0` (to floating-point
precision) for `C80(θ) − C40(θ)`. This is stated as a falsifiable
structural prediction, not swept aside: if the real, non-zero
`C80(θ)−C40(θ)` signal's period turns out to depend on genuine
ABSORB-tied physics after all, this mechanism cannot be the (sole)
explanation of the *difference* — only, at best, of a shared component
present identically in both raw curves. Both readings are scored openly.

**(b) Article-rim target, `P* = 2.9474°`** (exp-083's own `C40`-vs-`G40`,
article-loaded re-test — the secondary, cheaper comparison named in this
cycle's own assignment): same construction applied to the disk's own two
rim edges (`y = obj_y ± R_OUT`), propagated over `LEVER = 93` cells to the
observation plane by the identical Fresnel-integral method.

- **SUPPORT**: `R² ≥ 0.30` AND `rel_dev(P_model, P*) ≤ 0.20`.
- **INCONCLUSIVE**: `R² ≥ 0.30` AND `0.20 < rel_dev ≤ 0.50`.
- **REFUTE**: `R² < 0.30`, OR `rel_dev > 0.50`.

Both (a) and (b) are scored independently; the Combined Verdict is the
pair, not a single collapsed label (matching exp-083's own three-branch
practice), since this cycle addresses two structurally different targets
(source aperture vs. article rim) with the same method.

**R5 null-permutation / specificity control — pre-registered now, per
house rule (RULED OUT, R5 and its addenda: any free-period search needs a
look-elsewhere control before a match counts as evidence).** Because the
model curve is scored via a free-period search (not a closed-form,
zero-free-parameter formula like `P_edge_B`'s), the fitting procedure
itself has flexibility that a raw `rel_dev` number cannot rule out (the
exact failure shape exp-083's own Phase-5 audit found in QUANTUM's
phase-shift claim: 99.3% of arbitrary periods in `[1°,15°]` admitted an
equally good match). Before any SUPPORT is reported for (a) or (b), I
will run a **specificity sweep**: re-score the SAME model curve's `R²`
against a dense grid of ≥50 candidate target periods spanning `[1°,15°]`
(this sub-thread's own established scoring range) and report what
fraction of that grid *also* clears the `rel_dev ≤ 0.20` SUPPORT band —
if that fraction is not small (informally, comparable to the ~20%
"chance" width the band itself allows, i.e. this is not a narrow,
peaked, informative match), the result is downgraded to INCONCLUSIVE
regardless of the raw `rel_dev` number, exactly as exp-083's own Red Team
audit did to QUANTUM's phase-shift finding. This is a specificity/
look-elsewhere control, not a full Monte-Carlo null-hypothesis test
(there is no random noise process here — the model curve is
deterministic); it is the correct R5 analogue for a deterministic
free-period fit, as distinct from the permutation nulls used elsewhere on
noisy real FDTD data.

### 5. Idealizations

1. **2D scalar Huygens–Fresnel diffraction**, not the bench's own 2D
   vector (TMz) Maxwell/FDTD solution — reuses the same E/H convention
   already validated in `field_and_h` (E from the bare coherent sum, H
   from the obliquity-weighted sum, Faraday's law for this bench's
   line-current soft source), itself an idealization of the true FDTD
   fields.
2. **Single wavelength, 600 nm (`cpl=20`) this cycle only** — no
   750/450 nm generality claim; the standing x-wall wavelength-generality
   leg (now 8 cycles deferred) is untouched by this desk cycle.
3. **Near-field but not the full FDTD near-field**: the propagation
   integral itself is either (i) the exact free-space 2D Green's function
   sum (`G0 = exp(i(kr−π/4))/√r`, valid for `kr≫1`, no paraxial/small-angle
   approximation — already the bench's own validated choice in
   `edge_diffraction_c_empty_corrected`), or (ii) the classical Fresnel
   knife-edge integral (`C(v)`,`S(v)`) used for interpretation/cross-check
   of a single tapered edge in isolation — both are still vacuum,
   boundary-free, homogeneous-medium diffraction theory, not a solution of
   Maxwell's equations in the actual graded-index/graded-loss FDTD medium.
4. **No absorbing/lossy medium anywhere in this derivation** — the
   `ABSORB`/`PAD` graded-loss bands play no role; this is the explicit
   point of testing a diffractor mechanism, and the consequence (predicted
   zero `C80−C40` difference) is pre-registered as a structural, falsifiable
   corollary above, not hidden.
5. **Raised-cosine taper treated via its own aperture-amplitude weighting**,
   not re-derived as an independent "TAPER-as-sub-aperture" mechanism —
   that specific sub-hypothesis was already cleanly REFUTEd (exp-070,
   P-070-3, 1197% miss); here the taper only shapes the amplitude profile
   feeding the same diffraction integral, never scored as its own separate
   diffractor.
6. **Coherent, monochromatic, steady-state (CW) fields** — no pulse, no
   transient, matching the bench's own CW convention throughout T28.
7. **Article-rim leg (b) treats the disk as two independent point-like
   edges at `y=obj_y±R_OUT`**, ignoring any diffraction re-radiated from
   the disk's own curved surface between the two rim points (a further
   idealization on top of (1)-(3), disclosed and not defended as exact —
   consistent with `N_F≈13` meaning the disk sits closer to resonance/
   moderate-Fresnel than the source aperture's own deep-Fresnel regime).

### 6. Realizability / cost note

Zero new FDTD calls. This is a pure Python desk calculation reusing
already-committed, already-validated machinery (`dg048.field_and_h`,
`dg048.edge_diffraction_c_empty_corrected`, `dg048.aperture_profile`,
`dg065.CONFIGS`, and the `_free_period_search` staged-widening idiom from
`experiments/069-.../run.py`), plus a small new Fresnel-integral
implementation (`scipy.special.fresnel` or an equivalent closed-form
series) for the interpretive edge-isolation cross-check and the new
two-edge article-rim propagation in leg (b). No `lab/` engine change, no
trust-suite implication, no realizability claim (MATERIALS' seat, not
engaged this cycle — this thread carries zero realizability content by
construction, matching exp-083's own standing framing rule for the whole
T28 empty-scene/geometry-fact class).
