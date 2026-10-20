# Setup interview

Use this question bank during the [profile-first setup flow](../project-rules-workflow.md). Inspect first and prefill the [repository profile](project-rules-workflow-repository-profile.md); ask only about unresolved facts or choices. Do not run the entire interview for an audit or targeted update.

## How to ask

1. Show detected answers with their evidence. Offer them as defaults, not assumptions the user must accept.
2. Ask one focused question at a time, using an interactive question tool when available. Skip settled questions and irrelevant topics.
3. For initial setup, confirm a short project summary covering purpose, audience, problem, and stage. An accurate existing summary may be confirmed with the complete profile; do not demand a new essay.
4. Distinguish unknown, absent/disabled, and not applicable. A wanted build system or pipeline is future intent, not an existing system.
5. If a material conflict remains, ask the decision owner. Without access to user confirmation, return the draft and open questions without writing.

## Profile questions

Use these in a useful order for the detected project, not as a fixed script.

| Topic | Focused question when evidence is insufficient | Profile fields |
|---|---|---|
| Purpose | What does this project do, for whom, and what problem does it solve? | `project.summary`, `project.audience` |
| Stage | Is this a prototype, pre-release, or released project? | `project.stage` |
| Repository | Is this software, documentation, tooling, a template, or a mixed repository? | `repository.type` |
| Layout | Is this a single project or a monorepo with independently maintained components? | `repository.layout` |
| Deliverables | What does each component deliver: executable, library, web app, service, or another artifact? | `applications` with type, optional interface, and path |
| Languages | Which languages/toolchains are maintained here? | `languages`, authoritative manifest/guide links |
| Build | What build systems are in use, and is there a shared developer entry point? | `build` |
| CI | Is CI configured? Which provider or providers run it? | `ci` |
| CD | Is delivery/deployment automated? Which providers and non-sensitive targets are established? | `cd` |
| Platforms | Which operating systems or runtimes are intended to be supported? | `platforms.intended` |
| Authorities | Which existing documents/configuration own setup, architecture, and support details? | `authorities` |

Ask CI and CD separately. CI is automated validation; CD is automated delivery/deployment, including package publication where established. Neither records a successful run or gives permission to implement automation.

## Additional questions only when relevant

- **README:** What first supported user workflow should it explain? Verify prerequisites, commands, and expected results from the repository.
- **Agent guidance:** Is creating/updating `AGENTS.md` or scoped guidance useful and in scope? Identify constraints and authoritative documents rather than inventing policies.
- **License and ignore rules:** Resolve ambiguous licensing/ownership and intended tracked/generated content using the [safeguards](../project-rules-workflow.md#license-and-ignore-file-safeguards).
- **Tracking and policies:** Feature tracking is the default; include it unless an explicit, confirmed project-specific opt-out applies. Ask about unrelated stage-dependent policies, such as contribution/security policy or release documents, only when relevant to project stage and scope. Use [documentation selection](../../documentation/documentation-selection-workflow.md) and the responsible decision owners. Do not manufacture contacts, commitments, or release targets.
- **Architecture and tests:** Locate existing boundaries, non-goals, test tiers, and prerequisites needed for accurate documentation. Missing infrastructure is a gap, not permission to create it.

## Structure proposal and refinement

The default proposal is the profile and README. Expand it only for useful or project-required baseline items. Keep the proposal in the conversation unless a persisted document is requested.

| Path / item | Purpose | Action | Evidence / remaining decision |
|---|---|---|---|
| Established profile path, otherwise proposed `project-profile.yaml` | Confirmed technical profile | Create/update only after approval | Detected facts, confirmed answers, explicit unknowns |
| `README.md` | Human-facing introduction and first supported workflow | Create or focused update | Existing content and verified setup/usage |
| Additional applicable file | Explain why it is needed | Retain, create/update, defer, or not applicable | Project requirement, evidence, and any approval needed |

Explain alternatives before asking the user to choose. Use the [repository placement map](project-conventions-architecture-and-scope.md#repository-layout) only when layout decisions arise; do not propose every category or migrate files incidentally.

## Confirm and finish

- Show the completed profile, README outline or bounded changes, exact file actions, preserved decisions, and deferred gaps. Obtain setup approval before writing; resolve any later material scope changes separately.
- Save the profile and create/update the README using the [workflow](../project-rules-workflow.md#5-save-the-profile-and-write-the-readme). Apply optional baseline changes only within approved scope.
- Validate and report using the workflow. Unknowns and unverified commands remain explicit; a completed interview is not evidence that the build, CI/CD, or claimed platforms work.
