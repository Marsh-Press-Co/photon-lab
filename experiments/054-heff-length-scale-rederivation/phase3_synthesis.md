# exp-054 Phase 3 — SYNTHESIZE (Director)

Panel Iteration 31. All five Phase-2 blind critiques returned
**support-with-changes**; Red Team's audit ruled **PROCEED-WITH-MANDATORY-
FIXES**, a 7-item docket (`phase2_redteam_audit.md`). This entry states
which criticisms are accepted, which (if any) are overridden, and why —
PANEL.md's own requirement — then freezes the corrected design that Phase 4
actually builds and runs.

## Disposition of every Phase-2 finding

**All 7 of Red Team's mandatory-fix items are ACCEPTED IN FULL. None
overridden.** Every item was independently re-verified against source code
or committed data by Red Team itself (not merely trusted from a seat's
prose), and none conflicts with another — this is a clean-accept cycle, like
Iteration 25's own "no ask rejected" precedent, not a case requiring
Director-level arbitration between competing fixes.

1. **P-054-6 rescoped, not dropped.** Red Team's own attack 1 is the
   sharpest finding of this whole Phase 2: the Phase-1 proposal's framing
   conflated its own bench-scale `r_out`-vs-`w_on` question with Iteration
   25's separate, still-unaddressed **T8/T13/T14 witness-scale** `h_eff`
   estimate. Accepted verbatim. P-054-6 is struck and replaced below with a
   prediction that makes the scope boundary explicit, and the LOGBOOK
   Iteration 31 entry will state plainly that T8/T13's witness-scale
   question remains open.
2. **Block C becomes a genuine re-run**, not algebraic rescaling — adopts
   EM's fix and Red Team's own sharper framing (this also resolves the
   internal description mismatch Red Team caught). New P-054-3 replaces
   the old one.
3. **Silicon identity re-flagged ASSUMED — provenance terminates unsourced
   (T18)**, restored verbatim from `REALIZABILITY_MEMO.md`; 100%-fill
   assumption disclosed explicitly at the `mass_kg` claim. Accepted in
   full (MATERIALS).
4. **Trust-suite identity stage strengthened.** The two originally-named
   checks stay (they are still correct, just not sufficient alone) and a
   third is added: the ON-endpoint call site's literal `L_geometric` value
   is pinned in the regression assertion, not only the output figure. The
   helper's parameter is renamed `l_geometric` (not bare `L`) with an
   explicit docstring warning against passing an optical/extinction-derived
   length. Accepted in full.
5. **QUANTUM's scope caveat added** to the (renumbered) n(t)-independence
   prediction and to the idealizations list: the claim holds only while
   `k_f`/`k_r` remain exogenous rate constants, per `lab/kinetics.py`'s own
   `integrate_two_state` `I_profile=NotImplementedError` boundary. Accepted
   in full.
6. **VISION's NETD disclaimer propagated verbatim** to every locus a
   detectability classification is quoted outside `lab/thermo_sidecar.py`
   itself — every prediction row below, `results.json` keys, and the
   NOTES.md Results/Learned prose. Accepted in full — this is the fourth
   documented instance of this exact recurring pattern (Iterations 17, 22,
   23), so it is treated as load-bearing, not cosmetic.
7. **Forward-pointer into exp-043/exp-045's own committed records.** A
   short addendum will be appended to both experiments' `NOTES.md` (not a
   rewrite of their own committed numbers — T10's "flag, don't rewrite"
   convention) stating that their original `dt_ss_full`/margin figures are
   superseded by exp-054's corrected mixed-chain numbers for anyone citing
   them going forward. Accepted in full.

**Non-mandatory items, both accepted as cheap, low-risk improvements** (not
required by Red Team, adopted anyway since both cost one sentence): the
attack-5 rewording ("a physical length scale of the conducting solid," not
"a physical property of... the solid") — accepted, applied below. PHOTONICS'
Q_ext(x) closed-form check — **NOT** attempted this cycle (Red Team's own
downgrade: informative, not load-bearing); queued for Iteration 32+'s ranked
list instead, stated in the LOGBOOK close-out.

