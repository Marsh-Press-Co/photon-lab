# PHASE 3 — SYNTHESIS · Panel Iteration 44 · Director

Resolves MATERIALS' Phase-1 proposal, five blind Phase-2 critiques
(PHOTONICS, ELECTROMAGNETISM, THERMODYNAMICS, QUANTUM OPTICS, VISION
SCIENCE), and Red Team's Phase-2 final audit (verdict:
**PROCEED-WITH-MANDATORY-FIXES**) into ONE testable configuration —
candidate exp-067.

## Accepted / overridden

**All five Phase-2 critiques' load-bearing findings are ACCEPTED, exactly
as reconciled by Red Team's own docket (§2.1 of
`phase2_redteam_audit.md`). None overridden; nothing struck.** Red Team's
own audit independently re-derived every numeric claim against primary
artifacts (not seat prose) before ruling — including building and running
the alternate "replace-rear" model itself (A1) rather than taking EM's
flip condition on faith — and found every critique's load-bearing claim
confirmed, not overreach. This Director adopts that ruling without
override.

- **EM's topology attack (A1) — accepted as mandatory, not optional.**
  Confirmed materially consequential, not marginal: at the proposal's own
  Stress-B test point, the series-only design reports the witness margin
  as "nearly erased" (≈1.0047×) while the alternate replace-rear model
  reports "comfortably clear" (≈1.174×) — a verdict flip, not a rounding
  disagreement. **Fix applied**: `bonded_substrate_conduction_correction`
  now computes and returns BOTH endpoints —
  `correction_factor_series` (EM/A1's confirmed worst-case bound, kept)
  and `correction_factor_replace_rear` (the new complementary endpoint) —
  at every test point, with neither privileged as "the" answer.
- **PHOTONICS' α_true/e-fold arithmetic correction (A2) — accepted,
  independently re-derived by Red Team from exp-061's own committed
  `tau_true=8.2588`/`thickness=1440nm` figures.** `L/e-fold_real =
  tau_true ≈ 8.26` exactly by construction at every witness point (not
  "1,900–6,000×"); median absorption depth ≈8.4% of L, inside PHOTONICS'
  claimed 8–12% band. Does not change any R_contact arithmetic (R_contact
  enters via `h_combined(L)`, independent of where within L absorption is
  generated) — it is a documentation correction, applied below and in
  NOTES.md, not a code change.
- **QUANTUM's gate-completeness + dict-propagation attack — accepted in
  full.** The Phase-1 draft's Section 3 specified only a stage-23-style
  three-gate set plus a stage-24-style source-scan (4 gates total,
  missing the refusal-identity and `inspect.signature` gates entirely,
  and never committing to writing `r_contact_provenance`/
  `r_contact_diagnostic_only`/an honesty-note into the return dict).
  **Fix applied**: stage 25 now carries all SIX gates specified in Red
  Team's docket §2.1, mirroring stage 24's full four-gate-kind discipline
  plus stage 23's regression/bisection pair; the return dict literally
  carries `r_contact_provenance`, `r_contact_diagnostic_only`, and
  `r_contact_realizability`.
- **THERMODYNAMICS' `model_note`/`netd_disclaimer` correctness attack —
  accepted, with one disclosed Director judgment call (not a silent
  substitution).** Red Team's own docket text asked for a `model_note`
  that textually DIFFERS between `r_contact=0` and the primary anchor.
  This Director instead wrote a `model_note` that (a) states the series
  form is a one-sided worst-case bound, (b) names the replace-rear
  endpoint as the complementary case, and (c) reads IDENTICALLY at every
  `r_contact` value — a general, always-correct two-endpoint description
  rather than a per-value one. This closes the SAME staleness risk
  THERMODYNAMICS' attack targeted (there is no copied-then-partially-
  edited string that can go stale, because nothing is ever partially
  edited), by construction rather than by a value-dependent branch.
  Disclosed here explicitly as a deviation from Red Team's literal text,
  flagged for Phase-5 scrutiny rather than silently substituted. Gate
  3(b)/3(c) test the property actually needed (not silently copied from
  the wrapped call; names both endpoints), not the literal "differs
  between two r_contact values" wording.
- **VISION's Secondary-scope attack — accepted; the ask is NOT folded in
  this cycle.** VISION's own empirical record (exp-065: 144 FDTD calls,
  full cycle; exp-066: 39 calls, full cycle — both dedicated wholly to
  T27 and both still left Block ARTICLE/interior `FALLBACK_ANGLES`/Block
  MINI open) makes "secondary, if scope allows" on a cycle whose PRIMARY
  item is real desk-code-writing (new function, new guard type, a
  six-gate suite) read as a likely fourth quiet deferral. Per Red Team's
  offered options (A8: a pre-committed capped FDTD budget for Block
  ARTICLE only, OR an explicit disclosed deferral to Iteration 45), this
  Director selects the **explicit deferral**: R_contact's own desk build
  is substantial enough on its own that adding an FDTD leg this cycle
  risks exactly the under-resourced, capacity-short execution both prior
  T27 cycles already demonstrated. Named explicitly in PLAN.md's
  Iteration-45 queue below — not silently dropped.
