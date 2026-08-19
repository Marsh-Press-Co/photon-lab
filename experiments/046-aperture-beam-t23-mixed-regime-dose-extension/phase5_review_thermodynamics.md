# PHASE 5 — REVIEW · THERMODYNAMICS (fresh context, blind) · exp-046, Panel Iteration 23

*Reviewing this cycle's own lead seat's work. Per this program's precedent
(Iteration 22, ELECTROMAGNETISM reviewing its own Phase-1 draft — LOGBOOK
`f48de18`), no deference is owed to the Phase-1 document because it carries
this seat's name. Every number below was re-derived from `run.py`,
`results.json`, `lab/`, or by hand from the cited constants before it was
used. Verification log at the end. Python execution was unavailable in this
review context, so every arithmetic check below is hand-derived from committed
digits — which is, for a desk cycle, the stronger check anyway.*

---

## 1. Reading — what actually happened

### 1.1 The Block-B and Block-C arithmetic is clean. I found no error in any headline number.

I re-derived Block B from first principles rather than from `run.py`'s output,
starting from `DX=3e-8`, `R_OUT=78`, `SIGMA_EXT_ON=235.96673494878587`,
`RATIO_ON=0.6074830175566805`, `k_air=0.026`, ρ=2330, C_P=700, κ=148, ε=0.9,
T=293.15 K, irradiance `(40000/45²)/300/1e4 = 6.584362e-6` W/cm², dwell
0.0666667 s:

| quantity | hand-derived | committed | |
|---|---|---|---|
| `h_eff`(r_out) | 0.026/2.34e-6 = 11111.11 | 11111.111111111113 | ✔ |
| area(r_out) | 5.4756e-12 | 5.475599999999998e-12 | ✔ |
| mass(r_out) | 2330·1.2812904e-17 = 2.985407e-14 | 2.985406631999999e-14 | ✔ |
| 4εσT³ | 2.041335e-7 · 2.519241e7 = 5.1426 | (implicit) | ✔ |
| dP/dT(r_out) | 5.4756e-12·11116.25 = 6.08680e-8 | 6.086815889755324e-08 | ✔ |
| P_abs(w_on) | 6.584362e-6·5.011227e-11·1e4·0.607483 = 2.00443e-12 | 2.0044347652689456e-12 | ✔ |
| dt_ss(mixed) | 2.00443e-12/6.08682e-8 = 3.29307e-5 | 3.293076054169135e-05 | ✔ |
| τ(r_out) | 2.985407e-14·700/6.086816e-8 = 3.43330e-4 | 3.4332969490950116e-04 | ✔ |
| dwell/τ | 0.0666667/3.4332969e-4 = 194.177 | 194.17681504141214 | ✔ |
| (w_on/r_out)² | (235.96673/78)² = 9.15193 | 9.151923077 | ✔ |
| ratio to `w_on` | 3.293076e-5/1.087524e-5 = 3.02805 | 3.0280489 | ✔ |
| NETD_lo/dt_ss | 0.020/3.293076e-5 = 607.33 | 607.3348951257713 | ✔ |

Block C I re-derived **entirely by hand from the closed form**, not from the
code, and every count reproduces:

- Grid: 5 hosts × 5 ratios = 25, minus Host D's four already-committed exp-045
  points = **21 new**, ×2 gaps = **42 point-runs**. ✔ (Phase 3's hand-count and
  the code's computed count agree; Red Team's docket text "+18" was wrong and
  Phase 3 said so, correctly.)
- Negative controls: Hosts A/B/C at all five ratios = 15 points × 2 =
  **30 point-runs**, all at D/τ_k ≥ 66.7. ✔
- Memory-capable points: Host D r=1.0 (1) + Host E (5) = 6 points × 2 =
  **12 point-runs**. ✔ ("12 point-runs with memory.")
- Which of those exceed 1.05, from `ratio_∞ = 1/(1−a·f)`, `a=e^(−D/τ_k)`,
  `f=e^(−m/(1+r))`, D/τ_k = D·k_r(1+r):
  - Host D r=1.0 (D/τ_k=1.333): 0.5τ → a=0.2636, f=0.7788, ratio **1.258** ✔;
    5τ → f=0.08208, ratio 1.0221 (no).
  - Host E (k_r=1, D/τ_k=0.0667(1+r)): 0.5τ at r=1e-9/1e-5/1e-3 → ratio
    **2.312** ✔; r=1e-1 → **2.438** ✔; r=1.0 → **3.14** ✔.
    5τ at r=1.0 → a=0.8752, f=0.08208, ratio **1.0774** ✔ — exactly the figure
    Amendment 5 records.
  - Total > 1.05: 1 + 5 + 1 = **7**. ✔
- Thresholds: ln(21e^(−0.5)) = 3.0445224 − 0.5 = **2.5445224** ✔ (Phase 1's
  2.5443 was wrong; docket 23 fixed it). At r=1e-1, f=e^(−0.4545455)=0.63474,
  21f=13.329, ln = **2.58998** ✔. At r=1.0/m=5, 21e^(−2.5)=1.7238>1, supremum
  1/(1−0.082085)=**1.0894** ✔.
