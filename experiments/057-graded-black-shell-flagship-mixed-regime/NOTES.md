# exp-057 — Closing the Flagship's `H_CONV`/`MASS_KG`/`w_on`-Area Gap

Panel Iteration 34. Lead: **THERMODYNAMICS**, by **UNCONDITIONAL LOCK,
breaking rotation** — Red Team's Iteration-33 Phase-5 audit granted
THERMODYNAMICS' own escalation request: `graded_black_shell_flagship`'s
re-run through the corrected `mixed_length_scale_regime` had been deferred
three times (ranked #1 at Iteration 31's close, deferred at 32, deferred
again at 33), meeting the unconditional-lock bar Red Team pre-declared in
writing at Iteration 32's close. This item is NOT competitively chosen.

Full cycle: Phase 1 proposal (THERMODYNAMICS) → five blind parallel
critiques (PHOTONICS, MATERIALS, ELECTROMAGNETISM, QUANTUM OPTICS, VISION
SCIENCE — all support-with-changes; VISION's critique agent was terminated
mid-response by an upstream `[bio]`-tagged content-policy false positive,
~95% complete, ruled usable by Red Team, see Program note below) → Red
Team last with everything (also interrupted by the identical false
positive, ~98% complete, independently re-verified and ruled usable) →
this Phase-3 synthesis. Full verbatim record: `LOGBOOK.md`, Iteration 34.

## Hypothesis

Not a mechanism proposal — a sidecar-cycle correction, same register as
Iterations 20/22/25/27/31. `graded_black_shell_flagship` — this program's
headline result, and its thinnest thermal-detectability margin (~6.04×) —
is the last uncorrected instance of the bug exp-054 (Iteration 31)
resolved for two other articles: `h_eff`, thermal mass, and radiating/
convecting area computed from a diffraction-inflated optical length
(`w_on`) instead of the object's real geometric length (`r_out`). It is a
**worse** instance than either corrected article: unlike the ON-endpoint
and dose-accumulation articles, which had `H_CONV` already corrected once
(exp-045) before exp-054's own length-scale fix, the flagship still
carries `H_CONV=5.0 W/(m²K)` (a macroscopic natural-convection placeholder,
never replaced) and a hardcoded `MASS_KG=1.0e-15 kg`, untethered to any
geometric length at all.

This cycle applies `lab.thermo_sidecar.mixed_length_scale_regime` to the
flagship exactly as exp-054's own Part A applied it to the ON-endpoint:
`p_abs_w` stays on the already-measured, already-calibrated `w_on`-based
optical quantity (untouched); `h_eff`, thermal mass, and radiating area
are re-derived from `r_out` alone (78 cells × 30nm).

## Setup

| Parameter | Value | Source |
|---|---|---|
| `p_abs_w` | `1.7409069740390205e-12` W | `experiments/043-.../results.json::graded_black_shell_flagship.p_abs_w_central` — established via `absorbed_power_established_ratio` (`sigma_ext_cells=240.0073740162445`, `ratio_abs_ext=0.51`). **NOT re-derived this cycle**, pinned by a same-shift regression assert (below). |
| `l_geometric_m` | `2.34e-6` m (`=78 cells × 30e-9 m`) | exp-054's own `R_OUT_M` convention; identical `R_OUT_CELLS=78` to the flagship's own bench radius |
| `k_air` | `0.026` W/(m·K) | textbook room-temp, exp-045/exp-054 |
| `density_kg_m3`, `c_p_j_kgk` | `2330.0` kg/m³, `700.0` J/(kg·K) | silicon — **ASSUMED, provenance terminates unsourced (T18)**, `REALIZABILITY_MEMO.md`'s standing downgrade |
| `emissivity` | `0.9` | exp-043's own original value, unchanged |
| `t_ambient_k` | `293.15` K | standard |
| NETD band | `(0.020, 0.050)` K | `experiments/043-.../results.json::p_d7_4_netd` |

