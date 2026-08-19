# PHASE 5 — REVIEW · ELECTROMAGNETISM (fresh seat) · Panel Iteration 22 · exp-045

**Note on standing:** ELECTROMAGNETISM was this cycle's Phase-1 lead. Per
program precedent (Iteration 21's MATERIALS lead reviewed by a fresh
MATERIALS seat), this review is a fresh context with no exemption from
scrutiny of the lead seat's own draft, including its bug. All three charged
items below were re-derived from scratch against the committed record
(`phase1_proposal.md`, `phase2_*.md`, `NOTES.md`, `run.py`, `results.json`),
not copied from any prior seat's arithmetic.

---

## 1. Independent re-derivation of `coupled_kinetics_thermal_dT`

Stated system: `dn/dt = k_f(1-n) - k_r n`, n(0)=0; `dDT/dt =
(1/tau_th)(dt_ss_full*n(t) - DT)`, DT(0)=0.

**By hand.** Let K=k_f+k_r, tau_k=1/K, n_ss=k_f/K. The first equation gives
n(t) = n_ss(1-e^{-t/tau_k}) directly (n(0)=0, standard first-order
relaxation). Substituting into the linear DT equation and solving with an
integrating factor e^{t/tau_th}:

    d/dt[DT e^{t/tau_th}] = (dt_ss_full/tau_th) n(t) e^{t/tau_th}

Splitting n(t) into its constant and decaying pieces and integrating both
terms from 0 to t, then dividing back through by e^{t/tau_th} and collecting
the e^{-t/tau_th} coefficient, gives

    DT(t) = dt_ss_full * n_ss * [ 1 - (tau_k/(tau_k-tau_th))e^{-t/tau_k}
                                     + (tau_th/(tau_k-tau_th))e^{-t/tau_th} ]

— **exactly** `run.py`'s bracket (line 140-142), term for term, same
denominator `(tau_k - tau_thermal_s)` in both fractions.

**Numerically**, cross-checked with an independent forward-Euler integrator
(not `scipy`, not reusing any lab code) at 6 random (k_f, k_r, tau_th, dwell)
points spanning orders of magnitude: worst relative error **2.35×10⁻⁶**,
consistent with discretization error, not a formula mismatch.

**Verdict:** confirmed independently, by hand and numerically. This is now
the identity's **fourth-or-fifth** independent re-derivation across this
program (EM's own Iteration-20 original solve → QUANTUM's Iteration-21
closed-form re-derivation → Red Team's Iteration-21 derivation → Red Team's
Iteration-22 audit re-check → this review) — no error has ever surfaced in
it, at any check. I found none either. The Phase-1 proposal's own claim to
have "hand-derived the same bracket identity independently... before this
proposal was written" is credible and consistent with what I get from
scratch.

---

## 2. The Director's Biot-number refinement — verified correct

Red Team's Attack 6 (`phase2_redteam_audit.md`) proves `Bi = h_eff·L/k_solid`
is algebraically length-invariant because `h_eff = k_air/L`:

    Bi = (k_air/L)·L/k_solid = k_air/k_solid

**Algebra:** confirmed — L cancels exactly, for any L used consistently in
both `h_eff` and the Biot check (independent of the `w_on` vs `r_out`
regime fight in Attacks 1-3, which is a different question).

