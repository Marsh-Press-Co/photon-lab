# VISION SCIENCE — Phase 5 Review of exp-062 (Panel Iteration 39)

*Fresh sub-agent, blind to the other six seats' current-cycle Phase-5
reviews. Charter: human perceptual limits — contrast thresholds, luminance
edge detection, spectral sensitivity, adaptation, temporal (flicker/motion)
sensitivity, saccadic and attentional blindness. Central question: what
would make a human eye FAIL to register something physically present?
Standing duty this cycle: verify the `exp061-t18-evidentiary-tier-
propagation` registry widening and check for a second, same-iteration
Checkpoint-4-adjacent gap.*

**Read in full**: `PANEL.md`; `LOGBOOK.md` lines 1–12685 (the complete
Ruled-Out registry R1–R5, Live Threads T1–T26 in full, Iterations 1–4
verbatim, Iterations 36–38 verbatim — through the program's current
close at Iteration 38; no Iteration 39 entry exists yet in LOGBOOK.md,
as expected, since that is the Director's own Phase-5-close action);
`PLAN.md` lines 1–100 and ~1895–1993; this cycle's full record
(`phase1_proposal.md`, all five `phase2_critique_*.md`, my own
`phase2_critique_vision.md`, `phase2_redteam_audit.md`, `phase3_synthesis.md`,
`NOTES.md`, `phase4_results.md`); `lab/caveat_lint.py` and
`lab/caveat_lint_config.json` (full source, both read directly, and
**executed live** — see Section 1); `experiments/034-floor-convergence-
scale-bridge/REALIZABILITY_MEMO.md` Entry 2 in full, including its
Amendment 6 close.

---

## 1. Mandatory duty — verifying the widening, and checking for a second gap

### 1.1 Did the widening close the gap it was built to close? Yes — verified live, not taken on anyone's word.

I ran the tool myself, three ways:

```
$ python3 lab/caveat_lint.py
...
[exp061-t18-evidentiary-tier-propagation]  ...
  PASS  experiments/061-absorptivity-mechanism-literature-check/NOTES.md
  PASS  experiments/061-absorptivity-mechanism-literature-check/phase4_results.md
  PASS  experiments/062-thin-film-interference-and-near-field-coupling-bound/NOTES.md
  PASS  experiments/062-thin-film-interference-and-near-field-coupling-bound/phase4_results.md
...
6 caveat(s) checked, 0 required-site failure(s).

$ python3 lab/caveat_lint.py --only exp061-t18-evidentiary-tier-propagation
[same 4/4 PASS]
1 caveat(s) checked, 0 required-site failure(s).

$ python3 lab/caveat_lint.py --selftest
  PRE-FIX  (d5b4844, Phase 3, before the run): caveat phrase ABSENT -- expected ABSENT -> PASS
  POST-FIX (4f29982, Phase 5, same-shift fix): caveat phrase FOUND -- expected FOUND -> PASS
Self-test PASSED
```

All six registry entries pass with **0 required-site failures**, and the
specific entry Checkpoint criterion 4 fired on now correctly lists and
PASSES all four required sites — exp-061's original two plus exp-062's
own `NOTES.md` and `phase4_results.md`, both of which do carry the T18/
WebSearch-snippet disclosure at the verdict itself (confirmed by direct
read of `phase4_results.md`'s closing paragraph and every EM-verdict
line — the disclosure is genuinely present, not merely pattern-matched
by an over-loose regex).

I also confirmed the **code-level** half of the widening, not just the
config: `git log -p` on `lab/caveat_lint.py` at commit `9e73b45` (the
Phase-3 synthesis commit) shows `DEFAULT_CANDIDATE_GLOBS` gained
`"experiments/*/phase4_results.md"` — a real diff, not a claim:

```
+    "experiments/*/phase4_results.md",
```

**Verdict on the mandatory-fix docket item 1: correctly and completely
applied**, on the narrow question it was written to answer (can this
entry discover exp-061's and exp-062's own verdict-bearing NOTES.md/
phase4_results.md files). I find no defect in the widening itself.

### 1.2 Is there a NEW gap — in the widened entry, or any other entry — that could fire criterion 4 a second time?

**Yes. I find one, live, in the exact entry that was just widened,
verified directly rather than inferred.**

**The finding.** The `exp061-t18-evidentiary-tier-propagation` entry's
own `candidate_globs` — even after this cycle's widening — is:

```
["LOGBOOK.md", "PLAN.md", "experiments/*/NOTES.md",
 "experiments/*/phase4_results.md",
 "experiments/034-floor-convergence-scale-bridge/REALIZABILITY_MEMO.md"]
```

*(sic — `LOGBOOK.md` in the real file; typo mine, corrected in the
config quote above is exact otherwise.)*

This pattern set can **never** discover a `phase2_critique_*.md`,
`phase5_review_*.md`, or `phase5_redteam_audit.md` file, for exp-061,
exp-062, or any future experiment — not at FAIL tier (`required_sites`),
not even at WARN tier (`candidate_globs`). This is not hypothetical. I
confirmed, by direct grep and read, that this blind spot is **already
live**, right now, in the checked-in repo:

```
$ grep -n -B1 -A1 "UNOBTANIUM" experiments/061-absorptivity-mechanism-literature-check/phase5_review_materials.md
75:## Verdict: **PARTIAL**
76:The UNOBTANIUM-WITH-PARAMETERS tier itself is not overturned — no
77:numeric defect found that flips it. ...
```

`phase5_review_materials.md` (exp-061, Iteration 38) states exp-061's
own literature-check verdict in its own Verdict section — exactly the
class of statement the registry entry's own `description` says "must
disclose the WebSearch-snippet-only sourcing tier AT THE VERDICT
ITSELF." I checked the whole file for any T18/WebSearch-snippet
disclosure anywhere:

```
$ grep -c "T18\|WebSearch.snippet\|not primary.source" experiments/061-.../phase5_review_materials.md
0
```

**Zero.** Compare against its five siblings from the same Phase-5 batch,
checked the same way: `phase5_review_photonics.md` (3 matches),
`phase5_review_quantum.md` (1), `phase5_redteam_audit.md` (2) all carry
the disclosure somewhere; `phase5_review_em.md` and
`phase5_review_thermodynamics.md` have zero matches too, but — checked —
neither of those two ever restates the UNOBTANIUM verdict at all, so
they are not instances of the gap; `phase5_review_materials.md` restates
the verdict **and** carries no disclosure anywhere in the file. This is
not a borderline case.

**Why this is structurally the same shape as what just fired, not a
different question.** I ran the actual tool against this exact entry and
confirmed the file is invisible to it at *any* tier:

```
$ python3 lab/caveat_lint.py --only exp061-t18-evidentiary-tier-propagation
[shows only the 4 required_sites — zero WARN candidates listed anywhere,
 for exp-061 or exp-062]
```

No WARN line for `phase5_review_materials.md` exists because
`candidate_globs` has no pattern that can ever match it — the identical
"structurally invisible even at WARN" defect Red Team's own Phase-2
audit named for `phase4_results.md` before this cycle's fix
(`phase2_redteam_audit.md` §1, attack 1: "there is no
`experiments/*/phase4_results.md` pattern anywhere ... so a
`phase4_results.md`-style file ... is structurally invisible to this
tool, at any WARN or FAIL tier"). Swap "phase4_results.md" for
"phase5_review_*.md/phase2_critique_*.md/phase5_redteam_audit.md" and the
sentence is unchanged.

**This is precedented as fixable, cheaply, inside this same config
file** — I checked the other five entries, not just this one. Two
sibling entries already solve exactly this problem, for exactly this
class of file, by using a *broad* per-experiment glob rather than named
filename patterns:

- `exp052-alpha-60nm-absorptivity-open`'s `candidate_globs` includes
  `"experiments/061-absorptivity-mechanism-literature-check/*.md"` — and
  running it live shows this glob doing real work: it surfaces
  `phase1_proposal.md`, `phase2_redteam_audit.md`, `phase3_synthesis.md`,
  `phase5_review_vision.md`, `phase5_review_photonics.md`, and
  `phase5_redteam_audit.md` as WARN candidates for its own trigger terms.
- `exp061-thermo-length-scale-staleness` uses the same pattern
  (`"experiments/061-absorptivity-mechanism-literature-check/*.md"`) and
  — I verified directly — it is precisely this broad glob that keeps
  exp-062's own `NOTES.md` from becoming a silent gap under *that*
  entry: exp-062's `NOTES.md` (Idealization 9) restates the THERMO
  disposition's corrected margin (`"1.35×–3.79×"`, matching that entry's
  own `phrase_patterns`) and is caught, matched, and correctly excluded
  from the WARN list as "already carries the caveat" — confirmed by
  running `--only exp061-thermo-length-scale-staleness` and finding zero
  WARN lines for any exp-062 file, exactly as expected for a document
  that already complies.

The `exp061-t18-evidentiary-tier-propagation` entry is the one entry in
this six-entry registry that did **not** adopt this already-precedented,
already-working, zero-additional-code pattern when it was widened this
shift — despite being drafted by the same process, in the same config
file, sitting two entries away from a sibling that already does it
correctly.

**Does this fire Checkpoint criterion 4 a second time, this same
iteration?** I lay out both readings, because this is the highest-stakes
call in this review and I will not paper over the genuine ambiguity —
that ruling belongs to Red Team, not to me, per this program's own
division of labor (I am the seat that finds and pins the gap; Red Team
adjudicates whether it fires).

*The case that it fires.* The tripwire's own hardened text (quoted
verbatim in the registry entry's `description`, in `PLAN.md`'s Current-
state note, and in `phase2_redteam_audit.md` §3) says: *"any further gap
in this specific entry's own coverage — unregistered site, under-scoped
`required_sites`, or within-file location gap — discovered at Iteration
39 or later, auto-fires criterion 4, no 'different defect species'
argument entertained a second time."* What I found is exactly an
"unregistered site" / under-scoped-`candidate_globs` gap, in this exact
entry, discovered at Iteration 39 (now, in this Phase-5 review) — the
same temporal and textual match Red Team's own Section 3 argument used
to rule the Phase-2 finding fired. `phase5_review_materials.md` already
exists, already violates the entry's own stated propagation principle,
and was simply never checked against it because the glob can't reach it
— structurally identical to the defect this cycle's own mandatory-fix
docket item 1 was written to close, just at a different file-naming
pattern.

