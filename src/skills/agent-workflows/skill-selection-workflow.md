---
name: skill-selection-workflow
description: "Use at runtime to consult the skill matrices and select task-specific and language-specific guidance for an agent."
---

# Skill selection workflow

## When to use

Use this skill at runtime to consult the skill matrices and select task-specific and language-specific guidance for an agent.

## Scope and boundaries

Use this workflow when a task needs guidance beyond the active role's required procedures. Load it before choosing additional skills, then acquire only the maintained guidance relevant to the task. It selects guidance; the active agent remains responsible for the work, required procedures, and authorization.

## Procedure

### Select and acquire guidance

1. Keep workflows explicitly required by the active role in force. Identify the task and whether it needs additional guidance; do not use this workflow as a reason to load unrelated skills.
2. Open the applicable suite's task matrix. The maintained [Software Product Development task matrix](references/skill-selection-workflow-matrix.md) holds task signals and skill links across product management, engineering, and quality; match the task to relevant task-specific or cross-cutting entries and select only what applies. Use the matrix rather than copying its routing data here or choosing from memory.
3. When Engineering work needs language-specific code quality, testing, benchmarking, or source-documentation guidance, identify relevant languages from source, build configuration, harnesses, and interfaces—not file extensions alone—and consult the [language matrix](../programming-languages/references/programming-language-matrix.md). For an unlisted language, use its general code-quality fallback where applicable and select shared task workflows for other task types where available; do not imply language-specific coverage. For mixed-language boundaries, select guidance for each relevant side.
4. Acquire each selected skill by its exact name when the client supports invocation; otherwise read its maintained source and relevant references. If a required matrix or selected skill cannot be accessed, report the blocker without inventing a selection, substituting another skill, or claiming the guidance was applied.

The task matrix routes task categories to shared or task-specific skills; the language matrix supplements it with per-language guidance. Neither matrix is a runtime registry or a checklist. Selection does not authorize installation or task actions.