**Numbers**, checked against `results.json` directly (not NOTES.md's prose):

- PMMA: k_air/k_pmma = 0.026/0.19 = **0.13684** ≈ 0.137 ✓ (matches
  THERMODYNAMICS' Phase-2 figure and Red Team's citation of it).
- Silicon: k_air/k_solid = 0.026/148 = **1.75676×10⁻⁴**. `results.json`
  reports `biot_number = 1.756757e-04` identically in **both**
  `w_on_consistent` and `r_out_consistent` regimes — confirming the
  length-invariance claim numerically, not just algebraically.
- Ratio: 0.13684/1.75676×10⁻⁴ = **778.9×** ≈ "roughly 780×" as stated.

**Assessment: the Director-level refinement is correctly reasoned.** Both
the algebra and the two headline numbers check out exactly. If anything the
NOTES.md language ("relieves the concern almost entirely") is a slightly
*conservative* characterization — Bi(Si)≈1.76×10⁻⁴ sits **~570× below** the
classical Bi<0.1 lumped-capacitance threshold, not merely "relieved."
Silicon's own internal-gradient error under the lumped-capacitance
assumption is negligible by any reasonable standard.

**A nuance not raised by any seat this cycle, worth flagging (not a
required fix — doesn't change any number or verdict):** `h_eff = k_air/L`
is the textbook steady, quiescent-medium, pure-conduction heat-transfer
coefficient for a compact convex body of characteristic length L — e.g. for
an isothermal sphere of radius a in an infinite quiescent gas, exact
conduction theory gives Q = 4πka·ΔT ⇒ h = k/a (Nu ≡ hD/k = 2, the classical
"Nu=2" quiescent-gas limit). This derivation is only self-consistent when L
is a **real geometric length of the object**. `r_out` (the bench's actual
simulated disk radius) is such a length; `w_on` (`SIGMA_EXT_ON·dx`, an
**optical** extinction width, T9-established to depart from geometric size
whenever `Q_ext≠1`, which it does here — `w_on/r_out≈3.03`) is not. Red
Team's own recommendation to make `w_on` the "primary headline regime" is
defensible as *internal bookkeeping consistency* with
`ts.absorbed_power_established_ratio`'s own area convention — but it is not
obviously the more **physically grounded** choice for `h_eff` specifically,
and this is exactly the regime that lands `dwell/tau_thermal=21.24×` (below
`N_TRANSIENT_TAU=25`), while the geometrically-grounded `r_out` regime lands
at a comfortable 194×. Which convention is right is a genuine open question
this cycle disclosed but did not resolve — see ranked directions, below.

---

## 3. Block C — the energy-coupling/passivity question, resolved (not merely disclosed)

**What the record says.** `coupled_kinetics_thermal_dT` assumes n(0)=0.
Block C's population-memory points (nonzero n at the start of later ON
segments) are scored with a **decoupled** proxy, `dT = dt_ss_full × n`, not
fed through the closed form — disclosed in `run.py`'s docstring and
NOTES.md as a stated scope limit, "not a silent gap," but the record never
checks *which direction* that proxy errs. That is precisely EM's charge
(reciprocity/passivity/energy-coupling bookkeeping), so I checked it.

**General bound, derived by hand:** for `dDT/dt = (target(t)-DT)/tau_th`
with `target(t)=dt_ss_full·n(t)`, if `DT(0) ≤ target(0)` **and** `target(t)`
is non-decreasing, then `DT(t) ≤ target(t)` for all t (a first-order
low-pass filter chasing a rising, bounded target from below never overtakes
it — standard property of a single real pole). Randomized numerical test (4000
trials, `n0` restricted to `n0 ≤ n_ss`, `DT0 ≤ dt_ss·n0`): **zero
violations.** Without that restriction the bound genuinely fails (I found
counterexamples with `n0>n_ss`, i.e. a population *decaying* toward
equilibrium) — so the bound is conditional, not universal.

**Does Block C's actual construction satisfy the precondition?** Yes, by
induction on the pulse train: each ON segment starts from a population that
is strictly less than *that segment's own* n_ss (population never overshoots
its ceiling within finite time, and the preceding OFF segment only pushes n
further down, toward its own zero ceiling), so `n0 ≤ n_ss` holds at every ON
segment automatically. The `DT0 ≤ target(0)` half is less obvious — I
initially worried that during OFF, DT could quasi-statically lag *above* a
falling target (I found toy counterexamples of exactly this shape) — so I
did not rely on the general argument alone.

