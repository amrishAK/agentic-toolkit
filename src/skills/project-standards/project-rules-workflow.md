---
name: project-rules-workflow
description: "Use when setting up, standardizing, reviewing, or updating repository structure and guidance: questionnaire-based interviews, AGENTS.md, README, scoped instructions, project skills, feature tracking, LICENSE, and .gitignore. Covers baseline inventory, confirmed setup, license and ignore safeguards, convention drift, and validation."
---

# Repository setup and project rules workflow

## When to use

Use this skill to set up or audit repository structure and agent guidance.

## Scope and boundaries

Establish a useful repository structure and a reliable guide for any agent. Project guidance and its authorities live in the repository so they are versioned and shared. Cross-project defaults come from [project conventions](project-conventions.md); record adopted conventions locally because a repository cannot reference personal skills. Review-only requests are findings-only; setup and standardization use the confirmed interview scope.

For setup, follow **inspect → explain/propose → ask/refine → confirm → create essentials → validate/report**. Initial interview questions may collect context before a meaningful proposal is possible; they do not replace an explained structure proposal, refinement and final confirmation. Essentials are the applicable files confirmed during the interview, not every catalogue item or a fixed directory scaffold.

## Procedure

### 1. Gather evidence

- Inspect existing rule files first: `AGENTS.md`, `.github/copilot-instructions.md`, `.github/instructions/`, `.github/skills/`, `.github/agents/`, `CLAUDE.md`, and nested `AGENTS.md` files.
- Read the README, `docs/`, directory READMEs (such as `tests/`, `.github/`, or build folders), build manifests, CI workflows, test layout, and representative source modules.
- Inventory license files, notices, package license metadata, `.gitignore`, tracked files, generated output, local configuration, and existing release/contribution guidance. Do not read or reproduce secret contents.
- Assess each applicable baseline item as present, missing, inconsistent, or not established. Separate required project guidance from optional infrastructure; inspect existing authorities before proposing replacements.
- Load `documentation-selection-workflow` or read [the selection method](../documentation/documentation-selection-workflow.md) to access the shared matrix and assess essential and stage-dependent documents, their locations, owners, and rules. Reuse the selected shared rules and templates instead of inventing parallel formats.
- Confirm build, test, and lint commands from manifests, aliases, scripts, and CI. Run read-only or safe commands only when needed to confirm them.
- Check recent commit messages for the convention in use.
- Treat current code as evidence of present behaviour, not automatically the intended contract. When code and docs disagree, report the contradiction instead of choosing one silently.
- Do not invent commands, paths, conventions, or decisions. Ask one focused question when a material rule cannot be inferred.
- For initial setup or requested standardization, run the [setup interview](references/project-rules-workflow-setup-interview.md) after gathering evidence. Use the [repository-wide placement map](references/project-conventions-architecture-and-scope.md#repository-layout) to explain common items and propose a structure suited to the detected ecosystem. Show each relevant path's meaning/contents, existing/proposed/deferred state and rationale or applicable conditions before asking the user to choose; refine the proposal as answers arrive. Confirm the project summary, tracking applicability and feature states when relevant, exact files and structural changes, preserved opt-outs, and deferred gaps before writing. Create or update the tracker only when tracking applies and that scope is confirmed. Ask one question at a time whenever uncertain, including during implementation.

### 2. Choose the right place for each rule

The [repository-wide placement map](references/project-conventions-architecture-and-scope.md#repository-layout) covers code, tests, resources, tools and configuration. The table below routes guidance only; client-specific paths are options for supported hosts, not directories to create for every project.

| Content | Location |
|---|---|
| Rules that apply to most work | `AGENTS.md` at the repository root; use the [outline](references/project-rules-workflow-agents-md-outline.md) |
| Rules for specific folders or file types | `.github/instructions/<topic>.instructions.md` with a narrow `applyTo` glob |
| Repeatable multi-step project procedures | `.github/skills/<name>/SKILL.md` |
| Explanations, architecture, plans, status | `docs/`, following the [docs layout requirements](../documentation/references/documentation/docs-layout.md); link from rules |
| Project entry point and setup | `README.md`, linked to the project guide and authoritative docs |
| License and ignore policy | Existing license files (or `LICENSE`) and `.gitignore`, using the safeguards below |
| Contribution/security/changelog and issue/PR templates | Stage-appropriate policy docs and `.github/` templates from the document catalogue; confirm policy and contacts before writing |

- Prefer `AGENTS.md` over `.github/copilot-instructions.md`. If both exist, consolidate or make one defer to the other; never keep conflicting copies.
- Use nested `AGENTS.md` files only for independent subprojects, such as separate workspace members with their own commands.
- Avoid `applyTo: "**"`; it loads on every request. Use specific globs such as `src/db/**` or `tests/**`.
- Path-scoped instructions link to the matching directory README rather than repeating it.
- Create project skills or agents only for recurring procedures that `AGENTS.md` and path-scoped instructions cannot cover.

### 3. Apply conventions

- Record what the project actually does. Where it follows a [project convention](project-conventions.md), restate that convention briefly in the project's own rules.
- Where the project differs from a convention, write the project's actual rule and report the difference to the user. Do not migrate files, rename paths, or add tooling unless asked.
- For new projects, or when the user asks to adopt conventions, record the applicable, confirmed conventions in their repository-owned authorities and link them from the guide.
- After final confirmation, create or update the agreed essentials rather than stopping at recommendations: `AGENTS.md`, `README.md`, and applicable confirmed licensing, ignore rules and supporting documentation, using the safeguards below. Essentials do not mean every catalogue entry. Preserve existing decisions and opt-outs; report deferred items instead of filling gaps with placeholders.
- Implement only the confirmed documentation structure and baseline files with useful, evidence-based content. Report absent test tiers and infrastructure rather than creating empty directories, fictional commands, or unsupported guarantees.
- General setup does not authorize production code, tests, build/CI configuration, installing tools, publishing, or moving existing files. Obtain explicit authorization for those changes and otherwise report them as deferred.

#### License and ignore-file safeguards

- **License:** Inspect existing licenses, notices, README statements, and package metadata. Ask whether the project is intended to be open source when unclear; do not impose an open-source license on a private/proprietary project. Preserve existing licensing and third-party notices. Ask the user to choose or confirm a missing, replacement, conflicting, or ambiguous license and any required rights-holder details; never invent ownership or silently relicense.
- Use the exact authoritative text for the confirmed license and its identifier, not a paraphrase. Verify project references and metadata agree; manifest edits require explicit authorization, otherwise report the mismatch. Do not claim legal advice or grant rights on the user's behalf.
- **Ignore rules:** Derive focused `.gitignore` patterns from the actual tools and repository layout. Preserve useful existing rules and exceptions. Check lockfile and shared-editor-config conventions rather than blanket-ignoring them; keep intended source, fixtures, examples, and configuration templates visible.
- Validate representative ignored and retained paths with `git check-ignore -v --no-index` or equivalent, and inspect status for newly hidden intended files. An ignore rule does not untrack committed files or remove secrets from history. Never run `git rm --cached`, delete files, or rewrite history as an incidental fix; report tracked sensitive/generated files without exposing secret contents.

### 4. Write enforceable rules

- Make root `AGENTS.md` a navigation-first entry point, not a scope or architecture handbook. Link the authoritative scope, non-goals, architecture, and public-contract documents rather than reproducing their rules. Keep area-specific enforceable constraints in their owning guidance.
- Cover, where relevant:
  - the project summary and, when feature tracking is confirmed as applicable, a link to the feature tracker (`docs/status/features.md`);
  - links to scope/non-goals and architecture/public-contract authorities, with when to consult them;
  - where source, unit tests (including inline tests), integration tests, E2E tests, fixtures, test infrastructure, benchmarks and examples live, where established;
  - release plans, acceptance gates and candidate evidence, separately from feature state and high-level roadmap;
  - the shared entry-point commands for each test tier, which tiers need infrastructure or serial runs, and known platform limits;
  - where docs live, and the rule that status files are updated in the same change;
  - the commit convention;
  - paths and operations agents must not touch without approval.
- Keep `AGENTS.md` short. Move detail into path-scoped instructions, skills, or linked docs.
- Use a compact `Path | Purpose / authority | Consult when` map with relative Markdown links. Route agents to task-relevant context rather than requiring every document on every task. Report missing test tiers, benchmark harnesses, or owning documents instead of inventing them; distinguish planned gates from existing runners.
- When removing duplicated scope or architecture rules, preserve their authority elsewhere. If a constraint exists only in root instructions, report the gap and obtain a decision about preserving or relocating it rather than silently deleting it.
- Link to the authoritative document with relative paths. Never copy facts that change often, such as test counts, coverage, benchmark numbers, or progress percentages; link to their source.
- Keep current behaviour separate from planned work. Put proposals in the project's established location (default `docs/proposals/` for new structures); do not migrate an existing layout incidentally.
- Exclude secrets, credentials, machine-specific paths, and personal preferences that do not apply to other contributors.
- Customization files need valid YAML frontmatter where required and a keyword-rich `description` beginning "Use when" or "Use for". Quote values that contain colons.

### 5. Update and audit

- Preserve useful existing rules, terminology, and structure. Make focused edits rather than wholesale rewrites.
- An audit checks for:
  - stale paths, commands, or globs;
  - contradictions between rules, docs, and code;
  - duplicated rules, or copied facts that have drifted;
  - overly broad `applyTo` globs and missing descriptions;
  - plans described as implemented behaviour;
  - a missing or outdated project summary, and, when tracking applies, a missing tracker or one whose contents disagree with the code; assess any omission against confirmed project rules rather than treating a missing file alone as an opt-out;
  - missing/conflicting license declarations, lost notices, and absent or overly broad ignore rules;
  - drift from [project conventions](project-conventions.md), reported per convention and marked as deliberate or unexplained;
  - gaps against the [open-source baseline](references/project-conventions-oss-baseline.md), reported by stage.

### 6. Validate and report

- Confirm every referenced path, link, and glob matches real files.
- Confirm listed commands exist; run safe, relevant ones when feasible and report any not run.
- Check frontmatter syntax, that skill `name` matches its folder, and that `applyTo` globs are specific.
- Review the final changes, including new/untracked files, against the confirmed scope. Check that existing constraints and unrelated work were preserved.
- Report files created or changed, evidence used, convention drift, contradictions, open questions, and unverified items. Account for each baseline item as present, created/updated, deferred, not applicable, or unresolved; do not claim the whole baseline is complete when gates remain unverified.
