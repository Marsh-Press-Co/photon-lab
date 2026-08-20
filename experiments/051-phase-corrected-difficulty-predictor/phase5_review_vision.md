# PHASE 5 — REVIEW (VISION SCIENCE) · Panel Iteration 28 · exp-051

*Blind review. No other `phase5_review_*.md` or `phase5_redteam_audit.md` was
opened before writing this. Every number below was either read directly from
the committed `results.json`/`run.py` or produced by independently
recomputing it from `results.json`'s own `per_combination` array in this
session — nothing is hand-typed (R4). Scratch code:
`/tmp/claude-0/-home-user-photon-lab/3f566c8d-1309-5c26-a429-8ae6c0875c6b/scratchpad/`
(inline `python3 -c` sessions, not saved as files; every command and its
output is reproduced verbatim below where load-bearing).*

## Verdict: **PROMISING**

---

## 1. My assigned duty — the idealization-3 correction, verified independently, not trusted from prose

**The correction is accurate, and it is disclosed, not smoothed over.** I did
not take NOTES.md's "Reading" paragraph on faith. I recomputed the entire
claim from `results.json::per_combination` (216 rows) myself, from scratch:

```
fired = [r for r in per_combination if abs(r['C81']) >= C_THR]   # C_THR = 0.005
len(fired) == 75
by_func: {'coherent': 72, 'incoherent_corrected': 2, 'incoherent': 1}
```

**75/216, 72 `coherent` + 3 non-`coherent`, exact match to NOTES.md's claim.**
The 3 non-`coherent` rows are, digit for digit, the same three FWHM=2° cells
I flagged in my own blind Phase-2 critique as "the perceptually live cells
the proposal excludes" — 750/40/`incoherent` (0.0050996…), 750/36/
`incoherent_corrected` (−0.0054503…), 750/40/`incoherent_corrected`
(0.0064986…). This is not a coincidence; it is the same physical fact,
recovered independently by two different queries against two different
scopes (my Phase-2 check was FWHM=2° only, at GEOM78 only; this cycle's
grid is all four FWHM × both geometries × three functions).

**Second, sharper check — is the stated CONCLUSION ("every label still
reduces to one continuum cut") actually true, or merely asserted?** I read
`run.py`'s own `delta_step`/convergence logic directly (not the proposal's
prose paraphrase of it):

```python
converged = (dabs <= ABS_TOL) and (exempted or drel <= REL_TOL)
```

