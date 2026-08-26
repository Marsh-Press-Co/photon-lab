# PHASE 3 — SYNTHESIZE · Panel Iteration 52 · exp-075
## Director's resolution of Red Team's Phase-2 audit (`phase2_redteam_audit.md`)

*Director role per PANEL.md: synthesizes but does not vote in Phase 2;
states which criticisms are accepted and which are overridden, and why.
Red Team's Phase-2 verdict: **PROCEED-WITH-MANDATORY-FIXES**, five items,
priority-ordered. All five are ADOPTED. Zero overrides.*

---

## 1. Disposition table

| # | Item | Source | Red Team verdict | Director disposition | Where |
|---|---|---|---|---|---|
| 1 | Build + score the actual two-wall-cavity model, with a look-elsewhere/robustness check | PHOTONICS, sharpened by Red Team's own §3 | Mandatory | **ADOPTED — new work, this document's §3, executed in `two_wall_cavity.py`/`phase4_results.md`** | §3 below |
| 2 | Commit the `ABSORB`-depth residual cross-check to the permanent record | VISION, sharpened by Red Team | Mandatory | **ADOPTED — committed as code in `boundary_reflectance.py` (new §5b), re-run, numbers below** | §2 below |
| 3 | Add the matched-`eps=mu` realizability idealization | MATERIALS | Mandatory | **ADOPTED — in-place edit, `phase1_proposal.md` Idealization 2** | done, this commit |
| 4 | Correct Test A/B narrative precision (boundary-search artifact; sign-significant anti-correlation; "narrows the space" framing) | QUANTUM, Red Team's own core finding | Mandatory | **ADOPTED — in-place edits, `phase1_proposal.md` §5, all three sub-items** | done, this commit |
| 5 | Cross-module phase-convention gate (informational, bind forward) | ELECTROMAGNETISM | Informational only this cycle | **ADOPTED as informational** — not required to ship with item 1 unless item 1's own composition reuses the same coherent-sum machinery in a way that makes it load-bearing (it does — see §3.4) | §3.4 below |

**Nothing is overridden.** This matches Red Team's own read (§5 of its
audit: "Nothing here is overridden — every one of the five critiques'
load-bearing claims independently reproduces, several more sharply than
as first written").

---

## 2. Mandatory fix 2, executed — and a same-cycle arithmetic correction found while executing it

`boundary_reflectance.py` now computes (new §5b, re-run this shift) the
model's own per-config echo term `C_with_wall(ABSORB) − C_boundary_free`,
its `ABSORB`-depth amplitude scaling, and all six cross-config Pearson
correlations. Bit-exact against Red Team's own audit numbers on amplitude
(`ptp`: 7.978e-4 / 1.174e-4 / 1.927e-5 / 2.810e-5 at ABSORB=40/60/70/80)
and on every individual correlation (`r(40,60)=-0.985`, `r(40,70)=-0.203`,
`r(40,80)=+0.913`, `r(60,70)=+0.276`, `r(60,80)=-0.924`, `r(70,80)=-0.560`).

**One correction, found running this as committed code rather than restating
the audit's own prose (house rule R4, exactly the discipline this rule
exists to enforce, applied here to Red Team's OWN output — nobody's
arithmetic gets a pass):** `phase2_redteam_audit.md` §2e states "three of
six pairs negative." Counting the six values printed above: `r(40,60)`,
`r(40,70)`, `r(60,80)`, `r(70,80)` are negative — **four of six**, not
three (`r(40,80)` and `r(60,70)` are the two positive pairs). This does
not change the finding's substance — a majority (4/6, not a bare 3/6) of
the model's own predicted echo-shape pairs are negatively correlated
across `ABSORB` depth, sharply contradicting the real data's near-identical
(`r=0.992-1.000`) residual shapes, an even starker contrast than Red
Team's own write-up stated. Corrected here, in the permanent, code-backed
record; not a live defect in the finding, a minor restated-number slip in
an otherwise independently-re-derived audit (flagged per this program's
own R4 addendum: any reproduction section must recompute, not restate).

Mandatory fix 3 and 4 are executed as in-place edits to
`phase1_proposal.md`, marked `[PHASE-3 FIX]` at their point of use,
verbatim per Red Team's own adjudication text — not re-derived here as
they required no new computation, only narrative correction.

---

## 3. Mandatory fix 1 — the two-wall-cavity model, DESIGNED and PRE-REGISTERED here, BEFORE it is run

### 3.1 What PHOTONICS actually found, and what Red Team's own look-elsewhere check showed

PHOTONICS' Phase-2 attack substituted the domain width `nx` for `PLANE_X`
in the ALREADY-EXISTING single-wall closed-form period formula — not a
physically derived two-wall model. Red Team's own audit (§3) found this
specific substitution sits in a wide (`0.77×`-`1.43×` of `D_needed`)
SUPPORT band, and that 2 of 11 named geometric constants in the same
`CONFIGS` dictionary land in that same band under the identical
substitution — a real, not-dismissable finding, but explicitly flagged as
"suggestive, not yet evidence" pending an actual computed model.

