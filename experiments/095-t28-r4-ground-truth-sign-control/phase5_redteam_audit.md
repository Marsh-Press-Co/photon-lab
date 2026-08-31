# PHASE 5 — RED TEAM FINAL AUDIT · exp-095 · Panel Iteration 72

*Seat charter (PANEL.md, verbatim): "RED TEAM — attacks every proposal,
speaks last and hardest. Its standard is NOT textbook-physics compliance —
speculation is permitted. It kills: internal inconsistency, unfalsifiable
claims, mechanisms that cannot be expressed as simulation parameters, and
proposals that quietly violate a target constraint — especially #3. Red
Team never leads a cycle; it has no proposal of its own to protect."
Read in full, in order: PANEL.md; LOGBOOK.md (RULED OUT R1–R16 verbatim;
ESTABLISHED; LIVE THREADS, with T28's complete history Iteration 46→71,
including every Checkpoint-4 firing and non-firing precedent this
sub-thread has produced); the complete exp-095 record — `phase1_proposal.md`,
all five Phase-2 critiques, `phase2_redteam_audit.md`, `NOTES.md`, `run.py`,
`run_output.txt`, `results.json`, `gate5_wiring_defect_verification_
result.json`, and all six Phase-5 reviews (vision, photonics, materials, em,
thermodynamics, quantum). Every load-bearing figure below was independently
re-derived from `results.json`/`run_output.txt`/`NOTES.md`/LOGBOOK.md
primitives this session — not taken on any seat's word, including this
seat's own predecessor's Phase-2 audit.*

## 0. Headline re-verification, before anything else

Pulled directly from `results.json` (not from any prose restatement):

| Item | θ | `delta_scene` | `floor_pass` | Verdict |
|---|---|---|---|---|
| Rank 1a | 39.2° | −3.149521×10⁻³ | True | — |
| Rank 1a | 39.4° | −2.590877×10⁻³ | True | **PASS** |
| Rank 1c | 38.49° | −1.516840×10⁻³ | True | — |
| Rank 1c | 38.69° | −2.538531×10⁻³ | True | **FAIL** |
| Combined gate | — | — | — | `proceed_gate=false` |
| Rank 4 (corrected σ) | 38.4° | −2.938827×10⁻⁶ | **False** | **NEITHER** |

`total_fdtd_calls=20 = rank1_calls(16)+rank4_calls(4)+rank2_calls(0)+
rank3_calls(0)` — arithmetic checks. Every one of these numbers is
bit-exact across `results.json`, `run_output.txt`, and all four Phase-5
reviews that independently re-pulled it (photonics, em, materials, quantum,
vision, thermodynamics — six for six). **I find no arithmetic, wiring, or
gate-logic defect anywhere in this cycle's headline record.** This is not
in dispute among any of the seven independent parties (six blind reviews
plus this audit) who have now checked it from source. The task brief's own
summary of "what the six blind reviews found" is confirmed accurate on
every quantitative point I re-checked; nothing is overstated in the
mechanical facts.

## 1. Numbered findings, each independently adjudicated

**F1. All six headline numbers (Rank 1a PASS, Rank 1c FAIL, combined gate
HALT, Ranks 2/3 skipped, Rank 4 NEITHER) — SURVIVES, unanimous.** Re-derived
independently at §0 above. No seat disputes this; DISPUTE count is zero of
six, confirmed.

**F2. PHOTONICS' Rank-4-to-Rank-1c cross-reference (the ~0.19° migration
estimate) — SURVIVES independent re-derivation, and is the single most
load-bearing new finding in this cycle's Phase-5 record.** Re-derived from
first principles: exp-092's own located lower crossing shifted
`40.265420°→40.071838°`, `Δ=−0.193582°` (`cpl20→cpl30`) — I recomputed this
subtraction directly from `experiments/090-.../results.json::q8.
crossings_deg` and `experiments/092-.../results.json::rank1.crossing_
report.lower_crossing_cpl30`, both re-pulled, not hand-typed. This cycle's
own Rank 4 (38.4°, `cpl=30`, corrected σ=1/3) reads `frac_contrast=
5.204102×10⁻⁶` against `FLOOR=1.917438×10⁻⁴` — **2.71% of FLOOR**
(`5.204102e-6/1.917438e-4=0.02714`), i.e. `delta_scene` (`−2.938827×10⁻⁶`)
sits almost exactly on a zero. `38.590230°−38.4°=0.190230°` — matching the
independently-measured `0.194°` migration to two significant figures.
**One minor, non-substantive commensurability nit I flag under R9
discipline**: PHOTONICS'/NOTES.md's own "1.5% of FLOOR" figure divides
`|delta_scene|` (`2.939×10⁻⁶`) by `FLOOR` (`1.917×10⁻⁴`) — arithmetically
correct (`=0.0153`) but not the quantity R13's gate actually thresholds
(`frac_contrast`, giving `2.71%`, not `1.5%`). Both readings support the
identical qualitative conclusion ("far below floor, essentially on a
crossing") so this does not change PHOTONICS' conclusion, but the two
percentages should not be conflated in any future citation — a small,
disclosed, non-load-bearing correction, not a reason to discount the
finding.

**F3. PHOTONICS' magnitude-scale check — SURVIVES, order-of-magnitude
verified independently, with one caveat on sensitivity to slope-fitting
choice.** Using the `cpl=20` dense-grid points PHOTONICS cited
(`38.4°→+8.083×10⁻⁴`, `38.6°→−4.151×10⁻⁵`, `38.8°→−8.569×10⁻⁴`), I fit two
independent local slopes (the tight `38.4°→38.6°` segment: `−4.25×10⁻³`/deg;
the broader `38.4°→38.8°` segment: `−4.16×10⁻³`/deg) and, scaling by this
cycle's own measured far-field amplitude growth factor (39.2°/39.4°
comparators: `1.72×`/`1.39×`, mean `1.55×`), get predicted values at
`38.49°`/`38.69°` in the range `[+4.2, +6.6]×10⁻⁴` / `[−4.2, −6.4]×10⁻⁴` —
consistent with PHOTONICS' `±6.5×10⁻⁴` figure to within the natural
uncertainty of which slope segment is used. Ratio of observed to predicted:
**2.3×–3.6×** at 38.49°, **3.9×–6.0×** at 38.69° — both comfortably inside
PHOTONICS' claimed "2.3×–4.0×" range at the low end, and this audit's own
recomputation extends the plausible high end further, which if anything
strengthens rather than weakens the "the null has moved, not merely grown
in place" reading. Genuine, corroborating, independently-reproduced
evidence — not decisive on its own (see §2).

