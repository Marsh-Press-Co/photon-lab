# PHASE 5 — REVIEW (QUANTUM OPTICS, fresh context, blind) — exp-106

*Charter: non-classical absorption, state-dependent or coherent
interactions. Expressibility contract: mechanisms enter the bench only as
effective classical parameters — σ(I), σ(x,t), dispersive ε(ω), gain — or
Red Team strikes them. This seat led Phase 1 this cycle (Iteration 83
rotation) — its own original design is reviewed with the same rigor as
anyone else's, not defended. Every number below is independently
recomputed from `results.json`'s raw fields via a standalone script, not
read from `NOTES.md`'s prose, then cross-checked against `run.py`'s own
formulas.*

## 0. Independent numeric verification

Recomputed directly from `results.json` (script re-derivation, not
prose-reading):

```
kappa_windows_selfsim  : r78=0.018336958179764707  r156=0.0008866623871477821  r312=4.79303718569495e-06
kappa_windows_fixedabs : r78=0.018336958179764707  r156=0.0009621833317956940  r312=9.00926735843857e-06

shape_ratio          (selfsim)  = (k78-k156)/(k156-k312) = 19.787847024468125   -- matches results.json p3_selfsim.shape_ratio exactly
shape_ratio_fixedabs (fixedabs) = (k78-k156)/(k156-k312) = 18.228333623646076   -- matches results.json item4_fixedabs.shape_ratio exactly

model_A_miss (selfsim)  = 0.8554612460207963  (85.55%) -- outside 25% band
model_B_miss (selfsim)  = 0.7592763345085640  (75.93%) -- outside 60% band
model_A_miss (fixedabs) = 0.8435655776411324  (84.36%) -- outside 25% band
model_B_miss (fixedabs) = 0.7396035076955177  (73.96%) -- outside 60% band

noise_floor_flag(selfsim):  denom = k156-k312 = 8.818693499620872e-04
                             noise_floor = 3*0.10*|k156| = 2.659987161443347e-04
                             noise_dominated = (8.819e-4 < 2.660e-4) = False   -- matches
noise_floor_flag(fixedabs): denom = 9.531740644372554e-04
                             noise_floor = 2.886549995387083e-04
                             noise_dominated = False                          -- matches

abs_ratio: r156 = k_fixedabs(156)/k_selfsim(156) = 1.0851744088196273
           r312 = k_fixedabs(312)/k_selfsim(312) = 1.8796573048352636         -- both matches results.json.abs_ratio exactly

p_abs_frac_diff: r156 = 0.12305795332466973 (12.3%)   r312 = 0.17962207739772926 (18.0%) -- both exceed the informal 10% figure

n_fdtd_calls = 10 (of 12 scheduled); total_wall_s = 18398.414408683777 = 306.64 min = 5.11h
```

**Every headline figure reproduces exactly, digit-for-digit, from
`results.json`'s own primitives** — Gate P0 (`pass_=True`), the r=156/312
reproduction checks against exp-105's own committed `kappa_window` values
(`rel_dev=0.0` at both), `shape_ratio=19.787847…` and
`shape_ratio_fixedabs=18.228334…`, the floor-gate (`frac_unresolved=0.0`
at both r, `n=4000`), the settling leg at r=156 (`rel_change=1.85e-4`
selfsim / `1.15e-4` fixedabs, both PASS), `p3_trusted=False` and
`shape_ratio_fixedabs_trusted=False` (both forced by
`nyquist_margin(312)=1.233974…`, MARGINAL-REDUCED-CONFIDENCE), the ledger
`core_frac=0.0` at every (r, family), `box_dev` two orders of magnitude
inside the established ≤0.12 bound at every cell, and `abs_ratio` at both
r. **No reproduction failure anywhere.** This is a clean pipeline result
on the arithmetic — the substantive findings below concern what the
pipeline *does* and *does not* do with these correctly-computed numbers.

## 1. T1 scope check and this seat's own Phase-1 design under fresh scrutiny

