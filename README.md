# The Mom Test → Founder Conversation Skills

Rob Fitzpatrick's *The Mom Test*, turned into skills your coding agent can run, plus the
full framework behind them. Not a book summary: a set of tools for customer discovery,
outreach, interviews, and product decisions that produce **facts about the customer's
past** instead of **compliments about your idea**.

```
/mom-test-prep       → prep sheet for tomorrow's call
/mom-test-roleplay   → practice against a customer who lies politely, like a real one
/mom-test-debrief    → paste your notes, get facts vs. fluff, a score, and next steps
```

## Install

**Option 1 — clone and open (no install).** The skills load automatically when you run
Claude Code inside this repo, via `.claude/skills`.

```sh
git clone https://github.com/sreshtalluri/mom-test.git
cd mom-test && claude
```

**Option 2 — use everywhere.** Symlinks each skill into `~/.claude/skills/`.

```sh
git clone https://github.com/sreshtalluri/mom-test.git
cd mom-test && ./install.sh        # ./install.sh --uninstall to remove
```

**Option 3 — Claude Code plugin.**

```
/plugin marketplace add sreshtalluri/mom-test
/plugin install mom-test@mom-test
```

**Other agents.** Each skill is a standalone `skills/<name>/SKILL.md` following the
[Agent Skills](https://agentskills.io) format (YAML `name` + `description`, then
instructions). Copy the folders into wherever your agent loads skills from, e.g.
`~/.codex/skills/`, `.cursor/skills/`, or `.agents/skills/`.

## Skills

| Skill | Use it when | What you get |
|---|---|---|
| `/mom-test` | Anything about talking to customers | The rules, reflexes, and evidence ladder; routes to the others |
| `/mom-test-prep` | Before a conversation | One-page prep: three big questions, the scary one, broad opener, assumptions, commitment to ask for |
| `/mom-test-check-questions` | You have a question list or survey | Pass/fail per question, why, and a past-tense reframe |
| `/mom-test-next-question` | Mid-conversation, or staring at a quote | Ranked follow-ups by what you still don't know |
| `/mom-test-debrief` | After a conversation (or a batch) | Facts vs. interpretations, evidence-ladder count, 15-item scorecard out of 75, assumption updates, follow-up draft, segment table |
| `/mom-test-roleplay` | You want to practice | A simulated customer with hidden facts who gives compliments when pitched and specifics only when asked about the past; then a graded debrief |
| `/mom-test-outreach` | You need a reply | Cold email, warm-intro request, thank-you, confirmation, zombie revival, all using the book's five-part framing |

Example prompts:

```
/mom-test-prep I'm meeting a physio clinic manager tomorrow. Idea: reduce no-shows.
/mom-test-check-questions  Would you pay $20/mo for this? Do you struggle with scheduling? How often do no-shows happen?
/mom-test-next-question  She said "we always have no-shows, it's constant"
/mom-test-debrief  [paste notes]
/mom-test-roleplay  Be a solo YouTube creator with 200k subs. I'm building a sponsorship CRM.
/mom-test-outreach  Cold email to a head of ops at a regional trucking company
```

## The framework (docs/)

The skills are compressed from this. Read it to understand *why* the skills do what they do.

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

Ideas are tagged **[Book]** (Fitzpatrick's, restated) or **[Synthesis]** (extensions built on top).

## The three rules, so you don't have to open anything

1. Talk about their life instead of your idea.
2. Ask about specifics in the past instead of generics or opinions about the future.
3. Talk less and listen more.

## Contributing

Add a skill: create `skills/<name>/SKILL.md` with `name` and `description` frontmatter.
Keep it self-contained; skills get symlinked out of the repo, so don't rely on relative
paths to `docs/`. Open a PR.

## License

MIT. *The Mom Test* is © Rob Fitzpatrick; this repo paraphrases its ideas and adds its own.
Buy the book.
