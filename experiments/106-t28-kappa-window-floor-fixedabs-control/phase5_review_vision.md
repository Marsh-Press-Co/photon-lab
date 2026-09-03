# Phase 5 Review — VISION SCIENCE (blind)

*Panel Iteration 83, exp-106. Fresh context. Charter: human perceptual
limits — contrast thresholds, luminance edge detection, spectral
sensitivity, adaptation, temporal sensitivity, saccadic/attentional
blindness. Central question: what would make a human eye FAIL to
register something physically present? Duty: pin numeric thresholds,
with sources, BEFORE any run that scores against them. This cycle
performs no such scoring (T1: N/A, instrument-extension only) — my job
is to police whether that scope boundary is honestly kept and whether
the disclaimer discipline (R23) holds, not to perform perceptual
scoring myself.*

## 0. Independent verification of R23's single-source-of-truth discipline

Read directly, not trusted from any docstring or prose claim:

- `run.py` line 194–200 defines a single module-level `DISCLAIMER`
  string constant, concatenating a hand-written prefix (the "no
  Weber-contrast or C_thr(L) perceptual scoring" sentence, extended
  this cycle with the Nyquist-margin-proxy clause naming "mandatory fix
  7") with `ts.netd_disposition(0.0, NETD_BAND_K)["disclaimer"]` — the
  NETD instrument-vs-human-eye sentence, sourced from
  `lab/thermo_sidecar.py` line 806–810, confirmed byte-identical to the
  string that constant returns.
- `build_predictions_text()` (line 363) embeds `{DISCLAIMER}` at line
  366; `main()` asserts `assert DISCLAIMER in predictions_text_` at
  line 509, **before** the first real FDTD call (after Gate P0, before
  any `Sim.run()`).
- `build_result_text()`-equivalent block (line 777) embeds
  `{DISCLAIMER}` at line 779; `main()` asserts `assert DISCLAIMER in
  result_text` at line 831, after all captures/gates are computed and
  before the function returns.
- Both assert sites reference the **same** `DISCLAIMER` object — this
  is genuinely a single source of truth, not two independently
  hand-typed copies that happen to currently agree. **This is the
  cleanest implementation of R23 this exact sub-thread has shipped**:
  exp-104 (R23's founding cycle) shipped only one working assert at
  execution time despite a docstring claiming two; exp-105 shipped a
  `RESULT_TEXT`-only assert, missing `PREDICTIONS_TEXT` (caught by my
  own seat's predecessor at that cycle's Phase 5, fixed same-shift).
  exp-106 is the first cycle in this lineage where a fresh, independent
  read of `run.py`'s own source confirms **both** asserts present,
  both wired to the identical string, on the first pass, with no
  Phase-5 catch required to complete the pair.
- I independently re-ran the check the task asked for rather than
  trusting the module docstring: `grep -c '"result_text"'` /
  `'"predictions_text"'` against the committed `results.json` confirms
  both fields are persisted, and a direct Python load confirms
  `"Raw physical intensity ratios" in result_text` and `in
  predictions_text` are **both `True`** — the disclaimer, including the
  "(mandatory fix 7)" Nyquist-margin-proxy clause and the full NETD
  sentence ("...does NOT bear on constraint-3/4's human-eye verdict
  (panel Iteration 20, VISION SCIENCE's mandatory fix, Red Team attack
  7)"), is present verbatim in both persisted strings, exactly as R23
  requires.

**But the committed `NOTES.md` document itself does not carry this
through symmetrically, and this is a genuine, independently-caught gap
this review is the first to name precisely.** I grepped the committed
`NOTES.md` (not `results.json`, not `run.py`) for the disclaimer's own
distinctive text (`"Raw physical intensity ratios"`, `"not a claim
about human visibility"`, `"NETD is an instrument"`):

- The **Predictions** section (NOTES.md lines 186–251) is an explicit,
  self-declared verbatim fenced-code-block reproduction of
  `build_predictions_text()`'s actual output ("Verbatim from
  `run.py::build_predictions_text()`... reproduced here for the record
  at freeze time") — and it genuinely is: the DISCLAIMER text appears
  in full at lines 188–195, matching `run.py`'s constant exactly,
  including the mandatory-fix-7 clause and the NETD sentence.
- The **Result** section (NOTES.md lines 341–459) — the section this
  program's own R21 rule holds to a higher bar than mere persistence,
  because it is "the prose a future citation will actually read" —
  **contains the disclaimer text nowhere.** I re-checked this three
  ways: a direct grep of the committed file (zero matches outside the
  Predictions block), a manual re-read of every paragraph in the
  Result section (Gate P0, reproduction checks, Items 1–4, the
  absolute-ratio test, the ledger check, the realizability note — none
  of these paragraphs reproduces or paraphrases the disclaimer), and a
  direct comparison against `run.py`'s own `result_text` f-string
  (line 777–830), which the Director's synthesis clearly draws its
  numbers from but does not quote verbatim as the Predictions section
  does.

**This is not a false claim and does not itself violate R23's own
text** (R23 is about code-level enforcement on `PREDICTIONS_TEXT`/
`RESULT_TEXT`, and that enforcement is genuinely, verifiably intact —
confirmed above). Nor is it unique to this cycle: I checked
`experiments/105-t28-kappa-scale-bridge/NOTES.md` for comparison and
found the identical pattern there too — its own Predictions section is
a paraphrased bullet list that does not literally quote its own
`DISCLAIMER` string at all (a *weaker* practice than this cycle's own
genuine verbatim block), and its own Result section likewise never
quotes the disclaimer text. So exp-106 is a **strict documentation
improvement** over exp-105 in the Predictions half, while carrying
forward the identical Result-side gap unremarked, now for a second
consecutive cycle. Read against this sub-thread's own R21 standard —
"a persisted post-run analytic sidecar field's own headline finding
must be stated inline in a cycle's own Result section, not merely
persisted to `results.json`... persistence alone is necessary but not
sufficient" — the disclaimer is exactly such a field: code-enforced,
persisted twice over (both `results.json` keys), yet absent from the
one prose section a future citation is likeliest to quote in
isolation. I am not filing this as a fresh R23/R21 firing (the
underlying discipline this cycle actually improved on, and no false
claim was made), but it is a real, previously-unnamed edge of exactly
the "R23 scope decision" item Iteration 82's own queue already flagged
as needing resolution ("genericize the assert to cover all
multi-section disclaimers... four of six seats independently flagged
this") — see §2 below.

## 1. Substantive assessment — is the constraint-3/4 scope boundary honestly kept?

Read the entire Result section paragraph by paragraph, watching
specifically for perceptual-sounding language creeping in around the
`REFUTES-electrical-thickness-growth-hypothesis` classification and the
12–18% ledger divergence.

**Item 4's classification language is clean.** `shape_ratio_fixedabs=
18.2283` is described purely in terms of two internal, program-specific
optical hypotheses — "geometric z/z_R window effect dominates" vs. "the
coating's own growing electrical thickness" — with zero words that
would read as a claim about what a human eye would or would not
register. The `NOT-TRUSTED` qualifier that `run.py` appends to the
classification string itself (`"REFUTES-electrical-thickness-growth-
hypothesis (NOT-TRUSTED -- r=312 MARGINAL/unsettled)"`, confirmed
verbatim in `results.json::item4_fixedabs.classification`) is likewise
scoped entirely to instrument trust (Nyquist tier, settling status),
never to perceptual detectability. Good discipline, matching
mandatory fix 3's own intent.

**The 12–18% ledger divergence is reported as a raw absorbed-power
fraction, never converted toward anything eye-relevant.** `|p_abs_fa −
p_abs_ss|/p_abs_ss = 0.1231` (r=156) / `0.1796` (r=312) is presented
honestly as exceeding the informal ~10% expectation named in the frozen
Predictions, disclosed as un-gated and un-adjudicated — no attempt is
made to translate it into a contrast, luminance, or visibility figure,
and none should be: this is a cross-family absorbed-power-fraction
comparison, several conceptual steps removed from anything my charter
scores. Correctly left alone.

**The NETD/instrument-threshold separation is moot but correctly moot.**
P5 (the thermal sidecar, the only channel that ever computes an actual
NETD classification) is explicitly not re-invoked this cycle — stated
three times (Setup, Idealizations, and implicitly by the DISCLAIMER's
own unconditional presence despite nothing NETD-shaped being computed).
Because no `netd_classification`/`dt_ss_full_K` value exists anywhere
in this cycle's `results.json`, there is nothing for a human-eye claim
to accidentally attach to. Carrying the NETD clause of the disclaimer
forward anyway (rather than dropping it because "nothing NETD-shaped
ran this cycle") is the *correct* conservative choice under this
sub-thread's own R16 precedent — a disclaimer travelling unconditionally
is necessary even when its named byproduct is absent this cycle, and
doing so here costs nothing and closes a door before it can be opened.

**`kappa_window`'s own ~1,100× collapse (exp-105's own headline, cited
here only for context) is never described in this cycle's Result
section using visibility-adjacent language** ("vanishes," "invisible,"
"undetectable to the eye," etc.) — every mention is scaled, qualified
numeric ratio talk (`shape_ratio`, `abs_ratio`, `kappa_window(r)`
values), consistent with exp-105's own VISION-authored ΔC≈0.018
scope-boundary note this cycle inherits unchanged. I independently
re-derived that inherited note's own arithmetic is still the relevant
context: `kappa_window` is a coherent on-axis transmission diagnostic,
not a Weber-contrast measurement, and nothing in this cycle's data
changes that structural separation.

**Verdict on scope-boundary honesty: kept, cleanly, throughout the
Result section's own substantive prose.** The one gap I found (§0,
above) is a *carrying-forward* gap in the disclaimer's own physical
presence in one section of the human-facing document, not a leak of
perceptual-sounding claims into the physics prose. These are
different failure modes, and only the first occurred here.

## 2. Gaps, inconsistencies, unstated risks — cited against LOGBOOK.md's R-rules

1. **The NOTES.md Result-section disclaimer-carry-forward gap (§0),
   named here for the first time precisely** — not yet a rule
   violation (R23's own text targets code-level `PREDICTIONS_TEXT`/
   `RESULT_TEXT` enforcement, which is genuinely intact), but it sits
   in exactly the conceptual gap R21 exists to name ("persistence alone
   is necessary but not sufficient... a document can pass R16's own
   test perfectly and still fail R21's"). I recommend the still-open
   "R23 scope decision" item on Iteration 82's own queue (deferred
   again by this cycle, per its own Idealizations — the Nyquist-proxy
   extension, mandatory fix 7, is a partial, not full, discharge of
   that queue item) be explicitly widened to ask: should NOTES.md's own
   Result section, not merely `run.py`'s generated `result_text`, also
   be required to reproduce the disclaimer verbatim, the same way its
   Predictions section already correctly does? This is now a
   **two-cycle-consistent** pattern (exp-105, exp-106) — not yet at any
   rule's own three-strike forward-elevating threshold (R16/R21's own
   convention), but worth naming explicitly before a third cycle makes
   it a pattern nobody named.

2. **R23's own founding-cycle scope limitation (exp-104: the code
   enforces only the perceptual DISCLAIMER, not the MATERIALS
   aliasing-origin sentence, the THERMO thermal-sidecar-N/A sentence,
   or the λ/scope-only idealization) is unchanged by this cycle** —
   exp-106 does not touch or extend that boundary, and does not claim
   to. Consistent with the standing Iteration-82 queue item, still
   unresolved, not this cycle's obligation to close.

