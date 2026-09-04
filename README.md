# The Mom Test → Founder Conversation Skills

Rob Fitzpatrick's *The Mom Test*, turned into skills your coding agent runs, with a
`discovery/` folder in your repo so what you learn in one customer conversation changes
what the agent says in the next. Not a summary of the book. A loop.

AI interview tools run the conversation for you. This does the opposite: **you** stay in
the room, the agent makes you harder to fool, and the evidence compounds in plain markdown.

## 60 seconds

```
> /mom-test-memory init --example
  discovery/ created with sample data: 4 interviews, 5 assumptions, 1 decision, 2 practice scores.

> /mom-test-prep derm office manager, call Thursday
  Memory: 3 prior interviews in this segment; testing A4.
  Scary question → "Have you ever charged a no-show fee? What happened?"
  Already known (don't re-ask): ~$300+/wk lost (3×), owner signs recurring spend (3×), SMS reminders in place …

> /mom-test-next-question live
  F: So we're building a tool that charges deposits automatically. Would that help?
  C: Oh yeah, that sounds really useful.
  ─
  Signal: compliment (none)
  Why: you pitched and asked a would-question; the answer is politeness
  Say next: "When did you last try charging anyone for a missed slot? What happened?"
  Don't say: "So you'd turn deposits on if it was one click?"

> /mom-test-debrief  [paste notes]
  … Facts (tagged): [A4-] rung 13 "we tried a $25 fee, owner turned it off after complaints" …
  Record to discovery/? [Y/n] y
  wrote interviews/2026-09-04-derm-office-manager.md · assumptions.md A4 → WEAKENED · segments.md +1 row

> /mom-test-gate build one-click deposit charging
  Rests on: A4 "Clinics would charge deposits if a tool made it one click" [WEAKENED]
  qualifying interviews (rung 8+ supporting): 0 · contradicting: 3
  strongest against: "The fee lasted two months. Three patients complained, the owner turned it off."
  VERDICT: RUN 3 CONVERSATIONS FIRST

> /mom-test-roleplay random healthcare 3
  … (you interview a simulated office manager who is polite when pitched and specific only about the past)
  Scorecard: 48/75 · lowest: pitching, urgency · saved to discovery/practice/scores.md

> /mom-test-league
  Weakest: pitching (2 of 3 runs) · Next: /mom-test-roleplay random any 3
```

## Install

**Clone and open.** Skills load automatically inside this repo via `.claude/skills`.

```sh
git clone https://github.com/sreshtalluri/mom-test.git && cd mom-test && claude
```

**Use everywhere.** Symlinks each skill into `~/.claude/skills/` (bundled templates, seed data, and personas travel with them).

```sh
./install.sh            # ./install.sh --uninstall to remove
```

**Claude Code plugin.**

```
/plugin marketplace add sreshtalluri/mom-test
/plugin install mom-test@mom-test
```

**Other agents.** Each skill is a standalone folder in the [Agent Skills](https://agentskills.io) format. Copy `skills/<name>/` (the whole folder) into `~/.codex/skills/`, `.cursor/skills/`, or `.agents/skills/`. The gate hint that `init` writes to `CLAUDE.md` is Claude Code specific; add the same two lines to `AGENTS.md` by hand for other agents.

## Skills

| Skill | When | What you get |
|---|---|---|
| `/mom-test` | Anything about talking to customers | The rules, reflexes, evidence ladder; routes to the rest |
| `/mom-test-prep` | Before a conversation | Prep sheet: three big questions, the scary one (from your riskiest open assumption if `discovery/` exists), what not to re-ask |
| `/mom-test-check-questions` | You have a question list or survey | Pass/fail per question and a past-tense reframe |
| `/mom-test-next-question` | Mid-conversation or staring at a quote | Ranked follow-ups. **`live` mode**: paste `F:`/`C:` lines, get Signal / Why / Say next / Don't say |
| `/mom-test-debrief` | After a conversation or a batch | Facts vs. fluff tagged to your assumptions, evidence ladder, 15-item scorecard /75, then records to `discovery/` |
| `/mom-test-memory` | Set up or inspect memory | `init [--example]`, `status`, `record`. Plain markdown, no DB |
| `/mom-test-gate` | Before building anything | Which assumption it rests on, how many real interviews back it, strongest quote for and against, verdict. Never blocks |
| `/mom-test-roleplay` | You want to practice | Persona packs by industry and difficulty 1–5 (`random healthcare 3`), hidden facts, graded debrief, score saved |
| `/mom-test-league` | After a few practice runs | Trend, weakest category, personas beaten, next persona to try |
| `/mom-test-outreach` | You need a reply | Cold email, intro request, follow-up, using the book's five-part framing |

## The `discovery/` folder

Created in your repo by `init`. Tracked in git by default (you'll be asked).

```
discovery/
  assumptions.md    | id | assumption | segment | kill condition | status | evidence | updated |
  segments.md       one row per interview: role, attrs, unprompted top problem, highest rung
  decisions.md      what you decided and which interviews justify it
  interviews/       one file per real conversation; facts tagged [A3+] rung 13 "quote"
  practice/         roleplay scores (never counted as evidence)
```

Rules that keep it honest: assumption IDs never change; evidence lives only in interview files and is grepped, never copied; `KILLED` is sticky; the riskiest assumption is the first row still `UNTESTED` or `WEAKENED`; roleplay never becomes an interview. Full spec in `skills/mom-test-memory/SKILL.md`. Sample data in `skills/mom-test-memory/seed/`.

## Contribute a persona

Copy the closest file in `skills/mom-test-roleplay/personas/`, change every fact, keep the schema and difficulty table from `personas/README.md`, open a PR. Five ship today: café owner (1), VP Sales (2), derm office manager (3), staff engineer (4), YouTube creator (5).

## The framework (docs/)

The skills are compressed from this. Read it to understand *why* they do what they do.

| File | Contents |
|---|---|
| [docs/CHEAT-SHEET.md](docs/CHEAT-SHEET.md) | One page to keep open during interviews |
| [docs/01-core-philosophy.md](docs/01-core-philosophy.md) | The problem the book solves, why founders get bad data, the mindset |
| [docs/02-chapter-analysis.md](docs/02-chapter-analysis.md) | Every chapter in sequence: idea, principles, bad→good, listen-for, checklist, example |
| [docs/03-questioning-framework.md](docs/03-questioning-framework.md) | Twelve question categories, and 25 questions that sound good but are bad |
| [docs/04-signals-and-listening.md](docs/04-signals-and-listening.md) | Signal Strength Ladder, active listening, the don't-pitch-early principle |
| [docs/05-playbook.md](docs/05-playbook.md) | Before/during/after playbook, decision tree, follow-up engine, Discovery OS |
| [docs/06-training.md](docs/06-training.md) | Five-level training system, 12 practice scenarios, the scorecard |
| [docs/07-templates.md](docs/07-templates.md) | Ten copy-paste templates |
| [docs/08-mental-models-and-skill.md](docs/08-mental-models-and-skill.md) | 18 mental models and the unified skill |
| [docs/designs/discovery-os-roleplay-league.md](docs/designs/discovery-os-roleplay-league.md) | Design doc for the memory, gate, live, and league layer |

Ideas are tagged **[Book]** (Fitzpatrick's, restated) or **[Synthesis]** (extensions built on top).

## The three rules

1. Talk about their life instead of your idea.
2. Ask about specifics in the past instead of generics or opinions about the future.
3. Talk less and listen more.

## License

MIT. *The Mom Test* is © Rob Fitzpatrick; this repo paraphrases its ideas and adds its own. Buy the book.
