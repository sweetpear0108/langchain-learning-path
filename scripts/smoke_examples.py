#!/usr/bin/env python3
from __future__ import annotations

import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


@dataclass(frozen=True)
class SmokeTarget:
    name: str
    script: Path
    args: tuple[str, ...]
    expected_fragments: tuple[str, ...]


TARGETS = (
    SmokeTarget(
        name="chapter-01",
        script=REPO_ROOT / "examples" / "chapter-01" / "main.py",
        args=(),
        expected_fragments=("=== Prompt ===", "=== Model Output ===", "LangChain"),
    ),
    SmokeTarget(
        name="chapter-02",
        script=REPO_ROOT / "examples" / "chapter-02" / "main.py",
        args=(),
        expected_fragments=("=== Parsed Result ===", "- 标题: LangChain 核心抽象"),
    ),
    SmokeTarget(
        name="chapter-09",
        script=REPO_ROOT / "examples" / "chapter-09" / "main.py",
        args=(),
        expected_fragments=("# Evaluation Report", "Overall score: 13/13"),
    ),
    SmokeTarget(
        name="chapter-10",
        script=REPO_ROOT / "examples" / "chapter-10" / "main.py",
        args=("--root", str(REPO_ROOT)),
        expected_fragments=("# Capstone Assembly Report", "Readiness: 5/5"),
    ),
)


def run_target(target: SmokeTarget) -> None:
    completed = subprocess.run(
        [sys.executable, str(target.script), *target.args],
        cwd=REPO_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    if completed.returncode != 0:
        raise SystemExit(
            f"{target.name} failed with exit code {completed.returncode}.\n"
            f"stdout:\n{completed.stdout}\n"
            f"stderr:\n{completed.stderr}"
        )

    missing = [
        fragment for fragment in target.expected_fragments if fragment not in completed.stdout
    ]
    if missing:
        raise SystemExit(
            f"{target.name} output did not include expected fragments: {missing}\n"
            f"stdout:\n{completed.stdout}"
        )

    print(f"[ok] {target.name}")


def main() -> None:
    for target in TARGETS:
        run_target(target)
    print("Smoke tests passed for chapters: 01, 02, 09, 10")


if __name__ == "__main__":
    main()
