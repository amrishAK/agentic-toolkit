# Programming language catalogue

This catalogue owns the engineering suite's language inventory and task-to-skill routing. Agents own roles and authorization boundaries; task workflows own methods; language skills own language-specific guidance. This is a maintained reference, not an executable registry or a client-discoverable skill.

Use the [engineering skill catalogue](../skill-catalog.md) for category-level workflows and shared guidance. Language-specific inventory remains here rather than being duplicated in that catalogue.

## Select guidance

1. Detect relevant languages and compilation modes from source, build configuration, target frameworks, harnesses, and interface consumers, not extensions alone.
2. Select the task column in the skill matrix below. Load each matching skill by its linked name, or read the linked file when invocation is unavailable.
3. Load only the language skills needed for the task. At mixed-language boundaries, apply both sides; for comparisons, identify differing toolchain and harness semantics.
4. Pair language guidance with the active role's task workflow. Debugging, profiling, security, and release work use code-quality guidance where relevant; testing, benchmarks, and source documentation use their corresponding columns.
5. If a language or task has no entry, report the missing guidance. Do not substitute another language's skill, invent a skill name, or claim catalogue coverage. Use project-owned guidance where sufficient; ask or stop affected work when correctness depends on unavailable guidance.
6. If a listed skill cannot be loaded or read, report the limitation rather than claiming it was applied. Selection never grants editing, execution, delegation, or delivery permission.

## Skill matrix

Each linked label is the skill's invocation name and each target is its direct-read fallback.

| Language | Code quality | Unit testing | Integration testing | Benchmarking | Source documentation |
|---|---|---|---|---|---|
| C | [c-code-quality](c/c-code-quality.md) | [c-unit-testing](c/c-unit-testing.md) | [c-integration-testing](c/c-integration-testing.md) | [c-benchmarking](c/c-benchmarking.md) | [c-source-documentation](c/c-source-documentation.md) |
| C++ | [cpp-code-quality](cpp/cpp-code-quality.md) | [cpp-unit-testing](cpp/cpp-unit-testing.md) | [cpp-integration-testing](cpp/cpp-integration-testing.md) | [cpp-benchmarking](cpp/cpp-benchmarking.md) | [cpp-source-documentation](cpp/cpp-source-documentation.md) |
| C# | [csharp-code-quality](csharp/csharp-code-quality.md) | [csharp-unit-testing](csharp/csharp-unit-testing.md) | [csharp-integration-testing](csharp/csharp-integration-testing.md) | [csharp-benchmarking](csharp/csharp-benchmarking.md) | [csharp-source-documentation](csharp/csharp-source-documentation.md) |
| Rust | [rust-code-quality](rust/rust-code-quality.md) | [rust-unit-testing](rust/rust-unit-testing.md) | [rust-integration-testing](rust/rust-integration-testing.md) | [rust-benchmarking](rust/rust-benchmarking.md) | [rust-source-documentation](rust/rust-source-documentation.md) |

## Maintain the catalogue

- Add or change language skills in their language directory and update the corresponding matrix entries in the same change. Mark unavailable task guidance explicitly rather than linking to nonexistent files.
- Keep language inventories and per-language routing out of agent definitions and general workflow descriptions. Adding a language should not require changing those consumers.
- Update an agent or task workflow only when its responsibilities, methods, or permissions actually change, not merely because the language inventory grows.
- Verify skill metadata, unique names, relative links, and complete inclusion of referenced resources. The matrix records source guidance, not tested runtime, platform, framework, or client support.
