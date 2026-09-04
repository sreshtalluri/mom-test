# AGENTS.md

This repo is a set of customer-discovery skills built on Rob Fitzpatrick's *The Mom Test*.
Each skill is a plain markdown instruction file at `skills/<name>/SKILL.md` — no special
tool support required beyond reading a file and following its steps.

## If you're an agent with native skill-loading (Claude Code, or anything that adopts the
same [Agent Skills](https://agentskills.io) convention)

You already discovered these via `.claude/skills` or an installed skill directory.
Nothing else to do.

## If you're an agent that reads this file but has no skill loader (Codex CLI, Cursor,
others)

You have no special integration, and you don't need one. When the user's request matches
a row below, **read that file and follow its instructions directly**, exactly as if it
were part of this AGENTS.md. The files are self-contained.

| User wants to... | Read |
|---|---|
| Anything about talking to customers; not sure which skill fits | `skills/mom-test/SKILL.md` |
| Prep for an upcoming customer conversation | `skills/mom-test-prep/SKILL.md` |
| Check or rewrite a list of interview questions | `skills/mom-test-check-questions/SKILL.md` |
| Know what to ask next, given something a customer just said; live-call coaching | `skills/mom-test-next-question/SKILL.md` |
| Debrief a conversation or a batch of them, score it, update assumptions | `skills/mom-test-debrief/SKILL.md` |
| Set up or inspect the `discovery/` evidence folder; record an interview | `skills/mom-test-memory/SKILL.md` |
| Check the evidence before building a feature or picking a direction | `skills/mom-test-gate/SKILL.md` |
| Practice against a simulated customer | `skills/mom-test-roleplay/SKILL.md` |
| See practice score trend and what to practice next | `skills/mom-test-league/SKILL.md` |
| Write a cold email, intro request, or follow-up | `skills/mom-test-outreach/SKILL.md` |

## If you're working on this repo itself (not just using its skills)

- Skills stay self-contained: everything a skill needs (templates, seed data, personas)
  lives inside `skills/<name>/`. Never reference `docs/`, another skill's directory, or
  any top-level directory from inside a `SKILL.md` — skills get copied or symlinked out
  of this repo individually.
- `discovery/` is the runtime convention: a markdown folder created *in a founder's own
  project* by `mom-test-memory`. Its rules (IDs, `[A<n>±] rung <r>` tags, status merge,
  write discipline) live in `skills/mom-test-memory/SKILL.md`; keep every skill that
  touches `discovery/` consistent with that file.
- Full framework and design history: `docs/`, `docs/designs/discovery-os-roleplay-league.md`.
