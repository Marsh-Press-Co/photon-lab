# PHASE 5 — RED TEAM AUDIT · Panel Iteration 23 · exp-046

*Seventh seat, speaking last, with the full cycle record and all six blind
Phase-5 reviews. Standard: internal consistency, falsifiability, expressibility,
constraint violations — not textbook compliance. Red Team never trusts a seat's
prose, including its own: every load-bearing claim below was re-derived, re-run,
or re-read from source in this session, and where six seats agree I checked
whether they are agreeing on something true. **Four new 1400-step FDTD runs and
one full angular-spectrum/Huygens comparison were executed here**; scripts are
listed in the verification appendix.*

*Disclosure of interest, stated first: **Attack 2 of this cycle's own Phase-2
audit is my seat's work**, and QUANTUM OPTICS' Phase-5 review attacks it
directly. I re-derived QUANTUM's counter-claim numerically from the actual
`gaussian_angle_weights` code before reading its algebra as anything but a
claim. **QUANTUM is right and Attack 2 was scoped too broadly.** The finding is
recorded against my own seat, with numbers, in §2.*

---

## 0. HEADLINE

Six seats found real defects and three of the four disputes the Director put to
me resolve **against the committed record**. Ranked by consequence:

1. **The shipped stage-16 gate (b) is calibrated against a physically wrong
   comparator, and it is worse than PHOTONICS or ELECTROMAGNETISM stated.** I
   reproduce their corrected comparator independently, from the code, and then
   went one step further: at Block A's *own* extreme cell (FWHM=20°, θ₀=40°,
   `width`=28.03) I ran the FDTD and the gate reads **9.38% against its own 8%
   bar — it would FAIL, and would blame the engine, whose true error there is
   0.38%**. The gate is simultaneously ~17× too loose where it was calibrated
   and actively mis-firing inside the block it certifies. It is committed in
   `lab/`, it is green, and nobody re-derives a green gate. **Confirmed, load-
   bearing, mandatory same-shift.**
2. **QUANTUM's grating-lobe correction to my own Attack 2 is exact.** I measured
   the effective aperture directly: at all 9 FWHM=20° cells
   `beam_divergence_coherent` synthesises a three-lobe comb with replicas at
   ±433/578/722 cells (450/600/750 nm), amplitude 0.440, carrying **41.7–68.0%**
   of the aperture's intensity outside ±3·w_line. The docket's instruction to
   record "a permanent T21 fact" **unqualified** would enter this program's
   permanent memory false at 9 of 36 cells. **Confirmed against my own seat.**
3. **"Eye-invisible" is live and unflagged in `phase1_proposal.md` at exactly
   the two loci docket item 20 names, with no SUPERSEDED banner — one cycle
   after this program invented that banner for this exact failure mode, and in
   the same shift the Director cited that precedent for a different item.**
   Confirmed by direct grep and `git log`. **Checkpoint-4-shaped.**
4. **A1's "withheld as gate-backed" disposition exists in one prose paragraph
   and nowhere else.** `withheld` appears **0 times** in the 3.21 MB
   `results.json`; A1's canonical prediction record reads as an unqualified,
   fully-compliance-audited pass; `gate_disposition` is never printed to
   console; and the withheld reading is counted in the cycle's own PARTIAL
   tally. **Real propagation gap, not a defensible division of labour.**
5. **THERMODYNAMICS' Biot and MATERIALS' emissivity findings are both real and
   both non-verdict-moving** — verified by computing the worst case myself:
   **ε→0 moves the mixed regime's margin from 607.33× to 607.05×.** But
   THERMO's finding *is* verdict-moving for **T23**, which is a τ_thermal
   question, and T23's disposition is written nowhere durable.
