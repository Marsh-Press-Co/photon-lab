# exp-052 Phase 1 — The Fixed-Absolute-Thickness `graded_black_shell` Variant

Panel Iteration 29. Lead: THERMODYNAMICS (rotation). Executes the
**unconditional** build trigger locked at Iteration 28 Phase 2 (re-verified
intact three independent ways at Phase 5) and bound in `PLAN.md`
(`LOCKED — panel Iteration 29`): build and measure the fixed-absolute-
thickness `graded_black_shell` variant's own ambient-contrast `C`.
First queued Iteration 7 (`experiments/030-scale-bridge`, MATERIALS' own
Phase-2 flip); re-ranked without being reached at Iterations 25–28 — a
21-iteration deferral.

## 1. Mechanism narrative (≤300 words)

Every `graded_black_shell` reading this program has ever cited —
including the C≈−0.72 anchor used throughout T8/T13/T14 — comes from a
**self-similar** construction: `r_in(r_out) = round(30/78 · r_out)`, with
`sigma_max(r_out) = 0.5/κ` rescaled to hold the shell's radial optical
depth `τ_shell = σ_max·(r_out−r_in)` fixed at 24.0 as the object scales.
`REALIZABILITY_MEMO.md`'s Entry 2 formalized why that construction is the
*harder* realizability ask: it needs a re-engineered coating recipe at
every target size, and its self-similar thickness diverges to 0.31–0.92 m
at witness scale — no macroscopic real-material precedent. Real
ultra-black coatings (CNT-forest / Vantablack-class) instead carry a
**fixed absolute thickness independent of substrate size** — the opposite
scaling law. That distinction has sat as an argued-not-tested claim for
21 iterations; this experiment builds the object the claim is actually
about and measures its own `C`, directly, rather than reasoning about it
by analogy.

**Construction:** hold the shell's absolute thickness fixed at 48 cells
(the r=78-native value) — `r_in(r_out) = r_out − 48` — instead of scaling
`r_in` with `r_out`. **`sigma_max` is held fixed at 0.5** (the literal
r=78-gated value), not rescaled: a real coating's own conductivity/doping
does not change with the size of the object it is painted on, so "same
material, same thickness, bigger substrate" is the construction that
actually tests MATERIALS' realizability claim, not a formula that merely
avoids the self-similar family's optical-depth confound by another route.
This is a live design choice (§3 justifies it over the alternatives) — it
answers whether a *physically reusable* coating recipe produces a
materially different `C(r_out)` trend than the self-similar family, and
specifically whether it still shows T14's wrong-direction shallowing.

## 2. Parameter table

### 2a. Geometry — reused verbatim from `experiments/030-scale-bridge/design_geometry.py`

The domain-construction rule (`PLANE_DX=15`, `ABSORB=TAPER=40`,
`MARGIN_MULT=3.5`, `FALLBACK_ANGLES` N9 ±35°) is **unchanged from
exp-030** — only the material law inside the object window differs. Reuse
is deliberate: exp-030's own R-gate, δ_C empty-scene floor, and settling
diagnostics were already measured and passed at these exact `NX/NY/OBJ/
PLANE_X/D_SP/STEPS` geometries (§5 states which of those transfer and
which are re-verified).

| r_out (cells) | κ | NX | NY | OBJ | PLANE_X | D_SP | STEPS_AMBIENT | z/z_R |
|---|---|---|---|---|---|---|---|---|
| 78 (anchor, no new run) | 1 | 360 | 1528 | (170, 764) | 77 | 223 | 1400 | 0.04931 |
| 156 (mandatory) | 2 | 660 | 2480 | (340, 1240) | 169 | 431 | 2706 | 0.01233 |
| 312 (cost-gated) | 4 | 1260 | 4264 | (680, 2132) | 353 | 847 | 5317 | 0.00308 |

Single wavelength, λ=600nm, cpl=20 (matches exp-030 Block 1's own
established convention exactly — the C(156)/C(312) self-similar numbers
this cycle compares against are themselves single-λ 600nm, not the
3λ-V-weighted r=78 anchor). N9 fallback angle set (±35°, ±25°, ±15°, ±5°,
0°) at every r_out — this program's standard, per PANEL.md/T16.

