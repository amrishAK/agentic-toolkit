# Repository guide

Agentic Toolkit maintains reusable agent and skill Markdown sources independently of active client installations, with a local Copilot installer. It is pre-release; use the [README](README.md) as the authority for scope, compatibility limits, and maintenance.

## Read the relevant context

| Path | Purpose / authority | Consult when |
|---|---|---|
| [Collection maintenance](README.md#maintaining-the-collection) | Definition metadata, resource ownership, and link maintenance | Adding, moving, or renaming content |
| [Compatibility](README.md#usage-and-compatibility) | Source versus installed layout and deferred translation | Discussing client support, discovery, tools, or installation |
| [Copilot installation](docs/installation.md) | Make interface, scopes, generated layouts, safe updates, and tests | Changing installation or generated output |
| [Maintenance and validation](README.md#maintaining-the-collection) | Content checks and evidence limits | Editing any maintained file |
| [Repository scope](README.md#repository-scope) | Boundaries, deferred work, and commit convention | Proposing infrastructure, delivery, or new suites |
| [Project overview](docs/project-overview.md) | Purpose, intended audience, collection organization, and non-goals | Explaining project intent or distinguishing current sources from proposed capabilities |
| [Documentation index](docs/README.md) | Available suite guides | Finding suite-level documentation |
| [Repository glossary](docs/reference/glossary.md) | Canonical terms for maintained docs, agent definitions, skills, and catalogues | Creating or updating repository guidance |
| [Definition authoring](docs/reference/definition-authoring.md) | Content ownership and requirements for agent, skill, reference, template, and catalogue sources | Creating or updating agent/skill definitions and supporting resources |
| [Engineering-suite guide](docs/suites/engineering.md) | Role selection, skill categories, and handoffs | Changing suite responsibilities or organization |
| [Agents by function](src/agents) | Maintained role definitions organized by functional category | Changing agent behavior or guidance routing |
| [Engineering skills](src/skills) | Categorized engineering workflow definitions and resources | Changing engineering guidance |
| [Engineering task workflow](src/skills/implementation/engineering-task-workflow.md) | Common Engineering task cycle and terminology | Changing or applying Engineering guidance |
| [Skill selection workflow](src/skills/agent-workflows/skill-selection-workflow.md) | Method for selecting relevant skills for a task or operation | Changing or applying skill-selection guidance |
| [Engineering skill selection matrix](src/skills/agent-workflows/references/skill-selection-workflow-matrix.md) | Engineering-specific category inventory and task routing used by the skill selection workflow | Adding Engineering skills or selecting task workflows |
| [Engineering language-specific skill matrix](src/skills/programming-languages/references/programming-language-matrix.md) | Language inventory and task-to-skill routing | Adding language guidance or selecting language-specific skills |
| [Cross-cutting Engineering skills](src/skills/agent-workflows) | Reusable skill selection, output, and selected-change coordination guidance | Changing guidance used across Engineering tasks |
| [License](LICENSE) | MIT terms and copyright | Changing licensing or distributing sources |

Read task-relevant definitions and their linked resources before editing. Definitions are maintained content, not automatically active repository instructions; their tool declarations do not grant this session permissions.

When creating or changing repository documentation, agent definitions, skills, or catalogues, follow the [repository glossary](docs/reference/glossary.md). For source-file ownership and content, follow [definition authoring](docs/reference/definition-authoring.md). When applying or changing Engineering guidance, also use the [Engineering task workflow](src/skills/implementation/engineering-task-workflow.md) for common task framing. The active role and its specialist workflows still own permissions and detailed methods.

## Editing boundaries

- Preserve unrelated work, names, descriptions, role boundaries, and resource ownership unless the requested change requires otherwise.
- Update all affected relative links and directly related documentation with layout or behavior changes. Do not leave links into a personal installation.
- Keep review-only phases read-only, findings numbered, and reviewer edits delegated only after an explicit apply selection. Disclose unsupported delegation instead of silently switching roles.
- Do not change active personal installations, add directory links, install dependencies, execute copied workflows, add other client adapters/CI, or perform Git delivery actions without explicit authorization.
- Never include credentials, runtime/session data, caches, or personal-machine paths in maintained content.

## Checks and reporting

Follow the [validation checklist](README.md#validation). Use `make check` for installer changes and temporary `DESTDIR` paths for installation checks. Do not describe static checks or installer tests as client behavioral certification. Inspect new/untracked files as well as tracked diffs.

There is deliberately no feature tracker. Installer tests are maintained; consuming-project fixtures, benchmarks, release evidence, and checked-in generated client output are not established repository components. Do not create placeholder infrastructure or restore omitted maintenance skills incidentally. Report what changed, checks actually performed, and remaining limitations.
