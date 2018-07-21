from PIL import Image

img = Image.open("dukelogo.png")
pixels = [(int(r * .75), int(g * .75), int(b * .75)) for (r,g,b) in img.getdata()]
img.putdata(pixels)
img.show()
