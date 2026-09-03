# PHASE 5 — REVIEW · Panel Iteration 82 · Seat: ELECTROMAGNETISM
## exp-105 — "The T8 r=78/156/312 Bridge, Extended to the Coherent Point/Region-Intensity Channel"

*Fresh context, blind to any other seat's current-cycle Phase-5 review, per
PANEL.md. Read in full: PANEL.md; LOGBOOK.md (RULED OUT R1–R23; LIVE
THREADS T1, T8–T15 in full; the Iteration-80/81 record immediately
preceding this cycle); `phase1_proposal.md`; all five `phase2_critique_*.md`
(including this seat's own, which is the direct ancestor of this cycle's
mandatory settling leg); `phase2_redteam_audit.md`; `NOTES.md`; `run.py`;
`results.json` (hand-checked, not merely read). Also consulted
`lab/validation/VALIDATION.md` for this engine's own established settling/
noise-floor baselines and `lab/sections.py` for exactly what `phasors()`
assumes about the field it is handed.*

## Verdict: **CONFIRM-WITH-GAPS**

The settling result is genuine and, on independent hand-verification,
stronger evidence than a bare PASS boolean conveys. But one real,
code-level defect survives Phase 3 into Result/Learned: **P3's own scoring
logic — this cycle's headline finding — carries zero risk-propagation from
the r=312 leg's own MARGINAL Nyquist tier and its total absence of a
settling check, even though P3's number IS the r=312 capture, more
directly than P4's is.** A second, previously-uncaught gap, sharper than
anything flagged in Phase 1/2/NOTES.md: `kappa_window` — the actual
quantity P3's shape-discriminator is built on — has never been
settling-tested, at ANY r, including r=156, where the settling machinery
this cycle built ran but was pointed at a different quantity.

---

## 1. Hand-verification of the r=156 settling result against `results.json::r156.settling`

Spot-checked 5 of the 53 `DENSE_X` points (x=682, 708, 734, 760, 786 —
spanning the full span) by hand, then computed summary statistics over all
53 in `results.json::r156.settling`.

**Point-by-point (x=682):** `kappa_point_1x=2.8261134478728287e-4`,
`kappa_point_2x=2.817012644423949e-4`. `|Δk|=9.1008e-7`,
`rel_change = 9.1008e-7 / 2.8261134478728287e-4 = 0.0032203` — matches
the stored `0.003220254111076076` to the printed precision.
`dphi_point_1x=1.628550664221346`, `dphi_point_2x=1.621823136394612`,
`|Δφ|=0.006727528` — matches the stored `phase_diff=0.0067275278267340255`
exactly. Repeated for x=708, 734: both `rel_change` and `phase_diff`
reproduce the stored values to the last printed digit by direct arithmetic
on the stored `kappa_point_1x/2x` and `dphi_point_1x/2x` fields — the
settling block's own arithmetic (`run.py:611,615`) is correctly computed,
not merely correctly labeled.

