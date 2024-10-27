import PyPDF2

def read_pdf(PyPDF2.pdf):
    with open(pdf_file_path, 'rb') as file:

        pdf_reader = PyPDF2.PdfFileReader(file)
        
        num_pages = pdf_reader.numPages
        print("Total number of pages:", num_pages)
        
        for page_num in range(num_pages):

            page = pdf_reader.getPage(page_num)
            
            page_text = page.extractText()
            
            print("Page", page_num + 1, "content:")
            print(page_text)
            print("=" * 50) 

pdf_file_path = "path_to_your_pdf_file.pdf"

read_pdf(PyPDF2.pdf)
