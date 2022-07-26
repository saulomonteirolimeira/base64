import base64

with open("logo.png", "rb") as image_file:
  base64 =  encoded_string = base64.b64encode(image_file.read())
print(base64)

# b'iVBORw0KGgoAAAANS.....'