**T1 is correctly N/A, confirmed from primitives, not merely asserted.**
Direct read of `run.py::_run()` (lines 203–213): every article-scene call
is `materials.pec_disk(sim, CX, CY, R_CORE)` followed by
`materials.graded_black_shell(sim, CX, CY, R_CORE, R_COAT, sigma_max=...)`
— both static, real-valued, position-only `σ(x)` assignments with no
intensity, time, or field-state argument anywhere in either family's own
geometry function (`geom()`/`geom_fixedabs()`). `sigma_max` is a fixed
python float baked in before `Sim.run()` is called; nothing in this file's
2,240-line-domain, 25,600-step-longest-run execution path threads a field
value back into a material coefficient. Every quantity this cycle scores
(`kappa_window`, the settling ratio, the ledger's `sigma_abs/sigma_ext`,
`core_frac`) is a ratio or fraction of ordinary classical Poynting/`|Ez|²`
quantities from a deterministic linear solve. There is no σ(I), σ(x,t),
dispersive ε(ω), or gain anywhere in this cycle's pipeline — this seat's
own expressibility contract is satisfied vacuously, exactly as both
`phase1_proposal.md` and `NOTES.md` state, and exactly as the identical
finding held for exp-102/103/104/105 before it.

**Does this seat's own original Phase-1 design survive Red Team's/the
Director's corrections intact in substance?** Mostly yes on scope and
bands; **no** on two specific points worth flagging plainly now that the
real numbers are in, per this task's own instruction not to defend the
original draft:

- **My own §5 (Idealizations) realizability sentence was itself
  factually backwards**, independent of MATERIALS' own (also-wrong,
  Red-Team-overridden) Phase-2 critique. I wrote: "the fixed-abs family's
  own constant 2.4λ absolute thickness is, if anything, closer to the
  µm-scale real-CNT-black range... since the coating is fixed absolute
  size." Red Team's Attack 6 caught this directly: self-similar's
  *absolute* thickness *grows* with r (48→96→192 cells = 1.44→2.88→5.76µm
  at r=78/156/312, computed from my own table), so self-similar's gap to
  the real 100–500µm range *shrinks* with r (17.4× at r=312) while
  fixed-abs holds a *constant* 69.4× gap at every r — the opposite
  direction from what I wrote. This was a real, independently-derivable
  arithmetic error in my own proposal, not a restated stale claim like
  MATERIALS' — I should not have needed Red Team to catch it from my own
  table's own numbers.
- **The entire absorbed-power ledger (mandatory fix 1 — `ledger_check()`,
  `sections.widths()`/`radial_absorbed_power()`, the `p_abs_frac_diff`
  cross-family check) was not part of my own design at all.** My own §2c
  proposed only the `window_stats()` floor-gate; the ledger machinery
  that turned out to be this cycle's single most consequential
  addition (see §2 below) originated entirely from EM's and
  THERMODYNAMICS' independently-converging Phase-2 critiques and Red
  Team's own Attacks 4/8/9 — I had not considered that the fixed-abs
  family's `R_CORE/R_COAT` ratio (0.692/0.846) would exceed T9's
  only-validated 0.385 anchor, a real gap in my own original due
  diligence on the control I was proposing.
- By contrast, the four Tier-1 items' own scope, the pre-registered
  `shape_ratio_fixedabs` CONFIRM/REFUTE/AMBIGUOUS bands (8.0/14.8), the
  `abs_ratio` factor-of-2 band (adopted from PHOTONICS but consistent
  with my own §4 framing), the cost-gating discipline (§2e), and the
  `p3_trusted`/`shape_ratio_fixedabs_trusted` *concept* (my own §4 named
  this exact structural prediction before Red Team formalized it as
  mandatory fix 3) all survived intact in substance — the corrections
  were real but concentrated in realizability prose and one missing
  control, not in the cycle's own falsifiable machinery.

## 2. Gaps, inconsistencies, and unstated risks

### 2a. [Headline finding] Mandatory fix 1's own reclassification rule was written, adopted, and never implemented — the >10% trigger it names fired at both r, and item 4's headline verdict does not reflect it

`phase2_redteam_audit.md` §3.1, mandatory fix 1, states explicitly
(THERMODYNAMICS' own offered threshold, formalized by Red Team as part of
the SAME numbered mandatory fix as the ledger check itself): *"if
fixed-abs and self-similar's `p_abs`/`sigma_ext` fractions land within
~10% of each other at matched r, treat item 4's two-hypothesis framing as
adequately clean; if they diverge materially, report `shape_ratio_
fixedabs`'s CONFIRM/REFUTE bands as **three-way ambiguous** (thickness-law
vs. core-reflection/gradient-steepness vs. both), not a clean binary."*
`NOTES.md`'s Phase 3 synthesis states "All 7 of Red Team's mandatory fixes
ADOPTED in full" with no override recorded against this clause.

