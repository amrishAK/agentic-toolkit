---
name: project-conventions
description: "Use when applying, checking, or auditing cross-project conventions: repository items and placement, documentation catalog and templates, shared local/CI entry points, docs layout, feature documents, evidence-backed status and release gates, Conventional Commits, architecture boundaries, test tiers, project summary and feature tracker, LICENSE, .gitignore, and the staged open-source baseline. Adaptable defaults for new projects and drift audits of existing ones."
---

# Project conventions

These are adaptable cross-project defaults, not mandatory directory scaffolding. They explain common repository items, where they belong, when they are useful, and what belongs elsewhere. Each convention lives in its own file so it can be changed independently; other skills and agents link here instead of restating them. The [setup workflow](./project-rules-workflow.md) owns inspection, interviewing, structure proposals, confirmation, and creation of agreed essentials; conventions supply placement and content guidance.

| Convention | File |
|---|---|
| One shared entry point for local runs and CI | [entry-points.md](./references/project-conventions-entry-points.md) |
| Documentation tree only: `docs/` layout, documentation entry points, status files, evidence-backed claims | [documentation-requirements-docs-layout.md](../documentation/references/documentation-requirements-docs-layout.md) |
| Document catalogue: what each document is, where it lives, its owner, and its rules | [documentation-requirements](../documentation/documentation-requirements.md) |
| Feature document template | [documentation-requirements-feature-docs.md](../documentation/references/documentation-requirements-feature-docs.md) |
| Commit messages | [commits.md](./references/project-conventions-commits.md) |
| Repository-wide item/path/purpose/applicability map; architecture boundaries, non-goals, naming | [architecture-and-scope.md](./references/project-conventions-architecture-and-scope.md#repository-layout) |
| Test tiers, fixtures, infrastructure-dependent tests | [testing.md](./references/project-conventions-testing.md) |
| Open-source baseline: required files, CI, and release stages | [oss-baseline.md](./references/project-conventions-oss-baseline.md) |
| Project summary and default feature tracker (with project-specific opt-out) | [documentation-requirements-project-tracking.md](../documentation/references/documentation-requirements-project-tracking.md) |

Load only the files relevant to the task.

## How to apply

- **Applicability:** follow the host's instruction hierarchy and applicable organization/project requirements (`AGENTS.md`, scoped instructions). These personal conventions are defaults, not authority to override permissions or policy. Preserve deliberate project differences; surface unresolved conflicts rather than bypassing them.
- **Feature tracking:** the tracker is the default convention, but an explicit, confirmed project-specific rule may opt out. Follow that scope rather than imposing the cross-project default.
- **New work:** select applicable defaults for the project's ecosystem and confirmed scope. Example paths are options, not evidence that those paths exist or permission to create every item.
- **Existing projects:** follow what the project already does. Report drift from these conventions; migrate only when asked. Do not rename, move, or restructure files as a side effect of another task.
- **Project rules:** repositories cannot reference this personal skill. Record adopted conventions in repository-owned authorities and link them from a concise `AGENTS.md`; do not copy the whole convention catalogue into the guide.

## Maintaining these conventions

- Change a convention in its single file. Do not copy its wording into other skills or agents; link to it.
- When a convention changes, audit existing projects for drift with `project-standardizer` rather than editing them silently.
