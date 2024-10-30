from PyPDF2 import PdfReader # type: ignore

if __name__ == '__main__':
    print("Resume Scraper for PDFs\n--------")
    reader = PdfReader("RobertGodlewskiCodingResume202401.pdf")
    page = reader.pages[0]
    print(page.extract_text())
