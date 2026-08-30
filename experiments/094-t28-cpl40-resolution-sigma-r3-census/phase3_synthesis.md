# PHASE 3 — DIRECTOR SYNTHESIS · Panel Iteration 71 · exp-094

*Director: this shift's runner (photonlab-shift, cloud panel routine). Input:
`phase1_proposal.md` (QUANTUM OPTICS, lead per rotation), five blind Phase-2
critiques (PHOTONICS, MATERIALS, ELECTROMAGNETISM, THERMODYNAMICS, VISION
SCIENCE — all independently returned support-with-changes, five distinct,
non-overlapping catches, zero overlap), and `phase2_redteam_audit.md`
(PROCEED-WITH-MANDATORY-FIXES, 5 items, zero overridden).*

## 0. Director's own independent re-verification (third derivation of the
one disputed figure set, before accepting Red Team's ruling on faith)

Before adopting RT-2's correction, independently re-pulled the raw JSON a
third time (Red Team's own re-derivation was the second; PHOTONICS' was the
first):

```
41.6° (native sigma, experiments/091-.../results.json):
  delta_scene=1.78376e-04  frac_contrast=3.32960e-04  ratio_k=25.9467
  frac_p_abs=8.63922e-03   floor_pass=True

exp-093 item1 interior sweep, floor-clearing points (experiments/093-.../results.json):
  41.825° ratio_k=29.5769  frac_p_abs=5.79107e-03
  41.850° ratio_k=25.1088  frac_p_abs=5.39591e-03
  41.875° ratio_k=22.2585  frac_p_abs=4.98647e-03
  41.900° ratio_k=20.4774  frac_p_abs=4.56418e-03
```

Bit-exact match to both PHOTONICS' and Red Team's own citations. **41.6°'s
`ratio_k=25.9467` sits inside the interior sweep's own 20.48–29.58 range**,
not the far-from-null population's 0.076–3.841 range. `frac_p_abs` at 41.6°
(0.008639) runs ~1.5–1.9× the interior sweep's own values (0.00456–0.00579)
— same order of magnitude, confirming "near-flat, not the driver of the
`ratio_k` swing" as PHOTONICS/Red Team both concluded, though this Director
notes the ~1.5–1.9× gap is itself non-trivial and is folded into the
corrected Rank 2 language below as a disclosed, not glossed-over, feature.
**RT-2's correction is adopted verbatim, independently re-confirmed a third
time.**

## 1. Disposition of all Phase-2 findings

| # | Critic(s) | Finding | Red Team ruling | Director disposition |
|---|---|---|---|---|
| 1 | MATERIALS + EM (convergent) | No gate reads the constructed `Sim`'s own `sigma_e` array; a runtime sigma-wiring bug in the new `R4` family would sail through every static gate — reproduces R15's founding defect | CONFIRMED, MANDATORY (MATERIALS' runtime-array-read fix is the one that actually discharges it; EM's own proposed static assert independently shown algebraically tautological, does not substitute) | **ACCEPTED IN FULL.** New gate 5 (runtime, per-call) added to §2.4 below. EM's static assert retained as a documentation-only gate 6, explicitly labeled non-discriminating, not a substitute. |
| 2 | PHOTONICS | Rank 2's "CONFIRM is more likely" lean inverts R13/R14's own established ratio_k/near-null relationship | CONFIRMED, independently re-derived, MANDATORY same-shift fix, non-load-bearing to gates/bands | **ACCEPTED IN FULL**, independently re-verified a third time (§0 above). Rank 2 §4 language corrected below. |
| 3 | EM (secondary) | Rank 2's qualitative lean is `cpl=30`-only-established, provisional pending Rank 1b | Subsumed into RT-2's fix, not separate | **ACCEPTED, folded into the same edit** — no residual directional lean is retained for Rank 2 after RT-2's correction, so no separate provisionality clause is needed. |
| 4 | VISION SCIENCE | Ambiguous whether Rank 2/3 invoke `pair_metrics` or `pair_metrics_full`; if `_full`, NETD byproducts could land undisclosed | CONFIRMED by tracing actual exp-093 call sites (item1/item3 both call `_full`), MANDATORY | **ACCEPTED IN FULL.** Stated explicitly below: Rank 2/3 call the `_full` variants (matching exp-093's own item1/item3 idiom, verbatim reuse — no alternative was ever coded). The top-level `netd_disclaimer` convention from `experiments/093-.../results.json` is carried into this cycle's own `results.json`, unconditionally. |
| 5 | THERMODYNAMICS | Rank 1's new `cpl=40` cells carry no `p_abs_w`-vs-T9-anchor check despite zero marginal cost | CONFIRMED real and free, MANDATORY | **ACCEPTED IN FULL.** Added to Rank 1b's §4 predictions below, plus a new Idealization stating the energy-flatness finding is `cpl≤30`-verified only. |
| — | Red Team housekeeping | Idealization 18 should credit EM's from-first-principles re-derivation of `SIGMA_CORRECTED(RATIO)=SIGMA_NATIVE/RATIO`, not just empirical pattern-match | N/A (own finding) | **ACCEPTED**, Idealization 18 updated below. |

**Zero criticisms overridden.** All five Phase-2 critiques' underlying
findings, and all five of Red Team's mandatory fixes, are adopted without
exception — the proposal's core design (the `R4` geometry family, the call
budget, the cheapest-first sequencing, the T1/Realizability N/A framing)
survives independent re-verification intact and required no structural
change, only the five named corrections/additions.

