# Open-source baseline

**Goal:** every project meets the same open-source standard, so all of them can be maintained the same way. Requirements are staged so pre-v1 projects are not held to release standards too early.

## Stage 1 — always, from the first commit

| Item | Requirement |
|---|---|
| `README.md` | Project summary per [project tracking](../../../../../shared/skills/references/documentation/project-tracking.md), current status (link to the feature tracker when tracking is adopted), quick start, build/test commands, licence |
| `LICENSE` | A user-confirmed OSI-approved licence for open-source projects; package metadata uses the same identifier and notices are preserved |
| `.gitignore`, `.editorconfig` | Derive ignore rules from actual generated/local output without hiding intended files; set line endings, indentation, final newline |
| Formatter config | Committed and checked in CI (for example `rustfmt.toml`, `.clang-format`) |
| Linter | Run in CI with warnings treated as errors (for example clippy, clang-tidy or compiler warnings) |
| CI | A workflow on pull requests and the default branch that calls the [shared entry point](./project-conventions-entry-points.md) |
| `AGENTS.md` | Project guide, written and maintained with `project-standardizer` |
| Feature tracker | `docs/status/features.md`, required by default; omit only by an explicit, confirmed project-specific rule. When adopted, keep it current per [project tracking](../../../../../shared/skills/references/documentation/project-tracking.md) |
| Docs | The [docs layout requirements](../../../../../shared/skills/references/documentation/docs-layout.md); claims backed by evidence |
| Commits | [Conventional Commits](./project-conventions-commits.md), checked by a commit-msg hook or a CI check |

## Stage 2 — before the first public release

| Item | Requirement |
|---|---|
| `CHANGELOG.md` | [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) format with an `Unreleased` section; curate notable user-visible changes using Conventional Commits as evidence, not a raw commit dump |
| `CONTRIBUTING.md` | How to build and test, the commit convention, and the PR process; links to the docs instead of repeating them |
| `SECURITY.md` | Supported versions and a private way to report vulnerabilities |
| `.github/` templates | Issue templates (bug, feature) and a PR template with a checklist covering tests, docs, status and changelog |
| Dependency automation | Dependabot (or similar) for dependencies and GitHub Actions; a licence and advisory check (for example `cargo-deny`) |
| Toolchain floor | Minimum supported Rust version, C/C++ standard, or .NET SDK/target framework declared in the manifest and README, and tested in CI |
| Package metadata | Description, repository, licence, readme, keywords and categories, as the ecosystem requires |
| Platform matrix | CI covers every platform the README claims to support |

`CODE_OF_CONDUCT.md` is optional; add it when outside contributors arrive.

## Stage 3 — every release

- Use [Semantic Versioning](https://semver.org/). Before 1.0, breaking changes bump the minor version.
- Tag releases as `vX.Y.Z` from a clean, CI-passing commit.
- Move the `Unreleased` changelog entries under the new version and date.
- Review the public API: everything exported is intended, documented and covered by tests.
- Back every README claim (performance, coverage, guarantees) with evidence, or state it as a goal.
- Release procedure: apply `release-workflow`.

## Applying

- New projects start at Stage 1. Existing projects report their gaps by stage and fix them in order.
- This baseline is a checklist, not blanket authorization to add tooling or CI. During setup, confirm applicable items and deferred work through the [setup interview](./project-rules-workflow-setup-interview.md).
- Private/proprietary intent is not permission to add an open-source license. Follow the [license and ignore-file safeguards](../project-rules-workflow.md#license-and-ignore-file-safeguards); ask about ambiguous licensing and preserve existing rights and notices.
- Generated files must be reviewed against the real project. Do not add a template that describes commands, platforms or policies the project does not have.
