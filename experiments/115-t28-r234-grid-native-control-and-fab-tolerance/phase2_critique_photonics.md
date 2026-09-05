# exp-115 — Phase 2 blind critique — **PHOTONICS**

*Panel Iteration 92, candidate exp-115. Written blind: I have read the
Phase-1 proposal, PANEL.md, LOGBOOK.md (R1–R34, ESTABLISHED, LIVE
THREADS incl. T27/T28), PLAN.md 1–110, the exp-114 record (`run114.py`,
`chunk_runner114.py`, `analyze114.py`, `results.json`,
`phase5_redteam_audit.md`, my own `phase5_review_photonics.md`),
exp-113's runners, exp-112's and exp-108's `results.json`, exp-061's
NOTES.md, `lab/materials.py`, `lab/validation/VALIDATION.md`,
`lab/ARTIFACTS.md`. I have not read any other seat's current-cycle
output. Every figure below was produced by invoking committed code or
reading committed JSON this session; §4 gives the source for each. No
simulations were run.*

---

## 1. Steel-man (≤150 words)

The load-bearing identity is real and I reproduce it bit-exact:
`measured_ratio ≡ kappa_ratio × G`, `1.5 × 2.74550565394726 =
4.11825848092089`, identical to exp-114's filed value in all 15 digits.
That reframing is the best thing in this document — it converts a
cross-session normalization argument into a single same-session grid
ratio, which makes M5 genuinely R33-immune by construction rather than
by compliance, and it retires the v2 straddle with data instead of a
third assumption. The grid-interleaved execution order (1→2→3→4→5→6) is
the right control against thermal drift, the graceful-degradation branch
spends the *repeat* rather than the primary, and the M5 band edges
(`G ∈ [2.0785394, 2.8121415]`) re-derive exactly. Item 1 is cheap,
falsifiable, ranked #1, and executed in queue order. It should run.

*(147 words.)*

---

## 2. Sharpest attack (≤150 words)

**M9's optics are wrong by `exp(τ_true)` ≈ 3862×, and the error hides an
11% constraint-2-channel effect.** A buried scatterer perturbs a
cross-section through the *coherent cross-term*, linear in the leaked
**amplitude**: `δσ/σ ≈ 2·exp(−τ_true) = 5.18×10⁻⁴`. `exp(−2τ_true) =
6.71×10⁻⁸` is the round-trip *intensity* — the subdominant `|A_core|²`
term. Measured `Δσ_scat/σ_scat = 1.087×10⁻⁴` is **21% of the correct
prediction**, i.e. a resolved detection, not "three orders of magnitude
below anything this instrument can resolve." M9(b)'s floor cannot say
otherwise: it is bit-identically common-mode
(`Δσ_scat + Δσ_abs − Δσ_ext = 0.0`, exactly). Worse, M9(d)'s per-bin
figure is **peak-normalized**. Locally, exp-112's own committed arrays
show the backscatter hemisphere moving **3.6%–11.3%** when the core is
swapped — 753× the headline, in the observer-return direction.

*(139 words.)*

---

## 3. Verdict

**support-with-changes.**

**Item 1 (Block CG): support, unchanged.** I re-derived its central
identity, its band edges and its anchors; nothing in §2 touches it.

**Item 5 (M9): support only with the change below; as written it must
not ship.** M9(d) is written to be quoted verbatim into Result prose
(R21), and as written it states a claim that is false in the one angular
channel constraint 2 is measured on.

**The single change that flips my verdict to unqualified support** —
zero FDTD, zero grid-steps, from arrays already committed:

> `analyze115.py` computes the per-bin core-swap sensitivity under
> **local** normalization, `|Δ_bin| / |pattern_hollow_bin|`, alongside
> the existing peak normalization, over
> `experiments/112-.../results.json`'s own 48-bin arrays; M9(d) reports
> **both**, plus the backscatter-hemisphere (`|θ| ≥ 135°`) maximum
> explicitly; and M9(c)'s mechanistic estimate is re-derived on the
> coherent amplitude scaling `2·exp(−τ_true)`, not `exp(−2·τ_true)`.

If the seat declines that change, the correct action is to defer item 5
an **eighth** time rather than file a wrong bound. A deferral is a debt;
a false bound in the permanent record is a liability, and this one points
straight at constraint 2.

