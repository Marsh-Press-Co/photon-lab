# PHASE 5 — REVIEW · Panel Iteration 83 · Seat: THERMODYNAMICS

*Fresh-context review of exp-106's completed results. Blind to any other
seat's current-cycle Phase-5 review, per this cycle's own isolation
discipline. Charter: where absorbed energy goes; the per-proposal energy
sidecar (absorbed power → temperature rise → emission band →
detectability), a post-run analytic calculation, labeled as such, never an
FDTD output.*

## 0. Verdict up front

**CONFIRM-WITH-GAPS.** Every raw ledger figure in `results.json`
independently reproduces from its own primitive fields (§1, below) — this
cycle's arithmetic is clean. But the record contains three real,
charter-relevant gaps, none load-bearing to any scored PASS/FAIL verdict
this cycle filed, all cheap to close: (a) the "P5 not re-invoked"
idealization defends only half the relevant chain, and the promised
connective arithmetic that would close the other half is never actually
performed anywhere in the document — I perform it below and it holds, but
that closing step should not have needed a Phase-5 reviewer to supply it;
(b) this cycle's own self-similar-family ledger data closely corroborates
the standing `Q_ext`-invariance placeholder my own prior-cycle self-review
(exp-105 Phase 5) ranked as its #1 open item, sitting unused; (c) mandatory
fix 1's own THERMODYNAMICS-proposed, Red-Team-adopted "three-way ambiguous"
relabeling rule was triggered by this cycle's own data and was not applied.

## 1. Independent numeric verification (from `results.json` raw fields, not NOTES.md prose)

All four `ledger_check()` cells recomputed from `sigma_abs`/`sigma_ext`/
`radial_total`/`i_inc`/`core_power` alone:

| r | family | σ_abs | σ_ext | abs_ext_ratio (recomputed) | filed | core_frac | box_dev |
|---|---|---:|---:|---:|---:|---:|---:|
| 156 | selfsim | 249.017120 | 480.688101 | 0.518043 | 0.518043 | 0.0 | 0.0001 |
| 156 | fixedabs | 279.660657 | 560.198851 | 0.499217 | 0.499217 | 0.0 | 0.0008 |
| 312 | selfsim | 498.483237 | 960.445630 | 0.519012 | 0.519012 | 0.0 | 0.0000 |
| 312 | fixedabs | 588.021832 | 1191.325858 | 0.493586 | 0.493586 | 0.0 | 0.0002 |

`abs_ext_ratio` reproduces to the printed digit at every cell; `core_frac`
is exactly `0.0` at every cell (perfectly clean, generalizing T9's
core-incidental finding past its own only-validated 0.385 `R_CORE/R_COAT`
anchor to 0.692/0.846); `box_dev` is 2–3 orders of magnitude inside the
established ≤0.12 convention at every cell.