### 2b. Material law — the object under test

```
r_in(r_out)  = r_out − 48            # FIXED absolute thickness, not r_out-scaled
sigma_max     = 0.5                   # FIXED, not rescaled by kappa
eps_max       = 1.0                   # unchanged (no index step — untouched by this proposal)
```

| r_out | r_in (fixed-abs) | thickness (cells) | thickness (λ) | σ_max | τ_shell = σ_max·thickness |
|---|---|---|---|---|---|
| 78 | 30 | 48 | 2.4λ | 0.5 | **24.0** |
| 156 | 108 | 48 | 2.4λ | 0.5 | **24.0** |
| 312 | 264 | 48 | 2.4λ | 0.5 | **24.0** |

Printed-assertion arithmetic (the way exp-030's own module does):

```python
for r in (78, 156, 312):
    r_in = r - 48
    tau  = 0.5 * (r - r_in)
    assert tau == 24.0                      # trivial, but must be asserted, not eyeballed
assert (78 - 48) == 30                      # r=78 coincides EXACTLY with the established
assert 0.5 == 0.5                           #   self-similar r=78 object — see P-0, below
```

**Non-obvious, load-bearing consequence, worth stating explicitly:** this
construction holds `τ_shell = 24.0` constant across the family *by
construction*, identically to the established self-similar family — so
this experiment isolates the **geometric law only** (self-similar
`r_in∝r_out` vs. fixed-absolute `r_in=r_out−48`), not a difference in
total shell optical depth. That confound-control is a byproduct of the
design choice (§3), not something added on top of it. What genuinely
differs between the two families as `r_out` grows is the shell's
thickness **as a fraction of `r_out`** (constant 61.5% self-similar;
61.5%→30.8%→15.4% fixed-absolute) and its thickness **in wavelengths**
(grows 2.4λ→4.8λ→9.6λ self-similar; **constant 2.4λ** fixed-absolute —
the identical, R-gate-validated profile shape reused unchanged at every
scale, never diluted).

### 2c. Source spec

- Wavelength: 600nm (mandatory scope); 450/750nm not run this cycle
  (idealization, §6).
- Angles: N9 fallback, `(-35,-25,-15,-5,0,5,15,25,35)`.
- Scene: ambient incoherent sum (`lab/ambient.py::contrast_from_runs`),
  identical instrument to every other constraint-3 `C` citation in this
  program.

## 3. The design choice: why `sigma_max` is held fixed, not rescaled

Three options were considered:

1. **Rescale `sigma_max(κ)=0.5/κ`** (the self-similar family's own fix,
   holding `τ_shell` constant via a formula) — rejected. That formula's
   entire justification in exp-030 was to make the object's own optical
   depth *not* explode as an artifact of self-similar geometric scaling.
   Reapplying it here, on top of an *already*-fixed absolute thickness,
   would make `τ_shell` grow with `r_out` (σ fixed at growing thickness
   would be the wrong pairing) — not the question this cycle exists to
   ask, and not what a real coating does.
2. **Rescale `sigma_max` to hold some other invariant** (e.g. reflectance)
   — rejected as unmotivated: no realizability argument requires it, and
   it reintroduces exactly the "which invariant licenses which rescaling"
   argument Red Team adjudicated at Iteration 7 for the self-similar
   family. Nothing this cycle needs is served by inventing a new one.
3. **Hold `sigma_max` fixed at 0.5, the literal r=78-gated value**
   (adopted). This is the direct instrument-level statement of MATERIALS'
   own realizability claim: *the same physical coating* (same
   conductivity/doping, same thickness) applied to a larger substrate.
   `sigma_max` is a material property in this bench's convention, not a
   geometry-dependent tuning knob — holding it fixed is what "one real
   material, reused at any size" means as a simulation parameter, exactly
   the standard PANEL.md's latitude rule demands (concrete, testable
   numbers, not a qualitative gesture). The `τ_shell=24.0`-constant
   consequence (§2b) is a discovered property of this choice, not a
   design target — it happens to make the comparison to the self-similar
   family (also `τ_shell=24.0`) unusually clean, which strengthens rather
   than complicates the case for adopting it.

