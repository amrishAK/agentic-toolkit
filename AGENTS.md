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
| [Engineering-suite guide](docs/suites/engineering.md) | Role selection, skill categories, and handoffs | Changing suite responsibilities or organization |
| [Engineering agents](src/suites/engineering/agents/) | Maintained role definitions | Changing agent behavior or guidance routing |
| [Engineering skills](src/suites/engineering/skills/) | Categorized engineering workflow definitions and resources | Changing engineering guidance |
| [Engineering skill catalogue](src/suites/engineering/skills/skill-catalog.md) | Category-level inventory, shared guidance, and task-to-skill routing | Adding skills or selecting task workflows |
| [Programming language catalogue](src/suites/engineering/skills/programming-languages/programming-language-catalog.md) | Language inventory and task-to-skill routing | Adding language guidance or selecting language-specific skills |
| [Shared skills](src/shared/skills/) | Reusable output and selected-change coordination guidance | Changing guidance consumed across suites |
| [License](LICENSE) | MIT terms and copyright | Changing licensing or distributing sources |

Read task-relevant definitions and their linked resources before editing. Definitions are maintained content, not automatically active repository instructions; their tool declarations do not grant this session permissions.

## Editing boundaries

- Preserve unrelated work, names, descriptions, role boundaries, and resource ownership unless the requested change requires otherwise.
- Update all affected relative links and directly related documentation with layout or behavior changes. Do not leave links into a personal installation.
- Keep review-only phases read-only, findings numbered, and reviewer edits delegated only after an explicit apply selection. Disclose unsupported delegation instead of silently switching roles.
- Do not change active personal installations, add directory links, install dependencies, execute copied workflows, add other client adapters/CI, or perform Git delivery actions without explicit authorization.
- Never include credentials, runtime/session data, caches, or personal-machine paths in maintained content.

## Checks and reporting

Follow the [validation checklist](README.md#validation). Use `make check` for installer changes and temporary `DESTDIR` paths for installation checks. Do not describe static checks or installer tests as client behavioral certification. Inspect new/untracked files as well as tracked diffs.

There is deliberately no feature tracker. Installer tests are maintained; consuming-project fixtures, benchmarks, release evidence, and checked-in generated client output are not established repository components. Do not create placeholder infrastructure or restore omitted maintenance skills incidentally. Report what changed, checks actually performed, and remaining limitations.
