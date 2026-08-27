# PHASE 1 — PROPOSAL · Panel Iteration 59 · exp-082
## The PAD-loaded real-article check — the first genuinely new FDTD-requiring test in the T28 y-wall/PAD sub-thread since exp-069 (Iterations 46-58)

**Seat: QUANTUM OPTICS.** Lead by rotation. Fresh sub-agent, zero memory of
any prior session. Read, in order: `PANEL.md`, `AGENTS.md`, `LOGBOOK.md`
(RULED OUT R1-R9 in full, ESTABLISHED, LIVE THREADS T28 in full — Iterations
46-58), `PLAN.md`'s Iteration-59 queue, `experiments/081-.../` in full
(especially `phase5_redteam_audit.md`), `experiments/075-.../` and
`experiments/077-.../` (the x-wall models), `lab/validation/run_all.py`'s
gate pattern, `experiments/065-.../design_geometry.py` (`dg065.CONFIGS`),
and every "real absorbing article" scoping discussion across
`experiments/076-081/phase5_review_vision.md` and siblings.

**No RULED-OUT item (R1-R9) is re-proposed or re-litigated.** This is
instrument-fidelity/generalization work — a scene-realism check on an
already-characterized boundary-artifact channel — not a constraint-3
mechanism proposal, an integer-λ/shell-thickness claim, or a re-litigated
ground-truth/null-calibration gate.

---

## 0. Which route this cycle takes on item 7, and why

**Route (a): build and run the PAD-loaded real-article check as this
cycle's own primary item.** PLAN.md's tripwire is explicit and load-bearing:
item 7 has been deferred SIX consecutive T28 cycles (076-081), ranked #1 by
two Phase-5 seats and #2 by three more at Iteration 58, and a seventh
deferral without an explicitly stated reason fires Checkpoint criterion 4
outright — "not weighed as a close call again." Every deferral to date has
had a *good* reason (each prior cycle's own zero-FDTD Tier-0 scope was
genuinely, near-unanimously, the correct thing to build first) — but this
cycle's own Tier-0 batch (item 1, the x-wall realizable-admittance refit;
items 2-3, hygiene) is cheap enough to fold in as riders (§6-7, below)
without displacing this item. There is no remaining scheduling reason to
defer a seventh time, so this cycle builds it.

This is also, independently of the tripwire, the single most information-
dense open question on the T28 board by the Phase-5 audit's own words: "the
only queued item that tests whether ANY of this nine-cycle sub-thread's
findings... bear on a scene with a real absorbing article rather than free-
space domain-boundary geometry alone." Every T28 cycle since exp-069 has
run on an **empty scene** — confirmed directly, again, this cycle: `grep -n
"materials\." experiments/069*/run.py experiments/076*/run.py
experiments/077*/pad_round_trip_model.py` returns zero hits. `C_thr` is a
threshold on an object-vs-background Weber contrast; the whole nine-cycle
sub-thread has only ever measured the *background* half of that
comparison. The correctly-scoped version of "does this bear on
perceptibility," per VISION's own Iteration-53/54/55 findings (exp-076 §
Phase-5, exp-077 §Phase-5, exp-078 §Phase-5): load a real absorbing article
at the bench's own established object location and see whether the
empty-scene PAD-sensitivity axis survives the object-minus-flank
subtraction real constraint-3 scoring performs, or cancels as a shared
background term.

---

## 1. Mechanism narrative (≤300 words)

`PAIR_PAD ≡ (C40, G40)` is this sub-thread's own largest, best-established
empty-scene finding (Iteration 53, exp-076): two configurations sharing an
IDENTICAL `ABSORB=40` boundary (so the damping-mask's reflectance magnitude
is structurally guaranteed identical, proven from `lab/fdtd2d.py`'s own
primitives) but differing only in `PAD` (pure vacuum domain-extension, zero
absorbed-power effect) produce a real, resolution-robust, non-noise
oscillation in `C_empty(θ)` — this program's own **empty-scene proxy**
channel for the ambient-contrast instrument. Every subsequent cycle
(077-081) narrowed *what kind* of coherent-echo mechanism could explain it
(x-wall unrealizable-admittance: REFUTEd twice; y-wall echo, single-edge
and full-aperture-sum: structurally foreclosed twice; the plane-wave/
global-steering total-field construction, PHOTONICS' own specification
built in full: REFUTE-leaning, proven pair-specifically not to need wall
reflectance at all for its lone SUPPORT) — but no cycle has ever asked
whether this artifact, whatever its mechanism, actually reaches the
**scored** channel: real Weber contrast `C(θ)`, computed the way
`lab/ambient.py::contrast_from_runs` computes it for every constraint-3
citation this program has ever issued, with an object physically present
in the object window.

