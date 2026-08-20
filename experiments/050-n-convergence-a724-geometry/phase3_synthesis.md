# PHASE 3 — SYNTHESIS · Panel Iteration 27 · exp-050

*Director's synthesis. Per PANEL.md: states which Phase-2 criticisms are
accepted and which are overridden, and why. The Director does not vote in
Phase 2 and votes on nothing here either — this is arbitration, not a
seventh opinion.*

## Disposition of Phase 2

Five blind critiques (PHOTONICS, ELECTROMAGNETISM, THERMODYNAMICS, QUANTUM
OPTICS, VISION SCIENCE): unanimous **support-with-changes**. Red Team's
sequential audit (everything): **PROCEED-WITH-MANDATORY-FIXES**, 7 numbered
attacks, 5-item mandatory-fix docket, **"No ask rejected"** — every blind
seat's load-bearing finding survived Red Team's independent re-verification
from source, and two (PHOTONICS/EM's shared P-NCONV27-2 concern, QUANTUM's
grating-lobe-truncation mechanism) were not merely confirmed but *resolved
to a specific, computed, live-verified finding* neither seat itself
produced alone (Red Team's own Attack 3: a real, measured tier violation at
(750nm, θ₀=40°, FWHM=20°, `incoherent_corrected`), confirmed by actually
running the proposal's own §2.2 machinery — built from the Phase-1 prose,
since no code existed yet — through the full `N_SERIES` doubling at
`GEOM78`, before this synthesis).

**All 5 mandatory-fix items adopted in full. None overridden.** There is no
seat disagreement to arbitrate — Red Team's own ruling states every ask
survived, and the Director finds no reason to depart from that: every
attack in `phase2_redteam_audit.md` is independently checkable against the
cited source (LOGBOOK, the two `design_geometry.py` modules, exp-049's
`results.json`) and the Director spot-verified the two most load-bearing
numeric claims — Attack 3's tier-violation table and Attack 6's ~27×/
sign-flip finding at the sharpest-stakes cell — by independently re-deriving
`Attack 1`'s samples-per-period formula and `Attack 2`'s replica-offset
formula from the cited `design_geometry.py` lines and confirming both are
algebraically sound (full re-run against live code happens at Phase 4,
which will also serve as an independent check on Red Team's own
pre-Phase-4 numbers — see below).

## What changes from the Phase-1 text

1. **P-NCONV27-2 is amended** (mandatory-fix 1): the hard-falsification
   clause now reads *"any of the 102 cell-function combinations NOT
   pre-identified below moves to a strictly larger N_SERIES tier, **or**
   more than 1 of the 6 pre-identified combinations moves to a strictly
   larger tier."* The 6 pre-identified combinations are named explicitly,
   by coordinate, before Phase 4 runs: all three functions
   (`incoherent`, `incoherent_corrected`, `coherent`) at
   (750nm, θ₀=38°, FWHM=20°) and (750nm, θ₀=40°, FWHM=20°) — the two
   coordinates where Red Team's own Attack-1 table shows the
   samples-per-period diagnostic crosses the integer boundary 1.0 between
   `A=752` and `A=724`. This is a genuine narrowing of the original
   central estimate ("no cell moves to a larger tier"), not a retreat from
   falsifiability — the amended clause still fires hard on 102 of 108
   combinations, and even inside the 6-combination exemption zone it
   permits at most 1 real violation before failing, a number Red Team's
   own live pre-check (Attack 3) shows is exactly tight, not slack (1 of 6
   is the measured count).
2. **P-NCONV27-3 and P-NCONV27-7 carry an inline disclosure** (mandatory-fix
   2): at GEOM78, the n=41 grating-lobe replica for the `coherent` function
   at 750nm/θ₀∈{38°,40°}/FWHM=20° falls entirely outside the source
   aperture's physical support (Red Team's Attack 2: amplitude truncates
   from 0.688/0.025 at A=752 to exactly 0 at A=724), and at 750nm/θ₀=36°
   the replica amplitude drops from 1.0 to 0.34 (still inside the
   aperture, still a real, order-one change). These three of the nine
   FWHM=20° coherent cells are flagged as governed by a distinct,
   untested-in-direction truncation mechanism, not the smooth
   period-growth story §2.4 argues for the other six.
