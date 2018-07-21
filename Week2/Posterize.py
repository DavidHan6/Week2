from PIL import Image

img = Image.open("vases.png")

pixels = [(int(r), int(g), int(b), int(a)) for (r,g,b,a) in img.getdata()]
new_pixels = []
for (r,g,b,a) in pixels:
    if r >= 0 and r <= 63:
        great = 50
    elif r >= 64 and r <= 127:
        great = 100
    elif r >= 128 and r <= 191:
        great = 150
    elif r >= 192 and r <= 255:
        great = 200

    if g >= 0 and g <= 63:
        brown = 50
    elif g >= 64 and g <= 127:
        brown = 100
    elif g >= 128 and g <= 191:
        brown = 150
    elif g >= 192 and g <= 255:
        brown = 200

    if b >= 0 and b <= 63:
        shit = 50
    elif b >= 64 and b <= 127:
        shit = 100
    elif b >= 128 and b <= 191:
        shit = 150
    elif b >= 192 and b <= 255:
        shit = 200
    new_pixel = (great, brown, shit)
    new_pixels.append(new_pixel)
img.putdata(new_pixels)
img.show()
