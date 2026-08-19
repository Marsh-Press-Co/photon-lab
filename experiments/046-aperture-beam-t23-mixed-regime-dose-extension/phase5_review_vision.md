# PHASE 5 — REVIEW · VISION SCIENCE (fresh context, blind) · exp-046, Panel Iteration 23

*Every claim below was checked against `results.json`, `run.py`,
`REALIZABILITY_MEMO.md`, `lab/validation/run_all.py` and `git log` directly.
NOTES.md's own statements were treated as claims to be tested, not as findings.
Verification log at the end.*

---

## 1. My reading

Nothing in exp-046 measures, moves, or scores a perceptual quantity, and the
cycle is right to say so. My audit is therefore not about the physics — it is
the one thing my seat has a documented, repeated track record of catching: a
disclaimer, scope tag or fix adopted in principle that failed to reach every
locus where it is cited (LOGBOOK's fix-docket-delivery pattern, Iterations 13,
14, 15, 17, 20, 21, 22 — a 6th-plus recurrence in 8 iterations, rate not
decreasing).

**What actually landed, and deserves the credit before the attacks:**

- **Docket 20's substantive half is delivered.** `results.json`, `run.py` and
  NOTES.md are clean of the perceptual verdict. P-TH23-B3 is restated as a pure
  instrument comparison; the Wien peak is reported bare (9.8849 µm) with no
  perceptual gloss attached. At Phase 2 my seat offered two options — strike, or
  keep with a stated perceptual basis. The cycle took the stricter one. Correct.
- **Docket 21 reached both loci that have actually failed twice.** NOTES.md
  prose carries the disclaimer at document scope (line 10), again at the head of
  *Learned* (line 220), and as idealization 10. `run.py` prints it at both ends
  of the desk report (`:1394`, `:1493`) and inlines it inside B3/B5/C3's own
  printed dicts. This is the first cycle in four where I did not have to file the
  prose/prints gap.
- **`REALIZABILITY_MEMO.md` Amendment 5 is actually written** — both halves,
  the memory-axis closed form and the silicon provenance downgrade, committed in
  the same shift that promised it (`460f018`). This is the exact item that failed
  at Iteration 21 (memo never amended, Checkpoint-conditional) and it did not
  fail here.
- **C1 and C4 lacking the NETD disclaimer is CORRECT, not a gap.** My own
  Phase-2 enumeration ("B3, B5, C1, C3, C4") was over-broad: as delivered, C1 is
  a memory-ratio claim and C4 a tier-scoring claim, neither carrying a
  detectability classification. The cycle applied the functional rule (disclaim
  where a NETD/UNDETECTABLE claim is made) rather than my literal list. That is
  the better reading and I withdraw the literal one.

**Five propagation gaps, all zero-cost, ranked by severity.**

### V1 (sharpest) — A1's "withheld" disposition exists at exactly one locus, and it is not the one anyone will cite

This cycle introduced a genuinely new kind of judgment call: a pre-registered
*all-or-nothing* withholding clause (P-TH23-A6: "any gate fails ⇒ no Block-A
number is reported at all") applied **in scope** rather than as a blanket, after
S16-b failed. NOTES.md handles this well and even invites the stricter reading
("a reader who disagrees should read A1 as withheld entirely"). The problem is
where that disposition lives.

Measured directly in `results.json` (3.21 MB):

| string | occurrences |
|---|---|
| `withheld` | **0** |
| `gate-backed` | **1** — inside `block_a_fdtd.gate_disposition`, a prose paragraph |

Meanwhile the canonical record a future cycle will cite,
`block_a_aperture_consistent_beam.predictions["P-TH23-A1"]`, reads in full:

```
"class": "DESK-POINTING-READING (re-scoped, NOT a coherence adjudication) [docket 5]",
"n_above_C_THR": 36, "n_of": 36,
"n_at_or_above_20x_incoherent": 35,
"min_abs_C": 0.03227049044535179,
"band": "36/36 above C_THR; >=35/36 at or above 20x ... ; min|C| >= 0.03"
```

No withheld flag. No not-gate-backed flag. No class change. And it *does* carry
the `C_THR` disclaimer verbatim — which makes it read as the most
compliance-audited entry in the file, precisely the entry a future seat would
trust on sight.

`run.py` is worse: the post-run console path prints the gate table (S16-b
**FAIL**), then A5, then the exploratory legs, then writes the file. It **never
prints `gate_disposition` at all**. So the console shows "36/36 above C_THR" (in
the predictions block) and a failed pointing gate, and never once connects them.

NOTES.md is the *only* artifact carrying the disposition — and NOTES.md prose is
the locus this program's own history says does not get cited. exp-046 itself
demonstrates the citation route: it pulled exp-041's `block_main` C_empty and
exp-042's `phase5_erratum.block_beam_corrected.worst_cell` straight out of
`results.json`, not out of anyone's prose. This is the same shape as Iteration
17's Checkpoint-4 firing (a Phase-3-committed scope tag failing to propagate
into the committed record) with the loci inverted relative to Iteration 20.

