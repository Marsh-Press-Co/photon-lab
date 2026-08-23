# Phase 5 — ELECTROMAGNETISM blind review of exp-062 results (Panel Iteration 39)

*Fresh sub-agent, no memory of the cycle that proposed this experiment (a
different EM instance led Phase 1). Blind to every other seat's own
current-cycle Phase-5 review, per PANEL.md's fresh-context rule. Charter:
field/wave behavior, impedance matching, energy coupling — reciprocity/
passivity/causality bookkeeping, formalizing what T1 permits and forbids.*

**Read in full**: `PANEL.md`; `LOGBOOK.md` (RULED OUT, ESTABLISHED, and the
complete T1–T26 Live Threads section line-by-line, plus a full read of the
Iteration-38 entry and a targeted search across the rest of the file for
every prior mention of thin-film/Airy/black-matrix/n_eff/Salisbury-screen
content — none found outside Iteration 38, confirming this cycle's Section-4
physics is genuinely new to the record, not a restatement); `PLAN.md` lines
1–100 and ~1890–1990; this cycle's full record (`phase1_proposal.md`, all
five `phase2_critique_*.md`, `phase2_redteam_audit.md`, `phase3_synthesis.md`,
`NOTES.md`, `phase4_results.md`); `experiments/034-.../REALIZABILITY_MEMO.md`
Entry 2 in full; `lab/caveat_lint.py` (full source) and
`lab/caveat_lint_config.json` (all six live entries) — and I ran the tool
live against the current working tree rather than trusting any prior
party's report of its output (see §5).

---

## 1. Independent re-verification of the closed-form physics

### 1.1 Airy stack, passivity bound, R-vs-T factor — re-derived, unchanged

I re-ran every numeric claim in Sections 4.1–4.3 from scratch (own script,
not copied):

```
tau_T = 6.907755...  alpha_T = 6.9078e4 cm^-1   ratio = 1.20344
tau_R = 3.453878...  alpha_R = 3.4539e4 cm^-1   ratio = 0.60172
bound(T) = 2e^-tau_T = 0.0020   (0.20%)
bound(R) = 2e^-tau_R = 0.0632   (6.32%)
```

All match the Phase-1/Phase-2/Phase-4 printed digits exactly. The
underlying physics is standard and correctly applied: `r_stack`'s Airy
expansion for `|r₂₃|e^{-τ}≪1`, the passivity fact `|r₁₂|,|r₂₃|≤1` for any
lossless-*or-lossy* passive interface (this is genuinely a reciprocity/
passivity bookkeeping fact, not an assumption specific to this material —
it follows from `R+T+A=1` and `A≥0` at each interface taken as its own
two-port), and the R-vs-T double-pass geometric factor (an ordinary
ray-optics consequence of a reflectance-based OD encoding a round trip).
**Nothing in Phase 3 or Phase 4 weakened this core derivation.** The
mandatory-fix docket's Phase-3 additions (the measurement-geometry
conditioning on EM-3, the THERMO/QUANTUM disclosures) are additive
caveats, not edits to the Section-4 math, and I confirm none of them
touches the algebra in 4.1–4.3.

### 1.2 The EM-3 "structurally inapplicable" claim — correctly reasoned in
substance, overstated in wording

This is the specific claim my brief asks me to scrutinize:
`phase4_results.md`'s EM-3 result states that because query 14 establishes
the LCD-era black-matrix OD is measured **in transmission, through a
transparent, unbacked substrate**, "the entire Salisbury-screen/
critically-coupled-resonance mechanism... is **structurally inapplicable**,
not just disfavored by a broadband reading."

**The core inference is sound and the sourced fact supports it for the
purpose it's used for.** A meaningful, non-trivial transmission-based OD
(T=10⁻³ at OD=3, not T≈0 by construction) can only be measured if the
substrate assembly is not backed by a highly reflective/opaque layer at
the time of measurement — if it were, "transmission" would be undefined
or trivially zero regardless of the coating's own absorption. So "no
reflective backing in this measurement geometry" is a legitimate inference
from "this is a well-defined transmission measurement," not an assumption
smuggled in. And Section 4.4's specific mechanism — a Salisbury-screen/
critically-coupled absorber reaching *near-total absorption* via
destructive interference of light reflected off the film's own two
interfaces — genuinely **requires** a near-unity-magnitude back reflection
to null the front-surface reflection to near zero. A bare, low-index-
contrast dielectric substrate (photoresist `n≈1.5–1.7` on glass `n≈1.5`)
cannot supply that; `|r₂₃|` there is small (a few percent at most), nowhere
near the `|r₂₃|→1` this mechanism's critical-coupling condition needs. So
ruling out Section 4.4's *specific* near-total-absorption-via-critical-
coupling reading, for *this* OD figure, on *this* evidence, is correct EM
reasoning, not an overreach of the sourced snippets.

