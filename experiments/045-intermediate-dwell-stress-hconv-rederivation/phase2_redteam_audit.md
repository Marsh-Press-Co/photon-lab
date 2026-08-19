# PHASE 2 — RED TEAM AUDIT · Panel Iteration 22 · exp-045

**Seat: RED TEAM (final, sees everything).** Independently re-derived every
load-bearing number below from `run.py`'s own formulas before reading any
seat's arithmetic as authoritative — the house discipline (Red Team
re-derives, not merely adjudicates). All numbers quoted as "verified" were
recomputed from scratch in a standalone script against `lab/thermo_sidecar.py`
and `run.py`'s literal constants, not copied from any critique.

---

## 0. Scope framing (stated up front, per charter)

Both blocks are honestly framed: T1 escape route "NONE," pure
instrument/model-fidelity work, zero new FDTD calls. This audit therefore
does **not** apply constraint-#N-violation tags in the mechanism sense
PANEL.md calibrates them for — there is no σ(I)/σ(x,t)/angular/sub-threshold
claim here to check against constraints 1–4. Per the Director's own
instruction and PANEL.md's charter language ("use your judgment"), attacks
below are tagged with the closest-fitting category, and a fifth informal tag,
**[process]**, is used for house-discipline / program-integrity findings that
are real but not physics claims.

---

## 1. Independent re-derivation — the core numbers

Recomputing `run.py`'s Block B chain directly from its own constants
(`DX_M=30e-9`, `R_OUT_CELLS=78`, `SIGMA_EXT_ON=235.9667…`,
`K_AIR_W_MK=0.026`, `DENSITY_PMMA=1180`, `C_P=700`):

| Quantity | My value | `run.py`'s value | Match |
|---|---|---|---|
| `r_out_m` | 2.34×10⁻⁶ m | 2.34×10⁻⁶ m | ✓ |
| `w_on_m` | 7.0790×10⁻⁶ m | 7.079×10⁻⁶ m | ✓ |
| `w_on/r_out` | 3.0252 | (unstated, PHOTONICS: 3.03) | ✓ |
| `h_eff` (via `r_out`) | 11,111.1 W/(m²K) | 11,111.1 | ✓ |
| `h_eff` if computed via `w_on` instead | 3,672.83 W/(m²K) | — (never computed in `run.py`) | new |
| `area_ratio_on` (iso/geometric) | 2.9131× | 2.9131× | ✓ |
| `mass_kg_pmma` (`w_on³`) | 4.1860×10⁻¹³ kg | 4.186×10⁻¹³ kg | ✓ |
| `dt_ss_full_corrected` | 3.5982×10⁻⁶ K | 3.598×10⁻⁶ K | ✓ |
| `tau_thermal_fully_corrected` (as coded) | 5.2601×10⁻⁴ s | 5.260×10⁻⁴ s | ✓ |
| `dwell/tau_thermal` (as coded) | **126.74×** | "126.7×" | ✓ |

`run.py`'s arithmetic is internally correct — every seat's "no error found"
verdict on the raw computation is right. **The attack is not on the
arithmetic; it is on what the arithmetic is arithmetic of.**

---

## 2. Numbered attack list

### Attack 1 — [inconsistency] Two length scales, one "first-principles" claim

Confirmed independently, byte-for-byte with PHOTONICS and THERMODYNAMICS:
`h_eff = k_air / r_out` uses the bench's real geometric radius (2.34 µm);
`mass_kg = density × w_on³` uses the ON-endpoint article's measured
*extinction*-width (7.079 µm, `SIGMA_EXT_ON × dx`) — an optical quantity T9
already shows departs from geometric size (`Q_ext` = ratio implied ≠ 1).
`w_on/r_out = 3.025`, and because `mass_kg ∝ w³`, this single unflagged
length-scale swap propagates **cubically**. Narrative §1's claim that both
quantities are "derived from the object's own bench geometry" is false for
`mass_kg` as coded. **ADOPT (PHOTONICS + THERMODYNAMICS, independently
convergent).**