**Zero new FDTD calls.** Pure desk/analytic re-derivation from an
already-committed bench measurement, reusing `lab.thermo_sidecar.
mixed_length_scale_regime` and `netd_disposition` — already promoted,
trust-suite-gated (stage 18) reusable code from exp-054, no new engine
solves.

## Phase 3 — accepted / overridden (Director's synthesis)

Red Team's verdict: **proceed-with-mandatory-fixes**, 4 numbered attacks
(no `[unfalsifiable]`/`[inexpressible]`/constraint-#N findings — a pure
NETD/instrument-threshold correction, explicitly disclaimed against
constraints 3/4 at the code level), 6-item docket. **All 6 items ACCEPTED
IN FULL.** Full record:

1. **[EM, load-bearing] The Phase-1 draft's mechanism narrative
   ("h_eff jump ~2200× dominates ~9.47× area shrink") is WRONG attribution
   even though the final ~116× number is right — the naive two-factor
   product is ≈235×, not the real 115.76×.** **Fixed:** the mechanism is
   now code-verified and correctly attributed to a THIRD term neither
   factor captures alone — the radiative term's SHARE of `dP/dT`, which is
   co-equal with `H_CONV=5.0` in the old chain (50.70%/49.30% split,
   `results.json::mechanism_decomposition_code_verified`) and collapses to
   0.046% of `dP/dT` in the new chain (area shrinks 9.47× for both terms,
   but `h_eff` swamps radiation entirely). This dilution — not a clean
   product — is what halves the naive 234.71× down to the real 115.757×
   (both figures reproduced in `run.py`, computed from the actual chain,
   not hand-typed).
2. **[EM] Kn/slip-flow citation drift — "68nm/~0.029" was a generic round
   figure, not this program's own sourced mean free path.** **Fixed:**
   `Kn = LAMBDA_AIR_M(65.7nm, exp-046's own sourced constant)/r_out(2.34µm)
   = 0.02808`, matching exp-046's own committed B4 result and exp-054's own
   citation exactly. Slip-flow regime (0.01<Kn<0.1), not strict continuum.
   First-order slip correction (−5.3168%, exp-046 B4's own value, identical
   `r_out` regime, reused not re-derived) drops the margin to **662.09×**
   — no verdict risk (classification stays UNDETECTABLE by 2+ orders of
   magnitude either way).
