# Phase 5 Review — PHOTONICS · Panel Iteration 83 (exp-106)

*Fresh-context seat. Charter: surface interaction, absorption spectra,
angular dependence, scattering cross-sections — is the proposal's optical
response coherent as stated, across wavelength and angle? Read PANEL.md,
LOGBOOK.md in full (R1–R23, all live threads, through Iteration 82/exp-105),
the complete exp-106 record, and exp-105's NOTES.md before writing this.
Blind to all other Phase-5 seats — none exist yet.*

## 0. Independent numeric verification

Every figure below was recomputed directly from `results.json`'s raw
fields (`kappa_windows_selfsim`, `kappa_windows_fixedabs`,
`floor_gate_window_r*`, `settling_r*`, `ledger_r*`, `p3_selfsim`,
`item4_fixedabs`, `abs_ratio`), independently of NOTES.md's prose, and
where possible against `run.py`'s own source (`window_stats`,
`floor_gate`, `floor_gate_window`, `shape_ratio_fit`, `noise_floor_flag`,
`ledger_check`).

- **Floor gates.** r=156: `n_unresolved=0/4000`, `frac_unresolved=0.0`
  (rms=5.00227, floor=0.500227). r=312: `n_unresolved=0/4000`,
  `frac_unresolved=0.0` (rms=5.00268, floor=0.500268). **Reproduces
  exactly.**
- **Settling, r=156.** self-similar: `rel_change=|0.00088187−0.00088187|`...
  recomputed directly as `|k_2x−k_1x|/|k_1x|=1.8456e-4` (tol 0.20,
  PASS). fixed-abs: `1.1484e-4` (PASS). **Reproduces exactly**, three to
  four orders of magnitude inside tolerance — a genuine landslide, not a
  marginal clear.
- **Settling, r=312.** `pass_=false`/`rel_change=null` for both
  families — confirmed this is the **cost-deferred, never-run** state
  (`r312_settling_committed=false`, `wall_312_settling_s=null`), not a
  failed test. **Reproduces exactly**, matching NOTES.md's prose.
- **shape_ratio (self-similar), recomputed from `shape_ratio_fit`'s own
  formula** `(k78−k156)/(k156−k312)`: `(0.018336958…−0.0008866624…)/
  (0.0008866624…−0.0000047930…) = 19.787847…`. **Reproduces exactly**
  (NOTES.md: 19.7878; exp-105's own committed value: 19.79, matching to
  4 s.f.).
- **shape_ratio_fixedabs**, same formula on the fixed-abs triplet:
  `(0.018336958…−0.000962183…)/(0.000962183…−0.0000090093…) =
  18.228334…`. **Reproduces exactly** (NOTES.md: 18.2283). This sits
  inside the pre-registered REFUTE band (≥14.8), reproduced independently.
- **noise_flag denominators/floors**, both families: self-similar
  `denom=k156−k312=8.81869e-4`, `noise_floor=3·0.10·|k156|=2.65999e-4`;
  fixed-abs `denom=9.53174e-4`, `noise_floor=2.88655e-4`. Both
  **reproduce exactly**, and both correctly read `noise_dominated=False`
  (`|denom| > noise_floor` by a factor of ≈3.3× in both families —
  clears the gate, but not by a wide margin).
- **abs_ratio.** r=156: `k_fixedabs/k_selfsim = 0.000962183/0.0008866624
  = 1.085174`. r=312: `0.0000090093/0.0000047930 = 1.879657`. **Both
  reproduce exactly** and both clear the pre-registered ×2.0-of-1.0 band.
- **Ledger `p_abs_frac_diff`**, recomputed from `ledger_r*`'s own
  `sigma_abs` fields (not the pre-computed field, independently):
  r=156: `|279.6607−249.0171|/249.0171 = 0.12306`. r=312:
  `|588.0218−498.4832|/498.4832 = 0.17962`. **Both reproduce exactly**
  (NOTES.md: 0.1231/0.1796).
