# Phase 2 — RED TEAM final audit, Panel Iteration 79 (exp-102)

Fresh sub-agent. Received the complete packet: `phase1_proposal.md` and all
five `phase2_critique_{materials,em,thermodynamics,quantum,vision}.md`
files, plus PANEL.md, LOGBOOK.md's RULED OUT/ESTABLISHED/LIVE THREADS
sections and the full Iteration-76/77/78 narrative (R19-R21, the R20
firing), exp-101's `NOTES.md` and `phase5_redteam_audit.md`, and
`lab/sections.py`/`lab/fdtd2d.py` directly. Per charter #7 I defer to no
seat — every claim below (mine and the five critiques') is independently
re-derived from source, not restated.

---

## 0. What this cycle actually is, confirmed before attacking it

T1 route: **N/A**, confirmed — no σ(I)/σ(x,t)/angular-selectivity/
sub-threshold parameter appears anywhere in the parameter table; the
article is the byte-identical, already-LOCKED-UNOBTANIUM `graded_black_shell`
R4 construction. This is a diagnostic instrument build, matching exp-101's
own precedent exactly. No constraint (1-4) is scored this cycle by design
(no `C_thr(L)` comparison, no ambient scene). That scoping claim is
accurate — I checked the Predictions section line by line for a smuggled
threshold comparison and found none beyond the one prose overclaim in §4
(attack 4, below).

---

## 1. Ruling on each of the five Phase-2 critiques

**MATERIALS (support-with-changes) — CONFIRMED, elevated to mandatory.**
Independently re-verified the steel-man's own arithmetic: shell thickness
`(156-60)·15nm = 96·15nm = 1440nm` and `(78-30)·30nm = 48·30nm = 1440nm` —
identical; outer radius `156·15nm = 78·30nm = 2340nm` — identical. `SIGMA_R4_
CORRECTED=0.25` vs. the native flagship's `sigma_max=0.5` is consistent with
this (a factor-of-2 finer grid at constant physical optical depth needs a
factor-of-2 smaller per-cell σ), matching `design_geometry.py`'s own
documented intent, already established across exp-094–101. Gate B is
therefore a genuine same-article reproduction check, not a rescaled one.
The sharpest-attack claim (the UNOBTANIUM caveat is stated in Idealizations
but not required to travel into Result prose beside Prediction 1's
confirmation) is real: I read the full proposal and found no instruction
requiring this. Given the direct, on-the-books precedent this program has
already paid for once (R1's own Iteration-14 addendum, the ENZ
mischaracterization) and exp-101's own Change 6 (the T9 disclaimer required
to "travel...everywhere it is cited below"), this is not merely a nice-to-have
— see attack 6.

**ELECTROMAGNETISM (support-with-changes) — CONFIRMED, arithmetic verified
independently.** I recomputed the along-beam decomposition myself rather
than trusting EM's numbers:
`Δ = P_off - P = (0, 450)` in lab-frame coordinates; decomposed into the
proposal's own orthonormal basis `u(θ)=(-cosθ,sinθ)`, `v(θ)=(sinθ,cosθ)`
(confirmed orthonormal: `u·u=v·v=1`, `u·v=0`), the along-beam component is
`Δ·u = 450·sinθ` and the true-lateral component is `Δ·v = 450·cosθ`.
At θ=37.127246°: `sin(37.127246°) ≈ 0.60355` (interpolated from tables,
cross-checked against `450·0.60355=271.6`) — **matches EM's stated 271.6
exactly**. At θ=42.960901°: `sin(42.960901°) ≈ 0.68156`, `450·0.68156=306.7`
— **matches EM's stated 306.7 exactly**. I additionally computed the
lateral component EM did not state: `450·cosθ` ranges ≈358.8 (37.13°) to
≈329.4 (42.96°) — meaning the along-beam confound (271.6–306.7) is
**76%–93% as large as the intended lateral offset itself**, not a small
correction term. EM's arithmetic is exact and the finding is real: `P_off`
sits at a beam-axis distance of `D_STANDOFF + 450·sinθ` ≈ 471.6–506.7
cells, a genuinely different diffraction z-slice from `P(θ)`'s own 200
cells — 2.4–2.5× farther downstream. **This is exactly the fixed-lab-frame
failure shape this cycle exists to retire (`beam_behind_t28`, exp-100;
`back_frac`, exp-101), recurring one level down in the very cycle
commissioned to close it for the primary channel.** CONFIRMED, mandatory.

