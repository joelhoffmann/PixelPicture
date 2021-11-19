import random
import numpy as np


def randomPixelColor(pixelX, pixelY, img):
    img[pixelX, pixelY] = (random.randrange(0, 2) * 128, random.randrange(0, 2) * 128, random.randrange(0, 2) * 128)


def randomPixel(input, img):
    input += random.choice([-1, 1])
    if input < 0:
        input = 0
    if input > img.shape[0] - 1:
        input = img.shape[0] - 1
    return input


class pixel:
    def __init__(self, img):
        self.xKoord = random.randrange(0, img.shape[0])
        self.yKoord = random.randrange(0, img.shape[0])
        self.shapex1 = 0
        self.shapex2 = 0
        self.img = img

    def startAddPrecisePoint(self, x, y):
        self.xKoord = x
        self.yKoord = y

    def niceColorMashup(self, xKoord, yKoord):
        red = 255
        green = 0 + xKoord
        return (0,green,red)

    def move(self):
        self.xKoord = randomPixel(self.xKoord, self.img)
        self.yKoord = randomPixel(self.yKoord, self.img)

        if np.all(self.img[self.xKoord, self.yKoord] == 0):
            self.img[self.xKoord, self.yKoord] = self.niceColorMashup(self.xKoord, self.yKoord)
            #randomPixelColor(self.xKoord, self.yKoord, self.img)
