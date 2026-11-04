#!/usr/bin/env python3
"""Non-ARC self-stood baseline harness for the framework comparison.

No framework, no ARC machinery: a plain script that calls the same two
kit tools in the same order with the same arguments the LangGraph
adapter uses (validate_case.py as the gate, then run_case.py), parses
the runner's output the same way, and checks the same frozen CR-02
expectation set. It exists so the adapter's result can be read beside
a direct-scripted result at face value — same tools, same case, same
schema, same verdict rule; the only difference is the orchestration
layer (a framework graph vs sequential script calls).

Usage:
  baseline_harness.py [--case PATH] [--schema PATH]
                      [--kit-scripts DIR] [--out PATH]

Exit 0 = verdict PASS under the same rule as the adapter; 1 = FAIL.
"""

import argparse
import hashlib
import json
import re
import subprocess
import sys
import time
from pathlib import Path

PKG = (Path.home() / "workspace/goals/verifiable-one-mind-continuity-across-surfaces"
       / "hidden_files/agent-first-distribution/skill-build/consequence-boundary-audit")
DEFAULT_CASE = PKG / "references" / "CR-02-candidate.json"
DEFAULT_SCHEMA = PKG / "references" / "CASE_SCHEMA_DRAFT.json"
DEFAULT_SCRIPTS = PKG / "scripts"

EXPECTED_OUTCOMES = {
    "CR02-via-C": ("REFUSE", "ABSENT", "revoked_ancestor_A"),
    "CR02-via-B": ("REFUSE", "ABSENT", "revoked_ancestor_A"),
    "CR02-direct-A": ("REFUSE", "ABSENT", "direct_revocation_A"),
    "CR02-unrelated": ("ALLOW", "PRESENT", "authorized_unrelated"),
}
EXPECTED_DELTA = ["CR02-direct-A", "CR02-via-B", "CR02-via-C"]

MATCH_RE = re.compile(
    r"^(MATCH|MISMATCH) (\S+): computed decision=(\S+) effect=(\S+) reason=(\S+)")
DELTA_RE = re.compile(r"decisions changed by revocation: (\[.*\])")


def parse_run_output(text):
    outcomes = {}
    delta = None
    for line in text.splitlines():
        m = MATCH_RE.match(line.strip())
        if m:
            outcomes[m.group(2)] = (m.group(3), m.group(4), m.group(5))
        d = DELTA_RE.search(line)
        if d:
            delta = [x.strip().strip("'\"") for x in d.group(1).strip("[]").split(",") if x.strip()]
    return outcomes, delta


def outcomes_digest(outcomes, delta):
    canon = json.dumps(
        {"outcomes": {k: list(v) for k, v in sorted(outcomes.items())},
         "revocation_delta": sorted(delta or [])},
        sort_keys=True, separators=(",", ":"))
    return "sha256:" + hashlib.sha256(canon.encode("utf-8")).hexdigest()


def main(argv):
    ap = argparse.ArgumentParser(description="Direct scripted baseline over the benchmark kit tools")
    ap.add_argument("--case", default=str(DEFAULT_CASE))
    ap.add_argument("--schema", default=str(DEFAULT_SCHEMA))
    ap.add_argument("--kit-scripts", default=str(DEFAULT_SCRIPTS))
    ap.add_argument("--out", default=None)
    args = ap.parse_args(argv)

    scripts = Path(args.kit_scripts)
    steps = []
    started = time.perf_counter()

    proc = subprocess.run(
        [sys.executable, str(scripts / "validate_case.py"), args.case, args.schema],
        capture_output=True, text=True)
    steps.append("validate_case")
    validate_exit, validate_output = proc.returncode, proc.stdout + proc.stderr

    run_exit, run_output, outcomes, delta = -1, "", {}, []
    if validate_exit == 0:
        proc = subprocess.run(
            [sys.executable, str(scripts / "run_case.py"), args.case, args.schema],
            capture_output=True, text=True)
        steps.append("run_case")
        run_exit, run_output = proc.returncode, proc.stdout + proc.stderr
        outcomes, delta = parse_run_output(run_output)
    steps.append("report")
    wall_s = round(time.perf_counter() - started, 4)

    ok = (
        validate_exit == 0
        and run_exit == 0
        and "ALL COMPUTED OUTCOMES MATCH" in run_output
        and outcomes == EXPECTED_OUTCOMES
        and sorted(delta) == EXPECTED_DELTA
    )
    summary = {
        "harness": "baseline_direct_script",
        "framework": "none (plain sequential subprocess calls)",
        "case": Path(args.case).name,
        "steps_executed": steps,
        "validate_exit": validate_exit,
        "validate_valid_line": "VALID" in validate_output,
        "run_exit": run_exit,
        "run_all_match": "ALL COMPUTED OUTCOMES MATCH" in run_output,
        "outcomes": {k: list(v) for k, v in sorted(outcomes.items())},
        "revocation_delta": sorted(delta),
        "outcomes_digest": outcomes_digest(outcomes, delta),
        "run_stdout_sha256": "sha256:" + hashlib.sha256(
            run_output.encode("utf-8")).hexdigest(),
        "wall_seconds": wall_s,
        "verdict": "PASS" if ok else "FAIL",
    }
    print(json.dumps(summary, indent=2, sort_keys=True))
    if args.out:
        Path(args.out).write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n",
                                  encoding="utf-8")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
