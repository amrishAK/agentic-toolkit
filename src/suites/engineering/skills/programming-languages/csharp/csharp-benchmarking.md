---
name: csharp-benchmarking
description: "Use for C# benchmark review, planning, implementation, execution, or analysis. Covers .NET JIT and runtime effects, allocation and GC costs, async completion, workload setup, and reproducible reporting."
---

# C# benchmarking

Apply with the benchmark workflow; do not optimize production code or consume unapproved resources.

## Measure

- Respect SDK/runtime, target framework, configuration, architecture, JIT mode, tiered compilation, runtime settings, and installed benchmark harness. Reuse the project's BenchmarkDotNet or other established tooling.
- Measure optimized, representative artifacts. Account for JIT warmup, tiered compilation, dynamic profile-guided optimization, and cold-start versus steady-state behavior according to the question.
- Keep setup, fixture creation, input generation, and cleanup outside the measured operation unless they are part of the intended workload. Reinitialize consumed or mutated inputs between iterations.
- Use representative types, payloads, collection sizes, and call patterns. Check that the benchmark performs the intended work and investigate implausible or zero-cost results.
- Distinguish allocation rate, retained memory, garbage-collection activity, and process peak memory. Use supported diagnostics and state their scope.
- For async work, specify whether task creation, scheduling, runtime setup, and completion are included. Await the intended operation; do not benchmark only construction of an unexecuted task.
- For concurrency, describe worker startup/shutdown, contention, total work, and timing semantics. Complete worker lifetimes and avoid measuring setup unintentionally.
- Keep profilers, tracing, diagnostics, and instrumented builds separate from ordinary timing unless the measurement explicitly concerns their overhead.
- Record runtime/toolchain, configuration, hardware, and workload identity. Limit comparisons and causal claims to equivalent evidence.

## Validate and report

Build the intended optimized benchmark target and verify that the expected nonempty workload completed correctly. Use the shared workflow for repetitions, comparisons, raw metadata, shared entry points, and Python HTML reports.

Report harness and runtime settings, exact commands, results, variation, and limitations. Do not present one run or a profiler capture as verified performance improvement.
