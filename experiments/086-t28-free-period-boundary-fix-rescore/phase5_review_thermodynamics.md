# PHASE 5 — REVIEW (THERMODYNAMICS, blind) · Panel Iteration 63 · exp-086

*Fresh context. Read PANEL.md in full; LOGBOOK.md lines 1–380 (RULED OUT
R1–R11) and lines 426–4117 (LIVE THREADS, including the full T28 sub-thread
Iterations 46–62 and the Iteration-61 CHECKPOINT entry) in full; then the
complete exp-086 record: `phase1_proposal.md`, all five Phase-2 critiques,
`phase2_redteam_audit.md`, `phase3_synthesis.md`, `phase4_rescore.py` +
`phase4_rescore_results.json`, `phase4_null_calibration_rerun.py` +
`_results.json`, `phase4_null_calibration_controlled_comparison.py` +
`_results.json`, `phase4_prior_citation_audit.py` + `_results.json`,
`NOTES.md`. On T28 desk cycles this seat also serves as an independent
numerical-reproduction/timing check. I raised the missing
energy-interception exemption sentence at this cycle's own Phase 2.*

## 1. The exemption sentence — CONFIRMED DELIVERED

Grepped `NOTES.md` directly: the sentence is present, twice, matching the
Phase-3-frozen language verbatim.

- Idealizations (lines 67–70): *"The joint EM/THERMO energy-interception
  cross-check is structurally exempt this cycle — no article-loaded FDTD
  scene exists anywhere in its scope (matching exp-084/085's own
  established exemption language)."*
- Next (lines 191–194): explicitly names this as **"now FOUR consecutive
  cycles deferred/exempt (083/084/085/086)"** and flags it, unprompted, as
  "approaching the same escalation shape R6–R10 named for other
  repeatedly-deferred items."

Mandatory fix 3 from `phase2_redteam_audit.md` (which confirmed my own
Phase-2 attack exactly, by independent grep) is fully discharged. This
closes the gap that fired Checkpoint criterion 4 one cycle ago (Iteration
61/exp-084) on the identical silent-absence shape.

## 2. Independent timing reproduction — ALL THREE FIGURES CONFIRMED

Read the committed JSON's own `elapsed_s` fields directly (not NOTES.md's
prose, which — noted below — never actually restates these numbers):

| Script | Cited (task) | JSON `elapsed_s` (verified) | Match |
|---|---|---|---|
| `phase4_rescore.py` | ~64.7s | `64.7050404548645` | exact |
| `phase4_null_calibration_rerun.py` | ~472.5s | `472.53617000579834` | exact |
| `phase4_null_calibration_controlled_comparison.py` | ~70.4s | `70.3767626285553` | exact |

**Finding, not a defect**: `NOTES.md` itself contains no prose timing
citations at all — no "64.7s"/"472.5s"/"70.4s" appears anywhere in the
document. There is therefore nothing in NOTES.md's own prose to contradict
these figures; the timing claims live only in the committed JSON, which I
verified matches the task's citations exactly, digit for digit.

## 3. Controlled-comparison arithmetic — CONFIRMED, stronger than claimed

Read `phase4_null_calibration_controlled_comparison_results.json::diff`
directly:

```
"diff": {
  "p_r2_ge_070_diff": 0.0,
  "max_r2_over_trials_diff": 0.0,
  "mean_r2_over_trials_diff": 0.0002014956968885706
}
```

Independently re-parsed both operands and compared their IEEE-754 hex
representations rather than trusting the printed diff: `old_buggy.
max_r2_over_trials` and `corrected.max_r2_over_trials` are **bit-identical**
(`0x1.09334248d01cap-1` both) — not merely equal "to 4 decimal places" as
NOTES.md's own conclusion field states, but exactly equal at full float64
precision. `p_r2_ge_070_diff=0.0` likewise confirmed exact. Only
`mean_r2_over_trials` shows a small, correctly-disclosed non-zero diff
(2.0×10⁻⁴), consistent with NOTES.md's own "not the headline figure"
framing. `boundary_pin_rate=201/3000=0.067` reproduces Red Team's cited
6.70% figure exactly. **No arithmetic defect found; the claim is
accurate and, if anything, understated.**

## 4. Independent spot-checks beyond the three assigned items

Since the assigned checks all cleared cleanly, I extended verification to
the rest of the frozen-prediction chain, reading JSON directly rather than
NOTES.md's restatement:

- `method_c_rescore`: `frac_recovered=21/37=0.5676`, boundary set
  `θc∈{45,59,61,63,71,73}` (6/37), `classification_a="NOT STABLY
  PERIODIC"` — all reproduce Prediction 1–3 exactly.
- `spearman_stride_phases`: phase 5°→`ρ=0.8571,p=0.0238`; phase
  7°→`ρ=0.4286,p=0.354`; phase 9°→`ρ=0.5357,p=0.236` — reproduces
  Prediction 4 and QUANTUM's/Red Team's independently-confirmed figures
  exactly.
- `ss_tot_full`/`ptp` are in fact persisted per sub-window (mandatory fix
  5, PHOTONICS) — confirmed present in `sub_results[0]`.
- Re-ran the prior-citation audit's own file-discovery glob independently
  (`experiments/07[7-9]-*/*.json` + `experiments/08[0-5]-*/*.json`): 18
  files, matching `files_scanned=18` exactly. Two all-stage-boundary hits
  (exp-078, exp-079), matching Prediction 5.

## 5. Two minor findings (non-blocking, disclosed-adjacent, worth naming)

**(a) NOTES.md's own cross-reference is broken.** The Result section says
the N=3000-vs-60,001 scope reduction is "(bounded, disclosed scope
reduction from the mandated 60,001 calls — **see Idealizations**)" —
but the Idealizations section, read in full, never states this reduction
anywhere; it is disclosed only in the Result section itself and in Next
item (1). A minor, purely cosmetic self-citation-precision slip (the kind
R4 exists to catch, though far below load-bearing), not something that
changes any number.

**(b) The prior-citation audit's stated scope doesn't match its executed
scope, though the gap is independently justified.** `NOTES.md`'s Setup
(line 51, "committed JSON in experiments 069–085") and the original
`phase1_proposal.md` table ("21 files identified" spanning 069–085) both
describe a wider span than what `phase4_prior_citation_audit.py` actually
globs (`07[7-9]` + `08[0-5]` → 18 files, experiments 077–085 only,
independently re-run and confirmed by me in §4). The code's own comment
asserts 069–076 are "out of scope by construction" because the function
postdates exp-076 — a claim THERMODYNAMICS' own Phase-2 critique (mine)
already independently grep-confirmed true (`grep -rl
"free_period_with_widening" experiments/069-076/` → zero files) — so the
narrower actual scope is substantively fine. But this Phase-4 script does
not itself re-verify that exclusion; it inherits an assumption from a
different phase's grep, and NOTES.md's own Setup prose never states the
narrowing or points to the justification. A precision gap, not a
corruption risk.

Neither (a) nor (b) touches any frozen prediction, the Combined Verdict, or
any cited T28 number.

## 6. The energy-interception deferral pattern — flagged explicitly, not yet an automatic firing

NOTES.md's own Next section already names this "FOUR consecutive cycles
deferred/exempt (083/084/085/086)" and flags it as approaching the R6–R10
shape — correctly, and I confirm the undercount risk is real, but the
picture is more specific than "four strikes":

- **083** was a genuinely scene-bearing (article-loaded, 125-call FDTD)
  cycle that silently skipped the check — a real discretionary miss,
  one of the two that built the original tripwire.
- **084** was the cycle the tripwire fired on (Checkpoint criterion 4,
  13th firing, Iteration 61) — Red Team's own audit at the time drew the
  "scope mismatch, not neglect" distinction for zero-FDTD desk cycles,
  but ruled the literal pre-committed condition fired anyway because no
  exemption sentence was written down.
- **085 and 086** are both zero-FDTD desk cycles that *did* write the
  exemption sentence, discharging the documentation remedy Iteration 61
  actually asked for.

So: **no written rule currently fires on exp-086 alone** — the specific
remedy the last firing required (state the exemption) was delivered, twice
running now. But the deeper institutional fact is real and, in my seat's
own charter terms, is exactly the pattern this program's escalating-rule
lineage exists to name before it calcifies: Iteration 62's own §7 ranking
called the full energy-interception check **"highest institutional
priority for the first Iteration-62 cycle with a real article-loaded
scene"** — and neither Iteration 62 (exp-085) nor Iteration 63 (exp-086,
this cycle) *was* such a cycle. The check has now gone unexecuted for
**seven cycles** since it was first named (Iteration 59), and the
T28 board's own queued items ahead of/alongside it (PHOTONICS'
domain-truncation test, EM's kernel rebuild, the grazing-incidence
model-validity question) are *also* zero-FDTD — meaning the sub-thread
could easily produce two, three, or more further scene-less cycles before
a scene-bearing one naturally arises, at which point "next scene-bearing
cycle" as a scheduling mechanism has quietly become no mechanism at all.
This is the same shape R11 named for `free_period_with_widening` itself:
a condition ("when does the check finally run") that keeps deferring to a
category of event the program isn't actually scheduling to produce.

