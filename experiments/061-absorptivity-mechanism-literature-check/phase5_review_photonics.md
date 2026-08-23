# Phase 5 — PHOTONICS blind review (exp-061 / Iteration 38)

*Fresh sub-agent, blind to the other five Phase-5 reviews and to Red
Team.*

## Independent verdict: PARTIAL (UNOBTANIUM-WITH-PARAMETERS survives,
but one load-bearing judgment call needs to be flagged as genuinely
open, not settled)

**Arithmetic re-verification — all confirmed.** Independently computed
`tau_true = 2*(2*pi/20)*48*0.273840 = 8.258819829686677`,
`alpha_true = 5.7353e4 cm⁻¹`, e-fold = 174.36 nm, OD = 3.587 — all match
NOTES.md exactly. `design_geometry.py` reproduces `tau_shell=24.0`,
`alpha=0.016667/nm`, `e-fold=60.00nm` (the superseded anchor) exactly as
claimed. `caveat_lint.py` (full run and `--selftest`) both pass with
**0 required-site failures**.

**MP-1 spot-checks (2 rows, phase4_results.md):** R=1–2%/300–500µm
pairing → 78.2–153.5 cm⁻¹, bracketing the claimed 78–154 cm⁻¹ range
exactly. Patent row: OD=3.0 at ≤1µm → α=6.908×10⁴ cm⁻¹, ratio to target
= 1.204× — matches the claimed 1.20×.

## The MP-4 mechanism-class exclusion — this is the crux, and it does
not hold up cleanly

The patent candidate numerically clears both falsification thresholds
(1.20× on α, 1.44× on thickness) — the only thing standing between
UNOBTANIUM-WITH-PARAMETERS and a tier flip. The exclusion rests entirely
on "discrete-pigment vs. radially-graded ε(r)." From this discipline,
that is the wrong axis to exclude on. The document's own MP-1 verdict
and Idealization 3 already concede CNT forests are NOT well-described
as homogeneous Beer-Lambert media — structural/diffuse-scattering-
dominated, a genuinely different mechanism than `graded_black_shell`'s
smooth-ε(r) abstraction. A sub-wavelength, well-dispersed carbon-black/
dye-in-polymer film (what LCD black-matrix photoresists physically
are — engineered to be optically smooth, not hazy/diffuse) is the
textbook case where Beer-Lambert bulk absorption DOES apply cleanly. So
on the physically substantive criterion the document itself uses
elsewhere (homogeneous bulk loss vs. diffuse structural scattering), the
pigment film is arguably a CLOSER mechanism match to `graded_black_shell`'s
coded abstraction than CNT forests are — yet it's excluded on a narrower
literal-text technicality ("no radial grading") while CNT-forest
membership is never subjected to the same scrutiny.

A second, previously unflagged issue compounds this: black-matrix
"optical density" specs are conventionally TRANSMISSION-based
(OD=−log₁₀T), while every CNT-class α figure in MP-1 used
REFLECTANCE-based OD (OD=−log₁₀R). These are different physical
quantities. If the patent figure is T-based, applying the same
R→OD→τ→α conversion formula uniformly across both classes is a
units/methodology inconsistency that wasn't checked — could not verify
(T18-blocked), but it's a real, plausible defect that cuts in the
OPPOSITE direction from the grading argument (making the patent number
MORE comparable to τ_true, not less).

**Severity: load-bearing for MP-4's own dual-condition mechanics
specifically**, but not for the program's headline UNOBTANIUM-WITH-
PARAMETERS finding overall — MP-2's thickness gap (70–350×, multiply
corroborated, anchor-invariant) independently drives the same verdict
for the CNT-forest/Vantablack class the program actually targets.

**Idealization 4's scoping-out of index-graded comparators** (black
silicon/moth-eye) is also questionable from this seat: exp-060 already
established `graded_black_shell`'s gradation does real, separable
Fresnel-suppression work at the entry — an index-matching effect,
mechanistically the closest real-world analog to how moth-eye/black-
silicon structures work. Relegating that class to a "bound-widening
cross-check only" undersells the one comparator class that might
actually validate the grading half of this construction's mechanism.

**Wavelength handling:** mostly honest — the mid-IR forest figure is
repeatedly flagged as wavelength-mismatched. One cosmetic gap: the
Overall Summary table's MP-1 "Found" cell blends visible and mid-IR
figures without repeating the caveat inline — a small instance of the
caveat-propagation gap class this cycle's own tooling exists to catch
(not registry-tracked, so `caveat_lint.py` wouldn't catch it either —
consistent with the tool's disclosed Idealization 6 limitation).

## Ranked top-3 for Iteration 39

1. **Resolve the mechanism-class ambiguity properly**: determine whether
   black-matrix OD is T- or R-based, and whether real sub-µm pigment
   films are genuinely sub-wavelength/homogeneous or themselves diffuse
   at scale. Directly decides MP-4.
2. Pursue **index-graded (moth-eye/black-silicon) comparators as a
   primary, not secondary, class** for the Fresnel-suppression half of
   the mechanism, given exp-060's own finding.
3. PHOTONICS' own queued numeric-consistency-check tooling gap (a cited
   NUMBER, not just a phrase, drifting across sibling files — the exact
   `TAU_SHELL=24` failure mode) — still correctly deferred per Red Team,
   but should not slip further.
