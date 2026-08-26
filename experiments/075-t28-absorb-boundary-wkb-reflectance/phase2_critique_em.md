# PHASE 2 — CRITIQUE · ELECTROMAGNETISM · Panel Iteration 52 · exp-075

*Fresh sub-agent, ELECTROMAGNETISM charter (field/wave behavior, impedance
matching, energy coupling; owns the reciprocity / passivity / causality
bookkeeping — formalizes what T1 permits and forbids for each proposal;
T1 itself N/A this cycle). Blind to the other six seats' current-cycle
critiques.*

---

## 0. Independent verification performed (R4 — recompute, don't trust)

Ran `boundary_reflectance.py` unmodified: reproduces every number in
`phase1_proposal.md` and `boundary_reflectance_results.json` exactly
(`COMBINED VERDICT: REFUTE`, `rel_period_dev=4.28`, `shape_r2=0.2586`,
`Pearson r=-0.508`). Read `lab/fdtd2d.py` lines 72–264 directly: the
damping-order claim in §2a is correct — `Hx`/`Hy` are multiplied by
`damp_hx`/`damp_hy` immediately after their curl update (before that
damped H is used to update `Ez`), and `Ez` is multiplied by `damp_e`
*after* both the curl update and source injection (lines 226–253) —
verified against the code, not assumed. Confirmed `_c_empty`/`_one_run`
in `experiments/069/run.py` place **no** material object in the scene
(`Sim` + `add_line_source` + `.run()` only) — `sigma_e` is genuinely
zero everywhere in the dataset this proposal is tested against, so the
σ_e-composition question the task packet raises is real in general but
moot for *this specific* comparison; the proposal is correct not to
build an equivalence.

I then independently re-derived the friction-PDE dispersion relation
from `lab/fdtd2d.py`'s own literal update-equation signs (not the
proposal's own re-derivation) and, per R4, ran a direct numerical test
of the passivity-branch claim rather than trusting the prose:

```
n_minus = 1 - i*nu/omega   (proposal's "corrected" branch)
n_plus  = 1 + i*nu/omega   (proposal's "first tried, fails passivity" branch)
```

These are exact complex conjugates of each other, cell by cell. I
verified numerically that `kx(n_plus) == conj(kx(n_minus))` to machine
precision at *every* cell (both `z = n²-sin²θ` and its `sqrt` obey
conjugation exactly — no branch-cut crossing). Yet feeding these into
`reflection_coefficient()` gives `|r(n_minus)|=0.0043` vs.
`|r(n_plus)|=234` at θ=39°, ABSORB=40 — a ~5-order-of-magnitude gap
between two profiles that are pointwise conjugate. The cause: the
recursive `Zin = Zi*(Zin+1j*Zi*t)/(Zi+1j*Zin*t)` formula has an
explicit, un-conjugated `1j` baked into it (a standard EE
transmission-line convention with its own fixed time convention) — so
`r(n*) ≠ r(n)*` in general here, even though a naive rational-function
argument says it should for real-coefficient recursions. **This
confirms, numerically, that G-PASSIVITY is discriminating between two
branches whose difference is a genuine convention mismatch, exactly as
§2b's own prose suspects** — but also shows the discrimination is a
pure magnitude fact about one hard-coded formula, not an independent
physical re-derivation.

I then tested the most obvious candidate fix directly: recomputing
`c_empty_with_wall` with `r → conj(r)` instead of the committed `r`.
**Result: Pearson r goes from −0.508 to −0.542 — it does NOT flip
sign.** So I cannot hand the Director a specific correction that
resolves Test B; I can only show that nothing in this proposal's own
three gates is capable of *detecting* a cross-module phase error, and
that the simplest such error is not, in fact, the culprit.

---

## 1. Steel-man (≤150 words)

