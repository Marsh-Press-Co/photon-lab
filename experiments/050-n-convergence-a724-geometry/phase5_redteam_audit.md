# PHASE 5 — RED TEAM AUDIT · Panel Iteration 27 · exp-050

*Seventh seat, speaking last, with everything: `NOTES.md`, `results.json`,
`design_geometry.py`, `run.py`, and all six blind Phase-5 reviews
(PHOTONICS, MATERIALS, ELECTROMAGNETISM, THERMODYNAMICS, QUANTUM OPTICS,
VISION SCIENCE), plus my own predecessor's Phase-2 audit this same cycle
(`phase2_redteam_audit.md`) and exp-049's own record. Standard: internal
consistency, falsifiability, expressibility, constraint violations — not
textbook compliance. Charter: adjudicate disagreements by execution, not by
seat-counting. Every load-bearing claim below was independently re-run from
the actual committed `experiments/050-.../design_geometry.py`, not trusted
from any seat's prose, including my own predecessor's.*

---

## 0. Headline

Six blind Phase-5 seats: **PHOTONICS, MATERIALS, ELECTROMAGNETISM, QUANTUM
OPTICS PROMISING (4)**; **QUANTUM OPTICS' own verdict text is split**
(RULED OUT the specific proposed mechanism / PROMISING overall — read
correctly, this is one PROMISING vote with a named internal refutation, not
a fifth category); **THERMODYNAMICS, VISION SCIENCE PARTIAL (2)**. Raw count:
4 PROMISING + 1 PROMISING-with-a-ruled-out-sub-claim + 2 PARTIAL. Per this
program's own precedent (Iteration 26, Red Team's own ruling: "judged by
whether the cycle's own central question closed cleanly... not the raw seat
count"), the count is not the verdict. My own adjudication is below (§6).

I did three things no blind seat, individually, did in full: **(1)** ran
`beam_divergence_incoherent`'s own n=41→81 step at all three violating
coordinates *and* a fourth, unflagged near-null cell myself, from the actual
committed module, to settle the PHOTONICS-vs-(QUANTUM+EM) disagreement by
execution rather than by counting that it is 1-vs-2; **(2)** independently
re-derived THERMODYNAMICS' git-timestamp inference from `git log` directly,
not from THERMODYNAMICS' own quoted hashes; **(3)** independently reproduced
VISION's `results.json`-adjacent-cell table from both experiments' own
committed files. All three reproduce exactly. **Ruling: PROMISING, with a
mandatory same-shift disclosure/fix docket — no Checkpoint criterion fires.**

---

## ATTACK 1 — [resolved by execution] PHOTONICS vs. QUANTUM/EM: the
signed-cross-term mechanism is real but does not explain the tier
violations; QUANTUM's ruling is correct, PHOTONICS' *inference* is refuted

**What PHOTONICS got right, verified from source.** `beam_divergence_
incoherent`'s per-angle profile is `|G@amp|²` (`design_geometry.py:120`) —
algebraically non-negative pointwise. `beam_divergence_incoherent_
corrected`'s is `-Re(E·conj(H))` (`:104`) where, per `_geom_derived`
(`experiments/048-.../design_geometry.py:179-197`), `obliquity = d_sp/r` is
a full **(N,N) matrix** (one value per (observation-point, source-cell)
pair), not a per-row scalar — so `H(y) = Σ_x G0(y,x)·obliquity(y,x)·amp(x)`
is a *differently-weighted* coherent sum across source cells than
`E(y) = Σ_x G0(y,x)·amp(x)`, not a scalar multiple of it. `E` and `H` can
and do differ in phase at a given `y`, so `-Re(E·conj(H))` is a genuinely
signed, spatially-oscillating quantity, not a disguised `-obliquity·|E|²`.
This is confirmed, not assumed — I re-derived it from the two committed
`_geom_derived`/`_G_for_g` implementations directly.

**What PHOTONICS got wrong, confirmed by direct execution, not inference.**
I ran `beam_divergence_incoherent` at GEOM78 through `n∈{41,81,161,321,641}`
at all three violating coordinates:

