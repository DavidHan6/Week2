from PIL import Image

img = Image.open("dukelogo.png")
pixels = [(int(r), int(g), int(b)) for (r,g,b) in img.getdata()]
new_pixel = []
for (r,g,b) in pixels:
    if r < 128:
        r = 255 - r
    if g < 128:
        g = 255 - g
    if b < 128:
        b = 255 - b
    new_pixels = (r, g, b)
    new_pixel.append(new_pixels)
img.putdata(new_pixel)
img.show()
