---
name: fuzz-testing-workflow
description: "Use for reviewing, designing, implementing, or running bounded fuzz tests for parsers, binary formats, FFI, and stateful APIs. Covers harness correctness, corpus, oracles, instrumentation, minimization, and regression promotion. Uses the language-specific skill matrix."
---

# Fuzz testing

## When to use

Use this skill for reviewing, designing, implementing, or running bounded fuzz tests for parsers, binary formats, FFI, and stateful APIs.

## Scope and boundaries

Apply with the unit-test role and the [language-specific skill matrix](../programming-languages/references/programming-language-matrix.md)'s **Code quality** guidance for the relevant languages. Select supported fuzz tooling separately; the matrix does not establish fuzz-engine availability. Harness changes, campaign execution, and production fixes are separate scopes.

## Procedure

### Design and implement

- Identify target contract, public/internal boundary, accepted inputs, and oracle: invariant, round trip, independent implementation, defined rejection, or crash/sanitizer detection.
- Reuse supported installed tooling. C/C++ may use libFuzzer/AFL++ or project tools; Rust may use cargo-fuzz or existing property-based tools. Verify compiler, platform, and nightly requirements before choosing.
- Arbitrary bytes are valid inputs to a parser only if its contract permits them. For typed/FFI APIs, construct valid pointers, lengths, ownership, and state; do not manufacture UB as a rejection test.
- Keep harnesses small with explicit setup/reset/cleanup. Do not swallow unexpected failures or compare expected results using the same faulty algorithm.
- Isolate test-owned state, avoid uncontrolled I/O/global mutation, and reset persistent-mode state. Bound allocations and expensive parsing without excluding in-scope behavior silently.
- Use meaningful seeds and edge cases; document source/licensing and protect private payloads. Dictionaries/structured generators may improve exploration without proving completeness.

### Execute and triage

- Agree duration/run count, memory/storage/input-size, workers, and operation timeouts before campaigns. Do not exhaust shared resources or fuzz remote services without authorization.
- Build supported instrumentation; record revision, dirty state, toolchain, features, harness, corpus identity, arguments, and engine reproduction settings.
- Confirm inputs reached the intended target; an empty/unregistered or always-rejecting harness is not meaningful validation.
- Preserve crashing/hanging inputs and diagnostics before bounded engine-supported minimization. Distinguish harness defects, precondition violations, environment failures, and production bugs.
- Reproduce with the matching artifact and report the relevant issue/impact and suggested fix. No crashes in a bounded run does not prove safety.
- Promote confirmed findings into readable deterministic regressions when requested; production fixes require authorization. Keep sanitizer and fuzz throughput results separate from normal benchmarks.
