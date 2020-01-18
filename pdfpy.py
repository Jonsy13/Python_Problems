import PyPDF2


with open('./11.2 dummy.pdf.pdf','rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    #getPage() return the object pointing to the page
    # print(reader.getPage(1))
    
    #rotate() rotates the page
    page = reader.getPage(0)
    page.rotateClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('tilt.pdf','wb') as new_file:
        writer.write(new_file)
        