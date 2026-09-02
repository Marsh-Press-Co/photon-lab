# exp-103 Phase 1 — Proposal
**Panel Iteration 80 — LEAD seat: MATERIALS & METAMATERIALS**
**Thread: T28 (graded-black absorber near-field shadow, coherent point/region instrument family, R4/native-flagship line)**

## 1. Narrative

T28's newest instrument, kappa(theta) = |Ez_article|²/|Ez_empty|², passed its internal self-consistency gates (A, D, and a corrected C) in exp-102 but failed Gate B — not because it is wrong, but because its point sample and the established `beam_behind` figure's wide window sample are not taken at comparable standoff, and, on direct code read, Gate B's own source construction silently used `edge=24` instead of the R4 family's `edge=80`, conflating standoff with aperture shape. Both defects are fixable with the same single new field capture, so this cycle proposes one combined Phase-4 build: a fresh pair of native-scale flagship FDTD runs (empty + article, theta=0, Gate B's exact geometry) but built with `profile="plane", edge=80`, matching the R4 family the rest of this program already trusts. From that one capture we compute two things: a genuine window-averaged kappa_window over the literal established BEHIND footprint (the true apples-to-apples Gate B rebuild), and a standoff trend of kappa_region sampled from x=352 out through the window, using the same aperture-matched field for both so the two questions this cycle answers are never accidentally conflated with each other.

This is instrument-building, not physics. The graded_black_shell article under test is the program's already-established UNOBTANIUM-WITH-PARAMETERS idealization — arbitrary continuous grading, arbitrary sigma profile, no dispersion, no fabrication constraint. Nothing here characterizes a realizable coating; it characterizes how *this* idealized simulated article's own near-field shadow fills in with standoff, using an instrument whose cross-scale trust currently rests on self-consistency alone.

## 2. Parameter table

| Parameter | Value |
|---|---|
| Grid | N = 560 × 560 |
| cells_per_lambda | 20 |
| courant_frac | 0.32 |
| absorb (PML) | 40 |
| STEPS | 3200 |
| SRC_X | 64 |
| Source profile | `plane`, **edge=80** (R4-family aperture; corrects Gate B's silent `edge=24` default) |
| Wavelength | 600 nm (single) |
| Object center | (CX, CY) = (252, 280) |
| pec_disk core radius | r = 30 |
| graded_black_shell | r_in = 30, r_out = 78 (unchanged — same object Gate B already uses) |
| sigma_max | inherited unchanged from the existing graded_black_shell article definition (exp-094–102 / Gate B convention; not re-tuned this cycle) |
| Runs | 2: (1) empty scene, (2) article scene, theta = 0° only |
| **kappa_window footprint** | x ∈ [357, 457), y ∈ [260, 300) — literal established BEHIND window, spatial mean of \|Ez\|² in numerator and denominator |
| **Standoff sample x-values (kappa_region)** | Near-field gap-fill (Tier-1 item 1, between Gate B's own point and the window's near edge): **x = 352, 353, 354, 355, 356** (5 readings; x=352 doubles as the already-established Gate-B-corrected reference point). Window-spanning (coarser, ~18–20 cell pitch, Tier-1 item 2 support): **x = 357, 375, 395, 415, 435, 456** (6 readings, from the window's near edge to just inside its far edge). **11 kappa_region readings total.** |
| H_REGION | Gate B/exp-102's own established small-block convention, taken **unrescaled** — this cycle reuses Gate B's own object exactly (r_out = 78 = Gate B's r_out), so the r_out-ratio rescaling exp-102 needed for the T8 bridge-family geometries is exactly 1 here and is skipped rather than reapplied as a no-op. |
| FLOOR_FRAC | 0.10 (reused house convention, R13/R14) |
| **FDTD call budget** | **Exactly 2** real FDTD stepping calls (empty-scene run, article-scene run). kappa_window and all 11 kappa_region readings are post-processing arithmetic on those two captured Ez snapshots — **zero** additional FDTD calls. Code-assertable as call-count == 2. |

## 3. T1 escape-route statement

N/A. This is a diagnostic / instrument-building cycle. No mechanism, no T1 physical claim, no escape route is proposed — identical in kind to exp-101 and exp-102.

## 4. Falsifiable predicted outcomes

**(i) kappa_window.** Predicted band: **0.5%–4.0%**. The established `beam_behind` figure (1.5–1.8%) is the anchor, but kappa_window is a genuinely different instrument — a coherent, window-averaged \|Ez\|² intensity ratio at a single theta, not whatever power/envelope metric produced the original figure — so exact overlap is not the falsifiable claim. The band is centered near the established figure but widened roughly 2–3× on each side to allow for coherent standing-wave/fringe structure in \|Ez\|² that a non-coherent or flux-based metric would average out, and for the edge=80 aperture (wider than the original beam_behind construction may have used) shifting diffraction fill-in somewhat. What *would* falsify the reproduction: a result outside this band (e.g. an order-of-magnitude miss, or a value indistinguishable from the empty-scene floor), which would indicate the aperture fix did not, in fact, resolve Gate B's discrepancy.

**(ii) Standoff-trend shape.** Predicted: kappa_region **rises monotonically (non-decreasing above the FLOOR_FRAC noise floor) from x=352 through x=456, with at most one local reversal** exceeding the floor tolerance. This is the Fresnel-fill-in hypothesis from the Iteration-79 audit. Falsified by: a non-monotonic, multi-reversal (fringe-limited near-field null) pattern, which would instead support a diffraction-fringe explanation for Gate B's original failure rather than smooth fill-in.

**(iii) Floor-gate / consistency check.** At every one of the 11 sampled points, both empty- and article-scene \|Ez\| must stay above FLOOR_FRAC (0.10) of the source-region reference amplitude; any point failing this is flagged unreliable and excluded from the trend claim in (ii), not silently averaged in. Separately, the mean of the six window-spanning kappa_region readings (x=357..456) is predicted to fall within a factor of ~2 of kappa_window itself, as a coarse internal cross-check between the point-sample and window-average views of the same captured field. Note on R22: kappa is a ratio of squared magnitudes (\|Ez\|²/\|Ez\|²), not a signed vector identity — it is non-negative by construction and introduces no sign convention to justify, unlike the identity exp-102's Gate C caught.

## 5. Idealizations

- 2D FDTD, single wavelength (600 nm), normal incidence only (theta = 0°); no dispersion, no broadband claim.
- Near-field-only standoff range sampled (x = 352–456); no far-field extrapolation is claimed or implied.
- PEC core treated as ideal (lossless, infinite conductivity); graded_black_shell is the program's already-established **UNOBTANIUM-WITH-PARAMETERS** idealized article (arbitrary continuous sigma grading) — unchanged by this cycle.
- courant_frac, absorb, STEPS, and sigma_max are inherited unchanged from established convention, not re-tuned or searched (R5/R17) — only the source `edge` parameter is deliberately changed, and only to match the R4 family's own established value, not chosen post-hoc to force a pass.
- No thermal/energy-sidecar machinery is touched this cycle at all (R21) — matching exp-102's own precedent explicitly, to avoid any unforced R21 obligation.
- **Tier 1 item 3 (r=78/156/312 T8 bridge-family extension) is explicitly deferred to Iteration 81.** Reason: this cycle already spends its real FDTD budget (2 calls) on the Gate B rebuild + standoff trend, which is the higher-priority, cheaper item; a genuine r=156/312 extension requires new, non-trivial geometry-scaling work (not a parameter tweak) and deserves a dedicated cycle rather than being compressed alongside this build.
- **Tier 3 (delta_scene R3-vs-R4 split) — this is the FOURTH consecutive deferral (exp-100, exp-101, exp-102, and now exp-103).** MATERIALS-seat reasoning for deferring again: the Gate B rebuild in this cycle is a *precondition* for trusting any future kappa(theta)-family citation, including whatever a delta_scene resolution would itself need to cross-check against — resolving delta_scene now, before the instrument it would presumably be read through is independently trusted, risks producing a result nobody can yet calibrate. This is a scope-ordering argument, not a dismissal: if Iteration 81 completes the Tier 1 item 3 bridge-family extension, delta_scene should be treated as due next, and a fifth silent deferral should be considered a rule violation rather than routine.

## 6. Realizability bound

**Article status: UNOBTANIUM-WITH-PARAMETERS.** The graded_black_shell object measured here is the same idealized R4/native-flagship article already carrying that status across exp-094–102 and Gate B; this cycle does not change or re-examine that status, and every kappa reported in Section 4 is a statement about this idealized simulated article's own near-field falloff behavior in silico, not a claim about any fabricable coating.

If a realizable graded-absorption coating at comparable optical depth were substituted (e.g. a discretely-layered impedance-matched metamaterial absorber stack, tapered carbon-nanotube forest, or graded-index metasurface), I would expect the near-field fill-in curve to differ in two ways: (1) less smoothness — a finite number of discrete grading layers, rather than continuous sigma grading, would imprint small periodic ripple on the standoff trend tied to layer-boundary reflections, potentially producing exactly the kind of local reversal item (ii)'s prediction allows for one of; and (2) a higher floor at short standoff — real absorbers are bounded by causality (Kramers–Kronig) and finite sub-wavelength thickness in how much extinction they can pack into r_out − r_in, so a realizable shell would likely leak more field into the near-field shadow than this idealized, arbitrarily-strong-graded simulated article does, meaning kappa_window for a realizable coating should be expected to sit at or above this cycle's predicted band, not below it.
