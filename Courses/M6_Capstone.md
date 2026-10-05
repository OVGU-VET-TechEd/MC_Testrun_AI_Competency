<!--
author:   Hannes Tegelbeckers
email:    hannes.tegelbeckers@ovgu.de
version:  0.1.0
language: en
narrator: UK English Female
mode:     Textbook
comment:  MC01 · Module 6: Capstone. Explain it to someone who has never studied AI (5.5 h)

@style
.headline { border: 2px dashed #c62828; padding: .8em 1em; font-family: Georgia, serif; font-size: 1.15em; border-radius: 6px; }
.precise  { border-left: 6px solid #2e7d32; background: rgba(46,125,50,.08); padding: .6em 1em; border-radius: 6px; }
.journal  { border-left: 6px solid #6a1b9a; background: rgba(106,27,154,.08); padding: .6em 1em; border-radius: 6px; }
.deepdive { border-left: 6px solid #1565c0; background: rgba(21,101,192,.08); padding: .6em 1em; border-radius: 6px; }
.poe      { border-left: 6px solid #ef6c00; background: rgba(239,108,0,.08); padding: .6em 1em; border-radius: 6px; }
@end
-->

# Module 6 · Capstone: Explain It

> ⏱ **5.5 hours** · Learning outcome LO6: *communicate model behaviour (training data, inference, hallucination) accurately to a non-specialist audience.* This module is assessed.

<!-- class="headline" -->
> 📰 **Your headline goes here.**
>
> *Campus Circuit*, special issue: "How AI really works", written by the AI Desk

Mira: *"You've fixed five headlines. Now I want you to write the piece that makes those headlines unnecessary. Explain to our readers, people who have never studied AI, how a chatbot produces its answers and why they can be confidently wrong. Correct, clear, no 'the AI thinks'."*

## The portfolio at a glance

> ⏱ 15 min

Your micro-credential portfolio has **three parts**. Submit them as one file (PDF) or one folder in the LMS (⟨submission link⟩).

| Part | What | Size | Time |
|---|---|---|---|
| **A · Explainer** | Explain how a chatbot produces an answer and why it can be confidently wrong, for a non-specialist audience you choose | see formats below | ~3 h |
| **B · Language audit** | Analyse a real public text about AI: ≥ 5 anthropomorphic or imprecise statements, rewritten with justification | table, 1–2 pages | ~1 h |
| **C · Reflection** | Before/after comparison, self-assessment, declaration | ≤ 300 words | ~45 min |

Your journal entries J0–J5 go in an **appendix** (they are not assessed, but they show your learning path).

The **rubric** used for assessment is on the page "Assessment rubric". Read it **before** you start.

## Part A · Choose audience and format

> ⏱ 15 min

**Choose your audience** (one):

- 👵 a grandparent or relative who uses a smartphone but has never thought about AI;
- 🎒 first-semester students in your subject, in their first week;
- 🏛️ the university press office or a dean, who has to write about the new campus chatbot;
- 🧑‍🏫 school pupils (age 14–16) on a university open day;
- ✏️ another non-specialist audience (describe them in one sentence).

**Choose your format** (one):

| Format | Size | Tip |
|---|---|---|
| 🎬 Video or screencast | 3–5 min | Phone video is fine; content counts, not production quality |
| 🎙️ Podcast / audio | 4–6 min | Add a short written outline |
| 🖼️ Comic or illustrated story | 6–12 panels | Hand-drawn and photographed is fine |
| 📄 Illustrated one-pager / *Campus Circuit* article | max. 600 words + ≥ 1 visual | Use a headline and an explainer box |
| 🧩 Interactive (LiaScript page, slide set with quiz) | ~5 min to work through | Must work without you being there |

**My audience and format:**

[[___ ___]]

## Part A · What must be in it

> ⏱ 15 min

Your explainer must cover these **four core ideas**, correctly and in words your audience understands:

| # | Core idea | From |
|---|---|---|
| 1 | **Fitted to data:** the model's behaviour comes from patterns fitted to (very large amounts of) training text; people chose the data and the method | Modules 2–3 |
| 2 | **Next-token loop:** the model generates text piece by piece by computing probabilities for the next token and sampling one | Module 4 |
| 3 | **Plausible ≠ true:** nothing in this process checks truth, so fluent false output (hallucination) is a structural consequence | Module 5 |
| 4 | **So what:** what your audience should do differently (e.g. check, don't share personal data, who is responsible) | Modules 1, 5 |

And it must be **free of anthropomorphic framing**, except where you deliberately quote and correct it.

**Optional but strong:** one **concrete example** (e.g. your hallucination hunt results), one **analogy** with its limit named, an image or diagram.

## Part A · Storyboard

> ⏱ 45 min

Plan before you produce. Fill in the storyboard (you can copy it into your own document).

**1. Hook** (≈ 10 %): a question, scene or surprising fact that matters to your audience.

[[___ ___]]

**2. Core idea 1: Fitted to data.** Your wording:

[[___ ___]]

**3. Core idea 2: The next-token loop.** Your wording, and your example or analogy:

[[___ ___ ___]]

**4. Core idea 3: Plausible ≠ true.** Your wording and example:

[[___ ___ ___]]

**5. Core idea 4: So what?** One to three concrete takeaways:

[[___ ___]]

**6. Closing line** your audience will remember:

[[___]]

### Analogy check

If you use an analogy, test it:

| Question | Your answer |
|---|---|
| Which part of the mechanism does it capture? | |
| Where does it break? Do you say so? | |
| Does it smuggle in a person (a "student", "assistant", "parrot that understands")? | |

<details>
<summary>💡 Analogies others have used, and their limits</summary>

- **"Autocomplete on your phone, scaled up enormously."** Captures the next-token loop well. Breaks: an LLM uses far more context and has far more parameters, so it produces whole coherent essays, which phone autocomplete never does.
- **"An extremely well-read improviser."** Captures fluency without fact-checking. Breaks: "well-read" and "improviser" imply a person who reads and decides. Use with care, and say so.
- **"A probability machine for words."** Precise, but abstract; pair it with an example.
- **"Stochastic parrot"** (Bender et al., 2021). A memorable critique that emphasises repetition without meaning. Breaks: models do produce new combinations, not just repetition, and "parrot" is an animal metaphor.

</details>

## Part A · Produce

> ⏱ 1.5 hours

Produce your explainer. Some practical tips:

- **Video/audio:** write a script first (≈ 130 words per minute). Record in one take per section.
- **Comic:** one core idea per 2–3 panels. Speech bubbles for *people*; captions for *what the system computes*.
- **Text:** headline, lead (2 sentences), four short sections, explainer box, sources.
- **Visual:** a simple diagram of the loop (*context → probabilities → sample → append → repeat*) goes a long way.

### May I use AI to make my explainer?

Yes, under these conditions:

- The **explanation** (content, structure, wording of the core ideas) must be your own; that is what is assessed.
- You may use AI tools for production support (e.g. generating an illustration, cleaning audio, spell-checking).
- **Declare** every AI use in Part C: which tool, for what, what you changed.

### Self-check before you continue

Read or watch your explainer once more **as your audience**. Then tick:

[[a]] All four core ideas are in it.
[[b]] I used no "thinks / knows / understands / wants / lies / decides" for the system (except in a quote I correct).
[[c]] Technical terms (token, training, parameters, hallucination) are explained when first used, or avoided.
[[d]] Someone from my audience could repeat the main point after one viewing/reading.
[[e]] It contains at least one concrete example.
[[f]] If I used an analogy, I named where it breaks.

💡 **Best test:** show it to a real person from your audience and ask them to explain it back to you in their own words.

## Part B · Language audit

> ⏱ 1 hour

**Task:** Take a **real public text about AI** (≥ 150 words): a news article, press release, product page, university web page, policy document or social media post. You may use one of the texts from your Module 1 collection.

1. Provide the source (title, publisher, date, link) and attach a copy or screenshot.
2. Mark **at least 5** statements that are anthropomorphic or technically imprecise.
3. Fill in the audit table:

| # | Original statement | Problem type (mental verb / intention / emotion / social role / self-report / technical inaccuracy) | Precise rewrite | Justification (1 sentence, with reference to the mechanism) |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |

4. End with **two sentences**: how would a reader's trust in or expectations of the system change if the whole text were written precisely?

<details>
<summary>💡 Example row</summary>

| # | Original | Type | Precise rewrite | Justification |
|---|---|---|---|---|
| 1 | "Our assistant **understands** your documents and **knows** exactly what you need." | mental verbs | "Our assistant generates summaries and answers based on the text of your documents." | The system computes outputs from the document text in its context; "understands/knows" implies comprehension and reliability that the mechanism does not provide. |

</details>

## Part C · Reflection

> ⏱ 45 min

### Belief check: after

Answer the same question as in Module 0 again. **When a chatbot like ChatGPT answers a question, which of the following are happening?**

[[a]] It looks up the answer in a large database.
[[b]] It searches the internet every time.
[[c]] It understands the meaning of my question.
[[d]] It calculates which words are likely to come next.
[[e]] It knows when it does not know something.
[[f]] It was programmed with rules for every topic.
[[g]] It can lie on purpose.
[[h]] Its answers depend on the texts it was trained on.

<details>
<summary>💡 What the course suggests</summary>

By default only **d** and **h** describe the mechanism. **b** is true only if the app has a search feature switched on (and then the retrieved text is added to the context). The others attribute knowledge, understanding, intention or hand-written rules that the mechanism doesn't have.

</details>

### Self-assessment: after

**I can tell whether a sentence about AI describes it as if it were a person.**

[(0)] Not yet
[(1)] Partly
[(2)] Confidently

**I can rewrite such a sentence so it describes what the system actually does.**

[(0)] Not yet
[(1)] Partly
[(2)] Confidently

**I can explain to a friend how a chatbot produces an answer, including the role of training data.**

[(0)] Not yet
[(1)] Partly
[(2)] Confidently

**I can explain why chatbots sometimes produce false statements that sound convincing.**

[(0)] Not yet
[(1)] Partly
[(2)] Confidently

### Write your reflection (≤ 300 words)

Address these four points:

1. **Then and now:** Compare your journal entry **J0** (your explanation in Module 0) with what you would write now. What exactly changed?
2. **Beliefs:** Which of your Module 0 beliefs changed, and which experience in the course changed it?
3. **Practice:** One thing you will do differently in your studies.
4. **Declaration:** *"I produced this portfolio myself. I used the following AI tools: … for … ."* (or: *"I used no AI tools."*)

[[___ ___ ___ ___ ___ ___]]

## Assessment rubric

> ⏱ 15 min

Your tutor assesses your portfolio with this rubric. Each criterion is rated **not yet / meets / exceeds**.

| Criterion | Not yet | Meets | Exceeds |
|---|---|---|---|
| **1 · Technical accuracy** (Part A) · LO2–LO5 | One or more core ideas missing or wrong (e.g. "looks up answers", "learns while chatting") | All four core ideas present and correct: fitted to data; next-token loop with sampling; plausible ≠ true as structural; consequence | Also correctly includes nuance, e.g. temperature, retrieval/RAG, training stages, or test vs. training performance |
| **2 · Precise, non-anthropomorphic language** (Parts A + B) · LO1 | Anthropomorphic framing of the system in own voice (*knows, thinks, understands, lies*) | No anthropomorphic framing in own voice; technical terms used correctly | Deliberately addresses and corrects anthropomorphic framing for the audience (e.g. names where an analogy breaks) |
| **3 · Fit for a non-specialist audience** (Part A) · LO6 | Jargon unexplained, or so simplified that it becomes incorrect; audience unclear | Clear audience; terms explained or avoided; at least one concrete example; understandable without prior knowledge | Engaging and memorable; tested with a real audience member, or uses a visual that clarifies the mechanism |
| **4 · Critical transfer** (Parts B + C) · LO1, LO5 | Fewer than 5 audit items, or rewrites without justification; reflection only descriptive | ≥ 5 items with correct rewrites and justifications referring to the mechanism; reflection compares before/after and names a concrete change in practice; AI use declared | Audit shows how the text's framing shapes trust or responsibility; reflection links to own discipline |

**Pass** = at least **meets** in criteria 1, 2 and 3, and **not "not yet"** in criterion 4.

If you don't pass on the first attempt, you get written feedback and can **resubmit once** within ⟨4 weeks⟩.

## Submit

> ⏱ 15 min

Checklist before submitting:

[[a]] Part A: explainer (file or link; links must be accessible to the tutor)
[[b]] Part B: audit table + source copy/screenshot
[[c]] Part C: reflection incl. declaration of AI use
[[d]] Appendix: journal entries J0–J5
[[e]] File name: `MC01_Portfolio_<Lastname>_<Firstname>`

**Submit in the LMS:** ⟨link / course page⟩

### Course feedback (quality assurance)

Your feedback improves this micro-credential (EU principle *Quality*: learner feedback is part of quality assurance). Anonymous, 2 minutes.

**How useful were the interactive tools (POE activities)?**

[(1)] Not useful
[(2)] Somewhat useful
[(3)] Useful
[(4)] Very useful

**Was the workload of ~30 hours realistic for you?**

[(1)] Much less
[(2)] About right
[(3)] Much more

**What should we improve?**

[[___ ___ ___]]

## 🎓 What's next

> ⏱ 10 min

Congratulations, you have completed the AI Desk. After assessment, you receive your micro-credential as a digital credential (⟨European Digital Credential / Open Badge⟩), which you own and can add to your Europass wallet, CV or LinkedIn profile.

<!-- class="precise" -->
> 🟩 **The one sentence of this course, now with everything you know**
>
> *An AI system turns an input into an output by applying patterns, either written down by people or fitted to data. A language model generates text by repeatedly computing a probability for every possible next token, given the context, and sampling one. Because it produces what is probable rather than what has been checked, fluent but false output is a structural property, so the people who use it must check it.*

**Stack it.** This micro-credential is the first in a series on the HETAICF domain *Engage with AI*. Natural next steps:

| Competency | Topic |
|---|---|
| **E3** | Evaluating AI outputs: when to accept, revise or reject |
| **E6** | Bias: how AI systems inherit and amplify social patterns from data |
| **C3** | Steering generative AI: prompting with intent |
| **ST2** | Steering your own learning with AI, without outsourcing it |

Mira's last note: *"Thanks. From now on, every AI headline goes across your desk first."*
