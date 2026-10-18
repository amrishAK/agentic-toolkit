---
name: cpp-benchmarking
description: "Use for C++ benchmark review, planning, implementation, execution, or analysis. Covers RAII lifecycle, allocation, copy/move costs, optimization barriers, representative types, and concurrent timing semantics."
---

# C++ benchmarking

## When to use

Use this skill for C++ benchmark review, planning, implementation, execution, or analysis.

## Scope and boundaries

Apply with the benchmark workflow; do not optimize production code or consume unapproved resources.

## Procedure

### Measure

- Respect standard/compiler/library, optimization, allocator, exception/RTTI policy, and ABI. Reuse installed harnesses such as Google Benchmark.
- Use version-supported `DoNotOptimize`/`ClobberMemory` appropriately; barriers alone do not prove representative work. Validate results and investigate implausible timings.
- Distinguish construction/destruction, allocation, copy/move, and operation costs. Maintain RAII cleanup and explicit lifecycle inclusion.
- Recreate consumed/mutated/moved-from inputs when needed; never assume moved-from emptiness or time a changing workload unintentionally.
- Use representative types/sizes; identify dispatch, locality, small-object optimization, ownership, and allocator effects when relevant.
- Specify total work, contention, worker lifetime, and CPU versus wall-time semantics. Do not accidentally time thread startup for a steady-state question.
- Distinguish allocation/live-byte accounting from RSS/peak memory. Keep exception, sanitizer, and profiling diagnostics separate from ordinary timings.
- Record toolchain/library/configuration differences and limit causal claims accordingly.
