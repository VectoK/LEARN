import docx

doc = docx.Document()

doc.add_paragraph("TEST PARAGRAPH")

doc.save("TEST.DOCX")