| Cell | `incoherent` C(n) | `incoherent_corrected` C(n) | Δabs(41→81), incoh | Δabs(41→81), corrected | ratio |
|---|---|---|---|---|---|
| 36°/600nm | +1.182e-4 → **−2.311e-4** → −2.321e-4 (settled n≥161) | +3.173e-4 → **−3.691e-4** → −3.722e-4 | 3.493e-4 (passes) | 6.864e-4 (fails) | 1.97× |
| 40°/600nm | +5.663e-4 → +8.728e-4 → +8.723e-4 | +1.777e-4 → +7.664e-4 → +7.660e-4 | 3.065e-4 (passes) | 5.887e-4 (fails) | 1.92× |
| 40°/750nm | +1.115e-3 → +7.223e-4 → +7.216e-4 | +1.590e-3 → +7.040e-4 → +7.010e-4 | 3.924e-4 (passes) | 8.862e-4 (fails) | 2.26× |

(All figures independently reproduced this session by direct invocation of
`experiments/050-.../design_geometry.py`, exact to the digit against every
number QUANTUM's and ELECTROMAGNETISM's own Phase-5 reviews independently
report — three separate implementations of the same read now agree.)

`beam_divergence_incoherent` **shows the identical qualitative pathology**
at every one of the three coordinates: a large, same-order-of-magnitude
n=41→81 jump (54–197% relative), including an outright **sign flip** at
36°/600nm — the exact phenomenon PHOTONICS attributed to the corrected
convention's signed integrand alone. It differs only in *degree*: its
Δabs is consistently ~1.9–2.3× smaller than the corrected convention's,
narrowly staying under `ABS_TOL=5×10⁻⁴` at all three cells (61–78% of the
tolerance) where the corrected convention exceeds it (118–177% of the
tolerance). **This is not a coincidence of only checking three cells** — I
extended the check to the full 9-cell FWHM=20° grid and found a fourth cell,
450nm/38°, where `incoherent` *also* fails Δabs≤ABS_TOL at the 41→81 step
(5.743e-4 > 5×10⁻⁴) — it simply never registers as a "violation" in
`run.py`'s tier bookkeeping because that cell's `nstar` is already 81 at
*both* geometries (A=752 and A=724 alike — no tier *change*, so P-NCONV27-2
never sees it). PHOTONICS' own claim that "zero of `incoherent`'s 9 FWHM=20°
cells ever change tier" is true and independently reproduced by me — but
"never changes tier" is a fact about this cycle's own bookkeeping
(compares two geometries), not evidence the function is immune to near-zero
instability at either geometry individually. It is not.

**Ruling: QUANTUM's verdict ("RULED OUT" the H-vs-E-convention-specific
mechanism) is correct, confirmed by independent execution, not merely by
majority. ELECTROMAGNETISM's sharper reading — both conventions share a
genuine, fast-settling (converged by n≥161, stable to 9 s.f.) destructive-
interference null of the same underlying angular integral, and which one
trips the tier boundary is a coincidence of a *fixed* absolute tolerance
against two structurally-similar-but-not-identical-magnitude aliasing
artifacts — is the correct mechanistic account, not an artifact of EM and
QUANTUM sharing an error.** PHOTONICS was not wrong about the code (the
signed-vs-non-negative distinction is real and independently reconfirmed
here) but was wrong about its *consequence* ("making only
`incoherent_corrected` prone to near-zero sign crossings" — refuted at four
cells, not merely two of three).

**What remains genuinely open, not settled here or by any Phase-5 seat**:
QUANTUM's own Finding 2 — the ~1.9–2.3× Δabs ratio is tight and reproducible
across three wavelengths and two θ₀ values, not a single lucky/unlucky
draw. *Why* the cross-term functional (`-Re(E·conj(H))`) is systematically,
not randomly, ~2× more sensitive to angular-quadrature refinement than the
self-product functional (`|H|²`) near a shared cancellation is not derived
anywhere in this cycle's record. This is a real, secondary, unexplained
finding — QUANTUM's own Phase-5 review is the first to name it, and no
seat (including this audit) derives it. Flagged for Iteration 28, not
resolved here (§7).

