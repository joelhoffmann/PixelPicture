import random
from threading import Thread
import numpy as np
import cv2

import pixelManager

img = np.zeros((200, 200, 3), np.uint8)


def main():
    pM = pixelManager.pixManager(img)
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
