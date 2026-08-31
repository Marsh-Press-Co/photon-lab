# Phase 5 — PHOTONICS Review (exp-096, Panel Iteration 73)

*Seat charter (PANEL.md, verbatim): surface interaction, absorption
spectra, angular dependence, scattering cross-sections. Owns: is the
proposal's optical response coherent as stated, across wavelength and
angle? Blind review — this seat led exp-096's own Phase 1 proposal;
PANEL.md states that fact earns the proposal no deference, and it
receives none here. No other seat's current Phase-5 output was read.*

## 1. Independent re-verification of the headline results

Read `phase1_proposal.md`, `phase2_redteam_audit.md`, `NOTES.md`,
`run.py`, `results.json`, `run_output.txt` in full, plus, from source,
`lab/fdtd2d.py::Sim.__init__`/`add_line_source`, `lab/materials.py`, and
`experiments/069-.../design_geometry.py`'s `r4_config()`/`R4_CONFIGS`. Did
not take any print statement or NOTES.md sentence on faith — every number
below was recomputed independently this session.

**Registration-readback gate (Checks 1–6): CLEAN, reproduces bit-exact.**
All 16 representative constructions (8 `(family,θ)` points × both
`C40`/`G40` pair members) show `check1`–`check4` all `true`,
`check4_max_abs_diff: 0.0` in every one of `results.json`'s 16
`representative_results` entries — confirmed by direct inspection, not
the `representative_all_clean: true` flag alone. **Check 5** (the
recipe-internal spot-check): I independently re-derived it a third time,
from `design_geometry.py::r4_config()`'s own source, not from `run.py`'s
copy of the arithmetic. `r4_config(80, 0)` (i.e. `C40_R4`) computes
`src_x = R4_BASE_SRC_X + pad = round(300·2.0) + 0 = 600`,
`y_lo = R4_BASE_ABSORB + pad = round(40·2.0) + 0 = 80`,
`y_hi = ny − y_lo = (round(1584·2.0)+0) − 80 = 3088` — bit-exact against
both `R4_CONFIGS["C40_R4"]`'s stored values and `check5_recipe_spot_check`
in `results.json` (`600/80/3088` both places). **Check 6**: I hand-checked
all 8 `notes_line`/`notes_md_frozen_values` entries against
`NOTES_MD_FROZEN_LINE_VALUES` in `run.py` itself — internally consistent,
and the cited lines (437/445/476/495/511) do correspond to the claimed
`RANK1A`/`RANK1C`/`RANK2B_NATIVE`/`RANK3A`/`RANK4` angle pairs in
`experiments/095-.../run.py`. **CLEAN is a real, correctly-computed
result**, not a mis-set flag.

**Fault-injection triad: the `caught_as_defect` logic is correct, but one
of NOTES.md's own claims about *which* check independently catches FI-A
does not survive contact with the code that implements it — traced below,
independently, not merely asserted.**

`caught_as_defect = (not <scenario>["clean"])` for every scenario (`run.py`
lines 221/227/233/238) — tautological with `clean`, but tautological-and-
correct is exactly what a MUST-catch/MUST-NOT-catch gate needs: positive
control requires `clean=True → caught_as_defect=False`; each FI scenario
requires `clean=False → caught_as_defect=True`. `results.json` confirms
all four land as required (`False/True/True/True`), and
`fault_injection_all_as_predicted: true` correctly ANDs exactly those four
conditions (`run.py` lines 240–244) — the code is right.