Two smaller, non-flipping changes I would also make: strike the "six box
radii" clause from M9(d)'s headline (§4.6), and correct §2.2's "peccored
steps are ~14% costlier" to the 1.29% exp-114's own committed per-scene
wall times actually show (§4.7).

---

## 4. Appendix — derivations, reproductions, and failures to reproduce

### 4.1 REPRODUCED — the load-bearing identity (bit-exact)

```
d = json.load(open('experiments/114-.../results.json'))
  ps234 = d['t234_cpl25']/36000                                    = 0.19550806899203194
  ps156 = d['r31_control']['sustained']['this_session_per_step_s'] = 0.07121022268191168
  G     = ps234/ps156                                              = 2.74550565394726
  1.5*G                                                            = 4.11825848092089
  filed d['kappa_exponent_result']['measured_ratio']               = 4.11825848092089   (==, exactly)
  3*8000*ps156 = 1709.0453443658805 == d['t156_session_adjusted']
  d['t234_cpl25']/d['t156_session_adjusted'] = 4.11825848092089
```

The proposal's §1/§2.0 identity claim is **confirmed**. The algebra is
exact because `run114.py::refit_kappa_exponent` inverts
`kappa_ratio ** exponent` and `classify_kappa_exponent_check`
(`run114.py:258–277`) re-exponentiates it; both legs run three scenes and
`STEPS` scales linearly with `kappa`, so every cross-session term
cancels. exp-114 measured `G` and nothing else.

Also reproduced this session, each by invocation, none hand-typed:
`k = R110.KAPPA_COST_EXPONENT = 3.2053299988171697`;
`1.5**(k−1) = 2.4453404739580256 = reference_ratio/1.5`;
`(2100/1400)**2 = 2.25`; `1 + ln(2.25)/ln(1.5) = 3.0` **exactly** (the
proposal's previously-unstated observation that v2's assumption *is* the
pre-R28 hardcoded exponent — correct, and worth keeping);
`R_DEG = 0.07596424755863729`;
`2**(k−3) = 1.152950039837078 = 2**k/2**3 − 1` (R28's founding miss);
`2.25 × 2**(k−3) = 2.5941375896334256`.

M5 band edges re-derived independently:
`3.6680107109370383 × {0.85, 1.15, 0.70, 1.30} / 1.5 =
{2.0785394028643216, 2.812141545051729, 1.7117383317706178,
3.178942616145433}` — matches the proposal's `[2.0785394, 2.8121415]`,
`≤1.7117383`, `≥3.1789426`.

### 4.2 THE MAIN FINDING — M9(c) uses an intensity round-trip where the physics is a coherent amplitude cross-term

exp-061's own committed derivation (`experiments/061-.../NOTES.md:40–49`)
defines

```
tau_true   = 2 * (2*pi/cpl) * thickness_cells * I_graded = 8.258819829686677
alpha_true = tau_true / 1440nm = 5.7353e4 cm^-1 ; e-fold 174.36 nm ; OD 3.587
```

The leading factor 2, and the "e-fold / OD" framing, fix the convention:
`α = 2·k₀·Im(n)` is an **intensity** attenuation coefficient, so
`τ_true` is a one-way **intensity** optical depth. Therefore:

| quantity | value | what it is |
|---|---|---|
| one-way intensity transmission | `exp(−τ) = 2.590×10⁻⁴` | |
| one-way **amplitude** transmission | `exp(−τ/2) = 1.611×10⁻²` | |
| round-trip **amplitude** (in, reflect, out) | `exp(−τ) = 2.590×10⁻⁴` | **the core's far-field amplitude** |
| round-trip intensity | `exp(−2τ) = 6.706×10⁻⁸` | the `\|A_core\|²` term only |

The far field is `A = A_shell + A_core`, coherent single-frequency FDTD.
`σ ∝ |A|²`, so to first order

```
delta_sigma/sigma = 2 * Re(A_core * conj(A_shell)) / |A_shell|^2
                 <= 2 * exp(-tau_true) = 5.179e-4      for |A_shell| ~ O(1) at the aperture scale
```

`|A_shell| ~ O(1)` is not an assumption — it is measured. From exp-114's
own hollow ledger at r=234: `σ_ext / (2 × 2·R_COAT) = 0.936` and
`σ_abs/σ_ext = 0.4955`. This article sits on the extinction-paradox
asymptote with `σ_scat ≈ σ_abs ≈` its geometric width; its scattered
amplitude is of order the incident amplitude over the aperture.

**Consequence.** The measured aggregate `Δσ_scat/σ_scat = 1.0873×10⁻⁴`
is `0.21 ×` the coherent estimate and `1621 ×` the incoherent one. The
proposal's (c) says the physical value is "three orders of magnitude
below anything this instrument can resolve"; on the correct scaling it is
a **factor of ~5 above** what was measured — i.e. the measurement is a
plausible, resolved detection of exactly the effect (c) computes, sitting
below the crude upper estimate by about the factor the geometry predicts
(the core subtends `R_CORE/R_COAT = 0.795` of the aperture, and every
non-central chord through the annulus is longer than the radial one:
`sqrt(R_COAT² − R_CORE²)/(R_COAT − R_CORE) = 2.96×` at the tangent).

This is a **coherence** error, not an arithmetic one. `exp(−2τ)` is the
right answer to "how much core-reflected *power* comes back" and the
wrong answer to "how much does the *cross-section* change," which is what
(a)/(b) actually measure. It propagates into (e): the promised
improvement with a thicker coating scales as `exp(−τ_true)`, not
`exp(−2·τ_true)` — the backing freedom still improves exponentially, but
at **half the exponent** the proposal states.

### 4.3 THE FLOOR IS COMMON-MODE — M9(b)'s gate cannot bound a differential

From exp-114's `results.json` `energy_ledger` (peccored vs hollow,
r=234):