- **abs_ext_ratio** (`sigma_abs/sigma_ext`, not previously cross-tabulated
  anywhere in NOTES.md's Result prose): self-similar r=156=**0.51804**,
  r=312=**0.51901** (flat, consistent with the fixed `R_CORE/R_COAT=0.385`
  T9 ratio); fixed-abs r=156=**0.49922**, r=312=**0.49359** (falls
  slightly as `R_CORE/R_COAT` grows 0.692→0.846). This is a genuine,
  independently-derived new observation — see §1.

Everything load-bearing this cycle claims reproduces exactly from the raw
committed fields. No arithmetic defect, no R4-class citation mismatch
found anywhere in `results.json`.

## 1. Substantive assessment — is this cycle's optical-response story coherent?

**Floor-gate: clean, but tests the wrong operand for the risk item 1 was
built to close.** I read `run.py`'s own `window_stats`/`floor_gate_window`
source directly: `kappa_window = window_stats(article)["mean"] /
window_stats(empty)["mean"]`, and `floor_gate_window()` calls
`floor_gate()` **only on the empty-scene block** — a self-referential
test (`floor = 0.10·rms` of that same block) that asks only whether the
**denominator** (the unobstructed reference field, which has no physical
reason to approach zero anywhere in this window) has internal near-null
excursions. That is exactly R13's own established convention (floor-gate
a ratio's denominator when it is the operand with plausible zero-
crossings), correctly inherited. But `kappa_window`'s actual physically
shrinking quantity is the **numerator** — the article-scene window mean,
attenuated through a `τ_shell=24` shell (`e^{-24}≈4×10⁻¹¹` direct
transmission) plus whatever near-field diffraction leaks around it — and
it is never floor-gated against an absolute solver noise level anywhere
in this cycle. Order-of-magnitude check: using `floor_gate_window_r312`'s
own empty-block `rms≈5.0` as a proxy for `window_stats(empty)["mean"]`'s
scale, the r=312 article-scene window mean is `≈k_312·5.0 ≈ 2.4×10⁻⁵`
(absolute `|Ez|²` units) — about **five orders of magnitude below** the
`0.10·rms≈0.50` threshold the empty-scene reference is held to. Nothing
in this cycle (or, so far as LOGBOOK.md records, in any prior T28 cycle)
establishes what the solver's actual absolute residual floor is on this
specific channel, so I cannot say this number IS noise-dominated — but
item 1's own stated purpose ("is P3's r=312 reading dynamic-range-limited,
or purely physical?") is **not actually answered** by a gate that only
ever inspects the reference field. The r=156 settling landslide (§0,
three to four orders of magnitude inside tolerance) is real, reassuring
evidence that `kappa_window` is a stable, reproducible quantity at that
scale — but it is silent on r=312, which is precisely where this concern
bites hardest and where no settling data exists either. This is a
structurally new variant in the R13/R14 lineage: not a denominator with
known zero-crossings (R13) and not a subtractive-cancellation numerator
(R14), but a **genuinely, physically vanishing numerator, checked against
nothing but a self-referential floor on the (safe) other operand**. I
name it here for Red Team's/the Director's own judgment on whether it
merits a forward-looking addendum; it is not, on its own, evidence the
r=312 reading is wrong — only evidence the "floor-gate PASS, clean at
both r" headline should not be read as having closed the dynamic-range
question item 1 was written to close.

**Item 4's REFUTE is honestly NOT-TRUSTED, and I can partially quantify
why that matters less — and more — than it first appears.** I
independently re-derived the algebraic identity this program already
established (exp-105 Phase 5; reconfirmed by Red Team's Phase-2 audit
here): because `x∝1/κ∝1/r` is exact-integer-scaled (`x78:x156:x312 =
4:2:1`, verified directly from `p3_selfsim`'s own `x78/x156/x312`
fields), a pure power law `κ(x)=A·x^n` makes `shape_ratio ≡ 2^n`
*exactly* by algebra — I re-derived this from scratch rather than take
it on faith. That gives implied exponents `n_selfsim = log₂(19.7878) =
4.306` and `n_fixedabs = log₂(18.2283) = 4.189` — a 2.7% relative gap
between the two families' implied exponents, much smaller than the raw
shape_ratio gap (18.23 vs 19.79, 7.9%) makes it look. Two consequences,
in tension: (a) because `κ312 ≪ κ156` in both families (≈185× and ≈107×
smaller respectively), the shape_ratio *denominator* `(κ156−κ312) ≈
κ156` to within ≈0.5–1%, so **the reported shape_ratio VALUE is nearly
insensitive to plausible-sized noise or a modest settling drift in
κ312** — the NOT-TRUSTED flag is a correctly conservative, mechanical
firing on domain geometry (Nyquist tier), not evidence the specific
number 18.2283 is fragile to the exact kind of perturbation a completed
settling leg would have revealed. (b) But this robustness is about the
*ratio arithmetic* only — it says nothing about whether κ312 itself is
real diffraction physics rather than partly numerical residue (§ above),
which the ratio's insensitivity cannot rescue. So NOT-TRUSTED is the
correct label for the right reason (unverified physical validity of
κ312), even though the specific numeral 18.2283 would very likely survive
a completed settling leg largely unchanged. One further sharpening,
independently checked: `model_A_miss`/`model_B_miss` are 0.84–0.86
(self-similar) and 0.84/0.74 (fixed-abs) — both simple functional forms
fit through the (156,312) pair miss the held-out r=78 point by 74–86%.
That means the "n≈4.2–4.3" reading is not evidence of one clean power law
governing all three points; it is a statement that the 156→312 collapse
is much steeper, relative to its own scale, than the 78→156 collapse —
an *accelerating* signal, correctly described in exp-105's own prose, but
worth stating plainly since `shape_ratio≡2^n` could otherwise be
over-read as "the whole family follows κ∝r⁻⁴·³."

