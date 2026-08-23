# exp-064 — Phase 2 Red Team Audit

**Panel Iteration 41. Seat 7, RED TEAM.** Receives everything: the Phase-1
proposal (QUANTUM OPTICS, lead by rotation) and all five blind Phase-2
critiques (PHOTONICS, MATERIALS, ELECTROMAGNETISM, THERMODYNAMICS, VISION
SCIENCE). Speaks last. Standard: not textbook-physics compliance —
speculation is permitted here anyway, since none is offered (T1 escape
route: N/A, correctly stated). What is judged: internal inconsistency,
unfalsifiable claims, mechanisms inexpressible as simulation parameters,
and quiet constraint violations — none of the constraint-1/2/3/4 kind
apply to a zero-FDTD code-architecture cycle, so this audit is,
overwhelmingly, a program-integrity/process audit, exactly as the task
brief anticipated.

Every numeric claim below that could be independently re-verified against
a primary repo artifact (not merely re-asserted from a seat's own
critique) was re-verified by direct file read: `lab/thermo_sidecar.py` in
full, `lab/validation/run_all.py` stage 23 (lines 2067–2132) and the
`_stage_selected` mechanics, `lab/caveat_lint_config.json` and
`lab/numeric_lint_config.json` in full, `LOGBOOK.md` Iterations 17 and
36–40 in full plus the T23 thread, `PLAN.md`'s current-state and
Iteration-41 queue block, and `experiments/061-.../phase4_results.md`'s
MP-2/MP-3/MP-5 sections directly (not MATERIALS' summary of them).

---

## Numbered attacks (most severe first)

**1. [inconsistency] — the guard's own central verification claim is not
enforced by any of its four proposed gates; EM's catch, independently
confirmed by direct source read.** `lab/validation/run_all.py` lines
2067–2132 (`stage23_front_surface_biot_correction`) contains real,
currently-committed calls to `front_surface_conduction_correction` at
`L_MP5_730X_M = 1051.2e-6` — exactly the witness-scale, extinction-derived
length T23 forbids in a conduction role. QP-3 commits Phase 3 to retagging
these calls `extinction_derived_diagnostic_only` / `diagnostic_only=True`.
But §4's four stage-24 gates, read literally, only ever construct their
own fresh calls inside `run_all.py`'s new stage-24 function body — none of
them read `inspect.getsource`, AST-parse, or text-scan stage 23's *actual*
source lines to confirm what tag Phase 3 really wrote there. A Phase-3
author could tag the three real `L_MP5_730X_M` sites
`"bench_construction"` — a false, syntactically well-formed declaration —
and gates 1–4 as specified would still all pass green, because none of
them inspect that file at those lines. §0 claims this guard "resolves T23
permanently and structurally... any future call, with any future
material, is protected" — a claim the gate suite as written cannot verify
even for the three call sites that exist *today* and motivated the entire
cycle. This is not a hypothetical: it is the identical shape — a rule
stated in a document, enforced by Phase-3 author discipline rather than by
a gate that reads the committed artifact — that has fired Checkpoint
criterion 4 six times across five iterations (17, 36, 37, 38, 39×2) in
this program's own record. Shipped as specified, exp-064 would build an
"enforced" guard that is not actually enforced against the one call site
that matters — recreating T23's own multi-cycle failure pattern one level
up, inside the very mechanism built to end it.

**2. [inconsistency] — §6's headline number contradicts this program's own
already-established record; MATERIALS' catch, independently confirmed by
direct read of `experiments/061-.../phase4_results.md`.** MP-2 is
CONFIRMED (phase4_results.md lines 138–169) against three corroborated
real CNT-forest/Vantablack thicknesses at the visible band: 300–500µm
("Optical reflection and absorption of carbon nanotube forest films on
substrates"), 100–300µm (Surrey NanoSystems VBx2 datasheet), and a
weakly-sourced ~250µm (S-VIS). MP-5's own witness-need table (lines
299–335) computes the exact figures exp-064 §6 cites as "the witness-scale
need" — 332µm and 1056µm are two of MP-5's own six derived rows. Comparing
MP-5's own witness-need range (332–1056µm) against MP-2's own already-
CONFIRMED sourced thickness range (100–500µm) — the correct comparator,
since both are this program's own already-scored numbers — gives a gap of
roughly **1×–10.5×** (1056/100), not the "24×–75×" §6 computes against an
uncited "up to 14 micrometers" figure. That figure carries no citation
anywhere in this document, unlike every other numeric claim in §6 and
unlike every row of MP-2's own sourced table — and is very plausibly the
SAME `<20µm`, mid-IR, "randomly-modulated MWCNT forest" outlier MP-2
itself already found, named, and explicitly excluded from the record-
blackness comparison class (phase4_results.md line 149, and lines 157–159:
"not a like-for-like near-total-blackness comparator"). Filing §6 as
written risks seeding `LOGBOOK.md`'s persistent memory with a materially
wrong realizability number — a direct instance of the failure this
program's own R4 rule (check a number against the existing record before
citing it as new) exists to prevent. MATERIALS' critique is CONFIRMED
CORRECT by independent re-derivation, not merely trusted.

