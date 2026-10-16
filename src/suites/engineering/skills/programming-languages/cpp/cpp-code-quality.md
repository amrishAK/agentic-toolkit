---
name: cpp-code-quality
description: "Use for reviewing, writing, fixing, or refactoring C++ code. Covers RAII, lifetime safety, exception guarantees, copy/move contracts, templates, concurrency, portability, and supported compiler validation."
---

# C++ code quality

Apply with the code-quality workflow and authorized task scope; this skill does not authorize edits.

## Review and implement

- Respect standard/compiler/library, ABI/runtime, exception/RTTI policy, platform, and freestanding/real-time constraints. Shared headers may also have C consumers.
- Prefer value semantics, RAII, and Rule of Zero. Define/delete special members only when ownership or copy/move semantics require it.
- Prefer exclusive ownership where appropriate; justify shared ownership. Raw pointers/references can express non-owning access.
- Review exception guarantees, partial construction, and state changes. Apply `noexcept` only when valid and account for moves/container behavior.
- Use public virtual base destruction when supported, or protected nonvirtual destruction to prohibit base deletion. Do not require public polymorphic destruction universally.
- Check slicing, dangling references/views/iterators, captures, temporaries, invalidation, and moved-from operations against their contracts.
- Check initialization, nullability, bounds, arithmetic, alignment, aliasing/lifetimes, overflow, shifts, narrowing, and format compatibility.
- Choose value/reference passing by semantics and cost. Small values do not universally need `const&`.
- Use composition, templates/concepts, or runtime interfaces for demonstrated needs; preserve substitution contracts rather than imposing SOLID mechanically.
- Preserve headers/guards, linkage, template visibility, one-definition rule, API/ABI, and C interfaces. Do not let exceptions escape C-facing boundaries.
- Review synchronization, predicates, atomics, shutdown, and lifetime. Shared ownership does not make the pointee thread-safe; `volatile` is not synchronization.
- Document caller-visible ownership, lifetime, errors, and thread safety; review layout/width/endian/platform assumptions.

## Validate

Build/test relevant targets and template instantiations/shared-header modes. Use supported warnings/static analysis, instrumented ASan/UBSan, or separate TSan where useful; Valgrind is platform-dependent.

Consult supported compiler/library documentation and current C++ references/Core Guidelines when uncertain; compatibility and language rules take precedence over guideline slogans.
