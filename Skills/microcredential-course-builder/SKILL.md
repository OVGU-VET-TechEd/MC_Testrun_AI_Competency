---
name: microcredential-course-builder
description: Build a complete self-learning micro-credential course (1 ECTS ≈ 30 h) on an AI competency, aligned to the HETAICF framework and the EU approach to micro-credentials, written as LiaScript Markdown (exportable to SCORM). Use when asked to design, outline or write another micro-credential / AI-literacy self-learning unit from the /Reading, /Recyling, /Framework and /Tools folders.
---

# Micro-credential course builder (HETAICF × EU × LiaScript)

Repeatable procedure distilled from building the first course
(`Courses/MC01_E2_How_AI_Works`). Follow the steps in order; each step names its
inputs and the artefact it must leave behind.

## 0. Folder map (inputs)

| Folder | What it contains | Use it for |
|---|---|---|
| `Reading/` | EU brochure (2021), UNESCO definition report, papers (Delgado Kloos 2025 MC+AI; De Rosa 2024 stackable MC; Gillet AI-augmented OER) | Mandatory/optional EU elements, 10 principles, UNESCO 4-point definition |
| `Microcrededntials EU approach.md` | LiaScript seminar summarising the EU approach | Quick reference instead of re-reading the PDF |
| `Recyling/` | Earlier LiaScript workshops (prompting, local LLMs, GenAI in HE, OER creation, LiaScript how-to) | House style, LiaScript header conventions, reusable content blocks |
| `Framework/` | HETAICF v0.13 (19 core competencies, 4 domains, 3 levels, 3 profiles) | Pick competency + level; copy definition **verbatim** |
| `Tools/interactive-ai-learning-websites.md` | Curated interactive explainers (TF Playground, Teachable Machine, R2D3, Transformer Explainer, Diffusion Explainer, …) | Hands-on activities (one tool ≈ one Predict–Observe–Explain cycle) |
| `Skills/` | This file, `references/liascript-cheatsheet.md`, `scripts/check_course.py`, `scripts/combine_modules.py` | Re-use |

Text extraction (no system pdftotext): `textutil -convert txt` for .docx;
`pip3 install --target ./pylib pypdf` in the scratchpad, then `PYTHONPATH=pylib python3`
for PDFs. In zsh, never `echo =====` (glob error) – use `echo "---"`.

## 1. Read and extract (≈ 10 % of effort)

1. Framework: read `HETAICF_v0_13_Kurzueberblick_DE` first (structure), then
   `HETAICF_Definitions_EN-DE_tracked` for the **English** definition + level descriptors
   + object scope (O1–O5), and `Fundament_und_Profile_DE` for profile target levels
   (G = Grundlegend/Foundation, F = Fortgeschritten/Applied).
2. EU brochure: mandatory elements (11), optional elements (5), 10 principles.
3. UNESCO: 4-point definition (record of focused achievement · assessment against
   clear standards by trusted provider · standalone + stackable · QA).
4. Tools list: map each tool to the mechanism it makes visible.

## 2. Decide (ask the user only what you cannot derive)

Decide yourself (state choice + reason): competency, level target, didactic design,
format (LiaScript), module split, workload split.
**Ask** the user (AskUserQuestion, one round, ≤ 3 questions):
- Language (EN / DE / both)
- Assessment model (portfolio + tutor / fully automated / peer)
- Anything institution-specific you cannot know (awarding body name, QA body) – otherwise use clearly marked placeholders `⟨…⟩`.

Decisions taken in course MC01 (defaults for the next ones unless user says otherwise):
English · portfolio + tutor rubric · LiaScript · one file per module · pass/fail.

### Picking the competency
- Profile **Students**: all 19 core at Foundation; Applied for E3, C1, C3, C4, M1, M3;
  profile competencies ST1–ST4.
- 1 ECTS fits: **Foundation fully + first step into Applied** of ONE core competency,
  touching 1–2 neighbours (name them as "touched, not certified").
- Prefer competencies whose mechanisms can be *seen* in the Tools list.
- Already built: MC01 = E2. Good next candidates: E3 (evaluate outputs), E6 (bias,
  Teachable Machine + data), C3 (prompting, recycle Recyling/ prompting material),
  E5 (resources), ST2 (own learning with AI).

## 3. Align (the course design document)

Write `00_Course_Design.md` with, in this order:
1. **EU micro-credential descriptor** – all 11 mandatory elements + optional ones (table).
   Workload "1 ECTS (30 h)"; level EQF 6 / QF-EHEA 1st cycle; form "online, self-paced".
2. **Competency alignment** – verbatim HETAICF definition (EN) + level descriptors,
   the target level, and the profile it serves.
3. **Learning outcomes** – 5–6, observable verbs, each tagged with the HETAICF
   descriptor it operationalises (constructive alignment table: LO → activity → evidence).
4. **Workload table** – modules × hours; must sum to exactly 30 h; split roughly
   ⅓ reading/watching, ⅓ hands-on, ⅓ producing/reflecting.
5. **Didactic design rationale** (see §4).
6. **Assessment** – formative (quizzes, journal) vs summative (capstone + rubric);
   pass threshold.
7. **QA & EU 10 principles check** – one line per principle.
8. **SCORM/export notes.**

## 4. Didactic patterns that worked (re-use, vary)

- **Narrative frame**: one recurring case/character across modules (MC01: a
  student newsroom fact-checking AI headlines). Gives self-learners a reason to continue.
