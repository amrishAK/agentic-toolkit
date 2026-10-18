---
name: e2e-test-workflow
description: "Use when reviewing, designing, writing, updating, or diagnosing black-box end-to-end application tests through browser UI, CLI, or external network interfaces. Covers complete journeys, environment safety, real infrastructure, isolation, reliable waits, failure evidence, and reproducible validation."
---

# End-to-end test workflow

## When to use

Use this skill to design or review black-box tests of complete user-visible application journeys.

## Scope and boundaries

Verify complete user-visible journeys through a running application and the infrastructure required for those journeys. E2E scope is defined by the journey and system boundary, not by the number of services or implementation language. This workflow is self-contained; component integration and unit tests remain separate.

## Procedure

### 1. Define the journey and oracle

- Establish review/design versus test-writing scope. Review-only requests must not edit; explicit writing and combined requests may proceed directly.
- Read requirements, application interfaces, existing E2E tests, fixtures, runner configuration, and project guidance. Current behavior is evidence, not automatically the correct specification.
- Identify the actor, preconditions, external entry point, meaningful actions, and expected user-visible outcome. Select critical successful journeys and defined failure/recovery cases, not every unit-level edge case.
- Use public responses, UI state, CLI results, delivered test messages, or publicly queried persisted state as assertions. Do not assert private implementation details.
- Match project naming and keep Arrange/Act/Assert readable. Multi-step journeys are appropriate; avoid unnecessary inter-test dependencies.
- Keep changes to tests, fixtures, necessary registration, and related documentation. Ask before production, dependency, deployment, or infrastructure changes that are not explicitly authorized.

### 2. Verify environment safety

- Identify the application artifact/version, base URLs or executable, dependency versions, configuration, and required permissions before execution.
- Use local or explicitly authorized disposable environments. Confirm target identity and isolation before destructive actions; never infer safety solely from a hostname.
- Use test-owned accounts, data namespaces, directories, processes, and service instances. Never reset shared databases, delete broad directories, or stop unrelated processes.
- Prevent real payments, emails, messages, or other external side effects with supported sandbox endpoints or controlled substitutes. Do not expose credentials in logs, traces, screenshots, or committed fixtures.
- Do not install tooling or provision services merely to complete a checklist. Reuse documented infrastructure; report unavailable prerequisites or request necessary authorization.

### 3. Keep the journey real

- Exercise the actual running application and meaningful first-party components needed for the journey. Do not intercept core responses or call internal functions to simulate success.
- Use supported real dependencies where their semantics form part of the claimed coverage. Use controlled substitutes or provider sandboxes outside that boundary when necessary.
- State every relevant substitution and coverage limitation. A sandbox or emulator does not automatically certify production-provider compatibility.
- Use fixture APIs to establish preconditions, not to perform the action the scenario claims to test. Do not bypass authentication in a journey intended to validate login.
- Separate contract/provider compatibility tests, component integration, load testing, benchmarks, and security audits from ordinary E2E coverage.

### 4. Make setup and execution reliable

- Build/start the intended artifact or verify the existing authorized deployment. Check application and dependency readiness using bounded health checks, not fixed sleeps.
- Give each test independent state and unique names suitable for parallel execution. Reset permitted fixture state; avoid process-global environment or working-directory changes.
- Use runner-supported waits for observable conditions. For eventual consistency, poll within a defined deadline and retain final observations on timeout.
- Bound startup, actions, subprocess output collection, and teardown. Avoid deadlocks from unread stdout/stderr and do not leave workers or services running.
- Prefer accessible browser locators and project-approved stable identifiers. Assert outcomes, not incidental DOM layout, internal call order, or arbitrary timing.
- For CLI/protocol journeys, verify contractual exit/error responses and meaningful output or state; a status code alone rarely establishes the full journey.
- Use reproducible test data and justified comparisons. Treat unstable timestamps, ordering, locale, and floating-point expectations according to the actual contract.

### 5. Diagnose failures and clean up

- Capture relevant runner traces, screenshots, application logs, child-process output, exit status, and dependency diagnostics while redacting sensitive information.
- Separate test defects, production bugs, environmental failures, and ambiguous expectations. Preserve correct failing assertions; do not loosen or disable them to make runs green.
- Retries are not a fix. Follow any existing retry policy and report initial failures separately from later passes; never describe a retried pass as evidence of determinism.
- Ensure cleanup runs after assertion failures and timeouts. Gracefully stop and then, if necessary, terminate only specifically identified test-owned processes.
- Remove only known test-owned resources. Report teardown errors without hiding the original failure; retain bounded failure artifacts according to project policy.

### 6. Verify and report

- Register persistent automated tests and run the smallest relevant journey selection using the actual runner.
- Confirm selected scenarios executed. Zero matches, all-skipped runs, or missing required infrastructure are not verified behavior.
- Broaden execution when shared fixtures or evidence warrant it. Do not claim coverage of untested browsers, operating systems, feature sets, or deployments.
- State whether a regression failed on prior buggy behavior when feasible; never make destructive revisions merely to demonstrate this.
- For reviews, report concrete defects or journey gaps with file/item references, impact, and proposed scenarios.
- For applied work, report journeys and files changed, exact commands, artifact/environment identity, real dependencies and substitutes, executed results, retries/skips, cleanup status, and remaining limitations.
- Distinguish manual exploration from automated tests. Passing E2E tests does not establish performance, security, or universal correctness.
