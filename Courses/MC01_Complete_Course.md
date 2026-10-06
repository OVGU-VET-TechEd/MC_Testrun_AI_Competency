<!--
author:   Hannes Tegelbeckers
email:    hannes.tegelbeckers@ovgu.de
version:  0.1.0
language: en
narrator: UK English Female
mode:     Textbook
comment:  MC01 · Under the Hood: How AI Produces Its Outputs, and How to Say So Precisely (1 ECTS, self-paced)

@style
.headline { border: 2px dashed #c62828; padding: .8em 1em; font-family: Georgia, serif; font-size: 1.15em; border-radius: 6px; }
.precise  { border-left: 6px solid #2e7d32; background: rgba(46,125,50,.08); padding: .6em 1em; border-radius: 6px; }
.journal  { border-left: 6px solid #6a1b9a; background: rgba(106,27,154,.08); padding: .6em 1em; border-radius: 6px; }
.deepdive { border-left: 6px solid #1565c0; background: rgba(21,101,192,.08); padding: .6em 1em; border-radius: 6px; }
.poe      { border-left: 6px solid #ef6c00; background: rgba(239,108,0,.08); padding: .6em 1em; border-radius: 6px; }
@end
-->

# Module 0 · Welcome to the AI Desk

> ⏱ **1.5 hours** · Module 0 of 6 · *Under the Hood: How AI Produces Its Outputs, and How to Say So Precisely*

--{{0}}--
Welcome to this micro-credential. You will spend about thirty hours finding out how AI systems produce their outputs, and learning to describe that precisely.

Welcome! This micro-credential is about one competency that sounds simple and is surprisingly hard:

**Describing how AI systems perform tasks in accurate, non-anthropomorphic language.**

*Anthropomorphic* means describing something non-human as if it were human: as if it thinks, knows, wants, understands or lies. We do this with AI all the time. By the end of this course you will be able to explain what actually happens instead, and to explain it to people who have never studied AI.

## Your role: the AI Desk

> ⏱ 10 min

<!-- class="headline" -->
> 📰 **"AI now smarter than students: chatbot passes exam and *understands* the material better than most of us."**
>
> *Campus Circuit*, front page draft

You have just joined **The AI Desk**, the fact-checking column of the student newspaper *The Campus Circuit*. Your editor, Mira, has a problem: every week someone submits a headline like the one above. Some of these headlines are not exactly *wrong*, but they are *misleading*, because of the words they use.

Mira's brief to you:

> *"I don't need you to be a computer scientist. I need you to be able to say **what is really going on** inside these systems, in words our readers understand and that are still correct. Every week I'll bring you a new headline. Fix it."*

Each module opens with a new headline. At the end you will produce your own **explainer** for *The Campus Circuit* (or for anyone who is not an AI specialist). That explainer is the main part of your micro-credential portfolio.

## What you will earn

> ⏱ 10 min

This course leads to a **micro-credential** following the *European approach to micro-credentials*. That means it is a record of specific learning outcomes, assessed against transparent standards, that you own and can share (for example as a digital credential in your Europass wallet).

| | |
|---|---|
| **Title** | Under the Hood: How AI Produces Its Outputs, and How to Say So Precisely |
| **Workload** | 1 ECTS = 30 hours, self-paced, online |
| **Level** | EQF 6 / Bachelor level, any discipline, no prerequisites |
| **Competency** | HETAICF **E2**: *Describe how AI systems perform tasks in accurate, non-anthropomorphic language* (Domain D1, *Engage with AI*) |
| **Assessment** | Portfolio (explainer + language audit + reflection), assessed by a tutor with a published rubric; pass/fail |
| **Awarding body** | ⟨Otto-von-Guericke-Universität Magdeburg, …⟩ |
| **Stackable** | First credential of a series on the HETAICF domain *Engage with AI* |

### The competency in the framework's own words

The *Higher Education AI Competence Framework* (HETAICF) describes what members of a university should know and be able to do with AI. It is based on the OECD/EU *AILit* framework and helps universities meet the AI-literacy obligation of the EU AI Act (Art. 4).

> **E2:** The capacity to explain, in technically accurate terms, how an AI system produces its outputs (through **training data**, **statistical inference** and **probabilistic generation** rather than understanding, intention or knowledge) and to sustain that precision. For generative systems this explicitly includes naming **hallucination as a structural property** rather than an occasional malfunction.

The framework describes three levels. This course takes you to the first and into the second:

| Level | You can … | This course |
|---|---|---|
| **Foundation** | distinguish anthropomorphic from technically accurate descriptions of AI systems and use the latter | ✅ fully |
| **Applied** | explain model behaviour, including training data, inference and hallucination, to non-specialist audiences | ✅ shown in your capstone |
| **Advanced** | set terminological standards for an institution | (later in your career) |

## Learning outcomes

> ⏱ 5 min

When you have finished, you will be able to …

1. **distinguish** anthropomorphic from technically accurate statements about AI, and **rewrite** the former into the latter *(Module 1)*;
2. **differentiate** rule-based, learning and generative AI systems by *how* each produces its output *(Module 2)*;
3. **describe** how a model is fitted to training data, and **predict** how changes in the data change its behaviour *(Modules 2–3)*;
4. **explain** how a large language model generates text by repeated next-token prediction and sampling *(Module 4)*;
5. **explain** hallucination as a structural property of probabilistic generation, and **derive** consequences for your own studies *(Module 5)*;
6. **communicate** all of this accurately to a non-specialist audience *(Module 6)*.

## Your time plan

> ⏱ 5 min

| Module | Headline topic | Time |
|---|---|---|
| 0 | Welcome to the AI Desk | 1.5 h |
| 1 | Words Matter: anthropomorphism and precise language | 3.5 h |
| 2 | Rules vs. Learning: three families of AI systems | 5 h |
| 3 | What "Learning" Really Means: data, parameters, loss | 4.5 h |
| 4 | The Next-Token Machine: how language models generate text | 6 h |
| 5 | Plausible ≠ True: hallucination as a structural property | 4 h |
| 6 | Capstone: explain it to someone who has never studied AI | 5.5 h |
| | **Total** | **30 h** |

💡 **Tip:** Plan 2–3 sessions per week of about 90 minutes each. With that rhythm you will finish in about 4 weeks. Every page shows an estimated time (⏱).

## How this course works

> ⏱ 20 min

Each module has the same elements:

| Element | What it is |
|---|---|
| 📰 **Headline** | A misleading headline you will learn to correct |
| 🔮 **Predict – Observe – Explain** | You use an interactive website. *Before* you click, you write down what you expect. Then you look. Then you explain the difference |
| ✋ **Unplugged** | You do the computation yourself, on paper, before you see a machine do it |
| ✅ **Quiz** | Auto-checked, unlimited attempts. It is for you, not for grading |
| 🟩 **Precise Language Box** | The key wording of the module, ready to use |
| 🟪 **Journal** | A short reflection. You will need these entries for your portfolio |
| 🟦 **Deep dive** | Optional, for those who want more technical detail |

### Your portfolio document

Create **one document** now (Word, Google Doc, OneNote, a notebook, anything) and call it `MC01_Portfolio_<YourName>`. Copy each journal entry into it. Text you type into this course is saved only in your browser, so it can be lost when you clear your browser data.

### Tools and data protection

Most activities use **free interactive websites** that run in your browser and need no account. Some activities in Modules 4–5 use a chatbot. Please:

- use the AI tool approved by your university (⟨e.g. the university's chat service⟩), or a local model (no data leaves your computer);
- **never** enter personal data (yours or anyone else's), unpublished research data, or exam content;
- follow the rules for AI use in your study programme.

## Belief check

> ⏱ 10 min

Before you learn anything new, record what you believe **right now**. There are no right or wrong answers here. You will answer the same questions in Module 6 and compare.

**When a chatbot like ChatGPT answers a question, which of the following do you think are happening?** (Tick everything you believe is true.)

[[a]] It looks up the answer in a large database.
[[b]] It searches the internet every time.
[[c]] It understands the meaning of my question.
[[d]] It calculates which words are likely to come next.
[[e]] It knows when it does not know something.
[[f]] It was programmed with rules for every topic.
[[g]] It can lie on purpose.
[[h]] Its answers depend on the texts it was trained on.

**How much do you trust a confident, fluent answer from a chatbot?**

[(1)] Almost always correct
[(2)] Usually correct
[(3)] About half the time
[(4)] I always check it

📝 Copy your ticks into your portfolio document under the heading **"Belief check: before"**.

## Self-assessment

> ⏱ 10 min

Rate yourself against the framework descriptors. Be honest; this is for you.

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

📝 Copy your ratings into your portfolio under **"Self-assessment: before"**.

## Journal J0 · Your explanation today

> ⏱ 15 min

<!-- class="journal" -->
> 🟪 **Journal J0**
>
> In 3–5 sentences, explain **how you think a chatbot produces an answer** to a question like *"What is the capital of Saxony-Anhalt?"*.
>
> Write it the way you would explain it to a friend. Do not look anything up; this is your starting point and it is allowed to be wrong. In Module 6 you will rewrite it.

[[___ ___ ___ ___ ___]]

📝 Copy your text into your portfolio under **"J0"**.

## Quick check: how this course works

> ⏱ 5 min

**How is your micro-credential assessed?**

[( )] An online exam at the end of each module
[(X)] A portfolio (explainer, language audit, reflection) assessed with a published rubric
[( )] Automatically, from your quiz scores
[( )] By attendance

****************************************

Correct. The quizzes help you learn but are not graded. Your **portfolio** is assessed with a rubric that you will see in Module 6, and you are welcome to look at it from the start.

****************************************

**Which of these may you enter into a chatbot during the activities?** (Select all that apply.)

[[X]] A general question such as "Explain photosynthesis"
[[ ]] A fellow student's name and grades
[[X]] A request for literature on a public topic in your field
[[ ]] Unpublished data from your lab project

****************************************

Personal data and unpublished or confidential material never go into AI tools that your university has not approved for them.

****************************************

## ✅ Module 0 complete

<!-- class="precise" -->
> 🟩 **Precise Language Box: the one sentence of this course**
>
> *An AI system turns an input into an output by applying patterns, either written down by people or fitted to data. Generative systems produce their output piece by piece, sampling each piece from a probability distribution.*
>
> Every module looks at one part of this sentence: **patterns** (Module 2), **fitted to data** (Module 3), **sampling from a probability distribution** (Module 4), and what follows from that: **plausible is not the same as true** (Module 5).

**Next:** Module 1, *Words Matter*. Mira already has your first headline.

# Module 1 · Words Matter

> ⏱ **3.5 hours** · Learning outcome LO1: *distinguish anthropomorphic from technically accurate statements about AI, and rewrite the former into the latter.*

<!-- class="headline" -->
> 📰 **"University chatbot *understands* students' worries and *knows* all the exam rules."**
>
> *Campus Circuit*, submitted by the press office

Mira drops the headline on your desk: *"The press office sent this. It sounds nice. Is it true?"*

By the end of this module you will be able to say exactly what is wrong with it, and to offer a version that is still readable and correct.

## Why words matter

> ⏱ 20 min

In 1966 Joseph Weizenbaum wrote **ELIZA**, a program that imitated a psychotherapist. It had no model of the conversation at all: it matched keywords in what you typed and returned pre-written sentence templates (*"Why do you say you feel sad?"*). Weizenbaum was alarmed to see that people, including his own secretary, confided in it and asked to be left alone with it.

This is the **ELIZA effect**: we readily treat systems that produce human-like language as if they had human-like minds. Today's systems produce far more fluent language than ELIZA, so the effect is far stronger.

**Anthropomorphism** means attributing human mental states, intentions, emotions or social roles to something that is not human.

Why it matters in a university:

| If we say … | … people tend to … |
|---|---|
| "The AI **knows** the exam rules" | trust its answer without checking the actual exam regulations |
| "The AI **lied** to me" | look for a culprit inside the machine instead of asking who deployed it and how |
| "The AI **understands** your worries" | share personal information they would not type into a form |
| "The AI **decided** to reject the application" | lose sight of the people who designed, trained and approved the system |

Anthropomorphic language is not just imprecise. It shifts **trust** (we over-trust), **responsibility** (we blame or credit the machine instead of the people involved) and **behaviour** (we share more than we should).

## Spot the person in the machine

> ⏱ 25 min

Anthropomorphism comes in a few typical forms. Learn to recognise them.

| Type | Typical words | Example |
|---|---|---|
| **Mental verbs** | thinks, knows, understands, believes, realises, remembers, wonders | "ChatGPT *knows* a lot about history." |
| **Intentions and will** | wants, tries, decides, refuses, prefers, lies, admits | "The model *refused* because it *didn't want* to help." |
| **Emotions** | is happy, empathetic, worried, frustrated, polite | "The tutor bot is very *empathetic*." |
| **Social roles** | colleague, partner, friend, teacher, author | "My AI *co-author* wrote the introduction." |
| **Self-reports taken at face value** | "It *says* it is sure", "It told me it checked the sources" | The output "I have verified this" is treated as a report of a check, but it is generated text like any other |

The last type is the trickiest. When a chatbot outputs *"I am confident this is correct"*, that sentence is produced the same way as every other sentence it generates. It is **not** a report on an internal check.

### Practice: which of these are anthropomorphic?

Select **all** statements that describe the AI system as if it had human mental states, intentions, emotions or social roles.

[[X]] "The translation app understood the joke."
[[ ]] "The translation app produced a German sentence that keeps the pun."
[[X]] "The chatbot admitted it was wrong."
[[ ]] "After my correction, the chatbot generated a different answer."
[[X]] "The recommender system thinks I like jazz."
[[ ]] "The recommender system ranks jazz albums higher for my account, based on my listening history."
[[X]] "The image generator wanted to add a sixth finger."
[[X]] "The assistant is happy to help."

****************************************

The non-anthropomorphic statements all describe **what the system did** (produced, generated, ranks) and often **what it was based on** (listening history). The anthropomorphic ones describe the system as an agent with an inner life: it *understood*, *admitted*, *thinks*, *wanted*, *is happy*.

Note the last one: "happy to help" is a phrase that chatbots themselves often output. Repeating it is anthropomorphic, even though the chatbot "said it".

****************************************

## The translation toolkit

> ⏱ 30 min

Fixing anthropomorphic language does not mean writing like a technical manual. Use three moves:

1. **Name the mechanism.** What does the system actually do? *generates, computes, classifies, ranks, predicts, matches, retrieves, samples*
2. **Name the data.** What is the output based on? *training data, the prompt, the context window, your click history, retrieved documents*
3. **Name the humans.** Who designed, trained, configured, deployed or uses it? *the developers, the university, the user, the provider*

| Anthropomorphic | Precise | Move |
|---|---|---|
| "It **knows** a lot about history." | "Its training data contained a lot of text about history, so it is likely to generate plausible historical statements." | data |
| "It **understood** my question." | "It processed my prompt and generated a response that fits the question." | mechanism |
| "It **remembers** what I said earlier." | "My earlier messages are included in the input (the *context window*) for each new response." | data |
| "It **lied** about the source." | "It generated a reference that does not exist." | mechanism |
| "It **decided** to reject my application." | "The system assigned my application a score below the threshold that the admissions office set." | mechanism + humans |
| "It **refuses** to talk about politics." | "The provider trained and configured it to output a refusal for certain topics." | humans |
| "It **thinks** I like jazz." | "It ranks jazz higher for me, based on my listening history." | mechanism + data |

### Practice: choose the precise wording

Select the most precise option in each sentence.

1. The spam filter [[ hates | (classified as spam) | was suspicious of ]] the email from the unknown sender.
2. After I added a source, the chatbot [[ realised its mistake and | (generated a new answer that) | finally understood and ]] quoted the source correctly.
3. The face-recognition system [[ (produced a match score of 0.91 for) | recognised and knew | was sure about ]] the person in the photo.
4. The navigation app [[ wants me to | (computed a route that makes me) | thinks I should ]] take the motorway.
5. The essay-feedback tool [[ liked | (scored highly) | was impressed by ]] my introduction.

****************************************

In each case the precise version states **what the system computed or produced**. "Match score of 0.91" is more informative than "recognised": it tells you there is a number, and that someone chose a threshold for it.

****************************************

## Tricky cases: technical terms with human names

> ⏱ 20 min

The AI field itself borrowed many words from psychology and biology: *learning*, *neural network*, *attention*, *memory*, *reasoning*, *hallucination*. Are those forbidden?

**No, but you need to know what they mean technically.** They are **technical terms**, and they mean something much narrower than the everyday word.

| Term | Everyday meaning | Technical meaning |
|---|---|---|
| machine **learning** | gaining understanding | adjusting numerical parameters so that outputs fit training examples better (Module 3) |
| **neural** network | brain | a large function built from many simple weighted sums; loosely *inspired by* neurons |
| **attention** | conscious focus | a computation that weights how much each earlier token influences the next prediction (Module 4) |
| **memory** (in chat apps) | recalling experiences | stored text that the app adds to the input of later conversations |
| **reasoning** model | logical thinking | a model trained to generate intermediate text steps before the final answer; the steps are generated text too |
| **hallucination** | perceiving something not there | generating fluent output that is not supported by data or facts (Module 5) |

**Rule of thumb:** Using the technical term is fine in technical contexts. When you speak to non-specialists, **add the technical meaning** the first time ("the model *learns*, which means its parameters are adjusted to fit examples"), or use the precise wording instead.

<!-- class="deepdive" -->
> 🟦 **Deep dive: the intentional stance**
>
> The philosopher Daniel Dennett described the *intentional stance*: we predict the behaviour of complex systems by treating them *as if* they had beliefs and desires ("the chess computer *wants* to take my queen"). This can be a useful shortcut for predicting behaviour. The problem starts when the shortcut is taken literally, and when it hides the mechanism, the data and the humans involved. Academic writing should not rely on the shortcut.

## Is precision just pedantry?

> ⏱ 15 min

You may object: *"Everyone knows the chatbot doesn't really **know** anything. It's just a figure of speech."*

Three answers:

1. **Not everyone knows.** Many users assume that chatbots look up answers in a database or "understand" questions. Check your own belief poll from Module 0.
2. **Figures of speech shape expectations.** If something "knows", you expect it to be right. If something "generates likely text", you expect to check it.
3. **Your academic writing is judged on precision.** In a thesis, "the model understood the texts" invites the question: *how did you measure understanding?* "The model classified 87 % of texts correctly" does not.

The goal is **appropriate precision**: in a casual chat, shorthand is fine. In anything you publish, submit or use to inform a decision, name the mechanism, the data and the humans.

## Fix the headline

> ⏱ 25 min

Back to Mira's headline:

<!-- class="headline" -->
> 📰 **"University chatbot *understands* students' worries and *knows* all the exam rules."**

**Step 1:** Which words are anthropomorphic? Type them, separated by commas.

[[___]]

**Step 2:** Rewrite the headline so that it is **precise** *and* still works as a headline (max. 20 words). Use the three moves: mechanism, data, humans.

[[___ ___ ___]]

<details>
<summary>💡 Show possible solutions (try first!)</summary>

- *"New university chatbot answers questions about exam rules, generating replies from the official regulations it was given."*
- *"Chatbot trained on university documents responds to student questions, but its answers on exam rules still need checking."*
- *"Press office launches chatbot that generates answers from exam regulations. Students should check the original."*

What they have in common: no inner states ("understands", "knows"); they say **what it does** (generates, responds) and **what it is based on** (documents, regulations). The second and third versions also add the consequence: check the original.

</details>

**Step 3:** Compare your version with the solutions. What did you keep, and what would you change?

[[___ ___]]

## In the wild: collect real examples

> ⏱ 45 min

Anthropomorphic language about AI is everywhere: news, advertising, university websites, even research papers. This activity prepares **Part B of your portfolio** (the language audit).

1. Find **three** real sentences about AI in public texts (news article, press release, product page, university website, LinkedIn post …).
2. For each sentence, record:
   - the source (link + date),
   - the anthropomorphic word(s),
   - the type (mental verb / intention / emotion / social role / self-report),
   - your precise rewrite.

| # | Source | Original sentence | Type | Precise rewrite |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

📝 Copy this table into your portfolio document. You may use the best example later for your language audit.

💡 **Where to look:** search a news site for "AI" plus words like *knows, understands, decided, admits*. Company press releases about new AI products are reliable sources of examples.

## Quiz · Module 1

> ⏱ 15 min

**1. Why is "The AI decided to reject the loan" problematic?** (Select all that apply.)

[[X]] It hides the people who designed the system and set the threshold.
[[X]] It suggests the system has intentions.
[[ ]] It is grammatically wrong.
[[ ]] Computers can never be involved in decisions.

****************************************

The system computes a score; humans decided to use that score, and set the threshold, to approve or reject. "Decided" hides both the mechanism and the responsibility.

****************************************

**2. A chatbot outputs: "I have double-checked this answer." What is the most accurate interpretation?**

[( )] The chatbot ran an internal verification process.
[(X)] The chatbot generated this sentence the same way as all its other text; it is not evidence of a check.
[( )] The answer is now guaranteed to be correct.
[( )] The chatbot is lying.

****************************************

Unless the system documents an actual separate verification step (for example, a search with displayed sources), a sentence like this is simply more generated text. "Lying" is wrong too: lying requires an intention to deceive.

****************************************

**3. Which wording is acceptable in a non-specialist article?**

[( )] "The neural network learned to love Mozart."
[(X)] "The model learns, meaning its internal numbers are adjusted until its outputs match the training examples."
[( )] "The AI's brain stores every song it has heard."
[( )] "The AI understands music better than humans."

****************************************

Technical terms like *learns* are fine **if you explain them**. The other options use emotions ("love"), biology ("brain") or unmeasured mental capacities ("understands").

****************************************

**4. The three moves of the translation toolkit are …** (fill in: name the m______, the d___ and the h_____)

Name the [[mechanism]], the [[data]] and the [[humans]].

## Journal J1

> ⏱ 15 min

<!-- class="journal" -->
> 🟪 **Journal J1**
>
> 1. Which anthropomorphic word do **you** use most often when talking about AI? Why do you think that is?
> 2. Think of one situation in your studies where anthropomorphic language about AI could lead to a real problem (for trust, responsibility or data protection). Describe it in 2–3 sentences.

[[___ ___ ___ ___ ___]]

📝 Copy your answer into your portfolio under **"J1"**.

## ✅ Module 1 complete

<!-- class="precise" -->
> 🟩 **Precise Language Box · Module 1**
>
> - Avoid: *knows, understands, thinks, wants, decides, lies, admits, is happy to*
> - Use: *generates, computes, classifies, ranks, predicts, retrieves, outputs*
> - Always ask: **What is the mechanism? What data is it based on? Which humans are involved?**
> - A chatbot's statements about itself ("I'm sure", "I checked") are generated text, not reports.
> - Technical terms (*learning, attention, hallucination*) are fine if you explain them.

**Next:** Module 2, *Rules vs. Learning*. Why can't we just write down the rules for an AI system?

# Module 2 · Rules vs. Learning

> ⏱ **5 hours** · Learning outcomes LO2 and LO3: *differentiate rule-based, learning and generative AI systems by how each produces its output; predict how changes in the training data change a model's behaviour.*

<!-- class="headline" -->
> 📰 **"New library AI *decides by itself* which books you'll like, and nobody programmed it to."**
>
> *Campus Circuit*, science section

Mira: *"'Nobody programmed it'. Is that true? And if nobody programmed it, where does its behaviour come from?"*

Half of the headline is surprisingly accurate. To see which half, you need to know the three families of AI systems.

## Three families of AI systems

> ⏱ 25 min

"AI" is an umbrella term. Systems under that umbrella produce their outputs in quite different ways. HETAICF E2 distinguishes three families:

| | **Rule-based** | **Learning (predictive)** | **Generative** |
|---|---|---|---|
| **Where the behaviour comes from** | Rules written by people | Patterns fitted to labelled examples | Patterns fitted to very large collections of examples (text, images …) |
| **Typical output** | A fixed response or decision | A label, score, ranking or number | New content: text, image, audio, code |
| **Example** | Tax software, a chatbot with menu buttons, early spam filters (*"if subject contains 'WIN' → spam"*) | Spam filter trained on emails, face recognition, library recommendations, grade prediction | ChatGPT, Claude, Gemini, image generators, music generators |
| **Typical error** | Situation not covered by any rule | Wrong on cases unlike the training data; inherits bias from data | Fluent but false output (*hallucination*) |
| **Can you read why?** | Yes, the rules are readable | Partly (simple models) to hardly (large models) | Hardly |

Two things to notice:

1. **Learning and generative systems are also programmed.** People write the training procedure, choose the data and define what counts as "good" output. What is *not* written by hand is the final set of patterns: those are **fitted to the data**.
2. **Generative systems are learning systems** too. They differ in their output: they don't choose from fixed labels but produce new content, piece by piece.

So the headline is half right: nobody wrote a rule "recommend *Dune* to Hannes". But people chose the data (borrowing histories), the method and the goal (e.g. "maximise loans").

## ✋ Unplugged: write the rules yourself

> ⏱ 40 min

Before you watch machines learn, try the alternative: writing the rules by hand.

**Task:** You run the email inbox of a student council. Write **rules** that sort incoming emails into **"urgent"** and **"not urgent"**. Use only things a computer can check: words, sender, time, length, attachments …

Write at least 5 rules in the form *IF … THEN urgent / not urgent*:

[[___ ___ ___ ___ ___]]

Now test your rules on these emails. For each, apply **only your rules**, not your judgement:

| # | Email | Your rules say … | Actually … |
|---|---|---|---|
| A | Subject: *"URGENT: free pizza in the cafeteria!!!"* | | not urgent |
| B | Subject: *"Room booking"*. Text: *"the fire alarm in room G03 went off, we can't use it for tomorrow's assembly"* | | urgent |
| C | Subject: *"Re: Re: Re: minutes"*, from the dean's office, deadline today | | urgent |
| D | Subject: *"Quick question"*, from a first-semester student, about the date of next week's party | | not urgent |

**Reflect:** How many did your rules get right? What would you need to add? How many rules would you need for 10,000 different emails?

[[___ ___]]

<details>
<summary>💡 What usually happens</summary>

Most rule sets fail on A (the word "urgent" is there but it isn't) or B (it is urgent but the word isn't there). Each fix adds a rule, each rule creates new exceptions. This is the main limitation of rule-based systems: **the world contains more cases than anyone can write rules for.**

The alternative: collect thousands of emails that people have already labelled "urgent"/"not urgent" and let a procedure **fit** the patterns that separate them. That's machine learning.

</details>

## How a learning system produces its output

> ⏱ 20 min

A learning system has two phases:

**1. Training** (once, by the developers)

- Collect **examples** with the correct answer (*labels*): 10,000 emails marked urgent/not urgent.
- A training procedure adjusts the model's internal **parameters** until the model's outputs match the labels as well as possible.
- The result is a **trained model**: a fixed function from input to output.

**2. Inference** (every time it is used)

- A new email arrives. The trained model computes, for example, *"urgent: 0.83"*.
- A rule set by people turns this score into an action: *"if > 0.7, show in red"*.

```ascii
  TRAINING                                   INFERENCE
  ┌──────────────┐    adjust      ┌───────┐        ┌───────┐
  │ labelled     │ ─────────────▶ │ model │  new   │ model │──▶ score 0.83 ──▶ threshold (set by people) ──▶ "urgent"
  │ examples     │   parameters   │       │ input ▶│(fixed)│
  └──────────────┘                └───────┘        └───────┘
```

The model never "looks at" an email the way you do. It computes a number from features of the input, using parameters that worked well on the training examples. **Everything it can do comes from the patterns in those examples.**

## 🔮 POE 1: A decision tree learns from data (R2D3)

> ⏱ 50 min

<!-- class="poe" -->
> 🔮 **Predict – Observe – Explain**
>
> Tool: **A Visual Introduction to Machine Learning** (R2D3): http://www.r2d3.us/visual-intro-to-machine-learning-part-1/
>
> The story: a model is trained to tell whether a home is in **San Francisco** or **New York**, using data such as elevation, price per square foot and year built.

**Predict** (before opening the site): Which single piece of information do you expect to separate San Francisco from New York homes best? Why?

[[___ ___]]

**Observe:** Scroll through the whole visual story (≈ 15 min). Watch how the *decision tree* splits the data again and again. Pay attention to the end, where the model is tested on data it has **not** seen.

**Explain:**

1. What did the tree use first, and was your prediction right?
2. Who wrote the rules of this tree: people, or the training procedure? What did people decide?
3. The tree is 100 % accurate on the training data but less accurate on new data. Why?

[[___ ___ ___ ___]]

<details>
<summary>💡 Model answer</summary>

1. **Elevation** (San Francisco is hilly). Many people predict price; it helps, but less.
2. The split points were chosen **by the training procedure**, which finds the split that best separates the labelled examples. People chose the data, the features, the method and when to stop.
3. The tree has fitted details of the training examples that do not hold in general (**overfitting**). Accuracy on unseen test data is the honest measure.

Precise summary: *"The decision tree classifies homes using split rules that were fitted to labelled training data; it is less accurate on homes that differ from the training examples."*

</details>

<!-- class="deepdive" -->
> 🟦 **Deep dive:** R2D3 Part 2 (link at the end of Part 1) explains overfitting and the bias–variance trade-off. MLU-Explain (https://mlu-explain.github.io) has interactive essays on decision trees and train/test splits.

## 🔮 POE 2: Train your own classifier (Teachable Machine)

> ⏱ 90 min

Now you are the developer. You will train an image classifier and then deliberately give it a **bad data diet**.

<!-- class="poe" -->
> 🔮 **Predict – Observe – Explain**
>
> Tool: **Teachable Machine** (Google): https://teachablemachine.withgoogle.com → *Get started* → *Image project* → *Standard image model*
>
> Runs in your browser; webcam images are processed locally unless you choose to save the project. No account needed.

### Round 1: a fair data diet

1. Create two classes: **Class 1 = "pen"**, **Class 2 = "mug"** (or any two objects you have).
2. Record ~50 webcam images per class. Move the object, change the angle, use **different backgrounds** for both classes.
3. Click **Train Model**. Test with the live preview.

### Round 2: a biased data diet

4. Create a **new project**. Same two classes, but this time:
   - record **all "pen" images in front of a light wall**,
   - record **all "mug" images in front of something dark** (your jumper, a dark book).
5. **Predict:** Now hold the **pen in front of the dark background**. What will the model output?

[[___]]

6. **Observe:** Test it. Also try: the mug in front of the light wall; the dark background with **no object at all**.

7. **Explain:** What did the model actually fit in Round 2? Write a precise sentence, avoiding "it learned what a mug is".

[[___ ___ ___]]

<details>
<summary>💡 Model answer</summary>

In Round 2 the background was perfectly correlated with the label, and much larger in the image than the object. The training procedure fitted the pattern that separates the classes most easily: **light vs. dark background**. The model labels an empty dark background "mug".

Precise: *"The classifier assigns the label 'mug' to images with dark backgrounds, because in the training data all mug images, and only mug images, had a dark background."*

This is how many real failures happen. A well-known research example: a classifier that seemed to tell huskies from wolves had in fact fitted **snow in the background**, because most wolf photos in its training data showed snow (Ribeiro et al., 2016).

</details>

> 🔁 **No webcam?** Use *Upload* in Teachable Machine with photos from your phone, or work through the husky/wolf example in the model answer, and write the Explain step for that case.

### What follows from this

The training data is **all the model has**. It cannot tell an "important" pattern (the shape of a mug) from an "accidental" one (the background). Any pattern in the data that helps separate the labels can end up in the model, including **social patterns**: if past admission decisions were biased, a model trained on them will reproduce that bias. (This is HETAICF competency E6, a candidate for a later micro-credential.)

## 🔮 POE 3: Watch a trained network compute a class score (CNN Explainer) · optional

> ⏱ 15 min (optional)

Teachable Machine showed *that* an image classifier is fitted to example images. This tool shows *how* the fitted result works: it walks through a trained convolutional network (CNN) layer by layer.

<!-- class="poe" -->
> 🔮 **Predict – Observe – Explain**
>
> Tool: **CNN Explainer**: https://poloclub.github.io/cnn-explainer/

**Predict:** Before opening the tool, write one sentence describing what a trained CNN does to turn the pixels of an image into a class score — without using words like *sees*, *recognises* or *understands*.

[[___ ___]]

**Observe:** Choose one of the example images at the top of the page. The overview shows every layer of the network from the input image (left) to the class scores (right). Click a few units in different layers to see the calculation that produces them.
<!-- PRÜFEN: steps written from the tool's documentation; the live app could not be loaded during QA. Check the image selection and the click-through once in the browser. -->

**Explain:** In one or two sentences, describe what happens at each layer. Use the module's key words: *pixels, parameters, fitted, class score*.

[[___ ___]]

<details>
<summary>💡 Model answer</summary>

Each layer applies a calculation to the previous layer's output. In the **convolution layers** this calculation uses filters whose **parameters were fitted to labelled training images**; the other layers apply fixed operations (e.g. setting negative values to zero, or keeping only the largest value in a small window). The network does not "see" the image: it computes a sequence of numerical transformations, and the final layer outputs a **class score** for each class.

Precise: *"The CNN converts the image's pixels, layer by layer, into a class score by applying calculations whose parameters were fitted to labelled training images."*

</details>

## Precise language for learning systems

> ⏱ 30 min

Rewrite each sentence precisely. Use: *classifies, fitted, training data, score, threshold, people/developers*.

**a)** "The library AI decides by itself which books you'll like."

[[___ ___]]

**b)** "The camera AI recognised that the student was cheating."

[[___ ___]]

**c)** "The model taught itself to tell huskies from wolves."

[[___ ___]]

<details>
<summary>💡 Possible solutions</summary>

a) *"The library's recommender ranks books for each user. The ranking is computed by a model fitted to past borrowing data; the library chose the data and the goal."*

b) *"The proctoring software flagged the student because the model's score for 'suspicious movement' exceeded a threshold; the score was fitted to labelled training videos."* (And: someone must review the flag.)

c) *"During training, the model's parameters were adjusted to separate labelled husky and wolf photos; it turned out to rely mainly on snow in the background."*

</details>

## Quiz · Module 2

> ⏱ 20 min

**1. Match the systems.** Is it rule-based (R), learning/predictive (L) or generative (G)?

- A thermostat that heats when the temperature is below 20 °C: [[ (R) | L | G ]]
- A streaming service that ranks films for you based on what you watched: [[ R | (L) | G ]]
- A chatbot that writes a cover letter: [[ R | L | (G) ]]
- A spam filter trained on millions of emails marked as spam by users: [[ R | (L) | G ]]
- A tool that creates an image from the text "a cat in a lab coat": [[ R | L | (G) ]]
- A form that rejects your application if the field "matriculation number" is empty: [[ (R) | L | G ]]

**2. Which statement about learning systems is correct?**

[( )] Nobody programs them; they program themselves.
[(X)] People design the training procedure and choose the data; the specific patterns are fitted to the data.
[( )] They store all training examples and look up the most similar one.
[( )] They understand the concepts in the training data.

****************************************

"Fitted to data" is the key phrase. Some methods do compare against stored examples, but modern models generally compress patterns into parameters and do not store a lookup table of examples.

****************************************

**3. In Teachable Machine Round 2 the classifier labelled an empty dark background as "mug". The best explanation:**

[( )] The model is broken.
[( )] The model was confused.
[(X)] The background was the pattern that best separated the classes in the training data.
[( )] The webcam was too dark.

****************************************

"Confused" is anthropomorphic. The model works exactly as trained: it fitted the strongest distinguishing pattern in the data.

****************************************

## Journal J2

> ⏱ 15 min

<!-- class="journal" -->
> 🟪 **Journal J2**
>
> 1. Name one AI system you use in your studies or daily life. Is it rule-based, learning or generative, and how can you tell?
> 2. If it is a learning or generative system: what data might it have been trained on, and what kind of error would you therefore expect?

[[___ ___ ___ ___ ___]]

📝 Copy into your portfolio under **"J2"**.

## ✅ Module 2 complete

<!-- class="precise" -->
> 🟩 **Precise Language Box · Module 2**
>
> - **Rule-based:** "follows rules that people wrote."
> - **Learning:** "classifies / scores / ranks, using patterns fitted to labelled training data."
> - **Generative:** "produces new content, using patterns fitted to very large training data."
> - Training data is **all the model has**: accidental patterns (backgrounds, historical bias) are fitted just like meaningful ones.
> - Behind every "the AI decided" there is a **score** and a **threshold set by people**.

**Next:** Module 3, *What "Learning" Really Means*. What happens while a model is trained?

# Module 3 · What "Learning" Really Means

> ⏱ **4.5 hours** · Learning outcome LO3: *describe how a model is fitted to training data (data → parameters → loss) and predict how changes in the data change its behaviour.*

<!-- class="headline" -->
> 📰 **"AI *taught itself* to detect skin cancer. Doctors no longer needed?"**
>
> *Campus Circuit*, health column

Mira: *"'Taught itself.' Like a student in the library at night? What does a machine do when it 'learns'?"*

In Module 2 you saw *that* models are fitted to data. In this module you will see *how*. No maths beyond school level is needed; the optional deep dives go further.

## A model is a function with knobs

> ⏱ 40 min

Think of a model as a machine with an input slot, an output slot, and a very large number of **knobs** (*parameters*, also called *weights*).

- The **input** is turned into numbers: pixel brightness, word codes, measurements.
- The numbers flow through calculations. Each calculation is multiplied, added and compared using the knob settings.
- The **output** is a number or a set of numbers: *"probability of 'malignant': 0.12"*.

**Before training**, the knobs are set randomly, and the outputs are nonsense.
**Training** means: turn the knobs so that the outputs match the training examples better.

How big is "very large"? A simple line has 2 knobs (slope and intercept). The small networks in today's TensorFlow Playground activity have a few dozen. Large language models have **billions** of parameters.

### The simplest model: a line

You want to predict exam scores from hours studied. You have data from 6 students:

| Hours studied | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Exam score | 42 | 50 | 55 | 66 | 70 | 81 |

A model: `score = a × hours + b`. Two knobs: **a** and **b**.

Try it: which knob settings fit the data best? Change `a` and `b`, run, and look at the **total error**.

```js
var a = 5;     // knob 1: slope. Try other values!
var b = 40;    // knob 2: intercept

var hours  = [1, 2, 3, 4, 5, 6];
var scores = [42, 50, 55, 66, 70, 81];

var loss = 0;
for (var i = 0; i < hours.length; i++) {
  var predicted = a * hours[i] + b;
  var error = predicted - scores[i];
  loss += error * error;            // squared error
  console.log(hours[i] + " h: predicted " + predicted.toFixed(1) + ", actual " + scores[i]);
}
console.log("\nLOSS (sum of squared errors): " + loss.toFixed(1));
console.log("Lower is better. Can you get below 30?");
```
<script>@input</script>

The number you are trying to make small is called the **loss**: a measure of how far the model's outputs are from the training examples.

<details>
<summary>💡 Best settings</summary>

Around **a ≈ 7.6** and **b ≈ 34** gives a loss of about 12.5. That is what "training" computes: the knob settings with the lowest loss on the training data.

</details>

## Training = making the loss smaller, step by step

> ⏱ 30 min

With 2 knobs you can turn them by hand. With billions you can't. Training procedures do it automatically:

1. Feed a batch of training examples through the model.
2. Compute the **loss** (how wrong were the outputs?).
3. Compute, for every knob, in which direction turning it would **reduce the loss** (this is called the *gradient*).
4. Turn every knob a little in that direction.
5. Repeat, often millions of times.

This procedure is called **gradient descent**. Picture standing on a hilly landscape in fog: you can't see the valley, but you can feel which way the ground slopes under your feet, so you take a small step downhill, again and again.

That is all "learning" means here: **repeatedly adjusting parameters to reduce the loss on training examples.** Nothing is "understood" or "taught" along the way. The procedure was designed and started by people, runs on data people selected, and minimises a loss that people defined.

<!-- class="deepdive" -->
> 🟦 **Deep dive:** *Why Momentum Really Works* (Distill): https://distill.pub/2017/momentum/ lets you watch gradient descent move across a loss landscape and see why it sometimes zig-zags. *ML Visualized* (https://ml-visualized.com) shows the maths behind common algorithms.

## 🔮 POE: Watch a neural network being fitted (TensorFlow Playground)

> ⏱ 90 min

<!-- class="poe" -->
> 🔮 **Predict – Observe – Explain**
>
> Tool: **TensorFlow Playground**: https://playground.tensorflow.org
>
> Blue and orange dots are training examples of two classes. The network's job is to colour the background so that blue dots sit on blue and orange on orange. The **Training loss** and **Test loss** numbers are shown at the top right.

### Experiment 1: too few knobs

**Setup:** Data set **"Circle"** (top left, ring-shaped). Click **"–"** next to *hidden layers* until there are **0 hidden layers**. Features: only **X₁** and **X₂**.

**Predict:** Will the network be able to separate the inner blue circle from the orange ring?

[( )] Yes, quickly
[( )] Yes, after long training
[( )] No
[( )] I don't know

**Observe:** Press ▶ (play). Watch the background and the loss for ~30 seconds.

**Explain:** What can this model draw, and why does that fail here?

[[___ ___]]

### Experiment 2: more knobs

**Setup:** Reset (⟲). Add **1 hidden layer** with **4 neurons**.

**Predict:** What will change?

[[___]]

**Observe:** Press ▶. Watch the loss over time. Hover over the small neuron squares to see what each one has been fitted to.

**Explain:** Why does it work now? Use the words *parameters* and *loss*.

[[___ ___]]

### Experiment 3: noisy data and overfitting

**Setup:** Data set **"Spiral"**. Set *Noise* to **50**, *Ratio of training to test data* to **10 %**. Use **3 hidden layers with 8 neurons each**. Tick *Show test data*.

**Predict:** With very few training examples and a large network, what will happen to **training loss** vs. **test loss**?

[[___ ___]]

**Observe:** Run for 1–2 minutes.

**Explain:** What does the gap between training loss and test loss tell you?

[[___ ___]]

<details>
<summary>💡 Model answers for all three experiments</summary>

**Exp. 1:** With no hidden layer the model can only draw a **straight line** between the classes. No straight line separates a circle from a ring, so the loss stays high however long you train. The model is not "failing to understand"; it is a function that **cannot represent** the pattern.

**Exp. 2:** The hidden neurons add parameters and let the model combine several straight lines into a curved boundary. Training adjusts these parameters, the loss drops, and the background forms a circle. "More parameters" means "more flexible function", not "smarter".

**Exp. 3:** The training loss gets very low while the test loss stays higher or even rises. The model has fitted the **noise of the few training examples** (*overfitting*). Test data that was not used for training shows how the model performs on new cases. That is why serious claims about AI performance must report results on **held-out test data**.

</details>

> 🔁 **Site not working?** MLU-Explain (https://mlu-explain.github.io) → *Neural Networks* and *Train, Test, and Validation Sets* cover the same ideas in scroll-through form.

<!-- class="deepdive" -->
> 🟦 **Deep dive:** *Feature Visualization* (Distill): https://distill.pub/2017/feature-visualization/ and *Activation Atlas* (Distill): https://distill.pub/2019/activation-atlas/ make visible which input patterns individual units in an image network produce high activations for, once its parameters have been fitted to data. Phrase it precisely: say "this unit's activation is high for images with dog-like textures", not "this neuron knows what a dog is".

## Data is destiny: four consequences

> ⏱ 35 min

Everything a trained model does comes from three human choices: **the data**, **the model architecture** (how many knobs, how connected) and **the loss** (what counts as "good"). Four consequences you can now explain:

| Consequence | Why | Example |
|---|---|---|
| **1. It is only as good as its data** | The parameters are fitted to the training examples, nothing else | A skin-lesion classifier trained mostly on images of light skin performs worse on dark skin |
| **2. It struggles outside the training distribution** | New cases unlike the training data were never part of the fitting | A model trained on hospital A's scanner images performs worse on hospital B's scanner |
| **3. It optimises exactly what the loss measures** | Training reduces *that* number, not "what we meant" | A recommender that minimises "time until next click" will favour clickbait |
| **4. Good training scores ≠ good real-world performance** | Overfitting; test data may differ from real use | 95 % on a benchmark, much less in the clinic |

### Back to the headline

**"AI taught itself to detect skin cancer. Doctors no longer needed?"** Use what you know. Rewrite the headline and add one sentence of context a reader should know.

[[___ ___ ___]]

<details>
<summary>💡 Possible solution</summary>

*"Image classifier fitted to 100,000 labelled skin photos matches dermatologists on a test set."*
Context: *"The labels came from dermatologists; the model's accuracy on patients unlike those in the training photos, for example with different skin tones or cameras, has yet to be shown."*

Notice: the doctors did not become unnecessary. They **produced the labels** the model was fitted to.

</details>

## ✋ Unplugged: explain training with a kitchen analogy

> ⏱ 30 min

Analogies help non-specialists, and you will need one for your capstone. But every analogy breaks somewhere, and many smuggle in anthropomorphism.

Rate each analogy for "training a model":

**A) "Like a student studying for an exam."**

[(1)] Good analogy
[(2)] Partly
[(3)] Misleading

**B) "Like adjusting the knobs of a mixing desk until the recording sounds like the reference track."**

[(1)] Good analogy
[(2)] Partly
[(3)] Misleading

**C) "Like a cook who tastes the soup, compares it with the recipe photo, adds a little salt, tastes again, repeated a million times, without knowing what soup is."**

