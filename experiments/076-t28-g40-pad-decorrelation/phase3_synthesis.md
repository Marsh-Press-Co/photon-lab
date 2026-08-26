# exp-076 Phase 3 — SYNTHESIS (Director)

**Panel Iteration 53.** Executes Red Team's Phase-2 audit
(`phase2_redteam_audit.md`, overall verdict **PROCEED-WITH-MANDATORY-FIXES**)
against `phase1_proposal.md`. **All 8 items of Red Team's mandatory-fix
docket are ADOPTED IN FULL. Zero overridden.** This includes, transitively,
every one of the five blind Phase-2 critiques' findings, since Red Team
itself adopted or modified all five with zero overrides of its own (see the
disposition table below, reproduced from `phase2_redteam_audit.md`'s own
"Disposition of the five critiques' proposed fixes" section).

No seat criticism is overridden this cycle. This document, `NOTES.md`, and
`run.py` implement the docket exactly as written, with one disclosed
resolution of a textual ambiguity inside the docket's own literal wording
(§2 below) — flagged, not silently decided.

---

## 1. Acceptance table

| # | Origin (critique / attack) | Finding | Red Team disposition (from `phase2_redteam_audit.md`) | Director disposition |
|---|---|---|---|---|
| 1/2 | RED TEAM, Attack 1 | §4's (a)/(b)/(c1) bands are neither mutually exclusive (`x=0.04,y=0.01` trips both (b) and (c1)) nor exhaustive (`x<y<0.116` and `y≥0.050` has no verdict — "arguably the single most physically plausible non-null result this design could return") | **MANDATORY** — rewrite so every `(x,y)≥(0,0)` maps to exactly one named outcome | **ADOPT.** Replaced with the exhaustive, mutually-exclusive 9-cell/5-outcome scheme, §3 below. |
| 2 | RED TEAM, Attack 2 (closes MATERIALS-adjacent risk raised in Attack 6) | §4(c2)'s "real evidence... interaction exists" language for `rho_pad_absorb≥1.00` contradicts `experiments/072-.../run.py`'s own documented disposition of the identical `rho_c` construction ("NOT a basis-stability check... entirely an artifact of each pair choosing its OWN T_mean"); `rho_c` was **never evaluated on real data** in this program's history (`rho_c=None`, `NOT_EVALUABLE` in the committed `results.json`) | **MANDATORY** — downgrade to a disclosed, uncalibrated, non-interaction-claiming diagnostic; correct §5 Idealization 3's "established `rho_c` convention" phrase | **ADOPT**, verbatim downgrade language. Implemented in `run.py::rho_pad_absorb()` — never compared against a verdict anywhere in the file; docstring cites the exact contradiction. |
| 3 | RED TEAM, Attack 3 | §2c's "`R_i`, `R_q`... not used for any significance claim this cycle" is a blanket overstatement — `R_q` **is** used, via `delta_P_obs`, in `rho_pad_absorb` (uncalibrated, no null attached) | **MANDATORY but trivial** — scope the sentence precisely | **ADOPT.** `run.py` output carries the precisely-scoped `R_q_disclosure` field verbatim. |
| 4 | ELECTROMAGNETISM (support-with-changes) + VISION SCIENCE (support-with-changes), combined by RED TEAM | EM: no `STEPS=2800`-vs-`4200` settling leg exists for G40's own untested (thin-boundary × large-domain) geometry — every prior settling check co-varied boundary thickness and domain size. VISION: `STEPS=2800` is asserted as G40's "established settled floor" by citation only; G40 has been run in FDTD exactly once, ever, at `STEPS=1400` (exp-065 Block PAD), never at 2800, before this cycle | **MANDATORY**, combined: EM's 2-call forward leg (θ=39°/40°, `STEPS=4200`) **and** VISION's 1-call backward differential (θ=39°, `STEPS=1400`), both before any real G40 `amp_ratio` is scored | **ADOPT**, both, as a single HALT-if-fails precondition run and checked *first*. Implemented as `block_settle_precondition()` / `settling_gate_check()`. |
| 5 | PHOTONICS (support-with-changes), MODIFIED by RED TEAM Attack 4 | Every config this cycle runs (C40/G40 at ABSORB=40, C80 at ABSORB=80) sits at an *exact integer multiple of λ* at 600nm (2λ/4λ) — precisely the resonant/aliased condition C70 was added, in this identical sub-thread's own precedent cycle, to guard against. PHOTONICS' own proposed 6-call sparse fix is real but underspecified: `amp_ratio` needs the dense, carrier-fitted window a 6-point grid cannot supply | PHOTONICS' fix **MODIFY**: replace with a 16-call G40-at-750nm leg reusing the *already-committed*, non-aliased, `STEPS=2800` `block_leg750` window (θ∈[38°,41°]) that none of the five critiques found; label advisory/narrow-window; require a future full-width leg before any wavelength-general citation | **ADOPT**, exactly as MODIFIED. Implemented as `block_leg750()` / `score_leg750()`, explicitly `advisory_only=True, decisive=False` in `results.json`. |
| 6 | RED TEAM, Attack 5 | §4(a)'s prose gloss on the 0.050 threshold is numerically **backwards**: it says "at or below" the smallest established adjacent-pair reading `C70-C80=0.020`, but `0.050 > 0.020` (2.5× larger, not smaller/equal) | **MANDATORY but trivial** — fix the sentence | **ADOPT.** Corrected prose: *"0.050 is 30% of the combined baseline `amp_ratio(C40,C80)=0.166`, well ABOVE the smallest already-established adjacent-pair reading (`C70-C80=0.020`)"* — used verbatim in `run.py`'s print output and below. |
| 7 | MATERIALS (support-with-changes) | §4's decision language breaks the `ABSORB`/`PAD` symmetry — a "reassuring" outcome is called physically-tied ("substantively `ABSORB`-depth-tied") while the alternative is framed as a physical failure ("failing to be physically tied to the graded boundary's absorption depth"), though both are the same class of pure `Sim`-construction parameter | **ADOPT**, verbatim, applied uniformly across every branch | **ADOPT.** MATERIALS' caveat is attached to every outcome using ABSORB-tied/PAD-tied language, §3 below. |
| 8 | THERMODYNAMICS (support-with-changes) | A full-text search of `phase1_proposal.md` for "sidecar/thermo/energy/absorbed/re-radiat/watt" returns zero hits — the unbroken one-sentence energy-sidecar-N/A convention every T28 instrument cycle has stated since exp-071 is silently dropped here | **ADOPT**, verbatim | **ADOPT.** Sentence carried into `NOTES.md`'s idealizations, §5 below and reproduced in §4. |

