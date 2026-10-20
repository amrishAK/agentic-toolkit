# Documentation layout

This guidance covers the documentation tree and its entry points only, so readers and agents can tell current behaviour from plans, and stable content from content that changes often. It does not own interviewing or repository initialization. Use the [repository-wide placement map](../../../project-standards/references/project-conventions-architecture-and-scope.md#repository-layout) for code, tests, tools and other repository items, and the [setup workflow](../../../project-standards/project-rules-workflow.md) to inspect, propose, refine, confirm and create agreed essentials.

## Layout

```text
docs/
  README.md            Index: what lives where, and where to start
  architecture/        Current design: components, boundaries, data flow, decisions
  guides/              Build, test, usage, integration, troubleshooting
  proposals/           Active feature contracts: proposed or accepted, possibly awaiting or undergoing implementation
  status/              Feature tracker (when adopted), roadmap, known issues, decisions, technical debt
  releases/            Milestone plans, gates and evidence; versioned notes consolidating completed features
  reports/             Dated incident reports and investigations
```

- This is an adaptable docs tree, not a directory-creation checklist. Create only folders needed for applicable, confirmed documents with useful content. Preserve confirmed opt-outs, including feature tracking; see [project tracking](project-tracking.md).
- Name files in lowercase kebab-case, such as `concurrency-model.md`. Root files keep their standard names: `README.md`, `LICENSE`, `CHANGELOG.md`, `CONTRIBUTING.md`, `SECURITY.md`, `AGENTS.md`.
- A directory that needs local explanation, such as `tests/`, `.github/` or a build folder, may have a short `README.md` that links to the canonical guide instead of repeating it.
- Preserve established project locations, including a shared `features/` folder for current and planned feature references, when adopted by the repository. Do not migrate paths merely to match this default layout.
- Use the [document catalogue](../documentation-matrix.md) to select applicable documents and find their canonical owners and rules; it does not require every file in every project.

## README and documentation index

The README is the project entry point. Keep its summary aligned with [project tracking](project-tracking.md), describe current status with a link to the feature tracker when tracking is adopted, and provide a first successful supported workflow. Include verified prerequisites, quick-start steps, development entry points, links to deeper documentation, and the confirmed license. Do not duplicate detailed architecture or feature status.

```markdown
# <Project name>

<Confirmed summary: purpose, audience, problem, and current stage.>

## Status
<Availability and limitations; link to the canonical feature tracker when adopted and applicable plans.>

## Prerequisites
<Verified tools/versions, working directory, and platform/shell requirements.>

## Quick start
<Minimal supported setup and usage, with expected result.>

## Development
<Build/default-test entry points; link to the full development/test guide.>

## Documentation
<Links to the project guide, overview, contracts, status, and applicable guides.>

## License
<Confirmed license and link; no guessed licensing statement.>
```

When navigation spans multiple documents or audiences, add a documentation index, typically `docs/README.md`. Explain who the docs serve and how to choose a starting point; use a short task/audience-to-document map that identifies each document's canonical topic. Link to the sources of current behavior, plans, status, and historical evidence rather than copying them.

```markdown
# Documentation

<Who these docs serve and how to choose a starting point.>

| Task / audience | Document | What it owns |
|---|---|---|
| <Task> | <Relative link> | <Canonical topic> |

## Documentation maintenance
<Where current behavior, plans, status, and historical evidence belong.>
```

## What goes where

- **`architecture/`** describes only implemented behaviour. Record each design decision with the decision, rationale, and trade-off, in one place.
- **`proposals/`** holds active feature documents with a contract-decision status of `Proposed` or `Accepted`. This status does not describe implementation progress; the feature tracker records implementation state when adopted. Keep implemented features here while they await release consolidation; update `architecture/` for current behavior, which remains its authority. When versioned release notes are ready, consolidate completed features and remove superseded documents according to the [release notes requirements](release-notes.md#consolidate-feature-documents). Keep unfinished or future work active. Use the [feature document template](feature-docs.md).
- **`status/`** files carry an `Updated: YYYY-MM-DD` line. Update them in the same change that alters status, such as fixing a listed issue, completing a roadmap item, recording a decision, or changing a debt entry. A stale status file is a defect.
- **Product overview** describes product purpose, audience, intended usage, architecture direction, responsibilities and non-goals. Link the feature tracker when adopted and applicable plans; keep progress tables, acceptance gates and open decisions in their owners.
- Use the [product overview outline](product-overview.md) when a README does not provide enough room for product intent and boundaries.
- **`releases/`** holds milestone scope, observable acceptance, blockers, and candidate evidence, as well as adopted versioned release notes that consolidate completed features. Update readiness gates with changes affecting readiness; passing requires linked evidence for the candidate, not just an implemented feature. Follow the [release notes requirements](release-notes.md).
- **Roadmap** records high-level direction and proposed or approved priorities, not release progress or detailed acceptance. Link release documents instead of duplicating their scope/gates. Use the decision log for material product or technical choices; use the debt register for confirmed engineering liabilities.
- **Known issues** records confirmed user- or operator-impacting defects and limitations. Keep speculative risks, planned work, and technical debt in their respective owners.
- **Decision log** indexes important user, product, and technical decisions and links to their canonical records. It complements rather than replaces architecture decision records and feature contracts.
- **Technical-debt register** records confirmed maintenance costs, impact, accountable owner, state, and remediation links. It is separate from both the decision log and known-issues list.
- **`reports/`** files are named `YYYY-MM-DD-topic.md` and record symptom, root cause, fix, verification, and current state. They are historical records: add follow-ups rather than rewriting them.

## One source of truth

- Each topic has one canonical document. Others link to it with relative links.
- The root README states purpose and status briefly and links to `docs/` for detail.
- Do not copy changing facts, such as test counts, coverage, or benchmark results, into multiple documents. Link to the source.

## Claims need evidence

- Every performance, coverage, or correctness claim links to its evidence: a benchmark result, CI threshold, or test.
- Claims match the latest evidence. Remove or qualify a claim when an open known issue contradicts it.
- Avoid absolutes such as "zero data loss" or "no race conditions" unless they are proven and no open issue contradicts them.
- Mark fixture credentials and sample secrets as test-only.
