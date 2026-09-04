# PHASE 5 — MATERIALS & METAMATERIALS REVIEW · Panel Iteration 85 (exp-108)

Fresh-context seat, blind to the other six Phase-5 reviews. Reviewed
PANEL.md, LOGBOOK.md in full, PLAN.md's Vision/Current-state, this
cycle's full record (`phase1_proposal.md`, all five Phase-2 critiques,
`phase2_redteam_audit.md`, `NOTES.md`, `results.json`, `run_output.txt`,
`run.py`, `chunk_runner.py`, `analyze.py`, `reclassify_106.py`, the patch
to `experiments/106-.../run.py`, and the new `stage26_chunked_run_
identity()` in `lab/validation/run_all.py`), plus `lab/sections.py` and
`lab/materials.py` directly for the two functions this cycle's physics
turns on.

## Verdict: **CONFIRM-WITH-GAPS**

The cycle's numbers, code fix, and gating discipline all independently
reproduce. But the cycle's own scope statement ("no realizability claim
anywhere in this document," T1/constraint-3 both N/A) is too narrow: it
correctly rules out a *new mechanism* realizability question, but misses
a real, positive, MATERIALS-charter-relevant implication of its own
headline CONFIRM — exactly the gap the task brief asked this seat to
check for. Everything else load-bearing checks out clean.

---

## 1. Independent re-verification from primitives (zero-FDTD, as instructed)

All three ran clean, no re-runs needed:

- `python3 experiments/108-.../reclassify_106.py` — reproduces the exact
  string in NOTES.md's Result section: OLD =
  `REFUTES-electrical-thickness-growth-hypothesis (NOT-TRUSTED...)`, NEW =
  `THREE-WAY-AMBIGUOUS (REFUTES-... nominally ...; p_abs_frac_diff=
  0.1231(r156)/0.1796(r312) exceeds 0.10) (NOT-TRUSTED...)`. All other
  fields (`shape_ratio_fixedabs=18.228333623646076`, `noise_dominated=
  False`, `trusted=False`) bit-identical to exp-106's committed
  `results.json`, confirming the patch touches only the classification
  string.
- `python3 experiments/108-.../analyze.py` — reproduces item i
  (CONFIRM, both r, `sum_check_pass=True`), item ii (`residual_std=
  2.8972e-06`/`2.1022e-06` at r=156/312, both CONFIRM against
  `|Δ_boxA|=2.9690e-05`/`2.4680e-05`), item iii (`frac_unresolved=
  0.1827`/`0.2525`, both PASS), and `closure` (0.0196%/0.0160% at
  r=156, 0.0563%/0.0581% at r=312) to the digit against NOTES.md.
- `python3 lab/validation/run_all.py --only 26` — 2/2 PASS: positive
  control `max|diff|=0.000e+00`, negative control (off-by-one-chunk
  corrupted checkpoint) deviates `2.000` (200%), confirming the gate
  genuinely discriminates, not merely a tautology.
- `git diff HEAD~1 -- experiments/106-.../run.py` — the Tier-0 patch is
  real, committed, and matches the extracted-function shape Attack 1
  demanded: `classify_shape_ratio_fixedabs()` is a standalone,
  importable function at module scope, called both by `run.py`'s own
  inline classification block and by `reclassify_106.py` — one function,
  one name, no duplicated logic, R25's founding instance genuinely
  discharged in code, not merely narrated.

No discrepancy found anywhere I checked. The full trust suite (41/41,
`--only 12346789`) plus the new stage 26 (2/2) both read green in
`run_output.txt`, consistent with what I re-ran myself.

## 2. Does this cycle correctly bound realizability? — the gap

