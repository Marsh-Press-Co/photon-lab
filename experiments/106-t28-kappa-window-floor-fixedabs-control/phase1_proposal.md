# Phase 1 Proposal — exp-106: Floor-Gating, Settling, Risk-Propagation, and the Fixed-Absolute-Thickness Control for `kappa_window`

**Panel Iteration 83. Lead seat (rotation): QUANTUM OPTICS.** Executes
exp-105's own Reconciled Iteration-83 queue, Tier 1 items 1–4 in full
(Red Team's own final-audit tiered ranking, `NOTES.md` §Next, itself
sourced from `phase5_redteam_audit.md` §7). Instrument-extension cycle,
diagnostic only — **T1: N/A**, exactly as exp-102/103/104/105 were.

## 1. Mechanism narrative (≤300 words)

This is **not** a mechanism proposal. No σ(I), σ(x,t), angular-selective,
or any other constraint-1/2/3-relevant material law is introduced or
varied this cycle. This is pure instrumentation/diagnostic work closing
four specific gaps Red Team's Phase-5 final audit found in exp-105:

1. `kappa_window`/`window_stats()` has **never been floor-gated at any
   r** in this program's history, unlike its sibling `dense_x` channels
   — and r=312's own `wide_channel`/`point_channel` per-x scalars were
   computed in memory but never persisted, unlike r=156's.
2. `kappa_window` has never had its own **settling-independence leg**
   (exp-105's settling leg covered `kappa_region_point`/`delta_phi_point`
   only) — most urgently at r=312, which already carries a MARGINAL
   Nyquist tier.
3. P3's headline number (`shape_ratio=19.79`) is a **rawer, less-
   residualized read** of the identical MARGINAL-tier r=312 capture than
   P4 gets — P4 has `p4_156_trusted`; P3 has no symmetric gate at all.
4. A genuine, previously unconsidered alternative mechanism exists:
   holding `tau_shell` fixed while `R_CORE`/`R_COAT` scale by κ forces
   the self-similar coating's own **electrical thickness to grow 4×**
   (2.4λ→9.6λ) across the r=78/156/312 family — a materials confound,
   not the pure geometric-window (z/z_R) effect the bridge was built to
   isolate. exp-052's already-built, zero-new-mechanism fixed-absolute-
   thickness variant (constant 2.4λ coating at every r) is the
   discriminating control, never yet run on this channel.

Closing all four lets P3's own accelerating-collapse finding
(shape_ratio=19.79, kappa_window falling ~1,100× across r=78→156→312)
finally be **TRUSTED or REFUTED** as physics, rather than merely
SCORED-BUT-CAVEATED, which is where exp-105's Phase 5 left it. No new
`lab/` diff. No σ(I)/σ(x,t)/angular-selectivity machinery is built or
varied — QUANTUM OPTICS' own charter contract (mechanisms enter only as
effective classical parameters, or Red Team strikes them) is satisfied
vacuously this cycle: there is no mechanism to express.

## 2. Parameter table

### 2a. Self-similar family — reused verbatim from exp-105's `geom(r)`

Every number below is reproduced by executing the actual formula chain
(`kappa_of`, `geom`), not hand-typed — the same discipline exp-105's own
`run.py` enforces (mandatory fixes 1/2 there, after two prior hand-typo
incidents in this exact sub-thread).

| r | κ | N | CX | CY | SRC_X | STEPS (1×) | STEPS (2× settling) | R_CORE | sigma_max | tau_shell | thickness (cells / λ) | behind window | z/z_R | predicted_ripple_period | nyquist_margin | tier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 78 | 1.0 | 560 | 252 | 280 | 64 | 3200 | (n/a, reused) | 30 | 0.500 | 24.0 | 48 / 2.4λ | (357,457,260,300) | 0.253123 | 19.744 | 4.936 | TRUSTED |
| 156 | 2.0 | 1120 | 504 | 560 | 128 | 6400 | 12800 | 60 | 0.250 | 24.0 | 96 / 4.8λ | (687,787,540,580) | 0.063281 | 9.872 | 2.468 | TRUSTED |
| 312 | 4.0 | 2240 | 1008 | 1120 | 256 | 12800 | 25600 | 120 | 0.125 | 24.0 | 192 / 9.6λ | (1347,1447,1100,1140) | 0.015820 | 4.936 | 1.234 | MARGINAL-REDUCED-CONFIDENCE |

