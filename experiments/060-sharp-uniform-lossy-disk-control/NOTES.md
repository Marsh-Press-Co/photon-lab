# exp-060 — Panel Iteration 37: The Sharp-Uniformly-Lossy-Disk FDTD Control

**Lead: MATERIALS & METAMATERIALS** (rotation). Runner: cloud panel shift,
2026-08-22. Full five-phase panel cycle recorded verbatim in
`LOGBOOK.md` Iteration 37; this file carries the experiment-local record
(setup, predictions, results).

## Why this cycle

exp-059 (Iteration 36) measured the flagship absorber's `Q_ext=1.5385`
at 72.6% of the exact PEC-sharp-edge reference `Q_ext_PEC(24.5044)
=2.1177`. That comparison cannot separate two undisentangled mechanisms
(MATERIALS' own Phase-2 critique at Iteration 36, independently echoed by
five of six seats at Phase 5, MF-5): (a) the graded shell's C²-smooth,
adiabatic conductivity onset genuinely suppressing edge diffraction
beyond bulk absorption alone, versus (b) any sufficiently lossy disk,
sharp-edged or not, damping the PEC resonance ripple by bulk loss alone.
Iteration 36's own Phase-5 reconciliation ranked this the #1 priority for
Iteration 37 — a rare six-way seat convergence, five of six ranking it #1.

## Hypothesis

Holding the shell's total optical depth fixed (matched to the graded
shell's own line-integral) and removing ONLY the grading — replacing the
smooth quintic² profile with a spatially uniform, sharp-edged
conductivity over the identical annulus — measurably raises `Q_ext`,
back-scatter, and forward-concentrated excess scattering relative to the
graded article, because the sharp entry discontinuity reintroduces edge
diffraction/reflection the graded profile was built to eliminate.
Committed direction: **UNIFORM SUPPRESSES LESS than GRADED** (the
opposite outcome — uniform tracking graded closely — would mean bulk
loss alone explains the flagship's suppression and grading does little
separable work, a real finding against the founding phenomenon's own
"no bright reflection" design claim).

## Setup

Two new articles, exp-002/020's exact domain/geometry/source/box
convention (bit-identical, no deviation):

| Knob | Value |
|---|---|
| Domain | N=560×560 cells, ABSORB=40, courant_frac=0.32, STEPS=3200 |
| λ / cpl | 600nm / 20 (dx=30nm) — single wavelength, the point exp-059 anchored |
| Object center | CX=252, CY=280 |
| PEC core | `pec_disk(R_CORE=30)` — identical in both articles |
| Shell | r_in=30, r_out=`R_COAT`=78 (thickness 48 cells) |
| Source | boresight line source, SRC_X=64 (normal incidence) |
| Boxes | BOX_A=(142,362,170,390), BOX_B=(117,387,145,415) — exp-002 verbatim |
| Reference | REF=(CX,CY,60) |

**"graded"**: `materials.graded_black_shell(R_CORE, R_COAT, sigma_max=0.5)`
— reproduces `experiments/002-cross-sections/results.json::absorber-600`
EXACTLY (regression anchor for this cycle's own harness, checked in
`run.py::main()` before the new article is trusted).

