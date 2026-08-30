# PHASE 5 — RED TEAM FINAL AUDIT · Panel Iteration 69 · exp-092
## "T28 Crossing Relocation & Caution-Zone Rebuild"

*Fresh sub-agent, no memory of any prior cycle. Read in full: `PANEL.md`
(charter + Checkpoint criteria + Phase-5 spec); `LOGBOOK.md`, all ~20,232
lines, offset-by-offset — the complete RULED OUT registry (R1–R15 full
text), ESTABLISHED, and LIVE THREADS, with particular depth on the R8
founding text (Iteration 52), the R13/R14/R15 founding texts (Iterations
64/65/68), the complete four-instance disclaimer-erosion lineage
(Iterations 53/63/64/65) and the Iteration-65 CHECKPOINT's own escalated,
unconditional "a fourth instance fires automatically" text, the exp-080
missing-`NOTES.md` precedent (Iteration 57) and exp-091's own Phase-5
final audit's non-firing ruling on the print-parity gap (Iteration 68,
§2 there); the complete exp-092 record (`phase1_proposal.md`, all five
Phase-2 critiques, `phase2_redteam_audit.md`, `phase3_synthesis.md`,
`NOTES.md`, `run.py`, `results.json`, `run_output.txt`); the complete
exp-091 record (`phase1_proposal.md`, five critiques,
`phase2_redteam_audit.md`, `phase3_synthesis.md`, `NOTES.md`, `run.py`,
`results.json`, `phase5_redteam_audit.md`) as the immediately preceding
cycle; all six exp-092 Phase-5 blind reviews (photonics, materials, em,
thermodynamics, quantum, vision); `lab/thermo_sidecar.py`. Every
load-bearing number below was independently re-derived from
`results.json`/`run_output.txt`/source, by invoking the actual committed
functions (`find_zero_crossings`, `ts.netd_disposition`,
`ts.mixed_length_scale_regime`), never hand-typed — R4 discipline,
applied to this audit's own claims as much as to the record under review.*

---

## 0. Independent re-verification of the load-bearing numbers (before adjudicating anything)

