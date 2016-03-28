from PIL import Image 
import sys, os, platform

BLOCK = '\xA1\xF6' if platform.system() == 'Windows' else 'MM'

class QRCode():
    def __init__(self, fileName, size, padding = 0, background = 'BLACK'):
        self.size = size
        self.padding = padding
        self.img = Image.open(fileName)
        self.times = self.img.size[0]/(size + padding * 2)
        self.rgb = self.img.convert('RGB')
        self.white = BLOCK if background == 'BLACK' else '  '
        self.black = '  ' if background == 'BLACK' else BLOCK 
    def print_qr(self):
        sys.stdout.write(' '*50 + '\r')
        sys.stdout.flush()
        print self.white * (self.size + 2)
        startPoint = self.padding + 0.5
        for y in range(self.size):
            sys.stdout.write(self.white)
            for x in range(self.size):
                r,g,b = self.rgb.getpixel(((x + startPoint) * self.times, (y + startPoint) * self.times))
                sys.stdout.write(self.white if r > 127 else self.black)
            print self.white
        print self.white * (self.size + 2)

if __name__ == '__main__':
    q = QRCode(os.path.join(os.path.pardir, 'log', 'QR.jpg'), 37, 3, 'BLACK')
    q.print_qr()