[(1)] Good analogy
[(2)] Partly
[(3)] Misleading

**Where does each analogy break?** Write one sentence per analogy.

[[___ ___ ___]]

<details>
<summary>💡 Discussion</summary>

- **A** is the most common and the most misleading: students build understanding, can explain why, and transfer knowledge. It implies the model "understands".
- **B** captures *parameters* (knobs) and *loss* (difference from the reference) well. It breaks because a model has billions of knobs and they are turned automatically, not by a sound engineer's ear.
- **C** captures the iterative loss-reduction, but "tastes" and "cook" slip in a person again. That's why it needs "without knowing what soup is".

A good explainer often says: *"It's a bit like B, but …"* and **names where the analogy breaks**.

</details>

## Quiz · Module 3

> ⏱ 30 min

**1. Put the training steps in order** (type the letters, e.g. `DABCE`):

A: compute the loss · B: compute which direction reduces the loss for each parameter · C: adjust parameters slightly · D: feed training examples through the model · E: repeat

[[DABCE]]

**2. What is a "parameter" in a neural network?**

[( )] A rule written by a programmer
[(X)] A number inside the model that is adjusted during training
[( )] A stored training example
[( )] A setting the user chooses when using the model

**3. A model reaches 99 % accuracy on its training data but only 70 % on new test data. This is most likely …**

