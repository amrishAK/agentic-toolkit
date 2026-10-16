# Architecture documents

## Purpose and requirement

Architecture documentation explains how a system is organized, how its parts interact, and why important design choices exist. Use it when readers need more than a feature contract or a code-level reference. Preserve established project locations; the default is `docs/architecture/`.

For a system with several substantial concerns, use an architecture overview as the entry point and split detailed explanations by concern. Keep the overview useful on its own: summarize the system and its boundaries, show the major components or flow, and guide readers to deeper documents. A small system may keep this material in one document; do not split documents only to match this outline.

Keep implemented architecture separate from product direction, planned work, and feature contracts. State whether a document describes the current implementation or a proposed design. A review or proposal should put its conclusion or recommendation in a concise summary near the beginning; do not present a proposal as implemented or imply that a review is approval.

## Structure

Adapt this model to the system and audience. Omit sections that do not add useful information.

### Architecture guide or index

Use a short root document such as `docs/architecture.md` or `docs/architecture/README.md` to orient readers and navigate a set of architecture documents:

```markdown
# <System> architecture

<Brief summary of the system's purpose, architecture scope, and current
implementation status. State important boundaries or exclusions.>

## Start here
<Link to the high-level overview and point readers to the most useful
first documents for common audiences or questions.>

## Detailed architecture
| Document | Purpose | Audience |
|---|---|---|
| <relative link> | <Question this document answers> | <Readers it serves> |

## Decisions and limitations
<Link to the canonical design decisions, proposals, and known limitations.>
```

The index owns navigation, not the detailed explanations. Keep links and descriptions aligned with documents that actually exist.

### High-level system overview

```markdown
# <System> overview

<Opening summary: what the system is, what it does, its important design
priorities, and the boundaries of the current implementation.>

## What this overview covers
<System-level concerns included here and details delegated elsewhere.>

## System shape
<A readable diagram or concise description of the main components and flow.>

## Layers and responsibilities
| Layer or component | Responsibility | Detailed explanation |
|---|---|---|
| <Component> | <Responsibility> | <Relative link> |

## Architectural priorities
<Important design priorities and why they matter to this system.>

## Current system boundaries
| Boundary | Current behavior or limit | Further detail |
|---|---|---|
| <Boundary> | <Evidence-backed description> | <Relative link> |

## Reading guide
<Suggested path through the detailed documents.>
```

Use only sections that help readers understand the whole system. Keep algorithms, lock-level reasoning, data layouts, and other deep mechanics in focused documents.

### Focused architecture document

```markdown
# <Architecture concern>

**Design state:** <Current implementation | Proposed design | Partially implemented | Superseded>

## Summary
<The concern, its role in the system, and its key constraint or conclusion.>

## Scope
<What this document covers and what it leaves to other documents.>

## Design
<Relevant components, interfaces, ownership, lifecycle, and data flow.>

## Behavior and invariants
<Important state transitions, concurrency rules, resource limits, or
failure behavior, as applicable.>

## Decisions and trade-offs
<Evidence-backed rationale and consequences, or a link to the canonical
decision record.>

## Related documents
<Contracts, implementation evidence, tests, and neighboring architecture.>
```

Focused documents may use diagrams, tables, traces, or code references where they clarify the concern. Match detail to the topic; do not repeat the entire system overview.

### Architecture decision record or proposal

For a durable decision or proposed change, make its decision state and recommendation easy to find. Put proposals in the project's established proposal location (default `docs/proposals/`); keep accepted decisions with the established architecture decision records. Do not use this template for independent review findings.

```markdown
# <Decision or proposal title>

**Decision status:** <Proposed | Accepted | Rejected | Superseded>
**Implementation status:** <Not started | In progress | Implemented | Not applicable>

## Summary
<Problem, recommendation or decision, and most important consequence.>

## Context and constraints
<Current design, concrete problem, relevant requirements, and constraints.>

## Decision or proposal
<The selected or proposed architecture and its boundaries.>

## Alternatives considered
<Meaningful alternatives, including retaining the current design; explain
trade-offs without inventing historical discussion.>

## Consequences and risks
<Effects on components, interfaces, lifecycle, compatibility, operations,
testing, security, or performance where relevant.>

## Evidence and validation
<Implementation, contracts, tests, measurements, or verification still
needed. Distinguish observed facts from assumptions and unverified risks.>

## Related documents
<Affected architecture documents, contracts, proposals, and evidence.>
```

`Decision status` records whether the decision is proposed, accepted, rejected, or superseded. `Implementation status` separately records whether the accepted design has been implemented. Use the shorter `Title / Decision status / Context / Decision / Consequences / Evidence` form for a focused decision record, adding implementation status when it is not evident elsewhere. Put detailed feature behavior and acceptance criteria in the feature contract; link to it rather than copying it here.

### Architecture review

An architecture review is an independent assessment, not a design decision or proposal. Return findings in the review output with evidence, impact, and recommendations. Do not persist review findings as architecture documentation by default. If a recommendation is explicitly selected for design, record it separately as a proposal or decision using the structure above.

## What belongs here

Describe current components and responsibilities, dependency direction, interfaces, system shape, data flow, lifecycle, important invariants, failure behavior, resource or trust boundaries, and durable design decisions. For a proposal, include the problem, constraints, recommendation, meaningful alternatives, consequences, risks, and evidence needed to validate the decision. A review provides evidence-backed findings and recommendations without implying that a design decision has been made.

Split details by stable, reader-useful concerns such as data flow, concurrency, memory management, or subsystem design. Provide a navigation document when readers need help choosing among them. Keep a canonical explanation for each decision or contract and link to it from related documents.

## How it resolves the reader's need

The overview lets a reader quickly understand the system's purpose, shape, boundaries, and where to go next. Focused documents answer deeper implementation questions. Decision records and proposals make rationale, decision state, implementation state, consequences, and remaining uncertainty clear without confusing intended changes with current design. Independent reviews identify risks and recommendations without recording them as accepted decisions.

Architecture describes system design, not mutable feature progress, release readiness, or operational procedures. Link to those owners. Never turn an aspiration, review recommendation, or unverified diagram into a claim about deployed behavior.

## Validation

- Confirm that system summaries, components, interfaces, dependencies, lifecycle, and behavior match the relevant implementation and contracts; label material inferences.
- Check that the overview and index lead to real, current detailed documents and that each topic has a canonical owner.
- For proposals and decision records, distinguish decision status from implementation status; include meaningful alternatives and consequences, identify unresolved risks, and specify evidence or verification still needed.
- Keep architecture review findings separate from proposals and accepted decisions. A recommendation becomes a decision only through the project's decision process.
- Keep future designs in proposal/decision documents until implemented; then update the current-architecture owner and preserve the proposal's decision history.
- Label performance and security implications as risks unless supported by suitable evidence. Do not claim a design review proves measured improvement or security.
