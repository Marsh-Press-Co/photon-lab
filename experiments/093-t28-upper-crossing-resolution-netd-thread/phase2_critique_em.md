# PHASE 2 — CRITIQUE · ELECTROMAGNETISM (blind) · exp-093 · Panel Iteration 70

*Fresh sub-agent, ELECTROMAGNETISM charter. Read in full: PANEL.md;
LOGBOOK.md (RULED OUT R1–R15, LIVE THREADS, T28 history through
Iteration 69/exp-092); `experiments/093-.../phase1_proposal.md`;
`experiments/092-.../NOTES.md`, `results.json`, `phase5_review_em.md`,
`phase5_redteam_audit.md` §5/§7–8; `experiments/091-.../phase5_review_em.md`;
`lab/fdtd2d.py::Sim.__init__`. Independently traced `design_geometry.py`'s
`R3_CONFIGS`/`r3_config()` and `experiments/077-t28-pad-round-trip-echo-
model/phase1_proposal.md` (the origin of the cited echo model) directly
from source, not from this proposal's own characterization of them. Blind
to every other seat's current critique.*

## Verified against source before critiquing

`courant_frac=0.99` → `S = 0.99/√2 = 0.700036` reproduces exactly
(`lab/fdtd2d.py:78`) — §7's Courant-number citation is correct, not taken
on faith. `design_geometry.py::r3_config`/`R3_CONFIGS` confirms `C40_R3`
has `pad=0`, `G40_R3` has `pad=60` (native `G40` `pad=40` vs `C40` `pad=0`)
— the PAD-differential claim (native 40, R3 60, round-trip 80/120) is
geometrically accurate. `delta_scene = c_g − c_c` (`run.py:441`) confirms
this channel *is* a `G40−C40` config differential, so a length scale tied
to what actually differs between the two configs is not an arbitrary
choice on its face.

## Steel-man (≤150 words)

The proposal's strongest EM-side merit is that it finally *computes* the
twice-deferred check rather than arguing it a third time, honestly
discharging the shape of obligation R8 exists to enforce. The 2D Yee
dispersion relation is correctly stated for TMz on a Cartesian grid at
this bench's own `S`, the `θ↔90°−θ` symmetry is independently verified
(not merely asserted) to 12 significant figures — a genuine unit/sanity
check in R9's own spirit — and both `ΔΔφ` and `P*` are expressed in
degrees before the ratio is taken, so the mapping is dimensionally
consistent as far as unit-bookkeeping goes. Tying the length scale to
`PAD` — the one geometric quantity that actually differs between `C40`
and `G40`, the exact pair `delta_scene` subtracts — is the right
*instinct*: dispersion accumulated over the aperture length common to
both configs would largely cancel in the subtraction, so restricting
attention to the differential path is not an arbitrary or searched
constant (R5 correctly does not fire).

## Sharpest attack (≤150 words)

The chosen length scale is wrong, and its own citation undercuts it.
My seat's founding argument (exp-091 `phase5_review_em.md` §4(i), restated
exp-092 self-review) named the **aperture propagation length**
(A≈752–1128 cells, "tens of wavelengths") as where dispersion phase
accumulates — not `PAD`. Item 4 substitutes `ℓ=2×PAD` (80–120 cells,
~10× shorter) with no reconciliation. Worse: it cites "this bench's own
established `pad_round_trip_echo_model`, exp-077" as physical grounding —
but exp-077 **REFUTED** that exact coherent-echo-on-the-PAD-path
mechanism against the real `PAIR_PAD` `delta(θ)` signal (shape `r²=
0.0001`, four orders of magnitude off, under the complete two-wall
accounting exp-077 itself adopted as final; period test only reached
INCONCLUSIVE at best). A length scale this program's own record already
showed does **not** govern this channel's real interference structure is
being used to REFUTE a *different* candidate mechanism. That tests a
strawman, not the mandate ("this exact aperture/propagation geometry").
R8's third-citation tripwire is not actually discharged by this
computation as scoped.

## Secondary point (flagged per task brief, not the primary attack)

The `Δθ=(ΔΔφ/360°)×P*` mapping assumes the local waveform near each
crossing is a simple sinusoid at the macro period `P*=2.8421°` — a
reasonable approximation at the isolated lower crossing, but a poor one at
the upper near-null, which exp-092's own record (§3 of my prior-cycle
self-review) describes as a sharp, `0.057°`-wide near-tangency nested
*inside* the macro period, qualitatively unlike a smooth `P*`-period
sinusoid. The true local `dθ/dφ` slope there could differ substantially
from `P*/360°` in either direction. This should be measured from the
newly-collected item-1 off-grid data (a local finite-difference slope of
`delta_scene(θ)` at the two crossings) rather than assumed from the macro
period, at least as a disclosed cross-check — the proposal states this
mapping without flagging that its own governing assumption is weakest
exactly where the mandatory check most needs to be trusted (the upper
window).

## Branch-gating check (item 3 → item 1's `sigma_max`)

No energy-coupling inconsistency found. The branch logic (CONFIRM→native,
REFUTE/NEITHER→corrected `1/3`, both disclosed against comparability to
the native-sigma flanking anchors) mirrors exp-092's own Rank-3→Rank-1
precedent exactly, and `sigma_max` enters `graded_black_shell` as a
genuine linear conductivity multiplier (verified in `materials.py` by
exp-092's own EM self-review, not re-litigated here) — a passive-medium
parameter throughout either branch; nothing here risks non-passivity.

## Verdict: **support-with-changes**

The five-item design is otherwise procedurally sound (sequencing,
determinism argument for item 5, R1–R15 accounting) and I have no EM
objection to items 1/2/3/5 as scoped. Item 4 as computed does not, in my
judgment, actually discharge the twice-deferred, Red-Team-elevated
mandatory check — it answers a related but different question at the
wrong length scale, built on a citation that this program's own record
already refutes as the operative mechanism for this exact channel. This
is squarely my seat's charter (formalizing what the T1/energy-coupling
bookkeeping does and does not license), so I do not defer it.

**Single change that would flip me to full support:** recompute §7 a
second way, using `ℓ=A` (the aperture propagation length, ≈752/1128
cells, per my own seat's founding argument) alongside the existing
`ℓ=2×PAD` result, report both side by side, and explicitly disclose the
exp-077 REFUTE precedent for the PAD-echo length choice rather than
citing it as unqualified support. If the aperture-length version *also*
lands in the "orders of magnitude too small" range, the REFUTE conclusion
strengthens (two independent length scales agree) and I support outright;
if it does not, that is itself the more important finding this mandatory
check was supposed to surface.