[( )] a sign the model has understood the training data very well
[( )] a bug in the test data
[(X)] overfitting: the parameters fitted particularities of the training examples
[( )] normal; test accuracy is always much lower

**4. Which description of model training is precise?** (Select all that apply.)

[[X]] "The parameters were adjusted to minimise the error on labelled examples."
[[ ]] "The model studied thousands of images until it understood cancer."
[[X]] "The model was fitted to images labelled by dermatologists."
[[ ]] "The model taught itself without human help."

## Journal J3

> ⏱ 15 min

<!-- class="journal" -->
> 🟪 **Journal J3**
>
> 1. Before this module, what did you imagine when you heard "the AI learns"? What do you imagine now?
> 2. Choose one AI application in **your field of study**. What would its training data be, who would label it, and what could go wrong (use one of the four consequences)?

[[___ ___ ___ ___ ___]]

📝 Copy into your portfolio under **"J3"**.

## ✅ Module 3 complete

<!-- class="precise" -->
> 🟩 **Precise Language Box · Module 3**
>
> - A **model** is a function with many adjustable numbers (**parameters**).
> - **Training** = repeatedly adjusting the parameters to reduce the **loss** (the difference between outputs and training examples).
> - Say: *"fitted to data"*, *"trained on"*, *"optimised for"*. Avoid: *"taught itself"*, *"studied"*, *"understood"*.
> - The behaviour comes from **data + architecture + loss**, all chosen by people.
> - Trust test results on **held-out data**, not training results.

