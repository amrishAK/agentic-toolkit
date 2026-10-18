---
name: profiling-workflow
description: "Use for evidence-led performance diagnosis: CPU hotspots, allocations, retained memory, contention, I/O, and async work. Covers representative workloads, matching symbols, bounded capture, overhead, and benchmark confirmation. Uses the language-specific skill matrix."
---

# Profiling workflow

## When to use

Use this skill for evidence-led performance diagnosis: CPU hotspots, allocations, retained memory, contention, I/O, and async work.

## Scope and boundaries

Apply with code or benchmark engineering and the [language-specific skill matrix](../../../../shared/skills/references/programming-language-matrix.md)'s **Code quality** guidance for the relevant languages. Use its **Benchmarking** guidance when confirming measurements. Diagnosis does not authorize production optimization or host tuning.

## Procedure

### Capture

- Define the question and representative workload: CPU, wall latency, allocation churn/live memory, contention, I/O, or async scheduling. Do not assume CPU sampling explains waiting.
- Establish artifact/revision, optimized build intent, matching symbols, platform/tool support, warm/cold state, and a bounded capture budget.
- Reuse existing tools appropriate to the platform, such as supported sampling profilers, allocation tools, tracing, or lock diagnostics. Do not assume Linux perf or Valgrind works on Windows.
- Scope capture to test-owned authorized processes; attaching to shared services, privileged profiling, or host changes requires authorization. Traces/dumps may contain secrets.
- Validate workload correctness and completion. Record capture command, events, units, sample counts/loss, duration, instrumentation, and tool/configuration versions.

### Interpret and confirm

- Distinguish inclusive/self costs, on/off-CPU time, allocation totals versus retained memory, and process versus operation scope. Do not add overlapping inclusive costs.
- Inspect plausible call paths and workload distribution; account for inlining, optimization, incomplete stacks, sampling bias, and instrumentation overhead.
- For C/C++, consider copying, RAII/lifetime, allocators, and contention; for Rust, also distinguish cloning/drop, task scheduling, and awaiting actual work.
- For C#, consider JIT/runtime configuration, allocation and garbage-collection costs, async scheduling, and whether startup or steady-state behavior is being measured.
- Treat hotspots as evidence for hypotheses, not proof of causation. Use a focused check to distinguish competing explanations.
- Report costly paths, supporting evidence, impact, uncertainty, and suggested changes. Preserve raw bounded captures locally; do not upload private artifacts.
- After authorized optimization, validate behavior and use comparable uninstrumented benchmarks for speedup claims. Re-profile when useful; a smaller flamegraph alone is not verified improvement.
