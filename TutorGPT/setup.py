import fitz
from random import randint

doc = None

message_explanation = """### Definition 📝:
{Definition des Themas oder Konzepts}

### Ausführliche Erklärung: 📖
{Detaillierte Erklärung aller Informationen, inklusive aller Fachbegriffe, Formeln und Rechenwegen}

### Einfache Erklärung 🧩:
{So einfach wie möglich, aber dennoch vollständig}

### Praktisches Beispiel 🧑‍💻:
{Beispiel, welches das Thema/Konzept veranschaulicht}

### Mnemonic 🧠:
{Mnemonic, wodurch die Inhalte leichter zu merken sind}

### Formelsammlung 🧮:
{ALLE Formeln/Gleichungen in LaTeX-Syntax mit Erklärung}"""

def get_example(index):
    examples = [
    f"""## [Thema + Emoji als Titel]
    {message_explanation}
    
    ---

    ### Befehle 🤖
    1. 🔍
    2. ⏩
    3. ❓
    4. 🧩
    5. 🖥️
    6. 🧮
    7. 🗣️
    8. 📈""",
    f"""## [Thema + Emoji als Titel]
    {message_explanation}
    
    ---

    ### Befehle 🤖
    1. 🔎
    2. ⏩
    3. ❓
    4. 🧩
    5. 🖥️
    6. 🧮
    7. 🗣️
    8. 📈""",
    """## 📑 Dokument analysiert
    ### {Name des Dokuments} 📑:
    {Beschreibung des Dokuments}

    ---

    ### Befehle 🤖
    1. ✨
    2. 🔍
    3. 📑
    4. 💡
    5. ❓""",
    ]
    
    return examples[index]

def random_mnemonic():
    mnemonic_dictionary = {
        'Merksätze': "Mein Vater erklärt mir jeden Sonntag unsere neun Planeten.",
        'Akronyme': "KISS - Keep it simple and stupid",
        'Merkgeschichten': "Der König hat 12 Söhne. Der erste Sohn heißt 1, der zweite Sohn heißt 2, der dritte Sohn heißt 3, der vierte Sohn heißt 4, der fünfte Sohn heißt 5, der sechste Sohn heißt 6, der siebte Sohn heißt 7, der achte Sohn heißt 8, der neunte Sohn heißt 9, der zehnte Sohn heißt 10, der elfte Sohn heißt 11, der zwölfte Sohn heißt 12.",
        'Merkreime': "30 Tage hat September, April, Juni und November. Alle anderen haben 31, außer Februar, der hat 28.",
        'Merkregeln': "Die Summe der Innenwinkel eines Dreiecks beträgt 180°.",
        'Merkformeln': "a² + b² = c²",
        'Method of Loci': "Ich stelle mir vor, wie ich durch mein Haus laufe und an jedem Ort etwas abgefahrenes sehe, was ich mir merken kann.",
        }
    length = len(mnemonic_dictionary)
    random_number = randint(0, length - 1)
    key = list(mnemonic_dictionary.keys())[random_number]
    value = mnemonic_dictionary[key]
    
    return f'### {key} 🧠:\n>"_{value}_"'

