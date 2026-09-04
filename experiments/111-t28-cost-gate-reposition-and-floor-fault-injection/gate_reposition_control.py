"""exp-111 -- Panel Iteration 88: control for chunk_runner.py's own
upstream cost-gate reposition (Reconciled Iteration-88 Tier-1 item 2).
Zero Sim.run() calls anywhere in this file -- monkeypatches
chunk_runner.build_sim with a call-counting stub that raises a sentinel
StubReached exception the moment the real engine would be touched, never
constructs a real lab.Sim or calls .run() anywhere.

Mandatory-fix 1 (EM, phase2_redteam_audit.md Sec 5 -- the cycle's single
highest-priority fix, R28's own founding-instance shape one layer deeper if
left unbound): this control binds to the REAL, imported `chunk_runner`
module -- patches its actual `build_sim` attribute (not a local copy) and
calls its actual, unmodified `step_once()` function. Two explicit identity
assertions confirm this before any case is trusted:
  assert chunk_runner.build_sim is STUB   (after patching)
  assert chunk_runner.step_once is ORIGINAL_STEP_ONCE   (never patched)

Mandatory-fix 2 (EM): a fifth case, "r=312 already done, r=156 logs
absent/stale" -- the state the fixed guard-ordering (gate check AFTER the
existing done-file early-return) must handle without re-evaluating the
cost gate at all.

Uses a throwaway control SCRATCH directory (chunk_runner.SCRATCH is
monkeypatched too), never exp-110's own real SCRATCH/pickles.
"""
import json
import os
import pickle
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "experiments", "110-t28-item-i-local-norm-and-controls"))

import chunk_runner  # noqa: E402  -- the REAL, imported module (mandatory-fix 1)

CONTROL_SCRATCH = os.path.join(HERE, "_gate_reposition_control_scratch")

ORIGINAL_BUILD_SIM = chunk_runner.build_sim
ORIGINAL_STEP_ONCE = chunk_runner.step_once
ORIGINAL_SCRATCH = chunk_runner.SCRATCH


class StubReached(Exception):
    pass


class CallCountingStub:
    def __init__(self):
        self.count = 0

    def __call__(self, g, which):
        self.count += 1
        raise StubReached(f"build_sim reached for which={which}")


def fresh_scratch():
    if os.path.exists(CONTROL_SCRATCH):
        shutil.rmtree(CONTROL_SCRATCH)
    os.makedirs(CONTROL_SCRATCH, exist_ok=True)
    chunk_runner.SCRATCH = CONTROL_SCRATCH


def write_done_marker(r, which):
    _, done_path = chunk_runner.path_for(r, which)
    with open(done_path, "wb") as f:
        pickle.dump({"stub": True}, f)


def write_walltime_log(r, which, seconds):
    path = chunk_runner.walltime_log_path(r, which)
    with open(path, "w") as f:
        json.dump([seconds], f)


def run_case(name, setup_fn):
    fresh_scratch()
    setup_fn()

    stub = CallCountingStub()
    chunk_runner.build_sim = stub
    assert chunk_runner.build_sim is stub, "identity check: patch did not land on the real module attribute"
    assert chunk_runner.step_once is ORIGINAL_STEP_ONCE, "identity check: step_once must remain the real, unmodified function"

    outcome = dict(case=name, build_sim_calls=0, exception_type=None, exception_msg=None, returned=None)
    try:
        ret = chunk_runner.step_once(312, "empty")
        outcome["returned"] = ret
    except StubReached as e:
        outcome["exception_type"] = "StubReached"
        outcome["exception_msg"] = str(e)
    except RuntimeError as e:
        outcome["exception_type"] = "RuntimeError"
        outcome["exception_msg"] = str(e)
    finally:
        outcome["build_sim_calls"] = stub.count
        chunk_runner.build_sim = ORIGINAL_BUILD_SIM
    return outcome


