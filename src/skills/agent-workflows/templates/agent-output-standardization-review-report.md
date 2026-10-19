# Review: [mode]

**Verdict:** [Ready / Ready with fixes / Not ready] for [the requested gate or purpose].
**Scope:** [reviewed documents/code and revision, diff, branch comparison, or candidate].

## Guidance and checks

- **Guidance:** [relevant project rules and skills loaded; note anything unavailable].
- **Checks:** [commands or external checks run and their results].

## Findings

List findings from highest to lowest impact, using consecutive integer IDs. Repeat this block for each finding:

### 1. [Short issue title]

- **Type:** [Correctness / Security / Contract/API / Architecture / Testing / Documentation / Build/CI / Performance / Convention/preference].
- **Level:** [The active workflow's severity or priority].
- **Location:** [Linked file and line, or precise non-file evidence].
- **Issue:** [What is wrong, the triggering condition, and supporting evidence].
- **Impact:** [Why it matters to users or the selected gate].
- **Recommended solution:** [Specific, bounded correction; identify material decisions still needed].
- **Validation:** [How to establish the correction, distinguishing proposed checks from executed results].

If there are no findings, say so explicitly.

## Not checked

- [Relevant platforms, configurations, external checks, or surfaces not covered; say "None" only when appropriate.]

Keep convention drift, preferences, and uncertain observations distinct from defects. Use a stricter format if the task or review contract requires one.

## Selected-fix handoff

When findings exist, state that `apply 1`, `apply 1,2`, or `apply all` selects corrections from this report. A reviewer configured for approved delegation launches editing subagents only after that selection, never edits directly, and re-reviews their results. Disclose unavailable/prohibited delegation instead of claiming execution. Do not offer apply commands when there are no actionable findings.