- **The one arithmetic slip common to THERMODYNAMICS/A6** — `0.6–0.7
  cm²·K/W = 6×10⁻⁵–7×10⁻⁵ m²·K/W` (not `6×10⁻⁵–6.5×10⁻⁵`). Corrected in
  the test-point band below; the tested value 6.5×10⁻⁵ sits inside both
  the original and corrected band, so no downstream number changes.
- **A7 (Red Team's own new finding, no seat raised it)** — accepted as a
  disclosure requirement, not a code change: NOTES.md states explicitly
  which of the two anchors is the closer physical analogy (query 2's
  forest/TIM interfacial figure — a forest-to-external-surface contact,
  architecturally closer to a root/substrate bond — vs. query 10's
  inter-tube vdW figure, an internal microstructure interface), rather
  than let the "primary"/"second" labeling imply an unearned ranking.

## The one testable configuration (candidate exp-067)

**T1 escape route: NONE** — desk-analytic/instrument-trust class (same
class as exp-063/064). Zero constraint-1/2/3/4 metric scored, zero FDTD.

**New `lab/thermo_sidecar.py` machinery** (composes, does not reimplement,
`front_surface_conduction_correction` — this module's own established
reuse discipline):

```python
LICENSED_R_CONTACT_PROVENANCE = frozenset({"measured_direct"})
DIAGNOSTIC_ONLY_R_CONTACT_PROVENANCE = frozenset({"analogy_proxy_diagnostic"})

def _validate_r_contact_provenance(r_contact_provenance, r_contact_diagnostic_only): ...
def _r_contact_realizability_note(r_contact_provenance, r_contact_diagnostic_only): ...

def bonded_substrate_conduction_correction(
        k_air, l_geometric_m, k_solid, emissivity, r_contact_m2k_w,
        t_ambient_k=293.15, *, length_provenance, r_contact_provenance,
        diagnostic_only=False, r_contact_diagnostic_only=False) -> dict:
    ...  # returns BOTH correction_factor_series and correction_factor_replace_rear
```

**New `lab/validation/run_all.py` stage 25** — six gates, reconciling all
five seats' Phase-2 asks (full docket: `phase2_redteam_audit.md` §2.1;
implementation detail/deviation disclosures: stage 25's own docstring in
`run_all.py`).

**Test points** (units m²·K/W throughout; **all points compute and report
both endpoints**):

| Point | R_contact | Basis |
|---|---|---|
| Gate | 0 | identity check — recovers bracket B exactly |
| Primary band, low | 4×10⁻⁹ | query 10 (exp-063), inter-tube vdW proxy, −1 OOM |
| Primary anchor | 4×10⁻⁸ | query 10, inter-tube vdW proxy |
| Primary band, high | 4×10⁻⁶ | query 10, +2 OOM |
| Second anchor | 6.5×10⁻⁵ | query 2 (exp-063), forest/TIM interfacial figure — **the closer physical analogy to a root/substrate bond** (A7); corrected band [6×10⁻⁵, 7×10⁻⁵] |
| Stress A | 1×10⁻³ | speculative |
| Stress B | 1×10⁻² | speculative — EM/A1's headline divergence point |

**Every R_contact value this cycle proposes is honestly
`analogy_proxy_diagnostic`** — none is `measured_direct`. Zero
`measured_direct` R_contact figures were sourced this cycle (WebSearch
barred, per Phase 1's disclosed operational constraint); a real dedicated
literature search remains a queued follow-up (see Next, below).

**`caveat_lint_config.json` — new entry
`exp067-r-contact-analogy-proxy-disclosure`**: any future citation of
this cycle's R_contact-corrected numbers must disclose "analogy-based
proxy, not a directly-measured root/substrate figure," AND (mandatory
fix, this Director's own addition, closing A1's own risk of a stale
citation) must disclose which endpoint (series vs. replace-rear) is being
cited, since the two disagree materially at Stress-B-class R_contact
values. `required_sites` = `NOTES.md` + `phase4_results.md` from the
start (Iteration 41's own fix for the Iteration-40 NOTES.md-only-scoping
mistake, applied here without needing to relearn it).

## Predictions committed before any run

See NOTES.md's own frozen prediction table — every cell computed by
direct invocation of the actual committed `bonded_substrate_conduction_
correction` (this module's own R4 discipline; the same script, same
constants, that `run.py`/stage 25's own regression-anchor and bisection
gates independently reproduce).

## Checkpoint status

Per Red Team's own audit §5 (checked against all five criteria):

1. Configuration passes all constraint metrics — does not fire; zero
   constraint metric scored this cycle.
2. Proven boundary within a mechanism class — does not fire.
3. Synthesis requires engine physics beyond validated bench classes —
   does not fire, on direct precedent (exp-063/exp-064, both explicitly
   ruled non-firing for architecturally identical new-`lab/`-machinery-
   plus-new-trust-suite-stage additions).
4. Program-integrity drift — does not fire at this Phase; every defect
   in Phase 2 was caught blind, before Phase 3 freeze, "the mechanism
   working as designed." **Forward tripwire carried from Red Team's own
   audit, restated**: if a future cycle cites `correction_factor_series`
   alone as "the" R_contact correction without the replace-rear endpoint
   and its Stress-B divergence, that is itself a criterion-4-relevant
   finding at whichever cycle it recurs.
5. Two consecutive iterations with no logbook-advancing result — does
   not fire; Iterations 40–43 each advanced the record substantively,
   and this cycle adds a new, real function plus six new gates.

No Marsh convening required at this phase.
