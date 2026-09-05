# exp-115 — Panel Iteration 92

**Runner: bench panel shift (T5820) — Director Clyde, live session.**

## Phase 1 — Propose (MATERIALS & METAMATERIALS)

See `phase1_proposal.md` in full. Executes the Reconciled Iteration-92
queue's **Tier-1 item 1** — a genuine same-session control-timing burst
measured **directly on the r=234 grid** (`N=2100`), matched-protocol
against the r=156 grid (`N=1400`) in the same session, with EM's bundled
immediate repeat — plus **Tier-1 item 2** (the `..._DO_NOT_SCORE`
sensitivities, folded in at zero marginal cost) and **Tier-1 item 5**
(MATERIALS' own fabrication-tolerance bound, named-but-undone for seven
consecutive cycles, folded in as a clearly-labelled analytic sidecar at
zero FDTD cost).

Verified before proposing (R4/R9): **no control burst has ever been timed
on any grid but r=156 in this program's history** — `_time_control_blend`
hardcodes `geom_fixedabs_cpl(156, 25)` in both `chunk_runner113.py` and
`chunk_runner114.py`, and "cross-grid" exists only as prose, never as
executed code or a persisted field. And the load-bearing identity nobody
in exp-114 stated:

```
measured_ratio ≡ kappa_ratio × G,    G ≡ per-step(r=234) / per-step(r=156)
1.5 × 2.74550565394726 = 4.11825848092089   (exp-114's filed value, all 15 digits)
```

So exp-114 did not measure a cross-session cost ratio at all — it
measured `G`, and its residual confound is not cross-session
normalization but the **protocol mismatch** between a 12000-steps/scene
chunked numerator and a 3334-steps/scene cold-call denominator. This
cycle measures `G` directly, on both grids, in one session, at matched
step counts and matched scene mix: R33-immune by construction and free of
that protocol mismatch. **T1 escape route: NONE / N/A**, matching every
T28 desk/instrument cycle since Iteration 46.

## Phase 2 — Critique

Five blind critiques, all **support-with-changes**, zero opposition, plus
Red Team's audit — verdict **PROCEED-WITH-MANDATORY-FIXES** with a
fifteen-item docket (MF-1..MF-15), six disclosed-override
recommendations (OV-1..OV-6), and a program-level Checkpoint criterion-4
notification. Each seat's sharpest point:

- **PHOTONICS** (`phase2_critique_photonics.md`) — the physics. M9(c)'s
  `exp(−2·τ_true)` is the wrong functional form: the measured observable
  is a relative change in a **cross-section**, quadratic in the total
  field, whose leading term is the **coherent cross term**
  `2Re(A*δA)/|A|²`. The right scale is `exp(−τ_true) = 2.5896×10⁻⁴` and
  the right upper bound `2·exp(−τ_true) = 5.1793×10⁻⁴` — the draft was
  wrong by `exp(+τ_true) ≈ 3.86×10³`, in the paragraph R21 exists to push
  into LOGBOOK. It also showed the two family members are the **same
  optical article by construction**, not coincidence (`σ_max·cpl = 10`
  and `thickness/cpl = 2.40 λ` at both), and supplied the three-λ table
  (`2·exp(−τ)` = 3.58/5.18/7.35 ×10⁻⁴ at 450/600/750 nm): backing freedom
  is weakest in the red and has been measured only at 600 nm. Red Team
  called it the most thoroughly re-derivable critique of the five.
- **ELECTROMAGNETISM** (`phase2_critique_em.md`) — the run order and the
  ledger algebra. A3's closed-form drift algebra: under A,B,A,B both
  sustained pairs inherit a **same-signed** `(a+b)/2` lag, so the mean
  does not cancel it and `d_rep` — the cycle's only noise instrument —
  reads ≈0, an alarm structurally incapable of producing the reading that
  means "bad". A7 derived, from `lab/sections.py` alone, that
  `σ_ext_cross − σ_ext = F(pi)` is a function of the **empty** capture and
  the box alone, hence scene-independent — which kills M9(b)'s floor.
  A12(3) caught the assert/skip conflict; A12(1) that pure `N²` scaling
  lands **inside** the CONFIRM band.
- **THERMODYNAMICS** (`phase2_critique_thermodynamics.md`) — the sign
  conflict and the settling reason. From exp-114's own committed data:
  the first 3000 steps of the r=234 empty scene ran **4.467% SLOWER** per
  step than the 12000-step mean, i.e. per-step cost **fell** as the run
  went on — the opposite sign to `R_DEG = +7.596%` from the same
  session's own controls, and `run_control()` runs short-then-sustained
  with no counterbalance, so `R_DEG` conflates duration with elapsed
  position **by construction**. It also supplied the physical reason the
  energy ledger must be N/A (at 3334 steps the wavefront reaches only
  ~65% of the r=156 domain and ~47% of the r=234 domain, so a ledger from
  those fields would be a wrong number, not a free byproduct) and the
  exclusive-use requirement.
- **QUANTUM OPTICS** (`phase2_critique_quantum.md`) — the straddle
  arithmetic. B1 reconstructed the v2 straddle from primitives to every
  digit (`measured_ratio_v2 = 3.217195628521234`; sign boundary
  `G ≥ 2.5652851279677367`), showing that over **66.4% of M5's own
  CONFIRM band** the cycle would return "CONFIRM, replicated" while the
  straddle is still open — and that M6, titled "the direct answer to the
  v2 straddle", computes a quantity that never touches v2's construction.
  B10 supplied the admissible floor-gated per-bin figures.
- **VISION SCIENCE** (`phase2_critique_vision.md`) — the invocation and
  the registry. §4.7 executed M5's documented invocation literally and
  got `rel_dev = 0.44796720567305326` → **REFUTE**: a plausible-looking
  false verdict on the cycle's declared PRIMARY metric, invited by the
  document's own text. §4.8 demonstrated both caveat-registry
  blindnesses live (`UNOBTANIUM`/`unobtainium`; ASCII `alpha` / Unicode
  `α`). §4.9 raised the program-level constraint-3 drift Red Team then
  ruled on.

## Phase 3 — Synthesis (Director)

**All fifteen mandatory fixes accepted exactly as the docket states
them**, applied this shift, before any Phase-4 `Sim.run()` call.