Real, first-principles physics, not a re-fit — the correct move after
six statistical cycles. The WKB-vs-exact choice is argued and checked,
not asserted: the adiabaticity diagnostic is computed and correctly
read as marginal (0.089–0.178), and the exact recursive transfer matrix
is used instead precisely because a single-pass Born integral would not
be trustworthy at 2–4λ. The "matched E/H loss ⇒ Z=1 at normal
incidence" claim is an exact algebraic consequence of Idealization 2's
stated premise, not hand-waved — I re-verified `(1-ix)²=1-x²-2ix`
identically. G-LOSSLESS's `|r|=1` identity for any real profile is a
genuine, convention-independent check that the transfer-matrix code
itself is not buggy. Test A's REFUTE (`rel_dev=4.28`, the model's own
free period running to its search boundary) is set by the fixed,
measured geometric quantity `PLANE_X`, not by any loss-model detail —
that part of REFUTE is robust to everything below.

## 2. Sharpest attack (≤150 words)

**The passivity gate resolves a magnitude ambiguity in one hard-coded
formula's convention, not a physical ambiguity — and nothing gates
whether the resulting phase is consistent with the separately-authored
exp-048 propagator it is coherently summed against.** I confirmed this
directly (§0): the two candidate branches are exact conjugates
pointwise (`kx` included, to machine precision), yet `|r|` differs by
5 orders of magnitude, because the Zin recursion's own `1j` factors are
not conjugation-covariant — a real, load-bearing convention artifact of
the borrowed transmission-line formula, not a property of the physics.
G-N1's own random trials only ever sample `Im(n)∈[0,1.5]`, so it never
even self-tests the "corrected" branch. Test B's wrong-signed shape
correlation (r=−0.508) is exactly the symptom a cross-module phase
error would produce — I tested the obvious fix (r→r*) and it does
**not** flip the sign, so I cannot confirm this is the cause, but I can
confirm the proposal's own gates are structurally blind to this class of
error and REFUTE's amplitude/shape half rests on an unvalidated phase.

## 3. Verdict

**Support-with-changes.** Test A's REFUTE (period off by >4×, pinned to
the fixed geometric distance `PLANE_X`, independent of any loss-branch
or phase convention) is solid and would survive any fix to the issue
above — I see no plausible correction that moves `PLANE_X` by the
required 3–5×, so **idealization 4 (vacuum-Snell oblique substitution)
cannot plausibly be the missing factor for the period mismatch**: that
idealization perturbs the reflection phase/magnitude at a given angle,
not the interferometer baseline `2·PLANE_X` that sets the period scale
itself. Combined REFUTE is therefore not premature on the period axis.
But Idealization 3's "resolved by an unambiguous physical requirement"
language overclaims what G-PASSIVITY actually establishes, and Test B's
amplitude/shape conclusions (the ~5× and the wrong-signed correlation)
rest on a phase this proposal never independently validates against the
Huygens-Fresnel module it is summed with — those specific numbers
should be reported with that caveat attached, not folded into the same
confidence level as Test A.

Reciprocity: not violated as constructed — the mechanism is a linear,
time-invariant, gyrotropy-free medium, and G-LOSSLESS's unconditional
`|r|=1` identity is itself a reciprocity-consistent statement; I see no
separate reciprocity concern beyond the phase-convention issue above.

## 4. Single change that would flip my verdict

Add a **fourth gate that is convention-agnostic**: re-derive `r(theta)`
by a second, independently-coded route that fixes its own sign
convention from the friction-PDE alone (e.g., verify the recursion
against a direct finite-difference time-stepping of the *stated*
continuous ODEs `dE/dt=cdH/dx-νE`, `dH/dt=cdE/dx-νH` over the same
profile, rather than only against another closed-form instance of the
same transmission-line formula) and confirm it agrees with the
committed `r(theta)` in phase, not just magnitude. If that check passes,
I move to unqualified support (Test B's numbers become as trustworthy as
Test A's, and REFUTE is fully load-bearing). If it fails and a corrected
phase changes Test B's sign, the Combined Verdict's period-based REFUTE
would likely still stand (per §3), but the "rules out this mechanism
class narrowly" framing in §5 of the proposal would need to soften to
"rules out this mechanism at this scale," since a mis-conventioned phase
would mean the shape/amplitude comparison was never actually testing
the intended physics.
