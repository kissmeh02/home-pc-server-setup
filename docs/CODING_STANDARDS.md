# Coding standards

These apply to all work in this repository unless explicitly waived.

## Minimal version (always on)

- Split by responsibility; **~150–200 lines per file** — stop and split if larger.
- **Separate** data access, business logic, and UI; no circular deps.
- **camelCase** / **PascalCase** / **UPPER_SNAKE_CASE** / **kebab-case** files; verb–noun functions; `is`/`has` booleans.
- **One job per function** (~20–30 lines); pure where possible; early returns; named constants.
- **No silent errors**; validate inputs at boundaries; document exports.
- **Tests** mirror `src/`; stub or real tests for new logic.
- Refactor **without behavior change** when needed; call out smells.

**Notion (living doc):** [Add your Notion link here](https://www.notion.so/) — keep the Notion page and this file in sync when process changes.

## Architecture

- Avoid monolithic files. Split by responsibility: one file per module, class, or feature.
- Target **~150–200 lines per file**. If growth continues past that, pause and split.
- Separate **data access**, **business logic**, and **presentation/UI** — not in the same file.
- Prefer **composition** over inheritance; avoid deep hierarchies.
- **No circular dependencies** — flag and fix before adding code.

## File & folder structure

- Group by **feature/domain** first, then by type (not flat file dumps).
- Use conventional names for the stack (`src/`, `lib/`, `utils/`, `services/`, `components/`, `tests/` as applicable).
- Each package/module exposes a clear **public API** (e.g. `index` barrel); keep internals private.

## Naming

| Kind | Convention |
|------|------------|
| Variables / functions | camelCase |
| Classes | PascalCase |
| Constants | UPPER_SNAKE_CASE |
| Files | kebab-case |

- Names describe **intent**, not implementation. No single-letter identifiers except loop indices.
- Booleans: `is` / `has` / `can` / `should` prefixes.
- Functions: verb–noun (`fetchUser`, `buildPayload`, `validateInput`).

## Functions

- One responsibility per function; if you need “and” to describe it, split.
- Target **20–30 lines max**; extract helpers.
- Prefer **pure** functions; avoid hidden side effects.
- **Early returns** over deep nesting.
- No magic numbers/strings — use named constants.

## Refactoring

- Refactor in a **separate step** before features when required; state that explicitly.
- Preserve behavior; no scope creep.
- Call out smells (duplication, god objects, long parameter lists) even when out of scope.
- **DRY:** twice → extract; three times → utility.

## Error handling

- Never swallow errors silently; handle or propagate with context.
- Use typed/custom errors where supported.
- Validate external inputs at boundaries (API, user input, env).
- Log with enough context: what failed, where, with what data.

## Comments & documentation

- Code should read clearly; comment **why**, not what, when non-obvious.
- Exported symbols: JSDoc/docstring (purpose, params, returns, throws).
- `TODO` must include reason and ideally ticket/issue reference.

## Testing

- New logic gets a **unit test stub** minimum (`tests/` mirrors `src/`).
- Name tests: `it should [expected behavior] when [condition]`.
- No business logic in test setup — use factories/fixtures.

## Workflow

- Short plan (2–3 sentences) before non-trivial code.
- After changes: summarize what was done, gaps, risks.
- One clarifying question when ambiguous; not a questionnaire.
- “Quick fix” still follows these rules.
