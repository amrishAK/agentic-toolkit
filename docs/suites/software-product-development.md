# Software Product Development suite

The Software Product Development suite provides reusable guidance for product management, engineering, and quality. Start with the task routes below to find a role, or browse the [agent definitions](../../src/agents/) and [skills](../../src/skills/). These are maintained sources, not an installed client registry; see the repository's [usage and compatibility notes](../../README.md#usage-and-compatibility).

## Start with a task

Use these routes to find a useful starting point. They are navigation guidance, not automatic routing; follow the selected role's boundaries and linked workflows.

| Task | Starting point | Next guidance or handoff |
|---|---|---|
| Plan a roadmap or release | [product-planner](../../src/agents/design-and-planning/product-planner.md) | Use [roadmap planning](../../src/skills/design-and-planning/roadmap-planning-workflow.md) or [release planning](../../src/skills/design-and-planning/release-planning-workflow.md); request independent review from [product-plan-reviewer](../../src/agents/design-and-planning/product-plan-reviewer.md). |
| Design or independently review a feature contract | [feature-designer](../../src/agents/design-and-planning/feature-designer.md) or [feature-contract-reviewer](../../src/agents/design-and-planning/feature-contract-reviewer.md) | Follow the [feature-design workflow](../../src/skills/design-and-planning/feature-design-workflow.md); hand an accepted contract to [code-engineer](../../src/agents/implementation/code-engineer.md) for implementation. |
| Implement a feature or bounded fix | [code-engineer](../../src/agents/implementation/code-engineer.md) | Use [test-driven implementation](../../src/skills/implementation/test-driven-implementation-workflow.md); select the applicable tests and independent review for the change. |
| Diagnose a build or CI failure | [build-automation-agent](../../src/agents/build-and-delivery/build-automation-agent.md) | Start with the [debugging workflow](../../src/skills/implementation/debugging-workflow.md), then consult the relevant [build](../../src/skills/build-and-delivery/build-system-workflow.md) or [CI](../../src/skills/build-and-delivery/ci-workflow.md) workflow. |
| Test a component boundary | [integration-tester](../../src/agents/testing/integration-tester.md) | Use the [integration-test workflow](../../src/skills/testing/integration-test-workflow.md) and relevant language guidance. |
| Write or update a project guide | [technical-documentation-writer](../../src/agents/documentation/technical-documentation-writer.md) | Use the [documentation selection workflow](../../src/skills/documentation/documentation-selection-workflow.md) to find the document owner and applicable rules. |

## Choose a role

| Agent | Use for | Important boundary |
|---|---|---|
| [product-planner](../../src/agents/design-and-planning/product-planner.md) | Product intent, roadmaps, release plans, priorities, and scope | The user approves priorities and scope; detailed contracts belong to feature-designer. |
| [product-plan-reviewer](../../src/agents/design-and-planning/product-plan-reviewer.md) | Independent review of roadmaps and release plans | Read-only; does not decide scope or approve plans. |
| [feature-designer](../../src/agents/design-and-planning/feature-designer.md) | Requirements, behavior contracts, edge cases, and architecture trade-offs | Does not implement production code; contract acceptance requires user confirmation and independent validation. |
| [feature-contract-reviewer](../../src/agents/design-and-planning/feature-contract-reviewer.md) | Independent validation of a drafted feature contract | Reviews the contract; does not author or accept it on the user's behalf. |
| [code-engineer](../../src/agents/implementation/code-engineer.md) | Implementation, debugging, fixes, and refactoring | Implementation self-review is not independent readiness approval. |
| [unit-tester](../../src/agents/testing/unit-tester.md) | Unit-test design, coverage, boundary inputs, and regressions | Does not change production behavior to make tests pass. |
| [integration-tester](../../src/agents/testing/integration-tester.md) | Real component interactions through public interfaces | Does not replace integration with mocks or call it full-system E2E. |
| [e2e-tester](../../src/agents/testing/e2e-tester.md) | Complete application journeys through external interfaces | Uses isolated test-owned resources; infrastructure changes need authorization. |
| [change-reviewer](../../src/agents/review-and-security/change-reviewer.md) | Per-commit, pre-PR, and per-release readiness | Review is read-only; selected fixes are delegated, not edited directly. |
| [security-reviewer](../../src/agents/review-and-security/security-reviewer.md) | Authorized source security review and threat modeling | No command execution, active probing, or direct remediation. |
| [build-automation-agent](../../src/agents/build-and-delivery/build-automation-agent.md) | Make/CMake, native builds, GitHub Actions, and containers | Publishing, deployment, and remote workflow execution need explicit authorization. |
| [benchmark-engineer](../../src/agents/performance/benchmark-engineer.md) | Benchmark design, execution, comparisons, and reports | Execution needs an authorized scope and budget; measurements are not release approval. |
| [project-standardizer](../../src/agents/project-standards/project-standardizer.md) | Repository structure, guidance, licensing, ignore rules, and baseline documentation | Resolves setup decisions through its agreed interview; does not change personal installations. |
| [source-documentation-writer](../../src/agents/documentation/source-documentation-writer.md) | Source comments and API contracts | Comments-only work; not production logic or standalone guides. |
| [technical-documentation-writer](../../src/agents/documentation/technical-documentation-writer.md) | README files, guides, architecture docs, setup, and runbooks | Owns repository documentation, not source comments. |

