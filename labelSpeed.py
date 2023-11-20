import cv2
import numpy as np
import pytesseract
import re

startX = 125
startY = 843
endX = 173
endY = 869

# startX = 128
# startY = 256
# endX = 256
# endY = 384

img = cv2.imread("./temp2.png", 0)
img = img[startY:endY, startX:endX]
cv2.imwrite("./speed.png", img)

img = cv2.resize(img, (256, 128))

print(img.shape)
# Convert image to grayscale
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Apply threshold to convert to binary image
img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
# for j, y in enumerate(img):
#     for i, x in enumerate(y):
#         if x > 150:
#             img[j][i] = 255
#         else:
#             img[j][i] = 0

cv2.imwrite("./resultSpeed.png", img)

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
# out_below = pytesseract.image_to_string(img)

# Simply extracting text from image
custom_config = r'-l eng --oem 3 --psm 6' 
out_below = pytesseract.image_to_string(img,config=custom_config)
out_below = re.sub("[^0-9]", "", out_below)
# print(out_below)
out_below.replace("\n", "")
out_below = float(out_below) / 10
print(out_below)