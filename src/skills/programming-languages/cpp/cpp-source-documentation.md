---
name: cpp-source-documentation
description: "Use for reviewing or writing C++ source documentation and Doxygen comments. Covers ownership/lifetimes, exception guarantees, copy/move contracts, templates, invalidation, concurrency, and comments-only validation."
---

# C++ source documentation

## When to use

Use this skill for reviewing or writing C++ source documentation and Doxygen comments.

## Scope and boundaries

Apply within authorized comments-only scope. Respect the supported standard/compiler/library, exception policy, ABI, and existing tooling.

## Procedure

### Document

- Follow established Doxygen/comment syntax; place canonical contracts at public declarations and explain non-obvious implementation rationale locally.
- State preconditions, ownership/borrowing, lifetimes, iterator/reference/view invalidation, side effects, and thread-safety obligations where relevant.
- Describe actual copy/move behavior; copies need not be deep and moved-from objects need not be empty. Identify permitted post-move operations from evidence.
- Document promised exception guarantees and meaningful failure conditions, respecting no-exceptions builds. Do not claim `noexcept` prevents termination or all failure.
- Explain template requirements, supported operations/types, and semantic constraints beyond what signatures/concepts already express.
- Describe virtual-interface substitution and destruction contracts where relevant, not blanket smart-pointer or destructor policies.
- Include complexity/performance guarantees only when established; distinguish guaranteed complexity from measured speed.
- Use concise summaries and relevant parameter/return/precondition notes. Keep examples compatible with supported versions and realistic RAII/error handling.
- Preserve macros, directives, attributes, and tooling annotations. Shared C interfaces also need C caller contracts; exceptions must not be described as crossing a prohibited boundary.

### Validate

Review the diff for comments-only changes and safe placement. Use existing Doxygen warning/build checks and relevant supported compilation/template checks when needed.

Validate changed examples through established tooling where available; report unexecuted examples and unavailable checks. Diagnose failures rather than assuming documentation edits caused them.
