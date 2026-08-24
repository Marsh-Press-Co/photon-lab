# exp-068 — Block ARTICLE Settled-STEPS Re-Verification (T27 closure, part 2) (panel Iteration 45)

**2026-08-24 · driver: Clyde as panel Director · status: predictions
committed, run not yet executed**

Forty-fifth experiment of the panel program (PANEL.md / LOGBOOK.md). Lead
seat: **ELECTROMAGNETISM** (rotation — VISION SCIENCE → PHOTONICS →
MATERIALS → ELECTROMAGNETISM → THERMODYNAMICS → QUANTUM OPTICS → repeat;
Iteration 44 was MATERIALS). Executes the Iteration-44 Red-Team-ranked
queue item 2 (PLAN.md/LOGBOOK.md, verbatim): *"VISION's Block-ARTICLE
settled-STEPS FDTD leg (T27), now FOUR consecutive cycles (Iterations
42→43→44) without being a cycle's primary FDTD work... Pre-committed,
capped scope per VISION's own Phase-5 flip condition: article-present legs
at minimum the ±35°/600–750nm pair, STEPS≥2800, ceiling ~30–45 FDTD calls."*

## Hypothesis

`experiments/065-t24-absorb-boundary-sweep` (Iteration 42) built Block
ARTICLE — a τ_center=0.0065 uniform `off_pass`-analog disk, the *only*
construction in this program's history to ever produce a scored
constraint-3 PASS/MARGINAL number — and scored it entirely at
`STEPS=1400`, on the exact plane/tapered-source empty-scene channel that
same cycle showed is **NOT settled** by 1400 steps at near-grazing angles.
exp-066 (Iteration 43) closed the analogous gap for the *empty-scene*
channel (Block MAIN, all 36 mandate cells settled-verified at STEPS≥2800)
but explicitly left Block ARTICLE's own article-present legs untouched —
the P-VIS42-6/7 predictions from exp-065 remain RETRACTED, not
re-verified. **Hypothesis (ELECTROMAGNETISM's passivity argument,
extending exp-066's own finding one level up):** the channel's settling
behavior is governed by the domain's graded-loss boundary, a passive
dissipative termination with no thermodynamic obligation for its converged
residual to trend toward zero. The τ=0.0065 disk is optically thin — a
small linear perturbation introducing no new long settling timescale of
its own. So the article-present channel's settling shift (STEPS=1400→2800)
should track the empty channel's own settling shift in magnitude and
character, not converge to something smaller or safer merely because an
absorber is present. This is a falsifiable causality/passivity claim, not
an assumption — see the pre-registered bands below.

## Setup

Reuses exp-065's own `CONFIGS["C40"]`/`["C80"]` and `_one_run`/`_profile`/
`_c_empty`/`_c_n9` harness directly (`design_geometry.py`'s import-
collision-safe loading mechanism, same pattern exp-066 established).
**Zero new `lab/` engine code** (verified live, `_lab_diff_excluding_
registry()`, before this predict-commit).

| Knob | Value | Source |
|---|---|---|
| Geometry | exp-065's `CONFIGS["C40"]`/`["C80"]`, unchanged | `design_geometry.py` |
| Article | τ_center=0.0065 (`TAU_OFF_PASS`), σ_e=4.1667×10⁻⁵ (`SIGMA_OFF_PASS`), R_OUT=78 cells | exp-065's own Block ARTICLE, bit-identical |
| STEPS (baseline) | 1400 | exp-065's own original Block ARTICLE |
| STEPS (settled) | 2800 | exp-065/066's own established convergence floor |
| STEPS (stress) | 4200 | this cycle's own Tier2 |
| Wavelengths | 600nm (full N9), 750nm (Tier0/Tier2 ±35° pair only — first-ever article-present data at this λ) | mandate's own minimum scope |
| Angles | Full `FALLBACK_ANGLES` = (−35,−25,−15,−5,0,5,15,25,35) at 600nm; ±35° only at 750nm | exp-065's own N9 set |
| GATE_HARD | 0.001 | exp-024/041's own per-angle instrument-floor gate |
| C_THR_LAB | 0.005 | T2 frozen photopic lab bar |
| MARGINAL band | [0.5,2.0]× C_THR_LAB = [0.0025, 0.01] absolute | `lab/glare_sidecar.py::tier_w_verdict` convention |
| Baseline (STEPS=1400, N9, article row) | C=−0.004503 (C40) / −0.004602 (C80), both MARGINAL | `experiments/065-.../results.json::block_article::per_config`, loaded programmatically — never hand-typed (R4) |

### Call budget — final design (Phase-3 synthesis + two Director build-time corrections, see `run.py`'s own docstring for the full disclosure)

| Block | Content | Calls |
|---|---|---|
| Tier0 (mandatory floor, article) | Article-present, ±35°×{600,750}nm×{C40,C80}, STEPS=2800 | 8 |
| Tier0b (mandatory floor, empty — **build-time correction 1**) | Empty scene, ±35°×600nm×{C40,C80}, STEPS=2800 | 4 |
| Tier1a (N9 recert, article) | Article-present, 7 interior angles×{C40,C80}×600nm, STEPS=2800 | 14 |
| Tier1b (N9 recert, empty) | Empty scene, 7 interior angles×{C40,C80}×600nm, STEPS=2800 | 14 |
| Tier2 (convergence-generalization stress) | Article-present, θ=−35°×{600,750}nm×{C40,C80}, STEPS=4200 | 4 |
| **Total** | | **44** (ceiling 45) |

**Build-time correction 1 (self-caught, disclosed, not silently fixed):**
the Phase-1 proposal (endorsed through five blind Phase-2 critiques and
Red Team's own audit — no seat, including Red Team, caught this) assumed
the ±35° empty-scene companions needed for the N9 aggregate could be
*cited* from `settled_sweep_steps2800_diagnostic.json` at zero marginal
cost. That file stores only the reduced scalar `C_empty = weber(obj_mean,
flank_mean)` per cell; `lab.ambient.contrast_from_runs`'s N9 aggregate
needs the **raw profile** for every one of the 9 angles (per-component
flank normalization inside `incoherent_sum` does not reduce to a function
of the scalar alone once ≥2 angles with different flank levels combine).
Tier0b (4 calls) supplies the true marginal cost of this leg, verified via
the harness-continuity gate below.

**Build-time correction 2:** the original P-068-4 ("750nm ±35° bracket vs
600nm ±35° bracket, predict 750nm shift LARGER") implicitly assumed a
STEPS=1400 article-present baseline exists at 750nm. It does not — exp-065's
own Block ARTICLE was 600nm-only, and `results.json` stores only the
N9-aggregate STEPS=1400 baseline, never a per-angle breakdown, at any
wavelength. P-068-4 is reformulated below to compare Tier0/Tier2's own
within-cycle STEPS=4200-vs-2800 convergence deltas between the two
wavelengths (both computed this cycle) rather than a nonexistent
cross-STEPS delta at 750nm.

Tier0 and Tier0b/Tier2 together are the mandatory floor — never de-scoped.
If a hard-stop is approached, Tier1b is trimmed first, then Tier1a.

## T1 escape-route statement

**N/A.** Instrument/model-fidelity re-verification class, identical to
exp-041/exp-064/exp-066. No σ(I), σ(x,t), angular-selectivity, or
sub-threshold machinery is touched, advanced, or claimed. Constraint 3 is
not directly at stake this cycle (see mandatory fix 5/GATE_HARD_M3_NOTE
below — a GATE_HARD tally is an instrument-floor statistic, not a
constraint-3 verdict).

## Panel record

Full five-phase cycle preserved verbatim: `phase1_proposal.md`
(ELECTROMAGNETISM, lead), `phase2_critique_{photonics,materials,
thermodynamics,quantum,vision}.md` (five blind critiques, all
support-with-changes), `phase2_redteam_audit.md` (Red Team's final audit —
verdict PROCEED-WITH-MANDATORY-FIXES, a 7-item reconciled docket),
`phase3_synthesis.md` (Director's synthesis — all seven mandatory items
accepted, zero overrides, plus one Director-caught arithmetic correction
in Red Team's own reconciliation, and — disclosed here — two further
Director build-time corrections found while implementing `run.py`, above).

## Mandatory fixes applied (Red Team's docket, Phase 3)

**1.** Deferral-count correction: this is the **FOURTH** consecutive cycle
(Iterations 42→43→44→45) Block ARTICLE's article-present legs have not
closed at settled STEPS — exp-065 (144 calls) and exp-066 (39 calls) each
fully dedicated a cycle to the surrounding T27 thread without reaching it;
exp-067 explicitly deferred it a third time. This cycle is the first of
the four in which it is the cycle's own primary, dedicated FDTD work. A
failure to complete the mandatory floor must be disclosed as a **FIFTH**
consecutive miss, not a fourth (corrected from the Phase-1 proposal's own
miscount, caught by VISION SCIENCE's Phase-2 critique and confirmed
against `PLAN.md`/`LOGBOOK.md`'s own Iteration-44 close text by Red
Team's direct read).

**2.** Tier0/Tier1 double-count fix (Red Team's own Attack 1, self-found —
no seat caught this): Tier1's article-present block is the 7 **interior**
`FALLBACK_ANGLES` only, not all 9 — ±35° is already covered by Tier0.

**3.** Tier2 extended to both C40 and C80, both wavelengths (PHOTONICS'
flip, Red Team's disambiguation of a mechanically ambiguous flip
condition) — STEPS=2800 was never independently confirmed settled at the
highest-stakes cell (θ=−35°/750nm, the one that sign-flips) for *either*
config; Tier2 now tests both.

**4.** `T5_THERMAL_CAVEAT`, `REALIZABILITY_MEMO_CAVEAT`, and
`G_TRANSFER_T15_CAVEAT` (all three, verbatim from exp-065's own
`design_geometry.py`) are carried into every site stating Block ARTICLE's
C value or PASS/MARGINAL bucket (THERMODYNAMICS' flip, elevated to
mandatory by Red Team's own Attack 7: exp-065's Phase-5 Red Team audit had
already flagged registering a lint entry for this as "recommended before
any future cycle cites this article's caveats" — this is that cycle).

**5.** exp-066's own Phase-5 mandatory fix M3 sentence — *"GATE_HARD is
not VISION's own perceptual bar, and this result does not by itself move
any constraint-3 verdict"* — carried verbatim to every site reporting a
GATE_HARD tally (P-068-1, P-068-5). This is Red Team's own catch (Attack
3), the hidden constraint-3 angle no seat, including EM's own Phase-1
proposal, surfaced: a bare "≥12/14 pass GATE_HARD" headline is liable to
misreading exactly like exp-066's own 31/36→34/36 headline was, absent
this scoping sentence.

**6.** REALIZABILITY_MEMO.md contingency (MATERIALS' flip): if the
article-row C (N9, 600nm) flips PAST MARGINAL_LO=0.0025 at either config —
a live outcome, not a remote one, per exp-065's own Phase-5 correction
showing the exact −35° cells feeding this aggregate sign-flip by
0.0055–0.0065 in the empty channel alone under this identical STEPS
correction — this same-shift close must open a `REALIZABILITY_MEMO.md`
Amendment 2, not merely relabel `results.json`/caveat_lint. Coded as an
explicit, loud check in `run.py`'s scoring (`realizability_memo_amendment_
needed`), not silently absorbed.

**7.** `lab/caveat_lint_config.json`'s `exp065-steps1400-unsettled-plane-
channel` entry widened (Red Team's own Attack 6, applied as a disclosed,
separate step, not gated by this file's own `_lab_diff_excluding_
registry()` — same precedent as exp-066's own mandatory fix D) to add
exp-068's own `NOTES.md`/`phase4_results.md` to `required_sites`.

**8 (nice-to-have, applied).** QUANTUM's Block-MINI citation tripwire: the
14 new interior-angle empty-scene settling-delta cells (Tier1b) may NOT be
cited on T21's mechanism-vs-artifact question (whether the edge-diffraction
fringe is a genuine optical effect or a settling artifact) until Block
MINI's own properly-powered dense angular scan (≥2–3 T21 periods at
~0.2° spacing, settled STEPS) runs — these 14 cells are at 5° spacing, the
same statistical underpowering QUANTUM's own Phase-5 self-catch relabeled
P-VIS42-10 UNDECIDED over.

## Idealizations (numbered, per lab convention)

1. **2D TMz.** As with all prior work on this channel.
2. **Bench scale only** (r=78 cells). No witness-scale bridge — T8/T13/T14
   remains unclosed.
3. **The article is an analog, not a re-measurement** — shares τ and
   construction idiom with `off_pass` (exp-032), not exp-032's own domain.
4. **`REALIZABILITY_MEMO.md`'s own Amendment stands unless triggered
   (mandatory fix 6).** τ=0.0065 no longer clears the realizability bar at
   any geometry checked; this cycle probes instrument uncertainty, and
   only opens an Amendment if the settled-STEPS reading itself crosses the
   MARGINAL_LO line.
5. **Incoherent N9 quadrature is not converged** (T16/T21) — this cycle's
   settling delta sits on top of that already-uncharacterized uncertainty,
   not disentangled here.
6. **Block MINI's period-match question stays UNDECIDED** — nothing here
   bears on whether T21's fringe is a genuine optical effect or a settling
   artifact (mandatory fix 8's tripwire exists precisely to prevent this
   cycle's own interior-angle data from being misread as bearing on that
   question).
7. **The passivity argument in the Hypothesis is a physical expectation,
   not a proof** — the pre-registered bands below are set wide enough to
   be genuinely falsifiable against it, not to guarantee CONFIRM.
8. **Interior-angle empty-scene legs (Tier1b) have never been run at any
   STEPS beyond 1400 before this cycle** — P-068-5's grazing-vs-interior
   asymmetry prediction is reasoned from T21's own near-grazing geometry,
   not from any prior interior-angle data point.
9. **`_c_self` (this file's own helper) applies exp-065's own `_c_empty`
   reduction to an ARTICLE profile, not only an empty one.** Verified
   directly from `lab/ambient.py`'s `incoherent_sum`/`weber` definitions
   before this file was written: for a single-profile call, the
   per-component flank normalization cancels exactly in the Weber ratio,
   so `weber(obj_mean(p), flank_mean(p))` is independent of whatever
   profile the *pairing* empty run would have supplied — the function is
   content-agnostic, not label-agnostic. This is a mathematical identity
   of `lab/ambient.py`'s existing code, re-derived and confirmed by a live
   comparison (see `run.py`'s `gate_harness_continuity`, P-068-0), not a
   new claim about the physics.
10. **`bucket()`'s MARGINAL_LO/MARGINAL_HI are multipliers on C_THR_LAB
    (0.5×/2.0×), not absolute thresholds** — the absolute band is
    [0.0025, 0.01], matching exp-065's own `bucket()` function in
    `experiments/065-.../run.py` line 509–512 exactly (re-derived
    independently here, not copy-pasted, and cross-checked against that
    source before this predict-commit — the Phase-1/Phase-2/Red-Team
    record above all cite [0.0025,0.01] correctly in prose; this
    idealization records that the *code* implementing it must use the
    multiplier form, a distinction that has bitten other cycles in this
    program's history when GATE_HARD and C_THR_LAB were conflated).
11. **STEPS=1400 is NOT settled** on this channel at near-grazing angles
    (exp-065's own finding, reconfirmed by exp-066's Block MAIN closure) —
    stated here per `lab/caveat_lint_config.json`'s
    `exp065-steps1400-unsettled-plane-channel` entry, whose
    `required_sites` this cycle's own files now satisfy (mandatory fix 7).

## Predictions (committed BEFORE `run.py`'s first FDTD call)

See `run.py`'s own `FROZEN_PREDICTIONS` string, printed structurally at
the top of every run (exp-046/exp-065/exp-066's own structural-freeze
precedent) — reproduced here verbatim for the git record:

- **P-068-0** — harness-continuity gate (HALTS if it fails).
- **P-068-1** — empty N9 floor, settled, 600nm, both configs: CONFIRM ≤ GATE_HARD.
- **P-068-2** — article row C, N9, 600nm, settled vs 1400: CONFIRM |ΔC|≤1.5e-3, MARGINAL bucket stable, sign stable. Pre-registered flip thresholds stated.
- **P-068-3** — sign persistence.
- **P-068-4** — 750nm vs 600nm relative convergence (REFORMULATED, build-time correction 2).
- **P-068-5** — GATE_HARD count, 14 interior empty legs.
- **P-068-6** — Tier2 convergence-generalization stress, all 4 cells.

Full text with exact CONFIRM/REFUTE bands: `run.py::FROZEN_PREDICTIONS`.

## Result

44/44 FDTD calls, 7.1 min wall-clock. P-068-0 (harness continuity) PASSED
bit-exact. **P-068-1 REFUTED**: the settled empty N9 floor breaches
GATE_HARD for C40 (0.001138 vs 0.001 bar) — extends exp-066's own
"GATE_HARD gets worse, not better, at settled STEPS" finding to the
N9-aggregate level for the first time; per mandatory fix 5, this does not
move any constraint-3 verdict. **P-068-2/3 CONFIRMED — the headline
result**: Block ARTICLE's own scored article-row C is re-certified at
settled STEPS≥2800 for both configs, shift bounded (15–24% relative, both
inside the pre-registered band), bucket unchanged at MARGINAL, sign
unchanged at negative — the four-cycle-old retraction (P-VIS42-6/7) is
resolved, not merely re-attempted. P-068-4 PARTIAL (config-dependent, both
values tiny in absolute terms). **P-068-5 CONFIRMED 14/14**: interior
angles show none of the grazing-angle settling defect. **P-068-6
CONFIRMED 4/4**: STEPS=2800 independently verified converged for the
article-present channel at the highest-stakes cell, both wavelengths, both
configs — the assumption every other number in this cycle rests on is no
longer merely asserted. Full detail: `phase4_results.md`.

## Learned

1. The instrument-floor settling defect exp-066 found on individual
   grazing-angle empty-scene cells (GATE_HARD worse at 2800 than 1400)
   **generalizes to the incoherent N9 aggregate** — summing 9 angles does
   not average it away, at least not fully (C40 breaches, C80 does not).
2. **The article-present channel is more robust to the settling
   correction than the empty-floor-alone headline suggested.** The
   scored, constraint-3-relevant quantity (article row C) shifted by a
   bounded amount and did not change disposition — EM's passivity
   argument (settling shift tracks the boundary's own passive character,
   proportionate not catastrophic) held up as a genuine, falsifiable
   prediction, not just a plausible-sounding hope.
3. **STEPS=2800 is confirmed settled for the article-present channel** at
   the one cell this program's whole T27 thread has been most uncertain
   about (θ=−35°, both wavelengths) — a load-bearing assumption this
   cycle inherited from the empty-channel-only exp-065/066 record is now
   independently checked on the channel that actually matters for
   constraint 3.
4. **Process lesson (both build-time corrections):** a proposal endorsed
   by five blind critiques and a Red Team audit can still contain a
   materially wrong resource-citation claim (Tier0b) and an ill-posed
   comparison against nonexistent data (original P-068-4) — neither is a
   physics error, both are the kind of implementation-detail gap that
   only surfaces when someone actually builds the code, not when six
   independent readers review its prose description. Building the
   harness IS a review pass, not merely execution of an already-settled
   design.

## Next

1. **T27 is now substantially closed** for Block ARTICLE's own
   article-present legs at 600nm (full N9) and the ±35°/750nm pair. The
   only remaining named T27 sub-item is Block MINI's period-match test
   (queue item 3), explicitly out of scope here (mandatory fix 8's
   tripwire).
2. P-068-4's split result (750nm worse than 600nm at C40, opposite at
   C80) is a minor open point — not urgent given P-068-6's own strong
   absolute-convergence confirmation, but worth a one-line note in any
   future cycle that revisits 750nm settling behavior.
3. The C40 GATE_HARD N9-aggregate breach (P-068-1) is a genuine new
   instrument-characterization data point, not previously measured at
   this aggregation level — worth folding into any future write-up of
   this channel's own settling-defect scope (T27's own closure summary),
   though it does not itself require action per mandatory fix 5.
