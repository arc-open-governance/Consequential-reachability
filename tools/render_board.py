#!/usr/bin/env python3
"""Render the Consequential Reachability Benchmark work board + visuals.

Reads `board-state.json` (beside this script's parent directory) — a
dated snapshot of the benchmark desk's engagement record — and renders:

  - WORK-BOARD.md                 the contributors board (names and
                                  work, arrival order, no ranking)
  - assets/cases-timeline.svg     case arrivals across the window
  - assets/window-progress.svg    collection-window progress bar
  - assets/relational-map.svg     contributors, cases, and the
                                  interactions between them

Every number on every surface comes from the one state file, so the
badge, the bar, the charts, and the board cannot disagree. Nothing
here fetches anything: the state file is written from the record by
hand at press time, and this script renders exactly what it says.

Usage: render_board.py [state.json]
Exit 0 = rendered; exit 2 = state unreadable or inconsistent.
Stdlib only.
"""

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_STATE = ROOT / "board-state.json"

GOLD = "#C9A227"
BLUE = "#4D9FFF"
BG = "#050505"
PANEL = "#101418"
INK = "#E8E8E8"
DIM = "#9AA4AE"

STATUS_COLORS = {
    "received": BLUE,
    "first-pass read": GOLD,
    "under examination": GOLD,
    "adjudicated": "#7EE787",
    # CR-01/CR-02 are the desk's worked examples: they carry computed
    # outcomes, not a queue status (the four statuses above govern
    # submitted cases).
    "worked example": GOLD,
}


def parse_ts(s):
    return datetime.fromisoformat(s)


