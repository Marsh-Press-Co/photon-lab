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
12. **Block CG was run TWICE, and the outage is part of the record**
    (added at Phase 5 per R25 / R33 addendum (a) and PLAN.md's own resume
    instruction). Session 1 (2026-09-05T23:54:14Z -> 2026-09-06T00:31:28Z,
    four readings, 12 `Sim.run()` calls, 2228.700 s) was **interrupted**:
    `U234b` was in flight when the Windows host stopped answering SSH at
    ~00:53Z and went fully dark by ~01:15Z; the bench was power-cycled by
    hand at ~04:30Z. Session 2 (2026-09-06T04:39:25Z -> 05:41:04Z, six
    readings, 18 calls, 3690.309 s of `Sim.run`) is a **complete
    six-reading re-run from scratch** and is the **sole scored source**.
    Two facts about session 1 are load-bearing and neither is derivable
    from the repository alone: (a) a **Windows-side VC++ runtime
    installation by a desktop user at ~00:03Z**, which overlaps session
    1's `U156` (00:02:42Z -> 00:11:26Z) *exactly* and precedes the
    monotone 4.78 -> 8.33% per-step slowdown; and (b)
    `data/cg_session1_interrupted.log` contains **two lines** - the ticker
    output did not survive, the same shape as exp-114's lost scratch
    wall-time log one cycle earlier. Session 1's four readings are
    committed and are scored **nowhere**
    (`sensitivity_session1_across_reboot_DO_NOT_SCORE`, Phase 4 below).
13. **`loadavg` is WSL2-scoped and structurally blind to the Windows
    host** (THERMODYNAMICS D5, PHOTONICS F9(c); added at Phase 5).
    MF-6(e)'s machine-state block samples the Linux VM's run queue
    (`machine_state.platform = Linux-...-microsoft-standard-WSL2`), so a
    Windows-side process contributing to the DRAM bandwidth this
    measurement *is* never appears in it. Session 1's per-reading
    `loadavg_before` first components are `0.165 / 1.042 / 1.042 / 0.930`
    and session 2's are `0.044 / 1.005 / 1.039 / 1.237 / 1.005 / 1.009` -
    statistically indistinguishable - while session 1 ran **4.2-8.3%
    slower on every reading**. The instrument returned the same reading
    for the clean run and for the run that ended in a host hang: *a
    watcher that can only say "quiet" is not evidence it can hear.* **The
    exclusive-use protocol's real evidence in session 2 is therefore the
    readings' own mutual consistency** - `d_rep = 1.46%`, contiguous
    0.87-1.28 s gaps between the six readings, `loadavg` pinned at ~1.0
    (exactly one runnable process) for 61.7 min, and a per-scene replicate
    floor of 0.115% at r=234 - **not `loadavg` itself.** Arming a positive
    control for it is Iteration-93 Tier-2 item 7.

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

**Runner: bench panel shift (T5820) — Director Clyde, live session.**

Every figure in this section was re-derived from `data/readings.json`,
`data/readings_session1_interrupted_20260905T2354Z.json` and
`results.json` this shift and independently at six Phase-5 seats and at
Red Team's final audit. Where a figure corrects something already frozen
in `results.json`, `run115.py`, `DISCLAIMER_115` or `result_text`, the
correction is stated here in prose — the Phase-4 artifacts are **not**
edited (house convention: errata are disclosed forward, never
back-written).

### 4.0 Block CG was run TWICE — the outage, the third resume branch, and what is scored

**Session 1 (NOT scored).** Block CG started 2026-09-05T23:54:14Z under
the exclusive-use protocol after an all-green pre-flight (geometry
identity r=156/234/312; MF-12 identity gate 10/10; trust suite **41/41 in
87 s** with the platform-named console record committed at
`data/trust_suite_bench_20260905T235042Z.txt`; machine-state block
persisted). Four readings completed — `S156`, `S234`, `U156`, `U234`, 12
`Sim.run()` calls, 2228.700 s — and `U234b` was in flight when the
Windows host stopped answering SSH at ~00:53Z (TCP 22 accepted, no
banner; Tailscale still ponged) and by ~01:15Z went fully dark. **A
Windows-side VC++ runtime was installed by a desktop user at ~00:03Z**,
overlapping session 1's `U156` (00:02:42Z → 00:11:26Z) exactly and
preceding the monotone per-step slowdown described in §4.9. The bench was
power-cycled by hand at ~04:30Z. `data/cg_session1_interrupted.log`
survives with **two lines** — the ticker output did not survive, the same
shape as exp-114's lost scratch wall-time log one cycle earlier. Both
facts are in Idealizations 12–13.

**Session 2 (the sole scored source).** `chunk_runner115.py --run-cg` was
re-run **from scratch**, 2026-09-06T04:39:25Z → 05:41:04Z: the complete
six-reading ABBA block, 18 `Sim.run()` calls, 46,008 grid-steps,
3690.309 s of `Sim.run` inside 3700.506 s elapsed, `repeat_skipped=False`,
`sustained_stepped_down=False`, the R19 call-count assert satisfied at
18/18.

**R25 — the executed resume path is a THIRD branch, not one of the two
pre-registered.** `PLAN.md`'s resume recipe pre-registered exactly two
degradation branches: (i) analyse the four surviving readings with
`repeat_skipped=True` semantics, or (ii) re-run **only** the two repeats
(`U234b`, `U156b`) as a disclosed second session. The executed path — a
full six-reading re-run inside one post-reboot session — is **neither**.
It was the better choice, and the reason is pre-registered physics rather
than hindsight: branch (ii) would have destroyed ABBA's first-order
cancellation by splitting the A and B legs across a reboot, which is
precisely the systematic MF-6(a) exists to remove, and branch (i) would
have surrendered M4 entirely. The re-run also produced the
loaded-vs-clean session pairing that §4.9 turns into this cycle's most
citable positive result. **It is nonetheless a deviation from a
pre-registered degradation path and is therefore disclosed here as a
numbered R25 disclosure, not absorbed as a silent improvement** — it
previously existed only in a commit subject.

### 4.1 The scored readings — session 2, re-derived from per-scene wall times upward

`per_step_s = Σ(per_scene_wall_s) / (3 × control_steps)` reproduces all
six persisted rates bit-exactly.

| # | Reading | grid | steps/scene | per-step (s) | start → end (UTC) |
|---|---|---|---|---|---|
| 1 | `S156` | 156 | 1000 | `0.04858939027786255` | 04:39:25 → 04:41:51 |
| 2 | `S234` | 234 | 1000 | `0.11239203476905822` | 04:41:52 → 04:47:30 |
| 3 | `U156` | 156 | 3334 | `0.04970505291927912` | 04:47:31 → 04:55:48 |
| 4 | `U234` | 234 | 3334 | `0.11082375609762692` | 04:55:50 → 05:14:19 |
| 5 | `U234b` | 234 | 3334 | `0.11105367999581237` | 05:14:20 → 05:32:52 |
| 6 | `U156b` | 156 | 3334 | `0.04908984934084655` | 05:32:53 → 05:41:04 |

```
G_short     = S234/S156   = 2.3130982736423493
G_pair1     = U234/U156   = 2.2296275647790664
G_pair2     = U234b/U156b = 2.2622534289060674
G_sustained = mean(pairs)  = 2.245940496842567     <- the scored operand
```

**`S234` is the first per-step control ever timed on any grid but r=156
in this program's history**, and `G` is the first matched-protocol,
same-session, single-machine measurement of the cross-grid cost ratio the
program has ever had. Both are R33-immune by construction: no scored
operand mixes sessions.

### 4.2 The scored metrics

| Metric | Value | Bar(s) | Verdict |
|---|---|---|---|
| **M1** `G_short` | `2.3130982736423493` | — | descriptive |
| **M2** `G_sustained` | `2.245940496842567` | — | descriptive; the scored operand |
| **M3** `d_dur = \|G_sus−G_short\|/G_short` | `0.02903368938753793` | `R_DEG/2 = 0.037982123779318644` | `G-DURATION-INVARIANT` |
| **M4** `d_rep = \|G2−G1\|/G1` | `0.01463287619976741` | `0.02` | `REPEATABLE (M3 scored, M7 powered)` |
| **M5** `exponent_B = ln(1.5·G)/ln 1.5` | `2.995546218006855` → `measured_ratio 3.3689107452638507` vs `reference_ratio 3.6680107109370383`, `rel_dev 0.0815428277734715` | `≤0.15` | **CONFIRM** |
| **M5 interval** | `[2.217690396029104, 2.2458389149395477]`, rel width `1.269%` | edges `2.0785394 / 2.8121415 / 1.7117383 / 3.1789426` | no edge spanned; `m5_protocol_caveat=False` |
| **M6** `T = G/G_E` | `0.8180425684476521`, `\|T−1\| = 0.1819574315523479` | `0.152950039837078 / 0.305900079674156` | **AMBIGUOUS** |
| **M7** `excess = G/2.25 − 1` | `−0.0018042236255256805`; `k_B = 2.995546218006855` | `\|excess\| ≤ 0.05` | `N2_HOLDS` |
| **M9** sidecar | 11/11 reproduction checks pass | — | `REPRODUCED` (wording corrected, §4.3) |

Composition booleans, all code-persisted (MF-9): `m3_scored = True`,
`m5_protocol_caveat = False`, `m6_directional_only = False`,
`m7_underpowered = False`, `may_move_logbook_verdict = True` — **each
subject to the anchor disclosure of §4.5, which flips three of them under
any bench-native anchor.**

**`exponent_B ≡ k_B` identically, and it matters.** `1 + lnG/ln 1.5` and
`3 + ln(G/2.25)/ln 1.5` are the same function of `G`, because
`ln 2.25 = 2 ln 1.5`. M5's exponent, M7's `k_B` and M7's `excess` are
**one number under three labels**; only M3 (which adds `G_short`), M4
(which adds the pair split) and M6 (which adds `G_E`) contribute
independent information. **This cycle must not be read as five
corroborating measurements.** (PHOTONICS F8, ELECTROMAGNETISM §2.7,
independently.)

