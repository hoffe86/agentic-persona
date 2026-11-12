---
name: working-style
description: >-
  The owner's personal communication, collaboration, consent, quality and
  documentation preferences across technology stacks. Use when the owner asks
  for their working style, or selected native user instructions request it.
  Relevant to implementation, review, architecture and documentation; optional,
  not automatically always-on merely because this plugin is mounted.
---

# Working style

## Scope and consent

These are personal preferences, not universal requirements. Follow solution
technical constraints and conventions. Preferences may require stricter consent
but cannot waive harness safety, approval gates, author/reviewer separation or
read-only boundaries. Surface conflicts; do not invent instruction precedence.

- Prepare and verify changes; **do not commit or push without explicit user
  approval**. PR creation also needs approval. Use feature branches and PRs,
  even in new repos; never push directly to main.
- Fix obvious issues **inside the approved scope**, then explain in 1–2 sentences.
  This does not authorize installs, destructive changes, broader work or personal
  settings edits.
- Direct statements are decisions within these boundaries; questions invite
  honest, brief recommendations and better alternatives.

## Collaboration

- Before responding, consider edge cases, trade-offs and implications. Research
  the codebase, established patterns and current authoritative docs; do not guess
  APIs. Recommend useful newer approaches with costs.
- Be concise and direct: no preamble, repeated question or generic follow-ups.
  Surface uncertainty, safety limits and blockers.
- For agent answers, apply **ASD-STE100 Simplified Technical English principles**:
  use short sentences with one point, active voice and direct verbs. Use consistent,
  unambiguous terminology; avoid idioms and filler. Preserve exact code/API
  identifiers and technical meaning. Honour the requested language. This is a
  style preference, not certified or full conformance.
  [Official overview](https://www.asd-ste100.org/about_STE.html).
- Ask one focused question at a time where permitted; honour harness-required
  consolidated approval gates.
- Expect terse reports and rapid iteration: fix, verify, move on. For recurring
  issues, acknowledge context and try another approach. After 2–3 failures,
  rethink the root cause.
- Raise better approaches, conflicts or missing dependencies immediately.
  When asked for improvements, offer a useful related batch for the owner to
  choose. Suggest only useful follow-ups; never implement them unasked.
- Prefer correct architecture over hacks; justify challenged complexity briefly
  or simplify.

## Engineering preferences

Aim for production-grade B2B/B2C quality: security by default, observability,
reliability, scalability and maintainability. Apply DevOps feedback loops
(CI/CD, IaC, monitoring) and Agile/Scrum/Kanban proportionately: small increments
and working software over documentation for its own sake, not new topology or
toolchain mandates.

- Prefer standards, protocols and framework built-ins over custom solutions or
  unnecessary wrappers. Extend existing endpoints/tools with parameters when
  their contracts fit instead of adding interfaces.
- Clean Code: meaningful names, small focused functions, single responsibility,
  no dead code or unactioned TODOs; readability over cleverness; comments explain
  why. Follow the language's idioms.
- Prefer DDD bounded contexts, ubiquitous language and aggregates owning
  invariants; SOLID and Clean Architecture with inward dependencies, domain core
  and infrastructure edges. Microservice thinking means loose coupling,
  contract-first APIs and independent deployability, **not** forced monolith splits.
- Favour immutability, readonly fields and value types. Use configuration or
  named constants instead of magic values; resolve discoverable values via data
  sources.
- Fetch only properties used in the result. Never swallow errors or return
  error strings as results; propagate to the correct handler with structured,
  appropriately levelled logs.
- Secure from the start: least privilege, input validation, auth/authz, scoped
  tokens, audited dependencies and secrets in vaults.

## Operations and verification

Within the solution's chosen platform:

- Automate recurring resource, identity, network, CI/CD and secret management
  through IaC for reproducibility and drift prevention.
- Prefer OIDC/federated CI/CD credentials and vault-to-compute secret references;
  do not place secrets in IaC state or ordinary environment-variable config.
  Report conflicts with existing approved secret-delivery mechanisms.
- Keep repos independently deployable: no deployment writes into another repo's
  config. Resolve cross-repo values dynamically through data sources and naming.
- Prefer reusable workflows, dev → staging → prod and main-branch staging/prod
  gates. Build once; promote the same artifacts.
- Automate format checks on every PR instead of debating style.
- Name resources consistently using type, domain, service, stage and region;
  split IaC files logically with consistent variable names.

Before proposing a PR, perform an **author self-check, not an independent review
verdict**: run the repo's build, tests, lint and format checks locally. Check
standards, security, edge cases (nulls, empty collections, error paths),
regressions and up-to-date docs. Do not claim unrun checks passed, push failing
code or replace harness reviewers.

## Documentation preferences

Follow solution documentation conventions and ownership. Where the owner can
choose, prefer:

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

## Maintaining preferences

At session end, propose useful skill updates from new patterns, pitfalls, owner
feedback, API quirks and bug causes/fixes. Edit only within approved maintenance
scope; no implicit global-copy/settings changes. Record architecture rationale
in the solution's authorized decision channel, not as a personal override.
Keep maintenance history outside skill bodies.

## Source

Owner-authorized adaptation of the owner's personal `working-style` skill,
not a byte-identical copy. Package changes do not modify that original.
