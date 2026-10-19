# Technical guides

## Purpose and use

Use this reference for the guide type selected through the [documentation matrix](../documentation-matrix.md). The matrix owns document selection, locations, owners, and update triggers; this reference owns guide-specific content, structure, and validation. For README and documentation-index guidance, use [documentation layout](docs-layout.md#readme-and-documentation-index).

Apply the [common documentation rules](documentation-rules.md) and the relevant sections below. Create only guides needed for supported tasks. Suggested structures are prompts, not required headings; choose sections that serve the audience and purpose, follow established project formats, and never invent evidence to fill a section.

## User and developer guides

- **Structure and content:** Intended outcome, prerequisites, supported workflows, concrete examples, expected results, and common failures. For developer tasks, link the canonical build, test, and contribution instructions.
- **Keep separate:** Unsupported usage and implementation-level detail that does not help the reader complete the task.

## Setup and onboarding

- **Structure and content:** Platform/version requirements, working directory, installation/configuration, first successful workflow, verification, and troubleshooting.
- **Keep separate:** Unverified prerequisites, commands, or platform-support claims.

## Package and module guides

- **Structure and content:** Purpose, public surface, dependencies, lifecycle/ownership, configuration, usage, constraints, and related modules.
- **Keep separate:** Contracts owned by canonical API or feature documents; link to them rather than copying them.

## Integration guides

- **Structure and content:** Supported versions, boundary, configuration and credentials handling, minimal interaction, error/retry/lifecycle contracts, and verification.
- **Keep separate:** Unsupported versions or undocumented external behavior.

## Data and request flow

- **Structure and content:** Scope, entry points and inputs, ordered stages, state/side effects, outputs, async/retry/persistence boundaries, failures, observability, and invariants.
- **Keep separate:** Unverified behavior or decisions owned by architecture or feature documents.

## Runbooks

- **Structure and content:** Symptoms/triggers, authorization and prerequisites, safe diagnosis, recovery, expected results, rollback, and stop/escalation conditions.
- **Keep separate:** Unapproved actions or unclear irreversible steps. Distinguish read-only diagnosis from state-changing recovery and irreversible actions.

## Troubleshooting

- **Structure and content:** Symptom, evidence/checks, possible causes distinguished from confirmed causes, corrective actions, verification, and escalation.
- **Keep separate:** Speculation presented as a confirmed cause.

## Migration notes

- **Structure and content:** Source/target versions, affected users, behavior/configuration/data changes, prerequisites, ordered migration, verification, and rollback limits.
- **Keep separate:** Unverified compatibility or rollback guarantees.

## Writing and validation

- Separate user, developer, and operator detail when combining them would obscure the main task.
- Document alternatives and historical rationale only when evidence exists; mark new proposals as proposals.
- For diagrams, use the repository's supported format and accompanying text. Do not assume Mermaid renders everywhere.
- Check examples against the platform/shell, version, working directory, and actual project tooling. Include expected outcomes and relevant failure paths.
- Verify content against the applicable implementation and canonical contracts. In particular, check integration versions and lifecycle behavior, data-flow ordering and side effects, and migration compatibility and rollback limits.
- Check that operational steps identify authorization, state changes, irreversible effects, and stop/escalation conditions. Documentation validation does not authorize executing recovery or migration procedures.
- Use the specialist workflow linked by the selected [matrix entry](../documentation-matrix.md) for safe validation and reporting. Distinguish inspected examples from executed checks and report unverified claims or missing requirements.
