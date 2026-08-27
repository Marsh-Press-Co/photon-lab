# PHASE 3 — SYNTHESIS · Panel Iteration 56 · exp-079

*Director's synthesis. Not a fresh sub-agent seat — per PANEL.md the Director
synthesizes but does not vote in Phase 2, and states which criticisms it
accepts and which it overrides, and why. Adopting `phase2_redteam_audit.md`
in full: PROCEED-WITH-MANDATORY-FIXES, 9-item docket, **nothing overridden**.*

---

## 1. What is accepted, in full

All 9 mandatory-fix docket items from `phase2_redteam_audit.md` §9 are
adopted without modification. In particular, item 1/2 — the central
finding, given full weight by Red Team's own §2 and independently confirmed
there a third way (after EM's analytic derivation and QUANTUM's empirical
ablation) — is accepted as the cycle's own correct headline, replacing
`phase1_proposal.md`'s original §4/§7 framing:

**This construction (a coherent aperture sum whose only `theta_beam`-
dependent ingredient is the shared driven-phase ramp, with both the
per-point bounce angle `theta_local(y_s)` and the propagation distance
`dist_image(y_s)` fixed, `theta_beam`-independent quantities) is
structurally incapable of discriminating a real y-wall echo — at ANY
period, including T28's own — from no echo at all.** The recovered
`~2.02°` oscillation is the aperture's own T21-family window content, not
evidence for or against a real y-wall reflectance effect. This is narrower
and more useful than either of exp-078's own two named branches: the flat
result does not survive (branch (a) is refuted), but the recovered
`theta_beam`-dependence does not, and structurally cannot, discriminate a
real T28-matching echo from none (so branch (b)'s own implicit
"non-flatness would justify the full build" is also not licensed).

## 2. Nothing overridden — why

No Phase-2 finding conflicts with another; Red Team's own audit
independently re-verified every load-bearing claim from primitives (its own
§0) before adopting any of them, catching and correcting its own first-pass
tooling error (§0.3, the residual-decomposition basis) before crediting
PHOTONICS' finding — the exact self-check discipline this program holds
every seat to. There is nothing here to weigh against a competing claim;
the Director's own role this cycle is to execute the docket faithfully, not
adjudicate a live disagreement.

## 3. Execution (this document + the same-shift commits below)

1. **[Docket 1]** Added Idealization 9 to `phase1_proposal.md` §6, stating
   the structural finding explicitly.
2. **[Docket 2]** Rewrote `phase1_proposal.md` §4's "a priori prediction"
   framing and §7's self-scored verdict to state the structural finding as
   the headline, replacing the "closer to a genuine (informal) REFUTE"
   language and the "third, sharper outcome" framing (VISION's/Red Team's
   Attack 5 correction: this is branch (b), refined, not a third branch).
