# Product overview outline

## Purpose and requirement

Use a product overview when readers need a coherent explanation of the problem a product addresses, its intended use, who it serves, how its major usage modes differ, and where its responsibilities end. The default location is `docs/project-overview.md`; preserve established project locations.

Write the overview as an orientation to the product, not as a feature inventory or implementation manual. Make its status explicit near the start: distinguish current capabilities from product vision, and link to the canonical feature tracker and roadmap when they exist. Mark envisioned workflows, architecture, and examples as intended or illustrative rather than available or committed.

## Structure

Use the following as a model, adapting or omitting sections when they do not serve the product or its audience:

```markdown
# Project overview

<Short positioning statement: what the product is intended to make possible,
who it is for, and its central boundary.>

<Summarize the usage modes or primary workflow. State who retains surrounding
responsibilities.>

> **Product vision / Current product:** <Clarify whether this describes an
> intended direction or current usage. Link to the feature tracker for
> implementation state and the roadmap for high-level direction, if adopted.>

## The problem

<Describe the audience's problem and the product's intended approach.>

## What <product> is designed to do

<Summarize intended capabilities, define central concepts, and distinguish
product goals from proven claims.>

## How you would use it

<Describe the intended end-to-end workflow as ordered steps. Add a clearly
labeled illustrative example only when it makes the workflow easier to
understand; do not present it as runnable instructions.>

## Usage modes

<When there are multiple modes, compare how each is used, who it fits, and
meaningful differences such as boundaries, deployment, or lifecycle. For a
single mode, explain its intended context without forcing a comparison.>

## Is <product> for you?

<Describe suitable use cases and cases where the product may not fit. State
important trust, deployment, or responsibility boundaries when relevant.>

## Architecture

<Explain the high-level intended design and data flow. Mark proposed or
visionary components as such; link to architecture documentation for
implemented design. A diagram and component/responsibility table may help
when they clarify the flow.>

## Responsibilities and limits

<State what the product owns, what remains with its users or operators, and
what it is not intended to do. Avoid turning boundaries into unsupported
security or operational guarantees.>

<Close with a concise synthesis and links to canonical documents for current
implementation state, detailed contracts, roadmap, and architecture.>
```

## What belongs here

Explain:

- the problem, intended value, and audience;
- the product's intended capabilities and a representative end-to-end workflow;
- distinct usage modes and their important differences, if applicable;
- suitable and unsuitable use cases;
- high-level architecture direction and responsibilities; and
- boundaries, limits, and non-goals that help readers choose and use the product appropriately.

Keep the overview readable as a single orientation. Use concise examples and diagrams only when they explain the intended experience or boundaries better than prose.

## How it resolves the reader's need

The overview helps a reader decide what the product is for, whether it fits their situation, how it is intended to be used, and which responsibilities remain outside it. It connects that product-level explanation to authoritative sources for implementation state, detailed contracts, and current architecture.

Do not put mutable implementation-state tables, release progress or acceptance gates, detailed feature contracts, operational procedures, or unresolved design backlogs here. Link to their canonical owners instead. Do not present product vision as current availability, a support promise, a security guarantee, or a release commitment.

## Validation

Confirm the opening explains the product and its audience; the workflow and usage modes are understandable and internally consistent; and responsibilities, limits, and non-goals are explicit where relevant. Ensure proposed behavior and illustrative examples are labeled, current-state claims match available evidence, and links resolve to the correct canonical documents without duplicating their changing content.
