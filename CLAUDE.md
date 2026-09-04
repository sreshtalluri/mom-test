# mom-test

Skills repo: `skills/<name>/SKILL.md` are the product; `docs/` is the framework they're compressed from. Keep skills self-contained: everything a skill needs (templates, seed data, personas) lives inside `skills/<name>/`, because skills get symlinked or copied out of the repo. Never reference `docs/`, another skill's dir, or a top-level dir from a SKILL.md.

`discovery/` is the runtime convention: a markdown folder in the *user's* repo that `mom-test-memory`, `mom-test-prep`, `mom-test-debrief`, `mom-test-gate`, `mom-test-roleplay`, and `mom-test-league` read and write. Its rules (ids, `[A<n>±] rung <r>` tags, status merge, write discipline) are in `skills/mom-test-memory/SKILL.md`; keep every skill consistent with that file. Design: `docs/designs/discovery-os-roleplay-league.md`.

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
