# PHASE 5 — THERMODYNAMICS REVIEW · Panel Iteration 85 (exp-108)

Fresh context. Read in full: `PANEL.md`, `LOGBOOK.md` (RULED OUT R1–R25 and
LIVE THREADS T1–T28 in full, plus the Iteration 80–84 narrative entries),
`PLAN.md`'s Vision/Current-state, and this cycle's complete record —
`phase1_proposal.md`, `phase2_critique_{materials,em,thermodynamics,
quantum,vision}.md`, `phase2_redteam_audit.md`, `NOTES.md`, `results.json`,
`run_output.txt`, `run.py`, `chunk_runner.py`, `analyze.py`,
`reclassify_106.py`, the patch to `experiments/106-.../run.py`, and
`lab/validation/run_all.py`'s new `stage26_chunked_run_identity()`. I own
this cycle's Phase-2 critique (`phase2_critique_thermodynamics.md`) —
re-checked closely, below, not merely re-read.

## Verdict: **CONFIRM**

The one number this cycle owes my charter — my own Phase-2 finding that the
real absorbed-watts divergence between the fixedabs/selfsim families is
30.9%/46.3% at r=156/312, both UNDETECTABLE at minimum margin ≥117× — is
correctly, accurately, and completely carried into the frozen NOTES.md
record. I independently re-derived both percentages and the margin from
exp-107's own `item3_rows` primitives, from scratch, not from any
restatement, and they reproduce exactly. The `closure` field is correctly
scored as outside my charter. "No thermal sidecar invoked fresh this cycle"
is literally true (verified by grep, not merely accepted), and nothing in
the angular-pattern/noise-floor work implicitly touches absorbed-power
*magnitude* in a way that would call for a fresh sidecar reading — it
touches *scattered* power's angular shape, a different physical quantity
my charter does not own. One minor, non-blocking process observation is
noted in §5.

## 1. Independent re-derivation of 30.9% / 46.3% / ≥117× from `item3_rows`

Read directly from `experiments/107-t28-delta-scene-r5-census-decision/
results.json`'s own `item3_rows` field (not from NOTES.md's or my own
Phase-2 critique's restatement):

| cell | `sigma_ext` | `abs_ext_ratio` | `p_abs_w` | `dt_ss_K` | `margin` |
|---|---|---|---|---|---|
| `selfsim_156` | 480.6881014804668 | 0.5180430284747772 | 7.093307648790325e-12 | 5.824085844284275e-05 | 343.40 |
| `fixedabs_156` | 560.198850825502 | 0.4992167630142016 | 9.283886142008288e-12 | 7.622699104110958e-05 | 262.37 |
| `selfsim_312` | 960.4456295185845 | 0.5190124481393582 | 2.8371321293456664e-11 | 0.0001163662613549568 | 171.87 |
| `fixedabs_312` | 1191.3258584254531 | 0.4935860562303906 | 4.1512628975031126e-11 | 0.00017026593096860568 | **117.46** |

**r=156 divergence** (matching `p_abs_frac_diff`'s own denominator
convention, `|fixedabs−selfsim|/selfsim`, confirmed against exp-106's own
`run.py:625-626`):

```
|9.283886142008288e-12 - 7.093307648790325e-12| / 7.093307648790325e-12
= 2.190578493217963e-12 / 7.093307648790325e-12
= 0.308895... → 30.9%
```

**r=312 divergence**:

```
|4.1512628975031126e-11 - 2.8371321293456664e-11| / 2.8371321293456664e-11
= 1.3141307681574462e-11 / 2.8371321293456664e-11
= 0.463196... → 46.3%
```

Both match NOTES.md's Idealizations sentence exactly. **Minimum margin
across all four cells is 117.46× (`fixedabs_312`)** — matches "≥117×"
exactly, and matches LOGBOOK's own Iteration-84 entry's independently
cited "117.5× margin" for the identical cell (rounds the same way).