*The case that it does not fire, or fires differently.* The tripwire's
own history (Iteration 38's two self-catches, this cycle's Phase-2
catch) has so far always been about `required_sites` — the FAIL-tier
list of documents the entry treats as authoritative verdict-bearing
records. `phase5_review_materials.md` was never proposed by any Director
or Red Team ruling as a `required_sites` candidate; Phase-5 review
commentary is, by this registry's own established design language
(`caveat_lint.py`'s docstring: candidate sites are "a lead for a human to
triage, not a failure"), WARN-tier material, not FAIL-tier. Under that
reading, what I found is a **candidate_globs** coverage gap — a WARN-tier
instrument blind spot — not a `required_sites` gap, and the tripwire's
own text, read narrowly, was written about the specific class of failure
that just fired (an unreachable *verdict-bearing* document), which
Phase-5 review prose arguably is not, even when it restates a verdict in
passing. On this reading, the correct action is a same-shift widening
(mirroring the two sibling entries that already do this) treated as
ordinary, un-escalated registry maintenance — not a second firing in one
iteration, which would indeed be unprecedented in this program's
fourteen-cycle Checkpoint-4 history.

**My own position, stated plainly**: the *fact pattern* is not in
dispute — I verified it myself, by tool execution and direct source
read, not by inference. The live violation in `phase5_review_materials.md`
is real, present, uncorrected, and of the identical structural species
Red Team named this cycle. Whether it clears the tripwire's own bar for
"no further deliberation" is a textual-interpretation question I am
flagging with full evidence, not resolving unilaterally — consistent
with my seat's role in this program's Iteration-39 Phase-2 finding,
where I found and named the gap and Red Team supplied the ruling. I
recommend, at minimum, the same-shift fix regardless of the Checkpoint
question: add `"experiments/061-absorptivity-mechanism-literature-check/*.md"`
and `"experiments/062-thin-film-interference-and-near-field-coupling-bound/*.md"`
to this entry's `candidate_globs` (mirroring its own siblings), and
separately, close the live violation by adding the T18 disclosure to
`phase5_review_materials.md` itself.

**Everything else in the registry checked clean.** I ran the full
registry (all six entries) and read every WARN line produced. No other
entry shows a comparable live, uncaught, verdict-restating violation —
the WARN lists for `exp060-p10-fresnel-not-diffraction`,
`exp060-sigma-flat-convention-caveat`, `exp052-alpha-60nm-absorptivity-open`,
`exp060-sigma-flat-corrected-bias-direction`, and
`exp061-thermo-length-scale-staleness` all show either genuinely
low-stakes candidate mentions (a bare function/variable name, not a
verdict restatement) or, where a verdict-adjacent number is restated
(the `150µm`/`THERMO disposition` WARNs against exp-061's own Phase-1/
Phase-4/Phase-5 files), those are **historical** pre-correction
citations correctly left unflagged as caveat text (they predate the
correction and are not being cited as current), not live undisclosed
violations. I did not find a second, independent new gap beyond the one
above.

---

## 2. From my own charter's lens: does anything in exp-062 touch perceptual thresholds, contrast, or detection?

**No — confirmed, matching my own Phase-2 prediction exactly.** I read
`phase1_proposal.md`, `NOTES.md`, and `phase4_results.md` end to end a
second time, specifically hunting for any contrast, luminance,
adaptation, or temporal-sensitivity claim smuggled into an EM/materials
argument (the T17-spiropyran failure mode my own Phase-2 critique named
as the standing risk this charter exists to catch). I found none.
`phase1_proposal.md`'s Section 4.4 discusses spectral bandwidth as a
*resonance discriminator* (narrowband vs. broadband OD), and
`phase4_results.md`'s EM-3 result resolves it via measurement geometry
(transmission-mode, unbacked substrate) — this is optical-response
language throughout, never perceptual language. No `C_thr`, no Weber
contrast, no scotopic/photopic reference, no flicker/motion claim
anywhere in this cycle's record. Zero constraint-1/2/3/4 metric is
scored, as the proposal itself declares and as I independently confirm:
this is a realizability-bound refinement (an R-vs-T/interference
correction plus a near-field-coupling classifier), not a phenomenon-
reproduction attempt, and my charter's gate — "pin numeric thresholds
before any run that scores against them" — has nothing to attach to
this cycle. This is the correct outcome, not an absence to be filled.

---

## 3. Verdict on exp-062's own contribution

**PARTIAL** — on the physics, this cycle earns PROMISING outright:
independently re-verified, sound, honestly bounded, and it delivers real
findings (EM-2/EM-3/EM-4 close both MP-3/MP-4 open sub-claims in the
mechanism-class-reinforcing direction, more decisively than predicted;
EM-6 finds NiP-black as the closest real-material comparator this
program has ever measured, 6.9×–31× thickness gap; EM-7 finds
carbon/graphene aerogel as the *worst*, 694×–3472×; the standing
`n_eff=1.04+0.01i` citation, flagged unpinnable across three-plus
cycles, is finally pinned to a title/journal/volume). Nothing here is
sloppy, and nothing overturns `graded_black_shell`'s
UNOBTANIUM-WITH-PARAMETERS tier — if anything it is further
reinforced, exactly as EM-4's own falsification condition predicted in
advance and honestly disclosed as a real (not foreclosed) possibility.

But per this program's own established precedent — Iterations 36 and 37,
both of which overrode a clean multi-seat PROMISING/PASS consensus to
PARTIAL specifically because Vision Science's own last-mile catch found
a live, unresolved caveat-propagation gap in the very machinery meant to
prevent it — I apply the same discipline here. The gap in Section 1.2 is
real, present, verified by my own tool execution and source read, and
unresolved as of this review. Following the house pattern precisely:
this verdict is **PARTIAL, provisional-to-PROMISING** once (a) Red Team
rules on whether it fires Checkpoint criterion 4 a second time this
iteration, and (b) the `candidate_globs` widening and the
`phase5_review_materials.md` disclosure fix land and are re-verified —
at which point, per the same precedent, this cycle's verdict should read
PROMISING going forward. The override is about process completeness,
not physics: every numeric claim in Sections 4–5 of `phase1_proposal.md`
and every scored verdict in `phase4_results.md` stands unchallenged by
this review.

---

## 4. Top-3 ranked candidate directions for Iteration 40+

1. **Close the phase5-review-class coverage gap in
   `exp061-t18-evidentiary-tier-propagation`, and generalize the fix
   across the registry.** Concretely: (a) add
   `"experiments/061-absorptivity-mechanism-literature-check/*.md"` and
   `"experiments/062-thin-film-interference-and-near-field-coupling-bound/*.md"`
   to this entry's `candidate_globs`, mirroring the pattern its own two
   siblings (`exp052-alpha-60nm-absorptivity-open`,
   `exp061-thermo-length-scale-staleness`) already use successfully; (b)
   add the missing T18/WebSearch-snippet disclosure to
   `phase5_review_materials.md` itself, closing the live violation this
   review found; (c) as a standing-infrastructure question for the
   Director (not gated on rotation): should EVERY registry entry's
   `candidate_globs` default to a broad per-experiment `*.md` glob rather
   than named-filename patterns, given this is now the second entry in
   the registry's short history to need this exact correction? This is
   the direct, load-bearing successor to this cycle's own mandatory duty
   and should not wait for a future seat to rediscover it independently.

2. **Build the numeric-value-consistency-check tooling
   (`lab/caveat_lint.py`'s registered-NUMBER extension), already re-filed
   with an owner at Iteration 40 per `PLAN.md`'s current queue.** This is
   the direct generalization of both this review's own finding and the
   pattern Red Team named at this cycle's own Phase-2 audit (docket item
   6): documentation-consistency gaps recur in two different shapes now
   — a phrase that doesn't propagate to a new site (the T18 lineage,
   twice) and a number that drifts unreconciled across sibling files
   (`τ_shell=24` vs. 9.4026; the stale 150µm vs. the found range). Both
   are the same underlying failure class — a Phase-3/5 correction that
   doesn't automatically reach every site citing the old value — and
   this program now has three-plus independent instances of it. Building
   the tool once, rather than hand-catching a fourth and fifth instance,
   is the standing-infrastructure lesson this cycle's own review (and
   the caveat_lint tool's own origin story, Iteration 15→38) already
   teaches.

