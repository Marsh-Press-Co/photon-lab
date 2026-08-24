# RED TEAM — PHASE 5 FINAL AUDIT · Panel Iteration 43 · exp-066

*Seat 7, RED TEAM, fresh context, everything in hand. Every load-bearing
claim below was independently re-verified against primary artifacts
(results.json, git history, live tool execution, source code) — nothing
here is relayed on a seat's word alone. Preserved verbatim as delivered.
Verification trail: `results.json` recomputed by hand (gate G1, P-066-1/
2/3a/3b/4, closure_summary — all bit/near-exact matches);
`lab/caveat_lint_config.json` read and executed live (`python3 lab/
caveat_lint.py --only exp065-steps1400-unsettled-plane-channel`);
`lab/fdtd2d.py::_damping` read directly; `CPL` dict read directly; git
log/diff on the config file; LOGBOOK.md's exp-057/exp-059/T23 precedents
and REALIZABILITY_MEMO.md's D_req framing read directly.*

## 0. Headline verification result

Every numeric claim any of the six seats made about this cycle checks
out. Gate G1: 18/18 bit-exact (`Δ=0.0`, verified). P-066-1: median
0.005767, max 0.009575 (verified). P-066-2: exactly 3/18 flips, at
(−39°,450), (39°,750), (−39°,750) — **confirmed all at 450/750nm, none at
600nm**, exactly as PHOTONICS reported. P-066-3a/3b: ratios 9.76e-5 and
7.17e-6 respectively (verified). P-066-4: sign_agree 30/30, r²(c*)=0.8271,
Δ=+0.0418 (verified). closure_summary: 36 cells, 31→34 fails, 5 bucket
flips (verified, and I independently re-derived the flip table from raw
data — matches phase4_results.md exactly). No seat overstated a number.

## 1. Numbered findings on the cycle as a whole

**F1. [inconsistency, load-bearing, MUST FIX] `caveat_lint_config.json`'s
`exp065-steps1400-unsettled-plane-channel` entry is genuinely stale on
its own description, independent of the git-diff that landed this
cycle.** Confirmed by reading the entry directly and by `git log -p`:
this cycle's only edit (commit `1a90ecf`) touched `trigger_terms`/
`candidate_globs` (mandatory fix D, reachability only). The entry's
**description** still reads as if Block MAIN is wholly unsettled
("pending re-verification," "until Iteration 43 or later closes it")
with no acknowledgment that Iteration 43 — this cycle — closed it. This
is not a hypothetical gap: `phase4_results.md` itself explicitly says the
entry "should be updated (a Phase-5/close-of-cycle task, not this Phase-4
file's own scope)." We are at that point now. PHOTONICS' and VISION's
flags are both correct, and MATERIALS' separate claim (fix D works, 0
required-site failures) is also independently confirmed — these are two
different, both-true findings, not competing claims. VISION's further
point — `trigger_terms` don't distinguish Block MAIN (now closed) from
Block ARTICLE (still open), so a future citation of Block ARTICLE-as-
settled wouldn't trip anything — is also confirmed by inspection of the
term list.

**F2. [inconsistency, minor, non-blocking] `phase4_results.md`'s "Closure
summary — the concrete answer to 'how many citations are affected'"
header over-promises.** Its content is cell-coverage counts and the
GATE_HARD bucket-flip table; the actual citation enumeration lives in the
next section, "Downstream citation scope." Confirmed by direct read.
Cosmetic.

