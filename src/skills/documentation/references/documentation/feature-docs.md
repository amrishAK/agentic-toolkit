# Feature documents

**Goal:** every feature document has the same shape, so readers can find its status, boundaries, and unresolved decisions quickly.

## When to use

Use this template for an active feature contract regardless of implementation stage—planned, partially implemented, or implemented and awaiting release consolidation. Its **Status** line records the contract decision, not implementation progress. Keep the project overview high level and put feature detail here. Once release notes are ready, consolidate the completed features included in that release into the versioned notes and remove their standalone documents using the [release consolidation rules](release-notes.md#consolidate-feature-documents).

## Rules

- **One feature per active document.** If a section starts describing another feature, move it to that feature's document and link to it. Versioned release notes may consolidate multiple completed features.
- **Scope is explicit.** List what is out of scope and link to the document that covers each item.
- **Current and planned are separate.** Describe existing behaviour under *Current implementation*, with links to the code and relevant tests. Describe intended but unimplemented behavior under *Design*. Never present a proposal or an unverified example as current behavior.
- **Open decisions stay in the document.** Number them with a short feature prefix (for example `QM-1`), identify who must decide and when an answer is needed, and reference the ID where the question comes up in the text. When answered, record the decision in the relevant section and move the row to *Answered*.
- **Status records the contract decision, not implementation progress.** Use `Proposed` while the detailed contract is awaiting agreement and `Accepted` once its decision owner has accepted it. Set it back to `Proposed` if an accepted contract is reopened for a material decision. Track implementation separately in the feature tracker when tracking is adopted: its `Planned`, `In progress`, `Done`, and `Not planned` states are not aliases for feature-document status. An accepted contract does not mean work has started, implementation is complete, or a release gate has passed.
- **Omit sections that do not apply.** Do not add placeholder text; for example, a purely planned feature has no *Current implementation* section.

## Review and validation

- Check that scope is bounded and each in-scope acceptance criterion describes an observable outcome, including relevant failure or edge cases; do not invent thresholds or decisions.
- Verify that proposal/design text is distinct from current behavior, and that implementation claims link to relevant source and test evidence. Label unverified examples or behavior.
- Confirm each open decision has an ID, decision owner, and needed-by point, and that answered decisions are recorded in the contract rather than left unresolved.
- When the project has adopted a tracker, compare its implementation state and evidence links with the documented decision and current code/tests. Keep the two status meanings separate; if no tracker exists, verify that an explicit confirmed project opt-out applies.
- Check local file links and heading fragments, including links to source, tests, related contracts, and the tracker.

## Template

```markdown
# <Feature name>

Status: <Proposed | Accepted>

## Summary

<Two to four sentences: what the feature does, why it exists, and what is
implemented today.>

## Scope

In scope:

- <capability>

Out of scope for this document:

- <capability>, covered by [<document>](<relative link>)

## Current implementation

<Only when something exists. Describe actual behaviour with links to code and
tests. List known gaps that planned work must close.>

## Design

<Planned behaviour. Use numbered subsections so rules can be referenced, for
example "### 1. <Rule or component>". Include applicable interfaces/API
contracts, architecture and durable decisions, data, compatibility, migration,
security, operations, rollout, and recovery concerns. Link a separate ADR only
for a significant durable architecture decision. Include flows, examples, and
the reasoning for important choices.>

## Acceptance criteria

For each criterion, include one or more acceptance scenarios that make the expected behavior concrete. Given/When/Then may be used when helpful, but is not required. Identify the applicable verification method and test tier; do not assume every criterion needs unit, integration, and E2E tests.

| ID | Observable outcome | Acceptance scenario(s) | Verification |
|---|---|---|---|
| <FEAT-1> | <Testable result, including relevant failure behavior> | <Scenario(s), optionally in Given/When/Then form> | <Applicable test tier and test or other verification link; label planned or unverified checks> |

## Rule set

1. <Short, testable rule that summarises the design.>

## Open questions

Categorize open questions by the area they affect (for example product/scope,
behavior/API, architecture, data/migration, compatibility, security/operations,
or verification). When a question is answered, record the decision in the
relevant section above and move it to **Answered**.

| ID | Category | Question | Decision owner | Needed by |
|---|---|---|---|---|
| <XX-1> | <Area> | <Question> | <Role or person> | <Milestone or feature that needs the answer> |

### Answered

None yet.
```

## Related conventions

- Where feature documents live and how status files work: [docs layout](docs-layout.md).
- The feature tracker that lists every feature and its state is required by default and may be omitted only by an explicit, confirmed project-specific rule: [project tracking](project-tracking.md).