Two sub-defects in the same place:

- **V1b — the scorecard row says the opposite of what it means.** Row A1 reads
  "PARTIAL (computed in band; **withheld as gate-backed**)". Parsed literally
  that is "withheld, as [it is] gate-backed" — the inverse of the intent
  ("withheld from being reported as gate-backed"). LOGBOOK iteration entries are
  built by copying scorecard rows. This one inverts under copying.
- **V1c — a withheld reading is counted in the cycle's own success tally.** The
  headline is "11 CONFIRMED, 3 PARTIAL, 1 REFUTED, 2 DROPPED", and A1 is one of
  the three PARTIALs. A reading the Director has withheld should not contribute
  to the scorecard that summarises the cycle; it needs a fourth bucket
  (WITHHELD) or explicit exclusion from the count.

**Fix (5 minutes):** add to the A1 prediction dict
`"gate_backing": "NOT GATE-BACKED — S16-b (pointing) FAILED; this is an estimator reading, not a validated measurement. P-TH23-A6's withholding clause applied in scope; see block_a_fdtd.gate_disposition."`;
print `gate_disposition` to the console immediately after the gate table; restate
the scorecard cell as "WITHHELD — not gate-backed (S16-b FAILED)" and drop A1
from the PARTIAL count.

### V2 — "struck everywhere" is false at the two loci docket 20 actually named, and there is no banner

Docket item 20 reads: *"**Strike 'eye-invisible'** from §1 and from P-TH23-B3's
prediction text."* §1 and P-TH23-B3 are sections of `phase1_proposal.md`.

- `phase1_proposal.md:46` — "…607× below NETD, Wien peak 9.885 µm,
  **eye-invisible**." Still there.
- `phase1_proposal.md:342` — "Mixed regime is still UNDETECTABLE and
  **eye-invisible** (seat sidecar)". Still there.
- `git log -- phase1_proposal.md` → one commit, `8950125` (Phase 1). Never
  edited. **And no SUPERSEDED banner.**

Contrast the precedent set exactly one cycle ago: exp-045's
`phase1_proposal.md` was touched at Phase-5 close (`f48de18`) specifically to add
a SUPERSEDED banner, on Red Team's mandatory-fix list, for a *milder* case (a
fabricated citation inside a superseded block). exp-046's Phase-1 draft carries
far more superseded content than exp-045's did — the entire §2.1 geometry table
(docket 3), §1's N_F range, idealizations 2 and 4, the "sourced" silicon label,
predictions A3/A4/A7 — plus the perceptual claim the docket called
"non-negotiable" and "constraint-3-shaped".

NOTES.md then makes two statements that are only jointly true under a silent
rescoping:

- line 14: the "eye-invisible" language is "**struck everywhere** (docket 20)";
- line 40: "The full seven-file panel record precedes this file and is
  **unedited**."

And the disclaimer string itself — repeated **2672 times** in `results.json` —
asserts *"no 'eye-invisible' claim is made anywhere in this cycle [docket 20]"*.
That sentence is literally false against the cycle's own directory, 2672 times
over. This is the fix-docket pattern's signature exactly: an item claimed
complete, delivered at the live loci, silently rescoped at the named ones.

