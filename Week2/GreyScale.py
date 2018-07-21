from PIL import Image

img = Image.open("dukelogo.png")
pixels = [(int(r), int(g), int(b)) for (r,g,b) in img.getdata()]
new_pixels = []
for (r, g, b) in pixels:
    grey = int((r+g+b)/3.0)
    new_pixel = (grey, grey, grey)
    new_pixels.append(new_pixel)
img.putdata(new_pixels)
img.show()
