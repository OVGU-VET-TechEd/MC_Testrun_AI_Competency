<!--
author:   Hannes Tegelbeckers
email:    hannes.tegelbeckers@ovgu.de
version:  0.1.0
language: en
narrator: UK English Female
mode:     Textbook
comment:  MC01 · Under the Hood: How AI Produces Its Outputs, and How to Say So Precisely. Module 0: Welcome to the AI Desk (1.5 h)

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
