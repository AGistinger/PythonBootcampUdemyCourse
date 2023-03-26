# Working with Images in Python
from PIL import Image

mac = Image.open("example.jpg")
print(type(mac))

print(mac.size)  # Width and height
print(mac.format_description)

# Cropping an Image
# mac.crop((0, 0, 100, 100))
halfway = int(1993 / 2)
x = halfway - 200
w = halfway + 200
y = 800
h = 1257

computer = mac.crop((x, y, w, h))

pencils = Image.open("pencils.jpg")
print(pencils.size)

x = 0
y = 0
w = int(1950 / 3)
h = int(1300 / 10)

pencils.crop((x, y, w, h))

# Copying and Pasting Images
mac.paste(im=computer, box=(0, 0))

# Resize an image
mac.resize((3000, 500))

# Rotate images
mac.rotate(90)

# Color Transparency
# RGBA - Red, Green, Blue, Alpha (0 - 255)
red = Image.open("red_color.jpg")
blue = Image.open("blue_color.png")
blue.putalpha(128)
red.putalpha(128)
blue.paste(im=red, box=(0, 0), mask=red)  # Put red image on blue
blue.convert('RGB').save("purple.png")

# Reveal Secret Message
words = Image.open("word_matrix.png")
mask = Image.open("mask.png")
mask = mask.resize((1015, 559))
mask.putalpha(150)
words.paste(mask, (0, 0), mask)
words.save("message.png")
