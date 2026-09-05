# Phase 2 Critique — QUANTUM OPTICS (exp-113, Panel Iteration 90)

*Fresh sub-agent, blind context. I have not seen and did not seek out any
other seat's Phase-2 output this cycle. Charter: non-classical absorption,
state-dependent or coherent interactions, entering the bench only as
effective classical parameters (σ(I), σ(x,t), dispersive ε(ω), gain) or Red
Team strikes it. Read `PANEL.md` in full; `LOGBOOK.md`'s RULED OUT registry
(R1–R31, with R29/R30/R31 read in full, lines ~1247–1398) and the T28
live-thread/Iteration-89 entries; `experiments/113-.../phase1_proposal.md`,
`run113.py`, `chunk_runner113.py`, `analyze113.py` in full; and
`experiments/112-.../phase5_review_quantum.md`/`phase5_redteam_audit.md` —
my own seat's founding R30 record, which this cycle's own Check C
recalibration explicitly builds on. Every numeric claim below is
independently re-derived from committed `results.json` arrays
(`experiments/110-.../results.json`, `experiments/112-.../results.json`),
not trusted from any document's own prose — this program's own R4/R9
discipline. No real FDTD run by me; Phase 4 has not started.**T1 confirmed
N/A structurally** — no σ(I)/σ(x,t)/angular-selectivity/sub-threshold
content anywhere in `run113.py`/`chunk_runner113.py`/`analyze113.py`; my
charter's usual gate is silent this cycle, matching every T28
desk/instrument cycle since Iteration 46. My own charter's remaining live
question here — distinguishing genuine signal from instrument artifact at
a detection floor — is exactly what Check C's R30 recalibration claims to
do, so I audited it hardest, as directed.*

## Steel-man (142 words)

This cycle visibly internalizes this program's own hard-won lessons rather
than merely citing them. R29 module-naming risk is pre-empted with executed
identity asserts in every downstream file, not fixed reactively after a
crash. R31's same-session control genuinely gates the real spend before any
`Sim.run()`. `CPL_RATIO` normalization closes PHOTONICS' own real F3 units
confound, rather than leaving Check B free to trivially read SURVIVES at any
bin. Scope is properly restrained to one leg, matching R31's own founding
non-bundling lesson (five straight PARTIAL cycles disclosed, not hidden).
For my own charter specifically: the R13 `floor<=0.0` guard I found
non-robust in Iteration 88 poses no real misfire risk here — the
r=312/`cpl=20` floor (3.38e-4) sits nowhere near the pathological ~1e-18
regime my own adversarial construction required, so the still-unhardened
guard is correctly a disclosed backlog item, not a silent hazard specific to
this bin.

## Sharpest attack (145 words)