**Verdict on this attack: no inconsistency, no unfalsifiable claim, no
constraint violation.** PHOTONICS' proposed mechanism was a genuine,
falsifiable hypothesis that failed a direct test — exactly the outcome
PANEL.md's Phase-5 discipline is built to produce. Nothing here needs a
fix to `NOTES.md`'s own frozen predictions (none of the 8 scored
predictions depend on this mechanistic question) — but `NOTES.md`'s Reading
section's own three-way hedge ("(a) real... (b) artifact... (c) something
else... not decided by this cycle") should be updated to reflect that this
question is now substantially, though not completely, resolved: **(b) is
confirmed as the proximate trigger (a fixed `ABS_TOL` against a shared,
comparably-sized aliasing artifact); (a) is real as a description of the
underlying physics (both functions execute a genuine near-zero angular
integral) but not "specific to `incoherent_corrected`" as originally
hedged.**

---

## ATTACK 2 — [verified, real, non-load-bearing] THERMODYNAMICS' true-cost
finding — independently re-derived from `git log` directly, confirmed

I did not trust THERMODYNAMICS' quoted hashes — I pulled the commit history
myself:

```
3139376  2026-08-20 09:47:07  Phase 4: implementation (the buggy code)
dc7170f  2026-08-20 11:31:54  Phase 4: fix field-name bug (n401 -> c401)     [gap: 1h44m47s = 6287s]
291c6dd  2026-08-20 13:15:17  Phase 4: results committed                     [gap: 1h43m23s = 6203s]
```

`results.json`'s own `meta.elapsed_s=6225.346` matches the *second* gap
(6203s) almost exactly (the ~22s residual is ordinary commit/write
overhead) — confirming that field measures only the clean, post-fix run,
exactly as THERMODYNAMICS found. **The first gap is essentially the same
size.** I independently confirmed the control-flow claim underlying the
inference: `run.py`'s `main()` calls both `sweep()` invocations
(`old = sweep(...)`, `new = sweep(...)`, the full 1944-record cost) *before*
the regression-anchor comparison loop that raised the `KeyError` — the crash
site is unreachable without first paying the full compute cost of both
geometries. A ~1h44m gap between the implementation commit and the bugfix
commit, for a bug that can only be discovered after the full sweep
completes, is the natural reading of the evidence; no cheaper explanation
(idle debugging with no execution) fits a bug that only manifests
post-sweep. **Independently reconfirmed: the disclosed `elapsed_s=6225.3s`
almost certainly represents roughly half this cycle's true compute cost
(≈12,490s / ≈208 min total across both attempts), not the ~104 minutes
`NOTES.md`'s Results section reports.**