**3. [unfalsifiable] — even a corrected §6 rests on an undisclosed
physical equivalence; PHOTONICS' catch, layered on attack 2.** Both the
proposal's own "24×–75×" framing and the corrected "~1×–10.5×" framing
silently equate forest HEIGHT with the single-pass Beer-Lambert absorption
path length needed to reach τ_true. That equivalence requires ballistic,
normal-incidence propagation through a homogeneous effective medium. A
real CNT forest is a dilute (~1–10% fill), vertically-aligned, multiply-
scattering mat — it is black *because* it scatters and traps light
diffusively, so the true absorption path for a given physical height need
not equal that height. Separately: the target phenomenon is a swept,
generally oblique beam (constraint 4) — even in the pure-ballistic limit
the geometric path is `h/cosθ`, which alone can move the ratio either
direction depending on θ and front-surface `R(θ)`. As stated, §6 offers no
falsification condition and no idealization sentence bounding this — it
reads as a settled geometric-realizability finding when it is an
angle/transport-idealization-laden estimate of unstated direction.

**4. [inconsistency] — the guard's own edit touches lines that already
carry unprotected caveat strings; VISION's catch, confirmed by direct
read of `lab/thermo_sidecar.py`.** `mixed_length_scale_regime` (lines
229–290) and `front_surface_conduction_correction` (lines 313–387) both
already return dicts carrying hand-written string caveats —
`netd_disclaimer` (both functions, verbatim, lines 284–289 and 381–386),
`model_note`, `material_provenance`, `mass_fill_fraction_assumption`,
`idealization_note`. Implementing §3/§4 means hand-editing these same dict
literals to add `length_provenance`/`diagnostic_only`. None of the four
proposed stage-24 gates check that the pre-existing keys survive that edit
unchanged — gate 3 ("diagnostic-path identity") reads back only the two
NEW keys. This exact caveat-string-loss class has already happened twice
in this program's history on this exact caveat (Iteration 17/T3: dropped
from a per-point return; Iteration 40 mandatory fix 2: dropped from a
results table) — a live, disclosed, currently-unguarded risk sitting
precisely on the lines this cycle's own diff will touch.

**5. [inconsistency, non-blocking — flagged, not live] — the allow-list
checks provenance-TIER, not provenance-ROLE; EM's secondary point,
independently checked.** `_validate_length_provenance` only matches the
declared string against the allow-list; it does not and cannot check that
the underlying float is actually "of the modeled solid body" per
`gas_conduction_h_eff`'s own docstring. A future honestly-measured
gap/standoff or aperture length would pass the identical
`bench_construction`/`measured_geometric` tag while feeding a physically
different conduction regime into the same formula. Checked directly: no
current or proposed call site today is anything but `r_out`-class or the
MP-5 extinction-derived `L` — this is a structural blind spot, not a live
violation, correctly comparable in kind to Idealization 1's own
"declaration, not detection" admission. Non-blocking.

