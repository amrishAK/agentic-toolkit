# Using Agentic Toolkit effectively

Agentic Toolkit helps you find reusable guidance for product planning and software development. It does not make decisions, run a required end-to-end process, or guarantee that a client discovers installed definitions. The [Software Product Development suite](../suites/software-product-development.md) describes the roles available today.

## Start with a clear task

Before choosing an agent or skill, decide what you need: a product plan, a feature contract, an implementation, a test, or a review. Give the agent the relevant project context and point to authoritative sources. Mark what is confirmed, proposed, assumed, or still unknown.

Choose an **agent** for role-specific responsibilities and boundaries. Choose a **skill** for a task method. Use the [skill selection workflow](../../src/skills/agent-workflows/skill-selection-workflow.md) and its [task matrix](../../src/skills/agent-workflows/references/skill-selection-workflow-matrix.md) to find relevant skills.

## Use current guidance; treat the wider model as proposed

The proposed lifecycle model groups work into three areas. It is a way to think about decisions, not an automatic route or a requirement to use every stage.

1. **Product Discovery & Shaping — proposed.** This area covers understanding a problem, exploring options, and identifying useful evidence. It is not a current role in the suite. Do not present generated ideas or questions as completed research.
2. **Product Management — current roles, with limits.** The [product-planner](../../src/agents/design-and-planning/product-planner.md) supports product direction, roadmaps, release plans, and scope trade-offs. The [product-plan-reviewer](../../src/agents/design-and-planning/product-plan-reviewer.md) reviews plans independently. Product-level feature-brief guidance remains proposed; detailed Engineering feature contracts are current.
3. **Engineering — current roles.** The [feature-designer](../../src/agents/design-and-planning/feature-designer.md) defines detailed behavior and handoffs. The [code-engineer](../../src/agents/implementation/code-engineer.md) implements authorized changes and verifies them. Testing and independent change review are available when appropriate.

Use only the guidance needed for the task. For security work, use the [security-reviewer](../../src/agents/review-and-security/security-reviewer.md) within its authorization and read-only assessment boundaries; it does not perform active probing or direct fixes.

## Keep decisions and handoffs clear

For significant decisions, record what was decided, who owns it, the evidence considered, and whether it is proposed or approved. Link each handoff to the relevant goal, contract, or prior decision.

A handoff asks someone to make a decision or take an action; it does not grant approval or authorization. A review is not approval, implementation is not verification, and verified work is not automatically release-ready.

## Keep the process proportionate

- Use the smallest useful record. Do not create a roadmap, release plan, or feature document just because a template exists.
- Reuse canonical project documents and link to them instead of making competing copies.
- Ask for evidence, assumptions, risks, open decisions, and the next useful step.
- Match the depth of analysis to the impact and uncertainty of the decision.
- If guidance or evidence is missing, say so instead of filling the gap with a guess.

People remain responsible for checking facts, deciding priorities, approving scope, and judging results. For the individual version of this approach, see [Using Agentic Toolkit as a solo developer](using-agentic-toolkit-as-a-solo-developer.md).
