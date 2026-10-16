# Using the same Senmonka-kun across agents and chats

Keep **one canonical skill** in `skills/senmonka-kun/`. Do not fork the rules per vendor; adapters only explain how each product loads the same instructions. If a platform cannot install skills, its chat instructions are an explicit *fallback*, not equivalent to automatic skill discovery. All environments remain subject to their own permission model and available tools.

## Codex

Copy `skills/senmonka-kun/` to `.agents/skills/senmonka-kun/` for a project. Verify that its SKILL.md and references are visible, then try an explicit request: "Use senmonka-kun in Deep mode to review this flow without implementing changes." Also test whether normal task phrasing triggers it appropriately. Follow the current [Codex skill instructions](https://developers.openai.com/codex/skills).

## Claude Code

Copy the same folder to `.claude/skills/senmonka-kun/` for a project, or to `~/.claude/skills/senmonka-kun/` for personal use. Test explicit use and natural discovery separately. See [Anthropic Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview).

## Claude web chat

Make an uploadable ZIP:

~~~bash
python3 tools/package_skill.py
~~~

The archive `dist/senmonka-kun.zip` has a single top-level `senmonka-kun/` folder containing SKILL.md and references. In Claude's skill customization UI, upload it as a custom skill, enable it, and test a new conversation. Availability and menu labels depend on plan and settings. See [Claude's help](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

## ChatGPT chat

When native custom skill installation is unavailable in your ChatGPT product/account, you can still provide SKILL.md and relevant references as chat/project files and explicitly instruct the model to follow them. A [project instruction fallback](../adapters/chatgpt-project-instructions.md) is provided. This **does not** make automatic native skill invocation, GitHub sync, or access to private tools available.

If a ChatGPT or API environment supports the Agent Skills format, follow that environment's documented installation path instead. For API use see [OpenAI Skills](https://developers.openai.com/api/docs/guides/tools-skills). Platform capabilities may change; re-check official docs rather than assuming feature parity.

## Acceptance test on every surface

1. Check the skill is discovered or that the whole guidance was actually provided.
2. Run a substantive task requiring independent evidence.
3. Run a small mechanical task to check over-activation.
4. Run a conflicting-decision task: the agent must **propose, not silently change**.
5. Verify no fabricated test result or unauthorized external action.
6. Record product/version, availability of tools, outcome and limitations. Use [evaluation protocol](evaluation.md) to compare against baseline.

Installing a skill never grants permission to edit, merge, deploy, access proprietary data, or alter approved requirements.
