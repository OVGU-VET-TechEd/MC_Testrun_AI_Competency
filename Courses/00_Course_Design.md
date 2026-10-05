# MC01 · Under the Hood: How AI Produces Its Outputs, and How to Say So Precisely

**Course design document** · version 0.1 · 2026-10-02 · author: Hannes Tegelbeckers
Self-learning micro-credential · 1 ECTS (30 h) · English · LiaScript → SCORM

> Placeholders that must be filled by the institution are marked `⟨…⟩`.

---

## 1. EU micro-credential descriptor

Based on the *European approach to micro-credentials* (Council Recommendation 2022; brochure Dec 2021).

### Mandatory elements

| # | Element | Value for MC01 |
|---|---|---|
| 1 | Identification of the learner | Name + matriculation number (from LMS/SCORM learner record) |
| 2 | Title | *Under the Hood: How AI Produces Its Outputs, and How to Say So Precisely* |
| 3 | Country/region of issuer | Germany, Saxony-Anhalt |
| 4 | Awarding body | ⟨Otto-von-Guericke-Universität Magdeburg, Faculty/Institute …⟩ |
| 5 | Date of issuing | Date the capstone was assessed as *passed* |
| 6 | Learning outcomes | LO1–LO6, see §3 |
| 7 | Notional workload | 1 ECTS = 30 hours (see §4) |
| 8 | Level | EQF level 6 / QF-EHEA first cycle (Bachelor); open to all disciplines and semesters |
| 9 | Type of assessment | Formative: auto-graded quizzes + learning journal. Summative: portfolio, a capstone "explainer" artefact + language audit, assessed by a tutor against a published rubric (pass/fail) |
| 10 | Form of participation | Online, asynchronous, self-paced (LiaScript/SCORM in the LMS) |
| 11 | Type of quality assurance | Internal QA of the university (⟨evaluation procedure, e.g. course evaluation + peer review by KI-Campus partner⟩); framework alignment with HETAICF v0.13 |

### Optional elements

| Element | Value |
|---|---|
| Prerequisites | None. No programming or maths background needed. Optional "deep-dive" boxes for STEM learners |
| Supervision / identity verification | Unsupervised, no identity verification (self-declaration of independent work in the portfolio) |
| Grade | Pass / fail |
| Integration / stackability | Standalone. Stackable as MC01 of a planned HETAICF-D1 series (*Engage with AI*: E1–E7) towards a larger AI-literacy certificate (e.g. 5 ECTS) |
| Further information | Aligned with EU AI Act Art. 4 (AI literacy obligation) via HETAICF |

---

## 2. Competency alignment (HETAICF v0.13)

**Domain D1 – Engage with AI** · Level 1 (foundations) · Profile: **Students**

**HET-E2: Describe how AI systems perform tasks in accurate, non-anthropomorphic language**

> *Definition (verbatim):* The capacity to explain, in technically accurate terms, how an AI system produces its outputs (through training data, statistical inference and probabilistic generation rather than understanding, intention or knowledge) and to sustain that precision in teaching, in written course documentation and in institutional communication. For generative systems this explicitly includes naming hallucination as a structural property rather than an occasional malfunction.

| Level | Descriptor | Role in MC01 |
|---|---|---|
| Foundation (*Grundlegend*) | Distinguishes anthropomorphic from technically accurate descriptions of AI systems and uses the latter. | **Fully targeted** (= profile minimum for students) |
| Applied (*Fortgeschritten*) | Explains model behaviour including training data, inference and hallucination to non-specialist audiences. | **Entered** via the capstone; a pass shows this level in one bounded task |
| Advanced (*Vertieft*) | Sets terminological standards … | Not targeted (orientation only) |

