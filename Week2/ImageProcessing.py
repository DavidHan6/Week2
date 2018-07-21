from PIL import Image
from PIL import ImageFilter

print("       What is your request?      ")
print("           a is invert")
print("           b is darken")
print("           c is brigten")
print("          d is greyscale")
print("          e is posterize")
print("          f is solarize")
print("          g is denoise1")
print("          h is denoise2")
print("          i is denoise3")
print("            j is blur")
print("          k is sharpen")
print("            l is crop")
mudder = input("                ")

def apply_filter(image, filter):
    pixels = [ filter(p) for p in image.getdata() ]
    nim = Image.new("RGB",image.size)
    nim.putdata(pixels)
    return nim

def open_image(filename):
    image = Image.open(filename)
    if image == None:
        print("Specified input file " + filename + " cannot be opened.")
        return Image.new("RGB", (400, 400))
    else:
        print(str(image.size) + " = " + str(len(image.getdata())) + " total pixels.")
        return image.convert("RGB")

def identity(pixel):
    r,g,b = pixel
    return (r,g,b)

def invert(pixel):
    r,g,b = pixel
    return (255-r, 255-g, 255-b)

def darken(pixel):

    r,g,b = pixel
    return (int((9/10) * r), int((9/10) * g), int((9/10)* b))

def brighten(pixel):
    r,g,b = pixel
    return (int((1000000/10) * r), int((1000000/10) * g), int((100000/10)* b))

def gray_scale(pixel):
    r,g,b = pixel
    gry = (r + g + b) / 3
    return (int(gry), int(gry), int(gry))

def posterize(pixel):
    r,g,b = pixel
    if r >= 0 and r <= 63:
        r = 50
    if r >= 64 and r <= 127:
        r = 100
    if r >= 128 and r <= 191:
        r = 150
    if r >= 192 and r <= 255:
        r = 200
    if g >= 0 and g <= 63:
        g = 50
    if g >= 64 and g <= 127:
        g = 100
    if g >= 128 and g <= 191:
        g = 150
    if g >= 192 and g <= 255:
        g = 200
    if b >= 0 and b <= 63:
        b = 50
    if b >= 64 and b <= 127:
        b = 100
    if b >= 128 and b <= 191:
        b = 150
    if b >= 192 and b <= 255:
        b = 200
    return (r,g,b)

def solarize(pixel):
    r,g,b = pixel
    if r < 128:
        r = 255 - r
    if g < 128:
        g = 255 - g
    if b < 128:
        b = 255 - b
    return (r,g,b)

def denoise(pixel):
    (r,g,b) = pixel
    return(r*10, g*0, b*0)

'''def denoise2(pixel):


def denoise3(pixel):'''


def blur(pixel):
    num = int(input("What is your blur power: "))
    original_image = Image.open(input_file)
    blurred_image = original_image.filter(ImageFilter.GaussianBlur(num))
    blurred_image.show()
    exit()

def sharpen(pixel):
    original_image = Image.open(input_file)
    sharpened_image = original_image.filter(ImageFilter.SHARPEN)
    sharpened_image.show()
    exit()

def crop(pixel):
    coord1 = input("what is your first x")
    coord2 = input("what is your first y")
    coord3 = input("what is your second x")
    coord4 = input("what is your second y")
    allcords = (coord1, coord2, coord3, coord4)
    original_image = Image.open(input_file)
    blurred_image = original_image.crop(allcords)
    blurred_image.show()
    exit()

def load_and_go(fname,filterfunc):
    print("Loading ...")
    image = open_image(fname)
    nimage = apply_filter(image,filterfunc)
    #image.show()
    #nimage.show()
    '''
    processedImage.jpg is the name of the file
    the image is saved in. The first time you do
    this you may have to refresh to see it.
    '''
    nimage.save("processedImage.jpg")

if __name__ == "__main__":
    ''' Change the name of the file and the function
        to apply to the file in the line below
    '''
    input_file = input("What file would you like?")
    if mudder == "a":
        mudder = invert
    if mudder == "b":
        mudder = darken
    if mudder == "c":
        mudder = brighten
    if mudder == "d":
        mudder = gray_scale
    if mudder == "e":
        mudder = posterize
    if mudder == "f":
        mudder == solarize
    if mudder == "g":
        mudder = denoise
    if mudder == "h":
        mudder = denoise2
    if mudder == "i":
        mudder == denoise3
    if mudder == "j":
        mudder = blur
    if mudder == "k":
        mudder = sharpen
    if mudder == "l":
        mudder = crop
    load_and_go(input_file, mudder)
