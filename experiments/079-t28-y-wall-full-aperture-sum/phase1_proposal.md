# PHASE 1 — PROPOSE · Panel Iteration 56 · exp-079
## The full, non-edge-reduced y-mirrored aperture sum: does exp-078's flat/zero-amplitude result generalize? (T28)

*Fresh sub-agent, MATERIALS & METAMATERIALS charter (PANEL.md seat 2:
sub-wavelength structure; what could physically realize the proposed
optical behavior; owns the realizability bound), lead by rotation.
Executes `experiments/078-.../phase5_redteam_audit.md` §7 Tier 0 item 1 —
the reconciled Iteration-56 ranking's single highest-value item on the
whole T28 board.*

**PHASE-3 UPDATE (Panel Iteration 56, post Phase-2 Red Team mandatory-fix
docket, `phase2_redteam_audit.md`): this document's original framing
over-claimed what its own data can support.** As-originally-filed, this
proposal read the recovered `theta_beam`-dependence as evidence the
mechanism is "closer to a genuine (informal) REFUTE... than to an
INCONCLUSIVE." Red Team's Phase-2 audit — independently confirming, a third
way, what EM's analytic derivation and QUANTUM's empirical ablation each
found — ruled this construction **structurally incapable of discriminating
a real y-wall echo, at ANY period, from no echo at all**: because both the
per-point bounce angle `theta_local(y_s)` and the propagation distance
`dist_image(y_s)` are, by this file's own §3.1 derivation, pure functions
of static geometry with zero `theta_beam` dependence, `E_echo`'s entire
`theta_beam`-dependence is the spatial Fourier transform of a
`theta_beam`-independent envelope, evaluated at `k·sinθ_beam` — governed by
the shared aperture window's own T21-family content regardless of the
wall's true reflectance physics. §4 and §7 are corrected below to state
this as the headline; the underlying Test-A numbers (`rel_dev`, R²,
`ss_tot` ratios, gates, convergence check) are UNCHANGED — see
`phase2_redteam_audit.md` and `phase3_synthesis.md` for the full
adjudication, and `y_wall_aperture_sum.py` §[7]/§[7b] for the newly-folded-in
reflectance-ablation control that makes this finding directly, reusably
checkable in code.*

---

## 0. What this is, and what it is not

**ZERO new FDTD calls.** Every number below is produced by
`y_wall_aperture_sum.py`, this directory (`y_wall_aperture_sum_results.json`
/ `_output.txt`) — none hand-typed (R4). It imports, never reimplements:
`boundary_reflectance.py`'s (exp-075) gated transfer-matrix `n_profile_exact`/
`nu_profile`/`damp_e_profile`/`reflection_coefficient`/`CPL`/`ABSORB_LIST`,
`design_geometry.py`'s (exp-065) `CONFIGS`, `y_wall_prescreen.py`'s (exp-078)
`free_period_with_widening`/`_free_period_search`/`CONGRUENT_KEYS` (the
identical staged-widening idiom, including exp-078's own Phase-5
`SS_TOT_DEGENERATE` hardening), and the real, already-collected
`C40`/`G40`/`C80` dense-sweep arrays (`experiments/076/results.json::
headline`).