All confirmed bit-exact against `results.json`, `run_output.txt`, and
direct execution of the committed `run.py`/`lab/thermo_sidecar.py` code
(not against any review's own citation of them):

- **House gates.** `vac_pass`/`xi_pass`/`nonneg_pass` all `True`;
  `empty_leg_consistency_all_match=True` (all six freshly re-run empty
  legs reproduce exp-091's own filed `C_empty` values bit-exact). All 40
  FDTD calls present, matching the pre-registered design.
- **Rank 3, all six cells, recomputed from `results.json::rank3.per_theta`
  directly.** `delta_scene` ratio `0.9226442754936124` / `1.014147118444808`
  / `1.1720418612256387` at 37.2°/40.2°/41.4°, all sign-held; `frac_contrast`
  ratio `0.9381934454956976`/`1.0266706891311825`/`1.1827333731129215`.
  All six inside `[0.3,3.0]` with room (worst margin `1.18×`, well under
  half-way to `3.0` on a log scale). `p_abs_w` ratio
  `0.9610213000241329`/`0.9619165541390967`/`0.9602062494341871`;
  `ratio_abs_ext_dev_from_anchor` `0.77%`/`0.54%`/`0.93%`. **R3 CONFIRM
  and R3b CONFIRM are both correctly computed, not marginal calls.**
- **`sigma_max_R3_corrected=1/3`**, re-derived from
  `lab/materials.py::graded_black_shell`'s own linear-multiplier
  conductivity profile and `design_geometry.py::R3_R_OUT=round(78×1.5)=117`:
  native `τ_center=2×0.5×78=78`; as-filed R3 `τ_center=2×0.5×117=117`
  (1.5× inflation); corrected `78/(2×117)=1/3` exactly. Matches
  `run.py:119`'s own `assert abs(...-1/3)<1e-12`.
- **Both crossing locations, re-derived by directly invoking `run.py`'s
  own `find_zero_crossings`** (imported via `runpy.run_path`, not
  re-implemented) **against the exact combined-window values `run.py`
  itself builds** (Rank 1's seven fresh `delta_scene` values +
  exp-091's own filed `40.2°/40.4°/41.4°/41.6°` bracket, pulled at full
  precision from `experiments/091-.../results.json::raw.
  r3_leg2_cpl30_steps4200`/`r3_leg4_cpl30_steps4200_bracket`, not the
  4-significant-figure values printed in prose): **lower window** — one
  crossing, `40.07183833857387°` — bit-exact match to `results.json`'s
  filed `40.07183833857387`. **Upper window** — **two** crossings,
  `41.781067311937264°` and `41.8376530294636°` — the second reproduces
  `run_output.txt`'s own printed `41.8376530294636` bit-exact, but does
  **not** appear anywhere in `results.json::rank1.crossing_report`,
  which persists only `upper_crossing_cpl30=41.781067311937264` (the
  first). **MATERIALS' finding independently confirmed, at the source,
  not from its own citation of it** (§3 below).
- **Rank 2's DROP/RELABEL table**, re-imported `experiments/090-.../
  run.py`'s own `firth_logistic`/`auc`/`naive_mle_diverges` and re-run
  against the real `n=7` dataset myself: `AUC=1.0/1.0/0.8333`, zone
  `[1.4764,2.1709]`/unchanged/`[1.4764,1.3095]` (inverted),
  `m₅₀=2.071012796646712/1.818061.../1.031717...`,
  naive-MLE-diverges `True/True/False`. Bit-exact. **This is now at
  least a tenth independent reproduction of this specific table** across
  this sub-thread's history (EM Phase 1, QUANTUM/Red Team Phase 2, the
  Director twice, the live in-`run.py` recomputation, QUANTUM/Red Team's
  own Phase-5 reviews, and this audit).
- **NETD/detectability, computed for Rank 3's six cells** by directly
  invoking `ts.mixed_length_scale_regime`/`ts.netd_disposition` (the
  actual committed functions, via `run.py`'s own imported module
  namespace — not hand-derived) against the already-committed
  `sigma_corrected_p_abs_w_c`/`filed_p_abs_w_c` values: `dt_ss_full_K`
  `4.594353413478306e-05`/`5.0375476816593985e-05`/
  `5.1784646635965176e-05` K at 37.2°/40.2°/41.4° (sigma-corrected
  variant), all classified **UNDETECTABLE**, margins `435×`/`397×`/`386×`
  below the `NETD_BAND_K` floor — bit-exact match to THERMODYNAMICS'
  own independently-computed table. **Confirmed zero occurrences of
  `netd_classification`/`dt_ss_full_K`/`UNDETECTABLE` anywhere in the
  original `results.json` or `run_output.txt`** (direct grep, both files,
  §4 below), independent of trusting THERMODYNAMICS' own grep.
- **Duplicate `NOTES.md` placeholder (VISION's catch)**: confirmed
  already fixed. `git log` shows commit `5b12b4e` ("same-shift fix for
  VISION's own catch") landed after the Phase-4 close-out commit
  (`989a4a4`) and before the Phase-5 reviews that post-date it (QUANTUM,
  VISION themselves already read the fixed file). `grep -n "^## Learned\|
  ^## Next\|^## Result"` on the current file returns exactly one of each,
  at lines 258/386/420 — the fix landed cleanly, no residual duplicate.

No arithmetic, labeling, or geometry defect found anywhere independently
checkable. Every headline number cited by all six Phase-5 reviews
reproduces bit-exact.

---

## 1. Adjudication of the six Phase-5 reviews

### 1.1 PHOTONICS (CONCUR-WITH-GAP) — internal-inconsistency finding **UPHELD, real, and closed same-shift**

Independently re-derived both crossing locations from raw `per_theta`
values exactly as PHOTONICS did (§0 above) — the finding's own arithmetic
is not in question. The substantive claim — that Learned #3's "a
coherent, physically legible picture, not a numerical artifact" directly
answers the exact question Next #2 says is still open (genuine two-node
feature vs. under-resolved single deep null) — is correct on inspection:
both statements sit in the same document, written in the same Phase-4
close-out edit, about the same fact, and they disagree. **UPHOLD in
full.** Disposition and reasoning: §2 below.

### 1.2 MATERIALS (CONCUR-WITH-GAPS) — JSON-truncation finding **UPHELD, real, verified at the source, fixed same-shift**

Independently reproduced the missing-second-crossing defect directly from
`run.py`'s own control flow (§0 above) — `r1b_report["upper_crossing_cpl30"]
= float(upper_crossings[0])`, a single-element slice of a two-element
array whose own length (`len(upper_crossings)=2`) correctly drives the
scored NEITHER verdict elsewhere in the same function. The scored
verdict is genuinely unaffected (I confirm this independently: `r1a_verdict`
is computed from `len(lower_crossings)`/`len(upper_crossings)`, never from
`r1b_report`). **UPHOLD in full.** MATERIALS' further finding — that
Rank 3's CONFIRM does not, on its own text, cover the near-null region
Rank 1 discovers (none of the three tested angles sits closer than
`0.38°` to it, and the region's own `delta_scene` magnitude is an order
of magnitude smaller than anything Rank 3 perturbed) — independently
re-checked and correct: the closest Rank-3 angle to any Rank-1 crossing
is 40.2° (`0.128°` from the lower crossing), and even that proximity
shows no monotonic ratio-deviation trend with distance (40.2°'s own
deviation is the *smallest* of the three, not the largest) — so no
extrapolation of Rank 3's CONFIRM into the near-null region is licensed
either way. **UPHOLD.** MATERIALS' REALIZABILITY_MEMO coincidence-tracing
(§4 of its review) is independently checked and correct — a genuine
coincidence of the same `τ_center` identity arising from two physically
different operations (grid-refinement rescaling vs. real-object-scale
rescaling); no realizability content follows, and the record is right not
to re-open `REALIZABILITY_MEMO.md`. Disposition and fix: §3 below.

### 1.3 ELECTROMAGNETISM self-review (CONCUR-WITH-GAP) — **UPHOLD in full**

Every re-derivation matches §0. The self-diagnosed gap — Phase-1 §1
restating the qualitative "accumulated propagation phase" mechanism
argument a second cycle running, without running or disclosing the status
of the Yee-grid dispersion computation this same seat's own exp-091
Phase-5 review named as the needed follow-up — is real, independently
confirmed against both documents directly (`phase5_review_em.md` §4(i)–(ii)
of exp-091; `phase1_proposal.md` §1 of exp-092). The distinction EM itself
draws between component (a) (structural passivity/reciprocity/causality,
independently re-confirmed clean this cycle) and component (b) (the
specific accumulated-phase mechanism, still unverified) is correct and I
adopt it. **UPHOLD.** Disposition under R8: §4 below.

### 1.4 THERMODYNAMICS (CONCUR with likely PARTIAL) — **UPHOLD in full**

Independently re-derived the NETD-drop finding from source (§0 above) —
`cell_metrics()` computes `netd_classification`/`dt_ss_full_K` for every
one of this cycle's 20 unique cells, `pair_metrics()` even carries
`netd_classification_c` into its own return dict, and `rank3_report`/
`rank1_report` both drop it before it reaches `results.json`. Independently
confirmed present, unfixed, in exp-091's own record too (direct grep of
`experiments/091-.../results.json` for `netd_classification`: zero hits).
**UPHOLD in full.** THERMODYNAMICS' secondary finding — that "near-
saturation" is an imprecise citation for the ~4% `p_abs_w` swing, and the
extinction-paradox reading (T9) is the more precise, more falsifiable
established mechanism — is a genuine, correctly-argued refinement, though
explicitly non-load-bearing (changes no scored verdict) and resting on an
untested assumption of its own (whether `ratio_abs_ext` at `σ_max=0.5`
tracks the `0.51` anchor as closely as at `σ_max=1/3` — not verifiable
from committed data, as THERMODYNAMICS itself discloses). **UPHOLD**,
correctly scoped by its own author as a candidate reading, not a settled
decomposition. Disposition on the NETD gap's Checkpoint status: §4 below.

### 1.5 QUANTUM OPTICS (CONCUR) — **UPHOLD in full**

Independently re-derived every headline number from primitives — crossing
locations, Rank-3 ratios, Rank-2 table, and (added on its own initiative)
the `cpl=20` comparator baseline — with zero discrepancies anywhere,
matching this audit's own independent §0 reproduction exactly. This is
correctly the cleanest single-cycle record in this sub-thread's own
history by the numbers. The one substantive observation — that the
double-crossing's *second* crossing rests on two flanking points (41.8°,
42.0°) that are *both* `NODE-UNRESOLVABLE`, making its own evidentiary
basis weaker than the first crossing's — is independently confirmed
(`42.0°`: `frac_contrast=1.533e-4 < FLOOR=1.917e-4`, correctly
`floor_pass=False`) and folds directly into this audit's own ruling at §2.
**UPHOLD.** No Checkpoint-4 candidate raised by this review requires
independent adjudication beyond what §2/§3/§4/§5 below already cover.

### 1.6 VISION SCIENCE (CONCUR-WITH-GAP) — **UPHOLD; fix already landed, independently re-verified**

The duplicate/contradictory placeholder `## Learned`/`## Next` stub is
independently confirmed fixed (§0 above, via `git log` and direct
line-count grep) — VISION's own recommended fix (delete the stale
placeholder pair) was applied same-shift, correctly, before this audit
began. **UPHOLD**, no further action. VISION's separate finding — that
the double-crossing near-null has correctly received no constraint-3/4
perceptual reading anywhere in this cycle's own prose (`delta_scene` is a
two-config differential, not a real scene's absolute Weber contrast) — is
independently re-confirmed by tracing the same `run.py` line VISION cites
(`delta_scene = g_cell["C"] - c_cell["C"]`) and by an independent grep of
`NOTES.md` for the same terms. **UPHOLD.** The Iteration-61 ritualization
governance observation is real and independent of this cycle's own
findings; carried forward at §6/§8, not itself Checkpoint-worthy.

