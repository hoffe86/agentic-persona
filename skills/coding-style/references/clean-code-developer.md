# Clean Code Developer (CCD)

Original, actionable paraphrases of the official
[grade overview](https://clean-code-developer.de/die-grade/) and
[value system](https://clean-code-developer.de/das-wertesystem/).
CCD connects **evolvability** (keep change affordable), **correctness** (verify
required behavior), **production efficiency** (reduce delivery waste) and
**continuous improvement** (learn from feedback).
The seven colors mark practice focus, not earned certification, mastery or
developer superiority. Use relevant guidance together, not a grade selector.
These summaries attribute CCD; its articles, examples and source documentation
remain their owners' work, not relicensed under this package's MIT license.

## Bounded agent application

The grade membership below is CCD's; these concise actions adapt it to scoped
coding, refactoring and review, not universal CCD or enterprise compliance.

- Solution versions, constraints, conventions and approved design govern. Apply
  SOLID idiomatically across languages, not with an interface for every class.
  This reference is self-contained; no other personal testing skill is required.
- Solution coverage targets and test commands prevail. Coverage locates gaps;
  it does not prove correctness. CCD's numerical coverage targets, bracelet cycles,
  learning budgets and reading quotas are not agent gates or required cadences.
- Cleanup and refactoring stay within authorized touched scope. VCS, tracking,
  CI and CD practices grant no pipeline edits, commits, pushes, issue creation,
  deployment or publication rights. Preserve role boundaries and personal consent.
  Author self-checks do not replace independent review; reviewers stay read-only.
- Human learning practices are recommendations, discussion or authorized
  knowledge capture. Never invent participation or learning history, publish
  private material, or automatically publish externally or persist preferences.

## [Black — 0](https://clean-code-developer.de/die-grade/schwarzer-grad/)

Interest and preparation, not mastery: learn the values, examine current habits
and prepare to practise deliberately. No additional named principles or practices.

## [Red — 1](https://clean-code-developer.de/die-grade/roter-grad/)

### Principles

- **Don't Repeat Yourself (DRY):** Give the same knowledge one authoritative
  representation; do not merge code merely because it looks similar.
- **Keep it simple, stupid (KISS):** Choose the simplest clear solution that meets
  current requirements; remove needless indirection, not necessary safeguards.
- **Beware of Premature Optimization:** Establish a measured bottleneck before
  trading clarity for speed; verify the improvement against representative work.
- **Favour Composition over Inheritance (FCoI):** Assemble behavior from explicit
  collaborators rather than deep hierarchies; retain inheritance where
  substitutability and the language make it appropriate.
- **Integration Operation Segregation Principle (IOSP):** Separate orchestration
  from operations containing logic or I/O. Still test orchestration ordering,
  conditional invocation and error propagation; separation is no test exemption.

### Practices

- **Boy Scout Rule:** Leave authorized touched code clearer than you found it;
  make small safe improvements, not unrelated cleanup.
- **Root Cause Analysis:** Trace a failure beyond its symptom to its cause;
  address it and add a regression check where testable.
- **Version Control System:** Use the existing history and diffs to understand
  changes and prepare coherent, reversible units; writing history requires approval.
- **Simple Refactorings:** Use small behavior-preserving transformations, such as
  renaming or extracting a focused function; verify contracts before and after.
- **Daily Reflection:** Recommend reviewing what helped or hindered recent work
  and choosing one adjustment; capture observations only when authorized.

## [Orange — 2](https://clean-code-developer.de/die-grade/orangener-grad/)

### Principles

- **Single Level of Abstraction:** Keep a function's steps at one conceptual
  level; separate low-level mechanics from the workflow they support.
- **Single Responsibility Principle (SRP):** Group behavior by a coherent reason
  to change; separate unrelated responsibilities without splitting every small task.
- **Separation of Concerns (SoC):** Keep distinct concerns behind explicit
  boundaries so changes to one do not spread through unrelated behavior.
- **Source Code Conventions:** Follow local formatting and naming rules; choose
  names that express domain intent. Write purposeful comments explaining rationale,
  constraints or surprises, not restating code or preserving obsolete narratives.

### Practices

- **Issue Tracking:** Tie work, acceptance criteria and known defects to the
  existing tracker when authorized; otherwise propose the needed record, not a new tool.
- **Automated Integration Tests:** Exercise real interactions at selected
  boundaries with controlled dependencies; check contracts, failure handling and
  cleanup without relying on uncontrolled live services.
- **Read, Read, Read:** Recommend relevant technical reading, question its
  assumptions and discuss applicable lessons; report only material actually consulted.
- **Reviews:** Use pair programming for immediate feedback and independent code
  review for another perspective; request the appropriate review rather than
  labeling an author's self-check independent.

## [Yellow — 3](https://clean-code-developer.de/die-grade/gelber-grad/)

### Principles

- **Interface Segregation Principle (ISP):** Give consumers only the contract
  they need; split unrelated capabilities when coupling hurts, not by class count.
- **Dependency Inversion Principle (DIP):** Keep high-level policy independent
  of infrastructure details through stable, consumer-relevant contracts; wire
  implementations at the established boundary.
- **Liskov Substitution Principle (LSP):** Replacements must preserve observable
  promises, accepted inputs and invariants; do not strengthen preconditions or
  weaken guarantees behind the same contract.
- **Principle of Least Astonishment:** Make names, defaults, side effects and
  failure behavior match reasonable caller expectations and established conventions.
- **Information Hiding Principle:** Hide volatile implementation decisions behind
  stable contracts; expose what callers need without leaking internal representation.

### Practices

- **Automated Unit Tests:** Assert observable behavior of focused units, including
  boundaries and failures; keep tests deterministic, isolated and fast.
- **Mockups (test doubles):** Substitute dependencies selectively for control or
  otherwise hard-to-reproduce failures. Prefer real collaborators when practical;
  mocks are neither mandatory for every collaborator nor a definition of test level.
- **Code Coverage Analysis:** Inspect uncovered paths to find missing behavioral
  checks; judge assertion quality too, since execution alone does not establish correctness.
- **Participation in Professional Events:** Recommend relevant peer events and
  discuss lessons the person supplies; never imply attendance or learning that did not occur.
- **Complex Refactorings:** Break structural improvements into safe,
  behavior-preserving steps with contract checks; stop for approval when scope or
  architecture authority would be exceeded.

## [Green — 4](https://clean-code-developer.de/die-grade/gruener-grad/)

### Principles

- **Open Closed Principle (OCP):** Extend through stable boundaries when actual
  variation warrants them; do not invent extension points for hypothetical needs.
- **Tell, don't ask:** Place decisions with behavior that owns the relevant
  invariants instead of exporting state for callers to manipulate; getters,
  DTOs and functional transformations are not categorically wrong.
- **Law of Demeter (LoD):** Avoid coupling callers to collaborators' internal
  object graphs; offer a purposeful boundary when needed, not a blanket ban on
  pure-data traversal or functional code.

### Practices

- **Continuous Integration (CI):** Integrate small compatible changes frequently
  through the existing build and test feedback; surface failures promptly without
  changing pipelines or pushing without authorization.
- **Static Code Analysis:** Run the configured analyzers and investigate useful
  diagnostics; fix causes instead of suppressing warnings merely to pass.
- **Inversion of Control Container:** When beneficial, use existing dependency
  composition, root and lifetime conventions. Do not mandate a new or custom
  container, service locator or framework.
- **Share Experience:** Recommend peer discussion or authorized knowledge capture
  of concrete lessons; respect confidentiality and consent before sharing externally.
- **Error Measurement:** Examine escaped or customer-reported defects after an
  iteration using comparable definitions and trends; improve the team's process,
  not personal blame or developer rankings.

## [Blue — 5](https://clean-code-developer.de/die-grade/blauer-grad/)

### Principles

- **Design and Implementation Don't Overlap:** Separate reasoning about
  responsibilities and contracts from detailed internals; continue architectural
  thinking and feed discoveries back through the appropriate decision authority.
- **Implementation Reflects Design:** Make the approved structure and boundaries
  recognizable in code; surface mismatches and seek feedback rather than quietly
  drifting or preserving an unsuitable design.
- **You Ain't Gonna Need It (YAGNI):** Implement current demonstrated needs;
  defer speculative features, abstractions and configuration until justified.

### Practices

- **Design before Implementation:** Understand responsibilities, contracts and
  likely interactions before coding, with thought proportionate to risk; no
  automatic ADR or documentation creation.
- **Continuous Delivery (CD):** Keep changes reproducibly packaged, installable
  and releasable through the selected process; readiness is not automatic
  production deployment or permission to release.
- **Iterative Development:** Revisit a solution using feedback, tests and
  observation to improve it; an iteration need not add a new capability.
- **Incremental Development:** Deliver usable vertical slices that add capability
  end to end; avoid accumulating disconnected layers with nothing usable.
- **Component Orientation:** Define black-box contract boundaries adapted to the
  selected language and runtime; do not mandate .NET assemblies, separate
  projects, repositories or microservices.
- **Test First:** Where approved, write executable consumer-perspective examples
  before implementation. Respect the repository's chosen testing approach; visibly
  record non-application or conflict instead of switching a test-after project or
  claiming universal CCD compliance.

## [White — 6](https://clean-code-developer.de/die-grade/weisser-grad/)

Combine all principles and practices as appropriate, reflect on their effects
and loop back to red or earlier stages for renewed practice. White adds no named
items and is not a graduation from learning.
