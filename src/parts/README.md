# HTML parts (public build order)

Fragments are concatenated in **lexical** order: `part01.html`, `part02.html`, `part03.html`.

| Part | Contents |
|------|----------|
| `part01.html` | Document head (incl. OG meta), shell, PC 1, PC 2 |
| `part02.html` | PC 3, NAS |
| `part03.html` | Network → Summary, `</main>`, script, `</body></html>` |

**Build:** `python scripts/merge_site.py` → `site/index.html` (also used by CI and GitHub Pages).
