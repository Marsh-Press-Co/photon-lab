# PHASE 5 — REVIEW · PHOTONICS · Panel Iteration 72 · exp-095

*Blind, parallel review. No access to any other seat's Phase-5 output this
cycle. All figures below independently recomputed from `results.json`/
`NOTES.md`/`run.py`/LOGBOOK.md primitives this session — not taken from
any document's own prose (R4/R9 discipline).*

## 0. Independent re-derivation of the headline numbers

Pulled directly from `results.json::rank1.rank1c.per_theta`:

- `38.49°`: `delta_scene = -1.5168400043253927e-3`, `floor_pass=True`,
  `frac_contrast=2.698917922646329e-3`.
- `38.69°`: `delta_scene = -2.538530922948423e-3`, `floor_pass=True`,
  `frac_contrast=4.540115398680884e-3`.

Both **bit-exact** to the task's own cited figures (`-1.516840e-3`/
`-2.538531e-3`) and to `run_output.txt`'s printed values. Both negative,
both `floor_pass=True` → the pre-registered FAIL criterion ("both
floor-clear but SAME sign") is correctly triggered; `rank1c.verdict="FAIL"`
and `proceed_gate=false` are the right mechanical outputs of `NOTES.md`'s
own frozen rule, independently reproduced from `run.py`'s own gate logic
(lines 638–648): `rank1c_signs_differ = signs[0] != signs[1]` → `False` →
`verdict="FAIL"`; `proceed_gate = (rank1a=="PASS") and (rank1c in
{"PASS","INCONCLUSIVE"})` → `False`. No arithmetic or wiring defect in the
gate itself.

Margins against `R13`'s `FLOOR=1.917438e-4` (unrecomputed, Idealization 6,
independently confirmed unchanged from exp-091/092/093/094): `38.49°`
clears by **14.08×**, `38.69°` by **23.68×** — both comfortably
well-powered reads, not borderline floor calls. Rank 1a (39.2°/39.4°, both
negative, both floor-clearing, matching both cited comparators in sign)
also reproduces exactly. The Rank-1 combined gate and Rank-4 `NEITHER`
(`floor_pass=False`, `|delta_scene|=2.939e-6`, only 1.5% of `FLOOR`) all
check out against primary source.

## 1. Is a same-sign, both-floor-clearing FAIL at 38.49°/38.69° physically
plausible as node migration, or does it read as "no crossing nearby"?

**Steel-man for "genuine migration, window just too narrow."** T28's own
established period for `delta_scene(θ)` is ≈2.84°–2.95° (R13's founding
record, confirmed against the exp-083 dense grid I re-pulled directly —
see below), and this exact sub-thread has *already measured*, at a single
resolution step (`cpl=20→30`), a migration of **−0.194°** at the
neighboring lower crossing (`40.265420°→40.071838°`, exp-092's own Rank-1,
independently re-confirmed: `40.265420−40.071838=0.193582`). A ±0.1°
half-width bracket is narrower than that single already-measured
migration distance — before any new data even runs, the geometry of the
test is tight relative to this channel's own demonstrated behavior.

**Attack, and my own sharpest finding: this cycle's own data, not merely
history, already localizes this specific null far outside the tested
window — and NOTES.md never connects the two.** I pulled the raw `cpl=20`
dense grid directly (`experiments/083-.../results.json::thetas`/
`delta_scene`), not from any citation:

```
38.400°  +8.083349e-4
38.600°  -4.151305e-5
38.800°  -8.568729e-4
```

Two independent facts, both already sitting in this cycle's own
`results.json`, converge on the same conclusion:

1. **The Rank-4 leg of *this very cycle*** measured 38.4° at `cpl=30`,
   *corrected* sigma (`R3` family): `delta_scene=-2.939×10⁻⁶`, only
   **1.5% of `FLOOR`** — the reading is, to instrument precision,
   sitting almost exactly *on* a zero-crossing. That is a direct,
   well-localized measurement placing the corrected-sigma `cpl=30`
   crossing at essentially `θ≈38.4°` — a **≈0.19° shift** from `38.590°`,
   matching the lower crossing's own independently-measured `−0.194°`
   migration to two significant figures. (A companion, same-direction
   signal exists at *native* sigma too: exp-094's own already-filed Rank-3
   census shows 38.4° flipping sign between `cpl=20` (+8.083×10⁻⁴) and
   `cpl=30` (−1.632×10⁻⁴, `results.json::rank3.per_theta["38.4"]`,
   independently re-pulled) — a local sign change of its own, consistent
   with the same crossing having already crept past 38.4° by `cpl=30`.)
2. **A magnitude-scale check on the two tested Rank-1c points themselves
   argues against "just barely outside ±0.1°."** If the `38.590°` null
   simply held its `cpl=20` location while the whole curve scaled up by
   this cycle's own measured far-field amplitude growth (39.2°/39.4°
   comparators grow `cpl20→cpl40` by 1.72×/1.39×, average 1.55×), linear
   interpolation off the *unshifted* `cpl=20` dense grid predicts
   `delta_scene(38.49°)≈+6.6×10⁻⁴` and `delta_scene(38.69°)≈−6.4×10⁻⁴` —
   small, and **opposite in sign**, i.e. still straddling zero. The
   observed `cpl=40` values are **2.3×–4.0× larger in magnitude and the
   same sign** — not what "the null merely grew in place and shrank just
   inside the ±0.1° bracket" predicts. Both tested points already read at
   40–80% of this cycle's own *deep far-field* scale (39.2°/39.4°: −2.6
   to −3.15×10⁻³), not the order-of-magnitude-suppressed values a point
   genuinely adjacent to a crossing shows (compare: within 0.1°–0.2° of
   `38.590°` at `cpl=20` itself, magnitudes run 10⁻⁴–10⁻⁵, one to two
   orders of magnitude below the far field).

Both signatures point the same direction: **not** "no crossing anywhere
near here," but "the crossing has moved — plausibly to θ ≲ 38.4°, i.e.
*below* the tested window, by an amount at or somewhat past this exact
sub-thread's own established ~0.19° single-step migration scale."
The monotonic magnitude ordering *within* Rank 1c's own two points
(`|Δ(38.49°)|=1.52×10⁻³ < |Δ(38.69°)|=2.54×10⁻³`, continuing to grow
through 39.2° before turning over) is consistent with approaching a
smooth minimum from *above* a crossing sitting somewhere below 38.49° —
the same direction the Rank-4 localization independently indicates.

**Caveat, stated plainly rather than glossed over.** This is a
convergence-of-evidence argument, not a proof. The Rank-4 anchor mixes two
changes at once relative to `38.590°` (resolution refinement *and* the
sigma correction), so it cannot cleanly attribute the ≈0.19° shift to
`cpl` alone the way exp-092's own Rank-1 crossing search could. And this
exact channel has *also* shown the opposite qualitative behavior one
window over: exp-093's `cpl=30` denser sweep at 41.75°–41.90° found
*no* interior crossing at all (SINGLE-NULL) where exp-092's sparse
3-point net had inferred two, and exp-094's `cpl=40` family then
*reversed the entire span* relative to that — a directly-precedented
"the local topology itself changed, not merely shifted" outcome on the
identical construction recipe. I cannot rule that out here from two
points. What I *can* rule out, quantitatively, is the reading closest to
"business as usual, mild miss": the observed values are too large and
too same-signed for a crossing that merely sits just past 38.49° or
38.69° at roughly the `cpl=20` local slope, even after generously scaling
for this cycle's own measured amplitude growth.

## 2. A second, narrower angular-dependence point: the window itself was
undersized relative to this sub-thread's own history, independent of what
was found

