---
name: c-source-documentation
description: "Use for reviewing or writing C source documentation and Doxygen comments. Covers public C contracts, pointer/length inputs, ownership, allocation failures, errors, concurrency, portability, and comments-only validation."
---

# C source documentation

## When to use

Use this skill for reviewing or writing C source documentation and Doxygen comments.

## Scope and boundaries

Apply within authorized comments-only scope. Respect the selected C standard, compilation mode, platform, and existing documentation tooling.

## Procedure

### Document

- Use the project's Doxygen/comment style; do not require `/** */` when supported alternatives are established.
- Document public headers and meaningful internal invariants. Keep canonical contracts at declarations; avoid duplicating them at definitions.
- State accepted inputs, nullability, pointer/length relationships, buffer capacity, overlap/aliasing constraints, and output validity on failure where relevant.
- Explain ownership transfer, borrowed lifetimes, matching release operations, partial initialization/cleanup, and allocator requirements.
- Document allocation and `realloc` failures and size-zero behavior only as guaranteed by the API and supported standard/allocator.
- Describe actual return/error conventions; mention `errno`, assertions, thread safety, reentrancy, and synchronization only where evidenced. Do not promise rejection of undefined inputs.
- Use relevant `@param` directions, `@return`/`@retval`, and preconditions/warnings without empty boilerplate or redundant type descriptions.
- Keep examples valid C with checked failures and cleanup. Preserve C/C++ linkage, preprocessor structure, line continuations, and tool-consumed annotations.

### Validate

Inspect the diff for comments-only edits and valid placement; comments can affect preprocessing or code separation.

Use existing Doxygen generation/warning checks and relevant supported C/shared-header compilation checks when needed. Compile changed examples through established tooling where available; do not add a harness or dependency by default. Report exact results and unverified examples without claiming compilation proves the contract.
