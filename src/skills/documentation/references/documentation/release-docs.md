# Release document outline

## Purpose and requirement

Use a release document when a milestone is planned. The default location is `docs/releases/<milestone>.md`. It owns milestone scope and readiness, not feature implementation state or high-level roadmap direction. Distinguish a planning milestone from a package version or published release.

For a user-facing summary of delivered changes and upgrade actions, use the separate [release notes requirements](release-notes.md).

## Structure

```markdown
# <Milestone> release acceptance

Updated: <YYYY-MM-DD>
Status: <Planning / candidate assessment / outcome, based on evidence>

## Goal and scope
<Included capabilities with contract links; explicit exclusions.>

## Progress and evidence rules
Track milestone/release progress and candidate evidence in this table, separately from the feature tracker (when adopted), which records implementation state.

| Gate | Requirement | State | Evidence / remaining work |
|---|---|---|---|
| <REL-G1> | <Observable gate> | Pending | <Evidence needed> |

## Functional acceptance
| ID | Observable acceptance outcome | Verification / contract |
|---|---|---|
| <REL-F1> | <Testable outcome> | <Owner or test evidence> |

## End-to-end acceptance
| ID | Journey and oracle | State / evidence |
|---|---|---|
| <REL-E1> | <Public workflow and exact expected outcome> | Pending |

## Performance acceptance
<Only if applicable: scenarios, metrics, environment, resource budgets,
approved thresholds, baseline, and comparison policy.>

## Decisions and blockers
| Decision | Owner / required outcome | State |
|---|---|---|
| <Decision> | <Canonical contract/question link> | <State> |

## Candidate evidence and go/no-go
<Candidate identity, results, failures/skips, compatibility, known issues,
approved exceptions, decision, and decision authority.>

## Existing validation commands
<Current runners and prerequisites, distinct from future required runners.>
```

Adapt the sections to the milestone. Establish scope, supported configurations, required gates, performance budgets when applicable, compatibility, and approval policy before writing. Omit inapplicable gates only through an explicit scope decision.

## What belongs here

Record milestone goals, scope and exclusions, observable acceptance, readiness gates, blockers, and candidate-specific evidence. Gate states default to `Pending`, `In progress`, `Passed`, and `Blocked`, unless the project establishes another vocabulary.

## How it resolves the release decision

The release document makes readiness assessable for a specific milestone and candidate. It separates planned scope from implementation status and requires evidence for the candidate rather than treating implemented features as proof of release readiness.

## Validation

- `Passed` requires linked evidence for the assessed candidate: revision/dirty state, artifact and configuration identity, commands/scenarios, results, and environment. Missing or skipped runs are not passes; implemented features alone do not pass gates.
- A changed candidate reruns affected gates or explicitly justifies reused evidence. Failures and unresolved required thresholds remain blockers.
- Never invent budgets or silently relax them. Update readiness gates separately from feature state.