But trace **which** check does the catching for **FI-A**, from the actual
arithmetic, not the label. `run_checks_1234` computes
`expected = phase_expected(sim.lam, theta_intended, ...)` — note: **`sim.lam`**,
the value actually baked into the (possibly-corrupted) `Sim` object, not
an independently-verified reference. For FI-A, `sim` is built with
`cpl_actual=30` while `cpl_intended=40`; `sim.lam` therefore reads `30`.
`add_line_source` itself also used `self.lam=30` to build the real stored
`phase` array. So Check 4's comparator and the actual array are computed
from the *identical* (wrong) `lam` — they agree by construction, every
time, for a `cpl`-only corruption. `results.json` confirms this exactly:
FI-A's `check4_phase_ramp: true`, `check4_max_abs_diff: 0.0` — Check 4
does **not** flag FI-A; only Check 1 does. Yet NOTES.md's own Setup table
and Predictions section both state FI-A is caught by "Check 1
(transitively, Check 4)" — a claim the code's own mechanics, and the run's
own output, contradict. The Result section quietly drops the
"transitively Check 4" language ("FI-A ... caught by Check 1 as
predicted" — no mention of Check 4) without flagging that the earlier
claim was wrong. This is non-load-bearing to any headline verdict (FI-A
*is* caught, by Check 1 alone, exactly as the MUST-catch requirement
needs) but it is a real, independently-verified inaccuracy in the
committed record: Check 4, as implemented, can never independently
confirm a `cpl`-only registration defect, because it always re-derives its
own reference from whatever `sim.lam` the (potentially corrupted) object
actually holds. This is mechanically the same fragility Red Team's own
Phase-2 attack #3 named for the source-of-truth-constant case (§4
below extends it) — it also applies, undisclosed, to the simpler
caller-plumbing case this program built FI-A specifically to test.

**Zero-FDTD desk bound: bit-exact reproduction, both stages.** Pulled
`experiments/090-.../results.json::q8.crossings_deg[2:4]`
(`40.265420…°`, `41.460901…°`) and
`experiments/092-.../results.json::rank1.crossing_report`
(`40.071838…°`, `41.781067…°`, `41.837653…°`) directly and recomputed the
three migration magnitudes and all nine containment ratios by hand:
`0.19358…°/0.32017…°/0.37675…°`, and ratios `1.0332/0.6247/0.5309` (±0.2°),
`2.0663/1.2494/1.0617` (±0.4°), `2.5829/1.5617/1.3271` (±0.5°) — match
`results.json::desk_bound` to the displayed precision in every cell. The
qualitative reading (±0.2° insufficient; ±0.4° razor-thin at 1.06× against
the largest figure; ±0.5° the narrowest candidate clearing all three by
>30%) is arithmetically sound and honestly stated, not rounded in the
proposal's favor.

## 2. Verdict: **CONCUR-WITH-GAP(S)**

The headline CLEAN result, the fault-injection triad's overall
correctness, and the desk bound all independently reproduce bit-exact.
This is genuine, real information — nineteen T28 cycles never checked
this axis, and this cycle's positive/negative controls prove the check
would have caught the defect it exists to catch, had one existed. I do
not dispute the registration_gate_outcome or the desk-bound numbers. But
two gaps, both independently verified from source this session and
neither raised by any of the five blind Phase-2 critiques or Red Team's
own audit, mean the CLEAN result's *scope* is narrower than even
Idealization 38/39's own careful residual-scope language discloses.

## 3. Sharpest finding — a whole axis of "registration" is unchecked, and it
## is the one this specific sub-thread has direct history with

`add_line_source` (`lab/fdtd2d.py:132`) constructs **two** independent
per-source arrays from its inputs: the phase ramp (`phase`, driven by
`angle_deg`/`self.lam`) — the object this cycle's Checks 1/2/4 exhaustively
audit — and the **amplitude taper** (`profile = amplitude * p`, a raised-
cosine window built from the `edge` argument, `lab/fdtd2d.py:160-164`,
stored at `sim.sources[-1]['profile']`). `construct_sim` in this cycle's
own `run.py` passes `edge=TAPER[family]` (i.e. `dg.R4_TAPER`/`R3_TAPER`/
`R5_TAPER`) into every one of the 18 `Sim` constructions — but **no check
in this cycle (1 through 6, nor the fault-injection triad) ever reads
`sim.sources[-1]['profile']` or verifies `TAPER[family]` against anything.**
I confirmed this by direct inspection of `run.py`'s six check functions
and `results.json`'s own per-point dicts (`profile`/`edge`/`amplitude`
appear nowhere in either). A silent `TAPER` mis-registration — the wrong
family's edge-taper constant reaching a given call site, or a stale
literal surviving a `RATIO` rescale the way `PAD=ABSORB−40` already did at
Iteration 48 (exp-071) for a different constant — would pass every check
this cycle runs, at every one of its 16 representative points, with zero
FI coverage designed to exercise it.

