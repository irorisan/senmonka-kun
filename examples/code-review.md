# Example: engineering review

## Prompt

~~~text
Use senmonka-kun in Deep mode to review the payment-to-order path.
The existing checkout specification is a binding constraint.
Trace source-to-database behavior, check retries/idempotency, reproduce
important failure modes, and identify test gaps. Do not change code or merge.
If a different product flow looks better, propose it separately with evidence.
~~~

## Expected evidence

- Referenced code paths, contracts, migrations, tests and CI state.
- Affected users and reproducible failure conditions.
- Verified findings vs suspected risks; severity with clear rationale.
- Suggested minimal fixes and the independent tests needed.
- No unauthorized implementation or claims of tests having run.
