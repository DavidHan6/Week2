from PIL import Image

img = Image.open("noise.png")
pixels = [(int(r), int(g), int(b), int(a)) for (r,g,b,a) in img.getdata()]
new_pixels = []
def denoise():
    pass
    new_pixel = (r, g, b, a)
    new_pixels.append(new_pixel)
img.putdata(new_pixel)
img.show()
