# Phase 1 Proposal — exp-102: The Coherent, Phase-Resolved Downstream Point-Intensity Instrument

**Panel Iteration 79. Lead seat (rotation): PHOTONICS.** Reconciled
Iteration-79 queue, item 1 (Red Team's own top ranking, exp-101 close).
Instrument build, Tier-0-shaped scope: no new mechanism, no new material,
no `lab/` diff. Commissioned directly by exp-101's own "Next" item 1 and
LOGBOOK.md's Iteration-78 entry.

## Mechanism / instrument narrative (≤300 words)

T1 names the central tension: any LTI absorber that darkens the ambient
view (constraint 3) must, by the same physics, terminate the beam
(constraint 1) — one shared extinction mechanism. Constraint 1's own
witness question — "does the background stay lit behind the object?" —
has never been measured directly on this bench. `beam_behind_t28` (a
fixed lab-frame line window) proved uninterpretable at oblique incidence
(exp-100): the object's own shadow walks laterally faster than the
window tracks it. exp-101's replacement, `sigma_scat_downstream`
(closed-box Poynting flux), is interpretable but answers a different
question: it is an incoherent POWER integral, and the extinction paradox
guarantees a large forward-scattered cross-section accompanies any real
shadow — a large `sigma_scat_downstream` reading is the mathematically
expected companion of "dark," not evidence against it, because a power
integral discards the field's PHASE, and phase is exactly what
distinguishes destructive cancellation (a shadow) from constructive
refilling (a cloak-like escape, R1). Constraint 1's witness question is a
statement about coherent field amplitude at a point, not power crossing
a surface.

This proposal builds that missing instrument: read the already-gated
complex Ez/Hx/Hy phasors (`lab/sections.py::full_capture`/`phasors`,
trust-suite stage 8, zero `lab/` diff) at a small region on the beam's
OWN downstream axis, in both the empty-scene and article-scene runs
launched with bit-identical source phase — then compare coherently
(amplitude ratio and phase) at that same physical location. This
directly measures whether light reaches the point behind the object,
resolving the ambiguity `sigma_scat_downstream` cannot. Two structural
fixes, both bound by exp-101's own Phase-5 findings, are load-bearing
from first light: the sample point rotates with the beam's own launch
angle (never a fixed box), and the absolute incident reference is the
full, direction-agnostic Poynting magnitude, not `sc.widths()`'s
x-projected `i_inc`. Diagnostic-only: no mechanism parameter is
proposed or varied this cycle.

## Parameter table

### 1. Geometry — reused, unmodified R4 family (exp-094..101, zero new `lab/` diff)

| Quantity | Value | Source |
|---|---|---|
| Article | `pec_disk`(r=`PEC_R_R4`=60) + `graded_black_shell`(r_in=60, r_out=`R4_R_OUT`=156, σ_max=`SIGMA_R4_CORRECTED`=0.25) | exp-094 |
| Configs | `C40_R4` (nx=720,ny=3168,absorb=80,pad=0,obj_x=340,obj_y=1584,src_x=600) and `G40_R4` (pad=80, obj_x=420,obj_y=1664,src_x=680) | exp-094 `design_geometry.py::r4_config` |
| `cells_per_lambda` | 40 @ 600 nm | `R4_CPL={600:40}` |
| `DX_M_R4` | 1.5×10⁻⁸ m/cell | `600e-9/40` |
| Source | `add_line_source(profile="plane", edge=R4_TAPER=80, angle_deg=θ, amplitude=1.0)` | unchanged |
| Angles | `[37.127246, 38.590230, 39.200000, 40.265420, 41.460901, 42.960901]` — the same 6 established, re-verified-pool-wide-largest, R4-family angles exp-101 used | exp-101 §Setup |
| Wavelength | 600 nm only | matches exp-101 scope |
| Steps | `R4_STEPS`=5600 (settled, unchanged) | `design_geometry.py` |

### 2. The downstream point/region — beam-aligned frame (precondition (b))

Unit propagation direction, taken verbatim from `lab/fdtd2d.py::
add_line_source`'s own documented launch convention (the −x-going wave
travels along `(−cosθ, +sinθ)`):

```
u(θ) = (−cos θ, +sin θ)          # beam propagation direction
v(θ) = (+sin θ, +cos θ)          # perpendicular in-plane direction, u·v = 0
```