**6. [unfalsifiable-adjacent, real gap] — a green diagnostic-path PASS
cannot be distinguished from a validated-buildability claim;
THERMODYNAMICS' catch.** `diagnostic_only=True` still returns a full,
numerically complete dict (h_eff, mass, area, correction_factor) with no
field distinguishing "provenance correctly flagged as unlicensed" from
"the physical object this describes may not exist at any provenance tag."
Given §6's own flagged (even before attack 2's correction) order-of-
magnitude gap on whether a real forest of the needed thickness has ever
been grown, and given that TD-5 (exp-063) carries this program's thinnest-
ever safety margin (7.8×) and was explicitly billed as a "first-ever
thermal-detectability classification flip" candidate — precisely the
framing under which a reader is likeliest to misread instrument-DETECTABLE
as eye-visible, or a green code gate as an endorsement of physical realism
— a future caller reading stage-24's diagnostic-path PASS could reasonably
conflate "correctly labeled" with "physically real." I judge this
load-bearing enough to require a fix before freeze (see docket below), not
merely queue it: it is the same *kind* of ambiguity ("gates clean" read as
"more than gates clean") that this program's own Iteration-17 close
diagnosed as its recurring lesson — necessary, not sufficient.

**7. [inconsistency, non-blocking — flagged, not live] — `measured_
geometric` does not enforce material-identity coherence; MATERIALS'
secondary point.** A `measured_geometric` length from one CNT-forest
process class (e.g. densified/drawn-sheet) could sit, unflagged, beside a
`bench_construction` or diagnostic length from a different class (e.g.
as-grown bulk-aggregate) in the same sidecar call, with no cross-check
that they describe one candidate identity — exactly the classes exp-063
itself kept separate. Correctly named by the proposal's own Idealization 2
as future scope; not blocking this cycle.

**8. [process, cosmetic] — the new registry entry's `candidate_globs` is
left unstated.** §3's `exp064-length-provenance-disclosure` entry does not
specify `candidate_globs`, falling back to the program-wide default
(already widened at Iterations 39/40 to `experiments/*/phase*.md`), which
is adequate — VISION confirmed no Checkpoint-4-relevant risk is visible.
Recommend one added sentence stating this explicitly rather than leaving
correctness implicit in a reader's knowledge of `caveat_lint.py`'s own
default. Non-blocking.

---

## The load-bearing question, answered directly

**Does EM's catch (attack 1), on its own, mean this proposal is currently
written in a way that risks recreating T23's own multi-cycle failure
pattern one level up?** Yes, unambiguously, if shipped exactly as
specified in §3/§4. The whole reason this cycle exists is that a *prose*
rule (`gas_conduction_h_eff`'s docstring) went unenforced for three
cycles because nothing checked it against the actual call sites using it.
A *code* rule that checks its own abstract behavior but never checks the
actual call sites using it is the same defect wearing different clothes —
arguably a worse one, because a green trust-suite stage now carries more
apparent authority than a docstring ever did, and a future reader has
*less* reason to go re-check by hand a thing the suite already claims to
gate. This is exactly the "disclosure nothing checks" shape PANEL.md's own
Checkpoint criterion 4 exists to catch, transplanted from documents into
code. It is fixable — EM's own proposed fifth gate (attack 1's remedy,
below) closes it completely and cheaply, reusing the exact
`numeric_lint.py`/`derivation_consistency` idiom this program already
built at Iteration 40 for the textually identical problem shape
(`exp063-cf-bench-vs-witness-derivation`). The defect is in what this
cycle currently proposes to ship, not in what it is trying to do.

---

## Checkpoint-criteria ruling, explicit, all five

**Does ANY Checkpoint criterion fire at this stage?** No. Reasoning,
criterion by criterion:

- **Criterion 1** (a configuration passes all constraint metrics): does
  not fire — this cycle scores zero constraint-1/2/3/4 metric by design
  (T1 escape route N/A, correctly stated in §0/§2). Not applicable to a
  code-architecture cycle.