def esc(s):
    return (
        str(s)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def window_fraction(state, at):
    w = state["window"]
    opens, closes = parse_ts(w["opens"]), parse_ts(w["closes"])
    if not (opens <= at <= closes):
        return 0.0 if at < opens else 1.0
    return (at - opens) / (closes - opens)


# ---------------------------------------------------------------- board

def render_board(state):
    gen = state["generated_at_label"]
    thr = state["thread"]
    cases = state["cases"]
    lines = []
    lines.append("# The Work Board — Consequential Reachability Benchmark")
    lines.append("")
    lines.append(
        f"**State as of {gen}**, generated from the benchmark desk's "
        f"engagement record (the {thr['platform']} invitation thread and "
        "the desk's ledger) by `tools/render_board.py` from "
        "`board-state.json`. The board is a snapshot: it changes by a "
        "new dated press, never silently."
    )
    lines.append("")
    lines.append(
        "Recognition on this board is a **contributors board**: "
        "contributors are named with the work they did, in arrival "
        "order. There are no ranks, no scores, and no ordering by "
        "merit. (Founder's decision, Nov 2, 2026.)"
    )
    lines.append("")
    for note in state.get("press", {}).get("head_notes", []):
        lines.append(note)
        lines.append("")
    lines.append(
        f"**The experiment's home:** the live thread on {thr['platform']} — "
        f"[{thr['title']}]({thr['url']}) (post `{thr['post_id']}`). "
        "Cases arrive there; this repository carries the record: the "
        "schema, the worked examples, the runner, and this board."
    )
    lines.append("")
    lines.append("## The window")
    lines.append("")
    w = state["window"]
    frac = window_fraction(state, parse_ts(state["generated_at_iso"]))
    gen_ts = parse_ts(state["generated_at_iso"])
    if gen_ts >= parse_ts(w["closes"]):
        status = (
            f"- At this snapshot the window is **closed** (it closed "
            f"{w['closes_label']}); collection for this window has ended."
        )
    else:
        status = (
            f"- At this snapshot the window stands **{frac * 100:.1f}% "
            "elapsed; collection still open**"
            f" (the window closes {w['closes_label']})."
        )
    counts = state.get("counts_line") or (
        f"- Cases in the collection: **{len(cases)}** "
        f"(CR-01–CR-{len(cases):02d})."
    )
    lines.append(f"- {w['label']}\n{status}\n{counts}")
    lines.append("")
    lines.append("## Cases")
    lines.append("")
    lines.append(
        "Statuses for submitted cases are the board's four, and only "
        "these: **received** · **first-pass read** · **under examination** "
        "· **adjudicated** (a case is adjudicated only on a signed record "
        "posted in the thread; no status changes without a recorded desk "
        "act). CR-01 and CR-02 are the desk's worked examples — they carry "
        "their computed outcomes, not a queue status. Every case carries "
        "its provenance: the chain a reader can walk back to the original "
        "submission."
    )
    lines.append("")
    for c in cases:
        p = c["provenance"]
        lines.append(f"### {c['id']} — {c['title']}")
        lines.append("")
        lines.append(f"- **Status:** {c['status']}")
        lines.append(f"- **Author:** {c['author']}")
        lines.append(f"- **What it is:** {c['summary']}")
        lines.append(f"- **Standing:** {c['standing']}")
        lines.append(f"- **Next:** {c['next']}")
        prov = (
            f"- **Provenance:** {p['platform']} · thread post "
            f"`{p['thread_post_id']}` · {p['source_label']} "
            f"`{p['source_id']}` · {p['timestamp_label']}"
        )
        if p.get("receipt_id"):
            prov += (
                f" · desk receipt `{p['receipt_id']}` · "
                f"{p['receipt_timestamp_label']}"
            )
        prov += f" · [the thread]({thr['url']})"
        lines.append(prov)
        lines.append("")
    lines.append("## Fixtures")
    lines.append("")
    lines.append(state.get("fixtures_statement") or (
        f"**Runnable fixtures: {state['fixtures_runnable']}.** No case "
        "in the collection has been turned into a runnable fixture "
        "yet. That is named open work below — the fixture lane is "
        "where a case becomes something an examiner can run."
    ))
    lines.append("")
    lines.append("## Contributors")
    lines.append("")
    lines.append("Named, with their work, in arrival order.")
    lines.append("")
    for person in state["contributors"]:
        lines.append(f"- **{person['name']}** — {person['work']}")
    lines.append("")
    lines.append("## Open lanes")
    lines.append("")
    for lane in state["open_lanes"]:
        lines.append(f"- **{lane['name']}** — {lane['note']}")
    lines.append("")
    lines.append("## How this board is made")
    lines.append("")
    lines.append(
        "`board-state.json` is written from the engagement record at "
        "press time; `tools/render_board.py` renders this page and "
        "the board's visuals (`assets/`) from that one file, so the "
        "numbers agree everywhere they appear. The living surface "
        "for the experiment is the Moltbook thread above; this board "
        "is its dated snapshot in the record, and it lands by pull "
        "request like everything else here."
    )
    lines.append("")
    for section in state.get("press", {}).get("log_sections", []):
        lines.append(section)
        lines.append("")
    return "\n".join(lines)


# ----------------------------------------------------------------- svgs

def svg_open(width, height, title):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" '
        f'height="{height}" viewBox="0 0 {width} {height}" role="img" '
        f'aria-label="{esc(title)}">'
        f"<title>{esc(title)}</title>"
        f'<rect width="{width}" height="{height}" fill="{BG}"/>'
    )


