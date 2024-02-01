import fitz

def get_start():
    file_path = '/mnt/data/start.md'
    with open(file_path, 'r') as file:
        start_content = file.read()
    return start_content

def get_roadmap(section_name):
    file_path = '/mnt/data/roadmaps.md'
    with open(file_path, 'r') as file:
        roadmaps_content = file.read()
    roadmaps_content_split = roadmaps_content.split('## 🗺️ Roadmap: ')
    chosen_section = next((section for section in roadmaps_content_split if section_name in section), None)
    return chosen_section

class Doc:
    def __init__(self, filenameWithExtension):
        self.current_page_number = 0
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
        
        return self.pdf[page_number]

    def get_pages(self, page_number_start, page_number_end):
        if page_number_start < 0:
            page_number_start = 0
        if page_number_end >= len(self.pdf):
            page_number_end = len(self.pdf) - 1
        
        self.current_page_number = page_number_start
        
        return "\n".join(self.pdf[page_number_start:page_number_end])

    def get_next_page(self):
        self.current_page_number += 1
        return self.get_page(self.current_page_number)

    def search_section(self, section_name):
        pdf_sections = [page for page in self.pdf if section_name in page]
        return pdf_sections