Every row above traces to a specific, independently-verified finding (Red
Team re-ran `g0e_amplitude_channel_check.py`, `design_geometry.py`, and
independently recomputed all four baseline `amp_ratio`/`delta_P_obs`
figures from committed data before writing its audit — see
`phase2_redteam_audit.md`'s own header). Nothing in this synthesis
introduces a Director-original substantive change beyond faithfully
implementing the docket; the one non-substantive resolution below closes a
literal textual gap inside item 1/2's own wording.

---

## 2. Resolving the one textual ambiguity inside docket items 1/2

The docket's prose defines the outcome mapping as:

- **PAD-TIED**: `(x=HIGH, any y) OR (x=MED, y=LOW) OR (x=MED, y=MED AND x≥y)`
- **BOTH-HIGH**: `(x=HIGH, y=HIGH)` — "a **new** category"

Read completely literally, cell `(x=HIGH, y=HIGH)` satisfies *both*
descriptions simultaneously — the exact non-mutual-exclusivity defect
Attack 1 exists to close. The only reading consistent with BOTH-HIGH being
introduced as a genuinely new, distinctly-flagged outcome (rather than dead
text that never fires) is that it is **carved out of** PAD-TIED's otherwise
catch-all `(x=HIGH, any y)` disjunct. `run.py::OUTCOME_TABLE` implements
this resolution directly as a 3×3 lookup table, so cell `(HIGH,HIGH)` maps
to `BOTH_HIGH_SUPER_ADDITIVE` only, never to `PAD_TIED`. This is disclosed
here and in the script's own docstring rather than silently decided.

---

## 3. The frozen 9-cell / 5-outcome §4 scheme

`x = amp_ratio(PAIR_PAD) = amp_ratio(C40, G40)`,
`y = amp_ratio(PAIR_ABSORB40) = amp_ratio(G40, C80)`, both ≥0 by
construction (magnitudes). Bin edges, **re-derived programmatically from the
real committed baseline at implementation time, never hand-typed (R4)** —
`run.py::baseline_reproduction_check()` reproduces
`amp_ratio(C40,C80)` two independent ways (re-fit from raw data vs. read
from exp-072's committed coefficients) and asserts they agree to
~1e-15 relative before any threshold is derived from it:

```
THRESH_LOW  = 0.3 x amp_ratio(C40,C80) = 0.3 x 0.165873 = 0.049762
THRESH_HIGH = 0.7 x amp_ratio(C40,C80) = 0.7 x 0.165873 = 0.116111
LOW  = [0, 0.049762)      MED = [0.049762, 0.116111)      HIGH = [0.116111, inf)
```

**Docket item 6, corrected threshold gloss**: 0.050 is 30% of the combined
baseline `amp_ratio(C40,C80)=0.166`, **well ABOVE** the smallest
already-established adjacent-pair reading (`C70-C80=0.020`) — not "at or
below" it, the original proposal's backwards phrasing.

The 3×3 table (verified exhaustive and mutually exclusive by direct
enumeration, `run.py::verify_outcome_table_exhaustive_and_exclusive()`,
9/9 cells covered, exactly 5 distinct outcomes):

| x \\ y | LOW | MED | HIGH |
|---|---|---|---|
| **LOW**  | BOTH-LOW / NULL | ABSORB-LEANING | **ABSORB-TIED** |
| **MED**  | PAD-TIED | ABSORB-LEANING *(x<y)* / PAD-TIED *(x≥y, incl. tie)* | ABSORB-LEANING |
| **HIGH** | PAD-TIED | PAD-TIED | **BOTH-HIGH / POSSIBLE SUPER-ADDITIVE** |

Every cell maps to exactly one of 5 names; no `(x,y)` pair is left
unclassified (closes Attack 1's exhaustiveness gap) and no pair triggers two
names at once (closes its mutual-exclusivity gap). The `x=0.04, y=0.01`
point Red Team used to demonstrate the old scheme's double-fire now resolves
cleanly to `BOTH_LOW_NULL` alone; the `x<y<0.116, y≥0.050` gap region
(e.g. `x=0.03,y=0.07` or `x=0.08,y=0.15`) now resolves to `ABSORB_LEANING`.

### Outcome interpretations (MATERIALS' caveat, docket item 7, attached
verbatim to every outcome using ABSORB-tied/PAD-tied language)

> *`ABSORB` and `PAD` are both pure numerical domain-construction parameters
> of the FDTD boundary/domain construction — neither carries more physical
> standing than the other; "ABSORB-tied" vs "PAD-tied" language describes
> which construction axis the signal empirically tracks, not a claim that
> one axis is more physically real or material than the other.*

- **ABSORB-TIED** (`x=LOW, y=HIGH`): the pure-`ABSORB` effect at fixed `PAD`
  reproduces most of the combined signal while the pure-`PAD` effect stays
  near the noise floor — every prior T28 CONFIRM-shaped reading on the
  congruent series can be re-read as substantively `ABSORB`-tied. **[MATERIALS'
  caveat applies.]**
- **ABSORB-LEANING** (`x=LOW,y=MED` or `x=MED,y=HIGH` or `x=MED,y=MED∧x<y`):
  a real but not-strictly-reassuring `ABSORB`-dominant reading — the pure-`ABSORB`
  effect is larger than the pure-`PAD` effect but does not clear the strict
  0.7× reassurance bar on its own; closes Attack 1's exhaustiveness gap.
  **[MATERIALS' caveat applies.]**
- **PAD-TIED / confound not relieved** (`x=HIGH, any y≠HIGH` or `x=MED,y=LOW`
  or `x=MED,y=MED∧x≥y`, ties included): padding alone, at fixed `ABSORB`,
  reproduces as much or more of the combined signal than the pure-`ABSORB`
  effect — five iterations of T28 causal claims on the `ABSORB` series must
  be re-read as possibly padding/domain-geometry-tied. **[MATERIALS' caveat
  applies.]**
- **BOTH-LOW / NULL** (`x=LOW,y=LOW`): neither pure-axis effect individually
  clears the smallest established baseline reading, while the combined
  `amp_ratio(C40,C80)=0.166` is 3.3× larger than either — a detectable
  non-additivity signature about the metric itself, not attributable to
  either axis.
- **BOTH-HIGH / POSSIBLE SUPER-ADDITIVE SIGNATURE** (`x=HIGH,y=HIGH`): both
  axes individually clear the strong bar — together they would nominally
  exceed the combined `C40-C80` baseline. Disclosed as informative, **not
  itself an interaction proof** — see the `rho_pad_absorb` downgrade (item 2)
  for why no interaction claim follows from this alone.

None of the five outcomes constitutes a RESOLVED/CONFIRMED-class
significance claim on `R_q` or any carrier/phase-conditioned coefficient —
`amp_ratio` reads off `A_i`/`A_q` only, is null-free and `R_q`-free
(`phase1_proposal.md` §7), unaffected by this rewrite.

---

## 4. `rho_pad_absorb` and `R_q` disclosures (docket items 2/3)

`rho_pad_absorb` (formerly §4(c2)) stays as a **disclosed, non-gating**
diagnostic only:

> *a disclosed, uncalibrated magnitude signal that cannot, by this design,
> be distinguished from an artifact of each pair's independently-fit
> carrier — the identical construction in `experiments/072-.../run.py` (the
> `rho_c`/`rho_c_common_carrier_residual` machinery) is explicitly
> documented in that file's own source comments as NOT a basis-stability or
> interaction test, and was never evaluated on real data in this program's
> history (`rho_c=None`, `NOT_EVALUABLE`, verified against the committed
> `results.json`). No interaction claim may be drawn from `rho_pad_absorb`
> alone; it is reported for future reference only.*

§2c's "`R_i`, `R_q`... not used for any significance claim this cycle" is
corrected: not used in the **gating** `amp_ratio` statistic; `R_q` **is**
used, via `delta_P_obs`, in the disclosed-only, uncalibrated
`rho_pad_absorb` diagnostic.

---

## 5. Settling precondition (docket item 4) and 750nm leg (docket item 5)

Implemented exactly as the Director's brief and the FDTD budget table
specify: 3 new calls (2× `STEPS=4200` at θ∈{39°,40°}, 1× `STEPS=1400` at
θ=39°) run and checked **before** the remaining 29-point dense sweep or any
real `amp_ratio` is scored; HALT-if-fails on the forward (`2800`-vs-`4200`)
leg, translated into the same units `amp_ratio`'s own numerator is measured
in (a shift, as a fraction of the C40-C80 baseline's own carrier amplitude,
must stay below `THRESH_LOW` at both angles) — see `run.py::
settling_gate_check()`'s docstring for the exact bar cited and why. The
backward (`2800`-vs-`1400`) differential is disclosed, never gates. The
16-call 750nm leg reuses `experiments/069-.../results.json::block_leg750`'s
exact committed window for C40/C80 (zero marginal cost for those two
configs) and is scored with raw `amp_ratio` values plus a qualitative
same-direction/opposite-direction comparison only — the 9-cell band
machinery is explicitly not applied at 750nm (narrower window, not powered
the same way).

---

## 6. Checkpoint status — criterion 4 does NOT fire this cycle

Quoting `phase2_redteam_audit.md`'s own Checkpoint-status ruling verbatim:

> *"Criterion 4 (program-integrity drift, unfalsifiable claims) is the live
> one — Attacks 1 and 2 are exactly its shape (gapped/gameable falsifiable
> bands; a physical-evidence claim contradicted by its own cited machinery)
> — but per this program's own repeated ruling (most recently
> exp-065/Iteration 42's own explicit language, "Phase 2 catching defects
> before Phase 3 freeze is the designed mechanism working, not failing"),
> it does **not** fire *provided* the docket above is applied before Phase 3
> freezes §4's language. Should Attack 1 or 2's language survive into
> `phase3_synthesis.md` unaddressed and later prove outcome-determining
> (matching the exact shape that fired Criterion 4 at Iterations 49, 50, and
> 52), that would be a fresh, mechanically predictable Criterion-4 firing at
> Phase 5 — the docket above exists specifically to prevent that."*

This document applies the full docket (§1–5 above) before any §4 language
is frozen. Attack 1's language does not survive into this synthesis — it is
replaced by the exhaustive/mutually-exclusive 9-cell scheme (§3). Attack 2's
"real evidence... interaction exists" language does not survive either — it
is replaced by the disclosed, uncalibrated, non-gating framing (§4).
**Per Red Team's own explicit ruling above, Checkpoint criterion 4 does not
fire on this cycle.** Criteria 1/2/3/5 remain correctly disengaged for the
reasons Red Team's audit already states (no constraint metric scored, no
mechanism-class boundary at issue, no engine change, Iteration 52's own
genuine narrowing keeps criterion 5 unthreatened).

---

## 7. Files

- `phase3_synthesis.md` — this document.
- `NOTES.md` — house-format record: Mandate / Setup / fixed design /
  idealizations (docket item 8 included) / FROZEN PREDICTIONS (committed
  before any run) / Result / Learned / Next (pointers, not yet filled in).
- `run.py` — the implementation. Not executed this phase (house discipline:
  predictions committed before any run — see `NOTES.md`). Desk-only pieces
  (geometry congruence, baseline `amp_ratio` reproduction, the 9-cell
  classification, the settling-gate arithmetic) verified by dry run this
  phase; the actual 50-call FDTD execution is deferred to Phase 4, pending
  Director authorization.

Revised FDTD budget (unchanged from Red Team's audit): **50 calls total**
(31 dense + 2 settle-forward + 1 settle-backward + 16 leg750), ~15–17 min
wall-clock by the established linear-scaling method.
