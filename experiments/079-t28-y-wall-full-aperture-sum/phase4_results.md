# PHASE 4 — TEST · Panel Iteration 56 · exp-079

*Director. Zero new `lab/` diff, zero new FDTD — this cycle's entire Phase 4
is re-running the Phase-3-corrected `y_wall_aperture_sum.py` (mandatory-fix
docket item 3: the reflectance-ablation control + T21-forced-fit sub-check
folded in as committed code) and confirming every frozen/expected number.*

---

## 1. What changed in the script between Phase 1 and this run

**Correction (Phase-5 review, THERMODYNAMICS; figure re-verified,
corrected, by the Director before commit — R4 applies to a reviewer's own
recomputation too): the as-first-written version of this section overstated
its own claim.** `git diff 9e4e1ae 3673d42 --
experiments/079-.../y_wall_aperture_sum.py` shows **3** deleted lines, not
zero (THERMODYNAMICS' own review cited 4; independently re-run here,
`git diff ... | grep -c '^-[^-]'` = 3, not 4 — corrected in place, matching
this program's own R4 discipline that a reviewer's recomputation is not
exempt from being re-verified): the renumbered summary header
(`[7] SUMMARY` → `[8] SUMMARY`) and one extended dict literal
(`out["summary"] = dict(...)`, widened to add the new ablation/forced-fit
fields) required removing their own original lines before the replacement
was inserted. The substantive claim stands correctly: every PRE-EXISTING
computed value (§[0]–§[6]: geometry, gates, the primary/secondary
coherent-sum model, the real-data periods, the convergence check) is
unchanged line-for-line and reproduces bit-identically (§2, below) — the
deletions are cosmetic renumbering/dict-literal edits, not a removed
computation. "Only additive" was the wrong word for what a line-diff
shows; "no computation removed or altered" is the correct, and now
independently re-verified, claim.

## 2. Confirmation against Phase-3's own stated expectations

`phase3_synthesis.md` §4 stated, before this run: *"ablated `PAIR_PAD`/
`C80−C40` periods within a few hundredths of a degree of the r-weighted
model's own periods; `PAIR_ABSORB40`'s ablated delta expected to be
small-to-exactly-zero given G40/C80's shared geometry."*

**Confirmed, exactly:**

| quantity | expected (pre-run) | measured |
|---|---|---|
| `PAIR_PAD` `\|ΔP*\|` (r-weighted vs ablated) | few hundredths of a degree | `0.0150°` |
| `C80−C40` `\|ΔP*\|` | few hundredths of a degree | `0.0226°` |
| `PAIR_ABSORB40` ablated delta | small-to-exactly-zero | **exactly zero** (`ptp=0.000e+00`) |
| `C80−C40` T21-forced-fit `rel_dev` | (not numerically pre-stated; Red Team's own §0 item 9 cited `0.3101`) | `0.3101` — **matches Red Team's own independent computation exactly** |
| `C80−C40` T21-forced-fit R² | (Red Team cited `0.9425`) | `0.9425` — **matches exactly** |

All pre-existing Test-A numbers (`rel_dev`, R², `ss_tot` ratios, gates,
convergence check) reproduce bit-identically to the Phase-1 run — no diff
in `y_wall_aperture_sum_results.json` for any pre-existing key.

## 3. New, non-load-bearing finding from the extended run

`PAIR_ABSORB40`'s ablated delta is not merely close to zero but **exactly**
zero to the last printed digit — a stronger result than "small," confirmed
mechanistically (§7 of `y_wall_aperture_sum.py`'s own new code comment):
`G40` and `C80` share the identical `(OBJ_Y,y_lo,y_hi)=(832,80,1584)` triple
(both `PAD=40`), so once `r(theta_local(y_s))` is replaced by a config-
independent constant, their two aperture sums are bit-identical by
construction, not merely numerically close. This sharpens (does not
contradict) Red Team's own §2/Attack 1 finding: it shows `PAIR_ABSORB40`'s
real signal genuinely does require `ABSORB`-dependence (unlike `PAIR_PAD`/
`C80−C40`), while still landing on T21's own period — a two-part, not
uniform, confirmation, documented precisely in `phase1_proposal.md` §5.3
rather than folded into one blanket "indistinguishable" claim (which would
have overstated what the `PAIR_ABSORB40` case specifically shows).

## 4. Gates

- Zero new `lab/` diff (confirmed, `git status` on this shift).
- `SS_TOT_DEGENERATE` guard: correctly fires on `ABLATED(r=1) PAIR_
  ABSORB40`'s own exactly-flat array (`ss_tot=0.000e+00`, all three
  widening stages correctly flagged `SS_TOT_DEGENERATE`, matching exp-078
  Phase-5's own hardening working exactly as designed on a genuinely
  degenerate input — the trap that hardening exists to catch, now
  exercised for the first time by this file's own code, not merely a
  synthetic test case).
- `G-LOSSLESS`/`G-N1`/`G-PASSIVITY` at the full `[4.77°,15.50°]` envelope:
  unaffected by this cycle's code addition, re-confirmed clean on re-run.
- Evidence Gate: every number in the corrected `phase1_proposal.md` traces
  to this re-run's own `y_wall_aperture_sum_results.json`/`_output.txt`.

## 5. Combined result

**Test A (unchanged from Phase 1): 1/3 nominal SUPPORT (non-informative,
per the ablation control), 0/3 REFUTE, 2/3 INCONCLUSIVE (primary proxy);
0/3 SUPPORT (secondary proxy).** The reflectance-ablation control and
T21-forced-fit sub-check are now committed, reusable code — the mandatory-
fix docket's own item 3 is closed. See `phase1_proposal.md` §7 (revised)
for the full, corrected self-scored verdict this Phase-4 run confirms.
