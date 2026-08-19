# PHASE 5 — REVIEW · Panel Iteration 23 · exp-046 · Seat: ELECTROMAGNETISM

*Fresh context, blind to the other six Phase-5 reviews. Charter: field/wave
behaviour, impedance matching, energy coupling; owns the reciprocity /
passivity / causality bookkeeping. Every number below was re-derived from
first principles or re-run from the repo in this session. Where I ran new
FDTD, I say so and give the configuration; where I disagree with the cycle's
own record, I show the work rather than assert it. Scripts:
`/tmp/.../scratchpad/em{1..11}.py` (this session, not committed).*

---

## 0. Headline

The cycle is honestly run and its discipline held: the prediction freeze is
real and I reproduced it; `profile="gauss"` is gated for the first time and
the gate genuinely fires on the defect the cycle had; Block C's closed form is
correct and its verification is not tautological. Three of its four headline
claims do not survive independent re-derivation at the precision they are
stated:

1. **The S16-b diagnosis is right in direction and wrong in magnitude, and it
   mis-attributes ~40% of the offset to the engine.** The comparator the
   amended gate now scores against — `exact_center`, written post-freeze, in
   the results commit, reviewed by nobody — models `add_line_source` as a
   prescribed aperture *field* and reduces to `|E|²`. `add_line_source` is an
   additive line-**current** array and `observer_profile` returns **−⟨Sₓ⟩**.
   Correcting both, the engine reproduces exact non-paraxial physics to
   **0.45 cells (0.49% of the beam half-width)**, not 5.4%. **The correct
   comparator was already in this repo, and this same cycle already uses it**
   (exp-042's `_G0_for` + obliquity-on-H, the Block-A band-setter). These are
   the same two obliquity-bookkeeping errors this seat caught at Iteration 19
   — now inside the trust suite instead of an experiment.
2. **P-TH23-A5's "0.03%/0.11%" agreements are conditioning artefacts.** Both
   low-N_F legs sit at C_empty = −0.9969 / −0.9877. In the informative
   quantity B_obj/B_flank = 1+C the disagreement is **8.41% / 8.37%**, and the
   amplification factors are **326× / 81×** — inside the very "77–300×" range
   this cycle cites when it **drops P-TH23-A7 for being unusable**, at the
   identical two C_empty values. "Validated three orders of Fresnel number
   outside where it was built" is carried entirely by those two legs.
3. **The `--only` erratum is overstated.** `--only 16 → {1,6,16}` is real and
   correctly fixed. But "`--only 12346789,10,11`, cited as 46/46 across five
   SESSION_LOG entries, selected only stages 10 and 11" retro-applies the
   Iteration-17 code to five citations that all predate it. No historical
   citation was damaged.

Charter bookkeeping — **reciprocity, passivity and causality are genuinely
untouched, verified against the diff, not accepted on assertion.**

Verdict: **PARTIAL.**

---

## 1. My reading of the record

### 1.1 `width = w₀/cos θ₀` — re-derived from scratch. It holds.

I did not read Red Team's Attack 1b before deriving this. Source field on the
fixed vertical line, `Y ≡ y − y_c`:

> `E(Y) = exp(−Y²/w²)·exp(i k sinθ₀ Y)` ⇒ `A(k_y) ∝ exp(−(k_y − k sinθ₀)²w²/4)`

Propagating directions map as `k_y = k sinθ`, so the far-field intensity is
`I(θ) ∝ exp(−k²(sinθ − sinθ₀)²w²/2)`; half-max at `k|sinθ−sinθ₀|w = √(2ln2)`.
The half-width in **sinθ** is fixed by `w`; converting to angle at θ₀ costs a
Jacobian `d(sinθ) = cosθ₀ dθ`, so

> `Δθ = 2√(2ln2)/(k w cos θ₀) = C λ/(w cosθ₀)`,  `C = √(2ln2)/π = 0.3747812502585552`

⇒ to emit `Δθ` you must pass `w = w₀/cos θ₀`. Two independent cross-checks:

- *Geometric:* the straight aperture's projection perpendicular to the beam is
  `w_line·cosθ₀`; setting that to `w₀` gives the same answer. Two routes, one
  result.
- *Numerical (`em1.py`):* exact angular-spectrum far-field FWHM, obliquity
  applied once via `k_x` (i.e. through H), over 12 (θ₀, Δθ) cells. With
  `width = w₀` the emitted FWHM is inflated by exactly `1/cosθ₀`
  (2.608°/2.000° = 1.3043 vs 1/cos40° = 1.3054). With `width = w₀/cosθ₀` it
  reads **2.000° / 4.98° / 9.84° / 18.80°** at nominal 2/5/10/20° and θ₀ = 40°.

**So Red Team's central ruling is correct and the docket's adoption of it is
correct.** Two riders the cycle does not state:

- The identity degrades to **6% at the FWHM=20° cells** (18.80° emitted for
  20° nominal), and the far-field **peak drifts to 38.10° for a nominal
  θ₀=40°** — a 1.9° pointing error, purely from the non-paraxial `sinθ`
  mapping. Nothing in Block A scores this.
- The previous seat's Phase-2 reassurance that "no non-propagating power is
  smuggled in" (`exp(−(πw₀/λ)²) ≈ 1.2×10⁻⁵`) was computed at **θ₀ = 0** and
  does not transfer. At the adopted width and θ₀ = 40°, FWHM = 20°
  (`em10.py`): spectral amplitude at the evanescent boundary is **8.4×10⁻²**
  and the evanescent **power fraction is 8.3×10⁻⁴** — four and seven orders
  of magnitude worse respectively than the number on the record. Small in
  absolute terms; not "honest at the level claimed" as stated.

### 1.2 S16-b: the target is wrong, but so is the amended target

**Reproduced first.** Independent process, my own driver (`em4.py`), same
committed geometry: FDTD centre **992.0927**, peak cell **977.0**, half-width
**90.988**; gate-d half-width **80.4715**. Bit-for-bit with `results.json` and
with `run_all.py --only 16` (which I also ran: 4/4, 75 s). No dispute about
what was measured.

**The comparator, from the code.** `add_line_source` appends a per-cell array
and the solver does `Ez[x, sl] += env·sin(ωn − phase)·profile`
(`lab/fdtd2d.py:232-237`) — a prescribed **current sheet**, whose radiated
field spectrum is `Ẽ(k_y) ∝ J̃(k_y)/k_x`, i.e. carrying `1/cosθ`.
`observer_profile` returns `−⟨Sₓ⟩ = −½Re(Ez conj(Hy))` (`lab/ambient.py:36-39`
→ `lab/sections.py`), which carries `+cosθ` **once, via H**. Stage 16's
`exact_center` has **neither**: it propagates a prescribed *field* and reduces
to `|E|²`. Two missing obliquity factors, in opposite directions, and neither
cancels.

Four models, one FDTD number (`em2.py`, `em3.py`, S16-b configuration):

| desk model | 1/e² centre | half-width | peak |
|---|---|---|---|
| ray optics | 979.12 | — | — |
| field aperture, `\|E\|²` — **what stage 16 uses** | 987.14 | 89.10 | 973.56 |
| field aperture, Sₓ | 983.04 | 86.85 | 970.73 |
| current aperture, `\|E\|²` | 996.75 | 94.65 | 979.71 |
| **current aperture, Sₓ — the physically correct one** | **991.67** | **91.59** | **976.56** |
| **FDTD (measured)** | **992.09** | **90.99** | **977.0** |

And the decisive check: **exp-042's own committed, corrected-convention
Huygens–Fresnel propagator** — `_G0_for` (bare Hankel asymptotic, i.e. a line
*current* kernel) with obliquity on H and `Sₓ = Re(E conj H)`, the propagator
**this cycle's own `prop_c_empty` uses to set every Block-A band** — gives
(`em7.py`) centre **991.64**, half-width **91.58**, peak cell **977.0**:
**0.45 cells from FDTD, 0.49% of the beam half-width**, and the half-width to
0.01 cells.

**Blind prediction test** (`em6.py`), three configurations neither the cycle
nor I had run, predicted at the desk and then solved:

| config | ray | field/\|E\|² model | current/Sₓ model | FDTD | err(field) | err(current) |
|---|---|---|---|---|---|---|
| w=30, θ₀=30° | 920.75 | 927.10 | 930.43 | **931.05** | +3.95 | **+0.62** |
| w=70, θ₀=36° | 954.02 | 955.23 | 956.05 | **956.66** | +1.44 | **+0.62** |
| w=28.03, θ₀=40° (FWHM 20°) | 979.12 | 994.22 | 1005.09 | **1005.55** | **+11.32** | **+0.46** |

Consequences, in order of how much they matter:

- **The engine is exact to sub-cell.** `add_line_source(profile="gauss")` and
  the propagator have **no pointing defect at all**: 0.25–0.62 cells across
  four independent (width, θ₀) points spanning 10–20° divergence and 30–40°
  steering. The NOTES' "FDTD sits 4.95 cells (5.4% of the beam half-width)
  from the exact value" is **entirely comparator error**. So is A-v2's 2.26
  cells (correct comparator: 0.26).
- **The NOTES' framing "both estimators fail; there is no reading of this
  configuration that lands inside ±2 cells" reads as a property of the
  configuration.** It is a property of the ray-optics target. Against the
  correct target *both* FDTD estimators land inside 0.5 cells — the peak-cell
  reading 977.0 matches the correct model's 976.56/977.0 exactly.
- **The amended gate is simultaneously ~11× too loose and mis-targeted.** The
  8% bar was set "margin above the measured value" where the measured value
  (5.4%) is comparator error; the engine's demonstrated accuracy is 0.5%. Worse,
  at Block A's own extreme cell (FWHM = 20°, θ₀ = 40°, the third row above) the
  wrong comparator is off by 11.32 cells = **9.4% of the half-width — the
  amended gate would FAIL, and would blame the engine for its own comparator.**
  A gate that cannot be trusted to fail for the right reason is not a gate.
- **Gate S16-d inherits a milder version.** Its closed-form target 79.4747 sits
  **1.95% below** the exact answer (81.05, `em3.py`); FDTD is 0.7% from exact.
  So roughly two-thirds of the reported 1.25% residual is target error. Passes
  comfortably at a 5% bar, but the pattern is the same.

**Is the S16-b failure a target-attribution issue rather than a defect in
`add_line_source` or the propagator?** Yes — I checked the implementation
directly and independently, and the answer is a stronger yes than the cycle
gives itself. The `yc` used by the taper and by the phase ramp is the same
value (`lab/fdtd2d.py:153,161`), so there is no half-cell registration bug; the
phase ramp is continuous with no rounding stage (consistent with T21's own
finding); and the launched angle survives Yee numerical dispersion to ~10⁻³
degree at cpl = 20, worth <0.01 cells over `D_SP`. The engine is clean. But
the cycle's *stated* attribution — "the paraxial assumption failing at 14°
divergence" — accounts for only 8.0 of the 12.97 cells. The remaining 4.95 is
attributed to the engine and is in fact the second and third obliquity errors
in the comparator.

### 1.3 P-TH23-A5 — the cycle's only falsifiable content, re-scored

Phase 3 says it plainly: "*the genuine falsifiable content is the
FDTD-vs-propagator agreement at the four new Fresnel numbers (A5)*." I agree,
which is why it deserves the hardest look.

`results.json` re-expressed in the unsaturated quantity (`em`-analysis):

| leg | N_F | C: prop vs FDTD | rel in **C** | rel in **1+C = B_obj/B_flank** | conditioning \|C\|/\|1+C\| |
|---|---|---|---|---|---|
| A-v1 (600, 40°, 2°) | 53.98 | −0.123345 / −0.125698 | 1.91% | **0.268%** | 0.1× |
| A-v2 (600, 40°, 10°) | 2.16 | −0.996664 / −0.996945 | 0.028% | **8.405%** | **326×** |
| A-v3 (600, 40°, 20°) | 0.54 | −0.986618 / −0.987738 | 0.114% | **8.373%** | **81×** |
| A-v4 (750, 38°, 2°) | 65.60 | +0.163673 / +0.154376 | 5.68% | **0.799%** | 0.1× |

A-v2 and A-v3 are the legs where the beam has walked entirely off the object
window, so `B_obj/B_flank` ≈ 0.003–0.013 and any model that puts the beam
off-window scores C ≈ −1. `run.py` itself drops P-TH23-A7 with the words:
*"ill-conditioned by 77-300x at these C_empty values (-0.997/-0.987)"* — the
same two legs, the same two numbers. The cycle applied its own disqualifying
criterion to one prediction and not to the neighbouring one.

Both legs still **pass** in the honest currency (8.4% against a 15%/35% band),
so nothing is refuted. But the reported precision is inflated ~300×, and — the
part that matters — **the two ill-conditioned legs are precisely the ones that
reach the new regime.** The properly-conditioned legs sit at N_F = 54.0 and
65.6, only ~6× below the 310–518 the propagator was built at, not three orders
of magnitude. Corrected statement of Learned item 1:

> *exp-042's desk propagator reproduces FDTD to **≤0.80%** at N_F ≈ 54–66 (a
> factor ~6 extension), and to **≈8.4%** at N_F ≈ 0.5–2.2, where the reduction
> is ill-conditioned by 81–326× and the reading should not be quoted in C.*

