# PHASE 5 — REVIEW · QUANTUM OPTICS · Panel Iteration 23 (exp-046)

*Fresh context, blind to the other five seats' Phase-5 reviews. Charter:
non-classical absorption, state-dependent or coherent interactions;
expressibility contract — mechanisms enter the bench only as effective
classical parameters, or Red Team strikes them.*

*Disclosure of interest, stated first because it colours everything below:
**Block A is this seat's own Iteration-19/20 proposal**, and Red Team's Attack 2
rules on **this seat's own Iteration-20 conjecture**. I have therefore re-derived
Attack 2 from scratch on my own angular-spectrum reasoning before reading Red
Team's algebra as anything but a claim, and I have re-run every number I cite.
Scripts: `q_check.py`, `q_lobes.py`, `q_c.py`, `q_irr.py`, `q_m2.py`,
`q_phase.py` (scratchpad); one live `python -m lab.validation.run_all --only 16`.*

---

## 1. My reading of the results

### 1.1 I independently re-derived Attack 2. The algebra is right — for the central lobe, and only for the central lobe.

Red Team's proof is correct and I reproduce it without using its steps.
`beam_divergence_coherent` (`042/design_geometry.py:337-355`) forms
`E_tot = Σ_i √w_i (G @ _src_amp(θ_i))`. `G` is a fixed matrix, so by linearity
the whole angular sum can be pulled back to the source line:

> `E_tot = G @ [ P(Y) · Σ_i √w_i e^{i k sinθ_i Y} ]`, `Y ≡ y − OBJ_Y`

so the object being propagated is an **effective aperture**
`A_eff(Y) = P(Y)·Σ_i √w_i e^{i k sinθ_i Y}`. `w` is Gaussian in θ with
`σ_θ = FWHM/2.3548` (`:313`), so `√w` is Gaussian with `σ' = √2 σ_θ`. Taking the
sum to its integral and linearising `sinθ ≈ sinθ₀ + cosθ₀ δ`:

> `∫ e^{−δ²/2σ'²} e^{i k cosθ₀ δ Y} dδ ∝ exp(−k²cos²θ₀ σ'² Y²/2) = exp(−(k cosθ₀ σ_θ Y)²)`

⇒ 1/e **amplitude** half-width `W = 1/(k cosθ₀ σ_θ)`. And
`w₀ ≡ 2√(2ln2)λ/(2πΔθ) = 2√(2ln2)/(k·2.3548·σ_θ) = 1.0000085/(k σ_θ)`, so
`W = w₀/cosθ₀` to 8.5 ppm. **Attack 2's identity holds.** Measured myself over
all 36 cells: 0.022 %–0.78 % at the 27 FWHM ≤ 10° cells, 2.60 %–3.25 % at the 9
FWHM = 20° cells — reproducing `results.json`'s A3 numbers
(0.0224593…/0.7809178…; 2.6047698…/3.2524510…) to every printed digit. I also
confirm A3's check uses the **right** coherent-sum convention: `run.py:203-227`
weights by `√w`, ramps with `sin θ`, and measures on `Y_SRC − OBJ_Y` — exactly
`_src_amp` minus the taper `P`, and I verified that including `P` changes the
measured half-width by **0.0000 cells** at every cell tested. Because the
effective aperture is upstream of `G`, A3 as restated is also **immune to the
obliquity-on-E / corrected-E-H convention dispute** (Attack 8) — a genuine
improvement over the Phase-1 form, and worth recording as such.

**But the identity is a statement about the core, and at 9 of 36 cells the core
is a minority of the aperture.** The 41-point angular grid has spacing
`δθ = 0.125·FWHM`, which by the same Fourier relation puts **grating-lobe
replicas** on the effective aperture at `ΔY ≈ λ_cells/(cosθ₀ δθ)`. At FWHM ≤ 10°
that spacing (850–5984 cells) exceeds the 752-cell aperture half-span and
nothing appears. At **FWHM = 20° it is 425–748 cells — inside the aperture at
all three wavelengths**. Measured (`q_lobes.py`), at every one of the 9
FWHM = 20° cells:

| λ | replica position (measured) | replica amplitude | **fraction of aperture intensity outside ±3 w_line** |
|---|---|---|---|
| 450 nm | ±433 | 0.440 | **67.1 %** |
| 600 nm | ±578 | 0.440 | **64.3 %** |
| 750 nm | ±722 (±712 with taper) | 0.440 (0.438) | **48.1 % (41.7 % with taper)** |

So at those 9 cells `beam_divergence_coherent` does **not** synthesise "a
Gaussian aperture of 1/e half-width `w₀/cosθ₀`". It synthesises a three-lobe
comb, of which the `w₀/cosθ₀` Gaussian carries only 33–58 % of the energy. The
docket's item 5 instructs the Director to "**record in LOGBOOK that
`beam_divergence_coherent` synthesises a Gaussian aperture of half-width
`w₀/cosθ₀` — a permanent T21 fact**". As written that sentence is true at 27
cells and materially false at 9, and it is about to enter this program's
permanent memory unqualified. **It must be scoped before it is written.**

### 1.2 Both committed explanations of A3's own residual are wrong. Here is the right one.

`results.json`'s A3 band string reads "… ≤ 4 % at all 9 FWHM = 20° cells
**(taper truncation)**", carrying Red Team's Attack-2 parenthetical. NOTES.md
idealization 15 attributes the *excess over* that to integer-grid quantization.
Neither is the cause of the residual itself.

Taper truncation is refutable by inspection: at FWHM = 20° `w_line` is 21–35
cells against a 752-cell half-aperture — the Gaussian is truncated at **21–36
waists**, i.e. at `e^(−441)`. And I measured it directly: half-width with taper
vs without is **identical to four decimals** at every cell (`q_phase.py`).
Truncation is a live concern for the FWHM = **2°** cells (`w_line` up to 350,
half-span 752 → 2.1 w_line), which is a different set of cells entirely; Attack
6 is about those. The two got crossed.

