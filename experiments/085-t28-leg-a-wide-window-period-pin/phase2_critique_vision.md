# PHASE 2 — CRITIQUE · VISION SCIENCE · Panel Iteration 62 · exp-085

*Seat: VISION SCIENCE. Fresh sub-agent, blind to any other seat's current-cycle
critique. Charter: human perceptual limits; duty to pin numeric thresholds,
with sources, before any run that scores against them. Read in full:
PANEL.md, LOGBOOK.md (all ~18,728 lines, including RULED OUT R1–R10 and the
T28 thread's Iterations 55–61 in full), `experiments/084-.../NOTES.md`,
`phase1_derivation.py`, `derivation_results.json`, `phase5_redteam_audit.md`,
and `experiments/085-.../phase1_proposal.md`.*

---

## 0. Scope-framing check (my seat's first duty this cycle)

§3 claims: "N/A — instrument/model-fidelity thread... touches no
constraint-3 scene... Checkpoint criterion 2 (mechanism-class boundary) is
N/A this cycle." I verified this directly rather than accepting it: the
proposal's only computed quantity is `edge_diffraction_c_empty_corrected`
(an already-validated Weber-contrast-reduced curve) re-evaluated over a
wider/denser `θ` grid and re-fit by already-committed period-search
machinery (`free_period_with_widening`, a zero-padded FFT). Nowhere does it
compare any value to `C_thr`, to photopic/scotopic ambient conditions, or to
any adaptation/detection quantity — it never calls anything that would
constitute a constraint-3 scoring event. **The N/A framing is correct**;
no perceptual threshold needs pinning before this run, because none of my
seat's instruments are engaged by anything §4 actually scores.

One near-miss, not load-bearing: Idealization 4 justifies excluding
`θ>80°` partly on "where a physically swept flashlight beam would not
plausibly operate relative to this bench's own source-aperture axis" — an
unsourced witness-scene claim smuggled into an otherwise scene-free desk
cycle. It only *narrows* the domain (conservative in effect) and is not
scored against anything, so it doesn't retroactively require a pinned
threshold — but it is exactly the kind of casual perceptual/scenario
assertion that should route through my seat with a source, not ride in a
parameter-table idealization uncredited. Flag, not a blocker.

## 1. §4 outcome-band audit — does the classification actually honor "the finding IS the drift"?

I worked through Method C's three-way partition (`frac_recovered`,
`spread`, `ρ`) as a decision table rather than reading it as prose:

- STABLE: `frac≥0.80` AND `spread≤0.15`
- DRIFTING: `frac≥0.80` AND `0.15<spread≤0.50` AND `|ρ|≥0.5`
- NOT STABLY PERIODIC: `frac<0.80`, OR (`spread>0.50` AND `|ρ|<0.5`)