## 4. T1 escape route

**None.** This is a realizability/instrument-construction cycle for
constraint 3's own metric, not a new T1 mechanism candidate — the object
under test is the program's existing passive, LTI, always-on absorber.
It will read as a deep photopic silhouette by construction (the
ESTABLISHED section's own standing caveat), exactly like every other
`graded_black_shell` reading; this cycle does not attempt to clear
VISION's `C_thr` ladder and no PASS/MARGINAL/FAIL language is invoked
against it (unlike the σ(I) OFF-state family, this is a τ_shell=24 opaque
absorber — it is not a near-threshold article and the T2 ladder's
scoring is not the right instrument for it).

## 5. Scope: reused vs. re-verified gates (given, not assumed)

- **R-gate (flat-coating R≤0.2%): RE-VERIFIED, mandatory.** Domain is
  identical to exp-030's own r=156/312, but the *object* differs (thinner
  absolute shell, larger core) — exp-030's own r=156/312 R-gate readings
  (`R_coat` −4.91×10⁻⁵ / +3.51×10⁻⁵, for a *different* σ_max/thickness
  pair) do not transfer and are not cited as evidence here. A fresh
  R-gate check runs at r=156 and (if triggered) r=312 for this
  construction — cheap (~5–20s each, per exp-030's own `rgate` timings).
- **δ_C empty-scene floor and settling diagnostics: NOT re-run, cited by
  inheritance.** Both are properties of the empty domain/geometry
  (`GUARD_OUT`, `NY`, `PLANE_X`, angle set), independent of what fills the
  object window — exp-030's own r=156 floor (−0.001211) and settling
  check (native/doubled C agree to 5 decimals) were measured on this
  identical domain. Flagged explicitly as an inherited assumption, not a
  free pass: if Phase 2 wants it re-verified at near-zero marginal cost
  (the runs are already scheduled for other empty-scene purposes), that
  is a one-line addition, not a redesign.
- **r=78: zero new FDTD calls.** `r_in(78)=78−48=30` and `sigma_max=0.5`
  reproduce the established self-similar r=78 object exactly — this is a
  **code-only identity check** (P-0, below), not a measurement.

## 6. Idealizations (stated honestly)

1. Single λ=600nm — no 3λ sweep this cycle (cost discipline; matches
   Block 1's own established scope, but means no V-weighted comparator
   exists for the new r=156/312 points, only single-λ ones).
2. r=312 is cost-gated, not committed (§7) — if deferred, T14's own
   asymptotic-shape question (needs a 3rd point for any fit) is only
   partially answered by this cycle; the r=78→156 direction test (§8)
   still stands on its own.
3. δ_C floor/settling inheritance (§5) is argued, not re-measured, for
   this cycle's own new object.
4. The T9 σ_abs/σ_ext rim-transmission mechanism is NOT independently
   re-measured for this construction's differing thickness-fraction —
   the THERMO sidecar below reuses the established graded_black_shell
   ratio (0.51) as an analytic input, explicitly flagged as unverified
   for this specific geometry, not a new box-ledger measurement (kept out
   of scope to stay lean, per the cycle's own "decisive not maximal"
   instruction).
5. 2D TMz, single-pass (no multi-sweep dose accumulation), no coherent
   beam-divergence interaction (ambient sum only) — same standing
   idealizations as every other `lab/ambient.py` reading.
6. Engine-trust caveats (VALIDATION.md) apply as usual: FFT-wavelength
   quantization is irrelevant here (this instrument does not extract a
   spatial wavelength); the reflection-monitor-placement lesson is
   already baked into the R-gate's own established near-interface
   convention (reused verbatim); this is a scattered-quantity-adjacent
   but not cross-solver comparison, so the scattered-vs-total lesson does
   not bind; PEC-flush-at-cloak-walls is a cloak-only lesson, not
   applicable (no cloak object here).

## 7. Cost note

Mandatory: 1 R-gate check + 1 ambient block (9 angles) at r=156 — by
direct comparison to exp-030's own r=156 timings (Block 1 ≈1780s/45 runs
≈ 40s/run), estimated **≈6–7 minutes** for 9 angles + gate. r=312,
**cost-gated exactly per exp-030's own precedent**: time one single-angle
pilot first; exp-030's own r=312 leg took 3.87h for 37 runs (the largest
single timing miss in this program's history) — if the pilot extrapolates
to a comparable wall-clock, run it only if budget allows, else defer with
the r=78/156 two-point result reported as the cycle's own committed
finding (not provisional — §8's falsifiable claim is scored on r=78/156
alone).

