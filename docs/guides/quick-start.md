# Quick start

Use this guide to find, preview, install, and use Agentic Toolkit guidance. The repository includes the Software Product Development suite and a Copilot installer. It does not automate the workflow or guarantee that a Copilot client discovers installed files.

## 1. Choose guidance

Start with the [suite guide](../suites/software-product-development.md) to find a role or task. Use an **agent** for a role with defined responsibilities; use a **skill** for a task method. Browse the maintained files directly if you do not need to install them.

## 2. Preview an installation

From the repository root, use GNU Make and Python 3.10 or newer. Install the declared Python dependencies first:

```text
python -m pip install -r requirements.txt
```

On Linux, use `python3` instead of `python` if that is your Python command. List available guidance, then preview an agent and its required resources:

```text
make list
make plan SUITE=software-product-development AGENT=code-engineer SCOPE=user
```

`plan` shows the files and checks the destination without writing anything. The default `user` scope installs under `.copilot` in the Python user's home directory. For a project installation, use `SCOPE=workspace` and provide an existing project path with `WORKSPACE`. See the [installation guide](../installation.md) for platform details and safe update options.

## 3. Install what you need

If the preview looks right, run the corresponding `install` command:

```text
make install SUITE=software-product-development AGENT=code-engineer SCOPE=user
```

You can instead install a responsibility package:

```text
make plan PACKAGE=product-management
make install PACKAGE=product-management
```

Or select skills without installing an agent:

```text
make plan SUITE=software-product-development SKILLS=code-quality-workflow,rust-code-quality
make install SUITE=software-product-development SKILLS=code-quality-workflow,rust-code-quality
```

Choose one selector: `PACKAGE`, `AGENT`, `SKILL`, or `SKILLS`. Omit them to select the full suite. An agent includes its required linked resources; selected skills include their linked resources, not unrelated agents. The [installation guide](../installation.md) explains selection and update behavior.

## 4. Use and check the guidance

If your Copilot client discovers the generated files, select the agent and explain the task, relevant project context, and intended result. Follow the role's boundaries and required workflows. If discovery is unavailable, read the maintained source directly.

Check that files were written to the intended location and confirm discovery in the actual client. Installation does not configure client settings or prove discovery, tool availability, delegation, or behavior. See the repository's [usage and compatibility notes](../../README.md#usage-and-compatibility).

## Next

- [Installation guide](../installation.md): scopes, selection options, and safe updates.
- [Software Product Development suite](../suites/software-product-development.md): current roles and task routes.
- [Roadmap-to-release workflow](roadmap-to-release-workflow.md): planning through authorized delivery.
- [Using Agentic Toolkit effectively](using-agentic-toolkit-effectively.md) and [as a solo developer](using-agentic-toolkit-as-a-solo-developer.md): proportionate use and decision-making.