**There is an uncovered cell**: `frac≥0.80` AND `spread>0.50` AND `|ρ|≥0.5`
— locally periodic in almost every sub-window, but with a *strong,
coherent* trend in the local period, large in magnitude. This is not an
edge case; it is arguably the single most physically distinctive outcome
the mechanism narrative in §1 describes ("the chirp is strong enough that
'the period' is not a well-defined single number... the finding IS the
drift, not a number"). A large, coherent, well-resolved chirp is exactly
that outcome — and it falls through all three named bands. As written, this
cell would have to be adjudicated post hoc, off the pre-registered table,
at exactly the moment §1's own promise is most tested. This is the
overstatement-vs-band gap my duty asks me to check for: the narrative
commits to "the finding IS the drift," but the falsifiable band structure
does not actually commit a verdict for the strongest form of that outcome.

## 2. A rule citation I traced back to its source and found does not hold up

§4 states, verbatim: *"No circular-shift null is run on the wide curve —
per R10's own explicit carve-out (RULED OUT registry): this curve is
deterministic and zero-noise by construction, so a null-under-noise
question does not apply."*

I traced this back to R10's actual finalized text (I did not take the
proposal's paraphrase on faith), which appears twice — the LOGBOOK
transcription and its source, `experiments/084-.../phase5_redteam_audit.md`
§6 (both bit-identical, confirmed by direct comparison):

> "...circular-shift-on-the-real-data is **the mandatory default, always
> run and reported even when another surrogate is also tried** — before it
> is reported as evidence..."
>
> "When the 'observed curve' is itself a deterministic, zero-measurement-
> noise quantity... **state explicitly that the circular-shift result
> answers a self-similarity/specificity question**..., not a literal
> measurement-noise question — both are legitimate uses of the same test,
> **but conflating the two misdescribes what 'distinguishable from noise'
> means**..."
>
> "A cycle that ships a free-period/free-phase SUPPORT verdict backed only
> by an unreproduced surrogate, **or that omits the mandatory
> circular-shift baseline entirely, fires Checkpoint criterion 4
> automatically** — the one gap where R10, alone among the R6–R9 lineage,
> previously carried no escalation consequence."

The deterministic-curve clause changes how a circular-shift result on such
a curve is *interpreted* (a self-similarity/specificity reading, not a
noise-significance reading) — it does not say the test may be skipped. It
is a re-labeling clause, not a waiver clause. §4's own outcome (b) branches
("narrow window undershot — wide fit moves toward `P_edge_A`",
"wide fit confirms `2.5338°`") are period-match verdicts of exactly the
SUPPORT/CONFIRM shape R10 governs. **As currently written, this proposal is
pre-committed to omitting R10's own mandatory baseline while reporting
that class of verdict — which is the literal condition R10's own text says
fires Checkpoint criterion 4 automatically.** This is not a hypothetical
downstream risk; it is baked into §4's design before any code runs, and it
is the kind of "confirmed the arithmetic, never asked whether the operands
apply" gap R9 exists to catch, applied here to a rule citation instead of a
unit comparison.

(For the record: I independently re-derived `derivation_results.json`'s
cited figures rather than trusting the proposal's restatement —
`leg_a.p_model_deg=2.533834586466165`, `r_squared=0.36965580905914364`,
`rel_dev=0.10846560846560856`, and `p_edge_a=2.8421052631578947` all match
what §2's parameter table cites, to the printed digit.)

---

## Steel-man (≤150 words)

exp-085 is a disciplined, cheap desk-cycle extension of exp-084's own leg
(a): every reused primitive (`edge_diffraction_c_empty_corrected`,
`free_period_with_widening`) is cited to committed source per R4, the three
methods (wide grid-search, independent FFT, sub-window drift diagnostic)
are genuinely complementary rather than redundant restatements, and the
T1/Checkpoint-2 N/A framing is accurate — nothing here scores a
constraint-3 scene or a perceptual threshold, so my own duty to pin numeric
thresholds before a scoring run is correctly not triggered this cycle. The
parameter table's grid choices (θ-uniform vs. `sin(θ)`-uniform, padded FFT)
are motivated by the actual physics (Fresnel-zone chirp), not picked for
convenience, and the idealizations are stated honestly, including the frank
acknowledgment that a wide fit converging tightly would only motivate, not
itself constitute, a future real-FDTD re-test.

## Sharpest attack (≤150 words)

§4 states plainly: "No circular-shift null is run on the wide curve,"
citing R10's deterministic-curve carve-out. But R10's actual text
(finalized `phase5_redteam_audit.md` §6) makes circular-shift "the
mandatory default, always run and reported even when another surrogate is
also tried" — the carve-out only changes how a deterministic curve's
result is interpreted (a self-similarity question, not a noise question),
never whether it runs. R10's own escalation clause: omitting the baseline
entirely while reporting a SUPPORT-class outcome "fires Checkpoint
criterion 4 automatically." As written, any "wide fit moves toward
`P_edge_A`" or "confirms `2.5338°`" outcome this cycle produces is
pre-committed to that automatic firing. Separately, §4's own bands leave
`frac_recovered≥0.80` & `spread>0.50` & `|ρ|≥0.5` — a strong, coherent,
large-amplitude chirp — unclassified, exactly the case §1's "the finding IS
the drift, not a number" promises to capture.

## Verdict: **support-with-changes**

## Single parameter change that would flip me to full support

Add a fourth, mandatory step to §4: run and report the order-preserving
circular-shift null on Method A's wide-window fit (interpreted per R10's
own self-similarity/specificity framing for deterministic curves, not
skipped), and extend the three-way outcome table to explicitly cover
`frac_recovered≥0.80` & `spread>0.50` & `|ρ|≥0.5` (fold it into DRIFTING or
add a named fourth band) before any code runs. Either change alone
resolves the sharpest attack; both together close this critique entirely.
