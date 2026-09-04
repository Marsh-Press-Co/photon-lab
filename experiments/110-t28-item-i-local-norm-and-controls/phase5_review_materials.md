# PHASE 5 — REVIEW · MATERIALS & METAMATERIALS · Panel Iteration 87 (exp-110)

*Fresh sub-agent, blind to every other seat's Phase-5 output this cycle.
Charter: sub-wavelength structure; what could physically realize the
proposed optical behavior. Owns the realizability bound (published /
plausible / unobtainium-with-parameters). Read PANEL.md, LOGBOOK.md in
full (RULED OUT R1–R26; T28 Iterations 83–86), the complete exp-110
directory, and exp-106's own NOTES.md/run.py (`geom_fixedabs`'s own
origin, fabrication realism) before writing this review. My own Phase-2
critique this cycle flagged the "discharges R13 and R14" claim as false —
checked below whether the fix actually landed.*

## Verdict on the Combined Verdict claim

**NOTES.md states Combined Verdict: PROMISING. I dispute that framing —
the correct verdict is CONFIRM-WITH-GAPS.** Every physically/statistically
scored item in this cycle (1a/1b/1c/1d/2/3, all 8 mandatory fixes)
genuinely, independently reproduces exactly as claimed — nothing here is
outcome-reversed. But a real, non-trivial, independently re-derived
citation-accuracy defect survives into this cycle's own frozen NOTES.md,
inside the very text that ratifies new standing rule R27 — caught by
nobody across Phase 1 (THERMODYNAMICS' own critique), Phase 2 Red Team's
audit (twice), or Phase 3 synthesis, only now at Phase 5. This is the
identical shape (an unchecked historical/multi-cycle claim, stated as
established fact, that fails to reproduce from its own cited source) that
downgraded Iteration 84/86 (exp-107/exp-109) from their own Directors'
initial framing — "PROMISING" is not earned while this stands uncorrected.

## (a) Fix 3 — "discharges R13 only," not "R13 and R14": GENUINELY LANDED

Checked directly, not trusted. `run.py::classify_item_i_local`'s own
docstring (lines 312–318): *"Discharges R13 (denominator floor-gating)
ONLY -- NOT R14 (Red Team Fix 3: a literal R14(a) numerator-parent-
smoothness check does not apply to genuinely multi-lobed diffraction-
pattern curves that are non-monotonic/non-smooth BY PHYSICS, not by
artifact)."* `grep -n "R13\|R14" NOTES.md` returns exactly three hits, all
consistent with the corrected framing (the mandatory-fixes table's own
row 3: `Correct "discharges R13 and R14" → "discharges R13 only"` —
**Implemented**). No lingering instance of the false "R13 and R14"
compound claim survives anywhere in the frozen document. **Confirmed
genuinely fixed**, not merely promised.

## (b) Fix 4 — discretization-vs-fabrication-tolerance disclaimer: GENUINELY IN THE STRING

Checked directly against `run.py`'s own `DISCLAIMER` constant (lines
361–384), not the Idealizations prose alone. The exact sentence is
present verbatim in the actual string object: *"Item 1's mirror floor
characterizes grid-discretization/floating-point noise for the IDEALIZED
simulated geometry ONLY -- a bin clearing it licenses NO inference about a
physically realized coated disk's own achievable angular-pattern symmetry
(real deposition/machining tolerances sit orders of magnitude above this
floor's ~1e-9-1e-4 scale)."* Confirmed present in both `results.json
["predictions_text"]` and `["result_text"]` (direct substring check: both
`True`). This is exactly the disclaimer my own Phase-2 critique's single
flip-condition asked for — genuinely present, not merely referenced.

## (c) Item 1a's fabrication geometry — independently re-derived, genuinely identical

Not trusted from `run.py`'s own `gate_p0()` (which could itself carry a
bug). I re-implemented the formula chain from scratch, outside any of this
cycle's own code, using only the constants named in `phase1_proposal.md`'s
own parameter table (`k=r/78`, `N/CX/CY/SRC_X/STEPS` scaled by `k`,
`R_CORE=R_COAT-ABS_THICKNESS(48)`, `sigma_max=0.5` fixed, `box_a_hw/
box_b_hw/ref_hh` from the `_32/_57/_60` margin-margin convention), and
diffed the result directly against exp-106's own committed `results.json`
(`geom_156_fixedabs`/`geom_312_fixedabs`), not via any of exp-108's or
exp-110's own gate code:

```
r=156: N=1120 CX=504 CY=560 SRC_X=128 STEPS=6400 R_CORE=108 R_COAT=156
       sigma_max=0.5 tau_shell=24.0 box_a=(284,724,340,780)
       box_b=(234,774,290,830) ref=(504,560,120)
r=312: N=2240 CX=1008 CY=1120 SRC_X=256 STEPS=12800 R_CORE=264 R_COAT=312
       sigma_max=0.5 tau_shell=24.0 box_a=(568,1448,680,1560)
       box_b=(468,1548,580,1660) ref=(1008,1120,240)
```

**Every field matches exp-106's own committed geometry exactly** — not
merely close. I also independently confirmed `chunk_runner.py`'s own
`build_sim()` (materials calls, source construction) is byte-for-byte
unchanged from exp-108's version (`diff` shows only the disclosed `SCRATCH`
path repointing and the new wall-time-logging additions — zero touch to
geometry/materials/source code), and that exp-108's own committed
`reproduction_precondition` already independently verified its own capture
against exp-106's committed ledger to `rel_dev=0.0` — confirming the
identity is transitive (exp-110 ≡ exp-108 ≡ exp-106's own fabrication
parameters), not merely a two-hop chain of trust. exp-110's own
`results.json` shows `gate_p0.pass_=True` (zero mismatches) and
`reproduction_precondition.pass_=True` (`rel_dev=0.0` exactly) at both r —
genuinely reproduced by direct file inspection, matching my own
independent hand-computation to the last digit. **The "PASS exact" claim
is real, not uncritically inherited.** From MATERIALS' own lens: this
re-capture is the identical `graded_black_shell`/`pec_disk` fabrication
geometry as exp-106's own founding UNOBTANIUM-WITH-PARAMETERS instance
(REALIZABILITY_MEMO.md AMENDMENT 6/7) — nothing in this cycle changes that
disposition, and nothing should be read as revisiting it (R1/realizability
status unchanged, not re-litigated here).

## (d) R27 — well-scoped rule, but a materially overclaimed founding-instance narrative

**The forward-looking rule text itself is reasonable and correctly
scoped**: "a numeric cost/safety/scope gate defined as a module-level
constant, referenced only in prose, is not a gate until wired into
executable code" is a sound, generically valid discipline, in the
R16/R21/... lineage. My concern is with the **evidentiary basis NOTES.md
gives for ratifying it as a founding instance** — independently checked
against primary source, not taken on the Phase-2/Red-Team chain's own
say-so, and found to be false as stated.

**NOTES.md's own text**: *"Founding instance: exp-105 through exp-108
(four-plus cycles) each reused `COST_GATE_PILOT_S`/`COST_GATE_TOTAL_S`,
invoked only in prose... grep -rn 'COST_GATE' across exp-108's own
directory finds only the two definitions and zero enforcing branches
anywhere."* Note the shape: a **four-cycle claim**, evidenced by a **grep
of exactly one cycle's directory**. I checked the other three directly:

- **exp-105's `run.py`** (line 663): `r312_committed = projected_2call_min
  < 180.0 and (wall_312_pilot / 60.0) < 90.0`, then `if r312_committed:`
  gates the r=312 article calls — a real, executing conditional (hardcoded
  literals, no named constant, but genuinely code-enforced).
- **exp-106's `run.py`** (lines 642/658, 724/729): `r312_primary_committed
  = (wall_312_empty_pilot / 60.0) < 90.0 and projected_primary_min <
  180.0`, `if r312_primary_committed:`; separately `r312_settling_
  committed = ((wall_312_empty_settling_pilot / 60.0) < 90.0 and
  projected_settling_min < 180.0)`, `if r312_settling_committed:`. Both
  are real, executing conditionals — and exp-106's own NOTES.md Result
  section reports the settling gate genuinely FIRING: the empty-scene
  settling pilot took 103.28 min, exceeded the 90-min threshold, and the
  code's own `if` branch correctly skipped both article calls for that
  leg. **This directly contradicts THERMODYNAMICS' own Phase-2 sharpest
  attack** ("Iteration 83's own r=312 defer happened by a human reading
  printed per-chunk wall times and manually stopping; nothing in the
  codebase would stop a run that blew the budget") — Iteration 83 IS
  exp-106, and the defer was a real code branch, not a human intervention.
- **exp-107's `run.py`** (lines 111, 327–329) DOES define a named
  constant, `COST_GATE_TOTAL_S = 150*60` (a different value from exp-108's
  later `180*60`) — AND wires it into a real branch:
  `r312_committed = projected_total_s <= COST_GATE_TOTAL_S`.

**So the actual pattern is: exp-105/106 enforce a cost bound via
hardcoded, code-level conditionals (no named constant at all — they
cannot have "reused `COST_GATE_PILOT_S`/`COST_GATE_TOTAL_S`… invoked only
in prose," since those names did not yet exist); exp-107 introduces a
named constant AND wires it into a real branch; exp-108 is the ONLY cycle
that defines the two named constants and never wires either into any
branch.** The genuine founding instance of "a documented numeric gate,
referenced only in prose, with zero enforcing code" is **exp-108 alone —
one cycle, not four.**

This is not a stylistic quibble — it is exactly the shape this program's
own R4 lineage (and its explicit extension: *"an aggregate flag... is not
sufficient to certify an 'every single X' claim — the resolution the
claim is made at... must be independently checked, by the cycle that
first publishes the claim AND by any later Phase-5 reviewer"*) exists to
catch. The false claim propagates through **three** of this cycle's own
review layers, not one: THERMODYNAMICS' Phase-2 critique originates it;
Red Team's Phase-2 audit repeats and extends it TWICE — §1.5's "CONFIRMED
... exactly as THERMODYNAMICS states" (which actually only re-verified
the exp-108-scoped grep, never the "manually stopping"/"back through
exp-105/106" claims) and §4's "THERMODYNAMICS is the FIRST seat... to name
that the cost gate has never been code-enforced" (again, "back through
exp-105/106" — unverified against those files); Phase-3 synthesis
(NOTES.md's own R27 text) states it as ratified fact. None of the three
layers opened exp-105/106/107's own source before asserting a claim about
what all three of those cycles did.

**Answering the assigned question directly: R27 does risk, and in this
instance actually does, over-generalize from what is really a single
founding instance (exp-108) into a fabricated "four-plus cycles" recurring
pattern.** The rule's own forward text does not need the inflated
narrative to be worth keeping — a single genuine instance is sufficient
founding precedent under this program's own R5/R6/.../R26 convention (none
of them required more than one). The fix is cheap and does not touch the
rule's own operative text: **correct NOTES.md's "Founding instance: exp-105
through exp-108 (four-plus cycles)... invoked only in prose" to "Founding
instance: exp-108 alone — exp-105/106 enforced an equivalent bound via
hardcoded conditionals, no named constant; exp-107 introduced a named
constant AND wired it into a real branch; exp-108 is the first and only
cycle in this lineage to define the names and leave them unenforced,"**
and correct THERMODYNAMICS' "human reading printed times and manually
stopping" characterization of Iteration 83 to reflect the real code
branch found in `exp-106/run.py`. Non-outcome-reversing to any of this
cycle's own scored items (R27 fires on none of them; the rule's forward
text is unaffected), but load-bearing to the LOGBOOK's own permanent
record, which a future cycle would otherwise cite as an established
four-cycle-deep precedent that never actually existed.

## Minor, non-load-bearing note

Item 1c/1d's mirror-pooled-floor bin counts (203/288 = 70.5% RESOLVED at
r=156; 222/288 = 77.1% at r=312) were independently re-summed here
(`sum(n_resolved.values())` across all 6 margins, both r, from
`results.json` directly) and reproduce exactly; the two PHOTONICS-named
bins (`-146.25°`@r=156, `+168.75°`@r=312) are independently confirmed
`resolved=False` in `results.json["named_bin_status"]` at both r, matching
NOTES.md's Result prose exactly — no discrepancy found.

## Ranked top-3 candidate directions, Iteration 88

1. **Same-shift or Iteration-88 correction to R27's founding-instance
   text** (item d, above) — cheap, zero-FDTD, protects the LOGBOOK's own
   permanent record before a future cycle cites the false "four-plus
   cycles" precedent as justification for treating a marginal future case
   harshly.
2. **Item 1's own queued fault-injection control, both sub-cases** — the
   asymmetric case (already planned) closes nothing new on its own; the
   symmetric/common-mode case (Fix 2, PHOTONICS' own named remedy) is the
   one that actually tests the floor gate's disclosed structural blind
   spot. Genuinely load-bearing before `classify_item_i_local`'s
   RESOLVED/UNRESOLVED calls — including the two named bins' own still-open
   disposition — could ever be promoted past informational status.
3. **MATERIALS' own still-open, twice-queued (Iterations 85/86) Tier-2
   item: convert Fix 4's qualitative fabrication-tolerance disclaimer into
   an actual bounded estimate.** `graded_black_shell` is a CNT-black-style
   sponge coating (per its own docstring); a literature-grounded percent-
   level azimuthal thickness/dose non-uniformity figure for dip/sputter
   coating, propagated through to a predicted angular-pattern deviation
   scale, would let a future citation state — not merely gesture at —
   how far above the ~1e-9–1e-4 discretization floor a REAL coated disk's
   own achievable pattern symmetry would sit. This is squarely this
   seat's own realizability-bound duty and remains undone after two
   consecutive cycles naming it.
