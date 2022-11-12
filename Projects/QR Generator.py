import pyqrcode
import png
from PIL import Image

link = input("enter anything to generate QR:")
qr_code = pyqrcode.create(link)
qr_code.png("QRCode.png", scale=5)
Image.open("QRCode.png")
