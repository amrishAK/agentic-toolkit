# Manifest schemas

The maintained JSON Schemas in [`schemas/`](../../schemas/) use JSON Schema
Draft 2020-12 and describe skill frontmatter, agent manifests, suite manifests,
installation packages, selection matrices, and language packs. The current schema version for the YAML
manifest types is `1.0.0`; `version` identifies the manifest content itself.

## Current source layout

The schemas define the intended manifest contracts without replacing the
repository's existing source layout:

- Skills remain Markdown definitions with Agent Skills frontmatter. The skill
  schema validates `name`, `description`, and the supported optional frontmatter
  properties; it does not require an additional `schema_version` field, so the
  generated Copilot skill metadata remains compatible.
- Agents remain Markdown definitions discovered from frontmatter. An
  `agent.yaml` manifest schema is available for future use; the current source
  collection does not yet contain these manifests.
- Suites remain explicit YAML manifests under `src/suites/`. The installer
  resolves their `packages` lists into agent and skill membership. Direct
  `agents` and `skills` lists remain supported and are merged when present.
- Functional packages under [`src/packages/`](../../src/packages/) contain
  explicit `agents` and `skills` lists and are selected with `PACKAGE=<name>`.
  The [package schema](../../schemas/package.schema.json) requires both lists
  and at least one member or a non-empty `depends_on` list. Dependency IDs must
  resolve to local package manifests; cycles are rejected. Functional packages
  with agents explicitly depend on the shared `core` package, which includes documentation
  agents plus output, documentation, and selection skills. An optional
  `references` list names `src/` Markdown files (matrices) the package ships. Packages are distinct
  from language packs.
- Selection-matrix and pack schemas are available. The current repository
  selection matrices are Markdown references, and no language-pack manifests
  are maintained yet.

The manifest validator checks every matching manifest found in the source tree,
so adding an agent or pack manifest automatically enables schema and
cross-reference validation for it. Suite `skills` remains supported to
preserve the installer's explicit suite membership; `optional_agents` and
`language_packs.optional` are validated but are not part of the installer's
default selection.

## Compatibility and validation

Unknown fields are accepted and reported as warnings. Required fields, types,
enums, identifier syntax, versions, and relative paths are validated by the
schemas. Cross-file validation checks suite and agent references, matrix
signals and skills, matching required/excluded matrix conditions, and
pack-relative files.

Run validation and the regression tests locally with:

```text
make check
```

The GitHub Actions workflow runs the same manifest validator and tests on
pushes and pull requests. Schema validation does not certify client discovery,
runtime behavior, or permission enforcement.
