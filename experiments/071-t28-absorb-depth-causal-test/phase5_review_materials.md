# PHASE 5 — REVIEW · MATERIALS & METAMATERIALS · Panel Iteration 48 · exp-071

*Fresh sub-agent, blind to the other six Phase-5 reviews this cycle. Charter
(PANEL.md seat 2): sub-wavelength structure; what could physically realize
the proposed optical behavior; owns the realizability bound (published /
plausible / unobtainium-with-parameters).*

## Verification performed (independent, not taken on the document's word)

1. **Read `lab/fdtd2d.py::Sim._damping` directly** (lines 122–129). Confirmed
   bit-for-bit against `ABSORB_NOT_MATERIAL_CAVEAT`'s own description: a
   cubic ramp `((i)/absorb)**3` over the outer `absorb` cells on all four box
   edges, converted to a multiplicative field mask via `exp(-0.30*d)`. Traced
   its use (`self.Ez *= self.damp_e`, `self.Hx *= self.damp_hx`, etc.,
   lines 228–253): **it is applied as a bare post-update multiplicative mask
   on the field arrays, not a conductivity/loss term inserted into the
   Maxwell update equations.** There is no `σE` current, no dispersive
   `ε''(ω)`, no Kramers–Kronig-constrained loss anywhere in this mechanism —
   it never enters the physics being solved. This is a *stronger* case for
   "not a material" than the cycle's own caveat text states: even a crude
   graded-conductivity absorber would at least be a (bad) material model;
   this is an out-of-band numerical mask with no material referent even in
   principle. Confirmed the cycle's independently-derived caveat text is
   accurate, if anything slightly conservative.
2. **`grep`-verified `ABSORB_NOT_MATERIAL_CAVEAT`/`THERMO_SCOPE_CAVEAT`/
   `WAVELENGTH_SCOPE_CAVEAT` in `run.py`** — all three defined once (lines
   66–90), included in `FROZEN_PREDICTIONS` (printed unconditionally at the
   top of every run, line 485) and in `out["caveats"]` (lines 575–577,
   written to `results.json` regardless of which branch fires). **Genuine
   fix, not a claimed one**: my own Phase-2 critique's attack — CONFIRM
   branch titled "genuine ABSORB-depth-tied mechanism," caveat absent
   entirely — is resolved; the branch is renamed
   `CONFIRMED_ABSORB_TIED_NUMERICAL_BOUNDARY_EFFECT` and the caveat text is
   present in the committed code, not just asserted in prose.
3. **One real gap, found by tracing the branch that actually fired.** The
   `combined_reason` string built per-branch (lines 515–546) appends
   `ABSORB_NOT_MATERIAL_CAVEAT` only inside the `CONFIRMED` branch (line
   521). The `NEITHER` branch — the one that actually executed this run —
   appends only `THERMO_SCOPE_CAVEAT` (line 546); `WAVELENGTH_SCOPE_CAVEAT`
   is appended in none of the three branches' `combined_reason` strings.
   The caveat text is *present* in the artifact (top-level `caveats` dict,
   and the pre-run `FROZEN_PREDICTIONS` print), so nothing was silently
   dropped — but a consumer reading only `results.json["combined_reason"]`
   or only the tail of stdout (`COMBINED VERDICT: NEITHER` +
   `combined_reason`) on *this actual run* would not see the
   ABSORB-is-not-a-material caveat sitting next to the verdict text itself,
   only next to a branch that didn't fire. `phase4_results.md`'s closing
   line ("Caveats … disclosed unconditionally, printed with every result
   regardless of outcome") is true of the artifact as a whole but slightly
   overstates what is welded to the printed verdict line in the branch that
   ran. Cheap, zero-FDTD fix for Iteration 49: append all three caveat
   constants to `combined_reason` in every branch, not just `CONFIRMED`.

## Does the cycle's language backslide into implying ABSORB is physical?

No clean backslide found. `phase4_results.md`'s prose ("the period rises
smoothly and monotonically with `ABSORB` depth … a real, well-determined
*shape* to the trend") and `NOTES.md`'s "Learned" item 2 ("the per-config
periods DO rise smoothly with `ABSORB` depth (a real, well-fit shape)")
stay carefully scoped to describing the *numerical trend in the recovered
statistic*, not a physical mechanism, and both are immediately qualified by
the resolution-floor finding in the same paragraph. This is a real
improvement in discipline over exp-070/-069's own first-draft habits (R4,
the earlier "precisely recomputed" incident). The one place I'd tighten
language further: `design_geometry.py`'s docstring (line 8) poses the
question as "a genuine causal, ABSORB-tied **mechanism**" without the
caveat attached in the same sentence — defensible as a framing device (the
file explicitly disclaims implementing the caveat itself, deferring to
`run.py`/`NOTES.md`, lines 85–89), but a reader who opens only this file
gets the un-caveated framing first.