Framed only from what a resolution check on an oscillatory signal with a
known period requires: every migration or restructuring event this
program has *already measured* on this exact channel and construction
recipe exceeds a ±0.1° half-width — the lower crossing's 0.194° single-
step shift, and the upper window's outright topology change across two
steps. A bracket sized below the smallest of these precedents is,
independent of any single cycle's outcome, testing at a resolution finer
than the phenomenon it is built to detect is known to move at. This is a
design-time observation, not a post-hoc one — the ±0.1° figure could have
been checked against the 0.194° figure (already on file since exp-092)
before Rank 1c ran, and Idealization 28 ("tests presence, not exact
location") does not by itself flag that the half-width itself might be
smaller than the established migration scale.

## 3. Process-completeness / record hygiene

`NOTES.md`'s Rank 1c section (Predictions and Setup) is accurately
written to its own frozen spec and correctly reports the FAIL outcome
without softening it. `results.json`'s `rank1c` block is complete and
internally consistent with `run_output.txt`. I found no misreported
number, no silent floor-gate override, and no mismatch between the
pre-registered PASS/INCONCLUSIVE/FAIL taxonomy and what actually printed.
The one gap is interpretive, not a record-hygiene defect: neither
`NOTES.md` nor the printed summary cross-references Rank 4's own
same-cycle 38.4°-near-null finding against Rank 1c's own question, even
though both target variants of the identical `θ₀≈38.590°` feature and the
former materially sharpens how the latter's FAIL should be read.

## 4. Verdict

**CONCUR-WITH-GAP.**

Rank 1a and Rank 1c are both correctly computed from primary data, and the
combined go/no-go gate mechanically fired exactly as pre-registered — no
defect in the gate logic itself. From this seat's own charter (angular
dependence, scattering coherence): a same-sign, both-floor-clearing
outcome at 38.49°/38.69° is **not** evidence that no zero-crossing exists
near 38.590° in the `R4` family in any strong sense; it is better read as
evidence that the ±0.1° bracket was undersized relative to this exact
sub-thread's own already-measured migration scale, and — using this
cycle's own Rank-4 leg as an independent anchor, not previously connected
to Rank 1c in the record — the true `cpl=40` crossing most plausibly sits
below 38.49°, consistent with, not contradicting, a genuine (if larger
than anticipated) node-migration story. The weaker, magnitude-driven
alternative ("no crossing anywhere nearby") is not supported once the
Rank-4 cross-reference is included — it was only the more defensible read
looking at Rank 1c's two points in isolation.

## 5. Ranked candidate directions for Iteration 73 (PHOTONICS)

1. **Re-run the node-bracketing recovery check with a re-centered,
   widened window** — informed by this cycle's own Rank-4 anchor, not
   the stale `cpl=20` location: bracket something like 38.0°–38.5° (a
   half-width comfortably exceeding the established 0.194° single-step
   migration scale) in the `R4` (`cpl=40`) family at *corrected* sigma,
   the same leg Rank 1c used, so the sigma variable stays fixed and only
   the window moves. This is the single most direct way to convert this
   cycle's ambiguous FAIL into either a located crossing or a genuinely
   surprising "still nothing nearby" result.
2. **A native-sigma companion at the same relocated window** — mirroring
   Rank 3b's own native-vs-corrected discipline — since R15's addendum
   history shows native/corrected sigma alone can flip sign at fragile
   points (exp-093 Item 3, 42.0°); the 38.590° null has never been
   checked for this specific confound the way the 41.6°–42.0° window has.
3. **PHOTONICS' own long-standing grazing-incidence validity check** —
   still the single most-repeated undischarged item on the whole T28
   board (named at Iterations 64/65/67/68/69/70/71) — now doubly
   motivated: if the analytic boundary-reflectance/staircasing picture
   this near-null region's history keeps invoking has never been checked
   at the actual incidence angles this window sits at, neither has the
   assumption, implicit in every ±0.1°-scale bracket this sub-thread has
   chosen, that node-migration distance itself doesn't also depend on
   incidence angle in a way that would make a single fixed half-width
   wrong across different windows on the same curve.
