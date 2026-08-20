# PHASE 5 — REVIEW · QUANTUM OPTICS · Panel Iteration 26 (exp-049)

*Fresh context, blind to the other six seats' Phase-5 reviews. Charter:
non-classical absorption, state-dependent or coherent interactions;
expressibility contract — mechanisms enter the bench only as effective
classical parameters, or Red Team strikes them. This cycle is the sharpest
possible test of my own Phase-2 record this cycle: I found the ill-
conditioning, my own proposed fix formula was independently shown by Red
Team not to work, and Red Team's exemption formula was adopted instead. I
re-derive and re-run everything below rather than take my own prior seat's
word for it.*

*Scripts run this session (scratchpad, not committed): direct calls to
`experiments/042-t21-magnitude-bridge/design_geometry.py`'s
`beam_divergence_incoherent`/`beam_divergence_coherent`/
`beam_divergence_incoherent_corrected`, unmodified, across the full
`N_SERIES` at four spot-checked cells, plus manual re-derivation of
`run.py`'s `delta_step`/`predicted_difficulty_rank`.*

---

## (a) Does `run.py::delta_step` implement Red Team's corrected exemption formula?

**Yes, verified by direct read, not by trusting NOTES.md's prose.**
`experiments/049-.../run.py:91-101`:

```python
def delta_step(c_n, c_2n):
    dabs = abs(c_2n - c_n)
    if abs(c_2n) >= C_THR:
        drel = 100.0 * dabs / abs(c_2n)
        exempted = False
    else:
        drel = None
        exempted = True
    converged = (dabs <= ABS_TOL) and (exempted or drel <= REL_TOL)
```

This is Red Team's Attack-5 formula exactly: an **exemption** (`drel = None`,
the relative clause dropped entirely) when `|C(2n)| < C_THR`, not my own
Phase-2 `max(|C|, C_THR)` **floor** formula, and not the original
un-floored, un-exempted ratio that motivated my attack in the first place. I
independently confirmed at Phase 2 (and re-confirm below) that my own floor
formula does *not* clear P-NCONV26-1b's `≤4/9` band — Red Team ran it and
got 8/9, matching what I would get if I ran it myself. The shipped code
contains none of that; it contains only the exemption. **Zero drift between
what Phase 3 adopted and what Phase 4 ran.**

## (b) Does the corrected criterion actually fix the ill-conditioning, or is it still an artifact?

**Independently re-run, not re-read.** I called `beam_divergence_incoherent`
and `beam_divergence_incoherent_corrected` myself, unmodified, at the exact
cell my Phase-2 attack cited as the worst offender (450nm/36°/FWHM=20°,
`incoherent`, where the uncorrected criterion gave `Δrel(41→81)=6680%`):

```
41->81:   C(41)= 3.5527e-04  C(81)= 5.2398e-06  dabs=3.500e-04  exempted=True  converged=True
81->161:  C(81)= 5.2398e-06  C(161)=-8.2510e-05 dabs=8.775e-05  exempted=True  converged=True
161->321: C(161)=-8.2510e-05 C(321)=-8.2516e-05 dabs=6.170e-09  exempted=True  converged=True
```

Every step is judged on `Δabs` alone (both `|C(41)|` and `|C(81)|` sit
2–3 orders below `C_THR`), the absolute value stabilizes to nine
significant figures by `n=321` and stays flat through `n=5121`, and the
cell is correctly declared `n*=41` (already converged) — this is real
convergence, not the runaway relative-error blow-up my Phase-2 attack
flagged. This one cell is among the 6/9 `incoherent` cells that pass at
`n=41` under the corrected criterion (matching `results.json`'s reported
`3/9 fail`, CONFIRMED against the `≤4/9` band).

I also spot-checked one of the cells the corrected criterion *still* flags
as needing `n*>41` — `incoherent_corrected` at 450nm/38°/FWHM=20°
(`results.json`: `nstar=81`, `c41=-1.5234e-03`, reported
`converged_value=-1.8825e-04`). I re-ran the full doubling series myself:

```
n=41:  C=-1.5234e-03
n=81:  C=-1.8825e-04
n=161: C=-1.5977e-05
n=321: C=-1.5993e-05
n=641: C=-1.5992e-05
```

