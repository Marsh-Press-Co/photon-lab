# Phase 5 Review — ELECTROMAGNETISM (Panel Iteration 77, exp-100)

## Verdict: **CONCUR-WITH-GAP(S)**

The two load-bearing EM-discipline claims in this cycle's Result section —
(1) that `observer_record_t28`'s fix (RT-4/EM's own mandated unmirrored-call
+ scalar-relabel construction) was implemented correctly and its clean
empty-scene validation is real evidence, not an artifact of a different bug;
and (2) that `beam_behind_t28`'s anomalous 0.42–0.46 readings are fully
explained by a fixed-window/oblique-incidence lateral-shift defect, not some
additional undiagnosed energy-bookkeeping problem — both **independently
verify from primitives**, not merely from NOTES.md's own prose. The gaps
below are disclosure/completeness items and one forward-looking risk, none
of which change either finding.

---

## 1. `observer_record_t28` — fix correctly implemented, independently re-derived

Re-read `run.py:472-490` against `lab/emit.py:80-127`, without relying on
NOTES.md's or my own Phase-2 critique's prose.

**The fix as shipped matches the mandated construction exactly**: no array
mirror anywhere in `observer_record_t28`. It calls
`emit.observer_record(sim_scaffold, capture_tuple, plane_x_obs(cfg),
reference=None)` unmirrored, then labels `aux["p_forward_total"]` (the `a+`,
+x-traveling component) as `p_observer_raw` and `aux["p_backward_total"]`
(the `a-`, -x-traveling component) as `p_incident_raw` — the pure
scalar-relabeling fix Phase 2's RT-4 specified, with no field-array edits.
This is the correct labeling for this bench's reversed geometry
(`src_x > obj_x > plane_x_obs`, source launching the -x/`a-` wave): the
injected beam *is* `a-`, so the quantity traveling back toward the observer
(+x, toward high-x) is `a+` — exactly what the code reads.

**A place a regression of the identical defect class could have crept back
in, checked and found clean**: `emit.observer_record`'s own `reference=`
kwarg, if used naively, normalizes the angle-binned flux by
`reference["p_forward_total"]` — correct for `emit.py`'s own assumed
low-x/+x-source geometry, but for exp-100's reversed bench that would divide
by the *tiny* returned-signal total instead of the injected-beam total,
reproducing RT-4's exact failure mode one level downstream, inside the
"already-fixed" code path. The implementation avoids this: it passes
`reference=None` and performs its own direction-corrected normalization by
hand (`obs_article["p_observer_raw"] / obs_empty["p_incident_raw"]`, i.e.
against the empty capture's own `p_backward_total` — the injected beam's own
power). Confirmed this is also the physically correct choice on a second
count: normalizing the article-loaded reading against the *article* run's
own `p_incident_raw` would contaminate the denominator with whatever small
fraction of back-reflected light has already propagated upstream past
`plane_x_obs` by the time of capture; using the empty-scene reference's own
`p_incident_raw` avoids that contamination, matching `emit.py`'s own
documented `"vacuum_run"` intent even though the built-in kwarg path itself
was correctly bypassed.

**Does the small self-ratio (1.1×10⁻⁴–3.9×10⁻⁴, all 6 angles) make physical
sense as confirmation, or could a different bug produce a similarly small,
misleadingly reassuring number? Confirmed: it is real, discriminating
evidence, not a coincidence.** Three independent checks, all run against
`results.json` directly:

1. **Magnitude sanity.** The denominators (`p_incident_raw`, read from
   `beam_behind_empty_*` as an independent cross-check on overall field
   scale) are ~100–116 grid-power units at every angle — large, non-
   degenerate numbers, not a 0/0 near-cancellation. The self-ratio is small
   because the numerator (`p_observer_raw`, e.g. 1.6×10⁻⁴–3.9×10⁻⁴ raw) is
   genuinely small relative to a healthy, correctly-scaled incident total —
   not because both sides underflowed together.
2. **Directional determinism.** The label swap is not a coin flip that could
   have landed either way and still looked plausible: swapping it the
   *wrong* direction (reading the huge `a-` total as "observer," the near-
   zero `a+` total as "incident") would produce a self-ratio near infinity,
   not near zero — this R18 gate (`<0.02`) is a genuinely discriminating
   test of the swap direction, not a bar low enough for any bug to clear.
3. **Trend consistency.** The empty self-ratio climbs mildly and
   monotonically with θ (`C40_R4`: 2.27×10⁻⁴ → 3.87×10⁻⁴ across the 6
   angles) — matching this program's own established finding that the
   camera-floor scale rises with angle (T16/T21), not a flat or erratic
   pattern that would suggest a degenerate computation.

**Conclusion: constraint-2 (specular return) PASS stands, independently
confirmed from primitives, no dispute.**

