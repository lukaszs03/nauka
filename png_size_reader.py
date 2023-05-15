from PIL import Image

img = Image.open("Python.png")
print(img.format, img.size, img.mode)

img.show()