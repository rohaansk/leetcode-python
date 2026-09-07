#!/usr/bin/env python3
"""
Start a new problem folder in one command.

    python scripts/new.py 15 "3Sum" Medium

Creates solutions/0015-3sum/ with notes.md and solution.py, prefilled with
today's date and a review date a week out.
"""

import re
import sys
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "_template"
SOLUTIONS = ROOT / "solutions"


def slugify(title: str) -> str:
    s = title.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


def main() -> None:
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    number = int(sys.argv[1])
    title = sys.argv[2]
    difficulty = sys.argv[3] if len(sys.argv) > 3 else "Medium"

    folder = SOLUTIONS / f"{number:04d}-{slugify(title)}"
    if folder.exists():
        print(f"{folder} already exists.")
        sys.exit(1)
    folder.mkdir(parents=True)

    today = date.today()
    review = today + timedelta(days=7)

    notes = (TEMPLATE / "notes.md").read_text(encoding="utf-8")
    notes = (
        notes.replace("number: 0", f"number: {number}")
        .replace("title: Problem Name", f"title: {title}")
        .replace("difficulty: Medium", f"difficulty: {difficulty}")
        .replace("date_solved: 2026-01-01", f"date_solved: {today.isoformat()}")
        .replace("review_next: 2026-01-08", f"review_next: {review.isoformat()}")
        .replace("# 0. Problem Name", f"# {number}. {title}")
        .replace(
            "https://leetcode.com/problems/slug/",
            f"https://leetcode.com/problems/{slugify(title)}/",
        )
    )
    (folder / "notes.md").write_text(notes, encoding="utf-8")

    code = (TEMPLATE / "solution.py").read_text(encoding="utf-8")
    code = code.replace(
        "LeetCode 0. Problem Name  —  Medium",
        f"LeetCode {number}. {title}  —  {difficulty}",
    )
    (folder / "solution.py").write_text(code, encoding="utf-8")

    print(f"Created {folder.relative_to(ROOT)}")
    print("Now go solve it. Fill in notes.md while it's still warm.")


if __name__ == "__main__":
    main()