**No item from any of the six blind reviews is overridden.** All six
independently verify real, source-confirmed findings; none rests on a
misreading once checked directly against code and committed data.

---

## 2. Ruling on PHOTONICS' internal-inconsistency finding — real, a new gap shape, same-shift-fixable, non-firing

**Is this the established disclaimer-erosion shape (Iterations 53/63/64/65,
the Iteration-65 CHECKPOINT's escalated, unconditional rule)? No — checked
explicitly, not by pattern-matching.** Re-reading the Iteration-65 rule's
own text (LOGBOOK ~L4737–4776) verbatim: its defined shape is
*NETD-not-human-eye/constraint-3-not-tested language present in the
record's own supporting data but silently absent from one prose
restatement of the classification it governs* — a caveat correct in one
location, missing from another, both written in the same cycle. PHOTONICS'
finding shares none of that shape: there is no NETD/constraint-3/human-eye
disclaimer anywhere near it, and the defect is not a caveat's absence but
a positive claim ("not a numerical artifact") directly contradicting a
second positive claim ("still needs a check to tell genuine two-node from
under-resolved single null") elsewhere in the same document. This is a
**new failure shape**: an internal, same-document, same-edit assertion/
admission contradiction, not previously named anywhere in this
sub-thread's own registry (checked: neither R4/R9's "hand-typed figure"
lineage, nor the Iteration-65 disclaimer-carry-forward lineage, nor R13/
R14/R15's own resolution-sensitivity lineage covers this specific shape —
a write-up's own Learned section overclaiming certainty about a question
its own Next section discloses as open).

**Ruling: non-firing, on the standard discharge test this program applies
uniformly to every first-instance finding (R5 through R15, and every
non-firing disclaimer-erosion ruling before Iteration 65's fourth
instance) — caught blind, by PHOTONICS' own independent Phase-5 review,
before any LOGBOOK entry for this cycle exists.** It does not need the
Iteration-65 escalated rule to be non-firing, because it is not an
instance of the rule that escalated in the first place; it earns ordinary
first-instance treatment on its own, distinct shape.

**Fix applied, same-shift** (`NOTES.md`, both edited directly by this
audit): Learned #3 rewritten from "a coherent, physically legible picture,
not a numerical artifact" to "consistent with, but not yet independently
confirmed as, a genuine two-node feature" — matching almost verbatim the
walk-back language the task brief itself anticipates, and independently
the exact correction PHOTONICS' own review recommends. The rewritten text
also explicitly names *why* the original corroboration was weaker than
claimed: all three cited "independent" signals (two sign changes, one
`NODE-UNRESOLVABLE` classification) are drawn from the same
`floor_pass=False` neighborhood R13's own gate exists to flag as
untrustworthy — QUANTUM's own §2 finding, folded in here since it sharpens
the same correction rather than opening a separate one. A second,
related overclaim MATERIALS independently found (§1.2/§3) — the Result
section's "Rank 1's own results... directly comparable... with no
sigma-scaling caveat" sentence, which does not disclose that Rank 3 never
tested the near-null region — is corrected in the same edit pass, scoped
explicitly to "at the three tested census angles." **The Next section is
also re-ordered same-shift** (§7 below) so the denser-sweep resolution
check that Learned #3's corrected language now points to is no longer
ranked below the caution-zone re-fit it should gate.

---

## 3. Ruling on MATERIALS' JSON-truncation finding — real, verified, fixed additively (results.json patched, run.py corrected forward)

**Real and verified independently at the source** (§0/§1.2 above): `run.py`
computes and correctly counts both upper-window crossings but persists
only the first to `results.json::rank1.crossing_report`. **Does this
require touching the frozen `results.json`?** House convention generally
corrects forward (a frozen document's own prose is not silently
rewritten) — but this program's own record contains a direct, on-point
precedent for an **additive** same-shift patch to a frozen `results.json`
specifically: the `t23_disposition` key added post-hoc at Iteration 22/23
(LOGBOOK ~L1967), and the regenerated-but-bit-identical `results.json` at
Iteration 46's own 20-item docket (LOGBOOK ~L12787). Both share this
cycle's own exact shape: a key that adds already-correct, already-computed
information without altering any existing scored field. That is the
situation here precisely — the second crossing (`41.8376530294636°`) is
not new information; `run_output.txt` and `NOTES.md` already carry it
correctly, and `run.py` itself already computed and printed it. Silently
leaving `results.json` as the one incomplete artifact, when the program's
own convention treats it as "the machine-readable source most reused code
pulls from" (MATERIALS' own framing, and correct — Rank 2's own reuse
pattern of `experiments/090-.../results.json` is exactly this convention
in action), is the disposition most likely to actually cause the exact
harm MATERIALS names: a future Iteration-70 script building the R15
re-fit from `results.json` alone silently receiving two crossings where
three exist.

