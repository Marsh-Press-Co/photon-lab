# PHASE 1 — PROPOSAL · Panel Iteration 82 · Lead seat: THERMODYNAMICS
## "The T8 r=78/156/312 Bridge, Extended to the Coherent Point/Region-Intensity Channel" (candidate exp-105)

*Grounding note, matching exp-030's own Phase-1 discipline: every geometric
constant below is computed from a stated formula against actual established
constants in `experiments/030-scale-bridge/design_geometry.py`,
`experiments/102-.../run.py`, `experiments/103-.../run.py`,
`experiments/104-.../run.py`, `lab/thermo_sidecar.py`, and
`experiments/057-.../run.py`. No number here is a fresh FDTD measurement —
this is a proposal only, no `Sim.run()` call has been made. Every table
value was produced by two short Python scripts (geometry/cost script;
thermal-sidecar script), both reproduced in full in this document's own
Appendix so Phase 3 can re-execute them verbatim rather than retype
anything by hand (R4 discipline).*

## 1. Mechanism/instrument narrative (≤300 words)

This is diagnostic/instrumentation work, in the same sense exp-030 (T8's
own founding cycle, Iteration 7) and exp-102 (Iteration 79) were: **no
mechanism is proposed; T1 is N/A.** Executes Reconciled Iteration-82 queue,
Tier 1, item 1 (Red Team's own top pick, exp-104 close, "now unblocked by
this cycle's clean [P2] null").

exp-102/103/104 built and hardened a coherent, phase-resolved point/region
field-intensity ratio (`kappa_region_wide`, `kappa_region_point`,
`kappa_window`, `delta_phi`) on the native-flagship beam-transmission bench
(single on-axis source, `graded_black_shell` r_out=78) — but every reading
to date sits at ONE object scale. T8 (exp-030) established, and Iteration
8 (exp-031) hardened, a self-similar r=78/156/312 scaling methodology for
this exact bench family — including the mandatory fix (T8's own Red Team
docket, item 2) of rescaling `graded_black_shell`'s `sigma_max(κ)=0.5/κ`
to hold the coating's radial optical depth fixed across scale, removing
the optical-depth confound that methodology exists to avoid. That bridge
has never touched the newer coherent-intensity channel.

This cycle re-derives every geometric constant of the native-flagship
bench from T8's own formula chain (self-similar scaling by κ=r/78, every
length `round(value·κ)`, `ABSORB`/`TAPER` held FIXED — T8's own established
convention, confirmed unchanged in both of exp-030's own sub-geometries),
applies it to build genuinely new r=156/312 domains, and re-runs
exp-102/103/104's own established `kappa_window`/`kappa_region_wide`/
`kappa_region_point`/sub-Nyquist-ripple machinery unmodified at each new
scale — r=78 is entirely REUSED (0 new runs) from exp-104's own committed
`results.json`, exactly mirroring T8's own r=78-reuse precedent. The
question: does this channel's own scale-dependence resemble T8's original,
genuinely mixed finding (absorber shape-law failure but monotonic
darkening; PEC's own surprising non-monotonic reversal) or behave
differently — and does it shed any new light on the still-open T13 thread
(the C_∞-asymptote-vs-witness-|C| mismatch), on a channel where that
question has never been asked.

## 2. Parameter table

### 2a. The formula chain (T8's own methodology, re-derived for this bench)

T8's own `design_geometry.py` contains TWO self-similar scaling
sub-geometries, not one: `geometry(r)` (the ambient/9-angle bench) and
`beam_geometry(r)` (the T11 companion — a single-source beam-transmission
bench, `BEAM_N_BASE=560`, `BEAM_CX0,CY0=252,280`, `BEAM_SRC_X0=64` —
**this is the exact same base geometry class exp-001/002/102/103/104 use**,
confirmed by direct match of every constant). `beam_geometry(r)`'s own
formula (`experiments/030-.../design_geometry.py:253-264`) is:

```
kappa(r)  = r / 78
N(r)      = round(560 * kappa)
CX(r)     = round(252 * kappa)
CY(r)     = round(280 * kappa)
SRC_X(r)  = round(64  * kappa)
STEPS(r)  = round(3200 * kappa)
```

reused here VERBATIM for the object/domain/timing family (T8's own
established convention — not a new choice). `ABSORB`/`TAPER` are module-
level constants in `design_geometry.py`, **unscaled at every κ in BOTH of
T8's own sub-geometries** (`ABSORB=40` line 93, never re-derived per-r) —
confirmed, and reused unscaled here (`ABSORB=EDGE=TAPER=40`, matching
exp-103's own corrected, cpl=20-calibrated value — NOT `R4_TAPER=80`,
exp-103's own Phase-2 mandatory fix, `experiments/103-.../run.py:102`).

T8's Block-1 mandatory fix for `graded_black_shell` (PHOTONICS #2, adopted
by Red Team over MATERIALS'/QUANTUM's alternatives, `experiments/030-.../
NOTES.md` §Synthesis item 2) rescales `sigma_max`, holding radial optical
depth constant:

```
R_CORE(r)   = round(30 * kappa)     # exp-030's own r_in_shell formula
R_COAT(r)   = r                     # = round(78*kappa) exactly, by construction of the r-family itself
sigma_max(r) = 0.5 / kappa          # T8's own mandatory fix (exp-030 §Synthesis item 2)
tau_shell(r) = sigma_max(r) * (R_COAT(r) - R_CORE(r))   # printed-asserted == 24.0 at every r (T8's own house discipline)
```

**Independent cross-check, not previously stated in any prior LOGBOOK
entry**: at κ=2 this formula chain gives `R_CORE=60, R_COAT=156,
sigma_max=0.25` — bit-identical to `experiments/069-.../design_geometry.py`'s
own `PEC_R_R4=60`, `R4_R_OUT=156`, `SIGMA_R4_CORRECTED=0.25` (the R4
family's own already-validated, already-thermally-cited construction).
The R4 family was built independently (Iteration 46, exp-069, for a
different, oblique-angle instrument at `cpl=40`) and never cited T8's own
formula chain — the fact that it lands on IDENTICAL numbers at κ=2 is a
real, load-bearing corroboration that T8's own `sigma_max(κ)=0.5/κ`
self-similar-optical-depth convention is not merely internally consistent
but matches this program's OWN independent, already-thermally-scored
convention at the one scale both families share.

**The `kappa_window`/`kappa_region`/`delta_phi` channel itself is
NOT rescaled** — every formula in exp-102/103/104's own `run.py`
(`block_mean_intensity`, `point_intensity`, `kappa_region_wide`,
`kappa_region_point`, `delta_phi_wide`, `delta_phi_point`, `floor_gate`,
the FFT/quintile/near-null/signed-suppression-ratio machinery) is reused
byte-for-byte, unmodified, at every r. Only the OBJECT/DOMAIN geometry and
the WINDOW's own anchor point change.

**Window anchor, corrected relative to exp-103/104's own construction, per
MATERIALS' own untested Phase-5 hypothesis (`experiments/103-.../NOTES.md`
§"New hypothesis, MATERIALS' own Phase-5 self-review")**: exp-103/104's
`BEHIND` window is anchored to `R_CLK=90`, a legacy cloak-radius constant
inherited from exp-001's own three-scene domain reuse and explicitly
flagged by MATERIALS as physically arbitrary relative to `graded_black_
shell`'s own surface (`R_COAT=78`) — `R_CLK=90` is 12 cells beyond
`R_COAT`, an unexplained offset. This cycle anchors the window (and the
`DENSE_X` standoff span) directly to `R_COAT(r)` instead — algebraically
identical to exp-103/104's own window AT r=78 (`R_CLK+15 = R_COAT+27`,
`R_CLK+115 = R_COAT+127`, verified exactly: `90+15=78+27=105`,
`90+115=78+127=205`), so this is a re-parameterization, not a redefinition,
matching this program's own T10/SIGMA_ON-erratum-avoidance discipline (a
constant must be re-derived from its own physical anchor before reuse at a
new scale, not carried forward by name alone).