**Next:** Module 4, *The Next-Token Machine*. The same principle at enormous scale: how a language model produces text.

# Module 4 · The Next-Token Machine

> ⏱ **6 hours** · Learning outcome LO4: *explain how a large language model generates text by repeated next-token prediction and sampling, including the role of temperature.*

<!-- class="headline" -->
> 📰 **"ChatGPT has *read the whole internet* and now *knows* everything."**
>
> *Campus Circuit*, opinion page

Mira: *"Everyone writes this. And the answers really do look as if it knows everything. What's actually happening when I hit Enter?"*

This is the central module of the course. You will **be** a language model (on paper), **run** a tiny one (in this page), and **watch** a real one (in your browser).

## One sentence to remember

> ⏱ 15 min

A large language model (LLM) does one thing, over and over:

<!-- class="precise" -->
> 🟩 **Given the text so far, compute a probability for every possible next token, pick one, append it, repeat.**

Everything else (answering questions, writing code, translating, "chatting") is this one operation repeated hundreds of times. Let's take it apart:

| Part | Meaning |
|---|---|
| **text so far** | your prompt + everything generated so far (the *context*) |
| **token** | a piece of text: a word, part of a word, a punctuation mark. *"unbelievable"* might be `un` `believ` `able` |
| **probability for every possible token** | the model has a fixed vocabulary of ~50,000–200,000 tokens; for each one it outputs a number between 0 and 1 |
| **pick one** | *sampling*: usually not just the most likely one; controlled by *temperature* |
| **append, repeat** | the chosen token becomes part of the input for the next step |

