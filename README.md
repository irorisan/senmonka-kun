# 専門家くん / Senmonka-kun

**A cross-disciplinary Agent Skill that makes AI use expert methods—not just expert-sounding words.**

[日本語](README.ja.md) | English

Senmonka-kun helps AI agents tackle ambiguous, consequential work in **engineering, design, UX, marketing, business strategy, and security**. Inspired by the ideas of **Altitude** (work toward the outcome), **Depth** (use genuine expert methods), and **Range** (borrow useful techniques across disciplines), it adds independent **validation** and explicit **decision boundaries**.

It is a reusable process skill, not a role-playing prompt, autonomous decision-maker, or replacement for domain-specific policies.

## Non-negotiable rule

**Treat existing specifications and recorded decisions as constraints. When a better alternative emerges, propose it with supporting evidence and expected benefits. Do not change those decisions without explicit approval.**

Researching options, recommending improvements, and carrying out already-authorized work are allowed. Unauthorized scope expansion, policy/requirement changes, merging, publishing, or deployment are not.

## What it does

1. **Altitude:** Identify the user's outcome, explicit request, boundaries, and success criteria.
2. **Depth:** Examine primary evidence and apply practical methods used by specialists.
3. **Range:** Add only the other disciplines that materially improve the decision.
4. **Validation:** Use tests, observations, experiments, or independent checks; separate verified facts from hypotheses.
5. **Control:** Preserve approved constraints and seek approval before changing them.

Choose proportional effort: **Light** for contained low-risk tasks, **Standard** for ordinary analysis or improvement, **Deep** for audits, root-cause investigations, and high-risk or unclear work. More ambition means more rigorous thinking—not automatically more files, features, or work.

## Installation

The reusable skill lives in [skills/senmonka-kun](skills/senmonka-kun). Copy that directory into the skill-discovery location supported by your agent, for example:

- Codex (project-scoped): PROJECT/.agents/skills/senmonka-kun/
- Claude Code (project-scoped): PROJECT/.claude/skills/senmonka-kun/

Each installed directory should contain SKILL.md and the references/ directory. Exact discovery, invocation, and permissions vary by agent; consult your agent's documentation. The skill **does not grant tools, data access, or permission** to perform actions.

The SKILL.md file follows the [Agent Skills specification](https://agentskills.io/specification).

## Usage

Explicit invocation, if your agent supports skill names:

~~~text
Use senmonka-kun in Deep mode to review this checkout flow.
Keep the approved requirements unchanged. Identify root causes, test assumptions,
and propose improvements with evidence. Do not deploy or merge.
~~~

You can also describe the intent naturally:

~~~text
Review this landing page using actual UX, design, and marketing methods.
First clarify the success criterion; distinguish measured findings from assumptions.
~~~

For examples across disciplines, see [examples/](examples/) and the [Japanese guide](README.ja.md).

## Architecture

~~~text
skills/senmonka-kun/
├── SKILL.md
└── references/
    ├── engineering.md
    ├── design.md
    ├── ux.md
    ├── marketing.md
    ├── business.md
    ├── security.md
    └── validation.md
~~~

Read only the reference files relevant to the task. Project-specific requirements should stay in the host project's instructions and documentation, not in this public skill.

## Validation

Run the dependency-free static checks:

~~~bash
python3 -m unittest discover -s tests -v
~~~

These checks validate structure and key rules; they cannot prove that a given AI agent will follow instructions. Actual outcomes require scenario testing and independent evidence. See [tests/scenarios.md](tests/scenarios.md).

## Source, license, and boundaries

Conceptual inspiration: Felix Rieseberg, [How to Be More Ambitious: A Tutorial for Humans with Models](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/). This repository is an independent implementation and is not affiliated with the author or AI vendors.

Licensed under [MIT](LICENSE). Domain references are guides, not professional certification. Do not invent evidence, measurements, user research, or claims of approval.
