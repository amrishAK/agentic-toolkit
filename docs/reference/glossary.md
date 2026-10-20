# Repository glossary

This glossary is the vocabulary authority for Agentic Toolkit's maintained documentation, agent definitions, skills, and catalogues. Use these terms consistently when creating or updating repository guidance. Specialist documents may define additional domain-specific terms, but should not silently redefine terms here.

Entries marked **Proposed V2** describe future direction, not current repository capabilities.

| Term | Meaning and usage |
|---|---|
| **Suite** | A maintained grouping of agent and skill definitions listed in a YAML manifest under `src/suites/`. Source categories organize definitions but do not determine suite membership. Identify future groupings as proposed, not available. |
| **Installation package** | A versioned functional grouping of agents and skills explicitly listed under `src/packages/` and selected with `PACKAGE=<name>`. Uses the shared installer; distinct from a language pack or remote package registry. |
| **Agent client** | The external environment that may discover or run agent definitions and provides their runtime, available tools, and permissions. Source layout alone does not establish client support or behavior. |
| **Agent definition** | Maintained instructions describing an agent role and its boundaries. |
| **Skill definition** | Maintained reusable task guidance, distinct from agent role instructions. |
| **Supporting reference** | Focused material linked from an agent or skill definition. A reference is not a separately invokable skill unless it has its own skill definition and metadata. |
| **Catalogue** | A maintained inventory or routing aid for finding definitions. It is not a runtime registry or proof that entries are installed or available. |
| **Maintained source / generated client file** | The repository-owned source is canonical; a generated client file is an installation output for a particular client layout, not a second source of truth. |
| **Task workflow** | Procedural guidance for a particular task or a shared task cycle. Use **lifecycle model** for a broader grouping of responsibility areas. |
| **Stage** (**Proposed V2**) | A responsibility area in the proposed lifecycle model, not necessarily a maintained suite, separate person, or mandatory step. |
| **Lifecycle model** (**Proposed V2**) | The proposed grouping of Product Discovery & Shaping, Product Management, and Engineering responsibility areas. It is decision-support guidance, not a required sequence or automatic orchestration. |
| **Handoff** | Context and a requested next decision or action for a responsible person or role. It does not imply approval, execution, or automatic orchestration. |
| **Product-level feature brief** (**Proposed V2**) | A product-facing description of user outcomes, intended scope, and exclusions. It is distinct from a detailed Engineering feature contract. |
| **Engineering feature contract** | Detailed intended behavior, edge cases, and failure behavior used to guide implementation and verification. A contract describes intent, not implementation evidence. |
| **Acceptance criteria** | Observable conditions used to judge whether an intended outcome is met. |
| **Acceptance examples** | Illustrations of expected behavior that clarify intent. Examples do not replace criteria unless explicitly adopted as criteria. |
| **Proposed / approved / implemented / verified / released** | Distinct states of a decision or work item. Approval is not implementation; implementation is not verification; verification evidence is not release approval. Do not imply an automatic progression. |

## Guidance-selection verbs

Use **select guidance** when describing catalogue use. Say that a skill is **invoked** only when the agent client supports it; otherwise it is **read** from its maintained source. These verbs describe different actions and should not be used interchangeably.
