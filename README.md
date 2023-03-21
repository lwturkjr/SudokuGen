# SudokuGen
A series of scripts to generate Sudoku Puzzles and a PDF containing all the generated puzzles

So the puzzle_gen.py generates .eps files, which are then converted to png files and cropped with convert_and_crop.py finally, 
the create_pdf.py generates a PDF file with all of the puzzles, two per page and soultions in the "back" of the book.

The outputted files can then be uploaded with a cover to KDP or some other self publishing place.

I never got around to making a script to generate the cover.

I also wanted to make the script use multiprocessing for faster generation, I wasn't able to fully figure that out.
