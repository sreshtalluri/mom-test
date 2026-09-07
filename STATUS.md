# mom-test — Project Status

**Last updated:** 2026-09-07

## What's Live (main)

- Ten Claude Code Agent Skills implementing customer discovery per *The Mom Test*: `mom-test` (router), `mom-test-prep`, `mom-test-check-questions`, `mom-test-next-question` (paste-driven live mode), `mom-test-debrief`, `mom-test-memory` (init/status/record), `mom-test-gate`, `mom-test-roleplay` (5 seeded personas), `mom-test-league`, `mom-test-outreach`.
- `discovery/` convention: a markdown evidence folder skills read/write in the *user's own* project — assumptions with rung-tagged evidence, segments, interview files, practice scores.
- Agent-agnostic (v0.3.0): `AGENTS.md` bridge routes any repo-instruction-reading agent (Codex CLI, Cursor, etc.) to the right skill; native loading for Claude Code via `.claude/skills`.
- `docs/` has the full book-derived framework (~29k words) the skills compress from.
- Installable three ways: clone + open, `./install.sh` (symlink, has `--dir` flag), or `/plugin marketplace add`.
- Hand-tested end to end in fresh `claude -p` sessions across all 10 skills, including edge cases (idempotent `init`, collision `-2` suffix, no-`discovery/` fallback, roleplay difficulty scaling).

## What's In Progress

- **mom-test-live companion project** — 🚧 in progress, separate repo
  - Design approved after 3 rounds of adversarial review (docs/designs/live-coach-companion.md)
  - v0 (after-call CLI) built and shipping in `sreshtalluri/mom-test-live` — see that repo's STATUS.md

## Blocking Items

None currently open for this repo.

## Key Files

| File | Why it matters |
|---|---|
| `CLAUDE.md` / `AGENTS.md` | Skill routing rules + the self-containment constraint every `SKILL.md` must respect |
| `skills/mom-test-memory/SKILL.md` | Source of truth for `discovery/`'s write rules (IDs, tags, status merge) — every other skill that touches `discovery/` must stay consistent with it |
| `docs/designs/discovery-os-roleplay-league.md` | Design history for the memory/gate/league layer (v0.2.0) |
| `docs/designs/live-coach-companion.md` | Design history for the mom-test-live companion project |
| `install.sh` | Frontmatter-name-matches-directory check; symlink installer |

## Next Steps (priority order)

1. Get the skills loop in front of real founders (the one test that can't be done solo).
2. Terminal GIF for the README's 60-second demo.
3. `CONTRIBUTING.md` for persona packs, now that `mom-test-live`'s README links back here.
4. Keep `mom-test-live`'s progress cross-linked as it ships.
