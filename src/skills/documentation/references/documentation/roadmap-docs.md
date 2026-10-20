# Roadmap documents

## Purpose and ownership

Use a roadmap to communicate high-level direction, relative priorities, and proposed release sequence. The default location is `docs/status/roadmap.md`; preserve an established project location. The `product-planner` owns the roadmap, and the responsible product owner approves its direction and priorities.

A roadmap may organize work into proposed release milestones, beginning with an MVP when that is useful. The MVP is a scope decision, not an assumption that every possible platform or build system belongs in the first release. Do not invent version numbers, dates, commitments, or priorities.

## Structure

```markdown
# Roadmap

Updated: YYYY-MM-DD

<Purpose, current baseline, and whether release order is proposed or approved.>

## <Release or priority>
**Status:** Proposed | Approved

<Short outcome and concise feature summary.>

<Link to the release plan when its scope is defined.>

## Unassigned direction
<Evidence-backed future direction without a committed release target.>
```

## What belongs here

- Keep entries concise: intended outcome, short capability summary, decision status, and a link to a separately maintained release plan when one exists.
- Treat status as roadmap-decision status, not feature implementation progress or release readiness. Use the release plan for included/excluded scope, gates, blockers, progress, and candidate evidence.
- Distinguish current capability, proposed direction, and approved priority. Link to evidence or the project overview as appropriate.
- Label unassigned ideas. Do not force every idea into a release or target version.
- Update the `Updated` date when content changes. Record material user decisions in the canonical decision log, not as prose history in the roadmap.

## Validation

- Confirm every release link resolves and the roadmap summary agrees with its release plan.
- Check that approved priorities have an identified decision owner and evidence or rationale, and that proposed items are not presented as commitments.
- Do not duplicate feature state, release gates, known issues, technical debt, or detailed acceptance criteria here.