`dense_x`, `DENSE_PITCH=2`, `H_REGION_WIDE=5`, `H_REGION_POINT=0`,
`FLOOR_FRAC=0.10` unchanged (exp-105's own established values, reused
byte-for-byte). Window box size is **fixed in cells across r**
(100×40=4,000 cells) — the `D_EFF=77`-cell offset convention means the
per-cell floor-gate array (§2c) is small and cheap to persist in full at
every r, no approximation needed.

### 2b. Fixed-absolute-thickness family — exp-052's `design_geometry.py` formulas, applied to the beam geometry, generalized to r=156/312 (nothing invented — exp-052 already has these formulas; this cycle only applies them to the new channel and new r-points)

Domain construction (N, CX, CY, SRC_X, STEPS, behind window, dense_x) is
**identical** to §2a at the same r — only the object's material law
(R_CORE, sigma_max) differs, isolating the thickness-growth-law question
from any domain-construction confound (the same isolation discipline
exp-052 itself was built to enforce, R_CORE-fixedabs from `r_in_fixedabs(r)
= r - ABS_THICKNESS`, `sigma_max_fixedabs(r) = SIGMA_MAX_FIXED`, both
constants imported unchanged: `ABS_THICKNESS=48`, `SIGMA_MAX_FIXED=0.5`).

| r | R_CORE (fixed-abs) | sigma_max (fixed-abs) | tau_shell | thickness (cells / λ) | coincides with self-similar? |
|---|---|---|---|---|---|
| 78 | 30 | 0.500 | 24.0 | 48 / 2.4λ | **YES — identical object, 0 new calls** |
| 156 | 108 | 0.500 | 24.0 | 48 / 2.4λ | No (self-similar R_CORE=60, thickness 4.8λ) |
| 312 | 264 | 0.500 | 24.0 | 48 / 2.4λ | No (self-similar R_CORE=120, thickness 9.6λ) |

At r=78 the two families are the *same object* (`R_CORE=30`,
`sigma_max=0.5` in both) — this is the anchor point, verified by the
same printed-assertion pattern exp-052 already uses
(`r_in_fixedabs(78)==r_in_selfsim(78)==30`,
`sigma_max_fixedabs(78)==sigma_max_selfsim(78)==0.5`), so the fixed-abs
family's own r=78 `kappa_window` is **reused** from
exp-103's established value (0.018336958179764707) — 0 new FDTD calls.
At r=156/312 the families diverge: self-similar's coating keeps growing
electrically thicker (4.8λ→9.6λ) while fixed-abs holds it at a constant
2.4λ — this divergence *is* the control.

### 2c. Floor-gate design for `window_stats()`'s own output (concrete function, reusing `floor_gate()` verbatim)

`window_stats()` currently returns only `mean/std/min/max` of the window
box, discarding the per-cell array — the load-bearing gap Tier-1 item 1
names. Fix: because the window box is fixed at 4,000 cells across every
r (§2a), persisting the full per-cell array is cheap (≈32KB float64 per
box, negligible against `results.json`'s existing size), so no lossy
summary construction is needed:

```python
def floor_gate_window(ez_empty, x_lo, x_hi, y_lo, y_hi, label, floor_frac=FLOOR_FRAC):
    """Floor-gates window_stats()'s own per-cell intensity block, by
    reusing floor_gate() verbatim (R4) rather than inventing a new
    statistic. Operates on the EMPTY-scene capture only, matching this
    file's own established convention: floor_gate() is always called on
    the empty-scene reference (i_e_*), never the article-scene numerator
    — the question is whether the DENOMINATOR of kappa_window sits above
    the solver's own numerical noise floor, not whether the article
    signal does."""
    block_e = np.abs(ez_empty[x_lo:x_hi, y_lo:y_hi]) ** 2
    return floor_gate(block_e.ravel().tolist(), label, floor_frac=floor_frac)
```

Called once per (r, family) at the `behind` window coordinates already
computed by `geom(r)`. The persisted record adds, per (r, family):
`window_floor_gate` (the `floor_gate()` return dict: rms, floor,
n_unresolved, and now `frac_unresolved = n_unresolved/4000`) **plus the
full raveled empty- and article-scene per-cell arrays themselves**
(`window_block_empty`, `window_block_article`) — so a future cycle can
recompute or re-derive any statistic without a fresh FDTD call. This
also closes item 1's second half (r=312's `wide_channel`/`point_channel`
per-x scalars, currently computed but discarded): the same fresh r=312
capture this cycle already needs (for the window floor-gate) is reused,
at zero marginal cost, to persist those dicts the same way r=156's
block already does.

