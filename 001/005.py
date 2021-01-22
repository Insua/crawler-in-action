import tesserocr
from PIL import Image

image = Image.open('001/image.png')
print(tesserocr.image_to_text(image))

print(tesserocr.file_to_text('001/image.png'))
