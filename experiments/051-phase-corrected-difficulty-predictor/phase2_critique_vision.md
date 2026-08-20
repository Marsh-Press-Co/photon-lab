# PHASE 2 — CRITIQUE (VISION SCIENCE) · Panel Iteration 28 · exp-051

*Blind critique. Every figure below was produced by invoking exp-050's own
committed `design_geometry.py` at `GEOM78`, or read directly from
`experiments/050-.../results.json` / `experiments/049-.../results.json` —
none is hand-typed (R4). The recomputation is bit-exact against the
committed table (0.0 relative error on all 18 `c41`, and on every
`converged_value` where `results.json` records one), so the derived numbers
inherit that anchor.*

## Steel-man (≤150 words)

By my seat's own test — is a perceptual quantity being misused? — the
stated discipline is real: no material law, no T1 escape route, no
constraint-3/4 verdict, and idealization 9 refuses a perceptual claim
outright. And §2.1's table is *correct*, which the last two cycles' own
headline tables were not on first pass: I independently re-derived all
eighteen GEOM78 `n*` values and both `P(θ₀)` columns from the committed
modules — the 7-unstable/11-stable split matches `results.json` digit for
digit, the nine periods reproduce to <5×10⁻⁵ deg. It pre-registers
P-PCDP-2 *because* N=18 is thin (idealization 6), not despite it; keeps an
explicit `NOT_FOUND` diagnostic instead of a silent drop (idealization 5);
gates everything on an executable 27-point anchor; and P-PCDP-5 is a
genuine negative control against the trivial-rescaling story. Cost is
bottom-up on exp-050's honest ≈12,490 s, not the understated figure.

## Sharpest attack (≤150 words)

Both of §2.0's scoring constants are one perceptual number, and the label
breaks at that scale. exp-049's own §2.2 defines `ABS_TOL=5×10⁻⁴` as
**`0.1·C_THR`**; `C_THR=0.005` is T2's photopic Weber bar. §2.0 reprints
both without the dependency. Recomputed at GEOM78: every in-scope `|C|` is
≤**0.330·C_THR** at n=41 and ≤**0.218·C_THR** at n=81, so the
`|C(2n)|≥C_THR` clause **never fires** — all 18 labels are exactly
`Δabs(41→81) > 0.1·C_THR`. Measured `Δabs/ABS_TOL` spans **[0.073,
1.924]**; the entire class boundary is the gap **0.785→1.057**. At
`0.13·C_THR` four labels flip (7 positives→3); at `0.20·C_THR` all seven
vanish and P-PCDP-1/2/3 are undefined. The labelling is stable only over
`ABS_TOL ∈ [0.08, 0.10]·C_THR`. This cycle fits a predictor to where one
perceptual decimal, divided by ten, happens to cut a continuum.

## Verdict

**Support-with-changes.**

## The single parameter change that would flip to unqualified support

Score P-PCDP-1 against the **continuous** target
`log10(Δabs(41→81)/ABS_TOL)` (Spearman ρ over all 18, bands pre-registered
in the same CONFIRMED/PARTIAL/REFUTED shape), demoting the binary tier
label to a reported secondary — and commit one `ABS_TOL`-sensitivity
ledger row giving the positive/negative counts at `0.05/0.10/0.20·C_THR`.
Zero extra compute: `Δabs(41→81)` falls out of the same single `n=81` call
§2.2d already makes, against the `c41` `results.json` already holds. That
makes the cycle measure the quantity that is physical (the quadrature
residual, whose convention ratio is smooth and reproducible) rather than
the quantity that is an artifact (which side of `0.1·C_THR` that residual
lands on).

---

## Supporting evidence — the three questions in my lane, settled numerically

*(Working notes, not part of the critique proper. Method: `mine.py`,
18 combinations × n∈{41,81,161} through exp-050's committed
geometry-parameterized functions at `GEOM78`; anchor 0.0 relative error.)*

### 1. Is §2.1's labelling what the committed `results.json` says? — YES