The measured divergence is **12.3% at r=156 and 18.0% at r=312** — I
independently recomputed both from `ledger_r156`/`ledger_r312`'s raw
`sigma_abs` fields (§0, above) and they match `results.json`'s own
`p_abs_frac_diff` fields exactly. **Both exceed the ~10% trigger, at both
measured r.** Yet `run.py`'s actual classification logic (lines 754–764)
computes `classification` from `shape_ratio_fixedabs` alone — a
threshold check against `SHAPE_RATIO_FIXEDABS_CONFIRM`/`_REFUTE`, then a
`noise_flag` qualifier, then a `_trusted` qualifier — with **no reference
anywhere to `p_abs_frac_diff`**. The persisted headline reads
`"REFUTES-electrical-thickness-growth-hypothesis (NOT-TRUSTED — r=312
MARGINAL/unsettled)"` — the untrusted-r=312 caveat is present (mandatory
fix 3 was implemented correctly), but the three-way-ambiguous
reclassification mandatory fix 1 itself required, under exactly the
condition that occurred, is absent from both the classification string
and the frozen predictions text (`build_predictions_text()`'s own item-4
paragraph narrows the fix-1 language down to "checks... before
`shape_ratio_fixedabs` is trusted as a clean two-hypothesis
discriminator" — a vaguer sentence than Red Team's own explicit
reclassification instruction, and this dilution happened between the
Red Team audit and the frozen `NOTES.md`/`run.py`, i.e. at Phase 3, not
at Phase 2).

