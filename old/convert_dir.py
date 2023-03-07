from PIL import Image
import os

src_dir = "./puzzles_eps"
dst_dir = "./puzzles_png"
os.chdir(src_dir)
for filename in os.listdir():
    with Image.open(filename) as img:
        fig = img.convert("RGBA")
        converted = filename + ".png"
        fig.save(os.path.join(dst_dir, converted))
    #    converted_img = img.convert("P", palette=Image.ADAPTIVE, colors=8)
    #    converted_img.save(os.path.join(base_dir_dst, filename))