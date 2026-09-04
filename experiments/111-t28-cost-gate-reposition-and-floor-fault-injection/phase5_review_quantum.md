# Phase 5 Review — QUANTUM OPTICS (Panel Iteration 88, exp-111)

**Charter**: non-classical absorption, state-dependent or coherent
interactions — expressibility contract: mechanisms enter the bench only as
effective classical parameters or Red Team strikes them. This cycle is
governance/instrumentation (T1 correctly N/A throughout, re-confirmed
below); my substantive duty this Phase is to re-verify, independently, that
mandatory fix 3 — my own seat's Phase-2 finding from this cycle
(`local_snr_peccored`/`local_snr_hollow` = `inf` at `floor==0`, discovered
first as a Phase-5 gap at Iteration 87, then re-caught as a live
self-contradiction in exp-111's own Phase-2 critique) — is genuinely closed
in the actually-committed code, and to scrutinize NOTES.md's own disclosed
FI-D falsification and the guard's own construction for any further edge
case.

## 0. Method

Every claim below was independently re-derived this session by importing
and executing `experiments/110-t28-item-i-local-norm-and-controls/run.py`
as actually committed (not by re-reading prose), running the real
`floor_fault_injection_control.py` end-to-end, and constructing additional
synthetic inputs of my own beyond the four FI-A/B/C/D cases already on
file, per R4/R18 discipline.

## 1. Mandatory fix 3 — re-verified: CONFIRMED, no `inf` found anywhere

The committed `classify_item_i_local()` (`run.py` lines ~310–362):

```python
floor = K * max(floor_p, floor_h)
floor_degenerate = bool(floor <= 0.0)
resolved = ((floor > 0.0)
            & (np.abs(pattern_peccored) >= floor)
            & (np.abs(pattern_hollow) >= floor))
...
if floor > 0.0:
    local_snr_peccored = np.abs(pattern_peccored) / floor
    local_snr_hollow = np.abs(pattern_hollow) / floor
else:
    local_snr_peccored = np.full(pattern_delta.shape, np.nan)
    local_snr_hollow = np.full(pattern_delta.shape, np.nan)
```

Ran this directly (not the control script alone — I re-imported `run.py`
myself and called the function on FI-C's exact construction plus several
inputs of my own):

- FI-C exact construction: `floor=0.0`, `floor_degenerate=True`,
  `resolved=[False]*48`, `local_snr_peccored`/`local_snr_hollow` both
  **all-`nan`**, zero `inf` anywhere. Matches the control script's own
  persisted output (`floor_fault_injection_control_output.json`) exactly.
- Ran the full committed `floor_fault_injection_control.py` myself
  end-to-end: FI-A/B/C/non-regression all PASS exactly as filed; FI-D FAILs
  on `never_exactly_zero` exactly as filed (`floor_min=0.0`,
  `floor_max=3.534e-4`).
- **Tried, and failed, to reconstruct literal `inf` anywhere** in
  `local_snr_*` via a battery of adversarial constructions beyond the four
  filed cases: NaN-contaminated patterns (below), amplitudes swept from
  `5e-4` down to `5e-300` at the phase-180 near-cancellation point (below),
  and the 12 real committed cells (all `floor_degenerate=False`, strictly
  positive floors, `2.3458e-4`–`2.0959e-3`, independently re-confirmed).
  Every path that reaches `floor<=0.0` correctly nan-fills both SNR arrays;
  every path with `floor>0.0` divides by a genuinely positive number.

**Verdict on the literal mandate: CONFIRMED.** `classify_item_i_local()`,
as actually committed, produces `nan` — never `inf` — for both
`local_snr_peccored` and `local_snr_hollow` whenever `floor<=0.0`, with no
edge case I could construct producing `inf` through this specific pre-
existing ternary. The `resolved` mask correctly reads all-`False` in the
same branch. Non-regression against all 12 real cells is genuinely
bit-identical, independently re-run.

## 2. NOTES.md's own FI-D falsification — mechanism correct, the specific numeric claim is not

NOTES.md's Interpretation section states: *"the pooled floor reads exactly
0.0 at swept phases 0° and 180° (out of 24)... `cos(2·pi·BIN_CENTERS_DEG/P*
+ 0)` is an EVEN function of the bin index under `i<->47-i`... at those two
phases only."*

**The antisymmetry mechanism is mathematically correct, independently
re-derived from scratch:** `BIN_CENTERS_DEG[i] == -BIN_CENTERS_DEG[47-i]`
exactly for all 48 bins (I checked every pair, zero violations). Writing
`θ_i = 2π·c_i/P* + φ`, the mirror argument is `θ_{47-i} = -θ_i + 2φ`. For
`cos(θ_{47-i}) ≡ cos(θ_i)` to hold for **every** `i` (i.e. the array is
genuinely, exactly even under the mirror map, forcing every pairwise
difference to zero), real-analysis requires `cos(2φ)=1, sin(2φ)=0`, i.e.
`φ = 0` or `φ = π` (180°) exactly — no other phase in the 24-point sweep
satisfies this. The Director's derivation of *which* phases are special is
right.

**But I independently re-ran the exact FI-D construction, per-phase (the
per-phase array is never persisted anywhere — not in
`floor_fault_injection_control_output.json`, not in `results.json`; only
`floor_min`/`floor_max`/`spread` survive), and the specific claim "reads
exactly 0.0... at 0° and 180°" is only half true:**

| phase | `mirror_pooled_floor` (this session, direct re-run) |
|---|---|
| 0° | `0.0` — bit-exact |
| 180° | `1.9515639105e-18` — **not** bit-exact zero |

Phase 0° is bit-exact because `deg2rad(0)=0.0` exactly and `cos(-x)` is
computed as a direct symmetric evaluation — no argument shift is involved,
so `cos(θ_i)` and `cos(-θ_i)` are bit-identical by construction. Phase 180°
requires evaluating `cos(-θ_i + 2π)`, and `2π` (via `deg2rad(180)=π`, an
irrational number, only approximately representable) is **added to** the
argument before the trig call — a floating-point argument-reduction
operation that is mathematically exact but not bit-exact in IEEE-754. The
result is a genuine, reproducible floating-point residual at the
`~1e-18` scale, not a mathematical near-miss.

**This is non-outcome-reversing for this cycle's own filed verdict**: the
code's own `never_exactly_zero = bool(np.all(floors > 1e-12))` check
already treats anything below `1e-12` as "zero" for its own pass/fail
purposes, so `1.9515639105e-18` and a hypothetical bit-exact `0.0` both
correctly read `False` there — FI-D's own filed FAIL stands regardless.
**But it is a genuine, previously-uncaught defect in the permanent record**:
NOTES.md states a specific numeric fact ("reads exactly 0.0... at 180°")
that does not hold under direct re-invocation of the actual code, about a
quantity that was never itself persisted or checked — the same failure
shape R4 exists to catch (a claim about a computed quantity, stated in
prose, that turns out not to reproduce when actually invoked), here applied
to the Director's own Phase-3/4 synthesis text rather than a critique's.
Non-blocking, but should be corrected before this document is cited as a
numeric source elsewhere (e.g. by a future cycle asserting "floor is exactly
zero at the mirror-canceling phases" as an established fact).

## 3. A further latent edge case in `classify_item_i_local`'s own construction — genuinely new, not raised by Phase 2 or the Director

The phase-180° residual above is not just a documentation slip — it
exposes the actual shape of a **different, adjacent hazard from the one
mandatory fix 3 closed**, in the guard's own boundary condition.

`floor_degenerate = bool(floor <= 0.0)` is a **bit-exact-zero test**. But
`floor = K·max(floor_p, floor_h)`, where `floor_p`/`floor_h` are percentiles
of `|pattern[i]-pattern[47-i]|/2` — a subtractive-cancellation quantity on
a bench that is *exactly* mirror-symmetric by construction (confirmed,
`mirror_pooled_floor`'s own docstring, PHOTONICS' Sec 1.1 finding). Any
real or synthetic input whose asymmetric content happens to sit near this
geometry's own antisymmetric-canceling phase (exactly what FI-D's own
180°-phase point demonstrates) produces a floor that is **not exactly
zero, but astronomically close to it** — a floating-point residual, not a
measurement. I constructed this directly, feeding realistic-magnitude
patterns (`~3e-3`, matching the real captures' own scale) with a small
oscillatory component at the phase-180° near-cancellation point:

```
floor = 6.18e-18   floor_degenerate = False   n_resolved = 48/48
local_snr_peccored range: 4.05e14 – 5.66e14   (zero inf)
```

**`floor_degenerate` reads `False`** (the floor is `>0.0`, just barely), so
**every bin is marked `resolved=True`**, and `local_snr` is reported as
~`5×10¹⁴` — not infinite (I swept synthetic amplitude from `5e-4` down to
`5e-300` at this same phase and never produced a literal `inf`; the
residual floor is bounded below by roughly `machine_epsilon × pattern_scale`,
which keeps the ratio safely under float64's `~1.8e308` overflow ceiling
for any physically-plausible pattern magnitude — **mandatory fix 3's
literal target, an actual `inf`, is genuinely unreachable through this
path, confirmed**) — but a `~10¹⁴`-scale "SNR" is just as physically
meaningless as `inf` was: it reports a bin as cleanly, confidently resolved
against a floor that is pure floating-point noise, not a real measurement
of anything. **This is a live descendant of the exact failure family
mandatory fix 3 was built to close, one boundary case further out than the
one that shipped.**

Concretely answering the question this charter poses: **could `floor` be
exactly 0 for a real, non-synthetic capture in some future geometry?** For
this bench's own real, exactly-symmetric geometry, a hypothetical future
scene whose asymmetric contaminant happened to sit at the antisymmetric-
canceling phase (analogous to FI-D's 180°) would almost certainly **not**
land on bit-exact `0.0` — real FDTD solver output carries its own
floating-point noise from summation order, threading, and grid rounding,
so the realistic failure mode is not "floor is exactly 0" but "floor is a
tiny, solver-noise-scale nonzero number sitting in the same
`~1e-18`-to-`~1e-12` gap this cycle's own FI-D point just landed in by
accident." **`floor<=0.0` catches the idealized synthetic corner case
(FI-C) but is not the right boundary for that realistic one.** Notably,
the fault-injection control's own test code already implicitly recognizes
this: `never_exactly_zero`/`never_exactly_full` in `fi_d()` use a `1e-12`
tolerance, not a bit-exact `>0.0`/`<amplitude` test — but that `1e-12`
convention was never carried into the production guard itself, an
inconsistency between the control's own tolerance and the shipped code's
strict boundary.

This does **not** fire against any of the 12 real committed cells (all
floors `2.3458e-4`–`2.0959e-3`, five-plus orders of magnitude clear of this
danger zone, independently re-confirmed) — matching every prior rule in
this registry's own founding-instance precedent of not retroactively
violating itself on data that has never actually triggered it.

## 4. One more construction gap, lower severity: NaN-contaminated input mislabels `floor_degenerate`

Fed a pattern with a single `NaN` entry (simulating an upstream solver
divergence, not currently reachable on any of the 12 committed cells):
`floor` comes back `NaN`; `floor_degenerate = bool(NaN <= 0.0)` evaluates
to **`False`** (NaN comparisons are always False in IEEE-754), yet the
diagnostic is completely undefined in this case. The practical fallout is
benign — `resolved` correctly reads all-`False` (`NaN > 0.0` is also
`False`, so the guard's first conjunct fails everywhere) and `local_snr`
correctly fills with `NaN`, not `inf` — so this does **not** reopen
mandatory fix 3's own literal gap. But `floor_degenerate=False` is the
wrong label for a computation that did not actually succeed; a future
reader filtering on `floor_degenerate` to separate "genuinely degenerate"
from "normal" cells would silently misclassify a NaN-corrupted cell as
normal-but-simply-unresolved. Flagged for completeness, not urgent (not
reachable on any real data path today).

## 5. Steel-man

The core, charter-relevant fix is real and correctly implemented: I
independently re-derived, from the actual committed function (not the
proposal's prose), that the pre-existing `inf`-producing ternary is
genuinely replaced by a `floor>0.0` guard with `nan`-fill on both sides,
verified against FI-C's construction and several adversarial constructions
of my own, with zero regression against all 12 real cells. The Director's
own antisymmetry mechanism for FI-D's two special phases is mathematically
correct as *math* — a nontrivial, independently-checkable derivation that
holds up. The proposal's own R18 scope (positive/negative control) is
satisfied, and FI-D was added as a good-faith strengthening exercise, not a
requirement — its informational FAIL is disclosed, not buried, and its
mechanism is at least reasoned rather than asserted blind.

## 6. Sharpest attack

The one thing that would have made this cycle's own record airtight — and
didn't happen — is invoking the code to check the *specific* per-phase
value before writing "reads exactly 0.0... at 180°" into a frozen NOTES.md
Interpretation section. That value is not bit-exact, it was never
persisted anywhere, and no seat at Phase 2 could have caught it (FI-D
hadn't been run yet at Phase 2 — it was written into existence between
Phase 2 and Phase 4). More consequentially: the boundary condition the
whole exercise was built to police (`floor<=0.0`) is demonstrably not
robust to the realistic floating-point regime one bin-phase-alignment away
from the exact synthetic corner case this cycle tested — a `~5×10¹⁴`-scale
spurious "resolved, high-SNR" reading is one boundary short of the `inf`
this cycle fixed, on the identical mechanism, and nothing in this cycle's
own text or fixes narrows the claim to acknowledge it.

## 7. Verdict

**CONFIRM-WITH-GAPS.**

Mandatory fix 3 (my own seat's charter-relevant finding) is genuinely,
verifiably closed: `classify_item_i_local()` produces `nan`, never `inf`,
for `local_snr_peccored`/`local_snr_hollow` whenever `floor<=0.0`, with zero
counterexample found across the filed cases and my own additional adversarial
constructions. Not CONFIRM outright because two genuine gaps survive,
neither raised by Phase 2 or the Director: (1) NOTES.md's own disclosed
FI-D mechanism narrative states a specific numeric claim ("exactly 0.0 at
180°") that is empirically false by ~18 orders of magnitude when actually
re-invoked — non-blocking to this cycle's own pass/fail call, but a real,
previously-uncaught R4-shaped inaccuracy in a frozen document; (2) the
`floor<=0.0` guard's own boundary is not floating-point-robust — a
realistic near-degenerate (not bit-exact-zero) floor, demonstrably
reachable at exactly the phase this cycle's own FI-D construction landed
on by accident, evades `floor_degenerate`, is scored `resolved=True`
everywhere, and produces `local_snr` values around `10^14`–`10^15` — not
literally `inf` (confirmed unreachable via this path even at synthetic
amplitudes down to `5e-300`), but exactly as physically meaningless as the
bug this cycle fixed, one boundary further out. Neither gap fires on any
of the 12 real committed cells (all floors five-plus orders of magnitude
clear of the danger zone) — non-blocking today, genuinely latent for a
future geometry or a future contaminant landing near this bench's own
antisymmetric-canceling phase.

## 8. Ranked top-3 candidate directions for Iteration 89

1. **Harden `classify_item_i_local`'s degeneracy guard with an
   amplitude-normalized epsilon, not a bit-exact `<=0.0` test** — e.g.
   `floor_degenerate = floor <= max(ABS_EPS, REL_EPS * max(|pattern_peccored|.max(), |pattern_hollow|.max()))`,
   matching R13's own already-established amplitude-normalized
   floor-gating convention for the sibling denominator-zero hazard. Add a
   fifth fault-injection case using this cycle's own real phase-180°
   residual (`floor≈1.95e-18` on FI-D's own construction, or my
   realistic-magnitude `~6.18e-18` variant) as the injected input,
   asserting the *hardened* guard correctly flags it `floor_degenerate`
   rather than reporting a `~10^14`-scale spurious SNR. Zero new FDTD.
2. **Correct NOTES.md's own Interpretation section**: persist the actual
   per-phase `floors` array from `fi_d()` (currently discarded — only
   min/max/spread survive) and restate the claim precisely: bit-exact zero
   only at phase 0°; phase 180° is `~1.95e-18`, a floating-point
   argument-reduction residual, not a second bit-exact zero — a cheap,
   same-shift, zero-new-FDTD text correction, matching this program's own
   R4/R26 discipline for a disclosed-but-unverified internal claim.
3. **Execute the already-queued Tier-1 item 3** (PHOTONICS' `cpl`-
   refinement spot check at the two named bins, `-146.25°`/`+168.75°`),
   now doubly motivated: beyond discriminating genuine common-mode-masked
   structure from discretization noise, this cycle's own FI-D finding
   shows the established `P*=2.8421°` T28 contaminant, if present at
   those bins' own phase relative to the mirror axis, could itself
   produce a near-degenerate floor reading that (under the current,
   unhardened guard) masks its own presence behind an inflated,
   meaningless SNR rather than a flagged `floor_degenerate` case — raising
   the stakes of running that check, and of fix #1 above landing before
   item 3's own real data is scored against this diagnostic.
