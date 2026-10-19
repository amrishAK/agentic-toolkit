# Common documentation rules

These rules apply to documentation selected through the shared [documentation matrix](../documentation-matrix.md). They are common references for writers, reviewers, implementers, and standardizers, not the property of one workflow. Project instructions, established locations, and adopted formats take precedence over defaults.

- **One canonical owner per topic.** Other documents summarize and link with relative links; they do not copy mutable status, procedures, contracts, or evidence.
- **Keep kinds of truth separate.** Intended capabilities, detailed contracts, implementation state, release requirements, and executed evidence live in their own documents. Missing evidence is not a pass.
- **Respect decision owners.** Documentation changes must not silently make another owner's decisions. See the selection workflow's [ownership boundaries](../../documentation-selection-workflow.md#document-routing-and-maintenance-ownership).
- **Split by audience, owner, or update trigger,** not line count. Reuse an existing canonical home before creating a file. A split or move updates inbound and outbound links and removes the obsolete copy.
- **Only applicable documents.** Do not create placeholder files, trackers, or policies just because the catalogue lists them.
- **Readable navigation.** Readers reach a task and its authoritative document without circular or duplicate guidance. Use tutorials, how-to, reference, and explanation content purposefully ([Diataxis](https://diataxis.fr/)) without forcing a directory structure.
- **Validate the real format.** Check local links, anchors, heading hierarchy, and renderer compatibility. For external formats such as [GitHub templates](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/about-issue-and-pull-request-templates), [security policies](https://docs.github.com/en/code-security/how-tos/configure-and-manage-your-organization/establishing-a-security-policy), and [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), follow the actual specification. A license file or badge does not establish licensing rights.