**The T1/constraint scoring ruling itself is correct and I confirm it
structurally, not merely by trusting the proposal's self-report.**
Nothing in Tiers 0/1 builds, varies, or scores a σ(I)/σ(x,t)/angular-
selectivity/sub-threshold mechanism; `materials.graded_black_shell` and
`materials.pec_disk` are reused unmodified; no new material class or
parameter regime is proposed. "No realizability bound to publish/rate
this cycle" is the right call for that narrow question, and my own
Phase-2 critique said as much ("no realizability claim anywhere in this
document overclaims what a real material could do").

**But that is a different question from "does this cycle's own CONFIRM
carry a realizability implication that should have been named."** It
does, and the cycle's own Idealizations/scope language does not name it,
despite the task brief's suspicion being correct on inspection:

Item i's Result states the finding in pure optics terms: *"an opaque,
near-Babinet fixed-abs graded shell's scattering pattern is set by its
outer profile, not its interior fill, at both r tested."* Restated in
MATERIALS' own charter language — sub-wavelength/interior structure,
what could physically realize the proposed behavior — this is a genuine,
if modest, **manufacturing-tolerance finding**: for a real coating built
to this graded-conductivity recipe (`graded_black_shell`'s own docstring
names it explicitly as carbon-nanotube-black-style — a published,
physically realizable absorber class, not a hypothetical one), the
choice of backing/core (a bare substrate, a metal ground plane, a hollow
cavity, any of which the PEC-vs-hollow factorial spans) is now shown,
floor-gated, to leave the far-*angular* scattering signature unchanged to
≤5% at every one of 48 angular bins and 6 independent box radii — not
merely the aggregate cross-section T9 already established. That is
exactly the kind of finding this seat's charter exists to translate into
a fabrication-tolerance statement, and this cycle does not make that
translation anywhere in its own text — not in §Idealizations, not in
§Result, not in the "Next" ranking. The closest the document comes is
treating the result purely as closing T9/T11 (a bench-instrument/
noise-floor question), never as a materials-design degree of freedom.

**This is a real, correctable gap, not a mislabeled finding — and it is
appropriately modest, not overclaimed, for three independent reasons a
future write-up should state explicitly if it elevates this into a
standing materials note:**

1. **Scale**: this is NOT a sub-wavelength-metamaterial-unit-cell
   finding. I checked `geom_fixedabs()` directly: `ABS_THICKNESS=48`
   cells is held fixed across r (the family's whole point), giving a
   physical shell thickness of `48/CPL_600 = 2.4λ` at the 600 nm design
   wavelength — consistent with `graded_black_shell`'s own docstring
   design rule (≥1.5λ for broadband-small entry reflection) — while the
   CORE radius the finding is actually about is macroscopic: `R_CORE =
   108`/`264` cells = **5.4λ/13.2λ**, many wavelengths across. The
   "interior fill doesn't matter" result is a statement about a
   macroscopic backing/substrate choice sitting behind an already
   near-opaque graded coating (`core_frac≈10⁻⁷`, PLAN.md/exp-107's own
   figure), not about sub-wavelength interior structuring in the
   metamaterial sense my charter's first clause names. Worth being
   precise about which half of the MATERIALS charter this result serves
   (realizability/tolerance of a macroscopic backing), so it is not
   mistaken for a metamaterial-unit-cell claim it does not make.
2. **Regime**: floor-gated CONFIRM at θ=0° (normal incidence) only, at
   one wavelength (600 nm), at two radii (r=156/312, both bench-scale —
   T8's own live thread notes the bench plane sits deep in the shadow's
   near zone, z/z_R ≈ 0.04–0.06, not witness scale). The tolerance
   implication is licensed only inside that regime; it says nothing yet
   about oblique incidence (Red Team's own Reconciled-queue Tier 1 item
   3 already proposes exactly this extension, for a different, purely
   instrumental reason — worth doing partly *because* it would also
   test whether the tolerance finding survives off-normal illumination,
   the geometry closer to a real swept-beam witness scene).
3. **Profile-specific**: the null is for THIS graded σ(r) profile at
   THIS optical depth (`τ_center≈3.9` by construction, fixed-abs
   family). It is not licensed to generalize to a thinner or
   partially-transmissive coating, where a reflective backing could
   plausibly reappear in the angular pattern — the near-Babinet/near-
   opacity precondition is doing real work here and should travel with
   any future citation of this finding.

**Recommendation**: a one-sentence addition to a future cycle's (or a
standing LOGBOOK T9-family) record, in MATERIALS' own voice: *"Item i's
CONFIRM (both r, both articles, floor-gated at 48 bins × 6 box radii)
is a fabrication-tolerance finding, not merely an instrument-validation
one: for this graded-absorber recipe at this optical depth, the backing/
core material is angularly, not merely aggregately, optically free —
bounded to normal incidence, 600 nm, r=156/312 bench scale, and this
specific near-opaque profile."* This does not move any Combined Verdict,
does not compete for FDTD budget, and does not reopen T1/constraint-3 —
it is a naming gap, the kind R21's own "persisted but never stated in
Result/Learned prose" lineage exists to catch one level up (here: a
genuine finding stated in one discipline's terms but never translated
into the terms of the discipline it is actually most relevant to).

## 3. My own Phase-2 T9-anchor citation fix — did it survive into the
frozen NOTES.md Result section?

**Yes, correctly, and I re-verified the arithmetic myself rather than
trusting the restatement.** My Phase-2 critique's sharpest attack flagged
that the Phase-1 proposal's §1 called the hollow-vs-PEC-cored
`abs_ext_ratio` delta "the same order T9 found at r=78," when LOGBOOK's
own Iteration-84 record had already corrected this exact comparison to
**19.0×/15.8×** (not "same order"). Checking the arithmetic directly:
`2.9690×10⁻⁵ / 1.56×10⁻⁶ = 19.03` (r=156), `2.4680×10⁻⁵ / 1.56×10⁻⁶ =
15.82` (r=312) — matches the cited 19.0×/15.8× to the stated precision.

