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
- [Copilot installation guide](installation.md): supported installation workflow and its limitations.
- [Documentation index](README.md): available suite guides and collection navigation.
- [Software Product Development suite guide](suites/software-product-development.md): current packages, roles, skill categories, and handoffs.