6. **New, mine:** the `C_empty` channel carries an uncharacterized
   absorbing-boundary systematic. I ran ABSORB 40→60 at two legs: A-v4 moves by
   **+0.0070 in C** (1.39× VISION's own C_thr) and A-v1 by **−0.0022** — and
   the A-v1 shift moves *away* from the desk propagator, so EM's "mostly a
   boundary artefact" is confirmed at one leg and **not** established as a
   general explanation. What is established is a 0.002–0.007 absolute
   systematic on `ABSORB=40`, inherited unexamined by every T21/T16 reading
   since exp-041.

**Checkpoint criterion 4: does NOT fire, CONDITIONAL on the Tier-0 docket
below landing this same shift — with a harder condition than prior cycles
(§6).** Two items would fire it independently if propagated as written.

**Verdict recommendation: PARTIAL.**

---

## 1. DISPUTE 1 — the S16-b gate target. RESOLVED: PHOTONICS and EM are right, and understate it.

Two seats converging is not evidence. I resolved this from the code and from
four new FDTD runs.

### 1.1 What the engine actually is (read, not accepted)

- `lab/fdtd2d.py:232-237`: `self.Ez[s["x"], s["sl"]] += env*np.sin(ωn − phase)*profile`.
  A per-step **additive** term in the E-update — an impressed line-**current**
  sheet J_z, not a prescribed aperture field. The radiated field's angular
  spectrum therefore carries **Ẽ(k_y) ∝ J̃(k_y)/k_x**.
- `lab/ambient.py:36-39` → `lab/sections.py:79-88`:
  `observer_profile = −flux_profile_x = +½·Re(E_z · conj(H_y))`. A **flux**,
  which for each plane-wave component carries **+k_x/k**, once, via H — not
  `|E|²`.
- `lab/validation/run_all.py:1323-1337` (`stage16…exact_center`, shipped this
  cycle) propagates `exp(−(y/w)²)exp(ik sinθ₀y)` with `exp(ik_x z)` and reads
  **`|E|²`**. Neither factor. Two missing obliquities, in opposite directions,
  and they do not cancel.

This is the **same error species** ELECTROMAGNETISM adjudicated at Iteration 19
(LOGBOOK T21: "obliquity entering flux ONCE, via H, not squared via E"), now
inside `lab/` rather than inside an experiment. That is a fourth appearance and
the first in the trust suite.

### 1.2 My own numbers (independent implementation, n_fft = 2²²)

S16-b configuration: `width`=40, θ₀=40°, λ_cells=20, z=`D_SP`=223.

| model | 1/e² centre | half-width | peak |
|---|---|---|---|
| ray optics (the pre-registered target) | 979.119 | — | — |
| field aperture, `\|E\|²` — **what stage 16 ships** | **987.144** | 89.103 | 973.56 |
| field aperture, flux | 983.035 | 86.855 | 970.73 |
| current source (1/k_x), `\|E\|²` | 996.748 | 94.648 | 979.71 |
| **current source (1/k_x), flux — physically correct** | **991.675** | **91.587** | **976.56** |
| **exp-042's own committed `_G0_for` + `field_and_h`** | **991.645** | **91.576** | **977.0** |
| **FDTD, my own run** | **992.093** | **90.988** | **977.0** |

Two independent correct formulations — my from-scratch angular spectrum and
exp-042's committed Huygens propagator, which is *the propagator this cycle
exists to validate* — agree to **0.030 cells**. FDTD sits **0.418 cells** from
either, **0.459% of the beam half-width**.

**Corrected attribution of the 12.974-cell gate failure:**

| term | cells | share |
|---|---|---|
| target error (ray optics vs correct exact) | **12.556** | **96.8%** |
| engine error (FDTD vs correct exact) | **0.418** | **3.2%** |

NOTES.md commits **8.03 / 4.95 (62% / 38%)**. The engine is **12× better** than
the cycle reports; the target is **56% worse**. PHOTONICS' split (12.55/0.42)
is exact; EM's (0.45 cells / 0.49%) is exact.

**And PHOTONICS is additionally right that non-paraxiality is not the dominant
cause.** Under a *peak* estimator — which is what ray optics actually predicts,
a stationary-phase ray — the correct exact answer is 976.56, FDTD peak-cell
977.0, ray optics 979.12: **2.56 cells**. So the 12.97 cells decompose as
≈10.4 cells **estimator/skew mismatch**, ≈2.6 cells genuine non-paraxial target
error, ≈0.4 cells engine. NOTES.md Learned #2 and idealization 2 ("this
idealization has now bitten") name the right species and assign it ~4× too much
of the effect, and none to the estimator pairing that dominates.

### 1.3 The shipped gate is not merely loose — it mis-fires

PHOTONICS says ~17× loose. I confirm: bar 8%, engine's true accuracy 0.459% →
**17.4×**. A pointing regression of up to ~7 cells would pass.

But I ran the test neither PHOTONICS nor EM completed. **New FDTD run**, Block
A's own extreme cell (`width` = w₀/cosθ₀ = 28.03 at FWHM=20°, θ₀=40°, 600 nm):

| quantity | value |
|---|---|
| FDTD centre / half-width | **1005.549 / 120.776** |
| shipped comparator (`exact_center`) | 994.223 → offset **9.38%** vs an **8% bar → FAIL** |
| correct comparator (current/flux) | 1005.090 → offset **0.38%** |

**A gate that would fail on a configuration inside the very block it certifies,
and would attribute the failure to a solver that is accurate to 0.38%, is not a
gate.** EM's judgment ("a gate that cannot be trusted to fail for the right
reason is not a gate") is upheld and now demonstrated on the engine.

**Gate (d) carries the same disease in miniature**, confirmed: its closed-form
target is 79.4747; the correct exact propagation gives 81.051 (my `_G0_for`
run) and FDTD gives 80.4715 (my run). So ~2/3 of gate (d)'s reported "1.25%
engine error" is target error; the engine is 0.72% from exact. Gate (d) passes
for partly the wrong reason, but it *is* discriminating (9.8% at the wrong
width vs 1.25% at the right one) and it does satisfy PANEL.md's identity-gate
rule. Gate (a) is legitimate and passes for the right reason (EM checked the
target's own accuracy at 0.43%; I did not re-run it). Gate (c) is a regression
anchor, not an absolute identity.

**Ruling.** PHOTONICS' and EM's convergent finding is **CONFIRMED, sharpened,
and the single most consequential item in this packet.** It is repairable at
zero FDTD cost with an object already in this repo. Docket items 1–2.

---

## 2. DISPUTE 2 — QUANTUM vs my own Attack 2. RESOLVED AGAINST MY SEAT.

Attack 2 proved that `beam_divergence_coherent`'s effective aperture is
`P(Y)·Σ_i √w_i e^{ik sinθ_i Y}` and then replaced the **sum** by an **integral**.
That step is a Poisson-summation step, and it is exactly where the aliasing is
discarded. It is legitimate only when the comb's replicas fall outside the
aperture. Attack 2 never checked whether they do.

### 2.1 My measurement (from the actual code, all 36 cells)

`gaussian_angle_weights(θ₀, FWHM, n=41, half_width_factor=2.5)` gives
δθ = 0.125·FWHM. Replica spacing ΔY ≈ λ_cells/(cosθ₀·δθ_rad). Aperture
half-span = 752 cells.

| λ | θ₀ | FWHM | w_line | ΔY predicted | replica measured | replica amp | **intensity outside ±3w_line** (untapered / tapered) |
|---|---|---|---|---|---|---|---|
| 450 | 36° | 20° | 19.91 | 424.9 | −412 | 0.472 | **68.0% / 67.1%** |
| 450 | 40° | 20° | 21.02 | 448.8 | −433 | 0.440 | **67.1% / 66.6%** |
| 600 | 40° | 20° | 28.03 | 598.4 | −578 | 0.440 | **64.3% / 63.4%** |
| 750 | 38° | 20° | 34.06 | 727.1 | −704 | 0.456 | **52.7% / 47.2%** |
| 750 | 40° | 20° | 35.04 | 747.9 | −722 | 0.440 | **48.1% / 41.7%** |
| any | any | ≤10° | — | 850–5984 | none in aperture | ≤0.06 | **≤0.1%** |

QUANTUM's table (67.1 / 64.3 / 48.1%, with-taper 41.7%) is reproduced **to the
printed digit**. Across all 9 FWHM=20° cells the span is **41.7–68.0%**.

**Ruling: QUANTUM is right.** At the 27 FWHM≤10° cells the identity holds
without qualification. At the 9 FWHM=20° cells the synthesised object is a
three-lobe comb of which the `w₀/cosθ₀` Gaussian carries only 32–58% of the
energy. The A3 *measurement* (a local 1/e half-width around the peak) is not
falsified — the central lobe really does have half-width `w₀/cosθ₀`. What is
falsified is the *interpretation* NOTES.md item 3 and docket item 5 attach to
it: that the coherent column already **is** the diffraction-limited single
transverse mode. It is not, at 9 of 36 cells. **The "permanent T21 fact" must be
scoped before it is written into LOGBOOK.** Docket item 6.

### 2.2 The residual's attribution — my Attack 2 parenthetical is also wrong

`results.json`'s A3 band string carries my "(taper truncation)". I checked it
and it cannot be right: at FWHM=20° `w_line` is 21–35 cells inside a 752-cell
half-aperture, i.e. truncation at 21–36 waists (e^{−441}); and my own lobe
census shows including the taper moves the fraction only 67.1%→66.6%.

QUANTUM's replacement is the second-order term of the `sinθ` expansion,
zero free parameters:

> **w_meas/w_line = 1/√(1 − 4σ_θ² tan²θ₀)**

Checked by hand at both scored points: FWHM=10°/θ₀=40° → **0.783%** predicted vs
**0.781%** measured (`results.json`); FWHM=20°/θ₀=40° → **3.248%** predicted vs
**3.252%** measured. Two headline numbers, one closed form, no fit. Docket item 7.

### 2.3 A4 was dropped on a false premise

I dropped P-TH23-A4 at Phase 2 because "there is no divergence to explain." Its
*magnitude band* (5–20%) was indeed falsified. Its *mechanism* — 41-point
angular sampling aliasing — is real. I measured it: `beam_divergence_coherent`
at n=41 vs n=401, all 36 cells, moves the scored `C_empty` by up to **4.473%**
(450 nm/36°/FWHM=20°; QUANTUM measured 3.18% under a different reduction), 0.86–1.95%
at the other 450 nm FWHM=20° cells, and <0.16% everywhere else.
**`gaussian_angle_weights`'s n=41 has never had a convergence check in this
program's history**, and it is the kernel that produced both exp-042 columns
Iterations 19–23 have argued over. Docket item 8; new open item for Iteration 24.

### 2.4 QUANTUM's request to record its own conjecture as REFUTED — partly granted

QUANTUM asks that its Iteration-20 conjecture be recorded REFUTED rather than
"mis-posed," and is right that "mis-posed" is over-charitable. But QUANTUM is
being *harder* on its own seat than the evidence supports. My ruling, three
lines:

- **Premise** (exp-042's coherent column holds the full ~75λ aperture fixed —
  beamforming, not natural divergence): **REFUTED at the 27 FWHM≤10° cells**;
  **PARTIALLY VINDICATED at the 9 FWHM=20° cells**, where §2.1's replicas at
  ±433–748 cells do substantially occupy the aperture — directionally what the
  original premise claimed.
- **Prediction** ("lands much closer to the incoherent reading"): **REFUTED at
  all 36 cells, at the desk** (36/36 above `C_THR`, 35/36 at ≥20× incoherent,
  min|C| = 0.03227 — reproduced).
- **"Mis-posed"** belongs to **P-TH23-A1 as a scored metric** (Attack 7's
  pointing tautology) and nowhere else.

Docket item 18.

---

## 3. DISPUTE 3 — "eye-invisible". VISION and THERMODYNAMICS CONFIRMED, verbatim.

```
$ grep -n -i "eye-invisible|superseded|struck" experiments/046-*/phase1_proposal.md
46:  ... 607× below NETD, Wien peak 9.885 µm, eye-invisible.
342: | P-TH23-B3 | Mixed regime is still UNDETECTABLE and eye-invisible (seat sidecar) | ...
$ git log --oneline -- experiments/046-*/phase1_proposal.md
8950125  exp-046 (panel Iteration 23): Phase 1 proposal — ...
```

One commit. Never amended. No banner of any kind. Docket item 20 read: *"Strike
'eye-invisible' from §1 and from P-TH23-B3's prediction text"* — §1 and
P-TH23-B3 are **sections of `phase1_proposal.md`**, the exact two loci that
still carry it.

The precedent is one cycle old and I verified it directly:

```
$ git log --oneline -- experiments/045-*/phase1_proposal.md
f48de18  exp-045 Phase 5 + mandatory same-shift close: Red Team's 10 fixes applied ...
4c5f42c  exp-045: Panel Iteration 22 Phase 1 proposal ...
$ head -11 experiments/045-*/phase1_proposal.md
**SUPERSEDED — see `NOTES.md` Phase 3 ... This file is preserved UNEDITED below
as the historical record ... (T10's "flag, don't rewrite" convention, extended
here to a Phase-1 draft for the first time ...)**
```

And exp-046's Phase-1 draft carries **far more** superseded content than
exp-045's did: the entire §2.1 geometry table (docket 3), §1's N_F range,
`width = w₀` at every oblique call (docket 1), the `w_y=199.33` slip (docket 2),
idealizations 2 and 4 (dockets 12/11), the "sourced" silicon label (docket 18),
§2.3's "conduction length alone" (docket 19), predictions A3/A4/A7, and the
soft-form Tier-2 escalation (docket 24).

Against that, two committed statements are **false as claims about this
repository**:

- `NOTES.md:14-15` — "The Phase-1 proposal's 'eye-invisible' language is
  **struck everywhere** (docket 20)."
- the `NETD_DISCLAIMER` string, repeated **2672 times** in `results.json` —
  "no 'eye-invisible' claim is made anywhere in this cycle [docket 20]".

**Adjudication.** Two things must be held apart, and both seats hold them apart
correctly:

*The substantive half of docket 20 IS delivered.* No live artifact, no scored
prediction, no committed result carries a perceptual claim. VISION audited this
word by word and credits it; THERMO's grep table confirms it; I re-ran both.
P-TH23-B3 as committed is a pure instrument comparison with the Wien peak
reported bare. The constraint-3-shaped leak that the item existed to close **is
closed**. This is not a constraint quietly dropped.

*The delivery claim is false, and the house remedy exists and was not applied.*
That is the fix-docket-delivery pattern in its characteristic form — 95%
delivered, 100% claimed, gap in the historical record — and it is aggravated by
two facts the Director's brief names and I verified: (a) the SUPERSEDED-banner
convention was invented one cycle ago **for this exact failure mode**; (b)
`phase3_synthesis.md:39-53` cites the Iteration-22 hardened-rule precedent for
item 24 in the same document, so the convention was in the Director's hand that
shift.

Criterion-4 ruling in §6. Docket item 3.

---

## 4. DISPUTE 4 — A1's withholding. VISION CONFIRMED: a real propagation gap, not a division of labour.

Measured directly on the 3,210,029-byte `results.json`:

| string | occurrences |
|---|---|
| `withheld` | **0** |
| `WITHHELD` | **0** |
| `gate_backing` | **0** |
| `gate-backed` | **1** — inside `block_a_fdtd.gate_disposition`, a prose paragraph |

And the canonical record a future cycle cites,
`block_a_aperture_consistent_beam.predictions["P-TH23-A1"]`, has exactly these
keys: `class`, `statement`, `n_above_C_THR`, `n_of`,
`n_at_or_above_20x_incoherent`, `min_abs_C`, `band`. No withholding flag, no
class change — and it *does* carry the `C_THR` disclaimer verbatim, which makes
it read as the most compliance-audited entry in the file.

`run.py`'s post-run console path prints the gate table (S16-b **FAIL**), then
A5, then the exploratory legs, then writes the file. `gate_disposition` is
**never printed**.

**Ruling: this is a real defect, not a defensible division of labour.** Three
reasons, none of them stylistic:

1. **This cycle demonstrates the citation route itself.** exp-046 pulled
   exp-041's `block_main` `C_empty` and exp-042's
   `phase5_erratum.block_beam_corrected.worst_cell` out of `results.json`, not
   out of anyone's prose. Machine-readable is the load-bearing artifact by this
   program's own demonstrated practice.
2. **The shape is Iteration 17's Checkpoint-4 firing exactly** — a
   Director-level scope judgment failing to reach the committed record — with
   the loci inverted relative to Iteration 20.
3. **VISION's V1b and V1c are additionally correct and I confirm both.** The
   scorecard cell "PARTIAL (computed in band; **withheld as gate-backed**)"
   parses literally as the inverse of its intent, and LOGBOOK entries are built
   by copying scorecard rows. And a reading the Director has withheld is
   counted in the cycle's own "11 CONFIRMED, 3 PARTIAL" headline.

**Two things I will not join VISION on.** The withholding *judgment* itself is
sound — PHOTONICS is right that it hides nothing and invites the stricter
reading, and it is a better disposition than a post-hoc reinterpretation.
And once dispute 1's fix lands, the pointing chain is validated to **0.418
cells** and A1 is fully gate-backed at 600 nm/40°/FWHM=2°, so the honest end
state is *restore A1 as an explicitly-labelled desk geometry reading*, not
leave it in limbo. Docket item 5.

---

## 5. DISPUTE 5 — fill factor / Biot (THERMO) and emissivity (MATERIALS). Both real; neither moves a verdict; one moves T23.

### 5.1 The margins, and the worst case, computed here

`dt_ss = P_abs / [area·(4εσT³ + h_eff)]`. At the mixed regime
(L_cond = r_out = 2.34 µm): 4εσT³ = **5.1426** W/(m²K) against
h_eff = k_air/L = **11111.11** W/(m²K) — the radiative channel is **0.0463%** of
the loss.

| stress | dt_ss inflation | mixed-regime margin |
|---|---|---|
| committed (ε=0.9) | 1.000000× | **607.33×** |
| ε → 0.09 | 1.000417× | 607.08× |
| ε → 0 (absurd bound) | **1.000463×** | **607.05×** |

**MATERIALS' emissivity concern is real as a disclosure gap and wrong by ~4
orders of magnitude as a number.** Its review states ε_corr = 0.1 "only inflates
`dt_ss_full` by up to ~4×". The true figure is **1.0004×**. Its *conclusion*
("comfortably short of threatening 607×") holds a fortiori, and its actual
finding — that idealization 7's "dilution is uniformly conservative" framing
omits a third, opposite-signed consequence already flagged in
`lab/thermo_sidecar.py:151-153` since exp-033 — stands. Record the computed
number, not the estimate (docket 16). Note also that `netd_disposition`'s own
`emissivity_correction` is a multiplier **on** ΔT (`lab/thermo_sidecar.py:205`),
so on the detector side lower emissivity is strictly conservative.

Fill factor cannot touch `dt_ss` at all: mass and ρC_P do not appear in it.

**Answer to the Director's question: yes, 607×–6681× absorbs both concerns in
the worst case either seat computed, with four orders of margin to spare.** No
UNDETECTABLE classification anywhere across 2496 + 42 + 250 points is
threatened. Both reviewing seats' conclusion is upheld.

### 5.2 THERMO's Biot finding is right, and it is a T23 finding, not a ΔT finding

I reproduced its Maxwell–Garnett table exactly (κ_eff = k_air(1+2φ)/(1−φ)):

| φ | committed dwell/τ | κ_eff | **Bi = k_air/κ_eff** | lumped-valid (Bi<0.1)? |
|---|---|---|---|---|
| 1.00 | 194.18 | 148 | 1.757×10⁻⁴ | yes |
| 0.50 | 388.35 | 0.1040 | **0.250** | **no** |
| 0.10 | 1941.8 | 0.0347 | **0.750** | **no** |
| 0.01 | 19418 | 0.0268 | **0.971** | **no** |

THERMO's framing is exactly right and I adopt it: **the sensitivity table
offered as reassurance is evaluated at fill fractions where the lumped single-τ
model that produced its numbers is no longer licensed, and the reassurance is
largest precisely where the model is most invalid.** THERMO's own honest
counter is also right (internal gradients make the radiating surface cooler,
so detectability gets more conservative), which is why this does not move the
UNDETECTABLE verdict.

But **T23's entire content is a τ_thermal question**, and a τ_thermal that is
not a well-defined single number is a worse problem for T23 than the
length-scale ambiguity T23 was opened to settle. This is the sharpest
*charter-relevant* finding in the packet after dispute 1. Docket item 15.

### 5.3 T23's disposition is recorded nowhere durable — CONFIRMED

```
$ grep -n "T23" NOTES.md          → 2 hits: the title, and the Hypothesis line
$ (T23 in results.json)           → only inside two regime LABELS:
                                     "mixed_w_power_r_cond_T23", "..._T23_PRIMARY"
```

No `t23_disposition` key. No Learned item about Block B — the five Learned items
are propagator-out-of-regime, gate-target validity, grid-extension, the
dimensionless dwell, and the `--only` bug. The lead seat's own Tier-1 #2
deliverable produced no recorded lesson.

The *argument* for the mixed convention exists in exactly one place —
`phase1_proposal.md` §2.3 — which is the one document in this directory with a
dozen struck claims in it **and no banner**. The two failures compound: a future
seat citing exp-046 for T23 finds a number with no reasoning, or reasoning
inside a document it has been given no signal to distrust. EM's ruling ("three
endpoints and no ruling is worse than two") is upheld. Docket item 14.

---

## 6. CHECKPOINT CRITERION 4 — EXPLICIT RULING

**Criterion 4 does NOT fire — CONDITIONAL, with a harder condition than any
prior cycle has attached.**

### 6.1 What triggers the pattern

Four distinct instances this cycle, all verified above:

| # | instance | class |
|---|---|---|
| A | docket 20 undelivered at its two named loci; "struck everywhere" and ×2672 "anywhere in this cycle" are false; no banner, remedy one cycle old | fix-docket delivery + **false statement of completed work** |
| B | docket 21 delivered at 3 of 5 named loci with the override unstated; idealization 10's per-point claim false at 250 of 2788 | fix-docket delivery |
| C | A1's Director-level withholding absent from the canonical record and the console; counted in the success tally | **Iteration-17 shape exactly** |
| D | `VALIDATION.md`'s new `--only` erratum retro-invalidates five historically correct citations | over-claimed defect (the pattern's mirror image) |

Instance A carries the criterion-4 weight, and Iteration 20's own precedent is
directly on point: VISION's "erratum-never-written" finding was ruled **"worse
than described: a false statement of completed work, not an omission"** and the
non-firing was made conditional on the fix landing that shift.

### 6.2 Why it does not fire

1. **Criterion 4's own text is about drift** — an unfalsifiable claim standing,
   a constraint quietly dropped, especially #3. The constraint-3-shaped leak
   docket 20 existed to close **is closed**: no live artifact, no scored
   prediction, no committed result carries a perceptual claim, verified
   independently by VISION, THERMO and me. What survives is in a document the
   house T10 convention already designates an unedited historical record. That
   is a **labelling** failure, not a drift failure.
2. **The false-completion half — which is the part that carries criterion-4
   weight — is fully cured by a same-shift fix** (a banner, two corrected
   sentences, one corrected constant). The mechanism this program has applied at
   Iterations 19, 20, 21 and 22 is exactly this, and its stated justification
   ("caught and corrected within the same close, not left to a next cycle") is
   unimpaired here.
3. **The aggravating fact does not change the remedy's availability.** That the
   banner convention was invented one cycle prior, and that Phase 3 cited that
   precedent the same shift for item 24, raises **severity**, not cost. It is a
   reason to harden the condition — which I do — not a reason to convert a
   conditional non-firing into an unconditional firing, which would break a
   four-cycle precedent on a case whose substantive half is clean.
4. **Instances B, C and D are all cheap, disclosed-in-good-faith, and none of
   them conceals anything.** C is the closest to Iteration 17's firing, but
   Iteration 17 fired on an *uncorrected* recurrence; this one is caught inside
   the same close by the process designed to catch it.
5. **Criterion 5 does not fire** — Iteration 22 and Iteration 23 both advanced
   the logbook (T22 closed; T17/Amendment 3 collapsed to a closed form; the
   Iteration-22 hardened aperture rule satisfied). **Criterion 1** does not fire
   (no constraint metric is scored). **Criterion 2** does not fire (no boundary
   proven; no realizability tier moves). **Criterion 3** does not fire (zero
   `lab/` engine change — I verified `git diff` touches only
   `lab/validation/run_all.py` and `VALIDATION.md`).

### 6.3 The hardened condition

**If ANY Tier-0 item (docket 1–5) is carried past this close, Checkpoint
criterion 4 fires automatically and immediately — no further debate, no seat
vote, no Director discretion, and no renewed-deferral reason of any kind,
including one blessed by a Red Team audit.**

### 6.4 Two items that would fire criterion 4 independently if propagated as written

**(i) VISION's V3 — the item-24 carve-out.** This is the one finding in the
packet that meets criterion 4's *literal* text: a constraint quietly weakened
while being advertised as hardened. Compared clause by clause:

- Iteration 22 (`LOGBOOK.md:8324-8329`): "...no further debate, no seat vote, no
  Director discretion, **and no further one-cycle extensions via prose**."
- `phase3_synthesis.md:47-53`: "...(by any lead seat, ... **or with an explicit
  renewed-deferral reason that itself survives a Phase-2 Red Team audit**),
  ... **mirroring the aperture-check rule's own wording exactly**."

