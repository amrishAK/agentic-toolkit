# Agentic Toolkit

Agentic Toolkit is the authoritative source repository for reusable agents, skills, and supporting resources. It is for people maintaining reusable agent guidance independently of any one personal installation. The collection is initially engineering-focused, with research, product, and everyday-assistance suites intended for future expansion. It is pre-release and includes a Make-based Copilot installer for Windows and Linux. Installer tests do not constitute client behavioral certification.

## Documentation

Read the [project overview](docs/project-overview.md) for purpose, audience, organization, and boundaries. Browse the maintained definitions under [`src/`](src/). The [quick-start guide](docs/guides/quick-start.md) shows how to find and use current Engineering guidance; the [documentation index](docs/README.md) and [engineering-suite guide](docs/suites/engineering.md) explain roles, skill categories, and task handoffs. Source definitions own detailed behavior contracts; the guides explain how to navigate them.

## Usage and compatibility

Browse the source definitions and follow their relative links to supporting guidance. This repository is not an automatically discoverable agent or skill installation layout; use the [installation guide](docs/installation.md) rather than copying the source tree unchanged.

Filenames and source organization are neutral, but agent metadata and tool aliases remain Copilot/VS Code-oriented. Running a Claude model through Copilot is not the same as running Claude Code. No drop-in Claude Code support, cross-client tool equivalence, permission enforcement, or runtime discovery is established by this layout.

The Copilot installer:

1. Emits `agents/<name>.agent.md` and `skills/<name>/SKILL.md` under the user `.copilot` or workspace `.github` directory.
2. Resolves linked source dependencies and supporting resources, rewriting relative file links and preserving anchors. Repository documentation snapshots link back to the online repository.
3. Preserves existing Copilot metadata, tool aliases, read-only review phases, numbered findings, and approval-gated editing-subagent delegation. It does not translate to other clients or broaden tool permissions.
4. Warns that discovery, available tools, and delegation must be verified in the actual client. Unsupported delegation must be reported rather than replaced by direct reviewer edits.