**PHOTONICS' own `abs_ratio` cross-check clears its band, but at r=312
with much thinner margin than "clears its band" suggests.** `abs_ratio
(312)=1.8797` against a pre-registered `[0.5, 2.0]` band — only 6.4%
of headroom to the upper boundary (`2.0−1.8797=0.1203`), and this sits at
exactly the untested/MARGINAL leg. By contrast r=156's `abs_ratio=1.0852`
sits near the band's center. Framing both as equally "clearing the band,
independent of the settling question" (NOTES.md's own Result-section
language) is accurate as a literal boolean but undersells how close the
r=312 reading is to its own boundary, in the one leg where an unverified
settling-driven shift in either family's κ312 is most plausible.

**The 12–18% ledger divergence exceeds Red Team's own stated
interpretation rule, and the shortfall is not merely a gap — it has an
independently visible physical signature.** Red Team's Phase-2 mandatory
fix 1 specified a concrete flip rule (THERMODYNAMICS' own offered
threshold): *"if fixed-abs and self-similar's `p_abs`/`sigma_ext`
fractions land within ~10% of each other at matched r, treat item 4's
two-hypothesis framing as adequately clean; if they diverge materially,
report `shape_ratio_fixedabs`'s bands as three-way ambiguous."* The
observed divergence — 12.3% (r=156), 18.0% (r=312) — clears that ~10%
bar on both legs, yet the frozen `predictions_text`/`result_text` never
actually encodes this as a hard reclassification trigger the way
`p3_trusted`/`shape_ratio_fixedabs_trusted` are; NOTES.md's own Result
section explicitly declines to adjudicate it ("whether 12–18% is
physically sane... is not adjudicated here"). From my own seat, I can
add a genuine physical signature that sharpens this gap rather than
merely restate it: `abs_ext_ratio` itself (recomputed §0, never tabulated
cross-family in NOTES.md) sits essentially flat at ≈0.518–0.519 for
self-similar (constant `R_CORE/R_COAT=0.385`) but **falls** monotonically
from 0.499 (r=156, ratio 0.692) to 0.494 (r=312, ratio 0.846) for
fixed-abs — a small (1.1–4.9%) but directionally consistent shift toward
lower absorption / relatively more extinction-without-absorption as the
PEC core occupies a larger fraction of the coated radius. This is
exactly the qualitative signature EM's and Red Team's Attack 4/9
predicted for an untested core-reflection-leakage channel: `core_frac=0`
(clean at every cell, §0) only proves no energy is dissipated **inside**
the PEC disk — it cannot see power **specularly reflected off** the
larger, thinner-coated core into the forward window, which is precisely
what a falling `abs_ext_ratio` at fixed `τ_shell` would look like. Since
`box_dev` (the box-independence cross-check on the same `sigma_ext`
measurements) is 2+ orders of magnitude smaller than this signal at every
cell, the shift is very unlikely to be measurement noise. The ledger's
own stated purpose — establish that item 4 is a "clean two-hypothesis
discriminator" before trusting its classification — has not, on this
evidence, actually been established; a genuine third channel (core-
reflection/gradient-steepness) remains live and, if anything, has now
picked up independent circumstantial support beyond the raw
`p_abs_frac_diff` number Red Team's own audit already flagged.

## 2. Gaps, inconsistencies, and one process caution

- **Never-checked absolute floor on `kappa_window`'s numerator** (§1,
  above) — a genuinely new failure-mode shape, adjacent to but distinct
  from R13 (denominator zero-crossing) and R14 (numerator subtractive
  cancellation): a physically-vanishing numerator on a ratio whose
  denominator is, by contrast, structurally safe and gets the entire
  floor-gate's attention. Not evidence of a wrong number — evidence that
  item 1's own stated question (dynamic-range-limited vs. physical) is
  not actually closed by what this cycle built and calls the floor-gate.
