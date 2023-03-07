from PIL import Image

# Convert from eps to png
puzzle_eps = "solution.eps"
im = Image.open(puzzle_eps)

fig = im.convert("RGBA")

# Crop to the puzzle

# Size of the image in pixels (size of original image)
# (This is not mandatory)
width, height = im.size
 
# Setting the points for cropped image
left = 45
top = height / 100
right = 527
bottom = 3 * height / 3.1
 
# Cropped image of above dimension
# (It will not change original image)
im1 = im.crop((left, top, right, bottom))
 
# Save the image to png file
im1.save("solution.png")