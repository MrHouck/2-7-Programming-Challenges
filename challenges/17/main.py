from PIL import Image 
import numpy as np


grayscale = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "


image = Image.open("peppers.png")


# Convert the image to grayscale

image = image.convert("L")

# Now we resize to 100x100 so that it doesn't take up a lot of space


image = image.resize((100,100))
W, H = image.size[0], image.size[1]

pixels = image.getdata()
new_pix = []
for pixel in pixels:
    idx = (pixel / 255) * 70
    idx = int(np.floor(idx))
    new_pix.append(grayscale[idx])

new_pix = ''.join(new_pix)
ascii_image = ''
for i in range(0, len(new_pix), W):
    ascii_image += new_pix[i:i + W] + "\n"


with open("ascii_image.txt", "w") as f:
    f.write(ascii_image)