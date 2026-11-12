---
name: coding-style
description: >-
  Use when implementing, fixing, refactoring or reviewing application code.
  Apply Clean Code and professional enterprise craft with repository-specific
  and language-specific conventions. Optional personal guidance, not compliance
  certification, architecture authority or permission for reviewers to edit.
---

# Coding style

Works independently of core or other personal skills. Solution policies and
security controls determine compliance; personal defaults fill gaps. This skill
grants no edits, tool installation or architecture changes.

## Establish context

Read scoped instructions, accepted decisions and nearby conventions. Identify
supported language/runtime/compiler versions, formatter/linter/analyzer/type-checker
configuration and existing CI/check commands. Respect declared standards; surface
conflicts without inventing universal native-instruction precedence.

Consult [Clean Code Developer](references/clean-code-developer.md) for relevant
cross-language coding, refactoring and review guidance alongside the language
references, not only for explicit CCD requests. It covers all seven grades with
bounded application, not certification or grade selection.

Load only language references for languages changed or under review;
multilingual changes load each applicable reference:
- [C#](references/csharp.md)
- [Python](references/python.md)
- [TypeScript](references/typescript.md)

For other languages, use repository conventions and authoritative documentation;
do not force these references or silently author missing ones. Sources are in
each reference; verify uncertain version-specific claims, not routine guidance.

## Apply to the scoped change

- Use intention-revealing domain names, cohesive functions/modules and clear
  responsibilities. Prefer readable control flow; encapsulate invariants and
  expose explicit contracts/dependencies.
- Apply SOLID and composition where useful, without mandatory interfaces,
  wrappers, patterns or size quotas. Reuse real shared behavior; avoid speculative
  abstractions, premature deduplication and architecture migrations.
- Preserve compatibility and behavior except the requested change. Validate
  trust boundaries; parameterize data access and use established security
  mechanisms. Use specific exceptions or typed failures, never silent success
  fallbacks.
- Make resource ownership, lifetimes and cancellation explicit. Log useful
  structured context without secrets/PII. Avoid needless I/O, full-data loads and
  unbounded operations; measure before optimizing.
- Keep code testable; cover happy, negative, edge and error paths under existing
  contracts/test discipline. Comments explain rationale; document changed public
  behavior.

## Evidence and role boundaries

Authors run existing relevant checks. Never suppress diagnostics or weaken tests
to get green. No global strictness/ruleset/framework/version upgrades or new
linters/type checkers without scoped approval; repository formatting wins.
Reviewers remain read-only: report findings and relevant commands, not execute
the author workflow. Self-checks do not replace independent review. Report actual
evidence, gaps and unresolved conflicts, never unverified compliance.