Two structurally different outcomes are both informative and neither is
presupposed: (i) the PAD confound is a pure background/instrument
systematic that **cancels** in the object-window-vs-flank-window
subtraction real scoring performs (the flank windows see the SAME
domain-padding artifact the object window does, and Weber contrast is a
*difference* of the two) — good news, closes the practical risk this
six-cycle sub-thread has carried without ever testing; or (ii) it **rides
through**, meaning every existing and future PASS/MARGINAL/FAIL citation at
a `FALLBACK_ANGLES`-adjacent geometry silently inherits a named,
now-quantified domain-construction confound this program has never
disclosed on that channel. T1 escape route: **N/A** — this is
instrument-fidelity work, not a mechanism proposal; zero constraint-3
engagement (no scored contrast is claimed as evidence for or against any
phenomenon-program mechanism here — this measures whether an *existing*
finding generalizes to a scene, nothing about the phenomenon itself).

---

## 2. Parameter table

| Parameter | Value | Source / justification |
|---|---|---|
| Configs | `C40` (ABSORB=40, PAD=0), `G40` (ABSORB=40, PAD=40) | `dg065.CONFIGS` — `PAIR_PAD`, the dominant, headline PAD-tied confound (Iteration 53's own "largest reading this cycle produced") |
| Article | `materials.pec_disk(sim, obj_x, obj_y, 30)` + `materials.graded_black_shell(sim, obj_x, obj_y, 30, R_OUT)` | The **established flagship absorber** — bit-identical to `exp-024/run.py::build("absorber")`, the exact construction LOGBOOK's ESTABLISHED section cites (stage-7-gated, coated-wall R≤0.2%, observer return = camera floor). Not a new variant — reused verbatim. |
| Article location | `(obj_x, obj_y)` per config — `170,792` (C40) / `210,832` (G40) | Already-defined `dg065.CONFIGS[key]["obj_x"/"obj_y"]` fields — present in the geometry dict since exp-065 but never materialized as a physical object in any T28 cycle |
| Article radius | `R_OUT=78` cells (`dg065.R_OUT`) | Established bench radius, shared with `W_OBJ=78` (the contrast-scoring window half-width) by this bench's own long-standing convention |
| Wavelength / cpl | 600 nm / 20 | This sub-thread's own established single-λ scope (every T28 cycle since exp-069) |
| Angles (reduced dense window) | θ ∈ {36,37,38,39,40,41,42}° — 7 points, 1° step | A **disclosed, reduced-power** subset of T28's own established 31-point/0.2°-step `[36°,42°]` dense window (exp-069 Block DENSE) — spans ≈2.1 periods of the established `P*=2.8421°` fringe. Chosen because these are EXACT grid points of the already-committed 31-point sweep (`(42-36)/0.2+1=31`), enabling a bit-level reproduction check of this cycle's own freshly-run empty leg against `experiments/076-.../results.json::headline` before the new (article-loaded) leg is trusted |
| STEPS | 2800 | T28's own established settled step count for this exact dense-window geometry at C40/G40/C80 (exp-069 Block SETTLE, `dg.STEPS_SETTLE`) — reused, not re-derived |
| Settling precondition (new, this cycle) | G40 + article, θ=39°, STEPS 1400 vs 2800 | Prior settling checks (exp-069) tested the EMPTY scene only; an article introduces new reflected-path lengths (article↔plane, article↔boundary↔plane) never settling-tested. One directional check, not a full R3-grade convergence study (disclosed limitation, §5) |
| Total new FDTD calls | 29 | 2 configs × 7 angles × 2 legs (empty, scene-with-article) = 28, + 1 settling-precondition call |
| Perceptual bar (context only, not gating T1) | `C_thr = gs.c_thr(3.0, 0.4, bar="lab") = 0.005` | T2's frozen photopic lab bar, already used throughout this bench (`dg065.C_THR_LAB`) |

---

## 3. T1 escape route

**N/A.** Matches every T28 cycle's own disposition since exp-069: this is
instrument-fidelity/generalization work on an already-characterized
boundary-artifact channel, not a constraint-3 mechanism candidate. No
scored contrast in this cycle is presented as evidence for or against any
phenomenon-program escape route.

## 3b. R6 applicability (synthetic ground-truth recovery gate)

**Does not apply.** R6 binds any estimator that fits a carrier- or
phase-conditioned coefficient. This cycle computes only raw, pointwise
Weber-contrast values (`C(θ)`, `C_empty(θ)`) at discrete angles via
`lab/ambient.py::contrast_from_runs` — no fitted nuisance parameter, no
carrier phase, no regression. Stated explicitly per the task brief's own
instruction to address R6 applicability every cycle.

## 3c. New machinery / trust-suite gate

**None added.** Every primitive reused is already gated: `lab.Sim` (core
engine, suite stages 1-6), `lab.materials.graded_black_shell`/`pec_disk`
(stage 7), `lab.ambient.observer_profile`/`contrast_from_runs` (stage 9),
`lab.sections.full_capture`/`phasors` (core). `dg065.CONFIGS` is
established, reused geometry, zero new construction. `git diff --stat --
lab/` is verified empty both before and after this cycle's work (§8). No
new suite stage is added; none is required.

---

## 4. Predictions — pre-registered falsifiable bands (committed BEFORE the run)

**Primary metric.** For each of the 7 angles, compute real Weber contrast
`C(G40;θ) − C(C40;θ)` (scene, article present) and, from this cycle's own
freshly-run empty leg at the identical 7 angles, `C_empty(G40;θ) −
C_empty(C40;θ)`. Let `A_scene = ptp(ΔC_scene)`, `A_empty = ptp(ΔC_empty)`
(peak-to-peak amplitude over the 7-point window), `ratio = A_scene /
A_empty`.

- **SURVIVES** (the confound reaches the real scoring channel at comparable
  scale): `ratio ∈ [0.5, 2.0]`.
- **CANCELS** (the object-minus-flank subtraction removes it):
  `ratio ≤ 0.2`.
- **INCONCLUSIVE**: `0.2 < ratio < 0.5`, OR `ratio > 2.0` (amplification —
  not presupposed either direction; genuinely surprising, flagged for
  follow-up, not silently folded into SURVIVES).

**Secondary, disclosed-not-gating metric.** `A_scene` vs `C_thr=0.005`:
report `A_scene / C_thr` directly — informative regardless of the
ratio-based verdict, since it states independently whether this specific
confound, at real-scene scale, could ever be perceptually load-bearing on
its own (mirrors this program's own R9-corrected `PAD_TIED`
commensurability convention: compare only like-normalized quantities to
`C_thr`, never a fitted-carrier-normalized one).

**Reproduction precondition (must PASS before either verdict above is
trusted).** This cycle's own freshly-run empty leg at the 7 shared angles
must reproduce `experiments/076-.../results.json::headline`'s C40/G40
values at those same integer-degree points to float-precision (`max|Δ| <
1e-9`) — the R4 discipline this whole sub-thread has followed throughout:
never trust a new number until it reproduces an already-committed one it
should equal exactly.

**Settling precondition (disclosed, not gating — see idealization below).**
`|C(G40, θ=39°, article, STEPS=2800) − C(G40, θ=39°, article, STEPS=1400)|`
reported for context. No pre-registered pass/fail threshold, since this is
a single directional check, not the full R3-grade convergence protocol —
disclosed as reduced-power, not gated as though it were.

---

## 5. Idealizations

1. **Single wavelength (600 nm)** — matches this entire sub-thread's own
   scope since exp-069; wavelength generality is a separately-tracked,
   also-six-cycles-deferred item (Tier 1 item 8, this cycle's own board),
   not this cycle's job.
2. **7-angle reduced dense window, not the full 31-point/0.2° sweep** —
   budget-motivated; disclosed explicitly, not claimed as a full-power
   replication of T28's own `P-069`-style period-fit machinery. Spans ≈2.1
   periods of the established fringe — enough to see whether an
   oscillation of comparable *scale* survives, not enough to re-fit a
   precise period with this cycle's own statistical power.
3. **One pair only (`PAIR_PAD`, C40 vs G40)** — the dominant, headline
   confound (Iteration 53's own largest reading); `PAIR_ABSORB40`
   (G40 vs C80) and the full `C80−C40` comparison are not re-tested this
   cycle. If `PAIR_PAD` SURVIVES, a natural follow-up extends this same
   harness to the other two pairs.
4. **Single settling-precondition spot-check, not a full R3-grade
   convergence study** — disclosed, §4. A real, unaddressed limitation:
   this cycle cannot rule out that the article-loaded scene needs more
   than STEPS=2800 to fully settle at some angles even if the one spot-
   check at θ=39° looks clean.
5. **The established flagship absorber only** — `graded_black_shell`
   (PEC-cored, matching `exp-024`'s "absorber" construction) is the one
   article tested. A weaker σ(I)-style near-null article (`off_pass`,
   already used by exp-065's own pre-T28 Block ARTICLE) is not re-tested
   here; if this cycle's result is SURVIVES, a weaker-absorption article is
   a natural next comparison (does the confound's visibility in `C` scale
   with how strongly the article itself extinguishes the field).
6. **Object window = flank windows share the SAME dense-angle geometry as
   the object present** — `contrast_from_runs`'s flank-window computation
   (`GUARD_OUT`/`W_FLANK`) is unchanged by the article's presence (the
   article sits at `R_OUT=78` from `obj_y`, well inside `GUARD_OUT=185` —
   verified no geometric overlap, §2). This is a construction fact, not an
   assumption requiring a separate check.
7. **Interception/energy-budget accounting is out of scope for this test**
   — this cycle measures the OBSERVED contrast delta directly (an FDTD
   measurement), not an analytic power-budget estimate; THERMODYNAMICS'
   own energy-sidecar convention (post-run analytic, zero FDTD) does not
   apply to this item, which is itself the FDTD measurement.
