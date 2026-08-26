# PHASE 5 — REVIEW · MATERIALS & METAMATERIALS · Panel Iteration 54 · exp-077

*Fresh sub-agent, blind to the other six seats' Phase-5 reviews. Read
PANEL.md in full; LOGBOOK.md RULED OUT R1–R8 and T28's full Iteration
46–53 history; exp-077's complete record (`phase1_proposal.md` as edited
in place, `phase2_redteam_audit.md`, `phase3_synthesis.md`,
`phase4_results.md`, `NOTES.md`, `pad_round_trip_model.py`); and ran my
own independent checks against `lab/fdtd2d.py` and
`boundary_reflectance.py` rather than trusting the write-up's numbers.*

---

## 1. Verdict: **PARTIAL**

The specific mechanism this cycle actually tested — a coherent echo off a
wall whose admittance is the exact matched-`eps=mu` numerical construct —
is correctly, robustly REFUTEd, and I independently confirm the
realizability bound the write-up attaches to it. But "PARTIAL," not "RULED
OUT," because the REFUTE does not extend to the thing MATERIALS actually
cares about: whether a *realizable* coating's own round-trip echo could
explain the data. That question was never asked this cycle, and my own
check below (§2) shows it is not a small correction — a realizable
substitution changes the wall's reflection coefficient by an amount
comparable to the margins several of this cycle's own REFUTE verdicts
were decided by.

---

## 2. Independent check: is Idealization 10 complete?

**Idealization 10, verified true as far as it states:** I re-read
`lab/fdtd2d.py::Sim._damping` directly (lines 122–129) and independently
re-derived, from scratch, that `damp_e`, `damp_hx`, and `damp_hy` are
built by calling the *identical* `self.absorb`-parameterized cubic ramp on
all four domain edges:

```
worst |damp_e[:absorb,yc] - damp_hx[:absorb,yc]| = 0.0
worst |damp_e[:absorb,yc] - damp_hy[:absorb,yc]| = 0.0
```

— confirming `verify_symmetric_damping`'s committed `worst_abs_diff=0.0`
independently, not by re-reading the JSON. This is the actual physical
content of "matched eps=mu": because E and *both* H components are
attenuated by the same multiplicative factor per cell, the effective
medium has **zero impedance mismatch at every point in the ramp** — that
is what makes it reflectionless-by-design as a numerical absorbing
boundary. A real optical coating cannot do this: real materials have
`mu_r ≈ 1` at optical frequencies (negligible magnetic response), so
matching a lossy electric response with an equal magnetic-loss response
across a broadband ramp has no realizable analog at these wavelengths —
correctly `unobtainium-with-parameters`, the identical bound exp-075
already established and this cycle correctly re-applies to the `+x` wall
(§2b/Idealization 10, confirmed independently at the source).

**What Idealization 10 does NOT say, and should — this is my own angle,
and it is quantitatively real, not merely conceptual.** I re-derived
`boundary_reflectance.py::reflection_coefficient` and confirmed at the
source (line-read, not cited) that the matched-admittance assumption
enters through one specific line:

```python
Z = n_prof / np.sqrt(n_prof.astype(complex) ** 2 - s2)   # matched (eps=mu) TE admittance
```

A real, `mu_r=1` dielectric/conductive coating (the physically realizable
case — the standard TE admittance for an ordinary medium) is instead
`Z' = 1/sqrt(n(x)^2 - sin^2(theta))` — no `n(x)` numerator factor. I built
this alternate admittance, ran it through the *same* recursive
transfer-matrix recursion, gate-checked it (`G-LOSSLESS` worst dev
`2.22e-16` for random real profiles, same as the committed gate), and
computed it against the *same* `n(x)` loss profile the committed model
already uses for `ABSORB=40` (so this isolates only the
matched-vs-unmatched admittance choice, nothing else):

