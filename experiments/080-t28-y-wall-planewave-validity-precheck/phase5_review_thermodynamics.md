# PHASE 5 — REVIEW · THERMODYNAMICS · Panel Iteration 57 · exp-080

*Fresh sub-agent, blind to the other six seats' Phase-5 reviews this cycle.
Read, in order: `PANEL.md` in full, `AGENTS.md` in full,
`experiments/080-.../phase1_proposal.md` (incl. PHASE 1 RESULTS),
`validity_precheck.py` as it now stands (post-Phase-3 fold-in),
`validity_precheck_results.json`, all five Phase-2 critiques,
`phase2_redteam_audit.md`, `phase3_synthesis.md`, `phase4_results.md`,
`_output.txt`. All numbers below marked "independently reproduced" were
computed in fresh scratch scripts that import only `dg065`/`br`/`ywas`
primitives directly — never by calling `validity_precheck.py`'s own
functions and never copied from any prose in the record.*

**No RULED-OUT item (R1–R9) is re-proposed or re-litigated here.**

---

## Verdict on the whole cycle: **PARTIAL — concur with the record's own Combined Verdict**

This is a clean cycle by this program's own R4 standard. Every load-bearing
number I re-derived from primitives — part (a)'s geometry, part (c)'s
power-budget table, and part (d)'s PHOTONICS-image-term construction —
reproduces exactly. I find no arithmetic defect anywhere in the finished
record. My own contribution below is two genuine, independently-derived
findings that sharpen (not reverse) two of the three items I was asked to
examine, plus confirmation that the third (part (c)'s own numbers) is
correct as filed.

---

## 1. Independent re-verification of `part_c_power_budget_at_true_angle()`

Recomputed `|r(90°−θ_beam)|²` from scratch — a fresh script importing only
`br.n_profile_exact`/`nu_profile`/`damp_e_profile`/`CPL`,
`ywas.reflection_coefficient_vec`, and (as a second, independent
cross-check) `br.reflection_coefficient` itself (the un-vectorized scalar
function, called pointwise) — never calling `validity_precheck.py`'s own
`part_c_power_budget_at_true_angle()`:

| ABSORB | my `r²` min | my `r²` max | file's `reflected_power_fraction_min/max` | match |
|---|---|---|---|---|
| 40 | 2.482220e-04 | 1.494322e-03 | 2.482220e-04 / 1.494322e-03 | **exact** |
| 60 | 6.357808e-06 | 5.114969e-05 | 6.357808e-06 / 5.114969e-05 | **exact** |
| 70 | 9.371953e-07 | 1.315569e-05 | 9.371953e-07 / 1.315569e-05 | **exact** |
| 80 | 4.099449e-08 | 3.569215e-06 | 4.099449e-08 / 3.569215e-06 | **exact** |

Cross-checked a third way at the exact three θ_beam points THERMODYNAMICS'
own Phase-2 critique table used (36°/39°/42°, all four ABSORB depths) via
the scalar `br.reflection_coefficient` (not the vectorized function
`part_c` uses) — every one of the 12 cells matches to the printed digit.
**`part_c`'s own numbers are correct, bit-exact, verified from primitives a
third independent time** (after THERMODYNAMICS' own Phase-2 critique and
Red Team's Phase-2 audit item 5). Also independently reproduced
`part_d_photonics_construction()`'s full table (raw and scale-corrected R²,
both proxies, all 5 configs) from a from-scratch reimplementation of the
integral — bit-identical to the committed JSON and to Red Team's own §0
item 8 (4+ decimal places on every entry). No new discrepancy found
anywhere in this record.

---

## 2. Is `phase3_synthesis.md`'s explanation of the two `|r|²` scales correct and complete?

**Correct as far as it goes.** `theta_eff` (part b) is a purely geometric,
θ_beam-independent bounce angle (~8°, near the wall's own normal — the
amplitude-weighted summary of the true `theta_local(y_s)∈[5.3°,15.0°]`
envelope), while `90°−θ_beam` (part c/d) is a much larger angle from
normal (48°–54°, near grazing). I independently confirmed the physical
direction of the gap is sound, not an artifact: sweeping `|r(θ)|` across
0°–89° for every ABSORB depth shows a monotonic climb toward grazing
incidence at every depth (e.g. ABSORB=80: `|r|=2.6e-8` at θ=0° rising to
`|r|=0.91` at θ=89°) — ordinary lossy-boundary Fresnel behavior. The two
JSON quantities are legitimately different physical numbers, not a
mislabeled duplicate or a residual sign of the earlier `theta_beam`/
`90-theta_beam` convention bugs this exact sub-thread has already twice
been burned by (exp-078/079).

**But it is not complete, and my own charter is exactly the seat that
should say so.** Both `|r(theta_eff)|²` (~1e-13–1e-8) and
`|r(90°−θ_beam)|²` (~1e-8–1.5e-3) are properties of the **wall material
alone at an assumed incidence angle** — they answer "what fraction of
power *striking the wall at this angle* comes back," never "what fraction
of the total power reaching the observer is actually carried by this
echo path at all." That second question is what an energy-budget
sidecar actually needs to say anything about constraint 3, even
qualitatively — and neither part supplies it, nor does anything else in
`validity_precheck.py`. Two independent facts already sitting in this
sub-thread's own record show why the gap matters:

- `photonics_image_term_curve()`'s own docstring (fix-docket item 5, rated
  LOW by Red Team and left open by Phase 3) discloses that
  `E_direct(θ_beam)` — the un-reflected, directly-transmitted field that
  presumably dominates whatever an observer actually sees — is **omitted
  entirely**, "valid only insofar as it cancels identically across
  congruent-config pair deltas... flagged, not resolved." That framing
  treats the omission as a possible *bias on the period fit*. It is also,
  separately, the reason nobody in this eight-cycle T28 y-wall sub-thread
  has ever normalized `E_echo`'s own magnitude (`primary_model_curves`:
  `Re{E_echo}∈[-7e-6,+8e-6]`, config C40, arbitrary analytic field units)
  against ANY physically calibrated total-signal scale.
