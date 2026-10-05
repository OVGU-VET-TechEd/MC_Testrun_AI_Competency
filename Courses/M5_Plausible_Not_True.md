<!--
author:   Hannes Tegelbeckers
email:    hannes.tegelbeckers@ovgu.de
version:  0.1.0
language: en
narrator: UK English Female
mode:     Textbook
comment:  MC01 · Module 5: Plausible ≠ True. Hallucination as a structural property (4 h)

@style
.headline { border: 2px dashed #c62828; padding: .8em 1em; font-family: Georgia, serif; font-size: 1.15em; border-radius: 6px; }
.precise  { border-left: 6px solid #2e7d32; background: rgba(46,125,50,.08); padding: .6em 1em; border-radius: 6px; }
.journal  { border-left: 6px solid #6a1b9a; background: rgba(106,27,154,.08); padding: .6em 1em; border-radius: 6px; }
.deepdive { border-left: 6px solid #1565c0; background: rgba(21,101,192,.08); padding: .6em 1em; border-radius: 6px; }
.poe      { border-left: 6px solid #ef6c00; background: rgba(239,108,0,.08); padding: .6em 1em; border-radius: 6px; }
@end
-->

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