All 18 `n*` values, the 7-unstable/11-stable split, and the nine `P(θ₀)`
values reproduce exactly. `P(θ₀)=degrees(CPL[λ]/(724·cos θ₀))` with
`CPL={450:15,600:20,750:25}` gives 1.4673/1.5064/1.5496/1.9564/2.0085/
2.0661/2.4455/2.5107/2.5827 — the proposal's table to 4 dp. No defect here.

### 2. Does the 7/11 balance support P-PCDP-1's AUC bands at N=18? — PARTLY

Exact permutation null over all C(18,7)=31,824 rank orders:

| AUC bar | P(reach it by chance) |
|---|---|
| ≥0.55 (the **hard-falsification escape**) | **0.362** |
| ≥0.65 (PARTIAL floor) | 0.143 |
| ≥0.85 (CONFIRMED) | **0.0057** |

The CONFIRMED bar is genuinely strict; the *falsification* bar is not — a
pure-noise feature escapes REFUTED-by-falsification more than a third of
the time, so "not falsified" will carry almost no evidential weight. Note
also the falsification clause is ambiguous as written ("< 0.55 … on either
the LOOCV or plain in-sample metric"): an in-sample 2-feature fit on 18
points essentially never scores <0.55, so under the conjunctive reading
P-PCDP-1 is close to unfalsifiable. Phase 3 should disambiguate.

**A confound P-PCDP-2 cannot survive as written.** Six of the seven
positives are `incoherent_corrected`. The zero-phase-information predictor
"convention == `incoherent_corrected`" scores **sensitivity 6/7 and
specificity 8/11** — *exactly* P-PCDP-2's own CONFIRMED bar — and AUC
0.792 (PARTIAL for P-PCDP-1). P-PCDP-2 therefore cannot discriminate the
phase hypothesis from the function label. Separately, the second regressor
is uninformative alone: AUC(`|C(81)|`) over the 18 = **0.519**, chance. So
P-PCDP-1's discrimination must come from `|offset|` essentially alone,
making P-PCDP-1 and P-PCDP-2 near-duplicate tests rather than independent
ones. The one prediction that *would* expose the confound is P-PCDP-3: at
`GEOM_EXP042_OLD` the balance is 8/10 and the same convention-label
predictor drops to sens 5/8, spec 6/10 (AUC 0.613). Phase 3 should
pre-register the convention label as an explicit baseline both
P-PCDP-1 and P-PCDP-2 must **beat**, not merely match.

### 3. Do any in-scope cells sit near `C_THR`, and is it disclosed? — SUBTLE; NOT DISCLOSED

At raw amplitude, **no**: the worst in-scope value is `|C(41)| =
1.65100×10⁻³` (450 nm/40°/`incoherent_corrected`) = 0.330·C_THR, and the
2°-step angular neighbours inside the committed grid are themselves
in-scope and all sub-threshold. Two things the proposal nonetheless does
not disclose:

- **The perceptually live cells are the ones excluded.** At the *same*
  (λ,θ₀) coordinates but FWHM=2°, three combinations exceed `C_THR`
  outright at GEOM78 — 750/40/`incoherent` +5.0996×10⁻³ (1.020·C_THR),
  750/36/`incoherent_corrected` −5.4503×10⁻³ (1.090), 750/40/
  `incoherent_corrected` +6.4986×10⁻³ (1.300) — and **all three are
  tier-stable (`n*`=41)**. The cycle's positives therefore live only where
  perception cannot bind; the FWHM=2° family where it does bind is out of
  scope. That is a defensible scope choice, but it belongs in §5, because
  a downstream reader will cite "difficulty predictor" without the
  FWHM-20°-only qualifier.
- **One in-scope cell does cross under this program's own committed
  amplitude correction.** Applying exp-042's per-λ corrected-convention
  `c*` (1.81/2.74/3.23 at 450/600/750 nm — LOGBOOK T21, Iteration 19),
  the same operation the panel already applied to the `beam_divergence_*`
  grid at Iteration 19, gives 750/40/`incoherent_corrected` at n=41
  **1.027·C_THR** — a crossing, at one of the seven positives. (Global
  `c*` variants do not cross: 0.827 at c\*=2.60, 0.515 at c\*=1.6196.)
  Which amplitude scale governs is exactly the question T21 leaves open;
  the honest form is a disclosed idealization, not silence.

### 4. Does the Iteration-27 standing rule bind, and is it honoured? — LETTER NO, SPIRIT YES; UNMENTIONED

The rule (LOGBOOK T21 addendum / exp-050 NOTES.md Reading): *"any future
near-boundary headroom citation at any geometry must be re-measured at its
own citation's actual geometry and checked against its own immediate
angular neighbours, not read from a single tracked cell in isolation."*
The proposal issues no headroom citation, so the letter does not bind. But
this is the **first cycle after the rule's adoption**, its whole subject is
angular fringe structure at 2°-spaced cells, and it never names the rule.
§2.1 *does* copy `n*`/`P(θ₀)` from committed tables, with recomputation
deferred to Phase 4 — that satisfies R4 for those figures, not the
neighbour clause. Both halves are cheap: everything in §3 above took under
two minutes of compute. Phase 3 should state in one sentence whether the
rule binds and, if so, discharge it — leaving it unmentioned in the first
cycle after adoption is how standing rules quietly lapse.

### 5. Two concrete defects for Phase 3 (not load-bearing to my verdict)

- **§2.2b's snippet will raise `KeyError`.** `local_period_deg(...,
  g["A"])` — neither `GEOM78` nor `GEOM_EXP042_OLD` has an `"A"` key
  (verified: keys are `NY, OBJ_Y, D_SP, GUARD_OUT, R_OUT, W_FLANK,
  PLANE_X, SRC_X, ABSORB, TAPER`). The adjacent prose formula
  `A = g["OBJ_Y"] − g["ABSORB"]` is right (764−40=724; 792−40=752); the
  code is not.
- **P-PCDP-5 counts wrong, and its bar is probably already failed.** A
  `|slope_corrected|/|slope_incoherent|` ratio is per **cell**, not per
  combination: there are **9** at GEOM78, not "the 18 per-combination
  slope ratios". Its IQR test is therefore on 9 points. For reference, the
  already-measured `Δabs(41→81)` convention ratios at those 9 cells are
  1.382 / 1.675 / 1.658 / 1.965 / 1.952 / 1.921 / 2.176 / **0.775** /
  2.258 — IQR high/low ≈ **1.27**, which would **fail** P-PCDP-5's "IQR
  spans ≥1.5×" bar if the slope ratios track the step ratios.

### 6. A correction to an inherited figure

The "~1.9–2.3× convention asymmetry" this cycle exists to explain does not
hold across the FWHM=20° grid. Measured `Δabs(41→81)` ratios
(`incoherent_corrected` / `incoherent`) at all nine GEOM78 cells:

| λ | 36° | 38° | 40° |
|---|---|---|---|
| 450 nm | 1.382 | 1.675 | 1.658 |
| 600 nm | 1.965 | 1.952 | 1.921 |
| 750 nm | 2.176 | **0.775** | 2.258 |

The band holds at 600 nm and at 750/36°, 750/40°; at 450 nm it is
1.38–1.68, and at 750/38° it **inverts** — `incoherent`'s step is the
larger one. At P-PCDP-4's own four named cells (750/40, 600/36, 600/40,
450/38) the step ratios are 2.258 / 1.965 / 1.921 / 1.675, median 1.943 —
4/4 inside its [1.5,3.0] band. So P-PCDP-4 is well-posed; the *inherited
prose* "reproducible ~1.9–2.3×" is the part that overstates, and §1 should
say "1.4–2.3× across the grid, ~1.9–2.3× at 600–750 nm, inverted at
750/38°" instead.