**Is this load-bearing? No — checked directly, not asserted.** None of the
eight scored predictions (P-NCONV27-0 through -7/6b) reference wall-clock
time, cost, or runtime in their own committed bands or falsification
conditions (`NOTES.md`'s own prediction table, re-read in full for this
audit). This is a pure cost-accounting/disclosure gap, in exactly
THERMODYNAMICS' own charter lane (runtime accounting), not a science defect.
THERMODYNAMICS' second finding — that the `_G_for_g` docstring's own stated
justification for skipping a cache ("called far fewer times... than
exp-042's own dense theta sweep needed") is factually wrong, verified
against exp-049's own identical 972-calls-per-geometry loop structure — is
also independently confirmed: I compared `run.py:44-45` (this cycle) against
`experiments/049-.../run.py`'s own `CELLS`/`FUNCS`/`N_SERIES` construction
and the call counts are identical (36×3×9=972 per geometry, both cycles).
The *direction* of the attribution (no cache ⇒ real waste) is correct; the
docstring's own *reason* for accepting that waste is not.

**Ruling: real, correctly diagnosed, non-load-bearing. Mandatory same-shift
fix**: correct the `_G_for_g` docstring's stated justification, and add a
disclosed total-compute-cost line to `NOTES.md`'s Results section
(acknowledging the discarded first run's comparable cost, per THERMODYNAMICS'
own §(a) recommendation — record wall-clock from process start and persist a
partial-attempt timing record even on crash, for future geometry-
parameterized cycles).

---

## ATTACK 3 — [verified, real, materially significant, undisclosed]
VISION's threshold-breach finding at the sharpest-stakes cell's own grid
neighbors — independently reproduced from both committed `results.json`
files

I did not trust VISION's quoted table — I pulled both numbers directly from
`experiments/049-.../results.json` (`per_cell_summary`, A=752) and
`experiments/050-.../results.json` (`per_cell_summary_geom78`, A=724) at
(750nm, FWHM=2°, `incoherent_corrected`), θ₀∈{36°,38°,40°}:

| θ₀ | A=752 converged `C` | A=724 converged `C` |
|---|---|---|
| 36° | +1.7045681500076344e-3 | **−5.450293920551405e-3 — |C| > C_THR=0.005** |
| 38° | −4.006497410421138e-3 (headroom 24.8%) | +1.4646953954144948e-4 (headroom 3313.7%) |
| 40° | −2.9086034530989564e-3 | **+6.498600122495588e-3 — |C| > C_THR=0.005** |

**Exact match, digit for digit, to VISION's own reported table.** This is
not a computation outside the cycle's own grid — θ₀∈{36°,38°,40°} at
FWHM=2° is a genuine slice of exp-050's own committed 36-cell/108-row
`per_cell_summary_geom78` table (verified: all three rows are present, with
`nstar=41` at every one — n-convergence-stable, exactly as `P-NCONV27-6`
reports for the 38° member alone). VISION's "immediate 2°-step neighbors"
are literal, already-computed, already-committed grid points this cycle's
own design produced — not a new run, not an out-of-grid extrapolation.

**This is real and materially significant, for a specific, checkable
reason.** The one cell this cycle tracks as its "sharpest-stakes" citation
(38°) happens, at GEOM78, to sit almost exactly on a fringe zero-crossing
(the P-NCONV27-6b finding: 27× magnitude collapse, sign flip, 3313%
headroom) — but its immediate 2°-step neighbors on *both* sides now exceed
`C_THR` outright in the raw reading, a threshold crossing that did **not**
exist in this angular family's raw reading at A=752 (where 38° itself was
the worst point and both flanks stayed comfortably below threshold). A
future citation reading "GEOM78's sharpest-stakes cell: 3313% headroom" in
isolation would be citing the deepest null of a fringe that breaches
threshold one grid-step away in either direction — a genuinely different,
and worse, risk than the single-cell 27×-swing finding `NOTES.md` already
discloses in `P-NCONV27-6b`'s own row.

**Is this load-bearing? Narrowly no to any of this cycle's own eight scored
predictions (P-NCONV27-6/6b's own falsification bands are about
*this cell's* n-convergence and magnitude, not its neighbors — both are
scored correctly, exactly as VISION itself concludes), but yes to the
future-citation risk PANEL.md's own T21/T24 threads exist to prevent.**
This is the closest thing in this cycle's record to a constraint-3-adjacent
disclosure gap — not because this cycle claims anything about constraint 3
(it explicitly does not, idealization 9), but because the *next* cycle that
does cite a GEOM78 near-boundary headroom number is exactly the audience
PANEL.md's Tier-W/Tier-A discipline protects, and this fact is not
currently anywhere in `NOTES.md` or a LOGBOOK live thread.

**Ruling: real, mandatory same-shift disclosure fix, not a re-run.** Both
VISION's own ranked items (1: name the n-convergence≠geometry-stability
decoupling as a citable rule; 2: disclose the §3 adjacent-cell table) cost
zero new computation — the numbers already exist in the two committed
`results.json` files. Apply both to `NOTES.md`'s Reading section before this
shift closes (§8).

---

