# Part 5 — Detecting Real Signals

## 5.1 The hierarchy of evidence

**[Book]** The book's core epistemology: **facts about the past beat opinions about the future**, and **commitments (giving something up) beat words**. **[Synthesis]** Extending that into a ranked hierarchy:

```
                       ┌──────────────────────────────┐
  STRONGEST            │  Money paid to you           │
                       │  Resources committed to you  │
                       │  Intro to decision-maker     │
                       │  Time committed to you       │
                       ├──────────────────────────────┤
                       │  Money spent on the problem  │
  STRONG               │  Time invested in problem    │
                       │  Workaround built            │
                       │  Active search underway      │
                       ├──────────────────────────────┤
                       │  Specific past incident      │
  MODERATE             │  Emotional recounting        │
                       │  Named consequences          │
                       │  Specific objections         │
                       ├──────────────────────────────┤
                       │  Generic complaint           │
  WEAK                 │  Agreement when prompted     │
                       │  Feature request             │
                       ├──────────────────────────────┤
                       │  Intention ("I would…")      │
  FALSE POSITIVE       │  Hypothetical commitment     │
                       │  Opinion ("good idea")       │
  (feels like signal)  │  Compliment                  │
                       └──────────────────────────────┘
```

The dividing principle: **the higher you go, the more it cost the customer to produce the signal.** Compliments cost nothing. Wiring money costs a lot.

## 5.2 Customer Signal Strength Ladder

**[Synthesis]** Each rung, weakest to strongest, with what it actually tells you.

| Rung | Signal | Example | What it really means | Weight |
|---|---|---|---|---|
| 1 | **Compliment** | "That's a really cool idea." | You pitched. They're being kind. | 0 |
| 2 | **Opinion** | "I think there's a real market for that." | They're guessing about others. | 0 |
| 3 | **Intention** | "I'd definitely use that." | They like you right now. | ~0 |
| 4 | **Hypothetical commitment** | "I'd pay $50/month for that." | They picked a number to end the question. | ~0 |
| 5 | **Feature request** | "You should add X." | There's a motive under it. Dig. On its own: noise. | Low |
| 6 | **Generic complaint** | "Reporting is always a pain." | Might be real, might be small talk. Anchor it. | Low |
| 7 | **Prompted agreement** | "Yeah, that's a problem for us too." | You led. Discount heavily. | Low |
| 8 | **Specific past incident** | "Last Thursday it took me three hours." | Real. Datable. This is the entry to real evidence. | Moderate |
| 9 | **Emotional recounting** | Voice changes, groans, "don't get me started." | The problem has a nerve. | Moderate |
| 10 | **Named consequences** | "We lost the client over it." | The problem has a price. | Moderate–Strong |
| 11 | **Specific objection** | "That won't work unless it syncs with Salesforce." | They mentally tried to use it. | Moderate–Strong |
| 12 | **Active search** | "I've demoed three tools this quarter." | Urgency plus intent, proven by action. | Strong |
| 13 | **Workaround built** | "I made a spreadsheet with macros." | Pain crossed the action threshold. | Strong |
| 14 | **Time invested in problem** | "I spend every Friday afternoon on this." | Recurring cost they've accepted. | Strong |
| 15 | **Money spent on problem** | "We pay $400/month for a tool that half works." | Budget exists. Willingness proven. | Strong |
| 16 | **Time committed to you** | Books a 30-min trial with a date. | Costs them something real. | Very strong |
| 17 | **Intro to decision-maker** | Sends the intro email while you're there. | Reputation on the line. | Very strong |
| 18 | **Resources committed** | Assigns an engineer to the integration; shares data. | Organizational skin in the game. | Very strong |
| 19 | **Money paid to you** | Deposit, LOI with dollars, paid pilot. | The only true validation. | Strongest |

**How to use it:** After a conversation, place each thing you heard on the ladder. If everything is at rung 7 or below, you have no evidence, however good the meeting felt. Rungs 8–15 are discovery evidence (the problem is real). Rungs 16–19 are validation evidence (the solution is wanted).