`NOTES.md`'s Result section *does* disclose the raw 12.3%/18.0% numbers
honestly, in a clearly-labeled, un-gated paragraph ("No pre-registered
pass/fail band was frozen for this specific quantity... reported here as
a genuine, disclosed, un-gated observation for Phase 5 to weigh... not
adjudicated here") — this is not a concealment. But it means the
machine-generated `classification` string embedded in `result_text` (the
one artifact any future citation of this cycle is most likely to quote
verbatim, matching this program's own repeated R4/R20 lesson that a
document's *headline* language is what propagates, not its footnotes) is
**more confident than the cycle's own adopted mandatory fix says it is
entitled to be**. This is a genuinely new instance of the R16/R21/R23
lineage's own general shape — a discipline explicitly promised at Phase 2
and formally "adopted in full" at Phase 3 eroded, undetected, before
Phase 4 ran — but in a new sub-form none of R16/R21/R23's own text covers
verbatim (those concern a *persisted-field* or a *disclaimer-string*
specifically; this concerns a *reclassification rule* attached to an
already-persisted comparison). Per this program's own founding-instance
precedent (R11/R15/R16/R17/R18/R19/R20/R21/R22/R23 all: a rule's own
founding/discovering cycle does not retroactively violate it), this does
**not** fire Checkpoint criterion 4 on its own — but it is exactly the
shape of finding that lineage exists to catch, and I recommend the
Director name it explicitly (a same-shift documentation fix re-labeling
item 4's own classification as "REFUTES, nominally — reportable per
mandatory fix 1 as THREE-WAY-AMBIGUOUS given `p_abs_frac_diff`>10% at
both measured r — NOT-TRUSTED at r=312" is a one-line, zero-cost fix,
matching this program's own established same-shift-correction
convention) before this headline propagates into a future LOGBOOK
citation as a clean REFUTE.

### 2b. Phase 1's own §2c design (persist the raw per-cell window arrays) was silently never implemented

`phase1_proposal.md` §2c specified, concretely: *"The persisted record
adds, per (r, family): `window_floor_gate` (...) **plus the full raveled
empty- and article-scene per-cell arrays themselves** (`window_block_
empty`, `window_block_article`) — so a future cycle can recompute or
re-derive any statistic without a fresh FDTD call."* `NOTES.md`'s own
frozen Idealizations section repeats the disclosed cost of this design
choice verbatim: *"Persisting the full per-cell window-box arrays (§2c)
modestly grows `results.json` (...≈128,000 floats, ≈1MB uncompressed)."*

`run.py::floor_gate_window()` (lines 282–290), as actually written, calls
`floor_gate()` and returns only its aggregate `{rms, floor, n_unresolved,
frac_unresolved}` dict — the raw per-cell block (`block_e`) is computed,
then discarded, never returned or persisted. Confirmed directly:
`results.json` contains no `window_block_empty`/`window_block_article`
key anywhere (full key listing checked), and the file is 34,671 bytes —
two orders of magnitude smaller than the ~1MB the proposal and NOTES.md
both disclosed as the cost of doing what §2c actually specified. This is
not merely undisclosed — it is *disclosed as having happened, twice, in
two frozen pre-run documents*, and did not happen. No Phase-2 critique or
Red Team audit caught this (none reviewed `run.py`, which did not exist
at Phase 2 — "*No `run.py` exists yet for exp-106 — this is a pre-freeze
audit of the Phase-1 design only*," `phase2_redteam_audit.md` line 7-8),
and `NOTES.md`'s own Result section, which does correctly report closing
the *other* half of item 1 (r=312's `wide_channel`/`point_channel`
persistence, verified present in `r312_selfsim` with 53 entries each),
never mentions that the window-block raw-array half of the same item was
dropped. Non-load-bearing to any scored verdict this cycle (the
`floor_gate()` summary statistics that *were* persisted are exactly what
Item 1's own falsifiable band needed), but it reproduces, in a new
location, the exact "discard the byproduct instead of persisting it"
failure shape this entire cycle exists to close on the `kappa_window`
channel specifically — worth a same-shift correction to `NOTES.md`'s
Result section stating plainly that this half of item 1's design was not
executed as specified, one way or the other (implement it, or retire the
design commitment explicitly), rather than leaving two frozen documents
asserting a persistence that `results.json`'s own byte count already
falsifies.

### 2c. EM's own Phase-2 "core-reflection-leakage" attack is not fully discharged by the ledger check that was actually run

EM's sharpest Phase-2 attack named a specific, concrete hazard: with
fixed-abs's `R_CORE/R_COAT` reaching 0.846 at r=312, "*a thinner coating
in front of a much larger hard PEC disk can raise specular/diffracted
core-reflection into the forward window independent of any
electrical-thickness or z/z_R effect... a `shape_ratio_fixedabs≤8.0`
reading could be core-reflection leakage, not reduced attenuation.*" Red
Team's own Attack 9 *independently* identified the precise limit of the
check that was ultimately implemented: `radial_absorbed_power`'s
`core_frac` measures absorbed power landing *inside* the PEC core, which
is "trivially ~0 regardless of whether the core is 'incidental' in the
T9 sense" because a PEC forces `Ez=0` there by construction — confirmed
in `results.json`, `core_frac=0.0` (exactly, to the printed precision) at
every one of the four new (r, family) cells, giving this check zero
discriminating power against EM's own named hazard. `widths()`'s
`sigma_abs/sigma_ext` (the ledger's other half, ~0.49–0.52 at every
cell, box-independent) is a genuine, useful *aggregate* energy check, but
it does not spatially resolve *where* the non-absorbed power goes — it
cannot distinguish "reflected power spread isotropically" from
"reflected power concentrated in the forward diffraction window `kappa_
window` itself measures." The one test that would directly answer EM's
question — exp-052's own literal hollow-vs-PEC-cored delta methodology —
is explicitly and honestly deferred to Tier 2 in `NOTES.md`'s
Idealizations ("*not a re-run of exp-052's own hollow-vs-PEC-cored delta
methodology... a real, new-FDTD-call cost, not executed this cycle*").
This is disclosed, not hidden, and Red Team's own Attack 9 named the
identical limitation before the run — but it means item 4's own
"REFUTES-electrical-thickness-growth-hypothesis" reading, even setting
the NOT-TRUSTED r=312 qualifier and §2a's own reclassification gap aside,
still carries a third, honestly-disclosed-but-unclosed hazard (core-
reflection leakage) that no instrument run this cycle actually rules out.

### 2d. A structural ceiling this cycle's own text names but Phase 5 should restate plainly: `p3_trusted` cannot become True at r=312 under this bridge geometry, regardless of the deferred settling leg's outcome

`p3_trusted = settling_pass_window_312 AND (nyquist_tier(312)=="TRUSTED")`.
`nyquist_margin(312)=385/312=1.233974…` is a fixed function of `D_EFF=77`
and `LAMBDA_CELLS=20` (both module constants, unchanged since exp-105),
independent of anything any future FDTD capture at r=312 can produce —
confirmed directly from `geom()`'s own formula (§0). This means even a
hypothetically clean settling PASS at r=312 (the leg that was cost-
deferred this cycle, per the pre-registered gate, honestly) would still
leave `p3_trusted=False`, because `nyquist_tier(312)` can never reach
`"TRUSTED"` (requires margin ≥2.0) under the current self-similar
r-family construction. My own Phase-1 proposal disclosed this explicitly
in advance ("*readers should not expect `p3_trusted=True` to be reachable
this cycle without either an improved-Nyquist-margin geometry... or a
deliberate, explicitly-justified loosening of the bar*"), and `NOTES.md`'s
Result section is honest that the settling leg "did NOT resolve this
shift" — but neither document states in one place the sharper fact that
*running* the deferred leg, even to a clean PASS, would not have changed
`p3_trusted`'s own value. Worth stating plainly for Iteration 84: the
r=312 settling leg remains diagnostically valuable (a FAIL there would
still be informative, revealing settling contamination beyond the
Nyquist concern) but is not, and never was, capable of resolving this
bridge family's own trust ceiling at r=312 — only a genuinely different
domain geometry can.

### 2e. Clean passes worth naming explicitly (not gaps — positive controls this cycle got right)

- Gate P0 and both reproduction checks reproduce exp-105's own committed
  `geom()`/`kappa_window` values to `0.000e+00` relative deviation — a
  textbook R6-style ground-truth-recovery gate, correctly implemented and
  correctly halting-capable (`raise SystemExit` on failure, confirmed in
  source) before any of this cycle's own new diagnostics are trusted.
- The floor-gate on `window_stats()` cleanly falsified the Phase-1
  proposal's own "possibly >10% unresolved at r=312" prediction, in the
  reassuring direction (`frac_unresolved=0.0` at both r, `n=4000`) — a
  real, disclosed prediction that could have gone the other way and did
  not; this closes exp-105's own Phase-5-named gap cleanly on this half.
- The cost-gate fired two different ways on two legs of the identical
  r=312 domain (primary pilot 52.65 min → committed; settling pilot
  reported as 103.28 min → deferred) — exactly the asymmetric behavior
  the pre-registered rule was designed to produce, a genuine positive
  control for the cost-gating discipline itself. (One caveat: the
  103.28-min settling-pilot figure is not itself a `results.json` field —
  `wall_312_settling_s` is `None`, and no `run_output.txt` is committed
  to this directory — so this specific number, while almost certainly an
  accurate transcription of the live run's own console output, cannot
  currently be independently re-verified from any committed artifact.
  Minor, non-load-bearing, but worth a one-line persistence fix
  (`wall_312_empty_settling_pilot_s`) alongside §2b's above.)
- R23 code-enforcement (mandatory fix 5, VISION's own Attack 5) is
  correctly implemented: both `predictions_text_` and `result_text` are
  single f-strings that embed every one of items 1–4's own new verdict
  language, and both `assert DISCLAIMER in ...` lines check those actual
  concatenated strings — verified by direct read of `build_predictions_
  text()` and the inline `result_text` block. This is the correct
  discharge of a disclaimer-erosion risk this exact sub-thread has now
  hit three separate times (R23's own founding cycle, plus two more data
  points named in exp-105's own Phase-5 layer) — a clean pass this time.
- Red Team's own Attack 6 (overriding MATERIALS' stale realizability
  citation with a citation-grounded replacement, correcting my own §5
  sentence in the same stroke) is R8 discipline working exactly as
  designed — verify before claim, applied to a critique's own premise,
  not just a proposal's.

## 3. Ranked top-3 candidate directions for Iteration 84 (QUANTUM OPTICS' own charter)

1. **Same-shift-class fix: implement mandatory fix 1's own reclassification
   rule and re-report item 4's verdict.** Given `p_abs_frac_diff` already
   measured at 12.3%/18.0% (both over the ~10% trigger), item 4's
   classification should read three-way-ambiguous (thickness-law vs.
   core-reflection/gradient-steepness vs. both), not a bare REFUTE with
   only a trust qualifier — this is the single highest-priority, zero-new-
   FDTD-cost item on the board (§2a), and the cheapest one to close before
   any future cycle cites this cycle's own headline number as settled.
2. **Run exp-052's literal hollow-vs-PEC-cored delta test on the fixed-abs
   family at r=156/312** — the one instrument that would actually
   discharge EM's own named core-reflection-leakage hazard (§2c), which
   neither `core_frac` (structurally uninformative for a PEC core, per
   Red Team's own Attack 9) nor `sigma_abs/sigma_ext` (aggregate, not
   spatially resolved to the forward window) can rule out. A real,
   disclosed, Tier-2 FDTD cost, but the most load-bearing remaining gap
   standing between "REFUTES the electrical-thickness-growth hypothesis"
   and "this discriminator is actually clean."
3. **Pursue a genuinely different bridge-family geometry (wider `D_EFF`,
   a denser `DENSE_PITCH`, or a chosen 4th r-point) specifically engineered
   to cross `nyquist_margin≥2.0` at the far end of the family** — per §2d,
   the current self-similar r=78/156/312 construction structurally cannot
   ever produce `p3_trusted=True` at r=312 no matter how many settling
   legs are re-run on the identical geometry; if this program wants a
   fully-trusted `shape_ratio` reading at the scale where P3's own
   accelerating-collapse finding is most extreme, the domain construction
   itself — not another diagnostic on the existing one — is the load-
   bearing next step.
