from PIL import Image

img = Image.open("dukelogo.png")
pixels = [(int(r * 1.25), int(g * 1.25), int(b * 1.25)) for (r,g,b) in img.getdata()]
img.putdata(pixels)
img.show()
