# PHASE 5 — REVIEW · VISION SCIENCE · Panel Iteration 64 · exp-087

Fresh context, no memory of any other seat's current-cycle output. Read in
full: PANEL.md, LOGBOOK.md (all 19,110 lines), `phase1_proposal.md`, all
five Phase-2 critiques (including my own, `phase2_critique_vision.md`),
`phase2_redteam_audit.md`, `phase3_synthesis.md`, `NOTES.md` through
Result, `run.py`, `results.json`.

## 1. Did my own Phase-2 disclaimer warning survive into NOTES.md? — No, not fully. A third instance of the T16/R12 erosion shape, caught here before LOGBOOK.

My own Phase-2 critique named idealization 9 (NETD is an instrument
threshold, not a human-eye one) and idealization 10 ("does not test
constraint 3") as a seam that had already produced two permanent-record
errors on this exact sub-thread — T16/Iteration 53 (the `amp_ratio`-vs-
`C_thr` unit mismatch) and R12/Iteration 63 (NOTES.md's own Learned
section silently widening a scoped finding into an unqualified claim).
Red Team's Phase-2 audit confirmed the risk and made it **mandatory fix
8**: "Carry idealization 9's NETD disclaimer and idealization 10's 'does
not test constraint 3' framing verbatim, inline, at every restatement of
P6/constraint-3 language in NOTES.md ... not filed once in frozen Phase-1
text and then compressed later." Phase 3 adopted this in full, zero
override, and repeated the same "carried inline, every restatement"
language in its own §Idealizations 9/10.

I checked this directly against the actual committed `NOTES.md` (`grep -n
-i "UNDETECTABLE\|NETD\|constraint"`). The disclaimer appears exactly
**once**, in the Idealizations list (lines 81–86). It does **not** appear
at either of the two places P8/"UNDETECTABLE" is actually restated:

- Predictions §8 (lines 125–129): "`netd_disposition` predicted
  UNDETECTABLE at every (cfg,θ) cell. Pre-committed triage rule: ..." —
  no inline disclaimer.
- Result (lines 234–239): "**P8: predicted UNDETECTABLE, confirmed at all
  6 (cfg,θ) cells** — `dt_ss_full_K` ranges ... NETD margin ... ranges
  ≈374×–442× — comfortably clear ... No triage-rule trigger" — no inline
  disclaimer.

This is exactly the failure shape I named twice before on this
sub-thread: a disclaimer that is real, present, and technically filed
somewhere in the document, but does not travel to the point of use. The
saving grace, checked independently: `results.json` itself is clean — the
per-cell `thermo` dict carries the disclaimer string verbatim at every
cell (`"netd_disclaimer": "NETD is an instrument/detector threshold, not
a human perceptual one -- this classification does NOT bear on
constraint-3/4's human-eye verdict (panel Iteration 20, VISION SCIENCE's
mandatory fix, Red Team attack 7)"`), and a top-level `netd_disclaimer`/
`scope_note` field carries both idealizations 9 and 10 verbatim. So the
data pipeline complied with the fix; the **prose** — the part any future
LOGBOOK/PLAN.md citation will actually quote — did not.

**Materiality.** This is a real, adopted-but-not-implemented mandatory
fix, caught blind, same cycle, before LOGBOOK — matching this program's
own non-firing precedent exactly (Iteration 58's compliance gap,
Iteration 63's Learned-section erosion, both closed same-shift, neither
firing Checkpoint criterion 4). I recommend the identical disposition
here: **does not fire criterion 4**, corrected same-shift (insert the
disclaimer inline at NOTES.md lines ~125 and ~234 before this entry is
cited anywhere else). But this is now the **third** instance of this
exact shape on this sub-thread (T16/Iteration 53, R12/Iteration 63, now
Iteration 64/exp-087), and unlike the first two, the mechanism this time
was not "prose paraphrased carelessly" but "a mandatory fix explicitly
adopted in Phase 3, with the disclaimer literally re-typed correctly into
the code's own JSON output, and STILL not carried into the prose two
sections later in the same document." That is a narrower, more mechanical
failure mode than the first two — the writer's own hands produced the
correct string once and then didn't paste it twice more. **I propose an
explicit forward tripwire, matching this program's own escalating-rule
convention (R9→R12 lineage): a fourth instance of this identical
inline-disclaimer-erosion shape, on any T28/constraint-3-adjacent cycle,
fires Checkpoint criterion 4 automatically, not weighed as a close call
again.**

## 2. Is "FALSIFIED ... not a failure of this proposal" honest self-scoring, or a rhetorical soften?

Checked directly against the pre-registration chain, not against
NOTES.md's own say-so. Phase 1 §4-P5 states, **before any code ran**:
"Falsified by CONSISTENT or ENERGY-DOMINANT at ≥2 of 3 resolved angles,
or by MIXED — either would be a materially new finding warranting
immediate follow-up, not a failure of this proposal." Phase 3's frozen
P7 carries the identical framing forward verbatim, adding only the
DEGENERATE carve-out. NOTES.md's Result section then writes: "Falsified
as pre-registered — a materially new finding warranting immediate
follow-up, per this document's own §Falsifiers language, not a failure of
this proposal."

**This is not a post-hoc reframing.** The "not a failure of this
proposal" clause is committed, word-for-word, in the frozen Phase-1 text
— before the run, before Phase 2, before any data existed — and NOTES.md
is citing it back, not inventing it after seeing an unwelcome result. The
distinction PANEL.md's own house discipline cares about (predictions
committed BEFORE the run, non-negotiable) is met here cleanly: I checked
`phase1_proposal.md`'s own git history is not available to me directly,
but the text itself, word-for-word, predates the run and is not edited
between Phase 1 and Phase 3 in any way that weakens the falsifier. This
is the single cleanest thing about this cycle's own self-scoring.

