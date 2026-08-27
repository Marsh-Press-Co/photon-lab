# PHASE 1 — PROPOSE · Panel Iteration 56 · exp-079
## The full, non-edge-reduced y-mirrored aperture sum: does exp-078's flat/zero-amplitude result generalize? (T28)

*Fresh sub-agent, MATERIALS & METAMATERIALS charter (PANEL.md seat 2:
sub-wavelength structure; what could physically realize the proposed
optical behavior; owns the realizability bound), lead by rotation.
Executes `experiments/078-.../phase5_redteam_audit.md` §7 Tier 0 item 1 —
the reconciled Iteration-56 ranking's single highest-value item on the
whole T28 board.*

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
reappears (`ss_tot` ratio to real-data scale `9.4×10⁻⁷` — nine orders of
magnitude above exp-078's own `5.9×10⁻²⁷` floor). Genuine `theta_beam`-
dependence exists in the full sum that the single-point reduction could
never see, exactly as Red Team's own §2d flagged as "a real possibility."

But the newly-recovered oscillation is not a match to T28's own family. It
sits within 1.6%–3.5% of T21's own already-established, already-distinct
aperture-diffraction fringe (`1.9608°`, `A=752`) — not near T28's own
2.84°–4.6° periods (28.6%–56.8% away) — and EVERY individual config's own
curve, not merely the pair-deltas, already carries this same ~2.0° period
at `R²=0.97–0.98`. The mechanism is legible: the SAME driven-phase ramp
that produces T21's real fringe in the direct field dominates this
echo-model's coherent sum too; the y-wall geometry contributes only a
slowly-varying envelope, not an independent new frequency. Edge-domination
in the strict "flat" sense does not generalize — but the full sum still
does not explain T28's own real signal.

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
**Actual result (§5): neither branch cleanly — the flat result does NOT
survive (ruling out (a)), but the recovered signal does not support (b)'s
own implicit expectation that non-flatness would indicate a genuine T28
match either** (§5.3/§5.4) — a third, sharper outcome not named in either
of the ranking's own two branches, reported honestly rather than forced
into whichever branch it resembles more.

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
`ss_tot(real PAIR_PAD) = 6.439×10⁻⁵` — ratio `9.392×10⁻⁷`. This is **nine
orders of magnitude above** exp-078's own single-edge, rigorous-angle
model's `5.9×10⁻²⁷` ratio (`phase5_redteam_audit.md` §2c) — well above the
`SS_TOT_DEGENERATE` floor (`1×10⁻²⁰`), confirmed `ss_tot_degenerate=False`
in code. This is real, resolvable, non-degenerate signal, not floating-
point rounding noise on a flat array. **The flat result from the single-
edge reduction does NOT generalize to the full aperture sum.** Every
individual config's own `Re{E_echo(cfg,theta_beam)}` curve shows real
`ptp` variation (`C40`: `1.487×10⁻⁵`; `C60`: `3.509×10⁻⁷`; `C70`:
`3.365×10⁻⁷`; `C80`: `1.789×10⁻⁷`; `G40`: `1.693×10⁻⁵` — `C40`/`G40`, both
`ABSORB=40`, an order of magnitude larger than `C60`/`C70`/`C80`, matching
the same `|r|` ordering exp-078 already established).

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
   deferrable Phase-2 hardening item).

---

## 7. Self-scored verdict

**Neither of the two branches the reconciled ranking explicitly named
(`phase5_redteam_audit.md` §7 item 1) is what happened — a third, sharper
outcome, reported precisely rather than forced into either.**

**Branch (a), "edge-domination generalizes and the flat result survives":
REFUTED.** `ss_tot` ratio to real-data scale is `9.4×10⁻⁷`, nine orders of
magnitude above exp-078's own `5.9×10⁻²⁷` floor, well above the
`SS_TOT_DEGENERATE` guard, confirmed by a convergence-checked (1x→2x→4x,
`<0.002%` residual change) numerical integral, at a battery of gates
passing across the full, never-before-sampled `4.77°–15.50°` bounce-angle
envelope. This is real signal — the flat result does NOT generalize.

