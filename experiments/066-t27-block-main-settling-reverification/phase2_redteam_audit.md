# RED TEAM — PHASE 2 FINAL AUDIT · Panel Iteration 43 · Candidate exp-066

*Seat 7, RED TEAM. Independent re-verification performed on every load-bearing
claim below — none accepted on a critique's word alone. Preserved verbatim as
delivered.*

## 0. What I independently re-verified

- `experiments/041-t20-angle-audit/results.json::block_main` — read
  directly: **exactly 30 rows**, θ∈{36,37,38,39,40}×{±}, λ∈{450,600,750}.
  No 35°. The Phase-1 proposal's factual claim about exp-041's own code is
  correct.
- `experiments/065-t24-absorb-boundary-sweep/
  settled_sweep_steps2800_diagnostic.json` — keys confirm C40/±35°/±38°/
  ±40°×3λ (18 cells) at STEPS=2800, all 5 configs. **±35° data at
  STEPS=2800 already exists, committed, for the identical unpadded C40
  (=exp-041/024) geometry.**
- `experiments/065-.../phase4_results.md`'s Phase-5-correction §2 table —
  confirms C40/θ=−35°/600nm and /750nm values are **already committed at
  STEPS=1400 too** (`+0.00112→−0.00440`, `−0.00095→+0.00552`). So
  ±35°×3λ has committed data at **both** STEPS=1400 and STEPS=2800, for
  the exact anchor geometry — already in the repo, before exp-066 runs
  anything.
- `lab/caveat_lint_config.json` — read in full. Entry
  `exp065-steps1400-unsettled-plane-channel`'s `candidate_globs` =
  `[LOGBOOK.md, PLAN.md, experiments/*/NOTES.md, experiments/*/phase*.md,
  experiments/041-t20-angle-audit/*.md,
  experiments/042-t21-magnitude-bridge/*.md]`.
  `experiments/034-floor-convergence-scale-bridge/REALIZABILITY_MEMO.md`
  matches **none** of these patterns (confirmed by direct `fnmatch`
  reasoning, and by reading `lab/caveat_lint.py`'s own matching logic:
  `candidate_globs`+`trigger_terms` is how the tool discovers
  *undisclosed* citation sites beyond `required_sites`).
- `REALIZABILITY_MEMO.md` — read in full. Amendment 1's D_req≈537–600×
  "lower bound" language is explicitly built on the off_pass PASS→
  MARGINAL downgrade, which `experiments/041-.../NOTES.md` itself states
  was produced by "the N17 quadrature (±35° fallback plus the SAME
  excluded ±40° pair)." **MATERIALS' claim is confirmed exactly**, down
  to the ±35° inclusion.
- `PLAN.md` line 2279–2280 and `LOGBOOK.md` line 13469–13471 (T27 entry)
  and 13490–13491 ("Ranked top-3 for Iteration 43") — all three
  independent statements of the actual Iteration-43 mandate read,
  verbatim: **"Re-verify `experiments/041-t20-angle-audit`'s own
  MAIN-block ±35°/±38°/±40° rows at STEPS≥2800."** The word "MAIN-block"
  here is being used loosely for "the near-grazing angle standard this
  program cites," and it explicitly names ±35°.
