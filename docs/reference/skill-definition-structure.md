# Skill definition structure

Use this guide to create or reorganize maintained skill definitions in `src/`. It describes the repository source layout and the generated installation layout. For source ownership and content rules, see [definition authoring](definition-authoring.md). Source definitions are not generated client files or personal installations.

## Source and installed layout

Maintain each skill as a Markdown file named after the skill, under a category directory:

- Skills: `src/skills/<category>/<skill-name>.md`
- Suite membership: `src/suites/<suite>.yaml`, which lists canonical agent and skill names and suite metadata.

For example, `src/skills/testing/unit-test-workflow.md` is installed as `skills/unit-test-workflow/SKILL.md`. Source categories organize definitions but do not determine suite membership or appear in the installed skill directory.

## Metadata

```yaml
---
name: example-skill
description: "Use for [specific task or trigger terms]."
---
```

Use the two metadata fields shown above in maintained skill sources. `name` must use lowercase kebab-case and match the source filename stem; the installer uses it as the installed skill directory name. Make `description` specific enough to distinguish the task and trigger terms. The installer validates the name and description, then preserves the metadata when generating the installed layout. Do not add client-specific metadata unless the repository's supported installation behavior has been confirmed.

## Standard section structure

Every skill definition uses these three top-level sections, in this order, after its title:

1. **When to use:** In one short paragraph, describe the task and the situations where this skill applies. The frontmatter description supports discovery; this section helps a reader who has already opened the skill.
2. **Scope and boundaries:** State what the skill covers, what belongs elsewhere, and any relevant authorization or stop conditions. Include required inputs or assumptions here when they materially affect the method.
3. **Procedure:** Give the usable method. Use ordered steps when sequence matters and concise task-specific subsections when they improve scanning. Include decisions, failure paths, expected outputs, and validation/reporting guidance where relevant.

Use additional top-level sections only when they make substantial supporting guidance easier to find. Otherwise, put relevant links next to the procedure step that needs them. Do not add empty sections: inputs, outputs, guardrails, and validation/reporting may be integrated into the three standard sections when that reads more clearly. Keep reference-specific detail in supporting references rather than expanding every skill.

## Copy-ready starter

Replace the placeholders. Keep the three standard sections; omit optional material that adds no useful guidance.

````markdown
---
name: example-skill
description: "Use for [specific task or trigger terms]."
---

# [Skill name]

## When to use

Use this skill when [task, trigger, or conditions].

## Scope and boundaries

- Covers: [what this skill explicitly handles]
- Does not cover: [what belongs in another skill, workflow, or role]
- Requires or assumes: [material inputs, context, or constraints]

## Procedure

1. [Step 1: establish context or contract]
2. [Step 2: identify relevant files, behavior, or scope]
3. [Step 3: perform the task using the intended method]
4. [Step 4: validate and report the result, evidence, and limitations where relevant]
````

Keep each role, reusable method, and project decision authoritative in one place; link rather than copy it. Update inbound links when definitions move or change names, and verify metadata and relative links. Follow the [repository compatibility guidance](../../README.md#usage-and-compatibility); source definitions do not prove runtime discovery or behavior.