**Where the wording overstates it: "structurally inapplicable," read
literally, invites the conclusion that *no* coherent/interference
contribution of any kind is present in this transmission-mode geometry.**
That is not established, and is not quite true even in principle — any
two-or-more-interface dielectric stack (air/photoresist/glass/air here)
supports weak Fabry–Perot-style transmission ripple from partial
reflections at each interface, independent of whether a *strong* reflector
exists anywhere. The correct, precisely-scoped statement is narrower than
what shipped: **the strong-resonance/critical-coupling mechanism of §4.4
cannot operate here (no interface with `|r|` anywhere near the ceiling
assumed), so whatever residual coherent contribution this geometry does
support is not a *separate*, newly-ruled-out-or-in regime — it is exactly
the regime EM-1's own passivity bound (§4.3) already covers and already
showed small (≤0.2% at τ=6.91).** In other words: the sourced fact
(unbacked, transmission-mode) answers "is the *large*, resonance-driven
alternative live here?" (no) — it does not separately answer "is *any*
coherent correction present?" (answered already, and independently of the
backing question, by EM-1's own math). `phase4_results.md` conflates these
two facts into one absolute claim. This does not change EM-4's headline
number: `1.20×` stands as a checked point estimate either way, since
EM-1's own bound already shows the maximum possible correction (even under
the ceiling `|r₂₃|→1`, which real photoresist-on-glass indices fall far
short of) is ≤0.2% at this τ — negligible against the ~20% precision this
program's own falsification bar for EM-1 uses. **Net: EM-4's substantive
conclusion is unthreatened; the specific sentence in `phase4_results.md`
should be tightened at Phase 5 close** (see mandatory-fix recommendation,
§6) so a future reader does not read "structurally inapplicable" as license
to treat this geometry as interference-free by construction rather than
as bounded-small by EM-1's own already-computed ceiling.

### 1.3 A new finding: EM-6/EM-7's OD→α conversion silently drops the
R-vs-T distinction Section 4.2 itself established

This is not raised by any of the five Phase-2 critiques or Red Team's
Phase-2 audit (both predate Phase 4, before EM-6/EM-7 had numbers to
check) — a genuine Phase-5 catch.

EM-6 (NiP-black) and EM-7 (carbon/graphene aerogel) both convert a
**reflectance** figure (R≈0.5–5% for NiP, R<0.24% for aerogel) to an
implied α via `OD=−log₁₀(R)`, `τ=OD·ln10`, `α=τ/thickness` — with **no
÷2 correction**. But Section 4.2 is this proposal's own load-bearing
result: *a reflectance-based OD encodes a double pass through the
absorbing layer, so the correctly-inferred single-pass τ is HALF the
naively-computed value.* That correction was applied to the black-matrix
candidate (Section 4.2, ultimately mooted by EM-2's finding that the
actual convention there is T-based) but is **not applied, or even
mentioned, for EM-6/EM-7**, even though both are explicitly reflectance
figures.

I recomputed both ways:

```
NiP,  R=1.00%, t=10µm:  alpha(no /2)=4605 cm^-1   alpha(with /2)=2303 cm^-1
NiP,  R=1.00%, t=45µm:  alpha(no /2)=1023 cm^-1   alpha(with /2)=512  cm^-1
Aerogel, R=0.24%, t=1mm: alpha(no /2)=60.3 cm^-1  alpha(with /2)=30.2 cm^-1
```