**Independent sanity check on the quadratic-scaling claim** (NOTES.md/my
own critique: `p_abs_w` scales as `σ_ext²·ratio`, not `σ_ext·ratio` the
way `sigma_abs`/`p_abs_frac_diff` does — confirmed from `p_abs_w`'s own
defining formula, `experiments/107-.../run.py:274`,
`p_abs_w = i_incident * (sigma_ext*DX_M)**2 * 1e4 * abs_ext_ratio`):

```
r=156: (560.199/480.688)^2 × (0.49922/0.51804) = 1.3577 × 0.9637 = 1.3086 → +30.9%
r=312: (1191.326/960.446)^2 × (0.49359/0.51901) = 1.5385 × 0.9510 = 1.4632 → +46.3%
```

Both reproduce the divergence via an entirely independent method (squaring
the `sigma_ext` ratio and multiplying by the `abs_ext_ratio` ratio,
computed straight from the raw cell values, not from the pre-divided
`p_abs_w` numbers) — the "quadratic-in-`σ_ext`" mechanism claim is not
merely asserted, it is arithmetically demonstrated, twice over, by me.

**Confirmed independently a third time on the record**: Red Team's own
Phase-2 audit (`phase2_redteam_audit.md` §0.4) performed the identical
`item3_rows`-primitives recomputation and reported the same two
percentages and the same 117.46× minimum, ruling my Phase-2 critique
"arithmetically airtight." Three independent derivations (mine at Phase 2,
Red Team's at Phase 2, mine again here at Phase 5, by a different method)
now agree bit-for-bit. `margin` itself cross-checks cleanly against a
0.020 K NETD floor (`0.02/0.00017026593096860568 = 117.46`, exact), the
same NETD figure this program has used since exp-043/T5.

## 2. Does NOTES.md's Idealizations section state this correctly?

Yes, on every count I can check:

- **Correctly sourced**: "per exp-107's own `item3_rows`" — verified, not
  a paraphrase; the field name and file are exact.
- **Correctly directional**: "larger than the 12.31%/17.96% `sigma_abs`-only
  figure" — true (30.9 > 12.31; 46.3 > 17.96), and correctly attributed to
  quadratic-vs-linear scaling in `σ_ext`, verified in §1 above.
- **Correctly scoped**: "N/A holds" for constraint 1/thermal detectability,
  and the sentence is placed to prevent a specific, real confusion —
  Tier-0 item 1's reclassification trigger (`p_abs_frac_diff`, a
  `sigma_abs`-fractional quantity) is NOT the same number as the real
  absorbed-watts gap, and NOTES.md says so explicitly rather than letting
  a future citation conflate the two. This is exactly the kind of
  R9-class (commensurability) discipline this program's own registry
  exists to enforce, applied here correctly and pre-emptively rather than
  needing a later correction cycle.
