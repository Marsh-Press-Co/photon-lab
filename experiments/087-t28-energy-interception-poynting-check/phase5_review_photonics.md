# PHASE 5 — REVIEW · PHOTONICS · Panel Iteration 64 · exp-087

Charter: surface interaction, absorption spectra, angular dependence,
scattering cross-sections. Is the proposal's optical response coherent as
stated, across wavelength and angle? Everything below is independently
re-derived from `results.json`/`run.py`/`lab/sections.py`, not accepted
from NOTES.md's own prose (R4/R9 discipline).

## 0. Housekeeping re-verification

Re-ran the arithmetic independently from `results.json` rather than
trusting the write-up. All confirmed exactly:

- P1 vacuum footprint: `all_vacuum=True` at every `BOX_A`/`BOX_B` cell,
  both configs.
- P2 reproduction: `max_dev=0.0` exactly against `experiments/083-.../
  results.json::per_theta`.
- P4 `xi_ext`: max observed value `4.82×10⁻⁴` (`G40, 41.8°, BOX_B`), well
  inside the `≤0.12` tolerance, at all 12 (cfg,θ,box) cells.
- P5 synthetic recovery: all 14 cases pass (independently re-run the
  `_label`/`classify_resolved` logic against the frozen decade-boundary
  cases by hand; matches).
- Non-negativity gate: `sigma_abs≥0` at all 12 post-correction cells
  (154.2–168.1).
- `total_new_fdtd_calls=13`, matching the disclosed call-count correction.
- Primary table (`frac_p_abs`, `frac_contrast`, `ratio_k`) reproduces
  exactly: 36.0°→2.6424, 38.6°→53.9884, 41.8°→5.7102. Classification
  `ENERGY-DOMINANT` is the correct output of `classify_resolved()`'s own
  "any angle over `RATIO_HIGH`" priority rule applied to these three
  numbers — not a transcription error.

Zero discrepancies found between NOTES.md's prose and the underlying
`results.json`/`run.py`.

## 1. The θ=38.6° zero-crossing-artifact claim — independently re-derived, CONFIRMED and quantitatively sufficient

