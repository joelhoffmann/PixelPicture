import pixel

class pixManager:
    def __init__(self, img):
        self.manager = []
        self.img = img

    def newPixel(self, amount):
        for i in range(amount):
            self.manager.append(pixel.pixel(self.img))

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
        daughter = pixel.pixel(self.img)
        daughter.startAddPrecisePoint(mother.xKoord, mother.yKoord)
        self.addPixel(daughter)