## 5.3 Strong vs. weak vs. false positive, with worked examples

| Statement | Classification | Why |
|---|---|---|
| "I'd definitely use that." | False positive | Future, free, flattering. |
| "This is the kind of thing we need." | False positive | Opinion; "we" is vague; "need" is untested. |
| "Everyone in my industry hates this." | Weak | Guess about others. Ask about them specifically. |
| "It's annoying, yeah." | Weak | Prompted, generic, no cost. |
| "You should build a mobile version." | Weak (but dig) | Idea. The motive might be strong. |
| "Last month I stayed until 9pm twice to finish it." | Strong | Specific, past, time cost. |
| "I currently pay $200/month for a workaround." | Strong | Money already moving. |
| "We tried Vendor X, spent $12k, ripped it out after four months." | Very strong (discovery) | Money, time, action, and a learned constraint. |
| "I've been trying to solve this for six months and spent $2,000." | Very strong (discovery) | Sustained effort plus money. |
| "Here, let me introduce you to our CFO right now." | Very strong (validation) | Reputation committed. |
| "Send me the contract for the pilot." | Strongest | Money. |

## 5.4 The three questions to ask of any signal

**[Synthesis]**
1. **Is it about the past or the future?** Future = discount to near zero.
2. **Did it cost them anything to say or do?** No cost = weak.
3. **Is it specific enough to be false?** "It's a pain" can't be wrong. "Tuesday took three hours" could be. Falsifiable claims are the only ones that carry information.

---

# Part 6 — How to Listen

## 6.1 Why listening is the actual skill

**[Book]** Talk less, listen more. **[Synthesis]** Asking good questions is maybe 30% of the skill. The other 70% is hearing what came back, because customers rarely hand you the important thing in a labeled box. They mention it in passing, in a tone shift, in a half-sentence they cut off. If you're preparing your next question or defending your idea, you'll miss it.

## 6.2 What to detect and how

| Detect | How it shows up | How to respond |
|---|---|---|
| **Pain** | Specific incidents, vivid words, sighs, "honestly," lowered voice, humor that isn't funny | "Tell me more about that." Then silence. |
| **Urgency** | A date, a trigger event, "we have to fix this before…", active searching, a new boss | "What's driving the timing?" |
| **Frequency** | Countable references ("every close," "each new hire"), or the opposite: "once, years ago" | "How many times last month?" |
| **Frustration** | Emotion directed at a tool, person, or process. "I hate…" "It's ridiculous that…" | Don't agree or console. Ask what they've done about it. |
| **Workarounds** | "What I actually do is…", "I built a…", "we have an intern who…", embarrassed laughter | "Walk me through that." Workarounds are the current product. |
| **Buying behavior** | Names of tools, vendors, prices, "we signed up for," "we canceled" | "How did that purchase happen? Who decided?" |
| **Hidden constraints** | "We can't," "legal won't," "IT blocks," "the union," "our system doesn't" | Write it down verbatim. These are deal-breakers or moats. |
| **Decision criteria** | "The thing that matters is…", "we chose X because…", "what killed Y was…" | "Is that the top criterion? What's second?" |
| **Objections** | "But what about…", "the problem with that is…", "that wouldn't work here because…" | Welcome them. "Say more." Objections are engagement. |
| **Contradictions** | "We don't have a budget for this" + "we spend $30k on the vendor." "It's not a big deal" + a 10-minute rant. | Gently surface: "Earlier you said X, and now Y. Help me square those." |
| **Opportunities** | Adjacent problems mentioned in passing, "the real issue is actually…", "what I'd really pay for is…" | Follow the thread even if it's off your script. |
| **Unexpected insights** | Anything that surprises you. A different user, a different buyer, a different problem, a different reason. | Mark it. Ask "why?" three times. Surprises are the point. |

## 6.3 What founders miss and why

**[Synthesis]** Each mode of self-focus blinds you to a specific category:

