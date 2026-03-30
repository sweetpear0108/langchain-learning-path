from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class SectionStatus:
    path: str
    exists: bool
    purpose: str


KEY_DIRECTORIES = [
    SectionStatus("docs", False, "course content and site pages"),
    SectionStatus("examples", False, "chapter-level runnable samples"),
    SectionStatus("backend", False, "phase-2 interactive runtime"),
    SectionStatus("shared", False, "prompts, datasets, and diagrams"),
    SectionStatus(".github/workflows", False, "CI and GitHub Pages automation"),
]


def inspect_layout(root: Path) -> list[SectionStatus]:
    inspected: list[SectionStatus] = []
    for item in KEY_DIRECTORIES:
        inspected.append(
            SectionStatus(
                path=item.path,
                exists=(root / item.path).exists(),
                purpose=item.purpose,
            )
        )
    return inspected


def chapter_site_map(root: Path) -> list[str]:
    docs = root / "docs" / "chapters"
    if not docs.exists():
        return ["docs/chapters is missing"]

    chapters = sorted(p.name for p in docs.glob("chapter-*.md"))
    return [f"- {name}" for name in chapters]


def readiness_score(statuses: list[SectionStatus]) -> tuple[int, int]:
    ready = sum(1 for item in statuses if item.exists)
    return ready, len(statuses)


def print_report(root: Path) -> None:
    statuses = inspect_layout(root)
    ready, total = readiness_score(statuses)

    print("# Capstone Assembly Report")
    print(f"Repository root: {root}")
    print(f"Readiness: {ready}/{total}")
    print()
    print("## Key Sections")
    for item in statuses:
        state = "ready" if item.exists else "missing"
        print(f"- {item.path}: {state} ({item.purpose})")
    print()
    print("## Learning Site Map")
    for line in chapter_site_map(root):
        print(line)
    print()
    print("## Deployment Checklist")
    checklist = [
        "confirm docs pages are wired to VitePress",
        "verify chapter navigation links",
        "publish static site to GitHub Pages",
        "keep runtime code in an external backend",
    ]
    for item in checklist:
        print(f"- {item}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Inspect capstone structure and deployment readiness."
    )
    parser.add_argument(
        "--root",
        default="/home/litianwei/langchain-learning-path",
        help="Repository root to inspect.",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()
    print_report(Path(args.root))


if __name__ == "__main__":
    main()
