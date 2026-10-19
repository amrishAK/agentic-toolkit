---
name: general-code-quality
description: "Use for reviewing, writing, fixing, or refactoring code in a language without dedicated code-quality guidance in the Engineering language matrix."
---

# General code quality

## When to use

Use this skill for code in a language that has no dedicated code-quality skill listed in the Engineering language matrix.

## Scope and boundaries

Use this skill alongside the shared [code-quality workflow](../../implementation/code-quality-workflow.md). It provides a general fallback, not equivalent coverage to dedicated language guidance, a formal coding standard, or language-specific safety advice. It does not authorize edits.

## Procedure

1. Identify the language, version, runtime or compiler, project toolchain, targets, and relevant constraints from project configuration and source. Do not infer them from file extensions alone.
2. Read relevant code, callers, tests, project guidance, and public contracts. Identify affected interfaces and behavior before proposing or making changes.
3. Apply the shared [code-quality guidelines](../references/code-quality-guidelines.md) and the project’s established conventions. Prioritize language correctness and safety over general design heuristics.
4. Use configured project builds, tests, formatting, and analysis tools that cover the change. Consult authoritative, version-appropriate language or tool documentation when behavior is uncertain; do not invent language-specific rules or add tools solely to complete a checklist.
5. Report exact checks and results, unsupported configurations, and remaining uncertainty. If a question depends on language-specific behavior that cannot be verified, state that limitation rather than presenting the fallback as specialist guidance.
