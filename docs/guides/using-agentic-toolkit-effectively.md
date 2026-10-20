# Using Agentic Toolkit effectively

> **Status:** This guide describes a proposed lifecycle model, not a currently available end-to-end workflow. The maintained Software Product Development suite provides `product-management` and `engineer` packages, each including its respective independent reviewers. Discovery & Shaping and product-level feature-brief guidance remain proposed. For current roles and task routes, see the [suite guide](../suites/software-product-development.md) and [documentation index](../README.md).

Agentic Toolkit is intended to help people and teams do important software lifecycle work with less coordination overhead and better traceability. Use agents to surface gaps, organize project facts, connect decisions to evidence, and prepare useful handoffs—not to replace people or make decisions on their behalf.

## Start with the decision or outcome

Before invoking an agent, state what you need to understand or decide. Examples include:

- Is this user problem worth addressing?
- Which product outcome should a target version prioritize?
- What technical approach can meet an approved product need?
- Is a proposed scope change justified?

Give the agent the relevant project context and identify what is authoritative. This may include product goals, user research, constraints, existing architecture, supported environments, decisions already made, and current scope. Link to source documents where possible. Distinguish confirmed facts from assumptions, proposals, and questions.

Ask the agent to identify missing or conflicting information before it draws conclusions. Do not present generated summaries as verified project facts until a person has checked them against their sources.

## Apply the model with current guidance

The three-stage model below is future direction, not an automatic route through the toolkit. For work covered today, start with the current [suite guide](../suites/software-product-development.md), which links to maintained roles and workflows. Product planning and plan review are available through `product-management`; technical design, delivery, testing, and technical review are available through `engineer`. These are packages, not separate suites.

For an authorized source security review, use the [security-reviewer role](../../src/agents/review-and-security/security-reviewer.md) and its [security review workflow](../../src/skills/review-and-security/security-review-workflow.md). Assessment is read-only: it does not include command execution, active probing, or direct remediation. Fixes require an explicit selection and delegated editing; if the client cannot support that delegation, the reviewer must report the limitation rather than edit directly.

## Use the proposed lifecycle model

The proposed three-stage lifecycle model describes decision-support handoffs, not a required sequence or separate people. Use only the stage needed for the current decision; do not repeat completed work just to follow a process.

### 1. Product Discovery & Shaping

Use this stage when the problem, users, or opportunity are not yet clear. It can help plan research, structure supplied findings, explore use cases and solution options, challenge assumptions, and prepare a high-level proposal.

The proposal should make clear:

- Who has the problem and what evidence supports that claim
- The user need, opportunity, and relevant use cases
- Candidate solutions and meaningful scope trade-offs
- Assumptions, risks, unknowns, and further research needed
- What decision is being requested

Do not describe research as conducted unless there are actual findings. Treat generated hypotheses and devil's-advocate questions as prompts for investigation, not evidence that a risk exists or has been resolved.

### 2. Product Management

Use this stage to evaluate a proposal against product direction and constraints. It can help compare opportunities, shape goals and roadmap priorities, propose target-version scope, and produce product-level feature briefs.

Product-level feature briefs should describe user-visible outcomes, intended scope and exclusions, dependencies, success measures, and acceptance examples. Acceptance criteria are observable conditions for judging an outcome; examples illustrate expected behavior. Behavior-driven scenarios can help make outcomes concrete. Keep detailed technical contracts and implementation task breakdown for Engineering.

Plan in sequence: create and approve the high-level roadmap first, then plan individual releases from approved roadmap milestones. Keep roadmap entries brief and link to release plans; keep release scope, gates, and readiness evidence in the release plan. The `product-planner` can request independent read-only validation from `product-plan-reviewer`; the reviewer surfaces gaps and questions but does not decide priorities or approve the plan.

Priorities, roadmaps, target versions, and release scope remain proposals until the responsible product owner approves them. Ask the agent to make trade-offs and deferred work explicit rather than silently expanding scope.

### 3. Engineering

Use this stage after product intent and scope are sufficiently clear. Engineering should validate technical feasibility, identify technical risks and dependencies, elaborate architecture and feature contracts, plan implementation and verification, and deliver evidence about the result.

Engineering may discover that a product assumption is infeasible or that scope needs to change. Route that information back to the product decision owner; do not let a technical workaround silently redefine the user outcome or approved scope.

## Keep decisions and scope traceable

For each significant decision, preserve a short record of:

- The decision and its owner
- The evidence and constraints considered
- Alternatives or trade-offs that materially affected the choice
- The decision status: open, proposed, or approved
- Consequences for scope, roadmap, architecture, or release

Link handoffs to the user need, product goal, or prior decision they address. When scope changes, record what changed, why, who approved it, and what was deferred or affected. Agents can help identify missing links and summarize change impact, but people must verify the record and approve the change.

## Keep the process proportionate

- Use the smallest useful artifact for the decision. A small effort may combine research findings and a proposal; a roadmap or release plan is useful when there are actual priorities or versions to manage.
- Reuse and update canonical project documents rather than creating competing copies.
- Ask for concise outputs that include evidence, assumptions, decisions needed, risks, and next handoff.
- Do not repeat research, analysis, or design without a reason. Ask what changed since the prior decision.
- Record unresolved questions instead of filling gaps with invented facts, estimates, or commitments.
- Match the depth of analysis to the impact and uncertainty of the decision; do not mistake longer documents for better decisions.

## Select relevant technical guidance

For Engineering work, provide the project's actual stack and deployment context, then check the relevant maintained catalogues and workflows. A project might use a Vue frontend, Rust backend, containers, and Azure infrastructure defined with Bicep; that context would help select applicable guidance if it exists.

Do not infer technology coverage from an example or catalogue category. Language, framework, runtime, container, cloud, and infrastructure guidance may each have different scope. Deployment, validation, security, and operations should account for the actual target platform and toolchain. If relevant guidance is missing, make that gap explicit instead of substituting unrelated guidance.

## Human review and responsibility

At each handoff, the responsible person should check that:

1. Important claims are supported by project evidence or clearly marked as assumptions.
2. The output answers the intended decision and preserves relevant constraints.
3. Scope, risks, dependencies, and unresolved questions are visible.
4. The next responsible person or role accepts the context and understands what decision or action is needed.

Agents can help teams notice lifecycle gaps and avoid preventable omissions or scope creep. They cannot guarantee that every step is completed, that facts are correct, or that scope will not change. People remain responsible for validation, judgment, priorities, approvals, and outcomes.

For the proposed suite boundaries and document flow, see the [V2 project overview](../proposals/project-overview-v2.md).
