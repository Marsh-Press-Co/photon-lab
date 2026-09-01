# Phase 5 Review — THERMODYNAMICS (Panel Iteration 77, exp-100)

## Reading confirmation

Read in full: LOGBOOK.md's RULED OUT registry (R1–R20), ESTABLISHED section,
and LIVE THREADS T1–T28 (the T28 sub-thread narrative through Iteration 76,
exp-069–exp-099) — LOGBOOK's verbatim per-phase "# Iterations" transcript
currently extends only through Iteration 57 (exp-080); Iterations 58–76 exist
in the document only as the condensed running LIVE-THREADS record, which was
read in full. Also read: `NOTES.md`, `phase1_proposal.md`, all five
`phase2_critique_*.md` files, `phase2_redteam_audit.md`, `disposition_memo.md`,
`run.py`, `results.json`, and `run_output.txt` for this experiment. The
Iteration-76 self-review citation (LOGBOOK lines 6688–6691) was located and
read in its surrounding context.

## Verdict: **CONCUR-WITH-GAP(S)**

## 1. Fix 7 (netd_row persistence) — verified directly, genuinely landed, with one gap the data check alone cannot catch

**The literal commitment is honored, confirmed against `results.json`
directly, not on the strength of NOTES.md's own prose.** All 6
`tier2_leg_b.report` rows (θ = 37.127246°, 38.590230°, 40.265420°,
40.960901°, 41.460901°, 42.960901°) carry the full `netd_row()` output —
`p_abs_w_c/g`, `dt_ss_full_K_c/g`, `netd_classification_c/g`,
`sigma_ext_cells_c/g`, `ratio_abs_ext_raw_c/g` — for both `C40_R4` and
`G40_R4`. `run.py:531-534` calls `netd_row(pm)` inside the same per-angle
loop that builds each report row and hard-asserts
`set(nrow.keys()) >= NETD_ROW_KEYS` **before** any row is written, HALTing
the whole run rather than silently shipping a partial row — a stronger
mechanical guarantee than either prior occurrence of this pattern shipped
(neither exp-092/93's original gap nor exp-094's founding R16 instance had
a code-level assert gating `results.json` on this specific invariant). Read
back, the values are physically sensible and internally consistent: all 12
classifications (6 angles × 2 configs) read `UNDETECTABLE`, `p_abs_w`
clusters at 2.79×10⁻¹²–3.31×10⁻¹² (bench units) rising monotonically with
θ, `dt_ss_full_K` at 4.58×10⁻⁵–5.43×10⁻⁵ K, and — a genuine free
byproduct nobody flagged in advance — `ratio_abs_ext_raw_{c,g}` sits at
0.5129–0.5153 at all 6 angles/both configs, reconfirming T9's established
~0.51 anchor generalizes to this R4 family at oblique incidence for the
first time on this specific 6-angle set. **This is a genuine close of the
specific, narrow pattern R16 and I flagged as a live third-occurrence
risk at Phase 2**: the field is not merely disclaimer-covered, it is
computed, persisted, and now code-enforced. I do not read this as
triggering R16's own forward clause (that clause fires on the field
*failing to be persisted* a third time; here it was persisted, verifiably).

**But a gap remains, and it is exactly the shape the task brief asked me to
check for.** I grepped `NOTES.md`'s Result section (lines ~360–494) and
Learned section (~496–539) for every term this sidecar could plausibly
surface under — `netd`, `NETD`, `UNDETECTABLE`, `thermal`, `ΔT`,
`dt_ss`, `sidecar`, `energy`, `absorb`, `power`, `Watt` — and found **zero
occurrences in either section**. Every mention of the thermal fields in
the entire document is confined to the Phase-1-derived "Changes from
Phase 1" section (lines 150–156, stating the *commitment*) and the Setup
section (line 249, restating the same commitment) and the frozen
Predictions table (line 344, predicting only that presence-and-assertion
would hold, not any classification value). The Result section's own Leg-B
paragraphs discuss `observer_record_t28` (PASS) and `beam_behind_t28`
(UNINTERPRETABLE) at length but say nothing about what the sidecar found —
not the classification, not the ΔT scale, not even a one-line "all 12
cells read UNDETECTABLE, consistent with T9/T5's established pattern for
this article." The same silence covers the six fresh `ratio_abs_ext_raw`
confirmations of T9's anchor at these specific angles — a free, genuinely
new generalization this cycle produced and then never mentioned, even
though the *pooled*, cross-experiment `Δratio_abs_ext(θ)` check from Tier
1 item 1(c) — a different computation, reusing old filed data rather than
this cycle's own new points — does get a Result-section sentence (lines
407–409).