**F4. EM's dispersion-scaling extrapolation — SURVIVES, cleanly, on
independent re-derivation of every step of the chain.** Re-derived from
`experiments/093-.../results.json::item4`'s own filed phase columns: all
six angle ratios (`delta_phi_cpl20/delta_phi_cpl30`) cluster at
`2.2552–2.2555`, matching `(30/20)²=2.25` to `~0.24%` — confirmed by direct
division of the cited pairs (e.g. `2.577346/1.142836=2.25522`). Extrapolating
the same `O(Δx²)` scaling to `cpl=30→40`:
`delta_delta_phi(30,40)/delta_delta_phi(20,30) = 0.4375/1.2552 = 0.3485`,
applied to exp-093's own filed `predicted_dtheta(20,30)` range
(`0.0037°–0.0113°`) gives a projected `cpl=30→40` dispersion-only shift of
**`0.0013°–0.0039°`** — **25×–78× smaller** than the ±0.1° bracket half-width
(`0.1/0.0039=25.6`, `0.1/0.0013=76.9`, both independently reproduced here).
**This rules OUT smooth Yee-grid dispersion as a viable sole explanation
for Rank 1c's FAIL, at a level of independent re-derivation this audit
finds no gap in.**

**F5. EM's "observationally degenerate" framing — SURVIVES, and is the
crux finding of this entire cycle.** Gate 5 (`_run_sim_r4_sigma`, confirmed
by direct read of the described logic across all reviews and by
`gate5_wiring_defect_verification_result.json`'s own `control_pass=true`/
`injected_defect_pass=true`) checks exactly one thing: `sim.sigma_e
[shell_mask].max()` against the intended `sigma_max`. It has never, at any
point in this 19-cycle sub-thread's history (verified by a scan of every
Gate-numbered check named across LOGBOOK's own T28 record, Iterations
46–71), independently verified `cx`/`cy`/`angle_deg`/source registration.
A small, systematic coordinate or angle offset would produce **exactly**
Rank 1c's signature: PASS at amplitude-dominated far points (Rank 1a),
FAIL at phase-dominated near-null points (Rank 1c) — indistinguishable,
at a single tested null, from genuine curved-boundary staircasing
migration (which has direct, one-cycle-old precedent on this identical
construction recipe: exp-094's complete six-point reversal at
41.75°–41.90°). **Neither this cycle nor any prior cycle has run a test
that discriminates these two.**

