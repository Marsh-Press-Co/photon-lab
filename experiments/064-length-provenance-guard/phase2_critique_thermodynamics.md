# exp-064 — Phase 2 Critique: THERMODYNAMICS

**Panel Iteration 41. Blind critique, fresh context.** Speaking only from
the THERMO charter: where absorbed energy goes, and whether the resulting
ΔT/emission is detectable. This is Iteration 40's own lead seat reviewing
a proposal that acts directly on code I own (`lab/thermo_sidecar.py`) and
on a disposition (TD-5, 1.2920×, 7.8× above κ_critical) I issued.

---

## Steel-man (≤150 words)

This does exactly what T23 needed after three prose-only deferrals. It
converts a docstring rule nobody could enforce into a keyword-only,
no-default `length_provenance` argument a caller cannot omit, backed by a
12-case zero-tolerance refusal gate (stage 24 group 1) and a bit-for-bit
regression identity (group 3) proving the retag changes zero already-
committed physics. My own Iteration-40 record already carried TD-5's
rear-only endpoint as "conditional on that length being licensed — not
yet a clean, self-contained finding" in prose (`NOTES.md`); QP-3 forces
that exact caveat into code, where it cannot be silently dropped by a
future caller the way the prose survived unenforced for three straight
cycles. The allow-list-not-deny-list design (§7) is the physically
correct shape for the underlying error class (extinction cross-section ≠
geometric length), and `biot_number` correctly needs no guard.

---

## Sharpest attack (≤150 words)

QP-3 formalizes WHERE `L` came from, never whether `L` is physically
achievable — and §6/Idealization 4 deliberately scope that question out.
But for THERMO's own energy chain the two aren't that separable: if no
real CNT forest taller than ~14µm has ever been grown, the 331–1051µm
solid TD-5 computes a ΔT for may not exist at ANY provenance tag, licensed
or diagnostic. `diagnostic_only=True` still returns a full dict — h_eff,
mass, area, correction_factor — with no field distinguishing "provenance
unlicensed" from "magnitude unconfirmed as buildable." A future caller
reading a green stage-24 diagnostic-path PASS could reasonably, and
wrongly, read 1.2920× as a validated absorbed-power→ΔT→detectability
chain for a real object, when §6 shows the object itself, not merely its
length's provenance category, is the open question. The guard closes the
narrower bookkeeping gap while leaving the wider one invisible to code.

---

## Verdict: **support-with-changes**

## The one change that would flip this to plain support

Give QP-3's resolution an explicit third state, or pick its second stated
option: either add a `geometric_realizability` field to the diagnostic
return dict (distinct from `length_provenance`) that a future caller must
also read, or — cheaper — adopt the option QP-3 itself names but leaves
undecided ("must be removed from the gated regression path entirely")
for the witness-scale calls, so a green stage-24 diagnostic-path check
can never be read as endorsing the buildability of the length it
reproduces, only the arithmetic.

---

## Answers to the Director's specific questions

**1. Does QP-3's retag preserve or change the Iteration-40 THERMO
verdict (1.2920×, 7.8× above κ_critical)?** Preserves it, exactly.
Stage-24 gate 3 requires the diagnostic-path call to reproduce stage 23's
own committed numbers bit-for-bit, and QP-5 commits to zero physics
change anywhere. I independently confirm this is the correct outcome:
retagging a number's provenance string cannot and should not change the
arithmetic that already passed five independent re-derivations
(Iteration-40 Phase-2/5 record). The 1.2920× figure and its 7.8× headroom
over κ_critical=0.0897 stand unmodified.

**2. Does marking those numbers `diagnostic_only` retroactively weaken
the epistemic status of Iteration 40's UNDETECTABLE-supporting
conclusion, or correctly express something already true, in stronger
form?** The latter. Iteration 40's own `NOTES.md` and `phase4_results.md`
already disclosed, in prose, that TD-5's rear-only endpoint is
"conditional on that length being licensed" and is "NOT yet a clean,
self-contained finding" — that caveat is not new information this cycle
introduces; it is exactly what my own cycle already knew and stated. What
changes is only the caveat's durability: a prose sentence in a Phase-3
document can be forgotten by a future caller who reuses
`front_surface_conduction_correction` with a new `L`; a required, no-
default `length_provenance` keyword argument cannot be silently skipped.
This is a strengthening of the epistemic record, not a weakening —
identical in kind to how `caveat_lint.py`/`numeric_lint.py` upgraded
hand-checked disclosure discipline into machine-checked discipline at
Iterations 38–40, a precedent this program has never treated as
retroactively undermining the findings it applies to.

**3. Is `biot_number` correctly left unguarded?** Yes, confirmed against
my own module's ground truth, not merely the proposal's claim. Reading
`lab/thermo_sidecar.py:294`:

```python
def biot_number(k_air: float, k_solid: float) -> float:
    ...
    return k_air / k_solid
```

The signature takes exactly two floats, no length argument of any kind —
`Bi_gas = k_air/κ_solid` is structurally length-invariant (this program's
own Iteration-22 Attack-6 identity, reused unchanged, T22). There is no
`l_geometric` parameter for `_validate_length_provenance` to intercept.
The proposal's own §3/§8 item 3 states this correctly and I find no
daylight between that statement and the actual function body — the guard
would be inert decoration on this one function, correctly omitted rather
than added for symmetry's own sake.

**4. Does §6's new finding (real Vantablack forest height ~14µm vs
331–1051µm witness-scale need) threaten any THERMO-sidecar margin, or is
it orthogonal to the TD-3/4/5 bracket?** Orthogonal to the ARITHMETIC,
not orthogonal to the CLAIM. TD-3/4/5's bracket is a boundary-condition
question at a FIXED `L` (front-colocated-loss vs. rear-only-loss); §6 is
a question about whether that `L` itself, independent of which boundary
condition governs it, corresponds to any object that has been grown.
Numerically the two are cleanly separable — nothing in §6 changes a
single digit of TD-3/4/5 or of stage 23/24's regression anchors, and I
can find no path by which a shorter real length would make the Biot
correction WORSE (`Bi_rad` scales linearly in `L`, so a true ~14µm length
would shrink, not grow, the rear-only correction factor relative to the
1051.2µm figure actually used — if anything the honest direction is more
comfortable, not less, on the correction-factor axis alone). But the
DETECTABILITY chain THERMO's charter owns is "absorbed power → ΔT →
emission → detectability," and every link in that chain presumes a real
absorbing object of length `L` exists to have a temperature. §6 does not
move TD-5's number; it calls into question whether TD-5's number
describes anything buildable at witness scale at all — a realizability
finding sitting one layer upstream of anything this guard's provenance
categories can express, correctly named by the proposal itself (§6) as
"adjacent to but distinct from T23," and correctly queued rather than
folded into this cycle's own scope. I do not fault the proposal for not
solving it here — I fault the guard's return dict for giving a future
reader no code-level signal that the question remains open even after a
call passes.

---

*THERMODYNAMICS, Panel Iteration 41, blind Phase-2 critique of exp-064.
No other seat's critique of this cycle was read before writing this.*
