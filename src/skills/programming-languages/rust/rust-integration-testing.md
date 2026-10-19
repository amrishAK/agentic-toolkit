---
name: rust-integration-testing
description: "Use for black-box Rust integration test review, design, or implementation. Covers Cargo external test targets, public crate APIs, real components, parallel resource isolation, async teardown, and execution."
---

# Rust integration testing

## When to use

Use this skill for black-box Rust integration test review, design, or implementation.

## Scope and boundaries

Apply with the integration-test workflow. Preserve production behavior/interfaces unless explicitly authorized.

## Procedure

### Test

- Respect MSRV, features/targets, runtime, and test configuration.
- Use registered external Cargo integration targets, normally `tests/`; respect explicit `[[test]]` and shared test-support conventions.
- Do not include sources by path, expose private items, or add test-only production APIs to bypass crate visibility.
- Create fixtures through public constructors/configuration. Assert public error variants/state, not private representation or incidental messages.
- Use real components across the boundary and storage/database namespaces safe for Cargo parallelism. Avoid process-global environment mutation by default.
- Use existing async runtime/macros, readiness checks, bounded waits, and joined/awaited workers.
- Use synchronous guards plus explicit awaited teardown; `Drop` does not guarantee async shutdown.
- Discover Cargo-built executables through supported mechanisms, not guessed paths. Complete application journeys remain E2E.

### Validate

Select the correct package, registered target, and filter; confirm scenarios executed. Follow supported feature/target configurations rather than enabling all features.

Report exact commands, real dependencies/substitutes, infrastructure failures, and cleanup limitations. Zero matches, missing prerequisites, and only-skipped runs do not validate behavior.