**F6. THERMODYNAMICS' R16-clean claim — SURVIVES independent
re-verification against `results.json` directly.** I confirmed, field by
field, that every one of the ten article-bearing cells this cycle actually
spent an FDTD call on (Rank 1a ×2, Rank 1c ×2, Rank 4 ×1, each with `_c`/`_g`
legs) carries a complete `netd_row()` schema — `p_abs_w_c/g`,
`dt_ss_full_K_c/g`, `netd_classification_c/g`, `sigma_ext_cells_c/g`,
`ratio_abs_ext_raw_c/g` — present in `results.json` at every one of these
ten points, with no gap. `netd_disclaimer` travels at the top level,
byte-identical to exp-093/094's own wording (independently diffed by
VISION, confirmed here by direct comparison of the quoted strings). **R16's
own forward-elevating clause ("a third occurrence... fires Checkpoint
criterion 4 automatically") does NOT fire — there is no occurrence here at
all**, clean, first time since R16's adoption that this exact risk class
(a fresh `_full`-style metrics path on new-family code) was engaged and
closed *before* the run rather than discovered after. I additionally spot-
checked that `cell_metrics_r5` (the function that would matter had Rank 2
run) is present and correctly line-for-line mirrored, per MATERIALS' own
independent trace — though, correctly noted by every seat that touched it,
this remains unexercised code, proven present but not proven correct in
execution, since Rank 2/3 never ran.

**F7. VISION's NOTES.md structural-gap claim — SURVIVES, confirmed by
direct read of the file on disk.** I read `NOTES.md` in full: it ends after
the "Realizability bound" section (§ "N/A, for the identical reason...").
There is no `## Result`, `## Learned`, or `## Next` heading anywhere in the
document — confirmed by direct inspection, not merely a grep miss. This
document is explicitly labeled, in its own header, as "Phase 3 SYNTHESIS"
— i.e. this cycle never produced a distinct post-run write-up at all; the
frozen pre-run document is the only narrative record that exists. The
Iteration-65 CHECKPOINT's own non-discretionary rule (carried
idealizations banner mandatory at "BOTH the Predictions section AND the
Result section") is, as VISION states, currently unsatisfiable by
construction — there is no Result section for it to attach to.

**F8. The convergent six-seat finding — Rank 1c's FAIL is framed
one-sidedly toward a "registration defect"/"integrity finding" reading, not
matching R15's own addendum's explicit naming of migration as an equally
live alternative — SURVIVES, and is the second crux finding of this
cycle.** I independently traced the specific language VISION cited: `phase1_
proposal.md` §2 ("names the finding an **R4-family registration-defect
candidate**"), `NOTES.md`'s own frozen Rank-1c prediction ("the established
node **appears to have vanished**... a **genuine integrity finding**"),
`run_output.txt`'s own summary line ("**integrity finding,
Checkpoint-4-relevant**") — all three confirmed present, verbatim, on
direct read. None of the three gives equal billing to "the bracket was
undersized relative to this exact neighborhood's own already-documented
migration scale," even though — see F9 below — the data to compute that
scale was sitting in the same cycle's own crossing-set table.

**F9. QUANTUM's finding that the ±0.1° figure was never checked against
on-file calibration data before being frozen as the gating criterion —
SURVIVES, and traces further upstream than QUANTUM's own review states.**
I traced the ±0.1° figure's full provenance: QUANTUM's own Phase-2 critique
proposed it illustratively ("e.g. ±0.1°" — a placeholder, not a derived
number, per QUANTUM's own Phase-5 self-review, which I independently
confirm by reading `phase2_redteam_audit.md`'s own item 5 disposition:
"verify `delta_scene(R4)` brackets zero near θ₀≈38.590° within ±0.1°" —
the audit adopted QUANTUM's exact figure as mandatory-fix item 2, without
independently computing a calibration bound anywhere in its own text). This
matters because **this seat's own predecessor** — the Phase-2 Red Team
audit for this exact cycle — is the party that froze the figure as a
mandatory fix, and its own §1/item-1 table independently derived and
displayed the `40.0718°` `cpl=30` crossing location (for a *different*
purpose: checking Rank-1a control-angle distances) two sections away from
where it adopted the ±0.1° bracket, without connecting the two. I confirm
by direct text search that no computed shift magnitude (`0.194°`/`0.320°`/
`0.377°`) appears anywhere in `phase1_proposal.md`, `phase2_redteam_
audit.md`, or the frozen Predictions section of `NOTES.md` — only in the
"Rank-1-control-angle-distances" table (which computes static *distances*,
not cross-resolution *shifts*). This is a genuine chain-of-custody gap
spanning Phase 2 (both the critique and this seat's own predecessor's
audit) through Phase 3 (`NOTES.md` inherits the figure unchanged), caught
only at Phase 5, by design (see §3).

**F10. MATERIALS' bracket-width-vs-precedent finding — SURVIVES, and I
independently extend it.** Re-derived directly: lower crossing shift
`40.265420°→40.071838°`, `Δ=0.193582°`; upper-window shift
`41.460901°→41.781067°`, `Δ=0.320166°`; upper-second `41.460901°→
41.837653°`, `Δ=0.376752°` — all three recomputed from the cited
`results.json` files, matching MATERIALS' figures exactly. All three
**exceed** Rank 1c's ±0.1° half-width, for the *smaller* `cpl=20→30` step
(`RATIO 1.0→1.5`) than the `cpl=20→40` step (`RATIO 1.0→2.0`) Rank 1c
actually probes via the `R4` family. There is no physical reason on file
to expect a smaller migration at the larger resolution jump.

**F11. The `R5` family is fully built, gate-verified, and — per MATERIALS'
own review — has been exercised end-to-end once with real (if abbreviated)
FDTD via the fault-injection harness, though never on a scientific angle.**
Confirmed directly: `gate5_wiring_defect_verification_result.json` records
`control_pass=true`, `injected_defect_pass=true`, with the literal caught
`AssertionError` string quoted (`"...sim.sigma_e[shell_mask].max()=0.5 vs
sigma_max=0.2"`) — not a hand-typed placeholder. `results.json::gates`
shows all six `R5`-family static gates (`gate1`–`gate6`) PASS. **The block
is correct, load-bearing-ready, and should not be rebuilt from scratch by
a future cycle** (see §7, item 6).

**F12. No DISPUTE among the six Phase-5 reviews; the task brief's summary
of the review layer is accurate.** All six: CONCUR / CONCUR-WITH-GAP(S).
No two reviews contradict each other on any point I checked; the closest
to tension is MATERIALS' emphasis on the R5-family-cannot-discharge-R15
question (its own charter question, correctly scoped as "honestly N/A"
for realizability, §4 of its review) versus the other five seats'
concentration on the migration-vs-defect question — complementary framings
of the same cycle, not competing claims.

**F13. A finding this audit adds, not present at the required strength in
any single Phase-5 review: the "directional coherence" argument (QUANTUM,
§2b of its review) is weaker evidence for genuine physics than its own
framing suggests, because `R3`/`R4`/`R5` are not independent
discretizations.** QUANTUM's argument — both located migrations (the
`40.265°→40.072°` crossing and the inferred `38.590°→<38.49°` crossing)
shift toward *lower* θ, and "a wiring defect has no particular reason to
prefer one sign of angular offset over the other" — is a real, legitimate
point against an *arbitrary, random* defect. But `Idealization 17`
(carried through every T28 resolution-family cycle since exp-091, restated
verbatim in this cycle's own `r4_r5_family_disclaimer`) establishes that
`R3`, `R4`, and `R5` are all generated by the *identical, deterministic*
`r{n}_config()` recipe as a function of `RATIO` alone. A **systematic**
registration bias baked into that recipe itself (for instance, one tied to
the recipe's own half-cell rounding pattern on `PLANE_X`/`GUARD_OUT`,
present at `R3_RATIO=1.5` and `R5_RATIO=2.5` but *absent* at
`R4_RATIO=2.0` — MATERIALS' own Phase-1-critique observation, independently
re-verified in this cycle's own §3 arithmetic) would be expected to produce
a **consistent, same-direction** shift as `RATIO` increases, precisely
because it is a deterministic function of the same variable that also
drives genuine physical convergence. Directional coherence across two
points on a *shared, non-independent* construction family does not, by
itself, distinguish "genuine physics, coherently converging" from "a
recipe-level defect, coherently drifting with the same input variable" —
this is Idealization 17's own point, applied one level deeper than any
single Phase-5 review stated it. I do not find this fatal to the migration
reading (see §2) — but QUANTUM's own "modest directional coincidence in
favor of genuine migration over an arbitrary bug" claim should be read as
ruling out *only* a random/arbitrary defect, not a systematic recipe-level
one, which is exactly the class of defect this entire sub-thread (R15,
its addendum, and this cycle's own existence) was built to worry about.

## 2. The interpretive ruling: migration, registration defect, or undetermined

**My own position: genuine node migration is now the better-supported
reading of Rank 1c's FAIL — meaningfully more so than before this cycle
ran — but it is not proven to the exclusion of a systematic registration
defect, and the record should say so with both halves stated, not one.**

**What moved the needle, and how far.** Before this cycle, the ±0.1°
bracket FAIL, in isolation, would have been close to uninformative between
the two hypotheses (§1, F5/F9) — EM is right that it is "observationally
degenerate" at what Rank 1c alone measured. What changes this is
*convergent, independently-reproduced, quantitative* evidence assembled
across F2–F4 and F10, none of which existed before this cycle's own data
landed:

1. **F4 (EM) rules out smooth numerical dispersion by 25×–78×** — the one
   candidate mechanism that would NOT require trusting the `R4` family's
   own geometric registration is now quantitatively excluded. This
   narrows the live hypothesis space to exactly two: staircasing (genuine
   physics, precedented) and registration defect (unprecedented, but
   structurally undetectable by any gate this program has ever built).
2. **F2/F3 (PHOTONICS) supply an independent, quantitative anchor**: this
   cycle's own Rank 4 places the corrected-σ, `cpl=30` crossing at
   `θ≈38.4°`, a shift (`0.190°`) matching the *already-established*,
   *independently-measured* `40.265°→40.072°` migration (`0.194°`) to two
   significant figures — not merely "consistent with migration in
   principle," but a specific numeric match this program had no reason
   to expect in advance and did not engineer.
3. **F10 (MATERIALS) supplies the base rate**: every crossing on this
   channel ever tracked across a resolution step has moved by
   `0.19°–0.38°`, comfortably exceeding ±0.1°. A FAIL at ±0.1° is closer
   to the *expected* outcome under the migration hypothesis than under
   "the node genuinely vanished."

**What does NOT move the needle, and why the question stays open.** F5's
core point is untouched by any of the above: nothing this cycle ran
independently verifies the `R4` family's own geometric/angular
registration, separate from its `sigma_e` magnitude (which Gate 5 does
check). F13 shows the one argument that would most directly discriminate
"genuine convergent physics" from "a defect tied to the same input
variable" — directional coherence — is weaker than it first appears,
precisely because `R3`/`R4`/`R5` share one deterministic recipe rather than
being three independent numerical experiments. And this exact sub-thread's
own most recent precedent (exp-094, one cycle earlier, same recipe) is a
**complete, six-point sign-and-classification reversal** at 41.75°–41.90°
— a considerably larger and stranger event than a single shifted
zero-crossing would be, which is exactly why R15's own addendum (the rule
this whole cycle exists to discharge) explicitly refuses to let a
resolution family's own internal consistency be read as proof against a
"persistent recipe-level artifact."

**Stated as plainly as I can:** if forced to a single-sentence
characterization, I would write "the evidence assembled this cycle shifts
the balance of plausibility toward genuine node migration — plausibly by
something like 2:1 to 3:1, an impressionistic read of convergent-evidence
weight, not a computed posterior — but does not rise to the level of proof
this program's own house discipline (R13/R14/R15's shared standard: a
convergence-of-evidence argument is not, by itself, a discriminating test)
requires before a mechanism question is closed." **NOTES.md's own current
language ("integrity finding," "registration-defect candidate," with no
migration language anywhere at comparable weight) is now a
mischaracterization of the state of evidence and needs correcting before
this record closes** — not to declare migration proven (it is not), but to
stop presenting the *less*-supported of two live hypotheses as if it were
the *only* one on offer. This matches this program's own repeated
discipline (R4's own addendum: "don't let an overclaim from an earlier
phase survive to LOGBOOK uncorrected") applied here to an interpretive
framing rather than a numeric claim, which is a first for this specific
class of correction but squarely inside the discipline's own stated
purpose.

**What would move this further, precisely (both directions):**

- **Toward migration, decisively**: EM's bracket-the-other-three-nulls test
  (§7, item 3) — if `37.127°`, `40.265°`, and `41.461°` show a **mixed**
  result (some bracket a crossing at `cpl=40`, some don't, in a pattern
  tracking each null's own established local slope — exp-090's own Q8
  finding of a `~1.8×` slope spread across the four nulls), that is direct
  evidence for feature-dependent physics over a uniform family-wide
  defect.
- **Toward a registration defect, decisively**: the same test showing a
  **uniform** FAIL at all four nulls, in the same direction, would be hard
  to explain as four independent instances of feature-dependent migration
  and would instead point at something shared by construction.
- **Independent of any further node reading, the single most direct
  test**: QUANTUM's proposed angle-domain analog of Gate 5 (§7, item 1) —
  reading back the constructed `Sim` object's own actually-injected
  incidence angle/k-vector against the intended θ. This is the one check
  that settles the registration-defect question on its own terms, without
  depending on interpreting any further ambiguous zero-crossing, and (per
  every seat that commented on cost) is likely near-zero marginal FDTD
  cost — a code-level readback, not a new physics run.
- **What would NOT be sufficient on its own**: a wider node-bracketing
  re-run at 38.590° alone (§7, item 4), however wide, cannot by itself
  distinguish the two hypotheses — it can only locate a crossing (or
  fail to), which is consistent with either story. It sharpens the
  "where" question; it does not answer the "why" question. Useful, but
  not, alone, decisive — consistent with EM's own ranking (items 1–2
  before item 3 in EM's list).

## 3. Checkpoint criteria, worked through explicitly, all five

**Criterion 1 (a configuration passes all constraint metrics).** N/A. This
cycle is pure instrument recalibration; `results.json` scores zero
constraint-3/4 quantities anywhere. Unanimous across every seat that
addressed it (vision, materials, redteam Phase-2 audit).

**Criterion 2 (a proven mechanism-class boundary, gates clean).** N/A,
matching every T28 desk/instrument cycle since exp-069 without exception.
T1 route is explicitly N/A throughout this cycle's own record
(`phase1_proposal.md` §4, `NOTES.md`'s own T1/Realizability sections, both
independently re-verified against LOGBOOK's own unbroken T28 N/A record by
this seat's own Phase-2 predecessor and reconfirmed here).

**Criterion 3 (engine physics beyond validated bench classes).** N/A. The
`R5` family is a mechanical substitution into the already-validated
`r{n}_config()` recipe (MATERIALS' own independently-verified arithmetic,
F1 above) — no new engine machinery, no new instrument class. The only
genuinely new code this cycle wrote (`box_for_r5`, `_run_sim_r5_sigma`,
`cell_metrics_r5`, the `R5`-variant Gate 5) is a line-for-line mirror of
already-validated `R4` machinery at a new ratio, gated behind its own
mandatory new-suite static checks (Gates 1–6), all of which fired and
PASSed (`results.json::gates`, independently re-verified §0/F1/F11).

**Criterion 4 (program-integrity drift) — does NOT fire, but is named the
closest non-firing call this cycle produces, on TWO separate matters,
both discharged on this program's own established test.**

*Matter (a): the pre-registered, one-sided "registration-defect
candidate"/"integrity finding" framing (F8/F9).* This is a genuinely new
gap shape, not a recurrence of any existing R1–R16 rule (it is not a
hand-typed figure [R4], not an unverified robustness argument standing in
for a check that was never run [R8 — no affordable check was *skipped*
here; rather, an *illustrative* number was frozen without being checked
against data sitting two sections away], not a commensurability error
[R9], not a node-instability finding on the denominator or numerator [R13/
R14], not a cross-resolution boundary-trust question [R15], not a
disclaimer-persistence gap [R16]). Applying this program's own unbroken
discharge test (R6 through R16's founding texts, worked through
identically each time: caught blind, independently, before this LOGBOOK
entry; not defended against a named, affordable check the way R8's own
firing precedent required; non-load-bearing to any mechanically-computed
number, only to interpretive weight) — **all three conditions are met
here.** Six independent blind Phase-5 reviews caught this convergently and
without seeing each other's work; nothing in `NOTES.md` or `run_output.txt`
defends the one-sided framing against a named check that was available and
skipped (the calibration data existed but nobody, including this seat's own
Phase-2 predecessor, had *named* the specific check "compute the migration
scale and compare it to the bracket width" before Phase 5 — this is
materially different from R8's firing shape, where EM's own Phase-2 text
had *already named the exact check needed* and it was adopted unverified
anyway); no arithmetic or gate output is wrong. **Ruled non-firing**,
matching the founding-instance precedent every prior rule in this lineage
(R5, R6, R9, R10, R11, R12, R13, R14, R15) has received on its own first
application.

*Matter (b): VISION's NOTES.md structural gap (missing Result/Learned/
Next).* This is not a new gap shape at all — it is the identical failure
this program has already named and non-fired on twice, at exp-080 and
exp-090, both times closed same-shift by Red Team's own final audit
writing the missing section directly, "three of six Phase-5 reviews
independently converg[ing] on this same disposition unprompted" each time
(LOGBOOK, Iteration 68's own entry, quoted verbatim). This cycle: one of
six reviews (VISION) named it; no prior cycle in this specific instance's
own history to have "ignored" it. **Ruled non-firing**, matching the
exp-080/exp-090 precedent exactly, on the same discharge test.

**Neither matter (a) nor (b), individually or combined, meets the
"known, named, ignored" bar this program reserves for automatic firing
(R6/R11/R16's own shared standard)** — both were caught within the SAME
cycle's own Phase-5 layer, before any LOGBOOK entry, and neither survived
into a defended claim anywhere in this record. **Criterion 4: does NOT
fire.**

**Criterion 5 (two consecutive iterations with no logbook-advancing
result).** N/A — does not fire. exp-094 (Iteration 71) delivered a genuine,
independently-verified full-window reversal, unambiguously advancing. This
cycle (Iteration 72) delivered real, if partial, forward information: a
correctly-functioning, correctly-gated instrument that (i) saved 66 calls
on a well-justified HALT rather than spending them on a compromised
anchor, (ii) produced a genuinely new, load-bearing quantitative anchor
(Rank 4's near-total-null reading) that materially sharpens the migration-
vs-defect question for the first time, and (iii) narrowed the live
hypothesis space by ruling out smooth dispersion (F4) as an explanation.
This is not "flat" — the state of belief about T28's 38.590° null is
measurably more informed after this cycle than before it, even though the
underlying question remains open. Two consecutive non-advancing iterations
has not occurred.

## 4. Combined Verdict: **PARTIAL**

Not PROMISING (no constraint-metric progress; T1 route N/A throughout,
matching this program's own unbroken T28 desk/instrument-cycle
disposition). Not RULED OUT (no mechanism class foreclosed; the `R4`/`R5`
families remain live, gate-verified instruments). **PARTIAL**, matching
this program's own established vocabulary for a cycle that narrows a
question without closing it.

**What this cycle actually established, stated plainly:**

- A correctly-designed, correctly-executed, correctly-gated combined
  go/no-go control that did exactly what it was built to do: it caught,
  via Rank 1c specifically (the item added at Phase 2 in direct response
  to a critique this audit's own predecessor adopted), a genuine ambiguity
  that a sign-only far-field check (Rank 1a) would have missed entirely —
  VISION's own §4 finding, independently confirmed here, that this is a
  real, not hypothetical, save (a clean Rank-1a-only PASS would have
  licensed the full 66-call Rank 2/3 spend on a since-shown-fragile `R4`
  anchor).
- A cleanly-executed, honestly-reported HALT that spent 20 of 86 possible
  calls, correctly, per its own pre-registered discipline ("a FAIL is a
  reported outcome, never a crash").
- Smooth Yee-grid numerical dispersion independently, quantitatively ruled
  out (F4) as an explanation for Rank 1c's FAIL, by 25×–78×.
- A quantitative, independently-reproduced anchor (F2/F3) that shifts the
  balance of evidence toward genuine node migration at θ₀≈38.590°, without
  proving it (§2).
- A fully-built, gate-verified, once-real-FDTD-exercised `R5` (`cpl=50`)
  family (F11), correctly and appropriately left unused this cycle.
- Clean R16 compliance (F6) — the first T28 cycle since R16's adoption to
  engage this exact risk class and close it before, not after, the run.

**What this cycle did NOT establish:**

- Whether Rank 1c's FAIL reflects genuine node migration or a systematic
  registration defect — still open, per §2, though no longer symmetric.
- Whether exp-094's own headline complete-reversal finding at
  41.75°–41.90° survives — this cycle does not touch that window at all
  (its Rank 3, the sigma-comparability closes for that window, was gated
  on Rank 1 and skipped along with everything else).
- Whether the `cpl=50` third resolution point supports or refutes R15's
  addendum — Rank 2 never ran; MATERIALS' own independently-confirmed
  finding (F11's context) is that no `R5`-family outcome could have
  discharged R15's addendum alone regardless, so this is not, in itself,
  lost ground.
- A written account of any of the above in `NOTES.md` itself (F7) — the
  document that should carry this synthesis does not yet exist.

## 5. Same-shift mandatory-fix docket

*Per this task's own scope (write the audit file only — no FDTD, no git
commit), the items below are specified in full, ready for the Director to
apply directly to `NOTES.md`/`results.json`, not applied by this audit
itself.*

1. **Correct `NOTES.md`'s Rank-1c framing to weigh both hypotheses fairly,
   without declaring the question closed.** Do NOT replace "registration-
   defect candidate" with "migration, confirmed" — that would overclaim in
   the opposite direction and contradict EM's still-standing
   "observationally degenerate" point (§2). Instead, add language of the
   shape: *"This FAIL is consistent with either (a) the established node
   having genuinely migrated beyond the tested ±0.1° window — now the
   better-supported reading per this cycle's own Rank-4 anchor (§2 of
   Red Team's Phase-5 final audit: a ~0.19° shift matching exp-092's own
   independently-measured migration to two significant figures) and per
   independently-ruling-out smooth numerical dispersion (EM, 25×–78× too
   small) — or (b) a systematic registration/coordinate defect in the R4
   family's own construction, structurally undetectable by any gate this
   sub-thread has ever built (Gate 5 checks sigma_e magnitude only, never
   angular/coordinate registration). Neither is proven; see Red Team's
   Phase-5 final audit §2 for the full reasoning and the two tests that
   would discriminate them."*
2. **Write `NOTES.md`'s missing `## Result`, `## Learned`, and `## Next`
   sections.** Carry the Idealizations 1/3/6/7/8/11/16/17/21/23/24–30
   banner into the Result section per the Iteration-65 CHECKPOINT's own
   non-discretionary rule. State explicitly, in Result: the five
   headline numbers (§0 of this audit); in Learned: item 1's corrected
   framing above, plus F13's "systematic-vs-random defect" qualifier on
   the directional-coherence argument; in Next: the reconciled queue at
   §7 below.
3. **Correct the "1.5% of FLOOR" figure (F2) to state both the
   `frac_contrast/FLOOR` ratio (2.71%, the R13-gated quantity) and the
   `|delta_scene|/FLOOR` ratio (1.53%, the quantity actually cited) as
   distinct, both supporting the same qualitative conclusion — do not
   conflate them in future citations (R9-lineage, non-load-bearing this
   time).
4. **Add a one-sentence forward note, at the point Rank 1c's FAIL is
   discussed**, naming that the ±0.1° bracket width was adopted
   illustratively from a Phase-2 critique and frozen without being
   checked against the `0.194°/0.320°/0.377°` migration figures already
   computed two sections away in the same document's own crossing-set
   table (F9) — a disclosed process gap, not a numeric correction.
5. **No change required to any `results.json` field** — every number in
   it is independently re-verified correct (§0, F1–F11). This docket is
   entirely interpretive/narrative, not numeric.

## 6. New standing rule proposed and adopted: **R17**

*A tolerance, bracket, or window sized to test whether a feature (a node,
crossing, or period) is present or has moved must be justified, before the
run, against the largest already-established cross-resolution (or
cross-condition) shift magnitude on file for a comparable transition — not
adopted as an illustrative round number from the critique or proposal that
first suggested it, and not frozen by a Phase-2 audit without independently
computing that comparison even when the underlying data (e.g. a crossing
table) is already present elsewhere in the same document. Where a
narrower-than-precedented bracket returns a FAIL/negative outcome, the
pre-registered interpretive label attached to that branch must give equal
weight to "the window was undersized relative to established precedent" as
to any other named hypothesis (e.g. "registration defect") — unless a
specific, named, independently-run test has actually discriminated between
them. A future cycle that reuses an uncalibrated bracket/tolerance a second
time, after this rule is on the books, or that defends a one-sided
interpretive framing against a named, affordable calibration check that
was skipped, fires Checkpoint criterion 4 automatically, matching R6–R16's
own "known, named, ignored" standard.* **Does not fire on its own founding
instance (exp-095)**, matching R5/R6/R9/R10/R11/R12/R13/R14/R15's own
unbroken founding-instance precedent (§3, Criterion 4).

Adopted substantially as QUANTUM's own Phase-5 review named it (its own
"Standing-rule observation," offered as a recommendation for this seat to
weigh, per that review's own correctly-stated limits on its standing to
adopt a rule itself) — extended here (per F9/F13) to name the Phase-2
Red Team audit layer explicitly as subject to the same discipline R8
already applied to Phase-2 critiques and R9 applied to Phase-5 reviews:
the audit that freezes a tolerance is not exempt from checking it against
data sitting in its own document.

## 7. Reconciled Iteration-73 queue

Six seats named: VISION (widen to 38.1°–39.1°, symmetric, ~6–10 calls);
PHOTONICS (re-center at 38.0°–38.5°, using this cycle's own Rank-4 anchor,
plus a native-sigma companion); MATERIALS (≥0.4°–0.5° half-width, plus a
zero-FDTD desk bound first); EM (bracket the other three established
`cpl=20` nulls, ±0.1° each, ~24 calls — the only item that discriminates
uniform-defect from feature-dependent-migration at the node-location
level); QUANTUM (an angle-domain analog of Gate 5 — a registration
readback, likely near-zero marginal FDTD cost — plus a directional,
lower-θ-first search). These are not competing options; reconciled below
by what each is actually diagnostic of, cheapest-and-most-fundamental
first — a registration-readback gate and a bracket-the-other-nulls test
together are more decisive than either alone, and both are cheap enough to
run before any further spend on the ambiguous 38.590° window specifically.

**Rank 1 (near-zero marginal FDTD cost, code-only, the single most
fundamental unresolved question, run first).** QUANTUM's angle-domain
registration-readback gate: verify the constructed `Sim` object's own
actually-injected incidence angle/k-vector matches the intended θ, for
both the `R3` and `R4` families (retrofitting Gate 5's own runtime-check
idiom to a genuinely different quantity — geometric registration, not
sigma magnitude). If this finds a defect, every downstream item below is
reprioritized around fixing it before any further node-location spend;
if clean, it removes registration as a live explanation entirely and
converts F5's "observationally degenerate" status to "resolved in favor
of physics" without needing any further FDTD call.

**Rank 2 (zero FDTD, immediate, informs how wide Rank 3/4 below need to
be).** MATERIALS'/THERMODYNAMICS' desk bound: using already-filed data
(the `0.194°`/`0.320°`/`0.377°` migration figures), compute whether a
hypothetical `cpl=40` migration of comparable scale would land inside or
outside candidate bracket widths (±0.2°, ±0.4°, ±0.5°) at 38.590°,
informing the design of item 3/4 below rather than reusing a round number
again.

**Rank 3 (~24 calls, decisive discriminator at the node-location level).**
EM's bracket-the-other-three-established-nulls test: `37.127°`, `40.265°`,
`41.461°`, identical ±0.1° methodology to this cycle's Rank 1c, in the `R4`
family. A uniform FAIL across all four nulls (this cycle's 38.590° plus
these three) implicates a family-wide registration defect (strengthening
the case for fixing whatever Rank 1 finds); a mixed result supports
genuine, feature-dependent migration and directly re-opens the `cpl=50`
queue item with confidence Rank 1's sign check alone never gave it. Run
after Rank 1 (if Rank 1 already finds a defect, this becomes confirmatory
rather than exploratory) but does not need to wait for it if scheduling
favors running both together.

**Rank 4 (~8–16 calls, gated on Ranks 1–3 above, or run in parallel if
budget allows).** A single, reconciled node-bracketing re-run at 38.590°:
directionally weighted toward lower θ first (QUANTUM's argument and this
cycle's own Rank-4 anchor both point below 38.4°), covering at minimum
`37.9°–38.5°` in 0.1°–0.2° steps, extended to `38.9°` to also satisfy
VISION's/MATERIALS' symmetric-coverage concern, sized to comfortably clear
the `0.194°–0.377°` established-migration band (MATERIALS' `≥0.4°–0.5°`
recommendation, satisfied by this span) — with a native-sigma companion
leg at the same relocated window (PHOTONICS' own recommendation), since
R15's addendum history shows native/corrected sigma alone can flip sign at
fragile points (exp-093 Item 3, 42.0°) and 38.590° has never been checked
for this specific confound.

**Rank 5 (record hygiene, zero cost, should happen immediately, not wait
for Iteration 73's FDTD schedule).** The mandatory-fix docket at §5 above —
`NOTES.md`'s missing Result/Learned/Next sections and the corrected Rank-1c
framing — should land before any of Ranks 1–4 above are scoped into a
Phase-1 proposal, so that proposal inherits a correctly-weighted starting
point rather than NOTES.md's current one-sided language.

**Rank 6 (standing, explicitly deferred until Ranks 1–4 settle the
registration question).** Resume the `cpl=50` (`R5`) interior sweep (the
skipped Rank 2/3 of this cycle) — unanimous across every seat that
addressed sequencing (photonics, em, quantum, materials): do not spend this
budget until the registration-defect question is resolved one way or the
other. **The `R5` family is already fully built, gate-verified, and
once-exercised with real FDTD via the fault-injection harness (F11) — it
must be REUSED when this day comes, not rebuilt from scratch.** No redesign
is needed; only Rank 1's own gate (or its Iteration-73 successor) clearing
honestly.

**Standing, unranked, carried forward unchanged (lower priority than
Ranks 1–6, unaffected by this cycle):** PHOTONICS' own grazing-incidence
validity check (named at Iterations 64/65/67/68/69/70/71, now 72 —
**EIGHT** consecutive cycles undischarged, the single most-repeated item
on the whole T28 board); the x-wall wavelength-generality leg (now
**TWENTY** consecutive cycles deferred, 076–095); retrofitting Gate 5's
runtime check onto the `R3` family's own existing sigma-branch call sites
(MATERIALS' own standing rank); the unbiased margin-vs-distance rebuild
on the full 31-point window (open since exp-090); the ritualization
governance question (Iteration 61), still unresolved.