`classify_resolution_check`'s `supports_real_structure = percentile_in_null
<= 10.0` inverts, not merely calibrates, Check C's founding premise:
genuine resolution-stable structure should reproduce with HIGH correlation
across `cpl` (PHOTONICS' own founding docstring); R30 showed the OLD
`corr>=0.5` bar has zero discriminating power, not that low correlation is
diagnostic. I re-derived R30's own resolved/unresolved split from real
EXP110/EXP112 arrays: the gap (resolved mean 0.9793 vs unresolved 0.9921)
is thin, ranges overlap almost entirely, and is driven by 6 of the
pattern's 8 lowest-correlation bins sitting in "resolved" territory with
wildly varying SNR (1.3–287) — equally consistent with envelope
inflection/zero-crossing proximity, unrelated to "realness." Worse:
`local_diag["resolved"]` and `all_window_corrs` (full 48-bin arrays) are
already computed in `analyze113.py` once Phase 4 lands, zero marginal cost
— yet the code never re-runs this split-check on r=312's own data before
hard-coding the borrowed r=156 direction. Idealization 4 audits only the
threshold VALUE, never the direction.

## Supporting derivation (not part of the word-limited sections above)

Independently recomputed, zero new FDTD, from `experiments/110-.../
results.json["r156"]["raw_patterns"]["32"]["delta"]` (cpl=20 baseline) and
`experiments/112-.../results.json["pattern_delta"]` (real cpl=25 data),
replicating `run113.py::windowed_corr` exactly across all 48 bins:

- **Resolved population** (34 bins, per `local_diag_margin32["resolved"]`):
  mean **0.9793**, range **0.8169–0.9996**.
- **Unresolved population** (14 bins): mean **0.9921**, range
  **0.9689–0.9995**. (Matches `phase5_review_quantum.md`'s own 0.9793/0.9916
  to within its own rounding — confirmed bit-consistent.)
- Removing the single lowest resolved-population value (0.8169) raises the
  resolved mean to **0.9842** — closer to, though still below, the
  unresolved mean. The gap is not carried by one outlier alone: of the
  pattern's 8 lowest correlations overall, **6 sit in the resolved
  population** (SNR values 126.9, 130.5, 1.33, 1.35, 70.4, 67.7 — no
  monotonic relation to correlation, and no monotonic relation to how
  strongly "resolved" each bin is). This is consistent with those bins
  clustering near zero-crossings/inflections of the shared smooth
  diffraction envelope (where a ±2-bin window's local slope is most
  sensitive to exactly where a coarser vs finer grid places its sample
  points) rather than with anything about whether the bin carries a real,
  independent sub-wavelength feature. Both explanations produce the
  identical observed direction; exp-112's own Phase-5 record (and R30's own
  text) never distinguished between them — it stopped at "no discriminating
  power," which is the only claim actually established.
- The named r=156 bin's own correlation (0.9994) sits at the **89.6th
  percentile** of that pattern's own 48-window null (self-inclusive,
  matching this cycle's own Idealization 3 convention) — i.e., under
  exp-113's own new rule, it would NOT have been called a low-percentile
  outlier. No contradiction with old data, but also no positive evidence
  that a low-percentile reading, wherever it appears, means what
  `run113.py`'s own comment (line ~269–271: "LOW correlation = LESS like
  the generic pattern-wide behavior = more consistent with a bin-specific
  feature") asserts it means. That sentence is this cycle's own new,
  undisclosed-as-such interpretive premise — Idealization 4 discloses only
  that the *10th-percentile threshold value* is "not independently
  re-derived"; it never states that the *direction* (low vs. high) is
  likewise an undemonstrated, newly-adopted assumption, imported from a
  different `r`'s own thin, confounded, alternatively-explicable data.

**The concrete, low-cost fix R30's own text already licenses and this
cycle's own committed code already has the ingredients for**: the moment
Phase 4's three real FDTD calls complete, `analyze113.py` already computes
both `local_diag_margin32["resolved"]` (the full 48-element mask, at
r=312/`cpl=20` via `R.BASELINE_RESOLVED`'s own source array, and at
`cpl=25` via the fresh `local_diag`) and `resolution_check["check_c"]
["null_scan"]["all_window_corrs"]` (the full 48-element correlation array)
— but never cross-tabulates them. Doing so (resolved-vs-unresolved mean/
median windowed correlation, computed at r=312 the same way exp-112's own
Phase-5 review did at r=156) is zero marginal FDTD cost and would show
directly whether the borrowed low-percentile direction actually replicates
at this geometry, or reverses again — exactly the check R30's own text
requires ("checked against its own already-computable null/background
population... before its reading is cited with evidentiary language") but
`classify_resolution_check` does not perform.

## Verdict: **support-with-changes**

Not oppose: T1 is genuinely N/A, R29/R31 discipline is real and correctly
executed, Check B's `CPL_RATIO` fix is a genuine, well-evidenced
improvement, and the leg is worth running — Check A and Check B-normalized
alone are pre-registered, well-understood instruments untouched by this
critique. Not plain support: Check C's `supports_real_structure` field, as
coded, will attach a specific, load-bearing evidentiary direction
("candidate real structure") to the named bin the moment `percentile_in_
null <= 10.0` fires — and that direction rests on exactly the kind of
uncalibrated, evidentiarily-cited inference R30 exists to forbid, one level
removed: R30 was ratified to stop citing an *uncalibrated threshold*
evidentially; this cycle calibrates the threshold but never checks the
*direction* it recalibrated it into, which is the more consequential of
the two choices (it determines which tail counts as signal at all, not
merely how strict the bar is).

**Mandatory change that would flip my verdict to support**: before any
Phase-5 Interpretation language cites Check C's `supports_real_structure`
reading evidentially in either direction, add the resolved-vs-unresolved
population cross-tabulation described above to `analyze113.py` (a few
lines over already-computed arrays, zero marginal FDTD) and report its
outcome alongside the named bin's own percentile. If the direction
replicates at r=312 (resolved population's own mean/median windowed
correlation again sits below the unresolved population's), the current
code's choice gains real, if still modest, support and I would move to
plain support. If it does not replicate — or reverses again — Check C's
`supports_real_structure` field must be demoted to a disclosed, undirected
percentile reading (both tails reported, neither privileged as "supports
real structure") until a mechanistically grounded reason for a specific
direction is established, rather than inherited from a different `r`'s
own thin and alternatively-explicable data.