roadmaps = {
"Datenbanken": """## 🗺️ Roadmap: Datenbanken
### Motivation 🥇
> Datenbanken sind das Rückgrat moderner Anwendungen und spielen eine entscheidende Rolle bei der Speicherung und Verwaltung von Daten. Mit fundierten Kenntnissen in Datenbanken können Sie leistungsstarke und effiziente Anwendungen entwickeln.

### Themen 📝

- Datenbankmanagementsysteme 💽: Software zur Verwaltung und Manipulation von Datenbanken.
    Datenbankmanagementsysteme sind die Grundlage für die effiziente Verwaltung von Datenbanken. Sie ermöglichen das Erstellen, Ändern und Löschen von Datenbanken sowie das Ausführen von Abfragen.
- Datenbankentwurf 📐: Prozess der Definition der Struktur und Organisation einer Datenbank.
    Der Datenbankentwurf umfasst die Festlegung der Tabellenstruktur, der Beziehungen zwischen den Tabellen und der Integritätsregeln.
- ER/EER-Modelle 🧩: Konzeptionelle und grafische Darstellung von Datenbankstrukturen.
    ER/EER-Modelle helfen bei der Visualisierung und Kommunikation der Datenbankstruktur. Sie verwenden Symbole und Notationen, um Entitäten, Attribute und Beziehungen darzustellen.
- Relationale Datenbanken 💾: Datenbanken, die auf dem relationalen Modell basieren, bei dem Daten in Tabellen organisiert sind.
    Relationale Datenbanken verwenden Tabellen, um Daten zu speichern und Beziehungen zwischen den Tabellen herzustellen. Sie bieten eine flexible und effiziente Möglichkeit, Daten zu organisieren und abzufragen.
- Relationales Datenmodell 📈: Datenmodell, das Daten in Tabellen organisiert, die aus Zeilen und Spalten bestehen.
    Das relationale Datenmodell definiert die Struktur und Beziehungen der Tabellen in einer relationalen Datenbank. Es ermöglicht die Speicherung und Abfrage von Daten auf eine konsistente und effiziente Weise.
- SQL 📜: Standardisierte Sprache zur Abfrage und Manipulation von Daten in relationalen Datenbanken.
    SQL (Structured Query Language) ist eine mächtige Sprache, die verwendet wird, um Daten aus relationalen Datenbanken abzufragen, einzufügen, zu aktualisieren und zu löschen. Sie ermöglicht komplexe Abfragen und Datenmanipulationen.
- No-SQL Datenbanken 📚: Nicht-relationale Datenbanken, die für große Datenmengen und Echtzeit-Anwendungen entwickelt wurden.
    No-SQL-Datenbanken bieten eine alternative Möglichkeit, Daten zu speichern und abzufragen. Sie sind flexibel, skalierbar und eignen sich gut für Big-Data-Anwendungen und Echtzeit-Anwendungen.
- XML 📦: Markup-Sprache zur Darstellung hierarchisch strukturierter Daten in Textform.
    XML (Extensible Markup Language) wird verwendet, um strukturierte Daten in einer les- und bearbeitbaren Textform zu speichern. Es ist weit verbreitet in der Webentwicklung und im Austausch von Daten zwischen verschiedenen Systemen.

### Lernziele 🎯

- Verstehen der Grundlagen von Datenbanken und ihrer Bedeutung in der Softwareentwicklung.
- Beherrschen der Konzepte des Datenbankentwurfs und der Modellierung.
- Kenntnisse in der Verwendung von SQL zur Abfrage und Manipulation von Daten.
- Vertrautheit mit verschiedenen Arten von Datenbanken, einschließlich relationaler und No-SQL-Datenbanken.
- Fähigkeit, XML-Daten zu lesen und zu schreiben.

---

### Befehle 🤖

1. 🚀
2. 📜""",
"Webtechnologien": """## 🗺️ Roadmap: Webtechnologien
### Motivation 🥇
> Webtechnologien sind das Herzstück des modernen Internets. Sie ermöglichen es uns, Informationen zu teilen, miteinander zu kommunizieren und komplexe Anwendungen zu erstellen, die auf jedem Gerät laufen. Durch das Erlernen von Webtechnologien eröffnen Sie sich eine Welt voller Möglichkeiten, von der Erstellung Ihrer eigenen Website bis hin zur Entwicklung von High-End-Webanwendungen.

### Themen 📝

1. Einführung 🎓
    - Einführung ins Web 🌐: Grundlagen des World Wide Web und wie es funktioniert.
    - HTML 📝: Die Sprache, mit der Webseiten strukturiert werden.
    - Bilder und Tabellen 🖼️📊: Wie man Bilder und Tabellen in Webseiten einbindet.
    - Semantische Strukturierung 🧠: Wichtig für die Zugänglichkeit und SEO.
    - Formulare 📋: Interaktion mit Benutzern ermöglichen.
    - CSS 🎨: Gestaltung und Styling von Webseiten.
    - Grundlagen des Webdesigns 🎨: Ästhetik und Benutzerfreundlichkeit.
    - Responsive Design 📱: Webseiten für verschiedene Geräte optimieren.
    - Flexbox 📦 und Media Queries 📲: Moderne Layout-Techniken.
    - Bildoptimierung 🖼️: Wichtig für Performance und Ladezeiten.
2. JavaScript 🖱️
    - JavaScript 🖱️: Die Programmiersprache des Webs.
    - Asynchrone Kommunikation 🔄: AJAX und moderne Web-Apps.
    - Bibliotheken und Frameworks 📚: Tools zur Vereinfachung der Entwicklung.
    - Performance von Webapplikationen ⚡: Schnelle Ladezeiten und Effizienz.
3. Backend ⚙️
    - DNS und Protokolle 📚: Grundlagen der Internet-Kommunikation.
    - PHP 🐘: Eine weit verbreitete Serverseitige Sprache.
    - Datenbankzugriff 🗃️: Wie Webseiten mit Datenbanken interagieren.
    - Security 🔒: Sicherheitsaspekte von Webanwendungen.
    - Performance ⚡ und Skalierung 📈: Optimierung für hohe Nutzerzahlen.
    - Sicherheit von Webapplikationen 🔒: Schutz vor Angriffen.
    - Suchmaschinenoptimierung 🔍: Besser gefunden werden im Web.

### Lernziele 🎯

- Verstehen, wie das Web funktioniert und wie Webseiten erstellt werden.
- Erlernen der Grundlagen von HTML, CSS und JavaScript.
- Verstehen, wie man Webseiten für verschiedene Geräte optimiert.
- Erlernen der Grundlagen der Backend-Entwicklung, einschließlich PHP und Datenbankzugriff.
- Verstehen der Sicherheits- und Performance-Aspekte von Webanwendungen.

---

### Befehle 🤖

1. 🚀
2. 📜"""
}