This matters specifically to this seat's charter, not generically: the
amplitude taper *is* the effective-aperture edge profile that sets the
launched wave's angular spectrum and diffraction sidelobes — the physical
quantity this program already investigated by name as a T28 mechanism
candidate (`experiments/070-.../`, P-070-3: "TAPER alone as a sub-aperture
misses by 1197%," a clean REFUTE of TAPER *as a diffractor*, but that
result says nothing about whether `TAPER`'s own *value* is correctly wired
into each family's construction, which is a categorically different
registration question this cycle was explicitly built to close for the
phase/angle channel and simply never extended to the amplitude channel).
Idealizations 31–39 are otherwise a careful, honestly-scoped residual list
— run-time dispersion (31), formula-correctness vs. wiring-correctness
(33), lock-step maintenance risk (34), representative-set non-exhaustivity
(35), and the desk bound's own optimism (36/37) are all named precisely.
**None of them name the amplitude-taper channel as unchecked.** A gate
called a "registration-readback gate" that reads back resolution, angle,
placement, and phase, but not amplitude, has a real, un-disclosed hole in
its own stated completeness — not fatal to what it does prove (§4), but a
genuine PHOTONICS-relevant residual that the current Idealization list
does not own.

**Secondary finding (§1 above):** the "transitively, Check 4" claim for
FI-A is mechanically false as coded — Check 4's comparator always
re-derives from `sim.lam`, so it can never independently corroborate a
`cpl`-only corruption Check 1 already caught. Low severity (the MUST-catch
requirement is still met, via Check 1 alone, and the Result section's own
phrasing happens to avoid repeating the false claim) but it is the kind of
uncorrected overclaim this program's own R4 house rule exists to catch,
and it slipped past six blind Phase-2 reviewers and Red Team's own audit —
including the audit's own attack #3, which found the adjacent, more
general version of the same mechanical fact (Check 4 inherits whatever
Check 1 does or doesn't catch) but did not connect it back to correct
FI-A's own table entry.

## 4. Does the construction-time scope (Idealization 31/33) leave an
## angle/wavelength failure mode this seat would care about, structurally
## invisible to this gate?

Yes, two, both already partially named but worth stating in this seat's
own terms:

- **Wavelength.** Every check runs at 600nm only (`R{3,4,5}_CPL` are
  keyed `{600: …}` only, confirmed by reading `design_geometry.py`
  directly — no 750nm branch exists yet for this `R3`/`R4`/`R5` rescaled
  sub-family, unlike the parent T28/T21 threads' own `LEG750` block). This
  matches Idealization 1's blanket 2D/600nm scope carried by every T28
  desk cycle, so it is not a new omission — but it is worth this seat
  stating explicitly: if the `R3`/`R4`/`R5` resolution-migration work is
  ever extended to 750nm (as the wider T28/T21 program already has been),
  this registration gate would need re-running there from scratch — a
  CLEAN reading at 600nm says nothing about whether the same construction
  recipe is correctly wired at a different `cells_per_lambda` keyed to a
  different λ.
- **Angle.** The 8 representative points span a narrow 38.4°–41.85° band
  (3.45° total), all reused verbatim from exp-095's own already-committed
  job constants (Idealization 35, honestly disclosed as non-exhaustive).
  That is a defensible design choice for *this* cycle's purpose (closing
  the specific Rank-1c ambiguity), but it means the gate has never been
  exercised anywhere near grazing incidence or at an angle where
  `k·sinθ·Δy` wraps several more multiples of 2π than this band does — a
  regime where an `angle_deg`-sign or `np.sin`/`np.radians` ordering
  defect could plausibly manifest differently. Idealization 33 already
  and correctly disclaims formula-correctness (that is the trust suite's
  job); this is a narrower point about the *tested angular range* of the
  wiring check itself, not the formula.

Neither of these changes the CLEAN verdict's validity within its stated
scope — but both belong in a future re-statement of what "CLEAN" licenses,
alongside Idealization 38/39.

## 5. Is Idealization 38/39's residual-scope framing honest?

**Yes, as far as it goes — but it is incomplete, not dishonest.** Every
sentence I checked against source is accurate: the CLEAN result genuinely
rules out caller-level plumbing (Checks 1–4, confirmed by a real,
correctly-functioning fault-injection triad) and `run.py`-vs-NOTES.md
transcription drift (Check 6) within the phase/angle/placement/resolution
channel it audits, and Check 5 genuinely is a single spot-check
(`R4`/`C40_R4` only), not a census, exactly as Idealization 39 states. The
"strengthens, does not complete, the 2:1-to-3:1 impressionistic reading"
language is appropriately hedged and matches Red Team's own exp-095
framing. Nothing here is a hand-typed or unreproduced figure — every
number reproduces bit-exact (§1). The gap is one of *completeness*, not
*honesty*: the residual list never states that the amplitude-taper
channel (§3) is untouched by any of the six checks, so a reader relying on
Idealization 38's "post all fixes, the gate's honest residual scope"
sentence would reasonably but incorrectly believe the *entire* source
registration — not just its phase/angle/placement sub-channel — has been
audited. That is the specific, narrow sense in which this cycle's own
scope statement, while not making any false claim, is not fully complete
either.

## 6. Ranked candidate directions for Iteration 74

Reconciled Iteration-73 queue's own items 3 (EM's `cpl=40` bracket check
at the other three established `cpl=20` nulls, ~24 calls) and 4 (the
node-bracketing re-run at θ₀≈38.590°, ~8–16 calls) were both explicitly
gated on this cycle's own registration outcome (NOTES.md §"What this cycle
does NOT do"). A CLEAN reading, within the scope §4/§5 describe, is
sufficient to unblock both — but the taper-channel gap (§3) argues for one
more cheap step first.

