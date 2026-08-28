# PHASE 5 — REVIEW · THERMODYNAMICS · Panel Iteration 62 · exp-085

*Fresh sub-agent, blind to any other seat's current-cycle Phase-5 review.
Read in full: PANEL.md, LOGBOOK.md (RULED OUT R1–R10, ESTABLISHED, LIVE
THREADS, full T28 arc Iterations 46–61 including both Checkpoint entries),
`phase1_proposal.md`, all five Phase-2 critiques, `phase2_redteam_audit.md`,
`phase3_synthesis.md`, `phase4_derivation.py`, `derivation_results.json`,
`NOTES.md`.*

## 0. Independent re-derivation performed before reviewing

All numbers below were recomputed from the committed `derivation_results.json`
and, where the record itself does not persist enough to check a claim, by
re-executing the committed code — never accepted from NOTES.md's prose.

**Headline figure 1 — `rel_dev(P_wide, P_fft) = 0.628`.**
`P_wide = 3.2556390977443606`, `P_fft = 8.754371395917975` (both read
directly from `derivation_results.json::method_a.p_wide_deg` /
`method_b.p_fft_deg`). Using this sub-thread's own established convention,
stated explicitly in `phase1_proposal.md` §4 (`rel_dev(a,b) = |a−b|/b`, and
confirmed as the literal `rel_dev()` function in `phase4_derivation.py`):
`|3.2556390977443606 − 8.754371395917975| / 8.754371395917975 =
0.6281127507039039`. **Reproduces to the printed digit.** (Note for the
record: this is *not* the same quantity as the `>10%`-of-mean disagreement
test the classification code actually gates on — `|P_wide−P_fft|/mean =
0.9157` — a different, larger number computed from the same two inputs. Both
are internally consistent with their own stated formulas; NOTES.md's
`rel_dev=0.628` and the code's own `METHOD DISAGREEMENT` trigger are two
different, correctly-labeled statistics about the same pair, not a
contradiction — worth stating explicitly since two "disagreement" numbers
sitting in the same paragraph is exactly the kind of adjacent-figure
confusion R9 exists to flag if left unlabeled. NOTES.md does label them
correctly.)

**Headline figure 2 — "4/10 sampled sub-windows have circular-shift pass
rate ≥40%."** Recomputed directly from `derivation_results.json::
method_c.sub_results[*].circular_shift_null.fraction_meet_or_exceed` for
the 10 entries carrying a null: `{5°:0.867, 13°:0.067, 21°:0.633, 29°:0.033,
37°:0.600, 45°:0.600, 53°:0.000, 61°:0.167, 69°:0.000, 77°:0.000}`. Count
`≥0.40`: exactly **4/10** (θc = 5°, 21°, 37°, 45°), matching NOTES.md
exactly, and the bimodal 6-low/4-high shape NOTES.md describes ("the other
6/10... show LOW pass rates (0%, 0%, 0%, 3%, 7%, 17%)") reproduces precisely
against these same values, not a rounded gloss.

**Headline figure 3 — the "29.8s of a 2353s run" elapsed-time claim
(NOTES.md's "Learned" item 3).** This number is **not** stored as a field in
`derivation_results.json` — it exists only as a `print()` line in
`phase4_derivation.py`'s Method C block, and no run log was committed
anywhere in this experiment's directory (checked: no `.log`/`.txt`/`.out`
file exists). This means the committed record alone cannot verify it — a
real, if minor, gap in what R4 asks a permanent figure to rest on. Because
Method C's own inputs and code are fully deterministic and committed, I
independently re-executed the identical 37-sub-window-fit + 10-null-sample
loop (reusing `FastEval`/`free_period_with_widening`/`circular_shift_null`
from the committed `phase4_derivation.py`, unmodified) on this same machine:
**elapsed = 29.66s** — matching NOTES.md's "29.8s" to within run-to-run
noise, not a hand-typed guess. **Verdict: the figure is genuine (produced by
actually invoking the committed function, satisfying R4's substance), but
it is not independently *checkable from the committed artifacts alone* —
only by re-running deterministic code that happens to be cheap enough to
re-run. That is a real gap for a more expensive figure (the 2259.8s
Method-A-null elapsed time cited alongside it is NOT independently
re-verifiable within a reasonable review budget) and should be closed
forward, cheaply: persist per-stage elapsed times as JSON fields (as
`circular_shift_null()` already does for each null call) rather than
`print()`-only, so a future reviewer can check a timing claim by reading,
not re-running.** This is a disclose-forward finding, not a load-bearing
defect — nothing in this cycle's own Combined reading depends on the exact
value of "29.8s" being right to the tenth of a second.

**Specificity control**: `n_clear=0/60` on `(P_wide, R²_wide)` — reproduces
exactly against `derivation_results.json::specificity_control_wide`.

**Method C reference-angle correction (Fix 3) and Fix-4/Fix-5 decision
logic**: independently re-derived the algebra
(`p_local_corrected = p_local_reported_at_39 · cos(39°)/cos(θc)`) against
`phase4_derivation.py`'s own `Tc_wrong`/`p_local_corrected` lines — correct,
matches Red Team's Phase-2 specified fix exactly. Traced the
`classification_a` branch logic by hand against the actual numbers
(`frac_recovered=1.0`, `spread=9.259`, `rho=0.882`,
`null_pass_rate=0.40`): the `elif` chain correctly lands on `"STRONG
COHERENT CHIRP"` before the reliability-downgrade `if` block runs, and that
block's own guard (`classification_a == "STABLE"`) is not met, so no
downgrade fires — **NOTES.md's own claimed spec gap (§Result (a)) is real,
independently confirmed from the code, not an interpretive dramatization of
an intentional design.**

