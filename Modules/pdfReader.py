# importing required modules
from tkinter.filedialog import askdirectory
from pdfquery import PDFQuery
  
def readPdf(path) :
    pdf = PDFQuery(path)
    pdf.load()

    # Use CSS-like selectors to locate the elements
    text_elements = pdf.pq('LTTextLineHorizontal')

    # Extract the text from the elements
    text = [t.text for t in text_elements]
    return text
    
def choosePdf():
    path = askdirectory(title="Select PDF")  # shows dialog box and return the path
    return path