### 1.4 The 5.68% residual — narrowed, at four FDTD runs of new cost

A-v4's 5.68% is the one number in Block A that could have been physics. The
NOTES flags a possible settling confound (idealization 11, "the **fifth**
consecutive cycle in which the dedicated settling-margin test is not run") and
leaves it there. I ran it (`em8.py`, `em9.py`, `em10.py`, `em11.py`). First,
both informative legs reproduce **bit-identically** on a fresh process.

| candidate | test | result |
|---|---|---|
| **settling** | STEPS 1400 → 2800 → 4200 | A-v4 **0.083%**, A-v1 **0.036%** — ruled out; idealization 11's concern is now closed for the legs that matter |
| **source-aperture truncation** | extend aperture by 400/1000/2000 cells | **0.06% / 0.01%** — ruled out |
| **Hankel far-field asymptotic** | exact `H₀⁽¹⁾` vs `e^{ikR}/√R` in the propagator | **0.031%** — ruled out |
| **Yee numerical dispersion** | ordering | disfavoured — A-v4 is the *finer* grid (cpl 25 vs 20) and the *worse* residual |
| **FDTD absorbing-boundary bands** | ABSORB 40 → 60 (source span held fixed) | **gap falls 5.68% → 1.43%**; ΔC = **0.0070 absolute** |

So the residual is **mostly a boundary artefact of the FDTD scene**, not a
propagator failure — the desk propagator is *better* than this cycle credits
it. Two riders: ABSORB = 80 reads 2.42%, non-monotone, but at that width
`SRC_X = 300` sits inside the x-damping band, so that point is confounded and
the sweep needs a proper design. And the absolute shift, **0.0070 in C, is
1.4× VISION's own C_thr = 0.005** — on a channel (`C_empty` at oblique
wide-beam legs) that the entire T21/T16 line runs through, at an `ABSORB = 40`
inherited unexamined from exp-041.

