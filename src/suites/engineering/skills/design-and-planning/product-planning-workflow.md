---
name: product-planning-workflow
description: "Use for high- and mid-level product discussion, product overviews, roadmap priorities, release goals, scope trade-offs, dependencies and acceptance planning. Not low-level feature design or implementation."
---

# Product planning

## Establish intent and scope

- Identify discussion/review versus requested document updates. Discussion produces proposals in the response, not unsolicited files. Explicit document work authorizes only relevant documentation edits.
- Read the project's purpose, audience, scope/non-goals, feature tracker, roadmap and affected release plans. For requested document work, load `documentation-requirements` or read [the document catalogue and rules](../documentation/documentation-requirements.md) to select the owning document and its rules.
- Separate user needs, proposed capabilities, implemented behavior and release commitments. Personal conventions yield to applicable organization/project requirements; surface conflicts rather than bypassing them.
- Ask one focused question when a material priority, scope or policy decision is unresolved. Offer evidence-based choices; never invent customer demand, estimates, dates, support promises or approval.

## Discuss and plan

- Explain the problem, intended users and observable value. Compare practical scope options and their costs, dependencies and risks.
- Keep the roadmap high-level and link detailed scope to release plans and contracts to feature documents. Prioritization proposals are not approved commitments.
- For release planning, establish goals, inclusions/exclusions, dependencies, supported configurations and measurable acceptance requirements with the user. Load [release guidance](../build-and-delivery/release-workflow.md) for relevant policy questions, not to execute packaging or delivery.
- Record unknown acceptance thresholds as unresolved, not invented defaults. Keep planned validation requirements distinct from existing runners and actual candidate evidence.
- Hand detailed behavior and implementation decisions to `feature-designer`. Consult [architecture guidance](./architecture-workflow.md) only when technical constraints materially affect product scope or sequencing.

## Maintain and validate

- Use [technical documentation guidance](../documentation/technical-documentation-workflow.md) for requested writing. Preserve canonical ownership; do not duplicate release progress in the overview or roadmap.
- Update only the agreed product/release documents and directly affected navigation or intended feature targets. Do not promote a feature to implemented without evidence.
- Return decisions, alternatives/trade-offs, unresolved questions, changed documents and validation limitations. Verify affected links and factual claims.
- Do not edit production code, build/test infrastructure or dependencies; run workloads; stage/commit/push; create releases; or publish. The user retains product priorities and go/no-go authority.
