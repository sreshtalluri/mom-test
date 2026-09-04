---
name: mom-test-league
description: >
  Roleplay practice league for The Mom Test. Reads discovery/practice/scores.md and
  shows your last scores, trend, weakest scorecard category, which personas you've
  beaten, a share line, and which persona to try next. Use when the user says "league",
  "my scores", "how am I doing at interviews", "practice history", "what should I
  practice next", or after a mom-test-roleplay debrief.
---

# Mom Test — League

Reads only `./discovery/practice/scores.md`. If it doesn't exist, say so and offer
`/mom-test-roleplay random` (which creates it after the first run).

## Column contract (must match what `mom-test-roleplay` writes)

```
| date | persona | difficulty | total | lowest two | highest rung |
```
`persona` is `<industry>/<slug>` for a pack or `generated:<role-slug>`. `total` is out of
75. `lowest two` are scorecard category names. `highest rung` is 1–19.

## Rules

- **Beaten** = a persona whose best score is ≥ 46 (the "solid discovery" band).
- **Weakest category** = the most frequent entry in `lowest two` across the last 10 rows.
- **Next difficulty** from the most recent score: `< 46` same or easier · `46–59` same ·
  `≥ 60` one harder (max 5).

## Output

```
LEAGUE — <n> runs

Last 10:   <date> <persona> d<difficulty> <total>   (one per line, newest first)
Trend:     <rising / flat / falling> — <best> best, <mean of last 5> recent avg
Weakest:   <category> (in your lowest-two <n> of last 10 runs)

Beaten (best ≥ 46):   d1: <personas> · d2: … · d3: … · d4: … · d5: …
Not yet:              <personas attempted with best < 46>

Share:  Scored <best>/75 vs "<persona>" (difficulty <d>) — mom-test league

Next:   /mom-test-roleplay random <industry or any> <difficulty>
        because <one line: last score <total> → <same/easier/harder>; drill <weakest category>>
```

Keep it to that block plus one sentence of coaching aimed at the weakest category (for
example, "costs" → "before you leave any incident, ask what it cost in hours or dollars").
