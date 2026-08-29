# PHASE 5 — REVIEW · MATERIALS & METAMATERIALS (blind) · exp-088 · Panel Iteration 65

*Fresh context. Read: PANEL.md in full; LOGBOOK.md's RULED OUT (R1–R13) in
full and LIVE THREADS/T28 in full through Iteration 64/exp-087; the
complete exp-088 cycle record (`phase1_proposal.md`, all five Phase-2
critiques, `phase2_redteam_audit.md`, `phase3_synthesis.md`, `NOTES.md`,
`run.py`, `results.json`); my own `phase2_critique_materials.md` this
cycle; `experiments/034-.../REALIZABILITY_MEMO.md` and the LOGBOOK
passages establishing `graded_black_shell`'s realizability disposition
(Iterations 24–29). Independently recomputed every load-bearing number
below from primitives — not trusted from any prose restatement.*

## 0. Verdict

This cycle is T28 instrument work with no realizability claim of its own
(Idealization 10, correctly scoped) — my verdict is on process/scope
soundness, not a realizability bound. **CONCUR-WITH-GAP.** The frozen
cycle executed exactly as specified, my own Phase-2 mandatory fix was
adopted correctly and applies cleanly with no internal tension, and every
arithmetic claim in the record independently reproduces bit-for-bit. But
the Result section's own headline surprise — a non-monotonic dip in
`frac_p_abs(θ)` at 38.4° — is disclosed without either of two things my
charter requires before it enters this program's discourse further: an R3
resolution check, and an explicit caveat that `graded_black_shell`'s
angular absorption profile has never been validated against any real
material. Neither gap is this cycle's fault (the dip is a Phase-4
discovery no Phase-2 critique could have anticipated), but both are
real, live, and belong on the Iteration-66 docket before any future
cycle treats the dip as physics.

## 1. My own Phase-2 fix (Idealization 13): adopted correctly, no tension found

**Present, adequate, essentially verbatim.** `NOTES.md` Idealization 13
reads: *"FLOOR/RMS[frac_contrast(θ)] are specific to `graded_black_shell`
/600nm and must be independently recomputed, not numerically reused, for
any other absorber article or wavelength this gate is later applied to."*
This is my own critique's proposed sentence, word order lightly adjusted,
substance unchanged. `phase2_redteam_audit.md` §2 and §9 item 6 confirm
adoption; `phase3_synthesis.md` item 6 confirms it was not overridden.

**Checked for the tension my own critique warned about — none found.**
I re-read the entire `NOTES.md` Result section (Q1, Q3, Q4, Q5, Q6, Q7)
looking for any place `FLOOR=1.91744×10⁻⁴` is applied, cited, or compared
against a quantity NOT drawn from `graded_black_shell`/600nm. Every
single application — the retroactive reclassification of exp-087's three
points, the two new angles' floor-pass checks, the combined 5-angle
picture — stays inside the exact material/wavelength scope the
disclaimer names. No cross-material or cross-wavelength reuse occurs
anywhere in this cycle's own record. The risk I flagged at Phase 2 (a
*future* cycle citing the bare number without recomputing it — explicitly
tied to exp-087's own queued "near-null σ(I) article" extension) remains
live as a forward risk, not a violation inside this cycle. Idealization
13 is the correct, sufficient guard for this cycle's own scope; it does
not by itself prevent the future-cycle risk, which is a citation-
discipline matter for whoever runs that extension, not a defect here.

## 2. Independent re-verification of the R13 floor-gate arithmetic

Recomputed directly from `results.json::r13_floor_gate` and from
`experiments/083-.../results.json::per_theta` raw fields, by an
independent script, not by trusting any cited table:

| Quantity | My independent computation | `results.json` | Match |
|---|---|---|---|
| RMS[frac_contrast], n=31 | `1.9174375118374476×10⁻³` | `0.0019174375118374476` | exact |
| FLOOR (`0.10×RMS`) | `1.9174375118374476×10⁻⁴` | `0.00019174375118374476` | exact |
| `frac_contrast(36.0°)` | `7.438280×10⁻⁴` (margin 3.879×) | matches | exact |
| `frac_contrast(38.6°)` | `7.410063×10⁻⁵` (margin 0.386×, FAILS) | matches | exact |
| `frac_contrast(38.4°)` | `1.437049×10⁻³` (margin 7.495×) | matches | exact |
| `frac_contrast(38.8°)` | `1.537528×10⁻³` (margin 8.019×) | matches | exact |
| `frac_contrast(41.8°)` | `1.263381×10⁻³` (margin 6.589×) | matches | exact |
| `delta_scene` zero-crossings, [36°,42°] | `37.127°, 38.590°, 40.265°, 41.461°` | matches PHOTONICS'/Red Team's cited values | exact |
| Full-window floor-gate fail count | `1/31` (38.6° only) | matches Red Team's §0 finding | exact |
| `frac_contrast(40.2°)`/`(41.4°)` margins | `1.4764×` / `1.3095×` | matches | exact |

Every number in the proposal, all five critiques, and Red Team's audit
reproduces bit-exact against my own from-scratch computation. **No
arithmetic, citation, or indexing defect anywhere.** The RMS/FLOOR
construction is internally sound: applied to the full 31-point window it
excludes exactly the one point (38.6°) it should, at the disclosed
`FLOOR_FRAC=0.10` house-style choice — the threshold itself is correctly
calibrated to this material's own curve, not merely to the two angles
this cycle happened to bracket.

## 3. Charter question: is the realizability scoping adequate, and does the `frac_p_abs(θ)` dip risk being over-read?

