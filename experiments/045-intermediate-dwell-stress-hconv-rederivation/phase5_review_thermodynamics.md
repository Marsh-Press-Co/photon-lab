# Phase 5 Review — THERMODYNAMICS (fresh context)

**Panel Iteration 22, exp-045 · Seat: THERMODYNAMICS (blind, independent of my own
Phase-2 critique this cycle)**

I re-derived every load-bearing Block-B/Block-C number from `run.py`'s own
constants and `lab/thermo_sidecar.py`/`lab/kinetics.py`'s own formulas in a
standalone script, before reading `results.json` as authoritative — same
discipline Red Team's audit applied at Phase 2.

---

## Charge (1): independent re-verification of Block-B arithmetic

**Confirmed exact, to displayed precision, on every number checked.**

| Quantity | My independent value | `results.json` | Match |
|---|---|---|---|
| `h_eff` (w_on) | 3,672.834 W/(m²K) | 3,672.8340833921684 | ✓ |
| `h_eff` (r_out) | 11,111.111 W/(m²K) | 11,111.111111111113 | ✓ |
| `mass_kg` (w_on, Si) | 8.2656×10⁻¹³ kg | 8.265555284562492e-13 | ✓ |
| `dp_dt` (w_on) | 1.8431×10⁻⁷ W/K | 1.843117613244023e-07 | ✓ |
| `dt_ss_full` (w_on) | 1.0875×10⁻⁵ K | 1.0875240683859519e-05 | ✓ |
| `tau_thermal` (w_on) | 3.1392×10⁻³ s | 0.003139185832536293 | ✓ |
| `dwell/τ_thermal` (w_on) | **21.2369×** | 21.236929007418333 | ✓ |
| `dwell/τ_thermal` (r_out) | **194.1768×** | 194.17681504141214 | ✓ |
| `Bi` (silicon, both regimes) | 1.75676×10⁻⁴ | 0.00017567567567567568 (both) | ✓ |
| `area_ratio_on` / `area_ratio_absorber` | 2.91315× / 3.01377× | matches | ✓ |
| Global max ΔT (Block A) | — | 3.585×10⁻⁴ K, 55.79× margin | reproduced |
| Host-D witness check (4 pts) | — | 1.4955/1.4955/1.4950/1.4422% | reproduced |
| Block C max ratios | — | 1.0051 (5τ), 1.4509 (0.5τ) | reproduced |
| Block C max periodic ΔT | — | 7.385466×10⁻⁷ K | reproduced |

Zero arithmetic errors found anywhere in Block B or Block C. NOTES.md's
claims (P-IT22-A6, P-IT22-B, P-IT22-C) match `results.json` to displayed
precision in every case I checked. This cycle's arithmetic discipline is
clean — a genuine improvement over the Phase-1 draft's own length-scale-
mixing defect that five blind seats + Red Team had to catch last shift.

---

## Charge (2): the "Director-level refinement" of my own Biot-number finding

**Accurate, and — on closer inspection — not merely a narrowing for its own
sake but a *necessary* correction.** Red Team's Attack 6 (Phase 2) proved
`Bi = h_eff·L/k_solid = k_air/k_solid` algebraically L-invariant, correct,
and independently reconfirmed here (both `regime_w` and `regime_r` report
**identically** `1.75676×10⁻⁴`, to 6 significant figures — the cancellation
is exact, not approximate). But Attack 6's own mandatory-fix-4 text asked
for *"a standing ~10–15% internal-gradient-error caveat... on every
tau_thermal_s figure Block B produces (all regimes)"* — a **PMMA-scaled**
number (Bi≈0.137 ⇒ ~10–15% error), written before Phase 3 finalized the
material switch to silicon. Had that fix been applied literally — pasting
"~10–15% internal-gradient error" onto the silicon regimes too — the
caveat itself would have been **wrong**, not merely imprecise: at
Bi=1.76×10⁻⁴ the internal-gradient error is negligible (sub-percent), not
10–15%. NOTES.md's refinement catches exactly this and ships a
per-regime-correct disclaimer (`biot_disclaimer`, verified present and
correctly worded in both `regime_w` and `regime_r`, quoting both the
PMMA and silicon numbers explicitly). **This is not an overstatement or
understatement — it is the right fix, and it closes a trap the literal
mandate would otherwise have walked into.**

