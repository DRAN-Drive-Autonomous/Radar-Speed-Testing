import cv2
import numpy as np
import pytesseract

startX = 125
startY = 843
endX = 173
endY = 869

img = cv2.imread("./temp.png", 0)
img = img[startY:endY, startX:endX]
cv2.imwrite("./speed.png", img)

img = cv2.resize(img, (128, 128))
for j, y in enumerate(img):
    for i, x in enumerate(y):
        if x > 150:
            img[j][i] = 255
        else:
            img[j][i] = 0

cv2.imwrite("./resultSpeed.png", img)

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
out_below = pytesseract.image_to_string(img)
out_below.replace("\n", "")
out_below = float(out_below)
print(out_below)