| θ | matched \|r\| | matched arg | real (mu=1) \|r\| | real (mu=1) arg | \|r_real/r_matched\| |
|---|---|---|---|---|---|
| 36.0° | 0.0029 | −78.12° | 0.0041 | −102.78° | 1.40 |
| 39.0° | 0.0043 | −40.91° | 0.0053 | −63.38° | 1.25 |
| 42.0° | 0.0064 | −1.23° | 0.0074 | −19.48° | 1.15 |

(My matched-column reproduces §2e's committed table bit-for-bit,
confirming my re-derivation is methodologically sound before trusting the
comparison column.)

Swapping only the realizability-blocking assumption — nothing about the
loss profile itself — moves `|r|` by 15–40% and `arg(r)` by 15–24° across
the tested window. That is not negligible against this cycle's own
decision margins: the two-wall `PAIR_ABSORB40` Test B REFUTE sits at
`r²=0.0418`, just under the `≤0.05` REFUTE ceiling; the two-wall
`PAIR_PAD` Test A sits at `rel_dev=0.88`, just under the `>1.00` REFUTE
line from the other side. A phase shift of this size, propagated through
`c_empty_with_wall`'s coherent sum, is large enough to move numbers that
close to a bar — I am not claiming it *would* flip a verdict (that
requires actually re-running Test A/B with a real profile, which this
cycle did not do and which I have not fully done either), only that the
question is open and material, not closed by Idealization 10's own
language.

**Answer to the task's direct question:** REFUTE here is a statement
about one specific, zero-free-parameter model's fit to the data — it says
nothing about whether a *different*, realizable admittance's echo could
match, because the model's entire predicted curve is a function of
`r(theta)`, and `r(theta)` changes non-trivially (magnitude and phase
both) the moment the unrealizable matched-admittance assumption is
dropped. The concept "PAD's round-trip distance drives a coherent echo"
is not exercised against any physically buildable structure by this
cycle — only against the one construction that is, by the panel's own
established bound, impossible to build. Idealization 10's narrow claim
("cannot move the realizability bound... says nothing new about
realizability") is correct and I found no error in it. What is
incomplete is the surrounding record's broader framing (`NOTES.md`'s
"the coherent-echo mechanism class now doubly excluded," and its "Next"
section floating "no known mechanism class remains untested") — that
overstates what has actually been shown. Only one (unrealizable)
*instantiation* of the coherent-echo class has been excluded, twice; an
entire family of realizable instantiations has never been tried.

One further honest caveat on my own check, so it is not over-read either:
period (Test A) is set almost entirely by the round-trip geometric
distance (`PLANE_X`), not by `r(theta)`'s own value — so a realizable
substitution is unlikely to rescue Test A's already-marginal numbers.
Where it plausibly matters is Test B (shape), which is exactly where this
cycle's own two-wall numbers are weakest (`r²=0.0001`–`0.0418`, an order
of magnitude below the `0.30` SUPPORT bar) — a large phase change could
move these but is very unlikely to move them by two orders of magnitude
to clear 0.30. My honest expectation, stated before anyone runs it: most
likely still REFUTE, but genuinely untested, not merely a formality — and
per this program's own R8 standard, an untested-but-affordable,
outcome-relevant check should not be treated as already settled by an
unverified expectation (mine included).

---

## 3. A materials-class candidate worth nominating for Iteration 55

Yes. The lab already possesses a realizable, previously-characterized
recipe: `lab/materials.py::graded_black_shell` — a real, `eps_r≈1`
(broadband index-matched, no reflecting interface), conductivity-graded
(quintic-smoothstep `sigma_e(x)`) absorbing coating, already established
in this program at **R ≤ 0.2% across 450–750nm (0.10% @ 600nm,
normal-incidence characterization)**. This is a genuinely different
sub-wavelength structure class from the matched-`eps=mu` numerical
construct: it achieves low reflectance through index-matching plus real
electric loss alone, with no magnetic response required anywhere —
published/plausible physics, not unobtainium.