One un-flagged nuance, minor: Bi's *classical* definition typically uses a
characteristic length `L_c = V/A_surface` (for a sphere, `r/3`), not the
same `L` used to derive `h_eff` via the Nu=2 formula. Because both `h_eff`
and the reported `Bi` here use the *same* `L` by construction, the
"exactly `k_air/k_solid`" cancellation is in part an artifact of that
shared-length choice — using `L_c=L/3` would shift Bi by a factor of 3
(still ≈5.9×10⁻⁵ for silicon, still deeply lumped-valid; still ≈0.046 for
PMMA, i.e. would have crossed *below* the classical 0.1 threshold instead
of sitting just above it). Doesn't change any qualitative reading; worth a
one-line disclosure next time this module's Bi convention is touched.

**Propagation (fix 4) — adequate to its literal mandate, but a real
granularity gap recurs.** I grep-counted `biot_number`/`biot_disclaimer`
in `results.json`: **exactly 2 occurrences each** — one per Block-B regime
dict. Fix 4's own text ("every `tau_thermal_s` figure **Block B**
produces") is satisfied literally: Block B produces exactly two
`tau_thermal_s` figures, both carry the caveat. But Block A's own
`tau_thermal_regimes` summary (which *reuses* those same two figures,
`fully_corrected_si_w_consistent`/`fully_corrected_si_r_out_consistent`,
across **832 of the sweep's 2080 points**, 40%) carries no trace of the
disclaimer at all — a reader inspecting `sweep_points` or
`per_host_axis_worst_case_summary` alone would never see it, unlike the
NETD disclaimer, which fix 6 explicitly propagated to all 2080 points'
own `netd` dict. This is the *exact same pattern* Iteration 21's Phase 5
flagged for the h_conv caveat ("propagated to block scope only, not
per-point, unlike the NETD disclaimer") — recurring verbatim for a
different (related) caveat this cycle, unaddressed because fix 4 was never
worded to require point-level propagation the way fix 6 was. Not a broken
promise, but a standing process pattern worth naming so it isn't
rediscovered a third time.

---

## Charge (3): does Block A really never fall back to the decoupled shortcut?

**Verified TRUE, narrowly, by direct code read — but the claim should not
be read more broadly than its own scope.** I grepped every use of
`decoupled_dT`/`decoupled_shortcut_dT_K` in `run.py`: within Block A
(lines 337–350), `decoupled_dT` is computed **only** to build
`relative_difference` — the diagnostic Block A's own headline predictions
are about. Every classification decision in Block A —
`ts.netd_disposition(exact_dT, ...)` (line 339), the theoretical ceiling
check (line 393), `global_max_dT` (line 371), `all_undetectable_or_better`
(line 372–373) — is built from `exact_coupled_dT_K` only. NOTES.md's
"Learned" point 4 ("this does not threaten any actual verdict since Block
A always uses the exact closed form, never the decoupled shortcut") is
**true as stated, scoped to Block A.**

But **Block C's own classification does exactly what Block A's claim says
never happens**: `netd_first`/`netd_periodic` (lines 454–455) are built
from `dT_first_decoupled`/`dT_periodic_decoupled` — the decoupled shortcut,
by explicit, disclosed design (the module docstring states Block C reports
"a DECOUPLED delta-T estimate... NOT a new closed-form coupled-ODE
solution for nonzero initial population"). This is honestly disclosed as
scope, not hidden — but a reader who takes NOTES.md's "Block A always uses
the exact closed form" sentence as blanket reassurance for the *whole
cycle* would be wrong about Block C specifically. The sentence is accurate
as narrowly written; it should not be quoted outside its own Block-A
scope. Worth a one-clause fix next revision ("...since Block A [not Block
C, see its own disclosed scope note] always uses...").

---

## Charge (4): what does Block C's DECOUPLED estimate leave unaccounted for?

**A real, disclosed, but never actually quantified gap — and I did the
back-of-envelope check the record itself doesn't.** Block C's ΔT estimate
(`dt_ss_full × n_periodic`) assumes the thermal ceiling tracks the
population fraction *instantaneously* at every point in the 5-pulse train,
including across pulses that leave the kinetics population elevated
(population memory, exactly what Block C is built to test, and which it
tests correctly via the exact `relax_exact`/`integrate_segments`
kinetics-only propagation). What it does **not** do is check whether the
*thermal* state also carries memory across pulses — i.e., whether ΔT
itself fails to fully relax during the inter-pulse gap the way the
decoupled read assumes.

I checked the numbers this cycle's own record already computed: at the
primary `w_on`-consistent silicon regime, `τ_thermal = 3.139×10⁻³ s`
(3.14 ms); Block C's gaps are `5τ_kinetics(HostD) ≈ 0.45–0.5 s` and
`0.5τ_kinetics(HostD) ≈ 0.045–0.05 s` — **both 14×–160× longer than
τ_thermal**, meaning the thermal system genuinely does fully reset between
pulses (unlike the population, whose own `τ_kinetics ≈ 0.09–0.1 s` is
comparable to or larger than the 0.5τ gap, which is exactly why the
0.5τ ratio, 1.45×, is the interesting one). Within each 66.7 ms ON-exposure
itself, `dwell_central/τ_thermal(w_on) ≈ 21.2×` — the same regime Block A's
own axis-T sweep (P-IT22-A5/A6) already shows converges the decoupled and
exact solutions to well under 1% at comparable R. **So the decoupled
approximation is very likely safe here by both arguments — but neither
argument is stated, computed, or cross-referenced anywhere in `run.py`,
`phase1_proposal.md`, or `NOTES.md`.** Block A did this exact kind of
work rigorously (a swept, closed-form, falsifiable comparison against the
exact coupled ODE) for the single-exposure, n(0)=0 case; Block C's
repeated-pulse, n(0)≠0 case gets the disclosed-idealization treatment
instead of the computed-bound treatment, even though the margin (27,080×
below NETD) means it is extremely unlikely to matter. This is the
concrete form of the "genuinely new headline" gap Red Team's own
next-seat note anticipated (QUANTUM's Iteration-24 lead) — worth closing
with an actual number, not an inference, before it is relied on further.

---

## Verdict for the cycle: **PARTIAL**

The physics conclusion — the σ(I) ON-endpoint article's thermal signature
stays UNDETECTABLE across the entire intermediate-dwell regime (0.1×–10×
both time constants), under a properly re-derived h_conv/mass_kg with a
correctly-sourced material, including a first genuine repeated-sweep
check — is robust and, on my own independent re-derivation, arithmetically
clean: **zero errors found anywhere in Block B or Block C**, a real
improvement over the Phase-1 draft's own sign-flipping bug that needed
five blind seats plus Red Team to catch last time. My own self-imposed
floor (h_conv/mass_kg re-derivation) is **substantively closed**: h_eff is
now a real Nu=2 gas-conduction estimate with a disclosed Knudsen
correction, mass_kg uses a correctly-cited material, and the Biot-number
concern I raised at Phase 2 is resolved correctly (not merely
reframed) for the material actually adopted.

Not PROMISING, because this is instrument-fidelity work with T1 escape
route NONE — no mechanism moved. Not RULED OUT — nothing here closes off
any live thread. **PARTIAL** because two real, if minor, gaps remain open
at the close of this shift: the Biot-caveat granularity pattern recurring
from Iteration 21 (Charge 2), and Block C's decoupled-shortcut-at-nonzero-n0
never being checked against the exact machinery this program already has
(Charge 4) — both cheap to close, neither threatening the UNDETECTABLE
verdict as it stands (margins of 50×–27,000× below NETD throughout).

---

## Ranked top-3 candidate directions for Iteration 23

1. **Close Block C's own scope gap with a real number, not an inference**:
   extend `coupled_kinetics_thermal_dT` (or a segment-wise generalization
   using `integrate_segments`-style propagation) to nonzero initial
   temperature, and re-run Block C's 8 points through it. Cheap (the
   closed-form structure already exists; this is the same class of
   generalization Red Team supplied for the n(0)=0 case at Iteration 21),
   zero FDTD, and it turns Charge (4)'s back-of-envelope reassurance into
   an actual falsifiable check — closing the one place this cycle's own
   "Block A always uses the exact closed form" comfort claim does not
   reach.
2. **Propagate the Biot/lumped-capacitance-validity disclaimer to
   sweep-point granularity** (or at minimum tag the 832 Block-A points
   built from the two Block-B-corrected regimes with a
   `lumped_capacitance_valid`/Bi-sourced flag), closing the exact
   "block-scope-only, not per-point" pattern now confirmed to have
   recurred once already (h_conv, Iteration 21) and now a second time
   (Biot, this cycle) — cheap process hygiene that prevents a third
   instance from needing another Phase-2 panel catch.
3. **QUANTUM's aperture-consistent single-coherent-mode beam check** — not
   my seat's native charge, but the program's own most consequential open
   item: a third deferral fires Checkpoint criterion 4 without further
   debate per QUANTUM's own self-imposed tripwire (Iterations 19→20→21
   already deferred twice, and this cycle's Block C was explicitly
   executed *on QUANTUM's behalf*, not as a substitute for this check).
   Flagged here because letting it lapse a third time would cost the
   program a Checkpoint entry over a check whose cost is well-understood
   and low.
