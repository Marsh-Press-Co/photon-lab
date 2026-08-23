# Phase 5 — THERMODYNAMICS review (exp-063 / Panel Iteration 40)

*Fresh sub-agent, blind to the other six seats' current-cycle Phase-5
reviews. Charter: where absorbed energy goes; always asks what
re-radiates and whether it would be detectable; owns the per-proposal
energy sidecar (absorbed power → ΔT → emission band → detectability) as
a post-run analytic calculation, never an FDTD output.*

**Read in full**: `PANEL.md`; `LOGBOOK.md` (RULED OUT R1–R5 in full;
T1–T26 read structurally, T5/T22/T23 read in full as this cycle's own
direct ancestry, Iterations 38–39 read in full for the caveat-lint/
Checkpoint-4 precedent this cycle's own Phase-2 audit leans on); `PLAN.md`
Current-state section; this cycle's complete record (`phase1_proposal.md`,
all five `phase2_critique_*.md`, `phase2_redteam_audit.md`,
`phase3_synthesis.md`, `NOTES.md`, `phase4_results.md`); `lab/
thermo_sidecar.py` in full; `lab/validation/run_all.py::
stage23_front_surface_biot_correction`. Every headline number below was
independently recomputed from `lab/thermo_sidecar.py`, not taken from any
document's prose, and both `lab/caveat_lint.py`/`lab/numeric_lint.py`
entries this cycle registers were run live against the working tree, not
trusted from the record.

---

## 1. Independent verification — Phase 4's own arithmetic

Recomputed `front_surface_conduction_correction` and
`biot_number` myself, from a clean Python invocation of the committed
module, at all four sourced κ values (0.70, 9.62, 40.0, 50.0 W/(m·K)),
at both geometries (`L_bench=2.34µm`, `L_MP5-730x=1051.2µm`), plus the
`κ_critical` bisection:

```
kappa= 0.70  Bi_gas=0.03714  CF_bench=1.03716  margin_bench=674.22x   CF_mp5=1.04487  margin_mp5=1.2920x
kappa= 9.62  Bi_gas=0.00270  CF_bench=1.00270  margin_bench=697.38x   CF_mp5=1.00326  margin_mp5=1.3456x
kappa=40.00  Bi_gas=0.00065  CF_bench=1.00065  margin_bench=698.82x   CF_mp5=1.00079  margin_mp5=1.3489x
kappa=50.00  Bi_gas=0.00052  CF_bench=1.00052  margin_bench=698.91x   CF_mp5=1.00063  margin_mp5=1.3492x
kappa_critical = 0.089731 W/(m*K)
```

Every figure reproduces `phase4_results.md`'s own summary table to the
printed digit, independently of Red Team's own Phase-2 re-derivation
(which necessarily predates Phase 4's actual sourced κ values and could
only check the closed-form machinery, not this cycle's own scored
result). `stage23_front_surface_biot_correction` (4/4) also reproduces
cleanly on a direct re-run. **No arithmetic defect anywhere in this
cycle's headline claim.** The bottom-line finding — the correct
material's κ still licenses the lumped assumption, the worst sourced
figure (0.7 W/(m·K), the bulk-mat number, genuinely the most
conservative real value found) tightens the flagship margin by 3.6% and
exp-061's own thinnest witness margin by 4.3%, and κ_critical sits 7.8×
below even that worst-found κ — is correct as stated, not merely
asserted.

---

## 2. A gap this cycle's own record leaves for Phase 5 to close: `NOTES.md` has no `Result` or `Learned` section