**Direct numeric settlement, using this cycle's own real numbers.** I
integrated the full 11-segment pulse train (all `n`, all `DT`, no decoupling
anywhere) for Host D, all 4 ratios, both gap settings, using the actual
`dt_ss_full`/`tau_thermal_s` from the `w_on`-consistent (primary) regime in
`results.json`, resolution-checked from 5,000 to 320,000 steps/segment
(converged to 5 significant figures):

| r | gap | n_periodic | DT_exact (K) | DT_decoupled (K) | exact/decoupled |
|---|---|---|---|---|---|
| 1e-9 | 5τ | 4.883e-10 | 5.130e-15 | 5.310e-15 | 0.9660 |
| 1e-9 | 0.5τ | 7.060e-10 | 7.574e-15 | 7.678e-15 | 0.9865 |
| 1e-5 | 5τ | 4.883e-6 | 5.130e-11 | 5.310e-11 | 0.9660 |
| 1e-5 | 0.5τ | 7.060e-6 | 7.574e-11 | 7.678e-11 | 0.9865 |
| 1e-3 | 5τ | 4.881e-4 | 5.128e-9 | 5.309e-9 | 0.9660 |
| 1e-3 | 0.5τ | 7.057e-4 | 7.571e-9 | 7.675e-9 | 0.9865 |
| 1e-1 | 5τ | 4.749e-2 | 4.995e-7 | 5.164e-7 | 0.9673 |
| 1e-1 | 0.5τ | 6.791e-2 | 7.296e-7 | 7.385e-7 | **0.9879** |

**At every one of Block C's 8 points, the exact coupled-ODE ΔT sits BELOW
the decoupled proxy by 1.2%–3.4%.** The reported decoupled numbers
(`dT_periodic_decoupled_K` in `results.json`) are a genuine, verified
**over**-estimate of the true physical ΔT at Host D under this cycle's
own parameters — the safe direction for an UNDETECTABLE claim, not a
non-conservative one.

**Answer to charge 3: no unaddressed energy-coupling or passivity concern.**
The disclosed "decoupled, not exact" scope note in the record was accurate
but incomplete — it flagged the gap without checking which way it errs. I
have now closed that gap with a proof-plus-number, not just a disclosure.
**Scope caveat on my own finding:** the bound rests on `tau_thermal` being
comfortably shorter than every inter-pulse gap tested this cycle (the
tightest margin, r=1e-1/0.5τ, is still ~14.5 thermal time constants — see
the `dt_gap/tau_thermal` ratios I computed directly from `results.json`,
ranging 14.5–1456× across the 8 points) — it is not a proof that the
decoupled proxy is *always* conservative for arbitrary future host/gap
choices, only that it demonstrably is for every point Block C actually
tested. A future cycle testing a host with `tau_kinetics` comparable to or
faster than `tau_thermal` (none of A-D at this grid are) would need this
check redone, not assumed.

---

## Other observations

- Red Team's Iteration-22 audit is itself sound wherever I independently
  checked it: Attack 1-3's length-scale/material-identity findings, Attack
  4's fabricated-citation catch (I independently `grep`-confirmed zero PMMA
  hits outside this experiment's own two files), and Attack 12's
  ceiling-monotonicity argument (Block B corrections can only lower
  `dt_ss_full`, never raise it) all reproduce cleanly.
- The Phase-1 draft's own bug (mixing `r_out` for `h_eff` with `w_on` for
  `mass_kg`, a cubic-in-length error) is real and was mine to have avoided
  as lead — but it was caught **pre-run**, at Phase 2, before any commit or
  published number. That is the process working as designed, a different
  outcome from several of this program's prior post-hoc-erratum cycles
  (Red Team's own "5 of 7 iterations" pattern note is about *post*-Phase-3
  discoveries; this is not an instance of that pattern, and Red Team says
  so explicitly).
- I found no arithmetic or logical error anywhere in `run.py` as committed
  (Phase-3 corrected version) — every load-bearing number I re-derived
  (bracket identity, Biot algebra/numbers, Block-C conservatism) matches to
  the precision I computed it.

---

## Verdict: **PARTIAL**

