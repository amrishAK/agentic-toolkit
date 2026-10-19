# Release review

**Gate:** is the project ready to tag and publish this version?
**Range:** everything since the last tag (`git log <last-tag>..HEAD`). Before the first release, the whole project.
**Depth:** [PR-review](review-workflow-pr-review.md) checks at project level, plus `release-workflow` and the [open-source baseline](../../project-standards/references/project-conventions-oss-baseline.md).

Load `release-workflow` and apply it alongside this list. Reviewing a release never authorizes tagging, pushing or publishing.

## Check

- **Open-source baseline:** applicable Stage 1 and Stage 2 items are present and accurate; honor confirmed project-specific opt-outs and report gaps by stage.
- **Version:** the manifest version follows SemVer for the changes since the last tag. Breaking changes since the last tag match the version bump.
- **Changelog:** the `Unreleased` entries cover every user-visible change since the last tag and match the commit history.
- **Release notes and feature consolidation:** if adopted, verify the filename and documented version match exactly, delivered features are covered, and ready notes preserve necessary contracts and evidence for completed features they consolidate. Verify completed superseded feature documents are removed only once notes are ready and their inbound links point to the replacement notes or canonical contracts; keep unfinished or future work active. Apply the [release notes requirements](../../documentation/references/documentation/release-notes.md#consolidate-feature-documents) and [feature-document guidance](../../documentation/references/documentation/feature-docs.md). Review only: report findings; do not author or edit notes, consolidate or delete documents. The review does not authorize edits or publication.
- **Public API:** list what is exported. Everything is intended, documented and tested; nothing internal leaks out. Names are final, because renaming after release is a breaking change.
- **Claims:** every README and docs claim about performance, coverage, safety or guarantees is backed by a test, benchmark or report, or stated as a goal.
- **Feature tracking and related docs:** when relevant feature documents, an adopted feature tracker, or roadmap files exist and are affected by this release, verify that the authors updated them for this release. Do not require documents the project has not adopted. When a tracker is adopted, every feature marked `Done` has working code and tests; features in this release are marked with this version as their target; the README status section agrees with the tracker. For a confirmed feature-tracker opt-out, assess the established status and evidence sources instead; do not require or suggest creating a tracker. This check assesses author updates; it does not authorize reviewer edits.
- **Consistency:** the project, crate, package and file names agree across the manifest, README, docs and code. Status files match the code.
- **Toolchain and platforms:** the declared minimum Rust version, C/C++ standard, or .NET SDK/target framework and each claimed platform are tested in CI.
- **Dependencies:** licence and advisory checks pass; no unexpected or unpinned dependencies.
- **Artifacts:** the package builds from a clean checkout and installs and runs in an isolated consumer, as `release-workflow` describes.

## Blockers

- Any PR-mode blocker still open on the release range.
- A missing applicable Stage 1 or Stage 2 baseline item, accounting for confirmed project-specific opt-outs.
- A version that does not match the changes, or a missing changelog entry.
- For adopted release notes, missing delivered-feature coverage, lost necessary contracts or evidence during consolidation, premature removal of feature documents, or stale replacement links.
- Internal API exposed by accident, or a non-final name in the public API.
- Any claim not backed by evidence.
- Failing licence or advisory checks, or a package that fails the install smoke test.