- **Red Team's own mandatory-fix-1 flip rule (~10% ledger-divergence
  threshold) was not carried into the classification logic as a hard
  gate**, despite being exceeded on both legs (12.3%/18.0% > 10%). The
  gap is disclosed honestly in NOTES.md's Result section (not hidden),
  which is the discipline that has kept prior comparable gaps from firing
  Checkpoint criterion 4 in this sub-thread's history — but it means the
  reported classification string carries only the Nyquist/settling
  NOT-TRUSTED qualifier, not a second qualifier for the exceeded ledger
  threshold Red Team's own docket specifically wrote an interpretation
  rule for. I flag this for Red Team's/the Director's own ruling on
  whether it rises to the standard of a fix-docket item whose specified
  content was diluted between critique and freeze (the general shape R4's
  lineage exists to watch for, though not a verbatim match to any single
  R-rule's own trigger condition) — my charter is the physics coherence
  question this bears on (§1), not the governance ruling itself.
- **`settling_r312.{selfsim,fixedabs}.pass_=false` with `rel_change=null`
  conflates "never run" with "failed" at the `results.json` schema
  level.** NOTES.md's prose is unambiguous that this is a cost-deferred
  non-run, not a failure, so this is not a live misreading risk this
  cycle — but a future cycle reading `results.json` alone (without
  NOTES.md's caveat) could mis-cite this as "settling FAILED at r=312."
  A `null`/`"not_run"` tri-state rather than a boolean would remove the
  ambiguity at the source.
- **`abs_ratio(312)=1.8797`'s thin margin** (6.4% headroom to its own
  2.0 boundary) is not disclosed as thin anywhere in NOTES.md — only
  that the band is cleared. Given this sits at the one leg with no
  settling data and a MARGINAL Nyquist tier, the margin itself is
  information worth stating explicitly next time this metric is cited.
- No R4-class defect (a citation/figure that fails to reproduce from its
  own source) was found anywhere in this cycle's own record on
  independent re-derivation (§0) — R20's tally-of-three bar is not
  approached.

## 3. Ranked top-3 candidate directions for Iteration 84 (PHOTONICS' own view)

1. **Complete the r=312 settling leg on `kappa_window` for both
   families** — already the single highest-ranked queued item (NOTES.md
   Next/queue, Tier 1), and now doubly justified from this seat: it is
   the only leg where (a) no settling data exists at all and (b) my own
   analysis above shows the never-tested absolute-noise-floor risk on the
   article-scene numerator is most acute. Pair it, if affordable in the
   same cycle, with a genuine absolute-floor check on that numerator
   specifically (e.g. a matched-STEPS/matched-grid zero-source or
   known-quiescent capture establishing the solver's true residual level
   at this channel's scale) — closing the gap §1/§2 names, which the
   existing floor-gate's name promises but its construction does not
   deliver.
2. **Resolve the un-gated 12–18% ledger divergence, not just disclose
   it.** Either (a) formally apply Red Team's own already-written ~10%
   flip rule retroactively — reclassify item 4 as three-way ambiguous
   (thickness-law / core-reflection-leakage / both) pending further
   test, rather than leaving a REFUTE headline standing unqualified by a
   threshold Red Team's own docket specified and the data exceeded — or
   (b) run the genuine discriminating test: exp-052's own hollow-vs-PEC-
   cored delta methodology (Red Team's Attack 9, a real but cheap new
   FDTD cost, already scoped as Tier 2) on the fixed-abs family at
   r=156/312, the only test that can actually separate "core becomes
   energetically non-incidental via reflection" from "coating electrical
   thickness/gradient steepness" as the driver of the observed
   `abs_ext_ratio` shift I derived in §1.
3. **A fourth r-point (already Tier 2 in NOTES.md's queue) to break the
   two-point-fit degeneracy — but scored against the `shape_ratio≡2^n`
   identity specifically, not just as a generic robustness add.** Given
   §1's finding that `model_A_miss`/`model_B_miss` already show neither
   simple functional form predicts the held-out r=78 point well, a
   fourth point (e.g. r=234, geometrically feasible without domain
   resizing per exp-060's own precedent for intermediate r) would let a
   genuine power-law-vs-accelerating-collapse distinction be tested
   directly, rather than inferred from a two-point ratio whose "n≈4.2–4.3"
   reading — real and independently reproduced here — currently rests on
   an assumption (single clean power law) the fit-miss statistics
   themselves already argue against.
