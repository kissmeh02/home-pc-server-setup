# -*- coding: utf-8 -*-
"""
Merge ordered HTML fragments from src/parts into site/index.html (UTF-8).

Run from repo root: python scripts/merge_site.py
"""

from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
PARTS_DIR = REPO_ROOT / "src" / "parts"
OUTPUT = REPO_ROOT / "site" / "index.html"
PART_GLOB = "part*.html"


def merge_html_parts() -> str:
    """Concatenate part*.html in lexical order. Raises if none found."""
    parts = sorted(PARTS_DIR.glob(PART_GLOB))
    if not parts:
        raise FileNotFoundError(f"No {PART_GLOB} under {PARTS_DIR}")
    return "".join(p.read_text(encoding="utf-8") for p in parts)


def main() -> None:
    merged = merge_html_parts()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(merged, encoding="utf-8")
    size = len(merged.encode("utf-8"))
    print(f"Wrote {OUTPUT} ({size} bytes) from {sorted(PARTS_DIR.glob(PART_GLOB))}")


if __name__ == "__main__":
    main()
