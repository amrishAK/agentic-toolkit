---
name: change-delivery-workflow
description: "Use for selected review fixes such as apply 1, apply 1,2 or apply all through authorized implementers or reviewer-delegated subagents. Separately approved commits, pushes and PR creation are parent-only. Preserves unrelated work and exact-action approvals."
---

# Approved change delivery

## When to use

Use this skill for selected review fixes such as apply 1, apply 1,2 or apply all through authorized implementers or reviewer-delegated subagents.

## Scope and boundaries

Selected-fix coordination is available to reviewers with explicit delegation capability; they never edit directly. Commit/push/PR actions remain separate and parent-only. This workflow grants no tools or implicit authorization; no MCP server is required.

## Procedure

### Fix handoff

- Read the numbered review and its scope/revision. Accept `apply1`, `apply 1`, comma-separated IDs such as `apply 1,2`, or `apply all` as explicit authorization for those recommended corrections only. `all` means all actionable findings in that report, not every issue discoverable in the project.
- Validate every ID before starting. If the report/selection is ambiguous, unavailable or invalid, ask one focused question rather than partially applying a guessed selection. Recheck affected content; refresh materially stale findings and confirm changed remedies before editing.
- Reviewers with delegation capability must launch the fewest appropriate editing subagents for explicit apply selections, not edit directly. Choose `code-engineer`, test specialists, documentation writers, `build-automation-agent`, `benchmark-engineer` or `project-standardizer` according to correction scope. Give each selected IDs, reviewed evidence, bounded file scope, preservation rules and required safe verification; prohibit staging/committing/pushing/publishing and active probing. Parallelize only independent changes with non-overlapping scopes.
- If subagents are unavailable or host rules prohibit delegation/nesting, disclose the limitation. An authorized implementation-capable parent can make in-role fixes directly; a reviewer must return a handoff and wait, never acquire direct edit permission. Do not claim delegation or automatic role switching that did not happen.
- Preserve unrelated work and correct failing expectations. Do not adopt new public behavior or architecture merely because a recommendation leaves a material decision unresolved; ask for the decision.
- Report each selected ID as fixed, unresolved or blocked with changed files, exact checks/results and remaining limitations. Preserve original IDs through the fix cycle; a new review must distinguish retained IDs from newly discovered findings.
- Re-review the affected scope and report remaining blockers. Approval to fix or a ready verdict is not approval to stage, commit, push or create a PR.

### Commit

Reviewer roles stop before this section; these actions require a separate authorized parent/coordinator.

1. Inspect status, staged/unstaged diffs and project commit rules. Propose exact reviewed files/content and the complete message using [commit conventions](../../suites/engineering/skills/project-standards/references/project-conventions-commits.md).
2. Obtain explicit approval. If approved and unrelated changes share a file, resolve the staging scope before acting; do not stage the whole file automatically.
3. Stage only approved content using explicit paths. Inspect the final index; if it contains unrelated work, stop without unstaging it. Reconfirm approval if scope/content changed.
4. Include `Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>` unless the user asks not to. Create only the approved local commit, verify its files/message, and report the hash and remaining worktree state. Do not push automatically.

### Push and create a PR

1. Obtain pre-PR review against the explicitly chosen base. Confirm repository, remote, source/base branches and reviewed head hash. Do not create branches implicitly or include unreviewed commits.
2. If the head needs pushing, show destination and commits and obtain separate push approval. Push only that branch without force; verify the remote head equals the reviewed hash. Warn that a push can trigger CI.
3. Check for an existing open PR for that source/base; if present, report it and stop rather than duplicating it.
4. Follow repository PR templates. Show repository, branches, reviewed hash, title, complete body and draft/ready state for separate approval. Ask if draft state is unspecified. Report actual validation and limitations.
5. Create the approved PR with available authenticated tooling, such as an approved local CLI. Do not alter credentials when blocked. Verify URL, branches, head hash and draft state; report remote checks only if observed.

Never amend, rewrite history, force-push, merge/close PRs, tag, publish, deploy or trigger remote workflows through this workflow. If head, base or content changes, repeat affected review and approval.
