# Quick start

Use this guide to find and use maintained Agentic Toolkit guidance for an Engineering task. The repository currently provides the Engineering suite and a Copilot installer; it does not provide an automatic workflow or guarantee that an agent client will discover installed definitions.

## 1. Choose a starting point

You can browse the maintained definitions without installing them. Start with the [Engineering suite guide](../suites/engineering.md) to find a role or task workflow, or use the [skill selection workflow](../../src/shared/skills/skill-selection-workflow.md) and its [Engineering task matrix](../../src/shared/skills/references/skill-selection-workflow-matrix.md) to select relevant guidance.

Choose an agent when you need a role with defined responsibilities and boundaries. Choose a skill when you need a task method. An agent may require linked skills; selecting one skill does not install an agent.

## 2. Preview a Copilot installation

To install guidance, use GNU Make and Python 3.10 or newer from the repository root. No Python packages are required.

List available definitions, then preview one agent and its linked resources:

```text
make list
make plan SUITE=engineering AGENT=code-engineer SCOPE=user
```

`plan` displays the generated paths and checks the destination without creating files. The user scope installs under `.copilot` in the Python user's home directory. To install to a project instead, set `SCOPE=workspace` and `WORKSPACE` to an existing project directory; see the [installation guide](../installation.md) for platform-specific examples and staging options.

## 3. Install only what you need

If the preview is as expected, run the matching install command:

```text
make install SUITE=engineering AGENT=code-engineer SCOPE=user
```

For a task that needs skills without an agent, select the relevant skills explicitly. For example, for Rust code-quality work:

```text
make plan SUITE=engineering SKILLS=code-quality-workflow,rust-code-quality
make install SUITE=engineering SKILLS=code-quality-workflow,rust-code-quality
```

Agent selection includes that agent's linked required skills and resources, not every skill listed in a catalogue. Skill selection installs the selected skills and their linked resources, not unrelated agents. Read the [installation guide](../installation.md) before updating an existing installation or when you need the full selection and update behavior.

## 4. Use and verify the guidance

If your Copilot harness discovers the generated definition, select the agent and describe the task, relevant project context, and desired outcome. Follow the role's boundaries and any required workflows; use the task matrix for additional guidance when needed. If discovery is unavailable, open the maintained source and use it directly rather than assuming the installation is active.

Confirm that generated files are in the intended destination and check discovery in the actual client. Installation does not configure client settings or prove runtime discovery, tool availability, delegation, or behavior. The [usage and compatibility notes](../../README.md#usage-and-compatibility) explain these limits.

## Next

- Use the [Engineering suite guide](../suites/engineering.md) to choose roles and understand handoffs.
- See [Using Agentic Toolkit effectively](using-agentic-toolkit-effectively.md) for proportionate decision-making and traceability.
- See [Using Agentic Toolkit as a solo developer](using-agentic-toolkit-as-a-solo-developer.md) for a lightweight individual workflow.
