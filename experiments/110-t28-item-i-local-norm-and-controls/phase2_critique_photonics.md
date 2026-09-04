# PHASE 2 — CRITIQUE · PHOTONICS · Panel Iteration 87 (candidate exp-110)

*Blind critique — written without sight of any other seat's Phase-2 output
this cycle. Charter: surface interaction, absorption spectra, angular
dependence, scattering cross-sections; is the proposal's optical response
coherent as stated, across wavelength and angle?*

## Verification performed before writing this critique

- **Mirror-symmetry index claim.** Read directly out of the committed
  `experiments/108-.../results.json`: `bin_centers_deg[0] = -176.25`,
  step `7.5`, both r. Computed `all(bc[i] == -bc[47-i] for i in
  range(48))` at both r=156 and r=312 — **exact**, floating-point
  identical. Independently re-derived from `lab/sections.py`'s own
  `angular_scattered_pattern()`: `edges = linspace(-180,180,49)`,
  `centers[i] = -176.25 + 7.5*i`, so `centers[47-i] = 176.25 - 7.5*i =
  -centers[i]` algebraically, matching the readback exactly. Confirmed.
- **The physical premise behind the mirror claim** (not just the index
  bookkeeping) — the proposal asserts "this bench is mirror-symmetric
  about the propagation axis" without deriving it; I checked this against
  `geom_fixedabs()` and `lab/fdtd2d.py` myself rather than take it on
  faith. `CY0=280`, `N0=560` ⇒ `CY0 = N0/2` exactly, and this ratio is
  preserved under the shared `k=r/R_BASE` scaling used for both `N` and
  `CY`: at r=156, `N=1120, CY=560=N/2`; at r=312, `N=2240, CY=1120=N/2`
  — **exact** at both r, not merely close. `add_line_source`'s default
  `y_lo/y_hi` span `[absorb, ny-absorb]` (the *whole* domain minus equal
  PML on both edges), with a symmetric tapered top-hat (`edge` window
  applied identically at both ends) — a genuine, full-width, y-symmetric
  plane wave, not a beam offset from `CY`. The core/coat circles and
  every `margin_box` are built from `hypot(x-CX, y-CY)` and
  `(CY±hw)`, both manifestly even under `y → 2·CY − y`. **Conclusion:**
  the underlying scattered field genuinely must satisfy `pattern[i] =
  pattern[47-i]` in the noiseless continuum/exact-grid-symmetry limit —
  this is not an assumption, it is forced by geometry+source+box, all
  independently confirmed exact at both r. Any measured `pattern[i] ≠
  pattern[47-i]` is registration/discretization noise, not a missed
  physical asymmetry — which is exactly what the proposal needs to be
  true for the floor to mean anything.
- **Grounding-fact finding (§0.5, "zero-FDTD" premise is false).**
  Independently re-verified, not trusted: `find / -iname "*exp108*"`
  across the full filesystem returns nothing — no scratch pickle exists
  anywhere in this session. Read both `experiments/108-.../results.json`
  and `analyze_output.json` directly: `item_i` in both carries only
  `verdict, rel32, runs, run_details, confirm_all_margins,
  sum_check_pass, bin_centers_deg` — no `pattern_by_margin_*` arrays
  anywhere, at either r, confirming the proposal's own claim #2. The
  cross-check against exp-108's own `phase5_review_photonics.md` §3b
  (62.5%/62.5% of bins <1% of peak, 9.88%/10.88% max local-normalized
  deviation, bins named at −146.25°/+168.75°) reproduces verbatim what
  this proposal cites — consistent, not inflated.
- **`lab/validation/run_all.py` stage26** (lines 2698–2792): read in
  full. The existing negative control (`corrupted_steps_done=0`,
  over-running by one chunk) and the proposal's symmetric addition
  (`corrupted_steps_done2=2·CHUNK`, under-running/truncating by one
  chunk, `remaining2=300>0` safely positive) are structurally identical
  in idiom — the proposed patch is a faithful, minimal mirror of the
  existing block, not a redesign.

## Steel-man (≤150 words)

The local floor gate answers exp-108's own PHOTONICS-flagged central gap
correctly, on genuinely re-derived physics rather than the proposal's own
assertion. I confirmed from source — not from the proposal's prose — that
`CY=N/2` exactly at both r (560=1120/2, 1120=2240/2), the source is a
genuine full-width symmetric plane wave, and every circle/box is exactly
`CY`-centered, so `pattern[i]=pattern[47-i]` is forced by geometry, and
`bin_centers_deg[i]=-bin_centers_deg[47-i]` reproduces exactly from the
committed array at both r. Unlike item ii's `abs_ext_ratio`-scale floor
(R9's unit-mismatch problem), this floor is same-instrument, same-units —
structurally stronger. It jointly discharges R13/R14 (both parents gated),
stays honestly scoped as informational rather than silently reclassifying
item i's frozen CONFIRM (avoiding a fresh R24 instance), and §0.5's
"zero-FDTD premise is false" finding is real: I independently confirmed no
scratch pickle exists and neither committed JSON carries the needed arrays.

## Sharpest attack (≤150 words)

The mirror-difference floor is structurally blind to any noise component
that itself respects the mirror symmetry. A common-mode bias present
identically in bin `i` and bin `47-i` — a systematic phasor-extraction
offset, a box-registration bias that is itself even in `y`, or a
Yee-staggering artifact affecting both mirrored half-cells alike —
cancels exactly out of `|pattern[i]-pattern[47-i]|` and vanishes from the
estimated floor. The construction can therefore only ever recover a
**lower bound** on the true per-bin noise, never the true or an
upper-bound floor — load-bearing for a gate whose entire purpose is
telling a ~10% near-null local deviation apart from noise. The proposal's
own queued Iteration-88 fault-injection control tests only detection of
an injected *asymmetric* perturbation; it cannot discover this blind
spot, since no common-mode case is in its planned scope. Without an
independent, non-differencing floor estimate at the two named bins
(a cheap `cpl` refinement spot-check would suffice), a bin cleared
RESOLVED here is unvalidated, not confirmed.

## Verdict: **support-with-changes**

The physical and index-level mirror-symmetry premise is sound and I
independently re-derived it from source rather than accepting it as
stated — this is the strongest-grounded floor-gate instrument this
sub-thread has built to date, and correctly kept informational this
cycle. The gap above is real but non-fatal precisely because of that
informational scoping: no scored constraint verdict this cycle depends on
`classify_item_i_local`'s output, so the common-mode blind spot cannot
corrupt this cycle's own deliverable — it can only mislead a *future*
cycle that later promotes this diagnostic's RESOLVED calls into a scored
verdict without addressing it first.

**Single change that would flip this to full support:** extend the
already-queued Iteration-88 fault-injection control's scope (§5,
Idealizations) to explicitly include a **symmetric/common-mode synthetic
perturbation case** (inject an identical offset into both members of a
mirror pair, confirm the floor correctly does NOT flag it as asymmetric
noise and does NOT inflate `local_snr`) alongside the already-planned
asymmetric case — cheap, zero-FDTD, and closes the one structural gap
this construction cannot self-diagnose.