## ATTACK 4 — [checked, no defect] Is anything here R4 territory (a
hand-typed "precisely recomputed" figure that does not reproduce)?

No. Independently re-ran the mandatory regression anchor (P-NCONV27-0)
myself — all 108 rows, all three functions, bit-exact against exp-049's own
committed `per_cell_summary` (0.0 relative error), matching both my own
predecessor's Phase-2 pre-check and Phase 4's own official run. Independently
re-derived the three violating cells' full n-doubling trajectories (Attack
1, above) and VISION's adjacent-cell table (Attack 3, above) directly from
`experiments/050-.../design_geometry.py` — every number I obtained matches
every number every seat (including my own Phase-2 predecessor) reported, to
the printed digit. `git diff --stat` on every exp-050 commit shows zero
`lab/` files touched (independently confirmed, matching MATERIALS' own
check). No fabricated, hand-computed, or non-reproducing figure found
anywhere in this cycle's record.

---

## ATTACK 5 — [checked, no defect] Does P-NCONV27-2's amended
exemption-zone design (my own predecessor's mandatory-fix docket) survive
Phase 4 honestly?

Yes, and it did its job exactly as designed. My own Phase-2 predecessor's
live pre-check found 1 of 6 exempted combinations violating (750nm/40°,
`incoherent_corrected`) and flagged, explicitly, that the exemption zone was
built from two mechanisms (Nyquist-proximity, grating-lobe truncation) whose
*coverage*, not whose *logic*, was untested outside the 750nm coordinates
they were computed at. Phase 4's full 108-combination sweep found exactly
that pre-registered violation **plus two more, at 600nm, outside the
exemption zone** — scored, correctly, REFUTED. This is the falsification
band working as designed, not failing: my predecessor's own docket
(`phase2_redteam_audit.md` mandatory-fix 1) explicitly reserved "any of the
102 non-exempted combinations" as the hard-falsification condition, knowing
the exemption zone's own coverage was unverified outside 750nm. Nothing
here indicates the amended design was insufficiently rigorous — it correctly
distinguished "the one violation two independent mechanisms predicted" from
"two violations neither mechanism's own domain covered," exactly the
diagnostic information a well-designed falsifiable prediction is supposed to
produce on a miss.

---

## Constraint check

No target constraint is violated or quietly dropped. Grep-confirmed: no
`REALIZABILITY_MEMO.md` reference anywhere in `experiments/050-.../`; no
constraint-3/4 verdict language anywhere in `NOTES.md`, `run.py`, or
`results.json`; T1 escape route stated as NONE and accurate (zero material
law, zero σ, zero source/engine change — every function this cycle touches
re-evaluates an already-committed desk propagator at different quadrature
orders and a different, already-committed geometry). VISION's Attack-3
finding (§3, above) touches a constraint-3-*adjacent* citation risk but does
not itself constitute this cycle dropping a constraint-3 claim, since this
cycle never makes one. **Criterion 4 is NOT fired by this audit** — see §6
for the full Checkpoint disposition.

---

## 6. Overall verdict: PROMISING

**Reasoning, per this program's own established standard (Iteration 26):
verdict turns on whether this cycle's own open questions closed, not the
raw seat count or a favorable headline number.**

The cycle's actual charge — closing the citation-scope trigger left open at
Iteration 26's close ("is n=41 safe by default at GEOM78?") — closed
cleanly and completely: **P-NCONV27-1 CONFIRMED** (global max n\*=81,
matching A=752 exactly), **P-NCONV27-5 CONFIRMED** (100% of FWHM≤10° cells
converged at n=41, matching A=752 exactly), and the regression anchor
(**P-NCONV27-0**) is bit-exact and structurally sound (§1 of the Phase-5
ELECTROMAGNETISM review, independently reconfirmed by this audit: there is
exactly one code path, exercised at both geometries, not two independently-
agreeing implementations). Nobody citing a GEOM78 `beam_divergence_*` value
at n=41 outside the FWHM=20°/`incoherent_corrected`-or-`coherent` regime
needs to defer to a future re-run.

**P-NCONV27-2's REFUTAL is genuinely informative, not a process failure —
and this audit has now substantially advanced, not merely re-confirmed, the
open question it left behind.** Three independent findings converge on the
same underlying picture: (i) the PHOTONICS-vs-QUANTUM/EM disagreement is
resolved by direct execution (Attack 1) — the H-vs-E convention is not the
origin of the pathology, both incoherent-family functions share a genuine,
fast-converging near-zero angular-integral cancellation at the T21 fringe
scale, and which one trips the fixed `ABS_TOL` gate is a magnitude
coincidence (~2×, tight and reproducible, mechanism still unexplained) —
not a qualitative difference in kind; (ii) THERMODYNAMICS' cost-disclosure
gap is real, independently re-derived from `git log` (Attack 2), and
non-load-bearing to any scored prediction; (iii) VISION's threshold-breach
finding at the sharpest-stakes cell's own immediate grid neighbors is real,
independently reproduced from both committed `results.json` files
(Attack 3), and materially sharpens the future-citation risk this cycle's
own `P-NCONV27-6b` finding first surfaced.

None of these three findings threatens any of the eight scored predictions.
None resurrects R1–R4. None constitutes an unfalsifiable claim or an
inexpressible mechanism — every quantity in this audit is a `numpy`
computation over an already-committed propagator and an already-committed
geometry, exactly as my own Phase-2 predecessor found for the proposal
itself. **This is not a RULED-OUT or PARTIAL cycle**: the instrument-
fidelity question this cycle exists to answer is closed, the one refuted
prediction sharpened rather than muddied this program's understanding (and
this audit has now sharpened it further by settling the specific mechanism
disagreement three fresh seats could not resolve among themselves), and
every disclosure gap found is a same-shift, zero-new-computation fix.