**Primary witness point** (rotates with θ — never a fixed lab-frame
column, the exact defect exp-100/101 diagnosed in `back_frac`/
`beam_behind_t28`):

```
P(θ) = (round(obj_x + D·(−cos θ)), round(obj_y + D·sin θ))
D = D_STANDOFF = 200 cells   (≈1.28×R4_R_OUT; comparable to, and just
    beyond, BOX_A's own already-gated clearance R4_R_OUT+
    BOX_CLEARANCE_A_R4=180 cells — reuses vetted scale, not a new
    distance regime)
```

Margin check (Phase-1 estimate, Phase-3 to re-verify by direct geometry
computation, `_verify_box_margins()`-style, per R17): at C40_R4 (the
tighter domain, obj_x=340, absorb=80), `Δx = −D·cos θ` ranges
−159.4 (37.13°) to −146.5 (42.96°) cells, landing `P_x` at 181–193 —
margin above the absorb-boundary interior edge (80) of 101–113 cells,
clearing the ≥90-cell Fix-4/R17 bar with room; `Δy` (121–136 cells) is
negligible against C40_R4's `ny`=3168.

**Region average** (mitigates VALIDATION.md's own "point-wise
measurements are fringe-limited" lesson — T10's independent restatement
of the same principle for a transmission channel): the `H_REGION`=10-cell
half-width block of Ez-grid cells nearest `P(θ)` (no interpolation,
nearest-cell block mean of `|E|²`), reported ALONGSIDE the raw
single-nearest-cell reading (Prediction 4 below scores whether the two
diverge enough to matter).

**Off-axis companion point** (validates that any measured darkening is
spatially LOCALIZED — the shadow — not broadband dimming; a secondary
check, not the primary witness measurement, so it is allowed the
simplification of a fixed lab-frame lateral offset at matching lab-frame
x, disclosed as an idealization):

```
P_off(θ) = (P_x(θ), P_y(θ) + 450)      # 450 cells ≈ 2.9×R4_R_OUT,
                                         # clears the ~312-cell (2×R4_R_OUT)
                                         # geometric shadow diameter
```

### 3. Coherent comparison method

Both legs (`with_article=False/True`) for a given `(key, θ)` already
launch with bit-identical `add_line_source` parameters (same `angle_deg`,
`ramp_periods`, `rel_phase=0`) — so `full_capture(sim)` → `phasors(cap)`
(unchanged `lab/sections.py`, stage 8) returns each run's own absolute
complex `ez`/`hx`/`hy` phasor referenced to the SAME time origin, exactly
the "same source phase" precondition `sections.py`'s own docstring
already states `widths()` relies on. No new phase-referencing machinery
is needed; only the READOUT location changes (a rotating point/region
instead of a box perimeter).

Primary witness metric — same-point coherent intensity ratio (dimensionless):

```
κ(θ) = mean_{cells in H_REGION block at P(θ)} |Ez_article(cell)|²
     / mean_{cells in H_REGION block at P(θ)} |Ez_empty(cell)|²
```

Because both terms are evaluated at the identical grid location in vacuum
(ε_r≡1 outside the object, so the local wave impedance — and thus the
proportionality between |Ez|² and Poynting magnitude — is identical in
numerator and denominator), κ(θ) is a same-point ratio and is
**automatically free of the `i_inc`/cosθ artifact** — it never calls
`sc.widths()` or normalizes by `i_inc` at all. Phase is read the same
way: `Δφ(θ) = arg(⟨Ez_article⟩/⟨Ez_empty⟩)` over the same block, reported
diagnostically (not scored against a band — see Idealizations).

### 4. Absolute-intensity normalization — precondition (a)

