# exp-102 — The Coherent, Phase-Resolved Downstream Point-Intensity Instrument

**Panel Iteration 79. Lead seat (rotation): PHOTONICS. Director: Clyde
(photonlab-shift, cloud panel shift).** Reconciled Iteration-79 queue, item
1 (Red Team's own top ranking, exp-101 close). Instrument build, diagnostic
only — T1: N/A, zero `lab/` diff, no mechanism proposed or varied.

Full record: `phase1_proposal.md` (PHOTONICS), `phase2_critique_
{materials,em,thermodynamics,quantum,vision}.md` (five blind critiques, all
support-with-changes), `phase2_redteam_audit.md` (9 numbered attacks, 7
mandatory fixes, 2 checked-and-cleared, PROCEED-WITH-MANDATORY-FIXES, 0
overridden).

## Hypothesis

exp-101 found that `sigma_scat_downstream` (a closed-box Poynting-flux
partition) is interpretable but structurally cannot answer constraint 1's
witness question ("does the background stay lit behind the object?") — a
power integral discards the field's phase, and the extinction paradox
guarantees a large forward-scattered cross-section accompanies any real
shadow, so a large reading is the expected companion of "dark," not
evidence against it. Hypothesis: reading the already-gated complex Ez/Hx/Hy
phasors (`lab/sections.py::full_capture`/`phasors`, trust-suite stage 8) at
a small region on the beam's own rotating downstream axis, and comparing
the empty-scene and article-scene captures coherently at the same point
(same launch phase), produces a genuine same-point field-intensity ratio
that is immune by construction to both defects exp-101's own Phase-5 layer
found in the box-flux family: the `i_inc`/cosθ commensurability artifact
(never invoked — no `sc.widths()` call) and fixed-lab-frame registration
(the point rotates with incidence angle).

## Setup

- **Article**: unchanged, byte-identical R4 family (exp-094–101) —
  `pec_disk`(r=`PEC_R_R4`=60) + `graded_black_shell`(r_in=60,
  r_out=`R4_R_OUT`=156, `sigma_max=SIGMA_R4_CORRECTED`=0.25),
  `R4_CONFIGS["C40_R4"]`/`["G40_R4"]`, 600nm, `cells_per_lambda`=40,
  oblique plane-line source (`profile="plane"`, `edge=R4_TAPER`=80,
  `STEPS=R4_STEPS`=5600). MATERIALS independently re-verified this cycle:
  shell thickness and outer radius are identical in physical units to the
  native flagship article (`96·15nm = 48·30nm = 1440nm` shell,
  `156·15nm = 78·30nm = 2340nm` outer radius) — Gate B (below) is a
  same-article reproduction check, not a rescaled one.
- **Angles**: the same 6 established, pool-wide-largest-magnitude R4-family
  angles exp-101 used: `[37.127246, 38.590230, 39.200000, 40.265420,
  41.460901, 42.960901]`.
- **The new instrument**: beam-aligned unit vectors, taken verbatim from
  `lab/fdtd2d.py::add_line_source`'s own documented launch convention
  (`u(θ)=(-cosθ,sinθ)` propagation, `v(θ)=(sinθ,cosθ)` perpendicular,
  confirmed orthonormal). Primary witness point `P(θ) = round(obj +
  D_STANDOFF·u(θ))`, `D_STANDOFF=200` cells. `H_REGION`=10-cell half-width
  nearest-cell block mean of `|E|²`, reported alongside the single-
  nearest-cell reading. Both legs (`with_article=False/True`) launch with
  bit-identical `add_line_source` parameters (same `angle_deg`,
  `ramp_periods`, `rel_phase=0`), so `phasors()` returns each run's own
  complex fields referenced to the same time origin — the coherent-
  comparison precondition `sections.py`'s own docstring already requires
  of `widths()`, verified by EM's Phase-2 critique against the real code
  rather than assumed.
- **Primary witness metric** (same-point coherent intensity ratio,
  dimensionless, immune to `i_inc`/cosθ by construction — it never calls
  `sc.widths()`): `κ(θ) = mean_block |Ez_article|² / mean_block |Ez_empty|²`
  at `P(θ)`. Phase `Δφ(θ) = arg(⟨Ez_article⟩/⟨Ez_empty⟩)` is read the same
  way, reported diagnostically only (not scored — see Idealizations).
- **Absolute-intensity reference** (precondition (a), fixed per mandatory
  fix 3 below): `I0_corrected(θ) = sqrt((mean_y Sx(y))² + (mean_y Sy(y))²)`
  at the existing `ref_for_r4(cfg)` strip, empty-scene run only — a
  direction-agnostic Poynting-magnitude reference built from the same
  linear-mean convention `i_inc` itself already uses (mean first, then
  the norm — NOT norm-then-mean), closing QUANTUM's Jensen's-inequality
  finding. `I_abs(θ) = mean_block(0.5·|Ez_article|²) / I0_corrected(θ)`.
- **Off-axis companion point** (precondition: spatially-localized
  darkening check, fixed per mandatory fix 2 below): `P_off(θ) = P(θ) +
  Δ_lat·v(θ)`, `Δ_lat=450` cells, a PURE beam-perpendicular offset (`a=0`
  along `u(θ)` by construction) — not the Phase-1 draft's fixed-lab-frame
  `(0,450)` offset, which EM's Phase-2 critique showed carries 271.6–306.7
  cells of along-beam displacement (76–93% as large as the intended
  lateral offset itself), landing it 2.4–2.5× `D_STANDOFF` downstream — a
  different diffraction z-slice, reproducing exactly the fixed-lab-frame
  failure shape (`beam_behind_t28`, `back_frac`) this cycle exists to
  retire, one level down, in the one channel meant to close it.
- **Thermal sidecar: NOT invoked this cycle** (mandatory fix 1). This
  proposal's geometry, angles, and configs are the byte-identical R4
  family already thermally scored UNDETECTABLE at exp-101 (368× margin)
  and the native flagship LOCKED UNDETECTABLE at exp-057 (699.27× margin)
  — no new absorbed-power regime is introduced (same article, same
  configs, same angles, same source amplitude). `run.py` does NOT import
  `netd_row`/`cell_metrics_r4`/`pair_metrics_full` from exp-101's `run.py`
  or any other prior experiment — only the new point/region-readout code
  and the already-gated `full_capture`/`phasors`/`_face_flux` primitives
  are used, so no thermal byproduct can be silently persisted. Stated
  explicitly here, before Phase 4, per THERMODYNAMICS' critique and Red
  Team's top-priority ranking (an unforced R21 third-strike risk).
- **`lab/` diff: zero.** All new code lives in this experiment's `run.py`.
- **Call budget**: 24 calls (6 angles × 2 configs × 2 conditions, the R4
  family) + 2 calls (Gate B's native-scale flagship, θ=0°, empty+article)
  = **26 real FDTD calls**. Gates A/C/D and the off-axis/point-vs-region
  predictions are zero-marginal-FDTD post-processing of the same 26
  captures. Call count (26) and row count (6 angles × 2 configs = 12 rows
  for the primary channel) asserted separately and explicitly (R19).

## New trust-suite stage 24 (four gates — Gate D added per mandatory fix 4)

- **Gate A (trivial-reduction identity).** No-object scene used as BOTH
  legs ⇒ `κ(P)=1.0` to float64 round-off (`<1e-10`), every point/angle.
  Zero marginal FDTD.
- **Gate B (known-good reproduction, R15-lineage).** At θ=0° on the
  original native-scale flagship absorber (exp-001/002, `beam_behind`=
  1.5–1.8% established), the new on-axis region-averaged `κ(θ=0°)` must
  land in `[0.005, 0.05]` — order-of-magnitude reproduction (log-space:
  ≈0.48 decades below to ≈0.44 decades above the established figure,
  checked and confirmed reasonably symmetric by Red Team), not an
  exact-match bar (a window envelope-ratio and a point/region
  field-intensity ratio are genuinely different quantities).
- **Gate C (absolute-normalization self-consistency).** `|I0_corrected(θ)
  ·cosθ − i_inc(θ)| / I0_corrected(θ) ≤ 0.01` at all 6 angles, using the
  corrected mean-then-norm `I0_corrected`.
- **Gate D (fault-injection positive control on the rotating `P(θ)`
  construction — new, per Red Team's own independent finding, attack 7).**
  Gates A and B cannot, by construction, catch a geometric-placement bug
  in the new rotating-frame `P(θ)` arithmetic itself: Gate A compares the
  same (possibly-wrong) point against itself, and Gate B only exercises
  θ=0°, where the beam-aligned frame trivially reduces to the lab frame.
  Gate D: at one nonzero angle (39.200000°, the largest-magnitude angle
  in the pool), independently hand-compute `P(θ)` from the raw `Sim` grid
  geometry (the same `_verify_box_margins()`-style direct-geometry check
  R17 already mandates elsewhere, not a re-derivation of the formula being
  tested), confirm it matches the code's own `P(θ)` to the nearest cell,
  then deliberately perturb `P(θ)` by a known 20-cell offset along `u(θ)`
  and confirm `κ` at the perturbed point differs measurably (>5%) from
  `κ` at the correct point on the SAME already-captured article-scene
  field (zero additional FDTD). This is a genuine positive control: it
  can fail for the right reason (a `P(θ)` bug that Gates A/B cannot see).

## Changes from Phase 1 (Red Team's Phase-2 audit, 7 mandatory fixes, all
## adopted, 0 overridden — Director's synthesis)

1. **[R21 risk discharged] Explicit thermal-sidecar disposition stated
   above (not invoked; `netd_row`/`cell_metrics_r4` not imported) before
   any Phase-3 implementation choice** — highest priority: cheapest fix
   against the highest-consequence failure mode in the packet (an
   unforced automatic Checkpoint-4 firing, R21's third strike).
   *(THERMODYNAMICS' critique; Red Team attack #3, ranked #1.)*
2. **[localization-check validity] Off-axis companion point rebuilt as a
   pure beam-perpendicular offset** `P_off(θ)=P(θ)+Δ_lat·v(θ)`, replacing
   the Phase-1 draft's fixed-lab-frame `(0,450)` offset, which EM's
   Phase-2 critique showed (independently re-verified by Red Team, exact
   arithmetic match at two angles) carries 271.6–306.7 cells of
   along-beam displacement — landing the "lateral" check 2.4–2.5×
   `D_STANDOFF` downstream, a different diffraction z-slice, reproducing
   the exact fixed-lab-frame failure (`beam_behind_t28`, `back_frac`) this
   cycle exists to retire. *(EM's critique; Red Team attack #1.)*
3. **[Jensen's-inequality bias fixed] `I0_corrected` rebuilt as
   `sqrt((mean_y Sx)²+(mean_y Sy)²)`** (mean-then-norm), replacing the
   Phase-1 draft's `mean_y sqrt(Sx²+Sy²)` (norm-then-mean) — mathematically
   confirmed by QUANTUM's critique (Jensen's inequality: `E[‖X‖]≥‖E[X]‖`,
   equality only if the sampled vector is constant, which a real FDTD
   reference strip's ripple/taper residue never is) and independently
   re-derived by Red Team. The corrected form matches `i_inc`'s own
   established linear-mean convention. *(QUANTUM's critique; Red Team
   attack #2.)*
4. **[new gate] Gate D — fault-injection positive control** on the
   rotating `P(θ)` construction, closing the one class of bug Gates A/B
   cannot detect (an R6/R18-lineage principle: a check's claimed scope
   must be independently confirmed against what it can actually detect).
   Zero additional FDTD. *(Red Team's own independent finding, attack 7.)*
5. **[perceptual-overclaim struck] §4's "which is constraint 1's witness
   question" replaced.** κ(θ) answers constraint 1's *physical*
   transmission question — a necessary but not sufficient input to the
   witness's actual percept, which needs an adaptation state and a
   `C_thr(L)` comparison (Tier 2, still unbuilt) that this instrument does
   not supply. *(VISION's critique; Red Team attack #4.)*
6. **["T3" mislabel struck]** The Phase-1 draft's Idealizations re-cited
   "the T3 build" for the still-unbuilt Tier-2 perceptual conversion — T3
   is LOGBOOK's unrelated temporal-contrast/switching instrument;
   exp-101's own Phase-5 VISION finding already corrected and dropped this
   exact label one cycle ago. Struck here; the conversion is stated
   plainly as "constraint 1's own missing conversion," matching exp-101's
   own corrected language exactly, no thread number implied. Red Team
   confirmed this is a real, single, isolated recurrence that does NOT
   approach R20's "three or more" bar, on two independent sufficient
   grounds (caught at Phase 2 not Phase 5; lives in Idealizations/Next,
   never Result/Learned — the identical ruling Red Team's own Phase-5
   audit made on this exact sentence's first appearance, exp-101
   `phase5_redteam_audit.md` §1.2 Candidate 5). Not R20-firing; fixed
   anyway because it is free to fix now. *(VISION's critique; Red Team
   attack #5 + dedicated §3 ruling.)*
7. **[realizability caveat travel requirement] Binding on Result-writing**:
   the UNOBTANIUM-WITH-PARAMETERS/"a buildable coating at this thickness
   would show a shallower, not deeper, on-axis darkening" caveat MUST be
   stated inline beside Prediction 1's κ(θ) confirmation text in the
   Result section below (not only cross-referenced via Idealizations) —
   the identical discipline this program already paid for once (R1's own
   Iteration-14 ENZ addendum) and already applied once as house style
   (exp-101's own mandatory fix 6, the T9 disclaimer). *(MATERIALS'
   critique; Red Team attack #6.)*

**Non-mandatory, checked and cleared by Red Team (no fix applied):** Gate
B's `[0.005,0.05]` band (log-symmetric, defensible); Prediction 4's 3×
point-vs-region band (defensible given near-null noise behavior).

## Predictions (committed to git BEFORE Phase 4 runs any FDTD call — house
## discipline, non-negotiable)

1. **On-axis coherent intensity ratio** `κ(θ) ∈ [0, 0.10]` at all 6 angles,
   both configs (`H_REGION`-block reading). Grounded in the established
   near-total-absorption/large-`Q_ext` behavior of this exact article
   (exp-001's flagship anchor; exp-101's own `Q_ext`≈1.54–1.56 corrected
   reading). **Falsified** if `κ(θ) ≥ 0.10` at any resolved angle/config.
   *(Realizability caveat, fix 7: this article is already locked
   UNOBTANIUM-WITH-PARAMETERS — a real, buildable coating at this shell
   thickness would show a shallower, not deeper, on-axis darkening than
   whatever this instrument measures here; this number characterizes the
   idealized article, not a claim about real-coating performance.)*
2. **Absolute-normalization self-consistency** (Gate C): `|I0_corrected(θ)
   ·cosθ − i_inc(θ)| / I0_corrected(θ) ≤ 0.01` at all 6 angles, using the
   corrected mean-then-norm `I0_corrected`. **Falsified** if the deviation
   exceeds 1% at any angle — would mean the local-plane-wave assumption
   itself needs revisiting, not merely a display fix (and, per fix 3's own
   correction, could no longer be confused with an averaging-order
   artifact, since that specific bias is now eliminated by construction).
3. **Off-axis companion point** `κ_off(θ) ≥ 0.90` at all 6 angles, both
   configs, using the corrected pure-beam-perpendicular `P_off(θ)`.
   Confirms the instrument resolves a spatially LOCALIZED dark region
   (the shadow) rather than broadband dimming of the whole downstream
   half-plane. **Falsified** if `κ_off(θ) < 0.90` at any angle/config — a
   genuinely more troubling, differently-interesting finding, not merely
   a miss.
4. **Point-vs-region stability**: the single-nearest-cell `κ(θ)` and the
   `H_REGION`=10-cell-block-averaged `κ(θ)` at `P(θ)` agree to within a
   factor of 3× at all 6 angles. **Falsified** if any angle shows
   disagreement exceeding 3×, which would mandate the region-averaged
   reading as this instrument's ONLY trustworthy output going forward.
5. **Gate D fault-injection control**: the 20-cell-along-`u(θ)` perturbed
   point's `κ` differs from the correct point's `κ` by more than 5% at
   39.200000°, both configs. **Falsified** (meaning: Gate D itself fails
   to discriminate, and the rotating-`P(θ)` construction needs an
   independent validation method before ANY reading from this instrument
   is trusted) if the perturbed and unperturbed `κ` agree within 5% —
   this would mean the instrument's core novel construction is not
   actually being exercised by the test geometry at this standoff, a
   pre-condition failure, not merely a missed number.

## Idealizations

- **Region-averaging is a small nearest-cell block, not a true
  beam-cross-section-perpendicular sample.** Disclosed; Prediction 4 is
  the pre-registered check of whether this matters at all.
- **Near-field standoff only (T8).** `D_STANDOFF`=200 cells sits deep in
  the shadow's near/Rayleigh zone — these numbers describe this bench's
  own near-field geometry, not an asymptotic witness-scale claim; the
  r=78/156/312 bridge family (T8) governs any future extrapolation.
- **T9's Babinet-ceiling / near-field disclaimer applies to any citation
  of this article's own shadow depth as evidence of "how black a real
  coating gets."**
- **Amplitude-floor discipline, proactively applied (R13/R14 lineage).**
  `κ(θ)`'s denominator (`|Ez_empty|²` in a smoothly-tapered vacuum plane
  wave) has no known/plausible zero-crossing at these interior points
  (unlike R13's founding `delta_scene` case), so no R13-style floor gate
  is structurally mandated — applied anyway as house-style due diligence:
  any cell whose region-mean `|Ez_empty|²` falls below 10% of its own
  12-cell-pool RMS (`FLOOR_FRAC`=0.10, exp-088/exp-101's convention) is
  reported `UNRESOLVED-BY-CONSTRUCTION`, never silently scored.
- **Phase (`Δφ(θ)`) is reported diagnostically, not scored against any
  band.** Inside a genuinely dark region `|Ez|` is small and phase is
  numerically noisy.
- **No perceptual/Weber-contrast scoring this cycle.** This instrument
  reports a raw coherent-field ratio and an absolute intensity fraction,
  not a witness-perceived contrast against `C_thr(L)` — per fix 5, this is
  constraint 1's *physical* transmission question only, a necessary but
  not sufficient input to the witness's actual percept. That conversion
  (constraint 1's own missing conversion, exp-101's Next item — no thread
  number assigned; NOT T3, per fix 6) is future work, out of scope here.
- **Single wavelength (600 nm), the two already-committed `R4_CONFIGS`
  only** — matching exp-101's own scope; a 450/750 nm leg is not proposed
  this cycle.
- **Exact `D_STANDOFF`/`H_REGION`/`Δ_lat` cell counts are Phase-1/3
  estimates; Phase 4 re-verifies every margin by direct `Sim` geometry
  computation (`_verify_box_margins()`-style, per R17) before any FDTD
  call**, not by hand-derivation alone.
- **Thermal sidecar: N/A this cycle** — see Setup; disposition stated
  explicitly per fix 1, not silently omitted.

## LOGBOOK.md RULED OUT registry / standing rules check

No item in LOGBOOK's RULED OUT registry (R1–R21) is re-proposed: no
mechanism or material parameter is touched (not R1); no named-constant
search is performed (not R5); the amplitude-floor discipline is applied
proactively though not structurally mandated (R13/R14 lineage, not a
violation); Gate B is a known-good reproduction check in R15's own
lineage, not a resolution refinement; `D_STANDOFF`/`H_REGION`/`Δ_lat` are
justified against already-established scales and re-verified by direct
geometry before any run (R17); the "T3" mislabel recurrence is struck
(fix 6) and independently ruled non-R20-firing by Red Team on two
sufficient grounds (§ above). No closed Live Thread claim is re-litigated:
T8's near-field caveat is disclosed, not resolved; T9's Babinet-ceiling
disclaimer is restated, not contested; T28's own `delta_scene`/R3-vs-R4
split (Tier 1, exp-100/101) is untouched — this experiment does not read,
cite, or score `delta_scene`/`frac_contrast`/`ratio_k` at all.

## Phase 4 process note (disclosed, non-scientific)

Two Phase-4 execution agents were inadvertently run concurrently against
this experiment's directory for part of this cycle (an orchestration
error by the Director, not a science defect) — each independently
executing/editing `run.py` without visibility into the other, and each
independently discovering the two real defects below by different routes.
The Director stood one down and consolidated the survivor's work into one
final, clean, from-scratch 26-call run once both defects were understood.
No `lab/` diff resulted at any point; the trust suite was confirmed green
before, during, and after. Recorded here in the interest of the same
verify-before-claim discipline this document applies to everything else —
the final numbers below are from the single final consolidated run
(`run_output.txt`/`results.json` as committed), not from either
intermediate attempt.

## Result

**Gate A: PASS.** Trivial-reduction identity — no-object scene as both
legs — `κ(P)=1.0` to `<1e-10` (measured: exactly `0.0`) at all 48
points/angles tested. Zero marginal FDTD.

**Gate B: FAIL — genuine, diagnosed, not force-fixed.** A real
implementation bug was found and fixed first: `D_STANDOFF=200`/
`H_REGION=10` cells were sized as `1.282×R4_R_OUT` for the R4 family's
`cells_per_lambda=40` grid; reused unscaled at the native flagship's
`cells_per_lambda=20` (confirmed directly from `experiments/001-.../
run.py`'s `SWEEP=[(15,450),(20,600),(25,750)]`), they put the sample
point at `2.56×r_out` instead of the intended `1.282×r_out` — rescaled
to `GATEB_D_STANDOFF=100`/`GATEB_H_REGION=5` (×0.5, the `cpl` ratio) to
correct this. **After the fix, Gate B still fails**: `κ_region(θ=0°) =
1.627×10⁻³`, now BELOW the `[0.005,0.05]` band floor (the original,
unrescaled crash had measured `5.471×10⁻²`, just above the ceiling — the
correction moved the reading past the band, not into it). Diagnosis,
independently verified against `experiments/001-flashlight-statement/
run.py`'s own `BEHIND` slice definition (`slice(CX+R_CLK+15,
CX+R_CLK+115)`, i.e. `x∈[357,457)`, `CX=252, R_CLK=90`, absorber
`r_out=78` ⇒ the established window spans `≈1.35×`–`2.63×r_out` from
center): the corrected point (`100` cells `≈1.28×r_out`) sits BEFORE
that window even starts, closer to the object, in the near-field zone
where a real shadow reads measurably darker than farther out (Fresnel
diffraction fills a shadow back in with increasing standoff — a real,
physically expected effect, not an artifact). A point sample and a
wide-window spatial average, taken at two different effective distances
from the object, are not the same quantity — moving the point to land
inside the established window post-hoc would be exactly the kind of
after-the-fact parameter adjustment LOGBOOK's R5 rules out, so it was not
done. **Consequence for trust**: per PANEL.md's new-machinery rule, only
Gates A (trivial identity) and D (fault-injection positive control, below)
independently support trusting this instrument's primary-channel readings
this cycle. Gate B — the cross-scale reproduction check against the
established old-instrument figure — is NOT validated. This is a real,
open limitation, not a formality; see Next.

**Gate C / Prediction 2: FAIL as originally specified, PASS after an
independently re-derived sign correction — CONFIRMED.** The frozen
spec's formula compared `I0_corrected(θ)·cos θ` (unsigned) against
`i_inc(θ)`. Measured: a uniform ~145–160% "deviation" at every single one
of the 12 (angle,config) cells (max `159.78%`) — a systematic sign-flip
signature, not per-cell noise, immediately suspicious. Root cause,
independently re-derived (per LOGBOOK's R4 addendum — never adopt a sign
correction merely because it makes numbers agree): `i_inc = mean_y(Sx(y))`
(`lab/sections.py`, confirmed directly from source) and the R4 family's
own propagation direction is `u(θ)=(-cosθ,+sinθ)` (independently verified
correct against `add_line_source`'s own documented convention by EM's
Phase-2 critique, for the unrelated purpose of constructing `P(θ)`).
Since the Poynting flux vector is parallel to the propagation direction
for a plane wave, `(Sx,Sy) ≈ I0_corrected·u(θ)`, i.e. `Sx ≈
I0_corrected·(-cosθ)`, NOT `+I0_corrected·cosθ` as originally written —
the frozen formula's sign, not the underlying instrument, was wrong.
Corrected formula: `|I0_corrected(θ)·u_x(θ) − i_inc(θ)| / I0_corrected(θ)
≤ 0.01`, `u_x(θ)=-cosθ`. Measured with the correction: max deviation
`0.92%` across all 12 cells (range `0.04%–0.92%`) — inside the
pre-registered 1% band. **Both the original erroneous values and the
corrected values are recorded in `results.json`**, per the same
non-negotiable disclosure standard this program's R4 lineage requires.
**PASS/CONFIRMED on the corrected formula.**

**Gate D: PASS.** At θ=39.2°, both configs: the hand-computed `P(θ)`
independently matched the code's own `P(θ)` to the nearest cell in both
configs (`(185,1710)`, `(265,1790)`). A +20-cell perturbation along
`u(θ)` changed `κ_region` by `48.95%` (C40_R4) and `8.24%` (G40_R4) —
both clearing the >5% discrimination bar. The rotating `P(θ)`
construction is genuinely exercised and independently validated at a
nonzero angle, closing the one class of bug Gates A/B cannot see.

**Primary channel** (24 real FDTD calls, 6 angles × 2 configs × 2
conditions, 3180.7s/53.01min wall): on-axis coherent intensity ratio
`κ(θ)` (region-averaged) ranges `3.48×10⁻³`–`7.29×10⁻³` (minimum at
`C40_R4@41.460901°`) across all 12 (angle,config) cells — genuinely dark,
well inside `[0,0.10]`.
**Realizability caveat (per fix 7, stated inline as required): this
article is the byte-identical R4-family `graded_black_shell`, already
locked UNOBTANIUM-WITH-PARAMETERS (`REALIZABILITY_MEMO.md` Amendments
6–7) — a real, buildable coating at this shell thickness would show a
shallower, not deeper, on-axis darkening than this idealized figure.**
Off-axis companion point `κ_off(θ)` (pure beam-perpendicular, 450 cells)
ranges `1.041`–`1.077` — mildly BRIGHTER than the empty scene (not
merely "undimmed"), consistent with light scattered/diffracted away from
the shadow's own axis rather than uniform dimming — confirming the
darkening at `P(θ)` is spatially localized, the check's stated purpose.
Point-vs-region agreement: ratios `1.23`–`1.56×`, comfortably inside the
3× band. `Δφ(θ)` (diagnostic only): `+0.21`–`+0.59` rad, all positive,
not scored. Floor gate: `0/12` cells `UNRESOLVED-BY-CONSTRUCTION` across
all three pools (region@P, point@P, region@P_off) — the amplitude floor
never triggered, as anticipated in Idealizations. Thermal sidecar: N/A
this cycle, exactly as committed in Setup — `netd_row`/`cell_metrics_r4`
were not imported into `run.py`, discharging the R21 risk cleanly.

**Predictions: 1, 3, 4, 5 CONFIRMED as originally specified. 2 CONFIRMED
on the corrected formula (FALSIFIED on the original, sign-erroneous
formula — disclosed, not hidden).** Real FDTD calls: 26 (24 R4-family +
2 Gate B), matching the committed budget exactly. Trust suite confirmed
green before, during, and after (41/41); zero `lab/` diff throughout.

## Learned

1. **The coherent point/region instrument works and is trustworthy for
   the primary channel it was built to answer** — constraint 1's own
   physical (not yet perceptual) transmission question now has a real,
   phase-resolved, rotating-frame answer on this bench for the R4 family:
   a genuine, spatially-localized on-axis darkening of `κ~0.3–0.7%`,
   immune by construction to the `i_inc`/cosθ artifact (it never calls
   `sc.widths()`) and to fixed-lab-frame registration (Gate D
   independently confirms the rotating construction is exercised
   correctly). This closes exp-101's own Next item 1 as a working
   instrument, not merely a proposal. **Realizability caveat (per fix 7,
   restated here per Red Team's Phase-5 mandatory fix 3 — this same
   caveat travels with this figure wherever it is cited, not only beside
   Prediction 1 in Result): this article is already locked
   UNOBTANIUM-WITH-PARAMETERS — a real, buildable coating at this shell
   thickness would show a shallower, not deeper, on-axis darkening.**
2. **A cross-scale "known-good reproduction" gate needs the SAME
   measurement footprint as the figure it reproduces, not merely the
   same relative-to-object-size standoff.** Gate B's failure is not a
   flaw in the new instrument — it is a mismatch between what the new
   instrument measures (a point/small-region sample) and what the old
   `beam_behind` figure measures (a wide spatial-window average starting
   farther from the object). A near-field shadow genuinely fills back in
   with distance (Fresnel diffraction), so a point sample and a window
   average at different effective standoffs are not interchangeable —
   this is a real, generalizable lesson for any future "does the new
   thing see what the old thing saw" gate on this bench: match the
   OLD measurement's own spatial footprint, don't merely rescale a
   different footprint by object size.
3. **A second, independent instance of the R4-lineage "sign correction
   must be independently re-derived, never adopted merely because it
   makes two numbers agree" discipline just earned its keep, live, at
   Phase 4 rather than at a later Phase-5 catch.** The ~150% deviation's
   own uniform, per-cell-invariant character (not noisy, not partial) was
   itself the tell that this was a systematic sign artifact rather than a
   per-cell physics discrepancy — a diagnostic heuristic worth carrying
   forward: a "deviation" that is suspiciously uniform across independent
   cells is more likely a formula/convention bug than a real effect.
4. **A frozen Phase-3 formula can still carry a sign defect through to
   Phase 4** — the `Sx≈I0_corrected·cosθ` self-consistency identity in
   this cycle's own NOTES.md (and in the Phase-1 proposal, verified by
   two Phase-2 critiques and Red Team without catching this) was written
   without the leading minus sign its own `u(θ)=(-cosθ,sinθ)` convention,
   used two lines away for `P(θ)`, already required. Neither the two
   independent Phase-2 seats (EM, QUANTUM) that specifically checked this
   formula, nor Red Team's own independent re-verification, caught the
   sign — all three verified the MAGNITUDE relationship and the
   AVERAGING-ORDER issue (correctly), but none independently re-derived
   the sign from `u(θ)` itself. Worth flagging to Phase 5/Red Team as a
   possible new standing-rule candidate: a self-consistency identity
   between two vector-valued quantities must have its SIGN independently
   re-derived from the same convention already governing any other use of
   that vector in the same document, not merely its magnitude.

## Next (candidate directions, not this cycle's scope)

1. **A properly-scoped Gate B, matched to the established `beam_behind`
   figure's own spatial footprint** (the literal `BEHIND` window, or an
   equivalently-justified window on the R4-family scale) rather than a
   rescaled point/region sample — the correct fix identified in Learned
   item 2, deliberately NOT applied this cycle to avoid a post-hoc
   parameter search on already-observed data (would need its own fresh
   Phase-1 justification and a re-run, cleanly separated from this
   cycle's own committed predictions).
2. **The candidate standing rule from Learned item 4** (sign of a
   vector-valued self-consistency identity must be independently
   re-derived from the same convention already governing that vector
   elsewhere in the same document) — a Red Team/Phase-5 call on whether
   to formally adopt it.
3. Tier 1 (the R3-vs-R4 `delta_scene`-realizability split, PHOTONICS'
   zero-FDTD physical-hypothesis check first) remains queued, unchanged,
   per exp-100/exp-101's own Reconciled-queue ranking — untouched this
   cycle by design.
4. The Tier-2 perceptual conversion (constraint 1's own missing
   conversion from this cycle's raw `κ(θ)`/`I_abs(θ)` to a witness-
   perceived `C_thr(L)` judgment) — still unbuilt, per fix 5/6's
   corrected scoping.

## Phase 5 outcome (six blind reviews + Red Team final audit)

Six blind Phase-5 reviews (all CONFIRM-WITH-GAPS) independently
recomputed `results.json` from primitives and converged on one real
citation defect: the on-axis `κ(θ)` range floor stated above as
`3.68×10⁻³` was actually the second-smallest of 12 cells, not the
minimum (true minimum `3.48×10⁻³`) — corrected above (Result and Learned
item 1), per Red Team's mandatory fixes 1–2. MATERIALS additionally
found the same headline recurring in Learned item 1 without the
realizability caveat Result carries beside it — corrected above (fix 3).
All six reviews independently re-derived and confirmed the Gate C sign
correction from scratch by different methods (six independent
derivations total, program's most heavily cross-verified single formula
fix); zero overrides. Red Team's final audit ruled: **ONE** distinct
R4-class defect survives Phase-3-freeze into Result/Learned (the range
floor, propagating unchanged into Learned #1 by direct inheritance, not
independent re-arising) — R20 requires 3+, does not fire, not close (1,
or 2 under the most generous counting). Checkpoint criterion 4 does not
fire on any ground (the disclosed process erratum touched zero `lab/`
code, independently confirmed via git; Gate B's FAIL is honestly scoped,
not unfalsifiable; constraint 3 untouched by design). **New standing
rule R22 adopted** (LOGBOOK.md): a frozen vector-valued self-consistency
identity's SIGN must be independently re-derived from whatever
convention already governs that vector elsewhere in the document, before
any Phase-4 FDTD call is scored against it — founding instance (this
cycle's own Gate C), does not fire. **Combined Verdict: PROMISING.**
Reconciled Iteration-80 queue (Red Team's own ranking): Tier 1 (a
zero-new-FDTD standoff diagnostic on Gate B's own already-captured field;
a footprint- AND aperture-matched Gate B rebuild; extending this
instrument across the T8 r=78/156/312 bridge family); Tier 2 (the Tier-2
perceptual conversion, gated on Tier 1; pinning the witness-scale source
wattage); Tier 3 (the standing `delta_scene` split, now 3 cycles
deferred; a pre-registered `κ_off(θ)` angular resweep). Full record:
`phase5_review_{photonics,materials,em,thermodynamics,quantum,vision}.md`,
`phase5_redteam_audit.md`.