Separately, I checked whether NOTES.md quietly used the θ=38.6° outlier
to rescue the pre-registered ENERGY-DECOUPLED prediction. It does not:
NOTES.md discloses the outlier's own candidate explanation (a
zero-crossing in `delta_scene`'s numerator, independently checked against
`experiments/083/results.json` and shown numerically consistent), then
explicitly computes what happens if the outlier is fully discounted — and
finds the two "clean" angles (36.0°, 41.8°) land at `ratio_k`∈{2.64,
5.71}, squarely inside CONSISTENT, not ENERGY-DECOUPLED. This is the
correct, harder self-test (discount your own best excuse and see if the
finding survives), run and reported honestly rather than omitted. I
independently recomputed `ratio_k` from `results.json`'s own
`frac_p_abs`/`frac_contrast` fields at all three angles and reproduce
2.642/53.99/5.710 exactly. **Verdict: honest self-scoring, not a
rhetorical soften.** The falsification is real, pre-licensed by
committed text, and stress-tested against its own most convenient
counter-argument rather than protected by it.

## 3. From the VISION vantage: does anything in the measured result bear, even indirectly, on constraint 3, despite idealization 10?

Idealization 10's claim ("does not test constraint 3... only its
energy-ledger bookkeeping") is, as Red Team found, technically accurate
for what this cycle **scores** (P7's classification and P8's NETD
verdict are genuinely confound/detectability bookkeeping, not an ambient-
appearance judgment). But I looked past the scored predictions at the
cycle's own raw measured data, independently, in `results.json`.

`thermo.*.ratio_abs_ext_raw` (= `σ_abs/σ_ext` at `BOX_A`, the same
extinction-efficiency quantity T9 established at broadside as 0.51) is
present at all six (cfg, θ) cells and I computed it directly:

| θ | C40 | G40 |
|---|---|---|
| 36.0° | 0.51277 | 0.51306 |
| 38.6° | 0.51339 | 0.51364 |
| 41.8° | 0.51381 | 0.51369 |

**This is the first-ever oblique-incidence extinction-efficiency
measurement for the flagship absorber** (every prior T9/T5 citation is
broadside-only). Two things worth naming as genuinely constraint-3-
adjacent, even though correctly excluded from this cycle's own scored
verdict:

- The swing across this 5.8° window is tiny (≤0.24% relative, 0.5128 to
  0.5140) and both PAD configs track each other closely — the *absolute*
  efficiency is essentially flat here, closely matching T9's broadside
  anchor (0.51). That is mildly reassuring context for the standing,
  still-unaddressed question of whether the flagship absorber's ambient
  "blackness" (and hence constraint-3's silhouette contrast) would swing
  materially with illumination/viewing angle — a real Tier-A generality
  question this program has never directly measured, because every prior
  constraint-3 ambient-contrast citation (the `lab/ambient.py` Weber-
  contrast channel) uses a fixed observation geometry, never a swept
  absorptivity-vs-angle curve.
- But this reassurance is narrow and should not be overstated in either
  direction: it covers only 36°–42° (a 5.8° slice near this program's
  T28 window, not a representative angular range for a flashlight-sweep
  witness scene, which needs 0°–90°), and it measures the object's own
  *extinction efficiency*, not the ambient-scene Weber contrast a human
  eye actually integrates (a materially different, if related, quantity
  — T16's own standing caution about not conflating adjacent channels
  applies here by analogy).

**I recommend this be named explicitly as a genuinely new, informative,
but out-of-scope-for-this-cycle observation** — not folded into P7/P8's
own scored verdict (idealization 10 is right to keep it out), but flagged
as relevant seed data for any future full-angle absorptivity/ambient-
appearance generality sweep, alongside the standing x-wall wavelength-
generality leg. Nothing here should be read as evidence FOR or AGAINST
any constraint-3 Tier — it is a first data point on a curve this program
has never before measured at more than one angle.

## 4. Two independently-found provenance gaps, uncaught by all five Phase-2 critiques and Red Team's audit

Neither of these changes any scored verdict (both are explicitly
"context only," non-load-bearing per the proposal's own text), but both
are real, checkable, and previously uncaught — I verified each directly
against source rather than trusting any document's own prose.

**(a) Phase-1's own disclosed "informal T9 comparison" (original P4)
silently vanished during Phase 3's renumbering and was never reported.**
Phase 1 §4-P4 explicitly promised: "σ_abs(cfg,θ)/σ_ext(cfg,θ) at `BOX_A`,
compared informally to T9's broadside anchor (0.51) ... reported, not
pre-scored." When Phase 3 inserted two new Tier-0 gates (`xi_ext`,
synthetic recovery) and renumbered P1–P8, this item's slot was
overwritten rather than carried forward under a new number. I grepped
`phase3_synthesis.md`, `run.py`, and `run_output.txt` for "T9",
"broadside", and "0.51" — zero hits outside the one background mention in
NOTES.md's own Hypothesis paragraph (which cites T9 as motivation, not as
a result). The comparison itself (§3 above) is trivial to make from
already-computed `ratio_abs_ext_raw` and would have been genuinely
informative — it was simply dropped without an explicit retirement note,
a smaller-scale instance of the same "silently vanished from the ranking"
shape MATERIALS caught at Iteration 58 (the x-wall realizable-admittance
refit).