**The window OFFSET-FROM-SURFACE is held FIXED across r (cells), NOT
scaled by κ** — this is the single most consequential design choice in
this proposal, and it is T8's OWN choice, not a new one: T8's own
`geometry(r)` (`design_geometry.py:111-143`) explicitly holds `PLANE_DX=15`
FIXED (not scaled) while every OTHER length scales by κ, stating explicitly
(line 89-92, and repeated in the Phase-1 narrative) that this is "the
deliberate choice that maximizes the z/z_R dynamic range the fit needs."
This cycle applies the identical principle: the window/`DENSE_X` offset
from the object's own surface stays fixed in cells across r=78/156/312,
so that (a) `z/z_R` still shrinks as `1/r²` exactly as T8's own bridge
requires for a genuine near-field-depth probe at growing scale, and (b)
this cycle's own Model-A/Model-B shape-discriminator (§4) inherits T8's
own exact geometric ratio structure (below), not a coincidentally similar
one:

```
WIN_LO_OFFSET, WIN_HI_OFFSET = 27, 127      # cells beyond R_COAT(r), FIXED (not scaled)
BEHIND_X_LO(r) = CX(r) + R_COAT(r) + 27
BEHIND_X_HI(r) = CX(r) + R_COAT(r) + 127
BEHIND_Y_LO(r) = CY(r) - 20                  # FIXED, unscaled (exp-103/104's own convention)
BEHIND_Y_HI(r) = CY(r) + 20
DENSE_X(r)     = [CX(r)+R_COAT(r)+22 .. CX(r)+R_COAT(r)+126], pitch=2 cells, FIXED (53 points, every r)
H_REGION_WIDE  = 5     # unchanged, exp-103/104's own established box (11x11 cells)
H_REGION_POINT = 0     # unchanged, exp-102/104's own established single-cell channel
FLOOR_FRAC     = 0.10  # unchanged, R13/R14 lineage house style
```

`z/z_R`-style bridging variable, T8's OWN formula (`design_geometry.py:133-135`,
`z_r=r²/λ_cells`, `z_over_zr=D·λ_cells/r²`, `x_bridge=√(z_over_zr)`),
evaluated at `D_eff=77` cells (the window's own fixed offset midpoint,
`(27+127)/2`), `λ_cells=20` (unchanged, single-λ scope):

```
z_over_zr(r) = 77 * 20 / r**2
x(r)         = sqrt(z_over_zr(r))
```

**Geometric consequence, independently reproducing PHOTONICS' own
Iteration-7 Phase-5 finding on a different bench, forced by the identical
`z/z_R∝1/r²` construction (not a new coincidence)**: `x(78):x(156):x(312)
= 4:2:1` exactly — the shape-discriminator bands in §4 below are forced by
this geometry, not by physics, exactly as PHOTONICS flagged for T8's own
Block 1.

### 2b. Computed geometry, λ=600nm, cpl=20 only (single-λ scope, unchanged
from exp-102/103/104), θ=0° only (see §T1/scope discussion below)

Computed by the script in the Appendix (`geom(r)` function), not hand-typed:

| r_out | κ | N | CX | CY | SRC_X | STEPS | R_CORE | sigma_max | τ_shell | BEHIND window (x,y) | DENSE_X span (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 78 (**REUSED**) | 1 | 560 | 252 | 280 | 64 | 3200 | 30 | 0.50000 | 24.000 | x∈[357,457) y∈[260,300) | [352,456] (53) |
| 156 (**NEW**) | 2 | 1120 | 504 | 560 | 128 | 6400 | 60 | 0.25000 | 24.000 | x∈[687,787) y∈[540,580) | [682,786] (53) |
| 312 (**NEW, cost-gated — see §2d**) | 4 | 2240 | 1008 | 1120 | 256 | 12800 | 120 | 0.12500 | 24.000 | x∈[1347,1447) y∈[1100,1140) | [1342,1446] (53) |

**Row r=78 reproduces exp-102/103/104's own established constants
bit-exact** (N=560, CX=252, CY=280, SRC_X=64, STEPS=3200, R_CORE=30,
sigma_max=0.5, window [357,457)×[260,300), DENSE_X [352,456]) — this is
this cycle's own zero-cost, R6/R15-lineage **ground-truth-recovery
precondition**: the generalized r-family formula chain, evaluated at
κ=1, must reproduce the already-validated bench exactly before any r=156/
312 reading is trusted (Gate P0, §4).

Margin check (every window/`DENSE_X` extent must clear the fixed
`ABSORB=40` band on all four domain sides — computed, not assumed):

| r_out | right margin | left margin | bottom margin | top margin |
|---|---|---|---|---|
| 78 | 63 | 24 | 220 | 220 |
| 156 | 293 | 88 | 500 | 500 |
| 312 | 753 | 216 | 1060 | 1060 |

All eight margins strictly positive at every r (the r=78 row's own margins
match the already-working bench exactly, since this row IS that bench);
margin comfortably GROWS with r (since `ABSORB` stays fixed while the
domain scales up) — Phase 4 re-verifies every one of these by direct `Sim`
geometry construction before any FDTD call, per R17's own standing
discipline, not by trusting this table alone.

### 2c. Articles

Byte-identical construction to exp-102/103/104 at every r:
`pec_disk(cx,cy,R_CORE(r))` then `graded_black_shell(cx,cy,R_CORE(r),
R_COAT(r), sigma_max=sigma_max(r))` — the SAME two-call sequence, same
material functions (`lab/materials.py:37,74`), only the four numeric
arguments changing per T8's own formula chain above. `eps_max=1.0`
unchanged (T8's own established default, never varied by either sub-
geometry). Empty scene: no material calls, unchanged.

### 2d. Run budget — realistically scoped, cost-gated per T8's own precedent

**r=78: 0 new FDTD calls.** `kappa_window`, `kappa_region_wide/point`,
`delta_phi`, the full P1-P6 sub-Nyquist machinery, and the floor gate are
all REUSED verbatim from `experiments/104-.../results.json` — exactly
mirroring T8's own Block-1 r=78 reuse (exp-030 §Synthesis: "0 new runs").

**r=156: 2 real FDTD calls (empty + article, θ=0°, STEPS=6400),
unconditionally committed.**

**r=312: cost-gated, T8's own precedent applied explicitly.** T8's own
Iteration-7 r=312 leg came in at **≈8× its own Phase-1 hand estimate**
(3.87h for 37 runs vs. the proposal's own estimate) — "the largest single
timing miss in this program's history" (`LOGBOOK.md` Iteration 7) — and
Iteration 8's own Red Team audit (finding 7) quantified the actual
per-step-doubling overrun at **≈3.5× worse than naive κ³ scaling**. This
bench's own cost driver is the identical species (grid cells ∝ N(r)² ∝
κ², steps ∝ κ, naive total cost ∝ κ³), so the identical risk applies here.
Cost model (script in Appendix, calibrated against this exact bench's own
two most recent timing figures — `experiments/103-.../run.py`'s primary
pair, 113.8s/2 calls = 56.9s/call, and `experiments/104-.../run.py`'s
primary pair, 58.7s/2 calls = 29.35s/call, a real ≈2× spread already
present in this program's own two most recent runs of the IDENTICAL r=78
geometry — disclosed as the baseline's own uncertainty, not smoothed
over):

| r | κ | naive κ³ per-call (range) | 2-call naive total | T8's own worst-case-observed multiplier (3.5×) applied |
|---|---|---|---|---|
| 156 | 2 | 235s – 455s | **7.8 – 15.2 min** | up to ≈53 min |
| 312 | 4 | 1878s – 3642s | **62.6 – 121.4 min** | **up to ≈7.1 hours** |

r=156's own worst-case (≈53 min) is affordable unconditionally. r=312's
own worst-case (up to ≈7.1 hours for just 2 calls) is not — this is
exactly the risk T8's own Iteration-7 precedent warns about, now disclosed
in advance rather than discovered mid-run. **Execution rule, adopted
verbatim from T8's own Phase-1 cost-tiering discipline** (exp-030 §7:
"time a single r=312 pilot before committing to the full leg"): run the
r=312 EMPTY-scene call alone first (1 call). If its own observed
wall-clock, doubled (a conservative proxy for the article-scene call,
which touches marginally more grid cells for material-array evaluation but
runs the same `STEPS`), projects a total 2-call r=312 leg **under 180
minutes (3 hours)**, proceed to the article-scene call and this cycle's
full r=312 analysis. If the empty-scene pilot call ALONE exceeds 90
minutes, or the doubled projection exceeds 180 minutes, STOP: report r=312
as **cost-deferred, not attempted**, this cycle's own deliverable is
r=78(reused)+r=156(new) only, and r=312 is queued, timed and de-risked, for
a future cycle. This is a disclosed, pre-committed decision rule, not a
post-hoc judgment call once real numbers are in hand (avoiding the exact
R5-family "adjust the parameter after seeing the data" failure shape).

**Total committed run budget: 2 calls (r=156, unconditional) + 1 call
(r=312 pilot, unconditional) + up to 1 more call (r=312 article, gated) =
3–4 real FDTD calls.** Substantially leaner than T8's own Block-1 budget
(89 calls) because this instrument (θ=0°-only, 2-call-per-scale) is itself
far cheaper than T8's own 9-angle ambient bench — the entire DENSE_X/
quintile/FFT/sub-Nyquist/floor-gate/THERMO analysis at each committed r is
**zero additional FDTD cost**, post-processing on the same captured field
pair, exactly as established by exp-102 Learned #3 / exp-103's own
settling-leg reuse precedent.

