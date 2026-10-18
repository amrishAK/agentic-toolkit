---
name: agent-output-standardization
description: "Standardize written agent output, including code reviews, findings, clarification questions, summaries, handoffs, and status updates. Use when formatting a response or when an agent needs a reusable output template."
---

# Agent Output Standardization

## When to use

Use this skill to standardize written agent output, including code reviews, findings, clarification questions, summaries, handoffs, and status updates, or when formatting a response or selecting a reusable output template.

## Scope and boundaries

Use the matching `agent-output-standardization-*` template in `./templates/` for the kind of response being written. Keep output easy to scan, direct, evidence-based, and no longer than the task needs.

## Procedure

1. Identify the output type: review, question, or general response.
2. Use the matching template as a structure, not as mandatory boilerplate. Omit empty sections and replace every placeholder.
3. Put the answer, verdict, or requested decision first. Use headings and lists only when they make the response clearer.
4. State evidence and distinguish observed facts from assumptions or uncertainty. Be explicit about work not done and checks not run.
5. End with a clear next action only when one is useful or requested.

### Numbered review findings and selected fixes

- Every actionable review finding has a unique sequential integer ID: `1`, `2`, `3`. Order by impact first; preserve IDs when explaining or applying that report. Never silently reuse an ID for a different issue.
- Include issue type, level, location, an explanation with evidence/trigger and impact, and a recommended solution. Suggested types include correctness, security, contract/API, architecture, testing, documentation, build/CI, performance, and convention/preference.
- Type and level are separate. Preserve the active workflow's severity vocabulary (for example Blocker/Major/Minor/Nit or Critical/High/Medium/Low); state the vocabulary where needed. Label recommendations and uncertainty, not just defects.
- Use the [review template](./templates/agent-output-standardization-review-report.md) for all in-role reviews, including documentation and test reviews. A mandatory security summary table keeps its required columns and uses the same IDs as the detailed findings.
- A review report or explanation alone never authorizes fixes. For explicit selections, follow [selected-fix handling](./change-delivery-workflow.md#fix-handoff).
- Personal workflow guidance never expands actual host permissions.

### Boundaries

- Follow the user's requested output format and any stricter task-specific or security-reporting contract over the templates.
- Do not imply an agent edited, tested, delegated, or verified something unless it actually did.
- Ask one focused question at a time. When an interactive question tool is available, use it instead of asking the user in plain response text.
- Preserve required review findings, severity labels, locations, and evidence; standardization must not hide or soften a finding.
- Do not force a template onto a trivial answer when a concise direct response is clearer.

### Templates

- Review: [review-report.md](./templates/agent-output-standardization-review-report.md)
- Clarification question: [clarification-question.md](./templates/agent-output-standardization-clarification-question.md)
- General response, summary, or handoff: [general-response.md](./templates/agent-output-standardization-general-response.md)
