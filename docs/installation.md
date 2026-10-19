# Copilot installation

The reusable [Makefile](../Makefile) delegates to the [installer](../scripts/install.py), which selects a client adapter through `CLIENT`. The [Copilot adapter](../scripts/clients/copilot.py) is currently the only implementation. It generates Copilot layouts from maintained sources without symlinks, downloads, or changes to client settings.

## Prerequisites and scope

- GNU Make and Python 3.10+ on `PATH`, with dependencies from [`requirements.txt`](../requirements.txt) installed for the Python interpreter used by Make.
- Run commands from this repository's root. On Windows, use native GNU Make from PowerShell or Command Prompt; on Linux, use GNU Make from a POSIX shell.
- Recipes invoke Python directly and do not require Bash on Windows or PowerShell on Linux. `PYTHON` defaults to `python` on Windows and `python3` on Linux; override it with an executable path if necessary. It is an executable, not a command with extra arguments.
- A Copilot client that supports the documented [custom-agent](https://code.visualstudio.com/docs/copilot/customization/custom-agents) and [agent-skill](https://code.visualstudio.com/docs/copilot/customization/agent-skills) layouts. Installation alone does not verify discovery or behavior.

| Scope | Installation root | Generated definitions |
|---|---|---|
| `user` (default) | `.copilot` in the Python user's home directory | `agents/<name>.agent.md`, `skills/<name>/SKILL.md` |
| `workspace` | `.github` under `WORKSPACE` | `agents/<name>.agent.md`, `skills/<name>/SKILL.md` |

User-agent folders apply to the Copilot harness. Legacy VS Code Local harness sessions may use profile storage instead; this installer does not migrate profiles or edit settings. Remote/WSL sessions need installation on the machine where the harness runs.

## Select and preview

```text
make help
make list
make list PACKAGE=testing
make plan PACKAGE=testing SCOPE=user
make plan CLIENT=copilot SUITE=engineering SCOPE=user
make plan SUITE=engineering LANGUAGE_SKILLS=exclude
make plan SUITE=engineering SKILLS=code-quality-workflow,rust-code-quality
```

`plan` resolves dependencies, checks destination conflicts, and prints generated paths without creating directories or files. `install` uses the same variables and performs the writes.

| Variable | Meaning |
|---|---|
| `CLIENT` | Only `copilot` is currently accepted |
| `SUITE` | Suite manifest name; defaults to `engineering` |
| `PACKAGE` | Optional functional package name; replaces suite selection and cannot be combined with `AGENT`, `SKILL`, or `SKILLS` |
| `AGENT` | Optional agent name listed in the suite manifest |
| `SKILL` | Optional skill name listed in the suite manifest; mutually exclusive with `AGENT` |
| `SKILLS` | Optional comma-separated skill names listed in the suite manifest; mutually exclusive with `AGENT` and `SKILL` |
| `LANGUAGE_SKILLS` | `include` (default) or `exclude`; applies only to full-suite or full-package selection. Other values fail explicitly. |
| `OPTIONAL_PACKAGES` | `include` (default), `exclude`, or comma-separated names from the suite's `optional_packages`; applies to full-suite selection. |
| `SCOPE` | `user` or `workspace`; defaults to `user` |
| `WORKSPACE` | Existing project directory; required for workspace scope unless staging |
| `DESTDIR` | Optional exact installation root, replacing `.copilot` or `.github`, for staging |
| `PYTHON` | Python executable used by Make |

Omit `AGENT`, `SKILL`, and `SKILLS` to install every definition listed in the suite manifest. Single-agent selection installs that agent plus its required linked skills, catalogues, templates, and references. Catalogue links are navigational: they do not pull in every listed skill. Installed catalogues link selected or otherwise-required skill definitions locally and link other entries to their maintained source. When the selection workflow is included, each installation renders its matrix from the current maintained source; installation does not modify that source. `SKILL` installs one skill; `SKILLS` installs several selected skills and their required linked resources. Cycles are resolved once. Skill selection does not install unrelated agents.

For full-suite selection, `LANGUAGE_SKILLS=include` preserves the default behavior. Set `LANGUAGE_SKILLS=exclude` to omit definitions listed in the suite manifest whose source is under `src/skills/programming-languages/`, unless explicitly required by selected definitions. Other listed agents, skills, and their linked resources remain included. Language-matrix navigation does not pull excluded skill definitions back in; unavailable entries link to their maintained source. Targeted `AGENT`, `SKILL`, and `SKILLS` selections always install the requested definitions and dependencies regardless of this option.

## Install examples

### Suites composed of packages

The [Engineering suite](../src/suites/engineering.yaml) lists package IDs rather
than duplicating their agent and skill membership:

```yaml
packages:
  - core
  - design-and-planning
  - implementation
  - testing
  - review-and-security
  - build-and-delivery
  - performance
  - project-standards
optional_packages:
  - programming-languages
```

`make install SUITE=engineering` resolves these packages and their dependencies,
deduplicating agent and skill members. `optional_packages` are offered by the
suite and enabled by default; the installer prints them on `plan` and `install`.
Set `OPTIONAL_PACKAGES=exclude` to skip them, or a comma-separated list of the
suite's optional package names to choose. Optional packages must exist, must not
also appear in `packages`, and are not affected by `AGENT`, `SKILL`, or `SKILLS`,
which can still name any suite member. `AGENT`, `SKILL`, and `SKILLS` still select
from the resolved suite membership. `LANGUAGE_SKILLS=exclude` still filters
language-specific seeds, not required linked dependencies.

Suite manifests may still declare direct `agents` and `skills` for compatibility;
if combined with `packages`, their membership is merged. A suite must declare
`agents` or a non-empty `packages` list. Missing packages and invalid dependency
graphs fail validation and installation.

### Functional packages

Versioned [package manifests](../src/packages/) explicitly list agents and skills
by canonical name. Available packages are `design-and-planning`, `implementation`,
`testing`, `review-and-security`, `build-and-delivery`, `performance`,
`project-standards`, and `programming-languages`. The seven agent-oriented packages depend
on the [`core` package](../src/packages/core.yaml), which contains:

- Agents: `source-documentation-writer` and `technical-documentation-writer`.
- Skills:
  - `agent-output-standardization`
  - `skill-selection-workflow`
  - `documentation-selection-workflow`
  - `technical-documentation-workflow`

Install `PACKAGE=core` directly to get these documentation agents, shared skills,
and their linked resources. Documentation is part of core, not a separate
installation package.

`programming-languages` is an independent skill-only package and does not depend
on core. Installing it alone does not install documentation agents. The
Engineering suite lists it as an optional package, enabled by default.

```text
make list PACKAGE=testing
make plan PACKAGE=testing SCOPE=user
make install PACKAGE=testing SCOPE=user
```

`PACKAGE` takes precedence over `SUITE` (including its default). It cannot be
combined with individual `AGENT`, `SKILL`, or `SKILLS` selectors. A package
recursively resolves its `depends_on` packages and installs their combined
agent and skill membership plus required linked skills and resources; it
does not infer extra members from source categories. `LANGUAGE_SKILLS` retains
its include/exclude behavior for full-package seeds, without dropping linked
dependencies. Current packages do not bundle all language-specific skills;
select additional language skills using existing suite commands.

Packages use the same scope, staging, additive updates, conflict checks, and
ownership manifest as suite installs. Installing another package adds its files
without removing previous packages. Versions describe maintained content, not
remote package resolution, version pinning, or a package lockfile. There is no
remote registry, download, or uninstall operation.

To author a package, add `src/packages/<name>.yaml` with explicit `agents` and
`skills` arrays. Either may be empty; a package must declare at least one member
or a non-empty `depends_on` list. Dependencies are local package IDs, not paths
or version constraints. Missing packages and dependency cycles fail both
installation and validation. Shared dependencies and overlapping members are
included only once. Newly authored functional packages should declare `core`
explicitly; the installer does not inject hidden dependencies.

An optional `references` list names repository-relative Markdown files under
`src/` (such as the selection or language matrices) that the package ships
with, so the matrices stay updatable alongside the package. They are installed
with full-package and suite installs (not with `AGENT`, `SKILL`, or `SKILLS`),
and the language matrix is omitted when `LANGUAGE_SKILLS=exclude`. Missing
reference files fail installation and validation. `core` ships the task and
documentation matrices plus the shared documentation rules, layout, and technical
guides; functional packages ship the document-type references for their area
(for example `design-and-planning` ships the feature, architecture, product, and
roadmap references); `programming-languages` ships the language matrix.

```yaml
schema_version: "1.0.0"
name: testing
depends_on: [core]
version: "0.1.0"
description: Unit, integration, end-to-end, and fuzz testing guidance.
agents:
  - unit-tester
skills:
  - unit-test-workflow
```

The [package schema](../schemas/package.schema.json) and reference checks run in
`make check` and CI. Unknown properties produce warnings rather than errors.

User installation, on either platform:

```text
make install SUITE=engineering SCOPE=user
make install SUITE=engineering LANGUAGE_SKILLS=exclude SCOPE=user
make install SUITE=engineering AGENT=benchmark-engineer SCOPE=user
make install SUITE=engineering SKILL=agent-output-standardization SCOPE=user
make plan SUITE=engineering SKILLS=code-quality-workflow,rust-code-quality
make install SUITE=engineering SKILLS=code-quality-workflow,rust-code-quality
make install SUITE=engineering SKILL=rust-code-quality LANGUAGE_SKILLS=exclude
```

Workspace installation from Windows PowerShell:

```powershell
make plan SCOPE=workspace "WORKSPACE=D:\Projects\My App" AGENT=benchmark-engineer
make install SCOPE=workspace "WORKSPACE=D:\Projects\My App" AGENT=benchmark-engineer
```

Workspace installation from Linux:

```sh
make plan SCOPE=workspace WORKSPACE="$HOME/projects/my-app" AGENT=benchmark-engineer
make install SCOPE=workspace WORKSPACE="$HOME/projects/my-app" AGENT=benchmark-engineer
```

Stage generated output without touching a client installation:

```powershell
make install "DESTDIR=$env:TEMP\toolkit-preview" AGENT=benchmark-engineer
```

```sh
make install DESTDIR="$HOME/toolkit-preview" AGENT=benchmark-engineer
```

Use a dedicated staging directory, not a home directory or repository root. The installer rejects dangerous roots, source-tree destinations, and symlink destinations. It never removes existing installations or configures additional discovery paths.

## Generated resources and updates

Metadata and tool aliases are preserved. Relative Markdown file links outside code examples are rewritten, including heading fragments. Owner-prefixed templates and references are placed with their skills; common references such as the [documentation references](../src/skills/documentation/references/documentation), and other navigation resources, retain source-relative paths under `agentic-toolkit/resources`. Linked repository documentation is included as a snapshot with its outbound links pointing to the online repository, rather than expanding installation to the whole repository. The MIT license is included under `agentic-toolkit`.

The installer discovers definitions from source frontmatter and follows required Markdown file links. Links from the maintained skill and documentation matrices to skill definitions are treated as navigation, not dependencies; the installer keeps available entries local and points unavailable entries back to their maintained source. The human-readable catalogues are not a second installation manifest. Sources currently use inline Markdown links. New dependency-link syntax needs corresponding installer support and tests.

## Shared engine and client adapters

The Make targets and shared installer do not need a separate copy per client:

- **Shared engine:** source discovery, suite/agent/skill selection, recursive dependencies, resource ownership, relative-link rewriting in agents, skills and supporting documents, install planning, ownership checks, and locking.
- **Common utilities:** [client-independent helpers](../scripts/utils.py) for frontmatter validation, Markdown link parsing/resolution, hashing, safe relative paths, and atomic file replacement. Utilities do not depend on the installer or client adapters.
- **Client adapter:** user/workspace roots, generated agent/skill filenames, definition metadata/tool translation, and the client compatibility notice. Copilot translation currently preserves definition content because the source metadata already targets Copilot.
- **Client registry:** the explicit [adapter contract and registry](../scripts/clients/__init__.py) select only implemented clients. There is no dynamic import from user input and no fallback to Copilot for an unknown client.

To add Claude later, implement a separate adapter against `ClientAdapter`, register it, and test its actual discovery layout, metadata/tool translation, references, and role boundaries. Existing Make commands then select it through `CLIENT` without duplicating install logic. No Claude adapter is provided now; `CLIENT=claude` fails explicitly.

Definition translation runs before the shared dependency and link pass. Both resource placement and rewritten links use the selected adapter's definition paths, so links are not tied to Copilot filenames. An adapter must preserve linked dependencies and approval boundaries or reject unsupported translation rather than silently dropping guidance. Alternate-layout tests exercise this boundary but do not establish Claude compatibility.

For direct Python invocation, use `python -B -m scripts.install plan` from the repository root (`python3` on Linux); Make exports the documented variables and invokes the same module.

## Update safety

An ownership manifest, `.agentic-toolkit.json`, records generated relative paths and content hashes. Re-running the same command updates unmodified managed files and leaves unchanged files untouched. Additional selections are additive: previously installed agents and skills remain. Removed or renamed source definitions are not pruned; uninstall and migration from manually copied definitions are not provided.

Switching an existing installation to `LANGUAGE_SKILLS=exclude` does not remove previously installed language skills. The option controls the current selection, not cleanup; use a fresh staging directory to preview an exclude-only layout.

An unmanaged name collision or locally modified generated file stops installation before generated-file writes. Preserve or move the conflicting file before retrying; do not delete the ownership manifest to bypass the check. Unrelated files are left alone. The manifest records ownership, not a signature or security boundary.

An exclusive `.agentic-toolkit.lock` blocks concurrent installers. Files are replaced atomically one at a time; the whole install is not transactional. An interruption or storage error may leave a partial install or stale lock. Inspect and preserve affected output before recovery, remove a stale lock only after confirming no installer is active, and resolve unmanaged collisions before retrying. There is no automatic rollback or broad cleanup.

## Validation and client checks

```text
make check
```

This first runs the [manifest validator](../scripts/validate_manifests.py) against the maintained schemas and cross-file references, then runs the [installer regression tests](../tests/test_install.py) in temporary directories, not active user configuration. It checks suite and individual selection, resource inclusion, generated file links, preserved agent metadata, conflict protection, repeat updates, and CLI planning/install behavior. The [manifest schema guide](reference/manifest-schemas.md) describes which source types currently use each schema.

After installation, start a fresh Copilot session and verify that the selected agent appears, skills can be invoked, and linked resources can be read. Check tool availability and approval-gated subagent delegation in that client. Tool declarations and prose are not hard permission enforcement. If the client cannot delegate approved reviewer fixes, the reviewer must report the limitation, not edit directly.

Windows execution, Linux execution, and actual client behavior require separate evidence; portable Python and valid generated files alone do not certify all three. No remote workflows or client sessions are launched by these commands.
