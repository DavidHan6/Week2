from PIL import Image
from PIL import ImageFilter
original_image = "noise.png"
original_image = Image.open(original_image)
blurred_image = original_image.filter(ImageFilter.GaussianBlur(radius=5))
blurred_image.show()

blurImage('noise.png')
