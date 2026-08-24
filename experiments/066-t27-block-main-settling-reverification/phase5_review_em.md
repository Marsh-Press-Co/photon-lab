# Phase 5 Review — ELECTROMAGNETISM seat, Panel Iteration 43 (exp-066)

*Fresh sub-agent, blind to the other five seats' Phase-5 reviews this
cycle. Preserved verbatim as delivered.*

## 0. Independent verification performed

I re-derived every headline number in `phase4_results.md` directly from
`results.json` rather than trusting the prose:

- **P-066-G1** (18-cell bit-exact identity gate): confirmed,
  `max_abs_delta=0.0` across all 18 `{36,37,39}°×{±}×3λ` cells at
  STEPS=1400 against exp-041's committed `block_main`.
- **P-066-1/P-066-2**: recomputed `|ΔC(2800−1400)|` and sign-flip count
  myself from `block_g1ext`/`block_main2800`'s raw rows — median
  0.005766909912278462, max 0.009574688227676709, 3/18 flips. Matches the
  report exactly.
- **Closure-summary GATE_HARD table**: recomputed pass/fail counts
  directly from the 36-row `closure_summary` array — **31/36 fail at
  STEPS=1400, 34/36 fail at STEPS=2800**, with exactly the 5 bucket-flip
  cells listed (4 PASS→FAIL, 1 FAIL→PASS at +38°/600nm). Matches exactly,
  cell-for-cell.
- **P-066-3a/3b**: `delta_4200_2800`/`delta_2800_1400` ratios reproduce
  the claimed 0.0098% and 0.00072% figures exactly from the raw
  `C_1400/2800/4200` fields.
- **P-066-4 fringe refit**: `sign_agree` 30/30 (was 27/30), `r2_cstar`
  0.8270797090069711 (was 0.7852421354715854, Δ=+0.0418) — inside the
  ±0.10 band, matches.

I did not find a single load-bearing number in `phase4_results.md` that
doesn't reproduce bit-for-bit from `results.json`. No R4-class violation
here.

## 1. Does the data actually support P-066-3a/3b's settling-generalization claim, and is the GATE_HARD-fails-increase finding electromagnetically sound?

**The two stress-test numbers are genuinely decisive at the two points
they test.** `|ΔC(4200−2800)|/|ΔC(2800−1400)|` = 0.0098% at 40°/750nm and
0.00072% at 37°/600nm — both 100–1000× inside their 1%/5%
CONFIRM/REFUTE bar. Combined with exp-065's own pre-existing 40°/600nm
point, this cycle now has **three** directly convergence-tested (θ,λ)
coordinates (not one), and all three plateau hard by STEPS=2800.

