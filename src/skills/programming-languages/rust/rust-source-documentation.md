---
name: rust-source-documentation
description: "Use for reviewing or writing Rust source documentation, rustdoc, and safety comments. Covers reachable APIs, Errors/Panics/Safety contracts, intra-doc links, doctests, MSRV/features, and comments-only validation."
---

# Rust source documentation

## When to use

Use this skill for reviewing or writing Rust source documentation, rustdoc, and safety comments.

## Scope and boundaries

Apply within authorized comments-only scope. Respect MSRV, edition, features/targets, runtime, panic strategy, and rustdoc conventions.

## Procedure

### Document

- Identify externally reachable APIs through module visibility and re-exports; do not mechanically document every `pub` or `pub(crate)` item.
- Use `///` for items and `//!` for module/crate documentation at valid positions. Preserve existing documentation attributes and attachment to the intended item.
- Start with a concise purpose; explain relevant input constraints, ownership/borrowing, lifecycle, errors, side effects, and thread/async cancellation behavior.
- Use `# Errors` and `# Panics` when meaningful. Public unsafe functions/traits require a `# Safety` contract covering caller/implementor obligations.
- Explain non-obvious unsafe operations with evidence-backed `// SAFETY:` rationale; never assert safety without checking the relevant invariants.
- Prefer intra-doc links to stable symbols, not brittle source-line links. Verify their resolution under supported feature configurations.
- Keep examples accurate, minimal, and MSRV-compatible. Use appropriate error propagation and hidden setup where useful; do not use `ignore` or `no_run` merely to hide a broken example.
- Comments explain contracts or reasoning, not every branch. Avoid arbitrary length thresholds and invented guarantees.

### Validate

Inspect the diff for comments-only edits and correct rustdoc attachment; documentation tests can execute code.

Use project rustdoc checks or appropriately scoped `cargo doc --no-deps`; run relevant doctests when runnable examples change and supported build checks when needed. Respect package/features/targets rather than enabling all features indiscriminately.

Report warnings, broken links, exact checks, unexecuted examples, and unavailable configurations. `cargo build` alone does not validate rustdoc/examples or prove unchanged behavior; diagnose failures before discarding edits.