**M8 — the folded-in Tier-1 item 2, persisted and NOT scored.** At the
measured `G = 2.245940496842567` the v2 re-normalization gives
`measured_ratio = 3.2113910881603176` (signed deviation
`−0.12448699274928553`), **below** the sign boundary
`G ≥ 2.5652851279677367`: **`straddle_still_open = True` — the v2
straddle remains OPEN**, exactly as MF-8 pre-registered it would over
**66.35%** of M5's own CONFIRM band. The two pre-run sensitivities are
unchanged: short-reading `measured_ratio = 4.431098887676021`,
`rel_dev = 0.20803869914110543` (AMBIGUOUS); v2
`measured_ratio = 3.217195628521234`, signed deviation
`−0.12290451635585277` against exp-114's filed `+0.12274985147707763` —
**opposite sides** of `reference_ratio`, a **28.0%** spread between
central estimates. **None is scored; none may move a LOGBOOK verdict.**

### 4.3 M9 — the fabrication-tolerance bound, as re-issued

The bound below **supersedes** the headline string persisted in
`results.json.sidecar_m9["headline"]` and quoted in `result_text`. The
aggregate half of the shipped bound is exactly right and fully
reproduced; the corrected MF-1 physics is right; what fails is the
scope wording, on five separately-verified counts (§4.7). **The shipped
sentence may NOT be cited forward. This is the citable form:**

