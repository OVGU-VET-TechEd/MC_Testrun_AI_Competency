<!--
author: Hannes Tegelbeckers
email: hannes.tegelbeckers@ovgu.de
version: 2.0.0
language: de
narrator: Deutsch Female
comment: Interaktiver 40-minütiger Workshop zu KI-Anwendungen in der Hochschullehre für die Entwicklung von OER-Materialien
logo: https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/Tensorflow_logo.svg/1915px-Tensorflow_logo.svg.png

link: https://raw.githubusercontent.com/OVGU-VET-TechEd/Integrating_AI_in_TVET_UNESCO/refs/heads/main/Vorlage.css

@style
.sector-card {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 2rem;
    margin: 1rem;
    border-radius: 15px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    transition: transform 0.3s ease;
}

.sector-card:hover {
    transform: translateY(-5px);
}

.ai-tool-demo {
    background: #f8f9fa;
    border: 2px solid #007bff;
    border-radius: 10px;
    padding: 1.5rem;
    margin: 1rem 0;
}

.quiz-interactive {
    background: linear-gradient(45deg, #ff6b6b, #ffa726);
    color: white;
    padding: 1rem;
    border-radius: 10px;
    margin: 1rem 0;
}

.resource-link {
    background: #28a745;
    color: white;
    padding: 0.5rem 1rem;
    border-radius: 5px;
    text-decoration: none;
    display: inline-block;
    margin: 0.25rem;
    transition: all 0.3s ease;
}

.resource-link:hover {
    background: #218838;
    transform: scale(1.05);
}

.prompt-example {
    background: #e3f2fd;
    border-left: 4px solid #2196f3;
    padding: 1rem;
    margin: 1rem 0;
    border-radius: 0 5px 5px 0;
}
@end

@customQuiz
[[...]]
<script>
"@0" == btoa( "@input".trim().toLowerCase() )
</script>
@end

@aiDemo: <div class="ai-tool-demo">**🤖 KI-Demo:** @0<br>**🛠️ Tool:** @1<br>**🔗 Ausprobieren:** [Hier klicken](@2)</div>

@sectorCard: <div class="sector-card">**@0**<br>@1</div>

@resourceLink: <a href="@1" class="resource-link" target="_blank">@0</a>

@promptExample: <div class="prompt-example">**💡 Prompt-Beispiel:** @0<br><br>@1</div>

-->

# Lehrinnovationen im Dialog

<svg xmlns='http://www.w3.org/2000/svg' width='1100' height='400' viewBox='0 0 800 450'>
<!-- Background -->
<rect width='800' height='450' fill='#2196f3' />
<!-- White rounded rectangle container -->
<rect x='50' y='50' width='700' height='350' rx='20' fill='white' />
<!-- Main Title -->
<text x='400' y='100' font-family='Segoe UI, Arial, sans-serif' font-size='26' font-weight='bold' text-anchor='middle' fill='#2196f3'>
Lehrinnovationen im Dialog
</text>
<text x='400' y='130' font-family='Segoe UI, Arial, sans-serif' font-size='24' font-weight='bold' text-anchor='middle' fill='#2196f3'>
OER-Lehrmaterial mit KI entwickeln
</text>
<text x='400' y='160' font-family='Segoe UI, Arial, sans-serif' font-size='20' font-weight='bold' text-anchor='middle' fill='#2196f3'>
LiaScript und AI in der Hochschullehre
</text>
<!-- Author -->
<text x='400' y='200' font-family='Segoe UI, Arial, sans-serif' font-size='16' font-weight='bold' text-anchor='middle' fill='#666'>
Hannes Tegelbeckers
</text>
<text x='400' y='220' font-family='Segoe UI, Arial, sans-serif' font-size='14' text-anchor='middle' fill='#666'>
Wissenschaftlicher Mitarbeiter, Doktorand
</text>
<!-- Institution -->
<text x='400' y='245' font-family='Segoe UI, Arial, sans-serif' font-size='13' font-weight='bold' text-anchor='middle' fill='#999'>
Professur Ingenieurpädagogik und Didaktik der Technik
</text>
<text x='400' y='265' font-family='Segoe UI, Arial, sans-serif' font-size='13' font-weight='bold' text-anchor='middle' fill='#999'>
Otto-von-Guericke-Universität Magdeburg
</text>
<!-- Event Info -->
<text x='400' y='300' font-family='Segoe UI, Arial, sans-serif' font-size='14' font-weight='bold' text-anchor='middle' fill='#2196f3'>
Workshop Hochschullehre: 40 Minuten
</text>
<text x='400' y='320' font-family='Segoe UI, Arial, sans-serif' font-size='12' text-anchor='middle' fill='#666'>
Praktische Anwendungen von KI in der Lehrmaterialerstellung
</text>
<!-- Date -->
<text x='400' y='345' font-family='Segoe UI, Arial, sans-serif' font-size='12' text-anchor='middle' fill='#666'>
September 2025
</text>
<!-- Project Attribution -->
<text x='400' y='375' font-family='Segoe UI, Arial, sans-serif' font-size='11' text-anchor='middle' fill='#999'>
Digital Skills to Succeed in Asia (DS2S) Projekt | Gefördert durch BMZ
</text>
</svg>

<!-- License info -->
<div style="position: fixed; bottom: 10px; right: 10px; font-size: 12px; opacity: 0.7;">
  <img src="https://licensebuttons.net/l/by-sa/4.0/80x15.png" alt="CC BY-SA" style="height: 20px; vertical-align: middle;">
  <a href="https://creativecommons.org/licenses/by-sa/4.0/" style="margin-left: 5px; text-decoration: none;">CC BY-SA 4.0</a>
</div>

---

# 🎯 Lernziele

📌 **Was Sie heute lernen:**

- Den Rahmen und Kontext für KI-Einsatz in Open Educational Resources verstehen
- Ihre KI-Toolbox mit praktischen Anwendungen erweitern
- Textbasierte Ansätze (Markdown) für die Erstellung von Lehr- und Lernmaterialien beherrschen
- Hands-on Erfahrungen mit LiaScript und KI-Integration sammeln
- Konkrete Prompt-Strategien für die Materialerstellung entwickeln

**🎯 Zielgruppe:** Lehrende an Hochschulen, die innovative digitale Lernmaterialien entwickeln möchten

---

# 🤖 Was ist Künstliche Intelligenz?

📊 **Aktuelle Realität:**

- Keine universell akzeptierte Definition
- Wir sprechen hauptsächlich über **Wahrscheinlichkeitsmaschinen**
- KI lernt aus historischen Daten und präsentiert vergangene Muster

🧠 **Der menschliche Faktor:**

- Wir schreiben generiertem Text Verständnis oder Bewusstsein zu, wo keines existiert
- Kritische Überlegung: Welche Prozesse wollen wir tatsächlich automatisieren?

## 🎯 KI-Exzellenz-Beispiele

✅ KI glänzt in spezifischen Aufgaben:
- 🏥 Krebs erkennen in medizinischer Bildgebung
- 🌾 Bewertung der Erntequalität in der Landwirtschaft
- 🔧 Qualitätskontrolle in Schweißprozessen
- 🚗 Autonome Fahrzeugnavigation
- 📊 Betrugserkennung im Finanzwesen
- 🎵 Musikkomposition und -analyse

---

# 📚 Open Educational Resources (OER)

## 🌍 Definition und Umfang (2019)

**Open Educational Resource (OER)** 

- *Dubai-Deklaration*:
> Lern-, Lehr- und Forschungsmaterialien in jedem Format und Medium, die gemeinfrei sind oder unter einem Urheberrecht stehen, aber unter einer **offenen Lizenz** veröffentlicht wurden, die kostenlosen Zugang, Wiederverwertung, Zweckänderung, Anpassung und Weiterverbreitung durch andere ermöglicht.

🎯 **Hauptmerkmale:**

- 📖 Umfasst Lehrbücher, Multimedia, Kursmaterialien
- 🤝 Priorisiert Inklusion, Gerechtigkeit und Zusammenarbeit
- 🤖 Durch KI verbessert für bessere Zugänglichkeit und Anpassbarkeit

## 🔑 Framework für offene Lizenzen

**Offene Lizenz** = Rechtliches Werkzeug, das ermöglicht:

- ✅ Eigentumsrechte der Ersteller*innen wahren
- ✅ Nutzungsbedingungen für andere festlegen
- ✅ Kostenlose Nutzung, Wiederverwendung, Anpassung und Weiterverbreitung ermöglichen
- ✅ Ordnungsgemäße Namensnennung sicherstellen
- ⚖️ **Neue Herausforderung:** Rechte zur Nutzung von KI-Trainingsdaten klären

## 📋 Wichtige OER-Erklärungen

🔗 **Ljubljana-Erklärung:**
[UNESCO OER Ljubljana Empfehlung](https://www.unesco.org/en/legal-affairs/oer-recommendation)

🔗 **UNESCO 2019 Empfehlung:**
[UNESCO OER Empfehlung](https://unesdoc.unesco.org/ark:/48223/pf0000373755)
*Hinweis: Regierungen berichten alle 4 Jahre über die Umsetzung*

🔗 **Dubai-Erklärung:**
[Dubai OER Erklärung](https://www.unesco.org/en/articles/dubai-declaration-open-educational-resources)

---

# 🧑‍🏫 UNESCO KI-Framework für Lehrende

| Kompetenz | 📖 Erwerben | 🔍 Vertiefen | 🚀 Erschaffen |
|-----------|-------------|-------------|---------------|
| **🧠 Menschenzentrierte Denkweise** | Kritische Reflexion über KI-Vorteile, -Grenzen und -Risiken in lokalen Kontexten | Anwendung menschenzentrierter Prinzipien bei der KI-Tool-Auswahl | Gestaltung KI-verbesserter Erfahrungen mit Fokus auf menschliche Handlungsfähigkeit |
| **⚖️ KI-Ethik** | Grundlegende KI-ethische Prinzipien verstehen | Ethische Implikationen von KI in der Bildung analysieren | Ethische Richtlinien für KI-Einsatz in der Lehre entwickeln |
| **🔧 KI-Grundlagen & Anwendungen** | Grundlegende KI-Konzepte und Bildungstools lernen | KI-Tools in die Lehrpraxis integrieren | Innovative KI-verbesserte Lernlösungen erstellen |
| **🎓 KI-Pädagogik** | Rolle der KI in der Pädagogik verstehen | Lehrmethoden mit KI-Unterstützung anpassen | KI-integrierte pädagogische Ansätze gestalten |
| **📈 KI für berufliche Weiterentwicklung** | KI für persönliche berufliche Entwicklung nutzen | Zusammenarbeit mit KI für kontinuierliches Lernen | Führung bei der beruflichen Entwicklung in KI-Kompetenz |

🔗 [UNESCO KI-Kompetenzrahmen für Lehrende 2024](https://www.unesco.org/en/digital-education/ai-future-learning)

---

# 💡 Warum LiaScript?

**🎯 Textbasierte Vorteile**

- **📝 Einfache Erstellung** - Leicht zu generieren, bearbeiten und teilen
- **🔄 Dynamische Darstellung** - Interaktiv vs. statische Präsentationen
- **🌍 Übersetzungsbereit** - Textbasierte Inhalte sind leicht übersetzbar
- **🔗 Plattformunabhängig** - Funktioniert überall, wo Markdown unterstützt wird

## 🤔 Strategische Überlegungen

**Ihre Datenstrategie-Fragen:**

- 📊 Was ist Ihre Datenstrategie?
- 🗝️ Wie wird sie Plattform- und Systementscheidungen beeinflussen?
- 🔮 Wie wird sie zukünftige Integration digitaler Ökosysteme beeinflussen?
- 🎯 Wie wird sie Learning Management Systems (LMS) Implementierung unterstützen?
- 🤖 Wie wird sie Intelligente Tutorsysteme und personalisiertes Lernen ermöglichen?
- 🏭 Wie wird sie sich an verändernde Anforderungen der Industrie anpassen?

## 💻 LiaScript für die Hochschullehre

**📖 Besonders geeignet für:**
- Interaktive Vorlesungsfolien
- Selbstlernmodule mit Quizzes
- Mehrsprachige Kursmaterialien
- Kollaborative Materialentwicklung

---

# 🛠️ KI-Tool-Beispiele

## 💬 Large Language Models (LLMs)

@aiDemo(Fortgeschrittene Konversations-KI für Forschung und Analyse, Perplexity AI, https://perplexity.ai)

@aiDemo(Ausgefeilte Argumentation und Textgenerierung, Claude AI, https://claude.ai)

@aiDemo(Microsofts KI-Assistent mit Web-Integration, Copilot, https://copilot.microsoft.com)

@aiDemo(OpenAIs Flaggschiff-Konversations-KI, ChatGPT, https://chat.openai.com)

## 🎨 Präsentations- und Kreativtools

@aiDemo(Grammatik und Schreibverbesserung, Grammarly, https://grammarly.com)

@aiDemo(Visuelle Präsentationserstellung mit KI, Napkin AI, https://napkin.ai)

@aiDemo(Interaktives Notizbuch für KI-Experimente, LM Notebook, https://lmnotebook.com)

@aiDemo(KI-basierte Präsentationserstellung, Gamma, https://gamma.app)

## 💻 Lokale KI-Implementierung

**GUI-basierte Lösungen:**

@resourceLink(GPT4ALL, https://gpt4all.io)
@resourceLink(Ollama GUI, https://ollama.ai)
@resourceLink(Hugging Face Spaces, https://huggingface.co/spaces)

**Kommandozeilen-Lösungen:**
@resourceLink(Ollama CLI, https://ollama.ai)

## 🎭 Avatar-Generierung

@aiDemo(KI-gesteuerte Video-Avatar-Erstellung, HeyGen AI, https://heygen.com)

---

# 📝 Prompting-Grundlagen

## 🤔 Was ist ein Prompt?
Ein Prompt ist Ihre Anweisung oder Anfrage an ein KI-System - der Input, der die Antwort der KI steuert.

## 🎯 Googles 5-Schritte-Framework

**Effektive Prompt-Struktur:**

1. **📋 Aufgabe:** Klar definieren, was die KI tun soll
2. **🌍 Kontext:** Hintergrundinformationen und relevante Details bereitstellen
3. **📚 Referenzen:** Externe Quellen oder Materialien einbeziehen
4. **✅ Bewerten:** Kriterien für die Bewertung der Ausgabequalität festlegen
5. **🔄 Iterieren:** Prozess zur Verfeinerung basierend auf Feedback

## 🧠 Erweiterte Techniken

**🔗 Chain of Thought (CoT):**
Schritt-für-Schritt-Argumentation durch komplexe Probleme fördern.

**🌳 Tree of Thought (ToT):**
Exploration mehrerer Argumentationszweige gleichzeitig für umfassende Analyse ermöglichen.

---

# 🎓 Prompt-Beispiele für Hochschullehre

## 📖 Lehrmaterialerstellung

@promptExample(Skript-Entwicklung, "Erstelle ein Kapitel für ein Hochschulskript über [THEMA]. Das Kapitel soll für [ZIELGRUPPE] geeignet sein und folgende Lernziele erfüllen: [LERNZIELE]. Verwende eine akademische Sprache und integriere praktische Beispiele.")

@promptExample(Übungsaufgaben generieren, "Entwickle 5 Übungsaufgaben verschiedener Schwierigkeitsgrade für das Thema [THEMA]. Jede Aufgabe soll eine Musterlösung und eine Bewertungsrubrik enthalten. Achte auf praxisnahe Szenarien aus dem [FACHBEREICH].")

@promptExample(Quiz erstellen, "Erstelle ein interaktives Quiz mit 10 Multiple-Choice-Fragen für [THEMA]. Jede Frage soll 4 Antwortmöglichkeiten haben, mit ausführlichen Erklärungen für richtige und falsche Antworten. Gestalte es für LiaScript-Format.")

## 🔬 Forschungsunterstützung

@promptExample(Literaturzusammenfassung, "Analysiere diese wissenschaftlichen Paper zu [THEMA] und erstelle eine strukturierte Zusammenfassung mit: 1) Haupterkenntnissen, 2) Methodischen Ansätzen, 3) Forschungslücken, 4) Relevanz für [ANWENDUNGSBEREICH].")

@promptExample(Konzeptuelle Erklärungen, "Erkläre das Konzept [KOMPLEXES THEMA] auf drei Ebenen: 1) Für Studierende im ersten Semester, 2) Für fortgeschrittene Studierende, 3) Für Fachexperten. Verwende jeweils angemessene Beispiele und Analogien.")

## 🌍 Mehrsprachige Materialien

@promptExample(Übersetzung und Lokalisierung, "Übersetze dieses Lehrmaterial von Deutsch ins Englische und passe es an internationale Studierende an. Berücksichtige kulturelle Unterschiede und verwende internationale Beispiele statt deutscher Bezüge.")

---

# 🛠️ Praxis-Workshop

## 🎯 Ihr Selbstlern-Tool entwickeln

**Schritt-für-Schritt-Prozess:**

1. **🎯 Ziele definieren:** Klare Lernziele festlegen
2. **📋 Methoden wählen:** Geeignete Lehr-/Lernansätze auswählen  
3. **🔧 Tools bestimmen:** Interaktive Elemente und Funktionen festlegen
4. **🤖 LLM auswählen:** Ihr KI-Tool wählen und Entscheidung begründen
5. **💻 In LiaScript erstellen:** Ihr Selbstlern-Tool entwickeln
6. **🚀 Testen & Einsetzen:** Mit [LiaScript Live Editor](https://liascript.github.io/LiveEditor/) arbeiten

## 🔧 Praktische Übung (15 Minuten)

**Aufgabe:** Erstellen Sie ein kurzes Lernmodul zu einem Thema Ihres Fachbereichs

**Vorlage verwenden:**
```markdown
# Mein Lernmodul: [TITEL]

## Lernziele
- [ ] Ziel 1
- [ ] Ziel 2
- [ ] Ziel 3

## Inhalt
[Hier KI-generierte Erklärung einfügen]

## Übung
[Hier KI-generierte Aufgabe einfügen]

## Quiz
[[X]] Richtige Antwort
[[ ]] Falsche Antwort 1
[[ ]] Falsche Antwort 2
[[ ]] Falsche Antwort 3
```

## 📝 Template-Ressourcen

🔗 **Startvorlage:** [Selbstlern-Template](https://raw.githubusercontent.com/OVGU-VET-TechEd/Self_Learning_Nuggets_AI_Basics/refs/heads/main/Self_Learning_Nugget_Outlinefile_V6.md)

🔗 **Mega-Prompt Beispiel:** [Advanced Prompting Guide](https://raw.githubusercontent.com/OVGU-VET-TechEd/Self_Learning_Nuggets_AI_Basics/refs/heads/main/Prompt_Feedback_V2.md)

---

# 🔧 Prompt-Verfeinerungs-Techniken

## 📊 Prompt-Engineering für Hochschullehre

**🎯 Spezifische Strategien:**

- **Rollenbasierte Prompts:** "Du bist Professor für [FACH] und erstellst Material für [ZIELGRUPPE]"
- **Strukturierte Ausgaben:** "Formatiere die Antwort als: 1) Einführung, 2) Hauptteil mit 3 Unterpunkten, 3) Zusammenfassung"
- **Qualitätskriterien:** "Verwende wissenschaftliche Quellen und akademische Sprache auf Niveau [SEMESTER]"

## 📚 Zusätzliche Ressourcen

🔗 **KI Campus:** [KI Prompting Kurs](https://ki-campus.org)
🔗 **AI-27 Prompt Support:** [Prompting Tools](https://ai-27.com)
🔗 **Hochschulforum Digitalisierung:** [KI in der Hochschullehre](https://hochschulforumdigitalisierung.de)

## 📖 Prompt-Bibliotheken

@resourceLink(AI for Education Library, https://www.aiforeducation.io)
@resourceLink(Microsoft Education Prompts, https://education.microsoft.com/en-us/resource/9c8f)
@resourceLink(UNIGlobal Careers Prompts, https://www.uniglobalcareers.com/ai-prompts)

## 🎥 Erweiterte Lernressourcen

🔗 **Umfassender Guide:** [KI Content-Erstellung mit LiaScript](https://liascript.github.io/course/?https://raw.githubusercontent.com/LiaPlayground/content-creation-with-ai/refs/heads/main/README.md)

---

# 💬 Diskussion und Feedback

## 🤔 Reflexionsfragen

**📊 Zufriedenheitsbewertung:**

- Wie zufrieden sind Sie mit dem Inhalt unter Berücksichtigung der investierten Zeit?
- Welche Aspekte funktionierten gut für Ihr Lernen?
- Welche Bereiche müssen verbessert werden?
- Wo sehen Sie Verbesserungsmöglichkeiten?

## 🚀 Zukünftige Anwendungen

**🎯 Überlegen Sie:**

- Wie werden Sie diese Tools in Ihrer Lehre umsetzen?
- Welche zusätzliche Unterstützung benötigen Sie?
- Welche Konzepte erfordern weitere Erkundung?

## 💡 Nächste Schritte

**📋 Action Items:**

1. Ein LiaScript-Modul für Ihren nächsten Kurs erstellen
2. KI-Tools in der Materialvorbereitung testen
3. Kolleg*innen über OER und KI informieren
4. Feedback zu entwickelten Materialien einholen

---

# 📚 UNESCO Digital Learning Resources

## 🎓 Politik- und Leitfadendokumente

@resourceLink(KI und Bildung: Leitfaden für Politik, https://www.unesco.org/en/articles/artificial-intelligence-education-guidance-policy-makers)

@resourceLink(Beijing Konsensus zu KI und Bildung, https://www.unesco.org/en/articles/beijing-consensus-artificial-intelligence-and-education)

@resourceLink(UNESCO Ethik der KI Empfehlung, https://www.unesco.org/en/artificial-intelligence/recommendation-ethics)

@resourceLink(IKT in der Bildung Policy Guidelines, https://www.unesco.org/en/education/digital-transformation/guidelines-policy)

## 🔗 Spezialisierte Ressourcen

@resourceLink(Bildung und Blockchain, https://www.unesco.org/en/articles/blockchain-education)

@resourceLink(Gateways to Public Digital Learning, https://www.unesco.org/en/education/digital-transformation/gateways)

@resourceLink(King Hamad Preisträger, https://www.unesco.org/en/prizes-fellowships/hamad-bin-isa-al-khalifa)

## 📊 Forschungskompendien

@resourceLink(KI und Inklusion Initiativen 2020, https://www.unesco.org/en/weeks/digital-learning/2020/compendium)

@resourceLink(KI in Bildung Initiativen 2019, https://www.unesco.org/en/weeks/digital-learning/2019/compendium)

@resourceLink(Beyond Disruption Report 2020, https://www.unesco.org/en/weeks/digital-learning/2020/report)

## 👨‍🏫 Lehrenden-spezifische Ressourcen

@resourceLink(Teacher Agency im KI-Zeitalter 2025, https://teachertaskforce.org/knowledge-hub/promoting-and-protecting-teacher-agency-age-artificial-intelligence)

## 🌍 OECD KI-Tools

@resourceLink(OECD KI Policy Observatory, https://oecd.ai/en/catalogue/overview)

## 🇩🇪 Deutsche Ressourcen

@resourceLink(KI Campus Deutschland, https://ki-campus.org)
@resourceLink(Hochschulforum Digitalisierung, https://hochschulforumdigitalisierung.de)
@resourceLink(DINI Deutsche Initiative für Netzwerkinformation, https://dini.de)

---

**🎉 Vielen Dank für Ihre Teilnahme!**

> 🚀 *Bereit, die Zukunft der KI-verbesserten Hochschullehre zu gestalten?*

**📧 Kontakt:** hannes.tegelbeckers@ovgu.de
**🌐 Weitere Ressourcen:** [LiaScript Community](https://liascript.github.io)