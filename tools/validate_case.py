#!/usr/bin/env python3
"""Graph + temporal validator for Consequential Reachability Benchmark cases.

Layer 1 (shape): the case must validate against CASE_SCHEMA_DRAFT.json
(JSON Schema Draft 2020-12).

Layer 2 (graph): the case's first-class `dependency_graph` must be
well-formed and must agree with every other place the case states
dependencies:
  - node ids unique; every edge endpoint is a declared node; no
    self-loops; the graph is acyclic;
  - every action id is a graph node of kind "action", and the action's
    typed `depends_on` list equals the graph edges leaving that node;
  - every request node is established by exactly one setup event, whose
    declared `depends_on` equals the graph edges leaving that node, and
    every dependency of an established request was itself established at
    a strictly earlier setup step.

Layer 3 (temporal): revocation events and action positions must be
consistent with the setup timeline:
  - each `revocation_events` entry matches a setup revocation at the
    same step, and the revoked node was established earlier;
  - each action's `at_step` position is inside the timeline, and every
    request in the action's transitive ancestry was established at a
    step strictly before that position (an action cannot be evaluated
    against a graph state its position makes impossible);
  - each setup `check_contested_state` expectation equals the contested
    set computed from the graph at that point in the timeline.

Usage: validate_case.py <case.json> [schema.json]
Exit 0 = valid; exit 1 = invalid (FAIL lines on stdout); exit 2 = usage/IO.
Stdlib + `jsonschema` (Draft 2020-12) only.
"""

import json
import sys
from pathlib import Path

DEFAULT_SCHEMA = Path(__file__).resolve().parent.parent / "CASE_SCHEMA_DRAFT.json"


def load_json(path):
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def edge_map(graph):
    """node id -> sorted list of direct dependency ids (edge targets)."""
    out = {}
    for edge in graph.get("edges", []):
        out.setdefault(edge["from"], []).append(edge["to"])
    for key in out:
        out[key] = sorted(out[key])
    return out


def transitive_ancestry(graph, start):
    """All nodes reachable from `start` following depends_on edges."""
    edges = edge_map(graph)
    seen = set()
    stack = list(edges.get(start, []))
    while stack:
        node = stack.pop()
        if node in seen:
            continue
        seen.add(node)
        stack.extend(edges.get(node, []))
    return seen


