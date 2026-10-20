# Engineering language matrix

Use this matrix alongside the Engineering [task matrix](../../agent-workflows/references/skill-selection-workflow-matrix.md). It routes supported languages to language-specific code quality, testing, benchmarking, and source-documentation skills.

Each linked label is the skill's invocation name and its target is the maintained source.

| Language | Code quality | Unit testing | Integration testing | Benchmarking | Source documentation |
|---|---|---|---|---|---|
| C | [c-code-quality](../c/c-code-quality.md) | [c-unit-testing](../c/c-unit-testing.md) | [c-integration-testing](../c/c-integration-testing.md) | [c-benchmarking](../c/c-benchmarking.md) | [c-source-documentation](../c/c-source-documentation.md) |
| C++ | [cpp-code-quality](../cpp/cpp-code-quality.md) | [cpp-unit-testing](../cpp/cpp-unit-testing.md) | [cpp-integration-testing](../cpp/cpp-integration-testing.md) | [cpp-benchmarking](../cpp/cpp-benchmarking.md) | [cpp-source-documentation](../cpp/cpp-source-documentation.md) |
| C# | [csharp-code-quality](../csharp/csharp-code-quality.md) | [csharp-unit-testing](../csharp/csharp-unit-testing.md) | [csharp-integration-testing](../csharp/csharp-integration-testing.md) | [csharp-benchmarking](../csharp/csharp-benchmarking.md) | [csharp-source-documentation](../csharp/csharp-source-documentation.md) |
| Rust | [rust-code-quality](../rust/rust-code-quality.md) | [rust-unit-testing](../rust/rust-unit-testing.md) | [rust-integration-testing](../rust/rust-integration-testing.md) | [rust-benchmarking](../rust/rust-benchmarking.md) | [rust-source-documentation](../rust/rust-source-documentation.md) |

Update the relevant row when adding or changing a language skill. Matrix entries describe maintained guidance, not runtime, framework, or client support.

For a language without a dedicated row, use [general-code-quality](../general/general-code-quality.md) for code-quality tasks. For other task types, select an applicable shared workflow from the [Software Product Development task matrix](../../agent-workflows/references/skill-selection-workflow-matrix.md) where one exists. This does not imply language-specific coverage.