**Ruling: fix now, additively — decided and applied, not deferred.**

**Applied** (`results.json`, patched via a script that invokes the
actual committed `find_zero_crossings` function against full-precision
inputs pulled from exp-091's own committed `results.json::raw` block, not
hand-derived — R4 discipline applied to this fix itself, verified §0
above):

- `rank1.crossing_report` gains `lower_crossings_cpl30_all`/
  `upper_crossings_cpl30_all` (the complete per-window lists) and
  `upper_crossing_cpl30_second` (`41.8376530294636`) with its own two
  comparator shifts, matching `run_output.txt`'s own printed values
  bit-exact.
- **Zero existing fields altered or removed** — independently verified by
  a full structural diff against the pre-patch file (every existing key's
  value identical; only new keys added, confirmed programmatically, not
  merely by inspection of the `git diff`, which shows spurious `-`/`+`
  lines from JSON re-serialization/trailing-comma placement, not value
  changes).
- A `phase5_redteam_backfill` top-level key documents exactly what was
  added, by what process, and why — matching this program's own
  disclosure convention for same-shift fixes.

**`run.py` is also corrected forward** (both the crossing-list gap and
the NETD gap this audit rules on at §4): `r1b_report` now persists
`lower_crossings_cpl30_all`/`upper_crossings_cpl30_all` alongside the
existing singular fields, so a future re-run of this exact script
(reusing this code, as this whole T28 sub-thread routinely does) does not
reproduce the gap a third time. **This is a code fix, not a re-run** —
the corrected `run.py` was not re-executed this audit (that would cost
new FDTD, out of scope for a same-shift text/JSON fix); it takes effect
the next time this file's own machinery is invoked.

---

## 4. Ruling on THERMODYNAMICS' cross-cycle NETD-persistence gap — first-time naming, non-firing, forward tripwire set explicitly

**The core question, ruled explicitly per the task brief: is this "known,
named, ignored" (Checkpoint criterion 4) because it recurs across two
cycles, or a first catch because it was never named until now?**