Make and the installation engine are shared across clients. The [Copilot adapter](scripts/clients/copilot.py) owns client-specific paths and definition translation; dependency resolution, reference rewriting, and safe updates remain reusable. A future Claude adapter can use the same `CLIENT` interface, but `CLIENT=claude` is not implemented. See [adapter boundaries](docs/installation.md#shared-engine-and-client-adapters).

No directory links or MCP dependencies are installed. Host tools, permissions, and task-specific executables are still required when using the guidance. The layouts follow current [Copilot agent](https://code.visualstudio.com/docs/copilot/customization/custom-agents) and [skill](https://code.visualstudio.com/docs/copilot/customization/agent-skills) documentation. User-agent discovery depends on the selected Copilot harness; legacy VS Code Local harness profile storage is not configured. Runtime discovery and model behavior remain unverified.

### Quick start

For a minimal Copilot install, use GNU Make and Python 3.10+ from the repository root, and install the declared dependency with `python -m pip install -r requirements.txt` (`python3` on Linux when needed). Preview and install one agent with its linked resources:

```text
make list
make plan PACKAGE=testing SCOPE=user
make install PACKAGE=testing SCOPE=user
make plan SUITE=engineering AGENT=code-engineer SCOPE=user
make install SUITE=engineering AGENT=code-engineer SCOPE=user
```

See the [quick-start guide](docs/guides/quick-start.md) to browse and select guidance, and the [installation guide](docs/installation.md) for workspace installation, multi-skill selection, staging, update safety, and validation.

## Maintaining the collection

- Keep one authoritative definition per agent or skill under `src/agents/<category>/` or `src/skills/<category>/`. Suite membership and descriptive metadata live in `src/suites/<suite>.yaml`; do not infer suite membership from source categories.
- Compose suites from explicit `packages` lists rather than repeating package members. The Engineering suite includes the language-guidance package to preserve full-suite coverage; legacy direct agent and skill lists remain supported.
- Maintain functional installation packages under [`src/packages/`](src/packages/), with explicit agent and skill membership and quoted schema/content versions. Use `PACKAGE=<name>` to select one instead of a suite; see [functional packages](docs/installation.md#functional-packages).
- Declare shared package dependencies in `depends_on`; functional packages depend on [`core`](src/packages/core.yaml) for output standardization, documentation, and skill selection. Dependencies are resolved recursively, deduplicated, and checked for missing packages and cycles.
- Organize agent source directories by function: design and planning, implementation, testing, review and security, build and delivery, performance, documentation, and project standards. These categories organize sources; they do not create installation bundles or change agent names.
- Keep suite manifests versioned with `schema_version` and `version`. JSON Schema Draft 2020-12 contracts and cross-file checks are maintained in [`schemas/`](schemas/) and [`scripts/validate_manifests.py`](scripts/validate_manifests.py); see the [manifest schema guide](docs/reference/manifest-schemas.md) before changing manifest formats.
- Keep required role workflows explicit in agent definitions; use the shared [skill selection workflow](src/skills/agent-workflows/skill-selection-workflow.md) to choose additional task-specific guidance from the applicable suite matrix. Maintain Engineering category-level inventory and task routing in its [skill selection matrix](src/skills/agent-workflows/references/skill-selection-workflow-matrix.md), and language coverage and task-to-skill mappings in the [Engineering language-specific skill matrix](src/skills/programming-languages/references/programming-language-matrix.md). Do not duplicate task-to-skill maps in agent definitions.
- Add language skills and update the language-specific skill matrix without duplicating language lists in agents, general workflow descriptions, or the Engineering category-level skill selection matrix.
- Selection workflows own how to access and use their matrices; matrices own routing data. Use the shared [documentation matrix](src/skills/documentation/references/documentation-matrix.md) as the single entry point for document types, locations, owners, update triggers, and rule links. Each linked document-type reference owns its usage guidance, content, suggested structure, and validation; common rules apply across types. Keep these references in the same [reference folder](src/skills/documentation/references/documentation) without workflow-specific filename prefixes.
- Keep `name` and `description` metadata meaningful. Preserve role boundaries and behavior unless an intentional change is requested.
- Follow [definition-authoring guidance](docs/reference/definition-authoring.md) for the responsibilities and content of agent definitions, skill definitions, supporting references, templates, and catalogues. Follow the [repository glossary](docs/reference/glossary.md) for canonical terminology.
- Use relative links for repository resources; never link back to a personal installation or embed machine-specific paths.
- When renaming or moving definitions, update inbound links and links from bundled resources in the same change. Keep resource owner prefixes consistent.
- Treat agent instructions as source content, not permission to execute their workflows while editing this repository.
- Keep generated client output separate from maintained sources when translation is introduced.

### Validation

There is no compiled application build or benchmark harness. The installer uses PyYAML for suite manifests, and the manifest checker uses `jsonschema`; install declared dependencies from `requirements.txt`. `make check` validates manifest schemas and cross-file references before running the installer's regression tests, including generated-layout link checks, temporary installs, update/conflict handling, and CLI checks. GitHub Actions runs these checks on pushes and pull requests. No compiler is required. Language-specific test, build, and benchmark skills describe work in consuming projects, not additional test tiers here.

For content changes, manually check:

- Frontmatter structure, unique names, descriptions, and filename/name agreement.
- Declared tools and reviewer boundaries; prose restrictions are not a hard permission sandbox.
- Relative file links, heading anchors, and complete inclusion of referenced resources.
- Absence of secrets, personal-machine paths, and obsolete definition references.
- The diff, including new and untracked files, for unintended changes.

Existing Git supports read-only inspection:

```text
git status --short
git diff --check
git diff
```

Git diff commands do not cover untracked file contents; inspect those separately. For installer changes, run `make check` and exercise affected Make targets using a temporary `DESTDIR`, never an active personal installation without explicit authorization. Passing static checks or installer tests does not establish runtime discovery, delegation, client compatibility, or behavior. Report executed checks separately from untested claims.

## Repository scope

This repository owns reusable source guidance, its supporting resources, and the local Copilot installer and its tests. GitHub Actions runs manifest validation and unit tests on pushes and pull requests; broader CI, release/deployment automation, other client adapters, generated distributions, and additional suites remain deferred. Changes here do not authorize changes to an active personal installation.

Feature tracking is intentionally omitted for this source-content repository. Dedicated release plans, contribution/security policies, and changelog are not established; do not infer support commitments or release approval from this baseline.

Use Conventional Commits for future authorized commits, such as `docs: clarify repository guidance` or `fix(skills): repair reference links`. Commit, push, remote, release, and installation actions require separate explicit authorization.

See [AGENTS.md](AGENTS.md) for repository editing guidance.

## License

[MIT](LICENSE). Copyright (c) 2026 Amrish Arunachalam Kulasekaran.