### 1.5 Reciprocity / passivity / causality — my charter's own line

Verified against the diff, not accepted on assertion.
`git diff 8fdea02 460f018 -- lab/fdtd2d.py lab/materials.py lab/sections.py
lab/ambient.py lab/emit.py` returns **zero lines**. The whole cycle touches
`lab/validation/run_all.py`, `VALIDATION.md`, and the experiment directory.
Therefore:

- **Passivity:** no update coefficient changes. `ca`, `cb`, `eps_r`,
  `sigma_e`, `pec`, `inv_mu` are untouched. Block A's scenes are ε_r ≡ 1 or
  the exp-041 sponge at `σ = 0.10/(2·78) > 0` — dissipative, passive. The
  Gaussian source is an *excitation* change, not a medium change: it only
  appends to `Sim.sources`.
- **Reciprocity:** scalar isotropic ε and σ, no anisotropic-µ path engaged.
  Reciprocal.
- **Causality:** non-dispersive ε with a real static σ is trivially
  Kramers–Kronig-consistent. Nothing in the cycle introduces gain, time
  variation, or dispersion.
- **T1:** escape route NONE is correctly declared. No constraint-1/2/3/4
  claim is made or implied anywhere in this cycle. Correct.

One residual charter note the cycle does not carry: the launch ramp `env` is a
function of step only, so the tilted wavefront switches on **synchronously**
across a 1504-cell aperture, where a physically launched tilt would sweep
across it over ≈ `L·sinθ₀` = 967 cells of light travel — comparable to the
920 cells of post-ramp budget at STEPS = 1400. This is a standard CW
idealization and I measured it to be harmless here (§1.4: ≤0.083%), but it is
the mechanism idealization 11 is actually about, and it is now tested rather
than deferred a sixth time.