Applying Section 4.2's own R-based halving would **push both classes'
implied α further below the target** (NiP: 11–56× short becomes 22–112×
short; aerogel similarly) — the falsification conditions were "not
triggered" under the reported (uncorrected) numbers and stay not-triggered,
more so, under the corrected ones. **This does not change EM-6/EM-7's
verdict or MATERIALS' pending tier interpretation** — if anything it
strengthens the "further from target" reading — but it is a real,
undisclosed methodological inconsistency: the same document applies its
own R-vs-T bookkeeping to one candidate and silently skips it for two
others measured the identical way (reflectance). It is also worth flagging
as a *conceptual* mismatch, not just an arithmetic one: NiP-black and
carbon aerogel reflectance figures are diffuse/hemispherical measurements
off effectively semi-infinite, porous, multiply-scattering media — not a
thin coherent film on a defined backing at all. Section 4's whole Airy-
stack apparatus (built for a two-interface coherent film) does not
obviously license *either* the T-based or the R-based-halved conversion
for this geometry class; a Kubelka–Munk-style diffuse-reflectance/
absorption relation would be the physically correct tool, and neither this
proposal nor `phase4_results.md` invokes one. **Recommended mandatory fix
for Phase 5 close**: disclose, in `NOTES.md`/`phase4_results.md`, that
EM-6/EM-7's α figures are an order-of-magnitude engineering estimate under
an unstated single-pass convention, not a rigorous application of
Section 4's own coherent-film framework — and note (for the record) that
the R-based correction, if applied, only widens the gap.

---

## 2. EM-5's three-geometry table — correctness and completeness

**Correctness: verified.** I recomputed every `ratio = gap/(λ/2π)` figure
independently (own script) for all three sourced geometry classes (query
11's stainless-steel-characterization D=65/93nm; query 12's directly
co-sourced r=60nm/f=11%/gap≈196.2nm; query 12's spin-capable-forest
directly-stated gaps of 47nm/64nm) and match `phase4_results.md`'s printed
digits to the last decimal in every case I checked.

**Completeness — two real gaps, neither conclusion-changing:**

1. **The table omits the 600nm bench-wavelength column for the two
   query-11 rows** (shown as `—`), even though the pre-registered
   falsification condition is scored "at all three bench wavelengths
   (450/600/750nm)." I filled the gap by direct computation:
   `ratio@600 = 2.017` (D=65nm) and `2.886` (D=93nm) — both comfortably
   `>1`, consistent with (and interpolating cleanly between) the reported
   450/750nm values, since `ratio∝1/λ` is monotone. **The omission is
   sloppy but harmless**: monotonicity guarantees the missing point cannot
   flip either row's conclusion. Still worth a same-shift fix so the table
   is actually complete against its own stated scoring bar, not merely
   correct by lucky monotonicity.

