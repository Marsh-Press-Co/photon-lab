# PHASE 5 — REVIEW · Seat: THERMODYNAMICS · Panel Iteration 68 · exp-091

Fresh sub-agent, blind to any other seat's current-cycle Phase-5 review.
Read in full: `PANEL.md`; `LOGBOOK.md` in full (RULED OUT R1–R14 with R13/R14's
complete founding text, ESTABLISHED, LIVE THREADS/T28 history through
Iteration 67/exp-090, both CHECKPOINT entries); the complete exp-091 record
(`phase1_proposal.md`, all five Phase-2 critiques, `phase2_redteam_audit.md`,
`phase3_synthesis.md`, `NOTES.md`, `run.py`, `run_output.txt`, `results.json`);
`experiments/087–090`'s `NOTES.md` and `phase5_redteam_audit.md` for context;
`lab/thermo_sidecar.py` in full. I have zero memory of critiquing this cycle
at Phase 2 — that critique (`phase2_critique_thermodynamics.md`) is read here
as a finished document belonging to a different, now-closed agent, exactly
like any other seat's.

## Verdict: **CONCUR with PARTIAL, on the energy-ledger axis — with one
load-bearing methodological gap I am elevating for Iteration 69.**

Every `p_abs_w`/`frac_p_abs`/`ratio_k` number in `results.json` that I
independently recomputed from raw primitives — not from `run.py`'s own
printed arithmetic — reproduces exactly. My own Phase-2 demand (a co-equal
`frac_p_abs(θ,cpl=30)` vs. `frac_p_abs(θ,cpl=20)` PRIMARY prediction) was
adopted verbatim as (b2) and CONFIRMs cleanly at all three angles. That is a
genuine, load-bearing methodological win: `frac_p_abs` — architecturally the
same R14 numerator-hazard class as the very construction that motivated my
critique — now has real cross-resolution evidence behind it, where before
this cycle it had none. But "CONFIRM" is not the same claim as "resolution-
invariant," and the CONFIRM band itself (`[0.3,3.0]`) is wide enough to hide
a real, systematic, mechanistically-traceable effect: `frac_p_abs` does not
scatter around 1.0× at finer resolution, it **grows** at finer resolution,
at all three sampled angles, by a factor that itself varies 2.5× angle to
angle (1.12×–2.78×). I trace this below to a real, small, well-behaved
resolution-dependence in the underlying absorbed-power primitive (`p_abs_w`,
for both the C40 and G40 configs individually) that is fully consistent with
reduced staircasing of the graded absorber's curved boundary at finer `Δx`
— not noise, and not evidence against the CONFIRM verdict — but it means
`frac_p_abs` should be read as "classification-stable across these two
specific resolutions," not "a converged, resolution-independent quantity,"
and a coarser-resolution `p_abs_w` should not be cited as the settled value
of that primitive going forward.

## 1. Independent re-derivation of `p_abs_w` from raw primitives (not `run.py`'s own arithmetic)

**1a. Internal consistency check: `frac_p_abs`/`ratio_k` from `results.json`'s
own `p_c`/`p_g` fields, recomputed by hand.** Pulling `raw.native_leg1_cpl20_steps4200`
and `raw.r3_leg2_cpl30_steps4200` directly:

| θ | leg | p_c (W) | p_g (W) | p_g−p_c | frac_p_abs = \|p_g−p_c\|/p_c (mine) | filed |
|---|---|---|---|---|---|---|
| 37.2° | cpl20 | 2.812726e-12 | 2.808679e-12 | −4.046228e-15 | 1.438543e-03 | 1.438543e-03 ✓ |
| 37.2° | cpl30 | 2.909923e-12 | 2.898304e-12 | −1.161898e-14 | 3.992880e-03 | 3.992880e-03 ✓ |
| 40.2° | cpl20 | 3.077219e-12 | 3.055371e-12 | −2.184828e-14 | 7.100007e-03 | 7.100007e-03 ✓ |
| 40.2° | cpl30 | 3.187660e-12 | 3.162362e-12 | −2.529763e-14 | 7.936113e-03 | 7.936113e-03 ✓ |
| 41.4° | cpl20 | 3.164978e-12 | 3.187847e-12 | +2.286916e-14 | 7.225692e-03 | 7.225692e-03 ✓ |
| 41.4° | cpl30 | 3.282666e-12 | 3.314142e-12 | +3.147596e-14 | 9.588537e-03 | 9.588537e-03 ✓ |

