---
name: debugging-workflow
description: "Use for diagnosing code, build, or CI failures: minimal reproductions, crashes, hangs, races, resource leaks, logs, stack traces, root causes, and regression verification. Uses the programming language catalogue. Diagnosis does not authorize production fixes."
---

# Evidence-led debugging

Apply with the active role and the [programming language catalogue](../programming-languages/programming-language-catalog.md)'s **Code quality** guidance for the relevant languages. Diagnosis/review reports findings; implement fixes only when requested.

## Reproduce and isolate

- Establish expected versus observed behavior, triggering input, artifact/revision, toolchain/features, environment, and relevant recent changes.
- Reuse the smallest representative failing test or command. Capture exact errors, exit status, logs, and reproduction steps; distinguish deterministic from intermittent failures.
- Preserve unrelated edits. Do not change revisions destructively, access production data, or upload dumps/logs containing private data.
- Separate application, fixture, configuration, dependency, and environment causes. State competing hypotheses and use the smallest discriminating check rather than speculative edits.

## Diagnose

- Reuse supported debuggers, symbolized traces/core dumps, sanitizers, and existing diagnostics. Confirm symbols match the artifact; instrumented behavior may differ.
- For C/C++, inspect ownership, bounds, partial cleanup, and lifetime; for Rust, inspect panic/error chains, unsafe/FFI, poisoning, and async cancellation.
- For C#, inspect exception chains, async task completion/cancellation, disposal, runtime/framework configuration, and allocation/GC behavior when relevant.
- For hangs/races, inspect all relevant workers, lock order, waits, readiness, and shutdown. Use bounded reproduction and supported race/model tools; sleeps or retries are not fixes.
- For leaks/resource growth, distinguish live ownership, allocator retention, caching, and process-wide metrics before assigning blame.
- Trace the failure to the responsible contract/data flow. Correlation, a plausible stack frame, or disappearing under instrumentation is not root-cause proof.

## Resolve and verify

- Report issue, evidence, triggering condition, impact, uncertainty, and suggested correction. Do not turn a plain diagnosis into unrequested changes.
- When fixes are authorized, make a focused correction and preserve a valid regression. Demonstrate pre-fix failure when feasible without destroying work.
- Re-run the reproduction and affected tests/configurations. Confirm the causal explanation, not just a green result after unrelated changes.
- Report exact commands, results, root-cause confidence, remaining hypotheses, and unsupported configurations. Escalate unresolved cases with useful evidence rather than masking failures.
