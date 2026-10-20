---
name: release-planning-workflow
description: "Use to draft, update, or independently review a release plan for milestone scope, exclusions, dependencies, supported configurations, acceptance gates, and candidate evidence."
---

# Release planning workflow

## When to use

Use this skill when planning, updating, discussing, or reviewing a milestone release plan. Use it with the shared [product-planning workflow](product-planning-workflow.md), which owns cross-plan decisions, review coordination, and approval boundaries.

## Scope and boundaries

This workflow covers milestone goals, included and excluded scope, dependencies, supported configurations, planned acceptance and readiness gates, and evidence required to assess a candidate. A planning milestone is distinct from a package version or published release.

This skill does not authorize release implementation, packaging, testing workloads, go/no-go decisions, publication, or product approval. The user retains release-scope and approval authority. Reviewers remain read-only.

## Procedure

### Establish the release-plan context

1. Identify the milestone, intended audience, decision owner, established document location, and requested work mode.
2. Confirm the plan derives from an approved roadmap milestone. If no approved milestone exists, report that decision as a blocker and route it through the [roadmap planning workflow](roadmap-planning-workflow.md); do not treat a proposal as approved scope.
3. Read the approved milestone, relevant feature contracts, supported configurations, project release rules, known limitations, and existing decision records. Separate planned requirements from current implementation and executed evidence.

### Draft or update

- Follow the project's established release-plan format or the [release document guidance](../documentation/references/documentation/release-docs.md).
- Define the milestone goal, inclusions, exclusions, dependencies, supported configurations, functional acceptance requirements, and applicable readiness gates. Link detailed behavior to feature contracts rather than copying it.
- Define acceptance as observable outcomes and identify relevant verification methods. Record unknown thresholds and missing owners as unresolved decisions; do not invent defaults, coverage targets, budgets, commands, or evidence.
- Keep progress and candidate evidence specific to the milestone and candidate. A passing or completed feature does not prove a release gate.
- Include performance criteria only when they apply and have an approved scenario, metric, environment, resource budget, baseline, and threshold.
- Keep plan status distinct from roadmap approval, feature implementation state, candidate validation, and release outcome.

### Review an existing release plan

Check whether:

- the plan is traceable to an approved roadmap milestone or explicitly reports the missing approval as a blocker;
- the goal, included/excluded scope, dependencies, and supported configurations are specific and internally consistent;
- acceptance outcomes and required readiness gates are observable and tied to relevant feature contracts and verification methods;
- unknown thresholds, assumptions, blockers, and decision owners are visible rather than silently resolved;
- milestone progress, feature implementation, candidate evidence, and release outcome are kept distinct;
- any `Passed` gate has candidate-specific evidence, including revision/dirty state, artifact/configuration identity, commands or scenarios, results, and environment; and
- performance requirements, when present, have approved workloads, metrics, environments, budgets, baselines, and thresholds.

Report unsupported claims, missing evidence, contract inconsistencies, blockers, and product-owner decisions separately. Do not approve the plan, infer readiness from implementation state, or execute gates as part of review.

### Validate and report

Verify local links, milestone traceability, configuration and scope consistency, gate definitions, and candidate evidence where available. Report the reviewed candidate or plan revision, findings, unresolved decisions, evidence limitations, and checks not performed. A review result is not release go/no-go approval.
