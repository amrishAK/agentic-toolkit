# Architecture and scope

## Boundaries

- Organize code in layers with a clear direction of dependency, for example platform primitives, then handlers, then the public API.
- Isolate platform- or backend-specific code in its own module behind one shared interface or dispatch point, such as per-OS socket modules or per-database backends.
- Make public and internal modules explicit. Changing a public contract requires a deliberate decision, not a side effect.
- Write down invariants that the API enforces, such as lifecycle or typestate order, so changes do not weaken them.
- Each module owns its error type. Map errors explicitly at layer boundaries rather than leaking lower-level errors unchanged.

## Scope

- Every project documents its non-goals. Do not add features that a non-goal rules out.
- Keep current behaviour separate from planned work everywhere: the README status section, `docs/architecture/` versus `docs/proposals/`, and code comments.

## Repository layout

Use this repository-wide map to explain placement and propose a suitable structure, not to scaffold every row. Paths below are examples, not existing project paths or required names. Preserve established layouts, workspace/package boundaries and ecosystem conventions. Distinguish production, test-only, documentation and generated resources by ownership even when the ecosystem colocates them.

| Item / example paths | Purpose and contents | When applicable / what belongs elsewhere |
|---|---|---|
| Production code and public interfaces: `src/`, package directories, `include/` or ecosystem equivalents | Runtime/library modules, public headers or exported interfaces; distinguish public contracts from internals | Where the project maintains code or interfaces. Follow the [language-specific skill matrix](../../programming-languages/references/programming-language-matrix.md) for language guidance; test helpers and generated output are not production modules. |
| Tests: inline modules, adjacent test files, `tests/` | Unit tests of local behavior, integration tests of real interactions, E2E journeys through external interfaces | Include only established or separately approved tiers. Follow [testing conventions](project-conventions-testing.md) and language guidance for placement; do not impose a runner or move inline unit tests into a new directory. |
| Fixtures and test infrastructure: `tests/fixtures/`, `tests/data/`, established test-support locations | Small test data, test helpers, seed SQL, test-only Compose/configuration and setup/teardown resources | When tests need them. Document lifecycle and prerequisites per testing guidance; do not mix test-only resources with production deployment configuration or ship them as runtime assets. |
| Documentation: `docs/`, root documentation entry points | Explanations, contracts, guides, proposals, status and evidence, each with a canonical owner | Select useful documents through the [document catalogue](../../documentation/references/documentation-matrix.md) and [docs layout requirements](../../documentation/references/documentation/docs-layout.md). Implementation, executable tests and scripts belong in their owning locations, not the docs tree. |
| Scripts and tools: `scripts/`, `tools/`, established developer-tool packages | Maintained automation and developer utilities; document entry points and prerequisites | When automation exists or is separately approved. Production features belong in production modules; generated executables and local environments are outputs, not maintained tools. |
| Examples: `examples/`, ecosystem example targets | Small supported usage demonstrations and required sample data/configuration | When demonstrations help consumers. Distinguish examples from tests, benchmark workloads and production applications; use no real credentials. |
| Benchmarks: `benches/`, `benchmarks/`, ecosystem benchmark targets | Measured workloads and harness sources; link methodology and results from their documented owner | When performance measurement is established or separately approved. A proposed performance gate is not an implemented harness; ordinary examples/tests and generated result files have different owners. |
| Build/dependency manifests and shared configuration: root or package manifests, lockfiles, tool configuration, existing CI locations | Package boundaries, dependencies, toolchain/format/lint/build settings and shared workflow definitions | Follow the ecosystem and existing [entry points](project-conventions-entry-points.md). Retain required lockfiles/shared settings; machine-local overrides belong outside shared configuration. Creating or changing infrastructure requires separate approval. |
| Client/agent guidance: `AGENTS.md`, applicable scoped instructions, existing client-specific locations | Navigation and durable project constraints; narrowly scoped rules and recurring project procedures where needed | Use the [setup workflow's routing](../project-rules-workflow.md#2-choose-the-right-place-for-each-rule) and supported host conventions. Do not generate every client's directory; detailed contracts, plans and mutable status belong in their documentation owners. |
| Generated outputs and local secrets: ecosystem build/cache/output directories, local environment/configuration files | Reproducible artifacts and machine-local state, kept separate from maintained inputs; never include secret values in guidance | Derive ignore rules from actual tools using the [safeguards](../project-rules-workflow.md#license-and-ignore-file-safeguards). Respect intentionally tracked generated files; retain sanitized templates and intended fixtures. Do not delete/untrack files incidentally or treat secrets as fixtures. |

During setup, use the [interview's structure proposal](project-rules-workflow-setup-interview.md#structure-proposal-and-refinement) to identify existing, proposed and deferred paths and obtain confirmation before writing. Record the adopted layout through a compact navigation map in `AGENTS.md`, linking existing owners and detailed guides rather than copying this table.

## Naming

- Keep the repository, package, and crate or library names consistent. When a project is renamed, update or explicitly note every place that still uses the old name.
- Spell file and identifier names correctly and consistently. Fix misspellings when the affected code is already being changed or when asked; do not mass-rename as a side effect.
