#!/usr/bin/env python3
r"""LangGraph adapter for the Consequential Reachability Benchmark kit tools.

The smallest real adapter: LangGraph's own StateGraph machinery (state,
nodes, conditional edges, compile/invoke — per the official Graph API
docs at docs.langchain.com/oss/python/langgraph/use-graph-api) drives
the Examiner Kit's two CLI tools as graph nodes:

    START -> validate_case --(exit 0)--> run_case -> report -> END
                          \--(exit != 0)-> report -> END

The adapter does NOT reimplement any kit logic. validate_case.py stays
the gate and run_case.py stays the runner; the graph only sequences
them, carries their outputs in state, routes on the validator's exit
code, and renders a verdict against CR-02's frozen expected outcomes.

Usage:
  langgraph_adapter.py [--case PATH] [--schema PATH]
                       [--kit-scripts DIR] [--out PATH]

Defaults point at the Consequence Boundary Audit skill package's
references/ copies of CR-02 and the frozen schema, at their canonical
pins:
  CR-02-candidate.json  sha256 112b0d4888b9d60343627dc427fe34b54b223a927efbb6b8eae25f379e19430e
  CASE_SCHEMA_DRAFT.json sha256 b0b0c9a37b93305dfe5433e47c89200aaf649de369ad346f90814e21e42fc44c

Exit 0 = adapter verdict PASS (validator exit 0, runner exit 0, all
computed outcomes match, and the parsed outcomes equal the frozen
CR-02 expectation set). Exit 1 = verdict FAIL. Exit 2 = the graph
itself could not run.
"""

import argparse
import hashlib
import json
import operator
import re
import subprocess
import sys
import time
from pathlib import Path
from typing import Annotated, TypedDict

from langgraph.graph import END, START, StateGraph

PKG = (Path.home() / "workspace/goals/verifiable-one-mind-continuity-across-surfaces"
       / "hidden_files/agent-first-distribution/skill-build/consequence-boundary-audit")
DEFAULT_CASE = PKG / "references" / "CR-02-candidate.json"
DEFAULT_SCHEMA = PKG / "references" / "CASE_SCHEMA_DRAFT.json"
DEFAULT_SCRIPTS = PKG / "scripts"

# CR-02's frozen expectation set, from the skill exercise of record
# (build record section 3: via-C / via-B / direct-A REFUSE, unrelated
# ALLOW; revocation delta = exactly the three reliance actions) and
# the case file's own expected_* fields.
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
            try:
                delta = [x.strip().strip("'\"") for x in d.group(1).strip("[]").split(",") if x.strip()]
            except Exception:
                delta = None
    return outcomes, delta


def outcomes_digest(outcomes, delta):
    canon = json.dumps(
        {"outcomes": {k: list(v) for k, v in sorted(outcomes.items())},
         "revocation_delta": sorted(delta or [])},
        sort_keys=True, separators=(",", ":"))
    return "sha256:" + hashlib.sha256(canon.encode("utf-8")).hexdigest()


class AdapterState(TypedDict):
    case_path: str
    schema_path: str
    kit_scripts: str
    steps: Annotated[list, operator.add]
    validate_exit: int
    validate_output: str
    run_exit: int
    run_output: str
    outcomes: dict
    revocation_delta: list
    outcomes_digest: str
    verdict: str


def _run_tool(state, script, extra_args):
    cmd = [sys.executable, str(Path(state["kit_scripts"]) / script)] + extra_args
    proc = subprocess.run(cmd, capture_output=True, text=True)
    return proc.returncode, proc.stdout + proc.stderr


def validate_node(state: AdapterState):
    rc, out = _run_tool(state, "validate_case.py",
                        [state["case_path"], state["schema_path"]])
    return {"steps": ["validate_case"], "validate_exit": rc, "validate_output": out}


def route_after_validate(state: AdapterState):
    return "run_case" if state["validate_exit"] == 0 else "report"


def run_node(state: AdapterState):
    rc, out = _run_tool(state, "run_case.py",
                        [state["case_path"], state["schema_path"]])
    outcomes, delta = parse_run_output(out)
    return {"steps": ["run_case"], "run_exit": rc, "run_output": out,
            "outcomes": outcomes, "revocation_delta": delta or [],
            "outcomes_digest": outcomes_digest(outcomes, delta)}


def report_node(state: AdapterState):
    ok = (
        state.get("validate_exit") == 0
        and state.get("run_exit") == 0
        and "ALL COMPUTED OUTCOMES MATCH" in state.get("run_output", "")
        and state.get("outcomes") == EXPECTED_OUTCOMES
        and sorted(state.get("revocation_delta") or []) == EXPECTED_DELTA
    )
    return {"steps": ["report"], "verdict": "PASS" if ok else "FAIL"}


def build_graph():
    graph = StateGraph(AdapterState)
    graph.add_node("validate_case", validate_node)
    graph.add_node("run_case", run_node)
    graph.add_node("report", report_node)
    graph.add_edge(START, "validate_case")
    graph.add_conditional_edges("validate_case", route_after_validate,
                                {"run_case": "run_case", "report": "report"})
    graph.add_edge("run_case", "report")
    graph.add_edge("report", END)
    return graph.compile()


def main(argv):
    ap = argparse.ArgumentParser(description="LangGraph adapter driving the benchmark kit tools over CR-02")
    ap.add_argument("--case", default=str(DEFAULT_CASE))
    ap.add_argument("--schema", default=str(DEFAULT_SCHEMA))
    ap.add_argument("--kit-scripts", default=str(DEFAULT_SCRIPTS))
    ap.add_argument("--out", default=None)
    args = ap.parse_args(argv)

    app = build_graph()
    started = time.perf_counter()
    final = app.invoke({
        "case_path": args.case, "schema_path": args.schema,
        "kit_scripts": args.kit_scripts, "steps": [],
        "validate_exit": -1, "validate_output": "", "run_exit": -1,
        "run_output": "", "outcomes": {}, "revocation_delta": [],
        "outcomes_digest": "", "verdict": "NOT RUN",
    })
    wall_s = round(time.perf_counter() - started, 4)

    summary = {
        "harness": "langgraph_adapter",
        "framework": "langgraph (StateGraph, Graph API)",
        "case": Path(args.case).name,
        "steps_executed": final["steps"],
        "validate_exit": final["validate_exit"],
        "validate_valid_line": "VALID" in final["validate_output"],
        "run_exit": final["run_exit"],
        "run_all_match": "ALL COMPUTED OUTCOMES MATCH" in final["run_output"],
        "outcomes": {k: list(v) for k, v in sorted(final["outcomes"].items())},
        "revocation_delta": sorted(final["revocation_delta"]),
        "outcomes_digest": final["outcomes_digest"],
        "run_stdout_sha256": "sha256:" + hashlib.sha256(
            final["run_output"].encode("utf-8")).hexdigest(),
        "wall_seconds": wall_s,
        "verdict": final["verdict"],
    }
    print(json.dumps(summary, indent=2, sort_keys=True))
    if args.out:
        Path(args.out).write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n",
                                  encoding="utf-8")
    return 0 if final["verdict"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