**On THERMODYNAMICS' and VISION's own PARTIAL verdicts**: both are correct
findings, both are real, and neither is downgraded here — but both are
disclosure-completeness gaps in `NOTES.md`'s own Reading section, not
defects in the science or the falsification machinery itself, matching this
program's own established distinction (e.g. Iteration 25's MATERIALS/VISION
PARTIALs, "each scoped to open items adjacent to the headline," did not
move that cycle's own PROMISING verdict). The difference this cycle is that
these two gaps are somewhat more consequential than typical adjacent-item
PARTIALs — VISION's finding in particular bears directly on how safely a
future cycle can read this cycle's own headline reassurance — which is why
both are elevated here to a **mandatory**, not optional, same-shift fix
(§8), not merely "queued."

---

## 7. Checkpoint disposition — all five criteria checked explicitly

1. **A configuration passes ALL constraint metrics.** Not applicable — no
   constraint-3/4 claim exists in this cycle's record.
2. **A proven boundary within a mechanism class.** Not applicable — no
   mechanism is proposed or tested.
3. **Synthesis requires engine physics beyond validated bench classes.**
   Not applicable — zero engine/`lab/` change, independently confirmed
   (Attack 4).
4. **Program-integrity drift (unfalsifiable claims, a constraint quietly
   dropped — especially #3).** **Does NOT fire.** Explicitly weighed, given
   the Director's specific instruction to scrutinize this criterion against
   THERMODYNAMICS' and VISION's findings: (a) no unfalsifiable claim exists
   anywhere in this cycle — every prediction, including the one REFUTED
   one, carried a numeric, pre-registered falsification band and was scored
   against it honestly; (b) no constraint is "quietly dropped" because none
   is claimed by this cycle in the first place — VISION's finding is a risk
   to a *future* citation's disclosure completeness, not evidence this
   cycle itself dropped or obscured an existing constraint-3 verdict;
   (c) THERMODYNAMICS' cost gap is confined to runtime provenance, a
   process/disclosure axis PANEL.md's criterion 4 language ("unfalsifiable
   claims... a constraint quietly dropped") does not reach; (d) this
   program's own hardened R4 tripwire (a *third* consecutive post-R4 cycle
   carrying a non-reproducing headline figure fires Checkpoint-4
   automatically, adopted Iteration 26) is not triggered — nothing in this
   cycle's record is a non-reproducing figure; every number checked in this
   audit reproduced exactly. Both defects are real, both are same-shift-
   fixable, and both are fixed below (§8) rather than escalated.