3. **[PHOTONICS/QUANTUM, converged independently] The `w_on`-vs-`r_out`
   diffraction-inflation assumption underlying `p_abs_w`'s own area
   convention is ASSERTED, NOT INDEPENDENTLY BOUNDED — exp-054's own
   NOTES.md flagged this, queuing a `Q_ext(x)` closed-form check (ranked
   #4, proposed at Iteration 31's close) that has now gone THREE full
   deferrals (32, 33, 34 — the proposing cycle, 31, does not itself count
   as a deferral, per this program's own T23/`h_eff` convention; a Phase-5
   PHOTONICS re-read of this file mis-stated this as "31, 32, 33" — a
   citation slip corrected here, no substance change) without being run —
   as of this cycle's own Phase-5 close, this hits the same 3-deferral
   threshold that triggered `graded_black_shell_flagship`'s own
   unconditional lock, and Red Team's Iteration-34 audit has now LOCKED
   `Q_ext(x)` for a future iteration on that basis (see Next).** **Fixed:**
   the caveat is restored verbatim (`DIFFRACTION_INFLATION_CAVEAT`,
   `run.py`/`results.json`), explicitly cross-referencing the still-open
   `Q_ext(x)` check. **Non-load-bearing, with a Red-Team-corrected bound**:
   `absorbed_power_established_ratio`'s own `iso_xsec_sq` convention
   SQUARES the linear width to get an area (`area_m2 = width_m**2`), so
   the correct area-domain bound implied by the ~1.54× LINEAR excess is
   **~2.37× (1.54²)**, not the originally-stated, arithmetically-wrong
   "~1.5–2×" — even that full 2.37× correction only RAISES the margin to
   **~1655×** (699.27×2.367≈1655.18×, matching Iteration 36/exp-059's own
   code-verified `margin_slip_corrected`-style figure, `margin_ceiling`),
   in the SAFE direction (a smaller assumed area only increases the
   margin). **Iteration-37 erratum (2026-08-22, THERMODYNAMICS' Phase-5
   catch at exp-059):** this entry originally read "drops the margin only
   to ~295×" — self-contradictory with the very next clause ("a smaller
   assumed area only increases the margin"), since 295× < 699.27× is a
   decrease. The error was computing 699.27/2.367≈295.4 (division)
   instead of 699.27×2.367≈1655.2 (multiplication). Corrected here; no
   scored classification changes either way (still 2+ orders of magnitude
   clear of NETD-lo).
4. **[MATERIALS, two Red-Team-corrected citations] `mass_kg`/`tau_thermal_s`
   silently assume a 100%-fill SOLID disk of radius `r_out`, but
   `graded_black_shell_flagship`'s real construction is an ANNULUS —
   `pec_disk(r=30)` then `graded_black_shell(r_in=30, r_out=78)`
   (`experiments/020-ambient-baseline/run.py` lines 44–45 — **NOT**
   `design_geometry.py` as originally cited in this document and in
   `run.py`'s own comments; Red Team's Phase-5 audit caught this file
   citation was wrong on all four original loci — `design_geometry.py` is
   a pure ray-trace/coverage script with zero materials calls, and has
   been corrected throughout) — not a solid disk (solid only if `r_in=0`,
   per `graded_black_shell`'s own docstring).** MATERIALS' own cited
   alternative core composition ("possibly bare vacuum per exp-027 Cell
   B") was itself wrong for this specific article — **corrected here**:
   the flagship's core (r<30, ~15% of the disk area) is unambiguously a
   **PEC disk**, per exp-020's own build. **THIRD CONSECUTIVE CITATION
   CYCLE of this exact defect** (Iteration 20/exp-043 → Iteration 31/
   exp-054 → Iteration 34/this cycle), now explicitly tracked as such
   (`SHELL_VS_SOLID_MASS_CAVEAT`) — **distinct from, and NOT to be
   conflated with, the SEPARATE silicon material-provenance chain**
   (ρ=2330 kg/m³ etc.), whose correct lineage is **exp-045/046
   (Iteration 22/23) → 31 → 34**, not "Iteration 20" — grepped directly:
   `experiments/043-.../run.py`/`NOTES.md` contain zero mentions of
   "silicon"/"2330"; Iteration 20's `MASS_KG=1.0e-15` was an unidentified
   material placeholder, not silicon (a conflation in this document's own
   original Realizability-bound draft, caught and corrected by Red Team's
   Phase-5 audit — see Realizability bound, below). **Confirmed
   non-load-bearing**: `mixed_length_scale_regime`'s own `dt_ss_full_K`
   formula has NO `mass_kg` term (steady-state has no mass dependence) —
   verified directly against `lab/thermo_sidecar.py`'s source,
   independently by both MATERIALS and Red Team. `mass_kg`/`tau_thermal_s`
   land in `results.json` as unscored byproducts; no future citer of
   either figure should assume a solid-disk reading of a shell object.
5. **[VISION, confirmed by Red Team against exp-054's own binding
   precedent — and against the LIVE table, not just the promise] The NETD
   disclaimer was stated once, generically, in Idealizations — not
   attached per-row to the predicted-outcomes table, unlike exp-054's own
   P-054-2/4/5, which each individually restate it (Iteration 20's Red
   Team attack 7, "elevated to load-bearing").** **Fixed, completely this
   time**: Red Team's own audit checked the Phase-3 draft's claim
   ("propagated to every row") against the actual table and found only 2
   of 5 margin/classification-bearing rows (P-057-2, P-057-3) carried it —
   P-057-1 (`dt_ss_full_K`, explicitly named in the original promise) did
   not, and P-057-4/P-057-6 (added beyond the three originally named)
   inherited nothing. The Results table below now carries the disclaimer
   on every row that states a margin, classification, or the ΔT feeding
   them (P-057-1, 2, 3, 4, 6). `results.json`'s `old_chain`,
   `knudsen_slip_flow`, and `comparison_to_standing_figure` sub-objects
   each now carry their own `netd_disclaimer` field (previously only the
   file-level sibling key covered them — invisible to a consumer
   extracting just that sub-object). `run.py`'s own print block now prints
   `NETD_DISCLAIMER` before any numeric line — closing an EXACT RECURRENCE
   of a finding VISION SCIENCE made against this identical code pattern at
   Iteration 31 Phase 5, never structurally fixed for ad hoc dicts built
   directly in an experiment's own `run.py` (only `thermo_sidecar.py`'s
   own helper-function return dicts got the Iteration-31 fix). Flagged as
   a standing structural gap for a future cycle (see Next): the
   Iteration-31 fix should be extended to cover this recurring pattern
   generally, not patched per-cycle.
6. **[Red Team, new this cycle] No same-shift regression assertion existed
   pinning this cycle's own inputs against `experiments/043-.../
   results.json`'s committed values — Iteration-31 Phase-5 THERMODYNAMICS
   had already pre-flagged this exact gap ("stage 18 cannot catch this...
   now shown non-hypothetical") for a future flagship rerun, and this
   cycle is that rerun.** **Fixed:** `run.py` asserts `p_abs_w ==
   1.7409069740390205e-12` (to float precision) and `dt_ss_full_K` against
   its own Phase-3-committed regression anchor (`2.8601275372385233e-05`
   K, tight tolerance) before writing any result — a script-level
   self-check, not a new trust-suite stage (no new machinery required
   under PANEL.md's own house rule).

## T1 escape route

**NONE.** Pure NETD/instrument-threshold sidecar correction — no material
or mechanism change, no σ(I)/σ(x,t)/coherent apparatus, nothing new
proposed. `netd_disposition`'s own returned dict structurally embeds the
"NETD is not a human perceptual threshold" disclaimer as a JSON field, so
it travels with the number regardless of narrative discipline.

## Realizability bound

Not applicable in the constraint-1/2/3/4 sense — no new material or
mechanism is proposed. The silicon material-provenance figure this cycle
reuses (ρ=2330 kg/m³, c_p=700 J/(kg·K)) is, per `REALIZABILITY_MEMO.md`'s
own standing downgrade, **ASSUMED, not independently sourced** (T18) —
this is its third consecutive citation cycle without a primary-source fix,
with lineage **exp-045/046 (Iteration 22/23) → exp-054 (Iteration 31) →
this cycle (Iteration 34)** — **corrected here, per Red Team's Phase-5
audit**: an earlier draft of this section wrongly named "Iteration 20" as
the first citation; Iteration 20/exp-043's own `MASS_KG=1.0e-15` was an
unidentified-material hardcoded placeholder (grep-confirmed: zero mentions
of "silicon"/"2330" anywhere in `experiments/043-.../`), not silicon —
that is a SEPARATE, correctly-stated defect (the shell-vs-solid mass
model, whose own lineage genuinely IS Iteration 20 → 31 → 34, see Phase-3
fix 4 above). The two chains were conflated in this section's own
first-draft text; kept distinct here. Carried forward unresolved, not
addressed this cycle (out of scope: this cycle corrects the length-scale
chain, not the material citation).

## Predictions — committed before this cycle's `run.py`

**P-057-1 (corrected `dt_ss_full_K`).** Predicted band **[2.5×10⁻⁵,
3.2×10⁻⁵] K** (central estimate, verified by direct code execution before
freeze: `2.8601275372385233e-05` K). Disposition: in band → CONFIRMED.

**P-057-2 (corrected NETD-lo margin, `0.020/dt_ss_full_K`).** Predicted
band **[600×, 800×]** (central `699.27×`). Disposition: in band →
CONFIRMED — **NETD is an instrument/detector threshold, not a human
perceptual one; this figure does NOT bear on constraint-3/4's human-eye
verdict.**

**P-057-3 (classification).** Predicted **UNDETECTABLE**. Disposition:
exact match → CONFIRMED — **again, an instrument-threshold classification,
not a constraint-3 finding.**

**P-057-4 (direction, relative to the standing 6.04× figure).** Predicted
**GROWS** (opposite exp-054's own ~3.03× shrink for its two corrected
articles), because the flagship never had `H_CONV` corrected even once —
this cycle applies two corrections (placeholder-`H_CONV` AND
`w_on`-vs-`r_out` length) in one step, and the placeholder-replacement
effect (a ~2200× per-area conductance-coefficient jump, diluted by the
radiative term's collapsing share) dominates. Falsification condition,
pre-registered: margin landing below ~50× (area-shrink effect dominating
instead) or below 1× (classification flip) would be a real, reportable
surprise. Disposition: see Results.

**P-057-5 (mechanism decomposition, code-verified, not hand-typed).**
Predicted: `dp_dt_ratio_new_over_old` computed directly from
`mixed_length_scale_regime`'s own returned values, NOT asserted from a
naive product of the two headline ratios (Red Team mandatory fix 1).
Disposition: see Results.

**P-057-6 (Kn/slip-flow disclosure).** Predicted: `Kn ≈ 0.028` (exp-046's
own sourced regime, identical `r_out`), slip-corrected margin still ≫1×
(no verdict risk). Disposition: see Results.

## Idealizations

Silicon material provenance reused verbatim from exp-054 — **ASSUMED,
provenance terminates unsourced (T18)**, third consecutive citation cycle.
Bench-scale, not witness-scale (T8/T13's near-field→witness bridge stays
unresolved, unaddressed here). Lumped-capacitance cube-shaped thermal mass,
100%-fill crystalline assumption — **confirmed non-load-bearing** for this
cycle's scored predictions (no mass term in `dt_ss_full_K`), but a real,
third-cycle-unresolved defect for any future citer of `mass_kg`/
`tau_thermal_s`. `area_m2 = l_geometric_m²` (iso-sq convention, only the
LENGTH differs from the old `w_on`-based area, not claimed more physically
"real"). Nu=2 quiescent-gas conduction limit, slip-flow correction
disclosed but not folded into the headline (Kn≈0.028, −5.3% conductance,
margin 662× either way). Steady-state graybody radiative linearization
about `T_ambient`. Achromatic, 600nm bench point only. `p_abs_w` itself is
measurement-locked, not re-derived — and inherits the still-open,
three-cycle-unresolved `w_on`-vs-`r_out` diffraction-inflation question
(non-load-bearing here). **NETD is an instrument/detector threshold, not a
human perceptual one** — no finding in this cycle bears on constraint-3/4's
human-eye verdict, stated at every row per Red Team's own mandatory fix 5.

## Program note — the `[bio]` content-policy interruption pattern

Two of six Phase-2 agents this cycle (VISION SCIENCE's critique, Red
Team's audit) were independently terminated mid-response by the identical
upstream `[bio]`-tagged content-policy false positive that blocked
Iteration 30's build twice. Unlike Iteration 30 (zero delivered content,
reproduced exactly on the same task twice), both occurrences here
delivered ~95–98% of a coherent, independently-verifiable critique before
cutting off — a different signature (late-stage truncation vs. immediate
termination). Red Team's own audit ruled both usable as Phase-2 input
(every substantive claim independently re-verified against source
regardless) and ruled this does not itself warrant fresh escalation beyond
Iteration 30's already-on-record, already-notified blocker — a milder,
differently-shaped data point in the same ongoing pattern, worth
pattern-tracking (this note; LOGBOOK.md Iteration 34) not a fresh
Checkpoint. Recorded here per that ruling.

## Results

Zero new FDTD calls. Full data: `results.json`.

| Prediction | Predicted | Measured | Verdict |
|---|---|---|---|
| P-057-1 (`dt_ss_full_K`) | [2.5e-5, 3.2e-5] K | **2.8601275372385233e-05 K** — feeds every downstream margin; NETD is an instrument threshold, not human-perceptual, does NOT bear on constraint-3/4's verdict | **CONFIRMED** |
| P-057-2 (NETD-lo margin) | [600×, 800×] | **699.27×** — instrument-threshold reading, NOT a constraint-3 finding | **CONFIRMED** |
| P-057-3 (classification) | UNDETECTABLE | **UNDETECTABLE** — instrument-threshold classification, NOT a constraint-3 finding | **CONFIRMED** |
| P-057-4 (direction) | GROWS, not below ~50×/1× | **GROWS to 699.27×, ~115.76× larger than the standing 6.04× figure** — instrument-threshold margins, NOT a constraint-3 finding | **CONFIRMED** — well clear of the falsification thresholds |
| P-057-5 (mechanism, code-verified) | computed directly, not hand-typed | `dp_dt_ratio=115.757×` (real); naive two-factor product `=234.71×` (WRONG, do not cite) — the gap is the radiative term's share collapsing from 50.70% to 0.046% of `dP/dT` | **CONFIRMED** — matches Red Team's independent re-derivation exactly |
| P-057-6 (Kn/slip-flow) | Kn≈0.028, margin ≫1× | **Kn=0.02808, slip-corrected margin=662.09×** — instrument-threshold margin, NOT a constraint-3 finding | **CONFIRMED** — matches Red Team's independent recomputation (≈662.1×) exactly |

### Headline (for LOGBOOK)

**This is a bench-scale, instrument-detector-threshold correction — NETD
is not a human perceptual measure, and no finding here bears on
constraint-3/4's human-eye verdict.** `graded_black_shell_flagship`'s
thermal-detectability margin, previously the program's single thinnest
(~6.04×, using a chain that had never had its `H_CONV=5.0` placeholder
replaced, unlike two other articles already corrected at Iteration 31),
corrects to **699.27×** — UNDETECTABLE by a wide margin, ~116× LARGER than
the standing figure, the OPPOSITE direction from exp-054's own ~3.03×
SHRINK for its two corrected articles. The direction flip is now
mechanistically understood and code-verified, not asserted: the old
chain's `H_CONV=5.0` placeholder and its radiative term were co-equal
contributors to heat loss (50.70%/49.30% split); the corrected chain's
physically-derived `h_eff=k_air/r_out≈11,111 W/(m²K)` (gas-phase
conduction at micron scale) swamps the radiative term entirely (0.046%
share), and this — not a clean two-factor product of the headline
ratios, a wrong story the Phase-1 draft told even though its final number
was right — is what produces the ~116× conductance jump. A first-order
slip-flow correction (Kn≈0.028, exp-046's own established regime) still
leaves the margin at 662× — no verdict risk under any disclosed idealization.
Two real, non-load-bearing defects were tracked, not fixed, this cycle: the
`w_on`-vs-`r_out` diffraction-inflation assumption underlying `p_abs_w`
itself remains asserted-not-bounded (`Q_ext(x)`, unrun for a third
consecutive cycle), and the lumped-mass model's 100%-fill-solid assumption
is now a third-consecutive-citation-cycle-unresolved mismatch against the
article's real annulus construction (confirmed non-load-bearing: no mass
term in the scored quantity). This closes this program's own three-
deferral-triggered LOCKED item cleanly (`h_eff`'s own lock, by contrast,
fired at five deferrals — a longer chain; "three-deferral" names this
item's own trigger count, not a claim to program-history primacy).

## Next (pre-registered, for Phase 5)

**LOCKED for Iteration 35, unconditional (Red Team's Iteration-34 Phase-5
ruling)**: Iteration 33's own pre-registered condition — "if QUANTUM's
phase-variance redesign is not built at Iteration 34, it becomes a LOCKED,
unconditional, non-competing trigger for Iteration 35" — has fired.
Iteration 34 was entirely consumed by this cycle's own, separately-LOCKED
flagship item and did not touch QUANTUM's redesign; the condition's own
language ("non-competing trigger") fires on the simple fact of
non-construction, independent of why. **QUANTUM's phase-variance redesign
leads Iteration 35.**

**LOCKED for a future iteration, unconditional (Red Team's Iteration-34
Phase-5 ruling, new this cycle)**: (1) **The `Q_ext(x)` closed-form check**
bounding `w_on`'s diffraction excess over `r_out` — now unrun for THREE
full deferrals (32, 33, 34; the proposing cycle, 31, does not itself
count, per this program's own T23/`h_eff` convention) — the same
3-deferral threshold that triggered this cycle's own lock. Red Team ruled
this is not "approaching" the bar, it already meets it, and pre-declared
the lock now rather than waiting for a retroactive discovery (as happened
with `h_eff`). **Scheduling note**: since QUANTUM's redesign also leads
Iteration 35, `Q_ext(x)` becomes Iteration 36's LOCKED item unless
Iteration 35's own Director finds capacity to fold it in as a genuine
zero-marginal-cost desk rider (it is itself zero-new-FDTD) — worth
checking before deferring a fourth time. (2) Resolve the shell-vs-solid
mass mismatch properly (parameterize `lumped_cube_mass_kg`/
`mixed_length_scale_regime` for a two-region — PEC core + shell — thermal
mass, or explicitly bound the error this simplification introduces) —
third-consecutive-cycle carried item, still non-load-bearing today but a
real, growing debt (a live landmine for the first future transient/
`tau_thermal_s`-dependent prediction off this chain, per THERMODYNAMICS'
own Phase-5 framing). (3) Promote `coupled_segment_general` into a real
trust-suite stage with an RK4 cross-check (exp-054's own carried item,
still unbuilt). (4) `graded_black_shell_flagship`'s
own re-run across the standard 450/600/750nm sweep, reusing already-
committed per-λ data, zero new FDTD (exp-054's own carried item). (5) The
remaining competitive queue behind the two LOCKED items above:
R3-on-loaded-legs for exp-056's own off_pass/off_bracket articles;
P-VIS-5's angle-quantization formula; MATERIALS' literature check
(zero-FDTD, deferred since Iteration 29, now six cycles running — itself
approaching this program's own escalation pattern).

**Phase 5 outcome:** six fresh seats + Red Team audit read these results —
**unanimous PROMISING, 6-for-6** (PHOTONICS, MATERIALS, ELECTROMAGNETISM,
THERMODYNAMICS, QUANTUM OPTICS, VISION SCIENCE) — the third unanimous
panel-era verdict, Red Team's final audit adopting the raw seat count
without override. Six mandatory same-shift fixes required and applied
above: two citation corrections (MATERIALS' wrong-file citation, corrected
throughout; the silicon-provenance chain, corrected to exp-045/046→31→34,
distinguished from the separate, correctly-stated shell-vs-solid-mass
chain); one arithmetic correction (PHOTONICS' diffraction-inflation bound,
~1.5–2× → the correctly-derived ~2.37×, margin ~1655× not stated —
itself corrected from an erroneous "~295×" at Iteration 37, see above);
one
cycle-count reconciliation (`Q_ext(x)`: three deferrals, 32/33/34, not
four — the proposing cycle does not itself count); full disclaimer
propagation (VISION's finding, completed on all five margin/classification
-bearing rows plus three `results.json` sub-objects plus `run.py`'s print
block, closing an exact recurrence of an Iteration-31 finding). **Two new
unconditional LOCKs issued this cycle's own Phase-5 close**: QUANTUM's
phase-variance redesign for Iteration 35 (Iteration 33's own pre-
registered condition fired) and `Q_ext(x)`'s closed-form check for a
future iteration (newly met its own 3-deferral bar, declared now rather
than awaiting a retroactive discovery). All five Checkpoint criteria
checked explicitly: **none fire** — criterion 4 scrutinized hardest given
this cycle's own density of findings (two citation errors, one arithmetic
imprecision, one cycle-count inconsistency, one disclaimer-propagation
gap), ruled the same same-shift-fixable documentation/precision-gap class
this program has repeatedly and correctly ruled non-firing (Iterations 28,
29, 31, 32, 33), with the disclaimer-propagation gap named explicitly as
the closest call (a genuine second recurrence) and flagged for structural
attention if it recurs a third time. Full verbatim record: `LOGBOOK.md`,
Iteration 34 Phase 5.