**F3. [process/disclosure gap, recommended] `phase4_results.md` never
states GATE_HARD (0.001, scored this cycle) is a different, stricter bar
than VISION's own perceptual `C_THR_LAB` (0.005).** Confirmed:
`results.json`'s own `gates` dict carries `C_THR_LAB: 0.005` and
`C_THR_FIELD: 0.02`, neither of which is ever named in
`phase4_results.md`'s prose. Also confirmed: Block MAIN's 36–40° window
sits outside `FALLBACK_ANGLES` (the N9 set is 5°-step, 0→±35°, excluding
±40°, per exp-041's own design_geometry.py convention) — only the ±35°
leg overlaps the scored aggregate. VISION's finding is accurate and not
overclaimed by VISION; the "GATE_HARD fails increased" headline is
numerically correct and does not move a constraint-3 verdict, but an
unfamiliar reader could conflate the two. Cheap, one-sentence fix.

**F4. [interpretive imprecision, my own finding, recommended] MATERIALS'
Phase-5 claim — that the GATE_HARD-fails-increase is "evidence-consistent
with" REALIZABILITY_MEMO's D_req-as-lower-bound framing — is directionally
defensible but loosely grounded.** I cross-checked the 5-cell bucket-flip
table against the N9/`FALLBACK_ANGLES` set myself: of the 5 flips, only
**one** (−35°/750nm, PASS→FAIL) is actually inside the aggregate that
feeds `off_pass`/D_req. The other four (36–39° cells) are outside it —
the same fact VISION independently established but did not cross-
reference against MATERIALS' claim. The interpretive link survives, but
only through that single cell, not through the aggregate GATE_HARD count
MATERIALS cites in support of it. Worth narrowing before this becomes a
written memo amendment.

**F5. [inconsistency, already resolved in-cycle, no action needed] EM's
"two orders of magnitude" ramp-vs-transit arithmetic was a real
overstatement, already caught and fixed by this cycle's own Phase-2 Red
Team audit** (ramp≈107 steps, transit≈1121 steps at 750nm/cpl=25 → ~10.5×,
one order of magnitude — I re-derived this myself from `lab/fdtd2d.py` and
confirmed it). Noted only because the Phase-5 EM review states this
correctly; flagging so it isn't miscounted as a new defect.

**F6. [unfalsifiable — checked, none found] P-066-4's causal-language
discipline holds completely.** I read `results.json::fringe_fit_
refit.statistical_only_note` and the corresponding `phase4_results.md`
prose directly, including the borderline c*-shift sentence QUANTUM
flagged ("consistent with (not proof of)... this cycle does not
adjudicate that reading"). Correctly hedged throughout, in both the
machine-readable field and the prose — QUANTUM's own Phase-5 conclusion
is accurate.

**F7. [constraint-#N-violation — checked, none found] T1 escape route is
genuinely NONE.** Verified against `design_geometry.py`/`run.py`: no
σ(I), σ(x,t), ε(ω), or gain parameter appears anywhere; the only `lab/`
file touched is the data-only `caveat_lint_config.json`. No constraint
metric is scored this cycle, so no constraint-1/2/3/4 exposure is
possible in this cycle's own scope.

**F8. [process, escalation — see §6/§7] R_contact's third consecutive
deferral (Iteration 41→42→43) is disclosed correctly** (verified verbatim
in `results.json::r_contact_disposition` and NOTES.md mandatory fix E).
Not a violation — but see the lock ruling below.

**Overreach check:** none of the six seats' findings is overreach. Every
attack traces to a primary artifact I could independently confirm. The
closest thing to overreach is EM's "build a predictive WKB/adiabatic-
taper model" (their #3) — real and legitimate, but a much bigger ask than
this cycle's gap-closing scope warrants; I rank it below the concrete
items, not off the table.

## 2. Load-bearing vs. recommended vs. overreach

**Load-bearing (must fix before close):** F1 (the caveat_lint entry —
three independent seats found this, `phase4_results.md` itself named it
as due now).

**Recommended, non-blocking:** F2, F3, F4, VISION's minor provenance-note
point (the −35°/750nm flip vs. +38°/600nm flip), QUANTUM's phrase_pattern
widening (bare "r2_cstar"/"0.8271"/"30/30").

**Overreach:** none found.

## 3. Reconciled ranked top-3/4 for Iteration 44

**#1 — LOCK: R_contact, unconditional, for Iteration 44.** This is a
ruling, not just a ranking — see §6. This program has an explicit,
exercised precedent: `Q_ext(x)` (exp-059) and
`graded_black_shell_flagship` (exp-057) were both granted unconditional,
rotation-breaking locks after **exactly 3 deferrals**, the program's
lowest-ever bar, both independently re-verified by me against LOGBOOK.md
directly. R_contact will have 3 deferrals (Iterations 41, 42, 43) at this
cycle's close, meeting that same bar, and this program's own record
already pre-named a 4th as "worth flagging." It is desk/literature work
on `lab/thermo_sidecar.py`'s analytic Biot formula — structurally
orthogonal to any FDTD budget (MATERIALS' point, verified: nothing here
competes for the same resource as item #2). Iteration 44 is MATERIALS'
turn by rotation regardless, so the lock costs nothing procedurally; it
only removes the option to defer a 4th time.

**#2 — Close T27's remaining settling gap in full**: interior
`FALLBACK_ANGLES` (0°,±5°,±15°,±25°) at STEPS=2800, Block ARTICLE's
article-**PRESENT** legs (not just the empty floor) at settled STEPS, and
Block EXTEND (41–43°) if budget allows. This is the highest-stakes item
still open in physics terms — Block ARTICLE is, per VISION's finding, the
only construction in this program's history that has ever produced a
scored constraint-3 PASS/MARGINAL number, and it remains unverified for
settling. Fold in EM's concrete, cheap addition: prioritize **39–40°/
450nm** as the convergence-check point, not another 37°/600nm-style test
— 450nm is the coarsest grid (`CPL={450:15,600:20,750:25}`, confirmed by
direct read) and the most grazing untested angle, and **zero** direct
multi-STEPS convergence data exists at 450nm anywhere in this record
(confirmed: this cycle's own stress tests were 40°/750nm and 37°/600nm;
exp-065's original point was 40°/600nm).

**#3 — Block MINI period-match test: build properly, or formally retire —
not a third deferral.** Before spending new FDTD budget, run QUANTUM's
proposed zero-cost desk check first: does this cycle's own 36-cell
settling-delta dataset already show `A·cosθ`-periodic structure matching
T21's period? That's a free second discriminator that could sharpen or
dissolve the need for the costlier redesigned FDTD test (≥2–3 T21
periods at ~0.2° spacing, at settled STEPS). This is now 2 consecutive
cycles of deferral-behind-relabeling (exp-065→exp-066); per this
program's own T23 precedent (closed by argument, then a further-deferral
tripwire explicitly pre-named), a 3rd would be worth flagging as
Checkpoint-4-adjacent — VISION's framing is appropriately hedged, not an
overclaim, and I adopt it as a forward note, not a firing.

**#4 (housekeeping, fold into whichever cycle runs next, non-blocking):**
verify the M1 caveat_lint edit actually reaches the correct state at
Iteration 44's own predict-freeze; if REALIZABILITY_MEMO.md is ever
amended to cite this cycle's GATE_HARD finding, ground it in the
−35°/750nm cell specifically (F4).

## 4. Checkpoint criteria — checked against all five, explicitly

- **Criterion 1** (passes all constraint metrics): does not fire — no
  constraint metric is scored this cycle.
- **Criterion 2** (proven mechanism-class boundary): does not fire — no
  mechanism class touched.
- **Criterion 3** (engine physics beyond validated bench classes): does
  not fire — zero `lab/` engine diff; the one touched file
  (`caveat_lint_config.json`) is a data registry, not code, and
  `run.py`'s own `_lab_diff_excluding_registry` assertion enforces this
  live.
- **Criterion 4** (program-integrity drift): **does not fire, conditional
  on the F1 fix (M1 below) actually landing before close.** This is the
  same disposition this program has repeatedly and correctly applied to
  "found before close, fixed same-shift" caveat-propagation gaps
  (Iterations 19, 23, 42, and this cycle's own Phase-2 audit). The
  distinguishing question — is this a "same-shift, still-fixable"
  non-firing precedent, or something worse? — resolves cleanly to the
  former: (a) this is Phase 5, i.e. the exact stage the process is
  designed to catch this class of gap at, not a gap that shipped past
  Phase 5 undetected; (b) `phase4_results.md` itself already flagged the
  update as due at close, so nothing was silently missed — it was
  explicitly deferred to exactly this point; (c) unlike the
  `exp061-t18-evidentiary-tier-propagation` lineage, this entry
  (`exp065-steps1400-unsettled-plane-channel`) carries no prior hardened
  "any further gap auto-fires" tripwire — it is one cycle old, and normal
  Phase-5 discretion applies (Red Team's own Phase-2 audit ruled this
  explicitly, and I independently confirm the reasoning). If the Director
  ships this cycle's close without M1 landing, **that** would be the fact
  pattern that fires criterion 4 at a future Phase 5 — not this audit
  finding it now.
- **Criterion 5** (two consecutive non-advancing iterations): does not
  fire — Iteration 42 opened T27; Iteration 43 closes its highest-stakes
  sub-item (Block MAIN, all 36 mandate-named cells) with all six of its
  own predictions confirmed. Clear, unambiguous advancement regardless of
  the housekeeping gap above.

## 5. Mandatory-fix docket (apply before LOGBOOK/PLAN/SESSION_LOG close)

**M1 (blocking).** Update `lab/caveat_lint_config.json`'s
`exp065-steps1400-unsettled-plane-channel` **description** (not just
`candidate_globs`/`trigger_terms`, which this cycle already widened) to
state explicitly: Block MAIN's 30 rows — all 36 mandate-named cells
(±35°/36°/37°/38°/39°/40°×3λ) — are now settled/closed as of exp-066/
Iteration 43 (G1 18/18 bit-exact, P-066-1/2/3a/3b/4 all CONFIRMED), while
Block ARTICLE's article-PRESENT legs, the four interior
`FALLBACK_ANGLES`, and Block MINI's period-match test remain open. Fold
in QUANTUM's zero-cost `phrase_patterns` widening (bare
`r2_cstar`/`0.8271`/`30/30` without "perturbation"). Re-run
`caveat_lint.py --only exp065-steps1400-unsettled-plane-channel` after
editing and confirm 0 required-site failures, as I did live.

**M2 (blocking, trivial).** Retitle or restructure `phase4_results.md`'s
"Closure summary" section so its header matches its content (F2).

**M3 (blocking, one sentence).** Add the GATE_HARD-vs-`C_THR_LAB`
distinction sentence to `phase4_results.md`, per VISION's finding (F3).

**M4 (ruling, not a fix).** LOGBOOK.md's Iteration 43 entry states
R_contact is **LOCKED, unconditional, for Iteration 44** (§3/§6).

Recommended, non-blocking, may land at Iteration 44: R1 (−35°/750nm vs
+38°/600nm provenance note), R2 (F4's narrowed grounding), EM's
WKB/adiabatic-taper model (queued behind the concrete items).

**Applied same-shift, verified before close (Director's note, appended
after M1–M3 landed): all three blocking fixes plus R1/R2 recommended
fixes were applied to `lab/caveat_lint_config.json` and
`phase4_results.md`; `caveat_lint.py --only
exp065-steps1400-unsettled-plane-channel` re-run and confirmed 0
required-site failures post-edit.**

## 6. On the R_contact lock

I grant THERMODYNAMICS' escalation request. This is within Red Team's own
established authority in this program — the exp-059 lock (Iteration 36)
and exp-057 lock (Iteration 34) were both granted this same way, by a
Phase-5 audit ruling on an escalation request at the 3-deferral mark. No
prior cycle pre-declared an explicit numeric lock-bar for R_contact
specifically (unlike `h_eff`, which had one set at 5), so this is a fresh
grant, not an automatic trigger — but the reasoning is identical to
precedent: R_contact is the only queued item that can *move* a number
(TD-5's 7.8× margin, this program's thinnest of any kind) rather than
relabel or disclose one, it has now been passed over twice by cycles
pursuing genuinely higher-priority work (T23 hardening, then T27), and it
costs nothing to lock since Iteration 44 is MATERIALS' turn by rotation
anyway.

## 7. Final verdict for exp-066: **PARTIAL**

I concur with the 5-seat majority (PHOTONICS/EM/THERMODYNAMICS/QUANTUM/
VISION) and decline to override to PROMISING on MATERIALS' single
dissenting vote, for reasons grounded in the cycle's own structure, not
vote-counting:

1. **T27 is only partially closed.** Block MAIN (36 cells) is closed
   cleanly, but three sub-items this program's own record names as part
   of the same thread — Block ARTICLE's article-present legs, the
   interior `FALLBACK_ANGLES`, Block MINI — remain explicitly open, by
   this cycle's own idealizations section, not by omission.
2. **The headline finding is double-edged, not a clean win.** GATE_HARD's
   own pass rate got *worse* at settled STEPS (31/36→34/36 fail), the
   opposite of a naive "unsettled=noisy" prior — a genuinely informative
   result, but one that required EM's own passivity/graded-damping-
   boundary explanation to make sense of, not a simple confirmation the
   way exp-064's guard build was.
3. **Real citation-hygiene work was explicitly left for this exact
   moment** (`phase4_results.md`'s own text: "a Phase-5/close-of-cycle
   task, not this Phase-4 file's own scope") — the cycle's own record
   acknowledges incompleteness at Phase 4 close, which is a different
   posture than exp-064's fully-closed, four-party-verified guard.
4. **Scope, by design, is narrower than the whole thread.** exp-066
   covers 36 of the cells relevant to T27's full closure; the mandate's
   own "scope exactly how many downstream citations are affected"
   question is answered honestly and well, but the answer is "some, not
   all, and here's what's still open" — that is itself a PARTIAL-shaped
   result, cleanly executed.

None of this diminishes the cycle's real accomplishment: six predictions
committed, six confirmed, a 19-iteration citation-exposure question
resolved for its highest-stakes 36 cells, with disciplined, independently
-verified statistical hygiene throughout. It is a clean, well-executed
PARTIAL — not a PROMISING physics finding, and not a RULED OUT (nothing
here forecloses a mechanism class or proves a constraint jointly
unsatisfiable). Close unblocked once M1–M4 land; Iteration 44 queue per
§3 above.