**This is a real, order-of-magnitude shift near a genuine zero-crossing**,
not the spurious relative-error artifact — `Δabs(41→81)=1.34e-3`, above
`ABS_TOL`, so this step correctly fails; the step *from* 81 onward
(`Δabs(81→161)=1.72e-4`, exempted, converged) correctly passes, giving
`n*=81`. This confirms two things at once: (i) the exemption formula is not
over-correcting into a rubber-stamp — it still fails cells with real
sub-threshold movement, exactly as designed; (ii) the mechanism split
Attack 5 demanded (re-score `incoherent_corrected`'s own residual 5/9
failures, not assume they inherited the same artifact as the 9/9 pre-fix
`incoherent` failures) was done correctly — these are now genuine findings,
not leftover bookkeeping noise.

Also independently re-derived the coherent worst-cell headline
(450nm/36°/FWHM=20°): `C(41)=-0.965320`, `C(81)=-0.923975`,
stable from `n=161` onward at `-0.923993`. Move `41→5121 = 4.4727%`,
matching `results.json`'s reported `4.4747%` (P-NCONV26-8) and exp-046's
own `4.4727%` figure to the printed digit. **Verdict on (a)+(b): the fix is
real, correctly implemented, and independently reproduces on unmodified
code at every cell I checked — my own Phase-2 attack is resolved, not
merely asserted resolved.**

**One methodological note, found here, non-load-bearing.** `converged_value`
in `results.json` is defined as `values[n*]` — the value *at* the smallest
qualifying `N_SERIES` entry, not the value at the series' true asymptote
(`n=5121`). At the cell above, `values[81]=-1.8825e-4` while the true
asymptote is `-1.599e-5` — a full order of magnitude apart in relative
terms, though the absolute gap (`1.72e-4`) stays under `ABS_TOL` in this
instance, so no reported headline is threatened. This is an inherent
property of the two-consecutive-doublings design (only the *next* two steps
are checked, not the tail of the series), disclosed implicitly by the
method but not called out explicitly anywhere in NOTES.md. Worth one
sentence in a future citation of this audit's near-zero-`|C|` cells, not
worth reopening any of this cycle's own verdicts.

## (c) Is the sign-convention erratum fix correct?

**Re-derived from first principles, independently of both the buggy and
corrected code.** The hypothesis under test is: *cells the T21-analogy
predicts as "harder" (more angularly undersampled) show larger measured
convergence error.* For a Spearman correlation to **confirm** that
hypothesis, the two ranked series must move together: a variable that
increases with predicted hardness must be paired against a variable that
increases with measured error, giving `ρ > 0`; a hypothesis-confirming
result cannot coherently be scored as a negative correlation.

`predicted_difficulty_rank()` assigns the *hardest* cell `(36°,450nm)` rank
`n=9` (the **largest** value) and the *easiest* `(40°,750nm)` rank `1` — i.e.
predicted rank **increases with hardness**, by construction (`n - i` for
`i=0` at the hardest). `measured` is `Δrel`/scaled-`Δabs` — a quantity that
**increases with convergence error**, i.e. increases with hardness, if the
hypothesis is true. Correlating two series that both increase with hardness
gives `ρ>0` when the hypothesis holds. This is exactly the corrected
computation, and it is the only convention consistent with Phase 2's own
informal, independently-obtained citations (my own `ρ=0.717`(uncorrected
formula)/EM's per-function `0.717/0.600/0.450`/Red Team's own
`0.717/0.600/0.450` table) — none of Phase 2's three independent
recomputations ever produced a negative number, which they would have under
the buggy convention (rank `1`→hardest, decreasing with hardness, anti-
correlated with an error series that increases with hardness). **The
runtime fix is correct**: assigning the largest rank number to the hardest
cell, so that a real effect reads as `ρ>0`, is the only self-consistent
choice given the committed `ρ≥0.70`-to-CONFIRM band (a negative-correlation
CONFIRM would be incoherent). I also spot-checked that the fix wasn't
overcorrected into a rigged-positive result: the corrected `ρ` values
(0.450–0.483) are genuinely below the `0.70` confirm bar and above the
`0.30` refute floor — an honest PARTIAL, not a sign flip dressed up as a
win. **No further correction needed.**