The carve-out re-admits precisely the device the sibling rule forecloses; the
"no further one-cycle extensions via prose" clause is dropped; and the claim of
exact mirroring is false. Worse — and this is dispositive — **my own Phase-2
docket item 24 wrote "I do not contest the deferral," so Iteration 23's own
deferral is an explicit renewed-deferral reason that survived a Phase-2 Red
Team audit. Under the new wording, the behaviour that tripped the tripwire
satisfies it.** A tripwire its own triggering event satisfies is not a
tripwire. And it exists in three inconsistent renderings (full text with
carve-out in `phase3_synthesis.md`; harder one-line form in `NOTES.md:60-63`;
a contentless pointer in `results.json`, where `glare`/`tripwire`/`Tier-W`/
`criterion 4` all occur **zero** times — I counted). Docket item 4, Tier 0.

**(ii) The shipped stage-16 gate (b).** A physics convention that is
demonstrably wrong, already committed inside `lab/`, forward-looking, green, and
shown in §1.3 to mis-fire inside its own block. This is a *trust-suite integrity*
defect, a different and arguably graver class than the fix-docket pattern. It
does not fire criterion 4 today for the same reason as the rest — caught at
Phase 5, repairable at zero FDTD cost this shift, disclosed in three places, and
`run.py` honestly scores the original gate as FAILED. But EM is right that this
is the **second consecutive cycle** in which a same-shift, post-freeze correction
shipped an unreviewed physics convention, and Iteration 19's own LOGBOOK entry
warned in terms that this "should not be read as establishing same-shift
correction is generally safe from criterion 4." I therefore adopt and harden
EM's proposed standing rule (docket item 20).

