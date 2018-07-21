from PIL import Image

img = Image.open("noise.png")
pixels = [(int(r), int(g), int(b), int(a)) for (r,g,b,a) in img.getdata()]
new_pixels = []
for (r,g,b,a) in pixels:
    return(r*10, g*0, b*0)
    new_pixel = (r, g, b, a)
    new_pixels.append(new_pixel)
img.putdata(new_pixel)
img.show()