### 3.2 The actually-derived geometry (zero data, computed here, before any real-data comparison)

The scene has TWO PEC walls (`lab/fdtd2d.py::Sim.run`, confirmed:
`Ez[1:-1,1:-1]` is the only slice ever updated by the curl step — indices
`0` and `nx-1` are permanently zero on both edges), both backed by an
`ABSORB`-thick graded-loss band of IDENTICAL construction (same
`self.absorb`, same cubic ramp — `lab/fdtd2d.py::_damping` applies to all
four edges with the same formula). The already-built `-x`-wall echo uses
mirror image at `x=-SRC_X`, giving interferometer-arm path difference
`2·PLANE_X` (source-position-independent, `phase1_proposal.md` §2e). By
the exact same interferometer-arm argument, applied to the OTHER wall
(mirror image at `x = 2·(nx−1) − SRC_X`), the path difference reduces to
`2·((nx−1) − SRC_X)` — call this `D_right`, the physically correct
"source-to-far-wall" distance, NOT the raw domain width `nx` PHOTONICS
substituted.

Computed here, in code (`two_wall_cavity.py::closed_form_period`, not
hand-typed — R4), from `experiments/065-.../design_geometry.py::CONFIGS`
directly:

| `ABSORB` | `D_left` (=`plane_x`) | `D_right` (=`nx-1-src_x`) | `P_left(39°)` | `P_right(39°)` |
|---|---|---|---|---|
| 40 | 77 | 59 | 11.824° | 15.431° |
| 60 | 97 | 79 | 9.386° | 11.525° |
| 70 | 107 | 89 | 8.509° | 10.230° |
| 80 | 117 | 99 | 7.782° | 9.196° |

**Both walls' own correctly-derived single-bounce echo period sits in the
same 7.8°-15.4° range — nowhere near `P*=2.8421°`, and if anything the
`+x`-wall (`P_right`) is FARTHER from the target than the already-tested
`-x`-wall.** This is a strong prior that PHOTONICS' `nx`-substitution
match was the look-elsewhere artifact Red Team's own §3 flagged it as
being at risk of, not a preview of what the real two-wall model predicts
— but it is not yet the same test. The real two-wall model coherently
SUMS both echo terms (not just their closed-form periods in isolation),
and a sum of two sinusoid-like signals at nearby-but-different periods
(11.8° and 15.4° at ABSORB=40, say) produces beat structure a per-
component closed-form period cannot show — so the actual numeric
interference calculation, not this table alone, is what gets scored.

### 3.3 Model construction

`two_wall_cavity.py` (new file, this directory) extends
`boundary_reflectance.py`'s own already-vetted machinery (imported, not
reimplemented — same house pattern `boundary_reflectance.py` itself used
for exp-048's propagator):

- `image_geometry_right(g, nx)`: mirror image through the `x=nx-1` wall,
  by the same interferometer-arm construction as the existing
  `image_geometry` (left wall), giving `D_SP_image = D_right` as derived
  in §3.2.
- `c_empty_two_wall(theta, lam, g, r, nx)`: THREE coherent terms — direct
  field + left-image weighted by `r` + right-image weighted by `r` (same
  `r(theta;ABSORB)`, both walls — justified below), summed before the
  `window_means`/`weber` reduction, reusing `dg048.field_and_h` exactly as
  the single-wall model does.
- **Same-`r`-for-both-walls justification (stated, not assumed):** the
  two `ABSORB` bands are geometrically identical (same thickness, same
  ramp) and the source's own phase-ramp construction
  (`lab/fdtd2d.py::add_line_source`) launches mirror-symmetric plane-wave
  components into BOTH half-spaces at the same incidence-angle magnitude
  `theta` from each wall's own normal (`k_x=∓k cosθ`, same `k_y=k sinθ`)
  — by the mirror symmetry of this empty, object-free scene (confirmed,
  `experiments/069/run.py::_one_run`, Red Team §0.3) in `x`, the two
  walls see the same physical incidence angle and the same medium, so the
  same `reflection_coefficient(...)` call is correct for both, not an
  independent idealization.
- **Idealization, stated up front:** only SINGLE bounces off each wall are
  modeled (no double-bounce/full round-trip terms) — justified
  quantitatively, not merely asserted: `|r|` is at most `0.0064` anywhere
  on the real dense-sweep grid (`boundary_reflectance_results.json`,
  `gate_passivity`), so a double-bounce term scales as `|r|² ≤ 4.1×10⁻⁵`
  — at least 150× smaller than the weakest single-bounce term in this
  file's own §2d table, and thus negligible against the observed real
  signal's own amplitude (`ptp≈4.0×10⁻³`) by more than two more orders of
  magnitude than the already-too-small single-bounce terms are. Not
  computed; stated as a bound, not swept under the rug.

