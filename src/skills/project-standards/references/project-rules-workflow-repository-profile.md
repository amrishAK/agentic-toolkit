# Repository profile

The [setup workflow](../project-rules-workflow.md) uses a small, version-controlled YAML profile to retain confirmed project characteristics and avoid repeated interviews. Reuse an established equivalent; otherwise propose `project-profile.yaml` at the consuming repository root. This reference defines the default format, not an executable installer manifest or a requirement to add a profile to every repository.

## Field rules

- `schema_version` is the integer `1` for this format. Report unsupported versions or invalid/duplicate-key YAML without overwriting or silently migrating the file.
- `project` records name, short confirmed summary, audience, and stage. Stage examples are `prototype`, `pre-release`, and `released`.
- `repository.type` describes purpose, for example `software`, `documentation`, `tooling`, `template`, or `mixed`. `repository.layout` distinguishes `single-project` from `monorepo`.
- `applications` is a list, not one repository-wide application type. Each entry has a name, type, and repository-relative path. Typical types are `executable`, `library`, `web`, and `service`; use a clear project-specific type when needed. `interface` is optional, such as `cli` or `desktop`. Use multiple entries for multiple deliverables, even if they share a path.
- `languages` lists maintained languages, not every transitive dependency. Link toolchain/version details to their authority rather than duplicating them.
- `build.state`, `ci.state`, and `cd.state` use `present`, `absent`, `not-applicable`, or `unknown`. Present means configuration exists, not that execution passed. Absence/disabled behavior must be evidenced or confirmed; an unconfigured but desired pipeline remains absent, not present.
- When build is present, `build.systems` lists native mechanisms such as Cargo, CMake, MSBuild, or npm scripts. `build.entry_point` optionally names the shared interface, such as Make or a maintained script; a wrapper is not a replacement build graph.
- When CI or CD is present, `providers` lists the actual providers; `configuration` lists existing repository-relative configuration paths when available. CD may include non-sensitive `targets`, such as a package registry or service environment. Never include endpoints, credentials, account identifiers, or machine-local details.
- `platforms.intended` lists intended operating systems/runtimes. It is not a tested-platform list; actual results remain with their evidence.
- `authorities` optionally maps topics to existing repository-relative documentation/configuration paths. Profile paths resolve from the repository root. Do not link proposed or nonexistent files.
- Use `null` for an unknown scalar/list, `[]` for a confirmed empty list, and `not-applicable` for an inapplicable state. Omitted optional fields are unspecified, never implicitly false or disabled. Explicitly resolve or defer core fields above during setup; omit irrelevant optional fields.
- For monorepos, use application paths and list the established systems/providers. Add per-application details only when shared values cannot describe the project accurately, documenting the agreed extension rather than inventing a configuration framework.

The field examples are suggestions, not a closed ecosystem inventory. Do not force a documentation or mixed repository into an executable application model. A documentation-only project may have `applications: []` and still have a documentation build and CI.

## Example

This fictional example demonstrates the format. It is not a copy-ready profile for the toolkit or another repository; replace all values using evidence and confirmed answers, and include configuration paths only if they exist.

```yaml
schema_version: 1

project:
  name: example-project
  summary: "A command-line tool and library for processing local data."
  audience: "Developers working with local datasets."
  stage: pre-release

repository:
  type: software
  layout: single-project

applications:
  - name: example-cli
    type: executable
    interface: cli
    path: .
  - name: example-library
    type: library
    path: .

languages:
  - rust

build:
  state: present
  systems:
    - cargo
  entry_point: make

ci:
  state: present
  providers:
    - github-actions
  configuration:
    - .github/workflows/check.yml

cd:
  state: absent

platforms:
  intended:
    - linux
    - windows

authorities:
  development: README.md
  toolchain: Cargo.toml
```

## Maintenance and authority

- Prefill from evidence, interview gaps, and confirm before setup writes. Later authorized updates change affected fields and directly related docs together; they do not require the full interview.
- Recheck relevant fields against configuration and project instructions before using them. Surface contradictions; neither the profile nor detected code silently overrides intended contracts or policy.
- Record only current, confirmed setup and explicitly labelled intended platforms. Future infrastructure belongs in a proposal, not the current profile. The file grants no execution, installation, deployment, or delivery permissions.
- Keep the README human-facing. Summarize relevant profile information but link detailed procedures/configuration rather than generating a YAML dump.
- Keep feature progress, validation results, interview transcripts, session data, secrets, and personal paths out of the profile. Audit mode reports discrepancies without modifying it.
- Validation checks syntax, field types/states, real paths, and consistency with evidence. This is a guidance format; the toolkit's installer does not parse or validate consuming-project profiles.