**No settling-independence leg this cycle** (a genuine scope reduction,
disclosed, not silently dropped) — see Idealizations §5.

## 3. T1 escape-route statement

**N/A — instrumentation/diagnostic work, not a mechanism proposal**,
exactly as T8's own founding cycle (exp-030) and exp-102 were explicit
about. No σ(I), σ(x,t), or angular-selectivity machinery is built,
proposed, or varied. `graded_black_shell`'s material law is rescaled ONLY
via `sigma_max(κ)=0.5/κ` to hold the coating's own radial optical depth
constant across a self-similar geometry family — reproducing T8's own
already-adopted fix verbatim, not a new material claim. This cycle asks
whether an already-built, already-trusted coherent-intensity instrument's
own near-field reading is scale-robust — a precondition question for any
future witness-scale citation of this channel — not a claim that
constraint 3 is closer to being satisfied. Constraint-3/4 perceptual
scoring is explicitly NOT performed this cycle (disclaimer restated in §4
and to be code-enforced per R23 at Phase 3, matching exp-104's own
precedent).

## 4. Per-metric predicted outcomes — falsifiable, numeric, pre-registered
## bands (modeled on T8's own P-VISION-1/1b/2/3 structure)

**Gate P0 (ground-truth recovery, mandatory precondition — R6/R15
lineage, run BEFORE any new FDTD call, zero cost).** The generalized
formula chain in §2a, evaluated at κ=1, reproduces every one of
exp-103/104's own established constants (N, CX, CY, SRC_X, STEPS, R_CORE,
sigma_max, window bounds, DENSE_X span) EXACTLY (integer equality, not a
tolerance band) — already verified in this proposal's own §2b table and
Appendix script output. **Falsified** if any constant disagrees even by
1 cell — would mean the formula chain itself is mis-derived and no r=156/
312 geometry should be built from it.

