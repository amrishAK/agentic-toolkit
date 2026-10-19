# Using Agentic Toolkit as a solo developer

> **Status:** This guide describes a proposed way for a solo developer to apply a broader lifecycle model, not a currently available end-to-end workflow. Discovery & Shaping and Product Management are not maintained suites here; the Engineering suite is. For current roles and task routes, see the [Engineering suite guide](../suites/engineering.md) and [documentation index](../README.md).

As a solo developer, you may be the researcher, product owner, designer, engineer, tester, and release decision-maker. Agentic Toolkit is intended to help you cover those perspectives without making you follow a heavyweight team process. Agents can help you ask better questions, organize evidence, identify gaps, and challenge your reasoning; you remain responsible for verifying facts and making decisions.

For the general workflow and shared principles, see [Using Agentic Toolkit effectively](using-agentic-toolkit-effectively.md). This guide focuses on keeping that workflow practical for one person.

## Use a lightweight project record

Start with one short, canonical project brief. Keep only the context that helps you make and revisit decisions:

- The user or audience and the problem you are trying to solve
- Evidence you have, and assumptions you still need to test
- The outcome you want and how you might recognize progress
- Current scope, explicit exclusions, and important constraints
- Significant decisions, their status, and unresolved questions

For a small project, this can be a single document. Add separate research notes, feature briefs, architecture decisions, or release plans only when they answer a real question or make a significant decision easier to track. Prefer links to existing project sources over copying their contents.

## Work in short decision loops

### 1. Clarify the problem

Ask a discovery-oriented agent to help state the problem, identify affected users, list assumptions, and suggest what evidence would reduce uncertainty. If you have real user feedback or research, provide it and ask for a synthesis that separates findings from interpretation.

If you do not have evidence, say so. The agent can help plan a small, appropriate research step or identify what you can validate directly, but generated personas, hypotheses, and interview questions are not user research findings.

### 2. Shape a bounded proposal

Ask for a few plausible solution options and their trade-offs, not an open-ended feature list. Use devil's-advocate review to surface risks, overlooked cases, and reasons the idea may not work. Treat these as questions to assess, not confirmed problems.

Write down the chosen direction, what is out of scope, the key assumptions, and the next decision. Keep the proposal brief enough to revisit as you learn.

### 3. Choose the next valuable slice

Use product-planning guidance to connect the proposal to a concrete user outcome. In the current Engineering suite, the [product-planner role](../../src/agents/design-and-planning/product-planner.md) provides this kind of guidance; the separate Product Management stage is proposed future direction. Define a small next increment, its boundaries, dependencies, and acceptance criteria, using examples to illustrate expected behavior. If you use BDD-style scenarios, make them describe user-visible behavior; avoid turning them into implementation prescriptions unless that is genuinely required.

Do not create a formal roadmap or version plan just because a template exists. For a solo project, a short ordered list of outcomes and a clear current focus may be enough. Record a target version only when you have a meaningful reason to plan against one.

### 4. Validate the engineering approach

Before building, give Engineering the approved product intent, scope, constraints, actual project stack, and unresolved technical questions. Ask it to identify feasibility concerns and propose the smallest adequate technical plan and verification approach.

Use guidance for the technologies and deployment platform the project actually uses. If suitable guidance is absent, note the gap rather than assuming a catalogue or example covers it.

### 5. Review the result and update the record

Compare what you built and verified with the intended user outcome. Record evidence, incomplete work, decisions that changed, and the next question. If implementation reveals a new constraint, revisit product scope explicitly rather than allowing the change to disappear into the code.

## Keep agent work useful

- Ask one agent task at a time when the decision or expected output is clear; use different perspectives when you need a deliberate challenge or independent technical review.
- Provide links or excerpts from the actual project context. Ask the agent to identify what it could not verify.
- Request concise results: recommendation, supporting evidence, assumptions, risks, decision needed, and next step.
- Ask agents to update or summarize the canonical project record when appropriate, rather than spawning parallel notes.
- Use an agent as a critic or thought partner, not as proof that an idea, design, or implementation is correct.
- Stop analysis when you have enough evidence to make the next proportionate decision; revisit it if new information changes the case.

## Protect focus and scope

When a new idea appears, capture it as a candidate rather than adding it automatically to current work. Ask:

1. Does it serve the current user outcome?
2. What evidence or constraint makes it important now?
3. What would be delayed or removed if it is included?
4. Is this a decision to make now, or a question to revisit later?

Record your decision and its rationale briefly. Scope can change for good reasons; the goal is to make the change intentional and visible, not to prohibit change.

## Your responsibility as decision-maker

As a solo developer, you retain the approvals a team might otherwise distribute. Check important claims against project sources, decide whether evidence is sufficient, choose priorities, approve scope changes, and judge whether the result is ready for its intended use.

Agents can help surface gaps and reduce avoidable overhead, but they cannot guarantee that every lifecycle step is complete, that research is representative, that technical advice is correct, or that scope will not change. The workflow should help you make better-informed decisions while keeping you in control.

For the proposed suite boundaries and handoffs, see the [V2 project overview](../proposals/project-overview-v2.md).
