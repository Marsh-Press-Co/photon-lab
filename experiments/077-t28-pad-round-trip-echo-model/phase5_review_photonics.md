# PHASE 5 — REVIEW · PHOTONICS · Panel Iteration 54 · exp-077

**Seat: PHOTONICS** (surface interaction, absorption spectra, angular
dependence, scattering cross-sections). Fresh context, blind to the other
six seats' Phase-5 reviews. Read `PANEL.md` in full, `LOGBOOK.md` lines
1–270 (RULED OUT R1–R8) and 1892–2461 (T28's full Iteration 46–53
history), and the complete exp-077 record (`phase1_proposal.md` as edited
in place, `phase2_redteam_audit.md`, `phase3_synthesis.md`,
`phase4_results.md`, `NOTES.md`, `pad_round_trip_model.py`,
`pad_round_trip_results.json`, plus `two_wall_cavity.py` and
`experiments/065-.../design_geometry.py` to check the physics
independently).

## 1. Verdict: **PARTIAL**

The instrument itself is sound and I independently reproduce its headline
numbers exactly (§2). But this seat's own charter question — *is the
proposal's optical response coherent as stated, across wavelength and
angle* — is not fully answered by a 600°-of-angle, one-wavelength REFUTE.
Two things I found independently (§2, §3) mean the correct reading is
"the tested x-wall coherent-echo mechanism is REFUTEd; the broader class
of coherent-boundary-echo mechanisms is not yet excluded," not "no
coherent-echo mechanism survives." That is PARTIAL, not RULED OUT, and
the REFUTE itself is real and well-earned, so it is not PROMISING either.

## 2. Independent verification performed

**(a) Test A/B reproduction, both cuts, from the committed JSON — exact
match.** I read `pad_round_trip_results.json` directly (not the prose)
and confirm: single-wall `rel_dev=1.879755`/`r²=0.044401` (PAIR_PAD),
`0.964154`/`0.199662` (PAIR_ABSORB40); two-wall
`rel_dev=0.879678`/`r²=0.0000941` (PAIR_PAD), `0.685089`/`0.041757`
(PAIR_ABSORB40). All four combined verdicts (REFUTE/REFUTE) reproduce.
The null-calibration appendix (`P(R²≥0.70)=0.0` over 20,000 pure-noise
trials, real `R²=0.8165`) also reproduces exactly.

**(b) Shape mismatch, inspected point-by-point, not just as a scalar
r².** I pulled `thetas`/`real_delta_pad`/`pred_two_wall_delta_pad` from
the JSON and counted zero-crossings over the 36–42° window: the real
curve crosses zero **3 times** (≈36.5°, 38.8°, 39.9°), the two-wall model
crosses **2 times** (≈37.3°, 39.9°) — the model completes roughly 0.7
cycle over the window where the real data completes roughly 1.3. This is
a directly visible, physically legible version of `r²≈0.0001`: the two
curves are not just weakly correlated, they are oscillating at
genuinely different rates over the same span, corroborating REFUTE
independent of the correlation statistic.

**(c) NEW — I ran the identical two-wall model against the
already-collected 750 nm leg (`experiments/076/results.json::
leg750_scored`), which exp-077 itself declared out of scope
(Idealization 11).** Zero new FDTD, zero new machinery — same
`boundary_reflectance.py`/`two_wall_cavity.py` imports, `CPL[750]=25`
substituted for `CPL[600]=20`, scored against `G40−C40` over the 16-point,
38.0–41.0°, 0.2° leg already sitting in exp-076's own `results.json`.
Result:

| | 600nm two-wall (filed) | 750nm two-wall (this check) |
|---|---|---|
| Test A `rel_dev` | 0.8797 → INCONCLUSIVE | **0.0873 → well inside SUPPORT (≤0.30)** |
| Test B `r`, `r²` | +0.0097, 0.0001 → REFUTE | **−0.5004, 0.2504 → INCONCLUSIVE (sign flips)** |
| Combined | REFUTE | **INCONCLUSIVE** |

This is a real, outcome-relevant finding, but I am not filing it as a
counter-REFUTE without the same caveat exp-076's own record already
attached to this exact dataset: the leg750 window is only 3° wide at 16
points (≈1 period of the signal at best), and both the real and model
curves fit a 4-parameter free sinusoid at `R²=0.988`/`0.979` — suspiciously
high in a way that is a classic symptom of an under-constrained fit on a
window barely wider than one cycle, not evidence of a strong periodic
match. exp-076's own record already flags this leg "advisory... NOT
decisive, does not license any wavelength-general citation." **No
null-calibration exists for this narrow window** (the 20,000-trial
appendix this cycle built is scoped to the 6°/31-point 600nm window
only). So my honest conclusion is: **the committed record's choice to
call this out of scope (Idealization 11) is exactly the kind of
"affordable, already-named check" this program's own R8 rule was written
to stop from surviving un-run once it is shown outcome-relevant** — it
is now shown outcome-relevant (the qualitative picture changes), so it
should not stay deferred past Iteration 55.

## 3. What the six-cycle sub-thread's own record may be missing