Read `experiments/083-.../results.json::per_theta` directly (not via
NOTES.md's citation). `delta_scene(θ)` around 38.6°:

| θ | 38.0° | 38.2° | 38.4° | **38.6°** | 38.8° | 39.0° |
|---|---|---|---|---|---|---|
| `delta_scene` | +1.923e-3 | +1.515e-3 | +8.083e-4 | **−4.151e-5** | −8.569e-4 | −1.484e-3 |

Confirmed: the curve changes sign between 38.4° and 38.8°, and 38.6° sits
almost exactly on the zero-crossing — `|delta_scene(38.6°)|` is 1–2 orders
of magnitude smaller than either flanking point. This is a genuine,
resolvable node of a smooth, well-established oscillation (the same
`P*=2.9474°` Branch-B curve `exp-083` resolved at `R²=0.86`, `p=0.0`
against 20,000 null permutations) — not noise, not a new artifact
specific to this cycle.

**Checked the competing explanation the task specifically asked for: is
`frac_p_abs` itself anomalously LARGE at 38.6°, not just `frac_contrast`
anomalously small?** Compared the measured `frac_p_abs(38.6°)=4.001×10⁻³`
against a plain linear interpolation between the two flanking measured
angles (36.0°→1.965×10⁻³, 41.8°→7.214×10⁻³):

```
interpolated frac_p_abs(38.6°) = 4.318e-3
measured     frac_p_abs(38.6°) = 4.000e-3   (−7.4% vs. the linear interpolant)
```

`frac_p_abs` at 38.6° sits **below**, not above, its own smooth trend
line — the opposite of what a competing "real energy spike" explanation
would need. There is no numerator anomaly. `frac_contrast`, by contrast,
collapses by a factor of **13.5×** relative to the mean of its own two
flanking angles (`(7.44×10⁻⁴+1.26×10⁻³)/2=1.004×10⁻³` vs. the measured
`7.41×10⁻⁵`). Substituting that neighbor-average `frac_contrast` for the
measured (zero-crossing-suppressed) one gives a hypothetical
`ratio_k(38.6°)≈3.99` — squarely inside CONSISTENT, matching the other
two angles' own readings (2.64, 5.71) closely. **The denominator artifact
is not merely plausible, it is quantitatively sufficient, on its own, to
manufacture the entire 54× reading**, with no residual gap requiring a
second or competing mechanism. NOTES.md's own hedging ("disclosed... not
adopted as settled") is appropriately cautious language for a
conclusion that, on independent re-derivation, is actually about as
clean as a single-cycle, 3-point instrument can produce.

**This does not change the falsification.** Excluding 38.6° as an
artifact, the remaining two angles (36.0°→2.64, 41.8°→5.71) both sit in
CONSISTENT, not the predicted ENERGY-DECOUPLED (`<0.1`). Both figures
independently re-derived from the raw `sigma_abs`/`sigma_ext` widths and
the cited `exp-083` contrast figures — confirmed exact.

## 2. Is the σ_abs(θ)/σ_ext(θ) trend physically coherent?

Two separate quantities are moving here and they should be examined
separately, which NOTES.md does not do explicitly:

**(a) The material-response fraction `ratio_abs_ext = σ_abs/σ_ext`** is
essentially flat across the window: `0.5128 → 0.5134 → 0.5138` (36.0° →
38.6° → 41.8°, C40; G40 nearly identical). A 0.2% spread across 5.8° of
incidence angle, on a rotationally-symmetric graded-shell absorber, is
exactly what ray/geometric optics predicts (this seat's own Phase-2
steel-man: a circle's absorbed/extinguished split shouldn't depend on
illumination direction) — this is a genuine, coherent, and previously
untested (obliquely, on `graded_black_shell`) confirmation of that
symmetry, sitting close to T9's broadside `0.51` anchor. Nothing
suspicious here; if anything, this is the single cleanest new fact this
cycle produced and is worth promoting to an ESTABLISHED-section citation
(§5 below).

**(b) The absolute cross-section magnitudes** (`σ_abs`: 154→160→167 cells,
C40; `σ_scat`, `σ_ext` moving in lockstep) rise smoothly and monotonically
by ~9% over the same 5.8°, at a mildly accelerating rate (≈2.1/°→2.4/°).
This is NOT the material absorbing more efficiently (that's flat, per
(a)) — it must be a box/reference-strip geometric effect: `i_inc` (the
empty-run reference-strip flux magnitude) itself rises ~7% over the same
range (0.3177→0.3279→0.3410), and `σ_ext = p_ext/i_inc` inherits both a
numerator and denominator that vary with θ. Given this exact bench
geometry sits deep in its own near-field regime (Fresnel number ~13,
established across ~15 prior T28 cycles) with a fixed-location,
swept-angle reference strip, a smooth several-percent θ-dependence in a
downstream flux measurement is exactly the kind of behavior this
program's own T28 sub-thread has repeatedly found elsewhere on this same
bench (empty-scene `delta_empty`, `P_edge_A`, `i_inc` itself). **Nothing
here is numerically suspicious** — no discontinuities, no sign flips
beyond the diagnosed `i_inc` convention issue (§3), no non-monotonicity —
but it should be named explicitly as a NEAR-FIELD BOX/REFERENCE-STRIP
effect, not silently left to look like "the absorber genuinely
extinguishes more light at 42° than 36°," which NOTES.md's raw table
could be misread as implying without this decomposition.

## 3. The `widths_direction_corrected()` fix — independently re-derived, holds up

Read `lab/sections.py::widths()` directly. `i_inc` is computed with the
SAME `<Sx> = −½Re{Ez·Hy*}` "+x-positive" convention `_face_flux` uses at
the box faces, evaluated on the empty run's reference strip. `p_scat`
(net outward box flux of the scattered field) and `p_abs` (net inward box
flux of the total field) are both computed via the same fixed-coordinate
divergence-theorem sum — genuinely direction-independent physical
quantities (a real photon count leaving/entering a source-free box does
not care which way "+x" happens to point). `dg069.CONFIGS` confirms
`src_x>obj_x>plane_x` for `PAIR_PAD` — the T28 window's actual geometry —
so the wave travels in `−x`, and the SAME fixed "+x-positive" convention
correctly reports the reference-strip's physical (positive) intensity as
a *negative* `i_inc`. Dividing a physically-positive `p_abs` by a
negative `i_inc` mechanically produces the observed
uniformly-negative-`σ_abs` symptom — exactly the diagnosis in `run.py`'s
own docstring, and I find no error in it.

**Independent stress-test of whether this masks a subtler bug, not run
by NOTES.md itself**: if `p_ext_cross` (the incident×scattered cross-term
route) carried any *additional*, direction-specific sign convention
beyond the shared `i_inc` denominator — e.g. a residual phase-convention
issue specific to the cross term under beam-direction reversal — then
applying the SAME single scalar correction (`×sign(i_inc)`) to
`sigma_ext_cross` as to `sigma_ext` would NOT reconcile the two routes;
`xi_ext` would blow up post-correction rather than shrink. Instead, the
already-independently-computed `xi_ext` (a P4 gate Phase 2's own EM
critique added, computed AFTER the correction) is tiny everywhere
(`≤4.82×10⁻⁴`) — the two independent extinction routes agree to within
0.05% post-correction, at all 12 cells, for the FIRST time this identity
has ever been exercised on `graded_black_shell` at any angle. This is
strong internal evidence, not merely NOTES.md's own assertion, that all
four `sigma_*` fields share exactly the single direction-dependence this
fix corrects, with no second, hidden convention issue riding along
specifically in the cross term. **The fix is correct, and — unusually for
a same-cycle bug-catch — is independently corroborated by a
gate the proposal added for an unrelated reason (route-agreement),
rather than resting on the fix author's own say-so.**

One completeness note, not load-bearing: `widths()`'s own `back_frac`/
`fwd_frac` fields (unused by this cycle) are computed from raw `p_back`/
`p_fwd`/`p_scat` directly, never divided by `i_inc` — they are correctly
untouched by this bug and require no correction; `run.py`'s wrapper
correctly leaves them unmodified (`out=dict(w)` copies them through). Any
future caller that DOES use those fields on a `src_x>obj_x` geometry
should confirm this remains true rather than assume it.

## 4. Aliasing-lattice residual risk (Phase-2 fix 2)

The adopted `{36.0°,38.6°,41.8°}` grid (gaps 2.6°/3.2°) sits 8.5–12.6%
from exact n=1 resonance against `P_edge_A`/`P*` — clearer than Phase 1's
original uniform 3.0° spacing (1.8%) but not zero risk, as Phase 3 itself
disclosed. In the event, the dominant finding (§1) traces to a
already-resolved, densely-sampled 31-point curve (`exp-083`'s own
`delta_scene`), not to any new aliasing artifact in this cycle's own
3-point `frac_p_abs` sampling — `frac_p_abs`'s own three points show a
smooth, close-to-linear trend (§1, −7.4% off interpolation, not a
flat/aliased plateau), which is mild evidence against (not proof against)
aliasing specifically corrupting the NEW channel. Because n=3 cannot
independently confirm this, I do not treat it as resolved — see §6 item 1.

## Verdict on this cycle's Combined Verdict contribution: **PARTIAL**

From PHOTONICS' vantage specifically: the optical response measured here
is internally coherent. The material-response ratio (σ_abs/σ_ext) behaves
exactly as ray optics predicts for a rotationally-symmetric absorber
across this angular window — a genuine, clean, previously-untested
confirmation. The absolute cross-section trend is smooth and explicable
as a near-field box/reference-strip effect, not evidence of anything
broken. The θ=38.6° outlier is independently re-derived here (not merely
trusted) to be fully and quantitatively explained by a denominator
zero-crossing artifact in the cited `delta_scene` curve, with the
numerator (`frac_p_abs`) showing no compensating anomaly whatsoever — as
clean a same-cycle self-correction as this sub-thread produces. The
direction-correction fix is independently verified sound, including by a
stress test NOTES.md itself did not run. None of this is grounds for
PROMISING, though: Checkpoint criterion 2 is correctly N/A (no mechanism
claim), and the substantive result — after the artifact explanation is
applied as generously as the data allow — is a genuine falsification of
the pre-registered prediction (CONSISTENT, not ENERGY-DECOUPLED, at the
two clean angles) that materially updates this sub-thread's ten-plus-cycle
phase/interference-only prior. That is a real, informative, correctly-
executed instrument result that leaves T28's own mechanism question more
open, not less — matching this sub-thread's own established PARTIAL
convention for genuinely new but non-conclusive findings (e.g. exp-082,
exp-083, exp-085, exp-086), not RULED OUT (nothing here forecloses a
mechanism class) and not PROMISING (no constraint-3 ledger progress, by
this cycle's own explicit scope).

## Ranked candidate directions for Iteration 65 (PHOTONICS' own charter vantage)

1. **Run the energy-interception channel (`widths()` at `BOX_A`) across
   the FULL 31-point/0.2° dense window, not a 3-point subset.** This
   cycle's own headline finding is dominated by exactly the failure mode
   a sparse sample is most exposed to (one point landing on a
   denominator's zero-crossing). A dense `frac_p_abs(θ)` curve, directly
   overlaid point-by-point on the already-resolved `delta_scene(θ)`
   curve, would settle whether `ratio_k`'s CONSISTENT reading is a stable
   trend or itself has structure that a 3-point sample cannot see —
   turning this cycle's single most information-dense open question into
   a properly-powered measurement, at the same per-call cost this
   sub-thread has already paid for the Weber-contrast channel (exp-083).
2. **Institutionalize the newly-validated extinction-routes-agreement
   identity for `graded_black_shell`, obliquely, into the trust suite
   (stage 8).** EM's Phase-2 finding (confirmed by Red Team, confirmed
   again here) is that this exact combination had never been gated before
   this cycle. It passed cleanly (`xi_ext≤4.82×10⁻⁴`) — a genuine new
   fact worth a permanent `VALIDATION.md`/suite row (`xi_k`, matching the
   existing `xi_p`/`xr`/`xi_u` rows), not left as a one-off P4 check that
   the next `graded_black_shell`-at-oblique-incidence cycle has to
   re-earn from scratch.
3. **A full R3-grade settling study for the `widths()`-derived channel
   specifically** (only one (cfg,θ,box) cell spot-checked this cycle,
   `rel_dev≈8×10⁻⁵`/`9×10⁻⁴`). This channel is now load-bearing for a
   falsifying, cited result, not merely disclosed context — the same
   discipline this program already applies to any channel that moves from
   "context" to "primary metric" status.
4. **Extend the energy-channel measurement to a second wavelength**
   (folds into the still-11-cycles-deferred x-wall wavelength-generality
   leg, but specifically for `frac_p_abs`/`ratio_k`): does the
   CONSISTENT-not-DECOUPLED finding hold at 450/750nm, or is it a
   600nm-specific near-field coincidence? Lower priority than items 1–3
   (a wavelength leg is already a standing, differently-owned board item),
   named here because it is the natural next generalization of THIS
   cycle's own specific finding.
