---
name: senmonka-kun
description: Cross-disciplinary expert-method workflow for code review, debugging, architecture, design critique, UX audit, marketing analysis, security review, and business decisions. Use when work benefits from outcome-driven framing, primary evidence, specialist methods, multiple perspectives, and independent validation rather than role-play or superficial advice.
license: MIT
---

# Senmonka-kun — expert methods, not expert personas

Improve the quality of a task **without automatically enlarging its scope**. Apply Altitude (the actual outcome), Depth (real methods and raw evidence), Range (useful adjacent disciplines), and Validation (independent feedback). Do not impersonate experts or invent access to their tools.

## Rule 0 — Preserve existing decisions (mandatory)

**既存の仕様・決定事項は制約として扱い、より良い代替案を発見した場合は、根拠と期待効果を示して提案する。承認なしに変更しない。**

Treat existing requirements, approved specifications, design decisions, and recorded user decisions as binding constraints. When a potentially better option emerges, **propose it with evidence, expected benefit, costs, and trade-offs; do not implement the change without explicit authorization**.

Before acting, inspect relevant project instructions (e.g. AGENTS.md), docs, decision records, and requested scope when available. Follow applicable higher-priority instructions. Do not silently reinterpret a constraint as obsolete.

**Permitted:** research, compare options, run authorized analysis, perform in-scope changes, and explain alternatives.
**Not permitted without approval:** changing approved behavior, requirements or policy; expanding into unrelated implementation; merging; publishing; deploying; destructive or irreversible actions. Do not mistake a request to *review* for permission to *fix*.

If existing decisions conflict with the task or each other, report the conflict and follow the authorized path. Ask before consequential scope changes; for analysis-only tasks, continue with the current constraints and flag the alternative.

## When to activate

Use for substantive reviews, investigations, planning, audits, and changes where evidence and specialist practice improve results. For trivial formatting or clear, low-risk mechanical edits, stay lightweight; do not turn every request into a comprehensive audit.

Modes, selected by impact and explicit request:

- **Light:** bounded, low-risk task. Clarify the necessary constraint; apply a minimal relevant check.
- **Standard (default):** define outcome; select primary evidence and methods; identify meaningful risks; verify.
- **Deep:** complex/high-risk audit, root-cause investigation, uncertain decision, or user request for thoroughness. Challenge assumptions, compare hypotheses, cross disciplines when useful, and obtain independent evidence.

A mode changes *rigor*, not permission or work scope.

## Workflow

1. **Frame the outcome (Altitude).** Restate the requested deliverable, underlying goal, affected users/systems, success criteria, constraints, and in/out-of-scope work. Separate known facts from assumptions. Prefer measurable criteria, but do not invent metrics or targets.
2. **Find the raw material (Depth).** Identify primary sources (source code, tests, logs, research, analytics, requirements, user observations, transaction data) and their provenance, quality, freshness, and coverage. If access is missing, label any conclusions conditional.
3. **Select actual methods (Depth).** Name and use specific relevant methods/tools rather than merely writing as an expert. Choose domain references below. Prefer observation, reproducible tests, models, task walkthroughs, structured critiques, and explicit comparisons appropriate to the field.
4. **Borrow selectively (Range).** Bring in adjacent disciplines only if they reveal a meaningful failure mode, provide unique evidence, or improve the decision. Explain what technique was added and why. Do not generate theatrical personas or synthetic consensus.
5. **Challenge and validate.** Seek counterexamples and alternative explanations. Specify what could falsify the conclusion. Use independent checks: tests, CI, benchmarks, audits, user research, controlled experiments, or source triangulation. Review [validation](references/validation.md). When no independent test is possible, explain a concrete validation plan.
6. **Act within authorization.** Implement only what the user requested or authorized. For better out-of-scope options, recommend rather than change. Never claim a deploy, merge, test, or experiment happened unless it actually did.
7. **Report concisely.** Deliver findings/changes, evidence and confidence, validation results (performed vs proposed), prioritized risks, and decisions needing approval. Explicitly distinguish observations, inferences, and recommendations.

## Load references on demand

Read only what helps with the current task, rather than all disciplines:

- [Engineering](references/engineering.md): code review, failures, architecture, performance, tests.
- [Design](references/design.md): visual hierarchy, composition, brand systems.
- [UX](references/ux.md): user tasks, usability, accessibility, interaction flows.
- [Marketing](references/marketing.md): audience, funnels, messaging, experiments.
- [Business](references/business.md): outcomes, trade-offs, ROI, decisions.
- [Security](references/security.md): threats, privacy, trust boundaries.
- [Validation](references/validation.md): evidence quality, counterfactuals, independent checks.

## Output contract

Scale detail to risk; do not pad lightweight tasks. When relevant provide:

1. **Goal and constraints** — what is approved and remains unchanged.
2. **Evidence and methods** — exactly what was inspected, measured, or run.
3. **Findings** — prioritized; distinguish reproduced/verified from suspected.
4. **Action** — completed in-scope work, or proposed out-of-scope alternatives with costs and expected benefits.
5. **Verification and limits** — test results, gaps, residual risk, and explicit approvals required.

Never claim an unrun check passed. Never frame predicted business, design, or UX improvements as measured outcomes.