| When you're busy… | You miss… |
|---|---|
| **Explaining the idea** | Their unprompted problem ranking. You'll never learn what they'd have said first. |
| **Pitching** | Objections. People don't object to a pitch; they wait for it to end. |
| **Defending the product** | Hidden constraints. They stop telling you why it won't work and just smile. |
| **Running through prepared questions** | Tangents. The most valuable thing is usually off-script. |
| **Looking for confirmation** | Contradictions and "meh." You hear the agreement and not the flatness. |
| **Trying to impress** | Workarounds and embarrassment. They match your polish and hide the messy truth. |

## 6.4 Listening mechanics

**[Synthesis]**
- **Wait three seconds after they stop.** The second answer is often the real one.
- **Repeat their last three words as a question.** "Ripped it out?" It's the cheapest way to get the next layer.
- **Write down exact phrases.** Not "reporting is hard" but "I dread the Friday close." The word "dread" is data.
- **Track ratio.** If you've spoken for more than 30% of the time, stop and ask an open question.
- **Notice your own excitement.** When you feel the urge to say "yes, exactly, that's what we're building!", that's the moment to say nothing and ask "what happened next?"
- **Listen for what isn't there.** No numbers? No names? No incidents? No spending? The absences are the finding.

## 6.5 "Listen For This" cheat sheet

```
PAST-TENSE SPECIFICS   dates, "last week", "the time when", numbers
MONEY                  $, "we pay", "we spent", "budget", "canceled", "renewed"
TIME                   hours, "every Friday", "stayed late", "took all day"
WORKAROUNDS            "what I actually do", "I built", "we have someone who", "hack"
EMOTION                sighs, laughs, "honestly", "don't get me started", "dread", "hate", "love"
URGENCY                deadlines, "before Q3", "new boss", "we just got audited", "we're looking now"
CONSTRAINTS            "can't", "won't allow", "IT", "legal", "compliance", "our system"
DECISION PATH          names, titles, "sign-off", "approve", "budget owner", "procurement"
OBJECTIONS             "but", "what about", "the problem is", "that wouldn't work here"
CONTRADICTIONS         claim vs. behavior, budget vs. spending, "not a big deal" vs. rant
ABSENCES               no incident, no number, no name, no spend, no action

ALARMS (you drifted)
  compliments · "would/could/might" · "always/never" · you've talked >30% · no surprises yet
```

---

# Part 7 — Don't Pitch Too Early

## 7.1 Why pitching early contaminates feedback

**[Book]** Once you've revealed your idea, the customer knows what you want to hear. Every answer after that is filtered through politeness. **[Synthesis]** More precisely, pitching changes three things at once:

1. **It changes the topic** from their life (where they're the expert) to your product (where they're a guesser).
2. **It changes their role** from witness to judge, and judges of a friend's work are lenient.
3. **It changes the tense** from past to future, because a product that doesn't exist can only be discussed hypothetically.

All three moves take you from the top of the evidence ladder to the bottom in one step.

## 7.2 Why customers become polite once you reveal the idea

**[Synthesis]** Because the social cost of honesty jumps. Before the reveal, saying "that's not a problem for me" is neutral information. After the reveal, it's telling you your baby is ugly. Most people won't, and the ones who will are rare and valuable. The book's answer isn't to find braver customers; it's to not create the situation.

## 7.3 How founders accidentally lead

**[Synthesis]** Leading rarely looks like a pitch. It looks like:
- **A framing sentence.** "I'm building something for people who struggle with X. So, do you struggle with X?"
- **A loaded word.** "How painful is your onboarding?" You've asserted pain.
- **An example answer.** "Do you deal with this a lot? Like, daily?"
- **Enthusiasm.** Nodding hard when they say something you like teaches them what to say more of.
- **A follow-up that reveals the hypothesis.** "So would you say the real problem is the reporting?"
- **The demo you brought "just in case."**

## 7.4 Separating discovery from selling

**[Book + Synthesis]** They're different activities with different success criteria:

| | Discovery | Selling / validation |
|---|---|---|
| **Goal** | Learn what's true | Test whether they'll commit |
| **Topic** | Their life | Your solution |
| **Tense** | Past and present | Present (asking for commitment now) |
| **Success** | New facts, surprises, killed assumptions | Commitment or advancement |
| **Failure** | Compliments, fluff, no surprises | "Sounds great, keep me posted" |
| **When** | Before you know the problem matters | After you do |