### Attack 2 — [inconsistency] P-EM45-A6's headline sign is not robust

Independently reproduced THERMODYNAMICS' sharpest number to displayed
precision: holding everything else fixed and using `w_on` for `h_eff`
consistently (the established-ratio branch's own already-adopted length
convention for area/absorbed-power — see Attack 6 for why this is the more
defensible of the two available conventions, not an arbitrary pick):

```
h_eff(w_on)            = 3,672.83 W/(m²K)   (vs. 11,111.1 as coded)
tau_thermal(w-consist.) = 1.590×10⁻³ s      = 1.154× the OLD uncorrected value
                                              (GROWS, not the coded 0.382× SHRINKS)
dwell/tau_thermal        = 41.9×             (vs. the coded 126.7×)
```

The proposal's own falsification condition for P-EM45-A6 is "landing outside
[100×, 160×] would mean this interaction doesn't hold as cleanly as
predicted." **41.9× already falls outside that band using only the
single most load-bearing correction identified this cycle.** **ADOPT,
independently reconfirmed bit-for-bit.**

### Attack 3 — [inconsistency] The combined, self-consistent correction — the finding no single blind seat computed

This is the answer to the Director's assigned question (b)/(c): what happens
when the length-scale fix (PHOTONICS/THERMO) and the material-identity fix
(MATERIALS) are applied **together**, not one at a time. I ran four
combinations from scratch:

| Combination | `h_eff` basis | Density | `C_P` | `dwell/τ_thermal` |
|---|---|---|---|---|
| As coded (buggy) | `r_out` | PMMA 1180 | 700 (mismatched) | **126.7×** |
| THERMO's fix alone | `w_on` | PMMA 1180 | 700 (mismatched) | 41.9× |
| MATERIALS' fix alone | `r_out` | Si 2330 | 700 (matched, coincidentally) | 64.2× |
| **Both fixes, Si identity** | `w_on` | Si 2330 | 700 (matched) | **21.2×** |
| **Both fixes, PMMA identity + correct C_P≈1450** | `w_on` | PMMA 1180 | 1450 | **20.2×** |

**Both fully-self-consistent combinations land at ≈20–21×, not the claimed
126.7×, and — this is the load-bearing new result — BELOW
`N_TRANSIENT_TAU=25`, i.e. *less* comfortable than the T22-area-only figure
(16.1–16.7×) that Iteration 21 flagged as the concern this whole cycle exists
to relieve, not merely "not as good as claimed."** P-EM45-A6's own
plain-language framing — "the properly-derived correction relieves, not
worsens, T22's remaining concern" — is backwards under either self-consistent
reading. It does not fully reopen the *decoupled-shortcut-vs-exact* physics
question at a 1:1 dwell-to-tau ratio (dwell still clears τ_thermal by an
order of magnitude, not by "≈1×" — no verdict-flipping risk, see Attack 12),
but it firmly and doubly fires the proposal's own pre-registered
falsification condition ([100×,160×]) under every self-consistent parameter
choice tried, not just MATERIALS' isolated one. **NEW finding — synthesizes
but goes beyond every individual blind-seat critique; none combined more
than one fix at a time.**

### Attack 4 — [inconsistency] The PMMA citation does not check out (independently reconfirmed)

