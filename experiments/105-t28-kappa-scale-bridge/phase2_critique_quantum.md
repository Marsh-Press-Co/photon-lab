#### QUANTUM OPTICS — verdict: **support-with-changes**

*Blind Phase-2 critique, candidate exp-105 ("The T8 r=78/156/312 Bridge,
Extended to the Coherent Point/Region-Intensity Channel"), Panel Iteration
82. Independently verified against `phase1_proposal.md`,
`experiments/030-scale-bridge/{NOTES.md,design_geometry.py}`,
`experiments/102-.../run.py`, `experiments/103-.../run.py`,
`experiments/104-.../run.py`, and this seat's own prior Iteration-7
critique in LOGBOOK.md.*

**Steel-man.** Disciplined instrumentation work squarely inside the T1:N/A
/ expressibility-contract lane. `graded_black_shell`'s `sigma_max(κ)=0.5/κ`
is the identical, already-Red-Team-adjudicated **static, position-only**
conductivity rescale from T8 (Iteration 7) — confirmed against
`lab/materials.py`/`run.py`: a fixed `σ(r)` profile, no intensity or time
argument threaded anywhere. Crucially, this cycle never touches the
OFF-lab/OFF-field σ(I)-proxy sponges — the one place my own Iteration-7
attack actually bit (the τ-held-vs-σ-held convention clash) — so that
specific confound structurally cannot recur here, even though it reuses
the same T8 rescale machinery. Gate P0/P1's ground-truth-recovery
discipline against exp-103/104's own committed numbers is exactly the
right precondition before any new-scale reading is trusted, and the
r=312 cost-gating explicitly incorporates T8's own 8× timing-miss lesson
rather than repeating it blind.

**Sharpest attack.** P4 predicts exp-104's clean r=78 ripple-null
reproduces "unmodified" at r=156/312 because "nothing about the article,
the channel construction, or the `H_REGION_WIDE/POINT` box widths... has
changed — only the object/domain scale." But this proposal's OWN §2a
geometry shows the object/domain scale IS the whole story: `z/z_R∝1/r²`
forces `x(78):x(156):x(312)=4:2:1`, i.e. the Fresnel number
`N_F=r²/(λ·D_eff)` grows **16×** from r=78→312 — the identical
Fresnel-crowding mechanism PHOTONICS and EM used in T8's own Iteration-7
critique to explain why a fixed-offset r-family under-samples a
hard-edged object's own diffraction ripple (P-VISION-1b's bands were
flagged there as "forced by geometry, not physics" for exactly this
reason). If a genuine ripple exists near this bench's own graded shell,
its period should plausibly SHRINK, not hold at ~10 cells, as N_F grows
— yet `DENSE_PITCH` stays fixed at 2 cells (not κ-scaled), with no
computed prediction of where a real period should land at the new
scales. A P4 "FALSIFIED" at r=312 could therefore be a second-generation
degenerate-aliasing null, not a genuine one — exactly the failure class
exp-104 exists to rule out, silently recreated one level up.

**Verdict: support-with-changes.**

**Flip condition.** Before P4's FALSIFIED/CONFIRMED verdict is trusted
at r=156 or r=312, compute a predicted-ripple-period band at each new r
using the SAME Fresnel-number-forcing argument this proposal already
invokes for P3's shape discriminator (e.g. period ∝ `1/√N_F(r)` or an
equivalent edge-diffraction scaling), and confirm `DENSE_PITCH` clears
that predicted period by the same sub-Nyquist margin exp-104 established
at r=78 (or scale `DENSE_PITCH(r)` down, e.g. `∝1/κ`, rather than holding
it at 2 cells absolute). Absent that check, a FALSIFIED P4 at the new
scales is not distinguishable from a repeat of exp-103's own original
aliasing bug.

---

**Additional verified finding (not part of the constrained sections
above, offered per this seat's own numeric-verification duty).** §5's
Idealizations states the r-family's `z/z_R` span as `[0.0026,0.041]`,
"giving 0.0253/0.0063/0.0016 at r=78/156/312," computed from the
proposal's own stated formula `z_over_zr(r)=77·20/r²`. Independently
re-executed that exact formula (`D_eff=77`, `λ_cells=20`):

```
r=78:  77*20/78**2  = 0.25312...
r=156: 77*20/156**2 = 0.06328...
r=312: 77*20/312**2 = 0.01582...
```

These are the correct values, and they are **~10× larger** than what
§5's prose states (0.0253/0.0063/0.0016) — a systematic decimal-place
error, not scatter. Two consequences: (1) the Appendix's own "no number
here is a fresh FDTD measurement... printed-asserted" discipline this
document claims for itself does not actually cover this sentence — the
Appendix script computes `geom(r)` and the thermal sidecar, but never
prints `z_over_zr(r)`, so this particular figure was hand-typed, the
exact R4-class failure mode this program has a standing rule against.
(2) The qualitative claim built on it — "narrower and shallower than
T8's own original 0.0031–0.049 span" — is backwards once corrected: the
true r=78 value (0.253) is **more than 5× past T8's own maximum**
(0.049), not narrower/shallower than T8's whole span. This changes how
near-field this bridge's r=78 leg actually is, which bears directly on
how much weight P3b's own T13/T14 cross-channel framing ("the near-field
shadow continuing to deepen toward a genuine floor as the object grows")
should be given — a materially different physical regime than the one
§5 describes. Recommend this be corrected and re-verified by an added
Appendix print statement (not by hand) before Phase 3 freeze.