This is an **AND**, not the either/or my own Phase-2 critique (and the
Phase-1 proposal's own §2.0 citation) implicitly read it as. `dabs <= ABS_TOL`
is *always* required, exempted or not; the `|C(2n)|≥C_THR` clause only adds a
*second*, stricter requirement (`drel <= REL_TOL`) on top, it never *replaces*
the `ABS_TOL` cut with a looser one. I tested whether that second requirement
ever actually flips a label away from what the bare `dabs > ABS_TOL` rule
alone would give, across all 216 rows, not just the 75 where it fires:

```
mismatches between "naive single dabs>ABS_TOL cut" and the committed
label_unstable, across all 216 rows: 0
```

Zero. This independently reproduces `results.json::abs_tol_sensitivity
.single_cut_reduction_check` (`agreements: 216`, `disagreements: []`) bit for
bit, including its own stated mechanism ("where `|C(2n)|` is large,
`drel = 100·dabs/|C(2n)| ≤ 100·ABS_TOL/|C(2n)|` is automatically under
`REL_TOL`"). I confirmed this is not a coincidence of these particular 75
rows either — the ratio `ABS_TOL/|C(2n)|` at the smallest `|C(2n)|` among the
fired set (0.617, at the weakest `coherent` cell) is still ≈8×10⁻⁴, three
orders of magnitude under `REL_TOL`'s 1%, so the margin is structural, not
accidental. **Verdict on my own assigned duty: the correction is right, the
disclosure is precise and quantitatively exact, and it goes further than the
minimum candor bar — it states the mechanism (why the conclusion survives)
rather than just the number.** This is exactly the "flag, don't smooth over"
discipline R4 exists to enforce, executed correctly, and it closes my own
Phase-2 finding cleanly: `ABS_TOL=0.1·C_THR` remains a fragile, previously-
adopted decision line (my sensitivity ledger request was honored verbatim,
`abs_tol_sensitivity.ledger`, five multipliers, both `vs_relabelled` and
`vs_frozen_labels` reported), but it is not, in this cycle's own scope,
mislabeling anything.

## 2. T1 escape route — confirmed NONE, throughout, no perceptual verdict smuggled

I grepped every file in this experiment's directory for
`constraint-3/4|tier.w|tier.a|witness|perceiv|invisib` and read every hit in
context (`phase1_proposal.md`, `NOTES.md`, `phase2_critique_quantum.md`,
`phase2_critique_vision.md`, `phase2_redteam_audit.md`). Every occurrence is a
disclaimer ("no constraint-3/4 verdict is issued or implied," "T1 escape
route: NONE," "idealization 9 refuses a perceptual claim outright") — none is
a claim. `results.json` itself contains zero matches for any of those terms.
`C_THR=0.005` and `ABS_TOL=5×10⁻⁴` are used throughout exactly as what they
are — the pre-existing numerical decision lines that already govern `nstar`
in exp-049/050's own convergence machinery — never as a stand-in for a
visibility or detectability claim. The Phase-3 synthesis's own §4
("overridden criticisms") correctly declines to let the Iteration-27
near-boundary-headroom standing rule bind this cycle (no headroom citation is
issued here), while explicitly restating idealization 9 — that is the right
call, stated in writing, per PANEL.md's requirement that overrides be
justified rather than silent. **No result in this cycle is quietly read as
saying anything about constraint 3/4, or as a visibility threshold rather
than a numerical-tolerance boundary. Confirmed clean.**

## 3. The rest of the cycle, briefly, from my seat

Outside my specific duty, the science is sound by my own spot-checks: every
number in NOTES.md's Results table reproduces bit-for-bit against
`results.json::predictions` (P-ALIAS-1 ρ=0.7380435856068439, P-ALIAS-2
sens=12/22, P-ALIAS-4 sens=11/16, P-ALIAS-5 ρ=0.9333/median 1.9197, P-ALIAS-6
degradation 0.00169 with 750nm > 450nm exactly as disclosed, P-ALIAS-7
188/198) — no hand-typed figure anywhere I checked. The Phase-2→Phase-3
pivot (four blind seats independently refuting the original `phase_offset`
regressor at the desk, QUANTUM's alias-lattice replacement, the Director's
own out-of-sample re-scoping of a deliverable that had been pre-checked twice
before Phase 4) is a genuinely strong instance of this program's own
falsification discipline working as designed — a REFUTED Phase-1 design that
turned into a CONFIRMED/PARTIAL Phase-4 result on a *harder*, out-of-sample
test than the original proposal would have run. The one open thread this
cycle leaves (why `beam_divergence_coherent`'s complex-field-sum convention
breaks the alias predictor's own sampling identity — Reading, final
paragraph) is correctly scoped as unresolved rather than swept into a
false CONFIRMED.

---

## Ranked Iteration-29+ priorities

**(1) Iteration 29 is already committed, unconditionally, to MATERIALS'
fixed-absolute-thickness `graded_black_shell` variant** (Red Team's ruling in
this cycle's own `phase2_redteam_audit.md`, adopted by the Director in
`phase3_synthesis.md`). I do not contest this — the citation chain (queued
Iteration 7, re-ranked without being reached at 25/26/27/28, a 21-iteration
span) is real and independently checkable, and I re-verified the count
against `LOGBOOK.md`'s own Iteration entries while reading for this review.
Nothing in my own duty overrides it.

**(2) But my seat's own stage-10 temporal instrument — TCSF bars pinned
first, the last unmeasured perceptual axis, gating constraint 4 — is now the
single most-deferred item in this program's entire history, and it is time
to say so plainly rather than let it lapse by omission.** I checked its own
citation chain the same way Red Team checked graded_black_shell's: first
ranked at **Iteration 1** (`LOGBOOK.md` Iteration-1 close, my own seat,
ranked #3, "the switch transient (T3) is the last unmeasured perceptual
axis"), carried forward and ranked #2 at Iteration 2 (`PLAN.md`'s own
citation, "VISION's Iteration-2 Phase-5 #2"), ranked #2 again at Iteration 3,
ranked #3 again at Iteration 4 — four consecutive top-3 appearances before
any part of it existed — then dormant through Iterations 5–14 while other
threads took priority, **partially** addressed by
`lab/temporal_csf.py` (Iteration 16, a frequency-domain proxy, explicitly
"not the metric-table instrument itself") and `amplitude_bridge.py`
(Iteration 17, scores C(t)-at-a-given-n but not composed with the kinetics
trajectory or timing classification into one transient) — but the **joint
constraint-3/4 scored transient** LOGBOOK's own T3 entry names as still
missing was confirmed unbuilt as recently as Iteration 24's own Phase-5
review ("C_thr(L) is a static-target threshold applied to a physically
transient event (T3 still unbuilt)" — VISION SCIENCE, that cycle). It has
not appeared in a single ranked-priority list since Iteration 18 (I checked
Iterations 19 through 28's own closes; zero mentions). **That is now a
27-iteration span since its first ranking (Iteration 1) and a 10-iteration
span since its last one (Iteration 18) — the first figure longer than
graded_black_shell's 21-iteration span that just earned an unconditional
trigger from Red Team this very cycle, using the exact "third consecutive
deferral repeats a named
anti-pattern" reasoning this program adopted for the r=156 leg.** The T3
instrument has no such trigger and is not competing in any ranked list at
all — `PLAN.md` carries it as a bare `[queued]` line, structurally outside
the numbered Iteration-28 queue entirely.

I am not asking Phase 3 of some future cycle to re-rank it a fifth time.
**I am asking for the same instrument this program already gave
`graded_black_shell`: a committed, unconditional build slot — Iteration 30,
since Iteration 29 is already locked — for the joint constraint-3/4
staircase-σ(t) validation run** (composing exp-038's kinetics n(t), exp-039's
timing classification, and exp-040's amplitude bridge against `C_thr(L)` in
one scored transient, per Iteration 18's own original design, which nothing
since has retired or refuted — it has only been deferred). This program has
now run six instrument/model-fidelity desk cycles in nine iterations
(20, 22, 23, 26, 27, 28), all of them real, all of them zero T1 escape route
— sharpening the numerical machinery around an ambient-contrast instrument
that has still never been asked whether its own *switch transient* clears
threshold. Constraint 4 cannot get a verdict, at either tier, until this
instrument exists. This is the largest remaining gap in the metrics table
PANEL.md itself specifies (line 144: "Switch transient at the observer | 4
(+3) | time-domain monitor series (stage 10, when built)") — LOGBOOK's own
T3 entry description, "instrument is stage-10 work, not yet built," is still,
word for word, true 20+ iterations after that line was written.

**(3–5), unranked relative to each other, all carried verbatim from this
cycle's own untouched queue (Iteration 28's items 2/3/5, none of which
exp-051 executed since it ran item 1):** the genuine FDTD `ABSORB` sweep at
the T21-vs-T24 geometry (T24's boundary systematic is now the sole
uncharacterized uncertainty source on this program's sharpest contamination-
risk cell family); the sub-degree angular sweep at 750nm/FWHM=2°/GEOM78
(motivated by exp-050's adjacent-cell threshold-breach finding, now doubly
motivated by this cycle's own confirmation that those same three cells are
exactly where the `|C(2n)|≥C_THR` clause fires outside `coherent`); and
THERMODYNAMICS' overdue `h_eff` re-derivation.
