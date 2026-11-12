# Runtime contract and limitations

`agentic-persona` uses `.github/plugin/plugin.json` with `skills: ["skills/"]`.
The repository root is the plugin root. It provides no agents, hooks, MCP
servers, marketplace or automatic instruction injection.

- CLI 1.0.105 supports a process-local `--plugin-dir` mount and
  `--sync-session=off`. Check the selected runtime's help; do not assume flags
  from another version or implicitly upgrade it.
- Native skill loading requires the `skill` tool to be exposed to the active
  agent. Check the tool result's source and path, especially with duplicate
  loose skills. Text assertions and discovery alone do not prove invocation.
- User instructions use `$COPILOT_HOME/copilot-instructions.md`, otherwise
  `$HOME/.copilot/copilot-instructions.md`, with separate approval and a restart.
  The plugin does not activate that file. No universal instruction precedence or
  automatic adherence is guaranteed.
- Persistent installation/update/uninstallation is not end-to-end verified.
  Until publication, use the feature checkout rather than the default branch.
- Environment isolation is not an OS sandbox. Keep normal consent controls.

Official references:

- [Plugin reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference)
- [Native instructions](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions)
- [Configuration directory](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-config-dir-reference)
