import cv2
import numpy as np

startX = 28
startY = 873
endX = 300
endY = 1045

img = cv2.imread("./temp.png", 0)
img = img[startY:endY, startX:endX]
cv2.imwrite("./radar.png", img)

for j, y in enumerate(img):
    for i, x in enumerate(y):
        if x > 120:
            img[j][i] = 255
        else:
            img[j][i] = 0

cv2.imwrite("./resultRadarNoise.png", img)

kernel = np.ones((3, 3), np.uint8)
img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel, iterations=1)

for j, y in enumerate(img):
    for i, x in enumerate(y):
        img [j][i] = abs(255 - x)

kernel = np.ones((3, 3), np.uint8)
img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel, iterations=1)

for j, y in enumerate(img):
    for i, x in enumerate(y):
        img [j][i] = abs(255 - x)

cv2.imwrite("./resultRadarDeNoise.png", img)