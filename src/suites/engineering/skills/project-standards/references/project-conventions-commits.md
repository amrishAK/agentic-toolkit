# Commit messages

Use [Conventional Commits](https://www.conventionalcommits.org/).

## Format

```text
type(optional-scope): summary

Optional body explaining why the change was made.
```

## Types

| Type | Use for |
|---|---|
| `feat` | New user-visible capability |
| `fix` | Bug fix |
| `refactor` | Restructuring without behaviour change |
| `perf` | Performance improvement |
| `test` | Adding or changing tests only |
| `docs` | Documentation only |
| `build` | Build system, dependencies, entry points |
| `ci` | CI workflows |
| `chore` | Maintenance that fits no other type |

## Rules

- Write the summary in the imperative mood and lowercase, with no trailing period and at most 72 characters.
- Use a scope when it helps, such as a module name: `fix(db): ...`.
- Mark breaking changes with `!` after the type or scope, and explain them in a `BREAKING CHANGE:` footer.
- One logical change per commit; do not mix a refactor with a behaviour change.
- Do not rewrite published history to fix older messages.
