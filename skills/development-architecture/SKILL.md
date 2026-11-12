---
name: development-architecture
description: >-
  The owner's optional architecture preferences: built-ins versus custom code,
  multi-repo ownership, environment promotion and API contracts. Use for personal
  architecture, IaC, CI/CD and operations guidance; consult the scoped reference
  only for solutions already using the matching Azure, Terraform, SPA or AI
  streaming/agent technologies. Does not choose a stack for unrelated solutions.
---

# Development and architecture preferences

## Applicability

Follow solution technologies, versions, architecture decisions and documentation
conventions. These optional preferences are subordinate to
solution technical constraints and harness safety, approvals and role boundaries.
They may tighten consent, never waive controls. Surface unresolved conflicts.
This skill does not authorize new clouds, frameworks, dependencies or topologies;
there is no blanket .NET, Azure or microservices default.

## Design choices

- Prefer standards and framework built-ins. Choose a small direct implementation
  over a third-party abstraction **when the abstraction adds more complexity than
  value**: fewer dependencies, clearer control, easier debugging. Do not hand-roll
  security or discard useful existing libraries.
- Extend existing APIs/tools with parameters when their contracts fit; avoid
  redundant endpoints, including REST controllers for data already returned.
- Prefer established protocols (such as OpenAPI and, where selected, AG-UI/A2A)
  over proprietary alternatives.

## Multi-repo ownership and promotion

- Keep repos self-contained and independently deployable, owning IaC, delivery
  config and environment variables. No deployment writes into another repo's config.
- Resolve shared resources through data sources and naming, not hardcoded IDs.
  Prefer type, domain, stage, region and, where relevant, service segments;
  respect solution conventions.
- Prefer reusable workflows, dev → staging → prod with main-gated staging/prod,
  and build-once promotion of the same container/artifact.

## Operations

For IaC, CI/CD, secret handling and resource naming, read the
[operations preferences](references/operations.md).

## API contracts

- Prefer stateless requests with client-supplied context for horizontal scaling
  without session affinity **where the protocol and data/security model permit**.
  Preserve required server state and validate client context.
- Share frontend/backend event and payload schemas in a common contract location.
- Prefer optional base64 data URIs in JSON over extra calls/endpoints for small
  binaries, within payload/privacy/protocol constraints. Large or streaming
  binaries may need the existing binary interface.
- Use a checklist to synchronize permissions across app registration, IaC and
  docs; change only authorized locations.

## Scoped platform and AI guidance

Read [platform preferences](references/platform-preferences.md) only for the
matching technologies already selected: Terraform/GitHub naming and delivery,
Azure compute/identity/configuration, and AI SSE/tools/UI/agent discovery.
It is not a general deployment recipe or permission to migrate stacks.

## Source

Owner-authorized adaptation of the owner's personal `development-architecture`
skill, not a byte-identical copy. Package changes do not modify that original.
