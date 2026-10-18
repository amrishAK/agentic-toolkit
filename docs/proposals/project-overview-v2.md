# Project overview (proposed V2)

> **Status:** This document proposes a future product direction for Agentic Toolkit. It does not describe the repository's current suite coverage or establish a delivery commitment. The existing [project overview](../project-overview.md) remains the current overview.

Agentic Toolkit aims to provide reusable agent and skill guidance that helps people and teams move software work from understanding a user problem through product decisions and into engineering delivery. Its intended boundary is to augment human work with structured guidance and handoffs, not replace the people doing it.

## Product philosophy

Agentic Toolkit is intended to help people and teams follow important software lifecycle steps with less coordination overhead and greater traceability. Its guidance should surface missing steps, connect decisions to project facts and evidence, and make scope, uncertainty, and open questions visible when they matter. This can help teams make informed decisions at the right time and prevent avoidable omissions and scope creep.

The workflow is designed for human oversight. Agents can organize information, prompt for gaps, and support analysis; people remain responsible for validating facts, exercising judgment, making decisions, approving scope changes, and acting on the results. The intended benefits are not guarantees that every step will be completed or that scope creep will never occur.

## The problem

Software work can lose context as it moves from user research to product planning and then to engineering. User evidence may not reach feature decisions; roadmaps can be mistaken for engineering plans; and product intent can be lost as implementation details are developed. Small teams may also have limited time or specialist capacity to keep every necessary step, decision, and handoff visible.

Agentic Toolkit's proposed direction is to organize reusable guidance into connected suites with explicit responsibilities and handoff documents. The aim is to reduce avoidable process overhead without skipping necessary work. Each stage should preserve the reasons for the work, distinguish evidence from assumptions, and make unresolved decisions visible.

## Product vision

The proposed lifecycle model has three connected responsibility stages:

1. **Product Discovery & Shaping** explores user needs, evidence, problems, use cases, and possible solutions, then prepares a high-level proposal.
2. **Product Management** evaluates proposals and shapes product goals, priorities, roadmap direction, target-version scope, and product-level feature briefs.
3. **Engineering** validates feasibility and technical implications, details the feature contracts and architecture, and plans, builds, tests, deploys, and operates the software.

These responsibility areas could be organized as suites in a future version, but no additional suites are currently maintained. The repository currently maintains the Engineering suite; see the [documentation index](../README.md) for current coverage.

These stages describe responsibilities, not required headcount or a mandatory sequence. One person may hold multiple responsibilities, and a team can use only the stages relevant to its decision. Keep decision ownership clear; use separate review when the risk or project requires independent review.

## Handoffs and document ownership

The proposed lifecycle model passes context forward without treating any handoff as automatic approval:

| Stage | Primary output | Next decision or handoff |
|---|---|---|
| Product Discovery & Shaping | Research plan and findings, opportunity framing, and a high-level proposal | Product Management decides whether and how to consider the opportunity |
| Product Management | Product goals, roadmap direction, target-version proposals, and product-level feature briefs | The product owner approves priorities and scope before Engineering takes approved work forward |
| Engineering | Validated technical design, detailed contracts and plans, implementation, and verification evidence | Engineering and product owners use the evidence for delivery and release decisions |

The proposal should identify intended users, the problem and supporting evidence, use cases, candidate solution, scope options, success measures, risks, assumptions, and open questions. Research activities must not be represented as completed unless findings are actually available.

Product-level feature briefs can describe user-visible outcomes, intended scope, exclusions, and acceptance examples, including behavior-driven scenarios where useful. These briefs are proposed product-facing artifacts, distinct from Engineering feature contracts, which describe detailed intended behavior, edge cases, and failure behavior. Acceptance criteria are observable conditions for judging an outcome; acceptance examples illustrate expected behavior and do not replace criteria unless explicitly adopted as criteria. Engineering remains responsible for validating technical feasibility and elaborating its contracts, implementation tasks, and verification.

Roadmaps, target versions, feature priorities, and release scope are proposals until approved by the responsible product owner. This repository does not currently maintain a product roadmap or release plan for these future suites.

## Shared guidance and technology selection

Some methods can be shared across suites while being applied at different levels. Architecture guidance, for example, could distinguish a conceptual solution in discovery, product capabilities and dependencies in planning, and validated technical design in Engineering. Shared guidance would not make a conceptual proposal an approved engineering architecture.

Engineering guidance may also benefit from separate catalogues for languages, frameworks and runtimes, and infrastructure or deployment platforms. Such catalogues should route to maintained guidance that matches the project's actual stack; they should not imply that every technology is supported. A project description such as a Vue frontend, Rust backend, containers, and Azure infrastructure defined with Bicep is an example of context an agent could use to select relevant guidance, not a claim that this repository currently provides all of it.

Containerization is a packaging and build concern, not a universal deployment model. Deployment, infrastructure as code, validation, security, and operations can vary by platform and should use explicit, relevant guidance. Shared baseline workflows can complement platform-specific guidance rather than replace it.

## Intended audience

- **Guidance maintainers** organize and improve reusable suite, agent, skill, and catalogue sources.
- **Product and research practitioners** use discovery and planning guidance to make evidence-informed proposals and product decisions.
- **Engineering practitioners** use engineering guidance to validate and deliver approved product work.
- **Readers and evaluators** assess the collection's intended scope and boundaries.

## Responsibilities and limits

- Agentic Toolkit provides written guidance and organization. The user and their agent client provide research access, tools, permissions, runtime behavior, and execution.
- The intended workflow uses agents under human oversight. People validate project facts, retain decision authority, and approve priorities, scope, and changes.
- Suite handoffs help preserve context; they do not automatically orchestrate agents, approve proposals, or enforce process.
- Guidance can help surface lifecycle gaps and prevent avoidable scope creep, but does not guarantee that every lifecycle step is completed or that scope remains unchanged.
- Research findings, product priorities, roadmaps, architectures, and release plans must be distinguished from assumptions, proposals, and implemented behavior.
- Product suites own product intent and decisions; Engineering owns technical validation and software delivery guidance.
- Shared guidance can be applied at different levels, but does not erase suite ownership or technical validation requirements.
- Client support, technology coverage, and runtime behavior must be established explicitly; a catalogue or source definition alone does not prove support.

## Non-goals

- Replacing an agent client or providing an agent runtime, workflow engine, or automatic project orchestrator.
- Replacing people, teams, or their judgment and decision authority.
- Claiming that proposed suites, agents, catalogues, or product handoffs are already maintained or available.
- Treating proposals, roadmaps, feature briefs, or conceptual architecture as approved commitments or validated engineering designs.
- Claiming uniform deployment, security, testing, or operational practices across languages, frameworks, cloud providers, or infrastructure tools.
- Claiming identical discovery, tool use, permissions, or behavior across clients and models.

## Related documents

- [Current project overview](../project-overview.md): repository purpose, current scope, and compatibility limits.
- [Repository README](../../README.md): current collection maintenance, supported installation, validation, and repository boundaries.
- [Documentation index](../README.md): maintained suite guides and navigation.
- [Using Agentic Toolkit effectively](../guides/using-agentic-toolkit-effectively.md): a guide to using the proposed future lifecycle model with human oversight.
- [Engineering suite guide](../suites/engineering.md): current Engineering roles, skills, and handoffs.
- [Copilot installation guide](../installation.md): current installation behavior and limitations.
