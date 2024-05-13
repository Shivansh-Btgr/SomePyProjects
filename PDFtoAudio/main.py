import pyttsx3
import PyPDF2

path = input("Enter path to the PDF : ")
pdf_file = open(path, 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)
engine = pyttsx3.init()

for page_num in range(pdf_reader.numPages):
    page = pdf_reader.getPage(page_num)
    text = page.extract_text()
    engine.say(text)
    engine.runAndWait()

pdf_file.close()