**Ruling: first catch — non-firing — because Checkpoint criterion 4's own
operative test, across every rule in this program's registry (R5 through
R15, without exception), is whether a defect was *previously named and
then left unaddressed*, not whether the underlying code defect existed
unnoticed across multiple cycles.** I independently re-ran THERMODYNAMICS'
own search (grepped LOGBOOK.md's full RULED OUT text and every T28
Phase-5 review filename back through exp-087 for `netd_classification`,
`netd_disposition`, "never reported", "silently dropped") and confirm:
**zero prior hits.** No LOGBOOK entry, no prior Phase-5 review, no
R-numbered rule has ever named this specific gap before THERMODYNAMICS'
own exp-092 Phase-5 review. The fact that the *same underlying code*
(inherited by exp-092 from exp-091, itself inherited from exp-087's own
`cell_metrics`/`pair_metrics` lineage) silently dropped the field in both
of the two most recent cycles is a fact about how long the defect has
existed in the codebase, not a fact about whether it was *known* in this
program's own operative sense — a defect nobody has ever named cannot
have been ignored. This is exactly the same logical structure this
program's Phase-5 audit already applied one cycle ago to a structurally
adjacent case: exp-091's own Red Team final audit (§2 there) ruled the
print-parity gap (a different, but related, disclaimer/data-surfacing
defect on the same channel) non-firing on identical reasoning — a defect
"first exercised in this exact cycle" or "first named here" receives
founding-instance treatment, matching R5/R6/R9/R10/R11/R12/R13/R14/R15's
own unbroken precedent that a rule's founding cycle establishes the
standard rather than retroactively violating it.

**One distinction worth being precise about, since it does NOT change the
ruling but sharpens it**: this is a third, mechanistically distinct gap
shape, not a repeat of either the Iteration-65 disclaimer lineage (a
caveat missing from one prose location, present in another) or exp-091's
own print-parity gap (data correctly in `results.json`, never `print()`-ed
to stdout). Here, the underlying **classification itself is missing from
both** `results.json` *and* `run_output.txt` — only the generic disclaimer
boilerplate (what NETD *is*) survives, never the cycle's own actual NETD
*reading*. THERMODYNAMICS' own characterization — "not a disclaimer-
carry-forward failure... but the inverse: the data the disclaimer exists
to qualify is simply missing" — is correct and independently confirmed
(§0). A fresh shape gets fresh, first-instance treatment; it does not
inherit the Iteration-65 lineage's escalated, unconditional consequence,
which is textually scoped to that lineage's own specific mechanism.

**Fix applied, additively, where the underlying data permits it** (§3's
own precedent, extended): `results.json::rank3.per_theta` backfilled with
`netd_classification`/`dt_ss_full_K` for both the `sigma_corrected` and
`filed` `p_abs_w` variants at all three census angles, computed by
invoking `ts.mixed_length_scale_regime`/`ts.netd_disposition` directly
(§0) — zero new FDTD, since the underlying `p_abs_w` was already
committed for these six cells. All six classify **UNDETECTABLE**, matching
the established exp-087 margin band (386×–435× below the `NETD_BAND_K`
floor) — informative in the sense that a reader no longer has to
independently re-derive it, unremarkable in the sense that nothing here
threatens any standing verdict. **Rank 1's own 14 cells cannot be
similarly backfilled** — their individual `p_abs_w` values were never
persisted either (only the ratio `frac_p_abs`), and recovering them would
require new FDTD, out of scope for a same-shift fix. Named open, not
fixed. `run.py` is corrected forward (§3) so both Rank 3's and Rank 1's
own future re-runs thread `netd_classification`/`dt_ss_full_K` through to
`results.json` without a further silent drop.

