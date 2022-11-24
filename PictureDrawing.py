#pip install pywhatkit - install pywhatkit first

from PIL import Image
Image.open("hakan.png")


import pywhatkit
pywhatkit.image_to_ascii_art('hakan.png', 'MyArt')
read_file = open("Myart.txt","r")
print(read_file.read())