## ✋ Unplugged: be the language model

> ⏱ 50 min

You need: a pen, paper, and a die (or any dice app).

**Your training data** (the whole "internet" of your model):

> *the cat sat on the mat . the cat ate the fish . the dog sat on the sofa . the dog ate the bone .*

**Step 1: Training = counting.** For each word, count which words follow it. Fill in the table on paper:

| After … | comes … (count) |
|---|---|
| the | cat (2), mat (1), fish (1), dog (2), sofa (1), bone (1) |
| cat | ? |
| sat | ? |
| on | ? |
| dog | ? |
| ate | ? |
| . (full stop) | ? |

**Step 2: Probabilities.** After *the*, there are 8 continuations in total, so P(cat) = 2/8 = 25 %, P(mat) = 1/8 = 12.5 %, …

**Step 3: Generate.** Start with *the*. Roll the die to choose the next word in proportion to the counts (assign die faces to words, re-roll if needed). Write the word down. Look up the row for *that* word. Roll again. Generate 8 words.

My generated text:

[[___ ___]]

**Step 4: Reflect.**

- Did you generate any sentence that is **not** in the training data?
- Is it grammatical? Is it *true* (in the world of the training data)?
- Did your model "know" anything about cats?

[[___ ___ ___]]

<details>
<summary>💡 What usually happens</summary>