**Forward tripwire, set explicitly, matching THERMODYNAMICS' own proposed
standard and this program's own established "third consecutive instance"
convention** (paralleling R11's `free_period_with_widening` precedent and
the disclaimer-erosion lineage's own four-strikes structure): a third
T28 cycle that computes but does not report a per-cell NETD classification
on this channel, **after this audit has named the gap explicitly and
`run.py` has been corrected forward**, would no longer receive
first-instance treatment and should fire Checkpoint criterion 4
automatically, on the same "known, named, ignored" standard R6 through
R15 already apply. This tripwire is now itself part of the named record,
for the next Phase-5 audit that touches this machinery to enforce.

---

## 5. Ruling on EM's own self-review gap — the twice-cited, once-run-nowhere Yee-dispersion check — non-firing, but elevated to a mandatory Iteration-70 item under R8

**The question, per the task brief: does R8 fire automatically here?**
R8's own text (LOGBOOK ~L220–241) requires two conjoined conditions before
automatic firing: **(a)** the named check was affordable and not run, AND
**(b)** the gap later proves outcome-determining. Both must hold; I check
each independently rather than assuming either.

**(a) Affordable and not run: yes, clearly.** EM's own review states this
plainly, and I confirm independently: the Yee-grid dispersion phase
accumulation is a **desk calculation** — zero new FDTD, using this bench's
own already-established dispersion relation and the aperture's own known
geometry. It was named once, in writing, as a ranked Iteration-70 item at
exp-091's own Phase-5 review (`phase5_review_em.md` §4, ranked item 2),
and it was not run at exp-092 Phase-1 — the same seat's `phase1_proposal.md`
§1 restates the identical qualitative claim a second cycle running,
without running the check or disclosing that it remains unverified.

**(b) Outcome-determining: no, checked directly against this cycle's own
scored verdicts.** R3/R3b/R1a/R1b/R2 are all direct FDTD or desk
measurements; none of them is derived from, or gated by, the qualitative
"accumulated propagation phase" mechanism argument in Phase-1 §1. The
crossing locations (`40.0718°`, `41.7811°`/`41.8377°`) were found
empirically by `find_zero_crossings` against real `delta_scene(θ)` data,
not predicted or validated by a phase-integral computation. Rank 3's
CONFIRM is a material-parameter test (component (a) of EM's own
argument — passivity/reciprocity/causality bookkeeping), independent of
whether component (b)'s specific dispersion mechanism is verified. **No
scored finding this cycle would change, or would have been differently
interpreted, had the integral been computed and come out differently** —
the un-run check is load-bearing to a Phase-1 *narrative* argument, not to
any Phase-4/Phase-5 *result*.

**Ruling: R8's automatic-fire condition does not engage — condition (b)
is not met.** This is not, however, the same clean non-firing exp-091's
own audit granted this argument one cycle ago (§1.3 there: "correctly
flagged forward, not silently assumed"). At exp-091, the gap was
explicitly disclosed as an open item at the point it was first named.
Here, `phase1_proposal.md` §1 re-cites the identical qualitative claim
without any such disclosure — a **new, narrower** defect than R8's
founding shape (which concerned an *argued-as-robust* claim, not a
*silently re-cited* one), caught here, at Phase 5, by the same seat's own
self-review, before this cycle's own LOGBOOK entry exists — the standard
discharge condition, met. **I rule this non-firing on the standard
discharge test, but I decline to treat it as a routine, low-priority
deferral.** This is now the **second** cycle this exact, affordable,
zero-FDTD, charter-owned check has been named and not run, by the same
seat both times. Matching the tripwire logic applied at §4 and this
program's own established convention for a check that survives one
disclosed deferral but risks becoming a pattern:

**Elevated, explicitly, to a mandatory (not merely ranked) Iteration-70
item** — not because it is Checkpoint-4-worthy this cycle, but because a
third cycle citing this argument without either running the check or
explicitly disclosing that it remains unverified would cross into R8's
own "known, named, ignored" territory on its own text, independent of
whether any future scored result happens to depend on it. This tripwire
is stated here as part of the named record, matching §4's own.

---

## 6. Checkpoint criteria — all five worked through explicitly

**Criterion 1 (all constraint metrics pass — candidate reproduction):**
does not fire. No constraint-1–4 claim is made anywhere in this cycle;
T1 route N/A throughout, independently reconfirmed against the unbroken
LOGBOOK record for this exact desk/instrument sub-thread since exp-069
(every entry, Iteration 46 through 68, reads "T1 route N/A"). There is no
metric to have passed.

**Criterion 2 (a proven mechanism-class boundary, gates clean):** N/A,
correctly and consistently — this cycle takes no position on
σ(I)/σ(x,t)/angular-selectivity/sub-threshold-operation and does not
touch `REALIZABILITY_MEMO.md` (independently confirmed correct not to,
§1.2 above — the `sigma_max=1/3` coincidence with `REALIZABILITY_MEMO`
Entry 2 is a numerical coincidence of the same τ_center identity, not a
shared physical claim).

**Criterion 3 (engine physics beyond validated bench classes):** does not
fire. No new `lab/` engine machinery — `_run_sim_r3_sigma`/
`build_article_r3_sigma` are parametrized variants of exp-091's own
already-validated `_run_sim_r3`/`build_article_r3`, confirmed by direct
source inspection (§0/§1.2, MATERIALS' own independent check of
`graded_black_shell`'s actual signature). The only new geometry-adjacent
parameter, `sigma_max`, is an existing function's own existing keyword
argument, not new physics.

**Criterion 5 (two consecutive non-advancing iterations):** does not
fire. exp-091 was itself logbook-advancing (R15 adopted, the caution zone
materially revised). exp-092 directly discharges R15's own single most
consequential open item (the true `cpl=30` crossing locations were
unknown; they are now located, cleanly, under a sigma-validated article)
and delivers a second, independently confirmed clean result (Rank 3's
CONFIRM) plus a genuinely new finding (the upper-window near-degenerate
double root) — logbook-advancing by a wide margin on both criteria's own
text.

**Criterion 4 (program-integrity drift — unfalsifiable claims, a
constraint quietly dropped, or a "known, named, ignored" rule violation):**
**does not fire**, worked through every candidate individually, not by
inertia or by analogy to prior non-firing rulings:

- **PHOTONICS' internal-inconsistency finding** — ruled non-firing at §2:
  a new, previously-unnamed failure shape (same-document assertion/
  admission contradiction), not an instance of the Iteration-65
  disclaimer-erosion lineage; caught blind, before this cycle's own
  LOGBOOK entry; fixed same-shift.
- **MATERIALS' JSON-truncation finding** — non-load-bearing to any scored
  verdict (independently confirmed, §3); caught blind, before LOGBOOK;
  fixed additively, same-shift.
- **EM's own twice-named, once-run-nowhere dispersion check** — ruled
  non-firing at §5: R8's own conjunctive test is not satisfied (the gap
  is not outcome-determining this cycle), and this is the check's
  *second* naming, not a "known, named, ignored" third-strike pattern —
  but elevated to a mandatory Iteration-70 item with an explicit tripwire
  for a third occurrence.
- **THERMODYNAMICS' NETD-persistence gap** — ruled non-firing at §4: the
  underlying code defect is two cycles old, but the *naming* of it is
  brand new (verified: zero prior LOGBOOK/Phase-5-review hits for this
  specific gap) — a founding catch, not a recurrence of a known-and-
  ignored defect, matching this program's own unbroken precedent that a
  rule fires on recurrence-after-naming, not on recurrence-before-naming.
  Backfilled additively where the data permits (Rank 3); `run.py`
  corrected forward for both Rank 3 and Rank 1; forward tripwire set for
  a third occurrence.
- **VISION's duplicate-placeholder catch** — already fixed same-shift,
  before this audit began (independently reconfirmed at §0); non-firing,
  matching the exp-080/exp-091 precedent for exactly this class of
  record-hygiene defect (caught blind, fixed same-shift, non-scientific).
- **No LOGBOOK misstatement found anywhere in this cycle's own record** —
  every cited historical figure (the n=7 caution-zone table, the FLOOR
  value, the known `cpl=20` crossing locations, exp-091's own filed
  bracket values, the T9 anchor) reproduces bit-exact against its own
  primary source, checked independently at this audit (§0) as at every
  earlier phase of this cycle.

**No criterion fires.** Consistent with this program's unbroken
precedent, a Checkpoint firing (had one occurred) would be a
notification, not a pause — moot here, stated for completeness per
PANEL.md's own procedure.

---

## 7. Combined Verdict: **PARTIAL**

**Confirmed, cleanly, by this cycle:**
- Rank 3's CONFIRM (the unscaled `sigma_max` confound does not materially
  contaminate the PRIMARY `delta_scene`/`frac_contrast` channel, at the
  three tested census angles) — independently re-verified bit-exact, all
  six cells comfortably inside band, no sign flips.
- Rank 3b's CONFIRM (`p_abs_w`/`ratio_abs_ext` both move as predicted,
  small and consistent) — independently re-verified.
