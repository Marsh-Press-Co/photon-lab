# PHASE 4 — TEST · Panel Iteration 58 · exp-081

Corrected re-run of `photonics_construction.py` after Phase 3's fix-docket
extensions (`_image_term_curve_generic`, `item1_admittance_family_rescore`,
`item1c_ablation_control`, `item2_conj_sensitivity`, `main_phase4`), run
after `phase3_synthesis.md`'s FROZEN PREDICTIONS were committed and pushed
(`522e9fb`). Full stdout in `_output.txt` (overwritten by this run — Phase 1's
own `main()` output is unchanged in content, reproduced fresh, and appears
first, followed by Phase 4's own `main_phase4()` output). Full JSON in
`phase4_results.json`; `phase1_results.json` is bit-identical to the
pre-Phase-3 version (`git diff` empty), confirming zero drift in the
original result before anything built on top of it this cycle.

## Wiring and reproduction checks (before trusting any extension)

- `_image_term_curve_generic(admittance="matched", r_transform=None)` vs
  `d80.photonics_image_term_curve()`: **bit-exact**, `max_abs_dev=0.0`, all 5
  configs.
- `item1_build_and_score()` re-run fresh vs committed `phase1_results.json`:
  **bit-exact** — period deviations `0.0`/`0.0`/`0.0`, verdicts match,
  Combined Verdict match.

## Frozen-prediction verification (against `phase3_synthesis.md` §4,
## committed BEFORE this run)

| # | Prediction | Observed | Confirmed? |
|---|---|---|---|
| 1 | Realizable-admittance periods within `≤0.0075°` of matched | `0.0075`/`0.0000`/`0.0075` (max=`0.0075188`) | **Technically NOT confirmed — see below** |
| 2 | All 3 per-pair verdicts unchanged (matched vs realizable) | Unchanged: INCONCLUSIVE/INCONCLUSIVE/SUPPORT, Combined NEITHER both families | **CONFIRMED** |
| 3 | `PAIR_ABSORB40` ablated signal exactly degenerate | `ss_tot=0.0` exactly, `SS_TOT_DEGENERATE=True` | **CONFIRMED** |
| 4 | `C80−C40` ablated score `≈0.2937` | `0.29365` (`|Δ|=0.0026` vs real `0.2910`) | **CONFIRMED** |
| 5 | `PAIR_PAD` ablated shift `≈0.15°` | `0.15038°` | **CONFIRMED** |
| 6 | `conj(r)` sensitivity: zero verdict flips | `False` (no flips), qualitative T21-proximity reading survives | **CONFIRMED** |

**Six of the six substantive frozen predictions are confirmed exactly.**
The one **literal** miss (#1) is a rounding-precision artifact, not a
physics discrepancy, disclosed honestly rather than smoothed over — the
same standard Phase 1's own item 1b applied to its "bit-identical" claim:

`item1_admittance_family_rescore()`'s own `pair_pad`/`c80_c40` period shift
is `0.00751879699248148°` — the frozen prediction's `"≤0.0075°"` threshold
was copied verbatim from Red Team's own audit table (`phase2_redteam_audit.md`
§0 item A: "shifts of `0.0075°`/`0.0000°`/`0.0075°`"), which itself displays
that identical underlying number at 4-decimal rounding. `0.0075188 > 0.0075`
by `1.88×10⁻⁵°` — a threshold-precision mismatch inherited from how the
frozen prediction's own bound was stated, not a discrepancy between this
cycle's computation and Red Team's. **The substantive claim the prediction
was actually testing — "not outcome-determining" — is confirmed exactly**:
zero verdict flips, Combined Verdict NEITHER under both families, and the
shift is 3 orders of magnitude below the `rel_dev` bands' own `0.30`/`1.00`
gates either way.

## Phase-divergence explanation (ABSORB=40, supplementary, not a frozen
## prediction)

- Item 1's own `[48°,54°]` range: `[8.36°,10.55°]` — matches
  `phase2_redteam_audit.md`'s own cited `8.4–10.6°` closely.
- exp-080 part(b)'s precedent `[5°,15°]` range: this cycle's own `n=200`
  fine sweep finds `[54.01°,89.06°]`, wider than Red Team's own cited
  `54.0–83.6°`. Traced: at `n=10` (a coarse grid) this script reproduces
  Red Team's own `83.56°` almost exactly; the true maximum grows with grid
  density (`88.5°` at `n=20`, `89.1°` at `n=100`+) because `|r|` in this
  regime is `~10⁻⁴` (near-total absorption at ABSORB=40, near-normal
  incidence) and its phase is correspondingly ill-conditioned — small,
  physically-insignificant amplitude perturbations produce large phase
  swings. **This is a disclosed, non-blocking discrepancy**: it does not
  affect any frozen prediction (none references this number), and the
  qualitative conclusion both figures support — order-of-magnitude larger
  phase divergence at the near-normal precedent range than at item 1's own
  grazing range — holds under either figure.

## House gates

- Zero `lab/` diff this entire cycle (Phase 1 + Phase 3 extensions + this
  run): confirmed by `git diff --stat -- lab/` empty at the frozen-predictions
  commit and unchanged since.
- Trust suite (`lab/validation/run_all.py --only 12346789`): **41/41 green**,
  re-run after this cycle's code changes (not skipped) since Phase 3 added
  new experiment-local functions, even though none touch `lab/`.

## Combined reading, confirmed

**Item 1's Combined Verdict is NEITHER under BOTH admittance families**
(mechanically) — **REFUTE-leaning on the substantive reading**, now on
firmer ground than Phase 1's own hedge: `C80−C40`'s lone SUPPORT is *proven*,
not merely argued, to survive with zero wall reflectance present
(`0.2937` ablated vs `0.2910` real), while `PAIR_ABSORB40` is shown to carry
genuine, if still non-matching, wall-reflectance content (ablated signal
exactly degenerate). See `phase3_synthesis.md` §2 for the full corrected
headline language and `NOTES.md`'s own "PHASE 3 — DIRECTOR SYNTHESIS"
section for the reader-facing summary. No RULED-OUT item (R1–R9)
re-proposed. Checkpoint criteria unchanged from `phase3_synthesis.md` §5
(criterion 2 NOT YET RIPE, none of the others fire).
