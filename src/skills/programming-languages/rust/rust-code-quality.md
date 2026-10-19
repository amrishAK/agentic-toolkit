---
name: rust-code-quality
description: "Use for reviewing, writing, fixing, or refactoring Rust code. Covers ownership, borrowing, types and traits, unsafe contracts, async lifecycle, rustdoc, Cargo feature/target validation, and MSRV."
---

# Rust code quality

## When to use

Use this skill for reviewing, writing, fixing, or refactoring Rust code.

## Scope and boundaries

Apply with the code-quality workflow and authorized task scope; this skill does not authorize edits.

Use the following as opinionated recommended defaults for Rust projects, not universal requirements. Follow established project conventions first. Do not add empty files or dependencies solely to match these defaults.

## Procedure

### Recommended file organization

- Keep every `mod.rs` declarative: module declarations and intentional visibility declarations/re-exports only. Do not put functions, implementation logic, model definitions, or tests in `mod.rs`.
- A module directory that only groups child modules (for example, `db/`) contains only `mod.rs`; it does not need its own `error.rs` or `model.rs`.
- For a module directory that contains implementation files, use `error.rs` for that module's error types and `model.rs` for its data models and type definitions. Do not invent placeholder error variants or add an empty `error.rs` solely to preserve the layout.
- Keep operational methods and behavior contracts in focused implementation files named for their responsibility; keep `model.rs` focused on data definitions.
- Put module-level tests in a sibling `tests.rs` file and include them from `mod.rs` only with a declaration such as `#[cfg(test)] mod tests;`. Keep test bodies and shared test helpers out of `mod.rs`. Tests tightly specific to a single implementation file may remain in that file under `#[cfg(test)]`.
- When adding or moving code, update module declarations and public re-exports in `mod.rs` as needed without placing implementation or test bodies there.
- During reviews, treat deviations from these defaults as recommendations, not defects; account for established project conventions and do not restructure unrelated code unless the task authorizes cleanup.

### Recommended Rust libraries

- Prefer `thiserror::Error` with descriptive variants for project error types. Preserve underlying causes with `#[source]` or `#[from]` where appropriate; avoid hand-written `Display`/`Error` implementations when `thiserror` fits.
- Prefer TOML for application settings files and the `toml` crate for parsing/serialization. Convert parsed TOML into typed settings models and validate configuration explicitly; avoid spreading raw TOML access throughout runtime code.
- Reuse these established preferences when they fit the task. Do not add or replace dependencies without a concrete need and authorization.

### Review and implement

- Respect MSRV, edition, toolchain, features/targets, allocator, panic strategy, runtime, dependencies, and project conventions.
- Use ownership/borrowing deliberately, purposeful types, and understandable lifetimes/trait bounds. Make invalid states difficult without speculative wrappers.
- Reuse standard/project patterns; avoid unnecessary clones, allocations, dispatch, and `unsafe`.
- Propagate or intentionally handle meaningful errors; do not swallow failures or return misleading success-shaped fallbacks.
- Review edge cases, resource lifetime, locks, concurrency, async cancellation/shutdown, and unsafe invariants using concrete evidence.
- Introduce traits/generics for actual contracts, reuse, or testability; apply Clean Code/SOLID without fighting the type system.
- For FFI, preserve ABI/layout, ownership, errors, lifecycle, and panic/exception boundary contracts on both sides.
- Document actually exposed APIs accounting for containing modules and re-exports, not every `pub` or `pub(crate)` item.
- Use `///` for items and `//!` for modules/crates, concise summaries, and relevant Errors/Panics/Safety sections. Every public `unsafe fn` needs a caller contract in `# Safety`.
- Use justified `// SAFETY:` rationale for nonobvious unsafe blocks. Keep examples accurate and ordinarily propagate errors with `?`.

### Validate

Use project formatting, targeted tests, Clippy, and affected builds. Respect supported feature/target combinations; do not enable all features indiscriminately or claim untested support.

For documentation-only work, follow rustdoc checks such as `cargo doc --no-deps`; run doctests when runnable examples change. Use Miri/concurrency-model tooling only when supported and relevant. Consult current official Rust documentation for uncertain rules.