κ(θ) alone answers "is this point dark relative to what would be there
with nothing in the way," which is constraint 1's witness question. But
this instrument ALSO reports an absolute intensity (needed for any
future conversion to physical irradiance / Weber-contrast scoring, per
the Next-item's own stated purpose) — and it is exactly this absolute
number exp-101's `Q_ext→2` artifact shows must not be built on
`sc.widths()`'s raw `i_inc`. **Fix**: compute the incident reference as
the FULL, direction-agnostic time-averaged Poynting magnitude at the
existing `ref_for_r4(cfg)` strip (empty-scene run only — no new field
capture, reuses the phasors already read for `i_inc`):

```
Sx(y) = −0.5·Re{Ez(y)·conj(Hy_interp(y))}     # sc.sections._face_flux's own sx()
Sy(y) = +0.5·Re{Ez(y)·conj(Hx_interp(y))}     # sc.sections._face_flux's own sy()
I0_corrected(θ) = mean_y sqrt( Sx(y)^2 + Sy(y)^2 )
```

`I0_corrected` is the genuine magnitude of the incident Poynting vector —
it does not assume or divide by `cos θ`; the cosine falls out as a
CONSEQUENCE (`Sx ≈ I0_corrected·cos θ`, `Sy ≈ I0_corrected·sin θ` for a
locally-plane-wave region), which is exactly what Gate C (below) checks
as a self-consistency identity, not an assumed correction. The
instrument's absolute-intensity output is then:

```
I_abs(θ) = mean_{H_REGION block at P(θ)} (0.5·|Ez_article(cell)|^2) / I0_corrected(θ)
```

— normalized against a reference that cannot leak the `1/cos θ`
artifact into any absolute number this instrument reports, closing
precondition (a) exactly as commissioned (not by relying on a ratio that
happens to cancel the bug, but by fixing the reference itself).

### 5. Wavelengths / angles tested

600 nm only, the same 6 established R4-family angles (§1), both
`C40_R4`/`G40_R4` configs — plus one new normal-incidence (`θ=0°`) leg on
the ORIGINAL native-scale flagship article (`graded_black_shell`,
`r_out`=78, `sigma_max`=0.5, exp-001/002) for Gate B below, where the
beam-aligned frame trivially reduces to the lab frame (isolating the new
readout machinery from the new rotating-frame machinery for the
reproduction check).

## New machinery / trust-suite stage

**Yes — new suite stage required** (PANEL.md Phase-4: "new machinery ⇒
new suite stage with at least one absolute identity gate BEFORE results
are trusted"). This is a genuinely new measurement class on this bench
(coherent point/region field-intensity ratio; every prior channel —
`ambient.py`'s window-mean contrast, `sections.widths()`'s box-flux
partition — is either a window-averaged incoherent contrast or a closed
box power integral, never a raw point/region field comparison). Proposed
**suite stage 24**, three gates:

- **Gate A (trivial-reduction absolute identity).** No-object scene used
  as BOTH legs (article physically omitted) ⇒ `κ(P)=1.0` to float64
  round-off (`<1e-10`) at every tested point, every angle. Zero marginal
  FDTD (reuses one already-planned empty-scene capture compared against
  itself). Cheap, mandatory, catches any indexing/registration bug in
  the new point-extraction code before it ever touches a real article.
- **Gate B (known-good reproduction, R15-lineage).** At `θ=0°` on the
  ORIGINAL native-scale flagship absorber (exp-001/002's own already-
  gated near-total-absorption article, `beam_behind`=1.5–1.8%
  established), the new on-axis region-averaged `κ(θ=0°)` must land in
  `[0.005, 0.05]` — same order of magnitude as the already-known-correct
  figure. Not an exact-match bar (a window envelope-ratio and a
  point/region field-intensity ratio are genuinely different
  quantities, disclosed below), but a mandatory "does the new instrument
  see the same physics the old, trusted one already established"
  reproduction check, in the same spirit R15's own addendum requires of
  any new resolution/measurement family before its first near-null
  reading is trusted.
- **Gate C (absolute-normalization self-consistency).** `|I0_corrected(θ)
  ·cos θ − i_inc(θ)| / I0_corrected(θ) ≤ 0.01` at all 6 angles
  (empty-scene reference strip, R4 family) — a direct, quantitative
  closure of exp-101's own QUANTUM finding (the qualitative claim that
  `i_inc` is the x-projection), promoted to a permanent gate protecting
  every future absolute-intensity citation from this instrument, not
  only this cycle's own numbers.

## T1 escape route

**N/A — diagnostic-only, matching exp-101's own precedent.** This is a
measurement-fidelity build on an already-committed, unmodified, passive
LTI article (the R4-family `graded_black_shell`, already locked
UNOBTANIUM-WITH-PARAMETERS by `REALIZABILITY_MEMO.md`). No mechanism
parameter (σ(I), σ(x,t), angular selectivity, sub-threshold operation) is
proposed, varied, or tested. If Prediction 1 below CONFIRMS (a genuinely
dark on-axis coherent field), that is evidence the *instrument* can
detect a real shadow, not evidence for or against any particular T1
escape route — the article under test is already known unbuildable.

## Predictions (falsifiable, committed before any FDTD call at Phase 3)

1. **On-axis coherent intensity ratio** `κ(θ) ∈ [0, 0.10]` at all 6
   angles, both configs (H_REGION-block reading). Grounded in the
   established near-total-absorption/large-`Q_ext` behavior of this
   exact article (exp-001's flagship anchor; exp-101's own `Q_ext`≈
   1.54–1.56 corrected reading) and the strong, near-field, essentially-
   geometric shadow such an optically large absorber casts at this
   bench's own standoff (T8's near-field caveat noted, not resolved).
   **Falsified** if `κ(θ) ≥ 0.10` at any resolved angle/config.
