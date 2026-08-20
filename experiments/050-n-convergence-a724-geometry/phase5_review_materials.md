# PHASE 5 — REVIEW (MATERIALS & METAMATERIALS) · Panel Iteration 27 · exp-050

*Fresh sub-agent, zero memory of Phase 1. Read `PANEL.md` in full, `LOGBOOK.md`
in full (RULED OUT R1–R4, ESTABLISHED, all LIVE THREADS including T21/T24,
PARKED, the full Iteration 26 entry), every file in
`experiments/050-n-convergence-a724-geometry/` (phase1 proposal, all five
phase2 critiques, the Red Team audit, phase3 synthesis, `NOTES.md`,
`design_geometry.py`, `run.py`, `results.json`), plus
`experiments/042-.../design_geometry.py` and
`experiments/049-.../results.json` for cross-reference. Blind to every other
seat's Phase-5 review this cycle, per PANEL.md's fresh-context rule.*

## Charter applicability — stated plainly, verified not assumed

**This cycle has essentially nothing for my charter to bound.** T1 escape
route: NONE. No material law, no σ, no structure, no optical mechanism —
`gaussian_angle_weights` samples a mathematical Gaussian kernel over
injection angle and `beam_divergence_*` re-evaluates an already-committed
analytic Huygens propagator at a different geometry dict. `grep`-confirmed:
`REALIZABILITY_MEMO.md` (`experiments/034-.../REALIZABILITY_MEMO.md`, the
only such memo in the repo) contains zero hits for `beam_divergence` or
`gaussian_angle_weights` — its tiers rest entirely on σ(I) dynamic-range/
irradiance tables and Entry 2's fixed-θ `C=−0.7209` anchor, a completely
disjoint code path from this cycle's own `beam_divergence_*` channel. This
is the identical charter-fit situation my own discipline's fresh seat found
at exp-049 (`experiments/049-.../phase2_critique_materials.md`), and I reach
the same conclusion independently: nothing here moves, or could move, an
UNOBTANIUM-WITH-PARAMETERS/plausible/published tier. I am not manufacturing
a realizability finding that isn't there.

## Verification performed — invoked, not trusted (R4 discipline)

I did not take `NOTES.md`'s numbers on faith:

