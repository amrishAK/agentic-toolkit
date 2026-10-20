---
name: feature-design-workflow
description: "Use to discuss, design, write or maintain feature documents: detailed requirements, public contracts, edge cases, acceptance criteria, implementation plans, dependencies and open decisions. Separates proposed design from implemented behavior."
---

# Feature design and handoff

## When to use

Use this skill to draft, update, discuss, or independently review detailed feature contracts, including requirements, public behavior, acceptance criteria, and implementation handoffs. Writers and read-only reviewers use the applicable procedure below.

## Scope and boundaries

This skill helps define feature intent, contracts, acceptance criteria, and implementation handoffs. It does not authorize implementation.

## Procedure

### Establish the contract

- Read relevant product/release goals, existing feature references, architecture, source and tests. Use the [document-routing map](../documentation/documentation-selection-workflow.md#document-routing-and-maintenance-ownership) and [feature format](../documentation/references/documentation/feature-docs.md); preserve established project conventions.
- Discussion/review is response-only. Write documents only when requested, including explicit combined discussion-and-documentation tasks.
- Distinguish intended behavior, current implementation, accepted decisions and proposals. Report contradictions; do not silently rewrite the intended contract to match a bug.
- Establish users, goals/non-goals, inputs/outputs, errors, edge cases and applicable compatibility, resource and security constraints. Ask one focused question for material unresolved behavior.
- Apply [architecture guidance](architecture-workflow.md) for significant boundaries, cross-component interactions or lifecycle decisions; do not load it mechanically for trivial changes.

### Walk through the proposed contract

- Draft and present applicable segments in a decision-friendly order: user outcome and scope; current behavior and gaps; proposed behavior and public/API contracts; architecture and durable decisions; data, compatibility, migration, security, operations and rollout; acceptance criteria, scenarios and verification; implementation tasks, dependencies and risks. Omit segments that do not apply and explain material omissions.
- Take the user through each segment before moving on. Summarize the proposal and its consequences, invite corrections, and obtain explicit confirmation for that segment. Confirmation of a segment records the user's decision; it does not authorize implementation or delivery.
- Record material confirmed product or technical decisions in the project's decision log when one is maintained. Keep detailed context in the feature contract or architecture decision record and link to it rather than duplicating it in the log.
- Categorize open questions by the affected area, such as product/scope, behavior/API, architecture, data/migration, compatibility, security/operations, or verification. Record the decision owner and needed-by point. Ask one focused question at a time for decisions that block the contract; keep non-blocking questions visible without inventing answers.
- Do not mark the full contract accepted while material decisions remain unresolved or any applicable segment is awaiting user confirmation.

### Design and implementation breakdown

- Express acceptance criteria as observable outcomes with meaningful failure cases. For each criterion, define one or more acceptance scenarios that make the expected behavior concrete and map them to the applicable verification method and test tier. Given/When/Then is an optional way to write a scenario, not a required format or a claim that a BDD framework is available. Select only relevant tiers; do not require unit, integration, and E2E coverage for every feature. Coverage thresholds must be agreed or defined by project gates, not guessed.
- Explain the simplest adequate design: responsibilities, interfaces, data flow, ownership/lifetimes and error propagation as relevant. Document alternatives only when actually considered.
- Outline coherent implementation tasks and actual prerequisites. Keep changes task-sized while tracing all affected behavior, callers, persisted data and public contracts.
- Identify rollout, migration, compatibility and rollback needs where applicable. Explicitly identify unknowns, decision owners and when answers are needed; do not invent estimates or commitments.
- Treat implementation detail as design documentation, not authorization to write production code. Hand off to `code-engineer` with goals/non-goals, acceptance criteria mapped to scenarios and applicable verification tiers, relevant authorities and contracts, sequenced implementation tasks and actual dependencies, risks, unresolved decisions and proposed checks. Identify the relevant test-specialist handoffs when useful; the selected tier does not imply that every test role or test layer is required.
- Existing agreed feature documents are inputs, not immutable truth: changes to their contract need an explicit decision. Small well-defined fixes do not require a new feature document.

### Review an engineering feature contract

For read-only review, establish the contract's audience, intended outcome, scope, and whether it describes current or proposed behavior. Apply the [feature-document guidance](../documentation/references/documentation/feature-docs.md) and check only relevant concerns:

- scope, non-goals, affected users, and dependencies are explicit;
- current implementation and intended behavior are distinguished, and implementation claims link to source and test evidence;
- applicable interfaces, errors, edge cases, compatibility, data/migration, operations, rollout, recovery, and security constraints are addressed without requiring irrelevant sections;
- acceptance criteria are observable, include meaningful failure cases, and map to concrete scenarios and appropriate verification methods;
- open decisions identify their category, owner, and needed-by point, and are not treated as accepted behavior;
- implementation tasks follow the confirmed scope, identify actual prerequisites and risks, and distinguish proposed checks from executed evidence; and
- relevant local links and evidence references resolve or are explicitly reported as unverified.

Report factual gaps, unresolved user decisions, inaccessible evidence, and optional recommendations separately. Do not invent requirements, decide product or architecture questions, modify the contract, or equate contract review with implementation, security, or release readiness.

### Maintain and validate

- Use [technical documentation guidance](../documentation/technical-documentation-workflow.md) for writing. Keep current implementation sections evidence-linked and proposed design clearly labeled.
- Maintain feature state and targets in the existing tracker when supported by actual decisions or implementation evidence. Accepted design is not implemented behavior or a passed release gate.
- For authorized release-document consolidation, follow the [release notes rules](../documentation/references/documentation/release-notes.md#consolidate-feature-documents): move completed release-specific feature content into versioned notes, preserve necessary contracts and links, then remove superseded standalone documents. Keep unfinished or future scope active.
- Check affected links, acceptance-criteria consistency, source/test references and release dependencies. Report unresolved decisions and unverified examples.
- After the user confirms the consolidated draft is ready for independent validation, invoke the read-only `feature-contract-reviewer` on the draft and relevant evidence. Do not ask it to make product or architecture decisions. Report its findings and questions to the user; resolve material decisions with the user and revise only from confirmed decisions. Repeat independent validation after material changes. If the user explicitly delegates bounded finalization, address remaining findings only within that authority, record decisions and assumptions, and continue to re-review material changes; return anything outside that scope to the user. Continue until findings are resolved or report remaining findings for the user's decision. If delegation is unsupported or the validator is unavailable, report validation as not performed and leave the draft unvalidated rather than substituting self-review.
- In either path, present the final candidate, validation result, decisions and remaining issues for explicit user acceptance. A clean review or delegated finalization is not acceptance. Acceptance authorizes the feature-design handoff only; implementation, independent change/security reviews, and PR creation remain separate work and approvals.
- For the requested end-of-work flow, identify independent readiness review by `change-reviewer` and the scope for `security-reviewer` when security review is requested or warranted by the feature's risks. Keep their review evidence and test/coverage evidence distinct; a passing test suite or coverage result is not a security audit. Do not claim either review is complete from design work.
- PR creation is a separate delivery action, not an automatic result of an accepted contract or completed implementation. Route it through the [change-delivery workflow](../agent-workflows/change-delivery-workflow.md) for explicit authorization and the required pre-PR review.
- Do not edit production code, source comments, dependencies, test/build/CI configuration or run workloads. Do not stage/commit/push, change approved release scope, or publish.
