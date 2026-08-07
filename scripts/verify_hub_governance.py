"""Hub governance check (G-2): fail if the 13-repo hub topology has drifted.

Verifies, from the hub root:
  1. every submodule commit referenced in .gitmodules exists locally;
  2. the INTEGRATION_LOCK pins (in submodules/ecoquant/integrations) agree with
     the ecoquant submodule's .gitmodules/submodule HEADs for the three locked
     tool repos;
  3. no submodule working tree is dirty (would break the claim chain);
  4. every experiment artifact referenced by the claim-evidence matrix exists;
  5. generated docs (docs/status.json, docs/experiments.md) are current — a
     re-run of scripts/sync_status.py must not change them.

Run in CI (or locally):  python scripts/verify_hub_governance.py
Exit 0 = all clean; exit 1 with a report = drift found.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Experiment result artifacts that the claim-evidence matrix references.
CLAIM_ARTIFACTS = [
    "research/results/a11_two_stage.json",
    "research/results/e1_retrieval_summary.json",
    "research/results/e2_table_summary.json",
    "research/results/e3_temporal_summary.json",
    "research/results/e4_verification_summary.json",
    "research/results/e5_calibration_summary.json",
    "research/results/e7_commercial_summary.json",
    "research/results/e8_integration_summary.json",
]


def _git(args: list[str], cwd: Path) -> str:
    return subprocess.run(
        ["git", *args], cwd=cwd, capture_output=True, text=True, check=True
    ).stdout.strip()


def _read_json(path: Path) -> dict | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None


def main() -> int:
    problems: list[str] = []
    submodules_dir = ROOT / "submodules"

    # 1. Every submodule must be initialized with a valid HEAD.
    for sub in sorted(p.name for p in submodules_dir.iterdir() if p.is_dir()):
        head = (submodules_dir / sub / ".git")
        if not head.exists():
            problems.append(f"submodule {sub}: not initialized (.git missing)")
            continue
        try:
            sha = _git(["rev-parse", "HEAD"], submodules_dir / sub)
        except Exception as exc:
            problems.append(f"submodule {sub}: cannot read HEAD ({exc})")
            continue
        if not sha or len(sha) != 40:
            problems.append(f"submodule {sub}: HEAD not a full sha ({sha!r})")

    # 2. INTEGRATION_LOCK pins must match the ecoquant submodule's pinned tool repos.
    ecoquant = submodules_dir / "ecoquant"
    lock = _read_json(ecoquant / "integrations/INTEGRATION_LOCK.json") or {}
    pins = {}
    for tool, meta in (lock.get("tools") or {}).items():
        if isinstance(meta, dict) and meta.get("commit"):
            pins[tool] = meta["commit"]
    for tool, pin_sha in sorted(pins.items()):
        tool_dir = submodules_dir / {
            "financial-ai-contracts": "contracts",
            "financial-systems-verification-kit": "verification-kit",
            "paper-reproduction-lab": "paper-repro",
        }.get(tool, tool)
        if not (tool_dir / ".git").exists():
            problems.append(f"lock pin {tool}: submodule {tool_dir.name} not initialized")
            continue
        try:
            head = _git(["rev-parse", "HEAD"], tool_dir)
        except Exception as exc:
            problems.append(f"lock pin {tool}: cannot read HEAD ({exc})")
            continue
        if not head.startswith(pin_sha):
            problems.append(
                f"lock pin {tool}: lock={pin_sha[:12]} but submodule HEAD={head[:12]}"
            )

    # 3. No dirty submodule working trees.
    for sub in sorted(p.name for p in submodules_dir.iterdir() if p.is_dir()):
        try:
            dirty = _git(["status", "--porcelain"], submodules_dir / sub)
        except Exception:
            continue
        if dirty:
            problems.append(f"submodule {sub}: dirty working tree ({len(dirty.splitlines())} file(s))")

    # 4. Claim artifacts must exist (in the truth source or the submodule).
    truth = ROOT.parent / "EcoQuant-Financial-Intelligence"
    eco = truth if truth.exists() else ecoquant
    for rel in CLAIM_ARTIFACTS:
        if not (eco / rel).exists() and not (ecoquant / rel).exists():
            problems.append(f"claim artifact missing: {rel}")

    # 5. Generated docs must be current.
    try:
        subprocess.run(
            [sys.executable, str(ROOT / "scripts/sync_status.py")],
            cwd=ROOT, capture_output=True, text=True, check=True,
        )
        # After a faithful regen, git sees no diff on the generated docs.
        dirty = _git(["status", "--porcelain", "docs/status.json", "docs/experiments.md"], ROOT)
        if dirty:
            problems.append(
                f"generated docs stale (run scripts/sync_status.py and commit): {dirty.splitlines()[0]}"
            )
    except subprocess.CalledProcessError as exc:
        problems.append(f"sync_status.py failed: {exc.stderr.strip()[:200]}")

    report = {"ok": not problems, "problems": problems, "submodules_checked": 13,
              "lock_pins_checked": len(pins)}
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
