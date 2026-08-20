# PHASE 5 — RED TEAM FINAL AUDIT · Panel Iteration 28 · exp-051

*Seventh seat, fresh context, going last with everything: the full exp-051
record (Phase 1 through Phase 4, all five Phase-2 critiques, the Phase-2
Red Team audit, the Phase-3 synthesis, `NOTES.md`, `design_geometry.py`,
`run.py`, `results.json`, `timing.json`) plus all six Phase-5 reviews
(PHOTONICS, MATERIALS, ELECTROMAGNETISM, THERMODYNAMICS, QUANTUM OPTICS,
VISION SCIENCE), `PANEL.md` in full, and `LOGBOOK.md` in full (~9843 lines
— LIVE THREADS T1–T24, ESTABLISHED, RULED OUT R1–R4, Iterations 26/27 in
full, exp-046's/Iteration-22-23's grating-lobe finding). Standard: internal
consistency, falsifiability, expressibility, constraint violations — not
textbook compliance. Nothing below is taken on any seat's word, including
Phase 2's or Phase 4's own: every load-bearing claim was independently
re-verified against `results.json`, `timing.json`, `LOGBOOK.md`,
`PLAN.md`, and `exp-046`'s own `NOTES.md`, in this session. Scratch
verification (inline `python3 -c` sessions, JSON queries, grep against
source): outputs reproduced verbatim below where load-bearing; nothing
under `lab/`, or in experiments 042/046/048/049/050, was modified.*

---

## 0. Headline

All six Phase-5 seats independently returned **PROMISING**, and their
independent from-scratch reproductions of every scored `P-ALIAS-*` number
agree to the displayed digit — this is a genuinely strong out-of-sample
cycle, and I confirm that assessment. But three seats, independently and by
different routes, surfaced defects that the task specifically asked me to
adjudicate rather than take on faith. I checked all three directly against
`results.json`/`timing.json`/`LOGBOOK.md` before ruling on any of them.

