# Project tracking

## Purpose and requirement

Anyone, human or agent, should be able to tell in a minute what the project is, what works today, and what is still to come. This convention defines a concise project summary and the default feature tracker, while allowing confirmed project-specific opt-outs.

## Structure

### Project summary (required)

The summary is three to five sentences covering what the project is, who it is for, the problem it solves, and its current stage (for example "pre-v1, API unstable"). It appears at the top of `README.md` and is restated in one or two sentences at the top of `AGENTS.md`.

Keep both in step. If the summary changes, update both in the same change.

### Feature tracker (default; project-specific opt-out)

By default, projects use one file, `docs/status/features.md`, to list features and their states. It is the single source of truth for what is implemented; the README status section and `AGENTS.md` link to it rather than copying it. A project may explicitly opt out through a confirmed project-specific rule, which takes precedence over this cross-project default.

Assess omissions from project evidence: an explicit, confirmed rule in `AGENTS.md` or other authoritative project guidance establishes an intentional opt-out; a missing tracker alone does not. During setup, confirm whether tracking applies before drafting, creating, updating, or linking the tracker. Do not create a tracker or links when the confirmed project scope excludes one.

## What belongs here

The project summary communicates purpose, audience, problem, and stage. The feature tracker records feature state, target, and concise notes or links:

```markdown
# Features

Updated: YYYY-MM-DD

| Feature | State | Target | Notes / links |
|---|---|---|---|
| Typed query binding | Done | v0.1 | docs/architecture/query-binding.md |
| SQLite backend | In progress | v0.1 | Missing: transactions |
| Connection pooling | Planned | v1.0 | docs/proposals/connection-pooling.md |
| Async API | Not planned | — | Non-goal; see README |
```

- **States:** `Planned`, `In progress`, `Done`, `Not planned`. Use `Not planned` for rejected ideas and non-goals, so they are not proposed again.
- **Target:** the version or milestone the feature belongs to, or `—`.
- **Links:** `Done` features link to their architecture doc or tests; `Planned` features with a design link to their proposal.
- Update the tracker in the same change that starts, finishes or drops a feature. A feature marked `Done` without working code and tests is a defect.
- Known bugs and limitations stay in `docs/status/known-issues.md`, not in the feature table.

## How it resolves tracking questions

- Feature state records what is implemented; feature references own detailed contracts and open design questions.
- Roadmap records high-level direction. Release documents own milestone scope, gates, progress and candidate evidence; an implemented feature is not itself a passed release gate.
- Product overview owns vision, intended usage and boundaries, not mutable status tables or unresolved decisions.
- Use the [roadmap guidance](roadmap-docs.md), [known-issues guidance](known-issues-docs.md), [decision-log guidance](decision-log.md), [technical-debt guidance](technical-debt-docs.md), [product overview outline](product-overview.md), and [release document outline](release-docs.md) for those document types. Update each affected owner in the same change without copying its mutable tables into other documents.

## Review and validation

- Check that the README summary has three to five sentences covering purpose, audience, problem, and current stage, and that the one- or two-sentence `AGENTS.md` summary agrees without introducing a different scope or stage.
- For an adopted tracker, verify each row uses an allowed state and an appropriate target; compare `In progress` and `Done` with current implementation and test evidence, and confirm `Planned` has a design link and `Not planned` reflects an adopted rejection or non-goal. Refresh the `Updated` date when tracker content changes, and ensure links still resolve and support the recorded state.
- Compare implementation states with current code and tests, not with feature-document decision status or release-gate status. Recheck evidence when implementation or linked tests change; `Done` requires working code and tests.
- Treat a missing tracker as an omission unless authoritative project guidance explicitly confirms an opt-out. Do not create or link one when that confirmed opt-out applies.
- Check local links and heading fragments in the summary and tracker.