Getting the per-cell array requires a **fresh capture** — raw `Ez`
fields were never written to `results.json` (only derived scalars), so
this is not a free post-hoc analysis on exp-105's already-run data. Each
fresh capture reproduces an already-known aggregate scalar
(`kappa_window_156=8.867e-4`, `kappa_window_312=4.793e-6`) as a **free
Gate-P1-style reproduction check**: if the freshly captured
`window_stats()` mean-ratio does not match exp-105's committed value to
<1e-6 relative, halt before trusting the new floor-gate diagnostic built
on the same fields.

### 2d. Settling-independence leg on `kappa_window` itself

Reuses `STABILITY_TOL=0.20` (exp-103's established tolerance; no
phase-based check is added here — `window_stats()` only ever pools
`|Ez|²`, never a complex mean, so there is no `delta_phi_window` to
settle-check, unlike the point/wide channels' `delta_phi_*`):

```python
def settling_pass_window(kappa_1x, kappa_2x, tol=STABILITY_TOL):
    rel_change = abs(kappa_2x - kappa_1x) / abs(kappa_1x) if kappa_1x != 0 else float("inf")
    return rel_change <= tol, rel_change
```

Applied at r=156 and r=312, for **both** families (self-similar and
fixed-abs), using the doubled-STEPS pair each leg already needs anyway
(§2e). No new tolerance is proposed — reusing `STABILITY_TOL=0.20`
without modification, per the instruction, since nothing here changes
the physical settling-time argument that tolerance was calibrated
against.

### 2e. Exact FDTD call budget — 16 new `Sim.run()` calls total

r=78 is reused in **both** families (0 new calls, per §2a/§2b). Every
other cell below is a real, new call:

| Leg | Family | r | STEPS | Calls (empty+article) | Purpose |
|---|---|---|---|---|---|
| 1 | self-similar | 156 | 6400 | 2 | floor-gate window_stats + item-1 persistence + Gate-P1-style reproduction of `kappa_window_156` |
| 2 | self-similar | 156 | 12800 | 2 | settling leg on `kappa_window` (item 2) |
| 3 | self-similar | 312 | 12800 | 2 | floor-gate window_stats + item-1 persistence + reproduction of `kappa_window_312` — **cost-gated, piloted** |
| 4 | self-similar | 312 | 25600 | 2 | settling leg on `kappa_window` (item 2, "more urgent" per queue) — **cost-gated, piloted** |
| 5 | fixed-abs | 156 | 6400 | 2 | primary pair, floor-gated from the start (item 4 reusing items 1–3) |
| 6 | fixed-abs | 156 | 12800 | 2 | settling leg, from the start |
| 7 | fixed-abs | 312 | 12800 | 2 | primary pair, floor-gated — **cost-gated, piloted** |
| 8 | fixed-abs | 312 | 25600 | 2 | settling leg — **cost-gated, piloted** |

**Total: 16 real FDTD calls** (8 self-similar + 8 fixed-abs; r=78
contributes 0 to both families). Item 3 (the `p3_trusted` risk-
propagation gate) and the `delta_scene` Tier-3 write-up (§5) are
**zero-cost logic/prose** — no FDTD calls of their own.

**Sequencing (cheapest/most load-bearing first, so a hard budget wall
defers the least-important legs, not the most):** Legs 1→2→5→6 (all
r=156, cheap) run first; the four r=312 legs (3, 4, 7, 8) run last, each
individually cost-gated. This means if the cycle's wall-clock budget is
exhausted, item 4's r=312 half (legs 7–8) — explicitly the lowest-
ranked of the four Tier-1 items — is what gets deferred, not items 1–3's
own r=156 diagnostics or the r=78 zero-cost anchor checks.

**Cost-gating rule, reused from exp-105's own precedent (pilot the first
call of each new r=312 leg, independently):** abort a leg if its first
call exceeds 90 minutes, or if the projected 2-call total for that leg
exceeds 180 minutes — exactly exp-105's own rule, applied per-leg rather
than once, since 1×-STEPS and 2×-STEPS legs are different cost regimes.
Two data points ground the estimate: **T8's own Iteration-7 precedent**
(a real r=156/312 leg overran its own hand estimate by up to 8×, the
reason this program carries a standing cost-gating discipline at all),
and **exp-105's own r=312 pilot**, which came in at 31.13 min (1867.5s),
comfortably under its 90-min threshold, with the full 2-call primary leg
at ≈52.1 min. Naive linear-in-STEPS scaling projects leg 4's settling
pair (STEPS=25600, 2× leg 3's 12800) at ≈62 min/call, ≈125 min total —
under the 180-min ceiling, but **not assumed**: each pilot is timed
before its paired call runs, exactly as exp-105 did. Worst case if every
r=312 leg pilots at just under 90 min and commits: legs 3+4+7+8 could
run to ≈5–6 hours of wall time; this is disclosed honestly rather than
hidden behind an optimistic naive estimate, and is the reason for the
"cheapest-first" sequencing above.

## 3. T1 escape-route statement

**N/A — instrumentation/diagnostic work**, exactly as exp-102/103/104/105
were. No σ(I)/σ(x,t)/angular-selectivity mechanism is built or varied
this cycle; no new material law is proposed. `DISCLAIMER` (exp-105's own
string, sourced from `thermo_sidecar.netd_disposition()`, asserted
present in both `PREDICTIONS_TEXT` and `RESULT_TEXT`, R23 pattern) is
reused verbatim — this cycle performs no thermal-sidecar work of its own
(P5 is not re-invoked; nothing about the thermal chain changes when only
`R_CORE`/`sigma_max` are varied at fixed `r_out`), but the disclaimer is
carried forward regardless, per R23's own standing discipline that a
disclaimer travelling only on some sections is not sufficient.

## 4. Per-metric predicted outcomes with falsifiable bands

**Gate P0′ / reproduction checks (zero new information, but
load-bearing preconditions):** every fresh capture's `kappa_window`
value must reproduce exp-105's committed scalar to <1e-6 relative
(r=156: 8.867e-4; r=312: 4.793e-6) — falsified by any larger deviation
→ halt before trusting that leg's floor-gate/settling data.

**Floor-gate outcome (item 1), self-similar r=156 and r=312:**
predicted **PASS** (`frac_unresolved` small, most window cells well
above the empty-scene RMS floor) at r=156, given the r=78/156 legs'
already-clean dense_x floor gates in exp-105 (`n_unresolved=0` at both).
At r=312, predicted **borderline** — the empty-scene window-box mean
intensity is itself falling steeply with r (consistent with
`kappa_window`'s own ~1,100× collapse being partly a shrinking-signal,
not shrinking-noise, story), so a genuinely elevated `frac_unresolved`
(band: **>10%** of the 4,000 window cells below floor) at r=312 would be
the single most direct evidence that P3's r=312 reading is
dynamic-range-limited, not purely physical — falsified (i.e., the floor
concern is unwarranted) if `frac_unresolved` stays **<2%**, matching the
clean r=78/156 precedent.

**Settling leg on `kappa_window` (item 2):**
- r=156: predicted **PASS** (rel_change ≤ 0.20), by direct analogy to
  the point-channel settling leg's landslide pass at this same r
  (0/53 failures, 14.5–30× inside tolerance per exp-105's Phase-5
  hand-verification).
- r=312: **genuinely uncertain, the reason this leg is "more urgent"
  here** — MARGINAL Nyquist tier at r=312 means the geometry is already
  closer to an aliasing/undersampling regime, and no settling leg has
  ever been run there for any channel. Falsifiable band: rel_change
  ≤0.20 → PASS; rel_change >0.20 → FAIL, meaning `kappa_window_312`
  itself (not just P4's ripple readings) may be settling-artifact-
  contaminated, materially undercutting P3's own r=312 anchor.

**`p3_trusted` (new symmetric risk-propagation flag, item 3) — named and
defined exactly as follows:**

```python
p3_trusted = settling_pass_window_312 and (nyquist_trust_tier(g312["nyquist_margin"]) == "TRUSTED")
```

— symmetric to `p4_156_trusted = settling_overall_pass and (nyq156 == "TRUSTED")`.
**Predicted value: False.** This is not a coin-flip prediction: r=312's
own `nyquist_margin=1.234` (MARGINAL-REDUCED-CONFIDENCE, computed by
`geom()`, zero new cost, already established in exp-105) is a fixed
property of the domain geometry, not of anything this cycle's new
captures can change — so `p3_trusted` is **structurally forced to False
at r=312 regardless of the settling leg's own outcome**, under the
literal symmetric definition Tier-1 item 3 asks for. This is disclosed
explicitly, not left implicit: the settling leg is still run and scored
in full (its own PASS/FAIL is separately informative, per item 2 above),
but readers should not expect `p3_trusted=True` to be reachable this
cycle without either an improved-Nyquist-margin geometry (a Tier-2 item,
a 4th r-point or wider `D_EFF`) or a deliberate, explicitly-justified
loosening of the bar to MARGINAL-or-better in a future cycle — a
decision this proposal does **not** make unilaterally.

**Fixed-absolute-thickness control's own `shape_ratio` prediction (item
4) — the falsifiable heart of this cycle:**

The self-similar family's own domain/window geometry (z/z_R, D_EFF,
LAMBDA_CELLS) is **identical** between families at a given r (only the
object's material law differs) — so if the pure geometric-window
diffraction effect the bridge was built to isolate is what drives
`shape_ratio`, the fixed-abs family should show approximately the
**same** `shape_ratio≈19.79` (its z/z_R sequence is unchanged). If,
instead, the self-similar family's own growing electrical thickness
(2.4λ→9.6λ, a materials/absorption confound Red Team named — a thicker,
still-fixed-`tau_shell` coating attenuates or dephases the near-field
diffractive tail differently as it grows) is what materially drives the
extreme collapse, the fixed-abs family (constant 2.4λ coating at every
r) should show a shape_ratio **much closer to the pure-diffraction
bands** already on file (sqrt-law 2.00±0.3, linear-law 4.00±0.5) — or at
least closer to T8's own already-REFUTED *ambient*-channel ratio of 5.33
(itself measured on a self-similar-thickness family, so not a clean
zero-confound reference, but the only other data point this program has
for "thickness-law held fixed, only geometry compared").

**Falsifiable bands, pre-registered:**
- `shape_ratio_fixedabs ≤ 8.0` (materially below self-similar's 19.79,
  by a factor of at least ≈2.5×) → **CONFIRMS** the growing-electrical-
  thickness hypothesis as a material driver; the pure geometric z/z_R
  window effect alone does not explain exp-105's own headline finding.
- `shape_ratio_fixedabs ≥ 14.8` (within 25% of self-similar's 19.79) →
  **REFUTES** the growing-electrical-thickness hypothesis as a material
  driver; the geometric z/z_R window effect (identical between families)
  dominates regardless of the coating's own thickness law, and some
  *other*, still-unidentified mechanism must explain why this channel
  collapses so much faster than the ambient channel's own C(z/z_R).
- `8.0 < shape_ratio_fixedabs < 14.8` → **AMBIGUOUS**, disclosed as such
  up front rather than forced into either bin; a genuine partial result,
  not a design failure (item 4 is a controlled comparison, not a
  guaranteed-decisive one).

This prediction is scored **only if `p3_trusted`-equivalent for the
fixed-abs family's own r=312 leg is at least evaluated and disclosed**
(same Nyquist/settling machinery, §2d/2e, applied "from the start" per
the queue's own instruction) — a caveated SCORED verdict, not a silent
one, symmetric to how P3 itself is now treated for the self-similar
family.

## 5. Idealizations

- 2D TMz, single λ=600nm/cpl=20 scope — unchanged from exp-102/103/104/105.
- θ=0° (normal incidence) only — the oblique-angle extension remains
  open (Tier 3 item 1, deferred again briefly, not executed this cycle).
- No settling leg is added for the point/wide channels at r=312 beyond
  what exp-105 already ran (none) — Tier 3 item 4 in the queue notes
  this spot-check is "largely superseded" by this cycle's own broader
  `kappa_window` settling leg, so it is not separately executed; the
  fixed-abs family's r=312 point/wide channels are captured (as a
  free byproduct of the primary/settling pairs already run) but their
  own settling status is disclosed as unchecked, not silently assumed
  clean.
- `graded_black_shell` remains UNOBTANIUM-WITH-PARAMETERS at every r in
  **both** families — the fixed-abs family's own constant 2.4λ absolute
  thickness is, if anything, closer to the µm-scale real-CNT-black range
  already cited in this program (exp-052's own realizability note,
  1.44µm at r=78-native, unchanged since the coating is fixed absolute
  size), but this is not re-verified or re-argued this cycle.
- No witness-scale extrapolation is attempted — bench-scale
  scale-robustness/control-comparison only.
- P5 (thermal sidecar) is **not re-invoked** this cycle — varying
  `R_CORE`/`sigma_max` at fixed `r_out` does not change the thermal
  chain's own `l_geometric_m` argument the way exp-105's own r_out
  sweep did; nothing new to report on that channel.
- `lab/` diff: zero.
- Persisting the full per-cell window-box arrays (§2c) modestly grows
  `results.json` (≈4,000 floats × 2 scenes × 2 STEPS-legs × 2 families ×
  2 new r-points ≈ 128,000 floats, ≈1MB uncompressed) — disclosed here
  as a real, if small, cost of closing item 1 properly rather than with
  a lossy summary.

**Tier 3 item 2 — the `delta_scene` R3-vs-R4 split, explicit
re-justification for a seventh consecutive deferral (required in
writing, per this cycle's own instructions, not a silent deferral):**
This is a genuinely different, older, much larger T28 sub-question — a
boundary-echo/PAD-diffraction mechanism's own resolution-sensitivity at
a specific x-normal-wall angle scan — with its own independent
multi-iteration history, structurally unrelated to the `kappa_window`
r-family bridge work this cycle's entire FDTD budget (16 calls, up to
≈5–6 hours at the disclosed worst case) is already committed to. Taking
it up this cycle would mean either abandoning Tier-1's own real,
load-bearing work (the single precondition for trusting or refuting
exp-105's own headline finding) or under-resourcing both questions at
once — neither is an acceptable trade against a genuinely different,
independently-resolvable question. This program has a direct precedent
for exactly this situation: **Iteration 51's "no-seventh-cycle" rule**,
which capped a different, prior `delta_scene` question at six
deferrals with the same structure (a standing, well-understood, but
never-executed-or-formally-retired item competing against a cycle's
own committed higher-priority FDTD budget) — that precedent is the
model followed here. Stated plainly, per the instructions: **Iteration
84, or the next cycle with spare FDTD/wall-clock budget, must either
execute the `delta_scene` R3-vs-R4 split or formally retire it** — a
seventh silent deferral beyond this one would not be acceptable under
this program's own standing discipline, and this proposal does not
attempt either option itself this cycle.