**I independently re-derived the causal-transit arithmetic my own Phase-2
critique got wrong, and Red Team's correction is right.** From
`lab/fdtd2d.py`: `ramp = int(ramp_periods * lam / S)` with
`ramp_periods=3.0` (line 133/180) and `S = courant_frac/√2 = 0.99/√2 ≈
0.70004` (line 78). At 750nm (cpl=25): ramp = int(3.0×25/0.70004) = **107
steps**, exactly as claimed. `TRANSIT_STEPS = R_EDGE/S = 784.4/0.70004 ≈
1120.5 steps` (exp-042's own established `R_EDGE=784.4`). Ratio =
1120.5/107 ≈ **10.47×** — one order of magnitude, not two. My original
Phase-2 attack was arithmetically wrong by a factor of ~10; Red Team's
audit and this cycle's `SETTLING_MECHANISM_NOTE` correct it accurately.
Good self-correction on this program's part.

**On the GATE_HARD 31→34 finding — yes, this has a clean electromagnetic
explanation, and it is the correct one, though the document doesn't frame
it in these terms.** The empty-scene channel is a fully passive, linear,
time-invariant system (vacuum interior + lossy graded-damping bands at
all four domain edges, cubic conductivity ramp — confirmed by reading
`_damping()` in `fdtd2d.py`, applied on all four boundaries, not just the
propagation axis). Passivity guarantees the CW-driven transient decays to
a **unique, generally nonzero** periodic steady state — there is no
physical principle under which that steady-state value should trend
toward zero as settling completes. `GATE_HARD=0.001` was calibrated as a
decision-floor gate against an *assumed*-small residual, not against a
known physical target; the T21 mechanism this program already
established (a genuine Huygens edge-diffraction fringe from the finite
taper, period 1.4–2.5°, native amplitude order 10⁻³–10⁻²) means the true
converged `C_empty(θ,λ)` was never expected to be near zero at most of
these grazing angles. The STEPS=1400 reading is not "the true small value
corrupted by noise" — it's a large-amplitude transient (74–89% of the
settled magnitude at several cells) riding on top of the true fringe,
which by chance cancels the fringe at some phase points (spurious PASSes)
and reinforces it at others. `phase4_results.md`'s own disclosure — 3 of
4 newly-failing cells were STEPS=1400 near-zero-crossing points that
"turn out to be genuinely larger once settled" — is exactly this
mechanism, independently reproducible from the raw numbers (I checked:
e.g. −39°/450nm goes from −3.02×10⁻⁵ at 1400 to +3.37×10⁻³ at 2800, a
sign flip through near-zero). **This is consistent with, not contrary to,
my charter's passivity bookkeeping**, and the write-up's own framing
("the settling correction makes the floor look worse... the opposite of
an 'unsettled=noisy' prior") reaches the right qualitative conclusion, if
without naming the underlying passivity argument explicitly.

## 2. Argue the next change — ranked top-3 EM-discipline candidates for Iteration 44

**1. Test convergence at 450nm — the one wavelength with zero direct
multi-STEPS convergence data anywhere in this record.** Both this cycle's
stress cells (750nm, 600nm) and exp-065's own original point (600nm) skip
450nm entirely, which is also the coarsest grid (`cpl=15` vs 20/25) and
therefore carries the worst Yee-grid numerical dispersion — the one place
where the "round-trip ringdown time in raw STEPS is θ,λ-independent"
assumption (built on the continuum group velocity `S`) is most likely to
break down, since numerical dispersion perturbs the *effective*
propagation speed away from `S` most at coarse `cpl`. A single
1400/2800/4200 convergence triple at, e.g., 40°/450nm (already has a
1400-step anchor) would close this gap at near-zero cost.

**2. Re-target the θ-generalization check to the most-grazing untested
interior angle, not the least-grazing one.** Mandatory fix B tested
37°/600nm — the *least* oblique of the three genuinely new interior
angles. Physically, a cubic-ramped (non-PML) graded absorber's residual
reflectivity generically worsens toward grazing incidence — the boundary
bands sit on all four domain edges (verified directly in `fdtd2d.py`'s
`_damping()`), and steered CW illumination reflecting off the y-boundaries
at a shallower angle traverses less effective lossy depth per bounce. If
ring-down time grows with angle, 37° is the wrong point to bound the
worst case with — 39° or 40° (the most-grazing cells still lacking their
own independent convergence check beyond the single 40°/600nm anchor
point) would test the direction the physics actually predicts might fail.
Concretely: a 1400/2800/4200 triple at 39°/450nm would jointly stress the
worst-λ and worst-θ axes at once, closing #1 and #2 in a single call.

**3. Replace ad-hoc extrapolation with an actual predictive model of the
boundary's angle/frequency-dependent residual reflection.** This program
has repeatedly favored building a zero-FDTD-cost analytic propagator once
an empirical pattern is found (`chord_model_g0`, `edge_diffraction_c_
empty`) rather than re-measuring piecemeal. A WKB/adiabatic-taper
estimate of the cubic damping profile's residual reflection coefficient
vs. angle of incidence, checked against the now-4 empirical convergence
points on record (40°/600nm, 40°/750nm, 37°/600nm, and whatever #1/#2
add), would let future cycles *predict* which (θ,λ) cells need STEPS
beyond 2800 instead of discovering them one point at a time — directly
answering the open question this cycle's own `SETTLING_MECHANISM_NOTE`
raises but declines to adjudicate.

(PLAN.md's own standing Iteration-43 item #2 — complete STEPS=2800 for
the interior `FALLBACK_ANGLES` and Block ARTICLE's article-present legs —
remains valid and is not superseded by the above; I rank the three above
it because they are the specific gaps my own charter's causality/
passivity lens surfaces, not because #2 is unimportant.)

## 3. Verdict: **PARTIAL**

Not PROMISING: no constraint metric is touched (T1 escape route correctly
disclosed as NONE), and the settling-generalization claim, while now
measurably stronger, still rests on only 3 of 36 mandate-scope cells with
direct multi-STEPS convergence evidence — the other 33 are extrapolated
on a physical argument (fixed domain geometry ⇒ θ,λ-independent ring-down
time) that is plausible but untested at its own most-adversarial
coordinates (grazing θ × coarse-grid λ).

Not RULED OUT: nothing here forecloses a mechanism class or shows a
jointly-unsatisfiable constraint set — this is pure instrument-fidelity
work, and it genuinely advances the record: my own Iteration-42 sharpest
attack (zero interior-angle convergence testing) is now partially but not
fully answered — there is real evidence along both axes for the first
time, at large margins, where before there was none.

## 4. Over-claims / under-disclosures / errors in `phase4_results.md`

- **Not a substantive over-claim, but a self-containedness gap**:
  `phase4_results.md` calls P-066-3a/3b "the single most decisive numbers
  in this run" without restating, in the same document, that they license
  generalization from only 3 of 36 cells. `NOTES.md`'s idealizations
  section states this clearly ("three of the program's 36 mandate-scope
  cells directly convergence-tested; the remaining 33 are extrapolated"),
  so it is disclosed *somewhere* in the committed record — but a reader
  who only reads `phase4_results.md`'s headline table could reasonably
  come away thinking the generalization question is more closed than the
  idealizations section admits. Worth a one-line cross-reference at
  Iteration 44.
- **No arithmetic errors found.** Every number I independently recomputed
  from `results.json` matched the prose exactly.
- **P-066-4's causal-language discipline is correctly maintained.** I
  checked this specifically given the exp-065 precedent (`P-VIS42-10`'s
  self-caught unfalsifiable-claim defect) — `phase4_results.md`'s own
  text on the c* shift (1.62→0.87) is properly hedged ("consistent with,
  not proof of... this cycle does not adjudicate that reading"), and the
  `FRINGE_FIT_STATISTICAL_ONLY_NOTE` tripwire is present and correctly
  worded in both `results.json` and `design_geometry.py`. No regression
  of the mandatory fix C discipline.
- **The GATE_HARD 31→34 framing is correct but under-argued from first
  principles** — see §1 above; the document reaches the right conclusion
  empirically without stating the passivity argument that makes it a
  *predictable* result rather than a surprising one. Not wrong, just
  thinner than it could be.

**Files reviewed**:
`/home/user/photon-lab/experiments/066-t27-block-main-settling-
reverification/{phase1_proposal.md,phase2_critique_em.md,phase2_redteam_
audit.md,phase3_synthesis.md,NOTES.md,phase4_results.md,design_geometry.
py,results.json}`; `/home/user/photon-lab/experiments/042-t21-magnitude-
bridge/design_geometry.py`; `/home/user/photon-lab/lab/fdtd2d.py` (lines
73–260 for `S`, `ramp`, `_damping`); `/home/user/photon-lab/LOGBOOK.md`
(RULED OUT, ESTABLISHED, LIVE THREADS T1–T27 in full, Iteration 42 in
full); `/home/user/photon-lab/PANEL.md`; `/home/user/photon-lab/PLAN.md`
(current-state + Iteration-43 queue);
`/home/user/photon-lab/lab/validation/VALIDATION.md`.