**Branch (b), implicit expectation that non-flatness "would justify the
full build for the first time" because it signals a genuine T28 match:
NOT SUPPORTED.** The recovered oscillation sits 1.6%–3.5% from T21's own
already-established, already-known-distinct-from-T28 fringe period
(`1.9608°`), not near T28's own real family (28.6%–56.8% away at the SAME
model periods) — and this is mechanistically explained, not a
statistical coincidence: every individual config's own curve, not just the
pair-deltas, already carries the T21-family period at `R²≥0.97` (§5.5),
confirming the coherent sum's dominant frequency is inherited from the
SAME `A=752`-scale driven-phase ramp that produces T21's real fringe,
weighted by a slowly-varying (not independently oscillatory) reflectance/
distance envelope. LOGBOOK's own founding T28 argument (two sinusoids
sharing one frequency sum/difference to a third at that SAME frequency,
regardless of amplitude/phase) applies here exactly as it did to rule out
"T21 fringe, differently weighted" for the real data.

**Test A, formally: 1/3 nominal SUPPORT (`C80−C40`, `rel_dev=0.2857`, just
inside the `≤0.30` bar), 0/3 REFUTE, 2/3 INCONCLUSIVE (primary proxy);
0/3 SUPPORT, 0/3 REFUTE, 3/3 INCONCLUSIVE (secondary proxy).** The one
nominal SUPPORT should be read with real skepticism, not taken at face
value: it sits an order of magnitude closer to T21's own frequency
(`rel_dev=0.0353`) than to its own nominal target (`rel_dev=0.2857`, just
inside the bar) — the same "compromise fit between two nearby,
imperfectly-separated frequencies" shape this program's own Iteration-47
precedent (P-070-1) already established as evidence AGAINST treating a
marginal SUPPORT as real confirmation, not for it. `PAIR_PAD` — T28's own
actual dominant empirical target — is the LEAST close of the three
(`rel_dev=0.5679`) under the primary proxy, and the secondary proxy loses
even the marginal SUPPORT entirely, confirming this reading rather than
contradicting it.

**Overall characterization: the y-wall self-echo-off-the-near-wall
coherent mechanism, now tested in its full (non-edge-reduced) form, is
NOT flat/degenerate — but it also does not match T28's own real
periodicity. Both of these are genuine findings, not a wash.** The
mechanism's flatness at the single-edge, rigorous-angle reduction was a
property of that specific reduction, not of the underlying physical
question (confirming exp-078 Phase-5's own §2d caveat that the flat result
might not generalize) — but the full sum's own honest answer is that it
recovers a DIFFERENT, already-known, already-ruled-distinct-from-T28
frequency, not T28's own signal. This is closer to a genuine (informal)
REFUTE of "the y-wall self-near-wall echo mechanism explains T28's real
signal" than to an INCONCLUSIVE — but is reported as a Test-A-only,
period-based characterization (no Test B / shape match is built here,
matching exp-078's own scope discipline) and is NOT filed as a formal
pre-registered-band REFUTE, since the pre-registered band was built for
comparing a model's OWN period against T28's, not for adjudicating a
three-way "matches X, not Y, and here's why" finding — the band's own
literal verdicts are reported in full above (§5.3/§5.4) without editing,
and this prose states what they mean, not a replacement for them.

**Recommended next step, stated plainly**: per the reconciled ranking's
own §7 conditional language ("if it does NOT generalize... that is itself
the discovery of genuine θ-dependence... and would justify the full build
for the first time"), the STRICT flat/zero-amplitude result did not
generalize — but this file's own §5.3/§5.4 finding (the recovered
θ-dependence is T21's, not T28's) is a materially different, and more
informative, answer than a bare "does not generalize, build the full
model" would have been. Building the full non-reduced y-mirrored
propagator (adding the far-wall pair, item 8's own deferred refinements)
is unlikely to change this file's own central finding — a slowly-varying
envelope addition to an already-identified T21-frequency-dominated sum is
very unlikely to introduce a genuinely NEW, independent, T28-matching
frequency — but this is stated as a judgment, not re-verified numerically
this cycle; Phase 2 may reasonably ask for it to be checked, or may
concur that the y-wall self-echo-off-either-wall coherent-echo sub-class
is, on this evidence, close to exhausted for explaining T28's own real
signal specifically (though not for the general question of whether
SOME y-wall-adjacent effect contributes — see Idealization 3).
