# Software Product Development task matrix

| Use | Skill |
|---|---|
| Universal guardrails for evidence, scope, simplicity, useful output, uncertainty, trust, and honest outcomes across agent roles | [agent-guidelines](../agent-guidelines.md) |
| Common task framing, evidence, role boundaries, validation, and reporting across product management, engineering, and quality | [engineering-task-workflow](../../implementation/engineering-task-workflow.md) |
| Standardized responses, clarification questions, findings, summaries, and handoffs | [agent-output-standardization](../agent-output-standardization.md) |
| Coordination of explicitly selected review fixes and separately authorized delivery actions | [change-delivery-workflow](../change-delivery-workflow.md) |

## Task-specific skills

| Task area | Task signal | Skill |
|---|---|---|
| Product planning coordination | Product purpose, planning decisions across documents, roadmap-to-release sequencing, approval boundaries, or handoffs to feature design | [product-planning-workflow](../../design-and-planning/product-planning-workflow.md) |
| Roadmap planning | Drafting, updating, or reviewing high-level direction, relative priorities, or proposed release sequence | [roadmap-planning-workflow](../../design-and-planning/roadmap-planning-workflow.md) |
| Release planning | Drafting, updating, or reviewing milestone scope, exclusions, dependencies, supported configurations, acceptance gates, or candidate evidence | [release-planning-workflow](../../design-and-planning/release-planning-workflow.md) |
| Feature contracts | Drafting, updating, or reviewing detailed behavior, public contracts, edge cases, acceptance criteria, or implementation handoffs | [feature-design-workflow](../../design-and-planning/feature-design-workflow.md) |
| Architecture | Component boundaries, dependency direction, public interfaces, lifecycle, data flow, storage/protocol choices, or compatibility trade-offs | [architecture-workflow](../../design-and-planning/architecture-workflow.md) |
| Code implementation and review | Reviewing code or implementing, fixing, or refactoring focused code changes; pair with test-driven implementation when changing behavior | [code-quality-workflow](../../implementation/code-quality-workflow.md) |
| Test-driven implementation | Implementing a feature, fix, or behavior change from an agreed contract or bounded request, including task planning, unit-first red-green-refactor, and feature validation; not review-only or diagnosis-only work | [test-driven-implementation-workflow](../../implementation/test-driven-implementation-workflow.md) |
| Debugging | Diagnosing code, build, or CI failures without implementing a fix; when a fix is authorized, use code-quality guidance and test-driven implementation for behavior changes | [debugging-workflow](../../implementation/debugging-workflow.md) |
| Unit testing | Focused unit tests, contract coverage, fixtures, or regression tests | [unit-test-workflow](../../testing/unit-test-workflow.md) |
| Integration testing | Real component interactions through public interfaces | [integration-test-workflow](../../testing/integration-test-workflow.md) |
| End-to-end testing | Complete application journeys through external interfaces | [e2e-test-workflow](../../testing/e2e-test-workflow.md) |
| Fuzz testing | Bounded fuzzing, harnesses, corpus management, or regression promotion | [fuzz-testing-workflow](../../testing/fuzz-testing-workflow.md) |
| Benchmarking | Workload design, measurement, comparison, or benchmark reporting | [benchmark-workflow](../../performance/benchmark-workflow.md) |
| Performance profiling | CPU, memory, contention, I/O, or asynchronous performance diagnosis | [profiling-workflow](../../performance/profiling-workflow.md) |
| Build systems | Make/CMake, .NET or native build workflows, dependencies, toolchains, and build entry points | [build-system-workflow](../../build-and-delivery/build-system-workflow.md) |
| CI/CD | GitHub Actions workflows, permissions, caching, artifacts, or deployment boundaries | [ci-workflow](../../build-and-delivery/ci-workflow.md) |
| Container builds | Dockerfiles, BuildKit, Docker Compose, or container runtime behavior | [container-build-workflow](../../build-and-delivery/container-build-workflow.md) |
| Release readiness | Versions, compatibility, package checks, provenance, SBOM/signing policy, or authorized release delivery | [release-workflow](../../build-and-delivery/release-workflow.md) |
| Documentation selection | Identifying document type, owner, placement, and applicable content/structure rules before reviewing or changing a document | [documentation-selection-workflow](../../documentation/documentation-selection-workflow.md) |
| Technical documentation | Writing, reviewing, or maintaining README files, guides, architecture docs, runbooks, and other technical documentation | [technical-documentation-workflow](../../documentation/technical-documentation-workflow.md) |
| Project conventions | Applying or auditing repository-wide conventions, documentation layout, entry points, test tiers, and baseline files | [project-conventions](../../project-standards/project-conventions.md) |
| Project setup and standardization | Inspecting, prefilling a repository profile, interviewing gaps, and creating/updating the profile, README, and agreed guidance | [project-rules-workflow](../../project-standards/project-rules-workflow.md) |
| Change review | Readiness assessment for a commit, pre-PR, pull request, or release in the active role's supported mode | [review-workflow](../../review-and-security/review-workflow.md) |
| Security review | Authorized source security review and threat modeling | [security-review-workflow](../../review-and-security/security-review-workflow.md) |

Language-specific code quality, testing, benchmarking, and source documentation are routed separately by the [Engineering language matrix](../../programming-languages/references/programming-language-matrix.md).