- **Criterion 2** (a proven boundary, gates clean): does not fire —
  nothing here maps a constraint-subset boundary; this is instrument
  trust, not a mechanism-class finding.
- **Criterion 3** (engine physics beyond validated classes): does not
  fire — zero FDTD, a pure analytic/code-architecture module, the
  exp-054/060/061/062/063 class this program has repeatedly confirmed
  does not require Marsh's convening.
- **Criterion 4** (Red Team flags program-integrity drift): **does not
  fire yet, and should not.** This is a Phase-2 critique of a Phase-1
  *proposal* — nothing has been committed, no gate has been built, no
  call site has been mistagged in a shipped artifact. Every prior
  Checkpoint-4 firing in this program's record (Iterations 17, 36, 37,
  38's non-firing, 39×2, 40) fired against a completed Phase-3/4/5
  artifact — a caveat that actually went missing from a committed
  document, a registry entry that actually failed to discover a real
  file, a docstring that actually shipped stale. Iteration 37's own
  standing language is explicit that the trigger is a defect
  "surviving into THIS cycle's own published Phase-3/5 artifact" — Phase
  1/2 catches followed by Phase-3 fixes are the *designed* mechanism, not
  a violation of it. Attacks 1–4 above are exactly what Phase 2 exists to
  surface before Phase 3 freezes; catching them here, before any code
  lands, is the process working as intended, not drifting. **This
  audit sets one explicit forward tripwire, binding on Iteration 41's own
  Phase 3 and beyond**: if Phase 3 ships stage 24 WITHOUT attack 1's
  fifth-gate remedy (or a materially equivalent code-level check on
  `run_all.py`'s actual committed source), and a future cycle
  subsequently finds a real witness-scale call site mistagged
  `bench_construction`/`measured_geometric` underneath a green stage-24
  suite, that is to be treated as a program-integrity finding for Red
  Team's own ruling at the cycle that finds it — no further deliberation
  required, mirroring the disposition this program has already applied to
  the `exp061-t18-evidentiary-tier-propagation` and `exp063-thermo-
  disposition-netd-disclaimer` lineages.
- **Criterion 5** (two consecutive non-advancing iterations): does not
  fire — Iteration 40 advanced the logbook with a genuine, independently
  re-derived result (κ_CNT-forest sourced for the first time); this cycle
  is mid-process, not yet closed, and is on track to advance it further
  once the mandatory-fix docket below lands.

**Summary: none of the five Checkpoint criteria apply at this Phase-2
stage.** The severity of attack 1 is real and load-bearing for Phase 3,
but severity-of-a-critique-finding and Checkpoint-firing are not the same
thing — PANEL.md's own Phase 2→3 mechanism (critique, then mandatory
fixes, then freeze) is precisely how this program is supposed to catch
exactly this class of defect before it becomes a program-integrity
finding, not after.

---

## Verdict: **PROCEED-WITH-MANDATORY-FIXES**

Matching this program's own overwhelming precedent (every Phase-2 Red
Team audit since Iteration 17 has landed here whenever the underlying
design was sound and the defects were fixable pre-freeze, which is the
case here: the allow-list/keyword-only/absolute-identity architecture in
§§3–4 is independently endorsed, on independent grounds, by all five blind
seats and by this audit — the defects found are in completeness and in
one uncited fact, not in the core design). The `length_provenance` guard
architecture should ship. It must not ship as currently specified.

## Mandatory-fix docket for Phase 3, ranked

**Blocking — must land before any code freezes or any prediction is
scored as closing T23:**

