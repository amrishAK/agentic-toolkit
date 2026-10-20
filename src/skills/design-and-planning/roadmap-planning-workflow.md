---
name: roadmap-planning-workflow
description: "Use to draft, update, or independently review a product roadmap covering high-level direction, relative priorities, and proposed release sequence."
---

# Roadmap planning workflow

## When to use

Use this skill when creating, updating, discussing, or reviewing a product roadmap. Use it with the shared [product-planning workflow](product-planning-workflow.md), which owns cross-plan decisions, review coordination, and approval boundaries.

## Scope and boundaries

This workflow covers roadmap direction, relative priorities, proposed release sequence, and links to defined release plans. It does not define detailed milestone scope, feature behavior, implementation state, candidate readiness, release notes, or product approval.

The product owner retains priority and approval authority. The active agent's permissions determine whether it may edit. A reviewer remains read-only and reports findings instead of revising the roadmap.

## Procedure

### Establish the roadmap context

1. Identify the roadmap's audience, purpose, current baseline, established location, decision owner, and whether the document records proposed or approved direction.
2. Read the project's purpose and boundaries, existing roadmap, relevant decisions, and linked release plans. Distinguish current capabilities from proposed direction and approved priorities.
3. If the source of direction or priority is unclear, state the evidence gap and ask the product owner; do not invent customer demand, prioritization rationale, release dates, version numbers, or commitments.

### Draft or update

- Use the project's established roadmap location; otherwise follow the [roadmap document guidance](../documentation/references/documentation/roadmap-docs.md).
- Keep each entry concise: intended outcome, brief capability summary, decision status, and a link to a separate release plan when one exists.
- Use proposed milestones and relative sequence only where supported by the product owner's direction. An MVP is an explicit scope choice, not a default commitment.
- Label unassigned future direction. Do not force every idea into a release or target version.
- Update the document's `Updated` date when its content changes and record material decisions in the canonical decision log when maintained.
- Keep roadmap status about decision/priority status only. Leave inclusions, exclusions, progress, blockers, gates, acceptance detail, and candidate evidence to the release plan.

### Review an existing roadmap

Check whether:

- the roadmap states its purpose, baseline, and whether direction or release order is proposed or approved;
- entries communicate outcomes and concise capabilities without becoming a feature inventory or progress tracker;
- priority and sequencing claims have an identified decision owner and evidence or rationale;
- proposed items are not phrased as commitments, and no dates or versions are invented;
- release links resolve and any linked plan agrees with the roadmap's summary; and
- current capability, proposed direction, and approved priority are clearly distinguished.

Report factual defects, unsupported claims, unresolved product decisions, and optional suggestions separately. Do not decide priorities or rewrite the plan on the user's behalf.

### Validate and report

Verify local links and anchors, status meaning, the `Updated` date, and consistency with linked release plans and canonical product decisions. Report the reviewed source, evidence and limitations, findings, questions for the product owner, and any claims that could not be verified. A clean review does not constitute roadmap approval.
