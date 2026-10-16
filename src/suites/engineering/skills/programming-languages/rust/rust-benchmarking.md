---
name: rust-benchmarking
description: "Use for Rust benchmark review, planning, implementation, execution, or analysis. Covers Cargo profiles/harnesses, black_box, ownership/cloning/drop costs, batched input setup, async completion, and memory metrics."
---

# Rust benchmarking

Apply with the benchmark workflow; do not optimize production code or consume unapproved resources.

## Measure

- Respect MSRV, bench profile, features/targets, allocator, panic strategy, and existing harness. Stable projects need not adopt nightly `#[bench]`.
- Reuse installed Criterion or other tools. Confirm actual target/export/sampling semantics; `cargo bench` does not make harnesses statistically interchangeable.
- Use version-supported `black_box` appropriately, validate results, and inspect implausible timings.
- Distinguish borrowing versus consuming work and input cloning, allocation, and `Drop`. Use supported batched setup only when justified by the measurement question.
- Reset consumed/mutated inputs; avoid accidentally measuring shrinking collections, precomputed work, or unintended warm caches.
- State runtime creation, scheduling, task startup/shutdown, and await-completion inclusion. Do not time only future construction when completion matters.
- Use representative supported types/payloads and explicit concurrent work/contention; join/await workers.
- Allocation counters have scope/allocator limitations and differ from process peak memory. Keep Miri/sanitizer/profiling/instrumented runs separate from ordinary timing.

## Validate and report

Confirm the intended artifact/configuration and nonempty correct workloads. Use supported feature sets, not indiscriminate all-features runs. Follow the shared workflow for repetitions, comparisons, raw metadata, shared entry points, and Python HTML reports.