**This is explicitly the item the reconciled Iteration-56 ranking named**
(`phase5_redteam_audit.md` §7 item 1): exp-078's single-edge (near-wall
edge only, one aperture point) reduction, evaluated at its own rigorous,
per-config-constant stationary-phase bounce angle, predicts EXACTLY ZERO
oscillatory signal (`ptp=0.000°`, `ss_tot` ratio `5.9×10⁻²⁷` below the real
data's own scale). `phase1_proposal.md`'s [exp-078's] own §3.2 stationary-
phase argument (no interior stationary point over 36°–42° for the mirrored
aperture) predicted edge-domination should hold for the FULL sum too — but
that was a prediction, never computed. This file computes it: every
aperture point `y_s ∈ [y_lo, y_hi]` gets its OWN per-point rigorous bounce
angle `theta_local(y_s) = atan(D_SP/(OBJ_Y+y_s))` (unlike the single-edge
case's one shared constant), its own driven source phase, its own
`r(theta_local(y_s))` weight, and its own image-path propagation phase,
summed coherently (a closed-form numeric integral, `numpy`, zero FDTD).

**Scope discipline (per the reconciled ranking's own sequencing):** item 8
(`|r(θ)|`-weighting the self-echo PROXY curve as a *separate* refinement on
top of an otherwise-flat unweighted sum; the far-wall/far-edge pair) is
explicitly deferred — both are refinements of the flat, unweighted
`90−θ_beam`-convention edge model that this item's own result may render
moot. **This file's construction already subsumes item 8's amplitude-
weighting concern, but not in the sense item 8's own text means**: item 8
asks whether weighting a coarse *two-point* self-echo PROXY curve by
`|r(θ)|` changes which comparisons clear SUPPORT — a refinement bolted onto
the single-edge model. This file instead builds the amplitude weighting
(the real raised-cosine taper, §2) and the per-point `|r(theta_local(y_s))|`
weighting (§3.1) directly INTO the primary construction, because for a
genuine coherent APERTURE sum (not a two-point reduction), which points
dominate is inseparable from their amplitude — it is not an optional
refinement of this specific model, unlike item 8's own narrower framing.
No far-wall/far-edge pair is added (Idealization 3, §6) — that remains
explicitly out of scope, matching the ranking's own deferral.

---

## 1. Narrative (≤300 words)

exp-078's Phase-5 final audit proved a striking negative: the single
near-edge point (`y_lo`), reflected through its own image and evaluated at
its own rigorous, `theta_beam`-independent bounce angle, predicts a flat
curve — because one point's own reflection geometry cannot depend on how
the whole aperture is steered. But a REAL aperture is not one point; it is
~1,504 coherently-driven source cells, each carrying its OWN `theta_beam`-
dependent driven phase `phase(y_s)=k·sinθ_beam·(y_s−OBJ_Y)` (`Sim.
add_line_source`'s own convention) and its OWN `theta_beam`-independent
bounce angle `theta_local(y_s)=atan(D_SP/(OBJ_Y+y_s))` — the same formula
Red Team's Phase-5 audit derived for `y_lo`, re-derived here for every
point. This file builds that full coherent sum and finds: the flat result
does **not** survive. A real, well-converged, non-degenerate oscillation
reappears (`ss_tot` ratio to real-data scale `9.4×10⁻⁷` — **≈20.2 orders of
magnitude** above exp-078's own `5.9×10⁻²⁷` ratio; a DIFFERENT comparison —
this cycle's own absolute `ss_tot` against the `SS_TOT_DEGENERATE_FLOOR`
guard — is the one that is `≈9.78` orders, corrected per
`phase2_redteam_audit.md` §3, Attack 2). Genuine `theta_beam`-dependence
exists in the full sum that the single-point reduction could never see,
exactly as Red Team's own exp-078 §2d flagged as "a real possibility."

**But this `theta_beam`-dependence cannot discriminate a real y-wall echo
from no echo at all (Phase-2 finding, given full weight — see the PHASE-3
UPDATE above and §7).** The newly-recovered oscillation is not a match to
T28's own family. It sits within 1.6%–3.5% of T21's own already-established,
already-distinct aperture-diffraction fringe (`1.9608°`, `A=752`) — not near
T28's own 2.84°–4.6° periods (28.6%–56.8% away) — and EVERY individual
config's own curve, not merely the pair-deltas, already carries this same
~2.0° period at `R²=0.97–0.98`. The mechanism is legible, and now
DIRECTLY, reusably checkable in code (§3.1's reflectance-ablation control):
both `theta_local(y_s)` and `dist_image(y_s)` are `theta_beam`-independent
by construction, so `E_echo`'s entire `theta_beam`-dependence is carried by
the SAME driven-phase ramp that produces T21's real fringe in the direct
field — the y-wall's own reflectance physics (`r(theta_local(y_s))`)
contributes only a slowly-varying (for `PAIR_PAD`/`C80−C40`) or, for
`PAIR_ABSORB40` specifically, load-bearing-but-still-T21-frequency-locked
envelope, never an independent new frequency. Edge-domination in the strict
"flat" sense does not generalize — but the full sum, by its own structure,
was never capable of answering whether a real y-wall echo at T28's own
period exists.

---

## 2. Parameter table / geometry

All values from `y_wall_aperture_sum_results.json::geometry` /
`::theta_local_envelope` (Sec `[0]`/`[0b]` of `_output.txt`).

| cfg | `ABSORB` | `PAD` | `OBJ_Y` | `y_lo` | `y_hi` | `A` | `D_SP` | `aperture_cells` | `theta_local(y_lo)` | `theta_local(y_hi)` |
|---|---|---|---|---|---|---|---|---|---|---|
| C40 | 40 | 0 | 792 | 40 | 1544 | 752 | 223 | 1504 | 15.0043° | 5.4531° |
| C60 | 60 | 20 | 812 | 60 | 1564 | 752 | 223 | 1504 | 14.3450° | 5.3618° |
| C70 | 70 | 30 | 822 | 70 | 1574 | 752 | 223 | 1504 | 14.0362° | 5.3173° |
| C80 | 80 | 40 | 832 | 80 | 1584 | 752 | 223 | 1504 | 13.7402° | 5.2735° |
| G40 | 40 | 40 | 832 | 80 | 1584 | 752 | 223 | 1504 | 13.7402° | 5.2735° |

`0.5*(y_lo+y_hi) == OBJ_Y` exactly for every config (asserted in code,
§0 of `_output.txt`) — the premise `source_driven_phase`'s simplification
`phase(y_s)=k·sinθ·(y_s−OBJ_Y)` rests on. `theta_local(y_s)` ranges from
`13.7°–15.0°` at the near edge (`y_lo`, matching exp-078's Phase-5 table
exactly) down to `5.3°–5.5°` at the far edge (`y_hi`) — a range spanning
`[4.77°,15.50°]` globally, never sampled by ANY prior gate in this program
(as-filed `±44°`; exp-078's corrected `48°–54°`; exp-078 Phase-5's rigorous
single-edge `13.7°–15.1°`) — gated fresh here (§3).

**T1 escape route: N/A.** Instrument/model-fidelity thread, matching every
T28 cycle since exp-069 — no absorber, no switch, no constraint-3 scene
anywhere in this file.

---

## 3. Derivation

### 3.1 — Per-point rigorous bounce angle, image geometry, reflectance weighting

Re-derived from the SAME image-source construction Red Team's Phase-5 audit
used for the single edge (`phase5_redteam_audit.md` §2a), generalized from
`y_s=y_lo` to a general aperture point. Every point on the source line
shares the same `x=SRC_X` (`Sim.add_line_source` places the whole aperture
on one vertical line) — mirroring through the near `y=0` wall flips only
`y`, giving an image at `(SRC_X,−y_s)`. The straight line from that image to
the observer `(PLANE_X,OBJ_Y)` has `Δx=D_SP` (constant across the whole
aperture) and `Δy=OBJ_Y+y_s`, so:

```
theta_local(y_s) = atan(D_SP / (OBJ_Y + y_s))     -- theta_beam-independent
dist_image(y_s)  = hypot(D_SP, OBJ_Y + y_s)        -- image-to-observer distance
```

Both are pure functions of static geometry — no `theta_beam` term anywhere,
confirmed by direct code inspection (Sec `[0b]` prints this per config).
`r(theta_local(y_s); ABSORB)` reuses `boundary_reflectance.py`'s already-
gated (`G-LOSSLESS`/`G-N1`/`G-PASSIVITY`), Red-Team-adjudicated-on-
convention (R8, Iteration 52) transfer-matrix reflectance **unchanged**
(exp-078 §3.4's premise: `Sim._damping` applies one shared cubic ramp to
all four domain edges — re-verified there, not re-verified again here,
per house discipline against redundant re-derivation of an already-settled
premise). Because `r()`'s scalar Python implementation is called once per
aperture point (up to ~6,000 for the 4x convergence check × 5 configs), a
**vectorized-over-theta** re-implementation of the identical recursive
transfer-matrix algebra is used for performance (§2 of the script) —
**validated bit-exact against the scalar, already-gated function** at a
battery of sample angles across all four `ABSORB` depths before use
(`max |r_vec−r_scalar| = 7.988×10⁻¹⁶`, Sec `[2b]` of `_output.txt`) — a new
performance path, not a new physics claim, gated before trust exactly as
this program's own R4/verify-before-claim discipline requires.

### 3.2 — Amplitude taper (load-bearing, per §0's own scope note)

Re-derived from `lab/fdtd2d.py::Sim.add_line_source`'s own code (verified
against that function's source, not guessed — quoted verbatim in the
script's own docstring): a unit-height top-hat over `[y_lo,y_hi)` with a
raised-cosine (half-Hann) taper over the first/last `edge=TAPER=40` cells,
`p[i]=0.5·(1−cos(π·i/edge))` for `i<edge` (and its mirror at the far end),
`p[i]=1` elsewhere, `i=y_s−y_lo`. This is `amp(y_s)` below.

### 3.3 — Driven source phase

Re-derived from `add_line_source`'s own code: `phase = k·sin(angle_deg)·
(yy − 0.5·(y_lo+y_hi))`. Since `0.5·(y_lo+y_hi)=OBJ_Y` exactly for every
congruent-series config (§2, asserted in code), this is
`phase(y_s;theta_beam) = k·sin(theta_beam)·(y_s−OBJ_Y)` — matching the
task's own stated convention, re-derived, not assumed.

### 3.4 — The coherent sum

Per-point complex contribution to the total REFLECTED (echo) field:

```
dE(y_s;theta_beam) = amp(y_s) * r(theta_local(y_s);ABSORB)
                      * exp(i*[phase(y_s;theta_beam) + k*dist_image(y_s)])

E_echo(cfg,theta_beam) = INTEGRAL over y_s in [y_lo,y_hi] of dE(y_s;theta_beam) dy_s
```

evaluated as a trapezoidal-rule numerical integral (`numpy`), not a bare
discrete sum — a defensible choice matched to the fact that `r(theta_local
(y_s))` is computed once per `(config, discretization)` (theta-beam-
independent, per §3.1) and cached, so the theta_beam sweep itself is a fast
vectorized re-weighting of that fixed profile (§4 of the script; run time
for the full pipeline, all convergence levels: **2.3s**, `_output.txt`
tail).

**Why no `dist_real` / phase-difference term (unlike exp-078's single-edge
`Delta_phi_self`):** exp-078's model computed a PHASE DIFFERENCE (reflected
minus direct) at one point, because a single point's own driven-phase term
cancels identically between its direct and reflected copies. Here the task
asks for "a total reflected-field complex phasor" — `E_echo` itself, not a
difference against a direct-field object — so no reference subtraction is
built. This is a stated, disclosed construction choice (§6, Idealization
4), not an oversight: it means `E_echo` genuinely does carry `theta_beam`
dependence through `phase(y_s;theta_beam)` for a single point too (trivial,
expected — a lone driven point's own reflected copy naturally inherits its
own steering phase) — the informative question this file actually answers
is whether the coherent SUM across many such points, weighted by amplitude
and by each point's own bounce-angle-dependent reflectance, produces
structure that (a) survives at all (§5.2) and (b) matches T28's own real
periods specifically, as opposed to some other, already-known frequency
(§5.3/§5.4).

---

## 4. Falsifiable predicted outcomes — pre-registered numeric bands

**Test A (period) band reused verbatim from exp-075/077/078**
(`rel_dev ≤ 0.30` SUPPORT / `>1.00` REFUTE / else INCONCLUSIVE), scored via
the identical imported `_free_period_search` machinery.

**Primary scalar proxy: `Re{E_echo(cfg,theta_beam)}`** — this bench's own
house phasor convention (`lab/emit.py`'s `f(n)=Re{F·e^{−iωn}}`), the
physically-meaningful, sign-carrying field value a real time-domain
observer monitor would record. **Secondary robustness cross-check:
`|E_echo|`** (sign-blind magnitude), reported symmetrically, not
cherry-picked (§5.1/§7).

**A priori prediction, stated before the primary run's own tables were
written up** (this is a single Phase-1 deliverable, not a multi-phase
git-frozen cycle — the prediction below reflects `phase1_proposal.md`
[exp-078]'s own §3.2 stationary-phase argument and Red Team's own §2d
framing, both already on record before this script's first execution):
per Red Team's own explicit framing (`phase5_redteam_audit.md` §7 item 1),
either (a) edge-domination generalizes and the flat result survives
(`ss_tot` ratio stays near float-noise scale), predicting the y-wall
self-near-wall coherent-echo sub-class is close to formally exhausted; or
(b) it does not, which "would justify the full build for the first time."
**Actual result (§5, corrected per `phase2_redteam_audit.md` Attack 5): this
IS branch (b) — the flat result does NOT survive (ruling out (a)) — refined,
not a third branch.** Genuine `theta_beam`-dependence is recovered, exactly
as branch (b)'s own premise states. What this file adds is why that
dependence does NOT license branch (b)'s own stated *consequence* ("would
justify the full build for the first time"): the recovered dependence is
mechanistically inherited from the shared aperture window (T21's own
frequency), and — per Red Team's own §2/Attack 1, given full weight —
this specific construction is structurally incapable of producing a
genuinely different, T28-matching frequency regardless of the wall's true
reflectance physics (§5.2/§5.3, §7).

**Convergence check, pre-registered as mandatory before trusting any
period fit** (task's own instruction): does the answer change if the
number of aperture points is doubled/quadrupled? Scored via relative
change in `ptp(PAIR_PAD)` between 2x and 4x oversampling, with an informal
convergence bar of `<1%` relative change.

**`SS_TOT_DEGENERATE` watch** (exp-078 Phase-5's own hardening,
`phase5_redteam_audit.md` §2c/§6 item 5): before trusting any high-`R²`
period fit, the model's own `ss_tot` is compared to the real data's `ss_tot`
on the identical statistic — a ratio near exp-078's own `5.9×10⁻²⁷` floor
would mean this file's model is ALSO degenerate/flat; a ratio many orders
of magnitude above it (but still small in absolute field units) means real,
resolvable signal.

**R5 disclosure (mandatory-control gap, stated explicitly per the task's
own allowance):** this file builds ONE primary model (no search over
candidate length scales or geometric constants) with two proxy CHOICES
(`Re`, `|·|`) reported symmetrically — not a dense search of the kind R5's
null-permutation-control rule targets. No null-permutation control is run
here. §5.4's comparison against T21's own fringe period is a SINGLE,
targeted, pre-named comparison (EM's own caution, already on record in
exp-078's `phase1_proposal.md` §3.3, not a candidate invented post hoc to
explain an inconvenient number) — disclosed as a real, if narrower, gap:
Phase 2 may still reasonably require a formal look-elsewhere control before
treating even this single T21-proximity finding as fully established,
particularly given the one nominal Test-A SUPPORT below (§5.3).

---

## 5. Results (all numbers from `y_wall_aperture_sum_results.json` / `_output.txt`, never hand-typed)

### 5.1 — Validation and gates (must pass before anything else is trusted)

- **Vectorized `r(theta)` vs the scalar, already-gated function:**
  `max |r_vec−r_scalar| = 7.988×10⁻¹⁶` over 4 `ABSORB` depths × 5 sample
  angles — float-precision agreement.
- **Gates at the full, never-before-sampled `[4.77°,15.50°]` envelope:**
  `G-LOSSLESS` worst `||r|−1| = 2.220×10⁻¹⁶` PASS; `G-N1` worst
  `|r_loop−r_direct| = 5.403×10⁻¹⁵` PASS; `G-PASSIVITY` worst
  `|r| = 0.000115` PASS. `reflection_coefficient` is trustworthy across the
  entire aperture's own angle range, not merely at the single near-edge
  point exp-078's Phase-5 audit checked.
- **Numerical-integration convergence:** `ptp(PAIR_PAD)` at 1x/2x/4x
  oversampling (1,505 / 3,009 / 6,017 points): `4.463023×10⁻⁶` /
  `4.464108×10⁻⁶` / `4.464175×10⁻⁶`. Relative change 1x→2x:
  `2.431×10⁻⁴`; 2x→4x: `1.496×10⁻⁵` — well under the pre-registered `<1%`
  bar, shrinking as expected for a converging Riemann-sum-style integral.
  **CONVERGED.** The reported primary-model numbers below use the 1x
  (native, `dy=1` cell — the real per-cell source resolution) grid; the
  convergence check confirms this is not an under-resolved artifact.

### 5.2 — Does the flat/zero-amplitude result generalize? NO.

`ss_tot(model, Re-proxy PAIR_PAD) = 6.047×10⁻¹¹`, vs
`ss_tot(real PAIR_PAD) = 6.439×10⁻⁵` — ratio `9.392×10⁻⁷`. This is
**≈20.2 orders of magnitude above** exp-078's own single-edge, rigorous-angle
model's `5.9×10⁻²⁷` ratio (`phase5_redteam_audit.md` §2c) — corrected per
`phase2_redteam_audit.md` §3 (Attack 2, THERMODYNAMICS): the as-filed
version of this document mis-stated this comparison as "nine orders,"
which is instead the value of a DIFFERENT, separately-named comparison —
this cycle's own absolute `ss_tot_model` (`6.047×10⁻¹¹`) against the
`SS_TOT_DEGENERATE_FLOOR` guard (`1×10⁻²⁰`) — `≈9.78` orders, correct on
its own terms but not the comparison this paragraph names. Both
comparisons independently confirm the same qualitative conclusion (well
above the `SS_TOT_DEGENERATE` floor, `ss_tot_degenerate=False` in code).
This is real, resolvable, non-degenerate signal, not floating-point
rounding noise on a flat array. **The flat result from the single-edge
reduction does NOT generalize to the full aperture sum.** Every individual
config's own `Re{E_echo(cfg,theta_beam)}` curve shows real `ptp` variation
(`C40`: `1.487×10⁻⁵`; `C60`: `3.509×10⁻⁷`; `C70`: `3.365×10⁻⁷`; `C80`:
`1.789×10⁻⁷`; `G40`: `1.693×10⁻⁵` — `C40`/`G40`, both `ABSORB=40`, an
order of magnitude larger than `C60`/`C70`/`C80`, matching the same `|r|`
ordering exp-078 already established). **But — per §5.3/§7 — "does not
generalize" is a different, narrower claim than "is informative about a
real y-wall echo"; this section's own non-degenerate `ss_tot` says only
that the model has real structure, not that the structure says anything
about the wall's reflectance.** A missing `1/√dist_image(y_s)`
cylindrical-wave amplitude-falloff term (Idealization 10, §6; this bench's
own established `field_and_h` convention, `experiments/048-.../design_
geometry.py`, subject of a dedicated correction, Iteration 19/exp-042) is
undisclosed in this file's as-originally-computed model — EM's own
Phase-2 re-run with the falloff added (`phase2_critique_em.md`) shows the
Test-A period verdicts below shift `<1%` (robust to this specific
omission) but the `ss_tot` ratio itself moves `≈753×`
(`9.392×10⁻⁷→1.248×10⁻⁹`) — still nowhere near the `SS_TOT_DEGENERATE`
floor either way, but the specific magnitude figures in this section
should be read as convention-dependent, not exact.

### 5.3 — But the recovered period is T21's own fringe, not T28's family

| comparison | P*_real (T28) | P*_model (primary, Re) | rel_dev vs T28 | verdict | rel_dev vs T21 fringe (1.9608°) |
|---|---|---|---|---|---|
| `C80−C40` | `2.8421°` | `2.0301°` | `0.2857` | **SUPPORT** | `0.0353` |
| `PAIR_PAD` (T28's actual dominant target) | `4.6113°` | `1.9925°` | `0.5679` | INCONCLUSIVE | `0.0162` |
| `PAIR_ABSORB40` | `4.1761°` | `2.0226°` | `0.5157` | INCONCLUSIVE | `0.0315` |

**Every model period sits 1.6%–3.5% from T21's own established
`A=752`/600nm/39° fringe (`1.9608°`, re-derived here from the already-
committed `dg048.ripple_period_deg`, not hand-typed) — an order of
magnitude closer than to any T28-family target (28.6%–56.8% away).** This
is not a coincidence discovered by searching: EM's own caution
(`phase1_proposal.md` [exp-078] §3.3) already named `A=752` as the risk to
watch for. The mechanism is directly legible in the per-config solo curves
(§5.5): every individual config's own `Re{E_echo}` curve — not just the
pair-deltas — already carries a `~2.02°` period at `R²=0.97–0.98`, meaning
the coherent sum's dominant oscillation frequency is set by the SAME
`A=752`-scale driven-phase ramp that produces T21's fringe in the real,
direct (non-reflected) field, weighted by a slowly-varying reflectance/
image-distance envelope that differs between configs in AMPLITUDE and
OVERALL PHASE, not in fundamental frequency. Differencing two
near-identical-frequency sinusoids (any pair of configs) necessarily
produces a third sinusoid near that SAME frequency — the identical
algebraic fact LOGBOOK's own T28 opening paragraph used to rule out "T21
fringe, differently weighted" as an explanation of the REAL data's
`C80−C40` signal (bit-identical `A=752` there too). The same logic applies
here: this echo model's own recovered oscillation is mechanistically tied
to T21's frequency, not to T28's independently-established, genuinely
different one.

**Companion note (PHOTONICS, `phase2_critique_photonics.md`; adjudicated
`phase2_redteam_audit.md` §4): the "only a slowly-varying envelope" claim
above is not fully earned by what was originally computed here.**
Subtracting `PAIR_PAD`'s own dominant `1.9925°` tone and free-period-
searching the residual finds a genuine secondary component at `2.5506°`
(R²=`0.6043`, `≈2.8%` of the primary fit's own `ss_tot`) — real, disclosed
structure, not noise, and closer to T28's own `C80−C40` real period
(10.3% away) than to T21's (30.1% away). Red Team's own ruling: this does
**not** change the verdict — a residual sideband inside a construction
whose entire `theta_beam`-dependence is structurally locked to the shared
aperture window (§7) is itself just another feature of that same window's
Fourier content (a diffraction-grating side-lobe, not a new physical
channel) — it cannot be independent evidence about the wall's own
reflectance any more than the dominant tone can.

**Reflectance-ablation control (Phase-2 mandatory fix, `y_wall_aperture_
sum.py` §[7]/§[7b], `::reflectance_ablation_control`/`::t21_forced_fit_
c80_c40` in the committed JSON) — the decisive, mechanism-appropriate test
of whether ANY of the above depends on the wall's reflectance at all.**
Replacing `r(theta_local(y_s))` with a bare constant `1.0` (zero wall-echo
physics) and re-fitting: `PAIR_PAD`/`C80−C40`'s ablated periods reproduce
the r-weighted model to `|ΔP*|≤0.023°` — geometry alone, independent of
`ABSORB`, already produces this file's own recovered signal for those two
comparisons. `PAIR_ABSORB40`'s ablated delta is EXACTLY zero (`ptp=0.0`,
not merely small) — `G40`/`C80` share identical `(OBJ_Y,y_lo,y_hi)`
(both `PAD=40`), so once `r()` is ablated to a config-independent constant
their aperture sums are bit-identical by construction. This means
`PAIR_ABSORB40`'s real (non-ablated) signal genuinely DOES require
`ABSORB`-dependence to exist at all — unlike `PAIR_PAD`/`C80−C40` — but
even this genuinely wall-physics-dependent signal still lands on T21's own
period (`rel_dev=0.0315` vs. T21, §5.3 table), not T28's, because
`ABSORB`-dependence only reshapes the envelope `w(y_s)`'s fine structure,
never the aperture window's own dominant support — the ONLY `theta_beam`-
dependent term in the integral remains the shared driven-phase ramp.
**Two independent routes (geometry alone; genuine but T21-frequency-locked
`ABSORB`-dependence) both land on the aperture's own period, never T28's —
this construction cannot discriminate a real T28-matching y-wall echo from
no echo at all, by either route.** The `C80−C40` T21-forced-fit sub-check
(force the fit to T21's own EXACT `1.9608°`, not the free-fit optimum):
`R²=0.9425` (vs. the free-fit's `0.9732`), `rel_dev=0.3101` against T28's
real target — **just outside the SUPPORT bar**, vs. the free-fit's own
marginal `rel_dev=0.2857` SUPPORT. The SUPPORT/INCONCLUSIVE line for this
one comparison rides on a `~2%` sub-fitting-window difference between
curves that are, structurally, all measuring the same T21-scale quantity —
**the one nominal Test-A SUPPORT below should be read as non-informative,
not as evidence, now that this control is in the record.**

**THERMODYNAMICS energy-sidecar disposition (house norm, PANEL.md seat 4):
N/A.** No absorbed-power computation appears anywhere in this file — `r()`
is reused unchanged from an already-gated model, and this cycle scores only
period comparisons on a reflectance phasor, never an energy/detectability
question (`phase2_critique_thermodynamics.md`, confirmed by direct grep of
the script).

### 5.4 — Secondary proxy (`|E_echo|`): 0/3 SUPPORT, confirms the same picture

| comparison | P*_real | P*_model (`\|·\|`) | rel_dev | verdict |
|---|---|---|---|---|
| `C80−C40` | `2.8421°` | `1.0075°` | `0.6455` | INCONCLUSIVE |
| `PAIR_PAD` | `4.6113°` | `1.0075°` | `0.7815` | INCONCLUSIVE |
| `PAIR_ABSORB40` | `4.1761°` | `1.0075°` | `0.7587` | INCONCLUSIVE |

The magnitude-based proxy loses even the one marginal SUPPORT — all three
periods collapse to `1.0075°` exactly (a harmonic/rectification artifact of
taking `|·|` of a near-sinusoidal complex phasor, plausible given `|E_echo|`
is not itself close to sinusoidal even when `Re{E_echo}` is), reinforcing
that the primary proxy's one nominal SUPPORT is not a robust, convention-
independent finding.

### 5.5 — Per-config solo periods (diagnostic, confirms the mechanism, not scored against a band)

| cfg | solo `P*` | solo `R²` |
|---|---|---|
| C40 | `2.0226°` | `0.9733` |
| C60 | `2.0226°` | `0.9779` |
| C70 | `2.0150°` | `0.9803` |
| C80 | `2.0150°` | `0.9791` |
| G40 | `2.0226°` | `0.9684` |

All five configs cluster at `2.015°–2.023°`, `R²≥0.97` — confirming §5.3's
mechanistic reading directly: the T21-family period is intrinsic to each
config's own echo curve, not an artifact of differencing.

---

## 6. Idealizations (stated explicitly, house norm)

1. **`r(theta_local(y_s))` reuses `boundary_reflectance.py`'s matched-
   `eps=mu` (TE, unrealizable-admittance) transfer-matrix formula
   unchanged** — the same caveat MATERIALS attached to both the x-wall
   (exp-077 Idealization 10) and the y-wall single-edge model (exp-078
   Idealization 6). A SUPPORT or REFUTE under this construction says
   nothing about realizability either way; MATERIALS' own re-ranking
   (exp-078 Phase-5, F2) found the realizable (`mu_r=1`) substitution is
   near period-invariant for the y-wall specifically (Pearson `r>0.9997`),
   so this idealization is unlikely to move §5.3's own headline finding,
   but was not independently re-tested here (out of scope this cycle,
   matching the standing realizable-admittance refit's own retargeting to
   the x-wall, exp-078 §7 item 3).
2. **No `dist_real` reference term** — `E_echo` is the total reflected
   field, not a phase difference against a direct-field object (§3.4).
   This is a deliberate construction choice matched to the task's own
   framing ("a total reflected-field complex phasor"), not a simplification
   of exp-078's own two-term difference.
3. **Single (near) wall, one aperture, no far-wall/far-edge pair** —
   matching the reconciled ranking's own explicit deferral (§0). A real
   model would sum both the near-wall image AND the far-wall image
   coherently; this file computes only the near-wall contribution.
4. **Trapezoidal-rule numerical integral, not the literal discrete FDTD sum
   over exactly `aperture_cells` grid cells** — the primary (1x) grid uses
   `dy=1` cell (matching the real source's own per-cell resolution
   exactly, `aperture_cells+1` points), so this is numerically very close
   to the literal discrete sum; the convergence check (§5.1) confirms the
   integral approximation is stable, not merely close by construction.
5. **TE/matched-admittance, 600nm only** — the 750nm reference period
   (carried in exp-078, not re-derived there either) is not modeled at
   750nm here; disclosed, not silently dropped.
6. **No null-permutation control on the single T21-proximity comparison**
   (§4's R5 disclosure) — a real, stated gap for Phase 2.
7. **Image-phase convention** — inherits R8's already-resolved committed
   convention (`arg(r)`, not `conj(r)`) unchanged, per every T28 cycle
   since Iteration 52; not independently re-tested here.
8. **Amplitude taper and driven phase are re-derived from `add_line_source`'s
   own code, not independently cross-checked against a live FDTD source
   array** — a static code-reading verification (quoted in the script's
   own docstrings), not a runtime comparison against `sim.sources` (would
   require instantiating a `Sim`, which is zero-cost/zero-`.run()` and
   arguably in scope, but not done this cycle; disclosed as a cheap,
   deferrable Phase-2 hardening item). **Closed at Phase 2** (PHOTONICS'
   own critique, `phase2_critique_photonics.md`): a live `Sim` was
   instantiated and its actual source array compared — exact (`0.0` diff)
   agreement with `aperture_amplitude`'s own re-derivation.
9. **[Added, Phase 3, `phase2_redteam_audit.md` Attack 1/§2 — the cycle's
   own most consequential finding] This construction is structurally
   incapable of discriminating a real y-wall echo, at ANY period, from no
   echo at all.** Both `theta_local(y_s)` and `dist_image(y_s)` are, by
   this file's own §3.1 derivation, pure functions of static per-config
   geometry — zero `theta_beam` dependence anywhere. `E_echo`'s entire
   `theta_beam`-dependence is therefore the spatial Fourier transform of a
   `theta_beam`-independent envelope `w(y_s)=amp(y_s)·r(theta_local(y_s))·
   exp(i·k·dist_image(y_s))`, evaluated at spatial frequency `k·sinθ_beam` —
   governed by `w(y_s)`'s own dominant support (the shared `[y_lo,y_hi]`/
   `TAPER=40` window, IDENTICAL to the real, direct-field aperture's own),
   regardless of what the wall's true reflectance physics is. A real echo
   at T28's own period, had one existed, could not have been recovered by
   this instrument; no echo at all produces a statistically
   indistinguishable result (confirmed directly, §5.3's reflectance-
   ablation control). This is not a data problem a finer grid or a wider
   angle sweep would fix — it is a structural property of building `E_echo`
   as a coherent sum over the real, `theta_beam`-driven aperture with a
   per-point weight that carries no `theta_beam` dependence of its own. See
   §7 for what this means for this file's own verdict.
10. **[Added, Phase 3, `phase2_redteam_audit.md` Attack 4, EM] Missing
    `1/√dist_image(y_s)` cylindrical-wave amplitude-falloff term.**
    `echo_field_curve`'s per-point contribution has no such factor, unlike
    this bench's own established many-point Huygens–Fresnel convention
    (`experiments/048-.../design_geometry.py::field_and_h`,
    `G0=exp(i(kr−π/4))/√r`, the subject of a dedicated magnitude-bridge
    correction, Iteration 19/exp-042). EM's own re-run with the falloff
    added (`phase2_critique_em.md`) shows the Test-A period verdicts are
    essentially unaffected (`<1%` shift on every P*, independently
    confirming §5.3's own mechanistic reading) but the `ss_tot` ratio moves
    `≈753×` (§5.2) — a real, previously-undisclosed idealization on the one
    statistic this file leans on hardest as evidence of non-degenerate
    signal, though not load-bearing to any scored verdict.
11. **[Added, Phase 3, `phase2_redteam_audit.md` §2c — forward caution, not
    a finding about this file] The effective aperture a fix would need is
    a name already on LOGBOOK's own RULED OUT list.** Using T21's own
    `P(θ)=λ/(A·cosθ)`, the effective aperture width `A_eff` a T21-class
    edge-diffraction model would need to exactly reproduce T28's own real
    `C80−C40` period is `A_eff = 752·1.9608/2.8421 = 518.8118` cells —
    bit-identical (to the fourth significant figure) to `A_eff≈518.81`,
    the exact quantity LOGBOOK's own R5 addendum (Iteration 47, exp-070)
    already found and ruled a statistically-indistinguishable-from-chance
    dead end (`null_p=0.497`). Any future attempt to "fix" this model class
    by shrinking its effective aperture toward T28's own period would be
    re-approaching that already-closed dead end, not new evidence.

---

## 7. Self-scored verdict

**[REVISED, Phase 3 — adopting `phase2_redteam_audit.md` in full, per the
PHASE-3 UPDATE at the top of this document. The as-filed verdict below this
line originally read "closer to a genuine (informal) REFUTE... than to an
INCONCLUSIVE" and framed the result as "a third, sharper outcome not named
in either of the ranking's own two branches." Both claims over-reached what
this file's own data can support. Corrected verdict follows.]**

**This IS branch (b) of the reconciled ranking (`phase5_redteam_audit.md`
§7 item 1), refined — not a third branch.** Branch (a), "edge-domination
generalizes and the flat result survives," is REFUTED: `ss_tot` ratio to
real-data scale is `9.4×10⁻⁷`, `≈20.2` orders of magnitude above
exp-078's own `5.9×10⁻²⁷` ratio (§5.2), well above the `SS_TOT_DEGENERATE`
guard, confirmed by a convergence-checked (1x→2x→4x, `<0.002%` residual
change) numerical integral, at a battery of gates passing across the full,
never-before-sampled `4.77°–15.50°` bounce-angle envelope. Genuine
`theta_beam`-dependence is recovered — real signal, not float noise.

**But — the single most consequential finding of this cycle, from Red
Team's own Phase-2 audit, given full weight, independently confirmed
three ways (EM analytically, QUANTUM empirically, Red Team's own
from-scratch re-run) — that recovered `theta_beam`-dependence CANNOT
discriminate a real y-wall echo, at ANY period, from no echo at all
(Idealization 9, §6).** Both `theta_local(y_s)` and `dist_image(y_s)` are
pure functions of static geometry with zero `theta_beam` dependence
(§3.1); `E_echo` is therefore the spatial Fourier transform of a
`theta_beam`-independent envelope, evaluated at `k·sinθ_beam` — governed by
the shared aperture window's own support, regardless of the wall's true
reflectance. **The reflectance-ablation control (§5.3) makes this directly
checkable, not merely arguable**: `PAIR_PAD`/`C80−C40`'s recovered periods
survive UNCHANGED (`|ΔP*|≤0.023°`) when `r(theta_local(y_s))` is replaced
with a bare constant `1.0` — geometry alone reproduces them; `PAIR_
ABSORB40`'s signal genuinely requires `ABSORB`-dependence to exist at all
(its ablated delta is EXACTLY zero), but even that signal still lands on
T21's own period, not T28's, because `ABSORB`-dependence only reshapes the
envelope's fine structure, never the aperture window's dominant support.
**A real echo at T28's own period, had one existed, would have been just
as invisible to this instrument as no echo at all is.**

**What this means, precisely (and what it does NOT mean):** it does NOT
mean this file's own Test-A numbers are wrong (they reproduce exactly,
the gates are genuine, the convergence check is real) — it does NOT mean
§5.3's mechanistic reading is false ("the recovered signal is T21's, not
T28's" is true, confirmed three independent ways). **It means this
specific construction was never capable, by its own structure, of
answering whether a real y-wall echo mechanism explains T28's signal, in
either direction.** This is narrower, and more useful for Iteration 57's
own board, than either the original "closer to an informal REFUTE" framing
this section carried as-filed, or a bare "the flat result does not
generalize" headline: it identifies WHY this whole reduction family cannot
answer the question it was built to answer, not merely that it didn't.

**Test A, formally: 1/3 nominal SUPPORT (`C80−C40`, `rel_dev=0.2857`, just
inside the `≤0.30` bar), 0/3 REFUTE, 2/3 INCONCLUSIVE (primary proxy);
0/3 SUPPORT, 0/3 REFUTE, 3/3 INCONCLUSIVE (secondary proxy). This one
nominal SUPPORT is non-informative, not merely marginal, now that the
ablation control (§5.3) is in the record**: the `C80−C40` T21-forced-fit
sub-check lands JUST outside the SUPPORT bar (`rel_dev=0.3101` at T21's
exact period, vs. the free-fit's own `0.2857`) — the SUPPORT/INCONCLUSIVE
line for this one comparison rides on a `~2%` sub-fitting-window
difference between curves that are, structurally, all measuring the same
T21-scale quantity, not an independent T28-matching frequency. `PAIR_PAD`
— T28's own actual dominant empirical target — is the LEAST close of the
three (`rel_dev=0.5679`) under the primary proxy, and the secondary proxy
loses even the marginal SUPPORT entirely.

**Overall characterization: does the flat/zero-amplitude result generalize
from the single-edge reduction to the full aperture sum? Literally, in the
narrow sense ("does the strict `ss_tot`-near-float-noise flatness
survive"): no — correctly answered.** But the deeper question the
reconciled ranking's own framing treated that narrow question as a proxy
for — whether the y-wall self-echo-off-the-near-wall mechanism sub-class
is close to exhausted, or newly worth pursuing — **is not actually closed
by this cycle either way**, because the instrument this file built is
structurally incapable of closing it in either direction. A different,
better instrument is needed, not a refinement of this one.

**Recommended next step (adopting `phase2_redteam_audit.md` §8/§9's own
finding, not this file's own as-filed judgment)**: building the full
non-reduced y-mirrored propagator by adding the far-wall/far-edge pair
(item 8 of exp-078's own ranking, still deferred, Idealization 3) is very
likely NOT the productive next step — it would add a SECOND `theta_beam`-
independent per-point weight term summed against the SAME shared
driven-phase ramp, inheriting this cycle's own structural limitation
unchanged. **The productive next move, if the y-wall coherent-echo
mechanism sub-class is worth testing further, is a construction that
breaks the "static per-point angle" pattern** — a plane-wave/global-
steering incidence-angle picture for the y-wall, the genuine analogue of
what already makes the x-wall's own two-plane-wave reduction (§3.1 of this
file; `phase1_proposal.md` [exp-078] §3.1) a `theta_beam`-dependent test
of the wall's reflectance in the first place — rather than another
refinement within the current point-source/per-point-image family.
