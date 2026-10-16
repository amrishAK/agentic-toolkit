---
name: csharp-unit-testing
description: "Use for reviewing, designing, writing, or maintaining C# unit tests. Covers contract assertions, async behavior, deterministic time and concurrency, disposal, and targeted .NET test execution."
---

# C# unit testing

Apply with the unit-test workflow. Keep production logic and interfaces unchanged unless explicitly authorized.

## Test

- Respect the supported SDK, target framework, language version, and installed test framework/version. Reuse the project's xUnit, NUnit, MSTest, or other established tooling rather than introducing a framework by default.
- Test observable behavior and documented contracts, including boundaries, validation, state transitions, and meaningful exception types or properties. Assert message text only when it is contractual.
- Keep test names and cases descriptive. Use parameterized tests for meaningful input variation without obscuring which behavior failed.
- Exercise synchronous and asynchronous outcomes correctly: await operations, assert failures through framework-supported async assertions, and verify cancellation only where the contract supports it.
- Prefer injected clocks, controlled schedulers, synchronization primitives, or bounded waits over sleeps. Avoid timing-sensitive assertions and uncontrolled worker lifetimes.
- Dispose test-owned `IDisposable`/`IAsyncDisposable` resources reliably, including fixture setup failures. Await asynchronous teardown where required.
- Isolate static state, environment, culture, current directory, and other process-wide settings; restore mutations and account for test parallelization.
- Use fakes or mocks at true external boundaries. Do not mock the behavior under test or assert incidental call ordering unless the contract requires it.
- Use property-based testing or generated cases only when supported by the project and when they improve meaningful contract coverage. Avoid brittle implementation-coupled assertions.

## Validate

Select the configured solution/project, target framework, test framework, and filter. Run the intended tests and confirm they executed; a successful command with zero selected tests is not validation.

Use the project's formatting, analyzer, and coverage tools when relevant. Report exact commands, target frameworks, results, and unavailable configurations; passing tests do not prove the absence of defects.