This program's own convention (CLAUDE.md: "every writeup states its
idealizations... a NOTES.md each — hypothesis / setup / result / learned
/ next") and this program's own recent, consistent practice — exp-054
(`## Results` / `## Learned` / `## Next`), exp-060 (same), exp-061 (`##
Result (Phase 4 — full record...)` / `## Learned` / `## Next`), exp-062
(`## Learned` / `## Next`, flagged by name in that cycle's own review as
a placeholder to fill at Phase 5 close) — all give `NOTES.md` a `Result`
and a `Learned` section restating Phase 4's actual outcome. exp-063's
`NOTES.md`, checked directly (`grep -n "^## "`), has **neither**: it runs
Hypothesis → Setup → the bracket derivation → the frozen predictions
table → Idealizations → Registry → `Next`, and `git log` on the file
shows it was written once, at the Phase-3 commit (`feed6ea`), and never
touched again — Phase 4 (`c2de14a`) added only `phase4_results.md`,
leaving `NOTES.md`'s own `## Next` section still reading "Phase 4 sources
κ_CNT-forest per the ten committed queries" as though Phase 4 were still
in the future, even though it has now run and delivered a decisive
result.

This is not a Checkpoint-4 matter — no wrong number propagated anywhere,
`phase4_results.md` itself is complete, correct, and independently
reproducible (§1 above), and the gap is in a section that by this
program's own pattern is customarily filled at Phase 5 close, not before.
But it is a concrete, checkable action item for the Director closing this
cycle, not merely a stylistic nicety: `NOTES.md` is this program's
self-contained frozen record per experiment, and a reader who opens it
alone (rather than chasing to `phase4_results.md`) currently cannot tell
that TD-1–TD-5 resolved at all. Recommended `Result`/`Learned` substance,
for the Director to adopt or amend:

> **Result**: κ_CNT-forest sourced for the first time, geometry-class-
> dependent: 0.7–9.62 W/(m·K) for as-grown/bulk-aggregate forest forms
> (the program's own actual candidate geometry class), ≈40–50 W/(m·K)
> for densified/drawn-sheet forms (a different, better-contacted
> processing class, flagged not scored as the primary figure). TD-1
> through TD-5 all CONFIRMED; the worst sourced κ (0.7 W/(m·K)) tightens
> the flagship bench margin 699.27×→674.22× and exp-061's own thinnest
> witness margin 1.35×→1.2920×, both nowhere near their own falsification
> bars (100× and 1.0× respectively); κ_critical=0.0897 W/(m·K) sits 7.8×
> below the lowest κ this cycle found. This program's "first-ever
> thermal-detectability classification flip" scenario does not
> materialize against any real figure sourced this cycle.
>
> **Learned**: (1) the correct candidate material's own κ does license
> the lumped-capacitance idealization every prior THERMO-sidecar margin
> rests on — a real, decisive, first-of-its-kind confirmation, not merely
> "not yet falsified"; (2) the correction is real and worth carrying
> forward (a 3.6–4.3% tightening at the worst sourced κ) but small next
> to either margin's own remaining headroom; (3) two structural questions
> this cycle deliberately left open (§5, below) — which boundary
> condition (front-colocated vs. rear-only loss) is physically real for
> the actual coating-on-substrate deployment, and whether the
> witness-scale conduction length `L=τ_true/α` is a licensed `h=k/L`
> input at all — remain genuinely unresolved and are NOT closed by how
> comfortably this cycle's own found κ values clear both brackets; a
> future cycle finding a materially lower κ, a materially longer L, or
> resolving either open question in the less favorable direction could
> still move the picture even though nothing in this cycle's own data
> does.

---

## 3. Registry tripwire — checked live, does not fire

Phase 3 adopted a forward tripwire (mirroring Iterations 23/37/38): any
gap surviving to Phase 5 or later in either new registry entry
(`exp063-biot-correction-machinery`, `exp063-thermo-disposition-netd-
disclaimer`) auto-fires Checkpoint criterion 4. I ran both live against
the current working tree rather than trusting Phase 3's "verified live"
claim on its own word:

```
python3 lab/caveat_lint.py --only exp063-biot-correction-machinery
  -> PASS NOTES.md, PASS phase4_results.md, 0 required-site failures
python3 lab/caveat_lint.py --only exp063-thermo-disposition-netd-disclaimer
  -> PASS NOTES.md, 0 required-site failures
python3 lab/numeric_lint.py
  -> exp063-cf-bench-vs-witness-derivation: PASS both TD-3 and TD-5 rows
python3 lab/validation/run_all.py --only 23
  -> 4/4 checks passed
```

**No gap found. The tripwire does not fire.** The only findings either
tool surfaces for exp-063 text are WARN-tier candidate sites (Phase-2
critique/synthesis documents that discuss `biot_number`/`κ_critical`
without repeating the disclaimer inline) — exactly the class Red Team's
own Phase-2 ruling already distinguished from a required-site failure,
and none of the six `required_sites` across both entries fail.

---

## 4. The assigned question: is the front-colocated-vs-rear-only bracket THERMO's job, and is it worth prioritizing?

**It is squarely this charter's territory in substance, but it is a
joint item with MATERIALS in practice, and it is not worth prioritizing
at Iteration 41 given this cycle's own numbers.**

*Whose job.* The physics question — given absorbed power enters
somewhere in a solid and must leave somewhere else, what does the
internal temperature field actually look like, and by how much does a
lumped estimate understate the true peak — is exactly "where absorbed
energy goes," the charter's own first sentence. That part is THERMO's to
own regardless of which boundary condition turns out to be real. But
*which* boundary condition is physically real for the actual candidate
deployment is not a thermodynamics question at all — it is a
realizability/deployment-geometry question (does a real record-blackness
CNT-forest coating's rear face sit against a bonded metal substrate, an
air gap, or something else) that only MATERIALS' own literature line can
answer, the same way MATERIALS, not THERMO, sourced κ_solid itself this
cycle. The correct division of labor, already implicit in how Phase 2
played out: MATERIALS sources the deployment answer; THERMO turns it into
a number. Neither seat can close this alone.

*Is it worth prioritizing.* No, not ahead of the two items ranked below
it in §5. The reason is in this cycle's own numbers, re-verified in §1:
at the single worst sourced κ (0.7 W/(m·K)), the two bracket endpoints
are `[1.0×, 1.2920×]` at witness scale and `[699.27×, 674.22×]` at bench
scale — a 4.5% and 3.6% spread respectively, and *both* endpoints sit
comfortably clear of their own falsification bars (κ_critical is 7.8×
below the lowest κ found; the bench 100× bar is cleared by 6.7×). Fully
resolving which endpoint is real, right now, would not move any
classification this program has issued — it would only narrow an already-
narrow bracket that no reading of this cycle's data threatens to cross.
That calculus changes only if a future cycle finds (a) a materially lower
κ than this cycle's own 0.7 W/(m·K) floor, (b) a materially longer
witness-scale `L` (Bi_rad scales with `L`, so a future MP-6-class
thickness revision that pushes `L` well past 1051.2µm would widen the
bracket, not just shift it), or (c) an independently fragile witness
margin from some other chain. None of those has happened. I would rank
the bracket-resolution question below both items in §5, not because it
is unimportant in principle, but because at the values this program has
actually measured it is currently inert — the same disposition Red
Team's own Phase-2 audit gave PHOTONICS' companion generation-side-
geometry caveat, and for the identical reason (numerically inert this
cycle, real, not free to ignore forever).

---

## 5. A reconciliation VISION flagged for this seat: does exp-063's "front hotter" contradict T23's "surface cooler"?

**Checked directly, independently of Idealization 1's own one-line
disambiguation: no contradiction — the two results are the same
mechanism, restated for two different generation profiles, and the sign
difference is exactly what the physics predicts.** T23's Iteration-23
finding (Amendment 5(b), `REALIZABILITY_MEMO.md`) concerns *volumetric*
absorption with loss from the *whole* exterior surface: heat generated
throughout the bulk, radiated/convected from every face. When internal
conduction is poor there, the interior runs hot and the radiating
surface — which sits at the boundary furthest from where most of the
volumetric heat sits, on average — runs *cooler* than the lumped
estimate. exp-063's model is the geometric opposite by construction: heat
generated *only* at one face (the illuminated front), lost *only* at the
other (the rear). Poor internal conduction here traps heat at the
*generation* boundary, which is now also the boundary furthest from the
*loss* channel — so the front runs *hotter* than lumped, not cooler. In
both cases the rule is the same: a poorly-conducting solid's temperature
field diverges from the lumped average in the direction of "hot near
generation, cool near loss," and which physical face is which determines
the sign. There is no inconsistency to reconcile beyond what
Idealization 1 already (correctly, if tersely) states — I confirm it
independently here because VISION's Phase-2 critique asked this seat to
render that confirmation explicitly, not leave it inferred.

---

## 6. η_thermal≡1 (mandatory fix 7) — sound as stated, one thing worth naming for a future cycle

QUANTUM's flip condition (unity thermal-conversion efficiency for
graphitic/semi-metallic carbon, sub-picosecond electron-phonon
relaxation, negligible photoluminescence) is standard physics and I have
no correction to it. Worth naming, not as a defect in this cycle but for
whichever future cycle next touches `P_abs`'s conversion into lattice
heat: the same assumption implicitly underwrites every prior
UNDETECTABLE THERMO disposition this program has issued (exp-043,
exp-057, exp-061's own witness-scale figures) under the *silicon* proxy,
where η_thermal≡1 is essentially unquestionable (silicon is not a
graphitic emitter). This cycle is the first to make the assumption
*material-specific* and *state it*, which is the correct fix — but it
also means every earlier disposition was carrying this same silent
assumption, undisclosed, for 15+ iterations, without incident (silicon's
own physics simply made it a non-issue). No action item follows from
this — the fix as applied is complete and correctly scoped to this
cycle's own new material identity — but it explains why this gap sat
unnoticed for so long rather than reflecting any inattention specific to
this cycle.

---

## 7. Verdict: **PROMISING**

The core derivation is sound (re-verified independently a third time,
after EM's Phase-2 re-derivation and Red Team's Phase-2 audit, now
against Phase 4's actual sourced numbers, not just the closed-form
machinery). The κ-sourcing task itself delivered a clean, decisive,
falsifiable result exactly as scoped — TD-1 through TD-5 all CONFIRMED,
with the falsification bar not merely avoided but missed by a wide,
disclosed margin (7.8× on κ_critical, 6.7× on the bench 100× bar), and
this program's own "first-ever classification flip" scenario explicitly
tested for and found absent. The process discipline is excellent: three
independently-triangulating Phase-2 attacks (generation-side geometry,
loss-side geometry, length legitimacy) were correctly adjudicated as
distinct rather than duplicative, all eight mandatory-fix items were
applied and are independently verifiable live (§3), the escalation
language Red Team caught (attack 7, "Checkpoint-1/2-adjacent") was
correctly walked back before it could mislead a future reader, and the
registry-gap question (§3 of `phase2_redteam_audit.md`) was argued from
the correct, closer precedent (Iteration 38's "tool built this same
cycle" ruling) rather than the more punitive but textually inapplicable
Iteration-39 tripwire. This is not RULED OUT territory (nothing here
closes a mechanism class, and none was proposed) and it clears PARTIAL:
the one item genuinely left open at Phase 3 close (§4/§5's bracket
question) is inert against every number this cycle actually measured, not
a live threat papered over, and the one process gap I found myself (§2)
is a Phase-5-customary fill-in, not a defect in Phase 4's own delivered
result. The single thing keeping this from an unreserved "closes cleanly"
read is that the witness-scale margin this cycle worked hardest to
defend (1.35×→1.2920× at the worst κ) is still, on its own terms, a
thin number — comfortably clear of every threshold this cycle checked,
but thin enough that the two items ranked below (§8) are not optional
follow-through, they are what keeps this exact number trustworthy the
next time something else about it moves.

---

## 8. Ranked top-3 for Iteration 41+

1. **Resolve EM's witness-scale length-legitimacy question**
   (`L=τ_true/α`, `gas_conduction_h_eff`'s own "never an optical/
   extinction-derived length" bar) — deferred at Iteration 38, deferred
   again at Iteration 39, disclosed-not-resolved a third time this
   cycle. This is logically *prior* to the bracket question in §4: if
   1051.2µm is not a licensed conduction length at all, the rear-only
   bracket endpoint's own witness-scale number needs to be re-derived
   under a different `L` before it is even asking the right question,
   independent of which boundary condition eventually wins. Three
   cycles of correct disclosure without resolution is long enough that
   this should be a committed, not merely carried-forward, Iteration-41
   item.
2. **Pin the record-blackness/Vantablack-class CNT forest's own
   pitch/diameter** — carried forward from Iteration 39's own ranked #1,
   still unaddressed this cycle (a different physical quantity from κ,
   correctly out of this cycle's own scope). Now doubly valuable: it
   would close the standing near-field-coupling/`l_geometric_m`
   homogenization question (T9-adjacent, EM's own Iteration-39 top pick)
   *and* let a future κ search target the SAME specific material class
   this program's α/n_eff citations use, closing Idealization 3's own
   "adjacent application class" caveat for κ as well as for α — one
   search, two open threads.
3. **[THERMO-owned, explicitly de-prioritized this cycle, see §4]**
   Once (1) resolves the length question and MATERIALS' own literature
   line has something concrete to say about real coating-on-substrate
   mounting, compute the front-colocated-vs-rear-only bracket at whatever
   the resulting `L` and deployment geometry actually are. Not worth
   accelerating ahead of items 1–2: this cycle's own numbers show both
   bracket endpoints comfortably clear every threshold, and resolving the
   bracket without first fixing the length question underneath it risks
   answering the wrong version of the question a second time.

**Process item, not ranked (Phase-5 close, not Iteration-41 scope):** add
`NOTES.md`'s missing `Result`/`Learned` sections per §2 before this
cycle's record is treated as closed.

---

## 9. Ruled-out / refuted-claim registry check

**No re-proposal found.** R1–R5 are all inapplicable — this cycle
proposes no T1 mechanism and scores no constraint-1/2/3/4 metric anywhere
in the record ("T1 escape route: N/A," honestly declared and true on
direct inspection of `phase1_proposal.md`, `NOTES.md`, and
`phase4_results.md`). T5 (the thermo ledger thread this cycle's own work
belongs to) is correctly extended, not contradicted — this cycle adds the
first-ever sourced κ_solid to a sidecar whose T5 entry has always flagged
that gap. T22/T23 are correctly inherited and, per §5 above, genuinely
reconciled rather than merely asserted compatible. No thread in T1–T26
makes any claim about CNT-forest through-thickness thermal conductivity,
Biot-number boundary conditions, or front-surface conduction correction
factors — this is new ground for the program's record, not a restatement
of anything already closed. No unfalsifiable claim, inexpressible
mechanism, or quietly-dropped constraint found anywhere in this cycle's
own text.

---

## Summary for the Director

The physics and the process both hold up under an independent,
fresh-context re-check: every headline number reproduces to the printed
digit, both new registry entries pass live with their forward tripwire
intact and unfired, and the one open structural question this seat was
specifically asked to weigh in on (§4) is real, correctly assigned as a
joint THERMO/MATERIALS item, and correctly de-prioritized given how far
this cycle's own numbers sit from either bracket endpoint's own
threshold. The one actionable gap I found independently (§2, `NOTES.md`'s
missing `Result`/`Learned` sections) is a Phase-5-close item, not a
defect in Phase 4's delivered result. Verdict: **PROMISING**.
