# PHASE 5 — REVIEW · PHOTONICS · Panel Iteration 71 · exp-094

*Blind, parallel review. No access to any other seat's Phase-5 output this
cycle. All figures below independently recomputed from `results.json`/
`run.py`/`design_geometry.py` primitives this session — not taken from
`NOTES.md`'s own prose (R4/R9 discipline).*

## 0. Independent re-derivation

- **Rank 2 (sigma@41.6°).** `ds_ratio = 1.92032e-4/1.78376e-4 = 1.07656`;
  `fc_ratio = 3.61448e-4/3.32960e-4 = 1.08556` — both inside `[0.3,3.0]`,
  signs matched. Bit-exact to the printed `1.0766`/`1.0856`. CONFIRM correctly
  derived.
- **Rank 3.** `ratio_k(38.4°): 16.9967271/0.9075118 = 18.7267×` — confirmed a
  FLIPPED classification (`0.9075<10<16.997`). 36.0° (2.4582 vs 2.6424) and
  38.8° (2.2729 vs 3.8733) both stay `Y=0` — CONSISTENT, correctly derived.
- **Rank 1a settling.** `rel_dev = |3.893642e-4−3.898698e-4|/3.898698e-4 =
  0.1297%` — PASS, two orders of magnitude inside the `1e-2` bar.
- **Rank 1b — the headline.** Recomputed all six interior points directly
  from `results.json::rank1b.per_theta`: `delta_scene` is **positive at every
  one of 41.750°/41.775°/41.825°/41.850°/41.875°/41.900°**
  (4.22e-4→4.12e-4), all `floor_pass=True` against the *same* `FLOOR=
  1.917438e-4` exp-093 used, `ratio_k` 7.13→3.67, all classified CONSISTENT.
  Cross-checked against exp-093's own committed `item1.per_theta` at the
  identical six angles (`cpl=30`, same `sigma_max` correction logic): **every
  one of those six reads `delta_scene<0`**, four clear the floor and read
  ENERGY-DOMINANT (`ratio_k` 20.48–29.58), the other two are
  `NODE-UNRESOLVABLE`. This is independently confirmed to be a genuine,
  complete sign-and-classification reversal at every sampled point, not a
  partial or boundary-adjacent effect — `NOTES.md`'s own characterization is
  accurate, not overstated.
- **Rank 3-ext.** Re-derived the margin/Y semantics from `compute_zone`'s own
  established convention (small margin ↔ near-null ↔ `Y=1`; large margin ↔
  `Y=0`): the new 38.4° point (`Y=1`, margin 1.485) sits *below* the existing
  zone's own lower edge (4.108), and the new 36.0°/38.8° points (`Y=0`,
  margins 7.775/18.15) sit *above* the existing upper edge (5.429) — all
  three land on the side of the ordering their own label predicts, so the
  zone is correctly unchanged and correctly reported non-inverted. No defect
  here, despite this being exactly the shape of check (R15's founding
  inversion) that has fired before on this sub-thread.
