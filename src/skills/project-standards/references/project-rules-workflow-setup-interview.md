# Setup interview

Use this for initial setup or requested repository standardization, including projects that already have `AGENTS.md`. Follow **inspect → explain/propose → ask/refine → confirm → create essentials → validate/report**, with evidence-based defaults. Collect initial context before proposing when needed, but do not replace meaningful proposal/refinement/confirmation with automatic scaffolding or a final unexplained file list.

## How to ask

1. Gather evidence first (workflow section 1). For each topic below, draft an answer from the repository.
   - Explain detected structure and suitable options using the [repository-wide placement map](project-conventions-architecture-and-scope.md#repository-layout). Clearly label example or proposed paths; do not imply they already exist.
2. Ask **one question at a time**, using the ask-question tool when available.
   - When evidence suggests an answer, offer it as the first choice, marked "(detected)", with alternatives.
   - When nothing can be inferred, ask an open question.
3. Skip questions the user has already answered in this conversation.
4. When running as a subagent without a way to ask the user, stop before writing. Return the drafted answers and the open questions instead of guessing.
5. Ask whenever a material fact or decision is uncertain; do not treat missing policy as permission to choose one.
6. Present and refine the structure proposal below before final approval. Finish by showing all answers, exact agreed files and structural changes, retained decisions/opt-outs, deliberate deviations, and deferred items. Ask for confirmation before writing files; a newly discovered material change needs another focused question and confirmation of that change.

## Required: the project summary

Never skip this. Ask the user for a summary of three to five sentences: what the project is, who it is for, the problem it solves, and its current stage. Offer a draft built from the README if one exists, but the user must confirm or rewrite it. Do not write `AGENTS.md` without a confirmed summary.

## Topics

Ask in this order. Skip a topic only when the evidence is unambiguous, and still show it in the final summary.

| # | Topic | What to establish |
|---|---|---|
| 1 | Summary | The required project summary above |
| 2 | Stage | Prototype, pre-v1 or released; first release target |
| 3 | Languages and toolchain | Languages, edition or standard, minimum Rust version or compiler support, supported platforms |
| 4 | Pipeline | The shared entry point (Make, Cargo aliases, scripts), the CI provider, and which CI jobs exist or are wanted |
| 5 | Layout | Explain and refine the repository-wide structure proposal: source/public interfaces, test tiers, fixtures/test infrastructure, docs, scripts/tools, examples, benchmarks, manifests/configuration, client guidance, outputs and local secrets |
| 6 | Test tiers | Which tiers exist, which need infrastructure (databases, containers, network), and how to run each |
| 7 | Architecture boundaries | Layers, platform or backend isolation, public versus internal API, invariants that must hold |
| 8 | Non-goals | What the project deliberately will not do |
| 9 | Features and tracking applicability | Whether the project adopts a feature tracker; if so, implemented, in-progress and planned features for `docs/status/features.md` |
| 10 | Licensing | Open-source or private/proprietary intent; existing or chosen license, notices, required rights-holder details, and metadata conflicts |
| 11 | Ignore policy | Generated/local files to exclude; source, fixtures, lockfiles and shared configuration to retain; ambiguous tracked output |
| 12 | Agent boundaries | Paths agents must not touch, and actions that need approval |
| 13 | Documentation and release policy | Applicable catalog documents; audiences, release scope/gates, contribution workflow, supported versions, private security-reporting contact and any adopted response commitments |
| 14 | Setup scope | Which missing baseline documents and structure to create now, which deviations to retain, and what to defer |

Use the [document catalogue](../../documentation/references/documentation-matrix.md) to prepare the documentation questions and proposed outlines. Ask unresolved policy questions separately, one at a time; the table groups topics, not multiple questions in one prompt. Do not manufacture policies or contacts to complete a template.

## Structure proposal and refinement

Once enough context is known, explain a suitable repository-wide structure, not just the docs tree or the placement of `AGENTS.md`. Use detected paths first and the placement map for applicable gaps. Cover the layout categories above; explicitly mark categories that are not applicable or not established rather than inventing paths. Keep the proposal in the conversation unless a persisted plan is separately requested.

Use a compact table or equivalent with these fields:

| Path / item | Meaning and contents | State | Rationale / applicable conditions |
|---|---|---|---|
| Actual path, or clearly labelled candidate path; no path if not established | What it owns and what belongs elsewhere | Existing (retain/update), proposed (create only after confirmation), deferred, or not applicable | Project evidence, ecosystem convention, user need, prerequisite or approval still required |

- Explain alternatives and trade-offs **before asking the user to choose**. Ask one focused structure question at a time; refine the table as answers arrive. Do not require a choice for settled, unambiguous locations, but include them in the proposal for context.
- Separate existing paths from proposed paths and future/deferred infrastructure. Describing a desired test tier, build system or CI layout does not authorize its implementation or a file migration.
- Identify the exact essentials to create/update: `AGENTS.md`, `README.md`, and applicable confirmed licensing, ignore rules and supporting documentation. Select these from evidence and interview answers, not every catalogue row. Preserve confirmed omissions and opt-outs; do not introduce a mandatory tracker.
- Before writing, confirm the final structure and file actions together with the answers, preserved decisions, deferred work and any remaining unresolved items. Do not silently add files after approval or put links to merely proposed paths in the finished guide.

## Feature list (when tracking applies)

- Confirm whether feature tracking applies. Treat a missing tracker as insufficient evidence of an opt-out; honor an explicit, confirmed project rule to omit one, even when the cross-project default recommends it.
- Only when tracking applies and is confirmed, build the first draft of the feature table from the README, `docs/`, the public API and tests. Mark each feature `Done` only when code and tests exist.
- When tracking applies, ask the user to confirm the states, add planned features, and assign targets.
- When tracking is confirmed as applicable, write the result to `docs/status/features.md`, using the format in the project-tracking convention, and link to it from `README.md` and `AGENTS.md`. Otherwise, do not create the table or add tracker links.

## After the interview

- Only after final confirmation, implement the agreed essentials; do not end at a proposal when setup is authorized. If confirmation cannot be obtained, return the draft proposal and open questions without writing.
- Write `AGENTS.md` from the [outline](project-rules-workflow-agents-md-outline.md) using the confirmed answers. Align the README summary, link both entry points to relevant authorities, and link to the feature tracker only when tracking is confirmed as applicable.
- Create or update the confirmed supporting documentation, `LICENSE`, and `.gitignore` using the workflow safeguards. Do not add placeholder directories or template policies unsupported by the answers.
- Report any differences from project conventions that the answers reveal. Pipeline wishes are not authorization to implement infrastructure: do not migrate files, add tooling, change build/CI configuration, or edit production code/tests without explicit authorization.
- Verify the completed setup and report deferred, not-applicable, unresolved, and unverified items separately.
