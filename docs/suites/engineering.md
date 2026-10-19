# Engineering suite

The engineering suite provides reusable guidance for software planning, implementation, testing, documentation, build automation, performance work, and review. The shared [skill selection workflow](../../src/skills/agent-workflows/skill-selection-workflow.md) uses the Engineering [category-level selection matrix](../../src/skills/agent-workflows/references/skill-selection-workflow-matrix.md) for task routing. The [Engineering language-specific skill matrix](../../src/skills/programming-languages/references/programming-language-matrix.md) owns language coverage and language-specific routing; some roles, such as end-to-end testing and technical documentation, are language-independent.

Browse the [agent definitions](../../src/agents) and [categorized skills](../../src/skills). These are maintained Markdown sources, not an installed client registry. See [usage and compatibility](../../README.md#usage-and-compatibility) before adapting them to a client.

Agent sources are organized by function, independently of the [suite manifest](../../src/suites/engineering.yaml):

| Functional category | Agents |
|---|---|
| [Design and planning](../../src/agents/design-and-planning) | product-planner, feature-designer |
| [Implementation](../../src/agents/implementation) | code-engineer |
| [Testing](../../src/agents/testing) | unit-tester, integration-tester, e2e-tester |
| [Review and security](../../src/agents/review-and-security) | change-reviewer, security-reviewer |
| [Build and delivery](../../src/agents/build-and-delivery) | build-automation-agent |
| [Performance](../../src/agents/performance) | benchmark-engineer |
| [Documentation](../../src/agents/documentation) | source-documentation-writer, technical-documentation-writer |
| [Project standards](../../src/agents/project-standards) | project-standardizer |

The Engineering suite still selects these agents by name. Source categories do not change suite membership, agent responsibilities, or installed client paths.

Use the shared [engineering task workflow](../../src/skills/implementation/engineering-task-workflow.md) for common task framing and the [repository glossary](../reference/glossary.md) for canonical terminology. Roles describe responsibilities, not required headcount.

## Start with a task

If you know the work but not the role, use one of these entry points. Follow the linked workflow and any handoff as needed; this is navigation guidance, not automatic routing.

| Task | Starting point | Guidance or handoff |
|---|---|---|
| Fix a bug | [code-engineer](../../src/agents/implementation/code-engineer.md) | Use the [debugging workflow](../../src/skills/implementation/debugging-workflow.md) to investigate; implementation follows when authorized. |
| Diagnose a build or CI failure | [build-automation-agent](../../src/agents/build-and-delivery/build-automation-agent.md) | Use the [debugging workflow](../../src/skills/implementation/debugging-workflow.md), then the relevant [build](../../src/skills/build-and-delivery/build-system-workflow.md) or [CI](../../src/skills/build-and-delivery/ci-workflow.md) workflow. |
| Design a feature | [feature-designer](../../src/agents/design-and-planning/feature-designer.md) | Use the [feature-design workflow](../../src/skills/design-and-planning/feature-design-workflow.md); hand agreed contracts to [code-engineer](../../src/agents/implementation/code-engineer.md) for implementation. |
| Test interactions across components | [integration-tester](../../src/agents/testing/integration-tester.md) | Use the [integration-test workflow](../../src/skills/testing/integration-test-workflow.md) and the relevant entries in the [language-specific skill matrix](../../src/skills/programming-languages/references/programming-language-matrix.md). |

## Choose a role

| Agent | Use for | Important boundary |
|---|---|---|
| [product-planner](../../src/agents/design-and-planning/product-planner.md) | Product intent, priorities, roadmap, release goals, and acceptance criteria | Does not implement production code or decide detailed feature contracts |
| [feature-designer](../../src/agents/design-and-planning/feature-designer.md) | Requirements, public contracts, edge cases, architecture trade-offs, and implementation handoffs | Does not implement production code |
| [code-engineer](../../src/agents/implementation/code-engineer.md) | Implementation, debugging, fixes, and refactoring | Implementation self-review is not independent readiness approval |
| [unit-tester](../../src/agents/testing/unit-tester.md) | Focused unit tests, boundaries, errors, and cleanup | Does not silently change production behavior to make tests pass |
| [integration-tester](../../src/agents/testing/integration-tester.md) | Real component interactions through public interfaces | Does not replace component integration with mocks or call it full-system E2E |
| [e2e-tester](../../src/agents/testing/e2e-tester.md) | Complete application journeys through browser, CLI, or external network interfaces | Uses isolated test-owned resources; infrastructure changes need authorization |
| [benchmark-engineer](../../src/agents/performance/benchmark-engineer.md) | Reproducible measurements, benchmark implementation, and performance reports | Workload execution needs an authorized scope and budget; measurements are not release approval |
| [build-automation-agent](../../src/agents/build-and-delivery/build-automation-agent.md) | Make/CMake, native build orchestration, GitHub Actions, and containers | Publishing, deployment, remote workflow execution, and delivery need explicit authorization |
| [source-documentation-writer](../../src/agents/documentation/source-documentation-writer.md) | Source API documentation, comments, and safety explanations | Comments-only work, not production logic or standalone guides |
| [project-standardizer](../../src/agents/project-standards/project-standardizer.md) | Confirmed repository structure, guidance, licensing, ignore rules, and baseline documentation | Uses an interview for unresolved setup decisions; does not modify personal installations |
| [change-reviewer](../../src/agents/review-and-security/change-reviewer.md) | Per-commit, pre-PR, and per-release readiness assessment | Read-only review; selected corrections are delegated, never edited directly; existing PR review is out of scope |
| [security-reviewer](../../src/agents/review-and-security/security-reviewer.md) | Authorized source security review and threat modeling | No command execution, active probing, or direct edits; selected fixes require editing-subagent delegation |

Product planning currently lives in this suite as part of software delivery, through the `product-planner` role. The proposed V2 Product Management stage is not a currently maintained suite and does not rename or replace that role.

An Engineering feature contract captures detailed intended behavior, edge cases, and failure behavior; it is distinct from the product-level feature briefs proposed for a future Product Management stage. Use **acceptance criteria** for observable conditions and **acceptance examples** for illustrative cases.

## Skill categories

Agents define responsibilities and boundaries. Skill definitions provide reusable methods and linked references supply supporting detail. Select only guidance relevant to the task; invoke a skill through the client only when supported, otherwise read its maintained source.

Use the [skill selection workflow](../../src/skills/agent-workflows/skill-selection-workflow.md) and the Engineering [category-level selection matrix](../../src/skills/agent-workflows/references/skill-selection-workflow-matrix.md#task-specific-skills) to choose workflows across categories. The matrix is the canonical Engineering category-level inventory; this guide owns role selection and handoffs. Agents continue to name mandatory workflows explicitly, then use the selection workflow when additional task guidance is needed.

Language-specific skills complement the task workflow. An integration-test task uses the [integration-test workflow](../../src/skills/testing/integration-test-workflow.md) and the **Integration testing** entries in the [language-specific skill matrix](../../src/skills/programming-languages/references/programming-language-matrix.md) for the relevant languages. For a mixed-language boundary, use the relevant language guidance for each side.

To add an Engineering category-level skill, update the category-level skill selection matrix. To add a language, maintain its skills and update the language-specific skill matrix rather than editing each agent's description or routing table. Agents consult the language matrix for the task column appropriate to their role. These matrices are reference documents, not skill definitions, runtime registries, or installer manifests.

The shared [technical-documentation-writer](../../src/agents/documentation/technical-documentation-writer.md) reviews, writes, and updates README files, architecture docs, setup, user/developer guides, and runbooks. It uses the shared [documentation selection workflow](../../src/skills/documentation/documentation-selection-workflow.md) to identify the document, its location, owner, and applicable rules, then applies the shared [technical documentation workflow](../../src/skills/documentation/technical-documentation-workflow.md) for evidence, writing, and validation. Both workflows are available to any agent; the selection workflow owns the method for accessing and using the shared [documentation matrix](../../src/skills/documentation/references/documentation-matrix.md). The matrix holds routing data; common rules, document-type guidance, layout guidance, and outlines live alongside it in the shared [documentation references](../../src/skills/documentation/references/documentation), without single-workflow ownership. Project standards retain repository-wide layout and setup conventions.

Definitions use `<skill-name>.md` directly inside their category. References owned by one skill carry its filename prefix; common references use neutral names under shared references. Keep links and ownership intact when moving content.

## Shared guidance

The suite links to shared definitions rather than maintaining copies:

- [Skill selection](../../src/skills/agent-workflows/skill-selection-workflow.md) uses the Engineering [selection matrix](../../src/skills/agent-workflows/references/skill-selection-workflow-matrix.md) to choose additional task-relevant guidance.
- [Output standardization](../../src/skills/agent-workflows/agent-output-standardization.md) covers clear responses, numbered findings, stable finding IDs, and matching [response templates](../../src/skills/agent-workflows/templates).
- [Change delivery](../../src/skills/agent-workflows/change-delivery-workflow.md) covers explicit selected-fix handoffs and separately authorized parent-only delivery actions.

Shared guidance does not override task-specific reporting requirements or grant tools, editing permission, or publication authority.

## Task flow and approvals

For a substantial feature, the roles can hand off product intent to detailed design, then implementation and relevant testing/documentation, followed by independent readiness review. This is a navigation pattern, not an implemented orchestrator or a requirement to invoke every specialist for a small change. The user or coordinating session selects the necessary roles.

A review alone produces findings without edits. Findings retain sequential IDs; an explicit selection such as `apply 1,2` authorizes only the selected corrections and their necessary tests or documentation. Delegation-enabled reviewers launch appropriate editing subagents, wait for results, and re-review the affected scope. If the host cannot support delegation or nesting, the reviewer reports the blocker and hands off rather than editing directly.

Implementation-capable specialists follow their own mode boundaries. No handoff or apply selection implicitly authorizes staging, commits, pushes, releases, deployment, or changes to a personal installation.

## Validation and limitations

Use the [repository maintenance checklist](../../README.md#validation) when changing these sources. Preserve role boundaries, names, descriptions, local links, heading anchors, and complete resource inclusion.

The suite describes tests and build workflows in consuming software projects; those definitions do not supply this repository with a compiler requirement, CI pipeline, or benchmark harness. The separate [Copilot installer](../installation.md) has regression tests through `make check`. Source inspection, link checks, and installer tests do not prove client discovery, skill loading, tool permissions, delegation, model behavior, or cross-client compatibility. Other client adapters remain deferred.
