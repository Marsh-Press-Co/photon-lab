# Phase 5 Review — PHOTONICS (exp-097, Panel Iteration 74)

*Blind review, fresh context. Charter: is the proposal's optical response
coherent as stated, across wavelength and angle — source construction,
angle/wavelength/taper registration? Does the Result section's own claims
survive contact with `run.py`'s source and `results.json`'s actual numbers?
Independently re-executed this cycle's `run.py`, diffed against the
committed `results.json`, and independently re-derived the phase-ramp,
taper-window, and `R3`/`R4`/`R5` base-constant formulas directly from
`lab/fdtd2d.py` and `experiments/069-t21-.../design_geometry.py` — not
taken on the document's word.*

## Independent reproduction (verified, not merely restated)

- **Bit-exact re-run.** `python3 experiments/097-.../run.py` reproduces
  the committed `results.json` exactly (every field except `wall_time_s`,
  a timing artifact) — including the registration-gate `CLEAN` outcome,
  all nine fault-injection results (positive control, FI-A/B/C/D/E/F/G/H),
  and the 21-construction count.
- **Trust suite**: re-ran `lab/validation/run_all.py --only 12346789`
  myself — **41/41 PASS**, matching the document's own claim.
- **Phase-ramp formula (Check 4).** `lab/fdtd2d.py:171-175`'s
  `k=2π/lam·sin(θ)·(y−ȳ)+rel_phase` is reproduced bit-for-bit by
  `phase_expected()` (imported unmodified from exp-096). Confirmed
  `self.lam = float(cells_per_lambda)` (`fdtd2d.py:75`) — so FI-A's
  spurious Check-4 agreement (comparator recomputed from the
  already-corrupted `sim.lam`) is real, not a restated claim: I traced it
  myself and it is structurally unavoidable given the formula's own
  inputs, exactly as R18's own founding finding states and as this
  document correctly, non-silently, carries forward.
- **Taper formula (Check 7, new this cycle).** `lab/fdtd2d.py:160-164`'s
  raised-cosine window (`p=ones(n); win=0.5·(1−cos(π·i/edge)); p[:edge]=
  win; p[-edge:]=win[::-1]`) is reproduced bit-for-bit by `taper_expected()`.
  This is the one item squarely inside this seat's own charter — the
  amplitude-taper channel sets the aperture illumination function feeding
  every sidelobe/near-null angular feature this sub-thread has fought
  over for twenty cycles, and it is now correctly, independently audited
  for the first time. Sound.
- **`R3`/`R4`/`R5` base constants and the `y_hi`/`BASE_NY` correction.**
  Read `design_geometry.py` directly: `R3_BASE_NY=2376`,
  `R3_BASE_ABSORB=60`, and `r3_config()`'s own `y_hi = ny − y_lo`
  gives `2376−60=2316` for `C40_R3` — confirming the Result section's own
  corrected citation (`y_hi=2316`, not the Phase-1 draft's mistaken
  `R3_BASE_NY=2376`) is right, and the fix that EM/THERMODYNAMICS caught
  independently at Phase 2 is genuinely applied in the frozen document,
  not merely promised. Same check for `R5` (`3960−100=3860`, not `3960`).
  Both bit-exact against my own from-scratch derivation.
- **NOTES.md line citations.** `grep -n` against
  `experiments/095-.../NOTES.md` confirms lines 265/291/304/437/445/476/
  495/511 all say exactly what `run.py`'s `NOTES_MD_FROZEN_*` dicts and
  Check 6's frozen-value comments claim, character for character.
- **FI-G banker's-rounding arithmetic.** `round(301·1.5)=452`,
  `round(301·2.0)=602`, `round(301·2.5)=752` — independently computed,
  bit-exact against `results.json`'s `FI_G` block.

Everything above independently reproduces exactly as claimed. This is a
well-executed cycle on its own stated terms.

## Gap 1 (primary, new — not raised by any Phase-2 critique or Red Team's audit): Check 5's own fault-injection control never exercises two of the three quantities the check itself asserts on