def validate(case, schema):
    """Return a list of (check_name, ok, detail) triples."""
    results = []

    def record(name, ok, detail=""):
        results.append((name, ok, detail))

    # ---- Layer 1: JSON Schema shape -------------------------------------
    try:
        import jsonschema
    except ImportError:
        record("schema", False, "jsonschema package unavailable")
        return results
    validator_cls = jsonschema.Draft202012Validator
    try:
        validator_cls.check_schema(schema)
    except Exception as exc:  # schema itself is broken
        record("schema", False, f"schema does not check: {exc}")
        return results
    errors = sorted(validator_cls(schema).iter_errors(case), key=lambda e: list(e.path))
    if errors:
        detail = "; ".join(
            f"{'/'.join(str(p) for p in e.path) or '<root>'}: {e.message}" for e in errors[:6]
        )
        record("schema", False, detail)
        return results
    record("schema", True, "case validates against CASE_SCHEMA_DRAFT.json")

    graph = case["dependency_graph"]
    nodes = graph.get("nodes", [])
    node_ids = [n["id"] for n in nodes]
    node_kind = {n["id"]: n.get("kind") for n in nodes}
    edges = edge_map(graph)

    # ---- Layer 2: graph well-formedness ---------------------------------
    dupes = sorted({i for i in node_ids if node_ids.count(i) > 1})
    record("graph.nodes_unique", not dupes,
           "duplicate node ids: " + ", ".join(dupes) if dupes else "node ids unique")

    dangling = sorted({
        ref
        for edge in graph.get("edges", [])
        for ref in (edge["from"], edge["to"])
        if ref not in node_kind
    })
    record("graph.edges_resolve", not dangling,
           "edge endpoints not declared as nodes: " + ", ".join(dangling)
           if dangling else "every edge endpoint is a declared node")

    loops = sorted({e["from"] for e in graph.get("edges", []) if e["from"] == e["to"]})
    record("graph.no_self_loops", not loops,
           "self-loops on: " + ", ".join(loops) if loops else "no self-loops")

    # acyclicity via DFS colours
    WHITE, GREY, BLACK = 0, 1, 2
    colour = {i: WHITE for i in node_ids}
    cycle = []

    def dfs(u, trail):
        colour[u] = GREY
        for v in edges.get(u, []):
            if v not in colour:
                continue
            if colour[v] == GREY:
                cycle.append(" -> ".join(trail + [u, v]))
                return True
            if colour[v] == WHITE and dfs(v, trail + [u]):
                return True
        colour[u] = BLACK
        return False

    has_cycle = any(colour[i] == WHITE and dfs(i, []) for i in node_ids)
    record("graph.acyclic", not has_cycle,
           "dependency cycle: " + cycle[0] if cycle else "graph is acyclic")

    # ---- Layer 2: actions bound to the graph ----------------------------
    actions = case.get("actions", [])
    action_ids = [a["id"] for a in actions]
    missing_nodes = [i for i in action_ids if i not in node_kind]
    wrong_kind = [i for i in action_ids
                  if i in node_kind and node_kind[i] != "action"]
    record("graph.actions_are_nodes", not missing_nodes and not wrong_kind,
           "; ".join(filter(None, [
               "actions missing from graph nodes: " + ", ".join(missing_nodes) if missing_nodes else "",
               "actions whose graph node kind is not 'action': " + ", ".join(wrong_kind) if wrong_kind else "",
           ])) or "every action is a graph node of kind 'action'")

    mismatched = []
    unknown_deps = []
    for action in actions:
        declared = sorted(action.get("depends_on", []))
        graphed = edges.get(action["id"], [])
        for dep in declared:
            if dep not in node_kind:
                unknown_deps.append(f"{action['id']} -> {dep}")
        if declared != graphed:
            mismatched.append(
                f"{action['id']}: action.depends_on={declared} != graph edges={graphed}")
    record("graph.action_edges_match", not mismatched and not unknown_deps,
           "; ".join(filter(None, [
               "depends_on references not declared as nodes: " + ", ".join(unknown_deps) if unknown_deps else "",
               " | ".join(mismatched) if mismatched else "",
           ])) or "each action's depends_on equals its graph edges")

    # ---- Layer 2/3: setup establishes the request graph ------------------
    setup = case.get("setup", [])
    steps = [s["step"] for s in setup]
    record("temporal.setup_steps_ordered",
           steps == sorted(steps) and len(set(steps)) == len(steps),
           f"setup steps {steps} are strictly increasing"
           if steps == sorted(steps) and len(set(steps)) == len(steps)
           else f"setup steps {steps} are not strictly increasing")

    established = {}  # request id -> step established
    establishment_problems = []
    setup_edge_problems = []
    for entry in setup:
        data = entry.get("data", {}) or {}
        req = data.get("request_id")
        event = entry.get("event", "")
        if req is None or "revoke" in event:
            continue
        if req not in node_kind:
            establishment_problems.append(f"step {entry['step']}: establishes undeclared node {req}")
            continue
        if req in established:
            establishment_problems.append(f"{req} established twice (steps {established[req]} and {entry['step']})")
        declared = sorted(data.get("depends_on", []))
        graphed = edges.get(req, [])
        if declared != graphed:
            setup_edge_problems.append(
                f"step {entry['step']} ({req}): setup depends_on={declared} != graph edges={graphed}")
        for dep in declared:
            if dep not in established:
                establishment_problems.append(
                    f"step {entry['step']}: {req} depends on {dep}, not established at an earlier step")
        established[req] = entry["step"]
    request_nodes = sorted(i for i, k in node_kind.items() if k == "request")
    unestablished = [i for i in request_nodes if i not in established]
    if unestablished:
        establishment_problems.append("request nodes never established by setup: " + ", ".join(unestablished))
    record("graph.setup_establishes_requests", not establishment_problems,
           "; ".join(establishment_problems)
           if establishment_problems else "every request node established exactly once, dependencies earlier")
    record("graph.setup_edges_match", not setup_edge_problems,
           "; ".join(setup_edge_problems)
           if setup_edge_problems else "setup depends_on declarations equal the graph edges")

    # ---- Layer 3: revocation events against the timeline -----------------
    setup_by_step = {s["step"]: s for s in setup}
    revocation_problems = []
    for rev in case.get("revocation_events", []):
        target = rev["revokes"]
        step = rev["step"]
        entry = setup_by_step.get(step)
        if target not in node_kind:
            revocation_problems.append(f"{rev['id']}: revokes undeclared node {target}")
            continue
        if target in established and established[target] >= step:
            revocation_problems.append(
                f"{rev['id']}: {target} established at step {established[target]}, not before revocation step {step}")
        if entry is None or "revoke" not in entry.get("event", "") \
                or (entry.get("data", {}) or {}).get("request_id") != target:
            revocation_problems.append(
                f"{rev['id']}: no matching setup revocation of {target} at step {step}")
    record("temporal.revocation_events_match_setup", not revocation_problems,
           "; ".join(revocation_problems)
           if revocation_problems else "each revocation event matches the setup timeline")

    # ---- Layer 3: action positions ---------------------------------------
    max_position = (max(steps) + 1) if steps else 0
    position_problems = []
    for action in actions:
        pos = action.get("at_step", max_position)
        if not (0 <= pos <= max_position):
            position_problems.append(f"{action['id']}: at_step {pos} outside timeline 0..{max_position}")
            continue
        for dep in transitive_ancestry(graph, action["id"]):
            if dep in established and established[dep] >= pos:
                position_problems.append(
                    f"{action['id']} at position {pos} depends on {dep}, "
                    f"established at step {established[dep]} — not yet in the graph at that position")
            elif dep in node_kind and node_kind[dep] == "action":
                other = next((a for a in actions if a["id"] == dep), None)
                if other is not None:
                    other_pos = other.get("at_step", max_position)
                    if other_pos >= pos:
                        position_problems.append(
                            f"{action['id']} at position {pos} depends on action {dep} positioned at {other_pos}")
    record("temporal.action_positions", not position_problems,
           "; ".join(position_problems)
           if position_problems else "every action is positioned after its ancestry is established")

    # ---- Layer 3: contested-state cross-check -----------------------------
    revocations = [(r["step"], r["revokes"]) for r in case.get("revocation_events", [])]
    contested_problems = []
    for entry in setup:
        data = entry.get("data", {}) or {}
        if "expected_contested" not in data:
            continue
        step = entry["step"]
        revoked = {t for (s, t) in revocations if s <= step}
        computed = sorted(
            req for req, est_step in established.items()
            if est_step <= step and req not in revoked
            and transitive_ancestry(graph, req) & revoked
        )
        expected = sorted(data["expected_contested"])
        if computed != expected:
            contested_problems.append(
                f"step {step}: computed contested set {computed} != case expectation {expected}")
    record("temporal.contested_state_matches_graph", not contested_problems,
           "; ".join(contested_problems)
           if contested_problems else "contested-state expectations equal the graph computation at each check")

    return results


def main(argv):
    if len(argv) not in (2, 3):
        print("usage: validate_case.py <case.json> [schema.json]", file=sys.stderr)
        return 2
    case_path = Path(argv[1])
    schema_path = Path(argv[2]) if len(argv) == 3 else DEFAULT_SCHEMA
    try:
        case = load_json(case_path)
        schema = load_json(schema_path)
    except Exception as exc:
        print(f"FAIL load: {exc}")
        return 2
    results = validate(case, schema)
    ok_all = True
    for name, ok, detail in results:
        ok_all = ok_all and ok
        print(f"{'PASS' if ok else 'FAIL'} {name}" + (f": {detail}" if detail else ""))
    print(f"RESULT {'VALID' if ok_all else 'INVALID'} {case_path.name}")
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