The real term is the **second order of the `sinθ` expansion**, which nobody in
the cycle kept. Retaining `sinθ ≈ sinθ₀ + cosθ₀δ − ½ sinθ₀ δ²` makes the
Gaussian integral's width parameter complex, `a = 1/2σ'² + i k Y sinθ₀/2`, and
gives

> `|A_eff(Y)| ∝ exp[ −(Y/W)² / (1 + u²) ]`, `u = 2 σ_θ tanθ₀ · (Y/W)`

so the 1/e crossing moves out by exactly

> **`w_meas/w_line = 1/√(1 − 4σ_θ² tan²θ₀)`**

Zero free parameters. Predicted vs measured, all 36 cells: FWHM 2° → 0.023 %
vs 0.023 %; 5° → 0.145 % vs 0.153–0.191 %; 10° → 0.585/0.677/**0.783** % vs
0.628/0.699/**0.781** %; 20° → 2.404/2.796/**3.246** % vs 2.605/2.898/**3.252** %.
The θ₀-ordering, the FWHM-ordering and the two headline numbers A3 is scored on
(**0.78 %** and **3.25 %**) all fall out of one closed form. Two consequences:

1. The identity is **tighter than the record says** — once the `sinθ`
   nonlinearity is carried, the deviation is not a tolerance, it is a computed
   term. A3's committed band should be re-stated against
   `w_line/√(1 − 4σ_θ²tan²θ₀)`, at which point the residual is <0.05 pp.
2. The same complex `a` carries an **imaginary** part — a residual (cubic-in-Y,
   coma-like) phase across the synthesised aperture, measured at 0.009/0.048/
   0.088 rad over `|Y| ≤ w_line` at FWHM 2/10/20°. Small, but it means the
   synthesised mode is not a pure diffraction-limited waist even in its core:
   it is a slightly aberrated mode. That is a charter-relevant statement about
   what the "coherent column" actually is, and it is not in the record.

### 1.3 Is "mis-posed" the right verdict on my own Iteration-20 conjecture? No. It was **refuted**, and the record should say so.

I want to be harder on my own seat here than Red Team was, because a generous
ruling on a seat's own prior claim is exactly the failure mode the panel exists
to prevent.

My Iteration-20 conjecture had two parts, both definite:

- **(a) the diagnosis** — exp-042's coherent column is "an artifact of holding
  the FULL ~75 λ aperture fixed while imposing an angular power spectrum on it",
  a deliberately BEAMFORMED array, physically different from a naturally
  divergent single-mode emitter whose aperture would be "3–30× smaller".
- **(b) the prediction** — an aperture-consistent single-mode beam is
  "predicted to land much closer to the incoherent reading".

Attack 2 shows (a) is **factually false**: the coherent sum self-apodises, the
full aperture is *not* effectively held fixed, and the object exp-042 built is —
in its core — the diffraction-limited single mode I said it was not. (b) follows
(a) down: the aperture-consistent reading is 36/36 above `C_THR`, 35/36 at ≥20×
the incoherent value, min |C| = 0.03227 — I reproduce all three. That is not an
ill-posed question that dissolved on inspection. It is a well-posed claim about
a computable quantity, computed, and coming out the other way.

**"Mis-posed" is a category error dressed as charity toward my seat.** Being
decidable at the desk makes a claim *cheap to refute*, not *unfalsifiable*; this
program's own precedent (T15's chord model, T22's area-invariance proof, exp-045
Block B's sign-flip catch) records desk-decidable refutations as refutations.
Red Team also conflates three distinct objects under one word: Attack 2 kills
the *headline* as an identity, Attack 7 kills *P-TH23-A1 as a scored metric* as
a pointing tautology, and the synthesis then applies "mis-posed" to *my
Iteration-20 conjecture*. Only the middle one is genuinely mis-posed. The honest
three-line ledger for LOGBOOK is:

- QUANTUM's Iteration-20 **premise** (beamforming/full-aperture diagnosis):
  **REFUTED** by Attack 2's identity, independently re-derived at Phase 5.
- QUANTUM's Iteration-20 **prediction** ("lands near the incoherent column"):
  **REFUTED**, at the desk, at zero FDTD cost.
- **P-TH23-A1 as a scored metric**: mis-posed (a pointing tautology, Attack 7).

Recording my conjecture as "mis-posed, not refuted or confirmed" leaves a wrong
diagnosis of the exp-042 machinery *unmarked* in the memory the next cycle
reads. I ask the Director to record it as refuted, with my seat named.

**One part of my Iteration-20 framing survives, and it is the useful part.** The
self-apodisation argument applies to the **coherent** sum only. The *incoherent*
column really does hold the full 1504-cell tapered aperture fixed for every
angular component — there is no coherent sum to apodise it. So the two exp-042
columns are not "coherent vs incoherent" at all: they are **two different
beam-quality factors of the same physical scene**, M² = 1 versus
M² ≈ aperture/w₀ = 2.15–35.8 — which is precisely the proposal's own
`1504/(2 w_line)` column, never identified as M² by anyone. I raised this at
Phase 2 (attack item iv, the étendue point); it was the one Phase-2 finding of
mine the docket did **not** adopt, and `grep` confirms no "M²"/"étendue"/"Schell"
framing survives anywhere in Block A's `run.py`, `results.json`, or NOTES.md
outside idealization 3's disclaimer. That omission is what leaves T21's
contamination question stranded on an unbuildable "sourced coherence length"
when a one-parameter, sourceable formulation was on the table. See §3.

### 1.4 "T1 escape route: NONE" — mostly holds, with two leaks my charter has to name.

Verified for this cycle's own numbers: no material law is touched, no update
coefficient moves, the only σ anywhere is the fixed linear `SIGMA_SPONGE` in the
two non-scoring object legs, `add_line_source` only appends to `Sim.sources`, and
the scene stays strictly LTI. Constraint-3 leakage was correctly caught (Attack
11's "eye-invisible" strike) and the `C_THR` disclaimer is carried verbatim. On
its own terms the statement is honest.

Two forward hazards this cycle **creates** and does not flag:

**(i) The illumination model is now a free parameter that multiplies intensity
by up to an order of magnitude — and T1's leading escape route is intensity-
gated.** At fixed *total emitted source power*, swapping the bench's tapered
top-hat for the aperture-consistent single mode raises the **peak flux at the
observation plane** by (measured, `q_irr.py`, θ₀ = 40°):

| λ | FWHM 2° | 5° | 10° | 20° |
|---|---|---|---|---|
| 450 nm | 4.16× | 9.88× | 12.37× | 7.80× |
| 600 nm | 3.09× | 7.52× | 10.83× | 7.60× |
| 750 nm | 2.46× | 6.06× | 9.53× | 7.41× |

Nothing this cycle claims depends on that. But `REALIZABILITY_MEMO.md`'s live
UNOBTANIUM verdict for TPA is a **9–12 order-of-magnitude irradiance gap**, and
the moment a σ(I) cycle adopts "the physically correct single-mode illumination"
it silently buys back 0.4–1.1 of those orders. That is a legitimate modelling
choice *if declared*; it is an escape-by-illumination-model if it arrives
unlabelled inside an instrument upgrade. **Recommend a standing rule**: any
future run that changes the illumination model and scores an intensity-dependent
quantity must report the peak-irradiance-at-fixed-power ratio against the
tapered-top-hat baseline, in `results.json`, at the point of claim.

**(ii) The same change would invalidate `w_on`, which Block B's own T23
resolution rests on.** `w_on = σ_ext·dx` is measured under broad, quasi-plane-wave
illumination. The aperture-consistent mode at FWHM ≥ 10° has `w_line` = 21–70
cells against `r_out = 78` — the beam becomes **narrower than the object**, which
changes the absorbed-power distribution and hence the measured extinction width
that defines `w_on` and calibrates `RATIO_ON`. Blocks A and B are independent
*this* cycle, so nothing is wrong here; but T23's whole `w_on`-vs-`r_out`
question is posed in an illumination regime Block A has just proposed replacing,
and the two blocks are presented in NOTES.md as "one coherent chain". Name it.

### 1.5 Smaller findings, verified

- **A5's "CONFIRMED 4/4 — the cycle's genuine falsifiable Block-A content" is
  really 2 informative legs plus 2 saturated ones.** Weber contrast is bounded
  below by −1 whenever both window means share a sign. A-v2's prediction is
  −0.99666, so the **largest negative-side deviation physically available is
  0.335 %** against a 15 % band; A-v3's is 1.36 % against 35 %. Attack 7's own
  tautology argument — the object window sits in the beam's wing, the +flank
  sits under the beam, `C → −1` regardless — applies verbatim to A-v2/A-v3, and
  Red Team did not carry it there. The two legs that could genuinely move are
  A-v1 (1.91 %) and A-v4 (**5.68 %**, the worst, at 750 nm, the wavelength with
  the thinnest causal-transit margin and the fifth consecutive deferral of the
  settling-margin test). The propagator validation is real; "4/4" overstates it.
- **P-TH23-A4 was dropped on a wrong premise.** Red Team dropped A4 because
  "there is no divergence to explain". A4's *mechanism* — 41-point angular
  sampling aliasing — is exactly right and I measured it: comparing
  `beam_divergence_coherent` at n = 41 against n = 401 moves the scored
  `C_empty` by up to **3.18 %** (450 nm/36°/FWHM 20), 0.28–1.41 % at the other
  FWHM = 20 cells, and <0.08 % everywhere else (`q_c.py`). A4's *magnitude band*
  (5–20 %) was wrong; its physics was not. The reason the effect is small in the
  scored scalar is geometric luck — the replicas radiate to y ≈ 401 and 1557,
  outside both the object window (714–870) and the flank windows (529–607,
  977–1055) — not absence of aliasing.
- **The S16-b diagnosis is an artifact claim that skipped this program's own R3
  check.** R3's inherited meta-rule is explicit: *"any surprising feature gets a
  resolution check before it gets a mechanism debate — and 'artifact' claims need
  the check too."* NOTES.md rules "the failure is in the gate's *target*, not the
  engine". The committed numbers say both: target off by **+8.03** cells, and
  then FDTD off by a further **+4.95** cells from the exact answer (and **+2.26**
  at A-v2's 10°). Same sign, growing with divergence — the signature of Yee
  numerical dispersion (angle-dependent `k_num`), which is a resolution-testable
  hypothesis (`(k dx)²` ⇒ cpl 20→30 should shrink it ≈2.25×) and was not tested.
  "Not the engine" is not established.
- **Stage 16 re-run independently here: 4/4, 77 s.** S16-a 1.06 %, S16-b amended
  gate 5.44 %, S16-c 6.96×10⁻¹⁵ relative, S16-d 1.25 %. The trust claim holds.
  Scope note for the record: `profile="gauss"` is now gated for **free-space
  divergence, oblique pointing and oblique width only** — it has never been
  exercised under a gate with an object present (A-o1/A-o2 are explicitly
  non-scoring), nor with ≥2 concurrent sources (exp-029's Q1/Q2 identities), nor
  with a PEC core. The superposition identity is profile-independent by
  construction so the risk is low, but "trust-gated for the first time" should
  carry its scope.
- Blocks B and C: I re-derived nothing new and found nothing wrong. B1's
  τ_thermal independence of `L_power` is algebraically obvious once written
  (`τ = ρC_P L²/(4εσT³L + k_air)`) and the bit-identical 194.17681504141214 is
  the right way to report it. C2's `ratio_∞ = 1/(1 − a f)` collapsing a host list
  to `D/τ_k < ln(21 f)` is the cleanest result in the cycle and the one I would
  cite outside it.

---

## 2. Physical meaning

Strip the docket away and this cycle established three things, in descending
order of durability.

**First: exp-042's two "beam divergence" columns were never a coherence
dichotomy.** They are the two ends of a **beam-quality (M²) axis** of the same
scene. The coherent column self-apodises to the diffraction-limited single mode
(M² = 1); the incoherent column keeps the full 1504-cell aperture while
imposing an independent Δθ (M² = 2.15–35.8). Read that way, the "coherent
reading is 36/36 above threshold, incoherent is 0/36" result stops being a
paradox about coherence and becomes a smooth statement about étendue: a beam
whose emitter is diffraction-limited concentrates enough flux at 223 cells to
dominate the window geometry, and one whose emitter is 2–36× past the
diffraction limit does not. Coherence per se is not doing the work — **the
source's phase-space volume is**. That is squarely this seat's charter and it is
the single most reusable statement the cycle produced.

**Second: the T21 contamination-risk question therefore has a one-dimensional
answer, and the bench already brackets it.** My sketch (`q_m2.py`, a
Gaussian-Schell-like family: a coherent mode of emitted FWHM `Δθ/M²`
incoherently summed over the complementary external spread) gives, at exp-042's
own worst incoherent cell (750 nm/38°/FWHM 2°): |C|/C_THR = 32.7 at M² = 1,
17.0 at M² = 3, 6.3 at M² = 5, 1.4 at M² = 10, 0.18 at M² = 20. The crossover
sits at **M² ≈ 10–20**. A real flashlight — a ~1 mm emitter with ~10° output —
has M² ≈ 10²–10³, two orders past the crossover, and it takes *no* coherence
length to say so: M² needs only emitter width × divergence, two numbers anyone
can read off a physical torch. This is the replacement for the "sourced
coherence length via van Cittert–Zernike" that has now blocked T21 for four
consecutive iterations, and it is not blocked by T18/EGRESS.

**Third — the negative result, and the one that most concerns me:** the
machinery that produced *both* exp-042 columns carries an **unnamed angular
quantization artifact**. The n = 41 Gaussian angle kernel is a comb, and a comb
of plane waves is a comb of apertures. At FWHM = 20° it puts 42–67 % of the
synthesised aperture's energy into grating lobes, and it moves the scored
`C_empty` by up to 3.2 %. This program has spent Iterations 18–23 arguing about
whether the T21 fringe is real physics or sampling; T21's own resolution
(EM's Huygens edge-diffraction model near the angular Nyquist limit) was *about*
being near a sampling limit. Finding a second, independent sampling limit inside
the very kernel used to test the first one is not a coincidence I am comfortable
leaving unexamined, and no gate anywhere covers it — `gaussian_angle_weights`'s
`n = 41` has never had a convergence check in this program's history.

---

## 3. Argued next change

**Build the M² bridge, and gate it on an n-convergence check first.**

The argument, stated so it can be attacked:

1. T21's open question is a single number — does the fringe contaminate a
   near-±40° constraint-3 run? — and it has been blocked for four iterations on
   an input nobody can source (a real flashlight's coherence length).
2. That input is the wrong parametrisation. The physics that decides the
   answer, as §2 shows, is the source's phase-space volume, i.e. M². M² is
   sourceable from geometry alone, and both endpoints of the M² family are
   **already computed and committed** (exp-042's two columns) — exactly the
   "two exact checkable endpoints" discipline this seat pre-registered at
   Iteration 19 and exp-029 established at Iteration 6.
3. It is zero-FDTD and it reuses `_G0_for`/`field_and_h`/`incoherent_sum`
   verbatim. The one design requirement is that the **high-M² endpoint must use
   the bench's actual tapered aperture**, not a Gaussian surrogate, so that it
   reproduces `phase5_erratum.block_beam_corrected`'s committed column
   bit-for-bit as an identity gate before any intermediate M² is trusted. My own
   Gaussian-surrogate sketch does *not* reproduce it (−0.0005 vs the committed
   −0.004006 at the worst cell) — that discrepancy is the aperture shape, and it
   is precisely why the endpoint must be gated rather than assumed.
4. It cannot be run honestly until the n = 41 comb is characterised, because the
   family interpolates *through* the FWHM = 20° regime where the comb is worst.
   Hence the ordering.

What it would settle: T21's contamination-risk verdict, as a function of one
dimensionless number, with a stated crossover and a stated real-flashlight
value — the first single-number answer the thread has been able to produce.
What it would not settle: the `c*` amplitude-scale question (Iteration 19's
still-open 1.62× residual), which multiplies whatever this returns and still
needs the settling-margin FDTD test.

---

## 4. Ranked top-3 candidate directions for Iteration 24

**#1 — The M² (beam-quality) bridge for T21, with a gated high-M² endpoint.**
Zero FDTD, hours of desk work. Replace the unbuildable Gaussian-Schell/
coherence-length route with the one-parameter M² family described in §3;
identity-gate the M² → aperture/w₀ endpoint against exp-042's committed
corrected incoherent column and the M² = 1 endpoint against this cycle's own
Block-A reading; report `|C|(M²)` across all 36 cells at both `c = 1` and
`c = c*`; state the crossover M² and the M² of a physically-specified torch
(emitter width × divergence, geometry only — no scholarly source needed, so
T18/EGRESS does not block it). Deliverable: T21's first single-number
contamination verdict, with its own falsifier (if the crossover lands above
M² ≈ 10³, a real flashlight *is* in the contaminating regime and every
near-±40° constraint-3 run needs a fringe budget).

**#2 — The angular-quantization audit of `gaussian_angle_weights(n=41)`.** Zero
FDTD, minutes. An n-convergence sweep (n = 41 → 101 → 401 → 1001) of **both**
`beam_divergence_coherent` and `beam_divergence_incoherent` across all 36 cells,
plus the effective-aperture lobe census I ran here, committed as data. Measured
here: replicas at 44 % amplitude carrying 42–67 % of aperture energy at all 9
FWHM = 20° cells, and up to 3.18 % movement in the scored `C_empty`. This is the
only kernel in the program's angular machinery that has never had a convergence
check, it is the kernel that produced the columns Iterations 19–23 have been
arguing about, and it is the gate #1 needs. It also fixes the LOGBOOK wording
before "a permanent T21 fact" is written down unqualified (see §5).

**#3 — The R3 resolution check the S16-b diagnosis skipped, doubling as the
cheapest available settling-margin probe.** ~2 FDTD legs. Re-run S16-b/A-v2 at
cpl = 30 and test the numerical-dispersion hypothesis for the residual
FDTD-vs-exact pointing offset (+4.95 cells at 14° FWHM, +2.26 at 10°, same sign,
growing with divergence): if it is Yee dispersion the offset should fall ≈2.25×;
if it does not, the offset is settling or something unmodelled, and either
answer is informative. This program's own R3 meta-rule requires it for an
artifact claim, and the dedicated settling-margin test PHOTONICS and EM have
ranked #1 since Iteration 19 has now been deferred **five** consecutive cycles —
this is the cheapest partial payment on it available.

*(Not ranked, but I endorse them: MATERIALS'/Red Team's Amendment 5 delivery,
and VISION's glare/adaptation sidecar under the hardened Iteration-24 rule the
Director adopted at Phase 3 — that hardening is correct and I would not soften
it.)*

---

## 5. Corrections requested to the LOGBOOK entry before it is written

Stated separately because they enter permanent memory and are cheap to get right:

1. **Scope docket item 5's "permanent T21 fact"**: `beam_divergence_coherent`'s
   effective aperture has 1/e half-width `w₀/cosθ₀` **in its central lobe**;
   at FWHM = 20° (all 9 cells) it additionally carries 41-point angular-sampling
   grating-lobe replicas at 0.44 amplitude and ±425–748 cells, holding 42–67 %
   of the aperture energy, so it is **not** a single transverse mode there.
2. **Replace A3's "(taper truncation)" attribution** — in `results.json`'s band
   string and in Attack 2's text — with the exact term
   `w_meas/w_line = 1/√(1 − 4σ_θ²tan²θ₀)`, which reproduces the measured
   0.023/0.15/0.78/3.25 % at FWHM 2/5/10/20° with zero free parameters, and note
   the accompanying residual (cubic) phase: the synthesised mode is slightly
   aberrated, not a clean waist.
3. **Record QUANTUM's Iteration-20 conjecture as REFUTED (premise and
   prediction), not "mis-posed"**, per §1.3's three-line ledger; reserve
   "mis-posed" for P-TH23-A1-as-a-metric, where Attack 7 earns it.
4. **Record the M²/étendue reframing** (the two exp-042 columns are M² = 1 and
   M² = 2.15–35.8 of the same scene, the proposal's own `1504/(2 w_line)` column
   being M²) — the one Phase-2 finding of this seat's the docket did not carry,
   and the enabling step for #1.
5. **Scope A5**: 2 informative legs (A-v1 1.91 %, A-v4 5.68 %) and 2 whose
   predictions sit at |C| ≈ 0.99 where the band cannot be violated from below
   (max available negative deviation 0.34 % / 1.36 %).
6. **Scope "`profile="gauss"` is trust-gated"**: free-space divergence, oblique
   pointing, oblique width — no object-present gate, no multi-source gate, no
   PEC-core gate.
7. **Add the illumination-model intensity ledger** (§1.4(i)) as a standing rule
   before a σ(I) cycle inherits a 2.5–12.4× irradiance gift unlabelled.

---

## VERDICT: **PARTIAL**

Not PROMISING: the cycle's advertised Block-A headline was correctly demoted to
an identity, and then the identity itself was recorded with the wrong scope (9
of 36 cells are not single-mode), the wrong physical attribution of its own
residual (taper truncation, twice-committed), and the wrong verdict on the
conjecture it retired ("mis-posed" where the record should read refuted). The
one prediction advertised as genuinely falsifiable, A5, is half-saturated. The
cycle's own dropped prediction, A4, was dropped on a false premise — the
aliasing it named is real and measurable.

Not RULED OUT: the instrument work is genuine and I verified it. Stage 16 is
green under my own hand (4/4, 77 s), `profile="gauss"` is exercised for the
first time in the program's history, exp-042's desk Huygens–Fresnel propagator
now has FDTD backing across three orders of Fresnel number, S16-c reproduces
exp-041's committed row to 7×10⁻¹⁵ relative, Attack 2's algebra is correct
where it applies and I re-derived it independently, Blocks B and C are clean,
and C2's `D/τ_k < ln(21 f)` is a real closed-form advance. The Iteration-22
hardened rule is satisfied: the check ran.

What did not close, stated for the record: T21's contamination-risk verdict
(fourth iteration open, and this cycle's re-scoping moved it further from an
answer, not closer, by retiring the framing that could produce one); the n = 41
angular-kernel convergence question (newly opened here); the settling-margin
test (fifth deferral); and the S16-b pointing residual, whose "not the engine"
attribution is not yet R3-checked.
