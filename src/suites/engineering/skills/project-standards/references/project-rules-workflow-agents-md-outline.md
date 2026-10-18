# AGENTS.md outline

Keep `AGENTS.md` short: it loads on every request. Use it for navigation and essential agent operations, not duplicated scope or architecture policies. Replace every `<placeholder>` with verified project facts, or delete the line. Link only existing paths; report missing authorities rather than inventing them.

Build the map from the [confirmed setup structure](./project-rules-workflow-setup-interview.md#structure-proposal-and-refinement), selecting only useful existing entry points from the [repository-wide placement map](./project-conventions-architecture-and-scope.md#repository-layout). Keep proposed/deferred paths and rationale in the setup proposal/report, not as fictional locations in `AGENTS.md`. Client-specific guidance directories are optional, not baseline scaffolding.

Feature tracking is required by default and may be omitted only by an explicit, confirmed project-specific rule; see [project tracking](../../../../../shared/skills/references/documentation/project-tracking.md). Include the tracker link and require same-change tracker updates when tracking is adopted; omit both when the project has confirmed an opt-out.

```markdown
# AGENTS.md

<One-sentence project orientation with a link to its user-facing entry point; keep changing status in its owning document.>

## Repository and context map

| Path | Purpose / authority | Consult when |
|---|---|---|
| <product overview link> | Product scope, non-goals and vision | Assessing product boundaries |
| <architecture/contract links> | Architecture constraints and public contracts | Changing relevant modules or APIs |
| <feature tracker link, when tracking is adopted> | Current implementation state | Checking or changing feature status |
| <release documents link> | Release scope, acceptance and evidence | Assessing release readiness |
| <source entry links> | Module ownership and implementation | Locating code for a task |
| <unit-test locations/guide links> | Unit tests, including inline tests if used | Testing local contracts |
| <integration/E2E guide links> | Established test tiers and prerequisites | Testing component or system workflows |
| <fixture/infrastructure links> | Test data and dependency setup | Changing or provisioning test resources |
| <benchmark guide/harness links> | Existing workloads, runners and performance evidence | Measuring performance |

Read task-relevant linked authorities and applicable scoped instructions before changing an area. Report contradictions rather than silently choosing a policy.

## Code conventions

- <Language edition/standard, MSRV or compiler support>
- <Module and error-handling patterns>

## Build and test

<Verified working directory and entry points. Claim CI parity only when confirmed.>

| Task | Command |
|---|---|
| Build | <command> |
| Unit tests | <command> |
| Integration tests | <command>; <infrastructure needed and setup link> |

- <Platform limits>

## Documentation

- Follow the linked scope, architecture and feature authorities; distinguish current behavior from planned work.
- Update adopted docs/status/ files in the same change that alters their status, including the feature tracker when tracking is adopted.
- Performance, coverage, and correctness claims must link to evidence.

## Commits

Conventional Commits: feat, fix, refactor, perf, test, docs, build, ci, chore.

## Agent boundaries

- <Paths agents must not modify, e.g. generated files>
- <Operations that need approval, e.g. publishing or changing CI secrets>
```
