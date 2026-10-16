---
name: ci-workflow
description: "Use for reviewing, creating, fixing, or optimizing GitHub Actions CI/CD workflows. Covers shared local/CI entry points, matrices, permissions, cache correctness, artifacts, deployment boundaries, and honest local/remote validation."
---

# GitHub Actions workflow

Use GitHub Actions for runner setup, orchestration, permissions, caches, artifacts, and authorized delivery. Keep reusable build/test commands in the project's [shared entry point](../project-standards/references/project-conventions-entry-points.md) rather than separate YAML recipes.

## 1. Establish the workflow

- Inspect existing workflows, entry-point commands, native build configuration, supported platforms/toolchains, triggers, and required checks.
- Define needed jobs and dependencies. Ensure deployment/publication depends on required successful checks; do not put every expensive check only on the main branch by default.
- Follow existing branch/trigger policy. Review path filters, fork pull requests, concurrency cancellation, and reusable workflow inputs for unintended missing checks or cancelled releases.
- Keep requested changes focused. Do not change branch protection, environments, credentials, repository settings, or delivery policy without authorization.

## 2. Preserve local/CI parity

- Have jobs invoke the same entry-point commands and documented variables used locally. CI-specific commands should compose shared ones, not maintain a second implementation.
- Install or select the tools and shell the entry point requires, such as the supported Make implementation and recipe shell. Set GitHub Actions shell explicitly when required; Windows PowerShell is not a Unix Make recipe shell.
- Select matrix compilers, versions, targets, and configurations explicitly and confirm them in build configuration. Avoid incompatible combinations instead of treating missing tools as evidence the platform cannot support them.
- Honor runner and action runtime requirements. Check current official action metadata and supported versions when changing actions; do not copy stale version numbers.
- Keep tool versions reproducible within project policy and update deliberately. Do not upgrade supported language standards or runtimes merely to match hosted runner defaults.

## 3. Permissions and trust boundaries

- Use explicit least-privilege token permissions at workflow/job scope. Grant publishing or OIDC permissions only where needed; use protected environments/approval controls where appropriate.
- Treat pull-request code and event text as untrusted. Avoid executing fork code with privileged credentials, including unsafe `pull_request_target` checkout patterns.
- Pass untrusted values through safely quoted inputs/environment variables rather than interpolating them into shell scripts.
- Use credential stores or supported OIDC flows; never print secrets or store them in caches/artifacts. Review third-party action trust and pin immutable revisions when project policy requires it.

## 4. Cache and artifact correctness

- Caches are disposable performance aids, not authoritative build inputs or a delivery mechanism. A cache miss must still permit a correct build.
- Key caches by relevant lockfiles/manifests, OS/architecture, toolchain, target/triplet/profile, and configuration. Restore only compatible state and consider trust boundaries between contributors.
- Prefer dependency/compiler caches over whole configured build trees unless path, toolchain, generator, and invalidation compatibility are demonstrated.
- Use supported cache inputs. For save timing requirements, check current restore/save action behavior instead of relying on deprecated `save-always`.
- Give artifacts unique matrix-aware names. Ensure paths contain the intended outputs and reports and fail or report clearly when required artifacts are missing.
- Keep evidence upload available after failures where appropriate, without masking the failed job. Distinguish missing test execution from successful tests.

## 5. Validate and report

- Validate workflow syntax/expressions with existing supported tooling and verify referenced entry-point commands, paths, secrets names, and preset configurations.
- Run canonical commands locally where feasible. Local emulation cannot establish complete hosted-runner, permissions, secrets, or deployment behavior.
- Inspect remote logs read-only when relevant. Trigger runs, push, publish, or deploy only with explicit authorization.
- Do not treat a locally validated YAML file as a successful CI run. Report exact local checks and, when observed, remote run/job identity and results.
- Document configuration and required prerequisites without embedding credentials. Record untested matrix entries and remote-only blockers.