| # | Fix | What changed |
|---|---|---|
| **MF-1** | the physics | `run115.py::sidecar_m9` reports the **coherent cross-term** form: characteristic scale `exp(−τ_true) = 2.5896×10⁻⁴`, upper bound `2·exp(−τ_true) = 5.1793×10⁻⁴`. `exp(−2·τ_true)` is persisted only under the key `proposal_figure_exp_minus_2tau_WITHDRAWN` with the factor it was wrong by. "The physical value is predicted at `O(10⁻⁷)`" is struck; M9(e)'s forward scaling is corrected to `exp(−τ_true)`. Idealization 9's concavity hedge is replaced by the **exact identity** (`σ_max·cpl = 10`, `thickness/cpl = 2.40` ⇒ `τ_true` bit-identical, recomputed `8.258813` at both members from `lab/materials._graded_black`). PHOTONICS' 3λ row is carried. |
| **MF-2** | the floor | M9(b)'s floor gate is **withdrawn**. The derivation and the numbers are persisted under `withdrawn_common_mode_statistic` and labelled a solver self-consistency statistic (`0.0` **exactly** at r=234, `2.27×10⁻¹³` at r=156 between scenes). exp-108's six-margin `item_ii` family is substituted as the only differential floor on file (`mean/std = 4.47×` at r=156, `11.70×` at r=312, sample std), with the explicit statement that **no differential floor exists at r=234**. The conclusion is rewritten: on the only differential floor available the effect is **resolved, not floor-limited**. |
| **MF-3** | the per-bin channel | `sidecar_m9` reports exp-110's floor-gated **local** normalization (`1.4669×10⁻²` at r=156, 34/48 resolved; `5.290×10⁻²` at r=312, 38/48) alongside the peak-normalized `1.5266×10⁻⁴`, states that the two largest resolved r=312 deviations sit at **±138.75°**, inside the observer-return hemisphere PANEL.md scores constraint 2 on, and **withdraws** the per-bin half of the "better than 1.6×10⁻⁴" claim. exp-112's ungated bins are not cited (0/12 backscatter bins resolved on that cycle's own gate). |
| **MF-4** | the scope | The bound is restated at the resolution its evidence certifies: **certified at margin=32 only** (the other five margins carry one boolean against a `5×10⁻²` *decision bar*, 330× looser); per-bin at cpl=20 only and aggregate at cpl=25 only, so **channel and resolution are fully confounded**; r=234 aggregate-only; "far-field" → near-to-mid-field box ledger at this bench's measurement geometry; "at all" → over the vacuum-to-PEC range tested at 600 nm, normal incidence, 2D TM. The constraint-3 failure, the realizability tier and the T18 evidentiary tier are all **inside** the quotable blockquote (`build_m9_bound_text`). |
| **MF-5** | the M5 invocation | `exponent_from_g()` computes `exponent_B = ln(1.5·G)/ln(1.5)` and `classify_m5()` feeds **that** to `R114.classify_kappa_exponent_check()` unmodified, with `assert abs(result["measured_ratio"] − 1.5·G) < 1e-12`. Verified live: `classify_m5(G_E)` reproduces exp-114's filed `rel_dev = 0.12274985147707763` **bit-exactly**, while the documented-literal route returns `0.44796720567305326` → REFUTE. |
| **MF-6** | protocol integrity | (a) The sustained pass is **ABBA** — `S156, S234, U156, U234, U234b, U156b` — and M2/M5 score on the **mean of the two pairwise G**, both persisted. (b) Per-reading start/end ISO-UTC timestamps, per-scene wall times and both pairwise `G`s are persisted **immediately, one reading at a time**. (c) Same-grid drift is reported as a **rate per unit elapsed time** (`drift_rate()`), because ABBA makes the two same-grid lags unequal (`a+2b` vs `b`). (d) `d_rep`'s semantics are restated as a **drift+noise** statistic, not a repeatability statistic, at every site that gates on it. (e) The **exclusive-use protocol** is stated in `chunk_runner115.py`'s own docstring and enforced procedurally; a machine-state block (lscpu/L3, THP, BLAS/OMP thread env, `numpy.show_config`, versions, hostname) is persisted once per run and `loadavg` before/after every reading. `--post-ticker` exists so the Director can follow the run without opening a second session on the bench. |
| **MF-7** | M5's power limit | (a) `protocol_mismatch_interval()` builds the two-point `p(n) = p_∞ + C_g/n` bound on each grid from the S and U readings already scheduled (exactly determined — it bounds, it does not fit, R7) and evaluates `G` at the burst protocol, the production protocol and the amortized limit; if the interval spans a band boundary, `m5_protocol_caveat=True` is persisted and M5 reports **BOUNDED-REPLICATION**, which explicitly may not move exp-114's LOGBOOK entry. (b) The Result prose states that pure `N²` scaling (`k = 3.0`, the pre-R28 exponent) gives `rel_dev = 0.0799`, **inside** the CONFIRM band. (c) The two protocol models are **pre-registered here, before the run**: `G ≈ 2.5403` (drift/degradation) vs `G ≈ 2.8681–2.8802` (warm-up amortization), on opposite sides of the CONFIRM ceiling `2.8121415`. |
| **MF-8** | the straddle | "Resolves the straddle" is **withdrawn** from the M6 title and from the cycle's framing. `sensitivity_v2_with_measured_G_DO_NOT_SCORE` is persisted with its signed deviation and the stated boundary `G ≥ 2.5652851279677367`, explicitly **not scored**. `DECLINE_8` adds the numbered §3 decline for the un-executable half of Tier-1 item 1. |
| **MF-9** | one boolean per rule | `m3_scored`, `m5_protocol_caveat`, `m6_directional_only` (**inverted**: directional-only unless M3 reads `G-DURATION-INVARIANT`, so PARTIAL / unscored / repeat-skipped all inherit the caveat), `m7_underpowered` — all persisted, all code. M4's MARGINAL is split at `0.03` and `R_DEG/2` into four labels that carry their own consequence. M3's labels are **mechanism-neutral** (`G-DURATION-INVARIANT` / `G-NOT-DURATION-INVARIANT`). M7's labels are **two-sided** (`N2_FAILS-SUPERLINEAR` / `N2_FAILS-SUBLINEAR`). The R19 call-count assert is **conditional** on `repeat_skipped` (18 or 12). |
| **MF-10** | `DISCLAIMER_115` | Its full text is written in this Phase-3 document and in `run115.py`, with **both** the predictions-side and result-side assert inside committed, re-invocable call sites — `run115.py --predictions-only` and `run115.py --selftest`, the latter invoking `build_result_text()` with synthetic operands **now**, at Phase 3, which is exactly the founding defect R23's First Addendum was written for. Minimum content carried: analytic-sidecar-not-FDTD; upper-bound-vs-resolved; **the article fails constraint 3 by construction**; the T18 tier; and the explicit **energy-ledger / thermal-sidecar N/A** sentence with THERMODYNAMICS' settling reason (~65% / ~47% domain fill at 3334 steps) — which also closes exp-104's own three-cycle-old named gap. |
| **MF-11** | the citations | "~14% costlier `peccored`" → the profiled **+1.287%** (peccored/hollow) and **+0.009%** (peccored/empty); Idealization 4's "≲5%" → the measured **8.83%** chunk spread **plus** the statement that chunk scatter cannot bound the 4.467% within-run level shift; "three independent energy-ledger channels" → **two independent channels and their exact algebraic sum**, with the residual `Δσ_scat + Δσ_abs − Δσ_ext` persisted (`0.0` exactly at r=234) and the note that at r=156 the two genuine channels partially cancel, which is the flattering direction. Both normalization conventions are disclosed as formulas (mean-normalized numerators; `peccored`-normalized withdrawn floors). |
| **MF-12** | identity gate | `chunk_runner115.py --identity-gate` runs **before any reading is trusted**: `build_sim`'s source segment is compared **byte-for-byte** against `chunk_runner114.py`'s (parsed out of the committed source with `ast`, no import, no side effects — `chunk_runner114` calls `os.makedirs` on a hardcoded scratch path at import time), plus `CONTROL_SCENES`, both step constants, the `geom_fixedabs_cpl(156, 25)` dict field-for-field, and confirmation that exp-114's own `_time_control_blend` really did hardcode r=156. **10/10 PASS**, zero FDTD. The trust suite is re-run **on the bench** and its console record committed (VALIDATION.md docket-14). |
| **MF-13** | the perturbation | Disclosed for what it is: vacuum → PEC over `rr ≤ R_CORE`, with **12 cells at exactly `rr = R_CORE`** both PEC-zeroed and maximally lossy (counted in code: 12/62,236 shell cells at r=156, 12/98,740 at r=234). The closing bound is computed rather than quoted (see the one disclosed forward correction below). |
| **MF-14** | the registry | `lab/caveat_lint_config.json`: the T18 entry now carries **both spellings** (`UNOBTANIUM`/`UNOBTAINIUM`) and **both alphabets** (ASCII `alpha`, Unicode `α`) as trigger terms, reaches `experiments/*/*.py`, and gains this cycle's `NOTES.md`/`run115.py`/`analyze115.py` as **required_sites**. A new entry, `exp115-t28-fabrication-tolerance-bound-certified-resolution`, gates the tolerance bound's **certified-resolution wording** at those same three sites. Verified: the old triggers return `False` on this cycle's text and the new ones `True`. |
| **MF-15** | the counterweight | exp-061's own MP-5 thermal rows are carried into M9(e), verified against that cycle's NOTES before quoting: **230× → ΔT_ss 5.277×10⁻³ K, margin 3.79×**; **730× → 1.4774×10⁻² K, margin 1.35×**, both UNDETECTABLE against NETD-lo 0.020 K — with the statement that the same thickening makes the article a physically larger black silhouette, constraint 3's own failure mode. THERMO's §7 warm-up sensitivity, if reported, is reported under consistent application: `rel_dev` spans `0.1227 → 0.2977` (**CONFIRM → AMBIGUOUS**, not CONFIRM → REFUTE). |

### The six disclosed overrides (each on Red Team's own recommendation)

1. **OV-1 — QUANTUM's M10, scored half: DECLINED.** Adopted as a
   NOT-scored sensitivity per MF-8. `1.5·G_bench·(p_prod/p_burst)`
   composes a bench-measured `G` with exp-114's own session's protocol
   ratio; pre-registering a scored `STRADDLE-CLOSED` verdict would
   presume exactly the machine-independence M6 exists to test.
2. **OV-2 — PHOTONICS' eighth-deferral branch: DECLINED.** The MF-1..MF-4
   changes are being adopted, so item 5 ships **corrected**. A corrected
   bound is strictly better than an eighth deferral, and PHOTONICS' own
   framing ("a deferral is a debt; a false bound is a liability")
   supports shipping it.
3. **OV-3 — THERMODYNAMICS' discard-first-1000-steps protocol: DECLINED
   ENTIRELY**, and no extra reading is taken in its place. The 18-call
   budget stands. It would change the recipe away from
   `chunk_runner114::_time_control_blend`, breaking matched-protocol
   comparability with every prior R31 reading and with the bench-native
   R31 artifact this cycle also exists to produce; MF-7(a)'s two-point
   bound carries the same information out of readings already scheduled.
4. **OV-4 — EM's `σ_ext_cross` third channel: DECLINED.** Refuted by EM's
   own A7: `Δσ_ext_cross ≡ Δσ_ext` bit-identically, and the "2 ppm
   agreement" is nothing but the difference between two normalization
   denominators. MF-11's wording fix is adopted instead.
5. **OV-5 — QUANTUM's `τ_true ∈ (6.6071, 8.2588)` interval: DECLINED.**
   Refuted numerically; the two family members are the same optical
   article by construction. PHOTONICS' exact identity is adopted (MF-1),
   and this cycle recomputes `τ_true = 8.258813` at **both** members.
6. **OV-6 — QUANTUM's 8.93% re-anchor magnitude: DECLINED; the sign
   finding ADOPTED.** The 8.93% inherits the refuted ~14% `peccored`
   premium; corrected it is 4.47–4.91%, **smaller** than `R_DEG = 7.60%`,
   so M3's bar is not undersized. The sign conflict is real and is
   carried by MF-9's mechanism-neutral labels.

### Adopted, recommended-not-mandatory, disclosed

Red Team's **`SUSTAINED_CONTROL_STEPS` step-down branch** (THERMO §12) is
**adopted** in `control_budget_gate()`, so degradation is graceful at
both ends: a budget breach spends the **repeat** first
(`repeat_skipped=True` with its reason persisted); only if the **primary**
sustained pass would itself breach does `SUSTAINED_CONTROL_STEPS` step
down to the largest value that fits (`sustained_steps_used` and
`sustained_stepped_down` persisted); only if no value at or above
`SHORT_CONTROL_STEPS` fits does the gate raise. R19's call-count assert
is conditional on the branch actually taken.

### Program-level Checkpoint criterion 4 (Red Team §4.2) — discharge

Red Team fired criterion 4 at **program level, not on this proposal**,
ruled a **notification, not a pause**, on the ground that PANEL.md's
Metrics section no longer described the program it governs (exp-101 →
exp-114 is fourteen consecutive cycles with no constraint-3 number).

- **D1 — PANEL.md Metrics amendment**: written separately by the
  Director this shift (PANEL.md's own "Scope amendment (Director,
  Iteration 92)"). Not edited from this document.
- **D2 — the Director's ruling of record on Tier-3 item 10.**
  **Iteration 93 executes Tier-3 item 10 — VISION SCIENCE's re-score of
  the program's only-ever Tier-W/Tier-A constraint-3 citation through the
  modernized ambient instrument — as its Tier-1 item 1, regardless of
  lead-seat rotation.** ELECTROMAGNETISM leads Iteration 93 by rotation
  and that is unchanged; VISION SCIENCE pins the numeric pass/fail
  thresholds per its charter duty, cited, before the run. This is the
  same explicit-Director-decision standard that was applied to Tier-1
  item 5 (MATERIALS' fabrication debt) and never yet to item 10, which
  is the asymmetry Red Team named. Under R34 the firing self-closes once
  Iteration 93's Red Team final audit confirms D1 and D2 discharged from
  primitives.

### The exclusive-use protocol (MF-6e), stated so it can be enforced

For the duration of `chunk_runner115.py --run-cg` on the T5820: **no**
concurrent trust-suite run, **no** second SSH session doing work, **no**
`analyze115.py`, **no** editor indexing the repo, nothing else on the
box. The entire product of this cycle is wall time; an uncontrolled
concurrent process invalidates every reading, and this bench is shared.
`--post-ticker` posts a one-line, values-only update (no IPs, no host
addresses) to the co-lab ticker after each reading precisely so following
the run does not require breaking exclusive use.

### One disclosed forward correction (R4), against the docket itself

MF-13 states its closing bound as "`~10⁻⁸` relative, **five orders below
the smallest measured delta**." Recomputed in `sidecar_m9()`: the
magnitude reproduces (`12/98,740 × exp(−τ_true) ≈ 3.15×10⁻⁸`), but it is
**~2.3 orders** below the smallest of the six measured aggregate deltas
(`5.67×10⁻⁶`) and **~3.5 orders** below the largest (`1.09×10⁻⁴`), not
five. The qualitative conclusion — the exact-radius overlap cells are
**ruled out** as an explanation, not merely unaddressed — is unchanged.
Both the reproduced magnitude and the corrected comparison are persisted;
the docket's phrasing is not propagated forward.

### One residual limitation, disclosed as a TODO rather than fixed

**TODO (a `lab/caveat_lint.py` code change, out of this cycle's
authorization):** `check_caveat()` uses `trigger_terms` for
*discovery only* — candidate-site findings print as `WARN` and **never**
affect the exit code (`lab/caveat_lint.py`, `run_registry`, which sums
only `site_results` failures). So MF-14's spelling/Unicode widening makes
the T18 entry able to **see** documents it was blind to, but seeing them
still cannot fail CI. The gating half of MF-14 is discharged the other
way — by adding this cycle's own documents to `required_sites` on both
entries — and that is what actually gates. The general fix (an
opt-in `gate_on_candidates: true` flag per entry, or promoting a
trigger-hit-without-phrase to a failure) is a change to
`lab/caveat_lint.py` itself, which this Phase-3 shift was explicitly not
authorized to make. `lab/ARTIFACTS.md`'s own invariant applies verbatim
and is the reason this is written down rather than left implicit: *a
silent gate and an absent gate produce identical observations.*

**Also disclosed:** MF-14 asks for a T18 disclosure "at §2.0's own
`τ_true` row where the exp-061 verdict is restated." `phase1_proposal.md`
is a frozen Phase-1 document (house convention: errata flagged, not
rewritten), so the disclosure lands at every **Phase-3** site that
restates that verdict — this document's Idealizations, `DISCLAIMER_115`,
and `sidecar_m9()["e_tier"]["evidentiary_tier"]` — and all three are now
`required_sites` on the T18 registry entry.

---

## Hypothesis

`G ≡ per-step(r=234)/per-step(r=156)`, measured same-session,
same-machine, at matched step counts and matched scene mix, reproduces
the value exp-114's `KAPPA_COST_EXPONENT` predicts at `kappa_ratio = 1.5`
(`G_ref = 2.4453404739580256`) to within R28's own founding-miss
magnitude — **and** the two competing protocol models on file
(`G ≈ 2.5403` vs `G ≈ 2.8681–2.8802`) can be separated by the readings
this cycle takes, or, if they cannot, the cycle says so in code rather
than returning a point verdict it has no power to support.

Falsifiable both ways: `G_sustained > 2.8121415` moves exp-114's filed
CONFIRM to AMBIGUOUS; `G_sustained ≥ 3.1789426` or `≤ 1.7117383` makes it
a REFUTE and forces exp-114's CONFIRM-WITH-NAMED-GAPS to be re-framed in
LOGBOOK by forward disclosure. `G_E = 2.74550565` sits inside the CONFIRM
window at 82% of the way to its upper edge, so the upward edge is only
2.427% away — reachable from a ~40–100 minute measurement.

Secondary, sidecar, no blind prediction: the `graded_black_shell`
article's optical signature is insensitive to the core/backing material
at a level the instrument can now state **with its resolution certified**,
rather than asserted.

## Setup

**Bench.** Dell T5820, Xeon W-2145 (8c/16t), 128 GB — WSL2 Ubuntu 24.04
sees 14 threads / 94 GiB — python 3.11 venv at
`~/projects/photon-lab/.venv311`, numpy from `requirements.txt`. This is
**not** the GitHub CI runner and **not** the cloud sandbox exp-114's
timing data was taken on; the bench has **no measured per-step FDTD rate
for either grid**, which is precisely why this cycle exists and why the
budget gate re-projects from measured readings rather than trusting any
prior. Trust suite measured on this bench today: **41/41 in 87 s** —
**uncommitted as of Phase 3**; MF-12 requires the re-run record be
committed in Phase 4, because `lab/validation/VALIDATION.md`'s own
docket-14 rule says a reproducibility claim that does not name its
platform is not a gate.

**Article, unchanged, reused not re-specified.**
`materials.graded_black_shell(sim, CX, CY, R_CORE, R_COAT,
sigma_max=0.4)` — a graded conductive sponge, `eps_r ≡ 1.0` throughout
(no index step, hence no interface to glint off), giving
`tau_shell = 24.0` at both radii. `peccored` adds
`materials.pec_disk(sim, CX, CY, R_CORE)` inside that shell; `hollow`
leaves the core vacuum. Source
`add_line_source(SRC_X, angle_deg=0.0, profile="plane", edge=50)`,
λ = 600 nm, `cells_per_lambda = 25` (dx = 24 nm),
`courant_frac = R110.COURANT_FRAC`.

| Quantity | r=156, cpl=25 | r=234, cpl=25 |
|---|---|---|
| `N` (cells, square) | 1400 | 2100 |
| `CX`, `CY` | 630, 700 | 945, 1050 |
| `SRC_X` | 160 | 240 |
| `R_CORE` / `R_COAT` | 135 / 195 | 232 / 292 |
| `tau_shell` (invariant, asserted) | 24.0 | 24.0 |
| `absorb` / `edge` | 50 / 50 | 50 / 50 |
| `kappa_of(r)` | 2.0 | 3.0 |
| cell-count ratio to r=156 | 1.00 | 2.25 |

**Block CG — six readings, 18 `Sim.run()` calls, 46,008 grid-steps**
(23,004 per grid), each reading a cold-built 3-scene blend
(`empty`, `hollow`, `peccored`), one `sim.run(steps)` per scene, timing
bracketing `sim.run()` only:

| # | Reading | grid | steps/scene | purpose |
|---|---|---|---|---|
| 1 | `S156` | r=156 | 1000 | short baseline |
| 2 | `S234` | r=234 | 1000 | **first r=234-grid control in program history** |
| 3 | `U156` | r=156 | 3334 | sustained (A) |
| 4 | `U234` | r=234 | 3334 | sustained (B) |
| 5 | `U234b` | r=234 | 3334 | sustained repeat (B) — **ABBA** |
| 6 | `U156b` | r=156 | 3334 | sustained repeat (A) — **ABBA** |

Nothing else runs: no production leg, no `full_capture`, no
`window_stats`, no angular-pattern instrument, no named-bin
classification, no checkpoint/resume. Data lands in
`experiments/115-.../data/readings.json` (`lab/ARTIFACTS.md` reserves
`artifacts/` for scene bundles) and verdicts in `results.json`.

**Exact Phase-4 commands, in order** (from the repo root, on the bench,
under the exclusive-use protocol; `PY=~/projects/photon-lab/.venv311/bin/python`):

```
# 1. geometry identity, zero FDTD
$PY experiments/115-t28-r234-grid-native-control-and-fab-tolerance/run115.py --verify-geometry

# 2. MF-12 absolute identity gate on the new machinery, zero FDTD
$PY experiments/115-t28-r234-grid-native-control-and-fab-tolerance/chunk_runner115.py --identity-gate

# 3. trust suite ON THE BENCH -- commit the console record (MF-12 / VALIDATION.md docket-14)
$PY lab/validation/run_all.py --only 12346789

# 4. machine-state block (MF-6e), zero FDTD
$PY experiments/115-t28-r234-grid-native-control-and-fab-tolerance/chunk_runner115.py --machine-state

# 5. Block CG -- EXCLUSIVE USE OF THE BENCH REQUIRED for the duration
$PY experiments/115-t28-r234-grid-native-control-and-fab-tolerance/chunk_runner115.py --run-cg --post-ticker

# 6. analysis -- run only AFTER the readings are complete (it is itself a concurrent process)
$PY experiments/115-t28-r234-grid-native-control-and-fab-tolerance/analyze115.py
```

Steps 1, 2 and 4 are zero-FDTD and were executed at Phase 3 on the
Director's workstation as a syntax/logic check; step 3's record and steps
5–6 are the bench's. `run115.py --selftest` (also zero-FDTD) is the
committed, re-invocable call site for the **result-side**
`DISCLAIMER_115` assert and for the MF-5 reproduction check.

## Idealizations — carried from `phase1_proposal.md` §7, amended at Phase 3

1. **Does establish (if it runs clean):** the first per-step cost
   measurement ever taken on any grid but r=156 in this program; a
   matched-protocol, same-session, single-machine measurement of `G` free
   of every cross-session normalization exp-114's verdict depended on; a
   second-machine replication (or refutation) of that verdict; a
   bench-native R31 control every future bench cycle can cite; and one
   written fabrication-tolerance bound with a stated realizability tier
   and a stated resolution.
2. **Does NOT establish** anything about `kappa_ratio` other than `1.5`.
   `k`'s portability to `kappa_ratio = 2.0` still rests on the single
   founding pair, and to ratios above `2.0` on nothing at all. A CONFIRM
   here does not license extrapolation past `2.0` — **and (MF-7b) does
   not distinguish `k = 3.2053` from `k = 3.0`**, since pure `N²` scaling
   gives `rel_dev = 0.0799`, inside the CONFIRM band.
3. **`G` is a machine property, not a physics constant.** Everything M2
   measures characterizes an FDTD implementation on a memory hierarchy.
   M6 is the only metric that tests portability across machines, and it
   does so with `N = 2` machines — the minimum that can detect a
   difference, not enough to characterize a distribution. QUANTUM's B8
   decomposition is accepted: with two machines and one protocol each,
   M6 cannot separate a machine factor from a protocol factor.
4. **`G_E`'s protocol mismatch is bounded, not eliminated — and the
   Phase-1 bound was wrong (MF-11).** exp-114's r=234 numerator was
   checkpoint-chunked at 1000 steps/scene; this cycle's readings are
   single-call. The three surviving chunk times give `max/min =
   214.2101/196.8292 = 1.0883`, an **8.83%** spread, **not** the "≲5%"
   the proposal stated — and chunk scatter is the **wrong statistic** for
   the mismatch it claims to bound: the real level shift inside that same
   run is **4.467%** between the first 3000 and the full 12000 steps,
   which chunk scatter cannot see. Those three figures survive only as
   quotations inside `experiments/114-.../phase5_redteam_audit.md` §2;
   the scratch wall-time log did not survive that session, so everything
   derived from them (including MF-7(c)'s two pre-registered protocol
   models and the v2 factor `p_prod/p_burst = 0.9532431`) is **cited, not
   independently re-derivable**, and is labelled directional. `p_prod/
   p_burst` is re-derived in code from the blend average and those three
   quoted times and reproduces the filed `0.9532431491914767` to
   `1.9×10⁻⁸`, not to `1e-9`, because they are quoted to 4 decimal
   places — disclosed rather than asserted.
5. **Pickle I/O is excluded from both sides by construction**, verified
   by direct read: `chunk_runner114.py::step_budgeted` records
   `dt = time.time() − t0` around `sim.run(chunk)` only, with the
   `pickle.dump` after it and resume `pickle.load` before `t0`. This
   cycle's readings do no pickling at all.
6. **The `HISTORICAL_R156_CPL25_TOTAL_S` per-scene split remains a bare
   3-scene-blend scalar** (exp-112's `analyze.py` merge clobbered the
   per-scene dict; carried unchanged since exp-113). This cycle's own
   readings are blends by design and additionally persist per-scene wall
   times, so this cycle at last leaves a recoverable split behind — but
   exp-112's is still not recoverable, and no future per-scene claim may
   use it.
7. **The sidecar's per-bin evidence is r=156/312 only, at cpl=20 only;
   its aggregate evidence is r=156/234 only, at cpl=25 only — so
   channel and resolution are fully confounded** (MF-4, an idealization
   the Phase-1 document did not disclose). exp-114's r=234 captures were
   never persisted, so r=234 contributes aggregate channels only. The
   bound is stated over the channels each radius actually supplies, never
   averaged across them as if all three radii carried all channels.
8. **The sidecar's optical-depth argument is a 1-D centre-line
   Beer–Lambert argument on a graded annulus, in its CORRECTED functional
   form (MF-1).** The core-dependent contribution to a **cross-section**
   is the coherent cross term, scale `exp(−τ_true) = 2.5896×10⁻⁴`, upper
   bound `2·exp(−τ_true) = 5.1793×10⁻⁴` — **not** `exp(−2·τ_true)`, which
   is the `|δA|²` (returned-power) term only and is wrong by
   `exp(+τ_true) ≈ 3.86×10³` for this purpose. It ignores diffraction
   into the geometric shadow, near-tangent chords (longer through the
   annulus, so conservative in the safe direction), and the `eps_r ≡ 1`
   idealization. It is an order-of-magnitude consistency check, never a
   replacement for the measurement — and, corrected, it is the **same
   order** as the measured aggregate deltas rather than orders below
   them, which is what makes it a check at all.
9. **`τ_true` is the SAME at both family members, by construction, not by
   assumption (MF-1 / OV-5).** exp-061 derived it at cpl=20 /
   `sigma_max=0.5` / 48 cells; the r=234 data is cpl=25 /
   `sigma_max=0.4` / 60 cells — and `σ_max·cpl = 0.5×20 = 0.4×25 = 10`
   (identical loss tangent) with `thickness/cpl = 48/20 = 60/25 = 2.40 λ`
   at both, so `I_graded` and `τ_true` are **bit-identical**. Recomputed
   this cycle from `lab/materials._graded_black`: `τ_true = 8.258813` at
   both, reproducing exp-061's filed `8.258819829686677` to `8.1×10⁻⁷`
   relative. The Phase-1 concavity hedge is withdrawn, and QUANTUM's
   `(6.6071, 8.2588)` interval is declined as refuted. The λ dependence
   is real but narrow: `2·exp(−τ)` = `3.58/5.18/7.35 ×10⁻⁴` at
   450/600/750 nm — backing freedom is **weakest in the red**, and has
   been measured only at 600 nm.
10. **T18 still binds.** No primary-source literature access is attempted
    or claimed. The `UNOBTANIUM-WITH-PARAMETERS` realizability tier in
    M9(e) is inherited from exp-061's Phase-4 record, which is
    **WebSearch-snippet synthesis, not primary-source-verified** —
    T18's WebFetch block stood at 41+ consecutive attempts as of that
    cycle. The tier is cited, not re-derived, and this disclosure travels
    inside the quotable bound itself (MF-4), not only in this section.
    `exp052-alpha-60nm-absorptivity-open` still bites on "thickness as
    the binding constraint": the 60 nm absorptivity question is open.
11. **Both the bench and the two cloud sessions are multi-tenant to an
    unknown degree.** Contention is the dominant known noise source on
    every wall-time figure in this program. This cycle's instruments for
    it are the exclusive-use protocol, the persisted machine-state and
    `loadavg` blocks, and M4 — which under ABBA samples **drift + noise**,
    not repeatability, exactly twice (MF-6d).

---

## Predictions (committed before any run)

Verbatim output of
`python experiments/115-t28-r234-grid-native-control-and-fab-tolerance/run115.py --predictions-only`,
executed at Phase 3 before any Phase-4 `Sim.run()` call. House
discipline, non-negotiable.

```
PREDICTIONS (pre-registered, exp-115, Panel Iteration 92)
Runner: bench panel shift (T5820) -- Director Clyde, live session.

This is an instrument-fidelity / governance cycle on the T28 sub-thread -- not a phenomenon-mechanism proposal and not a named-bin resolution-convergence classification. T1 escape route: NONE / N/A. No sigma(I)/sigma(x,t)/angular-selectivity/sub-threshold content, no Weber-contrast or C_thr(L) perceptual scoring, is performed anywhere in this document; none of PANEL.md's seven metric rows is recorded (see PANEL.md's Iteration-92 scope amendment). ANALYTIC SIDECAR, NOT FDTD: M9's fabrication-tolerance bound is desk arithmetic over already-committed results.json files plus one desk integral over lab/materials._graded_black -- it consumes zero FDTD calls, zero grid-steps and zero bench wall time on the timed path, and it is NOT an output of this cycle's own six timing readings. It carries a code-enforced arithmetic reproduction gate; any mismatch HALTs it and it is reported NOT-REPRODUCED rather than published. UPPER BOUND VS RESOLVED: the sidecar's per-bin channel figures are floor-GATED and resolved on exp-110's own local-normalization instrument; the aggregate channels are resolved at 4.47x/11.70x on exp-108's six-margin differential family, which is the ONLY differential floor this program has -- no differential floor exists at r=234, and the |sigma_ext - sigma_ext_cross| quantity the Phase-1 proposal used as a floor is WITHDRAWN (it is scene-independent and cancels exactly between the two scenes being differenced). The bound is certified at margin=32 only, with channel and resolution fully confounded. CONSTRAINT 3: the graded_black_shell article this bound describes FAILS CONSTRAINT 3 BY CONSTRUCTION -- a perfect absorber is a black shape in daylight (LOGBOOK ESTABLISHED) -- and nothing in this cycle is constraint-3 progress or a T1 escape route. EVIDENTIARY TIER (T18): every literature figure behind the UNOBTANIUM-WITH-PARAMETERS realizability tier is inherited from exp-061's WebSearch-snippet synthesis, NOT primary-source-verified; this cycle attempts no new literature search. ENERGY-LEDGER / THERMAL-SIDECAR: N/A THIS CYCLE, and the reason is physical, not clerical. geom_fixedabs_cpl sizes STEPS so each grid gets ~2 domain crossings at S = courant_frac/sqrt(2) = 0.2263 cells/step; the control bursts run 1000 and 3334 steps, so the wavefront reaches only ~65 percent of the r=156 domain and ~47 percent of the r=234 domain. A sigma_abs/sigma_ext ledger from fields that far from settled would be a WRONG NUMBER, not a free byproduct (T27 is this program's own paid-for lesson that a truncated run is not a small perturbation of a settled one) -- so PANEL.md's 'Absorbed energy budget + predicted re-radiation' row, which exp-114 filled, is declared N/A here rather than silently dropped. SCORING SCOPE: G is a MACHINE PROPERTY, not a physics constant. M5 replicates exp-114's own scored statistic and can move a filed verdict; M6 tests machine transfer with N = 2 machines; M7 is descriptive. Pure cell-count (N^2) scaling is algebraically identical to the pre-R28 hardcoded exponent 3.0 and lands INSIDE the CONFIRM band at rel_dev = 0.0799, so a CONFIRM does NOT distinguish k = 3.2053 from k = 3.0. Two defensible protocol models put G on OPPOSITE sides of the CONFIRM ceiling; whenever MF-7(a)'s protocol-mismatch interval spans a band edge, M5 is reported BOUNDED-REPLICATION and may not move exp-114's LOGBOOK entry. The claim that this cycle 'resolves the v2 straddle' is WITHDRAWN: v2's construction contains no r=156 quantity and its second operand, an intra-r=234 production-vs-burst factor, is not measured here. R30/R32: N/A -- this cycle produces no discriminating statistic of that class. R31/R33: M5 is R33-immune BY CONSTRUCTION (no scored operand mixes sessions); M6 is explicitly a cross-machine comparison and is labelled one.

**Geometry identity (zero-FDTD, pre-Phase-4)**: verify_geometry_identity()
returns pass_=True at r=156, r=234 AND r=312 -- geom_fixedabs_cpl(r, cpl=20)
must reduce to R110.geom_fixedabs(r) exactly at all three. Falsified by any
mismatch -- HALT before any Sim.run() call.

**MF-12 absolute identity gate on the new machinery (zero-FDTD, pre-reading)**:
chunk_runner115.py's parameterized _time_control_blend(r, ...) at r=156 must
construct a scene set IDENTICAL to chunk_runner114.py's own hardcoded
_time_control_blend() -- same geometry dict field-for-field, same three scenes
in the same order, same SHORT/SUSTAINED step constants, and a build_sim source
segment byte-identical to chunk_runner114.py's. Falsified by any difference --
HALT before any reading is trusted. The trust suite is re-run ON THE BENCH and
its console record committed (VALIDATION.md docket-14: a reproducibility claim
that does not name its platform is not a gate).

**Block CG -- six readings, 18 Sim.run() calls, 46008 grid-steps**
(23004 per grid), in the order S156, S234, U156, U234, U234b, U156b. The
sustained pass is ABBA (MF-6a), not ABAB: under ABAB both sustained pairs
inherit the same-signed (a+b)/2 lag while d_rep reads ~0 -- an alarm
structurally incapable of producing the reading that means "bad".
G_sustained is the MEAN of the two pairwise G values, both persisted.
Same-grid drift is reported as a RATE PER UNIT ELAPSED TIME, because ABBA
makes the two same-grid lags unequal (a+2b vs b). Exclusive use of the bench
is enforced for the duration of the readings; a machine-state block is
persisted with each reading.

**M1 `G_short` / M2 `G_sustained`** -- descriptive; M2 is the operand M5/M6/M7
score. No advance position is taken on which band any metric lands in.

**M3 -- is `G` duration-invariant? (MECHANISM-NEUTRAL labels, MF-9)**
| Outcome | Condition |
|---|---|
| G-DURATION-INVARIANT | d_dur <= R_DEG/2 = 0.0379821 |
| PARTIAL | between |
| G-NOT-DURATION-INVARIANT | d_dur >= R_DEG = 0.0759642 |
Anchor (R17): R_DEG = 0.0759642 is exp-114's own measured single-grid
(r=156) 1000->3334 steps/scene shift, the largest comparable on file. The
labels name no mechanism because the mechanism is unvalidated AND
contradicted in sign on file: R_DEG is +7.596% (longer = slower) while
exp-114's own intra-r=234 first-3000-vs-full reading is -4.467% (longer =
faster), and run_control() runs short-then-sustained with no counterbalance,
so R_DEG conflates duration with elapsed session position by construction.

**M4 -- drift+noise (MF-6d: under ABBA this is NOT a repeatability statistic)**
| Outcome | Condition | Consequence carried in the label |
|---|---|---|
| REPEATABLE | d_rep <= 0.02 | M3 scored, M7 powered |
| MARGINAL-M3-SCORED-M7-POWERED | <= 0.03 | |
| MARGINAL-M3-SCORED-M7-UNDERPOWERED | <= 0.0379821 | |
| MARGINAL-M3-UNSCORED-M7-UNDERPOWERED | < 0.0759642 | |
| NOISY-M3-UNSCORED-M7-UNDERPOWERED | >= 0.0759642 | |
Coded booleans, all persisted (MF-9): m3_scored = (not repeat_skipped) and
(d_rep <= R_DEG/2); m5_protocol_caveat; m6_directional_only = (m3_verdict !=
"G-DURATION-INVARIANT"); m7_underpowered. If the budget gate skips the repeat
pass, repeat_skipped=True is persisted with its reason, M4 reports UNMEASURED,
m3_scored is False, and the R19 call-count assert expects
12 calls instead of 18.

**M5 -- PRIMARY: bench replication of exp-114's own scored statistic**
Scored by exponent_B = ln(1.5*G_sustained)/ln(1.5) fed to R114's own
committed classify_kappa_exponent_check(), UNMODIFIED, with a code-assert
that |measured_ratio - 1.5*G_sustained| < 1e-12 (MF-5 -- passing
measured_ratio directly, as the Phase-1 document's own text says, evaluates
1.5**(1.5*G) and returns rel_dev = 0.4480 -> a false REFUTE on exp-114's own
filed value).
| Outcome | Condition | Exact boundary in G |
|---|---|---|
| CONFIRM | rel_dev <= 0.15 | G in [2.0785394, 2.8121415] |
| AMBIGUOUS | between | |
| REFUTE | rel_dev >= 0.30 | G <= 1.7117383 or G >= 3.1789426 |

**M5's stated power limit, pre-registered (MF-7)**. (b) Pure N^2 (cell-count)
scaling gives G = 2.25 exactly, i.e. k = 3.0 EXACTLY -- the pre-R28
hardcoded exponent -- and rel_dev = 0.0799, INSIDE the CONFIRM band. A
CONFIRM therefore does NOT distinguish k = 3.2053 from k = 3.0;
the entire hypothesis space between the two competing exponents is ~8% wide and
the CONFIRM band is 15% wide. (c) Two defensible protocol models, both on file,
predict G on OPPOSITE sides of the CONFIRM ceiling (2.8121415):
  - drift/degradation model (R_DEG extrapolated log-linearly from 1000->3334 to
    3334->12000, factor 0.08079): G ~ 2.5403 -- comfortable CONFIRM
  - warm-up-amortization model (exp-114's own r=234 first-3000-steps rate against
    its own 12000-step average): G ~ 2.8681 (scene-matched) to 2.8802
    (blend-denominator) -- ABOVE the ceiling, i.e. AMBIGUOUS
  The span is ~13%, comparable to M5's entire CONFIRM half-width. These two
  models' inputs include exp-114's three r=234 chunk times, which survive only
  as quotations and are NOT independently re-derivable -- directional, cited.
(a) A protocol-mismatch INTERVAL is persisted from the two-point
p(n) = p_inf + C_g/n relation on each grid (S and U are the two points, so it
is exactly determined -- it BOUNDS, it does not fit, R7). If the interval
spans a band boundary, m5_protocol_caveat=True is persisted and M5 is reported
BOUNDED-REPLICATION (protocol-mismatch interval spans a band edge) -- NOT a verdict that can move exp-114's LOGBOOK entry.

**M6 -- cross-machine transfer of G**: T = G_sustained/G_E, G_E = 2.74550565.
TRANSFERS if |T-1| <= 0.1529500 (R28's own founding-miss
magnitude, reused in the same ratio space); DOES-NOT-TRANSFER if
|T-1| >= 0.3059001. m6_directional_only is True unless M3 reads
G-DURATION-INVARIANT -- MF-9 INVERTS the Phase-1 rule so PARTIAL, UNSCORED and
repeat-skipped all INHERIT the caveat instead of escaping it. This cycle does
NOT claim to resolve the v2 straddle (MF-8): v2's construction contains no
r=156 quantity, and over 66.4% of M5's own CONFIRM band the cycle
would return "CONFIRM, replicated" with the straddle still open (sign boundary
at G >= 2.5652851).

**M7 -- the N^2 assumption, TWO-SIDED labels (MF-9/RT-14)**: excess =
G_sustained/2.25 - 1. N2_HOLDS if |excess| <= 0.05;
N2_FAILS-SUPERLINEAR if excess >= 0.152950040; N2_FAILS-SUBLINEAR if
excess <= -0.152950040 (sub-cell-count scaling is the OPPOSITE finding
and must not inherit the positive branch's meaning). Note, computed before any
bench data: N2_HOLDS requires BOTH candidate cost models to be wrong -- the
in-force constant-k model predicts excess = 0.08682 (AMBIGUOUS) and the
constant-eps model predicts excess = 0.152950039837078, bit-adjacent to the
N2_FAILS bar. The two models differ by only 6.085%, so the comparison is
reported UNDERPOWERED and NOT scored whenever d_rep > 0.03. VISION's identity
is carried forward: eps_E/eps_k == G_E/G_ref == measured_ratio/reference_ratio,
so M5 and M7's secondary comparison are ONE datum wearing two hats.

**M8 -- persisted, NOT-scored sensitivities (Tier-1 item 2)**:
sensitivity_short_reading_DO_NOT_SCORE: measured_ratio = 4.4310989, rel_dev = 0.20803870 (AMBIGUOUS). sensitivity_v2_straddle_DO_NOT_SCORE: measured_ratio = 3.2171956, SIGNED deviation -0.12290 against the filed +0.12275 -- opposite sides of reference_ratio, a 28.0% spread between central estimates. A third,
sensitivity_v2_with_measured_G_DO_NOT_SCORE, is added once G is measured
(OV-1: the SCORED half of QUANTUM's M10 is DECLINED -- scoring it would
presume the machine-independence M6 exists to test).

**M9 -- fabrication-tolerance bound (ANALYTIC SIDECAR, no blind prediction)**.
Its falsifiable element is a code-enforced arithmetic reproduction gate: every
cited figure is recomputed in analyze115.py from its source results.json and
asserted equal to <1e-12 relative, and tau_true is recomputed from
lab/materials._graded_black at BOTH family members and must reproduce
8.258819829686677 to <1%. Any mismatch HALTs the
sidecar, which is then reported NOT-REPRODUCED rather than published. The
sidecar's PHYSICS is stated in its corrected functional form BEFORE the run
(MF-1): the core-dependent contribution to a cross-section is the COHERENT
CROSS TERM, scale exp(-tau_true), upper bound 2*exp(-tau_true) -- NOT
exp(-2*tau_true), which is the |dA|^2 term only and is wrong by exp(+tau_true)
~ 3.86e3.

**Budget gate (R27/R28, executable, upstream of every Sim.run)**: reuses
R110.COST_GATE_TOTAL_S = 10800 and COST_GATE_SAFETY_MARGIN =
1.1 unmodified, re-projecting after S156 (G_prior = G_E),
after S234 (measured G_short), and after U234 (the repeat pass). Graceful
degradation at BOTH ends (Red Team's recommended-not-mandatory branch,
ADOPTED and disclosed): a breach spends the REPEAT first (repeat_skipped=True
with its reason persisted); if even the primary sustained pass would breach,
SUSTAINED_CONTROL_STEPS steps DOWN to the largest value that fits and
sustained_steps_used is persisted with a flag. Only if no value at or above
1000 steps/scene fits does the gate raise.

**Declined this cycle, numbered (R25)**: phase1_proposal.md Sec 3 items 1-7,
plus --
8. Tier-1 item 1's OWN SECOND HALF -- 're-score kappa_exponent_result against the corrected denominator' -- is DECLINED as un-executable, not silently absorbed (R25). It has two halves and neither is available: (i) the cross-session half DISSOLVES under the Sec-1 identity (measured_ratio == kappa_ratio * G; every cross-session term cancels identically, so there is no cross-session denominator left to correct); (ii) the burst-vs-production half is not measurable without an r=234 PRODUCTION leg, which this cycle does not run and which would cost three 12000-step scenes. What this cycle CAN do for it -- MF-7(a)'s two-point protocol-mismatch interval -- it does.
```

---

## Phase 4 — Results

(pending)

## Phase 5

(pending)
