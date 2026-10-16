# Roadmap and known-issues documents

## Purpose and requirement

Use a roadmap to record high-level future direction and priorities. Use a known-issues document only for confirmed bugs or limitations. Their default locations are `docs/status/roadmap.md` and `docs/status/known-issues.md`; preserve established paths.

Both status documents carry an `Updated: YYYY-MM-DD` line and are updated when their contents change. A roadmap is optional: create one only when there is useful, confirmed direction to communicate.

## Roadmap outline

### Structure

```markdown
# Roadmap

Updated: <YYYY-MM-DD>

<High-level direction and priorities, not detailed release scope, status,
or schedule commitments.>

## <Priority or direction>
<Short description; link to a release document only when a planned milestone
has separately defined scope or acceptance.>

## Future direction
<Ideas; label unassigned targets and do not imply commitments.>
```

### What belongs here

Record high-level direction and relative priorities. Use milestone names only when they clarify direction, and link to the release document for separately defined scope and acceptance. Label unassigned ideas and targets; do not imply approval, dates, or delivery commitments.

### How it resolves the reader's need

The roadmap communicates where the project intends to go and what matters most, without presenting that direction as detailed release scope, implementation progress, or a committed delivery schedule.

## Known-issues outline

### Structure

```markdown
# Known issues

Updated: <YYYY-MM-DD>

| ID | Affected versions / scope | Confirmed symptom and impact | Evidence / tracking issue | Workaround | State |
|---|---|---|---|---|---|
| <KI-1> | <Verified scope> | <Observed behavior and user impact> | <Reproduction, test, or issue link> | <Verified workaround or none known> | <Project-defined state> |
```

### What belongs here

List only confirmed bugs and limitations that affect users or operators. Record verified affected scope, observable impact, evidence or a tracking issue, and a verified workaround or an explicit statement that none is known. Distinguish observations from suspected causes; do not include unverified reports, planned features, or ordinary non-goals. A missing feature is not automatically a bug.

Use the project's established state vocabulary. Update entries when confirmation, affected scope, workaround, or resolution changes; do not mark an issue fixed until the fix is verified. Remove resolved entries unless the project has an established reason to retain them here.

### How it resolves the reader's need

The known-issues document lets readers quickly identify what is confirmed to be broken or limited in their affected version or scope, understand the impact, and find evidence or a verified workaround. It separates known problems from roadmap ideas and unverified reports.

## Cross-document boundaries

The roadmap owns high-level direction, not release scheduling commitments. Record approved milestone scope, acceptance, and candidate readiness in the release document; link between the documents rather than copying their content. Link release blockers to their release owner, and qualify product or architecture claims contradicted by confirmed known issues.