2. **The falsification condition, read literally, appears to have fired,
   and the verdict softens it to PARTIAL rather than FALSIFIED.** NOTES.md's
   own pre-registered condition: *"Falsified if Phase 4's actual sourced
   pitch/diameter figures give `ratio≥1` at any of the bench's three
   wavelengths."* Two of the three sourced geometry classes (the
   stainless-steel-characterization forest at any reasonable packing
   fraction, and the directly co-sourced r=60nm/f=11% forest) give
   `ratio≥1` at every one of the three bench wavelengths. Under the bar's
   own unconditional wording ("at any... wavelength," from any sourced
   figure), this condition is met — the strict, pre-registered scoring is
   **FALSIFIED**, not PARTIAL. `phase4_results.md`'s own more nuanced
   reading (mixed, geometry-class-dependent, one class still confirms) is
   the *more scientifically useful* characterization of what was actually
   found, and I do not think the underlying physics conclusion needs
   revising — but this program has repeatedly disciplined itself (R4;
   the recurring "no softening a pre-committed bar after the fact" theme
   running through T10, the Iteration-6/12 falsification-bar episodes,
   and Red Team's own standing rule against relabeling verdicts once a
   condition's letter is met) against exactly this move: relaxing a
   binary pre-registered condition into a softer tier once the actual
   result turns out more complicated than the prediction anticipated.
   **The honest fix is not to re-litigate PARTIAL vs. FALSIFIED after the
   fact, but to note explicitly, for the registry, that the pre-registered
   condition as worded did not anticipate a multi-geometry, class-dependent
   outcome, and to word any FUTURE multi-geometry near-field prediction so
   it pre-specifies how a mixed result across sourced geometries scores**
   (e.g., "FALSIFIED only if the program's own actual record-blackness
   comparator class gives ratio≥1," rather than "any sourced figure").

3. **The deeper, still-open gap `phase4_results.md` itself discloses and I
   confirm on independent read of the record: none of the three sourced
   geometry classes is the record-blackness/Vantablack-class CNT forest
   this program's own `α_true`/MP-1/MP-2 figures were actually drawn
   from.** The near-field-coupling question is therefore genuinely
   unresolved for the comparator class that matters — a real, disclosed,
   not-papered-over evidentiary gap, and (per §4 below) my top-ranked
   candidate for Iteration 40.

---

## 3. Verdict: **PROMISING**

The core EM contribution (Sections 4.1–4.3, EM-1/EM-2) is sound, cleanly
re-derived twice already (Phase 1 self-check, Phase 2 Red Team) and a
third time here, and genuinely closes two real open sub-claims from
exp-061's own MP-3/MP-4 finding: the R-vs-T basis (now pinned,
transmission-based, by two independent sourced queries) and the
resonance-vs-bulk-absorption question (correctly resolved against the
resonant-absorber alternative for the reasons in §1.2, even if the
`phase4_results.md` wording overstates the resolution slightly). The
cycle also delivers real, useful, non-tier-moving value: two new
falsifiable comparator classes with sourced numbers (NiP-black — the
closest real-material match this program has ever found, 6.9×–31×
thickness gap; carbon/graphene aerogel — the worst, 694×–3472×), and a
3+-cycle-standing citation (`n_eff=1.04+0.01i`) finally pinned to a title.
None of the issues I found (§1.2's wording overclaim, §1.3's undisclosed
EM-6/EM-7 methodology gap, §2's falsification-bar softening, §5's second
candidate_globs blind spot) change any verdict, tier, or headline number —
every one of them is a scoped, cheap, same-shift-fixable correction, in
exactly the register this program's own precedent (Iterations 10, 12, 32,
36, 37, 38) treats as PROMISING-preserving self-catches, not PARTIAL-
forcing defects. `exp061`'s own UNOBTANIUM-WITH-PARAMETERS tier is
untouched and, on the R-vs-T/resonance axis specifically, more solidly
grounded than before this cycle ran.

---

## 4. Top-3 ranked candidate directions for Iteration 40+

