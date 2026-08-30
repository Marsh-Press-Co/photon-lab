# PHASE 3 — SYNTHESIS · Panel Iteration 68 · exp-091 · Director

## 1. Disposition of the mandatory-fix docket: all ten items adopted, zero overridden

Red Team's Phase-2 audit (`phase2_redteam_audit.md`) independently re-derived
every load-bearing number in `phase1_proposal.md` and all five blind
critiques from primary sources before adjudicating. I re-checked the two
sharpest numeric claims myself, independently a third time, before accepting
anything: `margin(40.2°) = 2.830881e-4 / 1.91744e-4 = 1.4764`,
`margin(41.4°) = 2.510967e-4 / 1.91744e-4 = 1.3095` — confirming **41.4° is
the thinner-margin, more crossing-proximate angle** (0.061° vs 0.065° from
its own crossing), exactly as QUANTUM found and Red Team independently
reproduced. Both re-derivations landed bit-exact against the proposal's own
§2b table. I adopt the verdict PROCEED-WITH-MANDATORY-FIXES and all ten
items **in full, none overridden** — every item survived independent
re-derivation, none is discretionary, and two (fix 4 under R8, fix 1/2 as a
genuine self-contradiction) are load-bearing corrections, not style notes.

Disposition of each item, and how it is discharged in this cycle's final
design (§2) or in this document/`NOTES.md`'s prose (§3):

