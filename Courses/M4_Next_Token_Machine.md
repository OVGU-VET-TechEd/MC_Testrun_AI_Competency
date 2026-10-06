<!--
author:   Hannes Tegelbeckers
email:    hannes.tegelbeckers@ovgu.de
version:  0.1.0
language: en
narrator: UK English Female
mode:     Textbook
comment:  MC01 · Module 4: The Next-Token Machine. How language models generate text (6 h)

@style
.headline { border: 2px dashed #c62828; padding: .8em 1em; font-family: Georgia, serif; font-size: 1.15em; border-radius: 6px; }
.precise  { border-left: 6px solid #2e7d32; background: rgba(46,125,50,.08); padding: .6em 1em; border-radius: 6px; }
.journal  { border-left: 6px solid #6a1b9a; background: rgba(106,27,154,.08); padding: .6em 1em; border-radius: 6px; }
.deepdive { border-left: 6px solid #1565c0; background: rgba(21,101,192,.08); padding: .6em 1em; border-radius: 6px; }
.poe      { border-left: 6px solid #ef6c00; background: rgba(239,108,0,.08); padding: .6em 1em; border-radius: 6px; }
@end
-->

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
