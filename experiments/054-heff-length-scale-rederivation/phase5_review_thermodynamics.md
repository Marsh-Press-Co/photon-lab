# exp-054 Phase 5 Review — THERMODYNAMICS (blind, fresh-context, cold read)

Panel Iteration 31. Reviewing the FINISHED cycle: `phase1_proposal.md`,
all five Phase-2 critiques, `phase2_redteam_audit.md`, `phase3_synthesis.md`,
`NOTES.md`, `run.py`, `results.json`, `lab/thermo_sidecar.py` in full,
`lab/validation/run_all.py`'s `stage18_length_scale_chain`, and the
SUPERSEDED addenda in `experiments/043-.../NOTES.md` and
`experiments/045-.../NOTES.md`. This is my own charter's own module,
extended this cycle — read as if grading someone else's homework.

## What this cycle actually establishes

The physical argument is sound and, on this read, correctly implemented:
`P_abs` (a calibrated optical measurement, legitimately larger than
geometric shadow via the extinction paradox) stays on `w_on`; `h_eff`,
thermal mass, and radiating/convecting area — all properties of the real
conducting solid — move to `r_out`. `dp_dt = area·(4εσT³ + h_eff)` is not a
flux, so combining a `w_on`-based watt figure with an `r_out`-based
admittance needs no shared-area cancellation step; EM's Phase-2 steel-man is
right about this, and I independently re-derived `dt_ss_full`
(`h_eff=k_air/r_out=11111.11 W/(m²K)`, `dp_dt=6.0868e-8 W/K`,
`P_abs/dp_dt=3.293076e-5 K`) from `results.json`'s own numbers and it
checks out to the last digit against `part_a.regime.dt_ss_full_K`.

Every one of this cycle's own pre-registered predictions passed
(`p_054_1_pass` … `p_054_4_pass`, and `p_054_5_both_undetectable`, all
`true` in `results.json`). All seven of Red Team's Phase-2 mandatory fixes
were implemented, not just promised:
- ASSUMED–T18 provenance label and 100%-fill disclosure: present verbatim in
  `lab/thermo_sidecar.py:267-273`, `run.py`'s `MATERIAL_PROVENANCE_NOTE`,
  and `results.json`'s `material_provenance`/`mass_fill_fraction_assumption`
  keys.
- Block C is a genuine `coupled_segment_general` re-run at the mixed
  chain's own `dt_ss_full`/`tau_thermal_s` (`run.py:150-171`), not an
  algebraic rescale — `exact_vs_decoupled_ratio_periodic` is computed per
  point and the worst value (0.9987) is exactly what `p_054_3a` claims.
- P-054-6 is correctly rescoped: `results.json`'s
  `p_054_6_scope_statement` explicitly states the T8/T13/T14 witness-scale
  question "REMAINS OPEN AND UNADDRESSED by exp-054," not refuted.
- The NETD disclaimer is genuinely propagated at every locus a
  detectability classification is quoted, checked directly in
  `results.json`: `part_a.regime.netd_disclaimer`,
  `part_a.netd_disposition.disclaimer`, `part_a.netd_disclaimer`,
  every `block_c_points.*.netd_first/netd_periodic.disclaimer`,
  `part_b.netd_disclaimer`, and the top-level
  `netd_disclaimer_ALL_CLAIMS`. I did not find a bare classification
  anywhere in the file without an adjacent disclaimer.

**Net result for my own instrument (the energy sidecar): two headline
articles now have thermal-detectability margins substantially LARGER
(safer) than previously reported** — the ON-endpoint at ≈607× (vs. the
informal, never-run ~2.6× guess) and the dose-accumulation article at
≈8,955× exact / ≈8,943× decoupled (vs. ~38–42×). Both stay UNDETECTABLE by
wide margins, confirming Iteration 20's own finding that the original
`h_conv=5.0 W/(m²K)` macroscopic placeholder — not the `r_out`-vs-`w_on`
choice — was the dominant historical understatement.

