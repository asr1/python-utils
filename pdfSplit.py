from PyPDF2 import PdfFileWriter, PdfFileReader

inputpdf = PdfFileReader(open("One Bloodless Town.pdf", "rb"))

output = PdfFileWriter()
for i in range(0,1): # Add one to the second number.
    output.addPage(inputpdf.getPage(i))
with open("output.pdf", "wb") as outputStream:
    output.write(outputStream)