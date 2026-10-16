#!/usr/bin/env python3
"""Build a portable, deterministic ZIP of the canonical Agent Skill."""
from __future__ import annotations

import argparse
from pathlib import Path
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "senmonka-kun"


def package(output: Path) -> list[str]:
    if not (SKILL / "SKILL.md").is_file():
        raise ValueError("missing SKILL.md")
    files = sorted(path for path in SKILL.rglob("*") if path.is_file())
    if not files:
        raise ValueError("skill package is empty")
    output = output.resolve()
    if output.is_relative_to(SKILL.resolve()):
        raise ValueError("output must not be inside the source skill")
    output.parent.mkdir(parents=True, exist_ok=True)
    archived = []
    with ZipFile(output, "w") as archive:
        for path in files:
            if path.is_symlink():
                raise ValueError(f"refusing symlink: {path}")
            name = f"{SKILL.name}/{path.relative_to(SKILL).as_posix()}"
            entry = ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            entry.compress_type = ZIP_DEFLATED
            entry.external_attr = 0o644 << 16
            archive.writestr(entry, path.read_bytes())
            archived.append(name)
    return archived


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "dist" / "senmonka-kun.zip")
    args = parser.parse_args()
    for name in package(args.output):
        print(name)
    print(f"Created {args.output}")


if __name__ == "__main__":
    main()