- The lower-window crossing (`40.0718°`, `-0.194°` from the known
  `cpl=20` location) — a clean, single, monotonic, independently
  reproduced result.
- Rank 2's desk recomputation (now independently reproduced at least a
  tenth time across this sub-thread's history) — bit-exact.
- The empty-leg re-run-not-reuse fix — genuine FDTD, bit-exact
  determinism confirmed against exp-091's own filed values.
- All house gates, exhaustively, not sampled.

**Genuinely new, and genuinely still open:**
- The upper window's own double-crossing structure (`41.7811°`/`41.8377°`,
  `0.057°` apart, straddling a genuine near-total interference null) is a
  real, independently reproduced finding — but its own status (a genuine
  two-node feature, vs. an under-resolved single deep null) remains
  undetermined, resting entirely on floor-gate-failing data, exactly as
  this cycle's own corrected Learned #3 (§2) now states plainly rather
  than overclaiming resolved.
- The Rank-3 CONFIRM's own scope does not extend to this specific region
  (§1.2/§2/§3) — a real, disclosed, now-explicitly-stated limitation, not
  a defect in what was tested.

**Process, closed same-shift by this audit:**
- PHOTONICS' internal-inconsistency finding (§2) — fixed, non-firing.
- MATERIALS' JSON-truncation finding (§3) — fixed additively, non-firing.
- THERMODYNAMICS' NETD-persistence gap (§4) — backfilled where possible,
  corrected forward in `run.py`, non-firing, tripwire set.
- EM's own dispersion-integral gap (§5) — non-firing this cycle, elevated
  to mandatory Iteration-70 status with an explicit third-occurrence
  tripwire.
- VISION's duplicate-placeholder catch — already fixed, independently
  reconfirmed.

