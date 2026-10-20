# Agentic Toolkit

Reusable agent roles and task workflows for software product work—from planning and feature design to implementation, testing, and review.

Explore the guidance, use what fits your task, or install selected content into Copilot. The sources are maintained here so improvements can be shared instead of drifting across personal copies.

## Explore the collection

- **Find a starting point:** browse the [Software Product Development suite](docs/suites/software-product-development.md) by task, or use the [quick-start guide](docs/guides/quick-start.md).
- **See the available roles and workflows:** browse [agents](src/agents/) and [skills](src/skills/). Agents describe responsibilities; skills provide reusable task methods.
- **Understand the project:** read the [project overview](docs/project-overview.md) for the purpose, intended audience, and boundaries.

## Try it with Copilot

The installer needs GNU Make, Python 3.10 or newer, and the dependencies in `requirements.txt`. From the repository root:

```text
python -m pip install -r requirements.txt
make list
make plan AGENT=code-engineer SCOPE=user
make install AGENT=code-engineer SCOPE=user
```

On Linux, use `python3` instead of `python` when needed. Review the plan before installing: user scope writes guidance under `.copilot` in the Python user's home directory. For workspace installs, other selections, or safe-update details, see the [quick-start guide](docs/guides/quick-start.md) and [installation guide](docs/installation.md).

## Usage and compatibility

This repository contains maintained source definitions, not an automatically discoverable agent installation or runtime. The installer currently supports Copilot layouts only; other clients and suites are not supported. After installing, confirm that your Copilot client discovers the files and provides the required tools. Installation tests do not certify client discovery or behavior.

For the current installer behavior, compatibility limits, and source-versus-generated layout, see the [installation guide](docs/installation.md). The [project overview](docs/project-overview.md) distinguishes current capabilities from proposed direction.

## Maintaining the collection

- Keep agent and skill definitions in `src/agents/` and `src/skills/`. Suite and package manifests—not source folders—define what can be selected for installation.
- Keep linked resources and relative links up to date when adding, moving, or renaming definitions. Use the [definition-authoring guide](docs/reference/definition-authoring.md) for content ownership and the [repository glossary](docs/reference/glossary.md) for canonical terms.
- Before changing suite or package manifests, consult the [manifest schema guide](docs/reference/manifest-schemas.md). Keep generated client files separate from maintained sources.
- Use `make check` for manifest validation and installer tests. For content changes, also review frontmatter, role boundaries, links, and the full diff; `git diff --check` catches whitespace errors.

### Validation

`make check` validates manifests and runs the installer tests. These checks do not establish client discovery, runtime behavior, or compatibility with other clients. Check content links and definition metadata as part of review; inspect untracked files separately because Git diff does not include them by default.

## Repository scope

This is a pre-release source-content repository for reusable guidance and a local Copilot installer. The current suite is Software Product Development, covering product management, engineering, and quality. Additional suites, client adapters, and release automation are not established; the proposed V2 overview is not an approved roadmap. Use [Conventional Commits](https://www.conventionalcommits.org/) for repository changes.

See [AGENTS.md](AGENTS.md) for contributor instructions.

## Acknowledgments

The simplicity guidance in the [agent guidelines](src/skills/agent-workflows/agent-guidelines.md) draws on [Ponytail](https://github.com/DietrichGebert/ponytail), adapted here as role-independent agent guidelines.

## License

[MIT](LICENSE). Copyright (c) 2026 Amrish Arunachalam Kulasekaran.
