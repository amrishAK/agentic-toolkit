---
name: security-review-workflow
description: "Use for authorized security review and threat modeling with a read-only assessment phase. Explicit apply selections may authorize bounded fixes via editing subagents. No direct edits, exploitation or active scanning."
---

# Read-only security review

## When to use

Use this skill for authorized security review and threat modeling with a read-only assessment phase.

## Scope and boundaries

This is a read-only assessment workflow. It does not authorize active probing or direct remediation.

## Procedure

### Scope and evidence

- Establish the authorized source revision/diff or system boundary, deployment assumptions and assets. Read project policies and relevant contracts.
- Read source/configuration and trace attacker-controlled inputs through trust boundaries to sensitive operations. Consider authentication/authorization, injection, filesystem/process access, unsafe memory/lifetimes, cryptography, sensitive data, dependency/configuration risks and resource exhaustion only where applicable.
- Use the [language-specific skill matrix](../../../../shared/skills/references/programming-language-matrix.md)'s **Code quality** guidance for relevant language-specific issues, including managed-runtime and serialization/reflection boundaries where applicable. Use [architecture guidance](../design-and-planning/architecture-workflow.md) for cross-component boundaries.
- Do not expose secret values or copy private material into external tools. Report location/type and necessary redacted evidence only.
- External documentation lookup must use public generic identifiers, not private code or internal details.

### Assess findings

- Verify the actual call path, attacker prerequisites, existing defenses and practical impact. Distinguish reachable vulnerabilities from hardening recommendations and unsupported hypotheses.
- Provide precise location, triggering conditions, trust-boundary violation, impact, confidence and a focused remediation recommendation. Avoid duplicate findings for one root cause.
- Use critical/high/medium/low based on demonstrated impact and exploitability. Label missing evidence and conditional assumptions; do not equate a suspicious API or advisory with an exploitable path.
- Static inspection is not a proof of exploitability or absence of vulnerabilities. Separate inspected evidence, supplied test results and checks not run.

### Boundaries and report

- Return scope, limitations and findings in the response. During assessment do not delegate edits. Never directly edit files, persist reports, execute commands, install scanners, send payloads, access credentials, change data or probe running systems.
- Suggest safe bounded validation for a separately authorized executor if runtime evidence is needed. Do not fabricate a reproduction result or use an unauthorized target.
- Follow [output guidance](../../../../shared/skills/agent-output-standardization.md), with a numbered summary table containing severity, file/line, vulnerability and confidence. Use the same sequential IDs in detailed findings, each with issue type, level, triggering evidence, impact, recommended remediation and proposed verification. Preserve stricter required security-table formats. If none are established, say so with scope and limitations.
- On explicit `apply 1`, `apply 1,2` or `apply all`, follow [selected-fix coordination](../../../../shared/skills/change-delivery-workflow.md#fix-handoff): validate selected IDs/scope and launch appropriate editing subagents when host capabilities permit. Never edit directly. Fix approval excludes active probing, shared-data changes and delivery actions.
- Await results, inspect changes and re-review affected security paths. Report each original ID with actual validation and limitations. If delegation is unavailable/prohibited, disclose the blocker and hand off without claiming execution.
