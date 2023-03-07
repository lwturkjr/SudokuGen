from fpdf import FPDF
from fpdf.enums import XPos, YPos
import fnmatch
import os
import time


START_TIME = time.time()

src_dir = "puzzles_png"
os.chdir(src_dir)

difficulty = input("Puzzle Difficulty: ")
checks = input("How many checks: ")

def puzzles_pdf():
    pdf = FPDF("P", "mm", [152.4,228.6])

    # Add a page
    pdf.add_page()
    pdf.set_font("helvetica", "B", 20)
    pdf.cell(125, 50, difficulty, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
    pdf.set_font("helvetica", "I", 10)
    pdf.multi_cell(0, 10, "I generated these puzzles with a python script. The difficulty is increased \n by increasing the number of times, it checks if it can remove a number \n and there still being only one unique solution to the puzzle. \n These "+difficulty+" puzzles have "+checks+" checks.", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
    pdf.multi_cell(0, 10, "I intend on making improvements to the python script I use for future releases.", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
    pdf.ln()

    puzz_list = []
    for filename in os.listdir():
        if fnmatch.fnmatch(filename, "puzz*.png"):
            puzz_list.append(filename)
            puzz_list.sort()

    for x in puzz_list:
        pdf.image(x, x = 35, w = pdf.w / 1.75, h = pdf.h / 2.35)
    
    pdf.output("../output/"+difficulty+"_puzz_pdf.pdf")

def solutions_pdf():
    pdf = FPDF("P", "mm", [152.4,228.6])

    # Add a page
    pdf.add_page()
    pdf.set_font("helvetica", "B", 20)
    pdf.cell(125, 50, "Solutions "+difficulty, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
    pdf.set_font("helvetica", "I", 10)
    pdf.cell(125, 100, "Soltutions appear in the order of puzzles", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
    pdf.ln()

    sol_list = []
    for filename in os.listdir():
        if fnmatch.fnmatch(filename, "sol*.png"):
            sol_list.append(filename)
            sol_list.sort()

    for x in sol_list:
        pdf.image(x, x = 35, w = pdf.w / 1.75, h = pdf.h / 2.35)
    
    pdf.output("../output/"+difficulty+"_sol_pdf.pdf")

puzzles_pdf()
solutions_pdf()

# For debugging to make sure it didn't take too long to run
print("--- %s seconds ---" % (time.time() - START_TIME))