## Load-bearing defects found

**1. `mixed_length_scale_regime` bakes a silicon-specific, exp-054-specific
provenance narrative into every call, unconditionally, in code presented as
general-purpose.** `lab/thermo_sidecar.py:267-273`:

```python
"material_provenance": "ASSUMED -- provenance terminates unsourced "
                        "(T18); see REALIZABILITY_MEMO.md and "
                        "exp-054/NOTES.md idealizations",
"mass_fill_fraction_assumption": (
    "mass_kg assumes 100%-fill crystalline solid at l_geometric_m "
    "-- undisclosed in the Iteration-31 Phase-1 draft, disclosed "
    "here per Red Team mandatory fix 3"),
```

The function signature takes bare `density_kg_m3`/`c_p_j_kgk` floats — it
has no material-identity or provenance-status parameter. The module's own
docstring (lines 1-8) frames this function as *"reusable, trust-suite-gated
code"* replacing exp-045's one-off script. But the returned dict's
provenance string is not conditioned on what was actually passed in: a
future caller supplying a properly DOI-sourced material would still get
back `"ASSUMED — provenance terminates unsourced (T18)"`, and the citation
trail ("see... exp-054/NOTES.md idealizations") would be wrong for any
call site that isn't this cycle's own two articles. This is exactly the
failure mode Red Team's own mandatory-fix-3 language was trying to
prevent (silent provenance drift) — it has been fixed correctly for THIS
cycle's call sites and simultaneously re-introduced as a latent bug for
the very next one, because the fix was hardcoded into the general
function's return value instead of threaded through as a caller-supplied
argument. Not caught anywhere in Phase 2 or Red Team's audit (their
mandatory fix 3 only asked for the label to be *present*, not for it to be
correctly parameterized).

**2. `experiments/045-.../NOTES.md`'s SUPERSEDED note (line ~501)
misquotes its own cited figure.** It reads *"max `dT_periodic` (exact)
≈2.235×10⁻⁶ K"*. `results.json::part_b_block_c_rerun.max_dT_periodic_exact_K`
is `2.233484136554998e-06` — i.e. `≈2.233×10⁻⁶ K`, not `2.235×10⁻⁶ K` (a
~0.07% transcription slip in the fourth significant figure). Small and
non-load-bearing for the margin/classification claims (the margin figures
quoted in the same note, ≈8,955×/≈8,943×, DO match `results.json` exactly:
`netd_lo_margin_exact`=8954.619…, `netd_lo_margin_decoupled`=8943.123…),
but the task's own instruction was to verify these forward-pointers
against `results.json`'s actual numbers, not just plausible-sounding prose
— and this one number is not exact. Worth a one-line correction next time
this file is touched (T10 "flag, don't rewrite" convention applies to me
too — flagging here, not editing NOTES.md, per this deliverable's own
scope).

**3. Trust-suite stage 18's gate 4 (Red Team mandatory fix 4) is
implemented exactly as specified, and Red Team's own attack 4 already
named its residual scope limit correctly — that limit is no longer
hypothetical.** `lab/validation/run_all.py:1576-1611`: gates 1/2 remain
tautologically true for any `L` (confirmed — `gas_conduction_h_eff` and
`lumped_cube_mass_kg` satisfy their own identities by construction
regardless of which length is passed). Gate 3 is genuinely discriminating,
but only at the one call site it pins (the ON-endpoint's literal
`r_out_cells·dx_m`). Red Team's attack 4 explicitly flagged this as a
residual gap using a HYPOTHETICAL example: *"A future caller who
accidentally passes `w_on` into the `h_eff`/mass helper at some other
article (`graded_black_shell`, a future host) would trip neither of the
first two gates."* That hypothetical is not hypothetical — see finding 4
below: it already describes `graded_black_shell`'s own committed
`results.json` entry, unchanged by this cycle, and stage 18 does not
gate it.

