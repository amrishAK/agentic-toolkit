# Release notes requirements

## Purpose and requirement

Use release notes when the project adopts a user-facing summary for a version. Preserve its established release page or document location; the default file location is `docs/releases/<version>-notes.md`. Drafting notes does not authorize publication or establish that a release has shipped.

For file-based release notes, include the exact release version in the filename, including any prerelease suffix; for example, `v1.2.0-notes.md` or `v1.3.0-rc.1-notes.md`. Match the project's version/tag naming convention and keep one file per version.

Release notes explain what changed for users and what they need to do. The [release plan](release-docs.md) owns milestone progress, acceptance gates, and candidate evidence; the [changelog](community-docs.md#changelog) owns the curated history across versions. Link to those sources rather than copying progress tables or raw commit logs.

## Structure

```markdown
# <Product> <Version> release notes

Status: <Draft / prerelease / released, based on evidence>
Release date: <Verified date; omit until known>

## Highlights
<Most important delivered changes and their user impact.>

## Changes and fixes
<Notable additions, behavior changes, and resolved issues.>

## Consolidated feature details
<One anchored subsection per completed feature whose standalone document
is being removed; retain necessary contracts, decisions, and evidence links.>

## Compatibility and upgrade
<Breaking changes, deprecations, supported configuration changes,
required user actions, and links to migration or installation guidance.>

## Known issues and limitations
<Confirmed issues affecting this version, workarounds, and canonical links.>

## Release links
<Verified version/tag, artifacts or release page, and changelog links.>
```

Adapt headings to the audience and project format. Omit inapplicable sections; do not leave placeholders in completed notes.

## What belongs here

- Identify the product, exact version, release status, and publication date when verified. Clearly label draft and prerelease notes.
- Describe notable delivered changes and fixes in user terms, including practical impact rather than only issue numbers or internal implementation detail.
- State breaking changes, removals, deprecations, runtime/platform requirements, and required upgrade or migration actions where affected. Link to canonical procedures instead of duplicating them.
- Include confirmed version-specific limitations and workarounds. Link to known-issue records without presenting future fixes or roadmap items as delivered.
- Link to verified release artifacts, installation guidance, and the matching changelog entry where available. Do not invent URLs, dates, support promises, or performance claims.

## How it resolves the user's need

Readers can decide whether to adopt the version, understand compatibility risks, and find the actions needed to upgrade. Release notes are not release approval, a feature tracker, or evidence that all acceptance gates passed.

## Consolidate feature documents

- When versioned release notes are ready, compile and summarize the completed feature documents included in that release into the notes, then remove those standalone files in the same authorized documentation change. Preparing a draft alone is not sufficient, and review-only work does not authorize consolidation or deletion.
- Give each consolidated feature a stable heading. Keep the user-facing summary concise while preserving necessary behavior, edge cases, acceptance criteria, compatibility constraints, decisions, and source/test evidence in the feature's detail subsection or links to existing canonical contracts. Do not discard the only record of a continuing contract to shorten the notes.
- Keep proposed, deferred, partially implemented, or cross-release work in active feature documents. If a document mixes delivered and future scope, move only the completed release-specific content and retain the remaining work with a link to the notes.
- Before removing a completed feature file, update all inbound links, navigation, and adopted tracker references to the matching release-note heading or existing canonical contract. Rebase relative links copied from the old file and preserve referenced decision IDs.
- Verify content coverage and replacement links before deletion. Release notes become the version-specific historical record, not a mutable specification for future releases; subsequent changes use active feature documents and current contract or architecture authorities.

## Validation

- Reconcile every delivered-change claim with the intended version's source, artifacts, changelog, or supplied verification. A merged change is not necessarily included in the released artifact.
- Verify that the filename version matches the documented release version, including any prerelease suffix. Verify version/date/status consistency and release, issue, artifact, and guide links. Distinguish inspected evidence from checks actually executed.
- Check that affected compatibility changes, upgrade actions, and confirmed limitations are covered. Do not turn missing evidence into a claim of compatibility or an issue-free release.
- Keep drafts distinct from published notes. Corrections follow the project's publication policy and must not silently rewrite release history.
- For consolidation, verify that every removed feature document is represented, required details remain accessible, and no references still target removed files or anchors.