- **Conceptual change**: elicit misconceptions first (belief poll), then confront
  them with a demo, then re-poll at the end (pre/post).
- **Predict – Observe – Explain (POE)** for every external tool: *predict* in a
  text field, *observe* in the tool, *explain* in precise language.
- **Unplugged / be-the-model**: learner does the algorithm by hand (counting
  bigrams, a decision tree on paper) before seeing it automated.
- **Runnable micro-model in LiaScript** (`<script>@input</script>`): editable JS the
  learner can change (corpus, temperature). Keep it < 60 lines, ES5-safe, `console.log` output.
- **Language translation drills** (anthropomorphic → precise) with inline
  selection quizzes `[[ a | (b) | c ]]`.
- **Learning journal**: 1 entry per module, prompts given, collected into the portfolio.
- **Capstone with authentic audience** (explain to non-specialists) + rubric that
  mirrors the HETAICF descriptors.
- **Self-assessment** against the framework descriptors at start and end.

## 5. Write the modules (LiaScript)

- One file per module: `0X_Title.md`, each with the standard LiaScript header
  (see `references/liascript-cheatsheet.md`). Each module = 1 SCORM package, or
  concatenate for one package.
- Module skeleton: Why this matters (case) → Learning outcomes → Warm-up/poll →
  Content chunks (≤ 300 words each, then an activity) → Tool POE → Quiz → Journal
  prompt → Summary + "precise language box" → time estimate per page.
- Put time estimates in each page heading area (`⏱ 20 min`) so learners can pace.
- Keep external tools optional-proof: always give a fallback (screenshot description
  or unplugged alternative) in case a site is down.
- Language rule for E2-type courses: authors must themselves avoid anthropomorphic
  wording ("the model thinks/knows/understands") – lint with
  `grep -n -i -E "thinks|knows|understands|believes|wants|lies" *.md` and keep only
  hits that are deliberate examples.

## 6. Verify (use the scripts)

```bash
python3 Skills/microcredential-course-builder/scripts/check_course.py Courses/<MCxx_folder>
python3 Skills/microcredential-course-builder/scripts/combine_modules.py Courses/<MCxx_folder> Courses/<MCxx_folder>/MCxx_Complete_Course.md "<title>"
```

- `check_course.py`: page times (`> ⏱ nn min`) must add up to each module's stated total
  (±10 min), and the module totals must add up to 30 h; solution blocks balanced; every js
  block runnable; anthropomorphism lint (**review every hit**, since deliberate examples are
  fine but slips in your own author voice are not. MC01 had one: "T = 0.1 can't decide").
- Extract every ```js block and run it with jsc (see cheatsheet). **Recompute every number
  you state** (MC01: claimed loss "≈ 15", actual 12.5).
- Every LO appears in ≥ 1 activity and in the rubric; all 11 EU mandatory elements present.
- Links copied exactly from the Tools list; each external tool has a fallback.
- Avoid unsourced empirical claims ("surveys show …"); cite or rephrase.

## 7. Hand-off

Create `README.md` in the course folder (file table, preview, SCORM export, rebuild
commands, open placeholders). Tell the user where files are, how to preview
(LiaScript LiveEditor or `https://liascript.github.io/course/?<raw-url>`), how to export
(`npx @liascript/exporter --input MCxx_Complete_Course.md --format scorm1.2 --output name`),
and list open `⟨…⟩` placeholders. Do not claim the SCORM export was tested unless Node was
available and it ran.

## 8. Lessons learned (pitfalls)

- First drafts underestimate time: page estimates summed to 25 h of the 30 h. Write the
  workload table first, then **budget minutes per page** while writing.
- Hands-on tool POEs take longer than you'd expect: Teachable Machine with 2 rounds ≈ 90 min,
  TensorFlow Playground with 3 experiments ≈ 90 min, Transformer Explainer with 4 rounds ≈ 90 min.
- The combined file takes M0's header, so **M0 must define every style class** used anywhere.
- Glob `M[0-9]*.md`, not `M*.md`, or the combined `MCxx_Complete_Course.md` includes itself.
- Text-input quizzes need exact matches: one-word answers only, otherwise use single choice.
- The "one sentence of the course" must be true for **all** system families it covers
  (rule-based patterns are written, not fitted). Check the core claim against each module.
- Unplugged counting tasks: include **every** token type in the table (the full stop too).
- A runnable toy model that produces errors from true data (bigram on 4 true sentences →
  "the river spree flows through magdeburg") is the strongest single demo for hallucination.
  Reuse it.

## Course structure template (copy for MCxx)

```
Courses/MCxx_<Competency>_<Short_Title>/
  README.md
  00_Course_Design.md
  M0_Welcome.md            1–1.5 h  frame, credential info, pre-poll, self-assessment, J0
  M1_… – M5_…              3.5–6 h each, one per part of the core sentence
  M6_Capstone.md           5–5.5 h  portfolio A/B/C, rubric, post-poll, feedback survey
  MCxx_Complete_Course.md  generated
```

## Log of runs
- 2026-10-02 · MC01 · E2 "Describe how AI systems perform tasks in accurate,
  non-anthropomorphic language" · Students profile · EN · portfolio+tutor ·
  `Courses/MC01_E2_How_AI_Works` · 7 modules, ~2,100 lines · not yet exported to SCORM
  (no Node on machine).
