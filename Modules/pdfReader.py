# importing required modules
from tkinter.filedialog import askdirectory
from pdfquery import PDFQuery


def readPdf(path):
    pdf = PDFQuery(path)
    pdf.load()

    # Use CSS-like selectors to locate the elements
    text_elements = pdf.pq("LTTextLineHorizontal")

    # Extract the text from the elements
    text = [t.text for t in text_elements]
    textOut=[]
    for ele in text:
        #temp = re.findall(r'\b(?:[A-Za-z]+|[A-Za-z]\+[A-Za-z]+|\w+\.\w+|\w+\.\w+\.?\w*)\b', ele)
        temp = ele.split()
        
        for word in temp:     
            textOut.append(word.lower().rstrip('.,;'))
            
    return textOut


def choosePdf():
    path = askdirectory(title="Select PDF")  # shows dialog box and return the path
    return path
