<!--
author:   Hannes Tegelbeckers
email:    hannes.tegelbeckers@ovgu.de
version:  0.1.0
language: en
narrator: UK English Female
mode:     Textbook
comment:  MC01 · Module 1: Words Matter. Anthropomorphism and precise language (3.5 h)

@style
.headline { border: 2px dashed #c62828; padding: .8em 1em; font-family: Georgia, serif; font-size: 1.15em; border-radius: 6px; }
.precise  { border-left: 6px solid #2e7d32; background: rgba(46,125,50,.08); padding: .6em 1em; border-radius: 6px; }
.journal  { border-left: 6px solid #6a1b9a; background: rgba(106,27,154,.08); padding: .6em 1em; border-radius: 6px; }
.deepdive { border-left: 6px solid #1565c0; background: rgba(21,101,192,.08); padding: .6em 1em; border-radius: 6px; }
@end
-->

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
