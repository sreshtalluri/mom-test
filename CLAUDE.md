# mom-test

Skills repo: `skills/<name>/SKILL.md` are the product; `docs/` is the framework they're compressed from. Keep skills self-contained (they get symlinked out of the repo).

## Skill routing

When the user's request matches an available skill, invoke it via the Skill tool. When in doubt, invoke the skill.

Key routing rules:
- Product ideas/brainstorming → invoke /office-hours
- Strategy/scope → invoke /plan-ceo-review
- Architecture → invoke /plan-eng-review
- Design system/plan review → invoke /design-consultation or /plan-design-review
- Full review pipeline → invoke /autoplan
- Bugs/errors → invoke /investigate
- QA/testing site behavior → invoke /qa or /qa-only
- Code review/diff → invoke /review or /design-review
- Ship/deploy/PR → invoke /ship or /land-and-deploy
- Save/restore context → invoke /context-save or /context-restore
- Backlog-ready spec/issue → invoke /spec
- Customer conversations, interviews, validation → invoke /mom-test (routes to mom-test-* skills)
