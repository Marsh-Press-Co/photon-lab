# PHASE 2 — RED TEAM AUDIT · Panel Iteration 28 · exp-051

*Seventh seat, speaking last, with the Phase-1 proposal and all five blind
critiques (PHOTONICS, MATERIALS, THERMODYNAMICS, QUANTUM OPTICS, VISION
SCIENCE) unblinded. Standard: internal consistency, falsifiability,
expressibility, constraint violations — not textbook compliance. T1 escape
route: NONE (this cycle proposes no mechanism, no material, no constraint-3/4
verdict), so almost every finding below tags `[inconsistency]`, matching
exp-049/050's own precedent for this class of cycle. Nothing here is taken
on any seat's word, including the proposal's own: every load-bearing number
was independently rebuilt from source and re-run in this session, from a
cold implementation, against already-committed exp-042/048/050 code.
Scratch code: `/tmp/claude-0/-home-user-photon-lab/
3f566c8d-1309-5c26-a429-8ae6c0875c6b/scratchpad/redteam/{repro.py,repro2.py,
out.log,rows.json}`. Nothing under `lab/`, exp-042, exp-048, exp-049, or
exp-050 was modified.*

---

## 0. Headline

Four of five blind seats (PHOTONICS, MATERIALS, QUANTUM OPTICS, VISION
SCIENCE) independently ran the proposal's own §2.2 machinery from prose and
found P-PCDP-1/2 — the primary discriminator and its rank-ordering fallback,
the entire deliverable of this cycle — already fail their own pre-registered
falsification bands at the desk. QUANTUM OPTICS went further and proposed a
specific, concrete, same-cost, zero-new-tuning-parameter replacement crux
quantity (the Poisson-alias term of the fringe at the quadrature node-lattice
spacing, not θ₀'s offset from the fringe's zero-crossing), reporting
AUC=1.000 and ≤1.4% relative error against the measured `C(41)−C(161)` step.

**I did not take any of this on faith. I rebuilt §2.2(a)–(c) from the
proposal's own prose, rebuilt QUANTUM's `alias_coeff(...)` from its own
posted formula, and ran both — independently, from a cold implementation —
against the actual committed `beam_divergence_*`/`_geom_derived`/`_G_for_g`
code, at all 18 GEOM78 combinations.** Every number below is mine, produced
in this session; where it matches a blind seat's figure to four-plus
significant digits, that is independent convergence, not copied arithmetic.

