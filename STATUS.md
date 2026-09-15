# mom-test — Project Status

**Last updated:** 2026-09-15

## What's Live (main)

- Ten agent-neutral skills implementing customer discovery per *The Mom Test*: `mom-test` (router), `mom-test-prep`, `mom-test-check-questions`, `mom-test-next-question` (paste-driven live mode), `mom-test-debrief`, `mom-test-memory` (init/status/record), `mom-test-gate`, `mom-test-roleplay` (5 seeded personas), `mom-test-league`, `mom-test-outreach`.
- `discovery/` convention: a markdown evidence folder skills read/write in the *user's own* project — assumptions with rung-tagged evidence, segments, interview files, practice scores.
- Agent-agnostic (v0.3.0): `AGENTS.md` bridge routes any repo-instruction-reading agent (Codex CLI, Cursor, etc.) to the right skill; native loading for Claude Code via `.claude/skills`.
- `docs/` has the full book-derived framework (~29k words) the skills compress from.
- Installable three ways: clone + open, `./install.sh` (symlink, has `--dir` flag), or `/plugin marketplace add`.
- Hand-tested end to end in fresh `claude -p` sessions across all 10 skills, including edge cases (idempotent `init`, collision `-2` suffix, no-`discovery/` fallback, roleplay difficulty scaling).

## Completed in the release-preparation branch

- Added `CONTRIBUTING.md` with persona submission steps and skill verification guidance.
- Added a 60-second README animation, its generator, and a text equivalent. It is
  explicitly a scripted illustration with fictional data, not a founder trial.
- Fixed the installer to preserve unrelated files/directories/links, avoid nested
  links on reinstall, validate all skills before installing any, and handle a
  missing `--dir` argument. Uninstall removes only links owned by this checkout.
- Five real installer regression scenarios pass locally. Linux/macOS CI is added,
  including manifest JSON checks. These checks do not replace agent hand-testing.

## What's In Progress

- **mom-test-live companion project** — 🚧 in progress, separate repo
  - Design approved after 3 rounds of adversarial review (docs/designs/live-coach-companion.md)
  - v0 (after-call CLI) implemented locally in `sreshtalluri/mom-test-live`: verified
    model caching, offline/bundled Whisper inference, local speech detection,
    caption import, private output, and the existing agent hand-off.
  - Tested with real recorded speech across six formats and actual terminal consent
    scenarios; cross-platform CI/release workflows added. Release publication and
    real founder acceptance remain pending — see that repo's STATUS.md.

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
2. Review and merge the release-preparation PR after CI.
3. Keep `mom-test-live`'s progress cross-linked as it ships.

The companion includes a founder-trial protocol and blank outcome log at
`docs/founder-trials.md`. No real founder results have been supplied in this audit;
that acceptance work remains open.