5. **Two consecutive iterations with no logbook-advancing result.** Does
   NOT fire — this cycle (a) closed a real, named citation-scope trigger
   (Iteration 26's own top priority) completely, (b) produced a genuinely
   new, informative REFUTED finding, and (c) this audit has now resolved a
   live, three-seat mechanistic disagreement by direct execution — a
   logbook-advancing result on its own charter, distinct from and additive
   to the cycle's own headline. Iteration 26 was also a logbook-advancing
   PROMISING cycle; this is not a second consecutive null result by any
   reading.

**No Checkpoint criterion fires.**

---

## 8. Mandatory-fix docket (same-shift, zero new computation)

1. **[Attack 1, Red Team]** Update `NOTES.md`'s Reading section's own
   three-way hedge on the near-zero-crossing mechanism: state plainly that
   `beam_divergence_incoherent` shows the identical qualitative near-zero
   instability at all three violating coordinates (sign flip at 36°/600nm;
   large same-sign relative jumps at 40°/600nm and 40°/750nm) and at a
   fourth cell (450nm/38°, masked from the tier count only because its
   `nstar` was already 81 at both geometries) — the H-vs-E convention is
   **not** the origin of the pathology (settled by direct execution, this
   audit and QUANTUM's Phase-5 review independently). Name the reproducible
   ~1.9–2.3× Δabs asymmetry between the two conventions as a real,
   unexplained, secondary finding, queued for Iteration 28 (§9, priority 1).
2. **[Attack 2, THERMODYNAMICS + Red Team]** Correct the `_G_for_g`
   docstring's stated justification for omitting a cache (its claim that
   this module "is called far fewer times... than exp-042's own dense theta
   sweep needed" is factually wrong — call counts are identical, 972 per
   geometry, both cycles). Add a disclosed total-compute-cost line to
   `NOTES.md`'s Results section: report both the discarded first run's
   implied ~6287s and the reported second run's 6225.3s, and adopt
   THERMODYNAMICS' own recommended house fix (persist a partial/crash-state
   timing record from process start, not just the final successful run's
   `elapsed_s`) as forward guidance for future geometry-parameterized
   cycles.
3. **[Attack 3, VISION + Red Team]** Add, verbatim, both of VISION's own
   ranked Phase-5 items to `NOTES.md`: (a) a named, citable rule — n-
   convergence CONFIRMED at a cell certifies numerical stability under
   quadrature refinement only, and licenses no inference about the physical
   value's stability under a geometry change, however small; any future
   near-boundary headroom citation must be re-measured at its own citation's
   actual geometry; (b) the adjacent-cell table itself (§3, Attack 3, above)
   — at GEOM78, the raw `incoherent_corrected` reading at 750nm/FWHM=2°
   exceeds `C_THR=0.005` at both 36° and 40°, the immediate 2°-step
   neighbors of the one cell this cycle's own headline (`P-NCONV27-6b`)
   tracks, a threshold crossing that did not exist in this angular family's
   raw reading at A=752.
4. **[Carried, cosmetic]** Nothing further needed — my own Phase-2
   predecessor's Attack-5 fix (3.72%/3.73% rounding) is already applied and
   verified in the committed `phase3_synthesis.md`/`NOTES.md` text.

All four items are zero-new-FDTD, zero-new-computation — every number they
require already exists in the two committed `results.json` files or this
audit's own direct re-execution.

---

## 9. Ranked candidate directions for Iteration 28 — reconciling all six
seats' own rankings plus this audit's own findings

