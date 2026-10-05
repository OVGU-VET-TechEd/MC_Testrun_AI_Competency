<!--
author:   Hannes Tegelbeckers
email:    hannes.tegelbeckers@ovgu.de
version:  0.1.0
language: en
narrator: UK English Female
mode:     Textbook
comment:  MC01 · Module 3: What "Learning" Really Means. Data, parameters, loss (4.5 h)

@style
.headline { border: 2px dashed #c62828; padding: .8em 1em; font-family: Georgia, serif; font-size: 1.15em; border-radius: 6px; }
.precise  { border-left: 6px solid #2e7d32; background: rgba(46,125,50,.08); padding: .6em 1em; border-radius: 6px; }
.journal  { border-left: 6px solid #6a1b9a; background: rgba(106,27,154,.08); padding: .6em 1em; border-radius: 6px; }
.deepdive { border-left: 6px solid #1565c0; background: rgba(21,101,192,.08); padding: .6em 1em; border-radius: 6px; }
.poe      { border-left: 6px solid #ef6c00; background: rgba(239,108,0,.08); padding: .6em 1em; border-radius: 6px; }
@end
-->

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
