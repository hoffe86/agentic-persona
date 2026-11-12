# agentic-persona

Optional personal Copilot tooling with five skills:

- **working-style**: communication, collaboration, consent, quality and docs.
- **development-architecture**: design/API and multi-repo preferences, with
  platform guidance only for matching Azure, Terraform, SPA and AI technologies.
- **[microservice-testing](skills/microservice-testing/SKILL.md)**: risk-based test
  planning, implementation and review for existing services; scoped boundaries,
  owner preferences and [primary sources](skills/microservice-testing/SKILL.md#sources),
  without choosing a stack or granting execution rights.
- **[planning-tool-preferences](skills/planning-tool-preferences/SKILL.md)**:
  concise tracker-neutral work-item preferences, with an
  [ADO reference](skills/planning-tool-preferences/references/ado.md) only for
  Azure DevOps Boards. Solution mappings and item standards remain authoritative;
  no tracker access or approval is granted.
- **[coding-style](skills/coding-style/SKILL.md)**: Clean Code and professional
  craft, with cross-language
  [Clean Code Developer guidance for all seven grades](skills/coding-style/references/clean-code-developer.md)
  alongside on-demand C#, Python and TypeScript references.
  Repository standards and tooling win; no compliance certification, tool
  installation, architecture changes or reviewer edit rights are granted.

The repository is [agentic-tools](https://github.com/hoffe86/agentic-tools);
the plugin identity is `agentic-persona`. There is no name alias or marketplace.
The repository root is the plugin root; `.github/plugin/plugin.json` discovers
`skills/`. No agents, hooks, MCP servers or automatic instruction injection are
included.

## Ownership

| Owner | Responsibility |
|---|---|
| Harness, if used | Roles, approvals, safety and evidence |
| Solution | Technologies, architecture decisions, scoped instructions and check commands |
| User | Optional preferences and stricter consent |

This package does not require [Agile Agents](https://github.com/hoffe86/agile-agents).
Personal preferences cannot waive solution constraints, approvals or read-only
boundaries. Surface conflicts; do not assume universal native prompt precedence.

## Try locally

Use a checkout at a revision containing the package, not an earlier
default-branch revision. From a solution directory:

```sh
PLUGIN_DIR="/path/to/agentic-tools"
copilot --no-auto-update --sync-session=off --plugin-dir "$PLUGIN_DIR"
```

Check the selected runtime's help for supported flags; do not assume support
across versions or upgrade implicitly. Keep interactive approvals. Ask:

> Invoke working-style using the native skill tool and report its source directory.

Verify the native tool result and loaded source path, not an assistant's claim.
Duplicate loose skills can mask the source. Custom agents need a native `skill`
tool grant; skill `allowed-tools` metadata grants nothing.

The mount is process-local. Restart without the flag to remove it. Core and
personal packages can be mounted independently with repeated `--plugin-dir`.
This is not persistent activation or an OS sandbox.

## Native user instructions: separate opt-in

Mounting this plugin **does not activate**
[native/copilot-instructions.md](native/copilot-instructions.md). Skills are
on-demand; the manifest does not deliver arbitrary always-on instructions.

Only with explicit approval, copy the reviewed native source to
`$COPILOT_HOME/copilot-instructions.md`, or
`$HOME/.copilot/copilot-instructions.md` when `COPILOT_HOME` is unset.
If the file exists, inspect and back it up, then approve a deliberate merge.
Never overwrite it implicitly. Restart the CLI after changes; inspect discovery
with `copilot instruction list --json`. Discovery does not guarantee adherence
or skill invocation.

## Updates and rollback

- For a mount, inspect a newer revision in a separate checkout, run checks, then
  start a new session pointing at it. Keep the prior checkout for rollback.
- With approval, once the package is on the repository's default branch, the
  direct-repository install address is
  `copilot plugin install hoffe86/agentic-tools`. Named update/uninstall commands
  use `agentic-persona`; confirm syntax in the selected runtime's help.
  Persistent installation, update and uninstallation are not end-to-end verified.
- Roll back a mount by selecting the prior checkout or omitting the flag.
  Restore an approved native-instruction copy from its backup with consent.
- Inventory duplicate copies before activation. Remove only explicitly approved
  copies with reversible backups; never delete the whole user skills directory.
  Updates do not authorize changes to native instructions or loose skills.

## Checks and references

No application build or dependencies are required; tests use Python 3.9+ stdlib:

```sh
python3 -B -m unittest discover -s tests -v
git diff --check
```

Static tests check packaging, resources, links, scope and consent rules.
They do not prove model behavior.

Package code and authored guidance use the [MIT license](LICENSE). Source
attribution and third-party ownership qualifications are kept beside the
affected skills and references.

- [Official plugin reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference)
- [Native instructions](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions)
- [Configuration directory](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-config-dir-reference)
