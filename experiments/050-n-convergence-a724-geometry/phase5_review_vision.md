# PHASE 5 — REVIEW (VISION SCIENCE) · Panel Iteration 27 · exp-050

## 0. Charter framing

This cycle issues no mechanism, no material, no T1 escape route, and — by
its own explicit scope — no constraint-3/4 verdict. My duty here is narrow
and specific to the Director's brief: (a) verify my own Phase-2 requested
fix (P-NCONV27-6b) was delivered faithfully and completely; (b) assess,
from perceptual-threshold discipline, whether the 27× headroom swing at the
sharpest-stakes cell creates a real risk that a future citation misreads
"n-convergence CONFIRMED" as "perceptually safe"; (c) judge whether
NOTES.md's own disclosure is adequate; (d) check whether P-NCONV27-2's
REFUTED outcome opens any new risk near these angles/wavelengths. No
constraint-3/4 verdict is issued below — consistent with this cycle's own
scope.

## 1. P-NCONV27-6b: delivered faithfully — verified against `results.json`, not NOTES.md's prose

I read `results.json`'s `predictions.P_NCONV27_6` and
`predictions.P_NCONV27_6b` blocks directly, not NOTES.md's narrative, per
this program's own R4 discipline (LOGBOOK, adopted Iteration 25).

- `c_geom78_converged` = **+1.4646953954144948×10⁻⁴** — matches NOTES.md's
  Results-table figure exactly, digit for digit.
- `c_geom042old` = **−4.006497410421138×10⁻³** — matches.
- `headroom_pct_geom042old` = **24.79728520464539** (→ "24.8%" in NOTES.md) —
  matches.
- `headroom_pct_geom78` = **3313.679059587026** (→ "3313.7%") — matches.
- `ratio_geom042old_over_geom78` = **27.353792624488573** (→ "27.35×") —
  matches.
- `sign_flip` = **true** — matches the stated sign flip.
- `redteam_precheck_new_relative_error_to_2sf` = 0.000208 (0.0208%) — NOTES.md
  reports "0.021% relative," a correct 2-sig-fig rounding, and correctly
  frames this as cross-validation between Red Team's pre-Phase-4 scratch
  code and the Director's independently-committed `design_geometry.py`, not
  a rubber stamp.

I also independently spot-checked the two flanking angles at this same
(750nm, FWHM=2°, `incoherent_corrected`) row family — see §3, below, where
this check surfaces a second finding NOTES.md does not carry.

**Verdict on delivery: faithful and complete.** Every number in NOTES.md's
`P-NCONV27-6b` row traces exactly to the committed record. The
mandatory-fix docket item my own Phase-2 critique produced (Attack 6 /
mandatory-fix 4) was executed as specified: the actual converged value is
reported, not just the pass/fail band, and it is reported as a distinct
table row (`P-NCONV27-6b`, outcome `CROSS-VALIDATED`) rather than folded
silently into `P-NCONV27-6`'s own clean n-convergence pass. That structural
separation — stability-of-the-numerics in one row, magnitude-of-the-physics
in the next — is exactly what I asked for at Phase 2, and it is the right
design.

## 2. Does the 27× swing risk a future misreading of "CONFIRMED" as "safe"? Yes — and this cycle's own data sharpens that risk further than NOTES.md discloses

**The core hazard is real, not hypothetical.** `P-NCONV27-6` (n\*=41
unchanged, relative move 0.0% under doubling) and `P-NCONV27-6b` (value
swings 27.35× and flips sign under a 3.7% *geometry* perturbation, not a
quadrature-order perturbation) are answers to two entirely different
questions that happen to share a cell coordinate. N-convergence certifies
that increasing the angular quadrature order `n` no longer changes the
computed value — a statement about numerical stability of one propagator
evaluation. It says nothing about how sensitive that same propagator's
output is to the physical geometry it is evaluated at. This cycle proves,
with a real measured pair of numbers, that these two properties can be
completely decoupled: a cell can be numerically rock-solid (`n*` unchanged,
move 0.0000%) while its physical value is maximally fragile (order-of-
magnitude swing, sign flip) under a change an order of magnitude smaller
than the numerical perturbation being certified. A citation that reads only
the `P-NCONV27-6` row — "CONFIRMED, no flip" — and treats that as license to
carry a headroom number to a nearby geometry would be reading a numerical-
stability claim as a physical-stability claim. That is exactly the
conflation risk my Phase-2 attack named, and Red Team's Attack 6/targeted
computation independently confirmed the same reading: "a purely
n-convergence-scored prediction... can read CONFIRMED, cleanly, at both
geometries, while the actual physical quantity underneath it swings by more
than an order of magnitude and changes sign."

