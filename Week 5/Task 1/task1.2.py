import PyPDF2

pdfFile = open('task1.2.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFile)

page = pdfReader.getPage(0)

txtFile =  open('task1.2.txt', 'a')
txtFile.write(page.extractText())
txtFile.close()

pdfFile.close()