## REALIZABILITY_MEMO.md angle

Correctly untouched, and correctly declined by both my seat's own Phase-2
critique and this cycle's synthesis. There is nothing to amend: T1 is N/A,
no σ(I)/dispersive-ε/gain mechanism is proposed or scored, and — per the
verification above — `ABSORB` never even reaches this seat's realizability
ladder (published / plausible / unobtainium-with-parameters), because it
isn't a material claim of any tier; it's FDTD domain-truncation bookkeeping.
The memo's job is to track candidate *materials* for the phenomenon; T28 is
an instrument-fidelity question about this engine's own boundary condition,
categorically outside that scope regardless of which way its verdict lands.
Worth stating explicitly for the record (this cycle doesn't): **even a full
CONFIRM of "ABSORB-depth-tied" in a future, properly-powered rerun would be
zero evidence about any real absorbing material** — it would only be a
finding about this simulator's own boundary implementation, decoupled from
`materials.graded_black_shell` (the actual, already-validated,
physically-referenced witness absorber this program's constraint-1/2
results rest on). T28's resolution, either direction, cannot feed back into
this seat's realizability bound for the phenomenon itself.

## Proposed next move for T28 (Iteration 49 queue), from this seat's lens

The program's own queued fix (wider angular window to raise the Rayleigh
resolution above the 3.9% spread) is sound and I don't contest it — but it
is EM/QUANTUM's instrument-power fix, not a materials-discipline one, and
even if it succeeds it only tells you *whether* the period tracks `ABSORB`,
not *why* — which is the question this seat actually owns.

**Concrete, falsifiable, materials-discipline next step: a mask-functional-
form ablation, not a depth sweep.** Hold `ABSORB` depth fixed (e.g. at 80
cells, the `C80` config, zero new geometry) and vary the *shape* of
`_damping`'s ramp — the cubic exponent (`**3` → `**2`, `**4`, or linear
`**1`) and/or the decay constant (`exp(-0.30*d)` → `exp(-0.15*d)`,
`exp(-0.60*d)`) — while holding cell count constant. This is a one-line
change to `Sim._damping` (or a parametrized variant passed at construction),
zero new geometry, and directly answers the question this seat is chartered
to ask: **is the ~2.8°-family period tied to a *length scale* (which
`ABSORB` depth in cells approximates) or to the *numerical decay profile*
of the mask (which has no length-scale interpretation at all)?** If the
period shifts with the ramp exponent/decay constant at FIXED cell depth,
that is decisive, cheap (a handful of FDTD calls, no new configs) evidence
that the periodicity is an artifact of this engine's specific damping-mask
construction — not even weakly a stand-in for a physical boundary-layer
thickness — and T28 should be redirected entirely away from "ABSORB depth"
as a physical proxy. If the period is invariant to ramp shape/decay
constant at fixed depth, that strengthens (not proves) the case that
`ABSORB` depth-in-cells is doing something geometrically meaningful, which
would then justify the wider-window resolution fix as the right next
investment rather than a parallel path.

## Rating: **PARTIAL**

The causal test itself is well-designed, honestly executed, and its
NEITHER verdict is a real, resolution-floor-limited finding, not a hedge —
the mandatory-fix docket (settling closure, resolution-floor gate,
caveat reinstatement) demonstrably did its job, including catching a
result shape (small monotonic high-R² trend, floor-limited) that would
likely have been misreported as REFUTE without it. From this seat's own
charter, though, there is no materials content to promote here regardless
of which way P-071-2 eventually resolves: `ABSORB` sits entirely outside
the realizability ladder, T28's resolution feeds nothing into
`REALIZABILITY_MEMO.md`, and the caveat discipline — while genuinely
reinstated in the artifacts (unlike the R4-precedent failure this seat's
own Phase-2 review flagged) — has one cheap loose end (caveat not welded to
the `combined_reason` string in the branch that actually fired) worth
closing before this text gets quoted into LOGBOOK.md.