No finding from any seat is overridden. No new criticism is added by the
Director beyond what Phase 2 already surfaced — the synthesis work here is
compilation and one structural decision (§ below), not fresh critique.

## One Director-level structural decision

Red Team's attack 4 asks for the trust-suite regression check to pin the
literal geometric length value, and names the argument rename
(`L_geometric`/`l_geometric`) as part of the same fix. Both are folded into
ONE new stage (stage 18) rather than two separate changes, since they are
the same guard (a wrong-length call would fail the pinned-value check
regardless of the argument's name — the rename is a defense-in-depth
readability fix, not a separate gate). This keeps the mandatory-fix count
at 7 items delivered via one code change, not an inflated docket.

## Corrected, frozen design (what Phase 4 actually builds and runs)

- **`lab/thermo_sidecar.py` additions** (promoted, reusable, per the
  Phase-1 proposal's own commitment): `gas_conduction_h_eff(k_air,
  l_geometric)`, `lumped_cube_mass_kg(density_kg_m3, l_geometric)`, and
  `mixed_length_scale_regime(...)` — P_abs stays on whatever optical
  measurement produced it (`w_on`-based, unchanged); `h_eff`, `mass_kg`,
  and area (`l_geometric²`, the same iso-sq convention `w_on`'s own area
  uses, per the corrected wording — NOT claimed as "more real" geometry
  than that, just a different, physically-licensed *length*) all derive
  from `l_geometric` alone. `absorbed_power_established_ratio` is
  UNCHANGED.
- **New trust-suite stage 18** (`lab/validation/run_all.py`): (a)
  `gas_conduction_h_eff(k_air, l)·l == k_air` exactly, any `l`; (b)
  `lumped_cube_mass_kg`'s output divided by `l³` recovers density exactly,
  any `l`; (c) **the discriminating gate** — the ON-endpoint call site's
  literal `l_geometric` (2.34×10⁻⁶ m, i.e. `r_out_m`) is asserted equal to
  the bench's own committed `r_out_cells·dx_m` product (not a bare
  literal), AND the resulting `dt_ss_full` reproduces the already-published
  3.293076×10⁻⁵ K side-computation (LOGBOOK Iteration 23) to tight
  tolerance. All three gates zero-FDTD, desk-only.
- **exp-054/run.py**: computes `mixed_length_scale_regime` for the
  ON-endpoint (τ=3.9) using exp-043's committed `p_abs_w`, `r_out_m`,
  silicon identity (ASSUMED-flagged), `k_air`, emissivity, `T_ambient`;
  re-runs Block C's exact 8-point grid (Host D, 4 ratios × {5τ, 0.5τ} gaps)
  through `coupled_segment_general` — imported via `importlib.util` from
  `experiments/045-.../run.py` under a private module name (exp-050's own
  precedent, avoiding a basename collision) — at the MIXED chain's own
  `dt_ss_full`/`tau_thermal_s`, not the `w_on`-consistent one Block C
  originally used; both the decoupled proxy and the exact coupled-ODE
  trajectory are computed and compared (`exact <= decoupled` checked
  directly, not assumed).

## Predictions (frozen here, committed to git BEFORE any Phase-4 run — house discipline, non-negotiable)

See `NOTES.md` for the full pre-registered prediction table (P-054-1
through P-054-8) and idealizations, superseding `phase1_proposal.md`'s
own P-054-1/2/3/4/5/6/7 — the Phase-1 file is retained unedited as the
historical record of what Phase 1 proposed and Phase 2 critiqued, per this
program's own T10/exp-045 precedent (correcting BEFORE any run is a Phase-3
synthesis edit, not a post-hoc erratum).