**Fix:** the banner (Iteration-22 precedent, one cycle old), naming §1,
P-TH23-B3, §2.1's table, idealizations 2/4, the silicon label and the dropped
predictions — *or*, if the Director prefers, rescope NOTES.md's "struck
everywhere" and the disclaimer's "anywhere in this cycle" to "from every
committed result and every live claim; the Phase-1 draft is preserved unedited
and flagged." The banner is better: it is the convention already in force.

### V3 — the hardened rule protecting my own seat's deliverable contains a carve-out that would have excused this very cycle, while claiming to mirror the aperture rule "exactly"

This is the item the Director's brief asks whether a future Director could soften
back into prose. The answer is: it is already soft, and it advertises itself as
hard.

Iteration 22's rule (`LOGBOOK.md:8324-8329`), verbatim:

> QUANTUM's aperture-consistent single-coherent-mode beam check **MUST run** at
> Iteration 23, by any lead seat. **If Iteration 23 closes without it having been
> run, Checkpoint criterion 4 fires automatically and immediately — no further
> debate, no seat vote, no Director discretion, and no further one-cycle
> extensions via prose.**

`phase3_synthesis.md:47-53`, verbatim:

> if Iteration 24 closes without VISION's glare/adaptation Tier-W sidecar having
> been run (by any lead seat, sourced via WebSearch-snippet-tier per the standing
> T18 adaptation, **or with an explicit renewed-deferral reason that itself
> survives a Phase-2 Red Team audit**), Checkpoint criterion 4 fires
> automatically and immediately — no further debate, no seat vote, no Director
> discretion, **mirroring the aperture-check rule's own wording exactly.**

Three defects, compounding:

1. **The carve-out is the one device the sibling rule names and forecloses.**
   "A renewed-deferral reason that survives a Red Team audit" *is* a one-cycle
   extension via prose. Iteration 22's clause "and no further one-cycle
   extensions via prose" is dropped and its content re-admitted through the
   parenthetical. The claim of mirroring "exactly" is therefore false, and it is
   the kind of false-equivalence claim that survives copying into LOGBOOK
   unexamined.
2. **The rule is self-nullifying — it could not fire on the behaviour that
   created it.** Iteration 23's deferral had three specific stated reasons and
   Red Team wrote, in docket item 24: *"I do **not** contest the deferral — T18
   EGRESS_BLOCKED at eleven consecutive confirmations is dispositive."* That is
   an explicit renewed-deferral reason that survived a Phase-2 Red Team audit.
   Under the new wording, Iteration 23 would have satisfied the Iteration-24
   rule. A tripwire that its own triggering event satisfies is not a tripwire.
3. **"No Director discretion" and "a reason that survives an audit" are mutually
   exclusive.** Someone must adjudicate survival. The rule grants the discretion
   it denies in the same sentence.

And it does not exist in one form. Three renderings, all in this cycle:

| artifact | rendering |
|---|---|
| `phase3_synthesis.md:47-53` | full text, **with** carve-out, claims exact mirroring |
| `NOTES.md:60-63` | one-line summary, **without** carve-out (strictly harder) |
| `results.json` | *"item 24 is a standing program-integrity rule"* — the words `glare`, `tripwire`, `Tier-W`, `criterion 4` occur **zero** times |

Which one a future Director copies into LOGBOOK is a coin flip, and the
machine-readable artifact carries a pointer with no content.

**Fix — the exact text I ask be carried into LOGBOOK verbatim, and written into
`results.json` as a string so it cannot be re-derived:**

