# Known-issues documents

## Purpose and ownership

Use a known-issues document to record confirmed user- or operator-impacting defects and limitations. The default location is `docs/status/known-issues.md`; preserve an established path. The project’s documented issue owner maintains it when an issue is confirmed, its scope or workaround changes, or its resolution is verified.

Do not use this document for speculative risks, unapproved feature ideas, general technical debt, or unverified reports.

## Structure

```markdown
# Known issues

Updated: YYYY-MM-DD

| ID | Affected version/scope | Confirmed behavior and impact | Evidence | Workaround | State |
|---|---|---|---|---|---|
| KI-1 | <Verified scope> | <Observed behavior and user impact> | <Test, reproduction, or canonical reference> | <Verified workaround or none known> | Open |
```

## What belongs here

- Include only confirmed symptoms or limitations, affected versions/configurations, practical impact, and evidence.
- Separate observed behavior from suspected cause.
- A missing feature is not automatically a defect. Record intended future work on the roadmap; record accepted design trade-offs in the decision log; record maintainability costs in the technical-debt register.
- Use the project’s status vocabulary. Do not mark an issue resolved until the relevant fix is verified. Remove resolved entries unless a lasting historical record is needed; release notes may retain version-specific limitations.
- Do not copy feature implementation state or release readiness into this file.

## Validation

Verify the reported behavior and affected scope against evidence. Link to the canonical issue, test, reproduction, or limitation statement. Do not claim a workaround is verified unless it has been checked.
