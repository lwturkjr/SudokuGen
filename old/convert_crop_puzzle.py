from PIL import Image

# Convert from eps to png
puzzle_eps = "puzzle0.eps"
im = Image.open(puzzle_eps)

fig = im.convert("RGBA")

# Crop to the puzzle

# Size of the image in pixels (size of original image)
# (This is not mandatory)
width, height = im.size
 
# Setting the points for cropped image
left = 13
top = height / 50
right = 515
bottom = 3 * height / 3.15
 
# Cropped image of above dimension
# (It will not change original image)
im1 = im.crop((left, top, right, bottom))
 
# Save the image to png file
im1.save("puzzle0.png")