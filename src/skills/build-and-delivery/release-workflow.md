---
name: release-workflow
description: "Use for reviewing, planning, or implementing release readiness: versions, changelogs, API/ABI/package compatibility, installation smoke tests, dependency/licenses, provenance, SBOM/signing policy, and authorized delivery. Uses the language-specific skill matrix."
---

# Release readiness

## When to use

Use this skill to assess and prepare a software release.

## Scope and boundaries

Apply with build automation and relevant build/CI/container guidance. Consult the [language-specific skill matrix](../programming-languages/references/programming-language-matrix.md)'s **Code quality** guidance for language-specific compatibility concerns and its other task columns for affected checks. Preparing or reviewing a release does not authorize tagging, committing, pushing, publishing, or deployment.

## Procedure

### Establish policy and evidence

- Identify intended version, source revision/dirty state, supported platforms/features, artifact types, consumers, and project release/approval policy.
- Reuse established shared entry-point/native packaging commands and CI gates. Do not invent branch strategies, versioning rules, signing requirements, or disclosure policy.
- Check manifest/version/changelog consistency and evidenced user-visible changes. Separate unreleased documentation from released behavior.
- When authorized to prepare a release with adopted versioned release notes, prepare or update them using the [release notes requirements](../documentation/references/documentation/release-notes.md). Verify the filename and documented version match exactly and cover the delivered features. Once notes are ready, consolidate completed feature documents while preserving necessary contracts and evidence, remove superseded standalone documents, and update their replacement links; keep unfinished or future feature documents active.
- Check the project meets Stage 1 and Stage 2 of the [open-source baseline](../project-standards/references/project-conventions-oss-baseline.md); report gaps by stage.
- Review intended API/ABI/package, configuration, protocol, and persisted-data compatibility; assess dependency/runtime/target-framework/MSRV changes and required migration/rollback limits.

### Build and verify

- Verify required checks actually executed for the supported release matrix; distinguish reviewed, locally tested, and remotely observed results.
- Include applicable unit and integration regression suites and critical [E2E journeys](../testing/e2e-test-workflow.md) for the intended candidate. Release validation is broader than E2E: passing journeys or feature acceptance does not replace artifact, installation, compatibility, migration, provenance, or other project-specific gates. Reuse prior evidence only when it applies to the candidate; rerun affected checks after changes.
- Build intended artifacts with recorded toolchain/dependency identities. Version pinning alone does not prove reproducibility; verify repeatability only where required and feasible.
- Inspect package contents and test installation/loading plus a meaningful smoke operation in an isolated consumer environment. A build-tree test does not validate the installed package.
- Review direct/transitive dependency inventories and license obligations with existing tooling/policy. Report uncertain obligations; do not offer legal certification.
- Generate/verify checksums, SBOM, provenance, and signatures when required or requested using supported mechanisms. Do not fabricate attestations or expose signing keys.
- Check delivery permissions, immutable artifact identity, approval gates, secret handling, and failure/rollback behavior without executing remote actions by default.

### Report and deliver

- Report blockers by impact, suggested corrections, exact artifact/check identities, untested configurations, and remaining approvals.
- When delivery is explicitly authorized, publish only verified intended artifacts through the approved path and confirm destination/version. Report partial failures; never describe local packaging as a published release.
