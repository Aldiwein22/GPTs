import pandas as pd
from random import randint
import fitz

doc = None

COMMANDS = pd.read_csv('/mnt/data/commands.csv').set_index('Command')['Description'].to_dict()
NEXTMAP = pd.read_csv('/mnt/data/next_coms.csv').set_index('Command')['Next'].to_dict()
SEC = pd.read_csv('/mnt/data/sections.csv').set_index('Section')['Template'].to_dict()
MNEMONICS = pd.read_csv('/mnt/data/mnemonics.csv').set_index('Mnemonic')['Example'].to_dict()
RESPONSES = pd.read_csv('/mnt/data/responseMap.csv').set_index('Command')['Response'].to_dict()

def get_design(input):
    template = SEC["title"]
    
    if "📑" in input:
        template += SEC["document"]
    if any(x in input for x in ["📝", "📜", "🧠", "🔍", "⏩", "⏭️"]):
        template += SEC["definition"]
        template += SEC["explanation"]
        template += SEC["simple_explanation"]
        template += SEC["example"]
        template += SEC["mnemonic"]
    if "🔍" in input:
        template += SEC["explanation"]
        
    template += "\n---\n\n"
    template += "### Befehle 🤖:\n"
    template += get_next_coms(input)
    template = template.replace("### Mnemonic 🧠:", get_mnemonic())
    
    return template

class Doc:
    def __init__(self, addInfo):
        self.pdf = fitz.open('/mnt/data/' + addInfo)
        self.current = 0
        self.summary = self.get_summary()
        self.design = get_design("⏭️")

    def get_summary(self):
        s = ""
        for i, page in enumerate(self.pdf):
            s += "Page " + str(i+1) + ": " + page.get_text()[:10]
        return s

    def get_page(self, page_number):
        self.current = max(0, min(page_number, self.pdf.page_count - 1))
        return (self.pdf[self.current].get_text(), self.design)

    def get_pages(self, start, end):
        self.current = min(end, self.pdf.page_count - 1)
        ps = self.pdf[start:self.current + 1]
        return ("\n".join([page.get_text() for page in ps]), self.design)

    def get_next_page(self):
        self.current += 1
        return self.get_page(self.current)

    def search_section(self, section_name):
        pages = []
        for page in self.pdf:
            if section_name in page.get_text():
                pages.append(page.get_text())
        return (pages, self.design)

def get_next_coms(last_command):
    returnList = []
    next = NEXTMAP.get(last_command, "📑,📒,🧠,👋")
    next = next.split(',')
    
    for command in next:
        returnList.append(format_command(command))
    
    for i in range(len(returnList)):
        returnList[i] = f"{i + 1}. {returnList[i]}"
    
    return "\n".join(returnList)

def format_command(command):
    return f"{command} -> {COMMANDS.get(command)}"

def get_mnemonic():
    ranInt = randint(0, len(MNEMONICS) - 1)
    key = list(MNEMONICS.keys())[ranInt]
    return f'### {key} 🧠:\n>"_{MNEMONICS[key]}_"'

def start_chat(input, addInfo):
    template = get_design(input)
    response = RESPONSES.get(input[0], f"Optionen: 📑, 📒, 🧠, 👋")
    content = response.replace("__addInfo__", addInfo)
    
    if '📑' in input:
        global doc
        doc = Doc(addInfo)
        content = content.replace("__SUMMARY__", doc.summary)
    
    return {"design_template": template, "content": content}