# Decision log

## Purpose and ownership

Use the decision log as an index of important, accepted or proposed product and technical decisions, including decisions made by the user. The default location is `docs/status/decisions.md`; preserve an established project location. The relevant decision owner records or confirms each entry. Product priorities and scope remain with the product owner; technical decisions remain with their accountable technical owner.

The log is a concise register, not a substitute for detailed architecture decision records, feature contracts, release plans, or meeting transcripts. Link to the canonical document that contains the full context and consequences.

## Structure

```markdown
# Important decisions

Updated: YYYY-MM-DD

| ID | Date | Area | Decision | Status | Owner | Canonical record / consequences |
|---|---|---|---|---|---|---|
| DEC-1 | YYYY-MM-DD | Product | <Concise decision> | Proposed | <Decision owner> | <Link to rationale and affected scope> |
```

## What belongs here

- Record decisions that materially affect product goals, roadmap/release scope, public contracts, architecture, data, compatibility, security, operations, or long-lived maintenance.
- Include a stable ID, date, category, concise decision, status (`Proposed`, `Accepted`, `Rejected`, or `Superseded`), decision owner, and link to the canonical record and affected artifacts.
- Record user decisions as decisions only after the user has explicitly made or confirmed them. Distinguish the user's choice from agent recommendations and unresolved questions.
- When a decision changes, update its status and link to the superseding decision; do not silently overwrite history.
- Use an ADR for significant durable architecture context, alternatives, and consequences. The decision log points to the ADR rather than duplicating it. Link product decisions to the roadmap, release plan, or feature contract that reflects them.
- Capture technical debt in the separate technical-debt register. A decision that knowingly accepts or defers debt may link to that debt entry.
- Do not log routine implementation choices, every conversation turn, review findings, or unaccepted recommendations.

## Validation

Confirm the decision owner and status, verify that the canonical record reflects the decision, and check links and affected documents. A recorded decision does not by itself authorize implementation, release, or delivery.