You probably generated something like *"the dog ate the fish . the cat sat on the sofa"*: grammatical, plausible, and **not** in the training data. In your training "world", the dog never ate the fish.

Your model has no idea what a dog is. It only has **counts of which word follows which**. Yet it produces new, fluent sentences. That is the core of language modelling, and also the seed of *hallucination* (Module 5).

Your model looked at **one** previous word. That's called a **bigram model**. Real LLMs look at thousands of previous tokens, and instead of counts they use billions of parameters fitted by gradient descent (Module 3). The basic loop, however, is the same.

</details>

## 🔮 POE: Sampling from a probability distribution (Seeing Theory)

> ⏱ 10 min (optional)

<!-- class="poe" -->
> 🔮 **Predict – Observe – Explain**
>
> Tool: **Seeing Theory** (Brown University): https://seeing-theory.brown.edu/basic-probability/index.html
>
> An interactive introduction to probability. Use chapter 1 *Basic Probability*, section **Expectation** (a fair die: each face has probability 1/6).

**Predict:** You roll the die 10 times. Will each face appear in exactly 1/6 of the rolls? What do you expect after 100 more rolls?

[[___ ___]]

**Observe:** Click **Roll the Die** ten times, then **Roll 100 times** a few times, and watch the bars of the observed frequencies.

**Explain:** The probabilities never change, yet every short series of rolls looks different. What does this mean for a language model that samples its next token from a probability distribution?

[[___ ___]]

<details>
<summary>💡 Model answer</summary>

After 10 rolls the frequencies are uneven; after hundreds of rolls they come close to 1/6. Each single roll is a random draw from a **fixed probability distribution**. A language model does the same for every token: the distribution is fixed by the prompt and the parameters, but each draw can come out differently. That is why the same prompt can produce different answers, and why a less likely token is sometimes chosen.

</details>

## ⚙️ Run a tiny language model

> ⏱ 60 min

Below is the same bigram model as code. You don't need to understand every line. Change the parts marked **(change it!)** and press the ▶ run button.

```js
// ===== 1. TRAINING DATA (change it!) =====
var corpus = "the cat sat on the mat . the cat ate the fish . " +
             "the dog sat on the sofa . the dog ate the bone .";
var temperature = 1.0;   // (change it!) try 0.1 · 1.0 · 3.0
var start = "the";       // (change it!) first word
var length = 12;         // number of words to generate

// ===== 2. "TRAINING" = counting which word follows which =====
var words = corpus.toLowerCase().split(/\s+/).filter(function (w) { return w.length > 0; });
var counts = {};
for (var i = 0; i < words.length - 1; i++) {
  var a = words[i], b = words[i + 1];
  counts[a] = counts[a] || {};
  counts[a][b] = (counts[a][b] || 0) + 1;
}

// ===== 3. PROBABILITIES for the next word (temperature reshapes them) =====
function probabilities(word) {
  var options = counts[word] || {};
  var keys = Object.keys(options);
  var weights = keys.map(function (k) { return Math.pow(options[k], 1 / temperature); });
  var total = weights.reduce(function (s, x) { return s + x; }, 0);
  return keys.map(function (k, j) { return [k, weights[j] / total]; });
}

// ===== 4. GENERATION = sample, append, repeat =====
function sample(word) {
  var p = probabilities(word);
  if (p.length === 0) return null;
  var r = Math.random();
  for (var j = 0; j < p.length; j++) { r -= p[j][1]; if (r <= 0) return p[j][0]; }
  return p[p.length - 1][0];
}

var output = [start];
for (var n = 0; n < length; n++) {
  var next = sample(output[output.length - 1]);
  if (next === null) break;
  output.push(next);
}

console.log("Next-word probabilities after '" + start + "':");
probabilities(start).forEach(function (e) {
  console.log("  " + e[0] + "  " + Math.round(e[1] * 100) + " %");
});
console.log("\nGenerated text:\n" + output.join(" "));
```
<script>@input</script>

### Experiments

**E1: Same input, different output.** Run the code 5 times without changing anything. What do you notice?

[[___]]

**E2: Temperature.** Set `temperature = 0.1` and run 3 times. Then `temperature = 3.0`. Look at the probabilities **and** the text.

[[___ ___]]

**E3: Your own training data.** Replace the corpus with ~5 sentences of your own (e.g. about your field of study). Run it. What does your model "say"?

[[___ ___]]

<details>
<summary>💡 Model answers</summary>

**E1:** The output differs on each run, although the model is identical. Generation involves **random sampling** from the probabilities. That's why the same prompt gives different answers in ChatGPT, too.

**E2:** At **low temperature** the probabilities become extreme: the most frequent continuation gets almost 100 %, so the text is repetitive and predictable. At **high temperature** they flatten out: rare continuations become more likely, and the text gets more varied and more chaotic. Temperature doesn't make the model "more creative" in a human sense; it reshapes a probability distribution.

**E3:** The model can only recombine **your** words in sequences that appeared in **your** text. Output reflects training data, always.

</details>

<!-- class="deepdive" -->
> 🟦 **Deep dive: the temperature formula.** In the code, each count is raised to the power 1/T and then normalised. Real LLMs do the equivalent on their internal scores (*logits*): p = softmax(logits / T). T → 0 approaches "always pick the most likely token" (*greedy decoding*).

## From counting to a real LLM

> ⏱ 45 min

Your bigram model and GPT-4, Claude or Gemini share the loop. They differ in three ways:

| | Your bigram model | A large language model |
|---|---|---|
| **Context** | 1 previous word | thousands to millions of previous tokens |
| **How probabilities are computed** | counting | a *transformer* neural network with billions of parameters |
| **Training data** | 4 sentences | trillions of tokens: web pages, books, code, articles … |
| **Training objective** | (counting) | predict the next token; the loss is how much probability the model gave the actual next token |

### The transformer, in one paragraph

Each token is turned into a long list of numbers (an *embedding*). These numbers pass through many layers. In each layer, an operation called **attention** computes, for every token, how strongly each earlier token should influence it: in *"The bank of the river was muddy"*, the numbers for *bank* are adjusted using *river*. At the end, the numbers for the last position are turned into a probability for every token in the vocabulary. All of this is calculation with parameters that were fitted during training.

### Three training stages

1. **Pre-training:** predict the next token on huge text collections. Result: a model that continues any text plausibly, but doesn't reliably "answer".
2. **Instruction tuning:** further training on examples of *instruction → good response*, written by people.
3. **Preference tuning** (e.g. *RLHF*): people rate alternative outputs; the model's parameters are adjusted towards highly rated ones.

Stages 2 and 3 are why chatbots sound helpful, polite and confident: **that style was trained**. The friendly "I'd be happy to help!" is a learned output pattern, not a mood.

### What is *not* happening

When you send a question to a chatbot, by default:

- ❌ it does **not** look up the answer in a database of facts;
- ❌ it does **not** check whether its output is true;
- ❌ it does **not** "remember" you across conversations (unless the app stores text and adds it to the context, as a "memory" feature);
- ✅ it **computes** probabilities for the next token, given all text in the context, using parameters fitted to its training data, **samples** one, and repeats.

Some apps add tools: a **web search** or a **document search** (*retrieval-augmented generation, RAG*). Then the app retrieves texts and **puts them into the context**. The model still generates the answer token by token; it is just conditioned on more relevant text. Sources can still be misrepresented.

## 📺 Watch: the big picture

> ⏱ 25 min

Before you look inside a real model, get the big picture with animation.

