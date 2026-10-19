---
name: csharp-source-documentation
description: "Use for reviewing or writing C# XML source documentation. Covers reachable API contracts, nullability, exceptions, disposal, async behavior, examples, and documentation checks."
---

# C# source documentation

## When to use

Use this skill for reviewing or writing C# XML source documentation.

## Scope and boundaries

Apply within authorized comments-only scope. Respect supported target frameworks, language version, nullable context, and existing XML documentation conventions.

## Procedure

### Document

- Follow the project's XML documentation style. Use `<summary>` for purpose and appropriate `<param>`, `<typeparam>`, `<returns>`, `<exception>`, `<remarks>`, and `<example>` elements where they add contract information.
- Document externally reachable APIs, including the exposure created by containing types and interfaces. Do not mechanically add boilerplate to every member or repeat inherited contracts unnecessarily; use `<inheritdoc/>` where supported and appropriate.
- Describe preconditions, nullability, ownership, disposal responsibilities, side effects, and thread-safety obligations when they are not clear from signatures or established conventions.
- For asynchronous APIs, explain cancellation behavior, relevant completion effects, and meaningful exceptions. Distinguish cancellation from other failure results when the API does.
- Keep documented exceptions evidence-based; do not imply that every implementation detail or incidental exception is guaranteed.
- Ensure examples are minimal, compilable for supported target frameworks, and demonstrate realistic disposal and error handling. Do not hide broken examples with omissions or unsupported directives.
- Preserve attributes, directives, nullable annotations, and tooling-specific markup. XML documentation must remain well-formed and must not alter executable behavior.

### Validate

Review the diff to confirm comments-only changes and correct XML attachment. Use existing XML documentation warning, build, analyzer, or documentation-generation checks for the affected targets.

Validate changed examples through established project tooling when available. Report warnings, broken references, unexecuted examples, and unavailable configurations; compilation alone does not establish that a documented contract is accurate.