- **Correctly framed as a checked gap, not a missed one**: my own Phase-2
  critique named this an R8-shaped gap ("the proposal reached N/A by never
  looking, not by checking") — the Synthesis and Idealizations sections
  both preserve that framing rather than silently absorbing the number as
  if it always belonged there. Good historiography.

I found no error, omission, rounding abuse, or unit-mismatch anywhere in
how this finding survived Phase 2 → Synthesis → Idealizations.

## 3. The `closure` field: correctly outside my charter

`closure` (Result table: hollow 0.0196%/0.0563%, PEC-cored 0.0160%/0.0581%
at r=156/312) is defined in `analyze.py::closure_for()` as
`|radial_absorbed_power_total − box_ledger_sigma_abs·i_inc| /
|box_ledger_sigma_abs·i_inc|` — the relative disagreement between two
independent *measurements of the same already-computed absorbed power*
(a volumetric radial integral vs. a closed-surface flux-boundary
integral), both taken on this cycle's own fresh captures. This is a
Poynting-flux self-consistency identity — an EM-charter bookkeeping check
on whether the engine conserves energy correctly between two measurement
conventions — not a statement about how much power is absorbed, where it
goes thermally, or whether re-radiation would be detectable. It carries
**no thermal-detectability implication**:

- It does not report a new absorbed-power magnitude — both operands
  it compares are already-established quantities (`radial_absorbed_power`
  from exp-028/T9; box-ledger `sigma_abs` from `sections.widths()`), and
  the closure value is their *relative disagreement*, not either value
  itself.
- Even read maximally favorably as "does this validate the sidecar's own
  input," the answer is a reassuring but numerically inert yes: the two
  methods agree to ≤0.058% at every cell — five to six orders of magnitude
  tighter than the 30.9%/46.3% divergence and the 117–343× margins that
  actually govern the UNDETECTABLE classification (§1). A 0.06%-level
  cross-validation of the absorbed-power *input* cannot move a
  classification protected by a two-orders-of-magnitude margin.
- Consistent with exp-106's own established 0.02–0.06% precedent range
  (cited correctly in NOTES.md against PLAN.md's Current-state text) —
  this is not a new physical finding, it is EM's own mandatory fix 5
  (restoring a narration gap flagged since exp-106/Iteration-84 Phase 5)
  being discharged, correctly credited to EM in the Synthesis section, not
  claimed for my own charter.

**My own assessment: NOTES.md's scoping is right.** `closure` belongs to
ELECTROMAGNETISM (energy-conservation bookkeeping between two field
integrals), not to THERMODYNAMICS (what absorbed energy does once it is
correctly accounted for). I have no revision to propose.

## 4. Is "no thermal sidecar invoked fresh this cycle" actually correct?

**Yes, verified by grep, not merely accepted from NOTES.md's own claim**:

```
$ grep -n "thermo_sidecar\|netd\|dt_ss\|p_abs_w\|mixed_length_scale" \
    run.py chunk_runner.py analyze.py reclassify_106.py
(zero hits, all four files)
```

None of this cycle's four executable files call `lab/thermo_sidecar.py`,
compute `p_abs_w`, `dt_ss_K`, or `netd_disposition`, or reference NETD in
any form. The 30.9%/46.3%/≥117× check discussed above lives entirely in
prose (my own Phase-2 critique, the Synthesis section, and the
Idealizations sentence) and reuses exp-107's already-persisted
`item3_rows` values verbatim — it is, correctly, a **post-run analytic
calculation performed on already-committed sidecar output**, not a new
FDTD-adjacent sidecar invocation. This matches my charter's own
expressibility contract exactly ("the sidecar is a post-run analytic
calculation, not an FDTD output, and is labeled as such") — NOTES.md's
claim is accurate.

**Does the angular-pattern/noise-floor work implicitly touch absorbed-power
distribution in a way worth a sidecar reading?** I considered this
carefully and conclude **no, for a specific physical reason, not by
default**:

- **Item i (`angular_scattered_pattern`)** measures the *scattered* power
  σ_scat's angular distribution — light re-directed away from the object,
  never absorbed, never heats anything. It is orthogonal by construction
  to the absorbed-power channel my charter owns; a CONFIRM on the angular
  scattering null says nothing about where absorbed energy goes.
- **Item ii** (box-ledger noise floor) and **item iii** (numerator
  floor-gate) both characterize *measurement precision* on already-
  aggregate quantities (`abs_ext_ratio`, `frac_unresolved`) — they refine
  how well the existing bulk absorbed-power ratio is known, they do not
  introduce a new spatial/angular absorbed-power distribution that the
  sidecar's own lumped-capacitance model (validated by the low Biot
  number this program established at T22/T23, Iteration 21–23) would need
  to be re-checked against. The sidecar treats the object as a single
  thermal mass with one steady-state ΔT; nothing in items i–iii disturbs
  that idealization's own validity condition (Biot number, unchanged by
  either instrument).
- If a future cycle ever measured a genuinely *localized* absorption
  hot-spot (e.g. via `radial_absorbed_power`'s own radial binning showing
  a sharply peaked, not smoothly graded, profile), that would be the
  correct trigger for a fresh sidecar reading — this cycle's own radial
  profile is unchanged from exp-106/107 (same `graded_black_shell`
  construction; item i tests the *scattered*, not absorbed, angular
  shape), so no such trigger exists here.

**Conclusion: the claim is correct on both halves** — literally true by
code inspection, and correct in substance (nothing in this cycle's new
physics has a thermal-detectability reading that the existing 30.9%/46.3%/
≥117× check does not already cover).

## 5. Minor, non-blocking process observation

The 30.9%/46.3%/≥117× arithmetic (§1) exists only in prose across three
documents (my own Phase-2 critique, Red Team's Phase-2 audit, NOTES.md's
Synthesis/Idealizations) — it was never wired into `analyze.py` or
`reclassify_106.py` as a checked assertion the way this cycle's other
zero-FDTD post-processing figures are (e.g. `closure`, item i/ii/iii).
Given the R4 lineage's own standard ("a falsifier or self-consistency
figure... must be produced by invoking the actual committed function...
never hand-typed"), a stricter reading would want a one-line script
computing this ratio from `item3_rows` and asserting it, the same idiom
`reclassify_106.py`/`analyze.py` already use elsewhere in this cycle. I do
**not** treat this as a load-bearing gap and do not downgrade my verdict
for it: unlike the historical R4 instances that motivated that rule, this
figure has now been independently re-derived from primitives three
separate times (my own Phase-2 critique, Red Team's Phase-2 audit, and
this review), by two different arithmetic routes (direct percentage and
the independent quadratic-scaling cross-check, §1), all in exact
agreement — the actual risk R4 exists to catch (a hand-typed figure that
silently doesn't reproduce) has already been ruled out by cumulative
independent verification, not merely asserted. Worth a one-line code
assert if a future cycle touches this file again; not worth reopening this
one.

## 6. Zero-FDTD reproduction (primitives-level, this review)

All three requested independent checks were re-run from source and match
NOTES.md's own Result section exactly:

- `python3 experiments/108-.../reclassify_106.py` → NEW classification
  contains `"THREE-WAY-AMBIGUOUS"`; all other fields
  (`shape_ratio_fixedabs=18.228333623646076`, `noise_dominated=False`,
  `trusted=False`) bit-identical to exp-106's committed `results.json`, as
  predicted.
- `python3 experiments/108-.../analyze.py` → item_i CONFIRM (both r),
  item_ii CONFIRM (`residual_std`=2.8972e-06/2.1022e-06 vs
  `|Δ_boxA|`=2.9690e-05/2.4680e-05), item_iii PASS
  (`frac_unresolved`=0.1827/0.2525), `closure`=0.000196/0.000160 (r=156,
  hollow/PEC-cored), 0.000563/0.000581 (r=312) — matches Result table
  exactly.
- `python3 lab/validation/run_all.py --only 26` → 2/2 PASS (positive
  control `max|diff|=0.000e+00`; negative control relative deviation
  2.000, correctly `>0.01`).

## 7. What would have flipped this verdict

Any of the following, none of which occurred: the recomputed 30.9%/46.3%
or 117.46× figures failing to reproduce from `item3_rows`; the
Idealizations sentence mis-stating the direction, magnitude, or scope of
the finding; `closure` carrying any absorbed-power-magnitude information
beyond a sub-0.06% bookkeeping identity; a genuine grep hit for
`thermo_sidecar`/`p_abs_w`/`netd` inside this cycle's own executable
files contradicting the "no fresh sidecar" claim; or a plausible physical
argument that the angular-scattering/noise-floor work bears on absorbed-
power *spatial distribution* in a way the lumped-capacitance sidecar model
does not already account for. None of these held up.
