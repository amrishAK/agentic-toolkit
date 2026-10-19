# Commit review

**Gate:** is this change ready to commit, or correct as committed?
**Range:** staged changes (`git diff --staged`) or one commit (`git show <sha>`).
**Depth:** the changed files and their direct callers. Keep it fast.

## Check

- **Correctness:** logic errors, error handling, resource cleanup, and unsafe or undefined behaviour in the changed code.
- **One purpose:** the change does one thing. Unrelated edits, debug output, commented-out code, and stray files belong elsewhere.
- **Tests:** behaviour changes come with tests at the right tier, or the message explains why there are none.
- **Message:** follows [Conventional Commits](../../project-standards/references/project-conventions-commits.md). The type matches the change (`fix` fixes a bug, `refactor` changes no behaviour), and breaking changes are marked.
- **Conventions in touched files:** naming, architecture boundaries, and error patterns from the project rules. Report drift only in the files this change touches.
- **Secrets:** no credentials, tokens, private keys, or machine-specific paths.

## Blockers

- A bug, crash, data loss, or undefined behaviour introduced by the change.
- Committed secrets.
- A commit type that misdescribes the change, or a missing breaking-change marker.
- Code that fails to build or fails its own tests.
