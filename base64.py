import base64

with open("logo.png", "rb") as image_file:
  base64 =  encoded_string = base64.b64encode(image_file.read())
print(base64)

# b'iVBORw0KGgoAAAANS.....'

'''
#Tem programa que so aceita nesse formato de baixo
with open("rone.png", "rb") as img_file:
    b64_string = base64.b64encode(img_file.read())
print(b64_string.decode('utf-8'))
'''

# iVBORw0KGgoAAAA