---

## 7. THE REST OF THE PACKET, ADJUDICATED

**A5's conditioning — PHOTONICS, EM, THERMODYNAMICS and QUANTUM all correct,
independently, and I confirm the arithmetic from `results.json`:**

| leg | N_F | rel in **C** (reported) | rel in **1+C** | amplification |
|---|---|---|---|---|
| A-v1 | 53.98 | 1.907% | **0.268%** | 0.1× |
| A-v2 | 2.16 | **0.028%** | **8.405%** | **299×** |
| A-v3 | 0.54 | **0.114%** | **8.373%** | **74×** |
| A-v4 | 65.60 | 5.680% | **0.799%** | 0.1× |

`results.json` itself computes `conditioning_amplification` = **327.3** and
**81.6** for the object-present legs paired with A-v2/A-v3, and `run.py` uses
exactly that conditioning to **drop P-TH23-A7** as unusable. The cycle applied
its own disqualifying criterion to one prediction and not to the neighbouring
one at the identical `C_empty` values. Nothing is refuted (8.4% passes a 15%
band), but "CONFIRMED 4/4 — the cycle's genuine falsifiable Block-A content" is
2 informative legs and 2 saturated ones. **Upheld.** Docket item 9.

I also uphold PHOTONICS' narrower point that `_G0_for`'s validity parameter is
**kr**, not N_F (the module asserts `kr > 50`, set by `D_SP` and the window
span, not by aperture width). "Validated three orders of Fresnel number outside
where it was built" is the wrong statement of what was earned.

