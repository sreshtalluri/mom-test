---
name: mom-test-next-question
description: >
  Suggest the best follow-up question given something a customer just said. Use during or
  right after a customer conversation when the user pastes a customer statement and asks
  "what should I ask next", "how do I follow up on this", "they said X, now what", or wants
  to dig deeper into a complaint, compliment, feature request, or vague answer. Classifies
  the statement, identifies what's still unknown, and ranks follow-ups by what the founder
  most needs to learn.
---

# Mom Test — Next Question

Input: one or more customer statements, optionally with what the founder already knows.
Output: the ranked follow-ups and the one to say if they have two seconds.

## Step 1 — Classify the statement

| Type | Markers | Default move |
|---|---|---|
| Generic claim | always, never, usually, everyone, all the time | Anchor to an instance |
| Future / hypothetical | would, could, might, will | Redirect to the past |
| Opinion | I think, I feel, it seems | Ask for the experience behind it |
| Compliment | cool, great, love, smart | Deflect to current behavior |
| Feature request | you should, it needs, add | Dig for the motive |
| Specific incident | a date, a number, a name | Expand it and cost it |
| Emotion | sigh, laugh, "honestly", "don't get me started" | "Say more." Then silence. |
| Constraint | can't, won't allow, IT, legal | Verify hardness |
| Objection | but, what about, wouldn't work here | Welcome it; get detail |
| Name / role | a person or team | Ask their role in the decision, or for an intro |

## Step 2 — List what's still missing

Check each; the follow-up should fill the most important gap.

| Missing | Question |
|---|---|
| Instance | "When did that last happen?" |
| Story | "Walk me through it." |
| Frequency | "How many times last month?" |
| Time cost | "How long did that take?" |
| Money cost | "What did that cost? What do you pay now?" |
| Consequence | "What happened as a result?" |
| Action taken | "What have you tried?" |
| Why it failed | "Why didn't that work?" |
| Current solution | "How are you handling it today?" |
| Owner / decider | "Who deals with it? Who decides?" |
| Urgency | "What's making this matter now?" |
| Priority | "Where does it rank?" |
| Motive (for ideas) | "Why do you want that? What would it let you do?" |
| Hardness (for constraints) | "Is that a hard rule or a preference?" |
| Emotion source | "What's behind that?" |

## Step 3 — Rank by stage

- **Early discovery** (problem not yet confirmed): instance first. Nothing is verifiable
  without one.
- **Mid discovery** (problem confirmed): cost, frequency, current solution, why past
  attempts failed. This is where value and constraints live.
- **Late discovery / solution stage**: decision-maker, urgency, priority, then a commitment
  ask.

## Output format

```
Statement: "…"
Type: …            Signal strength: none / weak / problem-real / solution-wanted
Already known: …   Still missing: …

Follow-ups, ranked:
1. "…"  — fills [gap]; ask this because [stage reason]
2. "…"  — fills [gap]
3. "…"  — fills [gap]

If you only have two seconds: "When did that last happen?"
Don't say: [the tempting bad follow-up, e.g. "so would a tool that did X help?"] — because [reason]
```

If the user pasted several statements, handle each briefly, then say which one thread is
most worth pulling and why.
