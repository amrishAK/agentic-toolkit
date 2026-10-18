# Documentation

Start with the [repository README](../README.md) for maintenance guidance and client compatibility limits. Read the [project overview](project-overview.md) for purpose, audience, organization, and scope boundaries.

## Current documentation

- [Copilot installation](installation.md): Make commands, prerequisites, installation scopes, safe updates, and validation.

For terminology and source-authoring requirements, see the [reference guides](reference/):

- [Repository glossary](reference/glossary.md): canonical terminology for maintained guidance.
- [Definition authoring](reference/definition-authoring.md): content ownership and requirements for agents, skills, references, templates, and catalogues.
- [Agent definition structure](reference/agent-definition-structure.md): recommended organization, metadata, and a copy-ready starter for maintained agent sources.
- [Skill definition structure](reference/skill-definition-structure.md): maintained skill source layout, generated installation layout, and a copy-ready starter.

## Proposals

The following documents describe possible future direction and use; they are not descriptions of currently available suites or capabilities.

- [V2 project overview](proposals/project-overview-v2.md): a proposed lifecycle model connecting Discovery & Shaping, Product Management, and Engineering.

The [guides](guides/) include a [quick start](guides/quick-start.md) for using current Engineering guidance and two practical guides for applying the proposed model:

- [Using Agentic Toolkit effectively](guides/using-agentic-toolkit-effectively.md): applying it proportionately while preserving traceability and human review.
- [Using Agentic Toolkit as a solo developer](guides/using-agentic-toolkit-as-a-solo-developer.md): adapting it for an individual project owner.

Separate early-stage proposals for a Learning and Research Workspace, a Learning and Research App, and a Local File Editor are maintained outside this repository; they do not describe current Agentic Toolkit capabilities.

## Suite guides

| Suite | Guide | Coverage |
|---|---|---|
| Engineering | [Engineering suite](suites/engineering.md) | Agent responsibilities, skill categories, shared guidance, and task handoffs |

Only suites with maintained content are documented. Research, standalone product, and everyday-assistance suites are not currently present.

## Shared agents

- [Technical documentation writer](../src/shared/agents/review/technical-documentation-writer.md): reviews, writes, and updates project documentation using the documentation-selection workflow and applicable document-type rules.

For task-to-skill selection, use the shared [skill selection workflow](../src/shared/skills/skill-selection-workflow.md) and its [Engineering category-level selection matrix](../src/shared/skills/references/skill-selection-workflow-matrix.md). Language-specific Engineering selection is delegated to the [Engineering language-specific skill matrix](../src/shared/skills/references/programming-language-matrix.md).

The guides explain how to navigate the sources; they are not client installation instructions. Agent and skill definitions remain authoritative for their detailed contracts. Update the relevant guide when changing suite responsibilities or organization.