`check5_recipe_spot_check_extended()` (both the original `R4` leg,
unchanged since exp-096, and this cycle's new `R3`/`R5` legs) computes
**three** independently-recomputed quantities per family —
`src_x`, `y_lo`, `y_hi` — and its own CLEAN/DEFECT verdict is the
conjunction of all three matching (`ok = (src_x==target["src_x"] and
y_lo==target["y_lo"] and y_hi==target["y_hi"])`). NOTES.md's own Setup
section names all three explicitly as the check's job ("Check 5... `y_lo`/
`y_hi`/`src_x` independently recomputed").

But `FI-G` — the check's *only* fault-injection control, in either
exp-096 or this cycle's own 3-leg extension — corrupts exactly one native
constant, `native_src_x` (300→301), and `run_fi_g()` reports the result on
**`src_x` alone** (`src_x_recomputed`/`src_x_stored`/`caught_as_defect` —
no `y_lo`/`y_hi` fields anywhere in the function). `native_absorb` (which
generates `y_lo`) and `native_ny` (which generates `y_hi`) are never
perturbed, in any of the three families, in either cycle.

**Consequence:** two of Check 5's three asserted quantities —
the `y_lo`/`y_hi` branch, i.e. exactly the source-placement span the
phase-ramp formula (Check 4) itself centers on — have **zero demonstrated
fault-injection discriminating power**, for any of `R3`/`R4`/`R5`, as of
this cycle's own close. This is the identical shape of gap R18 exists to
police — a check's claimed scope (all three quantities, per NOTES.md's own
Setup text) exceeding what its own executed control actually demonstrates
— surfacing inside the cycle whose entire stated purpose is closing
exactly that shape of gap in this gate, missed by all five blind Phase-2
critiques (QUANTUM's own critique got closest, flagging FI-G's `R4`-only
*family* scope, but not its *src_x-only* scope within a family) and by Red
Team's own Phase-2 audit, whose own §3/§6 finding (the `cpl_ok` tautology)
is a different, correctly-caught defect in a different check.

**Not load-bearing to this cycle's CLEAN verdict on real data** — I
independently re-derived `src_x`/`y_lo`/`y_hi` for all three families
directly from `design_geometry.py`'s own `r{3,4,5}_config()` source above,
bit-exact against `R{3,4,5}_CONFIGS`'s stored values, so the underlying
placement truth Check 5 is meant to guard is independently confirmed
correct by a route outside this cycle's own instrument. But the
INSTRUMENT's own self-certification is incomplete: nothing in this
cycle's committed record demonstrates Check 5 would actually catch a
`native_absorb`- or `native_ny`-level corruption, despite the check's own
Idealization 41/42 discussing only the "shared-formula, not
formula-independent" scope limit and never naming this narrower,
sharper gap (which quantity within the formula is actually exercised).

**Cheap fix, matching this cycle's own idiom exactly:** add `FI-G′`
(`native_absorb=41`, not 40) and, optionally, `FI-G″` (`native_ny=1585`,
not 1584), each scored against all three families — zero new `Sim`
constructions, same cost class as the existing FI-G.

## Gap 2 (minor, non-load-bearing): `cpl_ok`'s own documented keying does not match its actual code

NOTES.md's Idealization 40 (and `run.py`'s own `check6_positional_and_cpl`
docstring, verbatim) states: *"`cpl_ok`... is STILL keyed by `pt["family"]`
on both sides... it means `cpl_ok` alone, read in isolation from
`family_ok`, is still not an independent per-point check."*

Reading the actual committed code:

```python
family_frozen = NOTES_MD_FROZEN_FAMILY_BY_LINE[line]        # keyed by notes_line
cpl_frozen, _ = NOTES_MD_FROZEN_CPL_BY_FAMILY[family_frozen] # keyed by family_frozen, NOT pt["family"]
...
cpl_ok = bool(CPL[pt["family"]] == cpl_frozen)
```

Only the **left-hand side** (`CPL[pt["family"]]`) is keyed by the untrusted
`pt["family"]` field; the right-hand side (`cpl_frozen`) is keyed by
`family_frozen`, the same independently-verified-via-`notes_line` ground
truth `family_ok` uses. This is Red Team's own fix, correctly implemented
— but it means `cpl_ok` is **not** "still family-keyed on both sides":
since `R3`/`R4`/`R5`'s `cpl` values (30/40/50) are all distinct, `cpl_ok`
actually independently re-catches a family mislabel too (redundant with
`family_ok`, confirmed by inspection of `FI_H`'s own result — both
`family_ok=False` and `cpl_ok` would independently fail there, though only
`family_ok` is surfaced in `results.json`), *in addition to* its intended,
narrower job (catching a `CPL` dict corruption at the correct family, per
`FI-F`, which it does independently and correctly). The claim in Idealization
40 under-states, not over-states, what the committed code actually
verifies — the opposite direction from the dangerous R18 failure mode,
so this creates no false confidence in untested coverage. But it is a
"claimed behavior doesn't match the actual code" instance, appearing in
the very Idealization written to correct the prior instance of that exact
shape, in a document whose own §0/Phase-1 predecessor was attacked twice
this cycle for exactly this failure class. Zero-cost fix: correct the
docstring/Idealization 40 text to state `cpl_frozen` is keyed by
`family_frozen`, not `pt["family"]`.