**Object scope:** O1 *Own academic practice* (describes model behaviour accurately in one's own writing and speech, including hallucination as a structural property).

**Touched, not certified:** E3 (checking outputs, in Module 5), E6 (bias as a consequence of training data, in Module 2), ST1 (academic work with AI, in Module 5).

**Understanding-AI concept that runs through the course:**
*"An AI system turns input into output by applying patterns, either written down by people or fitted to data. Generative systems sample the next piece of output from a probability distribution."* Each module looks at one part of that sentence: **patterns** (rules vs. learned), **fitted** (training/loss), **data** (what goes in shapes what comes out), **probability + sampling** (generation), and the result: **plausible ≠ true** (hallucination).

---

## 3. Learning outcomes and constructive alignment

After completing the course, learners can …

| LO | Learning outcome | HETAICF descriptor | Learning activities | Evidence |
|---|---|---|---|---|
| LO1 | **distinguish** anthropomorphic from technically accurate statements about AI systems and **rewrite** the former into the latter | E2 Foundation | M1 Headline Lab, translation drills, "precise language box" in every module | M1 quiz; language audit (capstone part B) |
| LO2 | **differentiate** rule-based, learning (predictive) and generative AI systems by how each produces its output, using concrete examples | E2 definition | M2 unplugged rule-writing, R2D3, Teachable Machine | M2 quiz; journal 2 |
| LO3 | **describe** how a model is fitted to training data (data → parameters → loss) and **predict** how changes in the data change its behaviour | E2 Applied ("training data"); touches E6 | M2 data-diet experiment, M3 TensorFlow Playground POE | M3 quiz; journal 3 |
| LO4 | **explain** how a large language model generates text as repeated next-token prediction and sampling (incl. temperature) | E2 Applied ("inference") | M4 be-the-model (bigram by hand), runnable mini model, Transformer Explainer | M4 quiz; capstone part A |
| LO5 | **explain** hallucination as a structural property of probabilistic generation and **derive** consequences for their own academic practice | E2 definition; touches E3, ST1 | M5 hallucination hunt, Diffusion Explainer transfer, rules of thumb | M5 quiz; journal 5; capstone part A |
| LO6 | **communicate** model behaviour (training data, inference, hallucination) accurately to a non-specialist audience | E2 Applied | M6 capstone production, peer-style self-check with rubric | Capstone (summative) |

---

## 4. Workload (30 h)

| Module | Title | Read / watch | Hands-on | Produce / reflect | Total |
|---|---|---|---|---|---|
| M0 | Welcome to the Newsroom: orientation, pre-poll, self-assessment | 0.5 | 0.25 | 0.75 | **1.5 h** |
| M1 | Words Matter: anthropomorphism and precise language | 1.0 | 1.5 | 1.0 | **3.5 h** |
| M2 | Rules vs. Learning: three families of AI systems | 1.5 | 2.5 | 1.0 | **5.0 h** |
| M3 | What "Learning" Really Means: data, parameters, loss | 1.5 | 2.0 | 1.0 | **4.5 h** |
| M4 | The Next-Token Machine: how LLMs generate text | 2.0 | 3.0 | 1.0 | **6.0 h** |
| M5 | Plausible ≠ True: hallucination as a structural property | 1.5 | 1.5 | 1.0 | **4.0 h** |
| M6 | Capstone: Explain It to Your Grandma (and Your Dean) | 0.5 | 0.5 | 4.5 | **5.5 h** |
| | **Sum** | **8.5** | **11.25** | **10.25** | **30 h** |

Roughly ⅓ input, ⅓ hands-on, ⅓ production/reflection. Times assume no prior knowledge; STEM learners will be faster and can use the optional deep-dive boxes.

---

## 5. Didactic design

| Approach | Where | Why |
|---|---|---|
| **Narrative frame "The AI Desk"**: the learner joins a student newsroom that fact-checks AI headlines; every module opens with a new headline that needs a correction | All modules | Motivation and coherence for self-learners; gives an authentic reason to care about precise language |
| **Conceptual change**: belief poll at the start (M0), confronted by demos, re-poll at the end (M6) | M0, M6 | Misconceptions about AI ("it knows", "it looks things up") are sticky; making them explicit first is necessary before they can change |
| **Predict – Observe – Explain (POE)** for every interactive tool | M2–M5 | Turns "playing with a website" into hypothesis testing |
| **Unplugged / be the model**: write rules by hand, count bigrams by hand | M2, M4 | Learners do the mechanism themselves before they see it automated, which counters "magic" explanations |
| **Runnable micro-model** inside the course (editable JavaScript bigram generator with temperature) | M4, M5 | Learners can change the corpus or temperature and watch hallucination appear |
| **Translation drills** (anthropomorphic → precise) + a recurring "Precise Language Box" | M1–M6 | Repeated practice of the core E2 behaviour |
| **Learning journal** (one prompted entry per module) | M0–M5 | Metacognition (cf. ST2); raw material for the capstone |
| **Authentic-audience capstone** with choice of medium | M6 | Applied-level evidence (LO6); learner chooses how to show it |
| **Self-assessment against HETAICF descriptors** pre/post | M0, M6 | Makes the framework visible to learners and supports the self-assessment → offering path HETAICF recommends |

**Accessibility:** all tools have a text-based fallback; no activity requires a paid account; LLM activities can be done with the university's approved tool (⟨e.g. institution chat service⟩) or a local model (see Recyling/local-llm-workshop.md). Learners are told not to enter personal data (ST3).

---

## 6. Assessment

**Formative (not graded, needed for completion tracking):**
- One quiz per module (auto-graded in LiaScript/SCORM; unlimited attempts).
- Learning journal entries J0–J5 (free text, saved in the course and exported to the portfolio).

**Summative portfolio (pass/fail), submitted in the LMS:**
- **Part A – Explainer** (main piece): a 3–5 min video/audio, comic (6–12 panels), or illustrated one-pager (max. 600 words) explaining to a non-specialist audience *how a chatbot produces an answer and why it can be confidently wrong*.
- **Part B – Language audit**: take a real public text about AI (news, press release, university web page, ≥ 150 words), mark ≥ 5 anthropomorphic or imprecise statements, and rewrite each precisely with a one-sentence justification.
- **Part C – Reflection** (≤ 300 words): pre/post comparison of own beliefs and self-assessment, plus a declaration of independent work and AI use.

**Rubric** (4 criteria × 3 levels, see Module 6). Pass = at least "meets" in criteria 1–3 and no "not yet" in criterion 4.

| Criterion | Linked LOs |
|---|---|
| 1 Technical accuracy (data, inference, sampling, hallucination) | LO2–LO5 |
| 2 Precise, non-anthropomorphic language | LO1 |
| 3 Fit for a non-specialist audience | LO6 |
| 4 Critical transfer to own practice (Part B + C) | LO1, LO5 |

---

## 7. EU 10 principles: check

| Principle | How MC01 meets it |
|---|---|
| Quality | Internal QA ⟨procedure⟩; learner feedback survey at the end of M6; peer review by a second educator |
| Transparency | This descriptor, LOs, workload and rubric are published at the start of the course |
| Relevance | Answers the AI-literacy obligation (AI Act Art. 4) and the HETAICF student-profile minimum for D1 |
| Valid assessment | Rubric criteria derived directly from HETAICF E2 descriptors |
| Learning pathways | Self-paced, any semester, stackable in a D1 series |
| Recognition | ECTS-based, can be credited as an elective/key-competence module ⟨per examination regulations⟩ |
| Portability | Issued as a digital credential (⟨European Digital Credentials for Learning / Open Badge⟩), owned by the learner |
| Learner-centred | Choice of medium in the capstone; optional deep dives; personal journal |
| Authentic | Digitally signed credential via ⟨EDC issuer⟩ |
| Information & guidance | Module 0 explains the credential, the time plan and the next steps (follow-up competencies E3, E6, C3) |

---

## 8. Files and export

| File | Content |
|---|---|
| `00_Course_Design.md` | This document (for QA, recognition, educators) |
| `M0_Welcome.md` … `M6_Capstone.md` | Learner-facing LiaScript modules |

Preview: open a module in the [LiaScript LiveEditor](https://liascript.github.io/LiveEditor/) or host it on GitHub and open `https://liascript.github.io/course/?<raw-url>`.

SCORM export (requires Node.js):

```bash
npx @liascript/exporter --input M1_Words_Matter.md --format scorm1.2 --output MC01_M1
# or one package for the whole course: concatenate the modules (keep only the first header)
```

For SCORM 2004 use `--format scorm2004`. Quizzes are reported as score/completion to the LMS.