class Doc:
    def __init__(self, filenameWithExtension, example):
        self.current_page_number = 0

        self.example = example
        
        (self.pdf, self.page_count) = self.init_doc(filenameWithExtension)

    def init_doc(self, filenameWithExtension):
        doc = fitz.open('/mnt/data/' + filenameWithExtension)
        page_count = doc.pageCount

        full_pdf = [page.get_text() for i, page in enumerate(doc)]
        doc.close()

        return (full_pdf, page_count)

    def get_summary(self):
        preview = list(set([page[:page.find('\n')] for page in self.pdf]))
        
        return preview

    def get_pdf(self):
        return self.pdf
    
    def get_current_page_number(self):
        return self.current_page_number

    def get_page(self, page_number):
        if page_number < 0:
            page_number = 0
        elif page_number >= len(self.pdf):
            page_number = len(self.pdf) - 1
        self.current_page_number = page_number
        return (self.pdf[page_number], self.example.replace("### Mnemonic 🧠:", random_mnemonic()))

    def get_pages(self, page_number_start, page_number_end):
        if page_number_start < 0:
            page_number_start = 0
        if page_number_end >= len(self.pdf):
            page_number_end = len(self.pdf) - 1
        
        self.current_page_number = page_number_end
        return ("\n".join(self.pdf[page_number_start:page_number_end + 1]), self.example.replace("### Mnemonic 🧠:", random_mnemonic()))

    def get_next_page(self):
        self.current_page_number += 1
        return (self.get_page(self.current_page_number), self.example.replace("### Mnemonic 🧠:", random_mnemonic()))

    def search_section(self, section_name):
        pdf_sections = [page for page in self.pdf if section_name in page]
        return (pdf_sections, self.example.replace("### Mnemonic 🧠:", random_mnemonic()))

def start_chat(choice, additional_info):
  design = ""
  content = ""
  start = """# Hallo 😊 Ich bin TutorGPT 🎓
    #### Der persönliche Nachhilfelehrer für deine Semesterprüfung. 📝
    Gemeinsam werden wir die Prüfung bestehen. 🤝

    ## Module 📚

    ### Datenbanken 🗄️

    ### Webtechnologien 🌍

    ### Mathematik 🧮

    ---

    ### Befehle 🤖
    1. ⭐
    2. 📜
    3. 📑
    4. 📝"""
    
  if choice == '📑 DOC':
    global doc, get_example
    doc = Doc(additional_info, get_example(1))
    content = doc.get_summary()
    design = get_example(2)
  elif choice == '🗺️ ROADMAP':
    content = roadmaps[additional_info]
    design = get_example(0).replace("### Mnemonic 🧠:", random_mnemonic())
  elif choice == '👋 START':
    content = start
    design = get_example(0).replace("### Mnemonic 🧠:", random_mnemonic())
  else:
    design = get_example(0).replace("### Mnemonic 🧠:", random_mnemonic())
    content = f"TutorGPT, bitte erkläre das Thema {additional_info}. Benutze dazu erst die Websuche, um dich auf den neusten Stand zu bringen. Danach erkläre es mir so, als wäre ich ein 5-jähriges Kind und formuliere es wie in {design} beschrieben."
    
  return {"design_template": design, "content": content}
