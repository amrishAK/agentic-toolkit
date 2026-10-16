---
name: build-system-workflow
description: "Use for reviewing, creating, fixing, or migrating Make/CMake, .NET, and native build workflows. Covers shared local/CI entry points (Make by default), incremental and parallel correctness, presets, toolchain compatibility, dependencies, artifacts, tests, and safe cleanup."
---

# Build system workflow

Expose consistent local and CI commands through the project's [shared entry point](../project-standards/references/project-conventions-entry-points.md), delegating compilation and dependency resolution to native tools. When that entry point is Make, apply section 2. Preserve project constraints; load CI or Docker skills only when those surfaces are affected.

## 1. Establish contracts and prerequisites

- Read project guidance, existing Makefiles, presets, native manifests, .NET solution/project files, tests, and affected consumers. Identify working directory, tool versions, compiler/standard, C# language version/target framework, Rust MSRV, generator, configurations, and expected artifacts.
- Define only needed commands, using the convention's names where the project has none. Reuse existing names. Avoid adding CI, Docker, installation, or deployment merely because build work was requested.
- Prefer CI aliases that depend on canonical targets rather than duplicate recipes. Ensure target prerequisites encode required ordering.
- Specify the Make implementation and recipe shell, especially on Windows. Distinguish host shell, Make recipe shell, and container shell; quote paths correctly and do not embed OS-specific commands in purportedly portable recipes.
- Keep MSVC environment setup and dependent commands in the same process where needed. Never mix incompatible compiler/runtime ABIs without a supported bridge.

## 2. Maintain Make correctness

- Mark command targets `.PHONY`, set an intentional default goal, and document useful targets with the project's help convention.
- Use overridable variables for intended configuration, with safe defaults and consistent names. Account for GNU Make built-in compiler variables: `CC ?= gcc` does not override a pre-existing built-in `CC`.
- Use `$(MAKE)` for recursive Make and respect the jobserver. Avoid hard-coded `nproc` or independently unbounded parallel builds inside `make -j`.
- Dependencies, not textual order, establish sequencing under parallel execution. Do not share mutable build directories across incompatible configurations or race cleanup against build/test.
- Each recipe line normally runs in a separate shell. Keep dependent shell state together or use a deliberately supported single-shell approach with explicit failure propagation.
- Do not swallow failures with ignored errors or `|| true` for required actions. Preserve useful diagnostics and final exit status.
- If Make directly compiles sources, track header/generated-input dependencies with compiler-supported mechanisms, create nested output directories, and keep configurations separate.
- Preserve link ordering and separate library inputs from linker options. Do not assume wildcard discovery or missing dependency rules provide reliable incremental builds.

## 3. Delegate to CMake or native tools

- In CMake projects, let Make invoke supported configure/build/test/install/package presets or documented commands. Avoid duplicating source and header graphs in Make.
- Match preset schema to the supported CMake minimum; validate preset names and required configure/build/test counterparts. Use distinct binary directories where configurations require isolation.
- Select compilers/toolchains at configuration time; a compiler matrix label alone does not select a compiler. Do not switch compilers in a reused incompatible cache.
- Distinguish single-config build types from multi-config build/test configuration selection. Respect platform-specific generators and runtime libraries.
- Prefer target-scoped sources, include paths, compile features/options, and dependencies. Use explicit source lists unless justified by project conventions; avoid indiscriminate global flags.
- Register tests and verify that selected tests execute. Integrate supported instrumentation with required compile/link settings and separate incompatible sanitizer configurations.
- Use supported dependency generators/toolchain integration. Pin external source revisions or verify archive hashes where appropriate; respect existing offline/vendor policies.
- For Cargo, .NET SDK/MSBuild, and other native tools, use their manifests, lockfile policy, target selection, and artifact discovery. Do not invent generic lockfiles: vcpkg uses manifests, baselines, registry configuration, and overrides; Conan has its own profiles/generators/lockfiles.

## 4. Validate incremental behavior and cleanup

- Use existing tools. Install/restore dependencies only for an intentional manifest change or demonstrated missing prerequisite, with authorization where required.
- Run the affected configure/build/test targets and inspect expected artifacts. A dry run is supplementary and may still evaluate shell expressions or recursive Make; do not execute untrusted Makefiles assuming `-n` is harmless.
- For dependency-graph changes, verify relevant header/generated-input changes cause rebuilds and unchanged inputs avoid unnecessary work. Test parallel behavior when touched.
- Verify migration outputs against the actual contract; byte-for-byte equivalence is required only when promised and reproducibility controls support it.
- Distinguish hermeticity, version pinning, offline capability, and reproducibility. Pinning alone does not eliminate timestamps, paths, undeclared environment inputs, or nondeterministic outputs.
- Restrict cleanup to validated project-owned artifact paths. Guard empty/root/out-of-scope overrides; never uninstall developer packages or delete broad directories as `clean`.
- Update target help and related setup documentation. Report exact commands, output/test results, configurations exercised, and unverified platforms.
