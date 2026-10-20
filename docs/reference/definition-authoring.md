# Definition authoring

Use this guide to decide what maintained agent and skill source files should contain and where their rules belong. Use the [repository glossary](glossary.md) for canonical terminology. This guide does not grant permission to change a role's responsibilities, permissions, client support, or project decisions.

## Choose the source type

| Source type | Purpose | What it should contain |
|---|---|---|
| **Agent definition** | Describes a role and its boundaries. | Valid role metadata (`name` and `description`, plus a useful `argument-hint` and the smallest relevant `tools` list where applicable); a concise role purpose; required and conditional guidance; applicable work modes; authorization and scope boundaries; and validation/reporting expectations. Link to the workflows that own detailed methods. Do not copy whole workflows into the agent or imply tool declarations enforce prose boundaries. Use the [agent definition structure](agent-definition-structure.md) and its copy-ready starter. |
| **Skill definition** | Provides a reusable method for a task or domain. | Skill metadata (`name` and task-specific `description`); scope and intended use; an ordered method where sequence matters; relevant decisions, inputs, outputs, edge cases, and failure paths; authorization boundaries; and validation/reporting appropriate to the task. Link supporting detail instead of loading unrelated guidance or duplicating another skill's method. Use the [skill definition structure](skill-definition-structure.md) for the maintained source layout and starter. |
| **Supporting reference** | Supplies focused detail for one definition or detail used by several workflows. | The specific rules, decision tables, examples, technical detail, or other material needed by its consumers; a clear title and enough context to stand alone when opened directly; and relative links to related sources. Keep the parent skill's filename prefix for owned references. Place cross-workflow references with their owning skill category and use neutral filenames when no one workflow owns them. Documentation rules and document-type guidance live under `src/skills/documentation/references/documentation/`; the routing matrix is `src/skills/documentation/references/documentation-matrix.md`. A reference is not a separately invokable skill unless it has its own skill definition and metadata. |
| **Template** | Helps produce a consistent artifact or response. | The intended use, a reusable structure, and clearly marked placeholders or examples. Keep normative rules in the owning workflow or document-type guide; templates should link to those rules rather than quietly create competing policy. |
| **Catalogue** | Routes readers to maintained definitions. | Canonical inventory, task-to-definition routing, selection guidance, ownership boundaries, and maintenance instructions. A catalogue is not a skill definition, dependency manifest, or proof of runtime availability. |
| **Project document or documentation rule** | Defines project intent, contracts, current state, or document requirements. | Follow the document's canonical owner and the applicable rules in [documentation selection workflow](../../src/skills/documentation/documentation-selection-workflow.md). A supporting reference under a skill is not interchangeable with a project-owned document in `docs/`. |

## Authoring rules

- Keep one authoritative source for each role, method, or project decision. Link to that source instead of copying it into other files.
- Write for the intended task and reader. State what applies, what is conditional, what is out of scope, and what to do when required evidence or guidance is unavailable.
- Separate the role's responsibilities from its methods: agent definitions own role boundaries; skill definitions own reusable procedures; supporting references own scoped detail.
- Make instructions operational and testable where possible. Distinguish required actions from examples, recommendations, and optional paths.
- State authorization and client limitations honestly. Instructions and declared tools describe intended behavior; they do not enforce permissions or establish runtime support.
- Preserve established naming, ownership prefixes, frontmatter, relative links, and resource inclusion patterns. Update catalogues and inbound links when a definition is added, renamed, moved, or removed.
- Use the narrowest useful scope. Do not add sections, templates, references, or mandatory workflows merely for uniformity when they do not help the role or task.
- Keep proposed behavior distinct from current behavior. Use the glossary's status terms consistently and do not turn an example or proposal into an implemented guarantee.

## Review before adding or changing a definition

1. Identify whether the change belongs in an agent, skill, supporting reference, template, catalogue, or project document.
2. Read its existing owner and directly linked sources. Reuse an existing definition when it already owns the behavior.
3. Check role boundaries, permissions, and project decisions against their owners. Ask the user when a material decision is unresolved; otherwise state a bounded assumption when the active role permits.
4. Add only the content needed for the source type; update applicable catalogues, inbound links, and directly affected docs when selection, names, or locations change.
5. Verify metadata, names, relative links, linked-resource inclusion, and catalogue routing. Run existing checks that cover the affected behavior.

For project documentation types and their owners, use the [documentation selection matrix](../../src/skills/documentation/references/documentation-matrix.md). For task-wide software product development framing, use the [shared task workflow](../../src/skills/implementation/engineering-task-workflow.md), which retains its canonical skill name.