3. **Pin the record-blackness/Vantablack-class CNT forest's own inter-
   tube pitch/diameter figure** — the one genuinely open physical
   sub-claim this cycle leaves unresolved (EM-5's own "PARTIAL, geometry-
   class-dependent" finding: near-field coupling confirmed for
   spin-capable/yarn-precursor forests, refuted for two other sourced
   geometry classes, and the actual comparison class this program's own
   α figures cite was never itself pinned, across two full cycles of
   searching). A narrowly-targeted query set (or a renewed T18 primary-
   source attempt, now that `n_eff`'s originating title is finally
   pinned and might itself state a packing geometry) would close this
   and, as a direct side effect, sharpen THERMODYNAMICS' own flagged
   Idealization-9 dependency (whether `l_geometric_m`'s underlying α
   figure rests on a licensed homogenization) — the two open threads
   this cycle leaves are the same physical question asked from two
   different charters, and one search plan should serve both.

---

## 5. Ruled-out registry check (R1–R5, T1–T26)

No re-proposal found, on my own independent read of the complete
registry (`LOGBOOK.md`'s Ruled Out summary and full Live Threads
T1–T26) against this cycle's actual content:

- **R1–R5**: none apply. exp-062 makes no refractive-cloaking claim
  (R1), no integer-λ shell-thickness claim (R2), no grid-artifact
  explanation for a measured feature (R3 — if anything, this cycle
  correctly *invokes* the R3 discipline by name when discussing
  resolution-independence of its own passivity bound), no hand-typed
  "precisely recomputed" figure (R4 — every numeric claim in Sections
  4.5/5.3 of `phase1_proposal.md` and every EM-verdict computation in
  `phase4_results.md` is explicitly computed by direct Python invocation,
  independently re-run and confirmed to the printed digit by Red Team at
  Phase 2 and again, implicitly, by this cycle's own Phase-4 record), and
  no `P`-normalized phase-offset regressor (R5).
- **T1–T26**: exp-062 declares, correctly, "T1 escape route: NONE" — it
  scores no constraint-1/2/3/4 metric and touches no σ(I)/σ(x,t)/
  angular-selectivity machinery anywhere. Its near-field-coupling rider
  (Item B / EM-5) is a *real-material homogenization-validity* question
  at VACNT pitch scales — a different physical object from T21's
  FDTD-source edge-diffraction fringe, T24's `ABSORB`-boundary
  systematic, or T25/T26's coherent-ambient-sum machinery, and the
  proposal does not conflate them (confirmed by my own re-read of T21/
  T25/T26 in full). Its Section 4.4 resonant-absorber/Salisbury-screen
  alternative is genuinely new to this program's realizability line, not
  a resurrection of anything closed. `REALIZABILITY_MEMO.md` Entry 2 /
  Amendment 6 is read and extended, not re-litigated — the cycle
  correctly treats MP-2's thickness axis (70–350×) as the tier's own
  independently-sufficient, unrevisited anchor throughout, exactly as
  Amendment 6 itself states.

No addition to the ruled-out registry is warranted from this cycle's
content.
