# Community documents and contribution templates

## Purpose and requirement

Use these outlines only when the project's stage and audience make the documents applicable. Confirm adopted policy, process, and contacts before writing. Suggested paths are defaults; preserve established files and formats.

## Contribution guide

### Purpose and requirement

Applicable when the project adopts a contribution process; the staged [open-source baseline](../../../../suites/engineering/skills/project-standards/references/project-conventions-oss-baseline.md) identifies when it is required. The default location is `CONTRIBUTING.md`.

### Structure and what belongs here

```markdown
# Contributing

## Ways to contribute
## Development setup
<Link to canonical setup/test guidance.>
## Change workflow
<Branch/PR expectations only where adopted; tests, docs, and status updates.>
## Commits and review
## Reporting bugs and proposing features
<Link security reports to the confirmed private security channel.>
```

### How it resolves the contributor's need

It explains the confirmed ways to contribute and the project's actual development and review process. Link to canonical setup, test, and security reporting guidance instead of repeating it or promising an unadopted process.

## Security policy

### Purpose and requirement

Use `SECURITY.md` when the project's stage requires a vulnerability reporting policy.

### Structure and what belongs here

```markdown
# Security policy

## Supported versions
<Confirmed scope/policy; do not equate latest version with support.>
## Reporting a vulnerability
<Confirmed private channel and information needed, with redaction guidance.>
## Response and disclosure
<Only commitments explicitly adopted by the maintainer.>
```

### How it resolves the reporter's need

It gives reporters a verified private channel and states only the supported-version scope and response/disclosure commitments the maintainers have adopted. Confirm maintained versions, private reporting channel, and response/disclosure commitments. Do not assume private reporting is enabled or invent an address, response time, or service level. If required policy/contact information is unresolved, defer publication rather than creating a usable-looking placeholder. A code of conduct is optional unless adopted; confirm its enforcement contacts and use a verified authoritative policy.

## Changelog

### Purpose and requirement

Applicable before the first public release; default location is `CHANGELOG.md`. Follow the project's adopted versioning policy and [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

### Structure and what belongs here

```markdown
# Changelog

<Versioning policy and link to the adopted changelog format.>

## Unreleased
### Added
### Changed
### Deprecated
### Removed
### Fixed
### Security
```

Use only populated categories. Released sections use the actual version/date and verified comparison links when available. Record user-visible changes and compatibility notes; do not fabricate release history or treat unreleased work as published.

### How it resolves the user's need

It lets users identify what changed between releases without treating development work as published or duplicating release acceptance evidence.

## GitHub issue and pull-request templates

### Purpose and requirement

Applicable when the project accepts GitHub contributions. Default locations are `.github/ISSUE_TEMPLATE/` and `.github/pull_request_template.md`. Follow the actual [GitHub template format](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/about-issue-and-pull-request-templates).

### What belongs here

- A bug template asks for summary, affected version/environment, minimal reproduction, expected/actual result, redacted diagnostics, and a link to private vulnerability reporting.
- A feature template asks for the problem/use case, desired outcome, scope/non-goals, alternatives, and relevant feature/roadmap links. Submission is not acceptance.
- A pull-request template asks for summary/reason, linked issue or contract, behavior/compatibility changes, actual tests and results, affected docs/status/release gates, and relevant checklist items.
- Keep checks relevant and allow an explained not-applicable response. Never precheck success, require nonexistent CI, or ask for credentials or private dumps.
- Markdown issue templates need valid GitHub frontmatter with a meaningful `name`, `about`, and blank or adopted `title`, `labels`, and `assignees` values. If YAML forms are used, validate their supported format rather than adding Markdown frontmatter.

Minimal Markdown issue-template skeleton; replace and adapt it for separate bug and feature templates:

```markdown
---
name: "<Bug report or feature request>"
about: "<What this template is for>"
title: ""
labels: ""
assignees: ""
---

## Summary
## Context
## Reproduction steps or proposed workflow
## Expected outcome
## Actual outcome or current limitation
## Environment and evidence
<Relevant version/platform and redacted diagnostics; no secrets.>
```

Feature templates should add scope/non-goals and alternatives where useful; do not require reproduction steps for a new capability.

### How it resolves the contributor's need

Templates collect the information needed to review reports and proposed changes while reflecting adopted policy. Keep checks relevant and allow an explained not-applicable response. Never precheck success, require nonexistent CI, or ask for credentials or private dumps.

Minimal pull-request template skeleton:

```markdown
## Summary and reason
## Related issue or contract
## Behavior and compatibility changes
## Validation
<Commands/scenarios actually run, outcomes, and checks not run with reasons.>
## Documentation and tracking
<Affected owners, or an explanation of why no update is needed.>
```

Add only relevant, unchecked checklist items for adopted requirements. Changelog or release-gate updates apply when a change affects those owners; do not require every pull request to update every document.

## Validation

Confirm repository hosting, review policy, labels/assignees, versioning, release history, links, syntax, and referenced policies match confirmed project facts. Do not enable remote features or workflows while creating templates.