**PHOTONICS' chromatic finding — CONFIRMED from `results.json`'s own 36 cells.**
Four of 36 cells read **positive** C (a glint at the object window), all at
FWHM=2° and 600/750 nm, with a sign reversal across the visible band at all
three θ₀:

| θ₀ | C(450) | C(600) | C(750) |
|---|---|---|---|
| 36° | −0.24576 | **+0.07625** | **+0.24362** |
| 38° | −0.37331 | −0.03227 | **+0.16367** |
| 40° | −0.47266 | −0.12334 | **+0.09368** |

This contradicts idealization 2's committed "**Consequently** Block A's 3-λ
sweep carries NO material wavelength dependence" *and* A1's own committed
mechanism sentence ("C → −1 regardless of coherence") at exactly those cells;
the `|C| > C_THR` band is blind to it because it takes an absolute value. The
emitter is λ-scale-invariant and the medium dispersionless — that part is true
— but `N_F ∝ λ_cells` and the reading is strongly chromatic. Given T7's
chromatic-silhouette finding and T21's worst cell having been 750 nm since
Iteration 19, this is not a cosmetic wording issue. Docket item 10; R3 check
queued for Iteration 24 before "glint at 750 nm" is allowed into the record as
physics.

**The `--only` erratum — EM and THERMODYNAMICS both right; I dated it myself.**
The exact-match rule (`if len(tokens) > 1: return str(n) in tokens`) landed at
**6082e02, 2026-08-17**. I extracted the pre-6082e02 `_stage_selected` from git
and ran it: `--only 12346789,10,11` selects **{1,2,3,4,6,7,8,9,10,11}** — the
intended ten stages. All five SESSION_LOG citations of that invocation sit at
lines 1026/1155/1253/1347/1455, under headers dated **2026-08-14 / 08-15**
(Iterations 7–11), every one predating the commit that created the regression.
**No published trust-suite citation in this program's history was damaged.** The
`--only 16 → {1,6,16}` and `--only 12 → {1,2,12}` halves are correct and the
fix itself is right. But `VALIDATION.md` is the file CLAUDE.md instructs every
agent to read before bench work, and it now retro-impugns five valid citations
against exp-030/031/032/033/034. Docket item 12 — **before** it reaches LOGBOOK.

**EM's absorbing-boundary finding — my own runs, and I narrow it.** Four new
FDTD legs:

| leg | ABSORB | FDTD C | vs desk propagator | ΔC vs ABSORB=40 |
|---|---|---|---|---|
| A-v4 (750/38°/FWHM2), desk C = +0.163673 | 40 | +0.154376 | 5.68% | — |
| | 60 | **+0.161333** | **1.43%** | **+0.00696** |
| A-v1 (600/40°/FWHM2), desk C = −0.123345 | 40 | −0.125698 | 1.91% | — |
| | 60 | **−0.127896** | **3.69%** | **−0.00220** |

EM's A-v4 numbers reproduce exactly (5.68%→1.43%, ΔC = 0.0070 = **1.39×
VISION's own C_thr**). But my A-v1 leg — which EM did not run — moves *away*
from the desk value under the same refinement. **So EM's headline ("the residual
is mostly a boundary artefact, and the desk propagator is better than credited")
is confirmed at one leg and is NOT established as a general explanation.** What
*is* established, and is the durable finding, is that `C_empty` on this channel
carries an uncharacterized `ABSORB` systematic of **0.002–0.007 absolute** —
0.4–1.4× the perceptual threshold the whole T21 contamination question is
scored against — at an `ABSORB = 40` inherited unexamined by every T21/T16
reading since exp-041, including all 30 Block MAIN rows T21's fringe mechanism
was fitted to and every N9/N17 delta T16 scores. This is structurally the same
debt T11 tracks for the box-ledger channel. **New live thread, docket item 19.**

**Settling — EM ran it and it should be credited, not re-deferred.** STEPS
1400→2800→4200 moves A-v4 by 0.083% and A-v1 by 0.036%; source-aperture
extension 0.06%/0.01%; exact Hankel vs asymptotic 0.031%. Idealization 11's
"fifth consecutive cycle" framing should be updated to "run for the two
informative legs; settling ruled out as the A-v4 confound," not repeated.

**Credit where it is due, and it is substantial.** Block C's
`ratio_∞ = 1/(1−a·f)`, memory ⟺ `D/τ_k < ln(21f)` is the cycle's real
scientific content: it converts Amendment 3's five-host empirical list into one
dimensionless number with a mechanism, verified at **250/250** duration-scan
points, with **exactly** zero (`|ratio−1| = 0.0`, not "small") at all 30
negative controls and all 7 memory point-runs confined to the UNOBTANIUM
corner. Four seats re-derived it independently and found nothing wrong; I did
not either. It vindicates my own Iteration-15 tempering of Amendment 3 and is
the one result I would cite outside this cycle. **`REALIZABILITY_MEMO.md`
Amendment 5 was actually written, in the same commit as the results
(`460f018`)** — the specific failure that made Iteration 21's non-firing
conditional did **not** recur, and MATERIALS, THERMO and VISION each verified
the live file rather than the claim about it. Block B's arithmetic survives two
independent hand re-derivations with zero defects. The prediction freeze is
structural and real (`a7eaaf8` contains `run.py` + `predictions_frozen.txt` +
stage 16 and **no** `results.json`). And **the Iteration-22 hardened rule is
satisfied: QUANTUM's aperture-consistent check ran.** No automatic criterion-4
firing on that count.