1. **(New, cheap, zero-FDTD — closes this review's own finding.) Extend
   the registration-readback gate with a seventh check: read back
   `sim.sources[-1]['profile']` and independently recompute the raised-
   cosine taper window from `TAPER[family]`, comparing against the stored
   array (mirroring Check 4's own `np.allclose` idiom); add a fourth
   fault-injection scenario (FI-D: wrong `edge` value, e.g. swap
   `R4_TAPER` for `R3_TAPER` at an `R4` call site) to prove the new check
   is a genuine discriminator, not a rubber stamp, per this program's own
   R-lineage standard. Also extend Check 5's recipe-arithmetic spot-check
   (currently `R4`/`C40` only, Idealization 39's own named residual) to at
   least one `G`-padded config and one non-`R4` family, since Idealization
   17's shared-recipe risk is exactly the class most likely to produce a
   family-wide, not caller-local, defect. Resolves: the two gaps this
   review found; costs zero FDTD calls, matching this cycle's own
   established near-free-instrument-work idiom.
2. **Reconciled queue item 3 — EM's `cpl=40` bracket check at the other
   three established `cpl=20→cpl=30` nulls (~24 calls).** Iteration 72's
   own framing names this "the decisive discriminator between a
   family-wide defect and feature-dependent migration" — now sequenced
   after a registration reading that (within its stated scope) removes
   the wiring-defect confound at the phase/angle/placement level. Resolves:
   whether Rank 1c's own FAIL pattern is a `cpl=40`-family-wide artifact or
   specific to the 38.590° feature.
3. **Reconciled queue item 4 — the re-centered, directionally-weighted
   node-bracketing re-run at θ₀≈38.590° (~8–16 calls), using this cycle's
   own desk bound to size the window ≥0.5° single-sided half-width, not
   the ±0.1° that produced Rank 1c's original FAIL.** Directly re-tests
   the specific ambiguity this whole sub-thread has carried since Iteration
   72. Sequenced after item 2 above per the reconciled queue's own
   ordering (item 3 before item 4), and after item 1 so any taper-channel
   defect found there doesn't have to be retroactively audited against
   fresh real-FDTD spend.
4. **Documentation-only, zero cost: correct NOTES.md's FI-A attribution**
   ("Check 1 (transitively, Check 4)" → "Check 1 alone; Check 4 self-
   confirms whatever `sim.lam` the corrupted object actually holds and
   cannot independently catch a `cpl`-only defect") — matching this
   program's own R4 house discipline that an inaccurate claim gets
   corrected in the record once found, regardless of load-bearing status.
   Cheap enough to fold into whichever of items 1–3 runs next rather than
   spending a cycle on it alone.
5. **Item 6 (the `cpl=50`/`R5` interior sweep) stays deferred** — nothing
   in this review changes the unanimous prior ordering; it remains the
   correct last item.