**P1 (reproducibility gate, R6/exp-104's own P1 lineage).** At r=78,
this cycle's own generalized code (evaluated at κ=1, using exp-104's own
`results.json`'s captured fields — no new FDTD) reproduces
`kappa_region_wide(x)` at all 16 of exp-104's original x-points to <1e-9
relative, exactly matching exp-104's own Gate P1 formula and tolerance.
**Falsified** → halt, do not trust r=156/312 readings (identical halt
discipline to exp-104's own `run.py`).

**P2 (monotonicity / T12-analog, T8's own P-VISION-2 structure).**
`kappa_window(r)` **decreases monotonically** with r (78 > 156 > 312 in
value — the object DARKENS at the fixed-offset window as r grows,
matching T8's own absorber-family finding, P-VISION-2 CONFIRMED for the
absorber in exp-030). **Falsified** by a non-monotonic reversal at either
step — the direct, on-this-channel analog of T12 (PEC's own reversal),
now tested on the article that actually matters for realizability
(`graded_black_shell`, not the constraint-2-disqualified PEC control T8
used for its own cleanest asymptotic signal).

**P3 (functional-form validation + shape discriminator, T8's own
P-VISION-1/1b structure, fit on r=156/312 held out against r=78).** Two
competing linear models, fit on the two NEW points, r=78 held out as a
free validation point (T8's own discipline):

- **Model A** (T8's own "sqrt-law", linear in `x=√(z/z_R)`):
  `κ_window(x) = κ_∞ + B·x`.
- **Model B** (T8's own "linear-law", linear in `z/z_R` itself, i.e.
  quadratic in `x`): `κ_window(x) = κ_∞' + B'·x²`.

Since `x(78):x(156):x(312) = 4:2:1` exactly (§2a, forced by `z/z_R∝1/r²`
— identical geometric necessity to T8's own finding, not re-derived data),
the shape discriminator `[κ_window(78)−κ_window(156)] /
[κ_window(156)−κ_window(312)]` **predicts 2.00±0.3 under Model A and
4.00±0.5 under Model B** — T8's OWN exact bands, reused because the
geometry forcing them is identical, not coincidentally similar.
**P3a (functional-form validation)**: whichever model the discriminator
favors, its own fitted `κ_window_pred(78)` (from the r=156/312-only fit)
must land within **25% relative** of the measured `κ_window(78)=1.8337%`
(exp-103's own established value) to count CONFIRMED; 25–60% relative →
widened-bars/inconclusive; >60% relative → REJECTED, matching T8's own
three-tier miss structure (adapted from T8's own absolute-C tolerance to a
relative-kappa one, since kappa's own established magnitude, ~2%, makes an
absolute tolerance meaningless by direct analogy to T8's own 0.03-in-C
band). **P3b (T13/T14-relevant sign test, this cycle's own genuinely new
prediction, not in T8's own structure)**: the sign of `B` (Model A's
slope). **B>0 is the physically expected, "right-direction" reading**
(κ decreases as x decreases, i.e. as r grows — consistent with the
near-field shadow continuing to deepen toward a genuine floor as the
object grows, the SAME direction T14 found the absorber's own C(r)
FAILING to show on the ambient/Weber-contrast channel). **B<0 would
directly replicate T14's own "wrong-direction asymptote" pathology on this
new, structurally different coherent-intensity channel** — a materially
informative finding for T13 either way, since it has never been asked on
this channel before. Not itself construed as resolving T13 (a different
metric, C not κ) — a cross-channel replication/non-replication data
point, stated as such.

**P4 (sub-Nyquist ripple generalization, exp-104's own P1–P6 machinery,
zero marginal FDTD cost, reused byte-for-byte at each committed r).**
exp-104's own P2 (ripple existence) FALSIFIED cleanly at r=78 — this
cycle asks whether that clean null generalizes across scale or is itself
an r=78-specific artifact. Applying exp-104's own `estimate_period`/
`near_null_exclusion`/`predicted_ratio`/quintile-FFT machinery unmodified
at r=156 (and r=312, if committed): **predicted P2 FALSIFIED again at
both new r** (0 or 1 qualifying sign changes, below the ≥2 threshold),
since nothing about the article, the channel construction, or the
`H_REGION_WIDE/POINT` box widths (held fixed in cells, unchanged) has
changed — only the object/domain scale. **Falsified** if P2 CONFIRMS
(≥2 qualifying reversals) at either new r — would mean the λ/2-scale
ripple hazard exp-104 ruled out at r=78 is scale-dependent, a genuinely
new finding worth its own follow-up.

**P5 (THERMODYNAMICS' own charter prediction — see §6 for the full
sidecar).** NETD classification (`lab/thermo_sidecar.py::
netd_disposition`) stays **UNDETECTABLE** at both r=156 and r=312, with
margin (against `NETD_BAND_K[0]=0.020`) **decreasing monotonically with
κ**, predicted band **[100×, 500×] at r=156** and **[30×, 250×] at
r=312** (illustrative center, computed via the ALREADY-GATED
`mixed_length_scale_regime` function under a `Q_ext`-invariance
assumption — see Appendix script output: 349.8× / 175.1× central,
reproducing the established r=78 anchor 699.27× exactly at κ=1). **Not
falsified** by the classification staying UNDETECTABLE even outside the
illustrative numeric band (a genuine, real `sigma_ext(r)` measurement
superseding the `Q_ext`-invariance placeholder could land the margin
anywhere above 1× and this prediction's own SUBSTANTIVE claim —
UNDETECTABLE, decreasing with κ — would still hold); **falsified** only if
the classification reaches MARGINAL or DETECTABLE at either new r, or if
the margin trend reverses (increases with κ) rather than decreases.

## 5. Idealizations

- 2D TMz, single polarization, single λ=600nm/cpl=20 scope — unchanged
  from exp-102/103/104, not broadened this cycle.
- **θ=0° only (normal incidence) — kept, not extended to an oblique-angle
  sweep. This is this seat's own explicit call, justified as follows** (the
  task's own required disclosure): (1) **cost** — r=312 already carries a
  disclosed, T8-precedented multi-hour worst-case risk at ONE angle; the
  R4 family's own oblique-angle construction (`experiments/069-.../
  design_geometry.py`) is a DIFFERENT `cpl=40` grid family entirely, not a
  drop-in extension of this bench — building a genuine self-similar
  oblique-angle r-family at this bench's own `cpl=20` convention would
  multiply the run count by the angle-set size (6, per the R4 family's own
  established angle count) at EVERY r, pushing r=312 alone toward a
  multi-day worst case, incompatible with "scope your own run budget
  realistically." (2) **apples-to-apples**: exp-104's own Gate P1
  reproducibility precondition, and this cycle's own Gate P0 ground-truth-
  recovery precondition, are both defined at θ=0°; extending to oblique
  angles in the SAME cycle would conflate two different instrument
  configurations (a `cpl=20` native-flagship family and a `cpl=40`
  R4-style family) in one bridge, reproducing the exact cross-article/
  cross-instrument confound Red Team has flagged repeatedly on this
  program (T9-vs-T11's own cross-article caveat, exp-030 §Synthesis item
  4; exp-102/103's own R4-vs-native-flagship geometry-family distinction).
  **An oblique-angle extension of this SAME θ=0°-validated bridge is
  named explicitly as a Next item (§7), not silently dropped.**
- `graded_black_shell` remains the program's already-established
  **UNOBTANIUM-WITH-PARAMETERS** idealized article at every r — the
  self-similar r=156/312 constructions are LARGER absolute idealized
  coatings, not more realizable ones (see §6 for the load-bearing
  consequence of this fact for the thermal sidecar).
- **No settling-independence leg this cycle** (a genuine, disclosed scope
  reduction). Justification, zero marginal FDTD cost: T8's OWN
  `P-VISION-S1` result (exp-030, `experiments/030-.../NOTES.md` §Results)
  found doubling `STEPS_AMBIENT` at r=156 (κ=2, the SAME κ-doubling this
  cycle's own r=156 leg needs) changed the absorber's own C by **0 to 5
  decimal places** — direct, already-measured, zero-marginal-cost evidence
  that a LINEAR-in-κ STEPS-scaling formula (T8's own `STEPS_AMBIENT(r) =
  round(1400·D_SP(r)/D_SP(78))`, structurally the same principle as this
  cycle's own `STEPS(r)=round(3200·κ)`) is settling-adequate at κ=2 for
  this SAME article class (`graded_black_shell`, sigma_max held via the
  IDENTICAL optical-depth-preserving fix). **Disclosed limitation**: this
  is corroborating evidence from a DIFFERENT bench (T8's own 9-angle
  ambient geometry, not this cycle's single-source beam-transmission
  geometry) at κ=2 only — NOT a literal re-derivation, and NOT tested at
  κ=4 (r=312) at all. If r=312 is committed (§2d), a single cheap doubled-
  STEPS spot-check at the near-field-closest `DENSE_X` point is a natural,
  low-cost follow-up, explicitly NOT committed this cycle to keep the
  budget minimal (Next item, §7).
- **Perceptual scoring: NONE this cycle**, exactly matching exp-103/104's
  own disclaimer, restated per the T28-adjacent dual-section banner
  convention (LOGBOOK Iteration 65) and R23's own single-source-of-truth
  discipline (to be implemented as a code-level assert at Phase 3,
  matching `experiments/104-.../run.py`'s own `DISCLAIMER`/
  `PREDICTIONS_TEXT`/`RESULT_TEXT` pattern): **`kappa_window`/
  `kappa_region`/the THERMO sidecar's NETD classification are raw physical
  intensity ratios and an instrument-threshold classification respectively
  — neither is a claim about human visibility or constraint-3/4 status.**
- **T8/T13's own near-field caveat is disclosed, not resolved.** This
  cycle's own r-family sits at `z/z_R∈[0.0026,0.041]` (computed:
  `z_over_zr(r)=77·20/r²`, giving 0.0253/0.0063/0.0016 at r=78/156/312 —
  narrower and shallower than T8's own original 0.0031–0.049 span, since
  this bench's own fixed window offset, 77 cells, sits closer to the
  object than T8's own PLANE_DX=15-cells-beyond-r_out convention did in
  RELATIVE terms at r=78, though the absolute offsets are comparable) —
  still 1.4–2.4 decades short of the witness z/z_R band (`[1.1e-5,9.9e-5]`,
  T8's own docket-#7-sourced figure). **No witness-scale extrapolation is
  attempted or claimed this cycle** — this is a bench-scale scale-
  robustness/generalization check only, exactly as T8's own Block 1 was
  for the ambient channel.
- `lab/` diff: zero. All new code lives in this experiment's own `run.py`
  (to be written at Phase 3), reusing exp-102/103/104's own already-
  committed functions by direct import or verbatim reproduction (matching
  their own established convention), never modifying `lab/`.
- No new trust-suite stage proposed — this cycle reuses only already-gated
  primitives (`Sim`, `materials.pec_disk`/`graded_black_shell`,
  `sc.full_capture`/`phasors`, `sc.widths()` for the THERMO sidecar's own
  `sigma_ext` input, all trust-suite stage 1/6/7/8-covered) in a new
  self-similar configuration, matching exp-102/103/104's own precedent
  (instrument-extension cycles, not new-machinery cycles).

## 6. THERMODYNAMICS' own mandatory sidecar

**Invoked this cycle — a deliberate departure from exp-102/103/104's own
"N/A" precedent, justified explicitly against the task's own question:
does a LARGER absolute coating volume change the thermal-detectability
conclusion?**

exp-102's own N/A disposition rested on an unchanged, already-thermally-
scored config (byte-identical R4-family geometry, already locked
UNDETECTABLE at exp-101's own 368× margin). exp-103/104's own N/A rested
on a dependency-chain argument: `absorbed_power_established_ratio`'s own
`p_abs_w` depends only on `sigma_ext_cells`/`i_incident_w_cm2`/
`ratio_abs_ext`, none of which read the source `edge` parameter those
cycles changed. **Neither precedent transfers here** — this cycle
genuinely changes `r_out` itself (and, by direct algebraic consequence,
the coating's own absolute volume: `π·(r_out²−r_core²)·dx_m²`, per unit
invariant length), which the thermal chain's own `l_geometric_m` argument
DOES depend on directly. R21/R23's own discipline (a sidecar's status
must be NARRATED, not silently omitted, whichever way it goes) requires
this section to say so explicitly rather than reuse a prior cycle's
disposition by inertia.

**Analytic finding, computed via the ALREADY-GATED `lab.thermo_sidecar.
mixed_length_scale_regime` function (trust-suite stage 18) — not a new
formula, a new application of an existing one** (full script: Appendix).
`mixed_length_scale_regime`'s own construction (`lab/thermo_sidecar.py:
333-393`) uses `length_provenance="bench_construction"` — `l_geometric_m
= r_out(r)·dx_m` feeds BOTH `h_eff = k_air/l_geometric_m` (Nu=2
quiescent-gas-conduction limit) AND `area_m2 = l_geometric_m²` for the
steady-state loss term. At this bench's own µm scale, gas-conduction loss
overwhelmingly dominates radiative loss at every r tested (computed:
`h_eff/[4·ε·σ_SB·T³] ≈ 1949× at r=78`, shrinking to `≈487× at r=312` —
**[Phase-5 correction, THERMODYNAMICS' own self-review + Red Team's
final audit, applied same-shift: these two figures do NOT reproduce
from this section's own stated constants -- the correct values are
≈2160.6× at r=78 and ≈540.1× at r=312 (likely a dropped ε=0.9 factor in
this one hand-evaluated sentence; recomputing with 4·σ_SB·T³ instead of
4·ε·σ_SB·T³ reproduces the cited 1949×/487× to within 0.25%). Confirmed
NOT to survive into NOTES.md's own frozen Result/Learned sections (zero
grep hits for "1949"/"487" there) -- non-load-bearing, does not change
this cycle's qualitative "gas-conduction dominates by ~3 orders of
magnitude" conclusion, which holds at either figure. Left uncorrected
above per house discipline (historical Phase-1 record, annotated not
rewritten); the correct values are what NOTES.md and results.json
actually use downstream.]** still radiative-loss-negligible at every r
in this family), so `dp/dT ≈
area_m2·h_eff = l_geometric_m·k_air` — LINEAR in `r_out`, not quadratic.
Meanwhile `p_abs_w` (via `absorbed_power_established_ratio`'s own
`iso_xsec_sq` convention, `area_m2=width_m²`, `width_m=σ_ext_cells·dx_m`)
scales as `σ_ext(r)²` — and since T9's own established `Q_ext≈1.5385`
anchor (`sigma_ext_cells/(2·r_out)`, `lab/qext_theory.py`, exp-059) is a
DIMENSIONLESS, presumptively roughly r-invariant quantity, `σ_ext(r) ≈
Q_ext·2·r_out` scales LINEARLY with `r_out` too, giving `p_abs_w(r) ∝
r_out²`. **Net: `ΔT_ss(r) = p_abs_w(r)/dp_dT(r) ∝ r_out²/r_out = r_out`
— the steady-state temperature rise is predicted to scale roughly
LINEARLY with object size**, NOT the area-invariant result T22 (exp-043,
LOGBOOK's own established finding) proved for the `w_on`-consistent single-
geometry regime — that proof's own area-cancellation holds only when BOTH
`p_abs_w` and the loss term share the SAME length convention; T23's own
adopted "mixed regime" (power via the optical `w_on`, conduction/mass via
the geometric `r_out`) does NOT cancel across a genuinely varying `r_out`,
exactly the previously-untested case this cycle is the first to actually
exercise.

**Computed (Appendix script, using the illustrative `Q_ext`-invariance
placeholder for `σ_ext(r)` at r=156/312 — to be SUPERSEDED at Phase 4 by a
real, zero-marginal-FDTD-cost `sections.widths()` measurement on this
cycle's own already-captured empty/article field pairs, exactly as
exp-087 first demonstrated is possible on this bench's own captured
fields)**:

| r_out | κ | σ_ext (illustrative, Q_ext-invariant) | p_abs_w | h_eff (W/m²K) | ΔT_ss (K) | margin vs NETD lo (0.020K) | classification |
|---|---|---|---|---|---|---|---|
| 78 (established) | 1 | 240.007 | 1.7409×10⁻¹² | 1.111×10⁴ | 2.8601×10⁻⁵ | **699.27×** | UNDETECTABLE |
| 156 | 2 | 480.015 | 6.9636×10⁻¹² | 5.556×10³ | 5.7176×10⁻⁵ | **349.80×** | UNDETECTABLE |
| 312 | 4 | 960.029 | 2.7855×10⁻¹¹ | 2.778×10³ | 1.1425×10⁻⁴ | **175.06×** | UNDETECTABLE |

**The r=78 row reproduces the LOCKED `699.27×` citation (exp-057) exactly**
(script output: `dt_ss=2.8601275372e-05` vs. the committed
`2.8601275372385233e-05` — a ground-truth-recovery check for the thermal
chain itself, R6-lineage, passed before the r=156/312 rows are trusted).
The backed-out `i_incident_w_cm2 = 6.584×10⁻⁶ W/cm²` used throughout also
independently reproduces LOGBOOK's own cited docket-#7 central witness-
irradiance figure ("6.58×10⁻⁶ W/cm² central" — LOGBOOK.md, T5 entry) —
a second, independent confirmation this chain is being applied correctly
before it is extended.

**Answering the task's own question directly: yes, the larger absolute
coating volume DOES change the margin — a real, roughly-linear-in-κ
decline — but the classification (UNDETECTABLE) does not flip within this
r-family**, and the margin at r=312 (predicted ≈175×) remains far above
1×, comfortably inside the same qualitative regime every prior thermal
citation on this bench has found. This is a genuine, previously
uncharacterized finding worth stating plainly rather than assuming
"unchanged" by analogy to T22's own different-scoped proof. **Disclosed
idealization, stated per R4/R9 discipline**: the table above is
ILLUSTRATIVE, built on a `Q_ext`-invariance ASSUMPTION for `σ_ext(156)`/
`σ_ext(312)` — not yet measured. Phase 4 must replace it with a REAL
`sections.widths()` measurement (zero marginal FDTD cost, reusing the
SAME captured fields §2d already commits to) before P5's own verdict is
scored — the illustrative numbers above are a pre-registered EXPECTATION,
not a substitute for the real Phase-4 computation, exactly matching this
program's own R4 standing rule (no hand-typed "precisely recomputed"
figure stands in for a real one).

## Appendix — scripts producing every computed number above (R4 discipline: no hand-typed figure)

```python
# --- geometry / cost script (§2b, §2c, §2d) ---
import math

DX_M = 30.0e-9
R_BASE = 78
N0, ABSORB0, EDGE0 = 560, 40, 40
CX0, CY0, SRC_X0 = 252, 280, 64
R_CORE0 = 30
STEPS0 = 3200
SIGMA_MAX0 = 0.5

def kappa(r):
    return r / R_BASE

def geom(r):
    k = kappa(r)
    N = round(N0 * k)
    CX = round(CX0 * k)
    CY = round(CY0 * k)
    SRC_X = round(SRC_X0 * k)
    STEPS = round(STEPS0 * k)
    R_CORE = round(R_CORE0 * k)
    R_COAT = r
    sigma_max = SIGMA_MAX0 / k
    tau_shell = sigma_max * (R_COAT - R_CORE)
    ABSORB = ABSORB0
    behind_x_lo = CX + R_COAT + 27
    behind_x_hi = CX + R_COAT + 127
    behind_y_lo = CY - 20
    behind_y_hi = CY + 20
    dense_x_lo = CX + R_COAT + 22
    dense_x_hi = CX + R_COAT + 126
    n_dense = (dense_x_hi - dense_x_lo) // 2 + 1
    right_margin = N - ABSORB - behind_x_hi
    left_margin = SRC_X - ABSORB
    bottom_margin = behind_y_lo - ABSORB
    top_margin = N - ABSORB - behind_y_hi
    return dict(r=r, k=k, N=N, CX=CX, CY=CY, SRC_X=SRC_X, STEPS=STEPS,
                R_CORE=R_CORE, R_COAT=R_COAT, sigma_max=sigma_max,
                tau_shell=tau_shell,
                behind=(behind_x_lo, behind_x_hi, behind_y_lo, behind_y_hi),
                dense=(dense_x_lo, dense_x_hi, n_dense),
                right_margin=right_margin, left_margin=left_margin,
                bottom_margin=bottom_margin, top_margin=top_margin)

for r in (78, 156, 312):
    print(geom(r))

# cost model, calibrated against exp-103/exp-104's own observed r=78 timing
baseline_calls = [113.8 / 2, 58.7 / 2]
base_lo, base_hi = min(baseline_calls), max(baseline_calls)
for r in (156, 312):
    k = kappa(r)
    naive_factor = k ** 3
    lo, hi = base_lo * naive_factor, base_hi * naive_factor
    worst_hi = base_hi * naive_factor * 3.5   # T8's own worst-case-observed multiplier
    print(r, k, lo, hi, "2-call min:", 2*lo/60, 2*hi/60, "worst 2-call min:", 2*worst_hi/60)


# --- thermal sidecar script (§6) ---
import sys
sys.path.insert(0, ".")
from lab import thermo_sidecar as ts

K_AIR = 0.026
DENSITY_SI, C_P_SI = 2330.0, 700.0
EMISSIVITY = 0.9
T_AMBIENT_K = 293.15
NETD_BAND_K = (0.020, 0.050)
SIGMA_EXT_78 = 240.0073740162445       # exp-057's own established value
RATIO_ABS_EXT = 0.51                    # T9's established anchor
P_ABS_78 = 1.7409069740390205e-12       # exp-057's own established, LOCKED value

Q_EXT = SIGMA_EXT_78 / (2 * 78)
width_m_78 = SIGMA_EXT_78 * DX_M
i_incident = (P_ABS_78 / RATIO_ABS_EXT) / ((width_m_78 ** 2) * 1e4)

for kappa_, r in [(1, 78), (2, 156), (4, 312)]:
    r_out_m = r * DX_M
    sigma_ext_r = Q_EXT * 2 * r              # illustrative, Q_ext-invariance placeholder
    width_m = sigma_ext_r * DX_M
    p_abs = i_incident * (width_m ** 2) * 1e4 * RATIO_ABS_EXT
    regime = ts.mixed_length_scale_regime(
        p_abs_w=p_abs, l_geometric_m=r_out_m,
        k_air=K_AIR, density_kg_m3=DENSITY_SI, c_p_j_kgk=C_P_SI,
        emissivity=EMISSIVITY, t_ambient_k=T_AMBIENT_K,
        length_provenance="bench_construction")
    dt_ss = regime["dt_ss_full_K"]
    margin = NETD_BAND_K[0] / dt_ss
    print(r, kappa_, sigma_ext_r, p_abs, regime["h_eff_w_m2k"], dt_ss, margin,
          ts.netd_disposition(dt_ss, NETD_BAND_K)["classification"])
```

*(Both scripts were actually executed in this cycle's own sandbox before
this document was written; their printed output is transcribed, not
retyped, into §2b/§2d/§6's own tables above — the r=78 row of every table
is a ground-truth-recovery check against an already-committed file, passed
in every case, per this section's own house-discipline requirement.)*

## 7. Next (candidate directions, not this cycle's own committed scope)

1. **The oblique-angle extension of this SAME θ=0°-validated bridge**
   (deferred explicitly, §5) — a genuinely new, larger-scope cycle, not a
   silent gap.
2. **A doubled-STEPS settling spot-check at r=312's own near-field-closest
   `DENSE_X` point**, if r=312 is committed this cycle — closes the one
   disclosed extrapolation gap in §5's own settling-adequacy argument
   (validated at κ=2 by T8's own P-VISION-S1, not yet at κ=4).
3. **A real, measured `sections.widths()` `sigma_ext(r)` trend**, replacing
   §6's own `Q_ext`-invariance placeholder — zero marginal FDTD cost,
   reusing this cycle's own captured fields, and itself a genuinely new
   test of whether `Q_ext` stays scale-invariant across this exact
   self-similar family (T9's own established anchor has never been tested
   away from r=78 on this article).
4. The standing `delta_scene` R3-vs-R4 split (Tier 3, now FIVE consecutive
   deferrals per exp-104's own explicit written warning) remains a
   SEPARATE, untouched thread — this experiment does not read, cite, or
   score `delta_scene`/`frac_contrast`/`ratio_k` at all, exactly matching
   exp-102/103/104's own precedent.
5. R23's own scope decision (genericize vs. formally ratify single-
   disclaimer scope) and the near-null-exclusion raw-bin-identity
   refinement — the OTHER two Reconciled Iteration-82 Tier-1 items, both
   explicitly out of THIS proposal's own scope (Tier 1 item 1 only, per
   the task's own instruction).

## LOGBOOK.md RULED OUT registry / standing rules check

No item in the RULED OUT registry (R1–R23) is re-proposed: no mechanism or
material parameter is touched beyond T8's own already-adopted
optical-depth-preserving rescale (not R1); no named-constant search is
performed (not R5); §2a's cross-check against the R4 family's own
independently-derived `sigma_max=0.25` at κ=2 is a corroboration of an
ALREADY-COMMITTED formula, not a post-hoc search over a parameter space
(not an R5 violation); the ground-truth-recovery precondition (Gate P0,
§4) is applied proactively, in the R6/R15 lineage, BEFORE any new-scale
reading is trusted, not after a surprising result is found; every
geometric constant is re-derived from its own physical anchor (R_COAT, not
R_CLK) rather than reused by name across a resolution/scale change,
directly the T10/SIGMA_ON-erratum discipline this program has paid for
before; the THERMODYNAMICS sidecar (§6) states explicitly, per R21/R23,
that its status changed (invoked, not N/A) and why, rather than reusing a
prior cycle's disposition by inertia. No closed Live Thread claim is
re-litigated: T8's own near-field caveat is disclosed, not resolved (§5);
T13 is engaged only as a cross-channel replication/non-replication
question (§4, P3b), never claimed resolved; T9's Babinet-ceiling
disclaimer is not engaged (this cycle does not compute `σ_abs/σ_ext` as a
scored ratio — the THERMO sidecar's own `ratio_abs_ext=0.51` is REUSED
from the established anchor, not re-measured); T28's own `delta_scene`/
R3-vs-R4 split remains untouched (§7 item 4).
