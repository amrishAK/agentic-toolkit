# Using Agentic Toolkit as a solo developer

You may own research, product decisions, design, implementation, testing, and release approval yourself. Agentic Toolkit can help you think through each part without requiring a large team process. You remain responsible for checking evidence and making decisions.

The broader Product Discovery & Shaping lifecycle model is proposed, not a current end-to-end workflow or available role. Current product-planning and Engineering roles are listed in the [Software Product Development suite](../suites/software-product-development.md).

## Keep one simple project record

Start with a short document that records:

- The user or audience and the problem
- Evidence, assumptions, and open questions
- The intended outcome and how you will recognize it
- Current scope, exclusions, and constraints
- Important decisions and who approved them

For a small project, one document may be enough. Add research notes, feature contracts, or a release plan only when they help answer a real question. Link to existing project sources instead of copying them.

## Work in small decision loops

1. **Clarify the problem.** Write down what you know and what you still need to learn. You can ask an available agent to organize supplied research or suggest questions, but generated ideas and personas are not research evidence.
2. **Choose the next outcome.** Use the current [product-planner](../../src/agents/design-and-planning/product-planner.md) for roadmap or release planning when you need it. For a small project, a short ordered list of outcomes may be more useful than a formal roadmap.
3. **Describe behavior when needed.** Use the [feature-designer](../../src/agents/design-and-planning/feature-designer.md) for detailed behavior, edge cases, acceptance criteria, and an implementation handoff. Not every small change needs a new feature document.
4. **Build and check the result.** Give Engineering the agreed goal, scope, constraints, project stack, and open questions. Ask for an appropriate implementation and verification plan. Compare the result with the intended outcome and record what you actually checked.

If technical work reveals that the agreed scope or user outcome should change, make that a deliberate product decision rather than silently changing the plan in code.

## Keep agent work focused

- State the decision or outcome you need, and provide links to the relevant project sources.
- Ask for concise results: evidence, assumptions, risks, decisions needed, and a suggested next step.
- Ask what the agent could not verify. Treat its output as advice, not proof.
- Update the canonical project record instead of creating parallel notes.
- Stop when you have enough information for the next decision; revisit it when new evidence changes the situation.

## Protect your focus

When a new idea comes up, capture it without automatically adding it to current work. Ask:

1. Does it support the current user outcome?
2. What evidence or constraint makes it important now?
3. What would be delayed or dropped if you include it?
4. Can the decision wait?

Record the decision and its reason briefly. Changing scope is sometimes right; make the change visible.

## You remain the decision-maker

Check important claims against project sources, choose priorities, approve scope changes, and decide whether the result is ready for its intended use. Agents can help you find gaps, but cannot guarantee that research is representative, advice is correct, or work is complete.

For the broader proposed lifecycle model, see [Using Agentic Toolkit effectively](using-agentic-toolkit-effectively.md). For current roles and handoffs, use the [suite guide](../suites/software-product-development.md).
