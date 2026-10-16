---
name: c-integration-testing
description: "Use for black-box C integration test review, design, or implementation. Covers public headers, real linked components, ownership/error propagation, harness teardown, platform resources, and actual test execution."
---

# C integration testing

Apply with the integration-test workflow. Preserve production behavior/interfaces unless explicitly authorized.

## Test

- Respect selected C standard, compiler/platform, ABI, and harness; infer compilation mode from build configuration.
- Link real production components through public headers, not included implementation `.c` files or overridden internal functions.
- Established C++ harnesses are acceptable; compile production C as C and preserve linkage.
- Test defined inputs/errors, ownership transfers, cross-component public state, and resource lifecycle through valid observable results.
- Use `errno` only where specified; never inspect freed storage or invoke undefined behavior as ordinary rejection coverage.
- Keep real implementations across the tested boundary; describe controlled substitutes outside it.
- Ensure setup/teardown releases buffers, handles, workers, and test-owned processes even on fatal assertions.
- Respect platform filesystem/socket/process semantics; do not assume POSIX behavior on Windows.

## Validate

Build real components and registered integration targets, verify dependency readiness, and confirm scenarios executed.

Use supported instrumented ASan/UBSan or separate TSan when relevant. Report real dependencies/substitutes, exact results, missing infrastructure, and cleanup limitations; missing prerequisites are not passed tests.
