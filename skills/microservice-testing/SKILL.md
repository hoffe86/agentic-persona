---
name: microservice-testing
description: >-
  The owner's optional guidance for test strategy, implementation and read-only
  review of existing HTTP/event-driven microservices. Use for unit, gateway or
  persistence integration, component, contract and end-to-end boundaries,
  coverage gaps, risk-based plans or scoped test changes. Does not select
  architecture or stack.
---

# Microservice testing

## Scope and authority

This is on-demand personal guidance, not project policy. Solution stack, versions,
test-first/test-after discipline, naming, check commands and accepted decisions
govern; safety, approvals and caller permissions win. Surface conflicts.
This grants no authority to change architecture, dependencies, settings, resources,
accounts or test APIs, install tools or activate skills. Infrastructure/pipeline
changes belong to their authorized owner.

Planning stays planning. Coding authors implement and own their tests;
read-only reviewers report findings and reference commands without edits, builds
or execution. Implement only the requested behavior/change, not every category.

## Owner preferences

Owner choices, not Martin Fowler requirements:

- Express scenarios as **Given–When–Then** using existing frameworks and naming:
  names, comments or sections suffice. Use adopted BDD frameworks; do not require
  Gherkin, `.feature` files, a parser/library, class-per-unit or `Test` suffix.
- Prefer **in-process component tests (IPCT)** when they prove the risk;
  use out-of-process tests when packaging, startup or real-network behavior matters.
- Focus E2E on critical **persona journeys**.
- Prefer automated, repeatable infrastructure and data setup/cleanup through
  approved facilities; missing facilities are gaps, not provisioning permission.

## 1. Establish the claim

Read scoped instructions, existing tests, accepted contracts, CI and check commands.
Identify changed business behavior, consumers, dependency owners, relevant versions
and costly failures. Ask only for material unknowns; mark evidence gaps.

Classify by **boundary and evidence**, not mocks, framework or process count.
The pyramid is a cost/feedback heuristic: favor fast, focused tests and a few
high-value broad ones, not fixed ratios or mandatory contract/component ordering.

## 2. Choose the smallest boundary that proves the risk

| Category | Real vs double | Evidence and limits |
|---|---|---|
| Unit | Cohesive behavior, possibly several related classes; real collaborators or doubles; control slow/nondeterministic I/O | Decisions, transformations, validation and orchestration branches. Solitary and sociable units are valid. |
| Narrow gateway integration | Real gateway/client and serialization against a controlled protocol server or approved provider environment | Request/response mapping, verb/path, status, auth headers, errors and timeouts. A stub cannot prove actual provider compatibility. |
| Narrow persistence integration | Real adapter/driver and relevant database engine/version; owned fixtures | Mappings, constraints, transactions and stored results via fresh, ORM-cache-bypassing reads. In-memory substitutes cannot prove production database behavior. |
| Service component | One service's real composition; other services doubled; storage real or doubled per claim | Observable behavior/collaboration. Whole-host claims require exercised routing, middleware and DI; direct-class calls may prove only a subsystem. Doubled storage leaves database compatibility to persistence tests. |
| Contract | Actual shared/versioned consumer expectations verified at the real provider boundary with controlled state | Supported consumers' interaction compatibility. Real HTTP with mocked internals alone proves an adapter, not consumer-driven compatibility. |
| E2E | Explicit journey ends and real service chain; disclose excluded/stubbed third parties | Critical outcome and deployed wiring within those ends, not excluded-provider compatibility. |

Never mock the client/driver under test. Assert verb/path directly or use a
strict protocol stub; **verify interaction and result**. An ignored 404 proves
nothing.

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

## 3. Cover behavior

- Cover observable business logic: happy, negative and meaningful edge cases,
  including conditional orchestration's call/no-call outcomes, not mechanical tests
  per method or only extracted predicates. Include invalid/empty/boundary input,
  forbidden access and dependency failures. Assert specific error types/contracts,
  not any exception; success must reject unexpected errors.
- Separate async schema/version compatibility from broker delivery semantics.
  Where relevant, cover duplicates/redelivery, ordering, idempotency, correlation,
  eventual consistency, retry limits, timeouts, dead letters and partial failures.
  Do not assume exactly-once delivery without a verified system contract.
- Security (including authentication/authorization), performance and resilience
  are cross-cutting risk dimensions, not extra levels or mandatory at every level.
- **Purposes are not levels:** smoke checks quick health; regression protects
  intended behavior (not only output comparison); specification examples document
  agreed behavior; compatibility covers supported old/new consumers, providers
  and schemas. Retire compatibility tests when support ends, not merely with age.
- Exploratory testing combines human learning, design and execution with a charter,
  timebox and recorded evidence; automation may assist, but manually triggering it is not
  exploration. BDD/SBE means collaborative discovery, formulation and automation,
  not just syntax; controlled real databases are valid when the risk warrants.

## 4. Keep execution deterministic and safe

Use bounded polling of observable, correlated async state with a deadline and
useful timeout diagnostics, never fixed sleeps as proof. Separate functional
completion from performance/SLO timing.

Use uniquely owned ephemeral fixtures and synthetic data; automate teardown/finally
cleanup even on failure. Never clear shared databases. Drop databases only within
authorized, provably owned, unique private fixtures. Prefer existing setup;
do not introduce public reset APIs.
An already-approved privileged setup API must be guarded and non-production.

Production smoke needs **explicit approval**, safe non-destructive synthetics,
approved sandbox accounts and no real PII. Reachability is not authorization;
accounts, permissions and cloud resources require separate approval.

## 5. Deliver only the requested evidence

Return a compact plan/gap assessment or scoped implementation with test evidence:

- **Per behavior/risk:** boundary/level, real vs doubles/exclusions,
  Given–When–Then assertions (success and meaningful failure), owner and run stage.
- **Commands/stages:** only repository/user-supplied commands; distinguish proposed
  from configured stages and planned from executed checks.
- **Evidence/gaps:** results, unsupported versions/boundaries, missing
  fixtures/approvals and residual risks. Claim no unproven coverage/compatibility.
- **Next action:** smallest requested change or human decision needed.
  Never weaken tests to get green.

## Sources

Primary guidance, paraphrased; platform-specific examples are not stack policy.

- **Toby Clemson**, [*Testing Strategies in a Microservice Architecture*](https://martinfowler.com/articles/microservice-testing/),
  martinfowler.com, 18 November 2014 — boundaries, pyramid and E2E;
  [broad contract definition](https://martinfowler.com/articles/microservice-testing/testing-contract-introduction.html).
- **Ham Vocke**, [*The Practical Test Pyramid*](https://martinfowler.com/articles/practical-test-pyramid.html)
  — credits **Mike Cohn** with the pyramid; cautions against rigid layer names.
- **Martin Fowler**, [*Unit Test*](https://martinfowler.com/bliki/UnitTest.html)
  (solitary/sociable units) and [*Exploratory Testing*](https://martinfowler.com/bliki/ExploratoryTesting.html).
- **Pact**, [*What is Pact good for?*](https://docs.pact.io/getting_started/what_is_pact_good_for)
  and [*Contract versus functional tests*](https://docs.pact.io/consumer/contract_tests_not_functional_tests)
  — interaction matching versus functional, side-effect and performance evidence.
- **Cucumber**, [*BDD overview*](https://cucumber.io/docs/bdd/) — collaborative
  discovery, formulation and automation.
