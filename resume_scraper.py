import json
import numpy
import pdfquery

# Grabs the information needed
class ResumeParse:
    def __init__(self) -> None:
        self.data = {}
        self.iterator = 0
        self.is_parsing = True

    def parse(self, pdf_name: str) -> None:
        print(f'--------\nLoading {pdf_name}.....\n---------')
        pdf = pdfquery.PDFQuery(pdf_name)
        pdf.load()
        # pdf.tree.write('resume.xml', pretty_print=True) # Only need this to help figure out what to do to build out json file
        # Gathering all text information
        text_elements = pdf.pq('LTTextLineHorizontal')
        # Gathering all hyperlinks - need to narrow this down because we are getting a big an HTML tag block here instead of just a url
        # link_elements = pdf.pq('Annot')
        # print(f'--------\nNeeded Links: {link_elements}\n---------')
        raw_data = numpy.array([i.text for i in text_elements])
        # raw_data = numpy.array([i.text for i in text_elements], [i.url for i in link_elements])
        # print(raw_data)
        # print(raw_data.shape)
        # print(raw_data.dtype)
        self._get_header(raw_data)
        while self.is_parsing:
            # edit this to loop through all needed information
            self.is_parsing = False
        print(f'--------\nFinished parsing data to get: {self.data}')

    def export(self) -> None:
        print(f'--------\nCreating a json file off of: {self.data}')
        with open(f'{self.data["first_name"]}{self.data["last_name"]}Resume.json', 'w') as f: 
            json.dump(self.data, f, indent=4)

    def _get_header(self, raw_data: list) -> None:
        # self.iterator = 0
        full_name_arr = raw_data[self.iterator].split(" ")
        self.data["first_name"] = full_name_arr[0]
        self.data["last_name"] = full_name_arr[1]
        self.iterator += 1
        self.data["titles"] = raw_data[self.iterator].split("/ ")
        self.iterator += 1
        contacts = raw_data[self.iterator].split(" | ")
        self.data["phone_number"] = contacts[0]
        location_raw = contacts[1].split(", ")
        self.data["location"] = {
            "city_area": location_raw[0], 
            "state_code": location_raw[1]
        }
        self.data["email"] = contacts[2]
        # Need to add in the links here

    def _BLOB(self) -> None: 
        # Add in different parsers for each needed thing in here....
        pass


if __name__ == '__main__':
    print("Resume Scraper for PDFs\n--------")
    # Need to fix this to ask for the name of the pdf file instead of this
    pdf_name = "RobertGodlewskiCodingResume202401.pdf"
    resume = ResumeParse()
    resume.parse(pdf_name)
    # resume.export()