**4. The program's actual flagship absorber, `graded_black_shell`, still
carries the exact historical bug this whole cycle exists to fix — and its
margin is the thinnest in the entire thermal-detectability record.**
`experiments/043-docket7-thermo-sidecar/results.json::graded_black_shell_flagship`:
`area_convention: "iso_xsec_sq"` with `sigma_ext_cells=240.007` (i.e. `w_on`,
not `r_out`) driving area for BOTH `P_abs` and the mass/h_eff chain, and
`H_CONV=5.0` (the original macroscopic placeholder, per
`experiments/043-.../run.py:184`) — never replaced with
`gas_conduction_h_eff`. Its `steady_state_dT_K_central` = 0.0033108 K gives
an NETD-lo margin of only **0.020/0.0033108 ≈ 6.04×** — thinner than
anything this cycle touched by two to three orders of magnitude, and close
enough to the `[0.020, 0.050]` K band that P-054-5's own inductive basis
("no candidate chain… has ever produced a margin below 5×") is describing
a floor this exact article sits only ~20% above. I grepped every
`results.json` under `experiments/*/` for `graded_black_shell` combined
with a thermal/NETD figure and found only this one, uncorrected entry —
exp-046 ("aperture-beam-t23-mixed-regime-dose-extension") applied the
informal T23 mixed regime to exp-045's own dose-accumulation grid, never
to `graded_black_shell`. exp-054 does not mention `graded_black_shell`
anywhere in its own files. This is not a hypothetical follow-up; it is the
program's own flagship candidate article sitting on the acknowledged-wrong
chain, at the record's thinnest margin, un-flagged by any SUPERSEDED
notice.

## On the energy bookkeeping itself (does the mixed chain still feel
physically uncomfortable?)

No, not on reflection, and I looked for exactly this. The apparent
oddity — absorbed watts computed over a diffraction-inflated optical
footprint (`w_on`, ~3.03× `r_out`) being dumped into a smaller solid's
conduction/radiation budget — is standard Mie-regime physics, not a
bookkeeping error: at this bench's size parameter (`x≈20-33` across the
3λ sweep, per PHOTONICS' Phase-2 critique), `σ_ext` legitimately exceeds
geometric cross-section (the extinction paradox, `Q_ext→2`), and the power
it removes from the incident beam is still deposited in the real,
smaller solid — `ratio_abs_ext` picks out exactly the absorbed share of
that removed power. `dp_dt`'s two loss terms (radiative, convective) are
both anchored on the SAME `l_geometric_m` (`area_m2 = l_geometric_m**2`
feeds both `4εσT³` and `h_eff` identically), so there is no term inside the
loss side of the ledger using two different lengths — only the
gain/absorption side and the loss side differ, which is the whole point
of the correction, not a residual defect. The one idealization that
remains genuinely unexamined by this cycle (and it says so itself,
idealizations bullet 2) is that `mass_kg=ρ·l³` is a compact-cube read of
what is, in the underlying 2D FDTD bench, more naturally an
infinite-invariant-axis geometry — the same "compact vs. rod" ambiguity
`absorbed_power_established_ratio`'s own docstring already flags for
`P_abs`. exp-046's true-disk sensitivity recheck (97×, still far above the
5× floor) is the right mitigation and is correctly cited as not re-run
here — I don't think this needs re-litigating this cycle.

## Does this close out the standing thermal-detectability thread?

**No.** Two things remain genuinely open, one of which this cycle's own
text already discloses correctly and one of which it does not surface at
all:

- **T8/T13/T14 (near-field→witness-scale bridge)** — correctly and
  explicitly left open by P-054-6/`p_054_6_scope_statement`. Not a gap in
  this cycle's honesty, just a gap in the program's overall coverage.
