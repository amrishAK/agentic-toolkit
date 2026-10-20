---
name: project-rules-workflow
description: "Use for profile-first repository setup, standardization, updates, and audits: inspect, prefill a YAML repository profile, interview about repository and application types, build systems and CI/CD, confirm, save the profile, create or update README, and validate. Covers optional agent guidance, licensing, and ignore safeguards."
---

# Repository setup and project rules workflow

## When to use

Use this skill to establish or maintain a repository profile, README, and agreed repository guidance, or to audit their consistency.

## Scope and boundaries

The default setup outcome is a confirmed repository profile and a useful README. Other baseline files are conditional on project requirements, usefulness, and approval, not a directory-creation checklist. Preserve established decisions and locations; use [project conventions](project-conventions.md) as adaptable defaults.

Setup follows **inspect -> prefill profile -> interview gaps -> confirm -> save profile and write README -> validate**. Audits are findings-only. Targeted updates use only the relevant steps and do not restart the full interview or require a new profile.

The profile is descriptive, not executable configuration, a policy override, permission, or proof of verification. Production code, tests, build/CI/CD configuration, dependencies, file migrations, and publishing require separate explicit authorization.

## Procedure

### 1. Inspect

- Read applicable repository instructions first, then the existing profile if any, README, relevant docs, manifests, CI/CD configuration, and established test/build entry points. Inspect representative source only as needed to understand deliverables.
- Identify repository purpose and layout, application types, languages/toolchains, build systems, CI, CD, and intended platforms. Distinguish configuration that exists from future wishes and successful execution.
- Inspect licensing, ignore rules, tracked/generated files, and other baseline items only as relevant to the request. Do not read or reproduce secret contents.
- Check paths and command definitions from actual files. Code is evidence of current behavior, not automatically the intended contract. Surface contradictions between instructions, profile, docs, and configuration rather than silently choosing one.

### 2. Prefill the profile

- Follow the [repository profile format and example](references/project-rules-workflow-repository-profile.md). Reuse an established equivalent; otherwise propose root `project-profile.yaml`.
- Draft supported facts from repository evidence. Keep unknown information explicit and distinguish absent tools from unknown or not-applicable ones. Do not substitute a desired build or pipeline for the current setup.
- Keep the draft in the conversation until approved. Do not write a scratch profile into the repository.
- For targeted updates, inspect only affected fields and authorities. Preserve unrelated fields and established formats; do not silently migrate a profile.

### 3. Interview gaps

- Use the [setup interview](references/project-rules-workflow-setup-interview.md) as a question bank, not a mandatory questionnaire.
- Confirm purpose, audience, problem, and stage for initial setup. Offer an evidence-based draft; do not require the user to retype facts or reconfirm settled answers individually.
- Ask one focused question at a time using an interactive question tool when available. Resolve only missing, ambiguous, conflicting, or intentional choices needed for the requested scope.
- Separate current CI/CD, build systems, and deliverables from requested future infrastructure. If user confirmation is unavailable, return the draft and open questions without writing.
- Use [documentation selection](../documentation/documentation-selection-workflow.md) for the README and any additional documents. Select relevant rules and owners rather than proposing every catalogue item.

### 4. Confirm