**THERMODYNAMICS (support-with-changes) — CONFIRMED by direct code read,
elevated to top-priority mandatory.** I read `experiments/101-.../run.py`
directly: line 78, `netd_row = exp095.netd_row`; line 222,
`cell_metrics_r4(...)` called unconditionally inside the main sweep loop;
lines 251-254, `pair_metrics_full`/`netd_row(pm)` called and asserted
present via `NETD_ROW_KEYS`. This is not a hypothetical import chain —
it is the actual, already-executed R4-family pipeline this proposal cites
repeatedly (`box_for_r4`, `ref_for_r4`, `R4_CONFIGS`, the six established
angles) as its own geometric foundation. `phase1_proposal.md` contains
**zero** occurrences of `netd`, `thermo`, `sidecar`, or `UNDETECTABLE`
(grepped directly). R21's own text: a **third** silent occurrence of "a
persisted byproduct field's own headline finding never stated in
Result/Learned prose" fires Checkpoint criterion 4 **automatically, no
further deliberation** — and exp-099/exp-100 are already R21's two
founding (non-firing) instances. If Phase 3 takes the path of least
resistance (reusing exp-101's `run.py` wholesale for the already-gated
`phasors`/`full_capture` machinery — the fastest route to exactly what this
proposal wants), `netd_row()` fires as an unplanned, silently-persisted
byproduct with zero Phase-1 acknowledgment it could even happen. This is
the single highest-consequence fix in this packet: an unforced,
easily-avoided path to an automatic Checkpoint-4 firing on the very rule
whose forward-elevating clause has never yet triggered a third time.
CONFIRMED, mandatory, top priority.

**QUANTUM OPTICS (support-with-changes) — CONFIRMED, mathematically
verified.** `I0_corrected(θ) = mean_y sqrt(Sx(y)²+Sy(y)²)` is a mean of a
strictly convex function (the Euclidean norm) of `(Sx(y),Sy(y))`. By
Jensen's inequality, for any non-constant random vector,
`E[‖X‖] ≥ ‖E[X]‖`, with equality **only** if `(Sx(y),Sy(y))` is constant
across the sampled `y` — a condition that fails whenever any ABC leakage,
edge-taper residue, or finite-sample ripple exists in the reference strip
(exactly the regime a real FDTD run produces, never exactly a plane wave
at a finite line). I confirmed this is a genuine, structural difference
from `i_inc = mean_y(Sx)`, a **linear** average that exactly cancels any
zero-mean ripple — the two expressions are mathematically NOT
interchangeable except in the degenerate constant-field limit. This means
`I0_corrected` is systematically biased **high**, and Gate C's own 1%
self-consistency check (`|I0_corrected·cosθ − i_inc|/I0_corrected ≤ 0.01`)
does not diagnose this bias — it could pass with both sides shifted by a
correlated amount, or fail while attributing the failure to "the
local-plane-wave assumption" (per Prediction 2's stated falsification
reading) when the real cause is an averaging-order artifact in the
reference calculation itself, not a physical breakdown of the plane-wave
approximation. This reproduces, structurally, the exact class of defect
(a hidden order-of-operations artifact silently corrupting the one
"absolute" number this instrument reports) that exp-101's own Learned
section names as the reason a phase-resolved instrument was needed in the
first place — recurring one level down, inside the fix meant to close the
prior instance of it. CONFIRMED, mandatory.

