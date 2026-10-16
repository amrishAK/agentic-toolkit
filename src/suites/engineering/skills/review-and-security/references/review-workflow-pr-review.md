# PR review

**Gate:** in pre-PR mode, is this branch ready to open a PR? In existing-PR mode, is it ready to merge? State the selected gate; do not treat opening a PR as merge approval. The active agent may support only pre-PR mode.
**Range:** the branch compared with its base (`git diff <base>...HEAD`, `git log <base>..HEAD`), or the PR diff when reviewing on GitHub.
**Depth:** all [commit-review](./review-workflow-commit-review.md) checks across the whole range, plus the design-level checks below.

## Check

- **Architecture:** layer and module boundaries, platform or backend isolation, and dependency direction follow the [architecture conventions](../../project-standards/references/project-conventions-architecture-and-scope.md) and the project rules.
- **Public API:** additions are intended, documented and tested. Breaking changes are deliberate, marked in commits, and noted for the changelog.
- **Scope:** nothing listed as a non-goal; no planned work presented as implemented.
- **Tests:** each [test tier](../../project-standards/references/project-conventions-testing.md) affected by the change is covered. Tests that need infrastructure stay opt-in, and fixtures are deterministic.
- **Docs and status:** user-visible changes update the README or guides. When relevant feature documents, an adopted feature tracker, or roadmap files exist and are affected by the reviewed change, verify that the authors updated them in the same PR. Do not require documents the project has not adopted. For a confirmed feature-tracker opt-out, assess the established status and evidence sources instead; do not require or suggest creating a tracker. Back new claims with evidence. This check assesses author updates; it does not authorize reviewer edits.
- **Layout:** new source, tests, fixtures and test infrastructure are in the locations the project rules define.
- **Build and CI:** new commands go through the [shared entry point](../../project-standards/references/project-conventions-entry-points.md); CI calls it rather than duplicating steps; workflow permissions and caches are correct.
- **History:** commits are coherent and follow the adopted project convention. Report merge-time cleanup separately from readiness to open a PR; do not rewrite history.
- **CI result:** read checks for the reviewed head when available. Pre-PR CI may not exist yet: report it as not observed, not passed, and distinguish submission requirements from merge requirements.

## Blockers

- Any commit-mode blocker.
- An architecture boundary violation, or an unintended public API change.
- A behaviour change without tests at the right tier.
- Stale docs or status that the change makes untrue.
- Failing checks required for the selected gate. Missing required evidence must be reported as a gap; do not invent unavailable pre-PR CI or treat it as passed.
