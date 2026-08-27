# PHASE 5 — REVIEW · MATERIALS & METAMATERIALS · Panel Iteration 59 · exp-082

**Seat: MATERIALS & METAMATERIALS.** Fresh sub-agent, zero memory of any
prior session. Read PANEL.md, AGENTS.md, LOGBOOK.md (RULED OUT R1–R9 in
full, ESTABLISHED, LIVE THREADS T28 in full — Iterations 46–58), PLAN.md's
Iteration-59 queue, and the complete `experiments/082-.../` record in the
order specified: `phase1_proposal.md`, `NOTES.md`, `run.py`, `results.json`,
`run_output.txt`, `x_wall_realizable_refit.py`/`_results.md`/`_results.json`/
`x_wall_output.txt`, `phase_convention_extension.py`/`_results.md`/
`_results.json`/`_output.txt`, all five Phase-2 critiques,
`phase2_redteam_audit.md`, `phase3_synthesis.md`. **Not read**: any
`phase5_review_*.md`/`phase5_redteam_audit.md` from this cycle — blind to
the other six seats' current-cycle Phase-5 output, per protocol.

**No RULED-OUT item (R1–R9) is re-proposed or re-litigated.**

---

## 1. Verification: did fix-docket item 2 (article-generality scoping) land correctly?

**Yes, both parts, independently checked against the post-Phase-3 files
directly, not trusted from `phase3_synthesis.md`'s own account.**

I re-read `phase1_proposal.md`'s corrected "Combined self-score" and
"What this result does NOT establish" sections and `NOTES.md`'s corrected
"Learned" §1 in full, then grepped both files for every occurrence of "real
absorbing article[s]" and "the channel" to check for any surviving
unscoped-generalization sentence Attack 2 was supposed to remove:

```
phase1_proposal.md:354  **No claim is made here about "real absorbing articles" in
phase1_proposal.md:355  general, or about the channel independent of which article occupies it**
NOTES.md:94   "real absorbing articles" in general (MATERIALS' Phase-2 finding,
```