### 1.6 Does stage 16 satisfy PANEL.md's identity-gate rule?

**Yes — but through gates (a) and (d), and neither (b) nor (c) should be
counted.**

- **(a) free-space divergence identity** — legitimate, and it passes *for the
  right reason*, which I checked rather than assumed: the exact answer sits
  within **0.43%** of the closed form at z = 223 (`em5.py`), so the measured
  1.06% really is engine accuracy, not target error. Zero free parameters, and
  a real lever (w grows 43% over the three planes). This alone satisfies the
  rule.
- **(d) oblique-width identity** — legitimate and *discriminating*: 9.8% at the
  wrong width, 1.25% at the right one. It is the stage's reason to exist and it
  works. (Rider: two-thirds of its 1.25% is target error, §1.2.)
- **(c)** is a bit-reproduction regression anchor against a previously
  committed number, not an absolute identity. Useful; not the rule's currency.
- **(b) as amended** is a model-vs-model comparison, with a post-hoc bar, against
  a physically wrong model. It should not be counted toward the rule at all.

**The real gap is coverage, not legitimacy.** Both identity gates run at
w₀ ≈ 2λ (40 and 42.947 cells). Block A's own cells run from **w₀ = 1.074λ**
(FWHM 20°, where the emitted FWHM is already 6% off and 8×10⁻⁴ of the power is
evanescent) to **w₀ = 10.74λ** (FWHM 2°, where the truncation idealization
lives). Neither extreme is gated. The stage certifies the middle of the block's
parameter range and nothing else — and the block's own worst A3 residual
(3.25%) and its whole A5 low-N_F reach both live at the ungated end.