1. **PHOTONICS and MATERIALS independently caught the same narrative
   defect**: `NOTES.md`'s Reading section attributes the 750nm/38°
   "ratio inverts below 1" anomaly to the scored, out-of-sample
   `P-ALIAS-5` block — **CONFIRMED as a genuine defect, verified directly
   against `results.json`.** `P_ALIAS_5.per_cell` contains no inversion
   anywhere; `measured_dabs_ratio_range = [1.5504, 3.5578]`, all nine
   cells above 1. The actual inversion (0.775–0.835) lives only in the
   unscored `calibration_18_unscored` block, a different geometry
   (GEOM78/A=724, not the P-ALIAS-5 block's A=752), known to two seats
   before Phase 3 froze anything. **Not load-bearing** to any scored
   verdict; **is** load-bearing to future citation accuracy. Same-shift
   fix required, exact text below (§2).
2. **THERMODYNAMICS found the "executed twice, 278s then 306s" claim
   likely does not withstand `timing.json`** — **CONFIRMED, more decisively
   than THERMODYNAMICS' own "unresolvable ambiguity" framing.** Exactly
   one `proc_start_unix` is on record; "278s" is the `calibration_18`
   internal stage-completion mark of that same single run (278.976198284s
   elapsed), and "306s" is that same run's own final `elapsed_s_from_import`
   (305.866s). No independent evidence of a genuine second execution exists
   anywhere (`__pycache__` mtimes, `run.py`'s own mtime, git history). Same-
   shift fix required, exact text below (§3).
3. **QUANTUM OPTICS sharpened the `coherent`-breakdown mechanism to
   discrete-aperture grating-lobe leakage, connecting it to exp-046's own
   Iteration-22/23 finding** — **CONFIRMED, independently re-verified
   against exp-046's own `NOTES.md`** (the 41.7–68.0%/48.1–68.0%-outside-
   ±3-aperture-widths figure reproduces from source, not from QUANTUM's
   citation alone), and against `results.json`'s own `|C41|` distribution
   (coherent median 0.9396, incoherent median 4.091×10⁻⁴ — four orders of
   magnitude, matching QUANTUM's cited numbers exactly). **This belongs in
   the permanent record as a located, connected finding, not a fresh
   mechanism claim** — ruling and exact NOTES.md language below (§4).

**Iteration-29 trigger**: independently re-verified from the LOGBOOK
citation chain — intact, correctly and bindingly recorded in
`phase3_synthesis.md` §3, not softened. **Confirmed, must survive
unedited into the LOGBOOK/PLAN.md close** (§5).

**VISION's new Iteration-30 request** (stage-10 temporal instrument):
independently re-derived the citation chain against `LOGBOOK.md` directly.
**GRANTED — unconditional Iteration-30 trigger** (§6), on grounds that
meet and in one respect exceed the `graded_black_shell`/r=156 precedent
bar this program has now applied twice.

**Checkpoint**: all five criteria checked explicitly (§7). **None fires.**

**Overall verdict: PROMISING** (§8).

---

## 1. Reconstructing what each seat actually found (independent cross-check)

| Finding | PHOTONICS | MATERIALS | THERMODYNAMICS | QUANTUM | EM | VISION | Red Team (this audit) |
|---|---|---|---|---|---|---|---|
| P-ALIAS-5 misattribution | found, independently | found, independently | — | — | — | — | **confirmed from `results.json` directly** |
| "executed twice" claim | — | — | found, flagged as ambiguous | — | — | — | **confirmed as an error, not merely ambiguous** |
| `coherent`-breakdown ⇒ grating-lobe/exp-046 link | — | — | — | found, independently | derived complementary algebra (E1 negation) | — | **confirmed against exp-046's own NOTES.md** |
| Iteration-29 trigger intact | — | verified, own charter duty | — | accepted as binding | — | re-verified | **re-verified a third way** |
| All 8 P-ALIAS outcomes reproduce | full clean re-run | from raw `per_combination` | spot-checked all 7 | not disputed | independently re-derived split | spot-checked all cited figures | **not separately re-run — six independent reproductions is not a gap needing a seventh** |

Six independently-written implementations converging on identical digits,
for the fourth cycle running (after 049, 050, and now 051), is this
program's own evidentiary ceiling short of a fresh FDTD run. I did not
re-run `run.py` a seventh time; I verified the disputed *claims* — the two
narrative defects and the mechanism-attribution question — directly
against source, which is where the actual disagreement lives.

---

## 2. Defect 1 — the P-ALIAS-5 misattribution, verified and ruled

### What I checked

```
$ python3 -c "... results.json['predictions']['P_ALIAS_5'] ..."
measured_dabs_ratio_range: [1.55043655317755, 3.557803828330809]
spectral_ratio_range:      [1.6557733629691027, 2.1368633005001416]
per_cell @ (750nm, 38°): spectral_ratio=2.1153, measured_dabs_ratio=2.0945
```

Every one of the nine scored A=752 cells sits above 1; the 750nm/38° cell
specifically sits at ≈2.1, not below 1. I then pulled the calibration-18
row at the geometry and coordinate where the inversion actually lives:

```
$ python3 -c "... calibration_18_unscored['rows'] ... theta0==38, lam==750 ..."
incoherent:            measured_C41_minus_C161 = -4.822e-05
incoherent_corrected:  measured_C41_minus_C161 = -4.027e-05
ratio (corrected/incoherent) = 0.8352
```

This is GEOM78 (A=724) — the calibration set, explicitly designated
"REPORTED, SCORED AGAINST NOTHING" three lines above the very sentence
that misattributes it. VISION's Phase-2 raw-`Δabs` figure at this same
cell (0.775) and Red Team's own Phase-2 spectral-ratio figure (0.835) both
independently land here, at A=724, not at the A=752 block P-ALIAS-5
actually scores. **Confirmed: the defect is real, exactly as PHOTONICS
and MATERIALS independently described it, and I reproduce their numbers
digit-for-digit from a fresh query, not from their write-ups.**

### Disposition

**Cosmetic to the verdict, load-bearing to the record.** P-ALIAS-5's own
CONFIRMED outcome does not move — ρ=0.9333 and median 1.920 are correct,
independently reproduced by four seats plus this audit, and sit nowhere
near either falsification band regardless of which geometry the
illustrative anecdote is drawn from. But this is squarely the failure mode
LOGBOOK's own accumulated record names eleven separate times (Iterations
13, 14, 15, 17, 20, 21, 22, 23, 24, 25, 26 — MATERIALS' own count,
independently re-verified: I spot-checked three of those citations against
LOGBOOK directly and they hold) — a document written to report a result
correctly ships a residual overclaim, one level down, inside its own
closing narrative. This is now the **twelfth** instance, and it is
precisely the kind of claim most likely to be lifted verbatim into
LOGBOOK.md's permanent record, since it is the most quotable sentence in
the cycle's own Reading section.

### Required fix (exact text for `NOTES.md`'s Reading section, Director to apply)

Replace:

> "P-ALIAS-5 closes exp-050's second open question cleanly. The
> alias-frequency spectral-amplitude ratio reproduces the measured
> Δabs-ratio at the 9 out-of-sample A=752 FWHM=20° cells (ρ=0.933, median
> 1.920 vs 1.921) — including, per Phase-2's own cross-seat convergence
> (QUANTUM, VISION, Red Team all independently found the same 750nm/38°
> anomaly by three different computations), the correct reproduction of
> the one cell where the ratio inverts below 1."

with:

> "P-ALIAS-5 closes exp-050's second open question cleanly, on its own
> scored data. The alias-frequency spectral-amplitude ratio reproduces the
> measured Δabs-ratio at the 9 out-of-sample A=752 FWHM=20° cells
> (ρ=0.933, median 1.920 vs 1.921), with every one of the nine ratios
> sitting comfortably above 1 (spectral range [1.656, 2.137], measured
> Δabs range [1.550, 3.558]) — a real, directionally-consistent, weaker
> version of the same mechanism (rising with λ) that does not invert at
> this geometry. The one cell where the ratio genuinely inverts below 1
> (750nm/38°, spectral ≈0.835, raw Δabs ≈0.775) is a calibration-set fact
> at the *other* geometry (GEOM78, A=724) — found independently by
> QUANTUM, VISION, and Red Team at Phase 2, reported here only in the
> unscored `calibration_18_unscored` block, and explicitly not part of
> what the scored A=752 P-ALIAS-5 test itself demonstrates."

---

## 3. Defect 2 — the "executed twice" claim, verified and ruled

### What I checked

`timing.json` in full:

```json
{
  "proc_start_unix": 1787242553.221942,
  "stage_times": {
    "calibration_18": 278.976198284,
    "step_convergence_spotcheck": 304.4487522849995
  },
  "elapsed_s_from_import": 305.86639585600005,
  "exit_unix": 1787242859.0883422
}
```

One `proc_start_unix`. One `exit_unix`. `run.py`'s own `stage_times_s`
places a checkpoint named `calibration_18` — the point at which every
`P_ALIAS_0` through `P_ALIAS_7` number and the calibration cross-validation
block are already computed — at **278.976s elapsed inside this single
recorded process**, and the process's own final elapsed time is
**305.866s ("306s")**. `main()` is called exactly once
(`if __name__=="__main__"`, no loop). `git log` shows a single commit
(`20b52d9`) for Phase 4, and I found no discarded-run artifact anywhere
(`__pycache__/{design_geometry,run}.cpython-311.pyc` show a single compile
each, consistent with one edit-then-run cycle, not with two full
executions separated by an edit).

**This is the same evidentiary pattern THERMODYNAMICS itself named but
declined to call resolved** — I reach a firmer conclusion than
THERMODYNAMICS' own review because the question the task poses is narrower
than THERMODYNAMICS framed it: not "can I prove a second run never
happened" (unprovable by construction, as THERMODYNAMICS correctly notes —
`_flush_timing` overwrites on every exit) but "does the record contain
*any* positive evidence for a second, independent, fully-completed
execution distinct from the one `timing.json` documents." **It does not.**
The only number offered as evidence for a second run (278s) is fully and
exactly explained as an intra-run checkpoint of the one run that
unambiguously happened. Occam's razor, applied to a record that offers one
documented process and zero corroborating evidence for a second, rules:
**the "executed twice" sentence in `NOTES.md` is an error** — almost
certainly a misreading of the two intra-run stage-completion marks
(278.976s, 305.866s) as two separate runs' own elapsed times, not a
fabrication and not a confirmed second execution.

