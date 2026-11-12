# TypeScript coding style

Use only for TypeScript within the entrypoint's scope and authority.

- Respect `tsconfig` target, libraries and module resolution, the supported
  compiler and actual browser/Node/framework environment. Follow `package.json`
  scripts and configured linters/formatters. Do not mix runtime APIs or flip
  strictness globally as a side effect.
- Work with existing strict/null checks. Prefer properly inferred implementation
  types and explicit boundary contracts, not annotations that merely repeat
  obvious types. Use `unknown` for untrusted values, then validate at runtime and
  narrow before use.
- `any`, postfix `!`, unsafe/double casts and `@ts-ignore` are not validation.
  Type assertions and non-null assertions are erased; they cannot establish
  runtime safety. Fix the contract or validate the input rather than hiding
  uncertainty.
- Use discriminated unions and exhaustive handling for real variants; use
  `never` checks where they expose missing cases. Avoid needless generics,
  wrappers and abstractions. Distinguish `null`/`undefined` from valid false,
  zero and empty values. `const` prevents rebinding, and `readonly` restricts
  writes through the declared type; neither guarantees deep immutability.
- Await, return or handle promises. Fire-and-forget work needs explicit
  ownership, error handling and lifecycle. Cover asynchronous error paths;
  narrow caught `unknown` values rather than assuming every thrown value is an
  `Error`. Preserve useful error context when propagating or translating.
- Propagate cancellation only through APIs that actually support it; verify the
  selected runtime's capabilities rather than assuming browser/Node parity.
- Prefer simple functions and composition. Follow repository naming/formatting;
  no universal `I`-prefixed interfaces, mandatory classes, quote/semicolon rules,
  libraries or frameworks.

## Sources

- [Narrowing and exhaustiveness](https://www.typescriptlang.org/docs/handbook/2/narrowing.html)
- [Strict options](https://www.typescriptlang.org/tsconfig/#strict)
- [Type assertions](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#type-assertions)