### 1.7 The `--only` claim — verifiable, and overstated

I executed all three historical selector implementations side by side
(`sel.py`), and dated the code and the citations from git:

| invocation | Iter-15 code (≤ 2026-08-16) | Iter-17 code (2026-08-17→) | this cycle |
|---|---|---|---|
| `12346789,10,11` | **1,2,3,4,6,7,8,9,10,11** (= 46) | 10,11 | 1,2,3,4,6,7,8,9,10,11 ✓ |
| `12` | 1,2,12 | 1,2,12 | 12 ✓ |
| `16` | 1,6,16 | 1,6,16 | 16 ✓ |
| `12346789,10,11,12,13,14,15` | 1..15 incl. **5** (over-selects) | 10–15 | 1,2,3,4,6,7,8,9,10–15 ✓ |

The Iteration-17 tokenizing fix landed in **6082e02, 2026-08-17**. All five
SESSION_LOG `--only 12346789,10,11` → 46/46 citations are at lines 916, 1026,
1155, 1253, 1347, under headers dated **2026-08-14, -15, -15, -16** (Iterations
8–12). Every one of them ran under the Iteration-15 selector, which selected
exactly the intended ten stages. **They were correct when made.** In the two
days the regression actually existed, the standing invocation had already moved
to the fully comma-separated form (`--only "1,2,3,4,6,7,8,9,10,11,12,13,14,15"`,
82/82, SESSION_LOG:218) — which is correct under the Iteration-17 code. **No
published trust-suite citation in this program's history was damaged by this
bug.**

The fix itself is right, the recurrence is real, and the `--only 16 → {1,6,16}`
and `--only 12 → {1,2,12}` halves of the claim are correct. But the sentence
now in `VALIDATION.md:51-53` and NOTES Learned item 5 retro-invalidates five
historically valid citations, and would propagate into LOGBOOK as an erratum
against exp-031/032/033/034/035. **It should be corrected before it does.**

### 1.8 What I checked and found sound