Every remaining hit is either task-framing prose from §0 (describing what
the cycle set out to test) or the explicit disclaimer itself — zero
surviving instances of the pre-audit generalizing claim ("every future
ambient-contrast citation... should now disclose this as a named,
quantified... confound", stated as a property of the channel). The
corrected headline is scoped explicitly and repeatedly to "the flagship,
strongly-absorbing article class" / "`materials.graded_black_shell`+
`pec_disk`, `C≈−0.55`" everywhere a generalizing claim previously stood.
**This is exactly the scoping my own Phase-2 critique asked for, and it
landed cleanly** — not softened, not left half-corrected the way T28's own
history (exp-055's T7/P-EST omission, exp-076's disclosed-then-dropped
gaps) has occasionally shown a fix-docket item partially applied.

**The near-null σ(I) follow-up is named as a board item — with one
residual gap, not a defect, worth flagging for Iteration 60's own
Director.** `NOTES.md`'s "Next" section states it explicitly, with the
correct construction and citation (`off_pass`, `τ_off≈0.0065`,
exp-032/exp-034) and the correct framing ("the test that would extend the
Combined self-score's own flagship-only scoping to the near-threshold case
where the confound could plausibly be perceptually load-bearing"). But
`phase3_synthesis.md` §3 item 2 is explicit that this is recorded in
`NOTES.md` only, not added to `PLAN.md`'s actual queue — that edit is
deferred to "the Director's own Phase 5 job." I confirm this disposition is
consistent (Phase 3 did what it said), but flag directly: **this Phase-5
pass is that job.** Whoever synthesizes this cycle's Phase 5 should add my
own flip-condition item to `PLAN.md`'s Iteration-60 queue explicitly, not
merely leave it standing in `NOTES.md`'s prose — otherwise it risks the
same "named-but-never-queued" governance gap MATERIALS itself caught and
Red Team adjudicated non-firing-but-flagged at exp-081 (the x-wall refit
silently dropping from a ranking for one cycle).

---

## 2. Verification: is item 1's own x-wall realizable-admittance result still correctly characterized post-Phase-3?

**Yes, unchanged, exactly as `phase3_synthesis.md` §3 item 6 states — and
I independently re-derived the load-bearing numbers rather than trusting
that statement.**

`phase3_synthesis.md` made zero edits to `x_wall_refit_results.md` or
`x_wall_realizable_refit_results.json` (nothing in the fix docket touches
either file). I re-read `x_wall_realizable_refit_results.json::
verdict_flips` directly: exactly two entries —
`(single_wall, pair_absorb40, INCONCLUSIVE, REFUTE)` and
`(two_wall, pair_pad, REFUTE, INCONCLUSIVE)` — matching both my own
Phase-2 critique's "2 of 4 cells flip, none to SUPPORT" claim and Red
Team's independent §0m reproduction bit-for-bit. The phase-divergence
figures (`ABSORB=40`: 18.25°–24.66°; `ABSORB=80`: 0.47°–15.01°) and the
qualitative pattern this program has established since exp-080 part(b)
(the two admittance families diverge more sharply nearer normal incidence,
less at grazing) also reproduce unchanged. **Item 1's own disposition
("closed for this cycle... no further action queued unless a future cycle
wants the full 3-λ leg") stands exactly as filed at Phase 1 — nothing
about it needed correcting, and nothing did.**

---

## 3. From my own charter: does this cycle's finding change how a future realizability memo touching T28 should be framed?

**Yes — and this is the most consequential thing my own charter has to say
about this cycle, worth stating plainly for Iteration 60 and any future
`REALIZABILITY_MEMO.md` amendment.**

Every prior T28 realizability question I or a predecessor MATERIALS seat
has scored (the x-wall single-/two-wall echo models, the y-wall echo, the
plane-wave/global-steering construction) was a question about a **candidate
boundary reflectance profile** — `r(theta; ABSORB)`, the graded-loss
band's own admittance, scored matched-vs-realizable (`μ_r=1`) because a
real coating is the only admittance family a physical material could ever
supply. That is exactly the shape "published / plausible /
unobtainium-with-parameters" is built to answer, and item 1's refit (§2,
above) is a legitimate instance of it.

**`PAIR_PAD` is not that kind of question, and this cycle's own record
makes the reason unusually clean and worth stating explicitly, not merely
inherited from Iteration 53's citation.** `PAIR_PAD`'s entire signal is
proven (Iteration 53, `lab/fdtd2d.py` primitives, re-confirmed this cycle
by THERMODYNAMICS' own Phase-2 attack and independently endorsed by Red
Team's Attack 3) to be a pure vacuum-domain-padding round-trip-timing
effect — `PAD` cells extend the FDTD lattice and shift coordinates, with
**zero** dependence in the damping-mask construction. It is `ABSORB`-
invariant by construction (bit-identical reflectance magnitude between
`C40`/`G40`), and — independently confirmed by this cycle's own x-wall
refit (§2 above) — the coherent-echo models built to explain it are
REFUTE/INCONCLUSIVE under *either* admittance family, not converging
toward either. There is no material, real or hypothetical, whose admittance
this effect is waiting on: it is a statement about **how far vacuum extends
inside the simulated domain before the model's own boundary**, not about
what any wall is made of. My own charter's realizability taxonomy —
published / plausible / unobtainium-with-parameters — has no correct entry
for it, because the question it answers is not "can a material supply
this," it is "does the scene's own physical geometry (a real wall's
standoff distance, a real room's extent) reproduce this bench's own domain
size." That is a scene-construction/geometry question, not a materials
one.

**The practical framing consequence, stated for the record:** even in the
counterfactual where the mechanism-identity question (§0d–k of Red Team's
audit, this cycle) resolved cleanly in favor of continuity — i.e. the exact
same lossless `PAIR_PAD` phase artifact were shown to persist unchanged
once a real absorber sits in the coherent path — **that would still carry
zero realizability content.** It would say the numerical-domain-truncation
artifact rides through to the scored channel; it would say nothing about
whether any coating, near-null σ(I) article, or exotic admittance profile
is needed, because none is implicated in the mechanism at all. A future
realizability memo that cites this cycle's SURVIVES finding must therefore
draw the line explicitly: **`PAIR_PAD`'s own contribution to any future
constraint-3 citation is a scene/instrument-geometry disclosure, filed
alongside (not folded into) any MATERIALS realizability score for the
article itself** — conflating the two would misattribute a domain-boundary
artifact to a material property nobody has proposed. This does not change
today's `REALIZABILITY_MEMO.md` verdicts (nothing in it cited `PAIR_PAD`
as material evidence to begin with), but it is worth stating as a standing
framing rule the next time this sub-thread's findings get folded into a
realizability document — the same discipline this program applies
elsewhere (R7: a design-time quantity is not a substitute for the fit that
actually measures the thing) applied here one level earlier: **a rides-
through/cancels finding about a proven-lossless-vacuum artifact is not
evidence about ANY material family, favorable or unfavorable, until a
mechanism that actually depends on `ABSORB`/admittance is shown to be what
produces the measured `delta_scene(θ)`.**

---

## 4. Other charter-relevant checks performed

- **Article identity, re-verified from primitives, not merely re-trusting
  my own Phase-2 critique's claim.** Read `experiments/024-.../run.py`
  directly: `build("absorber")`'s "stage-7 config verbatim" branch is
  `materials.pec_disk(sim, cx, cy, 30)` +
  `materials.graded_black_shell(sim, cx, cy, 30, dg.R_OUT)` —
  line-for-line identical to `exp-082/run.py::build_article`. The claim
  every phase of this cycle has relied on (this is the ESTABLISHED
  flagship, not a relabeled variant) is confirmed a third time, from the
  source file itself.
- **Secondary-metric relabeling (item 3) does not touch anything in my own
  charter's domain** — confirmed it does not reintroduce or restate any
  realizability claim; it is purely a VISION-charter unit/kind-mismatch
  correction, correctly scoped.
- **No new `lab/` machinery, confirmed independently**: `git diff --stat
  -- lab/` empty at the time of this review; both riders (x-wall refit,
  phase-convention extension) import only already-gated, already-committed
  experiment-local functions — nothing in this cycle touches
  `materials.py` or introduces a new admittance family beyond the two
  (matched, realizable) already validated at exp-080.

---

## 5. Verdict (this cycle's own work): **PARTIAL**

Not RULED OUT — nothing here forecloses a mechanism or closes a
realizability question; not PROMISING — zero constraint-3 engagement (T1:
N/A, confirmed consistently applied), and the cycle's own most consequential
substantive question (mechanism-identity of `delta_scene`) is demonstrated,
not merely left open, to be unresolvable at this cycle's own statistical
power. What this cycle delivers, cleanly: the standing six-cycle tripwire
on the PAD-loaded real-article check is genuinely discharged, not merely
argued past; item 1's x-wall refit is closed with a real (if non-flipping)
finding; the phase-convention extension is honestly self-downgraded rather
than reported as a false tie-break; and the Phase-2 process caught and
fixed two overclaims (mechanism-continuity, article-generality) plus one
reviewer's own arithmetic slip, entirely inside the review layer, with
Checkpoint criterion 4 correctly not firing. This is the sub-thread's own
established PARTIAL shape (matching Iterations 53, 55, 56, 58) — genuine,
independently-verified narrowing without resolving T28's own central
mechanism question.

## 6. My own ranked top-3 candidate directions for Iteration 60

1. **The near-null σ(I) article follow-up (my own named flip condition,
   Attack 2's fix, `NOTES.md`'s "Next" item 1).** Rerun the identical
   `PAIR_PAD`/C40–G40 harness with `build_article` replaced by `off_pass`
   (`τ_off≈0.0065`, exp-032/exp-034) in place of `graded_black_shell`. This
   is the single test that would tell my own charter whether this cycle's
   `ratio≈0.66`/`A_scene/C_thr≈0.68` reading is an artifact of testing a
   ~100×-past-threshold article, or whether a genuinely near-threshold
   article shows a comparable (or larger, or vanishing) relative reading —
   the only version of this question with any bearing on
   `REALIZABILITY_MEMO.md`'s own UNOBTANIUM-WITH-PARAMETERS scope. Should
   be added to `PLAN.md`'s Iteration-60 queue explicitly this pass (§1,
   above), not left as unqueued `NOTES.md` prose a second cycle running.
2. **The x-wall wavelength-generality leg (750/450nm), still six
   consecutive cycles deferred.** With item 1 now closed for this cycle
   (§2, above), the single oldest-standing MATERIALS-charter item on the
   whole T28 board is whether the matched-vs-realizable phase-divergence
   pattern this refit (and exp-080's own part(b)) established at 600nm —
   larger divergence nearer normal incidence, smaller at grazing — holds
   at 450nm and 750nm too, or is itself a 600nm-specific artifact of this
   bench's own `n(x)` dispersion model. Zero new FDTD machinery required;
   reuses `x_wall_realizable_refit.py`'s own structure at two more `CPL`
   values.
3. **The full 31-point/0.2° window at the same `PAIR_PAD` pair** — not
   primarily a MATERIALS-charter item, but a precondition for either of the
   above to mean anything: until the mechanism-identity question (§3,
   above) is resolved with real statistical power, no future realizability
   framing can responsibly say whether `delta_scene(θ)`'s article-loaded
   signal is still the proven-lossless `PAIR_PAD` artifact (§3's own
   scene-geometry disclosure, no material implicated) or a genuinely new,
   possibly absorption-coupled interaction (which WOULD re-open a live
   MATERIALS question — what article property would produce it). Ranking
   this third, not first, only because items 1–2 are cheaper and can run
   in parallel; if Iteration 60's own budget is tight, this is still the
   single item most likely to change how my own charter should treat this
   cycle's SURVIVES finding going forward.

Full record consulted: `experiments/082-t28-pad-real-article-check/` —
`phase1_proposal.md`, `NOTES.md`, `run.py`, `results.json`,
`run_output.txt`, `x_wall_realizable_refit.py`/`_results.md`/
`_results.json`/`x_wall_output.txt`, `phase_convention_extension.py`/
`_results.md`/`_results.json`/`_output.txt`, all five Phase-2 critiques,
`phase2_redteam_audit.md`, `phase3_synthesis.md`. Cross-checked against
`experiments/024-.../run.py` (article identity) and LOGBOOK.md's T28
history (Iterations 46–58) directly.

None of the above re-opens or re-proposes any RULED-OUT item (R1–R9).
