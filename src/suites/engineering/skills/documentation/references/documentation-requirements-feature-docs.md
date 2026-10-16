# Feature documents

**Goal:** every feature document has the same shape, so readers can find its status, boundaries, and unresolved decisions quickly.

## When to use

Use this template for an active feature document, whether it is planned, partially implemented, or implemented and awaiting release consolidation. Keep the project overview high level and put feature detail here. Once release notes are ready, consolidate the completed features included in that release into the versioned notes and remove their standalone documents using the [release consolidation rules](./documentation-requirements-release-notes.md#consolidate-feature-documents).

## Rules

- **One feature per active document.** If a section starts describing another feature, move it to that feature's document and link to it. Versioned release notes may consolidate multiple completed features.
- **Scope is explicit.** List what is out of scope and link to the document that covers each item.
- **Current and planned are separate.** Describe existing behaviour under *Current implementation*, with links to the code. Describe planned work under *Design*. Never present planned behaviour as current.
- **Open questions stay in the document.** Number them with a short feature prefix (for example `QM-1`), say when an answer is needed, and reference the ID where the question comes up in the text. When answered, record the decision in the relevant section and move the row to *Answered*.
- **Status uses one of:** `Proposed`, `Accepted`, `Partially implemented`, `Implemented`. Update it in the same change that alters the feature's state, along with the feature tracker when tracking is adopted.
- **Omit sections that do not apply.** Do not add placeholder text; for example, a purely planned feature has no *Current implementation* section.

## Template

```markdown
# <Feature name>

Status: <Proposed | Accepted | Partially implemented | Implemented>

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
example "### 1. <Rule or component>". Include flows, examples, and the
reasoning for important choices.>

## Rule set

1. <Short, testable rule that summarises the design.>

## Open questions

These questions are deliberately left open until they are needed. When one is
answered, record the decision in the relevant section above and move it to
**Answered**.

| ID | Question | Needed by |
|---|---|---|
| <XX-1> | <Question> | <Milestone or feature that needs the answer> |

### Answered

None yet.
```

## Related conventions

- Where feature documents live and how status files work: [docs layout](./documentation-requirements-docs-layout.md).
- The feature tracker that lists every feature and its state is required by default and may be omitted only by an explicit, confirmed project-specific rule: [project tracking](./documentation-requirements-project-tracking.md).