## Gap 3 (trivial, unverified to full rigor): standing-items ledger arithmetic

The x-wall wavelength-generality count ("TWENTY-TWO consecutive cycles
deferred, 076–097") is arithmetically exact under the inclusive-count
convention (`097−076+1=22`). The grazing-incidence count in the same line
("TEN consecutive cycles undischarged, Iterations 64–74") is not:
`74−64+1=11`, not `10` — inherited unchanged from exp-096's own already
slightly-miscounted "NINE... 64–73" (`73−64+1=10`, not `9`). I did not
trace every one of Iterations 64–73's own text to confirm whether the true
basis is "cycles elapsed" or "cycles the line was literally restated in"
(the record shows at least one gap, Iteration 66, where the line was not
verbatim-restated per Iteration 71's own "named at Iterations
64/65/67/68/69/70/71" phrasing) — flagged for completeness, zero stakes,
zero cost to reconcile.

## Verdict

**CONCUR-WITH-GAP(S).**

The core claim survives independent re-derivation cleanly: Checks 1–4/6/7
are genuine discriminators (every fault-injection scenario I re-ran
matches its prediction), the phase-ramp and taper formulas are bit-exact
reproductions of the actual FDTD source, the `y_hi`/`BASE_NY` citation
error Red Team caught is genuinely corrected in the frozen document (not
merely flagged), and the registration-readback gate's CLEAN outcome is
independently confirmed correct — both by re-executing the committed
instrument and, for Check 5's own domain specifically, by an independent
re-derivation from `design_geometry.py` source outside this cycle's own
code. Gap 1 is a genuine, previously-uncaught R18-shaped hole in the
gate's own self-certification (Check 5's `y_lo`/`y_hi` branch is
untested by its own fault injection), but it does not implicate the
underlying construction code — which I independently confirmed correct
by a route the gate itself doesn't use — so it narrows what this cycle's
own instrument has actually demonstrated about itself without reopening
the CLEAN verdict on real data.

## Is Tier 1 FDTD spend properly unblocked?

**Yes, concur — with Gap 1 tracked forward, not gating.** The registration
axes that matter for the next real FDTD spend (resolution, angle,
placement, phase-ramp, and now taper and NOTES.md-family/`cpl`
transcription) are confirmed correct for the actual `R3`/`R4`/`R5`
construction code by two independent routes: this cycle's own
fault-injection triad, and my own from-scratch re-derivation of
`src_x`/`y_lo`/`y_hi`/taper directly from `lab/fdtd2d.py` and
`design_geometry.py`. Gap 1 is a hole in the *instrument's own
self-test*, not evidence of an actual, undetected placement defect — the
placement quantities it under-tests are independently right, checked by
me outside the gate's own machinery. There is no remaining
Tier-0-shaped reason to hold up Tier 1's real spend; Gap 1 should be
closed same-shift or in parallel (it is zero-FDTD and cheap), not treated
as a blocker.

## Ranked candidate directions for Iteration 75

1. **Item 6 (EM's original queue item, ~24 calls):** bracket the other
   three established `cpl=20` nulls at `cpl=40` — the decisive
   discriminator between a family-wide defect and feature-dependent node
   migration, now that the registration axis has been checked as
   thoroughly as it can be without real FDTD data.
2. **Item 7 (~8–16 calls):** the re-centered node-bracketing re-run at
   θ₀≈38.590° at the confirmed ≥0.5° single-sided half-width — the direct
   payoff of the two-cycle registration detour.
3. **This review's own Gap 1 (zero-FDTD, same-shift-affordable):** add
   `FI-G′`/`FI-G″` to Check 5 (corrupt `native_absorb`/`native_ny` rather
   than only `native_src_x`), closing the one instrument-self-test gap
   this cycle's own R18-Tier-0 mandate did not reach. Cheap enough to run
   alongside item 6/7, not sequenced before them.

Still standing, unaffected by this cycle: PHOTONICS' own grazing-incidence
validity check (the single most-repeated undischarged item on the whole
T28 board) and the x-wall wavelength-generality leg (22 consecutive
cycles deferred) — restoring the ledger line this cycle correctly prevents
a second silent drop, but discharges neither.
