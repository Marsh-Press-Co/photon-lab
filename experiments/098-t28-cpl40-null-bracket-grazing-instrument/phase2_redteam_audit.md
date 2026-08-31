# Panel Iteration 75 — Phase 2 RED TEAM Audit

*Speaks last, sees everything: Phase-1 proposal (EM, lead) + all five blind
Phase-2 critiques (PHOTONICS, MATERIALS, THERMODYNAMICS, QUANTUM OPTICS,
VISION SCIENCE). Standard: not textbook-physics compliance — speculation
is permitted. Kills internal inconsistency, unfalsifiable claims,
mechanisms that cannot be expressed as simulation parameters, and quiet
constraint violations (especially #3). Every claim below re-verified
against source this session — nothing taken on the critiques' word.*

## 0. Source-of-truth confirmations (before any attack)

- Item (v)'s actual source is confirmed: `dg048._geom_derived` /
  `edge_diffraction_c_empty_corrected` live in
  `experiments/048-evidentiary-chord-closure/design_geometry.py:179-230`,
  loaded transitively through `experiments/085-t28-leg-a-wide-window-period-pin/phase4_derivation.py`'s
  `FastEval` (`dg048 = deriv.dg048`, `CFG_C40 = deriv.CFG_C40`). This *is*
  the file the proposal's item (v) intends — not a different path.
- `_geom_derived(g)` (design_geometry.py:179-197) takes **only** a
  geometry dict `g`; `gd["r"]` is built from `y_lo/y_hi/d_sp` alone —
  **no `theta` parameter anywhere in its signature or body.** The
  `FastEval` module's own docstring (phase4_derivation.py:18) independently
  states this in so many words: *"theta-INDEPENDENT G0/geometry matrix
  (`_geom_derived`...)"* — this is not a subtle inference, it is
  self-documented at the source.
- Numerically re-ran it myself (`CFG_C40`, λ=600nm/cpl=20):
  `kr_min = k·min(gd["r"]) = 70.05751617505238` — matches PHOTONICS'
  reported 70.06 to the stated precision, and is trivially identical for
  every θ since `gd` never depends on θ. **PHOTONICS' headline claim is
  confirmed exactly, both by code inspection and by direct numerical
  re-execution.**
- `lab/ambient.py::weber(b_obj,b_flank) = (b_obj-b_flank)/b_flank`
  confirmed by direct read — GP1's `C(θ)≥−1` is algebraically `bo/bf−1≥−1`
  ⟺ `bo≥0`, exactly as QUANTUM OPTICS re-derived; it is a **ratio**, so a
  uniform amplitude blow-up in both `bo` and `bf` cancels and is invisible
  to it.
- `experiments/086-t28-free-period-boundary-fix-rescore/phase5_review_photonics.md:120-138`
  confirmed on file: "a bare scalar Kirchhoff-Huygens coherent sum... no
  Fresnel-transition or UTD-style shadow-boundary correction term,"
  producing a **5,444×–6,631× amplitude blow-up at θc≈59°–73°**, verified
  against `phase4_rescore_results.json` (`ptp` 2.558e-4 → 1.696, exact
  factor). This sits squarely inside item (v)'s 30°–89.5° sweep.
- `experiments/069-t21-block-mini-period-match-power-up/design_geometry.py:309-310,395-398`
  confirmed: `L_GEOMETRIC_M_R4`/`L_GEOMETRIC_M_R5` are both asserted
  `== R_OUT*30.0e-9` (native) to `1e-12`, and asserted equal to each other.
  `CPL = {R3:30, R4:40, R5:50}` (dict lookups) is purely a grid-density
  parameter; the *physical* geometry is invariant by construction. MATERIALS'
  claim confirmed exactly. No convergence-order/Richardson computation exists
  anywhere in the codebase (`grep` for `Richardson`/`convergence_order`/
  `order_estimate` across `experiments/09*` and `LOGBOOK.md`: zero hits
  except one *proposed-not-executed* mention in exp-091's Phase-5-EM review).
- `_geom_derived`'s `y_src`/`y_obs` (design_geometry.py:190-191) are
  **the identical `np.arange(y_lo,y_hi)` call**, and I confirmed
  numerically that `obliquity` is symmetric under `i,j` swap purely because
  there is one shared `d_sp`. QUANTUM OPTICS' claim confirmed exactly.
- VISION's word count confirmed by direct re-run: `sed -n '5,35p'
  iter75_phase1_proposal.md | wc -w` → **270**, matching VISION's figure,
  not the proposal's own claimed 278 (moot either way — both are under the
  300 cap). The literal string "Result" (case-insensitive) does not occur
  anywhere in the Phase-1 document; §5's banner reads "every **prediction**
  in §4 is governed by..." — confirmed, VISION's claim is exact.
- **THERMODYNAMICS' precedent citation does NOT hold up** — see Attack 4,
  the one finding in this audit that overturns rather than sharpens its
  source critique.

## Numbered attacks

**1. [unfalsifiable] GP2 as specified cannot fail — the proposal's own §4
table misrepresents a deterministic non-test as an open empirical
question.** §4 calls GP2 "Genuinely open" with a stated falsifier ("if
`kr_min` drops to MARGINAL/INVALID at some θ*, report θ* as the model's
own self-diagnosed boundary"). Given `_geom_derived`'s structure (§0
above), `kr_min(θ)` is not merely *likely* to stay constant across the
21-point sweep — it is *the same floating-point number* for every θ,
because θ never enters the computation that produces `gd["r"]`. There is
no θ* this check can ever report; VALID-at-every-point is not a finding,
it is a restatement of one number (`kr_min=70.06`) computed once. A claim
whose falsifying observation is excluded by the code's own construction,
before any run, is not a falsifiable test dressed as a scheduled
evaluation — it is a guaranteed result dressed as one. This is the
proposal's own defect, independent of PHOTONICS having caught it; the
same source-read that produced item (v)'s design should have caught it
too. **Escalates PHOTONICS to a proposal-level defect, not just a
critique-level one.**

**2. [inexpressible] Neither GP1 nor GP2, as specified, can express the
one failure mode this seat has already quantified on file.** The actual
known defect (θc≈59°–73° amplitude blow-up, 5,444×–6,631×, no UTD/
shadow-boundary term in the model) is a raw-amplitude, θ-dependent
phenomenon. GP1 is a *ratio* (cancels scale by construction — confirmed
via `weber()`'s algebra). GP2 is a *θ-independent geometric distance*
(cancels θ-dependence by construction — confirmed via `_geom_derived`).
There is no simulation parameter in items (v) as specified that a UTD/
shadow-boundary correction failure could ever move. This is not a
tuning problem fixable by re-running with different angles; it requires a
genuinely different instrument (raw `|C(θ)|`/`max(|Sx|)`, or a
`kr·cos²θ`-type transition proxy) before the mechanism under question is
even representable. PHOTONICS' proposed flip is the correct fix; MATERIALS
and QUANTUM's blindness to this reinforces it independently (neither
seat's own charter caught the amplitude-blindness angle, which is
consistent with it being a genuinely orthogonal gap, not overlap noise).

**3. [inconsistency] Item (v)'s framing risks a quiet, indirect
constraint-3 exposure two cycles from now.** [Framed as a foreseeable risk,
not a violation this cycle — Checkpoint criterion 2/constraints 1-4 are
correctly N/A this cycle per Idealization 7, and I am not asserting
otherwise.] If (v) runs as specified and reports "PASS/VALID at every θ
through 89.5°" without correction, a future cycle citing this validity
certification to support an angular-selectivity contrast claim *near
grazing incidence* — exactly where constraint 3 (invisible at rest, only
the swept beam reveals it) would most plausibly need to be demonstrated
for a shell whose ambient-scene contrast depends on incidence angle — would
be building on a certification already known, at the time it was issued,
to be blind to a proven 5,444×–6,631× breakdown in that exact angular
band. This is precisely the "quietly violates a target constraint —
especially #3" pattern this charter exists to prevent, surfaced now while
it is a documentation fix, not later as a load-bearing false premise. This
is the strongest argument for treating item (v)'s current design as a
mandatory fix rather than a nice-to-have.

**4. [inconsistency] THERMODYNAMICS' central evidentiary claim
("exp-095/Iteration-72's own near-miss on this exact R4-family pairing")
is factually wrong on both particulars — OVERRIDE.** Independently traced
through `LOGBOOK.md` (lines 613-628, 6050-6090, 6230-6260) and both
experiments' own records:
  - The R16-founding near-miss (a `_full`-metrics byproduct computed but
    not persisted via `netd_row()`) occurred at **exp-094 / Panel
    Iteration 71**, not exp-095 / Iteration 72. LOGBOOK.md states R16
    "does NOT fire on its own founding instance (exp-094)" and names the
    gap as "exp-094's own Rank 2/Rank 3 calls."
  - exp-094's Rank 2/Rank 3 used **`PAIR_KEYS_R3=("C40_R3","G40_R3")`**
    (the R3 family, cpl=30) — confirmed directly from
    `experiments/094-.../NOTES.md:39-40,84-91`. It was *not* the
    `C40_R4`/`G40_R4` pairing this cycle's items (i)/(ii) actually reuse.
  - exp-095 (Iteration 72) is independently confirmed CLEAN on this exact
    axis by its own Phase-5 THERMODYNAMICS review
    (`experiments/095-.../phase5_review_thermodynamics.md`): *"CONCUR, NO
    R16 GAP FOUND — a genuinely clean cycle on my charter's own founding
    failure mode,"* and *"R16 compliance is clean, the first T28 cycle
    since its adoption to engage this exact risk class and close it."*
    That review traces `netd_row(pm)` splatted at every executed call
    site (`run.py:564,632,720/1288`) with no intervening filter.

  **Ruling: OVERRIDE the precedent claim, ADOPT the recommendation on
  independent grounds.** There is no on-file near-miss for the specific
  `C40_R4`/`G40_R4` pairing this cycle reuses — the "prose discipline
  already failed once under this same R4/C40/G40 pairing" framing should
  not be repeated in Phase 3/4 documentation; it is not supported by the
  record and a future audit citing it would inherit the error. This
  *weakens* the urgency framing, but does not eliminate the underlying
  risk: R16's own ratified text (`LOGBOOK.md:619-628`) already states a
  disclaimer traveling unconditionally is "necessary, not sufficient" —
  independent of any specific precedent, item (iii)'s prose-only
  commitment does not meet the rule as written (see Attack 5). The
  mandatory build-time assert THERMODYNAMICS proposes is correct
  engineering discipline on that independent basis, not on the
  misattributed one.

**5. [inconsistency] Item (iii) as specified does not satisfy R16's own
text, independent of any precedent dispute.** R16 (`LOGBOOK.md:619-628`,
ratified rule, not a critique opinion) reads: a disclaimer "travels
unconditionally, but is necessary, not sufficient: the byproduct itself
must be persisted... for every cell/angle where it is computed." Item
(iii) is stated as *"a design constraint on Phase 4 implementation, stated
here so Phase 2/3 can hold it as a mandatory fix if the eventual `run.py`
draft omits it"* — i.e., detection is deferred to a human re-reading the
diff after the fact. That is exactly the "disclaimer travels, persistence
optional" shape R16 was written to close off, applied one level up (to
the *review process* rather than the *code*). A written mandatory-fix note
that only fires if a reviewer happens to re-check it is not the same
category of guarantee as `assert NETD_KEYS <= row.keys() for all 32 rows`
failing the run. **ADOPT THERMODYNAMICS' fix in full** (the concrete
`assert` over all 32 rows' 10 keys, raising before `results.json` is
written) — on this independently-verified textual-consistency ground, the
misattributed precedent in Attack 4 notwithstanding.

**6. [inconsistency] MATERIALS' "false dichotomy" finding is confirmed and
adopted in full — ADOPT.** Source-verified (`experiments/069-.../
design_geometry.py`): `cpl` is exclusively a grid-density parameter
(`CPL={450:15,600:20,750:25}`-style dicts), physical geometry
(`L_GEOMETRIC_M_R4`/`_R5`) is asserted invariant to `1e-12` across R3/4/5,
and no convergence-order estimate has ever been computed from the three
now-available resolution points despite the shift history being
non-monotonic in sign (−0.194°/+0.320°/+0.377°, confirmed in
`experiments/092-.../results.json::rank1.crossing_report`). "Genuine
migration vs. family-wide recipe defect" omits a third live possibility —
unconverged discretization that happens to point the same direction at
cpl=20→30→40 without ever approaching the continuum value. Item (i)/(ii)
can PASS-family-clean and still be silent on where a real device's null
sits. The proposed Richardson-style pairwise-shift-ratio addition is
zero-marginal-cost (arithmetic over already-computed numbers) and should
be added to the report dict alongside `netd_row()` in the same commit.

**7. [inconsistency] QUANTUM OPTICS' GP3 degeneracy finding is confirmed —
ADOPT, non-blocking.** Numerically and textually confirmed: `y_src` and
`y_obs` are the literal same `np.arange(y_lo, y_hi)` construction
(design_geometry.py:190-191); `obliquity` is symmetric purely because one
`d_sp` serves both roles — there was never a second, independently-defined
observer-side obliquity to compare against. GP3's own framing ("symmetrized
... or single-sided") poses a question with only one live answer in this
geometry, and reporting "symmetric: confirmed" without saying *why* risks
a future citation reading it as evidence a genuine two-sided check was run
and passed. Add QUANTUM's one sentence to the GP3 write-up before Phase 4.

**8. [inconsistency] VISION's Result-banner gap is confirmed — ADOPT.**
The literal string "Result" does not appear in the Phase-1 document; §5's
banner text covers "every prediction in §4" only. `LOGBOOK.md` confirms
the dual Predictions+Result banner requirement is a standing, escalated
rule (multiple hits on "dual-section carried-idealizations banner"), and
`experiments/097-.../phase2_redteam_audit.md:289` confirms the
grep-verification duty is likewise on file, both unrestated here. Since
the NOTES.md this governs does not exist yet, this is a completion risk,
not a present defect — but given this exact silence-shaped precondition
(rule applies automatically, no need to restate) is what let the defect
recur twice already per VISION's own charter history, it should be closed
in writing before Phase 4, not left to "applies automatically."

**9. [inconsistency] Items (i)/(ii)'s own predicted-outcome table is
internally honest but the proposal's summary language in §1/§3 leans
harder toward "instrument-trust bookkeeping" than the actual epistemic
status of a still-open, genuinely bimodal physics question warrants.**
Not disqualifying — §4's table itself states "no confident lean" for both
outcomes — but §1's narrative ("determines whether the FDTD instrument...
is itself trustworthy") undersells that a family-wide FAIL result (all
three nulls same-sign) is *also* consistent with MATERIALS' unconverged-
discretization reading, which the proposal's own §3 T1-mapping does not
mention. Minor, cosmetic; flagged for Phase 4 wording only, not a fix
gate.

## Verdict on item (v) and the grazing-incidence governance ask

**Ruling: item (v) as specified cannot honestly discharge the
two-cycle-old grazing-incidence governance ask, and must not be written up
as doing so.** GP2's kr-classification is not a measurement of anything —
it is a single already-known number reported 21 times. GP1 is blind to
the one quantified failure mode by the algebra of a ratio. Both facts are
now confirmed at the source level (Attacks 1-2), not merely alleged.

This is not a case for REJECTing item (v) outright — GP1 (passivity) and
GP3 (reciprocity code-read, with QUANTUM's degeneracy caveat attached) are
legitimate, cheap, correctly-scoped self-consistency checks, and running
them costs nothing. The dishonest move would be letting the write-up
*call* the resulting PASS/VALID-everywhere finding a discharge of the
standing item. Two paths were offered in this audit's own mandate; I rule
for a **combination, not either alone**:

1. **Replace or supplement GP2** with a genuinely θ-dependent instrument
   before Phase 4 runs — PHOTONICS' proposed fix (report raw `|C(θ)|`/
   `max(|Sx|)` alongside the ratio, or a `kr·cos²θ`-style UTD-transition
   proxy) costs the same near-zero marginal time as the current 21-point
   sweep, since it reuses the same `FastEval.curve()` call.
2. **Regardless of (1)'s outcome**, Phase 4's write-up must state plainly,
   *before* any run, exactly the sentence PHOTONICS' flip proposes: GP1/
   GP2 as originally specified are passivity/reciprocity **self-
   consistency checks only**, and do not by themselves discharge the
   standing grazing-incidence item. If (1) is not implemented this cycle,
   the honest move is the smaller one named in this audit's own charge:
   explicitly scope GP1-3 as self-consistency-only and **formally defer**
   the two-cycle governance ask one more cycle, with the reason stated
   plainly (the model's own known blind spot, not a resourcing excuse) —
   rather than let a PASS/VALID table row be read as a discharge it
   cannot support.

Either path is acceptable; silently shipping item (v) as-specified with
its current §4 framing is not — that is exactly a quiet drop of a standing
commitment, which this audit's own mandate forbids.

## Adopt/Override summary (Director-citable)

| Seat | Headline finding | Ruling |
|---|---|---|
| PHOTONICS | GP2 θ-independent by construction; kr_min=70.06 constant; item (v) risks discharging governance ask blind to known θc≈59-73° blow-up | **ADOPT, ESCALATE** (Attacks 1-3) — confirmed exactly at source, elevated from "critique" to "proposal-level defect" |
| MATERIALS | `cpl` is grid density only, physical geometry fixed; "migration vs. defect" is a false dichotomy absent a convergence-order estimate | **ADOPT in full** (Attack 6) — confirmed exactly, zero-cost fix should be added |
| THERMODYNAMICS | exp-095/Iteration-72 near-miss on the R4-family pairing shows prose discipline already failed once | **OVERRIDE the precedent** (Attack 4) — wrong cycle (exp-094, not exp-095) and wrong family (R3, not R4); exp-095 is independently confirmed CLEAN. **ADOPT the recommended fix anyway** (Attack 5) on R16's own text, which needs no precedent to require enforcement over prose. |
| QUANTUM OPTICS | Idealization-40 correction is right; GP3's dichotomy is degenerate (single shared `d_sp`) | **ADOPT both** — Idealization-40 correction independently re-confirmed via `CPL` dict injectivity; GP3 degeneracy confirmed numerically (Attack 7), non-blocking as QUANTUM itself scoped it |
| VISION SCIENCE | §1 is 270 words (not 278), under cap; §5 banner covers Predictions only, never "Result" | **ADOPT both** (Attack 8) — word count and banner-gap both reproduced exactly from source |

## Overall verdict: **PROCEED-WITH-MANDATORY-FIXES**

Items (i)-(iv) are disciplined, cheap, well-scoped house-discipline work
and should proceed without gating on item (v)'s resolution — nothing in
(i)-(iv) depends on it. Mandatory fixes before Phase 4 `run.py` is
written:

1. Item (v): implement PHOTONICS' θ-dependent GP2 replacement/addition, or
   explicitly rescope GP1-3 as self-consistency-only and formally
   re-defer the grazing-incidence governance ask with a stated reason
   (Attacks 1-3).
2. Item (iii): replace the prose commitment with THERMODYNAMICS' concrete
   build-time `assert` over all 32 rows' 10 `netd_row()` keys — required
   by R16's own text regardless of the corrected precedent (Attacks 4-5).
3. Item (i)/(ii): add MATERIALS' zero-cost pairwise-shift-ratio
   (Richardson-style) field to the report dict (Attack 6).
4. Item (v) GP3: add QUANTUM OPTICS' one-sentence degeneracy disclosure
   (Attack 7).
5. §5: add VISION's dual-section (Predictions + Result) banner commitment
   sentence, restating the grep-verification duty, before Phase 4 drafts
   NOTES.md (Attack 8).

No REJECT-level defect exists: nothing here is unrepairable, nothing
implicates already-committed construction code, and the cheap items
((iii)/(iv)/(v)) can absorb every fix above at zero marginal FDTD cost.
