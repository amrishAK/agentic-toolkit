---
name: unit-test-workflow
description: "Use when reviewing, designing, writing, updating, or fixing unit tests. Provides contract-driven test selection, readable fixtures, deterministic execution, controlled test doubles, regression protection, and targeted validation. Uses the language-specific skill matrix for language guidance."
---

# Unit-test workflow

## When to use

Use this skill when reviewing, designing, writing, updating, or fixing unit tests.

## Scope and boundaries

Use this workflow with the [language-specific skill matrix](../programming-languages/references/programming-language-matrix.md)'s **Unit testing** guidance for the relevant languages. It complements the code-quality workflow with testing-specific procedures; it does not require loading that skill or authorize production-code changes.

Unit tests are the default first test tier for isolated implementation tasks in the [test-driven implementation workflow](../implementation/test-driven-implementation-workflow.md). Write and run the focused behavior test before an authorized production change; coordinate with the implementer when production edits are outside this role's scope. Real component interactions or complete journeys may need a different tier to drive TDD.

## Procedure

### 1. Establish the intended contract

- Identify review/design versus test-writing scope. Review-only requests must not edit; explicit writing or combined requests can proceed without redundant confirmation.
- Read requirements, public contracts, relevant implementation/callers, existing tests, and test configuration. Current implementation is evidence, not automatically the correct specification.
- Distinguish defined rejection behavior from violated preconditions and undefined behavior. Ask when a material expectation cannot be established.
- Reuse the existing framework, naming, fixtures, language standard/MSRV, and test registration. Avoid unrelated changes and new dependencies.
- Keep production logic and public interfaces unchanged unless explicitly authorized. Necessary test-target registration and fixtures are in scope.

### 2. Select meaningful scenarios

- Map important behavior to normal cases, boundaries, defined errors, state transitions, and regression conditions. Prioritize risk and observable contracts, not one test for every method.
- For a regression, reproduce the relevant triggering condition and assert the intended outcome. Demonstrate failure on the buggy behavior when feasible without destructive changes; otherwise report that this was not verified.
- Test properties and valid sequences when they add confidence. Do not make production-sized allocations or exhaust real shared resources to reach limits.
- Avoid arbitrary test counts, unit/integration ratios, speed limits, or coverage percentages. Honor explicit project gates and use coverage to identify meaningful gaps, not as proof of correctness.
- Keep unit, integration, diagnostic, stress, and performance scopes distinct. Recommend broader tests when unit isolation cannot validate the relevant contract.

### 3. Write readable, reliable tests

- Name tests by behavior using repository conventions. Keep Arrange/Act/Assert clear without mandatory phase comments or a rigid single-call rule.
- One coherent scenario per test; multiple assertions are appropriate when they jointly establish that scenario.
- Prefer small explicit fixtures over elaborate builders. Share setup only when it improves clarity; some duplication is better than obscuring intent.
- Use precise assertions with helpful failure context. Do not derive expected values by repeating the same algorithm under test.
- Keep tests independent of execution order, incidental representation, noncontractual message text, and unspecified outcomes.
- Clean up resources and restore modified state even when assertions fail, using framework- and language-appropriate facilities.

### 4. Control dependencies and nondeterminism

- Prefer real fast, deterministic collaborators where practical. Use fakes/stubs to control costly or nondeterministic boundaries; use mocks when interactions themselves form part of the contract.
- Do not mock every dependency or impose new production abstractions just for tests. Use existing injection seams and explain limitations when no suitable seam exists.
- Inject failures locally rather than exhausting memory, replacing process-wide allocators, or altering real services. Use unique temporary resources and never mutate shared user data.
- Prefer synchronization and controlled clocks over sleeps. Bound potentially hanging operations and ensure worker cleanup; do not hide failures with retries.
- Seed random inputs and preserve reproduction details. Repeated runs and sanitizers can expose issues, but cannot prove determinism or race freedom.
- Do not intentionally invoke undefined behavior in ordinary tests. Any diagnostic/death testing needs supported isolated infrastructure and an explicit purpose.

### 5. Diagnose failures without weakening contracts

- Determine whether a failure is a test defect, production bug, environment problem, or ambiguous specification.
- Correct wrong tests only when supported by the intended contract. Do not delete assertions, loosen expectations, ignore tests, or add retries merely to make a run green.
- When a correct regression test fails because production fixes are outside scope, report the failure and minimal required production correction rather than silently changing behavior.

### 6. Validate and report

- Build and execute the smallest relevant selection using existing project tooling. Confirm new tests are registered and the intended cases actually executed; zero matching tests is not a pass for the requested behavior.
- Broaden runs when shared fixtures, configuration changes, or failures warrant it. Use supported coverage or instrumentation only when relevant; do not install tooling simply to complete a checklist.
- Review the final diff for production changes, accidental churn, incomplete examples, and test weakening.
- For reviews, report concrete gaps or defects with file/item references, impact, and proposed scenarios; distinguish evidence from assumptions.
- For applied changes, report behaviors covered, files changed, exact commands and results, failing regressions, and unavailable checks. State whether pre-fix failure was demonstrated.
- Never claim a test, coverage threshold, sanitizer check, or performance result was verified unless it actually ran and supported the claim.
