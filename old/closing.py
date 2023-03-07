from fpdf import FPDF
from fpdf.enums import XPos, YPos

pdf = FPDF("P", "mm", [152.4,228.6])


# Add a page
pdf.add_page()
pdf.set_font("helvetica", "B", 20)
pdf.cell(125, 50, difficulty, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
pdf.set_font("helvetica", "I", 10)
pdf.multi_cell(0, 10, "", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
pdf.multi_cell(0, 10, "", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
pdf.ln()