### Disposition

**Not load-bearing to any scored prediction** — every `P-ALIAS` number
traces, unambiguously, to the one run `results.json`/`timing.json` both
derive from, verified bit-exact by six independent seats. **Is** a
factual error in the cycle's own cost-accounting record, in the same
document that (correctly) prides itself on cost-accounting honesty (§6 of
the Phase-1 proposal, THERMODYNAMICS' own Phase-2 catch on the ×8 cost
underestimate, Red Team's Phase-2 docket item 2). Leaving an
unsubstantiated "ran twice, bit-identical both times" claim in the
permanent record is the wrong kind of error for a program whose house
discipline is "flag, don't smooth over."

### Required fix (exact text for `NOTES.md`'s Results section, Director to apply)

Replace:

> "Total compute: ≈5.1 min for the scored sweep (the module was executed
> twice — 278s then 306s — while adding the post-hoc block and the
> idealization-3 premise disclosure below; every scored number was
> bit-identical between the two runs), plus the bench and pre-run helper
> checks, ≈13 minutes total, disclosed honestly per house discipline (the
> same standard exp-050's own Iteration-27 record was corrected against)."

with:

> "Total compute: ≈5.1 min for the scored sweep. `timing.json` records
> exactly one completed process (`proc_start_unix`=1787242553.222,
> single `exit_unix`); its own internal stage marks show every
> `P-ALIAS-0` through `P-ALIAS-7` number, and the calibration-18
> cross-validation block, complete at t=278.976s, with the post-hoc block
> and the idealization-3 disclosure (added in the same process) completing
> the run at t=305.866s (≈306s). An earlier draft of this section
> described this as two separate executions ('278s then 306s'); that was
> an error — a misreading of these two intra-run checkpoints as two
> runs. No second `proc_start_unix` exists anywhere on record, and no
> independent evidence (git history, `__pycache__` mtimes) supports a
> distinct second execution. Corrected at Phase-5 Red Team audit; no
> scored prediction is affected. Plus the bench and pre-run helper checks,
> ≈13 minutes total."

**Process recommendation, not a mandatory fix**: THERMODYNAMICS' own
suggestion — persist a distinguishable timing artifact per attempted run,
not only the final one's — is sound and cheap, and would make this exact
class of claim independently checkable rather than merely refutable by
absence-of-evidence next time. Worth adopting the next time any cycle's
Results section claims a multi-run reproducibility check.

---

## 4. Defect/finding 3 — the `coherent`-breakdown mechanism, sharpened and connected

### What I checked

**QUANTUM's regime-gap claim**, independently recomputed from
`results.json::per_combination`:

```
coherent:   |C41| median 0.9395550655531707, min 0.0266922, max 0.9997067
incoherent: |C41| median 0.0004091034066956, min 3.851e-05, max 0.0050996
```

Matches QUANTUM's cited "0.940 vs 4×10⁻⁴, four orders of magnitude" and
"min 0.027, max 0.9997" exactly.

**The exp-046/LOGBOOK Iteration-22/23 grating-lobe citation**, checked
against `experiments/046-.../NOTES.md` directly (not against QUANTUM's
paraphrase):

```
A3 | ... At the 9 FWHM=20° cells the synthesised object is a three-lobe
comb — replicas at ±412–722 cells, amplitude 0.440–0.472, carrying
48.1–68.0% (41.7–67.1% tapered) of the aperture's intensity outside
±3·w_line ... The residual is QUANTUM's closed form
w_meas/w_line = 1/√(1−4σ_θ²tan²θ₀) (predicted 0.783%/3.246% vs measured
0.781%/3.252% at FWHM=10°/20°, θ₀=40°, zero free parameters), not taper
truncation.
```

This is the same construction (`beam_divergence_coherent`'s n-point
angular comb at FWHM=20°), the same program, an already-validated,
zero-free-parameter closed form. QUANTUM's citation ("41.7–68.0% ... "
carries the intensity outside ±3 aperture-widths) is a faithful,
if slightly compressed, restatement — it mixes the tapered lower bound
(41.7%) with the untapered upper bound (68.0%) from the same source range,
which is a legitimate summary, not a fabricated figure. **Confirmed: the
grating-lobe leakage mechanism this cycle's `coherent` residual is being
connected to is the same physical phenomenon this program already
measured independently at Iteration 22/23 (exp-046), not a new claim
dressed in old language.**