2. **Absolute-normalization self-consistency** (Gate C, restated as a
   scored prediction): `|I0_corrected(θ)·cos θ − i_inc(θ)| / I0_corrected(θ)
   ≤ 0.01` at all 6 angles. **Falsified** if the deviation exceeds 1% at
   any angle — would mean the local-plane-wave assumption behind the
   `1/cos θ` correction itself needs revisiting, not merely a display
   fix.
3. **Off-axis companion point** `κ_off(θ) ≥ 0.90` at all 6 angles, both
   configs — confirms the instrument resolves a spatially LOCALIZED dark
   region (the shadow) rather than a broadband dimming of the whole
   downstream half-plane, the minimum sanity check this new instrument
   needs before its on-axis reading is trusted as "a shadow" rather than
   "everything got dimmer." **Falsified** if `κ_off(θ) < 0.90` at any
   angle/config (a genuinely more troubling, differently-interesting
   finding, not merely a miss).
4. **Point-vs-region stability**: the single-nearest-cell `κ(θ)` and the
   `H_REGION`=10-cell-block-averaged `κ(θ)` at `P(θ)` agree to within a
   factor of 3× at all 6 angles — i.e., fringe/Fresnel-ringing
   sensitivity (VALIDATION.md's own paid-for lesson) does not make the
   single-point reading wildly discordant from the region mean.
   **Falsified** if any angle shows disagreement exceeding 3×, which
   would mandate the region-averaged reading as this instrument's ONLY
   trustworthy output going forward (single-point readings retired for
   this channel).

## Idealizations

- **Region-averaging is a small nearest-cell block, not a true
  beam-cross-section-perpendicular sample.** A disclosed simplification;
  Prediction 4 is the pre-registered check of whether this matters at
  all at these angles/this standoff.
- **The off-axis companion point uses a fixed lab-frame lateral offset at
  matching lab-frame x, not a beam-perpendicular rotation.** This is
  deliberate and disclosed: only the PRIMARY witness point needs to
  rotate with the beam (the defect this cycle exists to fix); the
  companion point is a coarse "is the darkening localized at all" sanity
  check, not itself a claim about the shadow's exact geometry.
- **Near-field standoff only (T8).** `D_STANDOFF`=200 cells sits deep in
  the shadow's near/Rayleigh zone (z/z_R≈0.04–0.06 range, same order as
  every prior R4-family box measurement) — these numbers describe this
  bench's own near-field geometry, not an asymptotic witness-scale claim;
  the r=78/156/312 bridge family (T8) governs any future extrapolation.
- **T9's Babinet-ceiling / near-field disclaimer applies to any citation
  of this article's own shadow depth as evidence of "how black a real
  coating gets"** — `graded_black_shell` at this shell thickness is
  already locked UNOBTANIUM-WITH-PARAMETERS (`REALIZABILITY_MEMO.md`
  Amendments 6–7, restated at exp-101 Result item 3); a buildable coating
  at this thickness would show a shallower, not deeper, on-axis darkening.