3. **[Docket 3]** Folded QUANTUM's `r(theta_local(y_s))≡1` reflectance-
   ablation control into `y_wall_aperture_sum.py` as committed, reusable
   code (new §[7]/§[7b]), producing `reflectance_ablation_control` and
   `t21_forced_fit_c80_c40` in the results JSON. Re-run, confirmed: ablated
   `PAIR_PAD`/`C80−C40` periods reproduce the r-weighted model to
   `|dP*|≤0.023°` (statistically indistinguishable, matching all three
   independent Phase-2 reproductions — EM, QUANTUM, Red Team — within
   grid-resolution noise); `PAIR_ABSORB40`'s ablated delta is EXACTLY zero
   (`ptp=0.0`, not merely small — G40/C80 share identical `(obj_y,y_lo,y_hi)`
   under PAD=40, so ablating `r()` to a config-independent constant makes
   their aperture sums bit-identical), disclosed as a SHARPER, two-part
   confirmation (geometry alone for `PAIR_PAD`/`C80−C40`; genuine but
   still-T21-frequency-locked ABSORB-dependence for `PAIR_ABSORB40`) rather
   than folded uniformly into one "indistinguishable" claim, which would
   have overstated what the `PAIR_ABSORB40` case actually shows. The
   `C80−C40` T21-forced-fit sub-check reproduces Red Team's own cited
   numbers exactly (`R²=0.9425`, `rel_dev=0.3101`, INCONCLUSIVE, vs the
   free-fit's marginal `rel_dev=0.2857` SUPPORT).
4. **[Docket 4]** Fixed "nine orders of magnitude" in `phase1_proposal.md`
   §1/§5.2/§7 to the correct `≈20.2` orders for the comparison actually
   cited (`ss_tot` ratio vs. exp-078's own ratio), and added the separate,
   correctly-labeled `≈9.78`-order comparison (this cycle's own absolute
   `ss_tot` vs. `SS_TOT_DEGENERATE_FLOOR`) as a distinct, explicitly-named
   figure — resolving the ambiguity Red Team's audit found rather than
   picking one silently.
5. **[Docket 5]** Added Idealization 10, disclosing the missing
   `1/√dist_image(y_s)` cylindrical-wave amplitude-falloff term (this
   bench's own established `field_and_h` convention, exp-048/exp-042) and
   EM's quantified, non-load-bearing `≈753×` effect on the `ss_tot` ratio
   (Test-A period verdicts shift `<1%`).
6. **[Docket 6]** Added a §5.3 companion note disclosing PHOTONICS'
   residual-sideband finding (`2.55°`, R²=`0.60`, `≈2.8%` of primary
   `ss_tot`) and Red Team's own ruling that it is mechanistically subsumed
   by the structural finding (a side-lobe of the same shared-aperture
   Fourier content), not independent evidence.
7. **[Docket 7]** Added the THERMO N/A-disposition sentence (second
   consecutive cycle with this omission after being named once already at
   exp-078 — closed here).
8. **[Docket 8]** Added a forward-caution note in §7/Idealizations: the
   effective aperture `A_eff≈518.81` a fix would need is bit-identical to
   LOGBOOK's own R5-addendum-ruled-out dead end (Iteration 47, exp-070) —
   any future attempt to shrink this model class's effective aperture
   toward T28's own period would be re-approaching that already-closed dead
   end, not new evidence.
9. **[Docket 9]** Not a fix to this cycle's files — a recommendation for
   Iteration 57's own ranking (Red Team's own §8 finding: the deferred
   far-wall/far-edge pair would inherit Attack 1's own structural limitation
   unchanged; a plane-wave/global-steering construction, not a per-point-
   image refinement, is the genuinely different instrument needed). Carried
   forward into this cycle's own Phase-5 synthesis and the Iteration-57
   ranking, not applied to `experiments/079-.../` directly.

## 4. What is NOT a "prediction to freeze before a run," and why

Unlike exp-078's own Phase 3 (where the angle-convention fix changed the
actual computed physics and required FROZEN PREDICTIONS committed before a
corrected re-run), none of this cycle's 9 items change any of the model's
own already-computed, already-independently-reproduced Test-A numbers
(`rel_dev`, R², `ss_tot` ratios, the convergence check, the gates) — Red
Team's own §9 states this explicitly ("None of these nine items touch
`y_wall_aperture_sum.py`'s own frozen Test-A numbers"). Item 3's own new
code (the ablation control) is a genuinely new computation, but its outcome
was already independently reproduced three times over during Phase 2 (EM
analytically, QUANTUM empirically, Red Team's own from-scratch re-run) —
folding it into the committed script is a confirmatory re-run of an
already-known result, not a fresh, unknown prediction requiring a pre-run
git freeze. The expected outcome, stated here before the extended script
was re-run for the official record: ablated `PAIR_PAD`/`C80−C40` periods
within a few hundredths of a degree of the r-weighted model's own periods;
`PAIR_ABSORB40`'s ablated delta expected to be small-to-exactly-zero given
G40/C80's shared geometry. **Confirmed exactly** — see `phase4_results.md`.

## 5. Phase-4 gate

House gates apply: zero new `lab/` diff (confirmed — this entire cycle is
desk analysis reusing already-validated engine machinery); the already-
established Test-A band (`rel_dev≤0.30`/`>1.00`); the `SS_TOT_DEGENERATE`
guard (exp-078's own hardening, reused); the new gates at the full aperture
`theta_local` envelope (`[4.77°,15.50°]`, re-run and re-confirmed clean at
§0 of `_output.txt`, unaffected by this Phase-3 docket). Evidence Gate:
every number in the corrected `phase1_proposal.md` traces to
`y_wall_aperture_sum_results.json`/`_output.txt`, re-run after the docket's
own code change, R4-clean.
