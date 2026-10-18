---
name: documentation-selection-workflow
description: "Use before reviewing, writing, updating, placing, or auditing a document to classify the document, select its canonical owner/location and matching rules, and pass that selection into the calling documentation workflow."
---

# Documentation selection workflow

## When to use

Use this skill to find the right owner, location, and rules for a document.

## Scope and boundaries

Use this workflow to access the shared documentation matrix, the single entry point for document-type guidance. The matrix holds document types, canonical owners, default locations, update triggers, and rule links; each linked document-type reference owns its usage guidance, content requirements, suggested structure, and validation. Common documentation rules apply across types. The calling writer, reviewer, implementer, or standardizer keeps the workflow and permissions; selection grants no access or edit authority.

The matrix covers documents, not the whole repository. Use [repository-wide placement conventions](../../suites/engineering/skills/project-standards/references/project-conventions-architecture-and-scope.md#repository-layout) for code, tests, tools, manifests, and outputs. The [setup workflow](../../suites/engineering/skills/project-standards/project-rules-workflow.md) owns repository inspection, proposal, confirmation, agreed essentials, and validation; documentation selection does not initialize a repository.

## Procedure

### 1. Classify the document

- Identify whether the task is to find/access, create/update, review, or audit documentation. For access, review, or update, find and open the existing canonical document first. Before creating a new document, search project indexes and established locations; use a matrix default only when no canonical home exists. If a document cannot be found or accessed, report the blocker rather than assuming permission to create or change it.
- Classify by purpose and audience, not by filename. A `README.md` inside `docs/` may be an index; a file called `overview.md` may be a vision pitch or a current-usage guide.
- Distinguish intent from state: product vision, detailed contract, current implementation, plan, operational procedure, and candidate evidence are different documents even when they cover the same feature.
- Project instructions, established locations, and adopted formats override matrix defaults. Surface conflicts rather than overriding them.
- If the type, audience, or owner is materially ambiguous, ask one focused question rather than guessing.

### 2. Select the canonical owner, location, and rules

1. Open the shared [documentation matrix](references/documentation-matrix.md#document-and-topic-reference-matrix) and match the document's purpose and audience to the applicable row or rows. Use the maintained matrix rather than reproducing its data here or selecting from memory.
2. Read the selected entries for the canonical owner, established or default location, update trigger, and linked rules. Matrix defaults apply only when the project has no established home. Apply the [ownership boundaries](#document-routing-and-maintenance-ownership) when responsibilities overlap.
3. Read the [common documentation rules](references/documentation/documentation-rules.md), which apply to every selected row. The matrix's final column links document-type rules and related specialist workflows; read only those relevant to the task. Use the shared [documentation layout](references/documentation/docs-layout.md) for the overall tree when needed. Invoke selected skills by exact name when supported; otherwise read their maintained sources and relevant references.
4. If the matrix or required guidance cannot be accessed, report the blocker without inventing a selection or claiming the rules were applied. If no row fits, report that gap and resolve any material classification decision before proceeding.
5. Pass the selected document type, canonical owner/location, applicable rule links, and unresolved decisions back into the caller's workflow. Selection does not invoke another agent or authorize creating every listed document.

#### Document routing and maintenance ownership

Each topic has one canonical owner, identified in the selected matrix row. Ownership identifies the responsible decision and normal specialist, not an exclusive file lock: implementers update directly affected documentation and evidenced status in the same change. The matrix is a default routing map, not automatic agent invocation; project-owned instructions remain authoritative and must work without this suite.

Assess baseline, release, and community documents by the project's stage and audience; see the [open-source baseline](../../suites/engineering/skills/project-standards/references/project-conventions-oss-baseline.md). Operational guides apply only when relevant. A matrix entry is not a requirement to create the file.

- Product planning owns intent; feature design owns detailed contracts; implementation supplies current behavior and evidence; reviewers independently assess readiness. None of these roles independently approves business commitments, publication, or a release.
- Reviewers return findings without direct document edits or persisted reports. Explicit apply selections allow delegation-enabled reviewers to launch bounded editing subagents and re-review; reviewers never perform delivery actions.
- Release goals are not release results. A changed candidate reruns affected gates or explicitly justifies reused evidence.
- Feature handoffs include goals/non-goals, testable acceptance criteria, contracts, dependencies, risks, and unresolved decisions. A small, well-defined fix does not need a feature document or every specialist.

### 3. Create or update

- Work only within the caller's authorized scope. Apply the selected rules for purpose, required/excluded content, structure, and boundaries; selection alone does not demonstrate compliance.
- Adapt suggested headings; meaningful content, not matching headings, meets requirements.
- Report missing requirements as unresolved; do not invent facts, commitments, versions, contacts, dates, thresholds, or commands.
- Preserve the document's intended framing. A vision stays a vision with envisioned behavior labelled; it is not replaced by an implementation inventory.
- Review findings cite an applicable rule or factual defect; stylistic preference is not a missing requirement.

### 4. Validate and report

- Check applicable requirements individually as met, unmet, or not applicable, with evidence or a reason. Verify factual claims, local links and anchors, and format.
- Report unresolved requirements and unverified claims. A selected matrix row is not proof of compliance.
- For a coverage audit, separately mark each relevant catalogue entry present, create/update, deferred, not applicable, or unresolved, with reasons for absences. Inventory status does not establish document compliance.
