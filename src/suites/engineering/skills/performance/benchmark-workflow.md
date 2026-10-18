---
name: benchmark-workflow
description: "Use when reviewing, planning, implementing, running, comparing, or reporting benchmarks. Covers user focus, readable workloads, resource budgets, reproducible sampling, memory metrics, shared entry points, and Python-generated HTML reports. Uses the language-specific skill matrix."
---

# Benchmark workflow

## When to use

Use this skill to plan, implement, run, compare, or report benchmarks.

## Scope and boundaries

Apply this methodology with the [language-specific skill matrix](../../../../shared/skills/references/programming-language-matrix.md)'s **Benchmarking** guidance for the relevant languages. Benchmarking measures performance; tests establish correctness and profiling helps explain costs. Do not substitute one for another.

## Procedure

### 1. Clarify the measurement question

- Honor review-only or plan-only requests without edits or workload execution. Explicit implementation/run/report requests may proceed within their scope.
- Inspect existing benchmarks, contracts, relevant implementation, native tools, and entry-point commands before selecting tooling.
- Ask the user one focused question at a time for material missing decisions: operation/journey, latency/throughput/memory/startup/scaling focus, workload, baseline/candidate, practically meaningful difference, and run budget.
- Offer concrete metric choices for vague requests. Do not interrogate users about details already supplied or inconsequential harness settings; state reasonable minor assumptions.
- Record an agreed plan: scenarios, input distribution/sizes, concurrency, measured region, units, correctness oracle, warm/cold state, configuration, repetitions, run bounds, and comparison criteria.
- Separate microbenchmarks, real component benchmarks, and whole-application/load measurements. Public interfaces are preferred when relevant, but a microbenchmark can legitimately isolate an internal algorithm; label that scope.

### 2. Implement understandable workloads

- Reuse project harnesses and supported versions. Keep workload construction, measurement, and validation clearly separated with descriptive scenario names.
- Use small explicit fixtures and helpers only when they reduce confusion. Parameterize genuinely comparable inputs; avoid giant benchmark functions, speculative frameworks, and arbitrary benchmark counts.
- Derive expected results independently and check correctness. Invalid results, failed operations, and incomplete work cannot be counted as successful throughput.
- Define whether setup, allocation, teardown, I/O, retries, and durable writes are included. Do not exclude real costs merely to improve results.
- Prevent unintended optimization with harness-supported mechanisms and input/output handling; investigate implausible results rather than trusting a barrier alone.
- Use representative data and documented seeds. Reset mutable/consumed state correctly; distinguish intentional cache warming from accidental reuse.
- Keep production optimization outside scope unless explicitly requested. Preserve unrelated work and update only necessary benchmark registration, fixtures, report tooling, and usage documentation.

### 3. Make measurements safe and reproducible

- Specify duration, memory/storage, concurrency, and external-operation limits before heavy runs. Do not exhaust shared resources or alter affinity, power settings, services, or host configuration without authorization.
- Use test-owned files/data/services and clean up on failures. Real component benchmarks need explicit dependency arrangements and readiness; never silently switch a failed real dependency to a fake.
- Build appropriate optimized artifacts; record source revision and dirty-state identity, compiler/runtime, flags/profile, features, architecture, allocator, and dependency versions.
- Record OS/hardware, timer semantics, tool versions, commands, inputs, and known competing load. Do not expose secrets or private payloads in artifacts.
- Keep sanitizer, allocation-instrumented, and profiling runs separate when their overhead changes the measurement. Record instrumentation for every result.
- Prefer serial comparison runs over competing baseline/candidate workloads. Avoid running benchmarks under unbounded parallel Make or sharing mutable output paths.
- Use warm-up when appropriate and distinguish cold-start/cold-cache objectives. Never clear shared OS caches or claim a cold-cache experiment without a supported safe method.
- Use repeated samples and independent runs according to the runner's methodology. Alternate or randomize comparable run order where useful to reduce drift; record the order.

### 4. Compare honestly

- Compare equivalent scenario definitions, units, build intent, hardware/environment, and instrumentation. If a variable is intentionally changed, identify it and limit attribution accordingly.
- Separate within-process iterations from independent trials; do not inflate evidence by treating correlated iterations as independent samples.
- Report relevant central tendency, variation, sample counts, and supported uncertainty estimates. Preserve framework statistical semantics rather than inventing confidence intervals.
- Do not manufacture latency percentiles from aggregate timing or throughput. Tail-latency claims require appropriate per-operation observations/sampling; account for load-generation model and coordinated omission when relevant.
- State metric direction and percentage formula, especially for throughput versus latency. Handle zero baselines and unavailable values explicitly.
- Preserve raw results and all relevant runs; do not choose only fastest samples or discard outliers without a declared justified policy.
- Use improved/regressed/inconclusive conclusions against the agreed practical threshold and measurement uncertainty. Statistical significance alone does not establish practical value.
- Hosted CI runners are suitable for smoke checks but not automatically stable performance gates. Establish noise/baselines and controlled runner conditions before adding tight thresholds.

### 5. Standardize execution and reporting

- Expose needed commands through the project's [shared entry point](../project-standards/references/project-conventions-entry-points.md), for example `bench-build`, `bench`, `bench-report`, and `bench-compare`. Add only commands required by the request.
- Delegate measurement to native harnesses and analysis/reporting to Python. Keep identical target semantics locally and in GitHub Actions; document workload/configuration/result-path variables.
- Load `build-system-workflow` or `ci-workflow` only when changing those surfaces. Avoid build/CI migrations merely to add a benchmark.
- Keep machine-readable raw results and environment metadata independent of HTML. Prefer existing runner exports and explicit adapters over lossy ad hoc parsing.
- For Python HTML work, read [report generation guidance](./references/benchmark-workflow-python-html-reporting.md). Do not add a project report script unless implementation of reporting is requested or part of the agreed deliverable.
- Register and smoke-run intended workloads; confirm nonempty measurements and correct outputs. Full runs require the agreed budget and environment.
- Report scenarios/files changed, exact commands, environment/artifact identity, raw artifact locations, comparisons with units and uncertainty, failures, and limitations. State when no measurements were run.
- Never invent timings, claim untested configurations, or call noisy/incomparable evidence a verified speedup.
