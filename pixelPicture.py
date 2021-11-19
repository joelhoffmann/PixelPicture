import random
from threading import Thread
import numpy as np
import cv2

img = np.zeros((200, 200, 3), np.uint8)


def randomPixelColor(pixelX, pixelY):
    img[pixelX, pixelY] = (random.randrange(0, 2) * 128, random.randrange(0, 2) * 128, random.randrange(0, 2) * 128)


def randomPixel(input):
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

    def startAddPrecisePoint(self, x, y):
        self.xKoord = x
        self.yKoord = y

    def move(self):
        self.xKoord = randomPixel(self.xKoord)
        self.yKoord = randomPixel(self.yKoord)

        if np.all(img[self.xKoord, self.yKoord] == 0):
            randomPixelColor(self.xKoord, self.yKoord)


class pixManager:
    def __init__(self, img):
        self.manager = []
        self.img = img

    def newPixel(self, amount):
        for i in range(amount):
            self.manager.append(pixel(self.img))

    def addPixel(self, object):
        self.manager.append(object)

    def removePixel(self, index):
        if index > len(self.manager) - 1:
            print("index is out of bounce of manager")
        else:
            self.manager.remove(index)

    def moveAllPixel(self):
        for pixelM in self.manager:
            pixelM.move()

    def getLengthOfManager(self):
        return len(self.manager)

    def getPixel(self, index):
        return self.manager[index]

    def splitPixel(self, indexOfPixel):
        mother = self.manager[indexOfPixel]
        daughter = pixel(self.img)
        daughter.startAddPrecisePoint(mother.xKoord, mother.yKoord)
        self.addPixel(daughter)


def main():
    pM = pixManager(img)
    pM.newPixel(1)
    round = 0;
    randomRound = random.randrange(100, 1000)
    while True:
        round += 1
        pM.moveAllPixel()

        cv2.imshow("image", img)
        cv2.waitKey(1)

        if round == randomRound:
            pM.splitPixel(random.randrange(0, pM.getLengthOfManager()))
            round = 0


main()

""""
if __name__  == '__main__':
    #img = np.zeros((1000, 1000, 3), np.uint8)


    thread1 = Thread(target=row, args=((random.randrange(0, img.shape[0] - 1),random.randrange(0, img.shape[1] - 1))))
    thread1.start()
    #thread2 = Thread(target=row, args=((random.randrange(0, img.shape[0] - 1),random.randrange(0, img.shape[1] - 1)))).start()

"""""
