---
name: csharp-code-quality
description: "Use for reviewing, writing, fixing, or refactoring C# code. Covers .NET targets, type and resource lifetimes, async cancellation, exceptions, concurrency, API compatibility, and validation."
---

# C# code quality

Apply with the code-quality workflow and authorized task scope; this skill does not authorize edits.

## Review and implement

- Respect the supported .NET SDK/runtime, target framework(s), C# language version, nullable context, package versions, analyzers, platform, and deployment mode. Derive these from project configuration rather than assuming the newest defaults.
- Prefer clear types, straightforward control flow, and existing project conventions. Use records, pattern matching, LINQ, generics, and newer language features when they improve the contract and are supported by every target.
- Treat nullable reference annotations as compile-time analysis, not runtime validation. Validate untrusted inputs and keep annotations consistent across public APIs and implementations.
- Review value/reference semantics, copying, boxing, mutability, equality, and collection behavior. Consider allocation and lifetime costs when relevant without prematurely replacing clear code with low-level constructs.
- Dispose owned `IDisposable` and `IAsyncDisposable` resources on success, failure, and cancellation paths. Do not rely on garbage collection or finalizers for timely release of files, handles, transactions, or other external resources.
- Propagate meaningful exceptions or translate them at deliberate boundaries while preserving useful causes. Catch only when handling, adding context, or restoring a valid state; avoid broad catches and success-shaped fallbacks.
- For asynchronous work, return and await `Task`/`ValueTask` as appropriate, propagate `CancellationToken` through cancellable operations, and consider cancellation, exceptions, and disposal during shutdown. Avoid `async void` except event-handler contracts.
- Check thread safety, shared mutable state, lock scope/order, concurrent collection semantics, and object publication. `async` does not itself make state thread-safe.
- Treat `Span<T>`, `ReadOnlySpan<T>`, ref structs, pinning, unsafe code, and native interop as lifetime and boundary contracts. Verify ownership, encoding, layout, calling convention, error propagation, and supported runtime/platform assumptions.
- Preserve public API and behavioral compatibility across target frameworks. Review serialization, reflection, trimming, and ahead-of-time constraints when the project uses them.
- Document caller-visible nullability, ownership/disposal, exceptions, cancellation, side effects, and thread-safety guarantees where they are not clear from the API.

## Validate

Use the project's configured SDK, target frameworks, analyzers, formatting, builds, and focused tests. Confirm the intended targets ran; do not infer support for untested frameworks or runtime modes.

Use nullable analysis and static analysis as evidence, not proof. Run trimming, AOT, platform, or interop checks only when supported and relevant. Consult version-matched Microsoft .NET and C# documentation when language or runtime behavior is uncertain.