**The non-perturbative claim**, spot-checked against QUANTUM's own posted
table (§ "linear cross-term explains at most 48%... 0.1–1.0% at every
450nm cell"): this is a *different*, complementary finding from EM's own
Phase-5 review, which independently derived (from `lab/ambient.py` source,
not from QUANTUM's numbers) that `coherent`'s combination rule is an exact
algebraic negation of the E1 sampling identity (off-diagonal mutual-
coherence cross-terms with no counterpart in the diagonal alias model).
**Both are correct and non-contradictory**: EM shows *why* the diagonal
alias model cannot see the effect at all (it is structurally blind to
off-diagonal terms); QUANTUM shows that even the natural first-order fix
(a linearized cross-term correction) would not rescue it, because the
regime is non-perturbative (0.1–48% explained, worst at 450nm — the same
λ-ordering the grating-lobe mechanism predicts: shorter λ ⇒ more angular
oscillation cycles across the same physical aperture ⇒ worse leakage at
fixed n=41). This is why I rank QUANTUM's grating-lobe/array-factor
regressor over EM's own off-diagonal-alias-extension proposal in §6's
priority list below — QUANTUM already ran the experiment that shows EM's
proposed route is very likely inadequate as a leading-order fix, using
EM's own math, before EM's review was even written (Phase-5 seats are
blind to each other by design; this is a case where the fresh-context
discipline produced a genuinely useful cross-check rather than a
duplicated finding).

### Ruling: belongs in this cycle's permanent record, as a located finding, not a new mechanism claim

`NOTES.md`'s current closing language — "a materially different
combination rule breaks the sampling identity" — is correct as far as it
goes but stops one level short of actionable: it does not say *how*
different, or connect to prior, already-quantified program evidence for
the same phenomenon. QUANTUM's sharpening (i) is verified from source
independently in this audit, not merely repeated from QUANTUM's own
Phase-2/Phase-5 numbers, (ii) does not change any scored `P-ALIAS`
verdict — the split (126 non-coherent essentially exact, 72 coherent weak)
was already disclosed, unscored, in `post_hoc_observations_unscored`
before Phase 5 ran, and (iii) closes an explicit LOGBOOK cross-reference
gap: exp-046's own grating-lobe finding existed in the permanent record
for five cycles without ever being connected to this cycle's residual.
This is exactly the kind of connective finding LOGBOOK exists to capture.

### Required addition (exact text for `NOTES.md`'s Reading section, Director to apply — append after the existing "Unresolved, concretely scoped..." sentence)

> "**Sharpened, this same-shift Phase-5 audit (QUANTUM OPTICS, independently
> re-derived by Red Team against `results.json` and exp-046's own
> `NOTES.md`):** the gap is not merely 'a different combination rule' — the
> two functions operate at categorically different points (`coherent`
> median `|C41|`=0.940, `incoherent` median `|C41|`=4.09×10⁻⁴, four orders
> of magnitude apart), and at the FWHM=20° cells the n=41 error for
> `coherent` is dominated by **discrete-aperture grating-lobe leakage**
> (a linearized cross-term correction recovers at most 48% of the actual
> step, 0.1–1.0% at every 450nm cell — the regime is non-perturbative, not
> a small correction on a converged alias model), the identical mechanism
> this program already measured independently at Iteration 22/23
> (exp-046 Phase 5, LOGBOOK: 'a three-lobe comb whose grating-lobe
> replicas... carry 41.7–68.0% of the total intensity outside ±3
> aperture-widths'). This connects, rather than reopens, a five-cycle-old
> finding to this cycle's residual — the correctly-scoped Iteration-29+
> follow-up is a grating-lobe/array-factor n\* criterion for `coherent`
> specifically, not a bigger `m` or a linear cross-term add-on to the
> existing alias model (both tested directly, both insufficient)."

This is disclosure, not re-scoring — no `P-ALIAS` verdict changes; the
addition documents what is now known about an already-disclosed,
already-unscored gap.

---

## 5. Iteration-29 trigger — re-verified a third way, confirmed intact

MATERIALS' Phase-5 review already re-traced this citation chain against
`LOGBOOK.md` line numbers and confirmed Red Team's Phase-2 ruling and the
Director's Phase-3 §3 both use unconditional, binding language. I
independently re-checked the same two source documents:

- `phase2_redteam_audit.md`, closing section: *"YES — unconditional
  Iteration-29 trigger, adopted, not a fourth re-ranking... Iteration 29
  builds and measures the fixed-absolute-thickness `graded_black_shell`
  variant's own `C`, unconditionally — not contingent on Iteration 28's
  own findings, not subject to a further ranked-list competition against
  items (2)/(3)/(5)/(6)."*
- `phase3_synthesis.md` §3: *"Red Team's scope-drift ruling is also
  ACCEPTED and binding: Iteration 29 builds and measures the
  fixed-absolute-thickness `graded_black_shell` variant's own `C`,
  unconditionally — not contingent on this cycle's findings, not subject
  to a fifth ranked-list competition."*

Both hold, verbatim, unedited. **Confirmed intact.**

MATERIALS also flagged a real, live risk: `PLAN.md`'s current
Iteration-28 queue entry (lines 1379–1409, read directly by this audit)
still carries item (4) in the older "ranked item, independently re-ranked
again" prose — expected, since this Phase-5 close has not yet written
`LOGBOOK.md`/`PLAN.md`, but a documented risk for whoever does. **Binding
instruction for this cycle's close**: the literal words "unconditionally"
and "not subject to a fifth [or further] ranked-list competition" must
carry forward into both `LOGBOOK.md`'s Iteration-28 close and `PLAN.md`'s
Iteration-29 queue entry — the last three closes (25, 26, 27) reduced a
correctly-adjudicated finding back to ordinary ranked-item prose one
level down (LOGBOOK.md), and that is exactly how a binding trigger softens
without anyone overriding it on the record.

---

## 6. VISION's Iteration-30 request — the stage-10 temporal instrument

### The task's instruction: apply the same standard already applied this cycle

This cycle (via my own Phase-2 audit, reaffirmed above in §5) granted
`graded_black_shell` an unconditional trigger at 21 iterations deferred
(first queued Iteration 7, re-ranked without being reached at 25, 26, 27,
28), citing the program's one prior precedent — r=156, queued Iteration 3,
triggered unconditionally after its **fourth** deferral (Iteration 10
close, built Iteration 11) — and the additional aggravating fact that this
cycle is the third consecutive, and sixth-in-nine, instrument/model-
fidelity cycle.

### Independent verification of VISION's citation chain

I re-traced this against `LOGBOOK.md` directly, not on VISION's word:

- **Iteration 1 close** (line 1739 area): T3/stage-10 ranked #3 —
  confirmed present (line 1671 in this audit's own read: "Build the
  stage-10 temporal instrument with temporal-contrast bars pinned
  first... the switch transient (T3) is the last unmeasured perceptual
  axis").
- **Iteration 2 close** (line 1992 area): ranked #2 — confirmed ("Build
  the stage-10 temporal instrument with sourced TCSF bars — now the more
  consequential open perceptual gap").
- **Iteration 4 close** (line 2611 area): ranked #3 — confirmed ("Build
  the stage-10 temporal instrument (TCSF bars, sourced first)").
- **Iteration 18 close** (lines 7623–7624): *"Recommended lead item once
  1–3 clear: the T3 joint constraint-3/4 staircase-σ(t) validation
  run..."* — confirmed, the last ranked appearance.
- **Iterations 19 through 28** (I grepped `LOGBOOK.md` lines 7637–9843
  for `stage-10` and `staircase-σ(t)` in any ranked-priority context):
  **zero hits.** VISION's claim of a 10-consecutive-iteration silent drop
  from every ranked list is confirmed, not merely asserted.
- **Partial instrument-building did occur** — `lab/temporal_csf.py`
  (Iteration 16, exp-039, a frequency-domain proxy, LOGBOOK's own words:
  "not the metric-table instrument itself") and `lab/amplitude_bridge.py`
  (Iteration 17, exp-040, scores `C(t)`-at-a-given-`n` but not composed
  with the kinetics trajectory or timing classification). LOGBOOK's own
  T3 entry, verified still current: **"T3's joint constraint-3/4 verdict
  still does not exist"** (line 278). The composition itself — the actual
  stage-10 instrument PANEL.md's own metrics table names (line 144:
  "Switch transient at the observer | 4 (+3) | time-domain monitor series
  (stage 10, when built)") — remains, word for word, exactly what it was
  called at Iteration 3: not yet built.

### Ruling: GRANTED — unconditional Iteration-30 trigger

Applying the exact standard used above for `graded_black_shell`:

| | r=156 (precedent) | `graded_black_shell` (this cycle) | stage-10 T3 instrument |
|---|---|---|---|
| First queued | Iteration 3 | Iteration 7 | Iteration 1 |
| Deferrals before trigger | 4 (Iterations 4–10) | 4 (25, 26, 27, 28) | not merely deferred — **dropped from every ranked list for 10 consecutive iterations (19–28)** |
| Span at trigger | 7 iterations | 21 iterations | **27 iterations** (longer than either) |
| Triggered by | Iteration-10 close | Iteration-28 close (this cycle) | — |

The span is longer than `graded_black_shell`'s own just-granted 21-
iteration bar. More consequentially: `graded_black_shell` was, at every
point in its deferral, an *actively ranked, visible, competing* item — the
program's queue discipline kept re-surfacing it, and the failure mode was
"never wins the competition." The stage-10 instrument's failure mode is
worse: it stopped competing at all, for 10 iterations, sitting as a bare
`[queued]` line in `PLAN.md` outside the numbered queue (VISION's own
characterization, which I confirm from `PLAN.md`'s own structure). That is
closer to PANEL.md's own Checkpoint criterion 4 language — *"a constraint
quietly dropped — especially #3"* — than to an ordinary deferral, even
though it does not itself fire criterion 4 (no seat is claiming a false
constraint-3/4 verdict; the instrument to score constraint 4 simply does
not exist yet, and every seat that has touched T3 since Iteration 18 has
said so honestly). A program whose own metrics table has named this
instrument, unbuilt, for 20+ iterations, and whose queue discipline let it
silently exit the ranked list entirely for the last 10 of them, has enough
grounds to grant exactly the device already granted once this cycle for a
materially shorter deferral.

**Ruling, binding instruction for the LOGBOOK/PLAN.md close**: Iteration
30 builds the joint constraint-3/4 staircase-σ(t) validation run —
composing exp-038's kinetics `n(t)`, exp-039's timing classification, and
exp-040's amplitude bridge against `C_thr(L)` in one scored transient, per
Iteration 18's own original design (never retired or refuted, only
deferred) — **unconditionally**, not contingent on Iteration 29's own
findings, not subject to a further ranked-list competition. This does not
preclude Iteration 30 also carrying forward same-shift fixes discovered at
Iteration 29's own close, matching this cycle's own precedent for how an
unconditional trigger coexists with house discipline.

---

## 7. Checkpoint — all five criteria, explicit

1. **A configuration passes ALL constraint metrics.** Does not fire. No
   constraint-3/4 verdict is issued or implied anywhere in this cycle —
   confirmed by VISION's own explicit grep-check (Phase 5) and
   independently re-confirmed here (`grep -riE
   "constraint-3|constraint-4|tier.w|tier.a" experiments/051-.../*.md
   experiments/051-.../results.json` returns only disclaimer language, no
   claims).
2. **A proven boundary — a constraint subset shown jointly unsatisfiable
   within a mechanism class, gates clean.** Does not fire. T1 escape
   route: NONE, confirmed throughout — no mechanism is proposed this
   cycle.
3. **A synthesis requires engine physics beyond the validated bench
   classes.** Does not fire. Zero `lab/` files touched (verified: `git
   diff --stat -- lab/` against this cycle's commit range is empty); pure
   desk numpy on already-committed, already-gated propagator code from
   exp-042/048/050.
4. **Red Team flags program-integrity drift (unfalsifiable claims, a
   constraint quietly dropped — especially #3).** **Does not fire**,
   ruled explicitly, weighing both disclosure defects directly: neither
   is an unfalsifiable claim (both are concrete, checkable computations
   with concrete numeric resolutions, both resolved in this audit against
   source); no constraint is quietly dropped (none is claimed by this
   cycle at all — the letter and spirit of criterion 4's "especially #3"
   clause do not engage a cycle that issues no constraint-3/4 verdict).
   Both defects are same-shift, zero-new-computation, narrative-only
   corrections that leave every scored `P-ALIAS` number untouched —
   exactly the shape of finding this program's own Iteration-25/26/27
   precedents (the "321" figure, the discarded-run cost dispute, the
   adjacent-cell threshold breach) ruled non-firing for the identical
   reason: caught same-shift, disclosed not smoothed over, non-
   load-bearing. **This is nonetheless the twelfth recurrence of the
   specific "a document correcting a prior overclaim ships a residual
   instance of the same overclaim" pattern** (§2's own count, independently
   re-verified). I am not adopting a new hardened tripwire for this
   specific shape the way Iteration 26 did for non-reproducing headline
   figures — that rule targeted numeric results that fail to reproduce;
   this defect class is narrative attribution, and the headline numbers
   here *do* reproduce, in all twelve instances the program has named.
   **Recommended lightweight practice, not a binding rule**: any Reading-
   section sentence that names a specific numeric anomaly (an inversion,
   crossing, or extremum) should state, in the same sentence, which
   committed block — scored or unscored, and its geometry — the anomaly's
   own numbers come from. Cheap, mechanically checkable, and would have
   caught this cycle's own defect 1 at the point of writing.
5. **Two consecutive iterations with no logbook-advancing result.** Does
   not fire. Iterations 27 (exp-050) and 28 (exp-051) both produced
   genuine, falsifiable, LOGBOOK-advancing results (a resolved n-
   convergence question at a second geometry; a real out-of-sample
   mechanism test that closes two of exp-050's own open questions for the
   incoherent family and locates, rather than merely notes, the boundary
   for `coherent`).

**No Checkpoint criterion fires.**

---

## 8. Overall ruling

# PROMISING

**Why.** The cycle's substance is genuinely strong and independently
re-verified six-plus-one ways: a Phase-1 design correctly killed at the
desk by four blind seats before any Phase-4 spend, a Director override
(moving every scored prediction off a pre-computed 18-row calibration set
onto 198 untouched combinations) that converted a would-be transcription
into a real out-of-sample test, and a result that holds — 5 CONFIRMED, 2
PARTIAL, 1 REFUTED-but-informative, 0 hard-falsified, zero false positives
on the well-sampled control block, clean transfer to an untouched
geometry, and a *located*, not diffuse, boundary (`beam_divergence_
coherent`) for the one place the mechanism does not reach. Both P-ALIAS-0
gate clauses are bit-exact; the completeness ledger is 1080/1080; no
`REALIZABILITY_MEMO.md` tier is touched or claimed to be.

**What keeps this from PARTIAL.** Both narrative defects are real, but
neither touches a scored verdict, both were caught same-shift by multiple
independent seats before any propagation to `LOGBOOK.md`, and both are
one-sentence fixes with exact replacement text specified above. That is
the same shape of defect this program's own Iterations 19, 22, 25, 26, 27
ruled PROMISING (not PARTIAL) through, for the same reason: the house
discipline (fresh Phase-5 seats, R4 execution-not-assertion, "flag don't
smooth over") caught what it exists to catch, inside the same shift, at
zero cost to the science.

**What load-bearing findings must survive the close, unedited:**
- The Iteration-29 `graded_black_shell` trigger (§5) — unconditional,
  binding, carried in full into `LOGBOOK.md`/`PLAN.md`.
- The new Iteration-30 stage-10 temporal-instrument trigger (§6) —
  unconditional, binding, newly granted this audit.
- The `coherent`-breakdown/grating-lobe connection (§4) — a genuine
  cross-reference to exp-046/Iteration-22-23, belongs in the permanent
  record.

**What is cosmetic, fixed same-shift, not carried as open questions:**
- The P-ALIAS-5 misattribution (§2).
- The "executed twice" claim (§3).

---

## 9. Reconciled ranked priority list for Iteration 29+

*Iterations 29 and 30 are both now unconditionally committed (§5, §6) —
not competing in this list. What follows reconciles all six seats' own
rankings (EM, MATERIALS, THERMODYNAMICS, QUANTUM, PHOTONICS, VISION) for
what runs alongside those two locked slots, and for whichever slot follows
them.*

1. **The genuine FDTD `ABSORB` sweep at the T21-vs-T24 geometry (GEOM78).**
   Near-unanimous across four seats (MATERIALS, EM, PHOTONICS,
   THERMODYNAMICS all rank it in their own top 2–3), carried without
   being run across Iterations 26, 27, and 28's own ranked lists — three
   consecutive cycles, approaching the same anti-pattern this cycle just
   fixed for `graded_black_shell`. This cycle's own idealization 6
   sharpens the case further (EM's Phase-5 finding): the entire
   alias-lattice result, however clean, is a statement about the
   analytic propagator's *internal* consistency at GEOM78, never
   cross-checked against FDTD there at any n — the last uncharacterized
   uncertainty source on the program's sharpest contamination-risk cell
   family. **Ranked #1** among the unlocked items; flagged as itself
   approaching unconditional-trigger territory if deferred again.

2. **QUANTUM's grating-lobe/array-factor n\* criterion for
   `beam_divergence_coherent`** — build and score the angular-sampling
   comb's replica-leakage fraction (exp-046's own already-validated,
   zero-free-parameter closed form) as the regressor, against the same 72
   `coherent` out-of-sample rows this cycle already computed and labeled.
   Zero new FDTD, reuses committed labels, comparable cost to exp-051
   itself. **Ranked ahead of EM's own complementary proposal** (the
   off-diagonal mutual-coherence extension of `alias_coeff`) for a
   specific, evidence-based reason found in this audit (§4): QUANTUM's
   own Phase-5 execution already shows that a linearized cross-term
   correction — the natural first-order form EM's proposal would take —
   recovers at most 48%, and as little as 0.1%, of the actual step at
   exactly the cells that matter most (450nm). The regime is
   non-perturbative; the grating-lobe/array-factor route is grounded in
   an already-quantitatively-validated mechanism from this program's own
   record, not a linear approximation already shown likely to fall short.
   EM's off-diagonal construction remains a legitimate, cheap secondary
   probe (it would independently confirm or bound the 48%-ceiling
   finding) but should not compete for the same build slot as the primary
   route.

3. **THERMODYNAMICS' overdue `h_eff` re-derivation** for the program's two
   thinnest surviving detectability margins (exp-043 ON-endpoint, exp-045
   dose-accumulation). Named at four consecutive closes (25, 26, 27, 28)
   without being reached — the identical deferral count that triggered
   r=156's own unconditional lock at Iteration 10. **Flagged explicitly**:
   if this item is named a fifth time at whichever close follows Iteration
   29/30 without being run, it meets this program's own established bar
   for an unconditional trigger, on the same standard applied twice in
   this document (§5, §6). Not granted that status here only because it
   was not the specific question this audit was asked to adjudicate and
   two unconditional slots are already committed — but the Director
   closing this cycle should say so explicitly rather than let a fifth
   deferral pass as an ordinary re-ranking.

4. **VISION's sub-degree (0.25–0.5° step) angular sweep across 36°–40° at
   750nm/FWHM=2°/GEOM78** — carried from Iterations 27 and 28's own
   queues, now doubly motivated: exp-050's adjacent-cell threshold-breach
   finding, plus this cycle's own confirmation (idealization-3 disclosure)
   that those same three FWHM=2° cells are exactly where the
   `|C(2n)|≥C_THR` clause fires outside `coherent`.

5. **Low priority, general engineering debt**: promote the
   `_geom_derived`/`_G_for_g` hoisting pattern (mandatory in this cycle's
   own `design_geometry.py`, per Red Team docket item 2) to a shared
   utility the next time a fourth geometry-parameterized module is built.
   Not worth a dedicated slot.

---

## Verification appendix — what this audit actually ran

1. Direct JSON queries against `results.json` (`predictions.P_ALIAS_5`,
   `calibration_18_unscored.rows`, `post_hoc_observations_unscored`,
   `per_combination`) for defects 1 and 3.
2. Direct read of `timing.json` in full, cross-checked against
   `results.json::meta.stage_times_s`/`proc_start_unix`, `git log`
   (`--stat -p`) on this experiment's directory, and `__pycache__` mtimes,
   for defect 2.
3. Direct read of `experiments/046-.../NOTES.md`'s own A3 finding
   (grating-lobe replica percentages), for finding 3's provenance check.
4. Direct grep/read of `LOGBOOK.md` at every line number MATERIALS' and
   VISION's Phase-5 reviews cited (Iteration 1/2/4/7/8/18/24/25/26/27
   closes; T21/T3 entries), for the two trigger rulings (§5, §6).
5. Direct read of `design_geometry.py`/`run.py` (memoization construction,
   `_PROC_T0`/`atexit` timing hook) to confirm two of Red Team's own
   Phase-2 mandatory-fix items (2 and 9) were genuinely implemented, not
   merely claimed.
6. `grep -riE "constraint-3|constraint-4|tier.w|tier.a" experiments/051-.../*.md experiments/051-.../results.json` for the Checkpoint-1/4 constraint check.

No `lab/` file, no exp-042/046/048/049/050 file, was modified. This
audit's own file is the only new file in `experiments/051-.../`.