- **`graded_black_shell`** — not mentioned anywhere in this cycle's own
  record, and its committed thermal figure is the one place in the whole
  repository where the exact bug this cycle formally closed is still live
  and unflagged. Given the ~3× (P_abs-preserving) to potentially much
  larger swing the mixed-chain correction produced at the other two
  articles once `H_CONV` also moves off its 5.0 placeholder, I'd expect
  `graded_black_shell`'s margin to clear the detectability floor
  comfortably once corrected — but that is an expectation, not a result,
  and this program's own house discipline (verify-before-claim) says that
  expectation should not be treated as settled until run.

`off_pass` (exp-032) carries no thermal/NETD figure anywhere in its
`results.json` — it is a pure optical-depth-ratio study, not part of the
thermal-detectability thread at all, so there is nothing to re-derive
there.

## Ranked candidate next directions (Iteration 32+)

1. **Re-run `graded_black_shell` through `mixed_length_scale_regime`,
   replacing `H_CONV=5.0` and the all-`w_on` chain in
   `experiments/043-.../results.json::graded_black_shell_flagship`.** This
   is the program's actual flagship article, currently at the record's
   thinnest margin (~6×) under a chain this program has now formally
   repudiated. Cheapest, most load-bearing follow-up available — same
   zero-new-FDTD desk-analytic pattern as this cycle, one afternoon of
   work, closes the exact gap Red Team's own attack 4 named as a
   hypothetical.
2. **Parameterize `mixed_length_scale_regime`'s provenance/fill-fraction
   strings** (defect 1 above) so a future caller with a genuinely sourced
   material doesn't inherit exp-054's specific ASSUMED–T18 silicon
   citation. Small code change, prevents a documentation-integrity bug
   from propagating into the very next reuse this module was built for.
3. **PHOTONICS' desk Q_ext(x) cylinder closed-form check** (Red Team's own
   non-mandatory recommendation, deferred here) — bounds how much of
   `w_on`'s ~3.03× excess over `r_out` is genuine diffraction vs. the
   `iso_xsec_sq` shape convention. Doesn't change this cycle's
   classification, but firms up the interpretive claim ("`w_on` is
   diffraction-inflated, not just conventionally larger") the whole mixed
   chain leans on rhetorically.
4. **A one-line correction to `experiments/045-.../NOTES.md`'s SUPERSEDED
   note** (defect 2): `2.235×10⁻⁶` → `2.233×10⁻⁶ K`, or restate to more
   decimal places to avoid the ambiguity. Trivial, but this program's own
   convention is that forward-pointers get checked against `results.json`,
   not approximated.
5. **T8/T13/T14 witness-scale `h_eff` bridge itself** — still the largest
   standing gap in the thermal-detectability thread, correctly disclosed
   as out of scope again this cycle rather than attempted. Ranked last
   here only because it's a bigger build than the above four, not because
   it's less important; LOGBOOK.md should keep it live.

## Verdict: **PARTIAL**

As a piece of instrument/methodology work, this cycle is sound: the
physical argument for splitting `P_abs` (optical, `w_on`) from
`h_eff`/mass/area (geometric, `r_out`) holds up under my own
re-derivation, every mandatory Phase-2 fix was actually implemented (not
just promised in prose), all eight pre-registered predictions passed, and
the module's expressibility contract (post-run analytic, clearly labeled,
zero new FDTD calls) is honored throughout. On those narrow terms it would
earn PROMISING.

It is PARTIAL, not PROMISING, against the broader thread it was framed as
addressing (T1 escape route "NONE," but still explicitly Iteration-25's
queued "close the standing tripwire" work): the correction was applied to
two of at least three articles that share the bug it fixes, and the one
left untouched — `graded_black_shell`, the program's own flagship — is
the one sitting closest to the detectability floor. The thermal-safety
picture this cycle paints ("safer by 2-3 orders of magnitude than
previously feared") is not yet known to hold for the article that would
actually matter most if this program ever reaches a Checkpoint-1
candidate-reproduction moment. Not RULED OUT — nothing here contradicts
the mixed-chain argument or threatens its two completed results — but the
standing thread stays open until `graded_black_shell` gets the same
treatment.
