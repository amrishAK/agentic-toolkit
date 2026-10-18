---
name: csharp-integration-testing
description: "Use for black-box C# integration test review, design, or implementation. Covers public .NET boundaries, real component interactions, dependency setup, async lifecycle, and execution."
---

# C# integration testing

## When to use

Use this skill for black-box C# integration test review, design, or implementation.

## Scope and boundaries

Apply with the integration-test workflow. Preserve production behavior and public interfaces unless explicitly authorized.

## Procedure

### Test

- Respect the supported SDK, target frameworks, test framework, platform, and integration-test conventions.
- Exercise real components through public APIs and configured dependency-injection or hosting boundaries. Do not expose internals or add test-only production APIs to bypass the boundary.
- Use isolated test-owned databases, directories, ports, queues, and credentials. Do not connect tests to production or shared mutable data.
- Assert externally observable results, persisted state, and documented error behavior. Keep substitutes outside the integration boundary and identify them accurately.
- Use readiness checks and bounded waits for services and background work; avoid sleeps as readiness checks. Await worker completion and cancellation.
- Dispose service providers, hosts, clients, streams, database connections, and other resources. Ensure teardown also runs after assertion failures and asynchronous operations finish.
- Respect parallel execution. Avoid process-wide environment or static-state changes unless controlled and restored; isolate any resource that cannot safely be shared.
- Keep full user journeys across the deployed application boundary in end-to-end testing rather than labeling them component integration.

### Validate

Build the real components and registered test targets for the intended framework(s). Run the selected cases, confirm dependencies became ready and scenarios executed, and report substitutes and cleanup status.

Missing infrastructure, zero matches, and only-skipped tests are not passing validation. Report exact commands, results, and untested platforms or framework configurations.
