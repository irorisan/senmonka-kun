# Security and privacy methods

Use for security design, threat reviews, incident-related investigations and privacy implications. Prioritize lawful, authorized defensive analysis.

## Primary material

Trust boundaries, data flows, auth/authz rules, threat model, dependency versions, logs and audit trails, deployment configuration, data classifications, retention policies, and approved security requirements. Avoid disclosing secrets or personal data in reports.

## Practical methods

1. **Scope assets and adversaries:** identify data/operations at risk and plausible threat capabilities.
2. **Map trust boundaries:** entry points, identities, permissions, data stores, third-party integrations and privileged transitions.
3. **Examine controls:** authentication, authorization per object/action, least privilege, validation, rate limits, auditing, secrets handling and safe defaults.
4. **Failure and abuse cases:** replay, privilege escalation, data leakage, unsafe logging, broken recovery flows and dependency/supply-chain exposure.
5. **Independent validation:** targeted tests, config inspection and authorized scanning; record environment and limitations. Do not claim security solely because tests pass.
6. **Prioritize remediation:** consider exploit preconditions, impact, probability and compensating controls; separate urgent mitigations from architecture proposals.

Follow approved security boundaries. Do not launch intrusive tests against live systems without explicit permission. Do not alter logging/retention/privacy policies as an incidental fix.

Adjacent references: [engineering](engineering.md), [ux](ux.md), [validation](validation.md).
