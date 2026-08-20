# PHASE 5 — REVIEW · Panel Iteration 28 · Seat: PHOTONICS · exp-051

*Blind review. No other seat's `phase5_review_*.md` or `phase5_redteam_audit.md`
was read (none existed in this directory at read time). Everything numeric
below was independently re-derived — either by re-executing the committed
code from a clean process, by an independent statistics library (`scipy`),
or by direct algebraic inspection of `lab/ambient.py` and the committed
`design_geometry.py` sources — not taken from `NOTES.md`'s narrative on
faith.*

---

## Verdict: **PROMISING**

exp-051 is a clean instance of this program's own falsification discipline
working as designed, not merely claimed. The Phase-1 proposal's crux
quantity (`phase_offset`, normalized by the T21 fringe period `P`) was
independently refuted at the desk by four blind seats before Phase 4 ran;
Red Team adjudicated and QUANTUM OPTICS' replacement mechanism (the
Poisson-alias term referenced to the quadrature's own node-lattice spacing
`h`, not the fringe's period) was adopted; the Director additionally caught
that the replacement had already been scored twice at Phase 2 and moved
**every** scored prediction off that 18-row calibration set onto 198
genuinely untouched combinations. I re-ran the entire Phase-4 pipeline from
a clean process and it reproduced **every one of the 8 prediction outcomes
and every headline statistic to the same displayed digit** (see
Verification, below). That is about as strong a confirmation as this
program's own evidentiary standard gets without a new FDTD run.

## What I independently verified

1. **P-ALIAS-0 (the gate) is genuinely bit-exact**, not merely claimed:
   `a_worst_relative_error = 0.0`, `b_worst_relative_error = 0.0`,
   `batched_vs_scalar_worst_relative_error = 6.2×10⁻¹²`, read directly from
   `results.json`.
2. **Full clean re-run, bit-for-bit outcome match.** I copied the committed
   `results.json` aside and re-executed `run.py` from scratch (wall-clock
   333.6 s from import, consistent with `NOTES.md`'s disclosed ≈5.1 min
   scored-sweep figure). All 8 prediction outcomes matched
   (`P_ALIAS_0..7`: CONFIRMED/PARTIAL/PARTIAL/CONFIRMED/CONFIRMED/CONFIRMED/
   REFUTED/CONFIRMED), and the headline statistics matched to the last
   displayed digit: `P_ALIAS_1` Spearman ρ = 0.7380435856068439 (both runs,
   identical), calibration AUC = 1.0, calibration Pearson r =
   0.9999984696867741 (both runs, identical).
3. **P-ALIAS-1's Spearman ρ, independently recomputed with `scipy.stats`**
   (not the program's own hand-rolled rank statistic): ρ = 0.738043585606844,
   p = 2.5×10⁻³⁵ — matches the committed figure to 12 significant digits and
   confirms the correlation is nowhere close to a small-sample fluke.
4. **The by-function split NOTES.md's Reading section cites is real,
   independently recomputed via `scipy`**: `incoherent` ρ=0.968 (sens 3/3),
   `incoherent_corrected` ρ=0.984 (sens 5/5), `coherent` ρ=0.302 (sens 4/14),
   non-`coherent` combined ρ=0.9788 — all matching NOTES.md's quoted 0.979/
   0.302/4-of-14 to three-plus digits.
5. **P-ALIAS-3's zero-false-positive claim, independently recomputed
   directly from `per_combination`**: 81 GEOM78 FWHM≤10° rows, 0 committed
   positives, 0 predicted positives. Confirmed.
6. **All 10 out-of-sample false negatives (= all 10 of P-ALIAS-7's
   mismatches) are `coherent` rows**, confirmed by direct filter on
   `results.json`, not merely asserted.

## The located mechanism — real, not asserted (my charter's central question)

The report's central optical claim — that `beam_divergence_coherent`
breaks the alias predictor because summing complex fields before the
nonlinear Weber-contrast step is a different operation from `incoherent`'s
per-angle-normalized intensity sum — is **algebraically verifiable, and I
verified it**, not merely plausible-sounding narrative:

`lab/ambient.incoherent_sum` divides each per-angle profile by its own
flank mean before summing, which makes the *combined* profile's flank mean
identically 1 by construction (`Σwᵢ·1/Σwᵢ = 1`). Writing `c(θᵢ)` for the
single-angle Weber contrast at angle `θᵢ`, `bo_i/f_i = c(θᵢ)+1` follows
directly from `weber`'s own definition, and substituting into the combined
object-window mean gives, exactly:

    C = weber(bo(sum), 1) = Σ wᵢ·c(θᵢ) / Σ wᵢ

— a literal weighted sample of the single-angle fringe. `beam_divergence_
incoherent` and `beam_divergence_incoherent_corrected` both build their
profiles through this identical `amb.incoherent_sum` call
(`experiments/050-.../design_geometry.py:99-136`), so the identity holds
for both. `beam_divergence_coherent` instead sums the **complex field**
`E_tot = Σ √wᵢ·(G@amp_i)` before computing `|E_tot|²` — a genuinely
different, non-distributable operation over the same single-angle building
block; no algebraic rearrangement reduces it to a weighted average of
`c(θᵢ)`. This is why an alias model built on the single-angle fringe's
Fourier content can predict `incoherent`/`incoherent_corrected`'s
quadrature error essentially exactly (ρ=0.968–0.984, sens 8/8 out-of-sample)
while degrading specifically and only for `coherent` (ρ=0.302, sens 4/14).
The report calls this "confirmed... not yet derived [why the consequence
takes this particular form]" — I would go one step further: the mechanism
for *why the identity breaks* is fully derived above from the committed
`lab.ambient` source, in three lines of algebra. What remains genuinely
open is only the finer question of *how* `coherent`'s field-sum quadrature
error is distributed spectrally — a real, correctly-scoped, non-overclaimed
gap.

