<!--
author:   Hannes Tegelbeckers
email:    hannes.tegelbeckers@ovgu.de
version:  0.1.0
language: en
narrator: UK English Female
mode:     Textbook
comment:  MC01 · Module 2: Rules vs. Learning. Three families of AI systems (5 h)

@style
.headline { border: 2px dashed #c62828; padding: .8em 1em; font-family: Georgia, serif; font-size: 1.15em; border-radius: 6px; }
.precise  { border-left: 6px solid #2e7d32; background: rgba(46,125,50,.08); padding: .6em 1em; border-radius: 6px; }
.journal  { border-left: 6px solid #6a1b9a; background: rgba(106,27,154,.08); padding: .6em 1em; border-radius: 6px; }
.deepdive { border-left: 6px solid #1565c0; background: rgba(21,101,192,.08); padding: .6em 1em; border-radius: 6px; }
.poe      { border-left: 6px solid #ef6c00; background: rgba(239,108,0,.08); padding: .6em 1em; border-radius: 6px; }
@end
-->

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
