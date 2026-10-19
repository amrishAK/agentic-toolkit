# Shared entry points

**Goal:** the same commands run locally and in CI, so the pipeline can be tested on a developer machine before pushing.

## Rules

- Each project has one shared entry point for its repeated tasks: build, format/lint checks, each test tier, benchmarks, and packaging where they exist.
- CI jobs call the shared entry point. They do not duplicate its steps in workflow YAML. CI-only work (runner setup, caches, artifact upload, publishing) stays in the workflow.
- The entry point delegates to native tools: Cargo for Rust, CMake presets for C/C++, and the configured .NET SDK/MSBuild for C#. It standardizes commands, not compilation; never build a second, competing build graph.
- Document every entry-point command in the project's build/test guide, including prerequisites and the working directory.

## Choosing the mechanism

- **New projects:** use Make as the default entry point.
- **Existing projects:** keep the established mechanism if CI already calls it, for example Cargo aliases or local validation scripts that mirror CI jobs. Do not add a Makefile unless asked.
- Make is chosen for a single, uniform interface, not because it builds faster.

## Command names

Use these names where they apply and the project has no established names:

| Command | Purpose |
|---|---|
| `build` | Build the default artifacts |
| `check` | All CI gates that need no external infrastructure |
| `test-unit` | Unit tests |
| `test-integration` | Integration tests; separate commands for tiers that need infrastructure |
| `bench`, `bench-report`, `bench-compare` | Benchmarks and reports |
| `package` | Release artifacts |

## Platforms

- The entry point must work on every platform the project supports. Document the required tools and shell, for example the Make implementation and recipe shell on Windows.
- When one mechanism cannot serve all platforms, provide equivalent per-platform scripts (for example PowerShell and Bash) that run the same checks, and say which CI job each one mirrors.
- Document known platform limits next to the command, for example sanitizers that cannot run under WSL2.