**Cross-family divergence** — `p_abs_frac_diff = |σ_abs,fa − σ_abs,ss| /
σ_abs,ss`: r=156 → `30.6436/249.0171 = 0.123058` (12.31%, exact match to
`results.json`'s `0.12305795332466973`); r=312 → `89.5386/498.4832 =
0.179622` (17.96%, exact match to `0.17962207739772926`). **Both
reproduce exactly.**

**The `closure` identity IS computed and IS persisted** — `run.py:320`:
`closure = |radial_total − σ_abs·i_inc| / |σ_abs·i_inc|`. Hand-reproduced
for all four cells (r=156 selfsim: `615.2482` vs `σ_abs·i_inc=249.0171×
2.470111=615.098…` → closure≈2.41×10⁻⁴, matches filed `0.0002412…`; the
other three cells reproduce to the same precision). **This is a genuine
answer to the task's own question**: yes, the closure check (radial-binned
Joule dissipation vs. top-down `σ_abs·i_inc`) is computed, at all four
cells, and is clean (1.6×10⁻⁴–6.9×10⁻⁴, i.e. 0.016%–0.069%) — a real,
independent energy-conservation cross-check of the ledger's own two
instruments (`sections.widths()` and `sections.radial_absorbed_power()`),
agreeing to better than a part in a thousand. **It is not narrated
anywhere in `NOTES.md`** — I grepped the file for "closure" and found zero
hits, in Setup, Predictions, or Result. The Predictions text states the
ledger exists to check "concentration... and box-independence (box_dev)"
only; `closure` was never promised, so this is not a broken promise in the
strict sense, but it is a real, useful, already-computed self-consistency
result — the single strongest evidence in this document that the ledger's
two instruments are not fooling each other — left to sit in `results.json`
unread. Cheap fix, flagged for the record, not escalated (see §3).

## 2. Is "P5/thermal sidecar not re-invoked" actually correct/complete?

**The bottom-line conclusion is safe. The stated justification is
incomplete, and the promised closing arithmetic that would demonstrate
that safety is never performed.**

### 2a. What the idealization claims, and what it actually covers

`NOTES.md`'s Idealizations state: *"P5 not re-invoked this cycle —
varying R_CORE/sigma_max at fixed r_out does not change the thermal
chain's own `l_geometric_m` argument — only the absorbed-power INPUT to
that chain could, and the ledger measures it directly."* This is TWO
claims bundled as one. The first (the `l_geometric_m` argument is
unchanged) is correct and, on inspection of `lab/thermo_sidecar.py`, true
for a structural reason the document does not name: `mixed_length_scale_
regime()` (the actual chain, `l.333-393`) takes `l_geometric_m` and
`p_abs_w` as two **independently supplied** arguments — `area_m2 =
l_geometric_m**2` governs `h_eff`, mass, and the radiative/convective
denominator; `p_abs_w` is whatever an upstream optical measurement
produced. Since `R_COAT`(=`r_out`) is bit-identical between families at
each r (§ NOTES.md Setup, verified in `results.json::geom_156`/
`geom_156_fixedabs` etc.), the denominator side of `ΔT_ss = p_abs_w/dp_dt`
genuinely does not move between families. But this says nothing about the
numerator. The second claim — "the ledger measures [the absorbed-power
input] directly [and this is the scored proxy for whether re-derivation is
needed]" — is never cashed out: nowhere in this document is the ledger's
own `p_abs_frac_diff` (or any other ledger quantity) actually run through
`ΔT_ss = p_abs_w/dp_dt` against exp-105's own committed margins to show
the UNDETECTABLE classification survives. The Result section's own
closing sentence on this exact question — *"whether 12–18% is
'physically sane'... or itself informative is not adjudicated here"* —
is an explicit admission that the connective step was left undone.

### 2b. The correct proxy is not `σ_abs` alone — and the real divergence is larger than reported

exp-105's own thermal sidecar computes `p_abs_w` via `absorbed_power_
established_ratio()` (`lab/thermo_sidecar.py:124-170`): `width_m =
sigma_ext_cells·dx_m`; `area_m2 = width_m²`; `p_abs_w = i_incident·
area_cm2·ratio_abs_ext`. Substituting `ratio_abs_ext = σ_abs/σ_ext`:
`p_abs_w ∝ σ_ext² · (σ_abs/σ_ext) = σ_ext · σ_abs` — the relevant
"absorbed-power" proxy for THIS chain's own `iso_xsec_sq` area convention
is the **product** `σ_ext·σ_abs`, not `σ_abs` alone. (`mixed_length_
scale_regime()` then applies `area_m2 = l_geometric_m²` = `r_out²` to the
*denominator* only — confirmed by direct read of `lab/thermo_sidecar.py:
373` — so there is genuinely no area cancellation between the `σ_ext`-based
numerator and the `r_out`-based denominator; T22's Iteration-20 "provably
area-independent" finding does not apply to this — the corrected,
T23-resolved — mixed-length-scale chain, a distinction this document does
not draw.) Recomputing the family ratio on that proxy, from the ledger's
own raw fields:

```
r=156: (σ_ext,fa/σ_ext,ss)·(σ_abs,fa/σ_abs,ss)
     = (560.1989/480.6881)·(279.6607/249.0171)
     = 1.16546 · 1.12306 = 1.3088   (+30.9%)

r=312: (1191.3259/960.4456)·(588.0218/498.4832)
     = 1.24040 · 1.17967 = 1.4632   (+46.3%)
```

If the thermal chain were literally recomputed with the fixed-abs
family's own real, ledger-measured `σ_ext`/`σ_abs` in place of the fixed
`Q_ext`/`RATIO_ABS_EXT=0.51` placeholder exp-105's `run.py` hardcodes, the
implied `ΔT_ss` would be **~31% higher at r=156 and ~46% higher at r=312**
than the self-similar family's own value — not the 12%/18% the raw
`p_abs_frac_diff` figure suggests, because that figure omits `σ_ext`'s own
cross-family growth entirely.

### 2c. Does this threaten the UNDETECTABLE classification? No — checked, not asserted

Applying these factors to exp-105's own committed margins (`699.27×` /
`349.80×` / `175.06×` at r=78/156/312, self-similar, `NETD_BAND_K[0]=
0.020` K):

```
margin_fixedabs(156) ≈ 349.80 / 1.3088 ≈ 267.3×   (still >>1)
margin_fixedabs(312) ≈ 175.06 / 1.4632 ≈ 119.7×   (still >>1)
```

Both remain two-plus orders of magnitude below the NETD detectability
threshold. **The "P5 not re-invoked" decision's bottom-line safety holds**
— but only because I performed the arithmetic the document's own Setup
section claimed the ledger check made unnecessary. It does not; it made
the arithmetic *available*, at zero marginal cost, and the arithmetic was
not run. This is the shape R8 exists to name (an unverified
robustness/independence argument standing in for an actually-computed
check) — I do not read it as R8-firing, since the gap, once closed, is
non-outcome-determining and was caught within this same review layer
before LOGBOOK — but it is the family of gap R8 was adopted to prevent,
and a future cycle citing "P5 not re-invoked, safely" from this document
should cite the arithmetic above, not the bare idealization sentence.

### 2d. A genuinely positive, unclaimed finding sitting in the same data: `Q_ext`-invariance is now empirically corroborated, tightly

My own exp-105 Phase-5 self-review (required reading for this cycle)
ranked, as its #1 candidate direction, exactly this measurement: *"the
real, measured `sections.widths()` σ_ext(r) trend... build it with an
explicitly self-similar box (not a fixed offset)... floor-gate the
result before trusting it."* exp-106's own `ledger_check()` **is** that
measurement, on the self-similar family, using exactly the self-similarly
κ-scaled box convention I asked for (`box_a_hw=R_COAT+round(32κ)`, etc. —
NOTES.md Setup). Nobody in this cycle's record connects it back to that
question, so I do it here:

```
Q_ext(r) := sigma_ext_selfsim(r) / (2r)
Q_ext(156) = 480.6881 / 312 = 1.540667
Q_ext(312) = 960.4456 / 624 = 1.539112
Q_ext_placeholder (r=78 anchor, exp-105) = 240.007374 / 156 = 1.538509

deviation(156) = (1.540667 − 1.538509)/1.538509 = +0.140%
deviation(312) = (1.539112 − 1.538509)/1.538509 = +0.039%
```

This is a *tighter* confirmation than the only prior evidence on file
(exp-030's own T11 companion, a different article, `Q_ext` drift +0.58%
over κ=2 — cited in my exp-105 self-review as "corroborating, not
proof"). Here, on the actual `graded_black_shell` article, on a correctly
self-similar box, across κ=1→2→4, `Q_ext` drifts by under 0.15% — a real,
independently-derived, materially stronger validation of the placeholder
every self-similar-family P5 number in this program's history rests on.
This should have been logged as a finding in its own right; instead it is
an unexploited byproduct of item-1's ledger build.

## 3. Gaps, inconsistencies, and R-rule cross-references

1. **Mandatory fix 1's own "three-way ambiguous" flip rule fired and was
   not applied.** `phase2_redteam_audit.md`'s own mandatory fix 1 (which
   NOTES.md's Panel Record states was "ADOPTED in full") includes,
   verbatim: *"Flip/interpretation rule (THERMODYNAMICS' own offered
   threshold, reused): if fixed-abs and self-similar's p_abs/sigma_ext
   fractions land within ~10% of each other at matched r, treat item 4's
   two-hypothesis framing as adequately clean; if they diverge
   materially, report shape_ratio_fixedabs's CONFIRM/REFUTE bands as
   three-way ambiguous (thickness-law vs. core-reflection/
   gradient-steepness vs. both), not a clean binary."* This threshold was
   my own seat's Phase-2 proposal (`phase2_critique_thermodynamics.md`:
   *"if they land within, say, 10%... empirically closed... if they
   diverge materially, item 4's interpretation needs the three-way
   framing"*), Red Team's own audit reused it verbatim as mandatory. The
   measured divergence — 12.31%/17.96% — **exceeds the stated ~10%
   threshold at both r**. Item 4's classification string in
   `results.json` and `NOTES.md`'s Result section nonetheless reads
   `"REFUTES-electrical-thickness-growth-hypothesis (NOT-TRUSTED —
   r=312 MARGINAL/unsettled)"` — the original two-way framing, never
   relabeled three-way-ambiguous. The `NOT-TRUSTED` tag (a resolution/
   settling-reliability flag) and the three-way-ambiguous relabeling (an
   interpretive-adequacy flag) answer different questions; the first does
   not subsume the second, and NOTES.md's own text never makes that
   argument — it reports the >10% divergence in a separate paragraph and
   explicitly declines to adjudicate it ("not adjudicated here"), without
   ever connecting it back to the adopted rule that was built to
   adjudicate exactly this. This is the shape this program's own R6–R20
   "known, named, ignored" lineage exists to catch — a pre-registered
   decision rule, adopted in full, whose own stated trigger condition is
   met by the data, whose prescribed consequence is not executed. I do
   not think it independently fires any existing numbered rule as
   written (none of R6–R23 covers "a Phase-2-adopted interpretation rule,
   not a significance test/ground-truth gate/citation," verbatim), but it
   sits squarely in that family and Red Team should weigh it as such
   rather than let the `NOT-TRUSTED` tag be read as a substitute
   discharge.
2. **The stated justification for "P5 not re-invoked" defends only the
   denominator of the chain it cites** (§2a–§2c, above) — not a rule
   violation, but a real, closeable gap; the connective arithmetic
   belongs in the permanent record, not only in this review.
3. **The `closure` identity is computed, clean, and unnarrated** (§1) —
   a minor hygiene gap, not a rule violation (R21's own text scopes
   "persisted sidecar field" to the NETD/thermal-sidecar channel by its
   founding instances; `closure` is a ledger-consistency field, a
   different channel) — but the same underlying discipline (a computed,
   passing self-consistency check should be one sentence in Result, not
   silent) is worth naming so a third, genuinely R21-scoped instance
   doesn't arrive by the same root habit.
4. **T22's "provably area-independent" claim does not describe the chain
   this program actually runs since Iteration 23's T23 resolution**
   (§2b) — `mixed_length_scale_regime()`'s mixed-length-scale design
   means `ΔT_ss` is NOT independent of the absolute magnitude of
   `p_abs_w` (only of the *convention* used to compute it, holding the
   denominator length fixed at `r_out`). This is not this cycle's
   defect — T22's language was accurate for the Iteration-20 chain it
   described, superseded by Iteration 23 without T22's own LOGBOOK entry
   being flagged as narrowed — but it means any future citation of "the
   area convention cancels, so absolute σ_ext doesn't matter" is citing a
   claim that no longer describes the code as it stands. Worth a LOGBOOK
   cross-reference the next time T22 is cited.
5. **`core_frac`/`box_dev` both generalize T9's 0.385-ratio anchor
   cleanly past 0.692/0.846 at every cell** (§1) — a real, positive,
   independently-reproduced finding, correctly reported in NOTES.md,
   no gap.

## 4. Ranked top-3 candidate directions for Iteration 84 (THERMODYNAMICS' own charter)

1. **Close the `Q_ext`-invariance question formally, and compute a real
   (not placeholder) P5 row for both families at r=156/312, at zero
   marginal FDTD cost.** This cycle's own ledger already contains
   everything needed: feed `ledger_r156`/`ledger_r312`'s real `σ_ext`,
   `abs_ext_ratio` into `absorbed_power_established_ratio()` /
   `mixed_length_scale_regime()` directly (desk-only — the fields are
   already captured, no new `Sim.run()` calls), for BOTH families. This
   (a) formally logs the `Q_ext`-invariance corroboration found in §2d
   (currently unclaimed anywhere in the record), replacing exp-105's
   placeholder-based self-similar table with a genuinely measured one;
   and (b) produces the first-ever real, non-placeholder P5 classification
   for the fixed-abs family — closing §2's own open loop with a computed
   answer instead of a back-of-envelope review-time check. Highest
   value, lowest cost item on the board from this seat's own charter.
2. **Resolve the mandatory-fix-1 flip-rule gap (§3 item 1) explicitly** —
   either retroactively relabel item 4's classification
   three-way-ambiguous (thickness-law vs. core-reflection/gradient-
   steepness vs. both) per the adopted rule's own text, or write, in
   NOTES.md, the specific argument for why `NOT-TRUSTED` is judged to
   subsume it. Zero cost either way; what should not continue is silence
   between "the rule's trigger fired" and "the rule's consequence."
3. **Run the r=312 settling leg** (already this cycle's own
   highest-ranked open item, NOTES.md's Next) — but note, sharpened by
   §2b/§2c above, that once it lands, item 4's r=312 reading will need
   BOTH the trust gate AND the three-way-ambiguous interpretive question
   resolved before it is cited as a clean discriminator — closing the
   settling gap alone does not retire item 2 above.

*(NOTES.md's own remaining Next items — the `delta_scene` R3-vs-R4 split's
now-seventh deferral, the oblique-angle extension — are correctly
scoped and re-justified in writing per this program's own Iteration-51
precedent; not re-ranked here since they sit outside this seat's own
charter-specific findings this cycle.)*