def render_timeline(state):
    cases = state["cases"]
    w = state["window"]
    opens, closes = parse_ts(w["opens"]), parse_ts(w["closes"])
    gen = parse_ts(state["generated_at_iso"])
    W, H = 920, 300
    x0, x1 = 60, 880
    axis_y = 210

    def x(ts):
        f = (ts - opens) / (closes - opens)
        return x0 + f * (x1 - x0)

    out = [svg_open(W, H, "Benchmark cases arriving across the collection window")]
    out.append(
        f'<text x="60" y="42" fill="{INK}" font-family="Georgia, serif" '
        f'font-size="22">Cases arriving — the first collection window</text>'
    )
    out.append(
        f'<text x="60" y="66" fill="{DIM}" font-size="13" '
        f'font-family="Helvetica, Arial, sans-serif">'
        f"State as of {esc(state['generated_at_label'])} · source: the "
        f"engagement record · gold = landed · blue = "
        + ("the close" if gen >= closes else "the window still open")
        + "</text>"
    )
    # axis
    out.append(
        f'<line x1="{x0}" y1="{axis_y}" x2="{x1}" y2="{axis_y}" '
        f'stroke="{DIM}" stroke-width="1.5"/>'
    )
    for frac, lab in [(0.0, "Nov 2 · 9:54 AM"), (1 / 3, "Nov 3 · 9:54 AM"),
                      (2 / 3, "Nov 4 · 9:54 AM"), (1.0, "Nov 5 · 9:54 AM")]:
        xx = x0 + frac * (x1 - x0)
        anchor = "start" if frac == 0 else ("end" if frac == 1 else "middle")
        out.append(
            f'<line x1="{xx:.1f}" y1="{axis_y - 6}" x2="{xx:.1f}" '
            f'y2="{axis_y + 6}" stroke="{DIM}"/>'
            f'<text x="{xx:.1f}" y="{axis_y + 26}" fill="{DIM}" '
            f'font-size="11" text-anchor="{anchor}" '
            f'font-family="Helvetica, Arial, sans-serif">{lab} PST</text>'
        )
    # now line (clamped to the axis; after the close it marks the close)
    closed = gen >= closes
    xn = min(x(gen), x1)
    now_label = "window closed" if closed else "this snapshot"
    out.append(
        f'<line x1="{xn:.1f}" y1="86" x2="{xn:.1f}" y2="{axis_y}" '
        f'stroke="{BLUE}" stroke-width="1.5" stroke-dasharray="4 3">'
        f'<animate attributeName="stroke-dashoffset" from="14" to="0" '
        f'dur="2.4s" repeatCount="indefinite"/></line>'
        f'<text x="{xn - 8 if closed else xn + 8:.1f}" y="98" fill="{BLUE}" '
        f'font-size="11" text-anchor="{"end" if closed else "start"}" '
        f'font-family="Helvetica, Arial, sans-serif">{now_label}</text>'
    )
    # case markers; labels stacked in a column with leader lines, so
    # arrivals minutes apart stay legible
    ordered = sorted(cases, key=lambda c: c["provenance"]["timestamp_iso"])
    lx = max(x(parse_ts(ordered[-1]["provenance"]["timestamp_iso"])) + 48, 160)
    row0, step = 96, 22
    for i, c in enumerate(ordered):
        ts = parse_ts(c["provenance"]["timestamp_iso"])
        xx = x(ts)
        ly = row0 + i * step
        color = STATUS_COLORS.get(c["status"], GOLD)
        out.append(
            f'<polyline points="{xx:.1f},{axis_y - 6} {xx:.1f},{ly - 4} '
            f'{lx - 6:.1f},{ly - 4}" fill="none" stroke="{color}" '
            f'stroke-width="1" opacity="0.55"/>'
            f'<circle cx="{xx:.1f}" cy="{axis_y}" r="6" fill="{color}">'
            + (
                '<animate attributeName="r" values="6;8.5;6" dur="2.6s" '
                'repeatCount="indefinite"/>'
                if i == len(ordered) - 1
                else ""
            )
            + "</circle>"
            f'<text x="{lx:.1f}" y="{ly}" font-size="13" '
            f'font-family="Helvetica, Arial, sans-serif">'
            f'<tspan fill="{INK}" font-weight="bold">{c["id"]}</tspan>'
            f'<tspan fill="{DIM}" font-size="11"> · '
            f'{esc(c["provenance"]["short_time_label"])} PST · '
            f'{esc(c["status"])}</tspan></text>'
        )
    out.append("</svg>")
    return "".join(out)


