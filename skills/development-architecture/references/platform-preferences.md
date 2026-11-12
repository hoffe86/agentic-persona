# Scoped platform preferences

Apply **only matching sections** for technologies already selected, within solution
constraints. Verify current APIs/versions in official docs. Do not install
dependencies, deploy resources or change identity permissions without applicable
approval.

## Terraform and GitHub delivery

- Each repo owns its Terraform, CI/CD and GitHub environment variables.
- Resolve resources by name through Terraform `data` sources. The owner's pattern
  is `{type}-{domain}-{stage_short}-{region}[-{service}]`; existing solution
  conventions win.
- Consume shared outputs via tfvars, not hardcoded IDs; no secrets there.
- Use `_`-prefixed files for reusable GitHub workflows.
- Promote the same container image through dev → staging → prod; gate staging/prod
  to main.

## Azure compute and configuration

For compatible Azure solutions:

| Workload | Preference | Context |
| --- | --- | --- |
| APIs/backends | Azure Container Apps | Single-container, Terraform-managed |
| SPAs/static sites | Azure Static Web Apps | Vite output and config in `public/` |

- Entra ID app registrations with custom API scope (`user_impersonation`);
  MSAL.js SPA authentication via `loginRedirect`; OBO (On-Behalf-Of)
  backend-to-Microsoft Graph token exchange. Pre-authorize the SPA on the
  backend app registration.
- Least privilege; avoid admin consent where possible, document permissions
  requiring it and never bypass required consent.
- Link Key Vault secrets to compute. Terraform owns resources, model deployments
  and identity configuration.
- Use GitHub environment variables for **non-secret** build-time config
  (e.g. `VITE_*`); no secrets in browser bundles.
- OIDC/federated CI/CD credentials, not stored passwords.

## AI streaming and tools

For SSE solutions with compatible browser APIs:

- Backend emits typed text-delta, state-snapshot and error events.
- Frontend uses `fetch()` and `ReadableStream`; no wrapper when built-ins suffice.
- Merge out-of-band tool status, permitted reasoning-token metadata and approval
  requests through a concurrent state-snapshot channel. Never expose hidden
  reasoning or secrets, or bypass the real approval mechanism.

For matching tool/service integrations:

- Prefer a thin tool wrapper → service interface → platform SDK implementation.
- Return tool data directly, not through separate REST endpoints.
- Embed small, expensive optional data via parameters such as `includePhoto`
  returning a base64 data URI, within payload/privacy constraints.
- Map tool names to friendly UI status descriptions.

## AI chat presentation and discovery

- Simple questions get 1–2 sentences; chat headings no larger than `###`.
- No filler or repeated questions; Markdown only for readability. Omit boilerplate
  disclaimers, **not** necessary limitations or safety notices.
- Match system-prompt formatting to frontend rendering capabilities.
- Where A2A or another selected standard supports it, publish agent cards with
  capabilities, skills and example prompts. Load dynamically in the frontend,
  not hardcoded lists, so backend additions appear.