- Present the completed profile, proposed README content/changes, and exact file actions. Include retained decisions, deliberate deviations, unknowns, and deferred gaps.
- Explain any additional baseline files or structure changes with purpose and evidence using the [structure proposal](references/project-rules-workflow-setup-interview.md#structure-proposal-and-refinement). Do not expand into a full repository redesign.
- Obtain approval before setup/standardization writes. An explicit, sufficiently clear targeted update already authorizes that bounded scope; ask again only if a material decision or scope change arises.

### 5. Save the profile and write the README

- Save only confirmed information in the profile, with explicit unresolved values where the user accepts deferral. Create or update the README from confirmed project purpose and verified repository evidence, not by dumping YAML into Markdown.
- Follow the [README guidance](../documentation/references/documentation/docs-layout.md#readme-and-documentation-index): purpose, status, prerequisites, first supported workflow, development commands, deeper docs, and confirmed licensing where applicable. Preserve useful existing content; do not rewrite unrelated sections.
- Link to real configuration and authoritative docs instead of copying mutable details. Report missing or unverified commands without inventing usage or claiming setup works.
- Create other baseline files only within agreed scope. Use the routing and safeguards below. Record adopted conventions in repository-owned guidance, not links to a personal skill installation.

### 6. Validate and report

- Parse the YAML with an available safe parser, reject duplicate keys, and check the profile's [field meanings](references/project-rules-workflow-repository-profile.md#field-rules). If parsing is unavailable, explicitly report syntax as unverified; do not install tools without approval.
- Compare changed profile fields and README claims with manifests, workflows, and linked authorities. Check paths, relative links/anchors, documented commands, and relevant instruction globs. Distinguish intended platform support from executed evidence.
- Check customization frontmatter where applicable: names follow the source or installed layout being maintained, descriptions support discovery, and scoped globs are specific.
- Run the smallest safe relevant checks when feasible. Inspect the full diff and new/untracked files, preserving unrelated work.
- Report changed files, exact checks/results, contradictions, and unresolved/deferred items. Account for applicable baseline gaps without claiming the whole repository is complete.

### Choosing the right place for each rule

Use the [repository placement map](references/project-conventions-architecture-and-scope.md#repository-layout) for broader layout decisions. Client-specific paths below apply only to supported hosts.

| Content | Location |
|---|---|
| Structured project characteristics | Existing profile location, otherwise proposed root `project-profile.yaml` |
| Human-facing introduction and first workflow | `README.md` |
| Agent navigation and essential project constraints | `AGENTS.md`, using the [outline](references/project-rules-workflow-agents-md-outline.md) |
| Narrow folder/file-type instructions | Applicable scoped instructions, such as `.github/instructions/<topic>.instructions.md` |
| Recurring project procedures | Established project skills; create only when ordinary guidance is insufficient |
| Detailed explanations, contracts, plans, status | Existing canonical docs, selected through the [documentation matrix](../documentation/references/documentation-matrix.md) |
| Licensing and ignored output | Existing license files and `.gitignore`, with safeguards below |

- Preserve existing instruction ownership. Resolve conflicting copies before consolidating; do not remove rules that lack another authority. Keep `AGENTS.md` navigation-first, linking detailed scope, contracts, and commands.
- Use nested guides for independent subprojects where useful. Keep scoped globs narrow and link directory guides rather than copying them.
- Treat feature tracking as the default; omit it only for an explicit, confirmed project-specific opt-out. Keep unrelated stage-dependent baseline policies conditional, proposing them only when relevant. Never create other baseline items merely because a convention lists them.

### License and ignore-file safeguards

- Inspect existing licenses, notices, README statements, and package metadata. Preserve licensing and third-party notices. Confirm unclear open-source/private intent and ask the user to choose or confirm missing, replacement, or conflicting licensing and rights-holder details; never invent ownership or silently relicense.
- Use exact authoritative license text and identifiers, not paraphrases. Report metadata mismatches; manifest edits need explicit authorization. Do not claim legal advice or grant rights.
- Derive `.gitignore` rules from actual generated/local output. Preserve useful rules and exceptions; retain intended source, fixtures, lockfiles, shared settings, and sanitized templates.
- Check representative ignored and retained paths with `git check-ignore -v --no-index` or equivalent and inspect status for newly hidden files. Never incidentally delete/untrack files or rewrite history; report tracked sensitive/generated content without exposing secrets.

### Audit and follow-up

- Compare the profile with configuration and README claims. Check stale paths/commands, conflicting or duplicated rules, unsupported claims, plans presented as implemented, and applicable license/ignore gaps.
- Report convention differences as deliberate or unexplained, not automatically defects. Assess applicable [open-source baseline](references/project-conventions-oss-baseline.md) gaps by stage while preserving project-specific requirements.
- A missing profile is not a broken build or automatic permission to create one; recommend it where useful. Do not start an interview or persist a report during a findings-only audit.
- Explicit fix selections authorize only the selected recommendations. Follow the active role's review and delegation boundaries; selection does not authorize unrelated baseline work, infrastructure, or delivery.