## Steel-man

This is the cleanest-executed cycle in the T28 sub-thread's recent run.
Every one of Red Team's 7 mandatory fixes is genuinely implemented in
`phase4_derivation.py` (confirmed by reading the code, not the prose
describing it) — the circular-shift null on `c_wide` is exhaustive (3900/3900
offsets, not a subsample), Method C's reference-angle bug is fixed with the
exact algebra Red Team specified, the 4-band precedence and STRONG-CHIRP
cell close both demonstrated gaps, and the FFT is Hann-tapered. Git
provenance is clean and in the correct order (`phase1_proposal.md` →
critiques → Red Team audit → `phase3_synthesis.md` → `phase4_derivation.py`
→ run+NOTES, each its own commit) — a third consecutive cycle (083, 084,
085) restoring the discipline that lapsed at 081/082. The `FastEval`
performance optimization is verified bit-identical at 7 spot-check angles
before use, disclosed as a mechanical speedup only. Most notably: NOTES.md
discloses its own spec's blind spot (the un-downgraded STRONG COHERENT CHIRP
classification) rather than silently patching it post hoc or smoothing it
into a clean headline — exactly the R8/R9 discipline this program has had to
learn the hard way, applied here proactively, by the same Director role,
without a Red Team catch forcing it.

## Sharpest critique

The cycle's own central finding is scientifically inconclusive by its own
design, and NOTES.md is honest about that — but the two numbers actually
computed for question (a) point in tension with each other in a way the
frozen spec left genuinely unresolved, not just under-specified. The STRONG
COHERENT CHIRP reading (`frac_recovered=1.0`, `rho=0.88`, `p=6×10⁻¹³`) is
statistically overwhelming *if the underlying local fits are trustworthy* —
but 4 of the 10 sampled sub-windows are, by this cycle's own null test,
statistically indistinguishable from smoothness alone at a rate
(40%–87%) comparable to the exact precedent (50%) that sank the *narrow*
window's SUPPORT verdict one cycle ago. This is not merely "Phase 5's job to
resolve" (as NOTES.md frames it) — the spec-gap that let it ship un-adjudged
is itself the kind of pre-registered-decision-table hole R5's/R10's own
lineage exists to close before Phase 4 runs, and this cycle had four
independent seats explicitly warn (Phase 2) that the mandatory null was the
whole point, and the fifth mandatory-fix item that should have closed this
gap (Fix 2, extending the null to Method C) shipped without a
corresponding decision rule for what a failed null means for a *non-STABLE*
classification. That is a genuine, if narrow, repeat of the family-of-gaps
R5/R10 target: a control was added, but the control's own consequence for
every reachable outcome cell was not exhaustively specified before the run,
the identical shape (if smaller in stakes) as the very MECE gaps this same
cycle's Fix 4/Fix 5 were built to close in §4(b)/§4(a).

## NOTES.md §Next item 3 — premature or well-earned?

