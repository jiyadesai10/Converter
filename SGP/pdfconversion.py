from PyPDF2 import PdfFileReader
file = open("test.pdf", 'rb')
reader=PdfFileReader(file)
num_pages = reader.numPages
for p in range (num_pages):
    page = reader.getPage(p)
    text = page.extractText()
    print(text)
    from googletrans import Translator
    translator = Translator()
    translate_text = translator.translate(text, dest='hi')