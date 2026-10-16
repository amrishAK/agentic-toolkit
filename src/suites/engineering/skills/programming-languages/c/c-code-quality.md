---
name: c-code-quality
description: "Use for reviewing, writing, fixing, or refactoring C code. Covers ownership, allocation, cleanup, undefined behavior, concurrency, portability, public contracts, and supported compiler validation."
---

# C code quality

Apply with the code-quality workflow and authorized task scope; this skill does not authorize edits.

## Review and implement

- Respect the selected C standard, compiler, platform/ABI, dependencies, and freestanding/embedded/real-time constraints. Determine compilation mode from configuration, not header extensions.
- Check initialization, nullability, bounds/lengths, pointer arithmetic, alignment, aliasing/effective type, storage, and object lifetimes.
- Check overflow, signedness, narrowing, shift ranges, allocation-size multiplication, and format arguments. Defined unsigned wraparound may still violate the contract.
- Make ownership transfers and borrowed lifetimes clear. Release resources once on all relevant paths, including partial initialization.
- Handle allocation and `realloc` failure without losing existing storage; respect size-zero behavior for the selected standard/allocator.
- Follow project error conventions. Check meaningful failures; use `errno` only where specified and assertions only for appropriate invariants.
- Use structured cleanup, including `goto cleanup` where useful. Do not require heap allocation when stack/caller storage suffices.
- Prefer cohesive modules, opaque types, explicit contexts, and callbacks for real needs, not artificial class hierarchies.
- Preserve headers/guards, prototypes, linkage, API/ABI, and C++ consumer compatibility; keep production C compiled as C.
- Check synchronization, lock order, predicates, atomic publication, shutdown, and cross-thread lifetimes. `volatile` is not synchronization.
- Review width, endian, layout, extensions, and platform assumptions. Document caller-visible ownership, valid inputs, failures, and thread safety.

## Validate

Run relevant project builds/tests and shared-header compilation modes. Use supported warnings/static analysis or ASan/UBSan and separate TSan where useful; environment variables alone do not instrument binaries. Valgrind is platform-dependent.

Consult supported compiler documentation, current C references, and relevant CERT C guidance when uncertain. Do not treat guidelines or passing checks as proof of correctness.
