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

### Phase 1 result (self-scored)

Executed exactly as pre-registered above: `phase1_derivation.py`, output
captured verbatim in `phase1_output.txt`, every number below read from
`derivation_results.json` (R4 — never hand-typed). Zero FDTD calls, 57.3 s
wall time.

**LEG (a) — source aperture's own two tapered edges, vs `P_edge_A`.**
The exact (non-paraxial) Huygens–Fresnel sum over C40's real geometry is
genuinely θ-dependent (`ptp=2.02×10⁻²`, not flat), and its free-period fit
(staged widening, settled at the `narrow[1,4]°` window — an interior
optimum, no widening needed) gives:

- `P_model_a = 2.5338°`, `R² = 0.3697`
- `rel_dev(P_model_a, P_edge_A=2.8421°) = 0.1085`
- **Nominal verdict (pre-registered bands): SUPPORT** (`R²≥0.30` AND
  `rel_dev≤0.20`) — **but this verdict does NOT survive Phase 2. See the
  "Phase 3 correction" section appended below: two independent lines of
  evidence (Red Team's own circular-shift null test, and VISION's own
  pre-registered T21-decorrelation test run to its actual conclusion) both
  mandate downgrading this to INCONCLUSIVE. The R5 specificity-over-targets
  control below is real but answers a different question than the
  decisive one — do not read "FINAL VERDICT: SUPPORT" below as this
  cycle's standing verdict; it is superseded.**
- **R5 specificity control**: `5/60 = 8.3%` of a dense `[1°,15°]` candidate
  grid also clear the SUPPORT band at this fixed `(P_model_a, R²_a)` — well
  short of my own pre-registered "comparable to the ~20% width the band
  allows" downgrade trigger. Read AT THE TIME OF WRITING as "no downgrade,"
  but this specificity-over-targets question is not the same as a
  null-under-noise question — see the Phase 3 correction.
- **Structural corollary, checked directly (not merely asserted)**:
  `max|C_model(C80) − C_model(C40)| = 0.0` exactly — this ABSORB/PAD-
  independent mechanism predicts a bit-identical curve across the
  congruent series, confirming it can explain a component present
  identically in each raw config curve (matching exp-070's own
  individual-config finding), but structurally **cannot**, by itself,
  explain the real, non-zero `C80(θ)−C40(θ)` difference FDTD actually
  shows. Both readings are on the table, exactly as pre-registered — this
  result does not by itself decide between them.

**ANCHOR 1 (classical single straight-edge Fresnel diffraction) —
PASSED, with an informative twist.** The discrete exact-Green's-function
sum (independent of every `CONFIGS` number) disagrees with the classical
closed-form Hecht/Born–Wolf single-edge formula by up to
`max|diff| = 9.25×10⁻²` across `v∈[−3,3]`. Diagnosed, not left as a red
flag: substituting the SAME discrete sum's own deliberately-paraxial
version (quadratic-phase, constant-amplitude — i.e. reproducing the
classical formula's own approximation) cuts the residual to
`3.29×10⁻³` — nearly two orders of magnitude smaller, at
near-discretization precision. **This validates the underlying machinery
directly** and shows the larger exact-vs-classical gap is real,
disclosed non-paraxial physics (this file's exact `hypot`-distance,
non-constant-amplitude treatment, used everywhere else in this file),
not a bug — itself a first quantified measure of how far this bench's own
near-field geometry departs from the paraxial approximation.

**LEG (b) — article's own two rim edges, vs `P*` — verdict WITHHELD,
per this file's own pre-registered R4 gate.** Raw numbers, reported for
transparency only:

- `P_model_b = 2.1353°`, `R² = 0.1670`, `rel_dev(P_model_b, P*=2.9474°)
  = 0.2755` — nominal classification REFUTE (`R²<0.30`).
- **ANCHOR 2 (composition-of-propagators identity) FAILS, confirmed not
  a discretization artifact.** With the disk mask disabled
  (`R_OUT_test=0`), the two-stage calculation should reproduce leg (a)'s
  own direct one-stage curve (same total distance, `d1+d2=223`) by an
  exact identity of the free-space propagator. It does not:
  `max|diff| = 1.81×10⁻²` (comparable to the curve's own full
  `ptp=2.02×10⁻²`), `max relative pointwise deviation ≈ 2445%`. A
  dedicated convergence check — re-running at 1×/2×/4×/8× the native
  intermediate-surface sampling density, with an explicit quadrature
  weight — shows the mismatch is **stable** (ratio range
  `[2.8943, 2.8950]` across all four resolutions, `<0.03%` drift): this
  rules out under-resolution as the cause. The gap is a real, systematic,
  θ-dependent shortfall of the two-stage "bare Huygens secondary source"
  composition used here (most likely a missing Rayleigh–Sommerfeld-style
  boundary treatment at the intermediate re-radiating surface — a known
  subtlety of naive multi-screen Huygens propagation, distinct from
  single-screen Kirchhoff/RS diffraction, which is what leg (a) and
  Anchor 1 both correctly validate). **Per this file's own pre-registered
  R4 discipline, leg (b)'s REFUTE is NOT adopted as a trustworthy result
  this cycle — the instrument computing it failed its own anchor.** The
  R5 specificity control (`0/60` targets clear, moot since `R²_b<0.30`
  already fails the floor for any target) changes nothing here.

**Honest overall self-score (AS FILED at Phase 1 — see Phase 3 correction,
below, which supersedes the LEG (a) verdict)**: **LEG (a) — SUPPORT**,
holding up under its own specificity control, with a genuine,
correctly-diagnosed, pre-registered structural ambiguity (config-shared
component vs. the real `C80−C40` difference) left explicitly open, not
resolved by this result. **LEG (b) — NO VERDICT (instrument-validation
failure)**, not REFUTE — the two-stage propagation needs a corrected
kernel (a proper Rayleigh–Sommerfeld normalization, or a genuinely
single-integral double-diffraction treatment instead of a two-stage
composition) before its comparison to `P*` can be trusted. This is not
the clean two-target result pre-registered; it is reported exactly as it
came out, including where the secondary comparison's own machinery did
not pass its own bar.

---

### Phase 3 correction (Director, post Phase-2 Red Team audit)

**LEG (a)'s verdict is downgraded from SUPPORT to INCONCLUSIVE.** Full
reasoning, both independent lines of evidence, and the fix-docket
adoption in full: see `phase3_synthesis.md` and
`phase3_fix_docket_checks.py`/`phase3_fix_docket_results.json` (committed
code, not hand-typed, per R4). In one line: Red Team's own from-scratch
circular-shift null test (this program's established "harder companion,"
the same method that reversed exp-083's two-tone claim one cycle ago)
found `R²=0.3697` is met or exceeded by 50.0% of the curve's 30
order-preserving circular shifts — sitting at the null distribution's
median, not a rejection tail — independently reproduced bit-exact by this
Phase-3 script. VISION's own pre-registered T21-decorrelation escape test,
run to its actual conclusion, independently mandates the same downgrade
by an unrelated route (`R²_fixed=0.271` vs. the real curve's own `0.265` —
"comparable," not "near-zero"). **The genuine, surviving positive result
of this cycle is a different one**: `corr(leg_a_curve, real FDTD
C80(θ)) = +0.9582`, control-tested against leg (b)'s own output
(`r=−0.10`), a bare linear ramp (`r=−0.33`), and a bare quadratic
(`r=−0.55`) — a real, distinctive shape match between a zero-FDTD,
vacuum-only diffraction integral and the actual FDTD physics, independent
of whether its best-fit period specifically is distinguishable from
noise at this sample size (it is not).