You can do both in one conversation, but **discovery must come first and be complete before you flip.** Once you flip, discovery is over for that conversation.

## 7.5 When it's appropriate to introduce the solution

**[Synthesis]** You've earned the right to pitch in a conversation when you can answer all of these from what they told you:
- What's their top problem in this area, in their words, unprompted?
- When did it last happen and what did it cost?
- What do they do about it today, and what's wrong with that?
- Who decides and who pays?
- Is there urgency, or is it chronic and tolerated?

If any answer is blank, you're not done discovering. Don't pitch.

## 7.6 How to transition

**[Synthesis]** The transition should be short, honest, and grounded in what they said:

> "This is really useful. Can I flip it around for a minute? Based on what you said about [their words: the Friday close taking three hours], we've been working on [one sentence]. I'm not sure it fits what you described. What would make it not work for you?"

Three moves: acknowledge the shift, tie it to *their* specifics, and invite the objection rather than the compliment. Then, at the end, ask for a commitment.

## 7.7 How to know you've learned enough

**[Synthesis]** Across conversations, not within one:
- The last three people in your segment described the same problem the same way without prompting.
- You can predict what the next person will say and be right.
- You know the current solution, its cost, and its failure mode.
- You've heard the same objection twice and know whether it's fatal.
- Nothing in the last few conversations surprised you.

That's the moment to start showing something and asking for commitment.

## 7.8 Bad sequence vs. better sequence

**Bad sequence (validation theater):**
```
Pitch → "What do you think?" → "Love it!" → "Would you use it?" → "Definitely"
→ "Would you pay $30?" → "Sure" → founder logs a validated customer
```
Every arrow points to a false positive. Nothing here would be different if the idea were terrible.

**Better sequence:**
```
Broad problem   → "What's the hardest part of X?"
Specific past   → "When did that last happen? Walk me through it."
Current behavior→ "How do you deal with it today?"
Existing solution→ "What have you tried? What's wrong with it?"
Cost            → "What did that cost in time / money?"
Frequency       → "How many times last month?"
Impact          → "What happened as a result? Who noticed?"
Decision process→ "Who'd decide on a fix? Who pays?"
Urgency         → "What's making this matter now?"
────────────── only then ──────────────
Solution        → tied to their words, inviting objections
Commitment      → "Would you [trial / intro / pay] next week?"
```

**Worked example of the better sequence** (founder exploring a tool for restaurant managers handling staff scheduling):

> **F:** What's the most stressful part of your week?
> **C:** Sunday nights. Building next week's schedule.
> **F:** What happened last Sunday?
> **C:** Two people texted at 9pm that they couldn't do Tuesday. I redid half of it in a group chat until midnight.
> **F:** How do you build it today?
> **C:** Excel template, then screenshot into WhatsApp.
> **F:** Tried anything else?
> **C:** I looked at [scheduling app] once. It needed everyone to download something, and half my staff won't.
> **F:** What did last Sunday cost you?
> **C:** Three hours, and I opened Monday tired. And I comped two shifts because I double-booked.
> **F:** How many Sundays a month are like that?
> **C:** Three out of four.
> **F:** Who'd decide if you bought something for this?
> **C:** Me. I own the place. If it's under a couple hundred a month I don't think about it.
> **F:** What's making it worse lately?
> **C:** I just opened a second location. Now it's two schedules.
>
> *(All discovery boxes filled. Now the flip.)*
>
> **F:** Can I show you something? Based on the WhatsApp thing, we've been building a scheduler that works over text, no app for staff. I'm not sure it handles two locations well yet. What would break?
> **C:** Swaps between locations. That's the nightmare.
> **F:** Would you try it on next Sunday's schedule if I set it up Thursday?
> **C:** Yeah. Come by at 3.

The pitch was one sentence, it used the customer's own words, it invited an objection, and it ended in time commitment with a date.