**No Checkpoint criterion fires** (§6, worked through all five
explicitly). Not RULED OUT (no mechanism class is engaged or foreclosed;
T1 route N/A throughout, correctly) and not PROMISING (no constraint-
metric progress is claimed, correctly, by this cycle's own scope).
**PARTIAL** is the correct characterization: this cycle cleanly closes
R15's own founding question for the lower crossing and the sigma_max
confound, while its own most novel finding (the upper double-crossing)
opens a new, currently-unresolved question rather than closing one —
exactly the shape QUANTUM's own review independently characterizes as
"the cleanest single-cycle record this sub-thread has produced," with the
genuine caveat that "clean" describes the arithmetic, not yet the
underlying physical picture in the one region that matters most for what
comes next.

---

## 8. Reconciled Iteration-70 recommendations (ranked, merging all six reviews' own top-3s)

**Strong convergence, checked explicitly against the task's own
question**: five of six seats (PHOTONICS #1, MATERIALS #1/#3 split,
ELECTROMAGNETISM #1, THERMODYNAMICS #1, QUANTUM #2) independently name
some version of "resolve the upper-window double-crossing ambiguity" as
at or near the top of their own list — the same convergence pattern that,
one cycle ago, led exp-091's own Red Team audit to reorder its own
Iteration-69 recommendations. Applied identically here: **NOTES.md's own
Next section has already been re-ordered same-shift** (§2 above) to put
the resolution check ahead of the caution-zone re-fit it should gate.
The ranking below reflects that reordering, not the reverse.

**Tier 0 — same-shift, applied by this audit, before this document is
cited:** NOTES.md Learned #3 corrected (§2); the sigma-branch CONFIRM
scope-qualified (§2); NOTES.md Next section re-ordered (§2/here);
`results.json` patched additively for the missing second crossing (§3)
and the six backfillable NETD classifications (§4); `run.py` corrected
forward for both gaps (§3/§4); Checkpoint ruling recorded (§6); EM's own
dispersion-integral item elevated to mandatory with a tripwire (§5);
THERMODYNAMICS' NETD gap given a forward tripwire (§4).

**Tier 1 — the single highest-value next step, near-unanimous:**

1. **A dedicated, denser off-grid or `cpl=40` sweep of the upper window
   (≈41.6°–42.2°, finer than the native 0.2° `DENSE_ANGLES` step)** to
   determine whether `41.7811°`/`41.8377°` is a genuine two-node feature
   or an under-resolved single deep null. Named by PHOTONICS (#1,
   explicitly elevated above the caution-zone re-fit), ELECTROMAGNETISM
   (#1), QUANTUM (Rank 2, a cheaper settling-doubled spot-check variant
   at the two specific floor-failing angles first), and NOTES.md's own
   (now-reordered) Next item 1. The single most decisive, cheapest test
   available of this cycle's own most consequential open question — gates
   whether item 2 below should treat the upper region as one boundary
   point or two.
2. **Re-fit R15's own caution zone using the newly-located `cpl=30`
   crossings** (lower at `40.0718°`; upper as either one or two points,
   per item 1's own resolution) as direct inputs — the natural completion
   of R15's own founding mandate, now that Rank 3 has removed the
   sigma_max confound as a rival explanation. Named by every seat that
   ranked it (MATERIALS #3, QUANTUM Rank 1, THERMODYNAMICS #1 combined
   with a co-swept energy channel, PHOTONICS #2, VISION #2) — should run
   gated on, or explicitly report both readings pending, item 1.

**Tier 2 — cheap, real, non-load-bearing to any current verdict:**

3. **A small, targeted `sigma_max` PRIMARY-channel check at the upper
   window's own near-null region specifically** (MATERIALS #1) — 4–8
   calls, mirroring Rank 3's own recipe, closing the specific scope gap
   this audit named at §2/§3 (Rank 3's CONFIRM does not currently cover
   the region item 1 is about to make load-bearing).
4. **Compute the Yee-grid dispersion phase-accumulation integral** (EM's
   own #2, now elevated to mandatory at §5) — zero new FDTD, a desk
   calculation, closing a twice-named, still-unrun check before a third
   citation makes it Checkpoint-4-worthy under R8.
5. **Thread `netd_classification`/`dt_ss_full_K` through Rank 1's own 14
   cells** (THERMODYNAMICS #3) — requires new FDTD (individual `p_abs_w`
   values were never persisted for these cells), the one item on this
   list this audit could not close additively; closes the gap `run.py`'s
   own forward fix (§4) only guarantees for a future re-run.
6. **Extend the search past 42.0°** (NOTES.md's own Next item 3,
   unchanged) — the true picture beyond the window edge remains unknown.

**Tier 3 — governance, standing, unaffected by this cycle:** PHOTONICS'
own grazing-incidence validity check (still the single most-repeated item
on the whole T28 board); the x-wall wavelength-generality leg (well past
sixteen consecutive cycles deferred); the still-queued R14(b) formal
null-controlled period fit; the Rank-2-in-exp-090's-own-queue unbiased
margin-vs-distance rebuild on the full 31-point window; a `cpl=40` third
resolution point at the original three census angles; extending R3 to
exp-090's remaining four caution-zone points; VISION's own restated
Iteration-61 ritualization governance question (24 consecutive cycles
with no constraint-3-facing run) — carried forward unchanged, a decision
still owed, not a new finding this cycle adds urgency to beyond what
VISION's own review already states.

---

## 9. What this audit changed, exactly, and what it did not

**Edited, same-shift:**
- `NOTES.md` — Learned #3 rewritten (overclaim walked back, §2); the
  sigma-branch Result bullet scope-qualified (§2); the Next section
  re-ordered with an explicit note explaining why (§2/§8), item text
  otherwise unchanged.
- `results.json` — additive only, verified by full structural diff
  against the pre-patch file (§3): `rank1.crossing_report` gains the
  complete crossing lists and the second upper crossing; `rank3.per_theta`
  gains NETD classification/`dt_ss_full_K` for both `sigma_corrected` and
  `filed` variants at all three angles; a `phase5_redteam_backfill` key
  documents the change. **Zero existing scored field altered.**
- `run.py` — corrected forward, not re-run: `r1b_report` now persists
  full per-window crossing lists; `pair_metrics`/`rank3_report`/
  `rank1_report` now thread `netd_classification`/`dt_ss_full_K` through
  to their own returned dicts (Rank 3 fully closes the gap on the next
  re-run; Rank 1's own 14 cells still need new FDTD to populate, per §4).

**Not changed:** any scored verdict (R3, R3b, R1a, R1b, R2, the
sigma-branch decision, all house gates) — every number in this cycle's
own Result section stands exactly as filed, independently re-verified at
§0. No RULED OUT rule is revisited or violated. No new numbered rule is
proposed by this audit — every finding above fits inside R4/R8/R13's own
existing text, or is explicitly ruled a first-instance, non-firing gap on
this program's own established discharge test.

Full record: `experiments/092-t28-crossing-relocation-caution-zone-rebuild/`
— `phase1_proposal.md`, five Phase-2 blind critiques, `phase2_redteam_
audit.md`, `phase3_synthesis.md`, `NOTES.md` (Learned/Next corrected,
this audit), `run.py`/`results.json` (both corrected, this audit),
`run_output.txt`, six Phase-5 blind reviews, this document.
