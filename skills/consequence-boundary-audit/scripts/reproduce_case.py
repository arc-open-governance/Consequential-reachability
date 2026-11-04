#!/usr/bin/env python3
"""Reproduce an ARC Examiner Kit v0.2.0 case run, pin-first.

Downloads the pinned public release asset, verifies its sha256 against the
pin below BEFORE extraction, runs the kit's single entry command, and
writes a machine-readable reproduction report next to the kit's own
results.json. Standard library only. Writes only inside --workdir.

Usage: reproduce_case.py [--workdir DIR] [--asset FILE]
  --asset FILE   use a local copy of the release asset instead of fetching
                 (its sha256 is still verified against the pin).

Exit 0 = run completed and every control matched its frozen expectation.
Exit 1 = pin mismatch, kit failure, or a control diverged (a finding).
Exit 2 = usage / IO error.
"""

import argparse
import hashlib
import json
import subprocess
import sys
import tarfile
import urllib.request
from pathlib import Path

KIT_VERSION = "0.2.0"
KIT_ASSET_NAME = "examiner-kit-v0.2.tar.gz"
KIT_ASSET_URL = (
    "https://github.com/arc-open-governance/arc-examiner-kit"
    "/releases/download/v0.2.0/examiner-kit-v0.2.tar.gz"
)
KIT_ASSET_SHA256 = "aba968025892f5aa87bbdabfae2f749ead638ecb108c09bc093422f912977167"
KIT_ASSET_BYTES = 24740
KIT_TAG_COMMIT = "0eef0bd3fed6412b919e2efd097c3bddbb0533e2"
EXPECTED_RESULTS_DIGEST = (
    "sha256:f40f78fb4a382a3c24207ac835f3db750479c0b1609d55fc75bc625d05f824b1"
)


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--workdir", default="./audit-work",
                    help="directory for the asset, the kit, and the report")
    ap.add_argument("--asset", default=None,
                    help="local asset file to use instead of downloading")
    args = ap.parse_args(argv[1:])

    workdir = Path(args.workdir).resolve()
    workdir.mkdir(parents=True, exist_ok=True)

    # 1. Obtain the asset.
    if args.asset:
        asset = Path(args.asset).resolve()
        if not asset.is_file():
            print(f"ERROR: --asset {asset} not found", file=sys.stderr)
            return 2
    else:
        asset = workdir / KIT_ASSET_NAME
        print(f"fetching {KIT_ASSET_URL}")
        try:
            urllib.request.urlretrieve(KIT_ASSET_URL, asset)
        except Exception as exc:  # network / IO
            print(f"ERROR: download failed: {exc}", file=sys.stderr)
            return 2

    # 2. Verify the pin BEFORE trusting or extracting anything.
    digest = sha256_of(asset)
    size = asset.stat().st_size
    print(f"asset: {size} bytes, sha256 {digest}")
    if digest != KIT_ASSET_SHA256 or size != KIT_ASSET_BYTES:
        print("PIN MISMATCH: the fetched asset does not match the pinned "
              "Examiner Kit v0.2.0 release. Aborting — report this as a "
              "finding, do not run the contents.")
        return 1

    # 3. Extract and run the kit's own entry command. The kit root is the
    # tarball's own top-level directory — never assumed from the version.
    with tarfile.open(asset, "r:gz") as tf:
        top = tf.getnames()[0].split("/")[0]
    kit_root = workdir / top
    if kit_root.exists():
        print(f"kit already extracted at {kit_root} (pin-verified asset)")
    else:
        with tarfile.open(asset, "r:gz") as tf:
            tf.extractall(workdir, filter="data")
    runner = kit_root / "run_exam.py"
    if not runner.is_file():
        print(f"ERROR: {runner} missing after extraction", file=sys.stderr)
        return 2
    print(f"running: python3 run_exam.py  (in {kit_root})")
    proc = subprocess.run(
        [sys.executable, "run_exam.py"], cwd=kit_root,
        capture_output=True, text=True)
    sys.stdout.write(proc.stdout)
    if proc.stderr:
        sys.stderr.write(proc.stderr)

    results_path = kit_root / "results.json"
    report = {
        "skill": "consequence-boundary-audit",
        "job": "reproduce an Examiner Kit case run",
        "kit": {
            "name": "arc-examiner-kit",
            "version": KIT_VERSION,
            "tag_commit": KIT_TAG_COMMIT,
            "asset_sha256": digest,
            "asset_bytes": size,
            "pin_verified": True,
        },
        "kit_exit_code": proc.returncode,
        "results_json": str(results_path) if results_path.is_file() else None,
        "evidence_strength": (
            "SYNTHETIC / FIXTURE — local record-layer strength. This result "
            "is evidence about the kit's frozen fixture semantics only; it "
            "is not evidence about any deployed system."
        ),
    }
    if results_path.is_file():
        results = json.loads(results_path.read_text(encoding="utf-8"))
        report["results_digest"] = results.get("results_digest")
        report["results_digest_matches_frozen"] = (
            results.get("results_digest") == EXPECTED_RESULTS_DIGEST)
        # Surface per-test outcomes without re-grading them.
        tests = results.get("tests") or results.get("results") or {}
        report["kit_reported_outcomes"] = tests

    report_path = workdir / "reproduction-report.json"
    report_path.write_text(json.dumps(report, indent=2) + "\n",
                           encoding="utf-8")
    print(f"report written: {report_path}")
    print("strength: SYNTHETIC / FIXTURE — local record-layer strength; "
          "not evidence about any deployed system.")

    if proc.returncode != 0:
        print("KIT RUN FAILED OR A CONTROL DIVERGED — an honest result; "
              "see results.json and references/HANDOFF.md for how to "
              "submit a divergence.")
        return 1
    if report.get("results_digest_matches_frozen") is False:
        print("RESULTS DIGEST DIVERGES from the frozen expectation — "
              "a finding; see references/HANDOFF.md.")
        return 1
    print("REPRODUCED: every control matched its frozen expectation.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