1. **Move/add the settling spot-check to 41.4°.** Adopted as **run both**
   40.2° AND 41.4° (the docket's own offered alternative) rather than merely
   relocating — budget headroom is ample (see §2's cost re-accounting) and
   leaving 40.2° completely unchecked after having explicitly claimed it as
   "the hardest case" for three cycles running would trade one gap for
   another. Both angles now get an independent `STEPS=6300` settling
   spot-check.
2. **Correct Idealization 10.** Done in `NOTES.md` §5 — restated to name
   41.4° as the more crossing-proximate/thinner-margin angle, not 40.2°,
   and to reflect that both angles are now spot-checked (item 1).
3. **Add PHOTONICS' location-sensitive companion test.** Adopted as a
   zero-marginal-cost desk computation using item 4's own bracket points
   (see §2.3) — a linear interpolation of `delta_scene`'s `cpl=30`
   zero-crossing between each existing R3-leg angle and its new bracket
   neighbor, compared against the known `cpl=20` crossing location. Folded
   together with item 4 rather than run as a separate, weaker 3-point
   version, per Red Team §2's own compounding-finding recommendation.
4. **Add EM's bracketing points.** Adopted as **two new angles on the
   existing native `DENSE_ANGLES` grid**, not off-grid values: **40.4°**
   (bracketing the 40.265° crossing together with the already-budgeted
   40.2° R3-leg point) and **41.6°** (bracketing the 41.461° crossing
   together with the already-budgeted 41.4° R3-leg point). Grid-aligned
   angles are preferred over an arbitrary offset (e.g. ±0.15°) because
   `exp-083`'s own committed 31-point census already has bit-exact `cpl=20`
   `delta_scene` values at 40.4°/41.6°, giving this cycle a free, exact
   `cpl=20` comparator at the new bracket angles too — a strictly stronger
   design than an off-grid point would allow, at the same call cost (8 new
   calls: 2 angles × 2 configs (`C40_R3`/`G40_R3`) × 2 legs (empty/article),
   `cpl=30`, `STEPS=4200`). See §2.2 for the full cost re-accounting.
5. **Add THERMODYNAMICS' co-equal `frac_p_abs` prediction.** Adopted as a
   new PRIMARY prediction, §4(b2) in `NOTES.md`, reusing (a)'s own
   `[0.3,3.0]`/`[0.1,10]` bands at all three census angles, zero marginal
   FDTD cost.
6. **Fix the banner citation.** `phase1_proposal.md` is NOT retroactively
   edited (house convention: a frozen document is corrected forward, not
   rewritten in place — the same discipline `VALIDATION.md` states for
   exp-046's own unamended gate). `NOTES.md`'s own banner cites the correct
   **Idealizations 3/6/7** throughout.
7. **Add the computed absolute-Weber-contrast comparison.** Red Team's own
   §3 computation is reused verbatim (re-verified independently below,
   §2.4) and carried into `NOTES.md`'s Idealizations/Predictions sections
   as a checked fact, citing Red Team's audit as the source.
8. **Operationalize or drop the "felt-lucky" relief claim.** Adopted as a
   new disclosed (non-gating) prediction, §4(d), scoring the 37.2°
   `resolved`-gate noise-floor margin at `STEPS=4200` against its cited
   `STEPS=2800` figure of `1.046×` — zero marginal cost, uses Leg 1's own
   already-budgeted `p_abs_w` values.
9. **Precision QUANTUM's wording.** Applied throughout `NOTES.md`: "a
   close, live possibility," never "the expected case."
10. **Cross-reference item-1 and item-4's results.** Written into
    `NOTES.md`'s Predictions section as an explicit forward instruction for
    the Result write-up: report whether the bracket-derived `cpl=30`
    crossing shift (item 4) is directionally consistent with which of the
    two spot-checked angles (item 1) shows the larger settling residual.

## 2. Final design — reconciling the ten items into one frozen configuration

### 2.1 Unchanged from `phase1_proposal.md`

- Leg 1 (native-`cpl` repeat): `cpl=20`, `STEPS=4200`, angles
  `{37.2°,40.2°,41.4°}`, `PAIR_KEYS=("C40","G40")`, both legs (empty,
  article) — **12 calls**, unchanged.
- Leg 2 (R3 leg): `cpl=30`, `STEPS=4200`, angles `{37.2°,40.2°,41.4°}`,
  `PAIR_KEYS_R3=("C40_R3","G40_R3")` — **12 calls**, unchanged. `G40_R3 =
  r3_config(60, 60)` is the one new entry this cycle adds to
  `experiments/069-.../design_geometry.py::R3_CONFIGS` (`C40_R3` already
  exists there, unmodified, as `r3_config(60, 0)` — independently confirmed
  by Red Team §0 to be the correct R3-scaling of native `C40=config(40,0)`).

### 2.2 Extended per item 1: R3 settling spot-check now at BOTH angles

`cpl=30`, `STEPS=6300` (`=4200×1.5`), angles `{40.2°, 41.4°}` (was 40.2°
only), both configs, both legs — **8 calls** (was 4, +4).

### 2.3 New per item 4: the bracket leg

`cpl=30`, `STEPS=4200`, angles `{40.4°, 41.6°}` — both exact, existing
`DENSE_ANGLES` grid members (`DENSE_ANGLES[i] = 39.0 + i×0.2`: `i=7→40.4`,
`i=13→41.6`; independently satisfies the generator's own definition,
`round(39.0+7*0.2,4)=40.4` and `round(39.0+13*0.2,4)=41.6`). `run.py` will
select them by **value**
(`dg.DENSE_ANGLES[dg.DENSE_ANGLES.index(40.4)]`-style, i.e. asserting
membership rather than hand-typing an index), precisely to avoid shipping a
hand-computed index error into frozen code — R4's own standing discipline
(no hand-typed figure stands in for one the committed code actually
computes). `PAIR_KEYS_R3`, both legs — **8 calls** (new).

### 2.4 Total call count and cost (re-derived from `dg069._cost()`, by hand)

**40 calls total** (was 28): 12 (native) + 12 (R3) + 8 (R3 settling,
extended) + 8 (bracket, new).

| Block | CPU-s | Basis |
|---|---|---|
| Native repeat (unchanged) | 1076.4 | `3×2×(75.0+104.4)` |
| R3 leg (unchanged) | 2421.9 | `3×2×(168.75+234.9)` |
| R3 settling spot-check (2 angles) | 2422.0 | `2×[2×(253.125+352.35)]` |
| Bracket leg (new, 2 angles) | 1614.6 | `2×[2×(168.75+234.9)]` |
| **Total** | **7534.9 CPU-s ≈ 125.6 CPU-min** | |

Wall time at `N_WORKERS=4`, `PARALLEL_EFFICIENCY=0.98`, `OVERHEAD_FACTOR=
1.15` (unchanged house constants): `1.15×7534.9/(4×0.98) ≈ 2211s ≈ 36.9
min`; 3× safety envelope ≈ 111 min. Still comfortably inside every
established T28 per-cycle FDTD budget (exp-083's own 31-point census, the
largest single T28 FDTD block on record, ran well beyond this).

I independently re-verified Red Team's absolute-Weber-contrast table
(fix 7) by re-deriving one cell by hand from primitives rather than only
citing it: `|delta_scene(41.4°)| × 3.0 = 1.337362e-4 × 3 = 4.012086e-4`;
`4.012086e-4 / 0.005 = 0.08024 = 8.0%` — matches Red Team's cited "8.0%,
≈12.5× below" exactly. Accepted as checked, carried into `NOTES.md`.

### 2.5 Explicitly unchanged

`XI_TOL=0.12`, `NOISE_MULT=3.0`, `RATIO_LOW/HIGH=0.1/10.0`,
`FLOOR_FRAC=0.10`, `FLOOR=1.91744×10⁻⁴` (applied unrecomputed, per
Idealization 6/item 6 above), `BOX_CLEARANCE_A/B`, `REF_HALF_H` R3-scaled
exactly as `phase1_proposal.md` §2b specified. Nothing in the ten-item
docket touches these.

## 3. What this synthesis does NOT change

No item in the docket asks for a different mechanism, a relaxed threshold,
or a re-opened ruled-out question. This remains, exactly as proposed and as
every T28 desk/instrument cycle since exp-069 has been: **T1 route N/A,
Checkpoint criterion 2 N/A**, pure instrument recalibration. R13/R14 are
applied unchanged. No new numbered rule is being proposed by this
synthesis — the docket closes gaps in this cycle's own design, it does not
allege a program-wide defect in R13/R14's text.

## 4. Checkpoint criterion 4

I independently re-read Red Team's two-ground ruling (shape-mismatch vs.
the omission lineage; caught-blind-at-Phase-2 discharge) against
`LOGBOOK.md`'s own four prior disclaimer-erosion entries (Iterations 53,
63, 64, 65) myself before accepting it. Both grounds hold on inspection:
VISION's finding is a footnote-numbering error inside an otherwise
correctly-present, correctly-worded, correctly-scoped banner — not a
caveat failing to propagate at all. **Checkpoint criterion 4 does NOT
fire.** No other matter this cycle approaches it. Criterion 5 (two
consecutive non-advancing cycles) is N/A: exp-090 closed PARTIAL with a
usable deliverable, and this cycle, once run, directly discharges the
single oldest undischarged item on the T28 board.

## 5. Predictions frozen

See `NOTES.md`, committed in this same push, strictly before any Phase-4
`run.py` exists — house discipline, non-negotiable.
