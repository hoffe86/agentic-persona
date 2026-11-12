# Azure DevOps Boards preferences

Load only for Azure DevOps Boards work. Apply the entrypoint's ownership and
safeguards; these mechanics grant no additional authority.

## Target and fields

Confirm organization/collection, project, Services or Server, version/features,
process, actual work-item type and its metadata. Basic has no Bug type and
uses Issue for bugs; Issue is not universally Bug. Do not assume Product
Backlog Item or common fields exist on every type.

Use supported type-metadata reads (for example, `wit_work_item` action
`get_type` in current Microsoft MCP); discover actual tools/schemas at runtime.
When reading relations, current `get` supports `expand: Relations` but cannot
combine expansion with field selection.

Typical field hints, only after validation:

- `System.Description`: body.
- `Microsoft.VSTS.Common.AcceptanceCriteria`: acceptance criteria where present.
- `Microsoft.VSTS.TCM.ReproSteps`: bug reproduction steps where supported.

Get custom BDD/Open Points destinations from solution mappings or actual schema.
Never invent fields or silently discard content: use a solution-approved
description heading if permitted; otherwise retain the draft and ask.
Use solution/project area, iteration, tags and state mappings; merge, never
clobber unrelated values. No guessed iteration, hardcoded Draft/release tags,
or unauthorized priority/severity writes; severity is not priority.

## Text formats

Prefer Markdown only where target, field and tool support it—not "Services
means Markdown; Server means HTML." Preserve existing content and formats;
do not silently convert rich text or recommend irreversible conversion without
explicit approval.

Read the live write schema and current MCP examples below for field-specific
format controls. Current create/update_batch large-text values default to HTML
unless Markdown is explicit; add_child has its own Markdown default. Current
update uses JSON Patch, not a named format parameter. Never switch to batch
solely for markup if that bypasses concurrency protection.
Markdown text in an HTML field is not correct formatting; write success is not
rendering proof. If supported formatting cannot be expressed safely, ask/report.

## Links and states

Distinguish parent/child hierarchy, predecessor/successor dependencies and Related.
Preserve direction and existing links; don't infer hierarchy from labels or
record dependencies only in prose. Use inline `#ID` only on supporting surfaces;
prefer canonical URLs across contexts or when ambiguous. Follow solution PR
reference syntax; `AB#n` is a convention, not a universal cross-repository issue
reference. No PR creation, closure or merge authority is granted.

Use actual process/type states and solution mappings, never a universal table.
If an intermediate state has no equivalent, leave state unchanged and comment
only when authorized; never map "implemented" to "done" by convenience or walk
intermediate states to force a rejected transition.

## Safe writes

For read-modify-write, use a revision guard where supported. Current MCP update
supports prepending JSON Patch `test` on `/rev` with the previously read numeric
revision. On stale rejection, reread and resolve; don't blindly overwrite.
If creation's outcome is uncertain, check for the existing item before retrying.
Re-read fields, links and comments; report partial failures explicitly.

## Sources

- [Microsoft MCP examples](https://github.com/microsoft/azure-devops-mcp/blob/main/docs/EXAMPLES.md)
- [Field references](https://learn.microsoft.com/en-us/azure/devops/boards/queries/titles-ids-descriptions?view=azure-devops)
- [Bug/process differences](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/manage-bugs?view=azure-devops)
- [Markdown links](https://learn.microsoft.com/en-us/azure/devops/project/wiki/markdown-guidance?view=azure-devops#links)
