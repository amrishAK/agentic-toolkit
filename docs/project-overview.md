# Project overview

Agentic Toolkit aims to make useful agent guidance easier to maintain, reuse, and improve. Instead of keeping roles and workflows in scattered client-specific copies, maintainers develop them as linked, reviewable sources that people can browse or deliver to an agent client.

This is a product vision, not a promise of cross-client support. The repository is pre-release, maintains a Software Product Development suite with product-management and engineer packages that include their respective reviewers, and has a Make-based installer for Copilot layouts. Other clients are not currently supported. See the [README](../README.md) for current scope and compatibility.

## The problem

Agent guidance is often written into personal client configurations. As collections grow, copies drift, useful improvements are hard to share, and role instructions become tangled with workflows and client-specific details. People then have to rediscover, adapt, and maintain similar guidance in multiple places.

## Intended capabilities

- **A shared source to maintain.** Keep agent roles, workflows, and their supporting references together as reviewable source material.
- **Guidance that composes.** Separate role responsibilities from reusable methods, so people can combine the right expertise and workflow for a task without loading an entire collection.
- **Clear routes through the collection.** Organize guidance so users can start from a task or role and find the relevant skills and supporting material.
- **A path from source to use.** Make it practical to select and install guidance into an agent client, while keeping the source as the place to make and review changes.
- **Portability as a direction.** Over time, client-specific adapters could make the same maintained guidance usable in more clients. Each client would need explicit support; source organization alone does not provide compatibility.

## Agent design philosophy

The agents are designed as bounded specialist roles that people can select for a task, not as autonomous personas expected to own an entire project. Each role should make its outcome, responsibilities, and limits clear. Roles are reusable guidance categories, not a recommendation for a particular team structure or headcount.

The design follows several principles:

- **Define responsibility before procedure.** Agent definitions say what a role owns, where its responsibility stops, and when it should hand work to another role. This keeps adjacent responsibilities distinct—for example, product planning stays separate from detailed feature-contract design and implementation.
- **Keep methods reusable.** Skills describe task methods that can be shared across roles; supporting references hold focused detail. Agents link to the guidance they need instead of duplicating whole workflows. Selection should bring in only relevant additional guidance.
- **Make review distinct where it matters.** The collection includes independent reviewer roles for product plans, feature contracts, and engineering changes. Review boundaries are explicit: a reviewer evaluates work without taking over its authoring, and any selected remediation follows its own authorization and handoff rules.
- **Ground work in evidence and preserve human decisions.** Roles are expected to distinguish evidence from assumptions and proposals. Product priorities, scope, approvals, and other decisions remain with the responsible person; a recommendation or handoff does not itself approve or execute an action.
- **Coordinate through clear handoffs, not assumed automation.** A handoff carries context and identifies a requested next decision or action. It does not mean that another agent will be invoked automatically, that work is approved, or that a process must always run end to end.
- **Scale guidance to the task.** Shared task framing and specialist workflows help users choose an appropriate method, but roles do not require every workflow for every request. Select enough guidance to do the work correctly without turning a simple task into unnecessary process.

These principles describe how the maintained roles and workflows are intended to fit together. For the actual role boundaries and available handoffs, see the [Software Product Development suite guide](suites/software-product-development.md) and the maintained [agent definitions](../src/agents/). The [definition-authoring guide](reference/definition-authoring.md) explains how responsibilities are divided between agents, skills, references, templates, and catalogues.

## Intended user workflow

1. Maintainers improve roles, workflows, and supporting material in the shared source.
2. Changes are reviewed there, so improvements can be reused rather than maintained only in a personal installation.
3. Practitioners find the guidance that fits their task and use it directly or install it into a supported client.
4. When guidance needs improvement, the change is made in the source and shared with its users.

Today, users can browse the sources or install them into supported Copilot layouts. The [installation guide](installation.md) describes that current workflow.

## Usage modes and intended audience

- **Maintainers** organize and improve reusable guidance.
- **Software product practitioners** use roles and workflows for product planning, design, implementation, review, testing, and documentation.
- **Readers and evaluators** browse the sources to understand the collection without installing it.

## Architecture direction and data flow

The intended model is to maintain guidance once, select the relevant parts for a task, and deliver them in a form understood by a supported client:

```text
maintained guidance -> task-relevant selection -> client-specific delivery -> practitioner use
```

Sources contain role definitions, reusable skills, and supporting material. Selection follows the collection's organization and links. Client-specific delivery is a separate concern: it must account for that client's layout and definition format rather than assuming that one layout works everywhere.

The current installer implements this model for Copilot only. This high-level description is product direction, not a specification of installer behavior; consult the [installation guide](installation.md) for current details and limits.

## Responsibilities and limits

- The collection provides written guidance and organization. The client and user provide runtime discovery, tools, permissions, and execution.
- Role handoffs describe ways to coordinate work; they do not automatically orchestrate agents.
- Client support must be explicit. Preserving source text does not ensure that a client discovers, interprets, or behaves according to it.
- The Software Product Development suite covers product planning, engineering, and quality through responsibility packages. Discovery/research, product-level feature-brief guidance, other suites, and additional client support remain possible directions, not current offerings.

## Non-goals

- Replacing an agent client or providing an agent runtime, orchestrator, or execution engine.
- Treating a generated client installation as the authoritative place to maintain guidance.
- Claiming that the same guidance behaves identically across clients or models.
- Claiming that future suites, client adapters, or cross-client compatibility are already available.

## Related documents

- [README](../README.md): current repository scope, compatibility, and maintenance boundaries.
- [Definition authoring](reference/definition-authoring.md): source ownership and requirements for agent and skill guidance.
- [Copilot installation guide](installation.md): supported installation workflow and its limitations.
- [Documentation index](README.md): available suite guides and collection navigation.
- [Software Product Development suite guide](suites/software-product-development.md): current packages, roles, skill categories, and handoffs.