**VISION SCIENCE (support-with-changes) — CONFIRMED by direct text read on
both findings.** §4 states verbatim: "κ(θ) alone answers 'is this point
dark relative to what would be there with nothing in the way,' which is
constraint 1's witness question." This is a real overclaim: κ(θ) carries no
adaptation state, ambient regime, or `C_thr(L)` — Tier 2's conversion is
explicitly still unbuilt per this same document's own Idealizations
("Tier 2 / ... is future work, out of scope here"). Cheap, one-sentence
fix, VISION's own replacement text is adequate. CONFIRMED, mandatory. The
second finding (the "T3" mislabel recurrence) is addressed in its own
section below, per the Director's explicit instruction.

---

## 2. Numbered attacks

1. **[inconsistency]** The off-axis companion point conflates a lateral
   offset with a comparable-magnitude along-beam displacement
   (271.6–306.7 cells, independently re-derived above, matching EM's
   figures exactly at both checked angles). Prediction 3 (`κ_off≥0.90`)
   can pass or fail on Fresnel/diffraction structure at a **different**
   z-slice (2.4–2.5× `D_STANDOFF` downstream) rather than on whether the
   primary shadow is spatially localized — the stated purpose of the
   check. **MANDATORY.** Fix: EM's own proposed `P_off(θ) = P(θ) +
   Δ_lat·v(θ)` (pure beam-perpendicular offset, `a=0` by construction).

2. **[inconsistency]** `I0_corrected`'s mean-then-magnitude averaging
   order is a Jensen's-inequality-biased estimator on the one channel
   Gate C promotes to a *permanent* gate for every future absolute-
   intensity citation from this instrument (mathematically confirmed
   above — not a hypothetical). **MANDATORY.** Fix: QUANTUM's own
   proposed `I0_corrected(θ) = sqrt((mean_y Sx)² + (mean_y Sy)²)`,
   mirroring `i_inc`'s own established linear-mean convention.

3. **[inconsistency]** Silence on the thermal sidecar creates an unforced,
   easily-avoided path to an automatic R21 third-strike Checkpoint-4
   firing if Phase 3 reuses exp-101's `run.py` (confirmed by direct code
   read: `netd_row`/`cell_metrics_r4` execute unconditionally inside the
   exact pipeline this proposal's own geometry is drawn from).
   **MANDATORY, highest priority** — cheapest possible fix (one sentence)
   against the highest-consequence failure mode in this packet. Fix:
   THERMODYNAMICS' own proposed disposition sentence, stated before Phase
   3 freezes, not discovered after a run.

4. **[inconsistency]** §4's "which is constraint 1's witness question"
   is a perceptual claim not earned by a raw, adaptation-free,
   threshold-free ratio (confirmed by direct text read; contradicted by
   this same document's own Idealizations, which correctly scope Tier 2
   as unbuilt). **MANDATORY** — one-sentence fix, VISION's own text.

5. **[inconsistency]** The "T3" mislabel is reintroduced in Idealizations
   after exp-101's own Phase-5 correction explicitly dropped it (confirmed
   by direct text read: proposal line "the T3 build, exp-101's own
   corrected Next-item framing" cites the correction to justify the exact
   label the correction retracted). **MANDATORY but non-R20-firing** — see
   dedicated section 3, below.

6. **[inconsistency]** MATERIALS' caveat-travel gap: the
   UNOBTANIUM-WITH-PARAMETERS/"shallower-not-deeper" caveat is stated only
   in Idealizations, with no instruction requiring it to travel into
   Result prose beside Prediction 1's own headline confirmation — the
   identical shape of gap this program already paid for once (R1's own
   Iteration-14 ENZ addendum: a locked-unrealizable article's optical
   response read, in isolation, as informative about real-coating
   darkness) and the identical discipline exp-101's own mandatory fix 6
   (the T9 disclaimer) already established as this program's own house
   style one cycle ago. **MANDATORY** — one sentence in the Result-writing
   instructions, per MATERIALS' own proposed fix.

7. **[inconsistency] (my own finding, independent of the five critiques)**
   — Gate A over-claims its own diagnostic power, an R18-adjacent gap in
   a brand-new suite stage's founding gate. Gate A compares the
   already-planned empty-scene capture "against itself" ("zero marginal
   FDTD... compared against itself") — meaning both legs of the κ
   computation read the *same* underlying field array through the *same*
   `P(θ)`-construction code path. A bug that computes `P(θ)` incorrectly
   (a wrong sign in `Δx=-D·cosθ`, an off-by-one in the rounding, a wrong
   `H_REGION` block boundary) would corrupt numerator and denominator
   **identically** in this self-comparison, still yielding κ=1.0 to
   float64 precision — Gate A can only ever catch an *asymmetric*
   treatment between the `with_article=True` and `with_article=False`
   extraction code paths, not a geometric-placement bug in the new
   rotating-frame `P(θ)` construction itself, which is this cycle's own
   single most novel piece of code (precondition (b), the whole reason
   this instrument exists rather than reusing `beam_behind_t28`'s fixed
   window). Gate B does not close this gap either: it exercises `P(θ)`
   only at θ=0°, where the proposal's own text states "the beam-aligned
   frame trivially reduces to the lab frame" — i.e., Gate B is
   constructed to NOT exercise the rotating-frame arithmetic at all. **As
   proposed, no gate in suite stage 24 independently validates the
   rotating `P(θ)` construction at any of the six nonzero angles this
   cycle actually tests.** Not R18 itself verbatim (that rule concerns a
   check joining an *already-partially-verified* layered architecture;
   stage 24 is wholly new), but the same underlying principle this
   program has repeatedly re-derived (R6, R18): a check's claimed scope
   must be independently confirmed against what it can actually detect,
   and a genuinely new measurement class needs at least one check that
   can fail for the right reason. **MANDATORY** — add a fault-injection
   positive control to Gate A or B: e.g., deliberately perturb `P(θ)` by
   a known cell offset (or an independently hand-computed `Δx,Δy` at one
   nonzero angle, verified against raw `Sim` grid coordinates the same
   way `_verify_box_margins()` already does for box geometry) and confirm
   κ changes measurably — cheap, zero additional FDTD calls (post-
   processing on already-captured fields), and closes the one class of
   bug this new instrument's own core contribution is most exposed to.

8. **[inconsistency] (independent finding, non-mandatory)** — Gate B's
   `κ(θ=0°) ∈ [0.005, 0.05]` band is asymmetric in linear terms (0.33×
   to ~3× the established 1.5–1.8% target) but is in fact close to
   symmetric in log-space (≈0.48 decades below, ≈0.44 decades above) —
   I checked this specifically as a candidate R17 concern and it clears:
   a genuinely different quantity (point/region field ratio vs. window
   envelope-ratio) reasonably earns an order-of-magnitude tolerance, and
   the proposal discloses this is "not an exact-match bar." **No fix
   required** — noted for the record so a future reviewer does not
   re-raise it without checking the log-space symmetry first.

9. **[inconsistency] (independent finding, non-mandatory)** — Prediction
   4's factor-of-3× point-vs-region agreement band is loose, but
   defensibly so: near a genuine shadow the ratio's *numerator* can be
   small and noisy while the *denominator* (`|Ez_empty|²` in vacuum) is
   well-behaved, so a generous band for "does this matter at all" is a
   reasonable Phase-1 choice, to be tightened only if real data
   motivates it. **No fix required.**

---

## 3. The VISION "T3 mislabel recurrence" — dedicated ruling

**Confirmed as a real, genuine, single, isolated citation defect — and
confirmed NOT to approach R20's "three or more" bar, on two independent,
sufficient grounds, checked separately rather than assumed:**

**(a) Wrong phase to count at all.** R20's own adopted text (LOGBOOK.md
lines 799-844) requires defects "surviving a document's own Phase-3
prediction-freeze into its Result/Learned sections, **each caught only at
Phase 5** — not earlier." This defect is being caught right now, at Phase
2, before any Phase-3 freeze has happened. R20 exists to penalize a
citation-hygiene pattern that escapes this program's own five-blind-plus-
Red-Team review layers until after the document is frozen and results are
in; catching it here, at exactly the stage the process is designed to
catch it, is the system working as intended, not a near-miss of it
failing. A defect fixed before freeze never "survives... into Result/
Learned" at all.

**(b) Wrong section, independently precedented one cycle ago on the exact
same fact pattern.** Even setting aside (a): this mislabel lives in
Idealizations (and would, if uncorrected, likely persist into a future
Next section) — never in Result or Learned. This is not my own
interpretive judgment; it is **the identical ruling Red Team's own
Phase-5 final audit made one cycle ago, on this exact same "T3"
sentence's own first appearance** (exp-101 `phase5_redteam_audit.md`
§1.2, Candidate 5): "it lives in Idealizations (frozen at Phase 1/3) and
Next (post-run) — never in Result or Learned. R20's text is specific to
'Result/Learned sections'... This does NOT count toward R20's tally... a
legitimate scope exclusion under R20's own specific text." I re-read that
ruling in full and it applies to this cycle's recurrence with no
modification needed — same phrase, same section-scope logic, same
disposition.

**Could it combine with other citation/label defects this cycle to
approach the bar regardless?** I checked for other citation/label defects
in this proposal specifically (beyond the five critiques' own findings,
none of which are R4-class citation-restatement errors — they are design/
formula defects, a different category) and found none: every other
numeric citation I independently checked (exp-101's `Q_ext≈1.54–1.56`,
`REALIZABILITY_MEMO.md` Amendments 6-7, exp-001's `beam_behind=1.5-1.8%`,
`FLOOR_FRAC=0.10`'s exp-088 origin, the shell-thickness/outer-radius
identity) reproduces exactly from its cited source. **This is a single,
isolated instance, with no combinable siblings on file this cycle** —
ruling R20 risk **not fired, not close, not trending toward the bar**, on
both textual grounds independently. Standing forward caution, not a
current finding: if this mislabel (or any of attacks 1-4/6-7 above) is
left unfixed through Phase 3 and survives, unedited, into a frozen Result/
Learned section discovered only at Phase 5, THAT would begin building
toward R20 density in a way this Phase-2 catch currently forecloses —
exactly why fixing it now, at the cheapest possible stage, matters.

---

## 4. Mandatory fixes before Phase 3 synthesis (ranked)

1. **[Attack 3]** State the thermal-sidecar disposition explicitly —
   either "not invoked this cycle" (with exp-101/exp-057's standing
   UNDETECTABLE citations as the disposition covering this proposal's
   configs) or "invoked; will be narrated in Result per R21" — before any
   Phase-3 implementation choice is made. Highest priority: cheapest fix,
   highest-consequence failure mode (an automatic Checkpoint-4 R21
   third-strike).
2. **[Attack 1]** Replace `P_off(θ) = (P_x(θ), P_y(θ)+450)` with a purely
   beam-perpendicular offset, `P_off(θ) = P(θ) + Δ_lat·v(θ)`, so
   Prediction 3 tests localization at matched downstream distance.
3. **[Attack 2]** Replace `I0_corrected(θ) = mean_y sqrt(Sx²+Sy²)` with
   `I0_corrected(θ) = sqrt((mean_y Sx)² + (mean_y Sy)²)`.
4. **[Attack 7]** Add a fault-injection positive control to suite stage
   24 (Gate A or a new Gate) that independently exercises the rotating
   `P(θ)` construction at a nonzero angle against a hand-verified
   reference coordinate — not merely a self-comparison at the same
   (possibly wrong) point, and not only at θ=0° where the rotation is
   trivial.
5. **[Attack 4]** Replace "which is constraint 1's witness question" with
   VISION's proposed "constraint 1's *physical* transmission question — a
   necessary but not sufficient input to the witness's actual percept..."
6. **[Attack 5]** Strike "the T3 build" from Idealizations; state the
   Tier-2 conversion plainly as constraint 1's own missing conversion
   (matching exp-101's own corrected Next-item language exactly, not a
   paraphrase that reintroduces the retracted label).
7. **[Attack 6]** Add one line to the Result-writing instructions:
   require the UNOBTANIUM-WITH-PARAMETERS/"shallower-not-deeper" caveat
   to be stated inline beside Prediction 1's κ(θ) confirmation text, not
   only cross-referenced via Idealizations.

**Non-mandatory / deferred (no fix required, checked and cleared):**
attack 8 (Gate B band width — log-symmetric, defensible); attack 9
(Prediction 4's 3× band — defensible given near-null noise behavior).

None of the seven mandatory fixes requires a re-run, a new mechanism, a
`lab/` diff, or a re-scoping of the experiment's core design — all are
formula corrections, one geometry-construction correction, one new
zero-marginal-FDTD gate, and prose-level commitments, exactly the shape
of fix this program's Phase 3 synthesis routinely adopts without
returning to Phase 1.

---

## 5. Verdict

**PROCEED-WITH-MANDATORY-FIXES.** This proposal, once the seven fixes
above are adopted at Phase 3, is fit to synthesize into a committed
Phase-3 configuration. It is not sent back to Phase 1: every defect found
(mine and the five critiques', independently re-verified above) is a
formula, geometry-construction, gate-coverage, or prose-level fix, not a
flaw in the instrument's core design (a same-point coherent-phasor ratio,
correctly immune to the `i_inc`/cosθ artifact by construction, correctly
scoped as diagnostic-only, correctly T1: N/A). The design's central idea —
reading the already-gated complex phasors at a rotating downstream point
instead of an incoherent box-flux integral — is sound and directly
responsive to exp-101's own Learned-section mandate. The defects found are
exactly the kind of "known before Phase 4, therefore free to fix" issues
Phase 2 exists to surface.

---

## 6. Checkpoint criteria — explicit statement

**Criterion 4 (program-integrity drift) does NOT fire from this critique.**
Checked explicitly, not assumed:

- The T3 mislabel is real but, per §3 above, categorically excluded from
  R20's tally on two independent grounds (wrong phase — caught at Phase 2,
  not Phase 5; wrong section — Idealizations/Next, not Result/Learned),
  each sufficient alone, both already precedented on this exact fact
  pattern by exp-101's own Red Team audit one cycle ago.
- No other citation/label defect on file this cycle combines with it —
  checked and found none (§3).
- Attacks 1, 2, 3, 6, 7 are design/formula/gate-coverage defects, not
  R4-class citation-restatement failures — a different category R20 does
  not address, and none of them constitutes a quietly-dropped constraint
  (T1 is honestly N/A; constraints 1-4 are honestly out of scope this
  cycle, not silently abandoned mid-claim).
- No PASS/FAIL verdict, constraint claim, or scored prediction exists yet
  for any defect to corrupt — this is Phase 2 of a Phase-1 proposal; the
  process is intercepting these issues at the cheapest possible point,
  which is the opposite of drift.

**Criteria 1, 2, 3, 5 — N/A, confirmed rather than assumed.** No
constraint-satisfying configuration is claimed (1); no mechanism-class
boundary is proven or claimed (2, T1 route N/A); zero `lab/` diff is
proposed anywhere in this document (3); this is Iteration 79, one cycle
after Iteration 78's own genuinely logbook-advancing result — no
two-consecutive-null pattern exists or is at risk from this cycle alone (5).