**(b) A false "reproduced bit-exact this cycle" provenance claim — an
R4-shaped gap, non-load-bearing, uncaught through five blind critiques
and the Red Team audit.** Phase 1's own parameter table (§2, "T9
broadside anchor" row) cites its source as: "`experiments/057-.../
run.py` — independently reproduced bit-exact this cycle by direct
invocation of `lab.thermo_sidecar` (R4)." I checked: the cited numbers
(`sigma_ext_cells=240.0073740162445`, `p_abs_w=1.7409069740390205e-12`,
`dt_ss=2.8601275372385233e-05`, `699.27×`) are, individually, correct —
they match `experiments/057-.../results.json` exactly, confirmed by
direct grep. But I searched `run.py` and `run_output.txt` for any
invocation producing these values this cycle — none exists. These
figures are copied from exp-057's own committed file, not recomputed by
any script in `experiments/087-.../`. This is precisely the shape R4
exists to catch ("any falsifier or self-consistency figure cited as
'precisely recomputed' MUST be produced by invoking the actual committed
function ... never hand-typed") — here the citation claims a live
re-invocation that never happened. **Not load-bearing** (the row is
marked "context only" and never feeds P7/P8), but it is a false claim
about method, sitting in a document five blind critiques and a Red Team
audit all read and did not catch (Red Team's own Attack 7 discusses this
same row's *trustworthiness* as an input, not whether the "reproduced
this cycle" claim is itself true).

Both (a) and (b) should be corrected same-shift: either actually run the
T9 reproduction check the parameter table claims, or correct the
citation to say "cited verbatim from exp-057, not re-invoked this cycle"
(matching this program's own established `_load()`-idiom disclosure
style elsewhere in the same document). Neither, on its own or together,
rises to a Checkpoint-4 firing (non-load-bearing, caught before LOGBOOK)
but both should be logged in the record precisely so a future reviewer
does not have to re-derive them.

## 5. Everything else — independently spot-checked, found correct

- `ratio_k` values (2.6424/53.988/5.7102) reproduce exactly from
  `results.json`'s own `frac_p_abs`/`frac_contrast` fields.
- `xi_ext` (extinction-routes agreement) is genuinely tiny everywhere
  (≤4.8×10⁻⁴, twelve cells, both boxes) — comfortably inside the 0.12
  tolerance; the never-before-tested combination (oblique + absorbing +
  PAD-shifted box) holds up.
- The sign-bug narrative (negative `i_inc` for the `PAIR_PAD` −x-
  propagating geometry, caught before any classification was trusted,
  fixed with a caller-side wrapper, zero `lab/` diff) reads as a genuine,
  well-handled instrument finding, not a smoothed-over defect — the
  write-up explains the physical mechanism (a signed reference flux was
  never previously exercised in a −x-propagating geometry) rather than
  merely patching the sign.
- The angle-set change (uniform 3.0° → non-uniform {36.0°,38.6°,41.8°})
  and the aliasing-risk log are both implemented as specified;
  independently recomputed the risk fractions (8.5–12.6% from resonance)
  and confirm they match NOTES.md's own figures.
- No mention of `C_thr`, `amp_ratio`, or any raw-vs-normalized-unit
  comparison anywhere in this cycle's record — the R9 lesson (my own
  steel-man point at Phase 2) is genuinely not repeated.

## Verdict on this cycle's Combined Verdict contribution

**PARTIAL**, from this seat. Checkpoint criterion 2 remains correctly
N/A (no phenomenon-mechanism claim). The tripwire is genuinely
discharged — this is a real, purpose-built, article-loaded FDTD
measurement, not a sixth thin deferral. The PRIMARY result
(ENERGY-DOMINANT, falsifying the pre-registered ENERGY-DECOUPLED
prediction) is real, pre-licensed by committed text, and survives its
own hardest internal stress test (discounting the θ=38.6° outlier still
lands CONSISTENT, not DECOUPLED) — genuinely "a materially new finding,"
not a failure, exactly as pre-registered. **Checkpoint criterion 4 does
NOT fire** on any of the three gaps this review found (disclaimer
erosion; the dropped T9-comparison item; the false "reproduced this
cycle" citation) — all three are non-load-bearing, all three caught
blind, same cycle, before LOGBOOK, matching this program's own
established non-firing test. But the disclaimer-erosion finding is now a
**third** instance of an identical shape on this sub-thread and should
carry an explicit forward tripwire (§1 above) the way this program has
handled every other repeating near-miss (R9, R11, R12).

## Ranked candidate directions for Iteration 65

1. **Correct the three same-cycle gaps found here, same-shift, before
   this entry is cited elsewhere**: (a) add idealization 9/10's
   disclaimers inline at NOTES.md's Predictions §8 and Result P8
   restatements; (b) either run or correctly re-caption the T9
   "reproduced this cycle" citation; (c) restore the dropped informal
   T9-anchor comparison (§3/§4a above) as an explicit disclosed-context
   line, since the values are already sitting in `results.json`. All
   three are zero-FDTD, cheap, and close real (if non-load-bearing) gaps
   before they compound further down this sub-thread.
2. **Extend the raw `σ_abs/σ_ext(θ)` measurement (§3) beyond this
   cycle's 3-angle/36–42° window** — ideally onto the standing, now
   12-cycle-deferred x-wall wavelength-generality leg's own board item,
   or as its own cheap companion — to build the first real
   angle-dependence curve for the flagship absorber's extinction
   efficiency. This is the single most direct way this cycle's own
   incidental finding (§3) could eventually inform constraint 3's Tier-A
   generality question, which no prior cycle has measured at more than
   one angle.
3. **A densified re-run of P7's own classification at more than 3
   angles**, specifically to test whether the ENERGY-DOMINANT reading
   this cycle found is itself an artifact of `frac_contrast`'s
   denominator riding near a `delta_scene` zero-crossing (the disclosed,
   unresolved candidate explanation for θ=38.6° specifically) versus a
   genuine, smoothly-varying energy-dominant regime — this cycle's own
   biggest open question, and the most direct scientific follow-up to
   what was just measured.
4. PHOTONICS' own near-unanimous #1 (carried from Iteration 63): the
   grazing-incidence validity check on `edge_diffraction_c_empty_
   corrected` — unaffected by this cycle, still the highest-ranked
   standing item on the whole T28 board.
5. The x-wall wavelength-generality leg (now 12 consecutive cycles
   deferred, 076–087) — the single oldest item on the board; unrelated
   to this cycle's own scope but overdue enough that Iteration 65 should
   either run it or state explicitly, in writing, why not.
6. Standing carried-forward items, unaffected by this cycle: the
   full-scale null-calibration re-run (2 of 3 parts done per Iteration
   63), R12-into-standard-practice, PHOTONICS' domain-truncation test /
   EM's kernel rebuild for leg (b)'s Anchor 2, the near-null σ(I)
   article follow-up, QUANTUM's lossless-PEC-only-disk control, and the
   still-unresolved ritualization governance question (named Iteration
   61).