- **Prediction freeze.** `run.py --predict-only` today is byte-identical to
  `predictions_frozen.txt` modulo its own timing line; commit `a7eaaf8`
  contains `run.py` + `predictions_frozen.txt` + stage 16 and **no**
  `results.json`. The structural argument (the `lab.fdtd2d` import lives inside
  `fdtd_leg`) is true. House discipline held.
- **`profile="gauss"` never previously exercised** — grep and
  `git log --all -S` confirm: zero call sites outside this cycle and the new
  stage. The claim is exact.
- **Block B arithmetic** reproduces end to end: `(w_on/r_out)² = 9.1519231`
  (7.079002e-6 / 2.34e-6 = 3.0252145, squared); `dt_ss` ratios 3.0280 / 9.1519;
  `netd_lo/dt_ss` = 0.02/3.293076e-5 = **607.33**; 1839 / 5558 for the two
  endpoints. The mixed regime is self-consistent, and the reason PHOTONICS'
  Iteration-22 area-cancellation proof does **not** apply here is correct and
  worth stating: ΔT_ss is area-invariant only when the power area and the
  conduction area are the *same* area, which is exactly what the mixed regime
  breaks.
- **Block C's closed form is correct.** I re-derived it: composite map
  `n_{k+1} = n_eq(1−a) + a f n_k` with `a = e^{−D/τ_k}`, `f = e^{−m/(1+r)}`;
  fixed point over first pulse = `1/(1−af)`; `>1.05 ⟺ af > 1/21 ⟺ D/τ_k <
  ln(21f)`. The r=1.0 falsification is right: `21e^{−2.5} = 1.7238 > 1`, sup
  ratio `1/(1−0.082085) = 1.0894`. The 0.5τ crossings `ln(21e^{−0.5}) =
  2.5445224` and `ln(21e^{−0.4545}) = 2.5899770` both check. This is the
  cleanest work in the cycle: it converts Amendment 3's host-list correlation
  into one dimensionless criterion with a mechanism, which is exactly what
  Iteration 16's own "near-tautological co-location" caution asked for.

---

## 2. Physical meaning

**Block A.** Stripped of the comparator errors, what this cycle actually
established is narrower and better than what it claims: `add_line_source`'s
never-exercised Gaussian path, driven obliquely by a phase ramp, radiates
**exactly** what current-sheet electrodynamics says it should — beam centre to
0.25–0.62 cells and 1/e² width to ≲0.7% across 10–20° divergence and 30–40°
steering, against a zero-free-parameter angular-spectrum calculation. That is a
genuinely valuable engine result and it is *stronger* than the "5.4%" now on
the record. What it does **not** establish is any T21 finding. The
contamination-risk question is untouched: A1 is correctly withheld, the
partial-coherence bridge is not built, no sourced flashlight coherence length or
beam FWHM exists, and QUANTUM's Iteration-20 conjecture is correctly recorded as
*mis-posed* rather than tested. T21's live half — *which amplitude scale governs
a real object-present or beam-swept scene* — is exactly where Iteration 19 left
it.

**The physics of the S16-b failure, said properly.** Three distinct effects
separate ray optics from the measured beam centre, and only the first is in the
cycle's diagnosis:

1. *Non-paraxial `sinθ` mapping* (+8.0 cells): the Gaussian is Gaussian in
   `k_y`, and `θ = arcsin(k_y/k)` is convex, so the angular distribution skews
   toward larger θ. This is what the NOTES identifies.
2. *Current-source obliquity* (+9.6 cells): the radiated field is `J̃/k_x`, so
   the emitted spectrum is weighted by `1/cosθ` — a further skew toward +y.
3. *Poynting reduction* (−4.1 cells): the measurement is `−⟨Sₓ⟩ = I·cosθ`, one
   obliquity back the other way.

Net +12.5 cells; measured +12.97. The cycle captured (1) and charged (2)+(3) to
the solver. That (2) and (3) are precisely the E-vs-H obliquity pair this seat
adjudicated at Iteration 19 — where the ruling was *"obliquity entering flux
ONCE, via H, not squared via E"* — makes this a fourth appearance of one error
species, and the first inside `lab/`.

