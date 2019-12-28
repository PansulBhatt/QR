from pyzbar.pyzbar import decode
from PIL import Image

print(decode(Image.open('images/code.png'))[0].data)