# Phase 2 Critique — PHOTONICS

**Cycle:** exp-076, "G40/PAD Decorrelation" (Panel Iteration 53, lead: QUANTUM
OPTICS by rotation). Blind, independent — written without reading any other
seat's Phase-2 output or Red Team's audit.

## Steel-man (≤150 words)

The instrument earns its optical bookkeeping. Re-running `design_geometry.py`
independently confirms `G40` is bit-identical to `C80` in every scene
coordinate — `A=752`, aperture, both clearances — so the dominant,
already-characterized T21 edge-diffraction fringe (period 1.9608° at 600nm,
set by `A` alone) is held exactly constant across all three configs this
cycle uses; only boundary-band thickness/PAD varies, the one axis actually
under test. `static_construction_identity` correctly confirms (0.000 diff)
the padded/shifted scored windows sit in vacuum identically in both configs,
ruling out a coordinate-shift bug. `G0-e`'s design choice is the right one —
anchoring `(T_x,psi)` to the strong common-mode `Cbar`, not to the
possibly-small `delta` — which I independently re-ran and verified (worst-case
1.03e-4 / 8.35e-3 relative error), correctly sidestepping an R5-class
free-period-fit-to-noise degeneracy.

## Sharpest attack (≤150 words)

Every config this cycle actually runs — `C40`/`G40` (`ABSORB=40`) and `C80`
(`ABSORB=80`) — sits at an exact integer multiple of λ at the cycle's only
tested wavelength: 40/20=2.000λ, 80/20=4.000λ (verified). This is precisely
the resonant/aliased condition exp-065's own Phase-3 mandatory fix (Red Team
attack 1, a PHOTONICS catch) added `C70` (non-integer at all three λ) to
guard against for the original `ABSORB` series — and that guard is absent
here. A graded lossy boundary is exactly the stack type that can show
Fabry–Pérot-like reflectance-magnitude extrema at even-integer-λ thickness,
riding on any smooth depth trend. `PAIR_ABSORB40` (`G40→C80`, 2λ→4λ) cannot
distinguish a genuine `ABSORB`-depth effect from an artifact tied to both
endpoints sharing the same "even-multiple" phase of such an oscillation. No
second wavelength or non-aliased control exists this cycle — a §4(a)
"ABSORB-tied" verdict would rest on data that cannot, by construction, tell
the two apart.

## Supporting detail (not part of the word-limited items above)

- **Verification performed, not asserted.** I re-ran `design_geometry.py`
  (`experiments/065-.../design_geometry.py`) myself and reproduced the G40/C80
  congruence table and `static_construction_identity` (0.000 diff, all-vacuum
  scored windows) bit-for-bit. I re-ran `g0e_amplitude_channel_check.py`
  myself, in the background, to completion — Case 1 worst
  `|recovered/expected − 1| = 1.03e-4`, Case 2 worst `= 8.35e-3`, matching the
  proposal's own committed output exactly. I independently re-derived the
  baseline `amp_ratio` figures directly from `experiments/072-.../run.py`
  against its own committed `results.json`: `C40–C60=0.1611`,
  `C60–C70=0.0407`, `C70–C80=0.0198`, `C40–C80=0.1659` — matching the
  proposal's cited 0.161/0.041/0.020/0.166 to the stated precision (R4
  discipline, not taken on the proposal's word).
- **The `static_construction_identity` gate is correctly scoped, not a hidden
  gap.** The task brief for this critique specifically asked whether this
  zero-FDTD gate — which only checks the static `damp_e`/`damp_hx` arrays at
  the *scored windows* (confirmed `all_vacuum=True` in both configs) — is
  being over-read as saying something about the boundary band's own dynamic
  optical response. Having read the code and the proposal's own §2a framing
  ("this cycle spends the FDTD budget only where the boundary itself... is
  what's under test"), it is not: the gate is used exclusively to rule out a
  coordinate-shift/off-by-one construction bug in the padding, and the
  proposal never cites it as evidence about the boundary's reflectance. This
  is correct scoping, not a flaw — flagged here so it isn't mistaken for an
  unclosed gap by a later reviewer who reads only the gate's name.
- **Countervailing evidence I checked before finalizing the attack above,
  and why it does not resolve it.** exp-071 (Iteration 48) already showed the
  four congruent configs' own *free periods* (C40=2.4361°→C60=2.5188°→
  C70=2.5338°→C80=2.5338°) form a smooth saturating-exponential trend
  (R²=0.998) that the non-aliased `C70` point sits on cleanly alongside the
  aliased `C80` point — evidence against a *period*-level integer-λ
  resonance. But `amp_ratio` is not a period; it is an *envelope-amplitude*
  mismatch of the pairwise difference at a shared carrier, and no comparably
  smooth trend has ever been established for that quantity across
  aliased/non-aliased `ABSORB` values, nor for `G40` at all (it was never a
  member of the original four-point series `exp071` characterized). The
  period-smoothness finding is reassuring but answers a different question
  than the one this cycle's headline metric asks.
- **Window resolving power, noted but not the sharpest attack.** The 6°
  window (36°–42°) spans ≈3.06 periods of T21's own fringe (1.9608°) and
  ≈2.11 periods of T28's own established ≈2.84° periodicity — the same
  narrow window exp-074's Cramér–Rao pricing already quantified as poorly
  conditioned (`cond9≈478–529`, `VIF_Rq≈31–37`) for a 5-column carrier-
  conditioned fit sharing this exact design matrix. `G0-e` validates the
  estimator's *noiseless bias* under a matched, externally-supplied period —
  it does not test the fitted `A_i`/`A_q` coefficients' *sensitivity* to
  realistic instrument-floor-level noise (this program's own established
  0.001–0.007 absolute systematics, T20/T21/T24/T27) at a window this
  poorly conditioned. No error bar accompanies either `amp_ratio` reading in
  §4's bands, so the 0.116/0.050 thresholds are compared against bare point
  estimates. This compounds the aliasing concern above rather than
  standing alone as the sharpest issue, since both point the same
  direction: the cycle's single 600nm/36–42° window cannot, on its own,
  certify that an (a)-type "ABSORB-tied" reading is a real, generalizable
  boundary-depth effect rather than a narrow-window/aliased-λ artifact.

## Verdict: support-with-changes

The instrument's construction is sound — geometry congruence, the static
identity gate, and the `G0-e` recovery check all independently verify
correctly, and the cycle is honest about the significance-testing route it
deliberately avoids (R7/seventh-cycle compliance, §7). What is missing is not
a redesign but a cheap generalization check: as specified, a clean §4(a)
"ABSORB-tied" verdict from this cycle alone would be indistinguishable from
an artifact specific to the 600nm/even-integer-λ condition every config this
cycle runs happens to share.

**Single parameter change that would flip this to plain support:** add one
cheap second-wavelength leg for `G40` (450nm or 750nm, where 40/15=2.667λ and
80/15=5.333λ — neither integer — reusing exp-065's own 6-angle `SWEEP_ANGLES`
subset rather than the full 31-angle dense grid, ≈6 extra FDTD calls) to test
whether `PAIR_ABSORB40`'s qualitative reading survives away from the aliased
600nm condition, before any (a)/(b) verdict from this cycle is cited forward
as wavelength-general.
