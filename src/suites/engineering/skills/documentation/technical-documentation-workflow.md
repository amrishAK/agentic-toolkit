---
name: technical-documentation-workflow
description: "Use when reviewing, writing, updating, or maintaining technical documentation: README, architecture, setup, onboarding, user/developer guides, integration, runbooks, troubleshooting, migration notes, and data flow. Covers evidence, audience, concise writing, docs-as-code validation, and maintenance."
---

# Technical documentation workflow

Apply within the authorized task scope. This skill does not authorize edits, publishing, infrastructure changes, or operational commands.

## 1. Establish scope and audience

- Identify review-only, planning, writing, or combined work; review-only requests must not modify files or create tracking artifacts.
- Determine audience, purpose, document location, and relevant product/release version. Infer these from context when clear; ask only for material unresolved decisions.
- Read project instructions, existing document structure, and relevant source/configuration. Trace only the evidence needed for the requested topic.
- Preserve unrelated edits and useful content. Use established documentation locations and canonical sources, including non-Markdown formats where applicable.
- When creating new docs or restructuring and the project has no established layout, follow the [docs layout requirements](./references/documentation-requirements-docs-layout.md).
- Before writing, reviewing, or updating a document, load `documentation-requirements` or read [the document catalogue and rules](./documentation-requirements.md). It owns what each document means, its location, owner, and rules; read the matching rules, assess existing content or outline a new document against them, and validate the result against the same rules. Preserve established project formats and do not duplicate templates here.
- Use its [document-routing map](./documentation-requirements.md#document-routing-and-maintenance-ownership) to distinguish product intent, detailed feature contracts, implementation evidence and independent review. Writing prose does not authorize changing another topic's agreed decisions.

## 2. Establish evidence

- Verify claims against relevant implementation, tests, manifests, build targets, CI, configuration, release artifacts, and user-supplied contracts.
- Separate intended behavior, observed behavior, and version-specific support. A test or current implementation can also be wrong; report contradictions rather than silently changing the contract.
- Never invent APIs, paths, commands, environment variables, historical decisions, alternatives considered, support promises, or performance/security guarantees.
- Label material inferences and proposed/unverified commands; list blocking gaps explicitly. Do not bury operational uncertainty in polished prose.
- Consult authoritative version-matched external documentation when needed and available. Do not send private code/data to external services or copy credentials into examples.

## 3. Structure and write

- Put the purpose and most useful action or decision first. Follow the selected document-type requirements, adapting suggested headings to the project. The [technical document outlines](./references/technical-documentation-workflow-document-outlines.md) supply additional guide-specific prompts, not mandatory sections for every document.
- Use concrete nouns/verbs, short paragraphs, meaningful headings, consistent terminology, and concise technical language. Preserve the author's framing without retaining inaccuracies.
- Organize procedures as ordered steps with prerequisites, working directory, platform/shell, expected outcomes, and relevant failure/recovery steps.
- Align build/test/run examples with actual tooling. Prefer the project's [shared entry points](../project-standards/references/project-conventions-entry-points.md) used by local development and CI; retain native commands where they are the documented interface.
- Keep examples minimal but complete enough to follow. Distinguish literal commands from placeholders, redact secrets, and flag destructive effects before the command.
- Describe architecture using responsibilities, interfaces, lifecycle, constraints, tradeoffs, and evidenced failure paths; distinguish implemented design from proposals.
- For data flow, trace sources, transformations, sinks, state changes, side effects, ordering, async boundaries, retries, persistence, observability, and trust boundaries where relevant.
- Use tables or diagrams only when they improve understanding. Do not require a diagramming dependency; preserve readable text alternatives and follow existing accessibility conventions.
- Keep README concise and link deeper guidance. Prefer one canonical explanation and relative links over duplicated instructions; follow existing documentation tooling for navigation.

## 4. Review or update

- Review accuracy and operational risk first, then meaningful coverage, structure, clarity, consistency, and maintenance.
- Report actionable findings with precise references, affected audience/scenario, impact, and focused recommendations. Distinguish defects from editorial preferences.
- Apply authorized changes in place; restructure only when it improves the requested outcome. Do not create extra guides, templates, or tracking notes merely to fill a checklist.
- Update directly affected links/navigation and duplicated guidance where necessary. Do not rewrite unrelated documents or modify generated outputs instead of their maintained source.
- Remove filler, repeated claims, unnecessary headings, and unsupported certainty. Do not force every paragraph to repeat facts; useful context and transitions may remain.

## 5. Validate and report

- Identify existing docs lint/build/link checks and run the narrowest relevant selection when available. Use existing dependencies; do not add tooling just to satisfy a checklist.
- Check affected local links, generated heading anchors, paths, navigation, and configuration against the actual documentation renderer/tooling. Remote links may be inaccessible; report that rather than claiming verification.
- Validate changed runnable examples with existing snippet/doctest/test mechanisms when safe and feasible. Do not execute destructive, deployment, production, or shared-service procedures as routine verification.
- A command found in configuration is inspected, not executed. A successful build is not proof that every guide works; report exact checks, skipped examples, unavailable prerequisites, and unresolved contradictions.
- Review the diff for unintended changes, leaked secrets, unsupported claims, broken references, and voice drift. Fix failures introduced by the edits; report unrelated failures.
- Finish with changed documents or review findings, exact validation results, and remaining limitations. Never claim tested support or operational success without evidence.