**Blocks B and C.** Both are honest and both are, by their own admission,
reproductions or extensions rather than findings. Block B computes T23's third
endpoint and reports it is the least comfortable of three and still
UNDETECTABLE — but **T23 as posed is not answered**: which characteristic
length is *physically licensed* for `h_eff = k_air/L` was never argued to a
conclusion, only enumerated to three endpoints instead of two. Note also that
B1 ("mixed `dwell/τ_thermal` identical to the `r_out` regime to 0.0") cannot
fail: τ_thermal contains no absorbed-power term, and "mixed" is *defined* as
r_out-conduction. It is an algebraic identity reported as a confirmed
prediction — the same species Red Team's Attack 2 caught in A1/A3, one block
over. Block C is the cycle's real scientific content.

---

## 3. Argued next change

**Repair the gate before anything else is built on it, and it costs nothing.**
Stage 16 gate (b) should score FDTD against `exp-042`'s own committed
corrected-convention propagator — the object already in this repo, already
imported by this cycle's own band-setter, already validated at four Fresnel
numbers this cycle — instead of the fresh, unreviewed, doubly-wrong
`exact_center` written in the results commit. With the correct comparator the
bar should be **≤1.5% of the beam half-width**, not 8%: I measured the engine
at 0.31–0.80% across four configurations. And gates should be added at Block
A's actual extremes (w₀ = 1.074λ and 10.74λ), because the two identity gates
that carry PANEL.md's rule both sit at w₀ ≈ 2λ and neither can fail at the
ends where the block's own worst residuals live. Desk half of this work is
already done in this review; the FDTD runs already exist in `results.json`.

The wider point for the program: **this is the second consecutive cycle in
which a same-shift, post-freeze correction shipped a physics convention that
nobody reviewed.** Iteration 19's own LOGBOOK entry records Red Team's warning
verbatim — *"this should not be read as establishing same-shift correction is
generally safe from criterion 4, only that it worked this time."* This time it
did not work, and it landed in `lab/`, where every future cycle inherits it. I
do not think Checkpoint criterion 4 fires: nothing was concealed (the amendment
is disclosed in three places, the original gate is scored as FAILED, and the
Director explicitly invites a reader to treat A1 as withheld). But the standing
rule should be tightened: **a post-freeze change to a trust-suite gate's
*target* — as opposed to its bar or its reporting — is a physics change and
requires a second derivation from an independent route before it is committed.**

---

## 4. Ranked top-3 candidate directions for Iteration 24

**1. Repair and extend stage 16; re-score A5 in the conditioned currency.**
*(Zero new FDTD for the repair; 2 runs for the extension. Tier 1.)*
(a) Re-point gate (b) at exp-042's committed propagator, re-bar at ≤1.5% of
half-width, and record that the engine's measured pointing accuracy is 0.5%,
not 5.4% — this replaces a gate that would currently mis-fire at Block A's own
FWHM=20° cell. (b) Add identity gates at w₀ = 1.074λ and w₀ = 10.74λ. (c)
Re-issue A5 in `1+C` with the conditioning factor printed per leg, and state
the validated Fresnel reach honestly (≤0.80% at N_F 54–66; ≈8% at N_F 0.5–2.2).
(d) Correct the `--only` erratum in `VALIDATION.md` and NOTES before it reaches
LOGBOOK. Highest rank because it is nearly free, it removes a wrong physics
convention from `lab/`, and everything downstream of Block A depends on it.

**2. Characterize the FDTD scene's absorbing-boundary systematic on the
`C_empty` channel.** *(~6–9 FDTD runs. Tier 1.)*
My ABSORB 40 → 60 test moves A-v4's `C_empty` by **4.5% relative / 0.0070
absolute — 1.4× VISION's own C_thr = 0.005** — and closes most of the cycle's
one unexplained residual. `ABSORB = 40` with `SRC_X = 300` and `PLANE_X = 77`
(37 cells of margin) is inherited unexamined by **every** `C_empty` reading in
the T21/T16 line since exp-041, including all 30 Block MAIN rows T21's fringe
mechanism was fitted to and every N9/N17 quadrature delta T16 scores. Design it
properly: sweep ABSORB with `SRC_X` moved clear of the band so the ABSORB = 80
confound does not recur, hold the source span fixed, all 3λ. This is
structurally the same debt T11 tracks for the box-ledger channel — a decision
floor this channel has never had — and it is now measured once and large.

