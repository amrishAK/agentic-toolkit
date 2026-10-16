---
name: container-build-workflow
description: "Use for reviewing, creating, fixing, or optimizing Dockerfiles, BuildKit builds, and Docker Compose workflows. Covers shared local/CI entry points, multi-stage builds, runtime compatibility, secrets, caching, readiness, safe resources, and build/run verification."
---

# Docker workflow

Expose documented Docker/Compose actions through the project's [shared entry point](../project-standards/references/project-conventions-entry-points.md) where useful. Keep Docker-specific instructions in Dockerfiles and Compose configuration, not duplicated inline across the entry point and GitHub Actions.

## 1. Define the image and runtime contract

- Inspect application artifacts, native build commands, Docker context, Dockerfiles, Compose services, and consumers.
- Identify target architecture, libc/runtime ABI, dynamic libraries, startup arguments, writable paths, user identity, configuration, and health/readiness requirements.
- Reuse canonical build targets inside builder stages when their dependencies and shell are available. Do not add build tooling such as Make to a minimal runtime image merely to launch the app.
- Preserve project base-image policy. Check supported tags/digests, platform compatibility, and update strategy rather than copying stale OS or package versions.
- Changing to Alpine/distroless is a compatibility decision, not an automatic optimization. Verify libc, libraries, certificates, diagnostics, and required shell utilities.

## 2. Build correctly and efficiently

- Use multi-stage builds when they separate build tools from runtime requirements. Copy the verified artifacts and required libraries, not guessed output paths.
- Install every invoked build tool and supply manifests, lockfiles, profiles, generators, source, test, and packaging inputs required by the actual commands.
- Use `.dockerignore` to exclude unnecessary artifacts and sensitive files while retaining all required inputs.
- Arrange stable dependency-resolution inputs before changing source where correct. Use supported BuildKit cache mounts; cache hits must not change the expected result.
- Do not imply dependency-manifest-first resolution works for every ecosystem without checking source/workspace requirements.
- Use supported build arguments for nonsecret parameters. Pass credentials through BuildKit secret/SSH mounts; do not bake them into arguments, environment, layers, or build logs.
- Scope cache export/import by compatible platform/configuration and avoid exposing private material. Distinguish image tags from immutable identity and reproducibility guarantees.

## 3. Runtime and Compose lifecycle

- Prefer an appropriately permissioned nonroot runtime user where supported. Match file ownership, writable paths, and mounted volume expectations.
- Use suitable exec-form startup and verify signal handling/exit status. Do not invent an application health flag; health checks must use an existing supported interface and available runtime tools.
- Health-check configuration and readiness are not proof a service is ready for every operation. Verify real readiness and apply bounded operation/startup deadlines.
- In Compose, use supported service health/dependency semantics and explicit project-owned names/resources. Keep integration fixtures and production deployment configurations distinct.
- Avoid privileged containers, host mounts/networking, or broad host access unless explicitly justified and authorized.
- Preserve persistent volumes by default. Never run global prune or remove shared volumes as routine cleanup; tear down only known test-owned resources.

## 4. Verify build and runtime

- Use existing Docker/Compose tooling; report unavailable daemon/tool prerequisites instead of claiming validation.
- Run the affected entry-point command or equivalent canonical build and verify the image/artifact identity and selected platform.
- In an isolated authorized environment, launch the image, verify startup/readiness and a meaningful smoke operation, inspect logs, then verify shutdown and cleanup.
- Do not publish images, deploy, or incur external side effects without explicit authorization. Retain local-only validation when permission is absent.
- Distinguish Dockerfile review, build success, runtime smoke success, and full E2E validation. Report untested architectures and runtime configurations.
- Measure claimed size/build-time improvements where practical using comparable configurations; explain caching and base-image effects.
