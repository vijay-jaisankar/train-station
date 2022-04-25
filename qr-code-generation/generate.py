import pyqrcode
import png
from pyqrcode import QRCode


"""
@Class: To generate QR Codes
"""
class QRCode:
    
    def __init__(self, encode_string, scale):
        self._encode_string = encode_string
        self._scale = scale
        self._obj = pyqrcode.create(self._encode_string)

    def generate_svg(self, output_filename):
        self._obj.svg(
            output_filename,
            scale = self._scale
        )    
    
    def generate_png(self, output_filename):
        self._obj.png(
            output_filename,
            scale = self._scale
        )


if __name__ == "__main__":
    qr = QRCode("https://www.youtube.com/watch?v=dQw4w9WgXcQ", 6)
    output_file = "rickroll.png"
    qr.generate_png(output_filename=output_file)