**3. Close T23 by argument, and re-site A5's low-N_F legs.** *(Zero–2 FDTD.
Tier 2.)*
T23 asked *which* length is licensed for `h_eff = k_air/L`; exp-046 answered
with a third number. The `Nu = 2` conduction limit is derived for a real
geometric body, so `r_out` governs conduction and mass while `w_on` governs
absorbed power — that is the mixed regime, and the argument for it can be
written in a paragraph with no new computation. Ship the argument or ship the
reason it fails; three endpoints and no ruling is worse than two. Separately,
if the low-N_F propagator reach is genuinely wanted, re-site those legs at a
geometry where the beam is not entirely off-window, so `|C|` is O(0.1) rather
than O(1) and the reduction is not amplified 80–326×.

*Explicitly not ranked, and why:* another T21 FDTD cycle. T21's live question
is the partial-coherence bridge and a sourced real-flashlight coherence
length/beam FWHM, and this program still has neither. Item 24's hardened
Tier-W glare/adaptation tripwire is a standing program rule and outranks all
three of the above on program integrity, but it is VISION's item, not this
seat's to rank.

---

## 5. Verdict

# PARTIAL

**Reason.** The cycle is honestly run and three things in it are real: the
`w₀/cosθ₀` correction is right and I re-derived it independently; the
never-exercised Gaussian source path is now trust-gated by two legitimate
absolute identity gates; and Block C's memory-onset closed form is correct,
mechanistically explanatory, and verified against the integrator at 250/250
points. Reciprocity, passivity and causality are genuinely untouched, verified
against the diff.

But the cycle's own three headline claims each need correcting. Its Block-A
instrument result understates the engine by an order of magnitude and charges
the difference to the solver, on a comparator that reproduces this seat's own
Iteration-19 obliquity ruling in reverse — and that comparator is now committed
inside `lab/`. Its "validated three orders of Fresnel number" reach is carried
by exactly the two legs the same cycle disqualified elsewhere for 77–300×
ill-conditioning. Its `--only` erratum retro-invalidates five historically
correct trust-suite citations. And the one residual that could have been
physics turns out to be a boundary artefact nobody looked for — which is the
most interesting thing the cycle produced, and it is not in the write-up.

Not RULED OUT: nothing here is refuted, every correction is a sharpening, and
the engine comes out of it *better* validated than the record says. Not
PROMISING: no live thread advanced. T21 is where Iteration 19 left it, T23 has
a third endpoint and still no ruling, and the genuine new result — a
dimensionless memory-onset criterion — belongs to T17, not to the cycle's own
headline.

---

*Corrections this seat asks the Director to propagate to LOGBOOK at close:*
1. T21 — record that `add_line_source(profile="gauss")` + the propagator are
   validated to 0.25–0.62 cells (≤0.8% of half-width) against exact
   current-sheet angular-spectrum propagation at four (width, θ₀) points, and
   that the "5.4%" figure is comparator error, not engine error.
2. T21 — record the `exact_center` convention error (field-aperture + `|E|²`
   where the engine is a current sheet read through `−⟨Sₓ⟩`) as a **fourth**
   instance of the Iteration-19 obliquity species, and the **first inside
   `lab/`**.
3. A5 — record the conditioning: 8.41%/8.37% in `1+C`, amplification 326×/81×,
   and the corrected Fresnel reach.
4. `--only` — correct the erratum: the five SESSION_LOG 46/46 citations
   (2026-08-14…16) predate the Iteration-17 fix (2026-08-17) and were valid.
5. **New open item / candidate thread:** the `C_empty` channel's
   absorbing-boundary systematic — 4.5% relative / 0.0070 absolute at
   `ABSORB` 40→60, on the boundary every T21/T16 reading since exp-041
   inherits.
6. Idealization 11 — the settling-margin test is **run** for the two
   informative A5 legs (0.036% / 0.083% at 3× STEPS); the fifth deferral is
   closed for those legs, and settling is ruled out as the A-v4 confound.