**So: the answer to the brief's own question is "both."** Fix 7's literal
text ("netd_row() called and persisted for all 6 new pairs, asserted
present before results.json is written") is satisfied exactly, and I
credit that as real, mechanically-verified progress — the strongest
version of this commitment this sub-thread has ever shipped. But the
broader spirit the fix exists to serve — that this seat's own charter
finding is actually *engaged with*, not merely filed — recurs in a
narrower, one-level-up form: computed, persisted, asserted, and then
silently absent from the prose a future reader or LOGBOOK entry will
actually cite. This is not a literal third R16 occurrence (R16's trigger
is non-persistence, discharged here) and I am not asserting a new rule —
that is Red Team's call — but it is the same family of gap this exact
seat's own Iteration-76 self-review found in itself ("its own charter
instrument... silently omitted from Result/Learned," LOGBOOK 6688–6691),
recurring at Iteration 77 in a form the code-level check cannot see: a
`results.json` diff would show fix 7 fully honored; a diff against
`NOTES.md`'s own Result section shows the substantive scientific content
of that same fix still never reached the write-up a reader actually
consumes. I flag it plainly rather than resolve it myself.

## 2. The two new instruments' own energy implications

**`observer_record_t28`'s near-total absence of specular return raises no
new re-radiation/detectability question — it is fully consistent with,
and independently corroborated by, this cycle's own sidecar reading.** All
6 empty-scene self-ratios and all 6 article-loaded norms read within a
factor of ~4 of the established camera floor (1.0×10⁻⁴–3.9×10⁻⁴), and the
sidecar's own `p_abs_w` at the same 6 angles is tiny and classified
UNDETECTABLE throughout. Both instruments are telling the same story from
different sides: essentially none of the intercepted power is returning
toward this one observer direction, and essentially none of it is being
retained as heat either. Nothing here is in tension, and nothing here
raises a new thermal-detectability concern.

**`beam_behind_t28`'s UNINTERPRETABLE reading, by contrast, leaves exactly
the question my charter is supposed to answer open, not closed.** The
established graded_black_shell figure (near-normal incidence) is
beam-behind ≈1.5–1.8%: essentially all incident beam power is either
absorbed or scattered out of the forward path. This cycle's sidecar
confirms the *absorbed* share stays tiny at 37°–43° too (UNDETECTABLE,
consistent with `ratio_abs_ext≈0.51` holding at oblique incidence). But
with the forward/transmitted channel's own reading corrupted by a
diagnosed window-placement defect (reading 42–46%, dramatically above the
established figure, for reasons NOTES.md itself correctly attributes to
mis-centering, not physics), the three-way energy partition this seat's
charter exists to close — absorbed (now pinned, tiny) / returned to one
observer direction (now pinned, tiny, though only along the single scalar
channel Idealization 67 discloses) / continuing forward past the object
(currently unmeasurable) — cannot actually be closed this cycle. This is
not a new anomaly and I am not raising an alarm: the one number that is
wrong is diagnosed as an instrument defect, not a physical finding, and
there is no evidence of large real transmission. But it is the correct,
charter-relevant reason the corrected Iteration-78 beam-behind re-run
should not be scored as a stand-alone constraint-1 number in isolation —
see recommendation (1) below.

## 3. Ranked top-3 candidate directions for Iteration 78 (THERMODYNAMICS' seat)

1. **Endorse NOTES.md's own Tier-0 fix (`beam_behind_t28`'s window
   re-centering / closed-box replacement) as the top priority, and attach
   a zero-marginal-cost thermodynamic framing requirement to it**: once
   the corrected forward-flux reading lands at the same 6 angles, report
   it explicitly alongside the already-filed `p_abs_w`/`netd_classification`
   and `observer_article_norm` figures as one three-way energy-partition
   table (absorbed / observer-direction return / forward-continuing), not
   as a standalone corrected constraint-1 ratio. If the corrected reading
   confirms near-total blocking (∼1–2%, matching the established
   near-normal figure), that closes this seat's own open question at
   essentially zero added cost. If it instead reveals a materially larger
   oblique-incidence transmission fraction, that is a genuine, previously
   unasked re-radiation/energy-routing question (where does that power
   go, and would it be detectable at whatever surface it eventually
   terminates on) — worth flagging explicitly, not assumed either way in
   advance.

2. **A standing-rule candidate for Red Team's consideration, not asserted
   here as adopted**: R16 currently polices *persistence* of a computed
   NETD/thermal byproduct; this cycle shows persistence alone is not
   sufficient to guarantee the finding is actually engaged with in the
   Result/Learned prose a future citation will read. A cheap, precedented
   fix exists and has already been used for an analogous gap: Iteration
   65's own dual-section carried-idealizations-banner rule (adopted after
   a disclaimer proved not to propagate from Predictions into Result on
   its own) is the direct structural analog — an equivalent "any cycle
   that persists a `netd_row()`-class field must also state its headline
   classification/value inline in the Result section, not merely in Setup
   or Predictions" requirement would have caught this cycle's own gap for
   free. I flag this as a candidate addendum rather than a self-adopted
   rule, since ratifying new standing rules is Red Team's/the Director's
   call, not mine.

3. **File the six fresh `ratio_abs_ext_raw` points (this cycle's own free,
   previously-uncredited confirmation of T9's ~0.51 anchor at oblique
   R4-family incidence) as an explicit LOGBOOK citation under T9**, zero
   marginal cost, already computed and already in `results.json` — a
   positive, previously-untested generalization this cycle actually
   produced and should get credit for, distinct from and additional to
   the pooled cross-experiment `Δratio_abs_ext` check Tier 1 item 1(c)
   already reports.