- The one place this program has compared a model's variance against a
  *real, FDTD-measured* scale — exp-079's `ss_tot_sanity`
  (`ratio_model_to_real=9.4e-7`) and Iteration 55's `5.9×10⁻²⁷` figure —
  compares variance **of the θ_beam-dependent shape**, i.e. "does the
  model wiggle at all relative to how much the real data wiggles." It does
  not, and cannot, answer "if this model's period matched perfectly, would
  the resulting brightness modulation even clear a Weber-contrast floor,"
  because that requires an absolute (or at least beam-relative) power
  ratio, not a shape-variance ratio.

**The missing third quantity, stated concretely**: a calibrated
`|E_echo(θ_beam)|² / |E_total(θ_beam)|²` (or, failing a real `E_direct`
term, even a crude upper bound using the aperture's own total radiated
power as the denominator) — the actual fraction of scene brightness this
mechanism could contribute, as opposed to the wall's own local
reflectivity. This is a different question from fix-docket item 5's own
framing (whether omitting `E_direct` biases *which period* gets fit) — it
is whether this entire construction family could ever be large enough, in
absolute terms, to matter to constraint 3 regardless of period accuracy.
Given part (a)'s own FORECLOSE finding (the aperture never presents a
clean angle to the wall, dist_ratio ≤2.15% of Fraunhofer) and part
(c)/(d)'s own `|r|²` ceiling (≤0.15% even at the least-absorbing depth,
the most-grazing angle sampled), a back-of-envelope upper bound is already
implicit but never stated as such: even a wall that intercepted 100% of
the aperture's radiated power could return at most ~0.15% of it at
ABSORB=40 — before any geometric coupling factor (how much of the
aperture's power actually travels toward this wall at all, presumably far
less than 100%) is even applied. That two-step bound (material reflectivity
× geometric interception fraction) is the actual energy-budget question
constraint 3 needs, and this cycle prices only the first factor.
**Recommend**: fold this into Iteration 58's queue as an explicit item,
distinct from and prior to fix-docket item 5 — before scoring
`photonics_image_term_curve()`'s periods against real T28 data (Iteration
58 queue item 2), also price whether the resulting amplitude, once
scaled to match a period, would require an implausible geometric
coupling fraction to reach a detectable brightness modulation.

---

## 3. Is the shared C70/C80 concentration in part (b)'s `R²(abs)` and part (d)'s scale-corrected `R²` a genuine physical link, or coincidence?

**Genuine, independently confirmed physical link — not coincidence and not
a shared-code artifact.** I swept `|r(θ)|` across both angular regimes
each construction actually uses and measured the swing (max/min) at every
ABSORB depth, using a fresh 200-point grid per regime (not the 3–4 spot
points either prior critique sampled):

| ABSORB | `\|r\|` swing, near-field envelope [5°,15°] (part b's regime) | `\|r\|` swing, far/grazing [48°,54°] (part d's regime) |
|---|---|---|
| 40 | 1.305× | 2.454× |
| 60 | 2.205× | 2.836× |
| 70 | **7.521×** | **3.747×** |
| 80 | **9.189×** | **9.331×** |