## 8. Predicted outcomes — falsifiable bands

**P-0 (gate, zero-cost, code-only):** `r_in_fixed(78) == 30` and
`sigma_max_fixed == 0.5` reproduce exp-030's committed r=78 object
exactly (bit-identical `graded_black_shell` call). **Falsified if any
transcription drift changes the r=78 object** — this must hold trivially;
if it doesn't, the whole family is mis-specified.

**P-1 (primary, r=156, mandatory):** `C_fixedabs(156)` at 600nm.
Established self-similar comparators (`experiments/030-scale-bridge/
results.json::fit.absorber`, 600nm-only raw table):
`C_selfsim(78)=−0.7211`, `C_selfsim(156)=−0.730455`,
`C_selfsim(312)=−0.732254`, `C_∞,selfsim≈−0.734`.

Predicted: **`C_fixedabs(156) ∈ [−0.760, −0.735]`** — deeper (more
negative) than `C_selfsim(156)=−0.730455` by at least 0.0046, i.e. the
r=78→156 deepening step is **at least 1.5×** the established self-similar
step (`|ΔC_selfsim(78→156)| = 0.00936`), consistent with §3's mechanism
argument (a fixed-width rim-leak channel becomes a shrinking fraction of
a growing silhouette, unlike the self-similar family whose leak channel
grows with it). **CONFIRMED** if `C_fixedabs(156) ≤ −0.7350`. **PARTIAL**
if `C_fixedabs(156) ∈ (−0.7350, −0.7305]` (deepens, but not by the
predicted margin). **REFUTED** if `C_fixedabs(156) > −0.7305` (deepens
*less* than the self-similar family, or shallows) — this is the
result that would say the fixed-absolute-thickness construction shows
T14's wrong-direction pattern at least as strongly as the self-similar
one, the opposite of this proposal's mechanism claim.

**P-2 (conditional on r=312 running):** `C_fixedabs(312)` continues to
deepen rather than plateau: `C_fixedabs(312) < C_fixedabs(156)` (strictly
more negative) by at least 0.0010 — **CONFIRMED** if true and the implied
2-point (156,312) slope does not itself decelerate toward a sub-`−1`
asymptote as sharply as the self-similar family's own fitted `C_∞≈−0.734`
(i.e., a naive linear extrapolation of the 156→312 step should not
already be flattening at 312). **REFUTED** if `C_fixedabs(312) ≥
C_fixedabs(156)` (flat or reversed) — the same wrong-direction pattern as
T14, undiminished by removing the growing-shell-thickness confound.

**P-3 (T14 verdict, falsifiable either way, as required):** Taking P-1
and P-2 together — **FALSIFIABLE CLAIM:** *the fixed-absolute-thickness
construction does NOT reproduce T14's wrong-direction shallowing at the
same strength as the self-similar family.* This is CONFIRMED if P-1
reads CONFIRMED or PARTIAL (deepens faster than self-similar) and P-2 (if
run) does not REFUTE; it is REFUTED — a genuinely informative, opposite
finding — if P-1 REFUTES, meaning T14's shallowing is a property of the
absorber's near-field/rim-diffraction geometry generally, not an artifact
of the self-similar family's specific growing-thickness confound.

