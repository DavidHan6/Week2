from PIL import Image

img = Image.open("dukelogo.png")
pixels = [(int(255 - r), int(255 - g), int(255 - b)) for (r,g,b) in img.getdata()]
img.putdata(pixels)
img.show()