Both regimes independently show the same monotonic trend: ABSORB=70/80
carry the largest `|r(θ)|` swing across the relevant angular span, by a
wide margin over 40/60, **in two structurally unrelated angle windows**
(one near the wall's own normal, one near grazing). My near-field-column
numbers cross-check THERMODYNAMICS' own Phase-2 critique table (which
sampled only 4 points in that one regime) essentially exactly
(ABSORB=70: `5.7e-7→4.3e-6`, my continuous sweep: `5.74e-7→4.31e-6`) — but
the far-regime column is new: nobody in this cycle's record checked
whether the SAME swing pattern holds where part (d)'s construction
actually operates, since part (d) (QUANTUM's construction) and
THERMODYNAMICS' swing table were computed independently, blind to each
other, in the same Phase 2 layer, and neither Phase 3 nor Red Team's audit
connected them.

**Why this is a real shared driver, not two coincidentally-aligned
curve-fitting accidents**: both `single_angle_curve()` (part b) and
`photonics_image_term_curve()` (part d) share the identical mathematical
operation — pull a single, y_s-independent complex scalar `r_const`
outside the aperture integral, leaving the *shape* fixed and letting
`r_const` only rescale/rotate it. The fidelity of that operation is
governed by exactly one thing: how much the TRUE `r(θ)` varies across
whatever angular span the true per-point model actually visits. That is a
property of `boundary_reflectance.py`'s own admittance profile — not of
either summarization scheme. I also confirmed the underlying cause is
physically sensible, not a numerical artifact: `n_profile_exact` at every
ABSORB depth shares the identical peak `|Im(n)|=1.364116`, but the
imaginary part is spread over more grid cells as ABSORB deepens (`n[-1]`
imaginary part shrinks from `2.1e-5` at ABSORB=40 to `3e-6` at ABSORB=80) —
i.e. the SAME total loss is stretched over a longer, more gradual
impedance transition at larger ABSORB. A longer graded-index transition
accumulates more optical phase per degree of incidence-angle change (the
same physical reason a thicker interference film is more angularly
dispersive than a thin one), which is exactly what produces a more
angularly sensitive `r(θ)` — and that mechanism has no reason to be
confined to one angular window, which is why it shows up in both.

**Bottom line**: this is a property of the wall admittance model
itself, discovered independently in one regime by THERMODYNAMICS' own
Phase-2 critique and now confirmed to hold in the other regime as well —
answering the "open, unexplained" status Red Team's Attack 4 and Phase 3
both explicitly left standing. Any future single-angle or few-angle
summarization of this exact `ABSORB` sweep (not just these two
constructions) should expect its worst fidelity at the deepest boundary
depths, for this reason, not by chance.

---

## 4. Anything else, from the energy-accounting lens

Nothing else load-bearing. `part_b_realizable()`'s REFUTE-range concentration
at `ABSORB=40` (not 70/80) is a *different* fragility — an admittance-family
divergence (`MATERIALS`' own `89.08°` `arg(r)` deviation finding), not the
angular-dispersion mechanism above — and I confirm it should stay filed
separately, as the record already does; conflating the two would be a new
error this review does not want to introduce. Gates: zero `lab/` diff,
confirmed; house trust suite green, no re-run required (unchanged from
Phase 3/4). Checkpoint criteria: I concur with the record's own ruling
(criteria 1/3 N/A, criterion 2 NOT YET RIPE, criterion 4 does not fire,
criterion 5 not at risk) — nothing in my own review changes any of these.

---

## Summary for Iteration 58's queue

Add, alongside the record's own four queue items (`phase3_synthesis.md`
§6): **price the geometric-interception × material-reflectivity energy
budget** (§2 above) before or alongside scoring `photonics_image_term_curve()`
against real T28 periods — a cheap, still-zero-FDTD calculation that would
tell the program, for the first time in this eight-cycle sub-thread,
whether the coherent-echo mechanism class could ever be large enough in
absolute terms to matter to constraint 3, independent of whether its
period ever matches. And carry forward, as a now-confirmed (not merely
suspected) fact rather than an open question: the ABSORB=70/80
concentration of failure in both `R²(abs)` proxies is a real property of
`boundary_reflectance.py`'s own admittance profile's angular dispersion,
confirmed in two independent angular regimes — not a coincidence, and not
specific to either construction that exposed it.
