# Agent definition structure

Use this guide to create or reorganize maintained agent definitions in `src/`. It combines the recommended structure with a copy-ready starter. For source ownership and content rules, see [definition authoring](definition-authoring.md). Source definitions are not generated client files or personal installations.

## Metadata

```yaml
---
name: example-agent
description: "Use for [specific tasks and trigger terms]."
argument-hint: "Describe [the task, input, or outcome]."
tools: [read, search]
---
```

`name` must match the filename stem and use lowercase kebab-case. Make `description` specific enough to distinguish the role; keep `argument-hint` useful and `tools` limited to needed aliases. The installer validates `name` and `description`; metadata and prose do not enforce permissions or establish client support.

## Recommended section order

Use these standard headings in this order so readers can find information consistently across agent definitions. Include a section when it adds useful role-specific information; omit it only when it genuinely does not apply. Do not merge modes with authorization or reorder sections for emphasis.

1. **Role and outcome:** Identify the role and its primary result.
2. **Scope and ownership:** State what the role owns and does not own, including decisions it must hand off. Keep this about responsibility, not permissions.
3. **Required workflows:** Link the shared task workflow and any role-specific workflows the agent must follow. State when each applies; do not require unrelated suite guidance.
4. **Skills and supporting guidance:** Link required or conditional skills and references, explaining when each applies. Keep reusable methods in skills, not the agent.
5. **Modes:** Explain how the work or output changes in each applicable mode, such as review versus implementation.
6. **Authorization and guardrails:** State authorization, prohibitions, and other constraints that apply in every mode unless an explicit exception says otherwise.
7. **Output:** Include role-specific expectations; link shared output guidance instead of repeating it.
8. **Validation and reporting:** Identify evidence, incomplete results, and limitations the agent should report.

Keep modes separate from authorization and guardrails: modes describe how the work changes in a particular situation, while guardrails define what the agent may do. A mode or handoff must not imply extra authority or override a guardrail.

## Copy-ready starter

Replace placeholders. Omit a section only when it genuinely does not apply to that role; keep remaining sections in the listed order.

````markdown
---
name: example-agent
description: "Use for [specific tasks and trigger terms]."
argument-hint: "Describe [the task, input, or outcome]."
tools: [read, search]
---

## Role and outcome

You are a [role]. [State the primary responsibility and outcome.]

## Scope and ownership

- Owns: [State the responsibilities and decisions this role is accountable for.]
- Does not own: [State adjacent responsibilities or decisions that belong elsewhere, and who should receive the handoff when useful.]

## Required workflows

- Follow the shared [task workflow](relative/path/to/workflow.md) for [common task framing]. [Omit if not applicable.]
- Follow the [role-specific workflow](relative/path/to/role-workflow.md) for [role-specific method]. [Omit if not applicable.]

## Skills and supporting guidance

- Follow the [required skill](relative/path/to/skill.md) for [when and why it applies].
- Use the [conditional skill or reference](relative/path/to/reference.md) when [condition].
- If required guidance is unavailable, [state what to do].

## Modes

- [Include only if the role has distinct modes; state what changes in each mode.]

## Authorization and guardrails

- [State authorization, prohibitions, and other constraints that apply across modes.]

## Output

[State role-specific output expectations, or omit this section when shared guidance fully covers them.]

## Validation and reporting

- Verify [outcome] using [evidence].
- Report [results and limitations].
````

Keep each role, reusable method, and project decision authoritative in one place; link rather than copy it. Update inbound links when definitions move or change names, and verify metadata and relative links. Follow the [repository compatibility guidance](../../README.md#usage-and-compatibility); source definitions do not prove runtime discovery or behavior.