1. **[EM's fifth gate, attack 1]** Add a stage-24 gate (or a
   `numeric_lint_config.json` `derivation_consistency`-style entry,
   mirroring `exp063-cf-bench-vs-witness-derivation`'s own already-
   established pattern) that inspects `run_all.py`'s actual committed
   source — via `inspect.getsource` or a direct text scan, not by
   re-invoking the guarded functions in isolation — and FAILs unless
   every real `L_MP5_730X_M`-class witness-scale call site literally
   passes `length_provenance="extinction_derived_diagnostic_only"` and
   `diagnostic_only=True` in the committed file. Without this, QP-3 — the
   one prediction this cycle exists to make binding — is enforced by
   Phase-3 author discipline, not code, which is the exact failure shape
   T23 already spent three cycles proving unreliable in this program.
   This is the cycle's single most important deliverable; everything
   else in this docket is secondary to it.

2. **[§6 correction, attack 2 + attack 3]** Before Phase 3 lands: either
   (a) reconcile the uncited "~14µm" figure against MP-2/MP-5's own
   already-CONFIRMED, sourced 100–500µm real-forest-thickness record and
   MP-5's own 332–1056µm witness-need figures, rewriting §6 to the
   already-established ~1×–10.5× gap (not "24×–75×"), explicitly labeled
   a restatement of an existing PARTIAL finding, not a new one; or (b)
   strike §6 entirely and let the standing #3 PLAN.md queue item (pin
   pitch/diameter + κ together) carry the thickness question forward
   undisturbed. Whichever path is taken, if any form of §6 survives into
   the committed record, it must also carry PHOTONICS' one-sentence
   idealization disclosure (forest-height ≠ single-pass Beer-Lambert path
   length; not corrected for oblique incidence or diffusive/scattering
   transport) — a zero-code-change, zero-gate-change fix.

3. **[VISION's fifth gate, attack 4]** Add a stage-24 caveat-string-
   identity gate: for both `mixed_length_scale_regime` and
   `front_surface_conduction_correction`, assert every key present in the
   function's PRE-existing return dict (read from the currently-committed
   source, e.g. via a frozen golden-key-set fixture or `ast` inspection)
   is present, with an identical string value, in the post-guard return
   dict for at least one licensed (`bench_construction`) call. Closes the
   exact caveat-string-loss class this program has already paid for twice
   (Iterations 17, 40) on these exact strings.

4. **[THERMODYNAMICS' buildability-vs-provenance distinction, attack 6]**
   Judged load-bearing enough to require before freeze, not merely
   queued: give the `diagnostic_only=True` return path an explicit signal
   that a green call answers a provenance-honesty question, not a
   buildability question — either (a) add a `geometric_realizability`
   field to the diagnostic return dict, distinct from `length_provenance`,
   that a future caller must also read and disclose; or (b), the cheaper
   option THERMODYNAMICS itself names and QP-3 already leaves open, remove
   the three witness-scale calls from stage 23/24's own gated regression
   path entirely, replacing them with an explicitly-labeled, non-
   regression diagnostic script outside the trust-suite's PASS/FAIL
   surface. Either closes the risk that a green stage-24 diagnostic-path
   PASS is later cited as validating TD-5's own witness-scale margin as a
   real, buildable finding rather than as correctly-labeled arithmetic on
   an as-yet-ungrounded length.

**Non-blocking, recommended but not required before this cycle's freeze:**

5. EM's provenance-ROLE structural note (attack 5) — no live violation
   today; correctly deferred as future scope per the proposal's own
   Idealization 2.
6. MATERIALS' material-identity-coherence gap on `measured_geometric`
   (attack 7) — correctly named by the proposal's own Idealization 2 as
   future scope, not this cycle's job.
7. VISION's one-sentence `candidate_globs` disclosure for the new
   registry entry (attack 8) — cosmetic; apply if convenient.

---

*RED TEAM, Panel Iteration 41, Phase-2 audit of exp-064. Every seat's
critique read; independent re-verification performed against primary repo
artifacts (`lab/thermo_sidecar.py`, `lab/validation/run_all.py`,
`lab/caveat_lint_config.json`, `lab/numeric_lint_config.json`,
`experiments/061-.../phase4_results.md`, `LOGBOOK.md`, `PLAN.md`) before
any attack above was accepted as confirmed rather than merely relayed.*
