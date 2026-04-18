"""
Tests for the static site merge script.

Run: pytest tests/ -v   or   python tests/test_merge_site.py
"""

from __future__ import annotations

import pathlib
import subprocess
import sys


REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
MERGE_SCRIPT = REPO_ROOT / "scripts" / "merge_site.py"
SITE_INDEX = REPO_ROOT / "site" / "index.html"


def test_merge_produces_doctype_html() -> None:
    """Merged output should start with a valid HTML5 doctype."""
    subprocess.run(
        [sys.executable, str(MERGE_SCRIPT)],
        cwd=REPO_ROOT,
        check=True,
    )
    text = SITE_INDEX.read_text(encoding="utf-8")
    assert text.startswith("<!DOCTYPE html>"), "site/index.html must start with <!DOCTYPE html>"
    assert "<html" in text.lower(), "merged file must contain html element"


def test_merge_includes_open_graph() -> None:
    """Merged output should include Open Graph meta for embeds."""
    subprocess.run(
        [sys.executable, str(MERGE_SCRIPT)],
        cwd=REPO_ROOT,
        check=True,
    )
    text = SITE_INDEX.read_text(encoding="utf-8")
    assert 'property="og:title"' in text
    assert 'property="og:description"' in text
    assert 'property="og:type"' in text
    assert 'property="og:url"' in text


if __name__ == "__main__":
    test_merge_produces_doctype_html()
    test_merge_includes_open_graph()
    print("OK: test_merge_site manual run passed")