**Idealizations 9–10 and the historical-record disclosure are adequate
on their own literal terms** — they scope correctly (NETD is not a human-
eye threshold; this bears only on T28's confound-mechanism/energy-ledger
question; `REALIZABILITY_MEMO.md`'s verdict is not re-opened), are
carried inline at every Q1/Q4/Q5/Q6 restatement per VISION's mandatory
fix, and I independently confirmed `graded_black_shell` already carries a
formal `REALIZABILITY_MEMO.md` disposition from this program's own
record (Iteration 25/exp-048: formal entry created; Iteration 29/exp-052:
fixed-absolute-thickness variant scored **PLAUSIBLE, not PUBLISHED** —
1.44µm shell thickness sits inside the cited CNT-forest "few-µm" range,
`τ_shell`/thickness = 1/60nm never checked against a primary citation).
Idealization 10's refusal to re-score that verdict is correct and
consistent with the existing record.

**But that realizability disposition is about bulk shell thickness and
e-folding absorption length — not about the angular shape of
`frac_p_abs(θ)`.** Nothing in this program's history has ever validated
`graded_black_shell`'s θ-dependent absorption PROFILE — the shape now
under scrutiny — against any real material's own oblique-incidence
absorption response. This is exactly the gap my charter exists to catch,
and it surfaces for the first time with this cycle's own headline
surprise: `frac_p_abs`={1.9655, **1.3041**, 4.0006, 5.9552, 7.2142}×10⁻³
at θ={36.0°, 38.4°, 38.6°, 38.8°, 41.8°} — a genuine, box-dev-cleared,
non-monotonic dip at 38.4° that reads BELOW even the 36.0° value.
`NOTES.md`'s own Result section discloses this honestly and offers two
candidate readings — genuine EM structure (citing EM's own Phase-2
critique) or an artifact of the linear-interpolation prediction model's
own crudeness — and correctly declines to adjudicate between them.

**A third candidate reading is missing from that disclosure, and it is
the one my charter is best positioned to name: an FDTD grid-resolution
(cpl) artifact, unruled-out by any check this channel has ever received.**
I traced the settling/resolution history of the `sigma_abs`/`frac_p_abs`
energy-interception channel across both cycles that have used it
(exp-087, exp-088): Idealization 7 in both cycles discloses only a
*temporal settling* spot-check (`STEPS=1400` vs `2800`, one cell,
`rel_dev=7.9×10⁻⁵`) — **never a spatial-resolution (`cpl`) convergence
check**, the specific instrument this program's own R3 meta-rule
requires before any "surprising feature" is trusted or debated: *"any
surprising feature gets a resolution check before it gets a mechanism
debate — and 'artifact' claims need the check too"* (LOGBOOK.md, R3).
The original T28 confound signal (`delta_scene`, a structurally different
quantity) DID receive a `cpl` 20→30 check at exp-069; this newer,
independently-computed `sigma_abs`/`frac_p_abs` channel has not, at any
angle, in either cycle that has measured it. A dip that reads below its
own smooth-trend neighbor is precisely the shape a coarse, `dx_m=30nm`
(cpl=20) staircase discretization of a graded `sigma(r)` boundary could
produce near a specific angle without it reflecting any real absorber's
physics — and until that is checked, citing the dip as "genuine
structure" (as the disclosed EM reading already gestures toward) risks
exactly the R3 failure mode this program has hit before (R3's own
addenda, and the R5/R10 "something looks real until you check" lineage).

**Concretely, the risk the assignment asks me to bound is real and not
yet closed**: a future cycle building on this one's own queued "near-null
σ(I) article" extension, or on EM's disclosed critical-coupling framing,
could cite this dip as evidence of genuine sub-wavelength resonant
behavior in an absorber class before (a) a resolution check has ruled out
discretization artifact, and (b) anyone has checked whether
`graded_black_shell`'s specific `sigma(r)` grading law produces an
angular absorption shape any published or plausible real coating would
also produce. Neither check exists anywhere in this program's record for
this channel. This is not a defect in exp-088 itself — the dip could not
have been anticipated at Phase 2, and the Result section's own disclosure
is honest as far as it goes — it is an open gap this Phase-5 review is
the first opportunity to name.

## 4. Other findings from my own lens

- The proposal's `graded_black_shell(r_in=30, r_out=78, sigma_max=0.5,
  eps_max=1.0)` + `pec_disk(r=30)` article is confirmed bit-identical to
  exp-024/082/083/087's own construction (`dg065.CONFIGS["C40"]`/`["G40"]`)
  — no new material or geometry is introduced this cycle, so no new
  realizability question arises from the article itself.
- The historical-record disclosure (fix item 9: exp-087's own filed
  ENERGY-DOMINANT record is unedited; this cycle supplies a separate,
  forward-citable CONSISTENT reading) is the correct discipline and
  matches the R9/T16 lineage's own standard for label, not just numeric,
  commensurability. No issue found.
- `NODE-UNRESOLVABLE`'s scope gloss (fix item 10) correctly disclaims a
  scene-visibility or constraint-3 reading — no realizability-adjacent
  overclaim risk there.

## 5. Ranked top-3 for the Director's Iteration-66 queue

1. **Run an R3-mandated `cpl` resolution check on the `sigma_abs`/
   `frac_p_abs` energy-interception channel, at minimum at θ=38.4°/38.6°,
   before any future cycle treats the dip as physics or extends this
   channel to a new material.** This channel has never received a
   spatial-resolution convergence check in either cycle that has used it
   (exp-087, exp-088) — only a temporal-settling spot-check. Cheap (a
   handful of calls at existing cpl=30, reusing this cycle's own
   pipeline), and it is the specific missing instrument R3's meta-rule
   requires before the dip enters any mechanism debate.
2. **Add a disclosure — a new idealization or a Result-section addendum
   — stating that `graded_black_shell`'s angular absorption profile has
   never been validated against any published or plausible real
   material's own oblique-incidence response, distinct from the existing
   bulk-thickness/e-folding-length realizability disposition
   (`REALIZABILITY_MEMO.md`, PLAUSIBLE-not-PUBLISHED).** This closes the
   over-read risk named in §3 before exp-087's own queued "near-null σ(I)
   article" extension or any critical-coupling narrative treats the dip
   as evidence about real materials.
3. **Complete the already-committed forward tripwire** (measure `ratio_k`
   by real FDTD at the three other node-adjacent angles, ≈37.1–37.2°,
   40.2°, 41.4°) **before any channel-general CONSISTENT claim is made** —
   this was already correctly named in `NOTES.md`'s own Next section
   (Phase-2 fix item 4), but the new non-monotonic-dip finding sharpens
   its urgency: the linear-trend assumption this cycle's own Q4 band used
   to justify treating 40.2°/41.4° as "safe" extrapolations no longer
   holds now that `frac_p_abs` is shown non-monotonic near a node — those
   angles must be measured, not inferred by smooth interpolation.
