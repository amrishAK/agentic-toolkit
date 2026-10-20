---
name: test-driven-implementation-workflow
description: "Use for feature-to-task implementation planning and test-driven development (TDD): acceptance-criteria mapping, blocker questions, unit-first red-green-refactor tasks, integration-oriented feature validation, and review before completion."
---

# Test-driven implementation workflow

## When to use

Use this skill when implementing a feature, fix, or behavior change from an agreed feature contract or a bounded request. Scale the plan to the work; a small fix does not require a feature document. Do not use it for review-only work or diagnosis that does not include an authorized implementation.

## Scope and boundaries

This workflow owns implementation planning and the test-first implementation cycle. The active role retains authorization, language-specific correctness guidance, and review requirements. It does not authorize production edits for test-only roles, implementation during discussion or review, substantial feature-contract redesign, or delivery actions.

Treat the feature document as the source of intended behavior, not as proof of implementation. Keep unresolved product and contract decisions with their decision owner; use `feature-designer` for substantial contract changes. Reuse existing testing roles and their workflows rather than requiring a specialist handoff for every task.

## Procedure

### 1. Establish the implementation input

- Read the feature document and acceptance criteria when supplied, relevant project rules, existing implementation, callers, tests, and tooling. For a bounded request without a feature document, establish the expected behavior and verification directly from the request and authoritative project evidence.
- Identify scope, exclusions, supported configurations, real component boundaries, existing behavior to preserve, and reusable helpers. Distinguish accepted requirements from proposals and unresolved decisions.
- Surface missing criteria and contradictions before implementing affected behavior; do not silently choose public behavior or rewrite the contract to match current code.

### 2. Break the work into testable tasks

- Present a concise implementation plan before production edits. Prefer small observable behavior slices, not separate batches for all tests and all production code.
- Give each task an ID, intended outcome, acceptance-criterion references where available, dependencies, planned scenarios and test tier, blocking questions, and completion evidence. Identify the first ready task; track pending, active, completed, or blocked state through the project's existing task mechanism or the conversation.
- Plan normal cases, boundaries, defined errors, and regression conditions. Include feature-level component interactions and critical complete journeys from the outset, not only after implementation.
- Keep the plan distinct from the feature contract. Use the project's established planning location when adopted; do not create a separate plan file or tracker unless requested or required by project rules.

### 3. Resolve questions before affected work

- Present specific material questions with the affected task or criterion, who must decide, and when the answer is needed. Use the client's interactive question tool when available.
- Resolve blockers before the affected task starts. Do not invent thresholds, alter scope, or infer approval from a handoff. Unaffected ready tasks may proceed when independently useful and already authorized.
- Record agreed contract answers in the authoritative feature document when authorized; otherwise hand them to its owner and report the dependency. Update the plan to reflect the decision rather than keeping a competing answer.
- When no material questions remain and implementation is already authorized, state that and proceed. A planning-only request stops at the plan and questions; do not add a generic approval round to an authorized implementation request.

### 4. Implement one ready task through red-green-refactor

Repeat this short cycle for each behavior within the task:

1. **Red:** Add or update a focused test for the next required behavior before changing production code. Register and run it with the existing runner. Confirm it fails because the behavior is missing or wrong; unrelated build/setup failures, zero selected tests, and skipped cases do not establish red.
2. **Green:** Write the simplest correct production change that makes that test pass. Preserve existing contracts and error handling; do not weaken the test, hard-code fixture answers, or add unrelated abstractions.
3. **Refactor:** Improve cohesion, names, duplication, and dependency seams while keeping behavior unchanged. Prefer small modules with clear responsibilities and established public interfaces; do not expose private state or create speculative layers merely to make tests easy.
4. **Check:** Rerun the focused tests after refactoring and the affected regression selection before completing the task. Update its state and evidence, then select the next ready task.

Use [unit tests](../testing/unit-test-workflow.md) first by default for isolated behavior. If the required behavior is inherently a real component interaction or complete application journey, a focused [integration test](../testing/integration-test-workflow.md) or [E2E test](../testing/e2e-test-workflow.md) can drive the cycle instead. Select by observable behavior and boundary, not by development stage; do not replace meaningful real interactions with mocks just to call the test a unit test.

For regressions, demonstrate the expected failure before the fix when safe. If existing tests already verify the behavior, reuse them; if a meaningful red-green cycle cannot be demonstrated, explain why and report the alternative evidence without claiming TDD occurred. Documentation-only, behavior-preserving, and infrastructure changes use applicable existing checks rather than artificial failing tests. Missing tooling or infrastructure is a blocker or explicit limitation, never a passing result.

### 5. Validate the complete feature

- Map every in-scope acceptance criterion to executed verification evidence or an explicit unmet, blocked, or unverified outcome. Completing task tests alone does not establish feature acceptance.
- Use integration tests as the primary evidence for behavior spanning real components through public interfaces, including relevant error propagation, lifecycle, persistence, and recovery contracts. Keep unit coverage for isolated rules.
- Run critical E2E journeys when acceptance depends on the complete CLI, UI, or network workflow. Do not defer necessary feature-acceptance evidence until release or require every feature to exercise every test tier.
- Run affected builds and project checks, broaden regression selections when shared changes or observed failures warrant it, and update directly related documentation and evidenced implementation state without changing agreed intent.
- Keep release validation separate and broader than E2E. When release work is requested, follow the [release workflow](../build-and-delivery/release-workflow.md) for applicable regression suites, artifacts, installation, compatibility, migration, provenance, and project-specific gates. Feature acceptance does not approve a release.

### 6. Review, correct, and report

- Self-review the task changes against the contract, test quality, module boundaries, and scope. Follow the active role's independent implementation-review requirement; a review handoff must include the relevant changes, criteria, and verification evidence.
- Assess findings, fix applicable in-scope issues, rerun affected checks, and obtain re-review as required by the role. Report unavailable review, unresolved decisions, and blockers; do not claim the review loop is complete without evidence.
- Report completed and remaining tasks, acceptance-criterion evidence, whether expected red and green were actually observed, exact checks/results, review status, and limitations. Distinguish implemented from verified behavior.
- Finalization means an evidence-backed completion report, not automatic staging, commit, push, publication, or independent readiness approval.
