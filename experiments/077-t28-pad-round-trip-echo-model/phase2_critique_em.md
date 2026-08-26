# PHASE 2 — CRITIQUE (ELECTROMAGNETISM, blind) · Panel Iteration 54 · exp-077

*Fresh sub-agent, ELECTROMAGNETISM charter: field/wave behavior, impedance
matching, energy coupling; owns reciprocity/passivity/causality bookkeeping.
Blind to other seats' Phase-2 critiques. Grounded on PANEL.md, LOGBOOK.md
(RULED OUT R1–R8, T28's full Iteration 46–53 history), the proposal, its
code (`pad_round_trip_model.py`), its output
(`pad_round_trip_results.json`), and the reused machinery
(`boundary_reflectance.py`, `two_wall_cavity.py`).*

---

## 1. Steel-man

From EM's own bookkeeping lens, the premise is airtight. The single-wall
model reuses exp-075's already gated machinery unchanged (G-LOSSLESS
`2.2e-16`, G-N1 `1.4e-15`, G-PASSIVITY worst `|r|=0.0064` — all re-run here,
not merely cited), and the physical isolation is verified in code, not
assumed: `load_pair_geometries` asserts `c40["absorb"]==g40["absorb"]`, so
`n(x)`/`r(theta;40)` is the *same function call* for both configs — `PAIR_PAD`
truly is a pure round-trip-distance/coherent-phase test with zero
reflectance-magnitude confound, the cleanest possible isolation of a single
mechanism class. The proposal also resists over-claiming: it reports
`PAIR_ABSORB40` as INCONCLUSIVE rather than folding it into one convenient
REFUTE headline, and names the far-wall omission explicitly (Idealization 9)
with a concrete, cheap re-target path rather than a vague disclaimer. That is
exactly the incremental, falsifiable step this six-cycle sub-thread's own
physics charter calls for.

## 2. Sharpest attack

I retargeted exp-075's own `two_wall_cavity.py` (`image_geometry_right`/
`c_empty_two_wall`) at this cycle's `(C40,G40,C80)` triple — zero new
machinery, confirming `D_right=59/99/99` cells matches the proposal's own
Idealization-9 numbers exactly — and rescored against the same real data and
same bands. **Test A's REFUTE is not robust to the omitted far-wall term**:
adding it moves `P*_model` from 13.28° to 8.67°, `rel_dev` from **1.88
(REFUTE)** to **0.88 (INCONCLUSIVE)** — nearly halving the deviation, on the
task's own pre-registered scale. The proposal's "REFUTE, same failure shape"
framing understates this: half its evidentiary basis changes *category* once
the disclosed idealization is actually priced, not just named. The Combined
Verdict survives only because Test B gets *worse*, not better
(`r²: 0.0444→0.0001`) — a computed fact, not the untested-robustness-argument
shape R8 exists to catch, but one the proposal should have run itself before
calling Idealization 9 non-load-bearing.

## 3. Independently computed two-wall extension — full numbers

Script: `/tmp/.../scratchpad/em_two_wall_pad_check.py` (this session),
retargeting `two_wall_cavity.py` verbatim at `(C40,G40,C80)`, same
`_free_period_search` staged widening, same Pearson-`r²` shape test, same
pre-registered bands (period SUPPORT≤0.30/REFUTE>1.00, shape
SUPPORT≥0.30/REFUTE≤0.05, combined = REFUTE if either test REFUTEs).

| | `D_left` | `D_right` | `P_left`(39°) | `P_right`(39°) |
|---|---|---|---|---|
| C40 | 77 | **59** | 11.824° | 15.431° |
| G40 | 117 | **99** | 7.782° | 9.196° |
| C80 | 117 | **99** | 7.782° | 9.196° |

(matches the proposal's own disclosed `D_right: 59→99→99` exactly.)

| Test | Single-wall (exp-077, as filed) | Two-wall (this check) |
|---|---|---|
| PAIR_PAD `P*_model` | 13.2794° | **8.6677°** |
| PAIR_PAD Test A `rel_dev` | 1.8798 → REFUTE | **0.8797 → INCONCLUSIVE** |
| PAIR_PAD Test B `r²` | 0.0444 → REFUTE | **0.0001 → REFUTE (harder)** |
| PAIR_PAD Combined | REFUTE | **REFUTE (unchanged, via Test B alone)** |
| PAIR_ABSORB40 `P*_model` | 8.2026° | 7.0372° |
| PAIR_ABSORB40 Test A `rel_dev` | 0.9642 → INCONCLUSIVE | 0.6851 → INCONCLUSIVE |
| PAIR_ABSORB40 Test B `r²` | 0.1997 → INCONCLUSIVE | 0.0418 → REFUTE |
| PAIR_ABSORB40 Combined | INCONCLUSIVE | **REFUTE** |

**Reading.** For `PAIR_PAD` — the task's own primary target — the Combined
Verdict (REFUTE) does NOT flip, but for a different reason than the filed
proposal's prose suggests: the far-wall term genuinely helps Test A (moving
it a full band, REFUTE→INCONCLUSIVE) but the added coherent term makes the
shape match *strictly worse*, driving Test B's already-marginal `r²=0.0444`
(itself only just under the 0.05 REFUTE ceiling) down to essentially zero
correlation (`0.0001`). Under the combining rule ("REFUTE if EITHER test
REFUTEs"), Combined REFUTE for `PAIR_PAD` is confirmed independently and is
now on firmer ground than the single-wall cut alone established, because it
no longer depends on an untested idealization. But the write-up's own
characterization — "REFUTE... same failure shape... this is not merely
REFUTE on the same wrong pair" — is not accurate as stated: the failure
*shape* changes materially (a period-dominated REFUTE becomes a
shape-dominated one), even though the label does not.

For `PAIR_ABSORB40` (secondary/control), the two-wall term is
outcome-determining in the other direction: it moves the verdict from
INCONCLUSIVE to REFUTE, because Test B's shape match — the better-behaved of
its two tests in the filed proposal (`r²=0.1997`, "correctly signed, closer
to SUPPORT") — collapses to `0.0418`, just under the REFUTE floor. This
control pair is not this cycle's headline, but it is evidence the far-wall
term is not a directionally-neutral correction; it can move a pair by a full
verdict category in either direction depending on which test it degrades.

## 4. Verdict: **support-with-changes**

The physics and the isolation logic are sound, the gates are real, and the
Combined REFUTE for `PAIR_PAD` — the task's own primary target — is
confirmed, independently, by actually running the disclosed omission rather
than arguing about it (this is exactly what R8 demands of a named,
affordable check). But the proposal cannot be adopted into LOGBOOK as filed:
its own framing that the far-wall omission leaves "the same failure shape"
is empirically false — I show Test A's REFUTE is not robust to it (flips to
INCONCLUSIVE on its own) and only Test B's REFUTE, which gets *stronger*, is
robust. A document making the REFUTE call durable rather than accidentally
correct needs to say so.

## 5. Single change that would flip my verdict to plain `support`

Fold the two-wall re-target into `pad_round_trip_model.py` itself (it is a
~40-line addition, reusing `two_wall_cavity.py` verbatim, as demonstrated
above) and report Test A/Test B for both the single- and two-wall model
side by side in §5 of `phase1_proposal.md`, with the Combined Verdict stated
as "REFUTE, robust across both single- and two-wall cuts, but for different
reasons per test" rather than "same failure shape." No new FDTD, no
re-scoring of the headline verdict required — only correcting what the
REFUTE is actually resting on.
