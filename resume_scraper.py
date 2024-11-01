import pdfquery

if __name__ == '__main__':
    print("Resume Scraper for PDFs\n--------")
    pdf_name = "RobertGodlewskiCodingResume202401.pdf"
    pdf = pdfquery.PDFQuery(pdf_name)
    pdf.load()
    # pdf.tree.write('resume.xml', pretty_print=True)
    data_elements = pdf.pq('LTTextLineHorizontal')
    raw_data = [i.text for i in data_elements]
    print(raw_data)