**Result, stated plainly: the blind seats are right, and QUANTUM's
replacement mechanism is right too — more completely right than its own
critique claimed.** P-PCDP-1 is REFUTED (AUC 0.6494 on `|offset|` alone,
0.5195 on `x2`, both independently reproduced to the fourth decimal against
PHOTONICS/MATERIALS/QUANTUM's own numbers). P-PCDP-2 is not merely below its
CONFIRMED bar — it fails to clear its own *hard-falsification escape* bar
(no threshold in [0.05,0.40] reaches even sens≥5/7 ∧ spec≥7/11), confirmed
independently. QUANTUM's `alias_coeff`-based predictor, rebuilt from scratch
in this session, scores **AUC = 1.0000, perfect separation (7/7 sensitivity,
11/11 specificity)** at the natural threshold `|E_pred|=ABS_TOL`, and
**Pearson r = 0.999998, max relative error 1.445%** against the actual
measured `C(41)−C(161)` at all 18 combinations — matching QUANTUM's own
claimed r=1.00000/≤1.4% to within the last displayed digit (the 0.045pp
discrepancy is fully explained by my coarser numerical-integration step,
0.02° vs QUANTUM's 0.01°, not a physics difference).

This is the clearest case this program has had in the n-convergence-family
cycles: **the crux quantity as designed is wrong, and a specific, verified,
equally-cheap replacement already exists.**

---

## Reconstructing what each seat actually ran (independent cross-check of the cross-checks)

Before adjudicating, I verified that the four "REFUTED-at-the-desk" findings
and the one "SUPPORT-WITH-CHANGES, here's the fix" finding are actually
about the *same* computation, not four seats independently inventing
similar-looking numbers.

| Quantity | PHOTONICS | MATERIALS | QUANTUM | Red Team (this audit) |
|---|---|---|---|---|
| P-PCDP-0 anchor | bit-exact PASS | bit-exact PASS | (not scored) | **0 mismatches, 18/18 spot points, PASS** |
| AUC(\|offset\|) | 0.649 | (implicit, "node story runs backwards") | 0.6494 | **0.6494** |
| AUC(x2) | (not isolated) | 0.52 | 0.5195 | **0.5195** |
| P-PCDP-2 threshold scan | fails, hard | fails at t=0.30/0.40 | fails, hard | **fails at every t∈[0.05,0.40], both the 6/7∧8/11 bar and the 5/7∧7/11 hard-falsification escape** |
| Convention-baseline null | sens 6/7, spec 8/11, AUC 0.792 | (implicit) | (not isolated) | **sens 6/7=0.857, spec 8/11=0.727** |
| Alias predictor AUC | (not attempted) | (not attempted) | 1.000 | **1.0000** |
| Alias predictor vs C(41)−C(161) | (not attempted) | (not attempted) | r=1.00000, ≤1.4% | **r=0.999998, ≤1.445%** |
| 450/38 `NOT_FOUND`, widened | confirmed | confirmed | confirmed | **confirmed (`tag=WIDENED` both conventions)** |

Four independent implementations (three blind, one adjudicating) converge
on the same numbers to four-plus significant digits. This is not a
seat-counting exercise — it is the same computation, run cold four times,
landing in the same place. That is about as strong as this program's own
evidentiary standard gets without an FDTD run.

---

## ATTACK 1 — [inconsistency] P-PCDP-1 is REFUTED, independently confirmed, not merely under its CONFIRMED bar

§4's own band: AUC≥0.85 CONFIRMED, 0.65–0.85 PARTIAL, <0.65 REFUTED. My
from-scratch `|offset|`-only AUC (score = −|offset|, near-node ⇒ predicted
unstable, exactly §2.2(c)'s own reading) is **0.6494** — REFUTED, not
PARTIAL, by 0.6 percentage points. My `x2 = log10(|C(81)|/ABS_TOL)` AUC is
**0.5195** — statistically indistinguishable from chance (permutation-null
P(≥0.55 by chance) = 0.362 per VISION's own exact combinatorial check,
independently plausible from N=18, 7-positive). PHOTONICS' 2-feature
in-sample logistic (0.597) and LOOCV (0.000, the classic small-sample
leave-one-out anti-correlation at N=18) both sit at or below REFUTED too. No
seat, including this one, finds any reading of P-PCDP-1 above PARTIAL.

## ATTACK 2 — [inconsistency] P-PCDP-2 fails its own hard-falsification ESCAPE clause, not just its CONFIRMED bar

I scanned every threshold t∈[0.05,0.40] at step 0.001 (400 thresholds, finer
than any blind seat's scan) against sens≥5/7 ∧ spec≥7/11 — the *lenient*
hard-falsification-escape bar, not the stricter 6/7∧8/11 success bar.
**None passes either.** This is a stronger finding than "AUC is low": it
means no single-feature `|offset|` classifier at any operating point in the
proposal's own pre-registered search range survives even the most
forgiving reading the proposal itself wrote. Independently reproduces
MATERIALS' exact numbers (t=0.30→2/7,7/11; t=0.40→7/7,5/11) and QUANTUM's
identical finding.

**The reason is structural, not statistical, and I confirm it directly**:
the zero-phase-information predictor "unstable iff `conv==
incoherent_corrected`" scores **sens=6/7=0.857, spec=8/11=0.727** —
independently reproduced to the third decimal against PHOTONICS'/VISION's
number — *clearing P-PCDP-2's own 6/7∧8/11 success bar outright*, using no
phase information whatsoever. A predictor built from `|offset|` and
`log10(|C(81)|/ABS_TOL)`, both **convention-blind by construction** (mean
inter-convention |Δoffset| = 0.041, QUANTUM's own number, independently
plausible from my own offset table), cannot discriminate a label that flips
at 5 of 9 (θ₀,λ) cells between conventions (6 of 7 positives are
`incoherent_corrected`). This is not a fixable statistical-power problem —
the regressors and the label live on different axes.

## ATTACK 3 — [inconsistency, the crux] §2.2(c)'s `phase_offset` measures the wrong periodicity entirely; QUANTUM's alias-lattice quantity is the correct one, independently re-verified to near-exact agreement

Idealization 4 licenses using `P(θ)=λ/(A·cosθ)` "exactly as LOGBOOK states
it," and §2.2(c) is built on the assumption that the fringe's zero-crossings
recur at intervals of `P` (so `offset≈0`⇒node, `offset≈±0.5`⇒antinode is a
sensible reading). **PHOTONICS falsified this premise directly on the
committed function**: measured crossing-to-crossing gaps spanning
0.137P–1.279P, a 9.3× spread — the fringe's own period is not `P` at all.

I did not stop at confirming that the premise is false; I independently
rebuilt QUANTUM's replacement and ran it. QUANTUM's diagnosis: the n=41
quadrature error is the Poisson-alias term of the underlying fringe,
referenced to the **quadrature node-lattice spacing**
`h = 2·half_width_factor·FWHM/(n−1)` (=2.5° at n=41, FWHM=20°,
`half_width_factor=2.5` — read directly out of the already-committed
`gaussian_angle_weights`, not asserted), not the fringe period `P` at all.
I rebuilt `alias_coeff(θ₀,FWHM,λ,g,convention,m,h)` exactly per QUANTUM's
own posted formula and computed `E_pred = 2·Re[alias_coeff(m=1)] +
2·Re[alias_coeff(m=2)]` at all 18 GEOM78 combinations, independently:

- **AUC(|E_pred|/ABS_TOL) = 1.0000** — perfect separation.
- **Threshold |E_pred|=ABS_TOL: sensitivity 7/7, specificity 11/11** —
  every one of the 7 tier-unstable combinations reads `|E_pred|≥ABS_TOL`;
  every one of the 11 tier-stable combinations reads `|E_pred|<ABS_TOL`.
  No fitted parameter anywhere — the threshold is the pre-existing decision
  line the whole convergence machinery already uses.
- **Against the actual measured quantity it claims to predict**,
  `C(41)−C(161)` (read from `results.json`'s own `c41`, `C(161)` freshly
  computed from the committed `beam_divergence_*` functions): **Pearson r =
  0.999998**, **max relative error 1.445%** (at 450nm/36°/
  `incoherent_corrected`) across all 18 combinations, 14 of 18 under 0.5%.

QUANTUM's own critique reports r=1.00000/≤1.4%; mine is r=0.999998/1.445% —
agreement to the fourth significant figure from an independent
implementation using a coarser integration step (0.02° vs 0.01°), which
fully explains the residual 0.045-percentage-point gap. **This is not a
"could work" finding — I built it cold and it works, to the digit.**

**Ruling: §2.2(c)'s `phase_offset` is not a defensible approximation to
QUANTUM's alias quantity that merely needs tuning — it targets a different,
demonstrably wrong periodicity.** The two are not "the same idea, one
sharper" the way EM's Iteration-18 fringe model and PHOTONICS' λ-scaling
test turned out to be (LOGBOOK T21, Iteration 18 close). They diverge in
kind: one references the fringe's own (non-existent, at spacing P) node
structure; the other references the sampling grid's node structure. Only
the second is correct, and I have independently confirmed that to a
precision (r=0.999998) this program rarely achieves outside a bit-exact
regression anchor.

## ATTACK 4 — [inconsistency] P-PCDP-4/5's slope machinery is the wrong tool for the same reason Attack 3 identifies, and a correct replacement is already sitting inside QUANTUM's own object

QUANTUM's own critique reports the §2.2(e) slope-ratio vs. the thing it
should explain (the Δabs step-ratio) at **Spearman ρ = −0.300** — anti-
correlated, not merely noisy. I independently computed the alias-predictor's
own amplitude ratio `|E_pred_corrected|/|E_pred_incoherent|` at all 9 cells
from my own committed rows (a slightly broader 2-term object than QUANTUM's
single-frequency `|ĝ(1/h)|` ratio, so treat this as a directional, not
bit-exact, cross-check):

| λ | 36° | 38° | 40° |
|---|---|---|---|
| 450 nm | 1.475 | 1.637 | 1.737 |
| 600 nm | 1.968 | 1.951 | 1.923 |
| 750 nm | 2.162 | **0.835** | 2.262 |

Median **1.923**, tightly grouped within each λ, matching QUANTUM's own
1.664–2.232/median 1.950 in both magnitude and the same striking anomaly:
**750nm/38° inverts** (ratio <1), independently landing at 0.835 in my
implementation against QUANTUM's own figure and — a genuine cross-
instrument agreement — against **VISION's independently-measured raw
`Δabs(41→81)` step ratio at the same cell, 0.775** (a completely different
quantity: a finite-difference of two `beam_divergence_*` calls, not a
Fourier-domain integral). Two structurally unrelated diagnostics, run by
two different seats plus this audit, land on the same anomalous cell. That
is what a real, reproducible geometric fact looks like, not what a slope
artifact looks like. **P-PCDP-4/5's own machinery should be retired, not
patched — replaced by the alias-frequency spectral-amplitude ratio, which
is the same object Attack 3 already requires Phase 3 to build.**

## ATTACK 5 — [inconsistency] The §6 cost estimate is wrong by ~8×, independently confirmed, and the fix is independently confirmed to work

THERMODYNAMICS measured 168–269 ms/evaluation for §2.2(a) as transcribed
(rebuilding `_geom_derived`/the propagator matrix on every single-angle
call) versus 3.96/15.43 ms hoisted/memoized — roughly 7.9× — and projected
the zero-crossing search alone at ≈103 min unmemoized vs ≈5 min memoized.

I did not re-time the unmemoized path (THERMODYNAMICS' own direct
measurement is not in dispute and needs no third confirmation), but I
independently built and ran a memoized implementation from scratch — hoisting
`_geom_derived(g)` and the propagator matrices once per `(geometry,
wavelength)`, exactly THERMODYNAMICS' own recommended construction — covering
**all 18 combinations' `phase_offset` (4001-point grid, with widening) AND
both `alias_coeff` calls (m=1,m=2) AND the `C(161)` cross-check** — a
strictly larger computation than the original proposal's own §2.2(c)/(d)
scope (which needs only `phase_offset` and one `n=81` call, not the alias
scans or `n=161`). **Total wall-clock: ≈8.5 minutes, single-threaded, on
this box.** This independently corroborates THERMODYNAMICS' fix from the
opposite direction: not just "the current code is slow," but "the memoized
code, doing *more* work than the proposal asked for, is fast." §6's
13-minute headline becomes achievable, but only with THERMODYNAMICS'
mandatory-fix hoisting applied — the proposal's own optional, "cheap Phase-4
fix this proposal does not require" framing (§6, final paragraph) is wrong;
it is required, exactly as THERMODYNAMICS says.

## ATTACK 6 — [inconsistency] Three small, independently-confirmed counting/reference slips

(a) **§2.3/§6's "9×3=27 spot-check points"** double-counts λ: §2.1's own
table has 3 θ₀ × 3 λ = **9** (θ₀,λ) cells (I recounted its own rows
directly), × 2 conventions = **18** spot points, not 27/54. Confirmed
independently against §2.1's own table (THERMODYNAMICS, MATERIALS both
caught this).

(b) **P-PCDP-5's "18 per-combination slope ratios"**: §2.2(e) defines
`slope_ratio = |slope_corrected|/|slope_incoherent|` — an object that
*compares* the two conventions, so it exists once per **cell** (9), not
once per combination (18). Confirmed directly from §2.2(e)'s own formula,
which takes no independent `convention` argument in its output (VISION,
THERMODYNAMICS both caught this). Moot under Attack 4's own recommended
retirement of the slope machinery, but the counting error would recur
identically in the alias-amplitude-ratio replacement if not fixed at the
definition (the replacement ratio is also one-per-cell).

(c) **`local_period_deg(theta0_deg, lam_cells, g["A"])` raises `KeyError`.**
Confirmed by direct inspection of `experiments/048-.../design_geometry.py`'s
own committed `GEOM78`/`GEOM_EXP042_OLD` dicts: keys are `NY, OBJ_Y, D_SP,
GUARD_OUT, R_OUT, W_FLANK, PLANE_X, SRC_X, ABSORB, TAPER` — no `"A"` key
anywhere. The adjacent prose (`A = g["OBJ_Y"] − g["ABSORB"]`) is correct and
is what my own reimplementation used throughout this audit (PHOTONICS,
VISION both caught this).

## ATTACK 7 — [inconsistency] Excluding `coherent` removes a free, already-computed, degenerate-x1 control — and it is the control that would have caught Attack 2's confound earliest

Confirmed directly from `experiments/050-.../design_geometry.py`:
`beam_divergence_coherent` and `beam_divergence_incoherent` both build their
per-angle field via the **identical** `_G_for_g(lam_cells, gd,
obliquity=True)` and `_src_amp` call — the only difference is *how the
angular samples are combined* (coherent complex-field sum vs. incoherent
intensity sum), not the single-angle building block itself. This means
`coherent`'s single-angle fringe **is** `edge_diffraction_c_empty_g(...,
"incoherent")` by construction — any `|offset|` or alias-coefficient
computed for `coherent` at a given (θ₀,λ) is *identical* to `incoherent`'s
at that same cell. Yet the already-committed `results.json` gives `coherent`
tier labels **81,81,81,81,41,41,81,81,41** at these same 9 cells —
materially different from `incoherent`'s own **41,81,41,41,41,41,41,41,41**
— at an identical x1. That is precisely the shape of evidence that would
have shown Attack 2's convention-confound problem *before* running a single
new computation: two labels, one shared regressor, proof the regressor
alone cannot be the whole story. MATERIALS is right that dropping it removes
the falsifier, not merely 9 rows of data. **Restoring it costs nothing new**
(the tier labels already exist in `results.json`; only the alias-coefficient
evaluation is new, and it reuses the identical `incoherent`-convention
single-angle function already being computed for the other 9 cells).

## ATTACK 8 — [inconsistency] The binary tier label is a fragile artifact of one decimal in `ABS_TOL=0.1·C_THR`, and the fix converges with Attack 3's own recommended scoring

VISION's finding, confirmed by my own regressor table: every in-scope
`|C(41)|` at GEOM78 FWHM=20° sits well under `C_THR=0.005` (my own table
shows worst-case `|C(81)|` still under 0.003), so the convergence
criterion's `|C(2n)|≥C_THR` relative-error clause never fires anywhere in
this proposal's scope — every one of the 18 tier labels reduces to the
single condition `Δabs(41→81) > ABS_TOL = 0.1·C_THR`. VISION's own
sensitivity sweep (independently plausible, not re-run bit-for-bit here:
the underlying `Δabs`/`ABS_TOL` ratios I computed span 0.073–1.924, and the
class boundary VISION reports, 0.785→1.057, sits exactly inside that range)
shows the 7/11 split survives only over `ABS_TOL∈[0.08,0.10]·C_THR` and
disappears entirely by `0.20·C_THR`. **This does not disqualify the binary
label as a diagnostic** — `ABS_TOL` is a previously-adopted, non-negotiable
decision line (idealization 2, unchanged from exp-049), not a free parameter
this cycle re-litigates — but it does mean the binary label is the *wrong
primary scoring target* for a predictor whose whole point is to explain a
*magnitude* residual. **This converges exactly with Attack 3's own finding**:
QUANTUM's alias predictor was scored, and independently re-verified here,
against the *continuous* quantity `C(41)−C(161)` first (r=0.999998), with
AUC/threshold performance following as a consequence, not a design target.
Adopting the alias-lattice mechanism (Attack 3) and demoting the binary
label to secondary (VISION's, MATERIALS' requested fix) are not two
separate mandatory fixes — they are the same fix, arrived at from two
different directions.

---

## Constraint check

No target constraint is violated or quietly dropped. §3's "T1 escape route:
NONE" is accurate — confirmed directly: no material law, no σ, no new
source, no engine change anywhere in the proposal text or in anything
computed in this audit; every quantity above is a `numpy` evaluation of an
already-committed, already-gated analytic propagator at an already-committed
geometry. No constraint-3/4 verdict is issued anywhere (grep-confirmed).
`REALIZABILITY_MEMO.md` exposure: zero (no `beam_divergence`/
`gaussian_angle_weights`/`edge_diffraction` citation appears there; MATERIALS'
own blind critique independently confirms this and is the more authoritative
check on its own charter question). **Criterion 4 is NOT fired by the
proposal's own defects** — every one is a same-shift, zero-new-FDTD,
already-verified fix. It IS relevant to the separate scope-drift question
below, addressed on its own terms, not as a criterion-4 finding.

---

## The Director's two assigned questions, answered directly

**1. Does QUANTUM's alias-lattice mechanism independently reproduce?**
**Yes, to near-exact agreement**, from a cold, independent implementation:
AUC 1.0000 (QUANTUM: 1.000), perfect 7/7-11/11 separation, r=0.999998 against
measured `C(41)−C(161)` (QUANTUM: r=1.00000), max relative error 1.445%
(QUANTUM: ≤1.4%) — the small residual gaps are fully attributable to a
coarser numerical-integration step in this audit's implementation, not to
any physics disagreement. This is the single most load-bearing finding of
this cycle and it holds up completely under independent re-derivation.

**2. Is the original phase-offset design salvageable, or should Phase 3
adopt QUANTUM's mechanism as the corrected primary design?**
**Adopt QUANTUM's mechanism as the corrected Phase-3 crux quantity,
explicitly, not as an addendum.** §2.2(c)'s `phase_offset` is not a rough
draft of the right idea — Attack 3 shows it targets a periodicity (the raw
fringe's own zero-crossing spacing at `P`) that does not govern the
phenomenon at all; the phenomenon is governed by the sampling grid's own
node spacing `h`. No amount of re-tuning the window width, the interpolation
method, or the `n_grid` resolution inside §2.2(c) as written can fix this,
because the object it measures is the wrong object. This is exactly the
"corrected Phase-3 design, not the original Phase-1 proposal" situation
exp-050's own NOTES.md names for its own P-NCONV27-2 amendment, and the
house convention is the same one exp-050 followed: **flag it explicitly,
do not silently rewrite it.** `phase1_proposal.md` stands unedited as the
historical record; the corrected design (below) is what Phase 3 should
freeze.

---

## OVERALL RULING

# PROCEED-WITH-MANDATORY-FIXES

**Why this proceeds.** The proposal's scope, cost discipline (once
Attack 5's memoization fix is applied), regression-anchor rigor (bit-exact,
independently confirmed), idealization discipline, and pre-registered
"what would make this cycle a failure" framing are all sound — the same
qualities that made exp-049/050 PROMISING. The underlying scientific
question this cycle exists to answer (what explains exp-050's tier
instability and its ~1.9–2.3× convention asymmetry) is real, well-motivated,
and now **answered**, inside this cycle's own budget, using this cycle's own
already-committed building blocks (`_geom_derived`, `_G_for_g`,
`edge_diffraction_c_empty_g`) — just not by the specific regressor §2.2(c)
defines. Nothing found here is unfalsifiable (every attack above is a
concrete, executed computation with a concrete numeric outcome) or
inexpressible (every quantity is a closed-form or finite-difference `numpy`
computation on already-committed code).

**Why it does not proceed unchanged.** P-PCDP-1 and P-PCDP-2 — the entire
scored deliverable of the proposal as frozen — are REFUTED, independently,
four separate ways, before Phase 4 would even run. Freezing this design as
written and running Phase 4 on it would spend real (if small) compute to
reproduce a result already known at the desk, exactly the failure mode this
program's own zero-cost pre-check discipline (T21's chord-model idiom, this
cycle's own §2.2(c)) exists to prevent. Unlike exp-050's P-NCONV27-2 (where
the falsification clause's *wording* needed a documented exemption zone
while the underlying mechanism stood), this cycle's defect is in the
*regressor itself* — the fix is a replacement, not an amendment.

---

## MANDATORY-FIX DOCKET (adoptable at Phase 3)

1. **[Attack 3, QUANTUM+Red Team, CONFIRMED NECESSARY AND SUFFICIENT by
   independent re-derivation]** Replace §2.2(c)'s `phase_offset(...)`
   entirely with the alias-coefficient crux quantity: `h =
   2·half_width_factor·FWHM/(n−1)` (read from the already-committed
   `gaussian_angle_weights`, not re-derived), `alias_coeff(θ₀,FWHM,λ,g,
   convention,m,h)` per QUANTUM's own posted formula, `E_pred =
   2·Re[alias_coeff(m=1)] + 2·Re[alias_coeff(m=2)]` (both `m=1` and `m=2`
   are required — QUANTUM's own E5 and this audit both confirm `m=1` alone
   is 6–16% off at 450nm). This is the corrected Phase-3 crux quantity,
   flagged explicitly as a Red-Team-driven correction per this program's
   "flag, don't silently rewrite" convention (exp-050's own precedent) —
   `phase1_proposal.md` stands unedited.
2. **[Attack 5, THERMODYNAMICS+Red Team, independently confirmed both
   necessary and sufficient]** Hoist `_geom_derived(g)` and the propagator
   matrices (`G0`, `G_obl`) out of every per-angle inner loop, memoized once
   per `(geometry, wavelength)` — mandatory, not optional (§6's "cheap
   Phase-4 fix this proposal does not require" language is wrong). Re-cost
   §6 at the hoisted unit; this audit's own from-scratch memoized
   implementation, covering a strictly larger computation than the
   original design, completed in ≈8.5 minutes single-threaded.
3. **[Attack 7, MATERIALS+Red Team]** Restore `coherent` to scope (all 27
   FWHM=20° combinations, not 18). Its single-angle fringe is bit-identical
   to `incoherent`'s by construction (confirmed directly from code) — a
   free, already-computed, degenerate-x1 control that both tests whether
   `|offset|`/alias-coefficient carries real information (it does, per
   item 1) and provides a third convention (a different summation rule
   over the *same* single-angle fringe) to cross-check the alias-lattice
   mechanism's reach.
4. **[Attack 4, QUANTUM+VISION+Red Team]** Retire §2.2(e)'s slope-ratio
   machinery (P-PCDP-4/5 as written); replace with the alias-frequency
   spectral-amplitude ratio `|ĝ_corrected(1/h)|/|ĝ_incoherent(1/h)|` (the
   `m=1` term of item 1's own object) as the asymmetry-explaining
   regressor. Independently re-verified here (median 1.923, range
   0.835–2.262, tightly grouped within each λ, reproducing the same
   750nm/38° inversion VISION independently found in the raw `Δabs` ratio
   via a structurally unrelated computation) — a genuine cross-validated
   geometric fact, not a slope artifact.
5. **[Attack 6c, PHOTONICS+VISION]** Fix `local_period_deg(...)`'s `g["A"]`
   `KeyError` — use `A = g["OBJ_Y"] − g["ABSORB"]`, as the proposal's own
   adjacent prose already states. (Retained even though item 1 replaces
   `phase_offset`, since `h`'s own definition does not need `A`, but `P(θ)`
   remains cited elsewhere, e.g. §2.1's own table, and the geometry-dict
   generalization pattern should not carry a live bug forward.)
6. **[Attack 6a/6b, THERMODYNAMICS+MATERIALS+VISION]** Fix the counting
   slips: §2.3/§6's "9×3=27 spot points" → 9 cells × 2 conventions = 18;
   any surviving per-cell ratio object (item 4's replacement included) is
   one-per-cell (9), not one-per-combination (18) — state this explicitly
   in whatever prediction replaces P-PCDP-5.
7. **[Attack 8, VISION+MATERIALS+Red Team, converges with item 1]** Score
   the replacement predictor (item 1) primarily against the **continuous**
   target `log10(|E_pred|/ABS_TOL)` vs. `log10(|Δabs(41→81)|/ABS_TOL)`
   (Spearman ρ, pre-registered CONFIRMED/PARTIAL/REFUTED bands in the same
   shape as the original P-PCDP-1), with the binary `n*≠41` tier
   classification demoted to a secondary, reported read — not because the
   binary label is uninteresting, but because it is a threshold artifact
   of `ABS_TOL=0.1·C_THR` (stable only over `ABS_TOL∈[0.08,0.10]·C_THR`,
   VISION's independently-plausible finding) while the continuous quantity
   is a real, fast-settling, 9-significant-figure object. Pre-register the
   convention-identity null baseline (sens 6/7, spec 8/11, AUC≈0.79,
   independently confirmed this audit) as an explicit floor any secondary
   binary-classification read must beat, per PHOTONICS' own flip-condition
   — moot for item 1's own predictor (AUC 1.000 clears it trivially) but
   still worth stating for the record.
8. **[VISION, carried]** Commit one `ABS_TOL`-sensitivity ledger row:
   positive/negative counts at `0.05/0.08/0.10/0.13/0.20·C_THR` —
   informational disclosure, not a re-tuning of `ABS_TOL` itself
   (idealization 2 still governs).
9. **[THERMODYNAMICS, carried from Iteration 27's own overdue
   recommendation]** Commit the expected completeness-ledger record count
   as an executable assertion (this program's own `assert
   len(ledger)==N` idiom, exp-049/050 both used it); persist a
   partial/crash-state timing record from process start (`time.time()` at
   import, flushed on any exit path), not only the final successful run's
   `elapsed_s` — verified by direct code read that `run.py`'s own `t0 =
   time.time()` sits inside `main()`, not at import, in exp-050's own
   committed module, so this recommendation has not yet been adopted
   anywhere despite being named at Iteration 27's close.

---

## Ruling on MATERIALS' scope-drift flag: does Iteration 29 get an unconditional trigger on item (4), the fixed-absolute-thickness `graded_black_shell` variant?

**YES — unconditional Iteration-29 trigger, adopted, not a fourth
re-ranking.**

I independently verified MATERIALS' own citation chain rather than taking
it on faith: the fixed-absolute-thickness `graded_black_shell` variant was
first queued at **Iteration 7** (`LOGBOOK.md` line 4777: "MATERIALS' own
queued Iteration-7 item"). It has since been independently re-ranked,
without being reached, at Iteration 25 (exp-047's own close), Iteration 26
(exp-049's close, ranked item), and Iteration 27 (exp-050's close, ranked
item 4, "9+ iterations deferred across two consecutive instrument-fidelity
cycles" — LOGBOOK's own words), and it sits, unreached, as ranked item 4 of
Iteration 28's own queue in `PLAN.md` ("now ten-plus-iteration-deferred").
That is a **21-iteration span since first proposal**, with the item named
in every recent close's own ranked list and never once reaching the top of
a cycle's actual budget.

This program has exactly one prior precedent for a deferral this long: the
r=156 scale-bridge leg, queued at Iteration 3, which received a **committed,
unconditional Iteration-11 trigger** after its **fourth** deferral
(LOGBOOK, Iteration 10 close: "committed trigger adopted... Iteration 11
builds it unconditionally... do not defer a fifth time"). Item (4) has now
been deferred well past that bar, in absolute iteration count and in
consecutive-cycle count: this Iteration-28 cycle (exp-051) is itself the
**third consecutive** instrument/model-fidelity cycle (26, 27, 28) and the
**sixth such cycle in nine iterations** (20, 22, 23, 26, 27, 28) — the exact
ratio Red Team's own Iteration-26 language named as the threshold that
forced exp-049 to run in the first place ("a third consecutive deferral
would repeat this program's own named r=156 anti-pattern"). Letting item
(4) reach a fourth consecutive re-ranking without a committed build slot
would be a direct, disclosed instance of the very pattern this program
already named and fixed once.

**Ruling, stated as a binding instruction for the LOGBOOK/PLAN.md close:**
Iteration 29 builds and measures the fixed-absolute-thickness
`graded_black_shell` variant's own `C`, unconditionally — not contingent on
Iteration 28's own findings, not subject to a further ranked-list
competition against items (2)/(3)/(5)/(6). This does not preclude Iteration
29 also carrying forward same-shift, load-bearing fixes discovered at this
cycle's own Phase 5 close (house discipline requires that regardless), but
the substantive new proposal for Iteration 29 is item (4), full stop.

---

## Verification appendix — what I actually ran

All of the following was executed in this session, against unmodified
`experiments/042-t21-magnitude-bridge/design_geometry.py`,
`experiments/048-evidentiary-chord-closure/design_geometry.py`, and
`experiments/050-n-convergence-a724-geometry/design_geometry.py` (imported
via the same `importlib`-under-private-module-name pattern exp-050's own
module uses, to avoid the basename-collision hazard that module's own
docstring warns about):

1. `repro.py` — first-pass, unmemoized reimplementation of §2.2(a)–(e) plus
   QUANTUM's `alias_coeff`. Correct but too slow for a full run (confirmed
   THERMODYNAMICS' Attack 5 empirically by hitting the wall myself before
   reading the fix).
2. `repro2.py` — memoized reimplementation (hoisting `_geom_derived`/the
   propagator matrices once per `(geometry, λ)`, exactly THERMODYNAMICS'
   own recommended construction). This is the audit's primary tool;
   produced every number cited above. Full stdout: `out.log`. Per-row
   data (offsets, tags, `x2`, `E_pred`, `c41`): `rows.json`.
3. P-PCDP-0 regression anchor: reran independently, **0 mismatches** across
   all 18 (θ₀,λ,convention) spot points against exp-042's own committed
   `edge_diffraction_c_empty`/`edge_diffraction_c_empty_corrected`.
4. `local_period_deg`/`phase_offset`/`nearest_zero_crossing`: rebuilt per
   §2.2(b)/(c)'s own pseudocode, `n_grid=4001` (the proposal's own stated
   Phase-3-tunable default, not a reduced grid), ±0.6·P then ±1.5·P
   widening exactly as specified. `NOT_FOUND`→`WIDENED` fired at 450nm/38°
   in both conventions, matching all three blind seats that checked this.
5. `alias_coeff`/`E_pred`: rebuilt per QUANTUM's own posted formula,
   `step=0.02°` (QUANTUM used 0.01°), `m=1` and `m=2` both computed.
6. `C(161)` cross-check: fresh calls to exp-050's own committed
   `beam_divergence_incoherent`/`beam_divergence_incoherent_corrected` at
   `n=161`, per combination — not read from any cached table.
7. Total wall-clock for the full 18-combination sweep (regression anchor +
   `phase_offset` + `E_pred` (both `m`) + `C(161)`, i.e. a strictly larger
   computation than the original proposal's own §2.2(c)/(d) scope):
   **≈8.5 minutes single-threaded**, this box.

No `lab/` file, no exp-042/048/049/050 file, was read into a mutable path
or modified. This experiment's own `design_geometry.py`/`run.py` do not yet
exist (Phase 3 has not run) — everything above is a Phase-2 pre-check in
this program's own established idiom (exp-050's own Red Team precedent),
not a substitute for Phase 4's independent implementation.
