# Operations preferences

Optional personal guidance, subordinate to solution decisions, harness
safety and approvals. It never authorizes new platforms or resources.

Within the solution's chosen platform and existing consent boundaries:

- Automate recurring resource, identity, network, CI/CD and secret management
  through IaC for reproducibility and drift prevention.
- Prefer OIDC/federated CI/CD credentials and vault-to-compute secret references;
  do not place secrets in IaC state or ordinary environment-variable config.
  Report conflicts with existing approved secret-delivery mechanisms.
- Keep repos independently deployable and promote artifacts as described in
  the `development-architecture` skill's multi-repo ownership and
  promotion section.
- Automate format checks on every PR instead of debating style.
- Name resources consistently using type, domain, service, stage and region;
  split IaC files logically with consistent variable names.
