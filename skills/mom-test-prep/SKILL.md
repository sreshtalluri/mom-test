---
name: mom-test-prep
description: >
  Prepare for a customer conversation using The Mom Test. Use when the user has an upcoming
  customer interview, discovery call, user research session, or sales discovery meeting and
  wants to get ready: "help me prep for my call with X", "what should I ask this customer",
  "I'm meeting a clinic manager tomorrow". Produces a one-page prep sheet with three big
  questions, the scary question, a broad opener, assumptions to test, and the commitment
  to ask for.
---

# Mom Test — Prep

Produce a prep sheet for one conversation. Fill it from what the user gave you. If the
**segment** or **stage** (discovery vs. solution) is missing and you can't infer it, ask
for those two things only, in one message, then proceed. Never ask more than two questions.

## If `./discovery/` exists, read it first

1. Read `discovery/assumptions.md` and `discovery/segments.md`.
2. **Scary question** = the riskiest assumption: the first row whose status is `UNTESTED`
   or `WEAKENED`. Phrase it about their past, anchored to that row's kill condition. If no
   such row exists, say the assumption list is exhausted and fall back to the behavior
   below.
3. **Already known** about this segment (rows in `segments.md` whose `role` matches):
   list the facts you shouldn't re-ask, citing interview basenames. Spend the questions
   on what's still open.
4. Put a line at the top of the sheet: `Memory: <n> prior interviews in this segment;
   testing A<n>`.

If `discovery/` doesn't exist, don't mention it; just build the sheet.

## Rules for every question you write

- Subject is **them**. Tense is **past/present**. Answer is a **fact or story**.
- No *would, could, might, think, like, interested, pay, scale of*.
- Never name the founder's assumed problem in the opener. Let the customer rank first.
- The scary question is the one whose answer the founder least wants. Put it first.

## Output (use exactly this structure)

```
PREP — [person / role] — [date if known]

Segment (one sentence, specific enough to recognize at a party):
Stage:  [ ] discovery   [ ] solution / validation

What you currently believe (falsifiable sentences):
  1. …                     Would be killed by: …
  2. …                     Would be killed by: …
  3. …                     Would be killed by: …

Broad opener (no mention of your problem):
  "What's the hardest part of ____?"

Three big questions (about their past):
  1. …
  2. …
  3. …
Scary question → #_   Feared answer: …   ASK IT IN THE FIRST 5 MINUTES.

Anchors to have ready:
  "When did that last happen?" · "Walk me through it." · "What did that cost you?"
  "How many times last month?" · "How do you handle it now?" · "What have you tried?"
  "Who decided on the last purchase like this?" · "Why does it matter now?" · "Where does it rank?"

Reflexes:
  compliment → "Thanks. How do you handle that today?"
  "always / would" → "When did that last happen?"
  "you should add X" → "Why? What would that let you do?"

[Solution stage only]
  One-sentence flip, in THEIR likely words:
  Objection invite: "What would make this not work for you?"
  Commitment to ask for (with a date):  [ ] 30-min trial on __  [ ] intro to __  [ ] paid pilot / deposit

Close:  "Who else should I talk to?"  ·  "What should I have asked?"

Don't bring:  a pitch, a deck, more than these questions.
```

## After the sheet

Add two or three lines noting anything in the user's framing that already breaks the rules
(for example, an opener that names their problem, or a belief stated so vaguely it can't be
killed). Fix it in the sheet and say what you changed.

Point the user to `mom-test-debrief` for afterward.
