---
name: code-quality-workflow
description: "Use when reviewing, implementing, fixing, or refactoring code to apply a shared Clean Code/SOLID workflow, evidence-based findings, focused changes, regression tests, and honest validation reporting. Complements language-specific guidance selected through the programming language catalogue."
---

# Code quality workflow

Use this workflow with the [programming language catalogue](../programming-languages/programming-language-catalog.md)'s **Code quality** guidance for the relevant languages. Language correctness, safety, and supported toolchains take precedence over design heuristics. This skill does not replace project instructions or authorize edits on a review-only request.

## 1. Establish scope and constraints

- Identify whether the task is review-only, implementation, or both. Review-only work must not edit source or create caches or tracking artifacts.
- Read the relevant code, callers, tests, and project guidance. Identify the selected language version, toolchain/runtime floor, target configuration, platform requirements, public contracts, and existing patterns.
- Preserve unrelated work. Ask a focused question only when a material behavior or design choice cannot be safely inferred.
- Reuse established helpers and conventions. Do not introduce a dependency, upgrade a standard, or change an API/ABI merely to follow a newer idiom.

## 2. Apply Clean Code and SOLID pragmatically

- Choose names that convey domain meaning and keep functions/modules cohesive. Single responsibility concerns meaningful reasons for change, not how many steps a function performs.
- Prefer explicit contracts, straightforward control flow, and intentional error handling. Do not impose arbitrary limits on function length, nesting, or parameter counts.
- Keep APIs narrow and dependencies clear. Introduce abstraction where it addresses a demonstrated boundary, reuse, variation, or testability need.
- Open/closed is not a ban on editing code or using branching. Preserve documented contracts for interchangeable implementations; do not strengthen preconditions or weaken postconditions.
- Keep interfaces cohesive and avoid forcing clients to depend on unrelated operations. Dependency inversion is not a mandate to add an interface for every concrete type.
- Share genuinely common concepts without premature DRY abstractions. Avoid speculative frameworks and needless layers.
- Evaluate boolean and output parameters in context rather than treating them as automatic defects.
- Comments explain intent, invariants, ownership, safety, and non-obvious decisions. Accurate public API documentation remains important even when the implementation looks simple.

## 3. Review with evidence

- Apply relevant language-specific checks and trace suspected issues through callers and error paths. Prefer concrete triggering conditions over speculation.
- For diff reviews, focus on introduced or tightly coupled issues; label pre-existing issues separately.
- Report findings ordered by impact, each with severity, precise file/line references, triggering condition, practical impact, and a focused recommendation.
- Distinguish correctness defects from maintainability recommendations and personal preferences.

| Severity | Meaning |
|---|---|
| Critical | Demonstrated severe memory corruption, undefined behavior, or data-race risk with major impact |
| High | Significant incorrect behavior, resource loss, or failure-handling defect |
| Medium | Concrete maintainability, API, or reliability problem with explained impact |
| Low / recommendation | Minor clarity or consistency improvement, distinct from a correctness defect |

State review scope, checks performed, and remaining uncertainty. If no actionable findings are identified, say so without implying the code is proven correct. An ordinary code review is not a complete security audit.

## 4. Implement focused changes

- For implementation or combined requests, briefly identify key issues or design choices, then apply the requested changes without redundant confirmation.
- Make the smallest complete change. Preserve behavior and public contracts unless changing them is part of the request.
- Update affected callers and directly related documentation. Add focused tests for changed behavior, regression conditions, boundaries, and important error paths.
- Review the diff for unintended behavior, unnecessary complexity, formatting churn, and unrelated edits.

## 5. Validate and report

- Use existing build, formatting, test, and analysis tooling. Run the narrowest checks that actually cover the change, including affected compilation targets; broaden when evidence warrants it.
- Follow the language-specific agent and repository guidance for commands and supported tools. Do not guess commands from unrelated ecosystem files or impose artificial short build timeouts.
- Install or restore dependencies only when required by an intentional manifest change or a missing-dependency failure. Do not add analysis tooling merely to complete a checklist.
- Fix validation failures caused by the change. Explicitly report unrelated failures and unavailable checks; do not swallow errors or claim success without execution.
- Evaluate efficiency in context: complexity, allocations, copies, and contention. Lower asymptotic complexity is not automatically faster or simpler.
- Measure claimed performance improvements with representative workloads when practical. Otherwise state that performance is unmeasured.
- Finish with changes made, important design decisions, exact validation commands/results, and remaining limitations. Passing tests or analysis does not prove absence of bugs.
