# Phase 5 Review — ELECTROMAGNETISM seat
## Panel Iteration 78 (exp-101), fresh sub-agent, second pass on this cycle

I am the same seat whose Phase-2 critique (`phase2_critique_em.md`) found the
false `widths_direction_corrected` citation and the missing amplitude floor
on `p_scat`. This review does not reuse that memory as evidence — every
claim below was re-derived this session directly from the committed source
(`lab/sections.py`, `run.py`, `results.json`, `run_output.txt`,
`design_geometry.py`, `LOGBOOK.md`'s R13 text, and a live re-run of trust-
suite stage 8), per the task's own instruction to check what actually landed
in the executed code, not what NOTES.md says landed.

**Verdict: PROCEED. The Tier-0 core deliverable is sound and its two
mandatory Red Team fixes that this review was asked to re-verify (the false
citation, the amplitude floor) both genuinely landed in the executed code,
not merely in prose.** But this pass found two defects in the finished
cycle that survived every prior review layer (five Phase-2 critiques, the
Red Team audit, and NOTES.md's own self-scoring) — one substantive
(§5 below, an unquantified but large and systematic energy-bookkeeping
finding that undercuts how NOTES.md frames its own flagged `back_frac`
trend), one a concrete numeric restatement error in Result prose (§6). Both
are disclosed in full below with independent recomputation.

---

## (a) Was the false `widths_direction_corrected` citation actually removed?

**Yes, confirmed in both NOTES.md and run.py's own code comments — not just
asserted as fixed.**

- `run.py` lines 24-28 and the `sigma_scat_partition()` docstring (lines
  175-180) state the warrant correctly and *explicitly name the retracted
  citation as false*: "NOT by analogy to `widths_direction_corrected`
  (whose citation as precedent was FALSE — that function never touches
  `back_frac`/`fwd_frac` at all; Phase-3 fix 2)." This is not merely
  omitting the bad citation — it affirmatively documents why it was wrong,
  which is the stronger and more useful form of the fix (a future reader
  can't reintroduce the same error without seeing this note).
- NOTES.md's Setup section and "Changes from Phase 1" item 2 say the same
  thing in the same words.
- I independently re-read `experiments/087-.../run.py:123-168`
  (`widths_direction_corrected`) myself this session: it applies
  `sign(i_inc)` to exactly `sigma_scat`/`sigma_abs`/`sigma_ext`/
  `sigma_ext_cross` via a named-key loop and leaves `back_frac`/`fwd_frac`
  untouched in its `dict(w)` copy — confirming the false-citation finding
  itself was correct, and that the correction is now accurate.
- The *actual* function `widths_direction_corrected` is still *called* by
  `sigma_scat_partition()` (line 172-173) to do the real computation — that
  is correct and expected; only its use *as a citation/warrant for the
  back_frac/fwd_frac relabeling* was the false claim, and that citation
  role is gone from both files.

## (b) Is the `sigma_scat` floor gate a real amplitude floor, or still just a `1e-30` fig leaf?

**It is a real, data-driven, amplitude-normalized floor — genuinely
different from and stricter than the `1e-30` anti-division-by-zero guard —
but its enforcement in the executed code is incomplete relative to what
NOTES.md and R13 both say it should be.**

Traced the full chain in `run.py`:

```
FLOOR_FRAC_SCAT = 0.10                                          # line 159
all_sigma_scat = [partitions[(key, th)]["sigma_scat"] for th in ... ]  # line 242
floor_scat_rms = sqrt(mean(sigma_scat^2))                        # line 243
floor_scat = FLOOR_FRAC_SCAT * floor_scat_rms                     # line 244
...
scat_floor_pass = abs(part["sigma_scat"]) >= floor_scat           # line 269
outcome = "resolved" if scat_floor_pass else "UNRESOLVED-BY-CONSTRUCTION"
```

This is computed from the actual 12-cell `sigma_scat` distribution (10% of
its RMS), independent of the `1e-30` clamp buried inside `back_frac`'s own
formula in `lab/sections.py::widths()`. It is exactly the "amplitude-
normalized magnitude" form R13 explicitly permits (`LOGBOOK.md` line
410-412, re-read verbatim this session), not the anti-zero epsilon the
Phase-1 proposal originally, wrongly, cited as satisfying it. This is a
real fix, not a fig leaf — confirmed from the executed code, not NOTES.md's
description of it.

**Two things this review adds that no prior phase flagged:**

1. **The floor had no practical chance to fail this cycle, and "0/12
   unresolved" should not be read as evidence the gate is well-powered.**
   I recomputed the 12 raw `sigma_scat` values: they range 293.7–320.9 (a
   ~9% spread), giving `floor_scat=30.68` against a population that never
   drops below 293.7 — over 9× the floor at the closest approach. Given
   this family's `sigma_scat` is dominated by stable, near-total-absorption
   physics rather than the oscillatory `delta_scene`-like behavior R13's
   founding case worried about, this specific floor was never close to
   being exercised. That is a reassuring physics finding (the concern EM's
   own Phase-2 critique raised turned out not to materialize on real data)
   but it means this run does not constitute a genuine stress-test of the
   gate's discriminating power — worth stating plainly rather than letting
   "all cells cleared cleanly" imply more validation than it earned.

2. **The gate's exclusion is wired into only one of the four fields it is
   supposed to protect — a real gap between the code and both NOTES.md's
   own stated contract and R13's adopted text.** NOTES.md's Predictions
   section states: *"All four bands below apply only to cells that clear
   the Fix-1 amplitude floor... a cell failing it is reported
   UNRESOLVED-BY-CONSTRUCTION and is not scored against any band."* R13's
   own text (re-read verbatim, `LOGBOOK.md` ~444-448) requires a failing
   cell be "excluded from classification, never silently scored alongside
   angles that cleared it." Reading `run_leg_b_fixed()`'s row-building loop
   (lines 278-300) line by line: `scat_floor_pass` gates **only**
   `row[f"{prefix}_partition_forward_continuing"]` (line 299-300, set to
   `None` on failure — the field feeding Prediction 3's per-cell display).
   `row[f"{prefix}_sigma_abs"]` (Prediction 1), the raw
   `row[f"{prefix}_sigma_scat_downstream"]`/`sigma_scat_sourceward"]` pair
   from which `back_frac` is reconstructed (Prediction 2), and
   `row[f"{prefix}_box_dev_scat_downstream"]` (Prediction 4) are all
   assigned unconditionally from `part[...]` a few lines earlier
   (lines 279-286), with no `scat_floor_pass` check anywhere near them.
   `main()`'s own `n_box_dev_scat_downstream_fail` counter (line 344-345)
   likewise counts `>XI_TOL` cells with no floor exclusion. **This is moot
   for this specific run — 0 of 12 cells failed the floor, so no band was
   ever scored on an unresolved cell here — but it is a live latent defect
   in the code as committed**: if a future rerun/extension of this exact
   pipeline produces even one `UNRESOLVED-BY-CONSTRUCTION` cell, Predictions
   1, 2, and 4 will still silently score it, contradicting the cycle's own
   written commitment and the standing rule it was adopted to satisfy. None
   of the five Phase-2 critiques or the Red Team audit could have caught
   this — they reviewed the *proposal*, before `run.py` existed — but it
   also was not caught by NOTES.md's own Result section, which asserts
   compliance ("Every mandatory Phase-2 fix discharged as designed... the
   gate was a real, executed check, not merely asserted") without noticing
   the check's exclusion effect is partial.

## (c) Independent re-derivation of the face/sign convention from raw `_face_flux`/`Sx` primitives

**Confirmed correct — no sign or dimension error found.** Re-derived from
scratch, not from my own or Red Team's prior conclusion:

- `lab/sections.py::_face_flux`'s `sx(xf) = -0.5·Re{Ez·conj(Hy)}`; total
  outward flux = `sx(x1) - sx(x0) + sy(y1) - sy(y0)` — i.e. outward flux
  through the **low-x** face is `-sx(x0)`, through the **high-x** face is
  `+sx(x1)`.
- `widths()`'s `p_back = -Σ(-0.5·Re{Ez·conj(Hy_interp)})` at `x0` is
  literally `-sx(x0)` written out by hand — the *same* low-x outward term.
  `p_fwd = +Σ(-0.5·Re{...})` at `x1` is literally `+sx(x1)`. Both match
  `_face_flux`'s own convention exactly; no independent formula was
  introduced that could have drifted from it.
- `design_geometry.py::r4_config()` (read directly, not from the brief):
  `src_x = R4_BASE_SRC_X(+pad) = 600(+pad)`, `obj_x = 340(+pad)`,
  `plane_x = 154(+pad)` — confirming `src_x > obj_x > plane_x`, i.e.
  propagation toward **−x**.
- `experiments/100-.../run.py::plane_x_behind()` (read directly):
  `cfg["obj_x"] - R4_R_OUT - PLANE_OBS_STANDOFF_CELLS` — strictly less than
  `obj_x`, confirming this bench's own established "downstream" = low-x for
  this geometry, independent of anything exp-101 asserts.
- Therefore `back_frac`'s numerator (`p_back`, the low-x outward term) is
  independently, geometrically the downstream-exiting scattered power for
  T28/R4's own reversed source placement — the proposal's bottom-line claim
  holds, verified from three independent primitives (the raw Sx formula,
  the raw config constants, and the established `plane_x_behind` idiom)
  rather than by trusting any one of them alone.

## (d) Internal energy-bookkeeping consistency

**Confirmed, computed independently from `results.json`'s raw fields, not
from NOTES.md's restatement:**

- `sigma_abs + sigma_scat == sigma_ext` to floating-point precision at all
  12 cells (this is a definitional identity in `widths()`'s own return
  dict, so it is not an independent physics check by itself — but it does
  confirm no field got mislabeled or dropped between `lab/sections.py` and
  `run.py`'s persistence layer, which is exactly the kind of R4-class
  transcription error this bench has hit before).
- The genuinely independent check — `sigma_ext` (direct box ledger) vs.
  `sigma_ext_cross` (optical-theorem cross-term route) — agrees to
  `xi_ext ∈ [6.5×10⁻⁵, 2.6×10⁻⁴]` across all 12 cells, 460×–1800× inside
  the `XI_TOL=0.12` gate. I additionally ran `lab/validation/run_all.py
  --only 8` live this session (6/6 passed) and confirmed the trust suite's
  own reference case shows a comparable-quality two-route agreement
  (0.001–0.002 for PEC) — this cycle's real data is not merely passing a
  loose bar, it agrees about as tightly as this bench's own gold-standard
  gate case.
- All four of NOTES.md's headline Result ranges were independently
  reproduced by direct computation from `results.json`'s raw
  `partition_*` fields, exactly: `sigma_abs/sigma_ext ∈ [0.51291,
  0.51450]`, `back_frac ∈ [0.53243, 0.65358]`, `sigma_scat_downstream/312
  ∈ [0.54569, 0.61590]`, `box_dev_scat_downstream ∈ [0.00570, 0.04544]`.
  `run_output.txt`'s printed per-angle values match `results.json` exactly
  cell-for-cell (spot-checked all 12). No R4-class restatement defect in
  these four figures.
- `xi_pass=True`/`nonneg_pass=True` in `results.json` are genuine — I
  independently confirmed `cell_metrics_r4`'s `sigma_abs_nonneg` check and
  `sigma_scat_partition`'s own `xi_ext` gate operate on the *same*
  `box_for_r4(cfg, BOX_CLEARANCE_A_R4)`/`ref_for_r4(cfg)` pair (traced
  through `experiments/094-.../run.py:305-345`), so there is no gap between
  what the existing thermo channel gates and what the new partition
  channel reports for those two checks.

---

## New finding 1 (this review's own, not in any prior phase): the lateral-face leakage is large, grows systematically with angle, and is nowhere quantified

This is the substantive finding this review adds. `back_frac`/`fwd_frac`
only account for flux through the box's **x0/x1** faces; `sigma_scat`
(the denominator) is the **full four-face** sum, including `y0`/`y1`. I
computed, from persisted fields only, the fraction of `sigma_scat` that
neither channel accounts for:

| θ (deg) | lateral leak = 1 − (back_frac+fwd_frac), C40_R4 / G40_R4 |
|---|---|
| 37.127 | 0.3464 / 0.3471 |
| 38.590 | 0.3813 / 0.3814 |
| 39.200 | 0.3922 / 0.3928 |
| 40.265 | 0.4186 / 0.4170 |
| 41.461 | 0.4380 / 0.4396 |
| 42.961 | 0.4670 / 0.4656 |

Both configs agree to 3 decimal places at every angle, and the trend is
perfectly monotonic across all six (non-uniformly-spaced) angles, which is
itself evidence this is real oblique-incidence physics (flux redirected
toward the `y0`/`y1` faces as incidence steepens), not noise or an artifact
of the `delta_scene`-extremal angle selection.

This is not just "a lateral/diffuse remainder," the term NOTES.md's
Idealizations section uses — **at the largest tested angle (42.96°) it is
the single largest channel in the whole ledger**, exceeding `back_frac`
itself (46.7% lateral vs. 53.2–53.4% downstream), and it is the *mirror
image* of the very trend NOTES.md's own Learned section flags as
noteworthy ("`back_frac`'s real, monotonic decline with θ... worth a future
cycle's attention"). Framed only as "downstream scattering declines with
angle," that Learned-section observation is incomplete: the more complete
statement, trivially derivable from fields already in `results.json`
(`sigma_scat`, `sigma_scat_downstream`, `sigma_scat_sourceward`), is that
declining `back_frac` is largely *lateral redirection*, not a shift toward
`fwd_frac`/sourceward return (which stays a small fraction of a percent
throughout, `ssw/sscat` ≤ 0.0006 at every cell).

This matters specifically to my own charter (energy bookkeeping across the
whole ledger, not just the two channels this cycle chose to name) and,
independently, to a question the lead seat's own Phase-1 proposal raised
and explicitly declined to score: *"`sigma_scat` split by direction tells
me whether residual light exits toward the observer... or laterally (a
possible ambient cue at rest, constraint 3's own concern, unscored here)."*
The number that question needs — how much, and whether it is growing — was
already sitting in this cycle's own persisted data and was never computed
or surfaced. I am not asserting this changes any constraint verdict (this
cycle correctly disclaims scoring constraint 3 at all), only that the size
and clean growth of this un-named channel deserved a line in Result/Learned
that it did not get, given this bench's own standing sensitivity (R16/R21)
to headline-shaped quantities that are persisted (implicitly, via their
constituent fields) but never narrated.

## New finding 2 (this review's own): a concrete numeric restatement error in the Result section

NOTES.md's Result states: *"Constraint 2 (`observer_article_norm`, unchanged
`observer_record_t28`) stays clean this cycle: `2.26e-4`–`3.95e-4` across
all 12 cells."* I recomputed the true min/max of
`partition_{C40_R4,G40_R4}_observer_article_norm` across all 12 cells
directly from `results.json`:

```
true range: [1.1554e-4, 3.9490e-4]   (min at G40_R4, θ=37.127246°)
stated range: [2.26e-4, 3.95e-4]     (this is actually C40_R4's own min/max only:
                                       C40_R4 min = 2.2591e-4 @ θ=38.590°,
                                       C40_R4 max = 3.9490e-4 @ θ=42.961°)
```

The stated lower bound is roughly double the true minimum across all 12
cells — NOTES.md's own "across all 12 cells" claim silently reports the
C40_R4-only range instead. This does not change the substantive
conclusion — even the true minimum (1.1554×10⁻⁴) is still ~173× inside the
R18 validation-gate bar (0.02), comfortably satisfying the "≥50× inside"
framing NOTES.md separately states — but it is exactly the class of defect
R4 exists to catch ("a Phase-5 reviewer's own re-check must RECOMPUTE, not
restate, any cell/combinatorial count it cites"), and it slipped past this
cycle's own self-scoring because it only exists in the post-run data no
Phase-2 critique or the Red Team audit ever saw.

**Minor cosmetic note, not scored as a defect:** NOTES.md's phrase "absorbed
power rising 310→339 W-equivalent-cells" conflates `sigma_abs` (a
cross-section width, in cells — correctly 310.9→338.8 across the sweep)
with `p_abs_w` (actual absorbed power, in Watts, ~2.8×10⁻¹²→3.3×10⁻¹² W) by
inventing a hybrid unit that is neither. The cited numbers are correctly
`sigma_abs`, just mislabeled; worth a wording fix next time this sentence
is reused, not a substantive error.

---

## Disposition summary

| Item | This review's finding |
|---|---|
| (a) False citation removed | **Confirmed fixed**, in both NOTES.md and run.py's own comments, with the retraction explicitly documented, not merely omitted. |
| (b) Real amplitude floor vs. fig leaf | **Confirmed real** (data-driven, amplitude-normalized RMS floor, computed and applied in code) — but **only partially wired**: 3 of 4 predicted bands (1, 2, 4) are not actually excluded from scoring on a hypothetical floor-failing cell, contradicting NOTES.md's own stated contract and R13's text. Moot this run (0/12 failed); live latent gap for future reuse. |
| (c) Face/sign convention | **Confirmed correct**, independently re-derived from `_face_flux`'s raw Sx formula and `design_geometry.py`'s raw `src_x>obj_x>plane_x` ordering — no defect found. |
| (d) Three-way partition internal consistency | **Confirmed**: `sigma_abs+sigma_scat=sigma_ext` exactly; `xi_ext` (two independent extinction routes) agrees to 6.5e-5–2.6e-4, as tight as the trust suite's own reference case. All headline Result numbers independently reproduced exactly. |
| New: lateral-face leakage | **Not previously surfaced.** 35–47% of `sigma_scat`, growing monotonically with θ, exits laterally — larger than the disclosed "remainder" framing suggests, and the more complete explanation of the `back_frac` trend NOTES.md does flag. |
| New: `observer_article_norm` range | **Concrete restatement error**: NOTES.md's stated "2.26e-4–3.95e-4 across all 12 cells" is actually C40_R4's own range; the true 12-cell range is [1.1554e-4, 3.9490e-4]. Does not change the constraint-2 verdict. |

**Bottom line for this seat:** the Tier-0 mandate was executed honestly and
the two Red-Team-mandated fixes this review was specifically tasked to
re-verify (false citation, real floor) both genuinely landed in the
executed code. The cycle's own self-scoring is trustworthy on its
headline numbers but imperfect in two independently-verifiable ways this
pass caught: an incompletely-wired floor-exclusion (dormant this cycle,
live for the next), and a mismeasured range in one already-passing metric.
Neither defect changes this cycle's own verdict (PROCEED, Tier 0 delivered,
no constraint violated). The lateral-leakage finding is this review's
primary substantive contribution and belongs in the next cycle's LOGBOOK
disclosure alongside the `back_frac` trend it explains.
