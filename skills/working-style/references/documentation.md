# Documentation preferences

Follow solution documentation conventions and ownership. Where the owner can
choose, prefer:

- Document the **current state** of the solution. Do not add change history,
  migration notes, "previously/now" comparisons or change logs to docs; version
  control, PRs and release notes own change tracking. ADRs remain dated
  decision records; this rule does not rewrite them.
- Keep architecture and concept docs at **concept and architecture level**:
  responsibilities, boundaries, interactions, decisions and quality attributes,
  not code walkthroughs or implementation detail that duplicates the code.
- Tutorials, getting-started guides, hands-on guides, runbooks and operations
  docs may include concrete steps, commands and configuration detail when needed
  to complete the task.
- **arc42** structure for architecture overview, operations, compliance, testing,
  runbooks, hands-on guides and diagrams.
- **C4**: L1–L2 context/container diagrams in central solution docs; L3–L4
  component/code diagrams in the owning service repo.
- **DDD**: one file per aggregate in its service repo covering purpose, invariants,
  entities, value objects and domain events; central aggregate indexes link there.
- **Solution docs** own the big picture, domain model, glossary, ubiquitous
  language, event contracts, integration patterns, cross-repo indexes and
  operating conventions. **Service repos** own aggregates, service overview,
  APIs, data, deployment, testing, monitoring and runbooks.
- Centralize ADRs in solution docs; services link, not duplicate. Honour existing
  locations and human authorship/approval; this grants no permission to create
  or move ADRs.
- Use full GitHub URLs across repos and relative links within one, never relative
  paths into another checkout.
- Update docs with every essential architecture, setup, environment-variable,
  CI/CD, API or cross-repo dependency change. Prefer `docs/README.md` as the docs
  hub; avoid file-by-file project inventories that quickly go stale.
