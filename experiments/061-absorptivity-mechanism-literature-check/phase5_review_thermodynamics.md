# Phase 5 — THERMODYNAMICS blind review (exp-061 / Iteration 38)

*Fresh sub-agent, blind to the other five Phase-5 reviews and to Red
Team. First dispatch of this review was terminated mid-task by an
upstream `[bio]`-tagged content-policy block (API error, "Sonnet 5
can't help with this... Start a new session to continue") — the same
class of false-positive block this program first documented at
Iteration 30 (kinetics/dose/irradiance vocabulary pattern-matching a
dual-use-research classifier). A second, independent, fresh dispatch
(this file) completed cleanly with lightly-adjusted phrasing (no
substantive change) — noted here per the Iteration-30 precedent's own
instruction to record when a block reproduces or resolves.*

**Independent re-derivation (150 µm, as reported in NOTES.md):** running
the exact snippet gives central ΔT_ss = 3.6868×10⁻⁴ K (margin 54.25×)
and worst-case ΔT_ss = 2.4732×10⁻³ K (margin 8.09×). Both match
NOTES.md's reported 3.69e-4 K/54.2× and 2.47e-3 K/8.1× to stated
precision. `python3 lab/caveat_lint.py` passes clean: 5 caveats checked,
0 required-site failures.

**But the 150 µm choice is stale, and re-scoping it changes the finding
materially.** The THERMO disposition's `l_geometric_m=150e-6` is
explicitly sourced to "MP-2's own predicted upper thickness bound" — a
Phase-3 PREDICTION, frozen before Phase 4 ran. Phase 4 (MP-5) landed the
ACTUAL multiple needed to reach τ_true at visible wavelengths at
~230–730×, not the predicted ~15–100×, i.e. the representative real
object is roughly 331 µm–1.05 mm, not 150 µm. NOTES.md's own closing
line ("MP-5's own resolution here only widens the multiple, which does
not change the worst-case bound already computed") is asserted, not
re-derived — and it is wrong on the margin, though not on the
classification. Recomputing at the same worst-case irradiance
(4.414×10⁻⁵ W/cm²) and 100%-absorption ceiling across the actual MP-5
range:

| Multiple | l | ΔT_ss (K) | Margin vs 0.020 K |
|---|---|---|---|
| 230× | 331 µm | 0.00528 | 3.79× |
| 298× | 429 µm | 0.00672 | 2.98× |
| 374× | 539 µm | 0.00826 | 2.42× |
| 730× | 1.05 mm | 0.01476 | **1.35×** |

At the top of MP-5's own confirmed range (730×, the most plausible
visible-band figure per MP-5's own "most plausibly several hundred×"
restatement), classification is still nominally UNDETECTABLE — but the
margin has collapsed from the reported "8.1× (comfortably clear)" to
1.35×, a factor of ~6 erosion, and sits uncomfortably close to the
NETD_lo threshold itself. A ~35% adjustment to any one free assumption
in the chain (emissivity, k_air, the 100%→measured 0.51–0.61 absorption
ratio being partially relaxed, or the NETD_lo/hi band's own stated
uncertainty) would flip this cell to MARGINAL or DETECTABLE. That is not
true at 150 µm, where the same perturbations leave 8× of headroom.

## Verdict: **PARTIAL**

The classification (UNDETECTABLE) survives at every scale tested, so
this is not a reversal. But the disposition's own claim of "comfortably
clear" margin does not survive contact with this cycle's own later, more
authoritative Phase-4 finding — the box computed the right answer to the
wrong question's scale.

## Defects found

1. **[MAJOR — genuine THERMO gap]** The THERMO disposition anchors
   `l_geometric_m` to MP-2's PREDICTED thickness band (Phase 3,
   pre-search), not MP-5's FOUND multiple (Phase 4, post-search) — even
   though MP-5's own resolution was known before NOTES.md's closing
   "THERMO disposition ... reconfirmed, not re-run" line was written.
   The sentence asserting no consequence is a judgment call presented as
   a checked fact; it was not re-run against the actual number sitting
   three sections above it in the same file.
2. **[MODERATE]** "Comfortably clear" (Phase-3 language, carried into
   NOTES.md) is margin-dependent language that stops being accurate once
   the correct scale is substituted — a wording defect that will mislead
   a future cycle skimming NOTES.md rather than re-deriving.
3. **[MINOR]** No sensitivity sweep across MP-5's own 230–730× range
   appears anywhere in the disposition — a single point estimate at the
   (now-outdated) upper thickness bound stood in for what should have
   been a range check, given MP-5's own reported spread was nearly 3×.

## Ranked top-3 candidate directions, Iteration 39

1. **Rerun the THERMO disposition at the corrected scale** (331
   µm–1.05 mm, MP-5's own actual range, not MP-2's stale prediction),
   reporting the margin sensitivity table above as the disposition box,
   not a single point. Cheap (desk-only, same `thermo_sidecar.py`
   calls) and closes a real, now-documented gap.
2. **Add a caveat_lint registry entry** for "THERMO disposition length
   scale must track MP-5's own resolved multiple, not MP-2's pre-search
   prediction" — this is exactly the un-registered-drift shape the tool
   exists to catch, and this cycle just demonstrated it live.
3. **Sensitivity-test the margin's most fragile input at the corrected
   scale** — specifically emissivity and the 100%→realistic
   absorption-ratio ceiling, since at 1.35× margin, this disposition is
   now one modeling-choice away from crossing into MARGINAL/DETECTABLE.