```
Delta_scat + Delta_abs - Delta_ext        = 0.0                 (exactly, float64)
Delta(sigma_ext_cross) - Delta(sigma_ext) = 0.0                 (exactly, float64)
sigma_ext_cross - sigma_ext               = 0.0303914978344     (IDENTICAL in both scenes, all digits)
```

The optical-theorem residual the proposal adopts as its floor
(`2.7794×10⁻⁵`) is a **fixed, article-independent** discretization
offset: it is bit-identical in the two scenes being differenced, so it
cancels identically and bounds nothing about their difference. Two
independent `σ_ext` estimators agree on the *difference* to machine
precision — affirmative evidence that the `5.20×10⁻⁵` `σ_ext` delta and
the `1.087×10⁻⁴` `σ_scat` delta are **resolved**, not floor noise. Under
a correct differential floor, all six entries in M9(a)'s table are
resolved, including the `σ_abs` entry at r=234 (`5.666×10⁻⁶`) that M9(b)
singles out as "below floor."

This is the failure mode `lab/validation/VALIDATION.md:334–338` already
records as paid for once: *"Ratio gates can't see convention bugs —
absolute balances can … reference and scene shared the error."* Same
shape, one level over: a shared systematic used as a differential floor.

**Rule-compliance finding.** M9(b) invokes R13. R13's trigger is a
denominator with knowable real zero-crossings; `σ_ext ≈ 1093` has none,
so R13 is not what is being applied. What *is* being applied is an
uncalibrated discriminating threshold cited with evidentiary language
("upper bound, not a resolved measurement") — that is **R30**, and R30's
calibrating data already exists (the exact-zero differential closure
above; the 48-bin population in §4.4). R30 is live and undischarged on
M9(b) as written, not N/A. The proposal's §8 declares R30/R32 N/A for
M3/M4/M6/M7 — I agree for those four; I do not for M9(b).

### 4.4 THE PER-BIN CLAIM IS PEAK-NORMALIZED — the backscatter hemisphere moves 3.6%–11.3%

`experiments/108-.../run.py::classify_item_i` computes
`rel32 = |delta32| / max(|peccored32|)` — normalization by the **peak
over all 48 bins**, not by the bin's own value. So the `1.4760×10⁻⁴`
(r=156) / `1.5266×10⁻⁴` (r=312) figures M9(a)/(d) quote are
peak-normalized, then carried into a sentence about "48 angular bins."

Recomputed from exp-112's own committed `pattern_hollow` /
`pattern_peccored` / `pattern_delta` (r=156, cpl=25 — the same
`fixedabs_cpl` family as the r=234 leg), 48 bins, `|Δ|/|hollow|`:

| statistic | value |
|---|---|
| max, peak-normalized (reproduces the house figure) | `1.4977×10⁻⁴` |
| **max, locally normalized** | **`0.11280` at θ = −168.75°** |
| median, locally normalized | `2.353×10⁻⁴` |
| ratio max-local / max-peak | **753×** |
| bins exceeding 1% locally | **16 of 48** |
| bins exceeding the headline `1.6×10⁻⁴` locally | **24 of 48** |
| backscatter hemisphere `\|θ\| ≥ 135°`, local | `0.0357, 0.1128, 0.0908, 0.0689, 0.0914, 0.0507, 0.0514, 0.0908, 0.0679, 0.0919, 0.1112, 0.0366` |

This is not a normalization quibble; it is the same physics as §4.2 and
it corroborates it quantitatively. The shell's own backscatter amplitude
is tiny (`sqrt(pattern/peak) ≈ 1.0×10⁻³` at 168.75°), so the core's
leaked amplitude `exp(−τ_true) = 2.59×10⁻⁴` is a *large fraction* of it
there. The crude coherent estimate `2·exp(−τ)/(A_bin/A_peak)` gives
`0.49` at 168.75°, `0.51` at 176.25°, `0.27` at 146.25°, against observed
`0.111 / 0.037 / 0.091` — same order, below the crude bound, exactly the
pattern §4.2 predicts. The incoherent `exp(−2τ)` estimate is six orders
of magnitude off in these bins.

