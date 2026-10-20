# Technical-debt registers

## Purpose and ownership

Use a technical-debt register to make confirmed, deferred engineering costs visible, actionable, and reviewable. The default location is `docs/status/technical-debt.md`; preserve an established project location. The accountable engineering owner maintains entries and updates them when impact, priority, status, or remediation changes.

Technical debt describes a deliberate or inherited maintainability cost and its consequences. It is not a decision log, feature roadmap, or list of every known bug. Link related decisions and known issues rather than duplicating their records.

## Structure

```markdown
# Technical debt

Updated: YYYY-MM-DD

| ID | Area | Debt and impact | Priority | Owner | State | Evidence / remediation |
|---|---|---|---|---|---|---|
| TD-1 | <Component> | <Confirmed debt and cost> | <Project-defined> | <Role/person> | Open | <Evidence and proposed remediation> |
```

## What belongs here

- Record concrete, evidence-backed maintenance costs, affected components, practical consequences, an accountable owner, current state, and a proposed remediation or review point.
- Use project-defined priority labels; do not invent a scoring system, delivery date, or commitment.
- Link any decision that accepted or deferred the debt and any known issue caused by it.
- Keep confirmed behavioral defects in the known-issues document. A proposed improvement without a demonstrated maintenance cost belongs on the roadmap or in a feature proposal.
- Reassess entries when evidence or the design changes. Close an item only after the debt is removed or explicitly accepted as a lasting trade-off, linking the relevant decision.

## Validation

Check that each entry describes a real, current cost rather than speculative cleanup, identifies an owner and impact, and has evidence or a specific validation need. Do not infer that an empty register means the project has no technical debt.