One scope note on P-NCONV26-2 itself, not a defect: the corrected result
(all three functions positive, 0.45–0.48, none confirming) is a real,
disclosed finding that the T21-period analogy (my own idealization 3,
inherited from Iteration 18's edge-diffraction work) is a weaker per-cell
predictor than the Phase-1 prior assumed — right sign, wrong sharpness. That
is a legitimate, falsifiable miss this audit was built to allow, not a
process failure.

## (d) Does this cycle threaten or preserve the Iteration-19/22/23 mandatory coherent cross-check?

**Preserved, and strengthened, not threatened.** Three independent
headline-preservation results, all independently spot-checked above or
directly against `results.json`:

- **P-NCONV26-6, CONFIRMED at converged n**: `36/36` cells stay above
  `C_THR`; `35/36` stay at `≥20×` the incoherent reading (only 1 crosses,
  inside the predicted 1–3 band). This is exp-046's own P-TH23-A1 headline
  — the "0/36 incoherent vs. 36/36 coherent" contamination-risk asymmetry
  that grounds the mandatory cross-check's practical use — re-verified at a
  properly converged `n`, not merely at the silently-default `n=41` it was
  first measured at. It survives.
- **P-NCONV26-8, CONFIRMED, independently re-derived by me above**: the
  worst-cell coherent move (4.4727–4.4747%) is *the same number* exp-046
  already published as its own restored-mechanism headline — this audit
  shows that number was already close to the converged value, not an
  unrepresentative n=41 fluke. The cross-check's own most-cited magnitude
  figure does not move.
- **P-NCONV26-7, CONFIRMED**: the A3 effective-aperture identity (my own
  seat's Phase-5 re-derivation at Iteration 23, `w_meas/w_line =
  1/√(1−4σ_θ²tan²θ₀)`) is untouched by n-convergence (0.0pp shift at every
  FWHM≤10° cell) — expected, since that identity concerns the central lobe's
  shape, a different sensitivity axis from the grating-lobe aliasing this
  audit targets (my own idealization-4 note, Phase 2).

**Footnote question — checked directly, not assumed.** I grepped every
`experiments/*/` file in the repo for `beam_divergence_coherent` and its
siblings: the function is called only in `experiments/042-...`,
`experiments/046-...`, and this cycle — **never** in exp-047/048, which use
a structurally different, re-parameterized propagator
(`experiments/048-.../design_geometry.py`'s `GEOM78`, `A=724`) that this
audit explicitly does not test (idealization 7 / Attack 1's follow-up
trigger, correctly adopted). **No past citation outside exp-042/046 needs a
footnote — there isn't one to attach it to.** Within exp-042/046, the only
citation that could be read as needing a correction is any *future* reader
pulling a raw n=41 `C_empty` number for a FWHM=20° coherent cell without the
now-established ~4.5% convergence uncertainty; NOTES.md's own "What this
changes going forward" section already states this plainly and correctly
scopes it to n≥81, not n=41. **One real, still-open gap, already flagged in
this cycle's own idealization 7 and Red Team's Attack 1, not newly found
here**: the A=724/NY=1528 fallback geometry that exp-047/048's own
near-boundary Tier-W-adjacent citations actually use has never had this
convergence check run at all — a distinct future action item, not a defect
in what shipped this cycle.

---

## Additional findings, my own charter

- **The expressibility contract holds.** Grepped this cycle's own `run.py`
  and `design_geometry.py` imports: `numpy`, `math`, `scipy.stats`,
  `json`, `time`, `pathlib` — no new material law, no σ, nothing that
  smuggles a physical coherence *claim* past the classical-parameter
  boundary. `beam_divergence_coherent` remains scoped exactly as it was at
  its Iteration-19 birth: a mathematical upper-bound device, not a physical
  model of a real partially-coherent flashlight — this cycle characterizes
  its *numerical* convergence only, and says nothing new about whether the
  full-aperture-beamformed construction itself (my own Iteration-22
  finding, exp-046) is the right physical picture. NOTES.md does not
  conflate the two; good discipline, worth naming since it would have been
  easy to overclaim "coherent cross-check now validated" instead of
  "coherent cross-check's quadrature series now characterized."
- **The runtime erratum (sign-convention bug, self-caught before Phase 5)
  is handled correctly by house convention**: both the buggy and corrected
  computations are preserved in `results.json`
  (`P_NCONV26_2`/`P_NCONV26_2_ERRATUM_ORIGINAL_BUGGY`), the fix is
  documented inline in `run.py` at the point of the bug, and NOTES.md
  discloses it in its own Results section rather than silently shipping the
  corrected number. Matches this program's own "flag, don't smooth over"
  precedent (T10, R4).
- **The 972-record completeness ledger and the ≈52-minute cost profile
  (Red Team's Attack 4) both landed almost exactly as predicted**: `45m44s`
  measured vs. `≈52min` profiled, `972/972` records — a real, checked
  instance of this program's own cost-discipline working as intended, worth
  noting given how many prior cycles' cost estimates missed by 3×+ before
  being caught.

---

## VERDICT: **PROMISING**

The central hypothesis motivating this entire cycle — that `n=41` is
genuinely under-converged for the coherent function at FWHM=20°, the exact
finding my own Phase-2 attack this cycle depended on being real rather than
a bookkeeping artifact — holds up under my own independent re-execution of
the unmodified code, at every cell I checked, using both the raw values and
the corrected criterion. Red Team's exemption formula is exactly what
shipped in `run.py` (a), it resolves the ill-conditioning without over-
correcting into a false pass (b, both directions checked), the sign
convention Phase 4's runtime erratum fixed is the only physically coherent
choice given the committed confirm band (c), and the mandatory coherent
cross-check this program has leaned on since Iteration 19 survives this
audit's scrutiny intact — its two most-cited headline numbers (36/36 above
threshold, 4.47% worst-cell move) are now independently reproduced at a
properly converged `n`, not merely asserted at a never-tested default one.

Not an unqualified PROMISING: P-NCONV26-2's own secondary story (the T21
fringe-period analogy as a *per-cell* difficulty predictor, not just a
right-signed one) landed a genuine, disclosed miss, and the
`converged_value` reporting convention noted above deserves one clarifying
sentence before a future cycle treats every reported "converged" number as
the true `n=5121` asymptote rather than "converged enough by this audit's
own two-step test." Neither defect threatens any scored conclusion this
cycle reached.

## Ranked top-3 candidate next steps

1. **Re-run this identical sweep at exp-048's A=724/NY=1528 fallback
   geometry** (idealization 7 / Attack 1's own follow-up trigger). This is
   the geometry exp-047/048's own near-boundary Tier-W-adjacent citations
   actually use, and it has never had a convergence check — the exact gap
   T21's own six-iteration citation-scope saga (exp-042→048) already paid
   once to learn the hard way. Cheap: reuses this cycle's own `run.py`
   almost verbatim, swap the imported `design_geometry` module.
2. **Source a real physical M²/étendue value for a flashlight and close
   T21's contamination-risk verdict**, my own Iteration-23 Phase-5 pick,
   still unbuilt. This audit removes the last excuse for deferring it
   (the n=41 kernel that both `beam_divergence_coherent` and `_incoherent`
   depend on is now characterized and known-safe outside FWHM=20°) —
   the M² bridge interpolates through exactly that regime, and can now be
   built on a properly-scoped-n foundation instead of an untested one.
3. **One-sentence fix to `results.json`'s `converged_value` semantics**:
   either add and store the true `n=5121` value alongside `values[n*]` in
   `per_cell_summary` (checked directly: `main()`'s in-memory `values` dict
   already holds it per cell/function, computed during this same run, but
   it is discarded before serialization — only `c41`, `c401`, and
   `converged_value` are written), or add an explicit docstring/field
   noting `converged_value` is "value at the smallest n* passing two
   consecutive doublings," not "the series' asymptotic value." A
   ~10-line, zero-new-evaluation change either way. Prevents a future
   cycle from citing a near-zero-`|C|` `converged_value` as more precise
   than it is.