### 3.4 Cross-module phase-convention item (mandatory fix 5), now load-bearing here

EM's Phase-2 finding (informational-only for the single-wall cycle, §1
above) becomes directly relevant the moment a SECOND coherently-summed
echo term is added: if `r(theta;ABSORB)`'s phase convention is
inconsistent with `dg048.field_and_h`'s own convention in a way that
happens to cancel for one echo term but not two, the two-wall sum could
show a spurious phase relationship between its two echo contributions.
Mitigation, not a full resolution (EM's own gap stays genuinely open per
Red Team §2c): `two_wall_cavity.py` reuses the IDENTICAL
`c_empty_with_wall`-style composition (`E_direct + r·E_image`, coherently
summed, then the SAME `window_means`/`weber` reduction) for BOTH images —
whatever convention relationship exists between `r(theta)` and
`dg048.field_and_h` is applied IDENTICALLY to both terms, so a convention
mismatch, if one exists, enters both echo contributions the same way
rather than differentially — the two-wall model does not introduce a NEW
convention-mismatch risk beyond what the already-tested single-wall model
already carries. Flagged, not resolved; binding for any THIRD echo/cavity
variant this program builds in the future (per EM's own request).

### 3.5 Pre-registered falsifiable bands (frozen HERE, before `two_wall_cavity.py` touches the real `block_dense.rows` data)

**Reused verbatim from `phase1_proposal.md` §5** (Red Team's own
instruction: "on the same pre-registered-style bands") — Test A (period
match, SUPPORT≤0.30/REFUTE>1.00 relative deviation from `P*=2.8421°`) and
Test B (shape match, Pearson `r²`, SUPPORT≥0.30/REFUTE≤0.05), same
combining rule (REFUTE if EITHER test REFUTEs). Not re-tuned for this
mechanism — the same bands this program already committed to for the
single-wall test, applied to a structurally different model.

**New robustness/null-calibration leg, per Red Team's own mandatory
instruction ("must ship with a look-elsewhere/robustness check")**: a
CIRCULAR-SHIFT null-calibration test on Test B — the genuinely
order-preserving construction this program's own standing rule (R6,
LOGBOOK.md) requires for any null built on this kind of angularly-
autocorrelated data (T28's own real residuals are known
θ-autocorrelated, lag-1≈0.92-0.94, exp-074 Iteration 51). The model's own
FIXED predicted `delta(theta)` curve is compared against `N=20,000`
circular shifts of the REAL `delta(theta)` array (preserving its own
autocorrelation structure, unlike an i.i.d. permutation), giving a
p-value for the observed `|r|` under a null that respects the real data's
own known structure — the exact class of control this program's own R5/R6
addenda (Iterations 47/50) exist to require before an un-obviously-not-
coincidental match is trusted.

### 3.6 Prediction, committed BEFORE running `two_wall_cavity.py` against real data

**Primary prediction: Test A REFUTEs again.** Both walls' own correctly-
derived closed-form single-bounce periods (§3.2, `P_left`∈[7.8°,11.8°],
`P_right`∈[9.2°,15.4°]) sit far from `P*=2.8421°` — closer to each other
than either is to the target. A coherent sum of two components at similar,
still-far-from-target periods is expected to show beat structure with an
envelope period LONGER than either component (not shorter, and not
suddenly resonant at 2.84°) — the physics offers no mechanism by which
combining two ~8-15°-period signals produces a clean ~2.84° period. Stated
plainly: **this prediction expects PHOTONICS' `nx`-substitution match to
be confirmed as the look-elsewhere artifact Red Team's own §3 flagged it
as being at risk of** — but this is a prediction, not yet a result; the
actual numeric model, not this closed-form reasoning, is what gets scored
in `phase4_results.md`.

**Test B: no strong directional prediction** — a wrong-signed shape
correlation (as the single-wall model showed) is plausible but not
derivable in advance from the closed-form periods alone; reported as
observed.

**Falsification of this prediction (i.e. what would make this cycle's
finding a genuine positive lead rather than a second REFUTE):** Test A
SUPPORTs (rel_dev≤0.30) AND the circular-shift null-calibration p-value on
Test B is ≤0.05 (a real, non-look-elsewhere-explicable shape match). Per
Red Team §9: "If item 1 instead lands inside a properly-computed SUPPORT
band, that is this program's first real positive lead on T28's mechanism
in seven cycles, and would itself be a Checkpoint-2-adjacent finding" —
noted here, in writing, before the run, exactly as house discipline
requires.

---

## 4. What happens next

`two_wall_cavity.py` is written and run per §3's design; results go to
`phase4_results.md`, scored against §3.5's bands, checked against §3.6's
prediction — committed as a SEPARATE commit from this synthesis (predict/
results pair, house discipline, non-negotiable). Phase 5 (six blind
reviews + Red Team final audit) follows once Phase 4 lands.
