# Contract testing guidance

Apply within the scope and authority rules of the `microservice-testing` skill.

Verify supported consumer/provider versions in the provider pipeline, including
rolling deployments, not just latest heads. Mocked provider business logic can
support a limited adapter claim with functional tests elsewhere. Non-participating
external/public providers need a stated fallback (schema checks, controlled
sandbox/smoke, real-integration evidence) and compatibility gap.
Do not require a particular contract-testing library.

Toby Clemson's broad contract definition includes data, side effects, performance
(latency/throughput) and concurrency. Interaction/schema matching, including Pact,
does not prove provider functionality or these non-schema obligations. Use
appropriate component, integration, load or resilience evidence with measurable
budgets.
