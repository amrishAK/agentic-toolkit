---
name: integration-test-workflow
description: "Use when reviewing, designing, writing, or maintaining black-box integration tests. Covers real component boundaries, public contracts, dependency isolation, readiness, bounded waits, resource teardown, and targeted validation. Uses the language-specific skill matrix; not full-system E2E testing."
---

# Black-box integration-test workflow

## When to use

Use this skill when reviewing, designing, writing, or maintaining black-box integration tests.

## Scope and boundaries

Verify real components working together through their public contracts. Black-box describes how tests interact and assert, not a prohibition on reading source for planning or diagnosis. Integration tests need not launch the full application; complete deployed user journeys belong to a separate E2E workflow.

Use this skill with the [language-specific skill matrix](../programming-languages/references/programming-language-matrix.md)'s **Integration testing** guidance for the relevant languages. It is self-contained and does not require the unit-test or code-quality skills.

## Procedure

### 1. Define the boundary and scope

- Identify review/design versus test-writing intent. Review-only work must not edit or create tracking artifacts; explicitly requested writing or combined work may proceed directly.
- Read requirements, public APIs, relevant implementation, callers, existing tests, and configuration. Use intended contracts as the oracle, not merely current behavior.
- State the entry point, real components involved, boundary being verified, and dependency arrangement. A public API test that substitutes all meaningful collaborators may be a unit test, not integration coverage.
- Exercise supported public interfaces. Do not include private implementation files, bypass visibility, expose internals, or assert private counters or incidental call ordering to obtain coverage.
- Define the observable outcomes: responses, documented errors, events, public queries, or persisted artifacts. Inspect storage details only when those details themselves are a documented external contract.
- Keep changes to tests, fixtures, necessary test registration, and directly related test documentation. Do not change production logic, public interfaces, dependencies, or shared infrastructure without explicit authorization.
- Preserve unrelated work and ask only when material behavior, scope, or resource-safety decisions cannot be established.

### 2. Choose realistic dependencies

- Use real implementations across the boundary under test. For database-driver integration, for example, use the supported real database rather than a fake driver.
- Use controlled substitutes for dependencies outside that boundary when necessary for isolation or failure control. State what they replace and what compatibility claims they cannot support.
- Reuse existing test infrastructure and supported dependency versions. In-memory substitutes do not prove equivalence to another engine or deployed configuration.
- Prefer local, hermetic environments where feasible. Do not access production services, public networks, credentials, or shared user data without explicit authorization.
- If required infrastructure is unavailable, report the run as blocked or skipped under the project's explicit policy, not as verified behavior. Do not silently switch to mocks or turn missing prerequisites into passing tests.

### 3. Select contract-driven scenarios

- Cover meaningful component interactions: successful flows, boundary inputs, defined failures, error propagation, state consistency, persistence/reopen behavior, and recovery where promised.
- Overlap with unit tests is useful when it verifies different wiring or real dependency semantics. Avoid duplication that adds no confidence.
- Use documented expectations or independently derived properties, not the same algorithm under test to generate expected outputs.
- Keep fixtures small and readable, with descriptive scenario names and clear Arrange/Act/Assert structure. Multi-step interactions are appropriate.
- Do not impose arbitrary coverage thresholds, test counts, integration/unit ratios, or latency gates; follow explicit project requirements.
- Do not deliberately invoke undefined behavior or exhaust real system resources. Use supported isolated boundary-level failure controls; explain unreachable failure scenarios rather than adding invasive production hooks.
- Keep full-system E2E, stress, security-audit, and benchmark work separate unless explicitly requested.

### 4. Isolate and manage resources

- Allocate test-owned temporary directories, databases/schemas, ports, processes, and service instances. Use unique namespaces for parallel runs and avoid global environment or working-directory changes where possible.
- For transactions, verify that tested code shares the transaction before claiming rollback provides isolation. Use separate namespaces where it does not.
- Bind dynamically allocated ports where supported; avoid choosing a supposedly free port and racing another process.
- Establish readiness with bounded health checks or synchronization. Use deadlines for startup, operations, and shutdown rather than fixed sleeps.
- Distinguish bounded polling for documented eventual consistency from rerunning failed tests. Preserve final diagnostics on timeout; do not hide failures with retries.
- Clean up on success and failure using framework/language-appropriate teardown. Await or join workers and terminate only test-owned processes.
- Never delete broad directories, reset shared databases, or stop processes by name. Cleanup must target known test-owned resources.
- Capture useful logs, exit statuses, and dependency details without exposing secrets. Report teardown errors without masking the primary failure.

### 5. Diagnose and validate

- Diagnose contract failures, fixture defects, production bugs, and environmental failures separately. Do not weaken assertions, disable cases, or add retries just to obtain a green run.
- Preserve correct regressions when production fixes are outside scope; report the failure and required correction.
- Register tests in the existing harness and build the affected production components in supported modes.
- Execute the narrowest relevant integration selection and verify intended scenarios actually ran. Zero selected tests or a run containing only skipped scenarios does not validate the requested behavior.
- Broaden testing when shared fixtures, configuration changes, or observed failures warrant it. Use existing supported instrumentation when relevant, not as a mandatory checklist.
- State which configurations were exercised. Passing a local run does not certify every compiler, dependency version, feature, or platform.

### 6. Report

For reviews, provide concrete gaps or defects with file/item references, impact, and proposed scenarios. For applied work, report:

- Boundary and public entry points tested.
- Real components/dependencies and any substitutes.
- Scenarios added or updated and files changed.
- Exact build/test commands, executed scenario results, and any skips.
- Infrastructure, cleanup, and validation limitations.
- Whether a regression was demonstrated against the prior buggy behavior, when applicable.

Never claim a build, integration, compatibility, or safety result that was not actually verified.