## 2. Checkpoint ruling (Director's own, matching Red Team's)

None of PANEL.md's five checkpoint criteria fire. Criterion 4's non-firing
is conditional on the five mandatory fixes actually landing in this
document and `NOTES.md` before freeze — **they do, below, before this
document's own commit.**

## 3. Frozen configuration

See `NOTES.md`, this cycle's frozen spec, committed in the same push as
this document, strictly before any Phase-4 code exists. All five mandatory
fixes are incorporated there. Full change log against `phase1_proposal.md`:

1. §2.4 gains a new **gate 5** (mandatory, runtime): immediately after each
   `build_article_r4_sigma(sim, cx, cy, sigma_max)` call in Rank 1a/1b,
   before any FDTD step, assert
   `np.isclose(sim.sigma_e[shell_mask].max(), sigma_max, atol=1e-9)` where
   `shell_mask` selects the article's own shell cells (mirroring how
   `build_article_r4_sigma` itself indexes them) and `sigma_max` is the
   exact value passed at that call site. This is the discriminating check;
   it is new house machinery (first runtime-array sigma gate anywhere in
   this sub-thread's history) and is itself an absolute identity gate
   (fails loudly, pre-FDTD, on any wiring mismatch) satisfying PANEL.md's
   "new machinery ⇒ new gate" requirement.
   A **gate 6** (documentation-only, non-discriminating, explicitly labeled
   as such) retains EM's own static assert for the permanent record of its
   physical reasoning, with the caveat that it must never be read as
   equivalent to gate 5.
2. Rank 2's §4 "informed lean" paragraph is struck and replaced: 41.6°'s
   `ratio_k=25.9467` (native sigma) sits inside the *same* high-`ratio_k`,
   near-null-adjacent population as the confirmed-fragile interior sweep
   (20.48×–29.58×), not the far-from-null CONSISTENT population
   (0.076×–3.841×) — REFUTE is disclosed as at least as plausible as
   CONFIRM here, not a foreseeable-but-mislabeled surprise. No directional
   lean is stated. (This also discharges EM's provisionality point — no
   residual "settled" framing survives to need qualifying.)
3. New sentence in §2.2/§4: Rank 2 and Rank 3 invoke `cell_metrics_r4`
   (this cycle's own new function, itself calling `pair_metrics_full`'s
   generic form via the already-loaded `_full` machinery — see below) —
   **the `_full` variant, unconditionally**, matching exp-093's own
   item1/item3 idiom exactly (no plain-variant code path exists to choose
   between; this is a statement of fact about already-written reused code,
   not a new design decision). This cycle's own `results.json` carries the
   identical top-level `netd_disclaimer` key `experiments/093-.../
   results.json` established, written unconditionally at the top level of
   the output, regardless of whether any NETD field is ever printed to
   `run_output.txt`.
4. Rank 1b's §4 gains a new informational, non-gating check: `p_abs_w`
   ratio (G4/C4 config, per angle) expected within 2–5% of the 0.51 T9
   anchor, computed at zero additional FDTD cost from the already-budgeted
   32 calls (mirrors Rank 2b's own existing check). New **Idealization
   23**: exp-093's own energy-flatness/UNDETECTABLE finding (item 5b,
   Learned #2) is verified at `cpl∈{20,30}` only; this cycle's Rank 1b
   `p_abs_w` check is this sub-thread's first test of whether that finding
   is itself resolution-robust at `cpl=40` — a genuinely new question, not
   assumed answered by extension.
5. Idealization 18 updated: `SIGMA_CORRECTED(RATIO)=SIGMA_NATIVE/RATIO` is,
   per EM's own independent Phase-2 re-derivation (confirmed here against
   `lab/fdtd2d.py`'s own E-update/loss coefficient), derivable from first
   principles as the condition holding the shell's accumulated optical
   depth `2·σ·r_out(cells)` invariant under a pure grid-density rescale —
   not merely an empirical pattern-match confirmed at one ratio (`R3`,
   1.5×) and extrapolated to a second (`R4`, 2.0×). The *value* at
   `R4_RATIO=2.0` is still asserted by gate 4 (unchanged, still necessary
   as the one gate pinning the free numeric input), and gate 5 (new, §above)
   is still required to confirm the derived value is what actually reaches
   the constructed object — this update is to the *justification's*
   epistemic status, not a claim that any check becomes unnecessary.

No other change to the proposal's substance, budget, sequencing, geometry,
or falsifiable bands. Total FDTD call count unchanged: **48**.