- **Gate 5, independently re-run this session** (not merely trusted from
  `NOTES.md`'s own prose — see §2 below): confirmed genuinely
  discriminating.

## 1. Does the `cpl=40` reversal make physical sense, or does it read as an
`R4`-family artifact? (steel-man / attack)

**Steel-man.** Three independent facts, all verified above or from source,
argue this is a real optical-response finding about the discretized system,
not a construction-recipe artifact:

1. **`R4` disagrees with `R3` — it does not replicate a shared defect.**
   Idealization 17's own disclosed risk ("if the `R3` recipe carries an
   undetected systematic bias, `R4` inherits it unchanged") is a risk about
   false *agreement* masking a shared flaw. It is not, by itself, a reason to
   distrust *disagreement* — two members of the same congruent-construction
   family reading oppositely is exactly the observable a resolution check is
   built to produce, and disagreement here cannot be explained by a bias both
   families share identically.
2. **The physical geometry this comparison needs is genuinely preserved,
   independently re-verified from `design_geometry.py` source, not merely
   from the proposal's own claim**: `r4_config()` (lines 265–282) is a true
   line-for-line mirror of `r3_config()` (lines 192–210), and the aperture
   half-width in **physical units** is bit-identical across all three
   families — `A_HALF_APERTURE·dx_native = 752×3e-8 = 2.256e-5 m`;
   `A_R3·dx_R3 = 1128×2e-8 = 2.256e-5 m`; `A_R4·dx_R4 = 1504×1.5e-8 =
   2.256e-5 m` — the same identity the committed gate 3 checks for the shell
   radius specifically, but true (and independently confirmed here) for the
   aperture length too, algebraically guaranteed by the shared recipe rather
   than separately gated. The angular/diffractive physics this cross-`cpl`
   comparison depends on (a fixed `λ/A_phys`) is therefore genuinely held
   fixed, not merely asserted.
3. **The absorbed-power channel stays essentially flat across the same
   resolution change** (`p_abs_w` G4/C4 ratio 1.0029–1.0057, ≤0.6% deviation,
   all six angles) while the coherent channel reverses completely. This is
   the correct signature of a *narrow-linewidth coherent phase effect*
   specifically, not a generic numerical blow-up — a resolution-driven
   artifact broad enough to flip an entire six-point sign pattern would be
   expected to also perturb the smoother thermodynamic channel by more than
   noise, and it does not (R14's own established mechanistic account,
   `ratio_abs_ext` flat/config-invariant, continues to hold at a third
   resolution, exactly as `NOTES.md`'s Learned #2 states and I independently
   confirm above).

Given T28's own multiply-null-permutation-verified (`p<5×10⁻⁵`, several
independent cycles) narrow carrier period (~2.84°–2.95°) and an interior
window only 0.15° wide, a resolution-dependent shift of the underlying
near-total-cancellation trough's *location* by a fraction of that period is
not exotic — it is the generic behavior of a fragile local minimum formed by
two comparable-magnitude, oppositely-tending contributions (exp-093's own
Phase-5 PHOTONICS review already characterized this exact trough as "a
textbook near-degenerate local minimum... generically fragile to ANY small
perturbation"). A cheaper, more specific account than plain Yee-dispersion
phase accumulation (already REFUTEd as the ~2.84° period's *origin* by
exp-093's own item 4, discharged again bit-exact here — `2×0.25×156 =
2×0.5×78 = 78.0`, gate 6 confirmed) is this program's own established T10
mechanism: **curved-boundary staircasing**, whose exact stairstep pattern
approximating `graded_black_shell`'s circular profile does not vary smoothly
with `cpl` — a doubled-resolution mesh does not merely halve an existing
error, it re-tiles the curve with a discretely different pattern. That
naturally produces a qualitatively different-looking trough location rather
than an intermediate one, which is consistent with what was measured (a
clean flip at all six points, not a partial one at the window's edge).

**Attack.** None of the above tells us which resolution (if either) is
closer to the true continuum answer, and the record does not claim it does.
With only two data points on this specific interior window
(`cpl=30`→SINGLE-NULL, `cpl=40`→uniformly CONSISTENT), a monotonic
node-migration story, an oscillating-with-`cpl` story, and a genuinely
non-convergent-at-any-affordable-`cpl` story are all equally consistent with
the data — `NOTES.md`'s own Next item 1 says this explicitly and correctly
(a `cpl=50`+ point is needed to distinguish them), and I concur this is the
correct, undischarged state of the evidence, not an oversight. Separately: `R13`'s `FLOOR` is carried into this comparison **entirely
unrecalibrated across three different discretizations** — it was fixed once
from `exp-083`'s native-`cpl=20` 31-point window (independently confirmed:
`results.json::r13_floor_gate` here is bit-identical, `1.917438e-4`, to
`exp-093`'s own value) and applied verbatim to `cpl=30` and now `cpl=40`
data (Idealization 6, correctly disclosed, not new to this cycle). Whether a
noise/discretization floor calibrated at `cpl=20` is still the right scale
to gate a `cpl=40` measurement's significance is an open question this
cycle does not raise or test — non-load-bearing here only because Rank 1b's
margins are wide (`ratio_k` 3.67–7.13, `floor_pass` never close to the edge
at any of the six points), so I do not treat it as outcome-determining, but
it is a genuine unclosed gap specific to a *cross-resolution* comparison
that should be named as such rather than folded silently into the general
"FLOOR not recomputed" idealization.

**Net physical read**: the reversal is coherent with, not contradictory to,
this bench's own established physics — a real near-field coherent
interference feature whose node location is resolution-sensitive, most
plausibly via curved-boundary staircasing rather than smooth dispersion
(already ruled insufficient as the period's origin). It is not evidence the
`R4` family is defective. But it is also not yet evidence of *convergence* —
the window's status is genuinely unresolved across three resolutions, exactly
as `NOTES.md` itself states, and I do not find grounds to sharpen that
either toward "converging" or "artifact" beyond what is already disclosed.

## 2. Gate 5 — independently re-run this session, not merely trusted

`NOTES.md`'s Result section and Learned #4 both assert Gate 5 was
"independently confirmed during Phase 4 to be a genuine discriminator... by
injecting a simulated R15-style wiring defect into a standalone test harness
... (correctly raised `AssertionError`)." **No such test harness, script,
or output exists anywhere in this experiment's committed directory** (checked
directly: `run.py`, `results.json`, `run_output.txt`, and `__pycache__`
contain nothing matching "test harness," "inject," or a second script; only
`run.cpython-311.pyc` — the compiled `run.py` itself — is present). This is
an R4-shape gap: a specific verification event is cited as evidence in the
permanent record with no committed artifact behind it.

Per this house's own standard (verify, don't take on faith), I reconstructed
the fault-injection test myself this session, loading the actual committed
`run.py` module and calling its real `build_article_r4_sigma`/`_grids`
machinery with a deliberately mismatched `sigma_max` (built the shell at
`SIGMA_NATIVE=0.5`, checked Gate 5's own assertion against
`SIGMA_R4_CORRECTED=0.25`, reproducing exactly the "stray `SIGMA_NATIVE`
where `SIGMA_R4_CORRECTED` belongs" defect shape MATERIALS' Phase-2 critique
named): **it correctly raised `AssertionError`** (`sim.sigma_e[shell_mask]
.max()=0.5` vs expected `0.25`). The underlying scientific claim is true —
Gate 5 genuinely discriminates, confirmed independently, from the real
committed code, this session. But `NOTES.md`'s own citation of a Phase-4
verification event that left no trace anywhere in the repo is exactly the
kind of unverifiable-from-the-record assertion R4 exists to prevent, even
when (as here) it happens to be substantively correct. Recommend: either
persist the fault-injection check as a small committed script/output (cheap,
reusable for the "retrofit onto `R3`'s own sigma call sites" follow-up
Learned #4 itself proposes), or soften the claim to "verified by the
reviewing author, not preserved as a committed artifact."

## 3. A genuinely new, independently-checked arithmetic imprecision

`NOTES.md`'s Result section states 38.4°'s flip is "a **larger absolute
swing** than 41.4°'s own precedent-setting flip at exp-091 (28.85→9.21...)."
Recomputed both, from primitives:

- 38.4° (this cycle): `0.9075118 → 16.9967271`, raw difference **16.089**,
  fold-factor **18.73×**.
- 41.4° (exp-091, independently re-pulled from `experiments/091-.../
  results.json::b.per_theta["41.4"]`): `28.8072 → 9.211608`, raw difference
  **19.596**, fold-factor **3.13×**.

Under the most natural reading of "absolute swing" (raw magnitude of
change), **41.4°'s swing (19.60) is larger than 38.4°'s (16.09)** — the
opposite of what is claimed. The claim is only true under a *fold-change*
reading (18.73× vs. 3.13×), which is very likely what was intended (the
same sentence's immediately preceding clause already frames 38.4°'s own
change as "a factor of 19"), but "absolute" is the wrong word for a
ratio/factor and, read literally, states something false. Non-load-bearing
(no gate, band, or classification depends on this comparison — it is
narrative color in the Learned section), but it is exactly the class of
"wrong-but-non-binding claim entering the permanent record" this house's
R4/R9 discipline flags regardless of stakes. Recommend: replace "a larger
absolute swing" with "a larger *fold-change*" or drop the comparison
entirely.

## 4. Process-completeness / record hygiene

No other defects found. `NOTES.md`'s Hypothesis/Setup/Predictions sections
match `phase3_synthesis.md`'s frozen spec exactly (all five mandatory fixes
correctly landed — Gate 5 present and load-bearing, Rank 2's struck lean
correctly replaced with the no-lean framing, the `_full`-variant/
`netd_disclaimer` carry-forward correctly stated and correctly present in
`results.json`, the `p_abs_w` T9-anchor check present and reported for Rank
1b, Idealization 18's EM-derivation credit present). The Result section
accurately reports the pre-registered category outcomes without
downweighting the surprising one, and explicitly does not smooth the
TWO-NODE CONFIRMED technical label into something softer than what the data
show (correct, and independently confirmed accurate at §0 above). The
carried-idealizations banner is present and complete in both the
Idealizations and Predictions sections.

## 5. Verdict

**CONCUR-WITH-GAP(S).**

I concur that the `R4` cpl=40 geometry family is faithfully, independently
re-derivable as a physical-length-preserving mechanical rescale of the
already-trusted `R3` recipe, that Gate 5 genuinely discriminates the exact
R15-founding defect shape it was built to catch (verified myself, from
source, this session), and that the reported full-window sign-and-
classification reversal is an accurately reported, physically coherent
(not artifactual-on-its-face) finding whose ultimate convergence status the
document correctly and honestly leaves open rather than oversells. Two
independently-verified, non-load-bearing gaps: (a) the Gate-5
fault-injection verification claim cites an event with no corresponding
committed artifact — true on independent re-test, but not verifiable from
the record as filed (§2); (b) the "larger absolute swing" 38.4°-vs-41.4°
comparison is imprecise and, under its most natural reading, backwards (§3).
Neither moves any gate, band, or the Combined Verdict.

## 6. Ranked candidate directions for Iteration 72 (PHOTONICS)

1. **A third resolution point (`cpl=50` or higher) at the same six interior
   angles**, exactly as `NOTES.md`'s own Next item 1 proposes — the single
   test that can distinguish converging, oscillating, or genuinely
   non-convergent behavior in this window, and the most direct way to learn
   whether Idealization 17's "not independent confirmations of the
   re-discretization scheme" caveat is actually biting here or not.
2. **Recalibrate (or explicitly re-justify) R13's `FLOOR` at each new `cpl`
   family** before it gates another near-boundary classification — a
   cpl=20-derived noise floor applied unmodified to cpl=40 data is a
   disclosed but never-tested comparability assumption (§1, Attack), cheap
   to check (recompute RMS[frac_contrast] over an equivalent dense window at
   `cpl=30`/`cpl=40` and compare to the `cpl=20` value already on file).
3. **PHOTONICS' own long-standing grazing-incidence validity check** — still
   the single most-repeated undischarged item on the whole T28 board (named
   at Iterations 64/65/67/68/69/70), and now directly load-bearing to
   whether the analytic boundary-reflectance picture this near-null region's
   own history has repeatedly leaned on (exp-075/077/078/079/080/081's own
   two-wall/y-wall echo models, all REFUTEd or foreclosed) has ever been
   checked at the *actual* incidence angles this specific window sits at.
