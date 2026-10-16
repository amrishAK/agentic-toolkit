---
name: c-unit-testing
description: "Use for reviewing, designing, writing, or maintaining C unit tests. Covers defined inputs/errors, allocation failure injection, ownership, partial cleanup, C harnesses, and targeted execution."
---

# C unit testing

Apply with the unit-test workflow. Keep production logic/interfaces unchanged unless explicitly authorized.

## Test

- Respect the C standard, compiler/platform, and existing harness. Keep production C compiled as C.
- Reuse Unity, cmocka, CUnit, or project tooling. Catch2 is a C++ framework, not pure C; a C++ harness is valid only when established or requested.
- Assert documented outputs, error codes, state transitions, ownership, and cleanup. Null/zero/boundary rejection is valid only where behavior is defined.
- Do not ordinarily double-free, use freed storage, or access out of bounds to test rejection. Intentional diagnostic tests need supported isolated infrastructure.
- Use existing local allocator/I/O seams for failure injection, not real exhaustion or indiscriminate process-wide interception.
- Verify partial cleanup through valid observations or test-owned counters/resources, not freed objects.
- Ensure harness teardown survives fatal assertions. Reset permitted fixture state and avoid order dependencies.
- Check `errno` only as specified. Use type-appropriate assertions and descriptive names with useful table-case diagnostics.

## Validate

Register and build the affected test target in supported C mode. Run the relevant selection and confirm intended cases executed.

Use supported instrumented ASan/UBSan or separate TSan when relevant. Environment variables alone do not enable instrumentation; Valgrind requires a supported platform. Report exact results and limitations without claiming proof of safety.