Ratios `frac_p_abs(cpl30)/frac_p_abs(cpl20)`, computed independently from the
table above: `3.992880e-3/1.438543e-3 = 2.77564`; `7.936113e-3/7.100007e-3 =
1.11776`; `9.588537e-3/7.225692e-3 = 1.32701` — matching (b2)'s filed `2.7756,
1.1178, 1.3270` to every printed digit. Sign of `(p_g−p_c)` matches at every
angle across resolutions (−,−,−,− at 37.2°/40.2°, +,+ at 41.4°), confirming
(b2)'s `sign_match=True` at all three. **No arithmetic error anywhere in this
chain.** `ratio_k` cross-checked the same way (`frac_p_abs/frac_contrast`,
using (a)'s own filed `frac_contrast` values) also reproduces (b)'s table
exactly — e.g. 41.4°, cpl30: `9.588537e-3/1.040919e-3 = 9.21158`, matching
the filed `9.2116` and confirming the CONSISTENT reclassification is not a
rounding artifact.

**1b. The primitive one level down: `sigma_ext`/`ratio_abs_ext` are NOT
recoverable from this cycle's `results.json` — disclosed, and worked around.**
I searched the full committed JSON for `sigma_ext`, `sigma_abs`, and
`ratio_abs_ext` — none appear. `run.py` computes them (`ba["sigma_ext"]`,
`ba["sigma_abs"]` at `sc.widths_direction_corrected(...)`, `run.py:390–406`)
but the pipeline persists only the derived `p_c`/`p_g`/`frac_p_abs`/`ratio_k`
outputs, not the intermediate box-ledger fields — a real, if minor, gap
worth naming forward (see §4). Lacking the exact primitive, I built an
independent **estimate**, disclosed as such: `thermo_sidecar.py`'s own
formula is `p_abs_w = I_incident_w_cm2 · (sigma_ext_cells·dx_m)² · 1e4 ·
ratio_abs_ext`, with `IRR_CENTRAL_W_CM2 = 6.584362139917695e-06` a fixed
constant used identically at both `cpl` values (confirmed from
`run.py:165`/`exp087.IRR_CENTRAL_W_CM2` — this quantity is NOT itself
resolution-rescaled). Inverting with T9's own established, R14-confirmed
flat `ratio_abs_ext ≈ 0.51` anchor (Iteration 64/65's own finding: this
ratio holds to <0.1% across angle and across the C40/G40 pair on this exact
channel) gives an implied physical extinction width for `p_abs_w(C40,θ)` at
each angle:

| θ | width_m (cpl20, Δx=30nm) | width_m (cpl30, Δx=20nm) | width ratio | implied `p_abs_w` growth |
|---|---|---|---|---|
| 37.2° | 9.1521 µm | 9.3089 µm | 1.01713 | +3.456% |
| 40.2° | 9.5728 µm | 9.7430 µm | 1.01779 | +3.589% |
| 41.4° | 9.7083 µm | 9.8872 µm | 1.01842 | +3.718% |

(`sigma_ext_cells` implied: 305.1→465.4 cells at 37.2°, 319.1→487.2 at 40.2°,
323.6→494.4 at 41.4° — consistent with `sigma_ext_cells·Δx` converging on
the same ~9.2–9.9 µm physical width at both resolutions, as it must if the
object's real geometry is being measured rather than a grid artifact.)
**Reading, disclosed as an estimate under the fixed-`ratio_abs_ext` assumption,
not a measurement**: refining the grid grows the object's own measured
absorbed power by a small, nearly angle-independent ~3.5–3.7% at every one
of the three census angles — this is the base-quantity behavior `frac_p_abs`
is built on top of, and it is a mundane, well-behaved, monotonic-with-`Δx`
effect, not an erratic one.

## 2. Mechanistic reading: why `frac_p_abs` grows everywhere, and why that does not undercut the (b2) CONFIRM

The panel's framing question deserves a direct answer: **this is a real,
disclosed, worth-noting mechanism, and it does NOT fully vindicate
`frac_p_abs` as a resolution-*invariant* quantity — only as a
resolution-*stable-enough-for-classification* one, which is a narrower and
more honest claim.**

Decomposing `frac_p_abs(θ) = |p_g(θ)−p_c(θ)|/p_c(θ)`: `p_c` (the C40
reference article's own absorbed power) grows by a nearly constant
**+3.46% to +3.72%** across all three angles when the grid is refined
20→30 (§1b) — small, uniform, and exactly the size and direction (increase)
expected from **reduced staircasing of the graded-shell's curved absorbing
boundary**: a coarser Cartesian grid under-resolves a curved/graded
interface, systematically under-sampling the true absorbing path length at
oblique cuts through the coating, and refining the grid recovers more of it.
This is a well-understood, textbook FDTD discretization effect for curved
dielectric/lossy boundaries, not specific to this bench or this program.

But `|p_g−p_c|` — the small **difference** `frac_p_abs`'s numerator is built
from — grows far faster than that ~3.5% base drift: **+187% at 37.2°
(2.872×), +16% at 40.2° (1.158×), +38% at 41.4° (1.376×)**, recomputed
directly from Table 1a. Dividing by `p_c`'s own modest ~3.5% growth
(denominator, not numerator, of `frac_p_abs`) attenuates these slightly to
the filed 2.78×/1.12×/1.33× — but the *dominant* source of `frac_p_abs`'s
growth is squarely in the numerator's differential term, not the shared base
drift. This is exactly R14's own diagnosis, applied for the first time to a
resolution change rather than an angle-sampling change: a small-difference-
over-base construction takes a modest, mechanistically mundane, nearly
angle-independent ~3.5% base-quantity shift and turns it into a 12%–178%
apparent swing in the constructed ratio, because C40 and G40 do not have
*identical* curved-boundary staircasing corrections (they differ in `pad`,
hence in exactly how much curved/graded boundary each geometry exposes) —
so the two configs' own ~3.5%-scale corrections do not cancel when
differenced, and the residual, while individually small in absolute
absorbed-power terms, is large relative to the already-small `|p_g−p_c|` it
is built from.

**Answering the panel's question directly**: yes, mechanistically, absorbed
power in this graded sponge shell plausibly does increase systematically at
finer grid resolution, for the ordinary reason offered (reduced staircasing)
— my own estimate in §1b (+1.7–1.8% in the implied physical extinction
width, ~+3.5% in `p_abs_w` since power scales as width²) is consistent with
that reading and is the same size and direction at all three angles, which
is itself evidence for a shared, geometry-driven mechanism rather than
angle-specific new physics. That same base effect, filtered through R14's
own named construction hazard, is sufficient to explain the observed
1.12×–2.78× `frac_p_abs` growth without invoking anything angle-specific —
consistent with, not contradicting, PHOTONICS'/EM's/QUANTUM's own likely
readings of the same numbers. **The correct combined statement for the
record**: `frac_p_abs` survives (b2)'s CONFIRM band at this cycle's two
tested resolutions — a real, useful result, and a stronger cross-resolution
result than `frac_contrast` achieved (below) — but it is not evidence that
`frac_p_abs` itself has converged. A `cpl=40` or `cpl=45` check on the same
channel would, on this reading, be expected to show **further growth in the
same direction**, not oscillation around the `cpl=30` value — because the
underlying staircasing-reduction mechanism has not yet saturated at
`cpl=30` any more than it had at `cpl=20`. A future cycle citing `frac_p_abs`
as a precisely-measured number (rather than "CONFIRMed within [0.3,3.0] at
two resolutions") would be over-reading this result.

## 3. Post-run energy sidecar: min and max `p_abs_w` in this dataset (Expressibility contract: post-run analytic, not an FDTD output)

Scanning all 20 `(config,θ,steps)` cells' `p_c`/`p_g` values in `results.json`
for the extremes: **min = 2.808679×10⁻¹² W** (G40, native `cpl=20`, θ=37.2°);
**max = 3.347664×10⁻¹² W** (G40_R3, `cpl=30`, θ=41.6°, bracket leg — the
single largest absorbed-power reading in this entire 40-call dataset,
arising specifically from the finer-resolution leg, consistent with §2's
growth direction). Running both through `lab/thermo_sidecar.py`'s own
`mixed_length_scale_regime` → `netd_disposition` chain, `l_geometric_m
=2.34×10⁻⁶` m (identical at both resolutions by the R3 rescale's own
construction, `run.py:174`'s assertion), and exp-087's own sourced constants
(`k_air=0.026`, `ρ=2330`, `c_p=700`, `ε=0.9`, `T_amb=293.15` K,
`NETD_BAND_K=(0.020,0.050)`):

| | p_abs_w | dt_ss_full_K | τ_thermal | NETD classification | margin below NETD floor |
|---|---|---|---|---|---|
| MIN | 2.808679×10⁻¹² W | 4.6144×10⁻⁵ K | 3.433×10⁻⁴ s | UNDETECTABLE | 433× |
| MAX | 3.347664×10⁻¹² W | 5.4999×10⁻⁵ K | 3.433×10⁻⁴ s | UNDETECTABLE | 364× |

Wien peak wavelength at `T_amb+ΔT` is **9.884938 µm** at both endpoints
(ambient-alone peak: 9.884939 µm) — the absorbed-power-driven shift in the
emission peak is unmeasurable at this scale, six significant figures deep
into the LWIR band, itself an independent confirmation of how small these
temperature rises are.

**Reading, plainly**: this cycle's own finest-resolution, largest-magnitude
`p_abs_w` value — the single number in this entire dataset that resolution
refinement moved furthest from its coarse-grid counterpart — still sits
**364× below** the sourced microbolometer NETD floor, comfortably inside
the same 374×–442× order-of-magnitude margin exp-087 established for this
identical article at native resolution, and orders of magnitude short of
the 52,000×–225,000× swing-specific margin THERMODYNAMICS' own Iteration-64
Phase-5 review computed for the *fractional* absorbed-power swing at that
cycle's energy-dominant point. Nothing in this cycle's resolution-driven
`p_abs_w` growth comes remotely close to disturbing that verdict. **This
remains firmly in the "far below any detectable re-radiation" regime this
program established at Iteration 64 and has not moved since** — the
resolution question this cycle answers is an instrument-trust question, not
a new detectability question, and it does not reopen one. (Idealizations
3/6/7 apply throughout this section: NETD is an instrument/detector
threshold, not a human-eye one; this bears on neither constraint 3 nor 4.)

## 4. On the PRIMARY REFUTE and the classification instability — from the energy-ledger side, not competing with the ambient-channel diagnosis

I defer the mechanistic diagnosis of *why* `delta_scene`/`frac_contrast`
sign-flip and reclassify to the seats that own that instrument (PHOTONICS,
QUANTUM, EM) — that is not my charter. What IS my charter is confirming
that the (b) classification swing at 40.2°/41.4° is **not** an energy-ledger
artifact masquerading as an ambient-channel one: `p_abs_w`/`frac_p_abs`
(my own numerator) moved by only 1.12×–1.33× at those two angles (§1a) —
small, smooth, mechanistically explained (§2) — while `frac_contrast` (the
denominator, someone else's instrument) moved by 2.78×–4.16× and, at 40.2°,
**flipped sign outright** (`delta_scene`: −1.543×10⁻⁴ at cpl20 → +4.370×10⁻⁴
at cpl30). The (b) swing is overwhelmingly a denominator-side story,
consistent with the R13 lineage exp-089 already established for the
angle-sampling version of this same instability, now demonstrated for the
first time to also apply across *resolution*, not just across angle. My own
number is the well-behaved half of this cycle's result, and I want that
stated plainly rather than left to be inferred: **`frac_p_abs`'s good
behavior this cycle is real evidence that the numerator-side R14 hazard is
under control on this specific channel; it is not evidence that R13's
denominator hazard is under control, and nothing in this cycle closes that
question.**

One structural observation I want on the record for whichever seat
formalizes it: (a2)'s own result — that neither bracket pair
(40.2°/40.4°, 41.4°/41.6°) shows a sign change at `cpl=30`, even though both
brackets straddle a real, `p=0.0`-null-controlled `cpl=20` zero-crossing —
means the crossing itself did not merely *shift* by a resolvable amount
within the bracket; it moved **outside** the bracket entirely (at 40.2°, the
value flipped from negative to positive at the very point that used to sit
on the crossing's negative side). If R13's floor gate is meant to protect
against classifying near a *known* zero-crossing, and the crossing's own
measured location is this sensitive to grid resolution, R13's own
presupposition — that the denominator's zero-crossing is a fixed, knowable
feature of the underlying continuum problem, only needing to be avoided at
one resolution — deserves an explicit re-examination. That is not a finding
I can resolve from the energy-ledger side, but it materially bears on how
much weight either resolution's (b) classification should be given at
40.2°/41.4°, and I flag it forward rather than silently assume PHOTONICS/
QUANTUM will independently surface the same reading.

## 5. Ranked top-3 candidate directions for Iteration 69

1. **Persist `sigma_ext_cells`/`ratio_abs_ext_raw` into `results.json` for
   every `thermo`-chain cell, going forward on this channel.** Zero
   marginal FDTD cost (both are already computed in `run.py`'s live process,
   just not serialized) — this closed a real, if minor, verification gap I
   hit directly (§1b): without them, a from-primitives re-derivation of
   `p_abs_w` has to invert the sidecar formula under an assumed
   `ratio_abs_ext`, rather than checking it directly. This would also let a
   future cycle test §2's own prediction (`ratio_abs_ext` should stay
   T9-flat across `cpl`, while `sigma_ext_cells·Δx` should converge slightly
   upward) without a fresh FDTD run.
2. **A `cpl=40` (or denser) third resolution point on the same C40/G40
   channel, at minimum 40.2°/41.4°, explicitly to test §2's own directional
   prediction** — that `p_abs_w` continues to grow (not oscillate) with
   further refinement, and by how much the growth rate itself is slowing
   (a genuine convergence check, which this two-point cycle cannot itself
   provide: two points establish a direction, not a limit). This would
   upgrade `frac_p_abs`'s status from "CONFIRMed at two resolutions" to
   "converging," which is the claim any future citation of this quantity as
   a stable primitive actually needs.
3. **Re-examine R13's own floor-gate presupposition given (a2)'s finding
   that a real `delta_scene` zero-crossing can shift clean out of a
   0.2°-wide bracket under a `cpl` refinement that left the *ambient*
   channel's own `C_empty`/`C` values agreeing to <0.02%** (§(c1)/(c2)
   above, all-CONFIRM). If the crossing location itself is this
   resolution-sensitive while the underlying field data is this
   well-converged, R13's framing of "avoid classifying near a known,
   fixed crossing" may need a resolution-dependence clause of its own —
   a governance question for whichever seat (PHOTONICS/QUANTUM/EM) owns
   the ambient-channel instrument, named here because it bears directly on
   how much confidence any future `ratio_k` reading at 40.2°/41.4°, at any
   resolution, should be given.

Also still open, unrelated to this cycle's own deliverable: PHOTONICS' still-
overdue grazing-incidence validity check (the single most-repeated item on
the whole T28 board); the x-wall wavelength-generality leg (now sixteen-plus
consecutive cycles deferred); R14(b)'s still-queued formal null-controlled
period fit against the raw signed `p_abs(G40,θ)−p_abs(C40,θ)` difference —
which this cycle's own §2 decomposition (a shared, angle-independent
staircasing base-drift plus a config-differential residual) may now make
cheaper to formalize than before, since the base-drift term looks like it
can be estimated and subtracted first.
