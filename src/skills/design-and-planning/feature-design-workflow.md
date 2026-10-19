---
name: feature-design-workflow
description: "Use to discuss, design, write or maintain feature documents: detailed requirements, public contracts, edge cases, acceptance criteria, implementation plans, dependencies and open decisions. Separates proposed design from implemented behavior."
---

# Feature design and handoff

## When to use

Use this skill to define feature requirements, contracts, acceptance criteria, and implementation handoffs.

## Scope and boundaries

This skill helps define feature intent, contracts, acceptance criteria, and implementation handoffs. It does not authorize implementation.

## Procedure

### Establish the contract

- Read relevant product/release goals, existing feature references, architecture, source and tests. Use the [document-routing map](../documentation/documentation-selection-workflow.md#document-routing-and-maintenance-ownership) and [feature format](../documentation/references/documentation/feature-docs.md); preserve established project conventions.
- Discussion/review is response-only. Write documents only when requested, including explicit combined discussion-and-documentation tasks.
- Distinguish intended behavior, current implementation, accepted decisions and proposals. Report contradictions; do not silently rewrite the intended contract to match a bug.
- Establish users, goals/non-goals, inputs/outputs, errors, edge cases and applicable compatibility, resource and security constraints. Ask one focused question for material unresolved behavior.
- Apply [architecture guidance](architecture-workflow.md) for significant boundaries, cross-component interactions or lifecycle decisions; do not load it mechanically for trivial changes.

### Design and implementation breakdown

- Express acceptance criteria as observable outcomes with meaningful failure cases and appropriate validation tiers. Thresholds must be agreed or evidenced, not guessed.
- Explain the simplest adequate design: responsibilities, interfaces, data flow, ownership/lifetimes and error propagation as relevant. Document alternatives only when actually considered.
- Outline coherent implementation tasks and actual prerequisites. Keep changes task-sized while tracing all affected behavior, callers, persisted data and public contracts.
- Identify rollout, migration, compatibility and rollback needs where applicable. Explicitly identify unknowns, decision owners and when answers are needed; do not invent estimates or commitments.
- Treat implementation detail as design documentation, not authorization to write production code. Hand off to `code-engineer` with acceptance criteria, relevant authorities, dependencies, risks, unresolved decisions and proposed checks.
- Existing agreed feature documents are inputs, not immutable truth: changes to their contract need an explicit decision. Small well-defined fixes do not require a new feature document.

### Maintain and validate

- Use [technical documentation guidance](../documentation/technical-documentation-workflow.md) for writing. Keep current implementation sections evidence-linked and proposed design clearly labeled.
- Maintain feature state and targets in the existing tracker when supported by actual decisions or implementation evidence. Accepted design is not implemented behavior or a passed release gate.
- For authorized release-document consolidation, follow the [release notes rules](../documentation/references/documentation/release-notes.md#consolidate-feature-documents): move completed release-specific feature content into versioned notes, preserve necessary contracts and links, then remove superseded standalone documents. Keep unfinished or future scope active.
- Check affected links, acceptance-criteria consistency, source/test references and release dependencies. Report unresolved decisions and unverified examples.
- Do not edit production code, source comments, dependencies, test/build/CI configuration or run workloads. Do not stage/commit/push, change approved release scope, or publish.