Roles describe responsibilities, not required team headcount. Product planning is a package within this suite, not a separate suite. Discovery & Shaping and product-level feature-brief guidance remain proposed V2 capabilities; they are not current roles.

## Packages and selection

The [suite manifest](../../src/suites/software-product-development.yaml) composes two responsibility packages:

| Package | Responsibility |
|---|---|
| [product-management](../../src/packages/product-management.yaml) | Product goals, roadmaps, release planning, independent plan review, and product-to-engineering handoffs. |
| [engineer](../../src/packages/engineer.yaml) | Feature design and contract review, implementation, builds, performance, project standards, testing, and change/security review. |

Both packages include shared core guidance. The suite also offers [programming-language guidance](../../src/packages/programming-languages.yaml) as an optional package, enabled by default. Smaller functional packages can be selected independently. See the [installation guide](../installation.md) for selection and installation details.

Select additional skills using the shared [skill selection workflow](../../src/skills/agent-workflows/skill-selection-workflow.md) and its [task matrix](../../src/skills/agent-workflows/references/skill-selection-workflow-matrix.md). For language-specific code-quality, testing, benchmarking, and source-documentation guidance, consult the [Engineering language matrix](../../src/skills/programming-languages/references/programming-language-matrix.md). Matrices route readers to maintained guidance; they are not runtime registries or installation manifests.

Agent definitions own role responsibilities and boundaries; skills provide reusable task methods. Required workflows are named by the relevant agent. Choose other guidance as needed rather than loading every skill for every task. See [definition authoring](../reference/definition-authoring.md) for the source ownership rules.

## Handoffs and review

For substantial work, a useful route may pass from product intent to feature design, implementation, relevant testing or documentation, and independent readiness review. Smaller tasks may need only one role. The user or coordinating session chooses the roles; packages do not automatically orchestrate handoffs or grant permissions.

A handoff provides context and requests a next decision or action. It does not imply approval or authorization. Reviews report findings without editing; selected corrections follow the reviewer's explicit delegated-fix process. Implementation self-review, contract review, and readiness review are distinct checks. No handoff or fix selection authorizes commits, pushes, releases, deployment, or changes to a personal installation.

For the connected sequence from roadmap and release planning through feature implementation and release approval, see the [roadmap-to-release workflow](../guides/roadmap-to-release-workflow.md).

## Scope and validation

The suite describes guidance for consuming software projects; it does not provide this repository with a compiler, CI pipeline, or benchmark harness. The separate [Copilot installer](../installation.md) is validated with `make check`. Installer tests and source inspection do not establish client discovery, skill loading, tool permissions, delegation, model behavior, or cross-client compatibility. For repository maintenance checks, see the [README validation checklist](../../README.md#validation).
