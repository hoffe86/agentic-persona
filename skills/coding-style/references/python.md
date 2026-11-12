# Python coding style

Use only for Python within the entrypoint's scope and authority.

- Check `pyproject.toml`, other project configuration, supported interpreters and
  formatter/linter settings. Repository style wins; use PEP 8/PEP 257 as fallback,
  not a forced 79-column retrofit or compatibility-breaking modernization.
- Prefer `snake_case` functions/modules/variables, `CapWords` classes and
  `UPPER_CASE` constants unless project conventions differ. Use explicit imports,
  not wildcard imports.
- Prefer simple functions/modules and the standard library where suitable.
  Keep comprehensions readable; use ordinary loops when clearer. Dataclasses or
  `Protocol` should express actual data/contracts, not introduce mandatory
  interfaces, class boilerplate or new libraries.
- Follow repository practice for annotations on public/boundary code; use typing
  syntax available in supported interpreters. Do not spread `Any` or
  `# type: ignore` to hide errors. Annotations do not validate external data;
  validate at trust boundaries.
- Avoid mutable default arguments and accidental shared state. Distinguish
  `None` from valid false, zero or empty values rather than replacing them through
  truthiness defaults.
- Use `with`/`async with` for resource lifetimes. Catch specific exceptions;
  preserve the cause with `raise ... from ...` when translating. Avoid bare
  `except`, swallowed errors and fabricated success defaults.
- Use async only where the application uses it. Keep blocking I/O off the event
  loop; await tasks or give them explicit ownership, error handling and lifetime.
  Clean up in `finally`; propagate cancellation after cleanup if caught.
- Avoid import-time side effects such as opening connections or starting work.
  Public docstrings explain behavior, effects and errors, not repeat signatures.

## Sources

- [PEP 8](https://peps.python.org/pep-0008/) and [PEP 257](https://peps.python.org/pep-0257/)
- [Python typing](https://docs.python.org/3/library/typing.html)
- [Asyncio cancellation](https://docs.python.org/3/library/asyncio-task.html#task-cancellation)