**Concrete Iteration-55 proposal:** map `graded_black_shell`'s own
`eps_r(x)`/`sigma_e(x)` profile (scaled to the `ABSORB=40`/`80`-cell
thickness this bench already uses) onto a complex `n(x)`, feed it through
the *same* recursive transfer-matrix machinery already committed in
`boundary_reflectance.py`, but with the standard (non-matched, `mu_r=1`)
TE admittance formula in place of the matched one — and re-score Test A/B
against the same already-collected `PAIR_PAD`/`PAIR_ABSORB40` real data.
Zero new FDTD calls (the coating's own `_graded_black` closed-form profile
is analytic); reuses `_free_period_search`, the gates, and the real-data
JSON exactly as this cycle did. This is the direct, cheap, and — unlike
this cycle's own two-wall extension — *materials-progress-capable* test:
a SUPPORT here would be the first T28 finding in this six-plus-cycle
sub-thread to implicate a structure this lab could plausibly build; a
REFUTE would newly and properly close the entire realizable branch of the
coherent-echo class, which nothing to date has done.

One caveat to carry into that proposal, quantified above, not asserted:
because a real, unmatched admittance generically increases `|r|` (my
check: 15–40% larger at this loss magnitude) rather than decreasing it,
a realistic coating is at least as likely to worsen amplitude match as
improve it — the "realizable ⇒ automatically weaker signal" intuition is
not obviously correct here and should not be assumed either way before
the fit is actually run.

---

## 4. Ranked top candidates for Iteration 55 (MATERIALS' own ranking)

1. **Realizable-admittance refit (§3, above).** Swap
   `boundary_reflectance.py`'s matched-`eps=mu` admittance for
   `graded_black_shell`'s real, already-characterized `eps_r`/`sigma_e`
   profile in the *same* transfer-matrix/echo-model architecture, rescore
   Test A/B against `PAIR_PAD`/`PAIR_ABSORB40`. Zero new FDTD. Directly
   closes the gap §2 identifies, and is the only pending T28 test that can
   move MATERIALS' realizability bound in either direction — the two-wall
   extension explicitly could not (Idealization 10, confirmed).
2. **State the realizability caveat as a standing scope note on the whole
   coherent-echo mechanism class, not just this cycle's two-wall
   extension**, before any further instrument-fidelity work on T28
   proceeds — cheap, zero-FDTD, prevents the "no known mechanism class
   remains untested" framing (`NOTES.md`'s own "Next" section) from
   hardening into a false Checkpoint-2 claim. A materials-realizable
   branch of this exact mechanism class remains genuinely open; a
   Checkpoint-2 "mapped mechanism-class boundary" claim is premature until
   item 1 is actually run.
3. **If item 1 also REFUTEs**, broaden the admittance search beyond one
   named recipe before declaring the whole coherent-echo class closed:
   price an explicit realizability *ceiling* — the best broadband,
   oblique-incidence (36–42°), sub-wavelength anti-reflection/absorptive
   coating this program can point to in the published metamaterial
   literature (moth-eye graded-index ARCs are the standard published
   comparison class) — and check whether the coherent-echo model's
   predicted amplitude can even reach the observed `amp_ratio=0.119` at
   that ceiling, independent of period/shape matching. This is a pricing
   check in the R7 sense: it must be followed by an actual fit before it
   is used to certify closure, not substituted for one.

---

## Compliance note

No RULED OUT item is re-opened. R4: every number above I either
reproduced independently from the committed JSON/code or computed myself
from primitives and disclosed as my own (§2's alt-admittance table),
never hand-typed from the write-up. R5/R8: my own alternate-admittance
check is disclosed as illustrative and unverified for outcome (I explicitly
do not claim a flipped verdict), consistent with R8's standard that an
unverified expectation may not be filed as settled ahead of the actual
affordable check.