## 2. `beam_behind_t28` — the lateral-shift diagnosis is quantitatively correct and complete; no separate normalization defect found

Re-derived NOTES.md's own Δy = (R_OUT+10)·tanθ claim independently from
`lab/fdtd2d.py`'s documented source convention (`add_line_source`'s
docstring: *"The −x-going wave then travels along (−cosθ, +sinθ): for
positive θ it walks toward +y..."*) and `design_geometry.py`'s own
`R4_R_OUT=156` (`experiments/069-.../design_geometry.py:257`), independent
of the Idealization text:

| θ (deg) | computed Δy (166·tanθ, cells) | NOTES.md's claimed range |
|---|---|---|
| 37.127246 | 125.67 | 125.7 (low end) |
| 38.590230 | 132.47 | — |
| 40.265420 | 140.61 | — |
| 40.960901 | 144.10 | — |
| 41.460901 | 146.66 | — |
| 42.960901 | 154.59 | 154.6 (high end) |

This reproduces NOTES.md's cited 125.7–154.6 cell range to the stated
precision, computed independently, not copied. Against
`BEAM_BEHIND_HALF_WIDTH=160` (`dg.REF_HALF_H_R4`, itself `≈R4_R_OUT`, i.e. a
window sized to the object's own shadow, not the full illuminated
aperture), the true shadow center has walked 79%–97% of the window's own
half-width away from where the window is centered — most of the window at
the larger angles is sampling *un-shadowed* flux beside the true, displaced
shadow, exactly the "reads mostly un-shadowed flux... would show as a HIGH
ratio" mechanism NOTES.md names. The monotonic climb in the measured ratio
with θ (0.4156→0.4589 for `C40_R4`) tracks the monotonic climb in Δy(θ)
exactly as this mechanism predicts — an independent, quantitative
corroboration beyond the qualitative story.

**Is there an additional energy/normalization issue beyond the pure
geometric miscentering? Checked, and found: no.** `beam_behind_t28`'s ratio
(`sum(-flux_profile_x(...))`, scene ÷ empty, same fixed window both times)
is a self-normalizing quantity — no separate incident-intensity
normalization step exists to get wrong, unlike `sections.widths()`'s
`sigma_*` channels (which divide by a separately-measured `i_inc`). Read
against `lab/sections.py:79-88` (`flux_profile_x`, a straightforward
per-cell `<Sx>` sum, same gate-proven phasor conventions `_face_flux` uses)
there is no unit mismatch, no hidden double-counting, and no sign-
cancellation pathology large enough to explain the observed magnitude: the
window-shift mechanism alone, sized correctly against `R4_R_OUT` and the
documented propagation angle, is fully sufficient to produce readings in
the 0.42–0.46 range instead of the established 0.015–0.018. NOTES.md's own
characterization — *"unable to compare because the shadow lies outside the
fixed window"* — is the physically correct diagnosis, not an
undersell of a worse or differently-shaped defect; if anything it slightly
undersells how close to total the miscentering is (Δy reaches 96.6% of the
window half-width at the largest tested angle).

**Conclusion: constraint-1 (beam termination) result is correctly reported
as UNINTERPRETABLE-PENDING-WINDOW-CORRECTION, not a real transmission
finding — confirmed independently, no dispute.** This is a genuine,
first-time defect in a newly-built instrument, not a repeat of the
`observer_record_t28` defect class (that one already inherited a robust,
whole-domain-FFT construction "for free"; this one is a new fixed-window
extraction that never had angle-robustness built in) — Idealization/
Learned-item framing on this point is accurate.

## 3. Minor gaps (non-blocking, do not change the verdict)

1. **NETD/thermal-sidecar data is persisted but never narrated.** Fix 7's
   literal mandate (`netd_row()` called on all 6 pairs, persisted, asserted
   present) is satisfied exactly — confirmed directly:
   `dt_ss_full_K_{c,g}`/`netd_classification_{c,g}` are present in all 6
   report rows, and all 12 classifications read `UNDETECTABLE` (consistent
   with every prior R4-family cell on file). But NOTES.md's own Result/
   Learned sections never state this finding in prose — a completeness gap,
   not a persistence gap (R16 concerns persistence specifically, and R16 is
   cleanly satisfied here; this is a lesser, one-line backfill for
   Iteration 78, not a fresh rule-relevant defect).
