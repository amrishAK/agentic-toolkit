---
name: product-planning-workflow
description: "Use to frame product planning, route roadmap and release-plan work, coordinate user decisions and independent review, and maintain clear ownership between product plans and feature contracts."
---

# Product planning workflow

## When to use

Use this skill to coordinate product-planning work across product context, roadmaps, release plans, user decisions, and handoffs to feature design.

## Scope and boundaries

This skill owns the shared planning lifecycle and routing between roadmap and release planning. The [roadmap planning workflow](roadmap-planning-workflow.md) and [release planning workflow](release-planning-workflow.md) own their domain-specific drafting and review methods. Detailed feature contracts belong to [feature design](feature-design-workflow.md); release execution and delivery belong to the [release workflow](../build-and-delivery/release-workflow.md).

This guidance does not grant permission to edit documents, decide priorities, approve plans, implement features, or deliver releases. Follow the active role's permissions. The user retains product priorities, commitments, and release approval.

## Procedure

### Coordinate the planning work

1. Establish whether the request is product discussion, a roadmap, a release plan, or a handoff between them. Discussion is response-only; edit only when requested.
2. Read the project's purpose, audience, scope, current roadmap, decision log, relevant release plans, and applicable project rules. Use the [documentation selection workflow](../documentation/documentation-selection-workflow.md) to identify the canonical document and its rules before writing or reviewing it.
3. Select the [roadmap planning workflow](roadmap-planning-workflow.md) for roadmap creation or review and the [release planning workflow](release-planning-workflow.md) for milestone scope or release-plan review. Load both when the task moves from roadmap direction into a release plan.
4. Follow the roadmap-to-release sequence: a release plan must be based on an approved roadmap milestone. If there is no approved milestone, surface that decision before treating proposed direction as release scope.
5. Keep canonical ownership distinct: roadmaps own high-level direction and relative priority; release plans own milestone scope and readiness evidence; feature contracts own detailed behavior; release notes describe verified shipped changes. Do not duplicate mutable implementation state or candidate evidence in the roadmap.
6. Record material confirmed decisions in the project's decision log when one is maintained. Link to the canonical roadmap, release plan, or contract rather than duplicating its content.
7. Hand detailed behavior and implementation decisions to `feature-designer`. A plan or contract approval does not authorize implementation, independent readiness review, release go/no-go, PR creation, or publication.

### Coordinate review and user decisions

- Use the domain skill's review checklist as well as its drafting guidance. The `product-plan-reviewer` independently reviews roadmap and release-plan drafts; it does not decide priorities, scope, or approval.
- Report reviewer findings and material questions to the user. Resolve product decisions with the user or proceed only within explicitly delegated, bounded authority. Revise from confirmed decisions, record assumptions, and re-review material changes.
- Continue the review-and-decision loop until findings are resolved, or return remaining findings to the user if they are outside delegated authority. Delegated finalization and a clean review are not user approval.
- Present the final candidate, review result, decisions, assumptions, and remaining issues for explicit user approval. If review or delegation is unavailable, report that limitation without substituting self-review.
- Never invent customer demand, dates, estimates, support promises, acceptance thresholds, commitments, or passing evidence. Keep planned validation separate from existing runners and executed candidate evidence.

### Maintain and report

- Use the [technical documentation workflow](../documentation/technical-documentation-workflow.md) for requested writing. Update only agreed product documents and directly affected navigation.
- Verify local links, factual claims, status meaning, and consistency with canonical source documents. Report proposals separately from approved decisions, implementation evidence, and release outcomes.
- Do not modify production code, build/test infrastructure, or dependencies; run workloads; stage or commit changes; or execute release and publication actions as part of planning.