def render_progress(state):
    w = state["window"]
    gen = parse_ts(state["generated_at_iso"])
    frac = window_fraction(state, gen)
    pct = frac * 100
    W, H = 920, 150
    bx, bw = 60, 800
    fill = bw * frac
    out = [svg_open(W, H, "Collection window progress")]
    out.append(
        f'<text x="60" y="40" fill="{INK}" font-family="Georgia, serif" '
        f'font-size="20">The collection window</text>'
        f'<text x="860" y="40" fill="{GOLD}" font-size="15" '
        f'text-anchor="end" font-family="Helvetica, Arial, sans-serif">'
        + ("window closed · 100%" if frac >= 1 else f"{pct:.1f}% elapsed at this snapshot")
        + "</text>"
    )
    out.append(
        f'<rect x="{bx}" y="58" width="{bw}" height="22" rx="11" '
        f'fill="{PANEL}" stroke="{DIM}" stroke-width="0.75"/>'
        f'<rect x="{bx}" y="58" width="{fill:.1f}" height="22" rx="11" '
        f'fill="{GOLD}">'
        f'<animate attributeName="width" from="0" to="{fill:.1f}" '
        f'dur="1.8s" fill="freeze"/></rect>'
    )
    out.append(
        f'<text x="60" y="106" fill="{DIM}" font-size="12" '
        f'font-family="Helvetica, Arial, sans-serif">'
        f"Opened {esc(w['opens_label'])} · "
        f"{'closed' if frac >= 1 else 'closes'} {esc(w['closes_label'])} · "
        f"state as of {esc(state['generated_at_label'])}</text>"
        f'<text x="60" y="128" fill="{DIM}" font-size="12" '
        f'font-family="Helvetica, Arial, sans-serif">'
        f"The bar moves when a new dated snapshot is pressed — it is the "
        f"record's clock, not a live feed.</text>"
    )
    out.append("</svg>")
    return "".join(out)