- C3's ceiling: max n_eq on the extended grid is 0.5 (r=1.0), and
  3.293076e-5 × 0.5 = **1.646538e-5 K** — the committed 1.64654e-5 to six
  figures, margin 0.020/1.64654e-5 = **1214.7×** ✔.
- B5: max n_eq on the 4-host sweep is 0.0909, and 3.293076e-5 × 0.0909091 =
  2.9937e-6 vs committed **2.99357e-6** (just under, correct — the sweep does
  not fully saturate at every R). Margin 0.020/2.99357e-6 = **6681×** ✔.

Zero arithmetic defects. Block C's collapse of Amendment 3's host list to
`D/τ_k < ln(21f)` is, in my judgment, the most durable physical result this
cycle produced — a five-host empirical list replaced by one dimensionless
number and one gap parameter, verified at 250/250 duration-scan points.

### 1.2 The 194.176815× bit-identity: correct, and the structural argument is right — but the prediction is unfalsifiable by construction.

Algebra, re-derived independently:

> τ_thermal = m C_P/(dP/dT) = ρ L_c³ C_P / [L_c²(4εσT³ + k_air/L_c)]
> = **ρ C_P L_c² / (4εσT³ L_c + k_air)**

No `L_power` anywhere. The physics is standard and I agree with it: in a
linearised lumped system the absorbed power sets the *amplitude* of the
response, while the relaxation rate is (loss conductance)/(heat capacity),
both properties of the body alone. Splitting the power length from the
conduction length therefore cannot move τ. Numerically, at L_c=2.34e-6 the
denominator is 0.026 + 1.203e-5 — the radiative term is **0.046%** of the
loss, so τ ∝ L_c² to within 5 parts in 10⁴, which is why 194.177/21.237 =
9.1434 sits just short of (w_on/r_out)² = 9.15192. That small gap is itself a
correct signature of the radiative term, not noise.

**But P-TH23-B1 is a tautology of the implementation, not a prediction.**
`self_consistent_regime` computes `h_eff`, `area_m2`, `mass_kg` and hence
`dp_dt` and `tau_thermal_s` from `length_cond_m` alone (`run.py:616-622`);
`regime_r` and `regime_mixed` are called with the *same* `length_cond_m`.
Bit-identity is not a result, it is the same float ops on the same inputs.
The three `assert`s at `:625-627` check h_eff·L_cond, mass, and p_abs — none
of them asserts τ's independence of `length_power`, because nothing can make
it dependent. Red Team's Attack 2 struck P-TH23-A1/A3 precisely for being
"algebraic identities, not predictions" and recorded them as desk-verifiable
identities rather than experimental findings. **B1 is the same species and did
not get the same tag**: NOTES.md's scorecard reports it as CONFIRMED with the
emphatic "not 'within round-off' — bit-identical", which reads as a
measurement. Phase 3 §"Qualitative predictions" (3) does say "a reproduction,
not a fresh finding" — so the honest framing exists, one document upstream of
the one a future cycle will cite. That asymmetry should be closed at this
close, not left for a future seat to rediscover.

### 1.3 "Eye-invisible" (docket 20): struck in every live artifact; NOT struck, and not flagged, in the one document that still carries it.

Grep results, run directly:

| locus | state |
|---|---|
| `run.py` | 3 hits, all inside `NETD_DISCLAIMER`'s own **negation** ("no 'eye-invisible' claim is made anywhere in this cycle [docket 20]") and two `[docket 20]` strike-records | ✔ |
| `results.json` | 2674 hits, every one inside that same negating sentence | ✔ |
| `predictions_frozen.txt` | 5 hits, all negations | ✔ |
| `NOTES.md` | 1 hit, the strike-record itself | ✔ |
| **`phase1_proposal.md`** | **2 live, unmodified, unflagged hits — §1 line 46 and P-TH23-B3 line 342, the exact two loci docket item 20 names** | ✘ |

`phase1_proposal.md` carries **no SUPERSEDED banner of any kind** (`grep -n -i
"superseded\|struck"` → zero hits). Compare exp-045's `phase1_proposal.md`,
whose first eleven lines are a SUPERSEDED banner naming the fabricated-PMMA
citation and the length-scale-mixing bug — a convention this program adopted
one cycle ago, at Iteration 22's own close, as a mandatory fix, for exactly
this situation (LOGBOOK: "`phase1_proposal.md` gets a SUPERSEDED banner",
`f48de18`; T10's flag-don't-rewrite convention "extended to a Phase-1 draft
for the first time").

exp-046's Phase-1 draft needs that banner far more than exp-045's did. Struck
or superseded content in it now includes: "eye-invisible" (×2), the entire
§2.1 geometry table (docket 3 re-issued it), `width = w₀` at every oblique
call (docket 1), the `w_y(450,2°)=199.33` slip (docket 2), P-TH23-A4 and A7
(dropped), A1/A2/A3 (re-scoped or re-banded), idealization 2's "1.07–1.34 λ"
(docket 12: one value, 1.0737 λ), idealization 4's truncation numbers (docket
11: 25×/657× worse), the silicon "sourced" label (docket 18), §2.3's "decided
by the conduction length **alone**" (docket 19), C5/C6's constants (docket
23), and the soft-form Tier-2 escalation (docket 24).

