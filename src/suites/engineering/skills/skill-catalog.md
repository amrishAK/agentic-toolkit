# Engineering skill catalogue

This catalogue owns category-level skill inventory and task routing for the engineering suite, including the shared skills it consumes. The [programming language catalogue](programming-languages/programming-language-catalog.md) owns language-specific inventory and routing. Agents own roles and authorization boundaries; skill definitions own detailed methods and supporting resources.

This is a maintained navigation reference, not a skill definition, executable registry, dependency manifest, or client installation layout.

## Select guidance

1. Follow the active agent's required workflows first. This catalogue does not replace mandatory guidance or role boundaries.
2. Select additional guidance by task using the table below. Each linked label is a skill's invocation name; its target is the direct-read fallback when invocation is unavailable.
3. Load only relevant skills and the supporting references or templates they require. Do not load a whole category merely because one skill applies.
4. For language-specific work, use the programming language catalogue's matching task columns. Keep language lists and per-language selection there rather than duplicating them here.
5. If guidance is missing or cannot be loaded or read, report the limitation. Do not invent a skill name or claim it was applied; ask or stop affected work when correctness depends on unavailable guidance.
6. Selection never grants editing, execution, delegation, installation, or delivery permission. Preserve the active role's approval gates and report unsupported capabilities.

## Task workflows by category

| Category | Task | Skill |
|---|---|---|
| Design and planning | Product purpose, priorities, roadmap, and release goals | [product-planning-workflow](design-and-planning/product-planning-workflow.md) |
| Design and planning | Detailed feature requirements, contracts, and implementation plans | [feature-design-workflow](design-and-planning/feature-design-workflow.md) |
| Design and planning | Component boundaries, interfaces, lifecycle, and architecture trade-offs | [architecture-workflow](design-and-planning/architecture-workflow.md) |
| Implementation | Implementation, fixes, refactoring, and code-quality review | [code-quality-workflow](implementation/code-quality-workflow.md) |
| Implementation | Evidence-led diagnosis of code, build, or CI failures | [debugging-workflow](implementation/debugging-workflow.md) |
| Testing | Focused unit tests and regression coverage | [unit-test-workflow](testing/unit-test-workflow.md) |
| Testing | Real component interactions through public interfaces | [integration-test-workflow](testing/integration-test-workflow.md) |
| Testing | Complete application journeys through external interfaces | [e2e-test-workflow](testing/e2e-test-workflow.md) |
| Testing | Bounded fuzzing, corpus handling, and regression promotion | [fuzz-testing-workflow](testing/fuzz-testing-workflow.md) |
| Performance | Benchmark workloads, measurements, comparisons, and reports | [benchmark-workflow](performance/benchmark-workflow.md) |
| Performance | CPU, memory, contention, I/O, and async performance diagnosis | [profiling-workflow](performance/profiling-workflow.md) |
| Build and delivery | Build systems, dependencies, toolchains, and local/CI entry points | [build-system-workflow](build-and-delivery/build-system-workflow.md) |
| Build and delivery | GitHub Actions workflows | [ci-workflow](build-and-delivery/ci-workflow.md) |
| Build and delivery | Dockerfiles, BuildKit, and Docker Compose | [container-build-workflow](build-and-delivery/container-build-workflow.md) |
| Build and delivery | Release readiness, compatibility, and artifact checks | [release-workflow](build-and-delivery/release-workflow.md) |
| Documentation | Document catalogue and rule selector: before any agent reviews, writes, or updates a document, identify what it is, where it lives, who owns it, and which rules define its content and structure | [documentation-requirements](documentation/documentation-requirements.md) |
| Documentation | README, architecture, setup, user/developer guides, and runbooks | [technical-documentation-workflow](documentation/technical-documentation-workflow.md) |
| Project standards | Adaptable repository-wide item/placement conventions, docs-tree layout and documentation ownership | [project-conventions](project-standards/project-conventions.md) |
| Project standards | Repository inspection, explained structure proposal, interview/refinement, confirmation, creation of agreed essentials and validation | [project-rules-workflow](project-standards/project-rules-workflow.md) |
| Review and security | Change-readiness assessment in the active role's supported review modes | [review-workflow](review-and-security/review-workflow.md) |
| Review and security | Authorized source security review and threat modeling | [security-review-workflow](review-and-security/security-review-workflow.md) |

## Programming languages

Use the [programming language catalogue](programming-languages/programming-language-catalog.md) for language-specific code quality, unit testing, integration testing, benchmarking, and source documentation. Pair those skills with the relevant task workflow; source documentation remains distinct from standalone technical documentation.

## Shared guidance

These definitions are owned by shared skills, not copied into the engineering suite.

| Task | Skill |
|---|---|
| Responses, clarification questions, review reports, and handoffs | [agent-output-standardization](../../../shared/skills/agent-output-standardization.md) |
| Explicit selected-fix handoffs and separately authorized delivery actions | [change-delivery-workflow](../../../shared/skills/change-delivery-workflow.md) |

## Maintain the catalogue

- Add, rename, move, or remove category-level skills and update this catalogue in the same change. Keep invocation names aligned with skill metadata and links aligned with source locations.
- Maintain language-specific entries only in the programming language catalogue. Maintain detailed methods, required guidance, references, and templates in their owning definitions.
- Agents must continue to name their required workflows explicitly. Use this catalogue for additional task selection without turning every task into a full-inventory lookup or changing a role's permissions.
- Check relative links, unique skill names, category coverage, and referenced resources using the [repository validation checklist](../../../../README.md#validation). A catalogue entry records source guidance, not tested runtime support.
- The Copilot installer discovers definitions from frontmatter and resolves linked skills and resources, translating filenames and rewriting links. This table remains navigation guidance, not an installation specification or separately maintained dependency manifest.