- **Independently re-ran the actual committed `design_geometry.py`** (not
  Red Team's Phase-2 scratch code) for the two *non-exempt* P-NCONV27-2
  violation cells — (750nm no, 600nm/θ₀=36°, FWHM=20°,
  `incoherent_corrected`) and (600nm/θ₀=40°, FWHM=20°,
  `incoherent_corrected`) — through the full `N_SERIES` doubling at
  `g=GEOM78`. Both reproduce `results.json` **bit-exactly**: n\*=81 at both
  cells, `c41`=3.17297479...×10⁻⁴/1.77679257...×10⁻⁴ and converged value
  −3.69127956...×10⁻⁴/+7.66412853...×10⁻⁴, matching to every printed digit.
- Cross-checked exp-049's own committed `results.json` directly for the
  three FWHM=20°/`incoherent_corrected`/600nm-and-750nm rows cited in the
  Reading section — confirms the *before* state (36°/750nm: n\*=41 both
  geometries, unchanged; 40°/750nm: n\*=41→81, the pre-registered exempt
  violation; 36°/600nm and 40°/600nm: n\*=41 at A=752, →81 at A=724, the two
  unpredicted violations) is reported accurately.
- Confirmed via `git log` that `NOTES.md`'s frozen predictions
  (commit `7fa2258`, Phase 3) genuinely precede the Phase-4 implementation
  and results commits (`3139376`, `dc7170f`, `291c6dd`) — predictions were
  committed before the run, as claimed, not reconstructed after.
- Confirmed `git diff --stat HEAD -- lab/` is empty — no `lab/` file was
  touched, consistent with the "zero `lab/` file touched throughout" claim.
- Confirmed `experiments/050-.../design_geometry.py` imports exp-042's and
  exp-048's own committed functions via `importlib` rather than
  reimplementing them (read in full) — the regression-anchor design is
  structurally sound, not merely described as such.

No defect found in anything checked. The 7 CONFIRMED / 1 REFUTED / 1
CROSS-VALIDATED tally in `NOTES.md` is accurate.

## Is the Iteration-27 follow-up trigger actually closed?

**Yes, for its literal, operational purpose — with one honest caveat this
cycle's own Reading section already names correctly.**

The trigger (PLAN.md Iteration-27 queue item 1, verbatim, verified by
direct grep: `PLAN.md:1334-1341`) was never a claim that a *mechanistic
model* would predict GEOM78's convergence behavior — it was a citation-scope
guard: exp-049's A=752 n\* findings "must not be cited as governing the
A=724 fallback geometry... without this cheap re-run." That re-run now
exists, exhaustively: a full 108-row `per_cell_summary_geom78` table,
bit-exact-regression-anchored against exp-049's own committed numbers at the
old geometry. **P-NCONV27-1 (global max n\*≤81, CONFIRMED) and P-NCONV27-5
(FWHM≤10° universally converged at n=41, CONFIRMED, 100%) are the
predictions that actually answer the trigger's question** — "is n=41 safe
by default at GEOM78, and if not, how much larger does it need to be" — and
both hold. Nobody citing a GEOM78 `beam_divergence_*` value at n=41 outside
the FWHM=20°/`incoherent_corrected`-or-`coherent` regime needs to defer to a
future re-run any longer; nobody needing that regime needs to guess either,
since the exact cells and their n\* are now on record.

**What is NOT closed, and NOTES.md's own Reading section is honest about
this rather than smoothing it over**: P-NCONV27-2's own *directional
argument* — the specific mechanistic claim that a uniform period-growth
(plus, after Phase 3's amendment, a named grating-lobe-truncation
correction) exhaustively characterizes *where* GEOM78 tier-instability
occurs — is REFUTED. The exemption zone Red Team pre-registered from two
independently-converging mechanisms (Nyquist-sampling proximity,
aperture-truncation of an A-independent grating-lobe replica) correctly
caught the one cell it predicted (750nm/40°) but missed two more entirely
outside either mechanism's own domain (600nm/36° and 600nm/40°). That is a
narrower, genuinely new gap in the *predictive* story, not in the
*operational* table — and the operational table, not the predictive story,
is what the trigger asked for. I judge the trigger closed; I do not judge
the underlying convergence-risk mechanism understood.

## Does the new 600nm gap warrant a new live thread?

**No — not yet, and not at T21/T24's own weight class.** Three considerations:

1. **It is not outside any committed falsification band.** P-NCONV27-4 (the
   sibling prediction scoring `incoherent_corrected`'s own FWHM=20° failure
   count) predicted 3–7 of 9 cells fail, central estimate 5/9; the measured
   6/9 sits inside that band, only one cell above center. The *count* was
   correctly anticipated by a different, more conservative prediction in the
   same docket — only the *coordinates* (which specific cells) were
   mispredicted by the mechanistic exemption-zone story.
2. **The candidate explanation is specific and cheaply testable, not a
   standing mystery.** All three violating cells sit at `|C|`~10⁻⁴, two to
   three orders below `C_THR`, deep inside the regime where the corrected
   `delta_step` criterion's relative clause is exempted and only
   `ABS_TOL=5×10⁻⁴` — a fixed absolute number, not scaled to the local
   signal — governs convergence. That is structurally the same class of
   near-zero ill-conditioning QUANTUM OPTICS diagnosed and fixed for the
   *Δrel correlation metric* at Iteration 26; it has simply resurfaced, by
   the same underlying cause, one level down in the *n\* tier assignment*
   itself, which the Iteration-26 fix was never designed to cover. This
   reads as a testable instrument-criterion artifact, not a new
   physical/mechanistic finding about the T21 fringe.
3. **T24 and T21 opened as live threads because they threatened a
   scored, program-wide channel** (`C_empty`, the ambient-contrast
   instrument's own decision floor) with a systematic that every prior and
   future citation on that channel inherits. This gap is narrower by
   construction: it only affects `nstar` bookkeeping for `n<81` defaults at
   three specific (θ,λ) cells inside an already-flagged hard regime nobody
   was going to cite at n=41 anyway (P-NCONV27-3/4 already established the
   whole FWHM=20°/coherent-and-`incoherent_corrected` neighborhood needs
   n≥81 by default).

**Recommendation: keep this as a named, carried-forward open question
(exactly as `NOTES.md`'s Reading section already frames it) — do not open a
new T-numbered live thread until a cheap, targeted check is run and either
confirms or refutes the near-zero-ABS_TOL-artifact hypothesis.** If that
check resolves it (analogous to the Iteration-26 exemption fix), it closes
as an instrument false-positive with no thread needed. If it does not, *then*
it earns thread status on the same evidentiary footing T24 did.

## A materials-adjacent observation on P-NCONV27-6b (disclosed, not a new claim)

Outside my charter's literal scope but worth flagging since it bears on any
*future* realizability-adjacent citation near this geometry's boundary: the
program's own sharpest-stakes contamination-risk cell (750nm/38°/FWHM=2°,
`incoherent_corrected`) is n-convergence-stable at GEOM78 (P-NCONV27-6,
CONFIRMED, 0.0% move) — but its **raw value collapsed 27× and flipped sign**
between A=752 (−4.007×10⁻³, 24.8% headroom to `C_THR`) and A=724 (+1.465×10⁻⁴,
3314% headroom), a pure fringe-phase effect, not an amplitude/convergence
one (Red Team's own targeted angle-sweep check, independently reproduced in
`results.json`). This is good news at face value for any future near-±35°
contamination-risk citation at GEOM78 specifically — but idealization 6
correctly discloses that T24's own ~0.002–0.007 ABSORB-boundary systematic
was never measured at this geometry, so the 3314% headroom figure should
not be read as a validated all-clear, only as a desk-propagator reading at
one more geometry. This sharpens, rather than resolves, why the standing
LOGBOOK/PLAN.md queue item (2) — the genuine FDTD `ABSORB` sweep at the
T21-vs-T24 geometry — remains the correctly-sequenced next physically
grounded step; it is now the *only* uncharacterized uncertainty source left
on this program's own sharpest-stakes cell, n-convergence and (at this
particular geometry) fringe-phase magnitude both having just been resolved
in the same direction (favorably).

## Verdict

**PROMISING.**

Reasoning: the cycle did what it set out to do (closed the citation-scope
trigger with a full, regression-anchored table, independently
re-verified here), found a genuinely informative refutation rather than a
process defect (P-NCONV27-2, within a sibling prediction's own predicted
count-band, at coordinates a disclosed candidate mechanism can explain),
kept zero T1/REALIZABILITY_MEMO exposure exactly as designed, and left the
house-discipline gates clean (predictions frozen before the run, regression
anchor bit-exact and independently reproduced by me, zero `lab/` touched, no
hand-typed R4-risk figures found). Not RULED OUT (nothing here forecloses
anything), and not merely PARTIAL — the one refuted prediction sharpens the
program's understanding rather than leaving an unresolved mess, the same
distinction that separated exp-049's own PROMISING verdict from a PARTIAL
one at Iteration 26.

## Ranked candidate next-steps for Iteration 28

1. **[Cheapest, most directly closes this cycle's own open question]**
   Test whether a scale-relative reformulation of the `nstar`/tier
   convergence criterion near `|C|≈0` (e.g., requiring `Δabs` to also clear
   a floor tied to the local converged magnitude, not a fixed `ABS_TOL`,
   analogous to the Iteration-26 exemption fix for `Δrel`) changes the n\*
   assignment at the three violating cells. Zero new FDTD, desk-only,
   directly discriminates "genuine physical near-zero-crossing sensitivity"
   from "instrument-criterion artifact" before either gets promoted to a
   live thread.
2. **[Already ranked #3 by Red Team at Iteration 26, still correctly
   sequenced]** EM's phase-corrected difficulty-predictor test — score
   `Δrel(41→81)` against a predictor that includes each cell's phase offset
   within its own local T21 fringe period, not period-vs-Nyquist-margin
   alone. This would very likely also explain the two new 600nm misses,
   making it the single test most likely to retire both open questions at
   once.
3. **[Standing, unaffected by this cycle, now the single remaining
   uncertainty source on the program's sharpest-stakes cell]** The genuine
   FDTD `ABSORB` sweep at the T21-vs-T24 geometry (PLAN.md Iteration-27
   queue item 2) — this cycle's own P-NCONV27-6b finding (fringe-phase
   dominates, n-convergence is a non-issue) makes T24's boundary systematic
   the last unresolved piece on that cell.
4. **[Charter-relevant, MATERIALS' own lane, 9+ iterations deferred]** The
   fixed-absolute-thickness `graded_black_shell` variant remains queued and
   untouched by two consecutive instrument-fidelity cycles (49, 50) — a
   genuine materials proposal, not a mechanism-adjacent audit, is overdue
   for my own discipline's rotation slot to actually exercise its charter.
