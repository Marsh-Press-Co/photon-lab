# Phase 5 Review — THERMODYNAMICS (exp-097, Panel Iteration 74)

*Blind review, fresh context. Charter: where absorbed energy goes; what
re-radiates and whether it would be detectable — the per-proposal energy
sidecar. This cycle is zero-FDTD, zero-mechanism, and computes no
`p_abs_w`/NETD quantity of any kind, so that half of the charter is
correctly N/A (NOTES.md states this explicitly and accurately). Applying
this seat's other established duty instead, per the task brief: the
bookkeeping discipline this seat's own prior catches (exp-096's 12-vs-10
construction-count error, its own Phase-5 catch of an 18-vs-20 naming
mismatch and a reversed containment-ratio triple) established as its
signature contribution to this sub-thread — every count/percentage/tally
claim in this cycle's Result and Learned sections, checked against actual
execution, not restated on the document's own word.*

## What was independently verified this session

**The script was actually re-run, not read.** `python3 experiments/097-
t28-r18-tier0-gate-closure/run.py` was executed fresh against this
session's own checkout and diffed field-by-field against the committed
`results.json`. **Every field matches bit-exact except `wall_time_s`**
(2.343s committed vs. 2.097s this session — expected timing noise, not a
result). Confirms, by direct execution rather than trust: the
registration-readback gate outcome (CLEAN), all nine fault-injection
scenarios (positive control + FI-A through FI-H) resolving exactly as
`results.json` records, and the construction-count dict
(`representative=16, fault_injection_new=4, fi_d_new=1,
fi_e_f_g_h_new=0, total=21`).

**The 21-construction count.** Independently re-derived from first
principles, not merely re-run: 16 representative constructions (8 points
× 2 pair members) + 4 (positive control, FI-A, FI-B, FI-C, each sharing
one `Sim` between Checks 1–4 and the new Check 7) + 1 (FI-D, genuinely
new) = 21. FI-E/F/G/H are confirmed zero-`Sim` by direct code read
(`check6_positional_and_cpl`, `check6_set_membership_OLD`,
`check5_recipe_spot_check_extended` all take pre-existing constants/dicts
as arguments — no `Sim(...)` call appears in any of the three). Matches
both the Phase-1 prediction and the executed result, exactly.

**Learned item 3's "would have silently doubled... to 41" claim, checked
by independent construction, not accepted on arithmetic alone.** I built
the counterfactual explicitly: under a naive (unshared) implementation,
Checks 1–4 need one `Sim` per point in {16 representative + 4 (PC/FI-A/
FI-B/FI-C)} = 20, and Check 7 — no longer sharing that object — needs its
own separate `Sim` at the *same* 20 points = another 20, plus FI-D (1,
inherently Check-7-only in either design). 20 + 20 + 1 = **41, confirmed
independently, not merely re-arithmetic'd from the document's own
number.** The cited figure is correct. **One nitpick, non-load-bearing:**
calling this "doubled" is a loose description, not a literal one — 21×2
= 42, not 41; it is the 20-point shared subset that doubles (40), plus
the pre-existing, already-singular FI-D construction (+1). The word
"doubled" is close enough to be a fair intuitive gloss and does not
misstate the number itself (41 is exact), but a reader taking "doubled"
literally against the stated 21 would compute 42 and find a
one-off "discrepancy" that isn't real. Worth a one-word precision fix
("would have silently grown the construction count to 41, nearly
double") if this document is ever revised — not requiring same-shift
correction, since the actual cited figure is right.

**Standing-item cycle counts, checked for monotonic consistency across
three cycles, not taken on this cycle's own word.** Grepped all three of
exp-095/096/097's own `NOTES.md` for "grazing" and "wavelength-
generality": **EIGHT** (exp-095, Iterations 64–72 implied) → **NINE**
(exp-096, "Iterations 64–73") → **TEN** (exp-097, "Iterations 64–74") for
the grazing-incidence item, and **TWENTY** → **TWENTY-ONE** → **TWENTY-
TWO** for the x-wall wavelength-generality leg, over the identical
three-cycle span. Both sequences increment by exactly 1 per cycle with no
skip or double-count — internally consistent bookkeeping, correctly
restored after Phase 1's own draft silently dropped the line (PHOTONICS'
catch, correctly adopted).

**The `y_hi` vs. `R{n}_BASE_NY` mis-citation (EM + THERMODYNAMICS'
own prior-cycle instance, independently convergent; Red Team's own
extension that it appears twice, in §0 and §2b of Phase 1).** Confirmed
fixed in the frozen NOTES.md: the Setup section now cites the correct
comparison target (`R{3,5}_CONFIGS["C40_R{3,5}"]["y_hi"]` = 2316/3860),
never `R{n}_BASE_NY` (2376/3960 — the domain-height constant, a different
quantity, offset from `y_hi` by `y_lo`). Non-load-bearing throughout
(the executable `assert` always targeted the correct field), and now also
textually correct — the fix landed where Red Team's own audit insisted it
must: in the frozen document itself, not merely noted as cosmetic.

