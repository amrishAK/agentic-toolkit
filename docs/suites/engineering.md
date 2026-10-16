# Engineering suite

The engineering suite provides reusable guidance for software planning, implementation, testing, documentation, build automation, performance work, and review. The [engineering skill catalogue](../../src/suites/engineering/skills/skill-catalog.md) owns category-level task routing and shared skill selection. The [programming language catalogue](../../src/suites/engineering/skills/programming-languages/programming-language-catalog.md) owns language coverage and language-specific routing; some roles, such as end-to-end testing and technical documentation, are language-independent.

Browse the [agent definitions](../../src/suites/engineering/agents/) and [categorized skills](../../src/suites/engineering/skills/). These are maintained Markdown sources, not an installed client registry. See [usage and compatibility](../../README.md#usage-and-compatibility) before adapting them to a client.

## Start with a task

If you know the work but not the role, use one of these entry points. Follow the linked workflow and any handoff as needed; this is navigation guidance, not automatic routing.

| Task | Starting point | Guidance or handoff |
|---|---|---|
| Fix a bug | [code-engineer](../../src/suites/engineering/agents/code-engineer.md) | Use the [debugging workflow](../../src/suites/engineering/skills/implementation/debugging-workflow.md) to investigate; implementation follows when authorized. |
| Diagnose a build or CI failure | [build-automation-agent](../../src/suites/engineering/agents/build-automation-agent.md) | Use the [debugging workflow](../../src/suites/engineering/skills/implementation/debugging-workflow.md), then the relevant [build](../../src/suites/engineering/skills/build-and-delivery/build-system-workflow.md) or [CI](../../src/suites/engineering/skills/build-and-delivery/ci-workflow.md) workflow. |
| Design a feature | [feature-designer](../../src/suites/engineering/agents/feature-designer.md) | Use the [feature-design workflow](../../src/suites/engineering/skills/design-and-planning/feature-design-workflow.md); hand agreed contracts to [code-engineer](../../src/suites/engineering/agents/code-engineer.md) for implementation. |
| Test interactions across components | [integration-tester](../../src/suites/engineering/agents/integration-tester.md) | Use the [integration-test workflow](../../src/suites/engineering/skills/testing/integration-test-workflow.md) and the relevant entries in the [programming language catalogue](../../src/suites/engineering/skills/programming-languages/programming-language-catalog.md). |

## Choose a role

| Agent | Use for | Important boundary |
|---|---|---|
| [product-planner](../../src/suites/engineering/agents/product-planner.md) | Product intent, priorities, roadmap, release goals, and acceptance requirements | Does not implement production code or decide detailed feature contracts |
| [feature-designer](../../src/suites/engineering/agents/feature-designer.md) | Requirements, public contracts, edge cases, architecture trade-offs, and implementation handoffs | Does not implement production code |
| [code-engineer](../../src/suites/engineering/agents/code-engineer.md) | Implementation, debugging, fixes, and refactoring | Implementation self-review is not independent readiness approval |
| [unit-tester](../../src/suites/engineering/agents/unit-tester.md) | Focused unit tests, boundaries, errors, and cleanup | Does not silently change production behavior to make tests pass |
| [integration-tester](../../src/suites/engineering/agents/integration-tester.md) | Real component interactions through public interfaces | Does not replace component integration with mocks or call it full-system E2E |
| [e2e-tester](../../src/suites/engineering/agents/e2e-tester.md) | Complete application journeys through browser, CLI, or external network interfaces | Uses isolated test-owned resources; infrastructure changes need authorization |
| [benchmark-engineer](../../src/suites/engineering/agents/benchmark-engineer.md) | Reproducible measurements, benchmark implementation, and performance reports | Workload execution needs an authorized scope and budget; measurements are not release approval |
| [build-automation-agent](../../src/suites/engineering/agents/build-automation-agent.md) | Make/CMake, native build orchestration, GitHub Actions, and containers | Publishing, deployment, remote workflow execution, and delivery need explicit authorization |
| [source-documentation-writer](../../src/suites/engineering/agents/source-documentation-writer.md) | Source API documentation, comments, and safety explanations | Comments-only work, not production logic or standalone guides |
| [technical-documentation-writer](../../src/suites/engineering/agents/technical-documentation-writer.md) | README, architecture, setup, user/developer guides, and runbooks | Does not silently make product or feature decisions |
| [project-standardizer](../../src/suites/engineering/agents/project-standardizer.md) | Confirmed repository structure, guidance, licensing, ignore rules, and baseline documentation | Uses an interview for unresolved setup decisions; does not modify personal installations |
| [change-reviewer](../../src/suites/engineering/agents/change-reviewer.md) | Per-commit, pre-PR, and per-release readiness assessment | Read-only review; selected corrections are delegated, never edited directly; existing PR review is out of scope |
| [security-reviewer](../../src/suites/engineering/agents/security-reviewer.md) | Authorized source security review and threat modeling | No command execution, active probing, or direct edits; selected fixes require editing-subagent delegation |

Product planning currently lives in this suite as part of software delivery. Its presence does not imply a separate product suite exists.

## Skill categories

Agents define responsibilities and boundaries. Skills provide reusable methods that an agent loads or reads when relevant; their linked references supply supporting detail. Do not load every skill for every task.

Use the [engineering skill catalogue](../../src/suites/engineering/skills/skill-catalog.md#task-workflows-by-category) to choose workflows across all categories and shared guidance. It is the canonical category-level inventory; this guide owns role selection and handoffs. Agents continue to name mandatory workflows explicitly, then use the catalogue when additional task guidance is needed.

Language-specific skills complement the task workflow. An integration-test task uses the [integration-test workflow](../../src/suites/engineering/skills/testing/integration-test-workflow.md) and the [programming language catalogue's](../../src/suites/engineering/skills/programming-languages/programming-language-catalog.md#skill-matrix) **Integration testing** entries for the relevant languages. For a mixed-language boundary, use the relevant language guidance for each side.

To add a category-level skill, update the engineering skill catalogue. To add a language, maintain its skills and update the programming language catalogue rather than editing each agent's description or routing table. Agents consult the language catalogue for the task column appropriate to their role. Both catalogues are reference documents, not skill definitions, runtime registries, or installer manifests.

The [technical-documentation writer](../../src/suites/engineering/agents/technical-documentation-writer.md) uses [documentation requirements](../../src/suites/engineering/skills/documentation/documentation-requirements.md) to identify the document, its location, owner, and applicable rules, then applies [technical documentation guidance](../../src/suites/engineering/skills/documentation/technical-documentation-workflow.md) for evidence, writing, and validation. Documentation requirements is the document catalogue and rule selector used by any agent that reviews, writes, or updates a document; it is not a workflow. It owns the catalogue, ownership map, and document-type references; the technical-documentation workflow owns its guide-specific outlines. Project standards retain repository layout, feature tracking, and setup conventions.

Definitions use `<skill-name>.md` directly inside their category. Category-level reference filenames carry the owning skill's prefix; keep their links and ownership intact when moving content.

## Shared guidance

The suite links to shared definitions rather than maintaining copies:

- [Output standardization](../../src/shared/skills/agent-output-standardization.md) covers clear responses, numbered findings, stable finding IDs, and matching [response templates](../../src/shared/skills/templates/).
- [Change delivery](../../src/shared/skills/change-delivery-workflow.md) covers explicit selected-fix handoffs and separately authorized parent-only delivery actions.

Shared guidance does not override task-specific reporting requirements or grant tools, editing permission, or publication authority.

## Task flow and approvals

For a substantial feature, the roles can hand off product intent to detailed design, then implementation and relevant testing/documentation, followed by independent readiness review. This is a navigation pattern, not an implemented orchestrator or a requirement to invoke every specialist for a small change. The user or coordinating session selects the necessary roles.

A review alone produces findings without edits. Findings retain sequential IDs; an explicit selection such as `apply 1,2` authorizes only the selected corrections and their necessary tests or documentation. Delegation-enabled reviewers launch appropriate editing subagents, wait for results, and re-review the affected scope. If the host cannot support delegation or nesting, the reviewer reports the blocker and hands off rather than editing directly.

Implementation-capable specialists follow their own mode boundaries. No handoff or apply selection implicitly authorizes staging, commits, pushes, releases, deployment, or changes to a personal installation.

## Validation and limitations

Use the [repository maintenance checklist](../../README.md#validation) when changing these sources. Preserve role boundaries, names, descriptions, local links, heading anchors, and complete resource inclusion.

The suite describes tests and build workflows in consuming software projects; those definitions do not supply this repository with a compiler requirement, CI pipeline, or benchmark harness. The separate [Copilot installer](../installation.md) has regression tests through `make check`. Source inspection, link checks, and installer tests do not prove client discovery, skill loading, tool permissions, delegation, model behavior, or cross-client compatibility. Other client adapters remain deferred.
