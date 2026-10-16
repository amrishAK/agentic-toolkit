---
name: c-benchmarking
description: "Use for C benchmark review, planning, implementation, execution, or analysis. Covers C compilation, timer/barrier correctness, allocation and peak-memory accounting, input lifecycle, locality, and instrumentation."
---

# C benchmarking

Apply with the benchmark workflow; do not optimize production code or consume unapproved resources.

## Measure

- Compile production C as C with supported standard, compiler, optimization, and ABI. Established C++ harnesses may call C APIs without converting production code.
- Reuse the harness. For tiny operations, use monotonic timing/batching and supported barriers/output consumption; `volatile` is not a universal optimization barrier.
- Validate results and inspect implausible timings. Prevent constant folding/elimination and unintended state changes across iterations.
- Define inclusion of allocation, initialization, I/O/durability, and cleanup. Keep ownership explicit and do not leak resources to improve timing.
- Distinguish allocation count, requested/live bytes, allocator overhead, RSS, and peak memory. Wrappers may miss alternate allocators or mappings; describe measurement scope.
- Choose meaningful sizes, layouts, locality, and supported concurrency. Use only valid operations and inputs.
- Record architecture/vectorization/allocator/toolchain differences rather than attributing every effect to source changes.
- Run sanitizer/leak/profiling checks separately from normal timing; record instrumentation.

## Validate and report

Build the intended optimized artifact and confirm nonempty workloads completed correctly. Use the shared workflow for repetitions, comparisons, raw metadata, shared entry points, and Python HTML reports.
