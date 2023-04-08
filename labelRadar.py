import cv2
import numpy as np

startX = 28
startY = 873
endX = 300
endY = 1045

img = cv2.imread("./temp.png")
img = img[startY:endY, startX:endX]
cv2.imwrite("./radar.png", img)



for j, y in enumerate(img):
    for i, x in enumerate(y):
        if x[0] == 243 and x[1] == 84 and x[2] == 168:
            img[j][i] = 255
        else:
            img[j][i] = 0


cv2.imwrite("./resultRadarNoise.png", img)

kernel = np.ones((11, 11), np.uint8)
img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel, iterations=1)

img = cv2.resize(img, (128, 128))

for j, y in enumerate(img):
    for i, x in enumerate(y):
        if x[0] != 0:
            img[j][i] = 255
        else:
            img[j][i] = 0

cv2.imwrite("./resultRadarDeNoise.png", img)

img = cv2.imread("./resultRadarDeNoise.png", 0)
cv2.imwrite("./resultRadarDeNoise.png", img)