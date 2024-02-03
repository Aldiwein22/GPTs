import fitz
import pandas as pd
from random import randint

COMMANDS = pd.read_csv('/mnt/data/commands.csv').set_index('Command')['Description'].to_dict()
NEXTMAP = pd.read_csv('/mnt/data/next_coms.csv').set_index('Command')['Next'].to_dict()
SEC = pd.read_csv('/mnt/data/sections.csv').set_index('Section')['Template'].to_dict()
MNEMONICS = pd.read_csv('/mnt/data/mnemonics.csv').set_index('Mnemonic')['Example'].to_dict()
RESPONSES = pd.read_csv('/mnt/data/responseMap.csv').set_index('Command')['Response'].to_dict()

doc = None

class Doc:
    def __init__(self, fName):
        global get_design
        self.fName = fName if '.' in fName else fName + '.pdf'
        self.current = 0
        self.pdf, self.page_count = self.init_doc(self.fName)

    def init_doc(self, fName):
        with fitz.open('/mnt/data/' + fName) as doc:
            full_pdf = [page.get_text() for page in doc]
            page_count = doc.page_count
        return full_pdf, page_count

    def get_summary(self):
        return list(set(page.split('\n', 1)[0] for page in self.pdf))

    def get_page(self, page_number):
        self.current = max(0, min(page_number, len(self.pdf) - 1))
        return self.pdf[self.current], get_design("⏭️")

    def get_pages(self, start, end):
        self.current = min(end, len(self.pdf) - 1)
        return "\n".join(self.pdf[start:self.current + 1]), get_design("⏭️")

    def get_next_page(self):
        self.current += 1
        return self.get_page(self.current)

    def search_section(self, section_name):
        return [page for page in self.pdf if section_name in page], get_design("⏭️")

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
    response = RESPONSES.get(input[0], f"Entschuldigung, ich habe das nicht verstanden.\n\nBitte wähle eine der folgenden Optionen: 📑, 📒, 🧠, 👋")
    content = response.replace("__addInfo__", addInfo)
    
    if '📑' in input:
        global doc
        doc = Doc(addInfo)
        content = content.replace("__summary__", doc.get_summary())
    
    return {"design_template": template, "content": content}
