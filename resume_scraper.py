import json
import numpy
import pdfquery

if __name__ == '__main__':
    print("Resume Scraper for PDFs\n--------")
    pdf_name = "RobertGodlewskiCodingResume202401.pdf"
    pdf = pdfquery.PDFQuery(pdf_name)
    pdf.load()
    # pdf.tree.write('resume.xml', pretty_print=True) # Only need this to help figure out what to do to build out json file
    # Gathering all text information
    text_elements = pdf.pq('LTTextLineHorizontal')
    # Gathering all hyperlinks
    # link_elements = pdf.pq('Annot')
    raw_data = numpy.array([i.text for i in text_elements])
    # print(raw_data)
    # print(raw_data.shape)
    # print(raw_data.dtype)
    data = {}
    # Going through the header of the resume
    full_name_arr = raw_data[0].split(" ")
    # print(full_name_arr)
    data["first_name"] = full_name_arr[0]
    data["last_name"] = full_name_arr[1]
    data["titles"] = raw_data[1].split("/ ")
    contacts = raw_data[2].split(" | ")
    print(contacts) # Need to do something here with this
    # ....add in more stuff to go through.....
    print(f'--------\nCreating a json file off of: {data}')
    with open(f'{data["first_name"]}{data["last_name"]}Resume.json', 'w') as f: json.dump(data, f, indent=4)