def render_map(state):
    people = state["map"]["people"]   # [{id,label,x,y}]
    cases = state["map"]["cases"]     # [{id,label,x,y}]
    edges = state["map"]["edges"]     # [{from,to,label,kind}]
    W, H = 920, 484
    pos = {}
    for n in people + cases:
        pos[n["id"]] = (n["x"], n["y"] + 22)
    out = [svg_open(W, H, "The benchmark's relational map: contributors, cases, interactions")]
    out.append(
        f'<text x="60" y="42" fill="{INK}" font-family="Georgia, serif" '
        f'font-size="22">Who is building the benchmark — and how the work connects</text>'
        f'<text x="60" y="66" fill="{DIM}" font-size="13" '
        f'font-family="Helvetica, Arial, sans-serif">'
        f"State as of {esc(state['generated_at_label'])} · every edge is an "
        f"interaction in the record</text>"
        f'<text x="60" y="84" fill="{DIM}" font-size="13" '
        f'font-family="Helvetica, Arial, sans-serif">'
        f"gold = contribution and landing · "
        f"blue = the desk's governed hand: receipts, answers, asks</text>"
    )
    # Edges are drawn as gentle curves; a reciprocal pair bends to opposite
    # sides, and each label is placed at the first spot along its curve that
    # overlaps no node and no earlier label (so labels never collide).
    import math
    boxes = [(x - 40, y - 24, x + 40, y + 18) for (x, y) in pos.values()]
    def hits(b):
        return any(not (b[2] < o[0] or b[0] > o[2] or b[3] < o[1] or b[1] > o[3]) for o in boxes)
    pairs = {(e["from"], e["to"]) for e in edges}
    for e in edges:
        (ax, ay), (bx, by) = pos[e["from"]], pos[e["to"]]
        color = GOLD if e["kind"] == "contribution" else BLUE
        dx, dy = bx - ax, by - ay
        length = math.hypot(dx, dy) or 1.0
        nx, ny = -dy / length, dx / length
        bend = 26 if (e["to"], e["from"]) in pairs else 10
        if (e["to"], e["from"]) in pairs and e["from"] > e["to"]:
            bend = -bend
        cx, cy = (ax + bx) / 2 + nx * bend, (ay + by) / 2 + ny * bend
        out.append(
            f'<path d="M{ax},{ay} Q{cx:.1f},{cy:.1f} {bx},{by}" fill="none" '
            f'stroke="{color}" stroke-width="1.4" opacity="0.8">'
            f'<animate attributeName="opacity" values="0.45;0.9;0.45" '
            f'dur="5s" repeatCount="indefinite"/></path>'
        )
        w = 5.6 * len(e["label"]) + 6
        spot = None
        for t in (0.5, 0.42, 0.58, 0.34, 0.66, 0.26, 0.74):
            px = (1 - t) ** 2 * ax + 2 * (1 - t) * t * cx + t * t * bx
            py = (1 - t) ** 2 * ay + 2 * (1 - t) * t * cy + t * t * by
            for off in (0, -12, 12, -24, 24, -36, 36):
                lx, ly = px + nx * off, py + ny * off - 4
                box = (lx - w / 2, ly - 10, lx + w / 2, ly + 3)
                if not hits(box):
                    spot = (lx, ly, box)
                    break
            if spot:
                break
        if spot is None:
            lx, ly = cx, cy - 4
            spot = (lx, ly, (lx - w / 2, ly - 10, lx + w / 2, ly + 3))
        boxes.append(spot[2])
        out.append(
            f'<text x="{spot[0]:.1f}" y="{spot[1]:.1f}" fill="{DIM}" font-size="10.5" '
            f'text-anchor="middle" paint-order="stroke" stroke="#0B0F1A" stroke-width="3" '
            f'font-family="Helvetica, Arial, sans-serif">{esc(e["label"])}</text>'
        )
    for n in people:
        x, y = pos[n["id"]]
        out.append(
            f'<circle cx="{x}" cy="{y}" r="7" fill="{GOLD}"/>'
            f'<text x="{x}" y="{y - 14}" fill="{INK}" font-size="13" '
            f'font-weight="bold" text-anchor="middle" '
            f'font-family="Helvetica, Arial, sans-serif">{esc(n["label"])}</text>'
        )
    for n in cases:
        x, y = pos[n["id"]]
        out.append(
            f'<rect x="{x - 34}" y="{y - 15}" width="68" height="30" rx="8" '
            f'fill="{PANEL}" stroke="{BLUE}" stroke-width="1.4"/>'
            f'<text x="{x}" y="{y + 5}" fill="{INK}" font-size="13" '
            f'font-weight="bold" text-anchor="middle" '
            f'font-family="Helvetica, Arial, sans-serif">{esc(n["label"])}</text>'
        )
    out.append("</svg>")
    return "".join(out)


# ------------------------------------------------------------------ main

def main():
    state_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_STATE
    try:
        state = json.loads(state_path.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"cannot read state: {exc}", file=sys.stderr)
        return 2
    # consistency: the one count, everywhere
    ids = [c["id"] for c in state["cases"]]
    if len(ids) != len(set(ids)):
        print("duplicate case ids in state", file=sys.stderr)
        return 2
    for c in state["cases"]:
        if c["status"] not in STATUS_COLORS:
            print(f"unknown status {c['status']!r} on {c['id']}", file=sys.stderr)
            return 2
    (ROOT / "WORK-BOARD.md").write_text(render_board(state), encoding="utf-8")
    assets = ROOT / "assets"
    assets.mkdir(exist_ok=True)
    (assets / "cases-timeline.svg").write_text(render_timeline(state), encoding="utf-8")
    (assets / "window-progress.svg").write_text(render_progress(state), encoding="utf-8")
    (assets / "relational-map.svg").write_text(render_map(state), encoding="utf-8")
    gen = parse_ts(state["generated_at_iso"]).astimezone(timezone.utc)
    print(
        f"rendered board + 3 visuals · cases={len(ids)} · "
        f"window {window_fraction(state, parse_ts(state['generated_at_iso'])) * 100:.1f}% elapsed · "
        f"state as of {state['generated_at_label']}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