---

## 8. MANDATORY-FIX DOCKET — same shift, adoptable verbatim

*All zero new FDTD cost except where noted; the corrected comparator in items
1–2 is already derived, cross-validated two independent ways, and FDTD-verified
at three configurations in this audit.*

### TIER 0 — criterion-4-conditional (§6.3)

1. **Repoint stage-16 gate (b)'s comparator.**
   `lab/validation/run_all.py::stage16_oblique_gaussian_source::exact_center`:
   divide the propagated angular spectrum by `k_x` (line-current Green's
   function, matching `lab/fdtd2d.py:232-237`) and reduce with
   `Sx = Re(E·conj(H))`, `H = F⁻¹[(k_x/k)·Ê]` (matching
   `ambient.observer_profile`, a flux). **Re-bar at ≤1.5% of the beam
   half-width** (measured engine accuracy 0.459%; 3× margin, stage 10's
   convention). **Free acceptance test, mandatory:** the corrected function must
   reproduce exp-042's own committed `_G0_for` + `field_and_h` for the identical
   aperture — measured here at **991.675 vs 991.645 (0.030 cells)** and
   **91.587 vs 91.576** half-width. Add a peak-estimator `[info]` line
   (exact peak 976.56, FDTD peak-cell 977.0, ray optics 979.12 = 2.56 cells)
   so the ray-optics comparison is made against the estimator ray optics
   actually predicts.
2. **Fix `run.py::exact_angular_spectrum_center` identically, and file a
   flag-don't-rewrite `phase5_erratum` key** (exp-042 precedent) correcting the
   S16-b attribution from 8.03/4.95 (62/38) to **12.556/0.418 (96.8/3.2)**,
   with the estimator/skew decomposition (≈10.4 / ≈2.6 / ≈0.4 cells). NOTES.md
   Learned #2 and idealization 2 get the flag, not a rewrite. Record that the
   shipped 8% bar would have **FAILED at 9.38%** at Block A's own FWHM=20°/40°
   cell where the engine's true error is 0.38% (verified by new FDTD here).
3. **SUPERSEDED banner on `experiments/046-.../phase1_proposal.md`**, in
   exp-045's own form (`f48de18`), naming: "eye-invisible" (§1 line 46,
   P-TH23-B3 line 342), §2.1's geometry table, §1's N_F range, idealizations 2
   and 4, the "sourced" silicon label, and predictions A3/A4/A7. **Correct
   `NOTES.md:14-15`** to "struck from every live artifact and every committed
   result; the Phase-1 draft is preserved unedited under a SUPERSEDED banner
   (T10's flag-don't-rewrite convention)." **Correct the `NETD_DISCLAIMER`
   constant** so its 2672 instances read "...no 'eye-invisible' claim is made
   in any committed result of this cycle," not "anywhere in this cycle."
4. **Repair the item-24 hardened rule and give it ONE rendering.** Strike the
   "or with an explicit renewed-deferral reason that itself survives a Phase-2
   Red Team audit" carve-out; restore "and no further one-cycle extensions via
   prose"; strike the false "mirroring the aperture-check rule's own wording
   exactly"; add VISION's sentence verbatim: *"A Phase-2 Red Team audit blessing
   a renewed deferral does NOT satisfy this rule: Iteration 23's own deferral
   was Red-Team-blessed, and that is what tripped it."* Write the final text
   into `results.json` **as a string**, and propagate that same string verbatim
   to `NOTES.md` and to LOGBOOK's Iteration-23 close.
5. **Propagate A1's withholding to the record that gets cited.** Add
   `"gate_backing": "NOT GATE-BACKED — S16-b (pointing) FAILED; estimator
   reading, not a validated measurement; P-TH23-A6's withholding clause applied
   in scope, see block_a_fdtd.gate_disposition"` to A1's prediction dict; print
   `gate_disposition` to console immediately after the gate table; restate the
   scorecard cell as **"WITHHELD — not gate-backed (S16-b FAILED)"**; and drop
   A1 from the PARTIAL count (scorecard → 11 CONFIRMED / 2 PARTIAL / 1 WITHHELD
   / 1 REFUTED / 2 DROPPED). *Once item 1 lands, the honest end state is to
   restore A1 as an explicitly-labelled desk geometry reading — the pointing
   chain is then validated to 0.418 cells.*

### TIER 1 — mandatory same shift

