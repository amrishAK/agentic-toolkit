---
name: review-workflow
description: "Use when reviewing changes in per-commit, pre-PR, pull request or per-release mode: selecting exact ranges, checking contracts and evidence, routing relevant skills, classifying findings and reporting readiness. Does not authorize edits or delivery actions."
---

# Review workflow

## When to use

Use this skill to review commits, proposed or existing pull requests, and releases against the relevant gate.

## Scope and boundaries

One procedure for every review; the mode decides the range, depth and what blocks. The review phase is findings-only: no edits, persisted reports, editing subagents or delivery actions. For selected fixes, follow the shared [change-delivery workflow](../agent-workflows/change-delivery-workflow.md#fix-handoff). Respect host permissions and active-agent execution limits.

## Procedure

### Review modes

| Mode | Use when | Reference |
|---|---|---|
| Commit | Staged changes or a single commit, before or just after committing | [commit-review.md](references/review-workflow-commit-review.md) |
| Pre-PR | A local branch compared with the explicitly selected base, before opening a PR | [pr-review.md](references/review-workflow-pr-review.md) |
| PR | An existing PR before merging, only if the active agent supports that scope | [pr-review.md](references/review-workflow-pr-review.md) |
| Release | Everything since the last tag, or the whole project before the first release | [release-review.md](references/review-workflow-release-review.md) |

Each mode includes the checks of the one above it: release includes PR, and PR includes commit.

### 1. Select mode and range

- Use the mode the user names. Otherwise infer it: staged changes or one commit means commit mode, a local branch before submission means pre-PR mode, an existing PR means PR mode, a version or "release" means release mode. Ask when unclear; do not expand an agent's supported modes.
- For branch comparison, establish the user-selected base and resolve source/base hashes. Do not assume upstream/default branches. For release, establish candidate identity and approved acceptance requirements.
- Resolve the range with read-only git commands, for example `git diff --staged`, `git show <sha>`, `git diff <base>...HEAD`, or `git log <last-tag>..HEAD`. Report the exact range reviewed.
- For execution-capable read-only reviewers, use `git --no-optional-locks --no-pager` to avoid optional index writes and interactive pagers. Disable external diff/text conversion with `--no-ext-diff --no-textconv` for diff/show inspection; do not execute repository scripts as an inspection shortcut.
- Note uncommitted changes outside the range; do not review or touch them unless asked.

### 2. Load guidance

- Always load [project conventions](../project-standards/project-conventions.md) and the project's own rules (`AGENTS.md`, `.github/instructions/`). Project rules override conventions.
- Use the shared [skill selection workflow](../agent-workflows/skill-selection-workflow.md) and applicable suite matrix to select only skills matching surfaces the change touches. Use the language-specific skill matrix for language guidance.
- Use [document ownership](../documentation/documentation-selection-workflow.md#document-routing-and-maintenance-ownership) to distinguish product intent, feature contracts, implementation state and candidate evidence.
- Report any skill that could not be loaded; never claim it was applied.

### 3. Review

- Read the full changed files and their direct callers or consumers, not only the diff lines.
- Check the mode's list, then apply each loaded skill's review guidance to the surfaces it covers.
- Use read-only inspection and supplied check results within the active agent's tools. A strictly read-only reviewer must not execute builds/tests, formatting, active scans or other workloads; request missing evidence from a separately authorized executor.
- Never run commands that publish, push, deploy, modify shared state or alter maintained files/index. A shell tool is not an enforced read-only sandbox; report execution limitations.
- Leave deterministic checks (format, lint, commit-message format) to hooks and CI where they exist. Report their results; do not re-derive them by hand.

### 4. Classify findings

| Severity | Meaning |
|---|---|
| **Blocker** | Must be fixed before this mode's gate: commit, opening a PR, merge or release |
| **Major** | Should be fixed in this change; can be deferred only with a tracked reason |
| **Minor** | Worth fixing; does not block |
| **Nit** | Optional preference, clearly labelled |

- Each mode's reference lists what counts as a blocker in that mode.
- Separate defects from preferences. Label uncertainty and state what evidence would resolve it.
- Report drift from conventions as drift, not as defects, unless the project's own rules require the convention.

### 5. Report

1. **Verdict:** ready, ready with fixes, or not ready, for this mode's gate.
2. **Range and guidance:** the exact range reviewed, skills loaded, and checks run with their results.
3. **Findings:** numbered with stable sequential IDs, ordered by severity. Each has issue type, level, location, explanation/evidence, impact, recommended solution and proposed verification, following [output guidance](../agent-workflows/agent-output-standardization.md).
4. **Not checked:** platforms, configurations or surfaces not covered, and checks not run.
5. **Selected fixes:** after explicit selection, follow the shared [selected-fix handling](../agent-workflows/change-delivery-workflow.md#fix-handoff). Reviewers do not edit directly.
