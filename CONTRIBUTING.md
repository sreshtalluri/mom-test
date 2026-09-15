# Contributing

The product is ten plain Markdown skills. Keep changes readable by an agent that
only has the individual skill directory and the founder's project files.

## Add a practice persona

1. Copy the closest pack from `skills/mom-test-roleplay/personas/` into
   `personas/<industry>/<slug>.md` within that same skill directory.
2. Use a fictional person and change every fact. Keep the pack under 60 lines.
3. Follow the [persona schema and difficulty table](skills/mom-test-roleplay/personas/README.md).
   Include all twelve body sections, specific past incidents, costs, spending,
   decision authority, and the hidden motive behind the volunteered feature.
4. In a fresh agent session, run `/mom-test-roleplay <industry>/<slug>`. Check that
   the hidden facts stay hidden until earned by questions or revealed at debrief.
   Try a leading pitch and a specific past-event question; the responses should
   match the difficulty. Finish the roleplay and inspect the practice score.
5. Open a PR describing the persona, difficulty, and what you tried. Include short
   fictional example turns and the outcome, not private customer transcripts.

No registry change is needed: the roleplay skill discovers persona files directly.
Practice results must never be recorded as real interview evidence.

## Change a skill

- Keep resources inside `skills/<name>/`. A `SKILL.md` must not depend on `docs/`,
  another skill directory, or any other top-level repo resource.
- Keep frontmatter `name` identical to the directory name. Use plain instructions
  that work across coding agents; avoid product-specific tool calls.
- For evidence changes, follow [the memory contract](skills/mom-test-memory/SKILL.md):
  stable assumption IDs, signed rung tags, append-only interview files, sticky
  `KILLED` status, and practice separate from evidence.
- Exercise changed behavior in a scratch founder project. For memory changes,
  check fresh and repeated initialization, existing evidence, duplicate recording,
  declined writes, and an empty or missing `discovery/` folder.
- Report the agent used, exact steps, observed result, and any untested behavior.
  Automated installer checks do not establish skill quality or founder adoption.

## Local checks

```sh
sh -n install.sh
python3 -m unittest discover -s tests -v
python3 -m json.tool .claude-plugin/plugin.json > /dev/null
python3 -m json.tool .claude-plugin/marketplace.json > /dev/null
```

Tests install into temporary directories. The installer refuses to overwrite
unrelated paths; move your own conflicting installation explicitly if you want to
switch checkouts. Uninstall removes only links owned by the current checkout.

## Demo and companion app

The README animation is a scripted illustration using fictional sample data,
not a recording of a founder trial. See [the demo source](docs/demo/README.md)
to regenerate it. The Rust importer belongs in the separate
[mom-test-live repo](https://github.com/sreshtalluri/mom-test-live).
