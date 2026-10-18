---
name: architecture-workflow
description: "Use for architecture design or review involving component boundaries, dependency direction, public interfaces, lifecycle, data flow, storage/protocol choices, compatibility or significant cross-feature decisions. Supports feature design, implementation and review without expanding authorization."
---

# Architecture workflow

## When to use

Use this skill to design or review significant architecture decisions.

## Scope and boundaries

This skill supplies a method, not a new role or edit permission. Apply the active agent's scope and project requirements.

## Procedure

### Understand the system

- Read existing architecture, contracts, decisions, relevant implementation and consumers. Identify system scope, supported environments and non-goals.
- Consult the existing [architecture and scope conventions](../project-standards/references/project-conventions-architecture-and-scope.md) only as defaults; project-owned boundaries take precedence over personal design preferences.
- Distinguish implemented architecture from intended design and proposals. Surface contradictions without documenting defects as guarantees.
- Trace relevant responsibilities, dependency direction, state/data flow, ownership/lifetimes, failure propagation, concurrency and trust/resource boundaries. Investigate only what the decision affects.

### Evaluate a decision

- State the concrete problem and constraints. Compare the simplest adequate option with meaningful alternatives, including retaining the current design.
- Assess cohesion/coupling, public API/ABI or protocol contracts, testability, operational complexity and supported toolchains where relevant.
- Include persistence/migrations, backward compatibility, failure recovery and rollout/rollback limits when affected.
- Treat security/performance implications as risks requiring appropriate evidence. Do not claim security certification or measured improvements from a design review.
- Avoid speculative frameworks, interfaces for every type, premature distribution and arbitrary layer rules. Reuse existing boundaries and helpers when they fit.
- Ask before changing agreed architectural commitments. Escalate product/release-scope trade-offs to the user and product planning instead of silently expanding scope.

### Record and hand off

- Follow the [architecture document and decision outlines](../../../../shared/skills/references/documentation/architecture-docs.md) only when documentation is requested or directly coupled to authorized implementation.
- Record context, proposed/accepted status, decision, consequences and evidence. Never invent historical alternatives or approvals.
- Keep current architecture accurate after implementation; preserve proposal/decision history rather than presenting a future design as deployed.
- End with the recommended decision, affected contracts/components, open risks and verification needed. Review-only work returns findings without files or edits.