NOTES.md's own Phase 2→3 synthesis carries the fix verbatim and
correctly: *"the gap is 19.0× at r=156, 15.8× at r=312 — a real ~1.2-
decade gap, not 'same order.' This cycle's own §Setup/§Predictions below
use the corrected figures throughout; the regression is noted here as a
live finding..., not silently fixed."* Red Team's own audit independently
reproduced the identical figures (§0.5) before adopting my critique in
full and folding it into the mandatory-fix list (fix 2) — so the
correction is doubly, not merely singly, sourced in the record. I found
no place downstream (Setup, Predictions, Result, Next) where the
pre-correction "same order" framing resurfaced.

## 4. Item ii's own detrended noise-floor finding — consistent with, or
does it correct, any realizability-adjacent claim on file?

**Consistent, and it strengthens rather than corrects the standing
Babinet-ceiling reasoning — it does not touch the unrelated σ(I)
realizability memo at all.** Two things live under "realizability-
adjacent" in this program's record, and item ii bears on only one:

- **T9's own Babinet/geometric-optics ceiling caveat** (ESTABLISHED
  section, Iteration 3, EM): σ_abs/σ_ext ≤ 0.5 for any perfectly-black,
  zero-reflectivity object "independent of interior structure" is the
  founding statement this whole T9 thread exists to stress-test. Item
  ii's own detrended floor (`residual_std = 2.897×10⁻⁶`/`2.102×10⁻⁶` at
  r=156/312, both ~5× inside the CONFIRM bar against `|Δ_boxA|`) shows,
  for the first time with a genuine noise floor rather than an informal
  "box_dev is 1221× bigger" argument, that the near-zero hollow-vs-PEC-
  cored delta this "independent of interior structure" language predicts
  is not itself an artifact of box-placement/near-field convergence —
  it is a real, resolved near-zero. This is a direct, positive
  corroboration of the Babinet-ceiling reasoning, not a correction to
  it, and I independently re-derived the fit-and-residual numbers
  against `analyze.py`'s own output (§1, above) rather than trusting
  NOTES.md's restatement.
- **`REALIZABILITY_MEMO.md`'s own UNOBTANIUM-WITH-PARAMETERS verdict**
  (Iteration 11, exp-034) — RSA/TPA dynamic-range and irradiance gaps for
  the σ(I) intensity-gated escape route — is a completely different
  mechanism thread (T1's own switching/gating question) and is untouched
  by anything in this cycle. Nothing in item i/ii/iii bears on it in
  either direction; the two "realizability-adjacent" findings on file
  this cycle sit in genuinely disjoint parts of the program and I found
  no place where NOTES.md conflates them.

One scoping note, not a correction: item ii's own detrended floor answers
Iteration-85's Tier-2 item 1 (re-deriving T9's `≤2×10⁻⁵`/`≤2×10⁻⁴` bands)
as a byproduct — but NOTES.md's own "Next" section correctly keeps this
distinct from `box_dev`'s own separate, still-thinning margin (~9.0× at
r=312, per Iteration 84) — the two are different quantities (this
channel's intrinsic floor vs. `box_a`-vs-`box_b` self-consistency on
`sigma_ext`) and the document does not conflate them. Correct, and worth
confirming explicitly since conflating exactly these two quantities is
the kind of unit/commensurability slip R9 exists to catch.

## 5. Minor items, non-blocking

- The `graded_black_shell` docstring itself (`lab/materials.py:74`)
  independently confirms the "carbon-nanotube-black-style" framing this
  review leans on in §2 — a real, published absorber class (near-unity
  broadband absorption, near-index-matched surface), not an invented
  one; the idealization gap is the specific graded-conductivity profile
  achieving zero-reflection matching, not the material class itself.
  This cycle does not claim otherwise anywhere.
- The R23 live-fire check (VISION's mandatory bound condition) reports
  cleanly in `run_output.txt` (`run.py`: 4 `disclaimer` hits;
  `chunk_runner.py`/`analyze.py`/`reclassify_106.py`: 0 each) — outside
  my own charter to adjudicate, but I confirmed the numbers match
  NOTES.md's Result section exactly while re-reading the file for other
  purposes.
- I did not find any place where this cycle's own governance work
  (Tier 0, R25/R23) touches materials realizability at all — correctly
  so; nothing there needed my seat's review beyond the confirmation
  above.

## Summary

**CONFIRM-WITH-GAPS.** Every number and code change I could cheaply
re-derive from primitives reproduced exactly — the Tier-0 patch is real
and correctly scoped, the Tier-1 batch's four items are honestly gated
and land as clean CONFIRMs, my own Phase-2 T9-anchor fix survived intact
into the frozen record, and item ii's detrended floor is consistent with
(indeed corroborates) the only realizability-adjacent claim it actually
touches (T9's Babinet-ceiling reasoning), while correctly staying
disjoint from the unrelated σ(I) realizability memo. The gap: this
cycle's own scope language ("no realizability claim anywhere in this
document") is accurate for "no new mechanism," but the angular-pattern
CONFIRM is itself a modest, real, appropriately-bounded manufacturing-
tolerance finding — the backing/core material behind a near-opaque
graded absorber is angularly free, not merely aggregately free — that
falls squarely inside this seat's own charter and was never named as
such anywhere in the document.