**P-4 (R-gate, mandatory pre-run diagnostic):** `R_coat(156) ≤ 0.002`
(the established 0.2% flat-coating gate), expected comfortably inside
(same profile shape/steepness as the already-gated r=78 object, larger
`r_out` only reduces local curvature). **CONFIRMED** if ≤0.002;
**hard-stop, do not trust P-1** if it fails.

**P-5 (THERMO sidecar, analytic, post-run — expressibility contract per
PANEL.md: not an FDTD output).** Using `lab/thermo_sidecar.py`'s
established-ratio branch with the (flagged-as-unverified-for-this-
geometry, per idealization 4) established `graded_black_shell` σ_abs/σ_ext
ratio of 0.51, the T23-adopted mixed `h_eff` convention (power on `w_on`,
conduction/mass on `r_out`), and this program's own sourced flashlight
irradiance (~6.58×10⁻⁶ W/cm² central, Docket #7): predicted
`ΔT_ss` at r_out=156 remains **UNDETECTABLE** — more than 100× below the
sourced 8.6–100mK microbolometer NETD band, consistent with every prior
sidecar verdict this program has issued (exp-043/044/045). **Falsified**
if the computed `ΔT_ss` closes to within 10× of the NETD band at any
tested `r_out` — would be the first non-UNDETECTABLE sidecar reading in
this program's history and a genuine surprise.

## 9. Realizability note

`dx` at this bench's established 600nm/cpl=20 convention is **30nm**
(`r_out=78` cells ↔ 2.34µm, `REALIZABILITY_MEMO.md` Entry 2 — verified:
2.34µm/78 = 30.0nm exactly; also verified at 450nm/cpl15 and
750nm/cpl25, both 30nm, the same `dx` by this bench's own multi-λ
convention). Fixed absolute thickness = 48 cells:

```
thickness_nm = 48 × 30nm = 1440nm = 1.44 µm
```

**Unlike the self-similar construction — whose absolute thickness grows
with `r_out` and reaches 0.31–0.92 m (UNOBTANIUM, informal call,
Iteration 7/`REALIZABILITY_MEMO.md` Entry 2) at witness scale — this
construction's thickness is 1.44µm by definition at every `r_out` in the
family, including r_out=312 and, in principle, a literal witness-scale
core.** That is the entire point of the fixed-absolute-thickness
construction and this experiment is the first time this program has
measured its optical consequence rather than only its realizability
argument.

Is 1.44µm remotely realistic for a real ultra-black coating? Per
`REALIZABILITY_MEMO.md` Entry 2's own cited precedent (not a fresh
literature search — T18's WebFetch block is still unaddressed):
Vantablack-class CNT-forest coatings run "few-µm to sub-mm thick"; a
separate informal figure in the same memo cites "tens of nm to ~1mm."
**1.44µm sits inside the low end of the cited "few-µm" range and inside
the "tens of nm to 1mm" range** — plausible, not confirmed: this program
has never sourced a primary CNT-forest thickness figure below a few µm,
so 1.44µm is a reasonable extrapolation toward the thin end of a cited
range, not a value with its own direct citation. Stated honestly as
**PLAUSIBLE, not PUBLISHED** (MATERIALS' own three-tier standard) pending
the literature check T18 has blocked for six iterations running.

## 10. Computed-in-code vs. given-as-input

**Given:** `R_FAMILY=(78,156,312)` (156 mandatory, 312 cost-gated);
`ABS_THICKNESS=48`; `SIGMA_MAX_FIXED=0.5`; `EPS_MAX=1.0`; λ=600nm/cpl=20;
N9 angle set; all domain-construction constants reused verbatim from
`experiments/030-scale-bridge/design_geometry.py::geometry()`.

**Computed in code:** `r_in(r) = r − 48` per r; `τ_shell` per r (printed
assertion); the R-gate reflectance at each new r; the ambient contrast
`C_fixedabs(r)` at 156 (and 312 if triggered); the deepening deltas
against `experiments/030-scale-bridge/results.json`'s own committed
600nm-only established figures; the THERMO sidecar `ΔT_ss`/NETD
disposition; `thickness_nm = 48 × dx_nm` at all 3λ (verified equal).