> For the `graded_black_shell` article at `τ_shell = 24`, `ε_r ≡ 1`, λ = 600 nm,
> plane-wave normal incidence, 2D TM, measured on this bench's
> **near-to-mid-field box ledger** at its own measurement geometry (not a
> far-field pattern): replacing the entire core/backing from vacuum to a perfect
> electric conductor moves the **aggregate** cross-section channels by at most
> **1.0874×10⁻⁴** relative (`σ_scat` and `σ_abs`, plus their exact algebraic sum
> `σ_ext` — two independent channels, not three), **resolved, not floor-limited**,
> at **4.46×** (r=156) and **11.70×** (r=312) on exp-108's six-margin `item_ii`
> differential family, the only differential floor this program has — **no
> differential floor exists at r=234 at all**. On a **common (peak)
> normalization** the per-bin angular deviation is at most **1.4760×10⁻⁴**
> (r=156) and **1.5266×10⁻⁴** (r=312), i.e. **0.285× and 0.295× of the coherent
> cross-term upper bound `2·exp(−τ_true) = 5.1793×10⁻⁴`** — the bound is honored
> at **all 48 bins at both radii**. On exp-110's **floor-gated local**
> normalization the **typical** resolved bin moves by **≈1.2×10⁻⁴** (median
> `9.43×10⁻⁵ – 1.60×10⁻⁴` across **all six** box radii at both radii — within
> 1.6× of the peak-normalized figure), with a tail of 2–10 low-SNR bins
> (SNR 1.01–2.79 against the `K=3` gate) reaching **1.4669×10⁻²** at r=156 /
> margin 32, **4.9648×10⁻²** at r=156 / margin 40 and **7.3202×10⁻²** at r=312 /
> margin 40 — a near-constant `|Δσ_scat| ≈ 2×10⁻⁵` **absolute** divided by
> whichever backward bin is smallest at the chosen box radius, **not a growing
> physical effect.** The per-bin half of any "better than `1.6×10⁻⁴`" reading is
> **WITHDRAWN**. **The source-facing face (`|θ| > 135°`, `0° = +x = downstream`
> per `lab/sections.py`'s CODE, whose docstring states the convention backwards)
> is entirely below the floor gate at TEN of twelve (r, margin) cells, so the
> observer-return channel is UNMEASURED there, not bounded** — and it has never
> been scored in the **absolute** units against the camera floor that PANEL.md
> measures constraint 2 with. Per-bin evidence exists at cpl=20 only and
> aggregate evidence at cpl=25 only, so **channel and resolution are fully
> confounded**; r=234 contributes aggregate channels only. **Fabrication
> consequence, at that scope:** a process implementing this design need not
> control the core/backing material to better than the **~10⁻⁴ aggregate
> level**, and this does **not** license varying the backing without measuring
> the backward-hemisphere channel **against an absolute floor**. The optical
> function is carried entirely by a **1.440 µm (2.40 λ)** graded-σ coating whose
> physical thickness is invariant across r = 156/234/312 and cpl = 20/25.
> **THIS ARTICLE FAILS CONSTRAINT 3 BY CONSTRUCTION** (a perfect absorber is a
> black shape in daylight — LOGBOOK ESTABLISHED) and this bound is **not**
> constraint-3 progress. **REALIZABILITY TIER: UNOBTANIUM-WITH-PARAMETERS**,
> inherited unchanged from exp-061, driven by the **70–350×** thickness gap
> (1.44 µm asked of a class that runs 100–500 µm), every literature figure behind
> it **WebSearch-snippet synthesis, NOT primary-source-verified (T18)** — and
> **INVARIANT, not improved, under exp-061's own MP-5 re-spec**, which by its own
> definition preserves `τ_true` rather than growing it, so thickening buys **no**
> backing freedom while costing thermal margin (3.79× → 1.35× vs NETD-lo 0.020 K)
> and a physically larger black silhouette.

**R21 discharge, and the self-certification string.** `run115.py:1243`
labels the M9 headline *"R21: stated here, not merely persisted"*, where
"here" is `results.json` — the artifact R21 names as **insufficient**.
That self-certification is **withdrawn**: R21 is discharged by **this
section**, in `NOTES.md`, and by the LOGBOOK close, not by a string
inside the persisted result. The string cannot be deleted from a frozen
Phase-4 artifact; deleting it is Iteration-93 Tier-1 item 3(vi).

**PHOTONICS' reconciliation, which is the strongest positive result the
sidecar contains.** The apparent 28.3× / 102.1× "exceedance" of
`2·exp(−τ_true)` by the printed local figures is **exactly the
normalization change**: `local/peak = 99.382×` (r=156) and `346.532×`
(r=312), and `28.32/99.38 = 0.2850`, `102.14/346.53 = 0.2947`. Under a
common (peak) normalization the corrected coherent cross-term bound is
**honored at every one of the 48 bins at both radii with ≈3.4× margin**.
A future citation reading only the blockquote would otherwise conclude
the bound is violated.

**MF-1's three-λ row, carried (with its two disclosed caveats).**

| λ | `cpl` (physical `λ/dx`) | `τ_true` | `2·exp(−τ_true)` |
|---|---|---|---|
| 450 nm | 18.75 | `8.629337967255916` | `3.5757×10⁻⁴` |
| 600 nm | 25.00 | `8.258813114090952` | `5.1793×10⁻⁴` |
| 750 nm | 31.25 | `7.909062748146141` | `7.3480×10⁻⁴` |

**Backing freedom is weakest in the red — 2.055× worse at 750 nm than at
450 nm — and has been MEASURED only at 600 nm.** PHOTONICS' two
clarifications: the `cpl` in that row is the **physical** `λ/dx` and
carries no discretization confound, and the shell stays above
`graded_black_shell`'s own 1.5λ entry-reflection bar even at 750 nm
(1.92λ). MATERIALS' F8 disclosure: **the 450/750 nm rows assume a
frequency-independent σ**, an idealization the Phase-1 document did not
state.

**The MF-15 discharge is VACUOUS, and that is a good outcome nothing
else records.** MF-15's third clause asked for the warm-up sensitivity
(`rel_dev 0.1227 → 0.2977`) *if reported at all*. No warm-up sensitivity
is persisted, because MF-7(a)'s **measurement** superseded the estimate
at zero extra cost (§4.6).

### 4.4 M7 — the model comparison, restated: **NO MODEL FAVOURED**

`results.json.m7.model_comparison["favoured"] = "constant-k"` is
**withdrawn as a shipped reading.** The selection rule
(`run115.py:435-436`) is a bare nearest-neighbour with **no rejection
test**, and it is structurally incapable of emitting the reading that is
true here — `lab/ARTIFACTS.md`'s own invariant applied to a
model-selection string. The same file's adjacent `m7["note"]` already
says *"N2_HOLDS requires BOTH candidate cost models to be wrong"*, and it
is right; `result_text` propagates the second without the first.

> **M7 model comparison: NO MODEL FAVOURED.** Both nominated models are
> refuted by this datum — constant-`k` by **8.15%**, constant-`ε` by
> **13.42%**, against the **6.08%** that separates them; the measurement
> sits farther from both models than the models sit from each other —
> while the un-nominated pure-`N²` model (`k = 3.0` exactly) fits at
> **0.18%**. Constant-`k` predicts `excess = +0.08682`, constant-`ε`
> predicts `+0.15295`; the measurement is `−0.00180`.
> `m7_underpowered` was computed from `d_rep` (**1.46%**) alone — the
> **smallest** of four measurable uncertainty channels (within-session
> 1.46% · across-reboot 2.06–2.81% · burst-vs-production 4.90% ·
> **machine-to-machine 18.20%, which this cycle's own M6 reports as
> unresolved**) — so the power gate excludes the dominant variance
> channel by construction. Both nominated models are parameterized on
> `kappa_ratio` while any cache/bandwidth superlinearity is a function of
> absolute `N`, so they are not being tested on the axis they are defined
> on.

**PHOTONICS' DRAM-bandwidth interpretation, stated and labelled
NOT-SCORED.** Both grids' working sets exceed the W-2145's **11 MiB L3**
by roughly an order of magnitude (6 `N×N` float64 planes ⇒ ≈94 MB /
≈212 MB = 8.2× / 18.4× L3; on a 7-plane count ≈112 MB / ≈251 MB = 10× /
23× — the plane count is the only difference and neither changes the
conclusion), so both sit in the DRAM-bandwidth-bound regime of an
explicit Yee stencil, where per-step time is proportional to cell count
and `G → 2.25` is what the regime predicts. The slightly **sub**-`N²`
sign is reproduced equally by a 0.33% fixed per-step overhead, a 0.54%
perimeter term, or a 3.8% extra cost in the absorbing band: **two grid
points cannot distinguish three unknowns from one equation** (R5/R30
lineage). It is a mechanism consistent with one ratio, **not evidence**,
and it does **not** license "FDTD scales as `N²`, therefore `k = 3.0` is
the right cost exponent" — which MF-7(b) already warns M5 cannot
license.

**The honest `KAPPA_COST_EXPONENT` statement, for the record.**

> `k = 3.2053` is **not reproduced on this bench at
> `kappa_ratio = 1.5`**: the bench's two sessions give `k = 2.9955`
> (scored) and `k = 3.0459` (session 1, not scored), against exp-114's
> cloud `k = 3.4909` at the same `kappa_ratio` and R28's founding
> `k = 3.2053` at `kappa_ratio = 2.0`. Five measurements span
> **`2.9955 – 3.6090`** — 0.61 in exponent, 22% in `G` — with machine,
> contention, `cpl`, absolute `N` and protocol confounded across them.
> **`k` is a per-machine, per-configuration fitted parameter with one
> measurement per configuration, and has never been shown portable.** The
> record may **NOT** say `KAPPA_COST_EXPONENT` is a cloud-contention
> artifact: contention is a demonstrated, signed, **partial** explanation,
> insufficient at the measured magnitude — the bench's own 4–8% per-step
> slowdown between sessions moved `G` by **+2.81%**, **1/7.9** of the
> 22.24% bench-to-cloud gap, and its sign is protocol-inconsistent within
> that same pair (`−0.54%` on the short protocol, `+2.81%` on the
> sustained). **`KAPPA_COST_EXPONENT = 3.2053` is RETAINED for the cost
> gate as the conservative (larger) choice — a gate-margin decision,
> labelled as such, not a scientific one.**

### 4.5 M3's anchor — the sharpest finding of the cycle, disclosed and NOT scored

**M3's `G-DURATION-INVARIANT` is scored against a cloud anchor
(`R_DEG = 7.596%`) that this cycle's own readings supersede.** The
bench's own duration response is **+2.296% (r=156)** and **−1.395%
(r=234)** at matched protocol, first-reading construction — 3.3× smaller
than the cloud anchor and **opposite in sign between the two grids**. On
any bench-native anchor M3 reads `G-NOT-DURATION-INVARIANT`:

| anchor | `M3_INVARIANT_BAR` | M3 | `m3_scored` | `m6_directional_only` | `may_move_logbook_verdict` |
|---|---|---|---|---|---|
| cloud `R_DEG = 0.075964` (as filed) | `0.037982` | `G-DURATION-INVARIANT` | **True** | **False** | **True** |
| bench first-reading `R_DEG_bench = 0.022961` | `0.011481` | `G-NOT-DURATION-INVARIANT` | **False** | **True** | **False** |
| bench mean-form `0.016630` | `0.008315` | `G-NOT-DURATION-INVARIANT` | **False** | **True** | **False** |

The bench route reaches one boolean further than the drift route:
because `m3_scored` gates on `d_rep ≤ M3_INVARIANT_BAR` and
`d_rep = 0.014633` exceeds **both** bench-native half-bars, a bench
anchor also sets `m3_scored = False`, which sets
`may_move_logbook_verdict = False`. **So this cycle's own claim that M5
may move exp-114's LOGBOOK entry is anchor-fragile, on an anchor this
cycle's own data supersedes.**

**Independently, VISION's drift correction.** From `results.json.drift`:
r=156 `relative_rate_per_s = −4.552366720982913e−06` (−1.6389%/hour, the
later reading FASTER); r=234 `+1.8661564961051803e−06` (+0.6718%/hour,
the later reading SLOWER); `d(lnG)/dt = 6.418523×10⁻⁶ /s = +2.311%/hour`.
S-pass effective midpoint `1788669759.8136`, U-pass `1788671660.1500`,
gap **1900.336 s** ⇒ drift contribution to `G` over that gap
**+1.220%**, against a measured signed `G_sus/G_short − 1 = −2.903%`,
giving a **drift-corrected duration effect of −4.123%** (first-order
subtraction, VISION's construction; the multiplicative form gives
−4.080%). `0.041231 > 0.037982` and `< 0.075964` → **PARTIAL**, which
under MF-9's inverted rule also sets `m6_directional_only = True`. **The
drift and the duration effect push in opposite directions, so the raw
`d_dur` is a lower bound on the duration effect and the cycle scored the
flattering end.**

**Neither correction is scored, and that is deliberate (R17).** R17
requires the bar be justified *before the run* against the largest
already-established comparable magnitude on file. At Phase 3 no bench
figure existed and `R_DEG` was the largest comparable; the bands were
pre-registered and committed at `f75b905` before any reading, and
PHOTONICS verified the frozen Predictions block is **byte-identical** to
`build_predictions_text()` — pre-registration is a **verified property of
the git tree**, not a claim. Post-hoc re-anchoring to move a verdict is
the estimator-switching this program ruled out at Iteration 1 and it is
declined (decline **D-3**).

**Forward, and this is the half every future bench cycle inherits:
`R_DEG_bench = 0.022961` is this cycle's own deliverable and is the R17
anchor for every future bench cycle (mean-form `0.016630` disclosed as
the alternative); the cloud `R_DEG` is retired for bench work.**

**And the physics under the label, which is better than the label.**
Using each grid's mean-form duration response,
`(1 + r₂₃₄)/(1 + r₁₅₆) − 1 = −0.029078`, reproducing the filed
`d_dur = 0.029034` to four digits. The two grids' duration effects are
**opposite in sign, so in the ratio they ADD.** Had they been equal and
same-signed — the grid-independent throughput factor that R31's
r=156-only control and R33's normalization both assume — they would have
**cancelled** and `d_dur` would read ≈0.4%. **R31/R33's founding
grid-independence assumption is measured FALSE at the 2–3% level on one
clean machine**, twice and in two independent ways: the within-session
duration response above, and the session-1-vs-2 grid-differential
slowdown of **2.96 pp** (§4.9). That is this cycle's best
physics-of-the-instrument result and it existed in no committed file.

### 4.6 M5 and M6 read jointly — a containment result, not a replication

The bench's `G = 2.245940496842567` and the cloud's
`G_E = 2.74550565394726` sit on **opposite sides** of
`reference_ratio = 3.6680107109370383` (in `1.5·G` space) and **both
score CONFIRM**, while differing from each other by **18.20%** —
**above** M6's own **15.295%** transfer bar. `G_E/G_bench − 1 = +0.22243`
and `G_bench/G_E − 1 = −0.18196` are both inside the AMBIGUOUS window.
**M5's CONFIRM band is wider than the between-machine spread it must
survive**, and this cycle's central estimate `k_B = 2.995546218006855` is
**0.149%** from the pre-R28 exponent `k = 3.0`. QUANTUM's
protocol-matched cloud value `G_E/f = 2.880173` (using exp-114's own
session's `p_prod/p_burst = 0.9532431491914767`) gives
`|T − 1| = 0.2202` — **the known protocol correction moves M6 further
from transfer, not toward it.**

**The two-point interval, and the scope statement that is mandatory
with it.** `C₁₅₆ = −1.1542737280358781` s/scene,
`p₁₅₆,∞ = 0.04974366400589843`; `C₂₃₄ = +2.0759888398786654`,
`p₂₃₄,∞ = 0.11031604592917955`; `G_burst = 2.2458389149395477`,
`G_prod = 2.2276295684987977`, `G_∞ = 2.217690396029104`. Two
disclosures the record owes: **`C₁₅₆` is a negative fixed per-scene
overhead**, which is not an overhead — the model is being evaluated
outside its own physical interpretation on that grid; and **both
production endpoints (8000 / 12000 steps) lie OUTSIDE the `[1000, 3334]`
bracket the two points define**, so they are extrapolations. The
interval's **1.27%** narrowness is therefore **not** evidence that the
protocol mismatch is small, and it structurally cannot contain the
burst-vs-production step exp-114 itself measured at **4.90%** (3.9× the
interval's full width). `m5_protocol_caveat = False` is a true statement
about a **narrower** question than MF-7(a) promised. The outcome stands —
no plausible correction moves it — and the scope statement is mandatory.
(Minor, disclosed: `G_sustained`, a mean of ratios, exceeds
`interval_hi`, a ratio of means, by `4.52×10⁻⁵` relative; the interval's
own note discloses the construction difference. Non-load-bearing.)

### 4.7 The six corrections — what shipped FALSE in the frozen text

Each is desk-correctable at zero FDTD cost, each was introduced at or
before Phase 3, each was caught only at Phase 5, and **none is
load-bearing to a scored verdict.** Together they fire R20 (§ Phase 5,
CHECKPOINT).

| # | Statement as frozen | Correction, with the reproduced value |
|---|---|---|
| **α** | *"only the margin-32 array is persisted"* (`d_scope.margin_scope`, inside the quotable headline's own justification) | **FALSE of exp-110**, the channel the headline quotes: **all six** margins are persisted. Margin-40 maxima are **`4.9648×10⁻²`** (r=156) and **`7.3202×10⁻²`** (r=312) — **3.384×** and **1.383×** the quoted margin-32 figures. The headline understates its own instrument in the one direction that matters for a fabrication warning, on data already on disk. |
| **β** | *"`ITEM_I_CONFIRM_REL = 0.05` … 330× looser than the quoted figure"* | **FALSE against the quoted figure**: `0.05/1.4669×10⁻² = 3.41×` (r=156) and `0.05/5.2900×10⁻² = 0.95× — TIGHTER`. The 327.5× reproduces only against the **withdrawn** peak-normalized figure. The argument survives; the number does not. |
| **γ** | *"the core/backing freedom survives and **strengthens** … `τ_true` grows with thickness"* (`e_tier.forward_conditional`) | **FALSE against its cited source.** exp-061's MP-5 defines its multiple as the thickness at which a real, lower-α CNT-forest-class coating reaches the **SAME** `τ_true ≈ 8.2588` — `τ_true` is held **FIXED** and the thickness varies to hit it. So `2·exp(−τ_true) = 5.1793×10⁻⁴` is **unchanged at 230× and at 730× alike**: the bound **survives; it does not strengthen.** Mitigating and verified: the string appears **nowhere** in `result_text` and nowhere in the quotable headline. |
| **δ** | *"180× below the smallest … 3455× below the largest … **even allowing** a 4× standing-wave enhancement"* (`perturbation.closure`) | **FALSE as written**: `5.666×10⁻⁶/3.1472×10⁻⁸ = 180.04` and `1.087×10⁻⁴/3.1472×10⁻⁸ = 3454.94` are both computed **without** the 4×. **With** it: **45.01×** and **863.73×**. The RULED-OUT conclusion survives at 45×. |
| **ε** | *"`geom_fixedabs_cpl` sizes STEPS so each grid gets ~2 domain crossings"* (`DISCLAIMER_115`, in **both** `predictions_text` and `result_text`) | **FALSE**: at `geom_fixedabs_cpl`'s own STEPS (8000 at r=156, 12000 at r=234) the front travels **1.293** domain widths (**1.407** source-anchored) on **both** grids. The energy-ledger N/A conclusion it supports is *strengthened* by the correction. |
| **ζ** | *"4.47×"* in `DISCLAIMER_115` and `b_floor…reading`, beside the committed function's own `4.4646` printed as *"4.46×"* in the same document | **Self-contradiction inside one artifact.** The Phase-2 docket said `4.46×`; the `4.47` was introduced at Phase 3. The reproduction gate's own hardcoded `expected = 4.4653` is a **third** value, and passes only because `rel_bar = 1e-3` is 6.4× the disagreement — a hand-typed expected value inside the machinery built to prevent R4. **The computed value is `4.464601791167039`.** |

**And the near-miss, corrected rather than defended.** *"the SAME ORDER
as the measured aggregate deltas"* holds for four of six channels within
a decade and fails for two (`12.06×` for r=156 `σ_ext`, `45.70×` for
r=234 `σ_abs`). **The exact statement is: the six measured aggregate
deltas are bracketed from above by `2.38×–45.70×` (against the scale
`exp(−τ_true)`) and `4.76×–91.41×` (against the bound
`2·exp(−τ_true)`).**

**R18 — documented scope stronger than the source, four instances.**

1. **The M9 gate WITHHOLDS the headline string; it does not HALT.**
   `DISCLAIMER_115` says *"any mismatch HALTs it and it is reported
   NOT-REPRODUCED rather than published"*. What the code does is have
   `build_m9_bound_text` return the WITHHELD text while **returning and
   persisting every sub-dict the headline is built from**;
   `c_physics["withheld"]` keys on **2 of 11** checks.
2. **The reproduction gate is stated at `<1e-12` and coded at
   `1e-15 … 1e-2`** — with the two **load-bearing** differential-floor
   ratios gated at `1e-3`.
3. **Two of the eleven checks cannot fail**: they compare literal
   arithmetic expressions written on the same line (`0.4*25` vs `0.5*20`;
   `60/25` vs `48/20`), padding apparent coverage from 9 to 11. (This is
   a different check from the `τ_true` **bit-identity** gate, which
   PHOTONICS correctly defends: that one cannot fail *for this family* by
   construction but will catch a future member that breaks the identity.
   No conflict.)
4. **`σ_abs`, `σ_ext` and both channel-sum residuals are never passed
   through `gate()`** — only `σ_scat` is, while the headline's "at most
   `1.0874×10⁻⁴`" is a max over all six.

**The `lab/sections.py` angle-convention finding — a live R18-class
defect in shared `lab/` machinery.** The docstring at `:209-210` and
`:223-224` states *"0 deg = −x (toward the source, 'backward'), ±180 deg
= +x (downstream, 'forward')."* The code at `:246-247` computes
`arctan2(yy−bcy, x1−bcx)` with `x1 > bcx`, so the **high-x face maps to
≈0°**. Four independent confirmations: the inline comments; `widths()`'s
own face assignment (`p_back` at `x0`, `p_fwd` at `x1`) with the source
at low `x` (`SRC_X = 160`, `CX = 630`), so propagation is **+x**; the
committed pattern data (the `|θ| < 45°` sector carries **98.3%** of total
`σ_scat` at r=156 — nothing puts a 10⁶:1 lobe on the backscatter side of
a black absorber); and exp-112's own "0 of 12 backscatter bins resolved"
count, which reproduces exactly on the `|θ| > 135°` set. **So
`0° = +x = forward/downstream` and `±180° = −x = backward, toward the
source and the observer`. exp-115's `±138.75°` observer-return claim is
CORRECT under the code and inverted under the docstring it cites four
lines away.** This is **not exp-115's defect** — it has stood since
exp-017, whose `NOTES.md:22` propagates it verbatim — but exp-115 is
where it became load-bearing and where it was found, and it sits directly
under PANEL.md's **constraint-2** metrics row. It is **Iteration-93
Tier-1 item 2**, with a positive control (assert the argmax bin of a
`graded_black_shell` pattern lies within ±30° of 0°) as the part that
matters: a check that *can* produce the reading meaning "bad" would have
caught the inversion.

**The observer face is UNMEASURED, not bounded at ~5%.** Restricting to
`|θ| > 135°` (the twelve source-facing bins), the resolved counts are
0/12 at every (r, margin) cell except r=312 margin 32 (**2/12**) and
r=312 margin 40 (**4/12**) — **ten of twelve cells entirely below the
floor gate.** At r=156 the headline's own max bin (`+123.75°`) is **not
on the observer-facing face at all**; it is a side-face bin. And the
units are wrong for the constraint: PANEL.md scores constraint 2 as
**backscatter to observer vs camera floor**, an *absolute* comparison via
`emit.observer_record`, while the sidecar reports a *relative* movement
of a face carrying `3.4×10⁻⁶` of total `σ_scat` and never compares the
absolute `≈2×10⁻⁵` change to any floor. The absolute-units question is a
real open item (Iteration-93 Tier-3 item 11).

**Median vs tail — the better physical statement.** Median resolved
`local_rel` across all twelve `(r, margin)` cells spans
`9.4304×10⁻⁵ → 1.6020×10⁻⁴`, a **1.699×** total spread, and the
peak-normalized figures (`1.4760×10⁻⁴`, `1.5266×10⁻⁴`) sit **inside**
that band: **the two normalizations agree on central tendency to within
1.6×**, and the 99.4× / 346.5× divergence is entirely a **tail**
phenomenon. `|Δσ_scat|` at the four quoted max bins varies by only
**1.31×** while `local_rel` varies by **5.0×** — the core swap moves the
backward-hemisphere per-bin `σ_scat` by a near-constant **≈2×10⁻⁵
absolute**, and the "1.5%–7.3%" figures are that constant divided by
whichever backward bin happens to be smallest at the chosen box radius.

### 4.8 Cycle spend, and the gate's scope

```
session 2 (results.json)          : 18 calls, 3690.309 s of Sim.run, 3700.506 s elapsed
session 1 (…_interrupted…json)    : 12 calls, 2228.700 s of Sim.run, 2234.835 s elapsed
CYCLE TOTAL                       : 30 calls, 5919.009 s = 54.8 % of COST_GATE_TOTAL_S (10800 s)
```

`result_text`'s *"18 real FDTD calls (Sim.run), 3700.5s (61.68 min) total
wall time **this cycle**"* understates the **cycle** by **12 calls and
2218.503 s**. **This is an R21/R4 defect in the sentence, NOT an R19
violation**: the R19 assert is present, conditional and honest about what
it counts, but `_SIM_RUN_CALLS` is a module global reset at process
start, so **the invariant is per-invocation by construction while the
sentence it certifies says "this cycle."** The fix is the sentence plus a
cycle-scoped ledger (Iteration-93 Tier-2 item 6), not a new assert.

**The budget gate did not breach and is not an R27/R28 violation this
cycle**: it is executable, sits causally upstream of every `Sim.run()`
(three PROCEED projections at `after_S156`, `after_S234`, `after_U234`,
each before the next call — projected totals 4605.2 s, 4073.5 s,
4071.2 s against the 10800 s bound), and nothing breached at 54.8% of the
bound. **But the hole is real and now demonstrated: the resource is
consumed by the *cycle* and the gate is armed by the *process*. A
twice-interrupted cycle could spend 2–3× the bound with every gate
reading PROCEED.** That is R28's own founding lesson one scope level up.

### 4.9 Session 1 as a NOT-scored across-reboot replicate

Filed as **`sensitivity_session1_across_reboot_DO_NOT_SCORE`**: four
complete readings, same bench, same code, same protocol, 4.75 h earlier,
committed at `5bb62cc`, appearing **zero times** in `results.json`,
`result_text`, `run115.py`, `analyze115.py` or `chunk_runner115.py`
before this section. Re-derived:

```
per-step, session 1 vs session 2:  S156 +4.775 %   S234 +4.208 %
                                   U156 +5.369 %   U234 +8.328 %
G_short   2.3005776183025777  vs 2.3130982736423493   −0.541 %
G_pair1   2.2922398627376155  vs 2.2296275647790664   +2.808 %  ( 1.92 × d_rep )
                              vs 2.245940496842567    +2.061 %  ( vs the ABBA mean, 1.41 × d_rep )
k(session 1) = 1 + ln G/ln 1.5 = 3.0458713436566054   rel_dev 0.06260911838284892   CONFIRM
excess(session 1)              = +1.8773 %                                          N2_HOLDS
```

**Why it is NOT scored, and the reason is decisive.** Session 1's `U234`
is the largest deviation of the four (**+8.33%**) **and is the reading
immediately preceding the host hang**; the slowdown sequence in execution
order is `4.78 / 4.21 / 5.37 / 8.33%` — **progressive and tail-weighted,
a ramp into a fault, not a clean replicate** — and it contaminates
exactly the reading that carries the excess. Second, it is
cross-session: folding it into `G_sustained` would break the
R33-immunity M5 currently has by construction (decline **D-4**).

**Admitting it changes NOTHING, which is the strongest possible reason to
admit it.** Scoring session 1's pair as a hypothetical third pair
(explicitly NOT adopted): 3-pair `G = 2.2613736188075833` →
`k = 3.0124356`, `rel_dev = 0.07523` **CONFIRM**; `excess = +0.5055%`
**N2_HOLDS**; `|T−1| = 0.17634` **AMBIGUOUS**; max pairwise spread across
the three pairs **2.769%** → M4 would read
`MARGINAL-M3-SCORED-M7-POWERED`. **No verdict changes and no composition
boolean flips.**

**What it obliges the record to say about M4.** `M4`'s `REPEATABLE` is
correct **within one session and is not robust to a session change**: the
across-reboot spread (**2.06%** on the ABBA mean, **2.81%** on the
matching pair) is **1.41×–1.92× the `d_rep` that is the sole input to the
power gate** — and `d_rep` is the only noise instrument three composition
rules consume.

**And the positive finding buried in it, which is the most citable
science this run produced.** A 4–8% common-mode per-step slowdown moved
`G` by only **−0.54%** on the short protocol — **`G` is largely robust to
session-level load** — while the between-**machine** difference is
**18.20%**, i.e. **9–34× the between-session difference on the same
machine.** **M6's `AMBIGUOUS` is therefore better read as a genuine
machine property than as session noise.** Obtained for free, from the
session the outage wrecked.

### 4.10 What the instrument itself did right

This section is not a catalogue of defects, and the following are all
first-time results:

- **ABBA worked, and it was measured.** Mean-A midpoint
  `1788671659.5939`, mean-B `1788671660.7061` — residual lag **+1.112 s**
  against the `≈802.8 s` that ABAB's `(a+b)/2` would have left: a
  **721.8× reduction** (Red Team's ruled figure; my own re-derivation on
  the `(|a|+|b|)/2` construction gives 722.5× — same finding either way).
  The two pairwise lags are `+804.654 s` and `−802.430 s`, **symmetric to
  0.277%**. EM's A3 / RT-6 closed form is now empirically confirmed for
  the first time in this program; MF-6(a) earned its keep.
- **`d_rep` IS exactly the grid-differential log-drift**, and the
  consequence must be written down:
  `ln(G2/G1) = D_234 − D_156 = +0.0020725314347838 − (−0.0124543173049980)
  = +0.0145268487397818`, and `exp(·) − 1 = 0.014632876199767608` against
  the filed `0.01463287619976741`. **Common-mode drift cancels in `d_rep`
  exactly** — a uniform 10% session slowdown across both grids would
  still read `REPEATABLE`. ABAB's null channel was blind to monotone
  drift; ABBA's is blind to common-mode drift; neither ordering, with two
  sustained readings per grid, produces a channel that can see it. **`d_rep`
  and the MF-6(c) drift block are two independent quantities and their
  exact difference — not three pieces of evidence.** Adding a common-mode
  channel from the per-scene sub-timings already persisted is
  Iteration-93 Tier-2 item 8.
- **A real per-scene replicate floor**, from MF-6(b)'s per-scene wall
  times: comparing the same scene across the two sustained readings on a
  grid gives three genuine replicate pairs — r=234 `U234b/U234` =
  `1.00093 / 1.00323 / 1.00207`, **sample std 0.115%**; r=156
  `U156b/U156` = `0.97553 / 0.99090 / 0.99662`, **sample std 1.091%**,
  **dominated by one cold-start scene** (`U156/empty`, the first
  3334-step run on that grid in that session, ran 2.45% slower than its
  repeat while `peccored` moved 0.34%). The r=156 "rate" of −1.639%/hour
  is therefore an unwarranted rate-ification of a one-off step.
- **The central result is robust to the largest identifiable defect in
  its own inputs** (EM's not-scored substitution): replacing
  `U156/empty` with its own repeat moves `U156` per-step
  `0.04970505 → 0.04929552`, `G_sustained → 2.255202009175459`
  (**+0.412%**) and `k_B → 3.0056955221614476` — **toward exactly 3.0**,
  with **every verdict unchanged**.
- **No drift systematic is resolved at this precision** (PHOTONICS F10):
  the two same-grid rates have **opposite signs** and 6× different
  magnitudes (−1.6389%/hour at r=156, +0.6718%/hour at r=234). The record
  must say that, **not** report a measured drift rate — otherwise a
  future cycle anchors a bracket on `−0.0164 h⁻¹` the way this one
  anchored on `R_DEG`. R17's own lesson, applied pre-emptively.
- **MF-5 was load-bearing even though it changed no verdict** (VISION's
  counterfactual, and a new member of this program's class rule):
  evaluated at *this* cycle's own `G`, the un-fixed invocation returns
  `1.5**3.3689107 = 3.9195457`, `rel_dev = 0.0685753` → **CONFIRM** — the
  same verdict label from a `measured_ratio` wrong by **16.3%**. *A wrong
  computation that agrees with the right one is indistinguishable from
  correctness by verdict alone.* That is `lab/ARTIFACTS.md`'s invariant
  in its **false-positive** form.
- **The largest unmodelled systematic in the dataset, found by
  THERMODYNAMICS and recorded by no instrument in the cycle**: a
  monotone within-reading ramp on the r=234 **SHORT** reading —
  `peccored/empty − 1 = +5.635%` in session 2 and **+6.021%** in session
  1, reproduced in both independent sessions — while every **sustained**
  r=234 reading stays inside `±0.8%` on the same statistic (`+0.162%`,
  `+0.276%` in session 2; `−0.776%` in session 1). **It sits inside the
  reading that sets `G_short` and the budget gate's second
  re-projection.** Iteration-93 Tier-3 item 13, and the only remaining
  plausible home for exp-114's disputed 4.467% within-run level shift now
  that warm-up amortization is refuted at 16.9×.
- **Both pre-registered protocol models were REFUTED by the
  measurement.** `G ≈ 2.5403` (drift/degradation) and `G ≈ 2.8681–2.8802`
  (warm-up amortization) against the measured `2.2459405`; and THERMO's
  own cloud-derived warm-up constant estimate of 35.08 s/scene against
  the measured `C₂₃₄ = +2.076` — **16.9× smaller** — with `C₁₅₆`
  **negative**. Pre-registering two models and having the data reject
  both is house discipline working, and THERMO reported its own
  pre-registered expectation (`d_dur` negative, −4% to −6%) **REFUTED**
  before reporting anything it got right.
- **R23 and its First Addendum are DISCHARGED from the artifact, for the
  first time in this program.** `DISCLAIMER_115` (3788 chars) is a
  literal substring of **both** `predictions_text` and `result_text` in
  committed `results.json`; both builder functions carry internal asserts
  (`run115.py:1185`, `:1252`); `analyze115.py:259` and `:277` assert both
  sides; and there are **two committed, re-invocable call sites**
  (`run115.py --predictions-only`, `run115.py --selftest`), the second
  executed at Phase 3 with synthetic operands before any bench data
  existed.
- **The MF-12 absolute identity gate is a real gate**: 10/10, `build_sim`
  byte-identical to `chunk_runner114`'s, and the bench trust suite 41/41
  in 87 s with its platform named and its console record committed
  (VALIDATION.md docket-14).

---

## Phase 5 — Review

Six blind seats, then Red Team's final audit
(`phase5_redteam_audit.md`), then this close. **T1 escape route: N/A —
unanimous across all seven seats, and verified structurally by three of
them independently**: `chunk_runner115.py::build_sim` /
`_time_control_blend` bracket `sim.run()` only; the executed path
contains no `full_capture`, no `lab/sections.py` call, no
`lab/ambient.py` call and no angular instrument, so the cycle produces no
constraint-1/2/3/4 observable and moves none.

### 5.1 The six seats

- **PHOTONICS — CONFIRM (overturned to PARTIAL by Red Team).** The most
  valuable single contribution: a bit-exact re-import and leaf-diff of
  the whole analysis (16 last-ulp mismatches, all inside the `τ_true`
  desk integral, max relative `6.45×10⁻¹⁶`, attributable to numpy 2.5.0
  vs the bench's 2.4.6), and the **byte-identity of the frozen
  Predictions block against `build_predictions_text()`** — which makes
  pre-registration a verified property of the tree rather than a claim.
  **Sharpest finding: F4's reconciliation** — the printed local-frame
  28.3× / 102.1× "exceedance" of `2·exp(−τ_true)` is *exactly* the
  normalization change, and under a common peak normalization the
  corrected bound is honored at **all 48 bins at both radii** with ≈3.4×
  margin. Also F5 (the angle-convention inversion, with three independent
  physical checks), F8 (`exponent_B ≡ k_B`), F9(b) (contention accounts
  for 1/8.1 of the cloud/bench gap), F9(c) (`loadavg` blindness) and F10
  (no drift systematic resolved).
- **MATERIALS & METAMATERIALS — PARTIAL.** The deepest findings in the
  set, and the seat audited its own bound harder than anyone else would
  have — **five of five confirmed**, including a MATERIALS-charter error
  in MATERIALS' own sidecar, disclosed first. **Sharpest finding: the
  observer face is UNMEASURED at 10 of 12 (r, margin) cells**, so the one
  constraint-adjacent sentence in the quotable bound reports as bounded a
  channel that is not measured — and reports it in **relative** units
  where PANEL.md's constraint-2 row is **absolute**. Also the margin-40
  maxima and the false "only the margin-32 array is persisted"; the "330×
  looser" refutation; the median-vs-tail reading; the MP-5 inversion;
  "the gate is not a HALT"; the two checks that cannot fail.
- **ELECTROMAGNETISM — PARTIAL.** The most complete instrument analysis
  in the program's history: the 721.8× ABBA measurement, the
  `d_rep ≡ D_234 − D_156` identity and its common-mode blindness, the
  four composition booleans, the negative `C₁₅₆` and
  both-endpoints-extrapolated finding, the per-scene noise floor and the
  cold-start substitution. **Sharpest finding: the bench-native anchor
  flip** — on this cycle's own duration response M3 reads
  `G-NOT-DURATION-INVARIANT` and `m6_directional_only` becomes True (Red
  Team carried the chain one boolean further, to `m3_scored` and
  `may_move_logbook_verdict`). EM's standing observation, adopted
  verbatim into the CHECKPOINT entry: *"both new instances sit inside the
  `DISCLAIMER_115` string that MF-10 wrote to fix exactly this class —
  the correction machinery is now the place the class recurs."*
- **THERMODYNAMICS — PARTIAL.** One conclusion refuted; everything else
  confirmed, including a defect nobody else could have found. **Sharpest
  finding: the +5.63% / +6.02% monotone within-reading ramp on the r=234
  SHORT reading**, reproduced in both independent sessions, absent from
  every sustained reading, sitting inside the reading that sets `G_short`
  — the largest unmodelled systematic in the dataset, recorded by no
  instrument in the cycle. Also the cycle-spend arithmetic (30 calls /
  5919.0 s), the per-invocation gate scope, the R25 resume-path
  deviation, the `loadavg` class-rule finding, and the withdrawal of its
  own OV-3 request (*"I was wrong about the magnitude and Red Team was
  right about the method"*). **Refuted**: its §2.4 conclusion that
  `KAPPA_COST_EXPONENT = 3.2053` is a cloud-contention artifact — the
  mechanism is adopted NOT-SCORED, the causal conclusion is refuted at
  the measured magnitude (§4.4).
- **QUANTUM OPTICS — PARTIAL.** The sharpest statistical reading:
  the v2 reconstruction to 17 digits with the correct ruling that nothing
  "closed"; the protocol-matched `G_E/f = 2.880173`, `|T−1| = 0.2202`;
  four grounds against `favoured`; the R33(a) credit; two self-refutations
  accepted without reservation. **Sharpest finding: mutual AMBIGUITY** —
  `G_E/G_bench − 1 = +0.22243` and `G_bench/G_E − 1 = −0.18196` are both
  inside the AMBIGUOUS window while each scores CONFIRM against a
  reference lying between them: **M5 is a containment test, not a
  replication test.** Its D-Q4 (composition is one-directional; nothing
  gates `may_move_logbook_verdict` or the model comparison on M6's
  AMBIGUOUS) is elevated into Iteration-93 Tier-1 item 3(viii). One
  defect **refuted**: D-Q8 (7c/14t) — `NOTES.md` Setup already states
  both figures correctly, struck from the R20 tally.
- **VISION SCIENCE — PARTIAL.** The strongest single finding and the
  best-prepared hand-off in the set. **Sharpest finding: the MF-5
  counterfactual** — at this cycle's own `G` the un-fixed invocation
  returns **CONFIRM** from a `measured_ratio` wrong by 16.3%, so *a wrong
  computation that agrees with the right one is indistinguishable from
  correctness by verdict alone*. Also the drift correction (which VISION
  correctly refuses to score, naming the Iteration-1 estimator-switching
  rule itself), the live caveat-lint verification and the
  `LOGBOOK.md`/`PLAN.md` required-site gap, the LOGBOOK/PLAN supersession
  table including the **sign-flipped `excess`**, the M8 finding, the M7
  incoherence, the five-different-bars finding, and §2.10's three defects
  in D1 — of which the **self-certifying class test** (a cycle can become
  exempt from the seven metric rows by declining to name a mechanism,
  which is precisely what a drifting program does) is adopted into
  Iteration-93 Tier-0.

### 5.2 Red Team's adjudications

| Conflict | Ruling |
|---|---|
| PHOTONICS **CONFIRM** vs five **PARTIAL** | **PARTIAL.** A cycle whose computation is clean and whose frozen text is false in five places is not a CONFIRM; in this program **the record IS the product**. |
| MATERIALS ("headline understates by 3.38×") vs PHOTONICS ("appears to exceed the bound by 28×/102×") | **Both correct; not a conflict** — two different normalizations. The bound may only be stated in the **peak-normalized** frame where it is commensurable. |
| EM `+1.663%/−1.293%` vs THERMO `+2.296%/−1.395%` (bench anchor) | **Mean-of-sustained vs first-sustained. Both reproduce.** THERMO's is `R_DEG`'s own construction and is the forward R17 anchor; EM's is the disclosed alternative. **M3 flips either way.** |
| VISION's drift route (M3 → PARTIAL) vs EM/THERMO's anchor route (M3 → NOT-INVARIANT) | **Both hold, on different routes with different reach.** Route 1 flips `m6_directional_only`; route 2 additionally flips `m3_scored` and `may_move_logbook_verdict`. |
| THERMO "`k = 3.2053` is a cloud-contention artifact" | **REFUTED at the magnitude**; mechanism adopted NOT-SCORED. |
| MATERIALS "two gate checks cannot fail" vs PHOTONICS "the bit-identity gate correctly cannot fail" | **Different checks. Both right.** |
| EM R20 = 2 (no fire) · MATERIALS R20 = 3 (deferred to Red Team) · PHOTONICS R20 = 0 | **Each correct on its own slice; the union is SIX. R20 FIRES.** |
| QUANTUM D-Q8 (7c/14t) | **REFUTED**; struck from the tally. |
| EM D-7 (`d_rep` denominator `/G1` vs `/Ḡ`) | **A convention note, not a defect.** State the denominator; do not change the code. |

**Rules checked and NOT fired, so the absence is on the record:** R23 +
First Addendum (discharged from the artifact); R24 (all fifteen mandatory
fixes wired into code; the two disclosed partials disclosed, not
claimed-and-unwired); R25 (declines numbered, `DECLINE_8` exists — the
two new disclosures at §4.0 and §4.9 are what keep it from firing); R17
(satisfied at freeze; the forward anchor ruling is a disclosure, not a
violation); R19 (the assert exists and is honest about its scope — the
prose that quotes it is what is wrong); R27/R28 (executable, upstream, no
breach at 54.8% of the bound); R29 (module identity asserts executed);
R30/R32 (correctly declared N/A); R31/R33 (M5 is R33-immune by
construction; addendum (a) honored better than asked; addendum (b)
discharged by direct grid-native measurement, which is the whole cycle);
R13 (correctly withdrawn per MF-2 rather than mislabelled). **R21 does
NOT fire, conditionally** — four seats found the exposure and all four
ruled it should not fire *because this Result section did not yet exist*;
it fires automatically at Iteration 93 if any item of the audit's §3.1
discharge list is missing from this close.

### 5.3 CHECKPOINT (Iteration 92, Phase 5, 2026-09-06, criterion 4 — R20)

**Criterion 4 FIRES on R20's automatic clause. NOTIFICATION, NOT A
PAUSE. Marsh is NOT convened.**

R20's operative text: *"three or more independent R4-class defects …
surviving a document's own Phase-3 prediction-freeze into its
Result/Learned sections, each caught only at Phase 5 — not earlier — in a
single document, constitutes a Checkpoint-4-grade recurrence pattern **on
its own, independent of whether any individual instance is load-bearing
to a scored verdict** … fires Checkpoint criterion 4 automatically, **no
further deliberation**."* R20 is not on its founding instance; its
non-firing precedent does not apply.

**The tally is SIX against a bar of three** — α, β, γ, δ, ε, ζ of §4.7:
(1) "~2 domain crossings" → 1.293/1.407 on both grids [EM D-1]; (2) the
4.47 / 4.46 / 4.4653 triple [EM D-2, MATERIALS D12]; (3) "only the
margin-32 array is persisted" [MATERIALS D4]; (4) "330× looser"
[MATERIALS D6]; (5) "even allowing a 4×" [MATERIALS D10]; (6) the MP-5
forward conditional [MATERIALS D9]. Instances 1–4 sit in `result_text`,
which was until this close the **only** Result prose in the repository.
**Nobody had the union**: EM tallied two on its own slice and ruled it
does not fire, MATERIALS tallied three and explicitly deferred the ruling
to Red Team, PHOTONICS found none on the three line-ranges it checked —
all three correct about their own slice. Struck from the tally so the
count is honest: QUANTUM's D-Q8 (refuted), THERMO's D1 (a wrong scope of
words, R21/R4-adjacent — counting it would double-count), MATERIALS' D13
(R9), VISION's D4 (R18).

**Why a notification and not a pause:** no individual instance is
load-bearing to a scored verdict and every one is desk-correctable at
zero FDTD cost. **Under R34 this firing self-closes the moment Iteration
93's Red Team final audit confirms, from primitives, that the §3
discharge list has landed** — R34's conditions for convening Marsh (a
firing ruled a pause, or one still undischarged after the next
iteration's audit) are not met.

**The observation that gives the firing its teeth**, in EM's own words:
*"both new instances sit inside the `DISCLAIMER_115` string that MF-10
wrote to fix exactly this class — the correction machinery is now the
place the class recurs."* This is the sixth consecutive cycle at or above
R20's density bar, and the density is now concentrated in the
single-source-of-truth string this program built to stop disclaimer
erosion. **A single source of truth that is never independently
re-derived is a single source of *un-audited* truth.** Iteration 93's
discharge must therefore include a **re-derivation pass over
`DISCLAIMER_115`'s own arithmetic claims**, not merely a correction of
the six lines named here.

**The Iteration-92 PROGRAM-LEVEL criterion-4 firing (Phase 2) remains
OPEN.** Its own entry pre-registered closure by *"Iteration 93's Red Team
final audit"*, and Iteration 92's Red Team correctly declined to close
its own firing. Confirmed from primitives this cycle: **D1 is VERIFIED
PRESENT** (`PANEL.md:153-167`, the "Scope amendment (Director, Iteration
92, 2026-09-05)") — with three defects in it now confirmed and promoted
to Iteration-93 Tier-0 item 0.3; **D2 is VERIFIED AS A RULING** on the
record in three places (`PANEL.md:164-167`, the Phase-2 CHECKPOINT entry,
`PLAN.md`), and **verified as EXECUTED: not yet, and it cannot be until
Iteration 93 runs.** Both firings ride the same R34 closure mechanism.
Marsh is not convened for either.

### 5.4 Director's acceptance

**Red Team's Phase-5 final audit is ACCEPTED IN FULL. No overrides.**
Every item of its §3.1 (the twenty mandatory Result contents), §3.2 (the
LOGBOOK/PLAN corrections and the caveat-registry update), §4 (the
Checkpoint ruling, the R20 tally, the R34 status), §5.1 (the combined
verdict), §5.2 (the verdict-framing ruling on exp-114's entry), §5.3 (the
Reconciled Iteration-93 queue and its twelve numbered declines) and §5.4
is adopted as written. The one item that could not be executed as
literally worded is recorded as such: the "R21: stated here" string and
the six FALSE clauses live in **frozen Phase-4 artifacts**
(`run115.py`, `results.json`), which this close does not edit; they are
corrected in prose here and their deletion is Iteration-93 Tier-1 item
3(v)–(vi).

### 5.5 Combined verdict

# PARTIAL

**T1 escape route: N/A** (unanimous, seven seats). Seats: PHOTONICS
CONFIRM; MATERIALS, ELECTROMAGNETISM, THERMODYNAMICS, QUANTUM OPTICS,
VISION SCIENCE PARTIAL; Red Team overturns PHOTONICS' CONFIRM and files
**PARTIAL**.

**Why not CONFIRM.** The measurement half is CONFIRM-grade without
qualification: every scored statistic reproduces bit-exact from
primitives at six independent seats and again at Red Team's; the
pre-registration is a verified property of the git tree; the MF-12
identity gate is a real absolute gate (10/10); the bench trust suite is
41/41 with its platform named and committed; ABBA worked and its 721.8×
lag reduction was measured; the budget gate branched three times upstream
of spend; R23's First Addendum is discharged from the artifact for the
first time in this program. **The record half fails.** LOGBOOK and PLAN
quoted a superseded session, one figure in sign; six independent R4-class
defects sit in the frozen text (R20 fires); three mandated Phase-2 fixes
and an entire declared deliverable (M8) were persisted and un-narrated;
the quotable bound's scope clause is false against the instrument it
governs and its one constraint-adjacent sentence reports as bounded a
channel that is **unmeasured at ten of twelve cells**; and M3's verdict —
which gates `m6_directional_only` and, through `m3_scored`,
`may_move_logbook_verdict` — does not survive correction by the cycle's
own persisted data on **two independent routes**. In this program the
record is the product. That is PARTIAL.

**Why not RULED-OUT.** Nothing here is ruled out. Every defect is
desk-correctable at zero FDTD cost, no scored verdict reverses, and the
cycle delivered four things the program did not have: the **first
per-step control ever measured on any grid but r=156**; a
matched-protocol, same-session, single-machine `G` that is R33-immune by
construction; the **first bench-native R17/R31 anchor**; and MATERIALS'
seven-cycle fabrication debt written as a quotable, caveat-gated,
arithmetic-reproduced bound. OV-2 — decline the eighth deferral — is
vindicated.

### 5.6 What this cycle may and may not move in exp-114's LOGBOOK entry

**MAY:** add a **forward disclosure** to the Iteration-91 entry (this
program's established practice — never retroactively edit a frozen entry)
recording that exp-114's `G_E = 2.7455057` / `k = 3.4909` is **not
reproduced on a second machine at the same `kappa_ratio`**: the bench
gives `G = 2.2459405` / `k_B = 2.9955462` (scored) and `2.2922399` /
`3.0458713` (session 1, not scored); the two machines sit on **opposite
sides** of `reference_ratio` and **both score CONFIRM** while differing
by **18.20%**, above M6's own **15.295%** transfer bar; M6 reads
**AMBIGUOUS**; and the protocol-matched cloud value `G_E/f = 2.880173`
moves M6 **further** from transfer (`|T−1| = 0.2202`). *(Written into the
Iteration-91 record this close.)*

**MAY NOT:** upgrade exp-114's `CONFIRM-WITH-NAMED-GAPS` to anything
stronger (M5's CONFIRM is a **containment** result on a band 30% wide in
ratio space — wider than the between-machine spread it must survive — and
MF-7(b) pre-registered that a CONFIRM cannot distinguish `k = 3.2053`
from `k = 3.0`; this cycle's central estimate is **0.149%** from 3.0);
remove any of exp-114's named gaps (none was closed here); claim that
`KAPPA_COST_EXPONENT` is a cloud-contention artifact, or that `k = 3.0`
is restored program-wide (`k` was fitted at `kappa_ratio = 2.0`, this
cycle establishes nothing at any other ratio, and the machine and
protocol axes are unseparated); rest on `may_move_logbook_verdict = True`
without the §4.5 anchor disclosure (that boolean is **False** under any
bench-native anchor); or cite the M9 bound as shipped (corrected form
only, §4.3, with the caveat-registry entry updated in the same motion —
done this close). **`KAPPA_COST_EXPONENT = 3.2053` stays in force for the
cost gate, labelled a gate-margin choice.**

### 5.7 The Reconciled Iteration-93 queue

**Tier 0 — governance.**
**0.1** Record the R20 criterion-4 firing (§5.3) as a CHECKPOINT entry —
notification, not a pause, six instances listed, closure condition =
Iteration 93's Red Team audit confirming the §3 discharge list. Marsh not
convened. **0.2** Carry the Iteration-92 **program-level** criterion-4
firing **OPEN** to Iteration 93's audit; D1 verified present, D2 verified
as a ruling, D2's execution is Iteration 93's to demonstrate. **0.3**
Repair D1's three defects: the governance-vs-phenomenon class is assigned
by the **Director in the Iteration entry**, never self-certified by the
proposal; PANEL.md carries a standing **"consecutive governance-class
cycles: N"** counter on the page a fresh seat reads first; VISION's
threshold duty on a governance cycle is stated as discharged by the
DISCLAIMER's constraint-3 N/A sentence **and by nothing else**; the
hardcoded cycle count becomes *"since exp-100 (Iteration 77)"*. **0.4**
Ratify the forward **R17 anchor rule**: where a tolerance/bracket
quantity is venue-dependent, its anchor must come from the venue the run
executes on — the cloud `R_DEG` is retired for bench cycles;
`R_DEG_bench = 0.022961` is the anchor of record, `0.016630` the
disclosed alternative. **0.5** `COST_GATE_TOTAL_S`
wall-clock-vs-compute policy fork — **unchanged, still Marsh's own call**,
carried from Iteration 89; not a discovered defect. **0.6** Ratify or
reject: **a cost/safety gate must bound the CYCLE, not the process**
(§4.8). If ratified it becomes a rule; the code half is Tier-2 item 6.

**Tier 1 — Iteration 93's three items.**
**1.** **[FIXED by D2] VISION SCIENCE's constraint-3 re-score of the
program's only Tier-W/Tier-A citation, through the modernized
`lab/ambient.py`. ELECTROMAGNETISM leads by rotation; VISION pins the
thresholds.** Target: exp-047 / Iteration 24, P-G24-2,
`C_MEASURED = −0.7209` from exp-030 (**not** exp-020's superseded
`−0.686`). **S-A is the positive control, mandatory and first, with HALT
semantics** — and *the failure is the result*: a fifteen-cycle-stale
instrument is a finding, not a wasted slot. **Iteration 93 is a
phenomenon-program cycle, not a governance cycle**: it declares its
escape route as **σ(I)** and records the seven metric rows or states per
row why not — a thirteenth consecutive `NONE` would be wrong on the scope
amendment's own text. P3's pre-registered "36/36 out of calibration"
outcome is flagged in advance as potentially checkpoint-relevant: if it
lands, exp-047's "170× margin" is **withdrawn as un-scoreable** and Tier
W returns to open — a real result at zero FDTD cost, not a failure of the
cycle. **Cost: Iteration 93 must budget REAL FDTD** and project it from a
bench-native per-step rate at the geometry actually run — VISION's S-A is
the exp-030 `r=78`-native ±35° configuration, for which **no bench rate
exists** (the bench has measured only r=156 and r=234 at cpl=25:
`3 × 8000 × 0.0493975 = 1185.5 s` and `3 × 12000 × 0.1109387 =
3993.8 s`). Take a short r=78 control burst first, or project explicitly
conservatively and say so.
**2.** **`lab/sections.py`'s angle-convention correction, a positive
control for it, and a re-audit of every angular claim in the record.**
Fix the docstring at `:209-210` and `:223-224` to `0° = +x = forward /
downstream`, `±180° = −x = backward, toward the source and the observer`,
with the one-line justification. **Arm a positive control in the trust
suite**: assert the argmax bin of a `graded_black_shell` pattern lies
within ±30° of 0°. Then grep and re-audit every
forward/backward/observer-return/backscatter angular-sector claim in
`experiments/` against the corrected convention, and annotate
`experiments/017-.../NOTES.md:22` with a dated correction rather than
editing history. **This must land FIRST**: it is a live R18-class defect
in shared `lab/` machinery, it sits under PANEL.md's constraint-2 row,
and both item 1's angular scoring and item 3's re-issued bound quote the
phrase "observer-return hemisphere."
**3.** **The zero-FDTD re-issue of the fabrication-tolerance bound at
full scope, bundled with the complete R20/R21 discharge.** (i) Recompute
the per-bin channel at **all six** margins and report **median + p90 +
max + SNR-at-max + absolute `|Δ|`**, not max alone; strike "only the
margin-32 array is persisted"; correct "330× looser". (ii) Report the
observer-facing face as **UNMEASURED at 10/12 cells**. (iii) Correct the
MP-5 forward conditional to **invariant, not strengthened**, and restate
MF-15's counterweight as a **strict loss on two axes**. (iv) Publish the
per-bin↔bound reconciliation and MF-1's 3λ row. (v) Fix the six
shipped-FALSE items and the R18 gate-scope statements. (vi) Land the
corrected headline verbatim in `NOTES.md § Phase 4 — Results` *(done this
close)* and delete the "R21: stated here" self-certification. (vii)
Update the caveat entry's required phrase and its `required_sites`
*(done this close for the registry half; `results.json` is added when the
bound is re-issued into it)*. (viii) Replace `favoured` with a
rejection-gated label, and add the single boolean
`machine_transfer_caveat = (m6_verdict != "TRANSFERS")` gating
`may_move_logbook_verdict` and the model comparison. (ix) Persist the
bench-native anchors, the per-grid duration decomposition, and
`sensitivity_session1_across_reboot_DO_NOT_SCORE`. **Item 3 rides as a
labelled rider with no falsifiable question of its own. If Iteration 93
can carry only two items, item 3 is what drops — and it drops as a
numbered decline (R25), not silently.**

**Tier 2 — cheap riders.** **4.** QUANTUM's T18 primary-source probe,
**STAGE A ONLY** (~10 min, zero FDTD): fetch a primary source whose
content is already known from the repo's own record and confirm the
returned text contains a figure the record already quotes — *a probe that
can only return "blocked" is not a probe.* Persist the raw result either
way, so T18's status becomes a **measured** fact for the first time in 78
iterations. (A tool listed in a session roster is not a tool heard from.)
**5.** Persist the remaining not-scored sensitivities not covered by
3(ix): `G_E/f = 2.880173` / `|T−1| = 0.2202`; EM's `U156/empty`
substitution (+0.412%, `k_B → 3.005696`, every verdict unchanged);
PHOTONICS' F10 "no drift systematic resolved at this precision."
**6.** THERMO's **cycle-scoped spend ledger** — a committed
`data/spend.json` accumulating `(session, calls, Sim.run seconds,
elapsed)` across invocations; `build_result_text()` states the cycle
total and names every session including abandoned ones; the budget gate
seeds from it. **7.** **A contention instrument that can produce the
reading meaning "bad"**: run a CPU-bound **Windows-side** process and
confirm the recorded number moves. If WSL2 `loadavg` cannot move (it
should not), record that as a measured fact and add a host-side sample,
or state in the disclaimer that the exclusive-use evidence is
**VM-scoped and blind to the host**. Sample `cpu MHz` per reading rather
than once at idle — again with a positive control, since WSL2 may report
a static value, in which case the honest output is "not measurable here,"
not a constant. **8.** **Add a common-mode drift channel** the current
design cannot see: the per-scene sub-timings already persisted give three
replicate pairs per grid at zero cost; making that the null channel is
the positive control `d_rep` structurally cannot be.

**Tier 3 — bigger builds.** **9.** *(Iteration-94 Tier-1 candidate, and
Red Team's recommendation for it)* **EM's T1 passivity/causality
ledger** — what each of T1's four named escape routes *requires*, in
parameters: for σ(I), the required contrast as a ratio of two irradiances
(both pinned by item 1), converted to required `dσ/dI` and `I_th`, with
the **sign check against passivity** (a passive saturable medium
*bleaches*; the phenomenon demands reverse-saturable absorption) and a
bound on the required `β` or `σ_ex/σ_gs`; then σ(x,t) with its switching
energy, angular selectivity as a reciprocity argument against the beam's
own divergence, and sub-threshold operation. Zero FDTD. **If the σ(I)
sign-and-magnitude argument closes, that is Checkpoint criterion 2 — the
program's own named honest alternative product, never once reached.**
Gated on item 1. **10.** Merged: **VISION's G-variance decomposition + a
third grid point + a deliberate contention lever** — `r = 78/117/156/234`
at fixed cpl=25 in one ABBA session (separates absolute `N` from
`kappa_ratio` and makes `p = aN² + bN + c` exactly determined), a third
runner's six readings, and one deliberate concurrent-load reading that
converts session 1's accidental point into a calibration of
`dG/d(slowdown)`. Deliverable: a persisted three-level variance
decomposition (within-session 1.46% · between-session 2.06–2.81% ·
between-machine 18.20%) and a pre-registered test of whether **M5's ±15%
CONFIRM band is wider than the machine spread it must survive** — if it
is, the band must be re-derived from measured machine variance rather
than from R28's founding miss. **11.** MATERIALS' **observer-return
channel in ABSOLUTE units against the camera floor**
(`emit.observer_record`, stage 6) — two `Sim.run()` calls at the cheapest
geometry; **gated on item 2**, pre-register the floor comparison and its
units before the run (R9). **12.** EM's **r=312 / cpl=25 / +168.75° leg
— now UNBLOCKED**, priced from bench-native rates for the first time:
`1185.5 s + 3993.8 s = 5179.3 s`, inside `COST_GATE_TOTAL_S = 10800` with
the 1.10 margin; R31 and R33 satisfied by construction. **13.** THERMO's
**r=234 within-reading ramp** (~6 min): permute scene order, five
back-to-back single-scene bursts, per-scene `cpu MHz` and
`/proc/vmstat` compaction counters under item 7's positive control.
**14.** MATERIALS' **channel/resolution de-confound** — the per-bin
channel at cpl=25 or the aggregate channels at cpl=20, one radius;
**must follow item 3**, so the re-issued bound defines which figure the
new resolution point must reproduce (the **median**, not the tail max).
**15.** QUANTUM's **Stage B** (rigorous primary-source RSA/TPA/
third-class realizability check), gated on item 4 returning clear.
**16.** QUANTUM's **first bench-native σ(I) two-intensity run** — gated
on items 9 and 15, and it **fires Checkpoint criterion 3**: it must be
proposed as such, with a new trust-suite stage carrying an absolute
identity gate (`I → 0` reproduces the committed linear article
bit-exactly). **17.** `R2_SMOOTH_THRESHOLD = 0.90` re-derivation — now in
its **eighth** consecutive cycle, named so it is not silently dropped.
**18.** The `box_dev` **differential floor at r=234** — still the only
radius with **no** differential floor on file, and now load-bearing on
the shipped bound.

**Numbered declines (R25).**
**D-1.** The **MP-5 thickness re-spec as a forward direction — DECLINED**:
MP-5 holds `τ_true` fixed, so thickening buys **zero** backing freedom
while costing thermal margin 3.79× → 1.35× and enlarging a silhouette
that already fails constraint 3. Strictly worse on every axis.
**D-2.** Retiring `KAPPA_COST_EXPONENT = 3.2053` for the bench's
`2.9955` — **DECLINED for the gate**: 3.2053 is the conservative
exponent; adopting 2.9955 makes the gate anti-conservative on a contended
machine, which is R28's founding failure mode running backwards.
**D-3.** Re-scoring M3 against a bench-native anchor **as a SCORED
verdict — DECLINED**: R17 was satisfied at freeze; post-hoc estimator
switching is what Iteration 1 ruled out. Disclosed forward as a
NOT-scored sensitivity (§4.5) and as Tier-0 0.4.
**D-4.** Folding session 1's sustained pair into `G_sustained` as a
scored operand — **DECLINED**: cross-session, and its `U234` is a ramp
into a fault. It enters as `..._DO_NOT_SCORE` only; admitting it changes
no verdict and flips no boolean.
**D-5.** Scoring `sensitivity_v2_with_measured_G` — **DECLINED again**
(OV-1), now **empirically** reinforced: M6 returned AMBIGUOUS, so the
machine-independence the construction presumes is measured and
unresolved.
**D-6.** THERMO's discard-first-1000-steps protocol — **remains
DECLINED** (OV-3); THERMO withdrew the request itself at Phase 5.
**D-7.** Promoting `σ_ext_cross` to a third energy-ledger channel —
**remains DECLINED** (OV-4), refuted by EM's own A7 and accepted by EM.
**D-8.** QUANTUM's `τ_true ∈ (6.6071, 8.2588)` concavity interval —
**remains DECLINED** (OV-5), refuted numerically and accepted by QUANTUM.
**D-9.** A **sixteenth** consecutive T28 instrument cycle as Iteration
93's falsifiable heart — **DECLINED**. Items 2 and 3 ride as labelled
riders; item 1 is the cycle's heart.
**D-10.** QUANTUM's Stage B as a *scheduled* Iteration-93 item —
**DECLINED as un-schedulable** before Stage A returns.
**D-11.** EM's "zero-FDTD if exp-100's captures are committed" branch for
item 1 — **DECLINED as unavailable**: verified from primitives,
`experiments/100-.../` has **no** `artifacts/` directory.
**D-12.** Presenting the DRAM-bandwidth mechanism, or the
contention-artifact conclusion, **as evidence — DECLINED**: the mechanism
ships **NOT-SCORED** (post-hoc, one ratio, three unknowns, one equation —
R5/R30); the causal conclusion is refuted at the measured magnitude.

### 5.8 One thing on the record beyond the rules

This cycle built the best-instrumented wall-time measurement this program
has ever taken, and then wrote it up in a document that was false in six
places. **Both halves are the finding.** The machinery that produced the
six defects is the **correction machinery itself** — a
single-source-of-truth disclaimer string, a mandatory-fix docket, a
reproduction gate — each built to stop exactly this class and each now
the place the class lives. `lab/ARTIFACTS.md`'s invariant, *a silent gate
and an absent gate produce identical observations*, gained two siblings
this cycle: VISION's false-positive twin — *a wrong computation that
agrees with the right one is indistinguishable from correctness by
verdict alone* — and R20's, from firing inside `DISCLAIMER_115`: **a
single source of truth that is never independently re-derived is a single
source of un-audited truth.**
