# VISION SCIENCE — Phase 2 Critique of exp-064 Phase 1 Proposal

*Fresh sub-agent, blind to the other seats' current-cycle critiques.
Charter: human perceptual limits — contrast thresholds, luminance edge
detection, spectral sensitivity, adaptation, temporal sensitivity,
saccadic/attentional blindness. Central question: what would make a human
eye FAIL to register something physically present? Standing duty this
cycle: registry-propagation/caveat-collision check on this cycle's own
new dict-literal edits and registry entries, per this seat's own
established pattern (T3/Iteration 17 dropped-NETD-disclaimer catch;
Iteration 38/39/40 registry-scoping catches).*

## 1. Steel-man (≤150 words)

The allow-list shape is the physically correct enforcement choice, and §7
argues it honestly from this program's own record rather than borrowing
another seat's ground: `σ_ext` can differ from a real geometric
cross-section for a general wave-optics reason (T9), not a fact special
to `w_on` or `τ/α`, so a deny-list of today's two known-bad lengths would
leave the guard blind to the next one — exactly how T23 itself survived
three cycles of prose-only disclosure. QP-3's falsification condition
correctly pre-forecloses the one shortcut this cycle itself could take
(tagging the witness-scale call `bench_construction` to make it pass).
And the new registry entry's `required_sites` (NOTES.md + phase4_
results.md) explicitly avoids the single-file narrow-scope shape that
fired Checkpoint criterion 4 on the sibling `exp063-thermo-disposition-
netd-disclaimer` entry one cycle ago — a specific, correctly-applied
lesson, not a generic gesture toward "we widened it."

## 2. Sharpest attack (≤150 words)

Stage 24's regression-identity gate (group 2) checks only that returned
*numbers* match bit-for-bit before/after the edit. Both guarded dicts
(`mixed_length_scale_regime`, `front_surface_conduction_correction`)
already carry a hand-written `"netd_disclaimer"` string — this program's
oldest continuously-enforced caveat, which has already gone missing once
from a per-point return (Iteration 17, T3) and once from a results table
(Iteration 40, mandatory fix 2). Implementing §3/§4 requires hand-editing
those exact dict literals to insert two new keys; gate 3's "diagnostic-
path identity" reads back only `length_provenance`/`diagnostic_only`, not
`netd_disclaimer`, `model_note`, or `mass_fill_fraction_assumption`. No
proposed gate would notice if `netd_disclaimer`'s text were dropped,
truncated, or silently reworded during that edit — the exact caveat-
propagation failure shape this seat's charter exists to catch, on the
exact lines this cycle's own diff will touch, with zero machine check
proposed against it.

## 3. Verdict

**Support-with-changes.**

## 4. Registry-scoping and key-collision check (task-directed, this
seat's standing duty)

**Key collision: none at the Python-dict level, but the gate suite has a
blind spot the collision question exposes.** `length_provenance`/
`diagnostic_only` are new key names, distinct from `netd_disclaimer` —
no literal-collision risk from the *names* chosen. The real risk is
ordering/completeness of the *edit*, not the names: §3 says the return
dicts "gain" the two new keys but never shows the literal diff, and §4's
four gates verify (1) refusal behavior, (2) numeric equality, (3) the two
new keys' own readback, (4) `inspect.signature` shape — none verify that
the *other* string-valued keys already in those dicts (`netd_disclaimer`
above all, but also `model_note`, `mass_fill_fraction_assumption`,
`material_provenance`, `idealization_note`) survive the edit byte-for-
byte. This is precisely the gap this program's history says matters:
caveat strings get silently dropped exactly when a dict literal is
touched for an unrelated reason, not when someone deliberately deletes
them.

**Registry `required_sites` scoping: correctly avoids the narrow shape
named in the task brief.** §3's `exp064-length-provenance-disclosure`
entry specifies `required_sites` = this cycle's `NOTES.md` +
`phase4_results.md` — not NOTES.md alone, which is the exact shape that
fired Checkpoint criterion 4 at Iteration 40 on both
`exp063-thermo-disposition-netd-disclaimer` and the sibling
`numeric_lint` entry. On this specific, task-flagged failure mode, the
proposal is clean; no Checkpoint-4-relevant risk is visible in the §3
spec as written.

**Residual, not disqualifying: `candidate_globs` is left unspecified.**
§3's table never mentions `candidate_globs` for the new entry, so it
falls back to `DEFAULT_CANDIDATE_GLOBS` — already widened program-wide at
Iteration 39/40 to a generic `experiments/*/phase*.md` pattern, which
does reach this cycle's own `phase2_critique_*`/`phase3_synthesis`/
`phase5_review_*`/`phase5_redteam_audit.md` files for WARN-level
discovery. That is adequate given `candidate_globs`/`trigger_terms` never
gate the exit code (`lab/caveat_lint.py`'s own contract, lines 65-71) —
but it means the entry is silently *inheriting* correctness from a
default the proposal never states or commits to checking stays wide.
Recommend §3 say so explicitly (one sentence) rather than leaving it
implicit, so a future reader auditing this entry does not have to
re-derive that omission-equals-safe-default reasoning from
`caveat_lint.py`'s own source.

## 5. Parameter change that would flip this verdict to full support

Add a fifth stage-24 gate — **caveat-string identity** — asserting that,
for both `mixed_length_scale_regime` and `front_surface_conduction_
correction`, every key present in the function's PRE-existing return dict
(read from the current committed source, e.g. via `ast` inspection or a
frozen golden-dict fixture) is present in the POST-guard return dict with
an identical string value, for at least one licensed (`bench_
construction`) call. This converts "the two new keys read back correctly"
(already gate 3) into "nothing already there was silently lost or
altered" — closing the one class of regression this program has already
paid for twice and that no other proposed gate currently checks.