3. **The Predictions-section fenced code block in NOTES.md is a
   faithful verbatim reproduction of `build_predictions_text()`'s
   actual template**, confirmed by direct side-by-side comparison
   against `run.py` lines 364–478 (item numbering, band thresholds,
   the `n≤3.0` vs. theory's `n≈1–2` disclosure from mandatory fix 6,
   and the realizability replacement text from mandatory fix 4 all
   match). No R4-class transcription defect found in this section —
   a genuine, positive finding worth stating plainly rather than only
   negative ones.

4. **Outside my own charter, but worth flagging since it touches
   disclaimer/scope discipline indirectly**: Item 4's own `REFUTES`
   classification is scored while the cross-family ledger's own
   informal ~10% expectation is exceeded (12.3%/18.0%) with no
   pre-registered gate to catch it, and while `shape_ratio_
   fixedabs_trusted=False` throughout (the r=312 settling leg for
   BOTH families was cost-deferred, not merely the self-similar one —
   confirmed in `results.json::settling_r312`, which the Result
   section's own Item 2 paragraph discloses honestly: "genuinely NOT
   RUN at r=312"). This is a PHOTONICS/MATERIALS/EM-shaped physics
   question, not a perceptual one, and I defer the substance to those
   seats — but I note it here because a REFUTE classification carrying
   this much disclosed uncertainty is exactly the kind of result a
   future citation could quote stripped of context if the Result
   section's own NOT-TRUSTED qualifier is ever paraphrased away — the
   same erosion shape my own charter exists to police, one level
   removed from perceptual language specifically.

5. **No new perceptual threshold, C_thr(L), or Weber-contrast claim
   appears anywhere in this cycle's record** — confirmed by a full
   read of `phase1_proposal.md`, all five Phase-2 critiques, the
   Red Team Phase-2 audit, and `NOTES.md` end to end. My charter's
   core duty this cycle ("pin numeric thresholds... BEFORE any run
   that scores against them") is vacuously satisfied: there is no run
   scoring against a perceptual threshold to pin one for. This matches
   the Phase-1 proposal's own T1:N/A framing and the Red Team Phase-2
   audit's own explicit ruling that constraint-3 is "out of scope for
   this entire T28 sub-thread by explicit, numbers-backed precedent,"
   not silently dropped (PANEL.md Checkpoint criterion 4's "especially
   #3" clause correctly does not fire).

## 3. Ranked top-3 candidate directions for Iteration 84 — VISION SCIENCE's own perspective

1. **Resolve the widened "R23 scope decision" explicitly, folding in
   this cycle's own new data point (§0/§2 item 1).** Iteration 82's
   queue already named this Tier-1; it has now been touched (partially,
   via mandatory fix 7's Nyquist-proxy clause) but not resolved twice
   running. A concrete, cheap fix: either (a) require every future
   T28 `NOTES.md`'s Result section to fenced-code-block-quote its own
   `result_text` the same way Predictions already does (mechanical,
   zero new machinery, closes the gap this review names for good), or
   (b) formally rule that NOTES.md's prose Result section is
   intentionally a non-verbatim synthesis and the disclaimer's true
   home is `results.json`/`run.py`'s own output — but state that
   ruling explicitly rather than leaving it an unnamed convention two
   cycles running.

2. **Complete the r=312 settling leg on `kappa_window` for both
   families** (the one Tier-1 item this cycle's own cost gate
   correctly, honestly deferred rather than silently dropped) — this
   is the single precondition standing between "REFUTES... (NOT-
   TRUSTED)" and an actual trusted verdict on this cycle's own
   falsifiable heart. Not primarily my charter's own question, but the
   disclaimer/scope-boundary discipline I police depends on downstream
   citations correctly carrying the NOT-TRUSTED qualifier until this
   runs — worth stating from this seat because a resolved, TRUSTED
   verdict removes one more place a future citation could accidentally
   drop a qualifier.

3. **Execute or formally retire the `delta_scene` R3-vs-R4 split**,
   now explicitly re-justified for a seventh deferral by this cycle's
   own Idealizations section, with Iteration 84 named as the hard
   deadline by this cycle's own text (echoing Iteration 51's own
   no-seventh-cycle precedent). I rank this third, not first, because
   it is not disclaimer/perceptual-adjacent — but it is the oldest
   unresolved item on the whole T28 board and this cycle's own record
   commits the program to a decision next cycle, in writing, which my
   seat has no basis to override.
