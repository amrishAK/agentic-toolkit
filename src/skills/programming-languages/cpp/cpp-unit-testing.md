---
name: cpp-unit-testing
description: "Use for reviewing, designing, writing, or maintaining C++ unit tests. Covers RAII fixtures, exception safety, copy/move contracts, template types, lifetime checks, and targeted execution."
---

# C++ unit testing

## When to use

Use this skill for reviewing, designing, writing, or maintaining C++ unit tests.

## Scope and boundaries

Apply with the unit-test workflow. Keep production logic/interfaces unchanged unless explicitly authorized.

## Procedure

### Test

- Respect standard/compiler/platform, exception policy, and installed framework version. Reuse Google Test, Catch2, doctest, or project harness without stale boilerplate.
- Use RAII fixtures; join workers and restore injected state on assertion/exception paths.
- Assert actual copy/move contracts: copies need not be deep and moved-from objects need not be empty.
- Exercise promised no-throw/basic/strong exception guarantees using controlled throwing collaborators/allocators and observable rollback/cleanup.
- Compile-time traits can check declarations. Runtime no-throw assertions cannot prove `noexcept` is never violated; violations terminate and intentional termination requires isolated death/subprocess testing.
- Instantiate representative supported types, including move-only types where valid; arbitrary `void` instantiation is not meaningful coverage.
- Never dereference destroyed/invalidated objects. Use valid resource accounting or instrumentation for cleanup.
- Prefer behavior assertions; mock ordering only when contractual. Use floating-point tolerances justified by the contract.
- Keep uncontrolled wall-clock performance gates out of ordinary unit tests.

### Validate

Register/build/run affected targets and template instantiations in supported configurations; confirm cases actually executed.

Use supported instrumented ASan/UBSan or separate TSan when relevant; environment variables alone do not instrument binaries. Report exact checks and limitations; passing tools do not prove lifetime safety.
