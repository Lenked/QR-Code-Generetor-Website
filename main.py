import pyqrcode
import png
from pyqrcode import QRCode

s = input("Enter the link of the website :")

url = pyqrcode.create(s)

url.svg("myqr.svg", scale = 0)

url.png('myqr.png', scale= 6)