Assessed directly, against R4/R9 standards, as instructed. **Well-earned, on
balance, and correctly scoped and hedged** — this is not a premature
characterization masquerading as caution. Three reasons: (1) it is phrased
as a question for Phase-5/Checkpoint-2 to decide ("may itself be worth
folding in... not this Director's to pre-empt"), not asserted as settled;
(2) it is precisely scoped to "how far the edge-diffraction mechanism class
can be pushed *with a single-tone description*" — not a blanket claim that
the mechanism itself is bounded, which would directly contradict this same
cycle's own Fix 7 (Method A/B are stationarity-assuming instruments that
cannot, on their own, distinguish "no periodicity" from "genuine chirp too
broadband for a single-tone fit," per PHOTONICS's Phase-2 point, confirmed
by Red Team); (3) the underlying numbers are genuinely striking on their own
terms regardless of the chirp question's resolution — `R²_wide=0.0128` sits
inside the null's own middle (45.4% of shifts meet/exceed it), `0/60`
specificity targets clear, and the FFT's own largest peak over the *full*
spectrum sits at `140°`, entirely outside the primary `[1°,15°]` range — a
global single-tone description of this curve fails by every instrument this
cycle built, independent of whether Method C's chirp reading survives
adjudication. **One caveat for whoever picks this up**: the "boundary"
framing must carry Fix 7's own non-veto logic forward explicitly if it is
folded into T28's permanent record — a future cycle citing "Method A/B found
nothing" without also citing "and that is expected under a real chirp
hypothesis, not evidence against one" would silently drop the qualifier that
makes this cycle's own finding honest, repeating the exact confound
PHOTONICS flagged at Phase 2.

## Verdict: **PARTIAL**

Matching this sub-thread's own established Combined Verdict vocabulary.
Checkpoint criterion 2 (mechanism-class boundary) is correctly N/A — this is
instrument-fidelity/model-characterization work, no constraint-3 scene, no
absorption mechanism proposed anywhere in the record. **Checkpoint criterion
4 does not fire.** The one candidate — a fourth consecutive cycle without
the full joint EM/THERMO energy-interception cross-check — is explicitly,
correctly disposed of in `NOTES.md` §Next item 4 ("this cycle did not touch
Checkpoint criterion 4's own named cause"), continuing exp-084's own
Red-Team-instructed practice of stating the scope-mismatch precisely (a
second consecutive zero-FDTD/no-article-scene desk cycle, structurally
unable to run the full check, not a discretionary skip) rather than leaving
it silent — this is compliance, not a fourth silent miss. My own energy/
detectability charter finds nothing to attach a sidecar to this cycle either
(no material, no absorbed power, no article anywhere in scope) — the T1:N/A
scoping is honest.

## My ranked top-3 for Iteration 63

1. **Resolve this cycle's own self-disclosed spec gap FIRST, before citing
   any of exp-085's positive findings elsewhere**: extend the circular-shift
   null to all 37 of Method C's sub-windows (NOTES.md's own item 2 — now
   known to cost ~30s total, confirmed by my own re-run above) and, this
   time, pre-register what a ≥40%-pass-rate sub-window contributes to
   `frac_recovered`/`spread`/`ρ` (exclude it? downweight it? flag the whole
   STRONG-COHERENT-CHIRP cell UNRELIABLE if any fraction of sampled windows
   fail?) *before* rerunning — closing the exact gap this review's sharpest
   critique names, and answering NOTES.md's own "Phase 5's first job"
   directly with data rather than argument.
2. **Persist per-stage elapsed times as JSON fields, not print-only**, for
   any future cycle reusing this cost profile — a one-line forward fix
   costing nothing, closing the gap in headline-figure §0 above before a
   more expensive timing claim (hours, not seconds) is cited somewhere it
   cannot be cheaply re-verified.
3. **On my own charter's standing item**: the joint EM/THERMO
   energy-interception cross-check has now gone two consecutive cycles
   (084, 085) structurally unable to run for lack of an article-loaded FDTD
   scene. Iteration 63 should either deliberately select a cycle that
   *does* carry a real article-loaded scene so this finally runs in full
   (ending the scope-mismatch streak Red Team named at Iteration 61), or, if
   another zero-FDTD cycle is chosen, continue this cycle's own good
   practice of stating that disposition explicitly rather than let the item
   go stale by inertia a third time.
