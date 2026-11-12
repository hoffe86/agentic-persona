# C# coding style

Use only for C# within the entrypoint's scope and authority.

- Honor `global.json`, project `TargetFramework`/`TargetFrameworks` and
  `LangVersion`, `.editorconfig`, nullable settings and analyzer conventions.
  Use supported syntax; no blanket latest/.NET version mandate or automatic
  settings changes. Microsoft's documentation conventions are adaptable
  examples, not a universal enterprise specification.
- Follow established naming: normally PascalCase types/public members and
  camelCase locals; avoid private-field naming churn. Use the `Async` suffix
  where convention applies. Use `var` when the type is evident; choose modern
  syntax for readability, not novelty.
- Represent nullability honestly and validate runtime inputs; annotations alone
  do not protect boundaries. Do not use `!` or warning pragmas merely to compile.
  Choose records, value types and `readonly` only when equality, copying and
  mutation semantics fit; do not convert every DTO.
- Use `async`/`await` for I/O and propagate `CancellationToken` through supporting
  APIs. Avoid blocking `.Result`/`.Wait()` and `async void` except required event
  handlers. Do not wrap I/O indiscriminately in `Task.Run`; follow application
  or library context for `ConfigureAwait`, not a blanket policy.
- Own and dispose resources with `using`/`await using` where supported. Respect
  dependency-injection lifetimes and the disposal owner; do not indiscriminately
  dispose injected/shared objects.
- Follow the specific exception or typed-error contract. Catch when recovery
  or translation is meaningful; preserve the stack with `throw;` when rethrowing.
  Ensure cleanup without swallowing errors or turning cancellation into success.
- Keep LINQ readable while accounting for deferred execution, repeated
  enumeration, allocation and query-provider boundaries. Do not hide lifetime or
  query problems with eager full-data loads.

## Sources

- [Microsoft C# conventions](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/coding-style/coding-conventions)
- [Microsoft exception practices](https://learn.microsoft.com/en-us/dotnet/standard/exceptions/best-practices-for-exceptions)