- **Amplitude-floor discipline, proactively applied (R13/R14 lineage).**
  `κ(θ)`'s denominator, `|Ez_empty(cell)|²` in a smoothly-tapered vacuum
  plane wave, has no known or plausible zero-crossing at these interior
  points (unlike R13's founding `delta_scene` case) — so no R13-style
  floor gate is structurally mandated — but a floor is applied anyway as
  house-style due diligence: any cell whose region-mean `|Ez_empty|²`
  falls below 10% of its own 12-cell-pool RMS (the same `FLOOR_FRAC`=0.10
  convention exp-088/exp-101 already use) is reported
  `UNRESOLVED-BY-CONSTRUCTION`, never silently scored.
- **Phase (`Δφ(θ)`) is reported diagnostically, not scored against any
  band.** Inside a genuinely dark region `|Ez|` is small and phase is
  numerically noisy; phase is useful qualitatively (confirming the
  darkness is destructive-interference-shaped, not merely "the incident
  field happens to be weak there"), not as a falsifiable prediction this
  cycle.
- **No perceptual/Weber-contrast scoring this cycle.** This instrument
  reports a raw coherent-field ratio and an absolute intensity fraction,
  not a witness-perceived contrast against `C_thr(L)` — that conversion
  (Tier 2 / the T3 build, exp-101's own corrected Next-item framing) is
  future work, out of scope here.
- **Single wavelength (600 nm), the two already-committed `R4_CONFIGS`
  only** — matching exp-101's own scope; a 450/750 nm leg is not
  proposed this cycle.
- **Exact `D_STANDOFF`/`H_REGION`/off-axis-offset cell counts are
  Phase-1 estimates; Phase 3 re-verifies every margin by direct `Sim`
  geometry computation** (`_verify_box_margins()`-style, per R17),
  not by hand-derivation, before any FDTD call.
- **Call budget (Phase-1 estimate, R19-style call/row distinction
  flagged for Phase 3):** 24 calls (6 angles × 2 configs × 2 conditions,
  the same R4-family leg exp-101 ran — deterministic, reproduced fresh
  since raw field captures are not persisted across experiment
  directories) + 2 new calls (Gate B's native-scale flagship, `θ=0°`,
  empty+article) = **26 real FDTD calls**. Gates A and C, and Prediction
  3's off-axis point, are zero-marginal-FDTD post-processing of the same
  26 captures.

## Why nothing here re-treads a RULED OUT item or a closed Live Thread

No item in LOGBOOK's RULED OUT registry (R1–R21) is re-proposed:

- **Not R1** (refractive/real-Δε cloaking) — no material or mechanism
  parameter is touched; the article is unmodified.
- **Not R5/R5-addendum** (unconstrained search + null-permutation
  requirement) — no named-constant search or dense combinatorial match is
  performed.
- **Not R13/R14** (ratio-classifier floor-gating) — addressed
  proactively above (Idealizations) even though this instrument's
  denominator has no known/plausible zero-crossing, the founding
  precondition for either rule's mandatory trigger.
- **Not R15** (cross-resolution boundary stability) — no resolution
  refinement or calibration boundary is built this cycle; Gate B's
  "known-good reproduction" requirement is this rule's own lineage
  applied prophylactically, not a resolution check.
- **Not R17** (uncalibrated bracket/tolerance) — `D_STANDOFF`/`H_REGION`/
  the off-axis offset are all justified against already-established
  scales (BOX_A's own clearance, `R4_R_OUT`, the established shadow
  diameter `2×R4_R_OUT`), not picked as illustrative round numbers; Phase
  3 re-verifies against real geometry before any run, per this rule's own
  remedy.
- **Not R20/R21** — this document makes no claimed-figure citation of a
  prior cycle's specific numeric result beyond what is quoted verbatim
  above (exp-001's 1.5–1.8%, exp-101's `Q_ext`≈1.54–1.56, `REALIZABILITY_
  MEMO.md`'s UNOBTANIUM-WITH-PARAMETERS verdict) — each independently
  checkable against its own cited source at Phase 5.

No closed Live Thread claim is re-litigated: **T9**'s Babinet-ceiling
disclaimer is restated, not contested; **T8**'s near-field caveat is
disclosed, not resolved; **T28**'s own `delta_scene`/R3-vs-R4 split
(Tier 1, exp-100/101) is untouched — this proposal does not read, cite,
or score `delta_scene`/`frac_contrast`/`ratio_k` at all. This IS the
instrument exp-101's own Next item 1 and LOGBOOK's Iteration-78 close
both explicitly commissioned, with both of that item's own named binding
preconditions (the `i_inc`/cos θ fix, the beam-rotating frame) addressed
above as load-bearing design choices, not afterthoughts.
