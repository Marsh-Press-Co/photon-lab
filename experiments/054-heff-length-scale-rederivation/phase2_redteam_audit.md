# exp-054 Phase 2 — RED TEAM audit (last, with everything)

Panel Iteration 31. Reviewed: `phase1_proposal.md` plus all five blind
critiques (photonics, materials, em, quantum, vision). Every load-bearing
claim below was independently re-verified against `lab/thermo_sidecar.py`,
`lab/kinetics.py`, `experiments/043-.../results.json`,
`experiments/045-.../run.py` + `results.json`,
`experiments/046-.../{phase1_proposal,phase5_redteam_audit}.md`,
`REALIZABILITY_MEMO.md` lines 206-224, and `LOGBOOK.md` Iterations 20/22/23/25
— not taken from the proposal's or the critiques' own prose.

## Numbered attacks

**1. [inconsistency] P-054-6 mischaracterizes the very estimate it claims to refute.**
The proposal's own opening line frames this whole cycle as "replacing
Iteration 25's informal, not-run ~5.1×→~2.6× / ~27,080×→~38–42× estimates
with real numbers," and P-054-6 predicts these corrected margins will land
"REFUTED, not confirmed... 2–3 orders of magnitude ABOVE the informal
guess." I traced that estimate to source: `experiments/048-evidentiary-
chord-closure/NOTES.md` ("THERMODYNAMICS' own Phase-2 finding (**witness-
scale** `h_eff` unverified)... THERMO also computed... that **the
correction** shrinks this program's two thinnest detectability margins
[5.1×→2.6×; 27,080×→38–42×]") and `experiments/049-.../
phase5_review_thermodynamics.md` ("Resume the queued `h_eff` re-derivation
... ~5.1×→~2.6× **under the T8/T13/T14 correction**"). T8 is LOGBOOK's own
named live thread for the **near-field→witness-scale bridge**
(`LOGBOOK.md:352`), a completely different axis than the bench-scale
`r_out`-vs-`w_on` question this cycle formally derives. exp-054's own
Idealizations section explicitly disclaims that axis: *"Bench-scale, not
witness-scale... T8/T13's near-field→witness-scale bridge remains
separately unresolved and is not attempted here."* The proposal therefore
both claims to replace a witness-scale estimate and explicitly declines to
do witness-scale work — it cannot do both, and P-054-6's "REFUTED, not
confirmed" verdict compares a bench-scale-only figure against an estimate
of a different physical correction. The stated cause of the discrepancy
("the dominant effect... is Iteration 20 Phase-5's own finding that fixing
h_conv=5.0...") is a plausible guess, not something this cycle verifies —
it never computes what the T8/T13/T14 witness-scale correction would give.
**Nobody else caught this — not even Phase-5's own six-seat T23 audit,
which is unsurprising since exp-054 is the first cycle to state the
comparison explicitly.**

**2. [inconsistency] EM's Attack — CONFIRMED, load-bearing, and sharper on inspection.**
Verified directly in `experiments/045-.../run.py:557-558`:
`block_c_dose_accumulation_kinetics` computes both the decoupled proxy and
the "exact" `coupled_segment_general` comparator using `dt_ss =
regime_w["dt_ss_full_K"]` / `tau_th = regime_w["tau_thermal_s"]` — the
`w_on`-consistent regime exclusively (τ_thermal=3.14ms; the printed
`exact_vs_decoupled_ratio_first`=0.9658 for the first grid point confirms
EM's cited 0.966–0.987 conservative range). The mixed chain's τ_thermal is
**bit-identical to `r_out`-consistent's** (0.343ms — confirmed via
`results.json::block_b...r_out_consistent.tau_thermal_s`=
3.4332969490950116e-4, and via T23's own `P-TH23-B1`, "mixed regime's
dwell/τ_thermal equals the `r_out`-consistent value identically"), i.e.
9.15× shorter, genuinely untested for the conservativeness property. EM's
attack is real and its fix is the correct one.
**Compounding wrinkle EM did not flag**: the proposal's own Phase-4 docket
item (c) promises to "re-run exp-045's Block C dose-accumulation grid
through the corrected chain," but P-054-3's stated basis is pure algebraic
rescaling of the *already-computed* `w_on`-consistent headline number
(×3.0284), not a fresh evaluation of `coupled_segment_general` at the new
`dt_ss`/`tau_th`. These two descriptions of what Phase 4 actually does are
in tension. **The fix for both problems is the same one**: implement Block
C as a genuine re-run of `coupled_segment_general` at the mixed chain's own
`dt_ss_full`/`tau_thermal_s`, not a post-hoc scaling of the old numbers —
this satisfies docket item (c) literally and produces EM's requested
exact-vs-decoupled check as a free byproduct, rather than needing it bolted
on as a separate gate.

**3. [inconsistency] MATERIALS' Attack — CONFIRMED, load-bearing, verified verbatim against source.**
`REALIZABILITY_MEMO.md:206-224` reads exactly as MATERIALS states: silicon
ρ/C_p/κ is **"Relabelled `ASSUMED — provenance terminates unsourced
(T18)`"** because exp-037's citation traces to the unsourced phrase
"standard *cited* thermal constants," grep-confirmed to have no DOI or
handbook reference anywhere in exp-037. exp-054's own parameter table
restates the identical three numbers as a plain sourced citation
(`experiments/037-.../NOTES.md:828-829`) with no ASSUMED flag — silently
reverting a load-bearing provenance caveat this exact discipline filed one
cycle ago in this program's own most durable realizability record. Also
confirmed: `mass_kg=ρ_Si·L³` assigns 100%-fill crystalline silicon
throughout, undisclosed at the point of the proposal's own claim that
`r_out` is "the one length that is actually a physical property of the
conducting, radiating solid" — the memo's own text calls this exact host
"dilute vapour/aerosol" elsewhere in the same module family. Both halves of
MATERIALS' attack check out against source, not just against the
proposal's prose.

**4. [inconsistency] The proposal's own "cross-consistency" trust-suite gates are largely vacuous against the bug class they exist to prevent.**
P-054-7 names two of the three new identity checks: `h_eff·L == k_air`
exactly, and `mass_kg` built from the same `L`. Both are **tautologically
true for any `length_m` the caller passes** — `gas_conduction_h_eff(k_air,
L) = k_air/L` satisfies `h_eff·L==k_air` by construction regardless of
whether `L` is `r_out` or `w_on`; `lumped_cube_mass_kg(density, L) =
density*L**3` satisfies the second check the same way. They verify the
helper functions apply their own formula correctly, not that the **caller
chose the physically-licensed length** — exactly the failure mode Red Team
struck at Iteration 22 (mixing `r_out`/`w_on` inside one claimed-consistent
chain, "never a legitimate physical reading, only a bug," per exp-045's own
docstring). The *only* genuinely discriminating gate in the docket is the
third one: bit-for-bit reproduction of the single already-published
3.293076×10⁻⁵K figure — a single-point regression anchor, not a structural
guard, for a module explicitly being promoted as reusable beyond this one
call site. A future caller who accidentally passes `w_on` into the
`h_eff`/mass helper at some other article (`graded_black_shell`, a future
host) would trip neither of the first two gates and would only be caught
if that specific article also happens to have a pinned regression value —
which it won't, since this cycle only touches two articles.

**5. [inconsistency, minor/non-blocking] The "physical" `r_out` regime is itself a square/cube idealization, not the module's own real disk geometry — a claim gap, not a numeric one.**
The mixed chain's `area`/`mass` (via `lumped_cube_mass_kg`, mirroring
exp-045's `self_consistent_regime`) use `area=r_out²` (a square) and
`mass=ρ·r_out³` (a cube) — the *same* iso-sq/cube convention `w_on` uses,
just anchored at a different length. This is **not** the module's own
"geometric disk" convention (`area_m2 = π·r_out²`, used for the weak-tau
branch, stored as `geometric_disk_area_m2` in exp-045's own
`results.json`) — the two conventions differ by a factor of π on area and
more on volume. The proposal's prose ("r_out, the one length that is
actually a physical property of the conducting, radiating solid") reads as
claiming more geometric fidelity than the construction delivers: neither
regime uses the bench's *actual* disk cross-section; the real discriminator
is which *length* is used, not that one chain is "real geometry" and the
other isn't. **Downgraded to non-mandatory**: this is disclosed at the
idealization-bullet level ("cube-shaped thermal mass... not a true-disk...
model"), and exp-046's own true-disk sensitivity check already found the
operative conclusion survives at 97× (still far above the 5× UNDETECTABLE
floor) — so it does not threaten P-054-2/4's bands. Recommend one sentence
change: "the one length that is a physical LENGTH SCALE of the conducting
solid," not "a physical property of the conducting, radiating solid."

**6. PHOTONICS' Attack — CONFIRMED accurate, DOWNGRADED to non-load-bearing.**
Independently checked the arithmetic: `w_on/r_out` = 7.079/2.34 ≈ 3.025,
and `Q_ext = w_on/(2·r_out)` ≈ 1.51 — plausible, inside the diffraction-
paradox ceiling (Q_ext→2), but genuinely never checked against a closed
form as PHOTONICS says. The critique is right that "`w_on` is diffraction-
inflated past the real object" is asserted, not bounded against the
`iso_xsec_sq` convention's own contribution to the excess. But this does
**not** change the mixed-chain's conclusion: the argument for routing
`h_eff`/mass/area through `r_out` only requires that `w_on` is *not* a
geometric length of the solid — it holds whether the excess is 100%
diffraction or partly a convention artifact. Recommend as a follow-up
(a desk Q_ext(x) cylinder check), not a blocker for this cycle.

**7. QUANTUM's Attack — CONFIRMED accurate, elevated to MANDATORY given this program's own precedent.**
Verified directly: `lab/kinetics.py::integrate_two_state` raises
`NotImplementedError` on any non-`None` `I_profile` ("k_f is taken as a
given constant, not re-derived from I(t)"), and exp-045's Block C `RATIOS`
grid is a bare exogenous multiplier on `k_r_d`, never touching
`sigma_ext`/`w_on`/`r_out` anywhere in `run.py`. QUANTUM's scope-boundary
concern is real. This is the *exact* species of risk Iteration 23's own
Phase-5 close named as a standing pattern: "an analytic length scale
calibrated for one physical quantity is not automatically safe to reuse for
another" — undisclosed idealization boundaries have already cost this
program a multi-cycle correction once (T22/T23). One sentence is a trivial
cost against a documented-recurring risk class; elevate from "nice to have"
to mandatory on program-integrity grounds, not physics grounds.

**8. VISION's Attack — CONFIRMED, load-bearing, base rate independently spot-checked.**
Confirmed P-054-2 and P-054-4's rows carry no disclaimer text. Confirmed
the base-rate claim is not exaggerated: `LOGBOOK.md` shows a real
Checkpoint-criterion-4 firing near Iteration 17 (line ~295, "Checkpoint
criterion 4 FIRED") and the Iteration 22/23 NETD/eye-invisible recurrences
VISION cites are independently traceable in the Iteration 20/22/23 sections
already read for this audit. This is not VISION restating its own charter
reflexively — it is a documented, repeated, caught-only-by-active-review
failure mode in this exact program, about to mint two new headline
prediction IDs. Adopt VISION's fix verbatim.

## Checked and found clear (no attack)

- **T1 escape route "NONE"** — independently confirmed correct: this cycle
  touches no FDTD scene, proposes no σ(I)/σ(x,t)/angular-selectivity/
  sub-threshold parameter, and matches the Iteration 20/22/25/27
  sidecar-cycle precedent's own T1 disposition.
- **Constraint 3** — grepped `phase1_proposal.md`: zero occurrences of
  "eye," "human," "contrast," "luminance," "photopic," "scotopic," or
  "constraint-3." NETD comparisons stay strictly instrument-scoped. No
  visible-light or human-detectability claim is smuggled in anywhere.
- **Unfalsifiability** — none of P-054-1 through P-054-7 is unfalsifiable
  as stated. Each carries a numeric band, an exact identity, or a pass/fail
  classification that a real Phase-4 run could contradict. P-054-1 is
  disclosed as a low-risk regression anchor rather than a novel physics
  claim (fine, as labeled); P-054-5's basis ("no candidate chain has ever
  produced a margin below 5×") is inductive rather than a physical bound,
  but the prediction itself remains genuinely checkable. Not a Red Team
  strike.

## Overall ruling: **PROCEED-WITH-MANDATORY-FIXES**

The core physics argument — that `h_eff`, thermal mass, and radiating area
belong to the solid's own geometric length (`r_out`), while absorbed power
stays on the calibrated optical cross-section (`w_on`) — is sound,
independently re-derivable from committed data (the 3.293076×10⁻⁵K figure
reproduces exactly from `on_central["p_abs_w"] / dp_dt(r_out)` using
exp-045's own committed numbers), and was already vetted once at Iteration
23's Phase-5 six-seat audit. This is not reject-and-redesign territory. But
attacks 1–4 and 7–8 are real, independently verified, and several are
load-bearing enough that the headline margins should not be treated as
final until fixed.

### Mandatory-fix docket (7 items) — before Phase 3 synthesis commits predictions

1. **Fix or drop P-054-6.** Either re-scope it explicitly ("this cycle
   tests the `r_out`-vs-`w_on` bench-scale question and the `h_conv=5.0`
   placeholder fix; it does not address, and cannot refute, Iteration 25's
   witness-scale [T8/T13/T14] estimate") or remove the comparison. State in
   the LOGBOOK Iteration 31 entry that T8/T13's witness-scale `h_eff`
   question remains open and unaddressed by this cycle.
2. **Implement Block C as a real re-run**, not an algebraic rescaling: feed
   the mixed chain's own `dt_ss_full`/`tau_thermal_s` through
   `coupled_segment_general` for at least the 5τ/0.5τ extremes, and confirm
   `exact ≤ decoupled` holds there before P-054-3/P-054-4 are reported as
   headline (adopts EM's fix; also resolves the docket-item-(c)
   description mismatch).
3. **Restore the ASSUMED — provenance terminates unsourced (T18) label**
   on ρ/C_p/κ everywhere this cycle's parameter table and `results.json`
   keys touch them, and disclose the 100%-fill assumption at the point of
   the `mass_kg=ρ·r_out³` claim (adopts MATERIALS' fix in full).
4. **Strengthen the trust-suite identity stage** so it guards against the
   actual historical bug (wrong length passed to the right formula), not
   just formula self-consistency: at minimum, pin the ON-endpoint call
   site's literal `r_out` *value* (2.34×10⁻⁶ m) in the regression check
   (not only the output figure), and name the helper's argument
   `L_geometric` (not a bare `L`) with a docstring warning against passing
   an optical/extinction-derived length.
5. **Add QUANTUM's one-sentence scope caveat** to P-054-3 and the
   idealizations list: the `n(t)`-independence claim holds only while
   `k_f`/`k_r` remain exogenous rate-constant grid parameters, per
   `lab/kinetics.py`'s standing `I_profile` idealization.
6. **Propagate VISION's disclaimer verbatim** at every locus P-054-2,
   P-054-4, or P-054-5's UNDETECTABLE classification is quoted outside
   `lab/thermo_sidecar.py` itself: new `results.json` keys, NOTES.md
   Results/Learned prose, and the LOGBOOK Iteration 31 entry.
7. **Propagate a forward-pointer into exp-043 and exp-045's own committed
   records** (a short NOTES.md/results.json note, per T10's "flag, don't
   rewrite" convention and the SUPERSEDED-banner precedent this program
   already invented for this exact class of gap) stating that their
   original headline `dt_ss_full`/margin figures are superseded by
   exp-054's corrected mixed-chain numbers — so a future cycle citing
   exp-043/045 does not silently re-cite the pre-correction figures.

### Non-mandatory, recommended

- A desk Q_ext(x) cylinder closed-form check bounding how much of
  `w_on`'s excess over `r_out` is genuine diffraction vs. the
  `iso_xsec_sq` convention (PHOTONICS' request) — informative, not
  load-bearing for this cycle's numbers.
- Reword "the one length that is actually a physical property of the
  conducting, radiating solid" to "a physical length scale of" — the
  mixed chain's `r_out` regime is still a square/cube idealization, not
  the bench's true disk geometry (attack 5).