**Why this matters beyond bookkeeping.** `|θ| ≥ 135°` is the
observer-return hemisphere — PANEL.md's metrics table, row 2,
"Backscatter to observer vs camera floor | constraint 2". M9(d) as
written ("the material behind it is a free parameter over the entire span
from vacuum to a perfect conductor"; "does not need to control the
substrate or core material, its optical constants, or its interface at
all") licenses a future cycle to change the backing without re-measuring
a channel that demonstrably moves by 11%. That is a constraint-2 risk
carried by a sidecar that declares itself constraint-neutral. I am **not**
claiming a constraint-2 failure — `back_frac = 3.399×10⁻⁶` (exp-108,
r=156) is minuscule in absolute terms and the observer channel may well
stay at the camera floor either way. I am claiming the *bound as written
does not cover that channel* and reads as though it does.

### 4.5 REPRODUCED AND STRENGTHENED — M9(c)'s HALT sub-check will pass, and Idealization 9's worry is moot

I re-derived `I_graded` from `lab/materials.py::_graded_black`
(`materials.py:64–71`: quintic smoothstep `s`, `sigma = sigma_max·s²`)
with `Im(n) = Im(sqrt(1 + i·σ·cpl/2π))`, 2×10⁶-point trapezoid:

| member | `σ_max·cpl` | `I_graded` | `τ_true` |
|---|---|---|---|
| exp-061 (cpl=20, σ_max=0.5, 48 cells) | 10.0 | `0.273840` | `8.258813` |
| the r=234 leg (cpl=25, σ_max=0.4, 60 cells) | 10.0 | `0.273840` | `8.258813` |

`0.273840` reproduces exp-061's committed `I_graded` to six decimals and
`8.258813` reproduces `8.258819829686677` to `8×10⁻⁷` relative — inside
the proposal's own `<1%` HALT tolerance. So (c) will not HALT.

But Idealization 9 ("`Im(n)` is concave in `σ`, so the two are not
assumed equal") is answerable **exactly**, not empirically: the loss
tangent is `σ/ω = σ_max·cpl/2π`, and `σ_max·cpl = 0.5×20 = 0.4×25 = 10`
at both members, while both shells are `2.40 λ` thick. The two members
are the *same optical article* by construction, not by coincidence. The
seat can state that as an identity and drop the concavity hedge — a
strengthening, not an attack.

### 4.6 SCOPE OVERCLAIM in M9(d) — "six box radii" does not carry the `1.6×10⁻⁴` figure

`classify_item_i` persists `rel32` for `margin = 32` **only**; the other
five margins in `MARGINS = (24, 32, 40, 48, 57, 65)` are certified only
by the boolean `confirm_all_margins`, tested against
`ITEM_I_CONFIRM_REL = 0.05` — a decision bar `330×` looser. The proposal
discloses this correctly in its own §2.0 (as an R4 correction to my
seat's exp-114 review — accepted; that correction is right and I confirm
it). But M9(d), the sentence R21 exists to get quoted forward, still
reads "at better than 1.6×10⁻⁴ relative, measured across … 48 angular
bins, six box radii." Five of those six radii are certified at `5×10⁻²`,
not `1.6×10⁻⁴`. The clause should be struck or split. Under R4's second
addendum this is the "restated, not recomputed" shape — and here the
proposal supplies its own refutation two sections earlier, so the
headline contradicts its own §2.0.

### 4.7 FAILED TO REPRODUCE — §2.2's "peccored steps are ~14% costlier"

The proposal justifies the mandatory 3-scene control mix by citing
exp-113's Fix 3b: *"`peccored` steps are ~14% costlier."* exp-114's own
committed `total_wall_s_by_scene` (12000 steps/scene, r=234) says
otherwise:

```
empty    2355.936572790146  -> 0.19632804773251217 s/step
hollow   2326.2050988674164 -> 0.19385042490561802 s/step
peccored 2356.1488120555878 -> 0.19634573433796565 s/step
max/min = 1.0128723      (peccored vs hollow: +1.287%; peccored vs empty: +0.009%)
```

**1.29%, not ~14%** — a 10× overstatement, re-derivable from the same
`results.json` the proposal read for six other figures. The exp-113
figure is flagged in exp-114's own Phase-5 audit §2 as *"an estimate,
explicitly 'not a profiled measurement'"*; exp-114's production run **is**
the profiled measurement, and it refutes it. The 3-scene mix remains the
right protocol choice (matched protocol, R9), but the stated reason is
wrong, and R4's second addendum requires a cited figure to be recomputed
rather than restated.

### 4.8 A CONFLICT IN THE M3 ANCHOR (R17) — the only two duration-vs-rate facts on file have opposite signs

`R_DEG = +7.596%` says a 3334-step burst is *slower per step* than a
1000-step burst (r=156 grid). exp-114's own r=234 production data says
the opposite on the larger grid: the empty scene's first 3000 steps ran
at `0.2050978 s/step` (the three chunk times the proposal quotes in
Idealization 4) against that same scene's own 12000-step average
`0.19632805 s/step` — the early window is **4.47% slower**, i.e. a
warm-up that decays, not a degradation that accumulates.

Two consequences the proposal should absorb:

1. Idealization 4's claim that "no monotone cold-start penalty is
   visible" is drawn from the *internal* spread of those three chunk
   times (`max/min = 1.088`) and never compared against the scene's own
   full-run average. Against that average there **is** a 4.47%
   early-window penalty. The ≲5% chunk-boundary bound survives
   numerically; the "no cold-start" reading does not.
2. `4.47%` exceeds M3's own CANCELS bar (`R_DEG/2 = 3.798%`). A warm-up
   transient of that size, living entirely inside the 1000- vs
   3334-step regime M3 samples, is a candidate explanation for any
   `d_dur` M3 records — and this cycle's design (six cold builds, nothing
   longer than 3334 steps/scene) cannot separate it from the
   grid-dependent degradation M3 is written to detect. R17 asks that a
   band be anchored against the largest established comparable
   magnitude; `+7.596%` and `−4.47%` are both established and they
   disagree in sign. I would state that in M3's own text, and add one
   line to `analyze115.py`: persist each reading's **per-scene** times,
   not only the blend, so a future cycle can see the transient rather
   than infer it.

### 4.9 Rule-compliance summary

| Rule | Finding |
|---|---|
| **R4** (2nd addendum) | §4.7 — "~14% costlier" restated, not recomputed; refuted at 10× by committed data. §4.6 — M9(d)'s "six box radii" contradicts the proposal's own §2.0 recomputation. |
| **R9** | §4.3 — M9(b) divides a **differential** (Δσ_scat between two scenes) by a **common-mode** residual (the optical-theorem offset, bit-identical in both scenes). Incommensurable operands: the division is arithmetically fine and evidentially empty. |
| **R13** | Invoked by M9(b) but not triggered (`σ_ext` has no zero-crossing). Not a violation; a mislabel. |
| **R17** | §4.8 — M3's anchor conflicts in sign with the only other duration-vs-rate datum on file. Separately, M6 and M7 both cite R28's founding miss `0.1529500` but M6 uses `0.15`; harmless (M6 is the stricter) but one anchor should be spelled one way. |
| **R21** | M9(d) is explicitly written to be quoted into Result prose. That is why §4.4/§4.6 are blocking rather than cosmetic. |
| **R30** | §4.3 — live and undischarged on M9(b)'s floor gate; declared N/A only for M3/M4/M6/M7, where I agree it is. |
| **R32** | N/A confirmed — no directional statistic in this cycle. |
| **R33** | Genuinely made inapplicable for M5 by the §4.1 identity, as claimed. Confirmed. |
| **R5 addendum** | No named-constant search here. `r = 234` as a geometry size is unrelated to the ruled-out `A_alt ≈ 233/234` match; the proposal's §8 check is correct. |
| **R1** | Not engaged: `eps_r ≡ 1` throughout, no real-Δε mechanism proposed. |

### 4.10 Constraint / metrics-table exposure

- **Constraint 3:** not violated. The article already fails constraint 3
  by construction; the proposal says so in §4 and takes T1 route NONE.
  Correct, and correctly reasoned rather than copied.
- **Constraint 2:** exposed by M9(d)'s wording, per §4.4. The sidecar
  makes a claim about the far-field angular pattern that is
  quantitatively wrong in the observer-return hemisphere and is phrased
  as a licence to vary the backing freely.
- **Metrics table, "Wavelength (≥450/600/750 nm) and angle dependence —
  witness realism":** M9(d) scopes itself to 600 nm, but M9(e)'s
  fabrication consequence is broadband. Recomputing `τ_true` for the same
  physical shell (dx = 24 nm, 60 cells, `σ_max = 0.4`, `σ`
  frequency-independent as the engine models it) at this program's own
  three wavelengths:

  | λ | cpl | `I_graded` | `τ_true` | `2·exp(−τ_true)` |
  |---|---|---|---|---|
  | 450 nm | 18.75 | `0.214594` | `8.6293` | `3.58×10⁻⁴` |
  | 600 nm | 25.00 | `0.273840` | `8.2588` | `5.18×10⁻⁴` |
  | 750 nm | 31.25 | `0.327804` | `7.9091` | `7.35×10⁻⁴` |

  The band is narrow (`τ` spans 7.91–8.63; the `1/√λ` conductor scaling
  is partly cancelled at `σ/ω ≈ 1.6`, which is not deep in the conductor
  limit), but the core-leakage amplitude is monotonically **2.05× worse
  at 750 nm than at 450 nm**. That is a real, quantified, one-line caveat
  M9(e) should carry: the backing freedom is weakest in the red, and it
  has never been measured anywhere but 600 nm. A scoping fix, not a
  blocker.

### 4.11 An alternative explanation the sidecar does not exclude

`build_sim`'s `peccored` branch applies `pec_disk` (`sim.pec |= rr <=
R_CORE`) **before** `graded_black_shell` (which writes `sigma_e` for
`rr >= R_CORE`), so the innermost ring of shell cells is both maximally
lossy and PEC-masked in one scene and lossy-only in the other. A
one-cell-ring construction difference at the core boundary is a second,
non-physical candidate for a `~10⁻⁴` differential, distinct from genuine
coating leakage. My §4.2/§4.4 amplitude estimates favour genuine leakage
(they predict both the aggregate magnitude and the backscatter-bin
enhancement, from one parameter already on file), but the sidecar
distinguishes neither, and (c) currently supports neither. If M9 is to
claim a mechanism at all, it should say which of the two it is claiming —
or state that it is not distinguishing them.

### 4.12 What I could not check

- The bench (T5820) has no prior FDTD timing on file, so §6's 43.2%
  worst-anchor margin is unverifiable from this repository. I take no
  position beyond noting that the projection is bracketed by two real
  anchors and the gate re-projects from measured readings, which is the
  correct construction (R28-compliant by inspection of §6's pseudocode;
  I could not test it, since `chunk_runner115.py` does not yet exist).
- exp-114's three r=234 chunk times survive only as quotations inside
  `phase5_redteam_audit.md` §2, as the proposal discloses. §4.8's 4.47%
  figure inherits that same non-re-derivable status; I flag it as
  directional, not as a scored number.
- No r=234 per-bin angular data exists (the captures were never
  committed — §3 item 3, confirmed by direct read). §4.4's
  local-normalization figures are r=156/cpl=25 only. The fix I ask for
  costs nothing precisely because it uses the data that *does* exist.
