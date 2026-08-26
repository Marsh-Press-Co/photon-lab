# PHASE 2 — CRITIQUE · PHOTONICS · Panel Iteration 54 · exp-077

*Blind critique, PHOTONICS charter: surface interaction, absorption
spectra, angular dependence, scattering cross-sections. Owns: is the
proposal's optical response coherent as stated, across wavelength and
angle?*

---

## 1. Steel-man (≤150 words)

This is a clean, zero-cost stress test of the one mechanism class exp-076's
own lossless-vacuum proof still permits for `PAIR_PAD`. It reuses the
triply-gated (`G-LOSSLESS`, `G-N1`, `G-PASSIVITY`) transfer-matrix machinery
unchanged and applies it to the physically decorrelated pair the queue
named. I independently re-ran `pad_round_trip_model.py` and reproduced
every headline number bit-for-bit (`rel_dev=1.8798`, `r²=0.0444` for
`PAIR_PAD`; `0.9642`/`0.1997` for `PAIR_ABSORB40`). I also built the check
the proposal's own Idealization 9 names but does not run — retargeting
exp-075's already-built `two_wall_cavity.py` at `(C40,G40,C80)` — and found
it does **not** rescue the mechanism: `PAIR_PAD`'s shape match actually
collapses further (r²: 0.044→0.0001). The single-wall REFUTE is, on this
evidence, a robust negative result, not a cherry-picked one.

## 2. Sharpest attack (≤150 words)

The proposal asserts REFUTE while disclosing, but not running, the
already-built two-wall check (§6 idealization 9: "if Phase 2/3 flags this
REFUTE as premature... the two-wall extension is available immediately").
That is exactly the R8 failure shape (LOGBOOK Iteration 52, exp-075): an
unverified robustness claim standing in for a named, affordable check. I
ran it: Test A improves to INCONCLUSIVE (rel_dev 1.88→0.88) but Test B
collapses to r²=0.0001 (from 0.044) — Combined stays REFUTE, but the
*control* pair `PAIR_ABSORB40` flips INCONCLUSIVE→REFUTE too, meaning the
two-wall model is *less* internally consistent than the single-wall one,
not more. Separately: `r(theta;40)`'s phase drifts ~77° across the 6° grid
(nu/omega reaches 1.36 near the wall, Re(n²) as low as −0.86 — a
near-metallic, not dielectric, regime) — the model curve isn't close to a
single sinusoid, so "P*=13.28° well-determined" (§5) overstates what a
free-period fit to a chirped curve actually establishes.

## 3. Verdict

**support-with-changes.** The `PAIR_PAD` REFUTE appears to survive the
single-wall idealization's own worst case (I tested it), so the headline
conclusion is credible — but the document should not have asserted REFUTE
as final while an affordable, already-built, named check sat unrun. That
gap must close before this cycle's REFUTE is treated as settled record,
matching this program's own standing R8 discipline.

## 4. The one change that would flip my verdict

Execute and disclose the two-wall-cavity refit (§6 idealization 9) as a
primary result of *this* cycle, not a deferred item — pre-registered
before running, exactly as `two_wall_cavity.py` did in exp-075. Having now
run it myself and found it reinforces rather than overturns REFUTE, doing
so inside the proposal would move my verdict to full `support`.

---

### Verification appendix (commands/values, for the Director)

- Reproduced `pad_round_trip_model.py` end-to-end: identical
  `rel_period_deviation_pad=1.8798`, `shape_r_squared_pad=0.0444`,
  `rel_period_deviation_absorb40=0.9642`, `shape_r_squared_absorb40=0.1997`.
- Checked `r(theta;ABSORB)` for branch/continuity pathology over a dense
  36–42° grid (6001 points) for both ABSORB=40/80: no discontinuity or
  sign-flip in `Re(n(x)²−sin²θ)` for any cell across the grid; the fast
  phase drift is genuine model behavior, not a branch-cut bug — but it is
  large enough (~13–15°/deg peak slope) to be comparable to the periods
  under test.
- `nu/omega` for the ABSORB=40/80 damping profile reaches 1.364 at the
  cell touching the wall (`Re(n²)` as low as −0.861) — i.e. the innermost
  cells of the graded band are not a weak-loss dielectric in this model;
  they are a strongly lossy, negative-real-part ("near-metallic") layer.
  This is inherited unchanged from exp-075 and not re-litigated here as a
  new defect, but it is the physical reason the reflectance phase moves
  as fast as it does, and the proposal does not connect the two.
- Retargeted `two_wall_cavity.py::c_empty_two_wall`/`image_geometry_right`
  at `(C40,G40,C80)`: `PAIR_PAD` two-wall → `P*_model=8.6677°`,
  `rel_dev=0.8797` (INCONCLUSIVE), shape `r²=0.0001` (REFUTE) → Combined
  REFUTE. `PAIR_ABSORB40` two-wall → `rel_dev=0.6851` (INCONCLUSIVE),
  shape `r²=0.0418` (REFUTE) → Combined REFUTE (was INCONCLUSIVE
  single-wall). `D_right`: C40=59, G40=99, C80=99 cells, matching the
  proposal's own cited values.
