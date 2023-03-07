from PIL import Image
import os
from multiprocessing import Pool
import shutil
import time

START_TIME = time.time()

src_dir = "puzzles_eps"
dst_dir = "puzzles_png"

count = 0
for x in os.listdir(src_dir):
    if os.path.isfile(os.path.join(src_dir, x)):
        count += 1

puzz_files = [f"puzzles_eps/puzzle{n}.eps" for n in range(int(count/2))]
solu_files = [f"puzzles_eps/solution{n}.eps" for n in range(int(count/2))]
#print(puzz_files)
#print(solu_files)

def process_img(filename):
    with Image.open(filename) as img:
        fig = img.convert("RGBA")

    # Size of the image in pixels (size of original image)
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
    img.save(converted)
    shutil.move(converted, dst_dir)

with Pool() as pool:
    pool.map(process_img, puzz_files)
    pool.map(process_img, solu_files)
    
    pool.close()
    pool.join()



# For debugging to make sure it didn't take too long to run
print("--- %s seconds ---" % (time.time() - START_TIME))