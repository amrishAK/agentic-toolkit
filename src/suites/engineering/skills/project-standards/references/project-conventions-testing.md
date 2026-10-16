# Testing

## Tiers

- Keep tiers separate, each with its own entry-point command: unit, integration, end-to-end, and benchmarks.
- Unit tests sit next to the code under test, following the language's convention.
- Integration tests exercise the public API with real components. Split them into files by behaviour, such as reads, mutations, and errors.

## Default runs need no infrastructure

- The default test command passes on a clean checkout without external services.
- Tests that need infrastructure, such as a database container, are opt-in (ignored or gated). Document the setup, run, and teardown commands beside them.
- Tests that share infrastructure state reset it before each test and run serially. Prefer a fresh, isolated resource per test where possible, such as an in-memory database.

## Fixtures

- Keep fixtures in a documented directory with a README describing each fixture and the behaviour it covers.
- Keep fixtures small and explicit so changes stay reviewable.
- Mark fixture credentials as test-only; never reuse them outside tests.

## Local and CI parity

- Every CI test job has a local equivalent through the shared entry point. See [entry-points.md](./project-conventions-entry-points.md).
- Gates such as coverage thresholds and sanitizers are defined once, in the entry point or CI configuration. Documentation links to that source instead of restating the number.