And NOTES.md line 14–15 states, flatly: *"The Phase-1 proposal's 'eye-invisible'
language is **struck everywhere** (docket 20)."* As a claim about the state of
this repository, that sentence is **false** — the language is live in the
cycle's own Phase-1 document, unflagged, at both named loci. This is the
program's own fix-docket-delivery pattern (LOGBOOK: Iterations 13, 14, 15, 17,
20, 21, 22 — "the rate is not decreasing"), in its characteristic form: the
item is 95% delivered, the claim is 100%, and the gap sits in the historical
record rather than the load-bearing artifact. It is smaller in stakes than
Iteration 21's un-amended memo. It is not smaller in *kind*, and it recurs in
the cycle immediately after the one that invented the fix for it.

### 1.4 NETD disclaimer (docket 21): delivered at 3 of the 5 loci the docket names.

Docket 21: *"Harden idealization 9 at the loci that have actually failed:
NOTES.md prose, `run.py` console prints, and point-of-claim inlining at B3,
B5, C1, C3, C4."*

- NOTES.md prose: header (lines 10–13), Learned header (220–221), idealization
  10 (303–307). ✔
- `run.py` console prints: `:1394` and `:1493`, top and bottom of the frozen
  prediction block, plus per-prediction printing of any `netd_disclaimer` key
  via the generic `for k,v in p.items()` loop. ✔
- Point-of-claim inlining: `netd_disclaimer` is attached to **B3** (`:788`),
  **B5** (`:800`) and **C3** (`:1097`) — and is **absent from C1** (`:1054`)
  and **C4** (`:1098`). ✘ (2 of 5.)

