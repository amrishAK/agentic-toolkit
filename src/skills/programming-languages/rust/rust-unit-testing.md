---
name: rust-unit-testing
description: "Use for reviewing, designing, writing, or maintaining Rust unit tests. Covers module-local tests, error assertions, observable ownership/drop behavior, deterministic async execution, Cargo selection, and MSRV."
---

# Rust unit testing

## When to use

Use this skill for reviewing, designing, writing, or maintaining Rust unit tests.

## Scope and boundaries

Apply with the unit-test workflow. Keep production logic/interfaces unchanged unless explicitly authorized.

## Procedure

### Test

- Respect MSRV, edition, features/targets, panic strategy, and existing runtime/test tools.
- Prefer established `#[cfg(test)] mod tests` organization. Private access may verify meaningful invariants, not incidental representation.
- Use descriptive repository-consistent names; assert exact values, error variants, or properties. Match messages only when contractual.
- `unwrap`/`expect` can be appropriate for setup/asserted success with useful diagnostics; avoid vague assertions.
- Test observable ownership/drop behavior with guards, accounting for panic/abort configuration.
- Use existing async runtime/macros, channels/barriers or controlled clocks over sleeps, bounded operations, and joined/awaited workers.
- Do not construct invalid references or invoke undefined behavior as a safe-rejection test. Keep supported unsafe diagnostics separate.
- Reuse supported seeded property/model tests where useful; do not add crates to satisfy a checklist. Justify floating-point tolerances.

### Validate

Select the correct Cargo package, unit-test target, and filter. Confirm intended cases ran; zero matches are not validation.

Follow formatting/Clippy guidance and supported features. Broaden only when shared fixtures/evidence warrant it. Use Miri/concurrency-model tools where supported without implying proof of safety.