**A genuinely new, unmodeled coherent-boundary-echo candidate: the
y-direction (transverse) absorbing walls.** `lab/fdtd2d.py::Sim._damping`
applies the identical `self.absorb`-parameterized cubic ramp to **all
four domain edges** — this cycle's own `verify_symmetric_damping` only
checked the two x-edges, but the same code (`d[:, :self.absorb]`,
`d[:, -self.absorb:]`) puts the identical admittance class on the y=0 and
y=ny−1 edges too. I checked `design_geometry.py::CONFIGS` directly:

| | `C40` | `G40` | `C80` |
|---|---|---|---|
| `clear_span_y` (aperture edge → y-band inner edge, cells) | 0 | **40** | 0 |
| `clear_plane` (x: plane → −x band inner edge, cells) | 37 | 77 | 37 |

`clear_span_y` tracks `PAD` exactly the same way the x-wall round-trip
distances do (+40 cells for `G40` relative to both `C40` and `C80`) — a
real geometric fact invisible to `pad_round_trip_model.py`'s own 7-field
congruence assertion (`nx,ny,src_x,plane_x,obj_x,obj_y,d_sp`), none of
which include `clear_span_y`. This means **`PAIR_ABSORB40 ≡ (G40,C80)`,
which this cycle and exp-076 both treat as "geometry-fixed, ABSORB-only,"
is not fully geometry-fixed in the y-direction** — `G40` has a 40-cell
standoff from its own y-absorbing band that `C80` does not. The
boundary-*free* aperture-diffraction part of the model is unaffected
(`boundary_free_spread_internal_check=0.000e+00`, confirmed this cycle —
the aperture edges themselves, at `y_lo`, are held congruent), but a
coherent *echo* off the y-band, if one exists, would not be. Neither the
single-wall nor the two-wall model computes any such term — both only
ever image the source through x=0 / x=nx−1.

This is not merely a hypothetical: `design_geometry.py::
causal_identity_step` (exp-065, Iteration 42) already names exactly this
path — "(iii) source → (y) band inner edge → nearest scored window
cell" — as one of the causal-exclusion terms it computes, and that same
document's own `[4]`/`[4b]` sections found the **dynamic causal gate VOID
at the C40/G40 geometry** (the corrected 1-cell/step bound, n=247, is
*less* than the direct source→plane arrival time, 319 steps) — replaced
by a *static* vacuum-construction check, which proves the padded region
is empty at t=0 but says nothing about whether a wave that has actually
propagated for `STEPS=2800` could have reflected off a y-band and
returned coherently to the scored window. **Nothing in this six-cycle
sub-thread has ruled that in or out.** Given both the ABSORB-boundary
class (exp-075) and the x-wall PAD-echo class (this cycle) are now
REFUTEd, this is a structurally distinct third candidate — same
unrealizable admittance class (so it inherits MATERIALS' bound
unchanged), but a different wall, different path geometry, and a
different, not-yet-computed period — worth a Red Team reckoning before
anyone reads "no coherent-echo mechanism survives" into the record.

## 4. Ranked candidates for Iteration 55 (PHOTONICS' own view)

1. **Build the y-wall (transverse) coherent-echo model.** Same
   `boundary_reflectance.py` r(theta;ABSORB) and `dg048.field_and_h`
   Huygens-Fresnel machinery already vetted three cycles running — just a
   new image geometry (reflect through y=0/y=ny−1 instead of x=0/x=nx−1),
   scored on the same already-collected `PAIR_PAD`/`PAIR_ABSORB40` 600nm
   data. Zero new FDTD. The one candidate this record has not yet run,
   and the `clear_span_y` finding above (§3) gives it a concrete,
   PAD-tracking reason to be live rather than a shot in the dark.
2. **Gate the 750nm cross-check properly before treating it either way.**
   Add a null-calibration control sized for the leg's own 16-point/3°
   window (permutation or circular-shift, the same discipline the 600nm
   window already got) to my §2(c) spot-check. If the INCONCLUSIVE result
   survives calibration, the 600nm-only REFUTE should carry an explicit
   wavelength-generality caveat it does not currently have; if it doesn't
   survive (i.e. the window is too underpowered to mean anything), that
   itself is worth stating plainly rather than leaving Idealization 11
   silently deferred.
3. **Test whether a multi-bounce (not single-echo) treatment of the
   `ABSORB` band changes the period materially.** `r(theta;40)`'s own
   phase swings ~77° across just the 6° window (arg −78.12°→−1.23°,
   36°→42°, confirmed from this cycle's own §2e table) — a rate
   comparable to the round-trip fringe's own phase advance. The
   single-echo idealization (inherited unchanged from exp-075, item 5 of
   the carried-over list) has never been tested against a real multiple-
   internal-reflection treatment of the graded band itself; given how
   fast `r`'s own phase moves, that idealization is less obviously safe
   here than it looked when first stated.

## Compliance note

No RULED OUT item (R1–R8) is re-proposed. The y-wall nomination in §3 is
a new instance of the *already-permitted* coherent-echo class (same
matched-`eps=mu` admittance, same MATERIALS unrealizability bound per
this cycle's own Idealization 10) applied to a wall neither exp-075 nor
exp-077 modeled — not a resurrection of anything closed. The 750nm
spot-check in §2(c) is explicitly filed as a finding requiring its own
null-calibration (R5's own discipline), not as a stand-alone claim.