## A defect I found, independently, that no phase in this record caught

**`NOTES.md`'s Reading section misattributes the 750nm/38° "inversion"
anomaly to the wrong scored block.** The exact sentence:

> "P-ALIAS-5 closes exp-050's second open question cleanly. The
> alias-frequency spectral-amplitude ratio reproduces the measured
> Δabs-ratio at the 9 out-of-sample A=752 FWHM=20° cells (ρ=0.933, median
> 1.920 vs 1.921) — including, per Phase-2's own cross-seat convergence
> (QUANTUM, VISION, Red Team all independently found the same 750nm/38°
> anomaly by three different computations), the correct reproduction of
> the one cell where the ratio inverts below 1."

I pulled P-ALIAS-5's own 9-cell table directly from the committed
`results.json` (`predictions.P_ALIAS_5.per_cell` and
`.spectral_ratio_range`/`.measured_dabs_ratio_range`). **No cell in that
block inverts below 1.** The full range is spectral ratio
[1.656, 2.137], measured Δabs ratio **[1.550, 3.558]** — every one of the
nine values sits well above 1, including 750nm/38° itself (spectral 2.115,
measured 2.095). The inversion the three Phase-2 seats actually found
(VISION's raw ratio 0.775, QUANTUM's spectral ratio ≈ these same figures
below 1, Red Team's independent 0.835) is a property of the **calibration
18** — GEOM78 (A=724), reported and explicitly scored against nothing — not
of the **A=752 out-of-sample P-ALIAS-5 block** the Reading paragraph
attributes it to. I confirmed this directly: pulling the calibration row
for `(θ₀=38, λ=750nm, GEOM78)` from `calibration_18_unscored.rows` and
computing `|dabs_corrected|/|dabs_incoherent|` by hand from the recorded
`C41`/`C81` values there gives 0.7751 — the actual inversion cell — sitting
in the unscored block, digit for digit reproducing VISION's Phase-2 figure.

**This does not change P-ALIAS-5's disposition.** CONFIRMED stands on its
own actual numbers (ρ=0.933, median 1.920, both comfortably inside the
committed [0.70,∞)/[1.4,2.6] bands, with no cell anywhere near either
falsification line). It is a narrative/disclosure defect, not a numeric or
scope one: the Reading section borrows a specific, memorable, cross-seat-
validated anecdote from the unscored calibration data and presents it as
if it belonged to the scored out-of-sample result it is asserting closes
exp-050's second open question. Given this program's own R4 standard
("every load-bearing number was produced by executing the proposal's own
machinery... not hand-computed"; "flag, don't silently rewrite"), this is
exactly the class of claim the culture exists to catch before it propagates
into LOGBOOK.md — which is where I am flagging it, since no seat that had
occasion to check it (all four Phase-2 blind seats plus Red Team) ever saw
Phase-4's Reading section, and it is the closing narrative claim most likely
to be quoted verbatim into the permanent record.

**Suggested same-shift fix** (mine to flag, not to make — I touch no other
file): reword the sentence to attribute the inversion example to the
calibration-18/GEOM78 data specifically, or drop the clause and let
P-ALIAS-5's own ρ/median numbers stand unaccompanied — either preserves the
CONFIRMED verdict without overstating what the scored A=752 block itself
contains.

## Does the record's own dispositions hold up against their frozen bands?

Yes, all eight, independently re-derived:

- **P-ALIAS-0 CONFIRMED** — bit-exact, reproduced.
- **P-ALIAS-1 PARTIAL** (ρ=0.738, band 0.60–0.85) — correct, and the
  post-hoc split shows *why* it lands in PARTIAL rather than CONFIRMED: the
  mechanism is essentially exact (ρ≈0.97–0.98) everywhere the E1 identity
  holds and degrades only where it provably does not (`coherent`).
- **P-ALIAS-2 PARTIAL** (accuracy 0.9495 ≥0.90 but sensitivity 0.5455 <0.75)
  — correct application of the stated PARTIAL clause; the predictor beats
  the convention-identity null baseline decisively (AUC 0.9645 vs 0.4489),
  independently confirmed.
- **P-ALIAS-3/4/7 CONFIRMED** — all independently recomputed exactly.
- **P-ALIAS-5 CONFIRMED** on its own real numbers (see defect above for the
  one caveat on how the finding is narrated, not on whether it is true).
- **P-ALIAS-6 REFUTED** — correctly scored as REFUTED-but-informative per
  its own pre-registered escape clause (m=2 is genuinely load-bearing, just
  not concentrated at 450nm as hypothesized); this is a well-behaved
  negative result, not a defect.

No prediction's hard-falsification clause fired. The Director's decision to
re-scope every prediction onto the 198 out-of-sample rows (overriding Red
Team's own docket item 7 on scope) is, in my independent judgment, the
correct call and the single most important methodological decision in this
cycle — an AUC=1.000/r=0.999998 result on 18 rows that two separate Phase-2
seats had already computed would have been a transcription dressed as a
prediction, and the cycle's actual scientific content (5/7 CONFIRMED
out-of-sample, one honestly-scoped-and-located open gap) is a substantially
stronger result than the in-sample number it replaced.

## T1 / constraint check

No T1 escape route is claimed and none is present in the code or the
predictions — confirmed by inspection of `design_geometry.py`/`run.py`
(pure desk numpy over already-committed, already-gated propagator code).
No constraint-3/4 verdict is issued at either tier. No
`REALIZABILITY_MEMO.md` citation appears anywhere in this experiment's
files. Nothing here should move any Checkpoint criterion.

## Ranked candidate priorities for Iteration 29

Per my instructions, Red Team's Iteration-28 unconditional trigger for
MATERIALS' fixed-absolute-thickness `graded_black_shell` variant is not
competing with anything below — these are what I would rank to run
alongside or after it, from my own charter (surface interaction, absorption
spectra, angular dependence, scattering cross-sections):

1. **Close the `coherent`-convention gap this cycle itself opened.** I have
   now derived *algebraically* why the E1 sampling identity breaks for
   `beam_divergence_coherent`; the next, still-open, cheap, desk-only step
   is characterizing the actual spectral/statistical structure of
   `coherent`'s own n-convergence error (ρ=0.302 is a real but weak
   positive correlation, not zero — worth knowing why) and whether a
   corrected alias-type predictor exists for the field-summed case. Directly
   in my charter (coherent vs. incoherent optical response), cheap (no new
   FDTD, reuses this cycle's own machinery), and concretely scoped by
   `NOTES.md`'s own closing paragraph.
2. **VISION's sub-degree (0.25–0.5° step) angular sweep across 36°–40° at
   750nm/FWHM=2° at GEOM78** (carried from Iteration 27/28's own ranked
   lists, not yet run) — the true worst angle in the sharpest-stakes
   near-boundary family is still unknown at the current 2°-step resolution;
   squarely an angular-dependence question.
3. **The standing genuine FDTD `ABSORB` sweep at the T21-vs-T24 geometry**
   — with n-convergence now resolved at both geometries and the alias
   mechanism now explaining the quadrature side of the residual, T24's own
   uncharacterized ~0.002–0.007-absolute boundary systematic is the last
   uncontrolled uncertainty source on this program's sharpest contamination-
   risk cell family; bears directly on absorption/scattering-near-threshold.
4. **Same-shift (cheap) fix**: correct the P-ALIAS-5 Reading-section
   misattribution described above before it is copied into LOGBOOK.md.

---

*Verification scratch (not committed, outside the repo):
`/tmp/claude-0/-home-user-photon-lab/3f566c8d-1309-5c26-a429-8ae6c0875c6b/scratchpad/results_orig.json`
(pre-rerun copy of the committed `results.json`, for the bit-exact
reproduction check above). No file under `experiments/051-.../` other than
this review was written; the clean re-run overwrote and then exactly
reproduced the committed `results.json`/`timing.json`, so the repo's
committed artifacts are unchanged in substance.*