2. **RT-1's fix is a real improvement but still a partial one, as
   Idealization 68 itself discloses.** Leg B's two added angles are the
   largest *already-filed* `delta_scene` values in this window, not a
   located true extremum — the genuine local extremum near θ≈41.5°–42°
   (exp-099's own "bounce" finding) and whatever lies beyond 42.960901°
   (where exp-099's own span was still climbing) remain untested. Once
   Tier 0's window fix lands, a genuinely located extremum should be
   targeted before Leg B's constraint-1 reading is treated as covering
   `delta_scene`'s actual worst case, not just its worst *already-measured*
   case.
3. **Loose citation of "R18" for the empty-scene validation gate**
   (`phase1_proposal.md`/NOTES.md fix 4's Setup text). R18's actual text
   concerns a check's documented scope vs. its source code and
   fault-injection controls for a check joining an already-verified layered
   architecture — a defensible but imprecise fit for "validate a new
   instrument against a known floor before trusting it downstream," which
   is closer in spirit to this program's general R6/R8 validate-before-
   trust lineage. Non-load-bearing (the gate itself is correctly designed
   and correctly cleared regardless of which rule number labels it), flagged
   only for citation hygiene.

## 4. Ranked top-3 candidate directions for Iteration 78

**1. Fix `beam_behind_t28` — and, from this seat's own discipline, prefer
the closed-box reconstruction over a per-angle re-centering formula.**
This is unconditionally first: it is the one open item squarely inside this
seat's own charter (constraint-1 bookkeeping), and this cycle's own
Combined Verdict already labels the current reading UNINTERPRETABLE.
Recommendation, with reasons:
   - **Prefer the closed-box (4-face Poynting) reconstruction**, mirroring
     `cell_metrics_r4`/`sections.widths()`'s already-gated, fault-injection-
     verified machinery, over a `y_center = obj_y + Δx·tanθ` window
     correction, for three reasons: (a) it needs no new trigonometric
     correction to derive or verify at all — eliminating, by construction,
     the exact defect class that has now hit this one instrument family
     *twice in the same cycle* (first `observer_record_t28`'s missing Hy
     sign flip, now `beam_behind_t28`'s missing angle correction); a third
     instance of an unverified geometric/directional correction in this
     same new-instrument family, if it recurred, would be a serious,
     R18-adjacent pattern worth escalating explicitly. (b) It reuses
     machinery already validated across ~15+ T28 cycles and already
     fault-injection-tested (Checks 1–7), rather than a fresh, single-cycle-
     old formula with zero independent verification history. (c) The exact
     same 24 captures already computed `sigma_ext_cells`/`p_abs_w` this
     cycle (visible in `results.json` now) — a box-based "fraction of the
     beam surviving past the object" figure is derivable at **zero marginal
     FDTD cost** from data already on file, and can be cross-checked for
     free against whatever `beam_behind` reading Iteration 78 produces.
   - **If a window-recentering fix is chosen instead** (e.g. to preserve
     direct comparability with exp-001's own literal downstream-line
     definition and the established 1.5–1.8% benchmark it was measured
     against), it must not repeat the pattern that has now hit this
     instrument family twice in one cycle: require (i) the corrected center
     independently re-derived from `fdtd2d.py`'s own convention by a second
     seat, not copied from this document's own Next-section formula
     unchecked; (ii) a positive control confirming the correction reduces
     to the current (presumably-correct) reading at the smallest tested
     angle; (iii) a cross-check of the corrected ratio, at all 6 angles,
     against the already-computed, already-trusted `sigma_ext_cells`/
     `p_abs_w` channel from the same captures — free, and the one check
     that would catch a second sign/offset error in the new formula before
     it becomes this sub-thread's third instance of this exact defect
     shape.

**2. Resolve the R3-vs-R4 family-stratified contradiction in Tier 1 item 1
before either reading is treated as settled.** The pooled correlation
narrowly misses the joint rule (p=0.0758) while R3 alone clears it cleanly
(r=0.486, p=0.0042, n=33) and R4 — the larger, most-exercised family — does
not (r=0.110, p=0.525, n=35). Per R15's own addendum discipline, a genuine
article×PAD cross-term should recur across resolution families; a
family-specific-only signal is itself evidence of a resolution-specific
recipe artifact, not of new physics. This bears directly on this program's
own energy-bookkeeping question (is there any genuine article-coupled
content in `delta_scene` at all): worth a small, targeted R3-only follow-up
(NOTES.md's own Next section already proposes this) before either "genuine
coupling at R3" or "R3's own reading is an artifact" is asserted.

**3. Extend Leg A's `C_thr(L)` score to 750 nm (PHOTONICS' own flagged,
still-open contamination-risk precedent) before further conclusions rest on
a 600nm-only PASS.** This is a constraint-3 concern squarely in this
program's own ESTABLISHED finding that the phenomenon must be
wavelength-flat ("white light changes nothing"). T21's own on-file
750nm/θ=40° fringe, in this identical 36°–43° window, already measures
4.7×`C_thr` — a previously-disclosed, still-untested risk this cycle
correctly flags (Idealization 64/fix per PHOTONICS) but does not close.
Whether `delta_scene` itself shares that λ-sensitivity is unknown and
matters for any future white-light passivity argument resting on this
signal being negligible.