**Recommendation, not a firing**: the next T28 lead should not wait for a
scene-bearing cycle to arise organically. Either (i) make a minimal,
purpose-built article-loaded scene (even a cheap, narrowly-scoped one) the
explicit Tier-0 item specifically to discharge this check, rather than
folding it as item N of a longer list that a zero-FDTD cycle can
legitimately skip past every time, or (ii) if the check is judged genuinely
low-value until a substantive mechanism candidate exists to test energy
disposition against, say so explicitly and retire the "next scene-bearing
cycle" framing rather than let it keep re-accumulating silently. I would
treat a fifth consecutive deferral without one of these two actions as
the point this pattern should be named a standing rule in its own right,
matching R6–R11's own format.

## 7. Verdict: **PARTIAL**

Matches this sub-thread's own unbroken pattern since exp-069. The repair
itself is genuine, independently reproducible science, not mere hygiene:
R11's fix is now live at the source in all three affected functions,
verified interior-optimum-path-unchanged, and the automated pipeline
itself (not a hand audit) now confirms exp-085's own hand-computed
`frac_recovered` collapse (1.000→0.568, even lower than the hand-audit's
0.595, once the correctly-excluded `θc=45°` coincidence is folded in) —
cleanly REFUTING the filed "STRONG COHERENT CHIRP" classification a second,
independent way. The null-calibration side-question (does the same defect
threaten exp-077's own settled REFUTE) came back genuinely reassuring,
mechanistically explained, and — per my own bit-level check — even more
solid than claimed. T28's own founding mechanism question (`P_edge_A`'s
physical origin) is untouched by this cycle, as intended (Checkpoint
criterion 2 correctly ruled N/A, matching every T28 desk cycle since
exp-069). Checkpoint criterion 4 does not fire this cycle on any matter I
independently checked; the one real forward risk (§6) is named, not
resolved, and belongs on the next Director's board rather than in this
cycle's own ledger.

## 8. Ranked next steps for the T28 sub-thread (my seat's own picks; nothing here re-proposes R1–R11)

1. **Force the joint EM/THERMO energy-interception cross-check as an
   explicit Tier-0 item on the very next T28 cycle, scene-bearing or not**
   (§6, above) — my own charter's most directly engaged open item, now
   seven cycles named-and-unexecuted, and the one candidate for a genuine
   new standing rule if it slips an eighth time.
2. **PHOTONICS' grazing-incidence model-validity question**
   (`edge_diffraction_c_empty_corrected`'s own physical validity at the
   ~5,444×–6,631× `ptp` sub-windows) — zero-FDTD, cheap, and load-bearing:
   if the model itself leaves its valid near-field regime at grazing
   incidence, the "recovered" classification scheme this cycle just
   rebuilt is scoring some windows against a formula that may not apply
   there at all, independent of the boundary-pinning fix.
3. **The full-scale (60,001-call) `null_calibration_appendix` re-run**,
   already queued (NOTES.md Next item 1) — genuinely de-risked by this
   cycle's matched-N=3000 finding, but still the literal completion of
   mandatory fix 2, and cheap relative to its own 472.5s-per-3000-trials
   cost (roughly ~2.6 hours at N=60,001, a one-shot background run, not a
   blocking cost).
4. **The x-wall wavelength-generality leg** — now the single oldest
   deferred item on the whole T28 board (11 consecutive cycles, 076–086
   per NOTES.md's own count) — overdue enough that it should be weighed
   against item 1 for actual next-cycle scheduling, not merely re-logged
   again.
5. PHOTONICS' domain-truncation test for leg (b)'s Anchor 2 / EM's
   matrix-valued RS/Kirchhoff kernel rebuild — legitimate zero-FDTD next
   step, ranked below 1–4 because it advances a narrower, already-
   INCONCLUSIVE side-question rather than either the founding mechanism
   or a now-overdue institutional commitment.