6. **Scope the "permanent T21 fact" before it enters LOGBOOK.** The identity
   `w₀/cosθ₀` is a statement about the effective aperture's **central lobe**. At
   all 9 FWHM=20° cells `beam_divergence_coherent` synthesises a three-lobe
   comb: replicas at ±433/578/722 cells (450/600/750 nm), amplitude 0.440,
   carrying **41.7–68.0%** of the aperture's intensity outside ±3·w_line
   (measured here; QUANTUM's 42–67% confirmed to the printed digit). It is
   **not** a single transverse mode there.
7. **Replace A3's "(taper truncation)" attribution** in `results.json`'s band
   string and in Attack 2's text with QUANTUM's zero-free-parameter term
   **`w_meas/w_line = 1/√(1 − 4σ_θ² tan²θ₀)`** (0.783% predicted / 0.781%
   measured at FWHM=10°; 3.248% / 3.252% at FWHM=20°). Truncation is refuted:
   at FWHM=20° the Gaussian is cut at 21–36 waists (e^{−441}), and including
   the taper moves the lobe fraction only 67.1%→66.6%. **This corrects my own
   Phase-2 parenthetical.** Record QUANTUM's accompanying residual cubic phase
   (0.009/0.048/0.088 rad at FWHM 2/10/20°): the synthesised mode is slightly
   aberrated even in its core.
8. **Restore A4's mechanism.** The 41-point angular aliasing is real:
   n=41→401 moves the scored `C_empty` by up to **4.473%** (450 nm/36°/FWHM=20°,
   measured here). A4 was dropped correctly on its 5–20% band and incorrectly
   on its premise. Record that `gaussian_angle_weights(n=41)` has **never had a
   convergence check** in this program's history — new open item.
9. **Re-issue A5 in the conditioned currency.** Add a `1+C` column and per-leg
   conditioning amplification (0.1× / 299× / 74× / 0.1×) beside the C column.
   Restate Learned #1: *the propagator reproduces FDTD to **≤0.80%** at
   N_F ≈ 54–66 and to **≈8.4%** at N_F ≈ 0.5–2.2, where the reduction is
   ill-conditioned by 74–299× and should not be quoted in C.* State that
   `_G0_for`'s validity parameter is **kr**, not N_F.
10. **Correct idealization 2's "consequently" clause** to what the data
    supports: dispersionless medium and λ-invariant emitter, but `N_F ∝ λ_cells`
    and the reading is strongly chromatic — **4 of 36 cells read positive C**,
    a sign reversal across the visible band at FWHM=2°. Flag that A1's own
    "C → −1 regardless of coherence" statement is contradicted at those cells.
11. **Correct idealization 4's statement**: the unaimed rim **amplitude**
    (9.99×10⁻³) is *above* `C_THR`=0.005; only the intensity (9.98×10⁻⁵) is
    below — and comparing a source-plane field residual to a Weber contrast
    threshold is a category error in either direction. Carry `C_THR_COMMENT`
    verbatim here (VISION's V4: the docket's own re-authored sentence recreated
    the defect the same docket fixed at A1).
12. **Correct the `--only` erratum in `VALIDATION.md` and NOTES Learned #5
    before it reaches LOGBOOK.** The regression is real for invocations made
    after `6082e02` (2026-08-17); **no cited invocation postdates it** — all
    five `--only 12346789,10,11` citations (SESSION_LOG lines
    1026/1155/1253/1347/1455) are dated 2026-08-14/15 and selected the intended
    ten stages under the code in force. Keep the `--only 16` and `--only 12`
    halves, which are correct.
13. **State the docket-21 override explicitly** ("C1/C4 issue no detectability
    claim; block-scope key carries it") per this program's own rule that an
    overridden docket item is stated as overridden; and **correct idealization
    10's per-point claim**: 2672 keys, not 2496+42+250 — the 250 duration-scan
    points carry no NETD classification and need none.
14. **Write T23's disposition somewhere durable.** A `t23_disposition` key in
    `results.json` and a Learned item in `NOTES.md`, carrying the **argument**
    (power on `w_on` per `RATIO_ON`'s own calibration; conduction and mass on
    `r_out` per Nu=2's derivation requirement) plus the honest split: the
    operative below-vs-above-25 question is decided robustly (97×–19418× across
    every disclosed shape and fill variation), the nominal length question is
    decided by argument, not measurement.
15. **Attach the validity conditions to the fill-factor disclosure.** Add
    `biot_number` and `knudsen_number` per row to `rho_cp_sensitivity` under a
    stated mixing rule, and one sentence to `fill_factor_disclosure`, NOTES
    idealization 7 and Amendment 5(b): *a fill factor below unity also lowers
    κ_eff, raising Bi = k_air/κ_eff toward unity (0.25 / 0.75 / 0.97 at
    φ = 0.5 / 0.1 / 0.01, Maxwell–Garnett) and invalidating the lumped single-τ
    model the sensitivity row's own numbers come from; the ΔT classification is
    unaffected (internal gradients make the radiating surface cooler, not
    warmer), the τ_thermal numbers are.*
16. **Add MATERIALS' emissivity row with the corrected magnitude.** The
    radiative channel is **0.0463%** of `dP/dT`, so ε→0 inflates `dt_ss` by
    **1.000463×** and the mixed-regime margin moves 607.33× → **607.05×**;
    `netd_disposition`'s `emissivity_correction` is a multiplier on ΔT, so on
    the detector side lower emissivity is strictly conservative. **Record the
    computed number, not MATERIALS' "~4×" estimate**, which is wrong by ~4
    orders of magnitude in the safe direction.
17. **Tag P-TH23-B1 as a desk-verifiable structural identity** in the scorecard,
    matching how A1/A3 are tagged: τ_thermal contains no power term and "mixed"
    is *defined* as `r_out`-conduction, so bit-identity cannot fail. Same
    species Attack 2 struck one block over; Phase 3 already says "a
    reproduction, not a fresh finding," one document upstream of the one that
    gets cited.
18. **Record QUANTUM's Iteration-20 conjecture accurately** per §2.4: premise
    REFUTED at 27 cells, partially vindicated at the 9 FWHM=20° cells;
    prediction REFUTED at all 36, at the desk; "mis-posed" reserved for
    P-TH23-A1 as a scored metric.
19. **Open a new live thread — the `C_empty` channel's absorbing-boundary
    systematic.** `ABSORB` 40→60 moves C by **+0.0070** at A-v4 (1.39× C_thr,
    gap-to-desk 5.68%→1.43%) and **−0.0022** at A-v1 (gap 1.91%→3.69%, i.e.
    *away* from the desk value) — real at both legs, not a monotone convergence.
    `ABSORB = 40` with `SRC_X = 300` and `PLANE_X = 77` is inherited unexamined
    by every T21/T16 reading since exp-041. Record EM's finding **as narrowed
    here**, not as "the residual is explained."
20. **Standing rule (EM's, adopted and hardened).** A post-freeze change to a
    trust-suite gate's **target** — as opposed to its bar or its reporting — is
    a physics change and requires an independent second derivation, from a
    different route, before it is committed. **Shipping one without that
    derivation fires Checkpoint criterion 4 automatically at the next Phase 5
    that finds it.** Record alongside Iteration 19's own warning that same-shift
    correction "should not be read as establishing same-shift correction is
    generally safe from criterion 4."

### TIER 2 — ranked priorities for Iteration 24

1. **VISION's glare/adaptation Tier-W sidecar**, under the *corrected* hardened
   rule (item 4), run by any lead seat. Outranks everything on program-integrity
   grounds. VISION's §3 is the finding that unblocks it: **every input is
   already committed** — Iteration 1's Phase-5 parameter set (distance, lumens,
   candela, stray-light E, ambient classes, glare angle θ(t), Stiles–Holladay
   `L_v = 10E/θ²`, Crawford `L_eq(t)`) plus T2's frozen `C_thr(L)` and
   exp-020's measured `C = −0.686`. Nothing in that list requires a WebFetch.
   Scope it Tier-W-provisional, both exponents, both bars, per-sweep-phase, with
   the evidentiary-tier disclaimer pre-registered at all three loci.
2. **Stage-16 repair's forward half** (beyond item 1's same-shift fix): add
   identity gates at Block A's actual extremes, w₀ = 1.074λ and w₀ = 10.74λ.
   Both current identity gates sit at w₀ ≈ 2λ, and the block's worst A3 residual
   and its whole low-N_F reach live at the ungated end. ~2 FDTD calls.
3. **QUANTUM's n-convergence audit of `gaussian_angle_weights`, then the
   M²/étendue bridge for T21 — in that order.** The convergence audit is minutes
   and zero FDTD; the M² bridge must not run before it, because the family
   interpolates *through* the FWHM=20° regime where the comb is worst. QUANTUM's
   reframing (the two exp-042 columns are M² = 1 and M² = 2.15–35.8 of the same
   scene, the proposal's own `1504/(2w_line)` column being M²) is the one
   Phase-2 finding of that seat's the docket did not carry, and it replaces an
   input nobody can source (a flashlight coherence length, blocking T21 for four
   iterations) with two numbers anyone can read off a torch. **Identity-gate the
   high-M² endpoint against `phase5_erratum.block_beam_corrected` bit-for-bit
   before any intermediate M² is trusted** — QUANTUM's own Gaussian surrogate
   does not reproduce it (−0.0005 vs −0.004006), and that discrepancy is the
   point of the gate.
4. **Design the `ABSORB` sweep for the new thread (item 19)**: sweep ABSORB with
   `SRC_X` moved clear of the x-damping band so EM's ABSORB=80 confound does not
   recur, source span held fixed, all 3λ. ~6–9 FDTD runs.
5. **The R3 resolution check on the four positive-C cells** before "glint at
   750 nm" enters the record as physics (R3's own meta-rule: a surprising
   feature gets the check before the mechanism debate — and a sign reversal
   across the visible band on the axis T21's worst cell lives on is a surprising
   feature).

*Deprioritized, with reasons:* another T21 FDTD cycle (its live question is the
M² / partial-coherence bridge, item 3, not more field solves); a program-wide
re-audit of past `C_empty` citations for the `exact_center` convention error
(that function is new this cycle and touches no historical row — the ABSORB
systematic, item 4, is the one that does reach back); the settling-margin test
as a standalone (EM ran it for the two informative legs: 0.036%/0.083% at 3×
STEPS — credit it and close idealization 11 for those legs rather than deferring
a sixth time).

---

## 9. VERDICT RECOMMENDATION

# PARTIAL

**Raw seat count: 5 PARTIAL + 1 PROMISING** (MATERIALS, explicitly scoped to its
own charter and correct within it — every realizability item it was tasked to
verify checked out on the live files). Per this program's own established
precedent (Iterations 9, 10, 12, 17, 21, 22), the verdict turns on whether the
cycle's own open questions closed, not on the count.

**What closed cleanly.** The Iteration-22 hardened rule is satisfied — the
aperture-consistent check **ran**, and no automatic criterion-4 firing attaches.
`profile="gauss"`, declared since the bench was built and never once exercised,
is now trust-gated by two legitimate absolute identity gates (a and d), and the
oblique source-width convention `width = w₀/cosθ₀` is right — I re-derived it
from the angular spectrum independently of Attack 1b and confirmed it against
FDTD at four (width, θ₀) points. exp-042's desk Huygens–Fresnel propagator is
now FDTD-backed outside its construction regime, honestly at ≤0.80% at
N_F ≈ 54–66. Block C's `D/τ_k < ln(21f)` is a genuine advance: a five-host
empirical list replaced by one dimensionless criterion with a mechanism, verified
250/250, exact zeros at 30 negative controls, all memory confined to the
UNOBTANIUM corner — and it vindicates my own Iteration-15 tempering of Amendment
3. `REALIZABILITY_MEMO.md` Amendment 5 was actually written in the shift that
promised it: Iteration 21's specific failure did **not** recur. Block B's
arithmetic survives two independent hand re-derivations with zero defects, and
no UNDETECTABLE classification anywhere is threatened by anything any seat
found — worst case, computed here, 607.33× → 607.05×. The prediction freeze is
structural and real.

**What did not close.** The cycle's advertised Block-A headline was never an
experimental question, and the identity that replaced it was recorded with the
wrong scope (9 of 36 cells are not single-mode), the wrong residual attribution
(taper truncation, twice committed — my own error), and an instruction to write
it into permanent memory unqualified. Its one genuinely falsifiable prediction is
2 informative legs and 2 conditioning artifacts by the cycle's own disqualifying
criterion. **A trust-suite gate shipped into `lab/` scores the engine against a
physically wrong comparator, understating the engine by 12×, running ~17× too
loose where it was calibrated, and mis-firing at 9.38% against its own 8% bar
inside the block it certifies.** T21's contamination-risk verdict is exactly
where Iteration 19 left it — arguably further, since the framing that could
produce one was retired and the reading that bears on it was withheld into a
prose paragraph. T23 has a third endpoint and still no ruling, its argument
living only inside an unbannered Phase-1 draft. And four instances of this
program's own named fix-docket-delivery pattern reproduced in the cycle
immediately after the one that invented the remedy for the sharpest of them.

**Not RULED OUT:** nothing here is refuted, every defect is a sharpening, and
the engine comes out of this audit *better* validated than the record says.
**Not PROMISING:** a green gate calibrated against a wrong reference is exactly
the class of defect this program's Phase-5 culture exists to catch, and no live
thread advanced.

**Checkpoint: criterion 4 does NOT fire, conditional on Tier 0 (§6.3); no other
criterion fires.** If the Director overrides to PROMISING, the override should
state which of §9's four unclosed items it considers closed.

---

## Verification appendix — what I actually ran

- `rt_s16b.py` — exact non-paraxial angular-spectrum propagation
  (`k_x = √(k²−k_y²)`, evanescent clipped, n_fft = 2²², span 6×10⁴) of
  `exp(−(Y/w)²)exp(ik sinθ₀Y)` over Δx = 223, in **all four**
  source-model × reduction combinations. Produced §1.2's table.
- `rt_fdtd.py` — **two new full 1400-step FDTD runs** (`lab.fdtd2d.Sim`,
  `profile="gauss"`, θ₀ = 40°, cpl = 20, exp-041/042 committed geometry) at
  `width` = 40 and 56.063. Measured 992.0927 / 90.9881 / peak 977.0 and
  984.9512 / 80.4715 / peak 981.0 — bit-identical to `results.json`, a fourth
  independent execution of the determinism claim.
- `rt_extreme.py` — **one new FDTD run** at `width` = 28.03 (Block A's FWHM=20°,
  θ₀ = 40° cell): 1005.549 / 120.776. Produced §1.3's gate mis-fire result
  (9.38% vs the shipped 8% bar; 0.38% against the correct comparator).
- `rt_g0.py` — exp-042's own committed `_G0_for` + obliquity-on-H + `Sx =
  −Re(E conj H)` with a Gaussian aperture at three widths. Produced the
  991.645 / 984.688 / 1005.164 cross-validation.
- `rt_absorb.py` — **four new FDTD runs**, `ABSORB` ∈ {40, 60} at A-v4 and A-v1,
  each against its own desk-propagator prediction. Produced §7's boundary table.
- `rt_lobes.py` — effective-aperture lobe census of
  `Σ_i √w_i e^{ik sinθ_i Y}` from the actual `gaussian_angle_weights`, all 36
  cells, with and without the real taper `P`. Produced §2.1.
- `rt_nconv.py` — n = 41 vs n = 401 convergence of `beam_divergence_coherent`'s
  scored `C_empty`, all 36 cells. Produced §2.3's 4.473%.
- Arithmetic checks: 4εσT³ vs h_eff at ε ∈ {0.9, 0.09, 0.009, 0}; Maxwell–Garnett
  κ_eff and Bi at φ ∈ {1, 0.5, 0.1, 0.01}; the three headline NETD margins
  (607.33× / 6681.0× / 1214.7×); QUANTUM's `1/√(1−4σ_θ²tan²θ₀)` at FWHM 10°/20°.
- `results.json` (3,210,029 bytes) queried programmatically, never dumped:
  string counts (`withheld` 0, `gate-backed` 1, `gate_backing` 0,
  `netd_disclaimer` 2672, `T23` only in two regime labels); A1's full prediction
  dict; A5's four legs in both currencies; `conditioning_amplification`
  327.3/81.6; the 36-cell `C_empty_propagator_unaimed` grid;
  per-point disclaimer coverage 2496/2496, 42/42, **0/250**.
- Direct reads: `lab/fdtd2d.py:132-172, 225-245`; `lab/ambient.py:30-60`;
  `lab/sections.py:79-88`; `lab/thermo_sidecar.py:140-225`;
  `lab/validation/run_all.py:1194-1400`; `lab/validation/VALIDATION.md:40-60`;
  `experiments/042-.../design_geometry.py:110-360`; `PANEL.md` in full;
  `LOGBOOK.md` RULED OUT / ESTABLISHED / LIVE THREADS T1–T23 in full and
  Iterations 17–22 in full; the complete exp-046 record.
- Git: `git log`/`git show` on `experiments/046-*/phase1_proposal.md` (one
  commit, `8950125`, no banner), `experiments/045-*/phase1_proposal.md`
  (`f48de18`, banner present), `lab/validation/run_all.py` (exact-match
  selector introduced at `6082e02`, 2026-08-17), and extraction and execution of
  the pre-`6082e02` `_stage_selected` against every historical `--only`
  citation.
- **Ruled-out check:** nothing in this audit or in exp-046 resurrects R1, R2 or
  R3; the R3 meta-rule is invoked *for* the positive-C cells (Tier 2 item 5) and
  for QUANTUM's point that the S16-b "artifact" claim skipped its own R3 check.