**"uniform"**: new builder `materials.uniform_lossy_shell(R_CORE, R_COAT,
sigma_flat)` — sharp Heaviside window, `sigma_e += sigma_flat`,
`eps_r = 1.0` (no index step, matching `graded_black_shell`'s own
default so only σ(r)'s SHAPE differs).

### sigma_flat derivation (matched optical depth)

`graded_black_shell`'s profile: `sigma(r) = sigma_max * s(d(r))^2`,
quintic smoothstep `s(d)=6d⁵−15d⁴+10d³`, `d=clip((r_out−r)/(r_out−r_in),
0,1)`. Matching convention: equal radial line-integral of σ across the
shell (`∫ sigma dr` equal between the two profiles) —

```
integral_0^1 s(d)^2 dd = 181/462  (exact, term-by-term polynomial integration
                                    of s(d)^2 = 36d^10-180d^9+345d^8-300d^7+100d^6)
sigma_flat = sigma_max * (181/462) = 0.5 * 0.3917748917748918
           = 0.1958874458874459
tau_matched = sigma_flat * (r_out - r_in) = 9.402597402597403
```

**CAVEAT, propagated to every site this number is used (Iteration-37 Red
Team mandatory fix 5, closing VISION SCIENCE's Phase-2 caveat-placement
catch — the exact defect pattern that fired Checkpoint criterion 4 one
cycle ago, at Iteration 36):** this is ONE disclosed convention among
possible others (a peak-σ-matched or transmission-matched convention
would yield a different `sigma_flat`). More load-bearing: matching the
RAW conductivity line-integral does **NOT** match true field-attenuation
depth once loss is order-unity. `Im(n(sigma))` is concave in σ at this
bench's own grid normalization (physical loss tangent
`t = sigma_e * cpl / (2*pi)`, corrected from ELECTROMAGNETISM's first
Phase-2 attempt which divided by `sim.omega` — the per-step phase
advance, not the physical angular frequency — and was off by a factor of
`1/S≈4.42`; Red Team's Phase-2 audit independently re-derived and
confirmed the correction). By Jensen's inequality, the graded profile's
TRUE attenuation-weighted depth
(`integral_0^1 Im(n(sigma_graded(d))) dd = 0.273840`) sits **~8.3% below**
the flat profile's uniform value (`Im(n(sigma_flat))=0.298721`) despite
identical raw line integrals by construction (QUANTUM OPTICS' Phase-2
finding, independently re-derived and confirmed exact by Red Team; pinned
as trust-suite **stage 22 gate 4**'s regression anchor,
`gap=8.326%±0.05%`). **This residual is real, known, and disclosed — not
a code bug and not grounds to redefine `sigma_flat` this cycle** (Red
Team's Phase-2 ruling: redefining now would invalidate every other seat's
already-cross-checked arithmetic and force a second EM Fresnel
recomputation; disclosure, not redefinition, is this cycle's chosen path).
**Correction (QUANTUM OPTICS' Phase-5 catch, Red-Team-confirmed — this
paragraph originally got the bias's DIRECTION backwards):** since
`b_flat > I_graded` at the current `sigma_flat`, a true attenuation-match
would require LOWERING `sigma_flat` (to `t'≈0.566`, not raising it),
which via Learned #2's own Fresnel mechanism (below) would LOWER, not
raise, the entry reflectance/`back_frac` — the properly-matched
comparison would plausibly show a SMALLER back_frac gap than measured
here, not a bigger one. This does not threaten the headline: even a
generous 15–20% multiplicative correction on `back_frac_uniform` leaves
a >4000× gap vs. graded, still decisive, since the dominant mechanism is
a structural discontinuity, not a magnitude effect a convention tweak
could erase. (The Q_ext-based P-1/P-2/P-3 channel is unaffected either
way — that miss was already scored as directionally right with
over-tight bands, not a claim resting on this bias's sign.)

### New trust-suite stage 22 (`lab/validation/run_all.py`)

Four gates, all green pre-run (`python3 lab/validation/run_all.py --only
22` → 7/7; full bench `--only 12346789,10,11,18,19,20,21,22` → 74/74):
(1) write-identity (absolute, machine precision); (2) optical-depth
line-integral-match — an **implementation-fidelity** check (relabeled per
Red Team's mandatory fix 6: it certifies the code implements the chosen
convention correctly, NOT that the convention matches true attenuation —
see caveat above), tolerance widened to ≤1.0% after verifying the
~0.56% residual at this exact 48-cell thickness is a genuine, stable,
explainable discrete-grid effect (the 49-point circular-mask sum
straddling both shell endpoints), not a code defect; (3)
energy-conservation cross-check reusing stage 8's own box-independence/
extinction-agreement identities (≤0.12 both); (4) the attenuation-depth
disclosure gate above.

## Panel record (full verbatim record: `LOGBOOK.md` Iteration 37)

**Phase 1 (MATERIALS, fresh sub-agent):** proposed this control, the
`uniform_lossy_shell` builder, the τ-matching derivation, and the
original prediction bands P-1 through P-7 below.

**Phase 2 — five blind critiques, all support-with-changes, zero
opposes:**
- **PHOTONICS**: verified all arithmetic exactly; sharpest attack — every
  committed instrument (Q_ext, box_dev, back_frac, abs_frac) is
  angle-integrated/near-backward-only, but the proposal's causal claim is
  specifically about EDGE diffraction; `lab/sections.py::
  angular_scattered_pattern` already exists (exp-016/017, zero marginal
  FDTD cost) and would let the run actually attribute excess scattering
  to shape (edge/grazing-concentrated) vs magnitude (diffuse). **Accepted
  as mandatory fix 1.**
- **ELECTROMAGNETISM**: sharpest attack — computed the actual planar
  Fresnel power reflectance at `sigma_flat`, got R≈16.7% (via
  `t=sigma_flat/sim.omega`), ~80× the proposal's own P-4 upper bound;
  argued the direction (P-4 under-calibrated) is right but the specific
  numbers are likely off by 1-2 orders of magnitude. **Direction
  accepted; EM's own specific number found WRONG by Red Team** (see
  below) — a units error (divided by the per-step phase advance, not the
  physical angular frequency, missing a factor of `1/S≈4.42`).
- **THERMODYNAMICS**: sharpest attack — the proposal measures two new
  real-FDTD articles but never routes either through the energy sidecar,
  violating PANEL.md's "every run" requirement; direct Iteration-35
  precedent where Red Team ruled the identical omission escalates toward
  OPPOSE. **Accepted as mandatory fix 3** (P-8 below).
- **QUANTUM OPTICS**: sharpest attack, with independent calculation —
  "matched optical depth" via raw `∫σdr` silently assumes linear
  attenuation, false once loss is order-unity; Jensen's-inequality
  argument (concave `Im(n(sigma))`) shows the two profiles are NOT
  actually attenuation-matched, ~8-9% residual. **Confirmed exact by Red
  Team; accepted as mandatory fix 4** (stage 22 gate 4, above).
- **VISION SCIENCE**: sharpest attack — the "matched optical depth is one
  convention among alternatives" disclosure appeared exactly once, in
  Idealizations, bare everywhere the number was actually used (the
  τ derivation, the P-1–P-3 bands, the committed-direction reasoning) —
  the exact caveat-placement pattern that fired Checkpoint criterion 4 one
  cycle earlier. **Accepted as mandatory fix 5** (propagated above and in
  Idealizations below).

**Red Team's Phase-2 audit — PROCEED-WITH-MANDATORY-FIXES, 6-item
docket, all accepted:**
1. Add `angular_scattered_pattern` for both articles + a falsifiable band
   on excess-scattering concentration (PHOTONICS).
2. **Correct EM's own Fresnel-reflectance number before adopting it**:
   independently re-derived from source (`lab/fdtd2d.py`'s `alpha=
   sigma_e*S/(2*eps_r)` discretizes the continuous term `σΔt/(2ε)` with
   `Δt=S`, so `sigma_e` is calibrated against the PHYSICAL angular
   frequency `omega_phys=2π/cpl`, not `sim.omega=2π·S/cpl` — EM's
   original calculation used the latter, a units error off by `1/S`).
   Corrected: `t=0.6235` (independently cross-validated — this is
   EXACTLY QUANTUM's own `t=0.624` input, arrived at via a completely
   different route), `R≈2.14%` power reflectance — real, ~10.7× the
   graded shell's own ≤0.2% coated-wall ceiling and ~4.3× the original
   P-4 upper bound, but nowhere near EM's own reported 16.7%. **P-4
   rebanded around the CORRECTED anchor, not EM's number** (below).
3. Add the P-8 THERMO sidecar row (THERMODYNAMICS).
4. Add the attenuation-depth disclosure gate (QUANTUM OPTICS), keeping
   `sigma_flat` as originally derived rather than redefining it this
   cycle (Red Team's own scope-discipline ruling, avoiding a
   recomputation cascade that would invalidate every other seat's
   already-cross-checked arithmetic).
5. Propagate the convention-dependence caveat (plus the new ~8.3%
   residual) to every site `sigma_flat`/"matched" language appears, not
   Idealizations alone (VISION SCIENCE).
6. Relabel stage-22 gate 2 as an implementation-fidelity gate, not a
   physics-matching gate.

**Red Team's explicit ruling on Checkpoint criterion 4**: the
caveat-placement pattern DID recur in this cycle's own Phase-1 draft
(confirmed), but does **NOT** fire — Iteration 35's binding tripwire
language concerns a pattern surviving into a PUBLISHED, closing,
git-tracked claim; this was caught at Phase 2, before Phase 3 synthesis,
matching the program's own precedent (Iteration 36's own MF-3 origin, not
its later Phase-5 firing). **Hardened tripwire set**: any recurrence
surviving into THIS cycle's own published Phase-3/Phase-5 artifact fires
Checkpoint-4 automatically, no further deliberation — the propagation
above is written to close that exposure now, not to be revisited later.
**All five Checkpoint criteria**: none fire (full reasoning in
`LOGBOOK.md` Iteration 37).

**Red Team's own new finding** (recommended, not mandatory this cycle,
scope discipline per Iteration 36's own MF-5-override precedent): a
closed-form two-region (PEC core + uniform complex-ε annulus)
Bessel/Hankel series would give an exact, zero-FDTD reference for
`Q_ext_uniform` — real new machinery, queued for Iteration 38+, not
built here.

**Phase 3 — Director's synthesis**: all six mandatory fixes ACCEPTED, in
full — none overridden. New machinery (`uniform_lossy_shell`, trust-suite
stage 22) committed (`d5b4844`) before this predictions file. Predictions
below commit BEFORE the official `run.py` execution (house discipline).

## T1 escape route

**NONE.** Sidecar/validation work bounding an existing assumption
(disentangling the mechanistic SOURCE of the flagship's measured Q_ext
suppression), same category as exp-059. No beam-termination, backscatter,
ambient-appearance, or switching claim is scored this cycle.

## Predictions (committed before the official run)

| # | Quantity | Predicted band | Note |
|---|---|---|---|
| P-1 | `Q_ext_uniform` (measured, x=24.5044) | **[1.65, 2.00]**, central ~1.85 | vs. exact PEC ceiling 2.1177 and graded's measured 1.5385 |
| P-2 | `ratio_uniform / Q_ext_PEC(24.5044)` | **[0.78, 0.94]** | HIGHER than graded's own 72.6% |
| P-3 | `ratio_uniform / Q_ext_measured_graded(1.5385)` | **[1.07, 1.30]** | UNIFORM SUPPRESSES LESS than GRADED — the committed direction |
| P-4 | `back_frac_uniform` | **[3×10⁻³, 5×10⁻²]** | **REBANDED at Phase 3** around Red Team's corrected Fresnel anchor R≈2.14% (not EM's own miscalculated 16.7%, and not the original Phase-1 band [1×10⁻⁴,5×10⁻³], both wrong); still far above graded's near-null 2.08×10⁻⁶ |
| P-5 | `abs_frac` (`sigma_abs/sigma_ext`) | **[0.45, 0.58]** | comparable to graded's 0.512 — the least-differentiating channel |
| P-6 | `box_dev`, both articles | **≤ 0.01** | matches exp-002's own ~0.002-0.003 at this geometry |
| P-7 | Stage-22 gates | all 4 PASS | **already confirmed green pre-run** (generic machinery validation, independent of this experiment's own measured numbers) |
| P-8 | `margin_uniform` (NETD-lo/ΔT, THERMO sidecar) | **[350×, 700×]** | derived analytically from the P-1/P-5 boxes' own corners (see `run.py`); classification **UNDETECTABLE** at every corner — 2+ orders of magnitude clear either way, no scored classification change |
| P-9 | angular-pattern sum-identity, both articles | **≤ 0.5%** relative | implementation self-consistency (`sum(pattern)==sigma_scat`), not an independent physics check — verified before the shape claim (P-10) is trusted |
| P-10 | excess-scattering forward-cone fraction (`\|θ\|>150°`) | **≥ 0.50** | committed direction: the uniform article's excess scattering (vs graded) concentrates in the forward/grazing diffraction lobe, consistent with an edge-diffraction origin rather than a diffuse bulk-loss-only difference |

**Falsification, pre-registered:** P-3's direction failing (ratio ≤1.0,
i.e. uniform suppresses AS MUCH OR MORE than graded) would refute the
edge-grading-specific mechanism and instead support "bulk loss alone
explains the suppression" — a real finding against the flagship's own
design claim, stated as such regardless of which way it lands. P-10
failing (forward-cone fraction <0.5, i.e. excess spreads diffusely
rather than concentrating near the diffraction lobe) would weaken the
edge-attribution even if P-1–P-3 confirm on magnitude alone. Any gate
failing under the official `run_all.py --only 22` execution despite
passing during this shift's own informal verification would indicate a
regression, and would block Phase-5 review until root-caused (exp-059's
own precedent).

## Idealizations

2D, TM_z, normal incidence only (boresight beam, exp-001/002/059
convention) — NOT the multi-angle ambient instrument; no constraint-2/3/4
quantity is scored this cycle. Single λ=600nm/cpl=20 only — 450/750nm
explicitly out of scope (a separate, already-queued Iteration-37+ rider).
**"Matched optical depth" (equal `∫σdr`) is ONE disclosed convention
among possible others, and does NOT match true field-attenuation depth
once loss is order-unity — a real, disclosed ~8.3% residual (see
derivation above; this caveat is intentionally repeated here per the
Iteration-37 mandatory-fix propagation requirement, not an oversight).**
Both articles keep `eps_r≡1.0` throughout — isolates σ(r)'s SHAPE as the
single varied mechanism; a genuine permittivity discontinuity is not
tested and would plausibly show an even larger reflection/edge effect
than P-4's band. PEC-core presence/geometry (r_in=30) held identical in
both articles — T9 (Iteration 4, exp-027) already established PEC-core-
vs-rim-fill is incidental to the aggregate absorption ratio at this exact
geometry, not re-litigated here. `angular_scattered_pattern`'s own
idealization carries forward unchanged: a square-path angular sample, not
a true circular far-field pattern (consistent with `sigma_scat`'s own
near-to-mid-field box convention). This item does NOT resolve the
separate, still-open `iso_xsec_sq` area-convention question and does NOT
change any existing scored thermal-margin classification (P-8 is a NEW
measurement, not a revision of the flagship's own established 699.27×/
369×/1655× figures). Zero new engine physics (a `sigma_e`-array write on
the existing solver path, same class as `graded_black_shell`/
`absorber_shell_stub`).

## Results

Official run: 2.5 min, 3 FDTD calls (empty/graded/uniform). Full data:
`results.json`.

**Regression anchor holds to machine precision**: `graded` reproduces
`experiments/002-cross-sections/results.json::absorber-600` exactly
(`dQ_ext=4.4e-16`, `dback_frac=5.2e-19`, `dabs_frac=1.1e-16`) — this
cycle's own harness is trustworthy before the new `uniform` article is
read.

| # | Quantity | Predicted | Measured | Verdict |
|---|---|---|---|---|
| P-1 | `Q_ext_uniform` | [1.65, 2.00] | **2.0193** | **MISSED (narrow, +0.97% over the upper bound)** |
| P-2 | `ratio_uniform/Q_ext_PEC` | [0.78, 0.94] | **0.9535** | **MISSED (narrow, +1.4% over)** |
| P-3 | `ratio_uniform/Q_ext_graded` | [1.07, 1.30] | **1.3125** | **MISSED (narrow, +0.96% over)** |
| P-4 | `back_frac_uniform` | [3×10⁻³, 5×10⁻²] | **0.01156** | **CONFIRMED** |
| P-5 | `abs_frac` | [0.45, 0.58] | **0.4686** | **CONFIRMED** |
| P-6 | `box_dev`, both | ≤0.01 | graded 0.0019, uniform 0.0004 | **CONFIRMED** |
| P-7 | Stage-22 gates | all 4 PASS | 4/4 PASS (pre-run) | **CONFIRMED** |
| P-8 | `margin_uniform` | [350×, 700×] | **441.79×**, UNDETECTABLE | **CONFIRMED** |
| P-9 | angular sum-identity | ≤0.5% | **0.0000%** both | **CONFIRMED** |
| P-10 | excess forward-cone fraction | ≥0.50 | **0.0212** (forward); **0.5028** (backward) | **REFUTED — direction reversed** |

**The committed DIRECTION (UNIFORM SUPPRESSES LESS THAN GRADED) is
confirmed decisively** — `Q_ext_uniform=2.0193` sits at 95.4% of the exact
PEC ceiling (`Q_ext_PEC=2.1177`) vs graded's 72.6%, and `back_frac_uniform
=0.01156` is **5547× graded's near-null 2.08×10⁻⁶** — but P-1/P-2/P-3's
specific numeric bands were all narrowly missed on the high side (0.96–
1.4% over their own upper edges). The bands were too tight, not wrong in
kind: the physics call (less suppression, more like the PEC reference)
was right; the precision claimed for it wasn't warranted by the Phase-1/2
reasoning behind those three bands specifically (unlike P-4, which Red
Team's own corrected Fresnel-reflectance recalculation anchored
correctly, and which landed inside its rebanded window with room to
spare).

**P-10 REFUTED, and informatively so.** The uniform article's excess
scattering (relative to graded) concentrates overwhelmingly **BACKWARD**
(50.3% of total excess within 30° of the exact backward/source direction)
and almost NOT AT ALL in the predicted forward/grazing diffraction cone
(2.1%). On reflection this is exactly what Red Team's own corrected
mechanism — a genuine planar Fresnel reflectance at the sharp σ-step
entry (R≈2.14%, cross-validated by QUANTUM's independent loss-tangent
calculation) — predicts: a reflectance is by definition a **backward-
going, near-specular** quantity at a planar interface, not a
forward-peaked diffraction lobe. PHOTONICS' own Phase-2 framing ("edge
diffraction/grazing-incidence") was the wrong lens; EM's ("Fresnel
reflectance at the entry discontinuity") was the right one, and this
angular measurement is the first direct confirmation of THAT mechanism,
not the diffraction-lobe one originally proposed alongside it.

**Thermal sidecar**: both articles comfortably UNDETECTABLE, both inside
their pre-committed corners — `graded` margin=696.81× (matches the
established 699.27× figure closely; **correction, THERMODYNAMICS'
Phase-5 catch, Red-Team-confirmed: the ~0.35% gap is NOT `irr_central`'s
back-derivation rounding** — `run.py::main()`'s own regression assertion
pins `irr_central`'s back-derivation to `_ESTABLISHED_P_ABS_W` bit-exact,
zero tolerance, disproving that. **The real cause is exp-057's own
2-sig-fig hardcoded `RATIO_ABS_EXT=0.51`** vs. this cycle's full-precision
measured `abs_frac=0.5118033079980888` — the ratio of the two `p_abs_w`
values (1.0035359) matches `0.5118033/0.51` (also 1.0035359) to 7
significant figures. Non-load-bearing either way) and `uniform`
margin=441.79×, squarely inside P-8's [350×,700×] band. No scored
thermal-margin classification changes.

## Learned

1. **The mechanism question this cycle set out to answer has a real
   answer, not a null result**: edge grading does separable, measurable
   work beyond bulk loss alone — a sharp-edged disk of IDENTICAL total
   optical depth suppresses substantially less (Q_ext ~31.3% higher
   [2.0193/1.5385=1.3125, corrected from an original "30.7%" arithmetic
   slip, VISION SCIENCE's Phase-5 catch], back-scatter 5547× higher) than
   the graded shell. `graded_black_shell`'s
   own design claim ("the adiabatic entry is what kills the reflection")
   is now measurement-backed, not just asserted, for the first time.
   MATERIALS' own exp-059 Phase-2 concern (bulk loss alone might explain
   everything) is REFUTED for this geometry/optical-depth regime.
2. **The mechanism is Fresnel reflectance at a sharp discontinuity, not
   edge/grazing diffraction** — the angular data (P-10) discriminates
   between the two hypotheses proposed alongside each other at Phase 2
   and comes down clearly on EM's corrected-Fresnel side, not PHOTONICS'
   diffraction-lobe side. A useful correction for how this program frames
   "edge effects" in future cycles: a sharp conductivity step is a real
   material discontinuity with an ordinary planar reflectance, not a
   diffraction phenomenon per se.
3. **Pre-registered numeric bands can get the direction right and the
   precision wrong** — P-1/P-2/P-3 all missed narrowly (<1.5% over their
   own edges) while committing correctly to direction and to the ballpark.
   Worth naming as a pattern for future Phase-1 drafts: a band's width
   should reflect the actual uncertainty in the REASONING behind it, not
   just match the format of a well-anchored band like P-4's (which had a
   real quantitative anchor — the corrected Fresnel calculation — that
   P-1/P-2/P-3 never had; their bands were closer to informed guesses
   dressed as calibrated predictions).
4. Red Team's Phase-2 correction of EM's own Fresnel-reflectance
   calculation (16.7%→2.14%, a ~7.8× fix) is **directionally corroborated,
   not independently confirmed,** by this run (corrected, PHOTONICS' and
   ELECTROMAGNETISM's independently-convergent Phase-5 catch — the
   original wording here overclaimed): the measured
   `back_frac_uniform=0.01156` (1.16%) rules out EM's original,
   uncorrected 16.7% figure as clearly too large, but `back_frac` is
   `sections.widths`' `p_back/p_scat` — normalized against **scattered**
   power, not against **incident** power the way a planar Fresnel R is.
   The numeric proximity to 2.14% is a coincidence of this size regime
   (`Q_sca_uniform` sits near 1), not a generic identity between the two
   quantities. Renormalizing to incident power (EM's own Phase-5 figure)
   gives ~1.24%, still not precision-matching 2.14% — real evidence of
   the right mechanism *class*, not of the specific number.
5. This cycle's `sigma_flat` convention caveat (raw line-integral, not
   true attenuation-depth match, ~8.3% disclosed residual) stayed
   non-load-bearing: the measured effect (~31.3%/5547×) is far larger
   than the ~8.3% matching uncertainty could plausibly explain, so the
   headline finding does not hinge on which matching convention was used
   (see the corrected bias-direction discussion in the sigma_flat
   derivation section above — QUANTUM OPTICS' Phase-5 catch — the
   residual, correctly signed, would if anything SHRINK the measured gap
   slightly, not inflate it, reinforcing rather than undermining this
   point).

## Phase 5 outcome

Six fresh blind seats + Red Team audit. **5 PROMISING (PHOTONICS,
ELECTROMAGNETISM, MATERIALS, THERMODYNAMICS, QUANTUM OPTICS), 1 PARTIAL
(VISION SCIENCE)** — but all six independently re-derived and confirmed
every headline number byte-identical; nobody disputed the physics or the
committed direction (uniform suppresses less than graded).

Five real, independently-found defects, all confirmed by Red Team and
fixed same-shift above: PHOTONICS + ELECTROMAGNETISM (convergent) —
Learned #4's back_frac-vs-Fresnel-R "confirmation" overclaimed precision
(different normalizations); THERMODYNAMICS — the ~0.35% graded-margin
gap was mis-attributed to `irr_central` rounding when the real cause is
exp-057's own rounded `RATIO_ABS_EXT=0.51`; QUANTUM OPTICS — Learned #5's
`sigma_flat`-bias-direction claim was backwards; VISION SCIENCE — the
"30.7%" figure was an arithmetic slip (correct: ~31.3%), AND —
**load-bearing** — `lab/validation/run_all.py::stage22_uniform_lossy_shell`'s
own docstring, the single most permanent, git-tracked, every-run site
describing this control's purpose, still stated the pre-run "diffraction"
framing with zero pointer to this cycle's own P-10 refutation of it.

**Red Team's ruling: Checkpoint criterion 4 FIRES** — VISION's
docstring finding is a third consecutive-cycle recurrence of the
caveat-placement/propagation defect class (Iteration 35 → 36 → 37), the
identical failure shape as Iteration 36's own firing (a scoped
propagation promise, here NOTES.md's own original Next item 1, that
named specific sites and missed the more load-bearing one) — one
mitigating difference noted (this cycle's promise did not falsely claim
completion, unlike Iteration 36's MF-3), which lowers severity but does
not change the firing per the hardened tripwire Iteration 37's own
Phase-2 set ("no further deliberation required"). **Overriding the raw
5-1 PROMISING count to PARTIAL, provisional-to-PROMISING** — not on
physics (unchallenged by any seat) but because five real defects,
including a third consecutive recurrence of this program's own
worst-known process failure mode, is closer to Iteration 36's own
disposition than to a clean same-shift-fixable PROMISING (Red Team's own
reasoning, full text in LOGBOOK.md Iteration 37). **All five mandatory
fixes applied and shown inline above, same shift** (the `run_all.py`
docstring fix; the "30.7%"→"~31.3%" correction, two sites; Learned #4's
softened/corrected wording; the Results-section thermo-margin
re-attribution; the sigma_flat bias-direction correction). Full bench
re-verified green after (see SESSION_LOG.md/LOGBOOK.md for the exact
`--only` invocation and count).

**All five Checkpoint criteria, explicit**: criteria 1/2/3/5 do NOT fire
(no constraint metric scored; not a proven-boundary finding; zero new
engine physics; Iterations 36 and 37 both delivered genuine advancing
results). **Criterion 4 FIRES**, per above.

**CHECKPOINT.** Per PANEL.md's procedure: Marsh is notified. Per
Iterations 17/36's own direct, twice-established precedent, this is a
**notification, not a pause** — the mandatory-fix docket landed same-shift
(above) and Red Team's own explicit ruling is that Iteration 38's queue
proceeds unblocked. This CHECKPOINT entry is mirrored in LOGBOOK.md and
SESSION_LOG.md.

**Verdict: PARTIAL** (provisional-to-PROMISING per Red Team's own stated
path, now that the five-item docket has landed and been re-verified this
shift).

## Next

**Red Team's final ranked priorities for Iteration 38+** (reconciling all
six seats' proposals):
1. **[DONE, this shift]** The five-item mandatory-fix docket above.
2. **Build the mechanical caveat-propagation-check tool — now MANDATORY,
   zero-cost rider, Iteration 38, regardless of lead seat.** Carried as
   Iteration 37's own #3 priority and still not built this cycle (hand
   review missed the `run_all.py` site again, per the Checkpoint-4 finding
   above) — a fourth deferral of the one tool built specifically to catch
   this exact defect class would itself be a criterion-4-adjacent finding
   (Red Team's own words).
3. **MATERIALS' absorptivity/mechanism literature check — LOCKED,
   unconditional, Iteration 38.** Now EIGHT cycles deferred (Iteration
   29→37), exceeding every prior unconditional-lock threshold this
   program has ever applied (`h_eff` fired at 5; `graded_black_shell_
   flagship` and `Q_ext(x)` both fired at 3) — granted by Red Team using
   the identical escalation logic applied at Iteration 34, and sharpened
   by this cycle's own finding (MATERIALS' own Phase-5 review: the
   measured mechanism effect makes the flagship's design-claim
   realizability MORE consequential, not less).
4. **The closed-form two-region (PEC core + uniform complex-ε annulus)
   Bessel/Hankel `Q_ext_uniform` series** — four-seat convergence
   (PHOTONICS/MATERIALS/VISION/QUANTUM), zero-FDTD, the same
   non-tautological external-validation role MF-6 played at exp-059.
5. **The partial-grading dose-response curve** — four-seat convergence
   (MATERIALS/EM/QUANTUM/VISION): sweep grading length within the fixed
   48-cell/τ-matched shell, turning this cycle's two-point comparison
   into a real interpolation.
6. **QUANTUM's own item**: a genuinely attenuation-matched third
   `uniform` article (`t'≈0.566`) as a measured FDTD check on the
   corrected bias-direction claim (mandatory fix 5 above) — turns an
   analytic correction into an empirical one.
7. PHOTONICS' 3-λ sweep / T26 λ-angle generalization, paired with
   `graded_black_shell_flagship`'s own 450/750nm sweep (PHOTONICS +
   MATERIALS) — zero-new-FDTD closed-form extensions once item 4 lands.
8. EM's TE_z companion series for `qext_theory.py` — mechanical,
   resolves the still-open Hankel-choice documentation gap.
9. Carried backlog, lower urgency, unblocked: shell-vs-solid thermal-mass
   parameterization (open since Iteration 22/T23, now a fourth-
   consecutive-cycle-plus item); R3-on-loaded-legs for
   `off_pass_joint`/`off_bracket_joint`; a Geary-Hinkley tail-shape model
   of `C(δ)`; P-VIS-5's angle-quantization sensitivity formula; QUANTUM's
   convergence-guard audit pass for the "exact-threshold-from-a-wide-
   bracket" pattern across `lab/`'s other closed-form modules;
   `coupled_segment_general`'s trust-suite promotion. The exp-057 erratum
   fix is DONE (Iteration 37 rider, commit `d9ed12b`).