The core physics conclusion — the σ(I) ON-endpoint article's thermal
signature stays UNDETECTABLE across the entire genuinely-tested
intermediate-dwell regime (2080 Block-A points, 0.1×-10× both time
constants, 5 τ_thermal regimes) **and** across the population-memory/dose-
accumulation regime (Block C, now independently confirmed conservative
above) — is as solid as anything in this program's evidence base, and my
own from-scratch checks add nothing but confirmation to it. That's a real,
program-advancing result: T22's "genuinely unresolved half" (opened
Iteration 20) is now closed on the physics.

It is not PROMISING outright because: (1) the Phase-1 draft shipped a real,
sign-flipping physics bug in its headline Block-B claim (caught pre-run,
but the fact that a from-scratch "first-principles" re-derivation needed
five blind critiques plus a Red Team audit to reach self-consistency is
itself informative, per NOTES.md's own "Learned" #2); (2) the corrected
headline number for `dwell/tau_thermal` under the *primary* regime
(21.24×) sits below the informal `N_TRANSIENT_TAU=25` comfort heuristic —
genuinely less comfortable than the Phase-1 draft's retracted 126.7× claim,
and, per my §2 finding above, the choice of which regime counts as
"primary" is itself not fully physically settled; (3) P-IT22-A2 posted a
disclosed, if harmless, partial miss (1.60% vs. a predicted ≤1.55% ceiling
at one Host-D/ratio point). None of these threaten any UNDETECTABLE
verdict, but none of them is a clean pass either — PARTIAL is the honest
read, not RULED OUT (nothing here rules out a mechanism — there is no
mechanism this cycle) and not clean PROMISING.

---

## Ranked top-3 candidate directions for Iteration 23

1. **QUANTUM OPTICS' aperture-consistent single-coherent-mode beam
   check — mandatory, not optional.** This is a self-imposed Checkpoint-4
   tripwire on its *third* deferral (Iterations 19→20→21 already deferred
   twice; exp-045's own docstring states it "remains untouched... still
   due"). If Iteration 23 does not run it, Checkpoint criterion 4 fires
   automatically per the program's own standing rule, independent of
   physics content. Highest priority regardless of domain.

2. **Resolve which `h_eff` length convention is actually physically
   licensed — `r_out` (the bench's real geometric radius, the length the
   Nu=2 quiescent-conduction result is derived for) vs. `w_on` (an optical
   extinction width, T9-established to diverge from geometric size).**
   This is not cosmetic: it is exactly the choice between a corrected
   `dwell/tau_thermal` of 21.24× (below `N_TRANSIENT_TAU=25`) and 194× (well
   above it) — the one open number this cycle's own "primary regime"
   framing left unsettled (§2, above). A short, cheap follow-up: derive
   `h_eff` from an actual solved microscale conduction/convection
   correlation for the bench's real simulated geometry (disk radius
   `r_out`, or the `iso_xsec_sq` compact-blob idealization's own declared
   shape if that convention is kept), rather than treating `w_on` as a
   legitimate geometric input to a formula whose physical derivation
   requires a real geometric length. EM-native, near-zero FDTD cost.

3. **Extend Block C's dose-accumulation check beyond Host D.** This
   cycle's population-memory test (and my own conservative-bound
   confirmation above) covers only Host D, the slowest-kinetics host —
   chosen because it is most susceptible to memory, but Hosts A/B/C are
   entirely untested for this effect. Cheap (reuses
   `pulse_train_segments`/`integrate_segments` unmodified) and closes the
   remaining scope gap in a check Red Team itself only mandated as
   "bounded."

**Carried, lower priority (not in my top 3 but still open and due):**
PHOTONICS' R3 (cpl×1.5) recheck of exp-044's 0.45% achromatic-flatness
claim (still unresolved, comparable in magnitude to its own noise floor);
the still-blocked rigorous RSA/TPA literature check (T18/WebFetch, now many
consecutive shifts); T21's contamination-risk re-score; the settling-margin
FDTD test (PHOTONICS'/EM's own longstanding #1 pick, still not run).