Ran `grep -rln "PMMA"` across the full repository: zero hits outside
`experiments/045-…`'s own two files. `grep`-checked exp-036/037/038's
NOTES.md for any polymer-host / dye-host language: zero hits. MATERIALS'
claim is correct and, on inspection, actually *understates* the problem:
this is not merely "the wrong material for this grid" (Hosts A–D are
linearly-pumped FCA in doped Si/Ge, T17/exp-037/038) — the specific citation
string in both `run.py` and `phase1_proposal.md` ("the most commonly cited
photochromic-dye host polymer in this program's own literature surveys,
T17/T18, exp-036/037") is **fabricated provenance**: those experiments never
mention a polymer host at all. This is the same failure class as QUANTUM's
Iteration-21 `realizability_tier`-misattribution catch — a citation invented
to sound sourced. **ADOPT MATERIALS' finding; ELEVATE severity from
"wrong material" to "confabulated citation."**

### Attack 5 — [inconsistency] MATERIALS' and THERMODYNAMICS' fixes are the SAME fix, not two independent corrections

New synthesis, not caught by either seat in isolation: THERMODYNAMICS
correctly flags that `C_P=700` (fused-silica-like) is inconsistent with
PMMA's real ~1450–1500 J/(kg·K) *once Block B names PMMA*. But `C_P=700` is
not an arbitrary number that happens to be silicon-adjacent — exp-037's own
NOTES.md (line 828) independently sourced silicon's thermal constants as
**"ρ≈2330 kg/m³, c_p≈700 J/(kg·K)"** for this identical Host A–D mechanism.
`C_P=700` was carried forward unmodified from exp-032/043 without an explicit
material label (`"UNRESOLVED... NOT derived from a real material"`,
exp-043 `run.py` line 104) — so this is not a proven code lineage back to
exp-037's citation, but it is a materially significant coincidence: **if
MATERIALS' silicon-density fix is adopted, THERMODYNAMICS' C_P-mismatch
concern resolves for free — no further C_P change is needed. If PMMA is kept
instead, C_P must ALSO be changed (to ~1450–1500), a second correction the
proposal never applied.** The two blind seats' fixes are not orthogonal
inputs to be independently weighed; they are two views of one underlying
material-identity question, and the record's own literature (exp-037)
already answers it in silicon's favor for this specific Host-grid mechanism.
**Phase 3 should state this explicitly, not leave it to be independently
rediscovered a third time.**

### Attack 6 — [inconsistency] A structural Biot-number finding THERMODYNAMICS' own number understates

THERMODYNAMICS computed Bi = h_eff·r_out/k_solid ≈ 0.137 for the as-coded
`h_eff` and flagged it as "above the classical Bi<0.1 lumped-capacitance
threshold," framing it as a ~5–15% correction. Independently checking whether
this survives the Attack-1 length-scale fix: it does not go away, and it is
**worse than a fixable artifact — it is a structural property of the formula
itself.** Since `h_eff = k_air/L` for ANY conduction length `L`,

```
Bi = h_eff · L / k_solid = (k_air/L) · L / k_solid = k_air / k_solid
```

**— exactly cancels L.** Bi ≈ 0.026/0.19 ≈ 0.137 regardless of whether `L`
is `r_out`, `w_on`, or any other length picked consistently for both `h_eff`
and the Biot check. The length-scale-consistency fix (Attacks 1–3) does
**not** resolve this — it is orthogonal to it. The lumped-capacitance
assumption underlying the entire `tau_thermal_s`/`transient_delta_T`
framework is running at Bi≈0.14 for *any* self-consistent version of this
`h_eff=k_air/L` conduction-limit choice, not merely the buggy one. This
should be disclosed as a standing ~10–15% internal-gradient-error caveat on
every `tau_thermal_s` number Block B produces (all regimes, not just the
as-coded one) — a genuinely new finding, not caught by any blind seat
(THERMODYNAMICS computed one Bi value but did not derive its L-invariance).

### Attack 7 — [unfalsifiable] As coded, P-EM45-A6 cannot fail against the alternative the record itself supplies

`run.py`'s `TAU_TH_REGIMES` dict has exactly one Block-B-derived entry,
`"fully_corrected_pmma"`, built from the mixed-length-scale, unsourced-C_P
chain (Attacks 1, 4, 5). There is no code path anywhere in this script that
computes the length-scale-consistent alternative, the silicon-identity
alternative, or the two combined — the alternatives three independent seats
(and Red Team) derived by hand exist nowhere in the committed arithmetic.
Run as submitted, Phase 4 would execute, print, and commit
`results.json` confirming P-EM45-A6's [100×,160×] band using only the one
convention that produces it — **the falsification condition is tested
against the claim's own restatement, not against the physically live
alternative the record already contains.** This is a genuine instance of the
"unfalsifiable claims" category Red Team's charter names, even though this
cycle is instrument-fidelity work rather than a mechanism proposal — a
prediction whose only tested regime is chosen so it cannot fail is
unfalsifiable in practice regardless of the domain.

### Attack 8 — [process] NETD disclaimer dropped per-point, at 100× the prior scale — confirmed

Read `run.py` line 268 directly: `"netd_classification": netd["classification"]`
is the only field stored from `ts.netd_disposition()`'s return dict at all
1664 sweep points — the `"disclaimer"` field `netd_disposition` exists
specifically to carry (per its own docstring, and per Iteration-20's
mandatory fix) is discarded every time. `block_a["netd_disclaimer"]` is
block-scope only (one copy for 1664 points); none of the six console
`print()` statements mention it. VISION SCIENCE is correct that this is
Iteration-21's mandatory fix 6 regressing, now at 100× the point count.
**ADOPT unmodified.**

### Attack 9 — [inconsistency] Block C's deferral rationale is contradicted by the record — confirmed by direct code read

Confirmed via `run.py` line 255: `kin.relax_exact(n0=0.0, k_f=k_f, k_r=k_r,
dt=dwell)` is called identically at every one of the 1664 sweep points — the
starting population is cold every single time. QUANTUM's Iteration-21
population-memory catch (n0≠0, previously found up to a 2.106× peak ratio at
Host E under a 0.5τ stress interval, exp-038) is untouched, not partially
addressed, exactly as QUANTUM states. The stated deferral reason — that
choosing a sweep-rate/inter-pulse convention is "a QUANTUM-native judgment
call... not an EM-appropriable arithmetic swap" — does not survive contact
with the fact that `pulse_train_segments` already exists and exp-038 already
made and validated that exact judgment call (a 5τ/0.5τ bounding pair) at
Host D. This is now a second consecutive deferral (Iteration 21 close →
"Iteration 22" → this proposal's own re-deferral to "Iteration 24") of an
item whose marginal cost, per QUANTUM's own critique, is a handful of lines
reusing functions this script already imports. **MANDATE the bounded check
this same shift** (see Ruling §4).

### Attack 10 — [process] The "no new trust-suite stage" backing does not actually cover Block B

`run.py`'s docstring justifies skipping a new trust-suite stage with three
items: (i) exp-044's own scipy cross-check of `coupled_kinetics_thermal_dT`
— covers Block A only, a verbatim-reused closed form; (ii) "this script's
own internal analytic identity checks"; (iii) the monotone-ceiling bound.
Checking (ii) directly: the two assertions are
`abs(h_eff*r_out_m - K_AIR_W_MK) < 1e-15*K_AIR_W_MK` and
`abs(mass_kg_pmma - DENSITY_PMMA_KG_M3*volume_iso_cube_m3) < 1e-30`. Both are
tautological round-trips — they verify that a division was correctly undone
by a multiplication, and that a multiplication matches itself. **Neither
assertion is capable of catching the length-scale-mixing bug this cycle's
own Phase 2 found** (Attacks 1–3): both would pass identically whether
`h_eff` used `r_out` or `w_on`, since each only checks internal consistency
with itself, not cross-consistency with the OTHER formula in the same
physical chain. The claimed backing (i)+(ii)+(iii) does not actually cover
Block B's new physics at all — (i) is Block-A-only, (ii) is
bug-blind-by-construction, (iii) bounds the ceiling, not the time constant
where the actual bug lives. This does not require a full `lab/`-promotion +
formal trust-suite stage (disproportionate for zero-FDTD desk arithmetic,
consistent with Iteration-20's own precedent) — but it does require **one
real cross-consistency assertion** (e.g. `assert` that the length variable
feeding `h_eff` equals the length variable feeding the mass/area chain, or an
explicit "regimes agree to within factor X" sanity check across the
self-consistent alternatives) so a future re-run of this exact script would
catch a recurrence of this exact bug automatically, rather than relying on a
Phase-2 panel catching it by hand each time.

### Attack 11 — [minor, disclose only] Knudsen-number correction, confirmed small

THERMODYNAMICS' Kn≈0.028 slip-flow estimate and ≈−5% first-order thermal-slip
correction to `h_eff` check out order-of-magnitude (independently spot
checked: λ_air≈65–70 nm at 293K/1atm via standard kinetic-theory formula,
Kn=λ/r_out≈0.03). Real, worth a disclosed sensitivity line; does not change
any qualitative verdict at this magnitude. **ADOPT as disclosed caveat, not
mandatory recompute.**

### Attack 12 — [confirmation, not an attack] P-EM45-A1's global-UNDETECTABLE claim is structurally robust to all of the above

Stated explicitly so Phase 3 does not over-correct: the sweep's own global
maximum ΔT (3.585×10⁻⁴ K, 55.8× below `netd_lo`) occurs in regimes
i–iii (uncorrected / T22-area-only), which never touch Block B's `h_eff`/
`mass_kg` chain at all — Block B's own corrected ceiling (`dt_ss_full`) is
*always smaller* than the uncorrected one (h_eff-correction only ever drops
the ceiling, PHOTONICS' Iteration-20 area-invariance proof still holds), so
it can never be the sweep's worst case. Independently verified even the
worst self-consistent Block-B alternative (`w_on`-consistent `h_eff`):
`dt_ss_full = 1.088×10⁻⁵ K`, still **1,839× below `netd_lo`**. P-EM45-A2
through A5 similarly do not depend on the buggy regime (A2–A4 are axis-K,
governed by `τ_kinetics`, untouched by Attacks 1–6; A5 uses the T22-area-only
regimes, also untouched). **Only P-EM45-A6 — the specific quantitative
"relief" headline and its [100×,160×] band — is wrong. The underlying
physics conclusion (this article's thermal signature stays UNDETECTABLE
across every intermediate-dwell regime tested) is not threatened by anything
in this audit.**

---

## 3. Answers to the Director's assigned questions

**(a) Length-scale mixing, verified independently:** yes, confirmed exactly
(Attack 1); sign-flip consequence confirmed exactly (Attack 2, 41.9× not
126.7×, matches THERMODYNAMICS to displayed precision).

**(b) Combined correction:** verified (Attack 3) — landing at ≈20–21× under
either self-consistent material identity, BELOW `N_TRANSIENT_TAU=25`,
worse than (not "relieving") Iteration 21's own T22-area-only concern
(16.1–16.7×). Does not threaten any UNDETECTABLE verdict (Attack 12) or
reopen a genuine 1:1 dwell/τ crisis, but firmly fires the proposal's own
pre-registered falsification band under every self-consistent reading tried.

**(c) Are the three fixes mutually consistent, one coherent revision?**
Yes, and more tightly than either blind seat realized (Attack 5): the
silicon-identity fix and the C_P fix are the same underlying correction, not
two independent ones — adopting silicon density resolves the C_P mismatch
for free. The length-scale fix is orthogonal to the material-identity fix
and composes cleanly with either material choice (Attack 3's table). No
genuine conflict found between the three.

**(d) Block C deferral:** override recommended (Attack 9) — mandate the
bounded check this shift, QUANTUM's exact proposed design, at near-zero
marginal cost, closing a second consecutive deferral of a real,
previously-quantified risk (2.106× peak ratio at Host E).

**(e) Uncaught-by-any-blind-seat findings:** the combined self-consistent
number (Attack 3); the fabricated-citation severity elevation (Attack 4);
the silicon/C_P identity synthesis (Attack 5); the Biot-number
scale-invariance (Attack 6); the unfalsifiable-in-practice framing of
P-EM45-A6 as coded (Attack 7); the trust-suite-backing gap specific to Block
B (Attack 10).

**Docstring's "no new trust-suite stage" scope judgment:** inadequate as
currently backed for Block B specifically (Attack 10) — not because the
scale of NEW claims demands a full formal suite promotion (disproportionate
here), but because the *specific* internal checks offered as substitutes are
structurally blind to the exact class of bug this cycle produced. One real
cross-consistency assertion closes the gap without requiring a new `lab/`
stage.

---

## 4. RULING: PROCEED-WITH-MANDATORY-FIXES

The underlying instrument-fidelity work is sound: Block A's coupled-ODE
sweep methodology, `coupled_kinetics_thermal_dT`'s correctness (re-verified
independently a third time, after EM and QUANTUM), the T22 area-table
numbers, and the headline UNDETECTABLE-everywhere physics conclusion all
survive this audit intact. The defects are real, concentrated, and fixable
without redesigning either block. **No REJECT/REDESIGN warranted.**

### Mandatory fixes (numbered; all to be applied before Phase 4 runs anything)

1. **Fix the length-scale mixing in Block B.** Derive `h_eff` and
   `mass_kg`/area from ONE consistent characteristic length. Recommend
   `w_on` (the established-ratio branch's own already-adopted convention for
   area and absorbed power — internally the more defensible pick, not
   merely an arbitrary tie-break) over `r_out`, but either is acceptable if
   applied consistently and disclosed. **[Adopts PHOTONICS + THERMODYNAMICS,
   Attacks 1–2.]**

2. **Replace `density_PMMA=1180` with silicon's sourced density
   (ρ=2330 kg/m³, exp-037) and relabel accordingly**, OR keep a
   photochromic-dye-host material but (i) name a real one with an actual
   supporting citation from this program's own literature surveys and (ii)
   set `C_P` to match that material's real specific heat (not 700). Delete
   the fabricated T17/T18/exp-036/037 PMMA citation string in both
   `run.py` and `phase1_proposal.md` regardless of which path is taken.
   **[Adopts MATERIALS, Attack 4; note per Attack 5 that the silicon path
   requires no further C_P change, while the alternate path does.]**

3. **Recompute P-EM45-A6 under the fully self-consistent combination**
   (fix 1 + fix 2 applied together) and revise its committed predicted band
   from [100×,160×] to something matching the ≈20–21× region this audit
   independently derived (Attack 3) — or, if the Director prefers, keep the
   mixed-scale number as a clearly-labeled "naive/uncorrected sensitivity
   bound" alongside the corrected headline, never as the sole reported
   figure. Either way, `TAU_TH_REGIMES` must contain a genuinely
   self-consistent Block-B entry, not only the buggy one, so the sweep
   (`sweep_points`, `per_host_axis_axis_summary`, etc.) is computed against
   the corrected physics, not just reported as corrected in prose.
   **[NEW — Red Team synthesis, Attack 3.]**

4. **Disclose the Biot-number ~0.14 caveat as structural, not
   length-scale-fixable**, attached to every `tau_thermal_s` figure Block B
   produces (all regimes), not framed as a ~5% correction specific to the
   as-coded convention. **[Elevates THERMODYNAMICS, Attack 6.]**

5. **Add QUANTUM's bounded Block C sensitivity check this same shift**:
   `pulse_train_segments(k_f_ambient, k_r, A=1, T_pulse=dwell_central,
   dt_sweep, n_pulses=5)` at Host D, all 4 ratios, `dt_sweep ∈
   {5×τ_kinetics, 0.5×τ_kinetics}`, reporting periodic/first-pulse peak-ΔT
   via `coupled_kinetics_thermal_dT` fed the accumulated `n0` — exactly
   QUANTUM's proposed design, reusing functions already imported. Do not
   defer to Iteration 24 a second time. **[Overrides the proposal's Block C
   deferral; adopts QUANTUM, Attack 9.]**

6. **Propagate the NETD disclaimer to every sweep point**, not block-scope
   only — store the full `netd_disposition()` dict (or at minimum its
   `"disclaimer"` field) per point, add it to at least one console print
   adjacent to `all_points_undetectable_or_better`, and inline the
   disclaimer sentence at P-EM45-A1/A2 in `phase1_proposal.md` Section 4,
   not only in Idealizations. **[Adopts VISION SCIENCE, Attack 8,
   unmodified.]**

7. **Add one real cross-consistency assertion** in place of (or alongside)
   the two tautological identity checks — e.g. asserting the length variable
   used for `h_eff` matches the one used for `mass_kg`/area, or asserting the
   self-consistent and mixed-scale regimes' ratio falls in an expected band —
   so a future re-run of this script cannot silently reintroduce Attack 1's
   bug. Does not require a new formal trust-suite stage; does require the
   "no new stage" docstring language to state accurately what is and is not
   covered by the reused-precedent argument. **[NEW — Attack 10.]**

8. **Disclose the Knudsen-number ≈5% `h_eff` correction** as a stated
   sensitivity bound (not mandatory to recompute the headline against).
   **[Adopts THERMODYNAMICS, Attack 11, minor.]**

### Findings explicitly NOT requiring a fix (stated so Phase 3 does not over-scope)

- P-EM45-A1 through A5's core numeric claims (global UNDETECTABLE margin,
  Host-D axis-K curve, witness-dwell consistency check, short-dwell
  artifact note, T22-area-only ≤10% shift) — verified structurally robust
  to every correction in this audit (Attack 12). No recompute required
  beyond what fix 3 already produces as a byproduct.
- The T22 area-table numbers themselves (2.913×, 3.014×) — correct as
  computed; the table's PURPOSE is to compare two genuinely different area
  conventions, unlike the h_eff/mass_kg pairing, which wrongly mixed them
  inside what was claimed to be a single physical quantity.
- Water as a disclosed alternate density bound — MATERIALS' critique that it
  reads as an arbitrary second guess is fair but cosmetic; either drop it or
  give it the same one-sentence justification silicon now gets. Not
  mandatory.

### Explicit note to the Director on the standing program-integrity pattern

LOGBOOK.md records Red Team's own observation that a fix-docket item
"claimed complete" but not fully delivered has recurred across roughly
5 of the last 7 iterations, not decreasing. **This audit is a PRE-RUN
catch** (Phase 2, before any commit) — the pattern as named is specifically
about POST-hoc discovery after Phase 3/4/5 have already shipped a number.
Nothing in this cycle currently instantiates that pattern. **The risk is
prospective, not retrospective:** if Phase 3's synthesis adopts fixes 1–3's
*framing* (acknowledging the sign-flip, stating the corrected band in prose)
without actually re-running Block B's code so `results.json` reflects the
self-consistent numbers — i.e., if the fix is described but not delivered in
the committed artifact — that would be a sixth instance. Flagged explicitly
so the Director closes this loop the same shift, not merely in NOTES.md
prose.

**Next-seat note:** QUANTUM OPTICS leads Iteration 24. This cycle's Block C
addition (fix 5) should be read as EM/Red-Team executing QUANTUM's own
design on QUANTUM's behalf this shift, not as preempting QUANTUM's
Iteration-24 leadership — QUANTUM's own aperture-consistent single-coherent-
mode beam check (Checkpoint-4 tripwire, 3rd deferral) remains untouched by
this ruling and is still due.