> **HARDENED RULE (Iteration 23 close).** VISION SCIENCE's glare/adaptation
> Tier-W sidecar (docket #7's other original half, open since Iteration 1) MUST
> run at Iteration 24, by any lead seat, sourced at WebSearch-snippet tier per
> the standing T18 adaptation and labelled Tier-W-provisional. If Iteration 24
> closes without it having been run, Checkpoint criterion 4 fires automatically
> and immediately — no further debate, no seat vote, no Director discretion, no
> renewed-deferral reason of any kind, and no further one-cycle extensions via
> prose. **A Phase-2 Red Team audit blessing a renewed deferral does NOT satisfy
> this rule: Iteration 23's own deferral was Red-Team-blessed, and that is what
> tripped it.**

I want to be explicit that I am **not** contesting the Iteration-23 deferral
itself. T18's block at eleven consecutive confirmations is dispositive on my own
charter's terms, and manufacturing thresholds from seat memory is the failure
mode that produced the fabricated PMMA citation. The deferral is right. The rule
carrying it forward is broken.

### V4 — the C_THR disclaimer-stripping the docket fixed at A1 was recreated, this cycle, at a sentence the same docket re-authored

Docket 5 landed cleanly: `run.py:131` defines `C_THR_COMMENT` verbatim from
`042/run.py:41`, and both A1's statement and `results.json`'s
`C_THR_comment_verbatim` carry it. Good.

But `idealization_4_restated.statement` — a sentence **rewritten this cycle under
docket 11** — reads:

> "Under the corrected width the unaimed rim residual is ~1e-2 in amplitude /
> ~1e-4 in intensity — **still below C_THR=0.005** but WITHOUT the four-orders
> margin the Phase-1 idealization claimed."

That is the perceptual bar used bare, as a pass-shaped yardstick ("still below" =
"still fine"), with the disclaiming half stripped — in `results.json`, and
propagated verbatim into NOTES.md idealization 4 (line 276). It is the exact
mislabeling LOGBOOK T20 records having had to correct once already ("an earlier
draft of this entry mislabeled it 0.005, which is VISION's own T2 perceptual
C_thr bar, not an instrument-floor gate"), and the exact defect my Phase-2 item 2
filed. The fix reached the locus the docket enumerated and not the locus the same
docket item created.

**Fix (one clause):** "…still below C_THR=0.005 (VISION's T2 photopic C_thr —
context only, this leg scores no perceptual pass/fail; the instrument-floor gate
is GATE_HARD=0.001)…"

### V5 — idealization 10's per-point storage claim is false at 250 of 2788 points

NOTES.md:303-307 claims the disclaimer is "stored per point at **all 2496 + 42 +
250 points**". Measured:

| point set | carries `netd_disclaimer` |
|---|---|
| `block_b…block_a_regrowth.points` | 2496 / 2496 ✓ |
| `block_c…points` | 42 / 42 ✓ |
| `block_c…c3_duration_scan.points` | **0 / 250** ✗ |

Total `netd_disclaimer` keys in `results.json`: **2672**, not 2788+.

The omission is functionally benign — the 250 scan points carry no `netd`
classification (their keys are `measured_ratio`, `closed_form_ratio`,
`closed_form_predicts_memory`, `measured_memory`, `realizability_tier`), so no
detectability claim is made there and none needs disclaiming. **The defect is the
claim, not the omission.** "A claimed-complete fix-docket item that wasn't fully
delivered" is this program's own named pattern, and this is my seat's own
disclaimer failing on a third consecutive cycle (Iteration 20: prose/prints;
Iteration 22: per-point across 1664 points; now: per-point across 250).

**Fix:** either add the key at the 250 (two lines), or correct the sentence to
"stored per point at all 2496 + 42 points that carry a NETD classification; the
250 duration-scan points carry no detectability claim and no classification."

---

## 2. Physical meaning — what this cycle does and does not say about a human eye

**It says nothing about a human eye, and that is the correct outcome.** No
perceptual threshold was scored against; T1 escape route is NONE; no constraint-3
or constraint-4 verdict is issued at either tier. The one perceptual number in
play, `C_THR = 0.005`, is used as a contamination-risk yardstick for a *future*
near-±40° run, and is correctly labelled as such at A1 (and incorrectly bare at
idealization 4 — V4).

**On the thermal blocks.** ΔT_ss = 3.293×10⁻⁵ K at the mixed regime, Wien peak
9.8849 µm, 607× below the low edge of the sourced microbolometer NETD band, with
every one of 2496 + 42 sweep points UNDETECTABLE-or-better. Perceptually: 9.88 µm
sits an order of magnitude beyond the long-wave edge of any measurable human
photopic response — there is no photoreceptor mechanism there at any radiance.
But that is a statement about *spectral location*, not about whether the object
is visible, and it must not be allowed to become one. The silhouette question
constraint 3 asks is about the object's ambient reflectance/absorption contrast,
which no thermal quantity in this cycle touches at all. What Blocks B and C
actually close is an **instrument** axis: how much of the object's own thermal
emission could ever betray it to a detector. The answer is 607×–6681× below NETD.
That is a real closure and it is not a perceptual one. This is exactly why
striking "eye-invisible" mattered: the Phase-1 sentence welded a perceptual
verdict to a radiometric quantity whose only falsifier was a detector ratio —
exp-036's spiropyran shape verbatim.

**On Block A and T21.** The genuine deliverable is instrument trust:
`profile="gauss"` is trust-gated for the first time in this program's history,
and exp-042's desk Huygens–Fresnel propagator is confirmed against FDTD at
N_F = 0.54–65.6 to ≤5.68% having been built and used at N_F ≈ 310–518. For my
charter that licenses the *machinery* for a future contamination-risk re-score;
it does not deliver one. The single reading that bears on "would this fringe
contaminate a future near-±40° constraint-3 run" is A1, and A1 is withheld
(V1). Idealization 3 confirms the standing gap unchanged: no sourced flashlight
coherence length or beam FWHM exists anywhere in this program, so the
Gaussian Schell-model partial-coherence bridge T21 pre-registered at Iteration 19
remains unbuilt. **T21's contamination-risk verdict is exactly where Iteration 19
left it.** The cycle is honest about this; the LOGBOOK entry must be too, and
must not let "propagator validated" read as "contamination risk resolved."

**On Block C — the one result with downstream perceptual relevance.** The memory
criterion `ratio_∞ = 1/(1 − a·f)`, memory ⟺ `D/τ_k < ln(21 f)`, collapses
Amendment 3's host list to a single dimensionless number, and Hosts A/B/C sit a
factor ~26 past threshold with **exactly** zero accumulation (measured
`|ratio−1| = 0.0` at all 30 negative controls, not "small"). For T17's
constraint-3-at-rest risk class this is a genuine, if negative, Tier-W-relevant
statement: repeated flashlight sweeps in the reported scene cannot build a
colored population in any PUBLISHED-tier host, because published lifetimes are
10³–10⁸× shorter than the 66.7 ms sweep dwell. Memory appears only at Host D
r=1.0 and Host E — the grid's least realizable corner. What it is **not** is a
scene contrast: a population fraction still has to be carried through
ε_colored/ε_bleached, path length and geometry into a Weber C and scored against
a sourced threshold before it says anything about an eye. That conversion is the
gap I named at Iteration 13 and it is still open.

---

## 3. Argued next change

**Run the glare/adaptation Tier-W sidecar at Iteration 24, and run it at the
evidentiary tier this program already accepts, instead of deferring it a
twenty-third time on a sourcing standard nothing else in this program is held
to.**

The deferral reasoning has been the same for eleven shifts: it is a sourcing
deliverable, WebFetch is EGRESS_BLOCKED, and inventing thresholds from seat
memory is the fabricated-PMMA failure mode. Every clause of that is true. What
has been missed each cycle is that **the sourcing is already in the record and
does not need re-fetching.** Iteration 1's Phase-5 entry (`LOGBOOK.md:1471`)
committed the entire parameter set with named sources:

- distance 45 m [30–60]; flashlight 100–200 lm; beam 5×10³–2×10⁴ cd;
- stray-light-at-eye E ∈ [0.01, 0.1] lx; ambient classes 10⁻⁵–10⁻³ cd/m²,
  moonless-sky anchor 1.7×10⁻⁴;
- glare angle θ(t) 0.5°→10° over a 1–3 s sweep;
- Stiles–Holladay veiling luminance `L_v = 10E/θ²`;
- adaptation persistence as a Crawford equivalent background `L_eq(t)`, recovery
  half-times ≥ 10 s at these exposures — Crawford 1946; Hecht et al. 1937;
  Pugh & Lamb 2000;
- verdict quantity: `min over sweep phase of C_thr(L_bg+L_v+L_eq)/C_eff`, with
  `C_eff = 0.686·L_bg/(L_bg+L_v+L_eq)`, both exponents, both bars.

And the threshold function is already frozen and bench-committed (T2, exp-020):
`C_thr(L) = 0.005·max[1,(L/3)^−p]`, `p ∈ [0.4, 0.5]`, field ×4. The measured wall
is `C = −0.686` (exp-020). **Nothing in that list requires a WebFetch.** It
requires composing already-committed constants through already-committed
functions and labelling the result at the tier the program has used for eleven
shifts — the same `WitnessScenario` WebSearch-snippet convention
(`lab/thermo_sidecar.py:224-243`) that every sourced number since exp-043 carries.

Scope it honestly and it is a one-file, zero-FDTD deliverable:

- **In scope:** the analytic composition above, both exponents, both ambient
  bars, per-sweep-phase; a `Tier-W-provisional` label on every output;
  per-point storage *and* point-of-claim inlining of the "perceptual
  thresholds at WebSearch-snippet evidentiary tier, not primary-source verified
  (T18)" disclaimer, in `results.json`, NOTES.md prose and `run.py` prints —
  all three loci, pre-registered this time rather than fixed after the fact.
- **Explicitly out of scope, stated up front:** any claim that the resulting
  margin is primary-source-verified; any Tier-A (photopic) reading; any
  extrapolation past the bench-scale/witness-scale bridge (T8/T13).

If it closes 4–21× sub-threshold as Iteration 1's arithmetic projected, Tier W's
static-silhouette clause moves from hypothesis to result for the existing article
and Tier W reduces to constraint 4. If it does not, that is a real, pre-registered
loss and the sub-threshold escape route weakens. Either outcome advances the
logbook. Twenty-two iterations of deferral have produced neither.

**And carry the rule that protects it in the corrected form (V3).** As currently
worded, Iteration 24 can defer again with a Red-Team-blessed reason and the
tripwire will not fire — which is how this item reached iteration 23 in the first
place.

---

## 4. Ranked top-3 candidate directions for Iteration 24

1. **VISION's glare/adaptation Tier-W sidecar, scoped as in §3** — zero FDTD,
   one file, all inputs already committed to this repo, run by any lead seat
   (Iteration 24 is QUANTUM's slot; the non-native-lead precedent is Iterations
   18/20/21). Carried under the **corrected** hardened rule, with that rule's
   exact text written into `results.json` as a string, not left in prose.
2. **The five propagation fixes V1–V5 (plus V1b/V1c), applied in this same
   close** — every one is mechanical and zero-cost: A1's `gate_backing` key and
   console print; the SUPERSEDED banner on `phase1_proposal.md`; the C_THR
   disclaimer clause in idealization 4; the corrected per-point-count sentence;
   the scorecard cell reworded and A1 removed from the PARTIAL tally. Per the
   standing instruction (Iterations 15/17/20/21/22), if any is carried forward
   instead of applied here, Checkpoint criterion 4 should fire without further
   debate.
3. **Close A1's withholding with one FDTD leg, or close T21's contamination risk
   with one sourced number.** The propagator is now validated at the
   aperture-consistent Fresnel numbers (A5, 4/4), so the blocker on A1 is not the
   propagator — it is that S16-b's ray-optics target is non-paraxial-invalid at
   the 14° divergence it was gated at. Re-run the pointing gate at the
   physically-motivated 10° FWHM point (A-v2), where exact-vs-ray is 3.57 cells
   rather than 8.03, and A1 becomes gate-backed instead of withheld — one leg,
   ~15 s. Separately and independently: a single sourced real-flashlight
   coherence length or beam FWHM would unblock the Gaussian Schell-model bridge
   and convert T21's contamination risk from "open" to a number, for the first
   time since Iteration 19.

*(Not re-proposed, checked against RULED OUT: nothing here touches R1, R2 or R3;
nothing re-proposes a ruled-out mechanism; this cycle proposes no mechanism at
all.)*

---

## 5. Verdict

# PARTIAL

**Why not PROMISING.** The cycle's real deliverable is genuine and clean — a
desk propagator validated three orders of Fresnel number outside its construction
regime, `profile="gauss"` trust-gated for the first time in this program's
history, an honest REFUTED on a pre-registered gate with the failure attributed
to its own target rather than smoothed, and `REALIZABILITY_MEMO.md` Amendment 5
actually written in the shift that promised it. But this program's own precedent
is that the verdict turns on whether the cycle's open questions close, not on the
headline count (Iterations 9, 10, 12, 17, 21, 22). Here: the cycle's advertised
Block-A headline was never an experimental question at all (Attack 2 — recorded
honestly as *mis-posed*); the one Block-A reading that bears on my charter is
withheld, and its withholding did not reach the artifact anyone cites; the
"struck everywhere" claim is false at the two loci the docket named, with no
banner and a one-cycle-old precedent for one; a per-point storage claim is 250
points short; and the hardened rule protecting my own seat's twenty-two-iteration
deliverable contains a carve-out that would have excused the very deferral that
created it. Four of those five are the fix-docket-delivery pattern, in the cycle
whose own Phase-2 audit named that pattern twice.

**Why not RULED OUT.** Nothing here is a dead end. The physics is undamaged, no
arithmetic defect was found in my lane, every defect I filed is a mechanical,
zero-cost correction, and the perceptual leak the docket called non-negotiable
was in fact removed from every live artifact.

**Checkpoint stance, explicit.** Criterion 4 **does not fire** *on the condition*
that V1–V5 are applied in this same close — the identical mechanism this program
applied at Iterations 19, 20, 21 and 22. If any is carried to Iteration 24, it
fires. I flag V3 specifically: it is the one defect that, if propagated as
written, disables criterion 4's ability to fire on my seat's item ever again, and
it is the one a future Director is most likely to copy unexamined because it
advertises itself as the hardest rule in the document.

---

## Verification log (what I actually ran)

**Confirmed by direct read/grep/execution:**

- `grep -rn "eye-invisible" experiments/046-*/` — 2 live occurrences in
  `phase1_proposal.md` (`:46`, `:342`); every other hit is a negation
  (NOTES.md:14, phase3_synthesis.md:33/82, `predictions_frozen.txt`,
  `results.json`'s disclaimer string). `git log -- phase1_proposal.md` → one
  commit, `8950125`, never amended. No banner (`grep -n "SUPERSEDED"` → no hit in
  that file).
- `git log --oneline -- experiments/045-*/phase1_proposal.md` → `f48de18`, the
  Iteration-22 Phase-5 close, i.e. the banner precedent is exactly one cycle old.
  `head -12` of that file confirms the banner's form.
- `results.json` string counts (python, whole 3,210,029-byte file):
  `withheld` = 0; `gate-backed` = 1 (offset 89845, inside
  `block_a_fdtd.gate_disposition`); `netd_disclaimer` keys = 2672;
  `glare`/`tripwire`/`Tier-W`/`criterion 4` = 0 each; `item 24` = 1 (offset 202,
  in the top-level `docket` string).
- `block_a_aperture_consistent_beam.predictions["P-TH23-A1"]` dumped in full —
  keys are class/statement/n_above_C_THR/n_of/n_at_or_above_20x_incoherent/
  min_abs_C/band. No withholding key. `block_a_fdtd` keys are legs/gates/
  P-TH23-A5/exploratory_object_present/all_gates_pass/
  all_gates_pass_with_first_light_amendment/gate_disposition/n_new_fdtd_calls —
  no A1 entry there either.
- `run.py:1496-1560` (`main`) read in full: post-run it prints gates, A5 and the
  exploratory legs, then writes `results.json`. `gate_disposition` is never
  printed. `grep -n "print(" run.py` confirms the disclaimer appears on console
  only at `:1394` and `:1493`, plus inside B3/B5/C3's generic dict loops.
- Per-point disclaimer coverage, counted in python:
  `block_b…block_a_regrowth.points` 2496/2496; `block_c…points` 42/42;
  `block_c…c3_duration_scan.points` **0/250** (that set's keys carry
  `realizability_tier` but no `netd` classification). NOTES.md:304 claims all
  three sets.
- `C_THR` sites: `run.py:131` (`C_THR_COMMENT`, verbatim from `042/run.py:41`),
  `:137` (bare definition), `:320` (A1 count), `:409` (`C_THR_comment_verbatim`
  into `results.json`), `:462` (idealization 4 — **bare use, no comment**),
  `:483-488` (A1 statement, comment carried ✓). Propagates to NOTES.md:276 bare.
- `phase3_synthesis.md:39-53` (item 24) vs `LOGBOOK.md:8324-8329` (Iteration 22's
  hardened rule) compared clause by clause: the carve-out is added, "no further
  one-cycle extensions via prose" is dropped, "mirroring … exactly" is asserted.
  `phase2_redteam_audit.md:669-678` (docket 24) confirms Red Team wrote "I do
  **not** contest the deferral" — i.e. this cycle's own deferral satisfies the
  carve-out. NOTES.md:60-63 states the rule without the carve-out.
- `REALIZABILITY_MEMO.md:162-233` — Amendment 5 present, both halves ((a) the
  `D/τ_k < ln(21 f)` criterion with the r=1.0 refutation recorded, (b) the
  silicon `ASSUMED — provenance terminates unsourced (T18)` downgrade plus the
  `fill_factor`/`ρ C_P L²/(4εσT³L + k_air)` correction), committed in `460f018`,
  the same commit as the results. **Delivered.**
- `lab/validation/run_all.py:1194-1360` — stage 16 present; the first-light
  amendment is documented in the docstring with the ray-optics-target diagnosis
  (987.14 exact vs 979.12 ray optics, +8.0 cells) and the [info] line retains the
  original comparison; `run.py` does score the unamended gate as FAILED, as
  NOTES.md claims.
- `_stage_selected` executed directly: `"16"` → [16]; `"12346789,10,11"` →
  [1,2,3,4,6,7,8,9,10,11]; `"12346789,10,11,12,13,14,15"` → 14 stages; `"5"` →
  [5]. Learned #5's selector fix is real and correct; the 88/88 decomposition is
  internally consistent.
- Scorecard cross-checks against `results.json`: A1 36/36, 35/36, min|C| =
  0.03227049044535179 ✓; B3 607.3348951257713 / 9.884938340376813 µm /
  UNDETECTABLE ✓; B5 2496 points, 416 new, max ΔT 2.9935695894106383×10⁻⁶,
  margin 6680.99 ✓; C1 30 negative controls at max deviation **0.0**, 12 memory
  point-runs, all at Host D r=1.0 / Host E ✓; C3 max ΔT 1.6465380270845675×10⁻⁵,
  margin 1214.67 ✓; C4 12 PUBLISHED / 0 with memory, 18 UNOBTANIUM / 7 with
  memory ✓. **No arithmetic defect found in my lane.**
- `P-TH23-B3` in `results.json` re-read in full: the statement is a pure
  instrument comparison, the Wien peak is reported bare with no perceptual gloss,
  and the disclaimer is inlined. Docket 20's substantive half is genuinely
  delivered.

**Checked and cleared (not defects):** C1 and C4 carrying no NETD disclaimer (no
detectability claim is made at either — my own Phase-2 enumeration was
over-broad); the Wien peak reported without a perceptual interpretation (the
stricter of the two options I offered); idealization 3's refusal to build the
Schell-model bridge absent a sourced coherence length; the scoped application of
A6's withholding clause as a *judgment* (it is disclosed, reasoned, and invites
the stricter reading — my objection is to where the record of it lives, not to
the call); the Iteration-23 deferral of my own sidecar (T18 at eleven
confirmations is dispositive; my objection is to the rule carrying it forward).
