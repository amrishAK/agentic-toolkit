---
name: cpp-integration-testing
description: "Use for black-box C++ integration test review, design, or implementation. Covers public headers, real components, RAII fixtures, cross-component exception/lifetime contracts, templates, and actual execution."
---

# C++ integration testing

## When to use

Use this skill for black-box C++ integration test review, design, or implementation.

## Scope and boundaries

Apply with the integration-test workflow. Preserve production behavior/interfaces unless explicitly authorized.

## Procedure

### Test

- Respect standard/compiler/platform/ABI, exception policy, and installed framework version.
- Link real components through public headers; do not bypass encapsulation or add friends solely for black-box tests.
- Use RAII storage/handle fixtures and reliable explicit worker shutdown that survives assertions/exceptions.
- Assert contractual exception propagation and cross-component state consistency; respect no-exceptions builds and C-facing boundaries.
- Observe ownership/lifetime through valid public operations. Never inspect destroyed objects or assume moved-from emptiness.
- Exercise representative supported public template APIs without replacing the meaningful production implementation with mock specializations.
- Keep uncontrolled wall-clock benchmarks and full application journeys outside ordinary integration scope.

### Validate

Build real components, relevant template instantiations, and registered targets. Verify readiness and actual executions.

Use supported instrumented ASan/UBSan or separate TSan where relevant. Report real dependencies/substitutes, missing prerequisites, results, and cleanup limitations. No infrastructure or only skipped cases is not a validated scenario.
