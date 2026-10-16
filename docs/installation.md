# Copilot installation

The reusable [Makefile](../Makefile) delegates to the standard-library [installer](../scripts/install.py), which selects a client adapter through `CLIENT`. The [Copilot adapter](../scripts/clients/copilot.py) is currently the only implementation. It generates Copilot layouts from maintained sources without symlinks, downloads, package installation, or changes to client settings.

## Prerequisites and scope

- GNU Make and Python 3.10+ on `PATH`. No Python packages are required.
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
make plan CLIENT=copilot SUITE=engineering SCOPE=user
```

`plan` resolves dependencies, checks destination conflicts, and prints generated paths without creating directories or files. `install` uses the same variables and performs the writes.

| Variable | Meaning |
|---|---|
| `CLIENT` | Only `copilot` is currently accepted |
| `SUITE` | Suite directory name; defaults to `engineering` |
| `AGENT` | Optional agent name within the suite |
| `SKILL` | Optional skill name within the suite or shared skills; mutually exclusive with `AGENT` |
| `SCOPE` | `user` or `workspace`; defaults to `user` |
| `WORKSPACE` | Existing project directory; required for workspace scope unless staging |
| `DESTDIR` | Optional exact installation root, replacing `.copilot` or `.github`, for staging |
| `PYTHON` | Python executable used by Make |

Omit `AGENT` and `SKILL` to install all agents and skills in a suite. Single-agent selection installs that agent plus transitively linked skills, catalogues, templates, and references, including shared guidance. Catalogues can link most of the skill collection; selection is not a promise of a small skill count. Cycles are resolved once. Skill selection does not install unrelated agents.

## Install examples

User installation, on either platform:

```text
make install SUITE=engineering SCOPE=user
make install SUITE=engineering AGENT=benchmark-engineer SCOPE=user
make install SUITE=engineering SKILL=agent-output-standardization SCOPE=user
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

Metadata and tool aliases are preserved. Relative Markdown file links outside code examples are rewritten, including heading fragments. Owner-prefixed templates and references are placed with their skills; catalogues and other navigation resources retain source-relative paths under `agentic-toolkit/resources`. Linked repository documentation is included as a snapshot with its outbound links pointing to the online repository, rather than expanding installation to the whole repository. The MIT license is included under `agentic-toolkit`.

The installer discovers definitions from source frontmatter and follows Markdown file links; the human-readable catalogues are not a second installation manifest. Sources currently use inline Markdown links. New dependency-link syntax needs corresponding installer support and tests.

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

An unmanaged name collision or locally modified generated file stops installation before generated-file writes. Preserve or move the conflicting file before retrying; do not delete the ownership manifest to bypass the check. Unrelated files are left alone. The manifest records ownership, not a signature or security boundary.

An exclusive `.agentic-toolkit.lock` blocks concurrent installers. Files are replaced atomically one at a time; the whole install is not transactional. An interruption or storage error may leave a partial install or stale lock. Inspect and preserve affected output before recovery, remove a stale lock only after confirming no installer is active, and resolve unmanaged collisions before retrying. There is no automatic rollback or broad cleanup.

## Validation and client checks

```text
make check
```

This runs the [installer regression tests](../tests/test_install.py) in temporary directories, not active user configuration. It checks suite and individual selection, resource inclusion, generated file links, preserved agent metadata, conflict protection, repeat updates, and CLI planning/install behavior.

After installation, start a fresh Copilot session and verify that the selected agent appears, skills can be invoked, and linked resources can be read. Check tool availability and approval-gated subagent delegation in that client. Tool declarations and prose are not hard permission enforcement. If the client cannot delegate approved reviewer fixes, the reviewer must report the limitation, not edit directly.

Windows execution, Linux execution, and actual client behavior require separate evidence; portable Python and valid generated files alone do not certify all three. No remote workflows or client sessions are launched by these commands.
