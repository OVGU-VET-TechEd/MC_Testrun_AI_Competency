# LiaScript Nutzungsanleitung - GitHub Integration und Kurs-Einbettung

## 📚 Was ist LiaScript?

LiaScript ist ein textbasiertes Autorensystem für interaktive Lernmaterialien, das Markdown erweitert und folgende Vorteile bietet:

- **📝 Einfache Erstellung** - Leicht zu generieren, bearbeiten und teilen
- **🔄 Dynamische Darstellung** - Interaktiv vs. statische Präsentationen  
- **🌍 Übersetzungsbereit** - Textbasierte Inhalte sind leicht übersetzbar
- **🔗 Plattformunabhängig** - Funktioniert überall, wo Markdown unterstützt wird

## 🚀 Zwei Hauptwege zur LiaScript-Nutzung

### 1. 🌐 Direkte Kurs-Einbettung über liascript.github.io/course/

**URL-Schema:**
```
https://liascript.github.io/course/?[RAW-GITHUB-URL]
```

**Beispiel aus dem Dokument:**
```
https://liascript.github.io/course/?https://raw.githubusercontent.com/LiaPlayground/content-creation-with-ai/refs/heads/main/README.md
```

**Vorteile:**
- ✅ Sofortige Darstellung ohne lokale Installation
- ✅ Automatische Renderung der LiaScript-Syntax
- ✅ Interaktive Elemente funktionieren direkt
- ✅ Teilen über einfache URL möglich

### 2. 📁 GitHub Raw-Dateien Methode

**Schritt-für-Schritt-Anleitung:**

#### Schritt 1: GitHub Repository erstellen
```bash
# Neues Repository erstellen oder bestehendes nutzen
git clone https://github.com/IhrUsername/IhrRepository.git
```

#### Schritt 2: LiaScript-Datei erstellen
Erstellen Sie eine `.md` Datei mit LiaScript-Metadaten im Header:

```markdown
<!--
author: Ihr Name
email: ihre.email@domain.de
version: 1.0.0
language: de
narrator: Deutsch Female
comment: Beschreibung Ihres Kurses
logo: https://upload.wikimedia.org/wikipedia/commons/...

link: https://raw.githubusercontent.com/.../.../style.css

@customQuiz
[[...]]
<script>
"@0" == btoa( "@input".trim().toLowerCase() )
</script>
@end

-->

# Ihr Kurstitel

Inhalt hier...
```

#### Schritt 3: Datei zu GitHub hochladen
```bash
git add .
git commit -m "LiaScript Kurs hinzugefügt"
git push origin main
```

#### Schritt 4: Raw-URL ermitteln
1. Gehen Sie zu Ihrer Datei auf GitHub
2. Klicken Sie auf "Raw"
3. Kopieren Sie die URL (Format: `https://raw.githubusercontent.com/Username/Repository/branch/datei.md`)

#### Schritt 5: In LiaScript einbetten
Verwenden Sie die URL im LiaScript-Course-Viewer:
```
https://liascript.github.io/course/?https://raw.githubusercontent.com/IhrUsername/IhrRepository/main/IhrKurs.md
```

## 🛠️ Wichtige LiaScript-Features aus dem Beispiel

### Metadaten-Header
```markdown
<!--
author: Hannes Tegelbeckers
email: hannes.tegelbeckers@ovgu.de
version: 2.0.0
language: de
narrator: Deutsch Female
comment: Interaktiver Workshop...
-->
```

### Custom CSS-Stile
```markdown
link: https://raw.githubusercontent.com/.../style.css

@style
.sector-card {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    /* ... weitere Stile ... */
}
@end
```

### Interaktive Quiz-Elemente
```markdown
@customQuiz
[[...]]
<script>
"@0" == btoa( "@input".trim().toLowerCase() )
</script>
@end

# Verwendung:
[[X]] Richtige Antwort
[[ ]] Falsche Antwort 1
[[ ]] Falsche Antwort 2
```

### Custom Macros
```markdown
@aiDemo: <div class="ai-tool-demo">**🤖 KI-Demo:** @0<br>**🛠️ Tool:** @1<br>**🔗 Ausprobieren:** [Hier klicken](@2)</div>

@sectorCard: <div class="sector-card">**@0**<br>@1</div>

@resourceLink: <a href="@1" class="resource-link" target="_blank">@0</a>
```

## 🔧 Entwicklungstools

### LiaScript Live Editor
**URL:** https://liascript.github.io/LiveEditor/

**Features:**
- ✏️ Live-Vorschau während der Bearbeitung
- 🚀 Sofortige Darstellung von Änderungen
- 💾 Export-Funktionen
- 🔍 Syntax-Highlighting

### Template-Ressourcen
Aus dem Dokument:
- **Startvorlage:** [Selbstlern-Template](https://raw.githubusercontent.com/OVGU-VET-TechEd/Self_Learning_Nuggets_AI_Basics/refs/heads/main/Self_Learning_Nugget_Outlinefile_V6.md)
- **Mega-Prompt Beispiel:** [Advanced Prompting Guide](https://raw.githubusercontent.com/OVGU-VET-TechEd/Self_Learning_Nuggets_AI_Basics/refs/heads/main/Prompt_Feedback_V2.md)

## 📋 Best Practices für GitHub-Integration

### 1. Repository-Struktur
```
IhrRepository/
├── README.md (Hauptkurs)
├── kapitel1.md
├── kapitel2.md
├── assets/
│   ├── images/
│   └── css/
└── templates/
```

### 2. Branching-Strategie
- `main` - Produktive Version
- `dev` - Entwicklungsversion  
- `feature/xyz` - Neue Features

### 3. Versionierung
```markdown
<!--
version: 2.0.0
-->
```
Nutzen Sie semantische Versionierung (Major.Minor.Patch)

### 4. Lizenzierung
```html
<div style="position: fixed; bottom: 10px; right: 10px; font-size: 12px; opacity: 0.7;">
  <img src="https://licensebuttons.net/l/by-sa/4.0/80x15.png" alt="CC BY-SA">
  <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>
</div>
```

## 🎯 Workflow-Beispiel

### Schneller Start:
1. **Template kopieren** → Von GitHub-Repository clonen
2. **Inhalte anpassen** → Mit KI-Tools Inhalte generieren
3. **Live testen** → Im LiaScript Live Editor
4. **GitHub deployen** → Push zu GitHub
5. **Teilen** → URL mit `liascript.github.io/course/?` verwenden

### URL-Format verstehen:
```
Base-URL: https://liascript.github.io/course/
Parameter: ?[RAW-GITHUB-URL]
Vollständig: https://liascript.github.io/course/?https://raw.githubusercontent.com/user/repo/branch/file.md
```

## 🔗 Wichtige Ressourcen

- **LiaScript Community:** https://liascript.github.io
- **Live Editor:** https://liascript.github.io/LiveEditor/
- **Dokumentation:** https://liascript.github.io/course/
- **GitHub Templates:** Siehe Beispiel-URLs im Workshop-Material

## ⚡ Tipps für den Einsatz in der Hochschullehre

1. **Modularer Aufbau:** Einzelne Kapitel als separate .md-Dateien
2. **Interaktivität:** Quizzes und Übungen integrieren
3. **Mehrsprachigkeit:** Sprachvarianten in verschiedenen Branches
4. **KI-Integration:** Prompts zur Content-Generierung nutzen
5. **Kollaboration:** GitHub-Issues für Feedback nutzen