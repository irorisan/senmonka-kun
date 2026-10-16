# Engineering methods

Use for code review, defect investigation, architecture and technical change evaluation. Consult project architecture/docs first; preserve approved behavior.

## Primary material

Source files and call sites, version history, interfaces, schema and migrations, tests, CI logs, reproducible inputs, runtime telemetry. Source code is stronger evidence for behavior than a description; tests are evidence of the cases they exercise, not proof of completeness.

## Practical methods

1. **Trace execution paths:** identify entry points, side effects, state boundaries, error handling, data ownership and failure modes.
2. **Reproduce first:** create a minimal failing case; distinguish regression, environment mismatch and incorrect specification.
3. **Test boundaries:** null/empty states, invalid inputs, concurrency, idempotency, retries, timeouts, rollback, API compatibility and migrations.
4. **Check maintainability:** coupling, duplication, contract clarity, operational visibility, upgrade path and documented invariants.
5. **Measure performance:** establish a baseline, use profiling/tracing, change one meaningful factor at a time, remeasure the same workload.
6. **Independent review:** run relevant linters, type checks, unit/integration/E2E tests and CI when accessible; inspect diffs from a second perspective.

## Reporting

For each finding: severity, affected paths, reproduction/evidence, impact, and minimal safe remediation. Severity is about user/system impact and exploitability—not stylistic preference. Distinguish code defects from design trade-offs. Do not quietly rewrite requirements while fixing implementation.

Adjacent references: [security](security.md), [validation](validation.md), [ux](ux.md).