- `lab/fdtd2d.py:132–183` — `ramp = int(ramp_periods * self.lam /
  self.S)`. At 750nm (cpl=25), ramp ≈ 3.0×25/0.700 ≈ **107 steps**.
  Cross-checked against exp-042's own already-established causal-transit
  figure (`r_edge=784.4` cells, `S=0.700`): transit time to first
  arrival ≈ 784.4/0.700 ≈ **1121 steps**. Ratio ≈ **10.5×** — about
  **one** order of magnitude, not the "two orders of magnitude" EM's
  critique states (a minor overstatement of EM's own arithmetic) — but
  the qualitative point is confirmed and, more importantly, sharper than
  EM argues: this program **already has a better, established, citable
  candidate mechanism on the books** for exactly this residual (exp-042
  Phase-5, PHOTONICS' finding: T21's fit residual `c*` trends
  monotonically worse toward 750nm, tracking the λ-dependent
  *periods-of-settling-margin* figure — 13.0/9.8/7.8 periods at
  450/600/750nm, thinnest at 750nm — not Yee-grid dispersion). The
  Phase-1 proposal cites `phase4_results.md`'s ramp-based candidate
  mechanism but never engages this stronger, already-committed
  alternative from the same experiment family.
- `PLAN.md`/`LOGBOOK.md` R_contact history — confirmed: ranked #1 since
  Iteration 40, deferred Iteration 41 (`length_provenance`) and
  Iteration 42 (T24), with Iteration 42's own Red Team text pre-naming
  "a third consecutive deferral would itself be worth flagging at
  Iteration 44." THERMODYNAMICS' count is correct.

## 1. Numbered attacks

**1. [inconsistency, load-bearing] The proposal's §2 scope-definition
quietly narrows the actual Iteration-43 mandate, not just "resolves an
ambiguity."** The proposal argues Block MAIN (exp-041's own
`MAIN_ANGLES={36-40}`) is "textually distinct" from ±35° and excludes it
from the 38-call closure. That claim about exp-041's own code is correct
(verified: 30 rows, no 35°). But the thing this cycle exists to execute
is not exp-041's internal naming — it is Iteration 43's own ranked-#1
queue item, which is stated **three separate times, verbatim, in the
committed record** (`LOGBOOK.md` T27 entry, `LOGBOOK.md` "Ranked
top-3," `PLAN.md`'s queue) as **"MAIN-block ±35°/±38°/±40° rows."** The
mandate already named ±35° explicitly; the proposal's "resolved rather
than inherited" framing silently substitutes a narrower reading without
disclosing that it departs from the mandate's own text. This is the
load-bearing form of VISION's attack — sharper than VISION's own
framing, which argued from cost/stakes rather than from the mandate text
itself.

**2. [inconsistency, resolves the EM/VISION budget tension] VISION's own
costing of its ask is wrong, and correcting it dissolves the apparent
EM-vs-VISION conflict.** VISION priced folding in ±35° at "+6 calls,"
implying it competes with EM's 2-call reallocation for the same 38-call
pool. Independently verified (§0): exp-065's own C40 config — "the
unpadded, 19-iteration anchor geometry," i.e. exp-041's own construction
— already has ±35°×3λ committed at **both** STEPS=1400 and STEPS=2800
(12 numbers total, in `results.json`/`settled_sweep_steps2800_
diagnostic.json`). Folding ±35° into this cycle's closure costs **zero
new FDTD calls**, only a desk-level citation. EM's and VISION's asks do
not conflict for budget; they compose.

**3. [inexpressible→resolved by evidence, confirmed with a correction]
EM's causal-transit arithmetic is right in substance, off by a factor in
magnitude, and understates its own strongest form.** See §0: ramp≈107
steps vs. transit≈1121 steps is ~10.5× (one order of magnitude), not
two. Flagged, not load-bearing to EM's conclusion. What **is**
load-bearing: the proposal's candidate mechanism for the 750nm residual
(P-066-3, ramp-based) ignores the *better* mechanism this program's own
exp-042 record already established for the same phenomenon
(periods-of-settling-margin, thinnest at 750nm). A falsification test
scored against the wrong candidate mechanism is weaker evidence than the
proposal presents it as.

**4. [unfalsifiable, confirmed] P-066-4's CONFIRM interpretation, as
characterized, risks reproducing exp-065's own already-self-caught
failure mode (Block MINI/P-VIS42-10) one level up, at the T21-fringe-fit
level.** Confirmed against `experiments/065-.../phase4_results.md`/
`phase5_redteam_audit.md`: this program's own record already states the
settling-vs-coherent-fringe discrimination is UNDECIDED, precisely
because both the settling artifact and the T21 diffraction fringe are
governed by geometrically related quantities (transit distance,
`A·cosθ`). A recovered R² after settling correction does not, by
itself, distinguish "the diffraction mechanism is real" from "the
settling artifact's own θ,λ-dependence happens to correlate with the
fringe model's clock." QUANTUM's flip (strip causal language, attach the
tripwire verbatim) is correct and free.

**5. [inconsistency, load-bearing, confirmed] MATERIALS' citation-
reachability gap is real and specifically targets the memo's own
weakest, most load-bearing empirical foothold.** `REALIZABILITY_MEMO.md`
is unreachable by `caveat_lint_config.json`'s
`exp065-steps1400-unsettled-plane-channel` entry (neither
`required_sites` nor `candidate_globs` cover it — confirmed by direct
glob comparison and by reading `lab/caveat_lint.py`'s matching logic).
The gap is not cosmetic: Amendment 1's D_req≈537–600× "lower bound"
language is calibrated from the N17-quadrature off_pass downgrade, which
by exp-041's own text includes ±35° — an angle this cycle's own
predecessor (exp-065) already showed sign-flips under settling
correction. **This does not threaten the memo's ultimate
UNOBTANIUM-WITH-PARAMETERS verdict** (independently confirmed: that
verdict rests on RSA's 1–2 OOM dynamic-range gap and TPA's 9–12 OOM
irradiance gap, both stated by the memo itself as independent of D_req's
precise value) — but it is exactly the class of undisclosed-downstream-
citation gap this cycle's own charter exists to close, sitting in the
one document the mechanical tool cannot find.

**6. [inconsistency, minor, confirmed] THERMODYNAMICS' "third
consecutive deferral" count is correct and currently undisclosed.**
Verified against `PLAN.md`/`LOGBOOK.md`: R_contact deferred at Iteration
41 and 42, with Iteration 42's own record pre-naming a third deferral as
worth flagging. Exp-066 as drafted would be that third deferral,
unnamed.

**7. [not found — overreach check] None of the five critiques is
overreach.** Every attack above is independently verified against a
primary artifact, not relayed. THERMO's/MATERIALS'/QUANTUM's fixes are
all one-sentence-to-one-paragraph, zero-FDTD-cost. EM's and VISION's
calls compose once VISION's cost estimate is corrected (attack 2).
Nothing here should be struck.

**8. [confirmed non-issue, for completeness] No constraint-#1/2/3/4
violation anywhere.** T1 escape route is genuinely NONE (verified: no
σ(I)/σ(x,t)/ε(ω)/gain parameter appears in `design_geometry.py`'s
proposed reuse of exp-065's own `CONFIGS["C40"]` harness). No `lab/`
diff proposed. This is pure instrument re-verification, structurally
identical to exp-041/042/065's own T1-NONE precedent.

## 2. Overall ruling

**PROCEED-WITH-MANDATORY-FIXES.**

Not DO-NOT-PROCEED: every defect found is a scoping/labeling/citation
gap in an instrument-trust cycle that touches no mechanism, no `lab/`
code, and no constraint metric — exactly the class of issue this
program's own house discipline (Phase 2 critique, same-shift correction)
exists to catch and fix, not to kill a cycle over. Not PROCEED-AS-IS:
attack 1 (the mandate-narrowing) and attack 5 (the memo's reachability
gap) are both load-bearing and both independently verified — shipping
the proposal as drafted would silently under-deliver on Iteration 43's
own explicit mandate text and leave a real citation gap in place.

### Reconciled mandatory-fix docket (for the Director to apply at Phase 3)

**A. Scope — fold in ±35° at ~$0 marginal cost (resolves attacks 1 and
2).**
- Retain: G-1′ extension, 18 calls, {36,37,39}°×{±}×{450,600,750}nm @
  STEPS=1400.
- Retain: MAIN-2800, 18 calls, {36,37,39}°×{±}×{450,600,750}nm @
  STEPS=2800.
- **Add, zero new FDTD calls:** cite exp-065's own committed C40/±35°×3λ
  values at both STEPS=1400 (`results.json`, Block SWEEP) and STEPS=2800
  (`settled_sweep_steps2800_diagnostic.json`) directly. One desk-only
  consistency line, not a new gate: confirm these 12 already-committed
  numbers read correctly and are labeled as covering the ±35° leg of the
  mandate's own "±35°/±38°/±40°" text.
- Net: the closure now genuinely covers the full mandate-named angle set
  (±35° through ±40°, all 3λ, both STEPS) at the same 36-call core cost.

**B. λ×θ generalization — augment, don't swap (resolves attack 3).**
Given the proposal's own cost framing ("minutes, not hours"), don't
trade away the 750nm confirmatory point; add to it:
- 40°/750nm/C40 @ STEPS=4200 and 5600 (2 calls, as originally proposed —
  keeps the λ-axis discriminator intact).
- **Add:** 37°/600nm/C40 @ STEPS=4200 (1 new call) — the cheapest
  available interior-angle convergence check, giving a genuine second
  (θ,λ) point on the settling-generalization claim, not just a second
  harness-reproducibility point.
- Total stress-test block: 3 calls (was 2).

**C. P-066-4 relabeling (resolves attack 4, zero cost).** Strip causal
language from P-066-4's CONFIRM/REFUTE interpretation. Replace with a
strictly statistical statement (R² recovery/non-recovery only). Attach
QUANTUM's own exp-065 forward tripwire verbatim, extended: no future
citation of this refit's R² may be read as "confirmed edge-diffraction/
coherent-fringe mechanism" while Block MINI's period-match test
(P-VIS42-10) remains UNDECIDED.

**D. Citation-scoping widening (resolves attack 5, zero cost).** Widen
`lab/caveat_lint_config.json`'s `exp065-steps1400-unsettled-plane-
channel` entry: add `experiments/034-floor-convergence-scale-bridge/
REALIZABILITY_MEMO.md` to `candidate_globs`, **and** widen
`trigger_terms` to include terms the memo actually uses (`off_pass`,
`N17`, `D_req`, `537`, `540.{0,5}600`) — glob-only widening without
trigger-term widening would not actually make the tool find the
passage. Given attack 5's substance is confirmed load-bearing, do this
rather than declaring the memo unaffected on the record.

**E. R_contact disposition sentence (resolves attack 6, zero cost).**
One sentence in §2, per `experiments/041-.../NOTES.md` item 5's own
template: name R_contact explicitly, state this is a third consecutive
deferral (Iteration 41→42→43), note it is orthogonal desk/literature
work that never competed with this cycle's FDTD budget.

**Total: 39 new FDTD calls** (18+18+3, up from 38), plus 12
already-committed values cited at $0, plus two config-file edits and one
wording fix — all inside the proposal's own "minutes, not hours" cost
envelope. No mandatory fix requires killing or restructuring the core
G-1′/MAIN-2800 design.

## 3. Checkpoint criteria (per PANEL.md's five)

- **Criterion 1** (passes all constraint metrics): does not fire — no
  constraint metric is scored this cycle; T1 confirmed NONE.
- **Criterion 2** (proven mechanism-class boundary): does not fire — no
  mechanism class is touched.
- **Criterion 3** (engine physics beyond validated bench classes): does
  not fire — zero `lab/` diff proposed beyond one config-registry entry
  (D above), which is data, not engine code; reuses exp-065's own
  already-validated `CONFIGS["C40"]` harness verbatim.
- **Criterion 4** (program-integrity drift): **does not fire, conditional
  on this docket actually landing at Phase 3** — mirroring this
  program's own Iteration-19 ("mandatory same-shift erratum... not
  program-integrity drift, PROVIDED the erratum is applied this same
  shift") and Iteration-42 ("does not fire, conditional on a 3-item
  mandatory-fix docket landing") precedents. This is Phase-2, pre-freeze
  critique catching a real scope-narrowing and a real citation gap in a
  Phase-1 draft — exactly the mechanism this program's blind-critique
  design exists to run, not a defect that shipped undetected. Checked
  specifically against the one entry with a hardened "any further gap
  auto-fires" tripwire in this program's history
  (`exp061-t18-evidentiary-tier-propagation`): that lineage is unrelated
  to this cycle's findings, and `exp065-steps1400-unsettled-plane-
  channel` (the entry implicated here) is newly created at exp-065 with
  no such hardened clause — normal Phase-2/3 discretion applies. If the
  Director ships exp-066 without A–E landing, that is the fact pattern
  that would fire criterion 4 at a future Phase 5, not this audit.
- **Criterion 5** (two consecutive non-advancing iterations): does not
  fire — Iteration 42 clearly advanced the logbook (T27 opened); this
  cycle, once corrected, closes a load-bearing 19-iteration gap
  regardless of its own headline's outcome.