In substance this is defensible: C1 and C4 make memory/tier claims and never
name NETD or UNDETECTABLE, so a detector-vs-eye disclaimer has nothing to
disclaim there — VISION's own Phase-2 list was over-inclusive and the docket
copied it. Two block-level keys (`:815`, `:1140`) and a top-level
`netd_disclaimer_ALL_CLAIMS` (`:1552`) also cover them. But the docket is the
binding instruction, and NOTES.md idealization 10 asserts delivery "at every
point of claim in this file and in `run.py`'s console output" without noting
the two named loci that were judged not to need it. The correct disposition
is a one-line stated override ("C1/C4 issue no detectability claim; disclaimer
not inlined, block-scope key carries it"), not silence — this program's own
rule since Iteration 3 is that an overridden docket item is *stated as
overridden*.

Verdict on the Director's brief question: **the disclaimer genuinely does
appear at every point where a detectability claim is actually made.** The gap
is in the delivery *claim*, not in the disclaimer's coverage.

### 1.5 `REALIZABILITY_MEMO.md` Amendment 5: written, and I read it.

Checked the file directly, not NOTES.md's claim about it.
`experiments/034-floor-convergence-scale-bridge/REALIZABILITY_MEMO.md:162-233`
carries AMENDMENT 5, appended after Amendment 4 with Amendments 1–4 intact.
`git show --stat 460f018` confirms it landed in the same commit as the results
(+72 lines), i.e. the same shift that promised it. Both entries are present:
(a) the memory-axis collapse with the closed form and the refuted C6 clause
recorded rather than buried; (b) the silicon provenance downgrade. "No class
changes tier" is correct — nothing in Amendment 2's table rests on silicon's
thermal constants.

**This is the one place Iteration 21's failure did not recur, and it should be
said plainly.** The item most likely to be claimed-and-not-delivered was
delivered, verified.

One inherited defect, though: Amendment 5(b)'s closing sentence reproduces
the same incomplete fill-factor disclosure analysed in §1.6 below, so the
memo — the program's most-cited standing document — now carries it too.

### 1.6 Fill factor (docket 19): physically incomplete. It discloses the two *values* and omits the two *validity conditions*. **This is my sharpest finding.**

Docket 19 asked for the fill-factor idealization to be disclosed with a ρC_P
sensitivity row. What was delivered (`run.py:672-682`, `:739-749`,
`tau_thermal_structure_note`, NOTES.md idealization 7):

- `netd_disposition`'s `fill_factor` is left at 1.0 → a dilute host would push
  effective ΔT down → UNDETECTABLE is conservative. ✔
- `mass = ρ_Si·L³` assumes 100%-fill crystalline Si → τ_thermal scales
  linearly in ρC_P → sensitivity rows at φ ∈ {1.0, 0.5, 0.1, 0.01} giving
  dwell/τ = 194.18 / 388.35 / 1941.8 / 19418, each tagged
  `above_N_TRANSIENT_TAU_25: True`. ✔
- §2.3's "decided by the conduction length **alone**" corrected to
  ρC_P L²/(4εσT³L + k_air). ✔

**What is missing.** The same fill factor also scales the *solid* thermal
conductivity, and κ_solid appears in exactly one place: the Biot number, which
`run.py:634` computes as `h_eff·L_cond/K_SI_W_MK` = **k_air/κ_solid**,
length-invariant (Red Team's Iteration-22 Attack 6, LOGBOOK T22). It also sets
the Knudsen number, `λ_air/L_cond`, whose slip correction is −5.32%.

Bi and Kn are not incidental. They are the two quantities **P-TH23-B4 scores**,
and Bi is the sole licence for the entire single-τ lumped-capacitance model
that produces every τ_thermal, every `dwell/τ`, and hence T23's whole
"below-vs-above-25" question. LOGBOOK's own Iteration-22 record establishes,
as a Director-level refinement, that this Biot figure is **material-specific,
not structural**: 0.137 under PMMA, 1.7568×10⁻⁴ under silicon, a 780× swing
from a material-identity change alone. The fill-factor disclosure is precisely
the statement that the material identity may not be 100% silicon — and it is
the one consequence the disclosure does not follow through.

Quantified, using Maxwell–Garnett for high-contrast spherical inclusions
(κ_i ≫ κ_m ⇒ κ_eff = k_air(1+2φ)/(1−φ)), applied to the committed sensitivity
rows:

| fill φ | dwell/τ_thermal (committed) | κ_eff (W/m·K) | **Bi = k_air/κ_eff** | vs. committed 1.7568e-4 | lumped-valid (Bi<0.1)? |
|---|---|---|---|---|---|
| 1.00 | 194.18 | 148 | 1.757×10⁻⁴ | 1× | yes |
| 0.50 | 388.35 | 0.104 | **0.25** | 1420× | **no** |
| 0.10 | 1941.8 | 0.0347 | **0.75** | 4270× | **no** |
| 0.01 | 19418 | 0.0268 | **0.97** | 5520× | **no** |

So the sensitivity table offered as reassurance — "at 10% fill,
`dwell/τ_thermal` = 1942× and the `N_TRANSIENT_TAU`=25 question does not
change answer" (NOTES.md idealization 7) — is evaluated at fill fractions
where the lumped single-τ model that computes "1942×" is no longer licensed,
and the reassurance is *largest* exactly where the model is *most* invalid.
The same fill factor also drives Kn: if a dilute host's real conduction length
is the particle scale rather than the 2.34 µm envelope, Kn ≥ 0.1 for particles
below ~0.66 µm, and the −5.32% slip correction becomes a first-order effect
heading toward the free-molecular regime, where h = k_air/L fails outright.

The honest counter, stated: at the committed headline (φ=1.0) Bi = 1.76×10⁻⁴
and everything is fine, and none of this threatens any UNDETECTABLE verdict —
if the lumped model breaks, the body develops internal gradients, the
*surface* is cooler than the lumped mean at any time before saturation, and
detectability gets *more* conservative, not less. The finding is therefore
about **model validity**, not about the classification. But T23's entire
content is a τ_thermal question, and a τ_thermal that is not a well-defined
single number is a worse problem for T23 than the length-scale ambiguity T23
was opened to settle.

### 1.7 T23's own disposition is stated nowhere durable.

`grep -n "T23" NOTES.md` returns **two hits: the title and the Hypothesis
line**. There is no Learned item about Block B, no Results paragraph stating
whether T23 is resolved, narrowed, or still open, and no `t23_disposition` key
anywhere in `results.json` (grep on `run.py` returns only regime *labels*).
`results.json` marks the mixed regime `"primary_regime"` — which is an
implicit adoption of a convention, asserted by a label, never argued in any
document that will outlive this directory.

The *argument* for the mixed convention — absorbed power on `w_on` because
that is what `RATIO_ON` was calibrated against; conduction and mass on `r_out`
because Nu=2's own derivation requires a real geometric length of the
conducting body — exists in exactly one place: **`phase1_proposal.md` §2.3,
the one document in this directory with no superseded banner and a dozen
struck claims elsewhere in it.** A future seat citing exp-046 for T23 will
find a number with no reasoning attached, or reasoning inside a document it
has been given no signal to distrust. That is the propagation failure mode,
running in the opposite direction from §1.3 but from the same missing banner.

Meanwhile the cycle's five Learned items are: propagator out-of-regime,
gate-target validity, grid-extension-falsifies-prediction, the dimensionless
dwell, and the `--only` wiring bug. **Not one of them is about Block B.** The
lead seat's own Tier-1 #2 deliverable produced no recorded lesson.

### 1.8 Two findings in Block A and the trust suite that no Phase-2 seat could have made.

**(a) A5's two best numbers are conditioning artifacts, by the cycle's own
metric.** `lab/ambient.py:53` defines C = B_obj/B_flank − 1, so 1+C *is* the
object/flank flux ratio — the physically meaningful currency. At A-v2 and A-v3
the beam has walked entirely out of the object window and C sits at −0.997 /
−0.987, i.e. 1+C = 3.34×10⁻³ / 1.338×10⁻². Converting the committed
agreements:

| leg | C_pred | C_fdtd | rel. in **C** (reported) | 1+C_pred | 1+C_fdtd | rel. in **flux ratio** |
|---|---|---|---|---|---|---|
| A-v1 | −0.1233450 | −0.1256977 | 1.91% | 0.8766550 | 0.8743023 | 0.27% |
| A-v2 | −0.9966644 | −0.9969447 | **0.03%** | 3.3356e-3 | 3.0553e-3 | **8.41%** |
| A-v3 | −0.9866179 | −0.9877383 | **0.11%** | 1.33821e-2 | 1.22617e-2 | **8.37%** |
| A-v4 | +0.1636731 | +0.1543757 | 5.68% | 1.1636731 | 1.1543757 | 0.80% |

The compression factor at A-v2 is 8.41/0.0281 = **299×**, and at A-v3
8.37/0.114 = **74×**. `results.json` itself computes those very factors for
the paired object-present legs — `conditioning_amplification` **327.3** at
A-o1 (paired with A-v2) and **81.6** at A-o2 (paired with A-v3) — and docket
item 9 used exactly that conditioning to **drop P-TH23-A7**. The same
conditioning sits underneath A5's two headline-best agreements and is not
mentioned. Nothing here overturns A5 — 8.4% still passes the 15% band, and
the honest spread is 0.27%–8.4% rather than 0.03%–5.68% — but NOTES.md's
"survives the regime change ... to 1.91% / 0.03% / 0.11% / 5.68%", the cycle's
self-declared "result of the cycle," overstates the two best points by two
orders of magnitude in the currency the cycle's own docket treats as the
ill-conditioned one.

**(b) `lab/validation/VALIDATION.md`'s new erratum is retro-dated, and it
over-claims a defect against five historically-correct citations.** NOTES.md
Learned #5 and VALIDATION.md:45-56 state that "Iteration 17's fix silently
dropp[ed] packed tokens in mixed invocations, so `--only 12346789,10,11` —
cited as 46/46 five times in SESSION_LOG — selected only stages 10 and 11."
The *mechanism* is real and I verified it: the token-exact-match rule
(`if len(tokens) > 1: return str(n) in tokens`) landed at commit **6082e02,
2026-08-17**, Iteration 17's close, and it does break that invocation. But
every SESSION_LOG citation of `--only 12346789,10,11` sits at lines 1026,
1155, 1253, 1347, 1455 — the Iteration 9–13 entries, dated 2026-08-14 to
08-16 (the file is newest-on-top), i.e. **all five predate the commit that
created the regression.** Under the code actually in force at each of those
shifts, stages 1–9 matched by bare substring against the whole `only` string
and 10/11 by the digit-boundary regex, so all ten stages ran and 46/46 was
correct. Post-Iteration-17 shifts cite `--only 12346789` (single token,
unaffected), `--only 12,13` and `--only "1,2,...,15"` (all-exact tokens,
unaffected). The `--only 12` half of the erratum **is** correct (it fired
stages 1, 2 and 12, an over-run, harmless). The catastrophic-sounding half is
not.

This matters more than its size. `VALIDATION.md` is the file CLAUDE.md
instructs every agent to read before bench work; it now retroactively impugns
five green-suite citations that were valid when made. It is the *mirror image*
of the fix-docket pattern — a defect claimed but not delivered — and it landed
uncaught because it was authored at Phase 4, after every adversarial seat had
spoken.

---

## 2. Physical meaning — what this cycle actually tells us about where the energy goes

1. **The thermal ledger's insensitivity to the T23 dispute is now structural,
   not empirical.** τ_thermal = ρC_P L_c²/(4εσT³L_c + k_air) is independent of
   the power length; the radiative channel carries 0.046% of the loss at this
   geometry, so τ ≈ ρC_P L_c²/k_air and the *only* levers are the conduction
   length and ρC_P. T23's operative question ("below or above
   `N_TRANSIENT_TAU`=25") is therefore decided by conduction geometry and
   heat capacity alone, and it is answered "above" by a wide margin under
   every disclosed variation the cycle offers: 194× (cube, φ=1), 97× (true
   disk), 388–19418× (φ=0.5–0.01), and 21× only under the `w_on`-everywhere
   convention that the cycle argues (correctly, in my judgment) is not
   licensed for conduction. **T23's operative content can be closed; its
   nominal content — which length is licensed — is closed only by an argument
   that lives nowhere durable (§1.7).**

2. **`N_TRANSIENT_TAU` was never the right stake anyway, and the cycle proved
   it.** `lab/kinetics.py:97` defines it as the RK4-branch switchover for
   `integrate_segments` — a numerical-integration constant for the *kinetics*
   solver. Nothing in the thermal chain is numerically integrated:
   `coupled_kinetics_thermal_dT`, `coupled_segment_general`,
   `steady_state_delta_T` and `transient_delta_T` are all exact closed forms.
   B6's saturation deficits (1 − 5.98×10⁻¹⁰ at 21.2×, ~1 − 5×10⁻⁸⁵ at 194.2×)
   are physically indistinguishable. The consequential difference between the
   conventions is `dt_ss_full` — 3.03× vs the `w_on` regime, 9.15× vs `r_out`
   — and the mixed regime is **the least comfortable of the three** on the
   axis this seat's charter actually scores (607× below NETD_lo, vs 1839× and
   5558×). That is the right thing for this seat to have adopted as primary,
   and I endorse it: a charter that asks "what re-radiates and would it be
   detectable" should default to the convention that predicts the largest
   signature.

3. **Dose accumulation is a dwell/lifetime ratio, not a material property.**
   `ratio_∞ = 1/(1 − a·f)`, memory iff `D/τ_k < ln(21f)`. Hosts A/B/C sit at
   D/τ_k ≥ 66.7, a factor 26 past the 2.5445 threshold, so their zero is
   *exact* (measured `|ratio−1| = 0.0` at all 30 negative controls, not
   "small") — a genuinely rare thing to be able to say. All 7 memory
   point-runs are UNOBTANIUM-tier, and 0 of 12 PUBLISHED-tier point-runs show
   any. Physically: no published-tier switchable host has a lifetime within
   10³ of a flashlight sweep dwell, so repeated sweeps cannot build
   population in any material this program can point at. Amendment 3's host
   list is now a mechanism, and Red Team's Iteration-15 tempering of it is
   vindicated exactly.

4. **A radiometric point my own charter should have made and did not.**
   `dt_ss_full` is classified against NETD, but a microbolometer reads
   *radiance*, not temperature. The article here is 2.34 µm in `r_out` — about
   0.24× the 9.885 µm Wien peak — so it is a deep-Rayleigh emitter at its own
   emission band, and ε=0.9 over a geometric area L² overstates its 10 µm
   emission by orders of magnitude. This does not touch the ΔT numbers (the
   radiative channel is 0.046% of dP/dT, so even ε→10⁻³ moves nothing), but it
   means the "607× below NETD" margin is itself a large *under*-estimate of
   the true detectability margin. The direction is safe; the point is that no
   detectability claim in this program has ever converted ΔT to radiance
   through a sub-wavelength emission efficiency, and the sidecar's
   expressibility contract permits that calculation trivially.

---

## 3. Argued next change

**Close T23 in writing, in the LOGBOOK, and attach the Biot/Knudsen validity
condition to the fill-factor disclosure it is missing from.**

Concretely, at this close (all zero-cost):

1. Put the SUPERSEDED banner on `experiments/046-.../phase1_proposal.md`,
   naming "eye-invisible" (§1, B3) and the other struck items, per Iteration
   22's own precedent; correct NOTES.md's "struck everywhere" to "struck from
   every live artifact; the Phase-1 draft is preserved unedited under a
   SUPERSEDED banner per T10's flag-don't-rewrite convention."
2. Add a `t23_disposition` block to NOTES.md's Learned and to LOGBOOK's T23
   entry: the mixed convention is adopted as primary, **with its argument
   restated** (power on `w_on` per `RATIO_ON`'s calibration; conduction/mass
   on `r_out` per Nu=2's derivation requirement), and with the honest
   statement that the operative below-vs-above-25 question is now decided
   robustly (97×–19418× across every disclosed shape and fill variation) while
   the nominal length question is decided by argument, not by measurement.
3. Extend `rho_cp_sensitivity` to carry **`biot_number` and `knudsen_number`
   per row**, computed from a stated effective-conductivity mixing rule, and
   add one sentence to `fill_factor_disclosure`, NOTES.md idealization 7, and
   Amendment 5(b): *a fill factor below unity also lowers κ_eff, raising
   Bi = k_air/κ_eff toward unity and invalidating the lumped single-τ model
   that the sensitivity row's own numbers come from; the ΔT classification is
   unaffected (internal gradients make the radiating surface cooler, not
   warmer), the τ_thermal numbers are.* Ten lines.
4. Tag P-TH23-B1 as a desk-verifiable structural identity in NOTES.md's
   scorecard, matching how A1/A3 were tagged.
5. State the docket-21 override for C1/C4 explicitly ("no detectability claim
   made; block-scope key carries it") rather than leaving the delivery claim
   unqualified.
6. Correct `VALIDATION.md`'s and Learned #5's `--only 12346789,10,11` clause:
   the regression is real for any invocation made after `6082e02`
   (2026-08-17), and **no cited invocation postdates it** — all five
   SESSION_LOG citations were correct under the code in force when made. Keep
   the `--only 12` half, which is correct. Then add the erratum marker at the
   citation sites in SESSION_LOG/LOGBOOK for the `--only 12` cases only.
7. Add A5's flux-ratio column (1+C) beside the C column in `results.json`, so
   the propagator-vs-FDTD agreement is reported in both currencies and the
   0.03%/8.41% split is on the record rather than waiting for a future seat.

---

## 4. Ranked top-3 candidate directions for Iteration 24

**1. The fill-factor / effective-medium thermal-validity closure (this seat's
own charter, and the first thing in eight iterations that could actually
invalidate a τ_thermal number rather than merely re-scale it).** Every thermal
result this program has issued since exp-043 assumes a 100%-fill crystalline
solid inside a module whose own docstring calls the article "a dilute
vapor/aerosol host" (`lab/thermo_sidecar.py:152`). Compute Bi and Kn as
functions of fill fraction under a stated mixing rule across the committed
sensitivity grid, and state the fill range over which the single-τ lumped
model is licensed at all. Zero FDTD cost, ~30 lines, and it converts the
program's most-reused thermal instrument from "correct arithmetic under an
unstated assumption" to "correct arithmetic with a stated validity domain."
It also feeds directly back into T23, which cannot be closed on a τ that is
not well-defined.

**2. VISION's glare/adaptation Tier-W sidecar — now under this cycle's own
hardened, automatic criterion-4 rule.** Phase 3 adopted, unconditionally: if
Iteration 24 closes without it, Checkpoint criterion 4 fires automatically,
no debate, no discretion (`phase3_synthesis.md` §"Director's own call on item
24"). The tripwire had already tripped at Iteration 23 and was carried in
prose; the hardened form is now on the record and it binds Iteration 24. This
is not a preference of mine — it is a rule the cycle I am reviewing wrote for
its successor, and my ranking reflects that it outranks anything discretionary.
Its blocker (T18/WebFetch, eleven-plus consecutive confirmations) is real, and
the WebSearch-snippet-tier convention `WitnessScenario` already uses is the
adaptation.

**3. The radiance conversion for every detectability claim this program has
issued.** Convert ΔT to spectral radiance through a sub-wavelength emission
efficiency at the article's own size parameter (2r/λ_emission ≈ 0.47 here),
and re-score the whole UNDETECTABLE ladder in the currency a microbolometer
actually integrates. Every margin will get *more* comfortable, possibly by
several orders — which is precisely why it should be done: this seat has been
issuing detector verdicts through a temperature proxy for eight iterations
without ever stating the proxy's own conversion factor, and the honest version
of "UNDETECTABLE" is the one that names the instrument's real input. Analytic,
zero FDTD, and squarely inside the expressibility contract.

*(Carried, not ranked: extend `coupled_segment_general` to the swept host/ratio
grid beyond the 8 points closed at Iteration 22 — largely subsumed by Block C
this cycle; PHOTONICS' R3 recheck of exp-044's 0.45% achromatic flatness; T21's
contamination-risk re-score, still blocked on the missing sourced flashlight
coherence length; `realizability_tier` de-duplication.)*

---

## 5. VERDICT

# PARTIAL

**What closed cleanly.** Every Block-B and Block-C headline number survives
independent hand re-derivation with zero defects — including the ones I most
expected to break, since this seat wrote them. The dose-accumulation closed
form is a real result: a five-host empirical list replaced by one dimensionless
number, exact zeros at 30 negative controls, all 7 memory point-runs confined
to the grid's UNOBTANIUM corner, verified at 250/250 duration-scan points. No
UNDETECTABLE classification is threatened anywhere across 2496 + 42 + 250
points, and the structural argument for that (τ ⊥ L_power; the radiative
channel is 0.046% of the loss) is sound. `REALIZABILITY_MEMO.md` Amendment 5
was actually written, verified in the file and in the commit — the specific
failure that fired a Checkpoint discussion at Iteration 21 did **not** recur.
"Eye-invisible" is genuinely gone from every live artifact, and the NETD
disclaimer genuinely appears wherever a detectability claim is made. Block A's
honest deliverable — a desk propagator validated two-plus orders of Fresnel
number outside where it was built — survives even after my conditioning
correction reads it as 0.27%–8.4% rather than 0.03%–5.68%.

**Why not PROMISING.** Four things did not close, and three of them are the
program's own named failure pattern reproducing in the cycle immediately after
the one that invented the fix for it:

- The fill-factor disclosure (docket 19) is physically incomplete: it discloses
  the two *values* affected (ΔT, τ_thermal) and omits the two *validity
  conditions* (Bi, Kn) — the very quantities P-TH23-B4 scores — leaving a
  reassurance table whose comfort grows precisely as the model producing it
  becomes invalid (Bi 0.25 → 0.97 across the φ=0.5 → 0.01 rows).
- T23, the thread this cycle was chartered to resolve, has its disposition
  stated in no durable document; its argument survives only inside an unflagged
  Phase-1 draft with a dozen struck claims in it, and no Learned item mentions
  Block B at all.
- `phase1_proposal.md` carries no SUPERSEDED banner while NOTES.md claims the
  Phase-1 "eye-invisible" language is "struck everywhere" — false as a claim
  about this repository, at exactly the two loci docket 20 names.
- The newly-committed `VALIDATION.md` erratum retro-dates a real regression
  onto five citations that predate the commit that created it — an over-claimed
  defect in the one file every agent is instructed to read before bench work.

None of these moves a physics verdict. All of them are the same species this
program has now caught in 8 of 9 iterations, and the honest reading is that
the pattern is structural to the panel's process, not to any one seat's care.
It reproduced in the cycle where this seat led, was warned about at Phase 2 by
VISION and by Red Team, and was written into the docket as items 20/21/22 —
and it still reproduced, in the one document the docket's own remedy (a
banner) was invented for one cycle earlier. **PARTIAL**, and I would say the
same if another seat's name were on it.

---

## Verification log — what I actually ran

**Files read in full:** `PANEL.md`; `LOGBOOK.md` RULED OUT (R1–R3), ESTABLISHED,
LIVE THREADS T1/T5/T22/T23, Iterations 21 and 22 in full;
`experiments/046-.../phase1_proposal.md`, `phase2_critique_vision.md`,
`phase2_redteam_audit.md` (Attacks 11–13, overall ruling, full 24-item docket,
verification appendix), `phase3_synthesis.md`, `NOTES.md`;
`lab/thermo_sidecar.py:135-243`; `lab/ambient.py:36-56`;
`lab/validation/run_all.py:1383-1440`; `lab/validation/VALIDATION.md:1-60`;
`experiments/034-.../REALIZABILITY_MEMO.md:160-233`;
`experiments/046-.../run.py:125-133, 609-760, 765-805, 1039-1120, 1159-1300,
1385-1560`; `results.json` blocks `block_b_mixed_length_scale_regime`,
`block_a_fdtd.P-TH23-A5`, `exploratory_object_present`, prediction bands.

**Greps run:** `eye-invisible|eye_invisible` across NOTES.md (1, the strike
record), run.py (3, all negations/strike records), results.json (2674, all
inside the negating sentence), predictions_frozen.txt (5, all negations),
phase1_proposal.md (**2 live at :46 and :342**); `superseded|struck|banner` on
046's phase1_proposal.md (**zero**) vs. 045's (banner at lines 1–11);
`NETD_DISCLAIMER` call sites in run.py (13: `:641, :718, :788, :800, :815,
:924, :940, :1097, :1140, :1394, :1493, :1552` + definition `:125`);
`T23` in NOTES.md (**2: title + hypothesis**); `fill_factor|dilute|aerosol` in
`lab/thermo_sidecar.py` (`:152` "dilute vapor/aerosol host", `:188/:200/:213`
the multiplier); `--only` and `46/46` across SESSION_LOG.md and LOGBOOK.md.

**Git checks:** `git log --oneline -15`; `git show --stat --format="" 460f018`
(REALIZABILITY_MEMO.md +72, NOTES.md +345, results.json, run.py +112,
VALIDATION.md +57, run_all.py +64); `git show --stat --oneline a7eaaf8`
(predictions + run.py + run_all.py, **zero results.json** — the freeze is
structural, confirmed); `git show a7eaaf8 --format="" -- lab/validation/run_all.py`
(the pre-Iteration-23 `_stage_selected`, showing the `len(tokens) > 1` exact-match
rule being replaced); `git log --format="%h %ad %s" --date=short -- lab/validation/run_all.py`
(the exact-match rule introduced at **6082e02, 2026-08-17**);
`git show 6082e02 --format="" -- lab/validation/run_all.py` (confirming
`tokens = re.split(...)` / `if len(tokens) > 1` first appears there).

**Hand re-derivations (no code executed — Python was unavailable in this
context):** the full Block-B chain from `DX`, `R_OUT`, `SIGMA_EXT_ON`,
`RATIO_ON`, `k_air`, ρ, C_P, κ, ε, T, irradiance and dwell (table in §1.1);
τ_thermal's closed form and its L_power-independence; the 0.046% radiative
fraction; the 9.1434-vs-9.15192 discrepancy as the radiative signature; Block
C's grid counts (21 / 42 / 30 / 12 / 7), every `ratio_∞` value at Host D r=1.0
and all five Host-E points at both gaps, `ln(21e^(−0.5))=2.5445224`,
`ln(21e^(−0.4545455))=2.58998`, the r=1.0/m=5 supremum 1.0894; B5's and C3's
ceilings from `n_eq` × `dt_ss_full`; the four A5 legs converted to the 1+C
flux-ratio currency; Maxwell–Garnett κ_eff and Bi across the four committed
fill rows.

**Ruled-out check:** nothing in exp-046 or in this review resurrects R1, R2 or
R3, and nothing above contradicts an ESTABLISHED LOGBOOK finding. The T22
`h_conv`/`mass_kg` re-derivation, the T23 mixed regime, and Block C's dose
extension are all consistent with T22's and T23's committed text; the §1.6
Biot finding *extends* Iteration 22's own material-specificity refinement
rather than contradicting it.