1. **[Zero-FDTD, desk-only, near-unanimous — PHOTONICS #1, ELECTROMAGNETISM
   #2, MATERIALS #2, QUANTUM #1/#3, this audit's own Attack 1]** Red Team's
   own already-queued Iteration-27 priority (3), sharpened: a
   phase-corrected difficulty-predictor test scoring Δrel(41→81) against a
   predictor including (a) each cell's phase offset within its own local
   T21 fringe period, and (b) `|C(n=81)|/ABS_TOL` (PHOTONICS' own addition)
   — run across the *full* FWHM=20° grid (all 9 cells × both functions, not
   just the 3 cells that happened to trip the tier boundary this cycle),
   and derive (or numerically bound) *why* the corrected convention's
   refinement step is systematically ~1.9–2.3× larger than the original
   convention's near these near-null cells (QUANTUM's Finding 2, unexplained
   here). This single test is very likely to retire both this cycle's
   still-open questions at once (MATERIALS' own read) and is the most
   cross-seat-convergent item this cycle produced.
2. **[Zero-FDTD, desk-only, VISION's #3, now concretely motivated]** A
   sub-degree (0.25–0.5° step) angular sweep across 36°–40° at 750nm/
   FWHM=2° at GEOM78 — this cycle's own §3 finding shows the fringe swings
   from a near-perfect null to a threshold breach within 2° of arc, twice,
   on either side of the one grid point this cycle tracks; the true worst
   angle in this band is unknown at the current 2°-step resolution.
3. **[Real FDTD cost, standing item, now further motivated]** The genuine
   FDTD `ABSORB` sweep at the T21-vs-T24 geometry (LOGBOOK Iteration
   26/27's own priority (2)) — this cycle's own findings (n-convergence
   resolved to ~0% uncertainty at the sharpest-stakes cell; the fringe-phase
   swing and the adjacent-cell threshold breaches both now measured)
   converge to make T24's own uncharacterized ~0.002–0.007 boundary
   systematic the *only* remaining uncharacterized uncertainty source on
   this program's single sharpest near-boundary cell family.
4. **[MATERIALS' own charter item, 9+ iterations deferred across two
   consecutive instrument-fidelity cycles]** Build and measure the
   fixed-absolute-thickness `graded_black_shell` variant — the standing,
   repeatedly-reranked realizability item this program's own record shows
   keeps losing to instrument-fidelity cycles; MATERIALS' own rotation slot
   (Iteration 27, this cycle) did not exercise it, and the next MATERIALS
   slot is not guaranteed either without an explicit commitment.
5. **[THERMODYNAMICS' own standing item, overdue since Iteration 25]** The
   `h_eff` re-derivation for this program's two thinnest surviving
   detectability margins (exp-043 ON-endpoint, exp-045 dose-accumulation).
6. **[Low priority, performance-only, non-blocking]** Cache
   `_geom_derived(g)`/`_G_for_g` per `(geometry, lambda)` key for any future
   geometry-parameterized cycle (THERMODYNAMICS' own concrete fix,
   ~1944-call → single-digit-call reduction) — worth doing before, not
   during, the next such cycle; does not block priority 1–5 above.

**Not recommending a new numbered live thread this cycle.** The near-|C|≈0
tier-instability finding is real, reproducible, and now substantially
mechanistically clarified (§ Attack 1) — but per MATERIALS' own Phase-5
argument, independently endorsed here: it sits inside a band P-NCONV27-4
already predicted (6/9 inside the pre-registered 3–7/9 range), it is
concretely, cheaply testable (priority 1, above) rather than a standing
mystery, and its practical stakes are narrower than T21/T24's own — it
affects `nstar`-bookkeeping defaults at specific cells nobody was going to
cite at n=41 anyway, not a program-wide scored channel's decision floor.
Recommend folding VISION's §3 finding and this attack's own resolution into
**T21's existing entry** (the same underlying edge-diffraction-fringe
mechanism, now shown to also govern `beam_divergence_*`'s own integrated
quantity at a second geometry, not a new physical phenomenon) at the
Director's discretion when updating LOGBOOK.md, rather than opening a new
T-number — promote to a full live thread only if priority-1's own targeted
check comes back inconclusive or finds the ~2× asymmetry is NOT explained
by phase/near-null proximity alone.
