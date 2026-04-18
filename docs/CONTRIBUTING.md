# Contributing

1. Follow [CODING_STANDARDS.md](./CODING_STANDARDS.md).
2. Edit HTML fragments under `src/parts/`, then run `python scripts/merge_site.py` and commit `site/index.html` (CI rebuilds on push; keep the merged file in sync for local preview).
3. Run `python tests/test_merge_site.py` before pushing.
4. **Push every change to `origin main`** when work is ready so GitHub, Actions, and Pages stay the source of truth.

## Notion

Keep the Notion handbook linked from [CODING_STANDARDS.md](./CODING_STANDARDS.md) updated when process changes.