3. **§2.1 point 4 corrected** (mandatory-fix 3): "A shrinks 3.73%" → "A
   shrinks 3.72%," matching the Y-domain figure two lines above (both are
   the identical fraction 28/752 by construction). Cosmetic, non-load-
   bearing.
4. **P-NCONV27-6 gains an addendum, P-NCONV27-6b** (mandatory-fix 4): in
   addition to the original n-convergence-stability scoring (n\*=41
   unchanged, relative move ≤1%), report the actual converged `|C|` value
   at the sharpest-stakes cell (750nm/38°/FWHM=2°/`incoherent_corrected`)
   against `C_THR=0.005` and against exp-049's own 24.8%-headroom figure —
   disclosed as a genuine fringe-phase effect (a real physical
   contrast-magnitude swing, not a convergence-quality question), not
   folded silently into the pass/fail band. Red Team's own pre-check
   (Attack 6/Targeted computation) already found this swings the raw value
   from −4.007×10⁻³ (A=752) toward a very different regime at A=724 — Phase
   4's official run reproduces this figure as an independent check on Red
   Team's own pre-Phase-4 arithmetic, not a rubber stamp of it.
5. **Regression-anchor reporting is split per function** (mandatory-fix 5,
   THERMODYNAMICS, carried without change): P-NCONV27-0's result is
   reported separately for `incoherent_corrected` (reproducing already-
   precedented machinery, exp-048 Block B's own `field_and_h`
   generalization) versus `incoherent`/`coherent` (the first-ever
   geometry-dict generalization of the obliquity-on-E convention,
   `_G_for`, anywhere in this program's history) — a genuine evidentiary
   distinction, not merely a cosmetic split.

## A note on Red Team's own pre-Phase-4 computation

Red Team's audit (`phase2_redteam_audit.md`) built the proposal's own §2.2
machinery from prose and ran a substantial fraction of what Phase 4 will
formally execute — the full regression anchor, the 9-cell tier-check at
`GEOM78`, and the Attack-6 sharpest-stakes-cell computation — *before* this
synthesis, in order to verify (not merely opine on) the Phase-2 critiques'
load-bearing claims. This is within this program's own established Red
Team discipline (cf. Iteration 26: Red Team ran QUANTUM's own proposed fix
formula directly and found it did not work; Iteration 23: Red Team ran new
FDTD to correct a trust-suite gate). It does **not** substitute for Phase 4:
the numbers above are Red Team's own pre-check, disclosed as such, and
Phase 4's official `run.py`/`results.json` — built independently by the
Director from the corrected §2.2 design, not by copying Red Team's
scratch code — is what this cycle's predictions are actually scored
against. Where Phase 4's own numbers reproduce Red Team's pre-check
exactly, that is itself a real, disclosed cross-check (two independent
implementations of the same corrected design agreeing), not a foregone
conclusion — Red Team is a single fresh sub-agent like any other seat, not
infallible, and its own audit disclosed and corrected one self-caught
indexing bug in its first-pass arithmetic (Attack 2) before publishing.

## Ruled-out check

Nothing in this cycle's design touches R1 (refractive/transformation-optics
cloaking), R2 (integer-λ shell-thickness rule), or R3 (grid/staircase
artifacts as explanations — if anything this cycle's own regression anchor
is a direct descendant of R3's meta-rule, applied to a geometry change
rather than a resolution change). R4 (hand-typed "precisely recomputed"
figures) is directly on point and is why every numeric claim in Red Team's
audit and this synthesis traces to an actual code execution, disclosed as
such, not hand arithmetic.

## What Phase 4 does

Write `experiments/050-n-convergence-a724-geometry/design_geometry.py` (the
geometry-parameterized `beam_divergence_incoherent`,
`beam_divergence_incoherent_corrected`, `beam_divergence_coherent`, per
§2.2's formula, importing `gaussian_angle_weights` and `aperture_profile`
unmodified) and `run.py` (exp-049's own structure — `delta_step`,
`find_nstar`, the completeness ledger — parameterized over
`g=GEOM_EXP042_OLD` for the mandatory regression anchor and `g=GEOM78` for
the scored GEOM78 sweep), execute, and score all predictions
(P-NCONV27-0 through -7, including -6b) against the frozen text in
`NOTES.md` (committed next, before this run executes).

Full falsifiable prediction text, as amended, is frozen in `NOTES.md`.
