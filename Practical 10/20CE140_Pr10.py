# 20CE140 - Dhwani Suthar
# Generate PDF file of your 3rd Semester Mark-sheet

from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size = 10)
f = open("marksheet.txt","r")

for i in f:
    pdf.cell(200,10,txt=i,ln=1)

pdf.output("mark-sheet.pdf")

