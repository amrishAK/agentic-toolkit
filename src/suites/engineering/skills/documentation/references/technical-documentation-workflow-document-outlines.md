# Optional document outlines

## Purpose and requirement

These prompts help select a useful structure for task-specific technical documents. They do not replace the applicable document-type requirements in the [documentation catalogue](../documentation-requirements.md), and they do not require every listed document to exist.

## Structure

Choose only sections that serve the audience and purpose. Follow repository conventions; these are prompts, not required headings. Never invent evidence to fill a section.

## What belongs here

| Document | Purpose: the question it answers | Useful structure and content | Keep separate |
|---|---|---|---|
| README | What is this project, and how do I get started? | Purpose, supported prerequisites, quick start, minimal usage, development entry points, links to deeper docs | Detailed architecture, status tables, and procedures owned by deeper guides |
| User guide | How do I complete a supported user task? | Intended outcome, prerequisites, supported workflows, concrete examples, expected results, common failures | Unsupported usage and implementation-level detail |
| Setup/onboarding | How do I prepare an environment and verify the first successful workflow? | Platform/version requirements, working directory, installation/configuration, first successful workflow, verification, troubleshooting | Unverified prerequisites, commands, or platform support |
| Package/module guide | What does this module expose, depend on, and require to use safely? | Purpose, public surface, dependencies, lifecycle/ownership, configuration, usage, constraints, related modules | Contracts owned by canonical API/feature documents |
| Integration guide | How does this system interact with a supported external or public boundary? | Supported versions, boundary, configuration and credentials handling, minimal interaction, error/retry/lifecycle contracts, verification | Unsupported versions or undocumented external behavior |
| Data/request flow | How does information move through the system, and where are state and side effects introduced? | Scope, entry points and inputs, ordered stages, state/side effects, outputs, async/retry/persistence boundaries, failures, observability, invariants | Unverified behavior or decisions owned by architecture/feature documents |
| Runbook | How should an authorized operator diagnose and recover from a specific condition? | Symptoms/triggers, authorization and prerequisites, safe diagnosis, recovery, expected results, rollback, stop/escalation conditions | Unapproved actions or unclear irreversible steps |
| Troubleshooting | What checks can distinguish likely causes of an observed symptom? | Symptom, evidence/checks, possible causes distinguished from confirmed causes, corrective actions, verification, escalation | Speculation presented as a confirmed cause |
| Migration notes | How can affected users move between versions safely? | Source/target versions, affected users, behavior/configuration/data changes, prerequisites, ordered migration, verification, rollback limits | Unverified compatibility or rollback guarantees |

## How it resolves the reader's need

Use the purpose column to choose a document that answers the reader's actual question, the content column to select only useful sections, and the final column to avoid duplicating another document's authority.

- Separate user, developer, and operator detail when combining them would obscure the main task.
- Document alternatives and historical rationale only when evidence exists; mark new proposals as proposals.
- Runbooks must distinguish read-only diagnosis from state-changing recovery and irreversible actions.
- For diagrams, use the repository's supported format and accompanying text. Do not assume Mermaid renders everywhere.
- Keep examples consistent with platform/shell, version, working directory, and actual project tooling.