1. **Pin the actual record-blackness/Vantablack-class CNT forest's own
   inter-tube pitch/diameter** — the single most consequential open item
   this cycle leaves behind (§2.3). Every α figure this program's own
   realizability line (`α_true`, MP-1, MP-2, the standing THERMO
   disposition's `l_geometric_m`) is built from traces to a Bruggeman/
   effective-medium fit on forests of *this* class, not the three
   generic/application-specific geometries this cycle actually sourced.
   With the `n_eff=1.04+0.01i` citation now finally pinned to a title
   (*Carbon*, 2018, vol. 129, pp. 8–14), a targeted follow-up search
   naming that paper and its own citing literature directly, rather than
   generic "CNT forest pitch/diameter" queries, is the concrete next step
   — zero FDTD cost, reuses this cycle's own machinery unchanged. This
   also directly answers the THERMO-flagged dependency (§ mandatory fix
   4/idealization 9 in this cycle's own NOTES.md): whether `l_geometric_m`
   rests on a licensed homogenization cannot be settled without knowing
   whether *this specific* forest class sits in the near-field-coupling
   regime.
2. **The re-filed numeric-consistency-check tool, now a mandatory
   Director rider at Iteration 40 (PLAN.md, Red Team's exp-062 docket item
   6) — I endorse this priority and widen its scope by one class.** This
   cycle independently demonstrates a *third* instance of a related but
   distinct bug shape: not a single cited NUMBER drifting across sibling
   files (the originally-scoped case), but the **same conversion
   methodology (R-vs-T optical-density-to-α) applied two different ways in
   one document** without cross-reference (§1.3). Whoever builds this tool
   should consider whether its scope needs to extend from "does this
   NUMBER match its own earlier value" to "does this DERIVATION recipe get
   applied consistently to structurally-identical inputs" — a harder,
   more valuable check, and one this cycle's own EM-6/EM-7 gap is a live,
   concrete test case for.
3. **Widen `exp061-thermo-length-scale-staleness`'s `candidate_globs`**
   — my own finding, detailed in §5 below: the identical structural blind
   spot that just fired Checkpoint criterion 4 for this entry's sibling
   (`exp061-t18-evidentiary-tier-propagation`) exists, live and
   demonstrated (not hypothetical), in this entry too. Cheap, mechanical,
   same-shift fixable — should not wait for a third recurrence the way the
   T18-propagation lineage did before its own tripwire hardened.

EM-5's own open geometry-class question (item 1 above) should take
priority over the numeric-consistency tool (item 2) if only one can run
next: it bears directly on whether this program's own standing α/thickness
anchors rest on a licensed approximation, a physics question with a real
chance of moving a verdict; the tooling items are process debt, real and
overdue, but not verdict-bearing on their own.

---

## 5. A second, live-demonstrated Checkpoint-4-shaped gap (not the T18
lineage's own auto-fire tripwire — a sibling entry, same defect shape)

I ran `python3 lab/caveat_lint.py` against the current working tree myself
(not merely reading the audit's claim that it passes) — all 6 registered
caveats currently show **0 required-site failures**, confirming the
Iteration-39 mandatory-fix docket's registry-widening for
`exp061-t18-evidentiary-tier-propagation` genuinely works as claimed.

But inspecting the **sibling** entry opened the *same iteration* (38) by
the *same* mandatory-fix docket — `exp061-thermo-length-scale-staleness`
— I found it carries the **identical structural defect** that fired
criterion 4 for its sibling, live, not hypothetically:

- Its `candidate_globs` is `["LOGBOOK.md","PLAN.md",
  "experiments/*/NOTES.md","experiments/061-.../*.md"]` — a generic
  pattern only for `NOTES.md` files, plus an exp-061-specific catch-all.
  **It has no generic pattern that can discover a `phase2_critique_*.md`,
  `phase3_synthesis.md`, `phase5_review_*.md`, or `phase2_redteam_audit.md`
  file belonging to any experiment other than exp-061** — exactly the
  "cannot discover a [file type] belonging to any experiment other than
  the one that spawned the entry" shape Red Team's Section-3 ruling used
  to fire criterion 4 for the T18-propagation entry.
- This is not a future risk: **this cycle's own `phase2_critique_
  thermodynamics.md`, `phase2_redteam_audit.md`, and `phase3_synthesis.md`
  all already discuss `l_geometric_m` and this entry's own margin figures**
  — I confirmed by direct read (all three quote or restate "margin
  1.35×–3.79×" or "`l_geometric_m`... `τ_true/α`") — and I confirmed live,
  by running the tool, that **none of the three appears anywhere in this
  entry's WARN/candidate output.** They happen to already carry the
  correct phrase (so no live defect exists *today*), which is why the
  tool's own "already carries the caveat, not a gap" logic silently
  passes them by rather than flagging a failure — but that same logic
  means a **future** edit to any of these file types, at any future
  experiment, that got the margin figure wrong would be **completely
  invisible to this tool**, exactly the failure mode Checkpoint criterion
  4's tripwire mechanism exists to close.

**I am not the seat that adjudicates whether this fires Checkpoint
criterion 4** — Red Team's own hardened tripwire text names the
T18-propagation entry specifically, and I do not read its "no further
deliberation" auto-fire language as extending automatically to a
different-though-sibling entry. But under PANEL.md's general criterion-4
standard ("program-integrity drift... a constraint quietly dropped"), on
ordinary judgment rather than the specific auto-fire clause, I believe
this independently qualifies: it is the *same* defect shape, opened by the
*same* mandatory-fix docket, discovered in the *same* iteration (39) that
already convened Marsh once for the sibling gap. I flag it here for Red
Team's own ruling, per this program's standing practice, rather than
deciding it unilaterally. **Recommended same-shift fix regardless of the
Checkpoint ruling**: widen `exp061-thermo-length-scale-staleness`'s
`candidate_globs` with generic patterns (e.g.
`experiments/*/phase2_critique_*.md`, `experiments/*/phase3_synthesis.md`,
`experiments/*/phase5_review_*.md`, `experiments/*/phase2_redteam_audit.md`,
or simply `experiments/*/*.md`) mirroring exactly what was just done for
its sibling entry.

---

## 6. Mandatory-fix recommendations for this cycle's own Phase-5 close

1. Tighten EM-3's `phase4_results.md` wording (§1.2): scope "structurally
   inapplicable" explicitly to the near-total-absorption/critical-coupling
   mechanism of §4.4, and state that any residual coherent contribution in
   this transmission-mode/unbacked geometry is governed by, not separate
   from, EM-1's own already-computed passivity bound.
2. Disclose EM-6/EM-7's unaddressed R-vs-T methodology gap (§1.3): note
   that no ÷2 correction was applied to these reflectance-based figures,
   that applying one would only widen (not narrow) the realizability gap,
   and that neither conversion is a rigorous application of Section 4's
   own coherent-film Airy-stack framework to what are actually diffuse-
   reflectance measurements off semi-infinite porous media.
3. Fill the missing `ratio@600nm` cells for the two query-11 rows in
   EM-5's table (§2, item 1) — harmless by monotonicity, but the table
   should actually be complete against its own stated three-wavelength
   scoring bar.
4. Add a note to EM-5's verdict (§2, item 2) that the pre-registered
   falsification condition, read literally, is met by two of three
   sourced geometries, and that "PARTIAL" reflects a post-hoc, more
   informative recharacterization rather than the letter of the
   pre-committed bar — flagged for the record, not re-litigated.
5. Widen `exp061-thermo-length-scale-staleness`'s `candidate_globs` per §5,
   pending Red Team's own ruling on whether this independently fires
   Checkpoint criterion 4.

None of these change exp-061's UNOBTANIUM-WITH-PARAMETERS tier, exp-062's
own EM-4 headline (1.20× stands), or this cycle's own PROMISING verdict.

---

## 7. Ruled-out registry check (R1–R5, T1–T26)

Checked against the full registry (read in full: RULED OUT summary, T1–T26
Live Threads, and a targeted search across the entire LOGBOOK.md for any
prior mention of thin-film/Airy/black-matrix/n_eff/Salisbury-screen content
— none found outside this cycle and Iteration 38, confirming Section 4's
physics is genuinely new to this program, not a re-litigation).

- **R1–R5**: not implicated. This cycle makes no transformation-optics/
  refractive claim (R1), no integer-λ shell-thickness claim (R2), no
  grid-artifact claim needing an R3-style check (R3, though I note EM-5's
  own resolution/completeness questions above are a distant cousin in
  spirit, not a re-proposal), no hand-typed "precisely recomputed" figure
  (R4 — every number in this document and its predecessors was produced
  by direct invocation, confirmed independently three times over: Phase 1,
  Red Team's Phase-2 audit, and my own re-derivation here), and no
  `P`-normalized phase-offset claim (R5).
- **T1–T26**: exp-062 makes zero constraint-1/2/3/4 claim ("T1 escape
  route: NONE" is honestly declared and true on inspection — nothing here
  touches σ(I)/σ(x,t)/angular-selectivity/sub-threshold machinery). The
  near-field-coupling regime this cycle examines (VACNT inter-tube pitch
  vs. `λ/2π`) is a distinct physical object from T21's FDTD-source
  diffraction fringe (an instrument artifact of this bench's own line-
  source geometry) and from T25/T26's coherent-ambient-sum machinery (a
  bench-instrument coherence question, not a real-material homogenization
  question) — correctly not conflated anywhere in this cycle's record, and
  I independently confirm no conflation on my own re-read. No live thread
  is re-litigated or quietly contradicted.

---

**Summary**: PROMISING. The core EM physics holds up under a third
independent re-derivation. EM-3's headline conclusion survives scrutiny
substantively, though its wording overclaims slightly. A new, real, but
non-tier-moving methodological gap exists in EM-6/EM-7's OD-to-α
conversion. EM-5's table is numerically correct but incomplete in two
minor ways and leaves the program's actually-relevant comparator geometry
unresolved — the top priority for Iteration 40. A second Checkpoint-4-
shaped registry gap, structurally identical to the one that just fired for
this cycle's own sibling entry, is found live (not hypothetically) in
`exp061-thermo-length-scale-staleness` and referred to Red Team for
ruling.
