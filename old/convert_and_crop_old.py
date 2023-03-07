from PIL import Image
import os
import time


START_TIME = time.time()

src_dir = "puzzles_eps"
dst_dir = "../puzzles_png"
os.chdir(src_dir)
for filename in os.listdir():
    with Image.open(filename) as img:
        fig = img.convert("RGBA")

    # Crop to the puzzle

    # Size of the image in pixels (size of original image)
    # (This is not mandatory)
    width, height = fig.size
    
    # Setting the points for cropped image
    left = 13
    top = height / 50
    right = 515
    bottom = 3 * height / 3.15
    
    # Cropped image of above dimension
    # (It will not change original image)
    img = fig.crop((left, top, right, bottom))
    
    converted = filename + ".png"
    img.save(os.path.join(dst_dir, converted))

# For debugging to make sure it didn't take too long to run
print("--- %s seconds ---" % (time.time() - START_TIME))