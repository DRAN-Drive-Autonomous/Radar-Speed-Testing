import cv2
import numpy as np

startX = 20
startY = 839
endX = 300
endY = 1060

img1 = cv2.imread("./temp.png")
img2 = cv2.imread("./resultSpeed.png")
img3 = cv2.imread("./resultRadarDeNoise.png")
img1[startY:endY, startX:endX] = [0, 0, 0]
img1 = cv2.resize(img1, (256, 256))
finalImg = np.zeros((384, 256, 3), dtype="uint8")
finalImg[:256, :, :] = img1
finalImg[256:384, :128, :] = img2
finalImg[256:384, 128:, :] = img3

cv2.imwrite("./final.png", finalImg)