Go to **3Blue1Brown: Neural Networks** (https://www.3blue1brown.com/topics/neural-networks) and watch the short overview of **large language models** (~8 min) and, if you can, the first part of the chapter on **transformers**.

While watching, **listen for wording.** The videos are carefully made, but even good explainers sometimes use shorthand. Note:

| Time | Wording you heard | Precise, or shorthand? If shorthand: your precise version |
|---|---|---|
| | | |
| | | |

**In one sentence:** which idea from the video connects your bigram model to a real LLM?

[[___ ___]]

<details>
<summary>💡 Possible answer</summary>

*"Both produce the next word from a probability distribution; an LLM computes that distribution with billions of fitted parameters and the whole context, instead of counts of one previous word."*

</details>

## 🔮 POE: Watch a real model compute probabilities (Transformer Explainer)

> ⏱ 90 min

<!-- class="poe" -->
> 🔮 **Predict – Observe – Explain**
>
> Tool: **Transformer Explainer** (Georgia Tech): https://poloclub.github.io/transformer-explainer/
>
> A real (small) language model, **GPT-2**, runs **in your browser**. You can type a prompt and watch every step, from tokens to the final probabilities. Use a desktop browser; it needs a few seconds to load.

### Round 1: the probabilities

The default prompt is something like *"Data visualization empowers users to"*.

**Predict:** Which word will get the highest probability as the next token? Write down your top 3.

[[___]]

**Observe:** Look at the right side of the visualisation: the list of candidate next tokens with their probabilities. Click **Generate** a few times.

**Explain:** How did your top 3 compare? Is the top candidate always chosen?

[[___ ___]]

### Round 2: temperature

**Predict:** What will happen to the probability bars if you move the **temperature** slider to a low value? To a high value?

[[___]]

**Observe:** Move the slider and watch the bars change. Generate at both settings.

**Explain:** Link this to your bigram experiment E2.

[[___ ___]]

### Round 3: your own prompt

Type two prompts and compare the probability distributions:

- a prompt with an obvious continuation, e.g. *"The capital of France is"*;
- a prompt with many possible continuations, e.g. *"My favourite thing about university is"*.

**Explain:** How do the distributions differ? What does this mean when a model generates a **fact**?

[[___ ___ ___]]

### Round 4: look inside

Click on the blocks in the middle (*Embedding*, *Attention*, *MLP*). You don't need to understand the maths. Write down **one** thing you found surprising.

[[___ ___]]

<details>
<summary>💡 Model answers</summary>

**R1:** Top candidates are typically words like *"create"*, *"visualize"*, *"understand"*, *"explore"*. Generation does not always pick the top one: it **samples** according to the probabilities (unless temperature is close to 0).

**R2:** Low temperature makes the top bar dominate (predictable text); high temperature flattens the bars (more varied, more errors). Same mechanism as in the bigram model.

**R3:** For *"The capital of France is"*, one token (*" Paris"*) gets a very high probability because this sequence is extremely frequent in the training data. For open prompts, probability is spread across many tokens. A "fact" is produced when the training data makes one continuation very likely, **not** because the model checked a fact. For rare facts, the probability is spread out, and a wrong but plausible token can be sampled (Module 5).

**R4:** Common surprises: words are split into odd sub-word tokens; GPT-2 is "only" 124 million parameters and yet produces fluent English; every step is just matrix arithmetic.

</details>

> 🔁 **Tool not loading?** Read *The Illustrated Transformer* (https://jalammar.github.io/illustrated-transformer/) and watch 3Blue1Brown's chapter on transformers (https://www.3blue1brown.com/topics/neural-networks). Then do Round 3 with any chatbot: ask the same question 3 times in new chats and compare.

<!-- class="deepdive" -->
> 🟦 **Deep dive: LLM Visualization** (https://bbycroft.net/llm) is a 3D walk-through of every computation in a small GPT model, step by step. For the research frontier, see Transformer Circuits (https://transformer-circuits.pub), which tries to reverse-engineer what computations inside these models do.

## Fix the headline

> ⏱ 30 min

<!-- class="headline" -->
> 📰 **"ChatGPT has *read the whole internet* and now *knows* everything."**

**a)** What is *partly* true in this headline?

[[___ ___]]

**b)** Rewrite it precisely (max. 25 words) and add a second sentence that a reader needs to know.

[[___ ___ ___]]

<details>
<summary>💡 Possible solution</summary>

a) Partly true: the model was trained on a very large amount of text, including much of the public web. "Read" is anthropomorphic, though: the text was used to fit parameters; it is not stored or understood.

b) *"ChatGPT's parameters were fitted to a vast amount of internet text. It generates likely continuations of your prompt."*
*"Because it produces what is probable, not what has been checked, its answers can be fluent and still wrong."*

</details>

## Quiz · Module 4

> ⏱ 30 min

**1. Which of these happens every time an LLM generates one token?** (Select all that apply.)

[[X]] It computes a probability for every token in its vocabulary.
[[ ]] It searches a fact database.
[[X]] It uses the whole context (prompt + text generated so far) as input.
[[ ]] It checks the previous sentence for truth.
[[X]] One token is selected, often by random sampling.

**2. You ask the same question twice in two new chats and get two different answers. Why?**

[( )] The model learned something between the two chats.
[(X)] The next tokens are sampled from probabilities, so different paths are possible.
[( )] The model changed its mind.
[( )] The server is broken.

****************************************

Sampling. The parameters did not change between your two chats (training happens beforehand, not while you chat), and "changing its mind" is anthropomorphic.

****************************************

**3. Higher temperature …**

[( )] makes the model more intelligent
[( )] makes the model use more training data
[(X)] flattens the probability distribution, so less likely tokens are chosen more often
[( )] makes outputs more accurate

**4. A chatbot with web search gives you an answer with sources. Which statement is precise?**

[( )] It read the sources and understood them.
[(X)] The app retrieved web pages and placed their text in the context; the model then generated an answer conditioned on that text.
[( )] It verified all statements against the sources.
[( )] It can no longer make mistakes.

**5. Fill the gaps.** An LLM generates text by repeatedly predicting the next [[token]] from a [[probability]] distribution.

## Journal J4

> ⏱ 15 min

<!-- class="journal" -->
> 🟪 **Journal J4**
>
> 1. Explain the core loop of an LLM in **two sentences** to a 12-year-old. (Then check: did you use any word from the Module 1 "avoid" list?)
> 2. What changed in how you see chatbot answers after "being the model" yourself?

[[___ ___ ___ ___ ___]]

📝 Copy into your portfolio under **"J4"**. This text is a good starting point for your capstone.

## ✅ Module 4 complete

<!-- class="precise" -->
> 🟩 **Precise Language Box · Module 4**
>
> - *"The model **generates** text by repeatedly predicting a probability distribution over the next **token** and **sampling** from it."*
> - *"Its parameters were **fitted to** large amounts of text"* (not *"it read / knows"*).
> - *"Different answers to the same prompt come from **sampling**"* (not *"it changed its mind"*).
> - *"**Temperature** controls how evenly probability is spread across candidate tokens."*
> - *"With search or RAG, retrieved text is **added to the context**; the answer is still generated."*
> - The helpful, confident tone is a **trained output style**.

**Next:** Module 5, *Plausible ≠ True*. If a model produces what is probable, what happens when probable and true come apart?

# Module 5 · Plausible ≠ True

> ⏱ **4 hours** · Learning outcome LO5: *explain hallucination as a structural property of probabilistic generation and derive consequences for your own academic practice.*

<!-- class="headline" -->
> 📰 **"AI *lies* about sources. Engineers promise to *fix the bug* in the next update."**
>
> *Campus Circuit*, tech news

Mira: *"A student's term paper cited three articles that don't exist. The chatbot made them up. Is this a bug that will be fixed?"*

This headline is wrong twice. By the end of this module you'll be able to say why, and what that means for your own work.

## Why "plausible" and "true" come apart

> ⏱ 25 min

From Module 4, you know the core loop: *compute probabilities for the next token, sample one, repeat.* Now look at what is **not** in that loop:

- There is no step that checks the output against the world.
- The training objective rewards **likely continuations** of text, not **true** ones.
- Facts appear in the model only indirectly, as **statistical regularities in the training text**.

So when does a model produce a true statement? When the true continuation is also the **most probable** one, because it appeared often and consistently in the training data (*"The capital of France is Paris"*).

When does it produce a false one? When a **false continuation is plausible**: it fits the patterns of the text so far, but is not supported by facts. Typical situations:

| Situation | Why falsehood becomes likely |
|---|---|
| **Rare facts** (a small town's mayor, a niche paper) | Few training examples; probability spread over many plausible names |
| **Specific formats** (citations, DOIs, page numbers, statistics) | The *form* is very regular (Author, Year, *Title*, Journal), the *content* rarely repeated |
| **Recent events** | After the training data was collected; the model has no data about them |
| **Questions with a false premise** (*"Why did Goethe win the Nobel Prize?"*) | Continuing the premise is more probable than contradicting it |
| **Long outputs** | Each sampled token conditions the next; one improbable choice can lead the rest astray |

This is why HETAICF says hallucination is a **structural property**, not an occasional malfunction: it follows directly from how the output is produced. The same mechanism that lets the model produce **new, fluent text** also lets it produce **new, fluent falsehoods**.

## ⚙️ Watch a hallucination being born

> ⏱ 30 min

Here is the bigram model from Module 4, trained on **four true sentences**.

```js
// ===== TRAINING DATA: four TRUE sentences =====
var corpus = "the river elbe flows through magdeburg . " +
             "the river spree flows through berlin . " +
             "magdeburg is the capital of saxony-anhalt . " +
             "berlin is the capital of germany .";
var temperature = 1.0;
var start = "the";
var length = 10;
var runs = 8;            // how many texts to generate

var words = corpus.toLowerCase().split(/\s+/).filter(function (w) { return w.length > 0; });
var counts = {};
for (var i = 0; i < words.length - 1; i++) {
  counts[words[i]] = counts[words[i]] || {};
  counts[words[i]][words[i + 1]] = (counts[words[i]][words[i + 1]] || 0) + 1;
}
function sample(word) {
  var options = counts[word];
  if (!options) return null;
  var keys = Object.keys(options);
  var w = keys.map(function (k) { return Math.pow(options[k], 1 / temperature); });
  var total = w.reduce(function (s, x) { return s + x; }, 0);
  var r = Math.random() * total;
  for (var j = 0; j < keys.length; j++) { r -= w[j]; if (r <= 0) return keys[j]; }
  return keys[keys.length - 1];
}
for (var run = 1; run <= runs; run++) {
  var out = [start];
  for (var n = 0; n < length; n++) {
    var next = sample(out[out.length - 1]);
    if (next === null) break;
    out.push(next);
  }
  console.log(run + ": " + out.join(" "));
}
```
<script>@input</script>

**Task:** Run it a few times. Copy **every false sentence** you find:

[[___ ___ ___]]

**Explain:** Every word pair in the output appeared in the true training data. How can the output be false?

[[___ ___]]

<details>
<summary>💡 Model answer</summary>

Typical outputs: *"the river spree flows through magdeburg"*, *"magdeburg is the capital of germany"*, *"berlin is the capital of saxony-anhalt"*.

Each **step** is locally plausible: *"through"* is followed by *magdeburg* or *berlin* in the data, each with 50 %. The model has no representation of *which river* the sentence is about. It just samples the next word. The result is **fluent, grammatical, built only from true material, and false.**

Large models look at much more context, so they make this particular mistake far less often. But the principle remains: they produce **what is probable given the context**, and nothing in the mechanism guarantees that probable equals true. A fake reference is the same phenomenon: author names, title words and journal names that are each plausible, combined into an article that does not exist.

</details>

**Try:** Set `temperature = 0.1`. Do the false sentences disappear? Set it to `3`. What happens?

[[___ ___]]

<details>
<summary>💡 Answer</summary>

Low temperature reduces the variety, but since *magdeburg* and *berlin* are exactly equally likely after *through*, even at T = 0.1 the two stay exactly equally probable: false sentences remain. **Lower temperature does not make a model truthful**; it only makes it pick the most probable option more consistently, and the most probable option can be wrong.

</details>

## Words for the phenomenon

> ⏱ 15 min

Even "hallucination" is a metaphor borrowed from psychology: a person hallucinates when perceiving something that isn't there. Some researchers prefer other terms:

| Term | Pro | Con |
|---|---|---|
| **hallucination** | Established; used in HETAICF and in most research | Suggests perception and a mind; suggests an exception to normal function |
| **confabulation** | From neurology: producing fluent false statements without intent to deceive | Still a human-mind metaphor |
| **fabrication** | Plain description of the output | Can suggest intent |
| **"generating unsupported content"** | Most precise | Clumsy in headlines |

**And "lying"?** Lying means saying something you believe to be false **in order to deceive**. A language model has no beliefs about truth and no intention, so "lying" is the wrong frame. It also directs blame away from the people who **deploy and use** the system without verification.

**Recommendation for this course:** use *hallucination* (the established technical term), and the first time you use it for non-specialists, add what it means: *"the model generates fluent content that is not supported by facts or sources; this follows from how the text is produced"*.

## 🔮 Hallucination hunt

> ⏱ 65 min

Time to see it in a real system. You will ask a chatbot for literature, then **verify** every reference.

<!-- class="poe" -->
> 🔮 **Predict – Observe – Explain**
>
> Tool: the chatbot approved by your university (⟨e.g. the university's chat service⟩), or a local model. **No personal data.** If the tool offers a "web search" mode, do the hunt **twice**: once with search off, once with search on.

**Prompt** (adapt the topic to a **niche** question in your own field; niche topics give the clearest results):

```text
List 5 peer-reviewed journal articles on [narrow topic in your field],
with authors, year, title, journal and DOI.
```

**Predict:** How many of the 5 references will be completely correct?

[( )] 5
[( )] 3–4
[( )] 1–2
[( )] 0

**Observe:** Check each reference in your university library catalogue, Google Scholar or via the DOI (https://doi.org/…). Record:

| # | Exists? | Authors correct? | Year/journal correct? | DOI leads to this article? | Category |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |

Categories: ✅ **correct** · ⚠️ **real but distorted** (exists, details wrong) · ❌ **fabricated** (does not exist)

**Explain:** Use the table from the first page of this module. Why did the errors (if any) occur where they did? Did search mode change the result, and why?

[[___ ___ ___ ___]]

<details>
<summary>💡 What people typically find</summary>

Without search, results on niche topics often include ⚠️ and ❌ references: real authors attached to papers they didn't write, plausible titles in real journals, DOIs that lead elsewhere or nowhere. Errors cluster in **specific details** (DOI, page, year), because those are the least repeated in training text.

With search, the app puts real web pages into the context, so references are more often real. But the generated summary of a source can still misstate what the source says; you still need to open it.

If all 5 were correct: try a narrower topic, or a field with less English-language literature. Fewer training examples, more hallucination.

</details>

📝 Copy your table into your portfolio. It is good material for your capstone.

## Transfer: images are generated, too

> ⏱ 30 min

Hallucination is not specific to text. Every **generative** model produces outputs by sampling from patterns fitted to data.

<!-- class="poe" -->
> 🔮 **Predict – Observe – Explain**
>
> Tool: **Diffusion Explainer** (Georgia Tech): https://poloclub.github.io/diffusion-explainer/
>
> Shows how Stable Diffusion turns a text prompt into an image, step by step, starting from random noise.

**Predict:** Where does a generated image "come from"? (a) a database of images, (b) a combination of stored photos, (c) something else.

[[___]]

**Observe:** Choose a prompt, watch the timesteps from noise to image. Change the **random seed** and compare. Change the **guidance scale**.

**Explain:** Why do image generators produce hands with six fingers or text that is almost-but-not-quite readable? Use the words *noise*, *patterns*, *training data*.

[[___ ___ ___]]

<details>
<summary>💡 Model answer</summary>

The image is not retrieved. It starts as **random noise**; in each step, a model fitted to millions of image–caption pairs predicts how to change the noise so the result fits the patterns of images matching the prompt. A different seed means different starting noise and a different image.

Hands and lettering are **locally plausible** (finger-like shapes next to finger-like shapes; letter-like strokes) but the model has no constraint like "a hand has five fingers" or "this word must be spelled correctly". It is the same structural property as fake references: **plausible patterns, no check against reality.**

</details>

<!-- class="deepdive" -->
> 🟦 **Deep dive:** *The Illustrated Stable Diffusion* (https://jalammar.github.io/illustrated-stable-diffusion/) explains the architecture. *GAN Lab* (https://poloclub.github.io/ganlab/) shows an older family of generative models being trained live.

<!-- class="deepdive" -->
> 🟦 **Deep dive:** *How to Use t-SNE Effectively* (Distill): https://distill.pub/2016/misread-tsne/ shows with interactive examples how *t-SNE* plots (a common way to draw high-dimensional data, e.g. what a model has learned, in 2D) can mislead: cluster sizes and distances between clusters may mean nothing, and even random noise can appear to form clusters. Not only generated text and images, also **visualisations** of data can look convincing and still misrepresent it: plausible ≠ true.

## Can it be fixed? And what you do about it

> ⏱ 25 min

**Back to the headline: "Engineers promise to fix the bug."**

Developers can **reduce** hallucination considerably, but not eliminate it, because it isn't a bug in one line of code:

| Mitigation | What it does | What remains |
|---|---|---|
| More / better training data | Makes true continuations more probable | Rare and new facts stay rare |
| Preference tuning to say "I'm not sure" | Model outputs uncertainty phrases more often | The phrases are generated text too and don't reliably match real error rates |
| Retrieval (search, RAG) | Puts relevant sources into the context | Sources can be wrong, misread or summarised inaccurately |
| Tools (calculator, code execution) | Moves some tasks out of the probabilistic generation | Only for tasks that a tool can do |
| Citations with links | Makes checking easier | You still have to check |

**So the responsibility for checking stays with the person using the output.** That's you, in your studies. (This links to HETAICF **E3**, *evaluate whether AI outputs are accepted, revised or rejected*, and to **ST1**, *academic work with AI*.)

### Five rules of thumb for your studies

1. **Never cite what you haven't opened.** Every reference from a chatbot is a *lead*, not a source.
2. **Specific = suspicious.** Numbers, dates, names, DOIs, quotations: verify each.
3. **Fluent ≠ correct.** Confidence and good style are trained output patterns, not signs of accuracy.
4. **Check the premise.** If your question contains an assumption, the output will usually go along with it.
5. **Follow your rules.** Your study programme's regulations on AI use and labelling apply (HETAICF **ST3**).

## Fix the headline

> ⏱ 15 min

<!-- class="headline" -->
> 📰 **"AI *lies* about sources. Engineers promise to *fix the bug* in the next update."**

Rewrite the headline precisely, and add a 2-sentence explainer box for readers.

[[___ ___ ___ ___]]

<details>
<summary>💡 Possible solution</summary>

*"Chatbots generate convincing references that don't exist, and updates will reduce but not remove the problem."*

**Explainer box:** *"Language models produce text by predicting likely next words, not by checking facts. A plausible-looking reference can therefore be generated even when no such article exists, so every AI-suggested source must be checked in a library catalogue."*

</details>

## Quiz · Module 5

> ⏱ 20 min

**1. Why is hallucination called a *structural* property of LLMs?**

[( )] Because it is caused by bad hardware.
[(X)] Because the generation process optimises for probable continuations and contains no step that checks truth.
[( )] Because developers add it on purpose.
[( )] Because it happens only in long texts.

**2. Which situations make hallucinations especially likely?** (Select all that apply.)

[[X]] Asking for DOIs of articles on a niche topic
[[X]] Asking about events after the training data was collected
[[ ]] Asking for the capital of France
[[X]] Asking "Why did Einstein win the Nobel Prize for relativity?"

****************************************

Einstein received the 1921 Nobel Prize for the photoelectric effect, not for relativity. A false premise invites a plausible continuation of the premise.

****************************************

**3. Setting the temperature to 0 …**

[( )] removes hallucinations
[(X)] makes output more deterministic, but the most probable continuation can still be false
[( )] makes the model check facts
[( )] makes the model refuse uncertain questions

**4. Which sentence is precise?**

[( )] "The chatbot lied about the reference."
[( )] "The chatbot was confused and invented a reference."
[(X)] "The chatbot generated a reference that does not exist."
[( )] "The chatbot had a hallucination because it was tired."

**5. A chatbot with web search gives a source link. What must you still do?**

[( )] Nothing; the link proves the answer is correct.
[( )] Ask the chatbot whether it is sure.
[(X)] Open the source and check that it says what the answer claims.
[( )] Check that the link works; the content will match.

****************************************

The link shows that the app retrieved *something*. Whether the generated answer represents it correctly is a separate question, and asking the chatbot "are you sure?" only produces more generated text.

****************************************

## Journal J5

> ⏱ 15 min

<!-- class="journal" -->
> 🟪 **Journal J5**
>
> 1. What was the result of your hallucination hunt? Did it match your prediction?
> 2. Write **one personal rule** for using chatbot output in your next assignment, and explain it in one sentence using what you now know about how the output is produced.

[[___ ___ ___ ___ ___]]

📝 Copy into your portfolio under **"J5"**.

## ✅ Module 5 complete

<!-- class="precise" -->
> 🟩 **Precise Language Box · Module 5**
>
> - *"The model **generated** content that is not supported by facts"* (not *"it lied"*, *"it was confused"*).
> - *"Hallucination is a **structural property** of probabilistic generation: the model produces what is probable, and nothing in the mechanism checks whether it is true."*
> - *"Mitigations (retrieval, tuning, tools) **reduce** hallucinations; they don't remove them."*
> - *"Confident wording is a **trained style**, not evidence."*
> - Responsibility for checking lies with **the people who use and deploy** the output.

**Next:** Module 6, the **Capstone**. Time to explain all of this to someone who has never studied AI.

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