**Full-population statistics (all 53 points, computed directly from
`results.json`, not restated from `run.py`'s own printed summary):**

| | min | median | mean | **max** | tolerance | max/tolerance |
|---|---|---|---|---|---|---|
| `rel_change` (κ) | 1.74×10⁻⁴ | 5.09×10⁻³ | 5.28×10⁻³ | **1.380×10⁻²** | 0.20 | **6.9%** |
| `phase_diff` (rad) | 1.71×10⁻⁴ | 2.47×10⁻³ | 2.72×10⁻³ | **6.73×10⁻³** | 0.20 | **3.4%** |

Zero points anywhere near the tolerance boundary (the worst point uses
under 7% of the κ budget and under 4% of the phase budget) — this is not a
narrow escape.

## 2. Is a clean pass at 20%/0.20 rad actually strong evidence, or could the tolerance be too loose to catch a real transient?

**Strong evidence, on this specific data — not because the bar is tight,
but because the measured margin against it is enormous and structurally
informative about what `phasors()` actually tests.**

`lab/sections.py::full_capture`/`phasors` extracts a single-frequency
phasor from **two field snapshots a quarter-period apart, taken at the very
end of the run** — a construction that is only exact if the field is
genuinely in periodic steady state by the time `sim.run(steps)` returns.
Doubling `STEPS` and re-extracting is therefore not a generic "run it
longer and see" — it is a direct test of exactly the assumption this
two-point phasor construction depends on: if a real transient (turn-on
ringdown, a slowly-decaying evanescent near-field component) were still
present at `STEPS=6400`, the *same* two-snapshot method applied after
`STEPS=12800` would land on a measurably different point in that decay,
and `kappa_point`/`dphi_point` — a **single-cell, zero-averaging** read,
the most transient-sensitive channel this program has ever settling-tested
(EM's own Phase-2 point) — would show it. It didn't: not a borderline
pass, a landslide one, uniformly across the full 682–786 span (no growth
toward either edge that would suggest a partial, boundary-adjacent
artifact).

A second, independent corroboration: `VALIDATION.md`'s own stage-20 entry
(Iteration 35) establishes that on this program's **own canonical,
comparably-lossy bench** (`sigma_max=0.5`, this cycle's own r=78 value),
the identical phase-rotation-sensitive settling idiom converges to
~1.5×10⁻⁵ field-relative RMS by 900 steps — and that settling is governed
by material loss, not step count or domain size, a property that
transfers directly to `graded_black_shell(sigma_max(κ)=0.5/κ)` at r=156
(`sigma_max=0.25`, still substantially lossy, `τ_shell=24.0` held fixed by
construction). This cycle's own measured residuals (10⁻⁴–10⁻² range) sit
**one to three orders of magnitude above** that established pure-numerical
floor — meaning what was measured is not simply "everything is at the
noise floor so of course it passed," it is a genuine, small, physically
real point-channel residual that clears the pre-registered tolerance with
wide margin. Both readings point the same way: this is a real settling
check that really passed, not a loose bar that happened not to bind.

**One honest caveat, worth carrying forward, not a defect in this
cycle's own result:** `STABILITY_TOL=0.20`/`PHASE_STABILITY_TOL=0.20 rad`
were *reused* from exp-103's own wide-channel convention, not derived from
this channel's own observed residual-decay rate before the fact. The
actual data would have cleared a tolerance 10–15× tighter just as cleanly.
Recommend NOTES.md's own Result prose state the **measured max
margin** (6.9%/3.4% of budget), not only the pass-count booleans it
currently reports (`0/53`, `0/53`) — the booleans alone under-communicate
how comfortable this pass actually was, in the same spirit (if not the
letter) of this program's own R4 "an aggregate flag is not sufficient"
lineage.

## 3. Energy-conservation / diffraction consistency of P3's accelerating `kappa_window` collapse

**Qualitatively consistent with what a fixed-absolute-offset window
sampling a growing absorbing obstacle's own near field should do — this is
not, on its face, an anomaly demanding new mechanism — but the specific
factor-of-~9 acceleration (20.7× then 185×, not a constant ratio) is not
something I can certify as "the real physics" versus "partly a
measurement-floor effect" without the floor check named below.**

The window offset (`D_EFF=77` cells, the standoff-midpoint from the
object's own `R_COAT` surface) is held **fixed in absolute cells** while
`R_COAT` itself doubles at each step (78→156→312). Two consequences,
both already visible in this cycle's own `geom()` output and consistent
with standard near-field/Fresnel-diffraction bookkeeping:

- **The window moves from ~1 object-radius behind the surface (77/78≈0.99
  at r=78) to ~1/4 object-radius behind it (77/312≈0.25 at r=312)** — in
  units of the object's own size, the fixed window drifts steadily deeper
  into the geometric-shadow region as r grows.
- **The near-field depth scale that governs how far an edge-diffracted
  wave must travel to refill the shadow interior grows as `R_COAT²`**
  (the Rayleigh-range-like scaling this proposal's own `z/z_R∝1/r²`
  construction already encodes: 0.253→0.063→0.016, an exact ×4 shrink per
  r-doubling). A fixed absolute offset therefore represents an
  ever-shrinking *fraction* of the near-field depth that would need to be
  crossed for edge diffraction to refill the shadow at that plane.

For a **graded, apodized absorber** — no sharp edge, so no PEC-style
residual on-axis Arago/Poisson-type bright spot sustaining the shadow
interior — the physically expected consequence of shrinking `z/z_R`
faster and faster (in the sense that the SAME absolute distance
represents ever less of the relevant diffraction length as the object
grows) is a residual intensity at the fixed plane that falls off **faster
than either of the two power laws tested (linear in `x=√(z/z_R)` or in
`z/z_R` itself)** — consistent, in direction and in why it should
accelerate rather than merely miss a fit, with the measured shape_ratio of
19.79 sitting nearly 5× past even the more generous (linear-law, 4.00±0.5)
band. **T14's own established finding — this exact article's ambient
Weber-contrast channel shallows the WRONG way as the object grows — is a
genuinely different quantity under a genuinely different (incoherent,
9-angle-summed) instrument; this cycle's B>0 result (§P3b) is real
evidence of non-replication, not a contradiction, and I confirm the sign
reading independently: `model_A_B=+0.00701`, unambiguously positive.**

**What I cannot certify from EM reasoning alone, and what the code does
not yet check:** `kappa_window(312)=4.79×10⁻⁶` is a genuinely small
number, and **no floor gate exists anywhere on `kappa_window`'s own
denominator** (the BEHIND window's empty-scene mean intensity,
`win_e312["mean"]`). `floor_gate()` is called in this file on the
DENSE_X wide- and point-channel empty-scene intensities (`run.py:586-587,
675`) but never on `window_stats()`'s own output — the one quantity P3's
entire headline number is built from. A steep-but-real diffraction falloff
and a discretization/PML-leakage floor being approached from above look
identical in a single number with no independent floor characterization
attached; NOTES.md's own Next item 1 names exactly this ambiguity but the
code that could resolve it (zero marginal FDTD cost — `win_e312["std"]`
and `["min"]` are already computed by `window_stats()` and simply never
compared against anything) was not run this cycle.

## 4. Does P3's own scoring logic in `run.py` propagate the r=312 settling-risk flag? — No, and this is the sharpest finding of this review.

Directly checked. `p4_156_trusted = settling_overall_pass and (nyq156 ==
"TRUSTED")` (`run.py:632`) is real, working risk-propagation machinery —
P4's own verdict is explicitly gated on both the settling leg and the
Nyquist-margin tier, and the r=312 leg's own `MARGINAL-REDUCED-CONFIDENCE`
tier is carried into both the printed console output and
`result_text`'s own P4 paragraph ("no settling leg run at r=312 this
cycle — disclosed idealization, Next item").

**P3 has no equivalent gate at all.** `p3_result["verdict"]` is
unconditionally `"SCORED"` whenever `r312_committed` is true
(`run.py:696-718`) — it reads `kappa_window_312` directly (computed from
the identical `cap_e312`/`cap_a312` capture P4 also reads, at the identical
single `STEPS=g312["STEPS"]`, with **no doubled-STEPS r=312 leg run for
either channel**) and fits both candidate models against it with no
reference anywhere to `nyq312`, to a settling flag, or to any trust tier.
Confirmed directly in `results.json::p3` — the dict has fields for
`x78/x156/x312`, both models' `B`/`C`/`pred78`/`miss`, `shape_ratio`, and
`verdict:"SCORED"` — **no `nyquist_tier`, no settling-risk field, nothing**
— while the *same* r=312 capture's `nyquist_tier` field is present and
correctly populated one level up, inside `results.json::r312`. The
information exists in the file; P3's own scoring path simply never reads
it. `result_text`'s own P3 paragraph (`run.py:800-808`) likewise never
mentions the Nyquist/settling status — it states the pre-registered T8
prior and the miss percentages, nothing about the r=312 measurement's own
reduced-confidence status, even though P4's paragraph three lines later
does exactly that for the identical underlying capture.

This is not a hypothetical concern: P3 is arguably **more**, not less,
exposed to this risk than P4. P4's test is a *residual* construction
(`point − wide`), which by subtraction partially cancels a slowly-varying
transient common to both channels; P3's headline number **is**
`kappa_window(312)` itself, undivided, unresidualized — the rawest
possible read of exactly the capture whose own pre-registered Nyquist
pre-check landed at `MARGINAL-REDUCED-CONFIDENCE` (1.234, barely above the
1.0 `UNRESOLVED-BY-CONSTRUCTION` floor) with no settling leg run at all.
**A reader of `NOTES.md`'s own Result section sees P3 reported as
"SCORED — the headline, genuinely surprising finding" with no
qualification, while the structurally analogous P4 r=312 reading three
paragraphs later is correctly and explicitly flagged reduced-confidence.**
The asymmetry is a real gap, not a difference in how much risk actually
exists.

## 5. T1 / passivity-reciprocity-causality bookkeeping

Unchanged from this seat's own Phase-2 finding, reconfirmed against the
executed run: no σ/ε/μ physics is touched; `sigma_max(κ)=0.5/κ` stays
strictly positive at every κ run (1, 2, 4); passivity holds trivially.
Reciprocity remains moot (single-source, forward-only bench, no
source/observer swap anywhere in this program's history on this bench
family). Causality is moot for a steady-state phasor instrument, not
"satisfied." **N/A is still the correct disposition; nothing this cycle
executed changes that.**

## 6. Ranked top-3 candidate directions (ELECTROMAGNETISM's own picks, Iteration 83 queue)

1. **Floor-gate `kappa_window`'s own denominator at every already-captured
   r, before any mechanism debate on P3's accelerating collapse.** Zero
   marginal FDTD cost — `window_stats()` already computes `std`/`min`
   alongside `mean`; apply the same `floor_gate()` convention already used
   for the wide/point DENSE_X channels to the BEHIND-window's own
   empty-scene intensity at r=156 and r=312 (r=78's `window_stats` detail
   may need pulling from exp-103's own persisted record — check before
   assuming it is available). This is the single cheapest, most direct way
   to discharge NOTES.md's own Next item 1 and is a precondition, not a
   nice-to-have, for trusting P3's shape_ratio=19.79 as physics rather than
   partly a floor artifact.
2. **A settling-independence check on `kappa_window` itself — not just
   `kappa_region_point`/`delta_phi_point` — at r=156 (this cycle's already-
   captured doubled-STEPS fields, if not discarded) and, more urgently, at
   r=312.** `kappa_window` has never been settling-tested at ANY r in this
   program's history, a gap this review is the first to name specifically
   (distinct from, and not closed by, this cycle's own mandatory-fix-3
   point-channel leg, which tests a structurally different quantity).
   Given P3 is this cycle's own headline, surprising result, this is
   higher-priority than the still-open r=312 point-channel settling gap
   NOTES.md's own Next item 2 already names.
3. **Gate P3's own verdict language in `run.py` on r=312's Nyquist/
   settling status, symmetric to the `p4_156_trusted` pattern already
   built.** A cheap, mechanical fix (one boolean, propagated into the `p3`
   dict and into `result_text`'s own P3 paragraph) that directly closes
   the risk-propagation gap named in §4 — without it, any future citation
   of shape_ratio=19.79 as a clean, trusted result inherits an
   unstated confidence gap the file's own data already contains but never
   surfaces where a reader would see it.