def case_favorable():
    def setup():
        for which, wall in (("empty", 250.6266098022461), ("hollow", 250.08318996429443),
                             ("peccored", 251.51349687576294)):
            write_done_marker(156, which)
            write_walltime_log(156, which, wall)
    out = run_case("favorable", setup)
    predicted_exception = "StubReached"
    predicted_calls = 1
    gate_path = os.path.join(CONTROL_SCRATCH, "r312_costgate.json")
    gate_written = os.path.exists(gate_path)
    gate_proceed = None
    if gate_written:
        with open(gate_path) as f:
            gate_proceed = json.load(f)["proceed_to_r312"]
    out.update(predicted_exception=predicted_exception, predicted_calls=predicted_calls,
               gate_written_before_stub=gate_written, gate_proceed_to_r312=gate_proceed,
               pass_=bool(out["exception_type"] == predicted_exception
                          and out["build_sim_calls"] == predicted_calls
                          and gate_written and gate_proceed is True))
    return out


def case_unfavorable_budget():
    def setup():
        for which, wall in (("empty", 10000.0), ("hollow", 250.08318996429443),
                             ("peccored", 251.51349687576294)):
            write_done_marker(156, which)
            write_walltime_log(156, which, wall)
    out = run_case("unfavorable_budget", setup)
    out.update(pass_=bool(out["exception_type"] == "RuntimeError"
                          and "REFUSED" in (out["exception_msg"] or "")
                          and out["build_sim_calls"] == 0))
    return out


def case_unfavorable_precondition():
    def setup():
        pass  # zero r=156 done markers
    out = run_case("unfavorable_precondition", setup)
    out.update(pass_=bool(out["exception_type"] == "RuntimeError"
                          and "not complete" in (out["exception_msg"] or "")
                          and out["build_sim_calls"] == 0))
    return out


def case_scope_precision_r156():
    """The new guard must only fire for r==312 -- step_once(156, "empty")
    must reach build_sim unconditionally, any r=156 state."""
    fresh_scratch()
    stub = CallCountingStub()
    chunk_runner.build_sim = stub
    outcome = dict(case="scope_precision_r156", build_sim_calls=0, exception_type=None)
    try:
        chunk_runner.step_once(156, "empty")
    except StubReached as e:
        outcome["exception_type"] = "StubReached"
        outcome["exception_msg"] = str(e)
    finally:
        outcome["build_sim_calls"] = stub.count
        chunk_runner.build_sim = ORIGINAL_BUILD_SIM
    outcome.update(pass_=bool(outcome["exception_type"] == "StubReached" and outcome["build_sim_calls"] == 1))
    return outcome


def case_already_done_312_stale_156():
    """Mandatory-fix 2 (EM): r=312 already DONE, r=156 logs absent/stale.
    The fixed guard ordering (done-check BEFORE the gate call) must return
    True immediately WITHOUT ever evaluating check_cost_gate_for_312() or
    touching build_sim -- this state is reachable on any resumed/
    status-check invocation and was untested by the original four cases."""
    def setup():
        write_done_marker(312, "empty")
        # r=156 done markers/logs deliberately absent (stale/missing session)
    out = run_case("already_done_312_stale_156", setup)
    gate_path = os.path.join(CONTROL_SCRATCH, "r312_costgate.json")
    gate_written = os.path.exists(gate_path)
    out.update(gate_evaluated=gate_written,
               pass_=bool(out["returned"] is True and out["exception_type"] is None
                          and out["build_sim_calls"] == 0 and not gate_written))
    return out


if __name__ == "__main__":
    cases = [case_favorable(), case_unfavorable_budget(), case_unfavorable_precondition(),
             case_scope_precision_r156(), case_already_done_312_stale_156()]
    for c in cases:
        print(json.dumps(c, default=str))

    chunk_runner.SCRATCH = ORIGINAL_SCRATCH
    if os.path.exists(CONTROL_SCRATCH):
        shutil.rmtree(CONTROL_SCRATCH)

    out_path = os.path.join(HERE, "gate_reposition_control_output.json")
    with open(out_path, "w") as f:
        json.dump(cases, f, indent=2, default=str)
    print(f"Written: {out_path}")

    all_pass = all(c["pass_"] for c in cases)
    print(f"\nALL CASES PASS: {all_pass}")
    assert all_pass, "gate_reposition_control: at least one case failed"