**NOTES.md's disclosure is adequate at the level of the number, inadequate
at the level of the rule.** The Results-table row for `P-NCONV27-6b` states
the swing plainly (27.35×, sign flip, both headroom figures) — nothing is
hidden or softened there. But NOTES.md's **Reading** section — the
prose meant to tell a future reader what this cycle actually establishes —
discusses `P-NCONV27-2` at length and says nothing about `P-NCONV27-6b` at
all. The generalizable lesson (n-convergence stability and geometry
stability of the converged value are independent properties, and a
"CONFIRMED" tag on the former licenses no inference about the latter) lives
only inside one prediction row's own text, not as a named, citable rule any
future Phase-1 proposer would find without re-deriving it from the table.
That is the same "not re-derived unprompted" failure mode ELECTROMAGNETISM
named in its own Phase-2 critique of this exact cycle (re: the
obliquity-on-E convention's provenance) and the same pattern LOGBOOK's own
R4 rule and T15/T23 threads exist to prevent for other classes of
undisclosed fragility.

## 3. A second, sharper finding this review surfaced directly from the committed data — not narrated anywhere in NOTES.md

Checking whether the "sharpest-stakes cell" label itself survives the
geometry change, I read the immediate angular neighbors of the P-NCONV27-6b
cell (750nm, FWHM=2°, `incoherent_corrected`, θ₀ = 36°/38°/40°) at both
geometries directly from the committed `results.json` files
(`experiments/049-.../results.json` `per_cell_summary` for A=752;
`experiments/050-.../results.json` `per_cell_summary_geom78` for A=724):

| θ₀ | A=752 (`incoherent_corrected`, converged) | A=724 (`incoherent_corrected`, converged) |
|---|---|---|
| 36° | +1.7046×10⁻³ | **−5.4503×10⁻³ — EXCEEDS C_THR=0.005** |
| 38° | −4.0065×10⁻³ (24.8% headroom, worst of the three) | +1.4647×10⁻⁴ (3313.7% headroom, best of the three) |
| 40° | −2.9086×10⁻³ | **+6.4986×10⁻³ — EXCEEDS C_THR=0.005** |

At A=752, 38° was correctly identified as the sharpest-stakes point of this
angular triplet — the closest to threshold, both flanks comfortably below
it. At A=724, that ranking **inverts completely**: 38° becomes the safest
point (a near-perfect fringe null) while its immediate 2°-step neighbors on
*both* sides now breach `C_THR` outright, in the raw, unscaled reading — a
threshold crossing that did not exist in the raw reading of this triplet at
A=752 (Iteration 19's own record shows the raw incoherent-family reading
was 0/36 exceeding at A=752; only the amplitude-corrected `c*`-scaled
reading pushed the 38° cell above threshold there). This is not a new
computation or a new claim about physics — it is a direct read of numbers
already sitting in this cycle's own committed `per_cell_summary_geom78`
table, which NOTES.md's Results table and Reading section never mention.

**Why this matters more than the single-cell swing already reported:** it
shows the fragility is not a property of one coordinate, it is a property
of the *angular fringe itself* at this wavelength/FWHM/geometry — the same
mechanism PHOTONICS flagged at Iteration 25 (a 9-angle/10°-step FALLBACK
grid is far coarser than the ~1.5–2.6° fringe period it characterizes,
"the reported worst point is very likely not the true worst phase")
demonstrated concretely here at a much finer 2°-step grid: the fringe
genuinely oscillates from safely-below to above-threshold within two
degrees, twice, on either side of the one cell this cycle's own prediction
table tracks. A future reader citing "GEOM78's 38° cell is safe, 3313%
headroom" without also reading the immediately adjacent grid rows would be
citing the deepest null in a pattern that breaches threshold one grid-step
away in both directions — a materially worse misreading risk than the
27×-swing finding alone conveys.

## 4. P-NCONV27-2's REFUTED outcome: no new perceptual risk from the three actual violations, but a real forward-looking gap in the exemption mechanism's coverage

I checked the magnitude of all three violating cells directly
(`results.json` `predictions.P_NCONV27_2`, cross-referenced against
`per_cell_summary_geom78`): the pre-registered exempt violation
(750nm/40°/FWHM=20°) and both unpredicted 600nm violations (36°, 40°,
FWHM=20°) all have converged `|C|` values of order 10⁻⁴ — two to three
orders of magnitude below `C_THR=0.005`. **None of these three cells poses
any near-term perceptual/contamination risk**; they are deep in the
"exempted" regime (`|C| < C_THR`) where the convergence criterion's own
relative-error clause is switched off by design, and NOTES.md's own Reading
section correctly identifies this. From my seat, P-NCONV27-2's REFUTED
result does not, by itself, sharpen any risk near these specific angles or
wavelengths for a future perceptual citation — none of the three cells sit
anywhere near the threshold that would make them citable in a constraint-3
context at all.

**What it does establish, and what NOTES.md's own honest framing already
says**: the two pre-registered mechanisms (Nyquist-sampling proximity,
grating-lobe-replica truncation) that Red Team resolved the risk zone to
before Phase 4 do **not** exhaustively characterize where tier instability
occurs at GEOM78 — two violations landed at coordinates neither mechanism
flagged. This is a genuine, disclosed gap in the *predictive* model, not
the *measured* result (P-NCONV27-1's global max n\*=81 still holds; every
actual value is known). The practical consequence for VISION's own
concerns is indirect but real: if a future cell nearer to `C_THR` needs
similar n-convergence characterization, this cycle's own record shows the
currently-understood risk factors (Nyquist proximity, aperture truncation)
cannot be trusted alone to bound where instability will occur. Combined
with §3's finding — that the fringe pattern surrounding the one
threshold-adjacent cell this program actually tracks already breaches
threshold at immediate neighbors — this is a reason for caution about any
future *sparse* angular characterization near this geometry, not evidence
of an active miss in the present record.

## 5. Verdict

**PARTIAL.**

Not RULED OUT — nothing here refutes any physics or falsifies this cycle's
own predictions beyond what NOTES.md already scores (7 CONFIRMED, 1
REFUTED, 1 CROSS-VALIDATED, exactly as reported, verified against
`results.json` directly). Not PROMISING either, from this seat's narrow
brief: the requested fix (P-NCONV27-6b) was delivered completely and
accurately at the level of the raw numbers, but the cycle's own narrative
synthesis under-communicates the generalizable risk that prompted the fix
in the first place, and this review's own pass over the already-committed
data surfaced a materially sharper, wholly undisclosed instance of the same
risk (§3) sitting one grid-step away from the one cell the cycle does
discuss. Both are same-shift-fixable (zero new computation — the numbers
already exist in `results.json`) but neither has been fixed yet.

## 6. Ranked candidate next steps for Iteration 28 (VISION SCIENCE's ranking)

1. **[Zero cost, same-shift-eligible] Promote the n-convergence/geometry-
   stability decoupling to a named, citable rule**, not a sentence buried in
   one prediction row. Add an explicit paragraph to NOTES.md's Reading
   section (or a new LOGBOOK live-thread addendum under T21/T24) stating
   plainly: n-convergence CONFIRMED at a cell certifies numerical stability
   under quadrature refinement only; it licenses no inference about the
   physical value's stability under geometry changes, however small — any
   future near-boundary headroom citation must be re-measured at its own
   citation's actual geometry, not inherited from a nearby one even when
   both read "CONFIRMED."
2. **[Zero new computation, same-shift-eligible] Disclose the §3 finding
   in NOTES.md/`results.json`**: at GEOM78 (A=724), the raw
   `incoherent_corrected` reading at 750nm/FWHM=2° exceeds `C_THR=0.005` at
   both 36° and 40° (immediate 2°-step neighbors of the one cell this cycle
   tracks), a threshold crossing that did not exist in the raw reading of
   this angular family at A=752. The data is already in
   `per_cell_summary_geom78`; this is a documentation gap, not a new run.
3. **[Zero new FDTD, moderate desk cost] A sub-degree angular-resolution
   desk sweep (0.25–0.5° step) across 36°–40° at 750nm/FWHM=2° at GEOM78**
   — PHOTONICS' Iteration-25 priority, never executed, now directly
   motivated by a concrete measured swing (not a generic worry) at exactly
   this geometry/wavelength/FWHM combination. Needed to locate the true
   worst angle in this band, since the current 2°-step grid has already
   been shown, at this exact geometry, to alternate between a deep null and
   two threshold-exceeding peaks within 4° of arc.
4. **[Real FDTD cost, already LOGBOOK-queued] Execute Iteration-26/27's own
   priority (2): a genuine FDTD `ABSORB` sweep at the T21-vs-T24 geometry**,
   now better justified than when queued — this cycle shows the desk-level
   n-convergence uncertainty at the sharpest-stakes cell is confirmed
   negligible (~0%), and §3's finding shows the physical uncertainty
   (fringe phase across ~2° steps) plus T24's own uncharacterized
   ~0.002–0.007 ABSORB-boundary systematic are now the dominant unresolved
   sources at exactly the angular band this cycle's own data flags as
   threshold-crossing.