**Check 6's family-level tautology (Red Team's own novel Phase-2 catch —
no blind critique flagged it) and its fix, independently re-verified as
correct, not merely re-read.** The Phase-1 draft's `cpl_ok` compared
`CPL[pt["family"]]` against `NOTES_MD_FROZEN_CPL_BY_FAMILY[pt["family"]]`
— both operands keyed by the same untrusted, hand-typed `family` string,
making it a family-level tautology blind to a family-mislabeling
transcription slip (exp-096's own FI-A precedent for exactly this fault
class). The shipped fix re-keys the ground truth by `notes_line`
(`NOTES_MD_FROZEN_FAMILY_BY_LINE`), independent of `pt["family"]`, and
adds `family_ok` as a genuinely independent third sub-check. FI-H (new)
directly demonstrates the fix: representative point 6 (true `R3`/38.4°/
line-511) scored with `family` overridden to `"R4"` — my own re-run
confirms `caught_by_new=True, missed_by_old=True`, exactly as predicted.
This was the single most load-bearing accounting-adjacent catch of the
cycle (a check meant to close a coverage gap sharing the coverage gap's
own shape, one cycle into R18's life) and it is genuinely closed, not
merely documented as closed.

**FI-G's 3-leg extension, checked for a coincidental false-pass risk from
rounding, not merely trusted.** Hand-verified the corrupted
`native_src_x=301` against all three ratios: R3 (1.5) → `round(451.5)=452
≠ 450`; R4 (2.0) → `round(602.0)=602 ≠ 600`; R5 (2.5) → `round(752.5)=752
≠ 750`. All three genuinely diverge from their targets regardless of
Python's round-half-to-even convention — `all_caught=True` is not a
rounding coincidence.

**Word count and house gates.** Phase 1's §1 narrative independently
recounted programmatically: 212 words, matching the document's own
figure and VISION's Phase-2 confirmation. Trust suite independently
re-run this session (`python3 lab/validation/run_all.py --only
12346789`): **41/41 green**, matching the Result section's claim. `git
status` on `lab/` confirms zero diff, matching the "zero `lab/` diff"
claim.

## Assessment against this seat's charter

The energy/thermal half of the charter is correctly, honestly N/A — no
absorbed-power, temperature-rise, or NETD quantity is computed or implied
anywhere in this cycle, and nothing in the document overreaches into that
territory (a discipline this sub-thread has needed reminding of before —
R16's own founding cycle was exactly a NETD-byproduct bookkeeping gap).
Applying the bookkeeping half instead: every tally I could independently
re-derive — the 21-construction count, the 41-construction
counterfactual, the two monotonic standing-item counters, the word count,
the fault-injection outcome table, the trust-suite/`lab/`-diff
claims — reproduces exactly. This is the cleanest bookkeeping record this
seat has reviewed in this sub-thread: no arithmetic in the Result or
Learned sections failed independent re-derivation.

## Verdict: **CONCUR-WITH-GAP(S)**

One gap named, explicitly non-load-bearing: Learned item 3's "doubled...
to 41" phrasing is a loose gloss, not a literal doubling of the actual
21-construction total (42 ≠ 41) — the cited number (41) is itself
correct, independently re-derived from first principles in this review,
not merely re-arithmetic'd. This does not touch any verdict, gate
outcome, or construction count actually used anywhere in the pipeline,
and needs no same-shift fix; naming it only in service of this seat's own
standing bookkeeping-precision duty, matching the discipline R4/R9
already hold this program to for cited figures.

No second gap found. The cycle's central claim — that R18's own Tier-0
discipline, applied to R18's own founding gate, closes the four claimed-
vs-actual coverage gaps plus a fifth (taper) without discovering a
registration defect in the underlying construction code — is fully
supported by independently re-executed evidence, not merely restated
prose.

## Ranked candidate directions for Iteration 75

1. **Tier 1 items 6+7 as one combined build: bracket the other three
   established `cpl=20` nulls at `cpl=40` (~24 calls) together with the
   re-centered node-bracketing re-run at θ₀≈38.590° (~8–16 calls), sized
   to this sub-thread's own confirmed ≥0.5° half-width (exp-096's desk
   bound).** Item 6 first within the combined build, per EM's own
   original ranking: it is the decisive discriminator between a
   family-wide registration/dispersion artifact and a feature-specific
   migration, and its answer conditions how item 7's own result should be
   read. With the registration-readback gate now genuinely
   fault-injection-verified across all seven checks (this cycle closes
   the last three), there is no remaining zero-FDTD reason to defer real
   FDTD spend on this question — the two-cycle registration detour has
   now discharged what it was built to discharge.

2. **Pre-wire `netd_row()`/`cell_metrics_r{3,4,5}` sidecar extraction into
   whichever `run.py` executes (1) above, from first commit — not
   retrofitted after the fact.** This is this seat's own standing item
   (queued at exp-096 as "THERMODYNAMICS, preventive") and is not
   optional bookkeeping: R16 fired as the "closest non-firing call" TWICE
   in this sub-thread's recent history (exp-092/093's boundary; exp-094's
   own genuinely-new-code recurrence), both on this exact pattern — a
   disclaimer or byproduct field computed but never persisted. A third
   occurrence, per the standing forward-elevating clause R16 itself
   carries, fires Checkpoint criterion 4 automatically, no further
   deliberation. Given item (1) above is the first real-FDTD cycle on
   this window since exp-094, it is also the first opportunity for a
   third occurrence — wiring the sidecar in from the first commit, not
   the fix-docket stage, is the only way to guarantee it does not become
   that occurrence.

3. **Item 9 (the `cpl=50`/`R5` interior sweep) stays deferred**, unanimous
   across every seat that has addressed sequencing since exp-095 — reuse
   the already-built, gate-verified family; do not rebuild it. Standing,
   unranked, carried forward unchanged (correctly restored this cycle):
   PHOTONICS' own grazing-incidence validity check, now ten consecutive
   cycles undischarged; the x-wall wavelength-generality leg, now
   twenty-two.
